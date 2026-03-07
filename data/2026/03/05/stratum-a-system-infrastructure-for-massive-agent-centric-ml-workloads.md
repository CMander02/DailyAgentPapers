---
title: "stratum: A System Infrastructure for Massive Agent-Centric ML Workloads"
authors:
  - "Arnab Phani"
  - "Elias Strauss"
  - "Sebastian Schelter"
date: "2026-03-03"
arxiv_id: "2603.03589"
arxiv_url: "https://arxiv.org/abs/2603.03589"
pdf_url: "https://arxiv.org/pdf/2603.03589v2"
categories:
  - "cs.DB"
  - "cs.LG"
tags:
  - "Architecture & Frameworks"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Architecture & Frameworks"
    - "Tool Use & API Interaction"
  domain: "Data Science & Analytics"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "stratum system infrastructure (decouples pipeline execution from planning, compiles batches of pipelines into optimized execution graphs, uses Rust-based runtime)"
  primary_benchmark: "N/A"
---

# stratum: A System Infrastructure for Massive Agent-Centric ML Workloads

## 原始摘要

Recent advances in large language models (LLMs) transform how machine learning (ML) pipelines are developed and evaluated. LLMs enable a new type of workload, agentic pipeline search, in which autonomous or semi-autonomous agents generate, validate, and optimize complete ML pipelines. These agents predominantly operate over popular Python ML libraries and exhibit highly exploratory behavior. This results in thousands of executions for data profiling, pipeline generation, and iterative refinement of pipeline stages. However, the existing Python-based ML ecosystem is built around libraries such as Pandas and scikit-learn, which are designed for human-centric, interactive, sequential workflows and remain constrained by Python's interpretive execution model, library-level isolation, and limited runtime support for executing large numbers of pipelines. Meanwhile, many high-performance ML systems proposed by the systems community either target narrow workload classes or require specialized programming models, which limits their integration with the Python ML ecosystem and makes them largely ill-suited for LLM-based agents. This growing mismatch exposes a fundamental systems challenge in supporting agentic pipeline search at scale. We therefore propose stratum, a unified system infrastructure that decouples pipeline execution from planning and reasoning during agentic pipeline search. Stratum integrates seamlessly with existing Python libraries, compiles batches of pipelines into optimized execution graphs, and efficiently executes them across heterogeneous backends, including a novel Rust-based runtime. We present stratum's architectural vision along with an early prototype, discuss key design decisions, and outline open challenges and research directions. Finally, preliminary experiments show that stratum can significantly speed up large-scale agentic pipeline search up to 16.6x.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由大语言模型（LLM）驱动的自主或半自主智能体（MLE agents）进行大规模机器学习（ML）流水线搜索时，所面临的**系统性能瓶颈与基础设施缺失**的核心问题。

**研究背景**：随着LLM的发展，出现了一种新型的“智能体中心化”ML工作负载。智能体能够根据任务描述，自动生成、验证和优化由Python ML库（如Pandas、scikit-learn）编写的完整ML流水线。这个过程具有高度探索性，会产生成千上万次的数据分析、流水线生成和迭代优化执行。

**现有方法的不足**：当前支撑这一趋势的生态系统存在严重不匹配。一方面，主流的**Python ML库**（如Pandas、scikit-learn）是为人类中心化、交互式、顺序的工作流设计的，受限于Python的解释执行模型、库级别的隔离性以及对大规模并发流水线执行缺乏运行时支持，效率低下。另一方面，**系统研究社区**提出的许多高性能ML系统（如基于DSL的系统或特定任务优化系统），要么针对狭窄的工作负载类型，要么需要专门的编程模型，难以与主流的Python ML生态集成，因此不适合LLM智能体直接使用。现有的分布式框架（如Ray、Dask）侧重于任务调度而非整体优化，AutoML框架则缺乏编译和运行时支持。

**本文要解决的核心问题**：因此，在支持大规模智能体流水线搜索时，存在一个根本性的系统挑战：**高级别、灵活的Python API与对低级别、高性能执行的需求之间的巨大鸿沟**。论文旨在设计一个统一的系统基础设施，以弥合这一鸿沟，高效支持这种新兴的、大规模的、以智能体为中心的ML工作负载。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：系统优化类、数据科学加速类和智能体驱动的工作负载类。

