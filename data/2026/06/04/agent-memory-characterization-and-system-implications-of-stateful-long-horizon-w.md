---
title: "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads"
authors:
  - "Yasmine Omri"
  - "Ziyu Gan"
  - "Zachary Broveak"
  - "Robin Geens"
  - "Zexue He"
  - "Alex Pentland"
  - "Marian Verhelst"
  - "Tsachy Weissman"
  - "Thierry Tambe"
date: "2026-06-04"
arxiv_id: "2606.06448"
arxiv_url: "https://arxiv.org/abs/2606.06448"
pdf_url: "https://arxiv.org/pdf/2606.06448v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Memory"
  - "系统表征"
  - "长时任务"
  - "内存系统"
relevance_score: 9.0
---

# Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

## 原始摘要

LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characterization of agent memory. First, we introduce a system-oriented taxonomy classifying agent memory systems along four axes. Second, we build a phase-aware profiling harness attributing cost to construction, retrieval, and generation. Third, we characterize ten representative systems across two benchmark suites, uncovering how design choices shift cost across the write and read paths. Finally, we derive 10 system recommendations covering construction scheduling, capability floors, amortization via query volume, freshness-latency tradeoffs, and fleet-scale management.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长时域LLM代理（agent）在持续交互过程中面临的系统级内存管理与扩展问题。随着代理被部署于需要跨会话进行持久推理和状态维护的任务（如个人助理、代码代理、深度研究代理等），其累积的交互状态远超单次推理的上下文窗口容量。现有方法如单纯依赖长上下文窗口存在三个根本局限：首先是固定上下文预算无法容纳无限增长的会话历史；其次，窗口预填充成本随历史长度呈二次方增长，且跨会话的KV缓存因缓存驱逐和内存压力而失效；最后，长序列中模型的推理和召回保真度显著下降，形成“U形”性能曲线。虽然检索增强生成（RAG）将知识从模型参数中解耦，但传统RAG依赖静态语料库，而代理内存需要处理由自身交互流产生的、可被追加、总结、合并、链接或重写的可变状态。因此，核心问题在于：如何设计系统化的内存机制，以可控的成本实现跨会话持久化存储、选择性检索和增量更新，同时避免因现有设计选择（如压缩为原子事实或构建图结构内存）所引入的、精度指标无法反映的显著系统开销（如LLM预填充量激增、嵌入流量和存储膨胀）。本文旨在于首次对代理内存算法进行系统性研究，揭示不同设计范式（构造、存储、检索、可变性）下的关键权衡及其对部署基础设施（如计算、带宽、延迟、可扩展性）的系统级影响。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类。首先是长上下文记忆（Paradigm I），代表系统long_context直接将交互历史作为提示词，无外部存储，本文指出其随会话增长成本急剧增加。其次是扁平RAG记忆（Paradigm II），如BM25和embedRAG，采用确定性索引，构建过程无大模型介入，操作上接近经典RAG，但语料来自交互流。第三类是结构增强型RAG记忆，分为追加构建（III.a，如GraphRAG、HippoRAG v2）和整合构建（III.b，如Mem0、SimpleMem），区别在于是否定期合并或更新记忆记录，其写路径引入大模型作为固定提取器。第四类是智能体控制流记忆（Paradigm IV），如A-Mem、Letta和MIRIX，将记忆操作（读写）暴露给大模型作为决策工具，使读写路径变为可变深度的控制流。本文与此类工作的核心区别是，现有研究聚焦于设计新的记忆系统以提升任务性能，而本文首次从系统工程角度，对各系统的工作负载进行了量化特征分析与成本归因，揭示了设计选择如何影响读写路径的开销，并推导出系统优化建议。

### Q3: 论文如何解决这个问题？

该论文通过系统性的方法对Agent记忆工作负载进行了表征和分析。核心方法包括四个层面:首先,提出一个面向系统的四维分类法,将Agent记忆系统分为不同范式;其次,构建阶段感知的性能分析工具,将成本分解为构建、检索和生成三个环节;第三,对10个代表性系统在两个基准套件上进行特征化分析;最后,推导出10条系统设计建议。

