---
title: "From Multi-Agent to Single-Agent: When Is Skill Distillation Beneficial?"
authors:
  - "Binyan Xu"
  - "Dong Fang"
  - "Haitao Li"
  - "Kehuan Zhang"
date: "2026-04-02"
arxiv_id: "2604.01608"
arxiv_url: "https://arxiv.org/abs/2604.01608"
pdf_url: "https://arxiv.org/pdf/2604.01608v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "技能蒸馏"
  - "评估指标"
  - "自适应框架"
  - "单智能体"
  - "效率优化"
  - "理论分析"
relevance_score: 7.5
---

# From Multi-Agent to Single-Agent: When Is Skill Distillation Beneficial?

## 原始摘要

Multi-agent systems (MAS) tackle complex tasks by distributing expertise, though this often comes at the cost of heavy coordination overhead, context fragmentation, and brittle phase ordering. Distilling a MAS into a single-agent skill can bypass these costs, but this conversion lacks a principled answer for when and what to distill. Instead, the empirical outcome is surprisingly inconsistent: skill lift ranges from a 28% improvement to a 2% degradation across metrics of the exact same task. In this work, we reveal that skill utility is governed not by the task, but by the evaluation metric. We introduce Metric Freedom ($F$), the first a priori predictor of skill utility. $F$ measures the topological rigidity of a metric's scoring landscape by quantifying how output diversity couples with score variance via a Mantel test. Guided by $F$, we propose a two-stage adaptive distillation framework. Stage 1 acts as a selective extraction mechanism, extracting tools and knowledge while discarding restrictive structures on "free" metrics to preserve exploration. Stage 2 targets computationally intensive iterative refinement exclusively toward "rigid" metrics ($F \lesssim 0.6$) to eliminate trajectory-local overfitting. Evaluating across 4 tasks, 11 datasets, and 6 metrics, $F$ strongly predicts skill utility ($ρ= -0.62$, $p < 0.05$). Strikingly, identical agent trajectories yield diametrically opposite skill lifts under rigid versus free metrics, demonstrating that skill utility is fundamentally a metric-level property. Driven by this signal, our adaptive agent matches or exceeds the original MAS while reducing cost up to 8$\times$ and latency by up to 15$\times$.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）向单智能体技能蒸馏过程中一个根本性的、悬而未决的问题：**何时进行技能蒸馏才真正有益？** 研究背景是，为了处理复杂任务，领域普遍采用多智能体系统来分解问题并集成专业知识，但这带来了高昂的协调开销、上下文碎片化和脆弱的阶段排序等问题。将MAS蒸馏为具备专项技能的单智能体系统，虽能规避这些成本，但现有方法存在严重不足。它们主要关注“如何”蒸馏（例如，通过刚性结构转换或迭代轨迹优化），却将蒸馏效果的不一致性（在同一任务上，技能提升可从+28%到-2%不等）视为不可预测的任务复杂性副产品，并默认技能增强总是有益的。这种“一刀切”的方法存在关键盲点：非自适应的结构转换会在简单查询上过度约束智能体，而迭代方法则容易陷入轨迹局部过拟合，导致技能库膨胀直至检索失效。

本文的核心发现是，技能蒸馏的效用并非由任务本身决定，而是由**评估指标的拓扑特性**所主导。因此，论文要解决的核心问题是：**提供一个先验的、可量化的原则，来预测技能蒸馏在何种情况下有效，并据此设计一个自适应的蒸馏框架。** 为此，作者引入了“度量自由度”（Metric Freedom, F）这一概念，作为首个技能效用的先验预测指标。F通过Mantel检验量化输出多样性与得分方差之间的耦合程度，来衡量评分地形的拓扑刚性。基于F的指导，论文提出了一个两阶段自适应蒸馏框架，能够根据指标的刚性程度，有选择地提取知识、丢弃限制性结构，并仅在有益的方向上进行计算密集型的迭代优化，从而在保证或提升性能的同时，大幅降低计算成本和延迟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体系统框架、单智能体技能获取与优化，以及智能体性能比较与压缩。

在**多智能体系统（MAS）框架**方面，相关工作包括AutoGen、MetaGPT等通用框架，以及APEX-SQL、MATMCD、CAIS和FELA等面向特定任务（如文本转SQL、因果发现、特征工程）的系统。这些系统通常依赖严格的阶段顺序、智能体间消息传递和专门化的子智能体，虽有效但带来了协调开销。本文则研究如何将这些MAS中的特定组件（如工具、知识、启发式方法）转化为单智能体技能，而非一般性地比较单/多智能体。

