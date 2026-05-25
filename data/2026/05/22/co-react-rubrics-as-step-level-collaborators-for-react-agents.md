---
title: "Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents"
authors:
  - "Jiazheng Kang"
  - "Bowen Zhang"
  - "Zixin Song"
  - "Jiangwang Chen"
  - "Xiao Yang"
  - "Da Zhu"
  - "Guanjun Jiang"
date: "2026-05-22"
arxiv_id: "2605.23590"
arxiv_url: "https://arxiv.org/abs/2605.23590"
pdf_url: "https://arxiv.org/pdf/2605.23590v1"
github_url: "https://github.com/ZBWpro/Co-ReAct"
categories:
  - "cs.AI"
tags:
  - "Agent决策与规划"
  - "推理时指导"
  - "ReAct框架"
  - "多步推理"
  - "搜索增强Agent"
  - "评分规则生成"
  - "GRPO优化"
relevance_score: 9.0
---

# Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

## 原始摘要

ReAct-style agents for search-intensive, multi-step reasoning tasks rely largely on their own internal judgment to decide what evidence to seek, which reasoning or action step to take next, and when to stop, often producing shallow, redundant, or poorly targeted trajectories. Prior work has explored rubrics as external quality signals, but existing uses are mostly evaluative rather than action-guiding: rubrics typically serve as training-time rewards or post-hoc evaluators of completed outputs, and in deep-research settings they are often coarse-grained and report-level rather than step-level. We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference. At each decision step, Co-ReAct injects a rubric into the agent's context to guide the next Reason-or-Act decision, specifying what the agent should target in evidence seeking, search, reasoning, or self-evaluation. To make this guidance reliable, we train a dedicated rubric generator with GRPO. Unlike prior pairwise or binary preference formulations, our objective optimizes a list-wise Spearman rank-correlation reward against multi-judge expert consensus rankings, encouraging rubrics that are discriminative rather than merely plausible. On DeepResearchBench and SQA-CS-V2, Co-ReAct consistently improves over ReAct and representative test-time compute baselines across search agents built on both 8B/14B open-source and frontier closed-source base models. The trained rubric generator can also serve as a drop-in component that improves these baselines without changing their underlying decision mechanisms. Our code is publicly available at https://github.com/ZBWpro/Co-ReAct.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于ReAct范式的深度研究（deep research）智能体在执行搜索密集型、多步推理任务时存在的决策质量问题。研究背景是，当前的ReAct智能体在决定“下一步该做什么”（如搜索什么证据、采取何种推理或行动、何时停止）时，主要依赖自身的内部判断，这种自我导向的机制存在明显不足。具体来说，现有方法下，智能体容易产生浅薄、冗余或针对性不足的搜索轨迹，例如重复提交近似查询、在证据不足时过早停止，或固守于单一信息源。

尽管已有工作探索使用准则（rubrics）作为外部质量信号，但这些应用大多局限于“评估性”而非“指导性”。准则通常被用作训练阶段的奖励函数，或是对已完成输出的后验评估工具；在深度研究场景中，这些准则也往往是粗粒度的、面向最终报告，而非针对具体步骤。因此，现有的准则使用方式无法回答智能体在推理过程中面临的核心问题：“基于当前已观察到的信息，下一步行动应该满足哪些具体的要求？”

本文的核心问题是：如何将准则从事后的评估工具转变为推理过程中的、步骤级别的、具有区分度的行动选择指导信号？为此，论文提出了Co-ReAct框架，通过在每一个决策步骤向智能体上下文注入一个由专用生成器实时产生的、细粒度的步骤级准则，明确指引智能体在证据搜索、推理或自我评估中的具体目标，从而引导其做出更优的下一步行动。

### Q2: 有哪些相关研究？

1.  **增强推理时计算的方法**：例如Self-Refine、Best-of-N、Step-Back、CRITIC、Reflexion和Tree-of-Thought等。这些方法使用由通用LLM生成的提示、评分或批判信号来改进步骤级决策。本文区别在于，其指导信号并非来自未训练的提示模型，而是由一个经过GRPO训练、具有等级排序校准能力的专用规则生成器提供。实验表明，本文的信号可作为插件与这些方法互补，而非替代。

2.  **搜索策略强化学习方法**：如Search-R1、R1-Searcher、WebGPT和DR-Tulu。此类工作直接通过强化学习重新训练智能体的搜索策略本身，以产出更好的查询。本文的视角与之正交：不修改策略，而是训练一个**外部指导信号**（规则），在推理时被智能体消费，因此规则是独立于搜索策略之外的。

3.  **规则作为对齐信号**：如Rubric-ARM、OpenRubrics、DR-Tulu等。这些方法将规则用于**评估性**目的，例如在训练时作为奖励，或用于事后评估已完成的输出（如报告级规则）。本文核心区别在于，规则被用于**规定性**目的：在推理过程中，由规则生成器根据当前部分轨迹，逐步生成步骤级的规则，直接指导智能体下一步的“推理或行动”决策。

