---
title: "What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents"
authors:
  - "Xiaozhe Li"
  - "Tianyi Lyu"
  - "Yang Li"
  - "Yichuan Ma"
  - "Peiji Li"
  - "Linyang Li"
  - "Qipeng Guo"
  - "Dahua Lin"
  - "Kai Chen"
date: "2026-05-19"
arxiv_id: "2605.19447"
arxiv_url: "https://arxiv.org/abs/2605.19447"
pdf_url: "https://arxiv.org/pdf/2605.19447v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Multi-Turn Agent"
  - "Reinforcement Learning"
  - "Credit Assignment"
  - "Distillation"
  - "Selective Feedback"
  - "ALFWorld"
  - "WebShop"
relevance_score: 9.5
---

# What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents

## 原始摘要

Reinforcement learning can train LLM agents from sparse task rewards, but long-horizon credit assignment remains challenging: a single success-or-failure signal must be distributed across many actions. Existing methods rely on trajectory-level rewards or proxy signals, without fully leveraging per-step environmental feedback. Multi-turn agent settings are underexplored, where feedback can include error messages, page changes, observations, or reference trajectories. We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework. SERL uses the task reward to determine update direction, while environment feedback adjusts placement and magnitude, focusing on critical actions. On ALFWorld and WebShop, SERL achieves 90.0% and 80.1% success, outperforming strong RL and distillation baselines. Analysis shows that grounded, action-relevant feedback at meaningful points consistently outperforms indiscriminate use of longer or richer context.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在长程多轮对话智能体（multi-turn agents）训练中，强化学习面临的信用分配难题。研究背景是，大语言模型被部署为交互式智能体时，虽然能从稀疏的任务奖励信号（如最终成功或失败）中学习，但将单一的成败信号合理分配到长序列中多个动作上极具挑战。现有方法，如GRPO等组相对方法，对整个轨迹施加统一的优势值，导致高杠杆决策（如改变环境的关键步骤）与常规导航、格式化等无关动作收到相同的更新，无法区分关键动作。此外，现有工作（如SDPO、RLSD）在处理环境反馈时，要么在单轮推理任务中研究，未考虑多轮智能体的长程特性；要么缺乏对反馈来源（如错误信息、页面变化、参考轨迹等）和插入粒度（逐步骤或仅语义变化点）的系统设计。核心问题在于：如何利用环境提供的密集逐步骤反馈（如错误消息、页面更新）进行更精细的信用分配，同时避免教师模型因其后见之明（privileged information）带来的信息泄露风险，从而在保持优化方向由任务奖励主导的前提下，选择性、有节制地利用环境反馈来调整更新的位置和幅度，以提升训练稳定性和任务成功率。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **强化学习方法**：以PPO、GRPO、RLOO等为代表的策略优化方法，通过评分函数提供轨迹级奖励进行训练。本文指出这些方法在长周期智能体任务中存在信用分配问题，无法有效利用环境反馈。本文提出的SERL不同于GRPO等对所有token施加相同优势，而是利用环境反馈选择性调整更新方向和粒度。

2. **信用分配方法**：包括过程奖励模型、价值模型和中间评估器等，它们通过更密集的监督信号改善信用分配。但本文强调这些方法常需要辅助模型或代理信号，与真实环境反馈脱节。SERL直接利用环境反馈（如错误信息、页面变化、参考轨迹）作为调整依据，无需额外模型。

3. **知识蒸馏方法**：如OPD、SDPO、RLSD等，通过更强的教师模型提供token级监督信号。本文指出这些方法计算成本高且存在分布偏移问题。SERL创新性地将蒸馏与环境奖励结合，但去除了对额外教师模型的依赖，而是利用环境反馈作为“教师”来指导学习，实现了更有效的选择性回溯蒸馏。

### Q3: 论文如何解决这个问题？

SERL（Selective Environment-Reweighted Learning）提出了一种选择性事后蒸馏框架，核心是解耦奖励方向与反馈强度。整体框架基于GRPO强化学习范式，但解决了其粗粒度信用分配问题：标准GRPO将任务奖励的组相对优势（advantage）广播给轨迹所有token，导致决定性和冗余动作获得相同更新。

