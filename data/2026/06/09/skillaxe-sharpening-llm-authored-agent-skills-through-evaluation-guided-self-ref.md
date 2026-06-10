---
title: "SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement"
authors:
  - "Srishti Gautam"
  - "Arjun Radhakrishna"
  - "Sumit Gulwani"
date: "2026-06-09"
arxiv_id: "2606.10546"
arxiv_url: "https://arxiv.org/abs/2606.10546"
pdf_url: "https://arxiv.org/pdf/2606.10546v1"
categories:
  - "cs.MA"
tags:
  - "LLM Agent"
  - "智能体技能自动生成"
  - "技能评估与自优化"
  - "无监督框架"
  - "代码智能体"
  - "性能提升"
relevance_score: 9.5
---

# SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement

## 原始摘要

Skill documents, structured natural-language instructions that guide Large Language Model (LLM) agents, are critical to modern agent frameworks, yet LLMs struggle to write skills that actually work. On SkillsBench, human-authored skills improve pass rates by 16.2 percentage points, while LLM-authored skills provide no measurable gain. We introduce SkillAxe, a fully unsupervised framework that enables LLMs to iteratively diagnose and refine their own skills. SkillAxe decomposes skill quality into four interpretable dimensions (quality impact, trigger precision, instruction compliance with fault attribution, and solution-path coverage), producing structured improvement briefs that require no ground-truth labels, test suites, or environment rewards. On SkillsBench, SkillAxe improves pass rates by 28\% relative over unimproved LLM skills and closes 47--67\% of the gap to human-authored skills. We validate the approach as a continuous improvement engine in the wild on SpreadsheetBench, where a SkillAxe-built skill library learns from past agent trajectories and raises pass rate from 16.0\% to 52.0\% using only 22 skills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体技能（skill）编写中缺乏可操作诊断反馈的核心问题。研究背景是，智能体依赖结构化的自然语言技能文档来提升性能，人工编写的技能可使通过率提升16.2个百分点，但LLM自行编写的技能语法流畅却无法带来实际提升，甚至与无技能时持平。现有方法的不足在于：当前技能评估只提供粗粒度的任务级通过/失败信号，无法诊断具体失败模式（如误触发、指令冲突、智能体未遵循指导等）；人工和自动化优化均依赖试错和主观经验，缺乏系统性的诊断机制。尤其在电子表格等需要多步工具调用的程序化领域，技能缺陷（如公式不触发重算、VBA插入为文本）难以被简单信号捕捉。本文提出的核心问题是如何让LLM在无监督条件下，通过自省行为差异来自主诊断并精细化改进自身编写的技能。SkillAxe将技能质量分解为质量影响、触发精度、指令遵循度和方案覆盖度四个可解释维度，仅需对比有无技能时的行为差异即可生成结构化改进摘要，无需真实标签、测试用例或环境奖励，实现闭环的持续自我优化。

### Q2: 有哪些相关研究？

以下是基于该论文的相关研究工作介绍：

1. **技能库与生态系统研究**：相关工作如Voyager和SAGE探索了可重用技能库的构建与演化，但主要关注技能存储或选取，而非内部结构优化。本文SkillAxe的独特贡献在于通过评估引导的自我精炼来优化技能指令本身，且不依赖环境特定奖励信号。

2. **技能评估、优化与自我改进研究**：现有方法主要依赖任务级成功信号评估技能（如文本监督），或通过监督信号优化token效率、技能选择（如TextGrad、Trace）。另一类工作如Reflexion、Self-Refine、AgentRefine针对临时执行或模型行为进行改进，而非持久化技能文档。本文SkillAxe则针对可重用技能文档，通过从智能体行为中直接诊断反馈进行精炼，无需任务特定监督，填补了技能指令结构优化的空白。

3. **失效归因研究**：已有工作研究交互式智能体间的失效归因或指令遵循验证。本文SkillAxe独特地在技能与智能体边界处诊断失效，区分技能指令缺陷与智能体执行错误，从而支持定向重写，保留正确规则。

### Q3: 论文如何解决这个问题？

SkillAxe通过一个完全无监督的自我诊断与优化框架来解决LLM编写的技能文档效果不佳的问题。核心方法是对技能质量进行多维可解释评估，并基于评估结果生成结构化改进方案。

整体框架包含四个核心模块：**质量影响评估**、**触发精准度诊断**、**指令遵循与归因分析**和**解决方案路径覆盖评估**。

