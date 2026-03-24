---
title: "Profit is the Red Team: Stress-Testing Agents in Strategic Economic Interactions"
authors:
  - "Shouqiao Wang"
  - "Marcello Politi"
  - "Samuele Marro"
  - "Davide Crapis"
date: "2026-03-21"
arxiv_id: "2603.20925"
arxiv_url: "https://arxiv.org/abs/2603.20925"
pdf_url: "https://arxiv.org/pdf/2603.20925v1"
categories:
  - "cs.AI"
tags:
  - "Agent Security"
  - "Red Teaming"
  - "Adversarial Testing"
  - "Strategic Interaction"
  - "Multi-Agent Systems"
  - "Robustness"
  - "Economic Games"
relevance_score: 7.5
---

# Profit is the Red Team: Stress-Testing Agents in Strategic Economic Interactions

## 原始摘要

As agentic systems move into real-world deployments, their decisions increasingly depend on external inputs such as retrieved content, tool outputs, and information provided by other actors. When these inputs can be strategically shaped by adversaries, the relevant security risk extends beyond a fixed library of prompt attacks to adaptive strategies that steer agents toward unfavorable outcomes. We propose profit-driven red teaming, a stress-testing protocol that replaces handcrafted attacks with a learned opponent trained to maximize its profit using only scalar outcome feedback. The protocol requires no LLM-as-judge scoring, attack labels, or attack taxonomy, and is designed for structured settings with auditable outcomes. We instantiate it in a lean arena of four canonical economic interactions, which provide a controlled testbed for adaptive exploitability. In controlled experiments, agents that appear strong against static baselines become consistently exploitable under profit-optimized pressure, and the learned opponent discovers probing, anchoring, and deceptive commitments without explicit instruction. We then distill exploit episodes into concise prompt rules for the agent, which make most previously observed failures ineffective and substantially improve target performance. These results suggest that profit-driven red-team data can provide a practical route to improving robustness in structured agent settings with auditable outcomes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体（Agent）在现实世界部署中面临的一个核心安全风险：当外部输入（如检索内容、工具输出或其他参与方提供的信息）可被对手战略性地操控时，智能体是否容易受到自适应、逐利性攻击的利用。研究背景是，随着智能体系统从单轮提示转向多步交互的复杂部署，其决策越来越依赖于外部输入，而传统安全评估主要关注静态的、预设的攻击模式（如提示注入或越狱），这些方法难以反映真实场景中对手自适应调整策略以谋取利益的风险。

现有方法的不足在于，它们通常依赖于手工构建的攻击库或基于LLM的评判机制来检测违规，这既无法涵盖所有可能的自适应攻击策略，也难以模拟真实对手持续优化策略以最大化自身收益的行为。这种评估方式可能导致智能体在静态测试中表现良好，但在面对动态、自适应的战略压力时变得脆弱。

因此，本文要解决的核心问题是：如何设计一种更贴近实际部署风险的评估协议，以系统性地测试智能体在结构化、可审计结果的环境中对自适应利用的脆弱性。为此，论文提出了“利润驱动的红队测试”协议，该协议摒弃手工攻击和外部评判，转而训练一个仅通过标量结果反馈（即利润）来优化自身策略的对手模型，从而自动发现并利用智能体的弱点。通过在经济博弈等结构化环境中实例化该协议，研究证明了自适应对手能有效利用智能体，并进一步将攻击过程提炼为提示规则，以增强智能体的鲁棒性。这一方法旨在填补当前安全评估与真实世界战略互动风险之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用/评测类以及防御类。

在**方法类**上，本文与自动化红队方法密切相关，如 Tree of Attacks with Pruning (TAP) 和 AutoDAN，它们都采用迭代式黑盒搜索来生成有效的对抗策略。本文的区别在于其优化目标和监督信号：它不依赖于外部指定的失败度量（如策略违规标签、检测器分数或奖励模型判断），而是优化对手在明确交互环境中的**利润**，仅使用标量结果反馈，无需LLM作为裁判或攻击分类法。

