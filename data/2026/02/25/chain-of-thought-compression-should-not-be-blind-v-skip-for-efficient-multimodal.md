---
title: "Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring"
authors:
  - "Dongxu Zhang"
  - "Yiding Sun"
  - "Cheng Tan"
  - "Wenbiao Yan"
  - "Ning Yang"
  - "Jihua Zhu"
  - "Haijun Zhang"
date: "2026-01-20"
arxiv_id: "2601.13879"
arxiv_url: "https://arxiv.org/abs/2601.13879"
pdf_url: "https://arxiv.org/pdf/2601.13879v3"
categories:
  - "cs.MM"
  - "cs.CL"
  - "cs.CV"
tags:
  - "多模态推理"
  - "推理加速"
  - "思维链"
  - "视觉语言模型"
  - "信息瓶颈"
  - "效率优化"
  - "视觉锚定"
relevance_score: 7.5
---

# Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring

## 原始摘要

While Chain-of-Thought (CoT) reasoning significantly enhances the performance of Multimodal Large Language Models (MLLMs), its autoregressive nature incurs prohibitive latency constraints. Current efforts to mitigate this via token compression often fail by blindly applying text-centric metrics to multimodal contexts. We identify a critical failure mode termed Visual Amnesia, where linguistically redundant tokens are erroneously pruned, leading to hallucinations. To address this, we introduce V-Skip that reformulates token pruning as a Visual-Anchored Information Bottleneck (VA-IB) optimization problem. V-Skip employs a dual-path gating mechanism that weighs token importance through both linguistic surprisal and cross-modal attention flow, effectively rescuing visually salient anchors. Extensive experiments on Qwen2-VL and Llama-3.2 families demonstrate that V-Skip achieves a $2.9\times$ speedup with negligible accuracy loss. Specifically, it preserves fine-grained visual details, outperforming other baselines over 30\% on the DocVQA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型（MLLMs）在进行思维链（CoT）推理时，因自回归生成冗长序列而导致的计算延迟过高的问题。研究背景是，尽管CoT推理显著提升了MLLMs（如LLaVA、Qwen-VL）在复杂视觉问答中的性能和可解释性，但其逐词生成特性使得键值（KV）缓存线性增长，带来了严重的计算开销和延迟，限制了吞吐量和实际应用。

现有方法的不足在于，为提升效率而采用的令牌压缩技术（如TokenSkip、LLMLingua-2）大多源自纯文本领域，它们盲目地依赖语言模型的统计概率（如“惊奇度”）来判定令牌冗余性并进行剪枝。然而，在多模态上下文中，这种纯文本中心的压缩方法会导致一个关键故障模式，即论文提出的“视觉遗忘”现象：一些在语言上可预测（因此被判定为冗余）的令牌（例如描述物体颜色、形状的形容词），实际上在视觉推理中是至关重要的“视觉锚点”。错误剪枝这些锚点会割裂推理过程与输入图像的关联，导致模型产生幻觉（如物体属性错误）。

因此，本文要解决的核心问题是：如何高效地压缩多模态CoT推理序列，在显著降低计算延迟的同时，严格保持其视觉 grounding（即与视觉输入的关联性），避免因压缩而损害推理准确性和可靠性。论文通过引入V-Skip方法，将令牌剪枝重新定义为一种视觉锚定的信息瓶颈优化问题，旨在平衡语言效率与跨模态的视觉信息保留。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：**多模态推理方法**、**计算效率优化方法**和**针对推理链的压缩方法**。

在**多模态推理方法**方面，相关工作如PICa、Multimodal-CoT、PromptCoT和T-SciQ等，主要通过引入提示工程、人工标注的思维链或教师信号来生成详细的推理路径，以提升模型准确性。本文与这些工作的目标一致，即提升多模态大语言模型的推理性能，但本文的关注点从“生成更优的推理链”转向了“高效利用生成的推理链”。

在**计算效率优化**方面，存在系统级优化方法，如量化、结构化压缩和KV缓存优化（如PagedAttention），它们主要减少内存占用，但未直接解决自回归生成中序列长度带来的计算瓶颈。本文则直接针对序列长度导致的延迟问题进行优化。

在**针对推理链的压缩**方面，现有方法如TokenSkip、ASCoT和LLMLingua-2等，主要借鉴文本领域的压缩策略，利用困惑度、熵分布等**纯语言学指标**来识别和剪枝冗余token。本文指出，将这些方法盲目应用于多模态上下文会导致“视觉遗忘”问题，即错误剪除对视觉理解至关重要的token。本文提出的V-Skip与这些工作的核心区别在于，它首次明确将**视觉锚定**引入剪枝度量，通过双路径门控机制（结合语言惊异度和跨模态注意力流）来权衡token重要性，从而在压缩时保留关键的视觉细节。

### Q3: 论文如何解决这个问题？

论文通过提出V-Skip方法来解决多模态思维链推理中因盲目压缩导致的“视觉遗忘”问题。其核心是将令牌修剪重新形式化为一个视觉锚定的信息瓶颈优化问题，并设计了一个双路径门控机制来权衡令牌的重要性。

整体框架基于信息瓶颈原则，旨在找到一个压缩后的推理子序列，在最大化答案预测似然的同时最小化推理延迟。方法包含两个主要模块：双路径评分机制和V-Skip门控决策模块。

