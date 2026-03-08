---
title: "Expanding LLM Agent Boundaries with Strategy-Guided Exploration"
authors:
  - "Andrew Szot"
  - "Michael Kirchhof"
  - "Omar Attia"
  - "Alexander Toshev"
date: "2026-03-02"
arxiv_id: "2603.02045"
arxiv_url: "https://arxiv.org/abs/2603.02045"
pdf_url: "https://arxiv.org/pdf/2603.02045v1"
categories:
  - "cs.LG"
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
  key_technique: "Strategy-Guided Exploration (SGE)"
  primary_benchmark: "N/A"
---

# Expanding LLM Agent Boundaries with Strategy-Guided Exploration

## 原始摘要

Reinforcement learning (RL) has demonstrated notable success in post-training large language models (LLMs) as agents for tasks such as computer use, tool calling, and coding. However, exploration remains a central challenge in RL for LLM agents, especially as they operate in language-action spaces with complex observations and sparse outcome rewards. In this work, we address exploration for LLM agents by leveraging the ability of LLMs to plan and reason in language about the environment to shift exploration from low-level actions to higher-level language strategies. We thus propose Strategy-Guided Exploration (SGE), which first generates a concise natural-language strategy that describes what to do to make progress toward the goal, and then generates environment actions conditioned on that strategy. By exploring in the space of strategies rather than the space of actions, SGE induces structured and diverse exploration that targets different environment outcomes. To increase strategy diversity during RL, SGE introduces mixed-temperature sampling, which explores diverse strategies in parallel, along with a strategy reflection process that grounds strategy generation on the outcomes of previous strategies in the environment. Across UI interaction, tool-calling, coding, and embodied agent environments, SGE consistently outperforms exploration-focused RL baselines, improving both learning efficiency and final performance. We show that SGE enables the agent to learn to solve tasks too difficult for the base model.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）作为智能体进行强化学习（RL）训练时面临的**探索（exploration）难题**。研究背景是，RL已被证明能有效将LLM训练为执行计算机操作、工具调用和编码等任务的智能体，但现有方法在探索上存在严重不足。具体而言，LLM智能体通常在复杂的语言-动作空间中运作，其奖励信号稀疏（仅在达成目标时获得），且训练初始策略源自预训练模型，该模型已对“可能输出”形成高度集中的分布。这导致传统RL方法主要是在基座模型已有的行为分布内进行采样和微调，难以主动探索并发现全新的、能成功解决任务的动作轨迹，从而限制了智能体学习解决更困难任务的能力。

因此，本文要解决的核心问题是：**如何设计一种有效的探索机制，使LLM智能体在RL训练中能超越基座模型的初始能力边界，发现并学会解决那些原本无法完成的任务**。为此，论文提出了“策略引导探索”（SGE）方法，其核心思想是利用LLM自身的语言规划和推理能力，将探索从低层级的动作空间转移到高层级的语言策略空间。SGE首先让模型生成一个简洁的自然语言“策略”，描述为达成目标应采取的宏观步骤，然后基于此策略生成具体的环境动作。通过探索多样化的策略而非直接探索动作，SGE能引导出更具结构性、目标导向性的探索行为，从而更有效地发现通往成功的轨迹。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕强化学习中的探索问题、语言引导的层次控制以及LLM后训练方法展开，可分为以下几类：

**1. 强化学习探索方法**：传统RL探索方法如基于动作采样的简单探索在稀疏奖励或长视野任务中效果有限。一些工作通过建模环境动态的不确定性来引导探索，另一些则引入时间扩展的探索或分层RL（如选项学习）。本文同样关注复杂探索策略，但利用LLM的语言推理能力，将探索从底层动作转移到高层语言策略空间，从而更高效地处理语言-动作空间的复杂性。

**2. 语言引导的层次控制**：已有研究使用语言进行规划器与控制策略间的通信，但主要用于协调而非提升探索能力。本文提出的SGE则直接利用LLM生成自然语言策略来指导探索，旨在解决基模型无法完成的更困难任务，这与单纯的语言层次控制有本质区别。

**3. LLM后训练与探索技术**：先前研究表明，LLM的RL后训练通常仅优化基模型已有能力，难以解决新问题。一些工作通过维持高输出熵或使用“k中通过”奖励来促进多样性，但这些方法仍需基模型至少部分成功才能获得学习信号。SGE通过策略空间探索和混合温度采样等技术，能在基模型初始成功率极低的任务中有效引导探索。此外，其他探索技术如随机网络蒸馏或策略熵奖励虽也针对LLM设计，但多集中于数学推理等问答式任务，而SGE专注于多步智能体环境中的序列决策问题。

**4. 语言抽象与规划方法**：部分研究在LLM推理中引入语言抽象或规划步骤，例如通过蒸馏生成“推理抽象”。但SGE无需教师模型，并融合了在线RL中的多样性最大化机制（如策略反思），且适用于仅给定最终目标、无标准动作序列的多步智能体场景，这与依赖真实答案生成提示或专家模型的方法不同。

### Q3: 论文如何解决这个问题？

论文通过提出“策略引导探索”方法来解决LLM智能体在强化学习中探索效率低下的问题。其核心思想是将探索从底层动作空间转移到高层语言策略空间，利用LLM的语言规划能力生成多样化的策略来引导动作执行，从而在复杂观察和稀疏奖励的环境中实现更结构化、更有效的探索。

