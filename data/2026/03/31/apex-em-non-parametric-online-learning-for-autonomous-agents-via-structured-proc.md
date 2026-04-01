---
title: "APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay"
authors:
  - "Pratyay Banerjee"
  - "Masud Moshtaghi"
  - "Ankit Chadha"
date: "2026-03-31"
arxiv_id: "2603.29093"
arxiv_url: "https://arxiv.org/abs/2603.29093"
pdf_url: "https://arxiv.org/pdf/2603.29093v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "Agent Memory"
  - "Experience Replay"
  - "Non-Parametric Learning"
  - "Procedural Memory"
  - "Online Learning"
  - "Task Planning"
  - "Code Generation"
  - "Knowledge Graph QA"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay

## 原始摘要

LLM-based autonomous agents lack persistent procedural memory: they re-derive solutions from scratch even when structurally identical tasks have been solved before. We present \textbf{APEX-EM}, a non-parametric online learning framework that accumulates, retrieves, and reuses structured procedural plans without modifying model weights. APEX-EM introduces: (1) a \emph{structured experience representation} encoding the full procedural-episodic trace of each execution -- planning steps, artifacts, iteration history with error analysis, and quality scores; (2) a \emph{Plan-Retrieve-Generate-Iterate-Ingest} (PRGII) workflow with Task Verifiers providing multi-dimensional reward signals; and (3) a \emph{dual-outcome Experience Memory} with hybrid retrieval combining semantic search, structural signature matching, and plan DAG traversal -- enabling cross-domain transfer between tasks sharing no lexical overlap but analogous operational structure. Successful experiences serve as positive in-context examples; failures as negative examples with structured error annotations.
  We evaluate on BigCodeBench~\cite{zhuo2025bigcodebench}, KGQAGen-10k~\cite{zhang2025kgqagen}, and Humanity's Last Exam~\cite{phan2025hle} using Claude Sonnet 4.5 and Opus 4.5. On KGQAGen-10k, APEX-EM achieves 89.6\% accuracy versus 41.3\% without memory (+48.3pp), surpassing the oracle-retrieval upper bound (84.9\%). On BigCodeBench, it reaches 83.3\% SR from a 53.9\% baseline (+29.4pp), exceeding MemRL's~\cite{memrl2025} +11.0pp gain under comparable frozen-backbone conditions (noting backbone differences controlled for in our analysis). On HLE, entity graph retrieval reaches 48.0\% from 25.2\% (+22.8pp). Ablations show component value is task-dependent: rich judge feedback is negligible for code generation but critical for structured queries (+10.3pp), while binary-signal iteration partially compensates for weaker feedback.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自主智能体缺乏持久性、结构化过程记忆的问题。研究背景是，尽管LLM智能体在多步推理、代码生成等方面表现出色，但它们本质上在过程层面是“无状态”的。每次执行任务都需从头开始推理，无法像强化学习（RL）智能体那样，通过“经验回放缓冲区”积累和重用结构化的执行经验。现有方法（如MemRL、Voyager、Reflexion等）已开始为LLM智能体引入记忆机制，但仍存在三个核心不足：1. **经验表示扁平化**：现有方法存储的是非结构化的文本摘要或特定领域片段（如代码片段、反思日志），丢弃了任务执行的过程结构（如规划步骤、迭代历史、错误链、生成产物），导致检索到的记忆只能提供模糊的叙事性提示，而非可重放、可适配的完整过程。2. **缺乏双结果学习**：现有系统要么只存储成功经验，要么存储的经验缺乏系统化的质量评估。没有系统能同时将成功经验作为正面示例、将失败经验作为带有结构化错误标注的负面示例进行存储和利用，这限制了智能体从错误中学习的能力。3. **缺乏跨领域结构迁移能力**：现有检索机制主要依赖任务描述的表面语义相似度，无法识别和迁移那些表面描述不同但操作结构（如查询、过滤、聚合的流程）相似的任务。例如，从体育数据库查询中学到的过程，无法有效迁移到结构类似但领域不同的金融数据库查询任务。

因此，本文要解决的核心问题是：如何为LLM智能体构建一个**非参数化的在线学习框架**，使其能够积累、检索和重用**结构化的过程-情景经验**，从而实现类似经验回放的效果，提升智能体的任务执行效率和跨领域泛化能力，而无需修改模型权重。具体而言，APEX-EM框架通过引入结构化经验表示、带有多维奖励信号的PRGII工作流程以及结合语义与结构匹配的双结果经验记忆库，来直接应对上述三个不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆系统、经验回放与在线学习，以及案例推理。

在**记忆系统**方面，相关工作包括MemGPT（操作系统启发的内存层次）、Reflexion（基于自然语言反思的强化学习）、Voyager（用于具身智能体的已验证代码技能库）、Generative Agents（带周期性反思的记忆流），以及近期的A-MEM（基于卡片盒的自主链接记忆）、Mem0（以实体为中心的关系图）和MIRIX（多智能体路由的专用记忆存储）。这些系统大多存储非结构化的反思、代码片段或实体关系，而本文提出的APEX-EM则存储**结构化的程序性-情景性执行轨迹**，并具有双结果（成功/失败）索引和跨领域结构检索能力，这是与现有工作的核心区别。

