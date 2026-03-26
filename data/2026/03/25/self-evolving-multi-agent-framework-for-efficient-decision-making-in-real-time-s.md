---
title: "Self-Evolving Multi-Agent Framework for Efficient Decision Making in Real-Time Strategy Scenarios"
authors:
  - "Li Ma"
  - "Hao Peng"
  - "Yiming Wang"
  - "Hongbin Luo"
  - "Jie Liu"
  - "Kongjing Gu"
  - "Guanlin Wu"
  - "Hui Lin"
  - "Lei Ren"
date: "2026-03-25"
arxiv_id: "2603.23875"
arxiv_url: "https://arxiv.org/abs/2603.23875"
pdf_url: "https://arxiv.org/pdf/2603.23875v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent"
  - "Real-Time Decision Making"
  - "LLM-based Agent"
  - "Planning"
  - "Memory"
  - "Self-Evolution"
  - "Efficiency Optimization"
  - "StarCraft II"
relevance_score: 7.5
---

# Self-Evolving Multi-Agent Framework for Efficient Decision Making in Real-Time Strategy Scenarios

## 原始摘要

Large language models (LLMs) have demonstrated exceptional potential in complex reasoning,pioneering a new paradigm for autonomous agent decision making in dynamic settings. However, in Real-Time Strategy (RTS) scenarios, LLMs suffer from a critical speed-quality trade-off. Specifically expansive state spaces and time limits render inference delays prohibitive, while stochastic planning errors undermine logical consistency. To address these challenges, we present SEMA (Self-Evolving Multi-Agent), a novel framework designed for high-performance, low-latency decision-making in RTS environments. This collaborative multi-agent framework facilitates self-evolution by adaptively calibrating model bias through in-episode assessment and cross-episode analysis. We further incorporate dynamic observation pruning based on structural entropy to model game states topologically. By distilling high dimensional data into core semantic information, this approach significantly reduces inference time. We also develop a hybrid knowledge-memory mechanism that integrates micro-trajectories, macro-experience, and hierarchical domain knowledge, thereby enhancing both strategic adaptability and decision consistency. Experiments across multiple StarCraft II maps demonstrate that SEMA achieves superior win rates while reducing average decision latency by over 50%, validating its efficiency and robustness in complex RTS scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在实时策略游戏场景中进行高效、低延迟决策时所面临的核心挑战。研究背景是，虽然LLMs在复杂推理方面展现出巨大潜力，为动态环境中的自主智能体决策提供了新范式，但将其应用于以《星际争霸II》为代表的RTS场景时，存在严重的“速度-质量”权衡困境。RTS环境具有高维状态空间和严格的秒级交互要求，对逻辑推理和反应敏捷性都提出了极高要求。

现有方法存在明显不足。传统基于规则的算法泛化能力差，难以适应动态演变的未知场景。强化学习方法则受限于高昂的训练成本、收敛稳定性问题，并且通常需要精心设计奖励函数和裁剪动作空间。近期，直接利用LLMs进行RTS推理的研究分化为两个方向：侧重于长程规划和战略逻辑的“推理”方向，往往在捕捉瞬时环境变化时存在逻辑延迟；侧重于提供即时交互响应的“决策”方向，则直接受到海量高维观测数据的严重阻碍。具体而言，现有LLM方法面临两大关键瓶颈：一是原始环境数据维度高、信息冗余，导致LLM输入序列过长，产生灾难性的令牌溢出，引发极高的推理延迟，无法满足实时性要求；二是LLM固有的随机性会导致决策逻辑不一致，即使在相同情境下也可能产生矛盾决策，严重损害智能体在复杂对抗环境中的鲁棒性和可靠性。

因此，本文要解决的核心问题是：如何设计一个能够同时实现**低延迟**和**高质量**决策的鲁棒框架，以克服LLM在RTS场景中因数据冗余导致的推理速度慢，以及因模型随机性导致的决策不一致性这两大缺陷。论文提出的SEMA框架通过多智能体协作、基于结构熵的动态观测剪枝以及混合知识-记忆机制，力图在保证战略深度和逻辑一致性的前提下，大幅提升决策速度，从而填补这一研究空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为多智能体系统（MAS）架构、规划与推理方法、以及基于LLM的通用决策框架三大类。

