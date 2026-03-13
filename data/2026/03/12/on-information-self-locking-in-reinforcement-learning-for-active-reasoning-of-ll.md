---
title: "On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM agents"
authors:
  - "Deyu Zou"
  - "Yongqiang Chen"
  - "Fan Feng"
  - "Mufei Li"
  - "Pan Li"
  - "Yu Gong"
  - "James Cheng"
date: "2026-03-12"
arxiv_id: "2603.12109"
arxiv_url: "https://arxiv.org/abs/2603.12109"
pdf_url: "https://arxiv.org/pdf/2603.12109v1"
categories:
  - "cs.AI"
tags:
  - "强化学习"
  - "主动推理"
  - "信息探索"
  - "学习信号重分配"
  - "LLM Agent 训练"
  - "信念跟踪"
  - "动作选择"
relevance_score: 8.5
---

# On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM agents

## 原始摘要

Reinforcement learning (RL) with outcome-based rewards has achieved significant success in training large language model (LLM) agents for complex reasoning tasks. However, in active reasoning where agents need to strategically ask questions to acquire task-relevant information, we find that LLM agents trained with RL often suffer from information self-locking: the agent ceases to ask informative questions and struggles to internalize already-obtained information. To understand the phenomenon, we decompose active reasoning into two core capabilities: Action Selection (AS), which determines the observation stream through queries, and Belief Tracking (BT), which updates the agent's belief based on collected evidence. We show that deficient AS and BT capabilities will limit the information exploration during RL training. Furthermore, insufficient exploration in turn hinders the improvement of AS and BT, creating a feedback loop that locks the agent in a low-information regime. To resolve the issue, we propose a simple yet effective approach that reallocates the learning signal by injecting easy- to-obtain directional critiques to help the agent escape self-locking. Extensive experiments with 7 datasets show that our approach significantly mitigates the information self-locking, bringing up to 60% improvements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在进行多轮主动推理任务时，使用基于结果奖励的强化学习（RL）训练所遭遇的“信息自锁”问题。

**研究背景**：基于结果奖励的RL在训练LLM智能体执行复杂推理任务方面取得了显著成功。在主动推理场景中，智能体需要与环境交互，通过策略性地提问来获取任务所需的缺失信息（例如，面对模糊的用户查询）。然而，现有的基于结果奖励的RL方法在这种多轮交互的主动推理任务中存在明显不足。

**现有方法的不足**：论文发现，使用传统RL训练的LLM智能体经常陷入“信息自锁”状态。具体表现为：智能体停止提出有信息量的新问题，并且难以有效吸收和利用已经获得的信息。这导致智能体被困在一种低信息交互模式中，无法通过探索获取足够信息来提升任务表现。作者将主动推理分解为两个核心能力：**行动选择**（决定问什么问题以获取信息流）和**信念跟踪**（根据收集到的证据更新内部信念状态）。现有RL方法的问题在于，这两种能力在训练中无法得到有效协同提升，反而形成了一个负向反馈循环：低效的信念跟踪会掩盖有价值提问的贡献，导致信用分配错乱；而保守的行动选择又限制了可用于改进信念跟踪的信息预算，最终两者相互制约，使智能体锁定在低性能状态。

**本文要解决的核心问题**：因此，本文的核心研究问题是：为什么在主动推理的RL训练中会发生“信息自锁”现象，以及如何缓解它？论文不仅通过实证分析揭示了这一现象，还建立了理论框架来解释其成因，并最终提出了一种解决方案来打破这种自锁循环，旨在从根本上改善智能体在主动推理中的探索能力和信息利用效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于强化学习（RL）的大语言模型（LLM）智能体训练、主动推理任务中的信息获取策略，以及智能体失败模式的分析与缓解方法。这些工作可分为以下几类：

**1. 基于RL的LLM智能体训练方法**：已有大量研究利用基于结果的奖励（outcome-based rewards）通过RL训练LLM智能体，以提升其在复杂推理任务中的表现（如Zhang et al., 2025; Plaat et al., 2025）。这些工作通常关注单轮或多轮交互任务，但较少深入探讨在主动推理（active reasoning）中，智能体需通过策略性提问获取信息时出现的训练动态问题。

**2. 主动推理与信息获取策略**：在需要多轮交互的主动推理任务中，相关研究侧重于设计智能体的提问策略以高效收集信息。然而，这些工作往往假设智能体能有效内化已获信息（即信念跟踪），并未系统分析当行动选择（AS）与信念跟踪（BT）能力不足时，两者如何相互制约导致训练停滞。

**3. 智能体失败模式与探索问题**：部分研究指出了现实世界中智能体的失败模式，例如探索不足或信用分配（credit assignment）困难。本文与这些工作的关系在于，它具体揭示了在主动推理场景下，AS和BT的缺陷会共同导致“信息自锁”（information self-locking）现象，即智能体停止提出信息性问题且难以利用已有证据。这与一般RL中探索不足的问题有联系，但本文更聚焦于AS与BT在动态训练中的耦合效应。

**4. 训练信号增强方法**：为改善RL训练，已有工作尝试引入额外奖励或课程学习。本文提出的方法（PROJ）与这类研究相关，但区别在于它并非直接修改奖励函数，而是利用易于获取的方向性评判（directional critiques）重新加权优势函数，从而在自锁状态下提供稳定学习信号，针对性破解AS与BT的负向循环。

