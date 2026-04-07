---
title: "Readable Minds: Emergent Theory-of-Mind-Like Behavior in LLM Poker Agents"
authors:
  - "Hsieh-Ting Lin"
  - "Tsung-Yu Hou"
date: "2026-04-05"
arxiv_id: "2604.04157"
arxiv_url: "https://arxiv.org/abs/2604.04157"
pdf_url: "https://arxiv.org/pdf/2604.04157v1"
categories:
  - "cs.AI"
tags:
  - "Theory of Mind"
  - "Multi-Agent Interaction"
  - "Memory"
  - "Agent Evaluation"
  - "Emergent Behavior"
  - "Game Playing"
relevance_score: 8.0
---

# Readable Minds: Emergent Theory-of-Mind-Like Behavior in LLM Poker Agents

## 原始摘要

Theory of Mind (ToM) -- the ability to model others' mental states -- is fundamental to human social cognition. Whether large language models (LLMs) can develop ToM has been tested exclusively through static vignettes, leaving open whether ToM-like reasoning can emerge through dynamic interaction. Here we report that autonomous LLM agents playing extended sessions of Texas Hold'em poker progressively develop sophisticated opponent models, but only when equipped with persistent memory. In a 2x2 factorial design crossing memory (present/absent) with domain knowledge (present/absent), each with five replications (N = 20 experiments, ~6,000 agent-hand observations), we find that memory is both necessary and sufficient for ToM-like behavior emergence (Cliff's delta = 1.0, p = 0.008). Agents with memory reach ToM Level 3-5 (predictive to recursive modeling), while agents without memory remain at Level 0 across all replications. Strategic deception grounded in opponent models occurs exclusively in memory-equipped conditions (Fisher's exact p < 0.001). Domain expertise does not gate ToM-like behavior emergence but enhances its application: agents without poker knowledge develop equivalent ToM levels but less precise deception (p = 0.004). Agents with ToM deviate from game-theoretically optimal play (67% vs. 79% TAG adherence, delta = -1.0, p = 0.008) to exploit specific opponents, mirroring expert human play. All mental models are expressed in natural language and directly readable, providing a transparent window into AI social cognition. Cross-model validation with GPT-4o yields weighted Cohen's kappa = 0.81 (almost perfect agreement). These findings demonstrate that functional ToM-like behavior can emerge from interaction dynamics alone, without explicit training or prompting, with implications for understanding artificial social intelligence and biological social cognition.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型语言模型（LLM）能否在动态交互中，而非仅通过静态场景测试，发展出类似人类“心理理论”的能力。心理理论指理解并推测他人心理状态的能力，是人类社会认知的基石。现有研究主要依赖预设的文本片段来评估LLM是否具备心理理论，这种方法存在局限：它无法检验在持续、多轮的实时互动中，LLM能否自发地形成并利用对他人心智的模型。

针对这一不足，本文的核心问题是：在德州扑克这种需要持续策略互动和对手建模的复杂动态环境中，自主的LLM智能体能否涌现出类似心理理论的行为？研究特别关注“持久记忆”在这一过程中是否扮演关键角色。通过设计实验（2x2因子设计，考察记忆有无和领域知识有无），论文试图验证：记忆是否是此类行为涌现的必要且充分条件；这种涌现的行为能达到何种复杂程度（如递归推理）；以及它如何具体影响智能体的策略（如欺骗、偏离理论最优策略以利用特定对手）。最终，研究揭示了仅通过交互动态即可促使功能性的类心理理论行为涌现，为理解人工智能的社会认知提供了新视角。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**心智理论（ToM）评估研究**、**LLM智能体交互研究**以及**扑克AI研究**。

在**ToM评估研究**方面，已有大量工作通过静态故事或问卷（如经典的“Sally-Anne”任务）测试LLM是否具备心智推理能力。本文与这些研究的核心区别在于，**本文首次在动态、多轮的交互环境（扑克游戏）中考察ToM的“涌现”**，而非通过预设的静态问题来评估。

