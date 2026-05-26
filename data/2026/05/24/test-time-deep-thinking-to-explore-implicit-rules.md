---
title: "Test-Time Deep Thinking to Explore Implicit Rules"
authors:
  - "Wentong Chen"
  - "Xin Cong"
  - "Zhong Zhang"
  - "Yaxi Lu"
  - "Siyuan Zhao"
  - "Yesai Wu"
  - "Qinyu Luo"
  - "Haotian Chen"
  - "Yankai Lin"
  - "Zhiyuan Liu"
  - "Maosong Sun"
date: "2026-05-24"
arxiv_id: "2605.24828"
arxiv_url: "https://arxiv.org/abs/2605.24828"
pdf_url: "https://arxiv.org/pdf/2605.24828v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "隐式规则推理"
  - "Test-Time 推理"
  - "强化学习训练"
  - "智能体规划"
relevance_score: 8.5
---

# Test-Time Deep Thinking to Explore Implicit Rules

## 原始摘要

With the continuous advancement of Large Language Models (LLMs), intelligent agents are becoming increasingly vital. However, these agents often fail in environments governed by implicit rules--hidden constraints that cannot be observed directly and must be inferred through interaction. This causes agents to fall into repetitive trial-and-error loops, ultimately leading to task failure. To address this challenge, we propose Test-Time Exploration (TTExplore), a framework where a thinker component analyzes interaction history to infer these implicit rules and guide an actor. Effective exploration in this setting critically depends on the reasoning ability of the thinker. However, evaluating deep reasoning trajectories is inherently unstable and difficult, which poses a major obstacle to effective training. To overcome this issue, we introduce a novel and stable reinforcement learning pipeline. The core idea is to use accurate task-level scores as indirect rewards to bypass the difficulty of evaluating intermediate reasoning, and to retain only a single thinking node per trajectory to alleviate reward sparsity. Using this pipeline, we train a specialized 7B model, Exp-Thinker. Experiments on five text-based embodied tasks show that TTExplore equipped with Exp-Thinker improves baseline agent performance by an average of $14$-$19$ points, demonstrating the effectiveness of explicitly reasoning about implicit rules.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的智能体在存在隐式规则的环境中频繁失败的问题。隐式规则是那些无法直接观察、必须通过与环境的交互来推断的隐藏约束。研究背景在于，当前主流方法（如ReAct、Reflexion）虽然通过提示工程或微调增强了智能体的规划与推理能力，但它们严重依赖与通用世界对齐的预训练知识，当面对反馈与内部假设矛盾、特别是存在不可观测约束的环境时，这些基于固定世界模型的方法会失效，导致智能体陷入重复试错的局部探索循环，最终任务失败。核心问题在于，现有方法缺乏一种在测试时通过深度思考来动态更新世界模型的原则性方式，无法让智能体在交互过程中主动推断并适应环境的隐式规则。为此，本文提出的TTExplore框架通过引入一个专门的“思考者”角色来分析交互历史、推断隐式规则并指导“行动者”制定计划，从而在测试时实现有效的探索。但训练这样的思考者面临巨大挑战：缺乏直接奖励信号来评估中间推理步骤的质量。为解决这一难点，论文提出了一种稳定的强化学习流水线，利用准确的任务级分数作为间接奖励，并保留每轮轨迹中只有一个思考节点来缓解奖励稀疏问题，从而成功训练出7B参数的Exp-Thinker模型。

### Q2: 有哪些相关研究？

相关研究可分为两类：一类是**训练导向方法**，如AgentTuning、FireAct、Agent-FLAN、AgentOhana和AgentBANK，通过收集环境和任务增强推理能力，但泛化性不足；AgentGen和AgentRefine通过合成任务或纠正轨迹提升泛化。另一类是**知识注入方法**，如ExpeL从失败轨迹提取规则，LWM、KnowAgent和KWM利用预知识库指导规划，KnowSelf让智能体主动获取环境知识，AgentRM使用外部奖励模型进行波束搜索。

本文与现有工作的核心区别是：现有方法依赖离线训练（暴露更多环境）或离线指导（预收集知识），均缺乏**测试时探索**能力。而TTExplore框架的**Thinker组件**在测试时通过分析交互历史动态推断隐式规则，模拟人类行为。此外，本文提出稳定强化学习管道，用任务级得分绕过中间推理评估难题，并保留单思考节点缓解奖励稀疏，这与AgentRM的奖励模型直接评分推理轨迹不同。实验表明，该方法显著提升了基线智能体在隐式规则环境中的表现。

### Q3: 论文如何解决这个问题？

