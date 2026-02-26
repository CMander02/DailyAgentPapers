---
title: "Training Generalizable Collaborative Agents via Strategic Risk Aversion"
authors:
  - "Chengrui Qu"
  - "Yizhou Zhang"
  - "Nicholas Lanzetti"
  - "Eric Mazumdar"
date: "2026-02-25"
arxiv_id: "2602.21515"
arxiv_url: "https://arxiv.org/abs/2602.21515"
pdf_url: "https://arxiv.org/pdf/2602.21515v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "多智能体强化学习"
  - "智能体协作"
  - "泛化性"
  - "战略风险规避"
  - "博弈论"
  - "未见伙伴协作"
  - "LLM协作任务"
relevance_score: 8.5
---

# Training Generalizable Collaborative Agents via Strategic Risk Aversion

## 原始摘要

Many emerging agentic paradigms require agents to collaborate with one another (or people) to achieve shared goals. Unfortunately, existing approaches to learning policies for such collaborative problems produce brittle solutions that fail when paired with new partners. We attribute these failures to a combination of free-riding during training and a lack of strategic robustness. To address these problems, we study the concept of strategic risk aversion and interpret it as a principled inductive bias for generalizable cooperation with unseen partners. While strategically risk-averse players are robust to deviations in their partner's behavior by design, we show that, in collaborative games, they also (1) can have better equilibrium outcomes than those at classical game-theoretic concepts like Nash, and (2) exhibit less or no free-riding. Inspired by these insights, we develop a multi-agent reinforcement learning (MARL) algorithm that integrates strategic risk aversion into standard policy optimization methods. Our empirical results across collaborative benchmarks (including an LLM collaboration task) validate our theory and demonstrate that our approach consistently achieves reliable collaboration with heterogeneous and previously unseen partners across collaborative tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体协作任务中，学习到的策略在面对新合作伙伴时泛化能力差的问题。研究背景是，随着AI系统在多智能体环境中日益普及，协作任务（如机器人协同、多模型合作编程）变得至关重要，其中智能体需与不同合作伙伴（包括人类或其他算法）有效互动以实现共同目标。现有方法（如基于经典博弈论概念或标准多智能体强化学习的方法）存在明显不足：它们往往产生脆弱的解决方案，容易过度拟合特定合作伙伴的策略或惯例，导致在面对新伙伴时性能骤降；同时，这些方法在训练中常出现“搭便车”现象，即智能体倾向于减少自身贡献、依赖伙伴付出，这进一步损害了泛化能力。

本文的核心问题是：如何设计一种原则性方法，使智能体学习到既能保持协作性能，又能泛化到未知或异构合作伙伴的策略。为此，论文提出将“战略风险厌恶”作为解决该问题的归纳偏置。战略风险厌恶强调智能体应对合作伙伴行为的不确定性保持风险厌恶，从而迫使策略对伙伴的偏差具有鲁棒性。通过理论分析和算法设计，论文证明了战略风险厌恶不仅能提升协作效果、缓解搭便车问题，还能在不牺牲性能的前提下增强泛化能力，最终实现与多样化、未见伙伴的可靠协作。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕协作多智能体强化学习（MARL）中的伙伴泛化问题展开，可分为以下几类：

**1. 基于种群的方法**：这类方法通过训练智能体与多样化的策略种群交互，以提升对未知伙伴的适应性，类似于伙伴策略的领域随机化。然而，生成高质量的伙伴种群通常依赖启发式设计，计算成本高，且难以保证泛化性能，尤其在复杂任务（如大语言模型微调）中可扩展性有限。

**2. 基于随机化的鲁棒性方法**：部分研究通过在策略优化中增加熵正则化等随机性来增强鲁棒性。这类方法虽易于扩展，但本文实验表明其无法有效解决“搭便车”问题，因此难以实现跨任务的稳定泛化。

**3. 战略风险规避的理论与应用**：战略风险规避概念在实验经济学中早有研究，但近期才被引入MARL理论。本文与之的区别在于，首次系统性地将其作为归纳偏置应用于协作游戏，证明其不仅能设计上保证对伙伴行为偏差的鲁棒性，还能减少搭便车现象，并在均衡结果上优于传统博弈概念（如纳什均衡）。

本文方法区别于上述工作：它将战略风险规避作为原则性框架集成到策略优化中，既保持了计算效率（作为现有方法的简单改进），又基于博弈论提供理论保证，在多个协作基准测试中实现了对异构未知伙伴的稳定协作。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“战略风险规避”的归纳偏置，并基于此设计了一种新的多智能体强化学习算法SRPO，来解决协作智能体在面对新伙伴时策略脆弱、泛化性差的问题。核心方法是：将每个智能体的目标从最大化自身期望回报，转变为最大化其“战略风险规避效用”，该效用考虑了伙伴策略可能的最差偏离，从而鼓励智能体学习对伙伴行为变化更稳健的策略。

