---
title: "SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents"
authors:
  - "Yifan Zhou"
  - "Zhentao Zhang"
  - "Ziming Cheng"
  - "Shuo Zhang"
  - "Qizhen Lan"
  - "Zhangquan Chen"
  - "Zhi Yang"
  - "QianyuXu"
  - "Ronghao Chen"
  - "Huacan Wang"
  - "Sen Hu"
date: "2026-05-18"
arxiv_id: "2605.18693"
arxiv_url: "https://arxiv.org/abs/2605.18693"
pdf_url: "https://arxiv.org/pdf/2605.18693v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Skill Generation"
  - "Benchmark"
  - "Tool Use"
  - "Code Agent"
relevance_score: 8.5
---

# SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents

## 原始摘要

As LLM agents are increasingly built around reusable skills, a central challenge is no longer only whether agents can use provided skills, but whether they can generate correct, reusable, and executable skills from repositories and documents. Existing benchmarks primarily evaluate the efficacy of given skills or the ability of agents to solve downstream tasks from raw context, but they do not isolate skill generation itself as the object of study. We introduce SkillGenBench, a benchmark for evaluating skill generation pipelines under a unified and controlled protocol. In SkillGenBench, a generator receives raw corpora and produces standardized skill artifacts, which are then executed under fixed harnesses and assessed with unified evaluation procedures. The benchmark covers two generation regimes: task-conditioned generation, where a task-specific skill is synthesized after the task is revealed, and task-agnostic generation, where a reusable skill library must be distilled before downstream tasks are known. It also spans two complementary procedural sources: repository-grounded instances, where procedures are distributed across code, configuration, and scripts, and document-grounded instances, where procedures and constraints must be distilled from long-form text. We provide standardized task specifications, pinned environments, and evaluation protocols centered on deterministic execution-based checks, supplemented by auxiliary signals for diagnosis. Experiments across a range of skill-generation methods and backbones show substantial performance variation, highlight the difficulty of reusable skill distillation, and reveal distinct failure modes in skill generation from software repositories versus long-form documents. SkillGenBench establishes a reproducible testbed for studying skill generation as an independent research problem in agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基准测试无法独立评估LLM Agent技能生成能力的问题。研究背景是，随着LLM Agent系统的发展，人们发现将程序性知识外化为可复用的技能（skill）比单纯的上下文推理更利于审计、缓存、共享和组合，但现有评估存在明显不足：一方面，如CL-Bench所示，模型在复杂上下文中难以提取并正确操作化相关证据；另一方面，SkillsBench表明即便技能很重要，但自动生成的技能往往不稳定甚至导致负迁移。当前主流的基准测试要么评估给定技能的效能（如SkillsBench），要么评估Agent在原始上下文中解决下游任务的能力，但都没有将技能生成本身作为独立的研究对象进行隔离评估。因此，本文提出SkillGenBench，核心目标是建立一个统一的、受控的协议来直接评估技能生成管线（skill generation pipelines）。它设计了两种生成模式——任务条件生成（已知任务后合成技能）和任务无关生成（在未知下游任务前蒸馏可复用技能库），并覆盖代码仓库和长文档两种程序性知识来源。通过固定执行框架和确定性执行检查，该基准旨在将技能生成作为一个独立的可研究问题，为比较不同生成方法提供可复现的测试平台。

### Q2: 有哪些相关研究？

相关研究主要包括三大类：**方法类**工作聚焦技能生成的技术路径，如从代码库、文档或智能体经验中提取可复用技能，通过迭代执行反馈或结构验证进行优化；**评测类**工作如SkillsBench和SWE-Skills-Bench，它们主要评估给定技能在任务中的有效性，而非技能生成本身的质量。SkillsBench比较了无技能、给定技能和自生成技能在确定性验证下的表现，发现自生成技能不稳定；SWE-Skills-Bench则将相似逻辑应用于软件工程领域，结合公共技能和固定提交版本的真实仓库进行需求驱动验证。

本文与这些工作的核心区别在于：**研究焦点的转移**——现有评测将技能生成与下游执行、路由策略等耦合在一起，无法独立评估生成管道本身的质量；而SkillGenBench首次将技能生成管道作为独立对象进行评测。**评测维度的扩展**——现有基准仅覆盖“任务条件生成”（任务已知后生成技能），本文新增了“任务无关生成”（未知任务前预先蒸馏可复用技能库），并引入仓库文档和长文档两种来源。**评估协议的统一**——所有生成的技能均在固定测试框架和确定性验证下评估，保证了不同方法之间的可比性，从而揭示了从仓库和文档中提取技能时不同的失败模式。

### Q3: 论文如何解决这个问题？

