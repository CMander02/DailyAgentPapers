---
title: "Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate"
authors:
  - "Cunda Wang"
  - "Ziying Ma"
  - "Po Hu"
  - "Weihua Wang"
  - "Feilong Bao"
date: "2026-04-15"
arxiv_id: "2604.13551"
arxiv_url: "https://arxiv.org/abs/2604.13551"
pdf_url: "https://arxiv.org/pdf/2604.13551v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "多智能体协作"
  - "知识图谱对齐"
  - "LLM推理"
  - "多智能体辩论"
  - "实体对齐"
  - "Agent架构"
relevance_score: 8.0
---

# Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate

## 原始摘要

Entity alignment (EA) aims to identify entities referring to the same real-world object across different knowledge graphs (KGs). Recent approaches based on large language models (LLMs) typically obtain entity embeddings through knowledge representation learning and use embedding similarity to identify an alignment-uncertain entity set. For each uncertain entity, a candidate entity set (CES) is then retrieved based on embedding similarity to support subsequent alignment reasoning and decision making. However, the reliability of the CES and the reasoning capability of LLMs critically affect the effectiveness of subsequent alignment decisions. To address this issue, we propose AgentEA, a reliable EA framework based on multi-agent debate. AgentEA first improves embedding quality through entity representation preference optimization, and then introduces a two-stage multi-role debate mechanism consisting of lightweight debate verification and deep debate alignment to progressively enhance the reliability of alignment decisions while enabling more efficient debate-based reasoning. Extensive experiments on public benchmarks under cross-lingual, sparse, large-scale, and heterogeneous settings demonstrate the effectiveness of AgentEA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的实体对齐（EA）方法中存在的两个关键问题：候选实体集（CES）检索的可靠性不足，以及单一路径LLM推理的局限性。研究背景是，随着多源、多语言异构知识图谱（KG）的普及，实体对齐成为整合知识的关键任务。传统基于知识表示学习（KRL）的方法依赖嵌入相似度，但缺乏对语义、结构和属性一致性的显式建模与复杂推理能力，难以可靠区分语义相似但实际未对齐的实体。

现有LLM-based EA方法虽然利用LLM的语义理解和推理能力弥补了KRL的不足，但其性能受到两大制约。首先，它们通常依赖嵌入相似度的启发式阈值来筛选“对齐不确定实体集”（AES）并检索CES，但相似度分布不稳定可能导致真正模糊的实体被排除在推理之外，而错误对齐未被挑战。更重要的是，若真实对齐实体不在CES中，无论LLM推理能力多强，都无法做出正确对齐，导致其Hit@1性能本质上受限于KRL检索的Hit@20性能。其次，现有方法依赖单次、无挑战的LLM推理轨迹，缺乏对替代假设或反证的显式支持，在证据不完整或误导时无法修正结论，容易产生系统性错误，如拒绝真实对齐。

因此，本文的核心问题是：如何突破候选检索可靠性的上限约束，并增强对齐决策的鲁棒性与可靠性。为此，论文提出了AgentEA框架，通过嵌入质量优化和两阶段多智能体辩论机制来协同解决上述问题。具体而言，它引入实体表示偏好优化模块来提升嵌入质量，并设计包含轻量级辩论验证和深度辩论对齐的两阶段多角色辩论，以渐进方式增强对齐决策的可靠性，同时实现更高效的基于辩论的推理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：知识表示学习（KRL）的实体对齐方法、基于大语言模型（LLM）的实体对齐方法，以及多智能体辩论（MAD）技术。

在**KRL-based对齐方法**中，早期工作如MTransE、IPTransE和TransEdge基于翻译模型学习实体嵌入，后续方法如HGCN、AliNet、RHGN和LGEA引入图神经网络以更好地捕捉结构信息。这些方法主要依赖结构驱动的表示学习，但在语义模糊或图结构不完整时效果受限。本文的AgentEA框架首先通过实体表示偏好优化提升嵌入质量，继承了这类方法的基础，但进一步利用LLM的语义能力弥补其不足。

