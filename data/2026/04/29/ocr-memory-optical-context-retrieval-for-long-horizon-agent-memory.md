---
title: "OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory"
authors:
  - "Jinze Li"
  - "Yang Zhang"
  - "Xin Yang"
  - "Jiayi Qu"
  - "Jinfeng Xu"
  - "Shuo Yang"
  - "Junhua Ding"
  - "Edith Cheuk-Han Ngai"
date: "2026-04-29"
arxiv_id: "2604.26622"
arxiv_url: "https://arxiv.org/abs/2604.26622"
pdf_url: "https://arxiv.org/pdf/2604.26622v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Agent Memory"
  - "Long-Horizon Agent"
  - "Visual Context Retrieval"
  - "Agent Architecture"
relevance_score: 8.5
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

## 原始摘要

Autonomous LLM agents increasingly operate in long-horizon, interactive settings where success depends on reusing experience accumulated over extended histories. However, existing agent memory systems are fundamentally constrained by text-context budgets: storing or revisiting raw trajectories is prohibitively token-expensive, while summarization and text-only retrieval trade token savings for information loss and fragmented evidence. To address this limitation, we propose Optical Context Retrieval Memory (OCR-Memory), a memory framework that leverages the visual modality as a high-density representation of agent experience, enabling retention of arbitrarily long histories with minimal prompt overhead at retrieval time. Specifically, OCR-Memory renders historical trajectories into images annotated with unique visual identifiers. OCR-Memory retrieves stored experience via a \emph{locate-and-transcribe} paradigm that selects relevant regions through visual anchors and retrieves the corresponding verbatim text, avoiding free-form generation and reducing hallucination. Experiments on long-horizon agent benchmarks show consistent gains under strict context limits, demonstrating that optical encoding increases effective memory capacity while preserving faithful evidence recovery.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长期交互场景下LLM智能体记忆系统面临的核心矛盾：经验丰富性与上下文窗口限制之间的冲突。现有方法如直接存储原始轨迹会导致token消耗过高，而采用摘要或文本检索压缩则会丢失结构化、时序性或过程性细节，导致信息缺失和证据碎片化，影响复杂下游任务（如调试、错误分析、多步规划）的性能。核心问题是缺乏一种既能完整保留长程交互历史，又能在检索时以极低token开销获取忠实、无幻觉证据的记忆机制。为此，本文提出OCR-Memory，通过将交互轨迹渲染为图像（视觉模态）作为高密度、无损的长期记忆载体，并引入“定位-转录”检索范式，利用视觉锚点进行索引预测而非自由生成，再从外部日志确定性提取原文，从而在严格上下文限制下实现任意长历史的有效保留与忠实检索。

### Q2: 有哪些相关研究？

相关研究可分为三类：**检索式记忆系统**、**经验抽象**和**上下文压缩**。

- **检索式记忆系统**：这类方法将历史交互存储在外部，推理时通过语义检索获取相关片段。本文与其区别在于，OCR-Memory 摒弃了纯文本相似度匹配，采用视觉锚点定位再转录的范式，避免了检索结果在因果或长程依赖任务中的逻辑不相关性问题。
- **经验抽象**：该类工作将轨迹压缩为可复用的技能或工作流。本文指出，抽象虽节省token但会丢失精确错误信息、中间状态等关键细节；而OCR-Memory通过保留完整的视觉化轨迹（高密度图像+可检索原文），实现了细节与检索效率的平衡。
- **上下文压缩**：此类方法通过潜在记忆表征、token修剪等策略压缩历史。本文强调，文本压缩必然存在保真度与压缩率的折中，尤其在多模态场景中会丢失视觉布局信息。OCR-Memory以图像形式存储（高密度、低token开销），检索时才转录必要文本，从根本上避免了信息损失。

### Q3: 论文如何解决这个问题？

