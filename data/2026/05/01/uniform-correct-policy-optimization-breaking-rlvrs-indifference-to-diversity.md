---
title: "Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity"
authors:
  - "Anamika Lochab"
  - "Bolian Li"
  - "Ruqi Zhang"
date: "2026-05-01"
arxiv_id: "2605.00365"
arxiv_url: "https://arxiv.org/abs/2605.00365"
pdf_url: "https://arxiv.org/pdf/2605.00365v1"
github_url: "https://github.com/AnamikaLochab/UCPO"
categories:
  - "cs.LG"
  - "cs.CL"
  - "stat.ML"
tags:
  - "RLVR"
  - "策略优化"
  - "多样性崩塌"
  - "GRPO"
  - "推理任务"
  - "数学推理"
  - "一致性正则化"
relevance_score: 8.5
---

# Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has achieved substantial gains in single-attempt accuracy (Pass@1) on reasoning tasks, yet often suffers from reduced multi-sample coverage (Pass@K), indicating diversity collapse. We identify a structural cause for this degradation: common RLVR objectives, such as GRPO, are indifferent to how probability mass is distributed among correct solutions. Combined with stochastic training dynamics, this indifference induces a self-reinforcing collapse, in which probability mass concentrates on a narrow subset of correct outputs while alternative valid solutions are suppressed. We formalize this collapse mechanism and further characterize the optimal policy structure under two complementary criteria: robustness and entropy-regularized optimality, which identify the Uniform-Correct Policy as uniquely optimal. Motivated by this analysis, we propose Uniform-Correct Policy Optimization (UCPO), a modification to GRPO that adds a conditional uniformity penalty on the policy's distribution over correct solutions. The penalty redistributes gradient signal toward underrepresented correct responses, encouraging uniform allocation of probability mass within the correct set. Across three models (1.5B-7B parameters) and five mathematical reasoning benchmarks, UCPO improves Pass@K and diversity while maintaining competitive Pass@1, achieving up to +10\% absolute improvement on AIME24 at Pass@64 and up to 45\% higher equation-level diversity within the correct set. The code is available at https://github.com/AnamikaLochab/UCPO.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决强化学习与可验证奖励（RLVR）在推理任务中导致模型多样性坍塌的核心问题。研究背景是，RLVR（如GRPO算法）在提升单次准确率（Pass@1）方面表现出色，但在多次采样覆盖率（Pass@K）上却经常下降，这表明模型生成解决方案的多样性严重受损。现有方法的不足在于：它们多通过熵奖励、探索激励或token级约束来缓解多样性损失，但都未能直接规定正确解的概率质量应该如何分配。缺乏一个原则性的目标，导致这些方法只能满足局部启发式（如token级熵），而模型仍可能将概率质量集中在少数几个正确解上。本文要解决的核心问题是：在RLVR框架下，当存在多个正确解时，现有目标对概率质量在正确解之间的分配方式本质上是漠不关心的（即“无差别”），这种目标上的无差别性结合随机训练动态，会引发自我强化的模式坍塌，使得模型最终只输出少数几种正确路径。作者提出，理想的最优策略应该是“均匀正确策略”（Uniform-Correct Policy），即只给正确解分配非零概率且在它们之间均匀分布。为了达成这一最优结构，本文提出了均匀正确策略优化（UCPO），通过在GRPO中添加一个针对正确解的条件均匀性惩罚，重新分配梯度信号以放大未被充分代表的正确响应，从而打破无差别性导致的多样性坍塌。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：1）**分析驱动的方法**，直接诊断多样性坍塌机制并提出针对性修复。如一些工作将坍塌归因于正概率-优势协方差导致的熵衰减，提出协方差梯度裁剪和KL正则化；另一些工作表明KL正则化RLVR中的选择和强化偏差会放大正确集内的基策略不平衡，提出差分平滑；还有工作发现高成功率简单提示驱动正确性质量集中，提出焦点优势缩放；LAD指出期望优势最大化扭曲正确响应间的比例，代之以保留先前策略比例的f-散度目标。本文与这些工作的区别在于，本文识别出RLVR优势最大化目标对正确集内分配无动于衷这一结构原因，提出的UCPO通过将梯度质量重新分配至正确响应来重塑正确集内分布趋向均匀。2）**熵基方法**，通过维持训练随机性缓解坍塌，但全局熵正则化可能增加错误响应概率，而局部令牌级方法仍可能允许最终解集坍塌。3）**轨迹级探索方法**，通过自适应展开分配、定向探索或外部数据扩展推理轨迹。这些方法与UCPO互补，前者扩展训练中采样轨迹集，而UCPO在条件分布层面重塑正确响应的梯度分配。

