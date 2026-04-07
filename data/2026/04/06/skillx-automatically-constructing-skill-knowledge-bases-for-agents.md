---
title: "SkillX: Automatically Constructing Skill Knowledge Bases for Agents"
authors:
  - "Chenxi Wang"
  - "Zhuoyun Yu"
  - "Xin Xie"
  - "Wuguannan Yao"
  - "Runnan Fang"
  - "Shuofei Qiao"
  - "Kexin Cao"
  - "Guozhou Zheng"
  - "Xiang Qi"
  - "Peng Zhang"
  - "Shumin Deng"
date: "2026-04-06"
arxiv_id: "2604.04804"
arxiv_url: "https://arxiv.org/abs/2604.04804"
pdf_url: "https://arxiv.org/pdf/2604.04804v1"
github_url: "https://github.com/zjunlp/SkillX"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "技能库"
  - "经验复用"
  - "自动化构建"
  - "分层表示"
  - "长期规划"
  - "工具使用"
  - "基准评测"
relevance_score: 9.0
---

# SkillX: Automatically Constructing Skill Knowledge Bases for Agents

## 原始摘要

Learning from experience is critical for building capable large language model (LLM) agents, yet prevailing self-evolving paradigms remain inefficient: agents learn in isolation, repeatedly rediscover similar behaviors from limited experience, resulting in redundant exploration and poor generalization. To address this problem, we propose SkillX, a fully automated framework for constructing a \textbf{plug-and-play skill knowledge base} that can be reused across agents and environments. SkillX operates through a fully automated pipeline built on three synergistic innovations: \textit{(i) Multi-Level Skills Design}, which distills raw trajectories into three-tiered hierarchy of strategic plans, functional skills, and atomic skills; \textit{(ii) Iterative Skills Refinement}, which automatically revises skills based on execution feedback to continuously improve library quality; and \textit{(iii) Exploratory Skills Expansion}, which proactively generates and validates novel skills to expand coverage beyond seed training data. Using a strong backbone agent (GLM-4.6), we automatically build a reusable skill library and evaluate its transferability on challenging long-horizon, user-interactive benchmarks, including AppWorld, BFCL-v3, and $τ^2$-Bench. Experiments show that SkillKB consistently improves task success and execution efficiency when plugged into weaker base agents, highlighting the importance of structured, hierarchical experience representations for generalizable agent learning. Our code will be publicly available soon at https://github.com/zjunlp/SkillX.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在从经验中学习时存在的效率低下、泛化能力差以及知识难以复用的问题。当前，基于LLM的智能体在完成复杂、长周期的任务（如API调用、网页导航）方面取得了显著进展，但主流方法通常让每个智能体从零开始学习或仅依赖有限的任务特定演示。这种范式成本高昂、脆弱，且不符合智能系统应随时间积累和复用经验的预期。

现有基于经验学习的自进化智能体方法存在几个关键不足：首先，**学习是孤立的**，智能体重复执行相似任务并独立提取经验，导致大量冗余探索；其次，**经验的泛化能力弱**，在复杂环境中高质量训练数据稀缺，使得挖掘出的经验难以迁移到新任务；最后，存在**模型能力瓶颈**，仅依靠智能体自身探索和反思来获取经验，其提取上限受限于该智能体当前的能力边界。此外，现有的经验表示形式（如洞察、工作流或轨迹）往往无法同时兼顾强可迁移性、高效检索和直接可执行性。一些基于技能的方法则依赖于长上下文、渐进披露的格式，这对推理和环境工具有很高要求，限制了其鲁棒性和实际复用。

因此，本文的核心问题是：**如何构建一种可跨智能体和环境广泛复用的、结构化的经验知识库，以高效提升智能体的任务成功率和执行效率？** 为此，论文提出了SkillX框架，其核心目标是自动构建一个**即插即用的技能知识库**。该框架通过多层级技能设计、迭代式技能精炼和探索式技能扩展三项协同创新，将原始任务轨迹提炼为包含战略计划、功能技能和原子技能的三层层次结构，并自动优化和扩展技能库，旨在克服现有方法在经验表示和复用上的局限性，实现经验知识的结构化积累与高效迁移。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕**智能体经验编码**和**经验知识库构建**两大类别展开。

