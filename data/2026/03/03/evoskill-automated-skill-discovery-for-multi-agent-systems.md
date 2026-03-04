---
title: "EvoSkill: Automated Skill Discovery for Multi-Agent Systems"
authors:
  - "Salaheddin Alzubi"
  - "Noah Provenzano"
  - "Jaydon Bingham"
  - "Weiyuan Chen"
  - "Tu Vu"
date: "2026-03-03"
arxiv_id: "2603.02766"
arxiv_url: "https://arxiv.org/abs/2603.02766"
pdf_url: "https://arxiv.org/pdf/2603.02766v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "技能发现"
  - "自动化演化"
  - "Agent技能"
  - "自我演化"
  - "Agent架构"
  - "代码智能体"
relevance_score: 9.5
---

# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

## 原始摘要

Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through \textit{agent skills}: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts \& code) that are tightly coupled to specific models and tasks. We introduce \textbf{EvoSkill}, a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen. We evaluate EvoSkill on two benchmarks: OfficeQA, a grounded reasoning benchmark over U.S.\ Treasury data, where it improves exact-match accuracy by \textbf{7.3\%} (60.6\% $\to$ 67.9\%); and SealQA, a search-augmented QA benchmark with noisy retrieval, where it yields a \textbf{12.1\%} gain (26.6\% $\to$ 38.7\%). We also investigate the zero-shot transfer capabilties of skills evolved on one task to the other; in particular: skills evolved from SealQA transfers zero-shot to BrowseComp, improving accuracy by \textbf{5.3\%} without modification demonstrating that skill-level optimization produces transferable capabilities beyond the training task.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统中领域专业知识自动化获取与复用的核心难题。研究背景是，当前基于代码的智能体（如Claude Code）作为通用问题求解器日益普及，其通过代码作为灵活中介来调用复杂抽象和工具，但这种通用性本身并不能赋予智能体完成特定领域任务所需的深层专业知识。现有方法主要依赖人工手动设计“智能体技能”（即包含工作流、指令和代码的可复用组件），这一过程既需要大量领域知识，也难以规模化。虽然已有进化方法（如AlphaEvolve）尝试通过迭代搜索优化智能体的底层构件（如提示词或代码），但这些优化产物通常与特定模型和任务强耦合，缺乏可复用性和跨任务迁移能力。

因此，本文的核心问题是：如何自动化地发现和精炼出可复用、可迁移的智能体技能，从而在无需人工大量介入且不更新底层模型的情况下，系统性地提升智能体在专门任务上的性能。为此，论文提出了EvoSkill框架，其核心创新在于将优化层级从低层、易变的“构件”提升到高层的“技能”抽象。该框架通过迭代分析执行失败案例，自动提出新技能或编辑现有技能，并将其物化为结构化的技能文件夹。通过帕累托前沿进行选择，仅保留那些能在验证集上提升性能的技能，从而实现技能的自动积累与进化，最终增强智能体的领域能力并验证其跨任务零样本迁移的有效性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为技能框架、基于反馈的迭代优化、进化算法以及迁移学习等类别。

在**技能框架**方面，Voyager 为LLM驱动的智能体构建了可执行的技能库，通过环境反馈进行自动课程学习和迭代提示。近期提出的 Agent Skills 规范则将技能定义为包含元数据、指令和辅助脚本的便携式文件目录格式。本文的EvoSkill框架旨在自动发现和精炼技能，其产出物完全遵循此结构化格式，从而弥补了当前技能主要依赖人工编写的不足。

在**基于反馈的迭代优化**方面，Self-Refine 展示了LLM通过生成-批评-精炼循环进行自我改进，但仅限于单次输出。Feedback Descent 将其形式化为一个通用优化框架，利用丰富的文本反馈驱动持续改进。EvoSkill直接建立在此范式之上，但将其应用于技能发现问题，而非一般的工件优化。

在**进化算法**方面，AlphaEvolve 和 GEPA 等工作利用LLM驱动的突变进行进化搜索，分别优化整个代码库或提示。然而，这些方法优化的都是与特定任务和模型紧密耦合的低层工件（如代码或提示）。EvoSkill的关键区别在于其抽象层次更高：它进化的是**技能**——即结构化、可复用的能力模块，这使得技能具有可解释性、可组合性，并能跨任务迁移。

在**迁移学习**方面，已有研究探索了神经网络微调或提示迁移，但效果不一。Voyager 在具身智能环境中展示了代码技能库的跨环境迁移能力。EvoSkill从不同角度探讨了迁移问题：由于技能被构建为具有明确触发条件和过程指令的自包含文件夹，它们与训练任务和底层模型均实现了解耦。本文实验证实了这种技能层优化的零样本迁移潜力。

### Q3: 论文如何解决这个问题？

论文通过一个名为EvoSkill的自进化框架来解决自动化技能发现问题。其核心方法是采用迭代式的“文本反馈下降”过程，通过分析执行失败案例来发现和精炼智能体技能，同时保持底层模型参数冻结。

