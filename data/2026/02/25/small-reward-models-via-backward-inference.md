---
title: "Small Reward Models via Backward Inference"
authors:
  - "Yike Wang"
  - "Faeze Brahman"
  - "Shangbin Feng"
  - "Teng Xiao"
  - "Hannaneh Hajishirzi"
  - "Yulia Tsvetkov"
date: "2026-02-14"
arxiv_id: "2602.13551"
arxiv_url: "https://arxiv.org/abs/2602.13551"
pdf_url: "https://arxiv.org/pdf/2602.13551v2"
categories:
  - "cs.CL"
tags:
  - "Reward Modeling"
  - "Language Model Alignment"
  - "Backward Inference"
  - "Small Language Models"
  - "Reference-Free Evaluation"
  - "GRPO Training"
relevance_score: 6.5
---

# Small Reward Models via Backward Inference

## 原始摘要

Reward models (RMs) play a central role throughout the language model (LM) pipeline, particularly in non-verifiable domains. However, the dominant LLM-as-a-Judge paradigm relies on the strong reasoning capabilities of large models, while alternative approaches require reference responses or explicit rubrics, limiting flexibility and broader accessibility. In this work, we propose FLIP (FLipped Inference for Prompt reconstruction), a reference-free and rubric-free reward modeling approach that reformulates reward modeling through backward inference: inferring the instruction that would most plausibly produce a given response. The similarity between the inferred and the original instructions is then used as the reward signal. Evaluations across four domains using 13 small language models show that FLIP outperforms LLM-as-a-Judge baselines by an average of 79.6%. Moreover, FLIP substantially improves downstream performance in extrinsic evaluations under test-time scaling via parallel sampling and GRPO training. We further find that FLIP is particularly effective for longer outputs and robust to common forms of reward hacking. By explicitly exploiting the validation-generation gap, FLIP enables reliable reward modeling in downscaled regimes where judgment methods fail. Code available at https://github.com/yikee/FLIP.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在小型语言模型（SLMs，参数≤8B）上构建可靠且高效的奖励模型（RMs）的难题。研究背景是，奖励模型在语言模型的强化学习、偏好优化、重排序和自动评估等流程中至关重要，尤其是在答案难以直接验证的领域。当前的主流方法是“LLM-as-a-Judge”范式，即直接提示一个大语言模型对回答进行评分或判断。然而，这种方法严重依赖大模型强大的推理能力，当应用于计算资源有限的小型模型时，其性能会显著下降（据RewardBench2数据，性能下降41%）。此外，现有替代方法通常需要参考回答或明确的评分细则，这限制了其灵活性和广泛适用性。

现有方法的不足在于：1）基于判断的方法在模型规模缩小时变得不可靠；2）依赖参考或细则的方法成本高且难以获取；3）在优化和评估过程中反复调用大型奖励模型会大幅增加总体计算开销。

本文要解决的核心问题是：如何为小型通用语言模型设计一种无需参考回答、也无需人工制定细则的可靠奖励建模方法。为此，论文提出了FLIP方法，其核心思想是通过“逆向推理”来重构奖励建模任务：给定一个模型生成的回答，让语言模型推断出最可能产生该回答的原始指令（即用户的问题或指令），然后通过计算推断出的指令与原始指令的相似度来作为奖励信号。这种方法利用了小型模型在生成任务上相对较强的能力，规避了其在直接判断任务上的弱点（即“验证-生成差距”），从而在模型规模缩小的场景下实现了比传统判断基线平均提升79.6%的性能，并且在并行采样和GRPO训练等下游任务中也显著提升了效果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：奖励建模和语言模型反演。

在**奖励建模**方面，现有方法主要分为三种范式。首先是“LLM-as-a-Judge”，即依赖大语言模型的推理能力直接评判响应质量，但该方法存在系统性偏见且易受对抗性攻击。其次是**基于参考响应**的方法，例如计算生成输出与标准答案之间的BLEU分数，或利用模型对参考响应的词级概率进行评估。第三类是**基于评估准则**的方法，即将期望的响应质量分解为若干可解释的准则进行打分。然而，这些方法要么需要强大但昂贵的大模型，要么依赖于难以大规模获取的高质量参考答案或精心设计的评估准则。本文提出的FLIP方法无需参考响应或评估准则，仅使用小模型即可实现有效的奖励建模，在资源受限的场景下具有显著优势。

在**语言模型反演**方面，现有研究主要关注从模型输出中恢复隐藏的提示或输入，其动机多出于安全与隐私考虑（如提示泄露风险），或用于合成指令遵循数据。本文是首个将语言模型反演技术应用于奖励建模的工作，通过“逆向推断”生成响应最可能的指令，并以此作为奖励信号，开辟了该技术的一个新颖应用方向。

### Q3: 论文如何解决这个问题？

论文通过提出名为FLIP（FLipped Inference for Prompt reconstruction）的创新方法来解决奖励建模问题。该方法的核心思想是“逆向推理”：即给定一个模型生成的回答，推断最可能产生该回答的原始指令，并将推断出的指令与原始指令的相似度作为奖励信号。这种方法摆脱了传统方法对参考回答或明确评分规则的依赖，实现了无需参考和无规则的奖励建模。

