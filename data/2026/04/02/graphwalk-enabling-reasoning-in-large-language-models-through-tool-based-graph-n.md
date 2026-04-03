---
title: "GraphWalk: Enabling Reasoning in Large Language Models through Tool-Based Graph Navigation"
authors:
  - "Taraneh Ghandi"
  - "Hamidreza Mahyar"
  - "Shachar Klaiman"
date: "2026-04-02"
arxiv_id: "2604.01610"
arxiv_url: "https://arxiv.org/abs/2604.01610"
pdf_url: "https://arxiv.org/pdf/2604.01610v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Using Agent"
  - "Graph Reasoning"
  - "Multi-Hop Reasoning"
  - "Agent Framework"
  - "Knowledge Graph"
  - "LLM Agent"
  - "Training-Free"
  - "Agent Evaluation"
relevance_score: 8.5
---

# GraphWalk: Enabling Reasoning in Large Language Models through Tool-Based Graph Navigation

## 原始摘要

The use of knowledge graphs for grounding agents in real-world Q&A applications has become increasingly common. Answering complex queries often requires multi-hop reasoning and the ability to navigate vast relational structures. Standard approaches rely on prompting techniques that steer large language models to reason over raw graph context, or retrieval-augmented generation pipelines where relevant subgraphs are injected into the context. These, however, face severe limitations with enterprise-scale KGs that cannot fit in even the largest context windows available today. We present GraphWalk, a problem-agnostic, training-free, tool-based framework that allows off-the-shelf LLMs to reason through sequential graph navigation, dramatically increasing performance across different tasks. Unlike task-specific agent frameworks that encode domain knowledge into specialized tools, GraphWalk equips the LLM with a minimal set of orthogonal graph operations sufficient to traverse any graph structure. We evaluate whether models equipped with GraphWalk can compose these operations into correct multi-step reasoning chains, where each tool call represents a verifiable step creating a transparent execution trace. We first demonstrate our approach on maze traversal, a problem non-reasoning models are completely unable to solve, then present results on graphs resembling real-world enterprise knowledge graphs. To isolate structural reasoning from world knowledge, we evaluate on entirely synthetic graphs with random, non-semantic labels. Our benchmark spans 12 query templates from basic retrieval to compound first-order logic queries. Results show that tool-based traversal yields substantial and consistent gains over in-context baselines across all model families tested, with gains becoming more pronounced as scale increases, precisely where in-context approaches fail catastrophically.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在处理大规模知识图谱时面临的上下文窗口限制问题。研究背景是，尽管LLMs在推理能力上取得进展，但其表现仍严重依赖于将相关信息全部加载到有限的上下文窗口中。对于企业级应用（如供应链分析），图谱通常包含数十万节点和关系，远超现有最大上下文窗口的容量。现有方法主要依赖提示工程引导LLMs在原始图谱上下文中推理，或采用检索增强生成技术注入相关子图，但这些方法在面对超大规模图谱时都会因上下文不足而失效。

现有方法的不足在于：它们往往针对特定领域设计，需要领域知识嵌入或额外微调，缺乏通用性；且无法从根本上解决海量图谱数据与有限上下文窗口之间的矛盾。本文要解决的核心问题是：如何让未经微调的通用LLMs能够通过工具调用进行序列化图谱导航，从而实现对任意大规模图谱的结构化推理。为此，论文提出了GraphWalk框架，其核心思路是将图谱推理转化为工具组合问题——仅向LLM提供一组最小化的正交图谱操作工具（如节点查找、邻居检索），让模型通过组合这些工具自主探索图谱结构，逐步收集信息并完成复杂查询。这种方法不依赖领域知识或参数记忆，通过合成随机标签图谱的基准测试，确保评估的是纯粹的结构推理能力。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：

