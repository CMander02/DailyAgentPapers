---
title: "Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning"
authors:
  - "Yucheng Wang"
  - "Yifan Hou"
  - "Aydin Javadov"
  - "Mubashara Akhtar"
  - "Mrinmaya Sachan"
date: "2025-09-28"
arxiv_id: "2509.23744"
arxiv_url: "https://arxiv.org/abs/2509.23744"
pdf_url: "https://arxiv.org/pdf/2509.23744v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多模态大语言模型"
  - "多模态推理"
  - "Agent评测/基准"
  - "模型内部机制分析"
  - "任务分解"
  - "融合瓶颈"
relevance_score: 6.5
---

# Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning

## 原始摘要

Multimodal large language models (MLLMs) promise enhanced reasoning by integrating diverse inputs such as text, vision, and audio. Yet cross-modal reasoning remains underexplored, with conflicting reports on whether added modalities help or harm performance. These inconsistencies stem from a lack of controlled evaluation frameworks and analysis of models' internals to isolate when and why modality interactions support or undermine reasoning. We address this gap through a logic-grounded evaluation framework that categorizes multimodal reasoning into six interaction patterns, varying how facts are distributed across modalities and logically combined. Empirically, additional modalities enhance reasoning only when they provide independent and sufficient reasoning paths, while redundant or chained entailment support often hurts performance. Moreover, reasoning degrades in three systematic ways: weaker modalities drag down overall performance, conflicts bias preference toward certain modalities, and joint signals from different modalities fail to be integrated effectively. Therefore, we identify two core failures: task-composition bottleneck, where recognition and reasoning cannot be jointly executed in one pass, and fusion bottleneck, where early integration introduces bias. For further investigation, we find that attention patterns fail to encode fact usefulness, but a simple two-step prompting (recognize then reason) restores performance, confirming the task-composition bottleneck. Moreover, modality identity remains recoverable in early layers, and softening attention in early fusion improves reasoning, highlighting biased fusion as another failure mode. Overall, our findings show that integration, not perception, is the main barrier to multimodal reasoning, suggesting composition-aware training and early fusion control as promising directions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地探究多模态大语言模型（MLLMs）在跨模态推理中的核心瓶颈问题。研究背景是，尽管MLLMs通过整合文本、视觉和音频等多模态信息，有望实现比单模态系统更强的推理能力，但现有研究关于增加模态是否真正有益于推理的结论相互矛盾。这些不一致源于缺乏受控的评估框架以及对模型内部机制的分析，导致无法明确在何种条件下模态交互会支持或损害推理。

现有方法的不足主要体现在两方面：首先，大多数评估将MLLMs视为黑箱，只关注外部性能，而缺乏对其内部如何编码模态身份、评估证据相关性或执行跨模态融合的深入理解；其次，当前MLLMs的训练通常侧重于感知对齐（如配对监督、对比学习），这强化了浅层关联，而非促进深度的认知组合与推理，导致模型在需要灵活整合多模态信息进行推理时表现不佳。

本文要解决的核心问题是：在多模态推理中，增加模态何时以及为何会帮助或损害性能？其根本瓶颈是什么？为此，论文提出了一个基于逻辑的评估框架，将多模态推理归纳为六种交互模式（如等价、替代、蕴含、独立、矛盾、互补），通过控制事实在不同模态中的分布及其逻辑组合方式，进行系统性评估。研究发现，性能下降并非源于感知缺陷，而是源于两个核心瓶颈：1) **任务组合瓶颈**：模型难以在单步中同时执行跨模态的“识别”与“推理”；2) **融合瓶颈**：早期的跨模态融合会引入偏见，导致模型无法有效加权和整合异构信息。论文通过内部注意力分析和干预实验（如两步提示、软化早期注意力）验证了这些瓶颈，并指出未来需要关注组合感知的训练和早期融合控制，以使多模态真正成为推理的助力而非干扰源。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和理论分析类。

在**方法类**研究中，现有工作主要聚焦于提升多模态大语言模型（MLLMs）的感知能力，例如通过改进视觉编码器或跨模态对齐来增强模型对图像、音频等信息的理解。本文则指出，当前的核心瓶颈并非感知，而是**模态间的整合与推理过程**。本文提出的“两步提示法”（先识别后推理）是对现有端到端推理方法的一种补充和诊断。

