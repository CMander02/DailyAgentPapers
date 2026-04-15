---
title: "How memory can affect collective and cooperative behaviors in an LLM-Based Social Particle Swarm"
authors:
  - "Taisei Hishiki"
  - "Takaya Arita"
  - "Reiji Suzuki"
date: "2026-04-14"
arxiv_id: "2604.12250"
arxiv_url: "https://arxiv.org/abs/2604.12250"
pdf_url: "https://arxiv.org/pdf/2604.12250v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.GT"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "生成式智能体建模"
  - "记忆机制"
  - "社会模拟"
  - "囚徒困境"
  - "智能体个性"
  - "模型对齐"
  - "涌现行为"
  - "比较实验"
relevance_score: 8.0
---

# How memory can affect collective and cooperative behaviors in an LLM-Based Social Particle Swarm

## 原始摘要

This study examines how model-specific characteristics of Large Language Model (LLM) agents, including internal alignment, shape the effect of memory on their collective and cooperative dynamics in a multi-agent system. To this end, we extend the Social Particle Swarm (SPS) model, in which agents move in a two-dimensional space and play the Prisoner's Dilemma with neighboring agents, by replacing its rule-based agents with LLM agents endowed with Big Five personality scores and varying memory lengths. Using Gemini-2.0-Flash, we find that memory length is a critical parameter governing collective behavior: even a minimal memory drastically suppressed cooperation, transitioning the system from stable cooperative clusters through cyclical formation and collapse of clusters to a state of scattered defection as memory length increased. Big Five personality traits correlated with agent behaviors in partial agreement with findings from experiments with human participants, supporting the validity of the model. Comparative experiments using Gemma~3:4b revealed the opposite trend: longer memory promoted cooperation, accompanied by the formation of dense cooperative clusters. Sentiment analysis of agents' reasoning texts showed that Gemini interprets memory increasingly negatively as its length grows, while Gemma interprets it less negatively, and that this difference persists in the early phase of experiments before the macro-level dynamics converge. These results suggest that model-specific characteristics of LLMs, potentially including alignment, play a fundamental role in determining emergent social behavior in Generative Agent-Based Modeling, and provide a micro-level cognitive account of the contradictions found in prior work on memory and cooperation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型语言模型（LLM）智能体在基于生成式的多智能体建模（GABM）中，其模型特异性（特别是内部对齐特性）如何影响记忆能力对集体合作行为的塑造作用，从而解释现有文献中关于记忆与合作关系的矛盾结论。

研究背景方面，利用LLM进行生成式智能体建模为研究复杂社会现象提供了新方法，其中合作行为的涌现是核心议题。已有研究表明，LLM在博弈场景中能展现策略行为，且其行为受到模型对齐等特性的深刻影响。同时，在传统的基于规则的智能体模型（如社会粒子群SPS模型）中，记忆长度被视为影响合作的关键认知参数，但现有文献对此的结论相互矛盾：有些认为长记忆促进合作，有些则认为其抑制合作，尚无统一解释。

现有方法的根本不足在于，传统模型中的记忆与行为关系是预先由模型设计者通过固定规则或方程定义的，智能体无法对记忆进行灵活、依赖上下文的解读。这限制了模型捕捉复杂、涌现的社会动态的能力。

因此，本文要解决的核心问题是：当使用具有自然语言推理能力的LLM智能体（其决策基于个性评分和可变长度的交互历史）替代传统规则智能体时，LLM模型本身的特异性（包括内部对齐、架构等）是否会从根本上决定记忆长度对集体合作动态的影响模式？论文通过扩展SPS模型，使用Gemini-2.0-Flash和Gemma-3:4b这两个特性不同的LLM进行对比实验，旨在揭示模型差异如何导致记忆被截然不同地解读（例如，视为负面威胁还是积极信息），从而在宏观上产生甚至相反的集体行为趋势，为记忆与合作的矛盾发现提供一种基于微观认知过程的解释。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM在博弈论与多智能体系统中的行为研究**：多项工作已探索LLM在博弈环境中的策略性行为。例如，Akata等人发现GPT-4在重复囚徒困境中表现出类似“触发策略”的行为；Fontana等人指出LLM往往比人类玩家更具合作性，并将其归因于对齐训练所灌输的慷慨行为启发式；Pal等人则系统刻画了多个前沿模型在迭代囚徒困境中的策略剖面，证明对齐特性是影响博弈行为的关键因素。这些研究共同表明，LLM的模型特定特征（包括内部对齐）是生成式基于智能体建模（GABM）中涌现社会行为的重要决定因素，为本文研究奠定了基础。本文在此基础上，进一步探究记忆长度这一关键认知参数如何与模型特性交互影响集体合作动力学。

