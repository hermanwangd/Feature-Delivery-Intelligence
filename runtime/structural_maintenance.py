"""Maintain Product integration for Structural Intelligence deltas.

Structural deltas may create maintenance review signals only. Existing Layer 2
governance owns lifecycle and publication decisions.
"""

from __future__ import annotations

from copy import deepcopy


class StructuralMaintenanceError(ValueError):
    """Raised when structural-maintenance input violates FDI boundaries."""


def _fail(message: str) -> None:
    raise StructuralMaintenanceError(message)


def _repos(observation: dict) -> set[str]:
    result = set()
    for node in (observation.get("from", {}), observation.get("to", {})):
        repository_id = node.get("repository_id")
        if repository_id:
            result.add(repository_id)
    return result


def derive_structural_maintenance_signals(
    structural_delta: dict,
    affected_assets: list[dict],
    *,
    high_value_relation_types: list[str],
    max_signals: int,
) -> dict:
    if not isinstance(structural_delta, dict) or structural_delta.get("non_authoritative") is not True:
        _fail("StructuralDelta must be explicitly non_authoritative")
    if not isinstance(affected_assets, list):
        _fail("affected_assets must be a list")
    if not isinstance(high_value_relation_types, list) or not high_value_relation_types:
        _fail("high_value_relation_types must be non-empty")
    if not isinstance(max_signals, int) or max_signals <= 0:
        _fail("max_signals must be a positive integer")

    high_value = set(high_value_relation_types)
    diagnostics = []
    candidate_signals = []

    for change_kind, key in (("ADDED", "added"), ("REMOVED", "removed")):
        observations = structural_delta.get(key)
        if not isinstance(observations, list):
            _fail(f"StructuralDelta.{key} must be a list")
        for observation in observations:
            relation_type = observation.get("relation_type")
            observation_id = observation.get("observation_id")
            if not relation_type or not observation_id:
                _fail("changed structural observations require relation_type and observation_id")
            if observation.get("non_authoritative") is not True:
                _fail("changed structural observations must remain non_authoritative")
            if relation_type not in high_value:
                diagnostics.append({"code": "LOW_VALUE_RELATION_SKIPPED", "observation_id": observation_id})
                continue
            observation_repositories = _repos(observation)
            for asset in affected_assets:
                if not isinstance(asset, dict) or not asset.get("asset_ref_id"):
                    _fail("affected asset entries require asset_ref_id")
                asset_repositories = set(asset.get("repository_ids", []))
                asset_relations = set(asset.get("relation_types", []))
                if not observation_repositories.intersection(asset_repositories):
                    continue
                if asset_relations and relation_type not in asset_relations:
                    continue
                if asset.get("publication_state") != "PUBLISHED" or asset.get("validity_state") != "ACTIVE":
                    diagnostics.append(
                        {
                            "code": "ASSET_NOT_ACTIVE",
                            "affected_asset_ref_id": asset["asset_ref_id"],
                            "observation_id": observation_id,
                        }
                    )
                    continue
                candidate_signals.append(
                    {
                        "signal_id": f"maintenance:{change_kind.lower()}:{asset['asset_ref_id']}:{observation_id}",
                        "affected_asset_ref_id": asset["asset_ref_id"],
                        "change_kind": change_kind,
                        "relation_type": relation_type,
                        "observation_id": observation_id,
                        "repository_ids": sorted(observation_repositories),
                        "evidence_refs": sorted(set(observation.get("evidence_refs", []))),
                        "before_snapshot_id": structural_delta.get("before_snapshot_id"),
                        "after_snapshot_id": structural_delta.get("after_snapshot_id"),
                        "proposed_action": "REVIEW_REALIZATION",
                        "requires_governance_decision": True,
                    }
                )

    # Deduplicate deterministic duplicates caused by multiple asset selectors.
    by_id = {signal["signal_id"]: signal for signal in candidate_signals}
    signals = [by_id[key] for key in sorted(by_id)]
    truncated = len(signals) > max_signals
    incomplete = truncated
    if truncated:
        diagnostics.append({"code": "MAX_SIGNALS", "max_signals": max_signals})
        signals = signals[:max_signals]
    diagnostics.sort(key=lambda item: (item["code"], item.get("observation_id", ""), item.get("affected_asset_ref_id", "")))
    return {
        "signals": deepcopy(signals),
        "diagnostics": diagnostics,
        "truncated": truncated,
        "incomplete": incomplete,
        "requires_governance": bool(signals),
    }
