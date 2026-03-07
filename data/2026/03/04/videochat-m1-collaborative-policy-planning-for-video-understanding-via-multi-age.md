---
title: "VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning"
authors:
  - "Boyu Chen"
  - "Zikang Wang"
  - "Zhengrong Yue"
  - "Kainan Yan"
  - "Chenyun Yu"
date: "2025-11-24"
arxiv_id: "2511.19524"
arxiv_url: "https://arxiv.org/abs/2511.19524"
pdf_url: "https://arxiv.org/pdf/2511.19524v2"
categories:
  - "cs.CV"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 2.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Collaborative Policy Planning (CPP) with Multi-Agent Reinforcement Learning (MARL)"
  primary_benchmark: "LongVideoBench"
---

# VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning

## 原始摘要

By leveraging tool-augmented Multimodal Large Language Models (MLLMs), multi-agent frameworks are driving progress in video understanding. However, most of them adopt static and non-learnable tool invocation mechanisms, which limit the discovery of diverse clues essential for robust perception and reasoning regarding temporally or spatially complex videos. To address this challenge, we propose a novel Multi-agent system for video understanding, namely VideoChat-M1. Instead of using a single or fixed policy, VideoChat-M1 adopts a distinct Collaborative Policy Planning (CPP) paradigm with multiple policy agents, which comprises three key processes. (1) Policy Generation: Each agent generates its unique tool invocation policy tailored to the user's query; (2) Policy Execution: Each agent sequentially invokes relevant tools to execute its policy and explore the video content; (3) Policy Communication: During the intermediate stages of policy execution, agents interact with one another to update their respective policies. Through this collaborative framework, all agents work in tandem, dynamically refining their preferred policies based on contextual insights from peers to effectively respond to the user's query. Moreover, we equip our CPP paradigm with a concise Multi-Agent Reinforcement Learning (MARL) method. Consequently, the team of policy agents can be jointly optimized to enhance VideoChat-M1's performance, guided by both the final answer reward and intermediate collaborative process feedback. Extensive experiments demonstrate that VideoChat-M1 achieves SOTA performance across eight benchmarks spanning four tasks. Notably, on LongVideoBench, our method outperforms the SOTA model Gemini 2.5 pro by 3.6% and GPT-4o by 15.6%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂视频理解任务中，现有基于多智能体框架的工具调用策略静态、非自适应的问题。研究背景是，尽管借助工具增强的多模态大语言模型（MLLMs）和多智能体框架推动了视频理解的进展，但现有方法在处理具有长时序上下文或复杂空间结构的视频时仍面临挑战。现有方法的不足在于，它们通常采用预先定义、固定不变的工具调用策略（即静态策略），这种机制无法根据视频内容和用户查询动态调整，限制了智能体从视频中发掘多样化、多尺度的关键线索，导致对复杂视频的感知和推理能力欠佳。

本文要解决的核心问题是：如何设计一个能够动态生成、协作优化工具调用策略的多智能体系统，以更有效地理解复杂视频。为此，论文提出了VideoChat-M1系统，其核心是创新的协作策略规划范式。该范式通过三个关键过程——策略生成、策略执行和策略通信——使多个策略智能体能够针对用户查询生成各自独特的工具调用计划，在执行过程中通过交互共享中间线索并动态更新策略，从而协同探索更丰富的视频信息。此外，论文还为该范式配备了一种简洁的多智能体强化学习方法，通过结合最终答案奖励和中间协作过程反馈，联合优化整个智能体团队，以提升视频理解的性能和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为视频理解和多智能体强化学习两大类。

在**视频理解**方面，早期研究致力于通过扩展模型架构、上下文窗口或使用强化学习来提升单一模型的性能，但这些方法在同时处理感知、检索和推理时存在局限。后续工作尝试为单一智能体配备检索、记忆等工具，但其通用设计难以实现有效整合。与LVAgent等依赖静态、非学习性协作的系统不同，本文提出的VideoChat-M1是一个可训练的多智能体框架，能动态适应多样化的视频任务。

