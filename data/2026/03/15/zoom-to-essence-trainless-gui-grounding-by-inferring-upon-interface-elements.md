---
title: "Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements"
authors:
  - "Ziwei Liu"
  - "Tao Feng"
  - "Borui Kang"
  - "Yanbing Yang"
  - "Jun Luo"
date: "2026-03-15"
arxiv_id: "2603.14448"
arxiv_url: "https://arxiv.org/abs/2603.14448"
pdf_url: "https://arxiv.org/pdf/2603.14448v1"
categories:
  - "cs.LG"
tags:
  - "GUI Agent"
  - "Visual Grounding"
  - "Trainless Method"
  - "Inference Scaling"
  - "Multimodal LLM"
  - "Human-Computer Interaction"
relevance_score: 7.5
---

# Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements

## 原始摘要

Multimodal Large Language Model (MLLM)-based Graphical User Interface (GUI) agents develop rapidly, with visual grounding that maps natural language instructions to target UI elements serving as the core capability. Existing GUI agents typically fine-tune MLLM on massive datasets to handle challenges in understanding instructions and UI interfaces, which not only incurs high data annotation costs but also makes performance dependent on data quality and distribution. To avoid such cumbersome yet ineffective training, we notice that complex UI interfaces can be decomposed into basic visual elements directly understandable by common MLLMs. Consequently, we propose ZoomUI that leverages inference scaling to guide common MLLMs in progressively anchor instruction elements to increasingly detailed interface elements. Specifically, ZoomUI first optimizes the latent thinking to transform original instruction into element visual features description, and subsequently leverages internal attention to iteratively zoom in target element interface region. Evaluations on extensive benchmarks demonstrate that ZoomUI reaches or even surpasses SOTA baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于多模态大语言模型（MLLM）的图形用户界面（GUI）智能体在执行视觉落地任务时面临的核心挑战。研究背景是，GUI智能体需要将用户的自然语言指令精准映射到界面中目标UI元素的空间坐标，以实现点击、定位等操作。然而，在现实场景中，用户指令往往存在歧义，且现代应用界面信息密集、分辨率高，目标元素可能仅占极小像素区域，这导致智能体难以准确定位。

现有方法主要依赖于在海量标注数据上对MLLM进行微调。这种方法存在明显不足：首先，构建大规模高质量的GUI标注数据集成本高昂，无论是人工标注还是借助先进模型（如ChatGPT）都耗费巨大；其次，数据集本身难以避免标注错误和噪声，导致智能体的性能严重依赖于训练数据的质量和分布，泛化能力受限。

因此，本文的核心问题是：能否在不进行任何模型微调（即无需依赖大规模标注数据）的情况下，有效解决指令歧义和复杂界面带来的视觉落地挑战？论文提出的ZoomUI框架正是为了回答这一问题。其核心思路是避免繁琐且效果依赖数据的数据驱动训练，转而利用通用MLLM已有的推理能力，通过“推理缩放”将复杂的GUI落地任务分解为模型可直接理解的基本视觉元素理解步骤。具体而言，它首先通过优化潜在思维向量，将模糊指令转化为对目标元素视觉特征的描述；然后利用模型内部的注意力分布，在生成坐标的过程中迭代地“放大”目标元素所在的界面区域，从而实现无需训练的、精准的GUI视觉落地。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于微调的方法、基于强化学习的方法以及基于推理扩展的方法。

**基于微调的方法**是早期的主流，如OmniParser、OS-Atlas和SeeClick。它们通过在大量标注的UI数据集上对多模态大语言模型（MLLM）进行微调，来实现跨平台GUI的视觉定位。这类方法的核心挑战在于数据标注成本高昂，且性能严重依赖于数据质量和分布。

