---
title: "Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric"
authors:
  - "Ruipeng Jia"
  - "Yunyi Yang"
  - "Yuxin Wu"
  - "Yongbo Gai"
  - "Siyuan Tao"
  - "Mengyu Zhou"
  - "Jianhe Lin"
  - "Xiaoxi Jiang"
  - "Guanjun Jiang"
date: "2026-02-15"
arxiv_id: "2602.14069"
arxiv_url: "https://arxiv.org/abs/2602.14069"
pdf_url: "https://arxiv.org/pdf/2602.14069v2"
categories:
  - "cs.CL"
tags:
  - "LLM-as-a-Judge"
  - "Reward Modeling"
  - "Alignment"
  - "Reinforcement Learning"
  - "Pairwise Comparison"
  - "Agent Training"
relevance_score: 7.5
---

# Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric

## 原始摘要

Scalar reward models compress multi-dimensional human preferences into a single opaque score, creating an information bottleneck that often leads to brittleness and reward hacking in open-ended alignment. We argue that robust alignment for non-verifiable tasks is fundamentally a principle generalization problem: reward should not be a learned function internalized into a judge, but an explicit reasoning process executed under inspectable principles. To operationalize this view, we present the Open Rubric System (OpenRS), a plug-and-play, rubrics-based LLM-as-a-Judge framework built around Pairwise Adaptive Meta-Rubrics (PAMR) and lightweight Pointwise Verifiable Rubrics (PVRs), which provide both hard-constraint guardrails and verifiable reward components when ground-truth or programmatic checks are available. OpenRS uses an explicit meta-rubric -- a constitution-like specification that governs how rubrics are instantiated, weighted, and enforced -- and instantiates adaptive rubrics on the fly by conditioning on the semantic differences between two candidate responses. It then performs criterion-wise pairwise comparisons and aggregates criterion-level preferences externally, avoiding pointwise weighted scalarization while improving discriminability in open-ended settings. To keep principles consistent yet editable across various domains, we introduce a two-level meta-rubric refinement pipeline (automated evolutionary refinement for general principles and a reproducible human-in-the-loop procedure for domain principles), complemented with pointwise verifiable rubrics that act as both guardrails against degenerate behaviors and a source of verifiable reward for objective sub-tasks. Finally, we instantiate OpenRS as reward supervision in pairwise RL training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在开放领域任务中，使用强化学习进行大语言模型对齐时，传统标量奖励模型存在的根本性缺陷问题。研究背景是，基于人类反馈的强化学习（RLHF）已成为主流对齐范式，但其核心依赖的标量奖励模型会将多维、复杂的人类偏好压缩成一个单一、不透明的分数。这种压缩造成了信息瓶颈，导致模型在开放场景下容易变得脆弱，并引发奖励破解行为——即策略学会利用奖励模型的漏洞（如虚假线索）来获取高分，而非真正提升响应质量。现有方法，包括生成式奖励模型和基于静态量规的评估，虽然有所改进，但仍存在不足：标量或生成式奖励模型的奖励信号不透明、难以迭代，且评估原则是隐式编码的，在分布外场景下容易失效；而现有的量规方法大多依赖静态或半静态的量规，并通过点式评分加权聚合为标量，这种方式在开放场景下的判别能力存在上限，同样易受奖励博弈影响，且难以泛化到没有明确“理想答案”的、需要权衡多方因素的上下文相关任务中。

本文要解决的核心问题是：如何为不可验证的开放任务设计一个鲁棒、可扩展且原则明确的奖励监督框架。作者认为，稳健的对齐本质上是一个原则泛化问题，奖励不应是一个被学习并内化于评判模型的不透明函数，而应是一个在明确、可审查的原则指导下执行的推理过程。为此，论文提出了开放量规系统，其核心是通过成对自适应元量规，动态生成适应具体比较对的评估量规，并进行准则层面的成对比较与外部偏好聚合，从而避免点式标量化，提升开放场景下的判别力与鲁棒性。同时，系统通过两级元量规精炼流程确保原则的一致性与可编辑性，并结合轻量级点式可验证量规作为护栏和可验证奖励来源，最终构建了一个可插拔的、结合了可验证奖励与基于原则的成对偏好优化的统一框架，以用于可扩展的强化学习训练。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**强化学习算法**、**奖励模型与评估方法**以及**可扩展的成对评估技术**。

