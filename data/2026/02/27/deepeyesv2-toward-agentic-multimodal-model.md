---
title: "DeepEyesV2: Toward Agentic Multimodal Model"
authors:
  - "Jack Hong"
  - "Chenxiao Zhao"
  - "ChengLin Zhu"
  - "Weiheng Lu"
  - "Guohai Xu"
date: "2025-11-07"
arxiv_id: "2511.05271"
arxiv_url: "https://arxiv.org/abs/2511.05271"
pdf_url: "https://arxiv.org/pdf/2511.05271v3"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Perception & Multimodal"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen2.5-VL"
  key_technique: "two-stage training pipeline (cold-start stage and reinforcement learning stage)"
  primary_benchmark: "RealX-Bench"
---

# DeepEyesV2: Toward Agentic Multimodal Model

## 原始摘要

Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive benchmark designed to evaluate real-world multimodal reasoning, which inherently requires the integration of multiple capabilities, including perception, search, and reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative benchmarks, demonstrating its effectiveness across real-world understanding, mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2 exhibits task-adaptive tool invocation, tending to use image operations for perception tasks and numerical computations for reasoning tasks. Reinforcement learning further enables complex tool combinations and allows model to selectively invoke tools based on context. We hope our study can provide guidance for community in developing agentic multimodal models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何构建一个具备自主工具调用能力的智能体式多模态模型（Agentic Multimodal Model）这一核心问题。研究背景在于，当前的多模态大模型虽然在文本和图像理解方面表现出色，但本质上是被动的，缺乏主动调用外部工具（如代码执行环境、网络搜索）并将其无缝整合到复杂推理过程中的能力。这种能力的缺失限制了模型在需要精细感知、实时信息获取和复杂数值计算等真实世界场景中的应用效果。

现有方法存在明显不足。一方面，一些工作仅依赖单一工具，例如DeepEyes专注于通过图像裁剪实现细粒度感知，但缺乏信息检索能力；而MMSearch-R1能进行搜索，却缺少对图像的精细操作能力。另一方面，直接对现有基础模型应用强化学习来诱导工具使用行为被证明是失败的，模型无法形成稳定可靠的工具调用模式。这表明，现有方法在实现感知、搜索与推理的深度协同方面存在显著差距。

因此，本文的核心问题是系统性地探索如何构建一个真正的智能体式多模态模型。具体而言，研究聚焦于三个关键方面：1）**训练策略**：如何设计有效的训练流程（如论文提出的“冷启动+强化学习”两阶段方法）来使模型学会自主、可靠地调用和组合工具。2）**数据构建**：如何构建一个高质量、多样化且难度适中的训练数据集，确保工具的使用确实有益于问题解决。3）**模型评估**：如何建立一个全面的评估基准（如本文提出的RealX-Bench），以准确衡量模型在需要多种能力整合的真实世界多模态推理任务上的性能。通过引入DeepEyesV2模型，论文旨在为上述问题提供解决方案和实践指导。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大语言模型（MLLMs）、基于图像的思维范式以及搜索增强推理。

在多模态大语言模型方面，早期工作（如使用适配器连接视觉编码器与语言模型）和近期更强大的架构（如Qwen2.5-VL、LLaVA-OneVision）主要专注于提升视觉-语言对齐和感知任务性能，但它们本质上是**被动**的，缺乏主动调用外部工具的能力。本文的DeepEyesV2则旨在构建一个能**主动调用并整合工具**的智能体式多模态模型，这是核心区别。

在“基于图像的思维”范式方面，相关工作（如o3、PyVision、Thyme）探索了让模型通过迭代图像操作（如区域裁剪、代码执行）进行推理。多数采用“冷启动+强化学习”的两阶段训练。本文虽也采用两阶段管道，但指出**仅靠强化学习无法诱导出可靠的工具使用行为**，这构成了其方法论的动机。此外，现有工作工具集通常局限于图像操作，而DeepEyesV2整合了更广泛的工具（如代码执行、网络搜索），以处理知识密集型任务。

