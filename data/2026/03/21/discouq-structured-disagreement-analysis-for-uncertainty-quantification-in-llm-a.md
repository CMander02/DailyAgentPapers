---
title: "DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles"
authors:
  - "Bo Jiang"
date: "2026-03-21"
arxiv_id: "2603.20975"
arxiv_url: "https://arxiv.org/abs/2603.20975"
pdf_url: "https://arxiv.org/pdf/2603.20975v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Uncertainty Quantification"
  - "Multi-Agent Systems"
  - "Ensemble Methods"
  - "Reasoning"
  - "Calibration"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles

## 原始摘要

Multi-agent LLM systems, where multiple prompted instances of a language model independently answer questions, are increasingly used for complex reasoning tasks. However, existing methods for quantifying the uncertainty of their collective outputs rely on shallow voting statistics that discard the rich semantic information in agents' reasoning. We introduce DiscoUQ, a framework that extracts and leverages the structure of inter-agent disagreement -- both linguistic properties (evidence overlap, argument strength, divergence depth) and embedding geometry (cluster distances, dispersion, cohesion) -- to produce well-calibrated confidence estimates. We propose three methods of increasing complexity: DiscoUQ-LLM (logistic regression on LLM-extracted structure features), DiscoUQ-Embed (logistic regression on embedding geometry), and DiscoUQ-Learn (a neural network combining all features). Evaluated on four diverse benchmarks (StrategyQA, MMLU, TruthfulQA, ARC-Challenge) with a 5-agent system using Qwen3.5-27B, DiscoUQ-LLM achieves an average AUROC of 0.802, outperforming the best baseline (LLM Aggregator, 0.791) while being substantially better calibrated (ECE 0.036 vs. 0.098). The learned features generalize across benchmarks with near-zero performance degradation and provide the largest improvements where they are most needed: in the ambiguous "weak disagreement" tier where simple vote counting fails.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）多智能体系统中，对集体输出进行不确定性量化时存在的关键不足。研究背景是，由多个角色化LLM实例组成的多智能体系统，通过独立推理和多数投票来聚合答案，已成为提升复杂任务准确性和鲁棒性的重要范式。然而，现有方法（如基于投票边际的置信度估计）存在显著缺陷：它们仅依赖浅层的投票统计信息（例如3比2的票数），而完全丢弃了各个智能体在推理过程中产生的丰富语义信息。这导致系统无法区分不同性质的“分歧”。例如，同样是3比2的投票结果，一种情况可能是少数派的论据薄弱且证据基础完全不同，另一种情况则可能是少数派提出了被多数派忽视的、极具说服力的新证据。这两种情形下，多数投票结果的可靠性截然不同，但传统投票计数法却赋予它们相同的置信度。

因此，本文要解决的核心问题是：如何超越简单的投票计数，通过深入分析智能体间分歧的**结构化信息**，来为多智能体系统的集体输出提供更准确、校准更好的不确定性量化。论文提出的DiscoUQ框架，其核心思想是挖掘分歧的丰富内部结构，包括语言特性（如证据重叠度、少数论据强度、分歧深度）和嵌入表示几何特性（如聚类距离、离散度、内聚度），并利用这些结构化特征来更精准地判断多数投票结果的正确概率，从而生成校准更佳的置信度估计。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**不确定性量化方法**：现有研究包括让模型自我报告置信度的“言语化置信度”方法、利用输出概率的“词元级方法”、以及通过聚类语义测量熵的“语义不确定性”等。这些方法多为黑盒式，且通常仅关注分歧的存在与否。本文的DiscoUQ框架则进一步**挖掘并利用多智能体间分歧的结构化信息**（如语言特性和嵌入几何），从而提供更精确的校准置信度。

**多智能体辩论与聚合**：已有工作如Du等人和Liang等人的研究，侧重于通过多智能体辩论提升事实性与推理多样性；Cemri等人则对系统故障模式进行了分类。这些研究主要旨在**提升系统性能或分析故障**，而本文则专注于**量化集体共识的不确定性**，旨在预测何时可能出现失败，而非事后分类。

**集成方法与校准**：经典集成方法（如深度集成）及神经网络校准研究常利用预测分歧进行不确定性估计。自我一致性方法将集成思想应用于思维链提示。本文**扩展了集成范式**，不仅统计投票，更深入分析分歧的语义内容，从而超越浅层统计。

**选择性预测**：该领域允许模型在不确定时弃权。本文生成的置信度估计可直接用于实现选择性预测，并通过覆盖度指标进行评估，与此类应用紧密衔接。

### Q3: 论文如何解决这个问题？

论文通过提出DiscoUQ框架来解决传统投票统计方法忽略语义信息的局限，其核心是利用智能体间分歧的结构化特征来量化不确定性。整体框架包含三个主要模块：特征提取、特征融合与建模、以及置信度估计。