在**强化学习算法**方面，相关工作包括PPO（近端策略优化）及其高效变体GRPO（组相对策略优化）。GRPO通过组内归一化进行优势估计，无需价值函数批评器，提升了样本效率。本文的OpenRS系统将作为奖励监督机制，应用于基于成对反馈的RL训练（如GRPO框架）中，旨在解决传统标量奖励模型的信息瓶颈问题。

在**奖励模型与评估方法**方面，核心争议在于**点式评分**与**成对评估**。传统方法（如标量奖励模型）将多维人类偏好压缩为单一不透明分数，易导致奖励破解和脆弱性。本文主张，对于不可验证的开放任务，应采用基于明确原则（如量规）的成对评估。这与直接学习奖励函数的“黑箱”法官模型形成对比。OpenRS通过其“开放式量规系统”，将评估过程外部化为一个可检查的推理流程。

在**可扩展的成对评估技术**方面，直接进行全组成对比较（复杂度O(N²)）计算成本高昂。相关研究如BRPO（自举相对策略优化）通过随机采样一个响应作为动态锚点，将评估复杂度降至O(N)。其他方法则采用种子单淘汰锦标赛或选择贪婪解码响应作为参考锚点。本文的OpenRS框架通过其“成对自适应元量规”（PAMR）动态生成量规，并进行准则层面的成对比较，在保持判别力的同时，其计算模式与这些可扩展的成对评估思路在目标上一致，但更强调评估原则的**显式化、可适应性和可编辑性**。

### Q3: 论文如何解决这个问题？

论文通过提出开放评分系统（OpenRS）来解决传统标量奖励模型的信息瓶颈和奖励破解问题。其核心方法是构建一个透明、结构化的评分框架，将评估分解为两个互补的路径：用于主观质量评估的成对自适应评分机制，以及为具有客观事实的子任务提供可验证奖励组件和硬约束护栏的点对点可验证评分机制。

整体框架包含以下主要模块与创新设计：
1.  **成对自适应评分**：这是系统的主观评估核心。它基于一个静态的“元评分标准”（Meta Rubric），这是一个类似宪法的原则集合。针对每一对候选回答，系统首先通过语义差异函数识别其关键差异，然后动态地实例化一个“自适应评分标准”。该标准包含一组带权重的具体准则。评估时，模型对每个准则进行独立的成对比较（给出-2到2的分数），而非预测单一的整体偏好概率。最终的成对偏好分数是这些准则特定分数的加权平均。这种方法避免了点对点的加权标量化，提高了在开放场景下的判别能力。
2.  **分层元评分标准与进化式精炼**：为了平衡通用性与特异性，元评分标准采用分层结构，包括通用的基础元评分标准和针对特定领域（如代码生成）的领域元评分标准。更重要的是，论文将评分标准的设计视为一个离散优化问题，提出了一种自动化的进化精炼流程。对于通用元评分标准，采用基于遗传算法和束搜索的黑盒优化策略，通过编辑操作（增、删、改）来进化评分标准，并使用非对称GRPO目标函数训练精炼策略，以集中优化成功的编辑，避免在偏斜的奖励下强化“次优失败”。对于领域元评分标准，则采用数据驱动、结合人工审核的流程进行针对性更新。
3.  **点对点可验证评分**：对于可绝对验证的维度（如格式、字数、数学正确性），系统使用点对点可验证评分标准。它由一组从查询中派生的验证器组成，每个验证器对单个输出产生确定性的信号（如通过/失败）。该模块扮演双重角色：一是作为防止退化行为的硬约束护栏，二是在有客观事实时提供可验证的奖励组件。
4.  **强化学习集成**：在RL训练中，OpenRS作为奖励接口。对于一个输出，其最终标量奖励是成对自适应分数（与参考锚点比较得出）和点对点可验证分数的叠加。这种分解将主观质量优化与客观约束执行解耦，为策略优化提供了透明且可扩展的奖励信号。

