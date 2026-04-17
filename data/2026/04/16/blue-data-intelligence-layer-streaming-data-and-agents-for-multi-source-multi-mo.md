---
title: "Blue Data Intelligence Layer: Streaming Data and Agents for Multi-source Multi-modal Data-Centric Applications"
authors:
  - "Moin Aminnaseri"
  - "Farima Fatahi Bayat"
  - "Nikita Bhutani"
  - "Jean-Flavien Bussotti"
  - "Kevin Chan"
  - "Rafael Li Chen"
  - "Yanlin Feng"
  - "Jackson Hassell"
  - "Estevam Hruschka"
  - "Eser Kandogan"
  - "Hannah Kim"
  - "James Levine"
  - "Seiji Maekawa"
  - "Jalal Mahmud"
  - "Kushan Mitra"
  - "Naoki Otani"
  - "Pouya Pezeshkpour"
  - "Nima Shahbazi"
  - "Chen Shen"
  - "Dan Zhang"
date: "2026-04-16"
arxiv_id: "2604.15233"
arxiv_url: "https://arxiv.org/abs/2604.15233"
pdf_url: "https://arxiv.org/pdf/2604.15233v1"
categories:
  - "cs.AI"
  - "cs.DB"
tags:
  - "Compound AI System"
  - "Multi-Agent Orchestration"
  - "Multi-Source Data Integration"
  - "Data-Centric AI"
  - "Query Planning"
  - "NL2SQL"
  - "Enterprise Agent"
relevance_score: 7.5
---

# Blue Data Intelligence Layer: Streaming Data and Agents for Multi-source Multi-modal Data-Centric Applications

## 原始摘要

NL2SQL systems aim to address the growing need for natural language interaction with data. However, real-world information rarely maps to a single SQL query because (1) users express queries iteratively (2) questions often span multiple data sources beyond the closed-world assumption of a single database, and (3) queries frequently rely on commonsense or external knowledge. Consequently, satisfying realistic data needs require integrating heterogeneous sources, modalities, and contextual data. In this paper, we present Blue's Data Intelligence Layer (DIL) designed to support multi-source, multi-modal, and data-centric applications. Blue is a compound AI system that orchestrates agents and data for enterprise settings. DIL serves as the data intelligence layer for agentic data processing, to bridge the semantic gap between user intent and available information by unifying structured enterprise data, world knowledge accessible through LLMs, and personal context obtained through interaction. At the core of DIL is a data registry that stores metadata for diverse data sources and modalities to enable both native and natural language queries. DIL treats LLMs, the Web, and the User as source 'databases', each with their own query interface, elevating them to first-class data sources. DIL relies on data planners to transform user queries into executable query plans. These plans are declarative abstractions that unify relational operators with other operators spanning multiple modalities. DIL planners support decomposition of complex requests into subqueries, retrieval from diverse sources, and finally reasoning and integration to produce final results. We demonstrate DIL through two interactive scenarios in which user queries dynamically trigger multi-source retrieval, cross-modal reasoning, and result synthesis, illustrating how compound AI systems can move beyond single database NL2SQL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统自然语言转SQL（NL2SQL）系统在应对现实世界复杂数据查询需求时的局限性。研究背景是，随着数据驱动决策从技术专家扩展到业务分析师和普通用户，对自然语言数据交互的需求日益增长。然而，现有NL2SQL方法通常基于“封闭世界”假设，即所有必要信息都存在于单一数据库模式中。这在实际应用中存在明显不足：首先，用户查询往往是迭代式、多轮次表达的，而非单一明确问题；其次，许多问题需要跨多个异构数据源（如不同数据库、网络、知识库）获取信息，超出了单一数据库的范围；第三，查询常常依赖于常识或外部知识，以及通过交互获得的个人上下文信息，这些都无法被传统数据库系统直接涵盖。

因此，本文要解决的核心问题是：如何设计一个系统架构，以弥合用户意图与可用信息之间的语义鸿沟，满足现实世界中多源、多模态、数据中心化应用的需求。具体而言，论文提出的Blue系统数据智能层（DIL）试图通过将异构信息提供者（包括LLMs、网络和用户本身）统一视为一等数据源，并构建一个能够声明式地规划、检索、推理和集成跨模态数据的复合AI系统，来超越单一数据库的NL2SQL范式，实现对复杂、动态、依赖上下文的真实用户请求的有效响应。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自然语言数据交互系统展开，可归类如下：

