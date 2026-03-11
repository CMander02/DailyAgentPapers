---
title: "AgenticCyOps: Securing Multi-Agentic AI Integration in Enterprise Cyber Operations"
authors:
  - "Shaswata Mitra"
  - "Raj Patel"
  - "Sudip Mittal"
  - "Md Rayhanur Rahman"
  - "Shahram Rahimi"
date: "2026-03-10"
arxiv_id: "2603.09134"
arxiv_url: "https://arxiv.org/abs/2603.09134"
pdf_url: "https://arxiv.org/pdf/2603.09134v1"
categories:
  - "cs.CR"
  - "cs.MA"
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Security"
  - "Enterprise AI"
  - "Framework"
  - "Trust Boundaries"
  - "Tool Orchestration"
  - "Memory Management"
  - "Compliance"
relevance_score: 7.5
---

# AgenticCyOps: Securing Multi-Agentic AI Integration in Enterprise Cyber Operations

## 原始摘要

Multi-agent systems (MAS) powered by LLMs promise adaptive, reasoning-driven enterprise workflows, yet granting agents autonomous control over tools, memory, and communication introduces attack surfaces absent from deterministic pipelines. While current research largely addresses prompt-level exploits and narrow individual vectors, it lacks a holistic architectural model for enterprise-grade security. We introduce AgenticCyOps (Securing Multi-Agentic AI Integration in Enterprise Cyber Operations), a framework built on a systematic decomposition of attack surfaces across component, coordination, and protocol layers, revealing that documented vectors consistently trace back to two integration surfaces: tool orchestration and memory management. Building on this observation, we formalize these integration surfaces as primary trust boundaries and define five defensive principles: authorized interfaces, capability scoping, verified execution, memory integrity & synchronization, and access-controlled data isolation; each aligned with established compliance standards (NIST, ISO 27001, GDPR, EU AI Act). We apply the framework to a Security Operations Center (SOC) workflow, adopting the Model Context Protocol (MCP) as the structural basis, with phase-scoped agents, consensus validation loops, and per-organization memory boundaries. Coverage analysis, attack path tracing, and trust boundary assessment confirm that the design addresses the documented attack vectors with defense-in-depth, intercepts three of four representative attack chains within the first two steps, and reduces exploitable trust boundaries by a minimum of 72% compared to a flat MAS, positioning AgenticCyOps as a foundation for securing enterprise-grade integration.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型驱动的多智能体系统在企业级应用中的安全集成问题。研究背景是，随着生成式AI的进步，企业正从确定性的、基于规则的自动化流程转向自主规划、调用工具和自然语言协调的多智能体系统，以实现自适应、推理驱动的工作流。然而，赋予智能体对工具、内存和通信的自主控制权，引入了传统确定性流程所没有的攻击面。

现有方法存在明显不足。当前的安全研究主要集中在提示词注入等利用层面和狭窄的单个攻击向量上，呈现碎片化状态。这些研究缺乏一个针对企业级安全需求的整体性架构模型，未能提供一个统一的威胁模型来将多智能体系统的漏洞映射到可操作的防御机制上。此外，现有的授权标准（如OAuth 2.1）并非为自主、长周期的智能体会话而设计。

因此，本文要解决的核心问题是：如何为企业级的多智能体系统集成提供一个系统性的安全框架。具体而言，论文试图回答三个开放性问题：第一，多智能体系统的攻击向量如何映射到可被利用的架构层面；第二，哪些防御原则能够系统地应对这些攻击面；第三，这些原则能否在网络安全运营等高风险领域中得到实例化并具有可衡量的防护效果。为此，论文提出了AgenticCyOps框架，通过系统性地分解攻击面，将工具编排和内存管理识别为关键的信任边界，并在此基础上形式化了五项防御设计原则，旨在为安全的企业级多智能体集成奠定基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多智能体系统（MAS）的安全挑战展开，可归纳为以下几类：

**1. 针对单个智能体的攻击研究**：现有工作广泛关注提示注入、对抗性输入等组件级漏洞，旨在通过操纵感知或推理过程来破坏智能体行为。这些研究通常聚焦于模型内部的对抗性AI问题，但缺乏对系统集成层面的整体考量。

