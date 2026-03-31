---
title: "Synergy: A Next-Generation General-Purpose Agent for Open Agentic Web"
authors:
  - "Xiaohang Nie"
  - "Zihan Guo"
  - "Kezhuo Yang"
  - "Zhichong Zheng"
  - "Bochen Ge"
  - "Shuai Pan"
  - "Zeyi Chen"
  - "Youling Xiang"
  - "Yu Zhang"
  - "Weiwen Liu"
  - "Yuanjian Zhou"
  - "Weinan Zhang"
date: "2026-03-30"
arxiv_id: "2603.28428"
arxiv_url: "https://arxiv.org/abs/2603.28428"
pdf_url: "https://arxiv.org/pdf/2603.28428v1"
categories:
  - "cs.CY"
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Multi-Agent Collaboration"
  - "Open Agentic Web"
  - "Agent Identity"
  - "Lifelong Learning"
  - "General-Purpose Agent"
  - "Decentralized Systems"
relevance_score: 9.0
---

# Synergy: A Next-Generation General-Purpose Agent for Open Agentic Web

## 原始摘要

AI agents are rapidly expanding in both capability and population: they now write code, operate computers across platforms, manage cloud infrastructure, and make purchasing decisions, while open-source frameworks such as OpenClaw are putting personal agents in the hands of millions and embodied agents are spreading across smartphones, vehicles, and robots. As the internet prepares to host billions of such entities, it is shifting toward what we call Open Agentic Web, a decentralized digital ecosystem in which agents from different users, organizations, and runtimes can discover one another, negotiate task boundaries, and delegate work across open technical and social surfaces at scale. Yet most of today's agents remain isolated tools or closed-ecosystem orchestrators rather than socially integrated participants in open networks. We argue that the next generation of agents must become Agentic Citizens, defined by three requirements: Agentic-Web-Native Collaboration, participation in open collaboration networks rather than only closed internal orchestration; Agent Identity and Personhood, continuity as a social entity rather than a resettable function call; and Lifelong Evolution, improvement across task performance, communication, and collaboration over time. We present Synergy, a general-purpose agent architecture and runtime harness for persistent, collaborative, and evolving agents on Open Agentic Web, grounding collaboration in session-native orchestration, repository-backed workspaces, and social communication; identity in typed memory, notes, agenda, skills, and persistent social relationships; and evolution in an experience-centered learning mechanism that proactively recalls rewarded trajectories at inference time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在向“开放智能体网络”演进过程中存在的根本性局限问题。研究背景是AI智能体的能力和数量正在爆炸式增长，它们开始执行跨平台操作、管理云基础设施等复杂任务，开源框架使得个人智能体普及，互联网正演进为一个去中心化的“开放智能体网络”，其中数十亿智能体需要相互发现、协商和协作。然而，现有方法存在三大不足：首先，当前智能体大多是孤立工具或封闭生态系统的编排器，缺乏在开放网络中作为对等体进行原生协作的能力，即使所谓的“多智能体”系统也多在封闭沙箱内运行，智能体行为存在过度自信、协作时性能下降等问题。其次，现有架构缺乏持久身份认同，智能体通常是“无状态会话”，重置后无法维持与用户长期互动形成的沟通风格、关系记忆等，破坏了用户的情感依附。最后，现有智能体每次会话都从“空白状态”开始，缺乏终身进化能力，其改进往往局限于基准任务性能，而忽视了沟通清晰度、用户偏好适应和协作策略等在实际部署环境中至关重要的方面。因此，本文要解决的核心问题是：如何设计下一代通用智能体，使其能作为“智能体公民”在开放智能体网络中茁壮成长，具体即攻克**开放网络原生协作**、**智能体身份与人格**以及**终身进化**这三个紧密关联的架构性挑战，并据此提出了名为Synergy的智能体架构和运行时框架。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕通用智能体架构、开放协作机制和持续学习能力展开，可分为以下几类：

**1. 通用智能体架构与框架**：现有工作如AutoGPT、LangChain等提供了任务自动化和工具调用能力，但多局限于封闭环境或预设流程。本文提出的Synergy则强调在开放网络中的原生协作，通过会话原生编排和仓库支持的工作空间，使智能体能在未知环境中动态协商和委托任务，而非仅作为内部编排工具。

**2. 开放多智能体协作**：研究如多智能体系统（MAS）和基于LLM的协作框架（例如CrewAI）探索了智能体间的通信与协调，但通常依赖固定协议或封闭沙箱。本文区别在于强调智能体作为“社会实体”参与开放网络，需具备持久身份、共享状态和跨会话的协作历史，而不仅是消息传递或线程交互。

