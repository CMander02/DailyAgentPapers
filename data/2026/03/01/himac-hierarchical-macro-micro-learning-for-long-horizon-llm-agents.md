---
title: "HiMAC: Hierarchical Macro-Micro Learning for Long-Horizon LLM Agents"
authors:
  - "Hongbo Jin"
  - "Rongpeng Zhu"
  - "Jiayu Ding"
  - "Wenhao Zhang"
  - "Ge Li"
date: "2026-03-01"
arxiv_id: "2603.00977"
arxiv_url: "https://arxiv.org/abs/2603.00977"
pdf_url: "https://arxiv.org/pdf/2603.00977v1"
categories:
  - "cs.AI"
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
  key_technique: "HiMAC (Hierarchical Macro-Micro Agentic Control), critic-free hierarchical policy optimization, iterative co-evolution training strategy"
  primary_benchmark: "ALFWorld, WebShop, Sokoban"
---

# HiMAC: Hierarchical Macro-Micro Learning for Long-Horizon LLM Agents

## 原始摘要

Large language model (LLM) agents have recently demonstrated strong capabilities in interactive decision-making, yet they remain fundamentally limited in long-horizon tasks that require structured planning and reliable execution. Existing approaches predominantly rely on flat autoregressive policies, where high-level reasoning and low-level actions are generated within a single token sequence, leading to inefficient exploration and severe error propagation over extended trajectories. In this work, we propose HiMAC, a hierarchical agentic RL framework that explicitly decomposes long-horizon decision-making into macro-level planning and micro-level execution. HiMAC models reasoning as a structured blueprint generation process followed by goal-conditioned action execution, enabling robust long-horizon planning within LLM-based agents. To train this hierarchy efficiently, we introduce a critic-free hierarchical policy optimization paradigm that extends group-based reinforcement learning to bi-level structures through hierarchical relative advantage estimation. Furthermore, we propose an iterative co-evolution training strategy that alternates between planner exploration and executor adaptation, mitigating the non-stationarity inherent in hierarchical learning. Extensive experiments on ALFWorld, WebShop, and Sokoban demonstrate that HiMAC consistently outperforms strong prompting and reinforcement learning baselines, achieving state-of-the-art performance and substantially improved sample efficiency across both text-based and visually grounded environments. Our results show that introducing structured hierarchy, rather than increasing model scale alone, is a key factor for enabling robust long-horizon agentic intelligence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在执行长视野任务时存在的根本性局限。研究背景是，尽管LLM智能体在交互式决策中展现出强大能力，但在需要结构化规划和可靠执行的长视野任务（如多步骤推理、导航）中表现不佳。现有方法主要依赖于“扁平”的自回归策略，即在一个单一的令牌序列中同时生成高层推理和底层动作。这种方法的不足在于：它导致探索效率低下，因为智能体需要在巨大的组合搜索空间中进行短视的逐令牌预测；并且错误会沿轨迹指数级传播，早期步骤的微小偏差可能导致后续任务完全失败，即存在语义漂移问题。

因此，本文要解决的核心问题是：如何为基于LLM的智能体设计一种能够有效进行长视野决策的框架。具体而言，论文提出了HiMAC框架，通过显式的层次分解来应对上述挑战。它将长视野决策分解为宏观层面的蓝图规划和微观层面的目标条件执行，从而将探索问题从单一的巨大空间拆分为两个缩减的搜索空间，并遏制了错误的传播。此外，论文还致力于解决实现这种层次结构带来的优化难题，即如何在不依赖难以训练的价值网络（评论家）的情况下，对宏观规划器和微观执行器进行稳定、高效的联合训练，并处理两者在共同学习过程中固有的非平稳性问题。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：LLM智能体、智能体强化学习和分层强化学习。

在**LLM智能体**方面，早期提示方法（如ReAct、Reflexion）通过交错推理与行动来处理短视距任务，但它们采用“扁平”的自回归策略，在长视距任务中容易因微小偏差累积而失败。HiMAC与这些工作的核心区别在于，它明确地将高层推理与低层执行解耦，而非将其混在一个令牌序列中生成。

在**智能体强化学习**方面，传统方法（如PPO）或新兴的无评论者分组优化方法（如RLOO、GRPO）被用于优化LLM智能体策略。然而，这些方法仍优化一个将推理与动作联合编码的单一策略，未能解决长视距探索的指数级复杂性和错误传播问题。HiMAC则引入了分层策略优化，将分组相对优势估计扩展到双层结构，专门应对这些挑战。

在**分层强化学习**方面，经典方法（如Options框架、HIRO）通过时间抽象和子目标设定来分解任务。但它们的目标表示依赖于预定义的紧凑状态空间（如机器人关节位置），且优化依赖于不稳定的参数化价值网络。HiMAC的关键创新在于，它在开放的自然语言蓝图空间中进行操作，并用分层分组目标取代了基于评论者的优化，从而适应了LLM智能体的语义推理需求。

### Q3: 论文如何解决这个问题？

论文通过提出HiMAC这一分层宏观-微观学习框架来解决长视野任务中LLM智能体在结构化规划和可靠执行方面的根本性限制。其核心方法是**将长视野决策过程显式分解为宏观层面的蓝图规划和微观层面的目标条件执行**，从而替代传统的扁平自回归策略。