整体框架围绕"构建-服务-准确性"三角进行权衡分析。主要模块包括:构建阶段的成本分析(包括墙钟时间、能量消耗和调用次数),检索阶段的延迟分析,以及生成阶段的准确性评估。关键技术包括:通过长上下文提示与外部记忆系统的对比实验,量化不同记忆系统的每查询服务延迟;通过能量效率度量(每正确回答消耗的焦耳数)评估系统效率;以及通过构建LLM规模敏感性分析确定成本杠杆的可用范围。

创新点主要体现在:首次从系统角度对Agent记忆进行特征化表征,揭示了不同设计选择在读写路径上的成本分布差异;提出了构建成本作为不可隐藏成本的观点,并将其与查询时延进行联合评估;发现了构建过程是预填充密集型和嵌入密集型工作负载,与延迟敏感的QA服务存在结构性冲突;以及证明了构建-服务-准确性三者无法同时最优化的性能前沿关系。

### Q4: 论文做了哪些实验？

论文使用MemoryAgentBench(MAB)和MemoryArena两个基准测试套件进行实验。MAB包含准确检索、测试时学习、长程理解和选择性遗忘四类任务，使用LongMemEval_S_*作为核心工作负载（5个样本，约360K token历史，60个查询）。MemoryArena用于评估多会话任务中的时效性-延迟权衡。

实验比较了10个代表性系统，包括Letta、SimpleMem、A-Mem、Mem0等。设置两个构建模式：远程构建使用OpenAI模型（GPT-4o-mini等），本地构建使用Qwen3系列模型（32B/14B/8B/1.7B）在单块H100 GPU上运行。检索限制为10个条目，使用4096-token分块流式输入。

主要结果揭示设计选择如何在写入和读取路径上转移成本。关键发现包括：本地模型在小模型中成本更低、时效性-延迟权衡是核心系统特性、构造调度策略显著影响性能。系统特性通过API遥测（token量、延迟）和硬件遥测（GPU利用率90%+、内存带宽、能耗）进行量化分析。

### Q5: 有什么可以进一步探索的点？

论文在系统表征上非常全面，但仍有几个值得深入探索的方向。首先，当前研究主要基于静态数据集和离线评估，未来需要研究在**持续交互、动态演化**的长周期工作负载下，内存系统的**版本管理、一致性模型、以及冷热数据分层**策略。其次，论文揭示了构造与查询之间的成本权衡，但未深入探讨**自适应调度策略**——例如，能否根据查询的实时紧急程度或历史访问模式，动态决定是走全量精准检索还是近似快速检索，甚至跳过构造直接回退到长上下文。第三，能量效率分析虽引入了“每正确回答能耗”指标，但未来可进一步研究**异构计算和模型级联**的潜力，例如为不同复杂度的内存操作（如简单检索 vs. 关系推理）动态分配不同规模的嵌入或LLM模型。最后，论文对**联邦式或分布式多智能体**场景下共享内存的读写冲突、网络开销与去中心化索引构建问题着墨较少，这是走向大规模部署的关键挑战。

### Q6: 总结一下论文的主要内容

本论文首次系统性地研究了LLM智能体记忆的系统特性。问题定义在于长周期任务中，智能体需要跨会话持久存储、检索和更新自身记忆，而现有系统设计差异巨大但缺乏系统级分析。方法上，作者提出了一个面向系统的四维分类法（构建、存储、检索、可变性），并构建了相位感知分析工具，将成本归因于构建、检索和生成三个阶段，对十个代表性系统在两个基准套件上进行了表征。核心结论包括：不同设计选择会导致写入和读取路径的成本分布发生显著变化；记忆工作负载对部署基础设施提出了超越传统LLM服务的新需求。论文贡献在于提出了包含系统分类、分析工具、全面表征和十条系统建议的完整研究框架，为设计可扩展的状态化智能体系统提供了重要的工程指导和理论基础，填补了该领域系统级理解的空白。
