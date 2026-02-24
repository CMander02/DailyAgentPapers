---
title: "To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation"
authors:
  - "Apoorva Vashisth"
  - "Manav Kulshrestha"
  - "Pranav Bakshi"
  - "Damon Conover"
  - "Guillaume Sartoretti"
  - "Aniket Bera"
date: "2026-02-23"
arxiv_id: "2602.20055"
arxiv_url: "https://arxiv.org/abs/2602.20055"
pdf_url: "https://arxiv.org/pdf/2602.20055v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.CV"
tags:
  - "Agent 架构"
  - "规划"
  - "工具使用"
  - "具身智能"
  - "场景理解"
  - "主动感知"
  - "LLM 驱动"
relevance_score: 8.5
---

# To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation

## 原始摘要

Visual navigation typically assumes the existence of at least one obstacle-free path between start and goal, which must be discovered/planned by the robot. However, in real-world scenarios, such as home environments and warehouses, clutter can block all routes. Targeted at such cases, we introduce the Lifelong Interactive Navigation problem, where a mobile robot with manipulation abilities can move clutter to forge its own path to complete sequential object- placement tasks - each involving placing an given object (eg. Alarm clock, Pillow) onto a target object (eg. Dining table, Desk, Bed). To address this lifelong setting - where effects of environment changes accumulate and have long-term effects - we propose an LLM-driven, constraint-based planning framework with active perception. Our framework allows the LLM to reason over a structured scene graph of discovered objects and obstacles, deciding which object to move, where to place it, and where to look next to discover task-relevant information. This coupling of reasoning and active perception allows the agent to explore the regions expected to contribute to task completion rather than exhaustively mapping the environment. A standard motion planner then executes the corresponding navigate-pick-place, or detour sequence, ensuring reliable low-level control. Evaluated in physics-enabled ProcTHOR-10k simulator, our approach outperforms non-learning and learning-based baselines. We further demonstrate our approach qualitatively on real-world hardware.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统视觉导航系统在现实复杂环境中因杂物阻塞所有路径而失效的问题。传统方法通常假设起点与目标之间存在至少一条无障碍路径，但在家庭、仓库等实际场景中，杂物可能完全堵塞路线。为此，论文提出了“终身交互式导航”这一新问题，要求具备操作能力的移动机器人能够通过移动杂物来为自己开辟路径，以完成一系列顺序出现的物体放置任务（如将闹钟放到餐桌上）。  

论文的核心挑战在于，这是一个终身学习设置：环境变化的影响会累积并产生长期效应，机器人必须在未知环境中连续执行任务，且每个决策（如是否移动某个障碍物）都会对未来任务产生持久影响。现有方法要么无法处理此类序列任务，要么假设环境完全可观测，缺乏在部分可观测下进行感知与规划耦合的长期推理能力。  

为此，论文提出了一种基于大语言模型的约束规划框架，将LLM的角色从生成低级动作序列转变为在结构化场景图上进行约束推理，决定移动哪些物体、将其放置何处以及接下来应探索哪些区域以获取任务相关信息。这种方法将规划问题转化为约束求解，使LLM能够进行零样本的长期战略决策，而无需针对特定任务进行微调。

### Q2: 有哪些相关研究？

相关研究主要分为两大方向。首先是**具身与视觉导航**，代表性工作包括基于认知地图与规划的早期方法（如Cognitive Mapping and Planning）、以及一系列仿真平台与基准（如AI2-THOR、Habitat、ProcTHOR）。后续研究通过生成模型、记忆机制和结构化场景推理（如NaviDiffusor、MemoNav、SceneGC）提升了探索与表征能力，并拓展到语言驱动、多目标导航等任务（如CoWs on Pastures、Multi-Object Navigation）。然而，这些方法均假设环境是静态且最终可通行的，一旦所有路径被杂物阻塞，智能体只能绕行或失败。

其次是**交互式导航与可移动障碍物导航**。经典的可移动障碍物导航方法在机器人运动与障碍物配置的联合空间中进行搜索，但通常假设完全知晓几何与动力学信息、障碍物数量少、规划视野短，且仅针对单一目标优化。近期交互式导航工作（如Interactive Gibson、InterNav、CaMP）将此类问题引入具身环境，学习基于视觉输入移动障碍物；而Interactive-FAR、IN-Sight、ADIN等系统则探索了启发式方法、功能可供性或不确定性感知查询。

本文与这些工作的关系在于：**一方面，它突破了传统视觉导航对静态可通行环境的假设，直面完全阻塞的场景；另一方面，它超越了现有交互式导航仅关注短期、反应式障碍移除的局限，引入了终身、序列化的任务设定，要求智能体考虑环境改变的长期影响，并进行主动感知与约束推理，以实现持久的环境重构。**

