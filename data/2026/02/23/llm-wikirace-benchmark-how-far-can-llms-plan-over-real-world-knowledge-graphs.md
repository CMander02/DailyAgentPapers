---
title: "LLM-WikiRace Benchmark: How Far Can LLMs Plan over Real-World Knowledge Graphs?"
authors:
  - "Juliusz Ziomek"
  - "William Bankes"
  - "Lorenz Wolf"
  - "Shyam Sundhar Ramesh"
  - "Xiaohang Tang"
  - "Ilija Bogunovic"
date: "2026-02-18"
arxiv_id: "2602.16902"
arxiv_url: "https://arxiv.org/abs/2602.16902"
pdf_url: "https://arxiv.org/pdf/2602.16902v3"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Benchmark"
  - "Planning"
  - "Reasoning"
  - "World Knowledge"
  - "Knowledge Graph"
  - "Long-Horizon Task"
  - "Evaluation"
relevance_score: 8.0
---

# LLM-WikiRace Benchmark: How Far Can LLMs Plan over Real-World Knowledge Graphs?

## 原始摘要

We introduce LLM-Wikirace, a benchmark for evaluating planning, reasoning, and world knowledge in large language models (LLMs). In LLM-Wikirace, models must efficiently navigate Wikipedia hyperlinks step by step to reach a target page from a given source, requiring look-ahead planning and the ability to reason about how concepts are connected in the real world. We evaluate a broad set of open- and closed-source models, including Gemini-3, GPT-5, and Claude Opus 4.5, which achieve the strongest results on the easy level of the task and demonstrate superhuman performance. Despite this, performance drops sharply on hard difficulty: the best-performing model, Gemini-3, succeeds in only 23\% of hard games, highlighting substantial remaining challenges for frontier models. Our analysis shows that world knowledge is a necessary ingredient for success, but only up to a point, beyond this threshold, planning and long-horizon reasoning capabilities become the dominant factors. Trajectory-level analysis further reveals that even the strongest models struggle to replan after failure, frequently entering loops rather than recovering. LLM-Wikirace is a simple benchmark that reveals clear limitations in current reasoning systems, offering an open arena where planning-capable LLMs still have much to prove. Our code and leaderboard available at https:/llmwikirace.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型在真实世界知识图谱上进行长程规划和推理的能力评估不足的问题。研究背景是，尽管大语言模型在诸多结构化或合成环境的规划基准测试中表现出色，并因大规模预训练（尤其是维基百科等百科全书数据）而具备了丰富的世界知识，但现有评估大多局限于状态和动作空间有限的环境，未能充分检验模型在语义丰富、不确定性高的真实世界信息空间（如庞大的维基百科超链接网络）中，如何利用所学知识进行规划、推理和适应。

现有方法的不足在于，它们未能捕捉现实知识环境的复杂性和部分可观测性，无法有效区分模型是依赖知识记忆还是真正的多步推理与规划能力。因此，本文的核心问题是：大语言模型在多大程度上能利用其预训练的世界知识，在大型、真实的开放域知识环境中进行有效的多步规划、语义推理和策略调整？为了探究此问题，论文引入了LLM-WikiRace基准测试，模拟维基百科页面间的导航游戏，要求模型在仅能观察到当前页面及链接的部分信息下，通过一系列步骤从源页面规划路径至目标页面。该任务旨在评估模型协调长程规划、语义推理和世界知识运用的综合能力，并特别关注其在初始计划失败后重新规划和适应恢复的薄弱环节。通过分析不同难度下的性能差异和轨迹行为，论文揭示了当前前沿模型在知识充足时仍受限于规划与重新规划能力，从而明确了从“知识受限”到“规划受限”的瓶颈转变。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：**经典规划基准**、**现实与开放域规划基准**以及**知识图谱导航**。

在**经典规划基准**方面，相关工作包括PlanBench以及Blockworld、Sudoku等结构化游戏环境。这些研究旨在评估LLMs在受限、形式化领域中的规划能力，但对其是否进行真正的规划而非模式匹配存在争议。本文的LLM-WikiRace与之不同，它专注于**长视野规划**，并强调在单一文本模态中结合世界知识。

在**现实与开放域规划**方面，近期研究趋向于将规划嵌入更自然的任务中，例如旅行行程规划、个人日程安排，以及在解决编码问题等智能体框架中的规划任务。本文的基准与这一方向一致，追求现实性，但其独特之处在于任务核心是**在真实世界知识图谱（维基百科超链接网络）上进行导航**，这要求模型必须利用关于概念间实际联系的开放域知识进行多步推理。

此外，虽然未在提供章节中详述，但本文工作也与**知识图谱问答或导航**的研究相关。LLM-WikiRace的特别贡献在于，它创建了一个简洁的测试平台，将世界知识与前瞻性规划需求紧密结合，并通过难度分级清晰揭示了当前前沿模型在复杂规划与失败后重新规划能力上的显著不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个结构化的评估环境来解决LLM在真实知识图谱上进行多步规划的问题。其核心方法是设计了一个基于维基百科超链接图的基准测试LLM-WikiRace，将复杂的网页导航任务转化为一个受控的、可评估的序列决策问题。

整体框架上，论文首先对原始的WikiRace游戏进行了关键简化，以适应LLM代理的评估。主要模块包括：1）一个固定的、由549,232个页面组成的维基百科超链接图环境（取自2025年6月的快照，并保留最大强连通分量以确保连通性）；2）一个结构化的提示模板，在每一步向LLM明确提供当前页面、目标页面、访问历史以及可供选择的出站链接列表；3）一个定义了三种难度级别（简单、中等、困难，分别对应最优路径长度为3-4、5-6、7-8）的测试实例集。

