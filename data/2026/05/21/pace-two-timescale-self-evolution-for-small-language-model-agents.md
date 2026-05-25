---
title: "PACE: Two-Timescale Self-Evolution for Small Language Model Agents"
authors:
  - "Chen Ling"
  - "Pei Chen"
  - "Albert Guan"
  - "Jiaming Qu"
  - "Shayan Ali Akbar"
  - "Madhu Gopinathan"
  - "Erwin Cornejo"
date: "2026-05-21"
arxiv_id: "2605.23019"
arxiv_url: "https://arxiv.org/abs/2605.23019"
pdf_url: "https://arxiv.org/pdf/2605.23019v1"
categories:
  - "cs.LG"
tags:
  - "小语言模型Agent"
  - "自进化Agent"
  - "提示词优化"
  - "控制逻辑演进"
  - "多时间尺度框架"
  - "工具使用Agent"
relevance_score: 9.5
---

# PACE: Two-Timescale Self-Evolution for Small Language Model Agents

## 原始摘要

Deploying language-model agents in production often requires substantial compute and human effort to tune prompts, parsers, validators, and other components of the agent pipeline. Self-evolution offers a promising alternative, but most existing frameworks assume access to frontier models that can reliably diagnose failures, propose revisions, and judge their own updates. We study whether frozen small language models (SLMs) can serve as effective self-evolving agents under resource constraints. We propose PACE (Prompt And Control Logic Evolution), a two-timescale framework that coordinates low-risk prompt refinement with higher-risk control-logic updates. PACE evolves prompts under fixed control logic until prompt-level gains saturate, then considers constrained control-logic updates that are accepted through held-out validation. Across three frozen SLM backbones ranging from 4B to 14B parameters and four controlled benchmarks, PACE achieves the best performance on all 12 backbone--benchmark combinations, improving over vanilla SLM agents by up to +9.2% relative improvement and over the stronger single-mode evolution baseline by up to +5.4% relative improvement. A tau-bench case study further shows that PACE improves multi-turn tool-use success over vanilla and prompt-only evolution. These results suggest that reliable SLM agent self-evolution is possible without updating model weights or relying on frontier-model teachers, and that the key benefit is not any single final solver pattern but autonomous, validated discovery of task-appropriate inference strategies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在资源受限环境下，如何利用冻结的小语言模型（SLM）进行有效的智能体自我进化问题。现有方法大多依赖强大的前沿模型来诊断失败、提出修订和判断更新，但SLM能力较弱，对提示复杂度敏感，且多次提示修订后性能提升容易饱和。同时，允许SLM自由修改执行控制逻辑（如解析、验证、重试规则等）可能不稳定，导致语法有效但语义错误的更新，引发回归。因此，核心挑战在于如何在冻结SLM权重且无法依赖教师模型的前提下，实现可靠的自进化。本文提出PACE框架，通过双时间尺度协调低风险的提示精炼与高风险的逻辑更新，先利用提示进化直至饱和，再通过保留验证集谨慎引入控制逻辑更新，从而可靠地提升SLM智能体的性能。

### Q2: 有哪些相关研究？

相关工作可分为两类：**提示空间演化**和**控制逻辑演化**。提示空间演化方法通过执行反馈优化系统提示、任务指令等纯文本组件，但不改变控制逻辑，具有稳定性高、样本效率好的优点，适用于冻结的小语言模型（SLM）。然而，这类方法无法修复解析错误、验证缺失或重试逻辑等结构性瓶颈，性能容易饱和。控制逻辑演化方法则允许智能体修改自身的可执行逻辑，如控制流、验证规则和推理时配置，常通过递归自我改进实现。但其局限性在于，当提议模型（如SLM）能力较弱时，频繁的结构修改可能导致不稳定。

PACE与两者的核心区别在于：它不将提示和控制逻辑更新视为独立优化目标，而是将两者纳入一个**双时间尺度**框架——在固定控制逻辑下优先进行低风险的提示演化，直到提示增益饱和；随后才进行高风险的逻辑演化，且更新必须通过保留验证集的验证。与现有方法相比，PACE并非简单允许两种更新，而是通过**显式调度与验证门控**来协调其风险，解决了提示演化无法修复结构问题、控制逻辑演化在小模型上不稳定的双重困境。

### Q3: 论文如何解决这个问题？

PACE提出了一个双时间尺度（two-timescale）自演化框架，用于冻结的小语言模型（SLM）智能体。其核心在于将智能体定义为 (P, C) 两部分：P 是文本提示（如系统提示、指令），C 是控制逻辑（如解析、验证、重试等可执行代码）。PACE 的创新在于区分了两种不同风险的演化操作，并协调它们：

