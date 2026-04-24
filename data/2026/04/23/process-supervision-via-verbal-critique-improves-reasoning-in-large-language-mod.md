---
title: "Process Supervision via Verbal Critique Improves Reasoning in Large Language Models"
authors:
  - "Hao-Yuan Chen"
date: "2026-04-23"
arxiv_id: "2604.21611"
arxiv_url: "https://arxiv.org/abs/2604.21611"
pdf_url: "https://arxiv.org/pdf/2604.21611v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "推理时扩展"
  - "过程监督"
  - "语言批评"
  - "自我改进"
  - "大语言模型推理"
relevance_score: 7.5
---

# Process Supervision via Verbal Critique Improves Reasoning in Large Language Models

## 原始摘要

Inference-time scaling for LLM reasoning has focused on three axes: chain depth, sample breadth, and learned step-scorers (PRMs). We introduce a fourth axis, granularity of external verbal supervision, via Verbal Process Supervision (VPS), a training-free framework that uses structured natural-language critique from a stronger supervisor to guide an iterative generate-critique-refine loop up to a round budget R. Across GPQA Diamond, AIME 2025, and LiveCodeBench V6 (covering both closed and open models), VPS yields three key results. First, on GPQA Diamond, GPT-5.4 (High) | GPT-5.4 (Low) reaches 94.9% at R=4, surpassing the 94.1% state of the art without gradient updates. Second, on AIME 2025, VPS enables strong weak-actor rescue, boosting scores from 11.7-26.7% to 63.3-90.0% (up to +63.3 points). Third, at matched compute, VPS outperforms Reflexion by +8.5 to +12.1 points and Self-Consistency@5 by +5.0 pp (GPQA) and +8.3 pp (LiveCodeBench), isolating critique granularity as the key driver. Performance scales with the supervisor-actor capability gap (Pearson r=0.90) and degrades when errors are not linguistically expressible (e.g., code synthesis), motivating hybrid verbal-executable methods. These results establish critique granularity as a new axis of inference-time scaling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大语言模型推理过程中，如何更有效地利用外部监督信号来提升模型性能的问题。当前，推理时计算扩展主要沿着三个维度进行：链深度（增加每条轨迹的token分配）、样本广度（通过多数投票或搜索聚合平行轨迹）和训练步骤评分器（如过程奖励模型PRMs）。然而，现有方法存在不足：链深度和样本广度仅依赖模型自身输出，缺乏外部指导；而PRMs需要大量人工标注步骤正确性标签，训练成本高且扩展性差。更重要的是，现有工作忽略了外部监督的粒度维度——即反馈是从整体结果层面提供，还是在每个推理步骤提供细粒度自然语言批评。

本文提出了一种新型推理时扩展框架——语言过程监督（VPS），通过引入第四维度“外部语言监督的粒度”，在无需训练的情况下，利用更强的监督模型提供结构化自然语言批评，指导一个迭代的“生成-批评-优化”循环。核心要解决的是：能否通过调整监督反馈的粒度（步骤级 vs. 结果级），在不增加链深度、样本量或训练成本的情况下，显著提升大语言模型的推理能力。实验表明，步骤级批评明显优于结果级批评（如Reflexion）和样本聚合方法（如Self-Consistency），验证了批评粒度是推动性能提升的关键变量。

### Q2: 有哪些相关研究？

相关工作可分为三类。首先，**自我修正与口头强化学习类**：Reflexion引入口头强化学习，通过自然语言反馈提供监督信号，但它在完整轨迹上计算口头奖励，导致单次中间错误与策略缺陷共享相同批评压力。VPS通过按步骤索引的批评分解该信号，保留正确子轨迹并定位具体失败点，在相同计算量下取得比Reflexion高8.5-12.1个百分点的提升。ReAct、CRITIC等方法虽也用语言反馈，但多依赖工具使用。VPS还规避了纯自我修正缺乏外部反馈的局限。

第二，**过程监督与推理时扩展类**：“Let's Verify Step by Step”等工作表明过程级信号优于结果监督，后续PRM研究通过自动步骤标签和更强评估器强化了该路线。VPS则用更强LLM的口头批评替代训练好的评分器，消除标注与训练瓶颈。Chain-of-Thought、Self-Consistency、Tree-of-Thoughts、Self-Refine等推理时扩展方法主要关注链深度、样本广度或步骤评分器，VPS在这些轴线之外增加了批评粒度这一新维度，强调结构化外部语言监督的精细度。

第三，**评估与局限类**：实验在GPQA Diamond、AIME 2025、LiveCodeBench上验证，显示VPS与监督-演员能力差距正相关（r=0.90），且当错误难以语言表达（如代码合成）时性能下降，催生了混合口头-可执行方法的必要性。

### Q3: 论文如何解决这个问题？

