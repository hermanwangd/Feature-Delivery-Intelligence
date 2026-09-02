from runtime.product_semantics import resolve_layer1_product_semantics_ref, validate_product_semantics_asset


def exact_common_descriptor_asset():
    return {
        "fdi_asset_version": "0.1",
        "asset_id": "pa01:spc",
        "asset_family": "PRODUCT",
        "asset_type": "PA-01_MINIMAL_PRODUCT_SEMANTICS",
        "asset_revision": 1,
        "descriptor_ref": "descriptor:pa01:spc@1",
        "content_ref": "content:pa01:spc@1",
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
        "as_of": "catalog:spc@r1",
        "source_refs": ["catalog:spc@r1"],
        "dependency_refs": [],
        "freshness_policy": {"mode": "SOURCE_CHANGE", "ttl": None},
        "supersedes": None,
        "invalidation_triggers": [
            {
                "trigger_type": "SOURCE_CHANGED",
                "source_scope": "catalog:spc",
                "effect": "RECHECK_REQUIRED",
            }
        ],
        "selection_metadata": {"terms": ["SPC"], "applicability": ["product:SPC"]},
        "reviewed_by": ["SPC Frontier Team"],
        "product": {"product_id": "SPC", "name": "SPC Platform"},
        "sub_products": [],
        "capabilities": [
            {
                "capability_id": "CLR",
                "parent_id": "SPC",
                "name": "Control Limit Resolution",
                "scope_statement": "Resolve applicable control limits.",
                "semantic_refs": ["domain:spc/chamber-match@12"],
            }
        ],
    }


def test_pa01_reuses_exact_approved_common_descriptor_fields():
    asset = exact_common_descriptor_asset()
    assert validate_product_semantics_asset(asset) is asset
    ref = resolve_layer1_product_semantics_ref(asset)
    assert ref["asset_id"] == "pa01:spc"
    assert ref["scope_match"]["products"] == ["SPC"]
