import json

import pytest

from runtime.code_intelligence_provider import SnapshotBindingAttestor
from runtime.grafel_binding_attestor import (
    GrafelBindingAttestorError,
    GrafelDashboardGroupMetadataClient,
    GrafelSnapshotBindingAttestor,
    StaticGrafelSnapshotRouteResolver,
)
from runtime.structural_intelligence import validate_snapshot_binding


def snapshot():
    return {
        "snapshot_id": "struct:f001-cutoff",
        "provider": {"name": "GRAFEL", "version": "0.x"},
        "adapter_version": "fdi-grafel-adapter@0.4",
        "source_snapshots": [
            {"repository": "repo:a", "revision": "aaaaaaaaaaaa1111111111111111111111111111"},
            {"repository": "repo:b", "revision": "bbbbbbbbbbbb2222222222222222222222222222"},
        ],
        "created_at": "2026-09-02T00:00:00Z",
    }


class FakeTransport:
    def __init__(self, response=None):
        self.calls = []
        self.response = response or {
            "group": "spc-f001-replay",
            "indexed_ref": "fdi/f001-cutoff",
            "queryable": True,
            "warming": False,
            "indexing": 0,
        }

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return self.response


class FakeGroupMetadataClient:
    def __init__(self, group):
        self.group = group
        self.calls = []

    def get_group(self, group_id):
        self.calls.append(group_id)
        return self.group


def group_metadata(*, ref="fdi/f001-cutoff", sha_a="aaaaaaaaaaaa", sha_b="bbbbbbbbbbbb"):
    return {
        "id": "spc-f001-replay",
        "repos": [
            {"slug": "repo-a", "indexed_ref": ref, "indexed_sha": sha_a},
            {"slug": "repo-b", "indexed_ref": ref, "indexed_sha": sha_b},
        ],
    }


def route_resolver(*, freshness="FROZEN_INDEXED"):
    return StaticGrafelSnapshotRouteResolver(
        {
            "struct:f001-cutoff": {
                "provider_scope_id": "spc-f001-replay",
                "provider_ref": "fdi/f001-cutoff",
                "freshness": freshness,
                "repository_map": {"repo:a": "repo-a", "repo:b": "repo-b"},
            }
        }
    )


def test_attestor_proves_exact_multirepo_frozen_scope_and_is_protocol_compatible():
    transport = FakeTransport()
    metadata = FakeGroupMetadataClient(group_metadata())
    attestor = GrafelSnapshotBindingAttestor(
        transport,
        route_resolver=route_resolver(),
        group_metadata_client=metadata,
    )

    assert isinstance(attestor, SnapshotBindingAttestor)
    state = attestor(snapshot())
    verified = validate_snapshot_binding(snapshot(), state)

    assert transport.calls == [
        (
            "grafel_orient",
            {"view": "me", "group": "spc-f001-replay", "ref": "fdi/f001-cutoff"},
        )
    ]
    assert metadata.calls == ["spc-f001-replay"]
    assert verified["binding_state"] == "VERIFIED"
    assert verified["provider_route"] == {
        "scope_id": "spc-f001-replay",
        "ref": "fdi/f001-cutoff",
    }
    assert {x["provider_repository"] for x in verified["repositories"]} == {"repo-a", "repo-b"}
    assert verified["freshness"] == "FROZEN_INDEXED"
    assert {x["indexed_revision"] for x in verified["repositories"]} == {
        "aaaaaaaaaaaa1111111111111111111111111111",
        "bbbbbbbbbbbb2222222222222222222222222222",
    }


def test_attestor_fails_closed_when_grafel_graph_revision_does_not_match_canonical_snapshot():
    attestor = GrafelSnapshotBindingAttestor(
        FakeTransport(),
        route_resolver=route_resolver(),
        group_metadata_client=FakeGroupMetadataClient(group_metadata(sha_b="cccccccccccc")),
    )

    with pytest.raises(GrafelBindingAttestorError, match="indexed SHA"):
        attestor(snapshot())