### Q3: 论文如何解决这个问题？

该论文通过一个基于约束的规划框架来解决终身交互式导航问题，其核心是将大语言模型（LLM）作为高层约束推理器，并与低层运动规划器解耦。框架首先通过感知模块增量构建并维护一个结构化的场景图，该图以节点表示已发现的对象或房间，以边编码对象间的阻塞关系。每个节点还附加了关键属性，如到达成本、阻塞对象列表、所在网格节点的中介中心性（衡量其对全局连通性的影响）以及替代路径成本，为决策提供几何与拓扑上下文。

LLM 的核心作用是基于场景图的文本化描述，进行成本效益分析，以决定下一步高层动作：是移动障碍物、绕行还是主动探索。具体而言，对于每个候选障碍物，系统计算一个移除成本，该成本综合了导航至物体的时间、操纵物体所需的时间（如抓取放置）以及将其移至可行放置区的导航时间。同时，LLM 会权衡移除该障碍物所带来的连通性收益（通过中介中心性量化）。这近似于一个优化问题：选择能使“移除成本减去连通性收益”最小化的障碍物-放置区对。当没有障碍物提供足够收益时，规划器会优先检查是否存在无需操纵的绕行路径；若不存在，则尝试移动最少障碍物以恢复连通性；若目标物体尚未发现，则根据任务语义引导探索最可能包含相关物体的房间。

这种设计使得 LLM 无需生成具体的机器人低级动作序列，而是专注于解决“改变世界中的哪些约束”这一战略问题，例如决定移动哪个物体、放置何处以及下一步探索哪里。最后，由标准的基于 Dijkstra 的低层运动规划器可靠地执行具体的导航、抓取和放置动作序列，从而在未知、杂乱的环境中实现终身、零样本泛化的交互式导航能力。

### Q4: 论文做了哪些实验？

论文在ProcTHOR-10k模拟器中构建了一个包含杂乱障碍物的室内导航数据集，包含1万条episode，并按房间复杂度（1-3、4-6、7-10间）分组测试。评估指标包括任务成功率（SR）、耗时步数（TS）、环境杂乱代价（PoC）以及综合长期效率分数（LES）。

实验首先与多个基线比较：学习模型InterNav、纯绕行策略（Always Detour）、纯交互策略（Always Interact）以及先清理再执行策略（Clean + S/P）。结果表明，在复杂场景（4-10个房间）中，本文提出的约束规划方法（Ours (known/unk)）在综合指标LES上表现最佳，尤其在平衡任务成功、时间效率和长期环境维护方面优于基线。纯交互策略虽SR高，但TS过长；纯绕行策略TS短，但SR和PoC差。

此外，论文进行了消融实验：1）改变操作代价系数（e=1,5,10,15,20），分析其对成功率、路径长度等的影响；2）改变历史上下文长度（h=1,3,6,9），考察规划器利用历史信息的能力；3）比较不同大语言模型（Gemini, GPT-5, Deepseek）作为推理核心的性能，发现GPT-5在较小场景表现较好，而Gemini在复杂场景中LES更优；4）测试不同障碍物密度下的鲁棒性。这些实验验证了方法各组件的作用及其在不同条件下的稳定性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于：1）依赖预构建的场景图，在动态或高度混乱环境中可能无法实时更新；2）约束推理基于静态成本效益抽象，缺乏对意外干扰（如物体滑动、新障碍出现）的适应性；3）实验主要在模拟环境中进行，真实世界的物理交互复杂性（如抓取稳定性、物体材质影响）尚未充分验证。  
未来方向可探索：1）集成在线场景图更新机制，结合实时感知数据动态修正约束；2）引入强化学习或世界模型，让智能体通过交互学习调整成本估计策略；3）扩展多智能体协作场景，研究分布式约束解决与任务分配；4）开发更细粒度的物理推理模块，提升对复杂操纵任务（如堆叠、推拉）的泛化能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了“终身交互式导航”新问题，解决传统视觉导航中因杂物堵塞而无可行路径的挑战。其核心贡献是设计了一个基于约束规划的LLM驱动框架，使机器人能主动移动障碍物、开辟路径以完成顺序物体放置任务。该框架的关键在于让大语言模型基于结构化场景图进行推理，动态决策移动哪个物体、放置何处以及下一步探查哪里，从而将高层任务规划与主动感知耦合，避免低效的全环境探索。论文在ProcTHOR-10k物理仿真器中验证了方法的优越性，并展示了在真实硬件上的应用潜力，为零样本泛化的具身智能导航提供了新思路。
