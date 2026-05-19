---
title: "MA$^{2}$P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion"
authors:
  - "Dingyi Zhang"
  - "Ziqing Zhuang"
  - "Linhai Zhang"
  - "Ziyang Gao"
  - "Deyu Zhou"
date: "2026-05-18"
arxiv_id: "2605.18572"
arxiv_url: "https://arxiv.org/abs/2605.18572"
pdf_url: "https://arxiv.org/pdf/2605.18572v1"
categories:
  - "cs.CL"
tags:
  - "persuasive agent"
  - "multi-agent"
  - "meta-cognition"
  - "LLM agent"
  - "dialogue system"
relevance_score: 8
---

# MA$^{2}$P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion

## 原始摘要

Persuasive dialogue generation plays a vital role in decision-making, negotiation, counseling, and behavior change, yet it remains a challenging problem. In complex persuasion where the persuadee's internal states are not expressed clearly, the persuader must interpret responses, infer the persuadee's latent mental states (e.g., beliefs and desires), and translate them into targeted, strategy-consistent actions; however, current approaches often produce generic or weakly grounded responses even when such cues are identified. Moreover, although large language models (LLMs) can generate persuasive content, their performance varies substantially across domains due to uneven knowledge coverage and limited reasoning generalization. To address these challenges, we propose MA$^{2}$P, a meta-cognitive autonomous intelligent agent framework for complex persuasion. Specifically, we develop an autonomous multi-agent architecture that coordinates perception management, mental-state inference, strategy execution, memory maintenance, and performance evaluation. To mitigate cross-domain performance variation, we further design a meta-cognitive configurator that selects an appropriate meta-strategy from a structured knowledge base at the outset, thereby guiding subsequent reasoning and planning. Experimental results show that our approach achieves a higher persuasion success rate than baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂说服对话中现有方法的两大核心不足：一是缺乏可操作的规划能力，二是跨领域性能波动剧烈。在复杂说服场景下，被说服者的内部状态（如信念、欲望）常未明确表达，说服者需推断这些潜在状态并转化为针对性行动。然而，现有基于大语言模型（LLM）的方法虽能流畅生成内容并识别用户担忧（如“需要钱”、“日程忙”），却往往仅给出“强调心理治疗重要性”这类泛泛建议，无法将识别出的障碍转化为具体的策略化行动（如提供保险、灵活在线预约）。同时，LLM说服者的跨领域泛化能力差，例如gpt-5-mini在最好域成功率达88.24%，最差域仅16.67%，相差71.57个百分点。为此，本文提出MA²P——一个元认知自主智能体框架。它借鉴自主智能体蓝图，将说服建模为闭环交互，通过模块化分解（感知、心理状态推理、策略规划、响应生成、记忆、评估）实现从心理状态线索到策略化行动的可操作映射；并引入元认知配置器，在交互开始时从结构化知识库中选择元策略，指导后续推理与规划，以减轻跨域性能差异。核心目标是提升说服成功率、心理状态对齐度与规划连贯性，同时降低跨领域方差。

### Q2: 有哪些相关研究？

在相关工作中，本文主要涉及两类研究：

1. **基于大语言模型的劝说**：包括（i）对劝说行为与风险的调查与实证分析（如公共健康、消费决策、政治语境）；（ii）用户感知型劝说，明确建模用户状态并适应心理策略；（iii）将劝说形式化为序列决策（如劝说博弈、离策略评估）；（iv）智能体方向，构建模块化或多智能体劝说器进行多轮交互。与这些工作相比，本文强调在复杂的、用户内隐状态未明确表达的劝说场景下，需要主动推断心理状态并生成针对性策略一致的回应，而现有方法往往产生通用性响应且知识覆盖不均。

2. **大语言模型的元认知**：将元认知建模为决定何时规划、验证、修正或停止的控制器。包括（i）提示/接口方法；（ii）推理过程方法，建模元推理信号以提高鲁棒性；（iii）智能体编排，利用元控制进行工具使用与规划；（iv）评估与应用。本文与这些工作的区别在于：提出一个元认知配置器，在初始阶段从结构化知识库中选择合适元策略，以指导后续推理与规划，从而缓解跨领域性能差异问题。

总体而言，本文在劝说与元认知交叉领域，通过多智能体架构与元认知配置的创新，超越了现有方法在处理复杂劝说场景时的局限性。

