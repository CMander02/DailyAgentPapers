---
title: "SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution"
authors:
  - "Kang He"
  - "Kaushik Roy"
date: "2026-03-01"
arxiv_id: "2603.01327"
arxiv_url: "https://arxiv.org/abs/2603.01327"
pdf_url: "https://arxiv.org/pdf/2603.01327v1"
categories:
  - "cs.SE"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Code & Software Engineering"
  - "Tool Use & API Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "SWE-Adept (two-agent framework with agent-directed depth-first search, adaptive planning, structured problem solving, and shared working memory with Git-based tools)"
  primary_benchmark: "SWE-Bench Lite, SWE-Bench Pro"
---

# SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution

## 原始摘要

Large language models (LLMs) exhibit strong performance on self-contained programming tasks. However, they still struggle with repository-level software engineering (SWE), which demands (1) deep codebase navigation with effective context management for accurate localization, and (2) systematic approaches for iterative, test-driven code modification to resolve issues. To address these challenges, we propose SWE-Adept, an LLM-based two-agent framework where a localization agent identifies issue-relevant code locations and a resolution agent implements the corresponding fixes. For issue localization, we introduce agent-directed depth-first search that selectively traverses code dependencies. This minimizes issue-irrelevant content in the agent's context window and improves localization accuracy. For issue resolution, we employ adaptive planning and structured problem solving. We equip the agent with specialized tools for progress tracking and Git-based version control. These tools interface with a shared working memory that stores code-state checkpoints indexed by execution steps, facilitating precise checkpoint retrieval. This design enables reliable agent-driven version-control operations for systematic issue resolution, including branching to explore alternative solutions and reverting failed edits. Experiments on SWE-Bench Lite and SWE-Bench Pro demonstrate that SWE-Adept consistently outperforms prior approaches in both issue localization and resolution, improving the end-to-end resolve rate by up to 4.7%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在处理仓库级软件工程（SWE）任务时面临的核心挑战。研究背景是，尽管LLM在独立的编程任务上表现出色，但在处理真实世界的软件问题时仍存在显著不足。现有方法主要存在两大缺陷：一是在代码库导航和问题定位方面，现有方法往往采用粗粒度索引或算法控制的遍历（如固定跳数的广度优先搜索），导致搜索路径冗余，并将大量与问题无关的代码内容注入代理的上下文窗口，不仅浪费有限的上下文长度，也降低了定位的准确性。二是在问题修复方面，现有方法（如SWE-agent）通常缺乏系统性的解决策略，多采用自由形式的“思考-编辑”循环，缺乏明确的规划、进度跟踪和检查点机制。这使得迭代过程中的代码状态难以管理和验证，代理在编辑失败后难以可靠地回退到先前状态，也无法有效地探索替代解决方案。

因此，本文要解决的核心问题是：如何构建一个能够端到端自主解决仓库级软件问题的智能体框架，该框架需要同时实现**高效的、依赖感知的深度代码库导航与精准问题定位**，以及**系统的、支持迭代测试和版本控制的结构化问题修复**。具体而言，论文提出了SWE-Adept框架，通过一个定位代理和一个修复代理的分工协作，并引入基于代理引导的深度优先搜索、两阶段过滤、自适应规划、以及结合工具与共享工作内存的检查点机制等创新设计，来应对上述挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于LLM的代码库分析与问题解决框架，可分为方法类和应用类。

在方法类研究中，针对问题定位，现有工作包括基于代理的代码库导航方法（如SWE-agent、OpenHands）和图依赖引导方法（如LocAgent、RepoGraph），它们通过工具辅助或多步探索实现定位，但难以平衡搜索深度与上下文管理。本文提出的**定向深度优先搜索**通过选择性遍历依赖关系，减少了无关内容检索，提升了定位精度。针对问题解决，现有方法如Agentless、SWE-agent和AutoCodeRover采用生成-验证或迭代测试的范式，但多依赖自由形式的“思考-执行”模式，可能导致编辑轨迹混乱。本文引入**自适应规划与结构化问题解决**，结合专门工具（如进度跟踪、Git版本控制）和共享工作内存，支持系统化的代码修改与版本回退。

在应用类研究中，部分系统如SWE-Search和Claude Code支持计划执行和代码状态检查点，但其检查点由系统运行时管理或主要用于用户控制，代理无法自主利用。本文设计使代理能**自主利用检查点进行版本控制**，实现长视野的系统性问题解决。此外，内存设计相关工作（如HiAgent、MemoryOS、A-MEM）侧重于经验复用与反思，而本文从正交视角出发，利用工作内存存储代码状态检查点，以支持可靠的代理驱动版本控制操作。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SWE-Adept的双智能体框架来解决仓库级软件工程问题，其核心是分离关注点：一个负责定位问题代码，另一个负责实施修复。整体框架首先对代码库进行细粒度的定义级索引，并构建轻量级的代码结构树以表示单元间的依赖关系，这为后续的导航提供了高效的数据基础。

