---
title: "Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark"
authors:
  - "Lalitha Pranathi Pulavarthy"
  - "Raajitha Muthyala"
  - "Aravind V Kuruvikkattil"
  - "Zhenan Yin"
  - "Rashmita Kudamala"
  - "Saptarshi Purkayastha"
date: "2026-02-23"
arxiv_id: "2602.19502"
arxiv_url: "https://arxiv.org/abs/2602.19502"
pdf_url: "https://arxiv.org/pdf/2602.19502v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agentic AI"
  - "多模态"
  - "临床预测"
  - "人机协作"
  - "基准评测"
  - "特征工程"
  - "医疗AI"
relevance_score: 8.0
---

# Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark

## 原始摘要

Agentic AI systems are increasingly capable of autonomous data science workflows, yet clinical prediction tasks demand domain expertise that purely automated approaches struggle to provide. We investigate how human guidance of agentic AI can improve multimodal clinical prediction, presenting our approach to all three AgentDS Healthcare benchmark challenges: 30-day hospital readmission prediction (Macro-F1 = 0.8986), emergency department cost forecasting (MAE = $465.13), and discharge readiness assessment (Macro-F1 = 0.7939). Across these tasks, human analysts directed the agentic workflow at key decision points, multimodal feature engineering from clinical notes, scanned PDF billing receipts, and time-series vital signs; task-appropriate model selection; and clinically informed validation strategies. Our approach ranked 5th overall in the healthcare domain, with a 3rd-place finish on the discharge readiness task. Ablation studies reveal that human-guided decisions compounded to a cumulative gain of +0.065 F1 over automated baselines, with multimodal feature extraction contributing the largest single improvement (+0.041 F1). We distill three generalizable lessons: (1) domain-informed feature engineering at each pipeline stage yields compounding gains that outperform extensive automated search; (2) multimodal data integration requires task-specific human judgment that no single extraction strategy generalizes across clinical text, PDFs, and time-series; and (3) deliberate ensemble diversity with clinically motivated model configurations outperforms random hyperparameter search. These findings offer practical guidance for teams deploying agentic AI in healthcare settings where interpretability, reproducibility, and clinical validity are essential.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个核心矛盾：在医疗临床预测任务中，日益强大的自主智能体（Agentic AI）系统虽然能自动化数据科学流程，但缺乏关键的领域专业知识，而纯粹的自动化方法难以提供这种专业知识。具体而言，论文试图探索和验证如何通过“人类引导”来增强智能体AI，以提升其在多模态临床预测任务中的表现。研究以AgentDS医疗健康基准的三个挑战任务（30天再入院预测、急诊科费用预测、出院准备评估）为具体场景，旨在系统性地衡量人类专家在关键决策点（如多模态特征工程、模型选择、验证策略）的指导所带来的价值，并提炼出可推广的实践经验，以弥合自动化优化与临床可解释性、可复现性及领域知识整合之间的鸿沟。

### Q2: 有哪些相关研究？

相关工作主要围绕三个方向：1) **医疗预测的多模态机器学习方法**，例如结合结构化电子健康记录（EHR）、临床文本和时序生命体征的模型，在再入院预测等任务上取得高AUROC（如Loutati等人，2024）；图神经网络（如Tang等人，2023）通过建模患者相似性进一步提升性能。2) **自主Agentic AI系统在医疗领域的应用**，例如多智能体LLM框架（如MDAgents、EHRAgent）通过代码生成和协作提升医疗推理任务准确率（Kim等人，2024；Shi等人，2024）；LLM驱动的数据科学代理（如Rahman等人，2025）被探讨用于自动化工作流。3) **医疗预测中特征工程与人工干预的重要性**，研究指出临床知识指导的特征（如早期预警评分统计特征）对预测至关重要（Bishop等人，2021），且医疗场景需平衡自动化与可解释性（Karunanayake等人，2025）。

本文与这些研究的关系是：**批判性继承与拓展**。它认可多模态方法（方向1）和Agentic AI的潜力（方向2），但指出完全自主的代理在临床领域存在局限（如缺乏领域知识）。因此，本文**重点融合方向3的思想**，提出“人工引导的Agentic AI”范式，强调在特征工程、模型选择等关键决策点注入临床专家判断，并通过AgentDS基准系统量化人工干预的价值（如多模态特征提取带来+0.041 F1提升）。这弥补了现有研究（如Ashfaq等人，2019的基准）仅评估纯自动化或纯人工方法的不足，为医疗AI部署提供了兼顾性能与可解释性的协作框架。

### Q3: 论文如何解决这个问题？

该论文通过一种迭代式的人机协作工作流来解决临床预测任务中纯自动化方法缺乏领域知识的问题。核心方法是让智能体系统处理常规的数据科学操作（如数据加载、预处理、初始模型训练和基于贝叶斯优化的超参数搜索），而人类分析师在关键决策点进行干预，以引导整个流程。

**架构设计**：针对三个不同的临床预测任务，论文设计了定制化的特征工程和模型架构，但都遵循相同的人机协作范式。系统首先由智能体生成基线解决方案，人类通过交叉验证误差分析和临床推理诊断其局限性，然后指导下一轮迭代。这种设计确保了领域知识被系统地注入到工作流的各个关键环节。