**2. 多智能体协同安全研究**：部分研究探讨了智能体间协调带来的新威胁，如横向渗透、拜占庭攻击或共谋行为。这些工作揭示了集体系统可能涌现出孤立智能体不具备的攻击路径，但多集中于特定攻击模式的分析，未能提供统一的架构安全模型。

**3. 企业级安全与合规框架**：已有标准如NIST、ISO 27001等为传统IT系统提供了安全基线，GDPR和欧盟《人工智能法案》则涉及数据隐私与AI治理。然而，这些标准尚未充分适配多智能体AI系统特有的动态、自主特性及其引入的新型攻击面。

**本文与这些工作的关系与区别**：本文承认并借鉴了上述研究对具体攻击向量的分析，但指出当前研究缺乏一个**整体的、企业级的安全架构模型**。不同于多数工作仅关注孤立攻击向量，本文通过系统性地分解组件、协调和协议层的攻击面，发现已记录的向量均可追溯至**工具编排和内存管理**这两个核心集成表面。在此基础上，本文提出了一个将这两个表面形式化为主要信任边界的框架，并定义了五项防御原则，旨在为企业级多智能体集成提供一个可落地、符合现有合规标准的基础安全方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgenticCyOps的综合性安全框架来解决多智能体系统在企业网络运营中的集成安全问题。其核心方法是系统性地分解攻击面，并将工具编排和内存管理识别为两大关键信任边界，围绕此定义了五项防御原则，并基于Model Context Protocol (MCP)构建具体架构。

**整体框架与主要模块**：
该框架以MCP为结构基础，设计了分阶段作用域的智能体、共识验证循环和按组织划分的内存边界。主要组件包括：
1.  **经过验证的MCP客户端-服务器通信模块**：在智能体与工具的每次交互中，引入一个独立的、基于共识的验证器。该验证器主要负责授权、审计以及基于上下文的验证和过滤，旨在限制攻击面。
2.  **安全内存管理架构**：这是一个纵深防御的持久状态管理方案。其核心是**分层隔离**机制，根据安全级别分类、智能体关系和任务范围对内存进行分区，以防止未经授权的跨智能体检索。同时，通过基于共识的写入过滤来确保数据完整性，并在共享层级间实现同步。

**核心方法与关键技术（对应五项防御原则）**：
1.  **授权接口**：针对工具集成生命周期中的“认证”阶段。采用签名清单确保密码学上的工具来源可信，防止身份伪造；结合管理员批准的集中式工具目录，以及运行时最小权限会话策略。
2.  **能力限定**：针对“范围界定”阶段。实施最小权限原则，根据具体任务上下文动态限定工具权限。关键技术包括**提示流完整性**，用于跟踪指令在提示中的流动并强制执行边界，防止权限静默提升；以及持续的能力审计。
3.  **验证执行**：针对“验证”阶段。采用“先验证，后执行”范式。智能体生成包含计划、目标工具API调用和参数的行动提案，提交给验证模块（可由其他智能体或类似仲裁器组成）进行策略、关键性和历史行为日志的核对。借鉴了区块链共识思想，确保无单一自主行动能构成威胁。
4.  **内存完整性与同步**：确保存储内容的可信度。在写入边界进行合法性验证和定期清理；在检索边界采用**基于共识的验证**。例如，采用“隔离-聚合”范式，先对检索到的内容进行独立处理，再进行安全聚合，确保有限的中毒内容不会污染最终输出。同时，通过序列化、版本控制或协调器来管理多智能体并发读写，确保同步。
5.  **访问控制的数据隔离**：控制内存访问权限。采用**分层隔离架构**和**动态二分访问图**来编码随时间变化的权限，维护具有细粒度读写策略的私有和共享内存层级，并在跨边界共享前应用上下文感知转换（如敏感字段编辑）。

