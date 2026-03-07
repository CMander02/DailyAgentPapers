---
title: "RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization"
authors:
  - "Siwei Zhang"
  - "Yun Xiong"
  - "Xi Chen"
  - "Zi'an Jia"
  - "Renhong Huang"
date: "2026-03-03"
arxiv_id: "2603.03078"
arxiv_url: "https://arxiv.org/abs/2603.03078"
pdf_url: "https://arxiv.org/pdf/2603.03078v1"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Retrieval-Augmented Policy Optimization (RAPO)"
  primary_benchmark: "N/A"
---

# RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization

## 原始摘要

Agentic Reinforcement Learning (Agentic RL) has shown remarkable potential in large language model-based (LLM) agents. These works can empower LLM agents to tackle complex tasks via multi-step, tool-integrated reasoning. However, an inherent limitation of existing Agentic RL methods is their reliance on a pure on-policy paradigm for exploration, restricting exploration to the agent's self-generated outputs and preventing the discovery of new reasoning perspectives for further improvement. While recent efforts incorporate auxiliary off-policy signals to enhance exploration, they typically utilize full off-policy trajectories for trajectory-level policy estimation, overlooking the necessity for the fine-grained, step-level exploratory dynamics within agentic rollout. In this paper, we revisit exploration in Agentic RL and propose Retrieval-Augmented Policy Optimization (RAPO), a novel RL framework that introduces retrieval to explicitly expand exploration during training. To achieve this, we decompose the Agentic RL training process into two phases: (i) Hybrid-policy Agentic Rollout, and (ii) Retrieval-aware Policy Optimization. Specifically, we propose a Hybrid-policy Agentic Rollout strategy, which allows the agents to continuously reason over the retrieved off-policy step-level traces. It dynamically extends the reasoning receptive field of agents, enabling broader exploration conditioned on external behaviors. Subsequently, we introduce the Retrieval-aware Policy Optimization mechanism, which calibrates the policy gradient estimation with retrieval reward and importance shaping, stabilizing training and prioritizing retrieval-illuminating exploration. Extensive experiments show that RAPO achieves an +5.0% average gain on fourteen datasets across three agentic reasoning tasks, while delivering 1.2x faster training efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在“代理强化学习”（Agentic RL）范式下所面临的**探索不足**这一核心问题。研究背景是，LLM智能体通过整合工具进行多步推理，在复杂任务上展现出强大潜力，而Agentic RL（如GRPO等方法）能有效优化智能体的分步推理能力。然而，现有方法存在明显不足：它们主要依赖纯粹的**同策略（on-policy）探索**范式，即智能体仅能从自身反复试错产生的轨迹中学习。这导致探索空间被限制在智能体固有的行为模式内，难以发现全新的、有潜力的推理视角，从而阻碍了性能的进一步提升。

近期有工作尝试引入**异策略（off-policy）信号**来辅助探索，但它们通常将完整的异策略轨迹用于轨迹级别的策略估计。这种方法的不足在于，它**忽视了智能体在推理展开（rollout）过程中所需的细粒度、步骤级别的动态探索**。异策略信息被静态地使用，无法在智能体每一步推理时动态地、显式地拓宽其探索视野。

因此，本文要解决的核心问题是：**能否在Agentic RL的步骤级别推理展开过程中，显式地注入异策略信号，以动态扩展智能体的推理感知范围，从而解锁更广阔的探索空间？** 为此，论文提出了“检索增强的策略优化”（RAPO）框架，通过引入检索机制，在训练期间显式地扩大探索。其核心创新在于将训练分解为两个阶段：1）**混合策略的智能体展开**，使智能体能持续参考检索到的异策略步骤轨迹进行推理，动态扩展其探索的“感受野”；2）**检索感知的策略优化**，通过设计检索奖励和重要性重塑来校准策略梯度估计，以稳定训练并优先考虑那些由检索启发的探索行为，最终实现更优的性能和更高的训练效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕Agentic RL（智能体强化学习）和LLM（大语言模型）智能体的训练方法展开，可分为以下几类：

