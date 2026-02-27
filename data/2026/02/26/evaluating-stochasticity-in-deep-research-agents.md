---
title: "Evaluating Stochasticity in Deep Research Agents"
authors:
  - "Haotian Zhai"
  - "Elias Stengel-Eskin"
  - "Pratik Patil"
  - "Liu Leqi"
date: "2026-02-26"
arxiv_id: "2602.23271"
arxiv_url: "https://arxiv.org/abs/2602.23271"
pdf_url: "https://arxiv.org/pdf/2602.23271v1"
categories:
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "Agent 架构"
  - "Agent 数据合成/规划/推理"
  - "多智能体系统"
  - "Agent 自演化"
relevance_score: 9.0
---

# Evaluating Stochasticity in Deep Research Agents

## 原始摘要

Deep Research Agents (DRAs) are promising agentic systems that gather and synthesize information to support research across domains such as financial decision-making, medical analysis, and scientific discovery. Despite recent improvements in research quality (e.g., outcome accuracy when ground truth is available), DRA system design often overlooks a critical barrier to real-world deployment: stochasticity. Under identical queries, repeated executions of DRAs can exhibit substantial variability in terms of research outcome, findings, and citations. In this paper, we formalize the study of stochasticity in DRAs by modeling them as information acquisition Markov Decision Processes. We introduce an evaluation framework that quantifies variance in the system and identify three sources of it: information acquisition, information compression, and inference. Through controlled experiments, we investigate how stochasticity from these modules across different decision steps influences the variance of DRA outputs. Our results show that reducing stochasticity can improve research output quality, with inference and early-stage stochasticity contributing the most to DRA output variance. Based on these findings, we propose strategies for mitigating stochasticity while maintaining output quality via structured output and ensemble-based query generation. Our experiments on DeepSearchQA show that our proposed mitigation methods reduce average stochasticity by 22% while maintaining high research quality.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（Deep Research Agents, DRAs）在实际部署中面临的一个关键但被忽视的问题：**输出结果的随机性（stochasticity）**。研究背景是，DRAs作为基于大语言模型的智能体系统，在金融决策、医学分析和科学发现等领域展现出通过自主信息搜集与综合来辅助研究的潜力。尽管现有研究在提升其输出准确性（如存在标准答案时）方面取得了进展，但系统设计往往忽略了随机性这一现实部署的重大障碍。现有方法的不足在于，DRA的执行通常涉及搜索、推理和合成的迭代循环，其中微小的生成或搜索差异会级联放大，导致对同一查询的多次重复执行产生在研究成果、发现和引用上差异巨大的输出。这种不可靠性使得用户（无论是缺乏专业知识的普通用户，还是需要高效自动化工作流的专业用户）难以信任和有效利用DRA，反而可能因需要手动验证而增加负担。

因此，本文要解决的核心问题是：如何**形式化地定义、量化、分析并缓解DRAs中的随机性**。具体而言，论文将DRA建模为信息获取的马尔可夫决策过程，以此为基础提出一个评估框架，从系统层面量化输出方差，并识别出随机性的三个具体来源：信息获取（查询生成）、信息压缩（摘要）和推理。通过研究这些模块在不同决策步骤中引入的随机性如何影响最终输出方差，并基于此提出有效的缓解策略，目标是在保持输出质量的同时，提升DRAs的可靠性和一致性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两类：**深度研究智能体系统**和**评测基准与方法**。

在**深度研究智能体系统**方面，相关工作始于早期的检索增强生成（RAG）系统，其专注于利用外部知识库提升事实性问答的准确性，但通常缺乏生成综合性报告所需的深度推理。后续研究如GPTResearcher引入了智能体工作流，通过查询分解和分层规划来生成长篇内容。更近期的系统（如OpenDeepSearch、Tongyi DeepResearch）则通过交织迭代的“行动-观察”循环与外部工具（如Python执行）来扩展能力。FlashResearch等工作则专注于实时智能体编排以提升效率。这些研究共同推动了AI从被动检索器向能驾驭复杂、多阶段研究任务的自主智能体的演进。**本文与这些工作的关系在于，其研究对象正是这类深度研究智能体（DRA），但区别在于本文不侧重于设计新的系统功能，而是聚焦于被现有系统设计所忽视的一个关键问题：其执行结果的随机性（stochasticity）。**

在**评测基准与方法**方面，早期研究主要使用传统问答（QA）基准来评估检索准确性，但难以衡量综合性研究报告的质量。近期工作引入了专门基准，利用基于内容质量和事实可靠性的指标（如将报告分解为原子性发现、采用LLM-as-a-judge）来评估。也有相关工作针对DRA环境开发了检索忠实度和声明验证的诊断方法，或研究了智能体系统评估本身的随机性并提出了可靠的统计度量。**本文与这些工作的关系在于同属评估范畴，但核心区别在于：现有评测工作主要关注输出内容的“质量”或评估过程的可靠性，而本文首次系统性地提出一个框架，用于量化DRA在不同运行次数下的“随机性”，并将随机性溯源至系统的不同组件，进而提出缓解方法。**

### Q3: 论文如何解决这个问题？

论文通过一个系统的评估框架和针对性的缓解策略来解决深度研究代理（DRA）中的随机性问题。核心方法首先将DRA建模为一个信息获取的马尔可夫决策过程（MDP），从而形式化地分解并识别随机性的三个来源：信息获取（查询生成）、信息压缩（内容摘要）和推理（证据整合与状态更新）。基于此模型，论文设计了一个评估流程，通过多次独立运行DRA，将其输出的答案、发现和引用聚类并向量化，最终计算总方差来量化系统的随机性。

