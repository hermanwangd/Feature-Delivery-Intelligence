import pytest

from runtime.structural_maintenance import StructuralMaintenanceError, derive_structural_maintenance_signals


def edge(relation_type, left_repo="repo:a", right_repo="repo:b", oid="so:1"):
    return {
        "observation_id": oid,
        "relation_type": relation_type,
        "from": {"type": "COMPONENT", "id": "component:a", "repository_id": left_repo},
        "to": {"type": "COMPONENT", "id": "component:b", "repository_id": right_repo},
        "evidence_refs": [f"{left_repo}@aaa:path"],
        "non_authoritative": True,
    }


def delta():
    return {
        "before_snapshot_id": "struct:r0",
        "after_snapshot_id": "struct:r1",
        "added": [edge("HTTP_CALL", oid="so:add")],
        "removed": [edge("MESSAGE_CONSUME", oid="so:remove")],
        "unchanged": [edge("LOCAL_IMPORT", oid="so:same")],
        "non_authoritative": True,
    }


def assets():
    return [
        {
            "asset_ref_id": "pa03:realization:spc@7",
            "repository_ids": ["repo:a", "repo:b"],
            "relation_types": ["HTTP_CALL", "MESSAGE_CONSUME"],
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
        },
        {
            "asset_ref_id": "pa03:unrelated@2",
            "repository_ids": ["repo:z"],
            "relation_types": ["HTTP_CALL"],
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
        },
    ]


def test_high_value_added_and_removed_relations_create_review_signals_only():
    result = derive_structural_maintenance_signals(
        delta(),
        assets(),
        high_value_relation_types=["HTTP_CALL", "MESSAGE_CONSUME", "SCHEMA_DEPENDENCY"],
        max_signals=10,
    )
    assert len(result["signals"]) == 2
    assert {s["change_kind"] for s in result["signals"]} == {"ADDED", "REMOVED"}
    assert {s["affected_asset_ref_id"] for s in result["signals"]} == {"pa03:realization:spc@7"}
    assert all(s["requires_governance_decision"] is True for s in result["signals"])
    assert all(s["proposed_action"] == "REVIEW_REALIZATION" for s in result["signals"])
    serialized = repr(result)
    for forbidden in ("publish_revision", "mark_stale", "supersede", "retire", "PUBLISHED + ACTIVE"):
        assert forbidden not in serialized


def test_unchanged_and_low_value_relations_do_not_create_signals():
    d = delta()
    d["added"] = [edge("CONFIG_DEPENDENCY", oid="so:low")]
    d["removed"] = []
    result = derive_structural_maintenance_signals(
        d, assets(), high_value_relation_types=["HTTP_CALL"], max_signals=10
    )
    assert result["signals"] == []
    assert result["diagnostics"] == [{"code": "LOW_VALUE_RELATION_SKIPPED", "observation_id": "so:low"}]


def test_ineligible_asset_is_not_silently_mutated():
    items = assets()
    items[0]["validity_state"] = "STALE"
    result = derive_structural_maintenance_signals(
        delta(), items, high_value_relation_types=["HTTP_CALL", "MESSAGE_CONSUME"], max_signals=10
    )
    assert result["signals"] == []
    assert any(d["code"] == "ASSET_NOT_ACTIVE" for d in result["diagnostics"])


def test_signal_generation_is_deterministic_and_bounded():
    result = derive_structural_maintenance_signals(
        delta(), list(reversed(assets())), high_value_relation_types=["HTTP_CALL", "MESSAGE_CONSUME"], max_signals=1
    )
    assert len(result["signals"]) == 1
    assert result["truncated"] is True
    assert result["incomplete"] is True
    assert any(d["code"] == "MAX_SIGNALS" for d in result["diagnostics"])


def test_authoritative_or_unbounded_input_fails_closed():
    bad = delta()
    bad["non_authoritative"] = False
    with pytest.raises(StructuralMaintenanceError):
        derive_structural_maintenance_signals(
            bad, assets(), high_value_relation_types=["HTTP_CALL"], max_signals=10
        )
    with pytest.raises(StructuralMaintenanceError):
        derive_structural_maintenance_signals(
            delta(), assets(), high_value_relation_types=["HTTP_CALL"], max_signals=0
        )
