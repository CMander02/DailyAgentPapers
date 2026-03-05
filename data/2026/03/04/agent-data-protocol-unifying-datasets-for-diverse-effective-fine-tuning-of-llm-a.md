---
title: "Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents"
authors:
  - "Yueqi Song"
  - "Ketan Ramaneti"
  - "Zaid Sheikh"
  - "Ziru Chen"
  - "Boyu Gou"
  - "Tianbao Xie"
  - "Yiheng Xu"
  - "Danyang Zhang"
  - "Apurva Gandhi"
  - "Fan Yang"
  - "Joseph Liu"
  - "Tianyue Ou"
  - "Zhihao Yuan"
  - "Frank Xu"
  - "Shuyan Zhou"
  - "Xingyao Wang"
  - "Xiang Yue"
  - "Tao Yu"
  - "Huan Sun"
  - "Yu Su"
date: "2025-10-28"
arxiv_id: "2510.24702"
arxiv_url: "https://arxiv.org/abs/2510.24702"
pdf_url: "https://arxiv.org/pdf/2510.24702v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 数据合成"
  - "Agent 训练"
  - "监督微调"
  - "数据集标准化"
  - "工具使用"
  - "Agent 架构"
relevance_score: 9.0
---

# Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents

## 原始摘要

Public research results on large-scale supervised finetuning of AI agents remain relatively rare, since the collection of agent training data presents unique challenges. In this work, we argue that the bottleneck is not a lack of underlying data sources, but that a large variety of data is fragmented across heterogeneous formats, tools, and interfaces. To this end, we introduce the agent data protocol (ADP), a light-weight representation language that serves as an "interlingua" between agent datasets in diverse formats and unified agent training pipelines downstream. The design of ADP is expressive enough to capture a large variety of tasks, including API/tool use, browsing, coding, software engineering, and general agentic workflows, while remaining simple to parse and train on without engineering at a per-dataset level. In experiments, we unified a broad collection of 13 existing agent training datasets into ADP format, and converted the standardized ADP data into training-ready formats for multiple agent frameworks. We performed SFT on these data, and demonstrated an average performance gain of ~20% over corresponding base models, and delivers state-of-the-art or near-SOTA performance on standard coding, browsing, tool use, and research benchmarks, without domain-specific tuning. All code and data are released publicly, in the hope that ADP could help lower the barrier to standardized, scalable, and reproducible agent training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体进行大规模监督微调（SFT）时，缺乏标准化、统一格式训练数据集的根本瓶颈。研究背景是，虽然预训练LLM可以利用海量的互联网数据，但针对智能体（即能够执行序列化动作、与环境交互的模型）的微调却面临数据收集的独特挑战。当前已有许多针对不同任务（如网页导航、软件开发、工具调用等）创建的智能体数据集，但它们**在格式、表示方法和接口上高度碎片化和异构**。这种不一致性使得研究者难以有效地整合、共享和利用这些现有数据源，导致大规模智能体SFT在学术研究中仍不常见，相关公开成果稀少。

现有方法的不足在于，尽管底层数据源并不缺乏，但数据格式的多样性成为了实际使用的障碍。每个数据集通常有其专属的结构，要将其用于训练需要大量的工程化工作来进行逐一的解析和适配，这极大地阻碍了数据的规模化利用与跨任务知识迁移。

因此，本文要解决的核心问题是**智能体训练数据的标准化与统一化**。为此，论文提出了“智能体数据协议”（Agent Data Protocol, ADP），这是一种轻量级的表达语言，充当了不同格式的原始数据集与下游统一训练管道之间的“中间语言”。ADP的设计目标是在能够广泛捕获各类智能体任务（如API/工具使用、浏览、编码、软件工程等）的同时，保持解析和训练的简易性，从而无需针对每个数据集进行单独的工程处理。通过将13个现有数据集统一转换为ADP格式，并进一步转化为多种智能体框架的训练就绪格式，论文证明了ADP能有效降低标准化、可扩展和可复现的智能体训练门槛，并最终通过实验展示了基于ADP统一数据训练的模型在多个基准测试上取得了显著的性能提升。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体训练数据的收集、标准化与利用展开，可分为以下几类：

