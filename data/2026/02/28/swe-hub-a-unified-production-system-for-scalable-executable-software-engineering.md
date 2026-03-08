---
title: "SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks"
authors:
  - "Yucheng Zeng"
  - "Shupeng Li"
  - "Daxiang Dong"
  - "Ruijie Xu"
  - "Zimo Chen"
date: "2026-02-28"
arxiv_id: "2603.00575"
arxiv_url: "https://arxiv.org/abs/2603.00575"
pdf_url: "https://arxiv.org/pdf/2603.00575v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Code & Software Engineering"
  - "Architecture & Frameworks"
relevance_score: 9.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "SWE-Hub (Env Agent, SWE-Scale, Bug Agent, SWE-Architect)"
  primary_benchmark: "N/A"
---

# SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks

## 原始摘要

Progress in software-engineering agents is increasingly constrained by the scarcity of executable, scalable, and realistic data for training and evaluation. This scarcity stems from three fundamental challenges in existing pipelines: environments are brittle and difficult to reproduce across languages; synthesizing realistic, system-level bugs at scale is computationally expensive; and existing data predominantly consists of short-horizon repairs, failing to capture long-horizon competencies like architectural consistency. We introduce \textbf{SWE-Hub}, an end-to-end system that operationalizes the data factory abstraction by unifying environment automation, scalable synthesis, and diverse task generation into a coherent production stack. At its foundation, the \textbf{Env Agent} establishes a shared execution substrate by automatically converting raw repository snapshots into reproducible, multi-language container environments with standardized interfaces. Built upon this substrate, \textbf{SWE-Scale} engine addresses the need for high-throughput generation, combining cross-language code analysis with cluster-scale validation to synthesize massive volumes of localized bug-fix instances. \textbf{Bug Agent} generates high-fidelity repair tasks by synthesizing system-level regressions involving cross-module dependencies, paired with user-like issue reports that describe observable symptoms rather than root causes. Finally, \textbf{SWE-Architect} expands the task scope from repair to creation by translating natural-language requirements into repository-scale build-a-repo tasks. By integrating these components, SWE-Hub establishes a unified production pipeline capable of continuously delivering executable tasks across the entire software engineering lifecycle.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决软件工程智能体（AI Agent）领域因缺乏高质量、可执行、可扩展的训练与评估数据而面临的瓶颈问题。研究背景是，尽管大语言模型在代码生成和错误修复方面能力日益增强，但其在仓库级软件工程任务上的进展受到严重制约。这种制约源于软件工程正确性的“执行基础”特性——判断一个修改是否正确，依赖于构建系统、依赖关系、运行时行为和测试框架等复杂因素的交互，而非简单的文本差异。

现有方法存在三个主要不足：首先，现有环境脆弱且难以跨语言复现，真实项目往往需要专家手动调试环境，这阻碍了数据的规模化生成。其次，现有数据合成方法（如错误注入）计算成本高昂且规模有限，生成的错误大多局限于单个函数或文件，无法反映涉及跨模块契约、配置交互或症状与根因分离的系统级真实故障。最后，当前主流基准测试主要关注“给定失败信号生成补丁”的短视距修复任务，严重缺乏对长期规划、依赖管理、多文件一致性和仓库级架构设计等长视距能力的评估。

因此，本文要解决的核心问题是：如何构建一个统一的生产系统（即“数据工厂”），以自动化、可扩展的方式，持续地将原始代码仓库转化为多样化、可执行且覆盖软件工程全生命周期的任务数据。该系统需要同时满足三个核心要求：环境可靠性（为异构仓库自动提供确定性的、可执行的环境）、可扩展的数据合成（结合自动化合成算法与集群级计算进行并行验证，实现大规模数据生成）以及任务多样性（生成从局部修复到仓库构建的广泛任务类型）。论文提出的SWE-Hub系统正是为了具体实现这一“数据工厂”抽象，通过集成环境代理、规模化合成引擎、高保真错误代理和长视距架构任务生成器，形成一个连贯的生产栈，从而突破当前数据稀缺的约束。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：可执行基准评测、可扩展任务生成和长视野能力评估。

在**可执行基准评测**方面，SWE-bench 开创了基于真实 GitHub 仓库和 Docker 环境的问题解决评测，后续的 SWE-bench Verified、SWE-bench++ 以及 Multi-Docker-Eval 等工作进一步提升了评测的鲁棒性和环境构建能力。然而，这些工作主要将容器化视为评测工具或特定基准任务，环境设置与特定基准规范紧密耦合，未能抽象为可复用的资产。SWE-Hub 的改进在于将容器化评测推广为一个**共享的执行基底**，将仓库转换为版本化、标准化的容器镜像，使环境逻辑与任务逻辑解耦，从而支持多种下游任务。

