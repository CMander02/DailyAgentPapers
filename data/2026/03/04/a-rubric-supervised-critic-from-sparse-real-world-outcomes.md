---
title: "A Rubric-Supervised Critic from Sparse Real-World Outcomes"
authors:
  - "Xingyao Wang"
  - "Valerie Chen"
  - "Heng Ji"
  - "Graham Neubig"
date: "2026-03-04"
arxiv_id: "2603.03800"
arxiv_url: "https://arxiv.org/abs/2603.03800"
pdf_url: "https://arxiv.org/pdf/2603.03800v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "Agent 强化学习"
  - "Agent 数据合成"
  - "Agent 规划/推理"
  - "工具使用"
relevance_score: 8.0
---

# A Rubric-Supervised Critic from Sparse Real-World Outcomes

## 原始摘要

Academic benchmarks for coding agents tend to reward autonomous task completion, measured by verifiable rewards such as unit-test success. In contrast, real-world coding agents operate with humans in the loop, where success signals are typically noisy, delayed, and sparse. How can we bridge this gap? In this paper, we propose a process to learn a "critic" model from sparse and noisy interaction data, which can then be used both as a reward model for either RL-based training or inference-time scaling. Specifically, we introduce Critic Rubrics, a rubric-based supervision framework with 24 behavioral features that can be derived from human-agent interaction traces alone. Using a semi-supervised objective, we can then jointly predict these rubrics and sparse human feedback (when present). In experiments, we demonstrate that, despite being trained primarily from trace-observable rubrics and sparse real-world outcome proxies, these critics improve best-of-N reranking on SWE-bench (Best@8 +15.9 over Random@8 over the rerankable subset of trajectories), enable early stopping (+17.7 with 83% fewer attempts), and support training-time data curation via critic-selected trajectories.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实世界中编码智能体（coding agents）评估信号稀疏、延迟和噪声大的问题。当前，学术基准（如SWE-bench）通常通过可验证的奖励（如单元测试通过率）来评估智能体的自主任务完成能力，但这与真实场景存在显著差距。在现实应用中，智能体需与人类协同工作，用户会通过多轮对话澄清意图、审查代码差异并决定最终合并，成功信号不仅取决于测试通过，更涉及代码的正确性、可维护性及是否真正减轻用户负担。然而，现有方法依赖的监督信号（如用户反馈）往往稀疏且延迟，难以提供密集、及时的学习信号，限制了智能体在真实交互中的优化。

为此，本文提出一种从稀疏、噪声数据中学习“评论家”（critic）模型的方法，以弥合学术基准与真实应用之间的评估鸿沟。核心创新在于引入“评论家评分标准”（Critic Rubrics），通过24个可观测的行为特征（如“误解意图”“测试不足”“用户挫败感”）对交互轨迹进行密集标注，并结合稀疏的现实结果代理（如代码存活率）进行半监督训练。该方法使评论家能同时预测评分标准特征和任务成功概率，从而将大量未标注的交互轨迹转化为有效训练数据，提升模型在真实场景中的评估能力。最终，学习到的评论家可支持推理时重排序、早期停止和训练数据筛选等下游应用，显著提升智能体在现实环境中的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类方面，相关工作包括奖励模型与多目标监督。例如，基于人类反馈的强化学习（RLHF）中的奖励模型通过成对比较来预测偏好；过程奖励模型则将评估分解为步骤级反馈。ArmoRM进一步通过多目标学习将奖励分解为可解释的目标（如诚实性、安全性、冗余度）。本文提出的“评分标准监督”框架与之相关但目的不同：它不仅追求可解释性，更通过评分标准实现半监督学习——行为特征可在所有轨迹上标注，无论其是否有结果标签，从而将未标注数据转化为有用信息。在应用类方面，相关工作涉及批评者模型的应用。例如，在数学推理和近期软件智能体领域，验证器已用于最佳K项选择；研究表明推理时计算可超越训练时扩展。本文的评分标准监督批评者模型同时支持推理时选择（通过提前停止减少83%计算）和训练时数据筛选（相比随机选择提升监督微调效果），并能泛化至同一智能体框架内的不同大语言模型骨干。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Critic Rubrics”的基于量规的监督框架来解决从稀疏、嘈杂的真实世界交互数据中学习“评论家”模型的问题。其核心方法是利用可观测的交互轨迹，定义一组细粒度的行为特征（量规）作为监督信号，从而将大量无标签的交互片段转化为可用的学习数据。

