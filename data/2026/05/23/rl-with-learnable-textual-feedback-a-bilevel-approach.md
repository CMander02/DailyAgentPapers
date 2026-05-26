---
title: "RL with Learnable Textual Feedback: A Bilevel Approach"
authors:
  - "Utsav Singh"
  - "Sidhaarth Sredharan"
  - "Souradip Chakraborty"
  - "Amrit Singh Bedi"
date: "2026-05-23"
arxiv_id: "2605.24547"
arxiv_url: "https://arxiv.org/abs/2605.24547"
pdf_url: "https://arxiv.org/pdf/2605.24547v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "RL with feedback"
  - "bilevel optimization"
  - "critic model"
  - "actor-critic"
  - "reasoning agent"
relevance_score: 9.5
---

# RL with Learnable Textual Feedback: A Bilevel Approach

## 原始摘要

Reinforcement learning with verifiable rewards can improve LLM reasoning, but learning remains sample-inefficient when terminal rewards are sparse. This has motivated a growing line of work on RL with textual feedback, where a critic model generates natural language feedback to guide a reasoning model (the actor), augmenting scalar rewards with richer learning signals. However, existing methods typically treat feedback as fixed or auxiliary, which misses a key property: feedback should not merely be correct, but should improve the policy (actor model) when provided in context. This motivates a paradigm of learnable textual feedback for RL. Yet the learnability and usefulness of feedback depend on the policy's ability to learn from it, making RL with learnable feedback an inherently bilevel problem. We formalize this coupling as a Stackelberg bilevel program and derive Bilevel Natural Language Actor-Critic (Bi-NAC), which jointly trains a critic to generate reward-improving feedback and an actor to exploit it. Across MATH-500, MBPP, and GPQA, Bi-NAC improves sample and parameter efficiency over RL and fixed-critic baselines: our 2B model outperforms the 3B GRPO baseline, achieving 46.6% versus 41.4% on MATH-500, while our 6B model surpasses the 7B GRPO baseline, achieving 49.3% versus 43.6% on GPQA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决强化学习中可验证奖励稀疏导致的样本效率低下问题，尤其是在大语言模型推理任务中。现有方法如GRPO虽然有效，但终端奖励是二元的、稀疏的，部分正确或中间步骤得不到有效反馈，且当所有采样候选都错误时，策略梯度会消失，导致学习停滞。为缓解这一问题，研究者引入了文本反馈机制，用一个评论模型生成自然语言反馈来指导推理模型。然而，现有方法通常将反馈生成视为固定或辅助组件，评论模型要么被冻结，要么用与演员下游表现解耦的目标进行训练。这就导致一个关键缺陷：反馈可能语法正确或局部准确，但缺乏对演员策略的可操作性，无法真正提升策略性能。本文的核心问题正是如何使文本反馈可学习且有效，即生成能实际改善演员下游表现的反馈。这本质上是一个双层耦合优化问题：评论模型的反馈质量取决于演员的学习能力，而演员的改进又依赖收到的反馈。为此，论文提出Bi-NAC框架，将训练建模为Stackelberg双层规划，下层演员优化策略，上层评论通过演员学习动态优化，以生成能最大化演员任务奖励的反馈，从而提升参数和样本效率。

### Q2: 有哪些相关研究？

主要相关工作可分为三类。**方法类**：本文与标准RL方法（如GRPO）不同，后者仅依赖稀疏的终端奖励，而本文提出可学习文本反馈。与固定或独立训练的评论家模型相比（如生成式奖励模型、基于预定义修正指令的方法），本文指出这些方法可能产生正确但无效的反馈，而Bi-NAC通过双层优化将评论家与演员的学习动态耦合，训练评论家生成能提升演员后续表现的反馈。**应用类**：现有工作将文本反馈用于增强语言模型推理，但将反馈生成视为固定或辅助组件。本文则明确将反馈的可学习性作为核心，强调反馈的效用应通过演员学习后的下游表现来评估。**评测类**：在MATH-500、MBPP、GPQA等基准上，本文对比了GRPO和固定评论家基线，显示Bi-NAC在参数和样本效率上的优势。与标准RL和固定反馈基线的主要区别在于，本文从理论上建模了反馈与策略学习的耦合关系，并端到端联合训练演员和评论家，解决了独立训练时反馈不具可操作性的失效模式。

### Q3: 论文如何解决这个问题？

