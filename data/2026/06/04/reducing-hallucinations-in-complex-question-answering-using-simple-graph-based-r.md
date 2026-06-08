---
title: "Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)"
authors:
  - "Christopher J. Wedge"
  - "Joshua Stutter"
  - "Danny Dixon"
  - "Jacek Cała"
date: "2026-06-04"
arxiv_id: "2606.05901"
arxiv_url: "https://arxiv.org/abs/2606.05901"
pdf_url: "https://arxiv.org/pdf/2606.05901v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "RAG"
  - "Graph-based RAG"
  - "Hallucination Mitigation"
  - "Complex QA"
  - "Agentic System"
  - "Tool Use"
  - "Wikipedia QA Benchmark"
relevance_score: 7.5
---

# Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)

## 原始摘要

Large language models (LLMs) have fundamentally transformed the landscape of Natural Language Processing. Despite these advances, LLMs and LLM-based systems remain prone to a variety of failure modes. Retrieval-augmented generation (RAG) systems have emerged as a common deployment scenario seeking to both avoid the well known risk of the LLM "hallucinating" information, and to enable reasoning and question answering over proprietary information that the LLM did not have access to during training without resorting to expensive model fine-tuning.
  In this work, we explore the idea of using a lightweight graph structure with a relatively simple graph schema, to support the RAG subsystem via a dedicated toolset. We design an agentic system with a variety of vector search and graph query tools operating over a structured dataset based on a curated subset of English Wikipedia articles, and evaluate its performance on questions from MoNaCo, a challenging Wikipedia QA benchmark of complex query answering tasks.
  Our results show that the introduction of graph-based tools can significantly increase the precision and recall of factual correctness, can halve the number of hallucinated answers, and achieves the highest fine-grained truthfulness score among the three evaluated scenarios. All this with a modest increase in token usage.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

大型语言模型（LLM）在自然语言处理领域取得了突破性进展，但依然存在幻觉、信息遗漏等关键失败模式。检索增强生成（RAG）系统通过引入外部知识库来缓解幻觉，并支持对私有知识的推理。然而，传统基于向量检索的RAG在处理需要多跳、跨文档、多实体推理的复杂问答（如“列出英荷战争中所有战役及胜者”）时效果不佳，因为这类问题需要从分散的多源文档中获取、聚合和推理知识。现有图增强RAG方法（如GraphRAG）虽能改进检索，但构建复杂知识图谱难度大、上下文窗口占用高，而简单结构又可能无法充分捕获知识。

本文针对上述不足，提出一种基于轻量级图结构的检索增强生成方法。其核心是构建一个结构简单（仅包含文档标题、章节标题和段落及其链接）的图知识库，并设计统一工具集（基于Neo4j和Cypher查询语言）支持高效图遍历。研究旨在回答：对结构化知识库的查询（KBQA）是否比非结构化向量RAG能更有效提升复杂问答性能。通过对比零样本、纯向量RAG和所提向量+图RAG方法在MoNaCo基准上的表现，发现图工具能显著提高事实正确性的精确率和召回率，将幻觉答案数量减半，并获得最高的细粒度真实性得分，且仅带来适度的token使用量增加。

### Q2: 有哪些相关研究？

相关研究主要集中在检索增强生成（RAG）和知识图谱增强的问答系统两个方向。在RAG方面，Lewis等人提出的经典RAG框架通过检索外部文档来减少幻觉，本文在此基础上引入结构化图查询工具，与传统纯向量检索的RAG形成对比。在知识图谱增强方面，GraphRAG等研究利用知识图谱结构进行推理，本文的不同之处在于采用轻量级图模式（仅含实体和关系两类节点），避免复杂图谱构建的开销。

方法类工作包括：基于向量相似度的密集检索方法（如DPR）、基于知识图谱的问答推理（如KGQA）。本文将这些方法融合为Agentic系统，通过工具调用实现协同推理。评测类工作包括MoNaCo、HotpotQA等复杂问答基准，本文重点在MoNaCo上验证图结构工具的效果。

本文创新点在于：1）提出简单图模式而非复杂知识图谱；2）设计专用图查询工具集与向量搜索配合；3）在不过度增加token消耗的前提下，显著降低幻觉率（减少50%），同时提升事实性精度和召回率。与现有工作相比，更强调轻量化实现和可部署性。

### Q3: 论文如何解决这个问题？

