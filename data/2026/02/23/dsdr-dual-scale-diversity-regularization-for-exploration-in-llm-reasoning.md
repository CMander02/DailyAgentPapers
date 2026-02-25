---
title: "DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning"
authors:
  - "Zhongwei Wan"
  - "Yun Shen"
  - "Zhihao Dou"
  - "Donghao Zhou"
  - "Yu Zhang"
  - "Xin Wang"
  - "Hui Shen"
  - "Jing Xiong"
  - "Chaofan Tao"
  - "Zixuan Zhong"
  - "Peizhou Huang"
  - "Mi Zhang"
date: "2026-02-23"
arxiv_id: "2602.19895"
arxiv_url: "https://arxiv.org/abs/2602.19895"
pdf_url: "https://arxiv.org/pdf/2602.19895v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "强化学习"
  - "LLM推理"
  - "探索策略"
  - "多样性正则化"
  - "策略优化"
  - "Agentic强化学习"
relevance_score: 7.5
---

# DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning

## 原始摘要

Reinforcement learning with verifiers (RLVR) is a central paradigm for improving large language model (LLM) reasoning, yet existing methods often suffer from limited exploration. Policies tend to collapse onto a few reasoning patterns and prematurely stop deep exploration, while conventional entropy regularization introduces only local stochasticity and fails to induce meaningful path-level diversity, leading to weak and unstable learning signals in group-based policy optimization. We propose DSDR, a Dual-Scale Diversity Regularization reinforcement learning framework that decomposes diversity in LLM reasoning into global and coupling components. Globally, DSDR promotes diversity among correct reasoning trajectories to explore distinct solution modes. Locally, it applies a length-invariant, token-level entropy regularization restricted to correct trajectories, preventing entropy collapse within each mode while preserving correctness. The two scales are coupled through a global-to-local allocation mechanism that emphasizes local regularization for more distinctive correct trajectories. We provide theoretical support showing that DSDR preserves optimal correctness under bounded regularization, sustains informative learning signals in group-based optimization, and yields a principled global-to-local coupling rule. Experiments on multiple reasoning benchmarks demonstrate consistent improvements in accuracy and pass@k, highlighting the importance of dual-scale diversity for deep exploration in RLVR. Code is available at https://github.com/SUSTechBruce/DSDR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于验证器的强化学习（RLVR）在提升大语言模型推理能力时面临的探索不足问题。研究背景是，RLVR通过利用验证反馈（如答案正确性）而非逐词模仿来优化模型，已在数学推理、代码生成等任务上取得显著进展，并常结合基于组的策略优化方法（如GRPO）以提升训练稳定性。然而，现有方法存在明显不足：在训练过程中，策略容易收敛到少数同质的推理模式上，导致解决方案多样性崩溃；尽管存在多种有效解题路径，模型却过早停止深度探索。传统的熵正则化等方法主要引入词元级别的局部随机性，无法促进路径级别的多样性，使得基于组的优化中学习信号弱化且不稳定。

本文要解决的核心问题是：如何在确保正确性的前提下，协调不同尺度上的多样性，以实现更深度的探索。具体而言，作者指出探索需要在两个互补的尺度上进行：在全局层面，需要发现并维持多种不同的推理模式（即不同的解题路径）；在局部层面，需要防止每个模式内部的熵崩溃，保持正确解轨迹的鲁棒性和表达性。现有方法通常是单尺度的或跨尺度耦合较弱，未能有效协调这两者，导致探索与正确性之间的张力未能解决。

为此，论文提出了DSDR（双尺度多样性正则化）框架，通过将多样性分解为全局和耦合组件来系统性地应对上述问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕**强化学习与验证器（RLVR）范式下的探索问题**以及**大语言模型推理中的多样性与熵控制方法**展开。

在**RLVR与探索增强**方面，已有工作通过多种策略缓解探索不足：一是增加策略随机性，如熵正则化或温度调整；二是修改优化目标，如松弛裁剪或基于pass@k的奖励；三是干预rollout动态以鼓励模式切换（如“采样后遗忘”机制）。这些方法虽从不同角度提升探索，但依赖非结构化的随机性、目标层松弛或rollout干预，未显式协调不同推理尺度间的探索。本文则通过**在策略优化中结构化地构建全局到局部的多样性**，实现深度探索而无需修改rollout过程。

在**多样性与熵控制**方面，现有研究可分为两类：一是**局部（token级）方法**，如通过熵奖励、裁剪或KL约束选择性鼓励随机动作，虽能缓解过早崩溃，但仅作用于局部动作层面，无法促进完整推理轨迹的多样性；二是**全局方法**，如利用pass@k作为训练信号鼓励多候选解，或训练分区分类器以度量并放大优势函数中的多样性。然而，这些方法大多将全局与局部多样性信号独立处理，未明确优化中多尺度多样性应如何交互。本文提出的DSDR则**显式分解多样性为全局与局部成分**，并通过全局到局部的分配机制耦合二者，将局部熵正则化自适应集中于更具区分度的正确轨迹上。

### Q3: 论文如何解决这个问题？

