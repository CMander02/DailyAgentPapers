---
title: "REVES: REvision and VErification--Augmented Training for Test-Time Scaling"
authors:
  - "Yuanxin Liu"
  - "Ruida Zhou"
  - "Xinyan Zhao"
  - "Amr Sharaf"
  - "Hongzhou Lin"
  - "Arijit Biswas"
  - "Mohammad Ghavamzadeh"
  - "Zhaoran Wang"
  - "Mingyi Hong"
date: "2026-06-17"
arxiv_id: "2606.18910"
arxiv_url: "https://arxiv.org/abs/2606.18910"
pdf_url: "https://arxiv.org/pdf/2606.18910v1"
github_url: "https://github.com/yxliu02/REVES"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM推理增强"
  - "多步推理训练"
  - "测试时缩放"
  - "修正与验证"
  - "强化学习"
  - "代码生成"
  - "数学推理"
relevance_score: 8.0
---

# REVES: REvision and VErification--Augmented Training for Test-Time Scaling

## 原始摘要

Test-time scaling via sequential revision has emerged as a powerful paradigm for enhancing Large Language Model (LLM) reasoning. However, standard post-training methods primarily optimize single-shot objectives, creating a fundamental misalignment with multi-step inference dynamics. While recent work treats this as multi-turn reinforcement learning (RL), conventional approaches optimize over the multi-step trajectories directly, failing to further exploit the high-quality mistakes in intermediate steps that model can learn from correcting them. We propose a two-stage iterative framework that alternates between online data/prompt augmentation and policy optimization. By converting the intermediate steps (``near-miss'' answers) in the successful recovery trajectories into decoupled revision and verification prompts, our approach concentrates training on both effective answer transformation and error identification. This approach enables efficient off-policy data generation and reduces the computational overhead of long-horizon sampling compared to standard multi-turn RL. On LiveCodeBench, using publicly available test cases as feedback, we observe gains of +6.5 points over the RL baseline and +4.0 points over standard multi-turn training. Beyond coding, our approach matches the previously reported SOTA result on circle packing while using the smallest base model (4B) and far fewer rollouts than the much larger evolutionary search systems. Math results under ground-truth verification further confirm improved correction ability. It also generalizes to out-of-distribution constraint-satisfaction puzzles such as n\_queens and mini\_sudoku, where correctness is defined entirely by problem constraints. Code is available at https://github.com/yxliu02/REVES.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在测试时通过顺序修订进行推理时，后训练与多步推理动态之间存在的根本性错配问题。研究背景是，LLM在复杂任务中通常需要多轮修订才能得到正确答案，而现有的测试时缩放（TTS）算法，如顺序修订、树搜索等，都依赖于模型根据反馈进行改进的能力。然而，当前主流的后训练方法——如RLHF、RLVR或GRPO——主要优化单次期望奖励，与多步推理的序列性质不匹配。直接的改进方案是多轮强化学习（RL），但这种方法存在严重不足：它直接在完整的多步轨迹上优化，导致路径依赖的信用分配问题（例如，会给一个“错误-错误-正确”轨迹中所有中间步骤相同的正梯度），无法有效利用中间步骤中产生的高质量错误让模型从中学习修正。核心问题是：需要一种算法，能够绕过轨迹级信用分配的偏差，通过解耦中间步骤的“接近正确”答案，将训练集中在每个中间状态的一次性恢复能力上，从而高效地提升模型的顺序修订能力。

### Q2: 有哪些相关研究？

以下是本文的相关研究，按类别组织：

**方法类**：测试时感知的后训练方法，如优化pass@k以匹配并行采样策略（如best-of-N、多数投票）。本文与之区别在于，其部署的测试时策略（如顺序修订、MCTS变体、Mind Evolution）是修订型算法，依赖先前尝试及其反馈，因此需要不同的训练目标。

**训练类**：训练顺序修订能力的先前方法，包括监督式、偏好式、强化学习及多轮RL方法（整合每轮自然语言或数值反馈）。本文共享增强修订能力的目标，但核心区别在于框架设计：本文聚焦于将训练与修订型推理的测试时目标对齐，而非仅优化单轮或多轮轨迹。

**数据合成与探索类**：弱点驱动数据合成（如SwS，利用强外部教师模型生成针对模型弱点的数据）和引导式探索（如POPE，利用特权提示指导困难问题上的策略探索）。本文与之正交：这些方法优化单轮pass@1，而REVES针对不同的测试时目标（修订式推理），通过将中间“近失”答案转化为解耦的修订和验证提示，实现更高效的离策略数据生成，并减少长程采样的计算开销。

### Q3: 论文如何解决这个问题？

REVES通过一个两阶段迭代框架解决测试时扩展中多步推理与单步训练目标不匹配的问题。核心思想是将成功恢复轨迹中的中间“接近正确”答案转化为独立的修订和验证提示，从而将长程轨迹信用分配转化为短程恢复概率优化。

