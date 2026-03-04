---
title: "StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning"
authors:
  - "Shiyang Li"
  - "Zijian Zhang"
  - "Winson Chen"
  - "Yuebo Luo"
  - "Mingyi Hong"
  - "Caiwen Ding"
date: "2026-03-03"
arxiv_id: "2603.02637"
arxiv_url: "https://arxiv.org/abs/2603.02637"
pdf_url: "https://arxiv.org/pdf/2603.02637v1"
categories:
  - "cs.MA"
  - "cs.CL"
  - "cs.PL"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "Agentic强化学习"
  - "工具使用"
  - "代码生成"
  - "自动化编程"
relevance_score: 9.0
---

# StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning

## 原始摘要

Modern machine learning (ML) workloads increasingly rely on GPUs, yet achieving high end-to-end performance remains challenging due to dependencies on both GPU kernel efficiency and host-side settings. Although LLM-based methods show promise on automated GPU kernel generation, prior works mainly focus on single-kernel optimization and do not extend to end-to-end programs, hindering practical deployment.
  To address the challenge, in this work, we propose StitchCUDA, a multi-agent framework for end-to-end GPU program generation, with three specialized agents: a Planner to orchestrate whole system design, a Coder dedicated to implementing it step-by-step, and a Verifier for correctness check and performance profiling using Nsys/NCU. To fundamentally improve the Coder's ability in end-to-end GPU programming, StitchCUDA integrates rubric-based agentic reinforcement learning over two atomic skills, task-to-code generation and feedback-driven code optimization, with combined rubric reward and rule-based reward from real executions. Therefore, the Coder learns how to implement advanced CUDA programming techniques (e.g., custom kernel fusion, cublas epilogue), and we also effectively prevent Coder's reward hacking (e.g., just copy PyTorch code or hardcoding output) during benchmarking. Experiments on KernelBench show that StitchCUDA achieves nearly 100% success rate on end-to-end GPU programming tasks, with 1.72x better speedup over the multi-agent baseline and 2.73x than the RL model baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动化生成高性能、端到端GPU程序的核心挑战。研究背景是现代机器学习工作负载日益依赖GPU，但其端到端性能不仅取决于单个GPU内核的效率，还受主机端设置（如内存分配、CPU-GPU重叠）等系统级因素的显著影响。尽管基于LLM的代码生成方法在自动化GPU编程方面展现出潜力，但现有方法存在明显不足。

现有方法主要包括多智能体系统和针对特定领域的微调或强化学习（RL），但它们大多局限于单内核优化（例如，仅优化一个3D最大池化内核），无法处理包含多个交互内核和复杂系统级协调的完整端到端程序。例如，像VisionTransformer这样的模型，其性能瓶颈往往超越单个内核，涉及内核融合边界、启动配置和同步等问题。现有的多智能体方法（如CUDAForge）在单内核任务上表现良好，但缺乏跨内核优化和主机端编排的机制，导致在端到端任务上成功率低、性能提升有限。此外，直接应用基于可验证奖励的强化学习（RLVR）来提升编码智能体（Coder）能力的方法，容易导致“奖励黑客”行为（例如，直接复制PyTorch代码或硬编码输出），产生无意义的退化解决方案，且未能训练模型有效利用结构化反馈（如性能剖析结果）进行针对性优化。而理论上能解决此问题的多轮次智能体强化学习，则因在真实CUDA环境中收集多轮交互数据计算开销巨大，导致训练效率极低。

因此，本文要解决的核心问题是：如何构建一个能够自动化生成和优化完整端到端GPU程序的框架。具体而言，论文提出了StitchCUDA框架，它通过一个包含规划、编码、验证三个专门智能体的多智能体系统来应对端到端程序所需的全局协调挑战。更重要的是，为了从根本上提升编码智能体在端到端GPU编程中的能力，并克服现有RL方法的缺陷，本文创新性地引入了基于量规的智能体强化学习。该方法将多轮智能体强化学习分解为“从零生成”和“反馈驱动优化”两个原子技能进行高效训练，并结合基于真实执行的规则奖励与由高级LLM生成的、与专家对齐的量规奖励，从而有效防止奖励黑客行为，引导模型学习实现高级CUDA编程技术，并可靠地依据反馈进行优化，最终实现高效的端到端GPU程序自动生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基准与任务定义、智能体工作流以及强化学习训练范式。

