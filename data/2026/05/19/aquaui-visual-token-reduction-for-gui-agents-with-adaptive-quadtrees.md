---
title: "AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees"
authors:
  - "Yuankai Li"
  - "Tinghui Zhu"
  - "Ha Min Son"
  - "Zhe Zhao"
  - "Xin Liu"
  - "Muhao Chen"
date: "2026-05-19"
arxiv_id: "2605.19260"
arxiv_url: "https://arxiv.org/abs/2605.19260"
pdf_url: "https://arxiv.org/pdf/2605.19260v1"
categories:
  - "cs.AI"
  - "cs.CV"
  - "cs.MA"
tags:
  - "GUI Agent"
  - "视觉token压缩"
  - "四叉树"
  - "推理加速"
  - "训练无关"
  - "多模态大模型"
relevance_score: 7.5
---

# AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees

## 原始摘要

Large Multimodal Models (LMMs) have recently emerged as promising backbones for GUI-agent models, where high-resolution GUI screenshots are introduced to the prompts at each iteration step. However, these screenshots exhibit highly non-uniform spatial information density: large regions may carry little information and are visually homogeneous, while key text and icons may require high visual fidelity. Existing approaches to this problem either require additional training or rely on attention-based token compression, ignoring the structured layout and spatial redundancy of GUI screenshots. To fill the gap, this paper proposes AquaUI, a training-free inference-time token reduction method for GUI agent models that utilizes the non-uniform information density in screenshots. AQuaUI constructs an adaptive quadtree on each screenshot input and keeps one representative merged token per leaf of the quadtree. AQuaUI preserves the spatial positions of retained tokens throughout the pipeline to ensure that all position-encoding stages remain consistent. To further improve temporal consistency across multi-step GUI interactions, we propose a conditional quadtree algorithm that leverages the continuity between consecutive screenshots within a single request. Specifically, it refines the current quadtree using previous quadtrees as references, helping preserve fine-grained regions across static or mildly shifted GUI states. We implement AQuaUI on state-of-the-art GUI agent models and conduct experiments on standard grounding and navigational benchmarks. AQuaUI consistently shows improved accuracy-efficiency trade-offs over prior baselines. Notably, on GUI-Owl-1.5-32B-Instruct, AQuaUI achieves up to 13.22% speedup and 29.52% fewer visual tokens while retaining 99.06% of full-token performance, suggesting that the spatial redundancy of GUI screenshots can be exploited at inference without retraining.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决GUI代理模型中高分辨率截图带来的视觉token冗余问题。研究背景是大型多模态模型（LMMs）已成为GUI代理模型的主流骨干，每次交互都需要输入高分辨率GUI截图，导致大量视觉token（如2400×1080像素截图约产生3000个token），增加了计算成本并限制了上下文窗口中的对话历史保留。现有方法的不足包括：一是针对自然图像的token压缩方法不适用于具有非均匀信息密度和简单规则空间结构的GUI截图；二是已有的GUI图像token缩减方法需要作为模型训练的一部分，无法直接应用于任意GUI代理模型。本文要解决的核心问题是：如何在无需额外训练的情况下，在推理阶段有效利用GUI截图中大面积视觉同质区域与关键文本图标区域之间的非均匀信息密度，实现视觉token的高效缩减，同时保持空间位置信息的一致性，并通过多步交互间的条件四叉树算法提升时序一致性，从而在不显著影响性能的前提下提高推理速度和减少token数量。

### Q2: 有哪些相关研究？

本文相关工作可分为三类。第一类是GUI代理方法，如UI-TARS、GUI-Owl等训练LMM在屏幕轨迹上，而UI-Voyager、MAI UI、ClawGUI探索规划、多智能体协调等方向。这些方法共享一个瓶颈：每次交互引入高分辨率截图，产生大量视觉token。ShowUI利用UI结构规则性减少token，FocusUI选择指令相关UI补丁并采用位置感知策略。区别在于这些方法主要在模型特定训练设置下获得结果，而AQuaUI专注于免训练部署在现成模型上。

第二类是Token剪枝方法，如FastV在深层使用注意力剪枝视觉token，G-Prune通过图传播建模token重要性，SimIgnore使用跨模态相似性丢弃冗余补丁，以及HiPrune和VisionZip等通用剪枝器。这些方法主要将减少视为token重要性估计，但GUI截图中低注意力token可能仍重要（如定义标签或坐标上下文），且依赖注意力图计算会增加复杂性。AQuaUI通过自适应四叉树利用非均匀信息密度，无需注意力计算。

第三类是KV缓存压缩，如SnapKV、PyramidKV等，通过不同策略压缩token进入transformer后的KV缓存。GUI KV专门基于GUI截图计算空间和时间评分。这些方法与AQuaUI正交：它们减少编码后内存和解码成本，而AQuaUI在KV缓存计算前减少视觉token序列本身。

### Q3: 论文如何解决这个问题？

