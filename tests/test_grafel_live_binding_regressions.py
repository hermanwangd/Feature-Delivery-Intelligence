import pytest

from runtime.grafel_adapter import GrafelAdapter, GrafelAdapterError
from runtime.grafel_binding_attestor import (
    GrafelBindingAttestorError,
    GrafelSnapshotBindingAttestor,
    StaticGrafelSnapshotRouteResolver,
)
from runtime.structural_intelligence import validate_snapshot_binding


REV_A = "aaaaaaaaaaaa1111111111111111111111111111"
REV_B = "bbbbbbbbbbbb2222222222222222222222222222"


def snapshot(snapshot_id="struct:current", revision=REV_A):
    return {
        "snapshot_id": snapshot_id,
        "provider": {"name": "GRAFEL", "version": "0.x"},
        "adapter_version": "fdi-grafel-adapter@0.4",
        "source_snapshots": [{"repository": "repo:orders", "revision": revision}],
        "created_at": "2026-09-02T00:00:00Z",
    }


def structural_query(snapshot_id="struct:current"):
    return {
        "query_id": "sq:orders",
        "snapshot_id": snapshot_id,
        "scope": {"products": ["shop"], "repositories": ["repo:orders"]},
        "seed": {"type": "COMPONENT", "id": "orders-api"},
        "allowed_relation_types": ["HTTP_CALL"],
        "max_depth": 2,
        "max_nodes": 20,
        "max_edges": 30,
        "max_paths": 5,
        "max_result_bytes": 32768,
    }


def route(snapshot_id="struct:current", provider_ref="refs/current", repository_map=None):
    return StaticGrafelSnapshotRouteResolver(
        {
            snapshot_id: {
                "provider_scope_id": "shop-group",
                "provider_ref": provider_ref,
                "freshness": "FROZEN_INDEXED",
                "repository_map": repository_map or {"repo:orders": "orders-service"},
            }
        }
    )


def group_metadata(group_id="shop-group", *, repos=None):
    return {
        "id": group_id,
        "repos": repos
        if repos is not None
        else [
            {
                "slug": "orders-service",
                "indexed_ref": "refs/current",
                "indexed_sha": REV_A[:12],
            }
        ],
    }


class ExactTransport:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return self.response


class GroupMetadataClient:
    def __init__(self, response):
        self.response = response

    def get_group(self, group_id):
        return self.response


def attestor(orient_response, metadata=None, route_resolver=None):
    return GrafelSnapshotBindingAttestor(
        ExactTransport(orient_response),
        route_resolver=route_resolver or route(),
        group_metadata_client=GroupMetadataClient(metadata or group_metadata()),
    )


@pytest.mark.parametrize(
    "response, error",
    [
        ({}, "incomplete"),
        ({"indexed_ref": "refs/current", "queryable": True, "warming": False, "indexing": 0}, "scope"),
        ({"group": "shop-group", "queryable": True, "warming": False, "indexing": 0}, "ref"),
        (
            {
                "group": "other-group",
                "indexed_ref": "refs/current",
                "queryable": True,
                "warming": False,
                "indexing": 0,
            },
            "scope",
        ),
        (
            {
                "group": "shop-group",
                "indexed_ref": "refs/other",
                "queryable": True,
                "warming": False,
                "indexing": 0,
            },
            "ref",
        ),
    ],
)
def test_route_probe_requires_complete_exact_scope_and_ref_identity(response, error):
    with pytest.raises(GrafelBindingAttestorError, match=error):
        attestor(response)(snapshot())


@pytest.mark.parametrize(
    "response, error",
    [
        ({"group": "shop-group", "indexed_ref": "refs/current", "warming": False, "indexing": 0}, "queryable"),
        (
            {
                "group": "shop-group",
                "indexed_ref": "refs/current",
                "queryable": False,
                "warming": False,
                "indexing": 0,
            },
            "queryable",
        ),
        (
            {"group": "shop-group", "indexed_ref": "refs/current", "queryable": True, "indexing": 0},
            "warming",
        ),
        (
            {"group": "shop-group", "indexed_ref": "refs/current", "queryable": True, "warming": True, "indexing": 0},
            "warming",
        ),
        (
            {"group": "shop-group", "indexed_ref": "refs/current", "queryable": True, "warming": False},
            "indexing",
        ),
        (
            {"group": "shop-group", "indexed_ref": "refs/current", "queryable": True, "warming": False, "indexing": 1},
            "indexing",
        ),
    ],
)
def test_route_probe_requires_explicit_queryable_ready_state(response, error):
    with pytest.raises(GrafelBindingAttestorError, match=error):
        attestor(response)(snapshot())


@pytest.mark.parametrize("group_id", [None, "", "other-group"])
def test_group_metadata_requires_exact_nonempty_scope_identity(group_id):
    response = {"repos": group_metadata()["repos"]}
    if group_id is not None:
        response["id"] = group_id
    orient = {
        "group": "shop-group",
        "indexed_ref": "refs/current",
        "queryable": True,
        "warming": False,
        "indexing": 0,
    }
    with pytest.raises(GrafelBindingAttestorError, match="group metadata.*scope"):
        attestor(orient, response)(snapshot())


