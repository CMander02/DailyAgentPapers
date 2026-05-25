---
title: "DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA"
authors:
  - "Jianing Yin"
  - "Tan Tang"
date: "2026-05-21"
arxiv_id: "2605.22411"
arxiv_url: "https://arxiv.org/abs/2605.22411"
pdf_url: "https://arxiv.org/pdf/2605.22411v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "长期记忆"
  - "证据精炼"
  - "强化学习"
  - "检索增强生成"
  - "LLM Agent"
  - "问答系统"
relevance_score: 9.0
---

# DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

## 原始摘要

Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query. This workflow leaves downstream answerers to denoise retrieved candidates and reconstruct query-specific evidence. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. DeferMem uses a lightweight segment-link structure to organize raw history and retrieve broad candidates at query time. It then applies a memory distiller trained with DistillPO, our reinforcement learning algorithm for distilling the high-recall but highly noisy candidates into a set of faithful, self-contained, and query-conditioned evidence. DistillPO formulates post-retrieval evidence distillation as a structured action comprising message selection and evidence rewriting. It optimizes this action with a decomposed-and-gated reward pipeline and structure-aligned advantage assignment, gating reward components from validity to quality checks while exposing task-level correctness feedback early and assigning each reward to its responsible output span. On LoCoMo and LongMemEval-S, DeferMem surpasses strong baselines in QA accuracy and memory-system efficiency, achieving the highest QA accuracy with the fastest runtime and zero commercial-API token cost for memory operations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长期记忆问答系统中存在的关键瓶颈问题。研究背景是，大语言模型（LLM）智能体在长期交互中需要依赖外部记忆系统来存储和检索过往信息，以回答未来的查询。然而，现有方法存在显著不足：首先，大多数记忆系统在查询到来之前，就通过压缩、遗忘或更新机制对原始对话历史进行“写入时”组织。这种查询无关的预处理方式，可能会丢弃或模糊对未来查询至关重要的细节。其次，即使保留了原始历史，在“查询时”的检索阶段，现有系统通常只依赖嵌入相似度或关键词重叠等间接相关性线索，而非根据它们对回答当前问题的实际效用。这导致检索结果中通常包含大量噪声，有用的证据被淹没，且检索到的候选内容粒度粗于直接可用的证据，迫使下游的问答模型必须自行去噪和提炼证据。因此，本文的核心问题是：如何在保留高召回率候选集的前提下，有效且高效地将这些嘈杂的候选信息，蒸馏为一组忠实、自包含且面向特定查询的精确证据。论文提出的DeferMem框架通过将问题解耦为高召回率候选检索与查询条件化证据蒸馏两个阶段，并使用强化学习（DistillPO）来训练一个专门的蒸馏器，以解决这一瓶颈。

### Q2: 有哪些相关研究？

首先，在**记忆系统**方面，相关工作主要聚焦于设计专门的存储结构（如图、摘要、笔记、语义片段等）和引入压缩、遗忘与更新机制。然而，这些方法在查询时通常基于嵌入相似度、关键词等信号进行检索，获取的是与查询相似而非对回答有用的候选内容。DeferMem 指出，这类信号会返回噪声较大的候选记忆，并将证据精炼的负担转嫁给下游模型。与之对比，DeferMem 通过“延迟处理”策略，在查询阶段进行高召回率候选检索，再通过强化学习训练的蒸馏器将噪声候选转化为查询相关且自包含的证据，将证据精炼的任务纳入记忆系统本身。

其次，在**强化学习（RL）** 方面，近期研究已将 RL 应用于推理、工具使用等任务，但用于长时记忆利用的工作尚不充分。已有的记忆导向 RL 方法主要被形式化为从预定义记忆池中选择相关项，而非对噪声候选进行证据蒸馏。DeferMem 提出的 DistillPO 算法则开创性地将 RL 用于证据提炼，通过结构化的消息选择与改写动作，以及分解式门控奖励和结构对齐的基线分配，从而优化了查询条件下的证据生成。

综上所述，DeferMem 的核心创新在于将记忆系统的职责从简单的检索扩展为主动的证据蒸馏，并利用 RL 解决了这一新任务的优化问题。

### Q3: 论文如何解决这个问题？

DeferMem通过将长期记忆问答解耦为高召回候选检索和查询条件证据蒸馏两个阶段来解决证据稀疏分散的问题。整体框架包含两个核心模块：一是基于分段链接结构的检索器，二是使用DistillPO强化学习算法训练的记忆蒸馏器。