论文提出了AQuaUI，一种无需训练、仅在推理时进行的视觉令牌缩减方法，专门针对GUI智能体模型。其核心是利用GUI截图非均匀的空间信息密度，通过自适应四叉树（Quadtree）结构实现令牌压缩。

**整体框架与核心方法**：处理流程分为三步。首先，将输入截图分解为可被C×C块平铺的中心区域和边界区域，边界区域保持原样，中心区域被划分为多个块。然后，在每个块内独立构建自适应四叉树。四叉树的每个节点根据区域加权灰度方差（或梯度）递归分裂，直到满足停止条件。这样，信息量低的均匀区域由大叶子节点表示，而细节丰富的文本、图标区域则由小叶子节点精细表示。最后，从每个四叉树叶节点中选择一个中心代表令牌块，作为该区域的视觉令牌，从而用少量令牌覆盖冗区域，同时保留关键细节。

**关键技术**：为保持多步GUI交互中的时间一致性，论文提出了条件四叉树算法。该算法通过比较连续截图对应块的变化，将块分为三种模式：静态（像素变化极小）、移位（滚动操作导致的内容偏移）和替换（全新内容）。对于静态和移位块，算法复用或微调前一步的四叉树结构，从而避免重要细节在帧间丢失；对于替换块，则重新构建四叉树。这保证了长序列交互中视觉信息的连贯性。

**创新点**：一是首次将四叉树结构引入GUI智能体的视觉令牌缩减，充分利用了GUI截图中大面积均匀冗余与小区域高密度细节的结构特性，无需额外训练。二是提出了条件四叉树机制，有效解决了多步交互中帧间信息一致性问题，进一步提升了压缩效率和性能。实验表明，AQuaUI在多种模型上实现了显著的速度提升和令牌减少，同时保持了接近全令牌的性能。

### Q4: 论文做了哪些实验？

论文在多个GUI基准测试上评估了AQuaUI方法，实验设置包括五大 grounding 基准（ScreenSpot-Pro、ScreenSpot-V2、OSWorld-g、UI-Vision、MMBench-GUI）和两大导航基准（AndroidControl 离线、AndroidWorld 在线）。主要对比方法包括 ShowUI 的 UI-guided token selection、随机降采样和 FastV。关键数据指标显示，在Qwen2-VL-7B-Instruct模型上，AQuaUI在26.82%压缩率下平均准确率仅下降3.29个百分点，而ShowUI在27.55%压缩率下下降5.95个百分点；延迟仅增加0.02秒（ShowUI增加0.31秒）。在Qwen3-VL系列上，约30%压缩率下准确率下降均小于1点（如32B模型下降0.85点），延迟减少0.09-0.23秒。在GUI-Owl-1.5-32B模型上实现13.22%加速和29.52%令牌减少，同时保留99.06%性能。AndroidWorld消融实验表明，条件四叉树机制对多步交互至关重要，移除后UI-Voyager成功率从68.10%降至65.52%。对比实验证实，随机降采样导致显著性能下降（如ScreenSpot-V2从67.14%降至57.47%），而AQuaUI恢复至60.06%。

### Q5: 有什么可以进一步探索的点？

论文在GUI截图的空间冗余利用上取得了良好效果，但仍存在一些可进一步探索的方向。首先，四叉树分割策略对“同质区域”的定义依赖固定阈值，未能自适应地根据任务复杂度（如目标定位精度）动态调整分割粒度，未来可引入内容感知的阈值学习机制。其次，条件四叉树仅在静态或轻微变化时复用历史分区，对动态交互（如滚动、弹窗切换）的场景鲁棒性不足，可考虑结合光流或注意力图对关键区域进行时序预测。此外，当前方法仅保留每个叶节点单一token，可能丢失细粒度特征（如高密度文字区域的局部细节），建议对重要区域保留多token级表示或使用层次化特征融合。最后，该方法在更大规模模型上的效率增益显著，但未探讨其对人机交互中实时性要求极高的任务（如手势跟踪）的适应性，未来可结合稀疏注意力或动态token剪枝策略进一步降低延迟。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为 AQuaUI 的免训练推理时视觉令牌缩减方法，用于解决 GUI 智能体模型中高分辨率截图信息密度分布不均匀的问题。现有方法要么需要额外训练，要么依赖注意力机制压缩，忽略了 GUI 截图的空间结构和冗余性。AQuaUI 通过自适应四叉树将截图划分为非均匀区域，在信息量少的同质区域使用粗粒度叶子节点，关键区域保留细粒度，每个叶子节点仅保留一个代表令牌，并保持其空间位置以确保位置编码一致性。为进一步提升多步交互的时间一致性，论文设计了条件四叉树算法，利用前后截图的连续性重用或重建分区。在 GUI 接地和导航基准测试上，AQuaUI 在保持接近全令牌性能（如 99.06%）的同时，实现了高达 13.22% 的速度提升和 29.52% 的视觉令牌减少。该工作证明了利用 GUI 截图空间冗余性进行高效推理的可行性，并强调了在令牌缩减中考虑其空间位置的重要性。
