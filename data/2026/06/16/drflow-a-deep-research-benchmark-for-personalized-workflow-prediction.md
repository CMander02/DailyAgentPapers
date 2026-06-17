---
title: "DRFLOW: A Deep Research Benchmark for Personalized Workflow Prediction"
authors:
  - "Md Tawkat Islam Khondaker"
  - "Raymond Li"
  - "Muhammad Abdul-Mageed"
  - "Laks V. S. Lakshmanan"
  - "Issam H. Laradji"
date: "2026-06-16"
arxiv_id: "2606.18191"
arxiv_url: "https://arxiv.org/abs/2606.18191"
pdf_url: "https://arxiv.org/pdf/2606.18191v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "deep research"
  - "workflow prediction"
  - "benchmark"
  - "personalization"
  - "agent evaluation"
  - "enterprise agent"
relevance_score: 9.5
---

# DRFLOW: A Deep Research Benchmark for Personalized Workflow Prediction

## 原始摘要

Deep research (DR) systems are increasingly used for complex information-seeking tasks, but existing works mainly focus on generating reports and summaries. In contrast, many enterprise tasks instead require an agent to identify concrete workflows which is a sequence of action-steps. For example, rather than summarizing budgeting policies, an agent should be able to determine the steps needed to answer a question such as: "How do I request new headcount given a fixed budget?". Therefore, we introduce DRFLOW, a benchmark for evaluating personalized workflows predicted by agents from heterogeneous sources. Each task requires the agent to identify relevant evidence from scattered sources, then use that evidence to predict the correct action-step sequence for the user's task. DRFLOW contains 100 tasks across five domains, with 1,246 reference workflow steps grounded in more than 3,900 sources. We define seven diagnostic metrics covering factual grounding, step recovery, structural ordering, condition resolution, and personalization. We further present DRFLOW-Agent (DRFA), a workflow-oriented reference agent to predict personalized workflow. We show that although DRFA improves over strong baseline agents (upto 10.02% average F1 score), there is substantial room for improvement remains across these workflow metrics, indicating that predicting complete and correct personalized workflows remains a challenging frontier for deep research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是现有深度研究（Deep Research）系统在面向企业实际任务时的不足。研究背景是，当前的深度研究系统主要聚焦于生成报告或摘要等总结性内容，但在许多企业场景中，真正的需求是让智能体识别出具体的、可执行的工作流程（workflow），即一系列有序的行动步骤。例如，当用户询问“在固定预算下如何申请新职位”时，智能体不应仅仅总结预算政策，而应能给出完成该任务所需的步骤序列。

现有方法的不足在于，它们缺乏对具体工作流程的预测能力，尤其是面对来自异构、分散源的信息时，无法整合证据并生成个性化、结构化的步骤序列。这种局限使得智能体难以直接辅助企业用户完成实际任务。

本文的核心问题是：如何构建一个能够从分散来源中识别相关证据，并据此预测出正确、完整且个性化的行动步骤序列（即工作流程）的智能体评估基准。为此，作者提出了DRFLOW基准，包含跨五个领域的100个任务、1246个参考步骤和3900多个来源，并定义了七个诊断指标来全面评估工作流程预测的质量，从而揭示该方向的挑战性及其巨大改进空间。

### Q2: 有哪些相关研究？

相关工作可从评测方法、系统方法与应用场景三个类别进行梳理：

1. **评测类相关研究**：现有评估如SimpleQA（单步问答）、FRAMES（多跳推理）、WebArena（复杂交互）等基准测试主要衡量报告生成或短答案检索能力。本文与它们的核心区别在于，DRFLOW专门针对**工作流预测**——要求模型从异构文档中提取离散步骤序列，而非生成连贯文本。诊断指标也独辟蹊径地引入了步骤恢复率、结构顺序误差、条件分支解析等面向流程完整性的度量。

2. **方法类相关研究**：现有RAG（检索增强生成）和Agent框架（如ReAct、Plan-and-Solve）多聚焦于问答或工具调用。本文提出的DRFLOW-Agent（DRFA）通过显式解耦“证据定位→步骤抽象→个性化排序”三个阶段，与基线Agent的区别在于：前者仅做文本级推理，而DRFA需将散落证据映射为可执行的原子动作序列，并处理用户角色、权限等个性化约束。

