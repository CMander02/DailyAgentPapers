---
title: "Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning"
authors:
  - "Wei Yang"
  - "Defu Cao"
  - "Jiacheng Pang"
  - "Muyan Weng"
  - "Yan Liu"
date: "2026-03-09"
arxiv_id: "2603.07972"
arxiv_url: "https://arxiv.org/abs/2603.07972"
pdf_url: "https://arxiv.org/pdf/2603.07972v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Human-Agent Collaboration"
  - "Continual Learning"
  - "Policy Optimization"
  - "Deferral Decision"
  - "Metacognition"
relevance_score: 8.5
---

# Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning

## 原始摘要

While scaling individual Large Language Models (LLMs) has delivered remarkable progress, the next frontier lies in scaling collaboration through multi-agent systems (MAS). However, purely autonomous MAS remain ''closed-world'' systems, constrained by the static knowledge horizon of pre-trained models. This limitation makes them brittle on tasks requiring knowledge beyond training data, often leading to collective failure under novel challenges. To address this, we propose the Human-In-the-Loop Multi-Agent Collaboration (HILA) framework, a principled paradigm for human--agent collaboration. HILA trains agents to learn a metacognitive policy that governs when to solve problems autonomously and when to defer to a human expert. To operationalize this policy, we introduce Dual-Loop Policy Optimization, which disentangles immediate decision-making from long-term capability growth. The inner loop applies Group Relative Policy Optimization (GRPO) with a cost-aware reward to optimize deferral decisions, while the outer loop implements continual learning, transforming expert feedback into high-quality supervised signals that strengthen the agent's reasoning ability. Experiments on challenging mathematical and problem-solving benchmarks show that HILA, equipped with Dual-Loop Policy Optimization, consistently outperforms advanced MAS, establishing a principled foundation for collaborative and continually improving agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前纯自主多智能体大语言模型系统在面临超出其预训练知识边界的新颖或复杂任务时，由于无法获取新知识而表现脆弱、容易集体失败的根本问题。研究背景是，尽管通过协调多个智能体（多智能体系统，MAS）在超越单一模型能力的问题上取得了进展，但这些系统本质上是“封闭世界”的，其知识范围受限于训练数据，无法生成新知识或适应未见过的情境。

现有方法主要分为两类，但均存在不足。第一类专注于优化智能体间的自主协作协议（如结构化辩论、工作流优化），虽能有效整合内部已有知识，但无法突破固有的知识边界，不具备真正的持续学习能力。第二类尝试引入人类专家，但往往将人类视为被动的“预言机”或任务监督者，未能系统性地解决两个核心问题：一是“何时”寻求帮助，现有方法多依赖低置信度阈值等启发式规则，而非学习得到的策略；二是“如何”从人类反馈中学习，现有处理通常是一次性的纠正，而非用于促进智能体长期能力增长。

因此，本文要解决的核心问题是：如何构建一个原则性的、自适应的人-智能体协作框架，使多智能体系统能够智能地、战略性地利用人类专业知识。具体而言，即让智能体学会一种元认知策略，以动态决策何时应自主解决问题，何时应策略性地求助于人类专家，并确保从专家干预中获得的学习能够持续提升智能体自身未来的推理与协作能力，从而实现系统的开放性与持续进化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体系统、人机协同交互，以及持续学习与策略优化方法。

在多智能体系统方面，早期研究主要基于提示词范式，通过预定义角色或工作流（如辩论、评审或流水线）组织多个LLM进行协作。这类方法缺乏适应性，交互协议固定且无法从经验中演化。近期工作转向结构化协调与自适应通信，例如通过路由、剪枝或工作流搜索动态重组交互。本文提出的HILA框架属于自适应多智能体系统，但进一步引入了人类专家作为协作核心，突破了纯自治系统的“封闭世界”限制。

