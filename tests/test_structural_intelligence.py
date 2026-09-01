import copy

import pytest

from runtime.structural_intelligence import (
    StructuralIntelligenceError,
    derive_discovery_hints,
    diff_observations,
    normalize_observations,
    validate_snapshot_ref,
    validate_snapshot_binding,
    validate_structural_query,
)


def snapshot():
    return {
        "snapshot_id": "struct:spc@2026-08-31T120000Z",
        "provider": {"name": "GRAFEL", "version": "0.x-pinned"},
        "adapter_version": "fdi-grafel-adapter@0.1",
        "source_snapshots": [
            {"repository": "repo:spc-rule-service", "revision": "abc123"},
            {"repository": "repo:wafer-context", "revision": "def456"},
        ],
        "created_at": "2026-08-31T12:00:00Z",
    }


def binding_for(s):
    return validate_snapshot_binding(s, {
        "provider_scope_id": "grafel-group:spc-test",
        "provider_ref": s["snapshot_id"],
        "queryability": "QUERYABLE",
        "freshness": "FROZEN_INDEXED",
        "repositories": [
            {
                "repository": item["repository"],
                "indexed_revision": item["revision"],
                "queryable": True,
                "head_revision": None,
            }
            for item in s["source_snapshots"]
        ],
    })


def query():
    return {
        "query_id": "sq:SPC-123:1",
        "snapshot_id": snapshot()["snapshot_id"],
        "scope": {"products": ["SPC"], "repositories": ["repo:spc-rule-service", "repo:wafer-context"]},
        "seed": {"type": "COMPONENT", "id": "component:sampling-service"},
        "allowed_relation_types": ["HTTP_CALL", "SCHEMA_DEPENDENCY"],
        "max_depth": 3,
        "max_nodes": 100,
        "max_edges": 200,
        "max_paths": 20,
        "max_result_bytes": 65536,
    }


def provider_records():
    return [
        {
            "from": {"type": "COMPONENT", "id": "component:sampling-service", "repository_id": "repo:spc-rule-service"},
            "relation_type": "HTTP_CALL",
            "to": {"type": "COMPONENT", "id": "component:wafer-context", "repository_id": "repo:wafer-context"},
            "evidence_refs": ["repo:spc-rule-service@abc123:src/SamplingClient.java"],
            "provider_observation_id": "grafel-edge-99",
            "provider_assessment": {"score": 0.91, "method": "cross_repo_http_resolver"},
        },
        {
            "from": {"type": "COMPONENT", "id": "component:sampling-service", "repository_id": "repo:spc-rule-service"},
            "relation_type": "SCHEMA_DEPENDENCY",
            "to": {"type": "SCHEMA", "id": "schema:wafer-context", "repository_id": "repo:wafer-context"},
            "evidence_refs": ["repo:wafer-context@def456:openapi.yaml"],
            "provider_observation_id": "grafel-edge-100",
        },
    ]


def test_snapshot_requires_provider_adapter_and_exact_repository_revisions():
    assert validate_snapshot_ref(snapshot())["snapshot_id"] == snapshot()["snapshot_id"]
    for mutation in (
        lambda s: s.pop("provider"),
        lambda s: s.pop("adapter_version"),
        lambda s: s.update(source_snapshots=[]),
        lambda s: s["source_snapshots"][0].pop("revision"),
    ):
        bad = copy.deepcopy(snapshot())
        mutation(bad)
        with pytest.raises(StructuralIntelligenceError):
            validate_snapshot_ref(bad)


def test_query_must_match_snapshot_and_be_finitely_bounded():
    validated = validate_structural_query(query(), snapshot())
    assert validated["max_depth"] == 3
    assert validated["allowed_relation_types"] == ["HTTP_CALL", "SCHEMA_DEPENDENCY"]

    for field in ("max_depth", "max_nodes", "max_edges", "max_paths", "max_result_bytes"):
        bad = query()
        bad[field] = 0
        with pytest.raises(StructuralIntelligenceError):
            validate_structural_query(bad, snapshot())

    bad = query()
    bad["snapshot_id"] = "struct:future"
    with pytest.raises(StructuralIntelligenceError):
        validate_structural_query(bad, snapshot())

    bad = query()
    bad["allowed_relation_types"] = []
    with pytest.raises(StructuralIntelligenceError):
        validate_structural_query(bad, snapshot())