总之，OpenRS的创新点在于将奖励内部化为一个在可检查原则下执行的显式推理过程，通过动态自适应评分、分层进化精炼以及主客观评估路径的分离，构建了一个透明、可扩展且鲁棒的评估框架，有效缓解了奖励破解问题，并提升了在开放领域对齐中的判别力和一致性。

### Q4: 论文做了哪些实验？

论文在四个标准奖励建模基准上进行了实验：RM-Bench、JudgeBench、RewardBench v2和PPE Preference（其中PPE Preference使用了其约1.2k条样本的中文子集）。实验设置上，使用Qwen3-235B-A22B-Instruct-2507等开源模型作为评判骨干，并与Skywork-Reward-V2等最先进的标量奖励模型（SRM）基线进行对比。主要结果显示，OpenRS在所有基准上都取得了最优的人类偏好对齐性能，平均得分达到89.4，比最强的开源SRM基线（84.3）高出5.1个百分点。具体关键指标包括：在RM-Bench上得分为93.0（优于基线92.8）；在JudgeBench上得分为93.3（大幅优于基线82.0）；在RewardBench v2上得分为90.7（优于基线84.1）；在PPE Preference中文子集上得分为82.3（优于基线79.6）。实验还分析了不同骨干模型对OpenRS性能的影响，发现更强的骨干模型能带来更好的评判质量（例如，使用Qwen3-30B-A3B时平均分为84.9，使用Qwen3-235B-A22B时提升至89.4），并绘制了精度与计算开销的帕累托前沿，表明Qwen3-235B-A22B在保持高精度的同时具有较高的计算效率，因此被选为后续强化学习训练的默认骨干。

### Q5: 有什么可以进一步探索的点？

该论文提出的OpenRS系统在可解释性和抗奖励破解方面有显著优势，但仍存在一些局限性和值得深入探索的方向。首先，系统严重依赖大语言模型作为评判者，其推理成本和延迟限制了在更大规模RL训练中的实时应用，未来可研究如何通过蒸馏或专用小型模型来提升效率。其次，当前的元准则（Meta-Rubric）生成和进化机制虽然引入了自动化，但对初始准则设计和人类反馈的依赖性仍较强，可能导致领域适应性瓶颈；未来可探索更自主的准则发现与优化框架，减少人工干预。此外，系统主要针对成对比较，在需要绝对评分或处理大量候选的場景（如大规模排序）中可能效率不足，需研究高效的点式评分与成对机制的融合。从方法层面看，论文虽验证了非标量奖励的有效性，但未深入探讨不同准则聚合方式（如基于偏好的排序学习）对最终策略收敛性的理论影响，这值得进一步分析。最后，系统在高度动态或对抗性环境中的鲁棒性尚未充分测试，未来可考虑将准则系统与形式化验证结合，以提供更严格的安全保障。

### Q6: 总结一下论文的主要内容

该论文针对开放域任务中基于标量奖励模型进行对齐时存在的“信息瓶颈”和“奖励黑客”问题，提出了一种新的强化学习对齐框架——开放准则系统。其核心观点是，稳健的对齐不应将奖励内化为一个不透明的评分函数，而应是一个基于可检查原则的显式推理过程。

论文的主要贡献是提出了OpenRS框架，它包含两个关键组件：用于成对比较的“成对自适应元准则”和用于可验证子任务的“点式可验证准则”。该方法的核心创新在于，它通过一个类似宪法的“元准则”来动态生成针对具体响应语义差异的评估准则，并进行准则层面的成对比较与外部偏好聚合，从而避免了传统的点式加权标量化，提升了开放域下的判别能力。此外，论文还设计了一个两级元准则优化流程，结合自动化进化与人工参与，以保持原则的一致性与可编辑性。

主要结论是，OpenRS作为一种即插即用的评估框架，能够为开放域非可验证任务的对齐提供更透明、更稳健的奖励监督，并通过在成对强化学习训练中的实例化验证了其有效性。其意义在于将奖励建模从“黑盒”评分转向“白盒”原则推理，为构建可解释、抗攻击的AI对齐系统提供了新路径。
