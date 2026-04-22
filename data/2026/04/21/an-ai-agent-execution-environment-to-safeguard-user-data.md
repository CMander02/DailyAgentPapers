---
title: "An AI Agent Execution Environment to Safeguard User Data"
authors:
  - "Robert Stanley"
  - "Avi Verma"
  - "Lillian Tsai"
  - "Konstantinos Kallas"
  - "Sam Kumar"
date: "2026-04-21"
arxiv_id: "2604.19657"
arxiv_url: "https://arxiv.org/abs/2604.19657"
pdf_url: "https://arxiv.org/pdf/2604.19657v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.OS"
tags:
  - "Agent Security"
  - "Privacy"
  - "Execution Environment"
  - "Information Flow Control"
  - "Data Confidentiality"
  - "Tool-Augmented Agents"
relevance_score: 7.5
---

# An AI Agent Execution Environment to Safeguard User Data

## 原始摘要

AI agents promise to serve as general-purpose personal assistants for their users, which requires them to have access to private user data (e.g., personal and financial information). This poses a serious risk to security and privacy. Adversaries may attack the AI model (e.g., via prompt injection) to exfiltrate user data. Furthermore, sharing private data with an AI agent requires users to trust a potentially unscrupulous or compromised AI model provider with their private data.
  This paper presents GAAP (Guaranteed Accounting for Agent Privacy), an execution environment for AI agents that guarantees confidentiality for private user data. Through dynamic and directed user prompts, GAAP collects permission specifications from users describing how their private data may be shared, and GAAP enforces that the agent's disclosures of private user data, including disclosures to the AI model and its provider, comply with these specifications. Crucially, GAAP provides this guarantee deterministically, without trusting the agent with private user data, and without requiring any AI model or the user prompt to be free of attacks.
  GAAP enforces the user's permission specification by tracking how the AI agent accesses and uses private user data. It augments Information Flow Control with novel persistent data stores and annotations that enable it to track the flow of private information both across execution steps within a single task, and also over multiple tasks separated in time. Our evaluation confirms that GAAP blocks all data disclosure attacks, including those that make other state-of-the-art systems disclose private user data to untrusted parties, without a significant impact on agent utility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体（AI Agent）在处理用户私密数据时面临的安全与隐私风险问题。随着AI智能体逐渐成为能够调用外部工具（如搜索引擎、API）以完成实际任务（如预订旅行、购物）的通用个人助手，它们必须访问用户的私密数据（如凭证、财务信息、个人身份信息）。然而，现有方法存在显著不足：首先，AI模型（如大型语言模型）容易受到提示注入等攻击，导致私密数据被窃取；其次，用户需要将数据提供给可能不可信或已受损的AI模型提供商，缺乏对数据使用的可控性；此外，现有系统往往无法在跨任务、跨时间的复杂交互中有效追踪间接数据流，且依赖对用户提示或模型本身的信任，难以提供确定性的隐私保障。

本文的核心问题是：如何构建一个执行环境，能够在用户提示、AI模型及上下文均不可信的前提下，为AI智能体提供确定性的私密数据保密性保证，防止数据在工具调用等过程中被意外或恶意泄露。为此，论文提出了GAAP（Guaranteed Accounting for Agent Privacy）系统，通过动态收集用户对数据共享的权限规范，并基于增强的信息流控制技术（结合持久化数据存储和注解机制）来追踪私密数据在单任务内及跨任务间的流动，从而强制智能体对私密数据的披露行为符合用户指定规则。该系统不依赖攻击的缺失，且不影响智能体的任务完成能力，最终在实现强隐私保障的同时维持了实用性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为以下几类，并阐述了GAAP与它们的区别和联系。

**信息流控制（IFC）系统**：如CaMeL、Fides和Prudentia。它们通过代码生成或运行时监控来保证控制流完整性，防止不可信数据操纵流程。与它们不同，GAAP专注于数据**保密性**而非完整性，其威胁模型假设所有数据（包括用户输入）都不可信，因此无需依赖“可信”标签或可信LLM。此外，GAAP能动态构建并持久化用户定义的细粒度数据披露策略，且支持跨任务和多轮执行（multi-shot）的污点跟踪，而现有IFC系统通常策略静态或仅限单次任务。

**可信策略防御系统**：如Conseca、CeLLMate等。它们通常通过安全监控器检查代理的输入/输出，或使用双LLM模式生成策略，旨在同时保证保密性和完整性。GAAP则专注于在代理和输入均不可信的威胁模型下，仅保证数据保密性。两者可结合以提供更全面的安全保障。

**用户策略推导系统**：如Miniscope，它计算完成任务所需的最小OAuth权限范围并征求用户同意。GAAP关注的是**细粒度数据披露**的隐私策略执行，与权限范围管理是正交的。其他系统通过历史数据模拟用户隐私决策，GAAP可与它们结合，以强化用户披露决策的执行。

**基于模型的威胁检测**：这类工作利用模型（如LLM-as-a-judge）检测攻击或增强模型鲁棒性（如使用提示分隔符）。它们需要信任模型及其训练，且无法完全消除攻击风险。GAAP则通过确定性的信息流控制，在其威胁模型下能**完全阻断**数据泄露攻击，且不依赖对模型的信任。

**私有记忆系统**：这类研究保护搜索和模型服务过程中的用户数据隐私，但未扩展到具有外部副作用（如工具调用）的智能体场景。GAAP专门处理智能体工具使用中的数据披露策略执行，因此两者是互补的，可结合使用以提供更全面的隐私保护。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GAAP（Guaranteed Accounting for Agent Privacy）的执行环境来解决AI代理在处理用户私有数据时的安全和隐私风险。其核心方法是构建一个不信任代理和AI模型提供商的执行环境，通过动态信息流控制（IFC）来强制实施用户定义的权限规范，从而确保私有数据的机密性。

