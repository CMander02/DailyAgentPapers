---
title: "ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research"
authors:
  - "Zhibang Yang"
  - "Xinke Jiang"
  - "Yuzhen Xiao"
  - "Ruizhe Zhang"
  - "Yue Fang"
  - "XinFei Wan"
  - "Zhengxing Song"
  - "Yuxuan Liu"
  - "Yuheng Huang"
  - "Xu Chu"
  - "Junfeng Zhao"
  - "Yasha Wang"
date: "2026-06-18"
arxiv_id: "2606.20122"
arxiv_url: "https://arxiv.org/abs/2606.20122"
pdf_url: "https://arxiv.org/pdf/2606.20122v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Deep Research Agent"
  - "Multi-Round Retrieval"
  - "Outline Planning"
  - "Utility-Guided Optimization"
  - "Agent Architecture"
  - "Long-Form Generation"
relevance_score: 8.5
---

# ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research

## 原始摘要

Open-ended deep research (OEDR) requires systems to acquire knowledge through multi-round retrieval and generate coherent long-form reports. The outline plays a central role as a structural scaffold that coordinates retrieval, evidence organization, and generation. However, existing methods either fix the outline before writing or refine it with local heuristics, leading to scaffold drift under continuous information accumulation and delayed feedback for evaluating outline modifications. We propose ScaffoldAgent, a utility-guided dynamic outline optimization framework for OEDR. ScaffoldAgent models outline evolution as a structured decision process with three operations: Expansion, Contraction, and Revision, enabling controlled updates to the report scaffold. It further introduces a utility-guided feedback mechanism that estimates the downstream value of each outline operation from retrieval gain, structural coherence, and trial-generation quality. The resulting utility signal guides node selection, operation scheduling, and termination during inference. Experiments on DeepResearch Bench and DeepResearch Gym show that ScaffoldAgent consistently improves long-form report generation and factual grounding over existing deep research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决开放深度研究（OEDR）中动态大纲优化面临的“结构漂移”和“延迟反馈”两大核心问题。研究背景是，现有LLM驱动的智能体虽然能进行多轮检索与生成长篇报告，但在面对目标开放、证据不断演化的任务时，其大纲管理存在严重不足：一方面，“先计划后写作”的静态大纲法无法适应信息空间的动态变化；另一方面，现有动态更新方法依赖启发式规则或局部反馈（例如仅基于新检索文档或当前步骤信号更新），缺乏对检索质量、结构合理性和生成质量三者统一的优化目标。这导致两个关键挑战：一是反复的局部调整会使大纲发生结构漂移（C1），即冗余分支、粒度不均或层级错位会逐渐积累；二是大纲修改的效果只有在后续检索和试生成后才能显现，造成严重的延迟反馈（C2），使得系统难以实时评估修改的下游价值。因此，本文提出ScaffoldAgent框架，其核心目标是将大纲视为一个主动演化的结构支架，通过显式的扩展、收缩和修订操作来有序控制大纲演化，并引入效用引导的反馈机制，综合检索增益、结构一致性和试生成质量来估算每个操作的下游效用，从而在推理时指导节点选择、操作调度和终止决策，最终实现高质量的长篇报告生成与事实性支撑。

### Q2: 有哪些相关研究？

相关工作主要分为三大类：**长流程研究系统**、**大纲动态调整方法**和**长文生成规划方法**。

在**长流程研究系统**方面，STORM和TTD-DR采用计划或精炼导向的工作流；WebWeaver和AgentCPM-Report引入动态大纲连接证据获取与报告写作；EDR、RhinoInsight和FS-Researcher则从多智能体协调、行为/上下文控制及持久化外部记忆等角度进行增强。本文与这些方法的关键区别在于，它们的大纲更新仍基于固定工作流、局部启发式或单阶段反馈，而ScaffoldAgent首次将检索增益、结构连贯性和试生成质量统一为一个效用信号，用于指导节点选择、操作调度和终止决策。

在**大纲动态调整方法**方面，DOME使用动态分层大纲并增强记忆，WriteHERE进行异构递归规划，SurveyGen-I和SciSage则利用演化计划、记忆引导写作或反思来改进跨节连贯性和引用质量。本文与这些工作的核心差异在于，它们主要优化生成文本或局部写作计划，而ScaffoldAgent将大纲演化建模为扩张、收缩、修正三种操作的组合，并通过效用函数对下游价值进行前瞻性评估，实现了对大纲修改的结构化、全局化控制。

在**长文生成规划**方面，典型范式是先计划后写作（plan-then-write），而本工作则更进一步，将动态规划与检索证据的价值评估深度耦合。

### Q3: 论文如何解决这个问题？

