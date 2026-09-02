from runtime.feature_discovery import (
    compose_feature_discovery_candidate_view,
    ground_structural_hints_to_pa03_candidates,
)
from runtime.realization_traversal import derive_repository_candidates
from runtime.structural_intelligence import derive_discovery_hints, normalize_observations, validate_snapshot_binding


def relation(rel_id, src, relation_type, dst):
    return {
        "relation_id": rel_id,
        "from": src,
        "relation_type": relation_type,
        "to": dst,
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "declared_by_profile": True,
    }


def snapshot():
    return {
        "snapshot_id": "struct:payment@t0",
        "provider": {"name": "GRAFEL", "version": "0.1.x"},
        "adapter_version": "fdi-grafel-adapter@0.1",
        "source_snapshots": [
            {"repository": "repo:checkout-api", "revision": "aaa111"},
            {"repository": "repo:ledger-service", "revision": "bbb222"},
            {"repository": "repo:notification-service", "revision": "ccc333"},
        ],
        "created_at": "2026-08-30T00:00:00Z",
    }


def structural_query():
    return {
        "query_id": "sq:F001:payment-recovery",
        "snapshot_id": snapshot()["snapshot_id"],
        "scope": {
            "products": ["PAYMENTS"],
            "repositories": ["repo:checkout-api", "repo:ledger-service", "repo:notification-service"],
        },
        "seed": {"type": "COMPONENT", "id": "component:payment-orchestrator"},
        "allowed_relation_types": ["HTTP_CALL", "MESSAGE_CONSUME"],
        "max_depth": 3,
        "max_nodes": 100,
        "max_edges": 200,
        "max_paths": 20,
        "max_result_bytes": 65536,
    }


def pa03_inventory():
    return [
        {
            "repository_id": repo,
            "product_scope": "product:payments",
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
            "pa03_asset_ref_id": f"pa03:{repo}@1",
        }
        for repo in ["repo:checkout-api", "repo:ledger-service", "repo:notification-service"]
    ]


def test_full_fdi_composes_product_realization_and_live_structure_without_current_truth_shortcut():
    capability = {"id": "capability:payment-recovery", "type": "CAPABILITY", "product_scope": "product:payments"}
    component = {"id": "component:payment-orchestrator", "type": "COMPONENT", "product_scope": "product:payments"}
    checkout = {"id": "repo:checkout-api", "type": "REPOSITORY", "product_scope": "product:payments"}
    ledger = {"id": "repo:ledger-service", "type": "REPOSITORY", "product_scope": "product:payments"}

    realization = derive_repository_candidates(
        [capability],
        [
            relation("r1", capability, "REALIZED_BY", component),
            relation("r2", component, "IMPLEMENTED_IN", checkout),
            relation("r3", component, "IMPLEMENTED_IN", ledger),
        ],
        {
            "allowed_relation_types": ["REALIZED_BY", "IMPLEMENTED_IN"],
            "max_depth": 4,
            "max_edges_examined": 20,
            "max_paths_per_repository": 4,
            "allowed_product_scope": ["product:payments"],
            "lifecycle_required": "PUBLISHED_ACTIVE",
        },
    )
    assert {x["repository_id"] for x in realization["repositories"]} == {"repo:checkout-api", "repo:ledger-service"}

    snap = snapshot()
    binding = validate_snapshot_binding(snap, {
        "provider_scope_id": "grafel-group:payments-test",
        "provider_ref": "fdi/payment-t0",
        "queryability": "QUERYABLE",
        "freshness": "FROZEN_INDEXED",
        "repositories": [
            {
                "repository": item["repository"],
                "indexed_revision": item["revision"],
                "queryable": True,
                "head_revision": None,
            }
            for item in snap["source_snapshots"]
        ],
    })
    observations = normalize_observations(
        [
            {
                "from": {"type": "COMPONENT", "id": "component:payment-orchestrator", "repository_id": "repo:checkout-api"},
                "relation_type": "HTTP_CALL",
                "to": {"type": "COMPONENT", "id": "component:ledger", "repository_id": "repo:ledger-service"},
                "evidence_refs": ["repo:checkout-api@aaa111:PaymentClient.java"],
                "provider_observation_id": "g:1",
            },
            {
                "from": {"type": "TOPIC", "id": "topic:payment-state", "repository_id": "repo:checkout-api"},
                "relation_type": "MESSAGE_CONSUME",
                "to": {"type": "COMPONENT", "id": "component:notifications", "repository_id": "repo:notification-service"},
                "evidence_refs": ["repo:notification-service@ccc333:consumer.ts"],
                "provider_observation_id": "g:2",
            },
        ],
        snap,
        structural_query(),
        binding_attestation=binding,
    )
    hints = derive_discovery_hints(observations, max_hints=10)
    structural_candidates = ground_structural_hints_to_pa03_candidates(
        hints, pa03_inventory(), allowed_product_scope=["product:payments"], max_candidates=10
    )

    combined = compose_feature_discovery_candidate_view(realization, structural_candidates, max_candidates=10)
    assert [x["repository_id"] for x in combined["repositories"]] == [
        "repo:checkout-api",
        "repo:ledger-service",
        "repo:notification-service",
    ]
    by_repo = {x["repository_id"]: x for x in combined["repositories"]}
    assert by_repo["repo:checkout-api"]["sources"] == ["PRODUCT_REALIZATION", "STRUCTURAL_INTELLIGENCE"]
    assert by_repo["repo:ledger-service"]["sources"] == ["PRODUCT_REALIZATION", "STRUCTURAL_INTELLIGENCE"]
    assert by_repo["repo:notification-service"]["sources"] == ["STRUCTURAL_INTELLIGENCE"]
    assert all(x["basis"] == "LAYER2_PA03" for x in combined["repositories"])
    assert combined["candidate_only"] is True

    serialized = repr(combined)
    for forbidden in ("CONFIRMED", "EXCLUDED", "SPEC_READY", "ChangeSurfaceSet"):
        assert forbidden not in serialized


def test_composed_candidate_view_propagates_incompleteness_and_budget():
    realization = {
        "repositories": [
            {"repository_id": "repo:a", "basis": "LAYER2_PA03", "paths": [{"relation_ids": ["r1"]}]},
            {"repository_id": "repo:b", "basis": "LAYER2_PA03", "paths": [{"relation_ids": ["r2"]}]},
        ],
        "incomplete": True,
        "diagnostics": [{"code": "MAX_DEPTH"}],
    }
    structural = {
        "candidate_augmentations": [
            {
                "repository_id": "repo:c",
                "basis": "LAYER2_PA03",
                "pa03_asset_ref_id": "pa03:repo:c@1",
                "structural_snapshot_id": "s1",
                "structural_observation_ids": ["so:1"],
                "structural_relation_types": ["HTTP_CALL"],
                "structural_evidence_refs": [],
                "candidate_only": True,
            }
        ],
        "incomplete": False,
        "diagnostics": [],
    }
    result = compose_feature_discovery_candidate_view(realization, structural, max_candidates=2)
    assert len(result["repositories"]) == 2
    assert result["truncated"] is True
    assert result["incomplete"] is True
    assert any(d["code"] == "MAX_CANDIDATES" for d in result["diagnostics"])
