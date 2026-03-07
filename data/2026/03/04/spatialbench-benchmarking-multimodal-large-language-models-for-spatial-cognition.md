---
title: "SpatialBench: Benchmarking Multimodal Large Language Models for Spatial Cognition"
authors:
  - "Peiran Xu"
  - "Sudong Wang"
  - "Yao Zhu"
  - "Jianing Li"
  - "Gege Qi"
date: "2025-11-26"
arxiv_id: "2511.21471"
arxiv_url: "https://arxiv.org/abs/2511.21471"
pdf_url: "https://arxiv.org/pdf/2511.21471v2"
categories:
  - "cs.AI"
tags:
  - "Perception & Multimodal"
  - "Reasoning & Planning"
relevance_score: 5.5
taxonomy:
  capability:
    - "Perception & Multimodal"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "hierarchical spatial cognition framework, high-level capability–oriented metric"
  primary_benchmark: "SpatialBench"
---

# SpatialBench: Benchmarking Multimodal Large Language Models for Spatial Cognition

## 原始摘要

Spatial cognition is fundamental to real-world multimodal intelligence, allowing models to effectively interact with the physical environment. While multimodal large language models (MLLMs) have made significant strides, existing benchmarks often oversimplify spatial cognition, reducing it to a single-dimensional metric, which fails to capture the hierarchical structure and interdependence of spatial abilities. To address this gap, we propose a hierarchical spatial cognition framework that decomposes spatial intelligence into five progressively complex levels from basic observation to high-level planning. Building upon this taxonomy, we construct SpatialBench, a large-scale, fine-grained benchmark covering 15 tasks aligned with these cognitive levels. To provide a unified evaluation across heterogeneous tasks, we further introduce a high-level capability-oriented metric that reliably assesses a model's overall spatial reasoning ability. Extensive experiments over massive MLLMs reveal distinct performance stratification across cognitive levels: models exhibit strong perceptual grounding yet remain limited in symbolic reasoning, causal inference, and planning. Additional human tests demonstrate that humans perform selective, goal-directed abstraction, while MLLMs tend to over-attend to surface details without coherent spatial intent. Our work establishes the first systematic framework for measuring hierarchical spatial cognition in MLLMs, laying the foundation for future spatially intelligent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在空间认知能力评估方面存在的体系化不足问题。研究背景是，空间认知作为与现实世界交互的基础智能，对MLLMs的发展至关重要。尽管已有一些基准测试评估MLLMs的空间推理能力，但现有方法存在显著缺陷：它们往往是碎片化和任务导向的，仅关注特定视觉-语言任务的表现；且多依赖于合成或范围狭窄的数据集，缺乏视觉多样性和真实世界复杂性，导致评估只能提供空间智能的片面视图，难以系统分析模型的认知过程与缺陷。

因此，本文要解决的核心问题是：如何对MLLMs的空间认知能力进行系统、分层、基于认知原理的评估。为此，论文提出了一个分层的空间认知框架，将空间智能分解为从基础感知到高级规划的五个渐进层次，并在此基础上构建了大规模、细粒度的基准测试SpatialBench，以统一评估模型在不同认知层级上的综合空间推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大模型（MLLMs）的演进、现有空间认知评测基准，以及本文工作与它们的区别。

**1. 多模态大模型（MLLMs）的演进**：相关研究指出，LLMs的发展推动了MLLMs的演进，其核心是通过模态接口将视觉编码器与语言主干模型对齐，以理解静态图像乃至动态视频中的跨模态语义。

**2. 现有的空间认知评测基准**：已有多个基准从不同角度评估MLLMs的空间认知能力。例如，Video-MME和VLM4D侧重于视频理解与动态运动分析；STI-Bench和VSI-Bench专注于物理推理与结构化空间理解；Ego-ST Bench评测以自我为中心的导航；SpatialLadder和MindCube则分别覆盖从图像到视频的推理任务以及从有限观察中推断空间结构的能力。

