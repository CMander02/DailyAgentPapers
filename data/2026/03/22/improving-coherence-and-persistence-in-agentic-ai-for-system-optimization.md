---
title: "Improving Coherence and Persistence in Agentic AI for System Optimization"
authors:
  - "Pantea Karimi"
  - "Kimia Noorbakhsh"
  - "Mohammad Alizadeh"
  - "Hari Balakrishnan"
date: "2026-03-22"
arxiv_id: "2603.21321"
arxiv_url: "https://arxiv.org/abs/2603.21321"
pdf_url: "https://arxiv.org/pdf/2603.21321v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Architecture"
  - "Long-Horizon Planning"
  - "Knowledge Persistence"
  - "System Optimization"
  - "Multi-Agent Collaboration"
  - "Code Generation"
relevance_score: 7.5
---

# Improving Coherence and Persistence in Agentic AI for System Optimization

## 原始摘要

Designing high-performance system heuristics is a creative, iterative process requiring experts to form hypotheses and execute multi-step conceptual shifts. While Large Language Models (LLMs) show promise in automating this loop, they struggle with complex system problems due to two critical failure modes: evolutionary neighborhood bias and the coherence ceiling. Evolutionary methods often remain trapped in local optima by relying on scalar benchmark scores, failing when coordinated multi-step changes are required. Conversely, existing agentic frameworks suffer from context degradation over long horizons or fail to accumulate knowledge across independent runs.
  We present Engram, an agentic researcher architecture that addresses these limitations by decoupling long-horizon exploration from the constraints of a single context window. Engram organizes exploration into a sequence of agents that iteratively design, test, and analyze mechanisms. At the conclusion of each run, an agent stores code snapshots, logs, and results in a persistent Archive and distills high-level modeling insights into a compact, persistent Research Digest. Subsequent agents then begin with a fresh context window, reading the Research Digest to build on prior discoveries.
  We find that Engram exhibits superior performance across diverse domains including multi-cloud multicast, LLM inference request routing, and optimizing KV cache reuse in databases with natural language queries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动化设计高性能系统启发式算法（heuristics）时，现有方法在**长期探索**和**知识积累**方面存在的根本性缺陷。

**研究背景**：为计算机系统设计高效的启发式算法是一个需要专家进行假设、测试和多次概念性调整的创造性迭代过程。近期研究尝试利用LLM自动化此循环，但在处理复杂系统问题时效果不佳。

**现有方法的不足**主要体现在两个关键失败模式：
1.  **进化邻域偏差**：基于代码进化的方法通过变异代码并根据标量基准分数选择候选方案。这种方法在需要渐进式优化时有效，但当改进需要**协调的多步骤变革**（如重新表述问题、引入可处理的松弛条件，或为转向不同算法家族而接受暂时性能回退）时，容易陷入局部最优。
2.  **连贯性天花板**：现有的智能体框架（如Glia）支持假设形成和定向实验，但受限于**单一、长运行的上下文窗口**，会随着时间推移出现注意力分散、上下文质量下降的“上下文腐化”问题。反之，运行多个独立的“最佳N次”尝试则无法**跨运行积累知识**，每次尝试都需从头开始重新发现相同的建模见解。

**本文要解决的核心问题**是：如何设计一种智能体架构，既能维持**长视野探索的连贯性**，又能**持久地积累和复用知识**，从而突破上述限制，使LLM能像人类专家一样进行持续、累积性的系统优化研究。为此，论文提出了Engram架构，其核心创新在于将长视野探索与单一上下文窗口的约束解耦，通过引入持久化档案和结构化研究摘要，实现跨智能体序列的知识传递与累积进步。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类方法，并围绕三个核心标准（连贯性、灵活性、持久性）展开讨论。

**1. 基于代码突变的进化方法**：这类方法，如FunSearch、AlphaEvolve、OpenEvolve、Evolution of Heuristics、GEPA以及ADSR，通过LLM对代码候选进行变异，并用基准测试的标量分数来指导后续代际选择。它们的特点是**持久性高**，能够进行长时间的搜索。然而，其**连贯性和灵活性低**，因为它们使用固定的提示模板，仅包含先前的代码片段和分数，无法编码设计者演进的推理思路，容易陷入局部最优，难以执行需要协调的多步骤概念转变。

**2. 基于推理和灵活工具的迭代设计方法**：以Glia为代表，这类方法受Codex等编码代理启发。代理在具有工具访问权限的编程环境中工作，通过一系列连贯的动作（如运行实验、分析数据）来探索设计问题，因此具有**高连贯性和高灵活性**。但其主要弱点是缺乏**持久性**：随着探索步骤增加，上下文会增长至极限或导致性能下降。虽然Glia尝试启动多个独立代理来缓解，但代理间不共享知识，导致知识无法积累，限制了长期进展。

本文提出的Engram架构旨在弥合这两类方法的差距。它通过引入持久化的档案库（Archive）和研究摘要（Research Digest），将长程探索与单一上下文窗口的限制解耦，使得后续代理能在全新上下文中基于先前的发现继续构建。因此，Engram同时实现了高连贯性、高灵活性和高持久性，解决了现有方法在复杂系统优化问题上的关键失败模式。

### Q3: 论文如何解决这个问题？

论文通过提出名为Engram的智能体研究架构来解决进化邻域偏差和连贯性天花板这两个核心问题。其核心方法是**将长视野探索与单一上下文窗口的约束解耦**，通过一系列迭代工作的智能体，并结合持久化知识存储与传递机制，实现知识的跨轮次积累。

