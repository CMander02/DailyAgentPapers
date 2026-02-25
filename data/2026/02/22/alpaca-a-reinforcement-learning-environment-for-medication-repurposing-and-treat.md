---
title: "ALPACA: A Reinforcement Learning Environment for Medication Repurposing and Treatment Optimization in Alzheimer's Disease"
authors:
  - "Nolan Brady"
  - "Tom Yeh"
date: "2026-02-22"
arxiv_id: "2602.19298"
arxiv_url: "https://arxiv.org/abs/2602.19298"
pdf_url: "https://arxiv.org/pdf/2602.19298v1"
categories:
  - "cs.AI"
tags:
  - "强化学习"
  - "决策"
  - "个性化治疗"
  - "医疗AI"
  - "环境模拟"
relevance_score: 6.0
---

# ALPACA: A Reinforcement Learning Environment for Medication Repurposing and Treatment Optimization in Alzheimer's Disease

## 原始摘要

Evaluating personalized, sequential treatment strategies for Alzheimer's disease (AD) using clinical trials is often impractical due to long disease horizons and substantial inter-patient heterogeneity. To address these constraints, we present the Alzheimer's Learning Platform for Adaptive Care Agents (ALPACA), an open-source, Gym-compatible reinforcement learning (RL) environment for systematically exploring personalized treatment strategies using existing therapies. ALPACA is powered by the Continuous Action-conditioned State Transitions (CAST) model trained on longitudinal trajectories from the Alzheimer's Disease Neuroimaging Initiative (ADNI), enabling medication-conditioned simulation of disease progression under alternative treatment decisions. We show that CAST autoregressively generates realistic medication-conditioned trajectories and that RL policies trained in ALPACA outperform no-treatment and behavior-cloned clinician baselines on memory-related outcomes. Interpretability analyses further indicated that the learned policies relied on clinically meaningful patient features when selecting actions. Overall, ALPACA provides a reusable in silico testbed for studying individualized sequential treatment decision-making for AD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决阿尔茨海默病（AD）个性化、序贯治疗策略开发中的现实瓶颈。由于AD病程漫长、患者异质性大，通过传统临床试验系统探索不同药物组合、用药时机和动态调整方案成本极高且不切实际。为此，研究者构建了ALPACA——一个开源的、与Gym兼容的强化学习环境，其核心是一个基于ADNI纵向数据训练的、能模拟药物干预下疾病进展的CAST模型。该平台将临床状态建模为连续变量，并定义了包含17类药物（多二元动作空间）的治疗选择，从而在计算机中创建了一个可重复、可扩展的“硅基试验床”。它允许研究者安全、高效地利用强化学习探索庞大的个性化治疗决策空间（包括药物再利用和联合用药策略），以优化长期结局，特别是记忆相关指标，并理解策略的决策依据，最终为克服现实世界临床试验的局限性提供一条新路径。

### Q2: 有哪些相关研究？

相关研究主要分为两个互补领域：基于模拟的离线医疗强化学习环境，以及现有的阿尔茨海默病（AD）强化学习环境。

在离线医疗强化学习方面，研究面临两大挑战：分布不匹配导致的策略外推误差，以及策略评估的高方差问题。相关工作包括：Fujimoto等人提出的离线策略深度强化学习方法，指出了未见动作导致价值估计不可靠的问题；Huang等人通过约束策略以接近临床医生行为来提升安全性；Uehara等人则关注离线策略评估中的分布偏移。为缓解这些问题，离线模型强化学习（MBRL）通过从回顾性数据学习动态模型进行策略优化。代表性工作有Yu等人的MOPO，它通过模型不确定性惩罚来管理分布偏移；以及医疗领域的TR-GAN和OMG-RL，分别利用对抗性学习和推断奖励进行治疗方案推荐。ALPACA将这一离线MBRL范式扩展到了AD领域。

在AD特定环境方面，已有研究构建了基于离散马尔可夫决策过程的环境，如Bhattarai等人的工作，它将连续认知测量映射到有限疾病阶段并使用离散动作集，但限制了治疗策略的多样性。另一项工作由Saboo等人完成，他们开发了基于微分方程的机制模拟，但主要用于模拟大脑对病理的反应，而非优化序列治疗决策。ALPACA针对现有环境的局限性（如粗粒度状态抽象和有限动作空间），通过建模连续临床状态和使用自回归的、药物条件化的状态转移，提供了一个支持在17个治疗类别上进行反事实推演的、可重复使用的环境。

### Q3: 论文如何解决这个问题？

ALPACA 通过构建一个基于强化学习的仿真环境来解决阿尔茨海默病（AD）个性化、序贯治疗策略评估的难题。其核心方法围绕一个名为 CAST 的疾病进展预测模型和包裹该模型的 Gym 兼容 RL 环境展开。