论文提出了一种名为“言语过程监督”（Verbal Process Supervision, VPS）的训练无关框架，通过引入外部言语监督的粒度作为推理时扩展的第四轴，有效提升了LLM的推理能力。核心方法基于一个迭代的“生成-批评-优化”循环：首先，基础演员模型生成推理轨迹；然后，一个更强的监督者模型（如GPT-5）对轨迹生成结构化自然语言批评，提供步骤级的语义丰富反馈，而非传统标量奖励。演员模型随后基于原始输入、当前轨迹和批评进行条件再生，优化轨迹。这一过程迭代至多R轮，直至收敛或满足停止条件。整体架构包含两个主要组件：演员πθ和监督者C。演员负责生成和优化轨迹，监督者负责评估并提供言语批评。关键技术在于将策略改进转化为条件生成：演员通过监督者的言语批评（即$R_v: \mathcal{T} \times \mathcal{V}^* \to \mathcal{V}^*$）进行条件再生，取代了梯度下降。创新的VPS更新算子F定义为$τ_{r+1} = F(τ_r, C(τ_r, x))$，封装了整个循环。论文创新点包括：将言语批评的粒度作为推理时扩展的新轴；实现无梯度更新的推理时策略改进；通过步骤级言语反馈改善时间信用分配；以及对黑盒模型的广泛适用性。实验表明，VPS在GPQA Diamond、AIME 2025和LiveCodeBench上显著优于现有方法，性能与监督者和演员的能力差距高度相关（皮尔逊r=0.90），但也指出在代码合成等错误无法语言表达的任务中效果受限，提示需要混合言语与执行方法。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：GPQA Diamond（研究生级科学推理，n=198，SOTA 94.1%）、AIME 2025（数学竞赛，n=30，SOTA 95.0%）和LiveCodeBench V6（无污染编程竞赛，SOTA 91.7%）。实验设置包括同家族和跨家族的监督器-执行器对：GPT-5.4 (High) | (Low)、GLM-5.1 | Nemotron-3-Super、Gemma 4 (31B) | GPT-OSS (20B) 和 GPT-OSS (120B) | GPT-OSS (20B)，并消融了轮次R∈{1,2,3,4}。对比方法包括Self-Consistency@5（SC@5，N=5轨迹多数投票）和Reflexion（基于最终答案的结果级反思）。主要结果：在GPQA Diamond上，GPT-5.4 (High) | (Low) 在R=4时达到94.9%，超过SOTA 94.1%和独立执行器92.8%；在AIME 2025上，VPS实现了强大的弱执行器救援，将GPT-5.4 Nano从26.7%提升至90.0%（+63.3点），Gemma 4 | GPT-OSS 20B从11.7%提升至70.0%（+58.3点）。在匹配计算量下，VPS在GPQA上优于Reflexion +8.5点，在AIME上+10.0点，在LiveCodeBench上+12.1点；优于SC@5在GPQA上+5.0点，在LiveCodeBench上+8.3点，在AIME上+1.1点（在n=30的方差内）。监督器-执行器能力差距与VPS增益呈强正相关（Pearson r=0.90）。代码合成场景下VPS增益有限，因错误信号不依赖语言表述。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向主要有四点。首先，当前所有结果为单次运行点估计，关键指标如GPT-5.4在GPQA上+2.1个百分点的优势仍需多种子验证以确认统计显著性。其次，VPS的效果受限于监督者能力：当监督者无法可靠识别演员错误时，批评信号失效，这要求探索如何自动衡量并提升监督者与演员间的能力差距（Pearson r=0.90）。第三，领域边界清晰——在代码合成等错误不可语言表达的任务中VPS增益消失，这催生了混合言语-可执行监督的设想，即引入运行时测试反馈作为批评信号的一部分。此外，轮数缩放的非单调性表明需要引入基于能力差距预测的自适应停止策略，而非固定轮数预算。未来工作还应扩展至多语言场景，并探索将VPS与自我一致性或束搜索等正交技术结合的可能性。

### Q6: 总结一下论文的主要内容

论文提出"言语过程监督"（VPS）框架，将外部言语监督的细粒度作为LLM推理时扩展的新维度。该方法无需训练，通过强监督者的结构化自然语言批评，引导一个迭代的生成-批评-修正循环（预算R轮）。在GPQA Diamond、AIME 2025和LiveCodeBench V6上，VPS取得显著提升：在GPQA上达到94.9%（R=4），超越此前94.1%的最优水平；在AIME 2025上，即使弱模型也能被"救援"，得分从11.7-26.7%跃升至63.3-90.0%。同等计算量下，VPS优于Reflexion（+8.5至+12.1点）和自洽性@5（+5.0至+8.3点），证明批评细粒度是关键驱动力。性能与监督者-执行者能力差距正相关（皮尔森r=0.90），而在错误难以语言表达的任务（如代码合成）中效果下降，提示需结合混合言语-可执行方法。该工作确立了批评细粒度作为推理时扩展的新轴心。
