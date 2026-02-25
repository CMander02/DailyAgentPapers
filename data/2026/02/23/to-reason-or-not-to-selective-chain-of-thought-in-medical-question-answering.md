---
title: "To Reason or Not to: Selective Chain-of-Thought in Medical Question Answering"
authors:
  - "Zaifu Zhan"
  - "Min Zeng"
  - "Shuang Zhou"
  - "Yiran Song"
  - "Xiaoyi Chen"
  - "Yu Hou"
  - "Yifan Wu"
  - "Yang Ruan"
  - "Rui Zhang"
date: "2026-02-23"
arxiv_id: "2602.20130"
arxiv_url: "https://arxiv.org/abs/2602.20130"
pdf_url: "https://arxiv.org/pdf/2602.20130v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "推理优化"
  - "链式思维"
  - "医疗问答"
  - "效率提升"
  - "推理策略"
  - "模型部署"
relevance_score: 7.5
---

# To Reason or Not to: Selective Chain-of-Thought in Medical Question Answering

## 原始摘要

Objective: To improve the efficiency of medical question answering (MedQA) with large language models (LLMs) by avoiding unnecessary reasoning while maintaining accuracy.
  Methods: We propose Selective Chain-of-Thought (Selective CoT), an inference-time strategy that first predicts whether a question requires reasoning and generates a rationale only when needed. Two open-source LLMs (Llama-3.1-8B and Qwen-2.5-7B) were evaluated on four biomedical QA benchmarks-HeadQA, MedQA-USMLE, MedMCQA, and PubMedQA. Metrics included accuracy, total generated tokens, and inference time.
  Results: Selective CoT reduced inference time by 13-45% and token usage by 8-47% with minimal accuracy loss ($\leq$4\%). In some model-task pairs, it achieved both higher accuracy and greater efficiency than standard CoT. Compared with fixed-length CoT, Selective CoT reached similar or superior accuracy at substantially lower computational cost.
  Discussion: Selective CoT dynamically balances reasoning depth and efficiency by invoking explicit reasoning only when beneficial, reducing redundancy on recall-type questions while preserving interpretability.
  Conclusion: Selective CoT provides a simple, model-agnostic, and cost-effective approach for medical QA, aligning reasoning effort with question complexity to enhance real-world deployability of LLM-based clinical systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在医疗问答（MedQA）任务中应用链式思维（CoT）提示方法时面临的效率与准确性权衡问题。研究背景是，医疗问答既需要精确的事实性知识回忆，又需要复杂的多步临床推理。CoT通过让模型生成中间推理步骤再给出最终答案，显著提升了复杂问题的逻辑性和可解释性，已成为该领域的常用方法。然而，现有方法（即始终使用CoT）存在明显不足：对于大量仅需知识回忆即可直接回答的问题，强制生成冗长的推理过程会产生不必要的计算开销，包括更多的输出令牌、更高的延迟以及更大的计算成本，这严重影响了LLM在现实临床部署环境（如教育平台或决策支持系统）中的吞吐量和响应性。

因此，本文要解决的核心问题是：如何在不牺牲（甚至提升）准确性的前提下，动态地、有选择地应用CoT推理，从而显著提升医疗问答系统的推理效率与成本效益。具体而言，论文提出了“选择性链式思维”（Selective CoT）这一推理时策略。该策略的核心思想是让模型首先自行预测当前问题是否需要显式推理，仅当判断为需要时，才生成推理依据（rationale）再作答；否则，直接给出答案。这样，系统能够根据问题复杂度自适应地平衡推理深度与效率，在召回型问题上避免冗余计算，同时在复杂推理问题上保留CoT的优势，最终实现准确性、效率和可解释性的更好平衡。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大型语言模型在医学问答中的性能与效率，可分为方法类和应用类。

在方法类研究中，**链式思维（CoT）提示**是关键基础，它通过生成中间推理步骤来提升复杂问题的逻辑性和可解释性，已被多项研究应用于医学问答基准测试。例如，Jeon等人全面评估了CoT在临床与非临床场景下的效果；Le等人将指令微调与CoT结合以处理上下文医学问答；Wang等人则进一步整合了检索增强生成（RAG）与CoT来增强模型性能。这些工作均默认对所有问题使用CoT，但忽略了其在简单回忆型问题上的计算冗余。

在应用类研究中，传统NLP方法（如基于关键词搜索或规则的系统）因难以处理语义变化和组合推理而受限，而LLMs通过预训练和领域适应改善了知识覆盖与推理能力。然而，现有方法未充分考虑效率问题，导致在部署时面临延迟与计算成本高的挑战。

本文提出的**选择性链式思维（Selective CoT）** 与上述研究的关系在于：它建立在CoT方法之上，但通过动态预测问题是否需要推理，仅在有必要时生成依据，从而区别于始终使用CoT的固定范式。与整合RAG等方法不同，本文专注于推理过程的优化，在保持精度的同时显著提升效率，为实际临床系统的部署提供了更成本敏感的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“选择性思维链”的推理时策略来解决医学问答中效率与准确性平衡的问题。其核心方法是让模型在回答每个问题前，先动态预测该问题是否需要复杂的推理过程，从而决定是否生成详细的推理依据。

