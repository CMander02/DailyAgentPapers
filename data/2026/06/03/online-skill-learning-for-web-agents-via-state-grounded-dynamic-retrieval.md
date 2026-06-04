---
title: "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval"
authors:
  - "Jiaxi Li"
  - "Ke Deng"
  - "Yun Wang"
  - "Jingyuan Huang"
  - "Yucheng Shi"
  - "Qiaoyu Tan"
  - "Jin Lu"
  - "Ninghao Liu"
date: "2026-06-03"
arxiv_id: "2606.04391"
arxiv_url: "https://arxiv.org/abs/2606.04391"
pdf_url: "https://arxiv.org/pdf/2606.04391v1"
github_url: "https://github.com/plusnli/skill-dynamic-retrieval"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "在线技能学习"
  - "动态检索"
  - "状态引导"
  - "WebArena"
  - "GPT-4.1"
  - "Qwen3-4B"
relevance_score: 9.0
---

# Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval

## 原始摘要

Language agents increasingly rely on reusable skills to improve multi-step web automation across related tasks. A growing line of work studies online skill learning, where agents continually induce skills from previous task trajectories and reuse them in future tasks on the fly. However, existing methods mainly reuse skills at the task-level: a fixed set of skills is retrieved based on the initial task instruction and then held fixed throughout execution. This static strategy is misaligned with web execution, where the appropriate next action depends not only on the task goal but also on the current webpage state, which often transitions into situations that the initial skills fail to cover. To address this gap, we propose State-Grounded Dynamic Retrieval (SGDR), an online skill learning method that enables stepwise skill reuse for web agents. SGDR consists of three components: a sliding-window extraction process that turns completed trajectories into reusable sub-procedures invokable at intermediate execution states, a dual text-code representation that connects skill retrieval with executable action, and a state-grounded dynamic retrieval mechanism that matches skills to both the task goal and the current webpage state. Experiments on WebArena across five domains show that SGDR consistently outperforms strong baselines, achieving average success rates of 37.5% with GPT-4.1 and 24.3% with Qwen3-4B, corresponding to relative gains of 10.6% and 10.0% over the strongest baseline, respectively. The code is available at https://github.com/plusnli/skill-dynamic-retrieval.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在线技能学习（online skill learning）框架下，网页自动化代理（web agents）在技能复用时的状态对齐问题。现有方法大多采用“任务级一次性复用”策略：基于初始任务指令检索固定技能集，并在整个执行过程中保持不变。然而，网页交互任务具有高度动态性，当前网页状态（如页面跳转、表单切换）会频繁变化，导致最初检索的技能可能过时，而未被选中的技能却在后续关键时刻变得有用。这种静态复用方式忽略了技能与中间执行状态之间的依赖关系，核心不足在于技能检索粒度与网页执行的实际需求不匹配。

为此，本文提出**状态接地动态检索（State-Grounded Dynamic Retrieval, SGDR）**方法，其核心是变静态任务级复用为动态步骤级复用。SGDR通过三个关键组件解决该问题：一是滑动窗口提取，将完整轨迹拆解为可复用的子过程，提供适中的技能粒度；二是双文本-代码表示，使技能既可通过自然语言描述检索，又能直接作为可执行浏览器动作；三是状态接地动态检索机制，在每一步决策时结合当前任务指令与实时网页状态，动态选择最匹配的技能。该方法旨在让代理在连续任务流中，根据执行状态自适应调整技能支持，从而提升多步网页自动化任务的成功率与效率。

### Q2: 有哪些相关研究？

本文的相关工作主要包括以下类别：

**方法类**：早期工作探索了语言模型与浏览器交互的指令遵循能力。后续研究通过工作流归纳、可复用技能、长程记忆等机制增强智能体鲁棒性，如将过程知识以自然语言反思或经验蒸馏形式存储。近年工作将技能结构化表示为工作流/可执行程序/可检索经验等。与这些方法的关键区别在于：现有工作通常将学习到的技能视为固定记忆库，在任务开始前根据初始指令一次性检索后全程使用；而本文提出的SGDR方法首次关注技能在执行过程中的**动态检索时机**，根据当前网页状态进行逐步匹配。

**评测类**：WebArena等基准推动了动态、长跨度的web自动化评估。本文在五个领域的评估表明，相比仅基于初始指令检索的静态方法，SGDR通过状态引导的动态检索实现了显著提升。

**本文创新点**：SGDR包含三个核心组件——滑动窗口提取将完整轨迹分解为可复用的子流程；双文本-代码表示连接检索与执行；状态引导的动态检索机制使技能选择同时匹配任务目标和当前页面状态，解决了现有方法在中间状态覆盖不足的问题。

### Q3: 论文如何解决这个问题？

