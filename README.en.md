# AI Value White Paper Frame

**[简体中文](README.md) | English**

Current version: **v2.0.0** · [Changelog](CHANGELOG.md)

A reusable AI value whitepaper framework that turns product materials, customer scenarios, test results and cost inputs into decision-oriented articles. It helps readers answer: **who a solution serves, how it performs, what value it can provide, and what supports those conclusions.**

The project provides two Codex Skills: a brief for getting started with incomplete information and an evidence-led framework for deeper testing and value analysis. The framework is not tied to a particular product, customer or industry. It defaults to separate Chinese and English deliverables; a single language can be requested.

## Start here

### 1. Choose a framework

|  | Brief whitepaper | Evidence-led whitepaper |
|---|---|---|
| Invocation | `$ai-value-brief-whitepaper` | `$ai-value-evidence-whitepaper` |
| When to use | Some material exists and a readable draft or initial customer discussion is needed | A scenario is defined and the team needs to design tests, compare options or support an investment decision |
| Main question | What is the solution, who is it for, and what do existing materials support? | Under comparable tasks and quality conditions, how do performance, capacity and cost compare? |
| When inputs are incomplete | Draft from available material and highlight specific gaps | Develop a research and validation plan and highlight unverified content |
| Typical readers | Product marketing, sales, business leads and enterprise IT | Architects, testing, procurement, finance, IT and business decision-makers |

The frameworks can be used independently. A team may start with a brief and develop an evidence-led paper as test and cost data become available.

### 2. Install

Download or clone the project, then copy `skills/ai-value-brief-whitepaper` and `skills/ai-value-evidence-whitepaper` to `~/.codex/skills/`. If same-named folders already exist, inspect them before replacing anything. Use them in a Codex session that supports Skills; if they do not appear, check the path and reopen the session.

### 3. Provide materials and invoke a skill

Name the skill explicitly with `$` in a Codex message and attach files or provide paths:

```text
Use $ai-value-brief-whitepaper to write separate Chinese and English briefs
from my solution materials for enterprise business and IT leaders. Populate
what is known, highlight gaps and unverified content in yellow, and list the
specific fields owners should complete.
```

```text
Use $ai-value-evidence-whitepaper to write Chinese and English whitepapers
from my solution, test and cost materials. Cover business tasks, comparators,
test methodology, quality, capacity and economics; highlight unsupported claims.
```

An environment with automatic discovery may select a skill from the task description; use the explicit name when a particular framework is required. Specify audience, region, length, language and a format such as Word, PDF, PPT or HTML. Available formats depend on the tools in the environment.

## What to prepare

**You can start with incomplete information.** Provide what is available; gaps will be identified in the review draft and checklist.

| Input | What to provide | If incomplete |
|---|---|---|
| Writing requirements | Solution name, audience, region, purpose, language and format | Draft from available context and flag unknowns that affect conclusions. |
| Product and solution | Overview, architecture, configuration, versions, support matrix and boundaries | Use known information; highlight unconfirmed capabilities or compatibility. |
| Customer and task | Industry, region, organization size, user role, workflow, pain points and volume | Identify gaps; label hypothetical scenarios and do not fabricate customers. |
| Tests and quality | Task samples, baseline, hardware/software, models, method, results and raw records | Retain qualified results; highlight missing conditions, quality or comparators. |
| Costs and permissions | Quotations, usage, region, currency, date, operations and disclosure permissions | Mark missing inputs or permissions; do not present illustrative assumptions as realized benefits. |

To collect inputs from owners, start with the [one-page owner intake (12 questions)](skills/ai-value-brief-whitepaper/references/owner-intake.md), then use the [detailed intake template](skills/ai-value-brief-whitepaper/references/intake-template.md) if needed. Industry, region, organization size, configuration, tests and costs are separate fields; populate existing information first.

### Use it in stages

