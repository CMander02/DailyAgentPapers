---
title: "AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement"
authors:
  - "Siqi Pei"
  - "Liang Tang"
  - "Tiaonan Duan"
  - "Long Chen"
  - "Shuxian Li"
  - "Kaer Huang"
  - "Yanzhe Jing"
  - "Yiqiang Yan"
  - "Bo Zhang"
  - "Chenghao Jiang"
  - "Borui Zhang"
  - "Jiwen Lu"
date: "2026-03-18"
arxiv_id: "2603.17441"
arxiv_url: "https://arxiv.org/abs/2603.17441"
pdf_url: "https://arxiv.org/pdf/2603.17441v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Vision-Language Model"
  - "Instruction Refinement"
  - "Adaptive Zoom"
  - "Localization"
  - "Tool Use"
  - "Benchmark Dataset"
  - "GRPO Training"
relevance_score: 7.5
---

# AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement

## 原始摘要

GUI grounding is a critical capability for vision-language models (VLMs) that enables automated interaction with graphical user interfaces by locating target elements from natural language instructions. However, grounding on GUI screenshots remains challenging due to high-resolution images, small UI elements, and ambiguous user instructions. In this work, we propose AdaZoom-GUI, an adaptive zoom-based GUI grounding framework that improves both localization accuracy and instruction understanding. Our approach introduces an instruction refinement module that rewrites natural language commands into explicit and detailed descriptions, allowing the grounding model to focus on precise element localization. In addition, we design a conditional zoom-in strategy that selectively performs a second-stage inference on predicted small elements, improving localization accuracy while avoiding unnecessary computation and context loss on simpler cases. To support this framework, we construct a high-quality GUI grounding dataset and train the grounding model using Group Relative Policy Optimization (GRPO), enabling the model to predict both click coordinates and element bounding boxes. Experiments on public benchmarks demonstrate that our method achieves state-of-the-art performance among models with comparable or even larger parameter sizes, highlighting its effectiveness for high-resolution GUI understanding and practical GUI agent deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型在图形用户界面（GUI）定位任务中面临的挑战。研究背景是，随着GUI成为人机交互的主要方式，自动化操作需求日益增长，而现有基于结构化数据（如HTML）的智能体难以处理纯图像界面。GUI定位要求模型根据自然语言指令在屏幕截图中精确找到目标元素，是实现自动化交互的核心能力。

现有方法存在两个主要不足。首先，面对高分辨率GUI截图和小尺寸UI元素（如图标、文本），模型在降采样过程中会丢失关键细节，导致定位不准。一些两阶段方法采用固定比例放大预测区域，但这种方式对简单或低分辨率截图会造成不必要的计算开销，且可能因丢失放大区域外的上下文信息而降低性能。其次，现有数据集的指令通常过于简单直接，而真实用户指令往往复杂或模糊，现有模型在语义理解上存在局限，单纯依赖定位数据训练难以提升指令理解能力。

本文要解决的核心问题是：如何在高分辨率GUI中精准定位小元素，同时提升对模糊自然语言指令的理解能力。为此，论文提出了AdaZoom-GUI框架，其创新点在于结合了自适应放大策略和指令优化模块。自适应放大仅针对预测的小元素触发二次推理，平衡了精度与效率；指令优化模块则将原始指令重写为明确详细的描述，使定位模型能专注于坐标预测而非语义解析。通过构建高质量数据集并采用GRPO训练，模型能同时预测点击坐标和元素边界框，从而支持条件放大策略，最终在公开基准测试中取得了先进性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，相关工作主要围绕提升GUI grounding性能展开。一类是直接基于通用视觉语言模型（VLMs）进行监督微调（SFT）或强化学习，以增强其在GUI截图上的定位能力。另一类是针对高分辨率GUI中元素小的问题，提出了两阶段策略，即先粗略定位再固定比例放大区域进行二次推理。本文提出的AdaZoom-GUI框架与这些方法密切相关，但存在关键区别：它没有采用固定的放大策略，而是设计了**条件性放大策略**，仅当预测的目标元素较小时才触发放大，从而在简单场景下避免不必要的计算和上下文信息丢失，在复杂场景下提升定位精度。

在应用类研究中，大量工作致力于开发基于自然语言指令与图形界面交互的GUI智能体。这些智能体通常依赖HTML或无障碍树等结构化表示，而本文聚焦于更通用的、仅基于屏幕截图（视觉模态）的 grounding 任务，这是实现此类智能体的基础能力。

在评测类方面，现有研究依赖于公开的基准测试数据集。本文指出这些数据集的自然语言指令通常过于简单直接，与真实场景中复杂模糊的用户指令存在差距。为此，本文引入了**指令精炼模块**，将原始指令重写为更清晰详细的描述，从而将指令理解与元素定位能力解耦，这是与以往工作的重要区别。此外，本文还构建了高质量的GUI grounding数据集，并采用分组相对策略优化（GRPO）进行训练，以支持条件放大策略。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AdaZoom-GUI的自适应缩放GUI定位框架来解决GUI定位中因高分辨率图像、小型UI元素和模糊用户指令带来的挑战。其核心方法是一个包含两个主要组件的端到端推理流程：指令精炼模块和定位模型，并辅以创新的条件性放大策略。

