---
title: "Useful Memories Become Faulty When Continuously Updated by LLMs"
authors:
  - "Dylan Zhang"
  - "Yanshan Lin"
  - "Zhengkun Wu"
  - "Yihang Sun"
  - "Bingxuan Li"
  - "Dianqi Li"
  - "Hao Peng"
date: "2026-05-13"
arxiv_id: "2605.12978"
arxiv_url: "https://arxiv.org/abs/2605.12978"
pdf_url: "https://arxiv.org/pdf/2605.12978v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "经验整合"
  - "LLM自我改进"
  - "情景记忆vs整合记忆"
  - "记忆退化"
  - "ARC-AGI"
  - "智能体记忆管理"
relevance_score: 9.0
---

# Useful Memories Become Faulty When Continuously Updated by LLMs

## 原始摘要

Learning from past experience benefits from two complementary forms of memory: episodic traces -- raw trajectories of what happened -- and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising self-improving agents without parameter updates. Yet we find that such consolidated memories produced by today's LLMs are often faulty even when derived from useful experiences. As consolidation proceeds, memory utility first rises, then degrades, and can fall below the no-memory baseline. More surprisingly, even when consolidating from ground-truth solutions, GPT-5.4 fails on 54% of a set of ARC-AGI problems it had previously solved without memory. We trace the regression to the consolidation step rather than the underlying experience: the same trajectories yield qualitatively different memories under different update schedules, and an episodic-only control that simply retains those trajectories remains competitive with the consolidators we test. In a controlled ARC-AGI Stream environment that exposes Retain, Delete, and Consolidate actions, agents preserve raw episodes by default and double the accuracy of their forced-consolidation counterparts; disabling consolidation entirely (episodic management only) matches this auto regime. Practically, robust agent memory should treat raw episodes as first-class evidence and gate consolidation explicitly rather than firing it after every interaction. Looking forward, reliable agentic memory will require LLMs that can consolidate without overwriting the evidence they depend on.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文聚焦于LLM智能体的记忆巩固（memory consolidation）机制，旨在解决当前主流方法中“持续更新记忆反而导致性能退化”的核心悖论。研究背景是：智能体系统借鉴人类认知中的记忆巩固理论，将原始经验轨迹（episodic traces）压缩为可复用的抽象知识（如文本记忆库），以实现无需参数更新的自进化能力。然而现有方法（如CLIN、AWM等）普遍采用“每次交互后强制更新”的设计，默认认为巩固步骤至少不会损害性能。本文通过系统实验揭示了关键缺陷：即便输入轨迹本身是完美可用的（如已解决的难题或标准答案），经过LLM的反复抽象后，记忆效用反而呈现先升后降的倒U型曲线，甚至低于无记忆基线。最典型的反例是，GPT-5.4在无记忆条件下可100%解决的ARC-AGI问题集，经过自身成功轨迹的巩固后反而解题失败率高达54%。论文要解决的核心问题是：为何当前LLM无法可靠地将有用经验转化为稳定的抽象记忆？并由此质疑“每次交互后立即巩固”的默认设计范式，提出应在原始证据和抽象知识间建立明确分工。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。方法类方面，研究集中在LLM智能体的记忆系统设计，包括层次化上下文存储、反思笔记、情景流、蒸馏经验、技能库、因果抽象、动态记忆存储、演变手册和推理记忆库等。这些工作普遍采用LLM从经验中抽象出可复用的程序性信息作为文本记忆，本文则聚焦于这种“压缩-更新”范式的潜在缺陷，通过实验证明该范式下记忆效用会先升后降，甚至低于无记忆基线。应用类方面，研究在ALFWorld、ScienceWorld、WebShop、AppWorld和ARC-AGI等环境上测试了智能体记忆系统。本文特别关注ARC-AGI任务，发现即使使用真实解，强制持续更新也会导致性能严重退化（GPT-5.4在已解决任务上失败率达54%）。与这些工作不同的是，本文揭示了记忆衰退的根本原因在于压缩步骤而非经验本身，并且证明了纯情景记忆（仅保留原始轨迹）能保持竞争力。此外，本文引入认知理论中的图式形成与元认知控制理论，指出当前系统让LLM同时负责记忆生成和抽象监控存在控制回路不可靠问题，这与思维链解释偏离底层计算的现象一致。

### Q3: 论文如何解决这个问题？