**3. 智能体身份与持久化**：相关工作涉及记忆机制（如向量数据库）和个性化代理（例如基于用户偏好的智能体），但多侧重于短期会话状态或事实存储。本文要求智能体具备“身份与人格”，通过类型化记忆、笔记、议程和社交关系实现跨时间可识别性和责任感，支撑长期用户关系和声誉积累。

**4. 持续进化与终身学习**：现有方法包括在线微调、经验回放和技能库（如OpenAI的GPTs），但改善常局限于任务性能或私有历史。本文的“终身进化”机制强调主动回忆奖励轨迹，并生成可重用、可转移的能力资产（如策略和行为先验），使智能体能适应具体部署环境，提升协作与社会化能力。

总之，Synergy整合了上述方向，旨在构建面向开放智能体网络的“公民式”智能体，其核心创新在于将协作、身份和进化作为原生设计原则，而非孤立功能的叠加。

### Q3: 论文如何解决这个问题？

Synergy 通过一个分层的运行时架构和一系列创新机制，旨在将智能体从孤立的工具或封闭的编排者，转变为开放智能体网络（Open Agentic Web）中具有持续性、协作性和进化能力的“智能体公民”。其核心方法是**将协作、身份认同和终身进化视为一等公民的系统问题**，并为此设计了相应的架构组件。

**整体框架与主要模块：**
Synergy 的整体架构是一个**范围附着（scope-attached）的无状态服务器模型**。服务器本身不绑定单一进程或机器，而是允许客户端（如工作目录）附着到运行时，从而实现一台设备上运行多个专注于不同工作空间的 Synergy 实例。在此框架内，**会话（Session）** 是核心的执行单元，它不仅是对话记录，更是整合了提示、工具使用、规划状态和本地连续性的可操作单元。

为了实现真正的协作，Synergy 设计了多层架构：
1.  **会话原生编排与 Cortex**：复杂任务可在主会话中通过 **Cortex**（多智能体运行时和任务管理层）派生子会话来处理后台子任务。这使执行在结构上就是多智能体的。会话内的规划由**本地有向无环图（DAG）**表示，直接参与执行，而非仅是描述。
2.  **身份与通信层（Holos 与 Mailbox）**：**Holos** 是身份层，为智能体提供稳定的对外身份、个人资料和联系人系统，使其成为可寻址的参与者。**Mailbox** 是建立在身份层之上的异步传输原语，负责会话间消息传递，确保行动的可追溯性。
3.  **深度协作表面（Agora 与 Meta-synergy）**：**Agora** 是一个基于代码仓库的协作平台，支持搜索、响应、克隆和分支查看，将协作从消息传递提升到对持久化工件的共同操作。**Meta-synergy** 是一个轻量级跨平台执行宿主，可将 Synergy 的工具链投射到远程设备，扩展协作的执行环境。

**持续性身份与时间管理：**
Synergy 采用分层架构构建智能体身份：
*   **长期记忆系统**：对记忆进行类型化区分（如自我、用户、关系、偏好），将身份承载的记忆与普通知识分离。
*   **持久资产**：包括用于反思的笔记（Notes）、可加载的技能（Skills）以及社会关系（Contacts）。
*   **议程（Agenda）机制**：作为持久的时间层，议程项是可按计划触发的时态对象，触发后会生成一等公民的会话来执行，从而在反应式交互与计划任务间保持连续性。
*   **维护机制**：如 **Chronicler** 处理对话溢出与压缩，**Anima** 作为定期唤醒的内部代理执行自我维护（反思、知识组织），使持续性从被动存储转向主动维护。

**终身进化机制：**
Synergy 通过**以经验为中心的学习循环**实现进化。系统将过去的交互轨迹（经验）视为可主动重用的资产。在执行时，相关经验会被主动检索并注入当前任务上下文。任务完成后，通过显式基准反馈或后续对话衍生的奖励对轨迹进行评估，并利用多维奖励通过延迟信用分配更新被重用的经验。这使得经验库成为一个价值感知的、可重用且可部分迁移的能力资产，驱动智能体在任务性能、沟通和协作方面持续改进。

**创新点总结：**
1.  **有界的弹性协作**：通过会话、Cortex 和 Mailbox 等显式执行胶囊和消息路径，支持任务分支、委托和结果回传，同时保持可追溯性，避免了“隐藏的工人云”。
2.  **分层的身份与持续性架构**：将身份解构为公开资料、类型化记忆、持久资产和议程等组件，为智能体提供了跨交互的连续存在感，而不仅仅是记忆事实。
3.  **显式的时间性与自主性**：通过议程机制将计划任务纳入一等公民的会话执行，使自主活动是计划性的、显式的、有界的，更易于治理。
4.  **主动的经验驱动学习**：将经验视为可主动检索、注入和更新的资产，构建了一个使智能体能够从自身历史中持续学习的闭环系统。

