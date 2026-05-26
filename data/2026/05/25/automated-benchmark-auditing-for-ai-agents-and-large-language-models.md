---
title: "Automated Benchmark Auditing for AI Agents and Large Language Models"
authors:
  - "Junlin Wang"
  - "Federico Bianchi"
  - "Shang Zhu"
  - "Fan Nie"
  - "Yongchan Kwon"
  - "Bhuwan Dhingra"
  - "James Zou"
date: "2026-05-25"
arxiv_id: "2605.26079"
arxiv_url: "https://arxiv.org/abs/2605.26079"
pdf_url: "https://arxiv.org/pdf/2605.26079v1"
categories:
  - "cs.CL"
tags:
  - "Agent评估基准"
  - "Agent审计"
  - "基准测试验证"
  - "Agent鲁棒性"
relevance_score: 8.5
---

# Automated Benchmark Auditing for AI Agents and Large Language Models

## 原始摘要

Modern AI benchmarks operate at a complexity that outpaces traditional verification methods. Tasks authored by domain experts often contain implicit assumptions, incomplete environment specifications, and brittle evaluation logic that human annotation cannot reliably catch. We introduce Auto Benchmark Audit (ABA), an agentic framework that systematically audits individual benchmark tasks, uncovering issues such as hidden environment dependencies, specification gaps, and limited grading logic. We run ABA on a collection of frontier LLM benchmarks and previous NeurIPS publications, totaling 168 benchmarks across nine domains. Across this corpus, ABA identifies critical issues including ambiguous task design, execution environment conflicts, and incorrect ground truths in over 25.7% of the evaluated tasks. The precision of these automated audits is validated by expert review and independent third-party reports such as upstream PRs. Crucially, we demonstrate that these problematic tasks severely distorts capability assessments for agents and LLMs: filtering out these tasks with issues shifts model rankings and increases average performance on SWE-bench Verified and Terminal-Bench 2 by 9.9% and 9.6%, respectively. We release the agentic tool and all task annotations to support the future development of frontier benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现代AI基准测试（benchmark）因复杂性超出传统验证方法能力而导致的可靠性危机。研究背景是，AI领域的进步依赖基准测试作为测量工具，但像SWE-bench、Terminal-Bench这类前沿基准，其任务通常由领域专家设计，包含容器化环境、多阶段评估流程和依赖运行时状态的评分逻辑，导致隐式假设、环境不完整规范和脆弱的评估逻辑等问题难以通过人工审查发现。现有方法的不足在于，传统人工审计（如NLI领域发现标注伪影）依赖通用人力且耗时，但面对专家撰写的复杂任务，通用人员无法填补专业知识鸿沟，而扩大人力规模也无法解决涵盖专家盲区的问题。核心问题是，当基准任务存在隐藏的环境依赖、规范缺口或错误真实值时，会严重扭曲对AI智能体和LLM的能力评估。为此，本文提出Auto Benchmark Audit (ABA)，这是一个智能体框架，能系统性地审计单个基准任务，自动化地发现隐藏问题。通过对168个跨领域基准的审计，ABA识别出超过25.7%的任务存在模糊设计、环境冲突或错误真实值等问题，并验证了这些问题会显著改变模型排名（如SWE-bench和Terminal-Bench性能分别提升9.9%和9.6%），从而实现更准确的能力评估。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **基准有效性批判**：现有工作如Jimenez等人在SWE-bench中发现32.7%的解决方案泄露和弱测试问题；Gao等人发现MMLU中6.49%的项目存在错误；以及DeepFact-Bench的审计-评分流程。这些工作都是基准逐个进行、以专家叙述形式进行批评，而本文提出的自动化基准审计（ABA）则定义了可执行的审计协议，生成统一的发现模式，将临时的批评转化为可重复的测量。

2. **智能体与LLM基准**：包括编程领域（HumanEval、SWE-bench）、交互式智能体基准、多模态智能体、安全与对齐基准等。评估框架如HELM和BIG-bench将底层基准视为可信输入。本文的框架针对多领域环境，在每个任务下生成审计级的证据。

3. **基于LLM的自动评估**：LLM-as-judge方法（如Chatbot Arena）对固定基准的模型输出进行单次判断，但存在位置偏差等系统失效模式。本文的审计器通过工具（文件系统检查、代码执行、容器内省）进行多步调查，直接检测环境漂移、矛盾真实标签等问题。与并行的BenchGuard相比，后者仅审计两个科学基准，而本文在168个基准上跨领域验证了审计粒度。

### Q3: 论文如何解决这个问题？

