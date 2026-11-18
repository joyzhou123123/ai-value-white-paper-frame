# 白皮书语言审校 / Humanizer-inspired editorial pass

## 适用范围 / Scope
在两套 Skill 的正文形成后、最终事实和版式检查前，对中文与英文分别进行一轮语言审校。采用正式、自然、准确的企业技术白皮书语气；如用户提供品牌手册或写作样稿，优先遵循其可观察的风格。This is a self-contained adaptation of selected humanizer editing principles, not a bundle of the full upstream skill or a guarantee that text will pass AI detectors.

## 审校流程 / Editing pass
1. 识别空泛的行业套话、堆砌形容词、口号、无依据的“领先/革命性”、没有来源的“专家认为”、重复标题和机械排比。将内容改成具体的客户问题、能力、证据及其含义；没有证据时保留清晰的待验证标记，不用华丽词句遮盖。
2. 把内部整理口吻改为对外叙述：说明模型、配置、结论与适用条件，而不是写“我们参考了资料”“请 Owner 补充”。审阅用黄色标注可保留，但在受影响的主张和数据处具体写明待核事项，Owner 分工放在单独清单。
3. 使用明确主语、动词和简洁的技术解释。合并重复句，适度变化句式与段落长度；保留必要专业术语并在首次出现时按受众解释。不要为了显得“人性化”添加俚语、夸张比喻或非正式口吻。
4. 改写前后核对全部事实、名称、数据、单位、计算、引文、来源、时间、条件、限制、授权状态和黄色标记。不能新增无依据事实，不能把相关性写成因果，不能把估算变成实测，也不能通过润色去掉缺口、限制或负面结果。发现事实有问题时列入待核，而非悄悄修正。
5. 中文和英文分别自然成文，保持事实、数字、证据等级、适用条件、假设及缺口一致，不逐字硬译。最终检查正文、图表、摘要和引用之间是否一致；中英文任何一版改动事实时同步更新另一版。

## Miniature example / 简短示例
Before: “这一革命性解决方案将全面赋能所有企业，显著提升效率。”
After: “该方案可用于支持指定业务任务；效率变化需结合任务耗时和验收结果评估。”
If an outcome has not been measured, retain `[待验证：任务耗时与验收结果]` / `[TO VERIFY: task time and acceptance results]` and yellow highlight where the format supports it.

Method credit: adapted selectively from the local `humanizer` skill, based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). The original skill is not included in this project; it may be invoked separately if installed and requested.
