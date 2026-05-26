---
title: "FrontierOR: Benchmarking LLMs' Capacity for Efficient Algorithm Design in Large-Scale Optimization"
authors:
  - "Minwei Kong"
  - "Chonghe Jiang"
  - "Ao Qu"
  - "Wenbin Ouyang"
  - "Zhaoming Zeng"
  - "Xiaotong Guo"
  - "Zhekai Li"
  - "Junyi Li"
  - "Yi Fan"
  - "Xinshou Zheng"
  - "Xi Jing"
  - "Yikai Zhang"
  - "Zhiwei Liang"
  - "Seonghoo Kim"
  - "Runqing Yang"
  - "Zijian Zhou"
  - "Sirui Li"
  - "Han Zheng"
  - "Wangyang Ying"
  - "Ou Zheng"
date: "2026-05-24"
arxiv_id: "2605.25246"
arxiv_url: "https://arxiv.org/abs/2605.25246"
pdf_url: "https://arxiv.org/pdf/2605.25246v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "代码生成Agent"
  - "科学Agent"
  - "Agent评测基准"
  - "优化算法设计"
relevance_score: 8.5
---

# FrontierOR: Benchmarking LLMs' Capacity for Efficient Algorithm Design in Large-Scale Optimization

## 原始摘要

Large language models (LLMs) are increasingly used for optimization modeling and solver-code generation, yet practical operations research and optimization problems often require a harder capability: designing scalable algorithms that exploit problem structure and outperform direct formulation-and-solve baselines. Existing benchmarks are limited to small or simplified examples far below real-world scale and complexity. We introduce FrontierOR, among the first benchmarks to systematically evaluate LLM-based efficient algorithm design for realistic large-scale optimization problems. FrontierOR includes 180 tasks derived from methodologically diverse papers published in top-tier operations research venues, each with standardized instances and a hidden, expert-verified evaluation suite. We evaluate seven LLMs spanning frontier, cost-effective, and open-source models both in one-shot and test-time evolution settings. The results reveal that frontier models still struggle to move from executable formulations to efficient optimization algorithms: the strongest one-shot model outperforms Gurobi in only 31% of cases in both solution quality and computational efficiency, and even strong coding agents with test-time evolution achieve only 50% on selected hard tasks. FrontierOR establishes a practical evaluation platform for LLM-based optimization algorithm design, which enables future LLMs and agents to be systematically tested on whether they can move beyond correct formulation toward a feasible, high-quality, and efficient algorithm. Our FrontierOR Benchmark is available at https://anonymous.4open.science/r/efficient-opt-bench-F03D.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型在运筹学优化领域应用中的一个关键缺失：现有工作主要评估LLM将自然语言问题转化为数学公式或求解器代码的能力（即建模能力），而忽视了更核心的“高效算法设计”能力——即针对大规模现实问题，设计能利用问题结构（如可分解性、稀疏性）的、可扩展的、比直接调用求解器更快更优的算法。

当前研究背景是，LLM在优化建模方面取得了进展，但现实运筹学问题通常规模巨大（如千万级变量和约束），需要更复杂的算法设计能力。现有基准测试存在明显不足：要么数据规模太小、过于简化，与实际应用脱节；要么缺乏自然语言问题描述；要么任务数量有限，难以全面评估。

因此，本文的核心问题是：**能否构建一个系统性的基准测试，来评估LLM在面对真实大规模优化问题时，能否生成不仅在数学上可行，而且在解质量、计算效率上与专家验证的求解器基线相当甚至更优的高效算法？** 为了填补这一空白，论文推出了FrontierOR基准，包含180个来自顶级运筹学期刊的真实任务，通过标准化实例和隐藏评估套件，全面衡量LLM在从问题描述到算法实现过程中的算法效率，而不仅仅是公式正确性。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是“LLM用于优化建模与求解器实现”的工作，代表包括NL4OPT、OptiMUS、OptiBench、MAMO、ORLM、OptMATH、CP-Bench、AlphaOPT、LEAN-LLM-OPT和StepORLM。这些工作主要评估LLM将自然语言问题转化为数学规划或可执行求解器代码的正确性（即公式化能力）。相比之下，本文Focus评价的是LLM设计高效算法的能力，重点处理传统“公式化-求解”管道在大规模实例中速度慢或内存不足的场景。第二类是“组合优化基准套件”，经典资源如OR-Library、TSPLIB、CVRPLIB、QAPLIB、MIPLIB等，以及近期基于LLM的CO-Bench和HeuriGym。这些基准主要关注问题数量的扩展或经典优化案例，但停留在小规模任务集合上。本文的FrontierOR则是首个系统地、面向真实大规模优化问题，评估LLM端到端算法设计效率的基准，包含180个源自顶刊论文的任务和隐藏专家验证套件，在问题数量、文献根基和端到端评估方面均优于现有工作。

