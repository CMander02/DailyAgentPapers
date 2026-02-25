---
title: "How Foundational Skills Influence VLM-based Embodied Agents:A Native Perspective"
authors:
  - "Bo Peng"
  - "Pi Bu"
  - "Keyu Pan"
  - "Xinrun Xu"
  - "Yinxiu Zhao"
  - "Miao Chen"
  - "Yang Du"
  - "Lin Li"
  - "Jun Song"
  - "Tong Xu"
date: "2026-02-24"
arxiv_id: "2602.20687"
arxiv_url: "https://arxiv.org/abs/2602.20687"
pdf_url: "https://arxiv.org/pdf/2602.20687v1"
categories:
  - "cs.AI"
tags:
  - "Embodied AI"
  - "Vision-Language Models"
  - "Agent Benchmark"
  - "Skill Evaluation"
  - "Low-level Control"
relevance_score: 8.0
---

# How Foundational Skills Influence VLM-based Embodied Agents:A Native Perspective

## 原始摘要

Recent advances in vision-language models (VLMs) have shown promise for human-level embodied intelligence. However, existing benchmarks for VLM-driven embodied agents often rely on high-level commands or discretized action spaces, which are non-native settings that differ markedly from real-world control. In addition, current benchmarks focus primarily on high-level tasks and lack joint evaluation and analysis at both low and high levels. To address these limitations, we present NativeEmbodied, a challenging benchmark for VLM-driven embodied agents that uses a unified, native low-level action space. Built on diverse simulated scenes, NativeEmbodied includes three representative high-level tasks in complex scenarios to evaluate overall performance. For more detailed analysis, we further decouple the skills required by complex tasks and construct four types of low-level tasks, each targeting a fundamental embodied skill. This joint evaluation across task and skill granularities enables fine-grained assessment of embodied agents. Experiments with state-of-the-art VLMs reveal clear deficiencies in several fundamental embodied skills, and further analysis shows that these bottlenecks significantly limit performance on high-level tasks. NativeEmbodied highlights key challenges for current VLM-driven embodied agents and provides insights to guide future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于视觉语言模型（VLM）的具身智能体评估中存在的关键缺陷。研究背景是，尽管VLM在推动具身智能方面展现出巨大潜力，但现有评估基准往往无法真实反映模型在现实世界中的实际能力。现有方法主要存在两大不足：一是“非原生”的动作空间设计，许多基准测试将低级动作抽象为高级指令（如“看向苹果”、“传送到桌子”），这掩盖了智能体在空间对齐、导航等关键基础技能上的缺陷，导致评估与真实控制场景脱节；二是“耦合式”任务设计，现有基准大多只关注包含多种技能混合的高级任务，仅以整体成功率进行评估，这种粗粒度的评估方式难以诊断模型在具体基础技能上的瓶颈，限制了评估的全面性和可解释性。

因此，本文要解决的核心问题是：如何从更原生、更细粒度的视角，系统性地评估VLM具身智能体的基础技能，并探究这些基础技能如何影响其执行高级任务的能力。具体而言，论文提出了两个关键研究问题：哪些基础技能对VLM具身智能体真正至关重要？这些基础技能如何影响高级任务的执行？为了解决这些问题，论文引入了NativeEmbodied基准，其核心创新在于采用统一的、原生的低级动作空间来模拟真实控制，并构建了一个包含高级任务和与之解耦的、针对特定基础技能的低级任务的联合评估体系，从而实现对智能体能力更精细的评估和瓶颈分析。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕具身智能基准测试展开，可分为以下几类：

**1. 高层任务基准测试**：如ALFWorld和ALFRED，专注于家庭环境中的高层任务规划，但通常忽略低层连续控制，使用离散或抽象的动作空间。

**2. 低层技能基准测试**：例如VLMbench（针对操作技能）和GOAT-bench（针对导航技能），它们评估孤立的底层技能，但缺乏与高层任务的整合评估。

