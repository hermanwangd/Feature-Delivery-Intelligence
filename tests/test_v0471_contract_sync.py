import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / '03-structural-intelligence' / 'contracts' / 'structural-runtime-contracts.schema.json'
GRAFEL = ROOT / '03-structural-intelligence' / 'GRAFEL-ADAPTER-CONTRACT-v0.2.md'
DISCOVERY = ROOT / '03-structural-intelligence' / 'FEATURE-DISCOVERY-INTEGRATION-v0.2.md'
HARDENING = ROOT / '00-product' / 'FDI-MVP-v0.4.7.1-STRUCTURAL-INTELLIGENCE-HARDENING.md'


def test_structural_runtime_schema_v0471_exposes_binding_and_bounded_set_contracts():
    schema = json.loads(SCHEMA.read_text())
    assert schema['title'] == 'FDI Structural Intelligence Runtime Support Contracts v0.4.7.1'
    defs = schema['$defs']
    for name in (
        'StructuralSnapshotRef',
        'SnapshotBindingAttestation',
        'StructuralQuery',
        'StructuralObservation',
        'StructuralObservationSet',
        'StructuralDiscoveryHint',
        'StructuralDiscoveryHintSet',
        'StructuralDiffQuery',
        'StructuralDelta',
    ):
        assert name in defs
    assert defs['StructuralSnapshotRef']['additionalProperties'] is False
    binding = defs['SnapshotBindingAttestation']
    assert binding['properties']['binding_state']['const'] == 'VERIFIED'
    assert binding['properties']['freshness']['enum'] == ['LIVE_CURRENT', 'FROZEN_INDEXED']
    assert {'provider_route', 'freshness'} <= set(binding['required'])
    assert binding['properties']['provider_route']['properties']['scope_id']['minLength'] == 1
    assert binding['properties']['provider_route']['properties']['ref']['minLength'] == 1
    assert 'binding_attestation_id' in defs['StructuralObservationSet']['required']
    assert 'before_binding_attestation_id' in defs['StructuralDelta']['required']
    assert 'after_binding_attestation_id' in defs['StructuralDelta']['required']
    serialized = json.dumps(schema)
    for forbidden in ('ProductAssetFamily', 'CONFIRMED', 'SPEC_READY'):
        assert forbidden not in serialized


def test_grafel_adapter_v02_requires_exact_queryable_binding_attestor_and_two_routed_diff_snapshots():
    text = GRAFEL.read_text()
    assert 'FDI release:** v0.4.7.1' in text
    assert 'binding_attestor' in text
    assert 'FROZEN_INDEXED' in text
    assert 'LIVE_CURRENT' in text
    assert 'provider scope' in text.lower()
    assert 'provider ref' in text.lower()
    assert 'grafel_index_status' in text
    assert 'insufficient' in text.lower()
    assert 'SnapshotBindingAttestation' in text
    assert 'before' in text and 'after' in text
    assert 'two' in text.lower() and 'StructuralSnapshotRef' in text
    assert 'path_id' in text
    assert 'metadata-only' in text.lower()


def test_feature_discovery_v02_declares_identity_only_pa03_grounding_and_no_semantic_leakage():
    text = DISCOVERY.read_text()
    assert 'FDI release:** v0.4.7.1' in text
    assert 'PA-03 CB-01' in text
    assert 'identity-only' in text.lower()
    assert 'capability terms' in text.lower()
    assert 'Product Realization' in text
    assert 'Delivery Intelligence' in text
    assert 'basis = LAYER2_PA03' in text
    assert 'CONFIRMED' in text and 'SPEC_READY' in text


def test_v0471_hardening_doc_supersedes_v0470_source_binding_and_evaluation_details_only():
    text = HARDENING.read_text()
    assert 'v0.4.7.1' in text
    assert 'supersedes' in text.lower()
    assert 'source binding' in text.lower()
    assert 'evaluation' in text.lower()
    assert 'does not modify' in text.lower()
    assert 'HERM-211' in text
    assert 'six helper contracts' in text
    assert 'current feature-specific Evidence' in text