**核心方法与架构设计：**
1.  **CAST 预测模型**：作为环境的核心引擎，CAST 是一个采用**混合专家（MoE）架构的 Transformer 模型**，旨在捕捉 AD 进展的异质性。它接收患者当前状态（21个临床变量）、治疗动作（17个多二元药物类别）及下次访视时间间隔，以自回归方式预测下一时间点的患者状态（包括生物标志物和认知评分）。MoE 设计让不同专家专注于不同医疗场景，提高了轨迹预测的保真度。
2.  **ALPACA 环境封装**：环境以 CAST 模型作为状态转移函数。为保护隐私并生成多样化的虚拟患者，初始状态并非使用真实数据，而是通过**高斯混合模型（GMM）** 从 ADNI 训练集的初始状态分布中采样得到。环境设定了合理的动作约束（如选择“无药物”时不能选择其他治疗）和状态有效性检查（特征需在训练分布三个标准差内），以防止智能体利用模拟缺陷。
3.  **奖励函数设计**：奖励信号以 **ADNI-Mem（记忆综合评分）的变化**为核心，该评分与神经精神症状严重程度强相关。奖励计算为连续状态间 ADNI-Mem 的变化，并经过基于测量标准误的缩放和裁剪，旨在鼓励改善或维持记忆功能。

**关键技术：**
-   **数据预处理与建模**：利用 ADNI 纵向数据，通过基于 ExtraTrees 的方法处理缺失值，并将药物记录整合为治疗类别。训练 CAST 时采用复合损失函数（均方误差、二元交叉熵和辅助的负载均衡损失），并使用最大平均差异（MMD）和 Mantel 检验来验证预测轨迹与真实轨迹在分布和时序关系上的相似性。
-   **多基准策略训练与评估**：在环境中训练了 PPO、A2C、SAC 和 BDQ 四种 RL 智能体作为基准策略，并与行为克隆的临床医生策略、启发式策略及无治疗基线进行比较。评估时，所有策略在由相同初始状态构成的 1000 个模拟患者队列上进行滚动执行，以确保公平对比。
-   **策略可解释性分析**：使用 **SHAP 分析** 来解释学习到的策略。分析表明，智能体在决定“无药物”或“AD 治疗”时，依赖于具有临床意义的特征（如记忆评分、脑体积、tau 蛋白水平等），其决策模式与疾病严重程度的生物学标记一致，验证了环境提供的是有临床意义的学习信号，而非可被“奖励黑客”利用的伪信号。

通过这套架构，ALPACA 成功创建了一个可重复使用的计算测试平台，使 RL 智能体能够探索优于临床医生基线的个性化序贯治疗策略，并为理解其决策逻辑提供了临床可解释的依据。

### Q4: 论文做了哪些实验？

论文实验主要包括基准策略训练与评估、行为克隆分析以及策略可解释性分析。实验设置上，研究者首先在ALPACA环境中训练了四种基于强化学习的治疗策略：PPO、A2C、SAC和BDQ，使用Stable Baselines3等工具，在四个并行环境中训练50万步，并对输入状态进行归一化处理。作为对比，还训练了一个基于行为克隆的临床医生策略（使用贝叶斯前馈神经网络模拟ADNI数据中的医生决策）以及一个基于临床指南的启发式策略（当ADNI-Mem分数低于-0.1时选择“AD治疗”，否则“无药物”）。

基准测试方面，所有策略在由ALPACA初始状态模型生成的1000个相同患者队列上进行评估，通过模拟推演计算累积奖励、每步奖励和最终ADNI-Mem分数等指标。主要结果显示，所有强化学习策略在统计上均显著优于无治疗基线和行为克隆的临床医生策略（p<0.001）。其中PPO表现最佳，获得了最高的累积奖励（3.38）和最终ADNI-Mem分数（-0.46），而行为克隆的临床医生策略在精确匹配所有17种药物组合上仅19.9%的准确率，但单个药物预测匹配率达91%。

此外，通过SHAP分析评估策略的可解释性，发现学习到的策略依赖具有临床意义的特征：例如，较高的记忆分数和海马体积会增加选择“无药物”行动的概率，而较高的脑室体积（与皮质萎缩相关）则会增加选择“AD治疗”的概率。这些模式表明策略学习到了与阿尔茨海默病严重程度相关的生物标志物，而非利用环境缺陷。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于其模拟环境基于历史观测数据，无法完全捕捉真实世界治疗的复杂因果机制，且模型性能受限于训练数据的质量和覆盖范围。未来可进一步探索的方向包括：第一，将环境扩展至多模态数据（如影像、基因组学），以更全面地建模疾病异质性；第二，开发更先进的解释性强化学习方法，专门处理多药联用和长期时序依赖，提升策略的可信度；第三，利用ALPACA进行临床试验模拟优化，例如通过机制分组药物来指导患者分层，减少实际试验中的潜在干扰；第四，结合因果推断方法增强模型的泛化能力，使其能更好地支持个性化治疗假设的生成与验证。

### Q6: 总结一下论文的主要内容

该论文提出了ALPACA（阿尔茨海默病自适应护理智能体学习平台），这是一个开源的、兼容Gym的强化学习环境，专门用于阿尔茨海默病的药物再利用和治疗优化研究。其核心贡献在于构建了一个由药物条件预测模型驱动的仿真平台，该模型基于ADNI的纵向临床数据训练，能够模拟不同治疗决策下的疾病进展。研究表明，在该环境中训练的强化学习策略，在改善记忆相关结局方面优于无治疗和模仿临床医生行为的基线策略，且其决策依赖于具有临床意义的患者特征。ALPACA的意义在于为个性化、序列化的治疗决策提供了一个可重复的、基于计算机的测试平台，克服了传统临床试验周期长、患者异质性大的限制，是迈向临床实用AD模拟环境的重要一步。当前版本存在动作离散、时间分辨率较粗等局限，为未来扩展指明了方向。