### Q3: 论文如何解决这个问题？

Co-ReAct的核心方法是将评估性准则转化为步骤级行动指南。整体框架分为三个阶段：首先，从真实ReAct轨迹中收集分支点，在每个分支点采样4个多样化候选动作并通过多裁判共识排序获得专家排名标签；其次，使用GRPO训练一个专用准则生成器，其奖励函数基于准则诱导的排名与专家排名之间的Spearman相关系数，配合原子性奖励和格式奖励进行优化；最后在推理阶段，将训练好的准则生成器作为即时指导意见注入搜索代理上下文。

关键技术包括：1）多裁判共识排序机制，通过Borda计数聚合来自不同模型家族的多个裁判对候选动作的完整排序，比点式评分更鲁棒；2）列表式Spearman奖励函数，直接优化准则在候选动作间的区分能力，而非仅生成表面合理的准则；3）推理时的五元组循环（准则-推理-行动-验证-观察），其中独立验证器检查动作对准则的满足程度，不满足时允许一次重试。创新点在于准则不仅作为事后评估工具，而是作为推理过程中的主动指导，且准则生成器可作为即插即用组件改进其他基线方法。该框架显著提升了搜索代理在多步推理任务中的轨迹质量。

### Q4: 论文做了哪些实验？

论文在两个基准数据集上评估了Co-ReAct：多轮搜索与长文生成的DeepResearchBench (DRB)和科学问题综合的SQA-CS-V2。实验设置中，所有方法共享两阶段流程：搜索代理通过ReAct循环收集证据，答案代理生成带引用的报告，工具集包含学术搜索、谷歌搜索和网页浏览。对比方法包括Self-Refine（迭代自我批评）、Best-of-N（采样4条轨迹选最优）、Step-Back（前加高层视角）和CRITIC（行动后验证搜索）。主要结果如表所示：在Qwen3-8B上，Co-ReAct在DRB达到平均34.01分（提升2.5%），SQA达74.80（提升2.8%），均优于最佳基线Self-Refine；在Qwen3-14B上，Co-ReAct在DRB达36.92分（提升7.9%），SQA达76.05（提升4.6%），显著超越第二名CRITIC。消融实验表明，去除RL训练使分数降至72.44，低于ReAct基线；去除列表式排序优化降为74.04；去除验证机制降至74.08。搜索行为分析显示，Co-ReAct平均调用6.5次工具、检索19.3个链接、引用18.6个来源，比ReAct分别提升约25%、52%和66%，且利用率达0.96。验证机制捕获了21.4%的不合格工具调用并触发重试。在Gemini 3.1 Pro上，Co-ReAct达到37.13分，比ReAct提升4.44%，而其他基线未能超越ReAct。

### Q5: 有什么可以进一步探索的点？

论文存在以下可探索点：首先，Co-ReAct仅针对固定搜索策略的ReAct范式增强，未验证其rubric能否堆叠在端到端RL训练的搜索智能体（如Search-R1）上，未来可探索跨范式迁移能力。其次，评估依赖LLM-as-a-judge（如Gemini），存在冗长性偏误等问题，可设计更鲁棒的评估标准或引入人类反馈校准。改进思路上，可尝试将rubric生成器与强化学习搜索策略联合训练，形成端到端的动态指导；或引入自适应rubric粒度，根据任务复杂度动态调整步骤级提示的详细程度。此外，当前rubric仅通过上下文注入影响决策，未来可探索将其嵌入动作空间或作为隐式奖励信号，进一步提升搜索效率与轨迹质量。

### Q6: 总结一下论文的主要内容

该论文提出了Co-ReAct框架，旨在解决ReAct风格代理在多步搜索推理任务中依赖内部判断、缺乏外部质量引导、导致决策浅层或冗余的问题。传统方法将评分准则用于训练奖励或事后评估，且多为粗粒度的报告级标准。Co-ReAct在推理过程中将步骤级评分准则注入代理上下文，指导其证据搜索、推理和自我评估等决策，形成（准则、推理、行动、验证、观察）的五元组结构。为生成可靠的准则，论文采用GRPO训练专用准则生成器，并创新性地利用列表级斯皮尔曼等级相关性奖励优化与多位专家共识的一致性，优于传统的成对或二元偏好目标。在DeepResearchBench和SQA-CS-V2数据集上，基于Qwen3-8B/14B及Gemini 3.1 Pro的搜索代理，Co-ReAct一致优于Self-Refine、Best-of-N、Step-Back等基线；其训练好的准则生成器作为即插即用模块，可提升所有基线性能。该工作表明，外部生成的、轨迹感知的步骤级评分准则是提升代理搜索能力的轻量且可组合的有效方法。
