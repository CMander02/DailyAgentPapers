---
title: "ABSTRAL: Automatic Design of Multi-Agent Systems Through Iterative Refinement and Topology Optimization"
authors:
  - "Weijia Song"
  - "Jiashu Yue"
  - "Zhe Pang"
date: "2026-03-24"
arxiv_id: "2603.22791"
arxiv_url: "https://arxiv.org/abs/2603.22791"
pdf_url: "https://arxiv.org/pdf/2603.22791v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "System Design"
  - "Architecture Optimization"
  - "Iterative Refinement"
  - "Topology Reasoning"
  - "Role Discovery"
  - "Knowledge Transfer"
  - "Contrastive Analysis"
  - "Natural Language Artifacts"
relevance_score: 8.0
---

# ABSTRAL: Automatic Design of Multi-Agent Systems Through Iterative Refinement and Topology Optimization

## 原始摘要

How should multi-agent systems be designed, and can that design knowledge be captured in a form that is inspectable, revisable, and transferable? We introduce ABSTRAL, a framework that treats MAS architecture as an evolving natural-language document, an artifact refined through contrastive trace analysis. Three findings emerge. First, we provide a precise measurement of the multi-agent coordination tax: under fixed turn budgets, ensembles achieve only 26% turn efficiency, with 66% of tasks exhausting the limit, yet still improve over single-agent baselines by discovering parallelizable task decompositions. Second, design knowledge encoded in documents transfers: topology reasoning and role templates learned on one domain provide a head start on new domains, with transferred seeds matching coldstart iteration 3 performance in a single iteration. Third, contrastive trace analysis discovers specialist roles absent from any initial design, a capability no prior system demonstrates. On SOPBench (134 bank tasks, deterministic oracle), ABSTRAL reaches 70% validation / 65.96% test pass rate with a GPT-4o backbone. We release the converged documents as inspectable design rationale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）设计中缺乏可解释、可复用设计知识的问题。当前基于大语言模型的多智能体系统主要依赖人工设计，而现有自动化方法通常将中间知识存储为代码、提示词或技能库，这些形式无法捕获“设计知识”——即哪些架构模式适用于哪些问题及其原因的可读性记录。研究背景是，随着多智能体系统在复杂任务中的应用增多，设计过程仍高度依赖经验，缺乏系统化的知识沉淀和迁移机制。

现有方法的不足在于：首先，它们未能以人类可读的形式封装设计决策的推理过程，导致设计知识难以审查、修改和跨领域复用；其次，多智能体协作存在显著的“协调税”（即协作开销），但此前缺乏精确量化，使得设计者难以权衡多智能体方案的优势与成本；最后，现有系统无法从执行轨迹中自动发现新的专家角色，限制了架构的适应性优化。

本文的核心问题是：能否以自然语言文档作为多智能体系统设计的优化目标，从而自动化地捕获、迭代和迁移设计知识？为此，论文提出ABSTRAL框架，将多智能体架构视为一个可演化的自然语言文档（基于SKILL标准），通过对比轨迹分析进行迭代精炼。该方法试图系统化地解决设计知识的表征、协调开销的量化以及角色自动发现三大挑战，最终实现可检查、可修订且可迁移的多智能体设计自动化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。在方法类中，技能范式经历了从“技能即代码”（如Voyager、DynaSaur，存储可执行函数但无法推理拓扑）、“技能即提示”（如ExpeL、SSO，从轨迹中提取行为提示但拓扑固定）到“技能即设计知识”（如AutoManual、\skill{}，通过环境交互构建Markdown文档）的演变。ABSTRAL属于第三范式，但专注于编码如何构建多智能体系统，而非如何在其中执行任务。同时，自动智能体设计系统（如ADAS、AFlow、MaAS、MASS、GPTSwarm、G-Designer、EvoAgent）通过演化代码、蒙特卡洛树搜索、概率超网络采样等方式优化拓扑或工作流，但知识存储形式（代码、神经参数、标量分数）不透明，无法作为可检查的设计原理。ABSTRAL则能同时优化拓扑、存储可读知识并发现新角色，与此类工作形成对比。在应用类中，新兴技能生态系统（如AutoSkill、SkillNet、EvoSkill、AgentSkillOS）使用结构化文档作为知识表示，但仅编码单个智能体的任务执行，而非组织设计；SkillOrchestra虽通过对比轨迹构建技能手册，但其技能是固定智能体池的路由描述符，不发现新角色或搜索拓扑族。ABSTRAL通过证据驱动的精炼解决了此类问题。在评测类中，交互式智能体基准SOPBench用于评估标准操作程序合规性，其基线通过率在33.58%到76.87%之间，研究表明多智能体失败中41-86%是结构性的，这与ABSTRAL的证据类别相呼应，凸显了组织设计的关键约束。总体而言，ABSTRAL在拓扑优化、可读知识存储和角色发现方面整合并超越了现有方法。

### Q3: 论文如何解决这个问题？

论文通过一个名为ABSTRAL的迭代精炼与拓扑优化框架来解决多智能体系统的自动设计问题。其核心方法是将系统架构视为一个可演化的自然语言文档（称为技能文档 $\mathcal{A}_t$），并通过对比执行轨迹分析来驱动该文档的持续改进。

整体框架是一个双层循环结构。内层循环（Layer 1）是核心设计迭代管道，包含四个阶段：1) **构建**：一个元智能体读取当前技能文档 $\mathcal{A}_t$，生成包含角色、边和路由的AgentSpec，并由图工厂实例化为可运行的LangGraph系统。2) **运行**：系统在沙盒环境中执行分层采样的任务，并通过OpenTelemetry捕获完整的、每个智能体的执行轨迹。3) **分析**：元智能体按任务类型配对失败与成功的轨迹，并将每个失败归类到五种证据类别（EC1-EC5）之一。4) **更新**：根据证据类别，对技能文档中相应的特定部分进行有针对性的编辑。

