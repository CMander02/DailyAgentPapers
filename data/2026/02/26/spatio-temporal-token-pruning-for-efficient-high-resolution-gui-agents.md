---
title: "Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents"
authors:
  - "Zhou Xu"
  - "Bowen Zhou"
  - "Qi Wang"
  - "Shuwen Feng"
  - "Jingyu Xiao"
date: "2026-02-26"
arxiv_id: "2602.23235"
arxiv_url: "https://arxiv.org/abs/2602.23235"
pdf_url: "https://arxiv.org/pdf/2602.23235v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Efficiency Optimization"
  - "Vision-Language Model"
  - "Token Pruning"
  - "Agent Architecture"
relevance_score: 8.0
---

# Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents

## 原始摘要

Pure-vision GUI agents provide universal interaction capabilities but suffer from severe efficiency bottlenecks due to the massive spatiotemporal redundancy inherent in high-resolution screenshots and historical trajectories. We identify two critical misalignments in existing compression paradigms: the temporal mismatch, where uniform history encoding diverges from the agent's "fading memory" attention pattern, and the spatial topology conflict, where unstructured pruning compromises the grid integrity required for precise coordinate grounding, inducing spatial hallucinations. To address these challenges, we introduce GUIPruner, a training-free framework tailored for high-resolution GUI navigation. It synergizes Temporal-Adaptive Resolution (TAR), which eliminates historical redundancy via decay-based resizing, and Stratified Structure-aware Pruning (SSP), which prioritizes interactive foregrounds and semantic anchors while safeguarding global layout. Extensive evaluations across diverse benchmarks demonstrate that GUIPruner consistently achieves state-of-the-art performance, effectively preventing the collapse observed in large-scale models under high compression. Notably, on Qwen2-VL-2B, our method delivers a 3.4x reduction in FLOPs and a 3.3x speedup in vision encoding latency while retaining over 94% of the original performance, enabling real-time, high-precision navigation with minimal resource consumption.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决纯视觉GUI智能体在处理高分辨率屏幕截图和历史轨迹时面临的严重效率瓶颈问题。研究背景在于，基于多模态大语言模型的GUI智能体通过直接分析屏幕截图进行交互，具有跨平台通用性优势，但同时也引入了巨大的时空冗余计算开销。现有压缩方法存在两大不足：一是时间维度上的不匹配，即传统方法对历史帧进行统一的高分辨率编码，忽视了智能体注意力随时间的“衰退记忆”模式（近期帧关注度高，远期帧关注度低），导致对远期帧的过度编码造成计算浪费；二是空间拓扑冲突，现有通用压缩方法采用非结构化剪枝策略，破坏了屏幕截图固有的二维网格结构，导致坐标定位时出现严重的“空间幻觉”，同时可能误删具有语义锚点作用的背景区域。

本文要解决的核心问题是：如何设计一种无需训练的压缩框架，在保持GUI智能体高精度交互能力的同时，显著降低其视觉编码的计算开销。具体而言，需要同时解决历史帧编码中的时间冗余问题，以及当前帧处理中稀疏性压缩与空间拓扑保持之间的矛盾，从而实现高效、实时的GUI导航。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两类：GUI智能体效率优化和视觉令牌剪枝。

在**GUI智能体效率优化**方面，早期工作依赖辅助工具（如无障碍树、OCR），而近期端到端多模态模型虽提升了通用性，却带来了高计算成本。为提升效率，OdysseyAgent通过可学习参数对历史截图进行重采样压缩；Iris和ShowUI尝试基于低级视觉线索过滤冗余背景，但前者仅处理当前帧，后者在推理时性能下降显著；SimpAgent和GUI-Rise则利用一致性引导训练或强化学习来总结历史交互。与这些方法不同，本文提出的GUIPruner是一个**无需训练**的框架，它通过时域自适应分辨率和分层结构感知剪枝，在保持GUI结构完整性的同时实现高效压缩，避免了参数更新和性能下降。

在**视觉令牌剪枝**方面，现有研究致力于减轻多模态大语言模型处理高分辨率图像的计算负担。早期方法使用可学习查询进行压缩（需额外训练），而当前前沿转向**无需训练**的推理时剪枝。例如，FastV根据浅层注意力分数过滤令牌；DivPrune、MoB和CDPruner等将剪枝构建为最大最小多样性问题，或利用文本提示对齐、行列式点过程来优化令牌选择。然而，这些通用方法主要针对自然图像设计，**往往无法保持GUI典型的密集、结构化布局**，可能导致空间幻觉。本文方法则专门针对GUI的结构特性进行压缩，解决了现有通用方法的局限性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GUIPruner的无训练框架来解决高分辨率GUI智能体中的时空冗余问题。该框架的核心是两种协同工作的创新机制：时间自适应分辨率（TAR）和分层结构感知剪枝（SSP）。

整体框架设计为处理历史轨迹（时间维度）和当前高分辨率截图（空间维度）的冗余。对于时间冗余，TAR机制采用全局到局部的资源调度。它首先通过一个全局超参数——历史令牌保留率（λ）——来约束整个历史序列的总计算预算。然后，通过一个线性衰减调度，根据时间距离远近动态分配令牌配额给各个历史帧，模拟“记忆衰减”模式，即近期帧获得更高分辨率，远期帧分辨率降低。最后，通过一个简单的缩放因子映射，将离散的令牌配额转换为连续图像尺寸的调整，从而在不引入可学习参数的情况下，严格将计算开销控制在预算内。

