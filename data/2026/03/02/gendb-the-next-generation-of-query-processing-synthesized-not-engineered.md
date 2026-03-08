---
title: "GenDB: The Next Generation of Query Processing -- Synthesized, Not Engineered"
authors:
  - "Jiale Lao"
  - "Immanuel Trummer"
date: "2026-03-02"
arxiv_id: "2603.02081"
arxiv_url: "https://arxiv.org/abs/2603.02081"
pdf_url: "https://arxiv.org/pdf/2603.02081v1"
categories:
  - "cs.DB"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Code & Software Engineering"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Tool Use & API Interaction"
  domain: "Data Science & Analytics"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "Claude Code Agent"
  key_technique: "GenDB (LLM-powered agentic system for synthesizing instance-optimized query execution code)"
  primary_benchmark: "TPC-H, a new benchmark to reduce LLM training data leakage"
---

# GenDB: The Next Generation of Query Processing -- Synthesized, Not Engineered

## 原始摘要

Traditional query processing relies on engines that are carefully optimized and engineered by many experts. However, new techniques and user requirements evolve rapidly, and existing systems often cannot keep pace. At the same time, these systems are difficult to extend due to their internal complexity, and developing new systems requires substantial engineering effort and cost. In this paper, we argue that recent advances in Large Language Models (LLMs) are starting to shape the next generation of query processing systems.
  We propose using LLMs to synthesize execution code for each incoming query, instead of continuously building, extending, and maintaining complex query processing engines. As a proof of concept, we present GenDB, an LLM-powered agentic system that generates instance-optimized and customized query execution code tailored to specific data, workloads, and hardware resources.
  We implemented an early prototype of GenDB that uses Claude Code Agent as the underlying component in the multi-agent system, and we evaluate it on OLAP workloads. We use queries from the well-known TPC-H benchmark and also construct a new benchmark designed to reduce potential data leakage from LLM training data. We compare GenDB with state-of-the-art query engines, including DuckDB, Umbra, MonetDB, ClickHouse, and PostgreSQL. GenDB achieves significantly better performance than these systems. Finally, we discuss the current limitations of GenDB and outline future extensions and related research challenges.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统数据库查询处理系统在面对快速演进的技术和用户需求时所面临的僵化与扩展性难题。研究背景是，尽管现有数据库管理系统（如PostgreSQL）经过精心设计和优化，但其架构往往针对特定负载（如OLTP）而固化，难以高效适应新兴需求，如OLAP分析、实时时序数据处理、向量相似性搜索或多模态查询等。现有方法主要依赖两种途径：一是对原有系统进行扩展，但这常因系统内部复杂性导致兼容性问题与高昂维护成本；二是从头开发专用系统，但这需要巨大的工程投入与资金成本。这两种方式均无法灵活、快速地响应持续变化的技术环境。

本文的核心问题是：能否摆脱“持续构建、扩展和维护复杂查询引擎”的传统范式，转而利用大语言模型（LLM）的能力，为每个查询动态合成定制化的执行代码？论文提出，通过LLM生成针对具体数据、工作负载和硬件资源进行实例优化的代码，可以实现前所未有的查询优化空间和极致的可扩展性。为此，作者设计了GenDB作为概念验证，它是一个基于LLM的多智能体系统，能够根据输入的模式、查询、数据及资源配置，自动分析工作负载、设计存储布局、生成资源感知的执行计划并输出可执行代码。这种方法特别适合重复性查询占主导的场景（如企业定期分析任务），其前期代码生成成本可通过多次执行分摊，从而显著提升性能。论文通过TPC-H和新构建的基准测试表明，GenDB在OLAP负载上优于DuckDB、ClickHouse等多个先进查询引擎，展现了其潜力。同时，作者也指出了当前在代码正确性验证等方面的限制，并展望了未来研究方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：编译式查询代码生成、大语言模型增强的代码生成，以及大语言模型增强的数据库系统。

在**编译式查询代码生成**方面，相关工作如HIQUE和LegoBase通过使用预定义的代码模板或高级语言编译器，为每个查询生成定制化的执行代码，旨在减少函数调用、提升硬件利用率。然而，这些方法依赖于人工设计的模板和编译器优化，生成过程固定，无法感知数据特性、负载模式或硬件属性，定制能力有限。GenDB同样追求为每个查询生成定制代码，但关键区别在于利用LLM进行代码合成，从而能够生成更灵活、实例优化且适应特定数据、负载和硬件的代码，突破了模板和编译器的限制。

