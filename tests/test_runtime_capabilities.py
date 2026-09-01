import pytest

from runtime.runtime_capabilities import RuntimeCapabilityError, compile_runtime_capability_requirements


def root_skill():
    return {
        "skill_id": "ft-t2-delivery-spec",
        "skill_revision": "0.4.2",
        "runtime_capability_templates": [
            {
                "template_id": "structural-navigation",
                "capability": "STRUCTURAL_INTELLIGENCE_QUERY",
                "allowed_modes": ["OPTIONAL", "ON_DEMAND"],
                "allowed_operations": ["find", "expand", "trace"],
                "maximum_bounds": {
                    "max_depth": 3,
                    "max_nodes": 100,
                    "max_edges": 200,
                    "max_paths": 20,
                    "max_result_bytes": 65536,
                },
                "may_promote_to_required": False,
            }
        ],
    }


def feature_plan():
    return {
        "plan_id": "fkp:SPC-123",
        "revision": 2,
        "runtime_capabilities": [
            {
                "template_id": "structural-navigation",
                "capability": "STRUCTURAL_INTELLIGENCE_QUERY",
                "mode": "ON_DEMAND",
                "operations": ["trace", "find"],
                "bounds": {
                    "max_depth": 2,
                    "max_nodes": 40,
                    "max_edges": 80,
                    "max_paths": 10,
                    "max_result_bytes": 32768,
                },
                "dependent_claims": ["candidate-repo-discovery"],
            }
        ],
    }


def test_feature_plan_only_instantiates_root_declared_runtime_capability():
    compiled = compile_runtime_capability_requirements(root_skill(), feature_plan())
    assert compiled == [
        {
            "root_skill_id": "ft-t2-delivery-spec",
            "root_skill_revision": "0.4.2",
            "root_runtime_template_id": "structural-navigation",
            "feature_plan_id": "fkp:SPC-123",
            "feature_plan_revision": 2,
            "capability": "STRUCTURAL_INTELLIGENCE_QUERY",
            "mode": "ON_DEMAND",
            "operations": ["find", "trace"],
            "bounds": {
                "max_depth": 2,
                "max_nodes": 40,
                "max_edges": 80,
                "max_paths": 10,
                "max_result_bytes": 32768,
            },
            "dependent_claims": ["candidate-repo-discovery"],
        }
    ]


def test_feature_plan_cannot_invent_runtime_capability_or_template():
    plan = feature_plan()
    plan["runtime_capabilities"][0]["template_id"] = "made-up"
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)

    plan = feature_plan()
    plan["runtime_capabilities"][0]["capability"] = "SHELL_EXECUTION"
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)


def test_feature_plan_cannot_promote_optional_runtime_to_required():
    plan = feature_plan()
    plan["runtime_capabilities"][0]["mode"] = "REQUIRED"
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)


def test_feature_plan_cannot_exceed_root_bounds_or_operations():
    plan = feature_plan()
    plan["runtime_capabilities"][0]["bounds"]["max_depth"] = 4
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)

    plan = feature_plan()
    plan["runtime_capabilities"][0]["operations"].append("diff")
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)


def test_runtime_requirement_cannot_masquerade_as_product_context():
    for forbidden_field in ("product_asset_ref", "knowledge_role", "authority_dimension", "context_selector"):
        plan = feature_plan()
        plan["runtime_capabilities"][0][forbidden_field] = {"fake": True}
        with pytest.raises(RuntimeCapabilityError):
            compile_runtime_capability_requirements(root_skill(), plan)


def test_all_runtime_bounds_are_required_positive_and_deterministic():
    plan = feature_plan()
    plan["runtime_capabilities"][0]["bounds"].pop("max_paths")
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)

    plan = feature_plan()
    plan["runtime_capabilities"][0]["bounds"]["max_paths"] = 0
    with pytest.raises(RuntimeCapabilityError):
        compile_runtime_capability_requirements(root_skill(), plan)
