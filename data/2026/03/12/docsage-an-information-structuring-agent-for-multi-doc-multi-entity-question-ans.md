---
title: "DocSage: An Information Structuring Agent for Multi-Doc Multi-Entity Question Answering"
authors:
  - "Teng Lin"
  - "Yizhang Zhu"
  - "Zhengxuan Zhang"
  - "Yuyu Luo"
  - "Nan Tang"
date: "2026-03-12"
arxiv_id: "2603.11798"
arxiv_url: "https://arxiv.org/abs/2603.11798"
pdf_url: "https://arxiv.org/pdf/2603.11798v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "信息结构化"
  - "多文档问答"
  - "关系推理"
  - "RAG 增强"
  - "动态模式发现"
  - "错误感知"
relevance_score: 7.5
---

# DocSage: An Information Structuring Agent for Multi-Doc Multi-Entity Question Answering

## 原始摘要

Multi-document Multi-entity Question Answering inherently demands models to track implicit logic between multiple entities across scattered documents. However, existing Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) frameworks suffer from critical limitations: standard RAG's vector similarity-based coarse-grained retrieval often omits critical facts, graph-based RAG fails to efficiently integrate fragmented complex relationship networks, and both lack schema awareness, leading to inadequate cross-document evidence chain construction and inaccurate entity relationship deduction. To address these challenges, we propose DocSage, an end-to-end agentic framework that integrates dynamic schema discovery, structured information extraction, and schema-aware relational reasoning with error guarantees. DocSage operates through three core modules: (1) A schema discovery module dynamically infers query-specific minimal joinable schemas to capture essential entities and relationships; (2) An extraction module transforms unstructured text into semantically coherent relational tables, enhanced by error-aware correction mechanisms to reduce extraction errors; (3) A reasoning module performs multi-hop relational reasoning over structured tables, leveraging schema awareness to efficiently align cross-document entities and aggregate evidence. This agentic design offers three key advantages: precise fact localization via SQL-powered indexing, natural support for cross-document entity joins through relational tables, and mitigated LLM attention diffusion via structured representation. Evaluations on two MDMEQA benchmarks demonstrate that DocSage significantly outperforms state-of-the-art long-context LLMs and RAG systems, achieving more than 27% accuracy improvements respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多文档多实体问答（MDMEQA）这一复杂任务中的核心挑战。该任务要求模型能够从多个分散的非结构化文档中，追踪不同实体之间隐含的逻辑关联，并构建连贯的证据链以生成准确答案。研究背景源于临床、金融、法律等高价值领域对碎片化信息进行深度整合与推理的迫切需求。

现有方法存在显著不足。尽管大语言模型（LLM）在单文档推理上表现出色，但其有限的上下文窗口和注意力扩散问题使其难以有效追踪跨文档的实体关系。检索增强生成（RAG）框架试图通过引入外部知识来弥补，但标准RAG基于向量相似度的粗粒度检索，往往优先语义重叠而非实体相关性，容易遗漏关键事实。基于图的RAG变体虽能改善多跳推理，却难以高效整合跨文档的复杂、碎片化关系网络，且图构建的计算成本随文档数量增长而急剧上升。这些方法的一个共同根本缺陷是缺乏“模式感知”能力，即无法根据查询动态构建明确的结构化表示，导致证据链割裂和实体关系推理不准确。

因此，本文要解决的核心问题是：如何设计一个能够系统性地克服上述局限的框架，以有效应对MDMEQA任务中信息碎片化、模式缺失和跨文档关系推理困难的挑战。为此，论文提出了DocSage，一个端到端的智能体框架。它通过动态模式发现、结构化信息提取和具备错误保证的模式感知关系推理，将非结构化文本转化为结构化的关系表格，并在此之上进行高效的多跳推理，从而精准定位事实、支持跨文档实体对齐并缓解注意力扩散问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多文档多实体问答（MDMEQA）任务展开，可分为方法类和应用类两大类。

