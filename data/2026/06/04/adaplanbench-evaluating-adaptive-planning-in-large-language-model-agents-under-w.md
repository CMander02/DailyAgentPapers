---
title: "AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints"
authors:
  - "Jiayu Liu"
  - "Cheng Qian"
  - "Zhenhailong Wang"
  - "Bingxuan Li"
  - "Jiateng Liu"
  - "Heng Wang"
  - "Jeonghwan Kim"
  - "Yumeng Wang"
  - "Xiusi Chen"
  - "Yi R. Fung"
  - "Heng Ji"
date: "2026-06-04"
arxiv_id: "2606.05622"
arxiv_url: "https://arxiv.org/abs/2606.05622"
pdf_url: "https://arxiv.org/pdf/2606.05622v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "自适应规划"
  - "动态约束"
  - "交互式评测"
  - "任务规划"
  - "规划能力"
  - "用户约束"
  - "世界约束"
relevance_score: 9.5
---

# AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints

## 原始摘要

Planning for real-world problems by language models often involves both world and user constraints, which may not be fully specified upfront and are progressively disclosed through interaction. However, existing benchmarks still underexplore adaptive planning under such progressively revealed dual constraints. To address this gap, we introduce AdaPlanBench, a dynamic interactive benchmark for evaluating whether Large Language Model (LLM) agents can adaptively plan and re-plan under progressively revealed world and user constraints. AdaPlanBench is built on 307 household tasks, with a scalable constraint construction pipeline that augments each task with dual constraints. At runtime, agents interact with the environment in a multi-turn protocol where hidden constraints are revealed only when the agent proposes a plan that violates them, requiring iterative plan revision under accumulating feedback. This makes planning challenging, as agents must infer and track constraints from feedback while re-planning effectively. Experiments on ten leading LLMs show that adaptive planning under dual constraints remains challenging, with the best model reaching only 67.75% accuracy. We further observe that performance degrades as more constraints accumulate, with user constraints posing a particularly large challenge and failures often stemming from weaker physical grounding and reduced effectiveness. These results establish AdaPlanBench as a testbed for dual-constrained interactive planning and highlight the challenge of reliable adaptation to dynamically revealed constraints in LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）智能体在现实世界任务中，面对逐步揭示的双重约束（世界约束和用户约束）时，缺乏自适应规划能力评估的问题。研究背景是，现有大语言模型智能体已在复杂交互任务中取得成功，但现实规划往往受限于用户偏好、优先级等用户约束，以及工具可用性、资源限制等世界约束。然而，现有基准测试存在明显不足：它们大多只关注单一维度的约束（如仅世界约束或仅用户约束），忽略了双重约束共同作用且逐步披露的挑战。具体而言，这些基准未能模拟约束并非预先完全指定，而是通过交互逐步揭示的渐进式披露过程，也缺乏对大型动作空间和解决方案空间中自适应重新规划的严格评估。为此，论文提出AdaPlanBench，一个动态交互式基准测试，它在307个家庭任务基础上，通过可扩展的自动管道为每个任务注入双重约束。在运行时，约束被隐藏，只有当智能体提出违反约束的计划时才会被揭示，迫使智能体在累积反馈中迭代重规划。核心问题是评估大语言模型智能体能否在动态揭示的双重约束下，实现有效的自适应规划和重新规划。

### Q2: 有哪些相关研究？

根据论文和相关工作分析，相关研究主要可分为以下几类：  
1. **带有约束的规划类基准**：如CostBench和FlowBench关注单一维度约束（成本或流程），但未实现用户与世界的双重约束（Dual Constraint）同时渐进披露。NaturalPlan和TravelPlanner虽涉及双重约束，但缺少交互式重新规划（Iterative Re-planning）和渐进披露机制。  
2. **用户偏好与交互类基准**：PrefEval和UserBench侧重于用户约束或交互，但忽略世界约束；PersonaMem-v2和RealPref关注用户偏好渐进披露，但未纳入环境限制和开放式评估。  
3. **世界交互与任务执行类基准**：τ-Bench和τ²-Bench包含世界交互和部分渐进披露，但缺乏完整的双重约束和可扩展的约束构造。  

本文（AdaPlanBench）与上述基准的核心区别在于：首次同时具备**迭代重新规划**、**用户与世界的双重约束**、**渐进披露**、**开放式评估**和**可扩展约束构造**六大特性，填补了现有工作在自适应规划下双重约束协同评估的空白。

### Q3: 论文如何解决这个问题？

