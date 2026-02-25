---
title: "Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight"
authors:
  - "Yi Yang"
  - "Xueqi Li"
  - "Yiyang Chen"
  - "Jin Song"
  - "Yihan Wang"
  - "Zipeng Xiao"
  - "Jiadi Su"
  - "You Qiaoben"
  - "Pengfei Liu"
  - "Zhijie Deng"
date: "2025-11-20"
arxiv_id: "2511.16175"
arxiv_url: "https://arxiv.org/abs/2511.16175"
pdf_url: "https://arxiv.org/pdf/2511.16175v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Vision-Language-Action (VLA)"
  - "机器人控制"
  - "视觉预测"
  - "模型架构"
  - "动作学习"
  - "多模态模型"
  - "指令跟随"
  - "泛化能力"
relevance_score: 7.5
---

# Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight

## 原始摘要

Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉-语言-动作（VLA）模型在机器人学习领域面临的核心挑战。研究背景是，尽管VLA模型通过结合视觉和语言信息来生成机器人动作取得了显著进展，但现有方法存在几个关键不足。首先，低维度的动作信号过于稀疏，难以充分监督处理高维视觉输入的大型模型，导致模型表示能力未被充分利用。其次，现有方法尝试引入对未来视觉状态的预测（视觉前瞻）来提供更密集的监督，但这会带来新问题：直接预测高维视觉状态会分散模型容量、增加巨大训练成本，且视觉状态中的冗余信息会干扰动作学习；而将视觉状态压缩为紧凑信号又会造成信息瓶颈，损失细微的运动变化信息。此外，许多现有方法忽视了语言监督，导致模型的理解和推理能力受损。

因此，本文要解决的核心问题是：如何设计一个VLA框架，既能利用密集的视觉前瞻信号来有效辅助动作学习，又能避免其带来的模型容量分散、训练成本高和信息损失等问题，同时保持并增强模型基于语言的理解与推理能力。为此，论文提出了名为Mantis的新框架，其核心创新是“解耦视觉前瞻”（DVF），通过将视觉状态预测任务从VLA主干模型中分离出来，减轻主干负担，使其能专注于利用语言监督来维持语义理解和推理，从而综合提升模型的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕视觉-语言-动作（VLA）模型中的视觉增强动作学习范式展开，可分为三类：

**1. 视觉预见（Visual Foresight）**：这类方法通过预测未来帧来增强动作预测。显式方法（如生成离散图像token）或隐式方法（联合训练视频生成与动作预测）均试图建立视觉预测与动作间的联系。但像素级预测会引入无关信息，分散模型对动作的专注，且训练成本高，可能导致模型混淆物理运动与外观变化。

**2. 轨迹引导（Track Guidance）**：为克服上述问题，一些研究将视觉状态压缩为紧凑的、面向控制的表示（如关键点轨迹），以捕捉核心物理动态并指导动作。然而，这种压缩会造成信息瓶颈，且从视频中提取的点轨迹精度有限，可能导致更高的动作预测误差。

**3. 潜在动作监督（Latent Action Supervision）**：这类方法使用潜在动作来监督动作预测。通常先训练一个动作量化模型从帧间差异中学习离散潜在动作，再让VLA模型预测这些动作。其利用了帧间动态可表征为动作基元的思想，但训练额外的量化模型增加了计算复杂度。

**本文与这些工作的关系与区别**：Mantis 同样属于视觉增强动作学习的范畴，但提出了**解耦视觉预见（DVF）** 的新框架。与现有方法不同，Mantis 通过元查询和扩散Transformer头，将视觉预见预测从VLA主干模型中解耦出来。这种设计避免了让主干模型直接预测高维视觉状态所带来的容量分散和训练成本问题，也规避了过度压缩视觉信息导致的信息瓶颈。同时，解耦使主干模型能专注于保持通过语言监督获得的理解与推理能力，从而在提升动作学习效果的同时，维持了模型对指令的遵循和泛化能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Mantis的新型框架来解决现有VLA模型在预测高维视觉状态时导致模型能力分散、训练成本高昂，以及在压缩视觉状态时产生信息瓶颈的问题。其核心方法是引入解耦视觉预见（DVF）机制，将视觉轨迹预测从主干网络中分离出来，从而减轻主干网络的负担，使其能够专注于语言监督下的理解和推理任务。

整体框架由三个主要组件构成：主干网络、DVF头部和动作头部。主干网络采用Qwen2.5-VL，负责处理语言指令和当前视觉状态，并生成隐藏表示。DVF头部基于一个扩散Transformer（DiT）构建，通过一个连接器接收主干网络的输出和当前视觉状态的残差连接，专门负责预测未来的图像帧。这种设计使得一组可训练的潜在动作查询（[LAT]）能够自动捕捉描绘视觉轨迹的帧间动态变化，这些动态变化与显式机器人动作相关联，从而为动作预测提供针对性指导。动作头部则利用这些潜在动作查询和额外的动作查询（[ACT]），通过另一个DiT去噪生成未来多步的动作轨迹。

