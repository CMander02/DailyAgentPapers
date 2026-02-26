---
title: "Spurious Rewards: Rethinking Training Signals in RLVR"
authors:
  - "Rulin Shao"
  - "Shuyue Stella Li"
  - "Rui Xin"
  - "Scott Geng"
  - "Yiping Wang"
  - "Sewoong Oh"
  - "Simon Shaolei Du"
  - "Nathan Lambert"
  - "Sewon Min"
  - "Ranjay Krishna"
  - "Yulia Tsvetkov"
  - "Hannaneh Hajishirzi"
  - "Pang Wei Koh"
  - "Luke Zettlemoyer"
date: "2025-06-12"
arxiv_id: "2506.10947"
arxiv_url: "https://arxiv.org/abs/2506.10947"
pdf_url: "https://arxiv.org/pdf/2506.10947v2"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "强化学习"
  - "奖励机制"
  - "数学推理"
  - "语言模型"
  - "RLVR"
  - "GRPO"
  - "模型评估"
  - "训练信号"
relevance_score: 6.5
---

# Spurious Rewards: Rethinking Training Signals in RLVR

## 原始摘要

We show that reinforcement learning with verifiable rewards (RLVR) can elicit strong mathematical reasoning in certain language models even with spurious rewards that have little, no, or even negative correlation with the correct answer. For example, RLVR training with GRPO improves MATH-500 performance for Qwen2.5-Math-7B by 21.4 percentage points using randomly assigned rewards, nearly matching the 29.1-point gain from ground-truth rewards. To explain this counterintuitive observation, we show that GRPO exhibits a clipping bias from the clip term, which can amplify high-prior behaviors learned during pretraining even without informative rewards. As a case study, we identify one such behavior in Qwen2.5-Math models, which we call code reasoning -- reasoning in code without actual code execution; code-reasoning frequency increases from 65 percent to over 90 percent with spurious rewards. However, the presence of such amplifiable behaviors is highly model-dependent. In practice, spurious rewards that are effective for Qwen models often fail to produce gains for other model families, such as Llama3 or OLMo2. Our results highlight the importance of validating RL methods across diverse models rather than relying on a single de facto choice: large gains can arise on Qwen models even from random rewards that do not reflect genuine capability improvements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并深入分析强化学习与可验证奖励（RLVR）方法中一个反直觉的现象：即使使用与正确答案相关性极低、甚至负相关的“虚假奖励”，也能在某些语言模型上显著提升数学推理性能。研究背景是RLVR在提升语言模型推理能力方面已被证明非常有效，但其内在机制尚不明确。现有方法通常默认RLVR的性能增益源于奖励信号对正确行为的引导，但本文发现，在Qwen2.5-Math等模型上，随机分配或基于错误答案的奖励也能带来接近真实奖励的性能提升，这表明当前对RLVR训练动态的理解存在不足，且相关研究过度依赖单一模型家族（如Qwen）作为事实标准，结论可能不具备普适性。

本文要解决的核心问题是：第一，解释为何虚假奖励能在特定模型上引发显著的性能提升，其背后的机制是什么；第二，阐明这种效应高度依赖于基础模型的预训练先验，并非普遍现象；第三，指出当前RLVR研究范式的潜在风险，即仅基于单一模型得出的结论可能具有误导性。为此，论文通过理论分析和案例研究（如识别出Qwen模型中的“代码推理”模式）表明，GRPO等算法中的裁剪偏差会放大模型在预训练阶段已习得的高先验概率行为（即使奖励信号本身不提供信息），从而导致性能的虚假提升。然而，这种可被放大的行为因模型而异，因此在其他模型家族（如Llama3、OLMo2）上，同样的虚假奖励往往无效。最终，论文呼吁未来研究应在多样化模型上验证RL方法，并将虚假奖励作为基准测试的一部分，以更严谨地评估能力的真实提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：无监督强化学习和语言模型的强化学习。

在无监督强化学习方面，相关工作包括：Self-Consistency Preference Optimization (ScPO)，它训练模型在无监督问题上偏好一致的答案；Test-Time Reinforcement Learning (TTRL)，利用对采样输出进行多数投票来估计伪奖励；以及EMPO，通过最小化语义空间中查询的熵来计算奖励，使PPO或GRPO适用于无监督RLVR。这些研究表明，模型内部的一致性可以作为正确性的有效代理。本文与这些工作的关系在于，同样探索了在缺乏明确正确信号下的强化学习，但区别在于，本文系统性地研究了不同训练奖励（包括虚假奖励）对各类模型家族的影响，并揭示了奖励信号与模型预训练先验行为之间的复杂交互。

在语言模型的强化学习方面，RLHF已成为模型对齐的标准技术，而RLVR则在答案确定的任务上被证明有效。这些方法传统上依赖于人类反馈或可验证奖励的准确监督信号。近期研究探索通过AI反馈机制和训练动态分析来减少对人类标注的依赖，支持了“RL主要放大预训练模型中已有行为”的发现。本文与这一脉络紧密相关，并在此基础上进一步指出：即使使用与正确答案相关性极低甚至为负的虚假奖励，RLVR也能在某些模型上引发显著的性能提升，但这种放大效应高度依赖于模型特定的预训练行为（如Qwen模型的代码推理倾向），并非普适。这强调了在评估RL方法时，需要跨不同模型家族进行验证，而非依赖单一模型。

### Q3: 论文如何解决这个问题？

论文通过理论分析和案例研究，揭示了在GRPO（Group Relative Policy Optimization）框架下，即使使用虚假奖励（如随机奖励）也能提升模型数学推理性能的内在机制。核心发现是，GRPO中的裁剪项（clipping term）引入了一种偏差，能够放大模型在预训练阶段已习得的高概率行为，从而产生有效的训练信号，即使奖励本身不包含真实信息。

