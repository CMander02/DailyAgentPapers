---
title: "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination"
authors:
  - "Chenyv Liu"
  - "Wentao Tan"
  - "Lei Zhu"
  - "Fengling Li"
  - "Jingjing Li"
  - "Guoli Yang"
  - "Heng Tao Shen"
date: "2026-02-25"
arxiv_id: "2602.21633"
arxiv_url: "https://arxiv.org/abs/2602.21633"
pdf_url: "https://arxiv.org/pdf/2602.21633v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.CV"
tags:
  - "Agent 架构"
  - "机器人操作"
  - "世界模型"
  - "在线规划"
  - "动作精炼"
  - "自我改进"
  - "视觉-语言-动作模型"
  - "强化学习"
relevance_score: 8.5
---

# Self-Correcting VLA: Online Action Refinement via Sparse World Imagination

## 原始摘要

Standard vision-language-action (VLA) models rely on fitting statistical data priors, limiting their robust understanding of underlying physical dynamics. Reinforcement learning enhances physical grounding through exploration yet typically relies on external reward signals that remain isolated from the agent's internal states. World action models have emerged as a promising paradigm that integrates imagination and control to enable predictive planning. However, they rely on implicit context modeling, lacking explicit mechanisms for self-improvement. To solve these problems, we propose Self-Correcting VLA (SC-VLA), which achieve self-improvement by intrinsically guiding action refinement through sparse imagination. We first design sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. Then we introduce the online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. Evaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieve state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments. Code is available at https://github.com/Kisaragi0/SC-VLA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉-语言-动作（VLA）模型在机器人操作任务中存在的核心问题：模型主要依赖对离线数据统计模式的拟合，缺乏对底层物理动态的鲁棒理解，且难以实现基于内部状态的自适应改进。

研究背景是，VLA模型通过大规模模仿学习实现了从语言指令到动作的映射，但其策略严重受限于预训练数据中的静态先验，泛化能力不足。为增强物理基础，强化学习被引入以通过环境交互和奖励信号优化策略。然而，现有方法（包括在线/离线强化学习以及利用大语言模型合成奖励的方法）普遍依赖**外部定义的奖励信号**。这些外部信号与智能体的内部状态存在脱节，难以针对多样化的复杂任务进行有效设计，从而限制了策略的自我改进能力。另一方面，世界模型虽能内部模拟物理动态，但现有VLA强化学习方法通常将世界模型与策略模块分离，未能充分利用其预测能力。新兴的“世界动作模型”范式虽能同时生成动作和预测未来状态，但缺乏**明确的机制**来利用这些预测状态主动修正动作，无法实现与内部状态对齐的自我优化。

因此，本文要解决的核心问题是：如何让VLA模型摆脱对外部奖励信号的依赖，通过其内部对未来状态的“想象”来**内在地引导动作的在线细化与自我改进**，从而在复杂的机器人操作任务中实现更鲁棒、更高效的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：VLA模型、VLA的强化学习方法，以及世界动作模型。

在**VLA模型**方面，相关工作如RT-2、OpenVLA、GR00T和π₀，它们通过将动作建模为离散标记或改进架构来整合多模态与机器人控制。然而，这些方法主要依赖离线模仿和当前步的语义对齐，缺乏对物理动态演化的显式建模。本文的SC-VLA则旨在通过在线想象和修正来增强对物理演化的理解。

在**VLA的强化学习**方法中，现有工作主要通过构造外部奖励来引导策略。这包括：1）利用视觉语言模型进行语义推理以生成奖励（如VLA-RL、VLAC）；2）基于规则或辅助预测目标设计奖励（如Self-Improving、NORA-1.5）；3）基于特征或轨迹相似度构建奖励（如ThinkAct、VLA-RFT）。这些方法虽提升了探索效率，但通常依赖外部模型、手工规则或相似度计算，与策略内部表征解耦，且增加了复杂性。本文方法与之不同，它通过内部稀疏想象生成依赖进度的密集奖励，实现了与策略更紧密耦合的在线精炼。

在**世界动作模型**方面，如GR-MG、FLARE、PAR和WorldVLA，它们在一个统一框架内联合建模动作生成与未来演化，通过潜在上下文预测来约束策略。但这些方法中的未来信号通常是隐式表征，缺乏可解释的物理语义和显式的自我评估机制，难以进行细粒度轨迹修正。本文SC-VLA通过设计显式的稀疏世界想象（预测任务进度和未来轨迹趋势）并引入在线动作精炼模块，弥补了这一不足，实现了基于预测状态的显式自我改进。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“自我纠正视觉-语言-动作模型”的两阶段框架来解决现有方法在物理动态理解、自我改进机制和奖励稀疏性方面的局限。其核心方法整合了稀疏世界想象与在线动作优化，实现了无需外部密集监督的自主改进。

