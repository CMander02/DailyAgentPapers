---
title: "Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering"
authors:
  - "Zaifu Zhan"
  - "Shuang Zhou"
  - "Rui Zhang"
date: "2026-06-13"
arxiv_id: "2606.15419"
arxiv_url: "https://arxiv.org/abs/2606.15419"
pdf_url: "https://arxiv.org/pdf/2606.15419v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体协作"
  - "推理提升"
  - "医疗问答"
  - "peer-review机制"
  - "评估与选拔"
relevance_score: 9.5
---

# Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering

## 原始摘要

Objective: To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA).
  Method: We designed a multi-agent peer-reviewed reasoning method in which multiple LLM agents independently generate chain-of-thought reasoning with candidate answers, then act as peer reviewers to evaluate each other's reasoning for factual correctness and logical soundness. The highest-rated reasoning chain is selected to produce the final answer. Experiments were conducted with five state-of-the-art LLMs (Llama-3.1-8B, Qwen2.5-7B, Phi-4, DeepSeek-LLM-7B, GPT-oss-20B) on three benchmark datasets: HeadQA, MedQA-USMLE, and PubMedQA. Performance was compared against single-model chain-of-thought reasoning and chain-of-thought-based majority voting.
  Results: Peer-reviewed reasoning consistently outperformed both baselines. The best model combination achieved an average accuracy of 0.820 across datasets, exceeding the strongest single model (0.777) and majority voting ensembles (up to 0.789). The method also scaled effectively with more participating models, while peer assessments reliably distinguished high- from low-quality reasoning chains.
  Conclusion: The proposed multi-agent peer-reviewed reasoning method enables LLMs to act as both solvers and evaluators, yielding superior performance in MedQA. By emphasizing reasoning quality rather than answer agreement alone, this approach improves accuracy, interpretability, and robustness, offering a promising direction for trustworthy biomedical AI systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型在医学问答（MedQA）领域中准确性和推理可靠性不足的问题。研究背景是：大语言模型在生物医学任务中展现了强大的能力，尤其是通过链式思维（CoT）提示方法能逐步生成推理过程并提升问答性能。然而，现有方法存在明显不足：大多数工作仅在生成答案后才评估推理质量（如人工审查或与人类推理对比），并未将推理评估融入决策过程本身。此外，现有方法如CoT多数投票只注重最终答案的多数一致性，忽视了不同推理链的内在质量差异，可能导致选择正确但推理有缺陷的答案。同时，仅依靠单个或少数模型容易因模型偏好或逻辑错误而产生误导性结论。核心问题是：如何让LLM在医学问答中不仅生成推理，还能相互评估推理的逻辑正确性和事实准确性，从而选出最可靠的推理链，以获得更准确、可解释且鲁棒的答案。为此，论文提出了一种多智能体同行评审推理方法，让多个LLM代理独立生成CoT推理和候选答案，再相互评审，最终基于评审评分选出最佳推理链输出答案，从而提升医学QA性能。

### Q2: 有哪些相关研究？

相关研究主要集中在三个类别：**多智能体协作方法**、**自检与反思机制**以及**医学问答评测**。  
- **多智能体协作方法**：如基于辩论（Du et al., 2023）或角色扮演（Li et al., 2024）的协作推理。本文创新地提出“同行评审”机制，让智能体交叉评估推理链的事实准确性，而非仅通过一致性投票或辩论达成共识，更强调逻辑质量。  
- **自检与反思机制**：如Self-Refine（Madaan et al., 2023）或Chain-of-Thought Self-Consistency（Wang et al., 2023）。这些方法依赖单个模型自我修正，易陷入确认偏误。本文通过多智能体外部评审打破这一局限，评审者会指出共因错误（如共同的知识缺陷）。  
- **医学问答评测**：已有方法如Med-PaLM（Singhal et al., 2023）或Clinician-like reasoning（Huang et al., 2024）。本文在HeadQA、MedQA-USMLE和PubMedQA上的实验表明，同行评审不仅提升准确率（平均0.820），且评审质量评分与推理质量高度相关，优于单一模型链式思维和多数投票，尤其适用于需严格推理的医学场景。

### Q3: 论文如何解决这个问题？

