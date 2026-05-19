---
title: "Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification"
authors:
  - "Shaddin Dughmi"
  - "Mahdi Haghifam"
  - "Yusuf Hakan Kalayci"
date: "2026-05-17"
arxiv_id: "2605.17609"
arxiv_url: "https://arxiv.org/abs/2605.17609"
pdf_url: "https://arxiv.org/pdf/2605.17609v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "推理时搜索"
  - "验证器"
  - "成本敏感搜索"
  - "自适应算法"
  - "数学推理"
  - "代码生成"
relevance_score: 8.5
---

# Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification

## 原始摘要

Many inference-time language-model pipelines combine a cheap reward signal with an expensive verifier, such as exact answer checking in mathematical reasoning or hidden-test execution in code generation.
  We formalize this setting using a learning-theoretic lens as generative active search: a cost-sensitive first-positive search problem in which a policy adaptively samples candidates from an unknown distribution, observes cheap scores, and pays for verifier labels until it finds a positive example. For a fixed prompt, the generator and reward model induce two unknown objects: a distribution over reward scores and a score-conditioned success function. When these quantities are known, we characterize the distribution-aware optimal policy using a dynamic programming approach. In the realistic and practical setting where both the score distribution and success function are unknown, we propose ADAP, a shellwise adaptive generate-rank-verify algorithm that progressively increases the number of sampled responses and top-ranked verifications. Under the monotonicity assumption that higher reward scores are no less likely to pass verification, we show that ADAP achieves expected cost within a constant factor of the distribution-aware optimum. We complement this result with learning-theoretic lower bounds, based on a centered star number, showing that structural assumptions on the score--label relationship are necessary. Experiments on mathematical reasoning and competitive programming validate the predicted advantage over both fixed non-adaptive policies and difficulty-adaptive baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的推理流水线中，昂贵的验证器与廉价但嘈杂的奖励模型之间的计算资源分配问题。现有方法通常采用固定的生成-排名-验证策略（如生成N_rew个候选、排序后验证前N_ver个），但这一策略高度依赖提示词的难度：简单问题会过度花费，而困难问题则可能搜索不足。尽管已有工作尝试通过历史数据预测难度来动态分配预算，但这种方法在分布漂移（如提示词分布或奖励-验证关系变化）时表现不可靠。本文的核心问题是：能否设计一种在线策略，仅利用当前提示词上观察到的奖励分数和验证结果，自适应地决定何时继续生成候选、何时进行验证，从而在无需预知分数分布和奖励-验证关系的情况下，实现接近最优（即已知这些分布的最优策略）的期望成本？作者将这一问题形式化为一个成本敏感的“生成性主动搜索”问题，并提出了一个理论框架来刻画其最优策略和自适应算法的理论保证。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：

1. **生成-排序-验证基础方法**：本文的抽象模型源于数学推理中的结果验证器、代码生成中的执行过滤（如AlphaCode、CodeT、LEVER）等工作。与这些聚焦于验证器设计或工程化流水线的研究不同，本文将其形式化为代价敏感的顺序决策问题，并首次从学习理论视角分析自适应策略的代价最优性。

2. **自适应测试时计算分配**：现有工作或通过预测难度分配预算（如基于奖励曲线的跨问题分配），或在单输入内自适应停止生成（如根据答案一致性）。本文的核心区别在于同时决策“生成更多候选”与“验证现有候选”之间的代价权衡，而非仅优化生成数量或奖励信号。

3. **选择性验证与主动搜索**：与“弱-强验证”分层策略或可行性门控验证不同，本文的验证器作为最终认证机制。在主动搜索领域，经典贝叶斯主动搜索依赖固定池和已知后验，而本文面临在线动态生成的候选池且分布未知，因此引入了生成-验证代价权衡这一新挑战，并证明了无假设时自适应策略存在本质代价下界。

### Q3: 论文如何解决这个问题？

