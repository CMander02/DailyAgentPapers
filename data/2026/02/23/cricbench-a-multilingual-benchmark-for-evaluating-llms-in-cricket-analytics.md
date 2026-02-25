---
title: "CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics"
authors:
  - "Vaibhav Devraj"
  - "Dhruv Kumar"
  - "Jagat Sesh Challa"
  - "Parth Agarwal"
  - "Navya Kommuri"
  - "Trizal Garg"
  - "Prisha Singhal"
  - "Dhruv Shah"
date: "2025-12-26"
arxiv_id: "2512.21877"
arxiv_url: "https://arxiv.org/abs/2512.21877"
pdf_url: "https://arxiv.org/pdf/2512.21877v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评测/基准"
  - "领域特定Agent"
  - "多语言Agent"
  - "Text-to-SQL"
  - "体育分析"
relevance_score: 7.5
---

# CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics

## 原始摘要

Cricket is the second most popular sport globally, commanding a massive following of over 2.5 billion fans globally. Enthusiasts and analysts frequently seek advanced statistical insights, such as long-term historical performance trends or complex player comparisons, that are often unavailable through standard web searches. While Large Language Models (LLMs) have advanced significantly in Text-to-SQL tasks, their capability to handle the domain-specific nuances, complex schema variations, and multilingual requirements inherent to sports analytics remains under-explored. To investigate this potential capability gap, we present CricBench, a comprehensive benchmark suite for evaluating LLMs on specialized cricket data. To curate a "Gold Standard" dataset, we collaborate with domain experts in cricket and SQL to manually author complex queries, ensuring logical correctness. Recognizing linguistic diversity, we construct the benchmark in both English and Hindi, establishing a framework that is open for further extension to other regional languages. We evaluate six state-of-the-art models, including GPT-4o, Claude 3.7 Sonnet, and open-source models, using a strict evaluation protocol. Our results reveal that high performance on general benchmarks does not guarantee success in specialized domains. While the open-weights reasoning model DeepSeek R1 achieves state-of-the-art performance (50.6%), surpassing proprietary giants like Claude 3.7 Sonnet (47.7%) and GPT-4o (33.7%), it still exhibits a significant accuracy drop when moving from general benchmarks (BIRD) to CricBench. Furthermore, we observe that code-mixed Hindi queries frequently yield parity or higher accuracy compared to English, challenging the assumption that English is the optimal prompt language for specialized SQL tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在特定领域、特别是体育分析领域中的能力评估不足问题。具体而言，作者聚焦于板球——全球第二大运动，拥有超过25亿粉丝。他们指出，虽然LLMs在通用Text-to-SQL任务上取得了显著进展，但其处理领域特定细微差别、复杂模式变化以及多语言需求的能力尚未得到充分探索。板球分析通常需要高级统计洞察，如长期历史表现趋势或复杂的球员比较，这些信息往往无法通过标准网络搜索获得。因此，论文的核心问题是：当前先进的LLMs能否有效理解和处理板球领域的复杂、多语言数据查询？为了系统性地研究这一“潜在能力差距”，作者构建了一个名为CricBench的综合性基准测试套件，用于评估LLMs在专业板球数据分析上的表现。

### Q2: 有哪些相关研究？

相关研究主要围绕三个方向：通用Text-to-SQL基准、领域特定基准以及多语言NLP评估。在Text-to-SQL方面，Spider、WikiSQL和BIRD是经典基准，其中BIRD特别关注真实世界的数据库复杂性和噪声，与CricBench在追求真实性和复杂性上有相似之处。在领域特定基准方面，已有工作如FinQA（金融）、MIMICSQL（医疗）和SciBench（科学），它们证明了通用模型在专业领域表现会下降，CricBench延续了这一研究方向，但专注于体育分析。在多语言NLP评估方面，XGLUE、XTREME等基准评估模型跨语言能力，而CricBench的创新在于将多语言性（英语和印地语）直接融入一个高度专业化的领域任务中。本文与这些工作的关系是：它借鉴了领域特定基准的构建理念和Text-to-SQL的评估框架，但创造性地将其应用于一个尚未被充分探索的、拥有巨大受众的体育领域，并强调了多语言和代码混合查询的现实挑战，从而填补了现有研究空白。

### Q3: 论文如何解决这个问题？

