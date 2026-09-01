from runtime import feature_knowledge_plan


def test_feature_knowledge_plan_runtime_exposes_required_api():
    required = {"FeatureKnowledgePlanError", "compile_feature_knowledge_plan"}
    missing = sorted(name for name in required if not hasattr(feature_knowledge_plan, name))
    assert missing == []
