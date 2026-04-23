---
title: "Dual-Cluster Memory Agent: Resolving Multi-Paradigm Ambiguity in Optimization Problem Solving"
authors:
  - "Xinyu Zhang"
  - "Yuchen Wan"
  - "Boxuan Zhang"
  - "Zesheng Yang"
  - "Lingling Zhang"
  - "Bifan Wei"
  - "Jun Liu"
date: "2026-04-22"
arxiv_id: "2604.20183"
arxiv_url: "https://arxiv.org/abs/2604.20183"
pdf_url: "https://arxiv.org/pdf/2604.20183v1"
categories:
  - "cs.CL"
tags:
  - "Agent Architecture"
  - "Memory-Augmented Reasoning"
  - "Problem-Solving Agent"
  - "Optimization"
  - "Training-Free Enhancement"
  - "Knowledge Distillation"
  - "Error Detection and Repair"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Dual-Cluster Memory Agent: Resolving Multi-Paradigm Ambiguity in Optimization Problem Solving

## 原始摘要

Large Language Models (LLMs) often struggle with structural ambiguity in optimization problems, where a single problem admits multiple related but conflicting modeling paradigms, hindering effective solution generation. To address this, we propose Dual-Cluster Memory Agent (DCM-Agent) to enhance performance by leveraging historical solutions in a training-free manner. Central to this is Dual-Cluster Memory Construction. This agent assigns historical solutions to modeling and coding clusters, then distills each cluster's content into three structured types: Approach, Checklist, and Pitfall. This process derives generalizable guidance knowledge. Furthermore, this agent introduces Memory-augmented Inference to dynamically navigate solution paths, detect and repair errors, and adaptively switch reasoning paths with structured knowledge. The experiments across seven optimization benchmarks demonstrate that DCM-Agent achieves an average performance improvement of 11%- 21%. Notably, our analysis reveals a ``knowledge inheritance'' phenomenon: memory constructed by larger models can guide smaller models toward superior performance, highlighting the framework's scalability and efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在求解优化问题时面临的一个核心挑战：**结构歧义性**。具体而言，当单个优化问题的文本描述同时包含多个相关但相互冲突的建模范式（例如，整数线性规划、约束规划、动态规划）的特征时，LLMs 会受到认知干扰，难以选择正确的建模路径，从而影响生成有效解决方案的能力。

研究背景是，LLMs 在自动化优化建模方面展现出潜力，有望减少对领域专家的依赖。然而，现有方法存在明显不足。一方面，**微调方法**容易受到上述范式干扰的误导，倾向于机械地应用记忆中的模板，而无法灵活应对需要不同策略的细微问题变体。另一方面，**基于智能体的框架**在验证阶段难以处理这种模糊性；它们通常依赖静态提示（如“检查是否正确”）进行验证，缺乏检测特定范式陷阱（如区分ILP中的线性间隙与DP中的递推有效性）的细粒度知识，导致在模糊的算法选择面前束手无策。

因此，本文要解决的核心问题是：如何让LLM在无需训练的情况下，既保持**灵活性**以导航范式歧义，又获得**针对性知识**以验证特定范式的正确性。为此，论文提出了**双集群记忆智能体**框架。该框架通过将历史解决方案外部化为结构化的记忆知识库，将抽象的建模决策与具体的代码实现解耦。其核心创新在于构建“建模”与“编码”两个集群，并从集群中提炼出“方法”、“检查清单”和“陷阱”三层结构化知识，用以在推理过程中动态引导、检测错误、修复并切换路径，从而系统性地解决多范式歧义带来的干扰问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于提示的优化建模、微调方法以及检索增强推理。

在**基于提示的优化建模**方面，现有工作利用多智能体工作流或树搜索算法来增强通用大语言模型在优化问题上的推理与代码生成能力。本文提出的DCM-Agent也属于此类，但核心区别在于其引入了**双聚类记忆结构**，将历史解决方案系统性地组织为建模与编码两个解耦的集群，并提炼出“方法、检查清单、陷阱”三类结构化知识，而非仅依赖即时提示或动态工作流。

在**微调方法**上，相关研究（如FOARL、ORLM、SIRL）通过在运筹学特定数据集上训练，使模型内化建模模式。本文方法与之根本不同，它完全**无需训练**，通过利用历史解决方案中的结构化知识来指导新问题的求解，更具灵活性和可扩展性。

在**检索增强推理**领域，已有框架（如ReAct、Retrieval-Augmented Thoughts）通过检索外部信息来动态修正推理轨迹。OptiTree等研究将其应用于优化问题，检索类似子问题以确保建模步骤的可验证性。本文的DCM-Agent与之有相似之处，均借助外部知识来缓解幻觉问题。但本文的创新点在于**记忆增强推理**机制，它不仅进行检索，还能基于双聚类记忆动态导航解决方案路径、检测修复错误，并利用结构化知识自适应切换推理路径，从而更系统地解决多范式模糊性这一特定挑战。

### Q3: 论文如何解决这个问题？

论文通过提出双聚类记忆智能体（DCM-Agent）来解决优化问题中的多范式模糊性挑战。其核心方法是将问题解决过程解耦为建模和编码两个独立空间，并构建一个结构化的记忆系统来存储和泛化历史经验，从而在无需额外训练的情况下引导大语言模型生成更可靠的解决方案。