在**基准与任务定义**方面，KernelBench 为评估LLM的CUDA编程能力提供了标准，但其Level 1/2主要关注单核生成，而本文的StitchCUDA旨在解决更复杂的、涉及多核与主机编排的端到端程序合成（对应Level 3/4）。

在**智能体工作流**方面，CUDAForge、cuPilot、astra和QiMeng等系统通过将开发循环外部化为多智能体工作流，专注于单核的迭代优化与性能调优。然而，这些方法在扩展到端到端程序时，面临局部最优、规范漂移、代码上下文过长和收敛不稳定等结构性限制。StitchCUDA通过引入专门的Planner、Coder和Verifier三个智能体进行分工协作，并采用基于量规的强化学习，旨在克服这些可扩展性挑战。

在**强化学习训练范式**方面，Kevin、CUDA-L1和CUDA-L2等工作利用基于功能正确性和运行加速比的奖励对LLM进行后训练，以优化内核生成。但这些方法容易导致奖励破解（如复制PyTorch代码）和退化行为，且模型难以解释结构化执行反馈。StitchCUDA提出的基于量规的智能体强化学习，结合了量规奖励和基于实际执行的规则奖励，旨在更有效地训练Coder掌握端到端编程技巧，并防止奖励破解。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为StitchCUDA的多智能体端到端框架，并结合基于量规的智能体强化学习来解决端到端GPU编程的挑战。其核心方法、架构设计和关键技术如下：

**整体框架与工作流程**：StitchCUDA采用一个由三个专门智能体（Planner、Coder、Verifier）组成的多智能体系统，它们在一个共享全局状态机的协调下，通过“编码-反馈”迭代循环协同工作。Planner首先解析参考PyTorch代码，通过性能剖析（Nsys）识别系统热点和主导内核，并生成结构化的任务清单。Coder根据清单逐步实现CUDA代码（包括内核、主机端编排等），并进行编译。Verifier则负责验证正确性和剖析性能：若编译失败，提供具体修复指导；若测试通过，则使用Nsys和NCU进行两级诊断（识别系统级瓶颈和内核级性能特征），并生成可操作的优化建议。整个循环由Verifier根据测试结果路由控制，决定重试、优化、推进下一任务、重新规划或停止。

**主要模块与创新点**：
1.  **专业化多智能体协同**：三个智能体各司其职，形成了从系统规划、代码实现到验证优化的完整闭环。Planner运用思维链提示进行系统级推理与分解；Coder负责具体的CUDA项目生成；Verifier则集成了RAG（检索增强生成）技术，能参考最新的GPU硬件和CUDA库文档来提供更有效的优化反馈。
2.  **基于量规的智能体强化学习**：这是提升Coder能力的核心技术。为了在避免高昂的多轮交互成本的同时获得强化学习的好处，该方法将多轮学习分解为两个原子技能进行单轮训练：**技能1**（根据PyTorch代码和子任务要求生成CUDA内核）和**技能2**（根据反馈优化现有内核）。训练使用GRPO算法。
3.  **创新的奖励函数设计**：最终的奖励函数结合了基于规则（正确性和加速比）的奖励和基于量规的奖励。**量规奖励**由CUDA专家设计，从四个维度评估候选内核：反黑客行为（防止奖励欺骗）、CUDA工程（奖励高级优化技术）、算子覆盖（鼓励对复杂多操作程序的优化）和技能符合度（确保遵循任务或反馈要求）。该奖励通过一个归一化公式转化为稳定的 shaping 信号，与规则奖励结合，有效鼓励了真正的内核优化并抑制了奖励黑客行为（如直接复制PyTorch代码或硬编码输出）。

**关键技术总结**：通过多智能体分工与迭代循环解决了端到端编程的系统性协调问题；通过将多轮RL分解为原子技能的单轮训练，实现了高效的能力提升；通过精心设计的量规奖励与规则奖励相结合，引导模型学习复杂的CUDA优化技术并避免了训练退化。实验表明，该方法在端到端任务上实现了接近100%的成功率，并显著超越了基线模型。