论文通过提出DSDR（双尺度多样性正则化）强化学习框架来解决RLVR中探索不足的问题。其核心方法是将LLM推理中的多样性分解为全局和局部两个尺度，并设计耦合机制进行协同优化。

整体框架以GRPO（组相对策略优化）为优化主干，对每个输入提示采样一组轨迹并计算可验证奖励。DSDR在此基础上引入两个正则化组件：**全局多样性正则化**和**局部熵正则化**。全局组件通过计算轨迹间的语义差异和公式独特性，为正确的轨迹分配多样性奖励，防止策略过早收敛到少数推理模式。局部组件则在正确的轨迹上施加长度不变的条件熵正则化，避免每个正确模式内部的token级崩溃。

主要模块包括：1）**全局多样性评分器**，结合嵌入语义相似性和公式级独特性计算有界多样性分数；2）**奖励塑造模块**，仅对正确轨迹添加裁剪后的多样性奖励，保持学习信号稳定；3）**全局到局部耦合机制**，通过基于多样性的softmax权重分配，将局部正则化集中在最具独特性的正确轨迹上；4）**局部熵目标**，使用时均条件熵和重要性采样，避免长度偏差并专注优化正确轨迹。

关键技术包括：使用预训练文本编码器计算语义差异；设计公式提取和独特性检测方法；通过裁剪和加权确保多样性信号不压倒正确性；理论推导出耦合权重与多样性倾斜策略梯度的一致性。

创新点在于：首次显式分解并耦合双尺度多样性；提出仅针对正确轨迹的局部熵正则化；设计理论驱动的全局-局部耦合规则；在多个推理基准上实现准确性和pass@k的稳定提升。

### Q4: 论文做了哪些实验？

实验在多个数学推理基准上评估DSDR。实验设置方面，使用过滤后的DAPO-Math-17K数据集进行训练，采用Qwen2.5-Math-1.5B、Qwen3-1.7B和Qwen3-4B作为基础模型。训练批次大小为256，每个提示进行8次rollout，学习率为1e-6，响应最大长度根据模型设为4K或8K tokens。评估基准包括AIME2024、AIME2025、MATH500、Minerva Math和Olympiad-level问题，报告Pass@1和Avg@16准确率，并额外评估Pass@k（k从2到64）。对比方法包括基础模型（Backbone）、GRPO和DAPO。

主要结果显示，DSDR在所有基准和模型规模上均一致优于基线。例如，在Qwen3-1.7B上，DSDR平均性能达到36.8/36.8（Pass@1/Avg@16），显著高于GRPO的28.4/29.7和DAPO的29.6/32.1。在更具挑战性的AIME24上，DSDR的Pass@1达到36.7，而DAPO为20.0。Pass@k曲线表明，随着k增大，DSDR的优势持续扩大，尤其在AIME和Olympiad上。消融实验显示，移除全局多样性（GD）或全局-局部耦合（GC）均导致性能下降，验证了双尺度设计的重要性。此外，训练动态分析表明DSDR能维持更高的策略熵和更低的语义相似性，促进了多样且正确的推理轨迹探索。

### Q5: 有什么可以进一步探索的点？

本文提出的DSDR框架在提升LLM推理探索多样性方面取得了进展，但仍存在一些局限和可拓展方向。首先，DSDR主要关注数学和逻辑推理任务，其在不同领域（如创意生成、复杂对话）的泛化能力有待验证；未来可研究如何将双尺度正则化适配到开放域任务中。其次，当前方法依赖“正确轨迹”的预定义，在真实场景中正确性可能难以判定，可探索结合不确定性估计的动态正则化策略。此外，全局与局部多样性的耦合机制仍较启发式，未来可引入元学习或博弈论框架来自适应调整权重。从技术角度看，可进一步探索多智能体协作下的群体多样性激励，或将DSDR与课程学习结合，逐步增加探索复杂度以提升训练效率。最后，理论分析目前基于简化假设，未来需在更一般的策略优化框架下提供更严格的理论保证。

### Q6: 总结一下论文的主要内容

本文提出DSDR（双尺度多样性正则化）框架，旨在解决基于验证器的强化学习（RLVR）中大型语言模型推理探索不足的问题。现有方法常因策略坍缩到少数推理模式而限制深度探索，传统熵正则化仅引入局部随机性，无法在路径层面促进多样性，导致基于组的策略优化信号弱且不稳定。

DSDR的核心贡献是将LLM推理多样性分解为全局和局部耦合组件。全局层面，它鼓励正确推理轨迹之间的多样性，以探索不同的解题模式；局部层面，在正确轨迹上应用长度不变的词元级熵正则化，防止各模式内部熵坍缩并保持正确性。两尺度通过全局到局部的分配机制耦合，对更具区分性的正确轨迹加强局部正则化。

理论分析表明，DSDR能在有界正则化下保持最优正确性，维持组优化中的有效学习信号，并提供理论依据的耦合规则。在多个推理基准上的实验显示，DSDR在准确率和pass@k指标上均取得稳定提升，验证了双尺度多样性对RLVR深度探索的重要性。
