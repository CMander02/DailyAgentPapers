---
title: "Stateful Visual Encoders for Vision-Language Models"
authors:
  - "Zirui Wang"
  - "Junwei Yu"
  - "Adam Yala"
  - "David M. Chan"
  - "Joseph E. Gonzalez"
  - "Trevor Darrell"
date: "2026-06-03"
arxiv_id: "2606.04433"
arxiv_url: "https://arxiv.org/abs/2606.04433"
pdf_url: "https://arxiv.org/pdf/2606.04433v1"
categories:
  - "cs.CV"
  - "cs.CL"
  - "cs.LG"
tags:
  - "VLM agent"
  - "stateful visual encoder"
  - "multi-turn agent"
  - "visual memory"
  - "fine-grained visual comparison"
relevance_score: 8.0
---

# Stateful Visual Encoders for Vision-Language Models

## 原始摘要

Vision-language models (VLMs) are increasingly used in multi-image, multi-turn agentic settings where decisions depend on visual changes. However, in existing open-weight VLMs, visual comparisons happen only inside the language model, while the visual encoder itself remains stateless: each image is encoded independently, without access to the prior visual context. As a result, small but task-critical changes may be attenuated before the language model has a chance to compare them, especially when those changes do not affect the high-level semantics of the scene. We introduce a Stateful Visual Encoder, which conditions each visual representation on prior visual features. Under supervised finetuning, VLMs equipped with stateful encoders achieve consistent improvements on controlled tasks involving cross-image spatial aggregation, multi-object visual differencing, and visual trajectory behavior cloning. These improvements are consistent across input resolutions, language model sizes, and VLM backbones. Finally, we validate our model on real-world tasks, including longitudinal radiology, fine-grained image comparison, and remote sensing, where stateful encoders consistently improve generalist VLM baselines and can match or surpass specialized models in selected domains. Project page: https://statefulvisualencoders.github.io/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决现有视觉-语言模型（VLM）在处理多图像、多轮交互任务时，视觉编码器缺乏状态记忆的问题。当前主流的开源VLM架构中，视觉编码器是无状态的，每张图像被独立编码，不参考任何先前的视觉上下文。这种设计导致视觉比较任务只能在语言模型内部进行，当图像间变化细微（如医学影像中病灶的新现或消散、卫星图像中小目标变化、图像编辑中局部属性修改）时，独立编码的过程可能抑制这些关键的低级视觉差异，使得语言模型在比较时已丢失重要信息。

现有方法的不足在于，视觉编码器的预训练目标（如语言对齐或自监督学习）侧重于图像的高层语义，独立编码机制无法主动捕捉跨图像的细粒度变化。这限制了VLM在需要严格视觉对比的实际场景（如时序放射学分析、细粒度图像比较、遥感变化检测）中的表现。

本文提出的Stateful Visual Encoder通过向视觉编码器中注入跨图像交互机制（如扩展自注意力上下文或引入交叉注意力），使当前视觉表示能够条件化于先前的视觉特征。在监督微调框架下，该方法在不替换骨干网络或从头训练的情况下，实现了视觉编码器的状态化，从而在编码阶段就感知历史视觉信息，显著提升了多图空间聚合、多目标视觉差异检测和视觉轨迹行为克隆等任务的性能，并在多个真实世界领域中匹配或超越专用模型。

### Q2: 有哪些相关研究？

1. **图像差异编码器 (Image Difference Encoders):** 这类专用模型（如变化检测模型）在视觉编码器内部进行图像比较。与之不同，本文提出的状态型视觉编码器 (SVE) 并非为特定变化检测任务设计，而是作为视觉语言模型 (VLM) 的通用视觉编码器进行研究，旨在提升 VLM 在多种任务上的跨图像理解能力。

2. **视频视觉编码器 (Video Visual Encoders):** 如 I3D、MViT、VideoMAE 等，它们从帧序列中学习时空表征。与这些需要处理连续视频流的编码器不同，SVE 专门针对接收多个独立图像（如前后对比图、交互状态）的 VLM。SVE 通过在现有图像编码器中引入因果性跨图像条件机制（当前图像特征基于前一个图像特征），更适合离散的、多图像交互场景，且不破坏原有 VLM 的视觉接口。

3. **VLM 中的多图像编码 (Multi-Image Encoding in VLMs):** 现有方法如 MANTIS、LLaVA-OneVision 等大多采用“晚期融合”，即独立编码每张图像，将跨图像比较完全留给语言模型。SVE 解决了一个互补的瓶颈：在视觉特征序列化输入给大语言模型 (LLM) 之前，SVE 就允许当前图像在视觉骨干网络中检索并整合先前图像的视觉特征，从而更早且更有效地捕捉跨图像变化。

### Q3: 论文如何解决这个问题？

为了解决现有视觉语言模型（VLM）中视觉编码器无状态、无法感知跨图像视觉上下文的问题，论文提出了**有状态视觉编码器（Stateful Visual Encoder, SVE）**。其核心思想是在编码当前图像时，显式地将先前图像的视觉特征作为条件输入，使编码器能够感知视觉变化。