论文通过构建并系统评估一个名为CricBench的多语言板球分析基准来解决该问题。其核心方法包括以下几个关键步骤：首先，数据收集与模式构建：作者从ESPN Cricinfo等可靠来源收集了全面的板球数据（涵盖2003-2023年），并设计了一个包含10个表、关系复杂的数据库模式，以真实反映板球领域的实体和关系（如球员、球队、比赛、系列赛、击球、投球等）。其次，“黄金标准”查询集构建：这是方法的核心。他们与板球领域专家和SQL专家合作，手动编写了200个复杂查询（100个英语，100个印地语），确保逻辑正确性和领域相关性。查询分为五类难度等级，从简单的事实检索到需要多步推理和子查询的复杂分析。第三，多语言与代码混合处理：基准原生支持英语和印地语。特别值得注意的是，印地语查询中包含了代码混合现象（即混用英语术语，如“strike rate”），这更贴近真实世界的查询习惯。第四，严格的评估协议：采用精确匹配（Exact Match）和部分匹配（Partial Match）两种指标，并执行严格的查询结果验证。他们评估了六种最先进的模型，包括专有模型（GPT-4o, Claude 3.7 Sonnet）和开源模型（DeepSeek R1, Llama 3.1系列, Qwen 2.5系列），以全面衡量模型性能。整个方法强调了领域专业知识、真实复杂性和多语言需求的结合。

### Q4: 论文做了哪些实验？

论文进行了一系列实验来评估LLMs在CricBench上的表现。实验设置如下：他们评估了六个SOTA模型：GPT-4o、Claude 3.7 Sonnet（专有模型），以及DeepSeek R1、Llama-3.1-405B-Instruct、Llama-3.1-70B-Instruct、Qwen2.5-72B-Instruct（开源模型）。评估使用零样本提示，提示词经过精心设计以包含数据库模式描述和任务指令。评估指标采用精确匹配（EM，要求生成的SQL与黄金标准在字符串和逻辑上完全一致）和部分匹配（PM，允许在列别名、空格等方面有微小差异）。主要结果揭示了几点关键发现：1. 领域性能差距：所有模型在CricBench上的表现均显著低于在通用Text-to-SQL基准（如BIRD）上的表现。例如，表现最佳的DeepSeek R1在CricBench上准确率为50.6%，远低于其在BIRD上的高分，证实了领域迁移的挑战。2. 开源模型的竞争力：DeepSeek R1以50.6%的EM率取得了最优性能，甚至超过了Claude 3.7 Sonnet（47.7%）和GPT-4o（33.7%），展示了开源推理模型的强大潜力。3. 多语言现象的意外发现：印地语查询（包括代码混合）的表现经常与英语持平甚至更好，挑战了“英语是专业SQL任务最佳提示语言”的假设。4. 难度分析：随着查询难度增加，所有模型的性能都急剧下降，尤其是在需要复杂嵌套查询和聚合操作的级别。实验还进行了错误分析，将主要错误类型归类为模式链接错误、聚合/嵌套错误等，为模型改进提供了方向。

### Q5: 有什么可以进一步探索的点？

基于本研究的发现，未来有几个值得深入探索的方向：首先，基准扩展与泛化：可以将CricBench扩展到更多语言（如孟加拉语、乌尔都语等板球流行地区的语言），并考虑纳入更动态的数据（如实时比赛数据）和更复杂的分析任务（如预测、战略模拟），以提升基准的广度和现实性。其次，模型适应方法：针对观察到的领域性能差距，可以研究专门的适应技术，例如领域特定的微调、检索增强生成（RAG）结合板球知识库、或针对复杂模式链接的提示工程优化。第三，深入理解多语言优势：需要进一步研究为什么代码混合的印地语查询有时表现更好。这是否与训练数据分布、术语的歧义性降低，或模型的多语言表示特性有关？这为多语言NLP和领域适应提供了新的研究课题。第四，错误缓解与推理增强：针对错误分析中发现的模式链接和复杂嵌套问题，可以探索结合符号推理、迭代修正或外部验证模块的混合方法，以提高生成SQL的鲁棒性和准确性。最后，将框架应用于其他领域：CricBench的构建方法论（专家协作、多语言、复杂模式）可以推广到其他专业领域（如法律、金融、医疗），以系统评估和提升LLMs的垂直领域能力。

### Q6: 总结一下论文的主要内容

本文提出了CricBench，一个用于评估大型语言模型在板球分析领域能力的多语言基准测试套件。论文的核心贡献在于揭示并量化了先进LLMs在从通用任务迁移到高度专业化、多语言领域时所面临的能力缺口。通过与领域专家合作，作者构建了一个包含复杂数据库模式和200个手动编写、逻辑正确的查询（英语和印地语各半）的“黄金标准”数据集。对六种SOTA模型的评估表明，即使在通用基准上表现优异的模型，在CricBench上也遭遇了显著的性能下降。一个关键发现是开源模型DeepSeek R1超越了包括GPT-4o和Claude 3.7 Sonnet在内的专有模型，取得了最佳性能。另一个反直觉的发现是，包含代码混合的印地语查询并不逊色于甚至优于纯英语查询，这对领域任务中语言选择的传统假设提出了挑战。总之，CricBench不仅为LLMs在体育分析和领域特定Text-to-SQL任务上的评估提供了急需的工具，也强调了在模型开发和评估中纳入领域复杂性、真实世界数据和多语言考虑的重要性。
