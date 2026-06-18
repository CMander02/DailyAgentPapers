---
title: "Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards"
authors:
  - "Yingyu Shan"
  - "Yuhang Guo"
  - "Zihao Cheng"
  - "Zeming Liu"
  - "Xiangrong Zhu"
  - "Xinyi Wang"
  - "Jiashu Yao"
  - "Wei Lin"
  - "Hongru Wang"
  - "Heyan Huang"
date: "2026-06-17"
arxiv_id: "2606.18810"
arxiv_url: "https://arxiv.org/abs/2606.18810"
pdf_url: "https://arxiv.org/pdf/2606.18810v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "LLM Agent"
  - "代码Agent"
  - "奖励设计"
  - "Token级信用分配"
relevance_score: 8.5
---

# Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. Existing token-level credit assignment methods require resources beyond the model's own rollouts. GRPO variants rely on process reward models or ground-truth answers. Knowledge distillation assigns credit through per-token divergence but requires external teachers (On-Policy Distillation) or privileged information (On-Policy Self Distillation). However, these dependencies limit applicability in the pure RLVR setting. We observe that conditioning the model on its own verified trajectories induces a measurable per-token KL divergence between the original and conditioned distributions, and prove that distilling from a self-teacher constructed by verified trajectories leads to infeasible weighted-average solutions when multiple verified trajectories exist. We propose SC-GRPO (Self-Conditioned GRPO), which uses KL divergence mentioned before as a multiplicative weight on GRPO gradients. Across five benchmarks spanning math, code, and agentic tasks, SC-GRPO consistently outperforms 8.1% over GRPO and 5.9% over DAPO with stronger OOD performance. Moreover, SC-GRPO achieves higher performance than OPD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决强化学习（RLVR）在训练大语言模型时存在的信用分配不当问题。现有方法如GRPO为所有token分配统一奖励，无法识别关键推理步骤，导致对关键token的梯度信号被稀释。虽然已有token级信用分配方法，但它们依赖外部资源：一些需要过程奖励模型或真实答案，另一些通过知识蒸馏需要外部教师模型或特权信息，这在仅能获得二元验证器的纯RLVR场景中难以应用。

论文的核心观察是：让模型以其自身验证过的正确轨迹为条件进行生成，会带来可测量的逐token分布偏移（KL散度）。基于此，作者提出SC-GRPO方法，利用这种自条件化产生的KL散度作为GRPO梯度的乘法权重，而非传统蒸馏中的加法损失。这样既保留了原始奖励信号的方向性，又通过KL权重实现了关键token的差异化更新。方法还巧妙处理了部分正确和全部错误两种场景，在数学、代码和Agent任务上显著优于现有方法。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**在线蒸馏方法**，如On-Policy Distillation及其变体（skew-KL、α-β-divergence等），它们通过学生生成轨迹与教师分布的散度进行训练，但需要更强的外部教师模型。本文方法（SC-GRPO）与它们的区别在于无需外部教师，仅利用模型自身验证轨迹构造自教师，并将KL散度作为逐token权重而非梯度方向。第二类是**自蒸馏方法**，如On-Policy Self Distillation，它们通过条件化特权信息（如文本反馈、真实答案）构建教师，但依赖外部监督。本文仅条件化于模型自身的已验证轨迹，消除了对特权信息的需求，且证明了多轨迹场景下加权平均解不可行。第三类是**过程奖励模型（PRM）**，如通过蒙特卡洛采样或分段采样估计token值的方法，但需要训练独立奖励模型或额外计算量。GRPO变体也依赖外部PRM或真实答案。本文的核心区别在于完全基于模型自身的rollout获取逐token奖励，无需任何外部资源。

### Q3: 论文如何解决这个问题？

SC-GRPO通过自条件化信用分配解决GRPO中令牌级信用分配不均的问题。核心方法是用模型自身生成的已验证轨迹构造自教师模型，计算令牌级KL散度作为梯度权重。

