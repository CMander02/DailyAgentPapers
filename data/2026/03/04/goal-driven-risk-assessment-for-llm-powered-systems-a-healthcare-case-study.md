---
title: "Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study"
authors:
  - "Neha Nagaraja"
  - "Hayretdin Bahsi"
date: "2026-03-04"
arxiv_id: "2603.03633"
arxiv_url: "https://arxiv.org/abs/2603.03633"
pdf_url: "https://arxiv.org/pdf/2603.03633v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Safety & Alignment"
relevance_score: 5.5
taxonomy:
  capability:
    - "Safety & Alignment"
  domain: "Healthcare & Bio"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Goal-driven risk assessment approach using attack trees"
  primary_benchmark: "N/A"
---

# Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study

## 原始摘要

While incorporating LLMs into systems offers significant benefits in critical application areas such as healthcare, new security challenges emerge due to the potential cyber kill chain cycles that combine adversarial model, prompt injection and conventional cyber attacks. Threat modeling methods enable the system designers to identify potential cyber threats and the relevant mitigations during the early stages of development. Although the cyber security community has extensive experience in applying these methods to software-based systems, the elicited threats are usually abstract and vague, limiting their effectiveness for conducting proper likelihood and impact assessments for risk prioritization, especially in complex systems with novel attacks surfaces, such as those involving LLMs. In this study, we propose a structured, goal driven risk assessment approach that contextualizes the threats with detailed attack vectors, preconditions, and attack paths through the use of attack trees. We demonstrate the proposed approach on a case study with an LLM agent-based healthcare system. This study harmonizes the state-of-the-art attacks to LLMs with conventional ones and presents possible attack paths applicable to similar systems. By providing a structured risk assessment, this study makes a significant contribution to the literature and advances the secure-by-design practices in LLM-based systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将大型语言模型（LLM）集成到关键领域（如医疗保健）系统时，所面临的安全风险缺乏结构化、可操作评估方法的问题。研究背景是LLM在医疗等敏感领域的快速应用带来了效率提升，但也引入了新型安全威胁，这些威胁可能与传统网络攻击结合，形成复杂的攻击链。尽管网络安全社区已有成熟的威胁建模方法（如STRIDE）和新兴的LLM安全分类（如OWASP Top 10），但现有方法存在明显不足：它们通常止步于抽象地枚举威胁或进行定性评估，缺乏将具体攻击向量、前提条件和攻击路径与威胁关联的机制。这导致已识别的威胁往往模糊不清，难以评估其实际发生的可能性和潜在影响，从而无法有效指导风险优先级排序和缓解措施的实施。

因此，本文要解决的核心问题是：如何为LLM赋能的系统（特别是医疗保健系统）提供一个结构化的风险评估框架，以弥补从抽象威胁识别到具体风险量化之间的鸿沟。论文提出了一种目标驱动的风险评估方法，通过使用攻击树，将针对系统各组件的分散威胁，围绕攻击者的具体目标（如干预医疗程序、泄露电子健康记录数据、破坏访问或可用性）进行情境化整合，描绘出包含传统攻击、LLM特定攻击（如提示注入）和对抗性模型攻击在内的详细攻击路径。这种方法旨在使系统设计者能够更准确地评估威胁的可能性和影响，从而实现更严格的风险评分和优先级划分，推动LLM系统实现“安全设计”。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：威胁分类与建模方法、传统风险评估框架，以及特定领域的安全分析。

在**威胁分类与建模方法**方面，已有研究为LLM提出了威胁分类法（如使用STRIDE框架），涵盖了提示注入、数据泄露和幻觉等行为。然而，这些工作主要侧重于威胁的分类和列举，未能将具体威胁与系统层面的影响和攻击路径联系起来，缺乏动态和交互式的风险视角。

在**传统风险评估框架**方面，医疗IT等领域已有成熟的风险评估实践，例如针对无线网络和医疗基础设施的分析。但这些方法通常是静态和粗粒度的，依赖于列举孤立问题，未能建模风险如何通过攻击场景在组件间演化与交互，也忽略了攻击者行为与漏洞在工作流中的传播，尤其无法涵盖LLM带来的新型攻击面和行为特性。

