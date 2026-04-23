---
title: "GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning"
authors:
  - "Jingyi Wang"
  - "Lei Zhu"
  - "Tengjin Weng"
  - "Song-Li Wu"
  - "Haochen Tan"
  - "Jierun Chen"
  - "Chaofan Tao"
  - "Haoli Bai"
  - "Lu Hou"
  - "Lifeng Shang"
  - "Xiao-Ping Zhang"
date: "2026-04-22"
arxiv_id: "2604.20659"
arxiv_url: "https://arxiv.org/abs/2604.20659"
pdf_url: "https://arxiv.org/pdf/2604.20659v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "策略优化"
  - "推理"
  - "过程监督"
  - "数学推理"
  - "通用推理"
  - "模型训练"
relevance_score: 8.0
---

# GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct outcome verification instead of learned reward models. Building on this paradigm, Group Relative Policy Optimization (GRPO) eliminates the need for critic models but suffers from indiscriminate credit assignment for intermediate steps, which limits its ability to identify effective reasoning strategies and incurs overthinking. In this work, we introduce a model-free and verifiable process supervision via probing the model's belief in the correct answer throughout its reasoning trajectory. By segmenting the generation into discrete steps and tracking the conditional probability of the correct answer appended at each segment boundary, we efficiently compute interpretable segment-wise progress measurements to refine GRPO's trajectory-level feedback. This approach enables more targeted and sample-efficient policy updates, while avoiding the need for intermediate supervision derived from costly Monte Carlo rollouts or auxiliary models. Experiments on mathematical and general-domain benchmarks show consistent gains over GRPO across diverse models: up to 2.6-point accuracy improvements and 13.7% reasoning-length reductions on math tasks, and up to 2.4 points and 4% on general-domain tasks, demonstrating strong generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂推理任务中，基于强化学习进行策略优化时，由于中间步骤的信用分配不精确所导致的样本效率低下和策略学习能力受限的问题。

研究背景是，可验证奖励的强化学习通过直接验证最终答案来提供奖励，避免了训练复杂奖励模型带来的问题。在此基础上，群组相对策略优化进一步移除了用于优势估计的评论家模型，简化了训练流程。然而，现有GRPO方法的不足在于，它将轨迹级别的优势均匀地分配给所有中间推理步骤，这种不加区分的信用分配方式无法有效识别哪些推理步骤是真正有益的，哪些是冗余甚至有害的。这导致模型难以学习到高效的推理策略，并可能引发“过度思考”问题，即生成了冗长但低效的推理路径。

因此，本文要解决的核心问题是：如何在无需依赖额外模型或昂贵计算（如蒙特卡洛模拟）的前提下，为GRPO框架提供一种细粒度、可验证的中间过程监督信号，以实现更精准的信用分配。论文提出的解决方案是通过探测模型在其推理轨迹中对正确答案的信念变化，来量化每个推理片段对最终结果的贡献。具体而言，该方法将模型的生成过程分割为离散的推理片段，并在每个片段边界处评估模型在给定当前上下文条件下生成正确答案的条件概率，相邻片段间的概率差值即作为该片段的局部监督信号。这种方法能够提供与模型内部决策流对齐的、可解释的密集反馈，从而引导模型进行更有效和高效的推理。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕强化学习在语言模型推理优化中的方法展开，可分为两类：

**1. 基于可验证奖励的强化学习（RLVR）与GRPO**  
RLVR范式利用基于规则的验证器提供确定性的最终结果奖励，避免了训练有偏的奖励模型。在此框架下，GRPO进一步取消了评论家（critic）模型，通过比较一组生成轨迹的最终结果进行策略优化，实现了轻量高效。但GRPO的局限在于其信用分配是轨迹级别的，对所有中间步骤给予均匀的奖励或惩罚，无法区分推理步骤的有效性，可能导致强化错误步骤或惩罚有潜力的部分逻辑。本文正是在GRPO基础上，通过引入细粒度的过程监督来改进其信用分配机制。

**2. 推理过程监督方法**  
这类工作旨在为长程推理提供更精细的指导，可细分为：
- **基于模型的方法**：如使用PPO训练价值网络来估计中间状态的期望回报，或使用离线训练的过程奖励模型（PRM）。这些方法需要额外的辅助模型，增加了系统复杂性和过拟合风险。
- **无模型的方法**：旨在无需辅助模型提供细粒度反馈。例如S-GRPO通过序列组目标和衰减奖励鼓励更早的高效推理；MRT基于元强化学习，通过计算成功似然的变化来定义“进展”奖励，但其奖励估计可能依赖复杂的蒙特卡洛模拟或多分支生成，影响训练效率。相比之下，本文提出的方法通过探测模型在推理轨迹中对正确答案的信念变化，仅需单次前向传播即可计算出可解释的、分段的进展度量，在保持高效的同时实现了更精准的过程监督。

### Q3: 论文如何解决这个问题？

论文通过引入一种可验证的过程监督框架来增强GRPO，以解决其信用分配稀疏、无法有效指导中间推理步骤的问题。核心方法是利用模型在推理轨迹中对正确答案的置信度变化，生成细粒度的、无需外部模型的监督信号，从而更精准地引导策略更新。

