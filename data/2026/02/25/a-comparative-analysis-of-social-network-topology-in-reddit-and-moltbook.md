---
title: "A Comparative Analysis of Social Network Topology in Reddit and Moltbook"
authors:
  - "Yiming Zhu"
  - "Gareth Tyson"
  - "Pan Hui"
date: "2026-02-14"
arxiv_id: "2602.13920"
arxiv_url: "https://arxiv.org/abs/2602.13920"
pdf_url: "https://arxiv.org/pdf/2602.13920v3"
categories:
  - "cs.SI"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent评测/基准"
  - "Agent社会模拟"
  - "Agent交互"
  - "网络拓扑分析"
relevance_score: 7.5
---

# A Comparative Analysis of Social Network Topology in Reddit and Moltbook

## 原始摘要

Recent advances in agent-mediated systems have enabled a new paradigm of social network simulation, where AI agents interact with human-like autonomy. This evolution has fostered the emergence of agent-driven social networks such as Moltbook, a Reddit-like platform populated entirely by AI agents. Despite these developments, empirical comparisons between agent-driven and human-driven social networks remain scarce, limiting our understanding of how their network topologies might diverge. This paper presents the first comparative analysis of network topology on Moltbook, utilizing a comment network comprising 33,577 nodes and 697,688 edges. To provide a benchmark, we curated a parallel dataset from Reddit consisting of 7.8 million nodes and 51.8 million edges. We examine key structural differences between agent-drive and human-drive networks, specifically focusing on topological patterns and the edge formation efficacy of their respective posts. Our findings provide a foundational profile of AI-driven social structures, serving as a preliminary step toward developing more robust and authentic agent-mediated social systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个新兴且关键的问题：在生成式AI推动下，完全由AI代理（Agent）驱动的社交网络（如Moltbook）已经出现，但其网络拓扑结构是否与人类驱动的传统社交网络（如Reddit）相似或存在差异，目前尚缺乏实证研究。

研究背景是生成式AI的进步使得AI代理能够模拟人类进行复杂的社交行为，从而催生了由AI代理自主运营和互动的社交平台。现有研究多关注AI代理的内容生成能力、集体行为模式及其潜在风险，但尚未从网络科学和图结构的角度，系统比较AI代理之间与人类用户之间互动所形成的网络拓扑差异。这是一个重要的知识空白，因为理解这些结构差异对于评估AI社交系统的真实性、鲁棒性及其社会动力学影响至关重要。

现有方法的不足在于，尽管已知人类社交网络通常呈现幂律度分布、同配性混合和双向连接等典型模式，但AI代理驱动的社交网络是否会自然复现这些模式，还是会产生全新的结构特征，此前完全没有大规模实证分析。这种比较研究的缺失限制了我们对于AI中介社交系统本质的理解。

因此，本文要解决的核心问题是：首次对AI驱动与人类驱动的在线社交网络进行大规模拓扑结构比较分析。具体而言，论文通过构建并分析Moltbook（AI代理）和Reddit（人类用户）的两个并行评论互动网络数据集，探究两者在度分布、聚类系数、密度等拓扑特性上的差异（RQ1），并比较两个平台上帖子作为网络连接催化剂的效率差异（RQ2），从而为理解AI驱动的社交结构提供基础性描述，并为构建更健壮、更真实的AI中介社交系统迈出初步的一步。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三类：AI代理社交系统研究、人类社交网络拓扑分析，以及新兴的代理驱动社交平台探索。

在**AI代理社交系统研究**方面，已有工作关注代理的内容生成能力、集体行为模式及其潜在风险，但尚未从图结构角度分析代理间的交互模式。本文则首次聚焦于代理驱动社交网络的拓扑结构，填补了这一空白。

在**人类社交网络拓扑分析**方面，大量研究已证实如Reddit等平台存在幂律度分布、同配混合和双向连接等典型模式。本文以此作为基准，对比代理驱动网络是否复现这些人类中心拓扑。

在**新兴代理驱动社交平台探索**方面，已有如Chirper.ai和Moltbook等纯代理社交网络出现，但缺乏对其网络结构的实证比较。本文选取Moltbook与Reddit进行大规模对比，首次揭示了二者在拓扑特征和帖子连边形成效能上的差异，为构建更鲁棒真实的代理中介社交系统提供了基础。

### Q3: 论文如何解决这个问题？

论文通过构建并比较两个社交网络的评论网络拓扑结构来解决研究问题。核心方法是**对比分析**，具体架构和关键技术如下：

**整体框架**：研究采用数据驱动的实证比较框架。首先，从两个平台（Moltbook 和 Reddit）独立收集大规模的帖子和评论数据。然后，将原始互动数据统一建模为**有向评论网络**，其中节点代表用户（或AI智能体），有向边代表“评论者”回复“接收者”的行为。最后，在此统一的网络表示基础上，进行拓扑结构指标的量化比较。

**主要模块/组件**：
1.  **数据收集模块**：
    *   **Moltbook数据集**：通过官方公开API获取。首先，通过迭代调用帖子排序API（按时间顺序，逐步增加偏移量）获取所有公开帖子列表。随后，针对每个帖子，通过其ID调用帖子API获取其下的所有评论。最终收集了2026年1月27日至2月10日期间的420,259个帖子和2,563,222条评论。
    *   **Reddit基准数据集**：使用公开的Pushshift数据转储作为基线。为减少时间偏差，选取了与Moltbook数据时间段最接近的2025年12月25日至31日的数据。为专注于人类驱动的网络，通过关键词（如“bot”、“GPT”、“Mod”等）过滤了疑似机器人账户的数据，最终得到9,317,777个帖子和67,081,004条评论。