**3. 多领域综合基准测试**：如EmbodiedBench，覆盖家庭、操作和导航等多个领域，但在处理高层任务时仍依赖高层动作指令，未完全采用原生低层动作空间。EmbodiedEval虽面向VLM，但规模有限且缺少低层任务设计。

**本文与这些工作的关系与区别**：本文提出的NativeEmbodied基准与上述研究均旨在评估VLM驱动的具身智能体，但核心区别在于其强调“原生性”和“联合评估”。具体而言：
- **动作空间**：不同于多数基准使用高层指令或离散动作，NativeEmbodied采用统一的、原生的低层动作空间（如“打开”“拿起”），更贴近真实世界控制。
- **评估维度**：本文同时构建了四类低层基础技能任务（感知、对齐、导航、规划）和三类高层综合任务，实现了从技能到任务的跨粒度联合评估，弥补了现有基准往往只侧重单一层级（高层或低层）的不足。
- **分析深度**：通过解耦复杂任务所需的基础技能，本文能更精细地诊断智能体的能力瓶颈，揭示了基础技能缺陷如何制约高层任务表现，为未来研究提供了更明确的改进方向。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为NativeEmbodied的基准测试来解决现有评估方法在原生性和细粒度分析上的不足。其核心方法是采用“自底向上、解耦评估”的架构设计，将复杂的具身任务分解为高低两个层次进行联合评估。

整体框架包含两大核心部分：一是定义了完全原生的低级动作空间，二是构建了涵盖高、低两个粒度的任务体系。在动作空间设计上，创新性地摒弃了传统的高级指令或离散化动作，转而采用八种最基本的动作原语（如MoveAhead、RotateLeft等）并允许完全自定义参数（如距离、角度），这使得智能体能够以最原始、无约束的方式与环境交互，模拟了真实世界的连续控制。

主要模块包括：
1.  **高级任务模块**：包含探索、搜索和交互三类代表性任务，用于评估智能体在复杂场景下的综合表现。例如，搜索任务要求智能体导航至目标物体并完成精细的空间对准。
2.  **低级技能任务模块**：这是论文的关键创新点。为了诊断具体的能力瓶颈，论文从技能中心视角解耦高级任务，构建了四个专注于基础技能的低级任务：
    *   **感知**：评估智能体对视觉观察中物体、位置和容器的结构化描述能力。
    *   **空间对准**：剥离了导航和规划，仅评估智能体调整视角以对准目标物体的精细空间对齐能力。
    *   **导航**：评估纯导航能力，确保目标在初始视野内，挑战在于路径执行的复杂性。
    *   **规划**：抽象掉运动控制，通过交互任务（如取放）的框架，专门评估多步骤的任务规划推理能力。

关键技术在于通过这种解耦设计，能够精细地分析各项基础技能（如感知、对准）的缺陷如何最终影响高级任务（如搜索）的成功率，从而揭示性能瓶颈的关键路径。此外，数据收集采用了自动生成与人机协同过滤的严格流程，利用模拟器的元数据批量生成样本，并通过大模型多轮测试和专家审核来保证样本质量和挑战性。最终构建的基准包含1085个样本，实现了对具身智能体从底层技能到顶层任务执行能力的全面、细粒度评估。

### Q4: 论文做了哪些实验？

论文在提出的NativeEmbodied基准上进行了系统性实验。实验设置上，智能体在模拟环境中接收640×480的自我中心视角图像，输出统一、原生的低级动作。每个回合的交互历史被截断为20轮，推理时所有VLM的温度统一设为0以确保可复现性。

使用的数据集/基准测试是论文提出的NativeEmbodied，它包含三个高层任务（探索、搜索、交互）和四个解耦的低层基础技能任务（感知、空间对齐、导航、规划），用于联合评估。