**创新点**：
*   **系统性建模**：首次将企业级多智能体系统的攻击面系统性地分解为组件、协调和协议三层，并收敛到工具编排和内存管理两个核心集成面。
*   **原则化防御**：形式化了五项与现有合规标准（NIST, ISO 27001等）对齐的防御原则，为安全设计提供了清晰指导。
*   **纵深防御集成**：将密码学授权、能力限定、去中心化审计验证、内存分层隔离与共识验证等多种安全机制创新性地整合到一个统一的框架中，实现了工具操作安全（“做什么”）与内存知识安全（“知道什么”）的互补，构建了弹性的“零信任”智能体操作架构。评估表明，该设计能深度防御已知攻击向量，将可利用的信任边界相比扁平化多智能体系统减少了至少72%。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕一个安全运营中心（SOC）工作流展开，采用模型上下文协议（MCP）作为架构基础，构建了一个包含阶段划分的智能体、共识验证循环和按组织划分的内存边界的系统。实验的数据集或基准测试基于合成的SOC操作流程，该流程整合了来自MITRE、NIST等框架的常见阶段：监控与分流、分析与调查、响应与修复、研究与报告。对比方法主要针对传统的、基于规则的安全编排、自动化与响应（SOAR）平台以及扁平的、无集中协调的多智能体系统（MAS）。

主要结果通过覆盖分析、攻击路径追踪和信任边界评估来验证。关键数据指标显示：1）所提出的框架能够深度防御已记录的威胁向量，在四条代表性攻击链中，有三条能在前两步内被拦截；2）与扁平的MAS相比，该设计将可利用的信任边界减少了至少72%。这些结果表明，AgenticCyOps框架通过集中化的主机协调、分阶段的能力限定和独立的内存管理，有效提升了企业级多智能体集成的安全性。

### Q5: 有什么可以进一步探索的点？

该论文聚焦于企业级多智能体系统的安全框架，提出了基于工具编排和内存管理两大集成面的防御原则。然而，其局限性在于：首先，框架验证主要基于理论分析和模拟攻击链，缺乏在真实复杂、高动态企业环境中的大规模部署和对抗性测试，实际有效性有待检验。其次，当前防御原则（如能力限定、共识验证）可能引入显著性能开销和延迟，对于实时性要求高的安全运营中心（SOC）工作流，需在安全与效率间取得更优平衡。

未来研究方向可深入探索：1）**自适应安全机制**：研究能根据实时威胁情报和工作负载动态调整安全策略（如验证强度、内存隔离粒度）的轻量级方法，实现安全与效能的弹性权衡。2）**跨组织协作安全**：论文提及“按组织划分内存边界”，但未深入探讨多企业或多部门智能体协作时的信任建立、隐私保护与审计溯源机制，这将是实际部署的关键挑战。3）**框架泛化与标准化**：可将AgenticCyOps的核心原则抽象为可插拔的安全中间件或协议扩展，便于集成到不同多智能体架构（如AutoGen、CrewAI）中，推动行业安全标准形成。此外，结合形式化验证或零知识证明等技术，进一步提升关键操作（如工具调用）的可验证性与隐私性，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型驱动的多智能体系统在企业工作流中引入的安全风险，提出了一个名为AgenticCyOps的整体安全框架。核心问题是当前研究多关注提示攻击等孤立向量，缺乏面向企业级多智能体集成的系统性安全架构模型。

论文方法首先系统性地分解了组件、协调和协议层的攻击面，指出已记录的威胁主要源于两个集成表面：工具编排和内存管理。基于此，作者将这两个表面形式化为关键信任边界，并定义了五项防御原则：授权接口、能力限定、执行验证、内存完整性与同步，以及访问控制的数据隔离。这些原则与NIST、ISO 27001等合规标准对齐。为验证框架，作者将其应用于安全运营中心工作流，以模型上下文协议为结构基础，设计了阶段限定智能体、共识验证循环和按组织划分的内存边界。

主要结论表明，该框架通过纵深防御有效应对了已记录的攻击向量，能在攻击链前两步拦截四分之三的代表性攻击，并将可利用的信任边界相比扁平化多智能体系统减少了至少72%。因此，AgenticCyOps为企业级多智能体AI集成安全奠定了重要基础。
