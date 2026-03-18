---
title: "Adaptive Theory of Mind for LLM-based Multi-Agent Coordination"
authors:
  - "Chunjiang Mu"
  - "Ya Zeng"
  - "Qiaosheng Zhang"
  - "Kun Shao"
  - "Chen Chu"
  - "Hao Guo"
  - "Danyang Jia"
  - "Zhen Wang"
  - "Shuyue Hu"
date: "2026-03-17"
arxiv_id: "2603.16264"
arxiv_url: "https://arxiv.org/abs/2603.16264"
pdf_url: "https://arxiv.org/pdf/2603.16264v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Theory of Mind"
  - "Reasoning"
  - "Coordination"
  - "Adaptive Agent"
  - "LLM-based Agent"
relevance_score: 8.5
---

# Adaptive Theory of Mind for LLM-based Multi-Agent Coordination

## 原始摘要

Theory of Mind (ToM) refers to the ability to reason about others' mental states, and higher-order ToM involves considering that others also possess their own ToM. Equipping large language model (LLM)-driven agents with ToM has long been considered to improve their coordination in multiagent collaborative tasks. However, we find that misaligned ToM orders-mismatches in the depth of ToM reasoning between agents-can lead to insufficient or excessive reasoning about others, thereby impairing their coordination. To address this issue, we design an adaptive ToM (A-ToM) agent, which can align in ToM orders with its partner. Based on prior interactions, the agent estimates the partner's likely ToM order and leverages this estimation to predict the partner's action, thereby facilitating behavioral coordination. We conduct empirical evaluations on four multi-agent coordination tasks: a repeated matrix game, two grid navigation tasks and an Overcooked task. The results validate our findings on ToM alignment and demonstrate the effectiveness of our A-ToM agent. Furthermore, we discuss the generalizability of our A-ToM to non-LLM-based agents, as well as what would diminish the importance of ToM alignment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体在协作任务中，由于心智理论（Theory of Mind, ToM）推理层级不匹配（即不对齐）所导致的协调失效问题。

研究背景是，多智能体协调（如自动驾驶、群体机器人）常面临零样本协调的挑战，即智能体需与未经共同训练的新伙伴协作。LLM因其强大的决策和泛化能力，被广泛用于构建此类零样本协调智能体。为了预测并适应伙伴行为，近期研究将显式的ToM（即推断他人信念、意图等心理状态的能力）乃至高阶ToM（考虑他人也拥有ToM）引入LLM智能体架构，并显示出积极效果。

然而，现有方法存在不足。研究发现，更高的ToM阶数并不总能提升性能，以往工作将其归因于LLM进行高阶ToM推理的能力有限，或高阶ToM本身引入了过度推理。本文指出一个更深层的原因：智能体之间的ToM阶数错配。根据定义，一个k阶ToM的智能体与(k-1)阶或(k+1)阶伙伴协调最佳；否则，错配会导致对伙伴的推理不足（如高阶对低阶）或过度（如低阶对高阶），从而损害协调。例如，两辆相向而行的汽车若都基于相同的一阶ToM（“我认为你会避让”）而采取相同避让动作，仍可能导致事故。

因此，本文要解决的核心问题是：如何让LLM驱动的智能体能够适应性地与不同ToM阶数的伙伴对齐，以实现稳健的零样本协调。为此，论文提出了首个自适应ToM（A-ToM）智能体。它通过历史交互实时估计伙伴可能的ToM阶数，并利用该估计预测伙伴行动，进而选择能与之协调的自身行动，从而解决因ToM阶数不对齐而引发的协调障碍。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及方法类和应用类研究。在方法类方面，现有研究已为基于大语言模型（LLM）的智能体配备了感知、记忆和控制等模块，使其能够在机器人控制、工业自动化、图形用户界面操作和开放世界游戏等多个领域成功执行复杂任务。这些智能体在单智能体和多智能体任务中均展现出可靠的决策能力，为本文研究理性协作者之间的心理理论（ToM）对齐影响提供了基础。此外，LLM智能体因其强大的泛化能力，无需为每个任务从头设计决策规则或训练模型，这为本文的实证评估提供了便利。

