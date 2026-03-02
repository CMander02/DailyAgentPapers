---
title: "SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale"
authors:
  - "Ibragim Badertdinov"
  - "Maksim Nekrashevich"
  - "Anton Shevtsov"
  - "Alexander Golubev"
date: "2026-02-27"
arxiv_id: "2602.23866"
arxiv_url: "https://arxiv.org/abs/2602.23866"
pdf_url: "https://arxiv.org/pdf/2602.23866v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Software Engineering Agent"
  - "Agent Training Data"
  - "Reinforcement Learning"
  - "Tool Use"
  - "Multi-Language"
relevance_score: 8.0
---

# SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale

## 原始摘要

Software engineering agents (SWE) are improving rapidly, with recent gains largely driven by reinforcement learning (RL). However, RL training is constrained by the scarcity of large-scale task collections with reproducible execution environments and reliable test suites. Although a growing number of benchmarks have emerged, datasets suitable for training remain limited in scale and diversity or often target a limited set of high-resource language ecosystems. We introduce SWE-rebench V2, a language-agnostic automated pipeline for harvesting executable real-world SWE tasks and constructing RL training environments at scale. The pipeline synthesizes repository-specific installation and test procedures via an interactive setup agent, and filters unsound instances using an ensemble of LLM judges, validated against human-verified SWE-bench annotations. Using this pipeline, we construct a dataset of 32,000+ tasks spanning 20 languages and 3,600+ repositories, with pre-built images for reproducible execution. To further scale training data, we additionally release 120,000+ tasks with installation instructions, fail-to-pass tests and rich metadata, where the problem statement is generated based on the original pull request description. We validate the collected instances through a diagnostic study that covers a subset of tasks in five programming languages across seven popular models, and provide instance-level metadata that flags common confounders such as overly restrictive tests and underspecified descriptions. We release the datasets, the collection and execution code, and associated artifacts to enable large-scale training of SWE agents across diverse languages and repositories.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决软件工程智能体（SWE Agent）大规模训练数据稀缺的问题，特别是缺乏跨多种编程语言、具备可复现执行环境和可靠测试套件的大规模任务集合。研究背景是，基于大型语言模型的软件工程智能体发展迅速，其性能提升很大程度上依赖于强化学习，而强化学习需要大量能提供稳定奖励信号（即测试结果）的可交互任务环境进行训练。现有方法，如SWE-bench等基准测试，虽然为评估智能体提供了标准，但它们通常规模有限、语言多样性不足（主要集中于Python等高资源语言生态系统），且构建过程严重依赖人工验证，导致成本高昂、可扩展性差。尽管已有一些自动化流水线（如SWE-rebench、SetUpAgent等）试图改善可扩展性，但它们往往侧重于评估而非训练，缺乏为大规模交互式学习（如强化学习）设计的预构建环境和细粒度实例诊断元数据，并且在实践中对“语言无关”的鲁棒性存疑。

因此，本文的核心问题是：如何自动化、大规模地构建跨多种编程语言的、高质量的、可直接用于训练软件工程智能体的可执行任务环境集合。为此，论文提出了SWE-rebench V2，一个语言无关的自动化流水线，通过从海量代码仓库的拉取请求中挖掘任务，利用交互式设置智能体合成环境，并采用大语言模型评判团进行质量过滤，从而高效生成包含可执行环境、测试和丰富元数据的大规模数据集，以突破当前SWE智能体训练的数据瓶颈。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

**1. 代码库级问题解决评测基准**：以SWE-bench为代表，基于真实的GitHub issue-PR对进行执行式评估，确立了“失败到通过”测试为主要验证标准。后续工作如SWE-bench Verified、SWE-bench-Live等提升了评估置信度或时效性。多语言扩展方面，Multi-SWE-bench和SWE-PolyBench等将评估范围扩展到Python之外的语言。本文的SWE-rebench V2与这些工作一脉相承，但核心区别在于其目标不仅是构建评测基准，更侧重于为**大规模训练**（特别是强化学习）提供海量、语言无关的任务集合，其数据规模和语言覆盖度远超多数以评测为目标的基准。

