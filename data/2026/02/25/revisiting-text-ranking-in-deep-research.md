---
title: "Revisiting Text Ranking in Deep Research"
authors:
  - "Chuan Meng"
  - "Litu Ou"
  - "Sean MacAvaney"
  - "Jeff Dalton"
date: "2026-02-25"
arxiv_id: "2602.21456"
arxiv_url: "https://arxiv.org/abs/2602.21456"
pdf_url: "https://arxiv.org/pdf/2602.21456v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent评测/基准"
  - "信息检索"
  - "工具使用"
  - "Agent架构"
  - "LLM应用于Agent场景"
relevance_score: 7.5
---

# Revisiting Text Ranking in Deep Research

## 原始摘要

Deep research has emerged as an important task that aims to address hard queries through extensive open-web exploration. To tackle it, most prior work equips large language model (LLM)-based agents with opaque web search APIs, enabling agents to iteratively issue search queries, retrieve external evidence, and reason over it. Despite search's essential role in deep research, black-box web search APIs hinder systematic analysis of search components, leaving the behaviour of established text ranking methods in deep research largely unclear. To fill this gap, we reproduce a selection of key findings and best practices for IR text ranking methods in the deep research setting. In particular, we examine their effectiveness from three perspectives: (i) retrieval units (documents vs. passages), (ii) pipeline configurations (different retrievers, re-rankers, and re-ranking depths), and (iii) query characteristics (the mismatch between agent-issued queries and the training queries of text rankers). We perform experiments on BrowseComp-Plus, a deep research dataset with a fixed corpus, evaluating 2 open-source agents, 5 retrievers, and 3 re-rankers across diverse setups. We find that agent-issued queries typically follow web-search-style syntax (e.g., quoted exact matches), favouring lexical, learned sparse, and multi-vector retrievers; passage-level units are more efficient under limited context windows, and avoid the difficulties of document length normalisation in lexical retrieval; re-ranking is highly effective; translating agent-issued queries into natural-language questions significantly bridges the query mismatch.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究场景中文本排序方法的性能评估与优化问题。研究背景是，深度研究作为一种新兴任务，需要通过多轮网络探索来回答复杂、多跳的推理密集型查询。现有方法通常依赖基于大语言模型的智能体调用不透明的网络搜索API进行迭代检索和推理，但由于搜索组件是黑盒，导致难以系统分析不同文本排序方法在深度研究中的实际表现。现有研究的不足主要体现在三个方面：一是多数工作采用文档级检索单元，容易因上下文窗口限制而截断文档，造成信息丢失，且忽略了段落级单元的优势；二是对重排序在深度研究中的作用缺乏系统评估，尤其是当内容消费者是智能体而非人类时；三是智能体发出的查询往往具有网络搜索风格（如带引号的关键词），与现有神经排序器训练时使用的自然语言问题不匹配，这种查询格式失配的影响尚未被充分探索。

本文的核心问题是：在深度研究设定下，如何系统评估并提升文本排序方法的有效性？具体而言，论文通过三个研究问题展开：探究段落级与文档级检索单元的效果差异；评估不同检索器、重排序器及重排序深度配置下的性能；分析智能体查询与训练查询之间的失配对神经排序方法的影响，并提出缓解方法。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度研究任务中的信息检索方法展开，可分为以下几类：

**方法类**：包括传统的文本排序方法，如基于词法的稀疏检索（如BM25）、学习型稀疏检索（如SPLADE-v3）、单向量稠密检索（如RepLLaMA、Qwen3-Embed）以及多向量稠密检索（如ColBERTv2）。这些方法在传统检索任务中已有广泛研究，但本文重点探讨它们在深度研究场景中的适用性。与这些工作相比，本文系统评估了这些方法在深度研究中的表现，特别关注了检索单元（文档vs.段落）、查询特性（智能体生成的查询与训练查询的差异）等因素的影响。

**应用类**：涉及基于大语言模型（LLM）的智能体在深度研究中的应用。先前研究通常依赖不透明的网络搜索API，智能体通过多轮推理和搜索获取外部证据。本文与这些工作的区别在于，它使用固定文档库和人工标注的相关性判断，避免了黑盒API的干扰，从而能系统分析搜索组件的贡献。

