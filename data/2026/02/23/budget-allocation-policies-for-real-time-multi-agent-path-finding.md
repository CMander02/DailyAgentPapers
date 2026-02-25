---
title: "Budget Allocation Policies for Real-Time Multi-Agent Path Finding"
authors:
  - "Raz Beck"
  - "Roni Stern"
date: "2025-07-22"
arxiv_id: "2507.16874"
arxiv_url: "https://arxiv.org/abs/2507.16874"
pdf_url: "https://arxiv.org/pdf/2507.16874v2"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.RO"
tags:
  - "多智能体系统"
  - "实时路径规划"
  - "预算分配"
  - "机器人学"
  - "决策算法"
relevance_score: 7.5
---

# Budget Allocation Policies for Real-Time Multi-Agent Path Finding

## 原始摘要

Multi-Agent Path finding (MAPF) is the problem of finding paths for a set of agents such that each agent reaches its desired destination while avoiding collisions with the other agents. This problem arises in many robotics applications, such as automated warehouses and swarms of drones. Many MAPF solvers are designed to run offline, that is, first generate paths for all agents and then execute them. In real-world scenarios, waiting for a complete solution before allowing any robot to move is often impractical. Real-time MAPF (RT-MAPF) captures this setting by assuming that agents must begin execution after a fixed planning period, referred to as the planning budget, and execute a fixed number of actions, referred to as the execution window. This results in an iterative process in which a short plan is executed, while the next execution window is planned concurrently. Existing solutions to RT-MAPF iteratively call windowed versions of MAPF algorithms in every planning period, without explicitly considering the size of the planning budget. We address this gap and explore different policies for allocating the planning budget in windowed versions of MAPF-LNS2, a state-of-the-art MAPF algorithm. Our exploration shows that the baseline approach in which all agents draw from a shared planning budget pool is ineffective in challenging scenarios. Instead, policies that intelligently distribute the planning budget among agents are able to solve more problem instances in less time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决实时多智能体路径规划（RT-MAPF）中规划预算分配的核心问题。研究背景在于，传统MAPF算法通常离线运行，先为所有智能体生成完整路径再执行，但在实际应用（如自动化仓库、无人机集群）中，机器人往往无法等待完整规划完成，必须边规划边执行。RT-MAPF通过引入固定规划预算和执行窗口来模拟这一场景，形成迭代式的规划-执行循环。

现有方法（如窗口式规划）通常在每个规划周期调用MAPF算法的窗口版本，但忽略了规划预算的显式考量。这些方法在规划预算耗尽时可能无法返回可行解，且普遍采用共享预算池的基线策略，导致在复杂场景中效率低下——智能体可能争夺有限资源，而关键冲突未获足够预算解决。

本文的核心问题是：如何在有限规划预算下，设计能显式考虑预算分配的RT-MAPF算法，以提升解的质量和求解效率。为此，论文提出基于先进MAPF算法MAPF-LNS2的预算感知框架，并重点探索多种智能预算分配策略（BAP），例如根据冲突程度调整预算、借鉴PID控制器或多臂老虎机方法，以动态优化预算在智能体间的分配，从而在挑战性场景中解决更多问题实例。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕实时多智能体路径规划（RT-MAPF）及其基础算法展开，可分为以下几类：

**1. 经典MAPF算法与窗口化求解器：**
论文重点参考了两种快速次优MAPF算法：优先级继承回溯（PIBT）和基于大邻域搜索的MAPF-LNS2。PIBT通过迭代分配优先级为智能体选择下一步动作，速度极快；MAPF-LNS2则通过初始规划和邻域搜索两阶段优化路径。在实时场景中，现有RT-MAPF解决方案（如滚动视野冲突消解RHCR框架）通常迭代调用这些算法的“窗口化”版本，即在每个规划周期内仅规划有限步长（执行窗口）的路径，但未显式考虑规划预算的分配策略。本文正是在此基础上，专门研究如何在窗口化MAPF-LNS2中智能分配规划预算。

