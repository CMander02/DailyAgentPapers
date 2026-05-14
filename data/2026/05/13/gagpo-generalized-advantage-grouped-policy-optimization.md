---
title: "GAGPO: Generalized Advantage Grouped Policy Optimization"
authors:
  - "Siyuan Zhu"
  - "Chao Yu"
  - "Rongxin Yang"
  - "Zongkai Liu"
  - "Jinjun Hu"
  - "Qiwen Chen"
  - "Yibo Zhang"
date: "2026-05-13"
arxiv_id: "2605.13217"
arxiv_url: "https://arxiv.org/abs/2605.13217"
pdf_url: "https://arxiv.org/pdf/2605.13217v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "多轮Agent强化学习"
  - "信用分配"
  - "无评论家方法"
  - "时序差分优势"
  - "分组策略优化"
  - "ALFWorld"
  - "WebShop"
relevance_score: 9.5
---

# GAGPO: Generalized Advantage Grouped Policy Optimization

## 原始摘要

Reinforcement learning has become a powerful paradigm for post-training large language model agents, yet credit assignment in multi-turn environments remains a challenge. Agents often receive sparse, trajectory-level rewards only at the end of an episode, making it difficult to determine which intermediate actions contributed to success or failure. As a result, propagating delayed outcomes back to individual decision steps without relying on costly auxiliary value models remains an open problem. We propose Generalized Advantage Grouped Policy Optimization (GAGPO), a critic-free reinforcement learning method for precise, step-aligned temporal credit assignment. GAGPO constructs a non-parametric grouped value proxy from sampled rollouts and uses it to compute TD/GAE-style temporal advantages, recursively propagating outcome supervision backward through time. Combined with group-wise advantage normalization and an action-level importance ratio, GAGPO extracts stable, localized optimization signals directly from multi-turn trajectories. Experiments on ALFWorld and WebShop show that GAGPO outperforms strong reinforcement learning baselines. Further analyses demonstrate faster early-stage learning, improved interaction efficiency, and smoother optimization dynamics, suggesting that GAGPO offers a simple yet effective framework for multi-turn agentic reinforcement learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多轮交互环境下大型语言模型智能体训练的信用分配问题。研究背景是，大语言模型正从单轮助手发展为能够与环境进行多轮交互的智能体，强化学习是这一转变的关键后训练范式。然而，现有方法存在明显不足：一方面，奖励信号稀疏且延迟，通常只在回合结束时给出轨迹级别的奖励，难以确定中间步骤的贡献；另一方面，尽管已有PPO等基于批评者的方法，但它们依赖额外的价值模型或过程奖励模型，增加了训练复杂度和估计误差；而无批评者方法如GRPO虽结构简单，但监督信号方差大且传播弱，无法实现步骤级别的对齐优化。本文核心问题是：在不依赖辅助批评者或特殊搜索过程的情况下，如何对标准多轮交互轨迹中的每一步动作进行精确、时域对齐的信用分配。为此，作者提出GAGPO，一种基于采样轨迹分组构建非参数化价值代理、并采用TD/GAE风格时域优势估计的无批评者强化学习方法，将稀疏结果监督递归传播回每个环境步骤。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类。第一类是基于强化学习的LLM后训练方法：经典方法如PPO需要学习价值函数（critic），计算昂贵且估值敏感；偏好方法如DPO虽无需在线RL但无法处理探索或多轮交互；近期无critic的在线策略方法如RLOO、GRPO、DAPO和GSPO主要面向单轮生成或序列级推理。本文GAGPO将这些无critic分组方法扩展到多轮智能体训练中，实现了时间传播的逐步骤信用分配。第二类是智能体RL中的信用分配方法：一部分引入辅助critic或过程奖励模型（如AgentPRM、iStar、Turn-PPO、SORL）来获得稠密步骤级信号，但需要额外建模；另一部分在无critic分组优化中追求更细粒度信用（如GiGPO的锚点状态分组、Tree-GRPO、AT²PO、ARPO的树形或轮次结构 rollout）。相比之下，GAGPO保持无critic且基于rollout，但用自举的TD/GAE风格时间估计器替代蒙特卡洛或相对回报估计，无需额外critic即可实现步骤对齐的信用传播，在ALFWorld和WebShop上显著优于GRPO和GiGPO等基线。

### Q3: 论文如何解决这个问题？

