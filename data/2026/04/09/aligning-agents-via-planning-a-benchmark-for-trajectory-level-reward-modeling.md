---
title: "Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling"
authors:
  - "Jiaxuan Wang"
  - "Yulan Hu"
  - "Wenjin Yang"
  - "Zheng Pan"
  - "Xin Li"
  - "Lan-Zhe Guo"
date: "2026-04-09"
arxiv_id: "2604.08178"
arxiv_url: "https://arxiv.org/abs/2604.08178"
pdf_url: "https://arxiv.org/pdf/2604.08178v1"
categories:
  - "cs.AI"
tags:
  - "Agent Alignment"
  - "Reward Modeling"
  - "Trajectory Evaluation"
  - "Benchmark"
  - "Tool-Using Agent"
  - "Planning"
  - "Preference Learning"
  - "RLHF"
relevance_score: 8.0
---

# Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling

## 原始摘要

In classical Reinforcement Learning from Human Feedback (RLHF), Reward Models (RMs) serve as the fundamental signal provider for model alignment. As Large Language Models evolve into agentic systems capable of autonomous tool invocation and complex reasoning, the paradigm of reward modeling faces unprecedented challenges--most notably, the lack of benchmarks specifically designed to assess RM capabilities within tool-integrated environments. To address this gap, we present Plan-RewardBench, a trajectory-level preference benchmark designed to evaluate how well judges distinguish preferred versus distractor agent trajectories in complex tool-using scenarios. Plan-RewardBench covers four representative task families -- (i) Safety Refusal, (ii) Tool-Irrelevance / Unavailability, (iii) Complex Planning, and (iv) Robust Error Recovery -- comprising validated positive trajectories and confusable hard negatives constructed via multi-model natural rollouts, rule-based perturbations, and minimal-edit LLM perturbations. We benchmark representative RMs (generative, discriminative, and LLM-as-Judge) under a unified pairwise protocol, reporting accuracy trends across varying trajectory lengths and task categories. Furthermore, we provide diagnostic analyses of prevalent failure modes. Our results reveal that all three evaluator families face substantial challenges, with performance degrading sharply on long-horizon trajectories, underscoring the necessity for specialized training in agentic, trajectory-level reward modeling. Ultimately, Plan-RewardBench aims to serve as both a practical evaluation suite and a reusable blueprint for constructing agentic planning preference data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）向智能体（Agent）范式演进过程中，奖励模型（RM）评估所面临的基准缺失问题。研究背景是，随着LLM从被动对话系统发展为能够通过工具集成推理（TIR）与环境交互的主动智能体，其行为模式从单一响应转变为包含用户输入、推理、工具执行和环境反馈的轨迹序列。这要求奖励模型不仅能评估最终结果，还需判断中间步骤是否合理、一致且安全。

然而，现有方法存在明显不足。当前的奖励模型基准主要集中于短上下文场景中评估有限维度（如帮助性和安全性），通常针对响应级别的偏好，缺乏对复杂推理过程的覆盖。虽然工具集成推理本质上是多轮交互，但现有的长上下文RM研究往往依赖人工扩展的上下文，无法刻画智能体工作流的自然复杂性和动态依赖性。此外，专门的工具使用基准主要验证孤立回合中的原子动作正确性，忽视了对连贯、长视野规划行为的评估。

因此，本文要解决的核心问题是：缺乏一个专门的、严格的基准来评估奖励模型在复杂工具集成场景下，对长视野、多步骤轨迹的偏好判断能力。为此，论文提出了Plan-RewardBench这一轨迹级偏好基准，旨在通过涵盖安全拒绝、工具无关/不可用、复杂规划和鲁棒错误恢复四大任务族的高质量正负轨迹对，系统评估不同奖励模型（判别式、生成式及LLM即法官）在真实多轮交互中判断规划逻辑和工具使用保真度的能力，并为智能体轨迹级奖励模型的专门化训练提供数据构建蓝图和诊断依据。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：奖励模型评测、工具调用与智能体轨迹评测，以及偏好协议与评估者偏差。

