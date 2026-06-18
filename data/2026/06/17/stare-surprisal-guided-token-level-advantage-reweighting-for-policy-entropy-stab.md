---
title: "STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability"
authors:
  - "Haipeng Luo"
  - "Qingfeng Sun"
  - "Songli Wu"
  - "Can Xu"
  - "Wenfeng Deng"
  - "Han Hu"
  - "Yansong Tang"
date: "2026-06-17"
arxiv_id: "2606.19236"
arxiv_url: "https://arxiv.org/abs/2606.19236"
pdf_url: "https://arxiv.org/pdf/2606.19236v1"
github_url: "https://github.com/hp-luo/STARE"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "RLHF/RL for Agent"
  - "Policy Entropy"
  - "Credit Assignment"
  - "Multi-Turn Tool Use"
relevance_score: 9.5
---

# STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability

## 原始摘要

Reinforcement Learning with Verifiable Rewards algorithms like GRPO have emerged as the dominant post-training paradigm for complex reasoning in LLMs, yet commonly suffer from policy entropy collapse during training. We conduct a first-order gradient analysis of token-level entropy dynamics under GRPO and identify a token-level credit assignment mismatch: the per-token entropy variation decomposes into the product of the trajectory-level advantage and an entropy sensitivity function over the next-token distribution, yielding an advantage-surprisal four-quadrant structure and a near-criticality property. Motivated by it, we propose STARE (Surprisal-guided Token-level Advantage Reweighting for policy Entropy stability), which identifies entropy-critical token subsets via batch-internal surprisal quantiles, selectively reweights their effective advantages, and incorporates a target-entropy closed-loop gate for stable entropy regulation. Across model scales from 1.5B to 32B and three task families (Short CoT, Long CoT, and Multi-Turn Tool Use), STARE sustains stable RL training over thousands of steps while maintaining policy entropy within the target band. On AIME24 and AIME25, STARE outperforms DAPO and other competitive baselines by 4%-8% in average accuracy, with reflection tokens and response length growing in tandem, indicating sustained exploration-exploitation balance that further unlocks RL training potential.Code is available at https://github.com/hp-luo/STARE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在基于可验证奖励的强化学习（如GRPO算法）后训练中普遍存在的**策略熵坍缩**问题。研究背景是，GRPO等RLVR算法虽能有效提升模型在数学推理、代码生成等复杂任务中的能力，但随着训练步数增加，模型策略熵会快速下降，导致输出多样性消失，策略过早收敛，同组内rollout趋同，进而削弱相对优势估计，最终限制可训练步数，成为长周期后训练的关键瓶颈。现有缓解方法主要从三个方向入手，包括调整重要性采样裁剪阈值、不对成轨迹级加权以及熵感知优势重塑，但这些方法要么作用不对称且不可控，要么仅提供粗粒度控制，要么容易引发振荡且超参数敏感，均缺乏对熵坍缩机制的原理性解释。基于此，本文提出了STARE方法。该方法通过对GRPO下token级熵动态的一阶梯度分析，揭示了token级信用分配错位：轨迹级优势被所有token共享，但每个token的熵贡献却由该优势与局部熵敏感度函数的乘积决定。STARE通过批次内surprisal分位数识别熵关键token子集，选择性地调整其有效优势，并引入目标熵闭环门控机制，在实现稳定熵调控的同时，使训练能够持续数千步，显著提升模型在AIME24/25等基准上的性能。

### Q2: 有哪些相关研究？

本文的研究背景是基于GRPO等可验证奖励强化学习算法在大型语言模型推理微调中的熵崩溃问题。相关工作可分为三类：

1. **方法类**：包括GRPO、PPO、RLOO等直接优化策略的算法，以及DAPO、Dr. GRPO等通过裁剪或动态采样缓解熵崩溃的变体。本文与它们的区别在于：通过梯度分析首次明确了熵崩溃的根源是**轨迹级优势与逐token熵灵敏度的四象限耦合**，并针对性设计了基于惊奇度的令牌级优势加权（STARE），而非简单剪枝或全局正则化。

2. **稳定性调节类**：如KL散度正则化、熵目标约束等方法。本文的独特贡献是提出**目标熵闭环门控**，能根据批次内惊奇度分位数动态调整有效优势，避免了固定熵惩罚带来的探索-利用失衡。

3. **评测与应用类**：短链推理（AIME24/25）、长链推理（MATH500）和多轮工具使用任务。本文在1.5B到32B规模模型上实验，相比DAPO在AIME24/25上提升4%-8%准确率，且反射令牌数与响应长度同步增长，验证了STARE能维持稳定的探索-利用平衡，而现有方法在高步数训练中常出现熵崩塌或奖励衰减。

### Q3: 论文如何解决这个问题？

