---
title: "A Formal Security Framework for MCP-Based AI Agents: Threat Taxonomy, Verification Models, and Defense Mechanisms"
authors:
  - "Nirajan Acharya"
  - "Gaurav Kumar Gupta"
date: "2026-04-07"
arxiv_id: "2604.05969"
arxiv_url: "https://arxiv.org/abs/2604.05969"
pdf_url: "https://arxiv.org/pdf/2604.05969v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Model Context Protocol (MCP)"
  - "Formal Verification"
  - "Threat Taxonomy"
  - "Defense Mechanisms"
  - "Multi-Agent Systems"
  - "AI Safety"
relevance_score: 8.0
---

# A Formal Security Framework for MCP-Based AI Agents: Threat Taxonomy, Verification Models, and Defense Mechanisms

## 原始摘要

The Model Context Protocol (MCP), introduced by Anthropic in November 2024 and now governed by the Linux Foundation's Agentic AI Foundation, has rapidly become the de facto standard for connecting large language model (LLM)-based agents to external tools and data sources, with over 97 million monthly SDK downloads and more than 177000 registered tools. However, this explosive adoption has exposed a critical gap: the absence of a unified, formal security framework capable of systematically characterizing, analyzing, and mitigating the diverse threats facing MCP-based agent ecosystems. Existing security research remains fragmented across individual attack papers, isolated benchmarks, and point defense mechanisms. This paper presents MCPSHIELD, a comprehensive formal security framework for MCP-based AI agents. We make four principal contributions: (1) a hierarchical threat taxonomy comprising 7 threat categories and 23 distinct attack vectors organized across four attack surfaces, grounded in the analysis of over 177000 MCP tools; (2) a formal verification model based on labeled transition systems with trust boundary annotations that enables static and runtime analysis of MCP tool interaction chains; (3) a systematic comparative evaluation of 12 existing defense mechanisms, identifying coverage gaps across our threat taxonomy; and (4) a defense in depth reference architecture integrating capability based access control, cryptographic tool attestation, information flow tracking, and runtime policy enforcement. Our analysis reveals that no existing single defense covers more than 34 percent of the identified threat landscape, whereas MCPSHIELD's integrated architecture achieves theoretical coverage of 91 percent. We further identify seven open research challenges that must be addressed to secure the next generation of agentic AI systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于模型上下文协议（MCP）的AI智能体生态系统所面临的系统性安全框架缺失问题。研究背景是，MCP自2024年11月由Anthropic推出并交由Linux基金会管理后，已成为连接大语言模型智能体与外部工具和数据源的事实标准，其生态发展迅猛（例如月SDK下载量超9700万，注册工具超17.7万）。然而，这种爆炸式采用暴露了一个关键缺口：现有的安全研究呈现碎片化状态，散见于个别攻击论文、孤立的基准测试和单点防御机制中，缺乏一个统一的、形式化的安全框架来系统性地刻画、分析和缓解MCP智能体面临的各种威胁。

现有方法的不足主要体现在三个方面：首先，从业者缺乏通用的威胁分类词汇，无法系统评估MCP部署的安全态势；其次，由于假设和威胁模型不同，各种防御机制之间难以进行有意义的比较；最后，由于缺乏对MCP安全属性的形式化语义定义，阻碍了自动化验证和可信部署的实现。

因此，本文要解决的核心问题是：为基于MCP的AI智能体构建一个全面的形式化安全框架（即MCPSHIELD），以提供一个统一的威胁分类法、一个支持静态和运行时分析的形式化验证模型、对现有防御机制的系统性评估，以及一个集成了多层防御的参考架构，从而填补当前生态在系统性安全分析和防护方面的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：MCP特定安全研究、MCP基准评测、MCP防御机制以及通用AI智能体安全研究。

在**MCP特定安全研究**方面，已有工作对MCP安全威胁进行了初步探索。例如，有研究首次系统性识别了MCP生命周期中的16种威胁场景，并映射到四类攻击者；另有工作分析了工具投毒、影子攻击和“拉地毯”攻击，并提出了基于RSA的清单签名和LLM语义审查方案。这些研究为本文的威胁分类学奠定了基础，但彼此较为分散。