**2. 自动化实例构建与环境设置**：SWE-rebench（初代）、SetUpAgent、SWE-Factory和SWE-Bench++等工作致力于自动化任务挖掘、环境搭建和测试执行流程，以降低构建成本。本文的SWE-rebench V2直接建立在此类工作之上，其创新点在于：a) 追求在单一可执行框架下实现更广泛的**语言无关性**（覆盖20种语言）；b) 不仅发布评测集，还专门为训练发布预构建环境镜像等可复现的交互式学习工件；c) 支持基于PR描述生成问题陈述，从而大幅扩展了可用于学习的任务规模。

**3. 用于智能体学习的训练环境与任务库**：如SWE-Gym和Multi-SWE-RL，它们明确将问题解决任务构建为训练环境。本文工作与这些研究目标一致，但在**规模**和**语言多样性**上进行了显著扩展，提供了远超先前工作的任务数量（数万级）和仓库覆盖。

**4. 自动化标注与实例质量评估**：例如SPICE，利用自动化方法评估实例属性（如问题清晰度）。本文集成了自动化质量评估流程，并利用人类验证数据进行校准，同时提供详细的实例级诊断元数据，以区分模型能力不足与环境缺陷（如不稳定的测试），这提升了数据集对下游训练和分析的实用性。

**5. 合成与测试驱动的数据生成**：如SWE-smith和SWE-Flow，通过合成测试失败或构建部分代码库来生成训练任务。本文方法与这类工作的根本区别在于，它**专注于采集真实世界的问题解决历史**，以保留实际开发中的噪声、模糊性和工具链多样性，同时通过丰富的元数据和诊断信息来增强其对于学习的可用性。

### Q3: 论文如何解决这个问题？

论文通过构建一个语言无关的自动化流水线来解决大规模、可执行的软件工程任务收集与验证环境构建问题。其核心方法是设计一个多阶段的流程，从海量GitHub数据中挖掘、筛选、验证并丰富任务实例，最终生成包含预构建环境的大规模数据集。

整体框架包含五个主要阶段：1) 初步数据收集：从GitHub Archive挖掘候选PR，并基于仓库语言、星数、已关闭issue数等进行过滤，以优化计算产出比；同时将PR差异拆分为解决方案补丁和测试补丁。2) 设置合成：为每个仓库部署一个交互式设置代理（基于Qwen3-Coder-480B-A35B-Instruct模型），通过闭环调试循环自动推断并生成该仓库的依赖安装和测试脚本，确保测试套件可无故障运行。此过程每个仓库仅执行一次，生成的脚本复用于该仓库的所有任务。3) 基于执行的验证：使用Docker构建可重现的执行环境。采用多阶段构建：预构建的基础镜像包含语言运行时和通用工具；随后应用测试补丁并运行完整测试套件；再应用解决方案补丁并重新运行测试套件，从而获取修复前后的配对执行轨迹，并确保每个任务至少包含一个“失败转通过”的测试作为有效学习信号。4) 基于问题清晰度的过滤：使用三个独立的LLM法官对任务描述进行评分，仅保留所有法官均认为描述足够清晰、可供实现的任务，以去除描述不明确的任务。5) 元数据丰富：使用LLM自动为每个任务标注潜在限制和特征（如测试不稳定、描述模糊等），并生成测试套件中明确调用的接口信息，支持研究者按难度或任务类型进行灵活的子集选择。

关键技术包括：**语言无关的统一工作流**：通过模板和LLM自动生成各语言的基础Dockerfile，并将语言特定组件（如基础镜像、运行器、解析器）模块化重用，从而支持扩展到新语言而无需手动工程。**交互式设置代理**：能处理异构构建系统和测试运行器，对于编译型语言（如C/C++），代理会显式插入重新编译命令，确保测试运行于修补后的源代码。**结构化日志解析**：引导生成仓库特定的测试输出解析器，将原始日志转换为标准化结果（通过、失败、错误等），优先支持结构化测试报告（如JUnit XML）以确保解析可靠性。**任务扩展机制**：除了基于issue的任务，还利用未直接关联issue的PR，通过LLM根据PR描述和补丁生成合成问题描述，从而显著扩大了训练数据规模（额外释放12万+任务）。

