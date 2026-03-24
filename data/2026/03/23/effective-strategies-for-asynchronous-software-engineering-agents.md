---
title: "Effective Strategies for Asynchronous Software Engineering Agents"
authors:
  - "Jiayi Geng"
  - "Graham Neubig"
date: "2026-03-23"
arxiv_id: "2603.21489"
arxiv_url: "https://arxiv.org/abs/2603.21489"
pdf_url: "https://arxiv.org/pdf/2603.21489v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体协作"
  - "软件工程智能体"
  - "异步执行"
  - "任务规划"
  - "协调机制"
  - "代码生成"
  - "基准评估"
relevance_score: 9.0
---

# Effective Strategies for Asynchronous Software Engineering Agents

## 原始摘要

AI agents have become increasingly capable at isolated software engineering (SWE) tasks such as resolving issues on Github. Yet long-horizon tasks involving multiple interdependent subtasks still pose challenges both with respect to accuracy, and with respect to timely completion. A natural approach to solving these long-horizon tasks in a timely manner is asynchronous multi-agent collaboration, where multiple agents work on different parts of the task at the same time. But effective application of multi-agent systems has proven surprisingly difficult: concurrent edits by multiple agents interfere with each other, dependencies are difficult to synchronize, and combining partial progress into a coherent whole is challenging. On the other hand, human developers have long relied on mature collaboration infrastructure to manage these challenges in large software projects. Inspired by these collaboration primitives, we introduce Centralized Asynchronous Isolated Delegation (CAID), a structured multi-agent coordination paradigm grounded in three core SWE primitives: centralized task delegation, asynchronous execution, and isolated workspaces. CAID constructs dependency-aware task plans through a central manager, executes subtasks concurrently in isolated workspaces, and consolidates progress via structured integration with executable test-based verification. In empirical evaluation, we find that CAID improves accuracy over single-agent baselines by 26.7% absolute on paper reproduction tasks (PaperBench) and 14.3% on Python library development tasks (Commit0). Through systematic analysis, we find that branch-and-merge is a central coordination mechanism for multi-agent collaboration, and that SWE primitives such as git worktree, git commit, and git merge enable it to be realized in a reliable and executable manner.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决异步多智能体在软件工程长周期任务中的协作难题。随着基于大语言模型的软件工程智能体能力的提升，研究者期望它们能够完成更复杂的任务，如从零构建大型应用或复现整篇研究论文。然而，现有方法在处理涉及多个相互依赖子任务的长期任务时，面临准确性低和完成耗时长两大挑战。虽然已有研究探索了多智能体协调，例如基于角色的流水线、分层任务分解与委派、集成验证机制以及自动化通信拓扑搜索，但这些方法主要关注任务如何分解和分配，并未有效解决智能体在共享工件上进行异步协作的核心问题。

现有方法的不足在于，当多个智能体并发修改共享资源时，它们的编辑会相互干扰，导致集成失败。例如，一个智能体的更改可能破坏另一个智能体所依赖的假设，即使每个智能体独立工作产出正确，集成时也可能因状态视图不一致而产生冲突。这些冲突往往在集成时才被发现，修复成本高昂。相比之下，人类软件开发团队通过成熟的协作基础设施（如版本控制）来管理此类挑战，但现有多智能体系统缺乏类似机制。

因此，本文的核心问题是：如何有效协调多个智能体，使其能够异步协作完成共享工件的长周期软件工程任务？论文提出了一种基于软件工程原语的结构化多智能体协调范式，通过集中式任务委派、异步执行和隔离工作空间等机制，旨在减少编辑冲突、管理依赖关系，并确保部分进展能可靠整合为完整成果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**多智能体系统架构**、**软件工程中的协调机制**，以及**针对共享工件的并发控制**。

在**多智能体系统架构**方面，早期工作如CAMEL、Generative Agents和ChatDev建立了基于自然语言通信的交互基础。后续研究如EvoMAC、AutoAgents、AgentOrchestra、MASS和DyLAN等，致力于提升系统的灵活性、自适应任务分解和标准化协议。然而，这些架构在长视野任务中仍面临通信密度高、认知过载以及执行冲突等问题。本文提出的CAID范式与这些工作的核心区别在于，它**不依赖纯粹的语言驱动协调**，而是引入了一种**基于物理隔离和集中管理的执行感知范式**，以直接解决并发修改导致的冲突。

