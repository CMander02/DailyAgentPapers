---
title: "Quantifying the Expectation-Realisation Gap for Agentic AI Systems"
authors:
  - "Sebastian Lobentanzer"
date: "2026-02-23"
arxiv_id: "2602.20292"
arxiv_url: "https://arxiv.org/abs/2602.20292"
pdf_url: "https://arxiv.org/pdf/2602.20292v2"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent评测/基准"
  - "Agent部署与评估"
  - "期望-现实差距"
  - "实证研究"
  - "工作流集成"
  - "人机协作"
relevance_score: 8.5
---

# Quantifying the Expectation-Realisation Gap for Agentic AI Systems

## 原始摘要

Agentic AI systems are deployed with expectations of substantial productivity gains, yet rigorous empirical evidence reveals systematic discrepancies between pre-deployment expectations and post-deployment outcomes. We review controlled trials and independent validations across software engineering, clinical documentation, and clinical decision support to quantify this expectation-realisation gap. In software development, experienced developers expected a 24% speedup from AI tools but were slowed by 19% -- a 43 percentage-point calibration error. In clinical documentation, vendor claims of multi-minute time savings contrast with measured reductions of less than one minute per note, and one widely deployed tool showed no statistically significant effect. In clinical decision support, externally validated performance falls substantially below developer-reported metrics. These shortfalls are driven by workflow integration friction, verification burden, measurement construct mismatches, and systematic variation in who benefits and who does not. The evidence motivates structured planning frameworks that require explicit, quantified benefit expectations with human oversight costs factored in.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在识别并量化一个关键问题：Agentic AI系统（即能够自主规划、推理和执行多步骤任务的智能体）在部署前的预期收益与部署后的实际成果之间存在系统性且显著的差距，作者称之为“期望-现实差距”。论文指出，尽管这类系统被寄予厚望，承诺带来巨大的生产力提升（如软件开发速度加快、临床文档时间节省、临床决策准确性提高），但严格的实证证据（包括随机对照试验和独立验证）反复显示，实际效果往往远低于预期，甚至可能产生负面影响。论文的核心目标是：1）通过回顾软件工程、临床文档和临床决策支持三个领域的实证研究，具体量化这种差距的大小；2）深入分析导致这种差距的机制性驱动因素；3）论证并倡导采用结构化的规划框架来缩小这一差距，以实现更负责任和有效的AI部署。

### Q2: 有哪些相关研究？

论文引用了大量来自不同领域的实证研究，作为量化期望-现实差距的证据基础。在软件工程领域，引用了METR对经验丰富的开源开发者进行的随机对照试验（RCT），该试验发现开发者预期AI工具带来24%的速度提升，但实际却导致19%的减速。同时，也引用了GitHub Copilot在Upwork开发者上的对照试验，该试验在标准化任务中观察到了56%的速度提升，这凸显了任务复杂性对结果的影响。在临床文档领域，引用了UCLA对两种商业环境记录工具（DAX和Nabla）的大规模RCT，以及多项队列研究和前后对比研究，这些研究显示实际节省的时间（通常不到一分钟）远低于供应商声称的“数分钟”。在临床决策支持领域，引用了对Epic脓毒症模型的外部验证研究（显示AUROC从内部报告的0.76-0.83降至0.63）以及对IBM Watson for Oncology的回顾性研究（显示严格一致性远低于宣传数据）。此外，论文还引用了关于规划谬误的心理学经典研究（如Kahneman和Tversky的工作），以及关于AI对技能形成长期影响的研究。这些相关工作共同构成了一个证据体系，表明期望与现实的不匹配是一个跨领域、可重复观察到的现象，而非孤立事件。

### Q3: 论文如何解决这个问题？

