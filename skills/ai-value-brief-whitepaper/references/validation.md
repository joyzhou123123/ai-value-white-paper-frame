# Evidence validator / 证据校验

Owner 填写 [一页表](owner-intake.md)；Agent 按 [空白 JSON](evidence.template.json) 汇总和运行脚本。脚本不会替 Owner 准备证据或验证其真实性。

```bash
python3 scripts/validate_evidence.py evidence.json
python3 scripts/validate_evidence.py evidence.json --text review.txt
python3 scripts/validate_evidence.py evidence.json --languages en
```

默认要求 `language_versions` 包含 `zh` 和 `en`；只有用户明确选择单语时使用 `--languages`。`--text` 仅检查 UTF-8 文本中 `[C-001]` 等 ID 与台账的一致性，不会检查 Word/PDF 或识别所有未标注的主张。退出码：0 无本模式下检查到的问题；1 有缺失、待核或假设；2 结构、类型或算术错误。无错误不表示数据真实、权限有效、无黄底或可发布。

## Schema / 格式
`claims` 含 `id`（如 `C-001`）、`text`、`status`、`grade`、`source`、`source_role`、`source_date`、`conditions`、`publication_permission`。状态 `verified`, `partial`, `missing`, `planned`, `illustrative` 表示完整程度；证据类型 `measured`, `calculated`, `third_party`, `vendor_stated`, `hypothesis`, `illustrative` 表示证据性质。来源主体另填，第三方厂商声明不等于独立测试。权限 `confirmed`, `unknown`, `restricted`。假设和示例始终提醒待核；`verified` 不等于第三方验证。

`economics` 可省略；有数据时记录 `currency`, `region`, `price_date`, `period_years`, `assumption_status`, `quality_comparable`，以及至少两个 `options`：每项 `id`, `initial_cost`, `annual_cost`, `passed_tasks_per_year`；可报告 `reported_period_cost`, `reported_cost_per_passed_task`。可选 `comparisons` 用 `baseline_id`, `candidate_id`, `reported_period_savings` 表示“基线成本减候选成本”。数值为非负，任务量须大于零，缺失用 null。年度成本为完整年均数，包含已列的运行、人工和混合费用，防止重复；阶梯价格、变化任务量、NPV、详细敏感性和分项完整性需另行计算与复核。工具不自动验证盈亏平衡和比较公平性。

旧版 `initial_local_cost` / `annual_local_cost` / `annual_cloud_cost` 仍支持；旧 `reported_five_year_*` 仅在 `period_years=5` 时允许，否则返回错误并提示迁移，避免三年值冒充五年值。旧主张 ID 请迁移为 `C-` 前缀并添加证据类型与来源主体。
