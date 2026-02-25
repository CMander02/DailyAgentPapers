---
title: "Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory"
authors:
  - "Haoyang Li"
  - "Yang You"
  - "Hao Su"
  - "Leonidas Guibas"
date: "2026-02-23"
arxiv_id: "2602.20323"
arxiv_url: "https://arxiv.org/abs/2602.20323"
pdf_url: "https://arxiv.org/pdf/2602.20323v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 自演化"
  - "Agent 规划"
  - "Agent 记忆"
  - "测试时学习"
  - "具身智能"
  - "机器人操作"
  - "物理推理"
  - "经验验证"
  - "视觉语言模型"
relevance_score: 9.5
---

# Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory

## 原始摘要

Reliable object manipulation requires understanding physical properties that vary across objects and environments. Vision-language model (VLM) planners can reason about friction and stability in general terms; however, they often cannot predict how a specific ball will roll on a particular surface or which stone will provide a stable foundation without direct experience. We present PhysMem, a memory framework that enables VLM robot planners to learn physical principles from interaction at test time, without updating model parameters. The system records experiences, generates candidate hypotheses, and verifies them through targeted interaction before promoting validated knowledge to guide future decisions. A central design choice is verification before application: the system tests hypotheses against new observations rather than applying retrieved experience directly, reducing rigid reliance on prior experience when physical conditions change. We evaluate PhysMem on three real-world manipulation tasks and simulation benchmarks across four VLM backbones. On a controlled brick insertion task, principled abstraction achieves 76% success compared to 23% for direct experience retrieval, and real-world experiments show consistent improvement over 30-minute deployment sessions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型（VLM）作为机器人规划器时，其抽象的物理知识难以在具体、动态的真实物理环境中有效应用的问题。研究背景是，尽管VLM能够描述摩擦力、平衡等通用物理概念，但当它们被部署为机器人规划器去执行具体操作任务（如预测特定球在特定表面的滚动行为、判断哪块石头能提供稳定支撑）时，往往因缺乏对具体对象和环境的直接物理体验而失败。现有基于记忆的方法（如直接检索和回放过往经验）存在明显不足：它们倾向于机械地应用历史经验，而物理环境（如摩擦系数、物体形状）的细微变化就可能导致这些未经核验的经验失效，表现为行为僵化和成功率低下。

因此，本文要解决的核心问题是：如何让VLM机器人规划器能够在测试阶段（即部署过程中），不更新模型参数，仅通过自身与环境的交互，来动态地学习并验证适用于当前具体场景的物理原理，从而提升其在复杂物理任务中的规划性能和适应性。论文提出的PhysMem框架正是为了通过一个结构化的“记忆-假设-验证”科学循环，实现这种从交互中学习可泛化物理原则的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、适应类与记忆系统类。

在**方法类**工作中，视觉语言模型（VLM）规划器已能进行常识推理，如Robotics Transformer系列通过大规模预训练实现技能迁移，后续研究通过流匹配、具身推理和思维链机制提升通用策略能力。然而，这些方法依赖预训练知识，无法在测试时适应新遇到的物理属性。本文提出的PhysMem框架则通过测试时记忆与交互来填补这一“领域鸿沟”，实现无需参数更新的物理原理学习。

在**适应类**工作中，测试时适应方法（如元学习、领域随机化、序列建模的上下文学习）使机器人能快速调整至新条件。近期研究也探索了通过强化学习、语言纠正进行在线适应。但这些方法侧重于隐式的策略调整，而本文专注于生成**可解释、可验证**的显式物理假设，使习得的知识透明且可迁移。

在**记忆系统类**工作中，现有方法通过层次检索、双记忆库或世界模型积累经验以增强规划。反思式方法利用大语言模型从失败中学习，检索增强方法直接提供过往经验。然而，它们通常仅从失败中反思，或盲目应用检索到的经验。本文的核心创新在于引入了“科学循环”：从成功和失败中生成假设，通过针对性交互进行验证，并仅提升已验证的原理，从而避免了在物理条件变化时对过往经验的僵化依赖。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PhysMem的测试时记忆框架来解决机器人物理操作中因物体和环境物理属性动态变化而导致的规划不可靠问题。其核心方法是设计了一个“科学循环”，使视觉语言模型（VLM）规划器能够在测试时通过交互学习物理原理，而无需更新模型参数。

整体框架由三个主要组件构成：1）基于VLM的规划器，负责结合观察和已学原理生成高层决策；2）分层记忆系统，包括存储原始经验的“情景记忆”、存储待验证假设的“工作记忆”以及存储已验证原理的“长时记忆”；3）执行器，通过底层策略执行规划动作。系统运行的核心是“科学循环”，它包含四个关键阶段：经验收集、假设生成、归因验证和原理提升。

