# Evidence validator / 证据校验

Copy `references/evidence.template.json` to a working file and fill it in. Run `python3 scripts/validate_evidence.py evidence.json` (from the skill directory or with an absolute script path). It prints a readable list of `ERROR` and `MISSING` items and a final result. Exit 0 means no structural or completeness flags under this schema; 1 means missing/unverified data; 2 means invalid JSON/schema or invalid arithmetic. It does not validate factual accuracy, privacy, publication authorization, quality of sources, or every claim in a document. The writer must inspect the output and highlight corresponding passages in the deliverable.

Schema example (replace with real inputs; omit `economics` when not applicable):

```json
{
  "language_versions": ["zh", "en"],
  "claims": [
    {"id":"P1", "text":"A specified test result", "status":"verified", "source":"Report section 4", "source_date":"2026-11-11", "conditions":"model, hardware and workload", "publication_permission":"confirmed"},
    {"id":"P2", "text":"Customer benefit", "status":"missing", "source":"", "source_date":"", "conditions":"", "publication_permission":"unknown"}
  ],
  "economics": {
    "currency":"EUR", "region":"EU", "price_date":"2026-11-01", "period_years":5,
    "initial_local_cost":100, "annual_local_cost":10, "annual_cloud_cost":40,
    "reported_five_year_local_cost":150, "reported_five_year_cloud_cost":200,
    "reported_five_year_savings":50, "reported_payback_months":40,
    "assumption_status":"illustrative", "quality_comparable":true
  }
}
```

Valid statuses: `verified`, `partial`, `missing`, `planned`, `illustrative`; permission: `confirmed`, `unknown`, `restricted`. `verified` means source-backed, not independently verified. The optional reported values are cross-checked using simple constant annual cost arithmetic only; assumptions are not automatically actual costs. `illustrative` values always flag for yellow review, even if arithmetically consistent. Fill unknown fields with empty strings or null; never invent values.