**2. 在线与终身MAPF（LMAPF）：**
终身MAPF（LMAPF）作为在线MAPF的一种，关注智能体持续接收新任务的情景，在多智能体取送（MAPD）等应用中备受关注。RHCR是解决LMAPF的常用框架，其交替进行规划与执行，并依赖窗口化MAPF算法在有限视野内寻找无冲突路径。本文的RT-MAPF设定与LMAPF有相似之处，但更强调固定规划预算下的实时决策，而非任务动态到达。

**3. 实时启发式搜索（RTHS）及其多智能体扩展：**
实时单智能体搜索要求智能体在恒定规划预算内决定动作，常采用RTHS算法，其通过局部前瞻搜索、启发式更新与动作执行交替进行。近期研究尝试将RTHS适配到多智能体场景：例如，有工作提出边界多智能体A*（BMAA*），让每个智能体独立运行RTHS并将其他智能体视为动态障碍；另一些研究如WinC-MAPF框架，则在所有智能体的联合配置空间上运行RTHS，并通过限制规划视野和使用窗口化MAPF算法来维持计算可行性。本文与这些工作的区别在于，不直接采用RTHS的搜索范式，而是专注于改进现有窗口化MAPF算法内部的预算分配策略，以提升在挑战性场景中的求解效率。

### Q3: 论文如何解决这个问题？

论文通过提出并评估多种预算分配策略来解决实时多智能体路径规划中规划预算分配不当的问题。其核心方法是，在基于窗口的MAPF-LNS2算法框架内，引入一个灵活的预算分配框架，并设计多种智能的邻域预算分配策略，以替代将所有预算一次性投入单个邻域的基线方法。

整体框架是一个迭代式的实时规划-执行循环。在每个规划周期内，算法并行运行PIBT和LNS2来生成初始路径，选择其中使最远智能体距离目标最近的方案。随后，核心的“LNS2_Improve”函数被调用，在严格的全局预算约束下，通过迭代选择邻域、分配预算、为邻域内智能体重新规划来改进局部解。任何未使用的局部预算会被回收至全局池。如果全局预算仍有剩余，则调用LNS1进行进一步优化。生成的局部路径被执行后，流程对下一个时间窗口重复。

主要模块与关键技术包括：
1.  **预算分配框架**：这是核心架构创新。它将固定的总规划预算（B）作为一个可动态管理的全局资源（B_rem）。每次为一个选定的智能体邻域（N）规划时，会咨询**预算分配策略**来为该邻域分配一个预算上限（B_N），并从全局预算中扣除。邻域内智能体通过SIPPS算法进行顺序重规划，按搜索节点扩展数消耗B_N。规划完成后，剩余的B_N会返还给全局池。
2.  **多种创新的预算分配策略**：这是论文的主要贡献。论文提出了四种策略来智能决定B_N：
    *   **冲突比例预算**：根据邻域内智能体卷入的冲突总数占总冲突数的比例来分配预算，并设有一个基于邻域大小和执行窗口的下限，确保基础搜索需求。
    *   **反向冲突比例预算**：为冲突较少的智能体分配更多预算，旨在先为简单智能体快速找到可行路径，从而简化剩余问题的搜索空间。
    *   **PID控制器启发策略**：将控制论中的PID思想引入，根据智能体的冲突数、冲突变化量以及被选中规划的历史次数，计算出一个绝对预算值，动态响应系统状态。
    *   **多臂赌博机在线学习策略**：将前三种策略作为“臂”，通过在线学习根据其历史改进效果动态调整选择概率，实现自适应的策略选择。

创新点在于首次在实时MAPF中系统性地研究了规划预算的分配问题，并证明了智能分配策略相对于共享池基线方法的优越性。通过将预算管理与邻域选择、冲突分析相结合，这些策略能够更有效地利用有限的计算资源，优先解决关键瓶颈（如反向冲突比例策略所示），从而在具有挑战性的场景中解决更多问题实例。

### Q4: 论文做了哪些实验？