在**LLM-based对齐方法**中，ChatEA和MM-ChatAlign将图结构转化为代码式表示输入LLM；EasyEA和ProLEA通过知识总结激活背景知识；Seg-Align和LLM4EA探索零样本能力。这些方法通常依赖单一LLM直接决策，缺乏多视角验证机制，易受不确定性或偏差影响。本文与之区别在于引入了多智能体辩论机制，通过两阶段辩论（轻量级验证与深度对齐）显式集成多视角推理，提升了决策的稳定性和可靠性。

在**多智能体辩论**领域，现有工作如MRBalance、MAD-AWSD等侧重角色异质性以增强观点多样性，BELLE等研究则设计辩论结构以提升推理稳定性。本文的AgentEA框架综合了这两方面，设计了两阶段多角色辩论机制，从快速验证到深度对齐逐步推进，在提升推理效率的同时确保了对齐决策的可靠性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentEA的、基于多智能体辩论的可靠实体对齐框架来解决候选实体集（CES）可靠性和大语言模型（LLMs）推理能力对对齐决策有效性的关键影响问题。其核心方法是一个两阶段多角色辩论机制，整体框架包括实体表示偏好优化、轻量级辩论验证和深度辩论对齐三大模块。

首先，为了提升嵌入质量和候选实体集的可靠性，论文设计了**实体表示偏好优化**模块。该模块采用直接偏好优化（DPO）方法，对一个基于LLaMA的编码器进行微调，以获得更具判别力的实体嵌入。其创新点在于构建了两种困难的负样本：基于误导性名称相似性的负样本和基于邻域度信息的负样本，从而让模型学习区分语义或结构上容易混淆的实体对，为后续检索提供更高质量的嵌入。

其次，框架的核心是**两阶段多角色辩论对齐**。第一阶段是**轻量级辩论验证**，旨在通过低成本的多智能体推理高效验证和过滤候选实体。它采用单轮辩论机制，由对齐支持者、对齐反对者和对齐裁判三个角色组成。在辩论前，通过基于频率的策略压缩实体描述信息，大幅减少输入令牌数。裁判综合各方观点对候选实体重新排序，并基于一致性验证更新“不确定实体集”，将计算资源聚焦于后续真正困难的案例上，在效率和可靠性间取得平衡。

第二阶段是**深度辩论对齐**，对剩余的不确定实体进行细粒度区分。其架构设计更具创新性：1）**多角色设计**：包含从实体名称、类型、属性和邻域结构等不同角度分析的专业智能体，以及一个负责挑战其他智能体判断的攻击者角色和一个负责汇总证据、管理流程的裁判角色。2）**多轮交互式辩论**：采用迭代的纠错策略，智能体可以访问前一轮的完整辩论输出，攻击者整合专业智能体的分数并对高风险候选施加更细粒度的惩罚，裁判则决定是否触发候选集扩展。3）**渐进式候选集扩展策略**：为了控制计算成本，并非对所有候选进行辩论，而是根据分数排名构建多个候选子集（如前5、10、15、20名），并在满足特定条件（如Top-1分数低、支持对齐的投票比例低且裁判判断为假）时，才动态扩展候选集进行更广泛的考察。4）**灵活的终止机制**：辩论可在早期达成可靠决策时提前终止（如Top-1与Top-2分数差距大或支持对齐投票过半且裁判判断为真），或在达到最大轮数时强制终止，确保过程可控。

总之，AgentEA通过嵌入优化提升检索基础，再通过一个由轻量验证（快速过滤）和深度对齐（精细辨析）构成的渐进式、多视角辩论框架，系统性地增强了实体对齐决策的可靠性和鲁棒性。

### Q4: 论文做了哪些实验？

