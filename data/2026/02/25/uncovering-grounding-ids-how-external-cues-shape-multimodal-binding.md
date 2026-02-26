---
title: "Uncovering Grounding IDs: How External Cues Shape Multimodal Binding"
authors:
  - "Hosein Hasani"
  - "Amirmohammad Izadi"
  - "Fatemeh Askari"
  - "Mobin Bagherian"
  - "Sadegh Mohammadian"
  - "Mohammad Izadi"
  - "Mahdieh Soleymani Baghshah"
date: "2025-09-28"
arxiv_id: "2509.24072"
arxiv_url: "https://arxiv.org/abs/2509.24072"
pdf_url: "https://arxiv.org/pdf/2509.24072v4"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "多模态模型"
  - "视觉语言模型"
  - "基础模型"
  - "表示学习"
  - "可解释性"
  - "跨模态对齐"
relevance_score: 5.5
---

# Uncovering Grounding IDs: How External Cues Shape Multimodal Binding

## 原始摘要

Large vision-language models (LVLMs) show strong performance across multimodal benchmarks but remain limited in structured reasoning and precise grounding. Recent work has demonstrated that adding simple visual structures, such as partitions and annotations, improves accuracy, yet the internal mechanisms underlying these gains remain unclear. We investigate this phenomenon and propose the concept of Grounding IDs, latent identifiers induced by external cues that bind objects to their designated partitions across modalities. Through representation analysis, we find that these identifiers emerge as consistent within-partition alignment in embedding space and reduce the modality gap between image and text. Causal interventions further confirm that these identifiers mediate binding between objects and symbolic cues. We show that Grounding IDs strengthen attention between related components, which in turn improves cross-modal grounding and reduces hallucinations. Taken together, our results identify Grounding IDs as a key symbolic mechanism that explains how external cues enhance multimodal binding and offer both interpretability and practical improvements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型视觉-语言模型（LVLMs）在利用外部结构化提示（如网格线、符号标注）时，其内部工作机制如何改善跨模态对齐与推理能力。研究背景是，尽管LVLMs在多模态任务上表现出色，但在结构化推理和精确指代方面仍存在局限，容易产生幻觉错误。现有方法（如添加形状标注或网格线）已被证明能提升模型性能，但其内部作用机制尚不明确，这构成了当前研究的关键空白。

本文的核心问题是：外部视觉和文本线索如何通过模型内部表征来增强多模态绑定，从而提升性能？具体而言，论文提出了“Grounding IDs”这一概念，指代由外部线索诱导产生的潜在标识符，它们能在嵌入空间中将对象与其指定的分区跨模态地绑定起来。通过表征分析和因果干预，论文揭示了这些标识符如何作为一致的分区内对齐机制出现，缩小了图像与文本之间的模态鸿沟，并中介了对象与符号线索之间的绑定。最终，论文阐明Grounding IDs通过加强相关组件间的注意力，改善了跨模态指代并减少了幻觉，从而为外部线索提升多模态绑定提供了关键的解释性机制。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、机制解释类和评测类。

在**方法类**工作中，先前研究表明，添加外部视觉结构（如分割线和标注）并结合思维链式提示，能显著提升视觉语言模型在计数、几何推理等任务上的表现。例如，VISER 引入了与输入无关的通用视觉结构（如水平线）和顺序扫描提示，以促进结构化推理。本文在此基础上，进一步探究这些外部线索如何通过内部机制提升模型性能。

在**机制解释类**工作中，近期研究利用机制可解释性方法，发现大语言模型通过“绑定ID”来连接实体与其属性。后续工作将这一概念扩展到视觉语言模型，证明了其在简单图像中连接视觉对象与文本引用的类似机制。然而，这些研究局限于接地（grounding）任务简单的场景。本文的核心贡献在于，针对更复杂、跨模态错位更显著的情景，提出了“接地ID”的概念，以解释外部线索如何通过诱导跨模态的绑定标识来增强推理。

