---
title: "Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki"
authors:
  - "Haoliang Ming"
  - "Feifei Li"
  - "Xiaoqing Wu"
  - "Wenhui Que"
date: "2026-05-25"
arxiv_id: "2605.25480"
arxiv_url: "https://arxiv.org/abs/2605.25480"
pdf_url: "https://arxiv.org/pdf/2605.25480v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Agent-native retrieval"
  - "Retrieval-Augmented Generation"
  - "Self-evolving knowledge structure"
  - "Multi-hop reasoning"
  - "Tool-using agent"
relevance_score: 9.5
---

# Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki

## 原始摘要

LLM agents require retrieval to behave less like one-shot context fetching and more like reasoning: searching, reading, traversing, and deciding when evidence is sufficient. However, Retrieval-Augmented Generation (RAG) typically organizes external knowledge as flat chunks retrieved by embedding similarity, exposing a retrieval-as-lookup interface that is poorly aligned with tool-using agents. We propose LLM-Wiki, an agent-native retrieval system that operationalizes the Retrieval-as-Reasoning paradigm by treating external knowledge as a compilable, composable, and self-evolving structure rather than a static retrieval index. LLM-Wiki compiles documents into structured Wiki pages with bidirectional links, exposes search, read, and link-following operations through standard tool-calling interfaces, and introduces an Error Book for persistent structural and semantic self-correction. On HotpotQA, MuSiQue, and 2WikiMultiHopQA, LLM-Wiki outperforms seven baselines, including HippoRAG 2, LightRAG, and GraphRAG, with gains of 2.0-8.1 F1 points over the strongest graph-based baseline and larger gains over Dense RAG. On AuthTrace, LLM-Wiki achieves the best overall accuracy, with especially strong gains on multi-document structured queries, showing that compilation-based knowledge organization generalizes beyond chain-style multi-hop reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前检索增强生成（RAG）系统在智能体环境中存在的主要问题。研究背景是，LLM智能体在复杂多跳推理任务中（例如比较两部电影的导演年龄）需要的检索行为应更像推理过程：包括搜索、阅读、遍历信息以及判断证据是否充分。然而，现有RAG方法采用“检索即查找”模式，将外部知识组织为扁平化文本块，单纯依赖向量相似度进行一次性检索。这种组织方式存在三个根本不足：首先，扁平块将检索降级为匹配而非推理，难以处理需要跨文档追踪关系、比较属性或聚合证据的任务；其次，检索是单次黑箱操作，智能体无法根据中间观察结果调整检索策略；最后，结构化知识库缺乏自我纠错机制，无法修复构建过程中产生的死链接、事实矛盾等错误。

本文提出“检索即推理”新范式，并通过LLM-Wiki系统将其具体化。核心问题是：如何将外部知识组织从静态索引转变为可编译、可组合且能自我进化的结构化形式，使智能体能够像推理一样进行检索，即通过工具调用来实现搜索、阅读、链接遍历以及证据充分性检查，并利用持续的错误簿机制实现知识库的结构与语义自愈。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

1. **检索增强生成（RAG）与层次检索方法**：包括DPR、IRCoT、Self-RAG、RAPTOR、MemWalker等。这些方法通过密集检索或摘要树组织知识，但缺乏显式的链接结构供智能体规划组合遍历路径。本文提出的LLM-Wiki通过双向链接的维基页面结构，弥补了这一不足。

2. **图增强RAG与知识编译方法**：如GraphRAG、HippoRAG、LightRAG等。它们利用实体、关系或图索引增强检索，但输出通常为摘要、三元组或向量化结构，而非人类可读且可遍历的页面。LLM-Wiki则编译文档为显式链接的维基页面，实现更直观的交互。

3. **LLM自我修正与基于智能体的检索**：Reflexion、Self-Refine、Self-RAG等方法在单次推理或查询时进行自我修正，而LLM-Wiki的Error Book通过约束积累与修复实现跨批次的持续性结构语义纠错。此外，LLM-Wiki将LLM Wiki范式具体化为可组合、可编译的知识存储系统，并通过工具调用接口支持搜索、读取和链接追踪操作。

### Q3: 论文如何解决这个问题？

