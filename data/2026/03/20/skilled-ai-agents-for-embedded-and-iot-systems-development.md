---
title: "Skilled AI Agents for Embedded and IoT Systems Development"
authors:
  - "Yiming Li"
  - "Yuhan Cheng"
  - "Mingchen Ma"
  - "Yihang Zou"
  - "Ningyuan Yang"
  - "Wei Cheng"
  - "Hai \"Helen\" Li"
  - "Yiran Chen"
  - "Tingjun Chen"
date: "2026-03-20"
arxiv_id: "2603.19583"
arxiv_url: "https://arxiv.org/abs/2603.19583"
pdf_url: "https://arxiv.org/pdf/2603.19583v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Framework"
  - "Tool Use"
  - "Benchmark"
  - "Embedded Systems"
  - "IoT"
  - "Hardware-in-the-Loop"
  - "Skill Learning"
relevance_score: 7.5
---

# Skilled AI Agents for Embedded and IoT Systems Development

## 原始摘要

Large language models (LLMs) and agentic systems have shown promise for automated software development, but applying them to hardware-in-the-loop (HIL) embedded and Internet-of-Things (IoT) systems remains challenging due to the tight coupling between software logic and physical hardware behavior. Code that compiles successfully may still fail when deployed on real devices because of timing constraints, peripheral initialization requirements, or hardware-specific behaviors. To address this challenge, we introduce a skills-based agentic framework for HIL embedded development together with IoT-SkillsBench, a benchmark designed to systematically evaluate AI agents in real embedded programming environments. IoT-SkillsBench spans three representative embedded platforms, 23 peripherals, and 42 tasks across three difficulty levels, where each task is evaluated under three agent configurations (no-skills, LLM-generated skills, and human-expert skills) and validated through real hardware execution. Across 378 hardware validated experiments, we show that concise human-expert skills with structured expert knowledge enable near-perfect success rates across platforms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将大型语言模型（LLM）和智能体系统应用于嵌入式与物联网（IoT）系统开发时所面临的独特挑战。研究背景是，尽管LLM在自动化软件开发方面展现出潜力，但在涉及真实物理硬件的硬件在环（HIL）嵌入式开发中，由于软件逻辑与硬件行为紧密耦合，成功编译的代码在真实设备上部署时仍可能因时序约束、外设初始化要求或硬件特定行为而失败。

现有方法存在明显不足。一方面，一些方法通过向智能体提供大量库文档或进行状态流图分析来扩充知识，但这会显著增加上下文窗口和令牌使用量，效率低下。另一方面，现有的编译器在环或烧录在环的验证范式存在局限，它们无法捕捉仅在物理执行时才会出现的硬件行为错误。此外，硬件仿真框架（如QEMU）对外设保真度低、时序模型不完整，难以模拟真实的传感器-执行器交互，导致许多硬件故障无法在纯数字环境中被捕获。

因此，本文要解决的核心问题是：如何构建一个高效可靠的AI智能体框架，使其能够在碎片化、约束严格的嵌入式与IoT开发环境中，生成并验证能够正确在真实硬件上运行的代码。为此，论文引入了基于技能的智能体框架，其核心思想是将针对特定外设、MCU或框架组合的关键编程模式、初始化约束和已知故障模式，提炼成紧凑、可读的技能文档，而非注入原始文档，从而在降低令牌开销的同时提升可靠性。为了系统评估该框架，论文还配套提出了IoT-SkillsBench基准测试，通过在多种平台和任务上进行真实的硬件执行验证，来量化结构化硬件知识（特别是专家提炼的技能）对智能体性能的提升作用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类，旨在解决AI代理在嵌入式与物联网系统开发中的挑战。

在方法类研究中，现有工作主要通过增强代理的记忆能力来应对硬件复杂性。例如，通过向代理提供大量库文档或利用状态流图分析来解决API使用冲突。然而，这些方法会显著增加上下文窗口和令牌使用量。此外，一些研究采用编译器在环或烧录在环的范式，但未能涵盖物理执行中出现的行为错误。硬件仿真框架（如QEMU和Wokwi）也被使用，但它们存在外围设备保真度有限、时序模型不完整以及对真实传感器-执行器交互支持不足的问题。

在应用类研究中，已有工作探索将基于LLM的代理应用于嵌入式系统，但通常专注于纯软件环境或有限模拟。这些方法往往假设成功编译即意味着正确运行，忽略了硬件部署后的时序约束、初始化要求或硬件特定行为导致的故障。

本文与这些工作的区别在于：1）提出了一个基于技能的代理框架，将关键编程模式、初始化约束和已知故障模式提炼为紧凑的技能文档，而非注入原始文档，从而降低令牌开销并提高可靠性；2）引入了IoT-SkillsBench基准，通过真实硬件执行系统评估代理，涵盖多个平台和任务复杂度，弥补了纯软件验证的不足；3）通过对比无技能、LLM生成技能和人类专家技能配置，强调了高质量、基于真实硬件行为的结构化知识对可靠开发的关键作用。

### Q3: 论文如何解决这个问题？

