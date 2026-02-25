---
title: "Quantifying the Expectation-Realisation Gap for Agentic AI Systems"
authors:
  - "Sebastian Lobentanzer"
date: "2026-02-23"
arxiv_id: "2602.20292"
arxiv_url: "https://arxiv.org/abs/2602.20292"
pdf_url: "https://arxiv.org/pdf/2602.20292v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent评测/基准"
  - "Agent安全"
  - "Agent部署与集成"
  - "实证研究"
  - "期望-现实差距"
relevance_score: 8.5
---

# Quantifying the Expectation-Realisation Gap for Agentic AI Systems

## 原始摘要

Agentic AI systems are deployed with expectations of substantial productivity gains, yet rigorous empirical evidence reveals systematic discrepancies between pre-deployment expectations and post-deployment outcomes. We review controlled trials and independent validations across software engineering, clinical documentation, and clinical decision support to quantify this expectation-realisation gap. In software development, experienced developers expected a 24% speedup from AI tools but were slowed by 19% -- a 43 percentage-point calibration error. In clinical documentation, vendor claims of multi-minute time savings contrast with measured reductions of less than one minute per note, and one widely deployed tool showed no statistically significant effect. In clinical decision support, externally validated performance falls substantially below developer-reported metrics. These shortfalls are driven by workflow integration friction, verification burden, measurement construct mismatches, and systematic heterogeneity in treatment effects. The evidence motivates structured planning frameworks that require explicit, quantified benefit expectations with human oversight costs factored in.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在识别并量化一个关键问题：Agentic AI系统（即能够自主规划、推理和执行多步骤任务的智能体）在部署前的预期收益与部署后的实际成果之间存在系统性且显著的差距，作者称之为“期望-现实差距”。论文指出，尽管企业和开发者对这类AI代理抱有巨大的生产力提升期望（如大幅缩短时间、提升准确性），但严格的实证证据（包括随机对照试验和独立验证）反复显示，实际效果往往远低于预期，甚至可能产生负面影响。这种差距并非偶然，而是由工作流集成摩擦、验证负担、测量指标不匹配以及处理效应的异质性等系统性因素驱动的。论文的核心目标是，通过综合软件工程、临床文档记录和临床决策支持这三个关键领域的证据，揭示这一差距的普遍性、规模和根本原因，从而为更负责任、更现实的AI代理部署和规划框架提供依据。

### Q2: 有哪些相关研究？

论文引用了大量相关研究来支撑其论点，主要分为三类：1) **软件工程领域**：引用了METR对经验丰富的开源开发者进行的随机对照试验，该试验发现AI工具反而使任务完成时间增加了19%，与开发者预期的24%提速形成巨大反差。同时，也引用了GitHub Copilot在Upwork开发者上的早期试验，该试验在标准化任务中观察到了显著的速度提升，这突显了任务复杂性（标准化vs.高上下文真实任务）对结果的影响。此外，还引用了关于Copilot生成代码安全性的研究，以及微软和埃森哲的现场实验。2) **临床文档记录领域**：引用了UCLA关于两种商用环境AI抄写员（DAX和Nabla）的随机对照试验，结果显示效果有限甚至不显著。同时引用了其他队列研究和前后对比研究，均显示时间节省远低于供应商宣传（如“每分钟节省” vs. “实际节省不足一分钟”）。3) **临床决策支持领域**：重点引用了对Epic脓毒症模型和IBM Watson for Oncology的外部验证研究，这些研究发现，模型在真实世界中的性能（如AUROC、一致性）远低于开发者最初报告的内部指标。论文将这些研究与心理学中的“规划谬误”理论联系起来，表明期望与现实的脱节是一个普遍存在的认知偏差。本文与这些工作的关系在于，它并非提出新的AI方法，而是对现有实证证据进行系统性综述和整合，首次明确地将跨领域的“期望-现实差距”概念化、量化，并提炼出其背后的共同驱动机制。

### Q3: 论文如何解决这个问题？

论文采用了一种基于证据综述和概念分析的方法来解决“期望-现实差距”问题，而非提出新的技术算法。其核心方法论和贡献在于：1) **系统性证据整合**：作者精心选取了软件工程、临床文档和临床决策支持这三个具有代表性且研究较为充分的领域，回顾了其中最严谨的实证研究（如随机对照试验、外部验证），通过具体数据量化差距。例如，在软件工程中揭示了43个百分点的校准误差；在临床文档中对比了供应商宣传的“数分钟节省”与实测的“不足一分钟节省”。2) **识别并归纳驱动因素**：基于证据，论文提炼出导致期望系统性高于现实的四个关键机制性驱动因素：**工作流集成摩擦与部分采用**（工具无法完全融入现有流程，采用率低）、**验证与审查负担**（人类检查、调试AI输出所花费的时间被低估）、**测量构念不匹配**（宣传指标与实际评估指标不一致，如“工作流影响” vs. “特定任务时间”）以及**处理效应的异质性**（AI效果因用户技能、任务复杂度、本地环境而异，并非均匀受益）。3) **提出结构化规划框架**：作为解决方案，论文论证了从临时性期望设定转向结构化规划的必要性，并提出了具体的设计原则，包括：要求明确量化的收益预期、纳入人类监督成本、确保结果度量与初始预期单位一致、以及明确建模异质性（指明哪些用户和任务类型会受益）。论文最后介绍了**Agentic Automation Canvas (AAC)** 作为实现这些原则的具体框架，旨在通过一个结构化的“画布”来捕获和对比用户期望与开发者评估，将双向契约正式化，从而在项目设计阶段就主动管理期望与现实之间的差距。

