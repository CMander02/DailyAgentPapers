---
title: "Agentic DAG-Orchestrated Planner Framework for Multi-Modal, Multi-Hop Question Answering in Hybrid Data Lakes"
authors:
  - "Kirushikesh D B"
  - "Manish Kesarwani"
  - "Nishtha Madaan"
  - "Sameep Mehta"
  - "Aldrin Dennis"
  - "Siddarth Ajay"
  - "Rakesh B R"
  - "Renu Rajagopal"
  - "Sudheesh Kairali"
date: "2026-03-15"
arxiv_id: "2603.14229"
arxiv_url: "https://arxiv.org/abs/2603.14229"
pdf_url: "https://arxiv.org/pdf/2603.14229v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Multi-Hop Reasoning"
  - "Agent Framework"
  - "Tool Use"
  - "Query Planning"
  - "Multi-Modal QA"
  - "Data Lake"
  - "Execution Orchestration"
  - "Caching"
relevance_score: 7.5
---

# Agentic DAG-Orchestrated Planner Framework for Multi-Modal, Multi-Hop Question Answering in Hybrid Data Lakes

## 原始摘要

Enterprises increasingly need natural language (NL) question answering over hybrid data lakes that combine structured tables and unstructured documents. Current deployed solutions, including RAG-based systems, typically rely on brute-force retrieval from each store and post-hoc merging. Such approaches are inefficient and leaky, and more critically, they lack explicit support for multi-hop reasoning, where a query is decomposed into successive steps (hops) that may traverse back and forth between structured and unstructured sources. We present Agentic DAG-Orchestrated Transformer (A.DOT) Planner, a framework for multi-modal, multi-hop question answering, that compiles user NL queries into directed acyclic graph (DAG) execution plans spanning both structured and unstructured stores. The system decomposes queries into parallelizable sub-queries, incorporates schema-aware reasoning, and applies both structural and semantic validation before execution. The execution engine adheres to the generated DAG plan to coordinate concurrent retrieval across heterogeneous sources, route intermediate outputs to dependent sub-queries, and merge final results in strict accordance with the plan's logical dependencies. Advanced caching mechanisms, incorporating paraphrase-aware template matching, enable the system to detect equivalent queries and reuse prior DAG execution plans for rapid re-execution, while the DataOps System addresses validation feedback or execution errors. The proposed framework not only improves accuracy and latency, but also produces explicit evidence trails, enabling verification of retrieved content, tracing of data lineage, and fostering user trust in the system's outputs. On benchmark dataset, A.DOT achieves 14.8% absolute gain in correctness and 10.7% in completeness over baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业环境中，针对混合数据湖（即同时包含结构化表格和非结构化文档的数据存储）进行自然语言问答时，面临的效率低下、推理能力不足以及结果可追溯性差等核心问题。

研究背景是，企业越来越多地使用混合数据湖来整合结构化记录（如数据库表）和非结构化文档（如文本、合同），并期望通过自然语言直接查询这些异构数据源，而无需掌握SQL等专业查询语言。然而，现有的主流解决方案，包括基于检索增强生成（RAG）的系统，通常采用一种“蛮力”方法：将用户查询同时、独立地提交给结构化（如通过NL2SQL）和非结构化（如向量检索）存储进行检索，然后对结果进行事后合并。这种方法存在显著不足：首先，它高度依赖NL2SQL等模型的精确生成，容易产生幻觉且效率低下；其次，为了确保召回率，常常会过度检索大量无关数据，导致计算开销大、数据泄露风险高；最关键的是，它缺乏对**多跳推理**的显式支持。多跳推理要求将一个复杂查询分解为多个连续的步骤（“跳”），这些步骤可能需要在结构化和非结构化数据源之间来回穿梭和关联信息，而现有方法难以有效规划和执行这种跨模态的、有依赖关系的推理链条。

