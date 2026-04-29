---
title: "SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?"
authors:
  - "Noam Tarshish"
  - "Nofar Selouk"
  - "Daniel Hodisan"
  - "Bar Ezra Gafniel"
  - "Yuval Elovici"
  - "Asaf Shabtai"
  - "Eliya Nachmani"
date: "2026-04-28"
arxiv_id: "2604.25737"
arxiv_url: "https://arxiv.org/abs/2604.25737"
pdf_url: "https://arxiv.org/pdf/2604.25737v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Code Editing"
  - "LLM Agent"
  - "Agent Framework"
  - "Agent Benchmark"
  - "Iterative Refinement"
  - "Failure Analysis"
relevance_score: 9.5
---

# SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?

## 原始摘要

Instructed code editing is a significant challenge for large language models (LLMs). On the EditBench benchmark, 39 of 40 evaluated models obtain a task success rate (TSR) below 60 percent, highlighting a gap between general code generation and the ability to perform instruction-driven editing under executable test constraints. To address this, we propose SAFEdit, a multi-agent framework for instructed code editing that decomposes the editing process into specialized roles to improve reliability and reduce unintended code changes. A Planner Agent produces an explicit, visibility-aware edit plan, an Editor Agent applies minimal, literal code modifications, and a Verifier Agent executes real test runs. When tests fail, SAFEdit uses a Failure Abstraction Layer (FAL) to transform raw test logs into structured diagnostic feedback, which is fed back to the Editor to support iterative refinement. We compare SAFEdit against both prior single-model results reported for EditBench and an implemented ReAct single-agent baseline under the same evaluation conditions. We used EditBench to evaluate SAFEdit on 445 code editing instances in five languages (English, Polish, Spanish, Chinese, and Russian) under varying spatial context variants. SAFEdit achieved 68.6 percent TSR, outperforming the single-model baseline by 3.8 percentage points and the ReAct single-agent baseline by 8.6 percentage points. The iterative refinement loop was found to contribute 17.4 percentage points to SAFEdit's overall success rate. SAFEdit's automated error analysis further indicates a reduction in instruction-level hallucinations compared to single-agent approaches, providing an additional framework component for interpreting failures beyond pass or fail outcomes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模语言模型（LLM）在指令性代码编辑（instructed code editing）任务中可靠性和鲁棒性不足的问题。研究背景是，尽管LLM在通用代码生成方面取得了显著进展，但在基于自然语言指令对现有代码进行精准修改时表现不佳。现有方法的不足主要体现在：在EditBench基准测试中，39/40的评估模型任务成功率（TSR）低于60%，表明模型能力本身难以应对指令性编辑任务。现有方法（如单模型基线或多智能体系统）主要针对代码生成或完整问题解决，缺乏专门针对指令性编辑的结构化、上下文敏感及需保留代码不变量的设计与评估。核心问题是：如何通过结构化分解与验证机制，提升LLM在指令性代码编辑中的可靠性，减少不必要的代码修改和指令级幻觉，并利用可执行测试进行迭代验证以优化编辑结果。该论文提出的SAFEdit框架通过多智能体分工（规划、编辑、验证）和失败抽象层（FAL）来解决这一挑战。

### Q2: 有哪些相关研究？

相关工作可以从三个类别来梳理。

1. **代码编辑与生成基准**: 传统代码生成评测（如Codex基准）与软件实践脱节，着重从零生成而非编辑。SWE-bench转向仓库级问题修复，但侧重端到端推理而非局部指令编辑。专门为指令代码编辑设计的基准包括Can It Edit?和CodeEditorBench，但两者多基于合成任务，缺乏真实世界指令的歧义性和噪声。本文使用的EditBench弥补了此空白，它基于真实开发者数据，包含三种可见性变体，能以测试通过率进行自动化评估。SAFEdit正是在EditBench的设定下（过滤后445个任务）进行评测并取得了SOTA。

2. **迭代程序修复方法**: 已有研究探索了利用LLM及测试反馈进行多轮修复，如The Art of Repair指出迭代次数存在收益递减点，LeDex通过执行验证的优化轨迹提升模型自调试能力。受此启发，SAFEdit设计了由Verifier Agent执行真实测试的反馈环路，并将迭代次数上限设为3次，在准确性与计算成本间取得平衡。

3. **多智能体系统**: 多智能体框架被用于分解复杂软件任务，例如AgentCoder（含程序员、测试设计者、执行者）和CodeR（用于SWE-bench的解析、规划、打补丁、验证）。SAFEdit属于此类，它将指令式代码编辑分解为三个专门角色：Planner Agent生成结构化编辑计划、Editor Agent实施最小化编辑、Verifier Agent执行测试验证。SAFEdit采用CrewAI进行编排，相较于未加结构的单智能体方法，其职责边界更清晰，工作流更可控。本文的主要区别在于提出了Failure Abstraction Layer (FAL)用于将原始测试日志转化为结构化诊断反馈，从而更有效地指导迭代修正，并显著减少了指令层面的幻觉。

### Q3: 论文如何解决这个问题？

SAFEdit通过一个多智能体框架解决指令代码编辑的可靠性问题。该框架将编辑流程分解为三个专业化角色，形成一个迭代优化循环：