在**MCP基准评测**方面，出现了多个专注于评估MCP安全性的基准，如MCPTox、MCP-SafetyBench和MCPSecBench。它们分别涵盖了不同数量的攻击类型和风险类别，但由于采用了互不兼容的分类体系，难以进行横向比较。本文的工作旨在提供一个统一的分类框架来整合这些分散的评估标准。

在**MCP防御机制**方面，已有一些点状防御方案被提出。例如，MCP-Guard采用了静态扫描、神经检测和LLM仲裁的三阶段防御；ETDI引入了结合OAuth和加密身份验证的工具定义；MCPS则实现了基于ECDSA的消息签名。本文对这些机制进行了系统性评估，发现单一防御的覆盖率均不超过34%，从而凸显了集成防御架构的必要性。

在**通用AI智能体安全**方面，相关研究指出了AI智能体安全在输入、执行、环境和外部交互等方面存在的知识缺口，并对LLM智能体的整体安全性进行了评测。此外，OWASP LLM应用十大风险中“过度代理”和“供应链”风险也与MCP安全直接相关。这些研究为理解MCP安全在更广阔图景中的位置提供了背景。

**本文与这些工作的关系和区别**在于：不同于以往零散的研究、互不兼容的基准或孤立的防御点，本文首次提出了一个统一的、形式化的安全框架（MCPSHIELD）。它整合并扩展了现有威胁分类，建立了首个支持形式化验证的MCP交互模型，并通过系统性的覆盖分析，提出了一个深度防御参考架构，理论上能覆盖91%的威胁场景，弥补了现有工作的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MCPSHIELD的综合性、形式化安全框架来解决MCP生态系统中缺乏统一安全框架的问题。其解决方案的核心是一个分层防御的深度参考架构，并辅以一个形式化验证模型来系统性地定义和分析安全属性。

**整体框架与架构设计**：MCPSHIELD采用纵深防御策略，其架构由四个互补的防御层构成：
1.  **基于能力的访问控制层**：通过为每个智能体分配不可伪造的能力令牌来实施最小权限原则，控制智能体可以调用哪些工具及参数，并引入组合策略防御能力链攻击。
2.  **密码学工具证明层**：确保工具完整性。要求MCP服务器为每个工具发布签名的工具证明记录，在每次调用前验证工具定义哈希、版本和依赖树，防止工具被篡改或回滚。
3.  **信息流跟踪层**：控制数据流向以实施数据约束属性。在MCP消息级别进行动态污点跟踪，为来自工具响应的数据标记其源信任域的安全标签，并检查调用参数的安全标签是否不高于目标服务器的许可级别。
4.  **运行时策略执行层**：监控交互过程。实现一个安全自动机（编辑自动机模型），实时监控MCP操作流，并可以抑制、插入或修改动作以执行安全策略，如速率限制、异常检测和语义验证。

**核心方法与关键技术**：
*   **形式化验证模型**：论文将MCP交互形式化为一个带有信任边界标注的标记转移系统。该模型精确定义了四个基本安全属性：**工具完整性**（防御工具替换和拉毯攻击）、**数据约束**（防御跨服务器数据泄漏）、**权限有界性**（防御权限提升）和**上下文隔离**（防御上下文渗透和内存污染）。该模型为静态和运行时分析提供了理论基础，并论证了部分属性的可判定性。
*   **集成与互补**：各防御层并非孤立，而是协同工作。例如，L-CAC控制“能做什么”，L-CTA确保“工具是什么”，L-IFT控制“数据去哪”，L-RPE监控“如何执行”。论文通过覆盖分析表明，单一现有防御最多覆盖34%的威胁，而MCPSHIELD的集成架构实现了91%的理论覆盖率（完全覆盖了23个攻击向量中的21个）。

**主要创新点**：
1.  提出了首个针对MCP智能体的**统一、形式化安全框架**，填补了该领域的空白。
2.  构建了一个**分层的威胁分类法**和基于形式化模型的**安全属性定义**，为系统化的威胁分析和验证奠定了基础。
3.  设计了一个**纵深防御参考架构**，创新性地整合了基于能力的访问控制、密码学工具证明、信息流跟踪和运行时策略执行，通过各层的互补实现了近乎全面的威胁覆盖。
4.  对现有防御机制进行了系统性评估，揭示了覆盖缺口，并论证了集成方案的有效性和必要性。