整体框架基于标准的RLVR（Reinforcement Learning with Verifiable Rewards）流程，但重点剖析了GRPO目标函数中的裁剪操作。关键模块包括策略模型、奖励函数（此处为虚假奖励）以及包含裁剪项的优化目标。创新点在于首次系统论证了裁剪偏差如何在不依赖信息性奖励的情况下驱动学习。

具体而言，GRPO的目标函数包含一个裁剪项，用于限制新策略与旧策略在token概率比（即重要性采样比）上的偏离幅度。当奖励为随机时，理论分析表明，期望梯度与奖励无关，而是取决于概率比相对于裁剪阈值的位置：对于高先验概率的token（即模型原本就倾向于生成的token），其概率比不易触发上界裁剪，从而获得非负的梯度偏差，进一步强化该行为；而对于低概率token，微小的概率增加就容易触发上界裁剪，导致负梯度偏差，从而抑制其生成。这种不对称的偏差效应，使得模型倾向于“利用”而非“探索”，从而巩固并放大了预训练中已有的、与任务成功可能相关的行为模式。

论文以Qwen2.5-Math模型为例进行了案例研究。该模型在预训练中形成了一种“代码推理”行为（即生成Python代码来辅助数学推理，尽管不实际执行）。实验表明，使用随机奖励进行GRPO训练后，模型使用代码推理的频率从65%急剧上升到90%以上，同时数学问题解决准确率显著提升。这是因为代码推理是该模型预训练中已存在的高概率、且与正确率正相关的行为，裁剪偏差将其选择性放大。相反，对于Llama或OLMo等模型家族，由于缺乏这种有效的预训练行为，同样的虚假奖励无法产生性能增益。

因此，论文解决该问题的核心方法是：1）从理论上阐明了GRPO中裁剪项在虚假奖励下产生训练信号的偏差机制；2）通过实证案例（代码推理）表明，该机制的有效性高度依赖于模型预训练阶段所内化的特定行为模式，揭示了RL方法评估需要跨模型验证的重要性。

### Q4: 论文做了哪些实验？

该论文设计了一系列实验，探究在RLVR（带可验证奖励的强化学习）训练中使用虚假奖励信号的效果。实验设置上，主要采用GRPO算法对语言模型进行微调，训练数据来自DeepScaleR数据集，评估时使用默认的聊天模板。研究对比了多种奖励函数：真实答案奖励（作为基线）、多数投票奖励（基于模型采样伪标签）、格式奖励（仅奖励包含特定格式框的响应）、随机奖励（以固定概率随机分配奖励）以及错误奖励（仅奖励与错误标签匹配的答案）。这些奖励均为二元（0或1），旨在检验所需监督信号的最低限度。

实验在多个数学推理基准上评估模型性能，包括MATH-500（报告pass@1准确率）和AMC（报告average@8准确率），并在附录中补充了AIME 2024和2025的结果。主要研究对象是Qwen2.5-Math系列模型，并扩展至通用Qwen模型、Llama3系列以及OLMo2系列模型，以验证效果的普适性。

关键结果显示，对于Qwen2.5-Math-7B模型，即使使用随机奖励，也能在MATH-500上带来21.4个百分点的性能提升，接近真实奖励带来的29.1个百分点增益；格式奖励和错误奖励也分别带来显著提升。然而，这种虚假奖励的有效性高度依赖于模型家族：在Qwen模型上观察到的增益并未推广到Llama3或OLMo2等模型，这些模型在虚假奖励下性能提升很小甚至没有提升。这表明RLVR方法可能并未教授新能力，而是放大了预训练中已存在的潜在行为（如论文中识别的“代码推理”行为），且这种放大效应因模型而异。

### Q5: 有什么可以进一步探索的点？

该论文揭示了RLVR训练中奖励信号可能存在的误导性，但仍有多个方向值得深入探索。首先，研究需系统性地识别和量化不同预训练模型中的“可放大行为”，例如Qwen模型的代码推理倾向，并探究其形成机制与泛化边界。其次，当前实验主要基于数学推理任务，未来可扩展至代码生成、科学问答等复杂领域，检验虚假奖励的放大效应是否具有任务普适性。此外，论文指出GRPO的裁剪偏差是放大效应的关键，未来可设计更稳健的RL算法，通过动态调整裁剪阈值或引入正则化来抑制对预训练偏好的过度依赖。最后，需建立跨模型家族的评估基准，避免结论局限于特定架构，从而推动RL方法在多样化模型上的可靠验证与改进。

### Q6: 总结一下论文的主要内容

该论文探讨了强化学习与可验证奖励（RLVR）中一个反直觉的现象：即使使用与正确答案相关性微弱、无关甚至负相关的虚假奖励信号，也能在某些语言模型中显著提升数学推理能力。研究发现，在Qwen2.5-Math-7B模型上，采用随机分配奖励的GRPO方法可将MATH-500数据集性能提升21.4个百分点，接近使用真实奖励带来的29.1个百分点增益。论文指出，GRPO中的裁剪项会产生“裁剪偏差”，即使奖励信号缺乏信息量，也能放大模型在预训练阶段已习得的高先验行为。作者以“代码推理”（即不实际执行代码的代码形式推理）为例，发现在虚假奖励下该行为频率从65%增至90%以上。然而，这种可被放大的行为高度依赖于模型本身：对Qwen模型有效的虚假奖励，在Llama3或OLMo2等模型家族上往往无效。核心结论在于，RL方法的评估需跨多种模型进行验证，不能仅依赖单一模型，因为随机奖励也可能在特定模型上产生显著的性能增益，但这并不代表真正的能力提升。
