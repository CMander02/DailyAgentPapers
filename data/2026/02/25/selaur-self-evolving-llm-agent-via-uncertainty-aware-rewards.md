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
pdf_url: "https://arxiv.org/pdf/2602.21158v2"
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
relevance_score: 9.5
---

# SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

## 原始摘要

Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards, a reinforcement learning framework that incorporates uncertainty directly into the reward design. SELAUR integrates entropy-, least-confidence-, and margin-based metrics into a combined token-level uncertainty estimate, providing dense confidence-aligned supervision, and employs a failure-aware reward reshaping mechanism that injects these uncertainty signals into step- and trajectory-level rewards to improve exploration efficiency and learning stability. Experiments on two benchmarks, ALFWorld and WebShop, show that our method consistently improves success rates over strong baselines. Ablation studies further demonstrate how uncertainty signals enhance exploration and robustness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为多步决策智能体进行强化学习时，奖励设计未能充分利用模型内在不确定性的问题。研究背景是LLM正从单轮问答任务演变为能够进行多步推理和决策的交互式智能体，例如在ALFWorld或WebShop等环境中执行一系列动作以达成目标。强化学习是优化此类智能体的常用范式。现有方法，包括传统的基于最终结果的奖励分配和近期引入的步级信用分配方法，虽然能提供更细粒度的学习信号，但普遍存在一个主要局限：它们忽视了LLM本身固有的不确定性。这种不确定性反映了模型的置信度，能指示何处需要探索，并且即使在失败的轨迹中也能提供有价值的学习线索，而现有方法未能有效利用这一关键信号。

因此，本文要解决的核心问题是：如何将LLM的内在不确定性显式地整合到奖励设计中，以更好地引导智能体的学习。具体而言，论文提出了SELAUR框架，通过集成基于熵、最小置信度和间隔的令牌级不确定性估计，构建统一的置信度度量，并设计一种失败感知的奖励重塑机制，将这些不确定性信号注入步级和轨迹级奖励中。这旨在使智能体不仅能利用不确定性来增强探索效率，还能从失败经验中提取有价值的信息，从而提升策略学习的平衡性和稳定性，最终提高任务成功率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：不确定性量化（UQ）和LLM智能体与强化学习。

在**不确定性量化**方面，已有研究利用词元级熵和一致性度量来检测不可靠输出、提升鲁棒性，并应用于答案验证、选择性问答、幻觉检测、持续学习、主动检索增强生成（RAG）及LLM自我改进等任务。这些工作表明不确定性是可靠性的重要指标。在强化学习中，不确定性也被用于驱动探索（如内在动机）。然而，现有研究很少将不确定性信号明确整合到LLM智能体的训练中。本文的SELAUR框架填补了这一空白，通过词元级不确定性来塑造步骤级和轨迹级奖励，使智能体能在利用已有知识和探索不确定策略之间取得平衡。

在**LLM智能体与强化学习**方面，先前工作通过提示工程、工具增强和轨迹优化（如思维链提示、规划-执行框架）来提升智能体性能，但这些方法常依赖监督轨迹，泛化能力有限。强化学习（如RLHF）虽能优化最终输出，但其基于结果的奖励通常稀疏，对中间推理步骤指导不足。步骤级信用分配方法虽能分配奖励，但普遍忽略了模型不确定性。近期智能体强化学习框架（如ReAct、Voyager、Reflexion）利用了过程级反馈，但仍严重依赖外部或自我生成的评估。相比之下，SELAUR利用基于不确定性的内在奖励作为内部学习信号，将低置信度或失败的推理步骤转化为结构化反馈，从而提供密集、信息丰富的监督，无需依赖外部环境奖励或反思启发式方法。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SELAUR的强化学习框架来解决LLM智能体在决策过程中因奖励信号稀疏而导致的探索效率低和学习稳定性差的问题。其核心方法是**将LLM的内在不确定性直接整合到奖励设计中**，从而为智能体提供密集的、与模型置信度对齐的学习信号。

**整体框架与主要模块**：
SELAUR的架构包含三个核心模块：
1.  **不确定性估计**：这是方法的基础。为了全面量化模型在每个解码步骤（token级别）的不确定性，论文没有依赖单一指标，而是**融合了三种互补的度量**：**熵**（衡量整个词汇表概率分布的分散程度）、**最小置信度**（基于被选中token的概率）和**间隔**（基于top-2 token概率的差距）。这三种度量分别捕捉了全局分布、局部决策信心和相对区分度。通过可调权重将它们线性聚合，形成一个统一的token级不确定性分数。
2.  **步骤与轨迹聚合**：为了将细粒度的token级不确定性转化为适用于强化学习的奖励信号，设计了分层聚合机制。**步骤级聚合**将同一决策步骤内所有token的不确定性取平均，得到该步骤的不确定性。**轨迹级聚合**则对一个完整决策序列（轨迹）中的所有步骤不确定性进行**指数折扣聚合**，赋予后期步骤更高的权重，因为后期决策往往对最终成败更具决定性。
3.  **失败感知的奖励重塑**：这是驱动学习的关键创新模块。在标准的成功/失败二元奖励基础上，SELAUR对**失败的轨迹**进行奖励重塑。具体而言，**步骤级奖励**被增强，加入了该步骤归一化的不确定性值，为失败的每一步提供反馈。**轨迹级奖励**则直接用整个轨迹的聚合不确定性来替代原有的零奖励。对于成功的轨迹，则仍使用标准奖励。这种机制确保失败经验不再被简单丢弃，而是转化为指导模型探索和修正其策略的宝贵信号。

