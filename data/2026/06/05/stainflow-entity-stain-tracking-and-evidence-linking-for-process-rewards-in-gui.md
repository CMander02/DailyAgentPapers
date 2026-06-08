---
title: "StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents"
authors:
  - "Haojie Hao"
  - "Longkun Hao"
  - "Yihang Lou"
  - "Yan Bai"
  - "Zhenyang Li"
  - "Zhichao Yang"
  - "Dongshuo Huang"
  - "Hongyu Lin"
  - "Lanqing Hong"
  - "Jiakai Wang"
  - "Xianglong Liu"
date: "2026-06-05"
arxiv_id: "2606.07027"
arxiv_url: "https://arxiv.org/abs/2606.07027"
pdf_url: "https://arxiv.org/pdf/2606.07027v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Process Reward Model"
  - "Reinforcement Learning"
  - "Entity Tracking"
  - "多智能体协作"
relevance_score: 8.5
---

# StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents

## 原始摘要

Reinforcement Learning (RL) has become a promising approach for improving GUI Agents in long-horizon, stochastic digital environments, but trajectory-level success feedback is too sparse to provide reliable credit assignment for intermediate exploration steps. To mitigate this issue, recent studies introduce Process Reward Models (PRMs), which provide finer-grained training feedback through global milestone verification or local step-level evaluation. However, these methods still suffer from two level-specific limitations: global milestone decomposition is subjective and singular, making it difficult to accommodate the multiple valid execution paths in real GUI tasks, while fixed local judging windows may miss long-range key evidence or dilute the decision signal with irrelevant frames. Inspired by stain-tracing mechanisms in network flow analysis, we propose StainFlow, an entity-stain-flow process reward model for GUI Agents. To reduce the subjectivity of global partitioning, we introduce the Global Entity Stain Tracking module, which extracts visually verifiable task entities and tracks how their stain concentrations and states evolve along the trajectory, allowing task phases to be objectively separated by changes in the entity evidence flow. To improve the accuracy of local verification, we introduce the Local Stain Evidence Linking module. Centered on the triggering entities of each candidate key node, it retrieves relevant steps based on their stain concentrations and state changes, and dynamically constructs high-density evidence windows for verifying true key nodes. Extensive experiments on AndroidWorld and OGRBench show that StainFlow relatively improves online RL success by 3.2% and trajectory completion judgment accuracy by 1.8%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习的GUI智能体在长程、随机数字环境中面临的奖励稀疏和信用分配困难的问题。现有方法（如过程奖励模型PRMs）虽能提供更细粒度的反馈，但存在两个层次局限：一是全局里程碑分解方面，基于预设或生成子目标序列的方法具有主观性和单一性，难以适应GUI任务中多样的有效执行路径，可能导致对实际进展的评分偏差；二是在局部步骤评估方面，采用固定长度上下文窗口的方法容易遗漏远距离关键证据（如首次目标发现），或引入无关画面稀释决策信号。为克服这些不足，本文受网络流分析中污渍追踪机制的启发，提出了StainFlow模型。其核心创新在于将GUI任务中可视觉验证的实体转化为动态的污渍信号，通过全局实体污渍追踪模块客观地依据实体证据流的变化划分任务阶段，并通过局部污渍证据链接模块围绕触发实体动态构建高密度证据窗口，以验证关键节点。最终，StainFlow旨在提供更客观、精确的步骤级奖励信号，改善强化学习的信用分配，从而提升GUI智能体在长程任务中的学习效率和成功率。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**方法类**中，全局方法如GUI-PRA、ProgRM、ADMIRE通过轨迹或任务阶段估计进度，但可能将多解任务绑定到单一子任务链；OS-Themis通过代理流程迭代里程碑缓解此问题，但推理成本高。局部方法如GUI-Shepherd、OS-Oracle、GUI-Critic-R1直接判断动作或短上下文，但易遗漏长程视觉证据。本文与它们不同，通过实体污点流实现客观全局划分和局部证据组织。**应用类**包括基于在线强化学习的GUI代理系统如DigiRL、ZeroGUI、ARPO，它们依赖稀疏的轨迹级成功信号，本文提出的StainFlow为其提供更细粒度的过程奖励。**评测类**基准如AndroidWorld、OSWorld、WebArena衡量任务最终成功，过程奖励基准如OS-Oracle、GUI-Critic-Test关注步骤正确性或局部评判，但缺乏全轨迹步骤值评估。本文通过下游RL训练和轨迹筛选效果进行更全面的过程奖励评估。

### Q3: 论文如何解决这个问题？