在**可扩展任务生成**方面，SWE-Smith、R2E-Gym、SWE-Gym 等工作通过操作真实代码库并执行验证来大规模合成可验证的 bug 修复实例。SWE-Synth、SWE-Mirror、Self-Play SWE-RL 等方法则探索了不同的数据扩展途径。这些方法大多专注于单一任务格式（如短视野修复），且环境设置、仓库结构等假设内嵌其中，限制了跨生态系统的可移植性和任务多样性。SWE-Hub 的改进在于提供了一个**统一的工厂架构**，通过标准化的执行基底解耦环境供应与任务逻辑，并组织模块化的任务产品线，支持高吞吐量合成和多样化任务生成。

在**长视野能力评估**方面，SWE-EVO、SWE-Bench Pro 等基准开始评估规划、依赖管理等长视野能力，NL2Repo-Bench 则要求从自然语言需求构建完整仓库。但这些基准通常是独立的数据集或任务，缺乏一个能持续生成和验证实例的统一生产流水线。SWE-Hub 的改进在于将**长视野仓库构建**作为一等公民的产品线，集成到与修复任务相同的执行基底上，确保了跨任务视野的一致验证和可扩展生成。

总之，SWE-Hub 的核心贡献是将上述分散的能力整合为一个统一的生产系统，通过共享的执行基底和多样化的任务产品线，实现了从短视野修复到系统级回归，再到长视野构建的全软件工程生命周期任务生成。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SWE-Hub的端到端数据生产系统来解决可执行、可扩展软件工程任务数据稀缺的问题。其核心方法是将整个流程抽象为一个“数据工厂”，通过统一的执行基底和多个并行的任务产品线，实现大规模、多样化的任务生成与验证。

**整体框架与架构设计**：
SWE-Hub采用分层架构。底层是**执行基底层**，由**Env Agent**模块构成。它负责将原始代码仓库快照自动转换为可复现的、多语言的容器化环境，并标准化验证入口点（如测试命令和结果收集器）。这确保了每个任务都绑定在一个不可变的容器镜像和统一的验证接口上，实现了“开箱即用”的可执行性（目标G1）。在此基底之上，构建了三条独立的**任务产品线**，分别针对不同复杂度和真实性的任务进行生成。

**主要模块/组件与关键技术**：
1.  **Env Agent（环境代理）**：作为系统基石，它自动分析仓库，识别工具链和依赖，构建版本化的容器镜像，并建立标准化的验证入口点。其关键创新在于实现了“环境就绪”状态——不要求测试必须通过，但要求验证过程能确定性地执行并产出可解析的结果，为下游合成提供了稳定边界。
2.  **SWE-Scale引擎（产品线A）**：专注于**大规模、短视界的修复任务合成**。它基于共享的代码分析骨干（如tree-sitter），进行跨语言代码分析，定位代码变换点，并通过程序化突变或LLM辅助重写来注入候选错误补丁。其核心创新在于通过集群规模的验证（执行测试）来筛选任务，只接受那些能产生明确执行信号（如从通过到失败）的实例，从而确保生成的任务具有可验证的故障特征，并实现了验证吞吐量的线性扩展（目标G3）。
3.  **Bug Agent（产品线B）**：致力于生成**高保真、系统级的回归错误和问题报告**。其创新点在于合成涉及跨模块、跨文件依赖的非局部错误（如组件间的契约违反），并配套生成类似真实用户的Issue报告。报告刻意描述可观察的症状和复现证据，同时避免透露根本原因提示，有效缓解了答案泄露问题，提升了任务的真实性和评估难度（目标G4）。
4.  **SWE-Architect（产品线C）**：将任务范围从修复扩展到**长视界的仓库构建任务**。它从干净的仓库版本出发，根据结构化自然语言需求，生成要求智能体实现完整仓库功能（如模块、API）的任务。评估通过相同的执行基底和隐藏测试进行，从而在统一的验证接口下覆盖了不同复杂度的任务（目标G5）。

**创新点与统一保障**：
系统的核心创新在于其**模块化、可扩展的“工厂”抽象**。它将环境自动化、可扩展合成和多样化任务生成统一到一个连贯的生产堆栈中。所有产品线共享执行基底、统一的任务模式、基于Kubernetes的集群级编排与隔离，以及标准化的日志和工件保留机制。这种设计使得添加新的任务家族（产品线）时，无需重新设计环境供给或验证逻辑，显著降低了支持新语言和生态系统的边际成本（目标G2）。最终，每个任务都被记录为一个自包含的、以执行为中心的任务记录，确保了从生成到验证的全流程可追溯性和可复现性。