在**单智能体技能获取与优化**方面，相关工作探索了如何使单智能体具备多智能体的能力。例如，有研究通过技能库让单智能体匹配MAS性能，但发现技能数量超过临界值后收益递减；OneFlow通过优化单智能体执行图来提升效率；AgentArk则通过分层微调将多智能体推理轨迹蒸馏到单一模型中，实现“智能体压缩”。此外，EvoSkill和Voyager通过自主探索和失败分析来发现与积累可转移技能。本文与这些工作的关键区别在于：它提出了一个先验的度量标准——“度量自由度（F）”，用以预测何时进行技能蒸馏是有益的，并提供了一个两阶段的自适应蒸馏框架。该框架不是无差别地积累技能，而是根据度量特性选择性提取知识，并针对“刚性”度量进行定向迭代优化。

在**智能体性能比较与压缩**方面，已有研究对MAS与单智能体的性能进行了实证比较，并揭示了技能质量的重要性。本文在此基础上进一步指出，技能效用本质上是一个与评估度量相关的属性，相同的智能体轨迹在不同“自由度”的度量下可能产生截然相反的性能提升或下降。这为理解技能蒸馏的收益提供了新的理论视角。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的自适应蒸馏框架来解决多智能体系统（MAS）向单智能体技能转换时效果不一致的问题，其核心是引入了首个先验预测指标——度量自由度（Metric Freedom, $F$），并以此指导整个蒸馏过程。

**整体框架与核心方法**：
框架分为两个阶段。**第一阶段**是自适应的多智能体蒸馏器，其设计原则是：对智能体施加结构性约束的价值，与这些约束在允许输出多样性的度量上限制探索的程度成反比。该阶段包含四个关键步骤：1) **度量分析**：通过计算$F$值来量化评估指标的“刚性”。$F$定义为$F = 1 - \rho(D^{out}, D^{score})$，其中$\rho$是输出距离矩阵$D^{out}$与得分距离矩阵$D^{score}$之间的斯皮尔曼等级相关性（Mantel检验）。$F$值低（≈0）表示指标“刚性”强，输出微小差异导致得分显著变化；$F$值高（≈1）表示指标“自由”，多样输出可能获得相似高分。2) **组件清点**：分解MAS架构，识别每个智能体的可调用工具、领域知识、经验启发式和协调机制。3) **$F$依赖的转换**：根据$F$值（低: <0.25, 中: 0.25–0.65, 高: >0.65）决定保留或丢弃哪些组件。核心规则是：始终保留所有可调用工具（因其扩展能力而不限制推理）；将领域知识编码为条件性参考而非强制指令；丢弃强制的流水线顺序和协调机制（因单智能体内部已具备多视角推理能力）。对于任务分解结构，仅在低$F$时保留作为建议阶段，在中$F$时作为条件提示，在高$F$时则完全丢弃。4) **验证**：确保生成技能的正确性。

**第二阶段**是一个可选的技能迭代器，专门针对刚性指标（$F \lesssim 0.6$）进行自动优化。它采用一个四智能体架构：**探索智能体**分析基准结构；**主智能体**作为协调器管理迭代流程；**分析器智能体**在每轮迭代中诊断性能根因并输出修订后的技能；**运行器智能体**执行评估。迭代过程包括评估、总结失败案例、分析和写入修订。分析器将根因分类（如工具错误、忽略指引等），并针对性修复技能指引、工具覆盖或思维路径。迭代在收敛、达到性能阈值、出现振荡或预算耗尽时终止。

**创新点**：
1.  **理论创新**：提出了“度量自由度”（$F$）这一概念，首次将技能效用的预测从任务层面转移到评估指标层面，揭示了相同任务下技能提升效果迥异的根本原因。
2.  **方法创新**：设计了一个由$F$值驱动的、两阶段自适应蒸馏框架。第一阶段根据$F$值选择性提取知识和结构，在自由度量上保留探索性，在刚性度量上提供结构化指导。第二阶段针对刚性度量进行定向迭代优化，避免了对自由度量进行无效优化可能导致的过拟合。
3.  **组件处理原则**：明确区分了MAS中的协调结构（应丢弃）与任务分解结构（依$F$值选择性保留），并制定了工具、知识、启发式等组件的差异化保留策略，确保了生成技能既高效又灵活。