创新点主要体现在三个方面。首先，DVF机制通过解耦视觉预测，避免了主干网络直接生成冗余视觉信息，使其能保持强大的语言理解和推理能力。其次，论文提出了渐进式训练策略，分三个阶段引入不同模态：第一阶段使用人类操作视频训练多间隙视觉预测；第二阶段引入机器人演示数据进行视觉-动作联合训练；第三阶段加入语言监督的混合训练，通过分阶段优化缓解了跨模态竞争和不稳定收敛问题。最后，在推理阶段，论文引入了自适应时间集成（ATE）机制，通过动态分析目标图像块（与指令最相关）和动态图像块（视觉变化显著）的重叠情况，智能地启用或禁用时间集成，从而在保证运动稳定性的同时提升计算效率。

### Q4: 论文做了哪些实验？

论文在仿真和真实世界环境中进行了多组实验。实验设置方面，Mantis模型总参数量为58亿，其中主干网络37亿，解耦视觉预测（DVF）头14亿，动作头0.3亿，VAE 0.3亿。模型使用AdamW优化器，并采用DeepSpeed进行分布式训练。训练分为三个阶段：第一阶段在SSV2数据集（约22万个人类操作视频）上进行预训练；第二阶段在DROID数据集（7.6万个机器人演示片段）上预训练；第三阶段引入语言监督，在38个多模态数据集和DROID上联合训练1.5个周期。下游微调在LIBERO基准上进行30个周期。

主要数据集和基准测试为LIBERO基准，包含Spatial、Object、Goal和Long四个任务套件，每个套件10个任务，每个任务进行50次试验以评估成功率（SR）。真实世界评估在Agilex机器人平台上进行，设计了三个场景，每个场景包含4个域内（ID）和4个域外（OOD）指令，以测试指令遵循、泛化和推理能力。

对比方法包括非视觉增强方法（如Diffusion Policy、OpenVLA、π₀、π₀-FAST、NORA）和视觉增强方法（如ATM、CoT-VLA、WorldVLA、UniVLA、UnifiedVLA、DreamVLA、ℱ₁）。主要结果显示，Mantis在LIBERO基准上取得了96.7%的平均成功率，在四个任务套件中的三个（Spatial: 98.8%, Object: 99.2%, Long: 94.2%）表现最佳，仅在Goal任务（94.4%）略低于最佳方法。在收敛速度实验中，Mantis显著快于传统视觉预测方法（如UnifiedVLA），与非视觉增强方法OpenVLA和潜在动作监督方法UniVLA相当。真实世界实验中，Mantis在ID和OOD指令上的平均成功次数均显著优于开源VLA模型π₀.₅，展示了其优异的指令遵循、泛化和推理能力。消融实验验证了DVF中残差连接和视频预训练的有效性，其中预训练DVF变体取得了96.2%的最高平均成功率。此外，自适应提前终止（ATE）机制将推理计数降低了近50%，同时保持了可比性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的Mantis框架在视觉-语言-动作模型领域取得了显著进展，但其局限性也为未来研究提供了多个探索方向。首先，模型在真实世界场景中因缺乏机器人本体状态输入而出现轻微动作回滚，这表明未来可整合更丰富的多模态输入，如3D点云、力觉传感器数据或本体感知信息，以提升动作执行的稳定性和精确性。其次，尽管解耦视觉预测降低了主干网络负担，但扩散Transformer头的引入可能增加推理延迟，未来需优化轻量化架构或蒸馏技术以提升实时性。此外，模型依赖大量多源数据预训练，未来可探索更高效的小样本迁移机制或元学习策略，增强对稀缺任务场景的适应能力。从方法创新角度看，可进一步研究视觉轨迹隐动作的自动化解耦程度，结合因果推理或符号学习提升模型的可解释性。最后，当前评估集中于机械臂操作任务，未来可扩展至动态环境或多智能体协作场景，验证框架的通用性与鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了一种名为Mantis的新型视觉-语言-动作（VLA）模型框架，其核心贡献是引入了“解耦视觉预见”（DVF）机制，以解决现有VLA模型在训练效率、信息瓶颈以及语言理解与推理能力不足等方面的问题。

具体而言，Mantis将高维视觉状态的预测任务从VLA主干模型中解耦出来，通过结合元查询（meta queries）和扩散Transformer（DiT）头来实现。该方法将当前视觉状态通过残差连接提供给DiT，并采用简单的下一状态预测目标，使得元查询能够自动捕捉刻画视觉轨迹的潜在动作，从而促进显式动作的学习。这种解耦设计减轻了主干模型的负担，使其能够通过语言监督保持强大的理解和推理能力。

实验表明，在人类操作视频、机器人演示和图像-文本对上进行预训练后，Mantis在LIBERO基准测试的微调中取得了96.7%的成功率，超越了现有基线并展现出高收敛速度。真实世界评估也证实，Mantis在指令跟随、对未见指令的泛化以及推理能力上均优于领先的开源VLA模型。该工作为平衡视觉预测与语言理解提供了有效方案，并开源了代码与权重以推动社区发展。
