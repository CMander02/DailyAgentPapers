---
title: "Provable and Practical In-Context Policy Optimization for Self-Improvement"
authors:
  - "Tianrun Yu"
  - "Yuxiao Yang"
  - "Zhaoyang Wang"
  - "Kaixiang Zhao"
  - "Porter Jenkins"
date: "2026-03-02"
arxiv_id: "2603.01335"
arxiv_url: "https://arxiv.org/abs/2603.01335"
pdf_url: "https://arxiv.org/pdf/2603.01335v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Algorithm"
attributes:
  base_model: "N/A"
  key_technique: "In-Context Policy Optimization (ICPO), Minimum-Entropy ICPO (ME-ICPO)"
  primary_benchmark: "N/A"
---

# Provable and Practical In-Context Policy Optimization for Self-Improvement

## 原始摘要

We study test-time scaling, where a model improves its answer through multi-round self-reflection at inference. We introduce In-Context Policy Optimization (ICPO), in which an agent optimizes its response in context using self-assessed or externally observed rewards without modifying its parameters. To explain this ICPO process, we theoretically show that with sufficient pretraining under a novel Fisher-weighted logit-matching objective, a single-layer linear self-attention model can provably imitate policy-optimization algorithm for linear bandits. Building on this theory, we propose Minimum-Entropy ICPO (ME-ICPO), a practical algorithm that iteratively uses its response and self-assessed reward to refine its response in-context at inference time. By selecting the responses and their rewards with minimum entropy, ME-ICPO ensures the robustness of the self-assessed rewards via majority voting. Across standard mathematical reasoning tasks, ME-ICPO attains competitive, top-tier performance while keeping inference costs affordable compared with other inference-time algorithms. Overall, ICPO provides a principled understanding of self-reflection in LLMs and yields practical benefits for test-time scaling for mathematical reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在推理时通过多轮自我反思进行自我改进（即“测试时扩展”）的机制缺乏理论理解，以及如何有效利用上下文信息进行策略优化的问题。

研究背景是，随着LLMs在数学推理等领域能力的提升，测试时扩展（即模型在推理时不更新参数，仅通过多轮自我反思来改进答案）已成为一种重要的能力。现有方法（如思维链、后验采样等）虽然经验上有效，但其内在机制尚不明确。现有理论研究主要关注LLMs在上下文学习中对监督学习（如线性回归）或强化学习（如时序差分学习）算法的模仿能力，但普遍假设模型能基于输入预测输出。然而，对于LLMs如何通过上下文信息优化自身策略以最大化奖励（即进行策略优化）的过程，理论理解几乎空白。同时，当前的理论研究与测试时扩展的实际应用之间存在巨大差距。

因此，本文的核心问题是：能否从上下文学习的角度理解LLMs的自我反思过程，并由此启发一种用于推理任务的、可证明且实用的测试时扩展方法？具体而言，论文试图填补两个主要不足：一是现有工作未能解释LLMs在预训练后为何能内在执行策略优化；二是缺乏如何迭代利用上下文反馈（如自我评估的奖励）进行稳健策略改进的实用算法。

为此，论文提出了“上下文策略优化”（ICPO）框架，将多轮自我反思形式化为一个上下文策略优化过程，并从理论上证明，在满足一定条件的预训练后，简单的线性自注意力模型可以可证明地模仿线性赌博机问题的策略优化算法。基于此，论文进一步提出了最小熵ICPO（ME-ICPO）这一实用算法，通过熵正则化和多数投票来确保自我评估奖励的稳健性，从而在数学推理任务中实现高效且高性能的测试时扩展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：测试时扩展、自我反思与评估，以及上下文学习与强化学习。

在**测试时扩展**方面，相关工作包括早期的少样本思维链（Chain-of-Thought），以及后续的蒙特卡洛树搜索、Best-of-N、思维树（Tree of Thoughts）等后训练搜索算法。TTRL 则进一步基于测试时的自我评估进行梯度更新以改进模型响应。本文提出的 ICPO 同样属于测试时扩展范畴，但区别于这些方法：它不修改模型参数，而是通过上下文内的策略优化迭代改进响应，从而在保持推理成本可控的同时实现性能提升。

