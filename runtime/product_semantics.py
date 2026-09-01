"""Minimal PA-01 Product Semantics conformance runtime for the v0.4.6.2 overlay.

The runtime deliberately reuses the approved Layer 2 ProductAssetDescriptor
vocabulary. PA-01 content adds only Product/Sub-product/Capability semantics;
repository realization remains a PA-03-oriented concern.
"""

from __future__ import annotations

from copy import deepcopy
import json


class ContractError(ValueError):
    """Raised when a Product Knowledge contract would otherwise fail open."""


_REQUIRED_TRUST_FACETS = {"provenance", "review", "verification", "authorization"}
_ALLOWED_TRUST = {
    "provenance": {"DIRECT", "DERIVED", "ASSERTED"},
    "review": {"UNREVIEWED", "REVIEWED"},
    "verification": {"NOT_VERIFIED", "VERIFIED"},
    "authorization": {"NONE", "SOURCE_INHERITED", "EXPLICIT"},
}
_ALLOWED_AUTHORITY_DIMENSIONS = {
    "DURABLE_CONSTRAINT",
    "CURRENT_BEHAVIOR_SUPPORT",
    "RATIONALE_SUPPORT",
}
_ALLOWED_MAINTENANCE_MODES = {"CURATED", "DERIVED", "REFERENCED"}
_ALLOWED_PUBLICATION_POLICIES = {"HUMAN_APPROVAL", "RULE_BASED_AUTO", "SOURCE_REFERENCE"}
_ALLOWED_FRESHNESS_MODES = {"UNTIL_SUPERSEDED", "SOURCE_CHANGE", "TTL", "EVENT_DRIVEN", "MANUAL"}
_LEGAL_LIFECYCLE = {
    ("DRAFT", "NOT_APPLICABLE"),
    ("PUBLISHED", "ACTIVE"),
    ("PUBLISHED", "STALE"),
    ("PUBLISHED", "SUPERSEDED"),
    ("RETIRED", "NOT_APPLICABLE"),
}
_REQUIRED_SCOPE_KEYS = {"products", "systems", "repositories", "environments"}


def _require_nonempty(asset: dict, key: str):
    value = asset.get(key)
    if value in (None, "", [], {}):
        raise ContractError(f"missing required field: {key}")
    return value


def _scope_partition(scope: dict) -> str:
    """Produce a stable equality key for the approved declared scope object."""
    return json.dumps(scope, sort_keys=True, separators=(",", ":"))


def _validate_common_descriptor(asset: dict) -> None:
    if asset.get("fdi_asset_version") != "0.1":
        raise ContractError("fdi_asset_version must be 0.1")
    if asset.get("asset_family") != "PRODUCT":
        raise ContractError("PA-01 asset_family must be PRODUCT")
    if asset.get("asset_type") != "PA-01_MINIMAL_PRODUCT_SEMANTICS":
        raise ContractError("unsupported PA-01 asset_type")

    revision = _require_nonempty(asset, "asset_revision")
    if not isinstance(revision, int) or isinstance(revision, bool) or revision <= 0:
        raise ContractError("asset_revision must be a positive integer")

    _require_nonempty(asset, "asset_id")
    _require_nonempty(asset, "descriptor_ref")
    _require_nonempty(asset, "content_ref")
    _require_nonempty(asset, "owner")
    _require_nonempty(asset, "as_of")

    lifecycle = (asset.get("publication_state"), asset.get("validity_state"))
    if lifecycle not in _LEGAL_LIFECYCLE:
        raise ContractError(
            f"illegal Product Asset lifecycle: {lifecycle[0]} + {lifecycle[1]}"
        )

    if asset.get("maintenance_mode") not in _ALLOWED_MAINTENANCE_MODES:
        raise ContractError("unsupported maintenance_mode")
    if asset.get("publication_policy") not in _ALLOWED_PUBLICATION_POLICIES:
        raise ContractError("unsupported publication_policy")

    scope = _require_nonempty(asset, "scope")
    if not isinstance(scope, dict) or set(scope) != _REQUIRED_SCOPE_KEYS:
        raise ContractError("scope must contain products/systems/repositories/environments")
    if any(not isinstance(scope[key], list) for key in _REQUIRED_SCOPE_KEYS):
        raise ContractError("all scope partitions must be lists")
    if not scope["products"]:
        raise ContractError("PA-01 scope.products must be non-empty")

    authority_dimensions = asset.get("authority_dimensions")
    if not isinstance(authority_dimensions, list) or not authority_dimensions:
        raise ContractError("authority_dimensions must be a non-empty list")
    unknown_authority = set(authority_dimensions) - _ALLOWED_AUTHORITY_DIMENSIONS
    if unknown_authority:
        raise ContractError(f"unsupported authority dimension: {sorted(unknown_authority)[0]}")

    trust = _require_nonempty(asset, "trust_profile")
    if not isinstance(trust, dict) or set(trust) != _REQUIRED_TRUST_FACETS:
        raise ContractError("faceted trust profile must contain exactly the four approved facets")
    for facet, allowed in _ALLOWED_TRUST.items():
        if trust.get(facet) not in allowed:
            raise ContractError(f"invalid trust_profile {facet}: {trust.get(facet)}")

    source_refs = asset.get("source_refs")
    if not isinstance(source_refs, list) or not source_refs:
        raise ContractError("source_refs must be a non-empty list")
    if not isinstance(asset.get("dependency_refs"), list):
        raise ContractError("dependency_refs must be a list")

    freshness = _require_nonempty(asset, "freshness_policy")
    if not isinstance(freshness, dict) or freshness.get("mode") not in _ALLOWED_FRESHNESS_MODES:
        raise ContractError("unsupported freshness_policy mode")
    if "ttl" not in freshness:
        raise ContractError("freshness_policy.ttl must be explicit")
    if freshness["mode"] == "TTL" and not freshness.get("ttl"):
        raise ContractError("TTL freshness_policy requires ttl")

    triggers = asset.get("invalidation_triggers")
    if not isinstance(triggers, list) or not triggers:
        raise ContractError("invalidation_triggers must be a non-empty list")
    for trigger in triggers:
        if not isinstance(trigger, dict) or not trigger.get("trigger_type"):
            raise ContractError("each invalidation trigger requires trigger_type")

    selection = _require_nonempty(asset, "selection_metadata")
    if not isinstance(selection.get("terms"), list) or not isinstance(selection.get("applicability"), list):
        raise ContractError("selection_metadata requires terms/applicability lists")