该论文提出的Auto Benchmark Audit (ABA)框架是一个自动化审计智能体基准测试的智能体系统。其核心方法是通过两阶段流水线架构实现：首先由证据收集代理将异构的基准测试任务（如SWE-bench的JSON格式、Terminal-Bench的目录结构等）统一映射为标准化的清单模式，包括内联轻量数据（如指令文本）和通过文件系统引用隔离重资产（如环境镜像、执行轨迹）。该设计使框架无需针对每个基准单独修改提示或模式，即可扩展到168个跨域基准。

核心审计由审计代理执行，支持两种模式：静态模式仅分析任务定义（指令、测试、配置）；轨迹模式额外读取智能体执行轨迹和测试输出，能捕捉运行时问题。审计过程基于三大独立缺陷轴心：指令缺陷（提示歧义/缺失关键信息）、环境缺陷（运行环境与任务需求冲突）、评估缺陷（测试不公或标准答案错误）。每个发现包含类别、严重性等级（0-2）、证据路径、缺陷描述与修复建议五个字段。

技术关键创新包括：1）异构任务统一表征机制，通过抽象化底层数据结构实现批量接入；2）双模式审计设计，静态扫描结合轨迹分析提升缺陷检出率；3）结构化缺陷分类体系支持跨领域比对。实验验证，经专家审查和第三方PR验证，ABA在25.7%的任务中发现关键缺陷，且过滤后SWE-bench和Terminal-Bench的模型排名分别提升9.9%和9.6%，证明自动审计能有效纠正能力评估偏差。

### Q4: 论文做了哪些实验？

论文围绕Auto Benchmark Audit（ABA）框架进行了系统性实验。实验设置包括两个数据来源：前沿LLM基准（如Opus 4.7等）和NeurIPS 2025接受的基准，共收集168个基准、34,285个任务，覆盖科学、多模态、编程等9个领域。对比方法包括静态审计和轨迹审计，并与基准维护者的修复PR（如Terminal-Bench 2）、第三方基准审计工具BenchGuard及人工审核进行验证。

主要结果：静态审计发现25.7%的任务存在重大缺陷（严重性2级），15.1%含轻微缺陷（严重性1级），仅不到60%的任务是干净的。安全/对齐（42.2%）、医学（41.5%）和专业领域（38.4%）重大缺陷率最高，而数学（13.2%）和编程（14.1%）最低。轨迹审计比静态审计多发现8.5%的重大缺陷任务。在影响评估上，过滤有问题的任务后，SWE-bench Verified和Terminal-Bench 2的平均性能分别提升9.9%和9.6%；轨迹审计下模型平均排名提升10.5%。外部验证显示，ABA在Terminal-Bench 2上严格召回率为66.7%，部分召回率81.0%；在BixBench上严格召回率62.5%（优于BenchGuard的54.2%）；人工审核56个重大缺陷样本精确率为73%（严格）和91%（部分），SWE-bench Verified轨迹审计25个样本精确率达92%/96%。

### Q5: 有什么可以进一步探索的点？

论文的局限与未来方向：首先，ABA当前主要依赖基于规则的静态分析和有限的动态执行，对需要复杂交互的多轮任务或隐式知识依赖的探测能力不足，未来可引入更强的大模型作为审计器，通过链式思考主动发现设计漏洞。其次，审计结果虽经专家验证，但缺乏对问题严重性的量化分级标准，可构建自动化严重度评估模型，区分“致命性错误”与“可容忍偏差”。此外，ABA在对抗性/攻击类基准上的适用性未被探索，可尝试扩展至红队测试数据的审计。未来可设计“元基准”机制，使审计反馈自动触发基准的迭代更新，形成动态闭环。结合我的见解，可借鉴软件工程中的“模糊测试”思想，生成变异任务来探测评价逻辑的鲁棒性；同时建议建立跨基准的“问题模式库”，利用迁移学习提升新基准的审计效率。

### Q6: 总结一下论文的主要内容

本论文介绍了Auto Benchmark Audit (ABA)，一个用于系统审计AI agent和大型语言模型基准测试的自动化框架。针对现代基准测试复杂度超越传统验证方法的问题，ABA通过证据收集智能体和审计智能体，对基准任务的指令、环境和评估三个维度进行结构化缺陷检测。对168个基准测试（涵盖9个领域，超过34000个任务）的评估显示，超过25.7%的任务存在重大缺陷，如隐藏环境依赖、规范缺口和错误标注。通过专家验证和上游PR确认了审计准确性。核心贡献在于，过滤问题任务后，SWE-bench Verified和Terminal-Bench 2上的模型排名平均提升9.9%和9.6%，证明这些问题严重扭曲了能力评估。ABA作为可复现的基准测试质量保障工具，为领域专家提供了系统性发现盲点的方法。
