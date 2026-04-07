---
title: "Decocted Experience Improves Test-Time Inference in LLM Agents"
authors:
  - "Maohao Shen"
  - "Kaiwen Zha"
  - "Zexue He"
  - "Zhang-Wei Hong"
  - "Siru Ouyang"
  - "J. Jon Ryu"
  - "Prasanna Sattigeri"
  - "Suhas Diggavi"
  - "Gregory Wornell"
date: "2026-04-06"
arxiv_id: "2604.04373"
arxiv_url: "https://arxiv.org/abs/2604.04373"
pdf_url: "https://arxiv.org/pdf/2604.04373v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Reasoning"
  - "Test-Time Inference"
  - "Experience Utilization"
  - "Context Construction"
  - "Agent Architecture"
  - "Agent Evaluation"
  - "Math Reasoning"
  - "Web Agent"
  - "Code Agent"
relevance_score: 8.5
---

# Decocted Experience Improves Test-Time Inference in LLM Agents

## 原始摘要

There is growing interest in improving LLMs without updating model parameters. One well-established direction is test-time scaling, where increased inference-time computation (e.g., longer reasoning, sampling, or search) is used to improve performance. However, for complex reasoning and agentic tasks, naively scaling test-time compute can substantially increase cost and still lead to wasted budget on suboptimal exploration. In this paper, we explore \emph{context} as a complementary scaling axis for improving LLM performance, and systematically study how to construct better inputs that guide reasoning through \emph{experience}. We show that effective context construction critically depends on \emph{decocted experience}. We present a detailed analysis of experience-augmented agents, studying how to derive context from experience, how performance scales with accumulated experience, what characterizes good context, and which data structures best support context construction. We identify \emph{decocted experience} as a key mechanism for effective context construction: extracting essence from experience, organizing it coherently, and retrieving salient information to build effective context. We validate our findings across reasoning and agentic tasks, including math reasoning, web browsing, and software engineering.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在测试时推理效率低下的问题。研究背景是，随着LLM的发展，焦点正从优化模型参数转向改进推理时行为。现有方法主要通过“测试时缩放”来提升性能，即增加推理时的计算量（如更长的推理链、采样或搜索）。然而，对于复杂的推理和智能体任务，这种简单粗暴地增加计算预算的方法存在明显不足：它不仅会大幅提升成本，而且可能导致大量计算资源浪费在对次优路径的无效探索上。

因此，本文提出将“上下文”作为另一个关键的、更高效的缩放维度。核心问题是：如何系统地构建高质量的输入上下文，以引导智能体进行更高效的推理，从而避免对计算资源的盲目扩张。现有方法要么依赖为特定任务手工设计提示或示例（这既不具可扩展性，也可能与智能体的实际能力不匹配），要么虽然利用智能体与环境交互积累的“经验”作为上下文来源，但缺乏对如何将原始经验有效转化为高质量上下文的系统性理解。

具体而言，本文致力于解决三个关键的研究空白：1) 性能如何随累积经验量的增加而扩展；2) 从理论和实证上，有效上下文应具备何种特征；3) 何种数据结构能最好地支持上下文构建。为此，论文引入了“提炼经验”作为核心解决方案，即从原始经验中提取精华、进行连贯组织，并检索关键信息来构建有效的上下文，从而在数学推理、网页浏览和软件工程等任务中实现更优的测试时推理性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕如何在不更新模型参数的情况下提升LLM性能，可分为以下几类：

**1. 测试时计算扩展方法**：这类研究通过增加推理时的计算量（如更长的推理链、采样或搜索）来提升性能，例如思维链（Chain-of-Thought）和自洽性（Self-Consistency）等方法。本文认同计算扩展的有效性，但指出对于复杂的智能体任务，单纯增加计算可能成本高昂且导致资源浪费在次优探索上。

**2. 基于经验的上下文构建方法**：部分先前工作尝试利用智能体与环境交互产生的经验轨迹（如成功或失败的示例）来构建测试时上下文，以指导当前任务。本文与这些工作的关系在于同样以经验作为上下文来源，但区别在于，现有方法多聚焦于特定应用框架，而本文系统性地研究了如何将原始经验转化为有效上下文，并提出了“提炼经验”这一核心机制。

**3. 提示工程与演示构建**：这包括手工设计提示或示例（few-shot demonstrations）来引导模型。本文认为这种方法缺乏可扩展性和可靠性，需要针对每个新任务重新设计，且可能无法与智能体的实际能力对齐。因此，本文转向从自动积累的经验中系统性地构建上下文。

本文的工作超越了上述类别，通过理论分析和实证研究，系统探讨了性能如何随积累的经验规模扩展、有效上下文的特征、以及支持上下文构建的最佳数据结构，从而填补了如何将原始经验转化为高效、可扩展上下文的系统性理解空白。

### Q3: 论文如何解决这个问题？

论文通过引入“经验熬制”这一核心机制来解决LLM智能体在测试时推理中因上下文过长或经验冗余导致的效率低下和性能不佳问题。其核心方法是构建一个基于熬制经验的上下文，以替代原始经验，从而在提升性能的同时控制计算成本。

