---
title: "QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models"
authors:
  - "Jingxuan Zhang"
  - "Yunta Hsieh"
  - "Zhongwei Wan"
  - "Haokun Lin"
  - "Xin Wang"
  - "Ziqi Wang"
  - "Yingtie Lei"
  - "Mi Zhang"
date: "2026-02-23"
arxiv_id: "2602.20309"
arxiv_url: "https://arxiv.org/abs/2602.20309"
pdf_url: "https://arxiv.org/pdf/2602.20309v2"
categories:
  - "cs.LG"
tags:
  - "模型量化"
  - "具身智能"
  - "视觉-语言-动作模型"
  - "推理优化"
  - "部署效率"
  - "后训练量化"
relevance_score: 6.5
---

# QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models

## 原始摘要

Vision-language-action (VLA) models unify perception, language, and control for embodied agents but face significant challenges in practical deployment due to rapidly increasing compute and memory demands, especially as models scale to longer horizons and larger backbones. To address these bottlenecks, we introduce QuantVLA, a training-free post-training quantization (PTQ) framework that, to our knowledge, is the first PTQ approach for VLA systems and the first to successfully quantize a diffusion transformer (DiT) action head. QuantVLA incorporates three scale-calibrated components: (1) a selective quantization layout that integerizes all linear layers in both the language backbone and the DiT while keeping attention projections in floating point to preserve the original operator schedule; (2) attention temperature matching, a lightweight per-head scaling mechanism that stabilizes attention logits and is folded into the dequantization scales at inference; and (3) output head balancing, a per-layer residual interface calibration that mitigates post-projection energy drift. The framework requires no additional training, uses only a small unlabeled calibration buffer, and supports integer kernels for low-bit weights and activations while leaving the architecture unchanged. Across representative VLA models on LIBERO, QuantVLA exceeds the task success rates of full-precision baselines, achieves about 70% relative memory savings on the quantized components, and delivers a 1.22x speedup in end-to-end inference latency, providing a practical pathway toward scalable low-bit embodied intelligence under strict compute, memory, and power constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉-语言-动作（VLA）模型在实际部署中面临的计算和内存需求过高的问题。随着模型规模扩大（如使用更长的序列和更大的骨干网络），其计算和内存开销急剧增长，这严重阻碍了VLA模型在计算资源受限的嵌入式或移动机器人平台上的应用。

现有提升VLA效率的方法主要分为两类：一是设计更高效的模型架构（如使用紧凑的多模态Transformer），二是围绕现有策略构建效率框架（如通过剪枝、缓存或动态计算跳过）。然而，这些方法主要优化视觉编码器部分，而未能有效处理语言骨干网络和基于扩散Transformer（DiT）的动作策略头。DiT动作头是计算和内存消耗的主要贡献者，且与上游推理模块紧密耦合，行为敏感，现有方法通常保持其全精度运行，因此未能充分挖掘推理和动作生成阶段的优化潜力。此外，现有的训练后量化（PTQ）技术（如SmoothQuant）主要针对大型语言或视觉语言模型设计，未能有效处理VLA系统中下游推理和动作模块的异构激活与精度行为。

因此，本文的核心问题是：如何为包含复杂DiT动作头的VLA模型，设计一种无需重新训练、能保持性能的**训练后量化框架**，以显著降低其内存占用和计算延迟，从而为在严格计算、内存和功耗约束下实现可扩展的低比特具身智能提供实用路径。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**VLA模型架构设计**、**VLA模型推理优化**以及**后训练量化（PTQ）方法**。

在**VLA模型架构设计**方面，相关工作包括：1）编码器-解码器架构（如ALOHA、RT-1）；2）基于预训练语言/视觉语言模型的方法（如RT-2、OpenVLA），将动作视为自回归token；3）基于扩散的策略（如Diffusion Policy、RDT-1B），用于生成平滑轨迹；4）视频驱动与逆向运动学模型（如UniPi）；以及5）结合语言推理与扩散控制的混合架构（如OPENPI π0、GR00T N1.5）。此外，还有旨在设计轻量级架构以降低部署成本的高效VLA模型（如TinyVLA、SmolVLA）。**QuantVLA与这些工作的根本区别在于，它不设计新模型或训练流程，而是一个保持原始架构不变的PTQ框架，因此可与上述各类模型正交组合，作为部署后处理步骤。**

