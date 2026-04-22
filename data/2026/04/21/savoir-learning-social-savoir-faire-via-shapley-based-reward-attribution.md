---
title: "SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution"
authors:
  - "Xiachong Feng"
  - "Yi Jiang"
  - "Xiaocheng Feng"
  - "Deyi Yin"
  - "Libo Qin"
  - "Yangfan Ye"
  - "Lei Huang"
  - "Weitao Ma"
  - "Yuxuan Gu"
  - "Chonghan Qin"
  - "Bing Qin"
  - "Lingpeng Kong"
date: "2026-04-21"
arxiv_id: "2604.18982"
arxiv_url: "https://arxiv.org/abs/2604.18982"
pdf_url: "https://arxiv.org/pdf/2604.18982v1"
categories:
  - "cs.AI"
tags:
  - "Social Agent"
  - "Reinforcement Learning"
  - "Reward Attribution"
  - "Shapley Value"
  - "Multi-turn Dialogue"
  - "SOTOPIA Benchmark"
relevance_score: 8.0
---

# SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution

## 原始摘要

Social intelligence, the ability to navigate complex interpersonal interactions, presents a fundamental challenge for language agents. Training such agents via reinforcement learning requires solving the credit assignment problem: determining how individual utterances contribute to multi-turn dialogue outcomes. Existing approaches directly employ language models to distribute episode-level rewards, yielding attributions that are retrospective and lack theoretical grounding. We propose SAVOIR (ShApley Value fOr SocIal RL), a novel principled framework grounded in cooperative game theory. Our approach combines two complementary principles: expected utility shifts evaluation from retrospective attribution to prospective valuation, capturing an utterance's strategic potential for enabling favorable future trajectories; Shapley values ensure fair credit distribution with axiomatic guarantees of efficiency, symmetry, and marginality. Experiments on the SOTOPIA benchmark demonstrate that SAVOIR achieves new state-of-the-art performance across all evaluation settings, with our 7B model matching or exceeding proprietary models including GPT-4o and Claude-3.5-Sonnet. Notably, even large reasoning models consistently underperform, suggesting social intelligence requires qualitatively different capabilities than analytical reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决提升语言智能体社会智能（Social Intelligence）时所面临的核心挑战——如何在多轮复杂人际对话中进行有效的信用分配（Credit Assignment）。研究背景是，随着大语言模型被越来越多地应用于需要谈判、协作和说服的交互场景，其社会智能变得至关重要。然而，社会交互具有多轮性、目标竞争性以及个体话语对长期结果贡献微妙等特点，使得通过强化学习训练此类智能体变得异常困难。

现有方法，如Sotopia-RL，虽然尝试将回合级别的反馈细化为话语级别的奖励，但存在两个根本性不足。首先，其信用分配机制缺乏理论依据，仅通过直接提示大语言模型进行启发式奖励分配，无法保证公平性或准确性。其次，更关键的是，该方法进行的是**回顾性归因**，即根据已观察到的最终结果来评估话语的贡献，这忽略了社会智能行为中常见的一种情况：某些话语的即时贡献看似微小，但其**战略定位**却能开启后续的成功可能。

因此，本文要解决的核心问题是：如何建立一个**有理论根基的、前瞻性的**信用分配框架，以更准确地评估和奖励话语在对话中的**战略价值**，从而更有效地训练出具有高级社会智能的语言智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升语言智能体社会智能的方法，可分为以下几类：

**1. 基于强化学习的社会智能训练方法**：这是本文最直接相关的领域。代表性工作包括 SOTOPIA-π，它结合了行为克隆和在过滤交互数据上的自我强化。更近期的 Sotopia-RL 通过直接提示大语言模型（LLM）将回合级反馈细化为话语级奖励，实现了性能提升。本文提出的 SAVOIR 框架与这些工作同属利用强化学习训练社会智能体的范式，但核心区别在于其**信用分配机制**。本文指出，Sotopia-RL 等方法缺乏理论依据，其LLM奖励模型是启发式、回顾性的分配，仅基于已观察到的结果评估话语贡献。而 SAVOIR 引入了博弈论中的期望效用和沙普利值，将评估转变为**前瞻性的战略价值评估**，并提供了公平、具有公理保证的信用分配。

**2. 社会智能评测基准**：本文的实验基于 SOTOPIA 基准。这类基准为评估智能体在复杂社交互动（如谈判、协作）中的表现提供了标准测试环境。本文的工作是在此基准上验证新方法的有效性，并与之进行性能比较。

**3. 大型语言模型与推理模型的应用**：研究中也对比了包括 GPT-4o、Claude-3.5-Sonnet 在内的专有 LLM，以及 OpenAI-o1、Gemini-2.5-Pro 等大型推理模型。这些模型代表了当前最先进的通用或推理能力。本文发现，尽管这些模型分析能力强，但在社会智能任务上 consistently 表现不佳，这凸显了社会智能所需能力（如战略前瞻、信用公平分配）与纯分析推理能力的差异性，从而反衬出 SAVOIR 这类专门化方法的价值。

综上，本文在现有社会智能强化学习方法的基础上，针对其信用分配的理论缺陷和回顾性局限，提出了一个基于博弈论原理的创新框架，并在标准评测中证明了其优越性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SAVOIR（ShApley Value fOr SocIal RL）的新型、基于原则的框架来解决社交对话中的信用分配问题。该框架将强化学习中的奖励建模构建为一个合作博弈，并融合了博弈论中的两个核心概念：期望效用和沙普利值。