创新点主要体现在：1) **规模化与语言多样性**：构建了涵盖20种编程语言、3600+仓库的32000+可执行任务集合，并提供了预构建镜像确保可重现性。2) **自动化与智能化流水线**：通过LLM驱动的设置代理、过滤法官和元数据生成器，实现了从数据挖掘到环境构建的全流程高度自动化。3) **诊断性元数据**：为每个任务标注了常见混淆因素（如限制性过强的测试、描述不明确），支持受控训练和细粒度评估。4) **兼顾效率与覆盖的过滤策略**：对高资源语言采用严格过滤以降低设置成本，对长尾语言放宽阈值以保持多样性，在减少仓库处理量的同时覆盖了大部分任务。

### Q4: 论文做了哪些实验？

论文实验主要包括三部分：环境配置代理的消融研究、问题描述过滤器的消融研究，以及数据集诊断分析。

**实验设置与数据集**：环境配置实验在103个任务（来自SWE-bench等基准，覆盖10种语言）上比较了非交互式流水线与基于mini-SWE-agent的交互式代理，评估指标为pass@k（成功配置的比例）。问题过滤实验使用SWE-bench Verified数据集（1699个人工标注实例），评估不同提示、模型和集成策略对“问题描述是否明确”分类的准确性、精确率、召回率和F1分数。诊断分析实验在300个任务子集（Python、JavaScript、Go、Rust、Scala各60个）上评估了7个前沿模型（如Claude Opus-4.5、GPT-5.2等）的通过率，并分析了常见失败模式。

**对比方法与主要结果**：在环境配置中，交互式代理显著优于非交互式流水线；例如，使用Qwen3-30B的交互代理pass@10达46.1%，而非交互式仅为15.7%。增大上下文长度（如128k token）和增加尝试次数（如10次运行）可提升成功率，但为权衡成本，主流水线采用单次运行。在问题过滤中，Verified-E提示在精确率上最优（0.83），而Verified+提示F1分数最高（0.50）；集成策略中，平均分数集成能提升鲁棒性（F1达0.43）。诊断结果显示，不同模型在各类语言上表现差异明显，Claude Opus-4.5综合表现最佳（pass@1为25.2%，pass@3为32.7%），同时识别出测试耦合、隐式命名要求和外部依赖等常见干扰因素，并据此为实例添加元数据标签以支持课程学习等训练策略。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向主要体现在以下几个方面。首先，虽然提供了丰富的诊断元数据，但缺乏基于不同过滤数据子集的智能体训练消融实验，未来可量化特定任务元数据（如生成式接口）对学习过程的影响，并验证元数据在课程学习设计中的有效性。其次，当前环境设计仅支持可打包为单一Docker容器的项目，限制了需要多服务、外部数据库等复杂系统的覆盖，未来可探索支持分布式或云原生架构的环境构建方法。此外，自动化流程可能导致任务存在环境准备问题，引入奖励噪声，未来可结合更精细的验证机制（如动态测试生成或符号执行）提升任务质量。从更广阔的视角看，可进一步探索跨语言任务的知识迁移机制，利用高资源语言任务提升低资源语言的智能体性能，并研究如何将人类反馈或代码演化历史融入训练，以增强智能体对复杂软件工程上下文的理解与决策能力。

### Q6: 总结一下论文的主要内容

该论文提出了SWE-rebench V2，一个语言无关的自动化流水线，用于大规模构建可执行的软件工程（SWE）任务集合，以解决强化学习训练中大规模、多样化且可复现任务数据稀缺的问题。其核心贡献在于设计了一套端到端的自动化流程：从挖掘代码仓库的拉取请求开始，通过一个交互式设置代理合成仓库特定的安装和测试程序，并利用LLM评判器集成过滤不可靠实例，最终构建了一个包含超过32,000个与问题关联的任务（覆盖20种语言和3,600多个仓库）并附带预构建执行镜像的数据集，以及额外12万多个基于拉取请求描述生成问题陈述的任务。主要结论是，该工作为跨多种语言和仓库的大规模SWE智能体训练提供了实践基础，并通过诊断研究验证了实例质量，提供了标识常见干扰因素的元数据。其意义在于显著扩展了训练数据的规模和多样性，突破了以往基准测试对高资源语言生态的依赖。
