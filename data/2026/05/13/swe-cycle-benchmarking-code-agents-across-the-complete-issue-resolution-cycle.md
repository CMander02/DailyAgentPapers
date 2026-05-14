---
title: "SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle"
authors:
  - "Hao Guan"
  - "Lingyue Fu"
  - "Shao Zhang"
  - "Yaoming Zhu"
  - "Kangning Zhang"
  - "Lin Qiu"
  - "Xunliang Cai"
  - "Xuezhi Cao"
  - "Weiwen Liu"
  - "Weinan Zhang"
  - "Yong Yu"
date: "2026-05-13"
arxiv_id: "2605.13139"
arxiv_url: "https://arxiv.org/abs/2605.13139"
pdf_url: "https://arxiv.org/pdf/2605.13139v1"
categories:
  - "cs.SE"
tags:
  - "LLM Agent"
  - "Code Agent"
  - "Benchmark"
  - "SWE-bench"
  - "Agent Evaluation"
  - "Software Engineering Agent"
  - "Multi-task Agent"
  - "Autonomous Agent"
relevance_score: 9.5
---

# SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle

## 原始摘要

As autonomous code agents move toward end-to-end software development, evaluating their practical autonomy becomes critical. Current benchmarks hide friction by testing agents in pre-configured environments, and their static evaluation pipelines frequently fail when parsing fully autonomous trajectories. We address these limitations with SWE-Cycle, a benchmark of 489 rigorously filtered instances. SWE-Cycle evaluates agents across three isolated tasks, including environment reconstruction, code implementation, and verification test generation, as well as an end-to-end FullCycle task that integrates all three. The FullCycle task requires agents to work autonomously in a bare repository without human scaffolding. To reliably assess these complex execution paths, we developed SWE-Judge. By combining static code review with dynamic testing, this execution-capable evaluation agent accurately verifies functional correctness and eliminates the systematic measurement errors of traditional static parsers. We evaluate code agents powered by six state-of-the-art LLMs across these four tasks. The results reveal a sharp drop in solve rates when transitioning from isolated tasks to FullCycle execution, exposing critical bottlenecks in handling cross-phase dependencies and maintaining code quality. Together, SWE-Cycle and SWE-Judge provide a comprehensive framework for accurately measuring the end-to-end capabilities of autonomous software agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前代码智能体评估体系中的两个核心缺陷：评估任务的人为割裂和评估方法的静态脆弱性。研究背景是，随着大语言模型和智能体框架的进步，代码智能体已能处理完整的工程级项目，但其实际自主能力需要更真实的评估。现有方法的不足体现在两方面：首先，现有基准测试将问题解决的完整流程（环境重建、代码实现、验证测试生成）人为隔离，并为智能体提供预配置环境，这屏蔽了真实世界中的级联错误和集成摩擦（如依赖解析、版本控制导航），导致高分结果严重高估了智能体的真实自主性，造成了能力假象。其次，传统的静态评估管线依赖预定义测试用例和刚性解析器，这些脚本不仅常因格式差异误判正确代码，而且无法适应智能体在端到端场景下的动态和自主行为，产生系统性测量误差，甚至完全失效。因此，本文要解决的核心问题是：如何设计一个能够准确、鲁棒地评估代码智能体在完整问题解决生命周期中真实自主能力的基准测试和评估框架。为此，论文提出了SWE-Cycle基准，通过构建包含环境重建、代码实现和验证测试生成的完整周期任务，以及一个结合静态审查与动态执行的SWE-Judge评估智能体，来克服现有范式的局限性。

### Q2: 有哪些相关研究？

在相关研究方面，本文涉及三类工作。第一类是代码智能体基准测试。以SWE-bench为代表的基准测试为评估代码智能体在真实GitHub工单上的表现建立了标准，但存在结构性局限：它们提供预构建的Docker环境并依赖固定测试套件，完全排除了环境重构和测试生成。其他变体虽在实例质量、多语言、长周期等维度上改进，但都继承了这一局限。第二类是环境构建基准，如EnvBench，它孤立地评估环境重构能力，与下游代码实现和验证测试生成完全脱节。第三类是自动化评估方法。传统单位测试存在缺陷，而LLM-as-a-judge方法存在位置偏差和无法验证运行时行为的根本局限。SWE-Cycle通过SWE-Judge采用Agent-as-a-Judge范式，将静态代码审查与动态测试执行结合，克服了这些局限。与现有基准相比，SWE-Cycle独有的特点是：它是一个覆盖环境重构、代码实现和验证测试生成三个孤立任务以及完整端到端工单解决流程的连贯框架，并采用可执行的细粒度评估智能体进行评测。

### Q3: 论文如何解决这个问题？

为了解决传统基准测试中环境预配置和静态评估管道脆弱性的问题，SWE-Cycle 提出了一个包含数据集蒸馏、任务分解和混合评估的完整框架。其核心方法分为三个部分：

