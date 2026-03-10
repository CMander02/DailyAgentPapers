---
title: "A Hierarchical Error-Corrective Graph Framework for Autonomous Agents with LLM-Based Action Generation"
authors:
  - "Cong Cao"
  - "Jingyao Zhang"
  - "Kun Tong"
date: "2026-03-09"
arxiv_id: "2603.08388"
arxiv_url: "https://arxiv.org/abs/2603.08388"
pdf_url: "https://arxiv.org/pdf/2603.08388v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Error Analysis"
  - "Graph-Based Retrieval"
  - "Strategy Transfer"
  - "Autonomous Agents"
  - "LLM-Based Action Generation"
relevance_score: 8.5
---

# A Hierarchical Error-Corrective Graph Framework for Autonomous Agents with LLM-Based Action Generation

## 原始摘要

We propose a Hierarchical Error-Corrective Graph FrameworkforAutonomousAgentswithLLM-BasedActionGeneration(HECG),whichincorporates three core innovations: (1) Multi-Dimensional Transferable Strategy (MDTS): by integrating task quality metrics (Q), confidence/cost metrics (C), reward metrics (R), and LLM-based semantic reasoning scores (LLM-Score), MDTS achieves multi-dimensional alignment between quantitative performance and semantic context, enabling more precise selection of high-quality candidate strate gies and effectively reducing the risk of negative transfer. (2) Error Matrix Classification (EMC): unlike simple confusion matrices or overall performance metrics, EMC provides structured attribution of task failures by categorizing errors into ten types, such as Strategy Errors (Strategy Whe) and Script Parsing Errors (Script-Parsing-Error), and decomposing them according to severity, typical actions, error descriptions, and recoverability. This allows precise analysis of the root causes of task failures, offering clear guidance for subsequent error correction and strategy optimization rather than relying solely on overall success rates or single performance metrics. (3) Causal-Context Graph Retrieval (CCGR): to enhance agent retrieval capabilities in dynamic task environments, we construct graphs from historical states, actions, and event sequences, where nodes store executed actions, next-step actions, execution states, transferable strategies, and other relevant information, and edges represent causal dependencies such as preconditions for transitions between nodes. CCGR identifies subgraphs most relevant to the current task context, effectively capturing structural relationships beyond vector similarity, allowing agents to fully leverage contextual information, accelerate strategy adaptation, and improve execution reliability in complex, multi-step tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主智能体（如机器人）在复杂、动态环境中执行多步骤任务时，面临的策略迁移、错误诊断与经验复用三大核心挑战。研究背景是，随着自主机器人和多机器人系统的发展，它们需要在非结构化环境中执行顺序动作、适应意外干扰并高效协作。现有方法（如结合经典规划与强化学习）虽提升了适应性和导航鲁棒性，但仍存在显著不足：1）策略迁移机制大多依赖单维性能指标（如累计奖励或成功率），难以捕捉源任务与目标任务间的语义兼容性与上下文对齐，导致策略选择易受“负迁移”风险影响；2）对执行失败的分析通常停留在聚合指标层面，缺乏结构化机制来分类错误类型、溯源根本原因并评估严重性，限制了系统进行系统性纠正优化的能力；3）在动态任务环境中检索或复用历史经验时，多依赖于扁平的相似性匹配，忽略了历史状态-动作轨迹中嵌入的因果与顺序依赖关系，从而制约了泛化能力和长时域适应性。

为此，本文提出了一个名为“分层纠错图框架”的解决方案，其核心是通过三项创新技术来系统性地应对上述问题：首先，引入“多维可迁移策略”机制，整合任务质量、置信度/成本、奖励以及基于大语言模型的语义推理评分，实现量化性能与语义上下文的多维对齐，以更精准地筛选高质量候选策略并降低负迁移风险。其次，设计“错误矩阵分类”方法，将任务失败归因于十种结构化错误类型（如策略错误、脚本解析错误等），并按严重程度、典型动作、错误描述和可恢复性进行分解，从而为后续纠错和策略优化提供清晰指导，而非仅依赖整体成功率等单一指标。最后，构建“因果-上下文图检索”模块，将历史状态、动作和事件序列组织成图结构，节点存储执行信息，边表示因果依赖关系，以此检索与当前任务上下文最相关的子图，有效捕捉超越向量相似度的结构关系，使智能体能充分利用上下文信息，加速策略适应并提升复杂多步骤任务中的执行可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**基于LLM的任务规划方法**、**面向鲁棒执行的反馈与控制框架**以及**检索增强与结构化记忆机制**。

