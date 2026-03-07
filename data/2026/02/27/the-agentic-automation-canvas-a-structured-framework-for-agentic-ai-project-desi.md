---
title: "The Agentic Automation Canvas: a structured framework for agentic AI project design"
authors:
  - "Sebastian Lobentanzer"
date: "2026-02-16"
arxiv_id: "2602.15090"
arxiv_url: "https://arxiv.org/abs/2602.15090"
pdf_url: "https://arxiv.org/pdf/2602.15090v2"
categories:
  - "cs.SE"
tags:
  - "Architecture & Frameworks"
relevance_score: 5.5
taxonomy:
  capability:
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Agentic Automation Canvas (AAC)"
  primary_benchmark: "N/A"
---

# The Agentic Automation Canvas: a structured framework for agentic AI project design

## 原始摘要

Agentic AI prototypes are being deployed across domains with increasing speed, yet no methodology for their structured design, governance, and prospective evaluation has been established. Existing AI documentation practices and guidelines -- Model Cards, Datasheets, or NIST AI RMF -- are either retrospective or lack machine-readability and interoperability. We present the Agentic Automation Canvas (AAC), a structured framework for the prospective design of agentic systems and a tool to facilitate communication between their users and developers. The AAC captures six dimensions of an automation project: definition and scope; user expectations with quantified benefit metrics; developer feasibility assessments; governance staging; data access and sensitivity; and outcomes. The framework is implemented as a semantic web-compatible metadata schema with controlled vocabulary and mappings to established ontologies such as Schema$\mathrm{.}$org and W3C DCAT. It is made accessible through a privacy-preserving, fully client-side web application with real-time validation. Completed canvases export as FAIR-compliant RO-Crates, yielding versioned, shareable, and machine-interoperable project contracts between users and developers. We describe the schema design, benefit quantification model, and prospective application to diverse use cases from research, clinical, and institutional settings. The AAC and its web application are available as open-source code and interactive web form at https://aac.slolab.ai$\mathrm{.}$

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM/VLM的Agentic AI系统在快速部署过程中缺乏结构化设计、治理和前瞻性评估方法的问题。作者指出，当前Agentic AI原型的开发往往是临时性的，缺乏标准化的规划流程，导致用户期望与技术可行性之间存在巨大鸿沟（即“期望-实现差距”）。现有的AI文档实践（如Model Cards、Datasheets）或治理框架（如NIST AI RMF）大多是回顾性的，且缺乏机器可读性和互操作性，无法有效支持Agentic系统从设计到部署的全生命周期管理。因此，论文提出了一个名为“Agentic Automation Canvas (AAC)”的结构化框架，旨在为Agentic自动化项目提供一个前瞻性的设计工具，促进用户与开发者之间的沟通，并生成机器可读、可共享的项目“合同”，以系统化地捕获项目定义、收益量化、可行性评估、治理阶段、数据敏感性和成果等关键维度。

### Q2: 有哪些相关研究？

论文将AAC定位在AI文档与治理工件的生命周期图谱中，并与多个相关研究进行了对比。1) **回顾性文档工具**：如Model Cards（用于报告训练好的模型）和Datasheets for datasets（用于记录数据集来源），它们主要关注事后描述，缺乏前瞻性和机器可读的规范。2) **项目设计画布**：如受商业模式画布启发的Machine Learning Canvas，它专注于机器学习项目的产品-市场契合，但未涉及治理、收益量化或机器可读规范。3) **治理与合规框架**：如NIST AI RMF，提供了合规性清单，但未生成可与数据管理基础设施集成的机器可读规范。4) **部署期治理工具**：如Policy Cards，它定义了部署阶段AI代理的运行时规范性约束（如允许/拒绝/升级规则），与AAC形成互补。AAC填补了从规划到部署的空白，专注于前瞻性设计，并生成可转化为Policy Cards的机器可读RO-Crate输出。此外，论文还借鉴了语义网标准（如Schema.org、DCAT、PROV-O）和FAIR原则，以确保输出数据的互操作性和可发现性。

### Q3: 论文如何解决这个问题？

论文的核心解决方案是提出了Agentic Automation Canvas (AAC)框架及其技术实现。AAC是一个结构化的元数据模式，包含六个维度：1) **项目定义与范围**：捕获标题、描述、目标、领域等核心元数据。2) **用户期望**：以结构化需求形式捕获，每个需求附带量化的收益指标（时间节省、质量提升、风险降低、能力启用、成本效率），并明确考虑人工监督成本以计算净收益。3) **开发者可行性评估**：评估技术就绪度、模型选择、实施架构（如简单提示、RAG、微调、Agentic框架）以及结构化风险评估（技术、数据、合规、运营、伦理、采纳风险）。4) **治理阶段**：定义生命周期阶段、负责主体（人、组织或软件）、里程碑、合规标准及Policy Card链接。5) **数据访问与敏感性**：记录数据集格式、许可、访问权限、敏感性级别及数据使用限制（DUO术语）。6) **成果**：跟踪可交付成果、出版物和评估结果。