实验在标准MAPF基准的不同网格地图上进行，包括Room（32x32-4）、Random（32x32-10）和Maze（32x32-4），分别对应120、300和27个智能体。实验设置基于实时MAPF框架，采用滚动时域控制（RHCR）模式，规划预算（budget）和行动窗口（execution window）是关键变量。预算范围设为[5,10,15,20,25,50,80,100,150,200,250,300,350,400]，行动窗口范围设为[5,10,15,20,25,30,35]。对比方法包括：作为快速初始解的PIBT基线、共享预算池的Shared基线，以及四种智能预算分配策略——PID、CPB、RCPB和MAB。此外，还引入了两种理论上限：SPO（为每个参数组合选择最高成功率策略）和Oracle（为每个具体场景选择最佳策略）。

主要结果以成功率和解决方案质量（AUC）衡量。成功率方面，没有单一策略在所有地图上始终最优。例如，在Room地图上，CPB在52%的参数配置中表现最佳；在Random地图上，MAB达到54%；在Maze地图上，CPB达到71%。SPO相比基线策略普遍具有优势，例如在Room地图上，Shared策略相对于SPO的最大性能差距为[0.72, 0.36]，而PIBT为[0.92, 0.44]。AUC指标进一步评估了解决方案质量，SPO在多数情况下优于基线，但并非总是最优，因为其选择依据是成功率而非AUC。例如，在Room地图中，当行动窗口为5、预算为15时，SPO的AUC相对于最佳基线的比值为1.09，表明其性能更优；但在某些配置下（如行动窗口15、预算250），比值可低至0.94，显示基线可能找到更高质量的路径。关键数据包括：成功率归一化表格中，SPO值常为1，而基线值常低于1（如Room地图中PIBT在预算200、窗口35时仅0.61）；AUC比较表中，SPO与最佳基线的比值在0.84至1.21之间波动，印证了策略性能对参数敏感。总体而言，实验表明智能预算分配策略（尤其是CPB和MAB）在复杂场景中能提升求解成功率，但最优策略高度依赖于地图类型和资源约束。

### Q5: 有什么可以进一步探索的点？

该论文主要探讨了实时多智能体路径规划（RT-MAPF）中的预算分配策略，但仍存在一些局限性和可进一步探索的方向。首先，研究主要基于MAPF-LNS2算法进行窗口化扩展，未来可测试更多类型的MAPF求解器（如基于冲突的搜索CBS或强化学习方法）在不同预算分配策略下的表现，以验证策略的通用性。其次，当前预算分配策略虽能提升求解成功率，但未充分考虑动态环境中的不确定性（如智能体故障、环境突变），未来可引入自适应机制，使预算能根据实时冲突密度或任务紧急度动态调整。此外，论文未深入分析多轮迭代中预算分配的长期影响，可探索基于强化学习的元策略，让系统在运行中学习最优预算分配模式。最后，实际应用中计算资源常受限制，未来工作可结合硬件约束（如分布式计算、边缘设备）设计轻量级预算调度方案，进一步提升系统在真实场景中的可扩展性与鲁棒性。

### Q6: 总结一下论文的主要内容

本文针对实时多智能体路径规划（RT-MAPF）中的规划预算分配问题展开研究。RT-MAPF要求智能体在固定规划预算（时间）内完成局部路径规划，并执行固定步数的动作，形成“规划-执行”交替的迭代过程。现有方法通常在每轮规划中调用窗口式MAPF算法，但未显式考虑规划预算的分配策略，导致在复杂场景中效率低下。

论文的核心贡献是提出并系统比较了多种规划预算分配策略。作者基于前沿算法MAPF-LNS2，设计了不同的预算分配机制，包括传统的共享预算池方法以及更智能的按需分配策略。实验表明，在挑战性场景中，简单均分预算的方法效果较差，而能智能区分智能体优先级、动态调整预算分配的策略可以显著提升求解成功率并减少总体求解时间。

这项工作的意义在于首次深入探讨了RT-MAPF中预算分配的关键作用，为实时多机器人系统的在线协调优化提供了新的思路和有效方法。
