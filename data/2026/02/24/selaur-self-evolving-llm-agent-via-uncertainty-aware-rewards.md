---
title: "SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards"
authors:
  - "Dengjia Zhang"
  - "Xiaoou Liu"
  - "Lu Cheng"
  - "Yaqing Wang"
  - "Kenton Murray"
  - "Hua Wei"
date: "2026-02-24"
arxiv_id: "2602.21158"
arxiv_url: "https://arxiv.org/abs/2602.21158"
pdf_url: "https://arxiv.org/pdf/2602.21158v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent自演化"
  - "强化学习"
  - "奖励设计"
  - "不确定性估计"
  - "探索效率"
  - "决策智能体"
  - "LLM Agent"
  - "Agent架构"
relevance_score: 9.5
---

# SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

## 原始摘要

Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards, a reinforcement learning framework that incorporates uncertainty directly into the reward design. SELAUR integrates entropy-, least-confidence-, and margin-based metrics into a combined token-level uncertainty estimate, providing dense confidence-aligned supervision, and employs a failure-aware reward reshaping mechanism that injects these uncertainty signals into step- and trajectory-level rewards to improve exploration efficiency and learning stability. Experiments on two benchmarks, ALFWorld and WebShop, show that our method consistently improves success rates over strong baselines. Ablation studies further demonstrate how uncertainty signals enhance exploration and robustness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型作为多步决策智能体时，奖励设计未能有效利用模型内在不确定性的问题。研究背景是，随着LLMs从单轮问答任务扩展到多步推理与决策的交互式智能体，强化学习成为优化这类智能体的常用范式。现有方法，包括传统的基于最终结果的奖励分配和近期引入的步级信用分配方法，虽然能提供更细粒度的学习信号，但普遍存在一个关键局限：它们忽视了LLMs本身固有的不确定性。这种不确定性反映了模型的置信度，能指示何处需要探索，即使在失败的轨迹中也能提供有价值的学习线索，而现有方法未能将其整合到奖励设计中。

因此，本文要解决的核心问题是：如何将LLM的内在不确定性系统地融入智能体的奖励设计中，以提供更密集、与置信度对齐的监督信号，从而提升智能体的探索效率、学习稳定性，并能从失败经验中提取有价值的信息。为此，论文提出了SELAUR框架，通过集成多种词元级不确定性度量并构建统一的估计，进而将这些不确定性信号注入步级和轨迹级奖励中，实现失败感知的奖励重塑。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：不确定性量化（UQ）在LLMs中的应用，以及LLM智能体与强化学习（RL）的结合。

在**不确定性量化**方面，已有研究利用词元级熵和一致性度量来检测不可靠输出、提升鲁棒性，并应用于答案验证、选择性问答、幻觉检测和持续学习等任务。这些工作表明不确定性是可靠性的重要指标。在RL领域，不确定性也被用于驱动探索（如内在动机）。然而，现有研究很少将不确定性信号明确整合到LLM智能体的训练中。本文的SELAUR框架填补了这一空白，它利用词元级不确定性来塑造步骤级和轨迹级奖励，使智能体能在利用已有知识和探索不确定策略之间取得平衡。

在**LLM智能体与强化学习**方面，先前工作通过提示工程、工具增强和轨迹优化来提升智能体在ALFWorld和WebShop等基准上的表现。RL方法（如RLHF）虽能优化最终输出，但其基于结果的奖励通常稀疏，对中间推理步骤指导有限。步骤级信用分配方法试图解决此问题，但普遍忽略了模型不确定性。近期智能体RL框架（如ReAct、Voyager）依赖于外部或自我生成的评估反馈。相比之下，SELAUR创新地利用基于不确定性的内在奖励作为内部学习信号，将低置信度或失败的推理步骤转化为结构化反馈，从而提供密集的监督，减少对外部奖励或反思启发式的依赖。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SELAUR的强化学习框架来解决LLM智能体在决策过程中因奖励信号稀疏而导致的探索效率低和学习稳定性差的问题。其核心方法是**将LLM的内在不确定性直接整合到奖励设计中**，从而为失败轨迹提供密集的学习信号，引导智能体更有效地探索和优化策略。

**整体框架与主要模块**：
SELAUR的架构包含三个核心模块：
1.  **不确定性估计**：在模型解码的每个步骤，从**词元（token）级别**量化模型的不确定性。为了避免单一指标的局限性，论文创新性地融合了三种互补的度量方式：
    *   **熵**：衡量模型在整个词表上概率分布的分散程度，反映全局不确定性。
    *   **最小置信度**：基于模型对所选词元的预测概率，反映局部决策信心。
    *   **间隔**：计算模型预测中排名第一和第二词元的概率差，反映决策的模糊性。
    通过可调权重将三者结合，形成一个综合的词元级不确定性估计，从而从多个角度全面捕捉模型的预测可靠性。