1.  **质量影响评估（外循环）**：通过比较有无技能时智能体的响应，判断技能的整体效果。分为两步：先确定响应偏好方向（正向、负向、无差异），再评估改进幅度，最终得到[-1,1]的分数。负分标记需要优化的技能。
2.  **触发精准度诊断**：在语义嵌入空间中评估技能的触发条件。通过提取正例和反例触发短语并构建上下文感知的嵌入向量，计算三个几何指标：覆盖广度（触发范围是否过窄）、负例特异性（排除条件是否清晰）、边界锐度（决策边界是否存在歧义）。这能定位触发过宽或过窄的问题。
3.  **指令遵循与归因分析**：将技能分解为带权重的规则，分别评估规则的精准度、智能体的遵循度以及故障归因（是智能体未执行还是技能本身模糊）。通过计算指令遵循度和技能信用分数，区分“智能体执行错误”和“技能指导错误”，避免因执行不当而错误修改优秀的技能。
4.  **解决方案路径覆盖评估**：针对任务的多种可行解决路径（如不同的编程库），评估技能知识是否均匀覆盖了每种策略。通过计算各路径描述与技能文本块的嵌入相似度，判断技能是否只支持单一的行为模式。

**创新点**在于：1）完全无监督，无需人工标签或环境奖励；2）将技能质量分解为四个可量化、可定位问题的独立维度；3）通过故障归因机制，智能体执行错误不会导致技能被错误修改。该框架最终能将LLM编写技能的成功率提升28%，并缩小与人类编写技能差距的47-67%。

### Q4: 论文做了哪些实验？

论文在两大场景下评估了SkillAxe。**实验一：任务特定技能提升**。使用SkillsBench基准（77个任务，191个技能，688次agent运行，k=2），以Claude Opus 4.5为骨干。对比方法：无技能、LLM自写技能、SkillAxe改进技能、人类专家技能。采用双评估协议：公平评分器（LLM评估输出）和原生验证器（pytest）。主要结果：SkillAxe将覆盖率从无技能的46.7%提升至72.7%，整体通过率（覆盖率×质量）在公平评分下达54.5%，相比无技能（42.7%）和LLM自写（39.0%）显著提升，并缩小了与人类技能（62.3%）47-67%的差距。分解显示增益完全来自覆盖率（+26pp），而非答案质量（两者质量均为57.1%）。

**实验二：持续技能库改进**。使用SpreadsheetBench（912个任务，200训练/50测试），对比无技能、LLM自建库（69个技能）和SkillAxe库（22个技能）。SkillAxe库通过嵌入路由、基于诊断的两阶段改进和每技能5个训练任务的上限构建。主要结果：技能库构建后，两项技能库均将测试通过率从无技能的16.0%提升至52.0%。SkillAxe以68%更少的技能（22 vs 69）匹配了准确率，且技能激活率更高（35.8% vs 20.0%），证明其压缩和描述质量优势。

### Q5: 有什么可以进一步探索的点？

SkillAxe的规则级细化难以检测结构性偏差——当技能本身策略错误但内部一致时，无法识别。未来可引入因果推理或反事实分析，通过对比“技能生效/失效”状态下的执行结果，暴露系统性缺陷。当前技能独立评估忽略了多技能间的交互冲突，可借鉴博弈论或依赖图建模，在库级联调时引入冲突检测机制，例如利用拓扑排序分析技能触发条件的重叠性。LLM评判者的位置偏差问题可通过交换规则顺序、多模型投票或引入概率校准项缓解。最重要的是，单次更新循环难以弥合与人类技能的差距，应探索在线学习框架：结合执行轨迹的稀疏奖励信号（如终止成功率）进行强化学习微调，或采用蒙特卡洛树搜索生成多步细化候选方案，通过模拟执行自动筛选最优改进路径。此外，当前规则维度可能遗漏“效率”或“鲁棒性”指标，可增加对抗性测试（如输入噪声注入）来量化技能的稳定性。

### Q6: 总结一下论文的主要内容

论文聚焦于LLM代理技能文档的自动化质量提升问题，指出现有LLM生成的技能文档在实际任务中效果远逊于人类编写的技能（人类技能使通过率提升16.2个百分点，而LLM技能几乎无提升）。为此，作者提出SkillAxe框架，这是一种完全无监督的方法，通过将技能质量分解为四个可解释维度（质量影响、触发精度、指令遵循与故障归因、解决方案路径覆盖），生成结构化改进摘要，无需真实标签、测试套件或环境奖励。在SkillsBench上，SkillAxe使LLM生成技能的通过率相对提升28%，并缩小了47%–67%与人类技能的差距。在SpreadsheetBench的真实场景中，SkillAxe构建的技能库仅用22个技能便将通过率从16.0%提升至52.0%。核心意义在于，该框架可作为连续改进引擎，大幅降低技能编写对人专业知识的依赖，使任何LLM都能通过自动诊断与修正生成可靠技能。
