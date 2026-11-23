# AI Value White Paper Frame

**[简体中文](README.md) | English**

Turn existing solution materials into an enterprise AI value whitepaper. This project provides **brief** and **evidence-led** skills, plus editable Chinese and English HTML templates.

## See the template

The image below shows the English template. The narrative is editable, owners can fill the tables, and pale yellow marks missing or unverified content.

![English whitepaper template preview](docs/images/template-preview-en.png)

**[Download editable templates in Chinese and English (ZIP)](https://github.com/joyzhou123123/ai-value-white-paper-frame/releases/download/v2.0.0/AI-Value-Editable-Templates.zip)**

Unzip the file and open `editable-whitepaper-en.html` or `editable-whitepaper-zh.html` in a browser. Select **Edit paper** to edit the narrative; owners can type directly in pale-yellow cells. Select **Download edited HTML** to save a copy.

> GitHub displays HTML as source code rather than running the template. Download the ZIP and open the file in your browser. Changes are stored only in the current browser and are not shared live; send the downloaded HTML when collaborating.

## Choose a skill

| | Brief whitepaper | Evidence-led whitepaper |
|---|---|---|
| Skill | `$ai-value-brief-whitepaper` | `$ai-value-evidence-whitepaper` |
| Best for | Writing an initial paper from incomplete materials | Evaluating tests, alternatives, task quality and economic value |
| Answers | What is the solution, who is it for and what is already supported? | How does it perform and cost under comparable conditions, and where are its limits? |
| Typical uses | Internal review, first customer conversations and organizing materials | PoC review, procurement, systematic tests and investment decisions |

Both skills default to separate Chinese and English outputs; request one language if preferred. Specific missing or unverified content receives a pale-yellow marker and a text label.

## Use a skill

1. Copy the two skill folders under `skills/` to `~/.codex/skills/`. Inspect any existing same-named folders before replacing them.
2. In a Codex session that supports Skills, attach available solution, test or cost materials and specify your audience, region and output format.
3. Name the skill in your prompt, for example:

```text
Use $ai-value-brief-whitepaper to create Chinese and English whitepapers from
my materials. Produce editable HTML, fill known content, highlight gaps in
yellow and list the fields owners need to complete.
```

For a fuller evaluation, use `$ai-value-evidence-whitepaper`. You can start with incomplete information; the skill uses what is available and identifies the evidence needed. For team input, start with the [one-page owner intake](skills/ai-value-brief-whitepaper/references/owner-intake.md).

## What you get

A paper normally follows the decision: **customer problem and baseline → solution and configuration → realistic alternatives → test results and quality → customer value → economics → limitations → sources and disclosures**.

The brief creates a readable starting point. The evidence-led paper goes further into workloads, methods, successes and failures, capacity and cost sensitivity. [Brief outline](skills/ai-value-brief-whitepaper/references/brief-framework.md) · [Evidence-led outline](skills/ai-value-evidence-whitepaper/references/evidence-framework.md)

## Methods that informed the framework

| Source | Problem it helps address |
|---|---|
| [Equipt white-paper](https://github.com/Salah-XD/equipt/tree/main/plugins/equipt-content/skills/white-paper) | Organizing the summary, analysis and recommendation around the reader's problem. |
| [research-paper](https://github.com/aniketkrs/research-paper) | Organizing research sources, methods, citations and review. |
| Humanizer | Reducing formulaic language while preserving facts, figures and limits. |
| Signal65 public methods | Connecting real tasks, quality, capacity and cost. |

The Signal65 comparison centers on **whether work is correct, how much work a system handles, cost per passed task and reproducible conditions**. Adapting methods does not imply Signal65 participation, testing, certification or endorsement. [Signal65 methodology](https://pinnacle.signal65.com/measuring-correct-work-pg-1/) · [Detailed methods in this project](skills/ai-value-evidence-whitepaper/references/research-methods.md)

This project includes adapted working methods, not the upstream projects' complete literature-fetching, statistics or conversion toolchains.

## Validation and publication

Each skill includes a structured evidence and economics validator. Ask Codex to prepare inputs using the [JSON template](skills/ai-value-brief-whitepaper/references/evidence.template.json) and run it; see the [validation guide](skills/ai-value-brief-whitepaper/references/validation.md). The script does not replace fact-checking, independent testing or authorization review.

Yellow markers and the draft label are for internal review. Review facts, test conditions and publication rights before releasing a paper externally.

---

Current version: **v2.0.0** · [Changelog](CHANGELOG.md) · [Project files](skills/)

Method credits: Equipt skill content is licensed [CC BY 4.0](https://github.com/Salah-XD/equipt/blob/main/LICENSE-CONTENT); research-paper is licensed [MIT](https://github.com/aniketkrs/research-paper/blob/main/LICENSE); editorial guidance refers to [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