总之，本文在已有RL训练LLM智能体的基础上，深入分析了主动推理中特有的信息自锁问题，并通过理论建模与轻量级干预方法，弥补了现有工作在训练动态与能力耦合分析上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“方向性批判注入”的方法来解决信息自锁问题。该方法的核心思想是利用易于获取的方向性信号，对智能体的行为进行局部、定向的引导，从而打破行动选择与信念追踪能力之间相互制约的负反馈循环。

整体框架建立在将主动推理过程分解为两个交替进行的核心模块之上：**行动选择**负责生成查询以获取信息，**信念追踪**负责根据收集到的证据更新内部信念状态。为了解决这两个模块在强化学习训练中因探索不足而陷入的僵局，论文设计了一个轻量级的辅助训练目标。

该方法的关键技术与创新点在于：
1.  **方向性批判的构建**：针对AS模块，根据查询是否从环境或用户处引出了新的、有帮助的反馈，为每个查询分配一个标量批判值（+1表示信息丰富，-1表示无信息，0表示弃权）。针对BT模块，通过一个可观测的置信度读数（如通过提示获得的任务相关置信度）的变化方向来定义批判值，以指示智能体是否成功地将新信息整合到了其内部状态中。
2.  **基于轨迹内似然边际的辅助目标**：设计了一个不依赖于中间奖励或额外判别器的辅助损失函数。该函数计算同一轨迹中所有被正向批判的决策的对数概率均值与所有被负向批判的决策的对数概率均值之差。这直接鼓励模型增加对优质决策的偏好，同时抑制不良决策，且其梯度形式与标准策略梯度兼容。
3.  **最小化修改的优势函数重加权**：该方法仅对强化学习算法（如PPO）中优势函数的计算进行了最小程度的修改。具体而言，将根据辅助目标推导出的、符号与批判方向一致的系数，乘以一个强度超参数后，直接加到原始的优势值上。这实质上是在同一轨迹内，根据方向性批判的指导，将策略梯度的更新幅度从负向步骤“重新分配”到正向步骤，从而实现了学习信号的重定向。

实验结果表明，单独使用AS批判或结合使用AS与BT批判，都能显著提升多个基准任务上的最终结果奖励，最高提升达60%以上，有效缓解了信息自锁，证明了该方法的有效性。

### Q4: 论文做了哪些实验？

论文在偏好估计（PE-G、PE-F）和医学诊断（MediQ）两个交互式基准测试上进行了实验。实验设置将主动推理建模为部分可观测马尔可夫决策过程（POMDP），通过强化学习训练LLM智能体，并引入了行动选择（AS）和信念跟踪（BT）两个代理指标来细粒度追踪行为。数据集包括7个不同的任务。对比方法主要基于使用结果奖励的标准RL训练。

主要结果揭示了信息自锁现象：尽管回合奖励随训练提升，但AS能力未能改善甚至下降，BT能力提升有限。关键数据显示，在MediQ任务中，当用“未知”替换所有患者反馈时，RL训练后的性能下降更小（从61.00降至55.50，而未经RL训练时从41.25降至30.50），同时信念一致性从78.7提升至92.8，表明智能体对交互证据的依赖减弱，变得更加“固执”。分析表明，弱的BT掩盖了信息性行动的贡献，而保守的AS则限制了信念更新，两者形成负反馈循环，导致智能体陷入低信息探索状态。最终，论文提出的注入定向批评的方法有效缓解了自锁，带来了高达60%的性能提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的方法通过引入方向性评判来缓解信息自锁，但仍存在一些局限性和值得探索的方向。首先，其评判信号（如查询是否带来新证据）的获取依赖于环境或用户的明确反馈，这在开放域或交互成本高的场景中可能难以实现。未来可探索如何从更隐式的反馈（如用户响应时间、部分信息）中自动生成可靠的评判信号。其次，方法主要针对动作选择（AS）和信念跟踪（BT）的分离优化，但两者在复杂任务中可能更紧密耦合；可研究更动态的联合训练机制，例如引入元学习来调整AS和BT的协作策略。此外，实验基于特定任务和模型规模，其泛化性需在更广泛的基座模型（如更大参数或多模态模型）和任务（如长期规划、多智能体协作）中验证。最后，当前方法依赖于强化学习框架，训练稳定性与采样效率仍有提升空间；结合世界模型或因果推理来预训练AS/BT模块，或许能进一步打破自锁循环并提升样本效率。

### Q6: 总结一下论文的主要内容

该论文研究了在基于强化学习（RL）训练的大型语言模型（LLM）智能体进行主动推理时出现的“信息自锁”问题。在主动推理任务中，智能体需要通过策略性提问来获取任务相关信息，但研究发现，使用基于结果的奖励进行RL训练的智能体常会过早停止提出信息性问题，并难以有效内化已获得的信息，导致性能受限。

论文的核心贡献在于将主动推理分解为两个核心能力：行动选择（决定提问策略以获取观察流）和信念跟踪（基于收集的证据更新内部信念）。作者指出，这两方面能力的不足会限制RL训练期间的信息探索，而探索不足反过来又阻碍了这两项能力的提升，从而形成一个使智能体陷入低信息状态的恶性循环。

为解决此问题，论文提出了一种简单有效的方法：通过注入易于获取的方向性评判来重新分配学习信号，帮助智能体打破自锁循环。该方法在7个数据集上的实验表明，能显著缓解信息自锁问题，带来最高达60%的性能提升。这项研究揭示了RL训练LLM智能体在主动推理中的内在挑战，并为改进其探索与学习效率提供了新的思路。
