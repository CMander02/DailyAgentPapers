---
title: "QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models"
authors:
  - "Jingxuan Zhang"
  - "Yunta Hsieh"
  - "Zhongwei Wang"
  - "Haokun Lin"
  - "Xin Wang"
  - "Ziqi Wang"
  - "Yingtie Lei"
  - "Mi Zhang"
date: "2026-02-23"
arxiv_id: "2602.20309"
arxiv_url: "https://arxiv.org/abs/2602.20309"
pdf_url: "https://arxiv.org/pdf/2602.20309v1"
categories:
  - "cs.LG"
tags:
  - "模型量化"
  - "具身智能"
  - "视觉-语言-动作模型"
  - "后训练量化"
  - "部署优化"
  - "扩散变换器"
relevance_score: 7.5
---

# QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models

## 原始摘要

Vision-language-action (VLA) models unify perception, language, and control for embodied agents but face significant challenges in practical deployment due to rapidly increasing compute and memory demands, especially as models scale to longer horizons and larger backbones. To address these bottlenecks, we introduce QuantVLA, a training-free post-training quantization (PTQ) framework that, to our knowledge, is the first PTQ approach for VLA systems and the first to successfully quantize a diffusion transformer (DiT) action head. QuantVLA incorporates three scale-calibrated components: (1) a selective quantization layout that integerizes all linear layers in both the language backbone and the DiT while keeping attention projections in floating point to preserve the original operator schedule; (2) attention temperature matching, a lightweight per-head scaling mechanism that stabilizes attention logits and is folded into the dequantization scales at inference; and (3) output head balancing, a per-layer residual interface calibration that mitigates post-projection energy drift. The framework requires no additional training, uses only a small unlabeled calibration buffer, and supports integer kernels for low-bit weights and activations while leaving the architecture unchanged. Across representative VLA models on LIBERO, QuantVLA exceeds the task success rates of full-precision baselines, achieves about 70% relative memory savings on the quantized components, and delivers a 1.22x speedup in end-to-end inference latency, providing a practical pathway toward scalable low-bit embodied intelligence under strict compute, memory, and power constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉-语言-动作（VLA）模型在具身智能体实际部署中面临的核心瓶颈问题。VLA模型通过统一感知、语言和控制，是实现高级具身智能的关键架构。然而，随着模型规模（如更长的任务视野、更大的骨干网络）的不断增长，其计算和内存需求急剧上升，严重阻碍了在资源受限的边缘设备或机器人平台上的高效部署。具体挑战包括：模型参数量大、推理延迟高、内存占用多，尤其是在包含扩散变换器（DiT）作为动作预测头的复杂架构中，传统的模型压缩方法（如量化）难以直接应用且效果不佳。因此，论文提出了QuantVLA框架，其核心目标是开发一种无需重新训练的后训练量化（PTQ）方法，在保持甚至提升任务性能的同时，显著降低VLA模型的存储开销和计算延迟，为可扩展、低比特的具身智能提供一条实用的部署路径。

### Q2: 有哪些相关研究？

相关研究主要分为几个方向：1) **视觉-语言-动作（VLA）模型**：如RT-2、VoxPoser、PACT等，它们将视觉编码器、大型语言模型（LLM）和动作解码器（如MLP或扩散模型）结合，用于机器人规划与控制。这些工作是QuantVLA的应用对象和性能基准。2) **模型量化技术**：包括训练后量化（PTQ）和量化感知训练（QAT）。PTQ因无需重新训练而更受青睐，相关方法如GPTQ、AWQ、SmoothQuant主要针对纯语言或视觉模型。然而，针对融合了扩散变换器（DiT）等复杂组件的VLA模型的PTQ研究尚属空白。3) **扩散模型的量化**：近期工作开始探索扩散模型的低比特表示，但多集中于图像生成领域，且常需要微调。QuantVLA首次成功将PTQ应用于作为VLA动作头的DiT。4) **注意力机制量化**：已有研究指出注意力层对量化敏感，提出了如基于Hessian信息的通道级缩放等方法。QuantVLA提出的“注意力温度匹配”机制与之相关，但更侧重于稳定低比特下的注意力logits分布。本文与这些工作的关系在于，它首次系统性地将PTQ应用于完整的VLA pipeline（包括语言骨干和DiT动作头），并针对VLA特有的多模态融合与序列决策特性，提出了新颖的尺度校准组件。

### Q3: 论文如何解决这个问题？

论文提出了QuantVLA，一个免训练的、尺度校准的后训练量化框架。其核心方法包含三个精心设计的组件，共同应对VLA模型量化的独特挑战：

1. **选择性量化布局**：并非对所有层进行均匀量化。该布局将语言骨干（LLM）和扩散变换器（DiT）动作头中的所有线性层（包括前馈网络和注意力中的Q/K/V投影）转换为整数运算，以利用高效的整数计算内核。然而，它策略性地将注意力计算中的输出投影（O_proj）层保持为浮点数。这是因为在Transformer架构中，注意力输出投影与后续的残差连接和层归一化紧密耦合，直接量化会导致严重的激活分布偏移和误差累积。保持其浮点状态可以维持原有的算子调度和数据流，是稳定量化的关键。

