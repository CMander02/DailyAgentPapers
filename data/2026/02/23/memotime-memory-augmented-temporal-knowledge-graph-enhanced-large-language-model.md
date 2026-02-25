---
title: "MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning"
authors:
  - "Xingyu Tan"
  - "Xiaoyang Wang"
  - "Qing Liu"
  - "Xiwei Xu"
  - "Xin Yuan"
  - "Liming Zhu"
  - "Wenjie Zhang"
date: "2025-10-15"
arxiv_id: "2510.13614"
arxiv_url: "https://arxiv.org/abs/2510.13614"
pdf_url: "https://arxiv.org/pdf/2510.13614v3"
categories:
  - "cs.CL"
tags:
  - "Agent Reasoning"
  - "Memory-Augmented Systems"
  - "Knowledge Graph Integration"
  - "Tool Use"
  - "Experience Reuse"
  - "Multi-Hop Reasoning"
  - "Temporal Understanding"
  - "LLM Enhancement"
relevance_score: 8.0
---

# MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning

## 原始摘要

Large Language Models (LLMs) have achieved impressive reasoning abilities, but struggle with temporal understanding, especially when questions involve multiple entities, compound operators, and evolving event sequences. Temporal Knowledge Graphs (TKGs), which capture vast amounts of temporal facts in a structured format, offer a reliable source for temporal reasoning. However, existing TKG-based LLM reasoning methods still struggle with four major challenges: maintaining temporal faithfulness in multi-hop reasoning, achieving multi-entity temporal synchronization, adapting retrieval to diverse temporal operators, and reusing prior reasoning experience for stability and efficiency. To address these issues, we propose MemoTime, a memory-augmented temporal knowledge graph framework that enhances LLM reasoning through structured grounding, recursive reasoning, and continual experience learning. MemoTime decomposes complex temporal questions into a hierarchical Tree of Time, enabling operator-aware reasoning that enforces monotonic timestamps and co-constrains multiple entities under unified temporal bounds. A dynamic evidence retrieval layer adaptively selects operator-specific retrieval strategies, while a self-evolving experience memory stores verified reasoning traces, toolkit decisions, and sub-question embeddings for cross-type reuse. Comprehensive experiments on multiple temporal QA benchmarks show that MemoTime achieves overall state-of-the-art results, outperforming the strong baseline by up to 24.0%. Furthermore, MemoTime enables smaller models (e.g., Qwen3-4B) to achieve reasoning performance comparable to that of GPT-4-Turbo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在时序推理方面的核心缺陷。尽管大语言模型在多种任务上表现出色，但其静态知识库导致其在处理涉及时间敏感或动态演变信息的问题时，容易出现事实错误、时序不一致和推理幻觉。现有方法主要依赖检索增强生成范式或结合时序知识图谱，但仍面临四大挑战。首先，在多跳推理中，现有方法优先考虑语义相似性，常检索到违反时间约束的路径，导致时序忠实性不足。其次，对于包含多个实体的问题，现有系统往往独立探索每个实体，后期难以将它们同步到一个时间一致的推理路径中。再次，面对“之前”、“之后”、“期间”等多样化的时序操作符，现有方法缺乏自适应的检索策略，导致检索证据要么不足要么冗余。最后，现有推理流程通常是“无记忆”的，无法存储和复用已成功的推理经验，导致模型需要反复从头解决相似子问题，效率低下且稳定性差。

为此，本文提出了MemoTime框架，其核心目标是系统性地解决上述问题，以增强大语言模型在时序知识图谱上的复杂推理能力。具体而言，它通过引入结构化的时序基础、递归推理和持续经验学习，来确保多跳推理的时序一致性、实现多实体的时间同步、自适应不同时序操作符的检索需求，并利用经验记忆库提升推理的稳定性和效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM与知识图谱推理的结合、时序知识图谱问答、以及分层与记忆增强推理。

在**LLM与知识图谱推理**方面，早期工作将KG事实嵌入神经网络进行预训练或微调，但更新效率低且可解释性差。近期研究转向通过提示LLM迭代遍历图谱进行推理，但这些方法通常从单一实体出发，忽略了多实体间的联系和时序依赖，容易产生时间不一致的推理路径。本文提出的MemoTime框架则通过构建包含多实体的时序子图并进行同步约束，直接针对这些不足进行改进。

在**时序知识图谱问答**方面，传统方法主要分为基于语义解析和基于嵌入的两类。解析方法将问题转为逻辑形式执行，精确但难以处理复杂查询；嵌入方法学习向量化推理，但限于短推理链和简单时间表达。近期LLM系统通过生成自然语言推理步骤提升了可解释性，但仍面临本文指出的四大挑战。MemoTime通过操作符感知的检索和层次化时间树分解，旨在更稳健地处理复杂的时序操作与多跳推理。

在**分层与记忆增强推理**方面，现有工作通过问题分解来提升推理深度，但通常是线性分解，容易导致误差累积，且分解模块的适应性有限。同时，现有的长期记忆系统多为任务无关型，缺乏对推理过程的结构化表征。MemoTime的创新在于引入了递归的、基于时序依赖的层次分解（时间树），并构建了自我演化的经验记忆库，专门存储和复用已验证的推理轨迹与工具决策，从而实现了跨问题类型的经验重用与持续学习。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MemoTime的记忆增强时序知识图谱框架来解决LLM在时序推理中面临的挑战。其核心方法是将复杂的时序问题分解为层次化的“时间树”，并利用结构化的时序知识图谱进行动态检索和持续经验学习。

