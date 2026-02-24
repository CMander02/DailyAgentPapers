---
title: "Compositional Planning with Jumpy World Models"
authors:
  - "Jesse Farebrother"
  - "Matteo Pirotta"
  - "Andrea Tirinzoni"
  - "Marc G. Bellemare"
  - "Alessandro Lazaric"
  - "Ahmed Touati"
date: "2026-02-23"
arxiv_id: "2602.19634"
arxiv_url: "https://arxiv.org/abs/2602.19634"
pdf_url: "https://arxiv.org/pdf/2602.19634v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "stat.ML"
tags:
  - "强化学习"
  - "世界模型"
  - "分层规划"
  - "策略组合"
  - "长时程预测"
  - "离线学习"
relevance_score: 9.0
---

# Compositional Planning with Jumpy World Models

## 原始摘要

The ability to plan with temporal abstractions is central to intelligent decision-making. Rather than reasoning over primitive actions, we study agents that compose pre-trained policies as temporally extended actions, enabling solutions to complex tasks that no constituent alone can solve. Such compositional planning remains elusive as compounding errors in long-horizon predictions make it challenging to estimate the visitation distribution induced by sequencing policies. Motivated by the geometric policy composition framework introduced in arXiv:2206.08736, we address these challenges by learning predictive models of multi-step dynamics -- so-called jumpy world models -- that capture state occupancies induced by pre-trained policies across multiple timescales in an off-policy manner. Building on Temporal Difference Flows (arXiv:2503.09817), we enhance these models with a novel consistency objective that aligns predictions across timescales, improving long-horizon predictive accuracy. We further demonstrate how to combine these generative predictions to estimate the value of executing arbitrary sequences of policies over varying timescales. Empirically, we find that compositional planning with jumpy world models significantly improves zero-shot performance across a wide range of base policies on challenging manipulation and navigation tasks, yielding, on average, a 200% relative improvement over planning with primitive actions on long-horizon tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体在复杂长时程任务中进行组合规划（Compositional Planning）的核心挑战。传统强化学习通常基于原子动作进行规划，效率低下且难以应对复杂任务。本文研究如何将预先训练好的策略（如导航、抓取等技能）作为时间抽象的“宏动作”进行组合，以解决单个策略无法完成的复杂任务。核心难题在于：当序列化执行多个策略时，长时程动态预测的误差会不断累积，导致难以准确估计组合策略所诱导的状态访问分布，从而无法可靠地评估不同策略序列的价值。论文的目标是开发一种能够准确预测由预训练策略在多个时间尺度上诱导出的状态占用分布的方法，从而支持零样本（zero-shot）的组合规划，即在无需额外环境交互的情况下，通过组合现有技能解决新任务。

### Q2: 有哪些相关研究？

相关研究主要围绕分层强化学习（HRL）、技能组合和基于模型的规划。1) **分层强化学习**：如选项（Options）框架，旨在学习时间抽象的动作，但通常需要在线学习或专门的技能发现机制。2) **策略组合与几何框架**：本文直接建立在 arXiv:2206.08736 提出的几何策略组合框架之上，该框架将策略视为状态空间上的转移算子，组合即算子的串联。本文的工作是为该理论框架提供可实际学习的高效实现。3) **基于模型的规划与价值估计**：传统方法如基于动态规划或蒙特卡洛树搜索的规划器，在长时程任务中面临组合爆炸和误差累积问题。4) **时间差分流（TD-Flow）**：本文的核心技术基础是 arXiv:2503.09817 提出的 Temporal Difference Flows，这是一种用于学习状态占用分布的生成模型。本文扩展了该方法，引入了跨时间尺度的一致性目标。5) **世界模型**：如 Dreamer 系列，学习环境的动态模型以进行规划，但通常针对原子动作而非预训练的策略技能。本文的“跳跃世界模型”（Jumpy World Models）专门为预测策略执行多步后的状态分布而设计。

### Q3: 论文如何解决这个问题？

