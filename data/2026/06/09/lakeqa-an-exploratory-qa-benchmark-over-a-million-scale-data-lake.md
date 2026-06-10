---
title: "LakeQA: An Exploratory QA Benchmark over a Million-Scale Data Lake"
authors:
  - "Haonan Wang"
  - "Jiaxiang Liu"
  - "Yurong Liu"
  - "Austin Senna Wijaya"
  - "Tianle Zhou"
  - "Eden Wu"
  - "Yijia Chen"
  - "Wanting You"
  - "Reya Vir"
  - "Daniela Pinto"
  - "Grace Fan"
  - "Yusen Zhang"
  - "Juliana Freire"
  - "Eugene Wu"
date: "2026-06-09"
arxiv_id: "2606.10460"
arxiv_url: "https://arxiv.org/abs/2606.10460"
pdf_url: "https://arxiv.org/pdf/2606.10460v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent基准"
  - "多跳推理"
  - "数据湖问答"
  - "搜索与推理"
  - "大语言模型评估"
relevance_score: 8.5
---

# LakeQA: An Exploratory QA Benchmark over a Million-Scale Data Lake

## 原始摘要

Recent large language models (LLMs) have shown rapid progress in reading-based question answering (QA), where evidence is explicitly provided or can be trivially retrieved. In contrast, real-world questions are often not paired with accurate evidence documents. The useful evidence resides in massive data lakes, making search a prerequisite for answering. However, there is a lack of comprehensive benchmarks that require both searching and reasoning over large data lakes. To this end, we introduce LakeQA, a comprehensive benchmark for search-centric question answering over data lakes that jointly emphasizes searching and reasoning capabilities. LakeQA is built on a heterogeneous collection of approximately 9.5 TB of text resources from Wikipedia and open-source government data, spanning structured and unstructured data. To ensure task quality, each sample is annotated by at least one Ph.D.-level expert. Each task requires long-horizon multi-hop reasoning with implicit intermediate steps: agents need to discover the correct documents and then compose evidence across sources to produce the answer. Experimental results on seven frontier LLMs demonstrate that LakeQA is challenging. For instance, GPT-5.2 achieves only an exact-match score of 18.37% on LakeQA. Overall, LakeQA provides a realistic testbed for developing LLM agents that can both find and analyze data in modern data lakes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有问答系统在面对大规模、异构数据湖时，无法同时兼顾高搜索强度和高推理强度的问题。研究背景是，近年来大语言模型在基于明确提供证据或简单检索的阅读理解问答上取得了显著进展。然而，现实世界中的问题往往没有预先配对的准确证据文档，所需证据分散在包含数百万文档（涵盖结构化与非结构化数据）的庞大、异构的数据湖中，搜索成为回答问题的前提。现有方法的不足在于，大多数基准测试要么搜索空间有限（如推理强度大但仅包含数百个文档），要么推理步骤过少（如搜索空间大但平均推理步骤不足两步），无法真实模拟现实场景中需要反复搜索与长链推理相结合的任务。本文要解决的核心问题是，构建一个能同时评估智能体在大规模数据湖（约40M文档、9.5TB数据）中进行多跳、探索性搜索与推理能力的综合性基准，填补现有基准在联合强调搜索与推理能力方面的空白。

### Q2: 有哪些相关研究？

根据论文内容，相关工作主要分为三类：

1. **多跳文本问答**：包括ComplexWebQuestion、HotpotQA、MuSiQue和StrategyQA等。这些工作主要针对结构化知识库或有限文本集进行组合推理，但通常提供黄金支持段落，无需大规模搜索。本文的LakeQA与之不同，需要在约40M个文件的异构数据湖中进行搜索和推理，显著扩展了检索和推理复杂度。

2. **异构数据问答**：包括FeTaQA、MMQA、HybridQA、OTT-QA和MultiModalQA。这些工作涉及表格、文本或多模态推理，但多提供相关上下文或操作于策划好的语料集。LakeQA则要求智能体从未经筛选的、包含结构和非结构数据的海量集合中发现证据。

3. **开放域数据发现**：包括BrowseComp和MM-BrowseComp，强调在开放互联网上的迭代检索。而LakeQA聚焦于数据湖规模的数据发现，要求同时处理结构化和非结构化数据。此外，数据管理领域有关于数据湖文档检索的工作，但未将多跳问答作为下游任务。LakeQA首次将数据检索作为多跳问答的必要组成部分，融合了高搜索强度和高推理强度。

### Q3: 论文如何解决这个问题？

LakeQA通过构建一个大规模异构数据湖基准测试来解决搜索和推理协同挑战。核心方法包括三个层面：**数据湖构建**、**多跳问题生成**和**交互式工具集定义**。

