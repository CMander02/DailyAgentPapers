---
title: "Environment-Grounded Automated Prompt Optimization for LLM Game Agents"
authors:
  - "Rean Clive Fernandes"
  - "Lukas Fehring"
  - "Theresa Eimer"
  - "Marius Lindauer"
  - "Matthias Feurer"
date: "2026-06-16"
arxiv_id: "2606.17838"
arxiv_url: "https://arxiv.org/abs/2606.17838"
pdf_url: "https://arxiv.org/pdf/2606.17838v1"
categories:
  - "cs.CL"
tags:
  - "Prompt Optimization"
  - "Multi-Agent"
  - "LLM Agent"
  - "Game Agent"
  - "Evolutionary Optimization"
  - "Goal-Conditioned Agent"
relevance_score: 8.5
---

# Environment-Grounded Automated Prompt Optimization for LLM Game Agents

## 原始摘要

LLM agents in interactive environments are highly sensitive to their prompts, yet prompt engineering remains a manual, task-specific process. We introduce an automated prompt optimization framework for LLM agents that decomposes the observation-to-action pipeline into a goal-conditioned descriptor agent and an action selection agent, and iteratively refines each module's prompt through an LLM-driven evolutionary loop guided by environment returns. We propose a behavior analyzer to attribute episode outcomes to specific prompt components, and a mutator to propose targeted revisions to the prompt, before validating them through environment rollouts. We evaluate on all five BabyAI tasks in the BALROG benchmark, comparing our pipeline against BALROG's RobustCoTAgent under both plain and guided prompt initializations. Optimization improves performance consistently across tasks and conditions, without requiring updates to the model weights. On PutNext, a multi-step coordination task where the RobustCoTAgent achieves 0% success, our framework reaches up to 72.5% success rate using the same underlying LLM with optimized prompts. These results suggest that a multi-agent framework, combined with automatic prompt optimization, enhances LLMs without the need for fine-tuning or extensive human supervision.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在交互式环境中的提示工程高度依赖人工且缺乏泛化能力的问题。研究背景设定在游戏AI领域，将LLM作为具身智能体的推理引擎，而现有方法存在明显不足：一方面，人工设计任务特定的提示词极为繁琐，且需要针对每个新领域重新调整；另一方面，单一智能体架构（即一个智能体同时处理状态解析、策略制定和动作选择）性能有限，尤其在需要长期规划和空间理解的复杂任务中表现不佳，难以达到人类水平，甚至不及领域专用的强化学习方案。这些方法的共同局限在于需要大量人工干预或以模型权重更新为代价。本文创新性地提出一个自动化的提示优化框架，核心解决两个关键问题：一是通过将观察到动作的过程分解为“描述智能体”（专注于状态信息提取）和“动作选择智能体”（负责决策）的多智能体架构，降低单一智能体的负担；二是利用环境回报驱动的进化算法自动迭代优化两个子智能体的提示词，从而无需人工编写提示或微调模型权重，即可显著提升LLM智能体在复杂任务（如BabyAI基准中多步协调任务PutNext）上的成功率。

### Q2: 有哪些相关研究？

相关研究主要分为四类:

1. **LLM智能体架构**：与本文的分解式管线设计紧密相关的工作包括将智能体分解为规划器-执行器-报告器框架的研究，以及分离记忆与技能组件的方法。这些工作与本文的关键区别在于，它们专注于架构本身的最优设计，而本文在此基础上集成了自动化提示优化，并强调该方法在原则上是正交的，可兼容多种现有架构。

2. **自动化提示优化**：典型工作包括APE（自动基于性能指标优化提示）、APO/ProTeGi（引入文本梯度分析失败案例）、OPRO（将LLM视为黑盒优化器）和GEPA（反思性提示进化）。与这些方法在固定数据集上评估不同，本文用环境奖励替换静态数据集作为优化信号，解决了非平稳环境下的过拟合问题。RePrompt虽使用LLM生成即时奖励，但仅限于非交互式设置。

3. **面向LLM智能体的提示优化**：本文特别关注失败归因方法，如AgentTracer通过定义决定性错误实现多智能体系统归因，这直接启发了本文的行为分析器模块。其他工作通过从经验中提取规则来改进未来交互，但本文认为经过优化的提示更具灵活性。

4. **评测与应用**：本文在BabyAI任务上评估，与BALROG基准中的RobustCoTAgent对比。与其他在固定数据集上权衡的方法不同，本文利用环境返回作为真实反馈信号，展示了从0%到72.5%的成功率提升。