**关键技术实现**：AAC被实现为一个完全客户端运行的Web应用（Vue.js/TypeScript），确保数据隐私。用户填写的画布可导出为符合FAIR原则的RO-Crate包，其中包含JSON-LD格式的元数据，并映射到Schema.org、DCAT、PROV-O等标准本体，从而实现机器可读和互操作。RO-Crate包还包含一个AGENTS.md文件，可将设计合同转化为可供编码助手或基于LLM的开发代理使用的指令。此外，论文提出了从AAC到Policy Card的映射工作流，将规划意图（如合规标准、风险评估）转化为部署期的运行时约束规则，从而形成从设计到审计的完整治理链条。

### Q4: 论文做了哪些实验？

论文主要通过对多个前瞻性用例的应用来展示AAC的实用性和广泛适用性，而非传统的量化对比实验。这些用例涵盖了研究、临床和机构设置，包括：单细胞生物信息学、临床研究助理、药物靶点数据库、面向患者的聊天机器人、研究数据管理和机构AI协调。论文详细描述了一个具体案例：为Open Targets药物发现平台设计一个基于Agent的自然语言接口。在该案例中，用户期望被量化为“减少获得洞察的时间”和“提升非计算研究人员的可访问性”。开发者可行性评估认为，使用自定义MCP服务器在知识图谱上进行检索增强生成（RAG）在技术上是可行的，但存在中高风险（尤其是涉及专有数据时）。治理阶段定义了从原型内部验证到公开部署的分阶段推出计划。成果指标则与初始收益估计挂钩，以便直接比较预期与实际收益。论文通过这个案例说明，没有AAC时，这些考量往往分散在不同文档中，而AAC能将其整合为一份机器可读的“活文档”。此外，论文还通过表格（Table 1）将AAC与Model Cards、Data Cards、Machine Learning Canvas、Policy Cards等现有工件在生命周期阶段、规范性和机器可读性等方面进行了系统性对比，突出了AAC在前瞻性规划和机器可读规范方面的独特价值。

### Q5: 有什么可以进一步探索的点？

论文指出了几个未来可以进一步探索的方向和当前局限。1) **画布输出的发现与共享机制**：AAC生成的RO-Crate包是去中心化且默认私有的，这虽然保护了隐私，但也需要额外的机制来促进这些包的共享和发现。作者计划未来将其与Agentic工具链（如MCP服务器注册表、知识图谱组件注册表、社区研究软件平台）更紧密地集成，以支持开源Agentic工作流的广泛重用和重组。2) **自动化映射工具的开发**：论文提出了从AAC RO-Crate到Policy Card的结构化映射工作流，但该转换工具本身是未来的工作，需要实现并验证其有效性。3) **长期效用与社区采纳**：AAC作为一个促进沟通的“活文档”框架，其长期效用取决于社区的广泛采纳和使用。作者欢迎贡献者和更多用例，并计划通过开源机制持续支持。4) **量化验证**：论文中提到的用例是前瞻性的，未来需要对这些案例进行跟踪分析，以定量评估AAC在缩小“期望-实现差距”和提升复杂流程自动化成功率方面的实际效果。5) **框架扩展**：随着Agentic AI模式的快速演进，AAC模式中定义的结构化词汇和风险评估类别可能需要不断扩展和调整以适应新的技术范式。

### Q6: 总结一下论文的主要内容

本文提出了Agentic Automation Canvas (AAC)，一个用于基于LLM/VLM的Agentic AI系统结构化设计和治理的前瞻性框架。AAC通过一个包含六个维度（项目定义、用户期望、开发者可行性、治理阶段、数据访问与敏感性、成果）的画布，旨在弥合用户期望与开发者可行性之间的鸿沟，并促进双方的有效沟通。其核心创新在于将项目设计形式化为一份机器可读、版本化且可共享的“合同”，该合同以符合FAIR原则的RO-Crate包形式输出，并映射到多种语义网标准（如Schema.org, DCAT），确保了互操作性。AAC还引入了结构化的收益量化模型和风险评估类别，支持对自动化价值的理性评估。论文通过多个领域用例展示了AAC的实用性，并将其与现有的AI文档和治理工件进行对比，突出了其在填补从规划到部署的空白方面的独特价值。AAC作为一个开源工具，旨在为快速发展的Agentic AI领域提供一种系统化、负责任且可审计的项目设计方法。
