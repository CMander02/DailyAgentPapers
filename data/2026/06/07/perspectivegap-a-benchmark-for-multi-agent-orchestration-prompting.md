---
title: "PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting"
authors:
  - "Youran Sun"
  - "Xingyu Ren"
  - "Kejia Zhang"
  - "Xinpeng Liu"
  - "Jiaxuan Guo"
date: "2026-06-07"
arxiv_id: "2606.08878"
arxiv_url: "https://arxiv.org/abs/2606.08878"
pdf_url: "https://arxiv.org/pdf/2606.08878v1"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Orchestration Prompting"
  - "Benchmark"
  - "LLM Evaluation"
  - "Prompt Engineering"
  - "Agent Collaboration"
  - "Role Assignment"
relevance_score: 9.5
---

# PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting

## 原始摘要

Real-world LLM applications are moving beyond single-agent workflows toward orchestrated multi-agent systems, yet current models still struggle to determine what each sub-agent needs to know. To measure this, we introduce PerspectiveGap, a benchmark for evaluating LLMs' ability to compose orchestration prompts for multi-agent systems. PerspectiveGap contains 110 scenarios, each evaluated through two distractor-mixed task formats: role-fragment assignment and free-form prompt writing. These scenarios are organized into 10 topologies, which are distilled from the authors' real-world engineering practice and framed by the Prompt Economy principle: building loop-centered orchestrations that maximize utility with minimal role and engineering overhead. In experiments with 27 commercial models from 10 companies, GPT-5.5 substantially outperforms all competitors, whereas Opus 4.7 shows a notable weakness in orchestration prompting despite its strong coding performance. Nevertheless, PerspectiveGap remains challenging: the evaluated models achieve an average combined pass rate of only 14.9\% (GPT-5.5 62.0\%) and an average overall leakage rate of 246.5\% (a per-scenario information leak-event count, not a proportion; GPT-5.5 49.1\%). These findings suggest that multi-agent orchestration prompting is a distinct and under-evaluated capability, and PerspectiveGap provides a foundation for measuring and improving it systematically.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是多智能体系统编排提示（multi-agent orchestration prompting）能力缺失的问题。研究背景是，真实世界的LLM应用正从单智能体工作流转向编排式多智能体系统，需要主智能体为每个子智能体编写指令，明确其任务范围、上下文边界和交接规范。现有方法的不足在于：当前的能力评估体系存在明显空白——心智理论（ToM）基准测试仅评估问答或信念追踪，智能体基准测试只关注下游任务成功或工具使用，两者都无法衡量主智能体是否能为子智能体写出尊重非对称上下文和角色特定信息需求的提示。本文要解决的核心问题是：目前LLM在编排提示时普遍失败，具体表现为泄露干扰信息、暴露越权角色信息、丢失共享上下文、混淆产出所有权，甚至把指令放在子智能体看不到的位置，导致子智能体提示不完整、被污染或自相矛盾。为此，论文提出了PerspectiveGap基准测试，包含110个场景和两种任务格式（角色-片段分配和自由形式提示编写），以系统评估和推动多智能体编排提示这一独特且被低估的能力。

### Q2: 有哪些相关研究？

以下是该论文的相关研究工作，按类别组织：

**多智能体编排方法类**：早期系统如CAMEL、ChatDev、MetaGPT、AutoGen和AgentVerse展示了角色专业化LLM可通过自然语言消息和结构化流程协作。后续研究总结了路由、规划、反思、批判和工具中介交接等常见编排模式。这些工作激发了本文的设定，但未测试脆弱环节：LLM能否编写保持上下文边界和交接契约的角色特定指令，而非将所有角色扁平化为相同提示。

**智能体与工具使用基准类**：AgentBench、ToolLLM等基准评估在智能体任务、工具和指令已给定的执行能力。本文将其前移一步：在主智能体行动前，能否将上下文和约束分配到子智能体可安全使用的提示中。

**信息不对称与心智理论基准类**：ToMi、FANToM、SOTOPIA-TOM等测试信念追踪和心智推理，但不要求模型生成提示产物。本文的两个任务（分配测试和提示编写）镜像了“知道需要什么”与“根据知识行动”的区分，聚焦于交互前定义每个角色任务视图的编排提示构建。

**分布式信息与多智能体故障类**：HiddenBench、Silo-Bench、MAST等诊断多智能体在交互中的信息整合失败和角色混淆。本文隔离了前置工件——决定各智能体初始信息边界的角色提示。

**提示优化与角色状态管理类**：相关方法通过细化、角色演化、记忆或训练时优化改善行为，但通常以最终任务成功度评估。本文直接评估生成的提示工件本身，从提示中即可判断信息分配是否正确，而非从下游任务是否成功推断。

### Q3: 论文如何解决这个问题？