在**软件工程协调机制**的应用方面，已有工作如MetaGPT、AgileCoder借鉴了角色分解和生命周期管理等敏捷开发思想，SWE-agent等系统引入了类似持续集成的构建-测试循环。本文与这些工作的关系是**直接且系统性地借鉴了成熟的软件工程协作原语**（如分支、合并、隔离工作区），并将其**显式化、结构化**地整合到多智能体协调架构中，而不仅仅是隐式采用部分概念。

在**并发控制**方面，先前研究指出了多智能体在共享工件（如代码库）环境中面临的“协调税”、任务重叠和集成不一致等瓶颈。本文直接针对这一被忽视的瓶颈，通过**集中式任务委托、异步执行和隔离工作区**这三个核心原语，提供了一种可执行的、可靠的协调机制，从而在物理层面预防了干扰，确保了集成的一致性。

### Q3: 论文如何解决这个问题？

论文通过提出并实现名为“集中式异步隔离委托”（CAID）的结构化多智能体协调范式来解决长周期软件工程任务中多智能体协作的难题。其核心方法是借鉴人类软件开发中成熟的协作基础设施（特别是Git版本控制系统的基本操作），将多智能体协作过程形式化为一个以“分支与合并”为中心的协调架构。

整体框架围绕一个中央管理器展开，该管理器负责全过程的协调。主要模块与工作流程包括：1) **任务规划与依赖建模**：管理器首先分析代码库结构，构建一个有向依赖图，其中节点代表工作单元，边代表依赖关系。只有所有前置依赖都已满足的节点才被标记为“就绪”，可供委托。2) **依赖感知的任务委托**：管理器将总体任务分解为若干主要任务组，优先分配那些能更早启动测试、暴露更多评估信号或位于依赖链上游的任务。文件间若存在强依赖或循环依赖，则被分组并分配给同一工程师智能体以减少跨智能体协调开销。3) **工作区隔离与异步执行**：每个工程师智能体被分配一个独立的`git worktree`（工作树），确保其修改在隔离的沙箱中进行，互不干扰。执行过程由一个异步事件循环管理，多个工程师作为独立协程并发运行。4) **结构化通信与集成**：管理器与工程师之间通过结构化的JSON协议进行通信，明确任务边界与输出格式。工程师完成实现后，需先在其工作区内进行自我验证（如运行相关测试），通过后提交`git commit`。管理器随后尝试将其分支`git merge`到主分支。若发生合并冲突，则由提交该提交的工程师负责解决（通过拉取最新主分支、本地解决冲突并重新提交）。5) **进度整合与终止控制**：管理器在每次成功集成后更新依赖状态和已完成任务集，并动态分配新的就绪任务。管理器使用总结技术压缩执行历史以控制上下文长度。当依赖图中所有单元均已完成集成，或达到预设的轮次/预算限制时，过程终止。

关键技术及创新点在于：**系统性地将具体的软件工程原语映射为可靠的多智能体协调机制**。例如，用`git worktree`实现工作区隔离，用`git commit/pull request`实现结构化进度信号，用`git merge`实现输出集成，用依赖图确定调度约束。这种映射使得异步协作中的核心挑战——如并发编辑冲突、依赖同步和部分成果整合——能够通过可靠、可执行的标准操作来管理。此外，**强调工程师智能体的自我验证**（基于测试）作为提交前提，以及**管理器主导的、基于依赖状态的动态任务调度**，共同确保了任务推进的准确性和效率。最终，该架构使得多智能体能够像人类开发团队一样，在隔离环境中并行工作，并通过版本控制流程有序地整合成果，从而显著提升了长周期复杂任务的完成准确率。

### Q4: 论文做了哪些实验？

