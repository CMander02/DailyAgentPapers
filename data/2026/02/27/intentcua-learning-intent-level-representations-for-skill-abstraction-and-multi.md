---
title: "IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents"
authors:
  - "Seoyoung Lee"
  - "Seobin Yoon"
  - "Seongbeen Lee"
  - "Yoojung Chun"
  - "Dayoung Park"
  - "Doyeon Kim"
  - "Joo Yong Sim"
date: "2026-02-19"
arxiv_id: "2602.17049"
arxiv_url: "https://arxiv.org/abs/2602.17049"
pdf_url: "https://arxiv.org/pdf/2602.17049v2"
categories:
  - "cs.AI"
  - "cs.HC"
  - "cs.RO"
tags:
  - "Multi-Agent System"
  - "Agent Architecture"
  - "Planning"
  - "Skill Abstraction"
  - "Memory"
  - "Long-Horizon Execution"
  - "Desktop Automation"
relevance_score: 9.0
---

# IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents

## 原始摘要

Computer-use agents operate over long horizons under noisy perception, multi-window contexts, evolving environment states. Existing approaches, from RL-based planners to trajectory retrieval, often drift from user intent and repeatedly solve routine subproblems, leading to error accumulation and inefficiency. We present IntentCUA, a multi-agent computer-use framework designed to stabilize long-horizon execution through intent-aligned plan memory. A Planner, Plan-Optimizer, and Critic coordinate over shared memory that abstracts raw interaction traces into multi-view intent representations and reusable skills. At runtime, intent prototypes retrieve subgroup-aligned skills and inject them into partial plans, reducing redundant re-planning and mitigating error propagation across desktop applications. In end-to-end evaluations, IntentCUA achieved a 74.83% task success rate with a Step Efficiency Ratio of 0.91, outperforming RL-based and trajectory-centric baselines. Ablations show that multi-view intent abstraction and shared plan memory jointly improve execution stability, with the cooperative multi-agent loop providing the largest gains on long-horizon tasks. These results highlight that system-level intent abstraction and memory-grounded coordination are key to reliable and efficient desktop automation in large, dynamic environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决计算机使用智能体（Computer-use agents）在复杂桌面环境中进行长时程任务规划时面临的稳定性与效率问题。研究背景是，随着大语言模型（LLMs）的发展，GUI智能体在网页、移动端等环境的应用迅速扩展，但跨异构桌面应用（如涉及多窗口操作、系统快捷键和API）的鲁棒、长时程自动化仍是一个突出挑战。

现有方法，无论是基于强化学习的规划器还是轨迹检索方法，都存在明显不足。它们的主要缺陷体现在两方面：一是生成的计划在跨越多个子步骤时容易偏离用户原始意图，并会重复解决已完成的常规子问题；二是局部的感知错误会不断累积，导致级联式的重试。这些因素共同导致智能体陷入低效、重复的重新规划循环，行动常因上下文漂移而被重试或无效化，最终造成任务延迟长、完成率不稳定。

因此，本文要解决的核心问题是：如何设计一个框架，能够稳定、高效地执行长时程的桌面自动化任务，克服意图漂移和冗余重新规划。为此，论文提出了IntentCUA，一个多智能体计算机使用框架。其核心思路是通过“意图对齐的计划记忆”来稳定长时程执行。具体而言，该方法将原始用户交互轨迹抽象为多视图的意图表示和可重用的技能，并将其分层组织在共享的计划记忆中。在运行时，通过意图原型检索与子群对齐的技能，并将其注入到部分计划中，从而减少冗余的重新规划，并缓解跨桌面应用的错误传播。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，现有工作主要围绕强化学习规划器、轨迹检索与微调，以及记忆与技能抽象展开。本文与强化学习规划器（如离线强化学习）和轨迹检索方法（如基于大规模轨迹调优的AppAgentv2、AgentBank）都旨在提升长程执行的稳定性，但区别在于本文强调通过多视图意图抽象来结构化地捕捉用户意图，而非依赖原始轨迹回放或显式奖励信号，从而减少冗余重规划和错误累积。在记忆与技能抽象方面，相关工作如Reflexion、Conversational Memory通过检索历史轨迹或手册来辅助决策，SkillAct和UFO²则探索了技能级提示或应用特定演示的复用。本文与这些工作方向互补，但进一步提出了分层意图原型和共享计划内存，以实现跨异构桌面工作流的可迁移技能抽象，而现有方法通常在结构化意图表示和跨应用协调方面探索不足。

在**应用类**研究中，GUI自动化涵盖Web、移动和桌面领域。本文聚焦桌面环境，与Web智能体（如WebArena、WebVoyager）相比，桌面环境缺乏结构化DOM反馈，需处理跨应用协调和动态界面中断，因此本文针对长流程、噪声感知的桌面任务（如OSWorld基准）设计。近期桌面智能体（如UI-TARS、UFO、ScreenAgent）通过规划器-评判器循环增强视觉语言模型，但本文指出其仍存在意图漂移和冗余重规划问题，因此引入意图对齐的内存机制来提升稳定性。

