---
title: "Reducing Belief Deviation in Reinforcement Learning for Active Reasoning"
authors:
  - "Deyu Zou"
  - "Yongqiang Chen"
  - "Jianxiang Wang"
  - "Haochen Yang"
  - "Mufei Li"
  - "James Cheng"
  - "Pan Li"
  - "Yu Gong"
date: "2025-10-14"
arxiv_id: "2510.12264"
arxiv_url: "https://arxiv.org/abs/2510.12264"
pdf_url: "https://arxiv.org/pdf/2510.12264v2"
categories:
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "Active Reasoning"
  - "Belief Tracking"
  - "Policy Optimization"
  - "Training Stability"
  - "LLM Agent"
relevance_score: 9.0
---

# Reducing Belief Deviation in Reinforcement Learning for Active Reasoning

## 原始摘要

Active reasoning requires large language model (LLM) agents to interact with external sources and strategically gather information to solve problems in multiple turns. Central to this process is belief tracking: maintaining an accurate representation of the underlying state and uncertainty in understanding and solving the problem. However, due to limited reasoning capabilities, LLM-based agents often suffer belief deviation: their internal beliefs drift from the true problem state, leading to loss of state awareness and uninformative or repetitive actions. Once this happens, errors compound in the trajectories used for reinforcement learning (RL), leading to misattributed credits and limited exploration. To address this issue, we propose to track belief deviation and develop $\mathbf{T^3}$, a simple yet principled method that detects excessive deviation and truncates training trajectories to suppress uninformative tail effects. Hence, $\mathbf{T^3}$ preserves credits for informative prefixes and systematically improves policy optimization. Across 5 challenging tasks, $\mathbf{T^3}$ consistently enhances training stability and yields performance gains of up to 30 points while cutting token cost by up to 34%. These results highlight belief control as a key principle for building robust LLM agents capable of active reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在进行主动推理（Active Reasoning）时，由于内部信念偏离真实问题状态而导致的性能下降问题。研究背景是，尽管LLM在多种领域展现出强大的推理能力，并通过强化学习（RL）进行优化，但在需要多轮交互、主动从外部环境获取信息的复杂任务中，LLM智能体常常表现不佳，例如产生冗余、无关或非信息性的动作，甚至陷入无效循环。

现有方法的不足在于，标准的强化学习训练本身无法完全解决这些问题。论文指出，当LLM智能体被实例化为部分可观察马尔可夫决策过程（POMDP）中的代理时，其信念跟踪（即对问题状态和不确定性的内部表征）由于LLM有限的推理能力而存在固有缺陷。这种不完美的信念更新会导致智能体进入“信念陷阱区域”（Belief-Trap Region, BTR）。一旦陷入BTR，智能体的内部信念会严重偏离真实状态，后续动作变得不再提供信息，错误会累积，推理进程停滞。更重要的是，在RL训练中，轨迹尾部这些非信息性的动作会污染信用分配（credit assignment），误导策略优化，导致对早期关键动作的梯度估计出现偏差甚至反转，从而阻碍有效探索并产生次优策略。

因此，本文要解决的核心问题是：如何检测并缓解由信念偏离引发的“信念陷阱动态”，以稳定RL训练、改善信用分配，从而提升LLM智能体在主动推理任务中的性能和鲁棒性。为此，论文提出了T³方法，其核心思想是通过理论推导的准则来检测信念陷阱的进入点，并及时截断训练轨迹，以抑制非信息性尾部效应，保护信息性动作前缀的信用，从而系统性地改进策略优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于强化学习的LLM智能体优化方法、针对长视野/多轮任务的信用分配问题研究，以及主动推理与信念跟踪的相关工作。

在**基于强化学习的LLM智能体优化方法**方面，主流工作如PPO、GPRO、GSPO等通过设计奖励函数和策略梯度算法来优化模型行为。本文提出的T³方法并非替代这些算法，而是作为一个可无缝集成的“即插即用”模块，通过截断训练轨迹来改善这些现有优化框架中的信用分配问题。

在**信用分配问题**的研究中，已有工作多关注于如何更准确地为长序列中的动作分配奖励，例如使用资格迹或分层强化学习。本文的独特之处在于，它首次从“信念偏差”的理论视角剖析了该问题，指出LLM由于自身推理能力限制，其内部信念会逐渐偏离真实状态，导致后续动作失去信息量，从而污染了信用分配。T³通过检测并截断陷入“信念陷阱区域”的轨迹尾部，直接抑制了这种污染源。

在**主动推理与信念跟踪**领域，经典研究通常将问题建模为POMDP，并假设存在完美的信念估计（如贝叶斯滤波）。本文指出，当用LLM实例化智能体时，其信念跟踪是近似且不完美的，这正是信念偏差的根源。因此，本文的工作连接了经典POMDP理论与现代LLM智能体的实践，为解决LLM在复杂、多轮交互任务中性能下降的问题提供了一个新的理论视角和实用工具。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为 $\mathbf{T^3}$ 的简单而原则性的方法来解决信念偏差问题。该方法的核心思想是检测并截断因信念偏差而产生的无信息交互轨迹尾部，从而抑制其对强化学习策略优化的负面影响。

