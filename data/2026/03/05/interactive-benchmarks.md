---
title: "Interactive Benchmarks"
authors:
  - "Baoqing Yue"
  - "Zihan Zhu"
  - "Yifan Zhang"
  - "Jichen Feng"
  - "Hufei Yang"
  - "Mengdi Wang"
date: "2026-03-05"
arxiv_id: "2603.04737"
arxiv_url: "https://arxiv.org/abs/2603.04737"
pdf_url: "https://arxiv.org/pdf/2603.04737v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Evaluation"
  - "Benchmark"
  - "Interactive Reasoning"
  - "Decision Making"
  - "Long-Horizon Planning"
relevance_score: 7.5
---

# Interactive Benchmarks

## 原始摘要

Standard benchmarks have become increasingly unreliable due to saturation, subjectivity, and poor generalization. We argue that evaluating model's ability to acquire information actively is important to assess model's intelligence. We propose Interactive Benchmarks, a unified evaluation paradigm that assesses model's reasoning ability in an interactive process under budget constraints. We instantiate this framework across two settings: Interactive Proofs, where models interact with a judge to deduce objective truths or answers in logic and mathematics; and Interactive Games, where models reason strategically to maximize long-horizon utilities. Our results show that interactive benchmarks provide a robust and faithful assessment of model intelligence, revealing that there is still substantial room to improve in interactive scenarios. Project page: https://github.com/interactivebench/interactivebench

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型评估方法存在的局限性问题。研究背景是，随着大语言模型的快速发展，传统的评估范式已难以准确反映模型在真实场景中的智能水平。现有方法主要有三类不足：一是基于固定数据集（如GSM8K、MMLU）的基准测试容易达到性能饱和，且存在数据污染问题；二是基于人类偏好的竞技场评估（如ChatBot Arena）依赖主观判断，无法可靠衡量推理能力；三是智能体基准测试（如AgentBench、GAIA）虽然评估动态推理和工具使用，但通常依赖复杂的环境设置，泛化到实际部署时受限。

本文指出，这些现有协议普遍忽视了一个智能的核心组成部分：主动获取信息的能力。在大多数现有基准中，模型只是信息的被动接收者，而真实世界任务往往信息不完全，智能体需要主动判断何时信息不足、应获取何种关键证据，并高效地采取行动。因此，本文要解决的核心问题是：如何构建一个评估框架，以衡量模型在预算约束下，通过主动交互获取信息并进行推理的能力。为此，论文提出了“交互式基准测试”这一统一评估范式，并将其具体化为两个场景：交互式证明（如逻辑和数学问题中通过与持有真相的法官互动来推导答案）和交互式游戏（如扑克和信任游戏中通过与其他智能体策略互动以最大化长期收益），从而对模型的交互推理能力进行更鲁棒和真实的评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：静态基准、动态与智能体基准，以及需要交互的基准。

在**静态基准**方面，相关工作包括HotpotQA、GSM8K、HumanEval等广泛使用的数据集，它们通过固定输入和参考答案进行标准化评估。本文认为这些基准难以反映真实应用中的模型行为，且易受数据污染和过拟合影响，因此提出了更具动态性的评估范式。

在**动态与智能体基准**方面，相关工作如Chatbot Arena、MT-Bench通过人类偏好或LLM评判进行动态排名；SWE-bench、BrowseComp等则评估模型作为工具使用智能体的能力。本文指出这些基准虽更贴近部署，但通常依赖固定的工具接口和协议，未能充分评估模型主动规划工作流程、决定信息获取的能力。

在**需要交互的基准**方面，相关工作包括TurtleBench、Entity-deduction Arena、ARC-AGI等，它们要求模型通过多轮交互解决问题。本文认为这些基准未能明确分离交互本身与其他因素（如任务先验）的贡献，且缺乏统一的数学原理支持跨任务比较。

本文提出的“交互式基准”与上述工作的主要区别在于：它提供了一个理论形式化的统一评估框架，强调在预算约束下主动获取信息的能力，并通过“交互证明”和“交互游戏”两种实例，系统性地评估模型的推理与战略规划能力，从而更客观、可泛化地衡量模型智能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“交互式基准测试”的统一评估范式来解决传统基准测试存在的饱和、主观性和泛化性差等问题。该范式的核心思想是在预算约束下，通过模型与环境的多轮交互过程来评估其主动获取信息和推理的能力。

整体框架将每个基准实例建模为模型π与环境ε之间一个长度为T的交互过程。在每一轮t，模型观察交互历史h_t并选择动作a_t，环境则返回下一个观察o_{t+1}。交互在模型提交最终答案或预算耗尽时终止。该框架具体实例化为两种主要设置，构成了两个核心评估模块：

1.  **交互式证明**：用于评估在逻辑和数学等领域中推导客观事实的能力。环境提供一个全知验证者，模型通过提问（产生成本c(a_t)）来获取受限反馈（如是/否），最终在总预算B内提交答案。评估目标是最大化在预算约束下给出正确答案的概率。其关键技术在于设计了严格的交互协议以防止信息泄露，例如在“情境谜题”中，对中间查询的回复严格限制为{是，否，两者，不相关}，迫使模型通过积累逻辑约束来推进推理。在数学问题评估中，模型可以查询中间断言的有效性，从而早期修剪错误分支，提高了搜索效率并提供了可解释的推理过程追踪。

