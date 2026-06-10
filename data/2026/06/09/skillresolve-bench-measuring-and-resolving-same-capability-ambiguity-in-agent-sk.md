---
title: "SkillResolve-Bench: Measuring and Resolving Same-Capability Ambiguity in Agent Skill Retrieval"
authors:
  - "Jiandong Ding"
date: "2026-06-09"
arxiv_id: "2606.10388"
arxiv_url: "https://arxiv.org/abs/2606.10388"
pdf_url: "https://arxiv.org/pdf/2606.10388v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agent技能检索"
  - "Agent评测基准"
  - "技能库"
  - "多智能体系统"
  - "检索增强"
relevance_score: 8.5
---

# SkillResolve-Bench: Measuring and Resolving Same-Capability Ambiguity in Agent Skill Retrieval

## 原始摘要

Agent skill libraries are becoming routable software assets: a retrieved skill can contribute instructions, scripts, resource bindings, and execution assumptions to an agent. This makes skill retrieval more than broad relevance matching. A retriever can find the right capability family yet expose the wrong same-capability representative. We study this failure as same-capability execution-risk retrieval. Each query pairs a helpful skill with a query-specific risky sibling that shares the capability family but can lead execution toward a stale resource, missing precondition, or wrong procedure. We introduce SkillResolve-Bench 1.0, an auditable benchmark for this setting with 661 helpful/risky pairs, source-role and admission evidence, cue/leakage checks, query-disjoint splits, and a 7,982-candidate pool that includes 6,660 public SkillRet candidates. The benchmark reports helpful ranking together with harmful sibling rate (HSR@K), the top-K exposure of the risky sibling. We also provide SkillResolve, a reference method that resolves active candidate families, scores query-conditioned utility from confusable library negatives and contract-profile cues, and selects one representative from each family before the final top-K list. Under the released family relation, SkillResolve reaches Recall@3 0.766 and NDCG@3 0.699 while keeping HSR@3=0. It improves over SkillRouter by 0.112 Recall@3 and 0.165 NDCG@3 while reducing HSR@3 from 0.693 to 0. Without representative selection, HSR@3 rises to 0.236 under the same scorer, identifying within-family representative choice as the mechanism that turns capability retrieval into safer procedural exposure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决技能库检索中的“同能力歧义”问题——即当检索器找到了正确的技能类别（如“发送邮件”），却返回了错误的同类别代表技能（如指向过时的API或错误的资源绑定），从而导致智能体执行失败或产生风险。现有方法如SkillRet和SRA-Bench主要关注通用相关性匹配或技能集兼容性，但未系统性区分同一能力族内不同技能的执行后果差异。安全研究虽关注恶意技能，但未针对这种“无恶意但高危”的同族歧义。核心问题是：如何让检索器在保留有用技能（Recall/NDCG）的同时，抑制具有相同能力但执行有风险的兄弟技能出现。为此，论文构建了SkillResolve-Bench 1.0基准，包含661组有用/风险技能对，并提出了SkillResolve方法，通过能力解析、基于合约轮廓的效用评分和族内代表选择，在Recall@3=0.766和NDCG@3=0.699下实现有害兄弟技能率HSR@3=0，显著优于现有基线。

### Q2: 有哪些相关研究？

相关研究可分为五类。（1）技能基准与路由方法类：SkillsBench衡量技能执行增益，SkillRet评估公共库检索，SRA-Bench分离检索/整合/执行瓶颈，SkillRouter发现完整技能体携带信号，SkillSeek研究开源智能体堆栈的两阶段检索，R3-Skill将技能检索建模为查询条件化的top-K兼容性而非独立相关性，而分组结构化检索揭示平面相关列表会隐藏入口点与风险信息。本文在这些研究基础上挖掘了能力检索后的补充目标——选择有用代表而非同能力风险兄弟。（2）技能库质量与治理应用类：OpenSkillEval与生态系统分析发现可复用制品缺陷与缺失路由引导，SkillOps将其框架为技能技术债务，SkillsVote等生命周期系统强调技能价值依赖任务与阶段证据。本文聚焦于检索时决定暴露哪个代表的对应性挑战。（3）技能生成与运行时接口类：Trace2Skill和SkillAdaptor从轨迹更新技能，其他工作研究验证性合成与图结构化技能表示。本文假设推理时候选库固定，研究基于标签的查询级排序。（4）技能安全与执行风险评测类：MalSkillBench提供运行时验证的恶意技能标注，SkillGuard通过清单与访问控制治理可执行制品。本文不审计恶意包，而是关注检索阶段中全局合理但当前查询有害的代表选择。（5）重排序骨干方法类：BGE等密集与交叉编码器重排序器提供强语义匹配信号，但在同能力风险场景下需要分离能力解析与效用条件化选择。

