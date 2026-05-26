---
title: "From Model Scaling to System Scaling: Scaling the Harness in Agentic AI"
authors:
  - "Shangding Gu"
date: "2026-05-25"
arxiv_id: "2605.26112"
arxiv_url: "https://arxiv.org/abs/2605.26112"
pdf_url: "https://arxiv.org/pdf/2605.26112v1"
github_url: "https://github.com/SafeRL-Lab/cheetahclaws"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent架构"
  - "系统扩展"
  - "上下文管理"
  - "可信记忆"
  - "动态技能路由"
  - "编排与治理"
  - "基准评测"
  - "开源平台"
relevance_score: 9.5
---

# From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

## 原始摘要

This paper studies the next major bottleneck in agentic AI as system scaling, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models. We refer to this shift as scaling the harness: treating the structured execution layer around a foundation model as a first-class object of design, evaluation, and optimization. Although recent large language models enable agents to use tools, retrieve information, maintain memory, and execute long-horizon workflows, evaluation remains largely model-centric, often reducing agents to final-task success while treating memory, retrieval, tool use, orchestration, verification, and governance as secondary implementation details. This framing is increasingly inadequate because agent performance emerges from the interaction among the foundation model, memory substrate, context constructor, skill-routing layer, orchestration loop, and verification-and-governance layer. Together, these components form the agent harness, which translates model capability into long-horizon agent behavior. We study scaling the harness through three core bottlenecks: context governance, trustworthy memory, and dynamic skill routing, together with the orchestration and governance mechanisms that coordinate and constrain them. We further outline a research agenda for harness-level benchmarks that go beyond one-shot task success to measure trajectory quality, memory hygiene, context efficiency, communication fidelity, verification cost, and safe evolution over time. To make the discussion concrete, we develop CheetahClaws: https://github.com/SafeRL-Lab/cheetahclaws, a Python-native reference harness, and compare it with Claude Code and OpenClaw. Our main claim is that future progress in agentic AI will depend as much on system design as on stronger foundation models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前智能体AI（Agentic AI）发展中一个被忽视的核心瓶颈：系统扩展（system scaling）问题，而不仅仅是模型扩展（model scaling）。研究背景是，近年来AI进步主要源于模型扩展（如更大的模型、更多的数据），但当基础模型被嵌入到工具、终端、浏览器、记忆存储和外部服务中时，其行为不再仅由模型决定，而是由整个系统决定——包括上下文如何构建、记忆如何检索、工具如何调用、子智能体如何路由、动作如何验证以及失败如何审计。

现有方法存在明显不足：当前评估体系仍以模型为中心，往往将智能体简化为最终任务的成功率，而将记忆、检索、工具使用、编排、验证和治理等视为次要的实现细节。这导致许多所谓“模型分数”实际上是“模型+系统”的混合分数，且难以反映长期行为中的可靠性差距。

本文的核心问题是：如何将智能体系统的结构化执行层（即“缰绳”，harness）——包括上下文治理、可信记忆、动态技能路由、编排与治理机制——作为一个一等对象来进行设计、评估和优化，从而推动智能体AI从模型扩展转向系统扩展，以实现更可靠、更高效、可审计的长期行为。

### Q2: 有哪些相关研究？

本文从系统扩展角度梳理了相关研究。在**方法类**工作中，ReAct、自教导工具调用等奠定了智能体推理-行动基础，Claude Code、Codex等实现了工具、子智能体、持久记忆的工程化，但多以模型变体为评估单位，忽视框架本身的可控性研究。SWE-agent通过精心设计工具模式提升基准性能，但同样聚焦模型层面。**应用类**研究包括检索增强生成（RAG）、MemGPT的分层记忆管理、Voyager的技能库演化，以及多智能体框架如AutoGen、MetaGPT、CAMEL，这些工作将记忆、检索、技能路由作为独立能力，而本文将其整合为上下文治理、记忆卫生和动态技能路由三大瓶颈。**评测类**方面，现有基准多侧重单次任务成功率，缺乏对轨迹质量、记忆效率、通信保真度等系统级指标的度量。本文的区别在于：将框架视为一等设计对象，通过CheetahClaws与Claude Code、OpenClaw的对比分析，强调未来进展依赖于系统架构设计而非仅模型扩展。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是**系统缩放**，即通过工程设计基础模型周围的结构化执行层（称为“马具”）来提升智能体的长期任务绩效，而非仅依赖模型本身的能力增强。其核心主张是，在模型能力达到足够水平后，系统设计（即系统缩放）将成为制约智能体性能的关键瓶颈。

论文设计了一个六组件的整体架构框架来描述智能体系统：推理基座 (ℛ)、记忆存储 (ℳ)、上下文构建器 (𝒞)、技能路由层 (𝒮)、编排循环 (𝒪) 以及验证与治理层 (𝒢)。模型缩放主要改进ℛ，而系统缩放则通过优化 ℳ、𝒞、𝒮、𝒪 和 𝒢 来提升系统级的性能，从而将模型能力转化为可靠的长期行为。