OCR-Memory的核心方法是通过光学编码将代理的长期历史轨迹存储为图像，并采用“定位-转录”范式进行检索，从而在有限文本上下文预算下实现高密度记忆存取。整体框架包括外部记忆库、光学检索模块和主代理推理模块。记忆库存储渲染后的轨迹图像、对应的文本段和元数据。关键技术是使用Set-of-Mark提示对图像中的每个文本段标注唯一数字ID和红色边框，将检索任务转化为二进制相关性向量输出（0或1），避免自由文本生成带来的幻觉。检索时，通过解码器logits计算每个段的相关性概率，采用低阈值与Top-K混合的召回优先策略选择相关段，再根据索引从记忆库中精确获取原文文本。创新点包括：多分辨率轨迹机制模拟人类记忆的“从清晰到模糊”特性，对旧记忆自动降采样以降低视觉token成本，当检索到相关段时通过“主动召回放大”立即恢复高分辨率；训练中冻结视觉编码器，仅用LoRA微调解码器，并利用HotpotQA数据集构建二进制标签任务，采用加权二元交叉熵损失偏向高召回率；通过分辨率课程学习模拟推理时的多分辨率条件，增强模型对低分辨率图像的鲁棒性。

### Q4: 论文做了哪些实验？

论文在多个实验设置下系统评估了OCR-Memory。主要实验包括：在Mind2Web（Cross-Task split）和AppWorld（重点Hard子集）基准上，以4096 token为上下文预算，对比Zero-Shot、文本检索（RAG）、MemoryBank、AWM和ACON五种基线。主要结果：OCR-Memory在Mind2Web上达到53.8% Element Accuracy和46.1% Step Success Rate（Task SR 4.8%），显著优于AWM（49.1%/41.2%）；在AppWorld上平均成功率58.1%，Hard子集达30.8%（RAG仅21.4%，AWM 27.2%）。消融实验验证了Set-of-Mark的核心作用（移除后精度下降，且文本生成变种延迟增至5.3s）和多分辨率动态召回策略（动态策略以82 tokens/帧达到46.1% Step SR，接近静态高分辨率的46.5%但节省大量token）。在token限制实验中，OCR-Memory在1024-8192 token范围内一致优于RAG。RULER NIAH测试显示，其原始检索准确性在4k上下文达98.5%，32k时仍保持94.1%，压缩比超10×。背骨泛化实验在Qwen3-32B上验证了优势保持（48.6% vs 35.2% Ele Acc）。检索级评估中Recall@1达78.6%（Dense Text-RAG仅52.7%），内容忠实度达100%（文本生成变种仅84.3%）。系统效率分析表明，每步推理token从3980降至596，但存储增至1.47MB/episode，延迟增至1.7s。

### Q5: 有什么可以进一步探索的点？

论文可进一步探索的方向包括：一是降低OCR-Memory的额外训练成本，可尝试利用预训练的视觉-语言模型（如CLIP）替代专用检索模型，实现零样本或轻量级微调；二是优化渲染与存储效率，例如采用动态图像压缩、稀疏帧采样或文本-图像混合存储策略，减少计算和磁盘开销；三是探索更紧凑的视觉编码方案，如将历史轨迹编码为结构化草图或图标序列，在保持高信息密度的同时降低存储和推理负载。此外，当前方法主要依赖视觉锚点定位文本，未来可研究如何融入跨模态关联推理（如时序依赖、因果链），以处理更复杂的长期上下文绑定任务。最后，将OCR-Memory扩展到多模态代理场景（如具身机器人或GUI操作代理）中，验证其在物理世界交互记忆中的泛化能力，并解决视觉歧义性（如图像遮挡、尺度变化）带来的检索噪声问题。

### Q6: 总结一下论文的主要内容

该论文提出OCR-Memory，一种利用视觉模态作为高密度表示来增强LLM智能体长程记忆的框架。问题在于现有记忆系统受限于文本上下文预算，存储完整轨迹代价高昂，而摘要和纯文本检索则导致信息丢失和碎片化。方法上，OCR-Memory将智能体的完整交互历史渲染为带有独特视觉锚点（如索引边界框）的图像，通过“定位-转录”范式检索：模型扫描视觉记忆预测相关片段索引，再确定性提取对应原始文本，避免自由生成带来的幻觉。此外，采用自适应分辨率策略将旧轨迹以低分辨率缩略图存储，并通过主动召回上采样恢复高保真细节。在Mind2Web和AppWorld基准上的实验表明，该方法在严格上下文限制下持续优于现有方法，显著提升了有效记忆容量和证据恢复的保真度。核心贡献在于首次将图像模态用于智能体记忆，实现了无损、低token开销的长程经验存储与检索。
