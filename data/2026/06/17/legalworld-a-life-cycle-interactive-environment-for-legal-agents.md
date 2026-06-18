---
title: "LegalWorld: A Life-Cycle Interactive Environment for Legal Agents"
authors:
  - "Songhan Zuo"
  - "Shengbin Yue"
  - "Tao Chiang"
  - "Guanying Li"
  - "Yun Song"
  - "Xuanjing Huang"
  - "Zhongyu Wei"
date: "2026-06-17"
arxiv_id: "2606.18728"
arxiv_url: "https://arxiv.org/abs/2606.18728"
pdf_url: "https://arxiv.org/pdf/2606.18728v1"
categories:
  - "cs.CL"
tags:
  - "Legal Agent"
  - "Life-Cycle Environment"
  - "Multi-Stage Evaluation"
  - "LegalAI"
  - "Agent Benchmark"
  - "Interactive Environment"
relevance_score: 8.5
---

# LegalWorld: A Life-Cycle Interactive Environment for Legal Agents

## 原始摘要

Civil litigation is inherently a life-cycle process: what a lawyer drafts on day one constrains what unfolds at trial months later. Yet existing legal benchmarks evaluate isolated subtasks, and prior legal-agent simulators reinitialize each scenario from shared ground truth, leaving cross-stage causal dependencies unmodeled. We present LegalWorld, a life-cycle interactive environment that models Chinese civil litigation as a causally connected state chain of five stages (seven sub-scenarios), grounded in 75,309 paired Chinese civil judgments. We pair it with reusable infrastructure (local memory, global case memory, a Skill/Tool library) that keeps each dispute consistent across its full life cycle. Building on this environment, we construct LongJud-Bench to evaluate agent capability across all five connected stages. 18,992 ratings from 217 legal-background evaluators confirm that LegalWorld trajectories are procedurally faithful and role-consistent; and a capability-level cross-model evaluation reveals sharp divergences that aggregate scores cannot expose, with no single backbone leading across consultation, drafting, and courtroom advocacy. Detailed resources will be released publicly.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前法律人工智能领域中缺乏能够模拟完整民事诉讼全生命周期交互环境的问题。研究背景是，尽管法律AI在语言模型、评测基准和智能体系统方面取得了进展，但现有方法通常局限于孤立场景任务，即每个任务基于固定输入进行评估，不继承先前程序阶段的状态。现存的法律智能体模拟器存在三个关键不足：1) 长期阶段覆盖不全，仅模拟局部诉讼流程（如庭审），未能建模跨阶段的状态传递；2) 异质角色一致性缺失，不同角色（客户、律师、法官）的知识和立场在诉讼过程中持续演变，但现有模拟器从共享基准事实重新初始化每个场景，无法保持角色状态的连贯性；3) 缺乏程序性工具支持，复杂法律任务所需的证据提交、文书起草和庭审程序工具未被提供。因此，本文的核心问题是：如何构建一个完整的、因果关联的民事诉讼全生命周期交互环境，以评估法律智能体在跨阶段程序性能力上的表现，而非孤立的单任务技能。LegalWorld通过建模五阶段因果链、设计角色特定接口和可复用基础设施，旨在解决上述空白。

### Q2: 有哪些相关研究？

相关研究主要分为两类：

1. **法律模拟与生成式智能体**：如AgentCourt和AgentsCourt模拟对抗式审判流程，Ready Jurist One覆盖多个场景但各场景从共享案例真相初始化，Law in Silico通过群体模拟研究社会法律动力学。本文LegalWorld区别于这些工作，它将咨询、文书起草和两级审判链接为单一生命周期，使同一案例中的事实传递和错误放大可观测。

2. **法律能力基准**：现有法律AI基准主要评测局部能力（如法条检索、文书生成、单案推理和结果预测）；长上下文基准测试单次输入处理；智能体记忆研究关注长对话中的持久性。本文LongJud-Bench则将咨询、起草、庭审辩护、上诉和二审作为同一案件的关联阶段进行评测，同时衡量局部质量与跨阶段错误传播。

本文的核心创新在于构建了因果连接的诉讼全生命周期环境，而非孤立子任务评测或场景独立初始化，从而能够建模跨阶段依赖关系和错误累积效应。

### Q3: 论文如何解决这个问题？

