---
title: "SkillOrchestra: Learning to Route Agents via Skill Transfer"
authors:
  - "Jiayu Wang"
  - "Yifei Ming"
  - "Zixuan Ke"
  - "Shafiq Joty"
  - "Aws Albarghouthi"
  - "Frederic Sala"
date: "2026-02-23"
arxiv_id: "2602.19672"
arxiv_url: "https://arxiv.org/abs/2602.19672"
pdf_url: "https://arxiv.org/pdf/2602.19672v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 规划/推理"
  - "Agent 评测/基准"
  - "强化学习"
relevance_score: 9.0
---

# SkillOrchestra: Learning to Route Agents via Skill Transfer

## 原始摘要

Compound AI systems promise capabilities beyond those of individual models, yet their success depends critically on effective orchestration. Existing routing approaches face two limitations: (1) input-level routers make coarse query-level decisions that ignore evolving task requirements; (2) RL-trained orchestrators are expensive to adapt and often suffer from routing collapse, repeatedly invoking one strong but costly option in multi-turn scenarios. We introduce SkillOrchestra, a framework for skill-aware orchestration. Instead of directly learning a routing policy end-to-end, SkillOrchestra learns fine-grained skills from execution experience and models agent-specific competence and cost under those skills. At deployment, the orchestrator infers the skill demands of the current interaction and selects agents that best satisfy them under an explicit performance-cost trade-off. Extensive experiments across ten benchmarks demonstrate that SkillOrchestra outperforms SoTA RL-based orchestrators by up to 22.5% with 700x and 300x learning cost reduction compared to Router-R1 and ToolOrchestra, respectively. These results show that explicit skill modeling enables scalable, interpretable, and sample-efficient orchestration, offering a principled alternative to data-intensive RL-based approaches. The code is available at: https://github.com/jiayuww/SkillOrchestra.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复合AI系统中智能体协同（orchestration）的核心难题。现有方法存在两大局限：一是传统的模型路由（model routing）方法仅在查询级别进行粗粒度的、静态的模型选择，无法适应多轮交互中动态变化的任务需求；二是基于强化学习（RL）的编排器虽然能学习序列化路由策略，但训练成本高昂、难以适应模型/工具池的更新，并且容易陷入“路由崩溃”（routing collapse），即在多轮决策中反复调用同一个（可能强大但昂贵）的选项，无法实现性能与成本的均衡权衡。

为此，论文提出了SkillOrchestra框架，其核心思想是将编排决策建立在显式的、细粒度的“技能”抽象之上。该方法不直接端到端学习路由策略，而是首先从执行经验中学习一个可复用的“技能手册”，其中编码了不同操作模式下的细粒度技能要求，以及各个智能体在不同技能下的性能与成本画像。在部署时，编排器根据当前交互状态推断所需的技能，并依据明确的性能-成本权衡来选择最合适的智能体。这种方法旨在实现更精细、更稳定、可迁移且样本高效的智能体协同，为数据密集的RL方法提供了一个原则性的替代方案。

### Q2: 有哪些相关研究？

相关工作主要分为两类：模型路由（Model Routing）和基于强化学习的路由与编排（RL-based Routing and Orchestration）。

在模型路由方面，早期研究采用启发式或级联策略，例如基于预测难度或预算约束来分配查询（如FrugalGPT）。后续工作大多学习从查询特征到模型选择的静态映射（如Blender），或使用基于相似度的方法（如RouterBench、RouteLLM）、神经网络分类器/集成（如Zooter）以及基于图的模型（如GraphRouter）进行判别式查询-模型匹配。然而，这些方法通常仅基于输入级特征为每个查询做一次粗粒度的路由决策，无法建模模型在任务中间阶段的能力差异，因此难以支持细粒度的多步编排。

在基于强化学习的路由与编排方面，近期研究将路由建模为序列决策过程，并使用强化学习训练基于LLM的路由器，例如Router-R1和ToolOrchestra。这些系统通过轨迹级奖励优化性能与成本的权衡，实现了更灵活的多步决策。但它们也面临训练成本高、对新模型池或任务适应性差，以及策略“路由崩溃”（即路由器反复调用单一强大但昂贵的模型）等挑战。

本文提出的SkillOrchestra与上述工作的关系在于：它针对现有模型路由方法粒度粗糙、以及RL方法成本高且易崩溃的局限性，引入了“技能”作为中间抽象。通过从执行经验中学习细粒度技能并建模各代理在特定技能下的能力和成本，SkillOrchestra实现了数据高效、可迁移且更平衡的编排，为数据密集的RL方法提供了一种原则性的替代方案。

### Q3: 论文如何解决这个问题？

SkillOrchestra通过引入“技能手册”（Skill Handbook）这一核心概念，将智能体编排问题重构为基于技能的决策，而非端到端的策略优化。其核心方法、架构设计和关键技术如下：

