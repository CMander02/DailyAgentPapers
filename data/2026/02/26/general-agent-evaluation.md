---
title: "General Agent Evaluation"
authors:
  - "Elron Bandel"
  - "Asaf Yehudai"
  - "Lilach Eden"
  - "Yehoshua Sagron"
  - "Yotam Perlitz"
  - "Elad Venezian"
  - "Natalia Razinkov"
  - "Natan Ergas"
  - "Shlomit Shachor Ifergan"
  - "Segev Shlomov"
  - "Michal Jacovi"
  - "Leshem Choshen"
  - "Liat Ein-Dor"
  - "Yoav Katz"
  - "Michal Shmueli-Scheuer"
date: "2026-02-26"
arxiv_id: "2602.22953"
arxiv_url: "https://arxiv.org/abs/2602.22953"
pdf_url: "https://arxiv.org/pdf/2602.22953v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Benchmark"
  - "General-Purpose Agent"
  - "Agent Framework"
  - "Agent Leaderboard"
  - "Agent Protocol"
relevance_score: 8.5
---

# General Agent Evaluation

## 原始摘要

The promise of general-purpose agents - systems that perform tasks in unfamiliar environments without domain-specific engineering - remains largely unrealized. Existing agents are predominantly specialized, and while emerging implementations like OpenAI SDK Agent and Claude Code hint at broader capabilities, no systematic evaluation of their general performance has been pursued. Current agentic benchmarks assume domain-specific integration, encoding task information in ways that preclude fair evaluation of general agents. This paper frames general-agent evaluation as a first-class research objective. We propose conceptual principles for such evaluation, a Unified Protocol enabling agent-benchmark integration, and Exgentic - a practical framework for general agent evaluation. We benchmark five prominent agent implementations across six environments as the first Open General Agent Leaderboard. Our experiments show that general agents generalize across diverse environments, achieving performance comparable to domain-specific agents without any environment-specific tuning. We release our evaluation protocol, framework, and leaderboard to establish a foundation for systematic research on general-purpose agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决通用智能体（General-Purpose Agents）缺乏系统性评估标准的核心问题。研究背景是，尽管AI智能体在诸多领域（如软件工程、网页导航）展现出强大能力，但当前进展主要依赖于针对特定领域的专门化设计和手动调优。然而，现实世界的异构环境迫切需要能够在不进行领域特定工程的情况下，直接部署并完成陌生任务的通用智能体。

现有方法的不足主要体现在评估体系上。当前主流的智能体评测基准（如SWEBench、Tbench）本质上是为领域特定智能体设计的。它们存在两大局限：一是使用定制化的通信协议，二是默认智能体已预先知晓评测任务的具体目标和环境语义。这导致它们无法对通用智能体进行公平评估。近期的一些整合框架（如Browsergym、Harbor）虽然将多个基准统一到单一领域内，但仍强制使用单一协议（如Web或CLI），迫使通用智能体必须适配评测框架的接口，这相当于评估了一个功能被削弱的智能体版本，无法真实反映其原生能力和通用性。

因此，本文要解决的核心问题是：如何为通用智能体建立一套系统、公平且标准化的评估方法论。论文将通用智能体评估确立为一个首要的研究目标，旨在填补该领域系统性评估的空白。具体而言，论文提出了评估通用智能体的概念性原则、一个实现智能体与各类基准无缝对接的统一协议，以及一个名为Exgentic的实践性评估框架。通过这套体系，论文首次对多个主流通用智能体实现进行了跨六个环境的基准测试，并发布了首个“开放通用智能体排行榜”，以期为通用智能体的研究与发展奠定基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体评测领域展开，可分为以下类别：

**领域专用智能体评测基准**：当前研究已针对软件工程、客户服务、科学探索等具体领域建立了大量专用评测基准。这些基准通常定义了领域特定的协议与任务规范，但要求智能体针对每个基准进行专门适配，无法公平评估通用智能体的跨领域能力。

**评测基础设施统一化尝试**：部分工作如HAL尝试统一不同基准的基础设施，但仍需针对每个基准进行智能体适配。BrowserGym和Harbor通过固定交互协议（如网页/命令行）实现了标准化，但将评估限制在单一环境类型中，缺乏跨环境泛化能力的检验。

本文与上述研究的核心区别在于：现有工作均假设智能体需进行领域特定集成，或将任务信息以特定方式编码，这阻碍了对通用智能体的公平评估。本文首次将通用智能体评估确立为独立研究目标，提出跨环境评估的概念原则、支持智能体-基准无缝集成的统一协议，以及可实践的评估框架Exgentic，最终通过跨六个环境评测五个主流智能体构建了首个开放通用智能体排行榜，系统性推进了通用智能体的评估研究。

### Q3: 论文如何解决这个问题？

论文通过提出一套系统性的评估框架来解决通用智能体缺乏公平、统一评测标准的问题。其核心方法是构建一个名为 **Exgentic** 的实践框架，并辅以一个**统一协议**，旨在将通用智能体与各种现有基准测试环境无缝集成。

