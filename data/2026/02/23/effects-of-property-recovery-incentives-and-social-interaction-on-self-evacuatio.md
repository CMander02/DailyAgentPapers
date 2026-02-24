---
title: "Effects of Property Recovery Incentives and Social Interaction on Self-Evacuation Decisions in Natural Disasters: An Agent-Based Modelling Approach"
authors:
  - "Made Krisnanda"
  - "Raymond Chiong"
  - "Yang Yang"
  - "Kirill Glavatskiy"
date: "2026-02-23"
arxiv_id: "2602.19639"
arxiv_url: "https://arxiv.org/abs/2602.19639"
pdf_url: "https://arxiv.org/pdf/2602.19639v1"
categories:
  - "cs.MA"
tags:
  - "Agent-Based Modeling"
  - "Multi-Agent Systems"
  - "Evolutionary Game Theory"
  - "Decision-Making"
  - "Social Networks"
  - "Policy Design"
relevance_score: 4.0
---

# Effects of Property Recovery Incentives and Social Interaction on Self-Evacuation Decisions in Natural Disasters: An Agent-Based Modelling Approach

## 原始摘要

Understanding evacuation decision-making behaviour is one of the key components for designing disaster mitigation policies. This study investigates how communications between household agents in a community influence self-evacuation decisions. We develop an agent-based model that simulates household agents' decisions to evacuate or stay. These agents interact within the framework of evolutionary game theory, effectively competing for limited shared resources, which include property recovery funds and coordination services. We explore four scenarios that model different prioritisations of access to government-provided incentives. We discover that the impact of the incentive diminishes both with increasing funding value and the household agent prioritisation, indicating that there is an optimal level of government support beyond which further increases become impractical. Furthermore, the overall evacuation rate depends on the structure of the underlying social network, showing discontinuous jumps when the prioritisation moves across the node degree. We identify the so-called "community influencers", prioritisation of whom significantly increases the overall evacuation rate. In contrast, prioritising household agents with low connectivity may actually impede collective evacuation. These findings demonstrate the importance of social connectivity between household agents. The results of this study are useful for designing optimal government policies to incentivise and prioritise community evacuation under limited resources.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自然灾害中家庭自主疏散决策的复杂性问题，重点关注政府激励措施（如财产恢复资金）和社会互动如何影响疏散行为。研究指出，现有文献在结合政府支持与社会网络动态方面存在缺口：例如，有些研究考察了台风中的疏散行为但未考虑政府资金支持，而另一些研究了政府与家庭互动却未聚焦于对家庭的直接激励。因此，论文试图通过基于智能体的建模（ABM）与演化博弈论（EGT）相结合的方法，模拟家庭智能体在有限共享资源（如恢复资金和协调服务）下的决策过程，探索不同政府激励优先级分配方案的效果。核心目标是揭示社会网络结构（如社区影响者的作用）和激励政策之间的相互作用，从而为政府在资源有限条件下设计最优的疏散激励政策提供科学依据，以提高整体疏散效率。

### Q2: 有哪些相关研究？

本文涉及的相关研究主要涵盖灾害疏散决策、社会网络影响、政府激励政策以及建模方法四个方向。在灾害疏散决策方面，Chen (2005) 和 Shi (2021) 研究了家庭在灾害中的决策行为，但前者未考虑政府资金支持，后者则聚焦于对地方政府的奖励而非家庭。Sun (2020) 研究了台风期间的疏散行为，同样未纳入财产恢复基金这一政府支持因素。在社会网络影响方面，Bustillos Ardaya等人 (2017) 指出社区领袖拥有更广的网络和影响力，Rawsthorne (2023) 和 Losee (2022) 强调了社会网络对于动员社区行动和应对环境威胁的重要性，但未详细阐明网络连接如何具体影响疏散过程。在政府激励政策方面，Chester (2020) 指出发达国家政府常提供灾害救助项目。在建模方法上，研究借鉴了进化博弈论（EGT）来模拟策略演化（Adami, 2016），并广泛采用基于智能体的建模（ABM）来模拟洪水、干旱、风暴等多种灾害下的个体互动与系统行为（相关综述文献）。此外，研究采用小世界网络（Milgram, 1967; Torren-Peraire, 2024）来刻画社区互动结构。

本文与这些研究的关系在于：它**整合并拓展**了现有工作。具体而言，本文将政府提供的财产恢复基金激励直接引入家庭疏散决策模型，弥补了Sun (2020) 等人研究的空白。同时，它深入探究了社会网络结构（特别是节点度）和“社区影响者”对集体疏散率的**具体影响机制**，细化和深化了Rawsthorne (2023) 等人关于网络重要性的论述。在方法上，本文**结合**了进化博弈论（用于计算互动收益与成本）和基于智能体的建模（用于模拟家庭代理的互动），以此分析有限资源下不同激励优先分配方案的效果，从而为优化政府疏散激励政策提供定量依据。

