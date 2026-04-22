---
title: "Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game"
authors:
  - "HuaDong Jian"
  - "Chenghao Li"
  - "Haoyu Wang"
  - "Jiajia Shuai"
  - "Jinyu Guo"
  - "Yang Yang"
  - "Chaoning Zhang"
date: "2026-04-21"
arxiv_id: "2604.18975"
arxiv_url: "https://arxiv.org/abs/2604.18975"
pdf_url: "https://arxiv.org/pdf/2604.18975v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent Collaboration"
  - "Communication Efficiency"
  - "Memory"
  - "Decision-Making"
  - "Open-World Environment"
  - "Minecraft"
  - "MLLM Agent"
relevance_score: 8.0
---

# Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game

## 原始摘要

In long-horizon open-world multi-agent systems, existing methods often treat local anomalies as automatic triggers for communication. This default design introduces coordination noise, interrupts local execution, and overuses public interaction in cases that could be resolved locally. To address this issue, we propose a partitioned information architecture for MLLM agents that explicitly separates private execution states from public coordination states. Building on this design, we introduce two key mechanisms. First, we develop an event-triggered working memory based on system-verified outcomes to maintain compact and low-noise local state representations. Second, we propose a cost-sensitive gated escalation mechanism that determines whether cross-region communication should be initiated by jointly considering node criticality, local recovery cost, and downstream task impact. In this way, communication is transformed from a default reaction into a selective decision. Experiments conducted on long-term construction tasks in open environments demonstrate that, compared to baseline models based on strong communication and planned structures, the introduction of gated communication and a partitioned information architecture results in superior performance in terms of blueprint completion quality and execution chain length. It also improves local self-recovery, reduces ineffective escalations, and increases the utility of public communication.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在开放世界、长周期多智能体协作任务中，现有方法因过度或不当通信而导致的效率低下问题。研究背景是基于多模态大语言模型（MLLM）的多智能体系统在《我的世界》（Minecraft）等复杂开放环境中的应用日益广泛，这些环境具有资源依赖复杂、执行链条长等特点，需要通过多智能体分工协作来提升任务完成效率。

现有方法的不足在于，它们普遍遵循“通信优先”的范式，隐含地假设“更多通信必然带来更好协作”。具体表现为两类主流方法：或将通信视为持续共享上下文和同步计划的通道，或将通信绑定到特定异常事件（如资源短缺）的自动触发。这两种方法在长周期任务中均暴露出严重缺陷：首先，频繁的通信会中断智能体的本地连续执行，消耗认知与行动资源；其次，它将局部微小偏差不必要地升级为全局协调事件，放大了状态更新噪声，引发级联干扰；最后，现有触发机制仅基于异常的存在本身，缺乏对本地自修复能力与协作必要性的成本效益分析，导致大量无效或过早的通信。

因此，本文要解决的核心问题是：如何改变将通信作为异常发生后默认反应的范式，转而建立一个精细的裁决层，使智能体能够自主判断哪些问题应通过本地执行私下解决，哪些才真正需要升级为公开协调。换言之，论文致力于在长周期多任务场景中，实现本地自主执行稳定性与必要全局协作效率之间的最优平衡。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕开放世界多智能体协作的三个维度展开。在**规划与执行方法**方面，相关工作包括分层规划（如Voyager的迭代程序化技能库、Plan4MC的两层解耦范式）和记忆集成（如GITM和JARVIS-1利用外部知识库支持长时任务）。本文与这些工作的区别在于，现有方法通常假设环境是确定性的，仅在任务完全失败后进行恢复，而本文则专注于在持续执行中动态吸收微观层面的不确定性。在**错误恢复机制**方面，已有研究如DEPS通过自我反思触发全局重规划，但本文进一步引入了基于事件触发的本地工作记忆，以维持紧凑的低噪声状态表示，从而支持更高效的本地自我恢复。在**多智能体协作框架**方面，先前工作主要关注通信拓扑与交互协议的结构化设计，例如HAS的星型拓扑、S-agents的异步树结构、VillagerAgent的严格DAG规划器，以及ProAgent的意图建模和CoELA的记忆驱动通信。然而，这些范式通常将通信视为被动的、事件驱动的机制。本文的核心创新在于提出了成本敏感的选通升级机制，将通信从默认反应转变为选择性决策，通过联合评估节点关键性、本地恢复成本和下游任务影响，实现细粒度的成本效益权衡，从而减少无效升级并提升公共通信的效用。

### Q3: 论文如何解决这个问题？

论文通过提出一种**分区信息架构**与**门控升级机制**相结合的核心方法来解决多智能体协作中通信过度、噪声大、效率低的问题。

**整体框架与架构设计**：系统将智能体的信息状态明确划分为**私有执行状态**和**公共协调状态**两个隔离层。私有状态是一个紧凑的工作记忆，仅通过系统验证的关键事件（如初始化、动作完成）来更新，其结构化为一个包含库存、子任务、坐标、阻塞状态和已验证动作历史的元组，确保本地执行的连续性和自愈能力。公共状态则严格用于承载改变状态的协作信号，其与私有层之间的通道默认关闭，仅在必要时按协议开放短期窗口进行格式化通信，杜绝了自由形式的闲聊和冗余确认。

