---
title: "Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification"
authors:
  - "Yichi Zhang"
  - "Nabeel Seedat"
  - "Yinpeng Dong"
  - "Peng Cui"
  - "Jun Zhu"
  - "Mihaela van de Schaar"
date: "2026-03-03"
arxiv_id: "2603.02798"
arxiv_url: "https://arxiv.org/abs/2603.02798"
pdf_url: "https://arxiv.org/pdf/2603.02798v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Verification"
  - "High-Stakes Decision-Making"
  - "Clinical Diagnosis"
  - "Guideline Grounding"
  - "Evidence Accumulation"
  - "Calibration"
  - "Trustworthy AI"
  - "Agent Evaluation"
relevance_score: 8.5
---

# Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification

## 原始摘要

As LLM-powered agents have been used for high-stakes decision-making, such as clinical diagnosis, it becomes critical to develop reliable verification of their decisions to facilitate trustworthy deployment. Yet, existing verifiers usually underperform owing to a lack of domain knowledge and limited calibration. To address this, we establish GLEAN, an agent verification framework with Guideline-grounded Evidence Accumulation that compiles expert-curated protocols into trajectory-informed, well-calibrated correctness signals. GLEAN evaluates the step-wise alignment with domain guidelines and aggregates multi-guideline ratings into surrogate features, which are accumulated along the trajectory and calibrated into correctness probabilities using Bayesian logistic regression. Moreover, the estimated uncertainty triggers active verification, which selectively collects additional evidence for uncertain cases via expanding guideline coverage and performing differential checks. We empirically validate GLEAN with agentic clinical diagnosis across three diseases from the MIMIC-IV dataset, surpassing the best baseline by 12% in AUROC and 50% in Brier score reduction, which confirms the effectiveness in both discrimination and calibration. In addition, the expert study with clinicians recognizes GLEAN's utility in practice.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决高风险领域（如临床诊断）中LLM智能体决策的可靠验证问题。随着LLM智能体越来越多地应用于高风险决策，其错误可能导致严重后果，因此必须对其决策进行可信验证以确保安全部署。

研究背景在于，高风险领域存在“生成廉价、验证困难”的根本性不对称性，因为准确验证通常需要领域专业知识。现有验证方法存在明显不足：基于奖励建模的方法需要大量专家标注数据，成本高昂；而无需训练的方法（如LLM-as-a-Judge或自一致性采样）缺乏明确领域知识指导，容易受到模型隐含偏见或一致性错误的影响，且难以产生基于领域标准的校准信号。

本文的核心问题是：如何将领域知识（特别是已编纂的专业指南，如临床指南）编译成可靠的、具有校准正确性概率的验证信号，从而通过弃权或升级机制实现风险控制。为此，论文提出了GLEAN框架，其核心思路是将验证重构为基于领域指南的序列证据积累过程，通过评估智能体执行轨迹中每一步与指南的符合程度，积累证据并利用贝叶斯逻辑回归将其转化为校准的正确性概率。此外，框架还引入主动验证机制，针对高不确定性案例通过扩展指南覆盖和进行差异化检查来收集额外证据，从而提升验证可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，现有验证方法主要针对LLM生成答案的可靠性评估，包括学习型验证器（如结果和过程奖励模型）、无训练方法（如基于令牌概率或生成分数的模型评分）以及基于采样的信号（如自一致性和语义熵）。此外，外部检查方法（如检索验证和逻辑验证）也提供了额外证据。然而，这些方法通常缺乏领域知识、校准能力有限，或难以处理高风险决策中的不确定性。

在应用类研究中，LLM智能体已广泛应用于软件工程、网页浏览等高阶问题求解，并逐步进入金融、医疗等高风险领域。特别是在临床诊断等任务中，已有系统尝试进行医疗决策，但其表现与人类专家仍有差距，且多步骤错误复杂化。现有验证机制（如代码测试、动作验证或安全护栏）虽在特定任务中有效，但未能充分结合领域专业知识或提供校准置信度以支持风险管理。

在评测类研究中，现有工作多聚焦于事实核查和数学等领域的答案验证，缺乏对智能体多步骤决策的全面评估。本文提出的GLEAN框架与上述研究的关键区别在于：它首次将专家制定的领域指南系统性地融入验证过程，通过轨迹感知的证据积累和贝叶斯逻辑回归生成校准的正确性概率，并引入主动验证机制处理不确定案例，从而在高风险临床诊断中实现了更优的判别能力和校准性能。

### Q3: 论文如何解决这个问题？

论文通过提出GLEAN框架来解决高风险智能体决策的验证问题，其核心方法是将专家制定的领域指南（guidelines）转化为可校准的正确性信号，并基于贝叶斯证据积累进行概率化验证。整体框架包含以下关键模块与创新点：

首先，**框架将验证建模为序列化证据积累过程**。智能体执行轨迹被分解为多步观察与行动，通过贝叶斯规则将最终输出的正确性后验概率分解为每一步的增量证据。这允许验证器逐步累积信心，并最终通过累积证据的对数几率（log-odds）计算校准后的正确性概率。