在**经验编码**方面，现有研究可分为三类：一是**基于案例的经验**，直接存储和复用成功任务轨迹作为示例；二是**基于策略的经验**，通过对比成功与失败轨迹提炼高层工作流或洞察；三是**基于技能的经验**，将轨迹分割并提炼为模块化、可复用的技能（如文本或程序化技能）。本文与这些工作的关系在于，它同样致力于将经验结构化以提升智能体性能。区别在于，现有方法尚未明确哪种统一表示既易于“即插即用”又能在复杂工具使用场景中持续有效。本文提出了一种**混合表示方法**，结合了高层规划与文本技能，从而实现了对基础模型的显著提升。

在**经验知识库构建**方面，现有流程通常包括静态构建与动态更新两步。**静态构建**在训练集上反复尝试任务以提取和迭代精炼经验；**动态更新**则在执行新任务后立即更新知识库以实现持续学习。本文与这些工作的关系是遵循了类似的构建与更新范式。关键区别在于，针对复杂智能体场景中任务数据稀缺的挑战，本文创新性地通过**任务合成**来扩展技能，主动生成和验证新技能以超越初始训练数据的覆盖范围。据作者所知，本文是首个提供可直接复用的技能知识库及其全自动化构建流程的工作。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SkillX的自动化框架来解决智能体经验学习效率低下和泛化能力差的问题。其核心方法是构建一个**即插即用的分层技能知识库**，使智能体能够复用跨任务和环境的经验，避免重复探索。

**整体框架与主要模块**：
SkillX是一个完全自动化的流水线，包含三个协同创新的核心模块：
1.  **多层级技能设计**：将原始任务轨迹提炼为三层结构：**战略规划技能**、**功能技能**和**原子技能**。
    *   **原子技能**：与单一工具对齐，是对工具语义的扩展描述，包含使用模式、约束和常见失败模式。
    *   **功能技能**：对应一个子任务，由一组工具组合（宏操作）实现，包含名称、文档描述和具体工具调用模式。
    *   **规划技能**：对应任务的组织结构，指定功能技能的组合顺序与依赖关系以解决完整任务。
    系统通过一个技能提取器从成功轨迹中提取这些技能，并对轨迹进行压缩和总结，过滤掉无关的探索和试错行为。

2.  **迭代式技能精炼**：通过一个基于文本的迭代优化范式，持续提升技能库的质量和覆盖度。
    *   **迭代构建流程**：从初始空库开始，在每一轮迭代中，使用当前技能库增强的智能体在训练任务上执行，收集轨迹并提取候选技能。
    *   **技能合并**：为了解决技能冗余问题，该方法从优化角度出发，对语义相似的技能进行聚类。将每个邻居技能视为对同一底层技能的一个更新方向，然后聚合这些更新方向，最终合并成一个更优的技能表示。如果合并后的技能过于复杂，会进一步将其分解为更模块化的技能。
    *   **技能过滤**：采用严格的两阶段过滤确保技能质量。**通用过滤**移除不可移植或组合性差的技能（如依赖外部包、风格特异或过度封装的技能）。**工具特定过滤**根据环境提供的工具模式验证技能，拒绝引用不存在工具、无效参数或模式不兼容的技能。
    *   **库更新**：经过合并和过滤后，对技能库执行三种具体更新操作：添加新技能、修改现有技能或保留原技能。通过多轮迭代，技能库在覆盖度、质量和组合丰富性上逐步提升。

3.  **探索式技能扩展**：为了突破种子训练数据的局限，特别是在工具空间庞大的复杂环境中，采用了**经验引导探索**方案。
    *   系统利用在种子集上执行 rollout 收集的经验（如已可靠使用的工具、高失败率工具、从未调用的工具）来引导探索，优先探索利用不足或易失败的工具，从而提高样本效率。
    *   收集探索性轨迹后，从中合成新的任务，并在此数据上重新运行技能获取与精炼流水线，从而迭代地扩展技能库。与随机探索相比，此方法能发现更多样化的技能。