2.  **交互式游戏**：用于评估在战略互动中最大化长期效用的能力。模型与其他智能体互动，接收任务定义的奖励r_t，目标是最大化折扣累积回报。这测试了模型在不确定性下的推理、风险管理和对手心理建模等能力。论文实例化了两个游戏组件：
    *   **德州扑克**：采用标准无限制德州扑克引擎，测试模型在不完美信息下的战略决策。模型接收结构化观察，必须输出标准动作，并遵守超时和格式验证。
    *   **信任游戏（迭代囚徒困境）**：评估模型在重复战略互动中的适应能力。游戏采用随机视野（以概率δ继续），迫使模型优化折扣累积收益。评估采用循环赛制，计算平均每轮收益、合作率和背叛率等行为统计量，以衡量模型的动态博弈能力。

该方法的创新点在于：首先，它从被动评估转向主动评估，强调模型在预算约束下通过交互主动获取信息的能力；其次，它提供了过程可解释性，交互轨迹清晰展示了模型的假设检验和错误修正过程；最后，它通过严谨的协议设计（如受限反馈、随机视野）减少了记忆和捷径解决方案的可能性，实现了更鲁棒和客观的模型能力比较。

### Q4: 论文做了哪些实验？

论文在交互式基准框架下进行了三类实验：逻辑推理、数学解题和策略游戏。

**实验设置与数据集**：在逻辑推理（Interactive Proofs）中，使用包含46个谜题的Situation Puzzle数据集，交互轮次上限为20轮，法官模型固定为Grok-4.1-fast，玩家和法官温度均设为0以确保可复现性。在数学解题（Interactive Proofs）中，使用从HLE数据集中采样的52个挑战性数学实例，设置与逻辑推理相同。在策略游戏（Interactive Games）中，进行了德州扑克模拟（5000手牌，10张独立桌子）和信任博弈锦标赛。

**对比方法与指标**：主要对比了六款前沿大语言模型作为玩家（Grok-4.1-fast、Gemini-3-flash、GPT-5-mini、Kimi-k2-thinking、DeepSeek-v3.2、Qwen3-max）的表现。在数学实验中，引入了在近似匹配的推理令牌预算下的pass@k方法作为基线进行对比。在信任博弈中，加入了Grim Trigger和Tit-for-Tat两种规则基线。

**主要结果与关键指标**：
1.  **逻辑推理**：Gemini-3-flash准确率最高（30.4%），GPT-5-mini次之（17.4%），Qwen3-max最低（4.3%）。在已解决的谜题中，Kimi-k2-thinking平均所需轮次最少（12.3轮），DeepSeek-v3.2最多（18.0轮）。
2.  **数学解题**：在交互评估下，Grok-4.1-fast准确率最高（76.9%），GPT-5-mini为73.1%，Kimi-k2-thinking仅为34.6%。与预算匹配的pass@k基线相比，交互评估的准确率普遍高出20%-50%，表明固定预算下重复采样会低估模型能力。效率方面，Qwen3-max平均轮次最少（5.2轮），但准确率一般（46.2%）；DeepSeek-v3.2平均轮次最多（12.0轮）。
3.  **策略游戏**：
    *   **德州扑克**：Gemini-3-flash平均每手盈利最高（31.8 ± 42.4）且最稳定；Grok-4.1-fast（27.9 ± 53.5）和GPT-5-mini（22.2 ± 71.3）也盈利但方差大。GPT-5-mini风格最激进（自愿入池率VPIP 23.7%，弃牌率71.4%），DeepSeek-v3.2最保守（VPIP 9.0%，弃牌率90.5%）。
    *   **信任博弈**：Qwen3-max平均每轮收益最高（1.867），GPT-5-mini次之（1.836），两者均超过规则基线；DeepSeek-v3.2最低（1.648）。Qwen3-max和GPT-5-mini合作率极高（97%）且背叛率极低（2%和0%），而Gemini-3-flash和DeepSeek-v3.2合作率较低（82%和73%），背叛率较高（7%）。

### Q5: 有什么可以进一步探索的点？

该论文提出的交互式评测框架虽具创新性，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，当前框架仅覆盖了逻辑证明和博弈两类任务，其泛化能力有待验证。未来可扩展至更复杂的现实场景，如开放域对话、多模态交互或需长期规划的决策任务，以全面评估模型在动态环境中的适应能力。其次，实验中的“预算约束”设计较为简单，未来可引入更精细的资源管理机制（如时间、计算力或信息成本），模拟真实世界中的受限交互。此外，论文未深入探讨如何通过训练优化模型的交互能力，这为方法学改进留下空间：例如，可研究基于强化学习的交互策略学习，或设计自监督任务让模型在模拟交互中主动学习信息获取。最后，评测过程仍依赖预设的法官或环境，未来可探索 peer-to-peer 的模型互评机制，以更开放的方式衡量智能体的协作与竞争能力。这些方向将推动交互式评测向更通用、更实用的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对当前标准基准测试在饱和、主观性和泛化性差等方面的不足，提出了一种新的评估范式——交互式基准测试。核心问题是评估模型在预算约束下主动获取信息并进行推理的能力，这被认为是智能的关键组成部分。论文将这一框架具体化为两个主要设置：交互式证明，模型通过与持有客观答案的评判者互动来推导逻辑或数学真理；以及交互式游戏，模型通过战略推理来最大化长期效用。方法上，它借鉴了计算复杂性理论中的交互式证明概念，要求模型在互动中主动收集证据以完成任务。实验结果表明，交互式基准测试能更稳健、真实地评估模型智能，并揭示出模型在交互场景中仍有巨大改进空间。这一工作的意义在于推动评估方法更贴近现实世界中信息不完全、需主动探索的复杂任务。