### Q3: 论文如何解决这个问题？

该论文提出了一种基于环境奖励驱动的自动提示优化框架（RAPOA），用于优化LLM游戏智能体的提示，无需微调模型权重或大量人工监督。核心是将观察到动作的流水线分解为目标条件的描述智能体（Descriptor Agent）和动作选择智能体（Action Selection Agent），每个智能体都有自己的提示。整体框架分为两个阶段：第一阶段，智能体与基于文本的环境形成标准强化学习循环，收集轨迹数据；第二阶段，优化器评估聚合的回合数据，识别失败案例和低效行为，并构建修正后的提示。

关键技术包括行为分析器和变异器。行为分析器对收集到的轨迹数据进行关键分析，根据严重性排序生成一个有序列表，每个元素包含导致特定行为的子智能体、原因描述以及针对该行为的提示修改建议。变异器则根据这些建议迭代地调整子智能体的提示。变异后的提示需通过两阶段接受测试：首先在优化种子上评估，要求平均性能超过当前提示一个阈值δ；然后在保留种子上再次评估，确保泛化能力。该框架采用低选择压力（LSP）或高选择压力（HSP）策略来控制接受的严格程度。

创新点在于：1）将智能体架构拆分为描述和动作两个模块，实现目标条件化的感知-动作分离；2）利用LLM驱动进化循环，通过环境返回自动迭代优化提示；3）行为分析器能归因回合结果到具体提示组件，实现定向修改。在BabyAI任务上，该方法在PutNext任务上将成功率从0%提升至72.5%，证明了多智能体框架与自动提示优化结合的有效性。

### Q4: 论文做了哪些实验？

论文在BALROG基准测试的五个BabyAI任务（GoTo、PickUp、Open、PutNext、PickUpSeqGoTo）上进行了实验。环境为部分可观测的网格世界，任务难度从单步导航（GoTo）到多步物体协调（PutNext、PickUpSeqGoTo）不等。评估使用20个环境种子和6个推理种子，共120轮，以成功率（成功时奖励R=1，失败R=0，步折扣0.9）和平均步数为指标。对比方法为BALROG的RobustCoTAgent（单智能体基线），并在两种提示初始化（Guided和Plain）下比较。主要结果：SPA框架优化后性能持续提升。例如，在PutNext任务上，RobustCoTAgent成功率为0%，而SPA通过优化提示达到最高72.5%的成功率。在所有任务中，SPA的Guided提示优化将平均成功率从65.5%提升至79.2%，Plain提示从59.8%提升至62.2%。BALROG同样受益，从29.3%提升至49.0%。优化在困难任务上效果显著，如Open从54.2%提升至62.5%。此外，实验分析了接受阈值δ的影响：要求性能改进时，突变稀疏但性能单调增长；全部接受则提示漂移，导致峰值性能下降。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向如下：当前方法仅验证了单一游戏环境和GPT-4o模型，未来需扩展至多种环境（如Minecraft、WebShop）和不同规模的语言模型，以检验框架泛化能力。其次，行为分析器依赖回合级归因，可引入更细粒度的token级因果分析或记忆增强机制，提升对长链推理错误的定位精度。当前采用单候选提示迭代，易陷入局部最优，可尝试种群进化策略（如交叉变异、多样性筛选）并引入元提示作为遗传模板。此外，框架未整合长期规划模块，未来可结合规划反馈来指导提示突变方向。最后，程序化生成环境的无限状态特性为提示优化提供了低污染的测试平台，值得深入探索其如何用于自动发现通用的任务描述范式。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向LLM游戏智能体的环境驱动自动提示优化框架。针对LLM智能体在交互环境中对提示高度敏感但提示工程依赖人工且任务特定的问题，该框架将观察到动作的流程分解为基于目标的描述智能体和动作选择智能体，通过LLM驱动的进化循环，利用环境反馈迭代优化每个模块的提示。其核心创新在于设计了行为分析器将回合结果归因于特定提示组件，以及变异器提出针对性修订方案，并通过环境推演验证。在BALROG基准的五个BabyAI任务上进行评估，无论使用普通还是引导式提示初始化，优化均能显著提升性能。在PutNext任务中，原始RobustCoTAgent成功率为0%，而优化后可达72.5%。该研究表明，多智能体框架结合自动提示优化，无需微调或大量人工监督即可增强LLM能力，为提升交互式环境下LLM智能体的泛化性和效率提供了有效方案。