ADAP通过自适应搜索生成、排序和验证的循环，在缺乏分布先验知识的情况下近似最优策略。其核心设计是基于成本尺度的“壳”（shell）结构，将搜索空间按预期成本划分为指数级增长的区间，并逐步扩大采样与验证规模。整体框架包含三个关键组件：**生成器**（Generator）根据当前壳的采样规模m_s生成候选响应；**奖励模型**（Reward Model）为每个候选打分并维护一个按得分降序排列的未验证池（Pool）；**验证器**（Verifier）对池中排名前k_s的候选进行昂贵验证，若发现正确解则立即终止。技术实现上，算法在每一步s首先计算壳集合S_s，该集合包含所有满足成本处于[2^s*c_min, 2^(s+1)*c_min)区间的参数对(a,b)，其中a对应验证规模指数、b对应采样规模指数。然后选取当前壳内最大的采样指数b_s^*和验证指数j_s^*，据此确定m_s=2^(b_s^*+1)和k_s=6*2^(j_s^*)。新生成的候选加入池后按奖励得分重排序，验证器仅检查前k_s个高分候选。该方法的核心创新在于：1）无需知道奖励分布D和成功函数h*，仅依赖单调性假设（高奖励更可能通过验证）；2）通过成本尺度逐步翻倍的壳结构，使总预期成本始终在最优分布感知策略的常数因子（400倍）之内；3）基于池的设计保留历史高分候选，避免重复采样。这种设计使得简单问题在小壳内就能快速找到解，困难问题则自然扩大搜索范围。

### Q4: 论文做了哪些实验？

在数学推理和代码生成两个领域评估了ADAP算法。数学推理使用HMMT 2024和2025年竞赛共60道题，从Qwen2.5-Math-7B采样512个候选解，用Qwen2.5-Math-PRM-7B打分，验证采用精确答案字符串匹配，过滤后保留22道存在正确样本的题目。代码生成使用LiveCodeBench的中等和困难题目，从Qwen2.5-Coder-3B采样，用CodeScaler-8B打分，验证运行完整隐藏测试集，过滤后保留83道题。成本设置为生成成本1，验证成本10。对比方法包括：样本感知下界SAP（事后最优选择）、难度自适应策略DAP_k（按正确率分k类动态规划选最优(N_rew,N_ver)对）、以及成本匹配均匀策略Uni_{C_ADAP}。主要结果显示ADAP在成功率和成本之间取得更好平衡，数学任务上ADAP的平均成本为41.8，成功率达100%，而Uni_{C_ADAP}成本相近但成功率仅77.3%；代码任务上ADAP成本64.2，成功率100%，优于DAP_1的85.7%成功率。ADAP在两种任务中均接近理论最优下界SAP。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面：首先，ADAP的核心假设——奖励分数与验证通过概率单调递增——虽然在实验中成立，但理论上可能存在反例（如某些任务中高奖励样本因“奖励黑客”现象反而更易失败），未来可探索更宽松的假设（如部分单调性或多模态关系）。其次，常数因子400的竞争比虽具理论保证，但实际部署中可优化：通过贝叶斯方法实时估计分数分布和成功函数，动态调整采样和验证规模，而非固定的dyadic倍数。此外，当前假设每个prompt的分布相互独立，忽略了跨prompt的迁移学习潜力——可结合元学习或上下文Bandit，利用历史prompt的奖励-验证关系加速新prompt的适应。最后，实验仅覆盖数学推理和代码生成，未来应扩展至开放性任务（如文本生成中的人工评估），并探索“先验证后排名”的混合策略（如对低奖励样本也抽样验证），以应对真实场景中验证成本不对称或奖励模型严重偏差的情况。

### Q6: 总结一下论文的主要内容

这篇论文形式化了大语言模型推理时的生成-排序-验证流程，将其建模为**代价敏感的生成式主动搜索问题**，目标是找到一个已验证正确的响应，同时最小化生成样本和调用验证器的总代价。核心挑战在于，最优的生成和验证策略因提示词而异，固定策略效率低下。为此，作者提出了**ADAP**算法，一种壳状自适应方法，能够逐步增加候选样本和验证数量。在“高奖励分数更可能通过验证”这一单调性假设下，理论证明ADAP的期望代价能在常数因子内逼近已知最优分布的代价。作者还通过“中心星数”刻画了学习理论的界限，表明此类结构假设必不可少。在数学推理和编程竞赛任务上的实验表明，ADAP能以更低平均代价达到100%成功率，优于固定策略和基于难度自适应的基线方法。
