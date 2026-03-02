---
title: "Scaling Generalist Data-Analytic Agents"
authors:
  - "Shuofei Qiao"
  - "Yanqiu Zhao"
  - "Zhisong Qiu"
  - "Xiaobin Wang"
  - "Jintian Zhang"
  - "Zhao Bin"
  - "Ningyu Zhang"
  - "Yong Jiang"
  - "Pengjun Xie"
  - "Fei Huang"
  - "Huajun Chen"
date: "2025-09-29"
arxiv_id: "2509.25084"
arxiv_url: "https://arxiv.org/abs/2509.25084"
pdf_url: "https://arxiv.org/pdf/2509.25084v2"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "Agent 训练"
  - "数据合成"
  - "工具使用"
  - "多步推理"
  - "代码执行"
  - "开源模型"
  - "Agent 评测"
relevance_score: 9.0
---

# Scaling Generalist Data-Analytic Agents

## 原始摘要

Data-analytic agents are emerging as a key catalyst for automated scientific discovery and for the vision of Innovating AI. Current approaches, however, rely heavily on prompt engineering over proprietary models, while open-source models struggle to face diverse-format, large-scale data files and long-horizon, multi-step reasoning that real-world analytics demands. This paper introduces DataMind, a scalable data synthesis and agent training recipe designed to build generalist data-analytic agents. DataMind tackles three key challenges in building open-source data-analytic agents, including insufficient data resources, improper training strategy, and unstable code-based multi-turn rollout. Concretely, DataMind applies 1) a fine-grained task taxonomy and a recursive easy-to-hard task composition mechanism to increase the diversity and difficulty of synthesized queries; 2) a knowledge-augmented trajectory sampling strategy followed by model-based and rule-based filtering; 3) a dynamically adjustable training objective combining both SFT and RL losses; 4) a memory-frugal and stable code-based multi-turn rollout framework. Built on DataMind, we curate DataMind-12K, a high-quality trajectory set spanning diverse domains, task categories, and data file formats for data-analytic tasks. Trained on DataMind-12K, our DataMind-14B achieves state-of-the-art with an average score of 71.16% on multiple data analysis benchmarks, outperforming the strongest proprietary baselines DeepSeek-V3.1 and GPT-5. Our DataMind-7B also performs best among all open-source models with a score of 68.10%. We also incorporate some empirical insights gained from our exploratory trials into the analysis experiments, aiming to provide actionable insights about agentic training for the community. We will release DataMind-12K and DataMind-7B,14B for the community's future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决构建通用、开源的数据分析智能体（Data-Analytic Agents）所面临的核心挑战。研究背景是，大型语言模型在推理任务上展现出强大能力，数据分析智能体作为实现“创新AI”和自动化科学发现的关键工具日益重要。然而，现有方法严重依赖基于闭源模型（如GPT系列）的提示工程，或使用预定义的工作流；而现有的开源模型则能力有限，只能处理能塞进提示的简单表格任务，难以应对现实世界数据分析中常见的多样化格式、大规模数据文件以及长视野、多步骤的复杂推理。

现有方法的不足主要体现在三个方面：一是**数据资源不足**，公开的数据分析基准通常只提供有限的测试集，缺乏带详细步骤注释的高质量训练轨迹数据；二是**训练策略不当**，当前智能体训练通常遵循“监督微调后强化学习”的范式，但在新场景下如何稳定长视野训练以及如何分配不同训练阶段的步长以取得最优性能，尚不明确；三是**基于代码的多轮次展开不稳定**，数据文件和代码解释器涉及复杂的内存管理，在有限内存资源下进行并行智能体展开和多轮代码生成会加剧不稳定性。

因此，本文要解决的核心问题是：如何通过一个可扩展的数据合成与智能体训练方案（即DataMind），系统地克服上述挑战，从而成功训练出性能强大的通用型开源数据分析智能体，使其能够稳健地处理多样化、大规模的真实世界数据分析任务。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕数据智能体（Data-Analytic Agents）的构建与训练展开，可分为方法类、应用类和评测类。

