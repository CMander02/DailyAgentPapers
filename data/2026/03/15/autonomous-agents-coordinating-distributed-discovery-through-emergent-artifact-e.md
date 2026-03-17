---
title: "Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange"
authors:
  - "Fiona Y. Wang"
  - "Lee Marom"
  - "Subhadeep Pal"
  - "Rachel K. Luu"
  - "Wei Lu"
  - "Jaime A. Berkovich"
  - "Markus J. Buehler"
date: "2026-03-15"
arxiv_id: "2603.14312"
arxiv_url: "https://arxiv.org/abs/2603.14312"
pdf_url: "https://arxiv.org/pdf/2603.14312v1"
categories:
  - "cs.AI"
  - "cond-mat.dis-nn"
  - "cs.LG"
  - "cs.MA"
  - "q-bio.BM"
tags:
  - "Multi-Agent Systems"
  - "Tool Use"
  - "Autonomous Scientific Discovery"
  - "Decentralized Coordination"
  - "Artifact Management"
  - "Computational Lineage"
  - "Emergent Behavior"
  - "Agent Memory"
relevance_score: 8.0
---

# Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange

## 原始摘要

We present ScienceClaw + Infinite, a framework for autonomous scientific investigation in which independent agents conduct research without central coordination, and any contributor can deploy new agents into a shared ecosystem. The system is built around three components: an extensible registry of over 300 interoperable scientific skills, an artifact layer that preserves full computational lineage as a directed acyclic graph (DAG), and a structured platform for agent-based scientific discourse with provenance-aware governance. Agents select and chain tools based on their scientific profiles, produce immutable artifacts with typed metadata and parent lineage, and broadcast unsatisfied information needs to a shared global index. The ArtifactReactor enables plannerless coordination: peer agents discover and fulfill open needs through pressure-based scoring, while schema-overlap matching triggers multi-parent synthesis across independent analyses. An autonomous mutation layer actively prunes the expanding artifact DAG to resolve conflicting or redundant workflows, while persistent memory allows agents to continuously build upon complex epistemic states across multiple cycles. Infinite converts these outputs into auditable scientific records through structured posts, provenance views, and machine-readable discourse relations, with community feedback steering subsequent investigation cycles. Across four autonomous investigations, peptide design for the somatostatin receptor SSTR2, lightweight impact-resistant ceramic screening, cross-domain resonance bridging biology, materials, and music, and formal analogy construction between urban morphology and grain-boundary evolution, the framework demonstrates heterogeneous tool chaining, emergent convergence among independently operating agents, and traceable reasoning from raw computation to published finding.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI辅助科学研究中存在的自主性不足和协作机制缺失的问题。研究背景是，尽管人工智能（尤其是大语言模型和领域专用机器学习系统）已广泛应用于科学研究的辅助任务，如文献总结、假设生成和实验加速，但现有方法大多停留在“人类引导、AI响应”的交互范式上。这些系统通常缺乏自主发起和持续执行完整科学探索的能力，且往往围绕单一研究流程或中心化规划展开，难以模拟真实科学发现中分布式、多线索并行并最终收敛的协作过程。

现有方法的不足主要体现在：一是多数AI科学系统仍以辅助人类研究者为核心，或仅自动化单一研究管线，未能形成多智能体持久、自组织的科研生态系统；二是缺乏支持智能体间无中心协调、基于成果交换进行自发协作的机制；三是科学发现过程中产生的计算过程、中间结果和推理脉络往往未被系统化记录和共享，导致可追溯性和可复用性受限。

本文要解决的核心问题是：如何构建一个支持多智能体在无中央规划的情况下，通过发布、交换和合成“科研工件”来实现分布式自主科学发现的框架。具体而言，论文提出了ScienceClaw + Infinite框架，通过三个核心组件——可扩展的科学技能注册库、记录完整计算谱系的有向无环图工件层、以及支持溯源性治理的结构化智能体科学讨论平台——来使智能体能够基于科学配置文件自主选择并链式使用工具，生成带有元数据和谱系信息的不可变工件，并通过广播未满足的信息需求触发其他智能体的协作。该框架旨在实现“无规划者协调”，使独立运行的智能体能通过压力评分和模式匹配机制，自发地发现并满足开放需求，甚至跨分析进行多父源合成，最终推动异构工具链的整合、独立智能体间的涌现性收敛，以及从原始计算到发表成果的可追溯推理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类与平台类。

在方法类研究中，现有工作多集中于利用大语言模型辅助文献总结、假设生成或代码编写，以及利用特定领域机器学习系统加速蛋白质结构预测、材料筛选等任务。然而，这些系统通常以人为中心，依赖于交互式提示，而非自主发起和协调研究。近期研究开始探索多智能体在假设生成和研究提案中的辅助作用，或尝试自动化研究循环中的部分环节（如实验执行、论文草拟），但大多仍围绕单一人机协作流程或单一研究管线展开。本文的框架则强调构建一个持久的、去中心化的生态系统，智能体可自主选择并链式调用工具，通过无规划者的协调机制（如基于压力的需求匹配）实现跨智能体的涌现协作。

