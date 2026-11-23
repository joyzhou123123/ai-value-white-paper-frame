# 版本更新记录 / Changelog

## v2.0.0 — 2026-11-23

### 中文

- 补充框架价值、证据链、客户价值与 Signal65 方法的对照说明。
- 精简中英文 README，新增模板界面预览和中英文可编辑模板下载包。
- 新增不含具体方案资料的中英文可编辑 HTML 模板，可编辑正文、填写 Owner 表格、在浏览器暂存并下载。

- 统一简版和证据型白皮书结构，增加利益披露、客户价值、对照方案、失败结果与不适用场景。
- 新增 12 问的一页 Owner 填写入口；保留详细字段、中英文默认输出、缺口标黄和语言审校。
- 新增证据类型、来源角色与正文主张 ID 的关联检查；扩展多方案、实际核算周期和合格任务成本的校验。
- 为相关场景补充混合 AI、设备测试条件和模型时效的写作方法，并加入审阅稿发布提示。
- 增加自动化测试和两套 Skill 共享文件的一致性检查。

**迁移说明：**旧版 `reported_five_year_*` 字段只在 `period_years` 为 5 时有效；其他周期请迁移到 `options` 和 `reported_period_*`。原有主张 ID 需要改为 `C-` 前缀，并补充 `grade` 和 `source_role`。完整字段及局限见[校验说明](skills/ai-value-brief-whitepaper/references/validation.md)。

### English

- Expand the framework value, evidence chain, customer-value analysis and Signal65 methodology comparison.
- Simplify the bilingual READMEs and add template screenshots and a downloadable template bundle.
- Add generic editable Chinese and English HTML templates with narrative editing, owner tables, browser storage and downloadable copies.

- Align the brief and evidence-led outlines; add disclosure, customer value, comparators, failures and unsuitable cases.
- Add a 12-question one-page owner intake while retaining detailed fields, bilingual defaults, yellow gap markers and editorial review.
- Add evidence grades, source roles and claim-ID checks; validate multiple options, the actual accounting period and cost per passed task.
- Add applicable hybrid AI, device-test and model-currency guidance and review-draft publication labels.
- Add automated tests and a consistency check for files shared by the two skills.

**Migration:** Legacy `reported_five_year_*` fields are accepted only when `period_years` is 5. For other periods migrate to `options` and `reported_period_*`. Existing claim IDs must use the `C-` prefix and include `grade` and `source_role`. See the [validation guide](skills/ai-value-brief-whitepaper/references/validation.md) for the schema and limitations.