整体框架基于策略优化算法，特别是独立PPO。主要创新在于引入了一个辅助的对抗性游戏来高效近似战略风险规避目标。具体地，为每个智能体i引入一个对抗者，其策略为φ_i。智能体i的目标是最大化其标准PPO目标（但伙伴策略替换为对抗者策略），即L_i^CLIP(θ_i, φ_i)加上熵正则项。而对抗者的目标则是最小化智能体i的回报，同时受到一个KL散度项约束，惩罚其过度偏离其他智能体当前策略θ_{-i}。这个KL约束是关键设计，它确保了对抗者的破坏性探索被限制在合理范围内，从而稳定了训练，避免了过度保守的策略。

因此，SRPO算法包含两个交替优化的模块：主智能体模块和对抗者模块。主智能体学习与一个“受限的最坏情况伙伴”协作，从而内在地提升了鲁棒性；对抗者模块则负责模拟这种受限的破坏性伙伴行为。这种架构使得训练出的策略既能抵抗伙伴的策略偏离，又减少了“搭便车”现象，因为智能体必须确保即使在伙伴不完美协作时也能达成目标。最终，算法通过标准的梯度下降进行优化，其计算复杂度和迭代结构与标准的独立PPO相近，易于实现和扩展。

### Q4: 论文做了哪些实验？

论文在四个协作环境中进行了实验，以验证所提出的SRPO算法的有效性。实验设置方面，将SRPO与基准算法IPPO进行对比，并确保两者与环境交互的次数相同，以进行公平比较。实验环境包括：(1) 修改的Overcooked网格世界，包含团队共享奖励和个体私有成本；(2) Tag连续控制协调任务；(3) 4玩家Hanabi（3颜色3等级），这是一个部分可观测的协作游戏；(4) 基于LLM的多智能体辩论任务，使用GSM8K数据集解决数学问题。

数据集/基准测试方面，主要评估了智能体与训练中未见过的新伙伴（held-out partners）进行协作的跨游戏性能（cross-play performance），以检验泛化能力。关键指标包括平均奖励、跨游戏性能与训练性能的差异（均值和标准差），以及自由骑行为（free-riding）的减少情况。

主要结果如下：在Overcooked中，IPPO收敛到自由骑均衡，导致跨游戏性能显著下降（平均奖励降低，标准差增大），而SRPO（τ=10, ε=0.1）避免了自由骑，获得了更高的效用和稳定的跨游戏性能。在Tag环境中，IPPO在训练中表现良好但存在自由骑，面对未见过的伙伴或对手时性能急剧下降；SRPO（τ=10, ε=0.01）训练性能略低，但跨游戏性能更稳定且更高。在Hanabi中，通过策略共享（policy sharing）将SRPO扩展到多智能体，SRPO（τ=0.01, ε=0.001）比IPPO表现出更稳健的跨游戏性能。在LLM辩论任务中，SRPO在协作推理中展现了更好的鲁棒性。消融实验表明，随着战略风险规避参数τ的增加，自由骑行为消失，协作稳定性提高，且SRPO对τ的选择具有鲁棒性。

### Q5: 有什么可以进一步探索的点？

这篇论文提出了通过战略风险厌恶来训练泛化性协作智能体的方法，但仍有几个值得深入探索的方向。首先，论文主要关注完全协作环境，未来可研究混合动机或部分冲突场景下战略风险厌恶的适用性，例如谈判或资源分配任务。其次，当前方法依赖于已知的博弈结构来计算风险厌恶策略，在复杂或未知动态环境中如何高效估算战略风险仍需探索，或许可结合元学习或对手建模来适应更广泛的伙伴行为分布。此外，实验虽涉及LLM协作任务，但未深入探讨如何将战略风险厌恶与大型语言模型的推理能力结合，未来可设计更复杂的语言协作基准，研究如何让LLM智能体主动评估伙伴偏离风险并调整协作策略。最后，论文未讨论计算效率问题，战略风险厌恶可能增加训练开销，未来需开发更轻量的近似算法，以扩展到大规模多智能体系统。

### Q6: 总结一下论文的主要内容

该论文针对协作多智能体系统中策略泛化性差的问题，提出将战略风险厌恶作为提升智能体与未见伙伴协作能力的归纳偏置。核心问题是现有方法训练的智能体容易过度适应特定伙伴，导致在遇到新伙伴时性能下降，并存在搭便车现象。论文从博弈论角度引入战略风险厌恶均衡概念，证明其在连续二次聚合博弈中能促进协作，在有限动作私有成本博弈中可减轻搭便车行为。方法上，作者设计了战略风险厌恶策略优化算法，将风险厌恶目标集成到标准策略优化框架中。实验表明，该方法在多个协作基准测试中均能实现与异构未见伙伴的可靠协作，性能优于现有基线，并初步验证了在大型语言模型智能体协作任务中的有效性。
