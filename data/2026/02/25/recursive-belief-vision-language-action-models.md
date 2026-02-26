---
title: "Recursive Belief Vision Language Action Models"
authors:
  - "Vaidehi Bagaria"
  - "Bijo Sebastian"
  - "Nirav Kumar Patel"
date: "2026-02-24"
arxiv_id: "2602.20659"
arxiv_url: "https://arxiv.org/abs/2602.20659"
pdf_url: "https://arxiv.org/pdf/2602.20659v2"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Vision-Language-Action Models"
  - "World Model"
  - "Long-Horizon Planning"
  - "Partial Observability"
  - "State Representation"
  - "Robotic Manipulation"
  - "Diffusion Policy"
  - "Self-Supervised Learning"
relevance_score: 9.5
---

# Recursive Belief Vision Language Action Models

## 原始摘要

Vision-language-action models must enable agents to execute long-horizon tasks under partial observability. However, most existing approaches remain observation-driven, relying on short context windows or repeated queries to vision-language models (VLMs). This leads to loss of task progress, action repetition under perceptual aliasing, and high inference latency. While semantic grounding is important, long-horizon manipulation fundamentally requires persistent, action-conditioned state representations. Current VLAs lack such representations and exhibit limited temporal and physical reasoning, making them ill-suited for multi-stage control. This paper introduces RB-VLA, a belief-centric architecture trained with self-supervised world-model objectives that maintains a compact latent state encoding task-relevant history, dynamics, and object interactions. Queried once per task, the VLM provides high-level intent, while the belief tracks task progress and enables phase-aware, causally grounded control under partial observability without storing raw observations or scaling memory with time. The belief and intent jointly condition a diffusion policy for robust closed-loop execution. RB-VLA outperforms prior VLAs on long-horizon benchmarks, achieving 52.5 percent and 37.5 percent higher success rates on multi-stage pick-and-place and stacking tasks, respectively, compared to pi_0. It also reduces inference latency by up to five times relative to baselines and eliminates memory growth across timesteps observed in existing VLAs. Ablations show the belief module is the primary driver of performance, increasing success rates from 32.5 percent without belief to 77.5 percent with belief.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉-语言-动作模型在部分可观测环境下执行长时程任务时存在的核心缺陷。研究背景是，尽管VLA模型结合了语言理解和视觉感知，在机器人控制中展现出良好的泛化能力，但现有方法大多本质上是反应式的，仅基于当前观测或极短的历史窗口来决策。这导致了几大不足：首先，在存在感知混淆、遮挡或观测噪声时，模型容易丢失任务进度、重复执行动作；其次，许多方法依赖频繁查询计算代价高昂的视觉语言模型或扩展上下文窗口，导致推理延迟高且内存随步数增长；再者，现有VLA缺乏对物理动态和动作后果的显式建模，其时间推理和物理推理能力有限，难以胜任需要持续状态表示的多阶段操控任务。

因此，本文要解决的核心问题是：如何为VLA模型构建一个紧凑、持久且以动作为条件的内部状态表示（即信念），使其能够在部分可观测条件下，有效跟踪长时程任务的历史、动态和对象交互，从而实现稳健、高效且具有因果推理能力的闭环控制。论文提出的RB-VLA框架通过自监督的世界模型目标来训练一个递归信念估计器，该信念与VLM一次性生成的高层意图共同条件化一个扩散策略。这种方法将语义推理（稀疏进行）与基于信念的低层控制解耦，从而在无需存储原始观测或进行持续前向仿真的情况下，实现任务阶段感知的、内存恒定且低延迟的长时程操控。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。在方法类中，相关工作包括：1）基于大型语言模型的观察驱动方法，这些方法通过自回归预测动作令牌进行控制，但计算成本高且缺乏持续状态跟踪；2）引入连续动作解码器（如扩散策略）的方法，虽改善了动作生成，但仍依赖密集的语义重复推理；3）为长时程任务引入归纳结构的方法，如预测子目标或依赖手动定义的运动阶段，但需要任务特定的监督。在应用类中，研究如ECoT和ThinkAct通过生成视觉基础推理来改进决策，但主要在图像-文本空间操作，缺乏对任务进展的持续感知。在评测类上，现有方法常面临内存随步骤增长或推理延迟高的问题。

