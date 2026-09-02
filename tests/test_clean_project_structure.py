from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CleanProjectStructureTests(unittest.TestCase):
    def test_normal_project_top_level_exists(self):
        for name in [
            'governance','specs','contracts','skills','workflows','src','validation',
            'tests','config','templates','scripts','archive'
        ]:
            self.assertTrue((ROOT/name).exists(), name)

    def test_recovery_top_level_names_are_absent(self):
        for name in ['normative','candidates','implementation','recovery-reference','multica','product-intelligence-template']:
            self.assertFalse((ROOT/name).exists(), name)

    def test_project_is_named_clean_baseline(self):
        self.assertEqual((ROOT/'VERSION').read_text().strip(), '0.4.8.2')
        self.assertTrue((ROOT/'MULTICA-PROJECT-PROMPT.txt').exists())

if __name__ == '__main__':
    unittest.main()