**评测类**：包括对深度研究数据集的构建和评估。本文基于BrowseComp-Plus数据集进行实验，该数据集提供了固定的文档库和相关性标注。与先前仅评估少数检索器的工作不同，本文扩展了评估范围，涵盖了多种检索器和重排序器，并首次构建了段落级语料库以支持更细致的分析。

**重排序方法**：本文还涉及重排序技术的研究，如monoT5-3B、RankLLaMA-7B和Rank1-7B等。与以往工作相比，本文系统探讨了重排序在深度研究中的有效性，包括不同初始检索器、重排序类型和深度的影响，并发现重排序能显著提升性能。

总体而言，本文通过重现和扩展现有文本排序方法，填补了深度研究中检索单元、重排序配置和查询不匹配等方面的研究空白，提供了更全面的实证分析。

### Q3: 论文如何解决这个问题？

论文通过系统性的实验设计和分析，从三个核心研究问题出发，深入探究了深度研究场景中文本排序方法的行为与有效性。其核心方法是**在固定的深度研究数据集（BrowseComp-Plus）和可控的语料库上，对多种检索器、重排序器及其组合配置进行大规模复现与对比实验**，以揭示不同因素对性能的影响。

**整体框架与主要模块**：
1.  **实验主体**：研究基于两个开源LLM智能体（gpt-oss-20b和GLM-4.7-Flash）和BrowseComp-Plus数据集展开。该数据集提供了文档级语料和人工标注的相关性判断。
2.  **核心组件**：
    *   **检索单元**：对比**文档级**与**段落级**检索。论文从原始文档语料构建了段落语料库，并评估了三种设置：检索截断文档、检索文档但配备完整文档阅读工具、以及直接检索和阅读段落。
    *   **检索器**：涵盖了信息检索的四大主流范式，包括词汇稀疏检索器（BM25）、学习型稀疏检索器（SPLADE-v3）、单向量稠密检索器（RepLLaMA, Qwen3-Embed-8B）和多向量稠密检索器（ColBERTv2）。
    *   **重排序器**：选取了代表不同效率-效果权衡的模型，包括非推理型（monoT5-3B, RankLLaMA-7B）和基于推理链的模型（Rank1-7B）。
    *   **查询转换模块**：提出了**查询转问题（Q2Q）方法**，使用LLM将智能体发出的网络搜索式查询，翻译成更自然的、类似于MS MARCO训练数据的问题形式，以缓解查询不匹配问题。

**关键技术方法与创新点**：
1.  **多维度系统性评估**：论文的创新在于没有提出新的排序模型，而是**首次在深度研究这一特定、复杂的任务背景下，对现有文本排序技术的最佳实践进行了系统性的复现与剖析**。它通过三个研究问题，分别从检索单元粒度、排序流水线配置（不同检索器、重排序器及重排序深度）、以及查询特性（训练与部署时的查询不匹配）这三个关键维度进行了全面评估。
2.  **揭示关键发现**：实验得出了几个重要结论，构成了方法上的核心洞见：
    *   智能体发出的查询多具网络搜索语法特征（如精确匹配引号），这使得**词汇检索器、学习型稀疏检索器和多向量检索器表现更佳**。
    *   在有限的上下文窗口下，**段落级检索单元比文档级更高效**，避免了文档长度归一化等问题。
    *   **重排序阶段非常有效**，能显著提升检索结果质量。
    *   **查询不匹配问题确实存在且影响显著**，而提出的**Q2Q转换方法能有效桥接这一鸿沟**，将搜索查询转化为自然语言问题，从而提升了神经排序器的性能。
3.  **严谨的实验设计**：方法上确保了可比性与可复现性。例如，在评估段落检索时，采用Max-P策略将段落得分映射回文档以利用文档级标注；在智能体设置上统一了最大输出长度和迭代次数；对所有排序方法使用了公开可用的实现和标准配置。

总之，论文通过构建一个可控、可分析的实验平台，采用“复现-对比-分析”的方法论，清晰地揭示了不同文本排序组件在深度研究智能体工作流中的实际效果与相互作用，为未来优化此类系统的检索模块提供了实证依据和具体指导。

### Q4: 论文做了哪些实验？

本论文在深度研究（Deep Research）场景下，对信息检索（IR）文本排序方法进行了系统性实验。实验设置主要围绕三个核心视角展开：(i) 检索单元（文档 vs. 段落），(ii) 流水线配置（不同检索器、重排序器及重排序深度），(iii) 查询特性（智能体发出的查询与文本排序器训练查询之间的不匹配问题）。