本文提出的RB-VLA与这些工作的关系和区别在于：它通过自监督世界模型目标训练，维护一个紧凑的潜在状态（信念），编码任务相关历史、动态和对象交互，从而替代了昂贵的视觉语言模型重复查询。与观察驱动方法相比，RB-VLA的信念模块提供了固定大小、动态一致的内存，过滤观测噪声并选择性保留信息，解决了感知混淆和内存扩展问题。与基于世界模型的规划方法不同，RB-VLA无需在推理时进行沉重的向前模拟，降低了计算开销。实验表明，RB-VLA在长时程基准测试中优于先前方法，显著提高了成功率和推理效率。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为RB-VLA的信念中心化架构来解决长视野、部分可观测任务中的控制问题。其核心方法是**将语义任务指定与因果状态估计解耦**，并利用一个递归更新的信念状态来追踪物理交互进展，从而避免了对原始观测的依赖和内存随时间的增长。

**整体框架**由三个主要组件构成：
1.  **视觉-语言推理模块**：仅在任务开始时被查询一次，接收语言指令和初始视觉观测，通过一个可学习的查询向量进行注意力池化，提取出一个静态的、图像条件化的语义目标嵌入（意图向量 $\mathbf{I}_t$）。该意图在整个任务执行期间保持不变，将抽象指令与场景中的具体物体绑定。
2.  **信念估计器**：这是系统的核心创新模块。它递归地维护一个紧凑的潜在信念状态 $\mathbf{b}_t$，用于编码任务相关的历史、动力学和物体交互信息。在每个时间步，它整合**前一个信念**、一个固定窗口内的**标记化观测**（包括经DINOv2编码的视觉特征和机器人本体感知信号）、**动作**和**本体状态**。一个时序Transformer用于处理这些信息，并输出一个**证据表示** $\mathbf{e}_t$。为了处理不确定性，模型还引入了一个**随机潜变量** $z_t$，通过先验分布（基于历史）和后验分布（结合新证据）来建模。最终的信念更新通过一个GRU单元实现：$\mathbf{b}_t = GRU(\mathbf{b}_{t-1}, [\mathbf{e}_t, z_t])$。
3.  **扩散策略控制器**：这是一个基于扩散Transformer的低层控制器，以信念 $\mathbf{b}_t$ 和意图 $\mathbf{I}_t$ 为条件，在潜在空间中采样未来动作序列。它采用迭代去噪的方式生成平滑、闭环的控制指令，并以高频率（50 Hz）执行。

**关键技术**与**创新点**包括：
*   **解耦的语义与状态表示**：将静态的语义意图与动态的、递归更新的信念状态分离，使得高层任务语义不随执行过程变化，而底层状态能持续追踪物理进展。
*   **递归信念估计器**：借鉴了RSSM风格的世界模型思想进行训练。其训练目标不仅包括预测下一时刻的潜在观测（通过指数移动平均的帧编码器提供稳定目标），还包含一个轻量级的**多步预测辅助解码器**（预测 $x_{t+5}$），鼓励信念编码更长视野的动态演化。此外，**逆动力学损失**的引入强制信念编码与动作预测相关的可控状态信息。
*   **动作条件化的世界模型训练**：与预测未来视觉嵌入的先前方法不同，RB-VLA的预测目标是**动作接地的**（通过EMA帧编码器），这驱使信念捕捉**动力学**而非仅仅是外观相似性。
*   **高效推理与内存管理**：视觉-语言模型仅被调用一次，极大降低了推理延迟（相比基线提升达5倍）。信念状态的维度固定，不存储原始观测，因此内存不会随时间步增长，解决了现有VLA方法的内存膨胀问题。
*   **处理部分可观测性**：信念状态能够捕获单时间步不可见的信息（如被遮挡物体状态、接触历史、交互阶段），使智能体在视觉证据模糊或缺失时仍能进行阶段感知、因果接地的控制。

总之，RB-VLA通过引入并精心训练一个递归的、动作条件化的信念状态表示，成功地将高层语义规划与低层物理控制桥接起来，在长视野任务中实现了更鲁棒、高效且内存可控的执行。

### Q4: 论文做了哪些实验？

论文在仿真和真实世界环境中进行了系统性实验。实验设置方面，主要使用RoboSuite和LIBERO-Long仿真环境，并在真实UR5机械臂上部署验证。评估任务聚焦于长视野、多阶段操作任务（如多物体拾放和堆叠），并包含部分可观测性（如遮挡）条件。每个任务进行40次随机种子试验，并在推理时通过随机化物体身份、位置、光照、引入丢帧和观测噪声来评估鲁棒性。