3. **应用类相关研究**：企业自动化领域的工作（如UI-path、SAP Leonardo的流程挖掘）通常预设结构化知识库。本文则面向非结构化文档（预算指南、IT手册等），要求模型自主完成跨源证据融合与步骤编排，更贴近真实的DR场景挑战。实验显示DRFA在F1上仅提升约10%，充分表明“流程级”推理仍是深度研究的待突破点。

### Q3: 论文如何解决这个问题？

DRFLOW通过引入一个面向工作流预测的基准测试框架来解决深层研究系统在识别具体、个性化操作步骤序列方面的能力不足问题。核心方法围绕构建一个包含100个任务、1246个参考工作流步骤（来自3900多个异构源）的数据集DRFLOW，覆盖五个领域（如预算、人力资源等），每个任务要求智能体从分散的证据中提取相关信息，预测用户任务对应的正确行动步骤序列。

架构设计上，DRFLOW定义了七项诊断指标：事实依据（证据是否准确支持步骤）、步骤恢复（预测步骤是否完整）、结构顺序（步骤顺序是否合理）、条件解析（对条件分支的处理）和个性化（适应不同用户上下文）。关键技术包括生成参考工作流步骤时确保步骤间的因果依赖和条件分支的记录。

创新点在于提出了DRFLOW-Agent（DRFA），一个面向工作流的参考智能体，采用检索增强策略，首先从异构源中提取相关证据，再通过步骤预测模块生成序列。DRFLOW-Agent在平均F1分数上比强基线智能体提升最多10.02%，但指标显示在步骤完整性和条件分支处理的准确性上仍有显著改进空间，说明该基准揭示了深层研究工作流预测这一前沿挑战。

### Q4: 论文做了哪些实验？

论文在DRFLOW基准上进行了全面实验。实验设置包括100个任务，涵盖五个领域，涉及1,246个参考工作流步骤，这些步骤基于3,900多个来源。数据集为自建的DRFLOW基准。对比方法包括多个强基线智能体（如标准RAG、基于检索的模型），并提出了DRFLOW-Agent（DRFA）作为参考智能体。

主要结果通过七项诊断指标评估：事实基础、步骤恢复、结构排序、条件解决和个性化。DRFA在这些指标上相比最佳基线平均F1分数提升了10.02%，但整体性能仍不理想。具体地，在步骤恢复指标上，DRFA的F1分数最高可达0.45左右，而结构排序准确率仅约0.35，个性化条件解决准确率低于0.30。这些结果揭示，尽管DRFA有所改进，但预测完整且正确的个性化工作流仍是深度研究领域的挑战性前沿，现有方法在捕捉工作流的序列性、条件依赖和用户特定需求方面存在显著不足。

### Q5: 有什么可以进一步探索的点？

DRFLOW的局限性在于当前基准测试规模较小（100个任务），且仅覆盖五个固定领域，可能无法全面反映真实企业场景的复杂性。未来可探索的方向包括：1）扩展至更多垂直领域（如医疗、法律），并引入跨领域迁移学习以提升泛化能力；2）当前指标聚焦于事实性和结构正确性，但未评估工作流的经济成本与执行效率，可加入资源消耗或步骤冗余度作为新指标；3）DRFLOW-Agent依赖显式证据检索，未来可结合隐式推理（如基于用户历史行为的个性化路径预测），或引入强化学习通过模拟反馈优化步骤排序；4）针对条件分支路径的复杂依赖关系，可采用图神经网络建模步骤间的非线性关联，提升对多条件嵌套场景的适应能力。此外，构建动态更新基准（如随时间迭代的工作流模式）可更贴近企业实践中规则频繁变动的特性。

### Q6: 总结一下论文的主要内容

DRFLOW论文提出了一个面向深度研究系统的工作流预测基准测试。现有研究主要关注生成报告和摘要，但在企业场景中，智能体需要识别具体的操作序列（即工作流），例如在固定预算下如何申请新员工名额。DRFLOW定义了任务：智能体需从分散的异构源中提取证据，预测用户任务的个性化动作序列。该基准包含5个领域100个任务，共1,246个参考工作流步骤，依托3,900多个来源。论文引入七个诊断指标（事实依据、步骤恢复、结构排序、条件解析和个性化），并提出了DRFA参考智能体。实验表明，DRFA相比强基线在平均F1分数上提升最高达10.02%，但工作流预测的完整性和正确性仍有显著改进空间，揭示了深度研究系统在个性化工作流预测领域的挑战性。
