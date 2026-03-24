---
title: "Seed1.8 Model Card: Towards Generalized Real-World Agency"
authors:
  - "Bytedance Seed"
date: "2026-03-21"
arxiv_id: "2603.20633"
arxiv_url: "https://arxiv.org/abs/2603.20633"
pdf_url: "https://arxiv.org/pdf/2603.20633v1"
categories:
  - "cs.AI"
tags:
  - "Foundation Model for Agents"
  - "Multi-Turn Interaction"
  - "Tool Use"
  - "Multi-Step Execution"
  - "Unified Agentic Interface"
  - "Search"
  - "Code Generation"
  - "GUI Interaction"
  - "Latency-Aware Inference"
  - "Cost-Aware Inference"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# Seed1.8 Model Card: Towards Generalized Real-World Agency

## 原始摘要

We present Seed1.8, a foundation model aimed at generalized real-world agency: going beyond single-turn prediction to multi-turn interaction, tool use, and multi-step execution. Seed1.8 keeps strong LLM and vision-language performance while supporting a unified agentic interface-search, code generation and execution, and GUI interaction. For deployment, it offers latency- and cost-aware inference, including configurable thinking modes and optimized visual encoding for images and video. We report evaluations on standard benchmarks and application-aligned workflows spanning foundational skills, multimodal understanding, and agentic behavior. Seed1.8 is released to support further research and development on interactive, real-world use cases.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型和视觉语言模型在迈向通用现实世界智能体时所面临的挑战。研究背景是，尽管现有模型在自然语言理解、推理、代码生成和多模态感知等基础能力上表现出色，但它们主要局限于单轮预测任务。然而，许多实际应用（如工具调用、环境交互和多步骤任务执行）需要模型具备持续交互和决策的能力。现有方法的不足在于，它们往往依赖特定任务的代理流程，缺乏将感知、推理和行动统一在一个模型中的通用交互能力，同时也未能充分考虑实际部署中的延迟和成本约束。

本文的核心问题是：如何构建一个既能保持强大基础性能，又能支持统一、多步骤交互执行的通用智能体模型，以应对现实世界中复杂的交互式任务。为此，论文提出了Seed1.8基础模型，它致力于超越单轮预测，实现多轮交互、工具使用和多步骤执行。该模型强调在单一模型中整合感知、推理和行动，提供统一的智能体接口（包括搜索、代码生成与执行、图形用户界面交互），并引入延迟和成本感知的推理机制（如可配置的思考模式和优化的视觉编码），以平衡性能与效率。最终，Seed1.8的目标是支持交互式、现实世界的用例，推动通用智能体的研究和开发。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 基础大模型研究**：包括大型语言模型（如GPT系列、LLaMA）和视觉语言模型（如Flamingo、BLIP系列）。这些模型在自然语言理解、推理、代码生成和多模态感知方面取得了显著进展，为智能体行为提供了基础能力。Seed1.8继承了这些模型的强基准性能，但目标超越了单轮预测。

**2. 专用智能体框架与系统**：例如ReAct、Toolformer、AutoGPT等研究，它们通过外部工具调用、环境反馈和多步规划来增强模型的任务执行能力。这些工作通常采用“模型+外部管道”的架构。相比之下，Seed1.8强调在单一模型内集成感知、推理与行动，提供统一的智能体交互接口（如搜索、代码执行、GUI交互），旨在实现更通用的现实世界智能体能力。

**3. 多模态交互与具身智能研究**：涉及视觉基础模型和机器人控制等领域，关注模型对物理世界或数字环境的理解与操作。Seed1.8与此类研究的联系在于其原生视觉感知能力，可直接解读截图、图表、视频等并与之交互，但其重点更偏向广义的数字世界智能体，而非具体的机器人控制。

**4. 高效推理与部署技术**：包括模型压缩、推理优化、延迟敏感型架构等研究。Seed1.8的贡献在于提供了面向延迟和成本感知的推理机制，如可配置的“思考模式”和针对图像视频的优化视觉编码，以适配交互式部署的实时性要求。

**5. 智能体评估方法**：相关研究致力于开发超越传统静态基准的评估体系，以衡量模型在复杂、交互式任务中的表现。本文的评估策略与此一致，结合了公开基准和从高价值应用场景衍生的内部工作流评估，以更贴合实际应用。

### Q3: 论文如何解决这个问题？

论文通过构建一个统一的多模态智能体基础模型来解决从单轮预测到多轮交互与执行的泛化问题。其核心方法是将感知、推理与行动能力集成于单一模型，而非依赖特定任务的外部流水线。

整体框架上，Seed1.8 在保持强大语言与视觉语言基础能力的同时，设计了一个统一的智能体交互接口。该接口集成了三大关键模块：一是搜索模块，用于从外部获取信息并进行证据合成；二是代码生成与执行模块，支持结构化计算、程序修改与工具编排；三是图形用户界面交互模块，通过原生视觉感知能力直接解读截图、文档、图表及视频等视觉界面，从而在缺乏程序化 API 时也能操作软件环境。这些模块使得模型能够基于检索、代码执行和环境交互的中间结果进行多步迭代决策。

关键技术包括：首先，模型采用优化的视觉编码方案，显著降低了图像与视频输入的令牌消耗，提升了处理效率；其次，引入了可配置的“思考模式”，允许在推理深度与响应延迟之间进行权衡，以满足实际部署中对延迟与成本的敏感需求。创新点主要体现在将多种代理能力（搜索、代码、GUI交互）内聚到一个模型中，并实现了感知-行动闭环，同时通过效率优化机制确保其在交互式场景中的实用性。

