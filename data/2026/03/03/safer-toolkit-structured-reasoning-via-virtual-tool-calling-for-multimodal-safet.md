---
title: "SaFeR-ToolKit: Structured Reasoning via Virtual Tool Calling for Multimodal Safety"
authors:
  - "Zixuan Xu"
  - "Tiancheng He"
  - "Huahui Yi"
  - "Kun Wang"
  - "Xi Chen"
  - "Gongli Xi"
  - "Qiankun Li"
  - "Kang Li"
  - "Yang Liu"
  - "Zhigang Zeng"
date: "2026-03-03"
arxiv_id: "2603.02635"
arxiv_url: "https://arxiv.org/abs/2603.02635"
pdf_url: "https://arxiv.org/pdf/2603.02635v1"
github_url: "https://github.com/Duebassx/SaFeR_ToolKit"
categories:
  - "cs.LG"
tags:
  - "Agent Safety"
  - "Tool Use"
  - "Structured Reasoning"
  - "Multimodal Agent"
  - "Agent Alignment"
  - "Agent Training"
relevance_score: 7.5
---

# SaFeR-ToolKit: Structured Reasoning via Virtual Tool Calling for Multimodal Safety

## 原始摘要

Vision-language models remain susceptible to multimodal jailbreaks and over-refusal because safety hinges on both visual evidence and user intent, while many alignment pipelines supervise only the final response. To address this, we present SaFeR-ToolKit, which formalizes safety decision-making as a checkable protocol. Concretely, a planner specifies a persona, a Perception $\to$ Reasoning $\to$ Decision tool set, and a constrained transition graph, while a responder outputs a typed key-value tool trace before the final answer. To make the protocol reliably followed in practice, we train a single policy with a three-stage curriculum (SFT $\to$ DPO $\to$ GRPO), where GRPO directly supervises tool usage beyond answer-level feedback. Our contributions are two-fold: I. Dataset. The first tool-based safety reasoning dataset, comprising 31,654 examples (SFT 6k, DPO 18.6k, GRPO 6k) plus 1k held-out evaluation. II. Experiments. On Qwen2.5-VL, SaFeR-ToolKit significantly improves Safety/Helpfulness/Reasoning Rigor on 3B (29.39/45.04/4.98 $\to$ 84.40/71.13/78.87) and 7B (53.21/52.92/19.26 $\to$ 86.34/80.79/85.34), while preserving general capabilities (3B: 58.67 $\to$ 59.21; 7B: 66.39 $\to$ 66.81). Codes are available at https://github.com/Duebassx/SaFeR_ToolKit.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态视觉语言模型在安全对齐中存在的核心问题：模型在面对对抗性输入时容易产生“越狱”行为（即生成不安全内容），而过度强调安全又会导致“过度拒绝”问题（即错误拒绝良性请求）。研究背景在于，随着视觉语言模型从实验室走向实际部署，其决策可能带来真实危害，而现有的安全对齐方法（如SFT、DPO、RLHF等）大多仅在最终响应层面进行优化，缺乏对安全决策过程的显式结构化监督。现有方法的不足在于，它们将安全决策视为一个隐式的、不可检查的过程，无法有效分离视觉证据与用户意图，导致模型在遇到包含对抗性提示的图像时，可能忽略视觉证据而生成不安全输出，反之亦然。

本文要解决的核心问题是：如何设计一种可检查、可追溯的结构化安全推理框架，使模型的安全决策过程变得透明、可审计。为此，论文提出了SaFeR-ToolKit，将安全决策形式化为一个可验证的协议，通过虚拟工具调用（感知→推理→决策）生成结构化的工具使用轨迹，从而将安全目标从最终答案层面转移到可审计的决策过程层面。该方法通过三阶段课程学习（SFT→DPO→GRPO）训练单一策略，其中GRPO阶段直接监督工具使用，超越了仅基于答案的反馈，最终实现了安全性与有用性的更好平衡，并保持了模型的通用能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：多模态大语言模型（MLLMs）和安全对齐。

在多模态大语言模型方面，近期研究正从指令调优快速转向以推理为中心的训练和解码策略，例如OpenAI o1和DeepSeek-R1等模型，它们通过扩展测试时计算和利用基于验证的训练信号，实现了在视觉上下文中的多步演绎和思维链推理，从而在视觉感知、数学推理等基准上取得显著进展。然而，这种增强的认知能力也扩大了攻击面，复杂的思维过程可能被用来隐藏有害意图。

