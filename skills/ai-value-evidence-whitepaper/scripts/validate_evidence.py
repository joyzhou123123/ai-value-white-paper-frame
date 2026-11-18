#!/usr/bin/env python3
"""Flag missing evidence and cross-check simple five-year cost arithmetic."""
import json, math, sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 validate_evidence.py evidence.json', file=sys.stderr); return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        print(f'ERROR: Cannot load JSON: {exc}', file=sys.stderr); return 2
    if not isinstance(data, dict):
        print('ERROR: Root must be an object'); return 2
    missing, errors = [], []
    languages=data.get('language_versions')
    if not isinstance(languages, list) or not {'zh','en'}.issubset(set(x for x in languages if isinstance(x,str))):
        missing.append('language_versions: provide zh and en unless a single language was explicitly requested')
    claims=data.get('claims')
    if not isinstance(claims,list) or not claims:
        errors.append('claims: non-empty array required')
        claims=[]
    seen=set()
    for i,c in enumerate(claims,1):
        if not isinstance(c,dict): errors.append(f'claims[{i}]: expected object'); continue
        key=c.get('id')
        if not isinstance(key,str) or not key.strip(): errors.append(f'claims[{i}]: id required'); key=str(i)
        elif key in seen: errors.append(f'{key}: duplicate id')
        seen.add(key)
        if not isinstance(c.get('text'),str) or not c['text'].strip(): missing.append(f'{key}: claim text')
        status=c.get('status')
        if status not in ('verified','partial','missing','planned','illustrative'): errors.append(f'{key}: invalid status')
        elif status!='verified': missing.append(f'{key}: status is {status}; highlight affected content')
        for field in ('source','source_date','conditions'):
            if not isinstance(c.get(field),str) or not c[field].strip(): missing.append(f'{key}: {field}')
        perm=c.get('publication_permission')
        if perm not in ('confirmed','unknown','restricted'): errors.append(f'{key}: invalid publication_permission')
        elif perm!='confirmed': missing.append(f'{key}: publication permission is {perm}')
    if 'economics' in data:
        e=data['economics']
        if not isinstance(e,dict): errors.append('economics: expected object')
        else:
            for field in ('currency','region','price_date'):
                if not isinstance(e.get(field),str) or not e[field].strip(): missing.append(f'economics: {field}')
            if e.get('assumption_status') not in ('verified','partial','missing','illustrative'): errors.append('economics: invalid assumption_status')
            elif e['assumption_status']!='verified': missing.append('economics: assumptions are not verified; highlight assumptions and outputs')
            if e.get('quality_comparable') is not True: missing.append('economics: comparable task quality not established')
            fields=('period_years','initial_local_cost','annual_local_cost','annual_cloud_cost')
            for field in fields:
                x=e.get(field)
                if x is None: missing.append(f'economics: {field}')
                elif isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0 or (field=='period_years' and x==0): errors.append(f'economics: invalid {field}')
            valid=all(isinstance(e.get(k),(int,float)) and not isinstance(e.get(k),bool) and math.isfinite(e[k]) and e[k]>=0 for k in fields) and e.get('period_years',0)>0
            if valid:
                years=e['period_years']; local=e['initial_local_cost']+years*e['annual_local_cost']; cloud=years*e['annual_cloud_cost']; savings=cloud-local
                checks={'reported_five_year_local_cost':local,'reported_five_year_cloud_cost':cloud,'reported_five_year_savings':savings}
                net=e['annual_cloud_cost']-e['annual_local_cost']
                if net>0: checks['reported_payback_months']=12*e['initial_local_cost']/net
                elif e.get('reported_payback_months') is not None: errors.append('economics: payback is undefined for nonpositive annual savings')
                for name,expected in checks.items():
                    if name not in e or e[name] is None: continue
                    actual=e[name]
                    if isinstance(actual,bool) or not isinstance(actual,(int,float)) or not math.isfinite(actual): errors.append(f'economics: invalid {name}')
                    elif not math.isclose(actual,expected,rel_tol=0.001,abs_tol=0.02): errors.append(f'economics: {name}={actual}; expected {expected:.2f}')
    for x in errors: print('ERROR:',x)
    for x in missing: print('MISSING:',x)
    print(f'Result: {len(errors)} error(s), {len(missing)} missing/unverified item(s).')
    return 2 if errors else 1 if missing else 0

if __name__=='__main__': sys.exit(main())
