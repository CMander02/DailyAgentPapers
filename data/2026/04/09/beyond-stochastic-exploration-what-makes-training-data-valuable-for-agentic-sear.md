---
title: "Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search"
authors:
  - "Chuzhan Hao"
  - "Wenfeng Feng"
  - "Guochao Jiang"
  - "Guofeng Quan"
  - "Guohua Liu"
  - "Yuewei Zhang"
date: "2026-04-09"
arxiv_id: "2604.08124"
arxiv_url: "https://arxiv.org/abs/2604.08124"
pdf_url: "https://arxiv.org/pdf/2604.08124v1"
categories:
  - "cs.AI"
tags:
  - "Agent Training"
  - "Reinforcement Learning"
  - "Search Agent"
  - "Reasoning"
  - "Experience Replay"
  - "Training Stability"
  - "Generalization"
relevance_score: 7.5
---

# Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search

## 原始摘要

Reinforcement learning (RL) has become an effective approach for advancing the reasoning capabilities of large language models (LLMs) through the strategic integration of external search engines. However, current RL-based search agents often rely on a process of stochastic exploration guided by carefully crafted outcome rewards, leading to inefficient reasoning trajectories and unstable training. To address these issues, we propose a novel framework, Hierarchical Experience (HiExp), to enhance the performance and training stability of search agents. Specifically, we extract empirical knowledge through contrastive analysis and a multi-level clustering mechanism, transforming raw reasoning trajectories into hierarchical experience knowledge. By leveraging experience-aligned training, we effectively regularize stochastic exploration, evolving it into a strategic and experience-driven search process. Extensive evaluations on multiple complex agentic search and mathematical reasoning benchmarks demonstrate that our approach not only achieves substantial performance gains but also exhibits strong cross-task and cross-algorithm generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习（RL）的大语言模型（LLM）搜索智能体在复杂推理任务中，因依赖随机探索和手工设计的结果奖励而导致的推理轨迹低效和训练不稳定的核心问题。研究背景是，尽管RL在提升LLM的任务规划和智能体推理能力方面成效显著，但现有方法主要依赖于通过精心设计的最终结果奖励来引导随机探索过程。这种范式存在明显不足：首先，它难以进行全局战略规划，探索出的推理路径往往效率低下，尤其当使用较小语言模型处理复杂任务时更为突出；其次，在多轮交互场景中，提供一致的奖励信号本身非常困难，这导致端到端RL训练过程极不稳定，优化波动大。

因此，本文要解决的核心问题是：如何超越这种低效、不稳定的随机探索模式，使智能体搜索过程更具战略性和高效性。具体而言，论文提出通过从原始推理轨迹中提取并利用层次化的经验知识，来规整和引导RL智能体的探索行为，从而将随机的探索转变为由经验驱动的战略性搜索，最终实现更优的性能和更稳定的训练过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于检索增强生成（RAG）的方法、基于强化学习（RL）的智能体方法，以及针对训练数据与探索效率优化的方法。

在RAG方法中，早期工作如IRCoT、AirRAG等通过人工设计提示或工作流（如分支、迭代、蒙特卡洛树搜索）来引导检索过程。这些方法受限于固定的范式，未能充分释放大语言模型的内在推理潜力。随后，Search-o1等工作通过设计更灵活的智能体搜索工作流，提升了模型的泛化能力。

在基于RL的智能体方法中，DeepSeek-R1等工作证明了基于结果的RL能显著增强模型的自主推理与决策能力。后续研究如DeepResearcher、s3、EvolveSearch和StepSearch将RL应用于复杂搜索场景，分别从真实网络交互、样本效率、智能体自进化、细粒度奖励等角度进行优化。这些方法的核心是通过随机探索和结果奖励来训练智能体，但常导致推理轨迹低效和训练不稳定。

本文提出的HiExp框架与上述RL方法密切相关，但关键区别在于它超越了单纯的随机探索。本文通过对比分析和多级聚类从原始轨迹中提取层次化的经验知识，并利用经验对齐训练来正则化探索过程，从而将随机探索转变为战略性的、经验驱动的搜索。这解决了现有RL方法在训练效率和稳定性上的不足，并展现出强大的跨任务和跨算法泛化能力。

### Q3: 论文如何解决这个问题？

论文提出的HiExp框架通过构建层次化经验知识库并将其与训练过程对齐，来解决基于强化学习的搜索代理中存在的随机探索效率低下和训练不稳定的问题。其核心方法包含两个主要组件：层次化经验构建和经验对齐训练。

在层次化经验构建阶段，框架首先将训练过程中产生的原始推理轨迹（包含成功与失败路径）视为内生的知识源。利用策略模型或教师模型的自反思能力，通过对比分析提取关键决策点和推理陷阱，形成案例化经验（e_i）及其摘要描述（d_i）。随后，通过多级聚类机制将这些碎片化经验系统化：使用预训练语义编码器将经验映射到向量空间，通过凝聚聚类和严格的相似度阈值合并相似问题的经验，并利用大语言模型将每个簇内的实例级经验提炼为泛化的战略经验。这一过程构建了一个自演化的层次化经验知识库（HEK），其中包含从具体案例到通用策略的不同抽象层次的经验。