论文在两个长周期软件工程基准上进行了实验：Commit0-Lite 和 PaperBench。Commit0-Lite 要求从零开始实现一个 Python 库并通过所有单元测试，PaperBench 则要求复现一篇已发表会议论文的主要贡献，涉及多步骤实现、实验设置和结果验证。

实验设置方面，CAID 方法基于 OpenHands agent SDK (v1.11.0) 实现，包含一个负责依赖感知任务委派的中央管理器，以及多个在隔离工作空间中运行的软件工程师智能体。评估使用了三种语言模型：GLM 4.7、MiniMax 2.5 和 Claude-4.5-Sonnet。单智能体基线设置为 max_iterations=100，多智能体运行中，中央管理器为 50 次，每个工程师智能体为 80 次。主要结果中，PaperBench 使用 1 个管理器和 2 个工程师智能体，Commit0-Lite 使用 1 个管理器和 4 个工程师智能体。

主要对比方法是基于相同 OpenHands 框架构建的匹配单智能体系统，以隔离分支与合并协调机制的影响。此外，还测试了“单智能体+多智能体”的先后序贯策略。

主要结果与关键数据指标如下：在 PaperBench 上，CAID 相比单智能体基线显著提升了准确率。例如，使用 MiniMax 2.5 模型时，单智能体得分仅为 10.4%，而 CAID（2 工程师）达到 36.7%，绝对提升 26.3 个百分点；使用 Claude 4.5 时，从 57.2% 提升至 63.3%。在 Commit0-Lite 上，Claude 4.5 模型从 53.1% 提升至 59.1%，MiniMax 2.5 从 42.3% 提升至 57.0%。论文指出，性能提升源于执行方法的改变，而非底层模型的更换。实验还表明，简单地增加单智能体的迭代预算（从 100 次到 200 次）带来的改进非常有限甚至为负，而 CAID 带来的增益则大得多。此外，“单智能体+多智能体”的序贯策略虽然最终性能接近直接多智能体结果，但运行时间和成本几乎成倍增加，效率低下。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来可探索的方向包括：首先，提升中央管理器的智能任务分解与依赖识别能力。论文指出管理器的委派能力是关键瓶颈，尤其在任务结构不明确时（如PaperBench）。未来可研究如何结合代码库分析、动态依赖图学习等技术，使管理器能更精准地识别关键模块和高影响力任务，避免无效并行。其次，优化并行度与协调机制的动态适配。实验表明代理数量并非越多越好，需匹配任务内在模块性和管理器协调能力。可探索自适应机制，根据任务进展实时调整并行代理数量或协调策略（如切换严格审查与效率优先模式），以平衡效率与稳定性。再者，扩展隔离与协作机制。当前工作树隔离虽有效，但可能引入较高开销。可研究轻量级虚拟化或更细粒度的代码版本管理原语，以降低隔离成本，同时探索更灵活的冲突检测与合并策略，减少集成负担。最后，验证与测试的自动化增强。论文提到测试验证是整合进度的关键，但未深入探讨测试生成与修复。未来可集成自动化测试生成、模糊测试等工具，提升多代理协作中持续验证的可靠性和效率。

### Q6: 总结一下论文的主要内容

该论文针对异步软件工程代理在长周期、多子任务协作中的挑战，提出了一种名为“集中式异步隔离委托”（CAID）的多智能体协调范式。核心问题是多代理并发编辑时易产生冲突、依赖难以同步，以及部分进展难以整合。受人类开发者成熟协作基础设施启发，CAID基于三个核心软件工程原语构建：集中式任务委托、异步执行和隔离工作空间。方法上，通过中央管理器构建依赖感知的任务计划，在隔离工作空间中并发执行子任务，并通过基于可执行测试验证的结构化集成来整合进展。实验表明，CAID在论文复现任务（PaperBench）上比单代理基线绝对准确率提升26.7%，在Python库开发任务（Commit0）上提升14.3%。主要结论是，分支与合并是多代理协作的核心协调机制，而如git worktree、commit和merge等软件工程原语能使其以可靠、可执行的方式实现，从而显著提升长周期软件工程任务的准确性与完成效率。