**数据湖构建**方面，整合了Wikipedia文本语料和Data.gov开放数据（约9.5TB，4000万文件），涵盖结构化表格/非结构化文本等异构格式。通过去重保留单一规范副本，并保留原始元数据实现异构性。

**问题生成**采用人工驱动的子问题组合（Composition）技术：第一阶段由标注员从单个文档提取事实形成子问答对，然后逐步扩展，使前一答案作为后一子问题的条件，形成K跳推理链；第二阶段将子问题链改写为自然语言问题，同时消除文档标识符泄露（如用“纽约市公立学校的暴力事件记录”代替“vadir-incidents表”）。

**交互设计**定义了发现/检索/分析三类基础工具（如文档检索、表格查询），允许LLM智能体通过多步工具调用来定位相关文档、提取证据并生成答案。标注流程包含至少4名独立审核者（含博士级专家），确保推理正确性和问题自然性。

创新点包括：1)首个同时强调搜索与推理的大规模数据湖基准；2)人类标注的多跳问题需隐式中间步骤（不暴露文档路径）；3)覆盖约9.5TB异构数据，远超现有基准（如WikiQA仅基于Wikipedia短文本）。实验显示GPT-5.2仅达18.37%准确率，验证了挑战性。

### Q4: 论文做了哪些实验？

论文在LakeQA基准上对7个前沿大语言模型进行了多维度实验。实验设置分为两个规模：full版（完整9.5TB数据湖）和mini版（135个样本，用于快速迭代）。对比方法包括开源模型（Llama-3.3-70B、DeepSeek-R1）和闭源模型（GPT-5.2、GPT-5-mini、Claude-haiku/sonnet/opus-4.5）。主要评估指标为精确匹配率（EM），并额外记录运行时间、成本、以及检索集（D_ret）和访问集（D_acc）的精确率/召回率/F1。

主要实验结果：(1)端到端任务上，Claude-sonnet-4.5在full版上取得最佳EM为32.87%，GPT-5.2为18.37%，DeepSeek-R1为15.99%，Llama-3.3-70B仅5.06%。mini版上Claude-opus-4.5达45.93%。(2)RAG检索基线实验显示，在10K/25K/50K文档子集上增加BM25或混合检索工具可小幅提升EM但效果不稳定。(3)轨迹级失败分析发现，主要失败原因是搜索数据集缺失（如GPT-5-mini达112/135）和检索后未选择正确文档。(4)按推理跳数分层显示，随着所需文档数量增加（>18个），所有模型EM急剧下降，揭示了搜索与推理的耦合瓶颈。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于文档发现环节成为主要瓶颈：模型在需要长推理链和多证据源的复杂任务中表现急剧下降，且保守探索策略（高精度低召回）严重受限。未来可从三方面改进：

1. **分层检索策略**：当前一次性检索效率不足，可设计先粗粒度筛选文档类型/领域，再细粒度定位具体段落的分层架构，结合聚类或主题建模减少搜索空间。

2. **动态推理-检索协同**：现有模型在发现关键文档后仍难以整合跨源证据，可引入基于推理状态的反向检索机制——当推理路径中断时，主动召回缺失证据链对应的文档，类似迭代式知识图谱构建。

3. **多模态证据融合**：数据湖包含结构化表与半结构化文本，可设计统一的混合表示方式（如将表格转化为关系三元组），并在检索阶段对不同模态设置差异化权重，避免模型偏向纯文本证据。

此外，建议构建带有失败追踪反馈的强化学习框架，让模型在探索失败时自动调整文档选择策略，而不依赖固定阈值。

### Q6: 总结一下论文的主要内容

LakeQA是一个针对大规模数据湖的探索性问答基准，旨在评估具备搜索与推理能力的LLM智能体。该基准定义了一个现实问题：用户提问时未提供准确证据，必须从约9.5TB的异构数据湖（包括Wikipedia和政府开源的结构化与非结构化数据）中搜索并推理答案。每个样本由博士级专家标注，任务需要长程多跳推理，包含隐式的中间步骤——智能体需先发现正确文档，再跨来源整合证据。实验表明该基准极具挑战性：例如，GPT-5.2的精确匹配得分仅为18.37%。核心结论是，即使给予搜索工具，LLM在端到端准确率上仍很低，且随着推理链和证据源增加性能急剧下降。基于追踪的分析揭示主要瓶颈在于文档发现阶段——模型常无法检索并打开黄金文档，而保守的探索策略（高精度低召回）会严重惩罚性能。LakeQA为开发能在现代数据湖中查找和分析数据的LLM智能体提供了逼真的测试平台。
