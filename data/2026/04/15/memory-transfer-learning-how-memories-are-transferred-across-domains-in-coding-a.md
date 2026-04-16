---
title: "Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents"
authors:
  - "Kangsan Kim"
  - "Minki Kang"
  - "Taeil Kim"
  - "Yanlai Yang"
  - "Mengye Ren"
  - "Sung Ju Hwang"
date: "2026-04-15"
arxiv_id: "2604.14004"
arxiv_url: "https://arxiv.org/abs/2604.14004"
pdf_url: "https://arxiv.org/pdf/2604.14004v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Coding Agent"
  - "Memory"
  - "Transfer Learning"
  - "Self-Evolution"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

## 原始摘要

Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: https://memorytransfer.github.io/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于记忆的自进化编码智能体（coding agents）中，记忆利用范围受限的问题。研究背景是，随着语言模型通过扩大训练数据带来的性能提升逐渐趋于平缓，利用先前的推理结果来增强未来性能、无需额外监督的“自进化”范式，成为提升智能体能力的重要方向。记忆在其中扮演核心角色，它允许智能体从过去的经验中提取可重用的工作流和可迁移的见解，应用于后续任务。

然而，现有方法的不足在于，它们通常将记忆的生成和检索限制在**同质任务领域**（例如同一基准测试集内）。在现实世界中，编码智能体需要处理多样化的编程问题（如软件工程、机器学习开发、算法竞赛等），尽管任务各异，但它们共享着共同的基础设施（如运行时环境、编程语言、跨文件依赖栈）。现有方法未能利用这一共享基础，从而无法从异构领域构成的更丰富的记忆池中获益，限制了智能体性能的进一步提升。

因此，本文要解决的核心问题是：**如何实现跨领域的记忆迁移学习（Memory Transfer Learning, MTL）**，以释放异构领域记忆的潜力。具体而言，论文通过构建统一的异构领域记忆池，系统性地探究了三个关键研究问题：跨领域记忆是否能提升编码智能体性能；其带来收益的原因是什么；以及哪些因素（如记忆的抽象程度）最影响迁移效果。最终目标是建立经验性的设计原则，将记忆利用的范围从单一领域扩展到多个领域。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码智能体、基于记忆的自进化智能体，以及迁移学习在智能体中的应用。

在代码智能体方面，早期研究如AlphaCodium、LDB专注于单文件级别的代码生成与调试；后续工作如CodeAgent、RepoAgent扩展至仓库级代码修改；还有领域特定智能体如Paper2Code和BixbBench。这些研究为编码任务提供了基础，但通常局限于特定任务或领域。

在基于记忆的自进化智能体方面，AWM、ReasoningBank、Dynamic Cheatsheet、ReMe和MemEvolve等研究提出了记忆的生成、检索与利用机制，以帮助智能体复用成功经验、避免错误。然而，这些工作主要评估同领域内的记忆使用，未充分探索跨领域记忆的潜在价值。

在迁移学习与知识复用方面，传统方法依赖参数适应，而近期研究如in-context learning探索了基于上下文的非参数知识迁移。在智能体领域，AgentKB提出了跨任务领域的统一记忆池管理框架，但其未深入分析记忆迁移的内在机制（如何种知识可迁移、如何生成适于迁移的记忆），且其记忆池通常跨异构环境（如推理、网页交互、编码），未能充分挖掘编程任务特有的共享原则（如运行时环境、编程语言）。

本文与这些工作的关系在于，它直接建立在记忆自进化智能体和跨领域知识迁移的研究基础上。其区别在于：本文首次系统性地研究了编码智能体中的**跨领域记忆迁移**，重点关注记忆的**表示形式**（从具体轨迹到抽象见解）对迁移效果的影响，并深入分析了迁移的机制（如元知识转移、抽象度决定可迁移性），从而为利用编码任务间共享的基础设施提供了实证设计原则。

### Q3: 论文如何解决这个问题？

论文通过提出“记忆迁移学习”框架来解决跨领域记忆利用不足的问题。其核心方法是构建一个异构任务领域的统一记忆池，并设计了两阶段记忆利用流程：离线记忆生成与在线记忆检索。

整体框架包含三个主要模块。首先是记忆生成模块，该模块基于智能体在多个基准测试上的推理轨迹，利用LLM构建了四种抽象层级递增的记忆表示：轨迹记忆（Trajectory）、工作流记忆（Workflow）、总结记忆（Summary）和洞察记忆（Insight）。轨迹记忆保留了原始动作和观察序列；工作流记忆提取了可复用的代码片段序列；总结记忆概括了任务、环境、结果及成败分析；洞察记忆则提炼出最高层次的通用性原理与元知识。其次是记忆池构建模块，将除当前测试集外所有其他领域的记忆，按类型汇集并建立基于文本嵌入的索引。最后是记忆检索与应用模块，在推理时，通过计算当前任务与记忆的嵌入向量相似度，检索出最相关的N条记忆，并将其作为系统提示的一部分提供给编码智能体，以辅助其解决新任务。