整体框架是一个**顺序执行的智能体序列**，每个智能体都遵循“假设→实现→实验→分析→再假设”的科学研究循环来探索启发式设计。关键创新在于引入了两个外部持久化组件：**Archive（档案库）** 和**Research Digest/Ledger（研究摘要/账本）**。Archive存储代码快照、日志和结果等原始产出物；而Research Digest则是由每个智能体在结束时，将其探索中获得的高级建模见解提炼成的**结构化、紧凑的知识摘要**。

主要工作流程如下：每个智能体在一个独立的工作空间中运行，可以访问用户提供的任务相关工件、运行代码的评估工具（如模拟器），并**关键地**，能够通过工具调用按需检索先前智能体存储在Archive和Ledger中的知识。智能体被系统提示要求遵循严格的研究规程：先回顾问题描述和已有研究，提出具体假设和计划，然后实施代码、运行实验，并进行结构化的事后分析，比较结果、诊断问题，从而理解设计成败的深层原因，而非仅仅生成解决方案。

当一个智能体结束探索时，它会将详细产出存入Archive，并将核心发现、尝试过的策略、有效/无效的方法以及后续建议，以结构化总结的形式写入Ledger。随后，系统会**实例化一个全新的智能体**，其上下文窗口是空的，但它会获得任务描述以及对Archive和Ledger的访问权限。这种“交接”设计是架构上的关键创新点，它**定期刷新LLM的上下文**，避免了长上下文导致的注意力退化问题，同时通过外部化的知识库确保了探索的连贯性和知识的持久性。

因此，Engram的核心创新在于**将“单智能体长上下文内的连贯探索”与“通过结构化知识交接实现的多智能体长视野持久性”相结合**。每个后继智能体都能从一个干净的状态开始，并基于前人的精炼知识继续构建，从而有效突破了局部最优，实现了需要多步协调变革的系统优化。

### Q4: 论文做了哪些实验？

论文在三个系统优化问题上进行了实验：多云组播、LLM推理请求路由以及使用自然语言查询优化数据库中的KV缓存重用。实验设置方面，每个方法运行10次，每次运行有100次评估的预算，并报告90%的自举置信区间。

使用的数据集/基准测试包括：对于多云组播问题，采用了与Cloudcast相同的基准，使用一个包含71个节点的有向拓扑，每条边标注了出口价格和实测吞吐量，评估五种固定源/目的集的广播配置。对于其他两个问题，论文虽未详述具体基准，但提及了它们属于不同的领域。

对比方法包括四种最先进的利用LLM进行发现的框架：启发式进化（EoH）、FunSearch、OpenEvolve和Glia。论文提供了这些框架的具体参数配置，例如EoH的初始种群大小为20，FunSearch的提示程序数量为3，OpenEvolve的岛屿数量为6等。

主要结果如下：Engram在所有问题上均表现出优越性能。在多云组播任务中，使用“方向”提示和o3模型时，Engram取得了最佳平均成本（662美元），并找到了最接近人类最优（SOTA，成本626美元）的解决方案，其最佳单次运行成本甚至达到625美元，略优于人类SOTA。相比之下，进化方法（如OpenEvolve）倾向于停留在Steiner树式启发法上，成本在640至696美元之间；Glia的最佳解决方案成本为687美元。Engram还展示了更强的持久性，能够容忍性能暂时下降并持续在优化算法家族内进行改进，最终发现使用动态规划（DP）和混合整数线性规划（MILP）等新颖方法。实验还表明，提供高层战略指导比提供完整的数学公式更重要，且更强的推理模型（如GPT-5.2）能更可靠地找到这些解决方案。

### Q5: 有什么可以进一步探索的点？

该论文提出的Engram架构在解决长期探索与知识持久化方面迈出了重要一步，但其仍有进一步探索的空间。首先，其“研究摘要”的生成与利用机制较为依赖预设的提炼逻辑，未来可探索更动态、自适应的知识蒸馏方法，例如引入强化学习来评估并优先保留最关键的经验片段。其次，当前架构主要处理代码和日志等结构化信息，对于系统优化中更隐性的、基于自然语言的专家直觉和失败教训的捕捉能力有限，可结合更细粒度的语义记忆网络来增强。此外，论文验证集中于特定系统领域，其通用性有待检验；未来可将框架应用于更广泛的、需创造性突破的科学发现或复杂工程设计问题，以测试其极限。最后，多个智能体间的协作目前是顺序的，引入并行探索与竞争或协同机制，可能进一步提升搜索效率与突破局部最优的能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了名为Engram的智能体研究架构，旨在解决现有LLM在自动化系统启发式设计中的两个关键缺陷：进化邻域偏差和连贯性上限。进化方法依赖标量基准分数，容易陷入局部最优，难以实现需要协调的多步骤变更；而现有智能体框架则受限于单次上下文窗口，在长程探索中会出现上下文退化或无法跨运行积累知识的问题。

Engram的核心方法是将长程探索与单一上下文窗口解耦，组织成一系列迭代设计、测试和分析机制的智能体序列。每个智能体运行结束后，会将代码快照、日志和结果存入持久化档案库，并将高层建模见解提炼为紧凑的研究摘要。后续智能体则从全新上下文窗口开始，通过阅读该摘要继承先前发现，从而实现知识的持续积累与跨任务连贯性。

实验表明，Engram在多云组播、LLM推理请求路由和数据库KV缓存优化等多个领域均优于现有方法，其发现的启发式策略在多个基准测试中超越了人类专家设计和现有自动化方法的性能，证明了该架构在维持长程探索连贯性与持久性方面的有效性。
