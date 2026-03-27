---
title: "FluxEDA: A Unified Execution Infrastructure for Stateful Agentic EDA"
authors:
  - "Zhengrui Chen"
  - "Zixuan Song"
  - "Yu Li"
  - "Qi Sun"
  - "Cheng Zhuo"
date: "2026-03-26"
arxiv_id: "2603.25243"
arxiv_url: "https://arxiv.org/abs/2603.25243"
pdf_url: "https://arxiv.org/pdf/2603.25243v1"
categories:
  - "cs.AR"
  - "cs.AI"
tags:
  - "Agent Infrastructure"
  - "Tool Use"
  - "State Management"
  - "EDA Automation"
  - "Iterative Execution"
  - "Application-Specific Agent"
relevance_score: 7.5
---

# FluxEDA: A Unified Execution Infrastructure for Stateful Agentic EDA

## 原始摘要

Large language models and autonomous agents are increasingly explored for EDA automation, but many existing integrations still rely on script-level or request-level interactions, which makes it difficult to preserve tool state and support iterative optimization in real production-oriented environments. In this work, we present FluxEDA, a unified and stateful infrastructure substrate for agentic EDA. FluxEDA introduces a managed gateway-based execution interface with structured request and response handling. It also maintains persistent backend instances. Together, these features allow upper-layer agents and programmable clients to interact with heterogeneous EDA tools through preserved runtime state, rather than through isolated shell invocations. We evaluate the framework using two representative commercial backend case studies: automated post-route timing ECO and standard-cell sub-library optimization. The results show that FluxEDA can support multi-step analysis and optimization over real tool contexts, including state reuse, rollback, and coordinated iterative execution. These findings suggest that a stateful and governed infrastructure layer is a practical foundation for agent-assisted EDA automation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在电子设计自动化（EDA）领域，如何为基于大型语言模型和自主智能体的自动化系统构建一个统一、有状态且可靠的基础设施层的问题。随着芯片设计复杂度激增，EDA工具链的集成和运维高度依赖人工脚本，重复且易错。尽管AI智能体为自动化带来了新机遇，但现有方法（如ChatEDA等）通常仅通过脚本级或请求级的批量交互来连接智能体与EDA工具，每次调用都是独立的shell命令，导致工具运行时状态无法保持，形成“黑盒”式的一次性执行。这种模式使得智能体难以在真实的、面向生产的设计环境中进行需要多步迭代、状态复用和精细优化的任务（如时序修复和单元库优化）。同时，现有框架缺乏严格的运行时治理，让LLM直接生成和执行脚本存在命令幻觉、状态损坏和工具崩溃的风险，无法满足工业级可靠性要求。因此，本文的核心问题是：如何构建一个基础设施，既能标准化异构EDA工具的访问接口，又能维持其持久化的运行时状态，从而支持智能体在真实工具上下文中进行连续、可回溯、可协调的迭代分析与优化，并确保执行过程的安全可控。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，早期工作如ChatEDA尝试利用大语言模型生成特定工具脚本来实现自动化，但这种方式通常基于一次性脚本或请求级别的交互，难以维持工具状态。近期研究如MCP4EDA和AutoEDA引入了Model Context Protocol（MCP）或微服务概念，旨在降低异构EDA工具的集成复杂度。然而，这些框架大多仍通过生成命令和后处理日志解析来耦合智能体与EDA引擎，缺乏对持久化、结构化工具状态的支持。

在应用类研究中，现有工作主要关注利用智能体编排EDA工作流，但通常局限于脚本级别的批处理交互，无法在真实的工具上下文中进行细粒度、连续的优化。此外，这些方法在工业环境中存在可靠性风险，如幻觉命令和状态损坏，缺乏严格的语义边界和运行时治理。

本文提出的FluxEDA与这些工作的主要区别在于，它提供了一个统一且有状态的基础设施层，通过基于网关的架构和持久化后端实例，支持上层智能体与异构EDA工具通过保留的运行时状态进行交互，而非孤立的Shell调用。同时，FluxEDA引入了领域特定的Skills层，将低层工具访问与高层工作流知识分离，从而支持在真实生产环境中进行多步骤分析和迭代优化。

### Q3: 论文如何解决这个问题？

FluxEDA通过构建一个统一且有状态的执行基础设施来解决传统脚本级或请求级交互中难以保持工具状态、支持迭代优化的问题。其核心方法是设计一个分层架构，在客户端与后端EDA工具之间插入一个通用的执行栈，从而提供跨工具的持久化执行模型。

整体框架分为五层：访问层、通信层、网关层、EDA工具适配层和运行时管理层。主要模块包括：1）**结构化RPC客户端与会话管理器**，负责将代理请求封装为携带目标方法、参数和元数据的结构化消息，并通过统一路径转发；2）**受控网关**，作为核心调度组件，在执行前进行协议验证、注册表查找、参数检查和能力授权，仅解析已注册的`api_*`方法，明确执行边界；3）**能力发现机制**，通过内省API（如`api_ping`、`api_list_method`）渐进式暴露工具能力，避免一次性加载所有方法描述，节省LLM代理的上下文预算；4）**工具适配器**，将原生工具能力通过一致的调用接口暴露，将工具特定的命令语义、状态模型和报告格式差异封装在注册方法之后；5）**运行时管理层**，管理后端实例的生命周期，包括进程启动、实例绑定与路由、端口分配、活跃度监控以及清理回收。