**3. 本文与现有工作的关系和区别**：本文认为，现有基准大多将空间认知简化为孤立的任务（如识别、 grounding 或运动预测），评估设计碎片化，缺乏统一的能力导向框架，且数据多基于简单的室内场景，多样性有限。与之相对，本文提出的SpatialBench基于一个**层次化的空间认知框架**，将空间智能分解为从基础观察到高级规划的五个渐进层级，并构建了覆盖15个对应任务的大规模、细粒度基准。此外，本文引入了**高阶能力导向的统一度量标准**，以系统评估模型的整体空间推理能力，弥补了现有工作在系统性、认知层次覆盖和评估统一性方面的不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的分层评估框架和相应的大规模基准数据集来解决现有基准对空间认知能力评估过于简化的问题。其核心方法包括提出一个分层空间认知能力框架，并基于此框架构建名为SpatialBench的细粒度基准。

整体框架分为理论框架构建和基准数据集构建两大部分。首先，论文基于认知地图理论，提出了一个五层渐进式的空间认知能力分类框架。这五个层级从低到高依次是：观察（L1，识别物体及其属性）、拓扑与关系（L2，理解实体间的空间关系）、符号推理（L3，关联视觉符号与抽象含义并进行规则推理）、因果推理（L4，推断时空依赖关系和动作后果）以及规划（L5，整合前述能力进行目标导向的决策）。这一分层框架是能力驱动的，每个层级代表一个可衡量的、特定的认知阶段，为系统评估奠定了基础。

基于此框架，论文构建了SpatialBench基准。其架构设计的关键在于数据集的创建与验证流程。主要模块包括：1）**数据采集平台**：使用集成了校准RGB相机和3D激光雷达的定制传感平台，从第一人称视角录制视频，同步获取高分辨率视觉流和精确的3D点云几何信息，覆盖多样化的室内外静态与动态场景。2）**问答对生成流程**：采用“人工提问+AI辅助生成答案+传感器计算真值”的混合模式。人工标注员结对工作，根据视频内容提出符合15种任务类型（对应五个认知层级）的问题。对于非度量问题，使用针对不同任务设计的提示模板，调用先进的大模型生成答案并附上推理证据；对于度量问题（如尺寸、距离），则直接利用LiDAR点云数据进行几何计算得到精确真值。3）**多层次验证协议**：为确保标注质量，实施了分层的验证机制。对于低层级（L1, L2）问题，通过比较多个领先模型的输出一致性进行初步筛选，并辅以人工抽查；对于高层级（L3及以上）的复杂问题，则全部进行强制性的人工审核，审核过程有固定检查清单，且有争议的案例会由另一名标注员进行最终裁定。

论文的创新点主要体现在三个方面：一是提出了首个系统性的、基于认知理论的分层空间认知评估框架，将空间智能分解为五个渐进且相互关联的能力层级，超越了以往单维度或孤立任务的评估方式。二是构建了大规模、高质量、多任务的SpatialBench基准，其数据源自真实世界的第一人称视频，并创新性地融合了人工语义理解、大模型推理和传感器精确测量，保证了评估的生态效度和准确性。三是引入了高层次的、能力导向的评估指标，能够跨异构任务可靠地衡量模型的整体空间推理能力，从而揭示了当前MLLMs在感知层面表现较强，但在符号推理、因果推断和规划等高层认知上存在明显短板的性能分层现象。

### Q4: 论文做了哪些实验？

论文在 SpatialBench 基准上进行了广泛的实验，以评估多模态大语言模型（MLLMs）的层次化空间认知能力。

**实验设置与数据集**：实验在作者构建的 SpatialBench 基准上进行。该基准基于一个五层级的空间认知框架（从基础观察到高级规划），涵盖了15个任务。评估了多样化的 MLLMs，包括闭源模型（如 Gemini、GPT、Claude-Sonnet）和开源模型（如 Qwen、GLM、MiniMax、ERNIE），模型参数规模从7B到235B不等，以系统比较不同建模策略的影响。

