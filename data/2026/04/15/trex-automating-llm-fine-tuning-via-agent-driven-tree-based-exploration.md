---
title: "TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration"
authors:
  - "Zerun Ma"
  - "Guoqiang Wang"
  - "Xinchen Xie"
  - "Yicheng Chen"
  - "He Du"
  - "Bowen Li"
  - "Yanan Sun"
  - "Wenran Liu"
  - "Kai Chen"
  - "Yining Li"
date: "2026-04-15"
arxiv_id: "2604.14116"
arxiv_url: "https://arxiv.org/abs/2604.14116"
pdf_url: "https://arxiv.org/pdf/2604.14116v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multi-Agent System"
  - "Automated Workflow"
  - "LLM Fine-tuning"
  - "Tree-based Planning"
  - "Agent Benchmarking"
  - "Open-Domain Research"
relevance_score: 8.5
---

# TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

## 原始摘要

While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation. The multi-round experimental process is modeled as a search tree, enabling the system to efficiently plan exploration paths, reuse historical results, and distill high-level insights from iterative trials. To evaluate the capability of automated LLM training, we construct FT-Bench, a benchmark comprising 10 tasks derived from real-world scenarios, ranging from optimizing fundamental model capabilities to enhancing performance on domain-specific tasks. Experimental results demonstrate that the TREX agent consistently optimizes model performance on target tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）微调过程自动化这一复杂且资源密集的挑战。研究背景是，尽管LLM本身已成为强大的研究工具，并催生了能够自动化执行机器学习模型优化等闭环研究流程的AI智能体，但LLM自身的训练（尤其是微调）因其开放性和复杂性，尚未被现有自动化方法有效攻克。

现有方法的不足主要体现在两个方面。其一，当前的研究智能体通常处理的是目标明确、可编码为有限文本序列（如结构化参数或代码补丁）的优化问题。然而，LLM微调方案的设计涉及数据分布、算法和超参数等多重因素，尤其是海量训练数据无法直接纳入智能体的上下文，阻碍了自动化方案设计与执行。其二，与可快速验证的算法设计等任务不同，LLM的训练和评估耗时耗力，使得依赖批量生成和验证的进化式框架效率低下甚至不可行。

因此，本文要解决的核心问题是：如何构建一个能够自主管理整个LLM微调生命周期（从需求分析、文献与数据研究、策略制定到数据准备、模型训练与评估）的自动化智能体系统。为此，论文提出了TREX，一个采用多智能体协作和基于树的探索策略的系统，以应对方案设计的开放性和实验验证的高成本挑战，最终实现在有限资源下持续优化模型性能的目标。

### Q2: 有哪些相关研究？

本文的相关工作主要涵盖自动化AI研究、搜索优化、基准评测以及自动化机器学习等类别。

在**自动化AI研究**方面，相关工作包括专注于文献发现的工具（如DeepResearch、RAG）、辅助论文写作与评审的LLM应用，以及能够生成研究想法并实施实验的AI智能体系统（如Dolphin、InternAgent、AI-Scientist系列、AI-Researcher）。特别是AI Scientist v1&v2和AI Researcher等端到端AI研究员系统，已实现了包含想法生成、实验实施和论文撰写的核心研究流程。本文的TREX系统与这些工作的关系在于，它同样致力于自动化科学研究流程，但其**区别**在于具有明确的任务导向（即自动化LLM微调全生命周期），并进行了系统性能的定量评估，而先前工作主要验证可行性，缺乏明确任务导向和定量评估。

在**搜索优化方法**方面，一些研究将进化算法、树搜索等方法融入自动化科学发现，为生成和实现多样化研究想法提供支持。本文与之的**关系**是借鉴了搜索思想，将多轮实验过程建模为搜索树。**区别**在于，先前方法严重依赖大规模方法采样，难以应对计算开销巨大的任务（如LLM微调），而TREX通过智能体驱动的树状探索，旨在更高效地规划路径、复用结果并提炼见解。

在**基准评测**方面，存在MLE-bench、RE-bench等用于评估自动化AI研究系统的基准，以及IdeaBench等评估相关场景的基准。本文与这些工作的**关系**是都关注对AI智能体的评估。**区别**在于，本文针对“LLM训练自动化”这一特定空白，构建了专门的FT-Bench基准，用于系统评估。

在**自动化机器学习（AutoML）与数据构建**方面，传统AutoML专注于模型选择和超参数配置，近期也有工作利用LLM生成架构变体或合成训练后目标。在数据构建方面，近期研究广泛利用LLM进行数据合成、进化精炼和质量过滤。本文与这些工作的**关系**是都涉及自动化机器学习过程。**区别**在于，现有方法通常受限于预定义的搜索空间或专注于优化孤立组件，将LLM作为预定流程中的离散工具使用。而本文提出的TREX探索了一个更开放的环境，将数据准备等环节整合到一个自主循环中，实现了LLM训练全生命周期的整体、全自动范式。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TREX的多智能体系统，并采用树状探索与双循环工作流，来自动化解决LLM微调流程复杂、手动实验成本高昂的问题。其核心方法是将多轮实验过程建模为一棵搜索树，并基于蒙特卡洛树搜索（MCTS）策略来引导探索，同时通过研究员（Researcher）与执行器（Executor）两个核心智能体的协作来执行每一轮具体实验。

