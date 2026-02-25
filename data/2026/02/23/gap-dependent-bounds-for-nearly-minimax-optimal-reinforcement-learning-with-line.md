---
title: "Gap-Dependent Bounds for Nearly Minimax Optimal Reinforcement Learning with Linear Function Approximation"
authors:
  - "Haochen Zhang"
  - "Zhong Zheng"
  - "Lingzhou Xue"
date: "2026-02-23"
arxiv_id: "2602.20297"
arxiv_url: "https://arxiv.org/abs/2602.20297"
pdf_url: "https://arxiv.org/pdf/2602.20297v1"
categories:
  - "stat.ML"
  - "cs.LG"
tags:
  - "强化学习"
  - "线性函数近似"
  - "极小极大优化"
  - "间隙依赖分析"
  - "多智能体强化学习"
  - "样本复杂度"
  - "理论分析"
relevance_score: 5.5
---

# Gap-Dependent Bounds for Nearly Minimax Optimal Reinforcement Learning with Linear Function Approximation

## 原始摘要

We study gap-dependent performance guarantees for nearly minimax-optimal algorithms in reinforcement learning with linear function approximation. While prior works have established gap-dependent regret bounds in this setting, existing analyses do not apply to algorithms that achieve the nearly minimax-optimal worst-case regret bound $\tilde{O}(d\sqrt{H^3K})$, where $d$ is the feature dimension, $H$ is the horizon length, and $K$ is the number of episodes. We bridge this gap by providing the first gap-dependent regret bound for the nearly minimax-optimal algorithm LSVI-UCB++ (He et al., 2023). Our analysis yields improved dependencies on both $d$ and $H$ compared to previous gap-dependent results. Moreover, leveraging the low policy-switching property of LSVI-UCB++, we introduce a concurrent variant that enables efficient parallel exploration across multiple agents and establish the first gap-dependent sample complexity upper bound for online multi-agent RL with linear function approximation, achieving linear speedup with respect to the number of agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习中线性函数近似背景下，近乎极小极大最优算法的“间隙依赖”（gap-dependent）性能保证问题。研究背景是，在处理大规模状态和动作空间时，线性函数近似是一种广泛采用的高效方法。已有大量工作为线性函数近似下的强化学习建立了遗憾上界，其中LSVI-UCB++等算法在最坏情况下实现了近乎极小极大最优的遗憾界（如 $\tilde{O}(d\sqrt{H^3K})$）。然而，现有方法的不足在于，尽管已有研究在线性MDP或线性混合MDP设定下建立了间隙依赖的遗憾界（例如 $\tilde{O}(d^3 H^5/\Delta_{\min})$ 或 $\tilde{O}(d^2 H^5/\Delta_{\min})$），但这些分析并未覆盖到像LSVI-UCB++这样达到近乎极小极大最优最坏情况遗憾的算法。这导致现有的间隙依赖遗憾界对特征维度 $d$ 和步长 $H$ 的依赖关系较为松散，未能充分反映这些算法在存在次优间隙时的潜在高效性。

因此，本文要解决的核心问题是：能否为线性函数近似下近乎极小极大最优的强化学习算法（特别是LSVI-UCB++）建立改进的间隙依赖遗憾上界，从而显著改善对 $d$ 和 $H$ 的依赖关系？这不仅具有理论意义，也对机器人、医疗等高维长周期任务的实际应用至关重要。此外，论文还利用LSVI-UCB++的低策略切换特性，进一步提出了一个支持多智能体高效并行探索的并发变体，旨在为在线多智能体强化学习建立首个间隙依赖的样本复杂度上界。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：近最优强化学习、间隙相关（Gap-Dependent）强化学习，以及基于线性函数近似的多智能体强化学习（MARL）。

