---
title: "REVERE: Reflective Evolving Research Engineer for Scientific Workflows"
authors:
  - "Balaji Dinesh Gangireddi"
  - "Aniketh Garikaparthi"
  - "Manasi Patwardhan"
  - "Arman Cohan"
date: "2026-03-21"
arxiv_id: "2603.20667"
arxiv_url: "https://arxiv.org/abs/2603.20667"
pdf_url: "https://arxiv.org/pdf/2603.20667v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "持续学习"
  - "提示优化"
  - "代码智能体"
  - "科学工作流"
  - "记忆与反思"
  - "任务执行"
relevance_score: 7.5
---

# REVERE: Reflective Evolving Research Engineer for Scientific Workflows

## 原始摘要

Existing prompt-optimization techniques rely on local signals to update behavior, often neglecting broader and recurring patterns across tasks, leading to poor generalization; they further rely on full-prompt rewrites or unstructured merges, resulting in knowledge loss. These limitations are magnified in research-coding workflows, which involve heterogeneous repositories, underspecified environments, and weak feedback, where reproducing results from public codebases is an established evaluation regime. We introduce Reflective Evolving Research Engineer (REVERE), a framework that continuously learns from Global Training Context, recognizes recurring failure modes in cross-repository execution trajectories, distills them into reusable heuristics, and performs targeted edits across three configurable fields: the system prompt, a task-prompt template, and a cumulative cheatsheet. REVERE, via this reflective optimization framework, improves performance over prior state-of-the-art expert-crafted instructions on research coding tasks by 4.50% on SUPER, 3.51% on ResearchCodeBench, and 4.89% on ScienceAgentBench across their respective metrics. These results demonstrate that agents equipped with mechanisms for continual learning and global memory consolidation can meaningfully evolve their capabilities over time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在**研究代码复现**这类复杂、长周期任务中表现不佳的问题。研究背景是，尽管LLM在短期、定义明确的编码任务上取得了进展，但在处理研究代码库时，其可靠性会显著下降。这是因为研究代码工作流具有异构仓库、环境不明确、反馈弱且延迟、需要推断隐含假设以及跨框架积累过程性知识等独特挑战。

现有方法的不足主要体现在几个方面：首先，现有的提示优化或自优化技术（如自我精炼）通常依赖**局部评估信号**和启发式采样，容易过度拟合近期结果，而忽略了跨任务中更广泛、可复现的失败模式，导致泛化能力差。其次，许多系统依赖**静态提示**或固定策略，无法适应研究任务不断演变的惯例和开放特性。再者，即使一些方法尝试积累可重用策略，也因缺乏**持久的全局记忆**而限制了长期知识保留。此外，大多数提示适应框架通过**完全重写提示**来更新行为，这可能导致语义漂移和已有知识丢失，而结构化的编辑方法又往往实现复杂。

因此，本文要解决的核心问题是：如何设计一个能够**持续学习、积累并应用跨任务通用经验**的智能体框架，以克服上述不足，从而稳定提升在研究代码工作流中的性能。具体而言，论文提出了REVERE框架，其核心目标是让智能体能够从全局执行轨迹中识别反复出现的失败模式，将其提炼为可复用的启发式规则，并通过**有针对性的、非破坏性的结构化编辑**来更新系统提示、任务模板和累积备忘单等可配置字段，从而实现稳定、可泛化的能力进化，避免局部最优和知识遗忘。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：研究编码评测与方法、以及提示优化与自我进化技术。

在研究编码评测与方法方面，现有工作包括评估大语言模型在机器学习工程基准、端到端研究工作流及研究实验周期各项任务上的表现。近期基准如SUPER、ResearchCodeBench和ScienceAgentBench专门关注研究代码的复现性，揭示了尽管多智能体系统和基于搜索的方法有所进展，但性能差距依然存在。这些工作凸显了**对自反思系统的需求**，而非依赖人工设计的工作流。本文选取的这三个基准覆盖了互补的研究编码场景（长周期仓库执行、单次研究代码重建、交互式科学编程），为评估提供了多样化基础。本文与这些工作的关系是**直接在这些基准上进行评估和改进**，区别在于本文提出了一个能持续学习并整合全局记忆的框架来系统性提升性能。

在提示优化与自我进化技术方面，相关工作包括：将提示视为可调参数的传统优化方法（使用强化学习、无梯度或启发式搜索）；较新的方法如GEPA、MIPRO利用反思模型和进化策略来优化语言模型程序的提示；以及运行时自适应智能体动态修改其架构和工具。此外，一些方法探索严格的任务级适应，但改进往往难以跨任务迁移；而测试时上下文适应方法（如Dynamic Cheatsheet和ACE）通过生成和反思维护持久演化的“秘籍”。本文与这些工作的关系是**同属提示优化范畴**，但区别在于，现有方法通常在密集监督和短周期任务中进行评估，而本文针对的研究编码工作流具有**长周期、弱监督**的特点，且更新需紧密基于仓库结构、环境和执行轨迹，而非仅依赖高层自然语言反馈。因此，本文提出了一种专门适用于研究编码任务的新优化策略。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为REVERE的反思性优化框架来解决现有提示优化技术泛化能力差、知识易丢失的问题。其核心方法是构建一个持续学习的循环，通过分析跨任务的执行轨迹，识别反复出现的失败模式，并将其提炼为可复用的启发式知识，进而对控制智能体行为的三个可配置字段进行精准编辑。