在方法类研究中，现有工作主要包括基于大语言模型（LLM）和检索增强生成（RAG）的方法。标准RAG框架依赖向量相似度进行粗粒度检索，容易遗漏关键事实；图增强RAG将实体关系建模为三元组，虽能支持多跳推理，但难以高效整合跨文档的复杂、碎片化关系网络，且图构建的计算开销随文档数量增长而急剧增加。这两类方法的一个共同缺陷是缺乏模式感知能力，无法系统性地组织分散的实体和关系，导致证据链断裂和推理错误。

本文提出的DocSage框架与上述工作有显著区别和联系。它并非对现有RAG或图方法的简单改进，而是提出了一种全新的“信息结构化智能体”范式。其核心创新在于将动态模式发现、结构化信息提取和模式感知的关系推理集成为一个端到端的智能体框架，并引入了错误保证机制。具体而言，DocSage通过其模式发现模块动态推断查询相关的、可连接的最小模式，这直接针对了现有方法“模式缺失”的根本问题。其提取模块将非结构化文本转化为关系表，并辅以纠错机制，这比基于向量或图的检索能更精确地定位事实。其推理模块在结构化表上进行多跳关系推理，天然支持跨文档实体连接，避免了LLM在长上下文中的注意力扩散问题。因此，DocSage在方法论上是对现有LLM和RAG框架局限性的系统性回应和超越。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DocSage的端到端智能体框架来解决多文档多实体问答中的信息碎片化和逻辑推理难题。该框架的核心思想是动态地为文档集施加一个查询感知的、具有错误保证的关系型结构，从而将非结构化文本转化为可进行精确查询和推理的结构化知识库。其整体架构包含三个顺序集成的核心模块：交互式模式发现、逻辑感知的结构化提取和模式引导的关系推理。

**1. 交互式模式发现模块**：该模块旨在动态推断出针对特定查询的最小化、可连接的关系模式，以精确捕获回答查询所需的实体、属性和关系，而无需依赖任何预定义模式。其创新点在于提出了ASK（通过知识寻求查询进行主动模式发现）算法。该算法将模式发现构建为一个与文档集的交互式对话过程，而非传统的被动扫描。具体步骤包括：首先生成初始模式假设；然后分析模式在更多文档上应用时产生的实体对齐冲突、属性值分布异常和关系缺失等不确定性信号；接着主动生成澄清性问题，并利用这些问题引导针对性检索；最后基于检索到的证据迭代更新模式，直至收敛。这种主动交互设计确保了最终模式的鲁棒性和准确性。

**2. 逻辑感知的结构化提取模块**：在获得目标模式后，此模块负责从文档中高保真地提取元组来填充该模式。其关键技术是引入了CLEAR（通过跨记录逻辑强制执行进行准确性增强）校正机制。该机制包含两个层面：A）单点置信度评估：通过为提取模型微调一个轻量级的LoRA适配器，并结合保形预测阈值，为每个候选元组计算校准后的置信度分数。B）跨记录逻辑一致性检查：定义一组依赖于模式的逻辑约束（如函数依赖、时间约束、数值范围、外键引用完整性），并将所有候选元组暂存于临时数据库，运行一个轻量级约束验证引擎来检测违反约束的元组集合。对于低置信度或涉及逻辑冲突的元组，系统会动态触发校正工作流，可能使用更强大的LLM委员会进行重新提取，或启动验证与消歧子模块进行深度上下文分析。最终输出一个高质量的关系数据库。

**3. 模式引导的关系推理模块**：该模块直接在精确构建的关系数据库及其模式上执行查询。其创新在于利用显式的模式信息，将复杂的多跳推理转化为确定性的数据库操作。首先，一个推理LLM将自然语言查询编译并优化成SQL查询，模式中的显式连接键和关系定义使得编译器能够生成高度优化的连接查询。执行优化后的SQL查询得到结构化结果集。系统会自动将结果集中的每一行追溯至其在数据库中的源元组，并进一步映射回原始文档中的具体位置。最后，推理LLM基于结果集和完整的溯源链生成最终的自然语言答案，确保了答案的可验证性。