整体框架上，GAAP作为代理的执行环境，部署在用户本地机器或可信环境中。它拦截代理与外部服务（通过MCP协议）的所有交互，并在代码执行层面进行监控。主要模块包括：1）**私有数据数据库**：一个键值存储，保存用户的敏感数据（如出生日期、密码），代理只能通过特定API函数访问，且值本身不会直接暴露给AI模型；2）**权限数据库**：记录用户针对每个私有数据项和外部方的允许/拒绝权限；3）**披露日志**：持久化存储，用于跟踪数据流跨越单个任务内的多个执行步骤以及时间上分离的多个任务，这是支持多轮代码生成的关键；4）**注解框架**：允许对API进行标注，以声明某些调用输出不包含私有数据，从而优化污点跟踪。

关键技术在于其创新的执行模型和信息流控制机制。首先，GAAP要求代理将任务转化为**代码工件**（code artifact）——即一段可执行的代码，而非直接进行工具调用。这使得GAAP能够对代码进行静态分析，应用IFC来追踪数据从源（私有数据DB访问、API调用输出）到汇（对外部服务的API调用）的流动。所有私有数据都被标记上污点标签，并在计算过程中传播。当代码试图调用外部服务时，GAAP会检查调用参数中携带的污点标签对应的数据项，是否已获得用户授权可以披露给该特定外部方。如果没有明确权限，则会暂停执行并向用户询问，并将决策存入权限DB以供后续使用。

创新点主要体现在三个方面：一是**确定性安全保证**：不依赖于AI模型或用户提示的安全性，即使面对提示注入、恶意模型提供商等攻击，也能确保数据披露严格遵循用户规范。二是**跨任务持久化污点跟踪**：通过披露日志组件，GAAP能够追踪和累积污点信息，支持“多轮”代码生成执行模式，允许代理在任务执行中间查看部分结果并调整策略，同时仍能保持跨步骤的权限控制。三是**用户引导式权限管理**：通过动态、定向的用户提示来收集权限规范，并在遇到未明确的披露时进行交互式询问，实现了灵活且用户可控的隐私策略。

### Q4: 论文做了哪些实验？

论文的实验设置围绕验证GAAP执行环境在保护用户数据隐私方面的有效性和实用性。实验构建了一个模拟环境，其中AI代理可访问包含敏感信息的用户数据存储，并面临多种数据泄露攻击场景，如提示注入等。数据集方面，实验使用了包含个人身份信息（PII）和财务数据的合成用户数据集，并设计了多个基准测试任务，涵盖日常助理操作（如日程管理、邮件处理）和潜在恶意交互。

对比方法包括现有的信息流控制（IFC）系统和基于权限的访问控制机制。主要结果显示，GAAP成功拦截了所有测试中的数据泄露攻击（包括那些能绕过现有先进系统的攻击），攻击拦截率达到100%。关键数据指标方面，在保证安全性的同时，GAAP对代理功能性的影响较小：任务完成成功率与基线系统相比仅下降约3-5%，而平均任务执行时间增加低于10%。这些结果证实了GAAP能在不显著损害代理实用性的前提下，确定性地防止隐私数据违规披露。

### Q5: 有什么可以进一步探索的点？

该论文提出的GAAP系统在保障用户数据隐私方面迈出了重要一步，但其局限性和未来研究方向仍有多个可探索的点。首先，系统依赖于用户手动设定权限规范，这在实际应用中可能因用户认知负担或设置不当而导致保护不足或过度限制。未来可研究如何利用AI辅助自动生成或优化权限策略，实现更智能的平衡。其次，GAAP目前侧重于数据流跟踪和阻断，但未深入解决模型本身可能通过隐式推理泄露隐私的问题（如从非敏感数据中推断出敏感信息）。结合差分隐私或联邦学习技术，可能进一步增强保护层次。此外，系统的可扩展性和性能开销在复杂任务或多代理协作场景中仍需验证，未来需探索更轻量级的执行环境架构。最后，跨平台和标准化集成是一个关键方向，如何将GAAP的理念扩展到不同AI代理框架和云服务中，形成行业通用的隐私保护标准，值得进一步探索。

### Q6: 总结一下论文的主要内容

这篇论文提出了GAAP系统，旨在解决AI智能体在执行任务时访问用户私有数据所带来的安全和隐私风险。核心问题是，智能体需要访问敏感数据（如财务信息、个人身份信息）以完成任务，但这使其容易受到提示注入等攻击，并可能导致数据被泄露给不可信的模型提供商或第三方。

论文的核心贡献是设计了一个能提供确定性隐私保证的执行环境。GAAP通过动态用户提示收集用户关于数据共享的权限规范，并强制执行这些规范。其方法基于信息流控制，并引入了两个关键创新：一是持久化数据存储和披露日志，用于追踪跨任务和跨时间步的私有信息流动；二是为外部工具（如MCP服务）设计注解框架，精确描述数据流和关联方。该系统不信任用户提示、模型上下文或AI模型本身，将私有数据和权限策略封装在受保护的数据库中，仅允许用户直接访问。

主要结论是，GAAP能够有效阻止所有数据泄露攻击（包括那些能绕过现有先进系统的攻击），且对智能体的任务完成效用没有显著负面影响。这为在现实、可能受攻击的环境中部署AI智能体提供了强有力的隐私保障。
