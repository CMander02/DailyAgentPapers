---
title: "Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents"
authors:
  - "Xing Zhang"
  - "Guanghui Wang"
  - "Yanwei Cui"
  - "Wei Qiu"
  - "Ziyuan Li"
  - "Bing Zhu"
  - "Peiyang He"
date: "2026-04-17"
arxiv_id: "2604.15877"
arxiv_url: "https://arxiv.org/abs/2604.15877"
pdf_url: "https://arxiv.org/pdf/2604.15877v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "Agent Memory"
  - "Agent Skill"
  - "Agent Framework"
  - "Experience Compression"
  - "Knowledge Reuse"
  - "Survey/Analysis"
  - "Agent Efficiency"
  - "Long-Horizon Agent"
relevance_score: 8.5
---

# Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents

## 原始摘要

As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck. Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a cross-community citation rate below 1%. We propose the \emph{Experience Compression Spectrum}, a unifying framework that positions memory, skills, and rules as points along a single axis of increasing compression (5--20$\times$ for episodic memory, 50--500$\times$ for procedural skills, 1,000$\times$+ for declarative rules), directly reducing context consumption, retrieval latency, and compute overhead. Mapping 20+ systems onto this spectrum reveals that every system operates at a fixed, predetermined compression level -- none supports adaptive cross-level compression, a gap we term the \emph{missing diagonal}. We further show that specialization alone is insufficient -- both communities independently solve shared sub-problems without exchanging solutions -- that evaluation methods are tightly coupled to compression levels, that transferability increases with compression at the cost of specificity, and that knowledge lifecycle management remains largely neglected. We articulate open problems and design principles for scalable, full-spectrum agent learning systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在长期、多会话部署中，因经验不断积累而导致的扩展性瓶颈问题。随着智能体从单次演示转向持久化运行，其产生的海量交互轨迹会迅速超出任何实际上下文窗口或检索预算的承受能力，使得高效的经验管理成为关键挑战。目前，两个主要研究社区——智能体记忆系统和智能体技能发现——都在尝试从交互轨迹中提取可重用知识以应对这一挑战，但彼此之间却存在显著隔阂。论文通过文献计量分析发现，这两个社区之间的交叉引用率低于1%，表明它们几乎在独立发展。

现有方法的不足在于，它们各自固守于特定的经验压缩层级：记忆系统专注于提取结构化的、相对具体的“事件记录”（压缩率约5-20倍），技能系统致力于提炼可复用的“行为模式”（压缩率约50-500倍），而规则系统则追求高度抽象的“决策原则”（压缩率1000倍以上）。尽管这些方法本质上都是在进行经验压缩，但当前所有系统都只在一个预设的、固定的压缩层级上运作，缺乏在不同压缩层级之间进行自适应转换和协同的能力。这种局限性被论文称为“缺失的对角线”问题。

因此，本文要解决的核心问题是：如何建立一个统一的理论框架，来弥合记忆、技能和规则研究社区之间的概念鸿沟，并设计出能够支持跨压缩层级自适应学习与知识管理的智能体系统。论文提出的“经验压缩谱系”框架，正是为了将这三者置于同一连续轴上，揭示其内在联系，并指出未来系统需要实现知识在不同压缩层级间的双向流动与自动化管理，以构建真正可扩展的、全谱系的智能体学习体系。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体经验管理，可分为记忆系统和技能发现两大类，但两者间存在显著的社区隔阂（交叉引用率低于1%）。具体如下：

**1. 方法类（按经验压缩层级划分）：**
*   **层级1（情景记忆）：** 包括Mem0、MemSkill、A-MEM/MemoryOS、Memory-R1/Mem-α、MemPO、ALMA、MemMA、SSGM等约十个系统。它们通过LLM驱动提取、强化学习优化、元学习架构等多种机制，将原始交互轨迹压缩为结构化的事件记录（如关键值对、事件摘要），压缩比约为5-20倍。
*   **层级2（程序性技能）：** 包括Voyager、CASCADE、Trace2Skill、SkillRL、EvoSkill、AutoSkill等八个系统。它们将多条轨迹提炼为可重用的行为模式（如代码片段、工作流模板），压缩比约为50-500倍，并在多项基准测试中证明其性能优于层级1的记忆检索。
*   **跨层级系统：** ExpeL和AutoAgent同时操作于层级1和层级2，但使用的是预定的固定层级，而非自适应选择。
*   **层级3（声明性规则）：** 目前极度缺乏。现有研究（如Constitutional AI）多使用预设规则，或通过人工设计奖励函数编码规则，尚无系统能自动从智能体经验中提取可审查、可编辑的声明性规则。RuleShaping等初步研究探讨了自然语言规则的影响，但自动化提取仍面临技术挑战。

