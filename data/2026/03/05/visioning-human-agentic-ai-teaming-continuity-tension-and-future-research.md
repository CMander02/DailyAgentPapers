---
title: "Visioning Human-Agentic AI Teaming: Continuity, Tension, and Future Research"
authors:
  - "Bowen Lou"
  - "Tian Lu"
  - "T. S. Raghu"
  - "Yingjie Zhang"
date: "2026-03-05"
arxiv_id: "2603.04746"
arxiv_url: "https://arxiv.org/abs/2603.04746"
pdf_url: "https://arxiv.org/pdf/2603.04746v1"
categories:
  - "cs.AI"
  - "cs.HC"
  - "econ.GN"
tags:
  - "Human-Agent Interaction"
relevance_score: 5.0
taxonomy:
  capability:
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "Survey/Position Paper"
attributes:
  base_model: "N/A"
  key_technique: "Extension of Team Situation Awareness (Team SA) theory"
  primary_benchmark: "N/A"
---

# Visioning Human-Agentic AI Teaming: Continuity, Tension, and Future Research

## 原始摘要

Artificial intelligence is undergoing a structural transformation marked by the rise of agentic systems capable of open-ended action trajectories, generative representations and outputs, and evolving objectives. These properties introduce structural uncertainty into human-AI teaming (HAT), including uncertainty about behavior trajectories, epistemic grounding, and the stability of governing logics over time. Under such conditions, alignment cannot be secured through agreement on bounded outputs; it must be continuously sustained as plans unfold and priorities shift. We advance Team Situation Awareness (Team SA) theory, grounded in shared perception, comprehension, and projection, as an integrative anchor for this transition. While Team SA remains analytically foundational, its stabilizing logic presumes that shared awareness, once achieved, will support coordinated action through iterative updating. Agentic AI challenges this presumption. Our argument unfolds in two stages: first, we extend Team SA to reconceptualize both human and AI awareness under open-ended agency, including the sensemaking of projection congruence across heterogeneous systems. Second, we interrogate whether the dynamic processes traditionally assumed to stabilize teaming in relational interaction, cognitive learning, and coordination and control continue to function under adaptive autonomy. By distinguishing continuity from tension, we clarify where foundational insights hold and where structural uncertainty introduces strain, and articulate a forward-looking research agenda for HAT. The central challenge of HAT is not whether humans and AI can agree in the moment, but whether they can remain aligned as futures are continuously generated, revised, enacted, and governed over time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由“智能体化人工智能”（agentic AI）的兴起所引发的人类-AI协同（HAT）领域的新挑战。研究背景是，传统AI系统（如符号AI和早期机器学习）通常任务特定、不确定性有界且受人类直接监督，其输出和行为相对可预测。现有的人类-AI协作理论和设计原则（如基于互补性的团队协作模型）大多建立在这种“有界条件”的稳定假设之上，强调通过界面设计、可解释性和决策支持来实现初始对齐和协调。

然而，以大型语言模型和自主架构为驱动的智能体化AI具备了开放式智能体特性，包括：1）开放式行动轨迹（轨迹不确定性），能自主选择、修订多步行动；2）开放式表征和输出（认知不确定性），能生成流畅但认知基础可能薄弱的解释和内容；3）开放式目标与行为演化（机制不确定性），其决策策略和能力可能随时间非平稳变化。这些特性引入了“结构性不确定性”，使得传统方法的核心前提——即一旦通过共享感知、理解和预测达成团队态势感知（Team SA），就能通过迭代更新支持协调行动——不再成立。现有方法的不足在于，它们未能充分应对智能体化AI带来的持续动态对齐挑战，其稳定化逻辑在开放式智能体面前受到质疑。

因此，本文要解决的核心问题是：在智能体化AI引入结构性不确定性的条件下，人类与AI如何能够不仅在当下达成一致，更能在未来被持续生成、修订、实施和治理的过程中保持动态对齐？论文通过延伸和审视团队态势感知理论，旨在重新概念化开放式智能体下的人类与AI意识，并探究传统上用于稳定团队协作的动态过程（如关系互动、认知学习、协调控制）是否依然有效，从而为未来的人类-智能体化AI协同研究指明方向。

### Q2: 有哪些相关研究？

本文梳理了与人类-智能体团队协作（HAT）相关的多个研究脉络，并以团队态势感知（Team SA）作为整合框架进行组织。相关研究主要可分为以下几类：