1. **数据集蒸馏**：通过一个严格的三阶段过滤管道从 SWE-bench 等数据集中筛选出 489 个高质量实例。首先采用“零上下文探测”机制检测数据污染，即让 LLM 在没有问题描述的情况下生成补丁，若成功则视为训练数据泄露。其次，通过检查 Pull Request 是否包含至少一个代码评审意见且解决周期超过一天，过滤掉琐碎任务。最后，通过执行金标准测试验证状态转换的可靠性，过滤掉测试套件有缺陷的实例。

2. **任务分解与框架**：将问题解决生命周期分解为三个隔离任务：**环境重建 (Env)**（从源码独立构建 Docker 环境）、**代码实现 (Impl)**（根据问题描述修改代码）、**验证测试生成 (TestGen)**（为修复后的代码生成针对性单元测试），以及一个端到端的 **FullCycle** 任务，要求智能体在没有人类脚手架的情况下，自主完成从环境搭建到测试生成的全流程。

3. **混合评估智能体 SWE-Judge**：其创新点在于结合**静态代码审查**和**动态执行**。对于每个任务，SWE-Judge 先进行静态分析（如检查依赖缺失、代码逻辑），再进行分阶段动态验证（如环境激活、测试执行）。最关键的是，它引入了**测试干预机制**：若智能体生成的测试质量差，SWE-Judge 会基于官方测试进行细化，以确保后续代码实现的动态评估的准确性。这种容错管道能隔离上游失败，防止其无效化下游评估，从而精准衡量智能体在完整生命周期中的端到端能力。

### Q4: 论文做了哪些实验？

论文在SWE-Cycle基准上评估了6个LLM（GPT-5.4、Claude-Sonnet-4.6、Qwen-3.5、GLM-5.1、Kimi-K2.5、MiniMax-M2.7）驱动的代码智能体，涵盖4个任务：环境重构（Env）、代码实现（Impl）、验证测试生成（TestGen）及端到端的FullCycle。实验使用OpenCode框架，在隔离Docker容器中运行，孤立任务限时90分钟，FullCycle限时3小时。采用静态（Static）、动态（Dynamic）、综合得分（Score）和完美解决率（Solve）四项指标（0-1归一化后百分比）。主要结果包括：

- **孤立任务**：Env任务Solve率最高（Claude达78.12%），Impl是主要瓶颈（Solve率普遍低于40%）。Claude-Sonnet在Env（Solve 78.12%）、Impl（Solve 40.08%）和TestGen（Solve 67.28%）上均最优。
- **FullCycle任务**：相比孤立任务，阶段得分有所提升但Solve率骤降（最高仅GLM的13.50%），静态得分普遍低于动态。失败分析表明复合错误（如Impl+TestGen同时失败）占主导，存在强级联效应。
- **SWE-Judge可靠性验证**：人工标注显示SWE-Judge与人类判断在4个任务中一致率均超95%（全周期96.9%），在371例与脚本评估的分歧中，SWE-Judge正确率98.6%，而脚本仅0.5%。SWE-Judge通过动态测试（如自适应脚本编写、故障注入）克服了脚本的僵硬性、评估崩溃和过度宽容问题。
- **集成效应**：端到端任务中，上游Env和Impl受惠于上下文迭代，但下游TestGen全面退化；阶段消融实验证实各阶段紧密耦合，移除测试阶段会严重损害整体性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在当前基准仅针对单次issue修复的完整周期，未涉及多issue协作、代码库演进等更复杂场景。未来可从三个方向深入：第一，引入动态协作任务，如多个agent分别负责不同issue修复或代码审查，模拟真实团队协作；第二，构建持续维护场景，要求agent在多个版本迭代中保持代码质量不退化，并处理技术债务；第三，提升环境适应能力，当前FullCycle任务虽去除了脚手架，但仍是预设仓库，可考虑动态生成半结构化需求或加入不完整文档，测试agent的主动信息获取能力。此外，SWE-Judge虽结合静态与动态测试，但在代码风格一致性、安全漏洞检测等软性指标上仍存盲区，可借鉴学术界自监督学习思路开发代码“预训练+微调”的自动评估器。最终目标是推动agent从“单点修复”向“软件全生命周期自治”跃迁。

### Q6: 总结一下论文的主要内容

SWE-Cycle是一个针对代码智能体在完整问题解决周期中自主能力的基准测试。现有基准在预配置环境中测试、依赖静态评估管道，易因解析失败而测量错误。为此，SWE-Cycle构建了489个精调实例，定义了三项隔离任务（环境重建、代码实现、验证测试生成）及一项端到端FullCycle任务。后者要求智能体在无人工辅助的裸仓库中自主工作。为可靠评估这些复杂执行路径，论文提出SWE-Judge评估代理，它结合静态代码审查与动态测试来准确验证功能正确性，避免了传统静态解析器的系统性测量误差。实验评估了六个最先进LLM驱动的代码智能体在上述四项任务的表现，结果显示从隔离任务转向FullCycle执行时解决率显著下降，暴露出智能体在跨阶段依赖处理和代码质量维护上的关键瓶颈。SWE-Cycle与SWE-Judge共同为准确衡量自主软件智能体的端到端能力提供了综合框架。
