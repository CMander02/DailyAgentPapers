---
title: "GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis"
authors:
  - "Bo Yu"
  - "Cheng Yang"
  - "Dongyang Hou"
  - "Chengfu Liu"
  - "Jiayao Liu"
  - "Chi Wang"
  - "Zhiming Zhang"
  - "Haifeng Li"
  - "Wentao Yang"
date: "2026-04-15"
arxiv_id: "2604.13888"
arxiv_url: "https://arxiv.org/abs/2604.13888"
pdf_url: "https://arxiv.org/pdf/2604.13888v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool-Augmented Agent"
  - "Agent Architecture"
  - "Spatial Analysis"
  - "Dynamic Execution"
  - "Parameter Tuning"
  - "Error Recovery"
  - "Multi-step Reasoning"
relevance_score: 8.0
---

# GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis

## 原始摘要

The integration of Large Language Models (LLMs) into Geographic Information Systems (GIS) marks a paradigm shift toward autonomous spatial analysis. However, evaluating these LLM-based agents remains challenging due to the complex, multi-step nature of geospatial workflows. Existing benchmarks primarily rely on static text or code matching, neglecting dynamic runtime feedback and the multimodal nature of spatial outputs. To address this gap, we introduce GeoAgentBench (GABench), a dynamic and interactive evaluation benchmark tailored for tool-augmented GIS agents. GABench provides a realistic execution sandbox integrating 117 atomic GIS tools, encompassing 53 typical spatial analysis tasks across 6 core GIS domains. Recognizing that precise parameter configuration is the primary determinant of execution success in dynamic GIS environments, we designed the Parameter Execution Accuracy (PEA) metric, which utilizes a "Last-Attempt Alignment" strategy to quantify the fidelity of implicit parameter inference. Complementing this, a Vision-Language Model (VLM) based verification is proposed to assess data-spatial accuracy and cartographic style adherence. Furthermore, to address the frequent task failures caused by parameter misalignments and runtime anomalies, we developed a novel agent architecture, Plan-and-React, that mimics expert cognitive workflows by decoupling global orchestration from step-wise reactive execution. Extensive experiments with seven representative LLMs demonstrate that the Plan-and-React paradigm significantly outperforms traditional frameworks, achieving the optimal balance between logical rigor and execution robustness, particularly in multi-step reasoning and error recovery. Our findings highlight current capability boundaries and establish a robust standard for assessing and advancing the next generation of autonomous GeoAI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何系统、准确地评估基于大语言模型（LLM）的智能体在复杂地理空间分析任务中的实际执行能力这一核心问题。

研究背景是，将LLM集成到地理信息系统（GIS）中以实现自主空间分析是地理空间人工智能（GeoAI）的重要趋势。与传统针对单一任务的端到端模型不同，基于LLM的智能体能够理解自然语言、规划多步骤工作流并调用外部工具，有望将依赖专家手动操作的复杂空间分析流程转变为自动化过程，降低技术门槛。

然而，现有评估方法存在显著不足，无法有效衡量智能体在真实、动态环境中的表现。具体而言：1）**评估范式静态**：现有基准（如GeoBenchX、GeoAnalystBench）多采用静态文本规划匹配或代码相似度比较，缺乏在真实执行环境中的动态交互与反馈，无法测试智能体面对运行时错误（如坐标参考系不匹配）时的诊断与自纠正能力。2）**任务覆盖片面**：现有基准对复杂地理空间工作流的解构不足，任务往往较为基础或呈孤立算子组合，难以系统评估智能体在真实长链条、高复杂性分析工作流中的综合能力。3）**评估维度单一**：现有方法多简化为文本级比较，忽略了空间分析输出的多模态特性（如空间数据文件的几何正确性、最终地图制图的质量），未能进行统一评估。

因此，本文的核心问题是：**如何构建一个动态、交互式的评估基准，以全面、真实地衡量工具增强型GIS智能体在复杂、多步骤空间分析工作流中的规划、执行、参数推断及容错恢复能力**。为此，论文提出了GeoAgentBench（GABench），旨在填补上述研究空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**地理空间基础模型**、**地理空间智能体**以及**评估基准**。

在**地理空间基础模型**方面，相关工作包括通过持续预训练增强地球科学知识理解的K2模型，以及通过提示注入空间信息来提取知识的GeoLLM等语言模型。在视觉与多模态领域，出现了专注于遥感影像与自然语言对齐的VLM模型，以及支持多源异构时空模态的统一框架AllSpark。然而，这些模型主要聚焦于事实问答、文本摘要或基础感知任务，对于**复杂空间分析所需的多步骤工具调用和参数推理能力**探索不足，这是本文工作的出发点之一。

