---
title: "Lifted Forward Planning in Relational Factored Markov Decision Processes with Concurrent Actions"
authors:
  - "Florian Andreas Marwitz"
  - "Tanya Braun"
  - "Ralf Möller"
  - "Marcel Gehrke"
date: "2025-05-28"
arxiv_id: "2505.22147"
arxiv_url: "https://arxiv.org/abs/2505.22147"
pdf_url: "https://arxiv.org/pdf/2505.22147v3"
categories:
  - "cs.AI"
tags:
  - "规划"
  - "马尔可夫决策过程"
  - "并发动作"
  - "关系表示"
  - "前向规划"
  - "可扩展性"
  - "近似算法"
relevance_score: 5.5
---

# Lifted Forward Planning in Relational Factored Markov Decision Processes with Concurrent Actions

## 原始摘要

When allowing concurrent actions in Markov Decision Processes, whose state and action spaces grow exponentially in the number of objects, computing a policy becomes highly inefficient, as it requires enumerating the joint of the two spaces. For the case of indistinguishable objects, we present a first-order representation to tackle the exponential blow-up in the action and state spaces. We propose Foreplan, an efficient relational forward planner, which uses the first-order representation allowing to compute policies in space and time polynomially in the number of objects. Thus, Foreplan significantly increases the number of planning problems solvable in an exact manner in reasonable time, which we underscore with a theoretical analysis. To speed up computations even further, we also introduce an approximate version of Foreplan, including guarantees on the error. Further, we provide an empirical evaluation of both Foreplan versions, demonstrating a speedup of several orders of magnitude. For the approximate version of Foreplan, we also empirically show that the induced error is often negligible.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在具有大量不可区分对象的马尔可夫决策过程（MDP）中，尤其是在允许并发动作的情况下，进行精确规划时面临的计算爆炸问题。研究背景是，在现实世界问题（如流行病控制中为市民实施旅行禁令）中，状态和动作空间会随着对象数量的增加呈指数级增长，因为需要枚举所有可能的状态-动作组合。现有方法，如命题层面的MDP或因子化MDP（fMDP），虽然通过因子化过渡函数部分缓解了问题，但在处理并发动作时，仍需枚举动作空间的所有可能组合，导致计算效率低下，难以扩展到大规模问题。现有的一些方法，如状态聚类或基于互模拟的等价状态分组，也未能高效处理并发动作。本文要解决的核心问题是：如何利用对象之间的不可区分性（例如，行为相同的市民群体），通过一种一阶关系表示方法，将状态和动作空间的规模从对象数量的指数级降低为多项式级，从而设计出能够高效处理并发动作的精确规划算法，并进一步提供具有误差保证的近似版本以加速计算。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕马尔可夫决策过程（MDP）的表示和规划方法展开，可分为以下几类：

**1. 经典MDP与因子化MDP（fMDP）研究：**
传统MDP及其因子化变体（fMDP）是本文工作的基础。fMDP通过状态变量分解状态空间和转移函数，以应对状态空间随对象数量指数增长的问题。然而，当允许并发动作时，动作和状态空间的联合枚举仍会导致计算爆炸。本文提出的关系因子化MDP（rfMDP）和Foreplan规划器，正是在fMDP框架下，针对**并发动作**和**对象不可区分**这一特定场景进行的扩展与优化。

**2. 关系与提升（Lifting）表示方法研究：**
为处理大量不可区分对象，本文借鉴了概率图模型中“提升”（lifting）的思想，使用参数化随机变量（PRV）和参数化因子（parfactor）来紧凑地表示状态和转移模型。这类方法源于统计关系学习领域，旨在通过参数化表示避免对大量不可区分变量进行冗余计算。本文的创新点在于将这种关系表示首次应用于**支持并发动作**的MDP规划中，从而在表示层面直接解决了动作空间和状态空间的指数爆炸问题。

**3. 精确与近似规划算法研究：**
在规划算法层面，相关工作包括基于线性规划求解Bellman方程的价值迭代类方法。本文的Foreplan是一种**关系前向规划器**，其核心贡献在于证明了在该表示下，规划所需的时间和空间复杂度可**关于对象数量呈多项式级**，这显著提升了可精确求解的问题规模。此外，本文还提出了Foreplan的近似版本并提供了误差界保证，这属于在效率与最优性之间进行权衡的近似规划方法范畴，与各类启发式或近似动态规划研究有相似目标，但实现手段基于其特定的关系提升表示。

综上，本文工作与经典fMDP、关系提升表示及MDP规划算法这三条研究主线紧密相关。其区别与核心贡献在于，首次将提升表示与支持并发动作的fMDP相结合，并设计了在此表示下具有多项式复杂度保证的高效精确与近似规划算法。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为Foreplan的高效关系前向规划器来解决并发动作下MDP状态和动作空间指数级爆炸的问题。其核心方法是利用一阶表示（first-order representation）来紧凑地表示状态和动作，从而将计算复杂度降低到对象数量的多项式级别。

