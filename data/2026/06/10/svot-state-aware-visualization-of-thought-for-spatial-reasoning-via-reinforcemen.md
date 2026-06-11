---
title: "SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning"
authors:
  - "Chao Lei"
  - "Yanbei Jiang"
  - "Markus Hiller"
  - "Zhijian Zhou"
  - "Xunye Tian"
  - "Krista A. Ehinger"
  - "Nir Lipovetzky"
date: "2026-06-10"
arxiv_id: "2606.11770"
arxiv_url: "https://arxiv.org/abs/2606.11770"
pdf_url: "https://arxiv.org/pdf/2606.11770v1"
categories:
  - "cs.AI"
tags:
  - "MLLM Agent"
  - "自回归推理"
  - "物理世界推理"
  - "强化学习"
  - "空间推理"
  - "可视化思考链"
  - "多模态推理"
relevance_score: 9.0
---

# SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning

## 原始摘要

Spatial reasoning remains a challenge for Multimodal Large Language Models (MLLMs), as it requires reliable multi-hop inference over both intermediate states and state transitions. Current studies often leave intermediate states unverified and treat state transitions as implicit processes, which limits reliability in multi-hop spatial reasoning. To address this, we propose State-aware Visualization-of-Thought (SVoT), a reinforcement learning framework that generates interleaved, verifiable intermediate states and visualizations. SVoT integrates transition reasoning chains into the generation processes, enabling the model to verify action preconditions and effects through interleaved textual and visual reasoning. We train SVoT via Group Relative Policy Optimization (GRPO), instantiating verification through reward design and evaluating the efficacy of different fine-grained rewards. As existing benchmarks reduce state transitions to single-variable updates, substantially simplifying the problems, we establish five domains by extending classical environments and introducing two novel domains, Pacman and Gather, that require multi-object interactions and numerical reasoning. These domains support systematic evaluation of multi-hop spatial reasoning with quantitative verification of generated intermediate states and transition reasoning. SVoT with transition-aware supervision achieves state-of-the-art performance across the introduced domains, yielding up to a 65% absolute accuracy gain on out-of-distribution test sets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态大语言模型（MLLMs）在多跳空间推理中存在的可靠性和可验证性问题。尽管已有VQA基准和可视化思维（VoT）等方法，但仍存在两个关键不足：一是现有评估基准大多将目标简化为单一状态变量或二元成功标志，导致状态转换退化为单变量更新，弱化了多对象交互使得多跳推理缺乏真正挑战性；二是缺乏对中间状态的显式验证和状态转换推理，无法确定模型是真正逐步推理正确还是偶然到达正确最终状态，从而限制了序列状态跟踪的可靠性。为此，论文提出状态感知可视化思维（SVoT），这是一种基于强化学习的框架，通过生成可验证的中间状态和可视化，并将转换推理链集成到生成过程中，使模型能够显式验证动作前提与效果。同时，通过扩展经典环境和引入需要多对象交互与数值推理的新域（如Pacman和Gather），论文建立了五个网格域，支持对多跳空间推理的系统评估和中间状态与转换推理的定量验证，核心目标是提升MLLMs在复杂动态环境中序列状态跟踪的准确性和可验证性。

### Q2: 有哪些相关研究？

基于论文《SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning》，相关研究主要可分为三类：

1. **方法类相关研究**：本文直接借鉴并改进了**Visualization-of-Thought (VoT)** 和**Multimodal Visualization-of-Thought (MVoT)**。VoT 通过在每个推理步骤后生成文本可视化来显式跟踪中间状态，而 MVoT 则利用多模态原生模型生成实际可视化，将文本与视觉统一在推理轨迹中，实现了视觉化的推理过程。本文的 SVoT 与两者的关键区别在于：SVoT 不仅生成可视化，还引入显式的、可验证的中间状态表示和状态转换推理链，并通过强化学习（组相对策略优化 GRPO）和奖励设计（如过程奖励模型 PRM）实现中间状态与推理过程的验证，解决了 VoT 和 MVoT 缺乏中间状态验证和显式状态转换推理的问题。

2. **评测类相关研究**：现有评估多跳空间推理的基准（如 Maze、FrozenLake、Polyomino Tilings）通常将目标规范简化为单一状态变量或二进制成功标志，将状态转换降为单变量更新，削弱了多目标交互的复杂性。本文建立了五个网格域（扩展经典环境 Maze、FrozenLake，加入 Sokoban，并引入新域 Pacman 和 Gather），这些域包含多对象交互（如墙壁、障碍物、方块、硬币、球）和数值推理，支持对中间状态表示和转换推理正确性的定量验证，从而弥补了现有基准在评估多跳空间推理复杂性上的不足。

3. **应用类相关研究**：本文的空间推理与规划能力相关，规划是多模态大语言模型（MLLMs）的核心推理能力，对导航、机器人、自动驾驶等实际应用至关重要。SVoT 通过提升顺序状态跟踪的可靠性和可验证性，直接满足了这些领域对安全规划的基础需求。

