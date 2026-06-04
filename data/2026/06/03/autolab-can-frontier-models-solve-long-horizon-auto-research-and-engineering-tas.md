---
title: "AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?"
authors:
  - "Zhangchen Xu"
  - "Junda Chen"
  - "Yue Huang"
  - "Dongfu Jiang"
  - "Jiefeng Chen"
  - "Hang Hua"
  - "Zijian Wu"
  - "Zheyuan Liu"
  - "Zexue He"
  - "Lichi Li"
  - "Shizhe Diao"
  - "Jiaxin Pei"
  - "Jinsung Yoon"
  - "Hao Zhang"
  - "Mengdi Wang"
  - "Radha Poovendran"
  - "Misha Sra"
  - "Alex Pentland"
  - "Zichen Chen"
date: "2026-06-03"
arxiv_id: "2606.05080"
arxiv_url: "https://arxiv.org/abs/2606.05080"
pdf_url: "https://arxiv.org/pdf/2606.05080v1"
github_url: "https://github.com/autolabhq/autolab"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Long-Horizon Agent"
  - "Benchmark"
  - "Closed-Loop Optimization"
  - "Autonomous Code Generation"
  - "Iterative Refinement"
relevance_score: 9.5
---

# AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?

## 原始摘要

Scientific and engineering progress is fundamentally a long-horizon iterative process: proposing changes, running experiments, measuring outcomes, and continuously refining artifacts. Yet existing benchmarks for frontier models primarily evaluate either single-turn responses or short-horizon agent trajectories, failing to capture the challenges of sustained iterative improvement over extended time horizons. To address this gap, we introduce AutoLab, a new benchmark for ultra long-horizon closed-loop optimization. AutoLab consists of 36 realistic, expert-curated tasks spanning four diverse domains: system optimization, puzzle & challenge, model development, and CUDA kernel optimization. Each task begins with a correct but deliberately suboptimal baseline and challenges agents to improve it within a strict wall-clock budget. Evaluating 17 state-of-the-art models reveals the dominant predictor of success is not the quality of an agent's initial attempt, but its persistence in repeatedly benchmarking, editing, and incorporating empirical feedback. While claude-opus-4.6 exhibits strong long-horizon optimization capabilities, most frontier models, including several proprietary ones, either terminate prematurely or exhaust their budgets with minimal progress. These results underscore the importance of time awareness and persistent iteration in autonomous agents. We open-source the full benchmark, evaluation harness, and task artifacts, to accelerate research toward truly capable long-horizon agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有大语言模型（LLM）评估基准在衡量长期、迭代优化能力方面的显著不足。研究背景是，真正的科研和工程进步本质上是一个长期、迭代的闭环过程，需要不断提出修改、运行实验、衡量结果并优化产物。然而，现有的评估基准存在两大缺陷：一是主要评估单轮响应或短时间代理轨迹，无法捕捉长时间跨度的持续改进挑战；二是已有的长期基准范围狭窄，每个基准仅针对单一领域（如机器学习工程、系统优化等），缺乏跨科学和工程领域的广泛覆盖，且容易达到性能饱和。因此，本文的核心问题是：当前最前沿的模型是否具备在长时间跨度内进行闭环优化的能力？为了填补这一空白，论文引入了AutoLab，这是一个全新的超长期闭环优化基准，包含36个跨四个不同领域（系统优化、谜题与挑战、模型开发和CUDA内核优化）的专家策划任务。每个任务都提供一个正确但故意次优的基线，并要求代理在严格的挂钟时间预算内进行迭代改进，从而测试模型在长时间跨度内进行持续迭代、管理时间和利用实证反馈的能力。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几类工作：**评测类基准**方面，现有基准如SWE-bench、MATH等主要评估单轮响应或短期智能体轨迹，而AutoLab聚焦于超长周期闭环优化，这是其核心区别。**方法类研究**中，ReAct、Reflexion等工作探索了智能体的迭代推理与反馈机制，但本文强调实际工程场景中的持续基准测试与编辑行为，而非单纯的语言反馈循环。**应用类工作**如AutoGPT、Coding Agents展示了长任务执行潜力，但AutoLab通过36个跨领域任务（系统优化、模型开发、CUDA优化等）系统评估，并揭示持久迭代比初始尝试质量更关键。与OpenAI的MLE-bench相比，AutoLab更侧重工程性优化而非纯算法启发性任务，且提供严格的时间预算控制。此外，CUDA kernel优化任务关联到Triton等底层编程研究，但本文强调自动化的闭环优化。总体而言，AutoLab通过设计现实、子最优任务及时间感知的评测框架，填补了现有基准在长周期迭代优化方面的空白，并揭示了当前前沿模型在持久性上的根本局限。

### Q3: 论文如何解决这个问题？

