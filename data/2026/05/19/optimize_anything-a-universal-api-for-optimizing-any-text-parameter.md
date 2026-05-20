---
title: "optimize_anything: A Universal API for Optimizing any Text Parameter"
authors:
  - "Lakshya A Agrawal"
  - "Donghyun Lee"
  - "Shangyin Tan"
  - "Wenjie Ma"
  - "Karim Elmaaroufi"
  - "Rohit Sandadi"
  - "Sanjit A. Seshia"
  - "Koushik Sen"
  - "Dan Klein"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
  - "Omar Khattab"
  - "Alexandros G. Dimakis"
  - "Matei Zaharia"
date: "2026-05-19"
arxiv_id: "2605.19633"
arxiv_url: "https://arxiv.org/abs/2605.19633"
pdf_url: "https://arxiv.org/pdf/2605.19633v1"
github_url: "https://github.com/gepa-ai/gepa"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
  - "cs.NE"
  - "cs.SE"
tags:
  - "LLM-based Optimization"
  - "Agent Architecture Search"
  - "Multi-task Transfer"
  - "Code Generation"
  - "CUDA Kernel Optimization"
  - "Cloud Scheduling"
  - "Benchmark"
relevance_score: 8.5
---

# optimize_anything: A Universal API for Optimizing any Text Parameter

## 原始摘要

Can a single LLM-based optimization system match specialized tools across fundamentally different domains? We show that when optimization problems are formulated as improving a text artifact evaluated by a scoring function, a single AI-based optimization system-supporting single-task search, multi-task search with cross-problem transfer, and generalization to unseen inputs-achieves state-of-the-art results across six diverse tasks. Our system discovers agent architectures that nearly triple Gemini Flash's ARC-AGI accuracy (32.5% to 89.5%), finds scheduling algorithms that cut cloud costs by 40%, generates CUDA kernels where 87% match or beat PyTorch, and outperforms AlphaEvolve's reported circle packing solution (n=26). Ablations across three domains reveal that actionable side information yields faster convergence and substantially higher final scores than score-only feedback, and that multi-task search outperforms independent optimization given equivalent per-problem budget through cross-task transfer, with benefits scaling with the number of related tasks. Together, we show for the first time that text optimization with LLM-based search is a general-purpose problem-solving paradigm, unifying tasks traditionally requiring domain-specific algorithms under a single framework. We open-source optimize\_anything with support for multiple backends as part of the GEPA project at https://github.com/gepa-ai/gepa .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于LLM的优化系统领域碎片化的问题。研究背景是，大型语言模型（LLM）已经展现出了作为优化器的潜力，例如FunSearch用于数学发现，AlphaEvolve用于代码优化，GEPA用于提示词优化等。然而，现有方法存在显著不足：它们都是针对特定领域（如代码、提示词）设计的，每个系统只支持一种优化模式（如单任务或泛化），没有一个统一的系统能够同时处理代码、提示词、智能体架构、数值配置、图像生成等本质不同的领域。核心问题是：能否设计一个单一的、基于LLM的文本优化系统，使其在多种截然不同的任务上匹配甚至超越专业化的领域工具？本文提出的“optimize_anything”旨在验证这一点，它通过将各类问题统一转化为“优化文本工件”的范式，并引入统一的声明式API，首次实现了对多种模式和领域的通用支持。

### Q2: 有哪些相关研究？

相关研究主要分为四类：**LLM-based程序进化**、**提示优化**、**LLM自我改进与反思**以及**智能体架构搜索**。

在**LLM-based程序进化**方面，AlphaEvolve、OpenEvolve、ShinkaEvolve、FunSearch和EvoPrompting等均采用LLM驱动进化搜索，但均局限于单任务模式，且暴露了框架特定的复杂抽象（如岛屿拓扑、提示采样器）。本文（Optimize Anything）将其接口简化为声明式API，并首次引入多任务与泛化模式，将诊断性反馈提升为一等公民。

在**提示优化**领域，GEPA、OPRO、APE等方法专注于优化文本提示；TextGrad使用LLM生成“梯度”进行优化。本文支持GEPA作为后端，但将其扩展至任意文本工件的优化（如CUDA内核、调度算法），超越了仅提示优化的范畴。

在**LLM自我改进与反思**方面，Reflexion、Self-Refine等方法利用自我反馈改进输出，本文的ASI（Actionable Side Information）机制将其泛化为一种声明性评估器契约，而非硬编码的自我批评。

在**智能体架构搜索**中，ADAS和AFlow搜索智能体架构，本文的泛化模式直接将其作为特例：智能体代码作为工件，评估器模拟运行，同时进化架构与提示。

### Q3: 论文如何解决这个问题？

Optimize Anything 的核心是一个统一且极其简洁的API，它将文本优化问题形式化为一个迭代改进的过程。用户只需提供初始文本（或自然语言目标）和一个评分函数（Evaluator），系统便利用LLM作为核心优化引擎来驱动搜索。整体框架包含三个主要组件：**Evaluator**（评估器）接收候选文本并返回一个分数和“侧信息”（Side Information, SI）字典，SI被设计为类似梯度的诊断反馈，可包含错误信息、结构化数据甚至图像，为LLM提供明确的优化方向；**Reflection & Mutation**（反思与变异）环节是该系统的关键技术，LLM基于SI对候选方案进行诊断并提出针对性的改进，而非盲目变异；**Pareto Frontier**（帕累托前沿）管理策略则支持三种优化范式：单任务搜索（直接优化单个目标）、多任务搜索（跨任务共享前沿，自动进行模式迁移）以及泛化（在训练集搜索，在验证集评估泛化能力）。