在**基于LLM的任务规划方法**方面，相关工作（如SayCan、Joublin、InteLiPlan、ProgPrompt）利用LLM将自然语言指令转化为可执行的机器人动作序列，并常与符号推理或低级控制器结合。近期研究进一步探索高层语言推理与可执行控制原语之间的结构化对齐。本文的HECG框架与这些工作共享利用LLM进行高层动作生成的出发点，但区别在于，现有方法通常将可执行动作视为固定序列，依赖粗略的成功/失败信号或事后重规划，缺乏执行过程中系统化的错误阈值层级与纠正机制。本文则通过其核心创新（如错误矩阵分类EMC）系统性地建模和归因任务失败，实现更精细的错误感知控制。

在**面向鲁棒执行的反馈与控制框架**方面，相关工作包括经典的闭环控制、行为树（BTs）、有限状态机（FSMs）等结构化执行框架，它们通过预定义的故障分支和恢复策略提高可靠性。近期研究（如SDA-PLANNER、结合语义数字孪生的方法）尝试引入状态依赖建模和错误自适应修复策略。学习型方法（如分层强化学习HRL、模仿学习）也被用于泛化恢复行为。本文与这些工作共同关注提升执行鲁棒性，但指出现有方法多依赖反应式恢复、二元错误信号，且学习型方法需大量数据、难以解释。本文的HECG框架通过多维度可转移策略（MDTS）和EMC，实现了分级的、多层次的错误建模与纠正策略的层次化集成，将错误感知更直接地嵌入规划-执行循环。

在**检索增强与结构化记忆机制**方面，检索增强生成（RAG）范式被广泛用于改善LLM的上下文 grounding。在具身决策中，现有方法多依赖基于向量相似性的检索（如密集嵌入和最近邻搜索）。近期研究探索了结构化记忆表示（如场景图、任务图）和图检索机制，以捕捉状态、动作和事件之间的高阶依赖关系。本文的因果上下文图检索（CCGR）属于此类，但与现有工作相比，其创新在于将图检索与多维度转移评估（Q, C, R, LLM-Score）及结构化错误分类（EMC）紧密结合，不仅基于结构相似性检索相关子图，还联合考虑了策略可转移性和错误特征，从而更系统地支持经验复用和策略适应，减少负迁移。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“分层纠错图框架”（HECG）的集成系统来解决LLM生成的动作计划在具身模拟环境中执行时存在的“计划-环境对齐差距”和长视野任务中的脆弱性问题。其核心思想是将传统的线性执行过程转化为一个基于图结构的、反馈驱动的自适应控制流程，从而系统性地处理执行偏差，减少不必要的全局重规划，并提高在随机、部分可观测环境下的鲁棒性。

**整体框架与架构设计：**
HECG框架将LLM生成的高级计划表示为一个有向图 \( G = (V, E) \)。图中的节点 \( v_i \) 代表一个可执行的动作或子目标，边 \( e_{ij}^k \) 代表基于执行结果和错误分类的可能状态转移。执行过程因此被建模为图遍历，而非固定序列，使得控制流能根据运行时反馈和分层转移策略动态调整。

**主要模块/组件与关键技术：**

1.  **结构化错误分类与错误矩阵（EMC）：** 这是框架的诊断基础。系统不是笼统地判断任务失败，而是通过“错误矩阵分类”方法，将执行偏差归因于十种具体的错误类型（如策略错误、脚本解析错误等），并根据严重程度、典型动作、错误描述和可恢复性进行分解。这为后续的精准纠错提供了清晰指引。

2.  **基于图的经验检索与因果上下文图检索（CCGR）：** 为了重用历史经验，系统将过往的状态、动作和事件序列构建成经验图。图中的节点存储已执行动作、下一步动作、执行状态、可转移策略等信息，边则编码节点间的因果依赖关系（如状态转移的前提条件）。当遇到执行问题时，“因果上下文图检索”模块会检索与当前任务上下文最相关的子图。这些子图不仅提供候选动作，还包含已知的失败模式和恢复模式，使智能体能充分利用超越向量相似度的结构关系，加速策略适应。

3.  **分层转移策略与多维可转移策略（MDTS）：** 这是框架的决策核心。系统在图中定义了四种边类型：主执行边、可选边、校正边和回退边，分别对应不同的执行与恢复行为。从一个节点出发选择哪条边，由一个概率化的转移策略动态决定。该策略创新性地整合了四个维度的评估信号：
    *   **任务价值（Q）**：评估长期任务效用。
    *   **执行成本（C）**：考虑时间、能耗等效率因素。
    *   **风险（R）**：估计失败可能性或安全风险。
    *   **LLM语义推理分数（Φ_LLM）**：注入常识和逻辑一致性判断。
    通过Softmax函数综合这些维度（即“多维可转移策略”），系统能够实现量化性能与语义上下文的对齐，从而更精确地选择高质量的候选策略。纠错行动也按层次组织：轻微偏差触发本地校正边（如调整参数重试）；若无效，则通过可选边切换到实现同一子目标的替代动作；只有系统性不一致持续存在时，才通过回退边升级到任务级重规划。