**1. 评估与态度理论**：如算法厌恶/欣赏理论、计划行为理论，关注个体对AI输出的初始评价和接纳意愿，直接影响个体层面的感知（SA Level 1），但较少涉及跨行动者的感知对齐。

**2. 关系互动理论**：包括信任、社会临场感等研究，探讨人类将AI视为合法队友的社会条件，为持续的信息交换和共同期望提供支持，是共享SA的使能条件，但对任务理解和未来预测的形成机制阐述不足。

**3. 认知学习理论**：如实例学习理论、机器诱发反思模型，解释人类如何通过经验和反馈从AI中学习并调整心智模型，主要涉及理解层面（SA Level 2），但侧重于个体认知，对团队环境中心智模型的协同对齐关注有限。

**4. 解释与指导理论**：以可解释AI和意义建构理论为代表，通过系统干预（如解释）支持人类理解AI行为并规划行动，直接辅助Level 2理解及有限的Level 3预测，但多为片段化、工具中心式，对多行动者间持续协同的共享SA关注较少。

**5. 集体协调理论**：包括集体注意力、集体智能、互补性与角色理论，研究跨相互依赖行动者的意识与努力分配，强调差异化监控和信息流对分布式SA的贡献，但对快速变化条件下共享心智模型的更新机制阐述不足。

**6. 操作控制理论**：如有意义的人类控制、委托模型、工作系统视角，关注人机之间权威、责任与监督的分配，预设了对未来行为的预测能力（SA Level 3），但通常假定决策策略相对有界和稳定。

本文与这些工作的关系在于，**以团队SA为整合锚点**，将上述理论映射到感知、理解、预测三个层级，阐明各自如何解释HAT的特定方面，同时揭示其在孤立考量时的解释局限。**核心区别**在于，现有理论大多基于行为有界、目标稳定的系统，而本文聚焦于**具开放式能动性的智能体AI**所带来的结构性不确定性，挑战了传统团队SA中“迭代促进对齐”的稳定化逻辑，强调在持续生成、修订和治理未来的动态过程中维持对齐的新挑战。

### Q3: 论文如何解决这个问题？

论文通过重构团队态势感知（Team SA）理论来解决人-智能体团队协作中的结构不确定性挑战。核心方法是将Team SA作为分析框架，区分其静态基础层与动态团队过程层，并在此基础上识别连续性（continuity）与张力（tension），从而明确既有理论在智能体AI下的适用性与需重新思考之处。

整体框架以Team SA的三层结构（感知、理解、投影）为基石，分别从人类侧和AI侧进行重构。主要模块包括：1）**静态对齐层**：作为认知基线，要求人类与AI在感知、理解和投影上保持持续一致，但对齐的对象从有界输出转变为开放的行动轨迹、生成式表征和演化目标。2）**动态团队过程层**：涵盖关系互动、认知学习、协调与控制，传统上这些过程通过迭代更新稳定团队协作，但智能体AI的开放特性可能使其失效，引发表征漂移或权威模糊。

创新点体现在：第一，**扩展Team SA以重新概念化人类与AI的感知**：在感知层，人类需从识别离散输出转向诊断轨迹级线索，识别结构拐点；在理解层，需评估任务表征的连贯性与稳定性，进行结构性意义建构；在投影层，需判断“投影一致性”，即双方对未来轨迹和竞争目标权重的预期是否匹配。第二，**将AI态势感知视为可观测的并行系统**：提出必须使AI的内部状态（如注意力分布、任务表征、投影深度）变得可解释和可比较，通过可解释性技术（如概念激活测试）实现跨系统对齐评估。第三，**提出具体研究问题**：例如如何捕捉人类对AI轨迹转移的解释、如何评估任务表征的连贯性、如何衡量投影一致性等，使议程可操作。

关键技术涉及利用可解释AI方法（如特征归因、反事实解释）来近似AI的感知权重和内部表征，并通过系统工具化生成结构化工件，以支持人类与AI之间的态势感知互操作性。最终，论文通过区分连续性与张力，厘清了Team SA在智能体AI时代哪些核心见解依然有效，哪些机制面临压力，并为人-智能体团队协作的未来研究指明了方向。

### Q4: 论文做了哪些实验？

