---
title: "AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents"
authors:
  - "Sharareh Younesian"
  - "Wenwen Ouyang"
  - "Sina Rafati"
  - "Mehdi Rezagholizadeh"
  - "Sharon Zhou"
  - "Ji Liu"
  - "Yue Liu"
  - "Yuchen Yang"
  - "Hao Li"
  - "Ziqiong Liu"
  - "Dong Li"
  - "Vikram Appia"
  - "Zhenyu Gu"
  - "Emad Barsoum"
date: "2026-05-16"
arxiv_id: "2605.16819"
arxiv_url: "https://arxiv.org/abs/2605.16819"
pdf_url: "https://arxiv.org/pdf/2605.16819v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "代码Agent"
  - "Agent评测基准"
  - "GPU内核优化"
  - "泛化能力测试"
  - "多智能体对比"
relevance_score: 8.5
---

# AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents

## 原始摘要

GPU kernel optimization is increasingly critical for efficient deep learning systems, but writing high-performance kernels still requires substantial low-level expertise. Recent AI coding agents can iteratively read code, invoke compilers and profilers, and refine implementations, yet existing kernel benchmarks evaluate single LLM calls rather than full agent workflows, and none include both kernel-to-kernel optimization and unseen-configuration generalization testing. We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. The benchmark contains 196 tasks spanning HIP-to-HIP optimization, Triton-to-Triton optimization, and PyTorch-to-HIP translation, and evaluates complete agent workflows in isolated workspaces using gated compilation, correctness, and performance checks, centralized scoring and an unseen-configuration generalization protocol that tests whether optimizations transfer to input configurations the agent never observed. Across production agents including Cursor Agent, Claude Code, and Codex Agent, we find near-perfect compilation and high correctness rates on most task categories, with the strongest configurations achieving mean speedups of up to 6.89x on PyTorch-to-HIP, 6.69x on HIP-to-HIP, and 2.13x on Triton-to-Triton tasks. Our unseen-configuration evaluation shows that HIP-to-HIP and Triton-to-Triton optimizations largely transfer to unseen input shapes, while PyTorch-to-HIP exhibits substantial correctness drops, indicating that agents generating kernels from scratch frequently hardcode shape-specific assumptions. AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI编程智能体在GPU内核优化任务中缺乏全面、真实评估基准的问题。研究背景是，GPU内核优化对深度学习系统效率至关重要，但编写高性能内核需要深厚的底层硬件专业知识。现有AI编程智能体（如Cursor Agent、Claude Code）能够通过多轮迭代（编写、编译、测试、性能分析）来优化代码，模仿人类工程师的工作流程。然而，现有基准测试存在明显不足：SWE-bench针对通用软件工程，HumanEval评估单次代码生成，而KernelBench、TritonBench等虽然涉及内核生成，但仅通过单次大模型调用或轻量迭代提示，缺乏完整的工具调用智能体工作流，且不包含内核到内核的优化场景。更关键的是，没有基准测试评估智能体优化后的内核是否能够泛化到未见过的输入配置上。因此，本文提出AgentKernelArena，一个开源基准测试，包含196个任务（覆盖HIP到HIP、Triton到Triton优化，以及PyTorch到HIP翻译），通过隔离工作区中的编译、正确性和性能门控管线进行评估，并创新性地引入未见配置泛化测试，以揭示智能体在生成内核时是否硬编码了特定形状假设。

### Q2: 有哪些相关研究？

以下是相关研究的分类总结：

**方法类相关工作**：QiMeng-Kernel、AutoTriton、TritonForge、AdaExplore、GEAK等系统利用LLM优化或生成GPU内核，但它们采用不同的评估协议，难以跨系统比较。本文提出的AgentKernelArena为这些系统提供了统一标准化评估平台，可将它们作为新智能体接入。

**基准测试类相关工作**：包括KernelBench（从PyTorch规范生成内核，采用fast_p加速指标）、TritonBench（Triton内核生成）、ROCmBench（AMD GPU上的Triton任务）、robust-kbench（通过LLM验证器解决作弊问题）和MultiKernelBench（多硬件平台）。本文的三大创新点在于：1）评估在沙盒环境中多轮迭代的自主编译、测试和分析的智能体；2）新增内核到内核优化任务（HIP到HIP、Triton到Triton）；3）引入未见配置泛化测试来验证加速效果是否泛化。

**代码生成与智能体基准**：HumanEval/MBPP评估简单Python函数正确性，SWE-bench/AgentBench扩展到仓库级补丁和多环境任务，但都面向通用软件工程。本文专门针对性能关键的GPU编程领域。

**AI编码智能体**：SWE-agent、Cursor Agent、Claude Code、OpenAI Codex等已经从单次生成转向多轮工具增强开发，AgentKernelArena为这些智能体提供了GPU内核优化领域的专用基准，特别利用迭代编译和分析反馈的优势。

