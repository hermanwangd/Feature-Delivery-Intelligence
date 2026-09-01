import pytest

from runtime.feature_knowledge_plan import FeatureKnowledgePlanError, compile_feature_knowledge_plan


def root_skill():
    return {
        "skill_id": "ft-t2-delivery-spec",
        "skill_revision": "0.4.2",
        "context_requirement_templates": [
            {
                "template_id": "product-semantics-required",
                "knowledge_role": "SEMANTICS",
                "allowed_modes": ["REQUIRED"],
                "allowed_authority_dimensions": ["DURABLE_CONSTRAINT"],
                "selector_bounds": {"max_assets": 1},
                "minimum_trust": {
                    "review": "REVIEWED",
                    "verification": "VERIFIED",
                    "authorization": "EXPLICIT",
                },
                "freshness_requirement": "SOURCE_CHANGE",
                "may_promote_to_required": False,
            },
            {
                "template_id": "delivery-prior-on-demand",
                "knowledge_role": "DELIVERY_PRIOR",
                "allowed_modes": ["ON_DEMAND", "CONDITIONAL"],
                "allowed_authority_dimensions": ["RATIONALE_SUPPORT"],
                "selector_bounds": {"max_assets": 2},
                "minimum_trust": {
                    "review": "UNREVIEWED",
                    "verification": "NOT_VERIFIED",
                    "authorization": "NONE",
                },
                "freshness_requirement": "MANUAL",
                "may_promote_to_required": False,
            },
        ],
    }


def plan_item(**overrides):
    base = {
        "template_id": "product-semantics-required",
        "knowledge_role": "SEMANTICS",
        "mode": "REQUIRED",
        "authority_dimension": "DURABLE_CONSTRAINT",
        "selector": {"max_assets": 1},
        "trust_requirements": {
            "review": "REVIEWED",
            "verification": "VERIFIED",
            "authorization": "EXPLICIT",
        },
        "freshness_requirement": "SOURCE_CHANGE",
        "product_asset_ref": {
            "asset_id": "pa01:spc",
            "asset_revision": 3,
            "descriptor_ref": "descriptor:pa01:spc@3",
            "content_ref": "content:pa01:spc@3",
            "publication_state": "PUBLISHED",
            "validity_state": "ACTIVE",
            "as_of": "catalog:spc@r3",
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
        },
        "dependent_claims": ["intent:capability-scope"],
    }
    base.update(overrides)
    return base


def plan_with(item):
    return {
        "plan_id": "fkp:feature-123",
        "revision": 1,
        "items": [item],
    }


def assert_invalid(item, text):
    with pytest.raises(FeatureKnowledgePlanError, match=text) as exc:
        compile_feature_knowledge_plan(plan_with(item), root_skill())
    assert exc.value.code == "INVALID_FEATURE_KNOWLEDGE_PLAN"


def test_unknown_root_template_is_rejected():
    assert_invalid(plan_item(template_id="made-up"), "unknown root requirement template")


def test_invented_context_role_is_rejected():
    assert_invalid(plan_item(knowledge_role="MAGICAL_CONTEXT"), "knowledge role")


def test_invented_authority_dimension_is_rejected():
    assert_invalid(plan_item(authority_dimension="CURRENT_FEATURE_TRUTH"), "authority dimension")


def test_unauthorized_required_promotion_is_rejected():
    item = plan_item(
        template_id="delivery-prior-on-demand",
        knowledge_role="DELIVERY_PRIOR",
        mode="REQUIRED",
        authority_dimension="RATIONALE_SUPPORT",
        selector={"max_assets": 1},
        trust_requirements={
            "review": "UNREVIEWED",
            "verification": "NOT_VERIFIED",
            "authorization": "NONE",
        },
        freshness_requirement="MANUAL",
    )
    assert_invalid(item, "mode REQUIRED")


def test_weakened_trust_is_rejected():
    item = plan_item(
        trust_requirements={
            "review": "UNREVIEWED",
            "verification": "VERIFIED",
            "authorization": "EXPLICIT",
        }
    )
    assert_invalid(item, "weaken root trust")


def test_weakened_or_changed_freshness_is_rejected():
    assert_invalid(plan_item(freshness_requirement="TTL_365D"), "freshness")


def test_selector_cannot_expand_root_bound():
    assert_invalid(plan_item(selector={"max_assets": 2}), "selector bound")


def test_compilation_records_root_skill_and_plan_provenance():
    item = plan_item()
    plan = plan_with(item)
    compiled = compile_feature_knowledge_plan(plan, root_skill())
    assert len(compiled) == 1
    result = compiled[0]
    assert result["root_skill_id"] == "ft-t2-delivery-spec"
    assert result["root_skill_revision"] == "0.4.2"
    assert result["root_requirement_template_id"] == "product-semantics-required"
    assert result["feature_knowledge_plan_id"] == "fkp:feature-123"
    assert result["feature_knowledge_plan_revision"] == 1
    assert result["knowledge_role"] == "SEMANTICS"
    assert result["mode"] == "REQUIRED"
    assert result["authority_dimension"] == "DURABLE_CONSTRAINT"
    assert result["selector"] == {"max_assets": 1}
    assert result["product_asset_ref"] == item["product_asset_ref"]
    assert result["dependent_claims"] == ["intent:capability-scope"]


def test_incomplete_prebound_product_asset_ref_is_rejected():
    item = plan_item()
    item["product_asset_ref"] = {
        "asset_id": "pa01:spc",
        "asset_revision": 3,
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
    }
    assert_invalid(item, "exact ProductAssetRef")


def test_root_skill_requires_governing_skill_revision_field():
    skill = root_skill()
    compiled = compile_feature_knowledge_plan(plan_with(plan_item()), skill)
    assert compiled[0]["root_skill_revision"] == "0.4.2"