SkillGenBench通过一个统一的、受控的协议来评估技能生成流水线。其核心方法是将技能生成与下游执行解耦，从而直接衡量程序到技能的蒸馏能力。整体框架围绕一个基准实例，每个实例打包为一个容器化环境，包含五个组件：源材料、任务规范、技能接口、执行器和评估协议。

主要模块和关键技术包括：
1. **双来源与双设定**：基准覆盖两种程序知识来源——代码仓库（程序知识隐含在代码结构、配置和脚本中）和长文档（程序知识显式但分散在文本中）。同时定义两种生成设定——任务条件式（已知下游任务，提取相关技能）和任务无关式（未知下游任务，构建可复用的技能库）。
2. **五阶段构建流水线**：从源材料出发，经过知识图谱构建、场景生成、任务与测试用例生成、无技能验证、有技能验证，最终通过人工审核，确保任务具有挑战性且可程序化验证。
3. **评估机制**：采用基于执行的评估（对隐藏测试用例运行生成的代码，比较确定性输出）和基于产物的评估（执行代码生成产物并与参考输出比较）。所有技能在固定执行器下运行，且测试用例、验证器内部和参考输出对生成模型不可见。
4. **创新点**：首次将技能生成本身作为独立研究对象，而非仅评估下游任务解决能力。通过解耦生成与执行、统一不同来源的任务格式、以及提供容器化固定环境，建立了可复现的基准测试平台，揭示了技能生成在代码仓库与长文档场景下的不同失效模式。

### Q4: 论文做了哪些实验？

论文在SkillGenBench基准上进行了全面实验。实验设置方面，评估了五种技能生成方法（Naive Prompt、EvoSkill、SkillNet、SkillCreator、SkillSeekers），涵盖基于提示、工作流和自演进三类。对于每种方法，使用六个骨干模型（Claude Sonnet 4.5、GPT-5、Kimi K2.5、GLM-5、MiniMax-M2.7、Qwen3.6-Plus）生成技能，并固定下游执行器为MiniMax-2.5，所有技能均在统一评估框架下通过实例特定验证器进行确定性执行评估。主要指标为pass@3，每个技能最多进行三次独立试验。数据集包含187个任务，分为代码仓库和文档（代码文档+领域知识文档）两类源。

主要结果显示：SkillSeekers在六个骨干模型上取得最佳平均性能（代码14.4%，文档25.0%），而所有方法在代码任务上的表现（10.8%-14.4%）远低于文档任务（21.4%-25.0%）。任务无关技能生成普遍弱于任务条件生成，在某些情况下甚至低于无技能基线。静态诊断分析显示SkillNet在结构和环境方面得分最高（整体59.1），但与其执行性能不匹配，表明结构完整性与可执行性存在差异。失败分析揭示：代码仓库故障主要由运行时/依赖问题（53%）引起，代码文档故障集中在接口/模式错误（85%），领域知识文档故障则以状态/规则错误（44%）和数值/公式错误（37%）为主。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向可从以下几个层面展开：首先，当前基准主要依赖确定性执行检查，缺乏对技能可迁移性、鲁棒性（如输入边界条件）及跨环境适应性的评估，未来可引入对抗性测试或动态环境变异。其次，仓库型任务中隐式执行结构的恢复仍是瓶颈，可探索将代码依赖图、系统调用日志等结构化信息显式注入生成管道，或采用程序合成中常用的“执行引导搜索”策略。此外，当前方法虽生成结构正确的技能，但常因接口对齐或状态处理偏差导致执行失败，这说明需要更细粒度的“行为约束规范”（如状态机或断言模板）。另一个值得深入的方向是任务无关的技能库蒸馏，现有方法在泛化性上表现较差，可借鉴元学习或增量聚类思想，从多个任务中逐步抽象共享功能模块。最后，测评框架本身可扩展至多代理协作场景，验证技能生成系统能否支持角色分工与交互协议。

### Q6: 总结一下论文的主要内容

SkillGenBench提出了一个评估大型语言模型技能生成管道的基准。其核心贡献在于将技能生成本身作为独立研究对象，而非仅评估给定技能的有效性或下游任务能力。该基准在两个生成场景下进行评估：任务条件生成（根据任务规范合成技能）和任务无关生成（在未知下游任务前提炼可复用技能库）。它涵盖两种程序性知识来源：基于代码仓库的实例（需从分布式代码、配置中恢复程序）和基于文档的实例（需从长文本中提炼程序与约束）。主要结论是，技能生成本质上是一个管道级问题，性能受生成方法、骨干模型和源材料性质影响，特别是基于仓库的任务比文档任务更具挑战性，且生成的技能虽捕捉到正确结构，但常无法转化为满足严格验证约束的可执行程序。该基准为独立研究技能生成提供了可重复的测试平台。
