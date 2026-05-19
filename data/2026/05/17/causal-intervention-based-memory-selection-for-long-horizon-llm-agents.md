---
title: "Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents"
authors:
  - "Saksham Sahai Srivastava"
date: "2026-05-17"
arxiv_id: "2605.17641"
arxiv_url: "https://arxiv.org/abs/2605.17641"
pdf_url: "https://arxiv.org/pdf/2605.17641v1"
github_url: "https://github.com/Saksham4796/causal-memory-intervention"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Memory Selection"
  - "Causal Intervention"
  - "Long-Horizon Agent"
  - "Benchmark"
  - "Causal Reasoning"
  - "Robustness"
  - "Retrieval"
relevance_score: 9.0
---

# Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents

## 原始摘要

Long-horizon LLM agents rely on persistent memory to support interactions across sessions, yet existing memory systems often retrieve context using semantic similarity or broad history inclusion, treating retrieved memories as uniformly useful. This assumption is fragile because memories may be topically related while remaining irrelevant, stale, or misleading. We propose Causal Memory Intervention (CMI), a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. To evaluate this setting, we introduce Causal-LoCoMo, a causally annotated benchmark derived from long conversational data, where each example contains a user request, a structured memory bank, useful memories, irrelevant distractors, and synthetic harmful memories. We compare CMI against vector, graph, reflection, summary, full-history, and no-memory baselines. Results show that CMI achieves a stronger balance between answer quality and robustness to misleading memory, suggesting that reliable long-term memory requires selecting context based on causal usefulness rather than relevance alone. The full framework, benchmark construction code, and experimental pipeline are available at https://github.com/Saksham4796/causal-memory-intervention.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长时域LLM代理在记忆选择中的核心问题：现有记忆系统通常基于语义相似性或历史范围来检索上下文，并默认检索到的记忆都是有用的。然而，这种假设存在缺陷，因为记忆虽然在主题上相关，但可能包含无关、过时、误导甚至有害的信息。研究背景是LLM代理需要在跨会话的长期交互中依赖持久记忆，但现有方法如基于向量、图、反思、摘要或全历史检索的系统，都未能区分真正有用和仅仅相关或有害的记忆。论文的核心问题是：如何从候选记忆中选择那些对当前回答有正面因果效应的记忆，同时抑制不稳定、无关或有害的记忆。为此，本文提出因果记忆干预（Causal Memory Intervention, CMI），一种估计候选记忆在受控干预下对模型回答影响的技术，将记忆选择重新定义为基于干预的决策问题，而非纯粹基于相似性的检索问题。同时，本文还构建了因果标注基准Causal-LoCoMo，以评估记忆选择的质量。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**长时记忆与智能体系统**、**长上下文评测基准**和**检索增强生成（RAG）及鲁棒性**。

在**智能体记忆系统**方面，相关工作包括Generative Agents、Reflexion、MemoryBank、MemGPT和Voyager等，它们通过反思、反馈或系统化存储来增强智能体的持续性。这些工作通常假设检索到的记忆天然有用，而本文则直接研究问题：在包含噪声的记忆库中，应选择哪些记忆用于当前任务，并强调因果有用性而非仅相关性。

在**长上下文评测**方面，LoCoMo、LongBench、L-Eval、InfiniteBench和RULER评估模型从长输入或历史中恢复信息的能力。但这些基准通常测试模型是否能在给定上下文中作答。本文提出的Causal-LoCoMo则将长对话QA转化为明确的记忆选择场景，分离出有用、无关和有害记忆，从而评估智能体在回答前选择正确记忆的能力。

在**RAG与鲁棒性**方面，密集检索和生成式架构面临证据可能语义相关但无关或误导的问题，尤其在持久记忆库中更为严重。此外，提示注入和RAG投毒等工作表明，恶意记忆会破坏智能体鲁棒性。本文提出的因果记忆干预（CMI）与这些工作不同，它通过估计候选记忆对当前答案的因果效应进行排序，并主动抑制不稳定或有害记忆，而非仅基于语义相似度检索。该方法在推理时干预外部记忆输入，与因果中介分析等内部干预方法互补。

### Q3: 论文如何解决这个问题？

CMI通过将记忆选择建模为因果干预问题来解决长时程LLM智能体中的不可靠记忆检索问题。其核心思想是：记忆的有用性不取决于与查询的语义相似度，而取决于其是否对模型答案产生正向因果效应。

