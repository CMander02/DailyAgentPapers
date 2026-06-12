---
title: "SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents"
authors:
  - "Ziyi Wang"
  - "Yuxuan Lu"
  - "Yimeng Zhang"
  - "Qun Liu"
  - "Chen Luo"
  - "Jiri Gesi"
  - "Hanqing Lu"
  - "Yisi Sang"
  - "Manling Li"
  - "Jing Huang"
  - "Dakuo Wang"
date: "2026-06-11"
arxiv_id: "2606.12908"
arxiv_url: "https://arxiv.org/abs/2606.12908"
pdf_url: "https://arxiv.org/pdf/2606.12908v1"
categories:
  - "cs.CL"
tags:
  - "Tool-using Agent"
  - "Reinforcement Learning"
  - "Failure-Driven Training"
  - "Multi-Turn Tool Use"
  - "Agent Training"
  - "Tau2-Bench"
relevance_score: 9.5
---

# SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents

## 原始摘要

Language model agents are increasingly effective in solving realistic tasks through multi-turn tool use. However, training reliable tool-using agents remains challenging in practice. While reinforcement learning provides an on-policy paradigm for improving agents from their own environment interactions, its effectiveness depends heavily on the training task distribution. When tasks are fixed before training, the task distribution can become increasingly mismatched with the policy's evolving capabilities, causing many rollouts to be spent on uninformative tasks. We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks. SENTINEL follows a Controller--Proposer--Solver loop: the Controller analyzes failed trajectories and summarizes recurring error patterns, the Proposer generates executable tasks that stress these weaknesses, and the Solver is trained on the targeted tasks. On Tau2-Bench Retail with Qwen3-4B-Thinking-2507, SENTINEL improves Pass\^{}1 from 66.4 to 74.9 and outperforms RL on general synthetic tasks across Pass\^{}k metrics. These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在训练能够使用工具的智能语言模型代理时，现有强化学习方法因任务分布静态而导致的训练效率低下和策略改进受限的问题。研究背景是，虽然强化学习为代理提供了从自身环境交互中进行策略内学习的范式，但其效果高度依赖于预定义的训练任务分布。现有方法的不足在于，在训练前固定任务集，导致随着代理策略能力的演变，任务分布与策略实际弱点之间的不匹配会日益加剧，使得大量训练轨迹浪费在“无信息价值”的任务上，代理无法针对自身实际存在的错误进行有效学习，甚至可能被迫学习利用奖励函数漏洞的肤浅策略。本文的核心问题是，如何构建一个能够根据学习过程中当前策略的实时弱点自适应生成训练任务的强化学习框架。为此，论文提出了SENTINEL，一个失败驱动的强化学习流程，它通过分析代理在执行任务中的失败轨迹来诊断其具体的错误模式，然后生成专门针对这些弱点的可执行训练任务，最后在这些目标性强的任务上对代理策略进行强化学习优化，从而形成了一个闭环的、可控制的策略改进循环。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可归纳为以下几类：

1. **工具使用与智能体框架**：包括ReAct（结合推理与工具调用）、Tool-learning方法，以及APIBank、ToolBench、BFCL等工具使用基准。本文基于这些框架，但提出通过失败驱动生成针对性训练数据，而非依赖通用任务分布。

2. **工具使用基准与合成数据生成**：如Tau2-Bench系列（客服场景模拟）、MCP基准（MCP-Bench等）、ToolAlpaca、APIGen-MT。合成数据方法如Trajectory2Task和Firefly通过可验证轨迹生成任务。区别在于，本文不是生成广泛任务，而是从当前策略失败中挖掘弱点，生成针对性训练任务。

3. **智能体强化学习**：包括ToolRL、ToRL、ReTool等工具使用RL方法，Shop-R1等电商环境方法，以及自对弈（self-play）训练。现有工作多关注策略优化和奖励设计（如层次奖励、过程奖励）。本文创新点在于显式利用失败轨迹诊断错误模式，生成可执行的目标任务，使训练分布随策略演化自适应调整，克服固定任务分布下样本效率低下的问题。

### Q3: 论文如何解决这个问题？

