---
title: "Utility-Guided Agent Orchestration for Efficient LLM Tool Use"
authors:
  - "Boyan Liu"
  - "Gongming Zhao"
  - "Hongli Xu"
date: "2026-03-20"
arxiv_id: "2603.19896"
arxiv_url: "https://arxiv.org/abs/2603.19896"
pdf_url: "https://arxiv.org/pdf/2603.19896v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use"
  - "Agent Orchestration"
  - "Decision Policy"
  - "Quality-Cost Trade-off"
  - "ReAct"
  - "Utility-Guided"
  - "Multi-Step Reasoning"
  - "LLM Agent"
relevance_score: 8.5
---

# Utility-Guided Agent Orchestration for Efficient LLM Tool Use

## 原始摘要

Tool-using large language model (LLM) agents often face a fundamental tension between answer quality and execution cost. Fixed workflows are stable but inflexible, while free-form multi-step reasoning methods such as ReAct may improve task performance at the expense of excessive tool calls, longer trajectories, higher token consumption, and increased latency. In this paper, we study agent orchestration as an explicit decision problem rather than leaving it entirely to prompt-level behavior. We propose a utility-guided orchestration policy that selects among actions such as respond, retrieve, tool call, verify, and stop by balancing estimated gain, step cost, uncertainty, and redundancy. Our goal is not to claim universally best task performance, but to provide a controllable and analyzable policy framework for studying quality-cost trade-offs in tool-using LLM agents. Experiments across direct answering, threshold control, fixed workflows, ReAct, and several policy variants show that explicit orchestration signals substantially affect agent behavior. Additional analyses on cost definitions, workflow fairness, and redundancy control further demonstrate that lightweight utility design can provide a defensible and practical mechanism for agent control.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在使用外部工具时面临的一个核心系统级问题：**如何在答案质量与执行成本之间实现可控且可分析的权衡**。研究背景是，当前工具增强型LLM智能体在问答、决策支持等任务中展现出潜力，但现有方法普遍存在不足。这些方法主要分为两类：一类是**固定工作流**，其执行流程预先手动设定，虽然稳定可预测，但过于僵化，无法根据任务难度或中间证据动态调整；另一类是**自由形式的多步推理方法**（如ReAct），虽更灵活且通常能获得更高的任务质量，但容易导致不必要的中间步骤、重复的工具调用以及高昂的执行成本（如令牌消耗、延迟增加），且行为难以解释和控制。

因此，本文要解决的核心问题是：能否将智能体的行为编排（orchestration）作为一个**显式的决策问题**来研究，而非仅仅依赖于提示工程带来的隐式行为？论文提出，智能体在每一步应能主动选择执行何种动作（如直接回答、检索、调用工具、验证或停止），并为此设计了一个**效用引导的编排策略**。该策略通过评估预估收益、步骤成本、不确定性和冗余性等启发式信号，来平衡质量与成本。其目标并非宣称在任务性能上全面超越现有基线，而是提供一个可控、可分析的政策框架，使工具使用型LLM智能体的质量-成本权衡变得可量化、可调节，从而构建更高效、更可解释的智能体系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 工具使用与推理方法类**：ReAct 展示了交错进行推理和外部调用可提升任务性能；Toolformer 探索了模型如何学习结构化地调用工具；Gorilla 专注于 API 调用场景下的精确工具选择。这些工作奠定了工具使用智能体的可行性，但其核心关注点在于“能否成功使用工具”，而非对多步行为成本的显式控制。本文则明确将智能体编排（orchestration）作为一个策略层来研究，以权衡额外步骤的收益与成本。

**2. 推理与自我改进类**：Chain-of-Thought、Self-consistency、Tree of Thoughts 以及 Program-of-Thoughts 等方法通过引入中间推理步骤来提升复杂问题解决能力；Self-Refine、Reflexion、LATS 等工作则侧重于迭代优化和自我修正。这些方法虽能提升推理质量，但往往会增加中间步骤和上下文积累，并未直接回答“何时进行更多推理是合理的”这一系统级问题。本文的研究与之互补，不追求更强的推理范式，而是专注于在质量-成本权衡下进行显式的动作选择和停止决策。

**3. 多智能体与系统框架类**：AutoGen、MetaGPT、ChatDev 等工作研究了多智能体对话、角色化协作等框架，用于任务分解与协作；Voyager 探索了具身智能体通过迭代探索积累技能。这些研究反映了从单次提示向涉及记忆、交互、协调的智能体系统的转变。然而，它们多依赖固定工作流或提示驱动控制，编排逻辑常是隐式的。本文的不同之处在于，它使编排层变得显式且轻量，专注于为单智能体工具使用设计一个效用引导的决策机制，而非提出一个完整的多智能体框架。

**4. 效率优化与评测类**：在效率方面，已有工作探索了高效的 Transformer 架构、自适应计算机制和早期退出策略等。本文与之不同，不提出新的模型架构，而是在编排层面研究效率问题，即智能体显式评估下一步是否可能有益，并平衡预估收益与成本信号。在评测方面，WebShop、ALFWorld、ToolBench 等基准强调了在交互环境中评估多步决策、轨迹质量和动作效率的重要性。本文的评估视角与此一致，不仅衡量最终任务质量，还考察令牌消耗、执行时间、冗余度等，将智能体质量与获取该质量的计算和行为成本结合起来研究。

### Q3: 论文如何解决这个问题？

论文通过提出一个显式的、基于效用的编排策略框架来解决LLM智能体在工具使用中质量与成本之间的权衡问题。其核心方法是将智能体的多步决策过程形式化为一个序列决策问题，并设计了一个轻量化的效用函数来指导每一步的动作选择。

