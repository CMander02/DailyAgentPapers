---
title: "When Should an AI Act? A Human-Centered Model of Scene, Context, and Behavior for Agentic AI Design"
authors:
  - "Soyoung Jung"
  - "Daehoo Yoon"
  - "Sung Gyu Koh"
  - "Young Hwan Kim"
  - "Yehan Ahn"
  - "Sung Park"
date: "2026-02-26"
arxiv_id: "2602.22814"
arxiv_url: "https://arxiv.org/abs/2602.22814"
pdf_url: "https://arxiv.org/pdf/2602.22814v1"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "Agent Design Principles"
  - "Human-Centered AI"
  - "Conceptual Model"
  - "Proactive Intervention"
  - "Contextual Reasoning"
relevance_score: 8.5
---

# When Should an AI Act? A Human-Centered Model of Scene, Context, and Behavior for Agentic AI Design

## 原始摘要

Agentic AI increasingly intervenes proactively by inferring users' situations from contextual data yet often fails for lack of principled judgment about when, why, and whether to act. We address this gap by proposing a conceptual model that reframes behavior as an interpretive outcome integrating Scene (observable situation), Context (user-constructed meaning), and Human Behavior Factors (determinants shaping behavioral likelihood). Grounded in multidisciplinary perspectives across the humanities, social sciences, HCI, and engineering, the model separates what is observable from what is meaningful to the user and explains how the same scene can yield different behavioral meanings and outcomes. To translate this lens into design action, we derive five agent design principles (behavioral alignment, contextual sensitivity, temporal appropriateness, motivational calibration, and agency preservation) that guide intervention depth, timing, intensity, and restraint. Together, the model and principles provide a foundation for designing agentic AI systems that act with contextual sensitivity and judgment in interactions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个核心的、日益紧迫的Agentic AI设计问题：智能体在何时、为何以及是否应该主动干预用户行为。当前，基于LLM/VLM的智能体能够利用上下文数据推断用户情境并进行主动干预，但由于缺乏关于何时行动的、基于原则的判断，它们经常失败。具体而言，现有系统擅长感知客观场景（Scene），但难以理解用户赋予该场景的主观意义（Context），以及影响行为可能性的内在因素（Human Behavior Factors）。这导致智能体的干预可能不合时宜、不相关甚至具有侵入性。因此，论文提出了一个根本性的概念模型，将人类行为重新定义为一种整合了客观场景、主观语境和人类行为因素的“解释性结果”，旨在为设计具有情境敏感性和判断力的Agentic AI系统提供理论基础和设计原则。

### Q2: 有哪些相关研究？

论文从多学科视角梳理了相关研究。在行为理解方面，引用了心理学和HCI领域的经典理论，如计划行为理论（TPB）、COM-B行为改变模型以及Fogg的行为说服模型，这些研究聚焦于解释和预测行为的内部微观机制（如态度、能力、动机）。在场景理解方面，参考了计算机视觉、机器人学和HCI中的场景理解与基于场景的设计工作，这些研究侧重于从客观、第三人称视角分析和设计包含行动者、对象、背景和活动的“场景”。在上下文建模方面，借鉴了神经科学（关注用户如何接收和解释信息）和HCI（关注如何捕捉和设计用户上下文信息）的研究。论文指出，现有研究存在局限：心理学模型未能充分纳入行为发生的具体情境和动态变化的上下文；而技术导向的场景理解则忽略了用户的主观意义建构。本文的工作正是在此基础上，通过整合这些多学科视角，构建了一个统一的概念模型，明确区分了客观的“场景”、主观的“语境”和影响行为可能性的“因素”，从而弥合了现有研究之间的鸿沟。

### Q3: 论文如何解决这个问题？