**创新点**：
*   **分层、结构化的技能表示**：将经验系统性地组织为规划、功能、原子三个可重用层级，是实现高效知识迁移和组合泛化的基础。
*   **完全自动化的流水线**：从轨迹提取、迭代精炼（合并与过滤）到引导探索，整个过程无需人工干预。
*   **基于优化的技能合并方法**：将语义相似的技能视为对同一技能的多维度“更新视图”，通过聚合更新方向进行合并与优化，有效去冗余并提升技能质量。
*   **经验引导的主动探索机制**：智能地扩大技能库的覆盖范围，超越了被动从有限演示中学习的模式。

### Q4: 论文做了哪些实验？

论文在三个复杂、长视野、用户交互的智能体基准测试上进行了实验：BFCL-v3、AppWorld 和 τ²-Bench。实验设置方面，使用强主干智能体（GLM-4.6）自动构建可复用的技能库，并评估其在多个基础智能体（包括Qwen3-32B、Kimi-K2-Instruct-0905和GLM-4.6）上的迁移效果。对比方法包括无记忆（No-memory）、动态管理结构化情景记忆的A-Mem、重用历史轨迹模块化工作流的AWM，以及检索过去轨迹作为少样本示例的ExpeL。

主要结果显示，SkillX能显著提升基础模型的性能。例如，Qwen3-32B在多个基准上的平均成功率（Avg@4）提升了约10个百分点。在技能表示形式的对比中，SkillX的多层级技能设计（战略计划、功能技能、原子技能） consistently 优于其他经验表示方法。关键数据指标包括：在AppWorld和BFCL-v3上报告的Avg@4和Pass@4（四次独立运行的平均成功率和至少成功一次的概率）。分析还表明，迭代技能优化和基于经验的技能扩展策略能进一步提升库的质量和泛化能力，而多层级技能的组合能有效提高执行效率（减少执行步骤）。实验验证了结构化、层次化的经验表示对于可泛化智能体学习的重要性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向主要体现在以下几个方面。首先，论文指出对于用户交互式基准（如对话型任务），基于工具模式的技能学习是否是最佳形式仍是一个开放问题。这表明当前技能知识库的构建范式可能不适用于所有交互场景，未来需要探索更灵活、面向对话或开放式任务的技能表示与复用方法。

其次，技能库的构建和评估主要依赖于特定的大模型（如GLM-4.6）和有限的基准环境（AppWorld、BFCL-v3等）。虽然实验表明技能库能迁移到其他模型，但其在更广泛、更复杂或动态变化的环境中的泛化能力尚未充分验证。未来可研究技能库在跨领域、多模态或具身智能场景下的适应性与可扩展性。

此外，技能的精炼与扩展机制虽然能提升库的质量，但过程可能仍依赖大量试错与计算资源。未来可探索更高效的技能发现与优化算法，例如引入元学习或强化学习来自动调整技能提取策略，或利用小模型进行技能蒸馏以降低部署成本。最后，技能库目前侧重于原子操作到高层计划的层次化表示，但技能之间的组合与推理机制尚不完善。未来可研究如何让智能体动态组合已有技能来解决全新问题，实现真正的创造性问题解决。

### Q6: 总结一下论文的主要内容

SkillX 是一个全自动框架，旨在为基于大语言模型的智能体构建即插即用的技能知识库，以解决现有智能体在孤立学习中探索效率低、泛化能力差的问题。其核心贡献在于通过自动化流程构建了一个可跨智能体和环境复用的结构化技能库。

方法上，SkillX 提出了三个协同创新：首先，采用多层级技能设计，将原始任务轨迹提炼为包含战略规划、功能技能和原子技能的三层结构；其次，通过迭代技能精炼，依据执行反馈自动修订技能，持续提升库的质量；最后，通过探索性技能扩展，主动生成并验证新技能，以超越初始训练数据的覆盖范围。

实验表明，使用强大基干智能体自动构建的技能库，在多个具有挑战性的长视野、用户交互基准测试上均表现出良好的可迁移性。当该技能库接入能力较弱的基础智能体时，能持续提升任务成功率和执行效率，这凸显了结构化、层次化的经验表示对于实现可泛化的智能体学习具有重要意义。