整体框架包含三个主要模块：1) **教师构造**：将已验证轨迹τ放入系统提示中，条件化当前策略π_θ，形成自条件化教师分布˜π_θ(·|s_{i,t},τ)。教师和学生共享同一模型参数（教师梯度停止），仅在输入前缀上不同。2) **KL加权**：在每组部分解决时，对每个令牌计算教师分布与学生分布的前向KL散度D_{i,t}，通过函数f(D)=D/(D+c)映射到[0,1)的权重。其中c取当前微批次活跃令牌KL的75分位数与最小值的最大值，保证低KL令牌被降权、高KL令牌保留。3) **组路由**：根据组内正确轨迹数n_c采用不同策略：部分解决组(n_c∈[2,G-1])使用GRPO优势；无解决组(n_c=0)以均匀采样的一个失败轨迹为参考，计算其余轨迹与该参考的条件化KL，形成多样性得分并归一化为伪优势，鼓励探索新模式；完全解决或单轨迹组则回退到标准GRPO。

创新点在于：将条件化KL作为乘法权重直接调制GRPO梯度，避免了蒸馏方法中多个已验证轨迹导致的不可行加权平均解问题；通过组路由机制在无正确轨迹时也能提取探索信号。实验显示SC-GRPO在五个基准上平均超越GRPO 8.1%、DAPO 5.9%，且越界性能更强。

### Q4: 论文做了哪些实验？

论文在数学推理、代码生成和多轮智能体交互三类任务上进行了实验。数据集包括：数学任务使用DAPO-Math-17k训练，在AIME 2024/2025上评估；代码任务使用LiveCodeBench v6，保留一半单元测试用于训练；智能体任务使用AppWorld和WebShop的官方划分。对比方法包括GRPO、DAPO、REINFORCE++以及三种OPSD变体（使用MiniMax-M2.7、DeepSeekv4-Pro和Oracle作为外部演示）。所有方法共享Qwen3-8B基础模型、训练数据和每提示8条轨迹的采样配置。评估指标为Avg@8（8条轨迹的平均验证奖励）和Pass@8（至少一条正确轨迹的问题比例）。主要结果：SC-GRPO在所有五个基准测试中取得最高性能，相比DAPO在Avg@8上平均提升5.86%，在Pass@8上提升8.92%，相比GRPO提升8.1%。在多轮智能体任务上改进最大。REINFORCE++性能不稳定，在数学和智能体任务上显著较弱。OPSD变体表现均接近基础模型，低于所有RL基线，甚至Oracle在代码任务上不如基础模型。实验表明SC-GRPO通过从模型自身验证轨迹构建自教师，实现了稳定且显著的性能提升。

### Q5: 有什么可以进一步探索的点？

论文在方法上存在几个可进一步探索的方向。首先，其核心创新——利用自条件化模型与原始模型间的KL散度作为逐token梯度权重——虽然在8B模型上效果显著，但受限于计算资源，未在更大规模模型（如70B+）或更长序列上验证。未来可测试该方法在大模型上的扩展性，观察KL信号是否仍能有效区分关键推理步骤。其次，实验仅覆盖标准推理模式，未涉及显式思维链、多步修正或结构化输出场景。在这些场景中，中间推理步对最终答案的贡献更加复杂，自条件化KL可能无法准确捕捉逐步信用分配，需要设计更细粒度的分离机制。此外，论文证明当存在多个验证轨迹时，自教师蒸馏会得到不可行的加权平均解，但SC-GRPO仅使用了当前轨迹的KL权重。一个潜在改进是引入多轨迹聚合策略（如置信度加权或对抗性采样），以缓解单一轨迹带来的偏差。最后，现有方法依赖GRPO基线的正态性假设，未来可探索与非正态分布策略（如基于重要性采样的方法）的结合，以增强鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出SC-GRPO方法，解决强化学习中基于可验证奖励（RLVR）的信用分配问题。GRPO等现有方法对所有token分配均匀信用，导致关键推理步骤信用不足，而非关键token浪费梯度。作者发现模型在其自身已验证轨迹条件下会产生可测量的per-token KL散度，并利用该散度作为GRPO梯度的乘性权重，实现细粒度信用分配，无需外部资源。实验在数学、代码和智能体任务五个基准上，SC-GRPO以最小计算开销一致超越GRPO（提升8.1%）和DAPO（提升5.9%），且超越在线策略蒸馏方法。该工作为纯RLVR场景下的token级信用分配提供了有效且鲁棒的方案。