### Q4: 论文做了哪些实验？

论文的实验围绕SWE-Hub系统的核心组件SWE-Scale展开，旨在验证其高效生成可执行软件工程任务数据的能力。实验设置上，SWE-Scale采用“沙箱-候选”隔离的执行模型，每个候选补丁都在一个全新的、短暂的容器实例中运行，并通过维护一个预热的容器池来优化启动开销。验证过程被设计为分布式系统工作负载，候选补丁作为Kubernetes作业分发，在具有明确资源限制的独立Pod中执行，以实现高并发和可复现性。

数据集/基准测试方面，实验基于从原始仓库快照自动转换而来的、可复现的多语言容器环境。系统通过统一的tree-sitter解析骨干进行多语言代码分析，以合成大规模的、局部化的缺陷修复实例。关键的数据有效性标准是：对于一个注入的缺陷补丁 \(P_{bug}\)，必须至少有一个先前通过的测试变为失败（即非空的“通过到失败”集合 \(T_{P2F}\)），同时记录“通过到通过”集合 \(T_{P2P}\) 用于回归分析和稳定性检查。

对比方法主要针对先前存在共享可变状态瓶颈的合成工作流程。SWE-Scale通过强制三个系统级不变量（无状态沙箱、集群规模验证、多语言合成）来消除此瓶颈。主要结果表明，该系统设计能够实现大规模并行验证，支持跨语言缺陷注入而无需重写核心引擎，并生成包含丰富执行信号（测试结果、日志、运行时指标等）的鲁棒任务工件，为下游训练和评估提供了超越单一二元标签的全面数据。

### Q5: 有什么可以进一步探索的点？

本文提出的SWE-Hub系统在构建可扩展、可执行的软件工程任务生产流水线方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，系统虽然支持多语言，但其对不同编程语言生态（如包管理、构建工具、框架特性）的深度适配和异常处理能力可能仍有不足，未来可研究更智能的环境自适应技术，以降低容器环境的维护成本并提升泛化性。其次，在任务生成方面，尽管能合成系统级缺陷和跨模块依赖问题，但生成的缺陷类型和任务场景可能仍局限于预设模式，缺乏对真实世界中复杂、模糊或涉及非代码因素（如文档、配置、API变更）的任务的覆盖。未来可引入更开放的问题生成机制，结合大语言模型的理解能力，模拟更贴近人类开发者的不完美需求描述和交互过程。此外，评估维度目前侧重任务可执行性和规模，但对智能体在长期任务中的决策效率、代码架构合理性、与现有代码库的协同一致性等深层次能力的评估体系尚不完善。未来可设计更全面的评估指标，引入人类专家评分或基于软件质量模型的自动化度量。最后，该系统作为数据工厂，其产出的数据质量与多样性直接影响下游智能体的训练效果，如何确保生成数据的分布与真实开源项目的演化规律相匹配，避免过拟合或偏差，也是一个关键的研究方向。可以探索将真实开发者活动数据与合成数据相结合的方法，以提升数据的真实性和训练效果。

### Q6: 总结一下论文的主要内容

论文针对软件工程智能体训练与评估中可执行、可扩展、真实数据稀缺的核心瓶颈，提出了SWE-Hub这一统一生产系统。其核心贡献是将“数据工厂”抽象具体化，通过一个端到端的生产栈，系统性地解决了环境可复现性、大规模数据合成和任务多样性三大挑战。

具体方法上，系统以Env Agent为基础，将原始代码仓库快照自动转换为具有标准化接口、可复现的多语言容器环境，建立了统一的执行基底。在此基础上，SWE-Scale引擎通过跨语言代码分析和集群级验证，实现了海量局部缺陷修复实例的高通量合成；Bug Agent通过合成涉及跨模块依赖的系统级回归缺陷，并生成描述可观察症状（而非根本原因）的类用户问题报告，创造了高保真的修复任务；SWE-Architect则将任务范围从修复扩展到创建，通过将自然语言需求转化为仓库级的“构建仓库”任务，生成了面向长期视野能力的训练数据。

主要结论是，SWE-Hub整合了先前碎片化的环境自动化、可扩展合成和任务设计工作，形成了一个连贯的生产流水线。它并非发布静态数据集，而是提供了一个能够持续生成可执行任务、随计算资源扩展、并能适应新语言和任务类型的生产系统，为软件工程智能体的规模化发展奠定了数据基础设施。