在安全对齐方面，传统防御方法主要是结果导向的，依赖于通过监督微调（SFT）和偏好优化（DPO）进行的训练阶段对齐，或推理时干预。这些方法将安全视为黑箱，限制了可解释性和可审计性。因此，近期工作开始转向推理感知的安全方法，通过监督中间步骤来显式进行风险分析，例如使用监督推理数据集或强化学习。但这些方法通常缺乏对推理过程的明确结构或严格控制。

本文提出的SaFeR-ToolKit与上述工作密切相关，但存在关键区别。它通过将安全决策形式化为一个可检查的协议，引入了明确的结构化：规划器选择感知、推理、决策三层虚拟工具并遵循约束转移图，响应器在最终答案前输出类型化的键值工具轨迹。与主要依赖答案级反馈的现有方法不同，本文采用包含GRPO（直接监督工具使用）的三阶段课程训练单一策略，从而实现了对推理过程更严格、可验证的控制和更高的可审计性。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为SaFeR-ToolKit的结构化虚拟工具调用框架来解决多模态安全对齐问题。其核心思想是将安全决策过程形式化为一个可检查的协议，迫使模型在生成最终答案前，必须执行一个结构化的、分阶段的推理过程，从而提升其安全性和推理严谨性。

**整体框架与主要模块**：
该框架包含两个核心组件：**规划器（Planner）** 和**响应器（Responder）**。规划器根据输入（图像和问题）评估风险类别，并确定一个配置三元组：**角色（Persona）**、**工具子集（Tool Subset）** 和**拓扑结构（Topology）**。角色控制回答风格，工具子集定义了可用的虚拟工具，而拓扑结构（如线性、树状、网状、防护盾、循环）则约束了工具调用的顺序和路径。响应器在规划器生成的系统提示指导下，生成一个结构化的**工具轨迹（Tool Trace）**，然后基于此轨迹生成最终答案。

**关键技术**：
1.  **虚拟工具调用与结构化轨迹**：模型不直接调用外部API，而是使用一套文本定义的“虚拟工具”进行内部推理。工具库被划分为**感知（Perception）、推理（Reasoning）、决策（Decision）** 三个阶段。每个工具调用会生成一个文本观察结果，所有调用按顺序构成一个类型化的键值对轨迹。这种设计将模型的“思考过程”显式化、结构化，便于检查和监督。
2.  **三阶段课程学习训练策略**：这是方法的核心创新点。作者训练一个单一的策略模型，但分三个阶段进行：
    *   **监督微调（SFT）**：学习基本的工具使用和轨迹格式，生成参考轨迹和答案。
    *   **直接偏好优化（DPO）**：通过对比学习优化工具的选择和执行。正例是高质量的轨迹-答案对，负例是通过系统扰动生成的、包含工具选择或执行错误的低质量对。这教会模型区分好坏工具使用。
    *   **分组相对策略优化（GRPO）**：这是关键创新，直接对工具使用进行策略级监督。模型对同一输入进行多次“试运行”（rollout），生成多个候选轨迹-答案对。通过一个复合奖励函数（评估格式合规性、工具调用深度和语义正确性）计算每个候选的奖励，并使用组内中心化优势函数进行优化。这使得模型能根据具体输入自适应地调整工具使用策略（如调用哪些工具、调用深度和顺序），而不仅仅是模仿固定轨迹，从而实现了更灵活、更深度的推理。

**创新点**：
主要创新在于将安全对齐问题转化为一个**结构化、可审计的推理协议**，并设计了**GRPO训练阶段**来直接优化策略级的工具调用行为。与仅监督最终答案的传统方法不同，该方法通过强制模型生成中间工具轨迹，并对该轨迹进行多层次监督（SFT、DPO、GRPO），确保了安全决策基于视觉证据和用户意图的严谨推理过程，从而有效抵御越狱攻击和过度拒绝问题。实验表明，该方法在多个基准测试中显著提升了模型的安全性、帮助性和推理严谨性，同时保持了通用能力。

### Q4: 论文做了哪些实验？

论文实验主要围绕四个研究问题展开，评估SaFeR-ToolKit在安全对齐和通用能力上的表现。

**实验设置**：基于Qwen2.5-VL-3B/7B模型，采用三阶段训练流程：监督微调（SFT）、直接偏好优化（DPO）和组相对策略优化（GRPO）。具体参数如SFT学习率1e-5，DPO学习率5e-7，GRPO学习率1e-6，使用8张NVIDIA A800 GPU进行训练。