**评估指标与对比方法**：根据任务类型采用不同指标：多选题任务使用准确率（ACC），数值答案任务使用平均相对准确率（MRA）。为了进行统一评估，论文提出了一种高级能力导向的综合得分，该得分通过自适应权重整合五个认知层级的性能，强调高级推理。实验还进行了上下文学习（单样本）评估，以检验模型从少量示例中泛化空间推理的能力，并对人类参与者进行了基准测试以量化人机差距。

**主要结果与关键指标**：
1.  **模型性能分层**：闭源模型（如 Gemini-2.5-pro）总体得分最高，在高级任务（符号推理、因果、规划）上显著优于大多数开源模型。开源模型中，规模与平均性能呈正相关，但架构设计和训练范式也至关重要。
2.  **认知层级差异**：所有模型在低级任务（观察、拓扑）上表现较好（如物体计数、距离估计），但在高级任务（符号推理、因果、视觉规划）上性能显著下降，方差增大。这表明当前 MLLMs 擅长感知和基础关系推理，但在符号化、因果推断和多步规划方面存在局限。
3.  **上下文学习效果**：单样本提示能显著提升部分模型（如 GPT-5-chat-latest 和 Qwen3-VL）的性能，使其接近甚至达到先前最强模型（Gemini-2.5-pro）的水平，表明提示能有效增强高级空间认知能力。然而，Gemini-2.5-pro 在单样本下性能反而略有下降，可能因其内置上下文理解已足够高效。
4.  **人机对比**：人类在 SpatialBench 上的综合得分高达96.40，在几乎所有任务（尤其是高级任务）上都接近完美准确率（接近100%），表现远超所有 MLLMs，突显了机器在需要高层次推理整合的任务上仍存在巨大差距。人类表现出目标明确的选择性抽象能力，而 MLLMs 则倾向于过度关注表面细节。

### Q5: 有什么可以进一步探索的点？

该论文提出的分层框架和基准测试虽具开创性，但仍存在一些局限性和值得深入探索的方向。首先，SpatialBench主要评估静态图像和文本描述中的空间认知，未能涵盖动态、交互式的真实物理环境（如机器人操作或具身AI的连续空间决策），未来需向视频理解、物理交互和多模态时序推理扩展。其次，基准任务虽分层，但未充分建模各层级能力间的迁移与协同机制，例如高级规划如何依赖底层的符号推理；可研究通过课程学习或组合性任务设计，引导模型实现能力的层级跃迁。再者，论文发现MLLMs过度关注表面细节而缺乏连贯空间意图，这提示未来需探索如何将人类的选择性抽象和目标导向机制融入模型架构，例如通过强化学习引入任务奖励，或设计注意力约束模块以抑制无关感知细节。最后，评估指标虽统一，但未深入解释模型失败的内在原因（如是视觉编码缺陷还是逻辑推理不足），结合可解释性工具进行归因分析，能为模型改进提供更精准的方向。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型在空间认知能力评估上的不足，提出了一个分层空间认知框架，并构建了大规模细粒度基准SpatialBench。核心问题是现有基准将空间认知过度简化为单一维度指标，无法捕捉其层次结构与相互依赖关系。为此，作者将空间智能分解为从基础观察到高级规划的五个渐进复杂层级，并据此创建了涵盖15项对应任务的基准。为统一评估异构任务，论文进一步引入了面向高层能力的度量标准，以可靠评估模型的整体空间推理能力。通过对大量MLLMs的广泛实验，研究发现模型在不同认知层级上表现存在明显分层：它们在感知层面表现较强，但在符号推理、因果推断和规划方面仍受限。此外，人类测试表明人类会进行选择性、目标导向的抽象，而MLLMs往往过度关注表面细节，缺乏连贯的空间意图。这项工作的主要贡献在于建立了首个系统评估MLLMs层次化空间认知的框架，为未来空间智能系统的发展奠定了基础。
