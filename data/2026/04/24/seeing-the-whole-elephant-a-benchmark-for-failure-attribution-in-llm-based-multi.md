---
title: "Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems"
authors:
  - "Mengzhuo Chen"
  - "Junjie Wang"
  - "Fangwen Mu"
  - "Yawen Wang"
  - "Zhe Liu"
  - "Huanxiang Feng"
  - "Qing Wang"
date: "2026-04-24"
arxiv_id: "2604.22708"
arxiv_url: "https://arxiv.org/abs/2604.22708"
pdf_url: "https://arxiv.org/pdf/2604.22708v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent System"
  - "Failure Attribution"
  - "Benchmark"
  - "Debugging"
  - "Trace Analysis"
  - "LLM-based Agent"
relevance_score: 9.5
---

# Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems

## 原始摘要

Failure attribution, i.e., identifying the responsible agent and decisive step of a failure, is particularly challenging in LLM-based multi-agent systems (MAS) due to their natural-language reasoning, nondeterministic outputs, and intricate interaction dynamics. A reliable benchmark is therefore essential to guide and evaluate attribution techniques. Yet existing benchmarks rely on partially observable traces that capture only agent outputs, omitting the inputs and context that developers actually use when debugging. We argue that failure attribution should be studied under full execution observability, aligning with real-world developer-facing scenarios where complete traces, rather than only outputs, are accessible for diagnosis. To this end, we introduce TraceElephant, a benchmark designed for failure attribution with full execution traces and reproducible environments. We then systematically evaluate failure attribution techniques across various configurations. Specifically, full traces improve attribution accuracy by up to 76\% over a partial-observation counterpart, confirming that missing inputs obscure many failure causes. TraceElephant provides a foundation for follow-up failure attribution research, promoting evaluation practices that reflect real-world debugging and supporting the development of more transparent MASs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统（MAS）中故障归因（failure attribution）缺乏可靠基准的问题。研究背景方面，MAS通过自然语言进行推理和交互，其非确定性输出和复杂的动态交互使得故障归因极具挑战性。现有方法的不足体现在：目前唯一的专用基准Who\&When仅提供部分可观测的执行轨迹（仅包含智能体的输出，而缺失任务指令、提示词、中间消息等关键输入上下文），这导致在至少21%的故障案例中，开发者无法基于输出日志进行可靠归因。本文提出的核心问题是：在开发者实际调试场景（即拥有完整执行轨迹和可复现运行环境）下，如何系统评估和提升故障归因技术的有效性？为此，论文构建了TraceElephant基准，通过提供220个包含完整步骤级执行轨迹、可复现运行环境的故障案例，使研究人员能在全观测条件下对故障根源进行精确定位。实验表明，完整轨迹能将归因准确率提升高达76%，从而为开发更透明、更可调试的MAS奠定基础。

### Q2: 有哪些相关研究？

相关工作主要分为三类。**方法类**包括：FAMAS通过重复重放失败任务并执行谱系分析来定位故障；AgentTracer采用多粒度强化学习训练轻量级模型，同时优化步骤级和智能体级归因；GraphTracer将智能体交互建模为信息依赖图，追踪因果信息流；ECHO结合层次化上下文表示、目标分析评估和共识投票提升归因准确性。**评测类**方面，现有基准仅依赖部分可观测轨迹（仅记录智能体输出），忽略了开发者调试时实际使用的输入和上下文，导致许多失败原因被遮蔽。

本文提出的TraceElephant与上述工作的核心区别在于：1）首次要求**完全执行可观测性**，提供包含输入、中间状态和完整上下文的执行轨迹，更贴近真实调试场景；2）构建了可复现的多智能体环境，支持系统性归因技术评测；3）实验表明完整轨迹相比部分观测方案能提升最高76%的归因准确率。这为后续研究提供了更符合现实需求的评估基础。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 TraceElephant 的基准测试，系统性地解决了 LLM 多智能体系统中的故障归因问题。其核心方法是提供全执行轨迹的完全可观测性，而非传统方法仅依赖部分输出。

首先，论文定义了故障归因问题：在基于回合制的多智能体系统中，每个执行步骤记录完整的输入、输出及执行组件信息。归因目标包括两个层面：步骤级（识别故障变得不可避免的最早时间点）和智能体级（识别该步骤中导致故障的组件）。归因遵循“角色感知”和“可恢复性感知”原则，即若上游错误本可被后续（如检查器）组件恢复但未被执行，则故障归因于该恢复失败点。