**关键技术**：
1.  **领域知识驱动的特征工程**：这是性能提升的最大贡献者。人类分析师指导智能体超越简单的自动化特征提取，根据临床假设创建具有解释性的特征。例如，在再入院预测任务中，工程师了基于时间（如周末出院标志）、非线性效应（年龄平方）、交互项（年龄×并发症）和复合风险评分等结构化特征；并将文本特征从200个单字符TF-IDF扩展到850个三元组，以捕捉多词临床短语。
2.  **精心设计的集成模型**：人类干预推翻了智能体最初的单模型方案，转而采用多样化的集成策略。在再入院预测中使用了**堆叠集成**，包含五个具有不同复杂度（深度、学习率）的基学习器（XGBoost变体和正则化逻辑回归），以确保决策边界互补。在成本预测中，由于数据量较小，采用了**手动加权的模型集成**，根据模型在保留集上的表现分配权重，避免了元学习器过拟合的风险。
3.  **多模态数据融合与任务特定策略**：论文强调没有一种通用的提取策略能适用于所有模态。对于PDF账单，开发了基于正则表达式的解析管道，提取CPT代码、服务利用率等临床细节特征，并创新性地设计了**跨源特征**（如PDF总费用与结构化历史费用的比率），以捕捉单一数据源无法揭示的模式。对于时间序列生命体征，则计算了丰富的统计量（端点值、趋势、波动性、临床阈值跨越）作为特征。
4.  **临床信息验证策略**：采用嵌套交叉验证来可靠地评估模型性能，并在集成训练中使用分层交叉验证生成堆叠特征，以减少方差。

总之，论文的核心解决方案不是开发一个全自动的智能体，而是构建一个**人类专家在特征工程、模型架构选择和验证策略等关键环节进行深度指导和决策的协作系统**，从而将临床领域知识有效地转化为模型性能的提升。

### Q4: 论文做了哪些实验？

该论文在AgentDS Healthcare基准的三个挑战上进行了系统实验：30天再入院预测（分类）、急诊费用预测（回归）和出院准备评估（多模态分类）。实验设置上，研究者采用人类引导的智能体工作流，在关键决策点（如多模态特征工程、模型选择、验证策略）引入临床专家知识，并与纯自动化基线进行对比。

基准测试方面，模型在公开排行榜上进行了评估。主要结果显示：在再入院预测任务中取得Macro-F1 0.8986（第5名）；在急诊费用预测中取得MAE $465.13（第6名）；在出院准备评估中取得Macro-F1 0.7939（第3名）。综合领域排名第5。

此外，论文通过消融实验量化了人类决策的贡献。结果表明，人类引导带来了累计+0.065 F1的性能提升，其中多模态特征提取贡献最大（+0.041 F1）。具体而言，移除人类指导的多模态特征（如临床笔记的trigram TF-IDF、PDF账单的CPT代码提取、生命体征的统计聚合）会导致性能显著下降（平均-0.037 F1或+$20 MAE）。其他人类干预，如设计领域交互特征、构建临床关键词、调整集成多样性等，也带来了稳定的正向收益。实验验证了人类在特征工程阶段的早期决策比后期的超参数调优对最终性能影响更大。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，可以进一步探索的点主要围绕技术深化、泛化验证和系统优化。局限性包括：1) 使用合成数据，缺乏真实临床数据的噪声和复杂性；2) 为保持跨任务一致性，可能牺牲了单任务性能的优化空间；3) 受限于样本量（N<5,000），未充分探索深度学习模型；4) 多模态特征工程依赖人工，耗时且难以规模化；5) 计算资源要求可能影响可及性。

未来方向可分为短期和长期。短期可探索：在更大样本上应用Transformer模型（如BioClinicalBERT）以提升文本理解；引入不确定性量化以增强临床可信度；进行公平性分析以检测模型偏见。长期则应关注：在真实电子健康记录数据（如MIMIC-IV）上进行外部验证，评估泛化能力；开展前瞻性临床试验，测量对患者结局的实际影响；研究自动化多模态特征学习方法，以降低人工成本并处理更大规模数据；开发持续学习机制，使模型能适应数据分布的变化（如疫情、政策变更）。这些探索旨在平衡性能与可解释性，推动智能体系统在临床环境中的可靠部署。

### Q6: 总结一下论文的主要内容

该论文的核心贡献在于提出并验证了一种“人机协同”的智能体AI工作流，用于解决多模态临床预测任务。研究通过在AgentDS医疗基准的三个挑战任务（30天再入院预测、急诊费用预测和出院准备评估）中引入人类专家的关键性指导，显著提升了模型性能。研究发现，人类在三个环节的介入至关重要：基于临床知识的跨模态特征工程、针对具体任务的数据整合策略选择，以及构建具有临床合理性的模型集成方案。消融实验表明，人类指导带来了累积性的性能增益，其中多模态特征提取贡献最大。论文提炼出的核心洞见是：在医疗等对可解释性、可重复性和临床有效性要求极高的领域，将领域专家的判断系统地嵌入智能体AI的自动化流程中，其效果远超纯粹的自动化搜索或单一技术策略，这为未来在关键领域部署可信、高效的智能体系统提供了重要的方法论指导。
