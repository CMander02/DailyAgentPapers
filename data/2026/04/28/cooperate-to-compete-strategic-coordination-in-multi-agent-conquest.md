---
title: "Cooperate to Compete: Strategic Coordination in Multi-Agent Conquest"
authors:
  - "Abigail O'Neill"
  - "Alan Zhu"
  - "Mihran Miroyan"
  - "Narges Norouzi"
  - "Joseph E. Gonzalez"
date: "2026-04-28"
arxiv_id: "2604.25088"
arxiv_url: "https://arxiv.org/abs/2604.25088"
pdf_url: "https://arxiv.org/pdf/2604.25088v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体协作"
  - "混合动机博弈"
  - "谈判策略"
  - "人类-AI对比"
  - "基准测试"
relevance_score: 9.0
---

# Cooperate to Compete: Strategic Coordination in Multi-Agent Conquest

## 原始摘要

Language Model (LM)-based agents remain largely untested in mixed-motive settings where agents must leverage short-term cooperation for long-term competitive goals (e.g., multi-party politics). We introduce Cooperate to Compete (C2C), a multi-agent environment where players can engage in private negotiations while competing to be the first to achieve their secret objective. Players have asymmetric objectives and negotiations are non-binding, allowing alliances to form and break as players' short-term interests align and diverge. We run AI only games and conduct a user study pitting human players against AI opponents. We identify significant differences between human and AI negotiation behaviors, finding that humans favor lower-complexity deals and are significantly less reliable partners compared to LM-based agents. We also find that humans are more aggressive negotiators, accepting deals without a counteroffer only 56.3% of the time compared to 67.6% for LM-based agents. Through targeted prompting inspired by these findings, we modify agents' negotiation behavior and improve win rates from 22.2% to 32.7%. We run over 1,100 games with over 16,000 private conversations totaling 15.2 million tokens and over 150,000 player actions. Our results establish C2C as a testbed for studying and building LM-based agents that can navigate the sophisticated coordination required for real-world deployments. The game, code, and dataset may be found at https://negotiationgame.io/c2c.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有AI Agent在混合动机场景下长期战略协调能力不足的问题。研究背景是，随着AI进入复杂社会系统，需要能在多党政治等场景中利用短期合作实现长期竞争目标的Agent。现有多Agent基准测试主要评估纯合作或纯竞争行为，少数混合动机环境存在结构限制，如信息对称更新或短视任务，无法反映现实中长期协作与竞争并存、信息不对称、关系动态演变的复杂情况。本文提出的核心问题是：如何构建一个能模拟长期、非对称信息、且允许非约束性谈判的混合动机环境，以系统评估和提升LM-based Agent在“合作以竞争”策略下的表现。作者通过设计“Cooperate to Compete (C2C)”游戏环境，要求玩家在迷雾战争、秘密目标、非约束性联盟等条件下进行谈判和征服，从而研究Agent如何规划短期协调以获取长期竞争优势，并对比人类与AI的谈判行为差异，最终通过针对性提示改进AI策略。

### Q2: 有哪些相关研究？

在相关研究中，混合动机场景（如多党政治）下基于语言模型（LM）的智能体评估仍较少。本文与之相关的核心工作包括：

1. **多智能体游戏环境**：现有工作多聚焦短时互动（如简单回合制游戏），机会有限且联盟形成时间不足。社会推理游戏（如“狼人杀”）虽涉及多轮交互，但玩家被预先分入固定团队，限制了自然联盟的涌现。与本文C2C环境不同，后者是一个长时竞争游戏，允许短期合作自发形成临时“团队”，并支持非约束性谈判。

2. **与“外交（Diplomacy）”游戏的对比**：Diplomacy同样具有长时竞争、无固定团队和自然联盟演化特点，但其高度复杂性使战略规划能力比智能体间协调行为更重要。C2C则刻意降低推理负担，鼓励更多智能体间交互（如非绑定对话），聚焦于协调策略本身。

3. **廉价谈话与信任演化**：多智能体竞争中，非绑定通信（廉价谈话）被证明能影响结果，尤其当理性不完美时。C2C通过长时重复对话，允许LM智能体更新对他人可靠性的信念，动态演化信任、声誉和联盟结构。本文特别关注LM在长时协商中如何策略性地利用通信以推进自身目标，这与现有研究较少涉及的方向形成对比。

总之，C2C填补了LM在混合动机场景中协调策略研究的空白，尤其通过降低任务复杂度、强调交互行为而区别于Diplomacy等复杂环境。

### Q3: 论文如何解决这个问题？

