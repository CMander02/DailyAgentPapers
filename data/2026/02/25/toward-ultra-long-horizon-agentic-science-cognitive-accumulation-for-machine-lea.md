---
title: "Toward Ultra-Long-Horizon Agentic Science: Cognitive Accumulation for Machine Learning Engineering"
authors:
  - "Xinyu Zhu"
  - "Yuzhu Cai"
  - "Zexi Liu"
  - "Bingyang Zheng"
  - "Cheng Wang"
  - "Rui Ye"
  - "Yuzhi Zhang"
  - "Linfeng Zhang"
  - "Weinan E"
  - "Siheng Chen"
  - "Yanfeng Wang"
date: "2026-01-15"
arxiv_id: "2601.10402"
arxiv_url: "https://arxiv.org/abs/2601.10402"
pdf_url: "https://arxiv.org/pdf/2601.10402v4"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Ultra-Long-Horizon Autonomy"
  - "Cognitive Accumulation"
  - "Memory Management"
  - "Machine Learning Engineering"
  - "Hierarchical Cognitive Caching"
  - "Agentic Science"
  - "Context Management"
  - "Multi-Tiered Architecture"
  - "Autonomous Exploration"
relevance_score: 9.5
---

# Toward Ultra-Long-Horizon Agentic Science: Cognitive Accumulation for Machine Learning Engineering

## 原始摘要

The advancement of artificial intelligence toward agentic science is currently bottlenecked by the challenge of ultra-long-horizon autonomy, the ability to sustain strategic coherence and iterative correction over experimental cycles spanning days or weeks. While Large Language Models (LLMs) have demonstrated prowess in short-horizon reasoning, they are easily overwhelmed by execution details in the high-dimensional, delayed-feedback environments of real-world research, failing to consolidate sparse feedback into coherent long-term guidance. Here, we present ML-Master 2.0, an autonomous agent that masters ultra-long-horizon machine learning engineering (MLE) which is a representative microcosm of scientific discovery. By reframing context management as a process of cognitive accumulation, our approach introduces Hierarchical Cognitive Caching (HCC), a multi-tiered architecture inspired by computer systems that enables the structural differentiation of experience over time. By dynamically distilling transient execution traces into stable knowledge and cross-task wisdom, HCC allows agents to decouple immediate execution from long-term experimental strategy, effectively overcoming the scaling limits of static context windows. In evaluations on OpenAI's MLE-Bench under 24-hour budgets, ML-Master 2.0 achieves a state-of-the-art medal rate of 56.44%. Our findings demonstrate that ultra-long-horizon autonomy provides a scalable blueprint for AI capable of autonomous exploration beyond human-precedent complexities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能在迈向“代理科学”过程中所面临的“超长视野自主性”核心挑战。研究背景是，尽管大语言模型在短视野推理任务上表现出色，但科学发现本质上是一个超长视野的过程，涉及延迟反馈、高维探索以及持续数天甚至数周的实验周期。现有基于大语言模型的智能体在处理此类任务时存在明显不足：它们容易被执行过程中的海量细节所淹没，难以将稀疏的反馈整合成连贯的长期指导策略，本质上无法在长时间尺度上维持战略连贯性和进行迭代修正。

本文要解决的核心问题，正是如何使AI智能体具备这种“超长视野自主性”。作者将问题具体聚焦于“AI-for-AI”范式下的机器学习工程任务，以OpenAI的MLE-Bench（包含75个真实Kaggle竞赛）作为代表性场景。该场景要求智能体在长达数十小时的预算内，通过反复试错和经验积累来探索巨大的非结构化搜索空间，这远非简单的代码生成，而是对长期自主探索能力的严峻考验。

为此，论文提出了“认知积累”的概念框架，并引入了核心解决方案——分层认知缓存架构。该方法的核心创新在于，不再将长视野问题简单视为历史上下文窗口的线性扩展，而是将其重新定义为一种进化过程：将原始的瞬时经验提炼为稳定的知识，并进一步抽象为可跨任务迁移的智慧。通过这种结构化的信息分层与动态迁移机制，使智能体能够将高频的执行反馈与长期的战略规划解耦，从而克服上下文饱和的瓶颈，最终实现可持续、高效的长视野科学探索。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕上下文管理和自主机器学习两个核心领域展开。

在**上下文管理方法**方面，现有研究可分为两类。一是**系统架构扩展类**，如MemGPT、HiAgent和HippoRAG等，它们通过分层缓冲、外部内存分页或图检索等机制，从资源分配角度扩展有效上下文长度，但缺乏对经验如何随时间演化的显式建模。二是**经验抽象驱动类**，如Reflexion、Memento和Buffer of Thoughts等，它们将原始执行轨迹转化为可复用的反馈、案例或策略模板，但通常采用扁平或松散结构的内存存储，缺乏对内存生命周期和增长的明确调控机制。本文提出的分层认知缓存（HCC）与这些工作的区别在于，它首次将分层组织与经验抽象这两个设计维度在一个统一控制过程中进行联合调控，并引入了结构化的策略来管理原始痕迹的积累、提升和淘汰。

在**自主机器学习应用**方面，相关研究包括早期基准平台（如MLAgentBench）、采用迭代精化的工作（如AIDE），以及引入跨分支知识共享和进化策略的研究（如AIRA、AutoMLGen）。这些方法通常通过线性聚合或总结来管理上下文，或将“知识”视为同质实体进行传递，未能结构性地区分瞬时执行细节与长期稳定战略洞察。本文的ML-Master 2.0系统则通过HCC架构，明确实现了处理与状态的分离，动态管理上下文的提升与巩固，从而专门针对超长视野的自主性进行了优化。