整体框架是一个迭代的执行循环。智能体在每一步t观察状态s_t，该状态包含四类信息：原始用户查询与当前工作上下文、交互历史（包括先前的动作和中间推理痕迹）、外部检索或工具调用的观察结果，以及执行状态信号（如步骤计数和预算相关元数据）。基于此状态，智能体从一个紧凑的动作空间A={respond, retrieve, tool_call, verify, stop}中选择下一步动作。选择的标准是最大化一个显式定义的效用函数U(a|s_t)。

该效用函数是方法的核心创新点，它被设计为几个可解释组件的线性组合：U(a|s_t) = Gain(a|s_t) - λ1*StepCost(a|s_t) - λ2*Uncertainty(a|s_t) - λ3*Redundancy(a|s_t)。每个组件都有其特定的控制目的：
1.  **估计增益（Gain）**：评估执行动作a可能带来的边际价值提升，用于判断是否值得进行另一次检索、工具调用或验证。
2.  **步骤成本（StepCost）**：作为一个轻量化的归一化代理信号，用于抑制不必要的轨迹扩展，其与实际令牌成本或延迟成本的关系通过实验变体进行实证研究。
3.  **不确定性（Uncertainty）**：反映智能体对当前证据充分性的自我估计不确定性，高不确定性鼓励进一步收集证据。
4.  **冗余度（Redundancy）**：惩罚重复或高度相似的动作（特别是检索和工具调用），以减少低价值重复并压缩执行轨迹。

主要模块包括状态表示模块、效用计算模块和动作选择模块。流程从用户查询开始，智能体构建状态表示，为候选动作计算效用分数，选择效用最高的动作执行，然后根据执行结果更新状态，如此循环，直到选择“停止”动作、耗尽预设步骤预算或触发后备终止条件。

该架构设计的关键技术与创新点在于：首先，它将编排策略从提示词中解耦出来，作为一个显式的、可检查的控制层，从而分离了任务解决能力和控制逻辑。其次，它提供了一个结构化、可分析的控制机制，使得研究者能够通过调整效用函数的各个组件及其权重（λ参数），来实证研究不同编排信号（如成本、不确定性、冗余控制）如何影响智能体的行为和质量-成本权衡。这种方法的价值不在于提供一个完全学习或普遍最优的策略，而在于提供了一个轻量化、可辩护的机制，使得多步工具使用更可控、更可分析，更适合成本敏感的场景。

### Q4: 论文做了哪些实验？

实验在HotpotQA开发集的200个固定样本上进行，使用相同的基础模型、本地BM25检索器和问题集，以在匹配条件下隔离编排策略对质量-成本权衡的影响。评估指标包括F1分数、令牌消耗量、实际运行时间以及效率得分（F1/令牌）。对比方法包括直接回答、固定工作流基线（minimal、search-twice、search-verify）、阈值控制器、ReAct以及提出的效用引导策略。主要结果如下：直接回答成本最低但F1仅0.0719；固定工作流中最佳F1为0.1698（search-twice），但成本较高；ReAct获得最高F1（0.2662），令牌消耗546.6；默认策略（step-cost）F1为0.2360，令牌消耗1294.2，虽低于ReAct，但提供了更可控的行为。进一步实验分析了成本定义（token-cost策略F1提升至0.2562）、工作流公平性（验证更强工作流仍不如自适应方法）和冗余控制（语义冗余将令牌消耗从1294.2降至1156.6）。消融实验显示，移除预期收益或停止控制会使令牌消耗激增至2700以上，而F1仅微增至0.2621，证实了各效用组件的必要性。总体表明，显式编排策略在质量-成本权衡上提供了可分析且可控的替代方案。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是其核心的效用组件（如估计收益和不确定性）仍基于启发式设计而非学习得到，缺乏概率校准；二是该策略框架并未在任务性能上普遍超越如ReAct等自由形式基线，其贡献更在于提供了一个可分析的控制结构；三是冗余控制机制主要提升了令牌使用的紧凑性，但对降低延迟的效果有限，说明语义层面的控制机制仍需改进。

未来研究方向可以从以下几个角度深入：首先，将启发式信号替换为通过学习获得的评分器或经过校准的不确定性估计，以提升决策的准确性和适应性。其次，将框架扩展到更复杂的环境和长期任务中，验证其泛化能力。此外，可以探索显式的记忆感知编排，将检索、记忆读取和写入等操作纳入统一的决策框架，以优化信息流。更广泛地，这项研究启示我们，高效的大型语言模型智能体不仅需要强大的推理模型，还需设计明确的决策策略来约束和组织多步行为，这为构建可控、可解释的智能体系统开辟了新的设计空间。

### Q6: 总结一下论文的主要内容

该论文聚焦于大语言模型（LLM）工具调用代理在任务执行中面临的质量与成本权衡问题。针对固定工作流僵化、而自由推理方法（如ReAct）可能带来高昂调用成本与延迟的不足，研究将代理编排明确定义为一个决策问题，而非完全依赖提示驱动。核心贡献是提出了一种效用引导的编排策略，通过平衡预估收益、步骤成本、不确定性和冗余度，在响应、检索、工具调用、验证和停止等动作间进行选择。该方法旨在提供一个可控制、可分析的政策框架，以系统研究质量-成本权衡，而非追求绝对最优性能。实验表明，明确的编排信号能显著影响代理行为，轻量级的效用设计为代理控制提供了合理且实用的机制。论文最终强调，该工作为构建更具可控性、可分析性且成本感知的LLM代理迈出了结构化的一步，对预算敏感和上下文受限的部署场景具有重要价值。
