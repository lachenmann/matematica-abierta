"""Reject corrupted preparation evidence without invoking Lean."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('tlog_preflight', ROOT / 'MA-Lean/adapters/tlog_preflight.py')
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)

class TlogPreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / 'MA-Lean/mapeos/TLOG/inventory.json').read_text())
        cls.units = json.loads((ROOT / 'MA-Lean/mapeos/TLOG/units.json').read_text())
    def check_mutation(self, mutate):
        data = copy.deepcopy(self.original)
        mutate(data)
        self.assertFalse(preflight.validate(ROOT, inventory=data, units=self.units)['preparation_valid'])
    def test_canonical_preparation(self):
        result = preflight.validate(ROOT)
        self.assertTrue(result['preparation_valid'], result['errors'])
        self.assertFalse(result['formal_verification'])
    def test_duplicate_identity(self):
        self.check_mutation(lambda d: d['entries'][1].update(id=d['entries'][0]['id']))
    def test_orphan(self):
        self.check_mutation(lambda d: d['entries'][0]['depends_on'].append('TLOG-MTH-99999'))
    def test_cycle(self):
        self.check_mutation(lambda d: d['entries'][0]['depends_on'].append(d['entries'][0]['id']))
    def test_duplicate_edge(self):
        self.check_mutation(lambda d: d['entries'][1]['depends_on'].extend([d['entries'][0]['id']] * 2))
    def test_changed_proof_hash(self):
        self.check_mutation(lambda d: d['entries'][0]['source'].update(unit_sha256='0' * 64))
    def test_forged_verified_count(self):
        self.check_mutation(lambda d: d.update(verified=1))
    def test_unearned_declaration(self):
        self.check_mutation(lambda d: d['entries'][0].update(lean_declaration='False.elim'))
    def test_missing_semantic_review(self):
        self.check_mutation(lambda d: d['entries'][0].update(semantic_review='passed'))
    def test_incorrect_dependency_order(self):
        self.check_mutation(lambda d: d['topological_order'].reverse())
    def test_changed_source_text(self):
        units = copy.deepcopy(self.units)
        key = next(iter(units))
        units[key]['text'] += 'changed proof\n'
        self.assertFalse(preflight.validate(ROOT, units=units)['preparation_valid'])

if __name__ == '__main__':
    unittest.main()