**2. 评测类：**
现有评测方法与压缩层级紧密耦合。例如，SkillRL在ALFWorld上评估技能与记忆检索的差异，Trace2Skill在SpreadsheetBench上对比技能与人工编写技能的效果。研究表明，压缩层级本身不足以保证有效性，压缩过程的保真度至关重要（如SkillsBench发现LLM自生成的技能可能无益）。

**本文与相关工作的关系与区别：**
本文提出的“经验压缩谱系”是一个统一框架，将上述分散的研究（记忆、技能、规则）定位为同一压缩轴上不同抽象程度的点，揭示了它们本质上是解决同一核心挑战（从交互轨迹中提取可重用知识）的不同压缩层级。本文指出，现有系统均固定于单一或两个预定压缩层级，缺乏**自适应跨层级压缩**能力（即“缺失的对角线”），无法根据具体情境或证据积累动态选择、提升或降级知识表示。此外，本文强调两个社区独立解决了共享子问题而未交流方案，且知识生命周期管理普遍被忽视。因此，本文超越了现有孤立的方法，旨在为构建可扩展的全谱系智能体学习系统提供设计原则和开放问题。

### Q3: 论文如何解决这个问题？

论文通过提出“经验压缩谱”这一统一框架来解决LLM智能体在长期、多会话部署中高效管理累积经验的核心瓶颈问题。该框架将记忆、技能和规则视为同一压缩轴上不同抽象程度的点，并揭示了现有系统均固定于单一压缩层级，缺乏跨层级自适应压缩能力（即“缺失的对角线”）。

核心方法是将经验压缩形式化为一个四层谱系，并定义了经验压缩函数。整体架构基于从原始交互轨迹到高度抽象知识的渐进压缩过程：第0层是原始轨迹，无压缩；第1层是情景记忆，通过提取关键事件进行5-20倍压缩；第2层是程序性技能，抽象出可复用的行为模式，实现50-500倍压缩；第3层是陈述性规则，提炼领域不变的原则，压缩比达1000倍以上。每一层在通用性、信息保留和获取/维护成本间存在系统性的权衡。

关键技术贡献在于首次将分散的研究工作（分析了22篇主要论文的1136篇引用）统一到该谱系下，并系统映射了20多个现有系统，发现它们都聚集在L1或L2层级，且缺乏生命周期管理。创新点主要体现在三个方面：一是提出了量化压缩比与效用权衡的通用框架；二是指出了“缺失的对角线”这一关键研究缺口，即缺乏能自适应选择压缩层级、并在证据充足时进行知识向上压缩（如多个记忆合并为一个技能）或向下具体化的系统；三是揭示了压缩层级与评估方法的紧耦合关系，以及随着压缩程度提高，可转移性增强但特异性下降的规律。

论文进一步论证，单纯 specialization 不足，因为记忆系统和技能发现社区独立解决了共享子问题却缺乏交流。最终，该框架为设计可扩展的全谱系智能体学习系统提供了明确的设计原则和开放问题，强调需要通过元学习实现自适应层级选择，以应对知识存储和检索开销随经验线性增长的可扩展性瓶颈。

### Q4: 论文做了哪些实验？

论文通过构建“经验压缩谱”框架，对现有LLM智能体系统进行了系统性映射和分析，以揭示其设计模式与局限。实验设置上，作者从2023年以来发表的文献中筛选出20多个符合条件（从交互轨迹中学习、产生持久知识产物）的系统，并将其映射到压缩谱的四个层级（L0原始轨迹、L1情景记忆、L2程序性技能、L3声明性规则）上。