### Q3: 论文如何解决这个问题？

MA²P通过元认知自主智能体框架将复杂说服任务建模为“元层规划-任务层执行-反思更新”的三阶段循环。核心架构包含两个关键部分：一是元认知配置器（Configurator），二是多智能体团队。首先，配置器针对具体场景（领域、目标、背景）从结构化知识库中检索历史成功次数最高的元策略（基于Cialdini七项影响原则），同时构建评估规则，为后续推理设定明确方向和成功标准。然后，任务层由四个自主智能体协同执行：感知模块从对话历史中提取信念、欲望等心理状态线索；世界模型结合所选元策略和短期记忆持久化状态，推断出当前轮次的具体说服策略；说服者智能体将该策略转化为自然语言回复；短期记忆维护对话历史、感知输出及历史策略的共享快照，支持连续推理。最后，评估者根据预设规则判断对话是否成功，并将成功案例的模式（领域-策略对的经验计数）写回知识库，实现跨领域知识的自适应积累。这一设计使LLM能够通过即插即用的方式获得领域特化引导和结构化推理能力，实验表明在各基座模型上MA²P均显著提升了说服成功率，同时降低了对话轮次和生成范围。

### Q4: 论文做了哪些实验？

论文在CToMPersu数据集（525个测试实例）上进行了多组实验。对比了五种基础LLM（gpt-4o-mini、gpt-4o、gpt-5-mini、gemini-2.5-flash、deepseek-v3）及其MA²P增强版本，采用即插即用、无需训练的方式。主要指标包括：说服成功率（Success）、说服力（Persuasive）、逻辑性（Logic）、帮助性（Helpful）、领域性能范围（Range）和标准差（SD）。结果表明，MA²P在所有基础模型上几乎全面提升了成功率，例如gpt-4o-mini成功率从0.45提升至0.79，gemini-2.5-flash提升超过0.20。消融实验比较了基础模型、无元认知的自主智能体系统（+Auto）和完整MA²P。结果显示，+Auto虽提升成功率（如gpt-4o-mini从0.45提升至0.66），但扩大了领域离散程度（Range从0.45升至0.53）；而完整MA²P进一步将成功率提升至0.79，同时降低Range至0.40，表明元认知增强了跨域泛化。实验还研究了知识库大小K的影响：K=0时成功率为0.66，在K=500时达到最佳0.79，表明无需大量预热数据即可有效。A/B偏好测试中，LLM裁判（gpt-4o-mini）和人类评估者均一致偏好MA²P输出，加权Cohen's kappa为0.549，表明中等人机一致性。案例研究展示了MA²P能推断用户心理状态（如节省时间、认为线上资源足够），并生成针对性策略（如低承诺试验、线上vs线下对比）。

### Q5: 有什么可以进一步探索的点？

该框架的局限性首先体现在评估方法上：依赖LLM作为自动评估器存在主观性，人工评估则受限于样本量和标注者数量。未来可探索更客观的评估体系，如结合用户行为实验或生理信号测量说服效果。其次，跨域应用需要冷启动阶段，这限制了实际部署效率，可研究零样本或少样本的元策略迁移方法，或构建通用说服知识图谱。当前被说服者建模过于简化，仅聚焦于信念和欲望，未考虑人格特质、情绪状态或认知偏见等复杂心理因素。值得深入的方向是开发具有可控人格参数和动态信念更新能力的标准化仿真被说服者模型，这既能降低对真实对话数据的依赖，又能系统测试说服策略的鲁棒性。此外，当前元认知配置器依赖静态知识库，可探索在线学习机制使策略库随交互动态进化，并引入反事实推理来增强说服策略的泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出MA²P框架，解决复杂说服对话中的两个核心问题：如何将推断出的内隐心理状态转化为策略性行动，以及如何缓解大语言模型在不同领域间的性能波动。方法上，构建了自主多智能体架构，协调感知管理、心理状态推断、策略执行、记忆维护与性能评估；并设计元认知配置器，从结构化知识库中选择初始元策略以引导后续推理。实验基于五个基础大模型，通过大模型评估和人工评估，证明该方法在说服成功率与回复质量上均显著优于基线。该工作的意义在于提供了即插即用、无需训练的通用框架，为心理状态驱动的说服对话研究开辟了新路径。
