from runtime import realization_traversal


def test_realization_traversal_runtime_exposes_required_api():
    required = {"TraversalError", "derive_repository_candidates"}
    missing = sorted(name for name in required if not hasattr(realization_traversal, name))
    assert missing == []