在应用类研究中，已有诸多AI科学应用专注于特定领域的发现自动化，例如分子生成或材料筛选。本文通过四个跨领域自主研究案例（如肽设计、陶瓷筛选、跨域共振探索和形式类比构建），展示了其框架在异构工具链式调用、独立智能体间涌现收敛以及从原始计算到发表成果的可追溯推理方面的能力，超越了单一领域或任务的局限。

在平台类或评测类研究中，一些科学多智能体系统提出了支持AI研究的持久基础设施雏形。本文的工作与之相关，但更系统地构建了包含可扩展技能注册表、完整计算谱系追溯的工件层以及结构化科学讨论平台的三组件架构，并引入了如工件反应堆、自主突变层等机制，以实现无中心协调的分布式发现和知识状态的持续演进。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ScienceClaw + Infinite的分布式自主科研框架来解决无中心协调下的多智能体协作与发现难题。其核心方法是建立一个围绕**可计算溯源工件（Artifact）**和**无规划者协调（Plannerless Coordination）**的生态系统，使独立运行的智能体能通过共享的“信息需求”信号和工件图谱自发地协同工作，最终收敛于创新性科学发现。

**整体框架与主要模块**：
系统设计了一个六阶段闭环生态系统：
1.  **智能体与技能执行（ScienceClaw）**：每个智能体拥有独特的科学个性档案（Profile），据此从超过300个可组合的跨领域技能（如蛋白质分析、材料科学、音乐分析）中选择并串联工具链以研究问题。
2.  **计算与工件生成**：每次技能调用产生一个**不可变工件（Artifact）**，包含唯一ID、类型、内容哈希和父工件ID，形成有向无环图（DAG）记录完整计算谱系。智能体同时将未满足的“信息需求”广播至全局索引。
3.  **可视化**：专用绘图智能体从工件DAG生成图表。
4.  **结构化发布与交互（Infinite）**：研究发现被发布为包含证据面和溯源信息的结构化帖子，并可自动生成arXiv风格报告。
5.  **社区反馈**：来自其他智能体或人类的投票、行动等反馈信号产生新的需求。
6.  **反馈循环**：反馈信号影响**工件反应堆（ArtifactReactor）**的压力评分器，引导下一轮探索朝向高影响力、未充分探索的方向。

**关键技术设计与创新点**：
1.  **基于工件的无规划者协调机制**：这是核心创新。系统摒弃了中央任务分配器，代之以**工件反应堆**实现去中心化协作。其通过两种信号驱动：
    *   **显式需求广播**：智能体将具体数据需求（如“TP53 Y220C的蛋白质结构数据”）发布到全局索引。
    *   **隐式模式重叠匹配**：反应堆检测到多个独立产生的工件其数据模式（JSON键）与某个技能的输入参数重叠时，自动触发合成。
    *   **压力评分**：对开放需求进行优先级排序，评分函数综合考虑**新颖性**（被满足次数少则优先级高）、**中心性**（越多智能体共享此需求则优先级高）、**深度**（在DAG中的位置）和**年龄**（防止需求饿死）。这确保了协作资源自动流向最紧迫、最具共识潜力的探索方向。

2.  **多父合成与涌现收敛**：当两个及以上兼容的同行工件（针对同一需求或技能）存在时，反应堆将它们合并，运行共享技能，产生一个**多父合成工件**。该工件的父ID列表明确记录了所有贡献者，形成了一个任何单一智能体都无法独立产生的新知识节点，实现了真正的涌现性发现。

3.  **自主突变层与DAG治理**：**工件突变器（ArtifactMutator）** 持续监控扩展中的工件DAG，自动检测并处理冗余（重复分析）、停滞（死分支）和冲突（矛盾发现）。它通过修剪、分叉或合并操作来引导集体探索远离重复工作，趋向收敛共识，从而在没有人工干预的情况下维持探索的效率和方向性。

4.  **持久化状态与跨周期学习**：系统通过**智能体日志**、**调查追踪器**和**知识图谱**三个协同存储，使智能体能够在多次“心跳”循环中持续积累复杂的认知状态，实现长期的、递进式的科学探究。

总之，该论文通过构建一个以不可变工件为基石、以需求广播和模式匹配为协调纽带、以压力驱动和自主突变为导向机制的分布式系统，成功地解决了多智能体在无中心控制下进行有效、涌现式科学协作的复杂问题。

### Q4: 论文做了哪些实验？

论文在四个跨学科案例中进行了自主科学探究实验，以验证其框架的有效性。实验设置方面，系统部署了多个独立运行的智能体，它们基于可扩展的技能注册表（包含超过300种可互操作的科学技能）自主选择并组合工具，通过无中心协调的“ArtifactReactor”机制进行协作，并生成带有完整计算谱系（DAG）的不可变工件。

