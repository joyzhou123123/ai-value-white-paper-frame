# AI Value White Paper Frame

**简体中文 | [English](README.en.md)**

一套可复用的 AI Value 白皮书写作框架。它把产品资料、客户场景、测试结果和成本数据组织成面向企业读者的文章，帮助团队回答：**方案适合谁、表现如何、能带来什么价值，以及结论有什么依据。**

项目提供两套 Codex Skills：资料不足时可先写简版；需要系统评测和价值论证时使用证据型版本。框架不绑定特定产品、客户或行业。默认分别输出中文和英文版本，也可指定只输出一种语言。

## 从这里开始

### 1. 选择框架

|  | 简版白皮书 | 证据型白皮书 |
|---|---|---|
| 调用名称 | `$ai-value-brief-whitepaper` | `$ai-value-evidence-whitepaper` |
| 适合什么时候使用 | 已有部分方案资料，需要尽快形成可阅读的初稿或客户沟通材料 | 已有明确场景，需要设计测试、比较方案，或支撑采购和投资评估 |
| 主要解决什么问题 | 方案是什么、适合谁、现有资料可以证明什么 | 在可比任务和质量条件下，方案表现、容量和成本如何 |
| 信息不齐时 | 先写已有内容，具体缺口标黄 | 形成研究与验证计划，未证实的内容标黄 |
| 典型读者 | 产品市场、销售、业务负责人、企业 IT | 架构师、测试、采购、财务、IT 和业务决策者 |

两套框架可以独立使用。也可以先用简版汇总资料，再在测试和成本数据成熟后使用证据型版本深化。

### 2. 安装

下载或克隆本项目，将 `skills/ai-value-brief-whitepaper` 和 `skills/ai-value-evidence-whitepaper` 两个文件夹复制到 `~/.codex/skills/`。若已存在同名文件夹，请先检查内容，避免覆盖现有工作。安装后在支持 Skills 的 Codex 会话中使用；如果没有出现，检查路径并重新打开会话。

### 3. 提供资料并触发

在 Codex 消息中使用 `$` 名称明确指定 Skill，并附上资料文件或路径。例如：

```text
使用 $ai-value-brief-whitepaper，基于我提供的方案资料，写中英文简版白皮书。
读者是企业业务与 IT 负责人。已有内容先写进去，缺失和待验证的内容标黄，
另外列出各 Owner 需要补充的具体字段。
```

```text
使用 $ai-value-evidence-whitepaper，根据我提供的方案、测试和成本资料，
写中英文白皮书。请覆盖业务任务、对照方案、测试方法、质量、容量和经济性，
并把缺失依据的具体内容标黄。
```

支持自动发现的环境也可能根据任务描述选择 Skill；如果要指定框架，建议显式使用上面的名称。用户可指定受众、地区、字数、语言和 Word、PDF、PPT、HTML 等交付格式；可用格式取决于运行环境的工具能力。

## 使用前准备什么

**不需要等资料齐全才开始。** 提供已有内容即可，缺项会进入审阅稿和补充清单。

| 资料 | 具体可以提供什么 | 资料不足时 |
|---|---|---|
| 写作要求 | 方案名称、读者、地区、用途、语言、格式 | 按已有上下文拟定，影响结论的未知项标注出来。 |
| 产品与方案 | 介绍、架构、配置、版本、支持清单、部署边界 | 先写已知内容；未确认的能力或兼容性标黄。 |
| 客户与任务 | 行业、地区、组织规模、用户角色、工作流程、痛点和用量 | 明确缺口；使用示例时说明是假设，不虚构客户案例。 |
| 测试与质量 | 任务样本、基线、软硬件、模型、测试方法、结果与原始记录 | 保留有条件的结果；缺失条件、质量和对照信息标黄。 |
| 成本与权限 | 报价、使用量、地区、币种、时间、运维、案例及数据公开授权 | 标注未获数据或授权；演示假设不写成实际收益。 |

需要让各位 Owner 填写时，可以复制[通用中英文填写模板](skills/ai-value-brief-whitepaper/references/intake-template.md)。行业、地区、组织规模、配置、测试和成本等均拆成独立字段，已有内容先填写。

### 可以分阶段使用

