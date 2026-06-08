---
title: "MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights"
authors:
  - "Yilun Liu"
  - "Miao Zhang"
  - "Shimin Tao"
  - "Minggui He"
  - "Chunguang Zhao"
  - "Chenxin Liu"
  - "Li Zhang"
  - "Chen Liu"
  - "Cheng Qian"
  - "Liqun Deng"
  - "Xiaojun Meng"
  - "Daimeng Wei"
date: "2026-06-05"
arxiv_id: "2606.07020"
arxiv_url: "https://arxiv.org/abs/2606.07020"
pdf_url: "https://arxiv.org/pdf/2606.07020v1"
categories:
  - "cs.CL"
tags:
  - "多语言Agent"
  - "Agent评估与诊断"
  - "多Agent协作"
  - "细粒度分析"
  - "报告生成"
relevance_score: 8.5
---

# MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights

## 原始摘要

Multilingual and multicultural benchmarks now cover dozens of languages and model families, but the resulting score landscapes remain metric-rich and insight-poor, necessitating fine-grained multilingual post-evaluation diagnosis. However, single LLMs and open-ended agents are easily swamped by the long, noisy diagnostic input, and no reusable taxonomy exists for it. To address this, we propose MADE, a Multilingual Agentic Diagnosing Engine that decomposes post-evaluation analysis into planning, aggregate analysis, instance-level case inspection, multilingual and cultural reflection, and grounded report synthesis. MADE is paired with an expert-led 54-query and 15-language diagnostic set, evaluated on top of a large-scale multilingual evaluation substrate (33 model families, 11 benchmarks, 26 languages, 34 cultures, 8.66M evaluation records). Experiments show that MADE outperforms the strongest shared baseline by 47% in diagnosis report quality and is preferred by human multilingual experts in 87.9% of pairwise comparisons. Applied with multilingual experts, MADE further surfaces four actionable findings on deployment, iteration, and cross-cultural pitfalls, turning benchmark score tables into model-selection and remediation guidance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多语言多文化基准评估中“指标丰富但洞察贫乏”的核心问题。现有的大规模多语言评估（如覆盖33个模型家族、26种语言）虽然产生了大量分数，但只能展示模型表现如何（where they stand），而模型开发者和研究者更想知道模型为何失败（why they fail）以及如何改进（how to act）。具体存在三个关键不足：第一，现有评估缺乏细粒度洞察，总体分数掩盖了部署相关的关键信号，如特定语言上的显著性能差距或版本迭代中的修复与退化；第二，现有的单一大型语言模型或通用智能体难以处理长且嘈杂的诊断输入（如8.66M条评估记录），容易陷入无关信息、偏离分析目标或产生无根据的结论；第三，多语言诊断领域缺乏一个系统化、可复用的细粒度分类体系，当前工作多限于英语单一数据集。因此，本文提出MADE，一个多语言智能体诊断引擎，旨在将大规模基准测试分数转化为细粒度的、带有证据的可操作诊断报告，指导模型选择、迭代和跨文化风险评估。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是**多语言与多文化评测工作**，如从单一任务测试发展到覆盖知识、推理、阅读、翻译、主观生成和文化理解的系统级框架，以及揭示多语言“数字鸿沟”等宏观模式的高层次分析。这些工作主要产出标量或分组得分，但止步于提供可复用的引擎将原始记录转化为细粒度、多语言且基于文化的诊断报告，导致部署阶段的切片级、语言级或文化级问题仍需人工处理。第二类是**评测后诊断与错误分析**，包括数学推理错误类型分类、基于LLM裁判的机器翻译错误分析、自动评判陷阱，以及近期利用多智能体报告生成将评测输出转化为结构化弱点报告的系统。本文提出的MADE连接了上述两类工作：它直接消费多语言基准评测的输出，生成细粒度的诊断报告，明确指出特定语言、文化和切片级别的失败模式。与通用弱点发现系统的关键区别在于，MADE专门聚焦于多语言和多文化、跨数据集的评测后诊断，通过专家引导的54个查询和15语言数据集、显式的多语言文化反思机制，以及聚合证据智能体与案例证据智能体的分工协作，使结论更可靠，填补了大规模多语言评测与可操作、细粒度诊断之间的空白。

### Q3: 论文如何解决这个问题？