LegalWorld通过构建一个因果关联的五阶段状态链来建模民事诉讼全生命周期，解决了现有基准仅评估孤立子任务而忽略跨阶段因果依赖的问题。核心架构包括两个运行时组件：内存处理器和技能/工具支持入口。内存处理器将场景内本地记忆与全局案例记忆分离：本地记忆保留回合级对话连续性，全局记忆在阶段结束时将结构化事实（如证据状态、诉讼主张、委托人目标）持久化存储，并采用"修订/扩展"两种写操作来维护跨阶段一致性。律师与委托人共享同一全局案例记忆但视角分离，模拟了法律专业认知与普通当事人认知的差异。技能/工具层为每个阶段提供程序性支持，通过可见技能和可执行工具的组合定义阶段行为边界。技能包含步骤约束和输出规范，工具负责记忆读写、检索、文书导出和引证校验。阶段门控机制通过状态验证函数和可视工具集来防止隐藏信息、先验知识或后阶段信息的泄漏。实验表明该环境在程序保真度和角色一致性方面表现优异（人类评分8.96/9.02），且相比LLM基线更贴合程序规范。

### Q4: 论文做了哪些实验？

论文围绕LegalWorld环境开展了三组实验。首先验证环境可靠性：在Stage Authenticity（阶段真实性）和Role Consistency（角色一致性）上，217位法律背景评估者给出8.96/10和8.98/10的高分；18,992条评分中73%≥9，仅4.5%≤6。在Judicial Output Alignment（司法输出对齐）上，生成的判决书在事实推理（8.45）、实体（8.89）和结构（9.36）上高度匹配真实判决，法律引用略低（7.02）。其次在LongJud-Bench上对六种LLM骨干模型（Kimi-K2.5、Qwen3.5-Plus、GPT-5.2、DeepSeek-V4-Flash、GLM-4.7、Qwen3.5-Flash）进行全生命周期评估，覆盖咨询、文书起草和庭审辩护八项能力。结果显示无单一模型全面领先：Kimi-K2.5在文书起草项最强，GPT-5.2在一审证据辩论（0.61）和法律推理（0.57）领先，Qwen3.5-Plus在诉求构建（0.72/0.72）表现突出。庭审辩护是共同瓶颈，所有模型在该领域得分均明显低于文书起草能力。最后，基于生成的完整过程轨迹，尝试Reflective Legal Skill（RLS）训练信号，将LongJud-Bench平均分从61.56提升至65.29（+3.73），其中已反思案例提升4.20，未反思同类案例也提升2.34。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在两方面：一是当前环境仅覆盖中国民事一审/二审程序，未纳入刑事、行政、执行及再审等流程；二是模拟简化了管辖异议、证据保全、反诉、专家意见、调解失败等程序性分支事件，且评估依赖基准评分而非真实法律服务效果。未来可沿三个方向探索：首先，将生命周期建模扩展到刑事、行政诉讼等程序，构建跨司法领域的统一框架；其次，引入动态分支事件模拟，例如被告提出管辖权异议时自动触发中止审理，或当事人申请财产保全后改变后续执行阶段状态，使流程更贴近真实；最后，结合法律专业人员的反馈，优化代理人工具库（如改进类案检索算法），并设计混合智能协作范式，由AI完成文书草拟而人类律师主导庭审策略，通过对比实验验证这种分工对司法效率的提升效果。

### Q6: 总结一下论文的主要内容

法律世界（LegalWorld）是一个面向中文民事诉讼全生命周期的交互式环境，旨在解决现有法律基准中跨阶段因果依赖缺失、角色一致性不足及程序工具支持匮乏的问题。该环境将民事诉讼建模为从咨询、起草、一审、上诉到二审的五个阶段（七个场景）的因果状态链，基于75,309对民事判决书构建，并配备局部记忆、全局案件记忆和技能/工具库等可复用基础设施，确保案件事实、证据和立场在全流程中一致。基于此环境构建的LongJud-Bench基准用于评估代理在各阶段的综合法律能力。来自217名法律背景评估者的18,992份评分证实了轨迹的程序忠实性与角色一致性；跨模型评估揭示，聚合分数无法捕捉不同骨干模型在咨询、起草和庭审辩护中的能力差异，表明法律服务需要专业化能力而非单一模型主导。这项工作首次为法律代理提供了生命周期的因果模拟环境和评估基准，对提升法律AI的真实程序能力具有重要意义。
