---
title: "HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel"
authors:
  - "The Viet Bui"
  - "Wenjun Li"
  - "Yong Liu"
date: "2026-03-05"
arxiv_id: "2603.04750"
arxiv_url: "https://arxiv.org/abs/2603.04750"
pdf_url: "https://arxiv.org/pdf/2603.04750v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 8.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen3-8B"
  key_technique: "HiMAP-Travel (Hierarchical Multi-Agent Planning with synchronized global state, cooperative bargaining protocol, and unified role-conditioned policy trained with GRPO)"
  primary_benchmark: "TravelPlanner, FlexTravelBench"
---

# HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel

## 原始摘要

Sequential LLM agents fail on long-horizon planning with hard constraints like budgets and diversity requirements. As planning progresses and context grows, these agents drift from global constraints. We propose HiMAP-Travel, a hierarchical multi-agent framework that splits planning into strategic coordination and parallel day-level execution. A Coordinator allocates resources across days, while Day Executors plan independently in parallel. Three key mechanisms enable this: a transactional monitor enforcing budget and uniqueness constraints across parallel agents, a bargaining protocol allowing agents to reject infeasible sub-goals and trigger re-planning, and a single policy trained with GRPO that powers all agents through role conditioning. On TravelPlanner, HiMAP-Travel with Qwen3-8B achieves 52.78% validation and 52.65% test Final Pass Rate (FPR). In a controlled comparison with identical model, training, and tools, it outperforms the sequential DeepTravel baseline by +8.67~pp. It also surpasses ATLAS by +17.65~pp and MTP by +10.0~pp. On FlexTravelBench multi-turn scenarios, it achieves 44.34% (2-turn) and 37.42% (3-turn) FPR while reducing latency 2.5x through parallelization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在**长视野、硬约束规划任务**中的核心失败模式。研究背景是，尽管LLM在短视野、开放式任务中表现出色，但在需要同时满足严格预算、时间可行性、路线一致性等硬约束以及复杂用户偏好的组合优化问题上（如多日旅行规划），其性能会急剧下降。现有主流方法（如ReAct、Chain-of-Thought）采用**单体化、顺序执行的架构**，由一个单一策略逐令牌生成整个规划轨迹。这种方法存在一个根本缺陷：随着规划进程推进，中间的工具输出、搜索日志和推理痕迹不断累积，导致有效上下文长度增长，从而**稀释了对初始全局约束（如总预算）的注意力**，作者称之为“**长工具轨迹下的约束漂移**”。现有缓解策略（如ATLAS的迭代精炼）属于“生成-后修复”范式，即先生成完整候选计划再进行约束检查，这导致计算浪费，且延迟随计划长度呈超线性增长，未能从根源上解决问题。

因此，本文要解决的核心问题是：**如何设计一种新的智能体架构，以克服顺序LLM智能体在长视野、硬约束规划中出现的约束漂移问题，实现高效、可扩展且能主动在生成过程中保障全局一致性的规划**。为此，论文提出了HiMAP-Travel框架，其核心思想是通过**层次化多智能体规划**，将战略性的资源分配与战术性的每日执行解耦，从而在并行执行中主动、原子化地强制执行约束，将范式从“生成-后修复”转变为“构造即正确”。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类（具体为旅行规划评测）和架构类。

在**方法类**研究中，相关工作包括：1）基础序列规划方法，如ReAct和Toolformer，它们将推理与工具调用交织，但在长视野任务中易出现“约束漂移”；2）迭代优化方法，如Reflexion和EvoAgent，通过反思进行改进，但缺乏对全局约束的主动管理；3）分层与多智能体方法，如PMC（基于LLM的任务委派）、HIPLAN（分层规划）、MTP（管理者/执行者/监督者架构）和ATLAS（带约束管理器的验证-精炼循环）。这些方法大多支持分层或迭代，但通常缺乏并行执行、上下文隔离或确定性全局约束验证。本文的HiMAP-Travel通过引入分层并行执行、事务性监控和结构化协商协议，与这些方法区分开来，特别是在处理动态耦合约束时更鲁棒且延迟更低。

在**应用类（旅行规划评测）**方面，TravelPlanner和FlexTravelBench是评估智能体在预算、多样性等约束下规划能力的基准。先前方法如DeepTravel应用端到端强化学习进行序列规划，但早期次优决策会产生级联影响。HiMAP-Travel通过天级分解和并行规划缓解了这种序列依赖性，并在这些基准上取得了更高的最终通过率。

在**架构类**研究中，分层强化学习（HRL）和基于检索的分层规划（如HiPlan）提供了灵感。但HiMAP-Travel的创新在于其多智能体框架集成了角色条件化单一策略训练（使用GRPO）、同步全局状态和合作协商协议，从而实现了约束的主动执行和高效的资源重新分配，超越了以往依赖自然语言协商或事后纠正的方法。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HiMAP-Travel的分层多智能体规划框架来解决长视野、带硬约束的旅行规划问题。其核心思想是将复杂的整体规划解耦为两个功能层级：战略协调层和并行战术执行层，从而克服传统顺序LLM智能体在规划过程中因上下文增长而偏离全局约束的缺陷。

**整体框架与主要模块：**
框架包含一个**协调器（Coordinator）** 和多个**执行器（Executor）**。协调器位于战略层，负责解析用户查询，将全局需求（如总预算、必去目的地）分解为按天划分的元计划（子目标），包括目标城市、每日语义角色和预算提示。执行器位于战术层，每个执行器对应一天，基于分配的子目标并行生成当天的详细行程轨迹。这种设计将规划视野从T天缩短至T/D天，实现了并行化。