**基于强化学习的方法**则利用强化学习技术来进一步提升GUI定位能力。例如，一些工作采用群体相对策略优化（GRPO）和高效的奖励策略来增强GUI代理的视觉感知。GUI-AiF和UI-Ins则利用更精细的RL技术来微调MLLM，以应对跨平台多样性和指令理解的瓶颈。此外，FocusUI通过适当减少UI界面中无关的视觉令牌来辅助定位。然而，这些方法同样依赖于大规模数据标注和计算成本高昂的微调过程。

**基于推理扩展的方法**为本文提供了直接灵感。这类方法（如Chain-of-thought、best-of-N采样）旨在不调整模型参数的情况下，通过增加推理时的计算预算（如迭代思考、多次采样）来提升大语言模型的性能，并已在数学推理、代码生成等领域取得成功。在GUI定位领域，DiMo-GUI尝试对文本和图标元素进行分离推理，但依赖于OCR等外部工具的性能；RegionFocus采用固定网格等刚性规则对界面进行缩放，却忽略了MLLM对界面本身的内在理解。

**本文工作（ZoomUI）与这些研究的区别与联系**在于：它与基于推理扩展的方法同属“免训练”范式，都避免了对MLLM进行参数微调。但本文的创新点在于，它不依赖外部工具或刚性规则，而是通过优化潜在思维链将指令转化为对元素视觉特征的描述，并利用模型内部的注意力机制，以迭代缩放的方式逐步锚定目标元素区域，从而更充分地利用通用MLLM本身对界面元素的理解能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ZoomUI的无训练推理框架来解决GUI视觉定位问题，其核心思想是利用通用多模态大语言模型（MLLM）的推理能力，通过渐进式聚焦来锚定目标UI元素，而无需进行耗时的微调。

整体框架分为两个核心阶段：指令精炼和注意力引导的视觉聚焦。首先，针对用户自然语言指令与UI界面视觉特征之间的语义鸿沟，论文设计了“潜在思考”策略。该方法在模型的标准推理流程中注入一组可学习的潜在思考向量，这些向量作为可微分参数，与界面图像嵌入和指令文本嵌入共同构成输入。通过梯度上升法优化这些向量，目标是最大化模型生成目标元素视觉特征描述（如“一个灰色的相机图标”）的置信度。这一过程在模型的潜在空间中进行，不调整模型参数，从而将模糊的用户指令转化为对具体视觉属性的精确描述，为后续定位奠定基础。

其次，为了应对高分辨率UI界面中目标元素像素占比极小的挑战，论文提出了迭代式的注意力引导视觉聚焦机制。该机制不直接让模型预测边界框坐标，而是先分析模型在预测坐标过程中（特别是针对`[`和`,`等触发标记）产生的跨注意力分布图。通过最大池化策略聚合不同注意力头和触发步骤的注意力，得到一个能反映目标元素潜在位置的综合注意力热图。然后，采用滑动窗口计算该热图中注意力分数累积最高的区域，将其从原界面中裁剪并放大，作为下一轮推理的输入视图。这个过程迭代进行，逐步排除无关元素的干扰，并放大目标区域的视觉细节，最终在精细化后的视图上预测出精确的边界框坐标。

该方法的创新点在于：1) **无训练性**：完全依赖推理时优化和注意力分析，避免了昂贵的数据标注和模型微调，性能不依赖于特定数据分布。2) **潜在思考优化**：通过优化可学习的潜在向量来引导模型内部推理，生成可靠的视觉描述，弥合了语义与视觉的差距。3) **迭代注意力聚焦**：创造性利用模型自身的注意力分布作为定位先验，通过“裁剪-放大”的迭代过程实现了从粗到细的渐进式定位，有效解决了高分辨率下的感知难题。

### Q4: 论文做了哪些实验？

论文在四个代表性GUI基准测试上进行了实验，评估其无训练视觉定位方法的性能。实验设置方面，作者使用Qwen2.5-VL-3B-Instruct和Qwen2.5-VL-7B-Instruct作为骨干MLLM，不进行任何微调，仅依靠提出的推理缩放方法。默认配置下，从解码器70%深度层提取注意力分布，窗口大小固定为784x784，最多进行3次迭代，每次将视觉焦点区域裁剪至1/2并通过像素插值放大2倍以保持输入尺寸。