在**VLA模型推理优化**方面，相关工作通过剪枝、路由或缓存等机制提升运行时效率，而不改变数值精度，例如EfficientVLA（剪枝冗余层）、VLA-Cache（重用缓存特征）和MoLe-VLA（动态跳过计算）。**QuantVLA则直接操作数值精度，专注于后训练部署效率，并对语言主干和扩散动作头进行量化，不修改执行顺序或引入额外路由逻辑。**

在**后训练量化（PTQ）方法**方面，现有研究主要针对大型语言模型（如SmoothQuant、DuQuant）或扩散Transformer（如SVDQuant、ViDiT-Q），通过平滑异常值或精细分组来稳定低比特推理。**QuantVLA的独特挑战与贡献在于，它是首个针对VLA系统的PTQ方法，并首次成功量化了扩散Transformer动作头。它解决了VLA中多模态与扩散紧密耦合带来的新问题（如注意力温度漂移、残差能量漂移），而现有PTQ技术无法直接应对这些挑战。**

### Q3: 论文如何解决这个问题？

QuantVLA 通过一个无需训练的后训练量化（PTQ）框架，解决了视觉-语言-动作（VLA）模型因计算和内存需求巨大而难以部署的问题。其核心方法是结合**选择性量化布局**与两种轻量级的**尺度校准机制**，以稳定量化误差在跨模态和时序扩散过程中的传播，同时保持原始架构和算子调度不变。

**整体框架与主要模块**：
1.  **选择性量化布局**：这是框架的基础。它并非量化所有层，而是**将语言主干（LLM）中的所有线性层和扩散变换器（DiT）动作头中的所有多层感知机（MLP）层进行整型化**。同时，**刻意保持注意力投影层（Q, K, V, O）为浮点数**。这样设计是因为分析发现，注意力层的logits（决定softmax温度）和输出投影的能量（决定残差注入增益）对上游的量化扰动最为敏感。保留它们的浮点精度，从架构上避免了误差在这些关键接口被放大和累积。

2.  **注意力温度匹配（ATM）**：这是一个针对每个注意力头的轻量级校准模块，用于解决上游语言主干量化导致的注意力logits分布漂移（即“温度”变化）问题。其工作原理是：使用一个小的无标签校准缓冲区，计算教师模型（浮点）与学生模型（量化）在注意力softmax前logits的标准差之比，得到一个每头缩放标量α。该标量被裁剪并限制在一个安全范围内，然后**折叠到反量化尺度中**。在推理时，通过调整logits的尺度（L_Q = L_T / α），使量化模型的注意力分布与原始模型对齐，防止注意力变得过于尖锐或平坦。

3.  **输出头平衡（OHB）**：这是一个针对每个Transformer层的轻量级校准模块，用于解决因量化导致的注意力输出投影后能量漂移问题，该漂移会影响残差连接的注入增益和层归一化的操作点。OHB同样利用校准缓冲区，计算教师与学生模型在每一层输出投影后激活值的均方根（RMS）之比，得到每层缩放标量β。经过类似的裁剪和中性带处理后，**将β折叠到反量化尺度**，并在推理时对进入残差路径的激活值进行缩放（Z_Q = Z_l / β），从而恢复正确的残差注入能量。

**创新点与关键技术**：
*   **首个针对VLA系统（特别是含DiT动作头）的PTQ框架**：首次成功实现了对扩散变换器动作头的量化。
*   **基于误差传播分析的针对性设计**：框架的三大组件（选择性布局、ATM、OHB）均源于对量化误差在VLA跨模态及DiT迭代过程中传播路径的一阶分析，直击“注意力温度漂移”和“残差能量漂移”两大核心敏感点。
*   **完全训练免费且部署友好**：整个流程无需任何微调或再训练，仅需少量无标签数据进行一次性校准。ATM和OHB以标量形式实现并折叠到现有尺度中，**不引入任何新算子、额外缓冲区或改变整数矩阵乘（GEMM）计算**，保持了原始的推理计算图和延迟优势。
*   **显著的效率提升**：在量化组件上实现了约70%的相对内存节省，并带来了端到端推理延迟1.22倍的加速，为在严格资源限制下部署 embodied AI 提供了实用路径。

