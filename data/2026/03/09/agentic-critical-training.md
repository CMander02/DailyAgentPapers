---
title: "Agentic Critical Training"
authors:
  - "Weize Liu"
  - "Minghui Liu"
  - "Sy-Tuyen Ho"
  - "Souradip Chakraborty"
  - "Xiyao Wang"
  - "Furong Huang"
date: "2026-03-09"
arxiv_id: "2603.08706"
arxiv_url: "https://arxiv.org/abs/2603.08706"
pdf_url: "https://arxiv.org/pdf/2603.08706v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Training"
  - "Reinforcement Learning"
  - "Self-Reflection"
  - "Reasoning"
  - "Imitation Learning"
  - "Benchmark Evaluation"
  - "Generalization"
relevance_score: 9.0
---

# Agentic Critical Training

## 原始摘要

Training large language models (LLMs) as autonomous agents often begins with imitation learning, but it only teaches agents what to do without understanding why: agents never contrast successful actions against suboptimal alternatives and thus lack awareness of action quality. Recent approaches attempt to address this by introducing self-reflection supervision derived from contrasts between expert and alternative actions. However, the training paradigm fundamentally remains imitation learning: the model imitates pre-constructed reflection text rather than learning to reason autonomously. We propose Agentic Critical Training (ACT), a reinforcement learning paradigm that trains agents to identify the better action among alternatives. By rewarding whether the model's judgment is correct, ACT drives the model to autonomously develop reasoning about action quality, producing genuine self-reflection rather than imitating it. Across three challenging agent benchmarks, ACT consistently improves agent performance when combined with different post-training methods. It achieves an average improvement of 5.07 points over imitation learning and 4.62 points over reinforcement learning. Compared to approaches that inject reflection capability through knowledge distillation, ACT also demonstrates clear advantages, yielding an average improvement of 2.42 points. Moreover, ACT enables strong out-of-distribution generalization on agentic benchmarks and improves performance on general reasoning benchmarks without any reasoning-specific training data, highlighting the value of our method. These results suggest that ACT is a promising path toward developing more reflective and capable LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主智能体训练时，其核心决策能力发展不充分的问题。研究背景是，当前训练LLM智能体通常从模仿学习开始，即通过监督微调让模型复制专家演示的成功动作序列。然而，现有模仿学习方法存在根本性不足：它只教会智能体“做什么”，而没有让其理解“为什么”这么做。智能体仅接触最优轨迹，缺乏对次优选择的认知，因此无法真正理解动作质量的优劣，也无法发展出对决策背后原因的自主推理能力。近期有方法（如Early Experience）试图通过引入专家动作与替代动作的对比来生成自我反思文本，并让模型模仿这些文本来弥补不足。但这本质上仍是模仿学习——模型只是在模仿预先构建好的反思文字，而非自主学会如何进行推理判断。

因此，本文要解决的核心问题是：如何让LLM智能体不依赖于对固定反思文本的模仿，而是能自主地发展出对动作质量进行批判性评估和推理的内在能力。为此，论文提出了Agentic Critical Training（ACT）这一强化学习范式。其核心思想是直接训练智能体在给定状态下，从一对候选动作（专家动作与模型生成的替代动作）中判断出哪个更好。训练仅通过判断正确与否的奖励信号来驱动，而不提供任何现成的推理文本作为监督。这迫使模型必须内部自主构建推理链（Chain-of-Thought）来支撑其选择，从而产生真正的、内化的自我反思能力，而非对反射文本的表层模仿。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 基于LLM的智能体研究**：这类工作探索如何将大语言模型构建为自主智能体，应用于网页导航、工具使用和多步推理等任务。代表性方法如ReAct（交织推理与行动）和Reflexion（在推理时进行语言自我反思）。**本文与它们的区别在于**：现有方法主要在推理时通过提示来引入反思，而本文（ACT）则通过强化学习在训练阶段将自我反思内化为模型的一种习得能力。

**2. 智能体训练方法**：主流方法是基于专家演示的模仿学习。近期工作如“早期经验”尝试通过让模型生成解释专家行动优势的反思文本来丰富训练信号，但仍属于监督微调，本质是模仿预生成的文本目标。**本文的ACT范式与之根本不同**：它采用强化学习，训练模型去判别哪个行动更好，其监督信号仅为选择是否正确。这迫使模型自主发展出能导致正确选择的推理能力，而非模仿固定文本。

**3. 批判性RL训练**：近期研究利用RL训练批判能力，例如用于构建更强奖励模型（如R1-Reward）或直接通过批判训练改进策略（如LLaVA-Critic-R1）。**本文ACT与它们的区别有两点**：一是ACT专注于多轮次、序列决策的智能体环境，而非单轮对话或代码生成场景；二是ACT训练模型在序列决策过程中判别专家与次优行动，而非批判独立的解决方案。

**4. 智能体强化学习**：这是训练LLM智能体的一个重要范式，专注于解决复杂环境中的多轮、长视野决策问题（如DeepSeek-R1、GRPO、GiGPO等工作）。**本文工作是对该范式的补充和发展**，它表明通过RL训练智能体判别行动优劣，可以作为一个关键的推理训练阶段，进一步提升经模仿学习或RL训练的智能体的性能。

### Q3: 论文如何解决这个问题？