### Q3: 论文如何解决这个问题？

AgentKernelArena通过构建一个完整的代理评估系统和泛化测试协议来解决GPU内核优化基准测试的问题。核心设计是一个隔离的工作区执行框架，每个代理在独立的沙盒环境中运行，包含完整的任务源代码、编译工具链和评测脚本。工作流分三阶段：首先测量基线性能，然后让代理自主迭代优化（支持编译、执行、性能分析等交互），最后通过门控流水线统一评估——只有编译通过的代码才进入正确性测试，只有正确性通过的才测量性能。

关键组件包括：196个来自真实场景的任务，覆盖HIP-to-HIP（24个，测试优化现有内核的能力）、Triton-to-Triton（148个，来自vLLM和ROCmBench）、PyTorch-to-HIP（24个，从零生成内核，最困难）；领域知识速查表提供硬件架构和编程模型的最佳实践；集中式评分函数综合编译（20分）、正确性（100分）和加速比（100×s_k分），确保正确性优先于性能。

创新点在于引入未见配置泛化测试协议：为每个任务生成代理在优化过程中从未见过的输入形状，计算可见/未见配置间的加速比差距Δ_g，量化代理是真正学到了通用优化策略还是过拟合于特定形状。门控评估、隔离执行和多形状测试共同确保了基准测试的可靠性和可重复性。

### Q4: 论文做了哪些实验？

论文在AgentKernelArena基准上评估了三个生产级AI代理（Cursor Agent、Claude Code和Codex Agent）的GPU内核优化能力，每个代理使用多个底层模型，共196个任务，涵盖HIP-to-HIP（24任务）、Triton-to-Triton（148任务）和PyTorch-to-HIP（24任务）三类。所有实验在AMD Instinct MI300X上运行，超时3600秒，最大迭代3次，每个配置运行3次取平均。

主要结果：在所有代理配置中，编译率接近100%，正确率普遍较高（≥91%）。性能上，PyTorch-to-HIP加速最显著，平均加速比3.74–6.89×（如Cursor Agent/Opus 4.6 High达6.89×），geometric mean 2.19–4.64×；HIP-to-HIP平均1.44–6.69×，geometric mean 1.33–3.31×；Triton-to-Triton最困难，平均仅1.59–2.13×，geometric mean 1.01–1.31×。Claude Code/Opus 4.6在HIP-to-HIP上最佳（6.69×），Cursor Agent/Opus 4.7 High在Triton-to-Triton上领先（2.13×）。

此外，实验还测试了未见配置泛化能力：HIP-to-HIP和Triton-to-Triton泛化良好，条件正确率分别为93.6%–100%和90.9%–99.4%，但PyTorch-to-HIP仅59.7%–90.3%，表明从头生成的内核常硬编码形状相关假设，泛化性较差。

### Q5: 有什么可以进一步探索的点？

首先，当前研究的局限性在于仅针对单一GPU架构（AMD MI250）和有限迭代次数（max_iterations=3），这限制了结论的普适性。未来应扩展至多GPU架构（如NVIDIA H100、Intel Ponte Vecchio），并探索更大迭代预算对优化效果的非线性影响。其次，论文指出模型可用性差异导致跨模型比较受限，且开源模型因多文件上下文需求在单次调用中编译失败。一个关键改进方向是构建将开源模型封装为迭代代理的工程框架（如shell/compile/profile工具集成及错误重试策略），这能显著降低基准测试的门槛，同时验证开源模型在长时间迭代下的潜力。另外，当前任务覆盖在PyTorch-to-HIP翻译中暴露了硬编码形状假设问题，未来可设计对抗性测试集（如动态形状、不规则内存布局）来强化泛化能力的评估。最后，可借鉴AutoTriton等专用优化系统的思想，在代理中融入基于学习的自动调优模块（如RL驱动的autotune配置搜索），提升对不可见配置的鲁棒性。

### Q6: 总结一下论文的主要内容

AgentKernelArena提出了一个用于评测AI代码智能体GPU内核优化能力的开源基准测试。针对现有基准仅评估单次LLM调用、缺乏完整agent工作流测试及泛化性评估的问题，该基准包含196个任务，涵盖HIP-to-HIP优化、Triton-to-Triton优化和PyTorch-to-HIP翻译三类，通过封闭式编译、正确性和性能检查实现集中评分，并设计了未见配置泛化测试协议。实验评估了Cursor Agent、Claude Code、Codex Agent等生产级智能体，发现其在多数任务上近乎完美编译、正确率高，最优配置在PyTorch-to-HIP上平均加速6.89倍。然而，泛化评估揭示关键问题：PyTorch-to-HIP任务在未见输入配置上正确率下降高达40%，表明agent生成的代码常硬编码形状特定假设，导致可见配置上的指标被显著高估。该基准作为模块化可扩展框架，推动了agentic GPU内核优化在智能体、任务和硬件目标上的严格评估。
