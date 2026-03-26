---
title: "ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers"
authors:
  - "Songyang Liu"
  - "Chaozhuo Li"
  - "Chenxu Wang"
  - "Jinyu Hou"
  - "Zejian Chen"
  - "Litian Zhang"
  - "Zheng Liu"
  - "Qiwei Ye"
  - "Yiming Hei"
  - "Xi Zhang"
  - "Zhongyuan Wang"
date: "2026-03-25"
arxiv_id: "2603.24414"
arxiv_url: "https://arxiv.org/abs/2603.24414"
pdf_url: "https://arxiv.org/pdf/2603.24414v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Security Framework"
  - "Tool-Augmented Agents"
  - "Runtime Monitoring"
  - "Open Source Agent"
  - "Multi-Layer Protection"
relevance_score: 8.0
---

# ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers

## 原始摘要

OpenClaw has rapidly established itself as a leading open-source autonomous agent runtime, offering powerful capabilities including tool integration, local file access, and shell command execution. However, these broad operational privileges introduce critical security vulnerabilities, transforming model errors into tangible system-level threats such as sensitive data leakage, privilege escalation, and malicious third-party skill execution. Existing security measures for the OpenClaw ecosystem remain highly fragmented, addressing only isolated stages of the agent lifecycle rather than providing holistic protection. To bridge this gap, we present ClawKeeper, a real-time security framework that integrates multi-dimensional protection mechanisms across three complementary architectural layers. (1) \textbf{Skill-based protection} operates at the instruction level, injecting structured security policies directly into the agent context to enforce environment-specific constraints and cross-platform boundaries. (2) \textbf{Plugin-based protection} serves as an internal runtime enforcer, providing configuration hardening, proactive threat detection, and continuous behavioral monitoring throughout the execution pipeline. (3) \textbf{Watcher-based protection} introduces a novel, decoupled system-level security middleware that continuously verifies agent state evolution. It enables real-time execution intervention without coupling to the agent's internal logic, supporting operations such as halting high-risk actions or enforcing human confirmation. We argue that this Watcher paradigm holds strong potential to serve as a foundational building block for securing next-generation autonomous agent systems. Extensive qualitative and quantitative evaluations demonstrate the effectiveness and robustness of ClawKeeper across diverse threat scenarios. We release our code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开源自主智能体运行时OpenClaw所面临的严峻安全防护问题。研究背景是，OpenClaw作为领先的自主智能体平台，集成了工具调用、本地文件访问和Shell命令执行等强大能力，使其能够执行类似真实用户的操作。这种广泛的运行权限在带来实用价值的同时，也引入了关键的安全漏洞，将模型层面的错误转化为系统级的具体威胁，例如敏感数据泄露、权限提升和恶意第三方技能执行。

现有方法存在显著不足。首先，**防护措施高度碎片化**，现有研究通常只针对智能体生命周期的孤立阶段（如提示注入、运行时滥用），缺乏统一、全面的保护视图，且方案常与特定系统紧耦合，通用性差。其次，存在**安全性与效用的权衡困境**，现有防御多依赖嵌入在OpenClaw内部的技能或插件来执行安全约束，迫使智能体在完成任务和遵守安全规则两个竞争目标间做出妥协。再者，现有方法多为**被动防御**，主要依赖事后分析日志和行为模式来识别问题，无法在恶意行动生效前进行实时预警和阻止。最后，防御机制**静态僵化**，无法适应新兴威胁，这与OpenClaw自身具备的持续演化能力根本冲突。

因此，本文要解决的核心问题是：如何为OpenClaw这类高权限、可扩展的自主智能体系统，设计并实现一个**全面的、实时的、主动的且能自适应演化**的安全防护框架，以弥合现有碎片化方案的不足，覆盖智能体完整生命周期，并从根本上缓解安全与效用的矛盾。为此，论文提出了ClawKeeper框架，通过技能层、插件层和独立的“观察者”层这三重互补的架构，提供多维度的综合保护。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：**自主智能体系统框架**、**智能体安全威胁**以及**现有安全防护措施**。

