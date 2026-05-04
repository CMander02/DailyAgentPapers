---
title: "Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory"
authors:
  - "Derong Xu"
  - "Shuochen Liu"
  - "Pengfei Luo"
  - "Pengyue Jia"
  - "Yingyi Zhang"
  - "Yi Wen"
  - "Yimin Deng"
  - "Wenlin Zhang"
  - "Enhong Chen"
  - "Xiangyu Zhao"
  - "Tong Xu"
date: "2026-05-01"
arxiv_id: "2605.00702"
arxiv_url: "https://arxiv.org/abs/2605.00702"
pdf_url: "https://arxiv.org/pdf/2605.00702v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent 记忆"
  - "记忆更新策略"
  - "强化学习"
  - "个性化"
  - "认知启发"
relevance_score: 9.0
---

# Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory

## 原始摘要

Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long interactions. Existing memory systems mainly rely on static, hand-crafted update rules; although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable long-horizon optimization. Drawing on memory schema theory and the functional division between prefrontal regions and hippocampus regions, we introduce MemCoE, a cognition-inspired two-stage optimization framework that learns how memory should be organized and what information to update. In the first stage, we propose Memory Guideline Induction to optimize a global guideline via contrastive feedback interpreted as textual gradients; in the second stage, Guideline-Aligned Memory Policy Optimization uses the induced guideline to define structured process rewards and performs multi-turn RL to learn a guideline-following memory evolution policy. We evaluate on three personalization memory benchmarks, covering explicit/implicit preference and different sizes and noise, and observe consistent improvements over strong baselines with favorable robustness, transferability, and efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有大语言模型（LLM）智能体在长期记忆管理中的核心挑战：如何在有限上下文窗口下，实现对用户动态偏好的持续跟踪与利用。当前主流的记忆系统主要依赖静态、手工设计的更新规则，无法从交互反馈中学习适应。而基于强化学习（RL）的方法虽能学习记忆更新策略，但由于只依赖稀疏结果奖励（如最终回答正确性），导致在巨大的操作空间（自由编辑写入或遗忘内容）中面临弱监督问题，造成长程优化不稳定、训练效率低。为克服这些不足，受人类记忆的“前额叶-海马体”功能分离理论启发，论文提出MemCoE框架，将记忆管理解耦为两个阶段：第一阶段学习“如何组织”记忆（即全局的记忆指导原则），第二阶段学习在原则约束下“更新什么”内容。其核心创新在于通过对比反馈生成文本梯度来归纳指导原则，再利用原则定义结构化的过程奖励，引导多轮RL策略进行端到端学习，从而解决现有方法中动作空间过大、奖励稀疏、优化不稳定的根本问题。

### Q2: 有哪些相关研究？

相关研究可分为三类：第一类是LLM Agent的记忆系统，例如基于显式记忆库的存储方法（分割、摘要、压缩、遗忘/更新）、结构化记忆索引（树、图）以及面向个性化的用户画像捕获方法。这些方法依赖手工设计的启发式规则，在用户行为非平稳时表现脆弱。本文方法与之正交，作为通用记忆演化机制可兼容现有记忆后端。第二类是用强化学习优化记忆，代表工作包括RMM（反射式更新与检索）、MemAgent（选择性保留/覆盖长对话历史）、MEM1（紧凑记忆训练）和MemGen（生成式潜在记忆）。它们仅依赖最终结果作为稀疏奖励，缺乏过程级指导。本文通过引入对齐准则的奖励结构，提供细粒度学习信号。第三类是基于文本梯度的提示优化，如TextGrad（迭代式文本梯度提示优化）、OPRO（将大语言模型作为黑箱优化器）和Reflexion（失败经验反射）。本文的Memory Guideline Induction与之类似，但差异在于：优化长期记忆演化全局准则而非单轮提示，通过对比诊断和批量聚合稳定更新，并通过准则对齐的过程奖励与第二阶段RL交互，共同优化记忆更新策略与增强行为。

### Q3: 论文如何解决这个问题？

该论文提出了一个名为 MemCoE 的认知启发式两阶段优化框架，用于学习高效的用户记忆演化机制。整体框架分为两个核心阶段，协同解决“如何组织记忆”和“更新什么信息”的问题。