在**系统优化类**工作中，已有研究关注机器学习系统的编译器与运行时技术、流水线并行、算子间与算子内并行、基于任务的执行以及粗/细粒度复用等。Stratum 借鉴了这些思想，但与之不同的是，它专门针对“智能体驱动的流水线搜索”这一新型工作负载，应用了算子调度、多级并行和复用等优化策略。

在**数据科学加速类**工作中，相关系统旨在通过基于规则的动态分块、并行执行或将 Pandas 操作转换为 SQL 等方式来提升数据框（DataFrame）性能。其中，mlwhatif 通过插桩 Python 代码来构建算子有向无环图（DAG），为 Stratum 的逻辑重写提供了灵感。然而，Stratum 能够直接从任意 ML 库构建惰性求值的算子 DAG，并应用包括重写和算子选择在内的高级优化，其集成度和优化范围更为广泛。

在**智能体驱动的工作负载类**中，存在专注于 Text2SQL 和优化语义算子的系统。Stratum 与这类工作的目标不同，它并非处理 SQL 生成或优化，而是专门为智能体驱动的 ML 工作负载（即自主或半自主智能体生成、验证和优化完整 ML 流水线的过程）设计系统基础设施。

综上，Stratum 与这些相关工作的核心区别在于，它旨在为新兴的、高度探索性的智能体中心化 ML 工作负载提供一个统一的、能与现有 Python ML 生态无缝集成的高效执行系统，以解决现有系统在此场景下的不匹配问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为stratum的统一系统基础设施来解决大规模智能体中心ML工作负载的执行效率问题。其核心方法是**将管道执行与智能体的规划推理过程解耦**，并针对批量生成的、高度探索性的ML管道进行深度优化。

**整体框架**：stratum的架构是一个**多层编译与执行系统**。它接收由智能体生成的批量ML管道，首先通过skrub库将其转换为**统一的有向无环图**，然后依次进行逻辑优化、算子降级、后端选择，最后在异构后端上高效执行。

**主要模块与关键技术**：
1.  **统一DAG构建与逻辑优化**：stratum以skrub作为入口，将Pandas、scikit-learn等库的任意操作封装成语义明确的算子，形成惰性执行的DAG。其创新点在于**扩展了skrub的抽象**，增加了元数据收集（算子类型、数据特征等），并在此基础上应用基于规则的**逻辑重写**（如谓词下推、公共子表达式消除）和**API感知的重写**（如优化Pandas操作顺序以减少复制），以消除冗余计算。

2.  **算子降级与选择**：系统将高级复合算子（如交叉验证、TableVectorizer）**降级**为细粒度算子，以暴露更多优化机会（如细粒度复用、并行化）。同时，stratum设计了**分层的算子体系**，将逻辑算子与物理实现解耦，支持为同一逻辑算子（如降维）提供多种后端实现（如scikit-learn SVD、近似算法、原生Rust运行时）。一个**基于成本的优化器**会依据元数据和资源估算，为算子选择在内存约束下执行时间最短的实现。

3.  **高性能Rust后端**：针对Python算子（即使基于NumPy/Cython）存在的类型转换、临时分配、GIL限制等开销，stratum创新性地**增量开发了一个Rust后端**。该后端通过PyO3提供轻量级绑定，实现零拷贝数据访问和显式内存控制，并在执行时释放GIL，从而支持**真正的内核并发**和原生数据并行。这为算子融合、稀疏性利用等高级优化奠定了基础。

4.  **并行与复用机制**：
    *   **并行执行**：系统主要依赖多线程。成本优化器会遍历DAG，在评估最坏情况内存预算后，选择最佳执行计划，并**协调算子间与算子内的并行度**，以避免因嵌套并行（如Rust后端使用Rayon）导致的资源过载。
    *   **中间结果复用**：为利用工作负载的重复性，stratum结合了**粗粒度缓存**（缓存顶层算子结果）和**细粒度复用**（在Rust内核间共享）。它通过基于算子规格和输入哈希的缓存机制实现常数时间查找，并将缓存对象序列化到磁盘（Parquet格式），支持跨迭代的持久化复用。

