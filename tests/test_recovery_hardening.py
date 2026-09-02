import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'implementation' / 'structural-intelligence' / 'runtime'))
sys.path.insert(0, str(ROOT / 'implementation' / 'product-intelligence' / 'runtime'))

from grafel_adapter import GrafelAdapter
from registry import rebuild_registry

import types, importlib
_pkg = types.ModuleType('structural_runtime')
_pkg.__path__ = [str(ROOT / 'implementation' / 'structural-intelligence' / 'runtime')]
sys.modules['structural_runtime'] = _pkg
grafel_binding = importlib.import_module('structural_runtime.grafel_binding')
validate_binding_evidence = getattr(grafel_binding, 'validate_binding_evidence', None)


def load_schema(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def valid_descriptor(**overrides):
    d = {
        'fdi_asset_version': '0.1',
        'asset_id': 'CB-SPC-001',
        'asset_family': 'CODEBASE',
        'asset_type': 'CB-01_REPOSITORY_INVENTORY',
        'asset_revision': 1,
        'content_ref': 'assets/by-id/CB-SPC-001/content/r0001.json',
        'publication_state': 'PUBLISHED',
        'validity_state': 'ACTIVE',
        'owner': 'spc-product-team',
        'maintenance_mode': 'DERIVED',
        'publication_policy': 'RULE_BASED_AUTO',
        'scope': {'products': ['SPC'], 'systems': [], 'repositories': [], 'environments': []},
        'authority_dimensions': ['CURRENT_BEHAVIOR_SUPPORT'],
        'trust_profile': {
            'provenance': 'DIRECT', 'review': 'REVIEWED',
            'verification': 'VERIFIED', 'authorization': 'SOURCE_INHERITED'
        },
        'as_of': '2026-09-02T00:00:00Z',
        'source_refs': ['azure-repos://spc/repo@' + 'a' * 40],
        'dependency_refs': [],
        'freshness_policy': {'mode': 'SOURCE_CHANGE', 'ttl': None},
        'supersedes': None,
        'invalidation_triggers': ['repository source revision changes'],
        'selection_metadata': {'terms': ['spc'], 'applicability': ['SPC']},
    }
    d.update(overrides)
    return d


class FakeTransport:
    def __init__(self, result):
        self.result = result
        self.calls = []
    def invoke(self, tool, payload):
        self.calls.append((tool, payload))
        return self.result


class RecoveryHardeningTests(unittest.TestCase):
    def test_product_asset_descriptor_rejects_illegal_draft_active(self):
        schema = load_schema('implementation/product-intelligence/contracts/ProductAssetDescriptor.schema.json')
        validator = Draft202012Validator(schema)
        d = valid_descriptor(publication_state='DRAFT', validity_state='ACTIVE')
        self.assertTrue(list(validator.iter_errors(d)), 'DRAFT + ACTIVE must be illegal')

    def test_product_asset_descriptor_accepts_full_governing_contract(self):
        schema = load_schema('implementation/product-intelligence/contracts/ProductAssetDescriptor.schema.json')
        Draft202012Validator(schema).validate(valid_descriptor())

    def test_product_asset_ref_requires_resolution_metadata(self):
        schema = load_schema('implementation/product-intelligence/contracts/ProductAssetRef.schema.json')
        validator = Draft202012Validator(schema)
        errors = list(validator.iter_errors({'asset_id': 'A', 'asset_revision': 1}))
        self.assertTrue(errors)

    def test_registry_rejects_duplicate_active_lineage(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for rev in (1, 2):
                p = root / 'assets' / 'by-id' / 'A' / 'revisions' / f'r{rev:04d}.json'
                p.parent.mkdir(parents=True, exist_ok=True)
                d = valid_descriptor(asset_id='A', asset_revision=rev)
                p.write_text(json.dumps(d), encoding='utf-8')
            with self.assertRaises(ValueError):
                rebuild_registry(root)

    def test_registry_projects_governing_resolution_fields(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            p = root / 'assets' / 'by-id' / 'A' / 'revisions' / 'r0001.json'
            p.parent.mkdir(parents=True, exist_ok=True)
            d = valid_descriptor(asset_id='A')
            p.write_text(json.dumps(d), encoding='utf-8')
            row = rebuild_registry(root)['assets'][0]
            for field in ('descriptor_ref', 'content_ref', 'publication_state', 'validity_state',
                          'as_of', 'authority_dimensions', 'trust_profile', 'scope_match'):
                self.assertIn(field, row)

    def test_grafel_provider_query_maps_all_pre_execution_bounds(self):
        transport = FakeTransport({'nodes': [], 'edges': [], 'paths': []})
        adapter = GrafelAdapter(transport)
        snapshot = {'snapshot_id': 's', 'provider_scope_id': 'g', 'provider_ref': 'r'}
        query = {
            'snapshot_id': 's', 'operation': 'TRACE',
            'repository_scope': ['repo-a', 'repo-b'],
            'relation_allowlist': ['API', 'EVENT'],
            'max_depth': 3, 'max_nodes': 10, 'max_edges': 20,
            'max_paths': 5, 'max_result_bytes': 10000,
            'payload': {'query': 'x'}
        }
        adapter.query(snapshot, query)
        payload = transport.calls[0][1]
        self.assertEqual(payload['repository_scope'], ['repo-a', 'repo-b'])
        self.assertEqual(payload['relation_allowlist'], ['API', 'EVENT'])
        self.assertEqual(payload['max_depth'], 3)

    def test_binding_evidence_cross_field_validation_is_fail_closed(self):
        evidence = {
            'evidence_id': 'gbe-1',
            'snapshot': {
                'snapshot_id': 's', 'provider': {'name':'GRAFEL','version':'1.2.3','adapter_version':'recovery-0.2'}, 'provider_scope_id': 'g', 'provider_ref': 'r',
                'repositories': [{'repository_id': 'repo-a', 'local_path': '/tmp/repo-a', 'canonical_revision': 'a'*40}]
            },
            'attestation': {
                'attestation_id': 'attest:s', 'snapshot_id': 's', 'provider_scope_id': 'g', 'provider_ref': 'r',
                'repository_bindings': [{'repository_id': 'repo-a', 'canonical_revision': 'a'*40, 'indexed_revision': 'a'*40, 'indexed_ref':'r'}],
                'queryable': True,
                'runtime_version': '1.2.3', 'wire_version': 'mcp-1', 'adapter_version': 'recovery-0.2',
                'compatibility': 'VERIFIED', 'result': 'EXACTLY_BOUND', 'captured_at': '2026-09-02T00:00:00Z'
            },
            'provider_route': {'group': 'g', 'ref': 'r'},
            'runtime_version': '9.9.9',
            'wire_version': 'mcp-1',
            'adapter_version': 'recovery-0.2',
            'compatibility': 'VERIFIED',
            'captured_at': '2026-09-02T00:00:00Z',
            'result': 'EXACTLY_BOUND'
        }
        self.assertIsNotNone(validate_binding_evidence, 'validate_binding_evidence must exist')
        with self.assertRaisesRegex(ValueError, 'runtime_version mismatch'):
            validate_binding_evidence(evidence)

    def test_bundle_verifier_fails_on_unexpected_active_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'BUNDLE-MANIFEST.json').write_text(json.dumps({'files': []}), encoding='utf-8')
            (root / 'surprise.md').write_text('unexpected', encoding='utf-8')
            proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'verify_bundle.py'), str(root)], capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('unexpected', (proc.stdout + proc.stderr).lower())


    def test_baseline_validator_confirms_recovery_is_blocked(self):
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_baseline.py'), str(ROOT), '--expect-recovery-blocked'], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        proc2 = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_baseline.py'), str(ROOT), '--require-approved'], capture_output=True, text=True)
        self.assertNotEqual(proc2.returncode, 0)

    def test_governance_has_candidate_baseline_and_no_fake_active_authority(self):
        self.assertTrue((ROOT / 'governance' / 'baselines' / 'GB-0001-CANDIDATE.yaml').exists())
        current = (ROOT / 'governance' / 'CURRENT').read_text(encoding='utf-8').strip()
        self.assertEqual(current, 'NONE')
        self.assertFalse((ROOT / '00-governance' / 'ACTIVE-AUTHORITY.md').exists())

    def test_pa01_is_candidate_not_normative(self):
        self.assertTrue((ROOT / 'candidates' / 'PA-01').exists())
        normative = list((ROOT / 'normative').rglob('*PA-01*')) if (ROOT / 'normative').exists() else []
        self.assertEqual(normative, [])

if __name__ == '__main__':
    unittest.main()
