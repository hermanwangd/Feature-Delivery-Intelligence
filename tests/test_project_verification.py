import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProjectVerificationTests(unittest.TestCase):
    def test_git_worktree_marker_is_not_bundle_content(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = root / "payload.txt"
            payload.write_text("payload\n")
            (root / ".git").write_text("gitdir: somewhere\n")
            manifest = {
                "schema_version": "1.0",
                "bundle": "fixture",
                "files": [
                    {
                        "path": "payload.txt",
                        "sha256": hashlib.sha256(payload.read_bytes()).hexdigest(),
                        "size": payload.stat().st_size,
                    }
                ],
            }
            (root / "BUNDLE-MANIFEST.json").write_text(json.dumps(manifest))

            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/verify_project.py"), str(root)],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("0 failures / 0 unexpected", result.stdout)


if __name__ == "__main__":
    unittest.main()