**实验设置与数据集**：实验在BrowseComp-Plus数据集上进行，这是一个具有固定文档集的深度研究基准。研究评估了2个开源智能体（gpt-oss-20b和GLM-4.7-Flash）、5种检索器（包括BM25、SPLADE-v3、ColBERT-v2、RepLLaMA、Qwen3-Embed-8B）以及3种重排序器在不同配置下的表现。实验对比了文档级和段落级检索单元，并测试了是否启用完整文档阅读器（full-document reader）工具。

**主要结果与关键指标**：
1.  **检索单元**：段落级检索在有限上下文窗口下更高效，能带来更高的答案准确率。例如，使用SPLADE-v3时，gpt-oss-20b在段落上的准确率为0.516，相比文档（0.476）有8.4%的相对提升。
2.  **检索器对比**：词法检索器BM25在段落语料上表现极具竞争力，gpt-oss-20b搭配BM25获得了最高的召回率（0.616）和答案准确率（0.572）。相比之下，单向量稠密检索器（如RepLLaMA、Qwen3-Embed-8B）尽管模型规模大，但性能持续落后于基于BERT的学习稀疏检索器（SPLADE-v3）和多向量稠密检索器（ColBERT-v2）。
3.  **查询特性**：智能体发出的查询具有网络搜索风格（含关键词、短语和引号），这更利于BM25等词法检索器。将这类查询翻译成自然语言问题能显著弥合查询不匹配。
4.  **重排序与文档阅读器**：重排序被证明非常有效。在文档语料上启用完整文档阅读器虽然减少了搜索调用和召回，但通过补偿文档截断造成的信息损失，提高了答案准确率（例如，gpt-oss-20b使用SPLADE-v3时准确率从0.476提升至0.529）。
5.  **BM25在文档上的问题**：BM25在文档语料上表现不佳，主要归因于其对文档长度归一化敏感。通过网格搜索调整其参数（\(k_1\)和\(b\)）或对文档进行截断索引，可以缓解此问题。

### Q5: 有什么可以进一步探索的点？

该论文揭示了在深度研究任务中，现有文本排序方法的行为特征，但仍存在一些局限性和可进一步探索的方向。首先，实验基于固定的静态语料库（BrowseComp-Plus），未能充分模拟开放网络动态、实时且规模不断扩大的信息环境，未来研究需在更真实的开放网络设置下验证排序方法的泛化能力。其次，研究主要关注传统检索与重排序模块，尚未深入探索如何将检索过程与LLM的推理能力更紧密地结合，例如开发检索感知的推理机制或让LLM动态指导检索策略的调整。此外，论文发现将智能体发出的查询转化为自然语言问题能有效缓解查询不匹配，但这仅是一个初步方案，未来可研究更高级的查询理解与重写技术，例如利用LLM根据对话历史和多轮交互动态优化查询。最后，评估维度可进一步扩展，除检索效果外，还需综合考虑计算效率、延迟以及智能体最终决策质量等端到端指标，以推动更实用、高效的深度研究系统发展。

### Q6: 总结一下论文的主要内容

该论文聚焦于深度研究任务中的文本排序问题，旨在通过系统实验揭示传统信息检索方法在此新兴场景下的表现。核心贡献在于填补了现有研究空白：以往基于大语言模型的智能体通常依赖不透明的网络搜索API，导致检索组件的行为难以分析；本文则在固定语料库的深度研究数据集BrowseComp-Plus上，复现并评估了多种文本排序方法的关键发现与最佳实践。

研究从三个维度系统考察了检索效果：检索单元（文档与段落）、流水线配置（不同检索器、重排序器及重排序深度）以及查询特性（智能体生成的查询与文本排序器训练查询之间的不匹配）。实验涉及2个开源智能体、5种检索器和3种重排序器。主要结论包括：智能体发出的查询多遵循网络搜索语法（如精确匹配引号），因此更适配词法检索、学习型稀疏检索和多向量检索；在上下文窗口有限时，段落级检索更高效，且能避免词法检索中文档长度归一化的难题；重排序技术效果显著；将智能体查询转化为自然语言问题能有效缓解查询不匹配问题。这些发现为优化深度研究系统中的检索模块提供了实证依据与实用指导。
