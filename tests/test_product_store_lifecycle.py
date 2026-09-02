import copy
from concurrent.futures import ThreadPoolExecutor
import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from fdi.product_intelligence import product_store
from fdi.product_intelligence import registry


def valid_asset(
    asset_id="A",
    revision=1,
    publication="PUBLISHED",
    validity="ACTIVE",
    supersedes=None,
    policy="RULE_BASED_AUTO",
):
    return {
        "fdi_asset_version": "0.1",
        "asset_id": asset_id,
        "asset_family": "CODEBASE",
        "asset_type": "CB-01_REPOSITORY_INVENTORY",
        "asset_revision": revision,
        "content_ref": f"content/{asset_id}/r{revision:04d}.json",
        "publication_state": publication,
        "validity_state": validity,
        "owner": "team",
        "maintenance_mode": "DERIVED",
        "publication_policy": policy,
        "scope": {
            "products": ["P"],
            "systems": [],
            "repositories": [],
            "environments": [],
        },
        "authority_dimensions": ["CURRENT_BEHAVIOR_SUPPORT"],
        "trust_profile": {
            "provenance": "DIRECT",
            "review": "REVIEWED",
            "verification": "VERIFIED",
            "authorization": "SOURCE_INHERITED",
        },
        "as_of": "2026-09-02T00:00:00Z",
        "source_refs": ["repo@" + "a" * 40],
        "dependency_refs": [],
        "freshness_policy": {"mode": "SOURCE_CHANGE", "ttl": None},
        "supersedes": supersedes,
        "invalidation_triggers": ["source change"],
        "selection_metadata": {"terms": ["a"], "applicability": ["P"]},
    }


def proposal(proposal_id, kind, asset, target_asset_id=None):
    return {
        "proposal_id": proposal_id,
        "target_asset_id": target_asset_id,
        "proposed_asset": asset,
        "evidence_refs": ["evidence/current-feature.json"],
        "proposal_kind": kind,
        "review_requirement": asset["publication_policy"],
    }


def authorization(policy="RULE_BASED_AUTO", approved=True, evidence_refs=("gate/run-1.json",)):
    return product_store.PublicationAuthorization(policy, approved, evidence_refs)