### Q3: 论文如何解决这个问题？

该论文通过构建一个系统化的基准测试平台来解决评估LLM在大型优化问题中设计高效算法能力的问题。核心方法包括三个方面：

首先，在数据构建上，论文从《Operations Research》等顶级运筹学期刊中筛选1992-2025年间的方法论论文，最终形成包含180个任务的基准数据集。每个任务都经过自动化组件生成和专家审计两阶段质量控制：先提取自然语言问题描述和数学公式，生成标准化实例、Gurobi参考实现和可行性检查器；再由15位运筹学专家进行多轮审查，确保问题描述完整性、公式保真度和代码一致性。

其次，在评估框架设计上，论文采用了隐藏评估器机制。LLM仅获取自然语言问题描述和实例格式，看不到任何数学公式或算法提示。生成的算法需通过小实例门控检查（执行成功、方案可行且最优性差距<10%），然后在大规模实例上评估四个核心指标：执行率、可行性、解质量和质量-时间效率。

第三，在实验设计上，论文设置了两种评测模式：一次性生成要求模型直接从零编写完整优化程序；自进化框架则测试LLM通过迭代优化（如AlphaEvolve、EoH和CORAL等多智能体系统）是否能发现更优算法。所有算法均在单核CPU的Docker容器中运行，确保可复现性。特别值得注意的是，论文在50个真正困难任务上设置了"硬"子集，这些任务具有组合爆炸性、实例结构复杂性和求解器饱和性三大特征。

### Q4: 论文做了哪些实验？

论文围绕两个研究问题设计实验：一是单次算法生成，二是测试时自演化。实验使用FrontierOR基准，包含完整集（180个任务）和困难子集（50个计算密集型任务）。评估指标包括执行率、可行性、解质量和质量-时间效率（QTE），以Gurobi为基线。

在单次生成实验中，对比了Claude Opus 4.6、GPT-5.3-Codex、Gemini 3.1 Pro等前沿模型，以及DeepSeek-R1、Grok-4.20-beta、Qwen3-Coder-Plus、LLaMA-4-Maverick等经济型模型。主要结果：前沿模型在完整集上的可行性约0.60-0.62，QTE约0.25-0.31；最强单次模型仅31%任务在解质量和效率上同时超越Gurobi。困难子集上，Gemini 3.1 Pro可行性最高（0.64），Claude Opus 4.6 QTE最高（0.32）。分析发现，前沿模型更常生成非单一求解器算法（如局部搜索、元启发式），而较弱模型多依赖直接求解器调用。

在测试时自演化实验中，选取困难集中40%最具挑战性任务，以GPT-5.3-Codex为骨干，对比EoH、OpenEvolve和CORAL三个框架（30次尝试预算）。结果显示，CORAL表现最佳：可行性达1.00，解质量0.67，QTE 0.50，显著优于单次生成的0.15。所有自演化框架在前约5次迭代内快速接近Gurobi基线，但解质量突破更慢，仅CORAL在约16次尝试后稳定超越Gurobi。

### Q5: 有什么可以进一步探索的点？

当前 FrontierOR 基准测试主要关注单次生成和固定步数的演化优化，未来可探索更高效的测试时搜索策略，如树搜索或遗传编程，以在更少的迭代次数内发现更优的算法结构。同时，论文仅评估了 7 个模型，未来可扩展至更大规模的模型系列，并研究模型规模与算法设计能力之间的 Scaling Laws。另一个重要方向是将人类专家知识嵌入奖励模型或提示中，引导 LLM 偏向更有效的算法范式（如分支定界、列生成），而非简单的调用求解器。此外，当前任务均来自已发表的运筹学论文，未来可引入更动态、数据驱动的优化场景，如在线调度或非凸优化，以检验 LLM 对新结构和未知约束的泛化能力。最后，可开发多智能体协作框架，让不同专长的 LLM 分别负责问题分解、算法设计与性能诊断。

### Q6: 总结一下论文的主要内容

该论文提出了FrontierOR，一个用于评估大语言模型在现实大规模运筹优化问题中设计高效算法能力的基准。传统基准主要关注公式化建模或求解器代码生成，忽略了算法工程的核心——设计可扩展且高效的算法。FrontierOR包含180个源自顶级运筹学期刊的真实任务，实例规模高达数千万变量和约束。评估不仅检查解的正确性，还通过解质量（与Gurobi最优解的目标值差距）和计算效率（运行时间）衡量算法性能。实验表明，当前最强的一次性模型仅在31%的任务上同时超越Gurobi，通过测试时演化提升后也仅达到50%。该基准揭示了LLM从生成可执行公式到设计高效算法之间存在巨大差距，为未来LLM在算法设计领域的系统评估提供了重要平台。