关键技术首先体现在**双路径评分**上。**文本路径**通过计算令牌的负对数似然来评估其语言信息量，识别语言上冗余的功能词。**视觉路径**则通过分析从生成文本到视觉上下文的跨模态注意力流来评估视觉锚定必要性。具体地，它计算特定层和注意力头上指向图像块的总注意力质量，并通过在关键层上取平均、在注意力头上取最大值的策略来聚合，得到视觉锚定分数，从而捕捉那些仅从文本难以预测但结合图像后变得确定的令牌。

创新点在于提出的**VA-IB目标函数**，它在传统的信息充分性约束之外，显式地增加了视觉锚定约束项，要求压缩后的序列与视觉输入保持高互信息，以缓解幻觉。另一个关键创新是**V-Skip门控的“显著性联合”策略**。它并非依赖单一阈值，而是分别为文本分数和视觉分数设定动态阈值，并采用逻辑“或”操作来决定令牌保留：只要一个令牌在语言上必要（文本分数高）或在视觉上必要（视觉分数高），就会被保留。这确保了视觉关键令牌即使语言上冗余也不会被错误修剪。

此外，为了消除运行时计算开销，论文还采用了**策略蒸馏**技术，通过指令微调将V-Skip的决策逻辑内化到模型参数中，使模型在推理时能直接生成简洁且视觉锚定的理由链，而无需显式进行注意力分析。

### Q4: 论文做了哪些实验？

论文在Qwen2-VL和Llama-3.2系列模型上进行了广泛的实验。实验设置上，V-Skip通过LoRA应用于注意力层，冻结预训练的视觉和语言骨干，在8张NVIDIA RTX 3090 GPU的服务器上运行。使用的数据集包括用于评估复杂多学科推理的MMMU（报告准确率Acc）和用于严格评估细粒度OCR及空间 grounding 能力的DocVQA（报告ANLS分数）。效率指标包括生成的平均推理令牌数（Tokens）、端到端推理延迟（Latency）和实际压缩比（ActRatio）。

对比方法包括仅依赖语言概率分布识别冗余的文本中心方法（ASCoT和LLMLingua-2）以及作为性能稳定性下界的视觉注意力剪枝方法。主要结果显示，在Qwen2-VL-7B上，当目标压缩比γ=0.5时，V-Skip在DocVQA上取得83.7%的ANLS，仅下降7.9%，而LLMLingua-2下降53.1%至38.5%，V-Skip以45.2%的优势大幅领先；在MMMU上，V-Skip准确率降至48.2%（下降5.9%），而基线方法下降超过20%。效率方面，V-Skip在DocVQA上实现2.71秒延迟，相比原始模型加速约1.8倍，且比计算量大的LLMLingua-2（2.93秒）更快。关键数据指标包括：在γ=0.5时，V-Skip的视觉属性保留率（VARR）在颜色、形状和物体类别上分别达到89.4%、86.3%和91.2%，显著高于LLMLingua-2的42.5%、55.1%和64.8%。此外，在POPE幻觉基准上，V-Skip的F1分数为88.9，Yes-Ratio为51.2%，接近未压缩基线（50.4%），而ASCoT和LLMLingua-2的Yes-Ratio分别飙升至66.8%和64.5%，表明V-Skip能有效保持事实完整性。模型规模扩展性实验显示，随着模型容量增大（从2B到72B），V-Skip的鲁棒性增强，在72B模型上即使压缩50%令牌，准确率下降仅3.2%。

### Q5: 有什么可以进一步探索的点？

该论文提出的V-Skip方法虽然有效，但仍存在值得深入探索的改进空间。其局限性主要在于两方面：一是方法依赖于基础模型的多模态对齐能力，若底层模型的跨模态注意力机制较弱，性能可能下降；二是需要离线的知识蒸馏训练，带来了额外的计算开销，并非完全免训练。

未来研究可以从以下几个方向展开：首先，可以探索更轻量、自适应的锚定机制，减少对预设模型结构的依赖，例如通过动态学习视觉-语言关联权重来提升泛化能力。其次，研究在线或渐进式的压缩策略，使模型能在推理过程中实时调整token保留比例，平衡效率与精度。此外，可将V-Skip的思路扩展到更多模态（如音频、视频），验证其在更复杂多模态场景中的通用性。最后，结合神经架构搜索或自动化机器学习技术，自动优化双路径门控的超参数，以降低人工调优成本并进一步提升压缩效率。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型（MLLMs）中思维链（CoT）推理因自回归特性导致的高延迟问题，指出现有基于文本指标的盲目令牌压缩方法在多模态语境下会引发“视觉遗忘症”，即错误剪枝对视觉理解至关重要的冗余令牌，导致幻觉。为此，论文提出V-Skip方法，其核心贡献是将令牌剪枝重新定义为视觉锚定信息瓶颈（VA-IB）优化问题。该方法通过双路径门控机制，结合语言惊奇度和跨模态注意力流来评估令牌重要性，有效保留视觉显著锚点，并通过轻量级LoRA适配器实现策略蒸馏。实验表明，V-Skip在Qwen2-VL和Llama-3.2模型系列上实现了2.9倍的推理加速，且精度损失可忽略；在DocVQA等细粒度视觉任务上性能超越基线超过45%，显著缓解了物体幻觉问题。这项工作为未来在视频流或音视频交互等更广模态中探索基于对齐的压缩策略奠定了基础。