整体框架包含几个关键部分：
1.  **概念原则**：首先确立了通用智能体评估应遵循的基本原则，例如评估必须在智能体未经特定环境调优的情况下进行，且任务信息不应以特定领域的方式编码，以确保公平性。
2.  **统一协议**：这是一个核心创新点，它定义了一套标准化的接口和交互规范。该协议充当了“适配器”的角色，使得原本为特定领域设计的多样化基准测试环境能够以统一的方式与不同的通用智能体进行对接，从而解决了现有基准“假定领域特定集成”而无法公平评估通用智能体的问题。
3.  **Exgentic 框架**：作为上述协议的具体实现，它是一个实用的软件框架。其主要模块包括智能体封装器、环境适配器、任务执行引擎和评估指标计算器。框架负责管理智能体与环境的交互生命周期，自动执行任务序列，并收集性能数据。

其创新点在于首次将通用智能体评估本身提升为一个独立的研究目标，并提供了从理论原则到实践工具的全栈解决方案。通过这套方法，论文成功地对五种主流智能体实现（如 OpenAI SDK Agent, Claude Code）在六个不同环境中进行了基准测试，创建了首个“开放通用智能体排行榜”，实证表明通用智能体在未经调优的情况下，其表现可媲美领域专用智能体。

### Q4: 论文做了哪些实验？

论文实验旨在系统评估通用智能体在不同环境下的性能。实验设置方面，评估了5种智能体架构（包括ReAct、smol CodeAgent、OpenAI Solo + MCP、Claude Code等），结合3种前沿大语言模型（GPT、Opus、Gemini Pro），在6个基准环境中进行测试，每个环境包含100个任务，共计90种配置。实验采用统一协议（Unified Protocol）和Exgentic框架进行集成。

使用的数据集/基准测试包括：BrowseComp（复杂信息搜索任务）、Tbench（零售、航空、电信领域的客服任务）、SWEBench（500个真实世界软件工程任务）、AppWorld（日常数字任务助手）。对比方法涉及不同智能体架构与模型的组合，主要评估其在无需环境特定调优下的表现。

关键数据指标包括：成功率（Success Rate）、每任务平均成本（Cost per Task）、平均步骤数（Average Steps）。主要结果显示，Opus模型整体表现最佳，平均成功率为0.66，Gemini为0.60，GPT为0.40。模型选择解释了28.2%的性能方差，而智能体架构仅解释0.6%。在特定基准上，通用智能体与领域专用智能体性能相当，例如在SWEBench上，Solo + Opus配置达到0.81的成功率，接近原领域专用智能体的0.79。成本效率方面，GPT配置最具优势，但高性能配置（如Solo + Opus）成本高出30倍。实验还发现，失败任务通常比成功任务消耗更多交互步骤，平均增加20%至54%，凸显了可靠性对成本的影响。

### Q5: 有什么可以进一步探索的点？

该论文为通用智能体评估奠定了重要基础，但仍存在若干局限性和未来可探索的方向。首先，评估的基准环境虽具多样性，但任务类型和复杂度仍有局限，未来需纳入更开放、动态和长周期的真实世界任务（如复杂项目管理、跨平台协作），以检验智能体在模糊指令、异常处理和长期规划方面的能力。其次，研究发现模型质量是性能主导因素，而智能体架构影响甚微，这提示当前架构创新可能未触及核心。未来可探索能更有效利用基础模型能力的新型架构范式，例如，设计具有元认知能力的组件，使智能体能动态评估自身置信度并调整决策策略，或开发能跨任务迁移学习技能的记忆模块。此外，成本与性能的权衡极为显著，未来研究需致力于提升效率，例如通过轻量级模型微调、动作压缩或提前终止机制来降低交互成本。最后，论文指出失败任务通常耗时更长，这启示未来可深入研究智能体的“故障模式”，构建细粒度的错误分类体系，并设计针对性的恢复机制，从而提升其鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

本文聚焦于通用智能体（能在陌生环境中执行任务而无需领域特定工程）的性能评估问题，指出当前缺乏对其通用能力的系统性评测。现有基准测试通常假设领域特定集成，其任务信息编码方式不利于公平评估通用智能体。为此，论文将通用智能体评估确立为首要研究目标，并提出了三项核心贡献：一是为通用评估建立了概念性原则；二是设计了一个支持智能体与基准无缝集成的统一协议；三是开发了名为Exgentic的实践性评估框架。基于此，作者首次构建了开放通用智能体排行榜，在六个环境中对五种主流智能体实现进行了基准测试。实验结果表明，通用智能体能在多样环境中实现良好泛化，其性能在未经任何环境特定调优的情况下，可媲美领域专用智能体。论文通过公开评估协议、框架和排行榜，为系统化研究通用智能体奠定了重要基础。
