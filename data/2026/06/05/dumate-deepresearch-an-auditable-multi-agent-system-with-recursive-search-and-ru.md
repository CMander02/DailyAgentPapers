---
title: "DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning"
authors:
  - "Lingyong Yan"
  - "Can Xu"
  - "Yukun Zhao"
  - "Wenxuan Li"
  - "Qingyang Chen"
  - "Jiulong Wu"
  - "Wenli Song"
  - "Xiangnan Li"
  - "Weixian Shi"
  - "Yiqun Chen"
  - "Xuchen Ma"
  - "Yuchen Li"
  - "Jiashu Zhao"
  - "Shuaiqiang Wang"
  - "Jianmin Wu"
  - "Dawei Yin"
date: "2026-06-05"
arxiv_id: "2606.07299"
arxiv_url: "https://arxiv.org/abs/2606.07299"
pdf_url: "https://arxiv.org/pdf/2606.07299v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Deep Research"
  - "Tool-Use Agent"
  - "Long-Horizon Planning"
  - "Recursive Search"
  - "Auditable Agent"
  - "Dynamic Planning"
  - "Test-Time Optimization"
  - "Agent Benchmark"
relevance_score: 9.0
---

# DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning

## 原始摘要

Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前深度研究（Deep Research）系统在实际应用中面临的四大核心挑战。研究背景是，尽管深度研究作为新兴智能体范式，旨在模拟人类研究者的系统化方法论，来处理复杂、开放的研究任务，但现有系统存在显著不足。首先，现有系统在处理长程规划和动态范围定义时表现短视，ReAct风格的逐步策略缺乏全局视野，难以在证据积累过程中灵活调整计划。其次，复杂任务的分解与调度瓶颈突出，单一扁平智能体难以兼顾高层策略与底层检索，局部失败极易传播至全局。第三，长文本合成中的幻觉难以抑制，且缺乏基于证据的自主停止机制，导致事实准确性无法保证。最后，现有系统的推理过程缺乏可审计性，用户无法追踪中间决策与工具调用，限制了在高风险场景中的可信度。针对这些问题，本文提出DuMate-DeepResearch，一个基于Qianfan Agent Foundry的多智能体框架。其核心贡献包括：通过解耦智能体核心与工具生态实现全过程可审计；引入基于图的动态规划策略，以全局视角迭代优化研究路线图；设计递归双层执行机制，隔离噪声检索、稳定长程执行；以及采用基于评分标准的测试时优化，将动态生成的质量标准作为推理脚手架，确保生成结果忠实于证据并自适应停止。最终，该方案在DeepResearch Bench和DeepResearch Bench II上均取得了新的最佳成绩。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**架构设计类**方面，现有工作包括OpenAI的DeepResearch等**单体架构**系统，将全部模块耦合于中央推理引擎，虽保证控制流程统一但限制了可扩展性；以及n8n等**管道架构**系统，通过顺序阶段分解流程实现组件复用，但难以处理复杂迭代和全局反馈。本文的DuMate-DeepResearch采用**解耦的多智能体架构**，将认知核心（Agent Core）与工具生态分离，实现完全可审计的执行轨迹，这是与前述系统的关键区别。**规划与执行类**方面，ReAct风格的**单步贪婪策略**缺乏全局视野，易导致局部最优或过早收敛。本文提出**图基动态规划**，将研究路线建模为有向无环图并支持粗到细扩展与回溯，以及**递归双层执行**机制，将复杂搜索子任务隔离到内部搜索智能体中，防止单点失败传播。**事实性与评估类**方面，许多系统依赖后验验证或固定检索预算。本文引入**动态生成评估准则**作为测试时推理支架，实现证据基生成和自适应停止，在两个基准上达到SOTA（58.03%和61.95%），在信息召回和分析维度尤其领先。

### Q3: 论文如何解决这个问题？

DuMate-DeepResearch构建了一个基于千帆智能体工坊的多智能体深度研究框架，核心架构采用解耦设计：智能体核心负责任务理解、规划和调度，而可扩展的工具生态负责检索、证据获取和报告生成，确保每个中间决策和工具调用都可追溯。整体工作流程遵循状态转换循环，维护研究状态s_t=(z, p_t, e_t, ρ_t)，其中固定任务上下文z包含研究主题x和报告大纲O，p_t是图结构计划，e_t累积证据，ρ_t是引导信号。

