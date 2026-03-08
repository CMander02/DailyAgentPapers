---
title: "ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context"
authors:
  - "Zidi Xiu"
  - "David Q. Sun"
  - "Kevin Cheng"
  - "Maitrik Patel"
  - "Josh Date"
date: "2026-03-02"
arxiv_id: "2603.01357"
arxiv_url: "https://arxiv.org/abs/2603.01357"
pdf_url: "https://arxiv.org/pdf/2603.01357v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 8.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "Claude-4.5-Opus, DeepSeek-V3.2"
  key_technique: "ASTRA-bench (event-driven scenario generation pipeline)"
  primary_benchmark: "ASTRA-bench"
---

# ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context

## 原始摘要

Next-generation AI must manage vast personal data, diverse tools, and multi-step reasoning, yet most benchmarks remain context-free and single-turn. We present ASTRA-bench (Assistant Skills in Tool-use, Reasoning \& Action-planning), a benchmark that uniquely unifies time-evolving personal context with an interactive toolbox and complex user intents. Our event-driven pipeline generates 2,413 scenarios across four protagonists, grounded in longitudinal life events and annotated by referential, functional, and informational complexity. Evaluation of state-of-the-art models (e.g., Claude-4.5-Opus, DeepSeek-V3.2) reveals significant performance degradation under high-complexity conditions, with argument generation emerging as the primary bottleneck. These findings expose critical limitations in current agents' ability to ground reasoning within messy personal context and orchestrate reliable multi-step plans. We release ASTRA-bench with a full execution environment and evaluation scripts to provide a diagnostic testbed for developing truly context-aware AI assistants.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI助手评测基准在评估智能体处理真实、复杂个人上下文与多步骤工具使用任务方面存在的不足。随着大语言模型在智能助理领域的应用日益深入，下一代AI需要能够整合海量、动态的个人数据（如邮件、日历），调用多样化的工具，并进行多步骤推理与规划。然而，现有大多数评测基准（如GTA、UltraTool、DialogTool等）往往是上下文无关、单轮交互的，或者仅孤立地评估工具使用、上下文理解或长期规划中的某一个方面，未能将**随时间演进的个人上下文**、**可交互的工具箱**与**复杂的用户意图**这三者统一在一个状态保持的、现实的评估环境中。这导致现有基准无法充分揭示智能体在必须基于用户杂乱、多源的个人上下文进行推理，并协调执行多步骤计划时所面临的独特挑战。

因此，本文的核心问题是：如何构建一个能够综合、诊断性地评估智能体在真实个人助理场景下核心能力（上下文推断与理解、工具使用的稳健推理、迭代式行动规划）的基准。为此，论文提出了ASTRA-bench基准。它通过事件驱动的流程，为四位主角构建了基于纵向生活事件的、连贯的个人上下文轨迹，并配备了可执行的工具环境。该基准包含了2,413个人工编写的对话场景，并沿指代模糊性、信息需求和功能规划需求这三个正交维度对任务复杂性进行了标注，从而能够更精准地诊断模型在不同复杂度条件下的能力瓶颈。论文的实证研究也证实了现有先进模型在高复杂度条件下性能显著下降，暴露了其在基于复杂个人上下文进行推理和规划方面的关键局限。

### Q2: 有哪些相关研究？

相关研究主要分为工具使用智能体框架和评测基准两大类。

在**工具使用智能体框架**方面，早期研究关注通过网页浏览或自监督API发现来为LLM扩充外部知识。随着核心挑战从简单的工具选择转向将工具输出整合为连贯的多步骤响应，ReAct、ToolLLM和Gorilla等框架改进了推理循环和调用准确性。这一演变正朝着使用真实上下文进行个性化任务的编排式智能体和以用户为中心的助手方向发展。

在**评测基准**方面，其发展轨迹从单轮函数调用（如API-Bank、BFCL）演进到多步骤推理任务（如AgentBench、GAIA）。这些基准拓宽了任务覆盖范围，但通常孤立地评估交互，仅使用基于结果的成功标准。近期工作如GAIA-2、ToolTalk和τ²-Bench引入了多轮目标，但仍主要依赖基于结果的评判标准。另一个前沿方向是在持久、有状态的环境中评估智能体。AppWorld提供了一个移动应用沙箱，但侧重于代码生成而非结构化函数调用。ToolSandbox和HiCUPID则向用户状态演化的有状态设置迈进，后者尤其针对个性化能力。