论文提出了一个名为“跳跃世界模型”（Jumpy World Models）的框架，用于支持基于预训练策略的组合规划。其核心方法包含三个关键技术：1) **学习多时间尺度的预测模型**：对于一组预训练的基础策略，模型学习预测每个策略在多个固定时间步长（即“跳跃”长度，如1步、4步、16步）后所诱导的状态占用分布。这是以离线、免策略的方式进行的，利用收集到的经验数据来训练生成模型，直接预测从当前状态开始，执行某个策略k步后的状态分布。2) **跨时间尺度的一致性目标**：这是论文的核心创新。为了确保长时程预测的准确性并减少误差累积，作者在 Temporal Difference Flows 的基础上，引入了一个新颖的一致性约束。该约束强制要求：一个策略执行k步的预测分布，应该与先执行该策略j步、再从结果状态执行该策略(k-j)步的复合预测分布相匹配。这通过一个耦合的损失函数来实现，显著提升了长时程预测的连贯性和精度。3) **组合价值估计**：利用学习到的跳跃世界模型，可以生成任意策略序列在不同时间尺度上执行后的状态分布。通过将这些生成的状态分布与任务奖励函数相结合，可以估计执行整个策略序列的期望累积回报，从而在规划时能够评估和比较不同的策略组合方案。整个系统使得智能体能够在零样本情况下，通过搜索和组合现有技能来解决新的长时程任务。

### Q4: 论文做了哪些实验？

实验旨在验证跳跃世界模型在组合规划中的有效性，主要在两个具有挑战性的领域进行：机器人操作（Meta-World）和视觉导航（ViZDoom）。1) **实验设置**：首先预训练一组基础技能策略（例如，接近物体、抓取、放置等）。然后，在完全离线的情况下，使用收集到的转移数据训练跳跃世界模型。测试时，面对新的长时程目标任务（例如“拿起杯子放到架子上”），智能体使用训练好的模型进行规划，通过组合基础策略来零样本解决任务，期间不与真实环境交互。2) **基准对比**：主要对比基线包括：(a) 使用原始原子动作进行规划的标准基于模型的规划器；(b) 使用选项（Options）的规划方法；(c) 不使用跨时间尺度一致性目标的跳跃世界模型变体（即标准的TD-Flow）。3) **主要结果**：实验结果表明，采用跳跃世界模型的组合规划方法在长时程任务上取得了显著优势。在多个任务上，其性能平均比使用原始动作的规划器高出约200%（相对改进）。与不包含一致性目标的变体相比，带有一致性约束的模型在长时程预测准确性上大幅提升，从而带来了更可靠的规划性能。此外，研究还展示了模型能够有效组合不同的技能，解决那些任何单一基础策略都无法完成的任务，验证了组合规划的能力。

### Q5: 有什么可以进一步探索的点？

论文的工作开辟了几个有前景的未来方向：1) **技能自动发现与抽象**：当前方法依赖于一组给定的预训练策略。未来的工作可以探索如何自动发现或学习有用的、可组合的技能基元，使其更适应组合规划。2) **扩展到更复杂的领域**：实验集中在相对结构化的模拟环境。将其扩展到更开放、高维、部分可观测的真实世界场景（如家庭机器人）是一个重大挑战，需要处理视觉输入、不确定性和更复杂的动态。3) **规划效率与搜索**：当前的价值估计方法可能面临策略序列组合爆炸的问题。未来可以集成更高效的搜索算法（如蒙特卡洛树搜索的变体）或学习启发式函数来引导规划。4) **在线适应与微调**：本文专注于零样本规划。一个自然延伸是允许智能体在规划执行过程中，根据少量在线反馈对世界模型或策略组合进行微调，以处理模型误差或分布外情况。5) **理论深化**：虽然基于几何框架，但对一致性目标的理论性质（如收敛性、误差边界）的进一步分析将有助于更好地理解方法的优势和局限。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“跳跃世界模型”的创新方法，用于实现智能体对预训练技能的策略组合规划，以解决复杂的长时程任务。其核心贡献在于：1) 提出学习能够预测预训练策略在多时间尺度上诱导的状态占用分布的生成模型；2) 引入了一个新颖的跨时间尺度一致性目标，显著提升了长时程动态预测的准确性和连贯性，这是实现可靠组合规划的关键；3) 展示了如何利用这些预测模型来估计任意策略序列的价值，从而支持零样本的组合任务求解。实验在机器人操作和导航任务上证明，该方法能大幅超越基于原子动作的规划器，平均实现200%的性能提升，有效解决了单个技能无法完成的复合任务。这项工作为分层强化学习和基于模型的规划提供了一个强大且实用的新工具，将理论上的策略组合框架转化为可操作的算法。