整体框架在GRPO的基础上，增加了三个关键技术模块。首先，**自适应基于熵的分割策略**：该方法利用生成过程中每个token的熵值来识别高不确定性的“决策点”，并以此将完整的推理轨迹分割成多个语义连贯的推理片段。具体而言，选择熵值超过自适应阈值的token作为候选分割点，并通过启发式方法确保每个片段包含大致相同数量的高熵位置，从而实现平衡且有意义的轨迹分割。

其次，**片段级进展估计**：这是方法的核心创新点。对于每个分割好的推理片段，通过探测模型在生成该片段后对预设正确答案的条件概率，来计算该片段的“贡献度”。具体公式为 ΔC_k = π_θ(y* | x, z_≤k) - π_θ(y* | x, z_≤k-1)，即当前片段生成前后模型置信度的变化量。这个值构成了一个密集的、可解释的、且完全基于模型自身信念的过程监督信号向量，量化了每个推理步骤对最终答案的增量贡献。

最后，**混合优势信号融合**：将上述过程监督信号与GRPO原有的、基于最终结果（对错）的稀疏组相对优势信号相结合。最终的混合优势计算公式为 Ã_k^i = A^i + α · ΔC_k，其中A^i是轨迹级的组相对优势，ΔC_k是片段级的进展得分，α是平衡权重。该混合优势信号随后被用于策略梯度更新。这种设计使得策略更新同时受到全局结果反馈和局部过程进展的指导，实现了更精准、更高效的信用分配，避免了GRPO中因稀疏奖励导致的过度思考或无效策略探索问题。整个流程无需昂贵的蒙特卡洛搜索或额外奖励模型，是一种模型无关且可扩展的增强方法。

### Q4: 论文做了哪些实验？

论文在数学和通用领域基准上进行了全面的实验。实验设置方面，使用MATH数据集（7500个问题）进行训练，采用verl框架，每个提示采样8个rollout，温度设为1.0，最大响应长度为3072个token，批大小为512，学习率为1e-6，在8×H800 GPU上训练。评估时在四个数学基准（MATH、AIME 2024、AMC23、OlympiadBench）和通用领域基准（如WebInstruct）上进行，报告4次运行的平均Pass@1，并使用Math-Verify检查答案等价性。

对比方法包括两类：仅使用结果监督的方法（GRPO及其变体DrGRPO、GSPO，以及未微调的BASE模型）和结合过程监督的方法（S-GRPO、基于PRIME风格奖励建模的Eurus-2-7B-PRIME，以及使用Skywork-o1-prm与GRPO微调的对照变体）。主要结果如下：在Qwen2.5-Math-1.5B上，本文方法（GRPO-VPS）相比BASE模型平均准确率提升27.7点（从15.9%到43.6%），平均输出长度减少35.9%；在Qwen2.5-Math-7B上，平均准确率提升31.0点（从21.3%到52.3%），长度减少34.0%。相比原始GRPO，在1.5B模型上准确率提升约2.6点，长度减少约10-11%；在7B模型上准确率提升约1.1点，长度减少类似幅度。在Gemma-2-2B-it上，准确率从6.9%提升至11.7%，同时输出长度相比GRPO大幅降低。通用领域任务上，在Qwen3-1.7B上相比GRPO提升达2.4点准确率，长度减少4%。消融实验表明，结合结果监督与过程监督信号效果最佳（72.0%准确率），仅使用任一种均会下降。过程信号的质量验证显示，其与人类标注的F1分数超过0.75，证实了有效性。此外，自适应分段策略（n=4）在训练效率和性能间取得最优平衡。

### Q5: 有什么可以进一步探索的点？

本文提出的GRPO-VPS方法通过条件概率进行分段信用分配，有效提升了推理效率和准确性，但仍存在以下局限性和可探索方向：首先，该方法依赖于模型对正确答案的条件概率估计，若模型初始置信度存在系统性偏差，可能影响信用分配的准确性，未来可研究更鲁棒的置信度校准方法。其次，分段边界依赖启发式划分，可能无法完全对齐推理的语义单元，可探索基于注意力机制或潜在表示的动态分段策略。此外，当前方法主要针对数学和通用领域推理，对于需要外部知识或复杂规划的领域（如代码生成、科学推理）的泛化能力有待验证。未来可结合课程学习，逐步增加推理复杂度，或引入多任务学习框架以增强适应性。最后，该方法尚未探索与思维链自我修正、递归验证等技术的结合，这可能是进一步提升推理可靠性的方向。

### Q6: 总结一下论文的主要内容

该论文针对强化学习在提升大语言模型推理能力时面临的奖励分配问题，提出了一种结合可验证过程监督的组相对策略优化方法（GRPO-VPS）。核心问题是现有GRPO方法在轨迹级反馈中无法区分中间步骤的贡献，导致信用分配模糊、策略更新低效，并可能引发过度思考。

方法上，GRPO-VPS在无需额外模型或蒙特卡洛搜索的情况下，通过“探测”模型在推理轨迹中对正确答案的信念变化来实现过程监督。具体而言，它将推理过程分割为离散步骤，追踪每个步骤边界处附加正确答案的条件概率，从而计算出可解释的、步骤级的进展度量，用以细化GRPO的轨迹级奖励信号。这使得策略更新更具针对性且样本效率更高。

主要结论显示，该方法在数学和通用领域基准测试中均显著优于原始GRPO。在数学任务上，准确率最高提升2.6个百分点，推理长度减少13.7%；在通用任务上，准确率最高提升2.4个百分点，长度减少4%。这证明了该方法能有效提升推理性能、缩短推理路径，并具有良好的泛化能力。
