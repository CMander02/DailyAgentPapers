---
title: "OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning"
authors:
  - "Yu Li"
  - "Rui Miao"
  - "Tian Lan"
  - "Zhengling Qi"
date: "2026-05-21"
arxiv_id: "2605.21851"
arxiv_url: "https://arxiv.org/abs/2605.21851"
pdf_url: "https://arxiv.org/pdf/2605.21851v2"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM推理"
  - "token级优势估计"
  - "强化学习"
  - "策略优化"
  - "数学推理"
  - "代码推理"
relevance_score: 7.5
---

# OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning

## 原始摘要

Reinforcement learning with verifiable rewards has become the standard recipe for improving LLM reasoning, but the dominant algorithm GRPO assigns a single trajectory-level advantage to every token, diluting the signal at pivotal reasoning steps and injecting noise at uninformative ones. Critic-free alternatives derived from on-policy distillation supply per-token signals through oracle-conditioned likelihood ratios, yet apply each signal in isolation from the trajectory-level evidence accumulated up to that position. We propose Oracle-Prompted Policy Optimization (OPPO), which rests on a single observation: the oracle signal used by prior distillation-style methods for local discrimination is also the natural Bayesian update of the model's belief about eventual success. Accumulating the signal along a trajectory yields, in closed form and at the cost of one extra forward pass, a running estimate of the success probability at every position, together with a token-level advantage that requires no learned value network and no additional rollouts. A first-order analysis factorizes the advantage into the per-token discrimination signal used by distillation methods modulated by a state weight that concentrates credit on genuinely pivotal tokens, with a directional variance-reduction guarantee. The framework admits two estimators differing only in which model scores the evidence: a \textit{self-oracle} that reuses the student and recovers the on-policy distillation reward as a strict special case, and a \textit{teacher-oracle} that delegates scoring to a stronger frozen model. On two base LLMs across seven mathematics, science, and code reasoning benchmarks, OPPO improves over GRPO, DAPO, and SDPO by up to $+6.0$ points on AMC'23 and $+5.2$ points on AIME'24, with gains that widen monotonically with response length.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）推理强化学习中，现有方法在细粒度信用分配上的不足。研究背景是，基于可验证奖励的强化学习已成为提升LLM推理能力的标准方法。然而，当前最主流的算法GRPO将单个轨迹级别的优势（advantage）赋予每一个token，这意味着在长达数百个token的推理链中，只有少数关键token（如策略选择、关键代数步骤）决定结果，而GRPO的“一刀切”做法会稀释这些关键token的信用信号，并向无关token注入噪声，随着推理链变长，问题愈发严重。尽管后续工作如Dr.GRPO、DAPO等改进了框架，但仍保留轨迹级别优势，未能实现token级细粒度信用分配。另一方面，一些方法尝试提供token级信号，但基于蒙特卡洛重采样的方法需要大量推理计算，隐式过程奖励模型需要在线更新，而基于蒸馏的先验知识方法（如使用语言模型比率 \(\log\lambda_t\)）虽然提供了token级信号，却将每个token的信用视为独立于历史累积证据的孤立一阶量，忽略了序列中“位置”的信念动态更新。因此，本文核心要解决的问题是：如何在不引入额外价值网络、不增加大量rollout成本的前提下，设计一种能够为每个token分配合适信用信号、且信号能够动态反映当前推理位置对最终成功可能性的不确定性程度的算法，从而更精准地引导模型在真正关键步骤上学习。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**中，GRPO（组相对策略优化）为核心基线，它为轨迹内所有token分配相同的轨迹级优势，稀释了关键推理步骤的信号并在无关位置注入噪声；本文通过贝叶斯价值递归提供token级优势，克服了GRPO的缺陷。**方法类**还包括基于策略蒸馏（OPD）的方法，如SDPO，它们利用或acles条件似然比提供逐token信号，但每个信号独立于轨迹累积证据；本文在此基础上引入状态权重，使信号随位置动态调整，保留了OPD的密集优势并修正其孤立性。**应用与比较类**中，DAPO等变体尝试改进GRPO，但方式不同；本文在七个数学、科学和代码推理基准上超越GRPO、DAPO和SDPO（如AMC'23提升+6.0分），性能增益随响应长度单调扩大。**理论类**中，PPO采用学习价值网络，但内存成本高；本文无需价值网络或额外采样，通过一次前向传播闭合地估计成功概率及其token级优势，具有方向方差减少保证。与这些工作相比，OPPO的核心创新在于将或acles信号视为贝叶斯更新并累积，实现了位置敏感的信用分配。

### Q3: 论文如何解决这个问题？

OPPO（Oracle-Prompted Policy Optimization）的核心创新在于利用贝叶斯证据累积机制实现token级别的信用分配，无需学习价值网络。其整体框架基于一个关键观察：之前蒸馏方法中用于局部判别的oracle信号，本质上是模型对最终成功概率的贝叶斯更新。

