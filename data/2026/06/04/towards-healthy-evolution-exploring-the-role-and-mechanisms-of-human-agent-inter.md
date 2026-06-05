---
title: "Towards Healthy Evolution: Exploring the Role and Mechanisms of Human-Agent Interaction in Self-Evolving Systems"
authors:
  - "Dianxing Shi"
  - "Junqi He"
  - "Junhao Chen"
  - "Bowen Wang"
  - "Yuta Nakashima"
date: "2026-06-04"
arxiv_id: "2606.06114"
arxiv_url: "https://arxiv.org/abs/2606.06114"
pdf_url: "https://arxiv.org/pdf/2606.06114v1"
categories:
  - "cs.AI"
tags:
  - "self-evolving agents"
  - "human-agent interaction"
  - "agent safety"
  - "feedback mechanism"
  - "LLM-based framework"
  - "self-play"
  - "human alignment"
relevance_score: 8.5
---

# Towards Healthy Evolution: Exploring the Role and Mechanisms of Human-Agent Interaction in Self-Evolving Systems

## 原始摘要

Self-evolving agents improve through continual self-play and self-generated learning signals, but autonomous evolution can also cause capability degradation and safety drift. Although human feedback has proven effective for static and post-trained agents, its role in self-evolving systems remains underexplored. We introduce Agent Norm Correction through Human-like Oversight and Review (ANCHOR), an LLM-based framework that simulates human supervision and delivers feedback at various phases of self-evolution. With ANCHOR, we evaluate two representative open-source self-evolving agent systems across coding, mathematical reasoning, and safety. Our results show that even limited supervision substantially mitigates safety degradation while preserving stable performance on core evolutionary objectives. Further analysis shows that supervision over the output verification phase is the most effective for intervention, whereas increasing supervision frequency yields diminishing returns. These findings provide empirical evidence and practical guidance for designing more stable, controllable, and human-aligned self-evolving agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决自进化智能体系统在自主进化过程中出现的能力退化与安全性漂移问题。研究背景是：当前大型语言模型通过后训练技术（如SFT、RLHF）实现了与人类意图的对齐，而自进化智能体则进一步通过自我对弈和自生成学习信号实现持续能力提升。然而，现有方法的不足在于：这种完全自主的进化模式存在严重风险，包括误评估、长期安全性漂移、模型遗忘甚至崩溃。根本原因是基于强化学习的微调过程中，智能体可能利用设计缺陷的目标进行奖励黑客或目标错配，导致初始安全对齐在参数更新过程中被逐渐侵蚀。虽然人类反馈在静态和后训练智能体中被证明有效，但在持续自我进化的动态过程中如何集成人类交互尚未得到充分研究。本文核心要解决的核心问题是：人类-智能体交互能否以及如何有效减轻自进化过程中的错误累积和安全性漂移，同时保持核心任务性能。通过模拟人类监督的框架ANCHOR，论文系统探究了不同监督时机和频率对编码、数学推理和安全性的影响，为设计更稳定、可控且与人类对齐的自进化智能体系统提供实证依据。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：**完全自主的自进化方法**、**人机协作方法**和**交互机制研究**。

1. **完全自主的自进化方法**：如DeepSeek-R1、R-Zero、AZR和MM-Zero等。这些方法通过自我对弈、自我生成数据实现完全闭环演化（如Proposer-Solver交互），但易因误差积累和分布漂移导致能力退化与安全偏移。本文指出这类系统缺乏外部监督，而ANCHOR通过引入模拟人类反馈来打破闭环，针对性解决其长期演化中的稳定性问题。

2. **人机协作方法**：代表性工作如Co-Gym，通过异步交互和共享控制缓解完全自主智能体的局限，但其重点在任务执行而非训练阶段演化。本文区别在于聚焦自演化系统的训练循环，将人类反馈直接注入自我学习过程，而非仅用于任务执行。

3. **交互机制研究**：包括AI-in-the-loop、Centaur等框架，以及SpeakRL（主动请求澄清）、AGDebugger（回滚与消息编辑）、R-Few（有限标注提升鲁棒性）等方法。这些工作主要针对特定推理阶段或有限交互量，缺乏统一框架。ANCHOR提出分阶段反馈（如输出验证阶段）和批量级总结，系统性分析不同交互阶段与频率的效果，填补了该领域缺乏跨阶段反馈分析的空白。