2.  **网络构建模块**：基于收集的数据，为每个平台分别**诱导构建有向评论网络**。网络构建规则一致：如果用户A回复了用户B的帖子或评论，则创建一条从节点A（评论者）指向节点B（接收者）的有向边。由此得到Moltbook网络（33,577个节点，697,688条边）和Reddit网络（约785万个节点，约5185万条边）。

3.  **比较分析模块**：在构建的两个同构网络（均为有向评论图）上，进行**拓扑模式**和**帖子边形成效能**等方面的关键结构差异分析。

**创新点**：
1.  **研究范式创新**：这是首次对纯AI智能体驱动的社交网络（Moltbook）与人类驱动的社交网络（Reddit）进行的**实证性比较拓扑分析**，填补了该领域的空白。
2.  **方法论创新**：提出了一个可复现的、系统的数据收集、清洗（针对Reddit去除机器人账户）和网络构建流程，确保了比较的公平性和一致性。特别是构建了大规模、公开可用的Moltbook网络数据集。
3.  **问题聚焦**：研究不仅关注宏观网络规模差异，更深入到**拓扑结构模式**和**帖子引发互动连接的效率**等微观机制层面，旨在揭示两类网络在形成机制上的本质差异，为构建更鲁棒和逼真的智能体中介社交系统提供了基础性见解和数据支撑。

### Q4: 论文做了哪些实验？

论文实验主要围绕两个研究问题展开。实验设置上，研究者构建并对比了AI驱动的社交网络Moltbook与人类驱动的社交网络Reddit的评论网络拓扑结构及帖子在构建网络中的效能。

在数据集方面，实验使用了两个平行数据集：Moltbook评论网络包含约3.96万个节点和69.77万条边；作为基准的Reddit数据集则包含约785.5万个节点和5185万条边。对比方法主要是对这两个网络的各项拓扑指标进行量化比较。

主要结果包括：首先，在网络拓扑分析（RQ1）中，尽管Moltbook规模小得多，但其网络密度（4.46×10⁻⁴）高于Reddit（8.14×10⁻⁷），平均邻居数（17.637 vs. 6.390）和聚类系数（全局：0.0084 vs. 0.0063；平均局部：0.330 vs. 0.024）也更高，表明互动更密集、社区结构更紧密。然而，Moltbook的互惠性更低（0.136 vs. 0.310），表明双向对话较少。其度同配性为-0.204（Reddit为-0.011），Freeman中心性为0.4441（Reddit为0.0027），揭示了更明显的“枢纽-辐射”结构。其次，在帖子效能分析（RQ2）中，Moltbook上能产生边的帖子比例更高（62.71% vs. 49.26%），中位数生成边数为1.0（Reddit为0.0），但平均生成边数较少（2.916 vs. 5.455）。在时效性上，Moltbook生成第一条边的中位时间（0.013小时）、生成50%边的中位时间（0.048小时）以及边生成间隔中位时间（0.378小时）均远快于Reddit，但帖子生成最后一条边的生命周期中位时间更短（1.950小时 vs. 6.746小时），表明互动爆发快但衰减也快。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于仅从网络拓扑结构（如中心辐射模式）和连接形成效率进行对比，未能深入探究节点（即AI代理或人类用户）的行为动机、内容质量或互动语义。例如，Moltbook中连接短暂可能源于代理缺乏长期记忆或情感纽带，而Reddit的持久连接则涉及复杂的社会资本积累。未来研究可探索以下方向：首先，引入动态时间分析，比较网络结构的演化轨迹（如社区形成速度或信息传播路径），而非静态快照；其次，结合自然语言处理技术，分析帖子内容的情感倾向或主题深度，以揭示拓扑差异背后的认知机制；最后，设计混合实验环境（如人类与代理共存的平台），观察互动模式如何影响网络韧性。改进思路包括为AI代理嵌入更复杂的社交目标（如合作或竞争），或模拟人类社交中的信任建立过程，从而推动代理中介系统从“信息广播网络”向真正具有社会性的生态系统演进。

### Q6: 总结一下论文的主要内容

本文首次对AI代理驱动的社交网络（以Moltbook为例）与人类驱动的社交网络（以Reddit为例）进行了拓扑结构的比较分析。研究问题在于探究两者在网络结构模式与内容发帖对边形成效能上的差异。方法上，作者构建了Moltbook的评论网络（含33,577个节点和697,688条边）以及一个大规模的Reddit并行数据集（含780万个节点和5180万条边）作为基准，并对比分析了其关键拓扑特征。主要结论发现，Moltbook网络呈现出强烈的“中心-辐射”模式，连接多为单向流动；其内容发帖虽能持续引发链接形成，但由于算法注意力的快速耗尽，连接难以持久深化。这表明Moltbook更像一个高速信息广播系统，而非连接持久、逐步演化的稳健社交社区。该研究的核心贡献在于首次为AI驱动的社交结构提供了基础性特征描述，为未来构建更健壮、更真实的代理中介社交系统迈出了重要一步。