整体框架基于关系因子化MDP（rfMDP），输入为rfMDP，输出为价值函数及由此导出的策略。Foreplan首先通过紧凑状态表示来利用对象的不可区分性，然后基于该表示运行线性规划计算价值函数。架构设计主要包括两个关键部分：依赖识别与状态表示、以及基于线性规划的价值函数计算。

主要模块/组件包括：
1. **关系成本图（Relational Cost Graph）**：用于识别PRV之间的依赖关系。图中的顶点代表当前状态的每个PRV，边连接共享逻辑变量且在同一个参数因子或局部奖励函数中共同出现的PRV。图中的最大团对应需要联合计数的PRV集合。
2. **扩展计数随机变量（Extended Counting Random Variable, CRV）**：用于紧凑表示状态。每个CRV对应关系成本图中的一个团，通过直方图统计该团中PRV所有可能真值赋值的出现次数，从而避免枚举具体对象。
3. **状态表示**：将状态定义为每个团对应的CRV（或单变量RV）的赋值集合。这种表示将状态空间从所有状态变量的笛卡尔积简化为可能直方图的集合。
4. **动作表示**：动作也基于计数进行定义，例如指定受限制的旅行者数量而非具体个体，从而将动作空间从指数级缩减为多项式级。
5. **线性规划求解**：基于紧凑状态和动作表示实例化线性规划，通过迭代所有状态和动作组合计算价值函数。转移概率的计算考虑了参数因子的影响以及多重系数加权的赋值转换。

创新点包括：
- 首次在关系MDP中引入一阶表示处理并发动作，通过关系成本图和CRV实现状态和动作的紧凑表示。
- 理论证明了状态表示的正确性，并分析了复杂度为对象数量的多项式。
- 提出了精确和近似两种版本的Foreplan，近似版本进一步加速计算并提供误差保证。
- 通过前向规划结合初始状态剪枝搜索空间，并支持添加互斥、容量等约束。

总之，Foreplan通过关系成本图识别依赖、利用CRV紧凑表示状态和动作、并基于线性规划高效计算策略，从而显著提升了可精确求解的规划问题规模。

### Q4: 论文做了哪些实验？

论文在实验部分主要进行了理论分析和实证评估，以验证所提出的Foreplan规划器的效率与准确性。实验设置方面，研究首先通过理论分析证明了Foreplan的复杂度：状态和动作空间在对象数量上是多项式级的，而在关系成本图的参数c（团数量）和w（团内顶点数）上是指数级的，但c和w通常较小且独立于领域大小，因此整体运行时在对象数量上是多项式复杂度，相比传统方法的指数级有了显著提升。

数据集或基准测试方面，论文虽未明确列出具体数据集名称，但实验基于关系因子化马尔可夫决策过程（MDP）模型，其中状态和动作空间因并发动作和大量不可区分对象而呈指数增长。对比方法主要针对传统规划方法，这些方法需要枚举状态和动作的联合空间，导致效率低下。

主要结果包括：1）理论分析显示Foreplan实现了精确规划，运行时在对象数量上为多项式，相比传统方法有指数级加速；2）实证评估中，Foreplan的精确版本在多个规划问题上实现了数个数量级的加速；3）近似版本Foreplan在进一步加速计算的同时，误差通常可忽略，论文还提供了误差保证。关键数据指标包括状态表示大小为O(c × 2^w)，其中c和w为小常数，以及运行时复杂度为对象数量的多项式。这些结果突出了Foreplan在合理时间内可解决更多精确规划问题的优势。

### Q5: 有什么可以进一步探索的点？

该论文在并发动作的马尔可夫决策过程中引入了关系一阶表示以应对状态和动作空间的指数爆炸，但仍存在一些局限性和可探索的方向。首先，论文假设对象是“不可区分的”，这在许多现实场景中可能不成立；未来研究可探索对象具有部分可区分性或属性差异时的扩展方法。其次，Foreplan 的近似版本虽然提供了误差保证，但理论误差界可能较宽松，实际应用时可能需更紧的界或自适应误差控制机制。此外，该方法目前侧重于前向规划，未来可结合反向搜索或启发式函数以处理更大规模或更复杂的任务。另一个方向是将其与深度学习结合，利用神经网络学习关系表示以进一步提升效率。最后，论文实证评估限于特定领域，未来需在更广泛的基准问题（如机器人规划、资源分配）中验证其通用性和鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对具有并发动作的马尔可夫决策过程（MDP）中，状态和动作空间随对象数量指数级增长导致策略计算效率低下的问题，提出了一种基于一阶表示的提升式前向规划方法。核心贡献是引入了关系因子化MDP（rfMDP）表示法，将不可区分的对象进行分组，从而将状态和动作空间的规模从指数级降低为关于对象数量的多项式级。论文提出了名为Foreplan的高效精确规划器，它利用关系代价图进行推理，其计算复杂度主要取决于图中团的数量和最大团的大小，而与域规模无关，因此在对象数量很大时能实现显著加速（实验显示可达四个数量级）。此外，论文还提出了Foreplan的近似版本，进一步降低了运行时间，并提供了误差保证。理论分析和实验评估表明，该方法能有效处理包含大量不可区分对象和并发动作的规划问题，极大地扩展了可精确求解的问题范围。
