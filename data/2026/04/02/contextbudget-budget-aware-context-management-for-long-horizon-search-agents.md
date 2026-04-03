---
title: "ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents"
authors:
  - "Yong Wu"
  - "YanZhao Zheng"
  - "TianZe Xu"
  - "ZhenTao Zhang"
  - "YuanQiang Yu"
  - "JiHuai Zhu"
  - "Chao Ma"
  - "BinBin Lin"
  - "BaoHua Dong"
  - "HangCheng Zhu"
  - "RuoHui Huang"
  - "Gang Yu"
date: "2026-04-02"
arxiv_id: "2604.01664"
arxiv_url: "https://arxiv.org/abs/2604.01664"
pdf_url: "https://arxiv.org/pdf/2604.01664v1"
categories:
  - "cs.AI"
tags:
  - "Long-Horizon Reasoning"
  - "Context Management"
  - "Reinforcement Learning"
  - "Compression"
  - "Web Agent"
  - "Budget Constraint"
  - "Sequential Decision"
relevance_score: 8.5
---

# ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents

## 原始摘要

LLM-based agents show strong potential for long-horizon reasoning, yet their context size is limited by deployment factors (e.g., memory, latency, and cost), yielding a constrained context budget. As interaction histories grow, this induces a trade-off between retaining past information and staying within the context limit. To address this challenge, we propose Budget-Aware Context Management (BACM), which formulates context management as a sequential decision problem with a context budget constraint. It enables agents to assess the available budget before incorporating new observations and decide when and how much of the interaction history to compress. We further develop BACM-RL, an end-to-end curriculum-based reinforcement learning approach that learns compression strategies under varying context budgets. Experiments on compositional multi-objective QA and long-horizon web browsing benchmarks show that BACM-RL consistently outperforms prior methods across model scales and task complexities, achieving over $1.6\times$ gains over strong baselines in high-complexity settings, while maintaining strong advantages as budgets shrink, where most methods exhibit a downward performance trend.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在长程推理任务中面临的上下文管理难题。随着智能体在交互式应用中执行更长的轨迹，其交互历史会迅速累积，导致上下文规模急剧膨胀。然而，在实际部署中，上下文窗口的最大容量受到内存、推理延迟和服务成本等资源的严格限制，形成了一个有限的“上下文预算”。这迫使智能体必须在保留历史信息和遵守上下文限制之间做出权衡。

现有方法，尤其是上下文压缩技术，虽然被广泛采用以在固定限制下保留关键信息，但大多采用“无预算”的表述。它们将压缩视为一种静态操作，没有明确考虑可用的上下文预算。这种简化带来了两个关键缺陷：在预算宽松时，智能体可能过度压缩，删除了对研究至关重要的证据，降低了信息保真度；而在预算紧张时，智能体可能压缩不足，导致上下文溢出、截断或脆弱的推理失败。虽然近期研究开始将预算意识引入智能体推理（如工具调用或输出令牌的预算控制），但这些方法主要通过外部控制来调节计算或行动次数，并未系统性地解决当上下文窗口预算本身成为限制资源时，如何主动进行历史压缩的问题。

因此，本文要解决的核心问题是：如何让LLM智能体在明确的上下文窗口预算约束下，进行有效的长程推理。论文提出了“预算感知的上下文管理”框架，其核心思想是将上下文管理中的压缩问题形式化为一个具有预算约束的序列决策问题，使压缩决策能够根据推理过程中剩余的上下文容量进行动态调整。这允许智能体在纳入新观察之前评估可用预算，并决定何时压缩、压缩多少以及保留哪些信息，从而在严格预算下保留关键证据，并在容量充足时避免不必要的信息损失。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕“LLM智能体的上下文管理”和“预算感知的推理扩展”两个类别展开。

在**上下文管理**方面，早期研究通过引入外部记忆系统来扩展可访问的上下文，但这依赖于外部存储而非更新推理过程中的上下文内部表示。近期工作将上下文管理视为压缩问题，旨在固定预算下最大化信息密度。这些方法在单轮次设置中进行输入级压缩，在多轮次设置中则进行连续的状态管理，例如将交互历史映射为有界表示或递归压缩轨迹为高层抽象。然而，现有方法大多采用“无预算”的设定，将压缩视为静态或周期性触发的操作，并未考虑可用的上下文预算。本文的BACM框架则与之不同，它将压缩建模为一个以上下文预算为条件的动态决策过程，使智能体能在保留信息与资源约束之间进行自适应权衡。

在**预算感知推理扩展**方面，先前研究主要在明确资源约束下优化LLM推理，例如控制输出长度或计算量（如令牌预算推理）。但这些工作大多局限于单轮次场景。在智能体设置中，近期研究开始对交互过程进行预算感知控制，例如约束工具使用频率或跟踪多步推理中的资源消耗。然而，这些方法主要调控的是可观察的交互行为（如动作频率），而非根据部署约束导致的上下文窗口限制来调整推理过程本身。因此，当上下文窗口成为主要瓶颈时，现有方法缺乏相应的自适应机制。本文则直接将上下文窗口管理表述为一个预算感知的决策过程，使智能体能够根据实时预算信号动态调整其历史信息表示。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“预算感知上下文管理”（BACM）的框架来解决长视野搜索智能体在有限上下文预算下面临的挑战。其核心方法是将上下文管理形式化为一个受预算约束的顺序决策问题，并引入两个关键机制和一个强化学习优化方案。

整体框架基于一个扩展的马尔可夫决策过程。智能体在每一步接收到一个预算感知状态，该状态不仅包含当前的推理状态和待处理观察的令牌长度，还明确包含了剩余的上下文预算。这种设计使得智能体在加载新观察之前，就能评估可用容量并预先调整现有上下文，从而避免了因上下文溢出导致的推理失败或过早压缩造成的信息丢失。