整体框架和主要模块包括：
1.  **量规设计与标注**：首先，论文定义了24个行为特征（Critic Rubrics），这些特征分为三类：**智能体行为问题**（如误解意图、工具使用不当）、**用户后续行为模式**（如请求澄清、表达沮丧）和**基础设施问题**。这些量规的关键特性是**可追溯观测性**，即仅从交互轨迹本身（用户消息、智能体动作序列）即可推导，无需依赖最终的成功标签，从而避免了信息泄露。
2.  **半监督学习目标**：基于这些量规标注，论文训练一个专门的评论家模型。该模型采用**半监督目标**，能够**联合预测**两类信号：a) 所有交互片段都有的、密集的量规特征；b) 仅部分片段存在的、稀疏的真实世界结果标签（如代码存活、PR合并）。这使得模型能够充分利用大量无标签数据中的行为模式信息，同时对齐稀疏的最终成功信号。
3.  **模型应用与创新点**：训练好的评论家模型可以快速地从新的交互轨迹中预测成功概率和失败模式。其创新点在于：
    *   **从稀疏到密集的监督转换**：通过引入可扩展、可自动标注（基于LLM）的量规体系，将稀疏的成功/失败信号转化为密集的行为特征监督，极大地扩充了有效训练数据。
    *   **真实世界与基准测试的桥接**：量规特征在基准测试（如SWE-bench）中与单元测试失败强相关，在真实数据中虽信号较弱但仍与最终结果关联，证明了其作为通用失败模式指示器的有效性。
    *   **灵活的下游应用**：该评论家模型可作为奖励模型用于强化学习训练，也可在推理时用于任务轨迹的**重排序**、**早期停止**（避免无效尝试）和**训练数据筛选**，从而在多方面提升智能体在真实人机协作环境中的性能。

### Q4: 论文做了哪些实验？

论文实验围绕评估Critic模型的泛化能力和实际应用效果展开。实验设置方面，研究者基于OpenHands Agent SDK构建智能体框架，使用Qwen3-4B-Instruct初始化Critic模型，并添加多任务预测头。输入数据为智能体交互轨迹片段，平均长度38K token，采用64K上下文长度并左截断以保留近期上下文。

数据集包括真实世界交互数据（1547个带PR合并标签的片段和1083个带代码存活标签的片段）和SWE-bench基准测试数据（使用Claude Sonnet 4.5和Claude Opus 4.5生成的各500个实例×4次运行轨迹）。对比方法主要分为两类训练目标：Success-Only（仅预测结果代理）和Success+Rubrics（联合预测结果标签和24个行为特征）。针对代码存活代理（连续值0-1），比较了BCE-floor、BCE-round和MSE回归三种变体。

主要结果如下：在真实世界数据上，仅使用基准数据训练的Critic模型表现接近随机水平（AUC 0.48-0.45），而加入真实数据训练的模型AUC提升至0.64-0.69。代码存活代理训练的Critic在真实数据上AUC达0.69，优于PR合并代理的0.58。在SWE-bench的混合结果子集上，Success+Rubrics（BCE-floor）的Best@8达到73.8%，较随机选择提升15.9个百分点；早期停止策略在τ=0.5时仅需平均1.35次尝试，计算量减少83%，性能提升17.7个百分点。跨骨干网络实验显示，Success-Only方法在Sonnet上表现良好但在Opus上低于随机，而Success+Rubrics方法在两个骨干网络上均保持正增益。在训练数据筛选方面，基于Critic筛选的SFT数据使智能体解决率达到47.8%，优于随机筛选的46.2%。

### Q5: 有什么可以进一步探索的点？

本文提出的基于评分标准的监督框架虽能有效利用稀疏、噪声的真实交互数据，但其局限性也为未来研究提供了多个探索方向。首先，当前方法依赖人工定义的24个行为特征，其完备性和普适性有待验证；未来可探索自动学习或动态扩展特征集，以适应更复杂的任务场景。其次，实验主要基于代码生成任务（SWE-bench），未来需验证其在多模态交互、长期决策等领域的泛化能力。此外，稀疏反馈的利用效率仍有提升空间，可结合主动学习或不确定性估计来优化数据标注策略。从方法改进角度看，可探索将评分标准预测与强化学习更深度结合，例如设计分层奖励函数或引入元学习来适应不同用户的偏好模式。最后，如何将此类批评家模型无缝集成到实际人机协作流程中，并实现实时自适应优化，也是值得深入探索的工程与应用挑战。

### Q6: 总结一下论文的主要内容

这篇论文针对现实世界中编码智能体（coding agents）面临的成功信号稀疏、延迟和噪声问题，提出了一种从稀疏真实交互数据中学习“评论家”（critic）模型的方法。核心贡献是引入了“评论家评分标准”（Critic Rubrics），这是一个包含24个可观测行为特征的监督框架，这些特征仅从人机交互轨迹中即可推导，为模型提供了密集的过程监督信号。

论文方法概述为：首先将人机交互轨迹结构化为“片段”（segments）；然后利用这些评分标准特征与稀疏的真实结果（如代码存活率）共同训练一个半监督、多任务的评论家模型，使其能联合预测评分标准特征和片段成功概率。这样，大量未标注的交互数据也成为了有效的训练样本。

主要结论表明：1）仅基于基准测试训练的评论家在现实场景中效果近乎随机，因此真实世界监督必不可少；2）在稀疏结果代理信号中，“代码存活”比“PR合并”能提供更精细、更可归因的监督；3）评分标准监督使评论家分数在不同LLM骨干模型间具有更好的泛化能力。该评论家模型能有效应用于推理时扩展（如在SWE-bench上通过最佳N重排序提升性能）、提前终止不成功的智能体轨迹，以及训练时的数据筛选。