在**奖励模型评测**方面，RewardBench系列工作基于“提示-优选-劣选”三元组在对话、推理和安全等领域评估RM，建立排行榜。近期研究如LongRM关注长上下文输入下的RM性能衰减，而本文的Plan-RewardBench与之互补，不专注于长文档本身，而是评估在复杂工具使用环境中由多步规划、工具执行日志和多轮交互自然带来困难的**轨迹级**偏好判断。

在**工具调用与智能体轨迹评测**领域，BFCL评测函数调用的正确性；ToolRM及其FC-RewardBench关注面向结果的、单轮工具调用正确性的奖励建模；AgentRewardBench则评估对完整网页智能体轨迹的自动评判。与这些工作不同，本文专注于**纯文本、工具增强、轨迹层面**的偏好判断，强调在多轮工具交互中自然产生的长期规划标准（如规划一致性、错误恢复和拒绝质量），而非单步正确性或多模态输入。

在**偏好协议与评估者偏差**方面，现有研究表明，在某些场景下，成对比较比标量评分更能使LLM评估者与人类判断对齐，但偏好判断易受呈现方式和干扰项影响。本文借鉴这些发现，采用与轨迹排序和偏好学习用例一致的成对比较协议，并通过精心构建硬负例（控制长度/格式等表面线索）和进行顺序交换评估来减轻位置偏差。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为Plan-RewardBench的轨迹级偏好基准来解决评估智能体环境中奖励模型能力的挑战。其核心方法是创建一个包含复杂工具使用场景的成对轨迹偏好数据集，并设计统一的评估协议来诊断现有奖励模型的不足。

**整体框架与主要模块**：基准构建遵循一个系统化的流程。首先，从Toucan等现实工具注册库中获取高质量种子轨迹。然后，通过**多模型自然推演**（使用如Qwen-Agent和OpenAI-Agent等不同智能体运行时，并变化基础模型、提示、温度等参数）来扩展候选轨迹池，以捕获自然的成功与失败模式。接着，将任务实例分类到四个核心场景族（安全拒绝、工具无关/不可用、复杂规划、鲁棒错误恢复），并针对每个族的典型失败模式，通过三种互补来源精心构建**难以区分的负例**：1) 来自多模型推演池的**自然负例**；2) 引入可控失败的**基于规则的扰动**（如约束丢弃、实体替换）；3) 从高分候选轨迹出发，通过最小化编辑生成的**近邻负例**，以制造风格可信但违反特定准则的案例。最后，采用**两阶段LLM标注协议**进行轨迹偏好标注：先由多评委面板根据族特定规则进行1-5分标量评分和诊断标签，再通过元评审解决分歧，并最终通过独立的成对评审确认偏好方向，同时进行**人工审计**以确保标签与人类判断一致。

**关键技术**：1) **成对轨迹偏好任务设计**：将评估形式化为给定工具环境和用户交互下的两个候选轨迹之间的偏好选择，这直接支持判别式/生成式奖励模型的训练、推理时重排序以及基于偏好的优化。2) **硬负例的战略构建**：通过结合自然推演、规则扰动和最小编辑扰动，确保负例具有混淆性，无法通过表面线索（如长度、格式）简单拒绝，从而迫使模型进行深度推理。3) **分族评估与诊断**：针对四个场景族分别设计评估规则和构建负例，使得基准不仅能评估整体性能，还能进行细粒度的失败模式分析（例如，安全拒绝中的不安全合规、复杂规划中的工具接地伪造）。4) **难度与偏差控制**：在组建成对数据时，平衡“近邻比较”和“易区分对”，并分层选择对以避免长度、工具令牌比等表面特征带来的偏差。

**创新点**：主要创新在于首次提出了一个专门针对**工具集成环境中轨迹级奖励建模**的综合性基准。它超越了传统单轮文本偏好评估，专注于多轮、工具交互的智能体轨迹。其构建方法强调**现实分布与可控挑战的平衡**（70%自然轨迹，30%扰动/注入），并系统化地覆盖了智能体规划中的关键挑战场景。此外，基准提供了**统一的评估协议**，能够横向比较判别式奖励模型、生成式奖励模型和LLM即评委三类方法，并揭示它们在长视野轨迹上性能显著下降等共性挑战，从而为开发专门的智能体轨迹级奖励建模技术提供了明确的路线图和可复用的数据构建蓝图。

### Q4: 论文做了哪些实验？