论文提出了一种名为状态锚定动态检索（State-Grounded Dynamic Retrieval, SGDR）的在线技能学习方法，旨在解决现有方法在Web自动化中仅基于初始指令静态复用技能、无法适应执行中网页状态变化的问题。SGDR的核心设计包含三个关键模块。

首先，在技能提取阶段，采用滑动窗口机制从成功完成的轨迹中分解出可复用的子过程。具体而言，对每条任务轨迹，使用长度集合L内的不同窗口枚举候选片段（如从观察状态到动作序列再到新观察状态），这些片段对应“打开设置页”或“填写表单”等局部但语义完整的子例程。每个候选片段经大语言模型评估后，若被判断为可复用状态条件过程，则生成技能并表示为文本-代码对（自然语言描述+可执行代码函数），使检索和执行业务对齐。此后，通过替换原始轨迹中的原始动作为技能调用并重新执行验证，确保添加的技能在替代后仍能保证任务成功。

在技能检索环节，核心创新在于状态锚定的动态检索机制。每步决策时，系统同时基于全局任务指令和当前网页状态摘要（对原始访问树等冗长状态压缩得到）计算技能相关性得分，通过超参数α平衡任务目标对齐与当前状态匹配。在此基础上，采用最大边际相关性对粗筛后的候选集进行重排序，引入λ参数在相关性与多样性间权衡，避免重叠窗口导致的冗余技能占用决策槽位。最终仅保留5个根据当前状态动态适应的技能供给智能体，实现每步层面的即时技能适配。

该框架采用渐进式知识积累：每个任务结束后，仅将验证通过的技能添加入特定领域的技能库，并持续服务于后续任务。实验表明，SGDR在WebArena五个领域平均成功率达37.5%（GPT-4.1），相对最强基线CER提升10.6%，同时将每任务平均步数降至4.8步（缩短21%），验证了状态感知动态复用策略的有效性。

### Q4: 论文做了哪些实验？

论文在WebArena基准上进行了实验，该基准涵盖购物、管理、Reddit、GitLab和地图五个网站域。实验采用二值成功奖励（成功为1，失败为0）作为评估指标，并与四种基线方法比较：Vanilla（无技能复用）、Agent Workflow Memory (AWM，存储自然语言工作流)、Agent Skill Induction (ASI，归纳可执行技能)和Contextual Experience Replay (CER，检索历史经验)。使用GPT-4.1和Qwen3-4B作为骨干模型。主要结果为：SGDR在GPT-4.1下平均成功率37.5%，在Qwen3-4B下为24.3%，相对最强基线CER分别提升3.6和2.2个百分点；在四个域上取得最优，其中Admin域从41.4%提升至47.7%。消融实验在购物、Reddit和地图三个域上进行，包括：1）检索信号消融：任务+状态组合（α=0.5）表现最佳，分别达34.6%、35.9%和32.3%，优于单一任务或状态；2）MMR重排序消融：λ=0.7时最优，优于无重排序；3）滑动窗口提取消融：滑动窗口（34.6%/35.9%/32.3%）优于全轨迹（31.1%/32.4%/28.8%）和单动作（29.5%/24.7%/25.4%）。效率方面，SGDR在GPT-4.1下平均4.8步，低于Vanilla的6.0步和CER的6.4步。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于实验仅基于WebArena平台，覆盖的网站域和交互模式有限，且仅采用非参数化的技能积累方式，未探索技能与模型微调或长期个性化的结合。未来可探索的方向包括：在更广泛的网络环境（如VisualWebArena、Multiverse）中验证SGDR的泛化性，并增强技能在跨域任务间的迁移能力；引入参数化方法（如将技能编码为模型权重或通过LoRA微调），使技能积累能持续影响模型自身行为；结合用户历史行为实现个性化技能库的动态更新与遗忘机制，避免技能膨胀；改进状态匹配的粒度，例如融合视觉信息或DOM树的层级结构，以提升复杂页面状态下的技能检索准确性。此外，可尝试将动态检索与强化学习结合，让模型在探索中主动触发技能学习循环。

### Q6: 总结一下论文的主要内容

本文提出了一种在线技能学习方法SGDR，用于解决网页代理在多步自动化任务中技能复用与当前状态脱节的问题。现有方法通常仅在任务开始时检索固定技能集并全程使用，但网页执行过程中状态频繁转换，导致初始技能无法覆盖后续需求。SGDR通过三个核心组件实现逐步骤的动态技能复用：滑动窗口提取机制从已完成轨迹中提取可复用的子过程；双文本-代码表示连接技能检索与可执行动作；状态接地动态检索机制同时考虑任务目标和当前网页状态来匹配技能。在WebArena五个领域的实验表明，SGDR在GPT-4.1和Qwen3-4B上分别取得37.5%和24.3%的平均成功率，相对最强基线提升10.6%和10.0%，证明了状态感知检索是提升闭源和开源模型网页代理性能的有效途径。
