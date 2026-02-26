---
title: "Efficient Cross-Domain Offline Reinforcement Learning with Dynamics- and Value-Aligned Data Filtering"
authors:
  - "Zhongjian Qiao"
  - "Rui Yang"
  - "Jiafei Lyu"
  - "Chenjia Bai"
  - "Xiu Li"
  - "Siyang Gao"
  - "Shuang Qiu"
date: "2025-12-02"
arxiv_id: "2512.02435"
arxiv_url: "https://arxiv.org/abs/2512.02435"
pdf_url: "https://arxiv.org/pdf/2512.02435v2"
categories:
  - "cs.LG"
tags:
  - "强化学习"
  - "离线强化学习"
  - "跨域学习"
  - "数据过滤"
  - "策略学习"
  - "决策"
relevance_score: 5.5
---

# Efficient Cross-Domain Offline Reinforcement Learning with Dynamics- and Value-Aligned Data Filtering

## 原始摘要

Cross-domain offline reinforcement learning (RL) aims to train a well-performing agent in the target environment, leveraging both a limited target domain dataset and a source domain dataset with (possibly) sufficient data coverage. Due to the underlying dynamics misalignment between source and target domains, naively merging the two datasets may incur inferior performance. Recent advances address this issue by selectively leveraging source domain samples whose dynamics align well with the target domain. However, our work demonstrates that dynamics alignment alone is insufficient, by examining the limitations of prior frameworks and deriving a new target domain sub-optimality bound for the policy learned on the source domain. More importantly, our theory underscores an additional need for \textit{value alignment}, i.e., selecting high-quality, high-value samples from the source domain, a critical dimension overlooked by existing works. Motivated by such theoretical insight, we propose \textbf{\underline{D}}ynamics- and \textbf{\underline{V}}alue-aligned \textbf{\underline{D}}ata \textbf{\underline{F}}iltering (DVDF) method, a novel unified cross-domain RL framework that selectively incorporates source domain samples exhibiting strong alignment in \textit{both dynamics and values}. We empirically study a range of dynamics shift scenarios, including kinematic and morphology shifts, and evaluate DVDF on various tasks and datasets, even in the challenging setting where the target domain dataset contains an extremely limited amount of data. Extensive experiments demonstrate that DVDF consistently outperforms strong baselines with significant improvements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决跨领域离线强化学习中的一个核心挑战：如何有效利用源领域（通常数据较丰富）的数据来提升在目标领域（数据有限）的策略性能，同时避免因领域间动态特性差异导致的性能下降。研究背景在于，现实应用中在线交互成本高昂或存在风险，离线强化学习通过利用预先收集的静态数据集进行学习，但目标领域数据往往有限，限制了策略性能。现有方法（如IGDF、OTDF等）主要通过动态对齐的数据筛选，选择与目标领域动态特性对齐的源领域样本进行训练，以缓解分布偏移问题。然而，这些方法存在不足：它们仅关注动态对齐，却忽视了样本的价值对齐（即样本本身的质量和潜在价值）。论文指出，仅依赖动态对齐可能选择低质量但动态对齐的样本，而忽略高质量但动态略有偏差的样本（如专家数据），从而限制策略学习效果。因此，本文要解决的核心问题是：如何设计一种跨领域离线强化学习方法，能同时考虑动态对齐和价值对齐，以更智能地筛选源领域数据，从而在目标领域学习出高性能策略。为此，论文提出了DVDF方法，通过理论分析推导了目标领域策略次优性的新边界，强调两者对齐的必要性，并设计统一框架实现动态与价值对齐的协同数据筛选。

### Q2: 有哪些相关研究？

本文的研究领域是跨域离线强化学习，相关工作主要围绕如何处理源域和目标域之间的动态不匹配问题。相关研究可分为以下几类：

**1. 基于动态对齐的数据筛选方法：**
这是最直接相关的类别。先前工作（如IGDF等）的核心思想是，仅从源域中选择那些动态特性（即状态转移概率）与目标域对齐的样本来进行训练。这类方法假设动态对齐是跨域迁移成功的关键。然而，本文通过理论分析和实验证明，仅依赖动态对齐是不够的，因为它可能引入低价值或次优的源域数据，从而限制目标域策略的性能上限。