关键技术包括三部分。首先，**反馈源与放置解耦**：系统研究五种事后环境反馈源（即时反馈、下一步观测、未来轨迹、成功轨迹、当前轨迹）和两种放置粒度（步级和锚点级）。锚点级通过语义状态聚类将相同状态下的步骤分组，聚合反馈（如取平均），避免密集噪声，将反馈集中在有意义的状态转换点。其次，**带符号的置信权重**：教师模型（条件化放置后的环境反馈）对学生采样动作计算对数概率差Δ，该差值经sgn(advantage)符号控制后，通过指数函数映射为裁剪后的权重w。对于优势为正的动作，教师支持的动作获得更大更新权重；优势为负时，教师支持的动作惩罚更轻，反对的动作惩罚更重。权重仅作用于可执行动作token，推理/格式token保持原始GRPO权重。最后，**渐进式衰减**：训练早期α较大，充分利用事后密集信号弥补探索不足；后期α衰减，让环境奖励主导优化方向，避免特权信息过拟合。最终损失由重加权RL目标和轻量动作蒸馏KL项组成，避免对整个推理链蒸馏的噪声。

### Q4: 论文做了哪些实验？

论文在 ALFWorld 和 WebShop 两个基准上进行了实验。ALFWorld 是包含6类家庭任务（如Pick、Look等）的多步决策环境，共3827个实例；WebShop 是包含110万产品和1.2万指令的在线购物模拟环境。

对比方法包括：1) 提示方法（ReAct、Reflexion）；2) RL训练方法（PPO、RLOO、GRPO、GIGPO、HGPO）；3) RL-蒸馏混合方法（SDPO、GRPO+SDPO、RLSD）。所有方法使用Qwen2.5-7B-Instruct作为基础模型，超参数保持一致（组大小N=8，学习率1e-6）。

主要结果：SERL在ALFWorld上达到90.0%平均成功率（高于最强纯RL基线HGPO的85.8%和GRPO的75.3%），在WebShop上达到89.5分和80.1%成功率（高于HGPO的88.4分和77.8%）。在反馈来源分析中，即时环境反馈本身就很强（ALFWorld 90.0%），但结合成功轨迹可提升至90.4%。反馈放置分析显示，锚点级放置（对相似状态分组）配合即时反馈可提升WebShop分数至91.5。使用Kimi-K2.6进行LLM判断反馈时，当前轨迹加成功轨迹达到WebShop 81.8%成功率。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于SERL主要依赖环境反馈（如错误信息、页面变化）和任务奖励的二元组合，但未探索更细粒度的内在奖励或语言模型自生成的反馈。未来可研究动态调整反馈权重：根据任务难度或阶段自适应融合多源信号。另一个方向是跨任务泛化，SERL在ALFWorld和WebShop验证，但能否迁移至更复杂的交互环境（如编程或对话）需验证。改进思路包括：引入元学习来自动选择反馈插入位置；将环境反馈建模为概率图，减少对预设阈值的依赖；或对比不同粒度反馈的因果影响，设计更高效的信用分配机制。此外，可结合逆强化学习从成功轨迹中推断隐含偏好，降低对稀疏奖励的敏感性。

### Q6: 总结一下论文的主要内容

本文提出了一种名为SERL的选择性环境加权学习框架，以解决多轮对话智能体在长程信用分配中的挑战。核心问题在于：强化学习的稀疏任务奖励虽能提供可靠优化方向，但难以对长期动作序列进行有效信用分配；而事后蒸馏虽提供密集的令牌级信号，却可能引入特权信息泄露和训练不稳定。SERL方法创新性地利用任务奖励确定更新方向，并仅使用环境条件化的教师信号进行有界的、动作级别的信用调整，从而将环境反馈的作用限定在关键动作上。在ALFWorld和WebShop基准测试中，SERL分别达到90.0%和80.1%的成功率，显著优于现有强化学习和蒸馏方法。主要结论表明，环境反馈不应被视为无限制的辅助监督，有效的智能体强化学习需要对齐反馈来源、插入位置和更新强度三个设计选择，且基于场景的动作相关反馈比更丰富但弱因果的事后反馈更为有效。