整体框架包含两个主要步骤：首先，利用一个语言模型（作为奖励模型）根据响应 \(y\) 生成一个推断指令 \(x'\)，即 \(x' \sim p_\phi(x' \mid y)\)。其次，通过一个相似度函数 \(s(x, x')\) 计算原始指令 \(x\) 与推断指令 \(x'\) 之间的相似性，并将其定义为标量奖励 \(r\)。在实现中，论文采用F1分数（词级别的精确率和召回率的调和平均数）作为相似度度量，即 \(r = F1(x, x')\)。对于包含系统提示和用户提示的复杂指令，方法会结合用户提示作为上下文，仅推断系统提示并进行比较。

架构设计的关键在于将奖励建模问题转化为一个生成任务，而非传统的判别或评分任务。这通过概率图模型清晰地形式化：奖励 \(r\) 仅依赖于指令对 \((x, x')\)，而推断指令 \(x'\) 仅依赖于响应 \(y\)，即满足条件独立性 \(r \perp y \mid (x, x')\) 和 \(x' \perp x \mid y\)。为了计算效率，论文使用最大后验估计近似推断 \(x'\)，从而简化奖励分布的计算。

创新点主要体现在三个方面：一是提出了“逆向推理”范式，直接利用生成-验证之间的差距作为质量信号；二是该方法特别适用于小规模语言模型，在实验中，使用13个小模型在四个领域上平均超越LLM-as-a-Judge基线79.6%；三是FLIP在长文本输出和对抗奖励攻击方面表现出更强的鲁棒性，并能通过并行采样和GRPO训练有效提升下游任务性能。此外，该方法无需外部参考或人工制定的规则，提高了灵活性和可访问性。

### Q4: 论文做了哪些实验？

论文通过内在和外在评估进行了多组实验。实验设置方面，主要使用了13个小语言模型（SLMs）作为生成式奖励模型，涵盖OLMo2、Llama3、Qwen3、Gemma3和Mistral-v0.3五个模型家族，均采用指令调优变体，并设置512的令牌限制，所有结果均为五次运行的平均值。

数据集和基准测试包括：1）内在评估使用RewardBench2基准，包含1,313个实例，覆盖Focus、Factuality、Precise IF和Math四个子集，任务是从每个提示的四个响应中选择偏好响应；2）测试时扩展（Best-of-N采样）实验在AlpacaEval、Human Interest、MATH和IFEval四个基准上进行，每个基准采样300条测试指令，使用Tulu-3-8B模型生成16个候选补全进行评估；3）强化学习实验使用GRPO训练，从WildChat采样12k英文提示进行训练，并在BBH、GPQA、IFEval、IFBench和Minerva Math五个基准上评估。

对比方法主要为LLM-as-a-Judge的三种变体：Pointwise Rating、Listwise Ranking和Pairwise Ranking。

主要结果如下：在RewardBench2上，FLIP方法平均准确率达到34.5%，显著优于Pointwise Rating（17.3%）、Listwise Ranking（21.0%）和Pairwise Ranking（19.7%），平均提升79.6%。关键数据指标显示，在Focus子集上FLIP平均准确率为59.6%，相比最佳基线提升118.3%；在Factuality、Precise IF和Math子集上分别提升39.5%、29.4%和28.3%。测试时扩展实验中，FLIP在所有基准上均稳定优于基线。GRPO训练中，使用Qwen3-1.7B的FLIP相比LLM-as-a-Judge基线平均提升1.0个绝对点（例如IFEval从78.0%提升至81.3%），部分基准甚至超过经过RLVR的最终策略性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的FLIP方法虽然有效，但仍存在一些局限性和值得深入探索的方向。首先，其核心假设要求回答具备足够长度和细节，这使其难以评估简短或单字回复的质量，未来可研究如何将方法泛化至低信息密度的响应场景。其次，依赖词级F1分数作为相似度度量在跨语言或语义相似但表述不同的指令对比中可能失效，未来可探索更鲁棒的语义相似性评估方法，例如结合小型嵌入模型或经过校准的评判模型。此外，论文提到可能存在不同指令生成相同回答的理论情况，尽管未在数据集中观测到，但在开放域或创意写作等场景中概率可能增加，未来需研究如何量化并处理这种多对一映射的模糊性问题。最后，FLIP目前主要应用于评估阶段，未来可探索将其奖励信号更深度地整合到强化学习训练循环中，或研究如何利用其“逆向推断”机制来主动生成或优化训练指令，从而形成从数据构建到模型对齐的闭环框架。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为FLIP的新型奖励建模方法，旨在解决传统奖励模型在非可验证领域中依赖大型模型、参考回答或明确评分标准的问题。其核心贡献在于通过“逆向推理”重新定义奖励建模任务：即根据给定的模型响应，推断最可能生成该响应的原始指令，并将推断指令与原始指令的相似度作为奖励信号。这种方法无需参考回答或评分细则，提升了灵活性和可访问性。

方法概述上，FLIP利用小型语言模型进行逆向指令推断，通过计算相似度来评估响应质量。实验在四个领域使用13个小模型进行，结果表明FLIP平均优于基于大模型的LLM-as-a-Judge基线79.6%，并在通过并行采样和GRPO训练进行测试时扩展的外在评估中显著提升下游性能。此外，FLIP对长文本输出效果尤佳，且能抵抗常见的奖励攻击。

主要结论是，FLIP通过显式利用验证与生成之间的差距，使得在规模缩小的场景下也能实现可靠的奖励建模，而传统评判方法在此类场景中往往失效。这为资源受限环境下的奖励模型部署提供了高效且稳健的解决方案。
