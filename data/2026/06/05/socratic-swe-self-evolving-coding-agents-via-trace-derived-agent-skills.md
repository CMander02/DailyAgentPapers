---
title: "Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills"
authors:
  - "Chuan Xiao"
  - "Zhengbo Jiao"
  - "Shaobo Wang"
  - "Wei Wang"
  - "Bing Zhao"
  - "Hu Wei"
  - "Linfeng Zhang"
  - "Lin Qu"
date: "2026-06-05"
arxiv_id: "2606.07412"
arxiv_url: "https://arxiv.org/abs/2606.07412"
pdf_url: "https://arxiv.org/pdf/2606.07412v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "代码Agent"
  - "自我进化"
  - "数据合成"
  - "SWE-bench"
  - "Agent训练"
  - "闭环框架"
  - "工具使用"
relevance_score: 9.0
---

# Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills

## 原始摘要

LLM-driven software engineering agents have become a central testbed for real-world language-model capability, yet their training remains limited by the availability of high-quality SWE tasks. Existing synthetic data methods typically create tasks through fixed mutation or bug-injection procedures, making the resulting distributions largely independent of the agent's own weaknesses and training progress. We introduce Socratic-SWE, a closed-loop self-evolution framework that reuses the agent's historical solving traces as a source of training signal. Rather than treating traces only as evidence for reward computation, Socratic-SWE distills them into structured agent skills that summarize recurring failures and effective repair patterns. These skills then guide the generation of targeted repair tasks in real repositories. Candidate tasks are checked through execution-based validation and scored with a solver-gradient alignment reward, so that the retained tasks are both verifiable and useful for improving the Solver. The updated Solver produces new traces, enabling the task curriculum to adapt over successive rounds. Across SWE-bench Verified, SWE-bench Lite, SWE-bench Pro, and Terminal-Bench 2.0, Socratic-SWE consistently improves over self-evolving baselines under the same compute budget, reaching 50.40% on SWE-bench Verified after three iterations. These results suggest that solving traces can serve as a scalable substrate for self-evolving SWE agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的软件工程（SWE）智能体在训练过程中面临的高质量任务数据稀缺问题。研究背景指出，SWE任务需要智能体在真实代码仓库中完成长程交互，是衡量模型真实智能的关键场景，而强化学习训练高度依赖大量高质量任务。现有方法主要通过固定的AST突变或注入bug流程来生成合成数据，但这些方法生成的任务分布独立于智能体自身的弱点与训练进度，导致任务分布静态化，与模型的实际能力缺口严重脱节。随着模型提升，固定分布中有用训练信号越来越稀疏，学习最终停滞。本文核心问题是：能否利用智能体自身的历史求解轨迹（traces）作为可再利用的原料，驱动自我进化的闭环？这些轨迹记录了智能体的失败模式和有效修复策略，但现有方法仅将其用于奖励计算或信用分配后就丢弃了。因此，Socratic-SWE提出将求解轨迹提炼为结构化的智能体技能（Agent Skills），再用技能指导生成针对性的修复任务，并通过执行验证和求解器梯度对齐奖励筛选任务，从而形成一个“轨迹→技能→任务→新轨迹”的自适应课程循环，实现无需外部标注的持续自我进化。

### Q2: 有哪些相关研究？

方法类相关研究包括：各类强化学习方法（如GRPO、DAPO、GSPO等）虽改进效率，但假设即时可验证奖励，而本文针对代码修复任务中反馈稀疏的问题，采用轨迹分析生成结构化技能。在SWE智能体方面，SWE-RL、SWE-Gym等工作利用执行环境构建训练场景，但依赖固定突变或注入故障生成任务，未充分挖掘模型自身失败模式；本文的Socratic-SWE通过历史解决轨迹提取可复用技能，据此定向生成针对性修复任务，实现自演化课程。在自演化LLM方面，TTRL、R-Zero、Challenger-Solver等方法通过自对弈减少人工标注，但反馈噪声较大；本文通过执行验证和求解器梯度对齐奖励筛选任务，确保可验证性并推动能力提升。SkillRL、SKILL0等从交互经验中提炼可重用技能，本文借鉴此思路，但将技能作为链接过去失败与未来任务分布的桥梁，使课程自适应演化。整体而言，本文是第一项将执行轨迹系统转化为结构化技能并驱动代码智能体自我进化的方法，区别于仅用轨迹计算奖励或独立生成任务的工作。

### Q3: 论文如何解决这个问题？

Socratic-SWE 通过**闭环自演化框架**解决训练数据与智能体真实弱点分布不匹配的问题。整体框架包含两个共享策略πθ的角色：**生成器(Generator)**和**求解器(Solver)**，二者交替演进。