def test_attestor_rejects_ambiguous_mapping_and_metadata_repository_set_mismatch():
    duplicate_map = route(
        repository_map={"repo:orders": "shared-slug", "repo:billing": "shared-slug"}
    )
    multirepo = snapshot()
    multirepo["source_snapshots"].append({"repository": "repo:billing", "revision": REV_B})
    with pytest.raises(GrafelBindingAttestorError, match="unique"):
        attestor({}, route_resolver=duplicate_map)(multirepo)

    orient = {
        "group": "shop-group",
        "indexed_ref": "refs/current",
        "queryable": True,
        "warming": False,
        "indexing": 0,
    }
    extra_repo = group_metadata(
        repos=[
            *group_metadata()["repos"],
            {"slug": "unattested-service", "indexed_ref": "refs/current", "indexed_sha": REV_B[:12]},
        ]
    )
    with pytest.raises(GrafelBindingAttestorError, match="repository set"):
        attestor(orient, extra_repo)(snapshot())


class AdapterTransport:
    def __init__(self):
        self.calls = []

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return {"tool": tool_name}


def binding_state(snapshot_ref):
    provider_ref = {
        "struct:before": "refs/before",
        "struct:after": "refs/after",
    }.get(snapshot_ref["snapshot_id"], "refs/current")
    return {
        "provider_scope_id": "shop-group",
        "provider_ref": provider_ref,
        "queryability": "QUERYABLE",
        "freshness": "FROZEN_INDEXED",
        "repositories": [
            {
                "repository": "repo:orders",
                "provider_repository": "orders-service",
                "indexed_revision": snapshot_ref["source_snapshots"][0]["revision"],
                "queryable": True,
                "head_revision": None,
            }
        ],
    }


def response_mapper(raw, *, operation, snapshot_ref, structural_query):
    if operation == "orient":
        return {"repository_id": "repo:orders"}
    if operation == "diff":
        return {"added": [], "removed": [], "unchanged": []}
    return [
        {
            "from": {"type": "COMPONENT", "id": "orders-api", "repository_id": "repo:orders"},
            "relation_type": "HTTP_CALL",
            "to": {"type": "COMPONENT", "id": "payments", "repository_id": "repo:orders"},
            "evidence_refs": [f"repo:orders@{snapshot_ref['source_snapshots'][0]['revision']}:orders.py:1"],
        }
    ]


def test_adapter_uses_attested_provider_slugs_on_wire_and_preserves_fdi_repository_ids():
    transport = AdapterTransport()
    adapter = GrafelAdapter(transport, response_mapper=response_mapper, binding_attestor=binding_state)

    orient_result = adapter.orient({"view": "overview", "repositories": ["repo:orders"]}, snapshot())
    find_result = adapter.find(structural_query(), snapshot())
    before = snapshot("struct:before", REV_A)
    after = snapshot("struct:after", REV_B)
    diff_result = adapter.diff(
        {
            "query_id": "sdq:orders",
            "repository": "repo:orders",
            "allowed_relation_types": ["HTTP_CALL"],
            "max_edges": 30,
            "max_result_bytes": 32768,
        },
        before,
        after,
    )

    assert transport.calls[0][1]["repo_filter"] == ["orders-service"]
    assert transport.calls[1][1]["repo_filter"] == ["orders-service"]
    assert transport.calls[2][1]["repo"] == "orders-service"
    assert "repo:orders" not in repr(transport.calls)
    assert orient_result["provider_result"]["repository_id"] == "repo:orders"
    assert find_result["observations"][0]["from"]["repository_id"] == "repo:orders"
    assert diff_result["non_authoritative"] is True

    attestation = validate_snapshot_binding(snapshot(), binding_state(snapshot()))
    assert attestation["repositories"][0]["provider_repository"] == "orders-service"


def test_adapter_rejects_missing_or_changed_attested_provider_repository_mapping():
    transport = AdapterTransport()

    def missing_mapping(snapshot_ref):
        state = binding_state(snapshot_ref)
        state["repositories"][0].pop("provider_repository")
        return state

    adapter = GrafelAdapter(transport, response_mapper=response_mapper, binding_attestor=missing_mapping)
    with pytest.raises(GrafelAdapterError, match="provider repository mapping"):
        adapter.find(structural_query(), snapshot())

    def changed_mapping(snapshot_ref):
        state = binding_state(snapshot_ref)
        state["repositories"][0]["provider_repository"] = (
            "orders-before" if snapshot_ref["snapshot_id"] == "struct:before" else "orders-after"
        )
        return state

    adapter = GrafelAdapter(transport, response_mapper=response_mapper, binding_attestor=changed_mapping)
    with pytest.raises(GrafelAdapterError, match="same provider repository"):
        adapter.diff(
            {
                "query_id": "sdq:orders",
                "repository": "repo:orders",
                "allowed_relation_types": ["HTTP_CALL"],
                "max_edges": 30,
                "max_result_bytes": 32768,
            },
            snapshot("struct:before", REV_A),
            snapshot("struct:after", REV_B),
        )