在搜索增强推理方面，早期检索增强生成（RAG）方法和近期在线搜索研究致力于弥补模型的知识局限。本文将这些**动态知识获取能力**视为智能体模型的关键组成部分，并将其与感知、工具调用能力进行整合，以应对更复杂的现实世界推理任务。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段训练流程来解决智能体多模态模型稳健使用工具的问题，核心方法包括冷启动阶段和强化学习阶段，整体架构设计为迭代式的“推理-工具调用-集成”循环。

**整体框架与主要模块**：DeepEyesV2 是一个智能体多模态模型，其核心架构是一个集成了工具调用的推理循环。给定图像和用户查询后，模型首先生成初始推理计划，并明确判断是否需要调用外部工具。如需工具，则生成可执行的 Python 代码或发起网络搜索查询。代码在沙箱环境中执行，可输出处理后的图像、数值、数组或日志；网络搜索通过 SerpAPI 进行，返回视觉匹配或文本相关的网页结果。所有工具输出被转化为观察结果并追加到模型上下文中，模型基于此进行进一步思考，并可计划新一轮的工具调用，如此迭代直至生成最终答案。该框架支持动态选择、组合和使用工具。

**关键技术**：
1.  **两阶段训练策略**：研究发现，仅靠直接强化学习会导致模型工具使用行为退化（如生成无意义的占位代码）。因此，论文提出先进行**冷启动监督微调**，使用高质量轨迹数据（通过提示 Gemini、GPT-4 等先进模型生成包含显式工具调用的正确推理链获得）来建立模型基本的工具使用模式。在此基础上，再进行**强化学习**，将模型置于交互环境中，通过稀疏的结果驱动奖励（基于答案准确性和输出格式），进一步优化工具调用的效率、灵活性和上下文适应性。
2.  **高质量数据集构建**：为支持训练，论文精心策划了数据集，遵循四大原则：任务和图像分布多样；问题可验证且为结构化开放格式；具有一定难度（过滤基础模型易解决的简单问题）；**强调工具使用的益处**，特别保留那些使用工具才能正确解答的案例用于强化学习。数据涵盖感知、推理和搜索三大类别，并包含长链思维推理数据。
3.  **任务自适应的工具调用**：经过训练后，DeepEyesV2 展现出根据任务类型自适应调用工具的能力，例如在感知任务中倾向于使用图像操作，在推理任务中倾向于进行数值计算。强化学习阶段进一步使模型能够进行复杂的工具组合，并能根据上下文选择性调用工具。

**创新点**：
1.  **揭示了直接强化学习在诱导稳健工具使用行为上的局限性**，并通过实验（如奖励黑客现象）论证了冷启动阶段的必要性。
2.  **提出了系统的两阶段训练流程**，结合了高质量的轨迹合成与交互式强化学习，有效引导模型掌握并优化工具调用。
3.  **设计了支持代码执行与网络搜索交织的迭代推理框架**，将工具作为推理循环中可互补、可交错使用的内部组件，而非孤立模块，增强了多模态推理的通用性和可扩展性。
4.  **引入了强调工具益处的数据集构建原则和难度过滤机制**，并提出了评估真实世界多模态推理的综合基准 RealX-Bench。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，主要涵盖以下几个方面：

**实验设置**：采用两阶段训练流程。第一阶段为冷启动监督微调（SFT），使用Qwen2.5-VL-7B作为骨干模型，批大小128，学习率1e-5，训练3个epoch。第二阶段为强化学习（RL），采用DAPO算法，批大小256，每个提示16次rollout，学习率1e-6。

**数据集与基准测试**：在多个基准上评估模型能力：
1.  **真实世界理解、OCR与图表理解**：包括V*Bench、HRBench（4K/8K）、MME-RealWorld、TreeBench、OCRBench、SEED2 Plus、CharXiv（描述/推理）、ChartQA。
2.  **多模态推理**：包括MathVista、MathVerse、MathVision、WeMath、DynaMath、LogicVista。
3.  **搜索导向任务**：包括FVQA-test、InfoSeek、MMSearch、SimpleVQA。
4.  **综合评估基准**：提出了RealX-Bench，用于评估感知、搜索和推理的综合能力。