在**应用/评测类**上，相关研究包括：1）在具有延迟反馈的现实多步骤环境中评估智能体的基准工作（如 WebArena、AgentBench），它们评估固定任务分布上的固定智能体，但未操作化一个主动搜索策略以提升自身利润的自适应对手。本文则引入了以利润最大化为目标的优化对手。2）研究具有可审计结果的混合动机经济交互的工作（如 scorable negotiation、Diplomacy 中的战略博弈），它们提供了任务和度量框架。本文的协议不同，它不是从固定池中采样对手或分配预定义的对抗角色，而是通过仅使用标量结果反馈直接针对目标优化对手，从而自动生成自适应压力。

在**防御类**上，近期研究探索如何将发现的攻击重新用于防御，例如上下文防御和对抗性游戏迭代优化。本文与之相关的是，它同样利用对抗性轨迹（攻击片段）来提炼简洁的提示规则以增强鲁棒性。但本文并未提出独立的防御范式，而是展示了其红队协议产生的数据可直接用于这种实用化硬化。

### Q3: 论文如何解决这个问题？

论文通过提出并实施“利润驱动的红队测试”协议来解决智能体在战略经济互动中的对抗性压力测试问题。其核心方法是用一个经过训练的对手（攻击者）取代手工设计的攻击，该对手仅利用标量结果反馈（即自身利润）来学习最大化利润的策略，从而暴露目标智能体的可被利用性。

整体框架基于一个结构化的、具有可审计结果的环境。该环境定义了四种经典的经济互动场景（最后通牒博弈、第一价格拍卖、双边贸易、供应点博弈），为压力测试提供了可控的测试平台。每个互动场景都明确定义了参与者的观察空间、行动空间以及将终端状态映射为可审计标量结果（即盈余）的规则。每一轮交互（episode）都会产生完整的交互记录和一个标量结果信号，而优化的对手只能观察到最终的状态反馈，确保了发现的策略纯粹是结果驱动的，而非依赖于攻击标签或外部监督。

主要模块/组件包括：
1.  **结构化环境**：定义了交互的公共参数、私有信息采样、交替回合制交互流程（包括自由形式消息和结构化行动），以及基于具体游戏规则计算双方盈余的终局结算机制。
2.  **利润优化的对手（攻击者）**：这是一个关键组件，其策略 φ 通过优化目标进行学习：在固定目标智能体策略 π 的情况下，最大化攻击者在与环境交互中的期望利润。这构成了一个纯粹的基于结果反馈的优化问题。
3.  **基于TAP的黑盒提示搜索算法**：这是实现对手优化的关键技术。论文对TAP（Tree-of-Thoughts Action Proposal）方法进行了适配，将其用于基于利润的选择。算法迭代地进行：从当前的攻击者提示池中，通过变异生成候选提示；然后在环境中让每个候选提示与目标智能体进行多次交互，并计算其平均攻击者利润作为评分；最后保留评分最高的候选进入下一轮迭代。整个过程完全依赖环境返回的利润信号，而不需要LLM作为评判员或任何攻击分类法。

创新点主要体现在：
1.  **问题定义与协议创新**：提出了“利润驱动的红队测试”这一新协议，将安全风险测试从静态的提示攻击库扩展到对手自适应策略的探索，更贴合现实世界中对手具有战略动机的场景。
2.  **无监督的对手训练**：攻击者的训练仅依赖于可审计的标量结果（利润），无需人工标注的攻击示例、攻击分类法或LLM作为评判员，简化了流程并提高了可扩展性。
3.  **策略发现与知识蒸馏**：该协议不仅能暴露智能体的脆弱性，还能自动发现有效的攻击策略（如试探、锚定、欺骗性承诺）。随后，论文将这些攻击案例提炼成简洁的提示规则，用于增强目标智能体，从而显著提升其鲁棒性和目标性能，形成了一种从压力测试到改进的实用闭环。