对于当前帧的空间冗余，SSP机制在大型语言模型的浅层实现，作为一个早期结构筛子。其关键技术在于分层保留策略。首先，通过边缘检测将视觉令牌划分为前景（包含交互元素）和背景集合，并结合浅层Transformer的注意力权重计算每个令牌的重要性分数。然后，在由当前令牌保留率（μ）定义的全局预算下，进行三层级的预算分配：1）**前景显著性保留**：优先保留前景中注意力分数最高的令牌，确保关键交互组件的高分辨率特征。2）**背景语义保留**：通过背景显著性因子（ρ），保留背景中一部分最重要的语义上下文令牌。3）**拓扑结构补全**：使用均匀网格采样（UGS）从剩余令牌中选取一部分，以维持全局布局和相对位置的粗粒度表征，这是防止坐标定位中出现空间幻觉的关键创新点。

该方法的创新点在于精准解决了现有压缩范式中的两个错位问题：TAR通过衰减式分辨率调整匹配了智能体的“记忆衰减”注意力模式，解决了时间错配；SSP通过结合显式结构先验（边缘检测）与隐式注意力显著性，并引入均匀网格采样来保障全局网格完整性，解决了空间拓扑冲突。这种协同设计使得GUIPruner能在显著降低计算开销（如FLOPs减少3.4倍）和加速视觉编码的同时，保留原始模型超过94%的性能，实现高效、高精度的实时GUI导航。

### Q4: 论文做了哪些实验？

论文实验围绕GUIPruner框架的有效性、效率和鲁棒性展开。实验设置方面，以Qwen2-VL-2B和Qwen2.5-VL-7B为基础模型，在GUI导航任务上进行监督微调，推理时设置特定温度，并设定方法超参数γ=0.2、ρ=0.3。评估数据集包括移动端的GUI-Odyssey、AndroidControl、AITW和网页端的Mind2Web，均涉及长视野交互和序列视觉历史。对比方法涵盖训练免费的前LLM剪枝方法（DivPrune、CDPruner）和推理中剪枝的In-LLM方法（FastV、MoB）。

主要结果在三种剪枝设置下评估：历史保留率分别为40%、20%、10%，当前帧固定保留75%。关键数据指标显示，在Qwen2-VL-2B上，GUIPruner在所有数据集上均表现优异，例如在Mind2Web（设置I）达到33.6%准确率，显著优于DivPrune（22.8%），接近原始上限（34.5%）。在Qwen2.5-VL-7B上，GUIPruner避免了DivPrune等方法出现的性能崩溃（如Mind2Web从35.2%骤降至7.7%），在设置I下恢复至34.7%。效率方面，在AITW数据集上，GUIPruner将总FLOPs降低3.4倍，视觉编码延迟加速3.3倍，预填充阶段加速1.9倍，GPU内存峰值仅5.9 GB。

此外，消融实验验证了TAR模块的自适应衰减策略优于均匀缩放，SSP模块的均匀网格采样优于随机采样，证实了各组件对保持性能和布局完整性的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文提出的GUIPruner框架虽有效，但仍存在一些局限和可拓展方向。首先，其“训练无关”特性虽利于部署，但可能限制了性能上限；未来可探索轻量微调或适配器模块，使剪枝策略能针对特定任务或界面风格进行优化。其次，当前方法主要针对GUI导航任务，其时空剪枝原则在更复杂的多模态推理（如理解图表、进行算术计算）中可能失效，需研究如何动态保留语义密集区域。此外，剪枝阈值目前可能依赖启发式设置，可引入强化学习让智能体自主学习最优的压缩策略，在效率与精度间实现动态平衡。最后，框架未充分考虑跨应用和跨平台的泛化性；未来可构建更大规模的异构GUI数据集，测试其在未知界面布局下的鲁棒性，并探索将空间拓扑感知机制与现有VLM进行端到端结合的架构创新。

### Q6: 总结一下论文的主要内容

该论文针对纯视觉GUI智能体在处理高分辨率屏幕截图和历史轨迹时存在的严重时空冗余效率瓶颈问题，提出了一个无需训练的轻量级框架GUIPruner。核心贡献在于识别并解决了现有压缩方法中的两个关键错位：一是时间错配，即均匀的历史编码与智能体“渐逝记忆”的注意力模式不符；二是空间拓扑冲突，即非结构化的剪裁破坏了精确定位所需的网格完整性，导致空间幻觉。为解决这些问题，GUIPruner融合了两种策略：时间自适应分辨率（TAR），通过基于衰减的尺寸调整来消除历史冗余；以及分层结构感知剪枝（SSP），在保护全局布局的同时，优先保留交互前景和语义锚点。实验表明，该方法在多种基准测试中均达到先进性能，有效防止了高压缩下大规模模型的性能崩溃。例如，在Qwen2-VL-2B模型上，实现了3.4倍的FLOPs降低和3.3倍的视觉编码加速，同时保持了94%以上的原始性能，从而以最小资源消耗实现了实时、高精度的GUI导航。