主要模块包括预算条件推理状态与延迟观察加载机制，以及承诺块聚合机制。前者通过在状态中暴露剩余预算和待加载观察的大小，让智能体能够基于未来所需的容量来指导压缩决策，确保在纳入新观察后上下文总长度不超预算。后者则允许智能体根据动态的预算压力，自适应地决定何时压缩以及压缩多少。具体而言，上下文被组织为一系列语义连贯的片段，策略可以生成三种互斥的结构化动作：不压缩、部分压缩（选择特定子集进行聚合）或完全压缩（聚合所有片段）。这三种动作分别对应高、中、低预算压力下的不同处理模式，从而将压缩的时机和强度决策统一到一个动作空间中。

关键的创新点在于：1）将上下文管理建模为顺序决策问题，使压缩决策与任务推理紧密协同；2）提出的承诺块聚合机制实现了压缩时机和强度的自适应、细粒度控制；3）采用基于课程的强化学习（BACM-RL）进行端到端优化。该方法使用分组相对策略优化（GRPO），通过设置预算逐阶段递减的课程，让智能体学习在变化的预算约束下进行有效的上下文分配。优化目标结合了策略梯度损失和相对于参考策略的KL散度正则化，并通过将轨迹级别的优势信号广播给所有令牌，使模型能够将局部决策与全局有效的上下文管理对齐。

综上所述，该方法通过预算感知的决策框架、自适应的压缩机制以及课程式强化学习，使智能体能够在严格的上下文预算下，动态且高效地管理不断增长的历史信息，从而在长视野任务中实现持续的高性能。

### Q4: 论文做了哪些实验？

论文在组合式多目标问答和长视野网页浏览两个基准上进行了实验。实验设置方面，所有方法均在Qwen2.5-7B-Instruct和Qwen3-30B-A3B-Instruct两个骨干模型上进行评估，上下文预算统一为8k tokens。BACM-RL方法采用课程学习策略，在训练中逐步将上下文预算从8k收紧至4k tokens以鼓励模型适应压力。

使用的数据集/基准测试包括：1）基于Wikipedia的多目标问答基准，由单跳（NQ, TriviaQA, PopQA）和多跳（HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle）数据集转换而成，评估指标为各目标答案的token级F1分数之和；2）BrowseComp-Plus长视野基准，采用LLM-as-Judge协议（使用Qwen3-32B作为评判模型）计算平均准确率。

对比方法分为三类：无上下文管理（ReAct、Search-R1）、反应式上下文管理（Summary Agent，仅在上下文缓冲区满时触发摘要）、以及主动式上下文管理（MEM1，通过强化学习在每一步迭代压缩历史信息）。BACM-RL属于预算感知的主动管理方法。

主要结果显示，BACM-RL在两个基准上均取得最佳平均性能。具体数据指标：在32目标的高复杂度设置下，BACM-RL（30B模型）的累计F1分数达到4.545，远超MEM1的0.909，提升约5倍；在BrowseComp-Plus基准上，BACM-RL（30B，8k预算）准确率达0.147，优于使用128k上下文的235B Qwen3-Inst模型（0.136）。在预算缩减至4k的极端情况下，BACM-RL在32目标设置中仍比最佳基线累计F1提升1.7倍（2.06 vs. 1.21）。消融实验表明，预算感知状态设计和渐进式预算课程对性能提升至关重要，移除预算信息会导致性能显著下降。

### Q5: 有什么可以进一步探索的点？

该论文在预算感知的上下文管理上取得了进展，但仍存在一些局限性和可探索的方向。首先，BACM-RL 依赖于强化学习训练，其策略可能对特定任务或环境过拟合，泛化到未见过的任务类型或更复杂的多模态交互（如图像、代码）时效果尚不明确。其次，当前的压缩决策主要基于文本信息，未充分考虑对话结构、实体关系等语义层面的重要性，可能导致关键信息丢失。此外，方法在极端紧缩预算下的性能虽有优势，但压缩后的信息表示（如摘要）的保真度和后续推理的可靠性仍需进一步评估。

未来研究可朝以下方向深入：一是开发更通用的、可迁移的上下文管理策略，或许能结合元学习或课程学习来适应多样化的任务分布。二是探索更精细的语义感知压缩技术，例如利用知识图谱识别并保留核心事实和推理链。三是将预算管理动态化，不仅考虑当前步，还能预测未来信息需求，进行前瞻性的压缩规划。最后，可研究压缩与模型推理效率的联合优化，在限制上下文长度的同时，也考虑计算开销，实现端到端的效率提升。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的智能体在长程推理任务中面临的上下文长度受限问题，提出了预算感知的上下文管理（BACM）框架。核心问题在于，部署时的内存、延迟和成本等因素限制了智能体可用的上下文预算，随着交互历史增长，需在保留历史信息和遵守预算约束之间做出权衡。

论文将上下文管理形式化为一个具有预算约束的序列决策问题。其核心方法是BACM-RL，一种基于课程学习的端到端强化学习框架，使智能体能在纳入新观察前评估可用预算，并动态决策何时以及以何种程度压缩交互历史，从而学习适应不同预算的压缩策略。

实验表明，在组合式多目标问答和长程网页浏览基准测试中，BACM-RL在不同模型规模和任务复杂度下均优于现有方法。在高复杂度设置中，其性能增益超过基线方法的1.6倍，且在预算缩减时仍保持显著优势，而多数基线方法性能则出现下降。该工作为长程智能体在有限资源下的高效上下文管理提供了系统性的解决方案。
