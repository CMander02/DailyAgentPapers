---
title: "Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective"
authors:
  - "Noppanat Wadlom"
  - "Junyi Shen"
  - "Yao Lu"
date: "2026-03-17"
arxiv_id: "2603.16104"
arxiv_url: "https://arxiv.org/abs/2603.16104"
pdf_url: "https://arxiv.org/pdf/2603.16104v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.DB"
tags:
  - "Agent Serving Systems"
  - "Workflow Optimization"
  - "Query Optimization"
  - "Caching"
  - "LLM Inference Efficiency"
  - "Multi-Agent Systems"
relevance_score: 8.5
---

# Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective

## 原始摘要

Agentic workflows are composed of sequences of interdependent Large Language Model (LLM) calls, and they have become a dominant workload in modern AI systems. These workflows exhibit extensive redundancy from overlapping prompts and intermediate results due to speculative and parallel exploration. Existing LLM serving systems, such as vLLM, focus on optimizing individual inference calls and overlook cross-call dependencies, leading to significant inefficiencies. This paper rethinks LLM and agent serving from a data systems perspective and introduces Helium, a workflow-aware serving framework that models agentic workloads as query plans and treats LLM invocations as first-class operators. Helium integrates proactive caching and cache-aware scheduling to maximize reuse across prompts, KV states, and workflows. Through these techniques, Helium bridges classic query optimization principles with LLM serving, achieving up to 1.56x speedup over state-of-the-art agent serving systems on various workloads. Our results demonstrate that end-to-end optimization across workflows is essential for scalable and efficient LLM-based agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体（Agent）工作流在现有服务系统中运行效率低下的核心问题。研究背景是，智能体工作流已成为现代AI系统中的主流负载，它由一系列相互依赖的LLM调用组成，通过推测性和并行探索来执行复杂任务。然而，这种工作流在运行过程中，由于重叠的提示词和中间结果，会产生大量的冗余计算。

现有方法的不足主要体现在当前主流的LLM服务系统（如vLLM）上。这些系统主要专注于优化单次LLM推理调用，采用了连续批处理等技术来提升GPU利用率。但它们的工作粒度局限于单个LLM调用，缺乏对整个工作流结构的全局视角，无法识别和利用跨调用之间的依赖关系与共享机会（如共享的提示词前缀、KV缓存状态或中间结果）。因此，当处理包含多个LLM调用、具有复杂依赖关系的批处理式智能体工作流时，这些系统无法进行端到端的优化，导致显著的性能低下和资源浪费。

本文要解决的核心问题，是如何从数据系统的视角，对智能体工作流进行端到端的全局优化，以消除冗余、提升服务效率。具体而言，论文试图将智能体工作流建模为数据库中的查询计划，将LLM调用视为一等公民的操作符，从而引入经典的查询优化原则。论文提出的Helium系统，通过设计工作流感知的服务框架、主动缓存策略以及缓存感知的调度算法，来最大化跨提示词、KV状态和工作流的复用，最终实现比现有先进系统最高达1.56倍的性能加速。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：方法类（LLM服务优化）与应用类（工作流编排）。

在**方法类（LLM服务优化）**方面，以vLLM为代表的研究专注于优化单个LLM推理调用。它们通过PagedAttention高效管理KV缓存，并采用连续批处理和前缀缓存等技术来提升GPU利用率和吞吐量。然而，这类系统是“工作流无关”的，其优化局限于独立的请求层面，无法感知或利用跨调用之间的依赖关系和冗余，例如无法保证同一工作流内相关查询的KV缓存复用。

在**应用类（工作流编排）**方面，以LangGraph或Spark（将LLM视为UDF）为代表的框架，专注于编排复杂的多步骤智能体工作流逻辑。它们提供了构建工作流的高级抽象，但将LLM调用视为黑盒单元。这种设计导致编排层对LLM内部的关键性能因素（如状态化的KV缓存、预填充/解码的双模成本结构）一无所知，因而无法做出基于成本的智能优化决策。

本文提出的Helium系统与上述工作的核心区别在于，它从**数据系统视角**重新思考了LLM服务。它没有孤立地看待单个LLM调用或仅进行黑盒编排，而是将智能体工作流建模为查询计划，并将LLM调用视为一等操作符。通过引入**主动缓存**和**缓存感知调度**，Helium能够跨提示、KV状态和工作流最大化复用，从而将经典的查询优化原则与LLM服务相结合，实现了对工作流的端到端优化，弥补了现有方法在跨调用优化方面的空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Helium的工作流感知服务框架来解决现有LLM服务系统在代理工作流中存在的冗余和低效问题。其核心方法是从数据系统的视角重新审视LLM服务，将代理工作流建模为查询计划，并将LLM调用视为一等操作符，从而进行端到端的优化。

整体架构采用经典的多阶段查询处理流程，分为解析、优化和执行三个阶段。系统使用一种领域特定语言（DSL）来表示批量的代理工作流，解析器将其转换为有向无环图（DAG），其中每个操作符对应一个提示相关的动作（如调用模型、检索数据）。该设计借鉴了TensorFlow的数据流表示，但支持跨操作符的连续批处理，使得就绪的输出可以无阻塞地转发给下一个操作符。

主要模块与关键技术包括：
1.  **查询优化器**：负责识别和消除冗余。它首先进行初始计划修剪，包括操作符剪枝（移除对最终输出无贡献的操作，类似于死代码消除）和公共子图消除（CSE），合并结构相同且输入相同的子图。随后，优化器利用一个全局提示缓存进行逻辑计划优化。该缓存映射确定性操作符的输入到其输出。通过自底向上遍历DAG，为每个操作符计算签名并查询缓存。若命中，则将该操作符替换为一个轻量级的`CacheFetch`操作符，将计算依赖转换为数据检索依赖，从而绕过昂贵的LLM计算。此机制仅限于确定性操作符（如非LLM操作符或采用贪婪采样的LLM操作符）以保证结果不变性。