### Q4: 论文做了哪些实验？

本文本身是一篇综述/观点论文，并未进行新的原始实验。它的“实验”部分体现在对已有高质量实证研究的系统性回顾、分析和对比上。作者设定了严格的证据筛选标准，主要聚焦于**随机对照试验**和**独立外部验证**这类方法学上最稳健的研究。具体回顾的“实验”包括：1) **软件工程**：详细分析了METR的RCT（16名经验开发者，246个真实任务），该实验测量了预期速度提升与实际任务完成时间的变化。同时对比了GitHub Copilot早期在标准化任务上的RCT结果，以说明任务背景的重要性。还引用了关于代码安全性的分析实验。2) **临床文档记录**：深入解读了UCLA的RCT（238名医生，约7.2万次就诊），该实验比较了两种AI抄写员与常规护理的效果，测量了“记录内时间”等客观指标。此外，还回顾了多个队列研究和前后对比研究，这些研究测量了AI工具使用前后医生在电子健康记录上花费的时间。3) **临床决策支持**：重点分析了针对Epic脓毒症模型和IBM Watson for Oncology的外部验证研究。这些研究在独立、真实世界的数据集上重新评估了模型的性能指标（如AUROC、与专家建议的一致性），并与开发者最初报告的内部性能进行对比。通过这些回顾，论文有效地“实验”了其核心假设——期望与现实存在显著差距，并利用这些高质量研究的数据来量化差距的大小和一致性。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来值得深入探索的方向：1) **异质性的精细建模与预测**：当前证据表明AI代理的效果高度依赖于用户特征（如技能水平、基线效率）、任务类型和上下文。未来研究需要开发更精细的模型来预测特定子群体在特定任务上的收益或成本，以指导精准部署，而非依赖“平均效应”。2) **长期影响与技能侵蚀**：论文提及的相邻证据（如ChatGPT损害学生长期记忆、AI使用削弱程序员概念理解）暗示了短期生产力指标可能无法捕捉的长期风险。需要更多纵向研究来评估AI代理对用户专业技能形成、知识保留和决策能力的长期影响。3) **更全面的效益度量框架**：当前度量多聚焦于时间节省或任务完成率。需要开发包含代码质量、系统安全性、临床结果、用户福祉、团队协作动态以及组织学习能力在内的多维效益度量体系。4) **改善集成与采用策略**：工作流摩擦和部分采用是主要障碍。未来研究应探索如何通过更好的用户体验设计、组织变革管理和定制化集成来提升采用率和工具效用。5) **期望校准与沟通机制**：如何设计有效的干预措施（如基于AAC的规划流程）来校准开发者、用户和管理者的期望，并建立更透明的性能沟通渠道，是一个重要的跨学科（人机交互、心理学、管理学）研究课题。6) **新领域验证**：本文聚焦于三个领域，未来需要在客户服务、教育、法律等其他Agentic AI应用领域进行类似的严格实证评估，以检验“期望-现实差距”的普遍性。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是首次系统性地提出并量化了Agentic AI系统中的“期望-现实差距”。通过对软件工程、临床文档和临床决策支持领域内最严谨的实证研究（随机对照试验和外部验证）进行综述，论文揭示了一个一致且显著的模式：部署前的预期收益（来自用户预测、供应商宣传或开发者报告）系统地、大幅度地高估了部署后的实际成果。例如，经验丰富的开发者预期AI辅助能提速24%，实际却被拖慢19%；临床AI抄写员宣传节省数分钟，实测仅节省数十秒；临床决策模型的真实世界性能远低于内部报告指标。论文深入分析了导致这一差距的四个根本原因：工作流集成摩擦、人类验证负担、测量指标不匹配以及处理效应的异质性。基于此，作者论证了从模糊承诺转向结构化、量化规划的必要性，并提出了具体的设计原则，包括明确量化收益预期、扣除监督成本、确保度量一致性和建模异质性。最后，论文介绍了Agentic Automation Canvas (AAC)作为实现这些原则的框架。本文的意义在于为AI代理的负责任部署敲响了警钟，强调成功的应用不仅取决于模型能力，更取决于对现实世界集成成本和社会技术因素的深刻理解与规划。