第一阶段为**记忆指南归纳**，旨在学习一个全局性的自然语言指南，指导记忆应该如何被组织和演化。关键技术包括：首先，通过对比反馈生成文本梯度，即利用一个训练实例中正确与错误轨迹的对比，由大语言模型生成文本形式的批评意见，作为优化指南的梯度；其次，通过批级梯度聚合，将一批实例的文本梯度汇总为单一的、稳定的更新方向，从而迭代地精炼指南。该方法将记忆更新指令视为可优化的自然语言参数，核心创新在于用数据驱动的方式替代了静态的手工模板。

第二阶段为**指南对齐的记忆策略优化**，固定第一阶段习得的指南，专注于学习具体更新什么内容。设计了一种结合指南对齐奖励和答案奖励的复合轨迹奖励函数，前者通过结构化评分确保记忆更新严格遵循指南格式，后者通过最终答案的正确性信号衡量下游表现。采用组相对策略优化（GRPO）对记忆演化策略进行多轮强化学习，以最大化期望奖励。第二阶段的创新在于利用第一阶段得到的指南来定义结构化的过程奖励，从而为强化学习提供更密集、更稳定的监督信号，解决了长序列优化中稀疏奖励导致的收敛困难问题。

### Q4: 论文做了哪些实验？

论文在三个个性化记忆基准上进行了全面实验：PersonaMem（32K/128K长历史）、PrefEval（显式/隐式偏好，各1000道多选题，含50轮干扰）和PersonaBench（不同噪声水平0.3/0.5/0.7下的检索问答）。对比方法包括：长上下文直接输入、RAG检索增强生成、三种检索式记忆方法（Mem0、A-Mem、LightMem），以及两种强化学习记忆智能体（MemAgent、Mem-α）。主要结果采用Acc（PersonaMem和PrefEval）和F1（PersonaBench）评估。方法MemCoE在全部八项设置中均取得最佳总体得分52.02。具体关键数据：PersonaMem 32K上达57.06（第二名MemAgent 53.58），128K上达47.24；PrefEval显式偏好81.30（第二MemAgent 72.30），隐式偏好69.90；PersonaBench无噪声32.27（第二名A-Mem 30.32），高噪声0.7下仍达25.09。消融实验证实两阶段框架各组件均不可或缺，去除任一会导致一致性能下降。效率分析显示方法在性能-时间权衡中处于前沿。跨LLM迁移实验表明优化出的guideline具有模型无关性。超参数分析发现每轮记忆演化4K-8K tokens效果最佳，Top-20检索时效果最优。

### Q5: 有什么可以进一步探索的点？

首先，论文的第二阶段依赖LLM评分器提供过程奖励，其可靠性直接影响性能，未来可探索更鲁棒的奖励建模方式，如引入对抗训练或基于人类反馈的校准机制来减少评分偏差。其次，长历史分段成多轮演化时，小错误会累积导致遗忘或过度泛化，可考虑引入错误检测与回滚机制，或设计增量更新策略而非全量重写来提升稳定性。第三，当前为固定准则下的单目标优化，未来可扩展为多目标权衡框架，例如利用帕累托优化动态平衡稳定性与可塑性、信息量与简洁性，或通过元学习自适应调整准则权重。此外，可借鉴认知科学中的睡眠重放机制，在离线阶段对记忆进行整合与抽象，以增强长期一致性。最后，当前主要评估显性和隐性偏好，可进一步探索在开放域对话中的记忆迁移能力，例如跨用户或跨领域的准则迁移。

### Q6: 总结一下论文的主要内容

这篇论文提出 MemCoE，一种受认知科学启发的两阶段优化框架，用于解决大语言模型（LLM）智能体中的长期用户记忆更新问题。当前记忆系统多依赖静态手写规则，而基于强化学习（RL）的方法因稀疏奖励导致优化不稳定。受记忆模式理论及前额叶与海马体功能分工的启发，MemCoE将“如何组织记忆”与“存储什么内容”解耦。第一阶段通过**记忆指南归纳**，利用对比反馈作为文本梯度优化全局指南；第二阶段通过**指南对齐的记忆策略优化**，将指南定义为结构化过程奖励，进行多轮RL以学习遵循指南的记忆演化策略。在三个个性化记忆基准上，MemCoE在显式/隐式偏好、不同大小和噪声条件下均取得一致改进，并展现出良好的鲁棒性、迁移性和效率。核心贡献在于将显式的演化指南与策略优化相结合，为对话智能体中演化用户记忆提供了一种实用方案。