**1. 数据收集方法类**：现有工作主要通过三种方式构建智能体训练数据。一是**人工创建**（如Mind2Web），由专家演示多步任务，质量高但成本昂贵。二是**合成生成**（如Orca Agentinstruct、Synatra），利用现有大模型生成轨迹，可扩展性强但质量验证困难。三是**记录智能体运行轨迹**（如Go-Browse、Nebius SWE Trajectories），从已有智能体系统中捕获交互数据，但受限于基线智能体的能力，多样性和复杂性可能不足。

**2. 数据集与任务类**：相关研究产生了大量面向特定任务的数据集，涵盖不同领域。例如：**编码**（Code-Feedback、CodeActInstruct）、**软件工程**（SWE-Gym、SWE-smith）、**API/工具使用**（AgentInstruct、Orca Agentinstruct）以及**网页浏览**（Mind2Web、Go-Browse）。这些数据集在各自领域推动了进展，但格式、动作空间和观察结构各异，导致碎片化。

**3. 数据标准化尝试类**：已有研究注意到数据异构性问题并开始寻求统一，但现有努力多集中于**特定任务或特定智能体框架**内的标准化，缺乏社区范围的通用数据表示标准。这使得跨数据集集成和比较仍需大量工程适配，阻碍了资源的有效整合与利用。

**本文与这些工作的关系与区别**：本文承认并利用了上述丰富的数据源，但指出其核心瓶颈在于**格式碎片化**而非数据稀缺。与专注于单一收集方法或领域的数据集工作不同，本文提出的Agent Data Protocol (ADP) 旨在成为一个**轻量级、通用的“中间语言”**，能够统一表达上述各类任务的数据格式。与已有的局部标准化方案相比，ADP追求**跨任务、跨框架的社区级标准化**，目标是实现数据集的即插即用，降低大规模、可复现智能体训练的工程门槛。

### Q3: 论文如何解决这个问题？

论文通过提出并实现一个名为“Agent Data Protocol (ADP)”的轻量级统一表示语言来解决异构智能体训练数据集难以整合与利用的问题。其核心方法是建立一个标准化的中间表示层（interlingua），将不同格式、工具和接口的原始数据集转换为统一的ADP格式，进而可以高效地适配到下游各种智能体训练框架中。

整体框架是一个三阶段的转换流水线：
1.  **从原始格式到标准化格式（Raw to Standardized）**：此阶段将各种原始数据集（如网页浏览、代码执行、API调用等）映射到ADP定义的标准模式。ADP的核心设计是将任何智能体轨迹抽象为一个由“动作”和“观察”交替组成的序列。动作分为三类：调用工具的`APIAction`、生成与执行代码的`CodeAction`以及自然语言交流的`MessageAction`。观察则分为捕获文本反馈的`TextObservation`和表示网页状态的`WebObservation`。这种设计既足够表达复杂的智能体工作流，又保持了结构的简洁性。
2.  **从标准化格式到SFT格式（Standardized to SFT）**：此阶段将统一的ADP轨迹转换为适用于特定智能体框架（如OpenHands、SWE-Agent、AgentLab）的监督微调（SFT）就绪格式。由于不同框架的动作空间、观察格式和系统提示各异，ADP为每个目标框架提供一个专用的转换脚本。该脚本负责将通用的ADP动作/观察映射到框架特定的表示，并处理上下文管理、对话格式化等，生成可直接用于训练模型的指令-响应对。
3.  **质量保证（Quality Assurance）**：通过自动化验证确保转换后数据的正确性与一致性，例如检查工具调用格式、验证推理链（thought）的存在比例以及对话结构的完整性。

