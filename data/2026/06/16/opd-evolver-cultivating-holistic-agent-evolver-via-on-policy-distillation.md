---
title: "OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation"
authors:
  - "Guibin Zhang"
  - "Xun Xu"
  - "Yanwei Yue"
  - "Zikun Su"
  - "Wangchunshu Zhou"
  - "Xiaobin Hu"
  - "Shuicheng Yan"
date: "2026-06-16"
arxiv_id: "2606.17628"
arxiv_url: "https://arxiv.org/abs/2606.17628"
pdf_url: "https://arxiv.org/pdf/2606.17628v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Self-Evolving Agent"
  - "On-Policy Distillation"
  - "Slow-Fast Co-Evolution"
  - "Multi-domain Benchmark"
relevance_score: 9.5
---

# OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation

## 原始摘要

Memory has become a standard substrate for self-evolving agents, yet retaining experience is not the same as learning how to evolve through it. Existing memory agents can store trajectories, retrieve reflections, or accumulate skills, but often lack the holistic competence to select useful experience, act on it, write reusable knowledge, and maintain a growing repository. We introduce OPD-Evolver, a slow-fast co-evolution framework that cultivates such an agent evolver through on-policy self-distillation. In the fast loop, OPD-Evolver interacts with a four-level memory hierarchy to read, use, write, and maintain experience for rapid test-time evolution. In the slow loop, outcome-calibrated memory attribution and privileged hindsight distill these four abilities into the deployable policy. Across multi-domain benchmarks, OPD-Evolver surpasses memory systems such as ReasoningBank by up to 11.5%, and training-based methods such as Skill0 by ~5.8%. Further analysis shows that OPD-Evolver internalizes high-value experience and memory management, enabling OPD-Evolver-9B to challenge giant counterparts such as Qwen3.5-397B-A17B and Step-3.5-Flash, pointing beyond memory-augmented agents toward genuinely qualified agent evolvers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有自进化智能体在经验利用上的碎片化问题。当前研究背景中，记忆已成为自进化智能体的标准组件，但存储经验并不等同于学会如何通过经验进化。现有方法存在明显不足：记忆增强智能体（如存储轨迹、反思、技巧）仅优化了检索和上下文使用；技能增强智能体（如Skill0）专注于将经验蒸馏为可复用策略；而训练方法（如SFT、RL）直接参数化经验，但大多只优化了进化过程的单一环节（如检索、使用、蒸馏或记忆架构设计）。核心问题在于：任务奖励只对执行提供直接监督，却无法指导记忆选择、知识写入或长期管理；同时，如何将这些耦合能力（经验选择、基于经验的执行、经验写入、经验管理）训练到一个策略中而不相互干扰，仍缺乏探索。因此，现有智能体可能在某些场景下提升，但缺乏全面的进化能力。本文要解决的核心问题正是：如何训练一个智能体获得通过经验进化的整体能力，成为真正合格的智能体进化器。作者提出了OPD-Evolver，一个快慢协同进化框架，通过在线策略自蒸馏，将任务结果和特权事后信息转化为对选择、执行、写入和记忆管理的监督信号，从而培养智能体的全面进化能力。

### Q2: 有哪些相关研究？

论文的相关研究主要分为两类：

**1. 自演化智能体（Self-Evolving Agents）**：根据经验生命周期，现有工作可细分为四阶段。经验选择：如嵌入检索、效用评分、学习路由或基于策略的排序；经验执行：基于记忆或技能的智能体，或通过SFT/RL将经验内化；经验写入：将轨迹蒸馏为反思、推理记忆、过程提示、可执行工具或可复用技能；经验管理：研究经验评分、整合、遗忘和架构级适应。本文的OPD-Evolver与之不同，它通过四层记忆层级联合优化所有四个阶段，而现有工作通常仅优化其中一两个阶段。

**2. 同策略蒸馏（On-Policy Distillation, OPD）**：传统OPD在智能体自访问状态上使用教师网络提供密集监督，减少离线策略的推理-训练不匹配，如数学推理、知识问答、工具使用等任务。本文创新在于利用OPD不仅强化执行能力，更是通过慢-快协同框架（快速循环实现实时演化，慢速循环通过结果校准的记忆归因和特权后见视角蒸馏）联合培养读、用、写、管四种演化能力，从而训练出真正全面的智能体演化器。

### Q3: 论文如何解决这个问题？

OPD-Evolver提出了一种慢-快协同进化框架，通过在线策略自蒸馏来培养智能体的整体进化能力。核心设计包含两个循环：快循环和慢循环。

