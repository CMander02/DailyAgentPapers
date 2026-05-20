---
title: "Beyond Mode Collapse: Distribution Matching for Diverse Reasoning"
authors:
  - "Xiaozhe Li"
  - "Yang Li"
  - "Xinyu Fang"
  - "Shengyuan Ding"
  - "Peiji Li"
  - "Yongkang Chen"
  - "Yichuan Ma"
  - "Tianyi Lyu"
  - "Linyang Li"
  - "Dahua Lin"
  - "Qipeng Guo"
  - "Qingwen Liu"
  - "Kai Chen"
date: "2026-05-19"
arxiv_id: "2605.19461"
arxiv_url: "https://arxiv.org/abs/2605.19461"
pdf_url: "https://arxiv.org/pdf/2605.19461v1"
categories:
  - "cs.AI"
tags:
  - "LLM agent reasoning"
  - "reinforcement learning"
  - "policy optimization"
  - "mode collapse"
  - "exploration"
  - "distribution matching"
  - "combinatorial optimization"
  - "mathematical reasoning"
relevance_score: 8.5
---

# Beyond Mode Collapse: Distribution Matching for Diverse Reasoning

## 原始摘要

On-policy reinforcement learning methods like GRPO suffer from mode collapse: they exhibit reduced solution diversity, concentrating probability mass on a single solution once discovered and ceasing exploration of alternative strategies. We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions. We propose DMPO (Distribution-Matching Policy Optimization), which prevents mode collapse through principled approximation of forward KL minimization. DMPO constructs a group level target distribution over sampled trajectories proportional to their rewards, then aligns the policy distribution to this target. This provides mode-covering behavior without requiring sampling from the intractable global target distribution, enabling sustained exploration throughout training. We validate DMPO on NP-hard combinatorial optimization, where exponentially many feasible solutions exist but only a few approach optimality, an ideal testbed for evaluating exploration. DMPO achieves 43.9% Quality Ratio on text-based NP-Bench (vs. GRPO's 40.1%) and 43.1% on vision-based NP-Bench (vs. 38.4%), demonstrating 9% and 12% relative improvements respectively. These gains generalize to mathematical reasoning (+2.0%) and out-of-domain tasks (+2.3%), showing that diversity-preserving training enhances general reasoning capabilities across modalities. Our work establishes distribution matching as a practical, principled approach to preventing mode collapse in on-policy RL, with consistent quality improvements demonstrating sustained exploration across diverse reasoning tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在线强化学习方法（如GRPO）在训练大语言模型时出现的模式崩溃问题。研究背景是，基于可验证奖励的强化学习（RLVR）已成为训练推理模型的主流范式，其中GRPO等在线策略方法通过替代奖励模型，在数学和代码任务上取得了显著成功。然而现有方法存在一个根本性缺陷：一旦发现一个高奖励解决方案，策略会迅速将概率质量集中在该轨迹上，停止探索其他策略，导致模式崩溃。论文指出，这源于这些方法隐含地最小化反向KL散度，其固有的“模式寻求”倾向会强化第一个被发现的高奖励轨迹，而不是维持多样化解决方案的分布。核心问题是：如何在在线策略强化学习中避免模式崩溃，实现持续探索，从而发现更优、更鲁棒的解决方案。论文提出DMPO（分布匹配策略优化），通过有原则地近似前向KL散度最小化来解决此问题。DMPO在组级别构造与奖励成比例的目标分布，并将策略分布对齐到该目标，提供“模式覆盖”行为，无需从全局不可处理的目标分布中采样，从而在整个训练过程中维持探索，有效缓解了模式崩溃。

### Q2: 有哪些相关研究？

1. **模式崩溃相关研究**：文献已建立反向KL散度（\(D_{KL}(q\|p)\)）与模式寻求行为的理论联系，如最大熵RL中的讨论。尽管已知反向KL会导致策略集中于单一解（如标准RL收敛至确定性策略，RLVR方法降低解多样性），但现有解决方案不足：熵正则化（如Haarnoja等人）在置信度过高时失效；内在动机方法（基于预测误差或状态计数）侧重于状态空间覆盖而非输出多样性，且易被无关新颖性干扰；集成方法训练多策略但扩展性差且缺乏单个策略多样性保证。本文通过前向KL最小化\(D_{KL}(p^*\|\pi_\theta)\)实现模式覆盖，区别于反向KL方法。

2. **多样性策略优化**：近期LLM训练中的尝试包括：Token级约束（保留随机性）、pass@k奖励优化（鼓励单次成功）、自适应温度策略及FlowRL（通过GFlowNet学习全局配分函数构建Boltzmann目标分布）。然而FlowRL仍最小化反向KL\(D_{KL}(\pi_\theta\|p^*)\)，因难以从目标分布采样而保持模式寻求行为。本文创新在于**在组级别近似前向KL最小化**——通过奖励加权构造轨迹目标分布，避免全局采样或学习配分函数，无缝集成GRPO的组归一化。

3. **语言模型RLVR方法**：PPO、GRPO、GSPO、GPG等主流方法均通过反向KL最小化进行策略优化，本质易导致模式崩溃。本文提出的DMPO通过简单修改（添加分布匹配项）在保持在线学习方法稳定性与效率的同时，通过前向KL对齐策略分布与奖励诱导的覆盖目标分布，在组合优化（NP-Bench提升9%-12%）、数学推理（+2.0%）及域外任务（+2.3%）上验证了多样性保持对推理能力的提升。

### Q3: 论文如何解决这个问题？

DMPO通过分布匹配来避免模式坍缩。核心方法是：在每组采样轨迹中构造一个与奖励成正比的组条件目标分布，然后让策略的概率分布去匹配这个目标分布。具体而言，对于从当前策略采样的G条轨迹，首先计算每条轨迹基于奖励的玻尔兹曼分布作为目标分布，同时用长度归一化的对数似然来消除轨迹长度偏差，得到策略在当前组上的概率分布。然后通过最小化这两个分布之间的均方误差来实现分布匹配，这比直接使用前向KL散度更稳定，因为梯度系数被限制在±1之间。最终的损失函数结合了原始GRPO的奖励最大化目标和分布匹配损失，用超参数λ平衡探索与利用。创新点包括：1) 将前向KL最小化近似近似到组级别，避免了全局计算分区函数的困难；2) 用均方误差替代KL散度，保证了梯度稳定；3) 理论证明了该方法能保证策略覆盖所有高奖励模式，且在极限情况下实现与奖励成比例采样。

