from runtime.structural_intelligence import (
    StructuralIntelligenceError,
    derive_discovery_hints,
    diff_observations,
    normalize_observations,
    validate_snapshot_ref,
    validate_structural_query,
)


def test_structural_runtime_public_api_exists():
    assert issubclass(StructuralIntelligenceError, ValueError)
    for fn in (
        validate_snapshot_ref,
        validate_structural_query,
        normalize_observations,
        derive_discovery_hints,
        diff_observations,
    ):
        assert callable(fn)