数据集/基准测试方面，实验引用了多个已发表研究中的基准来评估不同压缩层级的性能，包括ALFWorld、SpreadsheetBench、BrowseC.、SWE-bench以及一个多任务基准。这些基准用于对比不同压缩层级知识表示在下游任务中的有效性。

对比方法主要是在同一研究内部，比较更高压缩层级的表示与更低压缩层级基线（或无技能）的性能差异。例如，将L2技能与L1记忆检索对比，或将L2技能与人工编写技能对比。

主要结果与关键数据指标如下：
1.  **性能提升**：更高压缩层级的表示普遍带来性能增益。例如，在ALFWorld上，SkillRL的L2技能比L1轨迹检索性能绝对提升68.5个百分点（pp）；在SpreadsheetBench上，Trace2Skill的L2技能优于人工编写技能21.5 pp，优于无技能基线42.1 pp。
2.  **压缩有效性条件**：压缩过程的质量至关重要。SkillsBench的研究显示，精心策划的L2技能能带来16.2 pp的增益，而LLM自生成的技能则无增益（+0.0 pp）。
3.  **系统分布模式**：映射结果显示，现有系统高度聚集在固定层级：约10个系统集中在L1（如Mem0、MemPO），约8个系统集中在L2（如Voyager、Trace2Skill）。仅有ExpeL和AutoAgent同时支持L1和L2，但层级是预设而非自适应选择的。没有系统能自动化地从经验中提取L3规则。
4.  **关键发现**：论文揭示了“缺失对角线”问题，即缺乏能够根据给定轨迹自适应选择压缩层级、或在证据积累时进行知识向上压缩（如多个记忆合并为一个技能）、或在规则过于抽象时进行向下压缩的系统。这被认为是当前研究的一个核心局限。

### Q5: 有什么可以进一步探索的点？

基于论文提出的“经验压缩谱”框架，未来可进一步探索的核心方向包括：首先，开发能够自适应选择压缩级别的元控制器，根据经验轨迹的新颖性和频率动态决定将其压缩为记忆、技能或规则，这需要建立信息价值评估体系以权衡压缩成本与未来效用。其次，设计跨级别知识一致性维护机制，当同一行为在不同压缩级别（如具体记忆与抽象规则）共存时，系统需检测并解决语义冲突，这超越了传统数据库范式。第三，构建全生命周期治理系统，为知识工件引入版本控制、依赖追踪和废弃协议，实现“双向晋升/降级”——在低活跃期进行向上压缩，在规则失效时降级回具体证据收集。

此外，论文未充分探索的改进思路包括：将压缩机制扩展至多模态经验（如视觉观察），研究无奖励信号下的自监督压缩方法，以及探索跨领域技能迁移协议。当前系统多在摄入时同步压缩，未来可借鉴睡眠中的海马-新皮层巩固机制，实现异步压缩优化。这些方向有望填补“缺失的对角线”，构建真正自适应、可扩展的智能体学习系统。

### Q6: 总结一下论文的主要内容

该论文提出了“经验压缩谱”这一统一框架，旨在解决LLM智能体在长期、多会话部署中经验管理效率低下的问题。研究发现，现有的智能体记忆系统和技能发现方法虽目标相似，但社区间交流极少，存在重复解决共性问题的现象。

论文的核心贡献是将记忆、技能和规则统一视为同一压缩轴上不同压缩程度的体现：情景记忆压缩5-20倍，程序性技能压缩50-500倍，声明性规则压缩1000倍以上。通过将20多个系统映射到该谱系上，论文揭示了当前系统均固定于单一压缩层级，缺乏自适应跨层级压缩能力（即“缺失的对角线”问题）。此外，研究指出评估方法与压缩层级紧密耦合，可迁移性随压缩增加而提升但会牺牲特异性，且知识生命周期管理普遍被忽视。

论文的意义在于为构建可扩展的智能体学习系统提供了统一视角和设计原则，强调未来需开发能自适应选择压缩粒度的系统，以根据经验的价值和普适性进行高效管理，从而支撑智能体在长期部署中的规模化运行。
