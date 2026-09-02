"""FeatureKnowledgePlan delegation conformance runtime.

The plan is deliberately non-canonical: it may instantiate root-Skill Context
requirement templates but cannot create new requirement authority or weaken an
exact pre-bound ProductAssetRef.
"""

from __future__ import annotations

from copy import deepcopy


class FeatureKnowledgePlanError(ValueError):
    code = "INVALID_FEATURE_KNOWLEDGE_PLAN"


_TRUST_RANK = {
    "review": {"UNREVIEWED": 0, "REVIEWED": 1},
    "verification": {"NOT_VERIFIED": 0, "VERIFIED": 1},
    "authorization": {"NONE": 0, "SOURCE_INHERITED": 1, "EXPLICIT": 2},
}
_EXACT_REF_FIELDS = {
    "asset_id",
    "asset_revision",
    "descriptor_ref",
    "content_ref",
    "publication_state",
    "validity_state",
    "as_of",
    "authority_dimensions",
    "trust_profile",
    "scope_match",
}


def _invalid(message: str):
    raise FeatureKnowledgePlanError(message)


def _check_trust(requested: dict, minimum: dict):
    for facet, minimum_value in minimum.items():
        ranks = _TRUST_RANK.get(facet)
        if ranks is None or minimum_value not in ranks:
            _invalid(f"unsupported root trust facet/value: {facet}={minimum_value}")
        requested_value = requested.get(facet)
        if requested_value not in ranks:
            _invalid(f"missing or unsupported trust requirement: {facet}")
        if ranks[requested_value] < ranks[minimum_value]:
            _invalid(f"FeatureKnowledgePlan may not weaken root trust requirement: {facet}")


def _check_ref_trust(ref_trust: dict, requested: dict):
    for facet, requested_value in requested.items():
        ranks = _TRUST_RANK.get(facet)
        if ranks is None or requested_value not in ranks:
            continue
        actual = ref_trust.get(facet)
        if actual not in ranks or ranks[actual] < ranks[requested_value]:
            _invalid(f"exact ProductAssetRef does not satisfy trust requirement: {facet}")


def _validate_exact_product_asset_ref(ref: dict, *, authority_dimension: str, trust_requirements: dict):
    if not isinstance(ref, dict) or not _EXACT_REF_FIELDS.issubset(ref):
        _invalid("pre-bound knowledge must carry an exact ProductAssetRef")
    if (
        ref.get("publication_state") != "PUBLISHED"
        or ref.get("validity_state") != "ACTIVE"
        or not ref.get("asset_id")
        or not isinstance(ref.get("asset_revision"), int)
        or isinstance(ref.get("asset_revision"), bool)
        or ref.get("asset_revision", 0) <= 0
        or not ref.get("descriptor_ref")
        or not ref.get("content_ref")
        or not ref.get("as_of")
        or not isinstance(ref.get("authority_dimensions"), list)
        or not isinstance(ref.get("trust_profile"), dict)
        or not isinstance(ref.get("scope_match"), (dict, str))
    ):
        _invalid("pre-bound knowledge must carry an exact PUBLISHED + ACTIVE ProductAssetRef")
    if authority_dimension not in ref["authority_dimensions"]:
        _invalid("exact ProductAssetRef does not carry the requested authority dimension")
    _check_ref_trust(ref["trust_profile"], trust_requirements)


def compile_feature_knowledge_plan(plan: dict, root_skill: dict) -> list[dict]:
    """Compile a FeatureKnowledgePlan only through declared root-Skill templates."""
    if not plan.get("plan_id") or not isinstance(plan.get("revision"), int):
        _invalid("plan_id and integer revision are required")
    skill_id = root_skill.get("skill_id")
    skill_revision = root_skill.get("skill_revision")
    if not skill_id or not skill_revision:
        _invalid("root Skill skill_id/skill_revision is required")

    templates = {
        template.get("template_id"): template
        for template in root_skill.get("context_requirement_templates", [])
        if template.get("template_id")
    }
    compiled = []
    for item in plan.get("items", []):
        template_id = item.get("template_id")
        template = templates.get(template_id)
        if template is None:
            _invalid(f"unknown root requirement template: {template_id}")

        if item.get("knowledge_role") != template.get("knowledge_role"):
            _invalid("FeatureKnowledgePlan knowledge role is not declared by root template")

        authority = item.get("authority_dimension")
        if authority not in template.get("allowed_authority_dimensions", []):
            _invalid(f"authority dimension is not permitted by root template: {authority}")

        mode = item.get("mode")
        allowed_modes = set(template.get("allowed_modes", []))
        if mode not in allowed_modes:
            if not (mode == "REQUIRED" and template.get("may_promote_to_required") is True):
                _invalid(f"mode {mode} is not permitted by root requirement template")

        selector = item.get("selector", {})
        root_max_assets = template.get("selector_bounds", {}).get("max_assets")
        requested_max_assets = selector.get("max_assets")
        if (
            not isinstance(requested_max_assets, int)
            or isinstance(requested_max_assets, bool)
            or requested_max_assets <= 0
            or not isinstance(root_max_assets, int)
            or requested_max_assets > root_max_assets
        ):
            _invalid("FeatureKnowledgePlan selector bound exceeds or violates root selector bound")

        requested_trust = item.get("trust_requirements", {})
        _check_trust(requested_trust, template.get("minimum_trust", {}))

        requested_freshness = item.get("freshness_requirement")
        root_freshness = template.get("freshness_requirement")
        if requested_freshness != root_freshness:
            _invalid("FeatureKnowledgePlan freshness requirement may not weaken/change root freshness")

        product_asset_ref = item.get("product_asset_ref")
        if product_asset_ref is not None:
            _validate_exact_product_asset_ref(
                product_asset_ref,
                authority_dimension=authority,
                trust_requirements=requested_trust,
            )

        compiled.append(
            {
                "root_skill_id": skill_id,
                "root_skill_revision": skill_revision,
                "root_requirement_template_id": template_id,
                "feature_knowledge_plan_id": plan["plan_id"],
                "feature_knowledge_plan_revision": plan["revision"],
                "knowledge_role": item["knowledge_role"],
                "mode": mode,
                "authority_dimension": authority,
                "selector": deepcopy(selector),
                "trust_requirements": deepcopy(requested_trust),
                "freshness_requirement": requested_freshness,
                "product_asset_ref": deepcopy(product_asset_ref) if product_asset_ref else None,
                "dependent_claims": list(item.get("dependent_claims", [])),
            }
        )
    return compiled