在**经验回放与在线学习**方面，传统深度强化学习中的经验回放通过存储状态转移并利用梯度下降更新权重来稳定训练。APEX-EM与之概念相似，但本质不同：它通过**上下文学习**而非权重更新来改进；存储的是高级程序性计划而非低级状态转移；检索基于语义和结构匹配而非随机或优先级采样；并明确区分正负示例用于不同检索角色。最接近的前期工作是MemRL，它也是一个非参数、冻结主干网络的系统，在运行时积累经验。但MemRL存储的是LLM总结的反思（而非完整结构化轨迹），使用Q值加权排序（而非结构签名匹配），且通过Q值隐式编码成败（而非显式双结果索引）。APEX-EM的关键优势在于其**结构签名匹配机制**，能在任务间词汇零重叠的情况下实现有效的跨领域迁移，而MemRL在此类场景下性能会下降。

在**案例推理**方面，经典的“检索-重用-修正-保留”循环与本文的PRGII工作流程有结构相似性。但APEX-EM的不同之处在于：维护双结果索引（CBR通常只存储成功案例）；利用LLM进行上下文自适应而非依赖手工制定的转换规则；使用密集语义嵌入和结构签名进行相似性匹配而非基于特征的方法；并采用基于多标准评估的质量门控提交机制。

此外，其他相关方法如ALMA（元学习发现记忆设计）、SkillRL（通过RL权重更新提取可重用技能）、MemSkill（学习记忆操作本身）以及LATS（单回合内的蒙特卡洛树搜索）等，均未提供APEX-EM所具备的、可部署的、基于结构化程序性记忆的非参数在线学习架构。

### Q3: 论文如何解决这个问题？

APEX-EM 通过一个非参数化的在线学习框架来解决基于LLM的自主智能体缺乏持久性程序记忆的问题，其核心在于构建、检索和重用结构化的程序性计划，而无需修改模型权重。该框架的核心方法、架构设计和关键技术如下：

**整体框架与工作流程（PRGII）**：
框架采用 **Plan-Retrieve-Generate-Iterate-Ingest** 五阶段工作流。对于一个新任务，智能体首先进行**规划**，解析任务、发现实体与模式，并提取其**结构签名**（即抽象操作类型的序列）。接着，系统从**经验记忆**中**检索**相关经验。然后，基于检索到的上下文示例**生成**可执行工件（如代码、查询），并进行多轮**迭代**执行与验证。最后，将完整的执行记录**摄取**到经验记忆中，形成新的结构化经验节点。整个过程由可插拔的领域适配器、验证器和提示模板支持，实现了通用流程与领域特化的解耦。

**核心架构与主要模块**：
1.  **结构化经验表示与程序知识图谱**：这是框架的核心创新。每个任务执行过程被编码为一个结构化的**经验**节点，存储在**程序知识图谱**中。经验节点采用分层本体设计，包含六个可独立查询的反射层：目标反射（任务目标）、程序反射（可重用的参数化步骤模板）、证据反射（观察到的证明）、执行轨迹、错误注册表（结构化错误分解）和补丁反射（具体修复方案）。PKG还包括实体、子任务、操作和任务主题等其他节点类型，通过十种边类型（如 `uses_entity`, `structurally_similar_to`, `supersedes`）连接，形成一个统一的知识网络。
2.  **双结果经验记忆与混合检索机制**：经验记忆明确区分成功与失败的经验。检索时采用**混合策略**：结合**语义搜索**（基于任务描述嵌入）、**结构签名匹配**（基于最长公共子序列等算法比较操作序列）和**PKG图遍历**。这种设计使得系统能够实现**跨领域迁移**——即使任务在词汇上没有重叠，只要具有相似的操作结构（结构签名），就能检索并复用相关经验。成功的经验作为正面的上下文示例，失败的经验则提供带有结构化错误注释的负面示例，起到警示和指导作用。
3.  **实体解析与世界状态管理**：系统引入**实体解析器**，将任务中提到的实体映射到PKG中的现有实体节点，实现去重和消歧。实体作为PKG中的一等公民，通过 `uses_entity` 边与经验相连。当现实世界实体发生变化时（如API端点迁移），只需更新对应的实体节点并建立 `supersedes` 边，所有引用该实体的经验会自动解析到最新版本，避免了平面文本记忆中信息过时或需要大量重写的问题。

**关键创新点**：
*   **非参数化在线学习**：性能随经验积累而提升，模型参数固定。
*   **结构化程序-情景经验表示**：将完整的执行轨迹、错误分析和质量评分编码为可查询、可重用的结构化记录。
*   **基于结构签名的跨领域迁移**：通过比较抽象操作序列，实现词汇不同但操作逻辑相似的任务间的知识迁移。
*   **双结果记忆与结构化错误利用**：显式存储和利用失败经验，其结构化的错误注册表和补丁为后续任务提供防护。
*   **动态世界状态维护**：通过PKG中的实体节点和版本化边，高效、一致地管理变化的世界知识。