关键技术在于对记忆表征的抽象化设计及其与迁移性的关联。研究发现，抽象程度决定了迁移效果：高层次的洞察记忆能有效传递跨领域的元知识（如验证流程、通用策略），从而带来平均3.7%的性能提升；而低层次的轨迹记忆因包含过多具体细节，容易导致负迁移。此外，框架的创新点包括：证明了迁移效果随记忆池规模扩大而提升；实现了不同模型间记忆的迁移；并通过实验确立了“抽象化促进泛化”的设计原则，为突破单领域记忆孤岛提供了实证基础。

### Q4: 论文做了哪些实验？

论文在六个编程基准测试上进行了实验，评估了跨领域记忆迁移学习（MTL）的效果。实验设置包括使用四种不同抽象层次的记忆表示：轨迹（Trajectory）、工作流（Workflow）、摘要（Summary）和洞察（Insight），并构建了一个包含431条记忆的统一记忆池。数据集包括LiveCodeBenchv6（LCB）、SWEBench-Verified（SWEB）和ReplicationBench（RepliB）等六个基准。对比方法包括零样本（Zeroshot）基线以及两种自进化方法ReasoningBank和AgentKB。主要结果显示，MTL方法平均性能比零样本提升3.7%，其中洞察记忆带来的提升最高（部分基准达8.3%）。关键指标Pass@3显示，MTL平均得分为0.630，优于ReasoningBank（0.601）和AgentKB（0.613）。分析表明，迁移效果主要来自元知识（如验证流程、结构化工作流），而非具体代码；记忆抽象度越高，迁移性越好（洞察>摘要>工作流>轨迹）。此外，实验还验证了方法在不同模型（如DeepSeek V3.2和Qwen3-Coder）上的有效性，平均提升分别为2.6%和1.8%，并发现记忆池规模扩大能进一步提升性能。

### Q5: 有什么可以进一步探索的点？

该论文在跨领域记忆迁移学习方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，研究主要关注了记忆的抽象程度对迁移效果的影响，但未深入探讨记忆的**动态筛选与更新机制**。当前方法使用静态记忆池，未来可研究如何根据目标任务的实时反馈，动态评估记忆的相关性与可靠性，从而避免负迁移并提升效率。

其次，论文发现迁移的主要贡献来自元知识（如验证流程），而非具体算法。这提示我们，可以进一步探索**元知识的结构化表示与生成**。例如，能否设计一种机制，自动从原始轨迹中提炼出更泛化、可组合的“元技能”模板，从而系统化地提升智能体的推理与决策能力。

此外，实验主要在代码生成领域进行，其结论在其他领域（如机器人任务规划、科学发现）的普适性有待验证。未来工作可以探索**跨模态记忆迁移**，例如将代码调试中的“分步验证”策略迁移到物理实验的故障诊断中，检验元知识迁移的边界与条件。

最后，论文提到了记忆池规模扩大能提升效果，但未分析计算成本与收益的平衡。一个重要的改进方向是开发**轻量级记忆检索与融合算法**，例如通过记忆聚类或稀疏激活机制，在保持性能的同时降低检索开销，使该方法更适用于资源受限的场景。

### Q6: 总结一下论文的主要内容

本文研究了记忆迁移学习（MTL）在代码智能体中的应用，旨在解决现有基于记忆自我演进的智能体通常局限于同质任务领域、未能充分利用跨领域共享基础设施（如运行时环境和编程语言）的问题。其核心贡献在于探索并验证了如何利用来自异构领域的统一记忆池来提升智能体性能。

论文方法上，作者构建了一个跨领域的统一记忆池，并评估了四种不同抽象层级的记忆表示（从具体的执行轨迹到抽象的见解）在六个编码基准测试上的效果。主要结论包括：1）跨领域记忆平均能提升3.7%的性能，其增益主要源于元知识（如验证例程）的迁移，而非具体任务代码；2）抽象程度决定可迁移性，高层见解泛化性好，而低层具体轨迹常因过度特化导致负迁移；3）迁移效果随记忆池规模扩大而提升，且记忆可在不同模型间迁移。这项工作为打破单领域记忆孤岛、建立跨领域记忆利用的实证设计原则奠定了基础。
