import pytest

from runtime.grafel_adapter import GrafelAdapter, GrafelAdapterError


def snapshot():
    return {
        "snapshot_id": "struct:spc@r1",
        "provider": {"name": "GRAFEL", "version": "0.1.x"},
        "adapter_version": "fdi-grafel-adapter@0.1",
        "source_snapshots": [{"repository": "repo:a", "revision": "aaa111"}],
        "created_at": "2026-09-01T00:00:00Z",
    }


def query(query_id="sq:1"):
    return {
        "query_id": query_id,
        "snapshot_id": snapshot()["snapshot_id"],
        "scope": {"products": ["SPC"], "repositories": ["repo:a"]},
        "seed": {"type": "COMPONENT", "id": "component:a"},
        "allowed_relation_types": ["HTTP_CALL"],
        "max_depth": 2,
        "max_nodes": 20,
        "max_edges": 30,
        "max_paths": 5,
        "max_result_bytes": 32768,
    }


class FakeTransport:
    def __init__(self, response=None):
        self.calls = []
        self.response = response if response is not None else {"raw": True}

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return self.response


def mapper(raw, *, operation, snapshot_ref, structural_query):
    assert raw == {"raw": True}
    assert operation in {"find", "expand", "trace", "diff", "orient"}
    if operation == "orient":
        return raw
    if operation == "diff":
        return {"added": [], "removed": [], "unchanged": []}
    record = {
        "from": {"type": "COMPONENT", "id": "component:a", "repository_id": "repo:a"},
        "relation_type": "HTTP_CALL",
        "to": {"type": "COMPONENT", "id": "component:b", "repository_id": "repo:a"},
        "evidence_refs": ["repo:a@aaa111:a.py:10"],
        "provider_observation_id": "edge:1",
        "provider_assessment": {"confidence": 0.9},
    }
    if operation == "trace":
        record["path_id"] = "path:1"
    return [record]


def binding_attestor(snapshot_ref):
    return {
        "provider_scope_id": "grafel-group:test",
        "provider_ref": snapshot_ref["snapshot_id"],
        "queryability": "QUERYABLE",
        "freshness": "FROZEN_INDEXED",
        "repositories": [
            {
                "repository": item["repository"],
                "provider_repository": "repo-a",
                "indexed_revision": item["revision"],
                "queryable": True,
                "head_revision": None,
            }
            for item in snapshot_ref["source_snapshots"]
        ],
    }


def test_reference_adapter_hides_grafel_tool_names_behind_fdi_operations():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)

    result = adapter.find(query(), snapshot())
    assert transport.calls[0][0] == "grafel_find"
    assert transport.calls[0][1]["group"] == "grafel-group:test"
    assert transport.calls[0][1]["ref"] == snapshot()["snapshot_id"]
    assert result["observations"][0]["provider"]["name"] == "GRAFEL"
    assert result["observations"][0]["provider"]["provider_observation_id"] == "edge:1"
    assert result["observations"][0]["provider"]["provider_assessment"] == {"confidence": 0.9}
    assert result["observations"][0]["non_authoritative"] is True


def test_adapter_current_default_tool_mapping_is_confined_to_adapter():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    expected = {
        "orient": "grafel_orient",
        "find": "grafel_find",
        "expand": "grafel_subgraph",
        "trace": "grafel_find_paths",
        "diff": "grafel_diff",
    }
    assert adapter.tool_mapping == expected


def test_expand_trace_and_diff_translate_fdi_bounds_to_provider_payloads():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)

    adapter.expand(query("sq:expand"), snapshot())
    tool, payload = transport.calls[-1]
    assert tool == "grafel_subgraph"
    assert payload["depth"] == 2
    assert payload["max_nodes"] == 20
    assert payload["entity_id"] == "component:a"

    trace_query = query("sq:trace")
    trace_query["target"] = {"type": "COMPONENT", "id": "component:z"}
    adapter.trace(trace_query, snapshot())
    tool, payload = transport.calls[-1]
    assert tool == "grafel_find_paths"
    assert payload["from"] == "component:a"
    assert payload["to"] == "component:z"
    assert payload["max_hops"] == 2

    before = snapshot()
    before["snapshot_id"] = "struct:before"
    after = snapshot()
    after["snapshot_id"] = "struct:after"
    after["source_snapshots"][0]["revision"] = "def456"
    delta = adapter.diff(
        {
            "query_id": "sdq:1",
            "repository": "repo:a",
            "allowed_relation_types": ["HTTP_CALL"],
            "max_edges": 30,
            "max_result_bytes": 32768,
        },
        before,
        after,
    )
    tool, payload = transport.calls[-1]
    assert tool == "grafel_diff"
    assert payload == {
        "group": "grafel-group:test",
            "repo": "repo-a",
        "ref_a": "struct:before",
        "ref_b": "struct:after",
        "aspect": "refs",
    }
    assert delta["non_authoritative"] is True


def test_orient_is_source_bound_and_non_authoritative():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    result = adapter.orient({"view": "overview", "repositories": ["repo:a"]}, snapshot())
    assert result["provider_result"] == {"raw": True}
    assert result["non_authoritative"] is True
    assert result["binding_attestation_id"].startswith("sba:")
    assert transport.calls[-1][0] == "grafel_orient"


def test_adapter_rejects_unpinned_or_invalid_provider_identity():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    bad = snapshot()
    bad["provider"]["name"] = "OTHER"
    with pytest.raises(GrafelAdapterError):
        adapter.find(query(), bad)

    with pytest.raises(GrafelAdapterError):
        GrafelAdapter(transport, response_mapper=None, binding_attestor=binding_attestor)
