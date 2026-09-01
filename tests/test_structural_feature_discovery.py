import pytest

from runtime.feature_discovery import FeatureDiscoveryError, ground_structural_hints_to_pa03_candidates


def hint_set():
    return {
        "structural_snapshot_id": "struct:spc@r1",
        "non_authoritative": True,
        "truncated": False,
        "hints": [
            {
                "repository_id": "repo:rule-engine",
                "observation_ids": ["so:3", "so:2"],
                "relation_types": ["MESSAGE_CONSUME"],
                "evidence_refs": ["repo:rule-engine@ccc333:consumer.java"],
                "non_authoritative": True,
            },
            {
                "repository_id": "repo:spc-rule-service",
                "observation_ids": ["so:1"],
                "relation_types": ["HTTP_CALL"],
                "evidence_refs": ["repo:spc-rule-service@aaa111:client.java"],
                "non_authoritative": True,
            },
        ],
    }


def inventory():
    return [
        {
            "repository_id": "repo:spc-rule-service",
            "product_scope": "product:spc",
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
            "pa03_asset_ref_id": "pa03:repo:spc-rule-service@7",
        },
        {
            "repository_id": "repo:rule-engine",
            "product_scope": "product:spc",
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
            "pa03_asset_ref_id": "pa03:repo:rule-engine@5",
        },
        {
            "repository_id": "repo:other-product",
            "product_scope": "product:apc",
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
            "pa03_asset_ref_id": "pa03:repo:other-product@1",
        },
    ]


def test_structural_hints_are_grounded_to_active_pa03_identity_and_keep_existing_basis():
    result = ground_structural_hints_to_pa03_candidates(
        hint_set(), inventory(), allowed_product_scope=["product:spc"], max_candidates=10
    )
    assert [x["repository_id"] for x in result["candidate_augmentations"]] == [
        "repo:rule-engine",
        "repo:spc-rule-service",
    ]
    for candidate in result["candidate_augmentations"]:
        assert candidate["basis"] == "LAYER2_PA03"
        assert candidate["pa03_asset_ref_id"].startswith("pa03:")
        assert candidate["structural_observation_ids"]
        assert candidate["structural_snapshot_id"] == "struct:spc@r1"
    serialized = repr(result)
    for forbidden in ("CONFIRMED", "EXCLUDED", "SPEC_READY", "ChangeSurfaceSet"):
        assert forbidden not in serialized


def test_unknown_or_out_of_scope_hint_is_not_promoted_to_candidate():
    hints = hint_set()
    hints["hints"].extend(
        [
            {
                "repository_id": "repo:missing",
                "observation_ids": ["so:missing"],
                "relation_types": ["HTTP_CALL"],
                "evidence_refs": [],
                "non_authoritative": True,
            },
            {
                "repository_id": "repo:other-product",
                "observation_ids": ["so:other"],
                "relation_types": ["HTTP_CALL"],
                "evidence_refs": [],
                "non_authoritative": True,
            },
        ]
    )
    result = ground_structural_hints_to_pa03_candidates(
        hints, inventory(), allowed_product_scope=["product:spc"], max_candidates=10
    )
    assert {x["repository_id"] for x in result["candidate_augmentations"]} == {
        "repo:rule-engine",
        "repo:spc-rule-service",
    }
    codes = {d["code"] for d in result["diagnostics"]}
    assert codes == {"OUT_OF_PRODUCT_SCOPE", "UNRESOLVED_PA03_IDENTITY"}
    assert result["incomplete"] is True


def test_ineligible_pa03_lifecycle_does_not_ground_structural_hint():
    items = inventory()
    items[0]["validity_state"] = "STALE"
    result = ground_structural_hints_to_pa03_candidates(
        hint_set(), items, allowed_product_scope=["product:spc"], max_candidates=10
    )
    assert [x["repository_id"] for x in result["candidate_augmentations"]] == ["repo:rule-engine"]
    assert any(d["code"] == "INELIGIBLE_PA03_LIFECYCLE" for d in result["diagnostics"])


def test_candidate_augmentations_are_deterministic_deduplicated_and_bounded():
    hints = hint_set()
    hints["hints"].append(dict(hints["hints"][1]))
    result = ground_structural_hints_to_pa03_candidates(
        hints, list(reversed(inventory())), allowed_product_scope=["product:spc"], max_candidates=1
    )
    assert len(result["candidate_augmentations"]) == 1
    assert result["truncated"] is True
    assert result["incomplete"] is True
    assert any(d["code"] == "MAX_CANDIDATES" for d in result["diagnostics"])


def test_invalid_authoritative_hint_shape_fails_closed():
    hints = hint_set()
    hints["non_authoritative"] = False
    with pytest.raises(FeatureDiscoveryError):
        ground_structural_hints_to_pa03_candidates(
            hints, inventory(), allowed_product_scope=["product:spc"], max_candidates=10
        )