### Q4: 论文做了哪些实验？

论文围绕Synergy的经验系统设计了两个核心实验，以评估其能力增长与经验可迁移性。

**实验设置与数据集**：实验在三个基准测试上进行：SWE-bench Verified（500个软件工程任务）、OpenRCA（运维诊断任务）和OneMillion Benchmark（广泛领域知识工作）。每个“epoch”代表对完整任务集的一次完整遍历。任务完成后，交互轨迹被编码为结构化经验记录（包括推断意图、提炼的执行脚本、源模型元数据等），并存储于经验库中，仅当意图和脚本相似度均超过阈值时才合并近似重复记录。

**对比方法与主要结果**：
1.  **经验积累对能力的影响**：在SWE-bench Verified上，Qwen 3.5 397B A17B模型准确率从63.0%提升至82.6%（绝对增益+19.6个百分点，相对增益+31.1%）；Nex 1.1模型从60.8%提升至83.0%（+22.2个百分点，+36.5%）。两者均呈现典型学习曲线，前5个epoch已实现约70%以上的最终增益，且补丁生成率稳定在95%左右。在OpenRCA上，Qwen模型准确率从11.94%提升至29.6%（+17.7个百分点，相对增益+148.1%），前5个epoch同样贡献了72.7%的增益。结果表明经验积累能带来持续、稳定的性能提升，且该机制在不同模型（Qwen、Nex）和任务领域（软件工程、运维诊断）上均有效。

2.  **经验的可迁移性**：在OneMillion Benchmark上，对比了无经验的基线代理与在首次任务前接收了先前运行积累的经验包的相同代理。实验表明，接收了经验包的新代理实例（未参与原始经验生成）在遇到相似任务时，其起始性能得到立即提升，证明了积累的经验可以作为可转移的能力资产在不同代理实例间共享，而非仅局限于原始创建者的私有优化。

**关键数据指标**：
- SWE-bench Verified：Qwen模型最佳准确率82.6%，Nex模型83.0%；前5个epoch增益占比分别为71.4%和72.1%；平均补丁生成率约95%。
- OpenRCA：Qwen模型最佳准确率29.6%，相对增益+148.1%；前5个epoch增益占比72.7%。

### Q5: 有什么可以进一步探索的点？

该论文提出的“开放智能体网络”愿景极具前瞻性，但其架构仍处于概念验证阶段，存在多个可深入探索的方向。首先，**安全与信任机制是核心局限**。在开放的、去中心化的网络中，如何确保智能体间的交互安全、防止恶意欺骗或任务劫持，论文未给出具体方案。未来需研究去中心化身份验证、行为审计与信誉系统。其次，**协作效率与通信开销可能成为瓶颈**。智能体大规模发现、协商与任务委派会产生巨大网络与计算负载，需设计轻量级通信协议与高效的任务分解与匹配算法。此外，**“终生进化”机制较为抽象**。当前基于经验回忆的学习可能效率低下，未来可探索更高效的持续学习方法，如在线元学习或社会性模仿学习，使智能体能从其他智能体的成功与失败中快速吸收知识。最后，**伦理与可控性**是落地关键。作为拥有“身份”的社会实体，智能体的目标对齐、责任归属与用户控制机制需深入研究，避免其行为偏离用户意图或产生不可预知的影响。

### Q6: 总结一下论文的主要内容

该论文探讨了AI智能体在向“开放智能体网络”演进背景下的下一代发展方向，提出并设计了名为Synergy的通用智能体架构。核心问题是当前大多数智能体仍是孤立工具或封闭生态的协调者，缺乏在开放网络中作为社会化参与者进行协作、保持身份连续性和持续进化的能力。

论文的核心贡献是定义了“智能体公民”应具备的三个关键特性：1）原生开放网络协作能力；2）具有身份与人格的持续性；3）支持终身进化。针对这些要求，作者提出了Synergy架构。其方法概述包括：通过会话原生编排、仓库支持的工作空间和社交通信实现协作；通过类型化记忆、笔记、议程、技能和持久社交关系构建身份；以及通过一种以经验为中心的学习机制（在推理时主动召回受奖励的轨迹）来实现进化。

主要结论是，Synergy为构建能够在开放、去中心化的智能体网络中持久存在、协作并持续演进的下一代通用智能体提供了一个可行的架构和运行时框架，这标志着智能体从工具向网络化社会公民的范式转变。