2.  **查询处理器**：负责高效执行优化后的计划。其核心创新是引入了**模板化基数树（Templated Radix Tree, TRT）** 这一数据结构。TRT在标准基数树基础上扩展，用于建模整个工作流中操作符输入提示的前缀结构（包括静态组件和来自其他操作符输出的动态部分）以及叶子节点（对应LLM操作符）之间的依赖关系。TRT能够全局捕获前缀层次结构和依赖关系，为主动缓存和调度提供基础。

3.  **主动缓存管理**：系统利用TRT识别跨批次不变的静态提示前缀。在首次执行工作流时，预计算这些前缀的KV状态并存储在GPU内存中。后续批次中，LLM引擎可直接复用这些预计算的KV张量，避免重复的预填充计算。同时，全局主动提示缓存存储确定性操作符的完整输出，使得系统能为重复输入绕过整个操作符的执行。

4.  **缓存感知调度**：为了解决因依赖关系导致的次优KV缓存复用问题，系统将调度问题形式化为一个以最小化总令牌步数（类似于完工时间）为目标的多工作者调度问题。调度器考虑每个LLM调用的令牌使用量（受前缀共享影响而减少）以及为捕捉批处理效果而设定的前序延迟约束。系统采用一种基于成本的贪婪算法，该算法在操作符级别的TRT上运行（而非LLM调用级别），以工作流结构而非批量大小决定复杂度。算法生成一个包含嵌套序列的软调度，允许运行时根据系统动态进行调整，并通过将共享静态前缀的操作符分组到内部序列中，最大化跨不同级别提示共享的缓存复用。

创新点在于：1）将数据库查询优化原则（如公共子表达式消除、缓存替换）系统性地引入LLM服务领域；2）提出TRT来统一建模工作流的提示前缀结构和操作依赖；3）设计了结合主动KV缓存和缓存感知调度的端到端优化框架，实现了跨提示、KV状态和工作流的复用最大化。

### Q4: 论文做了哪些实验？

论文的实验部分围绕四个研究问题展开，评估了Helium框架在编排智能体工作流时的性能与效率。

**实验设置与数据集**：实验使用了五个基础工作流模式：Map-Reduce、Multi-Agent Debate、Multi-Agent Reflection、Iterative Refinement和Parallel Chains。这些工作流在三个数据集上运行：MMLU（用于MapRed和Debate）、TAT-QA（用于MapRed、Debate和Reflect）以及Amazon Reviews（用于Iterative和Parallel）。具体配置例如，MapRed在MMLU上使用14个专家，在TAT-QA上使用7个专家；Debate使用3个智能体进行2轮辩论。

**对比方法**：主要与先进的LLM服务系统和智能体工作流编排系统进行对比，包括vLLM（专注于单个推理调用优化的高性能服务系统）、以及论文中提及的其他智能体服务系统（如Cocktail，尽管提供的文本片段未完整列出所有基线）。

**主要结果与关键指标**：
1.  **端到端性能**：在多种工作流和数据集上，Helium相比最先进的智能体服务系统，实现了最高达**1.56倍的加速**（速度提升）。图表数据显示，在所有测试的基础工作流上，Helium的归一化端到端延迟均低于对比基线，表现更优。
2.  **消融与敏感性研究**：实验还通过消融研究分析了Helium关键组件（如主动缓存和缓存感知调度）对整体性能的贡献，并进行了敏感性研究以评估其在不同配置和工作负载约束下的表现。这些研究证实了跨工作流端到端优化的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的Helium系统虽在优化Agent工作流方面取得进展，但仍存在一些局限和可探索方向。首先，其缓存机制主要针对静态或可预测的提示重叠，对于高度动态、依赖实时上下文的工作流（如交互式Agent），缓存命中率可能下降，未来可研究自适应缓存策略，结合工作流执行路径的实时反馈动态调整缓存内容。其次，系统假设工作流结构相对固定，但实际应用中Agent可能涉及条件分支、循环等复杂逻辑，未来需探索更灵活的工作流建模方法，例如将LLM调用与数据流图更深度结合，支持运行时优化。此外，论文未充分考虑多租户场景下的资源隔离与公平性，在共享GPU集群中，跨工作流的缓存共享可能引发优先级冲突，需设计更精细的资源调度策略。最后，可结合LLM推理的稀疏性特点（如MoE模型），进一步优化KV状态的管理与复用，探索跨模型、跨任务的通用缓存表示，提升系统泛化能力。

### Q6: 总结一下论文的主要内容

该论文从数据系统的视角重新审视了LLM与智能体服务，针对当前LLM服务系统在处理智能体工作流时存在的冗余和低效问题，提出了名为Helium的工作流感知服务框架。核心问题是现有系统（如vLLM）仅优化单个推理调用，忽视了工作流中跨调用依赖和大量重复内容（如重叠提示词和中间结果）导致的效率低下。

论文将智能体工作流建模为查询计划，并将LLM调用视为一等操作符，从而将经典数据库查询优化原则引入LLM服务领域。Helium的核心方法包括：1）主动缓存机制，以复用提示、KV状态和工作流结果；2）缓存感知的调度策略，最大化跨工作流的重用。这些技术显著减少了冗余计算。

主要结论表明，Helium在多种工作负载上相比现有最优的智能体服务系统实现了最高1.56倍的加速。该研究的核心贡献在于论证了跨工作流的端到端优化对于实现可扩展、高效的基于LLM的智能体至关重要，为未来AI系统设计提供了新的数据系统视角和优化范式。
