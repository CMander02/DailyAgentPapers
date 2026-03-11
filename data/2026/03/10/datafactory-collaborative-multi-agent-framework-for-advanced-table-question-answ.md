---
title: "DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering"
authors:
  - "Tong Wang"
  - "Chi Jin"
  - "Yongkang Chen"
  - "Huan Deng"
  - "Xiaohui Kuang"
  - "Gang Zhao"
date: "2026-03-10"
arxiv_id: "2603.09152"
arxiv_url: "https://arxiv.org/abs/2603.09152"
pdf_url: "https://arxiv.org/pdf/2603.09152v1"
categories:
  - "cs.AI"
  - "cs.DB"
  - "cs.IR"
tags:
  - "Multi-Agent Collaboration"
  - "Table Question Answering"
  - "Reasoning & Planning"
  - "Knowledge Graph"
  - "Tool Use"
  - "ReAct"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering

## 原始摘要

Table Question Answering (TableQA) enables natural language interaction with structured tabular data. However, existing large language model (LLM) approaches face critical limitations: context length constraints that restrict data handling capabilities, hallucination issues that compromise answer reliability, and single-agent architectures that struggle with complex reasoning scenarios involving semantic relationships and multi-hop logic. This paper introduces DataFactory, a multi-agent framework that addresses these limitations through specialized team coordination and automated knowledge transformation. The framework comprises a Data Leader employing the ReAct paradigm for reasoning orchestration, together with dedicated Database and Knowledge Graph teams, enabling the systematic decomposition of complex queries into structured and relational reasoning tasks. We formalize automated data-to-knowledge graph transformation via the mapping function T:D x S x R -> G, and implement natural language-based consultation that - unlike fixed workflow multi-agent systems - enables flexible inter-agent deliberation and adaptive planning to improve coordination robustness. We also apply context engineering strategies that integrate historical patterns and domain knowledge to reduce hallucinations and improve query accuracy. Across TabFact, WikiTableQuestions, and FeTaQA, using eight LLMs from five providers, results show consistent gains. Our approach improves accuracy by 20.2% (TabFact) and 23.9% (WikiTQ) over baselines, with significant effects (Cohen's d > 1). Team coordination also outperforms single-team variants (+5.5% TabFact, +14.4% WikiTQ, +17.1% FeTaQA ROUGE-2). The framework offers design guidelines for multi-agent collaboration and a practical platform for enterprise data analysis through integrated structured querying and graph-based knowledge representation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的表格问答（TableQA）系统所面临的几个关键局限性。研究背景是，表格问答作为自然语言与结构化表格数据交互的重要方式，早期依赖规则或深度学习模型（如TAPAS），近期则转向LLM。然而，现有方法存在明显不足：首先，LLM存在上下文长度限制，难以处理大规模表格数据；其次，模型容易产生“幻觉”，导致答案不可靠；再者，主流单智能体架构在应对涉及语义关系和多跳逻辑的复杂推理场景时能力不足，缺乏系统性的任务分解与协作机制。

针对这些不足，本文的核心问题是：如何设计一个能够克服上下文限制、减少幻觉、并有效处理复杂推理的多智能体协作框架。为此，论文提出了DataFactory框架。该框架通过建立专门的数据团队和知识图谱团队，将复杂的查询任务系统地分解为结构化查询和关系推理子任务，并引入一个采用ReAct范式的“数据领导者”进行协调。其核心解决方案包括：1）形式化地定义了从数据到知识图谱的自动转换映射（T: D x S x R -> G），以捕获语义关系；2）设计了基于自然语言的智能体间协商机制，实现灵活的审议与自适应规划，而非僵化的工作流；3）应用集成历史模式和领域知识的上下文工程策略，以提高查询准确性并减少幻觉。最终，该研究旨在提供一个兼具专业化协作、自动化知识集成和可扩展推理能力的综合解决方案。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类，涵盖了当前表格问答领域的主要技术范式。

在方法类研究中，现有工作主要围绕两大范式展开。一是直接提示方法，即直接将表格内容作为上下文输入大语言模型以生成答案，但该方法受限于上下文长度、易产生幻觉且推理过程不透明。二是代码生成方法，通过生成可执行代码（如Python、SQL或电子表格公式）来操作表格，提高了可验证性，但在处理复杂层次结构或多步推理时仍有不足。这些方法都侧重于结构化字段提取，但难以有效处理涉及语义关系和跨行综合的复杂推理。

在应用类研究中，基于智能体的框架成为新兴方向。具体包括：ReAct式分解方法，通过交错推理与工具调用来系统导航表格；单智能体精炼方法，通过迭代验证提升准确性，但在处理需要多样化专业知识的复杂查询时存在局限；知识增强方法，通过整合外部知识或图表示来辅助推理，但通常对语义关系的覆盖较浅；工具编排与规划系统，选择性调用异构工具以提高透明度，但在保持全局一致性和故障恢复方面仍有挑战；以及多智能体协作方法，通过角色 specialization 构建管道（如AutoPrep、AutoTQA），但现有系统常因协调问题、规范违反和验证机制不足而失败，且协调多基于预定义工作流，缺乏动态协商能力。

本文提出的DataFactory框架与上述工作密切相关但存在关键区别。它继承了多智能体分工协作的思想，但通过引入专门的知识图谱团队，实现了数据到知识图谱的自动化转换（通过映射函数 T:D x S x R -> G），并支持结构化查询与图查询的集成推理。与现有固定工作流的多智能体系统不同，本文框架强调基于自然语言的协商与审议，使数据领导者、数据库团队和知识图谱团队三个专业智能体之间能够进行灵活的跨团队知识共享和自适应策略调整，从而更好地处理需要多跳推理和动态规划的复杂探索性查询。此外，本文还应用了整合历史模式和领域知识的上下文工程策略，以进一步减少幻觉。因此，本文工作是对现有智能体方法，特别是在动态协调和深度知识集成方面的重要推进。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为DataFactory的多智能体协作框架来解决现有TableQA方法在上下文长度限制、幻觉问题和复杂推理方面的局限性。其核心方法是将复杂的表格问答任务分解为结构化数据处理和关系知识推理两个互补的维度，并通过一个中央协调者进行动态任务编排。

整体框架采用三方协作架构，包含三个核心组件：**数据领导者（Data Leader）**、**数据库团队（Database Team）**和**知识图谱团队（Knowledge Graph Team）**。数据领导者作为总协调者，采用ReAct范式对用户查询进行推理和分解，将其拆解为适合数据库团队处理的结构化查询子任务，或适合知识图谱团队处理的关系推理子任务。其创新点在于摒弃了固定的工作流，通过基于自然语言的协商机制与两个专家团队进行动态、自适应的协调与策略调整。

**数据库团队**专注于结构化数据处理，其核心创新是**上下文增强的SQL生成**。该团队包含四个专门代理：信息处理代理（负责自动化数据摄取与模式理解）、信息检索代理（核心模块，负责生成SQL）、信息分析代理（解释查询结果）和可视化代理。其中，信息检索代理采用了**检索增强生成（RAG）技术**，动态地从历史问答对、数据库模式定义和领域知识三个来源整合上下文信息，构建提示词以生成准确SQL，从而有效减少幻觉并提高数值计算和聚合查询的准确性。

**知识图谱团队**专注于关系知识表示与推理，其关键技术是**自动化的数据到知识图谱的转换函数** $\mathcal{T}: \mathcal{D} \times \mathcal{S} \times \mathcal{R} \rightarrow \mathcal{G}$。该函数将原始表格数据$\mathcal{D}$、模式定义$\mathcal{S}$和关系规则$\mathcal{R}$，系统地转化为支持多跳推理的知识图谱$\mathcal{G}$。这一自动化转换过程结合了LLM辅助的模式识别和算法验证，解决了传统方法依赖手动模式工程、难以捕捉语义关系的可扩展性问题。该团队同样由处理、检索、分析和可视化四个代理组成，专门处理涉及实体间复杂关联的查询。

框架的运作分为三个阶段：信息存储阶段（自动化建立数据库和知识图谱）、知识提取阶段（通过上下文增强提示生成准确查询）和洞察生成阶段（协调多智能体协作并综合结果）。这种架构设计的根本创新在于**将表格问答解耦为结构化和关系化两种推理模态**，并通过灵活的、基于自然语言的智能体间协商机制进行协调，从而实现了结合两者优势的复杂多跳推理，同时保持了过程的可解释性。

### Q4: 论文做了哪些实验？

论文在三个主流表格问答数据集上进行了实验：TabFact（事实核查）、WikiTableQuestions（复杂问答）和FeTaQA（生成式问答）。实验设置使用了来自五个提供商的八个大语言模型作为基础，并对比了单智能体基线、仅数据库团队或仅知识图谱团队的变体。主要方法DataFactory采用多智能体协作框架，包含一个使用ReAct范式进行推理编排的Data Leader，以及专门处理结构化查询和关系推理的Database与Knowledge Graph团队。

关键数据指标显示，DataFactory相比基线模型在准确率上取得了显著提升：在TabFact上提高了20.2%，在WikiTableQuestions上提高了23.9%，且效应量显著（Cohen's d > 1）。团队协作的优势通过消融实验得到验证：完整框架相比单团队变体在TabFact上准确率提升5.5%，在WikiTableQuestions上提升14.4%，在FeTaQA的ROUGE-2指标上提升17.1%。这些结果证明了通过智能体间协商和自动化知识图谱转换（映射函数T: D x S x R -> G）的协作机制能有效处理复杂多跳推理，并减少幻觉。

### Q5: 有什么可以进一步探索的点？

本文提出的DataFactory框架虽在多智能体协作和知识转换方面取得进展，但仍存在若干局限和可拓展方向。首先，框架依赖外部LLM，其性能受限于所选模型的固有能力，如上下文长度和推理错误，未来可探索更轻量化的专用模型或持续学习机制来降低依赖。其次，自动化知识图谱构建的映射函数T可能无法完全覆盖复杂表格的隐含语义关系，可引入强化学习优化映射策略，或结合人类反馈进行迭代修正。此外，当前智能体间的协商机制虽灵活，但缺乏长期记忆和任务历史学习能力，未来可设计元认知模块，使智能体能够从过往协作中积累经验，动态调整分工策略。最后，框架在跨领域、多模态表格（如图表混合数据）上的泛化能力未经验证，可探索引入视觉-语言模型以处理更丰富的数据形态，进一步提升实际企业场景的适用性。

### Q6: 总结一下论文的主要内容

本文提出了DataFactory，一个用于高级表格问答（TableQA）的协作多智能体框架，旨在解决现有大语言模型（LLM）方法在上下文长度限制、幻觉问题以及单智能体架构处理复杂推理场景方面的不足。其核心贡献在于通过专业化的团队协调和自动化的知识转换来应对这些挑战。

该框架定义了由采用ReAct范式的“数据领导”智能体进行推理编排，并协同专门的数据库团队和知识图谱团队，从而将复杂查询系统性地分解为结构化和关系型推理任务。方法上，它形式化了通过映射函数T:D x S x R -> G实现的自动数据到知识图谱的转换，并采用了基于自然语言的协商机制，这使得智能体间能够进行灵活的审议和自适应规划，而非固定的工作流，从而提升了协调的鲁棒性。此外，通过整合历史模式和领域知识的上下文工程策略来减少幻觉并提高查询准确性。

实验在TabFact、WikiTableQuestions和FeTaQA三个基准上使用五个提供商的八种LLM进行，结果表明该方法取得了显著提升：相较于基线，在TabFact和WikiTQ上的准确率分别提高了20.2%和23.9%（效应量Cohen‘s d > 1），且团队协作版本也显著优于单团队变体。该框架为多智能体协作提供了设计指南，并通过集成的结构化查询和图谱知识表示，为企业数据分析提供了一个实用平台。