在**评测类**工作中，已有研究揭示了LVLMs在形状识别等方面的局限性（如“形状盲”），并展示了外部标注如何提升准确性。本文的评测则侧重于通过表征分析和因果干预实验，实证“接地ID”的存在及其在减少幻觉、改善跨模态对齐方面的作用。

本文与这些工作的关系在于，它建立在利用外部结构提升性能的方法之上，并借鉴了机制解释领域中“绑定ID”的思想。其区别在于，本文首次系统地提出了“接地ID”作为解释外部线索生效机制的关键概念，并在更复杂的多模态绑定场景中，通过实验验证了其存在、作用及其对减少模态鸿沟的贡献。

### Q3: 论文如何解决这个问题？

论文通过提出并验证“Grounding IDs”这一概念来解决外部线索如何增强多模态绑定的问题。核心方法是结合表征分析和因果干预，揭示外部结构线索（如符号和分区线）在大型视觉语言模型（LVLM）内部诱导出隐式标识符，从而改善跨模态对齐。

整体框架基于一个7B参数的Qwen2.5-VL模型，在推理时（无需微调）使用两种输入设置进行对比：基线（原始图像和标准提示）与结构化输入（在图像和提示中添加四个符号&、#、$、@，并用三条水平线将图像分为四个分区）。研究在合成数据集上进行，该数据集包含由不同形状-颜色组合构成的物体，每个物体位于独立的分区内。

主要模块和分析包括：
1.  **表征对齐分析**：通过计算视觉与文本嵌入的余弦相似度，发现结构化输入在模型深层（特别是22-27层）显著减少了模态间隙，提升了跨模态对齐。符号嵌入本身比物体嵌入表现出更强的对齐。
2.  **注意力模式分析**：通过分析跨模态注意力矩阵，发现结构化输入导致注意力更集中于对角线区域（即同一分区内），表明分区内的绑定更强。
3.  **因果干预实验**：这是验证Grounding IDs因果作用的关键。设计激活交换实验：从两个不同的上下文（源上下文c‘和目标上下文c）中，随机选择两个符号（如&和@），交换它们对应物体在所有层的激活，生成修补后的上下文c*。实验发现，模型在c*中的预测会遵循从源上下文转移过来的符号-物体绑定关系，而忽略修补后图像中物体实际所处的局部符号位置。这直接证明符号绑定信息被编码在物体激活中并因果地介导了预测。
4.  **层间与注意力头分析**：使用Logit Lens技术发现，模型在深层（20-27层）开始倾向于预测被转移绑定的物体（而非局部物体）。同时，通过计算信号噪声比，识别出某些中间层（如第16层）的注意力头专门负责传播Grounding IDs，它们会更多地关注与符号绑定的物体，而非仅仅空间相邻的物体。
5.  **Grounding IDs特性探究**：分析表明，符号之间的差异向量与它们所诱导的Grounding IDs之间的差异向量高度相似，支持了其类似于词汇绑定的机制。即使目标上下文使用与源上下文完全不相交的符号集，激活交换后模型仍能基于源符号做出正确预测，进一步证明了Grounding IDs的抽象性和可转移性。

创新点在于首次提出并因果性地验证了“Grounding IDs”这一机制，解释了简单外部结构提升模型性能的内在原因。该方法不仅提供了可解释性见解，表明绑定是通过抽象标识符在深层表征中实现的，也为未来设计更有效的视觉提示或模型改进提供了理论基础。

### Q4: 论文做了哪些实验？

论文实验主要分为三部分，旨在验证外部线索如何通过诱导“Grounding IDs”来增强多模态绑定。

**实验设置与数据集**：主要使用Qwen2.5-VL 7B等模型，在推理时进行分析，无需微调。核心数据集是合成的图像集，包含由不同形状-颜色组合构成的独特物体（如10、15、20个物体），并放置在划分好的分区（如四行）中。在结构化输入设置中，图像被水平线分割并添加符号（&、#、$、@），提示词也相应修改。此外，实验也使用了MS-COCO等大规模基准。