整体框架包含三个模块。第一，候选记忆生成器：使用混合检索器从持久记忆库中初步筛选与当前请求可能相关的候选记忆，这一阶段故意保持宽泛以覆盖潜在有用记忆。第二，因果干预评分模块：对每个候选记忆执行三种受控条件测试——无记忆基线（无上下文）、有记忆条件（包含该记忆）和扰动记忆条件（包含该记忆的扰动版本）。通过比较三种条件下的任务得分，计算两个关键指标：效用值（有记忆得分减无记忆得分）衡量记忆是否改善答案，稳定性值（有记忆得分减扰动记忆得分）衡量改善是否稳健。第三，最终选择与生成模块：仅保留同时满足效用值大于零且稳定性值非负的记忆，再将这些记忆作为上下文输入响应模型生成最终答案。

关键技术创新包括：用因果效应替代语义相似度作为选择标准，引入扰动测试作为稳健性检查机制，以及使用非参数任务评分器进行效率评估。CMI能抑制语义相关但实际有害或误导的记忆，在保持答案质量的同时提升对误导性记忆的鲁棒性，在因果标注基准Causal-LoCoMo上优于向量、图、摘要等基线方法。

### Q4: 论文做了哪些实验？

论文在自建的Causal-LoCoMo基准上进行了实验，该基准包含87个源自LoCoMo的示例，涵盖时间、多证据、推理和事实记忆QA四类任务。对比方法包括无记忆、全历史、摘要记忆、向量记忆、图记忆、反思记忆以及提出的CMI。所有方法共享GPT-4.1作为响应模型，GPT-5作为评判模型，并使用混合任务分数（0.7确定性分数+0.3 GPT-5评判分数）评估答案质量，同时报告成功率和多项记忆选择指标。

主要结果显示：CMI在任务分数（0.846）和成功率（0.816）上均最高，并取得了最优的有用记忆F1（0.875）、近乎完美的坏记忆拒绝率（0.990）和零有害记忆采纳率。反思记忆和向量记忆的任务分数接近（0.845和0.839），但采纳有害记忆率远高于CMI（分别为0.540和0.609）。按任务划分，CMI在多证据QA（0.754）和事实QA（0.985）上表现最佳，在时间QA和推理QA上略低于最佳基线。该实验还通过干预诊断验证了CMI选择记忆的因果有效性：有用记忆的平均效用为+0.307，而无关和有害记忆的效用分别为-0.009和-0.033。

### Q5: 有什么可以进一步探索的点？

该论文在受控标注环境下验证了因果干预记忆选择的有效性，但仍存在若干可深入探索的方向。首先，当前方法依赖人工标注的记忆角色标签（如有用/有害），未来应探索如何让模型从原始记忆中自主推断因果效用，例如通过训练一个因果预测模块来替代金标准标签。其次，实验结果揭示因果干预主要在需要综合多证据的复杂问题上优势明显，但在表面线索充分的时间问答任务中不及向量检索，因此可尝试将因果选择与语义检索进行混合或分层融合，以兼顾不同场景的需求。此外，论文中的因果效用评估基于确定性任务分数，未来可扩展至开放生成任务的因果效用估计，并引入对抗性噪声或分布偏移来检验方法的鲁棒性。最后，可探索将因果记忆选择与记忆更新、遗忘机制结合，形成动态、自适应的长期记忆系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向长期交互LLM Agent的因果记忆选择方法Causal Memory Intervention（CMI）。现有记忆系统通常基于语义相似度或历史覆盖检索上下文，错误地将所有检索到的记忆视为同等有用，导致模型可能受主题相关但无关、过时或误导性记忆的干扰。CMI通过受控干预估计候选记忆对模型答案的影响，从而选择能提升任务性能的记忆，抑制不稳定或有害的记忆。为评估该方法，作者构建了因果标注基准Causal-LoCoMo，包含用户请求、结构化记忆库、有用记忆、无关干扰项和合成的有害记忆。实验对比了向量检索、图记忆、反思、摘要、全历史和无记忆等基线方法。结果表明，CMI在答案质量和抵抗误导记忆的鲁棒性之间取得了更优平衡，说明可靠的长时记忆应基于因果有用性而非仅相关性选择上下文。该工作为Agent长期记忆系统的设计提供了新的理论基础。
