---
title: "Learning Virtual Machine Scheduling in Cloud Computing through Language Agents"
authors:
  - "JieHao Wu"
  - "Ziwei Wang"
  - "Junjie Sheng"
  - "Wenhao Li"
  - "Xiangfeng Wang"
  - "Jun Luo"
date: "2025-05-15"
arxiv_id: "2505.10117"
arxiv_url: "https://arxiv.org/abs/2505.10117"
pdf_url: "https://arxiv.org/pdf/2505.10117v3"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM-driven Agent"
  - "Agent Framework"
  - "Decision Making"
  - "Heuristic Design"
  - "Multi-stage Planning"
  - "Cloud Computing Application"
relevance_score: 7.5
---

# Learning Virtual Machine Scheduling in Cloud Computing through Language Agents

## 原始摘要

In cloud services, virtual machine (VM) scheduling is a typical Online Dynamic Multidimensional Bin Packing (ODMBP) problem, characterized by large-scale complexity and fluctuating demands. Traditional optimization methods struggle to adapt to real-time changes, domain-expert-designed heuristic approaches suffer from rigid strategies, and existing learning-based methods often lack generalizability and interpretability. To address these limitations, this paper proposes a hierarchical language agent framework named MiCo, which provides a large language model (LLM)-driven heuristic design paradigm for solving ODMBP. Specifically, ODMBP is formulated as a Semi-Markov Decision Process with Options (SMDP-Option), enabling dynamic scheduling through a two-stage architecture, i.e., Option Miner and Option Composer. Option Miner utilizes LLMs to discover diverse and useful non-context-aware strategies by interacting with constructed environments. Option Composer employs LLMs to discover a composing strategy that integrates the non-context-aware strategies with the contextual ones. Extensive experiments on real-world enterprise datasets demonstrate that MiCo achieves a 96.9\% competitive ratio in large-scale scenarios involving more than 10,000 virtual machines. It maintains high performance even under nonstationary request flows and diverse configurations, thus validating its effectiveness in complex and large-scale cloud environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决云计算环境中虚拟机器（VM）调度这一复杂且动态的优化问题。研究背景是，随着云计算服务的普及和规模扩大，VM调度——即如何高效地将动态到达、具有多维资源需求的VM分配到物理机器（PM）上——已成为一个典型的在线动态多维装箱（ODMBP）问题，其特点是规模庞大、需求波动且未来信息不确定，对云服务提供商的运营效率和成本至关重要。

现有方法存在明显不足。传统优化方法难以适应实时变化；由领域专家设计的启发式方法策略僵化，缺乏灵活性；而现有的基于学习的方法（如强化学习）则常常泛化能力不足且可解释性差。这些方法通常依赖于预定义的规则、静态假设或固定的特征表示，难以捕捉动态离开、上下文异质性和时间非平稳性等演化特征。此外，它们严重依赖人工设计和专家知识，在动态环境中难以实现“一刀切”的普适方案，且维护和适应新模式的成本高昂。

因此，本文要解决的核心问题是：如何设计一个能够自动适应复杂、大规模、非平稳云环境的VM调度框架，以克服现有方法在适应性、泛化性和可解释性方面的局限。为此，论文提出了名为MiCo的分层语言智能体框架，其核心是利用大型语言模型（LLM）驱动的启发式设计范式来自动发现可解释的、与上下文相关的调度规则，从而减少对领域专家探索性工作的依赖，并实现对动态请求模式的鲁棒适应。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统优化与启发式方法、基于学习的方法以及新兴的大语言模型（LLM）应用。

**1. 传统优化与启发式方法**：这是解决在线动态多维装箱（ODMBP）问题的经典途径。优化方法（如线性规划）在离线、已知完整序列时能求得最优解，但在在线动态场景中适应性不足。启发式算法（如First-Fit、Best-Fit）以及工业界系统（如微软的Protean）依赖专家设计的固定规则，虽简单高效，但策略僵化，难以适应动态、非平稳的请求流和多变的环境上下文。

**2. 基于学习的方法（特别是强化学习RL）**：这类方法（如SchedRL）利用RL在在线环境中进行快速决策，能处理大规模问题。然而，它们通常依赖于手工特征工程和特定的环境建模，泛化能力和可解释性有限，在上下文异构和时序非平稳的场景中表现可能不稳定。

**3. 大语言模型（LLM）在运筹与优化中的应用**：近期研究探索将LLM用于问题建模和决策支持，利用其代码生成和推理能力自动合成规则。但现有LLM方法在直接应用于复杂、非平稳的规划问题时存在根本性局限，例如难以直接进行动态环境下的启发式设计。

**本文与这些工作的关系和区别**：本文提出的MiCo框架属于第三类研究的深化与创新。它没有直接使用LLM进行调度，而是**首创了一个基于LLM的启发式设计范式**，并引入了**分层的语言智能体架构**。具体而言，MiCo将问题建模为带选项的半马尔可夫决策过程（SMDP-Option），通过Option Miner和Option Composer两个智能体，分别实现**非上下文感知策略的自动发现**和**基于上下文的策略组合**。这区别于：（a）传统启发式方法，实现了策略的自动生成与动态适配，减少了专家探索成本；（b）传统RL方法，提升了泛化性和可解释性；（c）直接的LLM应用，通过分层结构克服了其在动态环境中适应性差的短板，从而在复杂、大规模云环境中实现了更优且稳健的性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MiCo的分层语言智能体框架来解决虚拟机器（VM）调度问题。该框架的核心是将在线动态多维装箱问题（ODMBP）重新表述为带有选项的半马尔可夫决策过程（SMDP-Option），从而构建一个两阶段的层次化架构：选项挖掘器（Option Miner）和选项组合器（Option Composer）。整体框架旨在分离微观策略发现和宏观策略组合，以应对环境非平稳性和上下文依赖的挑战。