技能文档 $\mathcal{A}_t$ 是架构的关键载体，包含四个主要模块：**K（领域知识）**、**R（拓扑推理规则）**、**T（发现的角色模板）** 和 **P（构建协议）**。每个证据类别对应一个特定的更新目标：EC1（错误结论）更新K，EC2（瓶颈或错误路由）更新R，EC3（一个智能体处理不兼容子任务）和EC5（成功模式）更新T，EC4（消息/类型不匹配）更新P。

关键技术包括：1) **基于轨迹的专业化**：当EC3触发时，系统能推断出可预防失败的专用专家角色，并创建一个包含功能名称、认知立场、系统提示等的新角色模板，从而发现初始设计中不存在的角色。2) **收敛与整合**：内层循环根据多个信号（如技能文档变化、通过率平台期）终止。定期进行整合，合并冗余规则，删除引用少的规则，以控制语义漂移。3) **双标准多样性驱动的外层探索**：为防止陷入局部最优，外层循环通过向种子文档注入拓扑排斥约束，强制探索设计空间的不同区域。它要求新架构在交互图结构（图编辑距离）和角色集语义（余弦距离）上均与已有方案保持足够差异。

创新点在于将系统设计知识编码为可检查、可修改、可转移的自然语言文档，并通过对比轨迹分析实现自动化的、数据驱动的迭代精炼，特别是其自动发现专家角色和通过文档实现跨领域知识迁移的能力。

### Q4: 论文做了哪些实验？

论文在SOPBench基准上进行了实验，这是一个包含134个银行领域任务的数据集，具有确定性的oracle评估（5个布尔标准，不使用LLM作为评判者）。实验设置严格遵循已发布的协议：任务共享25个工具和约束规则，智能体使用未修改的系统提示，约束选项为“full”，每任务限制20轮/10个动作。主要使用GPT-4o作为智能体骨干模型，并使用Claude Sonnet 4作为元智能体（仅用于构建/分析/更新）。

对比方法包括已发布的SOPBench基线（FC模式）：GPT-4o-mini（33.58%）、GPT-4o（58.96%）、Claude-3.7-Sonnet（65.67%）、GPT-4.1（69.40%）、o4-mini-high（76.87%）。论文还复现了单智能体GPT-4o基线（在验证集上通过率为50%），并设置了仅内部循环（O1，分层拓扑）的消融实验。

主要结果如下：ABSTRAL完整流程在验证集（40个任务）上达到70%的通过率，在测试集（94个任务）上达到65.96%的通过率。关键数据指标包括：多智能体协调税测量显示，在固定轮次预算下，集成智能体平均只有约26%的轮次效率（每4轮产生1个工具调用），66%的任务达到20轮限制。仅内部循环（分层拓扑）在55%处收敛，表明外部循环的拓扑多样化贡献了额外的15个百分点提升。知识转移实验证明，将先前外部循环学到的领域知识（K）转移到新种子中，能使新循环在单次迭代内达到相当于冷启动第3次迭代的性能。此外，通过对比轨迹分析（EC3）发现了初始设计中不存在的专家角色（如验证者、执行者、预言家）。搜索总成本约为154K个令牌（约5美元）。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其收敛机制和任务适用性。研究发现，所有外部循环均因达到最大迭代次数而终止，而非基于收敛信号，这表明当前的收敛阈值可能过于保守，尤其是在小批量验证场景下，成功率波动较大。此外，多智能体协调的收益高度依赖于任务结构：对于可并行化的任务（如展开式执行）能有效提升效率，但对于需要长顺序链的任务（如多步骤信贷申请），路由开销会导致回合数不足而失败。

未来研究方向可围绕以下几点展开：首先，可以设计更自适应的收敛准则，例如引入统计显著性检验或动态调整阈值，以更可靠地判断优化过程是否完成。其次，需要探索如何将ABSTRAL框架扩展到更复杂的顺序性任务上，可能通过引入分层规划或动态拓扑调整来减少路由开销。再者，论文展示了设计文档的可迁移性，未来可以进一步研究跨领域知识的自动提取与组合机制，例如利用元学习来加速在新领域中的适应过程。最后，可以探索将自然语言文档与其他形式化表示（如图神经网络）相结合，以在保持可解释性的同时增强对复杂协作模式的建模能力。

### Q6: 总结一下论文的主要内容

本论文提出了ABSTRAL框架，将多智能体系统（MAS）的架构设计视为一个可通过迭代优化演化的自然语言文档。核心问题是探索如何以可检查、可修改、可迁移的形式捕获MAS的设计知识。方法上，ABSTRAL通过对比轨迹分析来迭代精炼描述系统架构的文档，该文档定义了知识、角色、拓扑和流程。主要结论有三点：首先，论文首次精确量化了“多智能体协调税”，发现在固定交互轮次预算下，多智能体系统的轮次效率仅为26%，但通过发现可并行化的任务分解，其性能仍能超越单智能体基线。其次，编码在文档中的设计知识（如拓扑推理和角色模板）具有可迁移性，迁移后的初始设计在新领域仅需一次迭代即可达到冷启动三次迭代的性能。最后，对比轨迹分析能够自动发现初始设计中不存在的专家角色，这是以往系统不具备的能力。在SOPBench基准测试中，该方法达到了约66%的测试通过率。论文的核心贡献在于证明了自然语言文档可作为MAS设计的可行优化目标，其产生的设计知识兼具可迁移性和可检查性，并揭示了多智能体协调何时物有所值。