### Q3: 论文如何解决这个问题？

该论文通过构建一个基于智能体的模型（ABM）来研究自然灾害中家庭的自发疏散决策问题，核心方法是结合进化博弈论（EGT）和社会网络分析，模拟政府激励措施和社会互动如何影响个体决策。模型架构以社会网络为基础，每个节点代表一个家庭智能体，边代表社会互动。智能体的决策框架采用保护动机理论（PMT），评估灾害威胁（发生概率和严重性）和应对能力（疏散与留守的成本），以最小化损失。

关键技术体现在以下几个方面：首先，模型引入了有限共享资源（如道路容量、避难所）的竞争，这会影响疏散成本，从而形成个体策略的相互依赖。其次，利用进化博弈论建模智能体间的互动：每对智能体交互后根据双方决策（均疏散、均留守、一方疏散一方留守）获得相应收益（Payoff），收益计算综合考虑了财产价值、风险感知、疏散/留守附加成本以及政府激励。政府激励分为财产恢复资金（按财产比例θ提供）和服务支持（如为疏散者提供交通协调，为留守者提供财产保护），这些激励会直接调整收益值，影响决策演化。

模型通过设计四种不同优先级的激励分配场景，揭示了激励效果存在最优水平，过度增加支持反而效果递减。更重要的是，研究发现社会网络结构对整体疏散率有决定性影响：优先激励高度连接的“社区影响者”能显著提升疏散率，而优先激励连接度低的个体反而可能阻碍集体疏散。这表明，模型通过量化社会互动和资源竞争的博弈动态，为解决有限资源下如何优化政府激励政策提供了计算实验依据。

### Q4: 论文做了哪些实验？

该研究基于智能体建模，通过模拟实验探究了政府激励和社交网络结构对家庭自主疏散决策的影响。实验设置方面，构建了一个包含5000个节点（代表家庭智能体）的小世界网络，模拟了3000个时间步长。智能体根据演化博弈论框架与邻居互动，通过基于概率的模仿规则更新决策（倾向于模仿收益更高的邻居）。政府激励通过财产恢复激励比例θ（从-10%到20%）来控制，并设定了风险估计、成本分摊等多项参数。

研究设计了四种优先排序场景作为基准测试：随机最高度（优先疏散连接数最多的节点，其余随机）、固定最高度（优先疏散最高度节点，其余固定为留下）、随机最低度（优先疏散连接数最少的节点，其余随机）和固定最低度（优先疏散最低度节点，其余固定为留下）。疏散率通过最后1000个时间步内选择疏散的智能体比例计算，并取5次模拟的平均值。

主要结果显示：1）激励效果存在最优水平，过高激励或过度优先排序会使其效果递减；2）疏散率受底层社交网络结构影响显著，在优先排序跨越节点度阈值时会出现不连续的跳跃式增长；3）识别出“社区影响者”（高度数节点），优先疏散他们能显著提升整体疏散率；4）相反，优先疏散低连接度节点可能阻碍集体疏散。例如，在随机最高度场景中，当优先排序达到57%（涵盖度数5的节点）时，0%激励下的疏散率从38.3%跃升至100%，触发了级联效应。这些发现强调了智能体间社会连接的重要性，为有限资源下优化政府疏散政策提供了依据。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在三个方面：一是模型基于特定的小世界网络，结论可能不适用于其他拓扑结构（如无标度网络、随机网络），需在多样化网络中进行验证；二是假设社会网络静态不变，而现实中社交互动是动态演化的，未来需结合动态网络和自适应模型；三是智能体同质性较强，未充分考虑个体在风险感知、行动能力等方面的异质性。

未来研究方向包括：扩展网络拓扑研究，验证不同网络结构下激励与优先策略的普适性；开发动态网络模型，以反映灾害中社会关系的实时变化；增强智能体异质性，融入心理、社会经济等多维属性，提升决策真实性；探索多灾种、多阶段疏散场景，并考虑政府信息发布、交通系统等外部因素的综合影响。

### Q6: 总结一下论文的主要内容

该论文采用基于智能体的建模（ABM）结合演化博弈论，研究了自然灾害中家庭智能体的自主疏散决策行为。核心贡献在于揭示了政府激励措施与社交网络结构对集体疏散率的复杂交互影响。研究发现，优先向社交连接度高的“社区影响者”提供财产恢复激励能显著提升整体疏散率，而优先连接度低的个体反而可能阻碍疏散进程。同时，激励效果存在阈值效应：超过一定水平后，增加资金或优先对象反而效果递减，且疏散率在特定优先值附近会出现突变式跳跃。这些非线性动态表明，在资源有限的情况下，政策制定应精准针对网络关键节点，而非简单扩大激励规模。该研究为优化应急疏散政策提供了基于数据的新视角，强调了社交连通性在灾害管理中的关键作用。
