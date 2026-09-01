from runtime import product_semantics


def test_product_semantics_runtime_exposes_required_api():
    required = {
        "ContractError",
        "validate_product_semantics_asset",
        "resolve_layer1_product_semantics_ref",
    }
    missing = sorted(name for name in required if not hasattr(product_semantics, name))
    assert missing == []
