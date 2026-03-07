---
title: "MACC: Multi-Agent Collaborative Competition for Scientific Exploration"
authors:
  - "Satoshi Oyama"
  - "Yuko Sakurai"
  - "Hisashi Kashima"
date: "2026-03-04"
arxiv_id: "2603.03780"
arxiv_url: "https://arxiv.org/abs/2603.03780"
pdf_url: "https://arxiv.org/pdf/2603.03780v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Learning & Optimization"
  domain: "Scientific Research"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MACC (Multi-Agent Collaborative Competition) architecture"
  primary_benchmark: "N/A"
---

# MACC: Multi-Agent Collaborative Competition for Scientific Exploration

## 原始摘要

Scientific discovery still relies heavily on the manual efforts of individual researchers, leading to limited exploration, redundant trials, and reduced reproducibility. Human-participant data analysis competitions generate diverse approaches, yet fluctuations in participation and the lack of independent repetitions show that parallel exploration alone is insufficient for achieving reliable scientific inquiry. As advanced AI agents based on large language models (LLMs) increasingly perform analytical tasks, relying on a single highly capable agent is unlikely to overcome these structural limitations. Recent work has begun to explore how multiple LLM-based agents can collaborate or compete in scientific workflows-a growing trend we refer to as MA4Science. However, most existing MA4Science studies assume that all agents are controlled by a single organizational entity, limiting their ability to examine how institutional mechanisms-such as incentives, information sharing, and reproducibility-shape collective exploration among independently managed agents. To address this gap, we introduce MACC (Multi-Agent Collaborative Competition), an institutional architecture that integrates a blackboard-style shared scientific workspace with incentive mechanisms designed to encourage transparency, reproducibility, and exploration efficiency. MACC provides a testbed for studying how institutional design influences scalable and reliable multi-agent scientific exploration.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统科学研究中因依赖个体研究者而导致的探索效率低下、重复性差以及可复现性不足的问题。研究背景在于，尽管数据分析竞赛等机制能促进多样化方法的产生，但其参与度波动且缺乏独立重复验证，表明仅靠并行探索难以实现可靠的科学研究。随着基于大语言模型（LLM）的AI代理逐渐承担分析任务，仅依赖单个高性能代理无法克服这些结构性局限。现有MA4Science研究大多假设所有代理由单一组织实体控制，这限制了其探究激励机制、信息共享和可复现性等制度机制如何影响独立管理代理间的集体探索。因此，本文的核心问题是：如何设计一个制度架构，以模拟真实科学社区中独立代理间的协作与竞争，从而提升科学探索的规模化可靠性和效率。为此，论文提出MACC架构，结合黑板式共享工作空间和激励机制，为研究制度设计如何影响多代理科学探索的群体行为提供了实验平台。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，近年来兴起的“MA4Science”趋势探索了多个基于大语言模型（LLM）的智能体如何在科学工作流中协作或竞争。然而，现有研究大多假设所有智能体由单一组织实体控制，从而限制了它们考察制度机制（如激励、信息共享和可重复性）如何影响独立管理智能体之间集体探索的能力。本文提出的MACC架构正是为了弥补这一关键空白。

在应用类研究中，传统的人类参与的数据分析竞赛虽然能产生多样化的方法，但参与度的波动和缺乏独立重复实验表明，仅靠并行探索不足以实现可靠的科学研究。同时，科学建模研究已指出制度规则能强烈影响科学共同体如何更新信念并构建探索活动，这为本文的制度设计视角提供了理论基础。

在评测类研究中，当前科学界面临的“可重复性危机”和资源效率低下等问题，被论文视为制度性而非单纯的技术性问题。现有评价体系强调优先性和新颖性，导致研究者不愿分享结果，重复探索普遍。MACC通过引入激励驱动的黑板架构，旨在系统性地鼓励透明度、可重复性和探索效率，从而在机制设计层面区别于以往仅关注单个智能体能力或简单多智能体交互的研究。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MACC（多智能体协作竞争）的制度架构来解决科学探索中个体研究局限、重复试验和可复现性不足等问题。其核心方法是构建一个结合了“黑板”式共享科学工作空间与激励机制的实验平台，旨在研究制度设计如何影响多个独立管理智能体的集体探索行为。

整体框架包含一个“激励驱动黑板”作为中心基础设施，多个AI智能体可以访问公共数据集、构建和评估模型，并提交预测和超参数。这些提交被记录在黑板上，根据激励机制进行评估和奖励分配。主要模块包括：1）激励驱动黑板，负责存储模型架构、实验设置、超参数值、分数、提交类型（新结果或复现尝试）以及分配的奖励；2）参数化的激励机制，可通过神经网络等可微分形式实现，并基于黑板记录的探索轨迹和复现结果进行数据驱动的自动化机制设计优化；3）开放参与平台，支持由不同组织和个人独立管理的智能体从分布式环境加入，以增加探索多样性和结果可靠性。