在应用类方面，心理理论作为人类推理他人信念、欲望和意图的能力，已被引入多智能体协作中，以提升智能体间的沟通效率、克服环境部分可观测性挑战并改善协调效果。先前研究探索了为AI智能体（包括LLM智能体）显式配备ToM，使其能够推断他人隐藏状态并预测行为。然而，也有研究表明，为智能体配备高阶ToM并不总能带来预期改进，这揭示了ToM深度可能存在的匹配问题。本文直接受到两项关键研究的启发：一是推断他人ToM状态的工作，二是为具有特定ToM层级的智能体动态匹配伙伴的研究。与这些工作不同，本文重点关注ToM层级错位（即智能体间ToM推理深度不匹配）对协作的负面影响，并提出了自适应ToM（A-ToM）智能体来解决对齐问题，通过估计伙伴的ToM层级来预测其行为，从而促进协调。本文通过矩阵游戏、网格导航和《Overcooked》等任务验证了ToM对齐的重要性及A-ToM的有效性，进一步拓展了ToM在LLM智能体协作中的应用边界。

### Q3: 论文如何解决这个问题？

论文通过设计一种自适应心智理论（A-ToM）智能体来解决多智能体协作中因心智理论推理深度不匹配（即ToM阶数错位）导致的协调失效问题。其核心方法是让智能体能够在线估计并适应其合作伙伴的ToM阶数，从而实现阶数对齐，提升协作效率。

整体框架基于一个完全合作的马尔可夫决策过程。智能体被建模为具有不同ToM阶数的策略执行者：ToM-0智能体将伙伴视为环境的一部分，仅基于状态决策；ToM-1智能体假设伙伴是ToM-0，并预测其行动后做出最佳响应；ToM-2智能体则假设伙伴是ToM-1，并递归推理伙伴对自己的预测。论文聚焦于k≤2的阶数，因为更高阶推理负担过重且人类通常也止步于此。

A-ToM智能体的架构设计包含几个关键模块：1）状态编码模块，将结构化环境状态转换为自然语言描述；2）ToM模块，用于预测伙伴行动，其创新点在于集成了三个假设的伙伴模型（ToM-0, ToM-1, ToM-2）；3）决策模块，结合状态描述和预测的伙伴行动，输出自身行动；4）动作控制器，将LLM输出的自然语言动作转换为环境可执行动作。

其关键技术在于将ToM阶数对齐问题形式化为一个在线专家建议问题。A-ToM智能体将每个ToM-k策略视为一个“专家”，并维护其累积损失（或权重）。在每次交互中：首先，使用每个假设的伙伴模型生成候选的伙伴行动预测；接着，根据历史预测准确率（通过专家权重体现）选择一个预测作为最终的伙伴行动预测；然后，基于此预测选择协调行动；最后，观察伙伴真实行动，更新各假设模型的预测准确率（即更新专家权重）。论文实现了两种在线学习算法来管理权重更新：Follow-the-Leader（FTL）和Hedge。FTL在伙伴ToM阶数固定的稳定环境中具有对数遗憾界，而Hedge通过维护专家权重的概率分布，能更好地处理不确定性和非平稳行为，其最坏情况遗憾界为O(√(T log N))。

这种方法的核心创新点在于：1）将原始策略空间的协调问题转化为ToM阶数空间的对齐问题，降低了协调的维度和结构复杂性；2）利用LLM的推理能力，让其在与其优势匹配的抽象阶数层面进行学习，而非纠缠于底层细节；3）通过在线学习动态适应伙伴的推理模式，实现了灵活有效的协调。实验在重复矩阵博弈、网格导航和Overcooked等任务中验证了ToM对齐的重要性以及A-ToM智能体的有效性。

### Q4: 论文做了哪些实验？

