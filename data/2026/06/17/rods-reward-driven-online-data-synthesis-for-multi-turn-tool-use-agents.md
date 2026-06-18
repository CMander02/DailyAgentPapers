---
title: "RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents"
authors:
  - "Ruishan Fang"
  - "Siyuan Lu"
  - "Chenyi Zhuang"
  - "Tao Lin"
date: "2026-06-17"
arxiv_id: "2606.19047"
arxiv_url: "https://arxiv.org/abs/2606.19047"
pdf_url: "https://arxiv.org/pdf/2606.19047v1"
categories:
  - "cs.AI"
tags:
  - "Multi-turn Agent"
  - "Tool-Use Agent"
  - "GRPO"
  - "Online Data Synthesis"
  - "Reinforcement Learning"
  - "Reward-Driven Synthesis"
  - "Dynamic Replay Buffer"
relevance_score: 9.5
---

# RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents

## 原始摘要

Multi-turn tool-use RL is bottlenecked by the rapid depletion of informative samples in static datasets. We observe that the gradient signal in GRPO concentrates on tasks with the highest rollout reward variance, a consequence of the Popoviciu upper bound. Consequently, samples near the agent's capability boundary -- where successes and failures are roughly balanced -- contribute disproportionately large policy gradients. As training progresses, this boundary continuously shifts, which gradually depletes the pool of informative samples in a static dataset. We propose RODS (Reward-driven Online Data Synthesis) to resolve this depletion. RODS closes the loop between RL training and data generation by repurposing the progress reward variance as a practical, zero-cost boundary detector that requires no extra inference beyond the rollouts already computed for training. It continuously identifies such boundary samples, synthesizes new multi-turn variants matching their structural complexity (e.g., API topology and dependency depth) via a skill-aligned resampling pipeline, and manages a dynamic replay buffer that co-evolves with the policy. Starting from 400 human seeds and maintaining an active training pool of ~800 samples, RODS achieves comparable performance to a 17K-sample offline pipeline while requiring roughly 20x fewer trajectories, and improves over fixed-data RL and environment augmentation in our controlled setting.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决训练多轮工具使用型智能体面临的核心困境：在静态数据集中，随着智能体能力提升，有信息量的训练样本会迅速耗尽。研究背景是，基于强化学习（如GRPO）训练智能体时，梯度信号高度集中在智能体能力边界附近（即任务成功率约50%的区域），因为这些任务的奖励方差最大。然而，现有方法存在明显不足：大规模离线合成数据虽然缓解了数据稀缺，但脱离了训练循环，无法追踪智能体能力边界的动态变化；而在线环境增强方法虽能学习，但受限于固定种子数据，同样面临信号枯竭。此外，无约束的在线自生成数据在多轮场景中常导致语义不连贯。因此，本文要解决的核心问题是：如何在极端数据稀缺条件下，动态合成训练数据，使其严格追踪智能体不断变化的能力边界，同时保持多轮对话的语义连贯性，从而避免信号快速耗尽、实现高效持续学习。

### Q2: 有哪些相关研究？

相关研究主要分为数据合成和在线强化学习两类。在数据合成方面，APIGen-MT、TOUCAN、Magnet等框架通过大规模离线生成百万级轨迹，但静态数据无法跟踪模型能力边界变化。FunReason-MT和LoopTool虽能针对特定失败模式进行定向合成，但仍是离线快照，不能适应训练中能力边界的迁移。本文（RODS）的创新在于引入奖励驱动的在线合成循环，动态生成当前能力边界附近的样本。在在线RL和课程学习方面，ScaleEnv、Agent World Model等通过环境模拟提升数据效率，EnvTuning则通过四阶段课程编排环境增强，但受限于种子语料固定多样性，随着模型能力提升梯度信息减少。自博弈方法虽能零数据生成，但难以处理多轮工具使用的长逻辑链。RODS采用补充性方案：以极少量人类数据为结构锚点，利用GRPO的奖励方差作为零成本边界检测器，通过技能对齐重采样生成复杂度匹配的样本，既继承了优先经验回放的定向采样原则，又融合了生成式合成对数据分布的扩展能力。

### Q3: 论文如何解决这个问题？

RODS通过构建一个闭环的奖励驱动数据合成框架，从根本上解决了多轮工具使用强化学习中静态数据集信息样本枯竭的问题。其核心架构由三个相互协同的模块构成。

首先，**基于奖励的种子检测**模块利用GRPO的梯度信号特性。通过Popoviciu不等式推导发现，当任务的平均进度奖励 \(\bar{r}_i\) 接近0.5时，其奖励方差最大，从而产生最密集的策略梯度信号。RODS据此将任务空间动态划分为已掌握、边界和困难三个区域，并选取边界区域（\(\alpha^- \leq \bar{r}_i \leq \alpha^+\)）内的任务作为高价值种子。为确保技能多样性，模块还采用类型配额机制，从不同技能类别（如长上下文、缺失函数）中优先选择方差代理值 \(4\bar{r}_i(1-\bar{r}_i)\) 最高的样本。

