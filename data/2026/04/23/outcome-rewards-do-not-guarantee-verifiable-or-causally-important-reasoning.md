---
title: "Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning"
authors:
  - "Qinan Yu"
  - "Alexa Tartaglini"
  - "Peter Hase"
  - "Carlos Guestrin"
  - "Christopher Potts"
date: "2026-04-23"
arxiv_id: "2604.22074"
arxiv_url: "https://arxiv.org/abs/2604.22074"
pdf_url: "https://arxiv.org/pdf/2604.22074v1"
categories:
  - "cs.CL"
tags:
  - "LLM推理"
  - "结果奖励"
  - "因果重要性"
  - "推理链评估"
  - "RLVR"
  - "思维链"
  - "后训练"
relevance_score: 8.0
---

# Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning

## 原始摘要

Reinforcement Learning from Verifiable Rewards (RLVR) on chain-of-thought reasoning has become a standard part of language model post-training recipes. A common assumption is that the reasoning chains trained through RLVR reliably represent how a model gets to its answer. In this paper, we develop two metrics for critically examining this assumption: Causal Importance of Reasoning (CIR), which measures the cumulative effect of reasoning tokens on the final answer, and Sufficiency of Reasoning (SR), which measures whether a verifier can arrive at an unambiguous answer based on the reasoning alone. Through experiments with the Qwen2.5 model series and ReasoningGym tasks, we find that: (1) while RLVR does improve task accuracy, it does not reliably improve CIR or SR, calling the role of reasoning in model performance into question; (2) a small amount of SFT before RLVR can be a remedy for low CIR and SR; and (3) CIR and SR can be improved even without SFT by applying auxiliary CIR/SR rewards on top of the outcome-based reward. This joint reward matches the accuracy of RLVR while also leading to causally important and sufficient reasoning. These results show that RLVR does not always lead models to rely on reasoning in the way that is commonly thought, but this issue can be remedied with simple modifications to the post-training procedure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在强化学习从可验证奖励（RLVR）训练语言模型推理链时，一个普遍但未被充分验证的假设：模型生成的推理链既因果重要（即推理步骤真正导致了最终答案）又充分可验证（即仅凭推理链本身，外部验证者就能唯一确定答案）。传统上，RLVR仅基于最终结果（答案）给予奖励，而忽略了推理过程的质量。

现有方法的不足在于，尽管RLVR能提升任务准确率，但模型可能产生“伪推理”——即推理链与最终答案之间缺乏真正的因果联系，或推理步骤模糊、不完整，导致外部验证者无法可靠地复现答案。这种现象使得人们无法信任模型的“思维链”作为其真实决策过程的可靠反映。

本文的核心问题是：能否设计出能够衡量并保证推理链因果重要性与充分可验证性的指标，并据此改进训练流程，使模型在提升准确率的同时，也能生成真正可靠、可解释的推理过程？为此，作者提出了因果重要性（CIR）和充分可验证性（SR）两个新指标，并发现标准RLVR无法可靠地提升这两项指标，但通过结合监督微调或直接引入CIR/SR的辅助奖励，可以有效解决这一问题。

### Q2: 有哪些相关研究？

以下是根据论文相关研究章节整理的主要相关工作类别和本文的对比：

**方法类：**
- **基于可验证奖励的强化学习（RLVR）**：如GRPO及其变体。本文发现，RLVR虽能提升任务准确率，但并**不能可靠提升推理的因果重要性（CIR）与充分性（SR）**，这与普遍假设相悖。
- **忠实性研究（Faithful Reasoning）**：如通过扰动推理链评估因果影响的工作（类似TRACE指标）。本文提出**CIR指标**衡量推理token对最终答案的累积因果效应，与它类似但用于RLVR训练中改进奖励设计，而非仅检测作弊。
- **可验证推理（Verifiable Reasoning）**：如神经符号方法将推理步骤翻译成形式化语句进行逻辑检验。本文提出**SR指标**评估仅凭推理链能否由验证者得出明确答案，并证明可通过辅助奖励联合优化**准确率、忠实性与可验证性**。

**应用类：**
- **数学与代码领域的基准**：如提供推理链细粒度标注的Benchmark，用于评估自动验证者。本文在**ReasoningGym任务**上实验，验证了其指标的有效性及SFT预处理或联合奖励对推理质量的改善作用。

**评测类：**
- **信任度与可解释性评估**：现有评估多关注推理链是否缺失关键信息。本文明确提出CIR和SR两维度，补充了仅依赖结果准确率的评测方式，揭示RLVR训练机制下推理质量可能的虚假性。

总之，本文在现有RLVR和忠实性研究基础上，**揭示了结果奖励的局限性**，并提出可补救的简单训练修改——如加入小规模SFT前训练或联合CIR/SR辅助奖励，以实现更可验证且因果重要的推理链。

### Q3: 论文如何解决这个问题？