**2. 记忆对合作行为影响的传统理论研究**：在基于智能体的集体行为模型中，记忆的作用已得到广泛探讨，但现有文献存在明显矛盾。部分研究表明较长记忆可通过识别过往行为、稳定互惠策略来促进合作；另一些研究则指出过长记忆可能导致基于声誉的惩罚循环、阻碍宽恕或引入信息质量权衡，反而损害合作；还有观点认为中等记忆长度最优，或效应具有情境依赖性。这些研究通常以预定义规则或方程来建模记忆与行为的关系，缺乏灵活性。本文的创新在于引入LLM智能体，使其能够以自然语言处理记忆并在博弈情境中进行自底向上的推理，从而为记忆的解读和行为转化提供了更贴近人类认知的机制。

**3. 社会粒子群模型及其相关扩展研究**：社会粒子群模型整合了自驱动粒子动力学与演化博弈论，用于研究连续空间中合作行为与社会关系的协同演化。该模型已识别出稳定的合作集群、集群周期性形成与崩溃、以及分散背叛等典型集体状态。先前的人类参与者实验在该框架下揭示了合作的不稳定性以及大五人格特质与行为的相关性。近期研究开始将LLM智能体引入该模型，例如通过LLM进行人格建模以复现和拓展人格与行为的关联，或探究LLM智能体人格特质的演化如何引致合作行为的涌现与崩溃。本文直接沿袭这一方向，通过用具备大五人格分数和可变记忆长度的LLM智能体替代原模型中的规则智能体，系统比较不同LLM（如Gemini-2.0-Flash与Gemma-3:4b）下记忆长度对集体动力学的影响，从而揭示模型特定特征（如对齐差异）的关键作用。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大语言模型（LLM）的扩展社会粒子群（SPS）模型来解决研究问题，其核心方法是用具备记忆和人格特质的LLM智能体替代原模型中的规则驱动智能体，以探究记忆长度和模型特性对多智能体系统中集体与合作行为的影响。

整体框架是一个在二维环面空间运行的多智能体模拟系统。每个时间步，每个智能体基于其当前状态、预先分配的大五人格特质、与邻居的近期交互历史（由记忆长度L_m控制）以及邻居的当前状态，通过LLM生成决策。决策包括下一时间步的策略（合作或背叛）和移动行动（速度大小和方向），并附有自然语言推理陈述。系统的关键设计在于将囚徒困境博弈嵌入空间交互中，即时收益随邻居距离增加而衰减，累计收益是智能体的优化目标。

主要模块/组件包括：1）**环境与交互模块**：定义了智能体在二维空间中的移动、邻居检测以及基于距离加权的囚徒困境收益计算。2）**智能体决策模块**：核心是精心设计的提示词模板，它结构化为五个部分：实验环境与目标描述、完整的收益矩阵、智能体的人格特质（以JSON格式提供连续数值）、当前状态与邻居信息（包括相对位置和策略）、以及与每个邻居的交互历史（当L_m>0时）。历史记录以JSON格式按时间倒序附加，使智能体能够进行依赖上下文的决策。3）**输出解析模块**：要求LLM以结构化格式输出行动、策略和推理，其中推理文本为后续的微观认知分析（如情感分析）提供了数据。4）**模型对比模块**：研究使用了Gemini-2.0-Flash和Gemma~3:4b两种不同特性的LLM进行对比实验，以考察模型特定属性（如对齐程度）的影响。

创新点主要体现在：1）**记忆的显式建模与注入**：通过提示词将对手特定的交互历史作为文本直接注入给无状态的LLM，实现了可调控的记忆机制，并允许分析记忆长度对宏观行为的非线性影响。2）**人格特质的量化集成**：将大五人格以连续数值形式融入提示，提供了可复现的个体差异性来源，并与人类实验发现进行关联验证。3）**微观推理与宏观行为的连接**：通过分析智能体输出的推理文本进行情感分析，为宏观集体动态（如合作簇的形成与崩溃）提供了微观认知层面的解释，从而揭示了不同LLM对记忆解读的情感倾向差异是导致合作行为相反趋势的内在原因。这种方法将基于生成智能体的建模从行为模拟提升到了认知机制探索的层面。

### Q4: 论文做了哪些实验？