在**大语言模型增强的代码生成**方面，CodexDB和GenesisDB利用LLM（如GPT-3 Codex）将执行计划中的操作符转换为自然语言描述，进而生成Python代码。它们提供了一定的定制选项（如选择数据处理库），但主要面向特定评估场景，并未系统性地以性能优化为目标。ADRS则专注于在现有系统中用AI生成的算法替换部分人工算法。GenDB与这些工作的关系在于都利用LLM生成代码，但GenDB的目标更为根本：它旨在用合成的执行代码完全替代传统的查询处理引擎，实现端到端的性能优化，而非仅增强或替换现有系统的局部组件。

在**大语言模型增强的数据库系统**这一更广泛的范畴内，相关研究包括利用LLM进行数据库调优、查询重写、学习型查询优化等。GenDB属于这一趋势，但聚焦于核心的执行层革新——即用LLM合成的代码直接执行查询，而非仅辅助优化或提供自然语言接口。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GenDB的、由大型语言模型驱动的多智能体系统来解决传统查询处理系统难以快速适应新技术和用户需求的问题。其核心方法是摒弃持续构建、扩展和维护复杂查询引擎的传统路径，转而利用LLM为每个传入的查询即时合成高度定制化的执行代码。

**整体框架与主要模块**：GenDB是一个端到端的系统，它将复杂的查询处理与优化任务分解为一系列由专用LLM智能体处理的步骤。其架构包含以下关键模块：
1.  **工作负载分析器**：分析硬件资源、数据库模式、SQL查询和底层数据，生成结构化的负载特征（如存储类型、表列统计信息、连接模式），为下游优化决策提供指导。
2.  **存储/索引设计器**：设计并生成代码，将原始数据格式转换为优化的存储结构（如为OLAP负载使用带编码和压缩的列式存储）并构建相应的索引。
3.  **查询规划器**：基于工作负载分析及存储/索引设计，生成高效的执行计划。其物理算子实现是资源感知的，能根据硬件特性（如缓存层次结构）自适应选择策略。
4.  **代码生成器**：使用合适的编程语言（如高性能C++、AI操作Python）实现执行计划，并应用系统级优化（如编译器优化、操作系统函数）。
5.  **查询优化器**：利用执行反馈，迭代地优化执行计划和代码实现以提升性能。优化目标可由用户灵活定义。

**创新点与关键技术**：
*   **范式转变**：从“工程化”固定引擎转变为“合成”实例优化代码，从根本上应对了快速变化的技术和需求挑战。
*   **LLM驱动的多智能体架构**：每个智能体以LLM为核心推理组件，并配备文件操作、终端访问、网络搜索等工具，能够自主规划并调用工具完成复杂任务（如通过采样程序评估连接顺序）。
*   **高度定制化与实例优化**：所有生成的组件（存储结构、索引、每个查询的可执行文件）都针对特定的数据、工作负载和硬件资源进行量身定制，实现了传统“一刀切”引擎难以达到的深度优化。
*   **灵活的优化框架**：支持单目标（如热运行时间）优化，并计划扩展至约束优化和多目标优化，平衡性能与成本。
*   **验证与迭代**：通过与传统数据库结果对比验证正确性，并基于反馈进行迭代优化，直至达到用户配置的预算或目标。

通过这一架构，GenDB在实验中超越了包括DuckDB、ClickHouse在内的多个先进查询引擎，证明了其方法的有效性。

### Q4: 论文做了哪些实验？

论文的实验设置旨在评估GenDB系统相对于现有最先进查询引擎的性能。实验在配备双Intel Xeon Gold 5218 CPU（32物理核心）和384 GB内存的Ubuntu服务器上进行，确保数据完全缓存在内存中。GenDB的原型使用JavaScript实现，并采用Claude Sonnet 4.6作为底层LLM，生成的执行代码为C++。

使用的数据集和基准测试包括：(1) 经典的TPC-H基准测试（比例因子10），选取了五个代表性查询（Q1, Q3, Q6, Q9, Q18）进行详细分析；(2) 新构建的SEC-EDGAR基准测试，基于2022-2024年的真实财务数据（约5GB），旨在减少LLM训练数据泄露的影响，并通过SQLSmith生成了1000个随机查询后采样出六个查询进行评估。