该论文在四个多智能体协作任务上进行了实验验证。实验设置方面，所有实验均基于LLaMA-3.3-70B-Instruct模型，温度参数设为0.1，每个配置独立重复30次，随机种子固定为42。实验环境包括：1）重复矩阵博弈，智能体需在无通信下通过选择A或B来最大化奖励（不同选择各得5分），分为仅记忆上一轮动作的Memory-1和记忆历史累计次数的Memory-N两种设置，每轮进行15步；2）两个网格世界导航任务（Game 1和Game 2），两个智能体需避开障碍并协调路径到达各自目标位置，Game 2因布局更窄而更具挑战性，最大步数为30；3）Overcooked烹饪场景，两个智能体需协作完成洋葱汤的烹饪与配送，布局完全对称以增加协调难度，最大步数为100。

对比方法上，主要评估了提出的自适应心智理论（A-ToM）智能体与固定ToM阶数（ToM-0、ToM-1、ToM-2）智能体之间的协作性能，并比较了A-ToM采用的两种在线学习算法：FTL（Follow-the-Leader）和Hedge。

主要结果与关键指标如下：在重复矩阵博弈中，ToM阶数对齐的智能体对（如ToM-0 vs ToM-0）在Memory-1设置下能获得最高75分的平均奖励，而错配（如ToM-1 vs ToM-1）会导致因“过度思考”而协调失败，得分较低；在Memory-N设置下，由于历史记忆的缓冲，错配对也能获得一定成功。在网格导航任务中，协调性能以完成任务的步数衡量（越低越好），例如在Game 2中，A-ToM与ToM-0智能体协作时平均步数为7.00（FTL算法），而与ToM-1协作时步数增加至10.53，表明对齐的重要性。在Overcooked任务中，A-ToM与ToM-0协作平均用时45.33步（FTL），与ToM-1协作用时增至52.17步。结果普遍显示，当智能体与伙伴的ToM阶数对齐时，协调性能最优；A-ToM智能体能有效估计并适应伙伴的ToM阶数，从而提升协作效率，其中FTL在应对固定阶数伙伴时略优，而Hedge在双A-ToM自对弈时因更强的探索能力表现更佳。

### Q5: 有什么可以进一步探索的点？

本文提出的自适应心智理论（A-ToM）虽然有效，但仍存在局限性和广阔的探索空间。首先，其评估主要基于相对简单的协作任务（如矩阵游戏、网格导航），在更复杂、开放或动态变化的多智能体环境中（如长期社会模拟、竞争与合作交织的场景）的有效性有待验证。其次，A-ToM 依赖于对伙伴 ToM 阶数的估计，这在面对策略复杂或故意欺骗的智能体时可能失效，未来可探索更鲁棒的对手建模方法，例如结合元学习或递归推理。此外，论文发现任务最优行动空间越模糊、智能体理性程度越低，ToM 对齐的重要性会下降，这提示未来研究需深入探讨 ToM 机制与其他协作范式（如显式通信、联合规划）的互补与替代关系。最后，当前方法基于 LLM 实现，计算成本较高，如何设计轻量级、可学习的 ToM 模块并将其集成到非 LLM 智能体（如强化学习智能体）中，是推动其实际应用的关键方向。

### Q6: 总结一下论文的主要内容

该论文探讨了在大语言模型驱动的多智能体协作中，心智理论（ToM）对齐的重要性。核心问题是：智能体间ToM推理深度的不匹配（即ToM阶数错位）会损害协作效果，而非简单地拥有ToM就能改善协调。为解决此问题，作者提出了一种自适应心智理论智能体（A-ToM）。该方法将ToM对齐视为专家建议问题，智能体通过先前的交互推断伙伴的ToM阶数，并据此预测对方行动，从而动态调整自身行为以实现协调。实验在重复矩阵博弈、网格导航和Overcooked等多个任务上验证了ToM错位确实会阻碍协作，而A-ToM智能体通过实现ToM阶数对齐，能有效提升协调性能。主要结论是：有效的协作关键在于智能体间ToM推理深度的对齐，而不仅仅是具备ToM能力；所提出的A-ToM架构能成功实现这种对齐，促进多智能体协作。
