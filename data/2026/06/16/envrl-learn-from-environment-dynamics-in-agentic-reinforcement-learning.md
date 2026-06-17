---
title: "EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning"
authors:
  - "Zhitong Wang"
  - "Songze Li"
  - "Hao Peng"
  - "Shuzheng Si"
  - "Yi Wang"
  - "Maosong Sun"
  - "Juanzi Li"
date: "2026-06-16"
arxiv_id: "2606.17680"
arxiv_url: "https://arxiv.org/abs/2606.17680"
pdf_url: "https://arxiv.org/pdf/2606.17680v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "强化学习"
  - "环境动力学"
  - "内部模型"
  - "辅助目标"
  - "状态预测"
  - "逆动力学"
  - "长程任务"
relevance_score: 9.5
---

# EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning

## 原始摘要

Reinforcement learning (RL) has emerged as a powerful paradigm for training Large Language Models (LLMs) as agents. However, conventional RL methods for long-horizon agentic tasks often struggle with sparse outcome rewards. Intuitively, this overlooks the rich environment dynamics information contained in rollout interaction trajectories. We argue that the interaction experience inherently serves as an implicit supervision signal, reveals the underlying transition mechanisms of the environment, and enables the agent to construct a more accurate internal model of the environment.. Therefore, in this work, we investigate how to leverage this additional signal to improve policy learning. Specifically, we propose EnvRL, a framework that incorporates environment dynamics learning into agentic RL via two auxiliary objectives: state prediction and inverse dynamics. By jointly optimizing with the primary RL objective, we encourage the agent to internalize environment dynamics from its own interaction experience. Extensive experiments on two long-horizon agentic benchmarks demonstrate that EnvRL achieves significant improvements on success-rates over RL-only baselines, e.g., when trained with GRPO, lifting Qwen-2.5-1.5B-Instruct from 72.8% to 77.4% on ALFWorld, and from 56.8% to 67.0% on WebShop.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在基于强化学习（RL）训练大语言模型（LLM）作为智能体时，现有方法在长周期、多轮交互任务中面临奖励稀疏的问题。研究背景是LLM被越来越广泛地部署为自主智能体，需要与环境进行多轮交互，完成复杂任务。现有方法如GRPO和RLOO主要依赖结果奖励，即只在完整回合结束时提供二值反馈（如成功或失败）。这种稀疏的奖励信号在长周期任务中学习效率低下，因为智能体在整个交互过程中缺乏有效的监督信号来指导其行为。

本文的核心观点是，智能体在环境交互中产生的轨迹数据本身包含了丰富的环境动态信息，如状态如何随动作变化、动作与状态变迁之间的因果关系。现有方法忽视了这些信息。因此，本文的核心问题是：如何有效地从智能体自身的交互经验中提取并利用环境动态信息，作为额外的监督信号来增强策略学习。

为解决这一问题，论文提出了EnvRL框架，通过引入两个辅助目标：状态预测（根据当前状态和动作预测下一状态）和逆动力学（根据状态转变推断导致这一转变的动作），来强制智能体学习环境动态。这些辅助目标与主RL目标联合优化，使得智能体能够内化环境动态，从而在复杂环境中做出更优的决策。该方法在ALFWorld和WebShop两个基准上显著提升了成功率。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：

1. **智能体强化学习方法类**：早期研究如DQN、PPO等经典算法用于游戏和控制等离散环境，近期GRPO等群体强化学习方法因其计算效率和稳定的优势估计被应用于网页导航、软件操作等复杂任务。这些方法面临的核心挑战是长周期任务中环境反馈稀疏导致的监督信号不足，现有工作主要通过识别中间状态发展细粒度信用分配方案来解决。本文与该类方法正交，不关注奖励分配，而是挖掘环境动力学中的隐式监督信号，可与其互补结合。

2. **环境动力学学习类**：通过从交互轨迹中学习环境状态转移机制来辅助决策，世界模型是典型代表，作为内部模拟器使代理通过潜在想象预测状态转移并规划动作，显著提升样本效率和泛化能力。本文与这类研究紧密相关，但区别于预训练世界模型，我们的方法通过探索新环境直接捕获转移机制，并将其作为额外监督信号优化策略学习。

综上，本文创新在于提出EnvRL框架，通过状态预测和逆向动力学两个辅助目标，将环境动力学学习融入强化学习主目标，与现有奖励驱动方法互补，在ALFWorld和WebShop等长周期任务中显著提升成功率。

### Q3: 论文如何解决这个问题？

EnvRL通过引入环境动力学学习来增强基于强化学习（RL）的智能体训练。其核心思想是在标准的RL训练过程中，利用智能体与环境的交互轨迹（rollout）作为隐式监督信号，帮助智能体构建更准确的环境内部模型。具体来说，论文设计了一个联合优化框架，整体架构包括以下三个并行训练的模块：