### Q3: 论文如何解决这个问题？

UCPO通过引入条件均匀性惩罚机制直接解决RLVR中的多样性崩溃问题。整体框架基于GRPO，但新增了一个核心模块：KL散度条件均匀性惩罚项，用于约束策略在正确解集上的概率分配。具体地，给定提示x，定义正确解集Y+(x)上的条件策略q_θ(y|x)=π_θ(y|x)/Z_θ(x)和均匀分布u(y|x)=1/|Y+(x)|，UCPO目标函数为L_UCPO(θ)=E[log Z_θ(x) - τ KL(u||q_θ)]，其中第一项最大化正确响应总质量，第二项通过KL散度惩罚促使q_θ接近均匀分布。关键技术在于梯度分解：∇L_UCPO = Σ[(1-τ)q_θ+τ·u]∇logπ_θ，通过重要性采样估计，为低概率正确解分配更大权重w_i=(1-τ)/n+τ·v_i/Σv_j，实现优势重分配（总优势质量守恒）。创新点包括：（1）理论证明均匀正确策略是UCPO唯一最优解；（2）相比全局熵正则化，条件惩罚直接调控正确集内分布，避免增加错误输出概率；（3）零额外计算开销，直接复用GRPO的验证器采样。该设计在1.5B-7B模型上实现Pass@64提升10%，正确集内多样性提升45%。

### Q4: 论文做了哪些实验？

论文在三个模型（DeepSeek-R1-Distill-Qwen-1.5B、7B 和 Qwen2.5-7B）和五个数学推理基准（AIME 2024/2025、AMC 2023、MATH 500、OlympiadBench）上评估了 UCPO。训练集使用 DeepScaleR 语料库中的 10K 竞赛题，预留 500 题做验证。对比方法包括标准 GRPO 以及五种多样性保持基线：熵正则化（Ent-Reg）、熵优势奖励（Ent-Adv）、协方差 KL 控制（KL-Cov）、Pass@K 导向训练和 FGRPO。主要实验报告了 Pass@1 和 Pass@64。结果表明，UCPO 在保持与 GRPO 竞争性 Pass@1 的同时，在 Pass@64 上持续提升：DeepSeek-1.5B 模型平均 Pass@64 达 78.27%（比 GRPO 高 +3.5 点），在 AIME25 和 AMC 上分别提升 +6.7 和 +6.0；DeepSeek-7B 上平均提升 +3.6 点，AIME24 提升 +10.0；Qwen2.5-7B 上平均 Pass@64 达 73.19%（比 GRPO 高 +4.8）。此外，通过方程级多样性指标（正确解集中唯一数学表达式的比例）衡量多样性，UCPO 在所有基准上均最高，平均 0.215（GRPO 为 0.182），AIME 上提升 45%，MATH 上提升 13%。

### Q5: 有什么可以进一步探索的点？

UCPO通过强制均匀性提升多样性，但在理论层面仍存在局限。未来可探索以下方向：1) 动态公平性机制：当前均匀校正可能过度抑制高概率正确解，可引入自适应权重，根据任务难度动态调整均匀性惩罚强度；2) 结构化多样性：UCPO仅控制正确解概率均匀，未考虑解空间的语义拓扑结构，可结合聚类或对比学习，在等价类内而非全体正确解上施加约束；3) 跨任务泛化：数学推理有明确正确性判定，但在开放式生成任务中“正确”定义模糊，需设计软标签或置信度引导的多样性奖励；4) 联合优化框架：将Pass@1与Pass@K作为多目标优化问题，通过帕累托前沿搜索实现精度-多样性权衡；5) 理论扩展：分析均匀校正策略对收敛速度的影响，并探索离散策略空间中熵正则化与均匀约束的等价条件。

### Q6: 总结一下论文的主要内容

这篇论文发现，基于可验证奖励的强化学习（RLVR）虽然能提升推理任务单次准确率（Pass@1），但会导致多样性崩溃，降低多次采样覆盖率（Pass@K）。作者识别出这一结构性问题：常见RLVR目标（如GRPO）对正确解内部的概率分布无差别，结合随机训练动力学，会诱发自我强化的坍缩，使概率质量集中在少数正确输出上。理论分析表明，最优策略应是均匀正确策略，即在所有正确解上均匀分配概率。为此，论文提出均匀正确策略优化（UCPO），通过添加条件均匀性惩罚，重新加权梯度，放大被低估的正确解，抑制主导解。在多个模型（1.5B-7B参数）和五个数学推理基准上，UCPO在保持Pass@1的同时，显著提升了Pass@K和多样性，在AIME24上Pass@64绝对提升达10%。该工作强调了显式塑造策略多样性结构对RL训练大模型的重要性。