在**评测类**研究中，以往的多模态基准测试（如VQA、MMLU）通常混合了感知与推理，难以孤立地评估模态交互对纯逻辑推理的影响。本文构建了一个**受控的逻辑推理评估框架**，通过六种明确的模态交互模式（如等价、互补、矛盾等），系统性地分离了信息分布与整合效果，弥补了现有评测在因果分析上的不足。

在**理论分析类**研究中，已有工作对多模态融合的机制（如早期融合与晚期融合）进行了探索，但对其如何影响推理性能缺乏深入的系统性分析。本文通过分析模型内部注意力模式，揭示了**任务组合瓶颈**（识别与推理无法一步完成）和**融合瓶颈**（早期融合引入偏差）两大核心失败模式，为理解模型内部工作机制提供了新的实证依据。

### Q3: 论文如何解决这个问题？

论文通过构建一个逻辑驱动的评估框架来系统性地诊断多模态推理中的核心瓶颈，并提出了相应的解决方案思路。其核心方法是设计一个受控的合成数据集，将多模态推理分解为六种规范的交互模式，以精确分析模态间信息如何组合与整合。

整体框架包含三个关键部分：首先，定义并生成六种交互模式的数据，包括等价、替代、蕴含、独立、矛盾、互补，这些模式系统地改变了事实在不同模态间的分布和逻辑组合方式。其次，在统一的实验设置下评估多个先进的多模态大语言模型，使用相同的提示模板、解码策略和评估指标（多项选择题准确率）。最后，通过分析模型在不同交互模式下的性能变化，并结合对模型内部注意力模式等的探查，识别出根本性的失败模式。

主要模块包括：1）**逻辑驱动的评估框架**：这是方法论的核心创新，它超越了传统基准测试，能够隔离并量化不同模态交互对推理的影响。2）**受控合成数据生成**：确保每个测试实例的逻辑结构清晰，变量可控，从而可以直接比较单模态与多模态条件下的性能差异。3）**多模型对比分析**：选取了Baichuan、Qwen、MiniCPM、Phi-4等具有不同架构特点的模型，确保了发现的普适性。4）**内部机制诊断**：通过分析注意力模式以及进行干预性实验（如两步提示），来验证假设的瓶颈。

关键技术发现与创新点在于：论文识别出两个根本性瓶颈。一是**任务组合瓶颈**：模型在单模态下能很好地进行事实识别和逻辑推理，但当需要跨模态同时执行识别与推理时，性能显著下降。这通过“先识别再推理”的两步提示法能恢复性能得到证实。二是**融合瓶颈**：模型在早期融合不同模态信息时会产生偏见，表现为对某些模态的偏好（即使该模态并非最强），以及无法有效整合互补的弱信号。早期层的表征分析显示模态身份信息仍然残留，而软化早期注意力能改善推理，这指向了早期融合控制是一个有前景的方向。

综上所述，论文的解决方案并非提出一个全新的模型架构，而是通过精细的归因分析，明确指出当前多模态推理的主要障碍在于“整合”而非“感知”，并为未来的模型设计（如具有组合意识的训练、早期融合控制）提供了清晰的理论和实证指导。

### Q4: 论文做了哪些实验？

论文实验围绕一个逻辑驱动的评估框架展开，系统评估了多模态大语言模型在六种交互模式下的推理能力。

**实验设置**：评估了四个开源MLLMs：Baichuan-Omni-1.5d (7B)、Qwen2.5-Omni (7B)、MiniCPM-o-2.6 (8B) 和 Phi-4 Multimodal (5.6B)。采用统一的提示格式，包含系统指令、随机顺序呈现的事实块（文本、视觉、音频）、文本推理规则和一个四选一问题。解码使用贪婪采样以确保输出稳定，并从响应中自动提取最终答案。主要评估指标为准确率，随机基线为25%。每个实验条件在1000个合成实例上进行。

**数据集/基准测试**：主要使用合成的逻辑推理数据集，其中事实按特定模式分布在多模态中。此外，还在真实世界的视觉-文本基准IsoBench上对“等价”交互模式进行了验证性实验。