在**多智能体强化学习（MARL）**方面，现有研究主要遵循两种范式。一是无需训练的系统（如CAMEL、MetaGPT），依赖预设逻辑和固定角色，但其静态的、以文本为中心的设计难以处理长视频理解等动态多模态任务。二是基于强化学习的范式，通过优化智能体行为或交互架构来训练协作策略，但这些方法目前多局限于单模态文本领域，未能有效应对视频特有的时序和感知挑战，且难以协同训练异构智能体。本文受成功的多智能体GUI流程启发，提出了VideoChat-M1框架，旨在实现针对复杂多模态任务的多样化智能体的联合训练。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VideoChat-M1的新型多智能体系统来解决静态、不可学习的工具调用机制在复杂视频理解中的局限性。其核心方法是**协作策略规划（Collaborative Policy Planning, CPP）范式**，并辅以**多智能体强化学习（MARL）** 进行联合优化。

**整体框架与主要模块：**
CPP范式包含三个核心组件：一组策略智能体 $\mathcal{G}$、一组视频感知工具 $\mathcal{T}$ 和一个共享内存缓冲区 $\mathcal{M}$。其工作流程是一个迭代的、三阶段协作循环：
1.  **策略生成**：每个智能体根据用户查询 $\mathcal{Q}$ 和可用工具集 $\mathcal{T}$，独立生成一个初始的、序列化的工具调用策略计划 $\mathcal{P}_i$。
2.  **策略执行**：每个智能体按序执行其策略计划中的步骤，调用指定工具分析视频 $\mathcal{V}$，并基于上一步结果生成中间答案 $\mathcal{A}_{i,n}$。
3.  **策略通信**：在执行每个步骤后，所有智能体将中间结果存入共享内存 $\mathcal{M}$。每个智能体参考 $\mathcal{M}$ 中的团队信息和自身初始策略，动态决定是否更新其后续策略为 $\mathcal{P}'_i$。此过程可迭代进行，使智能体能够基于同伴的探索经验实时优化决策。

最终，各智能体汇总自身结果形成答案，并通过多数投票或指定智能体（如性能最佳的Qwen3-8B）整合的方式产生最终输出。

**关键技术细节与创新点：**
1.  **动态、可学习的协作策略规划**：与以往静态、固定的工具调用机制不同，CPP允许多个智能体通过实时通信和内存共享，在策略执行过程中动态调整各自的计划，从而发掘更丰富、更多样化的视频线索以应对时空复杂性。
2.  **多智能体强化学习优化**：论文创新性地引入MARL框架来联合训练智能体团队，提升其协作与适应能力。训练分为两个阶段：
    *   **监督微调（SFT）**：利用高性能模型（如GPT-4o）通过CPP自动标注高质量的策略计划数据，以此训练每个智能体生成结构化初始计划的基本能力。
    *   **MARL联合优化**：设计了一个复合奖励函数 $\mathcal{R} = \mathcal{R}_{res} + \mathcal{R}_{format} + \mathcal{R}_{col}$ 来指导训练。其中，$\mathcal{R}_{res}$ 基于最终答案的正确性给予奖励；$\mathcal{R}_{format}$ 确保输出格式（如工具调用）的规范性和可执行性；$\mathcal{R}_{col}$ 则鼓励有效的协作行为（例如，借鉴同伴的有用信息、避免重复探索）。这使得智能体团队不仅能追求正确结果，还能优化协作过程本身。

综上所述，VideoChat-M1通过CPP范式实现了多智能体在视频理解任务中的动态、迭代式协作，并首次利用MARL对该协作过程进行端到端的优化，从而显著提升了在长视频和复杂场景下的理解性能。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估和分析。实验设置方面，研究使用8块A100 80G GPU进行训练和测试。监督微调（SFT）和多智能体强化学习（MARL）的学习率分别设为1e-6和1e-7，SFT进行1个epoch，MARL进行200步，采用4次rollout和8的批次大小，并应用了智能体随机丢弃（agent dropout）来增强协作泛化能力。

