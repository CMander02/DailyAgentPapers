---
title: "Not All Skills Help: Measuring and Repairing Agent Knowledge"
authors:
  - "Yixuan Wang"
  - "Yiyang Zhou"
  - "Yiming Liang"
  - "Congyu Zhang"
  - "Fuxiao Liu"
  - "Jiawei Zhou"
  - "Huaxiu Yao"
date: "2026-06-13"
arxiv_id: "2606.15390"
arxiv_url: "https://arxiv.org/abs/2606.15390"
pdf_url: "https://arxiv.org/pdf/2606.15390v1"
github_url: "https://github.com/aiming-lab/assay"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "技能学习与评估"
  - "因果归因"
  - "技能库优化"
  - "智能体技能消融"
  - "任务级技能匹配"
  - "AppWorld"
  - "tau-bench"
  - "无需权重更新的智能体提升"
relevance_score: 9.5
---

# Not All Skills Help: Measuring and Repairing Agent Knowledge

## 原始摘要

LLM agents can improve without weight updates by accumulating natural-language skills from experience, but current systems entrust every decision about which skills to keep and how to apply them to LLM judgment alone. We argue that this conflates two distinct roles: generating a skill from experience is a creative act that judgment handles well, while deciding whether that skill actually helps requires empirical evidence across many tasks. Measuring per-skill causal contributions via randomized masking, we find that skill libraries exhibit pervasive causal heterogeneity: individual skills routinely help on some task types while hurting on others, yet their opposing effects cancel in aggregate, making them invisible to global curation methods. We propose ASSAY, a framework that separates generation from curation: it computes a per-skill causal attribution on a small development set, restructures the library offline, and suppresses skills with negative predicted effect for each test task. Across seven base models spanning four providers and two benchmarks (AppWorld and tau-bench), ASSAY consistently improves over prior skill-curation approaches. On AppWorld's hardest split, DeepSeek-V3 achieves 69.3% task-goal completion (47.4% relative improvement), a new state of the art among all published methods including weight-tuned approaches. On tau-bench retail, GPT-4.1 improves by 8.7% relative, advancing past o4-mini, o1, and GPT-4.5 on the public leaderboard without any weight modification. Ablation traces the dominant gain to per-task masking, confirming that the bottleneck is matching skills to tasks at inference time, not removing bad skills globally. Code is available at https://github.com/aiming-lab/assay.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在无权重更新的情况下，通过积累自然语言技能来提升性能时，现有技能管理方式存在的一个系统性缺陷。研究背景是，当前方法通常依赖同一个LLM的判断来负责技能的整个生命周期（包括生成、保留和检索），却从未验证保留的技能是否真正有效。现有的不足在于，这种不加检验的积累会导致因果异质性：一个技能可能在帮助某些任务类型的同时，对其他任务类型造成损害，而这些相反的效果在全局统计中相互抵消，使得传统的全局筛选方法无法发现并纠正这种问题。论文要解决的核心问题是，如何在不需要全局删除“坏技能”的情况下，为每个测试实例动态匹配最合适的技能子集，从而避免不相关或有害技能的干扰，提升智能体在多样化任务上的表现。

### Q2: 有哪些相关研究？

在相关研究方面，该工作可归为几类。**技能生成与整理类**方法如Reflexion、ExpeL、ACE、CUGA、SkillNet和CoEvoSkills，均依赖LLM在单任务中判断技能生命周期（生成、保留、应用），而本文指出这混淆了创造性生成与经验性验证，缺乏跨任务聚合证据来确认技能是否真正有益。本文将这些方法输出作为原始材料，进行第二阶段的经验整理。**技能检索与应用类**方法如RAG及其变体、BERTScore-Recall等，通过嵌入相似性选择技能，隐含假设主题相关性等于有用性。本文通过因果归因揭示该假设可能错误（如“迭代前验证列表内容”技能在单记录查找任务中因诱导多余步骤而有害），并提出基于预测因果效应而非相似性的每任务过滤。**超越单任务判断的优化类**方法如Voyager（只增不删）、SkillRL、EvolveR、Agentic Memory、SkillClaw、GraSP及权重方法SAGE/FireAct等，或依赖强化学习、或需权重更新。本文方法与之互补，运行于推理时，无需权重更新，可叠加于任何技能生成流水线，核心创新在于通过随机掩码测量自然语言技能的因果效应（类似Shapley值归因和随机消融，但应用于技能指令而非模型组件）。

### Q3: 论文如何解决这个问题？