在经验对齐训练阶段，框架引入了经验对齐引导机制。在基于无评论家强化学习算法（如GRPO）的轨迹生成过程中，系统会动态检索HEK中的知识来指导探索。具体而言，在每个推理步骤，系统计算当前查询的语义嵌入，并与HEK中的经验索引进行相似度匹配，检索出最相关的经验。框架采用动态引导策略：在推理初期优先注入全局战略经验以提供高层指导；在中间推理步骤则自适应地提供与当前查询语义高度接近的细粒度启发式经验。这种层次化检索使智能体的探索从随机搜索转变为经验对齐的启发式搜索。

最终，训练目标在标准的策略优化目标中显式地结合了结果奖励和层次化经验知识库。由于推理轨迹以层次化经验为条件，采样轨迹的优势函数质量更高，从而促进了更稳定的策略更新。为防止训练偏差，在损失计算阶段会屏蔽所有检索到的文档片段和案例经验。

该框架的创新点在于：1) 提出了一个从原始轨迹中自动提取、抽象和提炼层次化经验知识的自演化机制；2) 设计了动态的经验对齐引导策略，将内生经验知识无缝集成到强化学习训练中，以正则化随机探索；3) 整体上超越了仅依赖外部知识或静态奖励的传统方法，实现了更高效、更稳定的搜索代理训练。

### Q4: 论文做了哪些实验？

论文在多个复杂的数据集和基准测试上进行了广泛的实验。实验设置方面，主要基于Qwen2.5系列模型（如7B和32B的Instruct模型），使用FSDP和vLLM在VeRL框架中进行训练，采样温度设为1.0，top-p为0.95，最大响应长度为8192。搜索工具结合了基于multilingual-e5-base模型的本地检索器（使用2018年维基百科语料库）和Tavily网络搜索工具。

使用的数据集和评估指标包括：1）六个多跳问答数据集（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle、MoreHopQA、Frames），其中前三个为域内数据集，后三个用于评估泛化性能，评估指标采用F1分数、CEM和EM，复杂任务还使用了LLM-as-Judge；2）六个数学推理基准（AIME 2024/2025、AMC、MATH-500、Minerva、OlympiadBench），对样本量少的基准报告Avg@32，其他使用Pass@1。

对比方法包括：先进的RAG方法、RL-based智能搜索模型（如GRPO、GSPO）以及前沿大语言模型（如DeepSeek-R1、GPT-4.1、Gemini-2.5-Pro等）。

主要结果如下：在数学推理任务上，HiExp在GRPO训练中结合时，相比基础模型平均提升17.4分（例如在AIME25上从16.7提升至23.3）。在多跳问答任务上，HiExp与不同RL算法结合均带来显著提升：与GRPO结合时，平均CEM从49.6提升至57.9（提升8.3分）；与GSPO结合时，平均CEM从52.8提升至58.9（提升6.1分）。此外，仅推理阶段使用HiExp（无需训练）也能带来稳定增益，如在Search-o1提示基础上，平均CEM从35.9提升至41.0。实验还表明，使用7B小模型结合HiExp可以达到或超越GPT-4.1等前沿大模型的性能，并展现出优秀的跨任务、跨算法和跨环境泛化能力以及训练稳定性。

### Q5: 有什么可以进一步探索的点？

本文提出的HiExp框架在提升搜索代理性能和训练稳定性方面成效显著，但其局限性也为未来研究指明了方向。核心局限在于其“半解耦”设计：分层经验的构建与后续策略优化是分离的，这导致从初始策略模型中提炼的指导知识是静态的，可能无法与模型在训练中动态演进的能力保持同步。随着智能体通过强化学习内化更复杂的推理模式，静态经验可能无法有效应对更高阶的挑战。

因此，首要的未来方向是构建一个动态的闭环系统，实现经验构建与模型训练的紧密耦合。例如，可以探索在线或增量式的经验更新机制，使经验知识能够伴随策略的优化而实时演进。此外，当前框架主要基于对比分析和聚类来提取经验，未来可研究如何更精细地量化与融合不同层次经验的价值，或引入元学习机制，让智能体学会在不同任务情境下自主选择与调整经验的使用策略。另一个值得探索的点是，将此类经验驱动框架与更广泛的工具使用、多模态交互等场景结合，检验其泛化能力并探索新的知识表示与迁移形式。

### Q6: 总结一下论文的主要内容

该论文针对当前基于强化学习的搜索智能体依赖随机探索导致训练低效和不稳定的问题，提出了一种名为HiExp的分层经验框架。其核心贡献在于通过对比分析和多级聚类机制，从原始推理轨迹中自主提炼出层次化的经验知识，从而将随机的探索过程转化为战略性的、经验驱动的搜索。方法上，HiExp通过内省和凝聚聚类合成元知识，构建经验先验，并在训练中利用经验对齐来正则化策略优化。实验表明，该框架在多个复杂搜索和数学推理基准上显著提升了性能，同时展现出强大的跨任务和跨算法泛化能力，有效增强了策略优化的稳定性与效果。