论文在多个实体对齐基准数据集上进行了系统实验。实验设置方面，研究在11个广泛使用的基准数据集上进行，包括DBP15K（跨中文-英文、日文-英文、法文-英文）、ICEWS（WIKI、YAGO）、DWY（DBP-WIKI、DBP-YAGO）以及SRPRS（英文-德文、英文-法文等）。评估指标采用Hits@K和平均倒数排名（MRR）。所有实验在单个NVIDIA A100 GPU上运行，在嵌入检索阶段使用LLaMA3-8B-Instruct模型并采用直接偏好优化进行微调，相似度阈值δ₁设为0.05；在辩论阶段使用gpt-3.5-turbo作为骨干大语言模型，最大辩论轮数设为3，阈值δ₂为0.5。

对比方法分为基于知识表示学习的方法（如MTransE、GCN-Align、BootEA、RDGCN、Dual-AMN、SCMEA等）和基于大语言模型的方法（如LLMEA、ChatEA、Seg-Align、EasyEA、ProLEA、AdaCoAgentEA等）。主要结果显示，AgentEA在所有数据集和指标上均一致优于现有方法。例如在DBP15K的ZH-EN、JA-EN、FR-EN数据集上，其Hits@1分别达到0.970、0.984、0.996，MRR分别达到0.974、0.987、0.998；在DWY（DBP-WIKI）和SRPRS（DBP-YAGO）数据集上甚至取得了多项1.00的完美分数，展现了卓越的对齐稳定性。

消融实验验证了关键组件的有效性：移除直接偏好优化（w/o DPO）导致性能大幅下降（如FR-EN上Hits@1从0.996降至0.859）；移除辩论机制（w/o Debate）使Hits@1从0.996降至0.976；移除深度辩论对齐（w/o DDA）或各功能代理（如属性、别名代理）均会造成不同程度性能下降。效率分析表明，两阶段辩论框架在性能与计算开销间取得了良好平衡，轻量级辩论验证能有效提升效率。此外，实验还表明AgentEA对底层大语言模型的选择不敏感，且在多数情况下三轮辩论即可达到最佳性能。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了几个明确的探索方向。首先，在效率方面，尽管采用了轻量级与深度辩论的两阶段设计，但深度辩论对齐阶段的计算开销在大规模知识图谱上依然显著。未来可探索更动态的辩论调度机制，例如基于实体不确定性或候选集质量的**自适应早期停止策略**，或引入**层级化辩论**，仅对最棘手的案例进行深度推理，以进一步提升可扩展性。

其次，框架的可靠性受限于基于嵌入的候选检索质量。一个重要的改进方向是开发**检索与推理的联合优化机制**。例如，可以设计一个迭代过程，让辩论中产生的推理反馈（如实体间复杂关系）动态地修正或扩展候选实体集，从而打破检索错误的瓶颈。

最后，辩论中智能体的角色和提示模板目前依赖人工设计。未来研究可以探索**元学习或自动化提示工程**，使系统能够根据具体知识图谱的特性（如稀疏性、异质性）自动配置或演化出最优的辩论角色与协作策略，从而减少人工启发式设计的依赖，增强方法的普适性与自适应性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为AgentEA的可靠实体对齐框架，旨在解决知识图谱（KGs）中实体对齐任务面临的候选集可靠性及大语言模型（LLMs）推理能力不足的问题。其核心贡献在于将实体表示偏好优化与两阶段多智能体辩论机制相结合，以提升对齐决策的稳定性和准确性。

具体方法上，首先通过基于直接偏好优化（DPO）的微调来改进实体嵌入质量，从而优化候选实体集（CES）的可靠性。随后，引入两阶段多角色辩论机制：第一阶段为轻量级辩论验证，快速筛选候选；第二阶段为深度辩论对齐，通过多智能体深入辩论逐步增强对齐决策的可信度，同时保持较高的推理效率。

实验结果表明，AgentEA在跨语言、稀疏、大规模及异构等多种公开基准设置下均表现出显著有效性和鲁棒性，能够稳定提升实体对齐的准确性，为基于LLMs的实体对齐方法提供了更可靠的解决方案。