创新点主要体现在：首先，**持久化实例执行模型**，为每个工具进程分配`instance_id`作为路由句柄，允许多个请求复用同一活动实例，保持加载的设计和内部工具上下文，支持跨调用的状态保留、回滚和协调迭代执行，这与将每个请求视为独立shell调用的传统方式截然不同。其次，**统一通信契约**，为调用、内省和结果交付提供一致的结构化路径，使上层自动化与可执行接口对齐，减少对工具特定shell约定的依赖。最后，**分离的工作流知识处理**，通过领域特定的“技能”（Skills）来指导能力选择和调用顺序，而不加重协议层本身的负担。

通过这些设计，FluxEDA能够支持多步骤分析和优化任务，例如在案例研究中展示的自动布线后时序ECO和标准单元子库优化，实现了在真实工具上下文中的状态重用和迭代执行。

### Q4: 论文做了哪些实验？

论文通过两个案例研究评估了FluxEDA框架。实验设置方面，系统采用GPT-5.4作为主要大语言模型，并使用OpenAI Codex框架实现智能体编排。实验在商业EDA环境中进行，旨在验证框架对持久化工具会话中多步骤优化的支持。

第一个案例研究是自动布线后时序ECO优化。任务基于一个具有140条违反路径的设计，初始建立时间WNS/TNS为-0.81/-37.37 ns，保持时间WHS/THS为-0.39/-1.33 ns。智能体通过迭代优化：第一次迭代通过默认单元尺寸调整，将建立时间WNS改善至-0.76 ns，TNS改善至-34.78 ns，违反路径降至130条；第二次迭代尝试更激进的设置但效果不佳，系统随即回滚至第一次迭代状态；第三次迭代进行针对性保持时间修复，将保持时间WHS提升至+0.01 ns，THS归零，消除了所有保持时间违规。

第二个案例研究是标准单元子库优化。实验从全库基线开始（面积14,651.55 μm²，WNS/TNS为-0.246/-20.996 ns）。通过面积驱动探索，找到低面积点A-Run9（面积12,530.89 μm²，但WNS/TNS恶化至-1.114/-186.934 ns）。随后通过时序恢复阶段，最终得到方案T-Run11，面积13,659.95 μm²，WNS/TNS为-0.448/-40.306 ns，仅使用36个具体单元引用和23个单元族。相比基线，单元引用和单元族数量分别减少75.8%和54.9%，同时从A-Run9恢复了88.4%的TNS差距。

主要结果表明，FluxEDA能够支持跨工具状态的迭代分析、回滚和协调执行，实现了持续的“分析-执行-优化”循环。

### Q5: 有什么可以进一步探索的点？

基于论文内容，FluxEDA的核心贡献在于构建了一个有状态的、统一的基础设施层，以支持EDA工具与上层智能体之间的持续交互。然而，该工作仍存在一些局限性和值得深入探索的方向。

首先，论文的评估仅基于两个具体的商业后端案例（时序ECO和标准单元子库优化）。其通用性和可扩展性有待在更广泛的EDA流程（如逻辑综合、物理设计、验证）中进行验证。未来研究可以探索将该框架适配到更多样化、更复杂的异构工具链中。

其次，FluxEDA侧重于基础设施层，对“上层智能体”的决策与规划能力涉及较少。一个重要的探索方向是如何让智能体更有效地利用这个有状态基础设施。例如，开发能主动学习工具状态、自动进行状态回滚或尝试不同优化路径的高级规划算法，或者研究多智能体如何在此基础设施上协同工作以解决更复杂的EDA问题。

此外，论文提到了状态持久化和回滚，但对于执行过程中的错误处理、异常恢复以及安全与权限的精细化管理可能论述不足。未来的改进可以加强基础设施的鲁棒性，例如引入更完善的检查点机制、对工具执行进行沙箱隔离，或设计细粒度的访问控制策略，以应对生产环境中对可靠性和安全性的高要求。

最后，从长期看，该方向可与“AI for EDA”更紧密地结合。基础设施不仅可以保存工具状态，还可以持续收集高质量的过程数据（如每次迭代的决策、工具输出和最终结果），用于训练更专业、更高效的领域特定智能体，从而形成从基础设施到应用算法的正向循环。

### Q6: 总结一下论文的主要内容

该论文提出了FluxEDA，一个面向电子设计自动化（EDA）的、支持状态保持的统一智能体执行基础设施。针对现有基于大语言模型的EDA自动化方案多依赖脚本级或请求级交互、难以维持工具状态和迭代优化的问题，FluxEDA的核心贡献是设计了一个有状态、可治理的基础设施层。其方法包括引入一个基于托管网关的执行接口，处理结构化请求与响应，并维护持久化的后端工具实例。这使得上层智能体或可编程客户端能够通过保持的运行时状态与异构EDA工具交互，而非通过孤立的命令行调用。论文通过两个商用后端案例（自动布线后时序ECO和标准单元子库优化）进行评估，结果表明FluxEDA能支持在真实工具上下文中进行多步骤分析与优化，包括状态复用、回滚和协同迭代执行。该工作为智能体辅助的EDA自动化提供了一个实用且可扩展的工程基础。