使用的数据集包括：ScreenSpot-Pro（评估专业软件的高分辨率界面）、OSWorld-G（基于真实操作系统界面，含拒绝能力评估）、UI-Vision（评估跨桌面应用的泛化能力）以及MMBench-GUI（涵盖移动、桌面和网页的跨平台综合评估）。评估指标采用点框内准确率，即预测边界框的几何中心是否位于真实框内。

对比方法包括：1）专有模型（GPT-4o、Claude、Gemini-2.5-Pro等）；2）基于微调的GUI智能体（如InfiGUI-R1、GTA1、SE-GUI、GUI-Actor、GUI-G²、UI-Ins、FocusUI等）。主要结果显示，ZoomUI在多个基准上达到或超越了开源模型的SOTA性能。例如，在ScreenSpot-Pro上，ZoomUI-3B平均准确率达40.2%，优于多数同规模模型；ZoomUI-7B达52.8%，与最佳微调模型相当。在OSWorld-G上，ZoomUI-7B平均准确率为54.2%，仅次于Jedi-7B（54.1%）。在UI-Vision上，ZoomUI-7B平均准确率为27.1%，接近最佳模型InfiGUI-G1-7B（26.1%）。但在MMBench-GUI上表现相对不足，作者归因于该数据集指令明确、分辨率适中，更适合利用训练分布知识的微调方法。关键数据指标包括各基准下的细分类别准确率（如文本、图标、元素类型等）及总体平均准确率，凸显了该方法在无需训练数据下的强泛化能力。

### Q5: 有什么可以进一步探索的点？

本文提出的ZoomUI方法虽然取得了显著效果，但其局限性为未来研究提供了明确方向。首先，该方法在MMBench-GUI等指令明确、分辨率适中的基准上表现相对不足，这表明其“渐进式聚焦”策略在处理已内化于MLLM的常见UI元素时，效率可能不如经过大量数据微调的模型。这揭示了其核心局限：依赖推理缩放和内部注意力机制，可能无法充分利用MLLM已有的潜在UI知识，在处理熟悉或结构化的界面时存在优化空间。

未来研究方向可以从以下几个层面展开：1）**混合策略**：探索将无训练推理与轻量级微调（如LoRA）相结合，使模型既能动态分解新界面，又能快速适配特定平台或应用的常见模式。2）**动态迭代机制**：当前迭代次数和缩放比例固定，未来可研究基于指令复杂度或界面信息密度自适应的决策机制，提升效率。3）**多模态理解增强**：除了视觉特征，可融入UI的层级结构、可访问性标签等元信息，辅助模型更精准地定位元素，尤其是在图标等非文本元素上。4）**扩展到复杂任务**：当前聚焦于单元素定位，未来可探索如何将此框架应用于多步骤任务规划，如“点击A后输入B”，实现更完整的GUI智能体能力。这些改进有望在保持其无需训练、泛化性强的优势下，进一步提升在多样化场景下的鲁棒性和精度。

### Q6: 总结一下论文的主要内容

本文提出了一种无需训练的GUI视觉定位方法ZoomUI，旨在解决现有基于多模态大语言模型的GUI智能体依赖大规模标注数据进行微调的问题。核心思路是通过推理缩放机制，引导通用MLLM逐步将自然语言指令与界面元素进行锚定，从而避免昂贵且低效的训练过程。方法上，ZoomUI首先优化潜在思维，将原始指令转化为对元素视觉特征的描述，随后利用内部注意力机制迭代地放大目标元素的界面区域，实现从整体到局部的精确定位。实验表明，该方法在多个基准测试中达到甚至超越了当前最优的基于训练的基线模型，证明了仅通过推理即可实现高效GUI理解的可行性，显著降低了数据依赖与部署成本。