在**自我反思与自我评估**方面，LLM-as-a-Judge 和多数判断（Majority-Judgment）等方法利用自我奖励提供低成本但带噪声的偏好信号；过程监督（如 PRMs、逐步验证器）则将监督从结果转向中间步骤。这些工作揭示了自我评估存在的提示/位置敏感性和风格偏差等问题。本文的 ME-ICPO 算法通过最小熵选择和多数投票来增强自我评估奖励的鲁棒性，与这些校准思路一脉相承，但提供了更理论化的解释。

在**上下文学习与强化学习**方面，理论研究表明，经过训练的线性自注意力可以在上下文中实现岭回归的梯度下降，或模仿 bandit/RL 风格的更新。本文与这些理论工作紧密相关，并在此基础上推进：它首次从理论角度证明，在满足特定预训练目标（Fisher 加权 logit 匹配）下，单层线性自注意力模型可证明地模仿线性 bandit 的策略优化算法，从而为上下文内的策略优化提供了原理性解释，并将理论分析延伸至策略优化这一较少被覆盖的领域。

### Q3: 论文如何解决这个问题？

论文通过提出“上下文策略优化”（ICPO）理论框架及其实践算法“最小熵ICPO”（ME-ICPO），来解决大模型在推理时通过多轮自我反思提升答案质量的问题。核心思路是不修改模型参数，而是在推理时利用上下文中的历史响应和自我评估奖励，以在线策略优化的方式迭代优化输出。

整体框架基于一个理论分析启发的线性自注意力（LSA）模型。该模型通过前向传递模拟策略优化过程：在每一步 \(t\)，模型根据当前上下文嵌入 \(\mathbf{E}^{(t-1)}\) 生成对数几率 \(\hat{\mathbf{s}}_t\)，进而得到策略 \(\mathbf{p}_t\)（混合了softmax和探索因子 \(\gamma\)），然后依此采样动作（即生成响应）并接收奖励 \(r_t\)。奖励可以是自我评估或外部观察得到的。随后，模型将动作的嵌入表示 \(\mathbf{x}_t\) 和奖励 \(r_t\) 作为新令牌插入上下文序列，更新嵌入 \(\mathbf{E}^{(t)}\)，进入下一轮。这种设计使得模型能够根据历史交互数据动态调整策略。

训练阶段采用了一种新颖的Fisher加权对数几率匹配目标进行监督预训练。具体地，损失函数 \(\mathcal{L}(\theta)\) 要求模型输出的对数几率 \(\hat{\mathbf{s}}_{t+1}\) 与一个专家策略优化算法（如FTRL）产生的对数几率 \(\mathbf{s}_{t+1}^{\text{ftrl}}\) 在投影后（移除不影响策略的常数偏置）的差异最小化，且该差异以Fisher信息矩阵 \(\Gamma\) 加权。论文理论证明了该损失与常用的KL散度损失相互约束，表明即使简单的线性自注意力层，通过足够的此类预训练，也能从结构上学会模仿策略优化行为，并具备对单步奖励扰动的稳定性。

基于此理论，论文提出了实用的ME-ICPO算法，主要包含三个关键模块以解决直接应用ICPO时的两大挑战（上下文过长和自评估奖励不可靠）：
1.  **响应生成与自我评估**：在每一轮，模型基于当前上下文历史 \(\mathcal{H}_{t-1}\) 采样生成 \(k\) 个候选响应及其最终答案。通过多数投票（Majority Voting）在这些答案中确定一个共识答案 \(\hat{a}_t\)，并将每个候选响应是否匹配该共识作为其自我评估奖励 \(r_j^{(t)}\)。这通过集体决策提高了奖励的鲁棒性。
2.  **思维链摘要**：为了压缩上下文长度，算法使用一个摘要器（Summarizer）将每个候选响应的详细推理过程提炼为简洁的思维链描述 \(x_j^{(t)}\)，仅保留关键解题思路，忽略冗长数值计算。
3.  **最小熵响应选择**：这是算法的核心创新点。不同于直接选择奖励最高的响应，算法为每个候选响应构建一个临时的扩展上下文 \(\tilde{\mathcal{H}}_j^{(t)}\)（包含该响应及其奖励），然后评估模型基于此临时上下文生成下一个响应的概率分布的熵 \(H(\tilde{\mathcal{H}}_j^{(t)})\)。选择使该未来响应熵最小的候选 \(j^*\) 及其对应的摘要和奖励正式加入历史上下文 \(\mathcal{H}_t\)。这种“悲观”选择机制倾向于避免那些可能导致后续输出随机化（高熵）的、可能被污染的响应，鼓励选择能降低未来不确定性的、信息量大的响应，从而引导更稳健的自我改进。