### Q4: 论文做了哪些实验？

论文在四个经典经济交互环境中进行了实验，包括最后通牒博弈、一级价格拍卖、双边交易和供应点博弈。实验设置上，固定目标智能体，对比基线攻击者与经过利润驱动红队优化（使用TAP风格搜索）的攻击者。每个条件进行20次独立交互，评估攻击者剩余（surplus）的变化。数据集基于自定义的交互环境，对比方法为优化前后的同一攻击者设置。

主要结果显示，利润驱动红队显著提高了攻击者的收益。例如在最后通牒博弈中，攻击者剩余平均提升范围从18.85到44.50（总资源R=100），所有提升均具有统计显著性（p值低至9.5e-30）。关键指标包括攻击者剩余提升值Δs_A及其95%置信区间。此外，研究分析了学习到的攻击模式，发现攻击者使用了谈判策略如制造紧迫感、协议框架和虚假约束，而非传统越狱攻击。

论文还进行了防御实验，从红队轨迹中提炼出简短的提示规则来硬化目标智能体。结果显示，硬化后目标剩余大幅提升，例如GPT-OSS-120B的目标剩余从-25.00增至7.00（提升Δs_D=32.00）。在所有游戏中，硬化都使目标剩余转为正值或消除了极端失败情况。

### Q5: 有什么可以进一步探索的点？

本文提出的利润驱动红队测试方法在结构化经济互动中验证了其有效性，但仍有多个方向值得深入探索。首先，当前实验环境局限于四种经典经济博弈，虽能清晰展示策略性压力与可审计结果，但现实场景更为复杂，未来可将框架扩展至更贴近实际的应用，如网页代理的金融欺诈、编码代理的资源消耗诱导等，这些场景中攻击者同样以经济利益为目标，但互动协议和结果评估可能更模糊，需设计更灵活的价值衡量机制。

其次，防御机制目前主要依赖从攻击轨迹中提炼提示规则，虽轻量但可能缺乏泛化能力。未来可通过监督微调或强化学习直接训练代理模型，使其不仅能识别恶意请求，还能在策略互动中主动做出利益最大化决策。此外，可引入交替对抗训练框架，让代理与攻击者在多轮迭代中共同优化，从而持续测试并提升鲁棒性，初步实验虽显示多数场景有效，但少数案例仍需更多轮次训练，这揭示了动态对抗中稳定性挑战。

最后，当前方法依赖结果信号优化攻击者，未考虑攻击策略的可解释性与多样性限制。未来可探索如何平衡利润最大化与攻击策略的探索范围，避免过拟合特定代理弱点，同时引入人类专家知识或理论博弈分析，以增强红队测试的覆盖面和系统性。这些改进有望将利润驱动框架发展为更通用、可扩展的智能体安全评估工具。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“利润驱动红队测试”的新方法，用于压力测试智能体在战略经济互动中的鲁棒性。核心问题是，当智能体依赖外部输入（如检索内容、工具输出或其他参与者提供的信息）时，这些输入可能被对手战略性地操纵，导致智能体做出不利决策，这超出了传统固定提示攻击库的范畴。

方法上，该协议摒弃了手工设计的攻击，转而训练一个学习型对手，该对手仅利用标量结果反馈（如利润）来最大化自身收益，无需依赖LLM评分、攻击标签或分类体系。研究在一个包含四种典型经济互动的精简实验场中实例化了该方法，以提供受控的测试环境。

主要结论表明，在面对静态基线时表现强劲的智能体，在利润优化压力下会持续被利用；学习型对手能自主发现探测、锚定和欺骗性承诺等策略。此外，研究成功将从攻击事件中提炼出的简明提示规则应用于智能体，使其能有效抵御先前观察到的多数失败，显著提升了目标性能。这证明了利润驱动的红队数据可为具有可审计结果的结构化智能体场景提供一条提升鲁棒性的实用路径。