论文通过系统性实验揭示了持续更新的抽象记忆会退化的问题，并提出了以原始轨迹为核心、显式控制记忆管理的解决方案。核心方法是在ARC-AGI Stream等基准上构建受控实验环境，将记忆过程分为两个存储：**情景缓冲（Episodic buffer）** 存储原始轨迹，**抽象存储（Abstract store）** 存储经LLM蒸馏后的课程式经验。三个关键控制条件对比：Force（每步强制抽象，不保留情景）、Auto（让模型自主选择保留原始或抽象）、Episodic Management Only（仅保留和删除，完全禁用抽象）。主要发现：1）抽象记忆效用非单调——早期提升后持续下降，甚至低于无记忆基线；2）高质量记忆无法稳定——持续更新导致GPT-5.4在已解决任务上从100%降至54%；3）抽象过程本身塑造退化速率——按任务族分组优于混合分组，一次性批处理优于流式增量更新，异构批次加速退化。技术创新点：设计了一个可追溯记忆操作细粒度影响的评估框架，证明原始轨迹日志本身作为竞争性基线（情景记忆仅追加保存）能与甚至超越抽象记忆方法。最终建议：原始轨迹应作为一等证据被默认保留，抽象应通过显式门控机制而非每次交互后自动触发，以避免覆盖依赖的证据。

### Q4: 论文做了哪些实验？

论文在多个基准测试上评估了记忆更新策略的效果。实验设置包括五个标准Agent基准（ALFWorld、ScienceWorld、WebShop、AppWorld、Mind2Web）以及一个自建的ARC-AGI Stream测试平台。对比了四种记忆方法：CLIN、Agent Workflow Memory、Dynamic Cheatsheet和ACE。主要实验发现：1）记忆效用呈非单调变化，在ScienceWorld上，分数在第20步附近达到峰值后持续下降，在第100步时低于无记忆基线；WebShop上AWM从64%下降至20%。2）在ARC-AGI Stream上，使用ground-truth解决方案流式更新时，GPT-5.4在先前100%解决的19个问题上准确率降至54%。3）批次组合影响显著，异质批次加速性能下降。4）对比三种控制循环（Force、Auto、仅情节管理），强制每次更新都进行整合（Force）的效果最差，仅情节管理（无抽象）的表现与Auto模式相当或更优。关键数据：AppWorld上，情节基线（All）在多个骨干模型上达到最高73%的TGC%，而整合方法如ACE仅65%。

### Q5: 有什么可以进一步探索的点？

论文揭示了当前LLM记忆系统的核心矛盾：连续更新会损害记忆效用，但这一发现基于特定的强制合并策略。未来探索可从三方面深入：首先，需要设计动态门控机制，让代理自主判断何时需要合并而非每次交互都触发，可借鉴互补学习系统中海马体与新皮层的交互模式，用“模式匹配”指标量化新旧经验的兼容性。其次，论文发现原始片段胜过抽象记忆，但未探索半结构化表示，或许混合存储层级（如保留关键统计量而非全量片段）能在压缩率与保真度间取得平衡。最后，当前评估仅在ARC-AGI领域，需在更复杂任务（如具身推理、多步工具使用）中验证，并研究当经验数量达百万级时，基于检索的片段池是否仍优于抽象记忆。值得注意的是，需开发专门的元认知监控模块，当检测到记忆效用退化时自动触发回滚或局部合并操作。

### Q6: 总结一下论文的主要内容

这篇论文系统地研究了当前大型语言模型(LLM)在智能体记忆系统中的记忆巩固能力。问题定义上，作者关注智能体在持续将过往经验轨迹压缩为文本记忆时，记忆质量是否会退化。方法上，他们设计了受控实验，使用ALFWorld、ScienceWorld等多个环境，并引入ARC-AGI测试平台，对比了不同更新策略（如一次性静态巩固与流式迭代巩固）和纯情景记忆基线。主要结论是：LLM的巩固机制存在严重缺陷，即便输入轨迹本身有用（如从已解决的问题或正确答案中获取），巩固后的记忆也会先上升后下降，甚至低于无记忆基线。在ARC-AGI任务中，GPT-5.4在依靠记忆后失败率高达54%。作者识别出错误分组、过度泛化条件剥离和过拟合三种失败机制。研究的核心贡献是揭示了当前“每次交互后立即巩固”设计范式的根本性问题，并指出保留原始情景记录作为一等证据比强制巩固更稳健，为未来可靠的智能体记忆系统设计指明了方向。
