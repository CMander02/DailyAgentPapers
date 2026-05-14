---
title: "Seg-Agent: Test-Time Multimodal Reasoning for Training-Free Language-Guided Segmentation"
authors:
  - "Chao Hao"
  - "Jun Xu"
  - "Ji Du"
  - "Shuo Ye"
  - "Ziyue Qiao"
  - "Xiaodong Cun"
  - "Guangcong Wang"
  - "Xubin Zheng"
  - "Zitong Yu"
date: "2026-05-13"
arxiv_id: "2605.12953"
arxiv_url: "https://arxiv.org/abs/2605.12953"
pdf_url: "https://arxiv.org/pdf/2605.12953v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Language-Guided Segmentation"
  - "Multimodal Chain-of-Reasoning"
  - "Test-Time Agent"
  - "Visual Reasoning"
  - "Training-Free"
  - "MLLM"
  - "Set-of-Mark"
  - "Seg-Agent"
relevance_score: 8.5
---

# Seg-Agent: Test-Time Multimodal Reasoning for Training-Free Language-Guided Segmentation

## 原始摘要

Language-guided segmentation transcends the scope limitations of traditional semantic segmentation, enabling models to segment arbitrary target regions based on natural language instructions. Existing approaches typically adopt a two-stage framework: employing Multimodal Large Language Models (MLLMs) to interpret instructions and generate visual prompts, followed by foundational segmentation models (e.g., SAM) to produce masks. However, due to the limited spatial grounding capabilities of off-the-shelf MLLMs, these methods often rely on extensive training on large-scale datasets to achieve satisfactory accuracy. While recent advances have introduced reasoning mechanisms to improve performance, they predominantly operate within the textual domain, performing chain-of-thought reasoning solely based on abstract text representations without direct visual feedback. In this paper, we propose Seg-Agent, a completely training-free framework that pioneers Explicit Multimodal Chain-of-Reasoning. Unlike prior text-only reasoning, our approach constructs an interactive visual reasoning loop comprising three stages: generation, selection, and refinement. Specifically, we leverage Set-of-Mark (SoM) visual prompting to render candidate regions directly onto the image, allowing the MLLM to ``see'' and iteratively reason about spatial relationships in the visual domain rather than just the textual one. This explicit multimodal interaction enables Seg-Agent to achieve performance comparable to state-of-the-art training-based methods without any parameter updates. Furthermore, to comprehensively evaluate generalization across diverse scenarios, we introduce Various-LangSeg, a novel benchmark covering explicit semantic, generic object, and reasoning-guided segmentation tasks. Extensive experiments demonstrate the effectiveness and robustness of our method.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决语言引导分割任务中现有方法的两个核心缺陷。研究背景方面，语言引导分割突破了传统语义分割的类别限制，能根据自然语言指令分割任意目标区域。然而，现有方法普遍采用两阶段框架，首先利用多模态大语言模型（MLLM）理解指令并生成视觉提示（如边界框），再交由SAM等基础分割模型生成掩码。现有方法存在明显不足：首先，由于现成MLLM的空间感知能力有限，直接生成的视觉提示质量较低，因此现有方法通常依赖大规模数据集进行昂贵且耗时的监督训练来提升性能；其次，近期引入的推理机制仅停留在文本域中进行思维链推理，缺乏对视觉证据的直接交互和验证。本文要解决的核心问题是：能否在不进行任何训练或参数更新的情况下，通过引入显式的多模态推理机制，在测试时利用视觉反馈循环来迭代修正视觉提示，从而以零训练成本达到与基于训练的方法相当的精度。为此，论文提出了Seg-Agent框架，通过生成-选择-精炼的三阶段交互式推理来直接在视觉域中进行空间关系推理。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **两阶段框架方法**：主流方法如LISA、Sa2VA、GSVA等采用MLLM理解指令后生成特殊<SEG>标记，需微调SAM以适应新型提示；而SAM4MLLM、Seg-Zero则保持SAM冻结，通过后训练MLLM生成SAM可直接理解的边界框或点提示。本文与后两者最为接近，区别在于完全无需训练，通过显式推理链提升视觉提示质量。

2. **端到端联合方法**：PixelLLM、OMG-LLaVA使用自建轻量解码器生成掩码，但性能普遍弱于大规模预训练的SAM。本文则直接采用SAM2作为分割骨干，聚焦于优化MLLM输出的视觉提示。

3. **视觉推理增强方法**：现有推理机制多在文本域进行思维链推理，缺乏视觉反馈。本文首创显式多模态链式推理，通过Set-of-Mark视觉提示将候选区域渲染到图像上，让MLLM在视觉域中迭代推理空间关系，实现训练-free框架与训练方法相当的性能。

### Q3: 论文如何解决这个问题？

Seg-Agent通过构建一种完全无需训练的测试时多模态推理框架来解决现有方法依赖大规模训练的问题。其核心架构包含四个模块：生成模块、选择模块、细化模块和分割模块，形成一个“生成-选择-细化”的迭代推理链。