整体框架基于将主动推理建模为部分可观测马尔可夫决策过程（POMDP）。在此框架下，智能体维护一个对潜在真实状态的信念分布。论文的关键创新在于理论分析了信念偏差的动力学，并定义了“信念陷阱区域”（BTR）。一旦智能体的信念进入BTR，其期望任务进展将停滞不前，导致后续动作变得无信息或重复。更重要的是，在基于结果的强化学习中，这种无信息的轨迹尾部会污染对早期探索性动作的信用分配，甚至导致其优势函数估计为负，从而误导策略梯度方向。

$\mathbf{T^3}$ 方法的核心模块是一个操作性的截断准则。由于直接观测理论定义的BTR入口（涉及不可观测的信念状态和阈值）不切实际，该方法设计了一个基于可观测代理指标的检测条件。该条件通过监控一个假设空间 $\mathcal{H}_t$ 在连续时间步之间的精化程度 $d(\mathcal{H}_\tau, \mathcal{H}_{\tau+1})$ 来工作。如果在长度为 $k$ 的滑动窗口内，所有步骤的精化度量都低于一个最小进展阈值 $\Delta_{\min}$，则判定为进展持续停滞，并在此刻截断训练轨迹。

在具体实现中，假设空间 $\mathcal{H}_t$ 和精化度量 $d(\cdot, \cdot)$ 可根据任务结构进行实例化。例如，在候选解空间有限的定向推理任务中，$\mathcal{H}_t$ 可定义为在时刻 $t$ 仍 plausible 的候选解集合，$d$ 可定义为集合大小的对数差，这恰好与理论分析中的势函数 $\Psi$ 动态对应。论文还指出，这一原则可以指导设计更通用的、不依赖特定任务结构的截断检测器。

该方法的主要优势在于，它作为一个元包装器，通过截断无信息尾部，保留了轨迹信息丰富的前缀部分应得的信用，从而系统性地改善了策略优化。实验表明，$\mathbf{T^3}$ 能显著提升训练稳定性，在多个任务上取得高达30个百分点的性能提升，同时降低高达34%的令牌消耗。

### Q4: 论文做了哪些实验？

论文在五个交互式推理任务上进行了实验：猜数字、情境谜题、电路解码、偏好估计和电影推荐。实验设置方面，主要使用Qwen2.5-7B-Instruct模型进行强化学习训练，在情境谜题任务中使用Qwen2.5-14B-Instruct模拟“用户”提供反馈。对比方法包括：1）未经训练的直接推理基线（如o3-mini、Gemini-2.5-Pro）；2）三种强化学习算法（PPO、GRPO、GSPO）及其与所提方法T³结合的版本。

主要结果如下：T³在所有任务和算法上均带来一致性能提升。关键数据指标包括：在电路解码任务中，PPO+T³将精确匹配率提升16.2个百分点至77.83%；在猜数字任务中，GRPO+T³提升30.1个百分点至91.36%，GSPO+T³达到99.74%；在电影推荐任务中，GSPO+T³提升41.0个百分点至55.67%。此外，T³将训练令牌成本降低高达34%，并显著提升了训练稳定性。实验表明，T³在18个报告指标中的14个上带来非边际增益，且在假设空间无限或连续的任务上，其增强的模型性能甚至超越了前沿推理大模型。

### Q5: 有什么可以进一步探索的点？

本文提出的T³方法通过截断信念偏离过大的轨迹来改进强化学习训练，但其核心局限在于“信念偏离”的检测高度依赖于任务特定的代理指标（如候选集大小变化、与真值的相似度），这限制了方法的通用性。未来研究可探索更通用、无需真值信息的偏离度量，例如利用LLM自身的不确定性估计或构建可学习的信念状态模型。此外，当前方法主要处理离散决策，可扩展至更复杂的连续状态空间或部分可观测环境。另一个方向是将截断机制与课程学习结合，动态调整任务难度以引导智能体更稳健地学习。最后，可研究如何将信念跟踪模块与策略网络更深度地整合，实现端到端的联合优化，而非仅作为训练时的外部过滤机制。

### Q6: 总结一下论文的主要内容

这篇论文针对大型语言模型（LLM）在主动推理任务中存在的“信念偏差”问题展开研究。主动推理要求智能体通过多轮交互从外部获取信息以解决问题，其核心是信念跟踪，即准确维护对问题底层状态和不确定性的理解。然而，由于LLM的推理能力有限，其内部信念容易偏离真实问题状态，导致状态认知丢失并产生无信息量或重复的动作。这种偏差会在强化学习（RL）的训练轨迹中累积错误，造成信用分配不当并限制有效探索。

为解决该问题，作者提出了名为 $\mathbf{T^3}$ 的方法。其核心思路是跟踪信念偏差，检测过度的偏差，并通过截断训练轨迹来抑制轨迹尾部无信息量的影响。这种方法保留了信息丰富的前缀段落的信用，从而系统性地改进了策略优化。

实验表明，在五个挑战性任务上，$\mathbf{T^3}$ 能持续提升训练稳定性，带来高达30个百分点的性能提升，同时降低多达34%的令牌消耗。论文的主要贡献在于揭示了信念控制是构建鲁棒主动推理智能体的关键原则，并提出了一种简单而有效的实现方法。