**对比方法与主要结果**：实验通过对比多模态设置与单模态基线（仅文本、仅视觉或仅音频包含决定性事实）来评估多模态的价值。核心发现如下：
1.  **多模态何时有益**：在“替代”模式（各模态提供独立且充分的推理路径）下，所有模型均表现提升（平均提升：视觉+12.7%，音频+14.8%，文本+1.7%）。在“等价”模式（冗余事实）下，若原模态为弱模态（视觉/音频）则有增益（视觉+9.7%，音频+10.9%），若原模态为强模态（文本）则性能下降（-5.7%）。在“蕴涵”模式（推理链跨模态分割）下，所有模型性能均大幅下降（视觉-7.8%，音频-7.1%，文本-12.8%）。
2.  **多模态何时有害**：在“独立”模式（一个模态含决定性事实，其他为干扰项）下，多模态准确率（70.29%）远低于纯文本基线（94.45%），但高于纯视觉（65.3%）或纯音频（74.7%）基线，表明弱模态会引入噪声。在“互补”模式（每个模态提供一个必要事实）下，多模态准确率（52.0%）甚至低于任何单模态条件（视觉73.2%，音频82.4%，文本94.6%），揭示了跨模态组合瓶颈。在“矛盾”模式（各模态指向不同答案）下，模型显示出对特定模态的偏好（如Baichuan偏好视觉49.0%，Qwen偏好音频44.6%），这种偏好偏差与单模态性能优势并不一致。

**关键数据指标**：论文提供了详细的准确率百分比及相对于单模态基线的变化值（Δ）。例如，在“互补”交互中，Qwen的多模态准确率为49.9%，较其视觉、音频、文本单模态基线分别下降37.6、48.9、48.9个百分点。这些量化结果系统地揭示了性能偏差、偏好偏差和融合偏差三种失败模式。

### Q5: 有什么可以进一步探索的点？

该论文揭示了多模态推理中两个核心瓶颈：任务组合瓶颈和融合瓶颈。基于此，未来研究可从以下几个方向深入探索：

首先，针对任务组合瓶颈，论文发现简单的两步提示（先识别后推理）能显著提升性能，这表明当前模型难以在单次前向传递中协同执行感知与推理。未来的工作可以探索更先进的架构设计，例如开发显式的“组合感知”训练机制，或在模型内部引入可学习的子模块来专门处理跨模态的任务分解与协调，而非依赖外部提示。

其次，对于融合瓶颈，论文指出早期融合会引入偏见，且模态身份在早期层中仍可恢复。一个重要的改进方向是设计动态或自适应的融合策略。例如，可以研究如何通过门控机制或注意力软化技术，在模型的不同层（而非固定早期层）有选择性地整合模态信息，从而减少偏见并促进更有效的信号整合。

此外，论文的评估主要基于受控的合成逻辑数据集。未来的研究需要验证这些瓶颈在更复杂、开放领域的真实多模态任务（如视觉问答、音频-文本推理）中是否同样存在，并探究其具体表现形式。同时，可以探索如何将论文中有效的干预措施（如两步提示）无缝集成到模型的端到端训练中，以实现根本性的性能提升。

最后，可以深入分析模型内部机制，例如研究注意力模式如何编码事实的有用性，并探索通过改进注意力机制或引入新的损失函数来直接优化跨模态的信息集成与推理路径选择。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型（MLLMs）在跨模态推理中性能不一致的问题，提出了一个基于逻辑的评估框架，系统分析了多模态交互如何影响推理效果。核心贡献在于揭示了当前MLLMs存在的两个根本瓶颈：任务组合瓶颈（模型难以在单次处理中同时完成识别与推理）和融合瓶颈（早期融合会引入模态偏见）。方法上，作者构建了一个包含六种交互模式的评估体系，通过控制事实在不同模态间的分布与逻辑组合进行实验。主要结论表明，仅当多模态提供独立且充分的推理路径时才能提升性能，而冗余或链式支持反而会损害结果；推理失败主要表现为弱模态拖累整体、冲突导致模态偏好以及跨模态信号整合失效。实验发现，简单的两步提示（先识别后推理）可缓解任务组合瓶颈，而软化早期融合的注意力则能减少偏见，这为未来设计组合感知的训练与早期融合控制提供了关键方向。