**创新点总结：**
论文的核心创新在于将**结构化错误诊断（EMC）、基于因果图的经验检索（CCGR）和融合多维度评估与LLM推理的分层决策（MDTS）** 统一在一个图执行框架（HECG）内。这使智能体能够区分错误类型、复用结构化的恢复知识，并动态选择最合适的恢复路径，从而将脆弱的开环或简单反应式执行，转变为一种反馈感知的、自适应的控制过程，显著提升了长视野任务在复杂动态环境中的执行可靠性和效率。

### Q4: 论文做了哪些实验？

论文在模拟环境中进行了实验，评估了所提出的分层纠错图（HECG）框架。实验设置方面，采用模块化架构实现了HECG智能体，整合了规划、验证和重新规划三个核心组件。数据集使用了广泛采用的具身AI和任务规划数据集VirtualHome，该数据集提供了带标注动作序列的程序化家庭场景，任务类型多样。实验选取了四个代表性任务：ReadBook、PutDishwasher、PrepareFood和PutFridge，场景覆盖卧室、客厅、厨房和浴室，这些任务均需要多步推理、顺序依赖以及与动态对象的交互。

对比方法包括三个基线：1）LLM Planner (Flat)：传统的基于LLM的规划器，一次性生成整个动作序列，无分层纠错或重新规划机制；2）HECG w/o Transition：HECG的变体，包含分层纠错但移除了学习到的转移策略，用于衡量显式状态转移的影响；3）HECG Full：完整的HECG智能体，同时启用分层纠错和转移策略。

主要结果方面，论文通过任务成功率等指标进行评估。关键数据指标显示，HECG Full在所有测试任务上均取得了最高的成功率，显著优于LLM Planner (Flat)基线。HECG w/o Transition的性能介于两者之间，表明转移策略对性能提升有重要贡献。具体而言，在复杂任务（如PrepareFood）上，HECG Full的成功率相比扁平LLM规划器有大幅提升，凸显了其分层纠错和因果上下文图检索在应对动态不确定性方面的优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的HECG框架在策略迁移、错误归因和因果检索方面有显著创新，但其局限性和未来探索方向可从以下几点展开：

**局限性方面**：首先，框架依赖LLM生成动作和评分，可能受模型幻觉和上下文长度限制，在长序列任务中误差易累积。其次，错误矩阵（EMC）的十类错误划分虽细致，但未充分探讨错误间的因果链，且修复建议仍依赖人工规则，自动化程度有限。最后，因果图（CCGR）的构建基于历史数据，在新领域或稀疏数据环境中可能检索效率低下。

**未来研究方向**：可探索以下改进：1. **动态错误修复机制**：将EMC与强化学习结合，让智能体通过试错自动生成修复策略，减少人工干预。2. **轻量化图检索优化**：引入元学习或图神经网络压缩技术，提升CCGR在新任务中的泛化能力和检索速度。3. **多模态策略对齐**：扩展MDTS的评估维度，融入环境感知（如视觉信号）或人类反馈，增强策略迁移的鲁棒性。4. **可解释性深化**：利用因果推理模型解析错误矩阵中的潜在关联，为智能体决策提供更透明的诊断路径。这些方向有望进一步提升自主智能体在开放环境中的适应性和可靠性。

### Q6: 总结一下论文的主要内容

本文提出了一种用于自主智能体的分层纠错图框架HECG，其核心贡献在于通过三个创新模块提升智能体在复杂任务中的执行可靠性与策略适应性。问题定义聚焦于现有智能体在动态多步任务中常面临策略负迁移、失败根因分析不足以及上下文检索能力有限等挑战。

方法概述包含：1) 多维可迁移策略，整合任务质量、置信度/成本、奖励及LLM语义推理分数，实现量化性能与语义上下文的多维对齐，精准筛选高质量策略以降低负迁移风险；2) 错误矩阵分类，将任务失败归因于十类错误类型，并按严重程度、典型动作等维度分解，为纠错与优化提供结构化指导；3) 因果上下文图检索，基于历史状态、动作序列构建图结构，通过节点存储执行信息与边表示因果依赖，检索与当前任务最相关的子图，增强上下文感知与策略适应速度。

主要结论表明，HECG框架能系统性地提升智能体的错误诊断与纠正能力，支持更高效的策略迁移与可靠的自主执行，为复杂任务环境下的智能体优化提供了可解释且实用的方法论。