1. **状态预测（State Prediction, SP）**：该模块训练智能体根据当前状态 \( s_t \) 和执行的行动 \( a_t \) 来预测下一个环境状态 \( s_{t+1} \)（即下一步的文本观察）。这通过标准的token级交叉熵损失 \( \mathcal{L}_{SP} \) 来实现，相当于对自生成的交互经验进行监督微调，使智能体能够前向推理行为的长期后果。

2. **逆动力学（Inverse Dynamics, ID）**：该模块作为SP的互补，训练智能体根据连续的两个状态 \( (s_t, s_{t+1}) \) 反推导致这一状态变化的行动 \( a_t \)。其损失 \( \mathcal{L}_{ID} \) 同样基于交互轨迹生成。这有助于智能体过滤无关的环境细节，专注于自身可控的行为学。

3. **主RL目标**：并行使用传统的稀疏结果奖励（outcome reward）进行标准RL更新（如GRPO）。

**创新点**在于设计了两阶段动态权重机制。初始阶段，SP和ID的权重 \( \lambda_{SP} \) 和 \( \lambda_{ID} \) 较高，为智能体提供密集的环境动力学监督；随着训练步数 \( t \) 增加，使用余弦衰减调度（\( \lambda(t) = \lambda \cdot \frac{1}{2}(1+\cos(\pi \frac{t}{T_{max}})) \)）逐渐降低辅助损失权重，使优化目标平滑过渡到主RL奖励最大化，避免了固定权重导致的学习瓶颈。整体上，EnvdRL实现了从环境交互中自监督学习双向动力学模型，显著提升了长周期智能体任务的成功率。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个长程智能体基准上进行了实验。ALFWorld包含Pick、Look等六类家务任务，WebShop是模拟电商环境，使用成功率(Success Rate)和Score指标评估。

对比方法包括：直接提示(Prompting)、ReAct、GRPO、GiGPO以及本文提出的EnvRL（在GRPO和GiGPO基础上增加状态预测和逆动力学辅助目标）。使用Qwen2.5-1.5B/7B-Instruct作为基础模型，训练150步，学习率1e-6，辅助目标初始系数λ_SP=λ_ID=0.2（1.5B模型）/0.1（7B模型）。

主要结果：在1.5B模型上，EnvRL-GRPO将ALFWorld成功率从72.8%提升至77.4%，WebShop从56.8%提升至67.0%；EnvRL-GiGPO在ALFWorld上达到91.8%（+5.1点），WebShop为74.2%（+6.8点）。7B模型上，EnvRL-GiGPO分别达到94.5%和76.3%。消融实验表明，状态预测在逻辑性强的ALFWorld中更重要，逆动力学在含噪的WebShop中更关键；余弦衰减调度优于线性或无常衰减。数据规模实验显示性能随经验数据量增加而提升。样本效率分析显示EnvRL平均只用约68.5%的训练步数即可达到基线最终性能。此外，EnvRL在推理时交互轮次和响应长度均更短，并在分布外测试中表现更好。

### Q5: 有什么可以进一步探索的点？

该论文在环境动力学建模上取得了显著进展，但仍存在几方面局限与探索空间。首先，其辅助任务（状态预测与逆动力学）在当前框架中共享相同权重衰减机制，但不同任务对学习阶段的敏感度可能不同，未来可探索动态自适应权重分配或课程学习策略。其次，当前方法仅从rollout轨迹中学习环境转移规律，未显式利用任务奖励信号来校准动力学模型，可引入基于模型的强化学习思想，将学到的环境模型用于规划或假设推演。此外，逆动力学任务在多智能体或非确定性环境中可能面临歧义性问题，可考虑结合因果推断或对比学习来增强表征的鲁棒性。最后，虽然实验在ALFWorld和WebShop上提升显著，但环境复杂度有限，未来应在更具开放性、部分可观测的3D环境或具身智能场景中验证方法的有效性。

### Q6: 总结一下论文的主要内容

这篇论文提出EnvRL框架，解决了在长时序智能体任务中，传统强化学习因稀疏结果奖励而难以有效学习的问题。其核心贡献在于将环境动态学习融入智能体强化学习过程。方法上，EnvRL除了主RL目标外，引入状态预测和逆动态两个辅助目标，通过联合优化，使智能体从其自身的交互经验中学习并内化环境动态模型。实验表明，在ALFWorld和WebShop两个长时序基准上，EnvRL显著提升了任务成功率（例如，在GRPO训练下，Qwen-2.5-1.5B-Instruct模型的成功率分别从72.8%提升至77.4%，从56.8%提升至67.0%）。这项工作的意义在于，它为利用交互轨迹中隐含的环境动态信息提供了有效思路，有望开发出更稳健、样本高效的自主智能体。