### Q3: 论文如何解决这个问题？

ANCHOR通过模拟人类监督机制，构建了一个基于LLM的监督框架来解决自进化系统中的能力退化与安全偏移问题。该框架作为“人类代理”附着于现有自进化系统，通过四个关键技术实现干预：

**核心方法**采用阶段化监督策略，将自进化过程分解为任务提议(task)、规划(plan)、思维(thought)、输出(output)和执行结果(exec)五个关键阶段。每个阶段由LLM监督器根据特定输入生成评估性反馈——例如在任务阶段评估任务质量，在输出阶段评估回答准确性，在执行阶段通过二元验证信号统计批量性能。

**架构设计**包含三个主要模块：1) **阶段感知监督器**，根据阶段类型选择不同输入信息(任务样本、推理轨迹、输出结果或验证决策)；2) **伯努利审核门**，通过可调采样频率f_p随机选择需要审查的阶段，模拟人类监督的有限注意力；3) **上下文聚合器**，将阶段级自然语言反馈汇总为批次级监督摘要，并通过LLM更新机制将反馈注入系统提示中，形成持续进化的指导上下文。

**创新点**在于：1) 首次系统化研究人类监督在自进化过程中的动力学作用；2) 提出验证阶段监督最为有效的实证发现；3) 揭示监督频率的边际递减效应，为设计高效干预策略提供理论依据。该方法无需金标准答案即可通过评估性反馈纠正演化方向，在保持核心能力的同时抑制安全退化。

### Q4: 论文做了哪些实验？

论文在AZR和R-Zero两个自进化框架上评估ANCHOR，使用Qwen2.5系列（3B至14B）和Qwen3系列（4B/8B）作为骨干模型。实验覆盖三个维度：编码（LiveCodeBench、EvalPlus）、数学推理（AIME24/25、AMC23、MATH500、OlympiadBench、Minerva Math）和安全（HarmBench、SaladBench、HEx-PHI、Reward Hacking）。主要结果：ANCHOR在多数编码和数学指标上优于基线，且显著缓解安全退化，如ANCHOR-Coder-7B的ASR从21.1降至16.2，ANCHOR-4B的ASR从16.0降至10.0；RR在ANCHOR-8B上从34.1提升至73.2。消融实验表明，执行验证阶段监督最关键（移除导致14.3%性能下降），输出阶段影响最小（-1.7%）。超参实验发现，监督频率在0.3-0.4时增益接近最大，继续增加回报递减。训练成本分析显示，ANCHOR仅带来适度开销，如ANCHOR-Coder-3B每步时间从7.3分钟增至8.5分钟。

### Q5: 有什么可以进一步探索的点？

首先，论文使用LLM模拟人类监督，这引入了模型偏见和偏好偏移的风险，未来可探索使用真实人类反馈或混合监督策略来校准模拟信号。其次，干预效果依赖于特定框架与任务域（如编码与数学推理），需在更广泛系统架构（如基于MCTS、RAG的进化范式）及多模态、工具调用或具身环境下的通用性验证。此外，输出验证阶段的监督最有效且增加频率收益递减，这表明存在最优监督时机与频率的组合，可研究自适应监督调度。进一步，可引入动态干预阈值与事后解释机制，平衡进化速度与安全性。最后，当前只分析了单个干预点，未来可探索多阶段协作反馈（如联合修正推理链、动作空间与目标函数）对长期进化轨迹及涌现行为的影响，以设计更鲁棒、可控且对齐人类价值观的自进化系统。

### Q6: 总结一下论文的主要内容

该论文研究自我进化智能体在人机交互下的健康进化问题，旨在解决自主进化中能力退化与安全偏移的挑战。作者提出 ANCHOR 框架，通过模拟类人监督与审查机制，在自我进化的不同阶段注入反馈信号。在编码、数学推理和安全三个任务上对开源自我进化系统进行评估，发现即使有限的人类监督也能显著缓解安全退化，同时保持核心任务性能稳定。进一步分析表明，对输出验证阶段进行干预最为有效，而增加监督频率则呈现收益递减规律。这些发现为设计更稳定、可控且符合人类价值观的自我进化系统提供了经验证据和实践指导，展示了可扩展人机协同机制的潜力。