**1. NL2SQL 系统：** 传统研究聚焦于将自然语言查询转换为单一数据库的 SQL 语句，如早期的模板匹配方法和近年基于深度学习的模型（如Seq2SQL、SQLNet）。本文的 Blue DIL 系统超越了这一范畴，它不局限于单一数据库的封闭世界假设，而是处理跨多源、多模态的复杂查询。

**2. 多源数据集成与查询：** 相关工作包括数据集成系统（如数据虚拟化、联邦查询）和多数据库查询语言。本文的 DIL 通过其数据注册表和统一的源抽象（将LLM、网络、用户均视为“数据库”）与之相关，但区别在于它更强调在智能体驱动的交互式场景中，动态整合结构化数据、外部知识和上下文。

**3. 基于LLM的数据交互与推理：** 近期研究探索利用大语言模型（LLM）进行数据查询、信息提取和常识推理，例如Text-to-SQL任务中引入外部知识。本文的 DIL 将 LLM 明确建模为一类数据源，并系统性地通过声明性查询计划（DAG）协调LLM与其他数据源的操作，这比单纯使用LLM生成查询或答案更结构化，并考虑了企业级优化。

**4. 复合AI系统与智能体编排：** 本文所属的Blue系统本身是一个复合AI系统，相关研究涉及用于任务分解和工具使用的AI智能体框架（如ReAct、AutoGPT）。DIL 作为其数据智能层，专注于为这类智能体提供底层数据访问与处理能力，其贡献在于设计了支持多模态操作符的规划器，以生成可执行的数据查询计划，从而将智能体的高层意图与具体的数据获取和集成连接起来。

综上，本文工作与NL2SQL、数据集成、LLM增强查询及智能体系统等多个领域相关，其核心区别与创新在于提出了一个统一的架构，以支持企业环境中由智能体驱动的、需要动态整合多源多模态数据的复杂应用场景。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为“数据智能层”的复合AI系统架构来解决多源、多模态数据集成与查询的复杂问题。其核心方法是构建一个统一的抽象层，将异构数据源（包括传统数据库、大语言模型、用户和网络）视为具有标准化查询接口的“数据库”，并利用智能规划器将用户自然语言查询转换为可执行的声明式数据计划。

整体框架包含四个主要模块：数据源、数据注册表、数据操作符和数据规划器。数据源模块进行了关键扩展，除了传统的关系型、文档型等数据库，创新性地引入了LLMDB（将LLM建模为结构化知识源）、UserDB（管理交互式用户上下文）和WebDB（提供按需网络数据提取）。数据注册表作为元数据目录，统一管理多级数据抽象的描述、样本和统计信息，支持跨源的数据发现与语义对齐。

数据操作符是处理异构数据的函数，采用分层设计。抽象（逻辑）操作符定义操作意图，物理操作符提供具体实现（如基于字典、模型或LLM）。所有操作符遵循统一的函数签名，其输入输出均为标准化的多层字典列表格式，这使得关系型、语义、向量等不同模态的操作符能够无缝互操作，构成可优化执行的数据流水线。

数据规划器是系统的创新核心。它将用户查询解释并分解为针对不同数据源的子查询，构建一个由操作符组成的有向无环图作为声明式数据计划。规划过程是递归的：首先实例化抽象操作符，然后通过`refine()`函数将其分解为可执行的替代子计划（例如将“问答”操作符细化为NL2SQL、NL2LLM或查询分解），直至所有节点均为具体操作符。规划器利用各注册表的信息，基于任务、成本等因素选择操作符和数据源。规划完成后，系统还进行两级优化：操作符级优化调整超参数（如模型选择）；计划级优化则重构DAG以降低执行成本或并行化独立分支。