框架包含三个关键模块：路由器模块解析用户查询并生成结构化任务表示，规划器模块作为战略引擎维护动态DAG图计划，执行模块负责调度工具调用、搜索智能体和写作器。主要技术创新包括三个机制：一是基于图的动态规划策略，采用从粗到细的扩展方式，初始宏观探索后生成固定大纲，然后进行粒度化细化，支持反思、重规划、回溯和并行分支；二是递归双层执行设计，外部研究智能体将复杂搜索子任务委托给内部搜索智能体独立执行本地规划循环，隔离嘈杂检索并稳定长期执行；三是基于标准引导的测试时优化机制，动态生成任务特定质量标准，用作证据驱动合成和自适应停止的实时推理支架。该框架在DeepResearch Bench和DeepResearch Bench II上均取得最优结果。

### Q4: 论文做了哪些实验？

论文在DeepResearch Bench和DeepResearch Bench II两个基准上进行了全面实验。实验设置中，外规划循环最多15次迭代，每个内部搜索代理最多进行10轮检索，每轮生成最多3个子查询，每个查询返回3个结果，并使用百度搜索作为主要检索后端，所有结果基于3次独立运行取平均。

在DeepResearch Bench上，系统对比了DR-Tulu、OpenAI DeepResearch、Gemini 2.5 Pro DeepResearch等20多个基线模型，按照官方评估协议（基于LLM评判的参考和自适应标准评估）从全面性、洞察力、指令遵循和可读性四个维度打分。DuMate-DeepResearch以总分58.03%取得最佳成绩，超越第二名ZTE Nebula DeepResearch（57.27%），并在全面性（59.48%）和洞察力（61.48%）两个维度排名第一。

在DeepResearch Bench II上，系统在22个领域的132个任务中使用9430个细粒度二元评估标准进行端到端评估，评估信息召回、分析和呈现三个维度。DuMate-DeepResearch以总分61.95%获得最佳总体成绩，并在信息召回和分析维度排名第一。评估时系统仅访问查询，独立生成评估标准，不接触基准的隐藏评估标准或专家报告。

### Q5: 有什么可以进一步探索的点？

未来的探索方向可从三个维度展开。首先，当前递归搜索的层级深度仍依赖人工预设，可引入自适应深度控制机制，根据搜索任务的语义复杂度动态调整内层Agent的规划循环次数，避免过度搜索或搜索不足。其次，基于课程的测试时优化目前依赖任务无关的通用质量准则，未来可结合领域知识库构建可迁移的课程规则库，同时通过强化学习让规则权重随任务类型自动调整。此外，系统的可审计性虽已实现工具调用链条全程追踪，但缺乏对中间推理步骤的因果归因能力，可借鉴反事实推理技术，当最终报告出现事实错误时能精准定位是搜索缺失、证据权重偏差还是综合阶段的逻辑断层。在扩展性上，当前工具生态仍局限于标准化检索接口，未来可支持动态注册异构工具（如代码解释器、实时API），并通过工具组合图自动发现最优协作路径。最后，跨模态任务（如图表分析、数学证明）的递归规划也是重要延伸方向。

### Q6: 总结一下论文的主要内容

DuMate-DeepResearch 是一个用于深度研究（DR）的多智能体框架，旨在解决现有DR系统在长程规划、复杂任务分解、幻觉风险和过程可审计性方面的局限。其核心贡献在于：首先，基于千帆Agent Foundry，将核心智能体（处理理解、规划与调度）与可扩展的工具生态系统解耦，使中间决策和工具调用完全可追溯，提升了可审计性。其次，引入了三种关键机制：基于图的动态规划策略，通过反射、重规划、回溯和并行分支，实现从粗到细的研究路径扩展与持续修正；递归双层执行设计，将复杂搜索子任务委托给内部搜索智能体独立执行，隔离噪声干扰以保障长程稳定性；以及基于量规的测试时优化机制，动态生成任务特定质量标准，作为推理支架进行基于证据的合成与自适应停止。实验表明，该方法在DeepResearch Bench和DeepResearch Bench II两个基准上均取得了最佳总分，建立了新的最优性能，显著提升了报告质量、信息召回与分析能力。