在多智能体系统架构方面，MetaGPT和ChatDev通过引入标准化流程或迭代交互，实现了任务分解与协作，但通常面向静态或非实时任务。Camel框架建立了自主协作的基础协议，而MindAgent探索了对抗场景下的个体与全局平衡。Generative Agents展示了长期记忆的作用。本文的SEMA框架与这些工作同属LLM作为认知核心的协作架构，但其核心区别在于**专门针对RTS场景的实时性约束**，通过自进化机制和动态观察剪枝来优化速度-质量权衡，这是先前通用架构未深入解决的。

在规划与推理方法上，Chain-of-Thought、Tree of Thoughts和Graph of Thoughts等系列工作增强了LLM的逻辑与路径规划能力，DEPS等框架通过分层规划处理长程依赖。然而，这些多步推理策略通常计算开销大，难以满足秒级决策需求。RASC框架尝试在实时环境中权衡效率与准确性，而本文SEMA则通过**结构熵进行状态拓扑建模与语义蒸馏**，并引入混合知识-记忆机制，旨在更直接地减少推理延迟并保持逻辑一致性，是对“以测试时间扩展换取规划精度”这一技术趋势的针对性发展。

在基于LLM的通用决策框架方面，Voyager通过技能库实现自进化决策，Agent-Omni增强多模态感知，另有研究将LLM应用于自动驾驶、空间理解等。针对逻辑漂移和幻觉，STeCa、PT-ALIGN等提出了校准机制。在游戏策略领域，已有研究探索LLM的行为偏差、编队控制及在《星际争霸II》中的反馈学习。本文SEMA与这些工作的共同点是利用LLM处理复杂语义观察，但其创新在于**深度融合了针对RTS的微观轨迹、宏观经验和分层领域知识**，并通过跨回合分析实现自适应偏差校准，从而在复杂动态对抗环境中同时提升胜率和降低延迟。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SEMA（Self-Evolving Multi-Agent）的新型协作多智能体框架来解决RTS环境中LLMs面临的推理延迟与逻辑一致性难题。其核心方法围绕一个闭环、自演化的三层架构展开，包含结构熵驱动的观察剪枝、自适应决策执行以及双环自演化三个阶段。

在整体框架上，SEMA首先通过**结构熵驱动的动态观察剪枝机制**对高维、非线性的原始游戏状态进行预处理。该方法将状态映射为动态属性图，并利用时空演化算子量化属性间的关联强度，构建加权图。随后，通过贪婪演化聚类算法构建分层编码树，并基于结构熵扰动变分度量（δ_H = α·ΔH_G + β·ΔH_T）识别并剪枝语义贡献低于阈值μ的非核心属性节点，在保留关键战略语义的同时，将LLM的token负载降低了约70%，显著提升了推理效率。

决策执行阶段采用**多智能体协作架构**，由决策、评估和分析反思三个智能体协同工作，并辅以**混合知识-记忆增强机制**。决策智能体接收剪枝后的观察、历史参考动作和战略经验，利用LLM进行逻辑推演，输出结构化的动作元组（e, op, ta），确保命令的确定性和可解释性。评估智能体则在决策前进行多尺度情境检索与语义对齐，从步级轨迹记忆库和回合级经验池中分别检索相似状态对应的历史动作a*与全局战略先验E，为决策提供多源信息融合的输入。分析反思智能体基于关键帧元数据进行事后评估，从分层领域知识库中提取战略规则，生成包含战术优劣的分析报告，并通过增量更新机制融入全局经验池，驱动策略的持续优化。

自演化阶段通过建立**嵌套反馈循环**实现：在步级进行游戏内评估，在回合级进行赛后分析。这种双环设计能够动态校准模型偏差，持续优化战略逻辑。评估智能体的闭环评估机制与经验库的增量更新共同构成了系统的自我修正能力，确保了策略在复杂对抗环境中的稳健性与适应性。