在基准构建上，TraceElephant 收集了来自三个代表性系统的 220 个失败轨迹，涵盖动态组队（Captain-Agent）、固定角色编排（Magentic-One）和单智能体工具脚手架（SWE-Agent）。其关键技术在于一个轻量级 LLM API 中间件，它能透明地拦截并捕获所有 LLM 请求、响应及工具交互，从而保留完整的执行上下文（包括输入上下文、系统构造信息、智能体配置等），而非仅输出。每个轨迹实例包含元数据、完整的步骤级记录（含输入和输出字段）以及经过多轮专家标注的故障标签。

在评估中，论文设计了多种归因技术（如全量分析、二分搜索、逐步分析、静态智能体分析和动态智能体分析）。动态配置通过允许重放执行和反事实探查来验证候选归因，实现了最佳性能（步骤级准确率提升 10% 至 33.3%）。消融实验证实，完整轨迹（特别是输入和元数据字段）对准确归因至关重要：移除输入字段导致步骤级准确率下降 76%。对比发现，纯输出设置（类似现有基准）表现显著更差，因为缺失了组件决策时所观察到的真实上下文。主要创新点在于：1) 提出了完全执行轨迹可观测性的归因范式；2) 构建了首个覆盖多种架构、包含完整上下文的基准；3) 系统评估并揭示了全观测相比部分观测的显著优势。

### Q4: 论文做了哪些实验？

论文针对基于LLM的多智能体系统（MAS）中的故障归因问题进行了系统实验。实验设置包括静态配置（一次性、二分查找、逐步、静态智能体）和动态配置（动态智能体），在三个系统（Captain-Agent、Magentic-One、SWE-Agent）上评估，数据集为作者提出的TraceElephant基准。对比方法主要有五种：三种基于LLM的提示技术（All-at-Once、Binary Search、Step-by-Step）和两种基于智能体的技术（Static Agentic、Dynamic Agentic）。主要结果如下：在完整观测下，动态配置表现最佳，步级准确率达33.3%，代理级准确率达66.7%；静态智能体配置次之。消融实验表明，完整轨迹（含元数据和输入）至关重要：移除输入使代理级准确率从62%降至54%，步级准确率从28%降至18%（下降76%）。在输出仅限设置（类似Who&When基准）下，代理级准确率仅51%，步级准确率16%。骨干LLM对比中，Claude-4.5-Sonnet和DeepSeek-R1表现较强。无真实标签时性能普遍下降，但动态智能体下降幅度较小。

### Q5: 有什么可以进一步探索的点？

该论文的主要局限体现在三个方面。首先，基准只覆盖了三种代表性MAS架构（动态团队、集中编排和软件工程流程），虽然具有多样性但未涵盖更多新兴架构如分层式或完全去中心化系统，这可能导致结论的泛化性受限。其次，论文假设开发者拥有完全执行轨迹（即白盒场景），但现实中API代理、黑盒商业系统等仅提供部分观测的场景同样普遍，未来的研究需要建立支持部分观察和噪声轨迹的归因基准。此外，当前仅针对单步故障归因，而现实故障常涉及多步连锁错误。未来可探索以下方向：1) 开发更细粒度的跨步骤交互依赖归因方法（如引入反事实推理或Shapley值分解）；2) 结合可解释AI工具自动生成自然语言故障解释而非仅标识责任点；3) 设计能适应动态重配置代理（任务中途增减代理）的鲁棒归因框架。

### Q6: 总结一下论文的主要内容

故障归因——即识别导致失败的智能体和关键步骤——在基于大语言模型的多智能体系统（LLM-based MAS）中极具挑战性，这源于其自然语言推理、非确定性输出及复杂交互动态。现有基准依赖仅捕捉智能体输出的部分可观测轨迹，忽略了开发者实际调试时所用的输入和上下文。本文提出TraceElephant基准，在完整可执行轨迹和可复现环境下研究故障归因。实验表明，完整轨迹相比部分可观测方法将归因准确率提升高达76%，证实缺失输入会掩盖大量故障原因。该工作为后续故障归因研究提供了基础，促进了反映真实调试的评估实践，助力开发更透明的多智能体系统。