**1. 图文本化与检索增强生成（RAG）方法**：这类研究（如GrailQA、WebQSP等基准）将知识图谱结构通过三元组线性化或JSON表示转化为文本，注入LLM上下文窗口进行问答。其核心是检索和格式化相关子图，但面临可扩展性差和难以保持全局图结构的局限。本文的GraphWalk通过工具调用进行顺序导航，避免了将整个图结构塞入上下文的瓶颈。

**2. LLM作为查询生成器**：此类方法训练或提示LLM将自然语言问题转换为SPARQL或Cypher等正式查询语言。它们依赖结构化查询引擎，但将任务视为一次性翻译问题，不适合需要探索性推理的场景，因为查询错误往往导致无法纠正的循环。本文方法则通过多步、可验证的工具调用链支持探索式推理。

**3. 混合LLM-GNN架构**：这类方法将图神经网络与LLM结合，使用GNN学习拓扑感知的节点和边嵌入，以提供压缩的结构表征。其重点是通过改进内部表示来增强LLM理解，而非外显的、可验证的工具使用行为。本文框架则强调通过明确的工具操作产生透明的执行轨迹。

**4. 工具增强的图智能体**：本文工作与此类新兴范式（如Reason-Align-Respond、SubgraphRAG）最为相关，均属于“LLM即智能体”在图表领域的应用。其中，KG-Agent采用了基于工具的方法，但其为7B的LLM微调了基于KGQA数据集合成的代码指令数据，并提供了13个专用工具。**本文GraphWalk的核心区别在于**：它评估LLM仅使用**最小化、通用**的图操作（迷宫任务2个工具，随机图实验4个工具）进行结构推理的能力，不编码任何领域特定逻辑。通过移除任务特定的脚手架和语义知识（使用合成图），本文隔离并聚焦于所有图-LLM集成方法最终都依赖的**核心推理能力**本身。

### Q3: 论文如何解决这个问题？

GraphWalk 通过一个免训练、与问题无关的、基于工具的框架来解决大语言模型在大型知识图谱上进行多跳推理的难题。其核心方法是让现成的LLM通过顺序性的图导航来进行推理，而不是依赖将整个图谱或子图注入上下文窗口的传统方法。

整体框架采用智能体（Agent）模式，LLM作为规划器，与一个确定性的图执行器交互。框架为LLM配备了一组最小但正交的图遍历工具，足以探索任何图结构。在迷宫遍历任务中，工具集包括 `get_possible_next_cells`（获取当前节点的可通行相邻单元）和 `get_connected_path`（基于已访问节点计算连通路径）。在更通用的合成知识图谱推理任务中，工具集演变为：`get_node_by_property`（按属性查找节点）、`get_all_nearest_neighbors`（获取节点的所有直接邻居）、`get_unique_property_values`（枚举属性的所有可能值）以及用于记录思考过程的 `think` 工具。

主要创新点在于其极简主义和可组合性的设计哲学。首先，工具设计是通用的，不编码任何特定领域的知识或高级算法（如最短路径计算），迫使LLM必须通过组合基本操作来构建复杂的推理链。其次，该方法将推理过程转化为可验证的步骤序列，每个工具调用都产生透明的执行轨迹，增强了可解释性。第三，通过使用完全随机、无语义标签的合成图谱进行评测，彻底隔离了模型参数知识的影响，纯粹评估其结构推理能力。实验表明，即使图谱小到可以完全放入上下文窗口，无工具的基础模型也表现不佳；而配备了GraphWalk工具的模型则能通过迭代探索和局部观察，显著提升在各种查询模板（从基础检索到复合一阶逻辑查询）上的性能，并且随着图谱规模增大，其优势更加明显。这证明了核心挑战在于推理步骤本身，而非检索质量，而基于导航的迭代探索能有效解决这一问题。

### Q4: 论文做了哪些实验？