本文提出的ASTRA-bench与上述工作的主要区别在于其独特的整合性。如表1所示，它同时具备人类创作、轨迹可验证、技能复杂、上下文相关目标和基于个人上下文等多项特征，填补了现有空白。与以往依赖表层文本正确性或仅匹配最终答案的基准不同，ASTRA-bench通过工具痕迹和系统状态快照中的可观察证据，实现对智能体行为的细粒度诊断性评估。此外，在个人数据生成方面，本文超越了Persona-Chat、Conversation Chronicles等将交互视为独立片段的数据集，通过事件驱动的生成管道，构建了基于连续、时间演化故事线的“主角”数字足迹，为评估智能体的长期连续性提供了更真实的测试平台。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ASTRA-bench的综合性基准测试平台来解决评估智能体在复杂个人上下文环境中进行推理和行动规划能力的问题。其核心方法是创建一个模拟真实用户数字生活的、事件驱动的、纵向一致的个性化场景数据集，并配套一个支持状态交互的执行与评估环境。

整体框架分为两大部分：**个人数据与场景生成管道** 以及**评估执行环境**。

**核心方法与架构设计：**
1.  **个人数据生成**：采用基于事件驱动的分层生成管道。首先定义具有固定传记和社交网络的**主角**，作为所有数据的中心。然后，通过“生活模式”语法生成纵向的、时间连贯的**事件序列**。每个事件被结构化为包含时间、地点、行动、参与者等要素的对象。最关键的一步是**事件投影**，即通过一个由多个轻量级、任务专精的智能体（起草、批评、修订、验证）组成的级联循环，将每个高层事件转化为跨多个应用（如邮件、日历、短信）的具体、一致的**数字制品**。这种方法确保了所有个人数据都源于一个连贯的“行为先验”，而非孤立生成。

2.  **主角中心场景创作**：基于生成的个人数据，构建具体的用户-智能体交互**场景**。每个场景围绕一个在特定**参考时间**（定义“现在”）提出的**用户目标**展开，迫使智能体必须进行时间规范化处理。场景根据三个正交的复杂度轴进行精细标注：**信息复杂度**（衡量多步推理与信息合成需求）、**指代复杂度**（衡量对模糊指代进行实体解析的难度）和**功能复杂度**（衡量工具调用协调与逻辑）。此外，还引入了**错误信息**和**上下文不足**两种压力测试条件。每个场景都配有包含相关实体、推理独白和成功条件的**完整真实标注**，为评估提供坚实基础。

3.  **评估执行环境与策略**：构建了一个增强的沙盒环境，深度集成了主角的个人上下文数据，引入了全局参考时间以实现时间感知，并扩展了跨6个领域的25+个工具。评估采用**双轨制**：
    *   **可验证的规则度量**：扩展了“里程碑与雷区”框架，将其组织为有向无环图以强化逻辑依赖，并引入高分辨率相似度度量来评估信息检索准确性和目标对齐度。任何“雷区”违规都会导致总分归零。
    *   **基于LLM的评估器**：使用遵循量规的LLM法官，从任务完成度、工具使用、信息检索、对话效果和无幻觉五个维度进行评分，以捕捉更灵活、语义层面的推理质量。

**关键技术及创新点：**
*   **事件驱动的纵向数据合成**：通过主角模型和生活模式语法，生成具有长期一致性的个人数字历史，解决了以往基准测试中上下文孤立、缺乏时间演进的问题。
*   **多智能体协作的“起草-批评-修订”管道**：无需微调，通过模块化智能体的协作，高效、可控地生成高质量、跨应用一致的数字制品。
*   **多维度复杂度标注与压力测试**：通过三个复杂度轴和两种压力条件，实现对智能体能力瓶颈（如论文中指出的论据生成）的精细诊断。
*   **双轨制评估框架**：结合了严格、可验证的规则度量与灵活、语义化的LLM评估，既能精确衡量工具执行的正确性，也能综合评价推理和对话的质量，提供了更全面的性能画像。