该论文主要进行了理论分析与框架构建，未涉及传统的量化实验或基准测试。其“实验”部分体现在对现有理论范式的延伸与检验上，具体包括：

**实验设置与数据集**：研究并未使用具体数据集，而是以“智能体化AI”（Agentic AI）这一新兴范式作为分析对象，将其特性（开放轨迹、生成表征、动态目标）视为一种“自然实验”场景，用以检验传统人类-智能体团队（HAT）理论的适用边界。

**对比方法**：核心是对比的两种理论框架。一是传统的**团队态势感知（Team SA）理论**，其基于共享的感知、理解和预测，假定达成共识后能通过迭代更新支持协调行动。二是论文**延伸后的Team SA框架**，它重新概念化了在开放智能体条件下人类与AI的感知，并强调了对异构系统间“预测一致性”的意义建构。

**主要结果与关键发现**：
1.  **连续性**：传统Team SA中关于共享认知基础（感知、理解、预测）的核心分析框架在智能体化AI背景下仍然具有**连续性**，是整合人机团队认知的基石。
2.  **张力与挑战**：智能体化AI的结构性不确定性（行为轨迹、认知基础、逻辑稳定性）对Team SA的“稳定化逻辑”构成了**根本性张力**。研究发现，传统上通过关系互动、认知学习、协调控制来稳定团队的过程，在AI具有自适应自主性时可能失效。
3.  **关键指标转向**：研究指出，HAT的核心评估指标应从静态的“瞬时共识”转向动态的**持续对齐能力**，即双方能否在目标、计划不断生成、修订、执行与治理的长期过程中保持协调。

因此，论文的“实验”本质是对理论适应性的压力测试，其核心结果是厘清了传统理论在新时代下的有效部分（连续性）与失效风险（张力），并据此提出了未来的研究议程。

### Q5: 有什么可以进一步探索的点？

本文指出，在智能体化AI带来的开放式行动轨迹、生成性表征和动态目标下，传统团队态势感知（Team SA）理论面临根本性挑战。其局限性在于，Team SA的静态认知基础（感知、理解、投射）虽仍具分析价值，但其动态过程（关系互动、认知学习、协调控制）所依赖的“对齐即稳定”前提在开放式智能体面前可能失效，反而可能导致表征漂移、认知锁定或权威模糊。

未来研究可从以下方向深入探索：首先，需开发新的评估框架，以量化人类与AI在动态任务中对轨迹信号、任务结构表征和未来投射的“对齐度”，特别是研究“投射一致性”在目标优先级漂移时的测量方法。其次，必须使AI的态势感知（感知什么、如何理解、投射何种未来）变得可观测与可解释，这需要发展新的系统工具（如结构化注意力摘要、概念激活测试）来翻译AI的高维内部状态，使其能与人类心智模型进行跨系统比较。最后，应探究不同任务类型（如常规性任务与高复杂性生成式任务）如何调节对齐机制的稳健性，并设计自适应的人机协调协议，以在持续生成与修订的未来中维持动态对齐，而非追求静态的瞬时共识。

### Q6: 总结一下论文的主要内容

本文探讨了智能体化人工智能（Agentic AI）的兴起对人类-AI团队协作（HAT）理论带来的根本性挑战。核心问题是：传统基于任务特定、边界明确、人类直接监督的AI协作理论，在面临具备开放行动轨迹、生成性表征和演化目标的智能体化AI时，已不再适用。这引入了行为轨迹、认知基础和治理逻辑稳定性三个维度的结构性不确定性。

论文的核心贡献是以团队情境感知（Team SA）理论为整合性锚点，对其进行扩展和审视，以应对上述挑战。方法上，首先扩展了Team SA理论，重新概念化了在开放智能体条件下人类和AI的感知、理解和预测，特别是跨异质系统的预测一致性意义建构。其次，论文审问了传统上通过关系互动、认知学习及协调控制来稳定团队协作的动态过程，在自适应自主性下是否依然有效。

主要结论是，智能体化AI将协调从通过初始对齐即可保障的结果，转变为一项持续的阐释与治理任务。HAT的核心挑战不在于人类与AI能否在某一时刻达成一致，而在于当未来被持续生成、修订、实施和治理时，他们能否保持对齐。论文通过区分传统见解依然有效的连续性领域与结构性不确定性带来压力的张力领域，为未来HAT研究勾勒了一个前瞻性议程。