论文进行了两类核心实验：迷宫遍历和合成知识图谱推理。实验设置上，作者为LLM配备了少量正交的图遍历工具（如获取相邻节点、按属性查找节点、获取邻居等），让模型通过序列化工具调用自主探索图结构，并与将全图信息直接输入上下文的基线方法进行对比。

在迷宫遍历实验中，使用10x10的网格迷宫，50%的单元格随机设置为墙，确保存在至少15步的有效路径。评估了gpt-4o-mini、gpt-4o、gpt-4.1系列及o3-mini、o4-mini共7个模型，每个模型在10个生成的迷宫实例上运行。关键指标为找到任意有效路径的准确率。结果显示，无工具访问的基线模型（全图在上下文中）表现极差，准确率接近0%（如gpt-4o-mini为0%，gpt-4o为10%）；而使用GraphWalk工具的模型则显著提升，例如gpt-4.1和gpt-4.1-mini达到了100%准确率，gpt-4o-mini达到80%。这证明了工具化导航在即使小图上也能解决模型固有的推理困难。

在合成知识图谱推理实验中，构建了完全随机、无语义标签的图谱以隔离世界知识干扰，评估了12种查询模板，涵盖检索、聚合、多跳遍历和一阶逻辑组合（如与、非操作）。图谱规模为最多100个节点（扩展实验达500节点），每个模型在10个不同随机图谱实例上运行所有12类查询（共120次）。对比方法同样为工具访问与无工具（全图上下文）两种配置。关键指标包括准确率（A）、精确率（P）、召回率（R）、F1分数及工具调用次数（TC）。主要结果显示，工具访问 consistently 带来性能提升：例如gpt-4.1在使用工具后准确率从17.50%提升至29.17%，F1从0.48提升至0.43；gpt-4o-mini的准确率从5.00%提升至15.00%。性能增益随模型规模增大而更明显，且无工具基线在图谱规模增大时性能崩溃，而GraphWalk方法能通过迭代探索保持推理能力。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，可以进一步探索的点包括：首先，模型在复杂逻辑查询（如“组合交集”和“带连接的否定”）上表现不佳，这表明LLMs在同时处理多重逻辑约束（AND/NOT）时存在固有局限。未来可研究如何通过增强工具链（如引入逻辑推理专用工具）或改进提示工程来提升此类任务的性能。其次，模型在“可变跳数路径”查询上完全失败，突显了LLMs在复杂查询规划方面的能力不足；未来可探索分层规划机制或与外部符号推理器结合，以支持更长的推理链。此外，论文指出工具辅助模型存在“最后一英里”问题，即模型能正确推理但无法遵循输出格式要求，这提示需要进一步优化指令遵循能力，例如通过强化学习或更精细的输出约束。最后，GraphWalk的通用性虽高，但未涉及动态图或实时更新场景；未来可探索在流式图数据上的应用，并研究工具集如何适应图结构的动态变化。从更广视角看，将GraphWalk与检索增强生成（RAG）结合，可能进一步提升其在超大规模知识图谱上的可扩展性。

### Q6: 总结一下论文的主要内容

GraphWalk 提出了一种无需训练、与问题无关的工具型框架，旨在解决大型语言模型在应对大规模知识图谱复杂查询时的局限性。传统方法依赖提示技术或检索增强生成，但受限于上下文窗口大小，难以处理企业级图谱。该框架的核心贡献是为通用LLM配备一组最小且正交的图遍历操作工具，使其能通过顺序导航进行多跳推理，从而将任务分解为可验证的步骤链。方法上，GraphWalk不依赖领域特定工具，而是通过工具调用组合实现结构化推理，并在合成图谱上评估以隔离世界知识影响。实验表明，该框架在迷宫遍历和模拟真实图谱的问答任务中显著提升了模型性能，尤其在大规模场景下优于上下文基线，并使非推理模型能达到更大推理模型的水平。此外，它提供了透明的执行轨迹，增强了决策可解释性，但也面临循环或长链处理等挑战，为未来改进指明了方向。