在架构设计上，MiCo首先通过场景生成工具将VM请求流划分为多个近似平稳的上下文片段，每个片段代表不同的需求模式。选项挖掘器负责在每个场景内，利用大语言模型（LLM）驱动的策略优化循环，发现多样且有效的非上下文感知调度策略。具体过程包括策略评估和策略改进两个阶段：LLM根据当前策略的性能评估结果，通过提示工程生成改进后的新策略，迭代优化直至收敛，最终形成一组基础选项策略库。

随后，选项组合器在宏观层面运作，其目标是学习一个主策略，该策略能够根据实时上下文特征（如有限长度的历史状态序列）动态选择最合适的选项。组合器同样采用LLM驱动的优化循环，但输入包含了上下文信息，以学习如何在不同场景间协调和切换选项。为了提升效率，在组合前会对选项库进行剪枝，保留那些在自身场景表现接近最优且在多数其他场景中具有鲁棒性的策略。

关键技术包括：1）将VM调度建模为SMDP-Option，引入了时间抽象，使宏观决策可以跨越多个时间步；2）利用LLM作为启发式策略生成器，通过自然语言交互和推理能力自动设计和优化调度策略；3）分层决策机制，分离了策略发现（微观）和策略组合（宏观），降低了学习复杂度并提高了可解释性；4）基于场景的离线选项挖掘与在线上下文感知组合相结合，有效处理了非平稳请求流。

创新点主要体现在：提出了一个LLM驱动的启发式设计范式，用于解决复杂的ODMBP问题；通过分层选项框架将非平稳环境下的调度分解为可管理的子问题；利用LLM的推理能力自动生成和优化调度策略，减少了对手工启发式规则的依赖，并提高了方法的通用性和适应性。

### Q4: 论文做了哪些实验？

论文实验部分主要包括以下内容：

**实验设置与数据集**：实验使用了两个真实企业数据集。主要数据集是华为云Huawei-East-1数据集，包含约12.5万个虚拟机请求，每个请求具有CPU、内存需求、到达时间和请求类型等属性。该数据集被按时间顺序划分为六个具有不同虚拟机分布特征的场景（例如，场景1以小型虚拟机为主，场景5中型大型虚拟机激增）。每个场景进一步划分为六个等距起点，以前五个起点的序列作为训练集，第六个起点的序列作为测试集，构成5:1的时序划分。此外，还在AzurePublicDatasetV2数据集上进行了验证。

**对比方法**：基线方法包括传统启发式算法和基于学习的方法。具体有：
1.  **传统启发式方法**：Best-Fit（选择当前分配率最高的服务器）、First-Fit（按索引顺序分配到第一个可用服务器）、Hindsight（按生命周期降序排列并分配到最合适的机器）。
2.  **基于学习的方法**：SchedRL（一种利用强化学习进行多NUMA虚拟机调度的框架）。

**主要结果与关键指标**：在涉及超过10,000个虚拟机的大规模场景中，论文提出的MiCo框架达到了**96.9%的竞争比**。实验表明，即使在非平稳请求流和多样化配置下，MiCo仍能保持高性能，验证了其在复杂大规模云环境中的有效性。此外，论文还进行了消融研究和鲁棒性分析，并探究了大语言模型发现的策略是否与传统启发式方法一致。

### Q5: 有什么可以进一步探索的点？

该论文提出的MiCo框架在利用大语言模型设计启发式策略方面具有创新性，但仍存在一些局限性和值得深入探索的方向。首先，其“选项挖掘”阶段依赖于LLM与构建环境的交互来发现无上下文感知的策略，这个过程计算成本高昂且可能受限于预定义的动作空间，未来可研究如何更高效地引导LLM生成策略或引入元学习来加速适应。其次，框架的决策可解释性虽优于黑盒模型，但LLM本身的“幻觉”问题可能影响策略可靠性，需设计更严格的验证机制。此外，实验主要针对CPU和内存资源，现实云环境中的网络、存储等多维约束与异构硬件尚未充分考虑，未来可扩展问题维度。另一个重点是框架的在线学习与持续适应能力，当前工作侧重于离线发现与组合策略，如何在不重训练的前提下让智能体实时适应未知请求模式是一个关键挑战。最后，将此类语言智能体框架与经典优化算法（如基于搜索的方法）更深层次地结合，可能催生更强大且高效的混合求解范式。

### Q6: 总结一下论文的主要内容

本文针对云计算中虚拟机调度的在线动态多维装箱问题，提出了一种名为MiCo的分层语言智能体框架。该框架利用大语言模型驱动启发式设计，以解决传统优化方法难以适应实时变化、启发式方法策略僵化以及现有学习方法泛化性和可解释性不足的问题。

MiCo将问题建模为带选项的半马尔可夫决策过程，采用两阶段架构：选项挖掘器和选项组合器。选项挖掘器利用LLM通过与构建的环境交互，发现多样且有用的非上下文感知策略；选项组合器则利用LLM学习一种组合策略，将非上下文感知策略与上下文信息相结合，实现动态调度。

实验结果表明，在涉及超过1万台虚拟机的大规模场景中，MiCo达到了96.9%的竞争比，即使在非平稳请求流和多样化配置下也能保持高性能。该框架的核心贡献在于为ODMBP问题提供了可自动生成可解释调度规则的LLM驱动新范式，并通过分层架构实现了对复杂动态云环境的高效适应。