### Q3: 论文如何解决这个问题？

该论文通过引入SkillResolve方法来解决同能力歧义问题,即检索到正确的能力族但暴露了错误的成员技能。核心方法包含三个组件:能力解析器、效用评分器和代表选择器。整体框架首先通过能力解析器将候选技能分组,每组是同一能力的替代代表;然后效用评分器学习查询条件下的技能效用函数;最后代表选择器从每组中选出一个最高效用的技能,组成最终Top-K列表。关键技术包括:效用评分器采用线性模型,结合基础特征(如TF-IDF、互惠排名融合等)和执行契约特征(资源绑定、前提条件、API范围等六个字段的文本轮廓对比),通过成对逻辑回归学习偏好有用技能而非混淆候选。创新点在于:1)将任务分解为能力解析和代表选择两步,解耦了基准关系与部署方法接口;2)定义了有害兄弟技能率(HSR@K)指标衡量执行风险暴露;3)在最终的全局排名前进行组内效用竞争,确保只有每个能力族的最高效用代表进入Top-K,从而在保持召回率和NDCG的同时将HSR降至零。

### Q4: 论文做了哪些实验？

论文在SkillResolve-Bench 1.0基准上进行了实验。实验设置是固定候选池检索任务，包含661个helpful/risky技能对，候选池共7982个候选（含6660个SkillRet公共技能）。数据集采用查询互斥的446/68/147划分。评估指标包括Recall、NDCG和有害兄弟率(HSR@K)。

对比方法分为零样本和同协议训练两组。零样本基线包括BGE重排序、混合词法RRF和SkillRouter。同协议基线包括Attribution-listwise。主要结果：SkillResolve达到Recall@3=0.766、NDCG@3=0.699，且HSR@3=0。相比之下，SkillRouter的Recall@3仅为0.654、NDCG@3=0.534，但HSR@3高达0.693。与Attribution-listwise相比（Recall@3=0.676，NDCG@3=0.596），SkillResolve在Recall@3上提升0.089，NDCG@3提升0.103。

消融实验表明：移除代表选择（representative selection）后，HSR@3升至0.236，而Recall@3几乎不变；去除合约特征轻微降低Recall@3至0.758。公共族源分析显示，使用发布的关系、元数据/标题或文本聚类族源均能实现HSR@3=0，而无分组时HSR@3=0.236。

### Q5: 有什么可以进一步探索的点？

SkillResolve-Bench的核心局限在于其评估范围限定在“预执行暴露”阶段，未覆盖下游执行器鲁棒性和运行时验证。未来可探索方向包括：1) 将HSR度量扩展到执行失败的动态反馈中，构建"执行-检索"闭环系统，通过执行器日志自动生成负反馈信号来更新检索策略。2) 当前基准的661个歧义对人工构建成本高，可设计基于LLM的自动对抗生成框架，通过指令扰动、资源版本变迁模拟等手段批量构造同能力歧义样本。3) 代表性选择机制依赖合约型描述（contract-profile cues），可引入多模态推理（如API调用轨迹）或结构化知识图谱增强效用评分。4) 现有方法假设能力家族已知，未来可探索无监督情况下自动发现能力家族边界，例如通过因果干预推断技能间的执行冲突关系。

### Q6: 总结一下论文的主要内容

该论文研究了智能体技能库检索中的“同能力歧义”问题：检索器虽能匹配到正确的技能家族，但会提供该家族中不合适的代表技能（例如指向过期资源或错误流程），从而带来执行风险。为此，论文提出了SkillResolve-Bench 1.0基准，包含661对有用/风险技能对、来源与准入证据等，并引入有害兄弟率（HSR@K）来评估风险。同时，论文设计了SkillResolve参考方法，通过能力解析、混淆库效用评分和代表性选择，在保持高排序性能（Recall@3 0.766, NDCG@3 0.699）的同时将HSR@3降至0。主要结论是：可扩展技能库必须评估家族内代表性选择，仅靠正排序指标会掩盖风险，需要在最终输出前进行风险感知的筛选。