论文并非提出一个新的技术算法，而是通过系统性文献综述和综合分析的方法来“解决”对期望-现实差距的认识和量化问题。其核心方法包括：1）证据合成：跨领域（软件工程、临床文档、临床决策支持）搜集和回顾最高质量的实证研究，特别是随机对照试验和独立外部验证，以提供具有说服力的量化数据。2）机制分析：基于证据，提炼出导致差距反复出现的三个核心驱动因素：工作流集成摩擦与部分采用（工具无法无缝融入现有流程，使用率低）、验证与审查负担（人类检查、修正AI输出所需的时间成本被低估）、测量构念不匹配（预部署宣传的指标与实际评估的指标不对应，例如“每次就诊节省分钟数” vs. “在笔记中的时间”）。3）强调异质性：论文明确指出，AI工具的效果并非均匀的，而是高度依赖于用户基线效率、任务复杂度和本地环境。平均效应会严重误导决策。4）提出解决方案框架：基于上述分析，论文论证了转向结构化规划的必要性，并引用了作者提出的“Agentic Automation Canvas”作为操作化示例。该框架要求明确量化多维度（时间、质量、风险、赋能、成本）的收益预期，纳入人类监督成本，建模效果异质性，并确保结果度量与初始预期使用相同的单位和粒度，以实现直接比较和追责。

### Q4: 论文做了哪些实验？

本文本身是一篇综述/观点论文，并未进行原创的实验。然而，论文的核心贡献在于对现有高质量实验证据进行了严谨的梳理、对比和综合分析。它重点依赖以下几类实验数据：1）随机对照试验：如METR对资深开发者的RCT（N=16，246个真实任务），UCLA对临床环境记录工具的RCT（涉及238名医生，约72,000次就诊）。这些实验提供了因果推断强度最高的证据。2）对照实验/队列研究：如GitHub Copilot在Upwork开发者上的对照实验，以及多项关于临床文档工具的配对队列研究和前后测试研究。3）独立外部验证研究：如对Epic脓毒症模型和IBM Watson for Oncology在真实临床环境中的性能验证，这些研究将开发商内部报告的性能指标与独立评估结果进行对比。4）调查研究：如对医生主观感知与客观测量时间节省之间关联的研究。论文通过整合这些来自不同领域、不同实验设计的实证结果，构建了一个强有力的论据，证明期望-现实差距是普遍存在的、可量化的，并且其驱动因素是可识别的。这种基于现有证据的元分析本身就是一种重要的研究方法。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来值得深入探索的方向：1）异质性的精细建模：需要更深入的研究来理解哪些具体的用户特征（如专业知识水平、认知风格）、任务属性（如结构化程度、创造性要求）和情境因素（如团队动态、组织文化）会调节AI智能体的效果。这有助于实现更精准的部署和目标定位。2）长期与二阶效应：现有研究多关注短期生产力指标。未来需要探索AI智能体对技能退化、组织学习、知识留存（如论文引用的教育研究所示）以及工作性质演变的长期影响。3）更全面的效益度量框架：需要开发超越“时间节省”和“准确率”的度量体系，纳入质量、风险、创新、员工福祉和公平性等多维度指标，以全面评估智能体的价值。4）减少集成摩擦的技术与组织设计：研究如何通过更好的UX设计、API集成、流程再造和变革管理，来降低工作流集成摩擦和提高采用率。5）验证负担的自动化缓解：探索如何通过AI本身（例如，开发更好的自我验证、不确定性量化或可解释性工具）来减少人类监督成本。6）结构化规划框架的有效性评估：像“Agentic Automation Canvas”这类框架本身需要在实际部署场景中进行实证检验，以评估其是否真能有效缩小期望-现实差距。

### Q6: 总结一下论文的主要内容

本文是一篇关于Agentic AI系统“期望-现实差距”的深度综述与论证。论文的核心贡献在于，通过系统回顾软件工程、临床文档和临床决策支持三大领域的严格实证研究（如随机对照试验和独立验证），首次量化并证实了在AI智能体部署中普遍存在的严重预期校准错误。例如，经验丰富的开发者预期24%的速度提升却遭遇19%的减速；临床文档工具声称节省数分钟但实测仅省数十秒；临床决策模型的内部高精度报告在外部验证中大幅下滑。论文深入剖析了导致这一差距的三大机制性驱动因素：工作流集成摩擦与部分采用、被低估的人类验证与审查负担、以及预部署与后部署测量指标的不匹配。同时，论文强调治疗效果存在高度异质性，平均效应具有误导性。基于这些证据，论文有力地论证了从临时性预期设定转向结构化、量化规划的必要性，并提出了诸如“Agentic Automation Canvas”的框架作为解决方案，要求明确量化多维度收益、计入监督成本、建模异质性并确保度量一致性。本文对AI智能体的负责任部署、投资决策和评估实践具有重要的警示和指导意义。