对比方法涵盖了15个开源和闭源的主流视觉语言模型，包括GPT系列（GPT-4o, GPT-4v, GPT-o3, GPT-o4-mini）、Claude系列（Claude-3.5-Sonnet等）、Gemini系列（Gemini-2.0-flash等）和Qwen系列（Qwen2.5-VL-72B等不同规模版本）。

主要结果和关键指标如下：
1.  **高层任务表现不佳**：即使在原生设置下，最强模型在复杂高层任务上也表现挣扎。例如，在搜索任务中，表现最好的GPT-o3成功率（SR）仅为34.64%，Claude-4-Sonnet成功率为0。交互和探索任务的最高成功率也分别仅为38.34%和52.43%。
2.  **低层技能表现分化显著**：
    *   **感知**：模型表现良好，例如GPT-o3的F1分数达到83.97%。
    *   **规划**：闭源模型成功率普遍超过50%，GPT-o3达到72.54%。
    *   **导航**：超过一半模型成功率低于50%，最差的闭源模型（Claude-4-sonnet）仅为27.78%。
    *   **空间对齐**：成为主要瓶颈，除GPT-o3（64.16%）外，无模型成功率超过50%，多个闭源模型成功率仅为个位数（如GPT-4v为6.94%）。
3.  **技能消融实验**（以Claude-3.5-Sonnet为对象）表明：提供真实感知信息对性能提升有限；在长视野任务（探索、交互）中，规划和导航是瓶颈；在搜索任务中，导航和对齐（尤其是对齐）能力是关键限制，规划影响有限。
4.  **推理模式影响**：对Gemini-2.5-Pro和Claude-4-Opus启用“思考”模式后，感知和规划任务性能提升，但需要精确动作执行的对齐和导航任务成功率反而下降，表明推理可能干扰低级动作控制。

关键指标包括成功率（SR）、平均步数（AS）、加权平均步数（WAS）、平均最近距离（ACD）、平均最近像素距离（ACPD）以及感知任务的精确率（P）、召回率（R）、F1分数。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准测试仍局限于模拟环境，且主要评估了静态视觉语言模型在具身任务中的表现。未来研究可进一步探索以下几个方向：首先，将基准扩展到真实物理世界，解决模拟到现实的迁移问题，这对实际应用至关重要。其次，当前研究侧重于技能评估，未来可设计针对性训练框架，例如通过强化学习或课程学习来系统性提升模型的基础技能（如空间推理、物体操作等）。此外，论文发现基础技能缺陷会制约高层任务表现，这提示我们需要更深入地研究技能之间的耦合关系，例如探索多技能协同机制或技能组合的泛化能力。最后，可考虑引入动态环境与部分可观测条件，以更好地反映现实世界的复杂性，推动具身智能向更通用、更鲁棒的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对当前基于视觉语言模型（VLM）的具身智能体评估存在的局限，提出了一个名为NativeEmbodied的新基准。核心问题是现有基准多依赖高层指令或离散化动作空间，这与现实世界的连续、低层控制（即“原生”设置）存在显著差异，且缺乏对低层基础技能与高层任务能力的联合评估。

论文的主要贡献是构建了一个统一的、基于原生低层动作空间的挑战性基准。该基准构建于多样化的模拟场景中，包含三种复杂场景下的代表性高层任务以评估整体性能。为了进行更细粒度的分析，作者进一步解耦了复杂任务所需的能力，构建了四类专注于基础具身技能（如导航、操作等）的低层任务。这种跨任务与技能粒度的联合评估框架，能够实现对具身智能体的精细化评估。

实验表明，当前先进的VLM在多项基础具身技能上存在明显缺陷，进一步分析证实这些技能瓶颈严重限制了其在高层任务上的表现。因此，该工作的主要结论是：基础技能不足是制约VLM驱动具身智能体性能的关键挑战。NativeEmbodied基准揭示了这一关键问题，为未来研究指明了方向，即需要加强对VLM底层感知与控制基础能力的提升。
