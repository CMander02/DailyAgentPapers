---
title: "Improving Parametric Knowledge Access in Reasoning Language Models"
authors:
  - "Melody Ma"
  - "John Hewitt"
date: "2026-02-25"
arxiv_id: "2602.22193"
arxiv_url: "https://arxiv.org/abs/2602.22193"
pdf_url: "https://arxiv.org/pdf/2602.22193v1"
categories:
  - "cs.CL"
tags:
  - "Agent 推理"
  - "知识访问"
  - "强化学习"
  - "语言模型训练"
  - "思维链"
relevance_score: 7.5
---

# Improving Parametric Knowledge Access in Reasoning Language Models

## 原始摘要

We study reasoning for accessing world knowledge stored in a language model's parameters. For example, recalling that Canberra is Australia's capital may benefit from thinking through major cities and the concept of purpose-built capitals. While reasoning language models are trained via reinforcement learning to produce reasoning traces on tasks such as mathematics, they may not reason well for accessing their own world knowledge. We first find that models do not generate their best world knowledge reasoning by default: adding a simple "think step-by-step" cue demonstrates statistically significant improvement in knowledge recall but not math. Motivated by this, we propose training models to reason over their parametric knowledge using world-knowledge question answering as a verifiable reward. After reinforcement learning on TriviaQA (+9.9%), performance also improves on Natural Questions, HotpotQA, SimpleQA, and StrategyQA by 4.2%, 2.1%, 0.6%, and 3.0%, respectively. Reasoning models are under-optimized for parametric knowledge access, but can be easily trained to reason better.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决推理语言模型在访问其自身参数化知识（即存储在模型参数中的世界知识）时效率不足的问题。研究背景是，当前通过可验证奖励的强化学习（RLVR）训练的推理语言模型在数学和编程等需要多步推理的任务上表现出色，但这些模型在访问自身内部知识时，可能不会自动生成有效的推理轨迹。现有方法的不足在于，模型默认的推理机制并未针对知识检索进行优化，导致在闭卷问答等需要回忆参数化知识的任务上表现未达最佳。

本文的核心问题是：如何提升推理语言模型访问其参数化知识的能力？作者发现，即使简单的“逐步思考”提示也能显著改善知识回忆（如在TriviaQA和Natural Questions上提升1-2%），但在数学任务上无效，这表明模型默认未执行最佳的知识访问推理。为此，论文提出使用世界知识问答（如TriviaQA）作为可验证奖励，通过强化学习训练模型，使其学会更好地推理以访问参数化知识。实验显示，经过训练后，模型不仅在训练集上性能提升（如TriviaQA的精确匹配提升9.9%），还能泛化到其他知识问答数据集，证明该方法能有效优化模型的知识访问推理能力。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，**RLVR（强化学习与可验证奖励）** 已被证明在数学、编程等需要多步推理的任务上训练语言模型是有效的。本文直接借鉴了此方法框架，但将其应用领域从通用的推理任务转向了特定的**参数化知识访问**问题。

在**应用类**研究中，相关工作包括：1) **开放书籍问答的强化学习**：已有研究将强化学习应用于需要访问外部知识库的问答系统。本文工作与这些研究的核心区别在于，本文专注于**闭卷式**的知识回忆，即仅利用模型自身参数中存储的知识，而不依赖任何外部检索。2) **语言模型的闭卷知识回忆**：已有工作通过微调等方式来改进模型对参数化知识的访问，但**尚未将强化学习应用于优化推理过程本身**。本文正是填补了这一空白，首次利用基于问答结果的奖励信号，通过强化学习来训练模型生成更好的知识推理链。

在**评测类**方面，本文使用了TriviaQA、Natural Questions等多个标准知识问答数据集进行训练和评估，与相关领域的主流评测方式保持一致，确保了结果的可比性。

### Q3: 论文如何解决这个问题？

论文通过强化学习训练模型，使其更好地利用参数化知识进行推理，以提升知识召回任务的性能。核心方法是设计一个基于答案正确性的可验证奖励函数，通过强化学习优化模型生成推理轨迹和最终答案的过程。

整体框架采用RLVR（Reinforcement Learning with Verifiable Rewards）设置：给定输入问题x，模型首先生成推理轨迹\(\hat{c}\)，然后基于轨迹生成最终答案\(\hat{y}\)。奖励函数仅依赖于最终答案与标准答案的匹配程度，不直接监督推理轨迹，从而鼓励模型自主探索有效的推理路径。奖励函数包含两部分：答案奖励\(r_{answer}\)和格式奖励。答案奖励优先奖励完全匹配（1.0分），部分匹配（答案包含标准答案）给予0.5分，否则0分；格式奖励则鼓励输出使用正确的<answer>标签。

关键技术包括采用GRPO风格的基于重要度采样的策略梯度方法进行优化。对于每个输入，采样K个轨迹计算奖励，并基于组内平均奖励计算优势值，通过策略梯度更新模型参数。训练使用LoRA适配（秩=32）以高效微调，并设置KL惩罚系数防止策略偏离过大。

