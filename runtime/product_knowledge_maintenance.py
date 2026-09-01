"""Governed Product Knowledge maintenance-path conformance runtime.

This module models only the minimum PA-01 maintenance boundary required by
v0.4.6.2. It produces/changes local Product Asset state; it never grants
publication authority to an Agent or Product Team Onboarding and never mutates
Layer 1 artifacts.
"""

from __future__ import annotations

from copy import deepcopy

from .product_semantics import validate_product_semantics_asset


class MaintenanceError(ValueError):
    """Raised when a maintenance action would cross a governance boundary."""


def create_semantic_draft(candidate: dict, *, proposer: str, source_snapshot_refs: list[str]) -> dict:
    """Create a PA-01 semantic proposal that is always DRAFT + NOT_APPLICABLE."""
    if not proposer:
        raise MaintenanceError("proposer is required")
    if not source_snapshot_refs or any(not ref for ref in source_snapshot_refs):
        raise MaintenanceError("at least one exact source snapshot ref is required")

    draft = deepcopy(candidate)
    draft["publication_state"] = "DRAFT"
    draft["validity_state"] = "NOT_APPLICABLE"
    draft["publication_policy"] = "HUMAN_APPROVAL"
    draft["source_refs"] = list(source_snapshot_refs)
    draft["proposed_by"] = proposer

    # Proposal generation cannot manufacture organizational review/authorization.
    trust = draft.setdefault("trust_profile", {})
    if proposer.startswith("agent:"):
        trust["review"] = "UNREVIEWED"
        trust["authorization"] = "NONE"
        draft["reviewed_by"] = []

    validate_product_semantics_asset(draft)
    return draft


def publish_semantic_revision(
    draft: dict,
    *,
    actor: str,
    authorized_publishers: set[str],
    existing_assets=(),
) -> dict:
    """Publish an eligible PA-01 DRAFT only through its accountable owner."""
    validate_product_semantics_asset(draft)
    if (draft.get("publication_state"), draft.get("validity_state")) != (
        "DRAFT",
        "NOT_APPLICABLE",
    ):
        raise MaintenanceError("only a DRAFT + NOT_APPLICABLE revision may be published")
    if draft.get("publication_policy") != "HUMAN_APPROVAL":
        raise MaintenanceError("PA-01 Product Semantics requires HUMAN_APPROVAL")

    owner = draft.get("owner")
    if not actor or actor != owner or actor not in authorized_publishers:
        raise MaintenanceError("accountable publication authority is required")

    published = deepcopy(draft)
    published["publication_state"] = "PUBLISHED"
    published["validity_state"] = "ACTIVE"
    published["published_by"] = actor
    published["trust_profile"]["review"] = "REVIEWED"
    published["trust_profile"]["authorization"] = "EXPLICIT"
    reviewed_by = published.setdefault("reviewed_by", [])
    if actor not in reviewed_by:
        reviewed_by.append(actor)
    validate_product_semantics_asset(published, existing_assets=existing_assets)
    return published


def mark_product_knowledge_stale(asset: dict, *, trigger: str) -> dict:
    """Apply only a lifecycle validity transition when a declared trigger fires."""
    validate_product_semantics_asset(asset)
    if (asset.get("publication_state"), asset.get("validity_state")) != (
        "PUBLISHED",
        "ACTIVE",
    ):
        raise MaintenanceError("only PUBLISHED + ACTIVE Product Knowledge may transition to STALE")

    declared = {
        item.get("trigger_type")
        for item in asset.get("invalidation_triggers", [])
        if isinstance(item, dict)
    }
    if trigger not in declared:
        raise MaintenanceError("staleness trigger is not declared by the Asset invalidation contract")

    stale = deepcopy(asset)
    stale["validity_state"] = "STALE"
    stale.setdefault("lifecycle_events", []).append(
        {"from": "ACTIVE", "to": "STALE", "reason": trigger}
    )
    validate_product_semantics_asset(stale)
    return stale


def supersede_semantic_revision(
    current_active: dict,
    replacement_draft: dict,
    *,
    actor: str,
    authorized_publishers: set[str],
) -> tuple[dict, dict]:
    """Return an old SUPERSEDED revision and a new PUBLISHED+ACTIVE successor."""
    validate_product_semantics_asset(current_active)
    validate_product_semantics_asset(replacement_draft)
    if (current_active.get("publication_state"), current_active.get("validity_state")) != (
        "PUBLISHED",
        "ACTIVE",
    ):
        raise MaintenanceError("supersession requires a current PUBLISHED + ACTIVE revision")
    if (replacement_draft.get("publication_state"), replacement_draft.get("validity_state")) != (
        "DRAFT",
        "NOT_APPLICABLE",
    ):
        raise MaintenanceError("replacement must be DRAFT + NOT_APPLICABLE")
    if replacement_draft.get("asset_id") != current_active.get("asset_id"):
        raise MaintenanceError("replacement must preserve asset_id lineage")
    if replacement_draft.get("scope") != current_active.get("scope"):
        raise MaintenanceError("replacement must preserve declared scope partition")
    if replacement_draft.get("asset_revision", 0) <= current_active.get("asset_revision", 0):
        raise MaintenanceError("replacement asset_revision must increase")

    old = deepcopy(current_active)
    old["validity_state"] = "SUPERSEDED"
    old.setdefault("lifecycle_events", []).append(
        {
            "from": "ACTIVE",
            "to": "SUPERSEDED",
            "reason": f"superseded-by:{replacement_draft['asset_revision']}",
        }
    )
    validate_product_semantics_asset(old)

    replacement = deepcopy(replacement_draft)
    replacement["supersedes"] = {
        "asset_id": current_active["asset_id"],
        "asset_revision": current_active["asset_revision"],
    }
    new_active = publish_semantic_revision(
        replacement,
        actor=actor,
        authorized_publishers=authorized_publishers,
        existing_assets=[old],
    )
    return old, new_active


def onboarding_request_maintenance(gap: dict, *, requested_by: str) -> dict:
    """Turn an onboarding gap into a bounded request, never a publication action."""
    if not requested_by:
        raise MaintenanceError("requested_by is required")
    target_profile = gap.get("target_profile")
    if target_profile not in {"PA-01", "PA-03", "PA-05"}:
        raise MaintenanceError("onboarding may request only declared MVP Product Knowledge profiles")
    gap_id = gap.get("gap_id")
    if not gap_id or not gap.get("reason"):
        raise MaintenanceError("gap_id and reason are required")
    return {
        "request_id": f"maintenance-request:{gap_id}",
        "status": "REQUESTED",
        "action": "CREATE" if "missing" in gap["reason"].lower() else "REFRESH",
        "trigger": "HUMAN_REQUEST",
        "target_profile": target_profile,
        "reason": gap["reason"],
        "requested_by": requested_by,
        "may_publish": False,
    }