其次，**技能对齐的合成**模块对选中的种子进行结构同构的扩展。它并非简单改写，而是提取种子任务的复杂性轮廓（如API依赖的有向无环图和参数流深度），然后通过一个五阶段多智能体流水线生成结构难度相近但逻辑和状态全新的变体。该流水线包含：1）基于API图的计划生成；2）带环境反馈的可执行轨迹生成；3）基于叙事路径的全轨迹语义重写，确保跨轮对话连贯性；4）批判智能体的质量验证与修正；5）可选的对抗性增强（如缺失工具、参数模糊化）。

最后，**动态回放缓冲管理**模块通过双层控制机制确保训练集始终与策略能力边界协同演化。扩展流量控制采用分批注入策略，在epoch边界按比例（\(\beta \cdot |\mathcal{D}_{active}|\)）混合新合成变体，防止分布剧烈偏移。库存管理则通过多层淘汰机制：过滤初始奖励过低的变体、移除飘移至已掌握或不可解区域的旧样本，并基于方差优先级裁剪冗余样本来维持缓冲池规模上限（\(P_{\max}\)）。

该创新方法仅需400个人工种子和约800个活跃样本即可达到17K样本离线管线的性能，效率提升了约20倍。

### Q4: 论文做了哪些实验？

论文围绕五个问题展开了系统性实验。**实验设置**：使用 GRPO 算法在 8×A100 GPU 上训练 Qwen3-4B-Instruct 等模型，采用三阶段课程学习（格式→基础推理→满数据+扩展）。**数据集/基准**：使用 BFCL V3 多轮子集（800个样本，分为Base、Missing Function、Missing Parameter、Long-Context四个平衡子集），400个用于训练，400个用于分布内评估；OOD测试使用 BFCL V4、τ²-bench 和 ACEBench Agent 拆分。**对比方法**：第一层控制对比（相同400种子样本）包括静态数据集基线、环境增强（EnvTuning）和本文的RODS动态边界扩展系统；第二层为数据效率参考，包括使用17K样本的 FunReason-MT-4B 和 GPT-4o、DeepSeek-V3.2-Exp 等大模型。**主要结果**：在 Qwen3-4B 上，RODS 总体得分 56.00%，优于静态数据集（50.00%）和环境增强（50.50%），各子集均有提升（Base 68%、Miss Func 59%、Miss Param 44%、Long-Context 53%）。使用约800个活跃样本即可达到17K样本离线管道的可比性能，数据效率提升约20倍。RODS 在三个模型系列（Qwen3-4B、Qwen2.5-7B、Llama-3.1-8B）上均表现最佳，证明了边界扩展的有效性和跨模型泛化能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面。首先，RODS依赖GRPO的Popoviciu上界来探测能力边界，但该上界对奖励方差极端敏感，可能在奖励稀疏或噪声较大的场景下产生不稳定边界检测。未来可探索更鲁棒的方差估计方法，如基于分位数的边界度量，或引入贝叶斯不确定性估计来替代。其次，当前重采样流程仅关注API拓扑和依赖深度等结构复杂度，未考虑工具执行的环境状态多样性，可能导致合成轨迹陷入局部模式。可以引入对抗性生成或课程学习策略，动态调整合成样本的难度分布。另外，动态回放缓冲区的容量固定为800样本，可能限制了模型对长尾工具调用模式的覆盖。借鉴神经科学中的记忆巩固机制，设计自适应缓冲区分级策略（如将高频任务与罕见任务分离存储）值得尝试。最后，RODS未显式建模多轮交互中的延迟奖励信用分配，可考虑将过程奖励模型与优势函数结合，提升对长序列工具链的梯度利用效率。

### Q6: 总结一下论文的主要内容

本文提出RODS（奖励驱动的在线数据合成）框架，旨在解决多轮工具使用智能体强化学习中的数据稀缺问题。核心挑战在于：静态数据集中信息样本会随训练快速耗尽，导致梯度信号失效。RODS的关键贡献是发现GRPO算法中的进度奖励方差可作为零成本的边界检测器，自动识别模型能力边界附近（成功率约50%）的高信息量样本。方法上，RODS通过技能对齐重采样管道，保持原始种子轨迹的API拓扑结构和依赖深度，合成新的多轮变体，并维护动态回放缓冲区与策略共同进化。实验表明，从400个人工种子出发、保持约800样本的活跃池，RODS即可达到17K样本离线管道的性能，数据效率提升约20倍，并在固定数据RL和环境增强的对比设置中取得显著改进。该工作揭示了多轮工具使用场景下数据合成与策略训练协同演进的核心机制，为数据稀缺下的智能体学习提供了新范式。