论文通过提出并度量两个关键指标——因果重要性（CIR）和推理充分性（SR），系统性地揭示了RLVR在训练推理链时的核心问题。整体框架基于Qwen2.5模型和ReasoningGym任务集，通过分析RLVR训练前后CIR和SR的变化来评估推理质量。

核心方法包括两个互补指标：CIR通过计算截断推理前缀后模型答案分布与完整推理下答案分布之间的Jensen-Shannon散度，量化推理token对最终答案的因果影响；SR则通过一个强验证器（如gpt-4o-mini）比较有无问题条件下从推理链解码出的答案是否一致，衡量外部验证者能否从推理链本身恢复答案。

主要发现揭示了RLVR的局限性：尽管RLVR提升了任务准确率，但并未可靠提升CIR或SR，许多任务中CIR和SR反而下降，表明模型可能在生成推理前就已决定答案，推理链沦为事后解释。

针对这一问题，论文提出两种改进方案：1）在RLVR前使用少量专家推理轨迹进行SFT，能显著提升CIR和SR；2）在RLVR中引入基于CIR或SR的辅助奖励信号，即使不使用专家数据也能在不降低准确率的前提下改善推理的因果重要性和可验证性。这两种方法共同构建了一个在不依赖外部监督的情况下提升推理质量的完整框架。

### Q4: 论文做了哪些实验？

论文主要围绕RLVR训练后推理链的因果重要性（CIR）和可验证性（SR）展开实验。实验设置采用Qwen2.5系列模型（1.5B、3B、7B）及Llama3.2-3B，从ReasoningGym中选取40个任务（排除基础模型准确率过高或为零的任务，优先选择多分类任务），并额外在Math-Hard上验证。对比方法包括：标准RLVR（仅基于答案的规则奖励）、直接回答训练（无推理链）、SFT后接RLVR（使用o3-mini专家轨迹，数量从2到512不等）、以及添加CIR或SR作为辅助奖励的RLVR。

主要结果如下：1）标准RLVR虽能提升任务准确率，但不会可靠地提升CIR或SR——40个任务中19个CIR下降，17个SR下降，且当准确率提升低于50%时CIR和SR更易降低。CIR与准确率提升无显著相关（Spearman ρ=0.17, p=0.31），而SR与准确率提升相关（ρ=0.57, p=0.0001）。2）在低CIR/SR任务上，仅需少量SFT（如64条专家轨迹）即可显著提升CIR（约0.4）和SR（约0.65），并最终提升准确率（约0.5-0.63）。3）添加CIR或SR辅助奖励（权重α=β=1.0）能在保持RLVR同等准确率的同时提升CIR和SR，且两者相互促进，模型不会通过重复问题来“奖励欺骗”（严格评估指标SR--同样提升）。

### Q5: 有什么可以进一步探索的点？

从论文结论出发，未来可探索以下方向：**1) 辅助奖励机制的泛化性**。当前CIR和SR奖励主要依赖规则计算，需探索如何在更复杂的开放式任务（如数学证明、多步推理）中自动化、高效地计算这类指标。**2) 奖励与准确性间的权衡**。论文发现当基础模型准确率极低时，辅助奖励无法提升性能，未来可研究如何动态调整CIR/SR奖励权重，避免牺牲核心任务性能。**3) 推理链的稳定性**。SR-评估已部分缓解奖励破解问题，但模型仍可能学习浅层模式（如重复关键步骤）而非因果链。可引入对抗性奖励或元学习，迫使模型生成更鲁棒的显式推理。**4) 跨模型迁移性**。当前实验基于Qwen2.5系列，需验证结论是否适用于其他架构（如Mamba、Gemini）或不同预训练策略的模型。**5) 可解释性联合优化**。结合CIR/SR与其他细粒度可解释性指标（如对抗鲁棒性、稀疏性），探索多目标强化学习框架，使模型在推理透明性与准确性间取得更优平衡。

### Q6: 总结一下论文的主要内容

这篇论文质疑了基于结果奖励的强化学习（RLVR）训练出的推理链是否真正可信和可验证。核心问题是：RLVR 虽然能提升任务准确率，但无法保证模型生成的推理过程（CoT）具有因果重要性（CIR）和充分可验证性（SR）。作者提出了两个新指标：CIR 衡量推理令牌对最终答案的因果影响程度，SR 衡量仅凭推理过程本身能否让验证者得出唯一答案。通过在 Qwen2.5 系列模型上的实验，主要发现：1）RLVR 训练后，多数任务上的 CIR 和 SR 并未提升，甚至下降，说明模型可能无需真正依赖推理就能答对；2）在 RLVR 前进行少量监督微调（SFT）能显著改善这两个指标；3）将 CIR/SR 奖励直接纳入 RLVR 目标，可以在不牺牲准确率的前提下，同时提升推理的因果重要性和可验证性。该研究的核心贡献在于揭示了结果奖励的局限性，并提出了简单有效的改进方法，对构建可靠、可解释的推理模型具有重要指导意义。