因此，本文要解决的核心问题是：如何设计一个统一的框架，能够将用户的自然语言查询**编译成明确的、可并行执行的执行计划**，以支持高效、准确、可追溯的**跨模态多跳问答**。具体而言，该框架需要克服现有方法在规划、执行、优化和可验证性方面的缺陷，实现查询的智能分解、依赖关系管理、并行化执行、中间结果的精准传递，并提供完整的证据链以供审计和验证。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，首先是**多模态问答与检索增强生成（RAG）系统**。现有部署方案通常对结构化（如SQL数据库）和非结构化（如向量库）数据源进行独立的暴力检索和事后合并，效率低且缺乏对跨模态多跳推理的显式支持。本文提出的A.DOT框架通过编译为有向无环图（DAG）执行计划，实现了跨模态的定向检索和中间结果路由，从根本上区别于这种后融合范式。其次是**面向表格的模型与文本到SQL系统**，如TaBERT、TAPAS和RAT-SQL等。这些工作主要专注于单一模态（表格）的问答，通常生成抽取式答案，而A.DOT则处理在结构化表格和非结构化文档间反复交替的多跳查询。第三是**智能体推理框架**，例如ReAct，它交错进行推理和工具调用，但以顺序方式执行子任务，导致延迟较高。A.DOT通过DAG实现子查询的并行执行，优化了延迟。第四是**基于DAG的规划器**，如LLM-Compiler，它们能编译依赖图，但常将结构化中间结果替换为原始文本传递，当下游步骤仅需结果子集时效率低下。A.DOT引入了变量绑定机制，在节点间选择性地传递精确数据元素，提升了效率。

在应用类研究中，**多跳问答基准**如HybridQA和MMQA，凸显了跨异构数据源进行联合推理的需求和挑战，本文的工作正是在此背景下，为这类复杂场景提供了一个统一的解决方案框架。

综上，本文与现有工作的核心区别在于，它首次在一个统一框架中，集成了并行执行、计划缓存、变量作用域数据传递和证据可追溯性，专门解决了在混合数据湖中反复跨模态的多跳推理问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Agentic DAG-Orchestrated Transformer (A.DOT) Planner的框架来解决混合数据湖中多模态、多跳问答的复杂问题。其核心思想是将用户的自然语言查询编译成一个跨越结构化和非结构化数据存储的有向无环图执行计划，从而显式地支持需要在不同数据源间进行多步推理的查询。

整体框架包含五个主要模块。**计划生成器**负责在单次大语言模型调用中，将输入查询分解为一系列原子性子查询，并组织成一个DAG。每个节点代表一个可从单一数据源回答的子任务，并标注了目标数据源、存储输出的符号变量等元数据。节点间的依赖边协调了跨模态的信息流，允许独立节点并行执行。**计划验证器**则在执行前对生成的DAG计划进行双重校验：结构检查确保计划符合数据模式、变量有效且无循环依赖；语义检查则利用大语言模型审计，确保计划与原始查询意图一致，防止语义漂移。**计划执行器**按照DAG的拓扑顺序协调执行，它维护一个变量存储来绑定中间结果。为应对中间结果可能过大的挑战，执行器采用了“变量精简”策略，仅向下游节点传递必要的键值，从而高效管理内存和上下文限制。对于不同数据源，它调用相应的子代理进行查询。**DataOps系统**是一个反馈驱动的修复模块，当验证或执行失败时被激活。它包含诊断、推荐、修复和重规划四个子模块，能够根据错误类型提供建议、应用局部修复或触发完整的计划重写，实现渐进式精炼。**计划缓存**模块则通过精确匹配、基于模板的匹配和语义匹配三种策略，复用已验证的DAG计划，以加速对重复或转述查询的处理。

该框架的创新点在于：1）**显式的DAG规划**：将多跳推理过程显式化为可执行的、可并行化的DAG，取代了传统的暴力检索与事后合并。2）**验证与修复闭环**：通过结构/语义双重验证和模块化的DataOps系统，在昂贵执行前拦截错误并支持反馈驱动的自动修复，提升了鲁棒性。3）**高效的执行协调**：通过变量绑定与精简机制，在保证逻辑依赖的同时，优化了跨异构数据源并发检索和中间结果路由的效率。4）**可验证的证据链**：整个执行过程记录详细的数据溯源信息，生成明确的证据轨迹，增强了结果的可解释性和用户信任。这些设计共同作用，在基准测试中实现了准确性和完整性的显著提升。