class ProductStoreLifecycleTests(unittest.TestCase):
    def test_draft_write_is_idempotent_but_rejects_conflicting_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            store = product_store.GitStoreAdapter(td)
            draft = proposal("p1", "CREATE", valid_asset())
            path = store.write_draft(draft)
            before = path.read_bytes()
            self.assertEqual(store.write_draft(draft), path)
            self.assertEqual(path.read_bytes(), before)

            conflicting = copy.deepcopy(draft)
            conflicting["evidence_refs"] = ["evidence/different.json"]
            with self.assertRaises(product_store.StoreConflictError):
                store.write_draft(conflicting)
            self.assertEqual(path.read_bytes(), before)

    def test_create_publishes_immutable_revision_and_rebuilds_registry(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            store = product_store.GitStoreAdapter(root)
            store.write_draft(proposal("create-A", "CREATE", valid_asset()))

            ref = store.publish_proposal("create-A", authorization(), expected_current=None)

            self.assertEqual(ref, product_store.ProductAssetRef("A", 1))
            asset_path = root / "assets/by-id/A/revisions/r0001.json"
            original = asset_path.read_bytes()
            self.assertEqual(store.get_asset(ref), valid_asset())
            self.assertEqual(list(store.list_assets()), [valid_asset()])
            active = json.loads((root / "registry/active.json").read_text())
            self.assertEqual(
                [(item["asset_id"], item["asset_revision"]) for item in active["assets"]],
                [("A", 1)],
            )

            with self.assertRaises(product_store.StoreConflictError):
                store.publish_proposal("create-A", authorization(), expected_current=None)
            self.assertEqual(asset_path.read_bytes(), original)

    def test_publication_gate_fails_closed_before_writing_an_asset(self):
        cases = [
            authorization(approved=False),
            authorization(evidence_refs=()),
            authorization(policy="HUMAN_APPROVAL"),
        ]
        for decision in cases:
            with self.subTest(decision=decision), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                store = product_store.GitStoreAdapter(root)
                store.write_draft(proposal("create-A", "CREATE", valid_asset()))
                with self.assertRaises(product_store.PublicationGateError):
                    store.publish_proposal("create-A", decision, expected_current=None)
                self.assertFalse((root / "assets").exists())

    def test_revise_stale_and_retire_are_append_only_legal_transitions(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            store = product_store.GitStoreAdapter(root)
            first = valid_asset()
            store.write_draft(proposal("create-A", "CREATE", first))
            ref1 = store.publish_proposal("create-A", authorization(), None)
            first_bytes = (root / "assets/by-id/A/revisions/r0001.json").read_bytes()

            second = valid_asset(revision=2, supersedes={"asset_id": "A", "asset_revision": 1})
            store.write_draft(proposal("revise-A", "REVISE", second, "A"))
            ref2 = store.publish_proposal("revise-A", authorization(), ref1)
            self.assertEqual(store.get_current_ref("A"), ref2)
            self.assertEqual((root / "assets/by-id/A/revisions/r0001.json").read_bytes(), first_bytes)
            self.assertEqual(registry.rebuild_registry(root)["assets"][0]["asset_revision"], 2)

            stale = valid_asset(
                revision=3,
                publication="PUBLISHED",
                validity="STALE",
                supersedes={"asset_id": "A", "asset_revision": 2},
            )
            store.write_draft(proposal("stale-A", "MARK_STALE", stale, "A"))
            ref3 = store.publish_proposal("stale-A", authorization(), ref2)
            self.assertEqual(store.get_current_ref("A"), ref3)
            self.assertEqual(registry.rebuild_registry(root)["assets"], [])

            retired = valid_asset(
                revision=4,
                publication="RETIRED",
                validity="NOT_APPLICABLE",
                supersedes={"asset_id": "A", "asset_revision": 3},
            )
            store.write_draft(proposal("retire-A", "RETIRE", retired, "A"))
            ref4 = store.publish_proposal("retire-A", authorization(), ref3)
            self.assertEqual(store.get_current_ref("A"), ref4)
            self.assertEqual(registry.rebuild_registry(root)["assets"], [])

            next_revision = valid_asset(
                revision=5,
                supersedes={"asset_id": "A", "asset_revision": 4},
            )
            store.write_draft(proposal("revive-A", "REVISE", next_revision, "A"))
            with self.assertRaises(product_store.InvalidLifecycleTransition):
                store.publish_proposal("revive-A", authorization(), ref4)

    def test_supersession_can_replace_an_asset_id_without_mutating_history(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            store = product_store.GitStoreAdapter(root)
            store.write_draft(proposal("create-A", "CREATE", valid_asset()))
            ref1 = store.publish_proposal("create-A", authorization(), None)

            replacement = valid_asset(
                asset_id="B",
                revision=1,
                supersedes={"asset_id": "A", "asset_revision": 1},
            )
            store.write_draft(proposal("replace-A", "SUPERSEDE", replacement, "A"))
            new_ref = store.publish_proposal("replace-A", authorization(), ref1)

            self.assertEqual(new_ref, product_store.ProductAssetRef("B", 1))
            self.assertEqual(store.get_current_ref("A"), None)
            self.assertEqual(store.get_current_ref("B"), new_ref)
            active = registry.rebuild_registry(root)["assets"]
            self.assertEqual([(item["asset_id"], item["asset_revision"]) for item in active], [("B", 1)])

    def test_concurrent_cross_asset_supersede_is_atomic(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            store = product_store.GitStoreAdapter(root)
            store.write_draft(proposal("create-A", "CREATE", valid_asset()))
            current = store.publish_proposal("create-A", authorization(), None)

            for asset_id in ("B", "C"):
                replacement = valid_asset(
                    asset_id=asset_id,
                    revision=1,
                    supersedes={"asset_id": "A", "asset_revision": 1},
                )
                store.write_draft(
                    proposal(f"replace-A-with-{asset_id}", "SUPERSEDE", replacement, "A")
                )

            contenders_ready = threading.Barrier(2)
            original_write_once = product_store._write_once

            def synchronize_successor_writes(path, content):
                if path in {
                    root / "assets/by-id/B/revisions/r0001.json",
                    root / "assets/by-id/C/revisions/r0001.json",
                }:
                    try:
                        contenders_ready.wait(timeout=2)
                    except threading.BrokenBarrierError:
                        pass
                return original_write_once(path, content)

            def publish(asset_id):
                try:
                    return product_store.GitStoreAdapter(root).publish_proposal(
                        f"replace-A-with-{asset_id}", authorization(), current
                    )
                except Exception as error:
                    return error

            with patch.object(
                product_store, "_write_once", side_effect=synchronize_successor_writes
            ), ThreadPoolExecutor(max_workers=2) as executor:
                results = list(executor.map(publish, ("B", "C")))

            committed = [result for result in results if isinstance(result, product_store.ProductAssetRef)]
            rejected = [result for result in results if isinstance(result, Exception)]
            self.assertEqual(len(committed), 1)
            self.assertEqual(len(rejected), 1)
            self.assertIsInstance(rejected[0], product_store.StoreConflictError)

            durable_successors = [
                asset_id
                for asset_id in ("B", "C")
                if (root / f"assets/by-id/{asset_id}/revisions/r0001.json").exists()
            ]
            self.assertEqual(durable_successors, [committed[0].asset_id])

            rebuilt = registry.rebuild_registry(root)
            self.assertEqual(rebuilt, registry.rebuild_registry(root))
            self.assertEqual(
                [(item["asset_id"], item["asset_revision"]) for item in rebuilt["assets"]],
                [(committed[0].asset_id, 1)],
            )
            self.assertEqual(
                json.loads((root / "registry/active.json").read_text(encoding="utf-8")),
                rebuilt,
            )

    def test_stale_expected_revision_and_malformed_transition_are_conflicts(self):
        with tempfile.TemporaryDirectory() as td:
            store = product_store.GitStoreAdapter(td)
            store.write_draft(proposal("create-A", "CREATE", valid_asset()))
            ref1 = store.publish_proposal("create-A", authorization(), None)

            bad = valid_asset(revision=3, supersedes={"asset_id": "A", "asset_revision": 1})
            store.write_draft(proposal("bad-revision", "REVISE", bad, "A"))
            with self.assertRaises(product_store.InvalidLifecycleTransition):
                store.publish_proposal("bad-revision", authorization(), ref1)

            good = valid_asset(revision=2, supersedes={"asset_id": "A", "asset_revision": 1})
            store.write_draft(proposal("good-revision", "REVISE", good, "A"))
            with self.assertRaises(product_store.StoreConflictError):
                store.publish_proposal(
                    "good-revision",
                    authorization(),
                    product_store.ProductAssetRef("A", 99),
                )

    def test_registry_rejects_forks_and_descriptor_path_mismatches(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            revisions = root / "assets/by-id/A/revisions"
            revisions.mkdir(parents=True)
            (revisions / "r0001.json").write_text(json.dumps(valid_asset()))
            for revision_number in (2, 3):
                descriptor = valid_asset(
                    revision=revision_number,
                    supersedes={"asset_id": "A", "asset_revision": 1},
                )
                (revisions / f"r{revision_number:04d}.json").write_text(json.dumps(descriptor))
            with self.assertRaises(registry.RegistryConflictError):
                registry.rebuild_registry(root)

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            revisions = root / "assets/by-id/A/revisions"
            revisions.mkdir(parents=True)
            (revisions / "r0001.json").write_text(json.dumps(valid_asset(asset_id="B")))
            with self.assertRaisesRegex(ValueError, "path does not match"):
                registry.rebuild_registry(root)

    def test_registry_rejects_multiple_current_heads_for_one_asset(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            revisions = root / "assets/by-id/A/revisions"
            revisions.mkdir(parents=True)
            first = valid_asset(revision=1)
            second = valid_asset(revision=2)
            second["scope"]["products"] = ["OTHER"]
            (revisions / "r0001.json").write_text(json.dumps(first))
            (revisions / "r0002.json").write_text(json.dumps(second))

            with self.assertRaisesRegex(registry.RegistryConflictError, "multiple current revisions"):
                registry.rebuild_registry(root)

    def test_registry_replace_failure_preserves_the_previous_projection(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            out = root / "registry/active.json"
            out.parent.mkdir(parents=True)
            out.write_text('{"sentinel": true}\n')
            before = out.read_bytes()

            with patch("fdi.product_intelligence.registry.os.replace", side_effect=OSError("disk failure")):
                with self.assertRaisesRegex(OSError, "disk failure"):
                    registry.write_registry(root)

            self.assertEqual(out.read_bytes(), before)
            self.assertEqual(list(out.parent.glob(".active.json.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