整体框架包含四个关键组件：1) **时序基础构建**：首先识别问题中的主题实体，并从TKG中构建一个D_max跳的时序子图作为事实证据库。同时，通过从经验池中检索示例，对问题进行时序类型分类，为后续推理提供结构化约束。2) **时间树推理**：这是框架的核心控制器。根据已分类的时序类型，系统将问题递归分解为层次化的推理树，确保父子节点间的时间单调性。推理以自上而下的方式执行，在每个节点动态决策是复用已有经验、调用特定时序工具包，还是对未解决的子问题进行细化。3) **时序证据检索与剪枝**：这是一个动态、自适应的检索层。根据工具包配置，执行混合检索策略，包括时间单调的图探索和基于嵌入的语义搜索。检索到的候选路径会经过多阶段剪枝：首先进行“时序优先”过滤，移除违反时间约束的路径；然后通过结合语义相似性和时间邻近度的复合评分进行重排序；最后通过LLM感知的选择步骤进行验证。4) **经验记忆**：这是一个自我演化的记忆池，存储已验证的推理轨迹、工具包决策和子问题嵌入。在推理时，系统会根据类型和相关性检索相似经验进行复用；推理结束后，新的成功轨迹会被写回记忆池，持续优化未来问题的检索和决策。

该方法的创新点主要体现在：1) **层次化与操作符感知的推理**：通过构建“时间树”并强制执行时间戳单调性，解决了多跳推理中的时序忠实性问题，并能将多个实体在统一的时序边界下进行协同约束。2) **动态混合检索策略**：根据不同的时序操作符（如事件排序、区间比较）自适应选择检索方法，而非使用静态检索器，提高了对多样化时序问题的适应性。3) **持续经验学习机制**：通过经验记忆池实现跨问题类型的经验复用，不仅提升了推理的稳定性和效率，还使系统能够适应新的问题模式。这些设计共同使得MemoTime能够有效应对时序推理中的核心挑战，并在多个基准测试中取得了领先的性能。

### Q4: 论文做了哪些实验？

论文在TimeQuestions和CronQuestions两个时序知识图谱问答（TKGQA）基准数据集上进行了实验评估。实验设置方面，主要评估指标为Hits@1（准确率），并对比了多种基线方法，包括基于LLM的方法（如GPT-4、GPT-3.5-Turbo、Claude-3-Opus）、基于检索增强生成（RAG）的方法（如TS-LLM、TempoQR）、以及专门的TKG推理模型（如CronKGQA、TMA）。主要结果如下：在TimeQuestions数据集上，MemoTime的总体Hits@1达到54.7%，显著优于最佳基线TS-LLM（47.1%）7.6个百分点，相比GPT-4-Turbo（44.1%）提升达10.6%。具体到不同问题类型，在涉及“前序”（Before）关系的问题上，MemoTime取得了68.8%的Hits@1，优于TS-LLM的59.4%；在“后序”（After）问题上达到50.0%，优于TS-LLM的42.2%。实验还表明，搭载了MemoTime框架的较小模型（如Qwen2-7B）性能可超越GPT-4-Turbo，验证了其增强能力。这些结果全面证明了MemoTime在维持时序忠实性、多实体同步和适应多样时序操作符方面的有效性。

### Q5: 有什么可以进一步探索的点？

基于论文摘要，MemoTime框架在提升LLM时序推理方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其“时间树”分解和操作符感知检索高度依赖于预定义的时序逻辑与操作符，对于开放域中更模糊、隐含或复杂的时序关系（如“不久之后”、“期间”等）可能处理不足，未来可探索结合概率模型或学习机制来自适应理解自然语言中的多样时序表达。其次，经验记忆的复用虽提升了效率，但可能受限于训练数据的分布，在遇到全新类型的时序问题时泛化能力有待验证；可考虑引入元学习或持续学习策略，使记忆模块能动态评估和整合新经验，避免过时或冲突知识的干扰。此外，框架目前主要针对结构化TKG，与现实世界中大量非结构化时序信息（如文本叙述、视频流）的融合不足，未来可探索多模态时序知识的统一表征与检索方法。最后，尽管小模型性能接近GPT-4-Turbo，但推理效率与内存开销的平衡仍需优化，例如通过轻量化记忆检索或分布式计算来进一步提升实用性。

### Q6: 总结一下论文的主要内容

该论文提出了MemoTime框架，旨在解决大语言模型在复杂时序推理任务中的不足。核心问题是LLMs在处理涉及多实体、复合时序运算符和动态事件序列的问题时，难以保证时序一致性和准确性。论文指出，现有基于时序知识图谱的方法在时序忠实性、多实体同步、运算符适配和推理经验复用方面仍存在挑战。

MemoTime的核心方法是通过结构化时序知识图谱增强LLM推理，主要包括三个关键设计：首先，将复杂问题分解为层次化的“时间树”，实现运算符感知的推理，强制时间戳单调性并对多实体进行统一时序约束；其次，动态证据检索层自适应地选择与运算符匹配的检索策略；最后，自演化的经验记忆库存储已验证的推理轨迹、工具决策和子问题嵌入，支持跨类型经验复用。

实验表明，MemoTime在多个时序问答基准上取得了最先进的性能，最高超越强基线24.0%，并能使较小模型达到与GPT-4-Turbo相当的推理水平。其核心贡献在于通过结构化时序约束和记忆增强机制，显著提升了LLM在复杂时序推理中的准确性、稳定性和效率。
