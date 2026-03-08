---
title: "According to Me: Long-Term Personalized Referential Memory QA"
authors:
  - "Jingbiao Mei"
  - "Jinghong Chen"
  - "Guangyu Yang"
  - "Xinyu Hou"
  - "Margaret Li"
date: "2026-03-02"
arxiv_id: "2603.01990"
arxiv_url: "https://arxiv.org/abs/2603.01990"
pdf_url: "https://arxiv.org/pdf/2603.01990v1"
github_url: "https://github.com/JingbiaoMei/ATM-Bench"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
tags:
  - "Memory & Context Management"
  - "Benchmark/Evaluation"
relevance_score: 7.5
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Benchmark/Evaluation"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Schema-Guided Memory (SGM)"
  primary_benchmark: "ATM-Bench"
---

# According to Me: Long-Term Personalized Referential Memory QA

## 原始摘要

Personalized AI assistants must recall and reason over long-term user memory, which naturally spans multiple modalities and sources such as images, videos, and emails. However, existing Long-term Memory benchmarks focus primarily on dialogue history, failing to capture realistic personalized references grounded in lived experience. We introduce ATM-Bench, the first benchmark for multimodal, multi-source personalized referential Memory QA. ATM-Bench contains approximately four years of privacy-preserving personal memory data and human-annotated question-answer pairs with ground-truth memory evidence, including queries that require resolving personal references, multi-evidence reasoning from multi-source and handling conflicting evidence. We propose Schema-Guided Memory (SGM) to structurally represent memory items originated from different sources. In experiments, we implement 5 state-of-the-art memory systems along with a standard RAG baseline and evaluate variants with different memory ingestion, retrieval, and answer generation techniques. We find poor performance (under 20\% accuracy) on the ATM-Bench-Hard set, and that SGM improves performance over Descriptive Memory commonly adopted in prior works. Code available at: https://github.com/JingbiaoMei/ATM-Bench

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个性化AI助手在理解和利用用户长期、多模态、多来源记忆时所面临的挑战。当前的研究背景是，AI助手需要能够回忆和推理用户的长期记忆，这些记忆天然地跨越多种模态（如文本、图像、视频）和来源（如照片、电子邮件）。然而，现有的长期记忆基准测试主要集中于对话历史，未能捕捉基于真实生活经历的个性化指代信息，这限制了AI助手在现实场景中的应用能力。

现有方法的不足主要体现在两个方面：一是现有的记忆问答基准缺乏对多模态、多来源个人记忆数据的覆盖，忽略了静态数据源（如带有时间和地点信息的照片）所蕴含的丰富上下文；二是它们未能充分处理复杂的个性化指代问题，例如理解“我在日本旅行时给妈妈买的礼物”这类需要综合个人经历才能解析的查询。因此，当前最先进的系统在应对这类现实且复杂的查询时，其性能表现尚不明确。

本文要解决的核心问题是：如何构建一个能够评估AI系统在长期、多模态、多来源记忆背景下，处理个性化指代问答能力的基准。为此，论文引入了ATM-Bench，这是首个针对多模态、多来源个性化指代记忆问答的基准测试。它包含了约四年的隐私保护个人记忆数据及人工标注的问题-答案对，其中涉及需要解析个人指代、进行多证据推理以及处理冲突证据的挑战性查询。同时，论文提出了模式引导记忆（SGM）的结构化表示方法来处理不同来源的记忆项，并通过实验揭示了现有系统在ATM-Bench-Hard集上性能不足（准确率低于20%），验证了SGM相对于传统描述性记忆方法的改进效果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**智能体架构与记忆管理方法**、**个性化与长期记忆评测基准**以及**检索增强生成（RAG）技术**。

在**方法类**研究中，早期工作如Toolformer和ReAct让语言模型使用工具并交织推理。后续框架引入了记忆流和反思机制以维持长期一致性，但反思多作为启发式过程。更结构化的方法包括Voyager的技能库、HiAgent和MindRef的分层工作记忆，以及SeCom等构建动态条件记忆的个性化代理。本文提出的Schema-Guided Memory（SGM）属于此类，旨在结构化表示多源记忆，区别于以往工作中常用的描述性记忆。

在**评测类**研究中，现有基准大多专注于基于对话历史的文本记忆评估，如LongMemEval、LoCoMo、MemoryBank和PerLTQA。近期开始探索多模态记忆，如OmniQuery和Memory-QA，但它们主要评估显式视觉检索或单一媒体源。本文的ATM-Bench与这些工作的核心区别在于，它首次专注于**多源**（如图像、视频、电子邮件）**多模态**的个性化指代记忆问答，强调对具有明确时空 grounding 的异构个人记忆进行证据聚合和指代推理。

在**应用技术类**中，RAG是知识密集型生成的标准方法，并已发展为迭代式、代理式工作流。然而，个性化指代推理的查询往往定义不明确且依赖隐式线索，这与标准QA不同。本文的工作正是要评估这种需要跨异构个人记忆数据进行检索和推理的复杂任务，填补了现有评估多局限于单一源（如对话历史或媒体库）的空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个模块化的个人记忆助手框架来解决多模态、多来源的长期个性化参考记忆问答问题。该框架包含三个核心步骤：记忆摄取、检索和答案生成，并引入了创新的模式引导记忆表示方法。

