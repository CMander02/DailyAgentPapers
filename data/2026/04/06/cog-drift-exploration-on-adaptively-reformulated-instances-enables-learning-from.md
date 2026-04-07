---
title: "Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems"
authors:
  - "Justin Chih-Yao Chen"
  - "Archiki Prasad"
  - "Zaid Khan"
  - "Joykirat Singh"
  - "Runchu Tian"
  - "Elias Stengel-Eskin"
  - "Mohit Bansal"
date: "2026-04-06"
arxiv_id: "2604.04767"
arxiv_url: "https://arxiv.org/abs/2604.04767"
pdf_url: "https://arxiv.org/pdf/2604.04767v1"
github_url: "https://github.com/dinobby/Cog-DRIFT"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "强化学习"
  - "推理"
  - "课程学习"
  - "LLM后训练"
  - "任务重构"
  - "探索"
  - "GRPO"
relevance_score: 7.5
---

# Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems

## 原始摘要

Reinforcement learning from verifiable rewards (RLVR) has improved the reasoning abilities of LLMs, yet a fundamental limitation remains: models cannot learn from problems that are too difficult to solve under their current policy, as these yield no meaningful reward signal. We propose a simple yet effective solution based on task reformulation. We transform challenging open-ended problems into cognitively simpler variants -- such as multiple-choice and cloze formats -- that preserve the original answer while reducing the effective search space and providing denser learning signals. These reformulations span a spectrum from discriminative to generative tasks, which we exploit to bootstrap learning: models first learn from structured, easier formats, and this knowledge transfers back to improve performance on the original open-ended problems. Building on this insight, we introduce Cog-DRIFT, a framework that constructs reformulated variants and organizes them into an adaptive curriculum based on difficulty. Training progresses from easier to harder formats, enabling the model to learn from problems that previously yielded zero signal under standard RL post-training. Cog-DRIFT not only improves on the originally unsolvable hard problems (absolute +10.11% for Qwen and +8.64% for Llama) but also generalizes well to other held-out datasets. Across 2 models and 6 reasoning benchmarks, our method consistently outperforms standard GRPO and strong guided-exploration baselines. On average, Cog-DRIFT shows +4.72% (Qwen) and +3.23% (Llama) improvements over the second-best baseline. We further show that Cog-DRIFT improves pass@k at test time, and the curriculum improves sample efficiency. Overall, our results highlight task reformulation and curriculum learning as an effective paradigm for overcoming the exploration barrier in LLM post-training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在基于可验证奖励的强化学习（RLVR）中，面对过于困难的推理问题时无法有效学习的根本性挑战。研究背景是，尽管RLVR（如PPO、GRPO算法）已成为提升LLM推理能力的主流范式，但当模型在当前策略下完全无法解决某个难题（例如pass@64=0）时，由于无法获得任何正向奖励信号，优势函数为零，导致模型参数无法得到有意义的更新，学习过程停滞。这类似于人类学习中的“最近发展区”理论：任务难度远超学习者当前能力时，学习无法发生。

现有方法的不足主要体现在两方面：一是依赖更强的专家模型（如更强大的LLM或人类）来提供引导轨迹或解决方案，但这成本高昂、可扩展性差，且对于能力上限的难题，专家也可能无法解决；二是让模型自我生成提示或简化问题，但这受限于模型自身能力，改进空间有限。这些方法未能系统性地将难题调整到模型可学习的难度范围内。

因此，本文要解决的核心问题是：如何让模型能够从那些原本因难度过高而无法提供任何学习信号（零奖励）的硬推理问题中有效学习。论文提出的解决方案是**任务重构**，即将开放的生成式问题（如开放式问答）转化为认知负荷更低的变体，例如选择题或完形填空。这种重构保留了原问题的答案，但显著约束了输出搜索空间，提供了更密集的学习信号。论文进一步提出了Cog-DRIFT框架，它不仅能自动生成一系列难度各异的任务变体（构成从判别式到生成式的任务谱系），还能根据模型的学习进度（如准确率）自适应地组织这些变体，形成一个从易到难的课程。通过这种“脚手架”式的渐进学习，模型得以先掌握简化格式中的知识，再将其迁移回解决原始开放式问题的能力上，从而突破了传统RL后训练中的探索壁垒，使模型能从原本无法学习的难题中获益。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕“基于可验证奖励的强化学习（RLVR）”和“从难题中学习”两个核心方向展开。