**数据集与基准测试**：评估分为两部分。1) **安全对齐**：使用BeaverTails-V、MM-SafetyBench、MSSBench、SPA-VL及自建的ToolkitBench，通过GPT-5-mini作为评判模型，对回答的安全性（Safety，范围[-3,3]）、帮助性（Helpfulness，[0,3]）和推理严谨性（Reasoning Rigor，[0,3]）进行评分，并报告获得最高分的样本百分比。2) **通用能力**：使用MathVista、MMMU、MMStar、MM-Vet和POPE基准，报告准确率。

**对比方法**：与三类安全对齐方法比较：1) 推理时防御（如ECSO、SIA）；2) 基于SFT的对齐（如TIS、VLGuard）；3) 基于偏好/强化学习的对齐（如SPA-VL、SaFeR-VLM）。同时，还比较了不同训练阶段组合（如+SFT、+SFT+DPO、+SFT+GRPO、+SFT+DPO+GRPO）的效果。

**主要结果与关键指标**：
1. **安全对齐性能显著提升**：在3B模型上，完整方法将Safety/Helpfulness/Reasoning Rigor从基线的29.39/45.04/4.98提升至84.40/71.13/78.87；在7B模型上，从53.21/52.92/19.26提升至86.34/80.79/85.34。均大幅优于对比方法，例如在3B规模上，Safety比TIS高11.85个百分点，比SaFeR-VLM高15.53个百分点。
2. **通用能力得以保持**：完整方法在五个通用基准上的平均准确率，3B模型从58.67%微升至59.21%，7B模型从66.39%微升至66.81%，性能下降远小于其他安全对齐方法（如TIS导致3B模型平均下降10.48%）。
3. **渐进式训练课程有效**：实验表明，DPO和GRPO阶段均带来增量收益。例如在3B模型上，DPO阶段在SFT基础上将平均Safety/Helpfulness/Reasoning Rigor提升了4.86/7.62/6.62；GRPO阶段进一步提升了13.63/13.13/14.29。
4. **工具架构与奖励设计贡献**：消融实验显示，完整的感知（P）+推理（R）+决策（D）三层工具组合效果最佳，在平均Safety上达到65.91%。GRPO奖励中结合格式奖励、语义奖励和工具使用质量奖励（$s_{tool}$）能带来最佳性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的结构化安全推理框架在提升模型安全性和可解释性方面成效显著，但仍有进一步探索的空间。其局限性在于：首先，当前工具集和状态转移图是预定义且相对固定的，可能难以覆盖复杂多变的真实世界安全场景，未来可研究如何让模型动态生成或调整推理协议。其次，训练依赖于大规模人工标注的工具使用轨迹数据，成本高昂；未来可探索通过合成数据或强化学习来自主学习工具调用策略。此外，该方法目前主要针对视觉-语言模型，其思想如何泛化到纯文本或多模态具身智能等更广泛场景，值得研究。结合个人见解，可能的改进方向包括：引入不确定性量化机制，让模型在推理过程中评估自身判断的置信度，并在低置信度时主动寻求人类反馈；或将协议图学习与端到端训练结合，使推理结构既能保持可检查性，又能自适应优化。最后，如何将这种结构化安全推理与模型的内在价值观对齐更深度结合，而非仅作为外部“插件”，也是一个重要的未来课题。

### Q6: 总结一下论文的主要内容

该论文针对视觉语言模型在安全对齐中存在的多模态越狱和过度拒绝问题，提出了一种结构化安全推理框架SaFeR-ToolKit。其核心贡献是将安全决策过程形式化为一个可检查的协议，通过虚拟工具调用实现从感知、推理到决策的透明化步骤。方法上，系统包含规划器（定义角色、工具集和约束状态图）和响应器（在最终答案前输出类型化键值对工具轨迹）。为确保协议被可靠遵循，作者采用三阶段课程训练单一策略：监督微调、直接偏好优化以及专门监督工具使用的分组相对策略优化。实验表明，该方法在Qwen2.5-VL模型上显著提升了安全性、帮助性和推理严谨性，同时保持了模型的通用能力。论文的意义在于首次构建了基于工具的安全推理数据集，并通过结构化协议和针对性训练，为实现更可靠、可解释的多模态模型安全对齐提供了新路径。