STARE的核心创新在于通过逐token的惊喜度（surprisal）引导优势重加权来解决GRPO训练中的策略熵坍缩问题。整体框架基于GRPO的裁剪替代目标函数，通过理论推导发现GRPO中轨迹级的共享优势导致逐token信用分配不匹配：高频低惊喜度token主导梯度聚合，而具有关键熵效应的高惊喜度token被低估。STARE引入了一个惊喜度驱动的信用再平衡机制，包含三个关键模块：首先是熵关键token子集识别模块，在正优势和负优势token集合内分别按惊喜度降序排列，选取前P%（默认10%）作为熵关键token集，无需逐位置计算阈值。其次是选择性优势重加权模块，设计了两种变体：变体I（O1）仅放大正优势高惊喜度token的权重（W>1），增强其熵增加信号；变体II（C2）额外衰减负优势高惊喜度token的权重（0<M<1），同时缓解熵减少压力。所有重加权权重均为正数，保持原始梯度方向不变。最后是目标熵闭环门控模块，通过批次平均熵与目标熵的比较，当熵低于目标时激活重加权，否则恢复为标准GRPO，避免过度调节导致熵发散。关键创新点包括：基于理论分析识别出优势-惊喜度四象限结构及近临界特性；利用批次内惊喜度分位数作为稳定代理；通过固定权重利用近临界特性降低超参数敏感性；支持自适应权重更新以适应训练阶段变化。实验表明STARE在1.5B到32B模型规模上均能稳定维持目标熵带内训练数千步。

### Q4: 论文做了哪些实验？

论文在三种场景下进行实验：Short CoT（使用Qwen2.5-Math-7B-Base、Qwen2.5-14B-Instruct和Qwen2.5-32B-Base，最大解码长度4k-8k）、Long CoT（使用DeepSeek-R1-Distill-Qwen-1.5B和Qwen3-8B-Base，解码长度16k）以及Tool-Use场景（Qwen2.5-7B-Base先经Retool 2K数据冷启动SFT，再以8k长度进行RL训练）。训练采用学习率1e-6、批大小64、每样本8次rollout，单梯度步on-policy更新，解码Top-p=1.0、温度T=1.0。STARE超参数设为W=1.1、M=0.9、H_tgt=0.3、P%=10%，使用批量门控和固定权重。训练语料为来自DeepScaler、Skywork-o1、Polaris和DAPO等开源RL数据集的10万去重样本。对比方法包括GRPO、DAPO、STEER、EntroReg、80/20 Rule、EntroAdv、KL-Cov、EAPO、GRPO-ds等多种基线。在AIME24、AIME25、AMC23、MATH-500、Minerva Math和OlympiadBench六个数学基准上评估，AIME24/25和AMC23评估32次，其余4次，报告平均准确率。主要结果：在Short CoT 7B尺度，STARE平均54.4%，比STEER（49.1%）高5.3%，AIME24达44.2%（比DAPO高约10%）；14B尺度STARE-O1达52.0%，超GRPO-ds 5.9%；32B尺度达60.7%，超GRPO-ds 4.6%。Long CoT 1.5B尺度STARE-C2平均66.3%，超JustRL（65.6%）0.7%；Qwen3-8B尺度62.2%，超GRPO-ds 3.7%。Tool-Use场景STARE-C2平均60.4%，超SimpleTIR约5.5%。

### Q5: 有什么可以进一步探索的点？

论文的核心创新在于通过优势-惊讶度四象限分析识别熵关键令牌并动态调整优势权重，但仍存在可探索方向。首先，当前方法依赖批次内部分位数阈值选择熵关键令牌，阈值对训练稳定性的敏感性未充分分析，可探索自适应阈值机制（如基于熵梯度信号动态调整分位数）。其次，闭环门控仅基于目标熵区间进行线性调节，未来可引入更复杂的非线性控制律（如PID控制器）以加速收敛。此外，该方法在长链推理任务中虽延长了响应长度，但未明确区分有效探索与冗余令牌生成；可引入令牌级奖励塑形（如基于语义相似度的稀疏化奖励）抑制无效扩展。最后，当前实验仅在数学推理和工具调用场景验证，需扩展至开放域对话或代码生成等目标更模糊的任务，检验策略稳定性。从理论角度，论文的梯度分析隐式假设优势估计无偏，未来可探索结合GAE或Retrace等优势估计方法进一步提升训练鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为STARE的方法，用于解决强化学习后训练中常见的策略熵崩溃问题。在GRPO等可验证奖励强化学习算法中，作者通过一阶梯度分析揭示了token级熵动态的关键机制：每个token的熵变化可分解为轨迹级优势函数与下一token分布熵敏感度函数的乘积，构成优势-惊奇四象限结构和近临界性质。基于此发现，STARE通过批次内惊奇分位数识别熵关键token子集，选择性地重新加权其有效优势值，并引入目标熵闭环门控实现稳定熵调控。在1.5B到32B参数规模、涵盖短链推理、长链推理和多轮工具使用的三个任务族上，STARE在数千步训练中保持策略熵稳定在目标区间内。在AIME24和AIME25基准上，STARE相比DAPO等基线平均准确率提升4%-8%，同时反映标记和响应长度协同增长，表明其有效维持了探索-利用平衡，进一步释放了强化学习训练潜力。这项工作的核心贡献在于从理论层面揭示了策略熵崩溃的根本原因，并提供了实用的稳定训练方案。