**2. 通用离线强化学习方法：**
本文的基线包括经典的离线RL算法，如保守Q学习（CQL）、隐式Q学习（IQL）等。这些方法并非专门为跨域设计，通常直接混合源域和目标域数据进行训练。本文指出，在存在动态偏移的情况下，这种简单混合会导致性能下降，从而凸显了进行跨域数据筛选的必要性。

**3. 领域自适应与迁移学习：**
更广泛地看，相关工作还包括机器人学和控制领域中的领域自适应方法，这些方法旨在补偿模拟器与现实世界之间的差异（即“模拟到现实”问题）。它们可能涉及动态模型辨识或策略自适应。本文的跨域离线RL设定与之有相似之处，但更侧重于在**纯离线、数据受限**的场景下，利用来自不同动态的静态数据集进行策略学习。

**本文与这些工作的关系和区别：**
本文与第一类方法（动态对齐筛选）关系最为密切，但提出了根本性的批评和扩展。本文的理论推导表明，除了**动态对齐**，**价值对齐**（即筛选出高价值、高质量的源域样本）同样至关重要。这是现有工作所忽视的一个关键维度。因此，本文提出的DVDF方法是一个统一的框架，同时基于动态和价值两个标准对源域数据进行筛选，从而在理论依据和方法设计上都超越了先前仅关注动态对齐的工作。在实验上，本文在运动学和形态学变化等多种动态偏移场景中验证了DVDF的优越性，特别是在目标域数据极少的极端情况下。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DVDF（动态与价值对齐数据过滤）的统一框架来解决跨域离线强化学习中源域和目标域动态不一致以及源域数据质量参差不齐的问题。其核心方法是**同时考虑动态对齐和价值对齐**，有选择地利用源域中与目标域动态一致且具有高价值（即接近源域最优策略）的样本。

**整体框架与主要模块**：
DVDF采用数据过滤范式，其流程主要包含三个关键模块：
1.  **价值失准度量模块**：为了量化价值对齐程度，论文推导出价值失准（学习策略与源域样本内最优策略的性能差距）的下界，该下界与源域行为策略数据分布下的优势函数期望值相关。因此，论文提出使用**源域样本内最优优势函数**作为价值失准的代理指标。为了获得该优势函数，论文采用**稀疏Q学习（SQL）算法**在源域数据集上进行预训练，以获得一个高性能策略及其对应的Q函数和V函数，进而计算优势函数 \(\hat{A}_{pre}(s,a) = \hat{Q}_{pre}(s,a) - \hat{V}_{pre}(s)\)。选择SQL是因为它既能实现接近样本内最优的性能，又能提供更可靠的优势估计，满足了算法性能和优势估计准确性的双重需求。
2.  **动态失准度量模块**：此模块负责评估动态对齐程度。论文借鉴了现有方法（如IGDF），采用**对比学习**来训练一个评分函数 \(h(s,a,s')\)。该函数通过噪声对比估计（NCE）损失进行训练，能够对符合目标域动态的转移 \((s, a, s')\) 给出高分，对不符合的给出低分。
3.  **统一过滤与训练模块**：将上述两个指标结合，构建一个统一的评分函数 \(g(s,a,s') = \lambda \cdot h(s,a,s') + (1-\lambda) \cdot Norm(\hat{A}_{pre}(s,a))\)，其中 \(\lambda\) 是超参数，\(Norm\) 是归一化操作。该函数平衡了动态对齐和价值对齐。在训练时，算法从源域数据批次中筛选出 \(g\) 值最高的前 \(\xi\) 分位数样本，并在其时序差分（TD）误差损失项中乘以权重 \(w \cdot g\)（其中 \(w\) 为指示函数），然后与目标域数据一起用于更新Q函数。最后，使用如IQL等离线RL算法更新策略。

**创新点**：
1.  **理论创新**：论文通过理论分析指出，仅进行动态对齐是不充分的，并首次明确强调了**价值对齐**（即选择源域中高质量、高价值的样本）对于跨域离线RL同等重要，并为此提供了理论边界支撑。
2.  **方法创新**：提出了首个**同时考虑动态与价值对齐**的跨域数据过滤框架（DVDF）。其价值对齐度量基于对样本内最优优势函数的近似，这与之前仅从价值差异角度间接反映动态对齐的工作（如VGDF）有本质区别。
3.  **实用创新**：DVDF设计为一个**即插即用**的模块，可以与不同的底层动态对齐方法（如基于对比学习的IGDF或基于最优传输的OTDF）灵活结合，形成DVDF-IGDF和DVDF-OTDF等变体，增强了方法的通用性。实验表明，该方法在多种动态偏移场景和极少量目标域数据的情况下，均能显著超越现有基线。