在整体架构上，系统首先进行**记忆摄取**，将原始异构的个人数据（如图像、视频、邮件）转化为标准化的记忆存储。这一步骤细分为预处理和组织两个环节。预处理是关键创新点，论文对比了两种记忆表示方法：一种是先前工作中常用的**描述性记忆**，即将每个记忆项转化为一段自然语言描述文本；另一种是本文提出的**模式引导记忆**，它将每个记忆项表示为遵循固定模式的一组键值对字段（如时间、地点、实体、OCR文本、标签等）。SGM通过结构化的方式统一了不同来源的记忆，便于后续的精确检索和推理。在组织环节，系统可选择将记忆项以“堆叠”方式简单存储，或构建**链接记忆**，即利用大语言模型推断记忆项之间的关系，形成图结构，以支持更复杂的关联检索。

接下来是**检索**模块。给定用户查询，系统使用基于嵌入的相似性搜索。查询和记忆项（无论是DM还是SGM表示）都被编码到共享的向量空间中，通过最大内积搜索返回与查询最相关的前k个记忆项作为证据集。

最后是**答案生成**模块。论文比较了两种范式：一种是**单次通过**的答案生成器，直接根据查询和检索到的证据一次性生成最终答案；另一种是**智能体式**的答案生成器，它进行迭代推理，包括规划、分解查询，以及在证据不足时重写查询以进行额外检索，然后再生成最终答案。

综上所述，论文的核心解决方案是一个清晰的三阶段流水线，其最主要的创新在于提出了**模式引导记忆**这种结构化的记忆表示方法，以替代传统的纯文本描述，旨在更有效地处理多源异构的个人记忆数据，并通过模块化设计支持对不同记忆表示、检索和生成技术进行受控的消融实验。

### Q4: 论文做了哪些实验？

论文在自建的ATM-Bench基准上进行了全面的实验评估。实验设置方面，使用Qwen3-VL-2B-Instruct模型作为记忆处理器，统一处理多模态原始记忆数据；使用Qwen3-VL-8B-Instruct进行答案生成。检索默认使用all-MiniLM-L6-v2嵌入模型，并设置top-k=10的证据预算。评估指标包括整体QS分数、检索召回率（R@10）、联合指标（Joint@10）以及针对数字、回忆列表和开放式问题的分类准确率（N/R/O）。

数据集为论文提出的ATM-Bench及其更具挑战性的ATM-Bench-Hard子集，包含约四年的个人多模态记忆数据及人工标注的问答对。

对比方法包括：1）上/下界基线（无证据和Oracle）；2）记忆代理系统（A-Mem、Mem0的Agentic和Plain变体）；3）RAG系统（HippoRAG2、Self-RAG、ATM-RAG）。这些系统测试了不同的记忆表示（描述性记忆DM vs. 模式引导记忆SGM）和组织方式（堆叠Piled vs. 链接Linked）。

主要结果：1）所有系统在ATM-Bench-Hard上表现均不佳（准确率低于20%）。2）SGM表示法显著优于普遍采用的DM。在Oracle设置下，SGM在ATM-Bench-Hard上将QS分数从25.6提升至47.3（相对提升约85%）；在RAG系统中，使用SGM的系统（如ATM-RAG SGM）QS达到51.0，明显高于DM版本（42.0）。3）链接式与堆叠式记忆组织对比发现，堆叠式在保持性能的同时大幅降低了编码时间（如A-Mem从12.6小时降至1.6小时）。4）检索增强实验表明，扩大检索器嵌入模型规模（如使用Qwen3-4B）能提升性能，但纯视觉嵌入模型（Qwen3-VL-2B）效果较差，QS仅为31.3。5）在Oracle设置下评估不同答案生成模型，即使最佳模型（GPT-5）在ATM-Bench-Hard上的QS也仅为74.7，表明任务具有挑战性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其提出的Schema-Guided Memory（SGM）虽能结构化多源记忆，但可能过于依赖预设模式，难以灵活适应动态、开放的新记忆类型。同时，基准测试ATM-Bench-Hard的低准确率（低于20%）揭示了现有系统在解决复杂指代、多证据推理及冲突处理方面的严重不足，尤其是跨模态信息的深度融合与长期依赖建模能力薄弱。

未来研究方向可探索更自适应的记忆表示方法，如结合动态图神经网络或神经符号系统，以自动学习记忆间的语义关联。此外，可引入增量学习机制，使系统能持续更新并修正记忆，处理证据冲突。在推理层面，可研究多跳推理与因果推断技术，提升对隐含个人指代的解析能力。最后，需开发更高效的检索生成一体化框架，减少信息碎片化，并考虑隐私保护下的联邦学习方案，以推动个性化记忆系统的实际部署。

### Q6: 总结一下论文的主要内容

该论文针对个性化AI助手需处理长期、多模态、多来源用户记忆的挑战，提出了首个多模态多来源个性化指代记忆问答基准ATM-Bench。核心问题是现有记忆问答基准局限于对话历史，未能涵盖基于真实生活经历的个性化指代查询。论文将记忆问答任务形式化为记忆摄取、检索和答案生成三个步骤，并提出了结构化记忆表示方法Schema-Guided Memory（SGM），以统一处理不同来源和模态的记忆数据。实验评估了五种先进记忆系统及RAG基线，发现它们在挑战性数据集ATM-Bench-Hard上准确率不足20%，而SGM相比广泛采用的描述性记忆能显著提升性能。主要贡献包括：引入包含约四年隐私保护个人记忆数据及人工标注问答对的基准；建立了系统化的问题框架；验证了结构化记忆表示的有效性；揭示了当前系统在复杂个性化指代推理上的严重不足，为未来研究指明了方向。