**方法类**：现有工作主要依赖基于闭源模型（如GPT系列）的提示工程（prompt engineering）或预定义的多智能体工作流来构建数据智能体。例如，一些研究通过设计复杂的提示链或协作框架来处理数据分析任务。然而，这些方法通常无法直接迁移到开源模型上，且缺乏针对大规模、多格式数据及长程推理的专门训练。本文提出的DataMind则专注于为开源模型设计一套可扩展的数据合成与训练方法，通过细粒度任务分类、递归任务组合、知识增强轨迹采样以及动态混合SFT与RL损失等技术，解决了现有方法在数据资源、训练策略和代码执行稳定性方面的不足。

**应用类**：在自动化数据分析领域，已有研究致力于将LLMs应用于科学发现和决策支持，但多数局限于处理结构简单的表格数据（如能嵌入提示的小型表格），难以应对现实世界中多样格式（如CSV、JSON）和大规模数据文件。本文的DataMind通过合成涵盖多领域、多任务类别和多格式的高质量轨迹集（DataMind-12K），并训练出通用型智能体（DataMind-7B/14B），显著提升了开源模型在复杂数据分析场景下的能力。

**评测类**：当前存在多个数据智能体评测基准，用于评估模型在数据分析任务上的性能。然而，这些基准通常仅提供有限的测试集，缺乏带详细步骤注释的训练轨迹，导致难以直接用于训练。本文不仅在这些基准上取得了领先性能（超越DeepSeek-V3.1和GPT-5等闭源模型），还通过构建大规模训练集填补了数据资源的空白，为社区提供了可复现的训练基础。

总之，本文与相关工作的核心区别在于：它系统性地解决了构建开源通用数据智能体的三大挑战（数据不足、训练策略不当、代码执行不稳定），并通过可扩展的管道实现了在多个基准上的最先进性能，同时为智能体训练提供了实证见解。

### Q3: 论文如何解决这个问题？

论文通过提出名为DataMind的可扩展数据合成与智能体训练方案来解决构建开源数据分析智能体所面临的三大挑战：数据资源不足、训练策略不当以及基于代码的多轮交互不稳定。其核心方法是一个包含数据合成、轨迹采样、训练优化和稳定交互的完整框架。

在数据合成方面，首先从Kaggle、BIRD等开源平台收集并过滤了CSV、Excel和SQLite等多种格式的数据文件。随后，设计了一个细粒度的任务分类法（18个类别），并利用大模型（DeepSeek-V3）基于文件元数据自动生成多样化查询。关键创新在于引入了递归的“由易到难”任务组合机制，通过将多个基础任务类型链式组合（迭代2-5次），生成了需要多步推理的复杂查询，显著提升了合成任务的难度和多样性。

为确保训练轨迹的质量，论文提出了知识增强的轨迹采样框架。首先为每类任务手动设计高级工作流程知识，引导专家模型（DeepSeek-V3.1）生成轨迹。通过采样多条轨迹并利用评判模型（GPT-4o-mini）进行自洽性检查，仅保留答案一致的轨迹，并选取其中最简洁准确的一条。对于未通过检查的轨迹，创新性地引入了“反思循环”：将评判模型的推理链反馈给专家模型，促使其修正轨迹，从而在提升数据质量的同时丰富了思维模式的多样性。此外，还实施了基于规则的三阶段过滤（格式合规、长度控制、语言完整性），最终得到了高质量轨迹集DataMind-12K。

在训练架构上，采用了监督微调（SFT）与强化学习（RL）动态结合的混合范式。创新点在于设计了一个动态可调的最终损失函数，将SFT损失和RL损失（采用DAPO算法）通过一个动态权重因子γ进行加权。训练初期γ值较大，侧重于从专家数据中吸收知识；随后逐渐衰减，鼓励模型通过RL进行探索。这种设计避免了传统“先SFT后RL”管道中可能出现的知识僵化或探索不足的问题。同时，通过过滤无效轮次（void turns）来稳定训练过程。