**1. Agentic RL方法类**：现有Agentic RL方法通常基于GRPO（Group Relative Policy Optimization）类算法，训练智能体使用工具进行多步推理以解决下游任务。然而，这些方法本质上是**纯同策略（on-policy）**的，其探索完全依赖于智能体自身生成的行为轨迹，限制了发现新推理视角的能力。近期工作尝试通过**轨迹重构**（如自适应分支或树搜索）来增强探索，但它们仍属于同策略范式，未能引入外部行为经验。

**2. 策略优化范式类**：根据训练中经验利用方式，LLM的RL训练可分为同策略和异策略（off-policy）方法。同策略方法（如GRPO）使用当前策略生成的轨迹进行更新，训练稳定但探索受限。为改进此问题，**近期研究尝试将异策略信号融入同策略RL**，例如引入辅助LLM或经验回放缓冲区来整合异策略轨迹进行优化。然而，这些方法主要关注**单步推理**，且仅将异策略信号用于**轨迹级别的策略估计**，忽略了智能体多步推演过程中所需的**细粒度、步骤级别的探索动态**。

**3. 熵相关方法类**：熵作为模型不确定性的度量，在LLM后训练中被广泛使用。近期工作利用熵来监控推理状态，并将其融入策略优化以提升性能。在Agentic RL中，熵也被用于实现推演中的自适应分支，或在优化中构建平衡的监督信号，从而增强智能体的工具使用能力。

**本文与这些工作的关系和区别**：本文提出的RAPO框架与上述工作有根本区别。首先，它通过**检索增强的混合策略推演**，允许智能体在训练过程中持续参考检索到的**异策略步骤级轨迹**，从而显式地扩展了推理的感知场，实现了超越自身内在行为的探索。其次，在策略优化阶段，RAPO引入了**检索感知的机制**（包括检索奖励和重要性加权），对策略梯度估计进行校准，优先考虑那些由检索启发的探索。这区别于仅进行轨迹级整合的现有异策略增强方法，保留了步骤级的探索动态，并为RL训练提供了新的视角。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RAPO（检索增强的策略优化）的新型强化学习框架来解决现有Agentic RL方法探索受限的问题。其核心思想是引入检索机制，在训练过程中显式地扩展探索范围，突破仅依赖智能体自身生成输出的纯同策略探索范式。

整体框架包含两个关键阶段：1) 混合策略的智能体推演；2) 检索感知的策略优化。

在混合策略的智能体推演阶段，核心创新在于构建了一个“步骤轨迹缓冲区”，用于存储从离策略智能体收集的细粒度、步骤级别的推理轨迹（以键值对形式：键为截至当前步骤的推理历史，值为该步骤的输出）。这区别于以往使用完整轨迹进行经验回放的方法。在推演过程中，系统会基于当前同策略推理历史动态检索缓冲区中上下文最相似的离策略步骤轨迹，并以50%的概率决定下一步是自主生成还是采纳检索结果。一旦检索被触发，智能体将以此外部轨迹为条件进行后续推理，从而动态扩展其推理感知域，实现步骤级别的探索增强。

在检索感知的策略优化阶段，为了解决引入外部轨迹可能带来的噪声和训练不稳定问题，论文提出了两项关键技术。首先，设计了一种基于熵的检索奖励机制，该奖励同时考量检索质量和时机：通过比较检索前后模型熵值的变化来评估检索是否提供了有益指导（降低不确定性则为正奖励），并利用检索前的高熵值作为时机信号（高熵状态代表强探索性，此时检索更有价值）。其次，引入了检索重要性重塑机制，通过根据检索令牌比例上调重要性采样比率，对稀疏梯度信号进行重新加权，确保模型能更有效地优化那些在离策略条件下生成的关键令牌。

