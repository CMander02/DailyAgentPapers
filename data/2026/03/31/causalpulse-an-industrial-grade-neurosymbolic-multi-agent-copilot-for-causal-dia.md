---
title: "CausalPulse: An Industrial-Grade Neurosymbolic Multi-Agent Copilot for Causal Diagnostics in Smart Manufacturing"
authors:
  - "Chathurangi Shyalika"
  - "Utkarshani Jaimini"
  - "Cory Henson"
  - "Amit Sheth"
date: "2026-03-31"
arxiv_id: "2603.29755"
arxiv_url: "https://arxiv.org/abs/2603.29755"
pdf_url: "https://arxiv.org/pdf/2603.29755v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Neurosymbolic"
  - "Tool Use"
  - "Industrial Application"
  - "Real-time Systems"
  - "Causal Reasoning"
relevance_score: 7.5
---

# CausalPulse: An Industrial-Grade Neurosymbolic Multi-Agent Copilot for Causal Diagnostics in Smart Manufacturing

## 原始摘要

Modern manufacturing environments demand real-time, trustworthy, and interpretable root-cause insights to sustain productivity and quality. Traditional analytics pipelines often treat anomaly detection, causal inference, and root-cause analysis as isolated stages, limiting scalability and explainability. In this work, we present CausalPulse, an industry-grade multi-agent copilot that automates causal diagnostics in smart manufacturing. It unifies anomaly detection, causal discovery, and reasoning through a neurosymbolic architecture built on standardized agentic protocols. CausalPulse is being deployed in a Robert Bosch manufacturing plant, integrating seamlessly with existing monitoring workflows and supporting real-time operation at production scale. Evaluations on both public (Future Factories) and proprietary (Planar Sensor Element) datasets show high reliability, achieving overall success rates of 98.0% and 98.73%. Per-criterion success rates reached 98.75% for planning and tool use, 97.3% for self-reflection, and 99.2% for collaboration. Runtime experiments report end-to-end latency of 50-60s per diagnostic workflow with near-linear scalability (R^2=0.97), confirming real-time readiness. Comparison with existing industrial copilots highlights distinct advantages in modularity, extensibility, and deployment maturity. These results demonstrate how CausalPulse's modular, human-in-the-loop design enables reliable, interpretable, and production-ready automation for next-generation manufacturing.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能制造领域中实时、可信且可解释的根因诊断自动化问题。随着制造系统日益依赖密集、异构的传感器和自动化产线，在严格的质量与产量约束下维持连续运行变得至关重要。传统分析流程通常将异常检测、因果推断和根因分析视为孤立的阶段，导致可扩展性和可解释性受限。现有方法多采用黑箱模型处理传感器数据，由专家人工解读警报并进行临时干预，这造成了诊断延迟、可追溯性差以及操作人员信任度降低。此外，由于生产数据多模态且不完整、因果关系部分已知且依赖上下文，以及需要可解释、可审计、人机协同的系统以确保安全与责任，可靠的根因分析仍然面临挑战。

当前工业级辅助系统与诊断平台缺乏一个统一的、基于标准的多智能体框架，无法有效整合预处理与多模态数据、利用领域规则约束因果分析、生成透明可解释的结果、支持运行时操作人员驱动的选择与审查，以及轻松扩展至新用例。因此，本文的核心问题是设计并实现一个模块化、可互操作且可组合的神经符号多智能体辅助系统，以自动化完成从异常检测到因果发现再到根因推理的完整诊断流程，实现实时、可靠且人机协同的因果诊断。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**智能体AI框架与编排协议**以及**工业与诊断副驾驶系统**。

在**智能体AI框架与编排协议**方面，相关工作如LangGraph、AutoGen、CrewAI和OpenDevin等框架，以及MCP、Agent Communication Protocol等协议，为智能体间的工具调用、规划和通信提供了标准化接口。这些工作为构建多智能体系统奠定了基础。CausalPulse与它们的关系在于采纳并利用了这类标准化协议来实现其多智能体编排，但其区别在于专门针对工业因果诊断场景进行了深度定制和集成，形成了一个完整的、面向生产的解决方案。