整体框架分为两个阶段。第一阶段是基础策略生成，采用基于扩散Transformer的骨干网络，接收由视觉语言模型融合的多模态观测作为条件输入。其创新点在于引入了“稀疏世界想象”机制：在查询序列中显式加入了预测任务进度和未来短时状态变化（如末端执行器位姿的相对变化）的辅助目标，并通过在Transformer中间层提取特征，用轻量级MLP头进行预测。这些预测与动作生成通过联合优化目标共同训练，使模型内部编码了物理演化先验，为后续优化提供了可解释的稀疏世界表示。

第二阶段是在线动作优化模块，旨在对基础策略进行微调以适应动态环境。其关键设计是残差策略结构：基础策略保持冻结，而一个轻量级的残差策略（采用SAC算法优化）基于第一阶段预测的稀疏世界想象观测（包含当前状态、预测进度和状态变化）来输出动作修正量。最终动作为两者加权和。这平衡了先验知识的稳定性与在线适应性。

为解决环境奖励稀疏问题，论文提出了一个由内部预测驱动的稠密奖励机制。该机制利用基础策略预测的短时状态变化（特别是位置变化）来定义一个短期目标方向，并计算实际位移与该预测方向之间的对齐度作为引导奖励。此外，通过动态权重调度，利用预测的任务进度来调整引导奖励的权重：在任务早期强调预测先验的引导，在后期接近接触等精细阶段则减弱其影响，更多地依赖真实环境反馈。这使得智能体能在探索效率与对真实动态的敏感性之间取得平衡。

综上，SC-VLA通过稀疏世界想象显式编码物理演化，并利用其产生的内部一致性信号来构建稠密奖励、指导残差策略的在线优化，从而实现了端到端的自我改进，无需依赖外部设计的密集奖励。

### Q4: 论文做了哪些实验？

论文在仿真和真实机器人环境中进行了系统性实验。实验设置方面，在仿真平台ManiSkill3上选择了StackCube、PlaceSphere、PegInsertion和LiftPegUpright四个复杂操作任务，每个任务使用100条演示数据训练，并在50个测试回合中评估。真实实验使用ARX5机械臂，在StackCube、PlaceSphere、PegInsertion和PushCube四个任务上进行，每个任务使用60条演示数据训练，并进行20次执行试验。

对比方法包括基于扩散控制的Diffusion Policy (DP)、基于动作分块的ACT、流匹配策略π₀以及基础模型GR00T N1.5。评估指标主要包括任务成功率和平均完成步数（用于衡量探索效率和系统吞吐量）。

主要结果显示，在ManiSkill仿真基准上，SC-VLA (SPI, OAR)取得了最佳平均成功率86%，在最具挑战性的PegInsertion任务上比π₀和GR00T N1.5分别提升28%和10%。在效率方面，SC-VLA平均完成步数为157步，比π₀减少43%，比DP减少8%。消融实验表明，移除状态引导（Δs_t）使平均成功率从82%降至78%，移除进度引导（p_t）降至80%，同时移除两者则大幅降至72%。稀疏世界想象奖励在复杂任务（如PegInsertion）中将平均步数从800步减少至650步，动态权重调度机制对防止先验偏差干扰精细操作至关重要。在真实世界实验中，SC-VLA (SPI)取得了71%的平均成功率，分别比DP和GR00T N1.5高出43%和14%。

### Q5: 有什么可以进一步探索的点？

该论文提出的SC-VLA框架虽在稀疏世界想象与在线动作修正方面取得进展，但仍存在若干局限与可拓展方向。首先，其稀疏想象依赖辅助预测头来估计任务进度与轨迹趋势，这可能在高度动态或非结构化环境中泛化不足，未来可探索更稠密或层次化的想象机制以捕捉复杂物理交互。其次，在线修正模块基于预测的未来状态调整奖励，但未深入处理长期规划与部分可观测性问题，可结合序列模型或记忆增强架构以提升多步决策能力。此外，实验集中于机器人操控任务，未来需验证在更广泛领域（如导航、人机协作）的适用性。从方法学角度，可进一步研究如何将语言指令更深度融入想象过程，实现语义引导的预测，或引入元学习机制使模型能在线适应新任务而不依赖大量微调。最后，当前框架在计算效率与实时性方面的权衡未充分探讨，优化稀疏想象的推理开销将是实际部署的关键。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为SC-VLA的自校正视觉-语言-动作模型，旨在解决现有VLA模型对物理动态理解不足、强化学习依赖外部奖励信号以及世界动作模型缺乏显式自我改进机制的问题。其核心贡献在于通过稀疏世界想象实现在线动作精炼，从而实现自我改进。方法上，首先设计了稀疏世界想象模块，通过集成辅助预测头来预测当前任务进度和未来轨迹趋势，从而约束策略以编码短期物理演化；随后引入在线动作精炼模块，基于预测的稀疏未来状态重塑与进度相关的密集奖励，调整轨迹方向。主要结论显示，在模拟基准和真实世界的机器人操作任务中，SC-VLA实现了最先进的性能，比最佳基线方法减少了16%的步骤并提高了9%的成功率，在真实世界实验中获得了14%的性能提升，显著提高了任务吞吐量。
