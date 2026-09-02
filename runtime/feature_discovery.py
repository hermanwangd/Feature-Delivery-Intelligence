"""Structural Intelligence contribution to FDI Feature Discovery.

This module only produces PA-03-grounded candidate augmentations. It does not
create current-feature Change Surface truth.
"""

from __future__ import annotations

from collections import defaultdict
from copy import deepcopy


class FeatureDiscoveryError(ValueError):
    """Raised when Structural Discovery hints violate FDI authority boundaries."""


def _fail(message: str) -> None:
    raise FeatureDiscoveryError(message)


def ground_structural_hints_to_pa03_candidates(
    hint_set: dict,
    pa03_inventory: list[dict],
    *,
    allowed_product_scope: list[str],
    max_candidates: int,
) -> dict:
    if not isinstance(hint_set, dict) or hint_set.get("non_authoritative") is not True:
        _fail("StructuralDiscoveryHintSet must be explicitly non_authoritative")
    if not isinstance(hint_set.get("hints"), list):
        _fail("StructuralDiscoveryHintSet.hints must be a list")
    if not isinstance(pa03_inventory, list):
        _fail("PA-03 inventory must be a list")
    if not isinstance(allowed_product_scope, list) or not allowed_product_scope:
        _fail("allowed_product_scope must be non-empty")
    if not isinstance(max_candidates, int) or max_candidates <= 0:
        _fail("max_candidates must be a positive integer")

    allowed_scope = set(allowed_product_scope)
    inventory_by_repo = {}
    for item in pa03_inventory:
        if not isinstance(item, dict) or not item.get("repository_id"):
            _fail("PA-03 inventory entries require repository_id")
        if item["repository_id"] in inventory_by_repo:
            _fail(f"duplicate PA-03 repository identity: {item['repository_id']}")
        inventory_by_repo[item["repository_id"]] = item

    hints_by_repo = defaultdict(lambda: {"observation_ids": set(), "relation_types": set(), "evidence_refs": set()})
    for hint in hint_set["hints"]:
        if not isinstance(hint, dict) or hint.get("non_authoritative") is not True:
            _fail("every structural hint must be non_authoritative")
        repository_id = hint.get("repository_id")
        if not repository_id:
            _fail("structural hint repository_id is required")
        hints_by_repo[repository_id]["observation_ids"].update(hint.get("observation_ids", []))
        hints_by_repo[repository_id]["relation_types"].update(hint.get("relation_types", []))
        hints_by_repo[repository_id]["evidence_refs"].update(hint.get("evidence_refs", []))

    diagnostics = []
    candidates = []
    incomplete = bool(hint_set.get("truncated"))

    for repository_id in sorted(hints_by_repo):
        pa03 = inventory_by_repo.get(repository_id)
        if pa03 is None:
            diagnostics.append({"code": "UNRESOLVED_PA03_IDENTITY", "repository_id": repository_id})
            incomplete = True
            continue
        if pa03.get("product_scope") not in allowed_scope:
            diagnostics.append(
                {
                    "code": "OUT_OF_PRODUCT_SCOPE",
                    "repository_id": repository_id,
                    "product_scope": pa03.get("product_scope"),
                }
            )
            incomplete = True
            continue
        if pa03.get("publication_state") != "PUBLISHED" or pa03.get("validity_state") != "ACTIVE":
            diagnostics.append(
                {
                    "code": "INELIGIBLE_PA03_LIFECYCLE",
                    "repository_id": repository_id,
                    "publication_state": pa03.get("publication_state"),
                    "validity_state": pa03.get("validity_state"),
                }
            )
            incomplete = True
            continue
        if not pa03.get("pa03_asset_ref_id"):
            diagnostics.append({"code": "MISSING_PA03_REF", "repository_id": repository_id})
            incomplete = True
            continue

        hint = hints_by_repo[repository_id]
        candidates.append(
            {
                "repository_id": repository_id,
                "basis": "LAYER2_PA03",
                "pa03_asset_ref_id": pa03["pa03_asset_ref_id"],
                "structural_snapshot_id": hint_set.get("structural_snapshot_id"),
                "structural_observation_ids": sorted(hint["observation_ids"]),
                "structural_relation_types": sorted(hint["relation_types"]),
                "structural_evidence_refs": sorted(hint["evidence_refs"]),
                "candidate_only": True,
            }
        )

    truncated = len(candidates) > max_candidates
    if truncated:
        diagnostics.append({"code": "MAX_CANDIDATES", "max_candidates": max_candidates})
        incomplete = True
        candidates = candidates[:max_candidates]

    diagnostics.sort(key=lambda item: (item["code"], item.get("repository_id", "")))
    return {
        "candidate_augmentations": deepcopy(candidates),
        "diagnostics": diagnostics,
        "incomplete": incomplete,
        "truncated": truncated,
    }


