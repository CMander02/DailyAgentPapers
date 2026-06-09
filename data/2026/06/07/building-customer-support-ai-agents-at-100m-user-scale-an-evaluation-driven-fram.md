---
title: "Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework"
authors:
  - "Aman Gupta"
  - "Kevin Rossell"
  - "Edesio Alcobaça"
  - "Jose Chrystian Lima Pacheco"
  - "Carolina Baptista de Lima"
  - "Shao Tang"
  - "Luiz Paulo Rabachini"
  - "Luis Moneda"
  - "Herbert Fei"
  - "Daniel Silva"
  - "Rohan Ramanath"
date: "2026-06-07"
arxiv_id: "2606.08867"
arxiv_url: "https://arxiv.org/abs/2606.08867"
pdf_url: "https://arxiv.org/pdf/2606.08867v1"
categories:
  - "cs.CL"
tags:
  - "Customer Support Agent"
  - "LLM Agent Evaluation"
  - "Production Agent Framework"
  - "Human-in-the-Loop"
  - "Offline-to-Online Validation"
relevance_score: 7.5
---

# Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework

## 原始摘要

The rapid rise in LLM capabilities has made AI agents increasingly viable across a broad range of tasks. Among the most promising applications is building production-ready customer-facing agents, a challenge that demands coordinated excellence in evaluation methodology, context engineering, training, and online measurement. Yet these critical pillars are typically developed in isolation, creating blind spots that only surface after deployment.
  In this paper, we present a unified framework that bridges offline development with online impact for customer support AI agents at Nubank, a company with 100M+ users. Our approach integrates several key components: (1) structured context engineering tailored to customer support agents, (2) systematic human-in-the-loop prompt iteration, (3) rigorous LLM judge evaluation with measured inter-rater agreement and GEPA optimization for consistency, and (4) ideation-to-production validation.
  A central insight is that evaluation-pipeline quality directly determines iteration velocity. We present results from five production deployments spanning distinct domains: card delivery, debt management, credit-limit support, card management, and product explanation. These deployments deliver consistent customer-satisfaction gains while substantially accelerating iteration. In our card-delivery deployment, large-scale A/B testing yields a 37 percentage-point improvement in AI transactional Net Promoter Score and a 29 percentage-point gain in self-service rate over prior agent variants, alongside a strong correlation between offline simulation metrics and online outcomes, demonstrating that eval-driven development reliably predicts production impact. On most use cases, AI satisfaction reaches within a few percentage points of expert human agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在超大规模（1亿+用户）生产环境中构建客户支持AI智能体所面临的系统性挑战。随着大语言模型（LLM）能力的快速提升，AI智能体在客户支持领域展现出巨大潜力，但现有方法存在显著不足：评价方法论、上下文工程、训练和在线测量这些关键支柱通常是孤立开发的，导致只有部署后才会暴露的盲点。具体而言，客户支持AI智能体面临特殊要求：极高的质量门槛（单次不良交互可能损害信任）、敏感数据处理（涉及余额、地址等真实客户数据）、狭窄但深入的专业化（5-15个工具但需处理大量边缘案例）、以及需要优雅地向人工客服移交。

本文核心要解决的核心问题是：如何构建一个统一的、以评估驱动的框架，将离线开发与在线影响有效连接起来，从而在100M+用户规模的银行环境中，可靠地构建并部署能显著提升客户满意度（如AI交易净推荐值提高37个百分点）且能保证迭代速度的生产级客户支持AI智能体。该框架的核心洞察是评估管道的质量直接决定了迭代速度。

### Q2: 有哪些相关研究？

相关研究可分为协同管理系统架构与基准测试、用户反馈与信任评估等类别。在系统架构与基准方面，本文参考了Obadinma等人的模块化设计（意图分类、检索、生成），以及Airbnb的策略到模式助手和超出范围检测以实现人工交接。数据方面，相关工作包括NatCS多领域支持语料库、CSConv/RoleCS的分阶段对话框架和合成训练数据，以及Mendonça等人标注情感和对话质量的双语语料库。在评估与信任方面，Feng等人通过目标跟踪任务槽建模用户满意度；Følstad等人发现早期故障会削弱信任；Reinhard等人将生成式AI视为增强人类代理的工具。Mohammadi等人综述了LLM代理评估的目标和模式（离线与在线），强调了企业面临的策略合规和长期可靠性等挑战。

本文与这些工作的核心区别在于构建了一个完整的评估驱动框架，将离线开发与在线影响桥接起来。不同于孤立地处理评估、上下文工程、训练或在线测量，本文提出了一个统一的方法，包括结构化上下文工程、人工参与的提示迭代、带有评分者间一致性和GEPA优化的严格LLM评估，以及从概念到生产的验证。本文的独特贡献在于证明了评估管道质量直接决定了迭代速度，并通过Nubank 100M+用户规模的五个生产部署验证了离线指标与在线结果之间的强相关性。