论文提出的多智能体同行评审推理方法包含两个核心阶段：首先，多个LLM智能体各自独立生成基于思维链的推理过程和候选答案；然后，这些智能体互相作为评审者，对彼此的推理进行事实准确性和逻辑合理性的评分（采用0-5分制）。最终选择评分最高的推理链对应的答案作为输出。整体框架由三个关键模块构成：多智能体生成模块负责并行产生多样化的推理路径；同行评审模块构建一个评分矩阵，每个智能体依据医学领域知识和内部推理能力对其他智能体的答案进行评判，而非依赖真实标签；聚合模块通过均值或中位数汇总所有评分，并选出最优结果。该方法的创新点在于：一是将学术界的同行评审机制引入LLM推理，强调推理质量而非仅答案一致性；二是通过模型异构性（如DeepSeek作为弱求解者但强评审者）实现互补优势；三是保留了可解释的推理轨迹，提升了模型在医疗问答任务中的准确性和鲁棒性。实验在五个不同系列、不同规模的LLM上验证了该方法在HeadQA、MedQA-USMLE和PubMedQA三个数据集上均优于标准思维链和多数投票基线。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行实验：HeadQA、MedQA-USMLE和PubMedQA。实验使用五个最先进的LLM代理：Llama-3.1-8B、Qwen2.5-7B、Phi-4、DeepSeek-LLM-7B和GPT-oss-20B。对比方法包括单模型链式思考推理和基于链式思考的多数投票。实验设置将所有可能模型组合（从两两组合到五模型组合）进行验证，并选取平均准确率最高的组合呈现。主要结果：单模型中GPT-oss-20B表现最优，平均准确率0.777；多数投票最佳组合（3+4+5）达0.789；而同行评审推理显著超越两者，最佳组合（Deepseek, Llama, Phi, GPT-oss）平均准确率达0.820。在单数据集上，HeadQA达0.861，MedQA-USMLE达0.827，PubMedQA达0.776。同行评审评分与模型准确率呈强正相关（r=0.91，p=0.034），且不同评审提示下性能稳定（标准差≤0.007）。排除自我评估的偏见实验显示，无偏同行评审性能依然优异。该方法虽增加了两阶段推理的时间开销，但相比多数投票在准确率、可解释性和鲁棒性上均有显著提升。

### Q5: 有什么可以进一步探索的点？

论文的局限与未来探索方向主要包括以下几点：  
1. **计算开销与效率**：当前方法需生成N²次评估调用（N=5时成本为多数投票的5倍），未来可探索**稀疏评估机制**（如仅对争议性推理链进行交叉评审），或引入**高效注意力路由**降低冗余计算。  
2. **模型与规模扩展性**：研究仅测试了5个LLM，未探索过大规模（如10+模型）下的协调成本与收益递减效应。可设计**动态聚合策略**（根据历史评审准确性动态调整评委权重），或结合**分层评审架构**（先聚类相似推理再抽样评审）。  
3. **数据污染与泛化性**：未控制训练数据泄漏风险。后续可引入**对抗性评估**（如从执业医师考试中筛选未公开题目），并构建**领域迁移验证**（从MedQA推广至影像报告生成等任务）。  
4. **多模态与知识增强**：论文仅处理文本，但临床决策常依赖影像、实验室数据。可结合**视觉语言模型**与**检索增强生成**，使评审阶段能直接引用指南或文献片段验证医学逻辑。  
5. **平票处理机制**：当前简单确定性策略可能忽略多组高质量推理的差异。未来可设计**二次评审回合**（让评委对顶部分案再辩论），或引入**不确定性量化**（如通过理由链的置信度投票）。  

这些方向有望平衡计算效率与推理质量，推动可信医疗AI的落地。

### Q6: 总结一下论文的主要内容

本文提出了一种多智能体同行评审推理方法，旨在提升大语言模型在医学问答中的准确性、可解释性和鲁棒性。该方法让多个LLM智能体独立生成思维链推理和候选答案，随后作为同行评审者评估彼此推理的事实正确性和逻辑连贯性，最终选择评分最高的推理链输出答案。在HeadQA、MedQA-USMLE和PubMedQA三个基准数据集上，使用Llama-3.1-8B、Qwen2.5-7B等五个先进模型进行实验。结果显示，该方法一致优于单模型思维链推理和基于思维链的多数投票，最佳模型组合平均准确率达0.820，超过最强单模型（0.777）和多数投票集成（最高0.789）。该方法随参与模型数量增加有效扩展，且同行评审能可靠区分高质量与低质量推理链。核心贡献在于让LLM同时扮演求解者和评估者，通过强调推理质量而非仅答案一致性，显著提升了医学问答性能，为构建可信赖的生物医学AI系统提供了有前景的方向。
