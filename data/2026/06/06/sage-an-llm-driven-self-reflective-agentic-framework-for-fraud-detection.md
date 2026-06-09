---
title: "SAGE: An LLM-driven Self Reflective Agentic Framework for Fraud Detection"
authors:
  - "Yichen Chen"
  - "Siying Li"
  - "Yuhang Liang"
  - "Lijun Wang"
  - "Renyang Liu"
date: "2026-06-06"
arxiv_id: "2606.08146"
arxiv_url: "https://arxiv.org/abs/2606.08146"
pdf_url: "https://arxiv.org/pdf/2606.08146v1"
github_url: "https://github.com/yichenC1c/SAGE"
categories:
  - "cs.AI"
tags:
  - "多智能体框架"
  - "欺诈检测"
  - "LLM智能体"
  - "自反思"
  - "数据诊断树"
  - "马尔可夫决策过程"
relevance_score: 9.5
---

# SAGE: An LLM-driven Self Reflective Agentic Framework for Fraud Detection

## 原始摘要

Fraud detection in payment, e-commerce, and telecommunications systems requires accuracy at the individual level, robustness under severe class imbalance, and ease of understanding for risk managers. Existing methods fall at least one of these requirements: automated machine learning systems search a fixed numerical space without semantic awareness of the dataset; graph neural network-based methods require pre-defined relational graphs and remain opaque at the individual-decision level; and the design of general-purpose large language model (LLM) agents does not consider the recall and precision constraints specific to real-world fraud detection. In this paper, we propose SAGE, the first end-to-end LLM-driven multi-agent framework for fraud detection. SAGE coordinates three dedicated agents that make decisions based on a six-layer Data Diagnostic Tree (DDT) and a Markov decision process guided by natural-language gradients, automatically optimizing the model under a fraud-specific reward. On five fraud datasets and five LLM backbones, SAGE wins $96.00\%$ of method--dataset comparisons and improves F1 by an average of $40.86\%$ over baselines. The code is available at https://github.com/yichenC1c/SAGE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在支付、电子商务和电信等系统中，针对个体级结构化数据进行欺诈检测时，现有方法无法同时满足高精度、鲁棒性（在严重类别不平衡下）和可解释性（对风险管理者）这三个核心要求的问题。研究背景是，欺诈已成为数字时代的主要经济威胁，急需从后端数据挖掘转向自动化的、可持续且可解释的工程流程。现有方法存在明显不足：传统的自动化机器学习（AutoML）系统仅在固定数值空间搜索，缺乏对数据集的语义理解；基于图神经网络的方法需要预定义的关系图，构建成本高且个体决策不透明；而通用的大型语言模型（LLM）代理则是基于通用基准开发，未考虑欺诈检测场景特有的召回率和精度约束。因此，本文要解决的核心问题是：如何基于个体级数据自动构建准确、鲁棒且可解释的欺诈检测模型。为此，论文提出了SAGE，这是第一个端到端的、专为欺诈检测设计的LLM驱动多代理框架。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：一是传统机器学习方法，如逻辑回归、随机森林、LSTM等，以及AutoML系统（Auto-sklearn、FLAML、AutoGluon），其局限在于仅搜索固定数值空间，缺乏语义理解和欺诈领域专有设计；二是图神经网络方法（CARE-GNN、PC-GNN），虽面向欺诈但需预定义关系图，在个体决策层面不透明且难以适应纯表格数据场景；三是通用LLM智能体框架（AutoGen、Reflexion、Data Interpreter、Claude Code），具备推理和自反馈能力，但未针对欺诈检测的召回率与精确率约束进行优化。本文提出的SAGE是首个端到端LLM驱动的多智能体欺诈检测框架，通过引入六层数据诊断树（DDT）和基于自然语言梯度的马尔可夫决策过程，在保持智能体可解释性的同时满足表格数据适配性和欺诈特定优化需求，弥补了现有方法在语义感知、个体透明度和领域专用性上的空白。

### Q3: 论文如何解决这个问题？

SAGE通过一个三阶段的多智能体框架系统性地解决欺诈检测问题。核心架构包含三个顺序协作的智能体：首先，Profiling Agent（A1）对输入数据集进行统计分析和语义诊断，其关键创新是六层数据诊断树（DDT），将原始数据集压缩为包含规模、标签、特征、质量、结构和诊断六个语义层的紧凑树结构，实现了超过25倍的token压缩率（以IEEE-CIS数据集为例），同时保留了关键决策信号。DDT通过两阶段构建：第一阶段进行确定性统计计算，第二阶段由LLM进行语义推理，生成数据集类型、关键风险特征和召回阈值τ等诊断信息。