整体框架是一个迭代的适应循环。主要模块包括：执行任务的智能体（Agent）和负责诊断与更新的反思器（Reflector）。流程上，智能体以批次（batch）为单位执行一系列任务，每个批次后，系统收集包含任务描述、得分和输出的“评估步骤上下文”（S），并将其与“全局训练上下文”一起提供给反思器。反思器基于这些信息，通过生成并执行Python代码，对三个关键字段进行外科手术式的编辑，而非重写整个提示。这三个字段构成了架构设计的核心：系统提示（F_s，定义全局行为规则）、任务提示模板（F_x，用于在运行时实例化任务特定指令）以及累积备忘单（F_c，一个从空开始、持续积累可复用策略和技巧的持久记忆）。编辑完成后，更新后的字段用于下一批次的任务，如此循环，使系统能力随时间不断演进。

关键技术在于其代码驱动的字段更新机制与全局训练上下文的设计。创新点主要体现在：1. **精准的代码化编辑**：反思器生成简短的Python程序来修改字段的特定部分，实现了高度靶向的更新，避免了全提示重写导致的语义漂移和知识丢失，同时保持了编辑的表达性和安全性。2. **三重全局信号整合**：系统通过“累积备忘单”（存储简洁的领域启发式知识，直接辅助任务执行）、“反思历史”（记录过往更新的摘要和原理，确保长期更新的一致性）和“辅助上下文”（包含未来或过往任务描述，促进泛化）这三个互补组件，使学习超越了当前批次的局部反馈，能够识别和应对跨任务的重复性模式。3. **一体化的反思器设计**：将失败诊断和字段编辑两个角色统一于单个反思器智能体，避免了多智能体管道中可能出现的意图误解和更新不连贯问题，保持了系统状态演进视图的一致性。

综上，REVERE通过一个集成了代码化精准编辑、结构化全局记忆与迭代反思循环的框架，实现了智能体在复杂科研编码工作流中的持续学习和能力进化。

### Q4: 论文做了哪些实验？

论文在三个研究编码基准测试上进行了实验：SUPER（长视野交互式）、ResearchCodeBench（单次生成）和ScienceAgentBench（交互式代码生成）。实验设置包括离线与在线两种适应机制。离线设置中，模型在固定的训练/验证任务上适应，并在未见过的测试集上评估；在线设置中，任务按顺序到达且无重复，模型需基于自身执行轨迹持续更新。对比方法包括基线（最小化提示）、静态SOTA（作者提供的最佳指令）、GEPA（基于遗传-帕累托的提示优化器）和ACE（基于策略清单的多代理学习方法）。主要结果如下：在离线适应中，REVERE在SUPER基准的Overall指标上相比静态SOTA提升4.50%（无监督时提升2.41%，有监督时提升4.50%），在ResearchCodeBench的Accuracy上提升1.3%，在ScienceAgentBench的Success Rate上提升4.89%。在线适应中，REVERE同样在所有基准上超越基线，例如在SUPER的Overall指标上提升8.10%。消融实验表明，移除全局训练上下文、累积备忘单等核心组件均会导致性能显著下降，验证了框架设计的必要性。效率分析显示，REVERE在保持提示长度受控增长的同时，其适应成本比ACE和GEPA低近10倍。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在两个方面：一是其基于提示的更新机制在领域知识密集、任务高度异构的场景下收益有限，这表明仅通过提示调整可能难以捕获高度专业化的知识，未来需要探索与更具体的任务适配形式（如微调模块或参数高效调整）相结合。二是其不断增长的全局训练上下文可能带来管理开销和信息冗余问题，影响长周期任务的效率。

未来研究方向包括：第一，开发更智能的上下文维护与剪枝策略，例如基于信息新鲜度、效用度量的动态筛选机制，以控制上下文膨胀并提升知识质量。第二，将REVERE框架与参数化适应方法（如LoRA）结合，形成混合适应系统，以更好地处理领域特异性强的问题。第三，探索更细粒度的失败模式分析与启发式提炼机制，例如引入因果推理来识别根本原因，从而生成更精准的编辑指令。此外，可考虑将框架扩展到非编码类科学工作流（如实验设计或论文写作），验证其通用性。

### Q6: 总结一下论文的主要内容

该论文提出了REVERE框架，旨在解决现有提示优化技术在科学编码工作流中泛化能力差和知识丢失的问题。核心问题是现有方法依赖局部信号更新，忽略了跨任务的全局重复模式，且采用全提示重写或非结构化合并会导致知识遗忘。

方法上，REVERE引入了一种反射式优化框架，它持续从全局训练上下文中学习，识别跨代码库执行轨迹中的重复失败模式，并将其提炼为可复用的启发式规则。框架通过针对性地编辑三个可配置部分来优化智能体：系统提示、任务提示模板和累积的速查表，从而实现知识的持续积累与精准应用。

主要结论显示，REVERE在多个科学编码基准测试上显著超越了现有最优的人工设计指令，在SUPER、ResearchCodeBench和ScienceAgentBench上分别提升了4.50%、3.51%和4.89%的性能。这证明了具备持续学习和全局记忆整合机制的智能体能够随时间有效进化其能力，对于提升AI在复杂研究环境中的适应性和可靠性具有重要意义。