2.  **步骤与轨迹聚合**：为了生成适用于强化学习的奖励信号，设计了分层聚合机制：
    *   **步骤级聚合**：将一个步骤内所有词元的不确定性取平均，得到该步骤的整体不确定性。
    *   **轨迹级聚合**：对整个决策序列（轨迹）中所有步骤的不确定性进行聚合。为了强调后期关键决策的影响，采用了**指数折扣聚合**，为更靠后的步骤分配更高的权重。

3.  **失败感知的奖励重塑**：这是框架的关键创新点，旨在利用失败轨迹中的信息。它根据任务的成功与否，对奖励进行差异化设计：
    *   对于**成功轨迹**，使用标准的成功奖励进行训练。
    *   对于**失败轨迹**，则将聚合得到的不确定性信号注入到奖励中。具体包括：
        *   **步骤级重塑**：用归一化的步骤不确定性来增强每一步的奖励信号。
        *   **轨迹级重塑**：用整个轨迹的不确定性来替代原始的失败奖励（如0奖励）。
    这种机制确保了失败经验不会被丢弃，而是转化为密集的、与模型置信度对齐的监督信号，鼓励智能体重新审视那些高不确定性的推理路径。

**创新点**：
1.  **首次系统地将LLM的内在不确定性作为核心奖励信号**引入到智能体强化学习框架中，弥补了传统稀疏奖励（仅基于最终成败）的不足。
2.  **提出了多视角融合的词元级不确定性估计方法**，结合熵、最小置信度和间隔，更全面地刻画模型决策时的犹豫和信心水平。
3.  **设计了失败感知的奖励重塑机制**，将不确定性信号以步骤级和轨迹级两种形式注入失败案例的奖励中，从而将失败转化为有价值的学习机会，显著提升了探索效率和学习的鲁棒性。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个交互式基准测试上进行了实验。实验设置方面，使用NVIDIA A100和H100 GPU，学习率为1e-6，训练步数为150，rollout大小为8。ALFWorld的最大交互步数设为50，WebShop设为15。对比方法包括纯提示（prompting）、PPO、RLOO、GRPO和GiGPO。主要评估指标为任务成功率，WebShop额外报告任务分数。

主要结果显示，在Qwen2.5-1.5B模型上，SELAUR在ALFWorld的总体平均成功率为89.06%，优于GiGPO的88.28%；在WebShop上任务分数为0.8812，成功率为76.56%，均高于其他基线。在Qwen2.5-7B模型上，SELAUR在ALFWorld达到96.87%的成功率，在WebShop任务分数为0.8935，成功率为79.68%，同样表现最佳。

消融实验探讨了不同不确定性度量的影响。在WebShop上，单独使用熵、最小置信度或间隔度量均不如三者结合（任务分数0.8812，成功率76.56%），表明它们是正交且互补的。此外，论文比较了不同的奖励函数设计，其中“负奖励”和“指数衰减”变体均不如SELAUR，后者在探索与利用间取得了更好平衡。可视化分析显示，SELAUR在训练后期保持了更高的熵值，促进了更广泛的探索。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估主要集中于文本交互环境（如ALFWorld和WebShop），尚未扩展到视觉或多模态任务，也未涉及高维观测或更复杂的不确定性形式。未来研究可首先探索将不确定性奖励机制应用于视觉语言模型（VLMs）或具身智能体，以处理图像、视频等模态中的置信度估计。其次，可研究动态不确定性融合方法，根据任务阶段自适应调整熵、最小置信度等指标的权重，而非固定组合。此外，当前方法依赖预定义的不确定性度量，未来可尝试让智能体通过元学习自主发现有效的置信度信号。另一个方向是将不确定性奖励与课程学习结合，逐步增加环境复杂度，以提升在稀疏奖励场景中的探索效率。最后，可探索不确定性估计对多智能体协作的促进作用，例如通过共享置信度信息来协调决策。

### Q6: 总结一下论文的主要内容

本文提出了一种名为SELAUR的新型强化学习框架，旨在通过将大语言模型的内在不确定性直接融入奖励设计，来提升多步决策智能体的性能。其核心问题是传统方法在为大语言模型智能体设计奖励时，往往忽略了模型自身的不确定性这一关键信号，而该信号能有效反映模型置信度、指导探索方向并提供学习线索。

方法上，SELAUR首先结合基于熵、最小置信度和间隔的度量，构建了一个综合的令牌级不确定性估计。然后，它采用一种失败感知的奖励重塑机制，将这些密集的、与置信度对齐的不确定性信号注入到步骤级和轨迹级奖励中，从而改善探索效率和学习稳定性。

主要结论是，在ALFWorld和WebShop两个基准测试上的实验表明，该方法能持续提升成功率，优于现有基线。消融研究进一步证实了不确定性信号在增强探索能力和鲁棒性方面的关键作用。该工作的核心贡献在于首次系统地将LLM不确定性作为核心奖励信号，为提升智能体的自我演进和学习效率提供了新思路。