### Q4: 论文做了哪些实验？

论文对Seed1.8模型进行了全面评估，涵盖三大类别：基础LLM能力、多模态（VLM）能力和智能体（Agentic）能力。

**实验设置**：模型支持四种“思考模式”（no_think, think-low, think-medium, think-high），以在延迟、计算成本和解决方案质量之间进行权衡。主要评估默认使用think-high模式，并在专门章节分析了不同思考模式的性能与成本对比。

**数据集/基准测试**：
1.  **基础能力**：在数学（AIME-25, HMMT-25等）、代码（AetherCode, LiveCodeBench等）、STEM推理（GPQA-Diamond, PHYBench等）、通用推理（KOR-Bench, ARC-AGI-1）、复杂指令遵循（Inverse IFEval, MARS-Bench等）和知识（MMLU, MMLU-pro等）领域使用了超过20个公开基准。此外，还设计了6个内部基准，评估教育、客服问答、信息处理、意图识别、信息提取和复杂工作流等高价值经济领域。
2.  **多模态能力**：
    *   **图像理解**：在超过30个公开基准上评估，包括多模态推理（MMMU, MathVista等）、通用视觉问答（VLMsAreBiased, MMBench等）、GUI定位（ScreenSpot-Pro）、指向与计数（CountBench, FSC-147）、2D/3D空间理解（BLINK, DA-2K等）、文档图表理解（AI2D, OmniDocBench）以及多模态长上下文理解（DUDE, MMLB-NIAH）。
    *   **视频理解**：在超过20个公开基准上评估，涵盖知识与推理（VideoMMMU, VCRBench等）、运动与感知（TVBench, TOMATO等）、长视频理解（VideoMME, LongVideoBench）和流媒体理解（OVBench, StreamingBench）。
3.  **智能体能力**：评估了需要与外部资源进行多轮交互的能力，包括搜索、编码与工具使用、写作和基于GUI的执行（相关表格在提供内容中未详细展开）。

**对比方法**：主要与当前领先的闭源大模型进行对比，包括GPT-5（High）、Claude-Sonnet-4.5、Gemini-2.5-pro和Gemini-3-pro。在多模态评估中，还与前代模型Seed1.5-VL进行了比较。

**主要结果与关键指标**：
*   **基础能力**：Seed1.8在多项基准上达到领先或极具竞争力的水平。例如，在数学推理的BeyondAIME、AMO-Bench和IMO-AnswerBench上获得第二高分（分别为77.0、60.0、76.3）。在客服问答（69.0）和教育（60.8）内部基准上取得了最佳性能。
*   **多模态图像理解**：Seed1.8在多个基准上表现优异，例如在VLMsAreBiased上取得62.0的高分，在ZeroBench (main)上达到11.0，在DA-2K上达到90.7，在OmniDocBench 1.5上获得0.106的低误差（NED指标，越低越好）。
*   **多模态视频理解**：Seed1.8在多个视频基准上取得最佳或次佳成绩，例如在VCRBench上达到59.8（最佳），在TOMATO上达到60.8（最佳），在Countix上达到31.0（最佳），在StreamingBench上达到84.4（最佳）。

### Q5: 有什么可以进一步探索的点？

这篇论文提出了一个面向通用现实世界智能体的基础模型，在统一接口和部署优化方面取得了进展，但仍存在一些局限性和值得深入探索的方向。

首先，模型在“通用性”和“现实世界”方面的评估可能仍显不足。论文提到了标准基准测试和应用导向的工作流评估，但现实世界的任务具有极高的复杂性和长尾分布。未来的研究可以更侧重于在开放、动态、非结构化的真实环境（如完全真实的操作系统、复杂的跨应用工作流）中进行系统性评估，检验其泛化能力和鲁棒性边界。

其次，模型架构与能力扩展方面有探索空间。论文支持多模态输入和工具调用，但如何更高效地整合持续学习机制，使智能体能在与环境的交互中自主发现并学习使用新工具，是一个关键挑战。此外，当前的“可配置思考模式”和延迟感知推理是重要优化，未来可以探索更细粒度的资源-精度权衡策略，以及面向复杂任务的动态规划与回溯机制，使其不仅能执行计划，还能在失败时进行有效的自我诊断与调整。

最后，在安全与对齐层面，一个能在现实世界执行多步操作的智能体带来了新的风险。论文未深入探讨其行动可能产生的物理或数字世界副作用。未来的工作必须加强对智能体行为可预测性、安全护栏以及对人类意图对齐的研究，确保其强大能力能被安全、可控地部署。

### Q6: 总结一下论文的主要内容

该论文介绍了Seed1.8基础模型，其核心目标是实现**广义的现实世界智能体能力**，即超越单轮预测，专注于多轮交互、工具使用和多步骤执行。论文的主要贡献在于设计了一个**统一的智能体接口**，该模型在保持强大语言和视觉语言性能的同时，集成了网络搜索、代码生成与执行以及图形用户界面交互等关键功能。

在方法上，Seed1.8为实际部署进行了优化，提供了**兼顾延迟与成本的推理方案**，包括可配置的“思考”模式和针对图像视频的优化视觉编码。评估涵盖了标准基准测试和面向应用的工作流，涉及基础技能、多模态理解和智能体行为。

主要结论是，Seed1.8作为一个公开发布的模型，在维持通用能力的基础上，显著推进了面向交互式现实场景的智能体技术，为相关研究和开发提供了重要支持。