StainFlow通过实体染色追踪和证据链接两个核心模块来解决GUI代理中过程奖励的稀疏性和主观性问题。整体框架将GUI过程奖励建模为轨迹证据的流动、记录和检索过程。

全局实体染色追踪模块首先使用辅助VLM从指令中提取可视觉验证的任务实体集合，包括实体名称、可检查规则和属性权重。在每一步，通过实体观察函数解析实体视觉状态，包括视觉证据标志、置信度、状态变化描述和当前状态。基于这些信息，实体获得染色浓度：出现在当前截图中的实体浓度为识别置信度，否则按特定衰减因子递减。通过设置染色阈值和变化阈值，从实体状态和染色动力学中召回候选关键步骤，使任务阶段从执行轨迹中自然涌现，避免了主观的里程碑分解。

局部染色证据链接模块针对每个候选节点的触发实体，在整个轨迹中检索其染色历史中的高染色步骤、突变步骤和状态转换步骤，构建动态证据窗口。通过VLM基于指令、复合证据、触发实体和已接受关键节点历史进行验证，确认引入新任务相关状态变化的节点。最终，连续染色项聚合作体浓度提供密集自适应反馈，离散关键节点项奖励关键进展，两者加权组合作为步骤奖励。在线RL中采用组级优势估计和标准化，实现细粒度信用分配。

### Q4: 论文做了哪些实验？

论文在AndroidWorld和OGRBench两个基准上进行了在线强化学习（RL）实验和推理时轨迹完成判断实验。在线RL实验使用Qwen3-VL-8B作为策略模型，分别以Qwen3.5-VL-9B和Qwen3.5-VL-27B作为辅助验证器，在AndroidWorld的928条轨迹上训练5个epoch，batch size为64，GRPO组大小为8，学习率1e-5，η=0.5。对比方法包括GUI-Critic-R1、ADMIRE和OS-Themis。主要结果：StainFlow在Qwen3.5-27B下取得62.28%的成功率，相对最优基线OS-Themis（60.34%）提升3.2%；成功/失败轨迹奖励分别为0.81/0.39，奖励差距0.42，优于其他方法。推理时轨迹完成判断实验在OGRBench的五个子集（Ubuntu、Mobile、Windows、MacOS、Web）上进行，对比DigiRL、ZeroGUI和OS-Themis。使用Gemini-3-Flash时，StainFlow取得88.2%的整体准确率和F1分数，相对OS-Themis（86.6/86.2）提升1.8%。消融实验表明，全局实体污点追踪和局部污点证据链接两个模块协同工作最佳，关键超参数η=0.5，持久实体污点衰减因子0.8，临时实体污点衰减因子0.5。

### Q5: 有什么可以进一步探索的点？

这篇论文的局限和未来方向主要集中在几个方面。首先，StainFlow 的 “stain” 定义目前依赖预定义的实体类型（如文本、图标），这限制了其在高度动态或抽象视觉元素（如渐变按钮或动态动画）上的泛化能力。未来可以探索一种基于深度视觉特征的无监督实体发现机制，让模型自动学习并跟踪任何具有任务语义的视觉斑点，从而增强对 GUI 界面的适应性。其次，当前方法仅在中小规模数据集上验证，计算资源限制了其在更长轨迹和更大规模模型上的应用。随着计算资源扩展，可以验证 StainFlow 在更大参数基座模型（如 7B 以上）上的效果，特别是在需要复杂推理和多步规划的端到端强化学习场景中。此外，目前的证据链接主要基于触发实体，未来可以考虑引入时间衰减或图神经网络建模实体间关系，以更鲁棒地处理长程依赖中的噪声干扰，并探索将 stain 流与大型语言模型的过程监督 token 结合，形成混合奖励信号。

### Q6: 总结一下论文的主要内容

StainFlow 提出了一种基于实体污点追踪的过程奖励模型（PRM），用于解决GUI智能体在强化学习中奖励稀疏和信用分配不准确的问题。现有PRM方法存在全局里程碑分解主观单一（难以适应多种有效执行路径）和局部证据窗口固定（可能遗漏远距离关键证据或稀释决策信号）的局限性。受网络流分析中污点追踪机制的启发，StainFlow将GUI轨迹中的关键实体建模为动态污点信号。其主要贡献在于：通过全局实体污点追踪模块，根据实体可见性和状态变化动态调整污点浓度，从而客观地划分任务阶段；通过局部污点证据链接模块，围绕触发实体检索相关步骤，构建自适应的高密度证据窗口以验证关键节点。实验表明，在AndroidWorld和OGRBench基准上，StainFlow将在线强化学习的成功率相对提升了3.2%，轨迹完成判断准确率提升了1.8%，实现了更客观、细粒度的信用分配。