| 阶段 | 建议操作 | 输出 |
|---|---|---|
| 资料盘点 | 用任一 Skill 整理已有和缺失内容 | 证据清单、缺失字段、建议 Owner 与优先级 |
| 首稿与评审 | 用简版 Skill 形成正文 | 中英文审阅稿、黄色标记和补充清单 |
| 设计验证 | 用证据型 Skill 定义任务、基线、质量与测试方法 | 测试方案、对照条件和补证计划 |
| 分析与交付 | 补入测试、成本及权限信息，完善文章 | 中英文白皮书、经济分析、来源与限制 |

## 最后可以形成什么样的白皮书

两套均以客户决策为主线，包含正式的执行摘要、章节结构、依据和适用边界；中英文版本的数字、来源及限制保持一致。具体章节和篇幅按方案、读者与证据成熟度调整。

### 简版：帮助读者理解方案与已有价值

| 章节 | 回答的问题 | 主要读者 |
|---|---|---|
| 执行摘要 | 方案解决什么问题，当前结论是什么？ | 管理层、客户负责人 |
| 业务挑战与场景 | 谁在什么工作中遇到什么问题？ | 业务、销售 |
| 方案与工作原理 | 方案如何工作，配置和支持范围是什么？ | IT、架构师 |
| 性能与价值 | 现有结果及条件是什么，意味着什么？ | 技术与业务团队 |
| 经济性 | 已知成本、收益和计算依据是什么？ | 采购、财务 |
| 部署与适用边界 | 落地要求及限制是什么？ | 实施、运维 |
| 来源与方法 | 数字从哪里来，如何解读？ | 审阅人、技术团队 |

[查看简版详细框架](skills/ai-value-brief-whitepaper/references/brief-framework.md)

### 证据型：帮助读者评估和比较

| 章节 | 回答的问题 | 主要读者 |
|---|---|---|
| 执行摘要 | 决策问题、主要结果和限制是什么？ | 管理层 |
| 行业与客户需求 | 场景与现有流程有什么依据？ | 业务、行业团队 |
| 解决方案与架构 | 系统、版本、配置和数据路径是什么？ | 架构师、IT |
| 工作负载与对照方案 | 测试哪些任务，与什么方案比较？ | 方案团队、采购 |
| 测试方法 | 如何配置、执行、测量和复核？ | 测试、架构师 |
| 结果与质量 | 任务能否正确完成，性能和错误如何？ | 技术、业务团队 |
| 系统容量 | 满足服务要求时能支持多少工作量？ | IT、运维 |
| 价值与经济性 | 全部成本、合格任务成本及敏感性如何？ | 财务、采购、管理层 |
| 落地与风险 | 部署、运维、数据及适用限制是什么？ | 实施、安全团队 |
| 附录与披露 | 来源、完整配置、测试主体及权限是什么？ | 审阅、法务、采购 |

[查看证据型详细框架](skills/ai-value-evidence-whitepaper/references/evidence-framework.md)

### 信息不完整时如何呈现

审阅稿会在**受影响的具体段落、数字或表格字段**标浅黄色，同时标明“待补充”或“待验证”及所需依据；纯文本使用文字标记。Owner 分工放在单独清单，客户正文使用正式叙述。正式对外发布前，仍需完成事实、测试条件和公开授权的审核。

## 参考了哪些 Skill，解决什么问题

以下是对原方法的**选择性整合**，并非打包了原 Skill 的全部文件或工具链。两套新 Skill 均内置相应写作指导；需要抓取、统计、格式转换等具体能力时，取决于运行环境是否具备相应工具。