ScaffoldAgent通过将开放式深度研究（OEDR）建模为一个效用引导的动态提纲优化过程来解决提纲漂移与反馈延迟问题。其核心架构包含三个专门化的智能体组件：
1. **提纲智能体**：作为中央控制器，维护一个分层提纲树（节点包括章节意图、支撑证据和效用统计），采用类似UCB的节点选择策略平衡探索与利用，并决定对选定节点执行三种结构化操作之一。
2. **搜索智能体**：在需要新信息时（扩展和修订操作）检索外部证据。
3. **报告智能体**：执行试写以评估操作效果，并在提纲收敛后生成最终报告。

关键技术包括：
- **三种提纲操作**：扩展（分解过宽节点并检索证据）、收缩（合并冗余兄弟节点）、修订（更新证据薄弱的节点），这些操作源自信念修正理论，但以实用结构动作实现。
- **效用引导反馈机制**：每次操作后从三个维度计算效用值：检索效用（证据相关性与新颖性）、结构效用（连贯性、平衡性与非冗余性）和生成效用（引用支持、内容覆盖率与跨节冗余惩罚）。该效用信号指导节点选择、操作排序和终止决策，无需梯度训练。
- **收敛判定**：当边际效用增益低于阈值时停止优化，确保提纲在稳定之前保持自适应能力。

创新点在于将提纲演化建模为结构化决策过程，并通过即时效用估计解决反馈延迟，相比固定提纲或局部启发式方法，在DeepResearch Bench和Gym上显著提升了长文生成的事实基础与结构连贯性。

### Q4: 论文做了哪些实验？

论文在三个实验中验证了ScaffoldAgent的性能。实验设置使用DeepSeek-V3.2和Qwen3-32B作为骨干LLM，以Bocha为Web搜索API。数据集/基准测试采用DeepResearch Bench和DeepResearch Gym：前者通过RACE（Overall, Comprehensiveness, Insight, Instruction-following, Readability）评估报告质量、FACT（有效引用率Eff.c.和引用准确性C.acc.）评估事实性；后者评估Clarity、Depth、Balance、Breadth、Supportability和Insightfulness六个维度。对比方法包括三类范式：Naive（Prompt、RAG）、Single-Agent（ReAct、IRCoT、WebShaper）、Multi-Agent（STORM、WebWeaver、EDR、StackPlanner）。

主要结果：在DeepResearch Bench上，ScaffoldAgent在Qwen3-32B下RACE Overall达44.70，比最优基线IRCoT高2.24点，Eff.c.和C.acc.分别为30.42和54.32；在DeepSeek-V3.2下RACE Overall为48.27，超越StackPlanner 1.45点，Eff.c.和C.acc.分别达51.18和62.20。在DeepResearch Gym上，平均分75.83，领先EDR 1.78点。消融实验显示，移除Contraction或Revision操作分别使RACE下降3.55和5.18点，移除U_ret、U_str、U_gen维度分别使RACE下降2.85、4.10和4.69点。多轮交互实验中，ScaffoldAgent总分72.60，显著优于ReAct-FW（57.76）和ReAct-GR（59.70）。

### Q5: 有什么可以进一步探索的点？

首先，当前评估仍以单轮任务为主，未能充分反映真实场景中用户反复修改范围、约束或子主题的交互过程。未来可构建多轮对话轨迹与更全面的评估协议，以验证框架在动态用户反馈下的鲁棒性。其次，受限于大规模评估成本，实验仅采用开源基础模型与固定搜索接口。随着更强力的骨干模型、先进搜索基础设施及更大检索预算可用，需系统性研究ScaffoldAgent在此类扩展条件下的性能缩放规律。最后，当前框架依赖推理时的效用引导控制，未显式学习大纲演化策略。动态大纲优化本质上是序贯决策问题，未来可引入强化学习直接学习展开、收缩与修订策略，将效用信号作为奖励函数以优化节点选择、操作调度及终止决策，从而进一步提升信息收集与报告生成的一致性。这也是我从决策理论视角看最值得突破的方向。

### Q6: 总结一下论文的主要内容

ScaffoldAgent针对开放式深度研究（OEDR）中的大纲漂移和反馈延迟两大挑战，提出了一种效用引导的动态大纲优化框架。该框架将大纲视为随证据演化而更新的结构骨架，而非静态计划。方法上，它通过扩展、收缩和修订三种明确操作控制大纲演化，模拟信念修正理论；并引入效用引导的反馈机制，从检索增益、结构连贯性和试生成质量三个维度评估每次修改的下游价值，从而在推理时指导节点选择、操作调度和终止决策。在DeepResearch Bench和DeepResearch Gym上的实验表明，ScaffoldAgent在生成长篇报告和事实准确性上持续优于现有深度研究智能体，验证了效用引导的动态大纲优化对提升报告质量和事实基础的有效性。