核心方法是**从历史求解轨迹中蒸馏结构化技能**，并用其引导生成针对性的修复任务。其包含三个关键模块：

1. **智能体技能注册表(Agent Skill Registry)**：通过三阶段流水线构建。首先收集求解器在种子任务集上的成功/失败轨迹；然后由蒸馏模型Mdistill从成功轨迹中提取通用策略、从失败轨迹中总结错误模式和修复原则；最后通过语义去重和覆盖过滤形成结构化的技能库(含名称、描述、适用条件、操作列表四个字段)。

2. **生成器**：基于技能注册表和求解器证据Et，在真实仓库中生成可执行修复任务。任务必须通过**四级验证关卡**(格式有效性、仓库引用可接地性、测试可执行性、语义可分离性)才能进入训练池。同时引入**求解器梯度对齐奖励**，计算候选任务产生的策略梯度与验证集目标梯度方向的余弦相似度，确保生成任务有助于求解器改进。

3. **求解器**：在仓库沙箱中执行修复任务，获得**可执行反馈奖励**，综合考量完整通过率、部分修复率和回归避免率。采用分组归一化优势估计(GDPO)处理多尺度奖励。

创新点在于将历史轨迹转化为可复用、可检索的结构化技能，形成"任务→轨迹→技能→新任务"的闭环演进，使任务分布随智能体能力自适应调整。

### Q4: 论文做了哪些实验？

论文在四个基准上评估了Socratic-SWE框架：SWE-bench Verified（500个issue）、SWE-bench Lite（300个）、SWE-bench Pro（731个）和Terminal-Bench 2.0。所有方法均使用相同的Solver（Qwen3.5-9B）、执行框架（mini-swe-agent）和训练预算（每轮12k实例，共3轮）。对比方法包括基线Base Agent以及五个自进化基线：R-Zero、SPIRAL、Absolute-Zero、Socratic-Zero和SSR。实验结果显示，Socratic-SWE在所有基准上均取得最优结果。三轮迭代后，它在SWE-bench Verified上达到50.40%（+7.80），在SWE-bench Lite上达到36.67%（+7.00），在SWE-bench Pro上达到22.85%（+5.61），在Terminal-Bench 2.0上达到14.61%（+4.50），整体平均分从基线的24.91提升至31.13（+6.22）。相比之下，R-Zero、SPIRAL和Absolute-Zero等自玩方法在后续迭代中性能饱和甚至退化，而SSR虽然稳步提升但增长有限（在Verified上+4.40）。Socratic-SWE的优势在于其技能引导的任务生成和基于执行验证的奖励对齐。

### Q5: 有什么可以进一步探索的点？

该论文的局限性和未来探索点主要有以下方向：首先是封闭世界设定问题，论文的Agent Skill Registry在固定种子仓库上会饱和，训练信号逐渐冗余。未来可以探索跨仓库技能迁移，引入动态更新的仓库池，甚至将技能学习扩展到不同编程语言和项目风格，打破单一分布的限制。其次是验证数据依赖问题，Generator-Gradient Alignment奖励依赖于固定的保留验证集，这可能导致过拟合于特定分布。未来可设计自适应验证集构建策略，或利用模型自身的不确定性来动态选择验证任务。另外，框架假设了可执行测试和沙盒环境，对于测试不完善或非确定性执行的项目适应性有限。可以研究如何从自然语言反馈或用户交互中提取验证信号，降低对执行环境的依赖。最后，手工技能分类或简单提取器仍有提升空间，可探索更细粒度的技能归纳方法，如结合代码结构分析或多模态特征，使技能描述更精确，从而进一步突破性能天花板。

### Q6: 总结一下论文的主要内容

该论文提出了Socratic-SWE，一个用于软件工程智能体的闭环自进化框架，旨在解决高质量SWE任务数据匮乏的问题。该方法的核心贡献在于，不再将智能体的历史求解轨迹仅用于奖励计算，而是将其蒸馏为结构化的“智能体技能”，总结重复失败和有效修复模式。这些技能随后指导在真实仓库中生成针对性的修复任务。通过执行验证和基于求解器梯度对齐的奖励评分筛选任务，确保任务对提升求解器能力有用。经过多轮迭代，任务课程不断适应智能体进化。在SWE-bench Verified等四个基准测试上，Socratic-SWE在三轮迭代后持续超越多种自进化基线方法，在SWE-bench Verified上达到50.40%的准确率。结果表明，历史求解轨迹可以作为自进化SWE智能体的可扩展训练信号来源，通过技能引导的任务生成能有效延迟性能饱和，提升数据利用效率。
