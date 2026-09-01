"""RuntimeCapabilityRequirement delegation for FDI v0.4.7.0.

Runtime capabilities are distinct from Layer 2 ContextRequirements. Feature
plans may only instantiate root-Skill-declared runtime templates.
"""

from __future__ import annotations

from copy import deepcopy


class RuntimeCapabilityError(ValueError):
    """Raised when a feature plan exceeds root-Skill runtime authority."""


_REQUIRED_BOUNDS = ("max_depth", "max_nodes", "max_edges", "max_paths", "max_result_bytes")
_FORBIDDEN_CONTEXT_FIELDS = {"product_asset_ref", "knowledge_role", "authority_dimension", "context_selector"}


def _fail(message: str) -> None:
    raise RuntimeCapabilityError(message)


def compile_runtime_capability_requirements(root_skill: dict, feature_plan: dict) -> list[dict]:
    if not isinstance(root_skill, dict) or not root_skill.get("skill_id") or not root_skill.get("skill_revision"):
        _fail("root skill_id/skill_revision are required")
    templates = root_skill.get("runtime_capability_templates")
    if not isinstance(templates, list):
        _fail("root runtime_capability_templates must be a list")
    template_by_id = {}
    for template in templates:
        if not isinstance(template, dict) or not template.get("template_id") or not template.get("capability"):
            _fail("root runtime template requires template_id/capability")
        if template["template_id"] in template_by_id:
            _fail(f"duplicate root runtime template: {template['template_id']}")
        template_by_id[template["template_id"]] = template

    if not isinstance(feature_plan, dict) or not feature_plan.get("plan_id") or not isinstance(feature_plan.get("revision"), int):
        _fail("feature plan_id/revision are required")
    items = feature_plan.get("runtime_capabilities")
    if not isinstance(items, list):
        _fail("feature runtime_capabilities must be a list")

    compiled = []
    for item in items:
        if not isinstance(item, dict):
            _fail("runtime capability item must be an object")
        forbidden = _FORBIDDEN_CONTEXT_FIELDS.intersection(item)
        if forbidden:
            _fail(f"runtime requirement may not carry Product Context fields: {sorted(forbidden)}")
        template_id = item.get("template_id")
        template = template_by_id.get(template_id)
        if template is None:
            _fail(f"runtime template not declared by root Skill: {template_id}")
        if item.get("capability") != template["capability"]:
            _fail("feature plan cannot change root runtime capability")
        mode = item.get("mode")
        if mode not in set(template.get("allowed_modes", [])):
            if mode == "REQUIRED" and template.get("may_promote_to_required") is False:
                _fail("feature plan cannot promote runtime capability to REQUIRED")
            _fail(f"runtime mode not allowed by root Skill: {mode}")
        if mode == "REQUIRED" and template.get("may_promote_to_required") is False:
            _fail("feature plan cannot promote runtime capability to REQUIRED")

        operations = item.get("operations")
        allowed_operations = set(template.get("allowed_operations", []))
        if not isinstance(operations, list) or not operations:
            _fail("runtime operations must be non-empty")
        if not set(operations).issubset(allowed_operations):
            _fail("feature plan requested operation outside root Skill allowance")

        requested_bounds = item.get("bounds")
        maximum_bounds = template.get("maximum_bounds")
        if not isinstance(requested_bounds, dict) or not isinstance(maximum_bounds, dict):
            _fail("runtime bounds and root maximum_bounds are required")
        normalized_bounds = {}
        for field in _REQUIRED_BOUNDS:
            requested = requested_bounds.get(field)
            maximum = maximum_bounds.get(field)
            if not isinstance(requested, int) or requested <= 0:
                _fail(f"runtime bound {field} must be a positive integer")
            if not isinstance(maximum, int) or maximum <= 0:
                _fail(f"root maximum bound {field} must be a positive integer")
            if requested > maximum:
                _fail(f"runtime bound {field} exceeds root Skill maximum")
            normalized_bounds[field] = requested

        compiled.append(
            {
                "root_skill_id": root_skill["skill_id"],
                "root_skill_revision": root_skill["skill_revision"],
                "root_runtime_template_id": template_id,
                "feature_plan_id": feature_plan["plan_id"],
                "feature_plan_revision": feature_plan["revision"],
                "capability": template["capability"],
                "mode": mode,
                "operations": sorted(set(operations)),
                "bounds": normalized_bounds,
                "dependent_claims": list(item.get("dependent_claims", [])),
            }
        )
    return compiled
