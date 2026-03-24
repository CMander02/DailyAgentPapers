---
title: "SWE-Next: Scalable Real-World Software Engineering Tasks for Agents"
authors:
  - "Jiarong Liang"
  - "Zhiheng Lyu"
  - "Zijie Liu"
  - "Xiangchao Chen"
  - "Ping Nie"
  - "Kai Zou"
  - "Wenhu Chen"
date: "2026-03-21"
arxiv_id: "2603.20691"
arxiv_url: "https://arxiv.org/abs/2603.20691"
pdf_url: "https://arxiv.org/pdf/2603.20691v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "SWE Agent"
  - "Data Collection"
  - "Execution-Grounded"
  - "Benchmark"
  - "Software Engineering"
  - "Self-Verifying"
  - "Scalability"
relevance_score: 9.0
---

# SWE-Next: Scalable Real-World Software Engineering Tasks for Agents

## 原始摘要

Executable software engineering data is valuable for training SWE agents, but scaling it remains difficult for two reasons: only a small fraction of real repository changes yield verifiable, high-signal task instances, and naively building repository-specific environments quickly becomes the dominant systems cost. We present SWE-Next, an execution-grounded framework for scalable SWE task and trajectory collection. On the data side, SWE-Next mines real merged pull requests, executes candidate base/merged commit pairs, and retains only those that produce strict test improvements without regressions, yielding self-verifying instances. It also applies strict submission gating so that collected trajectories remain evidence-driven rather than speculative. On the systems side, SWE-Next introduces reusable repo-quarter profiles, which reuse the same environment across nearby commits in time while keeping each task run separate and reproducible. Using only 30 hours and 639GB of environment storage, SWE-Next processes 3,971 seed repositories and 102,582 candidate commit pairs mined from real merged PRs to construct a dataset of 2,308 self-verifying instances. Experiments show that SWE-Next improves downstream pass@1 with fewer or comparable training trajectories, indicating that its gains come not from a stronger trajectory generator, but from higher-signal execution-grounded supervision and more efficient data collection.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决为训练软件工程（SWE）智能体而大规模收集高质量、可执行任务数据时所面临的核心挑战。研究背景是，基于大语言模型的智能体在软件工程等具体任务中展现出潜力，但其有效训练依赖于大量可通过执行环境验证的真实任务。现有方法存在两大不足：首先，从真实代码仓库中挖掘的变更（如合并的拉取请求）只有极少数能产生可验证、高价值（high-signal）的任务实例，现有数据收集方法容易引入弱过滤、监督信息泄露或推测性提交，导致训练数据质量不高；其次，在系统层面，为每个任务或代码仓库单独构建和存储专用执行环境的成本极高，这种“一次性”环境管理方式导致存储开销巨大（可达TB级别）、处理效率低下，成为大规模数据收集的主要瓶颈。

因此，本文要解决的核心问题是：如何设计一个可扩展的框架，既能从真实软件仓库中自动筛选出严格可验证、高质量的任务实例，又能通过高效的环境复用机制大幅降低系统开销，从而实现大规模、实用的软件工程任务与轨迹数据收集。具体而言，论文提出的SWE-Next框架试图同时攻克数据质量（通过执行测试仅保留能带来严格改进且无回归的提交对，确保任务自验证）和系统可扩展性（引入可重用的“仓库季度档案”来复用时间上邻近提交的环境）这两大难题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**仓库级软件工程评估与智能体**以及**可扩展且可验证的可执行软件工程数据收集**。

在**仓库级软件工程评估与智能体**方面，SWE-Bench及其Verified子集是核心工作，为现实问题解决提供了标准化、测试验证的框架。这区别于HumanEval等孤立代码生成基准，要求智能体进行长视野推理、处理依赖关系和探索大型代码库。现有智能体主要分为两类：工作流系统（将问题分解为定位、编辑等阶段，缩短了推理视野但依赖大量人工先验）和通用交互式智能体（更依赖基础模型进行长视野规划）。本文与这些工作的关系在于，同样关注仓库级任务，但指出它们的共同局限是缺乏高质量训练数据和大规模可执行环境，这导致了对强大专有模型和复杂提示系统的依赖。SWE-Next旨在通过其数据收集框架缓解这一数据瓶颈。