在**地理空间智能体**方面，研究探索了利用LLM自动化GIS任务全生命周期的“自主GIS”理论框架。具体系统包括专注于地理数据检索的LLM-Find、嵌入QGIS等平台的GIS Copilot，以及处理特定数据类型的多智能体系统如ShapefileGPT。在遥感领域，也有如REMSA、GeoLLM-Squad等多智能体系统用于模型推荐和任务协调。这些系统展示了潜力，但普遍**严重依赖LLM的零样本代码生成能力，缺乏对运行时错误（如坐标系不匹配、参数配置错误）的感知与自我纠正机制**，且在分解和编排未知步骤的复杂长链工作流方面能力较弱。本文提出的Plan-and-React智能体架构正是为了弥补这些缺陷。

在**评估基准**方面，通用领域已有成熟的基准如ToolBench和API-Bank，但它们将工具视为无状态的通用函数，难以捕捉地理空间分析特有的语义约束。地理空间领域近期也出现了一些基准，如专注于遥感影像感知的ThinkGeo、Earth-Agent，以及专注于代码或计划生成的GeoBenchX、GeoPlan-Bench、GeoAnalystBench等。然而，这些现有基准**主要依赖静态的文本或代码匹配进行评分，脱离了真实的执行环境**，无法评估代码在真实异构空间数据下的运行时健壮性、错误恢复能力，也缺乏对制图可视化质量的关注。本文的GeoAgentBench通过构建集成真实GIS工具库的闭环执行环境、引入基于运行时反馈的动态评估指标（如PEA）以及利用VLM进行多模态输出验证，旨在建立一个更全面、更贴近实际应用逻辑的新评估标准。

### Q3: 论文如何解决这个问题？

论文通过构建一个动态、交互式的评估基准（GeoAgentBench）并设计一种新型的智能体架构（Plan-and-React）来解决问题。

**核心方法与整体框架**：论文的核心是创建了GABench基准，它包含一个基于六大地域信息科学核心领域的分层任务系统（共53个典型任务）和一个集成了117个原子GIS工具的动态执行沙箱。该框架旨在弥合高级推理与物理地理空间计算之间的鸿沟。其工作流程包括：从专业来源筛选和重构任务，将粗粒度的分析逻辑分解为原子化的工具流，并通过闭环一致性校验和专家评审确保工具流的逻辑完整性与输出正确性，形成“已验证的物理事实”。

**主要模块与关键技术**：
1.  **任务系统与原子工具库**：任务涵盖空间数据管理、矢量/栅格分析等六个领域，难度递进。关键创新在于对原始任务进行了**结构性重构**，将高层语义步骤（如“插值”）转化为由精确、可执行的原子工具（如`ordinary_kriging`，需指定网格范围和变差函数模型）组成的工具流。这解决了原有基准中逻辑粒度粗、代码模块性差的问题。
2.  **动态执行沙箱**：这是一个轻量级的交互式运行时环境，基于开源地理空间栈（如GeoPandas）。其关键技术包括：为每个任务分配独立的**持久化状态管理工作区**；设计**隔离的去噪反馈机制**，将复杂的Python错误追踪转化为语义清晰的错误信息；模拟真实的**文件写入冲突**（如文件锁定），以测试智能体的错误诊断与恢复能力。
3.  **评估指标**：
    *   **参数执行准确率**：针对动态GIS环境中参数配置是执行成功的关键，设计了PEA指标。它采用“最后一次尝试对齐”策略，量化智能体对隐含参数推理的保真度。
    *   **基于VLM的验证**：提出使用视觉语言模型来评估输出结果的**数据空间准确性**和**制图风格符合度**，以应对空间输出的多模态特性。
4.  **Plan-and-React智能体架构**：这是为解决参数错配和运行时异常导致的频繁任务失败而提出的创新架构。它模仿专家认知工作流，**将全局编排与逐步反应式执行解耦**。具体而言，智能体先制定一个全局计划（Plan），然后在逐步执行中，根据沙箱的实时反馈（如错误、中间结果）进行反应和调整（React）。实验表明，该架构在逻辑严谨性和执行鲁棒性之间取得了最佳平衡，显著优于传统框架，尤其在多步推理和错误恢复方面。

**总结**：论文通过构建一个覆盖全面、逻辑原子化、支持动态交互执行的基准测试环境（GABench），并配套开发了专注于参数推理准确性的评估指标以及一种能有效应对执行不确定性的新型智能体架构，系统地解决了对工具增强型GIS智能体进行动态、可靠评估的挑战。