使用的数据集/基准测试包括RoboSuite和LIBERO-Long的长视野任务。对比方法包括GROOT-N1、OpenVLA和π_0等基线模型。主要性能指标为任务成功率（在规定步数内无碰撞完成任务的比率）。

主要结果如下：在长视野任务中，RB-VLA显著优于基线。具体数据指标显示，在多阶段遮挡拾放任务上，RB-VLA成功率（77.5%）比π_0（25.0%）高出52.5个百分点，比GROOT-N1（20.0%）高出57.5个百分点；在多阶段堆叠任务上，RB-VLA（80.0%）比π_0（42.5%）高出37.5个百分点。在计算效率方面，RB-VLA仅需在任务开始时调用一次视觉语言模型（VLM），推理延迟比无状态OpenVLA和RT1-X降低5倍以上，比多帧GR00T-N1快3倍以上。内存使用上，RB-VLA通过递归压缩历史到固定大小的信念状态，实现了与时间步长无关的恒定内存占用（相对内存使用始终为1.0倍），而基线模型（如Qwen2-VL-7B和GR00T-N1）的内存随帧数增加呈超线性增长（如8帧时分别达6.82倍和7.12倍）。

消融实验表明，信念模块是性能提升的关键驱动因素：移除信念到策略的调节后，成功率从77.5%降至32.5%；使用完整RB-VLA相比无信念的扩散策略（DiT）成功率提高45个百分点。信念质量分析显示，信念相似性与未来动作相似性（Pearson r=0.87）及未来视觉特征相似性（r=0.78）呈强单调相关，证实其能编码动态状态。真实世界实验中，RB-VLA在未经架构修改下迁移到UR5机械臂，经过100条轨迹微调后，在25次试验中取得68.0%的成功率，实现了低延迟闭环控制。

### Q5: 有什么可以进一步探索的点？

该论文提出的RB-VLA架构在部分可观测环境下通过信念状态实现了长时程任务的高效控制，但仍存在一些局限性和可拓展方向。首先，系统依赖于预训练的视觉语言模型（VLM）提供高层意图，其性能受限于VLM的语义理解能力，在复杂或未见过的任务中可能表现不佳。其次，当前方法主要针对桌面级操作任务，未来可探索在更动态、非结构化的真实场景（如家庭服务、户外导航）中的泛化能力。此外，信念模块虽能压缩历史信息，但如何更精细地建模物体间的物理交互和长期因果推理仍有提升空间。结合个人见解，可能的改进思路包括：引入强化学习或世界模型预训练，使智能体能主动探索并学习恢复策略以应对意外干扰；设计可解释的信念表示，便于人类监督和调试；探索多模态信念融合（如触觉、声音），以增强部分观测下的环境感知。最后，扩展任务多样性并构建更大规模的仿真与真实数据集，将是推动该类方法实际落地的关键。

### Q6: 总结一下论文的主要内容

该论文针对现有视觉-语言-动作模型在部分可观测环境下执行长时程任务时存在的局限性，提出了RB-VLA这一新型架构。核心问题是现有方法多为观测驱动，依赖短上下文或重复查询，导致任务进度丢失、动作重复和推理延迟高，缺乏持久且与动作条件相关的状态表示。

论文的核心贡献是引入了以信念为中心的递归架构。方法上，RB-VLA通过自监督的世界模型目标进行训练，维护一个紧凑的潜在状态，编码任务相关的历史、动态和物体交互。在每个任务中，视觉语言模型仅被查询一次以提供高层意图，而信念模块则持续追踪任务进度，实现在部分可观测下的、具有阶段感知和因果基础的闭环控制，无需存储原始观测值，且内存占用不随时间增长。该信念与意图共同条件化一个扩散策略以执行动作。

主要结论是RB-VLA在长时程任务基准测试中显著优于先前方法，在多阶段抓放和堆叠任务上成功率分别提升52.5%和37.5%，推理延迟降低高达5倍，并消除了内存增长。消融实验表明信念模块是性能提升的主要驱动力，将成功率从无信念时的32.5%提升至有信念时的77.5%。其意义在于为具身智能体在复杂、部分可观测环境中进行鲁棒、高效的长时程操作提供了新的解决方案。