其次，Planning Agent（A2）基于DDT输出自动选择合适的算法（如XGBoost/LightGBM/CatBoost）并生成结构化的初始训练代码c0，代码包含固定的五个块（加载、预处理、特征工程、训练、评估），每个块内的优化位置标记为handle，为后续迭代优化提供明确的操作锚点。

最后，Optimization Agent（A3）将代码优化建模为有限时域马尔可夫决策过程（MDP），采用ReAct风格的推理-行动循环。每次迭代包含两个独立LLM调用：第一个作为批评者生成自然语言梯度Dt（代码空间的文本诊断），第二个作为执行者将诊断转化为针对七个handle的具体代码编辑。迭代通过欺诈特定复合奖励函数R(mt)驱动，该函数融合F1、AUPRC、R@FPR10^-4和Recall四个指标，并包含召回惩罚门W_recall和精度保护门W_precision，确保模型在极端类别不平衡下不退化。历史轨迹Ht记录每次迭代的行动、奖励和诊断，支持自反思机制。

### Q4: 论文做了哪些实验？

为了评估SAGE的有效性，论文在五个欺诈检测数据集和五个LLM骨干网络上进行了实验。实验设置包括：使用IEEE-CIS、Credit Card等五个真实世界欺诈数据集，涵盖支付、电商和电信领域；对比方法包括AutoML、图神经网络和通用LLM agent三类基线。主要结果通过成对比较和性能提升衡量。SAGE在96%的方法-数据集对比中胜出，将F1分数平均提升了40.86%。关键数据指标包括：SAGE在20轮优化内收敛，利用三个专用agent（Profiling、Planning、Optimization Agent）协同工作。Profiling Agent通过六层数据诊断树（DDT）将数据集压缩约25倍（从50,000 tokens到2,000 tokens）；Optimization Agent通过NLG引导的MDP（马尔可夫决策过程）迭代优化代码，使用由召回率、精确率和F1组成的欺诈特定复合奖励函数，并在F1停滞≥2轮时触发动作切换。论文报告了在IEEE-CIS数据集上的具体性能提升，其中SAGE在召回率约束下实现了显著改善。

### Q5: 有什么可以进一步探索的点？

尽管SAGE在欺诈检测中展现了显著的优势，但仍存在若干可进一步探索的方向。首先，其依赖的LLM backbone和六层DDT在推理时会产生显著的计算开销，未来可探索轻量化模型或蒸馏技术以降低延迟。其次，当前框架主要聚焦于表格数据，但实际欺诈场景常涉及时序、文本或网络结构等异构信息，引入多模态融合策略或自适应特征选择机制可能提升泛化能力。此外，自然语言梯度的设计依赖人工模板，可尝试使用可学习的prompt生成器来自动优化状态到动作的映射。最后，欺诈模式具有时效性，现有静态训练难以适应概念漂移。引入在线学习或周期性自监督微调机制，使代理能根据新涌现的欺诈行为自动调整决策边界，将是重要延伸方向。

### Q6: 总结一下论文的主要内容

SAGE是一个专为欺诈检测设计的端到端LLM驱动多智能体框架，旨在解决个体级别表格数据欺诈检测中的精确性、鲁棒性和可解释性需求。论文定义的关键问题是现有方法（如AutoML、GNNs和通用LLM代理）在语义感知、图构建成本或召回率-精确率约束方面存在不足。SAGE通过三个专用智能体协调工作：Profiling Agent利用六层数据诊断树(DDT)对原始数据集进行结构化语义感知；Planning Agent基于DDT选择最优算法并合成初始分类器；Optimization Agent通过自然语言梯度驱动的有限时间马尔可夫决策过程迭代优化模型，在欺诈特定奖励机制下自动满足召回率和精确率约束。在五个欺诈数据集和五个LLM骨干上的实验表明，SAGE在96%的方法-数据集对比中胜出，F1值平均提升40.86%，显著优于AutoML、LLM编码代理和人类专家，且对底层语言模型变化不敏感。该工作的核心意义在于首次为欺诈检测任务设计专用LLM代理框架，实现了从数据分析到模型优化的全自动流程，同时保持了基于证据和业务规则的可解释决策。