数据集与基准测试涵盖四个领域：1）针对生长抑素受体SSTR2的肽设计；2）轻质抗冲击陶瓷筛选；3）跨生物学、材料和音乐领域的共振桥接研究；4）城市形态与晶界演化之间的形式类比构建。这些案例没有使用统一的传统基准数据集，而是作为异构、开放的探索性任务。

对比方法方面，论文主要强调其框架与传统集中式规划或人工引导工作流的区别，通过完全自主、分布式的多智能体协作来体现其创新性。实验过程中没有进行与外部特定算法的直接量化对比，而是通过框架内部的协调机制和产出结果来证明其能力。

主要结果通过定量指标呈现（汇总如下表），展示了系统的规模、复杂性和协调效果：

| 案例研究 | 参与智能体数 | 调用工具数 | 生成工件数 | 合成工件数 | 平均DAG深度 |
|:---|:---|:---|:---|:---|:---|
| 蛋白质设计 | 10 | 23 | 177 | 57 | 2.15 |
| 材料发现 | 8 | 10 | 73 | 22 | 2.25 |
| 共振景观 | 13 | 12 | 159 | 19 | 2.00 |
| 形式类比 | 9 | 23 | 52 | 25 | 2.00 |

关键数据指标分析表明：1）**工件生成效率**：不同案例模式各异，如蛋白质设计每个工具平均生成7.7个工件，而形式类比仅为2.3个，体现了工作流的差异性。2）**合成活动**：合成工件占比（合成密度）在12%（共振）到48%（形式类比）之间，设计驱动型研究约为30-32%，表明智能体能有效整合多源证据。3）**协调深度**：蛋白质设计和材料发现的平均DAG深度较高（>2.1），反映多阶段证据聚合；而共振和形式类比深度为2.0，表明更顺序化的分析流程。4）**自主性**：所有实验均在无人为干预或重定向下完成，证实了跨8-13个智能体的稳健自主协调能力。

具体到SSTR2肽设计案例，智能体通过结构分析（PDB 7XNA）、序列比对、进化分析和蛋白质语言模型（ESM-2）评估，识别出核心K-T-C基序为结合热点，并提出了优化候选肽（如MGLKNFFLKTFTSC），同时也发现了其分子量过大的潜在限制。该过程通过平台的“Graph”和“Dataflow”视图完整记录了智能体间的交互和计算溯源，体现了从原始计算到发表结论的可追溯推理。

### Q5: 有什么可以进一步探索的点？

该论文提出的无中心协调、基于涌现式交互的框架虽具创新性，但仍存在若干局限与可拓展方向。首先，系统依赖预定义的技能库与元数据模式，在面对高度开放、定义模糊的科学问题时，其自主探索能力可能受限。未来可引入基于大语言模型的动态技能生成与抽象问题分解机制，增强对未知领域的适应力。其次，当前“压力评分”与架构匹配的协调机制较为简单，可能导致效率低下或陷入局部优化。可探索引入基于强化学习的多智能体协作策略，使智能体能够学习何时竞争、何时合作，并动态调整资源分配。此外，系统虽支持工作流剪枝，但缺乏对科学假设生成与验证循环的显式建模。未来可整合主动学习与贝叶斯优化，使智能体能自主设计实验、评估证据强度，并形成可解释的因果推理链条。最后，该框架尚未充分解决跨模态、跨尺度数据的融合问题。在如生物-材料-音乐的跨域共振案例中，引入神经符号推理或概念嵌入对齐技术，可能更有效地发现深层类比关系，推动跨学科知识发现。

### Q6: 总结一下论文的主要内容

该论文提出了ScienceClaw + Infinite框架，旨在实现无需中央协调的自主科学发现。核心问题是如何让多个AI代理在分布式环境中独立开展研究，并通过交互与协作推动科学进程。框架包含三个关键组件：可扩展的科学技能注册库（含300多项互操作工具）、以有向无环图（DAG）形式完整保存计算谱系的**物证层**，以及支持代理间结构化科学讨论的平台。

方法上，代理基于科学配置文件选择和链式调用工具，生成带有类型化元数据和父系谱系的不可变物证，并将未满足的信息需求广播至全局索引。通过**ArtifactReactor**实现无规划协调：代理通过压力评分发现并响应开放需求，模式重叠匹配触发跨独立分析的多父合成。自主变异层主动修剪物证DAG以解决冲突或冗余工作流，持久化记忆使代理能在多周期中持续构建复杂认知状态。

主要结论显示，在肽设计、陶瓷材料筛选、跨域共振探索和形式类比构建四个自主研究中，框架成功实现了异构工具链式调用、独立运行代理间的**涌现式收敛**，以及从原始计算到发表成果的可追溯推理。其意义在于推动了AI从辅助工具向自主研究参与者的转变，为分布式、众包式科学发现提供了可审计、可扩展的生态系统。
