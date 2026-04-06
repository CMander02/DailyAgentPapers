---
title: "Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis"
authors:
  - "Zhiyuan Li"
  - "Jingzheng Wu"
  - "Xiang Ling"
  - "Xing Cui"
  - "Tianyue Luo"
date: "2026-04-03"
arxiv_id: "2604.02837"
arxiv_url: "https://arxiv.org/abs/2604.02837"
pdf_url: "https://arxiv.org/pdf/2604.02837v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Agent Skills"
  - "Threat Analysis"
  - "System Architecture"
  - "Multi-Agent Systems"
  - "Safety & Alignment"
relevance_score: 7.5
---

# Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis

## 原始摘要

Agent Skills is an emerging open standard that defines a modular, filesystem-based packaging format enabling LLM-based agents to acquire domain-specific expertise on demand. Despite rapid adoption across multiple agentic platforms and the emergence of large community marketplaces, the security properties of Agent Skills have not been systematically studied. This paper presents the first comprehensive security analysis of the Agent Skills framework. We define the full lifecycle of an Agent Skill across four phases -- Creation, Distribution, Deployment, and Execution -- and identify the structural attack surface each phase introduces. Building on this lifecycle analysis, we construct a threat taxonomy comprising seven categories and seventeen scenarios organized across three attack layers, grounded in both architectural analysis and real-world evidence. We validate the taxonomy through analysis of five confirmed security incidents in the Agent Skills ecosystem. Based on these findings, we discuss defense directions for each threat category, identify open research challenges, and provide actionable recommendations for stakeholders. Our analysis reveals that the most severe threats arise from structural properties of the framework itself, including the absence of a data-instruction boundary, a single-approval persistent trust model, and the lack of mandatory marketplace security review, and cannot be addressed through incremental mitigations alone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地解决Agent Skills框架所面临的安全风险问题。研究背景是，随着基于大语言模型的AI代理从被动问答转向能自主规划、执行代码和调用外部服务的主动工作流，一种名为Agent Skills的新型能力扩展框架应运而生。它采用基于文件系统的模块化封装格式，通过自然语言指令文件（SKILL.md）和可选的可执行脚本，让代理能按需获取领域专业知识，因其灵活性和易用性而迅速被多个平台采纳并催生了大型社区市场。

然而，现有方法存在严重不足。尽管该框架发展迅速，但其安全属性尚未得到系统研究。现有安全机制的发展滞后于其快速采用。论文指出，其架构特性——如自然语言指令传递、文件系统级代码执行和开放市场分发——带来了不同于以往AI扩展机制的新型安全漏洞。现实中的安全事件（如勒索软件执行、大规模供应链攻击）证实了这些风险并非理论假设，而是源于框架本身的结构性缺陷。

本文要解决的核心问题是：对Agent Skills框架进行首次全面的安全分析。具体而言，论文旨在构建一个统一的安全威胁模型，系统识别并分类其在整个生命周期（创建、分发、部署、执行）中暴露的攻击面，基于架构分析和真实事件证据建立一个分层的威胁分类体系，并通过分析实际安全事件加以验证，最终为每个威胁类别讨论防御方向并提出可操作建议，以推动该领域安全性的成熟。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大语言模型（Agent）能力扩展机制的安全架构展开，可分为方法类与评测类两大类。

在方法类工作中，论文重点对比了两种主流机制：**ChatGPT Plugins** 和**模型上下文协议（MCP）**。ChatGPT Plugins 通过强类型的 OpenAPI 接口定义远程服务，执行完全在服务提供商的沙箱环境中进行，保持了明确的数据-指令边界和严格的权限控制，并设有强制性的市场审核流程。MCP 则通过标准化的 JSON-RPC 协议连接工具与数据源，降低了集成成本，但允许服务器在本地运行，引入了更广的攻击面，并且其去中心化分发模式取消了强制审核。

本文研究的 Agent Skills 框架与上述工作存在演进关系，旨在解决 MCP 在编码复杂工作流和降低创作门槛方面的不足。然而，它在安全设计上做出了根本性不同的权衡：它用自然语言指令文件（SKILL.md）取代了类型化接口，将指令与可执行脚本置于同一文件包中，从而彻底**消解了数据-指令边界**；同时，它继承了 MCP 缺乏强制市场审核和单次授权持久信任模型的弱点，并因极低的创作门槛进一步加剧了供应链风险。因此，本文的核心贡献在于首次对 Agent Skills 这一融合了前代最弱治理属性与全新接口级漏洞的框架，进行了系统性的生命周期安全分析和威胁分类。

### Q3: 论文如何解决这个问题？

论文通过构建一个全面的安全分析框架来解决Agent Skills的安全问题，其核心方法是系统性地剖析Agent Skills架构的生命周期和攻击面，并建立威胁分类法。整体框架围绕四个阶段（创建、分发、部署、执行）和三个攻击层展开。