该研究基于扩展的“社会粒子群”（SPS）模型进行实验，其中LLM智能体在二维空间中移动并与邻近智能体进行囚徒困境博弈。实验设置固定智能体数量N=100，世界宽度W=500，交互半径R=50，最大速度MAX_SPEED=20，每轮运行T=500步。囚徒困境收益矩阵参数为：诱惑T=2.0，奖励R=1.0，惩罚P=-1.0，受骗S=-2.0。每个智能体被赋予从截断正态分布（均值0.5，标准差0.16）随机抽取的大五人格分数，并设置了不同的记忆长度Lm ∈ {0, 1, 2, 3}。每个条件进行10次独立实验。

研究使用Gemini-2.0-Flash和Gemma-3:4b（4位量化）作为对比的LLM模型。主要结果包括：
1.  **Gemini-2.0-Flash实验**：记忆长度显著抑制合作。关键数据指标显示，合作率均值随Lm增加从0.899（Lm=0）单调下降至0.0776（Lm=3）；平均邻居数相应从17.6降至2.48。Lm=1时合作率波动性最高（0.108），呈现合作簇循环形成与崩溃的周期性动态（Class-C类）。空间模式显示，背叛者向左漂移（约180°），合作者向右上移动（约60°）。
2.  **人格与行为相关性分析（Lm=1）**：宜人性与合作率呈最强正相关（r=0.55），与邻居数正相关（r=0.21），与移动距离负相关（r=-0.22）；外向性与移动距离正相关（r=0.58）；神经质与合作率负相关（r=-0.23）。这些结果与人类实验部分一致，验证了模型有效性。
3.  **Gemma-3:4b对比实验**：呈现相反趋势，记忆长度促进合作。合作率均值随Lm增加从0.279（Lm=0）上升至0.766（Lm=3）；平均邻居数从23.9（Lm=0）先升至30.2（Lm=1）后稳定在较高水平。Lm=3时形成密集合作簇，系统动态与Gemini相反。
4.  **微观认知分析**：对智能体推理文本进行情感分析发现，Gemini对记忆的情感评分随Lm增加从正转负（Lm=0约+0.85，Lm=3约-0.45），而Gemma则从负转正（Lm=0约-0.65，Lm=3接近中性）。早期阶段（t≤30）分析证实该差异是模型固有特性，而非宏观动态的结果，这为宏观行为的对立提供了微观解释。

### Q5: 有什么可以进一步探索的点？

该研究揭示了基于LLM的生成式智能体建模（GABM）中，记忆对合作行为的影响高度依赖于具体模型，这既是核心发现，也指明了局限性。未来研究可从以下几个方向深入：首先，需在更广泛的LLM（如不同规模、架构和alignment策略的模型）上进行系统性比较，以分离出影响社会性涌现的关键模型属性（如预训练数据、指令微调强度）。其次，当前记忆以结构化历史记录形式存在，未来可探索更丰富的记忆表征，如自然语言描述的定性印象或情感摘要，这可能更贴近人类社交记忆的运作方式。再者，论文提到未来将引入明确的推理阶段，这是一个重要改进思路；可进一步设计干预实验，例如通过提示工程或上下文学习来主动调节智能体对记忆的解读（如引导其更积极或更宽容），从而验证能否宏观上调控合作动态。最后，从方法论上，可结合“LLM-as-a-Judge”对智能体的推理文本进行更细粒度的认知特征分析（如归因方式、社会价值取向），建立微观认知模式与宏观群体行为之间的可解释链路，这有助于设计更可靠、可预测的多智能体系统。

### Q6: 总结一下论文的主要内容

本研究探讨了大型语言模型（LLM）智能体的模型特定特性（包括内部对齐）如何影响其在多智能体系统中的集体与合作行为。为此，论文扩展了社会粒子群（SPS）模型，将其中基于规则的智能体替换为具有大五人格分数和不同记忆长度的LLM智能体。智能体在二维空间中移动，并与邻近智能体进行囚徒困境博弈。

核心贡献在于揭示了记忆长度是调控集体行为的关键参数，但其影响方向高度依赖于所使用的具体LLM模型。使用Gemini-2.0-Flash时，即使很短的记忆也会显著抑制合作；随着记忆增长，系统从稳定的合作集群，经历集群周期性形成与崩溃，最终转变为分散的背叛状态。相反，使用Gemma~3:4b时，更长的记忆反而促进了合作，并形成了密集的合作集群。

论文的意义在于，通过对智能体推理文本的情感分析，为上述宏观矛盾现象提供了微观认知解释：Gemini将更长的记忆解读得越来越负面，而Gemma则不那么负面。这证明了LLM的模型特定特性（可能包括对齐方式）在基于生成智能体的建模中，对涌现的社会行为起着根本性的决定作用，并调和了先前关于记忆与合作关系研究中存在的矛盾发现。