创新点主要体现在：1）首次将结构信息理论引入RTS的观察表示，提出基于结构熵的动态剪枝方法，实现了状态的高效语义压缩；2）设计了融合微观轨迹、宏观经验和分层领域知识的混合知识-记忆机制，增强了战略适应性与决策一致性；3）构建了步级与回合级相结合的双环自演化框架，使系统能通过持续校准实现自主进化。实验表明，该框架在多种《星际争霸II》地图上实现了更高的胜率，同时将平均决策延迟降低了50%以上。

### Q4: 论文做了哪些实验？

论文在《星际争霸II》的八个不同地图上进行了实验，以评估SEMA框架的性能。实验设置以Qwen3-next-80b作为基础模型，测试地图包括四个“混战”地图（每个地图测试两个难度等级：Lv.1和Lv.2）以及三个来自星际争霸多智能体挑战（SMAC）的地图（3m、8m、25m）。混战地图（如Flat32、Flat48、Flat64、Simple64）侧重于战略规划和宏观管理，而SMAC地图则强调微操和快速反应。在每个地图上，均进行50次随机试验，对阵游戏内置AI。

对比方法涵盖了RTS领域的多种代表性方法，包括随机策略、基于规则的智能体、单一大语言模型（Single-LLM）以及前沿的LLM框架如TextStarCraft和HIMA。

主要评估指标是胜率和平均决策延迟（即每步平均响应时间）。关键数据指标如下：在SMAC地图上，SEMA在3m、8m、25m地图的胜率分别达到88%、70%、68%，显著优于其他方法（例如，在3m地图上，HIMA胜率为66%，TextStarCraft为56%），同时平均响应时间分别为10秒、17秒、17秒，实现了速度与质量的平衡。在混战地图上，SEMA在多个地图和难度等级上达到了100%的胜率（如Flat32 Lv.1、Flat48 Lv.1、Flat64 Lv.1、Simple64 Lv.1和Lv.2），并且游戏时长（代表单局成功对局的执行时间）普遍更短，例如在Flat64 Lv.1上为5分钟，而HIMA为6分钟。总体而言，实验结果表明SEMA在保持高胜率的同时，将平均决策延迟降低了超过50%，验证了其在复杂RTS场景中的高效性和鲁棒性。

### Q5: 有什么可以进一步探索的点？

该论文提出的SEMA框架在降低延迟和提升决策质量方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架在动态环境中的泛化能力有待验证，目前实验集中于《星际争霸II》的特定地图，未来需扩展至更广泛的RTS游戏或现实世界场景（如机器人协作、交通调度），以评估其通用性。其次，虽然通过结构熵进行状态剪枝降低了计算负担，但可能丢失关键细节，未来可探索更精细的注意力机制或可解释性方法，以平衡信息压缩与决策完整性。此外，知识-记忆机制依赖预定义领域知识，可能限制自主适应能力；可结合在线学习或元学习，使系统能动态更新知识库，应对未知策略。最后，框架未充分探讨多智能体间的通信效率问题，在高度实时场景中，通信开销可能成为瓶颈，未来可引入轻量级通信协议或分布式学习机制，进一步提升协同效率。这些方向有望推动自主智能体在复杂动态环境中的实际应用。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为SEMA（自我进化多智能体）的新型框架，旨在解决大型语言模型在实时策略游戏场景中面临的决策速度与质量之间的权衡难题。针对RTS环境中状态空间庞大、时间限制严格以及规划随机性导致的逻辑不一致问题，SEMA通过协作式多智能体架构实现自我进化，其核心方法包括：基于结构熵的动态观察剪枝，将高维游戏状态拓扑化以压缩核心语义信息，大幅降低推理延迟；同时设计混合知识-记忆机制，融合微观轨迹、宏观经验和分层领域知识，提升策略适应性与决策一致性。实验表明，在多个《星际争霸II》地图上，SEMA在取得更高胜率的同时，将平均决策延迟降低超过50%，验证了其在复杂动态环境中高效、鲁棒的决策能力。该框架为LLM在实时交互场景的应用提供了兼顾速度与质量的创新解决方案。
