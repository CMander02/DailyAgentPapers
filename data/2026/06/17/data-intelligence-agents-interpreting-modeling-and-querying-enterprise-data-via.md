---
title: "Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents"
authors:
  - "Anoushka Vyas"
  - "Aarushi Dhanuka"
  - "Sina Khoshfetrat Pakazad"
  - "Henrik Ohlsson"
date: "2026-06-17"
arxiv_id: "2606.19319"
arxiv_url: "https://arxiv.org/abs/2606.19319"
pdf_url: "https://arxiv.org/pdf/2606.19319v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.DB"
tags:
  - "多智能体系统"
  - "自主编码智能体"
  - "数据智能体"
  - "SQL生成"
  - "企业数据集成"
  - "共享记忆"
  - "Agent架构"
  - "工作流自动化"
relevance_score: 9.5
---

# Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents

## 原始摘要

Production data integration is bottlenecked by repeated, lossy handoffs between data owners, engineers, and analysts who must collaboratively discover, structure, and query enterprise data. We present Data Intelligence Agents (DIA), a system of three agents (Data Interpreter, Schema Creator, and Query Generator) that compresses this workflow by treating autonomous coding agents (ACAs) as a first-class abstraction: rather than emitting text, the agents generate, execute, validate, and repair concrete artifacts, draw on a shared memory for experience reuse, and surface each for review by domain experts. DIA is deployed in production for enterprise customers. We study the Query Generator in depth and evaluate it in fully autonomous mode across seven SQL benchmarks spanning four task categories and four dialects. It matches or surpasses the best published results on all seven, demonstrating that an architecture grounded in execution, built on ACAs and a shared memory, generalizes across the data intelligence workload with adaptation confined to natural-language instructions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

企业数据工作面临的核心瓶颈并非数据缺失，而是原始数据在被发现、理解、结构化和查询的过程中，存在数据所有者、工程师和分析师之间反复且丢失信息的交接。现有方法仅处理这一流程的碎片：文本到SQL的流水线系统依赖手工调整的模块，任务变化时表现脆弱；基于强化学习的专家模型在单一基准上准确率高，但锁定于特定方言且重新训练成本高昂；智能体探索器无记忆，每次查询从头开始；具备持久记忆的SQL智能体虽能复用经验，但未覆盖上游的数据理解与模式构建阶段。这些系统均输出文本而非可执行、可审查的产物，且未解决决定SQL能否正确运行的模式构建问题。为此，本文提出Data Intelligence Agents (DIA)系统，通过三个自主编程智能体（数据解释器、模式创建器、查询生成器）压缩工作流，核心创新在于将自主编程智能体作为第一类抽象，使其生成、执行、验证并修复具体产物，通过共享记忆复用经验，并由领域专家审查。该系统旨在将领域专家保留在控制环中，同时消除传递中的信息丢失与延迟，实现企业数据的端到端自动化集成与查询。

### Q2: 有哪些相关研究？

**方法类**：本文与Text-to-SQL系统密切相关。现有工作如MAC-SQL、CHESS、OpenSearch-SQL等主要针对单次查询生成，采用多智能体协作或流水线方法提升准确率，但任务设定单一；AgentNLQ虽是多智能体通用NL-to-SQL系统，仍仅覆盖一个设定。区别在于DIA的Query Generator能跨四个任务类别、四种方言统一处理，无需为不同场景定制专门系统。

**应用类**：在数据理解与模式生成方面，TableGPT2、Text2Schema、DeepPrep等独立工具分别用于表分析、模式构建和数据准备，但均为孤立组件。DIA将其整合为Data Interpreter和Schema Creator两个智能体，与Query Generator形成完整流水线，通过执行验证生成可复用的具体产物。

**评测类**：DAComp等基准测试评估了数据智能生命周期中的工程与分析代理，但针对独立工具。DIA则作为统一系统在七个SQL基准上达到或超越最佳结果，展现跨任务泛化能力。此外，DIA借鉴了OpenHands-Versa、CodeAct等通用编码代理范式，以及ARIA、Voyager等经验积累机制，但创新点在于三个智能体共享记忆体，实现系统级经验复用。

### Q3: 论文如何解决这个问题？

DIA 通过构建一个基于自主编码代理（ACA）的三代理系统，将生产数据集成中的重复性人工交接压缩为自动化、可执行的工作流。其核心抽象是ACA，它不再是输出文本，而是在沙箱环境中生成、执行、验证和修复代码，确保每个输出都是可执行且可执行验证的工件。