### Q4: 论文做了哪些实验？

论文在 HybridQA 数据集上进行了实验，这是一个要求跨结构化表格和非结构化文本进行多跳推理的基准测试。实验将数据集重构为双存储架构：结构化数据存储在关系型 SQL 后端（SQLDB），非结构化文本段落被分块并嵌入到 Milvus 向量数据库中，两者通过 document_id 建立连接以支持跨模态检索。整个 A.DOT 流水线由 LLaMA-3 70B 模型驱动，并使用 LangGraph 框架实现。

评估指标采用 Unitxt 库的 NL 中心指标：答案正确性（由 Mistral Large 2 作为评判模型进行二元判断）和答案完整性（由同一模型在“极差”到“优秀”的等级上评分）。对比方法包括：1) 标准 RAG，使用相同的两个检索器进行单次检索与生成；2) ReAct 框架，提供相同工具并允许交替推理与工具调用（最多 20 步）；3) LLM Compiler 框架，同样提供工具并生成可并行执行的 DAG 计划。

主要结果显示，A.DOT 在答案正确性和完整性上均显著优于所有基线。具体数据为：A.DOT 的正确性为 71.0%，完整性为 73.0%；而最强的基线标准 RAG 分别为 56.2% 和 62.3%。这意味着 A.DOT 相比标准 RAG 在正确性上绝对提升了 14.8%，在完整性上绝对提升了 10.7%。其他基线如 ReAct 和 LLM Compiler 的表现则更弱。

此外，论文还进行了消融实验，在 500 个样本的子集上评估了计划验证器（Schema Validator）和 DataOps 系统的影响。结果显示，同时移除两者时，正确性降至 67.9%；仅移除 DataOps 系统时，正确性大幅下降至 60.0%；而完整的 A.DOT 系统取得了最佳性能（正确性 71.8%，完整性 74.3%），验证了验证与重新规划组件协同工作的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的A.DOT框架在混合数据湖的多跳问答上取得了显著进展，但仍存在一些局限性和值得探索的方向。首先，系统目前主要针对单轮查询，未来可扩展至多轮对话场景，这需要解决上下文历史管理和用户意图消歧等挑战。其次，框架的模态支持虽可扩展，但实际集成图像、图谱等非文本数据时，跨模态对齐与联合推理机制仍需深入设计。此外，当前的缓存与复用机制基于语义模板匹配，对于复杂多变的自然语言表达，其泛化能力可能有限，可探索引入更精细的语义相似度度量或增量学习策略。从系统优化角度看，DAG执行计划的动态调整能力、资源约束下的自适应并行调度，以及错误恢复的自动化程度，都有进一步提升空间。最后，该框架在更开放领域或动态更新数据环境中的鲁棒性、以及计算开销与精度之间的平衡，也是未来值得关注的研究点。

### Q6: 总结一下论文的主要内容

该论文提出了A.DOT框架，旨在解决企业在混合数据湖（结合结构化表格和非结构化文档）上进行多模态、多跳自然语言问答的挑战。针对现有RAG等方案检索效率低、缺乏显式多跳推理支持的问题，其核心贡献是设计了一个基于有向无环图（DAG）的智能体规划器。该方法将用户查询编译为可并行执行的DAG计划，通过查询分解、模式感知推理以及结构/语义验证来确保准确性。执行引擎依据DAG协调异构源的并发检索，路由中间结果，并严格按逻辑依赖合并最终答案。系统还集成了高级缓存机制（如基于释义的模板匹配）以重用等效查询计划，并通过DataOps系统处理验证反馈或执行错误。实验表明，在基准数据集上，A.DOT在正确性和完整性上分别比基线显著提升14.8%和10.7%。该框架不仅提升了性能与延迟，还提供了显式的证据追溯链，增强了结果的可验证性与用户信任，为企业级混合数据问答提供了模块化、可扩展的解决方案。