在**RLVR方法类**研究中，已有工作利用数学、代码生成等领域的确定性验证器（如基于最终答案正确性的二元奖励）进行训练。近期研究探讨了RLVR是否能真正发现新推理能力，还是仅通过“分布锐化”放大模型潜在空间中已有的高奖励路径。部分研究认为RLVR主要提升采样效率（pass@1）而非总知识量（pass@k），另一些则主张RL能通过组合现有技能或平衡熵-奖励权衡来培养新能力。

在**从难题中学习**的应用与策略类研究中，针对RLVR中因问题过难导致策略采样无法获得任何奖励信号的挑战，现有方法主要集中于两类：一是通过自我生成提示、批判或部分解决方案来“助推”模型，以降低问题难度并扩展推理边界，例如穿插监督微调（SFT）或训练教师策略生成问答对；二是利用特权信息或离线轨迹在稀疏奖励环境中提供学习信号，例如POPE使用更强模型的离线前缀引导探索。此外，也有研究通过分阶段预热、经验回放和课程设计来实现“顿悟”式学习。

本文提出的Cog-DRIFT框架与上述工作均旨在使难题变得可学习，但采取了根本不同的视角：**以认知负荷为统一框架，通过将问题重构为更简单的变体（如选择题、完形填空），使模型能访问原本无法获得的奖励信号，并结合自适应课程动态调度这些重构问题**。相比之下，先前方法主要依赖额外信号注入（如更强监督、引导探索或丰富训练动态），而本文则通过问题重构和课程学习直接降低认知难度，实证中使训练期间可解决的难题比例大幅提升至18.9%，显著高于先前方法的1-4%范围。

### Q3: 论文如何解决这个问题？

论文通过任务重构和自适应课程学习来解决大语言模型在强化学习后训练中难以从过难问题中学习的问题。其核心方法是：将原本开放式的困难推理问题，转化为一系列认知上更简单、但保留原始答案的变体任务（例如选择题、完形填空），从而提供更密集的学习信号，并构建一个从易到难的自适应课程来引导模型学习。

整体框架（Cog-DRIFT）包含两个关键阶段：
1.  **任务重构与变体生成**：这是方法的基石。对于一个原始的开放式问题（如“解释并回答”），系统自动生成多种结构化、搜索空间更小的变体格式。这些格式构成一个从“判别式”到“生成式”的谱系，例如：
    *   **判别式任务**：如多项选择题、判断题，答案明确，搜索空间最小，提供最直接的正负反馈信号。
    *   **中间混合任务**：如带选项的完形填空，需要部分生成但约束性强。
    *   **生成式任务**：最终目标，即原始的开放式生成问题。
    所有变体都共享最终正确答案，确保学习目标的一致性。

2.  **自适应课程学习**：系统不是固定顺序，而是动态地将这些任务变体组织成一个课程。课程根据模型当前策略下在各个变体任务上的预估成功率（即难度）进行排序。训练开始时，模型主要在与当前能力匹配的、较简单的变体（如选择题）上进行探索和学习，获得有意义的奖励信号。随着训练的进行和模型能力的提升，课程会自适应地引入更接近原始形式的、更难的变体任务。

在技术实现上，模型使用基于验证奖励的强化学习（如GRPO）进行训练。关键创新点在于，奖励信号不仅来自最终答案的正确性验证，而且是在一系列重构的、难度递进的任务环境中获得的。这相当于为探索困难原始问题提供了一个“脚手架”。

**创新点**主要体现在：
*   **任务重构作为探索的使能器**：通过改变问题表述形式来降低即时探索难度，使模型能从原本“信号为零”的难题中开始学习。
*   **利用变体谱系进行知识迁移**：模型在结构化变体中学到的推理模式，可以有效地迁移回提升原始开放式问题的解决能力，实现了“引导式探索”。
*   **自适应课程设计**：根据模型实时表现动态调整训练任务难度，提升了样本效率和学习稳定性。

最终，该方法突破了传统RLVR在难题上的探索瓶颈，使模型能够循序渐进地攻克最初无法解决的硬推理问题，并在泛化性上表现出色。

