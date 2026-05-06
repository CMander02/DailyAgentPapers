---
title: "From Intent to Execution: Composing Agentic Workflows with Agent Recommendation"
authors:
  - "Kishan Athrey"
  - "Ramin Pishehvar"
  - "Brian Riordan"
  - "Mahesh Viswanathan"
date: "2026-05-05"
arxiv_id: "2605.03986"
arxiv_url: "https://arxiv.org/abs/2605.03986"
pdf_url: "https://arxiv.org/pdf/2605.03986v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Agent Recommendation"
  - "LLM-based Planner"
  - "Agent Orchestration"
  - "Information Retrieval"
relevance_score: 8.5
---

# From Intent to Execution: Composing Agentic Workflows with Agent Recommendation

## 原始摘要

Multi-Agent Systems (MAS) built using AI agents fulfill a variety of user intents that may be used to design and build a family of related applications. However, the creation of such MAS currently involves manual composition of the plan, manual selection of appropriate agents, and manual creation of execution graphs. This paper introduces a framework for the automated creation of multi-agent systems which replaces multiple manual steps with an automated framework. The proposed framework consists of software modules and a workflow to orchestrate the requisite task- specific application. The modules include: an LLM-derived planner, a set of tasks described in natural language, a dynamic call graph, an orchestrator for map agents to tasks, and an agent recommender that finds the most suitable agent(s) from local and global agent registries. The agent recommender uses a two-stage information retrieval (IR) system comprising a fast retriever and an LLM-based re-ranker. We implemented a series of experiments exploring the choice of embedders, re- rankers, agent description enrichment, and supervising critique agent. We benchmarked this system end-to-end, evaluating the combination of planning, agent selection, and task completion, with our proposed approach. Our experimental results show that our approach outperforms the state-of-the- art in terms of the recall rate and is more robust and scalable compared to previous approaches. The critique agent holistically reevaluates both agent and tool recommendations against the overall plan. We show that the inclusion of the critique agent further enhances the recall score, proving that the comprehensive review and revision of task-based agent selection is an essential step in building end-to-end multi-agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文旨在解决多智能体系统（MAS）自动化构建的核心挑战。当前，将用户意图转化为可执行的多智能体工作流仍高度依赖人工操作，需要手动分解任务、选择适配的智能体并构建执行图。随着智能体数量爆炸式增长，传统基于关键词或LLM单次输入上下文的搜索方式在处理大规模智能体注册库时效率极低且缺乏扩展性。现有方法的不足主要体现在三点：手动规划流程繁琐耗时、智能体选择无法兼顾效率和准确性、缺乏对工作流冗余和容错性的系统化支持。

本文提出的AutoMAS框架尝试解决上述问题。其核心是通过端到端自动化流程，将用户自然语言意图直接转化为带状态机（FSM）的智能体工作流。具体创新包括：采用两阶段混合检索（快速检索+LLM重排序）的智能体推荐系统，在保持可扩展性的同时提升召回率；通过动态执行图和冗余路径增强系统鲁棒性；引入批评智能体从整体规划角度对智能体与工具选择进行二次校验。实验证明该方法在召回率、鲁棒性和可扩展性上均超越现有基线，为大规模自动化构建MAS提供了可行方案。

### Q2: 有哪些相关研究？

在相关研究方面，本文的工作可分为以下几类：**方法类**中，现有的多智能体系统（MAS）构建依赖手动规划与智能体选择，如通过LLM上下文直接选择智能体或基于图的条件概率选择。本文提出的框架则用自动化流程替代这些手动步骤，重点引入两阶段信息检索（快速检索器+LLM重排器）进行智能体推荐，并通过智能体描述增强提升语义表示，这与Re-invoke和ToolGen的检索与调用生成方法形成对比，但更强调模块化与可扩展性。**评测类**方面，TaskBench等基准侧重于评估LLM分解用户意图为子任务的能力，但未集成推荐与检索技术；本文则端到端评估规划、智能体选择与任务完成，并引入批评智能体全局重审推荐，显著提升了召回率。**优化类**方向中，ITR-RAG和Reagt通过迭代调优或自我纠错提升检索可信度，但本文的批评机制更关注工作流中智能体的全局最优性（如输入输出兼容性、成本约束），而非局部检索精度。总体而言，本文在自动化流水线构建、两阶段智能体推荐与全局批评优化上超越了现有工作，解决了“在智能体栈中找针”的挑战。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为AutoMAS的端到端自动化框架，用于动态生成多智能体系统（MAS），以替代人工设计流程。其核心方法包括以下组件：