在**工业与诊断副驾驶系统**方面，相关工作包括UCSD Causal Copilot、MATMCD、IBM AssetOpsBench和SmartPilot等。这些系统也采用多智能体或模块化架构，用于工业监控、因果发现或预测性维护。CausalPulse与这些工作目标相似，均旨在实现工业自动化诊断。然而，本文指出，现有系统通常在可扩展性、语义上下文整合、领域先验知识利用以及神经符号推理方面存在局限，且往往将异常检测、因果发现和根因分析等阶段割裂。CausalPulse的核心区别与贡献在于，它提出了一个**统一的、神经符号架构的多智能体框架**，将数据预处理、异常检测、因果发现和根因分析无缝集成在一个可解释的、支持动态编排和人机交互的体系结构中，从而解决了现有系统模块化、可扩展性和部署成熟度方面的不足。

### Q3: 论文如何解决这个问题？

CausalPulse 通过构建一个工业级的神经符号多智能体协同系统来解决智能制造中实时、可信且可解释的因果诊断问题。其核心方法是采用一个统一的、模块化的四层架构，将异常检测、因果发现和根因分析等传统上孤立的阶段整合到一个自动化的工作流中。

**整体框架与主要模块：**
系统采用四层框架：1) **用户层**：提供基于浏览器的交互界面，支持人在回路的决策。2) **智能体层**：包含通用智能体和专用于因果诊断任务的专用智能体，均实现为FastAPI微服务，并通过基于注册表的A2A通信进行协调。3) **工具层**：提供支撑智能体操作的MCP工具、服务和资源，如过程本体、LLM、知识图谱、技术手册和规则库。4) **数据层**：整合来自信息物理系统的异构数据（传感器日志、图像、事件元数据等）。连接各层的是标准化协议（MCP、A2A和LangGraph）。

关键智能体组件包括：
*   **客户端进程智能体**：作为主要协调器，规范化用户输入，并根据任务标签调度到相应工具。
*   **预处理智能体**：执行确定性的数据清洗和标准化。
*   **背景信息智能体**：提供变量级别的语义描述，为诊断增添领域知识。
*   **异常检测智能体**：封装多策略管道（如跨模态融合模型、阈值规则、隔离森林），检测到异常后自动触发根因分析。
*   **因果发现智能体**：以模式感知、知识注入的方式从数据中推导候选因果结构。它根据数据类型选择算法（如PC或GES），并利用领域特定规则（如控制/观察类型、过程顺序）约束结构学习，确保只考虑物理上合理的因果边。
*   **根因分析智能体**：执行因果归因，封装ProRCA分析管道，输出结构化的、排序的根因解释。
*   **推荐智能体**：基于规则启发式，为操作员或自动规划器提供上下文感知的下一步指导。

**工作流与创新点：**
系统工作流由基于LangGraph的工作流引擎驱动，分为三个阶段：1) 智能体卡注册；2) 动态任务分解与执行（规划器、执行器、重规划器协同）；3) 后处理链式调用。其创新点主要体现在：
1.  **神经符号架构**：将神经组件（如LLM用于规划、多模态异常检测）与符号组件（领域规则、过程本体、约束因果发现）深度融合，实现了从数据中学习的同时受领域知识约束。
2.  **标准化与模块化设计**：基于MCP、A2A等标准化协议，以及智能体卡的注册发现机制，实现了高度的模块化和即插即用扩展性，允许无缝集成新数据源、工具和智能体。
3.  **动态、自适应的工作流**：工作流引擎能根据实时结果（如未检测到异常则跳过后续步骤）和推荐智能体的建议，动态重规划执行路径，实现上下文感知的连续推理。
4.  **端到端的可解释性与可追溯性**：通过分层架构、清晰的接口以及从原始数据到最终决策的完整状态记录，确保了整个诊断过程的透明度和可追溯性。