ME-ICPO的创新点在于：1) 首次为LLMs的上下文学习与策略优化之间的关联提供了严格的理论解释（基于LSA模型和Fisher加权损失）；2) 提出了无需梯度更新、纯粹在推理时进行的上下文策略优化框架；3) 设计了结合多数投票奖励和最小熵选择机制的实用算法，有效应对了自评估噪声和上下文膨胀问题，在数学推理任务上取得了有竞争力的性能，同时保持了可接受的推理成本。

### Q4: 论文做了哪些实验？

论文实验主要包括理论验证和实际算法性能评估两部分。实验设置上，首先通过两个受控实验验证理论结果：在单一线性自注意力（LSA）模型上，分别测试了教师-学生策略匹配误差（Policy Matching）和一次性奖励冲击下混合策略的稳定性（Reward-Shock Stability），并与理论分析边界进行对比。其次，评估所提出的最小熵ICPO（ME-ICPO）算法在标准数学推理任务上的性能，对比了其他推理时算法（如Self-Refine、Self-Correction等），并考虑了推理成本。

数据集/基准测试方面，主要使用了数学推理任务，具体包括GSM8K、MATH等标准数据集。对比方法涉及多种推理时优化算法，如Self-Refine、Self-Correction以及基于搜索的方法（如ToT、CoT-SC）。

主要结果上，理论验证实验显示，策略匹配误差随训练步骤增加而减小，且混合策略在奖励冲击下保持稳定，符合理论边界。ME-ICPO在实际任务中取得了竞争性的顶级性能，例如在GSM8K上达到高准确率（具体指标如准确率提升百分比需参考原文图表），同时保持可负担的推理成本（如减少迭代轮数或降低计算开销）。关键数据指标包括策略匹配误差值、稳定性边界、任务准确率（如GSM8K上的准确率）和推理效率（如平均迭代次数或时间成本）。总体而言，实验证实了ICPO的理论可行性，并展示了ME-ICPO在数学推理中的实用优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的ICPO方法虽然在理论上有较好保证，并在数学推理任务中表现出色，但仍存在若干局限和可拓展方向。首先，其理论分析基于单层线性自注意力模型和线性赌博机环境，这与实际LLMs的复杂结构和任务分布存在差距，未来可探索更贴近Transformer架构的理论解释。其次，ME-ICPO依赖自评估奖励的多数投票来保证鲁棒性，但在开放领域或主观性较强的任务中，自评估机制可能不可靠，需结合外部反馈或更精细的校准方法。此外，当前方法主要针对数学推理等封闭式问题，未来可研究其在创意写作、代码生成等开放式任务中的泛化能力。从实践角度看，ICPO的迭代优化可能增加推理延迟，可探索动态终止机制或蒸馏到轻量级模型的方法。最后，将ICPO与参数微调、强化学习等技术结合，形成混合优化框架，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了“上下文内策略优化”（ICPO）方法，旨在实现模型在推理时通过多轮自我反思来提升答案质量，而无需更新模型参数。核心问题是探索如何让智能体在上下文环境中，利用自我评估或外部观察到的奖励来优化其响应。论文首先从理论上证明，通过一种新颖的Fisher加权对数匹配目标进行充分预训练后，单层线性自注意力模型能够可证明地模仿线性多臂老虎机问题的策略优化算法。基于这一理论，作者提出了最小熵ICPO（ME-ICPO）这一实用算法，该算法在推理时迭代地利用自身响应和自我评估的奖励来优化上下文中的回答。通过选择具有最小熵的响应及其奖励，ME-ICPO借助多数投票机制确保了自我评估奖励的鲁棒性。在标准数学推理任务上的实验表明，ME-ICPO在保持可承受推理成本的同时，取得了具有竞争力的顶尖性能。总体而言，ICPO为大语言模型中的自我反思机制提供了理论依据，并为数学推理任务的测试时扩展带来了实际效益。