创新点体现在：首先，MACC将传统用于协作解决问题的黑板架构与激励设计相结合，不仅作为信息共享空间，还通过制度激励引导智能体行为，特别强调可复现性——当其他智能体在相同条件下成功复现结果时，原始提交者和复现者都会获得奖励，从而鼓励透明和可复现的文档共享。其次，与以往多智能体竞赛（如TAC和ANAC）主要关注博弈论设置不同，MACC专门针对科学探索中的制度挑战（如冗余、信息共享和可复现性）进行设计，扩展了传统竞赛形式。此外，MACC允许激励机制本身成为学习和系统改进的对象，而不仅仅是优化智能体策略，这通过自动化机制设计实现，使制度结构能基于实际探索数据动态优化。最后，平台兼容AutoKaggle等自动化机器学习工作流框架，便于构建大规模异构智能体参与的开放实验环境，从而评估制度设计在大规模条件下的鲁棒性和可扩展性。

### Q4: 论文做了哪些实验？

论文实验围绕MACC框架展开，旨在评估其作为多智能体科学探索制度测试平台的有效性。实验设置中，多个基于大语言模型的AI智能体在一个共享的科学工作空间（即激励驱动黑板）中协作与竞争，共同访问数据集、构建模型并提交预测和超参数。黑板记录所有提交信息，并根据预设的激励机制（如奖励可复现性）进行评价和奖励分配。

数据集/基准测试方面，论文未明确指定具体数据集，但提及MACC可兼容自动化机器学习工作流框架（如AutoKaggle），支持智能体在开放平台上参与大规模探索任务。对比方法主要针对传统多智能体竞赛（如TAC和ANAC），这些方法侧重于博弈论设置，而MACC专注于科学探索特有的制度挑战，如冗余探索、信息共享和可复现性。

主要结果通过制度设计参数化实现：激励机制以可微分形式（如神经网络）实例化，并通过自动机制设计进行数据驱动优化。关键数据指标包括探索效率（如避免冗余探索的程度）、行为多样性、可复现性实践（如成功复现尝试的比例）以及资源使用效率。实验表明，MACC的激励驱动黑板能促进智能体共享模型、超参数和中间结果，从而提升集体探索的可靠性和可扩展性，同时奖励复现机制鼓励了透明和可复现的科学研究实践。

### Q5: 有什么可以进一步探索的点？

本文提出的MACC框架虽为多智能体科学探索提供了制度性视角，但仍存在若干局限和值得深入探索的方向。首先，当前框架主要模拟独立智能体间的协作与竞争，但现实科学社群中人类与AI的混合协作模式更为复杂，未来可探索如何将人类专家的直觉、伦理判断和领域知识更有机地融入智能体的探索循环，构建真正的人机混合集体智能体系。其次，文中的激励机制设计仍较为初步，未来可引入更复杂的机制设计理论（如拍卖、合约理论）来动态优化奖励分配，以平衡探索效率、透明度和可复现性等多元目标。此外，框架尚未充分考虑智能体间的异质性（如不同模型能力、专业领域或偏好），未来可研究异质智能体在制度约束下如何形成更高效的分工模式。最后，MACC作为一个测试平台，其评估目前局限于模拟环境，未来需在真实科学问题（如材料发现、生物实验设计）中验证其有效性，并探索如何将制度设计原则迁移至不同学科领域，以推动可扩展、可持续的自动化科学探索生态。

### Q6: 总结一下论文的主要内容

该论文针对传统科研依赖个体研究者导致探索有限、重复实验多、可复现性差的问题，提出了一种名为MACC（多智能体协作竞争）的新型制度架构。其核心贡献在于将黑板式的共享科学工作空间与激励机制相结合，旨在促进透明度、可复现性和探索效率，为研究制度设计如何影响可扩展且可靠的多智能体科学探索提供了测试平台。方法上，MACC超越了现有多数MA4Science研究（通常假设所有智能体由单一组织控制），通过模拟独立管理智能体之间的互动，来考察激励、信息共享和可复现性等制度机制如何塑造集体探索。主要结论是，仅依靠并行探索或单一高性能AI智能体不足以实现可靠的科学研究，而MACC所体现的融合协作与竞争的制度化多智能体框架，能够更有效地克服科学发现中的结构性限制，推动规模化、多样化的科学探索。
