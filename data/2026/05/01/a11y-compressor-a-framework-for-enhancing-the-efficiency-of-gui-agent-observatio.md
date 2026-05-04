---
title: "A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction"
authors:
  - "Michito Takeshita"
  - "Takuro Kawada"
  - "Takumi Ohashi"
  - "Shunsuke Kitada"
  - "Hitoshi Iyatomi"
date: "2026-05-01"
arxiv_id: "2605.00551"
arxiv_url: "https://arxiv.org/abs/2605.00551"
pdf_url: "https://arxiv.org/pdf/2605.00551v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Observation Representation"
  - "Accessibility Tree"
  - "Input Compression"
  - "Efficiency"
  - "OSWorld Benchmark"
relevance_score: 8.5
---

# A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction

## 原始摘要

AI agents that interact with graphical user interfaces (GUIs) require effective observation representations for reliable grounding. The accessibility tree is a commonly used text-based format that encodes UI element attributes, but it suffers from redundancy and lacks structural information such as spatial relationships among elements. We propose A11y-Compressor, a framework that transforms linearized accessibility trees into compact and structured representations. Our implementation, Compressed-a11y, applies a lightweight and structured transformation pipeline with modal detection, redundancy reduction, and semantic structuring. Experiments on the OSWorld benchmark show that Compressed-a11y reduces input tokens to 22% of the original while improving task success rates by 5.1 percentage points on average.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决本地部署的开源多模态大语言模型（MLLM）在图形用户界面（GUI）代理任务中，因观测表示效率低下而导致的基础定位（grounding）困难问题。当前主流的基于文本的GUI观测表示，如可访问性树（a11y tree），虽能编码UI元素属性，但存在两大显著不足：首先，其层级结构与视觉布局不匹配，难以捕获元素间的空间关系与语义区域；其次，该表示包含大量冗余信息（如视觉隐藏元素、重复标签、冗长文本），导致令牌（token）消耗高，分散模型注意力。现有方法如元素选择或线性化处理，仅部分缓解冗余，但未能保留空间顺序与内在GUI结构。特别是广泛使用的线性化a11y树，还会引发不必要的点击坐标推断、模态UI层级混淆等问题。因此，本文核心目标是设计一个能从线性化a11y树出发，生成紧凑且结构化的观测表示框架，以大幅减少令牌消耗的同时提升基础定位准确性，从而增强本地MLLM在GUI任务上的可部署性与实际成功率。

### Q2: 有哪些相关研究？

相关研究可归为以下几类：**观察表示方法类**包括图像法（直接处理截图，如视觉语言模型，定位弱但视觉丰富）和文本法（基于可访问性树的元素角色、属性、位置，定位准确但冗余）。本文属于文本法改进，区别在于同时处理冗余和结构缺失。**混合方法**尝试结合图像与文本，但计算成本高，本文侧重纯文本优化。**可访问性树压缩**方面，现有工作如元素过滤、属性选取、线性化主要减少冗余和 token（类似冗余降低），但忽视层级结构与视觉布局的匹配，丢失空间语义。本文提出的 A11y-Compressor 创新在于通过模态检测、冗余降低和语义结构化构建紧凑且保留结构信息的表示，区别于仅压缩不重组的方案。**应用评测类**如 OSWorld 基准，本文在此验证压缩率（降至22%）和任务成功率提升（+5.1%）。整体上，本文定位在保留语义的轻量级压缩，区别于仅过滤或线性化的简单方法。

### Q3: 论文如何解决这个问题？

A11y-Compressor 通过一个三阶段的结构化流水线将线性化的无障碍树转换为紧凑且语义连贯的 GUI 观察表示。核心方法是：首先进行模态检测，识别前景模态元素（如弹窗）并将其与背景元素分离，明确交互约束，解决无障碍树中模态与背景元素并列排列的问题。然后进行冗余缩减，通过基于规则的预处理，包括过滤无关元素、去重、归一化属性、将边界框坐标转换为中心坐标以及压缩文本，减少输入长度并消除歧义。最后进行语义结构化，识别当前界面的应用归属，根据空间布局和应用特定的启发式规则将 UI 元素划分为语义区域（如任务栏、导航面板），从而显式提供 GUI 的功能结构信息。创新点在于其模块化设计，允许每个阶段采用不同算法实现，并且通过显式分离模态元素、减少冗余和增加语义信息，使最终观察表示在保持关键结构的同时，将输入 token 压缩到原始大小的 22%，并在 OSWorld 基准上平均提升 5.1 个百分点的任务成功率。

### Q4: 论文做了哪些实验？

论文在OSWorld基准测试上进行了实验，使用358个任务（排除环境错误后），涵盖Chrome、LibreOffice、GIMP、VLC、VS Code等多个应用域。采用Qwen3-VL-32B作为MLLM推理模型。对比方法包括：原始截图、线性化a11y树、动态选择相关行的LineRetriever。主要结果：Compressed-a11y将输入token减少至原始的22%（约3500以内），优于其他文本表示；任务成功率上，Compressed-a11y平均为0.207，超过截图（0.070）、线性化a11y树（0.156）和LineRetriever（0.151），尤其在Writer（0.304）和Thunderbird（0.467）表现突出。消融实验显示，完整三阶段管线（模态检测、冗余缩减、语义结构化）整体成功率最高（0.207），优于单一阶段（模态检测仅0.134、冗余缩减仅0.156、语义结构化仅0.134）。此外，定性案例分析证明Compressed-a11y能正确处理模态对话框，避免坐标错位或背景交互失败问题。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，框架仅基于线性化无障碍树，无法利用图标形状、颜色等视觉信息，这可能限制在依赖视觉线索的任务中的效果；其次，当前评估仅在OSWorld基准的桌面应用上完成，未涉及移动界面等其他环境；最后，Compressed-a11y实现依赖基于规则和启发式阈值的设计，鲁棒性和泛化能力受限。

未来可从以下方向扩展：一是引入学习型压缩策略，例如训练一个轻量级模型来自适应地识别和压缩冗余内容，替代固定阈值；二是融合视觉模态，通过在压缩表示中嵌入视觉特征（如图标语义嵌入），弥补无障碍树的信息缺失；三是探索跨平台泛化，针对移动或Web界面设计可迁移的模态检测与结构化规则。此外，当前方法依赖全局结构保留，但过度结构化可能引入噪声，未来可研究动态压缩率调节，根据任务复杂度或交互阶段自适应调整表示粒度，以平衡效率与信息完整性。

### Q6: 总结一下论文的主要内容

A11y-Compressor 是一个旨在提升 GUI 代理效率的框架，其核心贡献在于解决了线性化无障碍树（a11y tree）存在的冗余和缺乏结构信息的问题。该问题定义是：为 GUI 代理构建高效且准确的观察表示，以提升其与图形用户界面交互时的接地（grounding）能力。方法上，A11y-Compressor 通过一个轻量级的结构化转换管道，包括模态检测、冗余缩减和语义结构化三步，将线性化的 a11y 树转化为紧凑且有结构的 Compressed-a11y 表示。主要结论是，在 OSWorld 基准测试中，Compressed-a11y 将输入 tokens 减少至原来的 22%，同时将任务成功率平均提升了 5.1 个百分点。该研究的重大意义在于，它证明了通过精心设计的结构化和压缩策略，可以在显著降低计算成本的同时，提升 GUI 代理在复杂用户界面上的任务执行性能，为更高效、更可靠的 GUI 代理设计提供了新方向。