创新点在于识别并形式化了系统缩放中的三个核心瓶颈及其对应的系统级解决方案：
1.  **上下文治理 (𝒞)**：挑战不在于容量，而在于如何确保上下文的相关性、紧凑性、可追溯性和及时刷新。解决方案是将每次的上下文构建视为一个基于策略的选择过程，而非简单的固定缓冲区。
2.  **可信记忆 (ℳ)**：挑战在于存储信息的精准性、持久性和可验证性，核心威胁是“过时但自信”。解决方案是将信任度作为运行时决策的一部分，在检索时引入过时惩罚和置信度门控风险项，并主张将检索到的内容作为待验证的假设。
3.  **动态技能路由 (𝒮)**：挑战在于如何为特定任务选择性、可组合地调用正确的技能，并对其输出进行验证。解决方案是将路由视为一个可学习的策略，并在每一步都耦合显式的后置条件检查，从而将 𝒮 与 𝒢 紧密绑定。

此外，论文开发了一个名为 **CheetahClaws** 的开源 Python 参考实现，与 Claude Code 和 OpenClaw 进行对比，展示了针对不同部署优先级（生产级、个人助手、研究）的差异化设计，从而验证了系统缩放的具体工程实践。

### Q4: 论文做了哪些实验？

论文通过在三个核心瓶颈（上下文治理、可信记忆、动态技能路由）上设计实验，评估系统级扩展对智能体性能的影响。实验设置包括使用自研的Python原生参考实现CheetahClaws，并与Claude Code和OpenClaw进行对比。数据集/基准测试包括SWE-bench（可执行仓库级任务）、AgentBench（多环境交互）、WebArena（浏览器代理）和Terminal-Bench（终端任务）等，同时引入新的评估维度，如轨迹质量、记忆卫生、上下文效率、通信保真度、验证成本和长期安全演化。主要结果包括：在Anthropic的内部研究评估中，多智能体系统（Claude Opus 4主导智能体搭配Claude Sonnet 4子智能体）比单智能体Claude Opus 4性能提升90.2%；在基于BrowseComp的分析中，令牌使用量单独解释了80%的性能差异，结合工具调用次数和模型选择后可解释方差达到95%。实验揭示了系统设计因素（如路由策略、记忆管理）对智能体长期行为的显著影响，且多智能体架构的有效性更多源于系统层面的并行上下文窗口利用和任务分解，而非自动协作。论文强调，当前评估主要是模型中心化的单次任务成功指标，未能捕捉过程指标（如令牌数、工具调用、重试次数、审计性）和长期演化性质（如记忆污染、漂移、奖励黑客），因此提出需要系统级基准来测量这些维度，以区分模型能力与系统设计的贡献。

### Q5: 有什么可以进一步探索的点？

尽管论文提出了系统级扩展（Harness Scaling）的核心论点，但仍存在若干可深入探索的方向。首先，论文承认了反对观点，但未充分验证“更强模型是否真能内化系统问题”——例如，未来具备无限上下文的模型可能天然解决记忆治理问题，因此需要对比实验明确模型与系统设计的边界效应。其次，当前CheetahClaws作为参考实现，其模块化设计（如内存、工具路由、校验层）的通用性和迁移性仍需验证：不同任务领域（如医疗、金融）对治理策略的敏感性差异可能要求不同的架构折衷。此外，论文提出的轨迹质量、内存卫生等新指标缺乏标准化定义与可行性分析，例如如何量化“通信保真度”或“验证成本”仍悬而未决。未来可探索：1) 设计可解释的自动消融框架，量化每个系统组件（如上下文构造器）对任务成功率的独立贡献；2) 研究跨异构环境（如动态API、多代理协作）的自适应路由策略，取代静态规则；3) 开发轻量级模拟器，以可控成本快速验证治理策略（如权限回溯）的安全性与效率。最终，需警惕“过设计”风险——过度复杂的系统架构可能抵消模型自身的学习能力，因此平衡端到端学习与显式模块化的混合范式值得关注。

### Q6: 总结一下论文的主要内容

这篇论文提出，智能体AI的下一个主要瓶颈已从模型扩展转向系统扩展，即围绕基础模型构建可审计、持久、模块化和可验证的架构。当前评估仍以模型为中心，而智能体性能实际上源于基础模型与“系统 harness”（包括记忆、上下文构建、技能路由、编排、验证与治理等组件）的交互。论文通过三大核心瓶颈（上下文治理、可信记忆和动态技能路由）研究“扩展系统 harness”的重要性，并提出了一个将基础模型推理与系统因素分离的框架。为验证该观点，论文开发了开源参考系统 CheetahClaws，并与 Claude Code 和 OpenClaw 进行比较，发现相同模型在不同系统上会产生定性差异。论文主张，未来智能体AI的进步将同等依赖于系统设计和更强的模型，评估基准应超越单次任务成功，衡量轨迹质量、记忆卫生、上下文效率等过程级属性。