def test_normalization_is_deterministic_provider_isolated_and_non_authoritative():
    first = normalize_observations(provider_records(), snapshot(), query(), binding_attestation=binding_for(snapshot()))
    second = normalize_observations(list(reversed(provider_records())), snapshot(), query(), binding_attestation=binding_for(snapshot()))
    assert first == second
    assert len(first["observations"]) == 2
    obs = first["observations"][0]
    assert obs["structural_snapshot_id"] == snapshot()["snapshot_id"]
    assert obs["provider"]["name"] == "GRAFEL"
    assert obs["provider"]["adapter_version"] == "fdi-grafel-adapter@0.1"
    assert obs["provider"]["provider_observation_id"].startswith("grafel-edge-")
    serialized = repr(first)
    for forbidden in ("CONFIRMED", "EXCLUDED", "SPEC_READY", "ChangeSurfaceSet"):
        assert forbidden not in serialized


def test_observations_outside_query_relation_allowlist_fail_closed():
    records = provider_records()
    records[0]["relation_type"] = "LOCAL_IMPORT"
    with pytest.raises(StructuralIntelligenceError):
        normalize_observations(records, snapshot(), query(), binding_attestation=binding_for(snapshot()))


def test_discovery_hints_are_repository_oriented_bounded_and_non_authoritative():
    observations = normalize_observations(provider_records(), snapshot(), query(), binding_attestation=binding_for(snapshot()))
    hints = derive_discovery_hints(observations, max_hints=4)
    assert [h["repository_id"] for h in hints["hints"]] == ["repo:spc-rule-service", "repo:wafer-context"]
    assert all(h["non_authoritative"] is True for h in hints["hints"])
    assert all(h["observation_ids"] for h in hints["hints"])
    serialized = repr(hints)
    for forbidden in ("CONFIRMED", "EXCLUDED", "SPEC_READY", "ChangeSurfaceSet"):
        assert forbidden not in serialized

    with pytest.raises(StructuralIntelligenceError):
        derive_discovery_hints(observations, max_hints=0)


def test_structural_diff_is_deterministic_and_identifies_added_removed_edges():
    before = normalize_observations(provider_records()[:1], snapshot(), query(), binding_attestation=binding_for(snapshot()))
    after_snapshot = snapshot()
    after_snapshot["snapshot_id"] = "struct:spc@2026-09-01T120000Z"
    after_query = query(); after_query["snapshot_id"] = after_snapshot["snapshot_id"]
    after = normalize_observations(provider_records()[1:], after_snapshot, after_query, binding_attestation=binding_for(after_snapshot))
    delta = diff_observations(before, after)
    assert len(delta["added"]) == 1
    assert len(delta["removed"]) == 1
    assert delta["added"][0]["relation_type"] == "SCHEMA_DEPENDENCY"
    assert delta["removed"][0]["relation_type"] == "HTTP_CALL"
    assert delta["unchanged"] == []


def test_structural_runtime_schema_declares_runtime_support_artifacts_not_product_assets():
    import json
    from pathlib import Path

    schema_path = Path(__file__).resolve().parents[1] / "03-structural-intelligence" / "contracts" / "structural-runtime-contracts.schema.json"
    schema = json.loads(schema_path.read_text())
    assert schema["title"] == "FDI Structural Intelligence Runtime Support Contracts v0.4.7.1"
    assert set(schema["$defs"]) >= {
        "StructuralSnapshotRef",
        "StructuralQuery",
        "StructuralObservation",
        "StructuralDiscoveryHint",
        "StructuralDelta",
    }
    serialized = json.dumps(schema)
    assert "ProductAssetFamily" not in serialized
    assert "CONFIRMED" not in serialized
    assert "SPEC_READY" not in serialized