为了应对代码执行环境不稳定的挑战，论文设计了一个内存高效且稳定的基于代码的多轮交互框架。其核心优化包括：1）异步交互，解耦GPU生成与CPU代码执行的峰值内存需求；2）分块代码维护，采用轻量级笔记本式策略，仅维护文本代码块而非全局变量池，在运行时拼接执行，大幅降低内存开销；3）安全控制，包括运行环境隔离、资源限制和不安全代码过滤。奖励函数则综合了格式奖励、答案奖励（基于模型评判）和长度奖励，以鼓励正确且简洁的输出。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了评估：DABench、TableBench和BIRD，使用GPT-4o-mini作为评判模型来评估最终答案的正确性，并报告了pass@1和pass@3分数。实验设置方面，使用LlamaFactory进行监督微调（SFT），学习率为1e-5，全局批次大小为16；使用verl进行强化学习（RL），学习率为1e-6，批次大小为32。推理时温度固定为0.7，top-p为0.95。

对比方法包括五大专有模型（如GPT-4o、DeepSeek-V3.1、GPT-5）和多个开源模型（如Qwen-2.5-Coder、Llama-3.3），以及四个专门针对数据分析任务训练的开源基线模型：TableLLM、Table-R1、OmniSQL和SQL-R1。实验以Qwen-2.5-Coder-7B和14B为骨干模型进行比较。

主要结果显示，基于DataMind训练的DataMind-14B模型在多个基准测试中取得了平均71.16%的pass@1分数，超越了所有专有模型（包括DeepSeek-V3.1和GPT-5）和开源替代方案。DataMind-7B模型在开源模型中表现最佳，平均pass@1分数为68.10%。具体数据指标上，DataMind-14B在DABench、TableBench和BIRD的pass@1分数分别为80.29%、70.95%和62.23%；DataMind-7B的对应分数为77.30%、67.60%和59.41%。此外，论文还进行了消融实验，包括数据规模影响（采样2K、4K、8K实例训练）和训练策略比较（SFT、zero-RL、SFT-then-RL、SFT-and-RL），结果显示SFT-and-RL策略效果最佳，且性能随数据量增加而提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的DataMind框架在构建开源通用数据分析智能体方面取得了显著进展，但其仍有进一步探索的空间。局限性主要体现在：1）合成数据虽多样，但可能仍与真实世界中复杂、模糊且多模态的用户需求存在差距；2）训练主要基于合成轨迹，智能体在开放环境中的鲁棒性、对错误或意外输入的适应性有待验证；3）多轮交互框架的稳定性虽被强调，但长期记忆、复杂状态管理和动态规划能力仍需加强。

未来研究方向可包括：1）探索更真实的数据合成或引入真实人机协作轨迹，以更好地模拟实际分析场景中的歧义与协作需求；2）将强化学习与环境模拟器更深度结合，让智能体在更接近真实反馈的循环中学习决策与纠错；3）研究模块化或分层智能体架构，将数据分析任务分解为规划、工具调用、验证等子模块，提升可解释性与可控性；4）扩展智能体处理非结构化数据（如图像、文本报告）与跨领域知识融合的能力，向真正的“通用科学发现助手”迈进。这些方向有望进一步提升智能体的实用性、泛化能力和人机协作效率。

### Q6: 总结一下论文的主要内容

本文针对构建通用数据分析智能体（Agent）面临的挑战，提出了一个名为DataMind的可扩展数据合成与智能体训练方案。核心问题是现有开源模型难以处理现实世界中格式多样、规模庞大的数据文件以及需要长视野、多步骤推理的分析任务。DataMind通过四个关键方法应对三大挑战：1）设计细粒度任务分类法和递归式由易到难的任务组合机制，以增强合成查询的多样性与难度；2）采用知识增强的轨迹采样策略，并结合基于模型和规则的过滤，以提升数据质量；3）使用结合监督微调（SFT）和强化学习（RL）损失的动态可调训练目标；4）构建一个内存高效且稳定的基于代码的多轮次执行框架。基于此方案，作者构建了高质量轨迹数据集DataMind-12K，并训练出DataMind-7B和14B模型。实验表明，DataMind-14B在多个数据分析基准测试中平均得分达71.16%，超越了最强的专有模型基线，而DataMind-7B也在开源模型中表现最佳。该工作为社区提供了构建高性能、可扩展通用数据分析智能体的有效路径和开源资源。