在**近最优强化学习**方面，研究分为表格型RL和线性函数近似RL。表格型RL中，模型基方法（如UCBVI）和模型无关方法（如Q-learning变体）均能达到近乎极小极大最优的遗憾界。在线性函数近似RL中，主要围绕线性MDP和线性混合MDP两种结构假设展开。例如，LSVI-UCB算法首次在线性MDP中实现了无需生成模型的遗憾界，而后续的LSVI-UCB++算法进一步将遗憾改进至近乎最优的$\tilde{O}(d\sqrt{H^3 K})$。本文正是以LSVI-UCB++为基础，为其首次提供了间隙相关的分析。

在**间隙相关强化学习**方面，早期表格型RL工作主要关注渐近对数遗憾界，后续研究则转向非渐近的精细间隙依赖分析。在线性函数近似设置下，已有工作为LSVI-UCB和UCRL-VTR等算法提供了间隙依赖遗憾界，但其依赖关系在维度$d$和步长$H$上不够紧致。本文的分析显著改进了这些依赖关系，并为近乎最优的算法LSVI-UCB++建立了首个间隙依赖遗憾界，弥补了现有理论空白。

在**基于线性函数近似的MARL**方面，已有工作如Coop-LSVI将单智能体算法LSVI-UCB扩展到协作式并行设置，实现了有限通信轮次下的高效学习。本文则利用LSVI-UCB++的低策略切换特性，提出了一个支持高效并行探索的并发变体，并首次为在线多智能体线性RL建立了间隙依赖的样本复杂度上界，实现了关于智能体数量的线性加速。

### Q3: 论文如何解决这个问题？

论文通过改进LSVI-UCB++算法的理论分析，首次为具有线性函数逼近的强化学习提供了接近极小极大最优的间隙依赖（gap-dependent）后悔界。核心方法是基于LSVI-UCB++算法框架，通过精细的加权岭回归估计、乐观与悲观价值函数构造、以及方差感知的探索机制，实现对最优价值函数的高效学习。

整体框架沿用了LSVI-UCB++的在线学习流程，在每个回合中交替进行价值估计和策略执行。主要模块包括：1）加权岭回归模块，用于估计状态-动作值函数的线性参数；2）乐观与悲观价值估计模块，通过添加置信区间边界（bonus）构造高概率覆盖真实Q值的上界和下界；3）方差估计模块，通过额外回归问题估计价值函数的方差，用于调整数据权重；4）低策略切换（low policy-switching）机制，仅当协方差矩阵行列式显著增长时才更新价值函数，减少计算开销。

关键技术创新体现在三个方面：首先，算法采用双重价值估计（乐观上界Q和悲观下界ˇQ），通过两者差值控制估计误差，为间隙依赖分析奠定基础；其次，引入方差加权的最小二乘回归，其中权重¯σ²_k,h动态调整，包含估计方差、horizon长度和特征不确定性项，有效降低了高方差样本的影响；最后，利用LSVI-UCB++固有的低策略切换特性，设计了多智能体并发版本，将多个智能体在单轮内收集的轨迹视为单智能体的连续回合进行处理，仅在触发更新条件时同步更新策略，实现了线性加速。

理论贡献方面，论文证明了在适当设置超参数（λ=1/H², β=Õ(√d), ¯β=Õ(√d³H²), ˜β=Õ(√d³H⁴)）时，期望后悔上界为Õ(d²H⁴/Δ_min + d⁶H⁷)，较现有间隙依赖结果改进了对维度d和horizon H的依赖。进一步地，基于该后悔界推导出Õ(1/ε)的PAC样本复杂度，优于最坏情况下的Õ(1/ε²)依赖。对于多智能体场景，并发版本仅需Õ(d²H⁴/(MΔ_minε) + d⁶H⁷/(Mε))轮即可学习ε最优策略，在智能体数量M适中时实现线性加速。

### Q4: 论文做了哪些实验？

该论文主要进行理论分析，未涉及传统的数值实验或基准测试。研究重点在于为具有线性函数近似的强化学习算法建立理论保证，具体实验设置如下：