AutoLab通过构建一个超长周期闭环优化基准测试框架来解决现有评估无法捕捉持续迭代改进能力的问题。核心方法是将科学工程中的长期迭代过程（提出修改→运行实验→测量结果→改进工件）形式化为36个专家策划的真实任务，涵盖系统优化、谜题挑战、模型开发和CUDA内核优化四大领域。

整体框架采用“初始基线+严格时钟预算”的双约束设计：每个任务从一个正确但故意次优的基线开始，要求智能体在固定墙钟时间内持续改进。关键技术包括：（1）自动闭环评估系统，自动执行智能体生成的修改代码、测量性能指标并反馈结果；（2）迭代感知指标，不仅评估最终性能，还追踪智能体在时间预算内的迭代次数和每次迭代的改进幅度；（3）弹性交互协议，允许智能体自由选择规划、编码、测试和重新分析的时间分配。

主要模块包括任务生成器（确保基线次优性和改进空间）、评估调度器（管理多智能体并行实验的时钟约束）、以及性能追踪器（记录每次迭代的实证反馈）。创新点在于首次系统性地捕捉了智能体在长时间尺度上的持续迭代能力，特别是通过对比17个前沿模型，发现成功的关键不是初始尝试质量，而是在预算内坚持反复基准测试、编辑和整合实证反馈的持久性。

### Q4: 论文做了哪些实验？

论文进行了大规模多模型对比实验，在36个任务上评估了17个模型。任务分为四个领域：CUDA kernel优化、模型开发、谜题与挑战、系统优化。每个任务提供正确但次优的基线，要求代理在严格时间预算内迭代改进。评估指标包括Avg@3（三次运行平均分）、Best@3（最优分）和Dominance（模型间两两胜率）。实验使用Harbor框架和terminus-2代理，CPU任务在本地Docker沙箱运行，GPU任务在H100/L40S云沙箱运行，总耗时2544小时、消耗86亿token。主要模型包括claude-opus-4.6、gemini-3.1-pro、gpt-5.4、grok-4-20等闭源模型，以及qwen-3.6-plus、deepseek-v4-pro、glm-5、kimi-k2.6、hunyuan-3-preview、mimo-v2.5-pro、minimax-m2.7等开源模型。结果表明，claude-opus-4.6在整体Avg@3（0.68）、Best@3（0.76）和Dominance（0.93）上表现最佳，尤其在谜题与挑战领域（Avg@3=0.85）。gemini-3.1-pro和kimi-k2.6次之。关键发现是，成功的主要预测因素不是首次尝试的质量，而是迭代次数和持续融入实验反馈的能力。大多数前沿模型过早终止或预算耗尽前进展微小，凸显了时间感知和持续迭代的重要性。

### Q5: 有什么可以进一步探索的点？

根据论文分析，AutoLab揭示了当前前沿模型在超长周期优化任务中的核心局限：**时间感知与持久迭代能力的缺失**。未来可探索的方向包括：

1. **增强时间感知机制**：模型普遍无法合理校准探索与剩余预算的关系，要么过早终止（如gpt-5.4），要么耗尽预算未提交（如deepseek-v4-pro）。可引入显式的时间预算监控模块，或设计动态调整探索深度的策略，使模型能根据剩余时间主动改变行为。

2. **改进指令遵循与约束处理**：即使强闭源模型仍频繁违反任务约束（如使用禁用API）。需开发更鲁棒的约束嵌入方法，例如将禁止操作作为不可逆的"安全护栏"，或在奖励建模中强化约束违反的惩罚。

3. **降低推理成本的同时保持性能**：DeepSeek等模型展现了低成本高性能的潜力，未来可探索稀疏激活、推理时预算分配等技术，使开源模型在长周期任务中更高效。

4. **构建更真实的评估环境**：当前任务均为单一初始基线，未来可引入随时间动态变化的约束或目标，进一步逼近真实科研迭代的复杂性与不预见性。

### Q6: 总结一下论文的主要内容

AutoLab提出了一个新基准，专门用于评估前沿模型在超长时间跨度下的闭环优化能力。现有基准多聚焦单轮回答或短程交互，未能捕捉科学和工程研究中所需的持续迭代过程。AutoLab包含36个专家设计的任务，涵盖系统优化、谜题挑战、模型开发和CUDA内核优化四个领域。每个任务提供一个正确但次优的基线，要求智能体在严格时间预算内通过反复测试、编辑和整合实证反馈来改进。评估了17个模型后，发现预测成功的核心因素并非初始解的质量，而是持续迭代的毅力。Claude-opus-4.6表现最佳，但多数前沿模型因过早终止或预算耗尽而进展有限。该工作强调了时间感知与持续迭代在自主智能体中的关键作用，并开源了整个基准和评估工具，以推动长时域智能体的研究。