整体框架基于标准的POMDP建模，但关键创新在于对策略模型采样过程的三个修改。首先，**策略提示**：在每一步，模型不再直接采样中间推理轨迹和动作，而是先从一个专门的“策略采样分布”中采样一个简洁的自然语言策略描述。该策略描述了为达成目标应采取的高层行动计划，并映射到一组特定且互不重叠的动作分布。策略生成后，模型再基于该策略生成具体的推理轨迹和动作。

其次，**混合温度采样**：为了在策略层面鼓励多样性，该方法对策略令牌的采样采用较高的温度，而对后续推理和动作令牌的采样采用较低的温度。这种“混合温度”设计基于一个关键洞见：直接对动作进行高温采样可能只产生表面差异（如在UI控制中点击同一按钮的不同坐标），而生成多样化的高层策略能更有效地探索不同的环境结果。该方法并行生成K个策略，这与GRPO等基于组的RL算法所需的并行响应数量一致，因此不增加额外生成开销。

最后，**策略反思**：该方法利用环境反馈动态提升策略多样性。它包括两种机制：一是“负面策略反思”，当某个策略导致任务失败时，在后续同任务的训练中，会以该失败策略和负面反思提示为条件，引导模型批判失败策略并生成改进的新策略；二是“正面策略反思”，以成功策略为条件，引导模型生成受其启发的新策略。反思过程基于旧策略版本的策略序列，进一步增加了策略的多样性。

主要创新点在于：1）将探索空间从动作提升到语言策略层面，实现了更结构化、目标导向的探索；2）通过混合温度采样，高效且低成本地生成多样化策略；3）通过策略反思机制，利用环境反馈（包括稀疏奖励和可能的文本反馈）进行在线学习，不断优化和丰富策略库。该方法不依赖真实解、特权信息或更强LLM，仅通过修改RL训练中的采样过程，即可显著提升学习效率和最终性能，使智能体能够学会解决基础模型原本无法完成的任务。

### Q4: 论文做了哪些实验？

论文在四个智能体领域进行了实验：AndroidWorld（手机UI控制）、Language Rearrangement（具身家庭物体重排）、Coding（代码生成）和AppWorld（多步骤工具调用）。实验设置上，针对不同环境使用了不同的基础模型进行微调，例如在Coding和LangR中使用Qwen3-4B-Instruct，在AppWorld中使用Qwen3-8B，在AndroidWorld中使用Qwen2.5-VL-3B。对比方法包括标准的GRPO、鼓励探索的Entropy Advantage、基于新奇性探索的Random Network Distillation（RND）、同样涉及策略生成的RL with Abstraction Discovery（RLAD），以及基础模型的Zero-Shot性能（pass@k）。

主要结果显示，SGE在所有环境中均优于基线。在训练性能上，SGE的平均最终成功率比各环境下次优基线高出27%，并且在Coding和LangR中，其性能超越了基础模型的最大pass@k上限约11%，表明SGE能探索出基础模型不具备的新行为。在泛化到未见任务上，SGE也表现最佳：在Coding测试集上pass@1达到29.2（±0.7），优于GRPO的22.0和Zero-Shot的13.5；在AndroidWorld上达到36.7（±1.3），优于GRPO的21.9；在LangR上达到60.8（±0.6），优于GRPO的46.0；在AppWorld上达到66.6（±2.9），优于GRPO的49.3。此外，SGE训练出的策略其pass@k曲线能持续提升并超越基础模型的天花板，而标准GRPO仅能“拉平”曲线、使pass@1接近基础模型的pass@k值。

### Q5: 有什么可以进一步探索的点？

该论文提出的策略引导探索（SGE）方法虽然有效，但仍存在一些局限性和值得深入探索的方向。首先，策略的生成和评估高度依赖LLM自身的推理与规划能力，这可能导致策略质量不稳定，且在复杂、动态环境中策略的适应性和泛化能力有待验证。其次，当前方法主要关注策略的多样性，但对策略的“可执行性”和“最优性”缺乏精细的引导和评估机制，未来可结合环境反馈或价值函数对策略进行更精准的筛选与优化。

从改进思路上看，可以探索以下几个方向：一是将策略探索与基于模型的强化学习相结合，利用世界模型预测策略执行后果，从而在“想象”中进行更高效、低成本的策略搜索与迭代。二是引入分层强化学习框架，将高层策略生成与底层动作执行更彻底地解耦，并允许策略在不同抽象层级间进行学习和迁移。三是增强策略的元学习能力，使智能体能够从过往探索经验中总结出有效的策略生成模式，从而加速在新任务上的适应过程。最后，如何将SGE与模仿学习、课程学习等其他范式结合，以利用人类示范或渐进式任务设计来进一步引导和结构化探索过程，也是一个富有潜力的研究方向。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体在强化学习（RL）中面临的探索难题，提出了一种策略引导探索（SGE）方法。核心问题是LLM智能体在语言-动作空间中，面对复杂观察和稀疏奖励时，探索效率低下。SGE的核心思想是将探索从底层动作空间转移到高层语言策略空间。其方法首先让LLM生成一个简洁的自然语言策略，描述如何向目标推进；然后根据该策略生成具体的环境动作。通过引入混合温度采样并行探索多样化策略，并结合策略反思过程（基于先前策略的环境结果来调整新策略），SGE实现了结构化且多样化的探索。实验表明，在UI交互、工具调用、编程和具身智能体等多种环境中，SGE在学习和最终性能上均优于专注于探索的RL基线方法，使智能体能够学会解决基础模型难以完成的任务。该工作的主要贡献在于通过高层语言策略引导，有效扩展了LLM智能体的能力边界。