这篇论文通过构建一个名为“合作以竞争”（C2C）的多智能体环境，并采用基于语言模型（LM）的智能体与人类进行对比实验，来解决智能体在混合动机场景下的战略协调问题。

核心方法是一个非对称目标、非约束谈判的多智能体博弈游戏。整体框架包含四个玩家，每两个玩家组成一个“对”，每个对拥有一个秘密目标，玩家需要率先完成各自的目标才能获胜。游戏的核心在于玩家之间可以进行私密的、非约束性的谈判（如承诺结盟、交易地盘），这允许短期合作与长期竞争共存。架构设计上，每个玩家都由一个LM智能体驱动，通过提示工程（prompting）赋予其特定角色和谈判策略，例如可以接受或拒绝交易、进行加价谈判等。

关键技术包括：首先，设计了一个复杂的多轮谈判协议，玩家可以自由提出、接受或拒绝交易。其次，通过与人类玩家（用户研究）的对比，定量分析了人类与LM智能体在谈判行为上的显著差异：人类偏好低复杂度交易，且作为合作伙伴可靠性显著低于LM智能体；人类更激进，接受无还价交易的比例（56.3%）低于LM智能体（67.6%）。基于这些发现，作者通过针对性提示（targeted prompting），如让智能体模仿人类的激进谈判风格（主动还价、提高交易复杂度），成功将LM智能体的胜率从22.2%提升至32.7%。系统还集成了超过1,100场游戏、16,000次私密对话和15.2百万标记的庞大数据集用于分析和后续研究。创新点在于将LM智能体置于真实的人类谈判数据中，反哺改进智能体策略，建立了一个能够研究战略协调的测试床。

### Q4: 论文做了哪些实验？

论文进行了三类实验：(1) 用户研究: 82局游戏，1名人类与3个AI对手对战，人类来自机构内的40名参与者。(2) 匹配AI博弈: 重用人类相同的82个起始位置，由随机分配的AI代理（参考代理）以及顶尖模型Gemini 3.1 Pro进行对比。(3) 干预实验: 基于人类行为差异设计的提示干预，在162个起始位置上评估。AI代理池包含6个模型，包括Gemini 3.1 Pro等。主要结果：用户研究中人类胜率（41.5%）显著高于参考代理（22.0%），与Gemini 3.1 Pro（44.6%）无显著差异。行为分析显示，人类谈判更激进，直接接受率56.3%（AI为67.6%），更少承诺支持（0.063 vs 0.382次/协议），更频繁更换谈判对象。干预实验中，无谈判（12.3%）、单伙伴（16.7%）均降低胜率；而激进谈判（30.9%）、寻求支持（30.9%）和欺骗策略（32.7%）显著提升了胜率（基线22.2%）。实验总计超过1100场游戏，超过16,000次对话。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要包括：当前非约束性谈判机制可引入违约惩罚或强制合规（如扣除兵力），以增强合作可信度；游戏规模可扩展至不同人数组合，探索人类与不同推理能力、人格或架构的AI混合博弈；通信渠道可增设群组广播或定向信息通道。核心挑战在于对手依赖性：自博弈训练可能无法使AI应对多样化对手的策略漏洞与推理弱点，未来需研究元学习或对抗训练来提升泛化能力。此外，一个关键方向是检验在《C2C》中习得的协调策略能否迁移至《外交》《幸存者》等其他混合动机游戏。从人类行为差异（如更激进的谈判、更低的盟友忠诚度）出发，可进一步探索如何通过多轮博弈的反馈动态校准AI的社交推理与联盟操纵能力，这要求开发能实时评估对方信任可靠度与谈判风格的自适应算法。

### Q6: 总结一下论文的主要内容

这篇论文提出了**Cooperate to Compete (C2C)**，这是一个面向混合动机场景的多智能体环境。在该环境中，智能体需通过短期合作以实现长期的竞争目标。核心问题是：在非绑定谈判、信息不对称的长期博弈中，语言模型智能体能否展现策略性协调能力。方法上，作者设计了包含地图、迷雾战争与秘密目标（控制两个区域）的征服游戏，允许玩家进行私下谈判。主要结论包括：相比LM智能体，人类谈判更激进（直接接受更少）、更不可靠、更少协助对手；限制谈判或合作伙伴会显著降低胜率。基于人类行为的提示干预（如更激进、欺骗性谈判）可将AI胜率从22.2%提升至32.7%。该工作填补了从全合作或短视竞争到长期混合动机环境研究的空白，为构建能驾驭真实世界复杂协调的AI智能体提供了测试平台。
