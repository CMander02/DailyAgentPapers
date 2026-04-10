---
title: "Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents"
authors:
  - "Khushal Sethi"
date: "2026-04-09"
arxiv_id: "2604.08369"
arxiv_url: "https://arxiv.org/abs/2604.08369"
pdf_url: "https://arxiv.org/pdf/2604.08369v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "推理优化"
  - "自适应计算"
  - "训练免方法"
  - "动作一致性"
  - "多步决策"
  - "资源效率"
  - "控制器设计"
relevance_score: 8.5
---

# Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents

## 原始摘要

Inference-time compute scaling has emerged as a powerful technique for improving the reliability of large language model (LLM) agents, but existing methods apply compute uniformly: every decision step receives the same budget regardless of its difficulty. We introduce TrACE (Trajectorical Adaptive Compute via agrEement), a training-free controller that allocates LLM calls adaptively across agent timesteps by measuring inter-rollout action agreement. At each step, TrACE samples a small set of candidate next actions and measures how consistently the model commits to the same action. High agreement signals an easy decision; the controller commits immediately. Low agreement signals uncertainty; the controller samples additional rollouts up to a configurable cap before committing to the plurality action. No learned components, no external verifier, and no human labels are required. We evaluate TrACE against greedy decoding and fixed-budget self-consistency (SC-4, SC-8) on two benchmarks spanning single-step reasoning (GSM8K, n=50) and multi-step household navigation (MiniHouse, n=30), using a Qwen 2.5 3B Instruct model running on CPU. TrACE-4 matches SC-4 accuracy while using 33% fewer LLM calls on GSM8K and 39% fewer on MiniHouse. TrACE-8 matches SC-8 accuracy with 55% fewer calls on GSM8K and 65% fewer on MiniHouse. We further show that inter-rollout agreement is a reliable signal of step-level success, validating the core hypothesis that the model's own output consistency encodes difficulty information that can be exploited without training. TrACE is the first training-free, per-timestep adaptive-compute controller for LLM agents to be evaluated on multi-step sequential decision tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在序列决策任务中，推理计算资源分配不高效的问题。研究背景是，当前LLM智能体在执行多步任务（如导航、编码）时，通常对每个决策步骤采用统一的计算预算（例如，贪婪解码或固定数量的并行采样）。然而，不同步骤的决策难度差异很大：有些步骤简单明了，有些则复杂微妙。现有方法的不足在于，这种均匀分配计算的方式导致了资源浪费——在简单步骤上过度计算，而在困难步骤上计算不足。虽然通过学习策略来动态分配计算是一种解决方案，但这需要训练数据、奖励信号或过程监督，成本高昂且难以在部署时应用于开放权重的模型。

本文要解决的核心问题是：如何在不依赖训练、外部验证器或人工标注的情况下，实现一种**按时间步自适应分配计算**的机制。为此，论文提出了TrACE方法，其核心思想是利用模型自身产生的“免费”信号——即通过少量独立采样得到的候选下一步行动之间的一致性（agreement）——来评估当前决策步骤的难度。当多个采样结果高度一致时，表明决策容易，控制器立即采纳该行动；当一致性低时，表明模型不确定，控制器则增加采样次数以寻求更可靠的多数行动。这种方法将模型输出的一致性本身作为难度指标，从而实现计算资源的动态、高效分配。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕提升LLM推理可靠性的方法展开，可分为以下几类：

**1. 固定预算的自我一致性方法**：如自我一致性和多数投票，通过采样多条推理路径并取多数答案来提升准确性。但它们在每一步都使用固定的计算预算。本文的TrACE则根据模型自身的不确定性动态分配预算，对简单步骤减少调用次数。

**2. 推理时计算扩展方法**：这类研究主张为更困难的问题分配更多计算资源，例如使用最佳N采样或过程奖励模型。但这些方法通常需要训练一个验证器或奖励模型。TrACE的显著区别在于完全无需训练组件，仅利用原始输出的一致性来实现自适应计算。

**3. 基于树搜索的智能体方法**：如思维树（ToT）和LATS，通过构建显式的动作搜索树进行规划，功能强大但计算开销大，且常需LLM作为价值函数。TrACE是一个轻量级的单步控制器，可与这些方法互补，例如包装树搜索中的节点扩展步骤。

**4. 过程奖励模型与验证器**：这些工作通过训练得到步骤级反馈的奖励模型来提升性能。本文受此启发但截然不同，TrACE利用模型自身的行为一致性作为步骤难度的零训练代理指标，无需任何监督信号。

**5. 自适应早期停止方法**：这类研究基于词元级不确定性或置信度估计，在单个补全流内提前停止生成。TrACE则是在多个完整“展开”之间聚合一致性作为信号。相关研究为“一致性比口头表达的置信度更可靠”提供了理论依据，支持了本文的核心假设。

**6. 无需训练的智能体改进方法**：最接近本文设定的是利用口头反思作为免费信号的工作，但其需要多个完整回合的展开。TrACE在子步骤级别运作，控制对同一决策的采样次数，且无需多回合反馈循环，实现了更精细和高效的计算控制。

### Q3: 论文如何解决这个问题？