MADE通过多智能体协作架构将后评估诊断分解为五个专业化角色，解决单一大语言模型在处理长噪声诊断输入时能力不足的问题。核心方法包括：首先，Planner智能体根据用户查询生成结构化计划，指定诊断层级、所需分析师和工具集，并屏蔽基准泄漏风险。其次，Evidence Analyst在受限的ReAct循环中操作聚合切片工具，产生绑定具体工具调用的切片级发现；Case Analyst则检索实例级案例，包括错误、模型分歧、退化样本等，所有案例ID来自确定性池以防止虚构。Language Reflector作为多语言诊断专家，从文化敏感性和证据基础两个维度进行三次干预（规划前、分析中、报告前），检查语言文化因素并标记过度声明。最后，Reporter整合所有输入，生成结构化、带证据标签的诊断报告。关键技术包括：一套确定性诊断工具（聚合切片、实例检索、细粒度能力、版本差异），以及结构化诊断上下文注入，为每个角色提供目标、工具模式、多语言文化注意事项和基础约束。创新点在于将人类多语言诊断专家的四步工作流程（查询分类、切片验证、样本检查、文化验证）映射为五个专业化智能体，并通过专家引导的54个查询、15种语言的诊断集进行基准测试，显著提升诊断报告质量。

### Q4: 论文做了哪些实验？

MADE在五个轴线上进行了全面实验。第一，自动评估：在包含15种语言、54个查询（共810个）的诊断集上进行，评估基座为3.3个模型家族、11个基准、26种语言、34种文化、866万条评估记录和约52亿文本token。使用LLM作为裁判，从需求满足、证据质量等七个维度评分。MADE平均得分8.02±1.04，远超最强单LLM基线cot（4.31）和通用智能体框架opencode（5.45），并在所有15种语言上领先，报告标准差最低（1.04），且100%有效完成。第二，人类专家评估：在12种语言上抽样120个项目，MADE的人类专家偏好胜率为87.9%，远超nanobot（40.6%）和cot（21.5%），与自动裁判的一致性达79.4%。第三，消融实验：在中文子集上，删除Reporter导致最大下降（-3.10），其次是证据分析师（-1.46）和规划器（-0.87），各组件均有正向贡献；去除智能体循环和工具分别导致-1.20和-3.00的下降。第四，基础模型鲁棒性：在Gemini、Qwen和DeepSeek三种骨干下，MADE均保持领先，得分在8.08-8.49之间。第五，效率：MADE在Gemini-3-Flash骨干下每个查询仅需4.3分钟，速度约为其他骨干的两倍。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性与当前进展，未来探索可从以下方向切入：**1) 扩展诊断基座**：当前仅覆盖文本模态与有限语言，可将MADE的工种解耦设计迁移至视觉-语言、代码生成或工具使用等新基准，只需替换负载器即可，系统性验证其基座无关性。**2) 降低人机协同成本**：专家目前仍需参与查询审计与报告校准，未来可引入主动学习策略，自动识别高不确定性诊断案例供专家审查，或利用合成数据与弱监督生成多语言查询模板，减少人工构建。**3) 提升推理效率**：现有7.26分钟/报告仍偏慢，可探索缓存机制、轻量分析师模型（如小参数蒸馏版）、报告模板蒸馏以压缩生成步骤，或设计并行化工具调用管线。**4) 深化跨文化反思**：当前文化反思模块仅依赖显式规则，可结合细粒度文化知识图谱与冲突检测模型，识别隐含文化偏见（如非西方语境下的隐喻），并生成更具可操作性的补救建议。

### Q6: 总结一下论文的主要内容

MADE提出了一种多语言智能体诊断引擎，用于将大规模评测分数转化为细粒度的行动洞察。当前多语言评测存在“重分数、轻洞察”的问题，难以从海量、嘈杂的评测记录中找出模型失败的真正原因。MADE创新性地将专家分析流程分解为规划、聚合分析、实例级案例分析、多语言与文化反思、报告合成五个角色，并配套构建了涵盖54个查询、15种语言的结构化诊断集。在包含33个模型家族、11个基准、26种语言、860万条记录的大规模评测平台上，MADE的诊断报告质量相比最强基线提升47%，在87.9%的人类专家对比中被优先选择。应用MADE后，专家还能识别出部署陷阱、非单调迭代、文化立场分歧等四个可执行发现，真正将分数表转化为模型选择与修复的指导手册。
