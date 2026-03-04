---
title: "Architecting Trust in Artificial Epistemic Agents"
authors:
  - "Nahema Marchal"
  - "Stephanie Chan"
  - "Matija Franklin"
  - "Manon Revel"
  - "Geoff Keeling"
  - "Roberta Fischli"
  - "Bilva Chandra"
  - "Iason Gabriel"
date: "2026-03-03"
arxiv_id: "2603.02960"
arxiv_url: "https://arxiv.org/abs/2603.02960"
pdf_url: "https://arxiv.org/pdf/2603.02960v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 评测/基准"
  - "Agent 安全"
  - "多智能体系统"
  - "知识推理"
relevance_score: 7.5
---

# Architecting Trust in Artificial Epistemic Agents

## 原始摘要

Large language models increasingly function as epistemic agents -- entities that can 1) autonomously pursue epistemic goals and 2) actively shape our shared knowledge environment. They curate the information we receive, often supplanting traditional search-based methods, and are frequently used to generate both personal and deeply specialized advice. How they perform these functions, including whether they are reliable and properly calibrated to both individual and collective epistemic norms, is therefore highly consequential for the choices we make. We argue that the potential impact of epistemic AI agents on practices of knowledge creation, curation and synthesis, particularly in the context of complex multi-agent interactions, creates new informational interdependencies that necessitate a fundamental shift in evaluation and governance of AI. While a well-calibrated ecosystem could augment human judgment and collective decision-making, poorly aligned agents risk causing cognitive deskilling and epistemic drift, making the calibration of these models to human norms a high-stakes necessity. To ensure a beneficial human-AI knowledge ecosystem, we propose a framework centered on building and cultivating the trustworthiness of epistemic AI agents; aligning AI these agents with human epistemic goals; and reinforcing the surrounding socio-epistemic infrastructure. In this context, trustworthy AI agents must demonstrate epistemic competence, robust falsifiability, and epistemically virtuous behaviors, supported by technical provenance systems and "knowledge sanctuaries" designed to protect human resilience. This normative roadmap provides a path toward ensuring that future AI systems act as reliable partners in a robust and inclusive knowledge ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由大型语言模型（LLM）演变为“人工认知主体”所带来的新型信任与治理挑战。研究背景是，以LLM为代表的AI系统正从被动信息工具转变为能自主追求认知目标、主动塑造我们共享知识环境的“认知主体”。它们越来越多地承担信息策展、知识生成乃至专业建议的角色，深度介入人类的知识创造、管理和综合过程，尤其在复杂的多主体交互中形成了新的信息依赖网络。

现有方法的不足在于，传统的AI评估与治理范式主要针对作为工具的系统，侧重于其输出内容的准确性或安全性。然而，当AI成为具有自主性的认知主体时，其运作方式、可靠性以及对个人和集体认知规范的校准程度，将深刻影响人类的决策与知识生态。当前缺乏一个系统的框架来评估和确保这些认知主体在动态、交互环境中的可信赖性，也未能充分应对其可能引发的认知能力退化、认知漂移等系统性风险。

因此，本文要解决的核心问题是：在AI系统日益成为自主认知主体的趋势下，我们应在何种基础上信任它们提供的信息和参与知识创造？需要建立怎样的设计、评估、治理框架和社会技术基础设施，才能确保这些认知主体可靠地增强而非损害人类的知识生态系统，使其成为人类认知的可靠伙伴，并与人类的认知目标保持一致。论文试图通过构建一个以可信度为核心、融合技术规范与社会治理的综合性框架来回应这一问题。

### Q2: 有哪些相关研究？

本文的相关研究可大致分为三类：方法类、应用类和治理/评测类。

在**方法类**研究中，相关工作主要聚焦于提升大语言模型（LLM）的推理、规划、工具使用和持续学习能力。例如，研究通过扩展测试时计算和采用新推理方法来改进通用推理；通过集成世界模型和仿真环境来增强情境感知；以及探索工具学习的自动化。本文与这些工作的关系在于，它将这些技术进展视为构建“认知AI智能体”的基础能力。区别在于，本文并非提出新的技术方法，而是从更高层次的系统架构视角，探讨这些能力汇聚成自主追求认知目标的智能体时所引发的全新挑战和治理需求。

在**应用类**研究中，已有工作探索了AI在科学发现、新闻生成、教育、内容创作等领域的应用。本文系统性地归纳并扩展了这些潜在角色，将其明确为科学家、历史学家、记者、档案管理员、教育家、文化创造者等具体的“认知智能体”职能。本文与这些应用研究的区别在于，它特别强调了智能体在**多智能体交互**的复杂环境中运作，以及它们如何主动**塑造外部认知环境**，而不仅仅是完成特定任务。

在**治理与评测类**研究中，现有工作关注AI的可信度、对齐和安全性评估。本文提出的框架（强调认知能力、可证伪性和认知美德）与这类研究目标一致，但进行了重要拓展。本文特别指出，由于认知智能体将创造新的信息相互依赖性，因此评估和治理需要**根本性转变**，从评估单一模型转向校准整个生态系统。本文提出的“知识溯源系统”和“知识庇护所”等支撑性社会认知基础设施，是区别于传统技术对齐方案的新思路。

### Q3: 论文如何解决这个问题？

论文通过提出一个以“可信赖性”为核心的规范性框架来解决AI认知代理的评估与治理问题。该框架旨在确保AI代理能够作为人类知识生态系统中可靠的合作伙伴，其核心方法围绕构建可信赖的认知AI代理、使其与人类认知目标对齐，并强化周边的社会认知基础设施。