在**特定领域安全分析**方面，物联网和嵌入式设备威胁模型关注网络物理风险，但未涵盖AI原生威胁；关于用户信任和AI决策的研究聚焦于患者与AI的微观交互安全，却缺乏系统级风险建模。近期，有研究开始将攻击防御树等结构化模型应用于ATM系统或ML管道，证明了其可解释性优势，但这些框架尚未被深入探索用于LLM在安全关键场景（如医疗）中的独特风险。

**本文与这些工作的关系和区别在于**：本文没有停留在威胁分类或静态列表层面，而是提出了一种**目标驱动的结构化风险评估方法**。它通过构建**攻击树**来详细描述攻击向量、前提条件和攻击路径，从而将威胁具体化、情境化，并连接至临床影响。本文首次将攻击树与可能性×影响评分相结合，系统性地应用于LLM赋能的医疗系统，弥补了定性分类与实用安全设计之间的鸿沟，为LLM系统安全提供了可操作的风险评估框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个结构化的、目标驱动的风险评估方法来解决LLM系统安全威胁抽象、难以量化评估的问题。其核心是构建一个分层的方法论，将系统建模、威胁识别、攻击树构建和风险量化有机结合。

整体框架遵循一个清晰的流程：首先对基于LLM的医疗系统进行架构建模，明确其组件和信任边界；接着，综合运用STRIDE、MITRE ATLAS和OWASP Top 10 for LLMs等成熟框架，在组件层面识别威胁；然后，将识别出的威胁映射到以目标为导向的攻击树中；最后，基于攻击树推导出具体风险，并通过“可能性×影响”矩阵进行量化评估和优先级排序。

主要模块与关键技术包括：
1.  **系统与威胁建模**：论文对一个典型的LLM医疗代理系统（包含Web应用、医疗平台、协调器、外部资源和LLM核心五个组件）进行建模，并应用STRIDE方法识别威胁。创新点在于将威胁分为三类：针对基础设施的传统网络威胁、针对模型的对抗性机器学习威胁，以及通过输入或上下文操纵LLM行为的对话威胁（如提示注入），这为后续分析奠定了基础。
2.  **目标驱动的攻击树构建**：这是方法的核心创新。论文不是孤立地分析威胁，而是围绕三个高级安全目标（G1：干预医疗程序；G2：泄露电子健康记录数据；G3：破坏访问或可用性）分别构建攻击树。攻击树以攻击者目标为根节点，通过AND/OR逻辑运算符连接中间节点（前提条件或攻击步骤）和叶节点（原子攻击步骤），清晰地描绘出达成特定目标的多条可能攻击路径。这种方法将抽象的威胁转化为具体的、可分析的攻击场景。
3.  **结构化风险演化模型**：为了支持可操作的风险评估，论文提出了一个三阶段威胁演化模型：**前提条件**（攻击可行的系统状态或漏洞）、**执行阶段**（可观察的攻击行为）和**最终影响**（造成的系统损害）。这个模型揭示了威胁如何随时间演变，并阐明了不同威胁类型之间的依赖关系（例如，间接提示注入与知识库中毒可能共享“未净化的第三方输入”这一前提条件）。
4.  **基于上下文的可能性与影响量化**：风险评估采用“可能性×影响”矩阵。可能性评估基于两个因素：攻击者所需的**业务规则知识**和**技术复杂性**。关键创新在于，对一个风险（如G1-R1）的评估，是基于其所有关联攻击路径中**最可行**的那一条来打分，而非对单个威胁进行孤立评分。这种上下文感知的方案确保了评分的一致性和现实性。影响评分则与医疗领域的实际危害（患者伤害、隐私泄露、运营中断）紧密对齐。
5.  **攻击路径分类**：为了细化分析，论文将攻击路径对风险的贡献分为**直接**、**间接**和**情境性**三类。这种分类有助于理解威胁在实践中的具体表现方式，并影响可能性评分和缓解措施的优先级制定（例如，直接路径通常需要更紧急的防御）。

总之，该论文通过将系统组件威胁映射到以具体安全目标为导向的攻击树，并引入结构化的威胁演化模型和上下文感知的风险量化框架，成功地将抽象、模糊的威胁转化为具体、可优先处理的风险实例，从而为LLM系统的安全设计提供了可操作的指导。