主要模块和组件包括：
1. **架构分析模块**：深入解析Agent Skills的三个核心架构组件——包结构、渐进式披露模型和信任模型。包结构以SKILL.md文件为中心，包含YAML前件和自然语言指令体，但缺乏数据与指令的正式边界。
2. **生命周期与攻击面识别模块**：将Skill的完整生命周期划分为四个阶段，并识别每个阶段引入的结构性攻击面，为威胁建模奠定基础。
3. **威胁分类法构建模块**：基于架构分析和真实证据，构建包含七个类别、十七个场景的威胁分类法，这些威胁分布在三个攻击层上，并通过五个已确认的安全事件进行验证。

创新点体现在：
- **首次系统性安全分析**：这是对Agent Skills框架的首次全面安全研究，填补了该新兴标准的安全评估空白。
- **结构性问题揭示**：明确指出最严重的威胁源于框架本身的结构特性，包括数据-指令边界的缺失、单次批准的持久信任模型以及缺乏强制性的市场安全审查，这些问题无法仅通过渐进式缓解措施解决。
- **可操作的防御方向**：基于威胁分类法，为每个威胁类别讨论了防御方向，识别了开放研究挑战，并为利益相关者提供了可操作的建议，如加强内容验证和引入动态信任机制。

通过这一多层次的分析方法，论文不仅揭示了Agent Skills潜在的安全风险，还为后续的安全改进和标准演化提供了理论基础和实践指南。

### Q4: 论文做了哪些实验？

论文的实验部分主要围绕对Agent Skills框架的安全威胁进行系统性分析与验证。实验设置基于对Agent Skills完整生命周期（创建、分发、部署、执行）的结构化分析，构建了一个包含三个攻击层面、七大类威胁和十七个具体场景的威胁分类体系。

数据集与基准测试方面，研究并未使用传统机器学习数据集，而是以真实的Agent Skills生态系统作为分析对象，重点考察了多个主流智能体平台和社区市场中的实际技能。研究通过分析五个已确认的安全事件来验证所提出的威胁分类的有效性，这些事件提供了现实世界中的攻击证据。

对比方法上，由于这是首次对Agent Skills框架进行全面的安全分析，研究主要与当前生态中缺乏系统性安全审查的现状进行对比，突出了现有框架在安全机制上的缺失。

主要结果与关键指标包括：
1.  识别出框架本身的结构性缺陷是最高风险来源，特别是缺乏数据与指令的边界、单一的持久性信任模型，以及市场缺乏强制安全审核。
2.  威胁分类体系涵盖了从供应链攻击（如凭证窃取、仓库劫持）到运行时攻击（如提示词注入、权限滥用）的完整链条。
3.  通过五个实际安全事件的分析，证实了所分类威胁的现实存在性，例如恶意技能通过市场分发、安装后内容篡改以及运行时执行未授权操作等。
4.  研究指出，仅靠渐进式缓解措施无法解决这些根本性结构问题，并为每个威胁类别提出了防御方向和建议。

### Q5: 有什么可以进一步探索的点？

该论文虽系统分析了Agent Skills的安全威胁，但仍有多个方向值得深入探索。首先，论文提出的防御方向多为原则性建议，缺乏具体技术方案，未来可研究细粒度的安全机制，如动态权限沙箱、行为监控与自动拦截系统。其次，当前分析侧重于框架本身的结构性缺陷，但未充分探讨如何结合形式化验证或可信执行环境（TEE）来确保技能执行的可验证安全。此外，技能供应链安全（如依赖包审查、数字签名链）和去中心化治理模型（如社区驱动的安全审计）也是重要方向。最后，随着多智能体协作场景增多，跨技能交互中的隐蔽攻击（如合谋攻击、权限提升链）需进一步建模与检测。这些方向不仅需要技术突破，也需生态层面的标准与协作。

### Q6: 总结一下论文的主要内容

本文首次对Agent Skills框架进行了系统性安全分析。该框架是一种新兴的开放标准，采用基于文件系统的模块化封装格式，使LLM智能体能够按需获取领域专业知识。论文的核心贡献在于揭示了该框架因其架构特性而存在的固有安全风险，并构建了首个全面的威胁分类体系。

研究首先将Agent Skills的生命周期分解为创建、分发、部署和执行四个阶段，系统分析了每个阶段引入的结构性攻击面。在此基础上，论文构建了一个包含三层攻击面、7个威胁类别和17个具体场景的威胁分类法，涵盖了从供应链攻击到运行时攻击的完整链条。研究通过分析五个已确认的真实安全事件验证了该分类法。

主要结论指出，最严重的威胁源于框架本身的结构特性：缺乏数据与指令的边界、基于单次批准的持久性信任模型、以及缺乏强制性的市场安全审查。这些漏洞无法仅通过增量缓解措施解决。论文最后为每个威胁类别讨论了防御方向，并指出了未来研究面临的开放挑战。