论文的核心解决方案是提出一个名为“人类行为过程概念模型”的理论框架，并从中推导出五条具体的设计原则。该模型将行为生成过程解构为三个核心概念：1) **场景（Scene）**：由可客观识别的元素构成，包括行动者、可移动对象、背景（固定表面/结构）以及作为行为锚点的“活动”（Activity）。2) **语境（Context）**：为用户主观建构的意义层，为场景的客观元素赋予个人化含义。它包括空间、时间、内感受（生理信号）、个体（偏好、特征）和社会文化五个维度的上下文。3) **人类行为因素（Human Behavior Factors）**：决定行为可能性的内在认知因素，包括态度、感知机会、感知能力、动机和触发因素。模型描述了行为如何从可观察的场景出发，经过语境赋予意义，再结合行为因素（通过内部行为生成循环），最终形成具有意义的行为结果。基于此模型，论文提出了五条**Agent设计原则**：**行为对齐原则**（干预应与用户活动层级匹配）、**语境敏感原则**（干预应基于用户如何体验情境）、**时间适当性原则**（干预时机至关重要）、**动机校准原则**（干预强度和形式应根据用户的行为准备度调整）以及**主体性保护原则**（应保持用户对干预结果的控制权）。这些原则共同指导智能体在深度、时机、强度和克制方面做出更明智的干预决策。

### Q4: 论文做了哪些实验？

这篇论文是一篇概念性、理论性的研究，并未进行传统的实证实验或基准测试。论文的主要“验证”方式是通过**理论构建、模型阐述和示例说明**来展示其观点的合理性和实用性。具体而言：1) **模型构建与阐述**：论文系统地整合了来自人文、社会科学、HCI和工程学的多学科视角，严谨地定义了模型的核心组件（Scene, Context, Human Behavior Factors）及其相互关系，并提供了详细的图示（图1）。2) **示例演示**：论文通过一个日常情境的详细示例（用户下班后上公交车听音乐，见图2）来具体说明模型如何运作。该示例展示了同一个客观“场景”如何通过不同的“语境”（如个人压力状态、社会规范）被赋予不同意义，并最终解释了一个看似简单的“活动”如何成为寻求缓解压力的“行为”。3) **设计原则推导**：论文从概念模型中逻辑推导出五条具体的设计原则，并逐一解释了每条原则如何指导智能体设计，将抽象模型转化为可操作的设计指南。作者在讨论部分也明确指出，这项工作“主要是概念性的，尚未经过实证验证”，并建议未来研究应探索如何利用传感器数据和交互痕迹来操作化该模型，并检验其对行为预测和决策制定的贡献。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的未来研究方向。首先，也是最重要的，是**模型的实证验证与操作化**。当前模型是概念框架，需要研究如何将其转化为可计算的架构。这包括探索如何利用多模态传感器数据（视觉、音频、生理信号等）和用户交互日志来实例化“场景”和“语境”的各个维度，以及如何量化“人类行为因素”（如动机水平）。其次，需要开发**基于该模型的算法与系统**。未来的工作可以设计具体的AI代理架构，集成场景理解模块、上下文推理引擎和行为因素评估器，并实现论文提出的五条设计原则，例如开发动态调整干预时机的机制。第三，涉及**评估与基准测试**。需要建立新的评估指标和基准，不仅衡量代理的任务完成效率，更要评估其干预的适时性、相关性和对用户主体性的尊重程度。最后，论文的模型主要关注个体用户与代理的交互，未来可以将其扩展至**多智能体协作或社交场景**，研究在群体动态中，代理如何理解共享场景下的不同个体语境并进行协调。这些探索将把这一有价值的概念蓝图转化为实际可用的、真正人性化的Agentic AI系统。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了一个用于Agentic AI设计的、以人为中心的人类行为概念模型及其衍生的设计原则。论文指出，当前主动式AI智能体的主要瓶颈不在于感知信息，而在于理解用户行为背后的意义。为此，作者构建了一个三层模型：客观可观察的“场景”（Scene）、用户主观建构的“语境”（Context）以及决定行为可能性的“人类行为因素”（Human Behavior Factors）。行为被重新定义为这三者整合后的解释性结果，而非对场景的直接反应。基于此模型，论文提炼出五条关键设计原则：行为对齐、语境敏感、时间适当、动机校准和主体性保护，旨在指导智能体做出更明智、更体贴、更尊重用户的干预决策。这项工作为超越表面动作识别、迈向具有情境判断力的下一代Agentic AI系统提供了重要的理论基础和设计指南，强调了在AI代理设计中，理解“意义”与理解“事实”同等重要。