该方案的关键创新点在于其“中心辐射型”（hub-and-spoke）架构设计。ADP作为中心枢纽，将原本需要在每个数据集和每个智能体框架之间进行定制化转换的二次方复杂度问题（O(D×A)），简化为线性复杂度（O(D+A)）。每个数据集只需一次性地转换为ADP格式，每个智能体框架也只需一个从ADP到其自身格式的转换器。这种设计极大地降低了工程重复，使得新数据集或新框架能够快速接入，促进了大规模、标准化、可复现的智能体训练。

### Q4: 论文做了哪些实验？

实验设置方面，论文将13个异构的智能体训练数据集（涵盖编码、软件工程、API/工具使用和网页浏览等任务）统一转换为ADP格式，并基于Qwen2.5-Coder-Instruct系列模型（7B、14B、32B参数规模）进行监督微调。为确保训练平衡，对大规模数据集进行了子采样。实验使用了OpenHands、AgentLab和SWE-Agent三个不同的智能体框架，以验证ADP数据可轻松适配不同架构。

评估在四个基准测试上进行：SWE-Bench（软件工程任务）、WebArena（网页交互任务）、AgentBench OS（操作系统任务）和GAIA（通用AI助手任务）。对比方法包括各基准上已有的先进模型（如Claude 3 Opus、Claude 3.5 Sonnet）及使用特定领域数据（如SWE-smith、SWE-Gym、AgentInstruct）微调的模型。

主要结果显示，经ADP数据微调的模型在多个基准上取得了显著提升，平均性能较基础模型提高约20%，并达到或接近最先进水平。关键数据指标包括：在SWE-Bench上，7B模型准确率从0.4%提升至20.2%；在WebArena上，7B模型准确率从4.5%提升至21.0%；在AgentBench OS上，7B模型准确率从3.5%提升至27.1%。对于更大规模的14B模型，在SWE-Bench上准确率达到34.4%，超越了Claude 3.5 Sonnet的33.6%。这些结果表明，ADP协议能有效整合多样化数据，提升智能体在跨领域任务上的泛化性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的ADP协议在统一异构数据集格式方面迈出了重要一步，但其局限性和未来探索方向仍值得深入。首先，ADP目前主要整合了现有静态数据集，缺乏对动态、交互式环境（如实时多轮对话或复杂环境模拟）中生成数据的支持，未来可探索如何将强化学习或在线交互数据纳入协议。其次，协议的表达能力虽广，但对高度专业化领域（如医疗诊断或金融决策）的复杂工作流可能捕捉不足，需进一步扩展语义表示以支持嵌套决策和不确定性推理。此外，实验虽展示了SFT后的性能提升，但未深入分析不同数据混合比例、训练策略（如课程学习）对泛化能力的影响，未来可研究数据选择与加权机制。从更宏观视角看，ADP可作为基础推动跨任务知识迁移研究，例如探索预训练代理模型如何通过统一数据接口快速适应新工具。最后，协议的标准化需社区共建，未来可建立数据质量评估基准和版本迭代机制，以促进生态发展。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型智能体训练数据分散且格式不统一的问题，提出了“智能体数据协议”（ADP），旨在标准化和整合多样化的智能体数据集。核心贡献在于设计了一种轻量级、表达力强的表示语言，能够统一描述API/工具调用、网页浏览、编程、软件工程等多种智能体任务，从而作为连接异构数据源与下游训练流程的“中间语言”。

方法上，作者将13个现有智能体数据集统一转换为ADP格式，并进一步适配到多个主流智能体训练框架。通过在这些标准化数据上进行监督微调（SFT），实验结果表明，经过ADP统一数据训练的模型，在编码、浏览、工具使用和研究等标准基准测试中，平均性能比基础模型提升约20%，达到了当前最优或接近最优的水平，且无需针对特定领域进行额外调优。

论文的主要结论是，ADP协议有效降低了智能体训练的工程门槛，为实现标准化、可扩展和可复现的智能体训练提供了重要基础。其意义在于通过解决数据格式碎片化问题，促进了大规模、多样化智能体训练数据的整合与利用，有望推动该领域研究的进一步发展。
