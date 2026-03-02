---
title: "CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation"
authors:
  - "Weinan Dai"
  - "Hanlin Wu"
  - "Qiying Yu"
  - "Huan-ang Gao"
  - "Jiahao Li"
  - "Chengquan Jiang"
  - "Weiqiang Lou"
  - "Yufan Song"
  - "Hongli Yu"
  - "Jiaze Chen"
  - "Wei-Ying Ma"
  - "Ya-Qin Zhang"
  - "Jingjing Liu"
  - "Mingxuan Wang"
  - "Xin Liu"
  - "Hao Zhou"
date: "2026-02-27"
arxiv_id: "2602.24286"
arxiv_url: "https://arxiv.org/abs/2602.24286"
pdf_url: "https://arxiv.org/pdf/2602.24286v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "Agent Architecture"
  - "Tool Use"
  - "Data Synthesis"
  - "Agent Training"
  - "Code Generation"
  - "LLM-based Agent"
relevance_score: 9.0
---

# CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation

## 原始摘要

GPU kernel optimization is fundamental to modern deep learning but remains a highly specialized task requiring deep hardware expertise. Despite strong performance in general programming, large language models (LLMs) remain uncompetitive with compiler-based systems such as torch.compile for CUDA kernel generation. Existing CUDA code generation approaches either rely on training-free refinement or fine-tune models within fixed multi-turn execution-feedback loops, but both paradigms fail to fundamentally improve the model's intrinsic CUDA optimization ability, resulting in limited performance gains. We present CUDA Agent, a large-scale agentic reinforcement learning system that develops CUDA kernel expertise through three components: a scalable data synthesis pipeline, a skill-augmented CUDA development environment with automated verification and profiling to provide reliable reward signals, and reinforcement learning algorithmic techniques enabling stable training. CUDA Agent achieves state-of-the-art results on KernelBench, delivering 100\%, 100\%, and 92\% faster rate over torch.compile on KernelBench Level-1, Level-2, and Level-3 splits, outperforming the strongest proprietary models such as Claude Opus 4.5 and Gemini 3 Pro by about 40\% on the hardest Level-3 setting.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动生成高性能CUDA内核代码这一核心挑战。研究背景是现代深度学习基础设施高度依赖GPU内核，但其开发和优化需要深厚的硬件专业知识，门槛极高。尽管LLM在通用编程任务上表现出色，但在CUDA内核生成方面，现有方法仍无法与`torch.compile`等基于编译器的自动优化工具竞争，更遑论人类专家。

现有方法主要分为两类，均存在明显不足。第一类是无训练的精炼工作流，依赖人工设计的启发式规则和执行反馈进行迭代优化。这类方法无法从根本上弥补基础模型在CUDA编码能力上的固有缺陷，其性能提升严重受限于模型本身的能力上限。第二类方法是在固定的多轮执行反馈循环中对基础模型进行微调。这种方法将所有历史解决方案都纳入上下文，浪费了宝贵的上下文长度，并且限制了智能体自主学习和探索调试、搜索及性能分析策略的能力，导致学习效率低下。

因此，本文要解决的核心问题是：如何系统性地、从根本上提升LLM在CUDA内核编码与优化方面的内在能力，使其生成的代码在性能上能够超越传统编译器优化工具。为此，论文提出了CUDA Agent，这是一个大规模智能体强化学习系统，通过构建可扩展的数据合成管道、提供具备自动化验证与性能分析功能的技能增强型开发环境，以及设计稳定的强化学习算法，来培养模型在CUDA内核开发方面的专业“技能”，从而实现高性能内核的自动生成。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：方法类（基于显式搜索的训练免优化方法）和训练类（基于模型微调或强化学习的方法）。

在方法类中，STARK 采用多角色代理团队在树状搜索空间中进行规划、编码和调试；ReGraphT 构建检索增强的推理图并通过蒙特卡洛图搜索引导模型；EvoEngineer 将优化建模为代码演化问题，通过LLM驱动的进化循环迭代编辑；CudaForge 则设计双代理系统，通过性能剖析诊断瓶颈并提供反馈。这些工作均依赖基础模型的CUDA编码能力，在测试时通过搜索或迭代提升性能，但未从根本上增强模型内在的优化能力。本文的CUDA Agent与这些方法正交，其训练后的模型亦可结合此类测试时缩放技术。