### Q4: 论文做了哪些实验？

论文在ASTRA-bench基准上进行了全面的实验评估。实验设置上，构建了一个包含2,413个场景的基准，这些场景基于四个主角的纵向生活事件生成，并标注了指代性、功能性和信息性三个维度的复杂性。评估在一个完整的执行环境中进行，使用确定性里程碑指标来分解性能。

评估的数据集即ASTRA-bench本身。对比方法涵盖了前沿的专有模型和领先的开源模型，具体包括：专有模型GPT-o3、GPT-4.1、Claude-4.5-Opus和Claude-4.5-Haiku；开源模型DeepSeek-V3.2以及Qwen3系列（30B、30B-Instruct、235B）。

主要结果如下：
1.  **整体性能与复杂性影响**：所有模型在任务复杂性增加时均出现性能显著下降。Claude-4.5-Opus取得了最高的宏观平均分（0.9112），并在所有三个维度的高复杂性场景中表现最佳。开源模型中，DeepSeek-V3.2表现最强（宏观平均分0.9050），在低复杂性场景与专有模型相当，但在信息和功能需求增加时出现明显差距。
2.  **步骤级与任务级成功分析**：步骤级成功分解为信息检索（IR）召回率、响应生成和参数（Payload）生成。关键发现是**参数生成成为主要瓶颈**，其分数最低且方差最大（范围0.5603至0.8478），而IR召回率最强（如DeepSeek-V3.2达0.9516）。任务级成功（最终目标完成）方面，Claude-4.5-Opus和DeepSeek-V3.2在上下文问答（CQA）和实体创建两类任务中领先，其中DeepSeek-V3.2取得了最高的实体创建成功率（0.9161）。
3.  **压力测试结果**：在“上下文不足”和“错误信息”两种压力条件下，所有模型性能均大幅下降。上下文不足主要导致“执行偏差”，即模型在缺少前提时仍试图执行任务；错误信息场景则暴露了模型在自我纠正和前提验证方面的普遍不足。例如，在错误信息下，GPT-4.1的任务完成率下降了0.231，而Claude-4.5-Opus表现出较强韧性（仅下降0.027）。

### Q5: 有什么可以进一步探索的点？

本文提出的ASTRA-bench在评估工具使用智能体的推理与规划方面迈出了重要一步，但其局限性也为未来研究提供了多个探索方向。首先，基准构建依赖人工设计里程碑，成本高昂，未来可通过自动化方法（如执行轨迹对齐）从真实交互中挖掘复杂里程碑，提升可扩展性。其次，评估依赖LLM打分，可能误判未预料但有效的计划，需开发更稳健的评估器，如集成校准或免参考验证方法。此外，合成数据难以完全模拟真实场景的噪声与特异性，未来可引入带噪声的真实用户日志或更复杂的噪声生成过程，缩小现实差距。工具覆盖范围目前侧重生产力流程，未来应纳入更广泛的工具类型（如社交、创意类），并探索动态工具集的适应能力。最后，智能体在复杂条件下的性能瓶颈（如参数生成）提示需加强上下文感知与多步规划的研究，例如结合长期记忆机制或分层规划架构，以提升对混乱个人数据的推理鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了ASTRA-bench基准测试，旨在评估AI助手在复杂个人上下文中的工具使用、推理与行动规划能力。核心贡献在于构建了一个融合动态个人背景、交互式工具箱及多轮复杂用户意图的评估框架，弥补了现有基准缺乏上下文与多轮交互的不足。方法上，其通过事件驱动流程生成了2,413个基于长期生活事件的场景，并标注了指代性、功能性与信息性复杂度，采用里程碑式评分进行诊断性评估。主要结论显示，当前最先进模型在面临高复杂度任务时性能显著下降，其中参数生成和多步骤规划协调成为主要瓶颈，揭示了现有智能体在杂乱个人上下文中进行推理和可靠多步规划的严重局限性。该研究为开发真正上下文感知的AI助手提供了关键诊断工具和测试平台。