| Stage | Suggested action | Output |
|---|---|---|
| Inventory | Use either skill to organize available and missing information | Evidence register, missing fields, suggested owners and priorities |
| Draft and review | Use the brief skill to write the paper | Chinese and English review drafts, yellow markers and a checklist |
| Validation design | Use the evidence-led skill to define tasks, baseline, quality and methods | Test plan, comparison conditions and evidence requirements |
| Analysis and delivery | Add tests, costs and permissions, then refine the paper | Bilingual whitepapers, economic analysis, sources and limitations |

## What the finished whitepaper can contain

Both formats follow the reader's decision process, with an executive summary, structured sections, supporting evidence and applicability limits. Numbers, sources and qualifications remain consistent across languages. Sections and length can be adapted to the solution, reader and evidence maturity.

### Brief: explain the solution around one customer task

The brief prioritizes available evidence and covers the customer, status quo, solution, realistic comparators, successes and failures, value and applicability. Review drafts retain yellow gaps and connect claim IDs to evidence.

### Evidence-led: support decisions under comparable conditions

| Section | Question answered | Main readers |
|---|---|---|
| Authorship and interests | Who authored, tested and funded the work, and what are their interests? | All readers |
| Executive summary | What are the customer problem, key findings and limits? | Executives |
| Customer, task and baseline | Which industry and role face what task, and how is it done today? | Business, industry teams |
| Solution and scope | What are the system, configuration, data paths and support boundaries? | Architects, IT |
| Comparators | What is the status quo, what alternatives are realistic and is comparison fair? | Solution teams, procurement |
| Results and quality | Was the task correct; what were failures, latency and capacity? | Technical and business teams |
| Customer value | What evidence supports productivity, quality, control, experience, cost and new capability? | Business, finance |
| Economics | What are lifecycle costs, cost per passed task and both-sided break-even conditions? | Finance, procurement |
| Hybrid operation | Where applicable, how do local/external routing, quality and costs behave? | Architects, operations |
| When not to choose | Which tasks fail or are better served by an alternative? | All readers |
| Whole product and deployment | Which components, integrations, partners and support exist or are missing? | Implementation, IT |
| Sources and methods | What evidence type, source, conditions and rights support each claim? | Testers, reviewers |
| Market evidence | What authorized customer references, partners or independent tests exist? | Decision-makers, legal |

[Read the brief outline](skills/ai-value-brief-whitepaper/references/brief-framework.md) · [Read the evidence-led outline](skills/ai-value-evidence-whitepaper/references/evidence-framework.md)

### How incomplete information is shown

Review drafts use pale-yellow fill on **the affected passages, numbers or table fields**, together with “Missing” or “To verify” and the evidence required; plain-text output uses text markers. Owner assignments belong in a separate checklist, while customer-facing prose remains professional. Review drafts carry “DRAFT — NOT FOR DISTRIBUTION”. A human must resolve yellow markers and review facts, test conditions and publication rights before release.

## Which skills informed the framework

These are **selective integrations of methods**, not bundles of the original skills or their entire toolchains. Both new skills include the corresponding guidance. Concrete fetching, statistical or conversion capabilities depend on the tools available in the runtime.