### Q4: 论文做了哪些实验？

论文在三个层面上验证了DMPO防止模式坍缩的效果。首先，在自建的MM-NP-Bench基准（含10个NP-hard组合优化任务）上，与GRPO、GSPO、GPG、ClipCov、FlowRL及GRPOPass@K等基线对比。主要指标为成功率(SR)和质量比(QR)。DMPO在整体QR上达到43.1%，比GRPO的38.4%相对提升12%，同时以61.9%的SR取得最高成功率；其中在分区任务上近乎完美(98.5% SR, 73.1% QR)。此外，在文本版NP-Bench上，DMPO的QR为43.9%，相比GRPO的40.1%提升9%。其次，在数学推理任务上（AIME24/25、AMC、OlympiadBench等6个基准），DMPO平均准确率达44.5%，较GRPO的42.5%提升2.0%，且在AIME24等最难题上增益最大(+2.4%)。最后，在包括LogicVista、MathVista等7个视觉/逻辑推理的域外基准上，仅用MM-NP-Bench训练的DMPO平均得分为37.1%，优于GRPO的36.8%；联合通用数学数据(MM-16K)后达到39.8%，比基线提升5.0%。消融实验表明，DMPO对超参数λ和α较为鲁棒，且纯分布匹配项（无GRPO损失）已能防止模式坍缩，但与GRPO结合效果最佳。

### Q5: 有什么可以进一步探索的点？

论文的最大贡献在于提出DMPO通过近似前向KL散度来解决反向KL导致的模式坍缩，但该方法仍存在几个可探索的方向。首先，DMPO在每轮采样的组内构建目标分布，这种局部归一化可能无法完全逼近全局最优分布，尤其在奖励稀疏或长尾分布的任务中，组内样本的代表性不足会限制探索质量。未来可引入自适应组大小或基于不确定性采样的策略。其次，实验集中于NP-hard组合优化和数学推理，而对开放域生成任务（如代码生成、对话系统）的泛化性尚未验证，需评估多样性维持是否会引入低质量解。此外，DMPO的奖励归一化方式可能对离群值敏感，可探索更鲁棒的排序或对比损失函数。进一步地，结合非策略数据或离线反馈（如专家轨迹）来辅助分布匹配，或能加速收敛并提升样本效率。最后，理论层面可分析前向KL近似误差与策略性能的紧致界限，为自适应温度参数或探索预算提供依据。

### Q6: 总结一下论文的主要内容

基于反向KL的在线强化学习方法（如GRPO）存在模式坍缩问题：一旦发现单一高奖励解，策略便会集中概率质量，停止探索其他策略。本文证明，这是反向KL最小化固有的模式寻求行为所致。为克服此问题，作者提出分布匹配策略优化（DMPO），通过原则性地近似前向KL最小化来预防模式坍缩。DMPO在每组采样轨迹中，构建与奖励成比例的组级目标分布，并将策略分布与之对齐，从而实现模式覆盖，而无需从难以处理的全局目标分布中采样。在NP难组合优化这一理想测试床上，DMPO在文本版NP-Bench上达到43.9%的质量比（GRPO为40.1%），在视觉版上达43.1%（GRPO为38.4%），相对提升9%和12%。该方法在数学推理和域外任务上也分别提升2.0%和2.3%。核心贡献在于：识别并解决了模式坍缩的根源，提出了DMPO这一实用且原则性的解决方案；构建了多模态基准MM-NP-Bench；并通过实验证明，保持多样性的训练能提升通用推理能力。
