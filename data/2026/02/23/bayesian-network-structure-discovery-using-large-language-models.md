---
title: "Bayesian Network Structure Discovery Using Large Language Models"
authors:
  - "Yinghuan Zhang"
  - "Yufei Zhang"
  - "Parisa Kordjamshidi"
  - "Zijun Cui"
date: "2025-11-01"
arxiv_id: "2511.00574"
arxiv_url: "https://arxiv.org/abs/2511.00574"
pdf_url: "https://arxiv.org/pdf/2511.00574v2"
categories:
  - "cs.LG"
tags:
  - "Agent 推理"
  - "LLM 应用于 Agent 场景"
  - "知识表示与推理"
  - "数据合成/规划"
  - "贝叶斯网络"
relevance_score: 7.5
---

# Bayesian Network Structure Discovery Using Large Language Models

## 原始摘要

Understanding probabilistic dependencies among variables is central to analyzing complex systems. Traditional structure learning methods often require extensive observational data or are limited by manual, error-prone incorporation of expert knowledge. Recent studies have explored using large language models (LLMs) for structure learning, but most treat LLMs as auxiliary tools for pre-processing or post-processing, leaving the core learning process data-driven. In this work, we introduce a unified framework for Bayesian network structure discovery that places LLMs at the center, supporting both data-free and data-aware settings. In the data-free regime, we introduce \textbf{PromptBN}, which leverages LLM reasoning over variable metadata to generate a complete directed acyclic graph (DAG) in a single call. PromptBN effectively enforces global consistency and acyclicity through dual validation, achieving constant $\mathcal{O}(1)$ query complexity. When observational data are available, we introduce \textbf{ReActBN} to further refine the initial graph. ReActBN combines statistical evidence with LLM by integrating a novel ReAct-style reasoning with configurable structure scores (e.g., Bayesian Information Criterion). Experiments demonstrate that our method outperforms prior data-only, LLM-only, and hybrid baselines, particularly in low- or no-data regimes and on out-of-distribution datasets.
  Code is available at https://github.com/sherryzyh/llmbn.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决贝叶斯网络结构学习中的核心挑战。贝叶斯网络是表示变量间概率依赖关系的强大工具，对于复杂系统分析至关重要。传统的结构学习方法主要依赖于大量的观测数据，在数据稀缺或昂贵的情况下性能受限。同时，虽然可以融入专家知识来指导学习，但这个过程通常是手动、耗时且容易出错的。近年来，大型语言模型（LLMs）展现出强大的世界知识和推理能力，已有研究尝试将其用于结构学习，但大多仅将LLMs作为数据预处理（如生成变量描述）或后处理（如解释结果）的辅助工具，其核心学习过程仍然是纯粹数据驱动的。因此，本文试图解决的关键问题是：如何更深入、更核心地利用LLMs的推理能力，构建一个统一的框架，使其能够在无数据和有数据两种场景下，主导或深度参与贝叶斯网络结构的发现过程，从而克服传统方法对大量数据的依赖，并更有效地整合先验知识。

### Q2: 有哪些相关研究？

相关研究主要分为三类：1）**传统贝叶斯网络结构学习**：包括基于约束的方法（如PC算法）、基于评分搜索的方法（如贪婪搜索、BIC评分）和混合方法。这些方法严重依赖观测数据的质量和数量。2）**融入领域知识的方法**：研究者尝试手动或半自动地将专家知识（如变量间的必然因果、禁止边）作为约束加入学习过程，但这需要专业知识且难以规模化。3）**利用LLMs进行结构学习的新兴研究**：这是最直接相关的工作。例如，一些研究使用LLMs为变量生成描述，然后计算文本相似度来推断关系；另一些则让LLMs判断成对变量间的条件独立性。然而，这些方法通常将LLM视为一个“特征提取器”或“成对关系分类器”，其输出（如相似度分数或边概率）仍需输入给传统的数据驱动算法进行全局结构组装，并未让LLM直接进行全局、一致的图结构推理。本文的工作与第三类研究密切相关，但关键区别在于，它提出了一个让LLM处于“中心”地位的框架，直接生成完整的DAG，并设计了新颖的机制来保证图的全局属性（如无环性），从而超越了将LLM作为辅助工具的范式。

### Q3: 论文如何解决这个问题？

论文提出了一个统一的框架，包含两种核心方法，分别对应无数据和有数据两种场景，均以LLM为核心。

1. **PromptBN（数据无关模式）**：这是框架的基础。给定一组变量及其元数据（如名称、描述），PromptBN旨在通过单次LLM调用直接生成一个完整的、无环的有向图（DAG）。其关键技术在于精心设计的提示工程和双重验证机制。提示会引导LLM以特定格式（如邻接表）输出整个图。为了确保输出质量，作者设计了“双重验证”：首先，提示本身要求LLM进行“自我验证”，检查输出图是否满足无环性等约束；其次，在收到LLM回复后，系统会进行“外部验证”，自动解析输出并检查其语法和结构一致性（如是否为有效DAG）。这种设计将全局一致性和无环性的保证内嵌到推理过程中，实现了O(1)的查询复杂度，效率极高。