综上，该方案通过将LLM、用户和网络提升为“一等公民”数据源，并利用一个由规划器驱动的、基于统一操作符的声明式工作流，实现了跨结构化数据、外部知识和个人上下文的语义桥接与协同推理，从而超越了传统单数据库NL2SQL系统的封闭世界假设。

### Q4: 论文做了哪些实验？

论文通过两个应用场景展示了Blue数据智能层（DIL）的实验验证，均采用多智能体协同处理多源多模态数据。实验设置上，系统由交互控制器或规划器协调多个模块化智能体，共同完成复杂任务。

第一个实验是“公寓搜索”，这是一个数据密集型任务。数据集来自多个网站爬取的公寓列表及辅助信息（如社区质量），这些异构、非结构化的网络数据被整合到统一的SQL数据库中。系统包含多个智能体：从网页构建数据库、从本地文件构建数据库、数据库转换、自然语言转SQL（NL-to-SQL）、数据探索（分析属性分布、缺失值等）和数据可视化（如生成租金趋势图）。该场景展示了如何动态集成异构数据源，并通过用户交互和智能体协调，为数据密集型任务提供可操作的洞察。

第二个实验是“个性化食谱推荐”，旨在解决传统食谱应用的僵化问题。系统结合了经过验证的结构化食谱数据库（PostgreSQL）与多模态用户输入。工作流程包括：通过视觉识别分析用户提供的冰箱图片以检测可用食材；使用软向量搜索（ChromaDB）基于食材进行候选食谱检索，并结合关系查询进行精确过滤；通过交互式对话迭代优化食谱选择；最终提供分步烹饪说明、回答后续问题并生成辅助图像。此场景集成了结构化数据库、用户文本/图像输入以及LLM的内部知识，实现了复杂、个性化的任务支持。

主要结果方面，论文通过这两个交互式场景，实证了DIL能够支持动态触发多源检索、跨模态推理和结果合成，推动了复合AI系统超越单一数据库的NL2SQL能力。关键数据指标虽未在提供章节中明确列出，但实验突出了系统在集成结构化企业数据、LLM世界知识和个人交互上下文方面的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的Blue DIL系统在统一多源多模态数据查询方面迈出了重要一步，但其局限性和未来探索空间仍十分广阔。首先，系统高度依赖LLM进行意图理解和规划，其可靠性、延迟和成本在复杂企业场景中可能面临挑战，未来可探索更轻量级或确定性的混合规划方法。其次，当前框架虽支持多种数据源，但对流式数据、实时传感器数据等动态源的处理机制未深入探讨，如何实现低延迟的连续查询与增量更新是一个关键方向。此外，系统的“可解释性”和“可调试性”不足，当生成复杂查询计划出错时，缺乏有效的用户反馈和迭代修正机制，未来需设计更透明的溯源和交互式调试界面。从架构上看，数据注册表的元数据管理仍可能成为瓶颈，如何自动化、动态地维护跨源的数据模式、新鲜度和质量指标值得研究。最后，论文展示了两个场景，但未进行大规模基准测试，未来需要在更广泛的真实企业工作流中验证其扩展性、鲁棒性和用户接受度，并探索与现有数据湖、数据中台架构的深度融合路径。

### Q6: 总结一下论文的主要内容

该论文针对传统NL2SQL系统在现实应用中的局限性，提出了Blue系统的数据智能层（DIL）框架。核心问题是解决用户自然语言查询与多源、多模态、异构数据之间的语义鸿沟，满足迭代式、跨数据源且需常识推理的复杂数据需求。

论文的核心贡献是设计了一个统一的、以代理为中心的复合AI系统架构。DIL将关系数据库、LLMs、网络和用户本身均视为一等数据源，并通过一个数据注册表来管理其元数据。方法上，DIL通过数据规划器将用户查询转换为声明式的、可执行的查询计划（DAG），该计划统一了关系操作符与跨模态操作符，支持对复杂请求进行分解、从多源检索、跨模态推理与结果集成。

主要结论是，DIL框架通过可扩展的操作符层次结构和声明性数据规划，能够动态协调多源数据与智能体，实现超越单数据库NL2SQL的交互式数据应用。这为构建更可靠、可扩展且语义基础扎实的企业级数据智能系统迈出了重要一步。
