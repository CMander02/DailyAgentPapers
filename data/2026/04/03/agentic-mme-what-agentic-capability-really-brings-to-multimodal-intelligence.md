---
title: "Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?"
authors:
  - "Qianshan Wei"
  - "Yishan Yang"
  - "Siyi Wang"
  - "Jinglin Chen"
  - "Binyu Wang"
  - "Jiaming Wang"
  - "Shuang Chen"
  - "Zechen Li"
  - "Yang Shi"
  - "Yuqi Tang"
  - "Weining Wang"
  - "Yi Yu"
  - "Chaoyou Fu"
  - "Qi Li"
  - "Yi-Fan Zhang"
date: "2026-04-03"
arxiv_id: "2604.03016"
arxiv_url: "https://arxiv.org/abs/2604.03016"
pdf_url: "https://arxiv.org/pdf/2604.03016v1"
categories:
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "多模态Agent"
  - "工具使用"
  - "过程验证"
  - "基准构建"
relevance_score: 9.0
---

# Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?

## 原始摘要

Multimodal Large Language Models (MLLMs) are evolving from passive observers into active agents, solving problems through Visual Expansion (invoking visual tools) and Knowledge Expansion (open-web search). However, existing evaluations fall short: they lack flexible tool integration, test visual and search tools separately, and evaluate primarily by final answers. Consequently, they cannot verify if tools were actually invoked, applied correctly, or used efficiently. To address this, we introduce Agentic-MME, a process-verified benchmark for Multimodal Agentic Capabilities. It contains 418 real-world tasks across 6 domains and 3 difficulty levels to evaluate capability synergy, featuring over 2,000 stepwise checkpoints that average 10+ person-hours of manual annotation per task. Each task includes a unified evaluation framework supporting sandboxed code and APIs, alongside a human reference trajectory annotated with stepwise checkpoints along dual-axis: S-axis and V-axis. To enable true process-level verification, we audit fine-grained intermediate states rather than just final answers, and quantify efficiency via an overthinking metric relative to human trajectories. Experimental results show the best model, Gemini3-pro, achieves 56.3% overall accuracy, which falls significantly to 23.0% on Level-3 tasks, underscoring the difficulty of real-world multimodal agentic problem solving.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型（MLLMs）在向主动智能体（Agent）演进过程中，其能力评估体系存在的不足与空白。研究背景是MLLMs正从被动观察者转变为主动调查者，通过视觉扩展（调用视觉工具）和知识扩展（开放网络搜索）来解决问题，即发展“多模态智能体能力”。然而，现有的评估方法存在三大缺陷：首先，工具集成缺乏灵活性和全面性，往往将视觉工具和搜索工具分开测试，没有统一的框架支持智能体在它们之间流畅切换；其次，未能深入探究视觉扩展与知识扩展之间的协同效应，缺乏需要两者交织配合才能解决的现实任务；最后，也是最核心的不足，是缺乏严格的过程验证。现有评估主要关注最终答案的正确性，无法判断工具是否被实际调用、是否正确应用、或是否高效使用，导致模型失败的根本原因（如感知局限、工具调用缺失、执行错误或冗余尝试）被混淆，难以诊断多模态智能的真正瓶颈。

因此，本文要解决的核心问题是：如何构建一个能够对多模态智能体能力进行**过程验证**的综合性评估基准。为此，论文提出了Agentic-MME基准。该基准旨在通过一个支持视觉与搜索工具统一调用的框架，设计需要能力协同的现实任务，并引入包含大量人工标注的逐步检查点和参考轨迹，来对智能体在解决问题过程中的**中间状态和行为**进行细粒度审计，从而实现真正的过程级评估，精准定位模型在复杂多模态推理工作流中的能力缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：评测基准类、方法类和应用类。

在**评测基准类**工作中，现有研究多聚焦于单一能力评估。例如，GTA、m&m's、TIR-Bench和VisToolBench等基准专门评估视觉工具使用能力，而MMSearch和MMSearch-Plus则专注于评估开放网络搜索能力。这些基准通常将视觉扩展与知识扩展视为独立模块，缺乏对两者协同工作的综合测试。少数基准如MM-BrowseComp和GAIA2开始关注过程验证或效率指标，但往往不支持统一的代码与工具调用评估框架，或未明确划分任务难度等级。AdaptMMBench虽支持过程验证和难度分级，但其核心仍是视觉工具，未将开放网络搜索作为核心能力进行整合评估。