系统的创新点在于：第一，将**SI作为一等公民**，使得诊断反馈通用且可操作，大幅优于传统仅用标量分数的优化；第二，设计了**基于帕累托前沿的多目标保留机制**，避免信息坍缩，允许保留在不同任务或指标上表现优异的候选方案，并通过小批量选择（2-3个例子）实现集中改进；第三，实现了**声明式、零模板的统一接口**，无需任务特定的变异提示或配置，用户只需定义“什么”（工件、评估器、知识），系统处理“如何”。这些设计使其成为首个能以单一系统统一代码搜索、提示优化和智能体架构发现的通用优化框架。

### Q4: 论文做了哪些实验？

论文在六个领域进行了实验，覆盖了单任务搜索、多任务搜索和泛化到未见输入三种优化模式。实验设置如下：1) **代码技能优化**（Bleve代码库）：评估者使用编码代理解决仓库任务并评分，优化后的技能需泛化到未见任务。结果：Haiku 4.5通过率从79.3%提升至98.3%，Sonnet 4.5从94.8%提升至100%，且解决时间降低47%。2) **云调度算法优化**（ADRS基准）：优化CloudCast和Can't Be Late算法，采用包含训练/验证划分的泛化模式。结果：CloudCast相比Dijkstra路由节省40.2%成本，Can't Be Late节省7.8%成本，总得分96.6，超过OpenEvolve的92.9。3) **ARC-AGI代理架构优化**：将整个代理系统（代码、子代理架构等）作为文本工件优化，评估其对未见谜题的泛化能力。结果：使用Gemini Flash，测试准确率从32.5%提升至89.5%。4) **AIME数学提示优化**：优化GPT-4.1-mini的系统提示。结果：测试集准确率从46.67%提升至60.00%，超越MIPROv2的51.33%。5) **CUDA内核生成**（KernelBench的31个操作）：优化生成内核的提示。结果：87%的内核达到或优于PyTorch基线，48%加速超10%，25%加速超20%。6) **圆填充**（n=26）：优化填充算法代码。结果：得分2.63598，超过AlphaEvolve和OpenEvolve。**消融实验**显示：多任务搜索在CUDA内核任务上持续优于单任务（如F(1.2)阈值下多任务持续改进而单任务停滞）；引入可操作侧信息（SI）在提示优化任务上加速收敛（100轮次达0.80分 vs 无SI需600轮次）并提升最终测试分数（86.32 vs 82.5），并在圆填充和CUDA内核任务上获得一致性收益。**方法比较**：在圆填充任务上，OA仅用63次评估（$3.18）即达2.63598分，而OpenEvolve在200次评估（$6.85）后仅达2.6307分。

### Q5: 有什么可以进一步探索的点？

论文虽然展示了LLM在多种优化任务上的通用性，但仍存在几个关键局限与探索空间。首先，当前框架依赖外部得分函数提供反馈，在缺乏明确量化指标（如艺术创作、开放式设计）的领域中表现未知，未来可探索引入人类偏好或语言化定性反馈来扩展适用性。其次，多任务迁移能力虽已验证，但跨领域知识迁移的机制尚不明确——例如从CUDA内核优化中习得的模式如何影响调度算法设计，需要理论化分析以提升可解释性。此外，单次搜索的计算成本较高，尤其在问题规模剧增时，可考虑结合层次化搜索或动态种子机制来加速收敛。最后，对非文本或混合模态参数（如代码与数值混合的配置）的优化能力未涉及，建议扩展API以支持结构化参数空间的代理，例如将离散与连续变量联合调优。这些方向有望推动真正的通用优化智能体。

### Q6: 总结一下论文的主要内容

本文提出了一种名为optimize_anything的统一API，用于解决多种领域的文本参数优化问题。核心是将各种优化问题（如CUDA内核、云调度策略、智能体架构等）统一表述为“根据评分函数优化文本工件”，并采用基于LLM的搜索方法。该框架支持单任务搜索、多任务搜索（首次实现跨问题迁移）以及对未见输入的泛化。实验结果表明，该方法在六项多样任务中均达到或超越了专门工具的顶尖水平：将Gemini Flash的ARC-AGI准确率从32.5%提升至89.5%，将云成本降低40%，生成的CUDA内核中87%匹敌或超越PyTorch基线，并在圆填充任务中超过AlphaEvolve。关键发现表明，提供可操作的侧面信息（如堆栈跟踪）比仅返回分数能使收敛速度提升4-6倍且获得更高分数；多任务搜索在使用相同预算时通过跨任务迁移优于独立优化。这项工作首次证明了基于LLM的文本优化是一种通用的问题解决范式，可将传统上需要专门算法的任务统一于单一框架下。