在人机协同交互方面，已有研究将人类定位为监督者、预言者或评估者，为智能体提供修正或领域知识以增强其性能。另一类相近工作探索了LLM介导的指导，例如在MARL中使用LLM作为自然语言控制器来干预智能体学习轨迹。然而，这些系统通常依赖启发式规则（如置信度阈值）触发求助，且反馈多被视为一次性修正，而非用于持续能力增长。HILA则通过元认知策略来学习何时自主解决、何时求助人类，并利用反馈进行持续学习，实现了更原则化的人机协作范式。

在方法层面，现有工作缺乏将即时决策与长期能力增长解耦的机制。本文提出的双循环策略优化方法，内循环使用成本感知奖励的组相对策略优化来优化求助决策，外循环则通过持续学习将专家反馈转化为高质量监督信号，从而系统性地增强了智能体的推理能力，与以往基于启发式或一次性反馈的方法有显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HILA（Human-In-the-Loop Multi-Agent Collaboration）的框架来解决多智能体大语言模型在面临超出其预训练知识范围的任务时容易集体失败的问题。其核心是让智能体学会一种元认知策略，以自主决定何时自行解决问题，何时向人类专家求助。为实现这一目标，论文设计了整体框架、关键组件及创新的双循环策略优化算法。

**整体框架与主要模块**：HILA框架将人-智能体协作形式化为一个元认知马尔可夫决策过程（Meta-MDP）。该框架包含三个核心组成部分：1) **结构化的认知状态空间**：它编码了任务上下文（原始问题与交互历史）、智能体自身上下文（自身最新解决方案与推理状态）以及同伴上下文（其他智能体的响应），并可选地增强了一组轻量级的结构化认知线索（如社会共识、元认知监控和认知控制线索），为策略提供决策导向的抽象。2) **功能化的动作空间**：定义了三个高层认知策略动作：评估（`a^{eval}`，利用集体已有知识）、创建（`a^{create}`，生成全新解决方案）和求助（`a^{defer}`，向人类专家求助）。3) **多轮交互协议**：在每一轮中，所有智能体并行地根据共享状态独立选择并执行动作，输出结果（无论是自主生成还是采纳专家解答）共同构成下一轮的状态，从而将人类专业知识系统地整合到集体推理中。

**核心方法与创新点**：论文的关键创新在于**双循环策略优化**算法，它将即时决策优化与长期能力增长解耦。
*   **内循环（策略优化循环）**：采用**分组相对策略优化**来优化元认知策略。其核心是设计了一个成本感知的奖励函数，在任务正确性奖励的基础上，为“创建”和“求助”动作引入了递增的轻量级惩罚成本（`C_defer > C_create`），从而鼓励策略在结果相近时优先选择成本更低的动作。GRPO通过计算动作间的相对优势来更新策略，并结合KL惩罚和熵奖励正则化以确保训练稳定性。
*   **外循环（持续学习循环）**：当智能体选择“求助”动作时，会触发此循环。它接收人类专家提供的高质量演示，并将其转化为监督微调样本，通过最小化交叉熵损失来持续增强智能体的基础推理能力。这突破了仅靠强化学习无法提升基座模型知识天花板的问题。

最终，总训练目标是将内循环的GRPO目标与外循环的条件性SFT损失进行加权组合，联合优化单个智能体，使其兼具战略决策能力和持续改进能力。这种设计建立了一种“学徒-导师”动态：智能体策略性地寻求人类指导，并系统性地将其内化为持久的能力增长。

### Q4: 论文做了哪些实验？

论文在多个具有挑战性的数学和问题解决基准测试上进行了实验，以评估所提出的HILA框架和双循环策略优化（DLPO）方法的有效性。

**实验设置与数据集**：实验在广泛的基准测试套件上进行，包括通用语言理解（MMLU）、程序合成（HumanEval）和定量数学（GSM8K、AIME、AMC）。研究使用GPT-4o-mini作为模拟人类专家的代理，利用其强大的推理能力来模拟人类干预。模型主干主要基于LLaMA3-8B，并进行了跨主干（Qwen和LLaMA系列，涵盖多种规模）的泛化性评估。

