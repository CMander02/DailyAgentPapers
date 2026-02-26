---
title: "The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics"
authors:
  - "Gregor Bachmann"
  - "Yichen Jiang"
  - "Seyed Mohsen Moosavi Dezfooli"
  - "Moin Nabi"
date: "2026-02-16"
arxiv_id: "2602.14903"
arxiv_url: "https://arxiv.org/abs/2602.14903"
pdf_url: "https://arxiv.org/pdf/2602.14903v2"
categories:
  - "cs.AI"
tags:
  - "推理"
  - "思维链"
  - "大语言模型"
  - "可解释性"
  - "数学推理"
  - "能力转移"
relevance_score: 7.5
---

# The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics

## 原始摘要

Chain-of-thought (CoT) prompting is a de-facto standard technique to elicit reasoning-like responses from large language models (LLMs), allowing them to spell out individual steps before giving a final answer. While the resemblance to human-like reasoning is undeniable, the driving forces underpinning the success of CoT reasoning still remain largely unclear. In this work, we perform an in-depth analysis of CoT traces originating from competition-level mathematics questions, with the aim of better understanding how, and which parts of CoT actually contribute to the final answer. To this end, we introduce the notion of a potential, quantifying how much a given part of CoT increases the likelihood of a correct completion. Upon examination of reasoning traces through the lens of the potential, we identify surprising patterns including (1) its often strong non-monotonicity (due to reasoning tangents), (2) very sharp but sometimes tough to interpret spikes (reasoning insights and jumps) as well as (3) at times lucky guesses, where the model arrives at the correct answer without providing any relevant justifications before. While some of the behaviours of the potential are readily interpretable and align with human intuition (such as insights and tangents), others remain difficult to understand from a human perspective. To further quantify the reliance of LLMs on reasoning insights, we investigate the notion of CoT transferability, where we measure the potential of a weaker model under the partial CoT from another, stronger model. Indeed aligning with our previous results, we find that as little as 20% of partial CoT can ``unlock'' the performance of the weaker model on problems that were previously unsolvable for it, highlighting that a large part of the mechanics underpinning CoT are transferable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在深入探究思维链（CoT）提示技术在大语言模型中成功运作的内在机制，尤其是其如何以及哪些部分真正促成了最终正确答案的生成。研究背景是，CoT已成为从大语言模型中引出类推理响应的标准技术，通过让模型在给出最终答案前逐步阐述推理过程，在数学、编程等多个领域取得了突破性进展。然而，尽管其成功毋庸置疑，且设计上酷似人类推理，但驱动CoT成功的具体原理仍不明确。现有研究存在分歧：一种观点认为模型像人类一样通过逐步计算和回溯探索来获益；另一种观点则认为CoT的内容可能并不反映模型内部的真实计算策略，它更像是一种让模型执行更复杂底层算法的计算机制。

针对现有理解不足，本文的核心问题是：**CoT中的哪些部分（或什么因素）决定了其成功或失败？** 为了系统性地回答这个问题，论文引入了“潜力”这一量化概念，用于衡量给定部分CoT如何增加模型得出正确完成的概率。通过对竞赛级数学问题等任务生成的推理轨迹进行深入分析，作者旨在揭示CoT中哪些步骤（如关键洞察、无关枝节）实际影响了最终结果，并进一步探究不同模型间CoT的“可转移性”，以理解模型是否及如何能从外部提供的推理洞察中受益。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕对思维链（CoT）提示技术的解释、评估和应用展开，可分为以下几类：

**1. CoT的鲁棒性与归因分析**：一系列工作通过人为插入错误或改变符号来操纵CoT，发现模型对此表现出惊人的鲁棒性。另一些研究则采用多种归因策略来识别CoT中的重要部分。这些研究与本文都关注CoT内部机制，但本文引入了“势能”这一量化概念来更精细地度量CoT各部分对最终答案的贡献度。

**2. CoT与模型计算的关系**：有研究发现CoT并不总是反映模型底层的计算过程，因此难以精确定位其中真正有帮助的步骤。甚至有观点认为CoT不应与人类推理类比，或者只是模仿而非真正执行推理。本文通过分析竞赛级数学问题中的CoT轨迹，旨在厘清CoT中哪些部分实际推动了正确解答，与这类质疑性研究的目标部分一致，但提供了更具体的实证分析框架。

**3. 基于部分CoT的条件生成研究**：这是与本文最相似的研究方向。例如，有工作研究神经文本生成中的“分岔词”，另一些则探索通过条件生成寻找“思维锚点”——即帮助模型得出正确答案的CoT部分。这些研究与本文都涉及从部分CoT进行条件生成，但本文更专注于任务相关的“洞见”并探索CoT的失败模式。此外，有研究将部分CoT补全的思想融入强化学习以获得更好的奖励信号，还有工作使用了与本文“势能”类似的指标，但应用于在保持准确性的前提下提前退出长推理链的不同场景。

**4. 与强化学习的联系**：本文对“势能”的后一种定义与演员-评论员模型中的价值函数高度相似，都是在蒙特卡洛方式下衡量给定状态的质量，这体现了本文方法与强化学习领域的交叉。

