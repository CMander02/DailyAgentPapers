---
title: "Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents"
authors:
  - "Yuxuan Cai"
  - "Jie Zhou"
  - "Qin Chen"
  - "Liang He"
date: "2026-04-22"
arxiv_id: "2604.20572"
arxiv_url: "https://arxiv.org/abs/2604.20572"
pdf_url: "https://arxiv.org/pdf/2604.20572v1"
categories:
  - "cs.CL"
tags:
  - "Lifelong Learning"
  - "Experience Retrieval"
  - "Proactive Agent"
  - "Memory-Augmented Agent"
  - "Reinforcement Learning"
  - "Agent Architecture"
  - "Online Learning"
relevance_score: 8.5
---

# Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents

## 原始摘要

Online lifelong learning enables agents to accumulate experience across interactions and continually improve on long-horizon tasks. However, existing methods typically treat retrieval from past experience as a passive operation, triggering it only at task initialization or after completing a step. Consequently, agents often fail to identify knowledge gaps during interaction and proactively retrieve the most useful experience for the current decision. To address this limitation, we present ProactAgent, an experience-driven lifelong learning framework for proactive retrieval over a structured experience base. We first introduce Experience-Enhanced Online Evolution (ExpOnEvo), which enables continual improvement through both policy updates and memory refinement. The experience base organizes historical interactions into typed repositories, including factual memory, episodic memory, and behavioral skills, so that retrieval can provide both relevant evidence and actionable guidance. On top of this, we propose Proactive Reinforcement Learning-based Retrieval (ProactRL), which models retrieval as an explicit policy action and learns when and what to retrieve via paired-branch process rewards. By comparing continuations from identical interaction prefixes with and without retrieval, ProactRL provides step-level supervision for retrieval decisions, encouraging retrieval only when it leads to better task outcomes or higher efficiency. Experiments on SciWorld, AlfWorld, and StuLife show that ProactAgent consistently improves lifelong agent performance, achieving success rates of 73.50\% on SciWorld and 71.28\% on AlfWorld while substantially reducing retrieval overhead, and attains performance competitive with proprietary models on StuLife.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在线终身学习智能体在利用历史经验进行决策时存在的被动检索问题。研究背景是，随着语言智能体从孤立任务求解向在线终身学习范式演进，智能体需要在持续交互的任务流中积累经验，以应对不断变化的环境。尽管现有方法通过外部经验库为智能体提供了记忆增强能力，但它们通常将检索视为被动操作，仅在任务初始化或完成步骤后触发，导致智能体难以在交互过程中主动识别知识缺口，并动态获取对当前决策最有用的经验。

现有方法的不足主要体现在两方面：一是检索机制本质上是被动的，依赖于预定义的位置、外部设计的规则或独立的门控模块，而非由智能体自身学习何时检索，这限制了智能体在动态任务中主动填补知识空白的能力；二是在线更新策略通常将文本记忆积累与参数优化视为独立过程，要么仅关注记忆存储，要么只优化策略参数，未能协同演化，从而限制了智能体从交互历史中持续改进的能力。

本文要解决的核心问题是：如何让智能体在终身学习过程中主动、高效地检索历史经验，并同时实现记忆与策略的协同在线演化。为此，论文提出了ProactAgent框架，通过两个关键组件应对上述挑战：一是经验增强的在线演化机制，联合优化记忆库和策略参数；二是基于强化学习的主动检索方法，将检索建模为显式的策略动作，并通过对比有无检索的交互分支奖励，学习在何时检索何种经验，从而在提升任务性能的同时减少冗余检索开销。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆增强的终身智能体、大语言模型的检索控制，以及交互式智能体的在线演化。

在**记忆增强的终身智能体**方面，现有工作通过外部记忆系统来积累跨回合的交互经验。它们在检索触发机制上存在差异，包括静态初始化、持续检索和LLM门控等方法。然而，这些方法通常将检索视为被动的、按固定规则执行的操作，且记忆库多为单一、未分类型，未能区分事实证据与行为指导。本文提出的ProactAgent则构建了结构化的经验库（包括事实记忆、情景记忆和行为技能），并将检索建模为智能体可学习的显式策略动作，从而能主动识别知识缺口。

