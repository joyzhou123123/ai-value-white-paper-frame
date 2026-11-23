#!/usr/bin/env python3
"""Check structured evidence and simple period-based cost calculations."""
import argparse
import json
import math
import re
import sys
from pathlib import Path

STATUSES = {'verified', 'partial', 'missing', 'planned', 'illustrative'}
GRADES = {'measured', 'calculated', 'third_party', 'vendor_stated', 'hypothesis', 'illustrative'}
PERMISSIONS = {'confirmed', 'unknown', 'restricted'}


def number(value, *, positive=False):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and (value > 0 if positive else value >= 0))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', help='Evidence JSON file')
    parser.add_argument('--text', help='UTF-8 review text; check [C-...] claim IDs')
    parser.add_argument('--languages', default='zh,en', help='Required languages, e.g. zh,en or en')
    args = parser.parse_args(argv)
    try:
        data = json.loads(Path(args.file).read_text(encoding='utf-8'))
        paper = Path(args.text).read_text(encoding='utf-8') if args.text else None
    except (OSError, ValueError) as exc:
        print(f'ERROR: Cannot load input: {exc}', file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print('ERROR: Root must be an object')
        return 2
    errors, missing = [], []
    required = {x.strip() for x in args.languages.split(',') if x.strip()}
    if not required or not required.issubset({'zh', 'en'}):
        errors.append('languages: choose zh and/or en')
    languages = data.get('language_versions')
    if not isinstance(languages, list) or not required.issubset({x for x in languages if isinstance(x, str)}):
        missing.append('language_versions: required output languages missing')
    claims = data.get('claims')
    if not isinstance(claims, list) or not claims:
        errors.append('claims: non-empty array required')
        claims = []
    ids = set()
    for idx, claim in enumerate(claims, 1):
        if not isinstance(claim, dict):
            errors.append(f'claims[{idx}]: expected object')
            continue
        key = claim.get('id')
        if not isinstance(key, str) or not re.fullmatch(r'C-[A-Za-z0-9_-]+', key):
            errors.append(f'claims[{idx}]: id must start with C- and contain letters, numbers, _ or -')
            continue
        if key in ids:
            errors.append(f'{key}: duplicate id')
        ids.add(key)
        if not isinstance(claim.get('text'), str) or not claim['text'].strip():
            missing.append(f'{key}: claim text')
        status = claim.get('status')
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f'{key}: invalid status')
        elif status != 'verified':
            missing.append(f'{key}: status is {status}; highlight affected content')
        grade = claim.get('grade')
        if grade is None or grade == '':
            missing.append(f'{key}: evidence grade')
        elif not isinstance(grade, str) or grade not in GRADES:
            errors.append(f'{key}: invalid evidence grade')
        elif grade in {'hypothesis', 'illustrative'}:
            missing.append(f'{key}: {grade} is not an established result')
        for field in ('source', 'source_date', 'conditions', 'source_role'):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                missing.append(f'{key}: {field}')
        permission = claim.get('publication_permission')
        if not isinstance(permission, str) or permission not in PERMISSIONS:
            errors.append(f'{key}: invalid publication_permission')
        elif permission != 'confirmed':
            missing.append(f'{key}: publication permission is {permission}')
    if paper is not None:
        cited = set(re.findall(r'\[(C-[A-Za-z0-9_-]+)\]', paper))
        for key in sorted(ids - cited):
            missing.append(f'{key}: absent from review text')
        for key in sorted(cited - ids):
            errors.append(f'{key}: cited in review text but absent from evidence register')

    def check_reported(container, field, expected):
        actual = container.get(field)
        if actual is None:
            return
        if not isinstance(actual, (int, float)) or isinstance(actual, bool) or not math.isfinite(actual):
            errors.append(f'economics: invalid {field}')
        elif not math.isclose(actual, expected, rel_tol=0.001, abs_tol=0.02):
            errors.append(f'economics: {field}={actual}; expected {expected:.2f}')

    if 'economics' in data:
        econ = data['economics']
        if not isinstance(econ, dict):
            errors.append('economics: expected object')
        else:
            for field in ('currency', 'region', 'price_date'):
                if not isinstance(econ.get(field), str) or not econ[field].strip():
                    missing.append(f'economics: {field}')
            if not isinstance(econ.get('assumption_status'), str) or econ['assumption_status'] not in {'verified', 'partial', 'missing', 'illustrative'}:
                errors.append('economics: invalid assumption_status')
            elif econ['assumption_status'] != 'verified':
                missing.append('economics: assumptions are unverified; highlight inputs and outputs')
            if econ.get('quality_comparable') is not True:
                missing.append('economics: comparable task quality not established')
            years = econ.get('period_years')
            if years is None:
                missing.append('economics: period_years')
            elif not number(years, positive=True):
                errors.append('economics: invalid period_years')
            if 'options' in econ:
                options = econ['options']
                if not isinstance(options, list) or len(options) < 2:
                    errors.append('economics: options must contain at least two alternatives')
                    options = []
                totals = {}
                for option in options:
                    if not isinstance(option, dict) or not isinstance(option.get('id'), str) or not option['id'].strip():
                        errors.append('economics: each option requires a non-empty id')
                        continue
                    key = option['id']
                    if key in totals:
                        errors.append(f'economics: duplicate option id {key}')
                        continue
                    totals[key] = None
                    for field in ('initial_cost', 'annual_cost', 'passed_tasks_per_year'):
                        value = option.get(field)
                        if value is None:
                            missing.append(f'economics: {key}.{field}')
                        elif not number(value, positive=(field == 'passed_tasks_per_year')):
                            errors.append(f'economics: invalid {key}.{field}')
                    if (number(years, positive=True) and number(option.get('initial_cost'))
                            and number(option.get('annual_cost'))):
                        total = option['initial_cost'] + years * option['annual_cost']
                        totals[key] = total
                        check_reported(option, 'reported_period_cost', total)
                        if number(option.get('passed_tasks_per_year'), positive=True):
                            check_reported(option, 'reported_cost_per_passed_task',
                                           total / (years * option['passed_tasks_per_year']))
                comparisons = econ.get('comparisons', [])
                if not isinstance(comparisons, list):
                    errors.append('economics: comparisons must be an array')
                    comparisons = []
                for comp in comparisons:
                    if (not isinstance(comp, dict) or not isinstance(comp.get('baseline_id'), str)
                            or not isinstance(comp.get('candidate_id'), str)
                            or comp['baseline_id'] not in totals or comp['candidate_id'] not in totals):
                        errors.append('economics: comparison references an unknown option')
                        continue
                    base, candidate = totals[comp['baseline_id']], totals[comp['candidate_id']]
                    if base is not None and candidate is not None:
                        check_reported(comp, 'reported_period_savings', base - candidate)
            else:
                # Legacy schema: five-year names remain valid ONLY for a five-year period.
                fields = ('initial_local_cost', 'annual_local_cost', 'annual_cloud_cost')
                for field in fields:
                    value = econ.get(field)
                    if value is None:
                        missing.append(f'economics: {field}')
                    elif not number(value):
                        errors.append(f'economics: invalid {field}')
                legacy = ('reported_five_year_local_cost', 'reported_five_year_cloud_cost', 'reported_five_year_savings')
                if number(years, positive=True) and years != 5 and any(econ.get(x) is not None for x in legacy):
                    errors.append('economics: reported_five_year_* requires period_years = 5; migrate to options/reported_period_*')
                if number(years, positive=True) and all(number(econ.get(f)) for f in fields):
                    local = econ['initial_local_cost'] + years * econ['annual_local_cost']
                    cloud = years * econ['annual_cloud_cost']
                    if years == 5:
                        for name, val in zip(legacy, (local, cloud, cloud - local)):
                            check_reported(econ, name, val)
                    net = econ['annual_cloud_cost'] - econ['annual_local_cost']
                    if net > 0:
                        check_reported(econ, 'reported_payback_months', 12 * econ['initial_local_cost'] / net)
                    elif econ.get('reported_payback_months') is not None:
                        errors.append('economics: payback is undefined for nonpositive annual savings')
    for item in errors:
        print('ERROR:', item)
    for item in missing:
        print('MISSING:', item)
    print(f'Result: {len(errors)} error(s), {len(missing)} missing/unverified item(s).')
    return 2 if errors else 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
