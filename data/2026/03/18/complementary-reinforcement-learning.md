---
title: "Complementary Reinforcement Learning"
authors:
  - "Dilxat Muhtar"
  - "Jiashun Liu"
  - "Wei Gao"
  - "Weixun Wang"
  - "Shaopan Xiong"
  - "Ju Huang"
  - "Siran Yang"
  - "Wenbo Su"
  - "Jiamang Wang"
  - "Ling Pan"
  - "Bo Zheng"
date: "2026-03-18"
arxiv_id: "2603.17621"
arxiv_url: "https://arxiv.org/abs/2603.17621"
pdf_url: "https://arxiv.org/pdf/2603.17621v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "强化学习"
  - "经验复用"
  - "智能体训练"
  - "样本效率"
  - "互补学习"
  - "多任务学习"
  - "LLM-based Agent"
relevance_score: 8.5
---

# Complementary Reinforcement Learning

## 原始摘要

Reinforcement Learning (RL) has emerged as a powerful paradigm for training LLM-based agents, yet remains limited by low sample efficiency, stemming not only from sparse outcome feedback but also from the agent's inability to leverage prior experience across episodes. While augmenting agents with historical experience offers a promising remedy, existing approaches suffer from a critical weakness: the experience distilled from history is either stored statically or fail to coevolve with the improving actor, causing a progressive misalignment between the experience and the actor's evolving capability that diminishes its utility over the course of training. Inspired by complementary learning systems in neuroscience, we present Complementary RL to achieve seamless co-evolution of an experience extractor and a policy actor within the RL optimization loop. Specifically, the actor is optimized via sparse outcome-based rewards, while the experience extractor is optimized according to whether its distilled experiences demonstrably contribute to the actor's success, thereby evolving its experience management strategy in lockstep with the actor's growing capabilities. Empirically, Complementary RL outperforms outcome-based agentic RL baselines that do not learn from experience, achieving 10% performance improvement in single-task scenarios and exhibits robust scalability in multi-task settings. These results establish Complementary RL as a paradigm for efficient experience-driven agent learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体在强化学习（RL）训练中样本效率低下的核心问题。研究背景是，尽管RL已被证明能有效提升LLM智能体的能力，但传统的基于结果奖励的RL方法严重依赖稀疏的奖励信号，导致训练过程需要大量交互样本。智能体从多轮交互轨迹中获得的丰富过程信息（如有效行为模式、可恢复的失败模式、关键决策点）未被充分利用，加剧了样本低效。

现有方法试图通过利用历史经验（即从原始轨迹中提炼出的结构化文本知识，如成功策略、失败模式等）来缓解这一问题。然而，这些方法存在关键不足：它们通常将经验视为静态资源进行处理。例如，一些方法维护固定的经验库，或使用非自适应的经验提取器。这导致随着训练进行、智能体（执行者）能力不断进化，所存储或提取的经验与执行者当前的实际能力逐渐失配，变得陈旧且不相关，其指导效用随之下降，最终限制了学习效率的提升。

因此，本文要解决的核心问题是：能否设计一个RL框架，使得策略执行者与其经验提取器能够形成一个封闭的协同进化循环，彼此持续适应、相互塑造，从而在整个训练过程中动态地提供高质量、高相关性的经验指导，以显著提高学习样本效率？受神经科学中互补学习系统（CLS）的启发，论文提出了“互补强化学习”范式来回答这一问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升基于大语言模型的智能体在强化学习中的样本效率，特别是如何利用历史经验。相关工作可分为以下几类：

**1. 经验增强的智能体学习方法**：这类工作旨在通过利用历史经验来提高数据利用率。一种直接的方法是让智能体进行自我反思，并将反思结果作为上下文指导。然而，当基础模型能力较弱或任务复杂时，自我反思可能不可靠，产生幻觉。为了提升经验的可靠性，一些研究专注于提高所收集经验的质量，例如通过专门的数据结构维护自动优化的经验库，或使用专用的经验模型从智能体交互中动态提炼结构化经验。另一些研究则侧重于设计多阶段检索启发式方法，以从累积的经验库中筛选出最有价值的经验。本文与这些工作的区别在于，指出先前方法将经验视为静态资源（固定的经验库或非自适应的经验提取器），导致经验与智能体不断进化的能力逐渐失配。本文提出的互补强化学习则强调**经验提取器与策略执行器必须在训练过程中协同进化**。

**2. 神经科学启发的学习系统**：本文的核心灵感来源于神经科学中的互补学习系统理论。该理论指出，大脑通过新皮层（形成缓慢、结构化的长期知识，类似于策略）和海马体（管理快速、情景特定的记忆，类似于生成的经验）两个互补系统来协调学习。本文借鉴这一思想，设计了由策略执行器和经验提取器两个互补模型组成的框架，二者通过强化学习进行相互优化，形成了一个封闭的协同进化循环。

**3. 强化学习算法与训练框架**：本文属于旨在提升智能体样本效率的强化学习算法范畴。与仅依赖稀疏结果奖励的基线方法相比，本文方法通过动态提炼和利用经验来提供更丰富的学习信号。此外，为了满足大规模高效训练的需求，本文还设计了一个**异步训练框架**，其中央化的经验管理器将智能体交互、经验提炼和双模型优化解耦，避免了额外的阻塞延迟，这与那些可能引入同步瓶颈或简单静态经验库的方法不同。