AdaPlanBench通过两大核心组件解决动态规划问题：自动化约束构建流程和渐进式约束披露的交互协议。

**核心方法**采用多轮自适应重规划机制。在数据构建阶段，基于307个家庭任务，使用多智能体框架为每个任务构建双重约束档案（世界约束和用户约束）。具体通过三步迭代流程：1）**计划采样**：使用多个规划器在约束下生成候选方案；2）**约束提取**：从方案中提取工具及其属性，转化为世界约束（如工具不可用）和用户约束（如用户偏好）；3）**约束合并**：去重规范化后反馈指导下一轮采样，生成低中高三种难度等级。

**创新架构**体现在运行时交互协议：智能体与环境进行多轮动态交互，隐藏约束仅在智能体提出违反约束的方案时才被逐步披露。系统包含三个关键模块：**LLM评判器**评估方案的世界约束满意度、用户约束满意度和规划质量；**用户模拟器**将违反的约束转化为自然语言反馈；**终止条件**包括找到有效方案、达到最大轮次或连续两轮无新约束违反。

**关键技术**包括：1）基于查询重写和过滤的原始数据清洗；2）多角色语言模型协作（重写器、过滤器、规划器、提取器、合并器、检查器）；3）基于难度分档的增量约束积累。这种设计使智能体需要同时从反馈中推断潜在约束、追踪已披露违规并持续修正方案。

### Q4: 论文做了哪些实验？

论文提出了AdaPlanBench基准，用于评估大语言模型（LLM）智能体在逐步揭示的世界和用户双重约束下的自适应规划能力。实验评估了10个主流LLM，包括GPT系列（GPT-5、GPT-5-Mini、GPT-5-Nano）、DeepSeek（DeepSeek-v4-Flash）、Gemini系列（Gemini-3-Flash、Gemini-3.1-Pro）以及开源模型Qwen3系列（8B、14B、32B）和Llama-3.3-70B-Instruct。基准基于307个家务任务构建，每个任务通过可扩展的约束构造管道添加双重约束。实验采用多轮交互协议，代理提出违反隐藏约束的计划时才揭示约束，需根据累积反馈迭代修订计划。主要指标包括：准确率（Acc.%）、有效计划率（VPR%）、平均交互轮次（Avg Turns）、世界约束平均重复违规（AWRV）和用户约束平均重复违规（AURV）等。结果显示，最佳模型GPT-5仅达到67.75%的准确率，Gemini-3.1-Pro约35%，开源模型普遍低于30%。高VPR（如Gemini系列超90%）并未转化为高准确率。性能与主动约束探索（ATWC、ATUC）强相关（相关系数达0.898和0.919）。用户约束比世界约束更具挑战性，且模型规模并不直接决定自适应规划能力。

### Q5: 有什么可以进一步探索的点？

### 局限性与未来研究方向

论文主要在家庭领域验证，未来可扩展到旅行、办公等更广泛的场景，以检验双约束渐进披露框架的泛化能力。LLM裁判的潜在偏见虽通过多模型聚合部分缓解，但引入更细粒度的对抗验证或人类反馈校正机制仍有价值。当前纯文本环境隔离了感知与执行噪声，未来可整合多模态输入（如视觉场景理解）和具身操作，模拟真实世界的感知-规划耦合挑战。约束建模采用对象-属性简化形式，未能捕捉现实约束的模糊性、软性偏好及组合逻辑，下一步可引入自然语言模糊约束或概率性约束表示，并结合用户交互历史进行自适应约束推断。此外，随着约束数量增加，模型在物理推理和用户意图理解上出现显著退化，需要探索结构化约束记忆、动态子目标分解或多阶段规划框架来提升长程交互下的稳定性。

### Q6: 总结一下论文的主要内容

AdaPlanBench是一个用于评估大语言模型（LLM）代理在渐进披露的客观世界和用户双重约束下进行自适应规划与重规划的基准测试。该研究针对现有基准忽视这种动态约束的问题，基于307个家务任务构建了可扩展的约束生成流程。在运行时，代理通过多轮交互与环境协作，只有当提议的计划违反隐藏约束时，这些约束才会被揭示，迫使代理在不断累积的反馈下迭代修正计划。实验结果表明，即使在顶尖LLM中，自适应规划也极具挑战性，最佳模型准确率仅为67.75%，且随着约束增多性能显著下降，其中用户约束尤其困难，失败常源于弱物理基础知识和规划有效性降低。这项工作被确立为动态双重约束下交互式规划的测试床，突出了LLM代理在动态环境中的可靠适应性仍是重大挑战。