**创新点**：
1.  **不确定性作为核心奖励信号**：首次系统性地将LLM的多维度内在不确定性（熵、置信度、间隔）量化和整合，并直接用于塑造强化学习奖励，为智能体提供了传统二元奖励之外的关键学习线索。
2.  **分层与时间加权的聚合设计**：通过从token到步骤再到轨迹的分层聚合，并结合对轨迹后期步骤的强调，使奖励信号既能反映细粒度的决策犹豫，又能体现决策序列的整体置信趋势。
3.  **失败感知的差异化训练**：创新性地提出仅对失败轨迹注入不确定性奖励，而对成功轨迹保留标准奖励。这种非对称的奖励重塑机制，既能利用失败中的信息促进探索和鲁棒性，又不会干扰成功策略的稳定性，有效提升了学习效率。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个交互式基准测试上进行了实验。实验设置方面，使用NVIDIA A100和H100 GPU，学习率为1e-6，训练步数为150，rollout大小为8。ALFWorld的最大交互步数设为50，WebShop设为15。对比方法包括纯提示（prompting）、PPO、RLOO、GRPO和GiGPO。主要评估指标是任务成功率，WebShop额外报告任务分数。

主要结果显示，在Qwen2.5-1.5B模型上，SELAUR在ALFWorld的总体平均成功率为89.06%，优于GiGPO的88.28%；在WebShop上任务分数为0.8812，成功率为76.56%，均高于基线。在Qwen2.5-7B模型上，SELAUR在ALFWorld达到96.87%的成功率，WebShop任务分数为0.8935，成功率为79.68%，同样领先。消融实验表明，结合熵、最小置信度和间隔三种不确定性度量（任务分数0.8812，成功率76.56%）优于任何单一或双度量组合。此外，与负奖励或指数衰减奖励等变体相比，SELAUR的奖励设计在探索与利用间取得了更好平衡，在ALFWorld和WebShop上分别取得89.06%和76.56%的成功率。定性分析显示，SELAUR能通过不确定性感知引导更高效地探索，避免陷入局部循环。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估主要集中于文本交互环境（ALFWorld和WebShop），尚未扩展到视觉或多模态任务，也未涉及高维观测或更复杂的不确定性形式（如模型间分歧或外部知识不确定性）。未来研究可首先探索将不确定性奖励机制应用于具身智能或机器人控制等视觉密集型领域，其中感知不确定性可能对决策产生关键影响。其次，可研究动态不确定性融合方法，根据任务阶段自适应调整不同不确定性指标（如熵、最小置信度）的权重，而非固定组合。此外，当前方法依赖于LLM本身的不确定性估计，未来可结合贝叶斯深度学习或集成方法提升估计可靠性。另一个方向是将不确定性奖励与课程学习结合，让智能体从低不确定性任务逐步过渡到高不确定性场景，以提升学习效率。最后，可探索不确定性信号在多智能体协作中的应用，通过共享不确定性信息促进群体探索与分工优化。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为SELAUR的新型强化学习框架，旨在通过将大语言模型的内在不确定性直接融入奖励设计，来提升其作为多步决策智能体的性能。核心问题是现有方法在奖励塑造和信用分配中普遍忽略了LLM的不确定性信号，而该信号能反映模型置信度、指示探索需求，并提供有价值的学习线索。

方法上，SELAUR整合了基于熵、最小置信度和间隔的度量，构建了一个综合的令牌级不确定性估计，从而提供密集的、与置信度对齐的监督。同时，它采用了一种失败感知的奖励重塑机制，将这些不确定性信号注入到步骤级和轨迹级奖励中，以提高探索效率和学习的稳定性。

主要结论是，在ALFWorld和WebShop两个基准测试上的实验表明，该方法持续提升了成功率，优于现有基线。消融研究进一步证实了不确定性信号在增强探索能力和鲁棒性方面的关键作用。其核心贡献在于首次系统地将LLM不确定性量化为奖励，为构建能自我演进的智能体提供了一种新颖且有效的学习范式。
