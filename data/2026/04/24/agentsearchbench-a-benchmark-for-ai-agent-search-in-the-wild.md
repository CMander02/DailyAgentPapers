---
title: "AgentSearchBench: A Benchmark for AI Agent Search in the Wild"
authors:
  - "Bin Wu"
  - "Arastun Mammadli"
  - "Xiaoyu Zhang"
  - "Emine Yilmaz"
date: "2026-04-24"
arxiv_id: "2604.22436"
arxiv_url: "https://arxiv.org/abs/2604.22436"
pdf_url: "https://arxiv.org/pdf/2604.22436v1"
github_url: "https://github.com/Bingo-W/AgentSearchBench"
categories:
  - "cs.AI"
  - "cs.IR"
  - "cs.MA"
tags:
  - "Agent检索"
  - "Agent评测基准"
  - "Agent能力评估"
  - "信息检索"
  - "多智能体系统"
relevance_score: 8.0
---

# AgentSearchBench: A Benchmark for AI Agent Search in the Wild

## 原始摘要

The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at https://github.com/Bingo-W/AgentSearchBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI agent生态系统中如何有效搜索和选择合适agent的问题。当前，AI agent的能力具有组合性和执行依赖性，仅凭文本描述难以准确评估其真实能力，而现有的工具检索和agent选择研究通常假设功能明确、候选池可控，且主要面向可执行查询，忽略了现实世界中agent种类繁多、功能重叠、以及用户常从高层次非执行性描述开始搜索的场景。因此，现有方法存在语义相似性与实际执行性能之间不一致的“语义-表现鸿沟”。本文的核心问题是：在开放、真实的agent生态中，如何基于执行验证的性能信号（而非仅凭文本匹配）来有效检索和排序agent，以弥合这一鸿沟。为此，作者提出了AgentSearchBench，一个包含近万个真实agent的大规模基准，形式化了可执行与高层次任务描述下的检索与重排序问题，并利用执行结果定义相关性，旨在填补现有研究在真实场景下agent搜索评估的空白。

### Q2: 有哪些相关研究？

相关工作可分为三类。**方法类**方面，现有研究关注智能体系统设计与编排（如多智能体协作框架）及工具检索与选择（如基于文本描述或结构模式检索），但这些工作通常假设候选池有限且功能明确，或仅面向可执行任务查询。AgentSearchBench则聚焦于开放生态中高层面任务描述下的智能体搜索，并引入执行感知信号弥补文本相似度的不足。**应用类**方面，已有工作优化工具表示（如模式统一或执行信号），但主要针对工具使用而非大规模发现。本文则直接构建了含近万个真实智能体的搜索基准。**评测类**方面，传统信息检索和排序学习假设相关性静态可观察，不适用于依赖执行表现的智能体。本文将其扩展为执行驱动的排序问题，并通过实验揭示语义相似度与实际性能的普遍差距，验证了执行信号（如感知探测）对排序质量的提升作用。

### Q3: 论文如何解决这个问题？

本文通过构建一个大规模现实世界Agent搜索基准AgentSearchBench来解决Agent搜索问题，核心创新在于将搜索形式化为检索与重排序任务，并使用执行驱动的相关性评估信号。整体框架包含三个主要模块：首先是近10,000个真实Agent的候选库构建，从GPT Store、Google Cloud Marketplace等公开平台采集而成，引入现实世界的能力重叠与文档不一致性挑战。其次是分层任务生成流水线：先基于Agent文档合成可执行任务查询（包括单Agent和多Agent复合任务），再通过语义聚类和LLM生成高层任务描述，并利用基于视角的评判器为每个描述关联10个可执行查询。最后是执行驱动的相关性评估模块，针对任务查询使用LLM-as-judge进行5分制评估，对高层描述则聚合其关联查询的执行表现，同时引入文档—性能对齐折扣机制，对成功执行但无文档支持的Agent赋予0.5相关性权重。关键技术包括混合检索（BM25+BGE+ToolRet加权组合）用于候选筛选、自然语言推理验证多Agent任务组合合理性、以及基于子任务完成度的分级相关性标签。基准测试对比了4类检索模型（稀疏、稠密、工具感知、解码器仅编码）和4类重排序模型（交叉编码器、工具排序器、解码器重排序器、LLM排序器），实验揭示语义相似度与实际执行性能之间存在持续差距，而工具感知检索器（ToolRet）在任务查询上表现最优，但所有方法在高阶任务描述上的完整性（Completeness）指标均显著偏低，表明文档匹配无法准确捕捉执行效能。

### Q4: 论文做了哪些实验？

论文构建了名为AgentSearchBench的大规模基准测试，包含近10,000个来自多个提供商的真实世界AI Agent。实验将Agent搜索形式化为检索和重排序问题，在两类查询上进行评估：可执行的任务查询（T_q）和高层任务描述（T_d）。评估指标包括NDCG、Precision、Recall和Completeness，相关性基于执行结果生成。

检索实验比较了四类模型：稀疏（BM25, SPLADE v2）、稠密（ColBERT v2, BGE-Large v1.5等）、工具感知（Tool-Embed, ToolRet等）、解码器仅（E5-Mistral 7B, Qwen-Embedding 8B）。在任务查询上，工具感知模型ToolRet表现最佳（NDCG@5：37.52），优于稠密模型BGE-Large v1.5（31.78）；在任务描述上，稠密模型BGE-Large v1.5最强（NDCG@5：23.08）。重排序实验比较了交叉编码器（BGE Reranker v2）、工具特定排序器（Tool-Rank 8B）、解码器仅重排序器（Qwen Reranker 4B）、基于LLM的排序器（RankGPT GPT-5.2）。在任务查询上，Tool-Rank 8B表现最好（NDCG@5：64.36）；在任务描述上，RankGPT GPT-5.2最优（NDCG@5：64.66）。然而，所有方法的Completeness指标均较低，表明基于语义的匹配与实际执行性能之间存在显著差距。

### Q5: 有什么可以进一步探索的点？

该基准测试存在几个关键局限和可探索方向。首先，当前所有检索与重排序方法在Executable Task Query和Task Description下的Completeness指标均极低，表明纯文本匹配无法完全捕捉Agent的执行能力。未来可探索将执行感知信号（如轻量级执行探查）直接融入检索与重排序模型，而非仅作为后处理信号。其次，论文主要评估了基于静态描述的检索，忽略了Agent功能的动态演化特性。可研究在线学习机制，让Agent搜索系统能根据用户反馈和执行结果持续更新Agent表示。最后，该基准测试仅包含近万个Agent，且均来自公开提供商。未来可构建更大规模、包含更复杂组合任务和私有Agent的生态，并探索如何利用大语言模型的推理能力，在执行前进行更精确的Agent能力推断与匹配，以弥合语义与执行性能之间的鸿沟。

### Q6: 总结一下论文的主要内容

AgentSearchBench提出并形式化了一个新问题：在开放生态系统中基于执行依赖性的AI Agent搜索。现有研究假设功能可从文本描述推断，忽视了Agent能力的组合性和执行依赖性。该基准从多个平台收集近10,000个真实Agent，将搜索定义为可执行查询和高级任务描述下的检索与重排序问题，并使用执行结果作为相关性评判标准。实验揭示了文本相似度与实际性能之间存在一致差距，证明了基于描述的检索方法存在局限。进一步研究表明，轻量级的执行感知探测信号能显著提升排序质量，为构建更可靠的Agent发现机制提供了关键方向。
