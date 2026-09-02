import json, sys, tempfile, subprocess
from pathlib import Path
import unittest
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))

from fdi.structural_intelligence.git_revision import require_full_git_revision
from fdi.structural_intelligence.grafel_adapter import GrafelAdapter
from fdi.structural_intelligence.grafel_binding import validate_binding_evidence
from fdi.product_intelligence.registry import rebuild_registry

class FakeTransport:
    def __init__(self,result): self.result=result; self.calls=[]
    def invoke(self,tool,payload): self.calls.append((tool,payload)); return self.result

def schema(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))

def valid_asset(rev=1, publication='PUBLISHED', validity='ACTIVE'):
    return {
      'fdi_asset_version':'0.1','asset_id':'A','asset_family':'CODEBASE','asset_type':'CB-01_REPOSITORY_INVENTORY',
      'asset_revision':rev,'content_ref':f'content/A/r{rev:04d}.json','publication_state':publication,'validity_state':validity,
      'owner':'team','maintenance_mode':'DERIVED','publication_policy':'RULE_BASED_AUTO',
      'scope':{'products':['P'],'systems':[],'repositories':[],'environments':[]},
      'authority_dimensions':['CURRENT_BEHAVIOR_SUPPORT'],
      'trust_profile':{'provenance':'DIRECT','review':'REVIEWED','verification':'VERIFIED','authorization':'SOURCE_INHERITED'},
      'as_of':'2026-09-02T00:00:00Z','source_refs':['repo@'+'a'*40],'dependency_refs':[],
      'freshness_policy':{'mode':'SOURCE_CHANGE','ttl':None},'supersedes':None,
      'invalidation_triggers':['source change'],'selection_metadata':{'terms':['a'],'applicability':['P']}
    }

class CleanHardeningTests(unittest.TestCase):
    def test_full_git_revision(self):
        with self.assertRaises(ValueError): require_full_git_revision('abc123')
        self.assertEqual(require_full_git_revision('a'*40),'a'*40)

    def test_product_asset_illegal_draft_active(self):
        v=Draft202012Validator(schema('contracts/layer2/ProductAssetDescriptor.schema.json'))
        self.assertTrue(list(v.iter_errors(valid_asset(publication='DRAFT', validity='ACTIVE'))))

    def test_registry_only_published_active_and_unique(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); p=root/'assets/by-id/A/revisions'; p.mkdir(parents=True)
            (p/'r0001.json').write_text(json.dumps(valid_asset()),encoding='utf-8')
            (p/'r0002.json').write_text(json.dumps(valid_asset(2,'DRAFT','NOT_APPLICABLE')),encoding='utf-8')
            reg=rebuild_registry(root)
            self.assertEqual([(x['asset_id'],x['asset_revision']) for x in reg['assets']],[('A',1)])
            (p/'r0002.json').write_text(json.dumps(valid_asset(2)),encoding='utf-8')
            with self.assertRaises(ValueError): rebuild_registry(root)

    def test_grafel_maps_all_bounds(self):
        t=FakeTransport({'nodes':[],'edges':[],'paths':[]}); a=GrafelAdapter(t)
        snap={'snapshot_id':'s','provider_scope_id':'g','provider_ref':'r'}
        q={'snapshot_id':'s','operation':'TRACE','repository_scope':['r1'],'relation_allowlist':['API'],'max_depth':3,'max_nodes':10,'max_edges':10,'max_paths':5,'max_result_bytes':10000,'payload':{'query':'x'}}
        a.query(snap,q)
        payload=t.calls[0][1]
        for k in ['repository_scope','relation_allowlist','max_depth','max_nodes','max_edges','max_paths','max_result_bytes']:
            self.assertEqual(payload[k],q[k])

    def test_binding_cross_field_fail_closed(self):
        ev={'evidence_id':'e','snapshot':{'snapshot_id':'s','provider':{'name':'GRAFEL','version':'1','adapter_version':'fdi-0.4.8.2'},'provider_scope_id':'g','provider_ref':'r','repositories':[{'repository_id':'r1','local_path':'/tmp/r1','canonical_revision':'a'*40}]},
            'attestation':{'attestation_id':'a','snapshot_id':'s','provider_scope_id':'g','provider_ref':'r','repository_bindings':[{'repository_id':'r1','canonical_revision':'a'*40,'indexed_revision':'a'*40,'indexed_ref':'r'}],'queryable':True,'runtime_version':'1','wire_version':'mcp-1','adapter_version':'fdi-0.4.8.2','compatibility':'VERIFIED','result':'EXACTLY_BOUND','captured_at':'2026-09-02T00:00:00Z'},
            'provider_route':{'group':'g','ref':'r'},'runtime_version':'9','wire_version':'mcp-1','adapter_version':'fdi-0.4.8.2','compatibility':'VERIFIED','captured_at':'2026-09-02T00:00:00Z','result':'EXACTLY_BOUND'}
        with self.assertRaisesRegex(ValueError,'runtime_version mismatch'): validate_binding_evidence(ev)

    def test_governance_lock_has_approved_source_identities(self):
        lock=json.loads((ROOT/'governance/approved-source-lock.json').read_text())
        ids={x['id'] for x in lock['sources']}
        self.assertEqual(ids,{'L1-SEM','L1-IO','L2-FWK','L2-PROFILE','L2-MAINT','FT-T2'})
        self.assertEqual(lock['ft_t2_locked_surface']['contracts'],['IntentSpec','CandidateRepoSet','ChangeSurfaceSet','EvidenceRecord','ClosurePackage','ClosureReview'])
        self.assertEqual(len(lock['ft_t2_locked_surface']['skills']),5)

    def test_pa01_is_proposal_not_approved_profile(self):
        self.assertTrue((ROOT/'specs/proposals/PA-01').exists())
        self.assertFalse((ROOT/'specs/layer2/profiles/PA-01').exists())

if __name__=='__main__': unittest.main()