整体框架分为两个主要阶段：双聚类记忆构建和记忆增强推理。在记忆构建阶段，系统首先收集历史问题-解决方案对，并将其分类为始终正确、可恢复和持续失败三种类型，以便差异化提取知识。每个解决方案被分解为建模逻辑和编码实现两部分，并分别生成嵌入向量用于后续检索。关键创新在于，系统为每个部分提取一个结构化的知识三元组：方法（记录解决模板和步骤）、检查清单（列出有效性标准和边界检查）以及陷阱（指出常见错误和约束违反）。这些实例级知识随后被组织到独立的建模聚类和编码聚类中。每个聚类通过增量更新机制，将其成员的知识三元组合并升华为一个泛化的、非冗余的聚类级知识概要。此外，系统构建了一个二分图来建模不同建模聚类与编码聚类之间的关联强度，记录了哪些建模逻辑与哪些编码策略在实践中被证明是兼容的。

在记忆增强推理阶段，面对新问题，DCM-Agent采用双路径检索机制：既通过实例级检索找到语义最相似的具体历史节点，也通过聚类级检索匹配抽象的建模逻辑类别。两者结合确定候选的建模聚类。接着，利用预建的二分图，为每个候选建模聚类检索出与之关联最紧密的编码聚类，形成多条候选的“建模-编码”解决路径，并由LLM根据新问题对其进行排序，生成一个优先级队列。

最后，系统采用一个生成-验证-修复-回溯的管道来执行解决方案。生成步骤严格依据所选聚类的方法知识；验证步骤则使用对应聚类的检查清单知识来审核中间产出。如果代码执行失败，修复机制会参考聚类中提炼出的陷阱知识进行有针对性的调试，而非盲目尝试。若修复无效，则回溯到优先级队列中的下一条路径。这种设计使得智能体能够动态导航解空间，检测并修复错误，并自适应地切换推理路径。

实验结果表明，该方法在多个优化基准测试上平均提升了11%-21%的解决准确率，并揭示了“知识继承”现象，即由更大模型构建的记忆可以指导更小模型获得更优性能，体现了框架的可扩展性和效率。

### Q4: 论文做了哪些实验？

实验在七个优化基准数据集上进行，包括NL4Opt、NLP4LP、OptiBench、OptMATH、ComplexLP（来自MAMO）、IndustryOR和ComplexOR，以覆盖从标准到复杂、再到现实应用的不同复杂度。实验设置使用500个与基准不重叠的问题构建记忆，采用严格的端到端求解准确率作为评估指标，即生成的代码执行后，其输出的需求数值和目标函数数值均需与真实答案匹配。

对比方法包括不同规模的通用大语言模型（如Qwen3系列、DeepSeek-V3.2、GPT-5.1）以及三种先进的专用优化框架：OptiMUS、AF-MCTS和OptiTree。

主要结果显示，DCM-Agent在所有模型规模上均实现了最佳性能，平均准确率提升11%-21%。关键数据指标包括：在NLP4LP数据集上，使用Qwen3-235B时，DCM-Agent准确率达84.71%，而基线为74.38%；在OptiBench上，准确率从60.83%提升至75.21%；在OptMATH上，从31.33%提升至46.39%。实验还揭示了“知识继承”现象：由更大模型（如GPT-5.1）构建的记忆可以指导较小模型（如Qwen3-8B）获得显著性能提升，例如在NLP4LP上，使用Qwen3-8B构建记忆时准确率为62.40%，而使用Qwen3-235B构建记忆时可提升至78.51%。消融实验表明，建模集群的移除比编码集群移除导致更严重的性能下降，凸显了数学逻辑解耦的关键作用。参数敏感性分析显示，检索规模K=3、更新阈值N=5、规划候选M=3时达到最佳平衡。此外，内存预算实验表明，随着可用内存节点从0%增至100%，性能持续提升，验证了历史经验的广度对泛化能力的直接影响。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于初始化阶段的计算开销，即构建双簇记忆时收集、分类历史轨迹并提炼结构化知识的过程存在一次性延迟。未来研究可探索在线学习机制，使记忆能通过用户交互动态演化，避免全量重建。此外，还可进一步研究以下方向：一是提升记忆检索的精准度，例如结合问题语义与结构特征优化嵌入方法，减少无关知识的干扰；二是扩展框架的适用场景，如将其应用于非优化类问题（如规划、推理任务），验证其跨领域泛化能力；三是深化“知识继承”现象的研究，探索大模型引导小模型时知识传递的边界与效率，可能通过量化知识蒸馏的阈值来提升小模型独立解决问题的能力。最后，可考虑引入轻量化记忆更新策略，在保持性能的同时降低长期维护成本。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型在解决优化问题时面临的结构性歧义挑战，即同一问题存在多种相互冲突的建模范式，导致解决方案生成困难。为此，作者提出了双集群记忆智能体（DCM-Agent），其核心贡献在于以无需训练的方式利用历史解决方案来提升性能。

方法上，DCM-Agent首先进行双集群记忆构建：将历史解决方案分配到建模和编码两个集群中，并将每个集群的内容提炼为“方法”、“检查清单”和“常见陷阱”三种结构化知识，从而获得可泛化的指导信息。在此基础上，智能体通过记忆增强推理动态导航解决方案路径，检测并修复错误，并利用结构化知识自适应切换推理路径。

实验结果表明，在七个优化基准测试中，DCM-Agent平均性能提升了11%-21%。主要结论是，该框架能有效弥合数学形式化与可执行求解器代码之间的关键差距，显著提高解决方案的鲁棒性。论文还揭示了一个“知识继承”现象：由更大模型构建的记忆可以指导更小的模型获得更优性能，这凸显了该框架的可扩展性和高效性。