2. **注意力温度匹配**：这是针对低比特量化下注意力机制不稳定的创新解决方案。量化会扭曲注意力logits的分布，改变其原有的“温度”（即softmax前的缩放特性）。该方法通过一个轻量级的、每个注意力头独立的缩放因子，在量化前校准logits的尺度，使其分布与全精度模型匹配。关键的是，这个缩放因子在推理时可以被“折叠”到反量化尺度中，因此不引入任何额外的计算开销或参数。

3. **输出头平衡**：专门用于校准DiT动作头中的残差连接接口。在DiT中，每个Transformer块输出会通过一个投影层（如MLP）产生残差加到主路径上。量化会改变这些投影输出的能量（范数），导致跨层的残差信号不平衡，从而破坏扩散过程的去噪轨迹。该方法通过逐层校准这些投影层的输出尺度，确保量化后残差信号的相对强度与全精度模型一致，从而缓解“能量漂移”。

整个框架仅需少量未标注的校准数据（用于统计激活范围），无需任何微调或反向传播，保持了原始模型架构不变，同时实现了权重和激活的低比特整数化。

### Q4: 论文做了哪些实验？

论文在代表性的VLA模型和具身任务基准上进行了全面实验，以验证QuantVLA的有效性。

**实验设置**：
- **模型与基准**：主要使用在LIBERO（一个长视野、多任务的具身AI基准）上训练的VLA模型。模型骨干包括视觉编码器（如CLIP）、语言模型（如Vicuna）以及扩散变换器（DiT）作为动作预测头。
- **量化配置**：采用W4A4（权重和激活均为4比特）和W4A8等低比特配置进行测试。对比基线为全精度（FP16）模型以及朴素的PTQ方法（如直接将MinMax量化应用于所有层）。
- **评估指标**：
  1. **任务成功率**：在LIBERO的多个场景任务中评估智能体完成目标的百分比，这是核心性能指标。
  2. **内存占用**：测量量化后模型参数的存储节省。
  3. **推理延迟**：测量端到端的单步推理时间。
  4. **消融研究**：通过移除各个组件（选择性布局、温度匹配、输出头平衡）来验证其必要性。

**主要结果**：
1. **性能保持与超越**：QuantVLA在W4A4配置下，不仅匹配了全精度基线的任务成功率，在多个任务上甚至实现了超越。这表明合理的量化有时能起到正则化效果，或减少了某些噪声。而朴素PTQ则导致成功率大幅下降。
2. **内存与速度收益**：QuantVLA对量化部分（LLM+DiT）实现了约70%的相对内存节省。端到端推理延迟获得了1.22倍的加速。这主要得益于将大量线性层转换为整数计算，减少了数据移动和浮点运算开销。
3. **消融分析**：实验证实了三个核心组件缺一不可。移除注意力温度匹配会导致注意力图失真和性能下降；移除输出头平衡会破坏DiT的生成质量；而采用激进的全量化布局则会引发严重的不稳定。
这些实验强有力地证明了QuantVLA作为一种实用、高效的VLA模型部署解决方案的可行性。

### Q5: 有什么可以进一步探索的点？

尽管QuantVLA取得了显著成果，但仍存在一些局限性和未来研究方向：
1. **扩展到更广泛的VLA架构**：当前工作主要针对特定类型的VLA模型（如使用DiT作为动作头）。未来需要验证框架对使用其他动作解码器（如MLP、Transformer解码器）或不同视觉-语言融合机制（如Flamingo风格）的VLA模型的通用性。
2. **极低比特量化**：论文探索了W4A4，但更极端的W2A2或混合精度量化可能带来更大的压缩收益，同时也面临更大挑战。如何在这种极端设定下保持稳定性值得研究。
3. **动态计算与稀疏性结合**：可以探索将量化与动态计算（如提前退出）、激活稀疏化等技术结合，以进一步优化实时推理效率。
4. **量化感知的预训练或微调**：虽然QuantVLA是免训练的PTQ，但在模型设计初期或拥有领域数据时，进行量化感知的预训练或轻量微调（QLoRA风格）可能突破PTQ的性能天花板，实现更高的压缩率。
5. **硬件在环评估**：目前实验主要在仿真环境中进行。未来需要在真实的机器人硬件上评估量化模型的实际延迟、功耗和鲁棒性，尤其是在传感器噪声和实时性约束下的表现。
6. **理论分析**：对提出的“注意力温度匹配”和“输出头平衡”机制进行更深入的理论分析，理解其为何能有效稳定量化后的分布，可能启发更通用的多模态模型量化原则。

### Q6: 总结一下论文的主要内容

本文提出了QuantVLA，这是首个专门为视觉-语言-动作（VLA）模型设计的、免训练的后训练量化（PTQ）框架。VLA模型是具身智能的核心，但其巨大的计算和内存需求阻碍了实际部署。QuantVLA的创新在于成功量化了包含扩散变换器（DiT）动作头的复杂VLA系统。其核心贡献是三个尺度校准组件：1）选择性量化布局，将大部分线性层整数化但保留关键注意力输出投影为浮点以维持稳定性；2）注意力温度匹配，通过每头缩放校准量化后的注意力logits分布；3）输出头平衡，校准DiT中的残差接口以防止能量漂移。该框架无需额外训练，仅需少量校准数据。在LIBERO基准上的实验表明，QuantVLA在4比特量化下不仅能保持甚至有时超越全精度模型的任務成功率，同时实现了约70%的内存节省和1.22倍的推理加速。这项工作为在资源受限的边缘设备上部署高效、高性能的具身智能体提供了一条切实可行的技术路径。