1.  **低风险提示演化 (Prompt Evolution, PE)**：在固定控制逻辑 C 下，频繁迭代优化提示 P。它通过三种通道生成候选提示：手工设计的突变、基于 SLM 对失败进行根因分析后生成的反思性候选、以及将帕累托前沿上最互补的两个配置进行交叉合并。候选提示在训练小批量上评估，并维护一个权衡准确性与成本的帕累托前沿。当提示层面收益饱和时（即性能提升低于阈值），才触发更高风险的操作。

2.  **高风险控制逻辑演化 (Constrained Control Logic Evolution, CE)**：当提示演化饱和后，PACE 对控制逻辑 C 进行有界编辑。这些编辑受限于固定的求解器接口和资源预算，影响的是输出解析、验证、重试、采样配置等组件。关键原则是：**所有控制逻辑编辑都需通过保留验证集的实证检验**。只有新候选者(A_new)在验证集上的效用显著高于旧版本(A_old)（超过验证门控阈值δ），且满足资源约束时，才会被接受。接受后，PACE 会再次启动提示演化以适应新的控制逻辑。

整体架构由一个人工智能控制器（agentic controller）协调这两个模块，形成循环：持续进行提示演化直到饱和 → 基于失败分析提出有界控制逻辑更新 → 通过保留验证集的实证检验后才提交更新 → 更新后重新启动提示演化。该方法不更新模型权重，也不依赖前沿模型教师，实现了资源受限下 SLM 智能体的自主、已验证的演化。

### Q4: 论文做了哪些实验？

论文在四个静态基准和tau-bench多轮工具使用案例上进行了全面实验。静态基准包括MMLU（知识密集型多选题）、MGSM（多语言数学推理）、HotpotQA（多跳问答）和IFEval（可验证指令遵循），采用各自标准指标（如准确率、精确匹配）。使用三个冻结的小语言模型骨干（Qwen3-4B、Qwen3.5-9B、Ministral-3-14B），对比方法包括：朴素SLM、仅提示演化（+PE）、仅控制逻辑演化（+CE）以及现有优化器（MIPROv2、GEPA、ACE、Gödel Agent），并以DeepSeek-V3.2-685B作为前沿参考。主要结果：PACE在所有12个骨干-基准组合上取得最佳性能，相对朴素SLM提升最高达+9.2%，相对更强的单模式演化基线提升达+5.4%。例如在Qwen3.5-9B上，PACE在MMLU上达到0.889（+8.6%）、IFEval上0.761（+9.2%），并在HotpotQA上超越DeepSeek-V3.2参考（0.803 vs 0.779）。在tau-bench零售和航空领域的多轮任务中，PACE稳定提升一致性，Qwen3.5-9B+PACE在所有pass^k指标上超越Sonnet 3.5和GPT-4o。消融实验验证了信用分配阈值ε=0.01和验证门控阈值δ=0.02的设计最优。

### Q5: 有什么可以进一步探索的点？

PACE框架的局限性在于其验证依赖于固定的held-out集，可能无法覆盖长尾或动态分布的任务场景，导致演化策略过拟合验证集；同时两时间尺度中逻辑层更新的“保守”策略虽然降低了风险，但也可能错过激进但高效的探索机会，尤其在高复杂度工具调用场景中性能提升边际递减。未来可探索的方向包括：(1)引入在线验证机制或对抗性评估，使演化能适应环境变化和潜在分布偏移；(2)设计更灵活的风险控制策略，如基于不确定性估计动态调整逻辑层更新阈值，或结合贝叶斯优化解耦探索-利用；(3)利用演化轨迹中失败案例生成偏好数据，训练专用控制器实现元学习式初始化，减少冷启动成本；(4)探索多智能体协作演化范式，通过智能体间互评和知识蒸馏突破单一SLM能力上限。

### Q6: 总结一下论文的主要内容

部署语言模型代理需要大量计算和人工调优。PACE 提出双时间尺度自我进化框架，在固定控制逻辑下优先进行低风险提示优化，当提示改进饱和后再进行通过验证的受限控制逻辑更新。在4B到14B的三个冻结小语言模型和四个基准测试中，PACE在所有12个模型-基准组合上均取得最佳性能，相比原始模型提升最高9.2%，相比单模式进化基线提升最高5.4%。tau-bench案例研究显示PACE能改善多轮工具使用成功率。核心结论是：无需更新模型权重或依赖前沿教师模型，冻结小语言模型即可通过自主、验证的推理策略发现实现有效自我进化，关键在于协调不同风险的更新节奏。