### Q3: 论文如何解决这个问题？

论文通过引入“势能”这一量化概念，并结合对思维链轨迹的定性分析，来探究思维链提示如何以及哪些部分真正贡献于最终答案。核心方法是定义一个数学指标——势能，它衡量在给定部分思维链前缀的条件下，模型生成正确答案的条件概率。通过大量采样（如N=128次）来估计该势能，从而绘制出思维链生成过程中势能随token增加的变化曲线。

整体框架基于自回归语言模型生成思维链和答案的标准流程。主要模块包括：1) 势能计算模块，用于估计给定思维链前缀下模型答对的概率；2) 轨迹分析模块，对竞争级数学问题生成的思维链进行逐段定性分析，并与势能曲线对齐；3) 可转移性实验模块，测试弱模型在获得强模型的部分思维链后性能的提升。

关键技术在于势能的定义与估计方法，它允许研究者精确量化思维链中每个子步骤对最终正确性的贡献。创新点包括：1) 发现了势能变化中的非单调性（如推理切线导致下降）、尖锐峰值（对应推理洞察或跳跃）以及有时存在的“幸运猜测”；2) 通过势能曲线揭示了模型与人类在感知推理步骤难度上的错位，例如模型可能认为简单的算术步骤反而导致势能大幅跃升；3) 设计了可转移性实验，证明仅提供20%来自强模型的部分思维链，就能显著“解锁”弱模型解决此前无法解决的问题的能力，这表明思维链背后的机制在很大程度上是可迁移的，甚至在不同模型家族之间也有效。

### Q4: 论文做了哪些实验？

论文通过一系列实验深入分析了思维链（CoT）在推理过程中的作用。实验设置上，研究者定义了“潜力”（potential）概念，用于量化CoT的某个部分对最终正确答案生成概率的提升程度，并通过采样（如N=128次）来估计潜力值。主要数据集为竞赛级数学问题，包括AIME-2024、AIME-2025和MATH-500。对比的模型涵盖非推理型（如Qwen2.5-1.5B/7B、Llama-3.1-8B/70B）和推理型（如Qwen3-0.6B/32B）。实验主要结果包括：首先，潜力曲线分析显示，标准CoT常呈现非单调性，其中推理洞察（insights）和跳跃（jumps）会导致潜力骤升，而推理切线（tangents）或缺陷会导致骤降；关键数据指标显示，例如Qwen2.5-7B的推理洞察发生率为62%，推理切线为9.5%，单调性仅42%。其次，研究发现了猜测行为，即模型未依赖推理而直接给出正确答案，这影响了pass@k指标的可靠性。此外，通过优化CoT以最大化潜力，可以构建更单调的推理轨迹。最后，在CoT可转移性实验中，弱模型（如Qwen3-0.6B）在获得强模型（如Qwen3-32B）的部分CoT后，仅需20%的CoT内容即可显著提升在原本无法解决问题上的准确率，表明推理机制在不同模型间具有可转移性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于对“潜力”概念的解释仍不充分，尤其是非单调性和尖锐峰值等现象难以从人类视角完全理解，且研究仅聚焦于数学问题，未验证在其他复杂推理任务（如代码生成、科学推理）中的普适性。未来研究可探索以下方向：首先，将潜力作为细粒度奖励信号融入强化学习框架，以优化推理链的生成过程，实现更精准的信用分配；其次，深入分析“部分CoT迁移”的机制，探究如何通过关键推理片段（如前20%）高效提升弱模型性能，并扩展到多模态或跨领域任务中。此外，可结合可解释性工具（如注意力可视化）解析“推理跳跃”的本质，区分模型是依赖真实逻辑还是隐性模式匹配。最后，需设计更全面的评估指标，量化CoT中冗余信息与关键洞察的平衡，从而构建更高效、可解释的推理架构。

### Q6: 总结一下论文的主要内容

该论文深入探究了思维链（CoT）提示技术在大语言模型（LLMs）中引发类推理行为的内在机制。核心问题是理解CoT中哪些部分以及如何真正贡献于最终答案。为此，研究引入了“潜力”这一量化概念，用于衡量CoT的给定部分如何增加模型得出正确完成的可能性。

通过对竞赛级数学问题产生的CoT轨迹进行基于“潜力”的分析，论文揭示了几个关键且出人意料的模式：潜力的强非单调性（源于推理偏离）、尖锐但有时难以解释的峰值（对应推理洞见和跳跃），以及偶尔出现的“幸运猜测”（模型未提供相关论证却得出正确答案）。这些发现表明CoT的成功并非简单的线性累积。

论文进一步通过“CoT可转移性”实验量化了LLMs对推理洞见的依赖。研究发现，较弱模型仅需利用较强模型的部分CoT（如20%），就能解决其原本无法独立解决的问题，这有力地证明了CoT机制中相当一部分是可转移的、可解释的。核心贡献在于通过“潜力”这一分析工具，深化了对CoT工作机理的理解，识别了其关键组成部分（如洞见和偏离），并为未来研究（如更精细的强化学习奖励设计）提供了新方向。