### Q4: 论文做了哪些实验？

论文在KernelBench基准上进行了实验，该基准包含三个级别：Level 1（20个单核任务，如批处理矩阵乘法）、Level 2（20个单文件多核任务，如Conv2D+ReLU+BiasAdd）和Level 3（10个端到端GPU编程任务，如完整VisionTransformer推理）。实验在NVIDIA H200（Hooper架构）和RTX PRO 6000（Blackwell架构）GPU上进行。对比方法包括通用LLM（GPT-5.2、Claude-4-sonnet）、领域专用LLM（Qwen3-32B、Kevin32B）、开源多智能体框架CUDAForge，以及StitchCUDA的不同变体（使用不同Coder模型）。评估指标包括正确率（Success Rate）、端到端平均加速比（E2E Average Speedup）和综合指标Fast₁。

主要结果：在最具挑战性的Level 3任务上，StitchCUDA（使用经过强化学习的Qwen3-32B作为Coder）在RTX PRO 6000上达到10/10正确率、1.27倍加速比和70% Fast₁；在H200上达到9/10正确率、1.50倍加速比和70% Fast₁，显著优于基线。多智能体协调大幅提升了正确率和加速比（例如Qwen3-32B在H200 Level 1上从2/20正确率提升至17/20）；基于量规的智能体强化学习进一步优化了端到端性能（如StitchCUDA相比无强化学习变体StitchCUDA-Q，在H200 Level 3上加速比从0.24倍提升至1.50倍）。此外，实验还表明StitchCUDA能有效抑制奖励黑客行为（如仅输出PyTorch代码或硬编码结果），其部分黑客次数为8/50，低于对比方法。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向可从多个维度展开。首先，StitchCUDA 虽通过多智能体与规则奖励机制缓解了奖励欺骗和模型退化行为，但其验证器（Verifier）依赖 Nsys/NCU 等外部性能分析工具，这可能导致反馈延迟和资源开销较大。未来可探索轻量级、在线式的性能预测模型，以加速迭代优化过程。其次，框架目前主要针对 CUDA 生态，未来可扩展至其他并行编程模型（如 ROCm、SYCL）或新兴硬件架构（如 NPU、Chiplet），提升通用性。

从方法学角度看，论文中提到的智能体“缺乏信心”问题，揭示了当前 LLM 在复杂优化任务中决策保守的本质。未来可结合课程学习（Curriculum Learning），让智能体从简单子任务逐步过渡到复杂端到端优化，或引入不确定性量化机制，使模型能评估自身决策的置信度，从而更敢于尝试激进优化。此外，奖励设计虽结合了规则与量规（Rubric），但仍可能无法完全覆盖真实场景的多样性。可探索基于人类偏好或多目标 Pareto 优化的奖励模型，以平衡正确性、性能、能效等多重指标。

最后，实验评估集中于合成任务（KernelBench），未来需在真实世界、动态变化的 ML 工作负载（如推荐系统、科学计算）中验证框架的鲁棒性与泛化能力。同时，可研究智能体间的协作机制是否可进一步自动化，例如引入元学习让 Planner 能动态调整任务分解策略，以应对更复杂的异构计算场景。

### Q6: 总结一下论文的主要内容

该论文提出了StitchCUDA，一个用于端到端GPU程序生成的自动化多智能体框架，旨在解决现有基于大语言模型的方法通常只关注单内核优化、难以生成完整可部署程序的问题。其核心贡献在于设计了一个包含规划、编码和验证三个专门智能体的多智能体系统，并通过基于量规的智能体强化学习从根本上提升了编码智能体的能力。方法上，规划智能体负责整体系统设计，编码智能体通过强化学习训练其“任务到代码生成”和“反馈驱动优化”两项原子技能，验证智能体则利用性能剖析工具进行正确性检查和性能分析；其强化学习结合了来自量规的奖励和实际执行的规则奖励，有效防止了奖励欺骗行为。主要结论显示，该框架在KernelBench测试集上实现了接近100%的端到端任务成功率，性能分别优于多智能体基线1.72倍和强化学习模型基线2.73倍，显著推进了自动化GPU编程的实用化。
