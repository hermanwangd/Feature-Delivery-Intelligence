import copy
import pytest

from runtime.product_semantics import (
    ContractError,
    resolve_layer1_product_semantics_ref,
    validate_product_semantics_asset,
)


def valid_asset():
    return {
        "fdi_asset_version": "0.1",
        "asset_id": "pa01:spc",
        "asset_family": "PRODUCT",
        "asset_type": "PA-01_MINIMAL_PRODUCT_SEMANTICS",
        "asset_revision": 3,
        "descriptor_ref": "descriptor:pa01:spc@3",
        "content_ref": "content:pa01:spc@3",
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "owner": "SPC Product Owner",
        "maintenance_mode": "CURATED",
        "publication_policy": "HUMAN_APPROVAL",
        "scope": {
            "products": ["SPC"],
            "systems": [],
            "repositories": [],
            "environments": [],
        },
        "authority_dimensions": ["DURABLE_CONSTRAINT"],
        "trust_profile": {
            "provenance": "DIRECT",
            "review": "REVIEWED",
            "verification": "VERIFIED",
            "authorization": "EXPLICIT",
        },
        "as_of": "git:product-catalog@abc123",
        "source_refs": ["catalog:spc@2026-09-01"],
        "dependency_refs": [],
        "freshness_policy": {"mode": "SOURCE_CHANGE", "ttl": None},
        "supersedes": None,
        "invalidation_triggers": [
            {
                "trigger_type": "SOURCE_CHANGED",
                "source_scope": "catalog:spc",
                "effect": "RECHECK_REQUIRED",
            },
            {
                "trigger_type": "SCOPE_CHANGED",
                "source_scope": "capability:CLR",
                "effect": "SCOPED_RECORD",
            },
        ],
        "selection_metadata": {"terms": ["SPC", "control limit"], "applicability": ["product:SPC"]},
        "product": {"product_id": "SPC", "name": "SPC Platform"},
        "sub_products": [
            {"sub_product_id": "LIMITS", "parent_id": "SPC", "name": "Chart & Limit Management"},
            {"sub_product_id": "LIMIT_RESOLUTION", "parent_id": "LIMITS", "name": "Limit Resolution"},
        ],
        "capabilities": [
            {
                "capability_id": "CLR",
                "parent_id": "LIMIT_RESOLUTION",
                "name": "Control Limit Resolution",
                "scope_statement": "Resolve the applicable control limit for the measurement context.",
                "semantic_refs": ["domain:spc/chamber-match@12"],
            }
        ],
    }


def test_variable_depth_product_hierarchy_is_valid():
    asset = valid_asset()
    assert validate_product_semantics_asset(asset) is asset


def test_invalid_parent_fails_closed():
    asset = valid_asset()
    asset["capabilities"][0]["parent_id"] = "UNKNOWN"
    with pytest.raises(ContractError, match="unknown semantic parent"):
        validate_product_semantics_asset(asset)


def test_sub_product_cycle_fails_closed():
    asset = valid_asset()
    asset["sub_products"][0]["parent_id"] = "LIMIT_RESOLUTION"
    with pytest.raises(ContractError, match="cycle"):
        validate_product_semantics_asset(asset)


def test_duplicate_published_active_revision_in_lineage_fails_closed():
    asset = valid_asset()
    prior = copy.deepcopy(asset)
    prior["asset_revision"] = 2
    prior["descriptor_ref"] = "descriptor:pa01:spc@2"
    prior["content_ref"] = "content:pa01:spc@2"
    with pytest.raises(ContractError, match="one active lineage"):
        validate_product_semantics_asset(asset, existing_assets=[prior])


@pytest.mark.parametrize(
    ("publication_state", "validity_state"),
    [("DRAFT", "NOT_APPLICABLE"), ("PUBLISHED", "STALE"), ("PUBLISHED", "SUPERSEDED")],
)
def test_layer1_resolution_rejects_ineligible_lifecycle(publication_state, validity_state):
    asset = valid_asset()
    asset["publication_state"] = publication_state
    asset["validity_state"] = validity_state
    validate_product_semantics_asset(asset)
    with pytest.raises(ContractError, match=r"PUBLISHED \+ ACTIVE"):
        resolve_layer1_product_semantics_ref(asset)


@pytest.mark.parametrize(
    ("publication_state", "validity_state"),
    [
        ("DRAFT", "ACTIVE"),
        ("DRAFT", "STALE"),
        ("PUBLISHED", "NOT_APPLICABLE"),
        ("RETIRED", "ACTIVE"),
    ],
)
def test_illegal_common_product_asset_lifecycle_fails_closed(publication_state, validity_state):
    asset = valid_asset()
    asset["publication_state"] = publication_state
    asset["validity_state"] = validity_state
    with pytest.raises(ContractError, match="illegal Product Asset lifecycle"):
        validate_product_semantics_asset(asset)


def test_exact_product_asset_ref_projection_preserves_governed_metadata():
    asset = valid_asset()
    ref = resolve_layer1_product_semantics_ref(asset)
    assert ref == {
        "asset_id": "pa01:spc",
        "asset_revision": 3,
        "descriptor_ref": "descriptor:pa01:spc@3",
        "content_ref": "content:pa01:spc@3",
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "as_of": "git:product-catalog@abc123",
        "authority_dimensions": ["DURABLE_CONSTRAINT"],
        "trust_profile": {
            "provenance": "DIRECT",
            "review": "REVIEWED",
            "verification": "VERIFIED",
            "authorization": "EXPLICIT",
        },
        "scope_match": {
            "products": ["SPC"],
            "systems": [],
            "repositories": [],
            "environments": [],
        },
    }


@pytest.mark.parametrize(
    ("facet", "bad_value"),
    [
        ("provenance", "CURATED"),
        ("review", "APPROVED"),
        ("verification", "CONFIRMED"),
        ("authorization", "AUTHORIZED"),
    ],
)
def test_trust_profile_uses_exact_governing_enums(facet, bad_value):
    asset = valid_asset()
    asset["trust_profile"][facet] = bad_value
    with pytest.raises(ContractError, match=f"invalid trust_profile {facet}"):
        validate_product_semantics_asset(asset)