快循环负责在测试时实现快速进化。它包含一个四层记忆层次结构：轨迹层存储完整情节，技巧层存储局部启发式，技能层存储可重用流程，工具层存储可执行代码模板。面对新任务时，智能体首先从各层检索高召回候选记忆，然后通过选择器模块压缩为紧凑上下文，接着在此上下文中执行任务并产生行动。任务结束后，智能体自主决定向哪些层写入新记忆，并定期执行仓库维护（查找、合并、删除操作）。快循环不改变模型参数，只更新记忆仓库。

慢循环负责通过在线策略自蒸馏训练进化能力。其创新点在于：首先，通过结果校准的记忆归因，将环境反馈的标量奖励反向传播到每个记忆的价值估计，采用候选控制对比（比较被选中的候选记忆与未被选中的记忆在奖励上的差异）并加入置信度因子。然后，基于归因结果，对四个关键决策（选择、执行、写作、维护）分别构造特权后见视角：选择阶段看到所有候选记忆的价值评分，执行阶段通过省略记忆的轨迹让学生内化有用知识，写作阶段看到哪些新记忆后来变得有价值，维护阶段获得校准的诊断信息。学生模型先从公开输入采样在线输出，教师模型在此基础上利用特权信息生成理想输出，通过KL散度进行自蒸馏。

该架构的核心创新在于将经验演化的完整生命周期（检索、选择、执行、写作、维护）统一为可训练的闭环，使得9B模型能挑战397B的超大模型。

### Q4: 论文做了哪些实验？

论文在5个多领域基准（LifelongAgentBench(DB/OS)、MemoryArena(Math/Physics)、AMA-Bench(Causal/State Update/State Abstraction)、InterCode(Bash/CTF/SQL)和MiniHack(Room/Maze/KeyRoom)）上评估OPD-Evolver。实验设置采用Qwen3-4B-Instruct和Qwen3.5-9B为骨干，Qwen3-Embedding-0.6B检索，检索50个候选，保留最多20条记忆。对比方法包括7种记忆增强系统（ExpeL、AWM、ReasoningBank等）和5种训练方法（SFT、GRPO、Skill0、MemRL、Complementary RL）。主要结果：OPD-Evolver在所有10个子集上取得最优，较最强记忆基线在OS上提升4%（65% vs 61%），AMA-SA上提升4.92%（52.92% vs 48%），InterCode-CTF上提升4%（57% vs 53%）。与训练方法相比，在5/6子集上领先，较GRPO在MiniHack-KeyRoom提升5.88%（9.80% vs 3.92%），较Complementary RL在Maze提升6.6%（27.45% vs 20.85%）。9B模型在9/10子集上超越Step-3.5-Flash(196B)，在6/10子集上超越Qwen3.5-397B-A17B。消融实验显示去除记忆归因导致最大降幅（平均38.67%→32.13%）。选择蒸馏将中位记忆分数从0.66提至0.79，写作蒸馏从中位0.80提至0.91。经验内化实验显示成功率提升3-7点，步数减少最多2.5步。

### Q5: 有什么可以进一步探索的点？

该工作的核心局限在于其慢循环蒸馏过程高度依赖预定义的环境奖励信号进行结果校准，当面对稀疏奖励或奖励难以定义的真实场景时，演化信号的可靠性会显著下降。未来可探索基于内在动机或模型自生成的偏好对齐来替代外部奖励，使演化信号更通用。此外，当前四层记忆层次结构的设计仍依赖人工规则（如写操作用于存储技能，维护操作用于去重），这限制了系统在开放域中的自适应能力。值得探索让智能体自动发现最优记忆管理策略，例如通过元学习或基于大模型的自编程。另一个有趣方向是将该框架与感知-行动循环更紧密结合，使得演化能力不仅局限于经验池操作，还能直接引导策略网络的架构更新。同时，论文主要验证了在5B-9B参数规模下的有效性，未来可在更大模型上验证慢速蒸馏的迁移幅度，并分析其与涌现能力的关系。

### Q6: 总结一下论文的主要内容

该论文提出OPD-Evolver框架，解决现有记忆智能体虽能存储经验但缺乏系统性进化能力的问题，即无法有效选择、应用、书写及维护经验。方法上，采用“慢-快”共进化架构：快速循环中，智能体通过四层记忆层级交互，实现快速测试时经验读写与维护；慢速循环则利用结果校准的记忆归因和特权事后蒸馏，将上述四种能力提炼至部署策略中。主要结论显示，OPD-Evolver在多领域基准测试中，性能超越ReasoningBank等记忆系统达11.5%，超越Skill0等训练方法约5.8%。其9B模型甚至可挑战Qwen3.5-397B-A17B等大型模型，证实了从被动存储向主动将经验内化为进化能力的范式转变意义。
