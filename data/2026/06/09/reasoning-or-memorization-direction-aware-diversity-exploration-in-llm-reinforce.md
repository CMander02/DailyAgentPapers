---
title: "Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning"
authors:
  - "Jiangnan Xia"
  - "Yucheng Shi"
  - "Yu Yang"
  - "Kishan Panaganti"
  - "Zhenwen Liang"
  - "Ninghao Liu"
date: "2026-06-09"
arxiv_id: "2606.10346"
arxiv_url: "https://arxiv.org/abs/2606.10346"
pdf_url: "https://arxiv.org/pdf/2606.10346v1"
categories:
  - "cs.AI"
tags:
  - "LLM 推理"
  - "探索策略"
  - "强化学习"
  - "GRPO"
  - "奖励塑形"
relevance_score: 7.5
---

# Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning

## 原始摘要

Reinforcement learning has become a key paradigm for eliciting reasoning abilities in large language models, where exploration is crucial for discovering effective solution trajectories. Existing exploration methods typically encourage diversity in semantic or gradient spaces, without distinguishing what drives this diversity. A trajectory may appear novel because it follows a new reasoning process, or because it varies memorized patterns and shortcuts. Rewarding both cases equally may steer exploration toward memorization rather than genuine reasoning improvement. In this paper, we propose DiRL, a Direction-Aware Reinforcement Learning framework that anchors exploration to an internal reasoning-memorization direction of the policy. Specifically, DiRL extracts this direction from model representations, constructs direction-weighted gradient features to characterize rollout updates, and shapes rewards to amplify reasoning-aligned exploration while suppressing memorization-aligned variations. DiRL integrates seamlessly into standard Group Relative Policy Optimization (GRPO). Extensive experiments on mathematical and general reasoning benchmarks demonstrate the effectiveness of DiRL, showing significant improvements over various existing exploration methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大型语言模型（LLM）的强化学习（RL）中，现有探索方法无法区分“推理”与“记忆”导致探索效率低下的核心问题。研究背景是，RL已成为激发LLM推理能力的关键范式，探索（diversity exploration）对于发现有效解法至关重要。然而，现有方法（如在语义空间或梯度空间奖励多样性）存在严重不足：它们不加区分地奖励所有产生新颖轨迹（novel trajectories）的行为。一个轨迹可能因为探索了新的推理路径而新颖，也可能仅仅因为改变了模型记忆中的模式或捷径（memorized patterns and shortcuts）。两种行为都会被同等奖励，导致探索过程偏向于强化记忆而非真正的推理提升（genuine reasoning improvement）。近期研究表明，推理与记忆在LLM内部对应着不同的操作模式（operational modes），在残差流（residual stream）中产生可区分的信号。本文正是利用这一发现，提出Direction-Aware RL（DiRL）框架来解决该问题。其核心是：不再平等对待所有多样性，而是将探索锚定在模型内部推理-记忆的方向（reasoning-memorization direction）上，通过构造方向加权的梯度特征并塑造奖励，选择性地放大与推理对齐的探索，同时抑制与记忆对齐的变异，从而引导RL优化真正提升推理能力，而非仅仅记住模式。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两类。第一类是**面向LLM推理的强化学习探索方法**。现有方法如EVOL-RL在外部语义空间中衡量轨迹新颖性，G²RL则将多样性度量转移到策略自身的梯度空间，直接关联轨迹对模型更新的影响。然而，这些方法不加区分地奖励所有多样性。本文提出的DiRL与之区别在于，它锚定到一条推理-记忆方向，放大促进推理的多样性，同时抑制偏向记忆的多样性。第二类是**LLM推理与记忆的区分研究**。行为研究表明LLM在系统变化或输入扰动下失败，机械分析则发现推理与记忆密集型输入在残差流中沿单一方向线性可分。但这类发现此前主要用于诊断或推理时干预。DiRL的创新在于将这一方向区分融入训练过程，提取推理-记忆方向来引导强化学习，从根本上区分并提升推理能力。

### Q3: 论文如何解决这个问题？

论文提出DiRL（方向感知强化学习框架）解决LLM强化学习中探索偏向记忆化而非真正推理的问题。核心创新在于从模型表征中提取一个“推理-记忆方向”，并基于此方向重塑奖励信号，引导策略朝向推理对齐的探索。

