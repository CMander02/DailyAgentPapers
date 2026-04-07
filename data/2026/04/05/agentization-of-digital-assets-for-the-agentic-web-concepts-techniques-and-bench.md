---
title: "Agentization of Digital Assets for the Agentic Web: Concepts, Techniques, and Benchmark"
authors:
  - "Linyao Chen"
  - "Bo Huang"
  - "Qinlao Zhao"
  - "Shuai Shao"
  - "Zhi Han"
  - "Zicai Cui"
  - "Ziheng Zhang"
  - "Guangtao Zeng"
  - "Wenzheng Tang"
  - "Yikun Wang"
  - "Yuanjian Zhou"
  - "Zimian Peng"
  - "Yong Yu"
  - "Weiwen Liu"
  - "Hiroki Kobayashi"
  - "Weinan Zhang"
date: "2026-04-05"
arxiv_id: "2604.04226"
arxiv_url: "https://arxiv.org/abs/2604.04226"
pdf_url: "https://arxiv.org/pdf/2604.04226v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Agentic Web"
  - "Agentization"
  - "Multi-Agent Collaboration"
  - "Benchmark"
  - "Tool Use"
  - "Web Automation"
  - "Agent Architecture"
relevance_score: 8.5
---

# Agentization of Digital Assets for the Agentic Web: Concepts, Techniques, and Benchmark

## 原始摘要

Agentic Web, as a new paradigm that redefines the internet through autonomous, goal-driven interactions, plays an important role in group intelligence. As the foundational semantic primitives of the Agentic Web, digital assets encapsulate interactive web elements into agents, which expand the capacities and coverage of agents in agentic web. The lack of automated methodologies for agent generation limits the wider usage of digital assets and the advancement of the Agentic Web. In this paper, we first formalize these challenges by strictly defining the A2A-Agentization process, decomposing it into critical stages and identifying key technical hurdles on top of the A2A protocol. Based on this framework, we develop an Agentization Agent to agentize digital assets for the Agentic Web. To rigorously evaluate this capability, we propose A2A-Agentization Bench, the first benchmark explicitly designed to evaluate agentization quality in terms of fidelity and interoperability. Our experiments demonstrate that our approach effectively activates the functional capabilities of digital assets and enables interoperable A2A multi-agent collaboration. We believe this work will further facilitate scalable and standardized integration of digital assets into the Agentic Web ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决“智能体化网络”生态系统中，规模化、自动化生成领域专用智能体的核心瓶颈问题。研究背景是，随着大语言模型智能体在规划、工具使用和交互决策方面取得显著进展，基于LLM的多智能体系统被视为实现现实世界AI应用的有效范式。智能体化网络被设想为这类系统的基础设施，旨在通过A2A等互操作性标准，实现异构智能体的大规模协作。

现有方法的不足在于，当前智能体化网络的智能体供给严重依赖人工构建，这种方式成本高、速度慢且难以扩展多样性，导致网络缺乏一种可扩展的方式来持续供应领域专用智能体，从而限制了整个生态系统的容量、覆盖范围和整体性能。

本文要解决的核心问题是：如何将互联网中大量、多样且蕴含领域知识与功能的现有静态数字资产（如代码库、文档、在线服务等），自动、可靠地转化为符合智能体化网络标准（特别是A2A协议）且可被其他智能体调用的互操作智能体。这一“资产智能体化”过程面临三大技术挑战：环境不一致（依赖冲突难以复现）、技能非结构化（有用能力隐藏在未文档化的代码中）和语义鸿沟（即使代码可运行，也缺乏清晰、可发现的调用接口）。论文以最具复杂性和挑战性的代码仓库为代表场景，形式化定义了A2A智能体化过程，旨在通过自动化方法打破数据孤岛，为智能体化网络生态提供可扩展的专用能力来源。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码仓库利用、资产代理化（Agentization）以及标准化协议。

在**代码仓库利用**方面，现有研究分为两个方向：一是**仓库开发**，关注代码库的维护与扩展，如RepoBench、DevEval和EvoCodeBench等基准测试评估代码生成的保真度与依赖理解；二是**任务解决**，将仓库视为可执行资源以解决端到端问题，例如SWE-bench验证错误修复，GitTaskBench测试工作流自动化，而EnvBench和LoCoBench则分别针对环境设置和长上下文推理等瓶颈。与这些工作不同，本文并非评估如何利用仓库完成任务，而是专注于**代理化过程本身**，即如何将代码仓库转化为标准化的、符合A2A协议的智能体。

在**资产代理化**研究中，早期工作侧重于将现有服务转化为工具，以增强智能体的能力。近期则有研究直接尝试将数字资产转化为智能体，例如Paper2Agent将科研论文转化为交互式智能体，repomaster和EnvX探索为代码仓库生成对应智能体。然而，这些工作未能确保生成的智能体具备**Agentic Web兼容的通信能力**，限制了其广泛应用。本文通过提出一个严格遵循A2A协议的标准化代理化流程，填补了这一关键空白。

在**标准化协议**领域，早期系统依赖特定框架接口，阻碍了跨生态系统协作。近期出现了如模型上下文协议（MCP）和智能体间协议（A2A）等标准，以支持结构化工具使用和去中心化交互。但现有研究多集中于评估智能体如何有效利用这些协议兼容的工具，对于**如何构建或改造遗留软件以符合协议规范**这一过程关注不足。本文的工作正是针对这一薄弱环节，系统性地研究并评估了将数字资产转化为A2A合规智能体的能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个系统化的“代理化”框架来解决数字资产自动转化为智能代理的问题，其核心是设计了一个名为“代理化代理”的智能体，以端到端的方式执行转化流程。整体框架被形式化为一个四阶段的处理管道，将静态的代码仓库等数字资产映射为符合A2A协议、可交互的智能体。