2. **ReActBN（数据感知模式）**：当有观测数据可用时，该方法用于优化PromptBN生成的初始图。它结合了LLM推理和传统统计评分。其核心是受ReAct（推理-行动）范式启发的迭代优化过程。在每一轮，LLM会分析当前图结构、统计评分（如BIC分数）的变化以及数据证据，然后决定采取何种图编辑操作（如增加、删除、反转一条边）。这个过程将LLM的因果/领域推理能力与数据的统计证据动态结合。LLM不仅根据分数高低行动，还能理解分数变化背后的潜在原因（例如，分数下降可能是因为引入了虚假关联或违反了无环性），从而做出更合理的调整决策。这种混合方法允许用户在计算效率和准确性之间进行配置权衡。

### Q4: 论文做了哪些实验？

实验旨在全面评估所提框架的有效性，特别是在低数据和无数据场景下的表现。

**实验设置**：
- **基准方法**：对比了三类基线：1) **纯数据方法**：如PC（约束型）、GES（评分搜索型）。2) **纯LLM方法**：如基于LLM的成对关系查询（Pairwise-LLM），再通过传统方法组装成图。3) **混合方法**：如使用LLM生成先验知识再输入给数据驱动算法。
- **数据集**：使用了标准基准数据集（如ALARM、INSURANCE）以评估分布内性能，并创建了“分布外”数据集（通过修改真实网络或使用LLM模拟生成新领域变量关系）以测试泛化能力。
- **评估指标**：采用结构汉明距离（SHD，衡量与真实图的差异，越低越好）、精确率、召回率、F1分数等。
- **LLM**：主要使用GPT-4进行实验。

**主要结果**：
1. **在无数据/极低数据场景下**：PromptBN显著优于所有基线。纯数据方法因数据不足而失效；纯LLM成对方法由于缺乏全局一致性，组装出的图质量差。PromptBN通过单次全局推理，能产生结构合理且更接近真实图的DAG。
2. **在有数据场景下**：ReActBN在大多数情况下优于基线混合方法。它能够有效利用初始的LLM生成图作为“热启动”，再结合数据证据进行精细化调整，最终达到比从头开始的数据驱动方法或简单的LLM后处理方法更好的性能。
3. **分布外泛化**：在模拟的新领域问题上，本文方法展现了强大的泛化能力，因为LLM能够利用其内嵌的常识和因果知识进行推理，而传统数据方法完全无法处理未见过的变量关系。
4. **效率**：PromptBN的O(1)调用复杂度远低于需要进行O(n²)次成对查询的LLM基线。

### Q5: 有什么可以进一步探索的点？

论文的工作开辟了LLM主导的贝叶斯网络学习新方向，但仍存在一些局限和未来探索点：
1. **可扩展性**：当前方法处理变量数量较多（例如超过50个）的复杂网络时可能面临挑战。LLM的上下文窗口限制和单次生成超大图的可靠性需要进一步研究。可以探索分层或模块化的生成策略。
2. **对LLM知识质量和偏见的依赖**：PromptBN的性能高度依赖于LLM内部编码的知识的准确性和全面性。如果LLM对某个领域的知识存在偏见或错误，会直接导致错误的图结构。未来需要研究如何校准或验证LLM的“知识输出”，或许可以结合多模型查询或知识检索来增强可靠性。
3. **更复杂的先验与不确定性量化**：目前框架主要输出一个确定的图结构。未来的工作可以探索让LLM生成一个图的集合或对边存在的不确定性进行概率性评估，从而更好地反映认知的不确定性。
4. **与因果发现的深度融合**：贝叶斯网络通常关联因果发现。本文方法生成的边可以解释为因果假设。如何将LLM的推理与更严格的因果发现框架（如介入性因果）结合，是一个极具前景的方向。
5. **应用于更广泛的Agent场景**：本文聚焦于静态网络结构学习。在动态的、交互式的Agent（如机器人规划、多智能体协作）中，如何在线地、增量地利用此类方法进行世界模型学习，是一个重要的应用延伸。

### Q6: 总结一下论文的主要内容

本文提出了一种利用大型语言模型（LLM）进行贝叶斯网络结构发现的新型统一框架。其核心贡献在于将LLM从辅助工具提升为核心推理引擎，以应对传统方法对大量观测数据的依赖。框架包含两个主要方法：在无数据场景下，**PromptBN**通过精心设计的提示和双重验证机制，引导LLM单次调用即生成全局一致且无环的完整图结构，实现了极高的效率（O(1)查询复杂度）。在有数据场景下，**ReActBN**进一步引入一个结合推理与行动的迭代优化过程，将LLM的因果推理能力与数据的统计证据（如BIC分数）动态融合，对初始图进行精细化调整。实验表明，该框架在低数据、无数据以及分布外泛化任务上，均显著优于传统的纯数据方法、纯LLM成对方法以及简单的混合基线。这项工作标志着贝叶斯网络学习范式的重要转变，为构建更加数据高效、知识可融合的复杂系统分析工具提供了新思路，并在Agent的模型构建与推理能力增强方面具有直接的应用潜力。
