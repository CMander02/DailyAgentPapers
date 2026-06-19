---
title: "VIMPO: Value-Implicit Policy Optimization for LLMs"
authors:
  - "Zhewei Kang"
  - "Aosong Feng"
  - "Sergey Levine"
  - "Dawn Song"
  - "Xuandong Zhao"
date: "2026-06-18"
arxiv_id: "2606.20008"
arxiv_url: "https://arxiv.org/abs/2606.20008"
pdf_url: "https://arxiv.org/pdf/2606.20008v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent 推理增强"
  - "强化学习"
  - "策略优化"
  - "信用分配"
  - "数学推理"
relevance_score: 7.5
---

# VIMPO: Value-Implicit Policy Optimization for LLMs

## 原始摘要

Reinforcement learning with verifiable rewards has become a central tool for improving the reasoning ability of large language models, but current methods face a trade-off between simplicity and credit assignment. Group-relative methods such as GRPO avoid training a critic, but typically assign a trajectory-level advantage to every token. Actor-critic methods provide denser learning signals, but require a learned value function with its own training instability. We introduce VIMPO, a critic-free policy optimization method that derives a policy-implied value function from the optimality conditions of KL-regularized reinforcement learning. For autoregressive generation, the resulting value recurrence can be written in terms of policy-reference log-ratios and anchored by the terminal condition that no future reward remains at the end of a trajectory. This gives a simple value loss that incorporates outcome-level verifiable rewards without training a critic. The same derivation also yields a critic-free actor advantage, allowing VIMPO to separate reward incorporation through the value loss from policy improvement through a PPO-style actor update. On mathematical RLVR benchmarks, VIMPO improves over GRPO across MATH-500, AIME 2024, AIME 2025, and OlympiadBench, with especially larger gains on competition-style evaluations. Under noisy rewards, VIMPO retains a consistent advantage over GRPO, suggesting that policy-implied value optimization can provide finer credit assignment while preserving the practical simplicity of critic-free training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决强化学习微调大语言模型（LLMs）时，现有方法在简单性与细粒度信用分配之间的权衡问题。研究背景是，基于可验证奖励的强化学习已成为提升LLMs推理能力的关键技术，但当前方法存在明显不足：组相对方法（如GRPO）虽避免了训练价值网络（critic），保持了训练简单性，但只能为整个轨迹分配相同的优势，无法区分关键推理步骤与常规连接性token，导致信用分配非常粗糙；而演员-评论家方法（如PPO）虽能提供密集的token级学习信号，但需要额外学习价值函数，训练不稳定且易受评论家质量与策略-评论家协同适应问题的困扰。核心问题是：能否在不训练显式价值网络的前提下，实现token级别的细粒度信用分配，从而兼顾简单性与密集监督？为此，论文提出VIMPO方法，通过从KL正则化强化学习的最优性条件中推导出策略隐含的价值函数，将价值函数表达为策略与冻结参考模型的对数比，并利用轨迹末端零价值的边界条件形成价值递归，从而在无需评论家的情况下实现贝尔曼一致性优化和目标级奖励整合，同时通过闭式时间差分优势实现token级策略更新。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**带值函数的演员-评论家方法**，如PPO和VAPO。它们通过训练一个额外的价值模型为每个token提供密集的信用分配信号，但价值模型的训练误差和稳定性问题会干扰策略优化。本文的VIMPO旨在实现同样的token级信用分配，但无需训练一个独立的评论家网络。第二类是**无评论家与事后信用分配方法**，包括GRPO和DAPO。它们通过在同一prompt的多个采样结果中估算优势函数，避免了价值网络训练，但优势信号通常是轨迹级别的，并被均分给所有token。后续工作如FIPO和基于注意力机制的方法尝试通过辅助权重规则进行事后细粒度分配。VIMPO则从KL正则化最优条件与策略隐含价值递归中直接推导出token级的演员信号，而非依赖外部加权。第三类是**对数比率参数化与贝尔曼一致性**，如DPO、IPO和TDPO。这些工作利用策略与参考策略的对数比率来表征最优策略，但主要应用于离线偏好优化。VIMPO虽同样使用策略-参考对数比率，但将其应用于在线强化学习；同时，它通过贝尔曼一致性方程推导出无评论家的价值损失与演员优势，这与基于一致性的强化学习方法（如Path Consistency Learning）在思想上相关，但VIMPO专为LLM后训练中的自回归生成设计，并显式保留了参考策略的对数比率项。

### Q3: 论文如何解决这个问题？