**核心方法与架构设计：**
SkillOrchestra的架构围绕一个结构化的、可学习的“技能手册”展开。该手册在训练阶段从执行轨迹中增量构建，在推理阶段用于指导模式选择和智能体路由。手册包含三个层次的知识：(1) **模式级元数据**：存储不同交互状态下应选择何种操作模式（如搜索、编码）的洞察；(2) **技能注册表**：定义细粒度的、可重用的能力抽象（技能），作为高层模式与具体智能体之间的中间层；(3) **智能体档案**：为每个智能体在不同模式下，记录其针对各项技能的胜任概率估计、执行成本及路由信号。

**关键技术：**
1.  **技能建模与发现**：技能被形式化定义为能力描述和上下文指示符的元组。通过对比同一查询下成功与失败的执行轨迹，利用LLM抽象出缺失的能力，从而发现新技能并加入注册表。
2.  **基于技能的智能体路由**：在推理时，编排器首先根据当前交互状态和手册中的模式级元数据选择操作模式。然后，识别在当前状态下“活跃”的相关技能集合。最后，通过一个显式的性能-成本权衡公式选择智能体：综合考虑智能体在活跃技能集上的平均胜任概率估计和其在该模式下的预估执行成本。
3.  **技能手册的个性化选择与精炼**：并非所有编排器都能同等有效地利用细粒度技能。因此，系统通过帕累托最优验证，为特定编排器选择一个技能粒度最匹配其推理能力的子手册，以平衡性能与稳定性。此外，手册会通过周期性的**拆分**（当技能内智能体表现方差过大时）和**合并**（当不同技能的智能体表现分布无法区分时）操作进行精炼，避免冗余或过度碎片化。

总之，SkillOrchestra通过将编排知识显式地、结构化地编码进技能手册，实现了对智能体能力和任务需求的解耦。这种方法避免了传统基于强化学习的编排器常见的“路由崩溃”问题，并显著提升了样本效率和可解释性，同时通过技能粒度的自适应选择确保了不同能力编排器的稳定部署。

### Q4: 论文做了哪些实验？

论文在模型路由场景下进行了系统实验，覆盖十个基准测试，包括通用问答（Natural Questions、TriviaQA、PopQA）、多跳问答（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle）和数学推理（MATH、AMC23）。实验设置旨在评估SkillOrchestra在有效性、效率、路由行为、可迁移性和组件贡献五个方面的表现。主要结果显示，SkillOrchestra在端到端准确率上显著优于现有基于强化学习的协调器（如Router-R1和ToolOrchestra），最高提升达22.5%，同时学习成本分别降低了700倍和300倍。此外，技能建模有效缓解了路由崩溃问题，能根据任务难度动态匹配模型能力，并在不同协调器间实现了技能手册的零样本重用，证明了其可扩展性、可解释性和样本效率优势。

### Q5: 有什么可以进一步探索的点？

SkillOrchestra的核心创新在于通过显式技能建模来优化路由，但其局限性与未来方向也与此紧密相关。主要局限性在于：1) 技能的定义和提取仍依赖于预定义的执行轨迹和经验，其完备性和泛化性可能受限，对于开放域或动态变化的新任务，技能库的构建和更新可能成为瓶颈。2) 框架假设了技能需求可以被准确推断，但在复杂、模糊或多模态的交互中，对当前任务所需技能的实时、精确识别仍具挑战性，可能影响路由的准确性。

未来可探索的方向包括：1) 研究更动态、自适应的技能发现与演化机制，使系统能在任务执行过程中自动发现、组合或精炼新技能，减少对预先收集经验的依赖。2) 探索将技能建模与更强大的世界模型或推理模块结合，以提升对复杂、多步骤任务中隐含技能需求的推断能力。3) 将框架扩展到更广泛的多智能体协作场景，如考虑智能体间的主动技能传递与协同，而不仅仅是基于成本效益的选择，以实现更有机的群体智能。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillOrchestra框架，旨在解决复合AI系统中智能体协同调度的核心挑战。现有方法存在两大局限：一是基于输入的路由器仅做粗粒度的查询级决策，无法适应多轮交互中动态变化的任务需求；二是基于强化学习的调度器训练成本高昂且易陷入“路由崩溃”，即反复调用单一强大但昂贵的选项。

SkillOrchestra的核心贡献在于引入了“技能感知”的调度新范式。它不直接端到端学习路由策略，而是从执行经验中学习细粒度的技能，并建模每个智能体在不同技能下的能力与成本。在部署时，调度器会推断当前交互所需的技能组合，并在明确的性能-成本权衡下，选择最能满足需求的智能体。

该框架的意义在于提供了一种可扩展、可解释且样本高效的调度原理性替代方案。实验表明，其在十个基准测试上优于最先进的基于强化学习的调度器，性能提升最高达22.5%，同时学习成本降低了数百倍。这标志着通过显式的技能建模，能够实现更优的资源分配，为构建复杂、经济的多智能体系统提供了新路径。
