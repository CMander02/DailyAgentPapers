---
title: "Beyond Prompt-Based Planning: MCP-Native Graph Planning-based Biomedical Agent System"
authors:
  - "Zhangtianyi Chen"
  - "Florensia Widjaja"
  - "Wufei Dai"
  - "Xiangjun Zhang"
  - "Yuhao Shen"
  - "Juexiao Zhou"
date: "2026-06-03"
arxiv_id: "2606.04494"
arxiv_url: "https://arxiv.org/abs/2606.04494"
pdf_url: "https://arxiv.org/pdf/2606.04494v1"
categories:
  - "cs.AI"
tags:
  - "LLM驱动的智能体"
  - "生物医学智能体"
  - "MCP协议"
  - "图规划"
  - "工具使用"
  - "上下文压缩"
  - "智能体规划"
  - "多工具协作"
relevance_score: 8.5
---

# Beyond Prompt-Based Planning: MCP-Native Graph Planning-based Biomedical Agent System

## 原始摘要

Biomedical agents promise to automate complex biological workflows, yet current systems face two fundamental bottlenecks: bioinformatics tools are highly heterogeneous in interfaces and execution environments, while agent planning still relies on flat prompt-retrieved tool descriptions. As biomedical software ecosystems grow, this coupling between tool coverage and context size leads to tool confusion, unstable planning, and inefficient execution. We introduce BioManus, an MCP-native biomedical agent built on graph-scaffolded planning over structured biological capabilities. BioManus first introduces the BioinfoMCP Compiler, which converts heterogeneous bioinformatics software into standardized MCP servers, yielding a large executable MCP ecosystem. It then organizes this ecosystem as a typed heterogeneous MCP graph over tools, operations, datatypes, and workflow stages. At inference time, BioManus retrieves compact task-specific subgraphs, synthesizes operation-level workflow scaffolds. This design decouples planning complexity from raw tool inventory size, achieving a context compression ratio of Theta(N / (h * m_bar)) under high-recall retrieval, where N is the total tool count, h is the workflow horizon, and m_bar (much smaller than N) is the average number of candidate tools per operation. Experiments on BioAgentBench and LAB-Bench show that BioManus improves execution accuracy, workflow validity, and context efficiency over advanced biomedical agent baselines. This work suggests a paradigm shift: scalable biomedical reasoning requires structured executable capability graphs rather than increasingly larger prompt-level tool retrieval.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决生物医学智能体系统在面对大规模、异质性工具生态时所面临的核心瓶颈问题。当前，生物医学领域的软件工具在接口和运行环境上高度异构，而现有智能体的规划大多依赖基于提示的平面工具检索。这种方法将工具描述直接注入LLM的上下文，导致规划复杂度与检索工具数量线性相关（上下文呈O(kℓ_t)规模增长）。随着生物医学软件生态系统持续扩张，为了保持高召回率而不得不检索更多工具，从而引发上下文稀释、工具混淆和规划不稳定等问题。此外，现有系统还面临工具执行碎片化的挑战，需要处理跨语言、跨环境的依赖兼容性问题。本文的核心诊断是，问题不在于检索本身，而在于表征：生物医学工具并非存在于扁平的语义空间中，它们具有类型化的输入/输出、执行依赖和隐式工作流结构。因此，论文引入BioManus，提出一种基于图的规划新范式，通过构建结构化的、可执行的能力图来解耦规划复杂度与原始工具清单规模，将规划上下文压缩至Θ(N/(h·m̄))，从而实现可扩展且稳定的生物医学推理。

### Q2: 有哪些相关研究？

相关研究可从两个类别来梳理。首先是**方法类工作**，主要包括GeneAgent、CellAgent、SpatialAgent和Biomni等基于基础模型的生物医学代理系统。这些系统通过集成生物数据库和分析软件，实现了端到端的生物信息学工作流自动化。本文与它们的关键区别在于：BioManus不再依赖传统基于提示的扁平检索范式，而是采用图结构化的规划方式，从而避免了工具覆盖范围与上下文长度之间的耦合问题。其次是**系统类工作**，包括PromptBio、BioAgents、STELLA和PoSyMed等，它们侧重于可扩展、可复现的异构生物信息学生态系统编排。本文在这些工作的基础上进一步创新，通过BioinfoMCP编译器将异构工具标准化为MCP服务器，并构建类型化的异构MCP图来组织工具生态。这使得BioManus在推理时能够检索紧凑的任务特定子图并合成操作级工作流支架，实现了与原始工具库规模解耦的规划复杂度，在上下文压缩比和执行效率上显著优于现有基线系统。

### Q3: 论文如何解决这个问题？