该论文提出了一种基于轻量级图结构的检索增强生成(RAG)系统来解决复杂问答中的幻觉问题。核心方法是构建一个混合检索架构，将传统向量检索与图数据库查询相结合，通过一个智能体系统来协调多种工具的使用。

系统架构包含三个主要组件：推理代理、工具集和知识库。推理代理使用Langchain的create_agent函数创建，配备了三类工具：基于向量的检索工具（包括标题向量搜索和文本块向量搜索）、基于图的查询工具（包括文章邻域探索、结构导航、关系查询等）以及一个基本计算工具。知识库基于2025年8月的英语维基百科快照构建，经过数据对齐实验筛选出1207个MoNaCo问题所需的相关文章。

关键技术包括：图模式设计将文章、章节、段落和文本块组织为层次化结构，通过HAS_SECTION、HAS_PARAGRAPH、HAS_CHUNK等关系连接，并使用NEXT_*/PREVIOUS_*关系实现双向链表。此外，文章间通过MENTIONS和REDIRECTS_TO关系连接，段落通过LINKS_TO指向其他文章。为降低嵌入成本，选择Microsoft Harrier 0.6B模型（仅0.6B参数）处理超过3亿token的数据集，在检索性能与效率间取得平衡。

创新点在于：1) 使用预定义的Cypher查询而非让LLM自主生成，避免提示注入风险并减少LLM认知负担；2) 通过图结构实现多跳推理，无需像传统方法那样分解为多个独立步骤；3) 提供最短路径、反向链接等关系查询工具，使智能体能够同时探索多个关系跳数，大幅减少LLM调用次数。实验表明该方法使幻觉答案减半，事实正确性的精确率和召回率显著提升。

### Q4: 论文做了哪些实验？

论文基于MoNaCo基准测试集进行实验，该数据集包含复杂问答任务，来源于精选英文维基百科子集。实验设置了三种场景：纯向量检索RAG系统、向量检索+图数据库（KG）混合RAG系统，以及仅使用图查询的KG-RAG系统。主要采用两类评价指标：一是RAGAS框架中的事实正确性（Factual Correctness）分数，通过LLM将生成答案和参考答案分解为独立主张后计算精确率、召回率和F1值；二是CRAG分数，将答案分类为准确（+1）、缺失（0）或幻觉（-1）。未使用忠实度（Faithfulness）和上下文精确率/召回率，因MoNaCo无预定义的上下文块支撑复杂推理。

结果显示，引入图工具后，事实正确性的精确率和召回率显著提升，幻觉答案数量减半，CRAG分数中的最高细粒度真实度得分（Truthfulness Score）在三组场景中最佳。代价是token使用量适度增加。

### Q5: 有什么可以进一步探索的点？

该论文提出的基于简单图结构增强检索生成方法在减少幻觉方面效果显著，但仍存在几个可深入探索的方向。首先，当前方法仅针对Wikipedia结构化数据，对非结构化或混合数据场景的泛化性尚未验证，未来可探索将非结构化文本自动转换为图结构的方法。其次，系统依赖预定义的手写查询工具，限制了处理新型查询的灵活性，可以引入动态查询生成机制，让LLM基于问题自动构建图查询。再者，论文主要评估了端到端性能，未深入分析不同工具选择策略对结果的影响，可设计更智能的主动学习机制让系统自适应选择检索工具。最后，当前图结构较为简单，未来可研究更复杂的多层次图结构（如主题/实体/文档层级），或结合时序信息支持动态知识更新。此外，将图检索与向量检索的混合策略，以及如何减少图构建的计算开销，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

本论文针对大语言模型在复杂问答任务中容易产生幻觉的问题，提出了一种基于轻量级图结构的检索增强生成方法。该方法通过构建简单的图模式（文档标题、章节标题和段落链接），使用Neo4j图数据库和Cypher查询语言实现了向量搜索与图查询相结合的工具集。在MoNaCo基准测试上的实验结果表明，相比传统的向量RAG和零样本方法，图增强RAG显著提升了事实正确性的精确率和召回率，将幻觉回答数量减半，并获得了最高的细粒度真实性分数，同时仅带来适度的token使用增长。这项研究展示了在检索增强生成中结合简单图结构可以有效减少复杂问答中的幻觉问题，为在实际应用中部署轻量级知识图谱提供了实用方向。