Bi-NAC采用双层Stackelberg博弈框架，将文本反馈生成与策略优化联合建模。整体框架包含两个核心模块：**下层参与者（Actor）** 和 **上层参与者（Critic）**。

Actor是一个LLM策略，其目标是在给定反馈的条件下生成并改进解决方案，以最大化可验证奖励。具体地，Actor先根据问题x生成初始尝试y₀，再基于Critic生成的文本反馈z生成改进响应y₁，并优化参数θ以最大化R(x,y₁)的期望。

Critic同样是一个LLM策略，但其目标并非生成孤立正确的反馈，而是生成能最大程度提升Actor最终任务表现的反馈。Critic的参数φ通过最大化Actor在采纳反馈后的期望奖励来优化。这构成了先导-跟随结构：Critic预判Actor的学习方式而生成反馈，Actor则学习利用反馈提升表现。

关键技术是**双层联合优化**。论文将问题形式化为一个约束优化问题，并通过推导拉格朗日函数得到两层参数的梯度。Critic的梯度更新包含两项：一项鼓励在当前Actor策略下生成高奖励反馈，另一项抑制在最优Actor策略下生成低奖励反馈，从而确保反馈的有效性。Actor的梯度则同时更新初始生成和条件生成（基于反馈）两个阶段的策略。该设计解决了固定反馈或辅助反馈中Actor与Critic不匹配的问题，使反馈能够真正改善策略，避免了稀疏奖励造成的优势坍塌。

### Q4: 论文做了哪些实验？

论文在MATH-500、MBPP、GPQA、AIME 2024、AIME 2025和BeyondAIME六个基准测试上进行了实验，使用LLaMA-3.2（1B、3B、8B）和Qwen-2/Qwen-3模型。对比方法包括Behavioral Cloning (BC)、Hier-NFT、ArCHer、SCoRe、GRPO以及辅助评论家方法（Critique-GRPO、Dr. GRPO）。主要结果：1）在1B/3B/8B规模下，Bi-NAC在MATH、MBPP、GPQA上全面超越所有基线，例如8B规模GPQA上从SCoRe的44.6%提升至56.3%；2）参数效率上，2B Bi-NAC在MATH上以46.6%超越3B GRPO的41.4%，6B Bi-NAC在GPQA上以49.3%超越7B GRPO的43.6%；3）在困难数学基准AIME 2024上，Bi-NAC通过两轮迭代将未训练基线的6.7%提升至13.3%，BeyondAIME上从2.0%提升至4.0%，证明其样本效率和反馈可操作性优势。

### Q5: 有什么可以进一步探索的点？

该工作虽然证明了可学习的文本反馈对策略优化的价值，但仍存在若干可探索的方向。首先，当前的双层优化框架依赖于一个独立的critic模型来生成反馈，这与actor模型是分离的，未来可探索**端到端联合训练**，让actor的隐层表征直接参与反馈生成，从而消除信息瓶颈。其次，反馈的有效性在当前仅通过最终奖励信号评估，忽略了**过程奖励**的潜力，可以设计细粒度的过程反馈机制，对推理的每个步骤而非最终结果进行指导。再者，本文的算法在MATH-500等数学推理任务上表现优异，但数学问题的反馈模式相对结构化，未来应验证其在**开放域对话、代码生成**等更模糊任务中的泛化能力，可能需要引入对抗训练或多样性约束来防止反馈陷入局部最优。最后，从计算效率看，双层训练的代价较高，可尝试**元学习**来初始化解耦的批评者网络，或采用单轮博弈近似来简化优化过程。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型推理中强化学习样本效率低的问题，提出了一种可学习的文本反馈范式。现有方法中的文本反馈通常是固定的或辅助性的，即使反馈内容正确，也可能无法有效提升策略模型（actor）的性能。论文的核心贡献是将可学习反馈下的强化学习形式化为一个Stackelberg双层规划问题，并提出了双层自然语言演员-评论家算法。该方法通过联合训练评论家模型与演员模型，使评论家学会生成能最大化演员模型在接收反馈后最终任务奖励的指导性反馈，从而显式建模了反馈生成与策略学习之间的耦合关系。在MATH-500、MBPP和GPQA基准测试上的实验表明，Bi-NAC在样本和参数效率上均优于GRPO及固定评论家基线方法，例如2B参数模型在MATH-500上达到了46.6%的准确率，超过了3B参数的GRPO基线（41.4%），验证了将评论家训练与演员学习动态对齐以生成可学反馈这一思路的有效性和实践意义。