def _validate_semantic_content(asset: dict) -> None:
    product = _require_nonempty(asset, "product")
    product_id = product.get("product_id")
    if not product_id:
        raise ContractError("product_id is required")

    declared_products = asset["scope"]["products"]
    if product_id not in declared_products:
        raise ContractError("product_id must be included in scope.products")

    sub_products = asset.get("sub_products", [])
    capabilities = asset.get("capabilities", [])
    if not isinstance(sub_products, list) or not isinstance(capabilities, list):
        raise ContractError("sub_products and capabilities must be lists")

    sub_ids = [item.get("sub_product_id") for item in sub_products]
    capability_ids = [item.get("capability_id") for item in capabilities]
    all_ids = [product_id, *sub_ids, *capability_ids]
    if any(not node_id for node_id in all_ids):
        raise ContractError("semantic node ids must be non-empty")
    if len(set(all_ids)) != len(all_ids):
        raise ContractError("semantic node ids must be unique")

    semantic_parent_ids = {product_id, *sub_ids}
    parent_by_sub: dict[str, str] = {}
    for item in sub_products:
        child = item["sub_product_id"]
        parent = item.get("parent_id")
        if parent not in semantic_parent_ids:
            raise ContractError(f"unknown semantic parent: {parent}")
        if child == parent:
            raise ContractError("semantic hierarchy cycle detected")
        parent_by_sub[child] = parent

    for start in sub_ids:
        seen = set()
        cursor = start
        while cursor != product_id:
            if cursor in seen:
                raise ContractError("semantic hierarchy cycle detected")
            seen.add(cursor)
            cursor = parent_by_sub.get(cursor)
            if cursor is None:
                raise ContractError("sub-product hierarchy does not terminate at PRODUCT")

    for item in capabilities:
        parent = item.get("parent_id")
        if parent not in semantic_parent_ids:
            raise ContractError(f"unknown semantic parent: {parent}")
        if not item.get("scope_statement"):
            raise ContractError("capability scope_statement is required")
        refs = item.get("semantic_refs", [])
        if not isinstance(refs, list):
            raise ContractError("semantic_refs must be a list of exact governed refs")


def validate_product_semantics_asset(asset: dict, *, existing_assets=()):
    """Validate the approved common descriptor plus minimum PA-01 semantic hierarchy."""
    if not isinstance(asset, dict):
        raise ContractError("asset must be an object")

    _validate_common_descriptor(asset)
    _validate_semantic_content(asset)

    if asset.get("publication_state") == "PUBLISHED" and asset.get("validity_state") == "ACTIVE":
        partition = _scope_partition(asset["scope"])
        for prior in existing_assets:
            if not isinstance(prior, dict):
                continue
            prior_scope = prior.get("scope")
            if (
                prior.get("asset_id") == asset["asset_id"]
                and isinstance(prior_scope, dict)
                and _scope_partition(prior_scope) == partition
                and prior.get("publication_state") == "PUBLISHED"
                and prior.get("validity_state") == "ACTIVE"
                and prior.get("asset_revision") != asset["asset_revision"]
            ):
                raise ContractError(
                    "one active lineage violated: another PUBLISHED + ACTIVE revision exists"
                )

    return asset


def resolve_layer1_product_semantics_ref(asset: dict) -> dict:
    """Project an exact eligible ProductAssetRef without creating feature truth."""
    validate_product_semantics_asset(asset)
    if asset.get("publication_state") != "PUBLISHED" or asset.get("validity_state") != "ACTIVE":
        raise ContractError("Layer 1 normal resolution requires PUBLISHED + ACTIVE Product Knowledge")
    return {
        "asset_id": asset["asset_id"],
        "asset_revision": asset["asset_revision"],
        "descriptor_ref": asset["descriptor_ref"],
        "content_ref": asset["content_ref"],
        "publication_state": asset["publication_state"],
        "validity_state": asset["validity_state"],
        "as_of": asset["as_of"],
        "authority_dimensions": list(asset["authority_dimensions"]),
        "trust_profile": deepcopy(asset["trust_profile"]),
        "scope_match": deepcopy(asset["scope"]),
    }