BioManus 通过引入基于结构化能力图谱的 MCP 原生架构，有效解决了当前生物医药智能体面临的工具异构性高和基于提示词的规划可扩展性差两大问题。其核心方法包括四大组件：首先，**BioinfoMCP编译器**通过准备、执行和交付三阶段流水线，自动将异构的生物信息学软件（如手册、命令行界面等）转化为具有统一可调用接口的标准MCP服务器，并附带依赖和Docker封装，确保可移植性和可复现性。其次，所有生成的MCP服务器被组织成一个**异构图谱G=(V,E)**，包含工具、操作、数据类型、能力、工作流阶段和MCP服务器六类节点，以及实现、生产/消费、托管等工作流边缘关系。该图谱自动构建，通过LLM标注器推断输入/输出数据类型、语义操作分类和工作流阶段，工具被聚合到抽象操作节点，编码了生物可行的执行结构。在推理阶段，**图谱支架式规划**是关键创新：给定自然语言查询，系统首先将其转换为结构化任务规范，通过图RAG检索提取紧凑的任务特定子图（而非全局工具描述），LLM规划器基于此子图合成操作级执行路径P=(o_1,...,o_h)，每个操作只关联少量候选工具。最后，仅有选中的MCP服务器被动态注册执行。这一设计将规划复杂度与工具总数解耦，实现了上下文压缩比Θ(N/(h·m̄))，其中N为工具总数，h为工作流长度，m̄远小于N。通过在图结构上而非平铺文本上进行规划，BioManus显著提升了执行准确性、工作流有效性和上下文效率。

### Q4: 论文做了哪些实验？

论文在 BioAgentBench 和 LAB-Bench 两个基准上评估了 BioManus。BioAgentBench 包含 10 个真实生物信息学分析任务，使用 LLM 评分（0-1 连续尺度）和通过率（正确率>80%）进行评估；LAB-Bench 包含 DbQA、SeqQA 和 CloningScenarios 三个子任务，采用精确匹配准确率评估。对比方法包括通用工具使用代理（ReAct-Code）和生物医学基础代理（Biomni、Biomni-ReAct），以及基础 LLM（DeepSeek-V4）。为分析提示检索的可扩展性，还评估了工具库存从 100 到 2000 的多个 Biomni 变体。主要结果：在 BioAgentBench 上，BioManus 获得最高 LLM 评分（46.84%），与最佳 Biomni-2k（46.16%）相当，通过率并列最高（4/10）。在 LAB-Bench 上，BioManus 在 SeqQA（90.48%）和 CloningScenarios（81.82%）达到最优，超过 Biomani 的 84.76% 和 78.79%，在 DbQA（67.29%）也表现有竞争力。消融实验显示，单独加入 MCP 基础架构使 BioAgentBench 评分从 39.7% 提升至 42.7%，DbQA 从 57.5% 提升至 66.4%；进一步叠加图规划带来绝对增益 +7.2%、+9.8% 和 +5.7%。实验还表明，提示检索方法随工具库存增大导致上下文消耗增加且性能不稳定，而 BioManus 保持稳定且较低上下文消耗。

### Q5: 有什么可以进一步探索的点？

首先，论文依赖的文档质量参差不齐，未来可探索基于执行反馈的自动文档补全与编译器鲁棒性增强，例如通过模拟运行环境自动生成缺失的接口描述。其次，轻量语义标注限制了图谱的表达能力，可引入生物本体（如GO、UMLS）和已知工作流模式进行知识增强，实现更精准的节点类型推断与子图检索。第三，当前静态的图谱检索无法适应动态任务需求，可借鉴图神经网络或元学习，在推理时根据中间结果动态调整子图结构，形成迭代式规划。最后，虽然MCP解耦了工具数量，但多步骤操作的错误传播仍待解决，建议结合验证器或蒙特卡洛树搜索来评估候选子图路径的正确性，提升长链规划的稳定性。此外，专家监督的自动化折中、跨模态生物数据（如文本+图像）的MCP接口统一也是重要的扩展方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了BioManus，一个基于MCP原生架构的生物医学智能体系统，旨在解决当前生物医学软件工具异构性强、智能体规划依赖扁平提示检索导致的工具混淆、规划不稳定和执行效率低下等瓶颈问题。核心贡献包括：设计BioinfoMCP编译器，将异构生物信息学软件转化为标准化的MCP服务器，构建可执行的MCP生态系统；在此基础上，将工具、操作、数据类型和工作流程阶段组织为类型化异构图。推理时，BioManus检索紧凑的任务特定子图，合成操作级工作流骨架，从而将规划复杂度与原始工具数量解耦，实现上下文压缩比Θ(N/(h*m_bar))。在BioAgentBench和LAB-Bench上的实验表明，该方法在执行准确性、工作流有效性和上下文效率上显著优于现有基线。该工作的核心意义在于，提出从基于提示的扁平工具检索范式向结构化可执行能力图推理的转变，为生物医学领域乃至更广泛的科学智能体提供了可扩展的规划新范式。