**对比方法**：主要对比**基线方法**（原始图像和标准提示）与**结构化输入方法**（添加分区线和符号）。在行为影响实验中，还与专门的幻觉缓解方法（如OPERA、VCD、SPARC）以及VISER等方法进行了比较。

**主要结果与关键指标**：
1.  **对齐与注意力分析**：结构化输入导致注意力矩阵更强的对角线主导性，表明注意力更集中在分区内部。跨模态嵌入余弦相似度在后期网络层（如22-27层）更高，证实外部线索减少了模态间隙。
2.  **因果证据**：通过激活交换干预实验，模型在干预后的上下文（c*）中，高达**98%** 的准确率遵循从源上下文转移而来的符号-物体绑定，而非本地物理位置，证明了Grounding IDs的因果媒介作用。层间logit差异分析显示，在20-27层，模型开始显著倾向于绑定对象。
3.  **行为影响**：
    *   **幻觉缓解**：在合成场景描述任务中，结构化输入（尤其是图文双模态线索）显著提升了各项指标。例如，在20个物体的任务中，结构化输入（both）的F1分数达到**0.62**，远高于基线的**0.21**。在MS-COCO上，结构化方法将LLaVA-1.5的CHAIR_s从51.60%降至**41.00%**，将Qwen2.5-VL的CHAIR_i从7.97%降至**5.36%**，优于或匹配对比方法。
    *   **视觉推理**：在计数和视觉搜索任务上，基于Grounding IDs的方法提升了所有测试模型的准确率。例如，Qwen2.5-VL 7B的计数准确率从基线的29.67%提升至**53.00%**，视觉搜索准确率从30.00%提升至**52.25%**，均超过了VISER基线。

### Q5: 有什么可以进一步探索的点？

本文揭示了外部线索通过诱导“Grounding IDs”来增强多模态绑定的机制，但仍存在局限和可拓展方向。首先，研究主要依赖简单的、内容无关的结构（如分区和标注），这些线索在真实开放场景中可能不存在或更复杂，未来需探索如何让模型在缺乏显式外部提示时自发形成类似的 grounding 机制，或适应更自然的视觉结构。其次，论文聚焦于静态图像描述和基础视觉推理，未来可深入探究 Grounding IDs 在需要系统 2 推理的复杂任务（如计数、空间关系推理、多步规划）中的作用机制，并识别支持这些任务的专用神经回路。此外，当前方法主要基于观测和因果干预进行分析，未来可将这种机制主动应用于模型训练中，例如在强化学习微调阶段融入结构化外部线索，以显式增强模型基于线索进行序列化扫描和推理的内部能力。最后，研究为多模态模型的可解释性提供了工具，但 Grounding IDs 的形成与泛化能力之间的关系尚不明确，未来可研究其在跨领域、跨任务迁移中的表现，以及如何设计更优的线索以最大化 grounding 效果。

### Q6: 总结一下论文的主要内容

该论文探讨了大型视觉语言模型（LVLMs）中外部视觉结构（如分区和标注）如何提升多模态绑定性能的内部机制。核心贡献是提出了“Grounding IDs”的概念，即由外部线索诱导产生的潜在标识符，它们能在不同模态间将对象绑定到指定的分区。

研究问题在于，尽管已知添加简单视觉结构能提高模型精度，但其内在作用原理尚不明确。方法上，作者通过表征分析发现，这些标识符在嵌入空间中表现为分区内的一致性对齐，并缩小了图像与文本之间的模态鸿沟。进一步的因果干预实验证实，Grounding IDs 介导了对象与符号线索之间的绑定。

主要结论是，Grounding IDs 作为一种关键的符号机制，通过增强相关组件间的注意力，改善了跨模态的 grounding 能力，并减少了幻觉现象。这项工作不仅为外部线索如何增强多模态绑定提供了可解释的机制，也为模型的实际改进提供了方向。