论文通过引入一个基于技能的智能体框架来解决硬件在环嵌入式开发中软件与物理硬件紧密耦合的挑战。其核心方法是构建一个结构化的技能库，将人类专家的硬件知识编码为可重用的模块，从而引导大型语言模型生成符合特定硬件约束的正确代码。

整体框架采用LangGraph实现的三节点架构，包括管理器节点、编码器节点和汇编器节点。这种极简设计旨在隔离技能本身的影响，避免复杂的多步规划或反思循环等机制干扰评估。主要工作流程为：当启用技能时，管理器节点作为项目规划器，根据任务需求从可用技能头文件列表中选择相关技能，并将其与任务提示一起传递给编码器节点；编码器节点扮演专家嵌入式工程师角色，将所选技能内容作为适用标准，生成主固件代码文件；汇编器节点则负责将原始输出格式化为可编译项目，处理所有平台特定的脚手架代码，例如为ESP-IDF和Zephyr生成CMakeLists.txt，为Zephyr额外生成prj.conf配置文件和设备树覆盖层。这种职责分离确保了编码器专注于固件逻辑，而汇编器处理平台特定的项目结构。

关键技术在于“技能”的设计与应用。技能本质上是结构化的专家知识模块，涵盖了硬件初始化、时序约束、外设配置等关键领域。论文创新性地比较了三种技能配置：无技能、LLM生成的技能和人类专家技能。评估结果表明，简洁的人类专家技能能实现近乎完美的成功率。此外，论文还提出了IoT-SkillsBench基准测试，涵盖三个嵌入式平台、23种外设和42个不同难度的任务，并通过真实硬件执行进行验证，确保了评估结果反映实际部署行为而非仿真环境产物。通过这种技能增强的方法，智能体能够有效克服硬件特定行为带来的编译后故障，显著提高在真实嵌入式系统上的开发成功率。

### Q4: 论文做了哪些实验？

论文在自建的IoT-SkillsBench基准上进行了系统实验。实验设置方面，评估了三种智能体配置：无技能基线、使用LLM生成技能、使用人类专家编写技能。任务涵盖三个代表性嵌入式平台（Arduino、ESP-IDF、Zephyr），涉及23种外设和42个任务，任务难度分为三个等级，所有任务均通过真实硬件执行进行验证。

主要对比了不同技能配置下的任务解决成功率（Pass@1和Pass@5）以及令牌消耗。关键数据指标如下：无技能基线在Arduino和ESP-IDF的Level 1任务上达到完美（12/12），但在Zephyr为11/12；随着难度增加，性能下降，在Level 3任务上，ESP-IDF仅解决7/14，Zephyr解决6/14。LLM生成技能的结果不一致，例如在ESP-IDF上总体性能从31/42降至27/42，且令牌消耗最高（平均输入约8,500-9,500令牌，输出约1,500-2,000令牌）。相比之下，人类专家技能取得了近乎完美的性能：Arduino为42/42，ESP-IDF和Zephyr均为41/42，且令牌消耗更优（输入约650-2,900，输出约1,700-4,600）。实验表明，简洁、专家精心设计的技能在效果和效率上均优于LLM生成的技能。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其技能库依赖人工专家构建，这限制了其可扩展性和泛化能力。未来研究可探索如何自动化地从硬件文档、代码库或交互中学习技能，实现动态技能获取与更新。此外，当前框架主要针对特定微控制器平台，未来可研究跨平台、跨架构的通用技能表示方法，使智能体能适应多样化的嵌入式硬件环境。另一个方向是增强智能体的实时调试与诊断能力，使其不仅能生成代码，还能通过硬件反馈（如传感器数据、错误日志）自主修正时序或配置问题。最后，可结合强化学习，让智能体在仿真或实际硬件中通过试错优化技能策略，从而减少对精确领域知识的依赖，提升在复杂、非确定性环境中的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型在嵌入式与物联网系统开发中面临的硬件在环挑战，提出了一个基于技能的智能体框架，并引入了IoT-SkillsBench基准测试集。核心问题是：成功编译的代码在真实硬件上部署时，常因时序、外设初始化或硬件特定行为而失败，现有纯软件验证方法无法有效捕捉这些硬件行为错误。

论文方法的核心是“技能”框架。该框架将特定外设、MCU或开发框架的关键编程模式、初始化约束和已知故障模式，提炼为紧凑、人类可读的文档，供智能体使用，从而替代将大量原始SDK文档注入提示词的传统做法。这显著降低了令牌开销并提高了可靠性。为系统评估该方法，作者构建了IoT-SkillsBench，涵盖3个嵌入式平台、23种外设和42个不同难度的任务，并通过真实硬件执行来验证。

主要结论是：仅凭大语言模型的原始能力不足以实现可靠的嵌入式开发；由大模型自动生成的技能效果不稳定，有时甚至有害；而简洁、由人类专家精心构建的技能，能够将任务成功率提升至接近完美的水平，同时保持可控的令牌成本。这证明，基于真实硬件行为的、结构化的专家知识对于硬件在环的智能体编程至关重要。