整体框架包含三个关键模块：经验蒸馏、记忆整合和结构化记忆检索。首先，在**经验蒸馏**模块中，系统将原始交互轨迹（包含环境观察和动作序列）通过智能体自身提炼为简洁的“课程”，这些课程总结了可迁移的推理模式或决策技巧。这避免了直接使用冗长且可能包含噪声的原始轨迹作为上下文，在智能体任务（如WebShop和软件工程）中表现尤为突出，能有效过滤无关信息。

其次，为解决经验积累导致记忆库无限增长和冗余的问题，论文采用了**记忆整合**机制。具体通过基于嵌入向量的k-means聚类，将语义相似的记忆条目合并，仅保留每个簇中最具代表性的条目。研究发现，适度的整合（存在一个“最佳点”）能在减少冗余的同时保持策略多样性，从而提升检索上下文的质量和任务性能，避免因过度压缩丢失关键信息或过度相似限制泛化。

最后，为进一步优化检索，论文提出了**分层概念树**这一结构化记忆。它通过两个阶段构建：1）**概念提取**：使用LLM为每个记忆条目生成结构化的概念描述（如问题主题、模式和技巧）；2）**分层聚类**：基于这些描述的嵌入进行递归二分k-means聚类，形成树状结构。这种设计支持从粗到细的概念级检索，能自适应地控制检索粒度，并超越表面相似性来促进多样性，从而构建出更有效的上下文。

创新点主要体现在：1）**经验熬制**作为核心缩放轴，通过蒸馏和整合在局部和全局两个层面提升可扩展性；2）从信息论角度**理论分析了有效上下文的特征**，即高信息增益能减少输出不确定性，从而缩短推理轨迹，并通过实证验证了上下文质量（平衡相关性与多样性）与性能提升的正相关关系；3）**分层概念树**的结构化记忆设计，系统性地解决了扁平记忆在控制检索粒度和保障多样性方面的不足。

### Q4: 论文做了哪些实验？

论文在数学推理、网页浏览和软件工程三类任务上进行了实验验证。实验设置基于一个固定的基础大语言模型（Seed-OSS-36B-Instruct），通过构建经验记忆库来增强其测试时推理能力。记忆库由过往任务的经验（问题、轨迹和奖励）构成，并通过组织机制（如扁平化记忆）和检索机制（基于Qwen3-Embedding-4B编码器的相似度检索）来构建上下文。对比方法主要考察了不同经验利用方式（如使用原始经验与使用提炼后经验）对性能的影响。

使用的数据集/基准测试包括：数学推理任务使用DAPO-Math构建记忆，并在AMC、AIME、HMMT和BeyondAIME上评估答案精确匹配正确率；网页浏览任务使用WebShop环境，评估最终购买质量；软件工程任务使用SWE-bench，评估生成补丁能否通过测试。

主要结果表明，通过“提炼经验”构建上下文能有效提升代理在测试时的性能和效率。关键数据指标包括：在数学推理任务中，使用提炼经验相比基线（如无经验或原始经验）显著提高了准确率；在WebShop和SWE任务中，提炼经验减少了所需的交互步数（效率指标）并提升了任务成功率（有效性指标）。具体而言，效率通过推理任务的输出令牌数或代理任务的交互步数衡量，而有效性通过多次尝试的平均奖励（avg_m）衡量。实验验证了经验提炼（包括提取精华、组织记忆和检索关键信息）是构建高效上下文的关键机制。

### Q5: 有什么可以进一步探索的点？

该论文聚焦于利用“提炼经验”优化测试时上下文构建，但仍有多个方向值得深入探索。首先，其方法严重依赖历史经验的质量和相关性，在动态或稀疏反馈环境中可能表现不佳，未来可研究如何在线筛选和更新经验，或引入对抗性样本以增强鲁棒性。其次，当前上下文构建可能缺乏对长程任务结构的理解，可探索结合分层或图神经网络来建模经验间的语义关联，实现更精准的检索与组合。此外，该方法未充分考虑计算效率与延迟的平衡，未来可设计自适应机制，根据任务复杂度动态调整经验检索深度。最后，跨任务的经验迁移能力尚未充分验证，可研究如何将提炼经验泛化至未见领域，推动更通用的Agent架构发展。

### Q6: 总结一下论文的主要内容

该论文探讨了在不更新模型参数的情况下提升大语言模型性能的新方向。针对复杂推理和智能体任务，单纯增加测试时计算（如延长推理链或搜索）会显著提高成本且可能导致低效探索。为此，作者提出将**上下文构建**作为提升性能的补充扩展轴，系统研究了如何通过**经验**来构建更好的输入以引导推理。

核心贡献在于提出了**“提炼经验”**这一关键机制，强调从积累的经验中提取本质、进行连贯组织，并检索关键信息以构建有效上下文。论文通过数学推理、网页浏览和软件工程等任务验证了该方法，分析了经验增强型智能体的上下文构建方式、性能随经验积累的扩展规律、优质上下文的特征以及支持上下文构建的最佳数据结构。

研究结论表明，基于提炼经验的上下文构建能更高效地利用测试时计算，相比单纯增加计算量，能以更低成本实现更好的任务性能，为LLM智能体的优化提供了新的实用路径。