**核心方法**包括三个层次：首先，通过贝叶斯定理将成功概率的更新转化为逐token的对数几率加法递归式 \(\ell_{t+1} = \ell_t + \log\lambda_t^\star\)，其中\(\lambda_t^\star\)是成功分支与失败分支之间的贝叶斯因子。由此可闭式计算出每个位置的成功概率\(V_t\)和token级优势\(A_t = \sigma(\ell_t + \log\lambda_t^\star) - \sigma(\ell_t)\)，并满足累积信用恒等式\(\sum A_t = R - V_0\)。

**关键技术**在于构造\(\lambda_t^\star\)的两种可计算替代估计器，其设计依赖两个建模选择：1）成功条件分布近似为在提示后附加正确答案\(y^*\)的条件生成；2）失败条件分布近似为边际分布。这导出了统一估计器\(\lambda_t = \hat\pi(y_t|x,y_{<t},y^*) / \hat\pi(y_t|x,y_{<t})\)。自oracle版本（\(\hat\pi=\pi_\theta\)）仅需一次额外前向传播，恢复在线策略蒸馏（OPD）信号作为特例；教师oracle版本（\(\hat\pi=\pi_\phi\)，冻结的更强模型）则降低KL散度误差。

**创新点**包括：1）将优势分解为oracle证据\(\log\lambda_t\)（提供逐token判别信号）与状态权重\(V_t(1-V_t)\)（将信用集中于真正关键token）的乘积，具有方差缩减保证；2）先验\(V_0\)自动实现题目难度过滤；3）两种oracle版本构成灵活的设计轴，其中教师oracle在策略选择token上产生更尖锐的边际概率差异。最终，该框架以“一次额外前向传播”的代价实现了比GRPO等轨迹级方法更精确的细粒度信用分配。

### Q4: 论文做了哪些实验？

论文在7个推理基准上进行了实验，涵盖数学推理（GSM8K、MATH-500、AMC'23、AIME'24）、科学推理（GPQA-D、ARC-C）和代码生成（LCB）。所有方法在DeepScaleR（约4万道数学竞赛题）上训练，使用两个基础模型Qwen3-4B和Phi-4-mini-instruct。对比方法包括GRPO、Dr.GRPO、DAPO和SDPO。

主要结果：OPPO在所有基准上均超过基线，最大提升出现在AMC'23（+6.0点）和AIME'24（+5.2点）。具体而言，在Qwen3-4B上，基于GRPO的Self-OPPO在AIME'24达49.5%（比GRPO的46.4%高3.1%），Teacher-OPPO（使用Qwen3-32B作为教师）提升至51.3%；基于DAPO的Teacher-OPPO在AMC'23达61.5%（DAPO为55.8%）。消融实验显示，方向锚定（防止正梯度强化错误推理）贡献最大（移除后AIME'24降至43.0%），状态跟踪（V_t(1-V_t)因子）次要（移除后降至46.8%）。教师规模分析显示，性能随教师规模单调提升，4B→8B跳跃最大。按响应长度划分，OPPO在最长序列（1025+ token）上优势最大（62.8% vs GRPO的52.0%），验证了长链推理的方差减少。

### Q5: 有什么可以进一步探索的点？

从论文分析来看，OPPO通过贝叶斯值递归巧妙地将蒸馏式信号转化为token级优势，但存在几点可探索的空间。第一，当前方法依赖"正确性"二元标签，对于需要逐步中间状态校验的复杂推理任务（如多步数学证明或程序合成），可引入细粒度的过程奖励信号来替代最终的二元oracle。第二，教师-学生架构中，固定冻结教师模型可能在分布漂移时提供有偏信号，可设计动态教师选择机制或集成多教师进行贝叶斯加权。第三，理论框架的方差缩减依赖于状态权重的集中效应，对于长序列中稀疏关键token的检测仍依赖阈值设定，可探索学习自适应的注意力掩码来隐式标记关键位置。此外，将OPPO扩展到多智能体协作场景时，需要处理每个智能体局部证据的全局信用分配问题，这可能需要引入分布式贝叶斯更新机制。

### Q6: 总结一下论文的主要内容

OPPO通过贝叶斯递归方法解决了LLM推理中token级别信用分配问题。GRPO等现有方法将整个轨迹的单一优势值分配给每个token，模糊了关键推理步骤的信号并引入了噪声。OPPO基于一个关键发现：先前蒸馏方法用于局部歧视的oracle信号，本质上是模型对最终成功信念的贝叶斯更新。该方法沿着轨迹累积该信号，通过一次额外前向传播以闭式获得每个位置的成功概率运行估计，以及无需学习价值网络或额外采样的token级别优势。一阶分析将优势分解为蒸馏方法使用的逐token歧视信号与状态权重的乘积，该权重集中信用于真正关键的token，并具有方向性方差减少保证。OPPO提供两种估计器：自oracle和学生共享权重，以及教师oracle用更强冻结模型评分。在七个数学、科学和代码推理基准测试中，OPPO相比GRPO、DAPO和SDPO在AMC'23上提升高达+6.0分，在AIME'24上提升+5.2分，且增益随响应长度单调增加。
