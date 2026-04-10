---
title: "PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory"
authors:
  - "Zhifei Xie"
  - "Zongzheng Hu"
  - "Fangda Ye"
  - "Xin Zhang"
  - "Haobo Chai"
  - "Zihang Liu"
  - "Pengcheng Wu"
  - "Guibin Zhang"
  - "Yue Liao"
  - "Xiaobin Hu"
  - "Deheng Ye"
  - "Chunyan Miao"
  - "Shuicheng Yan"
date: "2026-04-09"
arxiv_id: "2604.08000"
arxiv_url: "https://arxiv.org/abs/2604.08000"
pdf_url: "https://arxiv.org/pdf/2604.08000v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
  - "cs.HC"
  - "cs.MA"
tags:
  - "Proactive Agent"
  - "Long-Term Memory"
  - "Intent Detection"
  - "Agent Architecture"
  - "Real-World Benchmark"
  - "Streaming Processing"
relevance_score: 8.0
---

# PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory

## 原始摘要

Proactivity is a core expectation for AGI. Prior work remains largely confined to laboratory settings, leaving a clear gap in real-world proactive agent: depth, complexity, ambiguity, precision and real-time constraints. We study this setting, where useful intervention requires inferring latent needs from ongoing context and grounding actions in evolving user memory under latency and long-horizon constraints. We first propose DD-MM-PAS (Demand Detection, Memory Modeling, Proactive Agent System) as a general paradigm for streaming proactive AI agent. We instantiate this paradigm in Pask, with streaming IntentFlow model for DD, a hybrid memory (workspace, user, global) for long-term MM, PAS infra framework and introduce how these components form a closed loop. We also introduce LatentNeeds-Bench, a real-world benchmark built from user-consented data and refined through thousands of rounds of human editing. Experiments show that IntentFlow matches leading Gemini3-Flash models under latency constraints, while identifying deeper user intent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前人工智能系统在现实世界中缺乏主动性和长期适应能力的问题。研究背景是，尽管AI在推理、多模态统一和智能体系统方面取得了进展，但现有系统大多仍局限于“你问我答”的被动交互模式。这种模式存在明显不足：首先，它与真实世界中智能应用的时机、情境和人性化因素不匹配，例如在实时对话或敏感社交场合中，用户往往无法或不便主动求助；其次，它造成了信息瓶颈，阻碍了AI对用户形成深入、持续的理解。

现有方法主要集中在实验室环境下的特定领域（如编程辅助、游戏协作），其不足在于：1) 处理场景狭窄，缺乏泛化能力；2) 未能充分考虑现实世界对交互深度、实时响应和动态环境鲁棒性的关键要求；3) 最关键的是，缺乏一种能够积累长期用户理解、随用户共同演化的记忆机制。

因此，本文要解决的核心问题是：如何构建一个能够在真实世界复杂、模糊、实时约束的场景下，主动推断用户潜在需求，并基于长期记忆进行决策的智能体。具体而言，论文试图从范式、核心能力、长期适应和系统实现四个层面，提供一个统一的解决方案，以弥合实验室原型与实用化主动智能体之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**方法类**、**系统类**和**评测类**。

在**方法类**研究中，已有工作探索了特定领域的主动性AI，例如编程辅助、计算机操作协助和协作游戏。这些研究为主动性交互提供了初步案例，但通常局限于狭窄场景和受控的实验室环境，缺乏对**泛化能力**、**实时响应**、**动态环境鲁棒性**以及**长期记忆机制**的深入处理。本文提出的DD-MM-PAS范式（需求检测、记忆建模、主动代理系统）旨在提供一个统一且通用的架构，以弥补这些不足。特别是，本文的IntentFlow模型专注于在流式输入下进行低延迟的潜在需求检测，这与以往主要处理离散请求的模型有本质区别。

在**系统类**研究中，现有的智能体系统多侧重于规划、执行和适应，但通常以被动响应（“你问我答”）模式运行，缺乏主动发起帮助的能力。本文构建的Pask系统是一个完整的端到端技术栈，集成了超过20个模型/代理和10个核心工程模块，实现了从感知、记忆到执行的闭环，并强调了在真实世界部署中的稳定性和低延迟要求，这与多数停留在概念验证阶段的系统不同。

在**评测类**研究中，缺乏针对真实世界主动性AI的标准化基准。本文构建并开源了LatentNeeds-Bench基准，该基准基于用户同意的真实数据并通过多轮人工编辑精炼，专注于评估对深度、模糊用户意图的理解，这与以往在合成或受限任务上的评测形成了对比。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PASK的完整系统来解决现实世界中主动智能体面临的深度、复杂性、模糊性、精确性和实时性约束等挑战。其核心方法是构建一个基于DD-MM-PAS范式的三层架构，该范式将主动智能分解为需求检测、记忆建模和主动代理系统三个不可或缺的耦合功能。