在**大语言模型的检索控制**方面，相关工作（如FLARE、Self-RAG、Toolformer、ReAct）通过置信度阈值或监督分类器来决策检索时机，提升了检索精度。但这些方法主要面向静态知识库，且其检索决策是“被动”的，缺乏基于任务最终结果的反馈来评估特定检索动作的价值。本文的ProactRL方法则通过配对分支过程奖励，在终身学习动态增长的经验库中，为检索决策提供步骤级的监督信号，直接学习何时检索以及检索什么。

在**交互式智能体的在线演化**方面，现有研究通过记忆中心（如Reflexion、Voyager积累文本经验）或参数中心（在线强化学习优化策略）的途径实现持续改进，但两者往往相互孤立。本文的ExpOnEvo框架将策略更新与记忆精化相结合，实现了协同的持续改进，克服了现有方法将记忆增长与策略更新割裂的局限。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ProactAgent的框架来解决经验驱动型终身智能体在交互过程中被动检索、无法主动识别知识缺口并获取最有用经验的问题。该框架的核心由两个紧密耦合的组件构成：经验增强的在线演化（ExpOnEvo）和基于强化学习的主动检索（ProactRL）。

**整体框架与主要模块：**
ProactAgent的整体架构是一个自我强化的闭环系统。首先，**经验增强的在线演化（ExpOnEvo）** 构成了框架的基础循环，它将智能体的行动、经验积累与策略优化统一起来。智能体在与环境交互（行动）的同时，会从一个结构化的经验库中进行主动检索。完成的任务轨迹会被提炼并存入经验库，而策略则通过强化学习在收集的轨迹上进行更新。这创造了一个良性循环：更丰富的经验库提供更相关的检索结果，从而提升轨迹质量，进而产生更高质量的经验条目和更强的策略梯度。

经验库的组织是架构设计的关键创新。它并非单一存储池，而是将历史交互组织成**五个类型化的存储库**：事实记忆（$\mathcal{M}^f$）、情景记忆（$\mathcal{M}^e$）、成功技能（$\mathcal{S}^+$）、失败技能（$\mathcal{S}^-$）和对比技能（$\mathcal{S}^\Delta$）。这种结构化设计使得一次查询能同时返回互补的证据（什么为真、过去发生了什么）和行为指导（该做什么、应避免什么），解决了单一记忆池可能导致的冗余或冲突问题。检索时，系统会从每个类型库中按排名（结合查询相似性和条目优先级）返回Top-K条目，确保结果的多样性和相关性。

**核心方法与创新点：**
框架最核心的创新是**基于强化学习的主动检索（ProactRL）**，它直接将“检索”建模为策略可执行的一个显式动作。其关键技术在于解决了如何为具体的检索决策提供步骤级监督的难题。传统的结果级奖励无法判断某次检索是否必要或有益。

为此，ProactRL引入了**配对分支过程奖励**机制。当一次初始交互轨迹在步骤$t_b$触发了检索动作时，系统会从完全相同的历史前缀$h_{t_b}$开始，自适应地采样两条后续分支轨迹：一条是包含该检索动作的原始分支（$\tau^{ret}$），另一条是临时抑制该检索动作、探索其他可能性的“无检索”分支（$\tau^{no\text{-ret}}$）。通过比较这两条共享前缀但后续决策不同的轨迹结果（如累计环境奖励和步骤数），可以精确计算出**检索边际收益**（$\Delta_i$）。基于此，系统为包含检索的轨迹分配一个**过程奖励**（$r_i^{proc}$）：仅当检索确实带来了更优或更高效的结果（$\Delta_i > 0$）时给予正奖励；若检索反而导致表现变差（$\Delta_i < 0$）则给予惩罚；其他情况奖励为零。此外，还引入了效率惩罚项（$r_i^{eff}$）来抑制重复查询和鼓励更短的成功轨迹。

这种方法为检索决策提供了直接的步骤级监督，教导智能体学会识别知识缺口，并仅在检索能切实改善后续进程时才主动发起查询，从而实现了真正的“主动性”。策略（包括检索决策和任务动作）通过GRPO等强化学习算法，利用结合了环境奖励、过程奖励和效率奖励的总轨迹奖励进行联合优化。