在架构设计上，论文以ReAct等典型DRA框架为实例，其整体运作是一个包含上述三个关键模块的循环。主要模块包括：1) 查询策略（π_query），负责决定何时停止或生成搜索查询；2) 信息压缩策略（π_sum），负责将检索到的大量异构内容提炼为中间表示（如笔记、结构化数据）；3) 推理更新策略（π_update），负责基于新证据更新知识状态（belief state）。环境内核（β_env）虽然也可能引入随机性，但在分析中被假定为固定（例如使用缓存搜索）。

基于控制实验的发现（即推理模块和早期阶段的随机性对最终输出方差影响最大），论文提出了两种创新的缓解策略。第一，针对信息压缩（π_sum）和推理（π_update）模块，引入结构化输出约束，强制模型按照预定义的JSON或Markdown模式生成内容，以减少输出风格的随机变化。实验表明，对推理模块施加此约束比压缩模块更能降低总体随机性。第二，针对信息获取模块（π_query），采用基于共识的集成方法：在早期步骤并行生成N组查询，仅保留其交集作为最终查询行动，以此减少早期查询的随机性；为提高效率，随着步骤推进，N会衰减至1。这两种策略可以组合使用。

实验结果表明，组合使用所有缓解方法能在DeepSearchQA数据集上，在保持甚至提高研究输出准确率（提升12%）的同时，将平均随机性降低22%。这证明了通过算法设计（结构化输出和集成查询）可以有效控制系统随机性而不牺牲质量。

### Q4: 论文做了哪些实验？

论文通过一系列受控实验和消融研究，系统评估了深度研究智能体（DRA）中的随机性。实验设置方面，研究将DRA建模为信息获取马尔可夫决策过程，并引入了一个量化系统方差的评估框架。实验在DeepSearchQA和WebWalkerQA数据集上进行，使用基于通义DeepResearch的ReAct实现，骨干模型为Qwen3-30B-A3B-Instruct-2507（分析实验）和Qwen3-235B-A22B-Instruct-2507-tput（缓解实验）。对比方法主要通过温度参数（λ=0.5和1.0）控制不同策略模块（查询π_query、摘要π_sum、推理更新π_update）在特定步骤（早期、中期、晚期及组合步骤）的随机性，以模拟和分解随机性的来源。

主要结果和关键指标如下：
1.  **随机性分解与传播**：通过模块化消融实验发现，早期步骤引入的随机性对最终输出方差的影响大于晚期步骤，证实了随机性的传播效应。例如，在λ=1.0时，步骤1的查询模块导致答案方差(TV(Y))为0.51，而步骤3的查询模块方差为0.34。
2.  **模块贡献度**：推理更新模块（π_update）对最终输出随机性的贡献最大，高于信息获取（π_query）和压缩（π_sum）模块。在λ=0.5的组合步骤中，更新模块的发现方差(TV(B))高达0.89。
3.  **随机性与质量关系**：更高的随机性并不总带来更高的准确性。例如，λ=1.0、步骤1的查询模块TV(B)为0.80时准确率为0.36，而λ=0.5、组合步骤的更新模块TV(B)为0.89时准确率为0.41。
4.  **指标相关性**：答案（Y）、发现（B）和引用（C）的随机性指标呈强正相关，平均TV值分别为约0.44、0.76和0.44，表明内部发现比外部引用更不稳定。
5.  **缓解策略效果**：提出了结构化输出和基于共识的查询生成等缓解方法。在DeepSearchQA上的实验表明，结合所有方法（Comb.）能将平均随机性（Avg. TV）从基线的0.69降低至0.47（降低22%），同时准确率从0.24提升至0.36。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于仅提出了基于结构化输出和集成查询生成的初步缓解策略，未来可探索更广泛的降随机性方法。例如，可研究如何将确定性更强的检索机制（如基于知识图谱的精确查询）融入信息获取模块，或开发能动态评估并调整随机性水平的自适应控制器。理论分析方面，需建立更严谨的数学模型来量化随机性传播与输出质量间的权衡关系，并探索不同领域任务中随机性的影响差异。此外，实验仅基于DeepSearchQA，未来需在医疗、金融等更复杂场景中验证框架的普适性。结合个人见解，或许可引入因果推断技术区分随机性中的“有益探索”与“有害噪声”，从而设计选择性抑制机制，在保持创新性的同时提升可复现性。

### Q6: 总结一下论文的主要内容

该论文聚焦于深度研究智能体（DRAs）在实际部署中面临的关键挑战——随机性。研究指出，即使面对相同查询，DRAs的多次执行也会在研究结果、发现和引用上产生显著差异，这阻碍了其可靠性。论文的核心贡献在于将DRAs建模为信息获取马尔可夫决策过程，并提出了一个量化系统方差的评估框架，识别出随机性的三个来源：信息获取、信息压缩和推理。

通过控制实验，论文分析了这些模块在不同决策步骤中如何影响输出方差。主要结论表明，降低随机性可以提升研究输出质量，其中推理阶段和早期阶段的随机性对总体方差贡献最大。基于此，作者提出了缓解策略，包括采用结构化输出和基于集成的查询生成方法，以在保持高质量的同时减少随机性。在DeepSearchQA上的实验验证了这些方法的有效性，平均随机性降低了22%，且研究质量得以维持。这项研究为提升DRAs的稳定性和可重复性提供了重要理论基础和实践指导。