整体框架由Pask系统实例化，形成一个从感知、理解到行动的闭环。主要模块包括：1）**Pask-DD（需求检测）**，其核心是**IntentFlow模型**，这是一个采用主-辅双模型架构的流式意图推理框架。主模型（Demand Detector）基于大型语言模型，负责实时分析信息流，并预测三种决策令牌：静默、快速干预或完整协助。辅助模型（MemLoader）则负责处理检索到的记忆证据并进行精炼。这种设计将主动协助转化为一个在增长的历史交互上进行在线决策的过程，并能灵活协调直接响应与基于记忆的深度推理。2）**Pask-MM（记忆建模）**，这是一个**自演化的分层混合记忆系统**，灵感来源于计算机体系结构。它包含三个功能组件：作为高速缓存的用户记忆（存储稳定用户画像）、作为主内存的工作空间记忆（维护会话级动态）以及作为外部存储的全局记忆（以树形结构存储长期交互历史）。为解决低延迟检索的挑战，系统采用了**解耦的状态返回与异步检索策略**，即时返回工作空间状态，并异步地从全局记忆的锚定子树中进行精细化检索增强生成。3）**Pask-PAS（主动代理系统）**，这是一个**系统实现框架**，将前端设备、服务器后端、控制层、数据层和AI后端连接成一个始终在线的循环，确保感知、理解和行动的协调执行。

关键技术创新点体现在多个层面：在**方法层面**，IntentFlow将深度意图推理转化为高效的端到端前向预测，并通过两阶段训练（大规模监督微调+基于真实数据的强化学习对齐）来内化推理过程，以在低延迟下识别更深层的用户意图。在**架构层面**，分层混合记忆设计通过**有界的自演化策略**（如冲突解决、记忆衰减和惰性合并）解决了长期部署中的信息冲突和数据爆炸问题，确保了系统的可扩展性和稳定性。在**系统层面**，DD-MM-PAS范式首次明确地将需求检测、记忆建模与执行系统统一为一个最小必要结构，强调了主动智能源于这三者的协同整合，而非单一的响应生成。此外，论文还构建了基于真实用户数据的**LatentNeeds-Bench基准**，为评估现实条件下的主动协助提供了重要基础。

### Q4: 论文做了哪些实验？

论文实验围绕PASK系统在真实世界场景下的主动代理能力展开。实验设置包括构建LatentNeeds-Bench基准测试，该基准基于用户授权数据，并经过数千轮人工编辑精炼，以评估模型在深度、复杂性、模糊性、精确性和实时性约束下的表现。对比方法主要涉及领先的Gemini3-Flash模型。实验分为多个方面：在需求检测（DD）上，使用IntentFlow模型在流式处理中推断潜在用户意图；在记忆建模（MM）上，采用混合记忆（工作空间、用户、全局）支持长期交互；并通过主动代理系统（PAS）框架整合这些组件形成闭环。主要结果显示，IntentFlow在延迟约束下性能与Gemini3-Flash模型相当，同时能识别更深层的用户意图。关键数据指标包括在Work、Learning、Daily等任务类别上的评估分数，具体数值未在提供内容中详细列出，但强调了模型在实时性和意图深度方面的优势。整体实验验证了DD-MM-PAS范式在提升代理主动性和记忆能力方面的有效性。

### Q5: 有什么可以进一步探索的点？

该论文在构建具有长期记忆的意图感知主动代理方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心组件IntentFlow模型虽然在延迟约束下性能可比肩大型模型，但其对“深层用户意图”的推断能力仍主要基于当前公开的基准测试，在更复杂、动态且充满噪音的真实世界开放场景中的泛化性与鲁棒性有待进一步验证。其次，论文提出的混合记忆架构（工作空间、用户、全局）如何高效地协同、更新与检索，尤其是在处理长期、多模态（如结合视觉与音频上下文）的用户记忆时，其效率与准确性面临挑战。

未来研究可以从以下几个方向展开：一是**增强意图推断的深度与可解释性**，探索如何将显式用户反馈与隐式行为信号更细腻地结合，并利用因果推理等方法提升意图归因的透明度。二是**发展更自适应与安全的记忆管理机制**，研究记忆的主动遗忘、隐私保护下的记忆加密，以及如何防止记忆偏差导致代理行为失准。三是**构建更复杂的评估体系**，当前基准虽源于真实数据，但可进一步引入多轮、多代理协作的交互场景，并设计量化指标来衡量代理干预的“适时性”与长期用户满意度，而非仅关注意图识别准确率。这些改进将推动主动代理从实验室原型迈向更可靠、个性化的实际应用。

### Q6: 总结一下论文的主要内容

该论文针对现有AI系统被动响应的局限，提出了一个面向真实世界、具备长期记忆和意图感知能力的主动智能体（Proactive Agent）通用框架。核心问题是解决在实时性、深度、复杂性和模糊性约束下，如何让AI系统能主动推断用户的潜在需求，并基于持续演进的用户记忆进行精准干预。

论文首先提出了一个名为DD-MM-PAS（需求检测、记忆建模、主动智能体系统）的通用范式。在此基础上，作者实例化了名为Pask的系统，其核心贡献包括：1）设计了流式意图检测模型IntentFlow，用于低延迟、准确地从连续上下文中识别用户潜在需求；2）构建了一个混合记忆系统（工作空间记忆、用户记忆、全局记忆），以支持跨会话的长期用户理解与共演化；3）开发了完整的端到端主动智能体系统（PAS）基础设施，集成了前端、后端和AI模块，实现闭环运行。此外，论文还引入了基于真实用户数据构建的评测基准LatentNeeds-Bench。

实验表明，IntentFlow模型在延迟约束下能达到与领先模型（如Gemini 3 Flash）相当的性能，并能识别更深层的用户意图。该研究的意义在于为主动AI提供了一个系统性的架构范式，推动了AI从被动问答工具向具有长期记忆、能实时感知并主动提供协助的共演化伙伴转变。