**对比方法**：对比了多种基线方法，包括单智能体方法（如Vanilla、CoT、SC）和多智能体方法。多智能体基线涵盖了辩论风格（如LLM-Debate/Debate）、基于拓扑的方法（如DyLAN）和图优化方法（如GPTSwarm、AFLOW、AgentPrune），这些方法均属于“封闭世界”协作。

**主要结果与关键指标**：
1.  **总体性能**：在LLaMA3-8B主干上，HILA在所有基准测试上均显著优于最强的自主多智能体基线，绝对提升幅度在3.7到15.4个百分点之间。具体性能指标（百分比）为：GSM8K (89.86)、AMC (35.83)、AIME (9.37)、HumanEval (72.15)、MMLU (73.62)。在AMC和AIME等竞赛风格数学基准上提升尤为显著。
2.  **跨主干泛化**：在Qwen2.5-7B/3B和LLaMA3-8B/3B四个不同主干上，HILA在GSM8K上均取得最佳性能，且对于较小或较弱模型（如LLaMA3-3B）的补偿效果更明显（相对Vanilla提升38.59个百分点至83.85%），证明了方法的通用性和可扩展性。
3.  **消融分析与能力增长**：通过比较HILA的变体（初始策略、仅内环GRPO优化、完整DLPO），发现完整DLPO带来最全面的性能提升（例如在GSM8K上从88.38%提升至89.86%）。进一步实验表明，经过DLPO训练更新的主干模型，即使应用于其他推理框架（如Vanilla、DyLAN、Debate）且不进行战略延迟，也能带来性能提升（例如将DyLAN的GSM8K得分从82.03%提升至88.32%），证明外部专家反馈通过持续学习增强了主干模型本身的推理能力。
4.  **策略分布演变**：分析训练过程中策略行动（评估、创建、延迟）的分布变化。从初始策略到GRPO再到完整DLPO，系统对“延迟”行动的依赖持续下降（同时“评估”行动增加），表明智能体不仅学会了更具成本效益的干预策略，其内在推理能力也通过持续学习得到增强，从而更少依赖外部帮助。

### Q5: 有什么可以进一步探索的点？

该论文提出的HILA框架虽在人类-智能体协作上迈出重要一步，但仍存在若干局限和可拓展方向。首先，其依赖“人类专家”作为理想反馈源，在实际中可能面临专家成本高、反馈延迟或不一致的问题。未来可探索如何集成更广泛的人类群体智慧（如众包）或利用高质量合成数据（如高级模型的推理过程）来部分替代专家。其次，当前框架主要处理“何时求助”的决策，但未深入优化“如何求助”——例如，智能体可学习如何提炼问题、提供上下文以减少人类认知负荷，或主动提出多个备选方案供人类选择。此外，论文中的持续学习主要基于监督信号，未来可结合更复杂的强化学习范式，让智能体从人类纠正中学习策略调整，而不仅是知识更新。另一个方向是扩展多智能体间的内部协作机制，在求助人类前，先尝试通过内部辩论或分工解决部分不确定性，从而形成“自主协作-人机协作”的层次化决策体系。最后，该框架的评估集中于数学和问题求解任务，未来需在更开放、动态的真实世界场景（如长期项目管理、创意协作）中验证其泛化性和鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对多智能体大语言模型在面临超出预训练知识范围的新任务时容易集体失效的问题，提出了一个名为HILA（人在回路多智能体协作）的框架。其核心贡献是设计了一种元认知策略，使智能体能够自主判断何时自行解决问题、何时向人类专家求助，从而打破纯自治系统的“封闭世界”限制。

方法上，论文引入了双循环策略优化来具体实现这一策略。内循环采用带有成本感知奖励的组相对策略优化，以优化智能体向人类求助的决策时机；外循环则实施持续学习，将人类专家的反馈转化为高质量的监督信号，从而持续增强智能体的推理能力。这种方法将即时决策与长期能力增长解耦。

主要结论是，在具有挑战性的数学和问题求解基准测试上，配备双循环策略优化的HILA框架持续超越了先进的多智能体系统。这为构建能与人类协作并持续进化的智能体系统奠定了理论基础，标志着从单纯扩展单个模型能力向扩展人机协作能力的重要转变。
