---
title: "AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models"
authors:
  - "Shouwei Ruan"
  - "Bin Wang"
  - "Zhenyu Wu"
  - "Qihui Zhu"
  - "Yuxiang Zhang"
  - "Jingzhi Li"
  - "Yubin Wang"
  - "Xingxing Wei"
date: "2026-06-08"
arxiv_id: "2606.08952"
arxiv_url: "https://arxiv.org/abs/2606.08952"
pdf_url: "https://arxiv.org/pdf/2606.08952v1"
categories:
  - "cs.AI"
tags:
  - "LLM/VLM Agent"
  - "Spatial Reasoning"
  - "Cognition Mapping"
  - "Tool-Use"
  - "Reinforcement Learning"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models

## 原始摘要

Multimodal Foundation Models (MFMs) have made substantial progress, yet remain fragile in spatial reasoning over the physical world. A key bottleneck lies in their inability to transform local egocentric observations into a global allocentric spatial representation. To address this, we propose AlloSpatial, an agentic framework for allocentric spatial cognition in foundation models. AlloSpatial introduces World2Mind, a plug-and-play cognitive mapping sandbox that converts egocentric observations into structured allocentric priors, including Allocentric-Spatial Trees and route maps that support querying object topology, geometric relations, passability, and trajectories. To utilize these priors reliably under noisy reconstruction and ambiguous visual evidence, AlloSpatial introduces a Spatial Reasoning Harness for tool-use judgment, modality-decoupled cue collection, and geometry-semantic arbitration. We further internalize this process in Qwen3-VL through cold-start reinforcement learning with a harness-gated trajectory-level reward. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models by 5%-18% in a training-free setting, while ASTs alone support strong spatial reasoning even when visual inputs are removed. The trained AlloSpatial agents further outperform larger general-purpose models and competitive spatial baselines, suggesting that structured allocentric representations, active tool use, and verifiable reasoning offer a promising route toward spatially capable foundation models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态基础模型（MFMs）在物理世界空间推理中的脆弱性问题。目前，MFMs主要处理局部、瞬时的以自我为中心的观察（egocentric observations），缺乏将这些局部感知转换为全局、持久、可查询的异中心空间表征（allocentric spatial representation）的能力。现有方法存在不足：视觉中心方法在训练分布外性能退化；几何中心方法需要大量配对数据和专门架构；工具增强方法则因返回像素级或低级几何测量，导致模型需通过冗长且易错的推理链来组装高阶空间结构，且容易吸收噪声或不完整的工具结果。为此，论文提出AlloSpatial框架，核心目标是构建一个代理系统，使基础模型能够利用结构化的异中心空间先验（如异中心空间树AST和路线图）进行可靠的空间推理。该框架通过引入World2Mind认知映射沙盒将自我中心观察转换为可查询的先验，并设计了空间推理约束机制（Spatial Reasoning Harness）来规范工具调用、证据收集和跨模态仲裁，从而解决现有方法在可靠利用结构化空间信息方面的局限。

### Q2: 有哪些相关研究？

相关研究主要分为三类:视觉导向方法、几何导向方法和工具增强方法。视觉导向方法(如SpatialVLM、Cambrian-S、SpatialReasoner、Spatial-MLLM)通过3D监督数据训练模型理解空间关系,但本文指出这些方法可能依赖训练分布统计特征,在场景布局变化时性能下降。几何导向方法(如SpatialBot、MM-Spatial、SD-VLM、N3D-VLM)通过RGB-D输入、深度图、点云等显式空间信号增强几何理解,但存在跨模态对齐挑战和数据需求高的问题。工具增强方法(如Think3D、pySpatial、SpaceTools、SpatialDreamer)让模型主动调用外部模块获取空间证据,但大多返回渲染视图、深度图等低层次信息,迫使模型通过长推理链构建空间结构。AlloSpatial的创新在于将噪声3D重建转化为紧凑的异中心空间表示(Allocentric-Spatial Trees),并通过Spatial Reasoning Harness实现工具调用、模态解耦证据收集和几何-语义仲裁,让模型基于结构化异中心空间记忆而非孤立自我中心观察或低级几何线索进行推理,从而避免长推理链的误差累积问题。

### Q3: 论文如何解决这个问题？

论文提出了一种名为AlloSpatial的智能体框架，以解决基础模型在空间推理中无法将自我中心观察转化为全局异中心表征的核心瓶颈。整体框架由三个核心组件构成：World2Mind认知映射沙箱、空间推理控制框架和基于强化学习的策略内化。