在训练类中，Kevin 提出了多轮强化学习框架模拟开发者工作流；CUDA-L1 采用基于执行的对比强化学习评估多个内核变体；ConCuR 通过合成带推理轨迹的数据集微调模型得到KernelCoder。这些方法尝试通过训练提升模型，但受限于高质量数据稀缺、训练规模有限以及手工设计的优化循环，性能提升存在瓶颈。本文与它们的核心区别在于：通过可扩展的数据合成管道、技能增强的自动化验证与剖析环境，以及稳定的强化学习算法，实现了大规模代理强化学习，从根本上培养了模型的CUDA内核优化专长，并避免了数据泄露问题，从而取得了显著的性能突破。

### Q3: 论文如何解决这个问题？

论文通过构建一个大规模智能体强化学习系统来解决高性能CUDA内核生成问题，其核心方法围绕三个关键组件展开：可扩展的数据合成管道、集成了技能且防作弊的训练环境与稳健的奖励调度设计，以及实现稳定训练的强化学习算法技术。

整体框架遵循智能体强化学习范式。首先，针对高质量CUDA内核数据稀缺的瓶颈，设计了一个可扩展的数据收集管道。该管道从PyTorch库中爬取种子算子，然后利用大语言模型进行组合式合成（将最多5个算子融合为单一计算层），最后通过严格的执行反馈过滤（包括正确性、非随机性、防作弊和难度筛选）构建出包含6000个样本的精选训练数据集CUDA-Agent-Ops-6K。这种组合合成方法能创造融合任务，其优化难点并非孤立优化算子的简单叠加，从而有效扩展了任务空间。

在训练环境与智能体循环设计上，系统采用了与OpenHands框架对齐的ReAct风格智能体循环，交替进行推理、行动执行和观察，以支持迭代式编码、调试和性能优化。关键创新在于引入了“CUDA编码技能”，将CUDA特定的优化指令和工具（如性能分析工具）封装为智能体技能，并制定了标准化的内核优化流程SKILL.md，引导智能体分析瓶颈、实现自定义CUDA算子、在GPU沙箱中编译评估并迭代优化，直至性能超越torch.compile基线至少5%。

奖励机制方面，论文提出了一个稳健的奖励调度方案以替代不可靠的原始加速比奖励。该方案根据正确性和性能将奖励分数r划分为四个等级（-1, 1, 2, 3），核心是判断生成的核函数是否相对于Eager模式或torch.compile版本实现了超过5%的显著加速。同时，系统通过文件权限控制、禁止回退调用、多输入验证、精细化性能剖析管道以及禁用网络搜索等多种措施，有效避免了奖励黑客行为。

为确保强化学习训练的稳定性，论文提出了一套初始化策略来解决因CUDA编码数据在预训练中占比极低（<0.01%）导致的严重领域分布失配问题。具体包括：1）**单轮热身**：先在基础模型上执行单轮PPO强化学习，提升其CUDA内核生成基础能力。2）**演员模型初始化**：使用经过单轮强化学习的模型收集智能体轨迹，并通过拒绝微调进行过滤（仅保留获得正奖励且行为高效的轨迹），然后用这些轨迹对演员模型进行监督微调。3）**评论家模型初始化**：利用收集的轨迹数据及其结果奖励，通过广义优势估计计算目标价值，对评论家网络进行价值预训练。这套预热策略使得训练能够稳定进行200步，并实现奖励的持续增长。

最终，该系统通过上述大规模、高质量的合成数据、精心设计的技能化智能体环境与防黑客奖励机制，以及针对分布失配的稳定训练技术，共同促成了模型内在CUDA优化能力的根本性提升，从而在KernelBench基准上取得了超越torch.compile及最强专有模型的先进性能。

### Q4: 论文做了哪些实验？