具体而言，生成模块首先对输入图像应用多种数据增强（如翻转、缩放），得到多个变体，并将每个变体与语言指令一同送入多模态大语言模型（MLLM），生成多个候选边界框。选择模块将这些边界框反变换回原始图像坐标系，通过非极大值抑制去除冗余，然后利用Set-of-Mark（SoM）技术将候选框直接渲染到原始图像上，使MLLM能够在视觉空间中直观比较框与目标的相对位置，从而选出最相关的一个。细化模块对选中的边界框进行精细调整，同样基于SoM渲染的图像，让MLLM根据语义和视觉上下文执行扩展、收缩、平移等操作，以更精确地贴合目标边界。最后，分割模块将细化后的边界框作为视觉提示输入SAM等预训练分割模型，生成最终掩码。

该方法的创新点包括：通过显式多模态链式推理替代传统文本域推理，让MLLM“看见”并迭代优化视觉提示；采用SoM技术增强空间感知能力；全流程无需参数更新，完全利用现成模型，具备强泛化性、可解释性和模块化可扩展性。

### Q4: 论文做了哪些实验？

论文在三个基准测试和自建数据集上进行了实验。实验设置采用QwenVL-2.5作为MLLM基座，SAM2-Large生成分割掩码，无需训练，在单张RTX 4090 GPU上完成推理。评估指标为gIoU和cIoU。

**1. 指代分割实验**：在RefCOCO、RefCOCO+、RefCOCOg数据集上测试显式语义分割。Seg-Agent-7B在RefCOCO testA上cIoU达79.9%，接近训练型SOTA方法Seg-Zero-7B的80.3%，显著优于无推理的基线Qwen2.5-VL-7B+SAM2-L（77.8%）。

**2. 推理分割实验**：在ReasonSeg数据集上测试。Seg-Agent-7B在Val集上gIoU达61.7%，cIoU达61.2%，与Seg-Zero-7B（62.6% / 62.0%）持平，远优于基线（57.6% / 48.3%）。

**3. 多场景泛化实验**：在自建的Various-LangSeg基准上，涵盖显式语义、通用物体和推理引导三种场景。Seg-Agent-7B总体gIoU达70.6%，cIoU达68.5%，在无训练方法中最佳，甚至超过多数训练型方法（如LISA-13B的65.8%）。

**4. 消融实验**：在Various-LangSeg上验证了三阶段模块（生成、选择、细化）的有效性。完整流水线总体gIoU 70.6%，高于缺少任一模块的变体（约68.8%-69.0%），表明显式多模态推理链能逐步提升性能。

**5. 可视化对比**：展示了在多种语言（中/英）、多种图像类型（照片、卡通、AI生成图）上的高质量分割结果，证明其强泛化能力。

### Q5: 有什么可以进一步探索的点？

Seg-Agent在完全无训练框架下取得了令人瞩目的成果，但其局限性和可探索方向依然明确。首先，该方法依赖Set-of-Mark（SoM）生成候选区域，当目标物体密集或边界极其模糊时，候选框的覆盖率和精度可能不足，导致后续推理失败。未来可引入自适应提案生成策略，例如结合视觉显著性检测或低分辨率粗略分割，动态调整SoM的粒度与数量。其次，当前推理过程虽实现了视觉域的“显式链式推理”，但仍局限于前向逐步决策，缺乏反向验证机制。可以构建双向反馈循环：在精炼阶段反向验证所选区域与自然语言指令的语义对齐度，若置信度低则回溯至选代步骤。此外，Seg-Agent仅依赖单一MLLM，可探索多专家协同架构，例如让空间定位较强的MLLM负责提案生成，而语言理解更强的MLLM负责指令解析，并通过置信度投票联合决策。最后，该框架未考虑实时性优化，对于高分辨率视频流或边缘端部署，可将离线SoM预计算与轻量化视觉推理模块结合，在保持零样本能力的同时提升效率。

### Q6: 总结一下论文的主要内容

Seg-Agent提出了一种全新的训练无关框架，用于解决语言引导分割任务中的多模态推理问题。该类任务要求模型根据自然语言指令分割任意目标区域，但现有方法通常依赖大规模训练来弥补多模态大模型（MLLM）空间感知能力不足的缺陷。论文核心贡献在于提出显式多模态推理链，通过生成、选择、优化三个阶段构建交互式视觉反馈回路：首先利用Set-of-Mark（SoM）技术将候选区域渲染到图像上，使MLLM能直接在视觉域中观察和比较候选结果，而非仅依赖文本抽象描述进行推理。这种测试时的闭环视觉推理机制无需任何参数更新即可实现自校正，性能达到甚至超越现有训练方法。此外，作者构建了包含显式语义、通用物体和推理引导三种场景的Various-LangSeg基准，填补了现有评测数据多样性不足的空白。实验表明该方法在多种分割任务中表现出色，为语言引导分割提供了一种低成本、可即时扩展的新范式。