### Q4: 论文做了哪些实验？

该论文在三个基准测试上进行了实验评估，以验证APEX-EM框架的有效性。

**实验设置与数据集/基准测试**：
实验使用了三个基准测试：BigCodeBench（代码生成）、KGQAGen-10k（知识图谱问答生成）和Humanity's Last Exam（HLE，实体图检索）。模型主干为Claude Sonnet 4.5和Opus 4.5，并保持其权重冻结。实验的核心是比较APEX-EM框架（启用经验记忆）与无记忆的基线模型。

**对比方法与主要结果**：
1.  **KGQAGen-10k**：APEX-EM取得了89.6%的准确率，相比无记忆基线（41.3%）提升了48.3个百分点（pp），甚至超过了Oracle检索（人工选择最佳经验）的上限（84.9%）。
2.  **BigCodeBench**：APEX-EM的成功率（SR）达到83.3%，相比基线（53.9%）提升了29.4pp。在可比条件下（冻结主干），其增益超过了MemRL方法（+11.0pp）。
3.  **Humanity's Last Exam (HLE)**：在实体图检索任务上，APEX-EM的准确率从基线的25.2%提升至48.0%（+22.8pp）。

**消融实验**：
消融研究表明不同组件的价值具有任务依赖性。例如，丰富的评判反馈（rich judge feedback）对于代码生成任务影响甚微，但对于结构化查询任务至关重要（能带来+10.3pp的增益）；而二元信号迭代（binary-signal iteration）可以在反馈较弱时部分补偿性能。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心创新在于通过结构化经验回放实现非参数在线学习，但仍存在一些局限性和值得探索的方向。

**局限性及未来研究方向：**
1.  **经验记忆的规模与效率**：论文未深入探讨经验记忆（PKG）无限增长带来的检索效率与存储开销问题。随着节点和边数量指数级增长，混合检索（语义、结构、图遍历）的延迟可能成为瓶颈。未来可研究高效的知识压缩、剪枝或分层索引机制。
2.  **跨领域泛化的深度与可解释性**：虽然通过“结构签名”实现了跨领域迁移，但“操作”节点的抽象程度和领域适配器的设计可能限制了其在更复杂、差异更大领域间的泛化能力。未来需要更普适、可学习的结构模式提取方法，并增强迁移过程的可解释性。
3.  **对失败经验的利用深度**：论文将失败经验作为负面示例，但其“错误注册表”和“补丁反射”的生成依赖教师模型的反馈质量。未来可探索更自动化的根本原因分析和补丁生成，例如通过强化学习或因果推理来优化修复策略。
4.  **动态环境适应的局限性**：虽然实体节点版本化能处理事实变化，但若任务本身的“目标”或“约束”范式发生根本性演变（而非实体属性更新），现有经验结构可能无法有效适应。需要研究经验结构的在线演化和重组能力。

**可能的改进思路：**
1.  **引入参数化微调与记忆的协同**：可探索“轻量级参数化适配器”与PKG的结合。例如，用少量参数对基础模型进行微调，使其更擅长从PKG中检索和应用特定类型的结构化经验，形成参数与非参数学习的优势互补。
2.  **发展更智能的经验合成与抽象机制**：当前经验存储具体执行轨迹。未来可设计机制，自动将多个具体经验合成更高阶的“策略模板”或“抽象规划模式”，从而提升记忆的概括性和检索的指向性。
3.  **探索多智能体间的经验共享与融合**：本文聚焦单个智能体的在线学习。一个自然的延伸是研究在多个智能体构成的系统中，如何安全、高效地共享和融合各自PKG中的结构化经验，实现集体经验的快速积累和冲突消解。

### Q6: 总结一下论文的主要内容

本文针对基于LLM的自主智能体缺乏持久性程序记忆、无法复用历史经验的问题，提出了APEX-EM框架，旨在实现不依赖模型参数更新的非参数化在线学习。其核心贡献在于：首先，设计了结构化经验表示（Procedural Knowledge Graph），完整编码任务执行的程序-情景轨迹，包括规划步骤、生成产物、迭代历史、错误分析和质量评分，并提取抽象操作序列作为结构签名。其次，提出了PRGII工作流（规划-检索-生成-迭代-吸收），通过任务验证器提供多维奖励信号，形成非参数化学习循环。最后，构建了双结果经验记忆库，结合语义搜索、结构签名匹配和计划图遍历的混合检索机制，使成功经验作为正面示例，失败经验作为带标注的负面示例，从而支持跨领域（表面描述不同但操作结构类似）的程序迁移。实验表明，在KGQAGen-10k、BigCodeBench和HLE等基准上，APEX-EM相比无记忆基线取得了显著提升，特别是在结构相似但词汇不重叠的任务上，其基于结构签名的检索机制超越了仅依赖语义相似性的现有方法（如MemRL），验证了结构化程序记忆对智能体经验复用与迁移的有效性。