数据集和基准测试涵盖了8个视频理解基准：MLVU-Dev、LongVideoBench、VSI-Bench、VideoMME、MMR-V、VideoMMMU、Video-Holmes和Charades-STA，涉及多项选择、开放问答、时空推理、跨模态推理、时序定位等多种任务。主要评估指标为准确率（Accuracy），部分数据集使用特定指标，如MLVU的算术平均（M-avg）和几何平均（G-avg），Video-MME的短/中/长视频准确率，VSI-Bench的距离、方向、顺序及平均准确率，Charades-STA则采用预测与真实时间段的平均交并比（mIoU）。

对比方法包括Qwen2-VL-72B、GPT-4o、Gemini-1.5-Pro等大规模模型。主要结果显示，VideoChat-M1在80B参数量级以下的模型中，在全部8个基准上取得了最先进（SOTA）性能。关键数据指标包括：在LongVideoBench上准确率达82.3%，超越Gemini 2.5 Pro 3.6%，超越GPT-4o 15.6%；在Video-Holmes和MMR-V上分别提升14.8%和14.3%；在VSI-Bench空间推理任务上提升2.4%，在Charades时序定位任务上领先1.8%。效率方面，模型平均每视频仅使用69.9帧（为基线模型的12.3%~18.2%），平均推理时间仅19.8秒（为基线模型的8.7%~21.9%），实现了优异的效率-性能权衡。

消融实验验证了多智能体协作规划（CPP）和MARL组件的有效性：智能体数量从1增至4时性能持续提升，4个异构智能体组合达到最佳（Video-Holmes 60.5%，LongVideoBench 82.3%）；MARL中的过程奖励、格式奖励和智能体丢弃均对性能有贡献；完整流程（SFT后接MARL）性能最优，显著优于单独使用SFT或MARL。

### Q5: 有什么可以进一步探索的点？

本文提出的VideoChat-M1系统在动态策略规划和多智能体协作方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，系统依赖于预定义的工具集，这限制了其在开放域视频理解中的泛化能力；未来可研究如何动态扩展或生成工具，以应对未知任务。其次，MARL训练过程可能计算成本高昂，且对中间协作过程的奖励设计较为启发式；可探索更高效的离线学习或模仿学习方法，并设计更理论驱动的协作奖励机制。此外，当前框架主要关注视觉时空线索，但视频理解常需结合音频、文本等多模态信息；未来可整合跨模态智能体，实现更深层次的融合分析。最后，系统的可解释性仍有提升空间；通过可视化策略决策链或引入因果推理模块，能增强用户对协作过程的理解与信任。这些改进有望推动多智能体视频理解系统向更高效、通用和可信的方向发展。

### Q6: 总结一下论文的主要内容

本文提出了一种名为VideoChat-M1的新型多智能体系统，旨在解决视频理解中现有方法因采用静态、不可学习的工具调用机制而难以发掘复杂视频时空线索的问题。其核心贡献是引入了协作策略规划（CPP）范式，该范式包含三个关键过程：首先，多个策略智能体根据用户查询生成各自独特的工具调用策略；其次，每个智能体按序调用相关工具执行策略以探索视频内容；最后，在执行过程中，智能体通过交互通信来更新彼此的策略，从而实现动态协同与策略优化。此外，论文还为CPP配备了一种简洁的多智能体强化学习（MARL）方法，利用最终答案奖励和中间协作过程反馈联合优化所有策略智能体。实验表明，VideoChat-M1在涵盖四项任务的八个基准测试中取得了最先进的性能，尤其在LongVideoBench上显著超越了GPT-4o和Gemini 2.5 pro等模型。这项工作通过动态、可学习的多智能体协作机制，显著提升了视频理解中感知与推理的鲁棒性。
