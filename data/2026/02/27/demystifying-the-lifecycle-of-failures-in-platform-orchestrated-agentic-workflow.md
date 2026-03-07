---
title: "Demystifying the Lifecycle of Failures in Platform-Orchestrated Agentic Workflows"
authors:
  - "Xuyan Ma"
  - "Xiaofei Xie"
  - "Yawen Wang"
  - "Junjie Wang"
  - "Boyu Wu"
date: "2025-09-28"
arxiv_id: "2509.23735"
arxiv_url: "https://arxiv.org/abs/2509.23735"
pdf_url: "https://arxiv.org/pdf/2509.23735v2"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "N/A"
  primary_benchmark: "AgentFail"
---

# Demystifying the Lifecycle of Failures in Platform-Orchestrated Agentic Workflows

## 原始摘要

Agentic workflows built on low-code orchestration platforms enable rapid development of multi-agent systems, but they also introduce new and poorly understood failure modes that hinder reliability and maintainability. Unlike traditional software systems, failures in agentic workflows often propagate across heterogeneous nodes through natural-language interactions, tool invocations, and dynamic control logic, making failure attribution and repair particularly challenging. In this paper, we present an empirical study of platform-orchestrated agentic workflows from a failure lifecycle perspective, with the goal of characterizing failure manifestations, identifying underlying root causes, and examining corresponding repair strategies. We present AgentFail, a dataset of 307 real-world failure cases collected from two representative agentic workflow platforms. Based on this dataset, we analyze failure patterns, root causes, and repair difficulty for various failure root causes and nodes in the workflow. Our findings reveal key failure mechanisms in agentic workflows and provide actionable guidelines for reliable failure repair, and real-world agentic workflow design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决低代码编排平台构建的智能体工作流中，新型且难以理解的故障模式所导致的可靠性和可维护性问题。研究背景是，基于大语言模型的智能体系统因其在复杂任务中的协作优势而广泛应用，而低代码平台（如Dify、Coze）进一步降低了构建多智能体系统的门槛。然而，现有方法存在明显不足：一方面，已有研究（如FAMAS、AgenTracer）多采用基于优化的故障定位与修复方法，未能从根本上理解这类新型智能体系统内在的故障机制和修复策略；另一方面，现有的故障分类研究（如MASFT、AgentErrorTaxonomy）主要描述故障的表面表现形式（如“步骤重复”），而未深入探究其根本原因，更未提供具体的修复指导，导致开发者在实际修复时缺乏可操作的依据。因此，本文要解决的核心问题是：从故障生命周期的视角，系统性揭示平台编排的智能体工作流中故障的表现形式、根本原因和修复策略，以填补对故障机制整体理解的空白，并为实现可靠的故障修复提供实践指导。为此，研究构建了包含307个真实故障案例的AgentFail数据集，并基于此分析了故障模式、根因及修复难度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**LLM多智能体系统**和**智能体系统故障分析**。

在**LLM多智能体系统**方面，相关研究聚焦于开发和应用基于LLM的多智能体系统。例如，MetaGPT、ChatDev等系统将智能体组织成结构化角色，以协作完成软件工程任务；SWE-agent专注于通过与代码库和环境的交互进行自动化程序修复；Magentic-One和Captain Agent则致力于解决GAIA基准测试中的复杂任务。**本文研究的智能体工作流与这些系统密切相关，都属于多智能体系统的范畴。但关键区别在于，本文专注于基于低代码/无代码平台编排的工作流**。这类工作流通过可视化、模板驱动的配置方式构建，而非纯代码开发，这在工作流设计、调试和修复方面引入了独特的挑战，构成了一个独特的子类。

在**智能体系统故障分析**方面，随着系统复杂性增加，故障分析成为研究重点。相关研究包括：
1.  **故障定位与归因**：如Zhang等人的Who&When数据集研究智能体及步骤级的故障归因，Ge等人提出评估智能体责任的方法。
2.  **故障修复与优化**：如Aegis和Maestro等系统旨在通过自动化优化提高系统鲁棒性。
3.  **故障根因分析**：如Cemri等人提出的MAST分类法总结多智能体系统常见故障模式，Lu和Zhu等人分别从执行阶段和智能体能力角度分析故障。
**本文与这些工作的关系是承接并深化了故障分析这一研究方向。然而，现有研究多侧重于故障发生的位置或表现形式，对“为何发生”以及“如何修复”关注不足，许多故障类型停留在表面现象，未能转化为可操作的修复指导。本文的贡献在于弥补这一局限**，通过实证研究从故障生命周期的视角，强调根因层面的分析，并构建了一个连接故障表现与系统性修复策略的结构化分类体系，旨在提供更直接、可操作的修复指南。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的、以修复为导向的分析框架来解决平台编排的智能体工作流中的故障问题。其核心方法包括三个关键部分：故障归因、根因分类和修复策略。

首先，论文提出了一个自动化的**故障归因框架**。该框架分为两个阶段：1）**细粒度分析**：联合分析故障轨迹和工作流配置，通过检查智能体交互、控制流和中间输出来识别一组可疑的候选节点，从而缩小搜索范围。2）**根位置检测**：对候选节点进行基于“重执行”的反事实验证。具体而言，选择性地用修正后的输出（由“预言生成器”产生）替换候选节点的输出，同时保持其余执行不变，然后重新执行工作流。如果故障被解决，则最早被修正的节点被识别为故障根源。这种方法将故障归因从启发式检查转变为基于因果关系的原则性过程，将归因准确率从46.3%提升至65.8%。