整体框架强调，可信赖的认知AI代理必须具备三个关键属性：认知能力、可证伪性和认知美德行为。这些代理层面的属性必须锚定在一个具有韧性的社会技术生态系统中，该系统包括用于溯源和验证的稳健技术基础设施，以及增强人类认知韧性的社会结构。

在架构设计与关键技术层面，论文提出了以下主要模块与创新点：
1.  **可论证的认知能力**：这要求AI代理具备理解和评估不同领域知识的能力。论文超越了当前基于静态问答套件的基准测试范式，提出了动态评估方法，以测试代理在实时信息环境中保持知识准确性的能力，包括对知识衰减的意识和跨领域信息迁移能力。此外，还强调需要评估代理在分布式认知网络中验证信息的能力，包括评估其他代理的知识与可信度，以及对涉及恶意代理的“认知供应链攻击”进行压力测试。
2.  **稳健的可证伪性管道**：承认错误无法完全消除，论文主张建立可证伪性系统，使AI代理的推理步骤受到审查并可迭代改进。关键技术在于要求代理能够清晰阐明其推理过程，提供完整的“论证审计线索”，包括其得出结论的步骤、使用的工具和审查标准。这超越了当前仅追溯信息来源的方法，要求以人类可解释的方式忠实表达推理过程，并能说明其结论在何种条件下将不再成立。
3.  **认知美德行为**：AI代理应展现与人类理想认知代理相一致的行为美德，主要包括诚实/真实性、知识谦逊（承认自身知识局限）以及追求准确性并修正信念的倾向。论文从功能主义视角指出，无论内部状态如何，可靠展现这些行为的代理就履行了与人类对应物相同的核心功能。当前的研究正通过对齐技术、自我评估、世界建模等方法试图灌输这些美德，但诸如“幻觉”等问题依然存在。

创新点在于将传统的信任与专业知识概念系统性地应用于AI代理，并构建了一个融合技术属性（能力、可证伪性）与行为规范（美德）的多维评估框架。同时，框架将代理本身的属性与其运作的生态系统（技术溯源系统、“知识庇护所”等社会结构）紧密结合，强调治理需从单一模型评估转向对整个互动知识生态的校准，以应对AI代理带来的新型信息相互依赖关系。

### Q4: 论文做了哪些实验？

该论文未报告具体的实验设置、数据集或基准测试，也未提供量化的关键数据指标。作为一篇理论框架性论文，其核心贡献在于提出一个关于构建可信人工认知代理的规范性路线图，而非进行实证研究。论文的主要“工作”是论证和概念构建，其“对比”对象是当前AI评估与治理范式的不足。作者主张，由于AI作为认知代理（能自主追求认知目标并塑造知识环境）带来的新型信息依赖关系，传统的评估方法已不适用，必须转向以信任架构为中心的治理框架。主要提出的解决方案包括：确保AI代理具备认知能力、可证伪性和认知美德；通过技术溯源系统记录其知识谱系；建立“知识保护区”以维护人类认知韧性。因此，论文的“结果”是一套旨在使AI成为可靠知识伙伴的原则性框架，而非可量化的实验性能结果。

### Q5: 有什么可以进一步探索的点？

本文探讨了构建可信赖的认知AI代理的框架，但其局限性和未来研究方向仍值得深入探索。论文主要从宏观框架和原则层面进行论述，缺乏具体的技术实现路径和可量化的评估指标。例如，如何在实际系统中精确衡量“认知能力”或“稳健的可证伪性”并未明确。

未来研究可以从以下几个方向展开：首先，在技术层面，需要开发更透明的溯源系统和可解释的决策机制，以应对多代理系统中可能出现的“验证危机”和“认知依赖”。其次，在交互设计上，应探索如何平衡个性化推荐与认知多样性，避免陷入“认知单一化”和“信息茧房”，例如设计能主动引入对立观点的“反共识”机制。再者，论文提及了“知识庇护所”的概念，但如何构建并维护这种抵御系统性认知扭曲的基础设施，需要结合分布式系统和治理模型进行跨学科研究。最后，关于代理间的协作与竞争，特别是它们如何形成集体智能并可能发展出人类难以理解的内部规范，是一个高风险但至关重要的前沿课题，需要建立新的安全评估范式。

### Q6: 总结一下论文的主要内容

这篇论文探讨了大型语言模型作为“认知代理”的兴起及其对人类知识生态的深刻影响。核心问题是：当AI系统能够自主追求认知目标并主动塑造我们的共享知识环境时，我们应在何种基础上信任它们？论文认为，AI从信息工具转变为自主的“人工认知代理”，这带来了新的信息依赖关系，要求我们在AI的设计、评估和治理上进行根本性转变。

论文的主要贡献包括：1）概念上，界定了“认知AI代理”的功能定义及其在未来知识生态中的潜在角色；2）分析了这些系统在个体和社会层面给认知与知识形成带来的风险（如认知能力退化、认知漂移）与机遇（如增强人类判断和集体决策）；3）提出了一个确保认知信任的规范性框架，核心在于AI代理需具备可验证的认知能力、强健的可证伪性以及符合认知美德的行为，并与人类认知目标对齐；4）建议了支持性社会技术基础设施，包括技术溯源系统和旨在保护人类韧性的“知识庇护所”。

主要结论是，为确保构建一个有益的人机知识生态系统，必须将AI代理的信任worthiness作为中心，通过技术标准和社会治理机制，使其成为可靠的知识伙伴，从而避免认知损害，促进知识生态的稳健与包容。