### Q4: 论文做了哪些实验？

论文实验设置方面，主要评估了Cog-DRIFT框架在Llama3.2-3B-Instruct和Qwen3-4B-Instruct-2507两个模型上的效果。训练数据来自BigMath数据集，通过筛选得到958个初始策略下难以解决（pass@64=0）的“硬问题”构成最终训练集。评估则在六个推理基准测试上进行：BigMathHard、OmniMATH-Hard、AIME 24/25、GPQA Diamond和Date Understanding。

对比方法包括：零样本提示、少样本提示、基于完形填空变体的拒绝采样微调、标准GRPO（使用结果正确性作为奖励），以及两种NuRL变体（分别使用抽象提示和部分步骤作为引导）。主要结果以准确率（pass@1）衡量。关键数据显示，Cog-DRIFT在原本无法解决的BigMathHard问题上取得了显著提升，Qwen和Llama的绝对提升分别达到+10.11%和+8.64%。在六个基准的平均性能上，Cog-DRIFT相比次优基线，Qwen平均提升+4.72%，Llama平均提升+3.23%。此外，实验还表明该方法能提升测试时的pass@k性能（例如在k=128时，在AIME和GPQA上相比基础模型有2-3.3%的提升），并且基于实例的自适应课程学习能提高样本效率。分析还发现，结合多种问题重构格式（如多项选择+完形填空）对实现有效的知识迁移至关重要，而基于pass@k筛选数据时需注意选择偏差，通过GPT-4进行答案过滤可提升数据质量，尤其对Llama模型效果改善明显。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心创新在于通过任务重构和课程学习，让模型能从原本无法解决的难题中学习。但仍存在一些局限和可探索的方向：

首先，论文中的任务重构主要依赖于预定义的格式转换（如多项选择、完形填空），其普适性和自动化程度有限。未来可以探索更动态、自适应的重构方法，例如利用模型自身生成简化变体，或引入强化学习来优化重构策略，使其能根据不同问题类型和模型状态自动调整。

其次，课程学习的难度评估主要基于预设的认知负荷理论，可能未充分考虑模型在训练过程中的实时能力变化。可以进一步研究更精细的难度度量，例如结合模型置信度、探索历史或问题语义复杂度，实现更个性化的课程安排。

此外，该方法目前主要针对数学和逻辑推理任务，在其他需要创造性或长文本生成的复杂问题（如代码生成、故事写作）上的有效性尚未验证。未来可扩展至更多元化的任务领域，并研究如何保持原始任务的开放性和创造性不被简化格式过度约束。

最后，论文强调了从“零信号”问题中学习，但未深入分析知识迁移的具体机制。可结合可解释性工具，探究模型通过简化任务学到了何种表征或推理模式，以及这些如何迁移回原任务，从而为课程设计和重构提供理论指导。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在强化学习后训练中难以从过于困难的推理问题中学习的问题，提出了一种基于任务重构和课程学习的解决方案。核心问题是：当模型在当前策略下完全无法解决某些难题时，由于缺乏有效的奖励信号，标准RL方法（如GRPO）无法进行有效学习。

论文的核心方法是Cog-DRIFT框架。该方法将原本难以解决的开放式问题，自适应地重构为认知负荷更低的变体，例如选择题和完形填空题。这些变体保留了原问题的答案和知识考查点，但通过约束输出空间和提供更密集的学习信号，有效降低了问题难度，使其进入模型的“最近发展区”。关键创新在于，这些重构任务构成了一个从判别式到生成式的难度谱系，并据此构建了一个自适应的课程：模型首先从结构化的、较简单的格式（如选择题）开始学习，获得的知识能够迁移回原始的开放式问题，从而提升其解决能力。训练过程中，系统根据模型在各类变体上的准确率自适应地推进课程，从易到难。

主要结论表明，Cog-DRIFT能有效解锁从原本无法学习的难题中进行学习的能力。在六个推理基准测试和两个模型上的实验显示，该方法在原始难题上的性能显著提升（例如Qwen绝对提升+10.11%），并且能良好地泛化到其他数据集，平均表现优于最强的基线方法。此外，该方法还提升了测试时的pass@k性能，且自适应课程学习提高了样本效率。研究结果强调了任务重构和课程学习是克服LLM后训练中探索障碍的有效范式。