### Q4: 论文做了哪些实验？

论文在LIBERO仿真基准上对两个先进的VLA模型（OpenPI π0.5和GR00T N1.5）进行了全面的量化实验评估。实验设置采用W4A8（4位权重，8位激活）的后训练量化（PTQ），使用少量未标记的校准缓冲区，无需额外训练。主要对比方法包括全精度（FP16）基线以及另一种PTQ方法DuQuant。

实验首先进行了层选择消融研究，比较了仅量化LLM、仅量化DiT、同时量化LLM+DiT以及量化LLM+DiT MLP等不同方案。结果显示，量化LLM+DiT MLP方案在保持性能的同时获得了最佳的内存收益。随后，论文验证了所提出的注意力温度匹配（ATM）和输出头平衡（OHB）校准机制的有效性，它们分别稳定了注意力logits统计量和缓解了残差能量漂移。

主要结果方面，在LIBERO的四个任务套件（Spatial, Object, Goal, Long）上，QuantVLA取得了优异的表现。对于π0.5模型，QuantVLA（W4A8）平均成功率高达97.6%，与FP16基线（97.1%）相当甚至略有超越，同时将内存占用从4.27 GB降至1.28 GB（相对节省70.0%）。对于GR00T N1.5模型，QuantVLA平均成功率为88.0%，超过FP16基线（86.5%），内存从2.02 GB降至0.91 GB（相对节省55.0%）。相比之下，DuQuant在量化LLM+DiT时性能下降严重（π0.5降至76.3%，GR00T N1.5降至70.0%）。

此外，鲁棒性分析表明，QuantVLA在更激进的W4A4精度下（π0.5平均成功率95.3%）以及在不同去噪步数下（GR00T N1.5在8步和16步下平均成功率分别为88.0%和88.5%）均能保持稳定性能。论文还报告了端到端推理延迟获得了1.22倍的加速。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其量化策略主要针对线性层和扩散变换器的前馈块，而注意力投影层仍保留为浮点运算，这限制了进一步的压缩潜力。未来研究可探索对注意力机制的完全量化，包括键、查询、值矩阵的低位宽表示，以达成更高的内存节省。此外，当前方法依赖小型未标注校准缓冲区，未来可研究更高效的校准策略，如基于合成数据或在线自适应校准，以提升泛化能力。结合见解，可考虑引入动态精度分配，根据层敏感度自适应调整位宽，平衡精度与效率。另一个方向是探索量化感知的架构搜索，设计更适合低位宽运行的VLA模型组件，从而在严格功耗约束下实现更优的部署性能。

### Q6: 总结一下论文的主要内容

QuantVLA 是一种针对视觉-语言-动作（VLA）模型的免训练后量化（PTQ）框架，旨在解决VLA模型因计算和内存需求巨大而难以实际部署的问题。其核心贡献是首次为VLA系统提出了PTQ方法，并成功量化了扩散变换器（DiT）动作头。

该方法包含三个关键组件：首先，采用选择性量化布局，将语言主干和DiT中的所有线性层整数化，同时保持注意力投影为浮点数以维持原有算子调度。其次，提出注意力温度匹配，这是一种轻量级的逐头缩放机制，用于稳定注意力逻辑值，其缩放因子可在推理时折叠到反量化尺度中。最后，引入输出头平衡，通过逐层残差接口校准来减轻投影后的能量漂移。

该框架无需额外训练，仅需少量未标记的校准数据，支持对低比特权重和激活使用整数内核，同时保持架构不变。实验表明，QuantVLA在LIBERO基准测试中超越了全精度基线的任务成功率，量化部分实现了约70%的相对内存节省，端到端推理延迟加速了1.22倍。这为在严格的计算、内存和功耗约束下实现可扩展的低比特具身智能提供了实用路径。