对比的系统均为最新版本的主流查询引擎：DuckDB v1.4.4、ClickHouse v26.2.1、Umbra（2026年2月发布）、MonetDB v11.55.1和PostgreSQL v18.2。为确保公平，实验报告了两个版本：一是各系统仅使用其自动创建的索引（如主键索引或默认区域映射），二是这些索引再补充由GenDB生成的额外索引。

主要结果显示，GenDB在性能上显著优于所有基线系统。在TPC-H的五个查询上，GenDB总执行时间为214毫秒，比最快的两个基线DuckDB（594毫秒）和Umbra（590毫秒）快2.8倍，比ClickHouse快11.2倍。在SEC-EDGAR基准上，GenDB执行时间为328毫秒，比DuckDB快5.0倍，比Umbra快3.9倍。性能优势随查询复杂度增加而扩大，例如在TPC-H Q9（五表连接带LIKE过滤）上，GenDB仅用38毫秒，比DuckDB快6.1倍。

此外，论文通过消融实验分析了GenDB多智能体设计的效果。在TPC-H上，完整多智能体系统（236毫秒）比最佳单智能体变体（引导式，281毫秒）快1.2倍；在SEC-EDGAR上，优势扩大到2.3倍（多智能体328毫秒 vs. 引导式752毫秒）。移除领域特定提示会导致性能进一步下降，在SEC-EDGAR上产生1.8倍减速。多智能体设计还降低了成本，在TPC-H上为14.15美元，低于单智能体变体的17.54美元。

关键数据指标包括：TPC-H Q6在迭代0达到近最优时间17毫秒；Q18从初始12,147毫秒优化至74毫秒，提升163倍；SEC-EDGAR Q4从1,410毫秒优化至106毫秒，提升13.3倍。这些优化源于数据感知列编码、算法级重构、缓存自适应聚合和工作负载特定派生数据结构等定制化策略。

### Q5: 有什么可以进一步探索的点？

基于论文提出的GenDB框架，未来可以从以下几个方向深入探索：

**系统优化与成本控制**：当前系统在LLM调用上存在较高的token消耗和延迟成本。未来可研究动态模型选择策略，根据查询复杂度自适应分配不同规模的模型（如简单分析步骤使用轻量模型），并设计更精炼的提示模板。同时，探索生成可复用组件（如参数化算子、共享数据结构）以减少重复生成开销，实现跨查询优化。

**鲁棒性与知识集成**：系统需解决“静默失败”问题（如代码无限循环、输出超限），需开发自动检测与优雅降级机制。此外，尽管LLM已编码领域知识，但缺乏专有优化技术与实时知识。可构建外部知识库，融合最新研究成果与内部实践，并通过检索增强生成（RAG）提升代码生成的准确性与先进性。

**扩展性与新场景适配**：当前多智能体通信依赖结构化JSON，未来可评估TOON、MCP等高效通信协议以降低对齐偏差。系统可进一步扩展至语义查询处理（如多模态数据ML推理优化）及现代硬件（如生成GPU原生代码，集成libcudf等高性能库），并探索自进化机制，通过经验积累自动优化提示与系统设计。

**验证与性能深化**：需突破现有串行执行队列的吞吐瓶颈，支持高并发评估。同时，引入细粒度反馈（如算子级性能剖析）加速优化收敛，并研究对生成代码的形式化验证方法，提升可靠性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个颠覆性的数据库查询处理新范式GenDB，其核心思想是利用大语言模型（LLM）为每个查询即时合成执行代码，从而取代传统上需要大量专家精心设计和持续优化的固定查询引擎。论文指出，传统系统难以适应快速变化的技术和需求，且开发维护成本高昂。

GenDB作为一个多智能体系统，其核心方法是利用LLM（如Claude Code Agent）作为底层组件，根据具体的查询、数据特征、工作负载和硬件资源，动态生成实例优化和定制化的执行代码。这种方法跳过了通用引擎的构建，实现了“按需合成”。

论文通过TPC-H基准和新设计的防数据泄露基准进行实验评估，将GenDB原型与DuckDB、Umbra等多个先进查询引擎对比。结果表明，GenDB取得了显著优于这些传统系统的性能。这证明了LLM驱动、代码合成的路径在数据库查询处理领域的巨大潜力，为下一代系统设计指明了方向。论文最后也讨论了当前局限性和未来的研究挑战。
