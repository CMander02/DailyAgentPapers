---
title: "Give Them an Inch and They Will Take a Mile:Understanding and Measuring Caller Identity Confusion in MCP-Based AI Systems"
authors:
  - "Yuhang Huang"
  - "Boyang Ma"
  - "Biwei Yan"
  - "Xuelong Dai"
  - "Yechao Zhang"
  - "Minghui Xu"
  - "Kaidi Xu"
  - "Yue Zhang"
date: "2026-03-08"
arxiv_id: "2603.07473"
arxiv_url: "https://arxiv.org/abs/2603.07473"
pdf_url: "https://arxiv.org/pdf/2603.07473v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Authorization"
  - "Model Context Protocol"
  - "System Vulnerability"
  - "Empirical Study"
relevance_score: 7.5
---

# Give Them an Inch and They Will Take a Mile:Understanding and Measuring Caller Identity Confusion in MCP-Based AI Systems

## 原始摘要

The Model Context Protocol (MCP) is an open and standardized interface that enables large language models (LLMs) to interact with external tools and services, and is increasingly adopted by AI agents. However, the security of MCP-based systems remains largely unexplored.In this work, we conduct a large-scale security analysis of MCP servers integrated within MCP clients. We show that treating MCP servers as trusted entities without authenticating the caller identity is fundamentally insecure. Since MCP servers often cannot distinguish who is invoking a request, a single authorization decision may implicitly grant access to multiple, potentially untrusted callers.Our empirical study reveals that most MCP servers rely on persistent authorization states, allowing tool invocations after an initial authorization without re-authentication, regardless of the caller. In addition, many MCP servers fail to enforce authentication at the per-tool level, enabling unauthorized access to sensitive operations.These findings demonstrate that one-time authorization and server-level trust significantly expand the attack surface of MCP-based systems, highlighting the need for explicit caller authentication and fine-grained authorization mechanisms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统化分析基于模型上下文协议（MCP）的AI系统中一个尚未被充分探索的安全漏洞——“调用者身份混淆”问题。研究背景是，随着大语言模型（LLM）代理从纯信息角色转向能够直接与后端系统交互的执行组件，MCP作为一种开放、标准化的接口被广泛采用，它解耦了代理推理与系统级操作，使LLM能通过独立的MCP服务器进程调用外部工具和服务。然而，MCP系统的安全性在很大程度上仍未得到充分研究。

现有方法（即当前普遍的MCP服务器实现方式）存在严重不足。核心问题在于，MCP服务器通常被当作可信实体，而缺乏对调用者身份的有效认证。由于MCP服务器往往无法区分请求的发起者，一次授权决策可能隐式地授予多个潜在不可信的调用者访问权限。具体不足体现在两方面：首先，大多数MCP服务器依赖持久的授权状态，在初始授权后，无论后续调用者是谁，都允许工具调用而无需重新认证；其次，许多MCP服务器未在单个工具级别强制执行身份验证，导致攻击者可能未经授权访问敏感操作。这种“一次性授权”和“服务器级信任”模式，本质上是将授权从每次调用的检查转变为服务器持有的持久执行状态，错误地假设所有工具调用都来自单一可信的调用者上下文。

因此，本文要解决的核心问题是：如何理解、测量并检测MCP服务器中普遍存在的“调用者身份混淆”漏洞。该漏洞使得一旦服务器建立了授权执行状态，后续无论来源为何的工具调用都可能继承此状态，从而导致授权在多个调用上下文之间被不当重用，显著扩大了基于MCP的系统的攻击面，可能引发远程命令执行、未经授权的UI控制或特权API滥用等实际攻击，而无需依赖凭证窃取或显式的授权绕过。论文通过设计一个名为MAP的分析框架并进行大规模实证研究，来系统地识别和验证这一安全问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕AI代理系统的执行范式和安全机制展开，可分为以下几类：

**1. 执行范式相关研究**：论文背景部分系统梳理了AI代理的三种主流执行范式。一是**进程内执行**，工具作为函数嵌入代理运行时，执行边界模糊，安全性较弱；二是**插件/API执行**，代理通过预定义接口调用外部服务，具有清晰的执行边界，后端可独立验证请求；三是**中间件执行**，以模型上下文协议为代表，将模型推理与系统执行解耦，通过独立服务器进程暴露工具。本文聚焦MCP这一中间件范式，深入分析其特有的安全风险。

**2. 安全与授权机制研究**：现有研究多关注传统系统的访问控制，如Android操作系统通过集中式权限框架在资源访问点统一实施授权。然而，MCP服务器缺乏系统级授权基础设施，其敏感操作范围更广（包括模型介导的操作、应用特定能力等），且没有标准化SDK提供内置授权原语。本文指出，现有MCP服务器的授权实现高度依赖开发者，常见模式包括无授权检查、一次性授权后持久化状态、或基于调用者身份重新授权。本文的核心贡献在于首次大规模实证分析了MCP服务器中普遍存在的“调用者身份混淆”漏洞，即服务器无法区分请求来源，导致单次授权可能被多个未受信任调用者滥用。

**3. 多智能体系统安全研究**：尽管已有工作探讨了多智能体协作中的信任与协调问题，但较少关注中间件架构下的身份隔离与细粒度授权。本文区别于现有研究，明确指出MCP服务器将自身视为可信实体的假设存在根本缺陷，并通过实证揭示了持久化授权状态和工具级认证缺失等问题，从而提出了对显式调用者认证和细粒度授权机制的需求。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为 \TheName{} 的工具来解决 MCP 系统中调用者身份混淆的安全问题。该工具的核心方法是，将授权分析从粗粒度的服务器级别假设转移到调用级别的归属分析，以检测因授权状态未与调用者身份绑定而导致的漏洞。