SENTINEL提出了一种故障驱动的强化学习框架，核心是一个Controller-Proposer-Solver迭代循环。整体框架中，Controller作为中枢组件，负责监控Solver的轨迹执行，分析失败轨迹并总结出可复现的错误模式，同时维护跨轮次的训练历史以区分持续性和已解决的故障。这些历史信息包括先前检测的模式、生成的任务摘要以及通过和失败的统计。基于当前错误模式、近期成功样本和训练历史，Controller生成自然语言指令指导Proposer。

Proposer采用轨迹接地任务构造方法：先在工具环境中采样相关状态并生成可执行工具调用轨迹作为参考答案，然后基于Controller指令将轨迹重写为自然语言用户请求，用户请求明确突出要锻炼的失败模式。例如，对物品定位失败，请求会包含相似产品变体或重叠名称。这种解耦设计避免了用户请求与期望工具动作不匹配的问题。

Solver使用GRPO算法在包含原始任务和Proposer生成任务的任务缓冲上进行强化学习训练。奖励设计包括任务成功奖励（验证最终环境状态和用户通信）和形状奖励，如动作级检查、重复工具调用惩罚、令牌长度惩罚和格式惩罚。迭代更新中，Solver的新失败又被反馈给Controller，形成循环，使训练分布持续向当前策略的弱点偏移。

### Q4: 论文做了哪些实验？

实验在 Tau2-Bench Retail 基准上进行，这是一个面向客服工具使用的可执行多轮决策任务基准，包含订单取消、换货、退货等任务。采用 Pass^k 指标，即 k 次重复试验均成功的概率。基础模型为 Qwen3-4B-Thinking-2507，对比了以下三种设置：Base（直接评估）、General RL（使用预生成的通用任务进行强化学习训练）以及 SENTINEL（使用本文提出的失败驱动任务生成流程进行强化学习）。强化学习训练使用 GRPO 算法，并采用了动态过滤、KL 正则化等技术，失败驱动任务生成每 12 个 rollout 批次触发一次。

主要结果显示，SENTINEL 在所有 Pass^k 指标上均取得最优性能：Pass^1 从 Base 的 66.4 提升至 74.9，Pass^2 从 51.6 提升至 60.5，Pass^3 从 43.2 提升至 51.2，全面优于 General RL（Pass^1 为 69.0）。进一步实验表明，在更强的 SFT 初始模型（Pass^1 为 74.3）上，直接应用 General RL 性能反而下降至 68.1，而 SENTINEL 则能进一步提升至 78.1。通过分析训练中发现的失败模式，控制器识别出的错误主要集中在精确工具使用行为上，如正确的物品/参数定位、多记录推理、必需中间动作和策略遵循等，而非简单的工具选择错误，表明 SENTINEL 能自适应地针对模型当前弱点生成训练任务。

### Q5: 有什么可以进一步探索的点？

SENTINEL将失败驱动训练成功应用于Tau2-Bench环境，但局限在于单一领域验证。未来应探索更复杂工具使用场景（如多API协作、动态环境），验证框架泛化性。其次，任务生成完全依赖模型当前暴露的弱点，可能导致“视野狭窄”——模型回避的困难模式不会被Controller捕获，形成性能天花板。可引入混合策略：以失败驱动为主，辅以少量人工设计的“压力测试”任务覆盖长尾场景。此外，Controller的失败模式总结依赖预定义模板，难以捕捉非结构化逻辑错误。可尝试使用大模型进行开放式错误根因分析，生成更具认知挑战的任务，或在策略梯度中引入对旧失败案例的记忆重放，防止灾难性遗忘。最后，SENTINEL的循环成本较高，如何用在线蒸馏或课程学习加速收敛是实用化关键。

### Q6: 总结一下论文的主要内容

SENTINEL提出了一种失败驱动的强化学习框架，用于提升工具使用语言模型智能体的训练效果。核心问题在于固定训练任务分布与策略能力演变不匹配，导致大量无效交互。该方法采用控制器-提议者-求解者循环：控制器分析失败轨迹并归纳错误模式，提议者生成针对这些弱点的可执行任务，求解者则在目标任务上通过RL训练。在Tau2-Bench零售任务上，Qwen3-4B- Thinking-2507模型的Pass@1从66.4提升至74.9，且优于通用合成任务的RL。主要结论是模型失败提供了有效且可扩展的目标训练信号，自适应数据生成能显著提升工具使用智能体的可靠性。这一框架为RL训练数据生成提供了新范式。