| Source | Problem addressed | How this project applies it |
|---|---|---|
| [Equipt `white-paper`](https://github.com/Salah-XD/equipt/tree/main/plugins/equipt-content/skills/white-paper) | How to organize an article around the reader's problem instead of product promotion | Executive summary, problem, analysis, solution, recommendation and editorial review |
| [research-paper](https://github.com/aniketkrs/research-paper) | How to make research, methods, sources and conclusions traceable | Evidence register, methods, reproducibility conditions, citations and review |
| The same project's `get-research-paper` | How to discover, screen and deduplicate research | On-demand search, primary-source reading and source assessment |
| The same project's `read-research-paper` | How to understand a paper or technical report | Extracting questions, methods, findings, limitations and applicability |
| Humanizer | How to reduce formulaic and vague AI writing | Chinese and English editorial review that preserves facts, citations and gap markers |
| Signal65 public methods | How to connect tasks, technical performance and economic value | Workloads, quality, capacity, comparable baselines and economics |

The upstream projects' complete literature-fetching, statistics, charting, conversion and other scripts **are not included**. If those skills are installed, they can be used as optional integrations. See the [integrated research workflow](skills/ai-value-evidence-whitepaper/references/research-methods.md) and [editorial review guide](skills/ai-value-evidence-whitepaper/references/humanizer-review.md).

## How this compares with Signal65 methods

This compares **aspects of public research and evaluation methods**. It does not claim to implement Signal65's complete test platform, datasets or automated graders. The user or test team must supply or perform the work in the final column; a skill cannot create measured results from nothing.

| Focus in Signal65's public methods | Corresponding element in this framework | Inputs or work required |
|---|---|---|
| Measure work outcomes around enterprise tasks | Describe customer roles, workflows, inputs, outputs and acceptance criteria | Supply representative tasks, samples and verifiable acceptance rules. |
| Separate task quality and system capacity | Report completion quality, errors, latency, throughput and concurrency separately | Measure successful and failed tasks, per-request experience and different concurrency levels. |
| Compare systems under task or service conditions | Define baselines, workloads, configurations and quality thresholds; disclose differences | Prepare realistic alternatives and comparable tests, or explain mismatches. |
| Relate work outcomes to costs | Calculate total cost, cost per passed task and sensitivity | Supply prices, usage, cost boundaries, pass rates and time horizon. |
| Disclose methods and limitations | Document sources, configuration, test date, statistics and disclosures | Retain test records and verify citation and publication rights. |

Method references: [Measuring Correct Work](https://pinnacle.signal65.com/measuring-correct-work-pg-1/), [The Economics of Agentic AI](https://signal65.com/wp-content/uploads/2026/05/Signal65-Insights_The-Economics-of-Agentic-AI.pdf), and [The New Economics of AI Inference](https://signal65.com/research/ai/from-dense-to-mixture-of-experts-the-new-economics-of-ai-inference/). Signal65 studies may have specific partners, models and assumptions. This framework adapts methods; it **does not imply Signal65 participation, certification, testing or endorsement**.

## How to check evidence and economics

Each skill includes a Python standard-library script, `scripts/validate_evidence.py`. Copy the [blank JSON template](skills/ai-value-brief-whitepaper/references/evidence.template.json), fill it in as `evidence.json` using the [validation guide](skills/ai-value-brief-whitepaper/references/validation.md), or ask Codex to organize the inputs from the one-page intake for an owner to review.

From the project root:

```bash
python3 skills/ai-value-brief-whitepaper/scripts/validate_evidence.py evidence.json
```

The evidence-led script is at `skills/ai-value-evidence-whitepaper/scripts/validate_evidence.py`. It checks structured evidence, statuses, evidence grades, publication-permission status, multi-option period costs and simplified arithmetic. `--text review.txt` checks claim IDs such as `[C-001]` in plain text; `--languages en` applies when a single-language output was explicitly requested: exit code `0` means no structural or completeness flags, `1` means missing or unverified items, and `2` means invalid JSON, schema or arithmetic. It **cannot** establish source truth, test reproducibility or valid authorization, and does not independently review an entire document.

## Project structure and credits

```text
README.md / README.en.md
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── references/       # outlines, credibility, one-page intake, research and validation
└── scripts/validate_evidence.py
```

Method sources: Equipt `white-paper` by Salah-XD, skill content under [CC BY 4.0](https://github.com/Salah-XD/equipt/blob/main/LICENSE-CONTENT); `research-paper` by Aniket Kumar under [MIT](https://github.com/aniketkrs/research-paper/blob/main/LICENSE); Humanizer-inspired editorial guidance draws on [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). This project selectively adapts methods and does not imply participation or endorsement by those authors or organizations.

Internal material without confirmed publication permission must not be presented as authorized public content. Do not upload sensitive working files to a public repository; the skills do not send or publish automatically.