**整体创新点**：DocSage框架通过上述模块的协同工作，实现了三大优势：1）通过SQL驱动的索引实现精确的事实定位；2）通过关系表天然支持跨文档实体连接；3）通过结构化表示缓解LLM的注意力扩散问题。这种智能体设计有效解决了传统RAG在细粒度检索、复杂关系网络整合和模式感知方面的不足。

### Q4: 论文做了哪些实验？

论文在MEBench和Loong两个多文档多实体问答（MDMEQA）基准上进行了实验评估。实验设置方面，DocSage使用GPT-4o和Qwen3作为主要大语言模型，Mistral-7B用于信息提取，GPT-4o用于推理模块。对比方法包括：作为纯生成基线的GPT-4o、基于向量检索的标准RAG（GPT-4o + RAG）、基于知识图谱的GraphRAG以及结构感知的StructRAG。

在MEBench数据集（包含4,780个问题，分为比较、统计和关系三类）上，主要评估指标为准确率。DocSage取得了显著优势，整体准确率达到89.2%，远超最佳基线GPT-4o + RAG的62.0%，提升超过27个百分点。在按实体数量划分的子集（Set1: 0-10, Set2: 11-100, Set3: >100）上，DocSage均表现最优，尤其在实体最多的Set3上仍保持87.9%的准确率，展现了极强的鲁棒性。

在Loong数据集（包含聚焦定位、比较、聚类和推理链四个任务，文档长度从10K到250K token递增）上，评估采用LLM评判的平均分数（0-100）和精确匹配率（Perfect Rate, 0-1）。DocSage在整体平均分数（68.29）和精确匹配率（0.53）上均大幅领先。特别是在最长的文档设置（200K-250K token）中，其精确匹配率（0.47）显著高于其他方法（均低于0.10），证明了其在长文档、信息分散场景下的卓越能力。

### Q5: 有什么可以进一步探索的点？

本文提出的DocSage框架虽然在多文档多实体问答上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其性能与底层基础模型的能力紧密耦合，且多阶段智能体流程带来了较高的计算成本。未来可研究更轻量化的模型微调或蒸馏技术，以降低对大型通用LLM的依赖，并优化流程的并行性与迭代策略，提升效率。其次，框架假设文档间存在语义连贯性和事实一致性，对高度噪声、矛盾或专业领域文本的鲁棒性不足。后续可探索引入领域自适应预训练、矛盾检测与消解机制，以及更强大的错误感知与修正模块。此外，当前结构主要基于关系型表格，未来可结合图神经网络等，更灵活地建模复杂、动态的关系网络。最后，可考虑将框架扩展至更具挑战性的场景，如实时流式文档处理、多模态信息融合，以及支持更复杂的推理类型（如因果、反事实推理），进一步提升其实用性与泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对多文档多实体问答任务中现有大语言模型和检索增强生成框架的不足，提出了DocSage这一新型智能体框架。核心问题是传统方法基于向量相似性的粗粒度检索易遗漏关键事实，且缺乏模式感知能力，难以构建跨文档证据链和准确推断实体关系。DocSage通过三个协同模块解决该问题：模式发现模块动态推断查询相关的最小可连接模式以捕获关键实体与关系；提取模块将非结构化文本转化为语义一致的关系表，并引入错误感知校正机制降低提取误差；推理模块在结构化表上进行多跳关系推理，利用模式感知高效对齐跨文档实体并聚合证据。该方法的主要优势在于通过SQL索引实现精准事实定位、利用关系表自然支持跨文档实体连接，以及通过结构化表示缓解LLM注意力扩散。实验表明，DocSage在两个MDMEQA基准上显著优于现有长上下文LLM和RAG系统，准确率提升超过27%，验证了以动态结构归纳为核心的智能体工作流能有效提升对碎片化、模式稀缺文档集合的复杂推理能力。