论文通过构建PerspectiveGap基准测试来解决多智能体系统编排提示中模型难以确定各子智能体所需信息的问题。核心方法是设计了一个包含110个场景的基准，每个场景包含子智能体角色列表、打乱的信息片段以及基于“仅需”规则的参考分配。整体框架分为三个层次：拓扑结构（10种角色-交接模式，如编码器-审查器循环、调度器-工作流等）、领域实例（拓扑的特定领域实现）和渲染后的基准项（供模型测试）。主要模块包括：确定性渲染模块，确保模型根据信息片段内容而非位置进行分配；干扰项插入机制，引入与子智能体无关但看似有用的信息，测试模型能否区分自身编排信息与子智能体所需信息；两种评估格式（角色-片段分配和自由提示编写），分别测试结构化映射能力和自然语言提示中的边界保持能力。关键技术包括：使用严格通过率作为主要指标，要求所有角色边界完全正确（无遗漏也无多余）；针对自由提示设计确定性评分器，通过n-gram指纹验证每个角色提示是否包含了所需片段的独特短语且未泄露无关片段。创新点在于：提出“提示经济”原则，强调以循环为中心的编排设计，最大化角色重用效用；通过扰动混合和双格式评估揭示模型在边界感知与实际应用中的差距。实验表明当前最优模型GPT-5.5的综合通过率仅62.0%，所有模型平均仅14.9%，信息泄露率高达246.5%，证明多智能体编排提示是一项独特且被低估的能力。

### Q4: 论文做了哪些实验？

在实验设置中，论文评估了27个商业模型（来自10家公司）在110个场景下的两种任务格式（角色-片段分配与自由形式提示编写），使用2个随机种子（1和42），总计11,880次评估。主要实验结果（主排行榜）显示，GPT-5.5以62.0%的通过率显著领先，远超第二名deepseek-v4-pro（32.0%）。在信息泄漏方面，GPT-5.5的干扰泄漏率仅为2.3%，整体泄漏率49.1%，而所有模型的平均整体泄漏率高达246.5%（按场景计的事件数，非比例）。对于难度分析，按角色数量聚合的通过率表明，角色越多场景通常越难，其中自由形式提示编写任务略难于角色-片段分配。论文还进行了四项消融研究（少样本提示、干扰数量、草稿板提示和推理努力），考察标准提示技术、推理时干预及干扰数对性能的影响。此外，通过Pearson相关性分析，净匹配分数与严格通过率的线性关联最强（r=0.744），且多项式拟合显示当n=5时相关性升至0.942，支持严格通过率作为保守但一致的指标。整体上，模型平均综合通过率仅为14.9%（GPT-5.5为62.0%），表明多智能体编排提示是一项独特且未充分评估的能力。

### Q5: 有什么可以进一步探索的点？

基于论文分析，该领域有以下进一步探索方向：

**1. 拓扑结构扩展**：当前仅覆盖10种拓扑和100个领域实例，未来可基于相同构建规则添加更多多智能体编排模式，例如动态切换拓扑或层次化混合结构，以提升基准的覆盖广度。

**2. 下游行为验证**：论文仅评估子智能体的提示质量，未验证这些提示在实际执行中的效果。后续可构建跨领域的下游任务运行时系统，测试提示边界错误是否会转化为任务失败，从而建立提示质量与执行性能的关联。

**3. 标注一致性与评分优化**：角色到片段的映射需建立外部标注者一致性验证。同时，自由格式提示评分器可改进为容忍高质量改写，例如引入语义等价性检测或基于任务表现的间接评估，避免惩罚表达变体。

**4. 智能体间视角推理**：模型在信息泄漏、边界混淆、共享上下文遗漏等失败模式中暴露了视角推理不足。未来可探索角色感知的注意力机制或显式边界约束生成策略，使模型能更精确地从子智能体角度推理其知识需求。

### Q6: 总结一下论文的主要内容

这项研究提出了PerspectiveGap基准测试，用于评估大语言模型在多智能体系统中编写编排提示的能力。问题定义上，针对实际应用从单智能体向多智能体系统演进时，模型很难确定每个子智能体所需信息的问题。方法上，构建了110个场景，每个场景通过角色片段分配和自由形式提示编写两种任务格式评估，这些场景基于真实工程实践提炼出10种拓扑结构，并遵循"提示经济"原则。结论显示，在测试的27个商业模型中，GPT-5.5表现最佳，但平均通过率仅14.9%，信息泄漏率高达246.5%。即使编码能力强大的Opus 4.7在编排提示方面也表现不佳，这表明多智能体编排提示是一种独特且未被充分评估的能力。该基准测试为系统化测量和改进这一能力提供了基础，揭示了当前模型在保持角色特定信息边界方面的脆弱性。
