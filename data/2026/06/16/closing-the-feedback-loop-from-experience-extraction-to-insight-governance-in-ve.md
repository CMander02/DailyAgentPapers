---
title: "Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning"
authors:
  - "Yanwei Cui"
  - "Xing Zhang"
  - "Yulong Zhang"
  - "Li Shao"
  - "Xiaofeng Shi"
  - "Guanghui Wang"
  - "Peiyang He"
date: "2026-06-16"
arxiv_id: "2606.17591"
arxiv_url: "https://arxiv.org/abs/2606.17591"
pdf_url: "https://arxiv.org/pdf/2606.17591v1"
categories:
  - "cs.AI"
tags:
  - "verbal reinforcement learning"
  - "LLM agent memory"
  - "non-stationary environments"
  - "insight governance"
  - "experience extraction"
  - "feedback-driven curation"
  - "financial forecasting agent"
relevance_score: 8.5
---

# Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning

## 原始摘要

Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic forgetting when conditions recur. We identify four requirements for navigating this dilemma -- outcome-driven evaluation, persistent structured evidence, non-monotonic knowledge lifecycle, and compositional governance -- and show that existing methods invest heavily in experience extraction while underinvesting in insight governance. We propose a three-layer architecture -- rules, evidence, and skills -- connected by a feedback-driven curation loop that closes the governance gap. Rules capture distilled experience from world outcomes; evidence logs track each rule's reliability across episodes; skills govern which rules to apply, how to resolve conflicts, and when to abstain. On financial forecasting as a case study, where world feedback is naturally abundant, noisy, and non-stationary, we show that the same accumulated experience either degrades performance below the zero-shot baseline or dramatically improves accuracy and risk-adjusted returns, depending on whether the curation loop is present.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决无参数训练的**语言模型智能体**在非平稳环境中学习时面临的核心矛盾：**“保留-遗忘困境”**。研究背景是，智能体可以从世界反馈中提取经验作为规则并注入上下文来改进行为，但非平稳环境（如金融市场）存在规律变化。现有方法（如反思积累、反思精炼等）存在以下不足：1）缺乏对存储知识持续的、基于结果驱动的评估（R1）；2）未建立跨回合、结构化的证据追踪（R2）；3）对知识采取“非删即留”的极端处理，无法实现非单调的生命周期管理（R3），即旧规则失效时无法去激活但保留证据；4）缺少组合治理能力（R4），无法解决规则间的冲突与取舍。现有方法过度注重“经验抽取”，而严重忽视了“洞见治理”。本文要解决的核心问题是：设计一套闭环反馈机制，通过规则、证据和技能三层架构，结合批评者、提议者和策展者三个角色的反馈驱动策展循环，实现对经验的有效评估、结构化追踪、非单调生命周期管理和组合治理，从而在非平稳环境下真正利用而非被经验所累。

### Q2: 有哪些相关研究？

本文的相关研究可归为三类：**方法类**包括Reflective accumulation、Reflective refinement、Trajectory-informed tips和Meta-MDP experience library，它们共同特点是侧重从世界反馈中提取经验（如错误反思、规则合并），但在治理环节普遍薄弱。本文通过对比揭示了这些方法在四项核心需求上的不足：多数方法仅部分满足R1（结果驱动评估），而R2（持久结构化证据）、R3（非单调知识生命周期）和R4（组合治理）存在严重缺失，例如Reflective accumulation保留所有经验导致负迁移，Reflective refinement的原地修改破坏证据链，Trajectory-informed tips缺少跨回合证据积累，Meta-MDP的经验库则因合并擦除来源轨迹。

**评测类**以SkillsBench为代表，它证实了技能质量（而非数量）和经验治理（如组合冲突处理）对静态任务的重要性，为本文动态场景下的治理需求提供印证。**基础设施类**包括Hindsight（意见网络追踪置信度，但缺乏证据溯源）、IMPACT-CYCLE（通过依赖图维护持久证据，但局限于单会话事实矫正）、AGM信念修正框架（提供知识生命周期的数学保证，如相关性公理）以及MemGPT（虚拟上下文管理）。本文与之区别在于：这些系统管理“记忆”，而本文的反馈驱动策展循环管理“信任”——通过连接世界结果与存储知识，动态评估、证据积累、审慎弃用和组合规则治理，从而在非平稳环境中实现经验利用与遗忘的平衡。

### Q3: 论文如何解决这个问题？

该论文提出一个三层架构（规则、证据、技能）配合反馈驱动的策展循环，以解决无训练语言强化学习中经验提取与知识治理的脱节问题。其核心创新在于设计了一套持久化、结构化的经验管理机制，而非像现有方法那样仅仅积累或重写规则。