### Q3: 论文如何解决这个问题？

论文通过提出“认知积累”框架和“分层认知缓存”架构来解决超长视野自主性问题。核心方法是将上下文管理重构为一个随时间进行认知积累的过程，其架构设计围绕HCC展开，包含两个关键组件：分层缓存和上下文迁移。

整体框架中，智能体首先通过上下文预取从先验智慧缓存中检索相关经验，构建初始上下文并生成初始代码。随后，它提出一个包含多个探索方向的分层研究计划，每个方向包含若干具体实施建议，并以并行方式执行这些建议。每个计划的执行定义了一个连续的探索阶段。在阶段结束时，智能体进行巩固并提议下一个研究计划，此过程循环直至任务完成或时间耗尽。

主要模块包括三层缓存结构：L1缓存（演化经验）存储高保真的原始执行轨迹，如当前研究计划、代码补丁和终端输出，作为工作记忆支持即时推理和调试。L2缓存（精炼知识）存储从已完成探索阶段提炼出的稳定认知，如关键判断、实验洞察和进度摘要，作为中期战略记忆，跨迭代试错保持连贯性。L3缓存（先验智慧）存储从以往任务中提炼出的、可迁移的任务无关策略，如稳健模型模板和可重用管道，作为长期记忆支持跨任务迁移和热启动。

创新点体现在：1）通过分层缓存将瞬态经验、稳定知识和可重用智慧在结构上分离，使智能体能解耦即时执行与长期实验策略，克服静态上下文窗口的限制。2）引入上下文迁移机制，包括预取、命中与提升。预取基于任务描述语义检索相关先验智慧；命中策略优先从L1获取原始事件，否则回退到L2的摘要；提升操作则通过LLM进行回顾性抽象，将原始轨迹压缩为精炼知识单元（阶段级提升）或可重用智慧（任务级提升），实现认知的持续精炼和积累。这一设计使智能体能在数十小时的探索中维持战略连贯性，并将稀疏反馈整合为连贯的长期指导。

### Q4: 论文做了哪些实验？

论文在MLE-Bench基准上进行了广泛的实验，以验证ML-Master 2.0的性能和有效性。实验设置方面，每个智能体配备36个AMD EPYC vCPU和两块NVIDIA GeForce RTX 4090 GPU，每四个任务共享1008GB内存和1TB SSD，每个任务的总时间限制为24小时。主要使用Deepseek-V3.2-Speciale作为编码和研究的主干语言模型，并使用407个Kaggle竞赛作为预热数据集以快速建立先验智慧。

对比方法包括基于专有LLM的方法（如OpenHands、MLAB、AIDE、R&D-Agent、AIRA-dojo、FM Agent、MLE-STAR、Thesis、Leeroo）和基于开源LLM的方法（如ML-Master、AutoMLGen）。主要结果如下：ML-Master 2.0在平均奖牌率上达到了56.4%的先进水平，显著优于之前最佳的专有LLM方法（50.7%），相对提升11.2%。在不同复杂度任务中，它在低、中、高复杂度任务上的奖牌率分别为75.8%、50.9%和42.2%，均排名第一。其他关键指标包括：有效提交率95.6%，高于中位数成绩的比例63.1%，银牌及以上比例45.3%，金牌比例19.6%。

此外，论文通过消融实验验证了分层认知缓存（HCC）架构的有效性。在MLE-Bench-Lite上的实验表明，完整架构（包含经验、知识和智慧三层）实现了72.7%的奖牌率，而移除任一层级都会导致性能下降，例如移除经验层会使奖牌率降至22.7%。上下文管理效果分析显示，HCC能将峰值上下文长度从超过20万token限制到约7万token，同时保留关键信息，使智能体能在第四次研究计划迭代中获得奖牌。性能随时间变化的分析也表明，ML-Master 2.0能随着迭代时间增加持续改进解决方案。

### Q5: 有什么可以进一步探索的点？

该论文提出的认知累积框架虽在长周期任务中取得进展，但仍存在可深入探索的方向。局限性方面，HCC架构依赖预定义的知识蒸馏层级，可能无法自适应复杂多变的科研环境；且评估仅基于MLE-Bench，在更开放的科学探索（如理论推导或跨领域实验）中泛化能力未经验证。未来研究可关注：1）动态层级优化，让智能体自主调整知识抽象粒度，例如引入元学习机制实时优化缓存策略；2）跨任务迁移增强，探索如何将已积累的“智慧”高效适配到异构科学问题中，减少重复试错；3）人机协同机制，设计人类专家反馈的增量融合接口，使智能体能兼顾自主性与领域知识纠偏。此外，可尝试将认知累积与神经符号计算结合，提升长期策略的可解释性与可靠性。

### Q6: 总结一下论文的主要内容

该论文针对智能体科学中的超长程自主性瓶颈问题，提出了一种名为ML-Master 2.0的自主智能体框架，旨在解决在持续数天或数周的实验周期中保持战略连贯性和迭代修正能力的挑战。核心贡献是引入了“认知积累”范式，并设计了分层认知缓存（HCC）架构。该方法将上下文管理从线性保留转变为动态的知识提炼过程，通过多层级结构将瞬时的执行轨迹逐步蒸馏为稳定的知识和可跨任务重用的先验智慧，从而解耦即时执行与长期实验策略，克服了静态上下文窗口的扩展限制。在OpenAI的MLE-Bench基准测试中，ML-Master 2.0在24小时预算内取得了56.44%的奖牌率，达到了最先进水平。主要结论表明，这种能够演化上下文的能力对于掌握现实科学研究中高维度、延迟反馈的环境至关重要，为超越人类先例复杂度的自主科学探索提供了可扩展的蓝图。