综上所述，CausalPulse通过其分层神经符号多智能体架构、标准化的互操作协议以及动态自适应的工作流，将因果诊断的各个环节有机统一，从而实现了可靠、可解释且可投入生产的自动化。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估，主要涵盖以下几个方面：

**实验设置与数据集**：实验使用了两个数据集。一是专有的平面传感器元件（PSE）数据集，来自博世安德森工厂的研磨工艺，包含26个变量。二是公开的未来工厂（FF）数据集，模拟火箭装配线，包含21个操作状态和多种传感器数据。系统部署在MacBook Pro（M1 Pro芯片）上进行测试。

**评估方法与主要结果**：实验核心是评估CausalPulse的多智能体核心能力，通过9个预定义的工作流（如W1-W9）进行测试。评估了四个智能体准则：
1.  **规划能力**：评估将用户意图分解为正确子任务序列的能力。在PSE和FF数据集上的成功率分别为98.75%和98.12%。
2.  **工具使用**：评估正确调用工具的能力。成功率分别为98.75%（PSE）和98.1%（FF）。
3.  **自我反思**：评估系统内省和重用中间结果的能力。两个数据集的成功率均为97.3%，重复计算减少了约22%。
4.  **多智能体协作**：评估智能体间协调与信息交换。成功率分别为99.2%（PSE）和98.3%（FF）。

**关键数据指标**：
*   **整体成功率**：PSE数据集为98.73%，FF数据集为98.0%。
*   **运行时性能**：端到端诊断工作流延迟为53-60秒（PSE约53秒，FF约60秒）。系统展示出近线性的可扩展性（R²=0.97）。
*   **根因归因质量**：使用PRORCA组件进行评估，在PSE数据集上，Hits@1为0.44，Hits@2为0.65；平均精确率、召回率和F1分数分别为0.46、0.40和0.39。

**对比方法**：论文将CausalPulse与现有的工业副驾驶进行了比较，突出了其在模块化、可扩展性和部署成熟度方面的优势。虽然没有列出具体竞品的量化对比数据，但强调了其独特的神经符号架构和标准化智能体协议带来的可靠性。

### Q5: 有什么可以进一步探索的点？

该论文展示了CausalPulse在特定生产线部署的成功，但其局限性在于验证场景相对单一（仅Bosch工厂和两个数据集），未来可探索更广泛的制造场景（如离散装配、化工流程）以验证通用性。神经符号架构虽提升了可解释性，但符号规则的维护与知识更新依赖人工，未来可研究如何实现因果知识的自动演化与增量学习。此外，系统延迟为50-60秒，对于毫秒级响应的极端实时场景（如高精度冲压）可能不足，需优化算法并行性与边缘计算部署。从多智能体协作角度看，当前智能体角色和协议固定，可引入动态角色分配与联邦学习机制，使系统能自适应不同故障复杂度。最后，论文未深入讨论人机回环中操作员的认知负荷问题，未来可集成AR/VR界面与自然语言对话，进一步降低使用门槛并增强协同诊断的沉浸感。

### Q6: 总结一下论文的主要内容

该论文提出了CausalPulse，一个面向智能制造因果诊断的工业级神经符号多智能体协同系统。核心问题是解决传统分析流程将异常检测、因果推断和根因分析割裂，导致可扩展性和可解释性受限的挑战。方法上，它基于标准化智能体协议构建了一个神经符号架构，统一了异常检测、因果发现与推理，实现了模块化、可扩展的多智能体协作。主要结论显示，系统在公开和专有数据集上均表现出高可靠性（总体成功率98.0%和98.73%），各环节成功率优异，端到端延迟为50-60秒且具近线性扩展能力，已成功部署于博世工厂。其意义在于通过人机回环的模块化设计，为下一代制造业提供了可靠、可解释且可直接投入生产的自动化诊断方案，在模块化、可扩展性和部署成熟度上优于现有工业协同系统。
