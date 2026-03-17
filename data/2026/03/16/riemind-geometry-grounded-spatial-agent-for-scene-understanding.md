---
title: "RieMind: Geometry-Grounded Spatial Agent for Scene Understanding"
authors:
  - "Fernando Ropero"
  - "Erkin Turkoz"
  - "Daniel Matos"
  - "Junqing Du"
  - "Antonio Ruiz"
  - "Yanfeng Zhang"
  - "Lu Liu"
  - "Mingwei Sun"
  - "Yongliang Wang"
date: "2026-03-16"
arxiv_id: "2603.15386"
arxiv_url: "https://arxiv.org/abs/2603.15386"
pdf_url: "https://arxiv.org/pdf/2603.15386v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Spatial Reasoning"
  - "Tool Use"
  - "3D Scene Understanding"
  - "Decoupled Perception-Reasoning"
  - "Scene Graph"
relevance_score: 7.5
---

# RieMind: Geometry-Grounded Spatial Agent for Scene Understanding

## 原始摘要

Visual Language Models (VLMs) have increasingly become the main paradigm for understanding indoor scenes, but they still struggle with metric and spatial reasoning. Current approaches rely on end-to-end video understanding or large-scale spatial question answering fine-tuning, inherently coupling perception and reasoning. In this paper, we investigate whether decoupling perception and reasoning leads to improved spatial reasoning. We propose an agentic framework for static 3D indoor scene reasoning that grounds an LLM in an explicit 3D scene graph (3DSG). Rather than ingesting videos directly, each scene is represented as a persistent 3DSG constructed by a dedicated perception module. To isolate reasoning performance, we instantiate the 3DSG from ground-truth annotations. The agent interacts with the scene exclusively through structured geometric tools that expose fundamental properties such as object dimensions, distances, poses, and spatial relationships. The results we obtain on the static split of VSI-Bench provide an upper bound under ideal perceptual conditions on the spatial reasoning performance, and we find that it is significantly higher than previous works, by up to 16\%, without task specific fine-tuning. Compared to base VLMs, our agentic variant achieves significantly better performance, with average improvements between 33\% to 50\%. These findings indicate that explicit geometric grounding substantially improves spatial reasoning performance, and suggest that structured representations offer a compelling alternative to purely end-to-end visual reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉语言模型在三维室内场景理解中，特别是在度量与空间推理任务上表现不足的问题。研究背景是，尽管大语言模型和视觉语言模型在多模态理解方面取得了显著进展，但它们在进行需要精确几何信息（如距离、尺寸、姿态）的空间推理时仍面临挑战，容易出现幻觉和性能下降。现有方法主要依赖于两种范式：一是对VLMs进行大规模空间指令微调，二是让VLMs使用深度图、边界框等几何工具进行增强推理。然而，这些方法都将感知（从视频或图像中提取信息）与推理紧密耦合在一起，这限制了模型在度量空间上的一致性和可解释性，且难以处理需要长期空间上下文的任务。

本文的核心问题是：**能否通过解耦感知与推理来显著提升空间推理性能？** 为此，论文提出了一个名为RieMind的智能体框架，其核心思想是将三维室内场景表示为一个显式的、持久的3D场景图，该场景图由独立的感知模块构建（在本文实验中为简化分析，直接使用真实标注构建，以隔离感知误差）。然后，让一个大语言模型作为智能体，通过调用一系列结构化的几何工具（如查询物体尺寸、距离、姿态、空间关系）来与此3D场景图进行交互和推理，从而将基于隐式视觉特征的端到端理解，转变为基于显式几何表征的、可解释的推理过程。这种方法旨在为LLMs提供一个几何 grounded 的、统一且持久的环境表示，从根本上提升其在复杂三维空间中的理解和推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类**、**工具增强类**和**场景表示类**。

在**方法类**研究中，主流工作如ViCA、SpaceR等，主要通过空间指令问答微调或强化学习来提升基础视觉语言模型（VLM）在VSI-Bench等基准上的性能。这些方法本质上是**端到端的隐式学习和推理**，将感知与推理耦合在一起。本文则与之相反，**解耦了感知与推理**，专注于在理想感知条件下（使用真实标注构建场景图）研究纯推理性能的上限。

在**工具增强类**研究中，一些工作探索为VLM添加几何工具以提升空间推理，如SpatialAgent、TIGeR和MM-Spatial。它们通过工具估计深度、姿态等几何量。本文与它们的共同点是都利用工具，但关键区别在于：本文的工具并非基于实时几何估计，而是**查询一个预先构建的、持久化的3D场景图**，从而提供了更稳定、显式的几何基础。

在**场景表示类**研究中，已有工作将3D场景图（3DSG）作为度量-语义表示，用于具身问答（EQA）等任务。然而，这些应用通常将3DSG以文本形式嵌入提示词中，且场景多为未知需探索。本文则首次将3DSG**系统化、结构化地**应用于室内3D空间理解基准（VSI-Bench），并通过**结构化工具箱**让智能体访问3DSG，专注于绝对和相对的空间理解，与此前应用方向显著不同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RieMind的几何空间智能体框架来解决视觉语言模型在度量与空间推理上的不足。该框架的核心思想是将感知与推理解耦，利用显式的三维场景图（3DSG）作为基础，并通过一组结构化的几何工具让大语言模型（LLM）进行空间推理。