### Q4: 论文做了哪些实验？

论文在多种具有动力学偏移的环境中进行了广泛的实验。实验设置方面，考虑了运动学偏移和形态学偏移两种类型，应用于OpenAI Gym中的四个任务（halfcheetah、hopper、walker2d、ant）。目标域数据集从D4RL离线数据集中采样10%的数据构成，源域数据集则通过在修改后的环境中收集获得，包含随机、中等、中等回放、中等专家和专家五种数据质量，每个约100万样本，总计40个源域和20个目标域数据集。此外，还测试了目标域仅含5000条数据的极低数据量场景。

对比方法包括直接在混合数据上训练的IQL，以及BOSA、DARA、IGDF和OTDF等基线方法。论文提出的DVDF方法实现了DVDF-IGDF和DVDF-OTDF两个变体进行比较。

主要结果显示，在运动学偏移下，DVDF-IGDF在20个任务中的16个上超越了基础算法IGDF，DVDF-OTDF在15个任务上超越了OTDF。DVDF使IGDF和OTDF的总归一化得分分别提升了16.3%（从1001.6到1164.7）和18.8%（从986.5到1172.3）。在包含高质量样本的数据集上，DVDF优势更为明显。消融实验表明，使用SQL预训练的优势函数进行数据过滤比IQL预训练性能更优，因为SQL能提供更准确的优势估计误差。参数敏感性分析显示，权衡系数λ=0.7和选择比例ξ=0.5能在动态对齐与价值对齐之间取得有效平衡，获得较优性能。

### Q5: 有什么可以进一步探索的点？

本文提出的DVDF方法虽在跨域离线强化学习中表现出色，但仍存在一些局限性和可探索方向。首先，该方法依赖于预训练的优势函数来评估价值对齐，这在目标域数据极稀疏时可能不够准确，未来可研究更稳健的价值估计方法，例如引入不确定性量化或基于模型的价值预测。其次，当前框架主要处理动态和价值的静态对齐，未考虑跨域策略的渐进适配过程，可探索在线或增量式数据过滤机制，使智能体在交互中动态调整源域数据的使用。此外，实验集中于运动学和形态学变化，未来可扩展到更复杂的语义或视觉域差异，并探索如何结合元学习或迁移学习技术来提升跨域泛化能力。最后，理论分析虽揭示了动态与价值对齐的必要性，但未深入探讨两者间的权衡机制，未来可建立更精细的理论框架，指导在不同数据分布下优化过滤策略。

### Q6: 总结一下论文的主要内容

这篇论文针对跨领域离线强化学习中的核心挑战，即如何有效利用源领域数据来提升目标领域的策略性能。论文指出，现有方法主要关注源领域与目标领域之间的**动态对齐**（即状态转移概率的相似性），但作者通过理论分析和实例证明，仅考虑动态对齐是不充分的，甚至可能因选择了动态对齐但质量低劣的样本而损害性能。

论文的核心贡献在于，首次从理论上推导了策略在目标领域的次优性边界，并明确指出**价值对齐**（即选择高价值、高质量的源领域样本）与动态对齐同等重要。基于这一理论洞见，作者提出了一个新颖的统一框架——**动态与价值对齐数据过滤**（DVDF）。该方法通过预训练的**优势函数**来量化价值对齐程度，并结合现有的动态对齐过滤机制，在两者间进行权衡，从而有选择地融合源领域数据来训练策略。DVDF被设计为一个即插即用的模块，可以无缝集成到现有方法中。

实验部分在包括运动学和形态学变化在内的多种动态偏移场景中进行了验证。结果表明，DVDF在多个任务和数据集上均显著优于现有基线方法，即使在目标领域数据量极其有限的极端挑战性设置下，也能展现出卓越的性能。这项工作为跨领域离线强化学习提供了新的理论视角和有效的实践方案。
