from runtime import product_knowledge_maintenance


def test_maintenance_runtime_exposes_required_api():
    required = {
        "MaintenanceError",
        "create_semantic_draft",
        "publish_semantic_revision",
        "mark_product_knowledge_stale",
        "supersede_semantic_revision",
        "onboarding_request_maintenance",
    }
    missing = sorted(name for name in required if not hasattr(product_knowledge_maintenance, name))
    assert missing == []