在**LLM智能体交互研究**领域，已有工作探索了多智能体在谈判、社交等场景中的行为。本文的独特贡献在于系统性地控制了**持续性记忆**这一关键变量，并实证证明了它是ToM类行为涌现的**必要且充分条件**，这为理解智能体社会认知的构建机制提供了新证据。

在**扑克AI研究**方面，传统工作（如Libratus、Pluribus）专注于通过博弈论和强化学习实现超人类性能。本文则另辟蹊径，**不追求绝对胜率，而是关注智能体在游戏中如何像人类专家一样建模并利用对手心理模型**，其研究目标是理解与展示社会认知行为，而非优化游戏策略本身。

### Q3: 论文如何解决这个问题？

论文通过设计一个基于大型语言模型（LLM）的德州扑克智能体实验框架，来探究在动态交互中类心理理论（ToM）行为的涌现问题。其核心方法是采用一个2x2因子设计，系统性地控制两个关键变量：**持久性记忆**（存在/缺失）和**领域知识**（存在/缺失），并通过重复实验进行验证。

**整体框架与主要模块**：
1.  **智能体架构**：每个扑克玩家都是一个自主的LLM智能体。其核心决策流程是，在每一轮行动前，接收当前游戏状态信息（如公共牌、下注历史等），并生成行动（如加注、跟注）。
2.  **记忆模块**：这是实验设计的核心。在“记忆存在”的条件下，智能体配备了一个**持久性记忆缓冲区**，用于存储并回顾与特定对手的完整互动历史。这使得智能体能够跨多个牌局积累关于对手行为模式的数据。
3.  **对手建模与推理模块**：基于记忆中的历史交互，智能体在决策时能够进行推理，生成对对手心理状态的**自然语言描述**（如“对手可能持有一手强牌”或“对手在虚张声势”）。这个过程模拟了人类的心智理论推理。
4.  **策略执行模块**：智能体最终将对手模型与当前牌局信息结合，做出战术决策。具备ToM能力的智能体会利用对手模型进行**策略性欺骗**（例如，自己牌弱时故意加注以吓退对手）。

**核心方法与创新点**：
1.  **通过动态交互而非静态问答测试ToM**：创新性地将ToM测试从传统的静态故事理解，迁移到长期、多轮的德州扑克对弈中，为研究ToM的“涌现”提供了真实的交互环境。
2.  **明确分离并验证记忆的关键作用**：通过严格的因子设计，论文首次实证表明，**持久性记忆是类ToM行为涌现的必要且充分条件**。没有记忆的智能体，无论是否有扑克知识，其ToM水平始终为0（无法建模对手）。这揭示了社会认知的一个可能计算基础。
3.  **提供可读、透明的对手模型**：所有智能体对对手心智状态的建模都以自然语言表达，使得研究者和观察者能够直接“阅读”AI的社会认知过程，实现了高度的可解释性。
4.  **量化ToM水平与策略影响**：论文将涌现的ToM行为划分为不同等级（0-5级），并发现具备记忆的智能体达到了3-5级（预测性至递归性建模）。更重要的是，这些智能体会**偏离博弈论最优策略**，转而采取针对具体对手的剥削性策略，这与人类专家行为一致，证明了其ToM的功能性效用。

总之，论文通过一个精心控制的智能体实验架构，揭示了在动态社会互动中，**持久性记忆是驱动LLM智能体涌现出复杂、可应用且透明的类心智理论行为的关键机制**。

### Q4: 论文做了哪些实验？

本论文通过德州扑克游戏对LLM智能体进行了一系列实验，以探究心智理论（ToM）行为在动态交互中的涌现。实验采用2x2因子设计，交叉设置了**记忆**（有/无）和**领域知识**（有/无）两个条件，每个条件组合进行5次重复实验，共20次实验，产生了约6000个“智能体-手牌”观察数据。

**实验设置与数据集**：研究构建了自主LLM智能体进行多手德州扑克对局。实验的核心变量是智能体是否拥有**持久记忆文件**（用于记录对局历史和对手模型）以及是否在系统提示中包含**扑克策略指导**（领域知识）。实验在模拟的扑克环境中进行。