本文提出测试时探索（TTExplore）框架来解决智能体在隐含规则环境中的探索失败问题。该框架的核心是将低级动作执行与高级策略推理解耦，通过两个角色实现：执行者（actor）和思考者（thinker）。执行者负责生成ReAct风格的逐步动作输出，而思考者在固定频率（如每n步）被触发，生成包含当前进展总结、隐含规则假设和未来修订计划的深度思考，并将其注入执行者的后续上下文。

整体框架包含四个关键模块：子任务划分、子任务过滤、滚动设置和奖励计算。在训练管线中，首先利用强模型将成功轨迹按过程分数划分为多个子任务，然后通过弱模型筛选出中等和困难难度的子任务（剔除简单子任务）。接着，利用弱模型产生的可能包含错误动作的轨迹构建上下文，促使思考者介入。之后，训练思考者针对同一历史轨迹生成m个深度思考，并使用冻结的执行者从每个思考节点继续执行最多(y-x)步，得到m条轨迹。

创新点主要体现在：采用间接评估策略，以任务级完成分数作为稳定奖励（提升则奖励1.0，否则0.0），避免了直接评估中间推理的不稳定性；在训练时每条轨迹仅保留一个思考节点，缓解了奖励稀疏问题，建立了清晰的因果判断；通过将成功的子任务划分、弱模型轨迹作为基础，构建了可控的训练环境。实验表明，基于此训练的专业7B模型Exp-Thinker在五项文本具身任务上平均提升基线智能体14-19个点，验证了显式推理隐含规则的有效性。

### Q4: 论文做了哪些实验？

论文在五个基于文本的具体任务（ALFworld、Sciworld、BabyAI、PDDL、Jericho）上进行了实验，使用过程分数（0-100）作为评估指标，并遵循AgentBoard的评估标准。实验将ReAct方法作为基线（无思考者），对比了大型模型（GPT-4o、Qwen2.5-72B）和微调智能体（Agent-FLAN、AgentGym、AgentRefine）。主要实验以LLaMA3-8B和Qwen2.5-7B作为执行者角色，使用专门训练的Exp-Thinker（基于Qwen2.5-7B，经过SFT+RL训练）作为思考者。结果显示，加入Exp-Thinker后，基线智能体性能平均提升14-19个点。例如，LLaMA3-8B在域内任务ALFworld上过程分数从32.15提升至63.49，Sciworld从20.31提升至55.43。对于已训练的Qwen2.5-Actor强智能体，在域外任务BabyAI上分数从50.62提升至60.25。消融实验表明，SFT+RL联合训练优于仅SFT或仅RL。思考者替换实验显示，Exp-Thinker（7B）性能匹敌甚至超越Qwen2.5-72B。量化探索行为分析显示，思考者显著提高了动作和观察多样性，降低了重复率。TTExplore在时间成本上略高于ReAct，但显著低于Reflexion方法。

### Q5: 有什么可以进一步探索的点？

该论文提出的TTExplore框架通过强化学习训练思考者来推断隐含规则，但仍存在几个可深入探索的方向。首先，当前训练依赖于任务级分数作为间接奖励，这可能导致思考轨迹与最终表现之间的因果关系不够精确，未来可设计更细粒度的过程奖励模型。其次，框架在文本环境上效果显著，但扩展到视觉或多模态环境时，隐含规则的表达和推理会更为复杂，需要设计跨模态的思考机制。第三，思考者模型仅固定使用7B参数，可研究在不同规模模型上的扩展性，以及是否可以通过知识蒸馏让小模型继承大模型的推理能力。此外，当前框架只保留单思考节点，未来可探索多步思考的奖励塑形或层级化思考结构，以平衡探索效率和计算成本。最后，在真实机器人任务中评估该框架的实用性，并研究如何将学到的隐含规则显式化存储，以实现跨任务的知识迁移。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型智能体在隐含规则环境中容易陷入反复试错循环的问题，提出了一种测试时深度思考框架TTExplore。核心思想是在智能体与环境交互过程中，引入一个专门的“思考者”组件，通过分析历史交互来推断环境中的隐含规则，并指导“行动者”制定合理计划。为了训练思考者的推理能力，作者设计了一种稳定的强化学习流水线，利用任务级稀疏奖励间接优化思考过程，并通过每个交互轨迹仅保留一个思考节点来缓解奖励稀疏问题，成功训练出7B参数的Exp-Thinker模型。在五个文本具身任务上的实验表明，TTExplore框架能将基线模型性能平均提升14-19个点，并能有效增强模型的跨领域泛化能力，显著缓解了重复行为和局部探索陷阱等常见问题。
