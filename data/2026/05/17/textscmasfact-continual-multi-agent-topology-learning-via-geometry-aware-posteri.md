---
title: "\textsc{MasFACT}: Continual Multi-Agent Topology Learning via Geometry-Aware Posterior Transfer"
authors:
  - "Xuefei Wang"
  - "Jialu Wang"
  - "Fengbo Zhang"
  - "Yihan Hu"
  - "Di Zhang"
  - "Yutong Ye"
  - "Yikun Ban"
  - "Jun Han"
  - "Ruijie Wang"
date: "2026-05-17"
arxiv_id: "2605.17361"
arxiv_url: "https://arxiv.org/abs/2605.17361"
pdf_url: "https://arxiv.org/pdf/2605.17361v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Multi-agent systems"
  - "Continual learning"
  - "Topology learning"
  - "LLM-based agent communication"
  - "Optimal transport"
  - "Posterior transfer"
relevance_score: 8.5
---

# \textsc{MasFACT}: Continual Multi-Agent Topology Learning via Geometry-Aware Posterior Transfer

## 原始摘要

Multi-agent systems (MAS) powered by large language models (LLMs) have emerged as a powerful paradigm for complex problem solving, where performance critically depends on the underlying inter-agent communication topology. However, existing topology generation methods mainly optimize for isolated tasks, while real-world deployments involve streams of evolving tasks, requiring previously effective collaboration patterns to be retained and reused rather than rediscovered or overwritten. We identify a previously underexplored failure mode, \emph{topology forgetting}, in which adapting to new tasks shifts the topology generator away from communication structures required by earlier tasks. This issue stems from cross-task misalignment in both agent-level functional semantics and relational communication structures. To address this challenge, we propose \textbf{\textsc{MasFACT}}, a geometry-aware posterior transfer framework that preserves and reuses historical collaboration knowledge as transferable topology priors. We transfer these priors across task-specific agent spaces through Fused Gromov-Wasserstein optimal transport and perform PAC-Bayes-guided conservative posterior adaptation to balance task-specific plasticity with structural stability. Experiments across class-, domain-, and task-level continual settings demonstrate that \textsc{MasFACT} consistently improves average accuracy while reducing topology forgetting compared to strong topology generation and replay-based baselines, and can be seamlessly integrated with different MAS topology generators.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统在持续学习场景中面临的**拓扑遗忘**问题。研究背景是，基于大语言模型的多智能体系统在复杂推理和决策中表现优异，其性能高度依赖于智能体间的通信拓扑结构。现有方法主要通过搜索优化或生成式图模型来自动生成拓扑，但它们大多假设任务分布是静态的，或在孤立任务上进行优化。然而，现实部署中任务流是不断演化的，这就要求系统能保留并复用先前有效的协作模式，而非重复发现或覆盖。

现有方法存在明显不足：搜索式方法在为新任务优化时会覆盖旧结构，生成式模型则因缺乏显式结构记忆而产生分布漂移。这导致了一个之前未被探索的失效模式——**拓扑遗忘**，即在适应新任务时，拓扑生成器会逐渐偏离旧任务所需的通信结构。不同于标准参数遗忘，拓扑遗忘源于跨任务在智能体功能语义和关系通信结构上的错位。

本文的核心问题是如何实现**持续的多智能体拓扑学习**，使拓扑生成器在适应新任务的同时，能保留并复用来自先前任务的可迁移协作知识，平衡任务特定可塑性与结构稳定性。为此，论文提出了\textsc{MasFACT}，一个基于几何感知后验迁移的框架，通过融合Gromov-Wasserstein最优传输对齐跨任务知识，并采用PAC-Bayes引导的保守后验更新来缓解拓扑遗忘。

### Q2: 有哪些相关研究？

本文的相关研究主要分为方法类和评测类。方法类方面，现有MAS拓扑生成方法主要分为两类：一是基于搜索的优化方法，通过搜索算法直接优化拓扑结构，但适应新任务时会覆盖历史结构；二是生成式拓扑模型，如基于图神经网络或扩散模型的结构生成器，但缺乏显式结构记忆，在任务流中易发生分布漂移。本文与这些方法的核心区别在于首次提出“拓扑遗忘”问题，并将历史拓扑作为可迁移的显式先验知识，而非孤立优化结果。与本文最接近的是持续学习方法中的回放机制和正则化方法，但本文指出，这些方法仅缓解参数级遗忘，无法处理拓扑空间中跨任务的语义和结构双重错位。本文创新性地引入Fused Gromov-Wasserstein最优传输实现结构化对齐，并结合PAC-Bayes理论平衡稳定性-可塑性，这与标准持续学习中的梯度正则化或经验回放有本质不同。在评测类方面，现有基准主要针对单任务拓扑优化或静态分布。本文提出了分层持续MAS评测协议，涵盖任务增量、领域增量和类增量三种场景，基于17个推理数据集构建12个持续场景，这是首个系统评估持续拓扑学习的基准，为领域内研究提供了标准化的评估框架。