论文在KernelBench基准上进行了全面的实验评估，该基准包含Level 1到Level 3共250个不同的算子任务。实验设置以Seed1.6（一个230B总参数、23B活跃参数的MoE模型）为基础模型，采用大规模智能体强化学习进行训练。训练使用全局批次大小1024，学习率分别为3e-6（行动者）和6e-6（评论者），并设计了CPU-GPU资源解耦的沙箱环境以确保稳定、无干扰的性能评测。

对比方法包括前沿的专有模型（Claude Opus 4.5和Gemini 3 Pro）以及强大的开源模型（GLM 4.6和Kimi K2），所有基线模型均在相同的智能体循环环境下评估。此外，论文还进行了深入的消融研究，分析了智能体循环、鲁棒奖励设计、拒绝采样微调（RFT）和价值预训练等关键组件的作用。

主要结果方面，CUDA Agent在KernelBench上取得了最先进的性能。关键数据指标如下：在整体任务上，其通过率（Pass Rate）达98.8%，相对于`torch.compile`的更快率（Faster Rate）达96.8%，几何平均加速比（Speed-up）为2.11倍。具体到不同难度级别：在Level-1、Level-2和Level-3任务上，相对于`torch.compile`的更快率分别达到100%、100%和92%。在最具挑战性的Level-3设置上，其性能比最强的专有模型（如Claude Opus）高出约40%。消融实验表明，移除智能体循环会导致性能大幅下降（更快率从96.8%降至14.1%）；移除鲁棒奖励设计或RFT、价值预训练中的任何一项，都会导致优化性能显著退化或训练不稳定。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心突破在于通过大规模智能体强化学习（Agentic RL）系统，结合数据合成、技能增强环境和稳定训练，显著提升了LLM生成高性能CUDA内核的能力。然而，该研究仍存在一些局限性和值得深入探索的方向：

首先，论文主要聚焦于特定基准测试集（KernelBench），其泛化能力有待验证。未来可探索该系统在更广泛、更复杂的真实世界内核优化任务（如动态形状、多GPU协同）上的表现，并研究如何减少对合成数据的依赖，增强对未知硬件配置和算子类型的适应能力。

其次，当前系统依赖于自动化验证和性能分析提供奖励信号，但奖励函数的设计可能过于简化。未来可以研究更细粒度的、多目标的奖励机制（如平衡性能、功耗、内存占用），甚至引入基于学习到的性能预测模型作为奖励，以减少实际编译和评测的开销。

此外，该方法依赖于大规模的强化学习训练，计算成本高昂。未来的改进方向包括：探索更高效的离线或混合强化学习算法；研究如何将习得的“优化技能”进行模块化或知识蒸馏，以迁移到更小的模型或新的任务上；以及探索如何让智能体主动构建内部的世界模型（如硬件行为模型），以实现更样本高效的推理和优化。

最后，从更广阔的视角看，这项工作展示了“环境+强化学习”赋能基础模型的潜力。未来的研究可以探索将此范式扩展到其他性能关键的系统软件领域（如数据库查询优化、网络协议栈调优），并研究智能体与人类专家协作的混合工作流。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为CUDA Agent的大规模智能体强化学习系统，旨在解决高性能CUDA内核生成的难题。核心问题是现有基于大语言模型的方法在CUDA内核优化上仍无法匹敌编译器系统，且传统微调或执行-反馈循环范式难以从根本上提升模型的底层优化能力。

其核心贡献在于构建了一个完整的智能体学习框架，包含三个关键组件：一个可扩展的数据合成流水线，用于生成训练数据；一个技能增强的CUDA开发环境，集成了自动化验证与性能分析功能，以提供可靠的奖励信号；以及一套确保训练稳定性的强化学习算法技术。

主要结论显示，CUDA Agent在KernelBench基准测试上取得了最先进的成果，在Level-1、Level-2和Level-3三个难度级别上分别比torch.compile快100%、100%和92%，并且在最难的Level-3设定上显著优于Claude Opus 4.5等最强专有模型约40%。这标志着通过大规模智能体强化学习，可以系统性地培养出超越现有编译器与通用大模型的、具备深度硬件专业知识的内核生成能力。