具体而言，方法的核心架构和主要模块如下：
1.  **环境设置**：这是代理可执行的基础。系统首先分析数字资产（如代码仓库）的依赖项和配置文件，通过一个映射函数合成一个可复现的运行环境。这确保了资产内部的静态逻辑能够在确定性的环境中运行。
2.  **技能提取为工具**：在已建立的环境中，系统从数字资产中识别、封装并验证其功能单元，将其转化为一组原子化的、可执行的工具。这一步骤赋予了智能体具体的能力。
3.  **内部代理实例化**：这是构建智能体认知架构的核心。系统将提取出的工具集成到一个推理循环中，实例化出一个具有内部逻辑的“内部代理”。该代理能够进行规划，并调用工具来完成任务。
4.  **最终代理化**：为了生成符合A2A协议的智能体，系统需要生成一个“代理卡片”。该卡片作为智能体的自描述注册表，详细说明了其身份和可用工具，使得其他代理无需内部检查就能理解其能力。最终的智能体由内部代理和代理卡片共同构成。

论文的关键技术创新点在于：
*   **形式化定义与分解**：首次严格定义了A2A代理化过程，并将其分解为四个关键阶段，明确了每个阶段的技术挑战和映射函数。
*   **端到端的自动化实现**：提出了“代理化代理”这一具体实现，它将上述理论框架操作化，能够自动执行从环境分析到最终代理生成的全过程，实现了数字资产到智能体的自动化转换。
*   **面向互操作性的设计**：通过强制要求生成符合A2A协议的代理和标准化的代理卡片，确保了生成的智能体能够被“代理化网络”中的其他智能体发现和理解，从而支持多智能体间的互操作与协作。

总之，该方法通过一个结构清晰、模块化的四阶段管道，结合一个专门的代理化代理，系统性地解决了数字资产自动、标准化转化为可交互、可协作智能体的问题。

### Q4: 论文做了哪些实验？

实验在四个代表性的编码智能体框架（Claude Code、Codex CLI、OpenHands、EnvX）上实例化所提出的Agentization Agent进行评估。实验设置采用标准化的智能体栈和具体编排机制，其中Inner Agent以Claude Code为推理骨干，多智能体评估则采用由Claude Code驱动的集中式编排，并利用基准构建中获得的真实子任务分解。

评估基于提出的A2A-Agentization Bench基准，该基准旨在从保真度和互操作性方面评估智能体化质量。实验分为三个阶段：第一阶段评估智能体化过程，报告成功率和成本；第二阶段评估能力继承，通过单仓库任务执行验证功能保真度；第三阶段评估协作执行，在多智能体环境中衡量编排成功率与执行成功率。对比方法即为上述四个框架。

主要结果如下：在阶段一，Claude Code和EnvX的Agentization Success（Pass@1）均达到100%，EnvX因额外验证步骤消耗更多tokens（约421万 vs 337万）。阶段二中，Claude Code在单仓库任务上的总体执行成功率最高（36.9%），EnvX为35.1%。阶段三评估协作能力，在技能规范质量上，EnvX的Skill F1得分最高（66.2%），Claude Code为63.0%；在最终执行成功率上，OpenHands的总体Execution SR最高（46.2%），但其编排成功率最低（65.1%）。实验还识别了环境预配置、技能构建和能力规范三个关键挑战作为优化方向。

### Q5: 有什么可以进一步探索的点？

本文提出的数字资产“代理化”框架为构建Agentic Web奠定了基础，但仍有诸多方向值得深入探索。首先，当前方法高度依赖环境预配置和技能构建的准确性，这在实际复杂、异构的软件资产中可能面临泛化能力不足的问题。未来可研究更鲁棒、自适应的环境理解与技能抽象方法，例如利用大模型进行代码语义的深层推理与动态适配。其次，基准测试主要关注保真度与互操作性，未来可纳入更多维度的评估，如代理在开放环境中的长期稳定性、安全边界以及多代理协作涌现的复杂性。此外，论文聚焦于代码仓库类资产，未来可将代理化范畴扩展至更广泛的数字实体（如API服务、数据库、甚至物联网设备），并研究跨模态资产的统一代理封装机制。最后，如何建立标准化、轻量级的代理描述与发现协议，以降低生态集成成本，也是推动Agentic Web规模化落地的关键。

### Q6: 总结一下论文的主要内容

本文针对“智能体化网络”中缺乏规模化、自动化生成智能体的问题，提出了将现有数字资产（以代码仓库为代表）自动转化为可互操作智能体的解决方案。论文首先形式化了A2A-智能体化过程，将其分解为关键阶段并识别了三大技术挑战：环境不一致、技能非结构化以及语义鸿沟。为解决这些问题，作者提出了A2A-智能体化智能体，这是一个能够自动处理依赖冲突、从代码中提取原子化技能并生成清晰接口（如智能体卡片）的自主框架。为了系统评估智能体化的质量，论文还创建了首个基准测试A2A-Agentization Bench，它基于35个真实代码仓库，从保真度（技能执行准确性）和互操作性（被其他智能体调用的能力）两个维度进行评估。实验表明，所提方法能有效激活数字资产的功能，并实现可互操作的A2A多智能体协作。这项工作的核心贡献在于为智能体化网络提供了一种标准化、可扩展的数字资产集成途径，对推动大规模异构智能体生态系统的建设具有重要意义。