**对比方法**：与多类模型进行比较：
1.  开源通用多模态大模型（如LLaVA-OV、Qwen2.5-VL、InternVL3）。
2.  基于特定工具的推理模型（如使用裁剪的Pixel-Reasoner和DeepEyes，使用代码执行的Thyme）。
3.  纯文本推理模型（如MM-Eureka、ThinkLite）。
4.  专有模型（如GPT4o、Gemini 2.5 Pro）和专用搜索模型（如MMSearch-R1、WebWatcher）。

**主要结果与关键指标**：
1.  **综合性能**：DeepEyesV2在多数基准上超越基线模型。例如，在真实世界理解任务上，相比Qwen2.5-VL-7B，在V*Bench上提升3.3分（81.8 vs. 78.5），在HRBench-4K上提升6.3分（77.9 vs. 71.6）。在数学推理任务上，在MathVista上达到71.9，相比基线提升3.6分；在MathVerse上达到52.7，提升7.1分。
2.  **搜索能力**：在搜索任务上表现突出，在MMSearch上达到63.7的准确率，显著优于专用搜索模型Qwen2.5-VL-7B Search（+11.5分）。
3.  **工具调用特性**：消融实验表明，冷启动阶段结合感知、推理和长思维链（Long CoT）数据效果最佳；强化学习阶段融合感知、推理和搜索数据能带来全面提升。RL训练后，模型工具调用频率降低但灵活性增强，能根据任务自适应地调用工具（如感知任务多用图像操作，推理任务多用数值计算）。
4.  **RealX-Bench结果**：在需要协调感知、搜索和推理的综合任务上，DeepEyesV2显著优于其他模型，而现有最佳专有模型准确率仅为46.0%，远低于人类水平。

### Q5: 有什么可以进一步探索的点？

该论文在构建具备工具调用能力的多模态智能体方面取得了进展，但其探索仍存在局限，未来可从多个维度深入。首先，**工具生态的扩展性**有限，目前主要聚焦代码执行和网络搜索，未来可集成更多专业工具（如数据库查询、API调用）并研究动态工具库的构建方法。其次，**训练方法的效率与稳定性**有待提升，两阶段训练虽缓解了直接强化学习的失败，但冷启动依赖高质量轨迹合成，成本较高；未来可探索更高效的课程学习或自监督方法，减少对强模型生成的依赖。再者，**评估体系仍需完善**，RealX-Bench涵盖了感知、推理和搜索，但对复杂任务中工具调用的**决策透明度**和**错误恢复能力**评估不足；未来需设计更细粒度的基准，如对工具选择合理性、多轮交互效率进行量化。此外，**模型的可解释性与安全性**是重要方向，当前工作未深入探讨工具调用决策的依据，也未系统评估工具使用带来的风险（如代码执行安全、信息检索偏差）；未来可结合因果推理或对抗性测试，提升智能体的可靠性和可控性。最后，**跨模态工具协同**的潜力尚未充分挖掘，例如如何让模型自主规划图像处理与网络检索的交替策略，以解决开放域动态问题，这将是实现更通用智能体的关键。

### Q6: 总结一下论文的主要内容

本文提出了DeepEyesV2，旨在构建一个能主动调用外部工具的智能多模态模型。核心问题是现有模型在需要紧密整合感知、搜索和推理的真实场景中表现不佳，缺乏自主调用工具的能力。为此，论文提出了一种两阶段训练方法：首先通过精心构建的冷启动数据集进行监督微调，以建立基本的工具使用模式；随后利用强化学习进一步优化工具调用行为，仅使用准确性和格式两种简单奖励。方法上，DeepEyesV2将代码执行和网络搜索无缝集成到动态推理循环中，实现证据获取与验证的迭代过程。

论文的主要贡献包括：1) 提出了DeepEyesV2模型，实现了在单一推理循环中统一代码执行和网络搜索；2) 通过严格的数据过滤和清理，构建了多样且难度适中的训练数据集，确保工具使用的有效性；3) 在多个基准测试中验证了模型在真实世界理解、数学推理和搜索密集型任务上的优越性能；4) 引入了RealX-Bench基准，用于综合评估需要感知、搜索和推理整合的真实世界多模态推理能力；5) 分析了模型的任务自适应工具调用模式，发现强化学习能促生更复杂的工具组合和上下文感知的调用行为。实验表明，DeepEyesV2在各项任务上均超越现有通用模型和专用方法，展现出强大的协同推理能力。