ASSAY框架通过将技能生成与技能策划分离开来解决技能库中普遍存在的因果异质性难题。整体流程分为三个核心阶段：首先采用随机掩码协议计算因果归因矩阵，即对每个开发任务随机采样技能子集，通过实验组与控制组的差分均值估计每个技能对每个任务的边际因果效应（平均治疗效应），从而构建一个N×M矩阵C，其中包含每个技能在各类任务上的帮助或损害量化指标。该矩阵揭示了关键发现：许多技能（C异质性大但均值趋于零）在部分任务上有益、在其他任务上有害，其正负效应在全局统计中相互抵消，导致传统全局策展方法（如直接删除低分技能）无法识别此类问题。

其次，基于归因矩阵进行线下库重构，包括三个按序执行的操作：分裂（Splitting）针对因果异质性大的技能，利用LLM将其重写为带显式触发条件的条件变体（分别应对有益/有害场景），并通过开发集验证门控；退役（Retiring）移除低边际贡献的噪音技能；合并（Merging）通过嵌入相似度聚类消除分裂引入的冗余变体。该顺序设计防止了信息损失（异质性技能若先被退役会误删有益部分）。

最后，推理阶段实现任务自适应掩码：将测试任务嵌入与开发任务计算余弦相似度，通过温度调节的softmax加权聚合邻域任务的因果证据，预测每个技能在当前测试任务的因果效应，然后依据风险最小化规则（保留所有预测效应高于阈值的技能及受保护模板），动态生成个性化技能库。若过滤后库过小则回退至完整库，确保稳健性。核心创新在于将技能选择从语义相似性检索转变为因果效应驱动的风险最小化，解决了嵌入空间无法区分技能有益/有害性的根本局限。

### Q4: 论文做了哪些实验？

论文在AppWorld和tau-bench两个基准上进行了实验。AppWorld模拟9个消费应用场景，使用ReAct智能体，以任务目标完成度(TGC)为指标，数据集分为test_normal(168任务)和test_challenge(417任务)。tau-bench模拟零售客服，使用ToolCallingAgent，以精确数据库状态匹配为指标，含115任务。实验涵盖7个基础模型（GPT-5.4、GPT-5.1、GPT-4.1、GPT-4o、DeepSeek-V3、Claude Sonnet 4.5、Gemini 2.5 Pro）。对比方法包括ACE、CUGA、以及未经验库的原始ReAct基线。

主要结果：在AppWorld上，所有模型均有提升。DeepSeek-V3在test_challenge上达69.3% TGC（相对提升47.4%），超越所有已发表方法（包括权重微调方法）。GPT-5.1较ACE提升10.1和13.9个百分点。在tau-bench上，GPT-4.1相对提升8.7%（68.0%→73.9%），排名从第14升至第8-9，超越o4-mini、o1和GPT-4.5。GPT-5.4达80.9%，进入前五。消融实验表明，逐任务掩码贡献最大（相对提升10.7%），确认核心瓶颈在于推理时技能与任务的匹配。深层分析显示，未策划技能库在困难任务上反而有害（如GPT-5.1在test_challenge从52.5%降至49.9%），而ASSAY通过因果归因能识别并抑制有害技能。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要有以下几点：首先，当基座模型能力足够强（如GPT-5.1、Sonnet 4.5）时，提示时技能注入的边际收益递减，说明该方法对中等能力的模型更有效，未来可探索如何为超强模型设计更高效的技能表征形式。其次，当前方法是离线、静态的，未来应扩展至在线场景，支持技能库持续动态增长时的增量式因果归因与屏蔽策略，避免每次新增技能都需要重新评估全部历史技能。此外，随机掩码的因果估计方差较大，可引入交叉验证或贝叶斯方法提升归因稳定性；技能生成环节目前完全依赖LLM，未来可引入多轮迭代生成或人类反馈来提升技能质量。最后，当前仅评估了工具使用类环境，未来可拓展至多步推理、代码编写等更复杂的任务范式。

### Q6: 总结一下论文的主要内容

这篇论文研究了LLM智能体通过自然语言技能积累进行无权重更新的经验学习。作者指出，当前系统将所有决策都交由LLM判断，混淆了技能生成与技能筛选两个角色：生成适合LLM判断，而判断技能是否真正有益需要实证证据。通过随机掩码测量每个技能的因果贡献，发现技能库存在普遍的因果异质性：单个技能在某些任务类型上提升性能，在另一些上却造成损害，而其相反效应在整体上相互抵消，使全局筛选方法失效。为此，提出ASSAY框架，将生成与筛选分离：在小开发集上计算每个技能的因果归因，离线重构技能库，并为每个测试任务抑制预测有负面影响的技能。在覆盖七种基础模型的两个基准测试中，ASSAY持续优于先前的技能筛选方法。在AppWorld最难分支上，DeepSeek-V3达到69.3%的完成率（相对提升47.4%），创下包括权重调优方法在内的所有已发表方法的新纪录。消融实验证实瓶颈在于推理时技能与任务的匹配，而非全局移除坏技能。该工作揭示了技能筛选的关键作用，为无需权重更新的智能体性能提升提供了新思路。