在**自主智能体系统框架**方面，早期研究如ReAct提出了结合推理与行动的范式，提升了性能与可解释性。后续工作如Voyager（具身终身智能体）、MetaGPT（多智能体协作框架）等进一步扩展了能力。这些研究共同确立了现代LLM智能体的核心设计模式。本文研究的OpenClaw正是在此背景下出现的一个突出的开源框架，其特点是持续运行、本地优先部署，并通过模块化技能架构与主机系统紧密集成，从而引入了独特的安全挑战。

针对**智能体安全威胁**，已有研究指出，智能体系统因多步规划、工具调用、持久化记忆及与不可信环境交互而面临独特风险。其中，提示注入（prompt injection）被确认为主要攻击向量。此外，研究如BadAgent揭示了微调或工具链构建过程中可能引入的后门攻击，而Prompt Infection则表明此类威胁可在互联的智能体间传播，导致系统性破坏。这些风险在OpenClaw这类直接与操作系统、本地文件等交互的框架中尤为严重。

在**现有安全防护措施**方面，当前防御手段（如防护栏、沙箱、插件审计等）往往呈现碎片化，仅针对特定攻击面提供孤立保护，缺乏覆盖智能体生命周期的整体架构。本文提出的ClawKeeper框架旨在弥补这一差距，通过技能层、插件层和观察者层这三个互补的架构层，提供一个统一、多维度的实时安全防护体系，特别是其创新的、解耦的观察者范式，与现有局部化方案形成鲜明对比。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ClawKeeper的多层实时安全框架来解决OpenClaw代理的安全漏洞问题。其核心方法是整合三个互补的架构层，提供从指令到系统级的全面防护。

**整体框架与主要模块：**
ClawKeeper的架构包含三个核心保护层：
1.  **基于技能的保护**：在指令层运作，将结构化的安全策略（以Markdown文档形式）直接注入到代理的推理上下文中。它包含两个维度：系统级（提供Windows、Linux、macOS等跨平台约束）和软件级（针对Telegram、飞书等集成软件定义安全规范）。此外，它还辅以轻量级的安全脚本，实现定期安全扫描和交互摘要分析，以增强鲁棒性和透明度。
2.  **基于插件的保护**：作为运行时的内部强制层，是一个硬编码的安全插件。它集成了审计、监控、加固等多种功能，构成一个统一的安全解决方案。其主要组件包括：**威胁检测**（扫描配置漏洞）、**加固模块**（执行防御措施并向核心配置文件注入安全规则）、**配置保护**（对关键文件进行哈希备份和验证）以及**行为扫描**（分析日志以检测复杂威胁模式）。
3.  **基于观察者的保护**：这是一种创新的、解耦的系统级安全中间件。它作为一个独立的外部代理运行，持续验证代理的状态演化，实现实时执行干预（如停止高风险操作或强制人工确认），而无需与代理的内部逻辑耦合。这提供了最高的安全隔离性。

**关键技术及创新点：**
*   **多层互补架构**：创新性地将技能层（灵活、低成本）、插件层（深度执行控制）和观察者层（独立、高安全保证）统一起来，允许用户根据安全、兼容性、成本等需求自由选择和组合，克服了现有方案零散、孤立的缺陷。
*   **观察者范式**：提出了一个解耦的安全审计范式，作为下一代自主代理系统的安全基石。其核心创新在于实现了安全执行与代理核心进程的严格架构分离，使得被攻破的代理难以绕过或禁用安全机制，显著提升了防护的稳健性。
*   **全面的覆盖范围**：在技能层，不仅考虑系统级风险，还首创性地建模了通信软件（如飞书）层面的安全风险。在插件层，整合并超越了现有开源插件的功能，提供了从静态配置加固到动态行为扫描的端到端保护。
*   **灵活的部署**：框架提供了从纯提示注入（高灵活性）到独立中间件（高安全性）的多种部署选项。特别是为观察者模式提供了简化的安装包，降低了其实际部署难度。