整体框架工作流程如下：首先，指令精炼模块接收原始自然语言指令和GUI截图，利用预训练的视觉语言模型（VLM）将其重写为明确、详细的描述。精炼过程包括两个维度：一是“指令解释”，将高层指令转化为具体的GUI元素操作（例如，将“启动新文件资源管理器”转化为“点击‘新建窗口’选项”）；二是“指令丰富化”，添加视觉特征（如颜色、图标形状）和空间位置（如“位于右上角”）等细节，以消除歧义。随后，定位模型以精炼后的指令和原始截图作为输入，同时输出目标元素的点击坐标和边界框。

该框架的关键技术创新在于其**条件性放大策略**。在推理阶段，系统不会对所有预测都进行二次处理，而是根据首次预测的边界框大小动态决定。具体而言，如果预测的边界框宽度或高度小于预设的较小阈值α，且另一维度小于较大的阈值β，则该元素被判定为“小型”目标。此时，系统会以预测的点击点为中心，对截图区域进行放大，并将放大后的图像再次输入定位模型进行第二轮推理，从而在更清晰的上下文中提升对小图标或文本的定位精度。对于预测边界框较大的简单情况，则直接使用首次预测结果，避免了不必要的计算和上下文信息损失。

在模型训练方面，论文构建了高质量的GUI定位数据集，并采用**分组相对策略优化（GRPO）** 进行训练。奖励函数结合了点击点奖励和边界框奖励，前者确保预测点击坐标位于真实边界框内，后者通过交并比（IoU）衡量边界框预测的准确性。这种多任务训练方式使模型能够协同预测点击动作和元素范围。

综上所述，AdaZoom-GUI通过指令精炼提升语义理解，通过条件性放大增强对小目标的定位能力，并结合GRPO训练策略，在保持计算效率的同时，显著提高了在高分辨率GUI截图上的定位准确率。

### Q4: 论文做了哪些实验？

实验设置方面，作者基于Qwen3-VL-4B-Instruct模型，采用ms-swift框架中的GRPO（Group Relative Policy Optimization）方法训练了定位模型，并使用了Qwen3.5-397B-A17B作为指令精炼模块。评估主要在ScreenSpot-Pro和ScreenSpot-v2两个公开基准上进行，前者包含高分辨率专业领域GUI截图，后者分辨率相对较低。

对比方法包括其他先进的GUI定位模型。主要结果如下：在ScreenSpot-Pro上，仅使用条件放大策略的基础模型平均得分为70.6；结合基于Qwen3.5-397B-A17B的指令精炼模块后，性能提升至76.8，超越了参数量相当的最先进模型，并与更大模型竞争。在ScreenSpot-v2上，基础模型得分为0.943；若采用无条件放大策略，性能下降至0.916；而条件放大策略则提升至0.945，凸显了自适应放大的优势。指令精炼模块单独使用时，系统得分为69.7，已超过原始Qwen3.5-397B-A17B模型的65.6。关键数据指标包括：ScreenSpot-Pro上的最高得分76.8，以及ScreenSpot-v2上条件放大策略带来的0.945平均得分。这些结果表明，AdaZoom-GUI框架在复杂高分辨率GUI场景中有效提升了定位精度和指令理解能力。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，当前框架主要针对单步的GUI元素定位任务，未来可探索多步骤的复杂交互任务，如跨页面的流程自动化，这需要模型具备状态跟踪和规划能力。其次，指令优化模块依赖预训练语言模型，可能受限于其泛化能力；未来可结合用户反馈进行在线学习，使指令描述能动态适应用户表达习惯。此外，条件放大策略的阈值依赖启发式设定，可引入强化学习自适应调整，以平衡精度与效率。从技术整合角度看，可探索将框架与具身智能体结合，实现从屏幕理解到物理交互的闭环。最后，数据集的多样性和规模仍有提升空间，需涵盖更多跨平台、跨语言的GUI场景，以增强模型鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出AdaZoom-GUI，一种基于自适应缩放的GUI定位框架，旨在解决高分辨率GUI截图中元素小、用户指令模糊带来的定位难题。核心贡献包括：1）引入指令精炼模块，将自然语言指令重写为明确详细的描述，使定位模型专注于精确坐标预测而非语义理解；2）设计条件性放大策略，仅当预测元素尺寸较小时触发第二阶段推理，在提升小元素定位精度的同时避免简单案例的冗余计算与上下文丢失；3）构建高质量GUI定位数据集，并采用分组相对策略优化（GRPO）训练模型，使其能同时预测点击坐标与元素边界框。实验表明，该方法在公开基准测试中达到同类参数规模模型的领先性能，为高分辨率GUI理解与实用化GUI智能体部署提供了高效解决方案。