VIMPO通过推导策略隐含的价值函数实现无评论家的策略优化。核心方法基于KL正则化强化学习的最优性条件，推导出π*(a|s)与π_ref的比例关系与贝尔曼残差间的恒等式。架构包括两大模块：**价值损失**和**演员损失**，整体框架采用PPO风格的交替更新。

主要技术步骤为：1）基于最优性条件得到恒等式βln(π*/π_ref) = r + γV* - V* + βKL*，从而获得价值函数的一步递推关系；2）利用终端状态V(π)(s_T)=0作为锚点，构建无评论家的价值损失L_V(π)=1/2·V(π)(s_T)^2，在仅有结局奖励时简化为累积对数比值与中心化最终奖励之差的平方；3）从同一恒等式导出策略隐含的优势函数A_t^TD = βln(π/π_ref) - βKL，无需奖励r；4）将A_t^TD进行GAE累积并归一化后，用于PPO裁剪演员损失L_A。

创新点在于：通过理论推导将奖励信息完全整合进价值损失，而演员损失仅依赖策略-参考对数比值，实现了奖励集成与策略优化的分离。无需训练价值网络，同时提供比GRPO更细粒度的信用分配——每个token都能获得稠密的学习信号，这在数学推理测试中带来显著提升。

### Q4: 论文做了哪些实验？

论文在数学推理RLVR设置下对VIMPO进行了全面实验。首先评估最终准确率：从Qwen3-4B-Base出发，在Guru数学子集上训练，对比GRPO（包括naive GRPO和token级GRPO）和VIMPO，并测试MATH-500、AIME 2024、AIME 2025和OlympiadBench。关键超参数为β=5×10⁻⁴和演员系数c_A=5×10⁻³。结果显示，VIMPO在各基准上均取得最高分，平均准确率达39.5%，优于GRPO的37.4%和naive GRPO的36.6%，在AIME 2025上提升显著（从17.6%到20.8%）。训练曲线表明VIMPO的学习动态更强，且其提升不是单纯由响应长度增加所致。

其次，在嘈杂奖励压力测试中，以25%概率翻转奖励标签训练200步。VIMPO在所有基准上保持一致性优势，平均准确率35.9%，远高于GRPO的32.2%，尤其在AIME评估中差距更大，表明VIMPO对奖励噪声更不敏感。

最后，对VIMPO的β和c_A进行消融实验，对比仅值函数（c_A=0）、主设置和高β高c_A设置。主设置训练加速最快且准确率最高，但VO KL更高；仅值函数变体学习较慢；高β高c_A设置限制了策略更新，准确率接近仅值函数基线。消融支持VIMPO作为值损失与演员更新组合的设计。

### Q5: 有什么可以进一步探索的点？

论文的一个核心局限性在于固定参考策略和KL系数β，这可能导致后期训练中过度约束策略更新空间。未来可以探索自适应调节β或周期性更新参考策略，让目标函数在早期提供稳定性，后期则允许更大探索。此外，当前使用精确全分布KL计算代价高昂，可尝试近似KL估计或缓存参考分布来提升可扩展性，但需注意这可能改变值目标函数的居中性质。实验范围也较为有限，仅基于4B数学推理模型，未覆盖代码生成、工具使用、开放式指令遵循等任务，也未与大模型或PPO/VAPO等精心调优的actor-critic方法对比。未来应拓展到更多可验证领域、随机种子、模型规模，并与tuned actor-critic基线进行系统对比。在这些设定下，VIMPO的优势是否依然显著，特别是在依赖密集状态价值信号的任务中，值得深入研究。

### Q6: 总结一下论文的主要内容

这篇论文提出了VIMPO（价值隐式策略优化），一种无需评论家的策略优化方法，旨在解决大语言模型推理能力提升中简单性与信用分配之间的权衡。问题定义是：当前方法中，GRPO等组相对方法虽简单但给每个token分配轨迹级优势，而演员-评论家方法虽提供密集信号但需学习价值函数且训练不稳定。VIMPO从KL正则化强化学习的最优性条件中推导出策略隐含的价值函数，利用自回归生成过程的确定性转移，将价值递归表示为策略-参考对数比，并通过终止边界条件进行训练，无需单独评论家。其核心贡献是提供了一个简洁的价值损失和评论家免费的优势函数，将奖励通过价值损失与策略改进分离。主要结论表明，在MATH-500、AIME 2024/2025和OlympiadBench等数学推理基准上，VIMPO相比GRPO有显著提升，尤其在竞赛型评估中优势更大，且在噪声奖励下表现更稳健，表明该方法能实现更细粒度的信用分配，同时保持无评论家训练的简洁性。