整体框架基于GRPO，但用方向感知探索信号增强了奖励构建。主要模块包括：1) **推理-记忆方向提取**：通过计算推理密集型任务（如多步数学题）和记忆密集型任务（如事实回忆）在最终层隐藏状态的均值差异，得到一个固定方向向量k。2) **方向加权梯度特征**：对于每个轨迹，计算逐令牌的梯度特征phi_t，并用其隐藏状态与k的对齐度（通过sigmoid激活）进行加权求和，得到方向加权梯度特征Phi。这个特征放大了与推理相关的策略更新信号，抑制了记忆相关信号。3) **探索分数**：基于Phi的余弦相似度，将响应分为推理对齐（s>0）和记忆对齐（s≤0）子组。对于推理对齐的响应，探索分数衡量其更新方向相对于组内其他推理响应的新颖性；对于记忆对齐的响应，分数衡量其与推理更新方向的偏离程度。4) **奖励塑造**：将探索分数整合进原始奖励。推理正确且新颖的响应奖励提高，推理错误但新颖的响应惩罚减轻；记忆正确但非推理的响应奖励降低，记忆错误且偏离推理的响应惩罚加重。这样通过奖励的正负强化，引导模型优先探索推理驱动的轨迹，避免陷入记忆化捷径。

### Q4: 论文做了哪些实验？

论文在Qwen3-1.7B-Base和Qwen3-4B-Base上，使用MATH数据集的7.5k问题训练，采用规则验证器提供二元奖励。主要实验在四个数学推理基准上进行：MATH500、AMC、AIME24和AIME25，评估指标包括pass@1、maj@16和pass@16。对比方法包括GRPO（无探索奖励）、Entropy Bonus（熵正则化）、EVOL-RL（语义多样性）和G²RL（梯度特征空间新颖性）。结果显示，DiRL在所有基准和模型大小上均优于基线。例如，在Qwen3-4B上，DiRL在AMC上pass@1达61.0（+8.0），在AIME24上pass@1达19.6（+7.3），在AIME25上pass@1达18.3（+7.9）。在GPQA和MMLU-Pro通用推理基准上，DiRL同样取得最佳性能，如GPQA上pass@1从23.2提升至25.8（Qwen3-1.7B），从35.9提升至39.9（Qwen3-4B）。消融实验验证了各组件贡献，其中No-Sub（移除推理/记忆分离）性能下降最显著。在GSM-Symbolic及其变体上，DiRL在P2（强扰动）上表现突出，如Qwen3-1.7B上pass@1达47（G²RL为46）。方向稳定性分析显示角度漂移仅5.75°（1.7B）和4.86°（4B）。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和未来研究方向，可以进一步探索的点包括：

1. **自动化方向发现机制**：当前方法依赖预先提取的固定推理-记忆方向，未来可研究如何让模型在训练过程中自动发现和更新多个潜在的行为维度，如规划、符号操作和事实回忆等，以适应更复杂的任务。

2. **跨任务泛化性验证**：论文主要在数学推理基准上评估，未来应扩展到更多领域的推理任务（如科学推理、代码生成、常识推理），验证方向感知探索的通用有效性。

3. **多方向奖励塑造**：针对复杂任务中推理行为的多维特性，可以设计更精细的奖励函数，为不同推理维度分配差异化的探索权重，避免单一全局方向可能造成的信息损失。

4. **动态方向调整**：探索在训练过程中根据策略演化动态调整推理-记忆方向的可能性，使探索能自适应地响应模型状态的变化，提升优化效率。

### Q6: 总结一下论文的主要内容

这篇论文提出DiRL框架，旨在解决大语言模型强化学习中现有探索方法无法区分真正推理与记忆模式的问题。现有方法在语义或梯度空间鼓励多样性，但可能将探索导向记忆捷径而非提升推理能力。DiRL通过提取策略内部的推理-记忆方向，构建方向加权的梯度特征来刻画策略更新，并设计奖励机制来强化推理对齐的探索、抑制记忆驱动的变化。该框架可无缝集成到标准GRPO算法中。在数学和通用推理基准上的实验表明，DiRL显著优于现有探索方法，能提高推理性能，增加推理导向的轨迹比例，并在符号扰动下表现出更好的泛化能力。核心贡献在于提出了表示感知的探索方法，引导强化学习向更鲁棒的推理行为发展。