**关键技术机制与创新点：**
1.  **同步全局状态与事务监控器**：为解决并行执行带来的资源冲突（如预算超支、重复预订），框架引入了一个外部结构化的同步全局状态Σ。它作为一个确定性的事务监控器，通过原子操作（检查、提交）强制执行预算守恒、地点去重和交通模式一致性等硬约束。当执行器的动作可能违反约束时，监控器会直接拒绝并返回结构化错误，从而预防冲突，无需智能体间频繁协商。
2.  **协作议价协议**：为避免顶层分配不切实际的子目标导致系统僵化，框架设计了双向反馈机制。如果执行器发现分配的子目标不可行（如预算不足、时间不够），它会通过轻量级的JSON格式反馈状态、赤字和违规类型。协调器根据此反馈在下一轮迭代中重新调整元计划。这种“提议-反馈-重规划”的议价循环增强了系统的鲁棒性。
3.  **统一策略与角色条件化**：所有智能体（协调器和各执行器）共享同一个策略模型π_θ，通过系统提示词来区分不同角色。这种设计不仅减少了参数量，还促进了知识迁移——例如，在执行器角色中学到的关于航班价格的推理，可以在协调器角色中用于更好的战略预算分配。策略使用组相对策略优化进行训练。
4.  **高效训练机制**：针对多智能体训练内存消耗大的问题，提出了**共享经验回放缓冲区与先进先出更新机制**。不同角色的轨迹被存入统一缓冲区并按角色分区。一旦某个角色分区积累了足够数量的轨迹，就立即基于该角色条件进行策略更新并清空该分区数据，这大幅降低了峰值内存需求，并适应了不同角色轨迹生成速度的差异。

综上，HiMAP-Travel通过分层解耦、并行执行、硬约束外部监控、轻量级双向反馈以及统一的角色条件化策略，系统性地解决了长视野约束规划中的上下文漂移、资源冲突和信用分配难题。

### Q4: 论文做了哪些实验？

论文在TravelPlanner和FlexTravelBench两个基准上进行了实验。实验设置上，采用Qwen3-4B/8B作为骨干模型，使用GRPO算法在45个查询上进行训练，并与相同模型、训练和工具下的顺序基线DeepTravel进行严格控制对比。解码参数（temperature 0.7, top-p 0.9）和工具调用预算（每天最多15次）均保持一致。

在TravelPlanner（1225个查询）上，主要评估单轮规划在13个耦合约束下的表现。关键结果显示，HiMAP-Travel（Qwen3-8B）的最终通过率在验证集和测试集上分别达到52.78%和52.65%。相比顺序基线DeepTravel（43.98%），提升了8.67个百分点，且方差显著降低（std: 0.48% vs 7.18%）。同时，它超越了已发表方法ATLAS（35.00%）和MTP（42.68%）。在约束满足度上，其常识约束微观准确率为94.62%，硬约束微观准确率为50.47%。特别地，在5天行程的预算满足度上，从第1天到第5天均保持在90%以上（第5天91%），而顺序基线在第5天骤降至42%。

在FlexTravelBench上，评估多轮约束适应能力。HiMAP-Travel在2轮和3轮场景下的最终通过率分别达到44.34%和37.42%，优于对比方法。此外，由于并行化，在7天行程上实现了2.5倍的延迟降低（72秒 vs 基线190秒）。消融实验表明，移除全局同步状态、协调器、协商协议或并行性分别会导致性能下降9.58、12.98、3.88和7.18个百分点，验证了各组件的重要性。

### Q5: 有什么可以进一步探索的点？

本文提出的分层多智能体框架在并行化执行和约束维护方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架依赖于任务本身可进行清晰的层次分解（如按天规划），对于结构更模糊或动态性更强的长视野任务（如开放式对话或实时策略调整），其适用性有待验证。其次，当前的“协商-重规划”协议虽能处理局部不可行性，但可能引发多次迭代，增加整体计算开销；未来可研究更高效的冲突消解机制或引入预测模型来预先评估分配方案的可行性。此外，所有智能体共享同一策略虽有利于训练效率，但可能限制角色专业化能力的深度发展；探索在共享基座基础上加入轻量级角色适配模块，或许能在保持统一训练优势的同时提升各执行器的专项性能。最后，论文主要关注预算和唯一性等硬约束，对于“体验多样性”、“用户偏好”等软约束的集成处理尚未深入，如何将软约束量化并融入监控与协商机制是一个开放问题。从更广义看，该框架中的事务监控和协商协议可视为一种多智能体协调范式，未来可探索将其与基于世界模型的规划或符号推理结合，以增强在不确定环境下的鲁棒性和可解释性。

### Q6: 总结一下论文的主要内容

该论文针对传统顺序LLM智能体在长周期、多约束旅行规划中容易偏离全局约束的问题，提出了HiMAP-Travel分层多智能体规划框架。其核心贡献是将规划任务分解为战略协调与并行执行两层：一个协调器负责在全局层面跨天数分配资源，多个独立的日执行器则并行处理每日的具体规划。该方法通过三个关键机制实现：事务监控器确保并行智能体间的预算和唯一性约束；协商协议允许执行器拒绝不可行的子目标并触发重新规划；以及采用GRPO训练的统一策略，通过角色条件化驱动所有智能体。实验表明，在TravelPlanner基准上，HiMAP-Travel显著超越了顺序基线及现有先进方法，并在多轮交互场景中通过并行化大幅降低了延迟。该工作证明了分层与并行化在解决复杂约束规划问题上的有效性，为多智能体系统在现实长周期任务中的应用提供了新思路。