整体框架采用内外双循环设计。内循环中，研究员智能体负责实验设计、结果分析与诊断。它采用由粗到细的策略：先根据任务目标和历史记忆（通过记忆上下文管理模块整合）确定高层改进方向（如增加数据、调整算法），再细化为包含具体目标、数据处理流程和训练配置的实验计划。为此，研究员可利用学术搜索引擎和Hugging Face等工具获取外部知识与数据资源。执行器智能体则部署在GPU集群上，负责将研究员的指令转化为可执行代码，具体执行数据预处理、模型训练与评估，并通过沙盒环境确保隔离与安全。两者通过多轮通信协同完成单次实验迭代。

外循环将整个多轮实验过程视为一棵树，每个实验轮次对应一个节点。系统使用MCTS策略来扩展实验节点：从根节点（初始基线实验）开始，每次迭代选择UCT值最高的节点进行细化，生成新训练方案并由智能体执行验证，随后根据实验收益（基于任务主要评估指标的归一化值）更新树中节点的UCT分数。这种机制平衡了对高性能现有方案的利用与对新方案的探索。

关键技术模块与创新点包括：1）**AIDP库**：一个专为LLM数据管道开发的高性能模块化库，基于HuggingFace Datasets构建，提供可重现、可并行处理的数据操作符，使智能体能灵活编排复杂数据流程。2）**实验诊断与归因**：不仅依赖基准分数，还通过分析验证集失败案例并进行归因，结合历史实验进行对比分析，生成详细评估报告以指导后续设计，从而从每次迭代中提取丰富反馈以加速优化。3）**记忆上下文管理**：为避免历史信息冗余或超出上下文窗口，系统动态整合当前节点的父轨迹、兄弟节点以及全局关键节点（带来显著性能增益或失败的实验）的信息，并压缩为记忆上下文，确保实验设计的连续性与效率。

综上，TREX通过树状探索框架、双智能体协作、以及上述关键技术，实现了对LLM微调全生命周期（从需求分析、文献数据研究到训练策略制定、数据准备及模型训练评估）的自动化，从而高效优化模型在目标任务上的性能。

### Q4: 论文做了哪些实验？

论文在FT-Bench基准的10个任务上评估了TREX框架，这些任务涵盖基础能力优化和领域特定任务。实验设置方面，统一使用Qwen3-1.7B作为基础模型进行微调，每轮实验最多使用5万个训练样本。系统设置中，研究者智能体（Researcher）测试了两种后端大语言模型：开源模型Qwen3-Next-80B-Thinking和专有模型Gemini 3 Pro；执行者智能体（Executor）采用Claude 4.5 Sonnet。每个任务最多进行20轮实验迭代，选取最佳轮次作为最终结果。

评估采用归一化相对性能增益指标 \( G_T \) 进行公平比较，其中参考模型 \( M_{Ref} \) 为Qwen3-235B-2507。主要结果显示，TREX在所有任务上均能持续提升基础模型性能。关键数据指标如下：在ACI-Bench任务上，使用Gemini 3 Pro后端的Rouge-1分数达到0.502（相对增益+849%）；在TOMG-Bench任务上，验证准确率达到0.681（+108%）；在HoC任务上，Macro-F1达到0.897（+238%）。总体而言，Gemini 3 Pro后端在大多数任务上表现优于Qwen3-Next-80B-Thinking后端。

论文还进行了对比实验，包括与人类专家微调效果的比较。例如，在TOMG-Bench任务上，TREX在Qwen3-1.7B上实现了0.498的性能增益，优于人类专家在Llama3.1-8B和Llama3.2-1B上实现的0.189和0.139增益。此外，消融研究评估了树搜索策略、AIDP工具集成和坏例分析的影响。结果表明，蒙特卡洛树搜索（MCTS）策略相比贪婪最佳优先搜索（GBFS）和顺序扩展搜索（SES）更稳定且能获得更一致的性能提升；集成AIDP工具能显著提高性能并减少数据处理失败；坏例分析有助于更有效地迭代实验并提升最终分数。

### Q5: 有什么可以进一步探索的点？

该论文展示了自动化微调流程的潜力，但仍有多个方向值得深入探索。首先，TREX依赖于MCTS进行搜索，其效率和效果受限于计算预算与启发式设计，未来可研究更高效的搜索算法或引入元学习来动态调整搜索策略。其次，系统在数据配方生成和训练策略制定上可能受限于现有文献的覆盖范围，对于高度新颖或跨领域的任务，其自动化探索能力可能不足，需增强Agent的创造性推理能力。此外，FT-Bench任务虽源自真实场景，但规模和多样性有限，未来需构建更复杂、多模态的基准测试以评估系统的泛化性。从实践角度看，可探索将人类专家反馈融入迭代循环，形成人机协同的优化机制，或引入因果推理来理解策略与性能间的深层关系，从而提升探索的针对性。最后，将此类系统扩展至大规模分布式训练或多目标优化场景，也是推动自动化AI研究迈向成熟的关键。

### Q6: 总结一下论文的主要内容

本文提出了TREX，一个通过多智能体协作自动化大语言模型（LLM）微调全生命周期的框架。其核心问题是解决复杂、开放的LLM训练工作流程自动化难题。方法上，TREX设计了研究员（Researcher）和执行器（Executor）两大核心模块进行协同，将多轮实验过程建模为一棵搜索树，并利用蒙特卡洛树搜索（MCTS）在有限计算资源下高效规划探索路径、复用历史结果并提炼高层见解。主要结论表明，TREX在涵盖基础能力优化和领域特定任务的FT-Bench基准测试中，能持续优化模型在目标任务上的性能，在多个案例中达到甚至超越了专家设计流程的效果。该工作证明了基于智能体的系统可作为自动化AI研究的可扩展范式，具有重要实践意义。