LLM-Wiki将检索重新定义为一种推理性过程，其核心方法是对原始文档进行编译，转化为具有双向链接的结构化Wiki知识库，并让智能体像推理一样组合使用搜索、阅读和链接追踪等原子化操作。整体框架分为索引时的构建阶段和查询时的遍历阶段。在构建阶段，主要组件包括结构化Wiki页面（包含目录索引、Markdown页面和源档案）以及错误簿。Wiki页面通过元数据、别名、标签、事实和双向Wiki链接实现结构化，支持智能体概览和导航。错误簿是核心创新之一，能够持续检测并修复编译错误。它遵循五阶段生命周期：发现错误、归因根因、生成约束规则、将规则注入后续编译提示、并定期验证关闭。这实现了知识结构的自我进化和持续纠错。在查询阶段，LLM-Wiki通过两个工具接口实现组合式检索：wiki_search和wiki_read。智能体根据查询特征自适应选择遍历策略：直接访问已知实体、通过页面间链接进行桥梁式查询（A→B→答案）、或通过目录进行探索性浏览。每次读取后，智能体都会评估证据是否充分，直到推理链完成或达到预算限制。最后，论文还设计了两层修复机制：代码层自动修复结构性错误，LLM层定期修复语义和内容一致性错误，并通过多轮交叉修复确保Wiki达到稳定状态。这些设计将传统RAG的一次性查找转变为智能体主动推理和动态遍历的检索过程。

### Q4: 论文做了哪些实验？

论文在三个多跳问答基准（HotpotQA、MuSiQue、2WikiMultiHopQA，各500题）和一个结构化知识基准（AuthTrace，含8种查询类型）上评估了LLM-Wiki。实验设置采用GLM-5.1作为统一LLM，Qwen3-Embedding-8B用于嵌入，对比了七种基线方法：无检索、BM25 RAG、密集RAG、RAPTOR、GraphRAG、LightRAG和HippoRAG 2。主要指标为F1和EM（多跳QA）以及GPT-4o评判的准确率（AuthTrace）。在多跳QA上，LLM-Wiki在所有数据集上取得最优结果：HotpotQA上F1为0.839（超LightRAG 2.0点），MuSiQue上为0.739（超LightRAG 8.1点），2WikiMultiHopQA上为0.911（超LightRAG 6.4点）。在AuthTrace上，LLM-Wiki总体准确率为70.4%（超HippoRAG 2 2.1点），在高多文档查询上优势显著（55.4% vs 46.5%）。消融实验证明，Wiki结构、渐进遍历和Error Book三个组件均至关重要，移除后F1分别下降6.1-7.0、11.7-13.8和3.4-4.0点。细粒度分析显示，LLM-Wiki在需要深层推理的查询上（如4跳问题F1达0.983）和组合型问题上增益最大（超密集RAG 15.6 F1点）。效率方面，LLM-Wiki与BM25/密集RAG相当，快于LightRAG等图基方法。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于编译成本和可扩展性：初始构建Wiki页面需要额外的LLM调用，且当前目录索引在数万页规模下可能退化，缺乏对动态更新和跨模态内容的支持。未来研究方向包括：1）优化编译效率，例如采用增量式页面更新机制或分级索引结构，将构建开销分摊到更多查询，或通过自适应页面选择策略减少冗余计算；2）引入动态维护机制，针对频繁变化的数据源设计陈旧事实检测和自动重编译模块，并探索图分片和层次化目录以支撑Web级语料库；3）拓展模态覆盖，将多模态信息（如图表、表格）嵌入Wiki结构，使链接推理能跨图文节点进行；4）研究跨语料库迁移能力，评估预编译的Wiki结构能否在领域间复用。此外，可尝试将Error Book的自我纠错机制与强化学习结合，让代理在检索过程中动态调整页面组织策略，使结构演化更贴合下游任务分布。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为LLM-Wiki的智能体原生检索系统，旨在解决传统检索增强生成（RAG）将外部知识组织为扁平块并通过嵌入相似性进行检索、与工具使用型智能体不匹配的问题。该系统将外部知识视为可编译、可组合、可自我进化的结构，而非静态索引。方法上，LLM-Wiki将文档编译成带双向链接的结构化Wiki页面，通过标准工具调用接口暴露搜索、阅读和链接跟踪操作，并引入错误簿实现结构和语义的持续自我修正。在HotpotQA、MuSiQue、2WikiMultiHopQA和AuthTrace数据集上，LLM-Wiki优于HippoRAG 2、LightRAG和GraphRAG等七种基线模型，F1分数提升2.0-8.1点。核心贡献在于提出了检索即推理范式，表明编译结构化知识、智能体组合遍历和自我修正机制能有效提升知识密集型问答性能，特别是在多文档结构查询中优势明显。