### Q4: 论文做了哪些实验？

该论文通过一个基于LLM的医疗系统案例研究，展示了其提出的目标驱动风险评估方法。实验设置上，研究者构建了攻击树（Attack Tree）来结构化地分析威胁，将高级目标（如“干预医疗流程”）分解为具体的攻击向量、前提条件和攻击路径。

数据集/基准测试方面，实验并未使用传统的数据集或基准，而是基于一个假设的LLM智能体医疗系统架构进行威胁建模分析。该系统包含用户Web应用、编排器（Orchestrator）、LLM以及外部工具等组件。

对比方法上，论文主要与传统的、通常较为抽象和模糊的威胁建模方法（如STRIDE）进行对比，突出了所提方法在提供具体攻击路径和上下文细节方面的优势。

主要结果方面，论文针对目标G1（干预医疗流程）识别并评估了四个主要风险：
1.  **G1-R1：危重疾病误诊**：最可行的路径是直接提示注入（Likelihood评分4-很可能），因其无需医疗专业知识或高级访问权限。影响评分为5（灾难性）。
2.  **G1-R2：未授权程序执行**：最可行的促成因素是提示注入与编排器操纵相结合。可能性评分为3（可能），影响评分为4（重大）。
3.  **G1-R3：药物推荐被篡改**：最可行的向量是提示注入（如插入对抗性指令），可能性评分为4（很可能），影响评分为4（重大）。
4.  **G1-R4：跨患者上下文污染**：主要由LLM会话管理不当和编排器错误驱动。可能性评分为3（可能），影响评分为3（中等）。

这些风险评估基于对攻击路径可行性和临床影响的分析，展示了如何将针对LLM的最新攻击（如提示注入）与传统攻击面（如会话劫持、中间人攻击）相结合，形成具体的攻击路径，从而为风险优先级排序提供依据。

### Q5: 有什么可以进一步探索的点？

该论文提出的基于攻击树的结构化风险评估框架，虽然为LLM系统安全提供了系统化分析思路，但仍存在一些局限性和可拓展方向。首先，当前的风险量化模型（可能性×影响）较为基础，未来可结合CVSS等多指标评分体系，或引入领域特定的威胁优先级标准，以实现更精细的风险校准。其次，研究尚未系统化提出针对攻击路径的具体缓解策略，未来需开发包含技术措施（如会话隔离、提示词净化）和运营保障（如访问控制）的完整防御方案，并基于高风险路径优化防护优先级。此外，案例研究聚焦医疗领域，其结论在其他高风险场景（如金融、自动驾驶）中的普适性有待验证，需通过跨领域专家评审确保模型贴合实际威胁环境。最后，论文提到利用LLM辅助威胁建模，这是一个富有潜力的方向：可探索LLM在自动化攻击树生成、威胁场景模拟或漏洞发现中的应用，以提升评估效率并降低对专家经验的依赖。未来还可考虑将动态风险监控与实时响应机制整合，形成闭环的安全防护体系。

### Q6: 总结一下论文的主要内容

该论文提出了一种面向LLM驱动系统的结构化、目标导向的风险评估方法，并以医疗健康系统为案例进行验证。核心问题是传统威胁建模方法在应对LLM等新型攻击面时，所识别的威胁往往抽象模糊，难以有效评估风险可能性和影响以进行优先级排序。

为此，作者构建了一个基于攻击树模型的风险评估框架。该方法从系统级威胁识别出发，围绕具有临床意义的对抗性目标（如误诊、数据泄露、服务中断）构建攻击树，详细描绘了攻击向量、前提条件和攻击路径。通过攻击树，系统性地推导出高风险项，并采用一个定制的“可能性×影响”框架进行量化评估，该框架兼顾了技术可行性和执行真实攻击所需的领域专业知识。

主要结论是，该方法将针对LLM的最新攻击与传统攻击方式相融合，为类似系统提供了可行的攻击路径分析。通过将抽象的威胁建模与可操作的风险推理相结合，实现了细粒度的、贴近现实的风险优先级排序，为安全关键环境中评估AI原生威胁提供了可扩展的基础，从而推动了LLM赋能系统的安全分析与“设计即安全”实践。