整体框架包含两个主要阶段：判断阶段与生成阶段。在判断阶段，模型基于问题本身，预测其属于“知识回忆型”还是“推理型”。若判定为推理型问题，则进入生成阶段，采用标准的思维链提示，先生成中间推理步骤再给出最终答案；若判定为回忆型问题，则跳过推理步骤，直接生成答案。这种方法本质上是一种模型无关的提示工程策略，无需对底层大语言模型进行微调。

关键技术在于设计了一个统一的提示模板，将“是否需推理”的二元决策与后续的答案生成流程整合进单次前向传递中。其创新点主要体现在三个方面：一是**动态选择性**，根据问题复杂度自适应调整推理深度，而非对所有问题采用固定长度的思维链；二是**效率优化**，通过避免在简单问题上进行不必要的推理，显著减少了生成的总令牌数和端到端推理时间；三是**保持可解释性**，对于复杂的临床推理问题，仍能提供清晰的推理路径，维持了医疗应用所需的透明度。

实验表明，该架构在多个医学基准数据集上，能以最多4%的准确率损失，换取8%至47%的令牌使用减少和13%至45%的推理时间降低，在某些情况下甚至能同时提升准确率与效率。这验证了其核心设计思想：一个具备推理能力的模型，也应能识别何时需要推理。

### Q4: 论文做了哪些实验？

实验设置方面，论文提出了选择性思维链（Selective CoT）推理策略，该策略在推理时首先预测问题是否需要推理，仅在需要时才生成理由。研究在两个开源大语言模型（Llama-3.1-8B 和 Qwen-2.5-7B）上进行了评估。

数据集与基准测试使用了四个生物医学问答基准：HeadQA、MedQA-USMLE、MedMCQA 和 PubMedQA。评估指标包括准确率、生成的总令牌数和推理时间。

对比方法主要包括标准的思维链（CoT）推理，以及作为对照的、具有明确控制长度的固定长度CoT（例如约300词和约500词）。此外，还对Qwen-2.5-7B模型进行了更细致的CoT长度扫描（从100词到600词，以100词为增量），以分析长度与性能的关系。

主要结果显示，与标准CoT相比，Selective CoT在保持准确率微小变化（通常在0-4%以内）的同时，显著提升了效率：推理时间减少了约13%至45%，生成的令牌数减少了约8%至47%。在某些模型-任务组合中（如Qwen2.5-7B在HeadQA上），甚至实现了准确率提升（+8.70%）与效率提升（令牌-19.0%，时间-17.6%）的双重收益。与固定长度CoT相比，Selective CoT达到了相似或略优的准确率，但计算成本（令牌数和时间）大幅降低，形成了更优的计算-性能权衡。长度扫描实验揭示了准确率与固定CoT长度之间的非单调关系，而Selective CoT的结果点通常位于或接近经验最优值附近。

### Q5: 有什么可以进一步探索的点？

该论文提出的选择性思维链方法在效率与性能间取得了良好平衡，但仍存在一些局限性和可进一步探索的方向。首先，其“是否需要推理”的二元分类决策可能过于简化，医疗问题的复杂性往往是连续的，未来可探索更细粒度的“推理强度”调控机制，例如根据问题难度动态调整推理深度或步骤。其次，当前方法仅在推理生成阶段进行选择，未来可将选择机制前置到检索或知识激活阶段，实现端到端的自适应计算分配。此外，研究主要基于通用开源模型，未来可针对医学领域预训练或微调的模型进行优化，探索领域知识如何影响推理必要性判断。另一个方向是提升决策模块的可靠性，当前方法可能因误判（如将复杂问题误判为简单回忆）导致准确性下降，可结合不确定性校准或多模型投票机制来增强鲁棒性。最后，实际临床部署中还需考虑动态环境因素（如实时更新的医学指南），未来可研究在线学习机制，使模型能根据反馈持续优化其选择性推理策略。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型在医疗问答任务中应用时，标准思维链方法会为所有问题生成推理步骤、导致计算效率低下的问题，提出了一种名为“选择性思维链”的推理时策略。其核心贡献在于动态平衡推理深度与效率，通过一个路由机制先预测问题是否需要显式推理，仅在必要时生成理由链，从而避免在仅需回忆的事实型问题上进行冗余计算。

方法上，Selective CoT 是一个与模型无关的轻量级框架，在推理时先对问题进行分类，再决定采用直接回答还是生成推理步骤后回答。研究在四个生物医学QA基准和两个开源LLM上进行了评估。

主要结论显示，该方法能显著减少生成令牌数（8-47%）和推理时间（13-45%），同时将准确率损失控制在极小范围内（≤4%），甚至在部分情况下能同时提升准确率与效率。与固定长度的CoT相比，它以低得多的计算成本达到了相似或更优的准确率。这项工作为在现实世界预算和响应能力约束下部署基于LLM的临床问答系统，提供了一条实用且高性价比的路径。