本文提出的Agentic-MME与上述工作的主要区别在于其**综合性、过程验证性和统一性**。首先，它首次在一个统一的工作流中**深度融合了视觉工具使用与开放网络搜索**，并专门设计了需要两者协同解决的任务（尤其是Level-3），以评估真正的多模态智能体能力。其次，它通过超过2000个人工标注的逐步检查点（S轴和V轴）实现了**严格的、细粒度的过程验证**，超越了仅依赖最终答案的评估方式，能诊断工具调用、执行正确性和效率等具体失败模式。最后，它提供了一个**统一的评估框架**，同时支持沙盒代码执行和函数调用API，并通过AST追踪器确保不同交互模式下的评分一致性，这是现有基准普遍缺乏的。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Agentic-MME的、支持过程验证的基准测试来解决现有评估方法在衡量多模态智能体能力方面的不足。其核心方法是设计一个包含真实世界任务、统一工具接口和细粒度过程监督的评估框架。

整体框架包括任务设计、数据构建、评估协议和指标计算。主要模块/组件如下：
1.  **任务与数据集**：包含418个任务，覆盖6个领域和3个难度等级。任务设计强调视觉扩展（调用13种视觉操作工具）与知识扩展（4种开放网络检索工具）的协同，并强制要求主动的视觉操作（如裁剪、旋转、增强）来获取隐藏证据。
2.  **数据构建与标注流程**：采用严格控制的协议确保标注质量。
    *   **图像来源与任务设计**：从开放网络收集高分辨率、视觉复杂的图像，并采用“模型在环反向起草”机制。标注者先让先进模型（如Gemini 3 Pro）被动描述原图，然后针对模型忽略或幻觉的视觉细节，通过操作工具提取证据，并验证模型能正确感知处理后的图像，从而确保主动视觉操作是解决问题的前提。
    *   **细粒度逐步标注**：不仅标注最终答案，还为每个参考解决路径的步骤详细标注：行动意图的自然语言描述、所需的具体工具或Python操作、用于自动化评估的结构化真值、处理后的中间视觉产物及其验证问题、以及多跳搜索所需的每一步关键词、已验证URL和预期答案。
    *   **答案标准化与验证**：通过提示指令约束输出格式，使最终答案评分可确定且支持正则表达式匹配。每个实例还需经过严格的人工共识审核和“逐步预言引导”的模型验证，确保任务逻辑合理且当前模型在遵循正确路径时可解决。
3.  **评估与度量**：
    *   **统一工具接口与执行跟踪**：评估框架支持通过函数接口进行原子工具调用，或在沙盒中执行自由形式的代码。通过严格的产物协议和基于AST的代码跟踪，将不同交互模式归一化为统一、可审计的事件流，确保跨模态评估的一致性。
    *   **过程级验证指标**：超越最终答案准确率（Acc），引入基于逐步检查点的过程感知和效率指标。核心创新在于将验证轴（V-axis）解耦为`V_tool`（代理是否在正确步骤启动了所需的视觉工具）和`V_true`（生成的中间视觉产物是否真正包含所需证据），从而进行更精细的诊断。效率方面，引入“过度思考”（Overthink）指标，根据代理交互步骤数相对于人类最小轨迹的冗余程度进行惩罚。

创新点在于：首次提出了一个**过程验证**的多模态智能体能力基准，通过超过2000个细粒度检查点实现对工具调用正确性、证据提取有效性和使用效率的量化评估；设计了**强制协同**的任务场景，特别是Level-3任务要求视觉操作与网络搜索进行多轮、交织的交互与交叉验证；以及采用了**模型在环反向起草**和**逐步预言引导验证**的数据构建方法，确保了任务的必要性和可解性。

### Q4: 论文做了哪些实验？

论文在自建的Agentic-MME基准上进行了全面的实验评估。实验设置上，评估了开源和闭源两大类多模态模型，包括Thyme-rl、Deepeyesv2、Qwen3-VL系列、Gemini3系列、Kimi-k2.5、GPT-5.2和Qwen3.5-plus等。每个模型在两种工具交互模式下测试：代码生成模式（Gen，编写沙盒Python代码进行视觉转换）和原子模式（Atm，通过结构化函数调用API交互）。评估协议采用过程级验证，使用MLLM-as-a-Judge方法（主评估模型为gpt-4o-mini）来审核细粒度的中间状态（如视觉伪影$V_{true}$和搜索过程），而非仅看最终答案。

数据集/基准测试为论文提出的Agentic-MME，包含418个现实世界任务，覆盖6个领域和3个难度等级（Level 1-3），并包含超过2000个人工标注的逐步检查点。

