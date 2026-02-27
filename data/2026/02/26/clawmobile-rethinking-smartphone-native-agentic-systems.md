---
title: "ClawMobile: Rethinking Smartphone-Native Agentic Systems"
authors:
  - "Hongchao Du"
  - "Shangyu Wu"
  - "Qiao Li"
  - "Riwei Pan"
  - "Jinheng Li"
  - "Youcheng Sun"
  - "Chun Jason Xue"
date: "2026-02-26"
arxiv_id: "2602.22942"
arxiv_url: "https://arxiv.org/abs/2602.22942"
pdf_url: "https://arxiv.org/pdf/2602.22942v1"
categories:
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Tool Use"
  - "Mobile Agent"
  - "Hierarchical Planning"
  - "System Design"
  - "LLM Runtime"
relevance_score: 9.0
---

# ClawMobile: Rethinking Smartphone-Native Agentic Systems

## 原始摘要

Smartphones represent a uniquely challenging environment for agentic systems. Unlike cloud or desktop settings, mobile devices combine constrained execution contexts, fragmented control interfaces, and rapidly changing application states. As large language models (LLMs) evolve from conversational assistants to action-oriented agents, achieving reliable smartphone-native autonomy requires rethinking how reasoning and control are composed.
  We introduce ClawMobile as a concrete exploration of this design space. ClawMobile adopts a hierarchical architecture that separates high-level language reasoning from structured, deterministic control pathways, improving execution stability and reproducibility on real devices. Using ClawMobile as a case study, we distill the design principles for mobile LLM runtimes and identify key challenges in efficiency, adaptability, and stability. We argue that building robust smartphone-native agentic systems demands principled coordination between probabilistic planning and deterministic system interfaces. The implementation is open-sourced~\footnote{https://github.com/ClawMobile/ClawMobile} to facilitate future exploration.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能手机环境下智能体系统（agentic systems）的可靠性问题。随着大语言模型从对话助手向行动导向的智能体演进，智能手机因其独特的约束环境（如有限的执行上下文、碎片化的控制界面和快速变化的应用程序状态）成为实现自主操作的新前沿和挑战。现有方法主要围绕智能体如何行动（基于UI交互 vs. 基于工具/API控制）以及在何处运行（云端托管 vs. 设备本地）展开，但两者存在固有矛盾：UI交互覆盖范围广却易受界面漂移和时序影响而不稳定；工具/API控制更稳定可验证，但难以覆盖所有应用和设备功能。这导致现实中的移动自主系统失败往往并非因为规划能力不足，而是由于移动设备多变的执行条件（如权限弹窗、后台切换、瞬时UI变化）反复中断执行过程。

因此，本文的核心问题是：如何设计一个能够在真实智能手机环境中稳定、可靠运行的智能体系统架构，以协调概率性的大语言模型规划与确定性的系统接口控制，从而克服执行过程中的干扰，实现高度的任务完成率。论文通过提出ClawMobile这一分层运行时架构作为具体探索，将高层语言推理与结构化的确定性控制路径分离，以提升在真实设备上的执行稳定性和可复现性，并以此案例研究提炼移动LLM运行时的设计原则。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，一系列工作致力于将大语言模型（LLM）应用于智能手机环境，实现多模态推理和界面交互。例如，Mobile-Agent和AppAgent等系统专注于移动GUI交互，强调视觉基础和结构化动作生成。另一类工作，如AutoDroid和DroidRun，则关注端到端的移动自动化，将LLM规划器与面向UI的控制层紧密耦合，以执行多步骤工作流，并支持合成可执行代码。这些方法虽然展示了潜力，但普遍以UI为中心，严重依赖对动态界面状态的概率性推理，在鲁棒性和效率上存在局限。

在应用类研究中，OpenClaw作为一个开源、自托管的通用智能体平台，通过统一的运行时将LLM与外部工具连接。其架构通过设备特定节点（如Android客户端）暴露本地能力，支持跨设备工作流。社区已将其扩展到移动设备，探索了远程编排、全本地托管和基于无障碍服务的UI自动化等多种部署策略。然而，这些扩展未能系统地将确定性系统控制与概率性UI推理统一在一个移动运行时内。

在评测类研究中，为了评估智能体在任务驱动条件下的性能，出现了标准化的评测环境，如AndroidWorld和SPA-Bench。

本文提出的ClawMobile与上述工作的关系和区别在于：它继承了现有工作对移动自动化和LLM规划的探索，但认为构建健壮的手机原生智能体系统需要重新思考推理与控制的组合方式。与UI中心化或依赖概率推理的方法不同，ClawMobile采用分层架构，明确分离高层语言推理与结构化、确定性的控制路径，旨在提升执行稳定性和可复现性。它旨在填补现有OpenClaw移动扩展中的空白，将确定性系统控制与概率性UI推理的协调作为首要的系统设计问题来解决。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ClawMobile的层次化架构来解决智能手机原生智能体系统面临的挑战，其核心思想是将高级语言推理与低级设备执行分离，以提高在真实设备上的执行稳定性和可复现性。整体框架包含三个主要协作组件：智能体编排器、控制后端和记忆模块。

智能体编排器作为顶层推理循环，负责将用户输入转换为可执行计划，但不直接操作设备接口，而是通过明确的工具调用与一组可插拔的控制后端交互。控制后端封装了具体的执行机制，例如结构化系统命令（如ADB）、硬件级API（如Termux API）或语义化UI交互模块，每个后端都暴露定义明确的操作原语并返回有界的执行结果。记忆模块则作为辅助运行时层，提供移动设备特定的知识、执行偏好和政策信号，以影响后端选择和任务分解，而不与低级控制逻辑紧密耦合。

其创新点主要体现在三个方面：首先，架构明确区分了确定性后端、UI智能体和直接UI控制操作这三类控制后端，使得执行模式显式化，并确立了“确定性优先”的调度策略，优先使用可预测的结构化接口，仅在必要时才调用概率性的UI推理，从而减少不必要的模型调用并提高执行可靠性。其次，系统采用执行感知的动态调度策略，将后端选择视为一个基于当前设备状态的迭代决策过程，而非固定路径，每次执行后都会通过明确的状态验证来评估任务进度，并据此进行进一步规划。最后，整个设计强调了概率性规划与确定性系统接口之间的原则性协调，通过模块化设计实现了控制路径的灵活扩展，为在资源受限的移动环境中平衡推理成本、执行可靠性和操作覆盖度提供了系统化框架。

### Q4: 论文做了哪些实验？

论文在Google Pixel 9设备（Android 16）上进行了实验，对比了ClawMobile（CM）、DroidRun（DR）以及不带DroidRun的ClawMobile基线版本（CM-w/o-DR）。实验设置了六个涵盖系统设置、单应用操作和跨应用工作流的真实世界任务。所有智能体均使用相同的底层大语言模型（GPT-5.2）。CM和CM-w/o-DR直接在设备上运行，无需连接其他设备，并通过Telegram机器人接收用户指令；DroidRun则按照官方指南，通过USB将设备连接到主机，在主机Python虚拟环境中运行并通过终端命令驱动设备自动化。

主要评估指标包括完成率（人工标注的0%-100%分数，衡量相对于人类完成任务的百分比）和端到端执行时间（秒）。实验结果显示，ClawMobile在所有任务上均实现了接近完美的完成率（所列任务达100%），但平均执行时间比DroidRun慢57.5秒。这种权衡源于运行时策略的根本差异：ClawMobile采用分层架构，通过明确的验证和恢复循环（例如，在每一步动作后重新查询设备状态以验证进展）来提升稳定性，而DroidRun作为UI智能体，在异步应用启动、模糊UI目标识别和错误成功检测等方面容易失败。基线版本CM-w/o-DR虽然也能实现高完成率，但时间成本显著高于CM，尤其在YouTube应用上会因超时而无法完成任务。这些结果凸显了在移动环境中协调概率性规划和确定性系统接口对于实现可靠自主性的重要性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向主要集中在效率、适应性和稳定性三个维度。在效率方面，当前系统依赖远程模型推理，存在延迟和隐私问题。未来可探索轻量级本地推理与选择性远程调用相结合的混合部署策略，并研究增量式状态表示和基于成本模型的混合确定性-概率性调度算法，以优化令牌使用和计算开销。在适应性方面，系统缺乏长期记忆和可复用技能库，导致跨应用和跨会话的连贯性不足。未来可研究从执行轨迹中自动提取结构化技能抽象，并设计分层记忆模型，以区分短期上下文与长期知识，提升泛化能力。在稳定性方面，移动环境中的部分失败和隐私风险尚未得到系统化处理。未来需将可靠性和隐私提升为运行时的一级目标，开发显式的进度验证、故障恢复机制以及形式化的隐私安全模型，确保代理在不可预测环境中的鲁棒执行。此外，将令牌预算和模型放置策略纳入统一的运行时优化框架，也是一个值得深入的系统设计问题。

### Q6: 总结一下论文的主要内容

该论文探讨了在智能手机这一独特且具有挑战性的环境中构建基于大语言模型的智能体系统。核心问题是，移动设备环境存在执行环境受限、控制接口碎片化和应用状态快速变化等挑战，使得传统的云端或桌面端智能体设计难以直接适用。

论文的核心贡献是提出了ClawMobile系统，作为一种具体的设计探索。其方法采用分层架构，将高层语言推理与结构化、确定性的设备控制路径分离开来，旨在提高在真实设备上执行的稳定性和可复现性。通过这一案例研究，论文提炼了移动LLM运行时的设计原则，并指出了在效率、适应性和稳定性方面的关键挑战。

主要结论是，构建健壮的智能手机原生智能体系统，不能仅仅依赖改进的UI推理或更大的模型，而需要在概率性规划和确定性系统接口之间进行有原则的协调。论文主张将移动智能体视为一个运行时系统问题，强调应从孤立的算法改进转向集成的架构设计，在真实设备约束下协同设计推理、控制、内存和可靠性机制，为未来研究奠定了基础。