首先，特征提取模块从多智能体输出中生成两类互补的特征族。第一类是**语言结构特征**，通过提示LLM分析非一致问题中各个智能体的推理文本，自动生成六个结构化评分：证据重叠度、少数派新信息量、少数派论证强度、多数派语言置信度、整体推理复杂度以及分歧深度（早期、中期、后期）。这些特征捕获了语义层面的分歧性质。第二类是**嵌入几何特征**，使用句子Transformer将每个智能体的推理文本编码为向量，并计算七个几何度量，如整体离散度、多数派内聚度、聚类间距离、少数派离群程度等，以量化向量空间中的分歧结构。两类特征均与基础的投票置信度结合。

其次，框架设计了三种递进复杂度的建模方法。**DiscoUQ-LLM**仅使用9维语言结构特征（包括投票置信度）进行逻辑回归，强调可解释性；**DiscoUQ-Embed**仅使用8维嵌入几何特征进行逻辑回归，无需额外LLM调用，计算高效；**DiscoUQ-Learn**则融合全部17维特征，通过一个两层MLP（含32个隐藏单元、ReLU激活和Dropout）进行端到端学习，以捕捉特征间的复杂交互。

创新点在于首次系统性地**结构化分析多智能体间的分歧**，不仅考虑投票统计，更深入挖掘语言语义和向量几何中的分歧模式。特别是通过LLM自动生成的语言特征，使得模型能识别“弱分歧”等模糊场景，从而显著提升校准性。实验表明，即使最简单的DiscoUQ-LLM也能在AUROC和ECE指标上超越基线，且学到的特征具有良好的跨任务泛化能力。

### Q4: 论文做了哪些实验？

实验在四个问答基准上进行：StrategyQA（687个二选一问题）、MMLU（746个多选题）、TruthfulQA（817个多选题）和ARC-Challenge（500个多选题），共计2750个问题，覆盖知识检索、多步推理、抗幻觉和科学推理。实验设置使用5个智能体组成的系统，主要模型为Qwen3.5-27B（温度0.7，最大token数800），嵌入提取使用BGE-large-en-v1.5。对比了六种基线方法：投票计数、投票熵、语言化置信度、自洽性熵、嵌入质心和LLM聚合器。评估指标包括AUROC（主要）、ECE、Brier分数等。

主要结果显示，DiscoUQ-LLM在平均AUROC上达到0.802，优于最佳基线LLM聚合器（0.791），且校准误差显著降低（ECE为0.036 vs. 0.098）。在具体基准上，DiscoUQ-LLM在StrategyQA和MMLU的AUROC最高（分别为0.706和0.870），而LLM聚合器在ARC-Challenge上表现最佳（0.868）。当按投票置信度分层时，DiscoUQ方法在“弱分歧”层（投票计数信息最少）提升最大，例如在MMLU的该层，DiscoUQ-LLM的AUROC为0.814，比投票计数高6.5个百分点。校准方面，所有DiscoUQ方法的ECE均低于0.074，而基线最高达0.338。在覆盖率指标上，DiscoUQ-LLM在MMLU的Coverage@95达到0.656，远高于投票计数的0.404，显示其在实际选择性预测中的优势。

### Q5: 有什么可以进一步探索的点？

论文的局限性为未来研究提供了明确方向。首先，可探索开放域生成任务中的不确定性量化，这需要设计新的评估指标来捕捉语义多样性和事实一致性。其次，需验证方法在不同模型架构（如小型化模型或MoE结构）上的泛化能力，并研究模型异构性对分歧结构的影响机制。第三，可改进LLM自省特征提取的可靠性，例如通过链式验证或对抗性提示来提升复杂推理链的分析质量。此外，无监督或半监督学习方法值得探索，以减少对标注数据的依赖。最后，可研究大规模智能体群体（如50+）中的分歧涌现规律，开发动态聚类算法来高效处理高维语义空间。这些方向将推动不确定性量化从静态统计向动态语义理解演进。

### Q6: 总结一下论文的主要内容

论文针对多智能体大语言模型系统中集体输出的不确定性量化问题，提出了一种名为DiscoUQ的新框架。现有方法通常依赖简单的投票统计，忽略了智能体推理中丰富的语义信息。该论文的核心贡献在于，通过分析智能体间分歧的结构——包括语言特性（如证据重叠、论证强度、分歧深度）和嵌入几何特征（如聚类距离、离散度、内聚性）——来生成更准确、校准更好的置信度估计。

论文提出了三种复杂度递增的方法：DiscoUQ-LLM（基于LLM提取的结构特征进行逻辑回归）、DiscoUQ-Embed（基于嵌入几何特征进行逻辑回归）以及DiscoUQ-Learn（结合所有特征的神经网络）。在四个不同基准测试（StrategyQA, MMLU, TruthfulQA, ARC-Challenge）上，使用Qwen3.5-27B模型的5智能体系统进行评估。结果表明，DiscoUQ-LLM取得了平均0.802的AUROC，优于最佳基线方法LLM Aggregator（0.791），同时校准误差显著更低（ECE为0.036对比0.098）。所学习的特征在不同基准间具有良好的泛化能力，性能下降近乎为零，并且在最需要改进的、智能体存在分歧的模糊“弱分歧”场景中提升效果最为明显。