论文提出的TrACE方法通过一种无需训练的自适应计算控制器，动态分配每个决策步骤的LLM调用次数，核心思想是利用模型自身多次推理（rollout）之间的动作一致性作为难度信号。其整体框架是一个在线决策循环，在每个时间步t，控制器根据当前上下文（任务目标、历史观察和动作）执行三步流程。

核心方法包含三个主要步骤：首先，进行初始采样，以温度τ从LLM中独立采样k_init个候选动作；其次，计算这些候选动作的一致性α_t，即最高频动作（plurality action）所占比例；最后，基于一致性阈值τ_high决定是否立即提交动作或继续采样。若α_t ≥ τ_high，则直接提交最高频动作；否则，控制器会逐个增加采样，重新计算一致性，直到满足阈值或达到最大采样数k_max，最终提交该步的最高频动作。

架构设计上，TrACE仅依赖LLM本身，无需额外训练组件、外部验证器或人工标注。其关键技术在于将多次推理的动作一致性作为隐式的难度指标：高一致性表明模型对该步决策信心充足，可提前终止；低一致性则触发更多采样以提升决策可靠性。创新点包括：首次在无需训练的前提下，实现了基于时间步的自适应计算分配；利用模型自身输出的一致性作为免费难度信号，避免了LLM置信度校准问题；通过动态调整采样数，在保持与固定预算自一致性方法（如SC-4、SC-8）相同准确率的同时，显著减少LLM调用次数。

默认超参数设置为k_init=2、k_max∈{4,8}、τ_high=0.75、τ=0.7。该方法在单步推理和多步顺序决策任务中均验证了有效性，例如TrACE-8在GSM8K和MiniHouse上分别以减少55%和65%的调用次数匹配了SC-8的准确率，实现了计算效率与性能的帕累托优化。

### Q4: 论文做了哪些实验？

论文在单步推理（GSM8K）和多步家庭导航（MiniHouse）两个基准上进行了实验。实验模型为Qwen 2.5 3B Instruct（量化至Q4_K_M格式），在Apple M系列CPU上运行。对比方法包括：贪心解码（Greedy，每步1次调用）、固定预算的自洽性方法（SC-4和SC-8，每步分别固定调用4次和8次）以及提出的自适应方法TrACE-4和TrACE-8（初始采样k_init=2，最大采样k_max分别为4和8，一致性阈值τ_high=0.75）。

主要结果如下：在GSM8K（n=50）上，TrACE-4准确率（0.82）与SC-4持平，但平均每任务调用次数从4.00降至2.68（减少33%）；TrACE-8准确率（0.84）与SC-8持平，调用次数从8.00降至3.56（减少55%）。在MiniHouse（n=30任务×3种子=90个任务-种子对）上，所有方法准确率均约为0.367，但TrACE-4调用次数从SC-4的24.67降至15.07（减少39%），TrACE-8从SC-8的46.93降至16.27（减少65%）。此外，实验验证了步骤间行动一致性是任务成功的可靠信号：高一致性（α_t ≥ 0.8）的步骤更多出现在成功任务中。消融实验表明，默认阈值τ_high=0.75在节省计算量的同时保持了精度平衡。

### Q5: 有什么可以进一步探索的点？

本文提出的TrACE方法虽然高效，但仍有多个可深入探索的方向。首先，评估规模有限，仅在3B模型和CPU上进行，未来需验证其在更大模型（如70B+）及GPU环境下的效率优势是否保持。其次，当前实验样本量较小，需扩大任务数量和随机种子以增强统计可靠性。再者，基准测试多样性不足，现有方法依赖于离散动作空间的一致性信号，在开放域生成（如代码编写、长文本规划）中可能失效，需研究如何将一致性度量适配于更灵活的输出形式。此外，方法对超参数（如阈值τ_high）敏感，缺乏系统调优，未来可探索自适应阈值设定机制。最后，TrACE未与基于训练的方法（如PRMs）对比，虽突出零训练成本优势，但实际应用中或需结合轻量微调以突破模型能力天花板，例如在复杂导航任务中引入思维链推理。总体而言，未来工作可围绕扩展评估规模、增强泛化性、优化超参数及探索混合方法展开。

### Q6: 总结一下论文的主要内容

该论文提出了TrACE，一种无需训练的自适应计算控制器，用于提升大语言模型（LLM）智能体的可靠性。核心问题是现有推理时计算扩展方法（如自一致性）对所有决策步骤均匀分配计算预算，而未考虑不同步骤的难度差异。TrACE通过测量“跨轮次动作一致性”来动态分配计算：在每个时间步，先采样少量候选动作，若模型输出高度一致则立即提交该动作（视为简单决策）；若一致性低则视为不确定性高，进而采样更多轮次直至达到预设上限，最终选择多数动作。该方法无需学习组件、外部验证器或人工标注。实验在单步推理（GSM8K）和多步家庭导航（MiniHouse）任务上进行，使用Qwen 2.5 3B模型。结果表明，TrACE-4在达到与固定预算自一致性（SC-4）相同准确率的同时，分别减少了33%和39%的LLM调用；TrACE-8在匹配SC-8准确率时减少了55%和65%的调用。论文验证了一致性可作为步骤级成功率的可靠领先指标，证明模型自身输出的一致性编码了难度信息，可直接用于优化计算分配。TrACE是首个在多步序列决策任务上评估的、无需训练的、按时间步自适应计算控制器，为LLM智能体的推理时可靠性方法提供了新方向。