**创新点**：stratum的主要贡献并非发明全新的单个技术，而在于**将这些技术（DAG抽象、逻辑优化、分层算子、成本优化、原生运行时、缓存）进行系统性的、原则性的集成**，构建出一个能与现有Python ML生态无缝衔接、并能对智能体生成的批量探索性管道进行端到端编译与优化的统一基础设施。其Rust后端的引入，是突破Python执行模型瓶颈、实现实质性加速的关键创新。

### Q4: 论文做了哪些实验？

论文的实验部分主要评估了stratum早期原型及其核心组件的性能，以验证其设计原则。实验在单节点上进行，硬件配置为AMD EPYC 7443P CPU（24物理/48虚拟核心）和256GB RAM，软件环境包括Ubuntu 20.04、Python 3.11、scikit-learn 1.8和skrub 0.6.2。实验使用了一个代表性的两阶段工作负载：第一阶段探索两种预处理策略（缺失值填充与特征编码，或使用TableVectorizer进行自动清洗与编码）与四种模型（Ridge、XGBoost、LightGBM、ElasticNet）的所有组合；第二阶段基于验证精度选择最佳预处理策略和模型进行超参数调优。数据集采用Kaggle的英国住房数据集，并调整数据规模以评估可扩展性。

对比方法包括：Base（AIDE系统顺序执行流水线）、Base_par（AIDE并发触发多个流水线）以及启用所有优化的stratum。主要结果显示，stratum相比Base实现了16.6倍的加速，相比Base_par也快7.8倍。关键优化贡献包括：流水线融合、公共子表达式消除（CSE）以去重预处理、算子选择（用Polars替代Pandas、用Rust内核替代scikit-learn）、算子内与算子间并行，以及第二阶段预处理结果的复用。消融实验进一步分析了各优化的独立影响：逻辑优化（如CSE）带来最高2.2倍加速；算子选择额外提供4.5倍改进；算子间并行再贡献10%加速。这些结果验证了stratum通过整体逻辑与运行时优化能有效加速大规模智能体驱动的ML工作负载。

### Q5: 有什么可以进一步探索的点？

该论文提出的stratum系统在原型阶段已展现出潜力，但仍有多个方向值得深入探索。首先，系统目前依赖启发式策略进行算子选择和并行规划，未来需开发更精细的成本模型，例如通过采样和自适应学习来动态优化执行计划，以应对Pandas等库中隐藏中间结果带来的内存估算难题。其次，跨库边界的数据移动和UDF黑盒问题限制了优化空间，可研究零拷贝数据交换和结构化UDF接口，以提升异构管道执行的效率。此外，对深度学习工作负载的支持尚不完善，需深化与PyTorch等框架的集成，实现量化、流水线并行等高级优化。从长远看，可探索多租户云服务架构，使系统能自适应管理资源并支持跨工作负载优化；同时，开发系统感知的智能体，使其能主动利用stratum的优化能力来指导管道搜索，形成双向协同。最后，针对智能体工作负载定制推理引擎（如共享缓存机制）也是一个重要方向，能进一步降低交互延迟与成本。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）催生的新型机器学习（ML）工作负载——**智能体驱动的流水线搜索**，提出了一个名为 **stratum** 的系统基础设施。其核心问题是：现有以Python库（如Pandas、scikit-learn）为中心的ML生态系统是为人类交互式、顺序化工作流设计的，无法高效支持智能体进行大规模、探索性流水线生成与验证所导致的数千次执行，存在性能瓶颈和系统不匹配。

论文的核心贡献是设计并初步实现了stratum系统。其方法概述为：**将流水线执行与智能体的规划推理过程解耦**，作为一个统一的执行层。它无缝集成现有Python库，将批量流水线编译成优化的执行图，并通过一个新颖的基于Rust的高效运行时，在异构后端上执行。系统关键设计包括支持惰性求值的执行引擎、基于成本的算子选择与并行化、以及将异构ML库抽象到统一执行模型的优化器。

主要结论是，stratum能显著提升大规模智能体流水线搜索的效率（初步实验显示最高达16.6倍加速），同时保持与现有生态的完全兼容。其意义在于为未来以智能体为中心的ML工作负载提供了必要的系统基础，重新思考了端到端ML系统设计，以应对ML开发抽象层级提升带来的新挑战。
