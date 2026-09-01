import copy
import json
from pathlib import Path

import jsonschema
import pytest

from tests.test_product_semantics_common_descriptor import exact_common_descriptor_asset


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "01-layer2" / "contracts" / "pa-01-minimal-product-semantics.schema.json"


def load_schema():
    return json.loads(SCHEMA.read_text())


def test_pa01_schema_exists_and_accepts_exact_common_descriptor():
    schema = load_schema()
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(exact_common_descriptor_asset(), schema)


def test_pa01_schema_rejects_legacy_helper_descriptor_shape():
    legacy = {
        "asset_id": "pa01:spc",
        "revision": 1,
        "lifecycle": "ACTIVE",
        "product": {"product_id": "SPC"},
        "provenance": {"source_refs": ["catalog:spc@r1"]},
        "freshness": {"as_of": "r1"},
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(legacy, load_schema())


def test_pa01_schema_rejects_current_truth_authority_dimension():
    asset = copy.deepcopy(exact_common_descriptor_asset())
    asset["authority_dimensions"] = ["TECHNICAL_OBLIGATION"]
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(asset, load_schema())