其次，论文构建了一个结构化的、**以修复为导向的故障根因分类法**。该分类法分为三层：最左层按故障起源的系统抽象级别分类（智能体级、结构级、平台级）；中间层指定具体的故障根因（如知识/推理限制、提示设计不良、缺少输入验证等）；最右层总结对应的修复策略（如升级模型、改进提示、添加验证模块等）。这种分类法不仅描述了故障现象，更重要的是将每个根因类别映射到具体的、可操作的修复策略，为修复提供了直接指导。实验表明，在根因识别任务中，同时提供该分类法和故障位置信息，能将准确率从仅9.6%大幅提升至45.6%。

最后，论文设计并评估了一个**基于专家团队的修复框架**。该框架受传统程序修复领域方法启发，构建了一个由四名专业专家组成的修复团队，他们分阶段协作，利用故障轨迹、工作流配置以及（可选的）故障位置和根因信息来指导修复决策。实验结果表明，同时提供故障位置和根因信息能实现最有效和最安全的修复，修复成功率高达66.8%，且新故障引入率仅为2.8%。相比之下，缺乏这些关键信息时，修复成功率低（16.3%）且会引入大量新故障（13.9%）。

**整体创新点**在于：1）首次从故障生命周期的角度对平台编排的智能体工作流进行实证研究，并构建了真实故障数据集AgentFail；2）提出了结合细粒度分析和反事实验证的自动化故障归因方法，有效应对了故障在异构节点间长距离传播的挑战；3）创建了首个以修复为导向的故障根因分类法，将根因与具体修复行动直接关联；4）系统评估了故障归因和根因知识对自动化修复效果的显著提升作用，为构建更可靠的智能体系统提供了实践指南。

### Q4: 论文做了哪些实验？

本研究基于自建的AgentFail数据集（包含从两个代表性智能体工作流平台收集的307个真实故障案例），开展了一系列实验，旨在剖析故障生命周期。实验设置主要包括故障归因分析、故障根因识别与修复策略评估。

在**故障归因分析**中，研究者首先分析了故障根因节点的类型与位置分布。关键数据指标显示：LLM与智能体节点是主要故障源，占比超过50%；逻辑控制节点和知识节点次之。约32%的故障其根因节点与故障表现节点不同，其中超过10%的案例其错误传播距离超过了工作流总长的40%。研究者还设计了一个自动化故障归因框架（包含细粒度分析和基于重执行的根位置检测），实验表明，仅使用细粒度分析（w/o RLDetect）的归因准确率为46.3%，而结合重执行验证（with RLDetect）后，准确率提升至65.8%。

在**故障根因识别**实验中，研究者构建了一个面向修复的故障根因分类法，并评估了不同信息（故障定位LO、根因分类法TA）对大型语言模型识别根因的影响。实验结果显示：在既不提供故障位置也不提供分类法（w/o LO, w/o TA）时，识别准确率仅为9.6%；仅提供分类法（w/o LO, with TA）时，准确率升至27.4%；仅提供故障位置（with LO, w/o TA）时为22.8%；而当两者同时提供（with LO, with TA）时，识别准确率达到最高，为45.6%。

在**故障修复评估**中，研究者构建了一个由四位专家组成的修复团队，并比较了在不同指导信息下的修复效果。主要结果如下：当不提供故障位置和根因信息（w/o LO & w/o RC）时，修复成功率仅为16.3%，且会引入13.9%的新故障；仅提供故障位置（with LO & w/o RC）时，修复成功率提升至34.9%，新故障率降至8.4%；而当同时提供故障位置和根因信息（with LO & with RC）时，修复成功率最高，达到66.8%，新故障率最低，仅为2.8%。此外，分析还发现，智能体级别的故障相对容易修复，而涉及工作流编排的结构级故障修复成功率较低且需要更多迭代。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其数据集主要来源于两个特定平台，可能无法涵盖所有类型的Agentic工作流故障模式。未来研究可进一步探索以下方向：首先，开发更智能的故障诊断框架，结合因果推理技术来精确定位跨节点传播的故障根源，而不仅仅是依赖经验性分类。其次，论文提到修复代理存在能力瓶颈和认知局限，未来可设计具有元认知能力的多代理协作修复系统，使其能动态评估自身知识边界并主动寻求外部知识。此外，可探索将形式化验证方法引入低代码平台，在部署前对工作流逻辑进行静态分析，预防循环依赖等结构性故障。最后，论文未充分讨论故障修复的自动化评估指标，未来需要建立更细粒度的评估体系，量化修复策略在保真度、效率和资源消耗方面的权衡。

### Q6: 总结一下论文的主要内容

该论文针对低代码编排平台构建的智能体工作流中存在的、难以理解的故障模式进行了系统性研究。论文的核心贡献在于从故障生命周期的视角，首次对平台编排的智能体工作流进行了实证分析，旨在揭示故障表现、根本原因及修复策略。

研究首先定义了问题：与传统软件不同，智能体工作流的故障会通过自然语言交互、工具调用和动态控制逻辑在异构节点间传播，导致故障归因和修复异常困难。为此，论文构建了名为AgentFail的数据集，包含从两个代表性平台收集的307个真实故障案例。

方法上，基于该数据集，论文对工作流中不同故障根本原因和节点的故障模式、根源及修复难度进行了深入分析，并提出了一个面向修复的根本原因分类法，以弥合故障表现与可操作修复策略之间的差距。

主要结论包括：揭示了智能体工作流中关键的故障机制；为可靠的故障修复提供了可操作的指导；并为设计更健壮的智能体工作流提出了实用指南，如模块化提示设计、显式验证和渐进式设计流程。这项工作为开发更可靠的自动化故障归因与修复方法奠定了基础。