整体框架由三个相互关联的模块组成：**规则层**用于存储从世界反馈中提取的触发条件和纠正动作；**证据层**为每条规则维护一个持久化的结构化日志，记录每次评估的回合、结果、条件及影响，即使规则被废弃，证据也永久保留，这避免了标量置信度分数丢失关键上下文；**技能层**作为治理层，基于跨规则证据决定哪些规则进入有限上下文、如何解决规则冲突以及何时要放弃推理。这三个层次通过批评者-提议者-策展者管道形成闭包：批评者通过比较规则增强推理与零样本基线在相同观测结果上的差异，为每条规则生成归因评价；提议者将评估结果追加到对应证据日志中，并基于证据提出新规则；策展者同时管理知识生命周期，废弃持续负面的规则并演进技能。关键技术特点包括证据的追加写入设计（从不修改或删除已有证据，确保治理决策基于完整历史）以及由证据驱动的技能演化（技能优先顺序等决策必须由日志中观察到的可靠性模式支撑，而非凭空生成）。在金融预测这一非平稳任务上，该方法使相同的经验积累要么提升性能、要么退化为低于零样本基线，完全取决于是否启用该策展循环。

### Q4: 论文做了哪些实验？

实验以金融预测为案例，使用2013-2016年S&P 500前五大股票（AAPL, AMZN, FB, GOOGL, MSFT）的日OHLCV数据作为学习期，2017年作为测试期，输入为20天K线图，预测5天方向。基础模型为Qwen3-VL-235B，批评者、提议者和策展者使用Claude Sonnet 4.6。对比方法包括：Zero-shot（无学习上下文）、Reflective Accumulation（提取所有规则但不策展）、Reflective Refinement（带重要性评分和就地修改但无持久证据日志）。主要结果（5次运行均值±标准差）：Zero-shot方向准确率51.2%±2.2、场景准确率23.8%±0.8、平均回报0.16%±0.1、夏普比率0.53±0.38、最大回撤34.5%±7.1；Reflective Accumulation全面下滑至46.3%±2.9、23.3%±3.2、-0.08%±0.2、-0.12±0.32、35.2%±11.4；Reflective Refinement恢复至51.1%±1.8、24.7%±1.5、0.14%±0.2、0.36±0.18、24.4%±9.0；本文方法（完整策展循环）达到56.5%±1.0、29.0%±2.5、0.33%±0.1、1.00±0.3、13.0%±4.4。结果表明：无策展时经验反而有害；部分策展仅部分恢复；完整循环实现真实学习——方向准确率提升5.3个百分点，夏普比率接近翻倍，最大回撤降低60%。还展示了规则库演化：无策展时累积19条，策展后仅11条活跃，技能主题（如触底反转）通过持久证据支持规则淘汰。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下方面：

1. **域与反馈类型的局限性**：当前验证仅局限于金融领域（2013–2017年S&P 500牛市）和单一点状反馈（噪声、延迟、非平稳）。未来需系统评估该框架对异质世界反馈（如即时二元任务成功、密集机器人控制信号）的迁移能力，构建跨反馈类型的标准化评估基准。

2. **元治理的自动化**：当前规则淘汰阈值、冲突解决策略等治理机制需手工设计。可借鉴元认知自我修正思想，让世界反馈驱动治理机制本身的演化——即学习“如何管理知识”的第二层反馈闭环。

3. **证据表示与时效性**：自然语言证据日志线性增长，难以扩展。可探索结构化表示（如键值存储）或嵌入压缩，同时保留可审计性。证据的等权累积在快速变化环境中反应滞后，引入贝叶斯时间折扣因子可平衡适应性与历史教训保留。

4. **动态技能组合学习**：当前技能规则仍基于固定结构，未来可研究如何从反馈中自动涌现出非单调的知识生命周期管理策略，例如将废弃规则转化为元特征供高层技能调用。

### Q6: 总结一下论文的主要内容

这篇文章针对LLM智能体从世界反馈中进行无梯度的言语强化学习时面临的“保留-遗忘困境”展开研究。所谓保留-遗忘困境，即在非平稳环境中，保留过时的见解会导致负迁移，而丢弃它们则在条件重现时造成灾难性遗忘。论文首次系统性地提出了应对该困境的四个必要条件：结果驱动的评估、持久的结构化证据、非单调的知识生命周期以及组合式治理。通过分析现有方法，发现它们过度侧重于经验提取，而严重忽视了见解治理。为此，论文提出了一种三层架构——规则层、证据层和技能层——通过一个反馈驱动的策展循环连接，以弥合治理缺口。该架构中，规则从经验中提炼知识，证据记录规则可靠性，技能则负责冲突解决和决策。在金融预测这一典型的、反馈丰富且非平稳的任务上验证表明，同样的经验积累，在有策展循环时能显著提升性能（准确率提升5.3pp，夏普比率翻倍），而无策展循环时性能甚至低于零样本基线。核心结论是，对于从世界反馈中学习的智能体而言，性能瓶颈并非经验提取的数量，而在于对洞察的治理能力。该工作为构建可调适的非平稳环境下的言语RL智能体提供了新的设计框架。