### Q3: 论文如何解决这个问题？

MasFACT通过几何感知后验迁移框架解决多智能体持续拓扑学习中的“拓扑遗忘”问题。整体框架包含三个核心阶段：分解式历史拓扑构造阶段将高效用拓扑抽象为可迁移的先验原子，每个原子包含共识拓扑结构、原型智能体属性和节点测度；几何感知先验检索阶段采用融合Gromov-Wasserstein最优传输（FGW-OT）对齐当前任务与历史先验的节点属性和关系结构，通过联合优化属性成本矩阵和关系成本张量获得软耦合矩阵，并基于对齐代价、结构离散度和历史效用分数选择最适先验；保守后验适应阶段通过任务空间投影将选中的共识拓扑映射到当前智能体空间，得到连续结构先验后，仅学习稀疏残差矩阵进行局部修正，利用直通Gumbel-Sigmoid估计器进行可微采样，并通过PAC-Bayes引导的后验-先验KL散度和残差L1正则化约束结构漂移。

关键技术创新包括：1) 将拓扑学习建模为几何感知先验到后验迁移问题，使历史协作知识可跨任务传递；2) 提出因子化先验原子表示，解耦拓扑结构与具体智能体身份；3) 推导几何感知PAC-Bayes迁移界，理论保证当前任务拟合与结构稳定性权衡。该方法可无缝集成不同MAS拓扑生成器，在类、域、任务级持续设置中持续提升平均准确率并降低拓扑遗忘。

### Q4: 论文做了哪些实验？

论文在三个维度的持续学习场景中评估了MasFACT：类别级（粗/细粒度子技能演化）、领域级（难度与评估风格变化）和任务级（推理范式转变）。实验使用了17个公开数据集，组织成12个持续学习场景，涵盖MMLU-Pro、MATH、TACO和2Wiki等推理家族。对比方法包括单智能体（Vanilla、CoT、Self-Consistency CoT）、固定拓扑（Chain、Tree、Complete Graph）、自适应拓扑（GDesigner、AgentDropout、ARGDesigner、MasRouter）以及带回放的持续多智能体变体。所有方法使用统一的图多智能体框架和Llama-3.1-8B-Instruct。主要指标为平均准确率（AA）和平均遗忘（AF）。在类别级实验中，MasFACT在所有四族任务上取得了最佳平均AA（62.73%）和负AF（-0.06），相比最强基线MasRouter（AA 61.31%，AF 1.89%）准确率提升2.32%，遗忘降低103.70%。在领域级和任务级持续学习中，MasFACT同样成为最优，例如在任务级设置中AA为51.67%（AF 2.07），远超回放变体（如MasRouter† AA 49.55%，AF 5.02%）。结果表明，MasFACT通过几何感知后验迁移有效缓解了拓扑遗忘，甚至实现了负遗忘（即正向后向迁移）。

### Q5: 有什么可以进一步探索的点？

该工作提出的拓扑遗忘问题确实具有启发性，但当前框架仍存在可扩展性瓶颈：Fused Gromov-Wasserstein最优传输在大规模异构智能体系统中的计算成本可能过高，未来可探索基于谱分解或随机近似的加速方案。其次，当前PAC-Bayes约束仅作用于后验分布的单层矩，未能显式建模跨任务拓扑结构的层级相似性，可引入分层贝叶斯框架对不同时间尺度的通信模式进行解耦。此外，所有任务共享相同的拓扑先验库可能限制对突发性新模式的适应，建议结合元学习技术为每组任务动态分配互斥的专家先验。更根本地，该方法隐含假设任务序列是离散且边界清晰的，而实际MAS常面临渐进式漂移，未来可设计连续时间版本，通过神经微分方程对拓扑演化进行流形路径规划。最后，当前评估仅关注准确率与遗忘率，缺乏对通信代价与推理延迟的量化，这是嵌入动态拓扑生成时不可回避的工程约束。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于多智能体系统（MAS）在持续学习场景中的拓扑遗忘问题。现有方法多为孤立任务优化拓扑，忽略了任务流中协作模式的重用需求，导致适应新任务时旧任务的通信结构被遗忘。作者指出该问题的根源在于跨任务中智能体功能语义和关系通信结构的错配。为此，提出MasFACT框架，核心创新为：利用几何感知的后验传递，通过融合Gromov-Wasserstein最优传输将历史拓扑先验迁移至当前任务空间，并结合PAC-Bayes指导的保守后验自适应平衡任务特异性与结构稳定性。实验在类增量、域增量和任务增量场景下验证，MasFACT显著提升平均精度并降低拓扑遗忘，且可无缝集成多种MAS拓扑生成器。该工作首次系统定义了多智能体拓扑遗忘问题，为持续协作学习提供了可迁移的拓扑先验新范式。