**实验设置**：研究基于线性MDP模型，算法为LSVI-UCB++及其并发变体。理论分析中，算法参数设置为正则化参数λ=1/H²，置信半径β、β̄、β̃根据理论推导设定，失败概率δ=1/(18T)。

**数据集/基准测试**：未使用具体数据集，而是基于理论框架进行分析。对比对象是先前工作中具有间隙依赖遗憾界的算法，如那些达到Õ(d√(H³K))最坏情况遗憾的算法。

**对比方法**：与现有间隙依赖遗憾界进行理论比较，特别是那些在d和H依赖上较弱的分析。论文指出，先前结果通常为Õ(d³H⁵/Δ_min)或Õ(d²H⁵/Δ_min)。

**主要结果与关键指标**：
1.  **单智能体遗憾界**：为LSVI-UCB++首次建立了间隙依赖的期望遗憾上界：O(d²H⁴/Δ_min * ι₁³ + d⁶H⁷ι₁²)，其中ι₁ = log(1+dHK/Δ_min)。这改进了对特征维度d和步长H的依赖（从H⁵降至H⁴）。
2.  **PAC样本复杂度**：以至少1-δ概率，经过K = Õ(d²H⁴/(Δ_min δϵ) + d⁶H⁷/(δϵ))幕学习后，可获得ϵ-最优策略。将ϵ的依赖从Õ(1/ϵ²)改进为Õ(1/ϵ)。
3.  **多智能体并发样本复杂度**：对于M个并行智能体，获得ϵ-最优策略所需的并发轮数上界为Õ(dH + d²H⁴/(MΔ_min δϵ) + d⁶H⁷/(Mδϵ))。当M = Õ(min{dH³/(Δ_min δϵ), d⁵H⁶/(δϵ)})时，算法实现关于智能体数量M的线性加速。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其理论分析主要集中于线性函数近似的理想化设定，且依赖于已知的“间隙”（gap）假设。未来研究可探索更复杂的函数近似类别，如深度神经网络，以验证间隙依赖理论在更实际场景下的适用性。此外，论文提出的多智能体并行算法虽能实现线性加速，但假设了智能体间完全独立的探索，未来可研究如何在部分信息共享或竞争协作的混合设定下保持理论保证。

从改进思路看，可考虑将间隙依赖的遗憾界推广到部分可观测马尔可夫决策过程（POMDP）或非平稳环境中，以增强算法的鲁棒性。同时，理论分析中对于间隙的先验依赖可能过强，未来可设计自适应算法，在未知间隙的情况下动态调整探索策略。最后，将样本复杂度理论结果与大规模实证验证结合，尤其是在高维实际任务（如机器人控制）中测试算法效率，将是推动该领域进展的关键方向。

### Q6: 总结一下论文的主要内容

该论文研究了具有线性函数近似的强化学习中，近乎极小极大最优算法的间隙依赖性能保证。核心问题是现有间隙依赖遗憾分析无法适用于达到近乎最优最坏情况遗憾界 $\tilde{O}(d\sqrt{H^3K})$ 的算法，这限制了理论理解的完整性。

论文的主要贡献是首次为近乎极小极大最优算法 LSVI-UCB++ 建立了间隙依赖的遗憾上界，从而填补了这一理论空白。其方法分析相比以往的间隙依赖结果，在特征维度 $d$ 和步长 $H$ 上实现了更好的依赖关系。此外，论文利用 LSVI-UCB++ 的低策略切换特性，提出了一个并发变体，能够在多个智能体间实现高效的并行探索。

主要结论是，该工作不仅为单智能体场景提供了改进的理论保证，还首次为具有线性函数近似的在线多智能体强化学习建立了间隙依赖的样本复杂度上界，并实现了相对于智能体数量的线性加速。这为设计高效、可扩展的强化学习算法提供了新的理论依据。