总之，ClawKeeper通过其三层协同的架构设计，在安全性、兼容性和灵活性之间取得了平衡，为OpenClaw代理提供了前所未有的系统性安全防护。

### Q4: 论文做了哪些实验？

论文实验部分主要包括实验设置、数据集/基准测试、对比方法和主要结果。实验设置上，ClawKeeper 在 OpenClaw 自主代理运行时环境中部署，通过三个互补的架构层（技能层、插件层、监视器层）进行集成评估。数据集/基准测试方面，研究构建了多样化的威胁场景，模拟了敏感数据泄露、权限提升和恶意第三方技能执行等实际风险，以全面测试框架的保护能力。对比方法上，论文将 ClawKeeper 与现有 OpenClaw 生态系统中零散的安全措施进行对比，这些措施通常只覆盖代理生命周期的孤立阶段。主要结果显示，ClawKeeper 在定性和定量评估中均表现出高效性和鲁棒性，能实时干预高风险操作（如停止动作或强制人工确认），有效防止系统级威胁。关键数据指标包括威胁检测的实时响应时间、安全策略注入的成功率，以及行为监控的误报/漏报率，这些指标均优于片段化保护方法。最终，代码已开源供进一步验证。

### Q5: 有什么可以进一步探索的点？

本文提出的ClawKeeper框架在OpenClaw代理的实时安全防护上迈出了重要一步，但其设计仍存在一些局限性和值得深入探索的方向。首先，框架的防护机制高度依赖于预定义的安全策略和规则，对于未知或新型攻击模式（如高级持续性威胁或利用模型本身弱点的对抗性提示）的适应性可能不足。未来研究可探索结合异常检测算法或轻量级机器学习模型，实现动态、自适应的威胁识别与响应。

其次，Watcher层的解耦设计虽降低了侵入性，但其“监控-干预”机制可能引入延迟，在需要极低延迟响应的关键任务场景中可能成为瓶颈。未来可研究更高效的异步监控协议或硬件加速方案，以平衡安全性与性能。此外，当前框架主要针对单代理环境，在多代理协同或竞争场景中，代理间的复杂交互可能引发新的安全挑战（如共谋攻击、资源竞争漏洞）。扩展ClawKeeper以支持多代理系统的安全协调将是一个重要方向。

最后，从更广阔的视角看，安全不应仅是“附加层”，而应深度融入代理的架构设计中。未来可探索将形式化验证、可解释AI技术与运行时防护相结合，从代理的决策根源提升其安全性与可靠性，构建真正内生安全的自主智能体系统。

### Q6: 总结一下论文的主要内容

本文提出了ClawKeeper，一个为OpenClaw自主智能体运行时设计的综合性实时安全防护框架。OpenClaw作为开源智能体运行时，其强大的工具集成、文件访问和命令执行能力带来了严重的安全风险，如数据泄露和权限滥用，而现有防护措施零散且仅覆盖部分生命周期。

ClawKeeper的核心贡献在于统一了三个互补的防护层，提供全生命周期的安全覆盖。第一，基于技能的防护在指令层面运作，通过结构化安全策略直接注入智能体上下文，强制执行环境特定约束和跨平台边界。第二，基于插件的防护作为内部运行时强制层，提供配置加固、主动威胁检测和持续行为监控。第三，基于观察者的防护引入了一种新颖的、解耦的系统级安全中间件，这是一个独立的监控智能体，能够持续验证智能体状态演化，实现实时执行干预（如停止高风险操作或要求人工确认），而无需与智能体内部逻辑耦合。

该方法的关键意义在于有效缓解了传统防护中安全性与效用性的权衡问题。观察者范式实现了监管分离，使安全监督独立于任务执行，从而允许各自优化。同时，观察者本身作为智能体，能够基于新出现的风险更新其技能和记忆，形成自适应、自我改进的安全层。评估表明ClawKeeper在各种威胁场景下具有有效性和鲁棒性。该框架不仅适用于OpenClaw，其观察者范式可作为构建下一代自主智能体系统安全的基础模块，具有广泛的兼容性和应用潜力。