GAGPO通过构建无评论家的时序信用分配机制解决多轮环境中稀疏奖励的信用分配问题。核心方法是用非参数化的分组价值代理取代传统的价值函数，基于采样轨迹组中状态一致的动作步骤构建价值代理：对每个状态，收集所有轨迹中该状态出现的步骤，计算其折扣回报的平均值作为该状态的价值估计。基于此代理计算时序差分残差，并采用GAE方式递归定义步骤级的时序优势，将延迟的结局信号通过时间反向传播到每个决策步。

主要创新点包括：一是设计了状态级分组价值代理，无需额外训练价值模型，仅从已收集轨迹中构建；二是采用步骤级时序优势作为唯一优化信号，避免传统方法中引入轨迹级全局偏移导致步骤间对比度降低；三是引入组归一化，在保持组内比较结构的同时消除跨任务尺度差异；四是使用动作级长度归一化重要性比率，为同一动作内所有token分配共享优势值。

整体框架遵循PPO风格的分组优化范式，但用时序优势替代蒙特卡洛相对优势，配合裁剪目标和KL散度约束实现稳定优化。实验表明该方法相比基线具有更快的早期学习速度、更好的交互效率和更平滑的优化动力学。

### Q4: 论文做了哪些实验？

论文在ALFWorld（家庭场景多轮决策）和WebShop（在线购物多轮交互）两个文本基准上评估GAGPO。使用Qwen2.5-1.5B-Instruct和Qwen2.5-7B-Instruct作为基础模型。对比方法包括：基于提示的（直接提示、ReAct、Reflexion、GPT-4o、Gemini-2.5-Pro）和基于RL的（PPO、RLOO、GRPO、GiGPO）。主要结果：GAGPO在所有基准和模型尺度上一致优于所有RL基线。在ALFWorld上，对1.5B模型，总体成功率从基线最强88.1提升至93.5（+5.4）；对7B模型，从88.8提升至95.6（+6.8）。在WebShop上，对1.5B模型，分数从80.5提升至88.6，成功率从66.4提升至78.1；对7B模型，分数从86.3提升至90.3，成功率从73.3提升至77.5。消融实验显示，去除时间递归（λ=0）、使用MC式优势、去除动作序列重要性比率、添加轨迹奖励广播、使用批归一化或无归一化，性能均全面下降，证实了完整GAGPO各组件的必要性。实验还分析了学习动态，GAGPO在早期训练中提升更快，交互效率更高（更短的平均回合长度），优化更稳定（梯度范数更低、熵损失下降更单调），并产生更集中的优势分布（在步骤120，GAGPO的IQR为0.56，|A|>1的比例为17.2%，而GiGPO为1.61和43.1%）。

### Q5: 有什么可以进一步探索的点？

GAGPO的局限性主要集中在三点：首先，其核心的非参数分组价值代理依赖于精确状态匹配，这在随机观测、连续输入或部分可观测环境中难以为继，未来可探索基于嵌入的聚类或学习等价关系实现近似状态聚合。其次，实验仅局限于ALFWorld和WebShop两个文本基准，且只用了稀疏端奖励和离散动作，尚未验证在密集过程奖励、混合奖励源、连续异步交互或更大规模、更多样化智能体领域中的有效性，未来需扩展至更复杂的长时域环境。最后，尽管实验环境封闭，但更强的多轮智能体训练可能降低开放环境部署门槛，带来自动化不良行为或资源浪费风险，因此实际应用中必须结合沙盒、权限控制和人机协同等安全措施。改进思路包括：引入对比学习或自监督方法构建状态表示空间，以替代精确匹配；设计自适应奖励混合机制；以及开发环境交互约束框架，在保证训练效率的同时提升安全边界。

### Q6: 总结一下论文的主要内容

GAGPO（广义优势分组策略优化）是一种免评论家的强化学习方法，旨在解决多轮交互环境中智能体的信用分配问题。传统方法常面临稀疏奖励和延迟反馈，难以将最终成败归因于中间步骤。GAGPO通过以下核心设计实现精确的步骤级时间信用分配：首先，从采样轨迹中构建非参数分组价值代理，基于相同环境状态的分组；其次，采用TD/GAE风格的时间递归将结果监督信号反向传播至各决策步骤；最后，结合分组级优势归一化和动作级重要性比率，获得稳定且局部化的优化信号。在ALFWorld和WebShop基准测试中，基于Qwen2.5-1.5B/7B-Instruct模型的实验表明，GAGPO在性能上持续超越PPO、GRPO等强基线，并展现出更快的早期学习速度、更高的交互效率和更平滑的优化动态。主要结论是，通过将信用分配单位从token对齐至环境步骤并进行时间传播，免评论家分组方法可更高效地训练多轮智能体。