主要结果和关键指标如下：
1.  **整体性能与人类差距**：最佳模型Gemini 3-pro（Atm模式）整体准确率（Acc）为56.3%，远低于人类参考性能（93.8%）。在最高难度Level-3上，其准确率骤降至33.3%（人类为82.3%），凸显了复杂任务对现有智能体的挑战。
2.  **闭源 vs. 开源模型**：闭源模型（如Gemini、GPT系列）在所有难度级别上均显著优于开源模型。在Level-3上，差距尤为明显，例如Qwen3-VL-235B（Atm）准确率为10.1%，而Thyme-rl（Atm）仅为2.5%。开源模型在搜索规划（S轴得分低）和可靠工具执行方面存在明显短板。
3.  **交互模式对比**：原子模式（Atm）在大多数情况下优于或持平代码生成模式（Gen）。例如，Gemini 3-pro在Atm模式下整体准确率（56.3%）高于Gen模式（49.5%）。过程指标显示，一些模型在Gen模式下很少生成有效的图像处理代码（如GPT-5.2的$V_{tool}$值极低），导致性能不佳。
4.  **工具使用有效性**：部分模型存在“过度调用但结果错误”的问题，例如Thyme-rl（Gen, L1）的$V_{tool}$高达63.3，但$V_{true}$仅13.0，表明其工具参数化或执行不可靠。
5.  **基准有效性验证**：通过消融实验验证了Agentic-MME任务必须依赖视觉信息（移除图像后准确率接近零）且需要主动使用工具（完整工具访问的性能优于仅感知、仅图像或仅搜索的设置）。特别是在Level-3任务上，视觉与知识扩展能力的协同效应显著，结合使用两种工具带来的性能提升远超单独使用之和。
6.  **标注质量验证**：通过向模型提供人工标注的参考轨迹（如真实中间视觉伪影和逐步描述）作为引导，模型性能得到一致提升，验证了标注的高质量和有效性。但即使有完美蓝图，模型在Level-3上的性能仍未饱和，表明自主执行仍极具挑战性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来研究可从以下几个方向深入探索：

1. **提升多步规划与工具执行的可靠性**：实验表明，模型在复杂任务（Level-3）上表现显著下降，与人类差距巨大（最佳模型33.3% vs 人类82.3%）。未来需设计更鲁棒的规划机制，例如引入强化学习或反思机制，让模型能动态调整工具调用策略，避免错误累积。

2. **弥合开源与闭源模型的差距**：开源模型在搜索规划和工具参数化上明显落后（如S轴得分极低）。未来可探索更高效的指令微调或模仿学习方案，利用高质量的人类轨迹数据（如论文中的stepwise checkpoints）提升开源模型的推理与工具组合能力。

3. **平衡代码生成与结构化API的优劣**：虽然结构化API（Atomic模式）更可靠，但代码生成（Gen模式）具有灵活组合的潜力。未来可研究混合范式，例如让模型在API框架下生成可验证的代码片段，或开发“代码编译为API”的中间层，兼顾可靠性与灵活性。

4. **优化工具调用效率与精准性**：模型常出现“过度调用但结果错误”的问题（如Thyme-rl的V_tool与V_true差距大）。未来可引入成本感知机制，让模型学习在精度与效率间权衡，并通过更细粒度的反馈（如过程检查点）改进工具参数化能力。

5. **扩展多模态智能体的泛化场景**：当前任务集中在6个领域，未来需涵盖更多元化的现实场景（如动态环境、多用户协作），并探索工具库的动态扩展机制，使智能体能自主适应新工具。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型向主动智能体演进时缺乏有效评估标准的问题，提出了首个过程验证的基准Agentic-MME。现有评测仅关注最终答案，无法检验工具调用、使用正确性和效率，且视觉与搜索工具测试分离。为此，作者构建了包含418个真实世界任务的基准，涵盖6个领域和3个难度等级，重点评估能力协同；每个任务均包含逐步检查点（总计超2000个）和人工标注的参考轨迹，支持沙盒代码与API的统一评估框架。其核心方法在于通过双轴（S轴与V轴）对中间状态进行细粒度审计，而非仅看最终输出，并引入相对于人类轨迹的“过度思考”指标量化效率。实验表明，最佳模型Gemini3-pro总体准确率为56.3%，但在最高难度任务上骤降至23.0%，揭示了当前多模态智能体解决复杂现实问题的能力仍严重不足。该工作的意义在于推动了多模态智能体评估从结果导向转向过程验证，为未来模型的能力协同与效率优化提供了重要基准。