在**可扩展且可验证的可执行软件工程数据收集**方面，相关研究致力于构建现实、可验证且可扩展的数据集，涉及可扩展环境构建、自动化任务收集、基于测试信号的可执行训练环境等。这些工作普遍面临规模、真实性和验证成本之间的权衡：合成数据可扩展但迁移性弱，而人工创建的任务或重型环境则有效但难以扩展。**本文SWE-Next直接针对这一权衡，其核心区别与贡献在于**：一方面，通过执行验证过滤真实的合并PR候选，提高了监督信号的质量（获得“自我验证”实例）；另一方面，通过引入可重用的“仓库季度档案”环境抽象，显著降低了收集开销和存储成本。与一些同样利用收集轨迹进行后训练的最新工作相比，SWE-Next更强调通过严格的提交门控和稳定的环境来确保任务实例构建的可靠性，从而为可扩展的数据收集提供更实用的基础。

### Q3: 论文如何解决这个问题？

论文通过一个名为SWE-Next的、基于执行验证的框架来解决可扩展的软件工程（SWE）任务和轨迹收集问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心方法：**
SWE-Next的流程分为数据生成和系统优化两个紧密耦合的方面。在数据侧，它从真实的、已合并的GitHub拉取请求（PR）中挖掘候选的提交对（基础提交 `c_base` 和合并后提交 `c_merged`）。关键在于，它通过**执行验证过滤**来确保数据质量：在构建的环境中，对两个提交运行固定的仓库测试命令，仅保留那些能产生严格测试改进（例如，失败的测试通过）且没有引入回归（例如，已通过的测试未失败）的提交对。这产生了**自验证任务实例**，其正确性由执行而非人工标注保证。此外，在收集代理解决这些任务的轨迹时，框架采用**严格提交门控**（例如，代理必须产生非空代码差异并至少运行一次测试命令才能提交），以确保收集到的监督信号是基于证据的，而非猜测。

**主要模块/组件与创新点：**
1.  **可重用的仓库季度配置文件（Quarter Profiles）**：这是解决系统扩展性瓶颈的核心创新。传统方法为每个提交对构建独立的重型Docker环境，导致依赖安装重复，成本高昂。SWE-Next引入“季度配置文件”概念，根据提交时间戳将每个提交确定性地映射到一个粗粒度的`仓库名_年Q季度`配置文件。这近似代表了一个依赖项版本区间。
2.  **季度环境（可重用镜像）与运行时快照挂载**：
    *   **构建时**：为每个配置文件构建一个共享的季度环境镜像。该镜像**仅包含可跨提交重用的组件**，如系统包、Python解释器以及一个缓存了pytest和配置文件特定依赖的虚拟环境。**关键创新在于，镜像不包含仓库源代码**，从而实现了环境与代码的解耦。
    *   **运行时**：执行时，将特定提交的仓库代码快照以只读方式挂载，然后通过“启动时复制”机制复制到一个可写的工作空间。同时，将共享的季度环境链接到工作目录。这样，同一个季度环境镜像可以被许多不同代码提交的任务实例重用，无需重建，极大地**分摊了环境构建成本**。
3.  **鲁棒性与回退机制**：季度配置优化并非硬性假设。当某个季度环境构建失败，或不足以支持某个罕见提交时，系统会**回退到为该提交构建专属的每提交环境**，以避免丢失任务覆盖。这种设计在追求重用效率的同时保证了系统的健壮性。
4.  **任务实例化与自然语言问题生成**：验证通过后，每个实例被转换为包含基础提交、真实补丁（分为代码差异和测试差异）和可执行环境规范的数据行。为了便于代理提示，框架可选地使用LLM，根据执行工件（如差异摘要和失败测试证据）生成自然语言问题描述，从而无需手动编写问题。