论文在Plan-RewardBench基准上进行了系统实验。实验设置方面，评估了三大类评判模型：判别式奖励模型（DRMs，对单条轨迹独立打分）、生成式奖励模型（GRMs，输出偏好决策及推理）以及通用LLM-as-Judge（采用成对“评判-批判”协议）。所有评估器在统一的成对协议下进行，接收相同的上下文输入（包括工具环境定义、多轮对话历史和完整交错轨迹），并采用位置偏置控制（如A/B交换协议）。

使用的数据集/基准测试是作者构建的Plan-RewardBench，涵盖四大任务族：安全拒绝、工具无关/不可用、复杂规划、鲁棒错误恢复。该基准包含经过验证的正向轨迹和通过多模型自然推演、基于规则的扰动及最小编辑LLM扰动构建的混淆性硬负例。评估按轨迹长度和任务类别分层进行。

对比方法包括代表性的开源和闭源模型，如Qwen-Plus、GPT-5、Gemini-3-Flash、Inf-ORM-Llama3.1-70B等。

主要结果与关键指标如下：1）整体性能：最佳平均准确率为Qwen-Plus（69.96%），但无模型在所有类别占优；2）任务差异：安全拒绝任务上GPT-5最佳（84.80%），工具无关任务上Gemini-3-Flash最佳（75.55%），显示基准评估能力多维；3）规模影响：70B参数标量RM（Inf-ORM-Llama3.1-70B，69.21%）与顶级LLM法官竞争，但27B标量RM远落后，表明参数规模有帮助但非唯一因素；4）长轨迹挑战：所有评估器在长视野轨迹（如多轮困难任务）上表现显著下降，准确率难以超过70%；5）安全拒绝极化：开源标量RM准确率接近随机（49-57%），而LLM法官跨度大（40.69-84.80%）；6）鲁棒错误恢复：开源RM（75.35%）与SOTA LLM法官（74.93%）相当，显示其对显式执行信号的利用能力。此外，分析显示输入长度超过32K令牌时，LLM法官准确率急剧下降，而点式RM衰减更线性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，基准测试目前局限于英文文本环境，未来可扩展至多模态（如视觉、语音）和多智能体交互场景，以评估奖励模型在更复杂环境下的泛化能力。其次，当前任务分布不均（如安全拒绝类样本较少），未来可通过合成数据生成或跨任务迁移学习来平衡数据，并探索更具挑战性的负样本构建方法（如对抗性扰动）。此外，论文提到黄金标签存在主观性，未来可结合人类反馈与自动化评估（如基于规则的验证）来提升标签可靠性。从技术角度看，现有奖励模型在长轨迹任务上表现显著下降，未来可研究分层奖励建模或引入规划感知的注意力机制来改善长期依赖问题。最后，可探索将基准测试与在线学习结合，使奖励模型能在动态环境中持续优化，更好地适应真实世界智能体的复杂需求。

### Q6: 总结一下论文的主要内容

该论文针对智能体（Agent）领域奖励模型（RM）评估的空白，提出了一个名为Plan-RewardBench的轨迹级偏好基准。其核心问题是：在工具集成环境中，现有奖励模型难以评估智能体在复杂、长视野任务中的整体规划轨迹质量，缺乏专门的评测基准。

论文的主要方法是构建一个涵盖四大代表性任务族（安全拒绝、工具无关/不可用、复杂规划、鲁棒错误恢复）的基准数据集。该数据集通过多模型自然推演、基于规则的扰动和最小编辑的LLM扰动，生成了经过验证的正向轨迹和具有迷惑性的困难负例。作者在统一的成对比较协议下，对生成式、判别式以及“LLM即法官”三类代表性奖励模型进行了基准测试。

主要结论是，所有评估模型都面临巨大挑战，尤其是在长视野轨迹上性能急剧下降。这表明，将通用大语言模型直接用作强化学习循环中的绝对奖励信号是脆弱的，容易受到噪声和偏见的影响。论文的意义在于，它不仅提供了一个实用的评估工具集，还为构建面向智能体规划的偏好数据提供了一个可复用的蓝图，旨在推动可靠轨迹级奖励信号的发展，从而促进下一代对齐的、以规划为中心的智能体的研发。