**核心机制与关键技术**：
1.  **事件触发的工作记忆**：私有状态的更新并非持续进行，而是由系统验证的行动结果在特定事件（如进入恢复模式）时触发。这维持了上下文的简洁性，避免了LLM自由推理带来的状态污染。
2.  **成本敏感的门控升级机制**：这是核心创新点。通信不再是对本地异常的默认反应，而是一个由三层结构（启发式规则 → 成本敏感评分 → 灰色区域LLM裁决器）驱动的选择性决策。
    *   **触发条件**：仅当检测到预定义的结构化建造问题（如材料缺失、依赖阻塞）时，才启动升级评估，避免了平滑执行阶段的不必要计算。
    *   **评分函数**：计算升级净收益的分数S，它综合了节点关键性、协调优势、下游影响等正项，以及本地可恢复性、协调历史惩罚等负项。权重经过精心设计，确保关键路径阻塞主导决策，并严格正则化过度通信。
    *   **非对称决策**：根据分数S与阈值比较，做出确定性决策（`stay_local` 或 `escalate`）。系统设计具有成本敏感性，默认倾向本地处理，仅在协作证据极强时才自动升级。
    *   **LLM裁决边界**：仅当分数处于灰色区域时，才调用一个受限的LLM作为二元分类器。其输入输出均被严格约束为结构化JSON，防止上下文漂移，确保其仅在语义模糊的边界情况下提供最小化干预。

**执行与回退**：根据门控决策，控制流被路由。若决定升级，则开放短期公共协调窗口，进行严格的协议化通信，完成后立即关闭。若决定保持本地，则交由本地求解器执行`本地恢复`（按成本从低到高尝试）或`本地跳过`（绕过非关键阻塞）。协作失败（如超时、无法供应）会触发强制通信冷却期，并立即回退到本地求解器，避免了系统死锁。

**参数校准**：门控逻辑的参数（特征权重、决策阈值）通过离线、成本敏感的优化问题进行校准，以在任务成功率与系统开销（如时间、冗余通信、LLM调用成本）之间取得帕累托最优，而非启发式调参，确保了方法的稳健性。

### Q4: 论文做了哪些实验？

论文在《我的世界》游戏的长视野开放世界多智能体协作任务上进行了系统实验。实验设置基于两个代表性平台：MindCraft 和 VillagerBench。评估分为两种环境：标准基准测试（弱协作，使用平台原生任务）和自定义数据集（高协作，通过注入显式的物资分割和依赖瓶颈来强制智能体进行通信权衡）。自定义数据集包含200个场景，分为四类压力测试情景。

对比方法选取了两种主流多智能体范式：MindCraft（采用即时自由形式通信的 FlatComm 基线）和 VillagerAgent（采用集中式有向无环图规划的 DAG 基线）。

主要结果从整体性能和协调效率两方面衡量。关键数据指标包括：
1.  **宏观性能指标**：任务成功率（TSR）和完成步数（CS）。在自定义高协作设置下，本文方法显著提升了TSR（例如，将VillagerAgent的TSR从22.04%提升至34.56%），并大幅降低了CS（例如，将VillagerAgent的CS从145步减少到92步），表明其在保持高成功率的同时减少了执行冗余。
2.  **协调效率机制指标**：本地解决率（LRR）、不必要升级率（UER）、有效通信率（ECR）和恢复成功率（RSR）。实验结果显示，本文方法将LRR从基线约40%大幅提升至73.2%-89.7%，将UER从超过60%降低至约11%-17%，并将ECR提升40-50个百分点（例如在MindCraft自定义设置下从46.2%提升至81.3%），证明了门控机制能有效过滤不必要通信、提升本地自治与协作效用。

此外，消融实验验证了分区信息架构和多层级门控策略各自的贡献。移除分区架构会导致消息数激增和TSR下降；而逐步引入规则层、成本评分层和LLM裁决器的门控机制，能持续优化性能，完整模型在TSR（32.8%）和通信开销（消息数11条）上达到最佳平衡。

### Q5: 有什么可以进一步探索的点？

该论文在提升多智能体协作效率方面提出了创新架构，但其设计仍存在一些局限性和值得深入探索的方向。首先，系统对“节点关键性”和“局部恢复成本”的评估依赖于预设的静态规则或学习到的固定模式，在高度动态、未知的开放世界中可能适应性不足。未来可探索引入元学习或在线适应机制，使智能体能够根据实时交互经验动态调整通信阈值和评估策略。

其次，架构中的“分区信息状态”假设了公私状态的清晰可分性，但在复杂任务中，局部决策的长期影响可能难以即刻评估，导致本应提前协调的信息被延迟。一个改进思路是设计一种轻量的、前瞻性的影响预测模型，使智能体能在执行早期预估潜在的区域间依赖，从而更智能地触发预防性协调。

此外，实验集中于《我的世界》中的建造任务，其状态空间和异常类型相对结构化。未来需在更复杂、对抗性或目标冲突的多智能体场景（如战略游戏、现实机器人集群）中验证方法的泛化能力。最后，当前工作主要优化了通信效率与任务完成度，未来可进一步将能源消耗、计算资源均衡等实际约束纳入“成本敏感”决策框架，推动其向更实用的多智能体系统发展。

### Q6: 总结一下论文的主要内容

本文针对开放世界多智能体系统中因默认触发通信导致的协调噪声、执行中断和通信滥用问题，提出了一种分区信息架构与门控协调机制。核心贡献在于将智能体的私有执行状态与公共协调状态显式分离，并引入基于成本效益评估的门控升级机制，使通信从默认反应转变为选择性决策。

具体方法上，首先设计了一个基于系统验证结果的事件触发工作记忆，用于维护紧凑、低噪声的本地状态表示。其次，提出成本敏感的门控升级机制，通过联合评估节点关键性、本地恢复成本和下游任务影响，来决定是否发起跨区域通信。这样既保障了本地执行的稳定性，又确保了公共通信的必要性与高效性。

实验在《我的世界》长期建造任务中进行，结果表明，相较于基于强通信和规划结构的基线模型，该方法在蓝图完成质量和执行链长度方面表现更优，同时提升了本地自我恢复能力，减少了无效升级，并提高了公共通信的效用。该研究为长视距开放世界中的高效多智能体协作提供了一种新范式。
