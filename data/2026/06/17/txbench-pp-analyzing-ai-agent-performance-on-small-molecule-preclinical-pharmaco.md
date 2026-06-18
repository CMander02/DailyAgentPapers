---
title: "TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology"
authors:
  - "Hannah Le"
  - "Ramesh Ramasamy"
  - "Alex Urrutia"
  - "Mahsa Yazdani"
  - "Tim Proctor"
  - "Kenny Workman"
date: "2026-06-17"
arxiv_id: "2606.19245"
arxiv_url: "https://arxiv.org/abs/2606.19245"
pdf_url: "https://arxiv.org/pdf/2606.19245v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "AI Agent"
  - "Benchmark"
  - "Drug Discovery"
  - "Preclinical Pharmacology"
  - "Automated Reasoning"
  - "Tool Use"
  - "Evaluation"
relevance_score: 8.5
---

# TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology

## 原始摘要

Artificial intelligence (AI) agents promise to accelerate drug discovery by compressing interpretation and decision-making loops, but practical deployment requires trusted evaluation on realistic program decisions. We introduce TherapeuticsBench Preclinical Pharmacology (TxBench-PP), a verifiable benchmark for small-molecule preclinical pharmacology and the first focused slice of a broader TherapeuticsBench effort across drug-discovery stages and therapeutic modalities. TxBench-PP tests whether agents can recover accurate conclusions from real-world assay data rather than memorized facts from literature. The benchmark contains 100 evaluations indexed by program stage, assay type, and task structure, spanning mechanism-of-action (MoA) and pharmacodynamic (PD) reasoning, compound-target engagement, causal target validation, developability and safety, and translational efficacy. Agents receive realistic workflow snapshots, inspect files in a coding environment, and return structured answers graded deterministically. Across 16 model-harness configurations, comprising 11 models and 4,800 trajectories, no system reliably recovered preclinical pharmacology decisions. The strongest configuration, Claude Opus 4.8 / Pi, passed 59.3\% of endpoint attempts (178/300; 95\% CI, 51.1-67.6), followed by GPT-5.5 / Pi at 55.3\% (166/300; 47.0-63.6).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何可靠地评估AI智能体在小分子临床前药理学实际工作流中的决策能力问题。研究背景是：AI智能体有望通过压缩药物发现中的解读和决策环节来加速研发，但实际部署前需要对其在真实项目决策上的表现进行可信评估。现有方法的不足在于：大多数生物学基准测试要么依赖从文献中记忆的事实，要么缺乏对药物发现这一复杂生态系统中各种局部科学判断的专注评测——这个系统涉及不同的检测类别、开发阶段、治疗模式和决策类型。本文要解决的核心问题是：构建一个可验证的基准测试TxBench-PP，专门测试AI智能体是否能够从真实工作流数据（如作用机制、药效学、靶点结合、可开发性及安全性等）中准确恢复临床前药理学的决策结论，而非依靠记忆的文献知识。实验结果表明，目前最强的模型配置（Claude Opus 4.8 / Pi）也仅通过了59.3%的测试端点，说明现有智能体系统尚无法可靠地执行此类任务。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要集中在生物医药领域的AI Agent评测基准。在评测类工作中，近期涌现出一些强调可验证分析任务和真实科学数据的生物学Agent基准，这些工作与TxBench-PP的目标一致，即评估Agent处理实际科学数据的能力。然而，TxBench-PP与这些工作的关键区别在于：它专门聚焦于小分子临床前药理学这一特定的药物发现阶段，而不是覆盖整个生物学或药物发现全流程。在方法类工作中，现有研究探讨了如何通过后训练、工具使用和领域特定脚手架来编码药物发现流程中各步骤的特定知识，并部署到实际数据解读工作流中。TxBench-PP在此基础上进一步要求Agent从真实实验数据中恢复准确结论，而非依赖文献中记忆的事实。此外，TxBench-PP是更广泛的TherapeuticsBench计划的首个聚焦子集，该计划将覆盖药物发现各阶段和治疗模式，而当前基准仅针对临床前小分子药物开发阶段，其他临床阶段和非小分子模态则留给后续工作。总体而言，TxBench-PP填补了现有评测在临床前药理学决策评估方面的空白。

### Q3: 论文如何解决这个问题？

TxBench-PP通过构建一个可验证的基准测试框架来解决AIagent在临床前药理学任务中的性能评估问题。核心方法围绕现实工作流模拟、确定性评分和系统性陷阱设计展开。