整体架构分为两个主要组件：感知层和推理层。感知层负责从RGB-D图像和相机参数构建持久化的3DSG，该图以层次化结构表示场景，包含建筑、楼层、房间和物体节点，以及它们之间的连接边。每个节点存储语义和度量信息（如尺寸、体积、位姿），边则表达空间关系（如“靠近”）。为了专注于评估推理能力，论文使用真实标注构建3DSG，以排除感知误差。

推理层是一个智能体系统，基于LLM并通过模型上下文协议（MCP）服务器与一组几何工具交互。这些工具被分为四个语义命名空间：记忆工具（提供场景图摘要）、场景工具（支持基于节点ID或文本的图查询）、几何工具（提供尺寸、距离等度量计算）以及位置与方向工具（处理坐标系转换与投影）。工具设计遵循三个关键原则：最小几何原语（每个工具仅执行原子操作）、显式接地（通过唯一节点ID确保引用一致性）和确定性（输出仅依赖于3DSG状态）。

创新点在于：第一，通过解耦感知与推理，使用显式3DSG作为唯一真实来源，避免了端到端模型中两者的纠缠；第二，设计了一套结构化、可解释的工具箱，迫使智能体依赖基础几何属性进行分步推理，而非内部隐含计算；第三，智能体提示经过精心设计，包含角色定义、工具列表、场景上下文和行为约束，确保推理过程可追踪。实验表明，该方法在理想感知条件下显著提升了空间推理性能，且无需任务特定微调。

### Q4: 论文做了哪些实验？

实验在VSI-Bench的静态空间问题上评估了所提出的几何基础智能体框架。实验设置上，为了隔离感知与推理并探究推理性能的上限，研究使用来自三个3D场景数据集（ARKitScenes、ScanNet和ScanNet++）的真实标注构建了显式的3D场景图（3DSG），作为智能体的几何基础。评估数据集为VSI-Bench的静态部分，包含4185个问题，涵盖物体计数、绝对距离、物体尺寸、房间尺寸、相对距离和相对方向六种类型。对比方法包括三类：1）未使用工具或微调的基础视觉语言模型（如GPT-4o、Gemini系列、Qwen2.5-VL-7B等）；2）开源模型（如InternVL3-78B、LLaVA系列）；3）经过特定任务微调的模型（如SpaceR、VLM-3R、SpaceMind等）。

主要结果表明，基于3DSG和几何工具的智能体框架显著提升了空间推理性能。关键数据指标如下：在基础VLM对比中，智能体版本相比原始版本平均提升显著，例如GPT-4o从35.3%提升至85.2%（+49.9%），Qwen2.5-VL-7B从31.2%提升至64.1%（+32.9%）。在绝对性问题（如物体计数、绝对距离、物体尺寸）上提升尤为巨大，GPT-4o在绝对距离问题上从5.3%提升至93.2%（+87.9%）。与所有对比方法相比，该框架取得了最先进的性能，其中GPT-4.1智能体达到了89.5%的平均准确率，超越了之前最佳的微调模型SpaceMind（73.6%）。研究还发现，性能提升与问题组合复杂性相关：简单问题（需1-2次工具调用）提升巨大，而复杂问题（如相对方向，需5-6次工具调用）则更依赖模型本身的推理能力，因此GPT-4.1在相对方向问题上比GPT-4o提升了近20个百分点。这些结果证明了显式几何基础对于提升空间推理的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其依赖真实标注来构建3D场景图（3DSG），这在实际应用中难以实现，因此未来首要方向是开发从RGB-D等传感器数据自动构建3DSG的感知模块。此外，论文指出复杂组合性问题（如相对方向推理）仍是瓶颈，尤其是较小模型表现较差，这提示未来需增强大语言模型（LLM）自身的空间关系推理能力，可能通过引入更精细的几何约束或混合符号推理机制。

进一步探索点包括：将框架扩展至动态场景，处理时序变化与交互；尝试将该几何 grounding 方法迁移至视觉语言模型（VLM），以增强其原生空间推理能力；探索3DSG的增量更新与在线学习机制，提升系统实用性。从方法融合角度看，可研究如何平衡解耦与端到端学习的优势，例如在保持结构化表征的同时，引入少量任务特定微调以进一步提升性能。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为RieMind的几何空间智能体框架，旨在解决现有视觉语言模型在室内场景理解中面临的度量和空间推理难题。核心问题是传统方法通常将感知与推理耦合，导致性能受限。为此，论文主张将两者解耦，并引入基于显式三维场景图的智能体框架。

方法上，RieMind通过专用感知模块构建持久化的三维场景图来表示静态室内场景，并基于真实标注实例化以隔离推理性能。智能体仅通过结构化几何工具与场景交互，这些工具暴露物体的尺寸、距离、姿态和空间关系等基本属性，从而将大型语言模型在三维场景图中进行几何接地。

主要结论显示，在VSI-Bench静态数据集上，该方法在理想感知条件下实现了空间推理性能的上限，比先前工作提升高达16%，且无需任务特定微调。相比基础视觉语言模型，性能平均提升33%至50%。这表明显式几何接地能显著增强空间推理，结构化表示为纯端到端视觉推理提供了有前景的替代方案。