在**评测类**研究中，大规模交互轨迹库（如OS-ATLAS）支持感知预训练，而意图识别（如从UI日志中学习）和表示学习（如Screen2Vec、Aria-UI）则致力于减少感知歧义。本文在此基础上，通过多视图意图表示整合环境、动作和描述信号，以学习意图级表征，从而更系统地进行技能抽象和多智能体规划。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为IntentCUA的多智能体框架来解决长时程任务执行中的意图漂移和重复规划问题。其核心方法是构建一个基于意图对齐计划记忆的协同系统，将原始交互轨迹抽象为可重用的技能，并通过多智能体协作来稳定执行。

整体框架由三个主要智能体模块组成：规划器（Planner）、计划优化器（Plan-Optimizer）和评论家（Critic），它们围绕一个共享的记忆系统进行协调。该共享记忆是架构的关键创新，它并不简单存储原始动作序列，而是通过多视图意图抽象技术，从原始交互轨迹中提取并存储高层次的意图表征和可复用的技能片段。这些意图表征形成了“意图原型”，用于在运行时进行高效检索。

在运行过程中，当面临新任务或子任务时，系统会从共享记忆中检索与当前子目标对齐的技能（即“子群对齐的技能”），并将其注入到部分计划中。这种方法避免了从零开始的重复规划，减少了冗余计算，并有效遏制了错误在跨桌面应用执行过程中的传播。多智能体协作环是另一大创新点：规划器生成初始计划，优化器利用记忆进行技能检索与注入以优化计划，评论家则评估计划与意图的一致性并提供反馈，形成闭环优化。

关键技术包括多视图意图抽象（从不同视角理解用户意图并形成紧凑表征）、基于意图原型的技能检索与注入机制，以及通过共享记忆实现的多智能体协同决策循环。这些设计共同作用，使得系统能在噪声感知和动态变化的环境下，保持执行与用户意图的对齐，提升长时程任务的鲁棒性和效率。

### Q4: 论文做了哪些实验？

实验设置方面，论文在包含Web、跨应用和本地应用场景的286个任务上评估了IntentCUA。对比方法选择了两种代表性的桌面GUI智能体：基于强化学习的视觉规划器UI-TARS-1.5和基于演示轨迹的自动化智能体UFO²。评估指标包括任务成功率、步骤效率比和任务执行延迟。

主要结果如下：IntentCUA在总体任务成功率上达到74.8%，显著优于UFO²（51.2%）和UI-TARS-1.5（38.8%）。在步骤效率比上，IntentCUA达到0.91，高于UI-TARS的0.85和UFO²的0.82。在延迟方面，IntentCUA平均每个任务耗时1.46分钟，远低于UFO²的6.63分钟和UI-TARS的9.82分钟。分析表明，随着任务步骤数增加，IntentCUA的成功率下降平缓（例如在20-25步时仍保持65.0%），而基线方法在超过20步后成功率急剧下降至20%以下。这些结果验证了IntentCUA通过意图抽象和共享记忆机制，在长序列任务中实现了更稳定、高效的规划。

### Q5: 有什么可以进一步探索的点？

该论文在意图抽象和多智能体规划方面取得了进展，但仍存在一些局限性和可探索的方向。首先，随着计划记忆库的扩展，检索效率可能波动，这提示需要研究更高效的记忆索引与检索机制，例如引入图神经网络或分层索引结构来管理不断增长的技能库。其次，系统对动态和视觉变化界面的适应性仍有提升空间，未来可探索结合轻量级视觉提示或增量学习，使智能体能更鲁棒地处理界面布局的实时变化。此外，当前的意图表示可能尚未充分捕捉用户的高层目标语义，未来可引入更细粒度的意图分解或与大型语言模型结合，以生成更精准的技能抽象。最后，多智能体协作机制虽已带来增益，但其协调策略仍较固定，可探索引入自适应协商或元学习，使Planner、Optimizer和Critic能根据任务复杂度动态调整协作方式，进一步提升长视野任务下的执行稳定性与泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了IntentCUA框架，旨在解决计算机使用代理在长时程、多窗口动态环境中执行任务时，因意图偏离和重复解决常规子问题导致的错误累积与效率低下问题。其核心贡献是设计了一个基于意图对齐计划记忆的多智能体框架，通过抽象交互轨迹为多视图意图表示和可复用技能来稳定长时程执行。

方法上，框架包含规划器、优化器和评估器三个智能体，它们基于共享记忆进行协同。该记忆将原始交互轨迹抽象为多视图意图表示（如目标、动作序列、状态变化），并从中提取可重用技能。在运行时，系统通过意图原型检索与子目标对齐的技能，并将其注入部分计划中，从而减少冗余重规划并抑制错误在跨应用间的传播。

主要结论显示，在端到端评估中，IntentCUA实现了74.83%的任务成功率和0.91的步骤效率比，优于基于强化学习和轨迹检索的基线方法。消融实验表明，多视图意图抽象和共享计划记忆共同提升了执行稳定性，而协作式多智能体循环对长时程任务的增益最大。这证明了系统级的意图抽象和基于记忆的协调是实现大规模动态环境下可靠、高效桌面自动化的关键。