1. **LLM驱动规划器**：接收用户自然语言意图，自动生成任务序列（FSM），并支持利用历史计划数据库（RAG）优化规划。

2. **可变调用图（VCG）**：动态路由机制，基于环境反馈（如网络状态、延迟、成本）选择最优执行路径。例如，在"查找餐厅"任务中，根据用户对成本和速度的偏好，从多个候选智能体中动态组合路径。

3. **智能体推荐器（AR）**：采用两阶段信息检索系统：
   - 第一阶段（检索器）：混合搜索（关键词+嵌入向量），快速召回候选智能体，支持约束过滤；
   - 第二阶段（重排序器）：基于LLM的语义重排，提升前序结果精度。

4. **智能体描述增强**：在索引阶段，通过合成查询扩展智能体元数据（如为"航班查询"智能体生成"从纽约到旧金山订票"的查询），生成更鲁棒的嵌入向量，不增加检索延迟。

5. **批判智能体**：可选的第三阶段，从全局视角评估智能体与任务的匹配性。支持两种模式：
   - 任务内模式：仅基于当前任务优化推荐；
   - 计划外模式：结合完整工作流和约束（如输入输出兼容性），提出调整建议或修改规划。

整体框架将用户意图转化为可执行的MAS，通过动态图优化、两阶段检索增强鲁棒性，批判机制确保全局最优。实验表明，该方法在召回率和可扩展性上优于基线。

### Q4: 论文做了哪些实验？

论文在多个维度上进行了实验。首先，在Agent推荐（AR）任务上，使用ToolE数据集（199个agent和20550个查询-工具对），对比了不同嵌入模型（text-embedding-3-small vs. large）和重排序器（gpt-4o vs. o1）的组合。主要指标为nDCG、Recall和mAP。结果表明，“text-embedding-3-large+重排序器”在nDCG@1上达0.7355，而仅检索器为0.6311，提升了模型早期精度。同时，Agent描述丰富化（如合成10个查询取平均嵌入）和过滤策略进一步将Recall提升至0.8398，mAP达0.8173，显著优于Re-Invoke方法（Recall仅为0.7821）。

其次，在端到端规划与组合任务中，基于TaskBench数据集（103个工具/agent和17000个查询），使用ReAct风格规划器进行实验。采用三种评价方式：语义指标（Rouge、BERTScore）显示综合Rouge-L为0.479；LLM-as-a-judge评估显示整体匹配率为59.3%，step-wise比率为0.742；结构化预测指标更细致，如DailyLife APIs的Tool F1达0.9064，序列相似度0.8956。最后，加入Critique代理进行迭代校正，进一步提升了性能，如Tool F1在DailyLife上提升至0.9161，序列相似度提升至0.9034，证明了Critique在全局规划中的有效性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在LLM重排序器对指令遵循能力的不足，存在对低成本代理的固有偏见，这暗示预训练数据可能携带了特定偏好。未来可探索方向包括：通过提示工程或微调来矫正LLM的决策偏好，使其能灵活适配不同成本/质量要求的任务；其次，当前系统依赖静态代理描述，可引入动态描述生成机制，根据任务上下文实时优化代理简介以提升检索准确性。此外，架构中规划模块与代理选择模块的耦合度仍需降低，可借鉴分层强化学习思想，让规划器生成抽象任务依赖图后再由推荐系统具体匹配。另一个值得深挖的点是批判机制的改进——当前仅做整体性重评，未来可设计多轮交互式批评，让代理通过辩论修正推荐结果。最后，面对海量代理库，可探索对抗训练增强检索鲁棒性，并引入增量学习使推荐系统能快速适应新注册代理。

### Q6: 总结一下论文的主要内容

该论文提出AutoMAS框架，旨在解决多智能体系统（MAS）构建中手动规划、代理选择和执行图创建的低效问题。核心贡献是自动化从用户意图到可执行工作流的全流程，通过两个主要模块实现：基于LLM的规划器将意图分解为子任务并表示为有限状态机（FSM）；两阶段代理推荐器（快速检索+LLM重排序）高效匹配任务与代理，并结合代理描述增强和批判机制优化选择。实验在ToolE和TaskBench数据集上进行，结果表明该框架在召回率上优于现有方法（如Re-Invoke），且具有更好的鲁棒性和可扩展性。批判机制进一步提升了选择质量，证明端到端构建中整体性审查的重要性。该工作为应对大规模代理注册表下的自动化MAS构建提供了有效方案。