在技术实现上，首先，系统通过“共振检查”机制收集交互经验。当新经验与当前激活的原理预测不一致（即“意外”事件）时，会触发记忆巩固过程，从而聚焦于学习新情况。其次，经验会按符号状态聚类，并利用一个反思模型（在现实世界中使用VLM，仿真中使用LLM）从经验簇中生成形式化的假设（如“避免在Y条件下做X”、“在Y条件下优先做X”等）。关键的创新点在于“行动级归因”验证：系统不是基于整个任务的成功与否，而是基于特定行动的结果来评估假设的置信度，从而隔离了混杂因素的影响。只有当假设的置信度超过阈值（如0.8）且有足够支持证据时，才会被提升为已验证的原理，并注入到VLM规划器的提示中，用于指导未来决策。反之，置信度过低的假设会被反驳和移除。这种“验证后应用”的设计，避免了检索增强方法中直接应用旧经验可能导致的“教条主义”问题，确保了在物理条件变化时系统的适应性。

此外，记忆系统通过“记忆折叠”机制在原理提升后压缩原始经验，优化了存储效率。长时记忆中的原理还引入了重要性衰减机制，以逐步淘汰过时的知识。该框架的创新性在于将科学方法的归纳-验证过程形式化地集成到机器人学习循环中，实现了在测试时持续、自主地提炼和更新关于物理世界的可操作知识。

### Q4: 论文做了哪些实验？

论文在真实世界和仿真环境中进行了多组实验，以评估PhysMem框架的性能。实验设置包括三个真实世界操作任务（零件放置、小球滚动和石块堆叠）以及一个仿真基准测试（积木插入任务）。使用了四种不同的视觉语言模型（VLM）作为骨干网络进行测试，包括Gemini-3-Flash、Gemini-ER-1.5、GPT-5.1和Qwen3-VL-235B。

对比方法主要涉及与直接经验检索（Direct Retrieval）的对比，并进行了广泛的消融实验，以验证框架中各个组件（如共振过滤、假设验证、工作记忆和遗忘机制）的必要性。主要结果如下：在受控的积木插入任务中，基于原理抽象的方法取得了76%的成功率，而直接经验检索仅为23%。真实世界实验显示，在30分钟的部署过程中，系统性能持续提升。关键指标包括共振分数（ρ），该分数从初始约0.2上升到第10次尝试时的0.9，表明预测与观察结果逐渐吻合。在任务得分方面，理性阶段（ρ > 0.7）的得分比最初几次尝试高出2.3倍。此外，研究还发现，当物理条件相似时，先验知识可以很好地进行迁移（例如石块堆叠任务达到80%成功率），但对于动态特性不同的新场景（如使用新类型小球），则必须依赖测试时自适应学习才能取得最佳效果（成功率从0%提升至40%）。消融实验进一步证实，原理抽象对于处理复杂任务至关重要，而遗忘机制则在准确性和计算效率（令牌消耗减少至1/3.4）之间取得了良好平衡。

### Q5: 有什么可以进一步探索的点？

本文提出的PhysMem框架虽在测试时学习物理原理方面取得了进展，但仍存在一些局限性和可拓展方向。首先，系统依赖于预设的假设生成与验证流程，其效率受限于交互次数和场景复杂度，在动态或高度不确定环境中可能难以快速收敛。其次，记忆存储与检索机制仍较简单，缺乏对经验之间关联性的结构化建模，可能影响知识迁移的泛化能力。

未来研究可从以下方向深入：一是引入元学习或概率推理方法，使系统能主动评估不确定性并优化探索策略，减少验证所需的交互成本。二是构建层次化记忆网络，将物理原理抽象为不同颗粒度的知识模块，支持跨任务的知识组合与推理。此外，可探索多模态感知（如触觉、力反馈）与VLM的融合，以更丰富的数据源提升物理理解的精度。最后，将框架扩展至长期部署场景，研究记忆压缩与遗忘机制，避免经验库膨胀导致的效率下降，实现持续自适应学习。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PhysMem的记忆框架，旨在解决视觉语言模型（VLM）在机器人规划中难以预测具体物体物理属性（如摩擦、稳定性）的问题。核心问题是VLM虽能进行一般性物理推理，但缺乏对特定物体和环境的直接经验，导致在实际操作中可靠性不足。

方法上，PhysMem允许VLM规划器在测试时通过交互学习物理原理，而无需更新模型参数。其框架包含三个关键步骤：记录交互经验、生成候选假设，并通过有针对性的交互验证这些假设。验证后的知识被提升为已验证记忆，用于指导未来决策。一个核心设计是“先验证后应用”，即系统用新观察测试假设，而非直接应用检索到的经验，从而在物理条件变化时减少对先前经验的僵化依赖。

主要结论显示，PhysMem在三个真实世界操作任务和模拟基准测试中显著提升了性能。例如，在积木插入任务中，其基于原理抽象的方法取得了76%的成功率，而直接经验检索仅为23%。真实世界实验也表明，在30分钟的部署中性能持续改善。该工作的意义在于为机器人提供了一种在测试时自适应学习物理知识的方法，增强了其在动态环境中的泛化能力和可靠性。