最终，训练目标将检索优势与任务结果优势相结合，并采用裁剪的重要性采样比率和KL散度约束来稳定策略更新。这种方法使智能体能够吸收外部高质量推理片段，在细粒度上拓宽探索空间，同时通过精心设计的奖励和优化机制保障了训练的有效性和稳定性。

### Q4: 论文做了哪些实验？

论文在三个多步智能体推理任务上进行了广泛的实验：计算推理、知识密集型推理和网络智能体推理，共使用了14个数据集。实验设置方面，作者选择了13个基线方法，涵盖工具集成推理方法、离策略学习方法和智能体强化学习方法，并使用Qwen2.5-3B-instruct、Llama3-8B-instruct和Qwen2.5-7B-instruct三种LLM骨干进行评估。对于计算推理和知识密集型推理，训练数据来自Tool-Star，并使用Python和搜索工具；对于网络智能体推理，则使用真实的搜索API。评估指标方面，计算推理使用Pass@1，知识密集型和网络智能体推理使用F1分数。

主要结果显示，RAPO方法在所有任务和数据集上均取得了最佳性能。在计算推理和知识密集型推理的10个数据集上，RAPO在三个骨干模型上的平均性能相比基线（以GRPO为基准）分别提升了6.3%、7.0%和4.6%。在网络智能体推理任务上，RAPO在Qwen2.5-7B-instruct骨干上取得了17.0%的平均得分，相比最佳基线AEPO（15.9%）提升了1.9%。关键数据指标包括：在计算推理任务上，RAPO在AIME2024、AIME2025、MATH500、GSM8K和MATH数据集上的得分分别为24.5%、24.8%、72.0%、87.2%和82.8%（以Qwen2.5-3B-instruct为例）；在知识密集型推理任务上，在WebWalkerQA、HotpotQA、2WikiMultihopQA、Musique和Bamboogle上的得分分别为18.0%、45.8%、48.9%、20.5%和45.9%。此外，效率研究表明，RAPO在训练时间、策略更新时间、产生的令牌数和工具调用次数方面均优于GRPO，实现了1.2倍的训练效率提升。

### Q5: 有什么可以进一步探索的点？

本文提出的RAPO框架虽在探索扩展上取得进展，但仍存在若干局限和可深化的方向。首先，其检索依赖外部轨迹库的质量和覆盖度，若库中缺乏多样或高质量的步骤级轨迹，探索增益可能受限；未来可研究动态构建或增量更新检索库的方法。其次，当前检索主要基于语义相似性，可能忽略逻辑结构或因果关系的匹配；结合程序合成或符号推理来增强检索的精确性是一大方向。此外，框架未充分处理多模态工具调用（如图像处理）的探索，可扩展至跨模态的检索与推理。从方法学看，检索奖励与重要性采样的设计仍较启发式，理论稳定性有待加强；未来可引入不确定性估计或贝叶斯优化来更系统地引导探索。最后，RAPO的训练效率虽有提升，但实时检索开销在复杂任务中可能成为瓶颈，探索轻量级索引或蒸馏技术是实用化的关键。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的智能体强化学习（Agentic RL）中探索受限的问题，提出了一种新颖的检索增强策略优化框架（RAPO）。现有方法主要依赖智能体自身生成的数据进行策略探索，限制了发现新推理视角的能力。RAPO的核心贡献在于通过引入检索机制，显式地扩展训练过程中的探索范围。其方法分为两个阶段：首先，在混合策略智能体推演阶段，智能体能够持续参考检索到的外部细粒度（步骤级）行为轨迹，动态扩展其推理感知域，实现更广泛的、基于外部行为的探索。其次，在检索感知策略优化阶段，通过结合检索奖励和重要性采样来校准策略梯度估计，从而稳定训练并优先考虑那些能带来新启示的探索行为。实验结果表明，RAPO在三个智能体推理任务的十四个数据集上平均性能提升了5.0%，同时训练效率提高了1.2倍。这项工作为增强LLM智能体的探索能力和学习效率提供了有效的新途径。