World2Mind是一个即插即用的认知映射模块，它将自我中心的图像序列转换为结构化的异中心先验知识。具体流程包括：首先通过单目几何模型估计每帧的深度图和相机姿态，并利用SAM 3提取开放词汇语义掩码；然后应用两级置信度滤波（像素级和帧级阈值）过滤不可靠的几何信息，采样有效点反投影到世界坐标系生成全局语义点云；接着通过K近邻密度去除稀疏离群点。基于过滤后的点云，World2Mind构建两种互补的异中心表征：1）异心空间树(AST)，通过自适应DBSCAN分离实例并用椭圆或矩形脚印参数化每个对象的中心、尺寸、朝向和垂直范围，编码层次包含关系；2）路线地图，对可通行区域进行体素化和栅格化，结合相机轨迹支持路径推理。

空间推理控制框架设计为一个循环协议，包含三个关键阶段：工具调用判断，模型先形成空间假设再决定是否需要查询World2Mind；模态解耦的证据收集，通过视觉、AST文本和可选俯视图三个独立通道收集证据；以及几何-语义交织仲裁，比较各模态证据的冲突，识别重建漂移、缺失实例等问题，决定是精化查询还是输出最终答案。该框架将外部认知地图视为可证伪的推理证据而非直接伪标签。

对于开放权重模型，论文通过监督冷启动(从专有模型蒸馏正确轨迹)和在线强化学习(使用控制门控的轨迹级奖励)将这一流程内化到Qwen3-VL策略中，使其学会稳定的多轮工具使用和跨模态仲裁行为。

### Q4: 论文做了哪些实验？

论文在VSI-Bench和MindCube两个基准测试上进行了实验，分别包含392和1050个问题。实验设置了两种评估模式：零样本设置（均匀采样最多32帧）和稀疏视觉输入设置（均匀采样7帧，用于训练后模型对比）。对比方法包括GPT-5.2、Claude-4.6-Opus等闭源模型，Qwen3-VL等开源模型，以及Spatial-MLLM、Think3D等专用空间推理模型。

主要结果：零样本下，AlloSpatial在VSI-Bench上提升GPT-5.2、Claude-4.6-Opus、Gemini-3-Pro分别为+7.3、+17.7、+5.8个整体点；MindCube上提升+4.7、+14.4、+6.5点。训练后，AlloSpatial-8B在VSI-Bench上取得最佳整体分数，AlloSpatial-4B排名第二，均超越GPT-5.2等更大模型。在MindCube上，AlloSpatial-4B达到69.1%整体准确率，远超Gemini-2.5-Pro的57.9%和Think3D的44.0%。消融实验显示，基于强化学习的Stage-2比SFT冷启动Stage-1在VSI-Bench上提升15.3个点（从38.2%到53.5%）。此外，在移除视觉输入的纯文本盲测中，AST空间树仍能有效支持空间推理，尤其在物体大小和路径规划任务上。

### Q5: 有什么可以进一步探索的点？

现有研究在以下方面存在局限性和改进空间：1) **细粒度度量精度不足**：World2Mind的AST和路径地图在粗粒度关系推理上表现优异，但在绝对距离、物体计数等精确数值估计任务上提升有限。未来可引入更精确的3D重建技术（如NeRF或3D高斯泼溅）来提升空间度量准确性。2) **冷启动数据依赖**：当前冷启动阶段依赖GPT-5.2和Claude-4.6-Opus蒸馏工具使用轨迹，这限制了方法的自主性和可扩展性。可探索通过自我探索式强化学习或在线学习让模型自主习得工具调用策略。3) **帧数敏感性**：实验显示性能随输入帧数变化，未来可研究自适应帧选择策略，根据任务复杂度动态决定观察帧数。4) **跨领域泛化**：当前评估集中在室内场景基准，可扩展至室外大场景、动态环境或多智能体协作场景，验证Allocentric表示在不同领域中的通用性。此外，将AST与更紧凑的隐式表示耦合、或引入多任务学习也值得探索。

### Q6: 总结一下论文的主要内容

多模态基础模型在物理世界的空间推理中仍然脆弱，其核心瓶颈在于无法将局部自我中心观察转换为全局的异中心空间表征。为此，本文提出 AlloSpatial，一个用于基础模型异中心空间认知的智能体框架。核心贡献为 World2Mind，一个即插即用的认知映射沙盒，能将自我中心观察转换为结构化的异中心先验知识，包括用于查询物体拓扑、几何关系、可通行性和轨迹的异中心空间树和路径地图。为了在噪声重建和模糊视觉证据下可靠利用这些先验，框架引入了空间推理约束，用于工具使用判断、模态解耦线索收集和几何-语义仲裁。通过在 Qwen3-VL 上使用约束门控的轨迹级奖励进行冷启动强化学习来内化该过程。在 VSI-Bench 和 MindCube 上的实验表明，AlloSpatial 在无需训练的设置下将闭源模型提升 5%-18%，且即使移除视觉输入，异中心空间树本身也能支持强大的空间推理。训练后的 AlloSpatial 智能体进一步超越了更大规模的通用模型和竞争性的空间基线，表明结构化的异中心表征、主动工具使用和可验证推理为打造具备空间能力的基础模型提供了一条有前景的路径。