def compose_feature_discovery_candidate_view(
    realization_result: dict,
    structural_result: dict,
    *,
    max_candidates: int,
) -> dict:
    """Compose Product Realization and Structural Intelligence candidates.

    This is an internal non-canonical candidate view. Every repository keeps the
    existing `LAYER2_PA03` basis; no current-feature disposition is produced.
    """
    if not isinstance(max_candidates, int) or max_candidates <= 0:
        _fail("max_candidates must be a positive integer")
    if not isinstance(realization_result, dict) or not isinstance(realization_result.get("repositories"), list):
        _fail("realization_result.repositories must be a list")
    if not isinstance(structural_result, dict) or not isinstance(structural_result.get("candidate_augmentations"), list):
        _fail("structural_result.candidate_augmentations must be a list")

    by_repo: dict[str, dict] = {}

    def entry(repository_id: str) -> dict:
        return by_repo.setdefault(
            repository_id,
            {
                "repository_id": repository_id,
                "basis": "LAYER2_PA03",
                "sources": [],
                "realization_paths": [],
                "structural_snapshot_ids": [],
                "structural_observation_ids": [],
                "structural_relation_types": [],
                "structural_evidence_refs": [],
                "pa03_asset_ref_ids": [],
                "candidate_only": True,
            },
        )

    for item in realization_result["repositories"]:
        if item.get("basis") != "LAYER2_PA03" or not item.get("repository_id"):
            _fail("realization candidates must be PA-03-grounded")
        target = entry(item["repository_id"])
        target["sources"].append("PRODUCT_REALIZATION")
        target["realization_paths"].extend(deepcopy(item.get("paths", [])))

    for item in structural_result["candidate_augmentations"]:
        if item.get("basis") != "LAYER2_PA03" or not item.get("repository_id"):
            _fail("structural candidates must be PA-03-grounded")
        if item.get("candidate_only") is not True:
            _fail("structural candidate augmentation must remain candidate-only")
        target = entry(item["repository_id"])
        target["sources"].append("STRUCTURAL_INTELLIGENCE")
        if item.get("structural_snapshot_id"):
            target["structural_snapshot_ids"].append(item["structural_snapshot_id"])
        target["structural_observation_ids"].extend(item.get("structural_observation_ids", []))
        target["structural_relation_types"].extend(item.get("structural_relation_types", []))
        target["structural_evidence_refs"].extend(item.get("structural_evidence_refs", []))
        if item.get("pa03_asset_ref_id"):
            target["pa03_asset_ref_ids"].append(item["pa03_asset_ref_id"])

    source_order = {"PRODUCT_REALIZATION": 0, "STRUCTURAL_INTELLIGENCE": 1}
    repositories = []
    for repository_id in sorted(by_repo):
        item = by_repo[repository_id]
        item["sources"] = sorted(set(item["sources"]), key=lambda value: source_order[value])
        item["realization_paths"] = sorted(
            item["realization_paths"],
            key=lambda path: (path.get("relation_ids", []), path.get("start_node_id", ""), path.get("node_ids", [])),
        )
        for key in (
            "structural_snapshot_ids",
            "structural_observation_ids",
            "structural_relation_types",
            "structural_evidence_refs",
            "pa03_asset_ref_ids",
        ):
            item[key] = sorted(set(item[key]))
        repositories.append(item)

    diagnostics = []
    for source in (realization_result.get("diagnostics", []), structural_result.get("diagnostics", [])):
        diagnostics.extend(deepcopy(source))

    truncated = len(repositories) > max_candidates
    if truncated:
        diagnostics.append({"code": "MAX_CANDIDATES", "max_candidates": max_candidates})
        repositories = repositories[:max_candidates]
    diagnostics.sort(key=lambda item: (item.get("code", ""), repr(sorted(item.items()))))
    return {
        "repositories": repositories,
        "diagnostics": diagnostics,
        "incomplete": bool(realization_result.get("incomplete") or structural_result.get("incomplete") or truncated),
        "truncated": truncated,
        "candidate_only": True,
    }