def test_attestor_fails_closed_when_graph_is_warming_or_provider_ref_is_wrong():
    warming = GrafelSnapshotBindingAttestor(
        FakeTransport({"group": "spc-f001-replay", "indexed_ref": "fdi/f001-cutoff", "queryable": True, "warming": True, "indexing": 0}),
        route_resolver=route_resolver(),
        group_metadata_client=FakeGroupMetadataClient(group_metadata()),
    )
    with pytest.raises(GrafelBindingAttestorError, match="warming"):
        warming(snapshot())

    wrong_ref = GrafelSnapshotBindingAttestor(
        FakeTransport(),
        route_resolver=route_resolver(),
        group_metadata_client=FakeGroupMetadataClient(group_metadata(ref="other/ref")),
    )
    with pytest.raises(GrafelBindingAttestorError, match="indexed_ref"):
        wrong_ref(snapshot())


def test_attestor_requires_explicit_repository_identity_mapping_and_full_repository_set():
    bad_routes = StaticGrafelSnapshotRouteResolver(
        {
            "struct:f001-cutoff": {
                "provider_scope_id": "spc-f001-replay",
                "provider_ref": "fdi/f001-cutoff",
                "freshness": "FROZEN_INDEXED",
                "repository_map": {"repo:a": "repo-a"},
            }
        }
    )
    attestor = GrafelSnapshotBindingAttestor(
        FakeTransport(),
        route_resolver=bad_routes,
        group_metadata_client=FakeGroupMetadataClient(group_metadata()),
    )
    with pytest.raises(GrafelBindingAttestorError, match="repository_map"):
        attestor(snapshot())


def test_dashboard_group_metadata_client_uses_explicit_base_url_and_unwraps_v2_data():
    calls = []

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self):
            return json.dumps({"data": group_metadata()}).encode("utf-8")

    def opener(request, timeout):
        calls.append((request.full_url, timeout))
        return Response()

    client = GrafelDashboardGroupMetadataClient(
        "http://127.0.0.1:43123",
        opener=opener,
        timeout_seconds=3.5,
    )
    result = client.get_group("spc/f001 replay")

    assert calls == [("http://127.0.0.1:43123/api/v2/groups/spc%2Ff001%20replay", 3.5)]
    assert result["repos"][0]["indexed_sha"] == "aaaaaaaaaaaa"


def test_concrete_attestor_composes_with_grafel_adapter_and_routes_query_after_attestation():
    from runtime.grafel_adapter import GrafelAdapter

    class CombinedTransport(FakeTransport):
        def invoke(self, tool_name, payload):
            self.calls.append((tool_name, payload))
            if tool_name == "grafel_orient":
                return self.response
            if tool_name == "grafel_find":
                return {"records": []}
            raise AssertionError(tool_name)

    def mapper(raw, *, operation, snapshot_ref, structural_query):
        if operation == "find":
            return []
        raise AssertionError(operation)

    transport = CombinedTransport()
    attestor = GrafelSnapshotBindingAttestor(
        transport,
        route_resolver=route_resolver(),
        group_metadata_client=FakeGroupMetadataClient(group_metadata()),
    )
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=attestor)
    structural_query = {
        "query_id": "sq:f001",
        "snapshot_id": "struct:f001-cutoff",
        "scope": {"products": ["SPC"], "repositories": ["repo:a", "repo:b"]},
        "seed": {"type": "COMPONENT", "id": "sampling-service"},
        "allowed_relation_types": ["HTTP_CALL"],
        "max_depth": 2,
        "max_nodes": 20,
        "max_edges": 30,
        "max_paths": 5,
        "max_result_bytes": 32768,
    }

    result = adapter.find(structural_query, snapshot())

    assert [tool for tool, _ in transport.calls] == ["grafel_orient", "grafel_find"]
    assert transport.calls[1][1]["group"] == "spc-f001-replay"
    assert transport.calls[1][1]["ref"] == "fdi/f001-cutoff"
    assert result["binding_attestation_id"].startswith("sba:")
    assert result["observations"] == []


def test_attestor_decodes_mcp_text_envelope_before_validating_route_identity():
    wrapped_wrong_ref = {
        "content": [
            {
                "type": "text",
                "text": json.dumps(
                    {
                        "group": "spc-f001-replay",
                        "indexed_ref": "wrong/ref",
                        "queryable": True,
                        "warming": False,
                        "indexing": 0,
                    }
                ),
            }
        ]
    }
    attestor = GrafelSnapshotBindingAttestor(
        FakeTransport(wrapped_wrong_ref),
        route_resolver=route_resolver(),
        group_metadata_client=FakeGroupMetadataClient(group_metadata()),
    )

    with pytest.raises(GrafelBindingAttestorError, match="different provider ref"):
        attestor(snapshot())