在问题定位阶段，**定位智能体**采用**智能体引导的深度优先搜索**策略。它从问题描述中提取初始关键词，利用一套搜索工具（支持文件级、定义级和内容级检索）进行探索。关键创新在于其选择性遍历：智能体根据工具返回的代码骨架和子单元标识符，每次优先选择一个最可能相关的子单元进行深度递归探索，而非广度遍历整个图。这种策略最小化了上下文中的无关内容。探索完成后，智能体进行两阶段过滤：先利用轻量级启发式信息（如代码骨架、位置元数据）初筛候选位置，再仅为这些候选位置加载完整源代码进行深入分析和重排序，从而提高了定位精度并减少了冗余检索。

在问题解决阶段，**解决智能体**在SWE-agent基础上构建，引入了两个关键的**工具家族**并与**共享工作内存**协同工作。`hypothesis_plan`工具用于管理多个假设（即备选解决方案）及其对应的待办事项列表，并跟踪执行状态和反馈见解。`hypothesis_git`工具则将复杂的Git版本控制操作（如分支、提交）封装成高级别、具有错误处理的单一命令，降低了智能体直接操作Git的出错率。这些工具通过语义标识符（如假设名、待办项名）与共享工作内存交互，工作内存存储了假设、待办步骤与代码状态检查点（Git哈希值和提交信息）的关联关系，使得智能体无需在上下文中记忆非语义的Git哈希值，实现了可靠的代码状态管理。

解决智能体的操作流程体现了**自适应规划和结构化问题解决**。它从确认问题开始，进行假设驱动的修复。对于复杂问题，会制定并评估多个竞争性假设。每个假设在一个独立分支上探索，并细化为具体的编辑和测试待办计划。计划是自适应的，可根据测试反馈动态添加新步骤。关键创新是**基于语义步骤的检查点索引**：每完成一个待办步骤，智能体就调用`hypothesis_git`提交当前状态，并将该检查点与完成的步骤在内存中关联。当某个假设部分失败时，智能体可以精准地回退到特定步骤对应的检查点，然后在新分支上继续探索，从而系统性地分离和管理不同的解决方案轨迹。最后，智能体比较所有假设的结果，选择最佳方案合并提交。

### Q4: 论文做了哪些实验？

论文在SWE-Bench Lite和SWE-Bench Pro两个真实世界的代码库级别软件工程基准测试上进行了实验。实验设置采用双智能体框架（定位智能体与解决智能体），并对比了多种基线方法：在问题定位任务中，对比了基于嵌入检索的CodeSage-Large和CodeRankEmbed，以及基于LLM的智能体方法SWE-agent、RepoGraph、LocAgent和OrcaLoca；在端到端问题解决任务中，对比了SWE-agent、RepoGraph和OrcaLoca。主要评估指标包括：问题定位的文件级Acc@3和函数级Acc@5，以及端到端问题解决的解决率（Resolve Rate）。关键数据指标显示，SWE-Adept在定位任务上显著领先，例如在SWE-Bench Lite上使用Claude-4.5时，文件级Acc@3达97.0%，函数级Acc@5达87.6%；在解决任务上，其在SWE-Bench Pro上使用GPT-5.2和Claude-4.5的解决率分别为40.7%和47.3%，较最强基线分别提升4.7%和4.0%。此外，该框架因有效的上下文管理，通常比基于图的方法消耗更少的令牌数。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性与内容，未来研究可从以下方向深入探索：首先，模型依赖方面，当前框架基于闭源LLM（如GPT/Claude），成本较高且可控性有限；未来可尝试将框架迁移至开源模型（如CodeLlama），并通过智能体强化学习优化其代码理解与工具调用能力，以平衡性能与部署成本。其次，语言泛化性上，实验仅针对Python代码库，虽框架设计为语言无关，但实际扩展需适配不同语言的解析与索引机制，例如针对JavaScript或Java的依赖分析工具，以验证跨语言通用性。此外，方法论层面可进一步优化：局部化搜索策略可结合广度优先或混合遍历，以处理复杂依赖场景；问题解决模块可引入更多自动化测试生成或协同调试工具，提升迭代修复的鲁棒性。最后，评估体系可扩展至更复杂场景（如多模块微服务），并探索智能体在长期代码维护中的自主学习机制。

### Q6: 总结一下论文的主要内容

该论文提出了SWE-Adept，一个基于大语言模型的双智能体框架，旨在解决仓库级软件工程任务中代码库深度导航与系统化问题修复的挑战。核心贡献在于将问题分解为定位与修复两个专门阶段，并设计了创新的方法支撑。在问题定位方面，框架引入了智能体引导的深度优先搜索与两阶段过滤机制，通过选择性遍历代码依赖来管理上下文窗口，减少无关信息，从而提升定位准确性。在问题修复方面，采用了自适应规划与结构化问题解决策略，通过代码状态检查点工具和共享工作内存接口，实现了可靠的智能体驱动版本控制操作，支持分支探索与回滚失败编辑。实验表明，SWE-Adept在SWE-Bench基准测试中显著优于现有方法，端到端问题解决率最高提升4.7%，证明了其在自动化软件工程中高效处理复杂代码库问题的能力。