在整体架构上，HiMAC包含两个主要模块：**宏观策略（规划器）**和**微观策略（执行器）**。宏观策略负责在开放的自然语言语义空间中搜索并生成一个结构化的蓝图 \(\mathbf{z}\)，该蓝图由一系列自然语言子目标 \(\{g_1, \dots, g_K\}\) 组成，将全局指令分解为可处理的子问题。微观策略则作为一个专门的执行器，在给定固定蓝图 \(\mathbf{z}^*\) 的条件下，基于当前观察 \(o_{\le t}\) 和活跃子目标 \(z_k\) 生成原子动作 \(a_t\)。子目标之间的转换由执行器自主触发，当它生成特殊的 `<sub_done>` 终止令牌时，即切换到下一个子目标。这种设计通过**时序注意力掩码**显式地将代理的上下文窗口限制在相关的任务片段，防止长轨迹中的语义漂移。此外，框架还引入了轻量级的、基于预算的回退机制，以处理意外的环境随机性。

关键技术体现在其**无需评论家的分层策略优化范式**和**迭代协同进化训练策略**。优化方面，HiMAC将基于群体的强化学习（GRPO）扩展至双层结构，通过**分层相对优势估计**分别为宏观和微观目标构建优化。具体而言，宏观目标通过采样一组候选蓝图，并用当前微观策略进行贪婪推演评估其回报，从而计算蓝图层面的群体相对优势来更新宏观策略（仅更新蓝图相关令牌）。微观目标则在固定一个高置信度蓝图 \(\mathbf{z}^*\) 的条件下，采样一组执行轨迹，利用轨迹回报的差异（完全归因于执行质量）计算微观层面的优势来更新微观策略（仅更新动作令牌）。

为了稳定这种双层优化中固有的非平稳性问题（规划器追逐变化的执行能力，而执行器适应漂移的子目标分布），论文提出了**迭代协同进化训练策略**。该策略将训练过程解耦为两个交替阶段：**A阶段（宏观探索）** 冻结微观策略，将其视为环境的一部分，仅优化宏观策略以探索更好的蓝图；**B阶段（微观适应）** 则固定从A阶段选出的最高回报蓝图 \(\mathbf{z}^*\)，仅优化微观策略以适应当前的规划。这种交替更新确保了每一层都在一个相对平稳的对应层基础上进行优化，从而实现了规划与执行的协同进化，显著提升了样本效率和长视野任务的最终性能。

### Q4: 论文做了哪些实验？

论文在三个具有挑战性的长视野智能体任务基准上进行了实验：ALFWorld（具身决策）、WebShop（网络购物导航）和Sokoban（视觉推箱子谜题）。实验设置方面，对于文本任务（ALFWorld、WebShop），使用Qwen2.5-Instruct（1.5B和7B）作为宏微观策略的骨干模型；对于视觉任务（Sokoban），使用Qwen2.5-VL和Qwen3-VL系列视觉语言模型。关键参数包括：ALFWorld的最大提示长度2048，响应长度512，并行环境128个；WebShop和Sokoban的回合步数限制为15步；KL散度系数β固定为0.01。

对比方法包括基于提示的方法（ReAct、Reflexion）和先进的强化学习方法（PPO、RLOO、GRPO、GiGPO）。主要结果如下：在ALFWorld上，使用1.5B骨干的HiMAC总体成功率达到89.9%，优于最强的GiGPO基线（86.1%）；在7B模型上达到92.1%。在WebShop上，HiMAC（1.5B）的成功率（83.4%）和得分（92.2%）显著超越GiGPO（成功率67.4%）。在Sokoban上，使用Qwen2.5-VL-7B的HiMAC成功率为87.5%，得分6.70，优于GiGPO（82.8%，5.27）。消融实验验证了层次结构、迭代协同进化策略、可学习的子目标完成标记（<sub_done>）以及高质量蓝图选择的重要性。样本效率分析显示，HiMAC在所有基准上都以更少的训练迭代达到目标性能，例如在ALFWorld上达到75%成功率仅需约110次迭代，而GRPO需要约150次。

### Q5: 有什么可以进一步探索的点？

该论文提出的HiMAC框架在长视野任务上取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，方法在相对封闭的基准环境（如ALFWorld、WebShop）中验证，未来需扩展到更开放、动态的真实世界场景（如家庭服务机器人、复杂游戏），以检验其泛化性和鲁棒性。其次，蓝图（macro-plan）的跨领域可迁移性尚未充分研究，未来可探索如何将学习到的结构化规划知识迁移到新任务，减少重复训练成本。此外，框架依赖LLM作为核心组件，可能受限于模型本身的推理错误和上下文长度，未来可结合更高效的思维链或检索增强技术来提升规划质量。从方法改进角度看，可引入多粒度层次（如增加中期策略层）或动态层次调整机制，以处理更复杂的任务分解。最后，训练中的协同进化策略虽缓解了非平稳性问题，但计算开销较大，未来可研究更轻量的异步优化方法，进一步提升样本效率。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）智能体在长视野任务中存在的规划与执行困难，提出了一个名为HiMAC的分层宏微观学习框架。其核心问题是现有基于单一自回归序列的“扁平”策略容易导致探索效率低下和错误累积，难以完成需要结构化规划的长程任务。

论文的核心方法是显式地将决策分解为宏观层面的蓝图规划和微观层面的目标条件执行。在方法上，HiMAC采用了一种免评论家的分层策略优化范式，通过分层相对优势估计将基于组的强化学习扩展到双层结构，并提出了规划器探索与执行器适应交替进行的协同进化训练策略，以缓解分层学习中的非平稳性问题。

主要结论是，HiMAC在ALFWorld、WebShop和Sokoban等多个文本与视觉环境中的实验均超越了先进的提示学习和强化学习基线，实现了最优性能并显著提升了样本效率。这表明，引入结构化的层次化设计，而非单纯增大模型规模，是构建鲁棒长视野智能体智能的关键因素。