### Q4: 论文做了哪些实验？

本文实验部分的核心是对12种现有防御机制进行系统性比较分析。实验设置基于论文提出的分层威胁分类法（涵盖7个威胁类别和23个攻击向量）。评估针对每个防御机制，分析其覆盖的威胁类别、执行模型（预防性、检测性或反应性）、部署要求和性能开销。

数据集/基准测试方面，分析基于对超过177,000个已注册MCP工具的分析，并参考了现有基准如MCP-SafetyBench和MCPSecBench。对比方法包括D1 ETDI（增强工具定义接口）、D2 MCP-Guard（三阶段防御）、D3 MCPGuard（自动化漏洞检测）、D4 Secure Tool Manifest（基于RSA的清单签名）、D5 MCPS（MCP Secure，使用ECDSA P-256加密）、D6 MCP规范安全原则、D7-D8基准衍生防御、D9企业安全框架、D10微软Agent治理工具包、D11 OWASP Agentic AI指南以及D12零信任架构原则。

主要结果通过一个覆盖度表格呈现，关键数据指标显示：没有单一防御机制能覆盖超过34%的已识别威胁场景（D8 MCPSecBench覆盖最广，为34%）。具体而言，D2 MCP-Guard在检测工具中毒（TC1）和提示注入（TC6）方面达到89.63%的准确率和89.07%的F1分数；跨服务器数据泄漏（TC3）是防御最薄弱的类别；协议级攻击（TC7）缺乏专门防御；防“Rug pulls”（TC2）主要依赖版本控制。相比之下，论文提出的MCPSHIELD集成架构实现了91%的理论覆盖度。实验还发现组合攻击缺乏组合性防御，现有工具级防御未考虑工具组合带来的新兴风险。

### Q5: 有什么可以进一步探索的点？

该论文提出的MCPSHIELD框架在统一威胁分类和集成防御方面迈出了重要一步，但仍存在若干局限性和值得深入探索的方向。首先，其形式化验证模型和深度防御架构的“理论覆盖率达91%”仍需在复杂、动态的真实生产环境中进行大规模实证验证，其性能开销、误报率以及对异构MCP工具生态的普适性有待评估。其次，框架侧重于静态和运行时的协议与交互安全，但对Agent本身的内在风险（如目标错位、推理被操纵）以及多Agent协同中涌现的级联攻击考虑不足。未来研究可朝以下几个方向深化：一是发展“自适应安全”机制，利用AI实时学习新型攻击模式并动态调整策略；二是探索“可解释的审计追踪”，使复杂的工具调用链安全状态对运维者透明；三是将安全框架与Agent的价值观对齐、鲁棒性测试相结合，构建更全面的智能体安全保障体系；四是需建立开放、持续更新的基准测试平台，以推动社区在快速演进的生态中共同验证和改进防御方案。

### Q6: 总结一下论文的主要内容

本文针对基于模型上下文协议（MCP）的AI智能体所面临的安全挑战，提出了一个名为MCPSHIELD的综合性形式化安全框架。核心问题是当前MCP生态虽被广泛采用，但缺乏统一的、形式化的安全框架来系统性地应对其多样化的威胁。论文的主要贡献包括：首先，基于对超过17.7万个MCP工具的分析，构建了一个包含7个威胁类别和23个攻击向量的分层威胁分类法。其次，提出了一个基于带信任边界标注的标记转移系统的形式化验证模型，用于对MCP工具交互链进行静态和运行时分析。第三，系统性地评估了12种现有防御机制，揭示了它们在威胁覆盖范围上的不足。最后，设计了一个纵深防御参考架构，集成了基于能力的访问控制、密码学工具认证、信息流跟踪和运行时策略执行。研究表明，现有单一防御最多只能覆盖34%的威胁，而MCPSHIELD的集成架构理论上能覆盖91%。该框架为理解和保障MCP智能体生态安全提供了系统性的理论基础与实践指南，并指出了未来需解决的七个开放研究挑战。