| 借鉴来源 | 解决的问题 | 本项目中的体现 |
|---|---|---|
| [Equipt `white-paper`](https://github.com/Salah-XD/equipt/tree/main/plugins/equipt-content/skills/white-paper) | 文章如何围绕读者的问题展开，而非写成产品宣传 | 执行摘要、问题、分析、方案、建议和编辑审阅 |
| [research-paper](https://github.com/aniketkrs/research-paper) | 研究、方法、来源和结论如何有据可查 | 证据台账、方法披露、可复现条件、引用和审稿 |
| 同一项目的 `get-research-paper` | 如何发现、筛选和去重相关研究 | 按需检索、读取原文、评估相关性与质量 |
| 同一项目的 `read-research-paper` | 如何读懂单篇论文或技术报告 | 提取研究问题、方法、结果、限制及适用条件 |
| Humanizer | 如何减少模板化和空泛的 AI 文风 | 中英文语言审校，同时保留事实、引用和待验证标记 |
| Signal65 公开方法 | 如何把任务、技术表现和经济价值连起来 | 工作负载、质量、容量、可比对照和经济分析框架 |

原始项目的完整文献获取、统计、绘图、格式转换及其他脚本**没有随本项目提供**；环境中有对应 Skill 时可以按需协同使用。[综合研究方法](skills/ai-value-evidence-whitepaper/references/research-methods.md)和[语言审校规则](skills/ai-value-evidence-whitepaper/references/humanizer-review.md)说明了本项目具体采用的做法。

## 与 Signal65 方法如何对照

这里对照的是**公开研究中的评测和分析方法**，不是宣称本项目实现了 Signal65 的全部测试平台、数据集或自动评分程序。下表中“需要提供”是用户或测试团队的工作；Skill 本身不会凭空产生实测结果。

| Signal65 公开方法中的关注点 | 本框架的对应内容 | 需要提供或完成的工作 |
|---|---|---|
| 围绕企业任务衡量工作结果 | 描述客户角色、工作流、输入输出和验收标准 | 提供代表性任务、样本及可核对的验收规则。 |
| 区分任务质量与系统容量 | 分别报告完成质量、错误、延迟、吞吐及并发 | 测量成功与失败任务、单请求体验及不同并发下的表现。 |
| 在任务或服务条件下比较系统 | 定义基线、负载、配置与质量门槛，并披露差异 | 准备现实可选方案及可比测试；无法对齐时说明差异。 |
| 将工作结果与成本联系 | 计算总成本、每个合格任务成本及敏感性 | 提供价格、使用量、成本边界、通过率和计算周期。 |
| 公开方法和适用限制 | 给出来源、配置、测试日期、统计方法及披露 | 保留测试记录，核实引用和对外使用权限。 |

方法参考：[Measuring Correct Work](https://pinnacle.signal65.com/measuring-correct-work-pg-1/)、[The Economics of Agentic AI](https://signal65.com/wp-content/uploads/2026/05/Signal65-Insights_The-Economics-of-Agentic-AI.pdf) 和 [The New Economics of AI Inference](https://signal65.com/research/ai/from-dense-to-mixture-of-experts-the-new-economics-of-ai-inference/)。Signal65 的研究可能有特定合作伙伴、模型和测试假设；本框架只借鉴方法，**不代表 Signal65 参与、认证、测试或背书**。

## 如何检查证据与经济账

每套 Skill 自带基于 Python 标准库的 `scripts/validate_evidence.py`。先复制[空白 JSON 模板](skills/ai-value-brief-whitepaper/references/evidence.template.json)，根据[校验说明](skills/ai-value-brief-whitepaper/references/validation.md)填写为 `evidence.json`；也可以让 Codex 从材料整理后由负责人核对。

在项目根目录运行：

```bash
python3 skills/ai-value-brief-whitepaper/scripts/validate_evidence.py evidence.json
```

证据型 Skill 的路径为 `skills/ai-value-evidence-whitepaper/scripts/validate_evidence.py`。脚本检查结构化证据、状态、公开权限状态、基础成本输入和简化算术：退出码 `0` 表示无结构或完整性提示，`1` 表示有缺失或待验证项，`2` 表示 JSON、结构或计算错误。它**不能**证明来源真实、测试可复现或授权有效，也不会独立检查整篇文档。

## 项目结构与来源

```text
README.md / README.en.md
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── references/       # 写作框架、研究方法、语言审校、填写及校验模板
└── scripts/validate_evidence.py
```

方法来源：Equipt `white-paper` 作者 Salah-XD，其技能内容采用 [CC BY 4.0](https://github.com/Salah-XD/equipt/blob/main/LICENSE-CONTENT)；`research-paper` 项目作者 Aniket Kumar，采用 [MIT](https://github.com/aniketkrs/research-paper/blob/main/LICENSE)；Humanizer 的语言审校方法参考 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)。本项目对方法作了取舍，不代表上述作者或机构参与或认可本项目。

未获公开授权的内部资料不能当作已获授权的公开内容。不要将含敏感信息的工作文件上传公开仓库；Skill 不会自行发送或发布。