整体框架分为两个交替进行的阶段。第一阶段（数据增强）：在当前策略πθ下执行序列修订，仅保留在预算K内最终成功的轨迹。对于每条成功轨迹中的每个中间状态z_t = (x, y_{t-1}, f_{t-1})，生成两类数据：(1) 修订提示，要求模型修正上一个错误响应；(2) 验证提示，要求模型判断当前响应是否正确。这些提示与原始RL提示集合并。第二阶段（单轮RL）：在增强后的提示集上使用标准单轮RL训练策略，优化每个状态z下的一步恢复概率V_π(z) = E_{y'~πθ(·|z)}[r*(x, y')]。

关键技术包括：(1) 危险率分解：将JSR目标分解为各状态一步恢复概率的加权和，绕过传统多轮RL中整条轨迹的高方差梯度信号；(2) 离策略数据生成：第一阶段的采样可以异步进行，与第二阶段训练并行，显著降低计算开销；(3) 成功轨迹过滤：只保留成功轨迹中的中间状态作为训练数据，确保每个状态都有明确的恢复目标；(4) 两阶段迭代：每个epoch内先采样增强数据，再训练策略，更新后的策略用于下一epoch的采样，形成良性循环。

该方法的创新点在于：(i) 将长程轨迹中的“错误-正确”对转化为多个独立的短程修订子问题，提供更清晰的局部恢复学习信号；(ii) 在训练中同时引入修订和验证两种任务，使模型在测试时能够自主判断是否停止；(iii) 通过离策略重用和单轮训练实现比标准多轮RL更高的计算效率。

### Q4: 论文做了哪些实验？

论文在多种任务上进行了实验验证。实验设置包括：训练Qwen2.5-7B/3B、Qwen3-4B和DeepSeek-R1-Distill-Qwen-7B模型，使用来自Skywork-OR1-RL-Data的8313条数据（7298条数学+1015条代码）进行强化学习训练。对比方法包括：单轮RL（无修订）、多轮（无明确自我验证）、PAG（带自我验证的多轮）。

在代码任务上，使用LiveCodeBench和CodeContest数据集，通过公开测试用例作为反馈进行顺序修订测试。主要结果：在Qwen-2.5-7B上，REVES在LCB（Aug-Jan）TC-32设置下达到29.5%，比RL基线（23.0%）高6.5点，比多轮（25.5%）高4.0点；CodeContest TC-32下达到16.6%，显著优于RL（11.1%）和多轮（14.3%）。

在数学推理上，使用AIME24/25和MATH500评估。在AIME24上，Qwen-2.5-7B-REVES在Oracle-32下达到45.7%，远高于RL（33.5%）；Oracle-4下25.9%优于RL（21.4%）。在MATH500上，Oracle-32下达到94.7%（RL为85.9%）。

在圆填充任务中，使用Qwen3-4B匹配了之前基于更大模型（Gemini-2.0 Pro/Flash和Qwen3-8B）的最佳结果（2.635983）。此外，在分布外谜题（n皇后和迷你数独）上展示了强泛化能力，且训练好的策略能提升其他测试时策略（如MCTS、Mind Evolution）的性能。

### Q5: 有什么可以进一步探索的点？

REVES的核心局限在于其依赖外部验证信号（如测试用例或ground-truth答案）来生成“near-miss”样本，这在缺乏明确反馈的开放式任务（如创意写作、战略规划）中难以直接迁移。未来可探索利用模型自生成验证器或引入过程奖励模型，以扩展至弱监督场景。此外，当前框架在修正轨迹中仅分离出“接近正确”的答案，但未系统建模错误积累路径——即模型为何会陷入特定错误模式。一个改进方向是引入细粒度的“错误类型分类器”，将失败步骤按逻辑跳跃、数值估算等类型打标签，从而指导针对性的修正策略生成。另外，两阶段迭代中数据增强与策略优化的耦合效率仍有提升空间，可借鉴课程学习思想，按修正难度逐步提高训练样本的复杂度，避免模型过拟合于简单修正场景。实验仅在编码、数学和受限拼图任务验证，其通用性需在更多依赖多步推理的领域（如定理证明、分子设计）中进一步检验。

### Q6: 总结一下论文的主要内容

论文提出REVES框架，旨在解决测试时缩放（TTS）中顺序修订（SR）策略的优化问题。核心挑战在于标准后训练方法（如RLHF、GRPO）仅优化单次输出，与多步推理动态不匹配，且多轮RL存在轨迹级信用分配偏差。REVES通过理论分解证明SR目标可精确表示为各状态一步恢复概率的加权和，从而设计两阶段迭代框架：每轮先用当前策略进行SR滚动并保留成功轨迹，将中间“接近正确”的答案解耦为修订和验证提示，再用单轮RL训练，避免了长序列采样开销。在LiveCodeBench上，REVES比RL基线高6.5分，比多轮训练高4.0分。在圆形装箱任务中，4B参数模型匹配了更大模型的SOTA结果。数学和约束满足谜题（如N皇后）实验也验证了其泛化性。核心贡献在于将TTS形式化为元RL问题，证明改进SR可提升所有使用修订的TTS算法，并提供了高效、无偏的训练方法。