总之，SVoT 在方法上超越了 VoT 和 MVoT，在评测上填补了现有基准的空白，并通过强化学习实现了更可靠的多跳空间推理。

### Q3: 论文如何解决这个问题？

SVoT通过强化学习框架实现状态感知的思维可视化，核心方法是将空间推理分解为可验证的中间状态和状态转移推理链。整体架构包含三个关键组件：首先，将任务规范扩充为包含初始状态描述s0的元组X=⟨d, s0, v0, A⟩，其中d是领域描述，v0是初始可视化，A是动作序列。其次，定义中间状态为zi=⟨ai, si⟩，其中ai是动作，si是通过确定性转移函数f(si-1, ai)得到的状态描述，精确编码对象布局、关系和属性。最重要的是，引入转移推理链ci，它作为显式的状态转移函数，帮助模型验证动作前提条件和效果，从而生成中间状态zi及其可视化vi。

技术上，SVoT采用交错的多模态生成过程：先基于前序状态和可视化生成当前转移推理链c_i^z和状态zi，再基于这些信息生成可视化转移推理链c_i^v和可视化vi，最终基于完整轨迹预测目标配置g。训练采用GRPO算法，通过奖励设计实现验证机制，并评估不同细粒度奖励的有效性。创新点包括：将中间状态从单纯的动作预测扩展为(动作,状态描述)元组，实现结构化状态追踪；用显式转移推理链替代隐式状态更新，确保空间推理的可验证性；在五个扩展经典环境（包括Pacman和Gather等需要多对象交互和数值推理的新领域）上实现SOTA，在分布外测试集上获得高达65%的绝对准确率提升。

### Q4: 论文做了哪些实验？

论文在五个空间推理域（Maze、FrozenLake、Sokoban、Pacman、Gather）上进行了实验。数据集的构建扩展了经典环境（Maze、FrozenLake、Sokoban）并引入了两个需要多对象交互和数值推理的新域（Pacman、Gather），每个域包含ID（分布内）和OOD（分布外）测试集，每个域-尺寸组合各有120个实例。对比方法包括：MVoT（最先进的求解器）、两个文本CoT基线（GPT-4o和经过指令微调的Anole），以及SVoT的两种变体SVoT$_{o}$（使用结果奖励模型ORM）和SVoT$_{p}$（使用过程奖励模型PRM）。主要结果以目标预测准确率衡量（自由回答和分类两种输出格式），SVoT$_{p}$在所有域-尺寸组合上均达到最佳性能，特别是在挑战性的OOD和自由回答设置中，在Sokoban的尺寸4上相较于MVoT取得了高达65%的绝对准确率提升。此外，还对单步预测准确率（分析Gather域瓶颈）、生成图像质量（定量和定性分析）以及消融实验（验证可视化、GRPO和过渡推理链的必要性）进行了详细分析，并通过奖励曲线比较了ORM和PRM的优化效果。

### Q5: 有什么可以进一步探索的点？

SVoT框架在空间推理上取得了显著进展，但仍存在若干可探索的方向。首先，其奖励设计对细粒度验证的依赖值得深究：当前通过GRPO优化离散视觉生成，但过渡状态的可信度仍受限于MLLM的视觉感知能力，未来可引入更鲁棒的视觉编码器或自监督一致性约束。其次，基准任务虽新增多目标交互（如Pacman），但状态空间仍较为结构化；将SVoT扩展到非网格化、连续动态环境（如机器人操作）是一个自然延伸，这需生成更复杂的数值推理链。此外，当前训练完全依赖强化学习，未结合预训练知识蒸馏；若用大模型生成的“理想过渡链”作为预训练信号，可降低对任务奖励的初始依赖。最后，SVoT的视觉化状态虽利于验证，但生成成本较高；可探索轻量级符号映射（如草图而非像素级渲染）以平衡效率与推理可靠性，同时保持可解释性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为SVoT（State-aware Visualization-of-Thought）的强化学习框架，旨在解决多模态大语言模型在多跳空间推理中验证中间状态和状态转换不可靠的问题。该框架通过生成交织的、可验证的中间状态与可视化结果，将状态转换推理链条融入生成过程，使模型能够通过文本与视觉的共同推理验证动作的前提条件和效果。训练采用Group Relative Policy Optimization算法，并通过奖励设计实例化验证机制，评估了不同细粒度奖励的效果。由于现有基准将状态转换简化为单变量更新，论文扩展了经典环境并引入Pacman和Gather两个新领域，支持多目标交互和数值推理，从而系统性地评估模型的多跳空间推理能力与中间状态的量化验证。实验表明，基于状态转换感知监督的SVoT在所有引入领域达到了最先进的性能，在分布外测试集上准确率绝对提升高达65%。