整体框架基于标准的VLM架构（视觉编码器 \( f_V \)、连接器 \( W \)、大语言模型 \( f_L \)）。论文设计了四种SVE实现方案进行对比：
1.  **Self-Ext**：将前一张图像的键值对直接拼接到当前图像自注意力层的键值集合中。
2.  **AdaLN-Zero**：通过自适应归一化，将前一张图像的池化特征作为调制信号，调节当前层的注意力与前馈网络。
3.  **Cross**：在每个预训练自注意力层前插入一个完整的交叉注意力层，以当前图像特征为查询，前一张图像特征为键/值。
4.  **Cross+FFN**：在Cross的交叉注意力层后额外增加一个前馈网络块，以增强特征变换能力。

关键技术包括：
- **参数初始化**：新增交叉注意力层的输入投影从对应自注意力层复制，输出投影零初始化，以保持预训练编码器初始行为，稳定训练。
- **梯度停止**：在交叉注意力变体中，对来自前一张图像的键/值分支应用梯度停止（stop-gradient），仅更新当前查询分支与状态条件参数，防止上下文特征的表示崩塌。
- **注意力机制**：交叉注意力变体执行逐token的跨图像特征检索，相比Self-Ext的拼接或AdaLN-Zero的池化，能更精细地捕捉细微视觉变化。

实验表明，**Cross+FFN** 是最优设计，在跨图像空间聚合、多物体视觉差异和视觉轨迹行为克隆等任务上一致超过无状态基线，且通过控制实验验证了零初始化和梯度停止策略的有效性。

### Q4: 论文做了哪些实验？

在实验中，论文首先对状态表征进行特征分析。通过比较Stateful Visual Encoder（SVE）与等参数量的无状态基线（使用自注意力替代时间交叉注意力），在CLEVR-Change数据集上评估。结果显示SVE的特征对前驱图像变化敏感，而基线保持不变；在SVE与基线预测不一致的样本中，SVE的胜率（WinRate）显著更高；跨图像特征更新呈现空间稀疏性，仅少数视觉token吸收大部分变化。 其次，论文在三个真实世界任务中验证SVE：(1) 纵向放射学：使用Medical-Diff-VQA数据集，对比Qwen3.5 4B SFT基线。SVE在BLEU-4（49.6 vs 47.9）、METEOR（40.9 vs 40.6）、ROUGE-L（66.3 vs 62.7）、CIDEr（178.9 vs 145.1）、Finding-level Micro F1（32.20 vs 31.55）、Macro F1（12.45 vs 11.95）和Change Accuracy（89.21 vs 86.83）上全面领先。(2) 细粒度图像比较：定性示例表明SVE正确描述编辑后差异，基线则出错。(3) 遥感：定性示例显示SVE正确识别变化，基线遗漏或错误描述。此外，SVE在跨图像空间聚合、多对象视觉差异和轨迹行为克隆等受控任务上也有持续改进，且效果在不同分辨率、语言模型大小和VLM骨干上一致。

### Q5: 有什么可以进一步探索的点？

该工作的主要局限性在于状态编码器的设计相对简单，仅通过线性投影和历史特征的简单拼接来实现，缺乏更复杂的时序建模机制。未来可探索引入门控循环单元或Transformer时序编码层来捕获长期视觉依赖，特别是在多轮交互中能更好地区分累积变化与瞬态噪声。另一个方向是研究状态重置或遗忘机制，当场景发生根本性变化（如用户切换任务）时，视觉编码器可能需要清除历史状态以避免干扰。此外，当前方法依赖人工标注的配对数据，可进一步探索自监督预训练策略，如通过视频帧间的自然时序关系或模拟的视觉变化进行预训练，减少对标注数据的依赖。最后，可探索将状态编码扩展到多模态对齐阶段，使视觉状态与语言上下文形成双向条件，提升复杂推理任务的性能。

### Q6: 总结一下论文的主要内容

论文提出了一种名为“有状态视觉编码器”（Stateful Visual Encoder, SVE）的方法，用于解决现有视觉-语言模型（VLM）在处理多图像任务时视觉编码器无状态的问题。现有VLM将每张图像独立编码，导致关键视觉变化（如医学影像中的细微病灶）在语言模型比较之前就被弱化。SVE通过在视觉编码器内引入跨图像交互（如扩展自注意力上下文或交叉注意力），使当前图像的视觉表示能够参考历史视觉特征，从而实现早期细粒度比较。实验表明，在监督微调下，SVE在跨图像空间聚合、多目标差异检测等合成任务上持续提升性能，并在放射学、图像编辑和遥感等真实场景中超越通用VLM基线，甚至匹敌或超越专门模型。该方法跨分辨率（256²-768²）、模型规模（0.8B-9B）及多种VLM架构（如Qwen3-VL、InternVL3.5）均表现稳健。核心贡献在于提出轻量级架构扩展，无需从头训练即可赋予VLM跨图像比较能力，显著提升了动态视觉推理任务的实用性。