创新点主要体现在：1）首次系统性地通过强化学习优化语言模型在参数化知识访问中的推理能力，而不仅仅是数学等任务；2）奖励函数设计兼顾答案准确性和输出格式，促进模型生成结构化输出；3）通过消融实验（如Reasoning-SFT和标准SFT基线）验证了强化学习在调整推理过程上的独特贡献，而不仅仅是模仿已有的正确推理链。实验表明，该方法在TriviaQA上提升9.9%，并在多个知识问答数据集上实现稳定提升，证明模型能够被训练得更有效地利用内部知识进行推理。

### Q4: 论文做了哪些实验？

论文主要进行了两部分实验。首先，研究者评估了“逐步思考”提示对知识召回任务的效果。实验设置上，他们使用了四个推理模型：DeepSeek-R1-Distill-Qwen-1.5B、Olmo-3-7B-Think、GPT-OSS-20B和GPT-5.2。在数据集方面，使用TriviaQA和Natural Questions（NQ）作为闭卷问答基准来测试知识召回，并使用MATH数学推理基准作为对比。评估指标为Ex-Recall（提取召回率，对TriviaQA和NQ）和准确率（对MATH）。主要结果显示，添加“逐步思考”提示后，模型在知识召回任务上普遍有提升（例如GPT-OSS-20B在TriviaQA上从60.1%提升至61.2%），但在MATH上提升不显著或略有下降，表明模型在知识召回上的推理能力并未饱和。

其次，研究者基于上述发现，在TriviaQA上对GPT-OSS-20B模型进行了强化学习训练，以改进其参数化知识访问的推理能力。实验设置采用GRPO风格的重要性采样策略梯度方法，奖励函数基于答案正确性（精确匹配得1.0，召回得0.5）和输出格式。对比方法包括基础模型、仅使用正确推理链进行监督微调的Reasoning-SFT基线，以及标准监督微调SFT基线。训练后的模型在多个知识问答数据集上进行了评估。关键数据指标显示，经过RL训练的模型在TriviaQA测试集上的Ex-Recall达到70.0%，相比基础模型（60.1%）显著提升9.9个百分点。在Natural Questions、HotpotQA、SimpleQA和StrategyQA上，性能也分别提升了4.2%、2.1%、0.6%和3.0%（Ex-Recall或EM指标）。结果表明，强化学习训练能有效提升模型在知识召回任务上的推理性能，且效果优于单纯的监督微调。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于，虽然强化学习训练提升了模型在知识问答任务上的表现，但其生成的推理轨迹在人类可解释性方面并未显示出实质性的改进。这表明当前的优化目标可能并未真正引导模型进行更深入、更符合逻辑的“思考”，而仅仅是调整了输出模式以匹配奖励信号。

基于此，未来研究可以从以下几个方向深入探索：
1.  **优化推理轨迹的质量与可解释性**：正如论文所指，未来的强化学习奖励设计应明确鼓励更优的推理过程。可以探索结合认知科学中的“扩散激活”等理论，设计奖励函数来引导模型生成更具逻辑链条、步骤清晰的推理轨迹，而不仅仅是追求最终答案的正确性。
2.  **探索更复杂的知识推理模式**：当前工作主要聚焦于事实性知识检索。未来可以研究模型如何对参数化知识进行更复杂的操作，如对比、整合、溯因推理或处理知识冲突，这在开放域多跳问答（如HotpotQA）和需要策略的问答（如StrategyQA）中尤为重要。
3.  **泛化能力与领域迁移**：虽然论文展示了在TriviaQA上训练能泛化到其他数据集，但这种泛化的稳健性和边界仍需进一步检验。可以研究如何让模型学会一种通用的“知识访问推理”能力，并能快速适应全新的知识领域或问题类型。
4.  **结合外部知识源**：将参数化知识访问与检索增强生成（RAG）技术相结合是一个富有前景的方向。研究模型何时以及如何决定依赖内部参数知识还是检索外部证据，并协调两者进行推理，可能带来性能的进一步提升和透明度的增加。

### Q6: 总结一下论文的主要内容

该论文研究了如何提升推理语言模型访问其参数化世界知识的能力。核心问题是，模型在默认情况下无法最优地利用自身存储的知识进行推理，例如回忆“堪培拉是澳大利亚首都”这类事实时，缺乏有效的内部推理过程。

论文首先通过实验发现，简单的“逐步思考”提示能显著提升知识召回任务的表现，但对数学推理无效，这表明模型在知识访问方面的推理能力未被充分优化。为此，作者提出了一种基于强化学习的方法，以世界知识问答（如TriviaQA）的答案正确性作为可验证奖励，训练模型更好地对参数知识进行推理。

主要结论是，当前推理语言模型在访问参数化知识方面尚未达到最优，但通过针对性的强化学习训练可以有效提升其推理能力。该方法在TriviaQA上性能提升9.9%，并在Natural Questions、HotpotQA等多个闭卷问答数据集上实现泛化性改进，证明了优化知识访问推理的可行性和重要意义。
