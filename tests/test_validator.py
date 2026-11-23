import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [ROOT / 'skills' / name / 'scripts' / 'validate_evidence.py' for name in
           ('ai-value-brief-whitepaper', 'ai-value-evidence-whitepaper')]
BASE = {
    'language_versions': ['zh', 'en'],
    'claims': [{'id': 'C-001', 'text': 'A test result', 'status': 'verified',
                'grade': 'measured', 'source': 'Report', 'source_role': 'internal test team',
                'source_date': '2026-01-01', 'conditions': 'specified workload',
                'publication_permission': 'confirmed'}],
    'economics': {'currency': 'EUR', 'region': 'EU', 'price_date': '2026-01-01',
                  'period_years': 3, 'assumption_status': 'verified', 'quality_comparable': True,
                  'options': [{'id': 'current', 'initial_cost': 0, 'annual_cost': 40,
                               'passed_tasks_per_year': 10, 'reported_period_cost': 120,
                               'reported_cost_per_passed_task': 4},
                              {'id': 'candidate', 'initial_cost': 30, 'annual_cost': 20,
                               'passed_tasks_per_year': 10, 'reported_period_cost': 90,
                               'reported_cost_per_passed_task': 3}],
                  'comparisons': [{'baseline_id': 'current', 'candidate_id': 'candidate',
                                   'reported_period_savings': 30}]}}


class ValidationTests(unittest.TestCase):
    def run_both(self, data, expected, *args, text=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.json'
            path.write_text(json.dumps(data))
            extra = list(args)
            if text is not None:
                text_path = Path(tmp) / 'review.txt'
                text_path.write_text(text)
                extra += ['--text', str(text_path)]
            for script in SCRIPTS:
                result = subprocess.run([sys.executable, str(script), str(path), *extra],
                                        text=True, capture_output=True, check=False)
                self.assertEqual(result.returncode, expected, (script, result.stdout, result.stderr))

    def test_valid_three_year_multi_option_and_claim_link(self):
        self.run_both(BASE, 0, text='Reported result [C-001].')

    def test_missing_grade_and_hypothesis_are_flagged(self):
        data = copy.deepcopy(BASE)
        data['claims'][0]['grade'] = 'hypothesis'
        self.run_both(data, 1)
        data['claims'][0]['grade'] = ''
        self.run_both(data, 1)

    def test_wrong_cost_and_unknown_claim_are_rejected(self):
        data = copy.deepcopy(BASE)
        data['economics']['options'][1]['reported_period_cost'] = 91
        self.run_both(data, 2)
        self.run_both(BASE, 2, text='Unknown [C-999]')

    def test_old_five_year_field_rejects_three_year_period(self):
        data = copy.deepcopy(BASE)
        data['economics'] = {'currency': 'EUR', 'region': 'EU', 'price_date': '2026-01-01',
                             'period_years': 3, 'assumption_status': 'verified',
                             'quality_comparable': True, 'initial_local_cost': 10,
                             'annual_local_cost': 2, 'annual_cloud_cost': 8,
                             'reported_five_year_local_cost': 16}
        self.run_both(data, 2)

    def test_single_language_is_explicit(self):
        data = copy.deepcopy(BASE)
        data['language_versions'] = ['en']
        self.run_both(data, 1)
        self.run_both(data, 0, '--languages', 'en')

    def test_missing_inputs_are_not_zero_and_invalid_types_are_handled(self):
        data = copy.deepcopy(BASE)
        data['economics']['options'][1]['annual_cost'] = None
        self.run_both(data, 1)
        data['claims'][0]['status'] = []
        self.run_both(data, 2)

    def test_nonpositive_savings_never_has_positive_payback(self):
        data = copy.deepcopy(BASE)
        data['economics'] = {'currency': 'EUR', 'region': 'EU', 'price_date': '2026-01-01',
                             'period_years': 5, 'assumption_status': 'verified',
                             'quality_comparable': True, 'initial_local_cost': 100,
                             'annual_local_cost': 40, 'annual_cloud_cost': 20,
                             'reported_payback_months': 4}
        self.run_both(data, 2)

    def test_duplicate_shared_files_in_sync(self):
        left, right = [script.parents[1] for script in SCRIPTS]
        shared = ['scripts/validate_evidence.py', 'references/credibility-and-economics.md',
                  'references/owner-intake.md', 'references/validation.md',
                  'references/evidence.template.json', 'references/intake-template.md',
                  'references/research-methods.md', 'references/humanizer-review.md',
                  'references/editable-html.md', 'assets/editable-whitepaper-zh.html',
                  'assets/editable-whitepaper-en.html']
        for name in shared:
            self.assertEqual((left / name).read_bytes(), (right / name).read_bytes(), name)


if __name__ == '__main__':
    unittest.main()