论文通过提出“Agentic Critical Training”（ACT）这一强化学习范式来解决大语言模型作为自主智能体时缺乏对动作质量内在理解的问题。其核心方法是将学习目标从“模仿专家动作”转变为“识别更优动作”，从而驱动模型自主发展对动作质量的判别性推理能力，而非简单地模仿预设的反思文本。

整体框架分为三个阶段。第一阶段是数据构建：给定专家演示轨迹，从每个状态中提取状态-动作对，并从初始策略中采样多个替代动作，与专家动作配对形成对比性训练样本。第二阶段是Agentic Critical Training：模型通过Group Relative Policy Optimization（GRPO）进行训练，其任务是在随机排序呈现的两个候选动作中识别出更好的一个。模型需要生成推理过程并输出选择，奖励仅基于其选择是否正确（即是否与专家动作一致）。这种基于可验证奖励的强化学习机制迫使模型自主发现能导致正确选择的思维链，从而内化对动作质量的理解。第三阶段是RL动作训练：将经过ACT增强的模型在专家轨迹上进一步用GRPO进行直接动作生成的训练，利用其已提升的判别推理基础来实现更有效的策略优化。

主要模块包括：1）对比样本构建模块，负责生成专家动作与模型替代动作的配对；2）GRPO优化器，它通过采样一组响应、计算奖励并使用组间相对优势来更新策略；3）复合奖励函数，包含准确性奖励（匹配专家动作）、可采纳性奖励（输出有效但非专家动作）和格式奖励（确保输出符合规范）。创新点在于：首先，它从根本上将训练范式从模仿学习转变为强化学习，通过正确选择的奖励来驱动真正的自主推理能力的涌现，而非模仿预先构建的反思。其次，ACT专注于训练模型的判别能力（识别优劣），并将其作为提升后续动作生成能力的基础。最后，该方法在多个智能体基准上显著提升了性能，并展现出强大的分布外泛化能力，甚至能提升通用推理任务的性能，这证明了其培养内化反思能力的有效性。

### Q4: 论文做了哪些实验？

论文在三个不同的智能体基准测试上进行了实验：ALFWorld（具身家庭任务）、WebShop（网络购物任务）和ScienceWorld（科学推理任务）。实验设置使用Qwen3-8B模型，所有方法均在相同的专家轨迹数据集上进行训练以确保公平对比。

对比方法包括：无思维链提示、有思维链提示、仅ACT训练、模仿学习、早期经验（自反思）、强化学习，以及ACT与模仿学习或强化学习结合的混合方法。主要结果如下：强化学习整体优于模仿学习；仅ACT训练虽不直接生成动作，但作为预训练阶段能显著提升后续模仿学习或强化学习的性能。具体而言，ACT结合模仿学习比单纯模仿学习平均提升5.07个百分点，ACT结合强化学习比单纯强化学习平均提升4.62个百分点。ACT方法也优于通过知识蒸馏注入反思能力的早期经验方法，平均领先2.42个百分点。

关键数据指标：在ALFWorld任务上，模仿学习的成功率（ID/OOD）为85.71%/82.84%，强化学习为90.71%/84.33%，而结合ACT的强化学习达到92.86%/88.06%。在WebShop上，结合ACT的强化学习成功率最高（33.80%）。在ScienceWorld上，结合ACT的强化学习准确率最高（50.34%）。此外，ACT显著提升了模型在分布外任务上的泛化能力，并在未使用任何推理专用数据的情况下，提升了在MATH-500和GPQA-Diamond通用推理基准上的性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的ACT方法虽然有效，但其探索仍处于早期阶段，存在多个可深入挖掘的方向。首先，其强化学习奖励机制目前仅基于动作选择的二元对错，未来可设计更细粒度的奖励函数，例如考虑推理链的严谨性或效率，以引导模型产生更高质量的反思。其次，ACT依赖于专家与自生成动作的对比，而专家轨迹的质量和覆盖范围可能成为瓶颈；未来可探索如何动态生成或筛选更优的对比样本，甚至引入多智能体竞争环境来自动产生差异化的行为范例。此外，论文发现ACT能提升通用推理能力，但其机理尚不明确；未来可系统研究智能体训练与认知能力迁移之间的关系，例如通过分析注意力模式或知识表征的变化来揭示内在联系。最后，ACT的计算成本较高，如何将其与参数高效微调技术结合，或扩展到更复杂的多轮决策任务中，也是值得探索的实用方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agentic Critical Training（ACT），一种用于训练大型语言模型作为自主智能体的强化学习新范式。核心问题是现有方法（主要是模仿学习）仅让智能体模仿专家行为，却无法理解行动优劣的原因，缺乏真正的反思能力。

ACT的方法是通过对比不同行动，训练智能体自主判断哪个行动更好。其核心贡献在于将训练目标从“模仿反思文本”转变为“学习自主推理行动质量”，通过强化学习奖励模型做出正确判断，从而驱动模型内生地发展出对行动质量的推理能力，产生真正的自我反思。

实验表明，在三个具有挑战性的智能体基准测试中，ACT结合不同后训练方法均能持续提升性能，平均超越模仿学习5.07分，超越传统强化学习4.62分，也优于通过知识蒸馏注入反思能力的方法（平均提升2.42分）。此外，ACT在分布外泛化和通用推理基准上也有出色表现，无需特定训练数据即可提升性能，这凸显了该方法在培养更具反思性和能力更强的LLM智能体方面的潜力和重要意义。