整体框架与主要模块包括：
1.  **执行触发的工具入口解析（S-1）**：首先，工具需要识别 MCP 工具的执行入口点。与传统系统不同，MCP 服务器的工具执行并非始于一个明确定义的函数，而是通过协议层的 `tools/call` 请求，经过服务器特定的派发逻辑（如动态查找、间接调用或运行时构建处理器）后才触发。因此，该工具将“执行触发点”建模为一流的分析抽象，识别外部请求转变为内部执行行为的程序位置，而非静态地寻找固定的处理函数。
2.  **路径敏感的授权分析（S-2）**：在识别执行入口后，工具对每条执行路径进行路径敏感的分析，以恢复 MCP 服务器中分散且异构的授权语义。它追踪从 `tools/call` 入口到影响系统、文件、网络或物理资源操作的控制流。对于每条路径，分析授权是否（i）被执行，（ii）被缓存为服务器级状态，或（iii）明确绑定到与调用相关的调用者身份。这克服了传统基于语法模式或函数摘要的分析方法的不足。
3.  **选择性动态授权验证（S-3）**：由于许多 MCP 服务器以有状态的方式实现授权（例如，一次性授权后缓存为全局状态），静态分析无法可靠判断资源访问是否针对当前调用进行了正确授权。因此，该工具在（S-2）的基础上，选择性地进行动态验证：通过观察执行结果，判断那些包含授权逻辑但缺乏每次调用强制检查的工具路径，在实际运行时是否依赖于为不同调用者建立的授权状态，从而确认身份混淆漏洞。

创新点在于：
*   **执行触发点抽象**：首次将 MCP 中协议层请求到内部代码执行的“承诺时刻”作为安全分析的关键入口点，解决了非标准化工具注册和入口带来的挑战。
*   **归属导向的路径分析**：将分析焦点从“服务器是否支持授权”转移到“授权决策是否明确限定于发起调用的调用者身份”，直接针对身份混淆漏洞的本质。
*   **动静结合的验证方法**：结合路径敏感的静态分析和选择性的动态执行验证，有效应对了授权状态在运行时被缓存和混淆的挑战，确保了分析的准确性。

### Q4: 论文做了哪些实验？

该论文的实验主要包括对MCP服务器进行大规模安全分析，以评估其身份混淆漏洞。

**实验设置**：研究团队开发了一个自动化分析工具，用于检测MCP服务器中的调用者身份混淆漏洞。该工具结合了静态和动态分析技术。静态分析部分识别工具执行的入口点，并追踪从入口点到影响资源（系统、文件、网络等）操作的执行路径，分析授权状态。动态分析部分则用于选择性验证授权，通过观察执行结果来判断授权是否与当前调用者身份明确绑定。

**数据集/基准测试**：实验对象是从开源社区（如GitHub）和官方MCP生态系统中收集的MCP服务器实现。论文评估了这些服务器在授权机制上的普遍缺陷。

**对比方法**：研究主要关注MCP服务器自身的设计模式，而非与其他系统进行横向对比。实验的核心是比较不同服务器在授权执行粒度上的差异，例如对比“服务器级信任/一次性授权”与“调用者绑定/细粒度授权”模式下的安全性。

**主要结果与关键指标**：
1.  **普遍存在身份混淆**：实证研究表明，大多数被分析的MCP服务器依赖持久的授权状态。一旦完成初始授权，后续的工具调用无需重新认证，无论调用者是谁。
2.  **授权粒度不足**：许多MCP服务器未在单个工具级别强制执行身份验证，导致攻击者可能未经授权访问敏感操作。
3.  **核心发现**：论文证实，一次性授权和服务器级信任显著扩大了基于MCP的系统的攻击面。关键的安全缺陷在于授权决策未明确限定于触发调用的具体身份，使得通过合法交互获得的授权可能被后续来自不同代理或执行上下文的调用 silently 复用。

### Q5: 有什么可以进一步探索的点？

本文揭示了MCP系统中因授权状态重用而导致的调用者身份混淆问题，其核心局限在于当前多数MCP服务器实现将授权绑定于服务器状态而非调用者身份。这导致一旦服务器获得授权，任何能发起远程调用的代理都可能滥用此权限，从而引发系统执行、数据访问、网络通信及物理设备交互等多层面的安全风险。

未来研究可从以下几个方向深入探索：首先，需设计并标准化显式的调用者身份认证机制，例如在MCP协议层引入可验证的调用者标识符或会话令牌，确保每次工具调用都能关联到特定身份。其次，应推动细粒度授权策略的实施，支持按工具或操作进行动态权限校验，而非依赖一次性的服务器级授权。此外，可探索如何在不损害用户体验和代理自主性的前提下，实现授权状态的轻量级重新评估，例如通过上下文感知的信任度评估模型。最后，从系统设计角度，可研究如何将传统中间件中成熟的身份传播模式适配到LLM驱动的代理架构中，以从根本上解决身份混淆问题。

### Q6: 总结一下论文的主要内容

本文对基于模型上下文协议（MCP）的AI系统进行了首次大规模安全分析，揭示了其核心安全漏洞——调用者身份混淆问题。研究指出，MCP系统普遍将服务器视为可信实体，缺乏对调用者身份的认证。这导致一旦某个调用者获得初始授权，其授权状态往往被持久化，后续任何调用者（包括潜在的恶意方）都可能利用此状态来调用工具，而无需重新认证。此外，许多服务器未在工具级别实施细粒度认证，使得未授权访问敏感操作成为可能。论文的核心贡献在于通过实证研究，证明了当前普遍依赖一次性授权和服务器级信任的模式会显著扩大攻击面。主要结论是，MCP系统的安全设计亟需引入明确的调用者身份认证机制和细粒度的授权策略，以防止权限被恶意滥用。