在检索阶段，DeferMem构建了轻量级的分段链接结构来组织原始历史记录。具体包括三个层次：首先通过注意力分数和语义相似度将连续消息划分为语义连贯的片段；然后根据片段间语义相似度构建跨越历史的链接；最后建立消息级索引。查询时通过top-k消息匹配并扩展至包含的片段和链接片段，实现高召回但含噪的候选集检索。

核心创新在于记忆蒸馏器。它将后检索蒸馏建模为结构化动作，包含消息选择和证据重写两部分。DistillPO算法采用分解门控奖励管道，将奖励分解为8个可验证组件，涵盖输出格式、消息选择、证据质量和下游答案正确性。通过分层门控策略，在保持依赖关系的同时，让可回答性奖励尽早生效。结构对齐的利得分配机制分别为选择和证据跨度计算独立利得，确保优化信号精确作用于相应输出部分。此外，全奖励锚定补全策略稳定了组相对优化过程，使蒸馏器能从高噪声候选中生成忠实、自包含且查询条件化的证据。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongMemEval-S两个长期记忆问答数据集上进行了实验，代理需要从包含稀疏、碎片化证据的冗长对话历史中回答问题。对比方法包括三组：FullText（直接提供全部历史）和NaiveRAG（检索top消息）；代表性记忆系统如Mem0、A-Mem、MemoryOS、MemGAS、LightMem、GAM；以及基于强化学习的Memory-R1。主要指标为准确率（由GPT-4o-mini评判）和效率（token成本与运行时间）。核心结果：DeferMem在LongMemEval-S上达到70.0%准确率，优于最强基线LightMem（68.64%），且运行时间仅90.30秒（LightMem为283.76秒，3.1倍加速），token成本为0。在LoCoMo上，DeferMem在非对抗和对抗问题上分别达到88.25%和97.09%准确率，对抗问题比最强基线高6.28个百分点，运行时间83.56秒（比LightMem快9.8倍）。剔除训练用对话后，准确率仍为87.90%/96.99%。消融实验显示，去掉蒸馏器导致准确率下降5.82/8.00个百分点；使用基础模型或SFT/DAPO训练均显著低于DistillPO；移除DistillPO组件（奖励管道、结构对齐优势分配）也导致性能下降。此外，段-链接检索器在多种阈值设置下保持近饱和召回（约98-99%），而候选集大小可调。在长历史场景（LongMemEval-M）下，DeferMem仍保持合理性能（63.0%准确率）。

### Q5: 有什么可以进一步探索的点？

首先，DeferMem的训练依赖于模拟对话数据集，这可能导致在真实、开放域长对话中泛化能力不足，因为模拟数据难以涵盖用户提问的多样性及信息噪声的复杂模式。未来可探索利用在线强化学习，让模型在真实交互中持续优化证据蒸馏策略。

其次，DistillPO中的奖励函数虽已分解，但其有效性高度依赖于手工设计的规则（如忠实性、自包含性检查），这些规则可能无法捕捉所有细微的问答需求。未来可引入更灵活的判别器或基于人类反馈的奖励模型，自动学习更精确的证据质量评估标准。

此外，DeferMem的“先检索后蒸馏”流程虽高效，但本质上是两阶段独立优化。一个值得探索的方向是端到端的联合训练，让检索器和蒸馏器通过共享梯度相互反馈，使检索结果更直接服务于下游答案生成，从而减少噪声累积。

最后，当前框架主要关注单轮证据提取，对于需要多步推理、依据多个分散证据片段进行综合回答的复杂长程问题，其表现有待验证。未来可扩展为迭代式或多轮证据蒸馏，以处理更复杂的推理链条。

### Q6: 总结一下论文的主要内容

《DeferMem》提出了一种长期记忆问答框架，解决大语言模型代理在长对话历史中定位分散证据的难题。现有系统在查询未知时预处理记忆，导致检索结果噪声大且缺乏查询针对性。DeferMem将问题分解为高召回候选检索和查询条件证据蒸馏两个阶段：通过轻量级片段-链接结构在查询时检索广泛候选，再基于强化学习算法DistillPO训练记忆蒸馏器，将高召回但高噪声的候选转化为忠实、自包含且针对查询的证据。DistillPO将蒸馏建模为消息选择与改写构成的结构化动作，采用分解门控奖励管道和结构对齐优势分配，按输出跨度分配奖励以优化质量。在LoCoMo和LongMemEval-S基准上，DeferMem在问答准确率、运行时间和零API成本方面全面超越强基线，证明了查询时证据蒸馏作为可训练组件能有效提升长期记忆系统的精度与效率。