整体框架包含100个评估任务，覆盖从疾病模型、筛选确认到转化药效的8个程序阶段。每个评估任务由三部分组成：真实化验数据工件（如转录组图谱、化学蛋白质组学数据）、解释数据所需的元数据、以及任务描述和结构化答案。任务设计刻意避免依赖文献已知事实，而是要求agent从提供的数据中推导出结论。

主要模块包括：1) **任务分类体系**，沿程序阶段、化验类型和任务结构三个轴标注；2) **确定性评分系统**，使用结构化答案的确定性函数进行评分，检查标签集、数值容差、排序关系或分类选择；3) **决策阻塞点追踪**，通过人工轨迹检查识别tox-species mismatch、hook效应等关键失败模式，用于解释失败原因。

创新点在于：采用真实工作流快照而非简化问题，模拟科学家在分析点所知的完整上下文；设计反过拟合陷阱，阻止系统仅凭训练知识作答而不进行实证探索；通过人工审查和模型轨迹检查迭代优化任务，确保答案只能通过数据交互获得。评估结果显示，最强配置Claude Opus 4.8/Pi仅通过59.3%的端点尝试，表明当前AI系统在现实临床前药理决策中存在显著性能缺口。

### Q4: 论文做了哪些实验？

论文在TxBench-PP基准测试上进行了实验，该基准包含100个从实际临床前药理学工作流程中提取的评估任务，涵盖作用机制、药效学推理、化合物-靶点结合、因果靶点验证、可开发性与安全性以及转化疗效等多个阶段。实验设置了16种模型-代理框架组合，涉及11个模型（如Claude Opus 4.8、GPT-5.5、Gemini 3.5 Flash等）和3个代理框架（Pi、Claude Code、OpenAI Codex），每个配置在每个任务上独立运行3次，共产生4,800条代理轨迹。对比方法包括不同的模型和框架配置，主要结果以终点通过率（即通过轨迹的百分比）为指标。最佳配置是Claude Opus 4.8 / Pi，通过率为59.3%（178/300；95% CI：51.1-67.6），其次为GPT-5.5 / Pi的55.3%（166/300；47.0-63.6）、Claude Opus 4.8 / Claude Code的54.7%（164/300；45.9-63.4）和Gemini 3.5 Flash / Pi的51.3%（154/300；42.9-59.8）。这些置信区间重叠，表明没有单一系统明显胜出。即使最好的模型，在100个任务中也仅能完全通过41个（三次独立运行全部通过）。实验进一步发现，性能因程序阶段而异（从筛选的27%到药物反应的55%），且整体准确率无法预测关键的推进决策（Spearman ρ = 0.08）。框架选择对性能有显著影响，Pi框架在匹配的模型上平均领先Claude Code 4.4个百分点。手动审查1,834条失败轨迹发现，71%的可归因科学错误源于方法错误或校准错误。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性与研究缺口，未来可探索以下方向：首先，当前基准聚焦于小分子临床前药理学，未来应扩展至抗体、ADC、蛋白降解剂、寡核苷酸、细胞与基因疗法等非小分子模态，并垂直拓展至更广泛的药物基因组学与临床任务。其次，现有评估仅为“单点快照”，缺乏跨发现、开发与转化全流程的长期追踪能力，构建类似其他生物领域的长程基准将更贴近真实药物研发周期。在Agent能力提升上，手动轨迹审查揭示了QC统计误读、生物上下文误解与过度依赖记忆等系统性失败，需设计专门模块纠正此类错误，例如引入内部逻辑校验机制或领域知识图谱辅助推理。此外，当前Agent难以区分局部实验噪声与全局结论，可探索多步因果推理与不确定性量化方法，减少“弱候选被推进、强候选被丢弃”的风险，最终实现可靠可复用的科研助手。

### Q6: 总结一下论文的主要内容

TxBench-PP是一个针对小分子临床前药理学的可验证基准，旨在评估AI智能体在真实世界药物发现决策中的表现。该基准包含100个评估任务，涵盖作用机制、药效学推理、化合物-靶点结合、因果靶点验证、可开发性与安全性以及转化疗效等多个维度。智能体需接收真实工作流程快照，在编码环境中检查文件并返回结构化答案。在16个模型-框架配置（包含11个模型和4,800条轨迹）中，最强配置Claude Opus 4.8/Pi仅通过59.3%的终点尝试，GPT-5.5/Pi获得55.3%。结果表明，尽管智能体能完成部分任务，但尚未达到可靠科学助手的水平，在质量控制、统计、生物学背景或分子特性推理方面存在错误。该基准填补了药物发现领域缺乏可验证AI评估工具的空白，为智能体在临床前药理学的实际部署提供了重要参考。