1. **整体框架**：包含规划器(Planner)、编辑器(Editor)和验证器(Verifier)三个智能体，通过CrewAI框架协调工作。当验证器检测到测试失败时，系统进入迭代优化循环（最多3轮），通过结构化反馈持续修正编辑结果。

2. **核心模块与关键技术**：
   - **规划器**：根据指令和原始代码生成结构化编辑计划，包含观察元素、编辑意图、目标描述、具体修改动作和约束条件等字段。该计划严格基于可见的代码上下文，不产生任何代码。
   - **编辑器**：严格按照规划器的修改列表执行精确的、最小化的代码改动，保留原格式和无关代码，避免过度编辑。
   - **验证器**：在沙箱环境中运行真实单元测试，提供确定性通过/失败结果。
   - **故障抽象层(FAL)**：将原始测试日志转化为结构化诊断反馈。通过日志解析器提取失败测试名称、异常类型、期望值与实际值；通过确定性模式匹配将失败归因于14种结构类型（如语法错误、断言不匹配）；最后生成包含测试名称、故障类型、诊断信息、修复建议和期望/实际值的反馈块。

3. **创新点**：规划与代码生成分离确保编辑操作基于明确指令；FAL将原始测试日志转化为语义化、可操作的反馈，减少迭代次数和指令幻觉；通过真实测试执行而非LLM预测提供确定性结果。实验表明该框架在EditBench上达到68.6%的任务成功率，迭代优化贡献了17.4个百分点的提升。

### Q4: 论文做了哪些实验？

在EditBench基准上进行实验，评估集包含445个代码编辑实例，涵盖五种自然语言（英语、波兰语、西班牙语、中文和俄语）及三种可见性变体（纯代码、高亮、高亮+光标位置），共计1335个独立评估实例。对比方法包括：零样本单模型基线（来自EditBench原始研究，最佳为claude-sonnet-4，TSR 64.8%）、ReAct单智能体基线（TSR 60.0%），均使用GPT-4.1作为骨干模型，最大迭代次数为3次。SAFEdit在HIGHLIGHT变体下取得68.6%的任务成功率（TSR），分别比最强单模型基线高3.8个百分点、比ReAct基线高8.6个百分点。迭代优化贡献了17.4个百分点的性能提升（首次尝试TSR为51.2%，最终TSR为68.6%）。按语言分析，SAFEdit在所有五种语言上的TSR均优于ReAct，提升幅度从俄语的5.7个百分点到西班牙语的12.4个百分点。错误分类分析显示，SAFEdit主要失败原因为指令幻觉和实施差距，且在所有语言中回归错误率为0%，而ReAct在多数语言中出现非零回归错误。

### Q5: 有什么可以进一步探索的点？

根据论文的实验结果和讨论，SAFEdit 虽然通过多智能体分解提升了可靠性，但仍存在若干值得探索的局限性和未来方向。首先，当前框架的 Planner Agent 依赖显式、可见的编辑计划，但在处理极其复杂或模糊的自然语言指令时，计划本身可能产生偏差，导致后续编辑偏离目标。未来可以引入对计划质量的自动评估机制，或在计划生成阶段融入更多上下文推理（如代码库全局依赖分析）。其次，迭代精炼虽高效，但收敛次数较少可能意味着失败案例中存在“硬错误”未被充分修复。改进思路是让 FAL 层不仅提供结构化诊断，还能区分错误类型（如逻辑错误 vs. 语法错误）并分配不同权重，从而指导 Editor 采取差异化修正策略。此外，当前评估局限于单一基准和五语种，未来应扩展到更真实的代码库场景（如多文件项目、增量更新），并检验框架在大规模语言模型（如 GPT-4 或 Code Llama）上的泛化能力。最后，SAFEdit 的故障分类仍基于自动分析，可结合人工标注优化错误分类器，并探索多智能体间更细粒度的协作（如让 Planner 在编辑后参与“计划修订”循环），以进一步减少指令层面的幻觉。这些方向将推动多智能体代码编辑系统向更可靠、更自适应的方向发展。

### Q6: 总结一下论文的主要内容

这篇论文提出了SAFEdit，一个用于指令驱动代码编辑的多智能体框架。当前大模型在EditBench基准上任务成功率（TSR）普遍低于60%，暴露出代码编辑可靠性的挑战。SAFEdit将编辑过程分解为三个专门角色：规划器生成显式的、考虑可见性的编辑计划；编辑器执行最小、字面的代码修改；验证器通过实际测试运行验证。当测试失败时，失败抽象层（FAL）将原始测试日志转化为结构化诊断反馈，指导编辑器进行最多三次迭代优化。在EditBench的445个实例（涵盖五种语言）上，SAFEdit实现了68.6%的平均TSR，超过单模型基线3.8个百分点和ReAct单智能体基线8.6个百分点。迭代优化贡献了17.4个百分点的成功率提升。错误分析表明，与单智能体方法相比，SAFEdit减少了指令级幻觉。其核心贡献在于证明了结构化角色分解与执行驱动的迭代验证能显著提升指令代码编辑的可靠性，而非仅依赖模型能力。