**总结：**
SWE-Next通过**执行验证过滤**确保数据的高信号质量，并通过创新的**季度配置文件与可重用环境架构**（分离依赖层与代码快照）大幅降低了大规模处理时的系统成本。其严格的数据收集策略（自验证实例、提交门控）旨在提升监督信号的质量而非单纯增加数据量，实验表明这能使用更少或相当的训练轨迹提升下游模型性能。

### Q4: 论文做了哪些实验？

论文实验旨在评估SWE-Next框架在训练软件工程智能体方面的有效性，采用了端到端的微调流程。实验设置包括：首先从SWE-Next任务实例中采样子集；接着使用基于R2E-Gym的专家智能体系统（集成OpenHands风格工具调用）执行任务，收集包含工具调用、观察和代码编辑的逐步轨迹；然后对基础/学生模型进行监督微调（SFT）；最后在标准基准上评估智能体性能。

数据集方面，SWE-Next基于3,971个Python仓库挖掘了102,582个候选提交对，经过基于执行的过滤后，保留了2,308个自验证实例作为最终数据集。这些仓库与SWE-Bench数据集无重叠。使用Claude 4.5 Sonnet和GPT-5-mini专家模型生成了3.7k条训练轨迹，分为“干净成功”（最终测试通过、有真实代码编辑且早期测试证据可解析）和“恢复成功”（最终通过但包含早期失败测试）两类。为公平对比，还使用claude-3-5-sonnet-20240620在相同框架下生成轨迹。学生模型采用Qwen-2.5-Coder-Instruct 7B和14B，使用LLaMA-Factory进行全参数SFT，学习率为1.0×10⁻⁵，上下文长度32,768令牌，全局批次大小8，最多4轮训练。

对比方法主要基于不同轨迹数据源（如SWE-Next与其他来源）训练的模型。评估使用SWE-Bench-Lite（快速迭代）和SWE-Bench-Verified（高置信度验证）两个基准，以pass@1（智能体最终补丁通过基准评估的任务百分比）作为关键指标。主要结果显示，SWE-Next以更少或相当的训练轨迹提升了下游pass@1性能，表明其增益源于更高信号的自验证监督和更高效的数据收集，而非更强的轨迹生成器。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：首先，将框架扩展到Python以外的编程语言，如Java、JavaScript等，以验证其通用性并构建更全面的多语言软件工程任务数据集。其次，在更大规模上进行轨迹生成和数据收集，当前研究受限于计算资源和预算，未来可探索在数千甚至数万个仓库上运行，以检验框架在极端规模下的效率和信号质量保持能力。此外，论文主要关注测试改进类任务，未来可纳入更广泛的软件工程活动，如代码重构、性能优化或安全漏洞修复，以提升智能体的综合能力。从方法角度看，可研究更动态的环境复用策略，在保证隔离性的同时进一步降低存储开销。最后，结合更强大的基础模型（如代码大模型）进行轨迹生成，探索高质量监督信号与模型能力提升之间的协同效应，推动软件工程智能体向实用化迈进。

### Q6: 总结一下论文的主要内容

该论文提出了SWE-Next框架，旨在解决为软件工程（SWE）智能体构建可扩展、高质量训练数据的难题。核心问题是现有方法难以从真实代码仓库中高效筛选出可验证、高价值的任务实例，且构建特定仓库环境的系统成本过高。

方法上，SWE-Next包含数据与系统两方面的创新。在数据侧，它从已合并的Pull Request中挖掘基础提交与合并提交对，通过执行测试并严格筛选（仅保留测试有改进且无回归的实例）来创建自验证任务实例，同时采用提交门控确保收集的轨迹基于证据而非推测。在系统侧，它引入了可复用的仓库季度配置文件，能在时间相近的提交间共享同一环境，从而大幅降低存储与计算成本，同时保持每个任务运行的独立性与可复现性。

主要结论显示，SWE-Next仅用30小时和639GB存储，从3,971个种子仓库和102,582个候选提交对中构建了包含2,308个自验证实例的数据集。实验表明，该框架能以更少或相当的训练轨迹提升下游模型的pass@1性能，证明其收益源于更高信号强度的执行监督与更高效的数据收集机制，而非更强的轨迹生成器。该工作为大规模、真实的SWE智能体训练提供了可扩展的解决方案。