整体框架是一个由三个智能体协作的循环系统：**执行智能体**负责在现有技能配置下执行任务并产生输出轨迹；**提议智能体**分析执行失败案例（包括输出轨迹、预测答案和真实答案），诊断根本原因，并据此提出高层次的新技能描述或现有技能修改建议，该智能体还维护一个反馈历史日志以防止冗余提议并实现渐进式改进；**技能构建智能体**将提议转化为具体的、结构化的技能文件夹，包含触发元数据、程序指令和可选的辅助代码。

关键技术包括：1）**帕累托前沿管理**：算法维护一个固定容量的最优程序集合（前沿），通过轮询方式从中选择父程序进行演化，新候选程序只有在验证集性能超过前沿中最弱成员时才能加入，确保演化方向始终朝向性能提升。2）**基于分类的迭代采样**：训练数据先通过LLM分类为不同类别，演化过程中按类别进行无放回采样，确保全面探索不同问题类型。3）**技能表示与隔离**：每个技能被实现为独立的文件夹，包含文档和代码；每个智能体程序表示为代码仓库中的一个分支，仅技能文件夹和元数据不同，确保性能差异完全归因于技能演化。

主要创新点在于：将技能作为高层次、可重用、结构化的工件进行演化，而非优化低层提示或代码；通过文本反馈驱动的闭环系统实现完全自动化技能发现；技能设计具有任务间零样本迁移能力，如SealQA上演化的技能能直接提升BrowseComp任务性能，证明了其产生的能力超越原始训练任务。

### Q4: 论文做了哪些实验？

论文在OfficeQA和SealQA两个基准上进行了实验，以评估EvoSkill框架的性能、技能质量影响因素及零样本迁移能力。实验设置方面，所有实验均使用Claude Code with Opus 4.5作为底层模型，并将基准数据划分为训练集（用于演化中的失败检测）、验证集（约7%，用于前沿选择）和保留测试集。在OfficeQA上，测试了5%、10%和15%三种训练集规模，各演化1.5个周期，并评估了技能合并配置（合并独立运行中的独特技能）。在SealQA上，使用10%的训练分割进行类似实验。

数据集与基准测试包括：1) OfficeQA，一个基于美国财政部公报（约89,000页）的接地推理基准，包含246个问题，需跨文档定位、合成信息并进行定量推理；2) SealQA，一个搜索增强QA基准，评估在对抗性检索条件下浏览开放网络的能力；3) BrowseComp，用于测试技能零样本迁移的浏览代理基准。

对比方法主要为基线模型（未使用EvoSkill的原始代理）。主要结果如下：在OfficeQA上，EvoSkill将精确匹配准确率从基线60.6%提升至67.9%（技能合并配置），绝对增益7.3%；不同训练分割（5%、10%、15%）下，精确匹配准确率分别达到63.4%、65.8%和64.5%。在SealQA上，准确率从基线26.6%提升至38.7%，绝对增益12.1%。关键数据指标包括：OfficeQA上不同容忍度阈值（0.00%、0.10%、1.00%、5.00%、10.00%）下的准确率提升；技能零样本迁移实验中，将SealQA演化出的搜索持久性协议技能应用于BrowseComp，准确率从43.5%提升至48.8%，绝对增益5.3%。这些结果表明EvoSkill能有效发现可迁移的技能，提升多代理系统在专业任务上的性能。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估范围相对有限，仅聚焦于两个特定基准测试（OfficeQA和SealQA），尚未验证技能在更广泛、更复杂领域（如多模态或动态环境）的泛化能力。此外，技能发现过程依赖于固定的底层模型，未探索模型更新或不同模型架构对技能演化的影响，且技能库的构建与共享机制仍处于初步设想阶段。

未来研究方向可围绕以下几点展开：首先，扩展评估至多样化领域（如科学计算、创意设计），以系统分析技能的可迁移性，区分领域通用技能与专用技能的形成规律。其次，探索多模态技能协同，使技能能跨视觉、代码和文本模态进行协调与组合，以适应更复杂的现实任务。再者，构建可交互、可检索的共享技能库，并研究技能的组合优化方法，提升智能体的模块化能力。最后，可引入元学习或课程学习策略，让技能发现过程能自适应环境变化或模型升级，从而形成更鲁棒、更高效的自动化技能演化生态系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了EvoSkill框架，旨在解决多智能体系统中领域专业知识不足的问题。核心问题是当前智能体技能多为人工设计，或通过进化方法优化与特定模型和任务紧密耦合的低层组件，缺乏可重用性和泛化能力。

EvoSkill的方法是通过迭代式失败分析自动发现和精炼智能体技能。其核心流程是：分析执行失败案例，提出新技能或对现有技能进行编辑，并将这些技能物化为结构化的、可重用的技能文件夹。该方法采用帕累托前沿进行选择，仅保留那些在模型参数固定的情况下能提升预留验证集性能的技能，从而确保技能的效用。

主要结论是，EvoSkill在两个基准测试中显著提升了性能：在基于美国财政部数据的OfficeQA基准上，准确率提升了7.3%；在检索噪声较大的SealQA基准上，准确率提升了12.1%。此外，研究还发现，在一个任务上进化出的技能能够零样本迁移到其他任务（如从SealQA迁移到BrowseComp，带来5.3%的准确率提升），这证明了技能级优化能够产生超越训练任务的可迁移能力。该工作的意义在于为构建具备自适应和可复用专业能力的多智能体系统提供了一种自动化途径。