整体框架分为三个主要阶段。首先，对目标代理在对话中的一系列话语进行联盟采样。其次，通过未来轨迹的蒙特卡洛模拟（Rollout）来评估每个联盟的期望效用。最后，利用沙普利值计算，公平地将总价值分配给各个话语。

核心方法包含几个关键模块。一是**期望效用价值函数**，它评估一个话语联盟的战略价值。其计算方式是从该联盟重构的对话历史出发，使用代理策略和伙伴策略进行多次完整的未来对话模拟，并对这些模拟轨迹的效用（基于SOTOPIA评估框架的多维度加权得分）取平均。这实现了从回顾性评估到前瞻性评估的转变，捕捉话语开启有利未来轨迹的潜力。二是**沙普利值信用分配**，它基于合作博弈论，通过计算一个话语在所有可能联盟顺序中的平均边际贡献来分配奖励。这确保了分配的公平性，并满足效率性、对称性、零贡献者等公理性质。三是**高效计算技术**，由于直接计算沙普利值需要评估所有2^n个子集，计算成本高昂，因此论文采用KernelSHAP算法，将问题转化为加权线性回归，并通过智能联盟采样策略（优先采样极端大小的联盟，如仅包含单个话语或几乎包含所有话语的联盟）来高效逼近沙普利值。

主要的创新点在于：1）理论基础的创新，首次将沙普利值这一具有公理保证的公平分配概念系统性地引入社交语言代理的奖励建模中；2）评估视角的创新，结合期望效用理论，从传统的回顾性归因转向前瞻性的战略潜力评估；3）框架的有效性，在SOTOPIA基准测试中取得了最先进的性能，其7B模型甚至能匹配或超越GPT-4o等大型专有模型，证明了该方法在培养社交智能方面的独特优势。

### Q4: 论文做了哪些实验？

实验在SOTOPIA基准上进行，包括SOTOPIA-Hard（14个复杂场景）和SOTOPIA-All（90个场景）。评估设置分为两种：智能体与自身对弈的Self-Play，以及智能体与GPT-4o交互以测试泛化能力的GPT-4o-as-Partner。主要评估指标为Goal（0-10分）和Avg。对比方法包括三类：专有LLM（如GPT-4o、Claude-3.5-Sonnet）、大型推理模型（如OpenAI-o1、Gemini-2.5-Pro）以及社交智能方法（如PPDPP、Sotopia-RL）。实验基于Qwen2.5-7B-Instruct模型，采用两阶段训练：先在GPT-4o自对弈数据上进行SFT，再使用GRPO和SAVOIR奖励模型进行在线RL。

主要结果显示，SAVOIR在所有设置中均达到最先进性能。在GPT-4o作为伙伴的SOTOPIA-Hard上，Goal得分为7.18，比Sotopia-RL提升7.5%；在Self-Play的SOTOPIA-All上，Goal得分为8.43，超过GPT-4o（8.19）和Claude-3.5-Sonnet（8.29）。尽管SAVOIR仅为7B模型，但其表现匹配或超越了专有LLM。大型推理模型普遍表现不佳，例如o3-mini的Goal得分仅为5.14，远低于SAVOIR的7.93（差距54.3%）。消融实验表明，预期效用（EU）和Shapley值均独立贡献性能提升：EU-only比基线提升3.1%，Shapley-only提升4.2%，两者结合实现7.5%的完整提升。数据规模分析显示，训练数据从2K增至7.5K时，Goal得分从6.23提升至7.18（+15.2%）。人工评估进一步验证了SAVOIR的优势，在响应策略性上得分为4.06（基线为3.41），且奖励模型质量在公平性和未来基础识别方面均获显著偏好（偏好率分别为67.1%和62.9%）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于SOTOPIA基准，该环境虽能模拟社交互动，但可能无法完全覆盖现实世界中复杂多变的社交场景（如非言语线索、文化差异或长期关系动态）。此外，Shapley值的计算复杂度较高，在更长的多轮对话中可能面临可扩展性挑战。

未来研究方向可从三方面展开：一是将SAVOIR框架扩展到更开放、动态的社交环境（如多智能体协作或在线社交平台），以测试其泛化能力；二是探索更高效的近似Shapley值计算方法，或结合因果推断技术来优化信用分配效率；三是研究如何融入人类实时反馈或社会规范知识，使奖励机制更能体现细微的社交礼仪（如幽默、共情或冲突化解）。这些改进有望推动语言智能体从“任务型社交”迈向更自然、自适应的人际交互。

### Q6: 总结一下论文的主要内容

该论文针对提升语言智能体社会智能的强化学习训练中存在的信用分配问题，提出了一个名为SAVOIR的理论框架。现有方法通常直接使用语言模型进行回顾式的、缺乏理论依据的奖励分配。SAVOIR的核心贡献在于结合合作博弈论中的两个互补原则来重构信用分配：首先，引入期望效用原则，将评估焦点从回顾性归因转向前瞻性估值，以衡量话语为未来有利轨迹创造战略潜力的能力；其次，采用沙普利值进行公平的信用分配，其满足效率性、对称性和边际性等公理保证，确保奖励与话语在所有可能顺序中的真实边际贡献成正比。在SOTOPIA基准测试上的实验表明，SAVOIR在所有评估设置中均取得了最先进的性能，其7B参数模型的表现匹配甚至超过了GPT-4o等专有模型。主要结论指出，社会智能需要与分析推理不同的能力，大型推理模型在此类任务上表现不佳，这凸显了SAVOIR所提出的前瞻性、理论驱动的信用分配方法对于培养真正社会智能体的重要意义。