其次，**引入指南接地的评分机制作为替代证据**。针对每一步，系统从外部指南库中检索与当前上下文及最终答案相关的指南，使用LLM评判器对当前步骤与指南的符合程度进行评分，生成标量评分 \(s_{t,g}\)。由于原始评分存在校准问题，论文进一步提出**多指南聚合与特征提取**：对每一步聚合多个相关指南的评分，提取统计特征（如均值、最小值）构成步级特征向量，再通过折扣累加得到前缀级替代证据 \(\mathbf{S}_t\)，以增强鲁棒性并降低噪声。

第三，**采用贝叶斯逻辑回归进行校准**。将累积证据映射到正确性概率，通过高斯先验正则化和MCMC采样后验分布，得到校准后的置信度估计 \(\hat{p}_T\)。这种线性校准器的有效性依赖于指南接地信号的两个关键性质：近似充分性和对数几率空间的近线性关系，论文通过实验验证了指南接地信号显著满足这些性质。

最后，**不确定性触发的主动验证机制**是重要创新。当校准后的不确定性超过阈值时，系统通过两种策略收集额外证据：一是**指南扩展**，检索更多相关指南以丰富证据池；二是**差分检查**，检索竞争性结果的指南并进行评分校正，通过对比当前轨迹与竞争指南的匹配程度来避免误判。这一机制显著提升了困难案例的验证可靠性。

整体而言，GLEAN通过将领域知识（指南）结构化地融入验证流程，结合序列证据积累、多指南聚合、贝叶斯校准及主动验证，实现了既具有高判别力又具备良好校准性的智能体验证。

### Q4: 论文做了哪些实验？

论文在智能体临床诊断这一高风险决策场景中进行了实验验证。实验设置方面，使用MIMIC-IV数据集中的三种疾病（憩室炎、胆囊炎、胰腺炎），采用ReAct风格的智能体工作流程，以Qwen2.5-7B-Instruct和Qwen3-30B-A3B-Instruct为骨干模型，为每个病例生成多条轨迹（温度0.9），并构建了包含2000条轨迹的测试集（正确与错误各半）。评估指标包括区分度的AUROC、置信度前50%样本的错误率Risk@0.5，以及校准指标ECE和Brier分数，同时通过Best-of-N选择评估实用性。

对比方法涵盖多类基线：基于模型评分的P(TRUE)和LLM-as-a-Judge；基于采样的Self-Consistency和Semantic Entropy；基于外部检查的Self-Verification和RAG增强评分；以及学习型验证器Med-PRM和ORM。

主要结果显示，GLEAN在各项指标上显著优于基线。例如，在Qwen2.5-7B骨干下，GLEAN（K=3）在三种疾病上的平均AUROC达0.9185，优于最佳基线Self-Consistency的0.8203；加入主动验证（阈值0.5）后，AUROC进一步提升至0.9381，Brier分数降低至0.0914。关键数据指标上，GLEAN（K=3+主动）在憩室炎任务中AUROC最高达0.9862（Qwen3-30B），Risk@0.5最低至0.0370；同时，在Best-of-N实验中，使用GLEAN信号可将Qwen3-30B的准确率从58.94%提升至78.3%。消融实验进一步证实了轨迹感知、指南 grounding、证据累积和校准各组件以及高质量指南内容的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的GLEAN框架虽然在临床诊断等高风险领域验证中表现出色，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖专家制定的指南，这限制了其在指南不完善或快速演变领域（如新兴疾病或个性化医疗）的适用性。未来可探索如何结合领域自适应或在线学习，使系统能从少量新证据中动态更新验证逻辑。其次，框架主要基于贝叶斯逻辑回归进行概率校准，未来可研究更复杂的校准模型（如深度贝叶斯网络）以处理更高维的非线性特征交互。此外，主动验证部分仅通过扩展指南覆盖和差异检查来收集证据，未来可整合多模态数据（如医学影像或传感器数据）作为补充证据源，并引入强化学习来优化证据收集的决策策略，以平衡验证成本与准确性。最后，当前验证聚焦于单个代理决策，未来可扩展至多智能体协作场景的联合验证，并探索其在不同高风险领域（如金融风控、司法判决）的泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为GLEAN的框架，旨在解决高风险领域（如临床诊断）中LLM智能体决策的可靠验证问题。核心问题是现有验证方法因缺乏领域知识和校准不足而性能不佳。GLEAN通过将专家制定的指南转化为轨迹感知的校准正确性信号来应对这一挑战。其方法概述包括：评估智能体每一步与领域指南的符合程度，将多指南评分聚合为代理特征，并沿轨迹累积这些特征，最后使用贝叶斯逻辑回归将其校准为正确概率。此外，框架通过估计不确定性触发主动验证，为不确定案例选择性收集额外证据（如扩展指南覆盖和进行差异检查）。主要结论是，在MIMIC-IV数据集中三种疾病的临床诊断任务上，GLEAN在AUROC上超越最佳基线12%，在Brier分数降低上提升50%，证明了其在区分度和校准方面的有效性，且临床专家研究认可其实用性。该工作的意义在于为高风险AI决策提供了可解释、可校准的验证工具，促进可信部署。