综上所述，本文在现有利用历史经验的工作基础上，关键性地解决了经验与智能体能力动态对齐的问题，并通过引入协同进化机制和高效的异步架构，推动了经验驱动智能体学习范式的发展。

### Q3: 论文如何解决这个问题？

论文通过提出“互补强化学习”框架来解决经验与策略演员在训练过程中逐渐错位的问题，其核心是让经验提取器和策略演员在RL优化循环中实现协同进化。整体框架包含两个主要模块：基于LLM的策略演员πθ和经验提取器πφ，它们共享一个经验库M。演员通过稀疏的结果奖励（如任务成功与否的二元奖励）进行优化，而经验提取器则根据其提炼的经验是否能显著提升演员的成功率来优化，形成一个相互强化的闭环。

关键技术在于协同进化机制的设计。对于经验提取器，算法采用CISPO目标进行优化，其关键创新是使用基于批次级别的优势估计Âi = r(mi) - r̄（其中r(mi)为经验条目mi引导产生的二元奖励，r̄为批次平均奖励），并通过裁剪的重要性采样比来约束策略更新，防止经验分布剧烈变动，确保稳定训练。对于策略演员，论文改进了标准的GRPO优化方法，创新性地提出了分组优势估计。具体而言，将每个任务下的K条轨迹样本均匀分为两个子组：经验引导组和无经验组。为避免两组间奖励尺度差异导致的优势估计偏差，算法分别在每个子组内计算归一化优势Âc = (r(τc) - r̄c)/σc，并以此计算裁剪替代损失。这种条件分离的优势估计确保了两种模式下的学习信号完整性，防止演员过度依赖外部经验而无法内化能力，从而实现了稳定且均衡的优化。

该方法的创新点主要体现在三个方面：一是提出了演员与经验提取器协同进化的范式，从根本上解决了静态经验库的错位问题；二是为经验提取器设计了基于因果重要性采样策略优化的稳定训练目标；三是为演员引入了分组优势估计机制，有效平衡了经验利用与自主能力发展。通过这种设计，经验库能够动态适配演员能力的演进，持续提供高质量指导，最终提升了样本效率和性能。

### Q4: 论文做了哪些实验？

论文在四个开放环境中进行了实验评估：MiniHack、WebShop、ALFWorld 和 SWE-Bench。实验设置方面，使用 Qwen2.5-7B-Instruct 作为策略行动者（actor），Qwen3-4B-Thinking-2507 作为经验提取器（experience extractor），所有对比方法均采用相同的超参数以确保公平比较。

在数据集/基准测试方面，训练过程中跟踪 MiniHack 和 WebShop 的成功率，并对 ALFWorld 和 SWE-Bench 的保留评估集计算奖励。最终所有方法均在固定的评估任务上进行性能评估。

对比方法主要与不学习历史经验、仅基于稀疏结果反馈的智能体强化学习基线进行比较。主要结果显示，Complementary RL 在单任务场景中显著优于基线，实现了约 10% 的性能提升。具体而言，在四个环境上的评估得分均表现出优势，证明了该方法能够通过经验提取器与策略行动者的协同进化，有效利用历史经验提升学习效率。此外，该方法在多任务设置中也展现出良好的可扩展性。关键数据指标包括 MiniHack 和 WebShop 的成功率提升，以及 ALFWorld 和 SWE-Bench 的奖励分数增长，这些结果共同验证了 Complementary RL 作为高效经验驱动智能体学习范式的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的互补强化学习（Complementary RL）虽然通过经验提取器与策略执行器的协同进化提升了样本效率，但仍存在一些局限性和可进一步探索的方向。首先，其经验提取器的优化依赖于策略执行器的成功信号，这在复杂或稀疏奖励环境中可能不够稳定，未来可研究更鲁棒的经验价值评估机制，例如引入内在好奇心或不确定性估计来指导经验选择。其次，当前方法主要关注单任务和有限的多任务场景，对于大规模、跨领域的终身学习适应性尚未验证，可探索动态经验库架构，使经验能够按任务相关性进行聚类和检索。此外，论文未深入分析经验与策略的“对齐度”量化指标，未来可设计更精细的协同进化度量，以实时监测并调整两者的交互。最后，受神经科学启发的互补学习机制仍较为简化，可结合记忆巩固、睡眠模拟等理论，使经验提取更贴近生物系统的高效性，从而进一步提升智能体在开放环境中的泛化与适应能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为互补强化学习（Complementary RL）的新方法，旨在解决基于大语言模型的智能体在强化学习中样本效率低下的问题。核心问题在于传统方法不仅面临稀疏奖励反馈的挑战，还难以有效利用跨回合的历史经验：现有方法存储的经验要么是静态的，要么无法与持续改进的策略执行器协同进化，导致经验与执行器能力逐渐失配，其效用随训练进程下降。

受神经科学中互补学习系统的启发，该方法的核心贡献是设计了一个在RL优化循环内实现经验提取器与策略执行器无缝协同进化的框架。具体而言，策略执行器通过稀疏的结果奖励进行优化，而经验提取器的优化目标则是其提炼的经验是否被证明能显著提升执行器的成功率。这种设计使得经验管理策略能够与执行器日益增长的能力同步演化。

实验结果表明，该方法在单任务场景中性能优于不学习经验的基线方法，实现了约10%的性能提升，并在多任务设置中展现出良好的可扩展性。主要结论是，互补强化学习确立了一种高效、由经验驱动的智能体学习新范式，显著提升了训练效率和智能体的最终性能。
