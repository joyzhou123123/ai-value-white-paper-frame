---
name: ai-value-evidence-whitepaper
description: 撰写和审核借鉴 Signal65 公开研究方法的 AI Value 完整白皮书，覆盖真实工作负载、可复现评测、正确任务成本和商业价值，自动标黄缺口，输出中英文独立版本；Create bilingual evidence-led AI whitepapers and test plans. For a fast brief using limited materials, use ai-value-brief-whitepaper.
---

# AI Value 证据型白皮书 / Evidence-led AI Value Whitepaper

## Purpose / 适用范围
为 AI 解决方案规划、研究和写作可供企业决策的完整白皮书。借鉴 Signal65 公开研究中的任务质量、容量、可比性能和经济性方法；方法借鉴不代表 Signal65 参与、测试、认证或背书。公开研究和价格具有时效时联网核查原始来源及日期。

## Deliverables / 交付
- 默认分别交付完整中文和英文版本，除非用户明确指定只需一种；两版的数字、引用、约束、假设、图表和缺口一致，以自然的目标语言撰写。按受众和用户所选格式生成可分享的正文，可按需提供成本模型、实验方案、Owner 清单或评审摘要。
- 内容或依据不足时，无须等待用户提醒：在受影响的具体段落、主张、数字或表格单元格自动加浅黄色底色，并写明“待补充/待验证”及缺什么；英文对应 “Missing/To verify”。纯文本用 `[待补充：…]` / `[TO VERIFY: …]`。黄底必须配文字，不能仅靠颜色。无证据的内容不伪装成事实或把缺失当零；已有可靠事实正常填写。
- 面向客户的正文采用专业叙述，不混入资料整理过程、指派 Owner 或内部待办。将未核实的对外主张标黄，配独立证据缺口及 Owner 清单；尚未获准公开的证据不放入正式对外版，不自行发布、发送或上传。

## Workflow / 工作流程
1. 识别决策者、行业和地区、真实工作负载、方案范围及可公开材料；建立结论—证据—条件—权限台账。按 [中英文完整框架](references/evidence-framework.md) 对照已有、部分已有、未提供及不适用，不把“未看到”当作组织内不存在。
2. 构建证据链：客户任务与现有流程 → 对照方案 → 技术方案及配置 → 任务质量与性能 → 承载能力 → 每个合格任务成本 → 客户价值与适用边界。对 Agent 分别测任务完成、结果准确、工具调用、错误与人工介入；量化精度变化应同时验证输出质量。
3. 测试披露硬件、模型、量化、软件、测试数据与样本、输入输出长度、并发、缓存、采样、重复次数、统计及原始记录。区分总吞吐、单请求、TTFT、端到端和 P95，记录失败、稳定性；不能推导的数据标黄。
4. 构建可比基线：优先比较相同任务与质量门槛下的本地、云端或其他客户现实选项；如模型、价格或服务范围不同，披露差异，避免把性能、token 成本直接当成业务结果。来源中的未来支持、宣传数字和预测独立标注。
5. 经济分析包含完整成本、币种/地区/税费/报价日期、使用量、重试与人工、计算周期和假设。每合格任务成本 = 相关总成本 ÷ 合格任务数。计算五年成本、回收期或 ROI 只有在输入足够且条件可比时；假设示例须显著标明并标黄，提供公式及敏感性。缺失成本不默认为零，非正年度净节省不应计算正回收期。
6. 在适用时收集第三方验证、委托与独立性披露、客户授权及可公开范围。内部资料与未经证实的外部认证不得以对外事实表述；主动给出内部团队可准备项与需要外部独立验证的增强项。
7. 校验中英文一致、每项主张可追溯、数字单位及算术、黄底和文本标识、图表与正文一致及输出格式视觉质量。运行 `scripts/validate_evidence.py`（见 [校验说明](references/validation.md)）；校验仅用于发现结构、证据和数值缺口，不能代替事实核查、独立测试或授权审核。

## Reusable intake / 通用填写模板
Use [the bilingual field-by-field intake template](references/intake-template.md) when gathering information or preparing owner-fillable tables. Apply the user’s requested format and preserve empty fields with yellow fill.

## Integrated whitepaper and research capability / 综合写作与研究能力
Apply [the integrated research and editorial workflow](references/research-methods.md) at the depth appropriate to the task: reader-first argument, source discovery and critical reading, traceable references, reproducibility, visual explanation and editorial review. These capabilities are built into this skill. Original upstream skills and their tools are optional and are not bundled.

## Editorial humanization / 双语语言审校
After drafting and before final evidence and layout checks, apply [the bilingual humanizer-inspired editorial pass](references/humanizer-review.md) to both language versions. Preserve claims, figures, conditions, citations, limitations and yellow gap markers. The editorial pass is built in; the original `humanizer` skill is optional and not bundled.