系统架构由三个通过共享工作区W和记忆库M协作的代理组成。Data Interpreter首先对异构原始数据D（CSV、JSON等）执行分析代码，生成结构化解释P，包括推断的schema、列分布、键关系和质量问题。Schema Creator利用P和D，遵循“先加载后规范化”的原则，生成并验证关系数据库(Σ, β)，包括表、键约束和完整性约束，并通过行计数、列覆盖、键有效性和加载完整性四轴验证确保可靠性。Query Generator则针对自然语言问题q，通过四个阶段生成SQL：声明预期结果形状κ（列、粒度、排序、过滤）、通过轻量级探测查询探索schema、生成并执行候选查询y，以及通过自验证机制V(R, κ)对照形状检查结果，不满足时迭代修正。

关键技术包括：基于工件的记忆M，分为三级（检索示例、会话经验、跨会话规则），通过拉取方式引用并在执行前验证条件。代理自主写入记忆，更新M ← w(M, a, o)，规则仅在证据确切时才被采纳。整体训练无关，仅通过自然语言指令适应不同任务。这种架构在七个SQL基准测试中达到或超越最佳结果，展示了基于执行的泛化能力。

### Q4: 论文做了哪些实验？

论文对Query Generator在七个公开SQL基准测试上进行了全面评估，涵盖BIRD-Dev、BIRD-Critic、LiveSQLBench、BIRD-Interact，以及Spider2系列（Spider2-Lite、Spider2-Snow、Spider2-DBT）。这些基准共包含4,187个实例，跨越四个任务类别（查询生成、调试、对话交互、dbt项目完成）和四种SQL方言（SQLite、PostgreSQL、Snowflake、DuckDB）。实验采用统一系统配置：以OpenHands为框架、Claude Sonnet 4.5为骨干语言模型（无微调），o3作为BIRD-Interact中的用户模拟器。所有运行均完全自主，无人工干预，各基准的定制仅通过自然语言种子文件和提示词模板实现。

主要对比方法为各基准上已有最佳公开发表结果（如MARS-SQL、CHASE-SQL、ReFoRCE+o3等）。官方主要指标包括执行准确率（多数基准）、任务成功率（BIRD-Interact）和数据库匹配准确率（Spider2-DBT）。结果显示，DIA在所有七个基准上均达到或超越了最佳公布结果：BIRD-Dev得分77.7%（vs. MARS-SQL 77.8%）、BIRD-Critic 64.2%（vs. 48.8%）、LiveSQLBench 50.7%（vs. 38.0%）、BIRD-Interact 55.7%（vs. 22.7%）、Spider2-Lite 71.3%（vs. 55.2%）、Spider2-Snow 69.5%（vs. 63.8%）、Spider2-DBT 37.5%（vs. 35.3%），尤其是在先前系统表现最差的对话交互（+33.0点）和调试（+15.4点）任务上提升显著。

### Q5: 有什么可以进一步探索的点？

DIA通过“生成-执行-验证”的迭代循环换取可靠性，但每查询平均耗时数分钟，在交互式或高吞吐场景下成本过高。未来可探索缓存机制、并行执行独立任务，以及将常规模式蒸馏为轻量组件以降低延迟。验证环节目前仅执行语法检查，缺乏语义理解，当agent误解问题意图时，验证环节会继承同一错误而通过错误答案。改进方向是将问题本身的语义纳入验证，而非仅依赖执行结果的形状匹配。此外，论文仅深入评估了Query Generator一个agent，且使用单一LLM与模拟用户，未来需扩展至Data Interpreter和Schema Creator的基准测试，测试不同LLM的敏感性，并开展真实用户研究。记忆系统目前以文件形式组织经验，若采用图结构链接工件与规则，可更高效地挖掘积累经验，提升系统泛化能力。

### Q6: 总结一下论文的主要内容

Data Intelligence Agents (DIA) 系统旨在解决企业数据集成中数据拥有者、工程师和分析师之间重复、有损的手动交接问题。该系统将自主编码代理（ACA）作为核心抽象，通过三个代理（数据解释器、模式创建器和查询生成器）压缩工作流程：代理生成、执行、验证和修复具体代码工件，而非文本；利用共享内存实现经验重用；并展示给领域专家审查。DIA已在企业生产环境中部署。对查询生成器的深入评估显示，在涵盖四个任务类别和四种SQL方言的七个基准测试中，其全自主模式匹配或超越了所有最佳已发表结果。核心贡献在于证明了基于执行的、构建于ACA和共享内存之上的架构能够泛化处理整个数据智能工作负载，仅需通过自然语言指令进行适配，无需针对特定任务进行微调。这表明一个执行驱动的代理架构可以取代一系列专业化系统，具有重要的实践意义。