### Q3: 论文如何解决这个问题？

论文提出了一套以评估驱动的统一框架，用于构建面向1亿用户规模的客户支持AI Agent。核心方法在于将离线开发与在线影响紧密耦合，强调**评估管线的质量直接决定迭代速度**。

**整体框架**采用双循环迭代结构：**快速循环**利用离线评估结果直接指导提示版本迭代；**慢速循环**通过生产环境指标(如tNPS、自助服务率)反馈来驱动架构级改进。框架包含四个主要阶段：1) 智能体架构设计；2) 提示版本化；3) 离线评估；4) 生产部署。

**核心技术组件**包括：1) **上下文工程**：将传统的提示工程扩展为系统化设计整个输入上下文，包含指令、惯例(将SOP转化为可执行步骤)、宏、工具规范及工作记忆五个独立版本化的模块；2) **系统化人工参与的提示迭代**：领域专家针对特定模块进行精确修复，避免整体重写；3) **严格的LLM评估器**：通过测量评估者间一致性和GEPA优化来校准评估器，确保离线评估可靠性；4) **从构思到生产的验证**：确保离线指标与线上业务结果强相关。

**创新点**包括：将工具设计视为提示的一部分，通过将确定性流程封装在代码中而非提示中来减少LLM认知负载；设计幂等工具以处理LLM重试；最小化工具输出表面区域以节省上下文窗口。该方法在五个领域部署中证明了有效性，在卡交付场景中通过大规模A/B测试，实现了AI事务性净推荐值提升37个百分点，自助服务率提升29个百分点。

### Q4: 论文做了哪些实验？

论文在Nubank的100M+用户规模上进行了系统实验验证。核心实验围绕卡片配送场景，构建了包含5个二元评估数据集（E1-E5）的离线评估体系，数据来自真实客服对话，由三位运营分析师通过多数投票标注。对比方法包括：多数类基线、人工编写启动提示词基线，以及经GEPA优化的提示词。离线结果显示，优化后提示词在所有指标上显著超越基线：如E1准确率从51.11%提升至82.00%，E2从77.78%提升至88.89%，E3从56.62%提升至73.01%。通过Cohen's Kappa分析，GEPA优化后模型间一致性大幅提升，例如GPT-4.1与GPT-4.1-mini的κ从0.00升至0.745，GPT-5与o3达0.950。在线A/B测试中，卡片配送agent部署了10个变体，大型A/B测试表明：与旧版agent相比，AI交易净推荐值（tNPS）提升37个百分点，自助服务率提升29个百分点，AI满意度与专家人类agent差距在10个百分点以内。离线评估失败率与在线tNPS呈强正相关，验证了评估驱动开发的可预测性。此外，实验扩展到另外4个领域（债务管理、信用额度支持等），在债务管理场景中AI tNPS提升40个百分点。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于框架高度依赖离线评估与线上指标的强相关性，但作者仅展示了5个用例的相关性，未深入探讨在更复杂或边缘场景下这种相关性是否依然成立。例如债务管理领域人机差距较大，说明框架在应对高情感复杂度或长尾伦理风险时预测能力下降。未来方向包括：1）引入持续在线对抗测试与压力测试，构建更鲁棒的离线-线上闭环；2）探索多模态交互（如语音情感检测）对评估鲁棒性的影响；3）研究基于强化学习的自动迭代机制，减少人工标注Prompt的依赖；4）设计可迁移的跨领域评估模板，降低冷启动成本。此外，文中GEPA优化仅用于对齐评判标准，未来可扩展至Agent整体行为优化，例如引入因果推断来区分评估偏差与真实能力缺陷。

### Q6: 总结一下论文的主要内容

该论文提出了一个针对百万级用户规模客服AI代理的评估驱动开发框架，由巴西数字银行Nubank在实际生产环境中验证。核心问题在于以往评估方法、提示工程、上下文工程和在线指标等关键环节常被孤立开发，导致部署后才发现盲点。方法上，该框架整合了四个关键组件：(1)面向客服代理的结构化上下文工程；(2)系统化的人工参与提示迭代流程；(3)具备评估者间信度度量和GEPA一致性优化的LLM评委评估管线；(4)从构思到生产的端到端验证。在卡片配送、债务管理、信用额度、卡片管理和产品解释五个生产部署中，该方法带来了一致的客户满意度提升。以卡片配送为例，大规模A/B测试显示AI交易净推荐值较先前代理变体提升37个百分点，自助服务率提升29个百分点。核心结论表明，评估管线质量直接决定迭代速度，离线模拟指标与在线结果之间存在强相关性，证明评估驱动开发能可靠预测生产影响。在大多数用例中，AI满意度已接近专家人工客服水平（仅差1-10个百分点），仅在债务管理这一最具挑战性的领域仍存在较大差距。