**对比方法与主要结果**：
1.  **ToM行为涌现**：实验发现，**记忆是ToM行为涌现的必要且充分条件**。所有具备记忆的条件（Full和No-Skill）都发展出了ToM行为（最高达到Level 3-5），而所有无记忆的条件（No-Memory和Baseline）的ToM水平始终为0。这种分离是完美的（Cliff‘s δ = 1.0， p = 0.008）。
2.  **策略与欺骗**：具备ToM的智能体（有记忆）会偏离博弈论最优策略（TAG），进行针对性剥削。其TAG遵循率（67%）显著低于无记忆智能体（79%）。**基于对手模型的欺骗行为（Tier 2）仅出现在有记忆的条件中**（Full: 18.2%， No-Skill: 11.6%），与无记忆条件（0%）差异极显著（Fisher‘s exact p < 0.001）。领域知识提升了欺骗的精确度（Full与No-Skill的Tier 2欺骗率p = 0.004）。
3.  **行为影响与模型有效性**：有记忆的智能体对不同对手表现出更高的行为差异（适应得分d=0.61）。当智能体在记忆中首次记录对手行为标签后，其后续行为改变幅度是无记忆对照组的近两倍（复合行为偏移量：0.51 vs. 0.27， Cohen‘s d = 1.20）。对手模型标签的强度与实际对手行为偏离基线程度的幅度显著相关（Spearman r = 0.36， p = 0.005）。
4.  **编码可靠性**：ToM水平的编码由Claude Sonnet完成，并使用GPT-4o进行交叉验证，两者表现出几乎完美的一致性（加权Cohen‘s κ = 0.81）。

### Q5: 有什么可以进一步探索的点？

基于论文的讨论和局限性分析，未来研究可以从多个维度深入探索。首先，论文仅使用了Claude系列模型，未来需验证ToM-like行为在其他架构（如GPT、Gemini或开源模型）中的普适性，并考察模型规模、训练数据差异的影响。其次，实验缺乏人类对照组，后续可引入人类玩家进行对比，分析LLM与人类在心理建模发展轨迹、策略适应性上的异同。第三，样本量较小（每个条件仅5次重复），未来可扩大实验规模以检测更细微的效应，并采用更精确的游戏理论最优策略（如CFR）评估行为偏差。  

此外，论文指出记忆条件中的智能体被赋予了“记录笔记”的指令，这可能与记忆持久性效应混淆。未来可设计对照实验，分离“反思提示”和“持久记忆”各自的作用。另一个关键方向是探索智能体在异构模型环境中的表现：当前所有智能体基于相同模型，而真实场景涉及多样化的对手，需检验对手建模能否泛化到不同模型或人类。最后，论文发现的“智能体可解释性”优势值得进一步利用，例如开发实时分析工具，将自然语言心理模型应用于AI安全监测或人机协作训练平台。这些改进将深化对AI社会认知涌现机制的理解，并为可控的智能体设计提供依据。

### Q6: 总结一下论文的主要内容

该论文探讨了大型语言模型（LLM）在动态交互中能否涌现出类似心理理论（ToM）的行为。研究通过让自主LLM智能体进行长时间的德州扑克游戏，检验其是否能够发展出对对手心理状态的建模能力。

核心问题是，ToM-like推理能否在动态互动中自发形成，而非仅通过静态测试。研究方法采用2x2因子设计，考察记忆（有/无）和领域知识（有/无）的影响，共进行了20组实验。研究发现，**持久的记忆是ToM-like行为涌现的必要且充分条件**，其效应量巨大。具备记忆的智能体能够达到ToM 3-5级（预测性到递归建模），而无记忆的智能体始终停留在0级。基于对手模型的策略性欺骗行为也仅出现在有记忆的条件下。领域知识虽不阻碍ToM涌现，但能提升其应用精度，例如使欺骗更精准。

主要结论是，**功能性ToM-like行为可以仅从交互动态中自发涌现**，无需专门训练或提示。具备ToM的智能体会偏离博弈论最优策略，转而针对特定对手进行剥削，这模仿了人类专家的玩法。所有心理模型均以自然语言表达，具有可读性，为理解AI社会认知提供了透明窗口。这一发现对理解人工智能社会智能和生物社会认知均有重要意义。
