import json, sys, tempfile
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"implementation"/"structural-intelligence"/"runtime"))
sys.path.insert(0, str(ROOT/"implementation"/"product-intelligence"/"runtime"))

from git_revision import require_full_git_revision
from grafel_adapter import GrafelAdapter
from registry import rebuild_registry

class FakeTransport:
    def __init__(self, result): self.result=result; self.calls=[]
    def invoke(self, tool, payload): self.calls.append((tool,payload)); return self.result

def valid_asset(revision=1, publication_state="PUBLISHED", validity_state="ACTIVE"):
    return {
      "fdi_asset_version":"0.1", "asset_id":"A", "asset_family":"CODEBASE", "asset_type":"CB-01_REPOSITORY_INVENTORY",
      "asset_revision":revision, "content_ref":f"content/A/r{revision:04d}.json",
      "publication_state":publication_state, "validity_state":validity_state, "owner":"team",
      "maintenance_mode":"DERIVED", "publication_policy":"RULE_BASED_AUTO",
      "scope":{"products":["P"],"systems":[],"repositories":[],"environments":[]},
      "authority_dimensions":["CURRENT_BEHAVIOR_SUPPORT"],
      "trust_profile":{"provenance":"DIRECT","review":"REVIEWED","verification":"VERIFIED","authorization":"SOURCE_INHERITED"},
      "as_of":"2026-09-02T00:00:00Z", "source_refs":["repo@"+"a"*40], "dependency_refs":[],
      "freshness_policy":{"mode":"SOURCE_CHANGE","ttl":None}, "supersedes":None,
      "invalidation_triggers":["source change"], "selection_metadata":{"terms":["a"],"applicability":["P"]}
    }

class RecoveryTests(unittest.TestCase):
    def test_full_revision_required(self):
        with self.assertRaises(ValueError): require_full_git_revision("abc123")
        self.assertEqual(require_full_git_revision("a"*40), "a"*40)

    def test_grafel_tool_names_are_adapter_local_and_bounds_enforced(self):
        t=FakeTransport({"nodes":[1,2],"edges":[],"paths":[]})
        a=GrafelAdapter(t)
        snapshot={"snapshot_id":"s","provider_scope_id":"g","provider_ref":"r"}
        q={"snapshot_id":"s","operation":"FIND","repository_scope":["repo-a"],"relation_allowlist":[],
           "max_depth":2,"max_nodes":1,"max_edges":10,"max_paths":10,"max_result_bytes":10000,"payload":{}}
        with self.assertRaises(ValueError): a.query(snapshot,q)
        self.assertEqual(t.calls[0][0], "grafel_find")

    def test_registry_only_contains_published_active(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            base=root/"assets"/"by-id"/"A"/"revisions"; base.mkdir(parents=True)
            (base/"r0001.json").write_text(json.dumps(valid_asset()), encoding="utf-8")
            bad=valid_asset(2, "DRAFT", "NOT_APPLICABLE")
            (base/"r0002.json").write_text(json.dumps(bad), encoding="utf-8")
            reg=rebuild_registry(root)
            self.assertEqual([(x["asset_id"],x["asset_revision"]) for x in reg["assets"]], [("A",1)])

if __name__ == '__main__': unittest.main()