### Q4: 论文做了哪些实验？

实验在四个数据挖掘任务（Text-to-SQL、因果估计、因果发现、特征工程）上进行，共使用11个基准数据集（如BIRD-147、Spider-120、CauSciBench的子集等）。实验设置上，计算了度量自由度（F）作为先验预测指标，并采用两阶段自适应蒸馏框架。对比方法包括原始多智能体系统（如APEX-SQL、CAIS等）、无技能的单智能体（Claude Code Raw）、保持原始管道结构的MAS编译器，以及所提方法的两个阶段（自适应技能和自动优化）。主要结果显示，F与技能提升呈显著负相关（ρ = -0.62，p < 0.05），表明在刚性度量（F较低）上蒸馏效益最大。具体性能上，自适应技能在多数任务上匹配或超越原始多智能体，例如在因果估计的MSA度量上提升显著，同时在Text-to-SQL的执行准确率（EX）上优于单智能体基线（在BIRD-147上提升8.8个百分点）。关键数据指标包括：成本降低最高达8倍，延迟减少最高达15倍。实验验证了F能预测技能效用，且自适应蒸馏在性能和效率上均具优势。

### Q5: 有什么可以进一步探索的点？

本文的核心贡献是提出了度量自由度（F）作为技能蒸馏效用的先验预测指标，并基于此设计了自适应蒸馏框架。然而，研究仍存在一些局限性和值得深入探索的方向。

首先，论文的验证集中于相对有限的领域（4个任务、11个数据集），其结论在更复杂、开放式的任务（如具身智能、开放世界游戏）中的普适性有待检验。其次，F指标的计算依赖于对智能体输出轨迹的统计分析，这在在线学习或环境动态变化场景中可能面临挑战。此外，当前框架主要关注“何时”蒸馏，对“蒸馏什么”（即技能的具体表征形式）的探讨尚不深入。

未来的研究可以从以下几个方向展开：
1.  **理论深化**：探索F指标与任务马尔可夫决策过程（MDP）内在结构（如奖励稀疏性、状态空间拓扑）的理论联系，建立更坚实的理论基础。
2.  **动态与在线蒸馏**：研究在非稳态环境或在线交互中，如何动态评估度量特性并实时调整蒸馏策略，使单智能体能持续适应。
3.  **技能表征与组合**：结合因果发现或符号抽象等方法，不仅蒸馏原始动作序列，更提炼可解释、可组合的高层技能或子策略模块，提升蒸馏结果的泛化性和可复用性。
4.  **超越性能指标**：将分析扩展到包括安全性、公平性、能耗等多元、可能冲突的评估维度，研究多目标权衡下的蒸馏原则。

总之，将技能蒸馏从一种经验性技术转化为一门可预测、可调控的“科学”，仍需在理论、算法和应用层面进行大量探索。

### Q6: 总结一下论文的主要内容

这篇论文探讨了将多智能体系统（MAS）蒸馏为单智能体技能的核心问题：何时以及如何进行蒸馏才能带来性能提升。研究发现，技能效用的关键决定因素并非任务本身，而是评估指标的特性。

论文的核心贡献是提出了“度量自由度”（F），这是一个先验预测器，用于量化评估指标评分地形的拓扑刚性。F通过Mantel检验测量输出多样性与得分方差之间的耦合程度，从而预测技能蒸馏的效用。基于F的指导，作者设计了一个两阶段自适应蒸馏框架：第一阶段针对“自由”指标（F值较高），选择性提取工具和知识，同时摒弃限制性结构以保持探索能力；第二阶段则专门针对“刚性”指标（F ≲ 0.6），进行计算密集的迭代优化，以避免轨迹局部过拟合。

主要结论是，技能效用本质上是一个度量层面的属性。在4个任务、11个数据集和6个指标上的评估表明，F能强有力地预测技能效用（ρ = -0.62）。研究显示，相同的智能体轨迹在刚性指标与自由指标下会产生截然相反的性能变化。基于此信号构建的自适应智能体，在成本降低高达8倍、延迟减少高达15倍的同时，达到或超越了原多智能体系统的性能。