总之，论文通过ExpOnEvo构建了经验与策略协同进化的闭环，并通过ProactRL的创新性配对分支奖励机制，使智能体能够学习在何时、检索何种经验，从而在多个实验环境中显著提升了任务成功率和效率。

### Q4: 论文做了哪些实验？

论文在三个交互式基准测试（SciWorld、AlfWorld、StuLife）上进行了实验，以评估所提出的ProactAgent框架。实验设置使用Qwen2.5-7B-Instruct作为基础模型，并包含一个使用Qwen2.5-3B-Instruct的扩展实验。对比方法包括离线基线（如ReAct、SFT、GRPO）和在线基线（如在线GRPO、AWM、Reflexion、MemoryBank、Mem0以及GRPO+Reflexion）。主要结果如下：在SciWorld上，ProactAgent取得了73.50%的成功率（SR）和平均18.38轮交互，显著优于最强的在线基线GRPO+Reflexion（55.50% SR，27.52轮）。在AlfWorld上，ProactAgent达到71.28% SR和12.73轮，对比GRPO+Reflexion的67.18% SR和16.42轮。在StuLife上，ProactAgent获得12.35% SR和19.26 StuGPA，表现优于所有基线并接近专有模型性能。关键数据指标显示，ProactAgent在SciWorld和AlfWorld上分别将交互轮数降低了33.2%和22.5%，同时每任务仅消耗0.43k令牌，效率显著提升。消融实验证实了主动检索学习（ProactRL）和联合演化（ExpOnEvo）的关键作用，移除主动检索导致SciWorld上SR大幅下降45.0点。此外，模型缩放实验表明，即使使用3B模型，ProactAgent也能达到53.50% SR，接近7B基线的性能，同时减少48%的交互轮数。案例研究进一步说明，在关键决策点进行针对性检索能有效避免失败轨迹，提升长期任务完成的可靠性。

### Q5: 有什么可以进一步探索的点？

本文提出的ProactAgent框架在主动检索和结构化经验库方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，实验环境（SciWorld、AlfWorld等）虽具挑战性，但均为模拟或受限领域，未来需在更开放、动态的真实世界场景（如机器人交互、在线客服）中验证其泛化能力。其次，当前检索决策主要基于任务结果奖励，可能忽略长期知识积累的价值；可探索引入内在动机或好奇心驱动机制，使代理在无明显即时回报时也能主动获取潜在有用的经验。此外，经验库的结构化方式（事实、情节、技能）虽合理，但类型划分可能不够灵活；未来可研究动态类型生成或跨类型关联检索，以更好地支持复杂决策。从技术角度看，ProactRL的配对分支奖励设计依赖于精确的步骤级比较，这在部分稀疏奖励任务中可能难以实施；可结合模型不确定性估计或元学习来优化检索触发条件。最后，框架未充分探讨多代理协作场景下的经验共享与检索，这在分布式终身学习中是关键挑战。总体而言，如何使主动检索机制更高效、可解释且适应不断演化的环境，是未来研究的核心。

### Q6: 总结一下论文的主要内容

本文针对在线终身学习智能体在交互过程中被动检索经验、无法主动识别知识缺口的问题，提出了ProactAgent框架。其核心贡献在于将检索建模为智能体的显式策略动作，并通过经验增强的在线演化机制，联合优化记忆库与决策策略。

具体而言，论文首先设计了经验增强在线演化（ExpOnEvo），将历史交互组织为事实记忆、情景记忆和行为技能等类型化存储库，支持在交互过程中同步更新记忆内容与策略参数。在此基础上，提出了基于强化学习的主动检索方法（ProactRL），通过对比同一交互前缀下执行检索与不执行检索所导致的不同任务延续结果，获得步骤级的检索决策监督信号，从而学习在何时检索以及检索何种经验，确保检索仅在能提升任务效果或效率时触发。

实验表明，该方法在SciWorld和AlfWorld上分别取得了73.50%和71.28%的成功率，同时显著降低了检索开销，在StuLife上也达到了与专有模型竞争的性能。这证明了主动检索与联合演化机制能有效提升终身学习智能体的适应能力和决策效率。