关键技术设计体现在几个方面。首先，为了控制提示长度和计算成本，论文在每一步将动作空间限制为50个出站链接。这50个链接是根据其到目标页面的最短路径距离（由环境内部计算，不透露给模型）筛选出的最短路径最近的链接，并以随机顺序呈现。这一设计既大幅降低了评估开销（尤其是在困难实例上），又保留了任务对规划和世界知识的需求本质。其次，设定了固定的每轮最大步数（30步），这为代理提供了至少三倍于最优路径长度的预算，确保评估聚焦于规划能力而非时间不足。最后，交互流程被标准化：LLM代理从源页面开始，根据提示反复选择一个链接进行跳转，直到抵达目标或步数耗尽。

创新点在于：1）通过结构化提示和受限动作空间，将开放域的知识图谱导航转化为一个可重复、可量化的基准测试；2）基于最短路径长度明确定义了难度分级，从而能够细致分析模型在不同规划复杂度下的表现差异；3）环境设计巧妙——利用内部计算的最短路径信息来筛选动作选项，但这信息本身不提供给模型，从而在保证评估可行性的同时，不泄露解题线索，确保了任务挑战的真实性。

### Q4: 论文做了哪些实验？

论文在LLM-WikiRace基准上进行了广泛的实验。实验设置方面，评估了包括闭源模型（如GPT-5、Gemini 3、Claude Opus 4.5、Grok 4.1-Fast）和开源模型（如DeepSeek R1、Kimi K2、LLaMA 3系列、Gemma 3系列）在内的多种大语言模型。模型需要在给定的30步限制内，通过维基百科超链接从源页面逐步导航到目标页面。

数据集/基准测试是基于维基百科超链接图构建的LLM-WikiRace，任务难度分为Easy、Medium和Hard三个等级，通过最短路径长度进行分层。主要评估指标包括成功率（在步数限制内完成游戏的比例）和次优步数（成功游戏中超出最短路径的额外步数平均值）。此外，还报告了每步生成的令牌数和闭源模型的货币成本。

对比方法涵盖了不同模型家族和规模的广泛比较。主要结果显示，性能随难度显著分化：领先模型在Easy级别成功率超过90%（如Gemini 3达95%），在Medium级别约为50-70%（Gemini 3为66%），在Hard级别则低于25%（Gemini 3最佳，为23%）。关键数据指标包括：Gemini 3在Easy级别的次优步数为0.8，GPT-5在Hard级别成功率为15%，Claude Opus 4.5在Hard级别为18%。开源模型中DeepSeek R1表现最佳，在Hard级别成功率达17%。

论文还进行了深入分析实验：1）世界知识探测实验，构建了1k个页面连接性分类任务，发现世界知识是必要的，但超越一定阈值后，规划能力成为主导因素；2）轨迹分析，发现即使最强模型（如Gemini 3）在失败后也难以重新规划，在66%的检查轨迹中出现循环，且循环频率与成功率呈强负相关（回归系数-1.02）；3）微调实验，使用DAPO对Qwen-2.5-7B进行微调，在Easy级别成功率从22.5%提升至67.5%，但在Hard级别无改善；4）人类对比实验，发现顶级模型在人类游戏语料库上成功率可达100%，优于人类的98.5%。

### Q5: 有什么可以进一步探索的点？

基于论文分析，当前LLM在真实世界知识图谱上的规划能力仍存在明显局限，未来可从以下几个方向深入探索：

首先，**提升长视野规划与动态重规划能力**是核心挑战。论文指出，即使在困难任务中意识到陷入循环，模型也缺乏有效的策略调整机制。未来可研究更显式的规划架构，如集成蒙特卡洛树搜索（MCTS）或强化学习中的分层规划方法，使模型能评估多步后果并灵活调整路径。

其次，**知识表征与规划的解耦与协同**值得探索。论文发现世界知识达到一定阈值后，规划能力成为瓶颈。可尝试将知识图谱结构显式注入模型（如通过检索增强或图神经网络），让LLM专注于规划决策，而非依赖参数化记忆，这可能提升中小模型在困难任务上的表现。

再者，**基准本身可进一步扩展和细化**。当前任务基于最短路径，未来可引入多目标规划、带约束的路径查找（如避开特定类别）或动态变化的知识图谱，以评估更复杂的现实场景。同时，需设计更细粒度的评估指标，如重规划效率、探索-利用平衡等。

最后，**训练方法的创新**是关键。论文中简单的强化学习微调对困难任务提升有限，未来需开发针对长序列决策的算法，例如结合课程学习从易到难训练，或采用反事实推理来学习从失败中恢复的策略。这些方向有望推动LLM在复杂知识空间中的规划能力迈向新台阶。

### Q6: 总结一下论文的主要内容

该论文提出了LLM-Wikirace基准测试，旨在评估大语言模型在真实世界知识图谱上的规划、推理和世界知识能力。核心问题是要求模型从维基百科的给定源页面出发，通过一步步点击超链接，高效导航至目标页面，这需要模型具备前瞻性规划和理解现实概念关联的能力。

论文的主要贡献在于构建了一个简单而深刻的评估框架，将任务分为简单和困难两个难度等级。方法上，作者评估了包括Gemini-3、GPT-5和Claude Opus 4.5在内的一系列开源和闭源模型。研究发现，前沿模型在简单任务上表现出色甚至超越人类，但在困难任务上性能急剧下降（最佳模型Gemini-3成功率仅23%）。

主要结论指出，世界知识是成功的必要条件，但仅达到一定阈值；超过该阈值后，长期规划和推理能力成为主导因素。轨迹分析进一步揭示，即使最强模型在失败后也难以重新规划，常陷入循环。该基准清晰地揭示了当前推理系统的局限性，为规划能力强的LLMs提供了一个有待证明的开放竞技场。