### Q4: 论文做了哪些实验？

论文实验围绕评估和提升工具增强型GIS智能体的动态执行能力展开。实验设置方面，研究构建了名为GeoAgentBench的动态交互式评估基准，包含一个集成117个原子GIS工具的执行沙箱，覆盖6个核心GIS领域的53个典型空间分析任务。数据集/基准测试即该基准本身，用于模拟真实、多步骤的地理空间工作流。

对比方法上，研究评估了七种代表性大语言模型（LLMs）在传统智能体框架与新提出的“Plan-and-React”架构下的性能。主要对比维度包括任务执行的轨迹连贯性和最终输出质量。

主要结果通过一套多层次评估指标呈现。关键数据指标包括：
1.  **轨迹连贯性指标**：TAO（工具任意顺序，基于F1分数）、TIO（工具顺序准确度，基于最长公共子序列）、TEM（工具精确匹配，基于最长公共前缀）。
2.  **参数执行准确度**：提出了核心指标PEA（参数执行准确度），采用“最后尝试对齐”策略，量化智能体在动态环境中对隐含参数推断的保真度。
3.  **输出质量评估**：利用视觉语言模型进行自动化评估，检验数据空间准确性和制图风格遵循度。

实验结果表明，新提出的“Plan-and-React”智能体架构显著优于传统框架，在多步骤推理和错误恢复方面实现了逻辑严谨性与执行鲁棒性的最佳平衡，特别是在处理由参数错配和运行时异常导致的任务失败时表现出色。这些发现明确了当前能力的边界，并为评估和推进下一代自主地理人工智能建立了可靠标准。

### Q5: 有什么可以进一步探索的点？

该论文提出的GeoAgentBench和Plan-and-React架构是重要进展，但仍存在局限性和广阔的探索空间。

**局限性方面**：1) **工具覆盖度**：虽然集成了117个工具，但专业GIS工具链庞大且不断更新，现有集合可能无法覆盖某些细分领域（如水文建模、网络分析）的复杂操作。2) **评估维度**：PEA指标和VLM验证主要关注参数准确性和输出样式，但对**空间分析逻辑的语义正确性**（如分析流程的合理性、结论的可靠性）评估尚显薄弱。3) **环境真实性**：沙箱环境虽提供动态反馈，但与真实GIS软件环境（如ArcGIS、QGIS）的复杂性、数据多样性和意外错误（如投影冲突、内存不足）仍有差距。

**未来研究方向与改进思路**：
1.  **增强评估的深度与广度**：可引入**领域专家评分**或**基于知识图谱的推理验证**，以评估分析链条的语义正确性。同时，将基准扩展至**时空预测、模拟优化**等更复杂的决策支持任务。
2.  **提升代理的认知与适应能力**：当前的Plan-and-React架构在错误恢复上仍有提升空间。可探索**基于强化学习的策略优化**，使代理能从历史错误中学习，动态调整规划策略。此外，可研究代理的**元认知能力**，使其能评估自身知识盲区并主动查询或学习新工具。
3.  **迈向通用地理空间智能**：未来工作可探索**多智能体协作框架**，让多个具备不同专长的Geo-Agent协同解决复杂地理问题。同时，推动**工具与模型的深度融合**，例如开发能理解工具底层算法原理、并能自主组合或微调工具的“创造型”代理，这将是迈向真正自主空间智能的关键一步。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）与地理信息系统（GIS）结合后，其智能体在复杂空间分析任务中难以被准确评估的问题，提出了一个动态交互式评测基准GeoAgentBench（GABench）。其核心贡献在于构建了一个包含117个原子工具和53个典型任务的动态执行沙箱，以模拟真实、多步骤的地理空间工作流。为应对动态环境中精确参数配置这一关键挑战，论文设计了参数执行准确率（PEA）指标，采用“末次尝试对齐”策略来量化智能体对隐含参数的推断能力，并辅以基于视觉语言模型（VLM）的验证来评估数据空间准确性和制图风格。此外，针对参数错配和运行时异常导致的任务失败，论文提出了一种新颖的“规划与反应”（Plan-and-React）智能体架构，通过将全局规划与逐步反应式执行解耦，模仿专家的认知工作流。实验表明，该架构在七种代表性LLM上显著优于传统框架，在多步推理和错误恢复方面实现了逻辑严谨性与执行鲁棒性的最佳平衡。该研究不仅揭示了当前LLM在空间分析中的能力边界，也为下一代自主地理人工智能（GeoAI）的评估与发展建立了坚实的标准。
