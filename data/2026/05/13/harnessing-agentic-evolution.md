---
title: "Harnessing Agentic Evolution"
authors:
  - "Jiayi Zhang"
  - "Yongfeng Gu"
  - "Jianhao Ruan"
  - "Maojia Song"
  - "Yiran Peng"
  - "Zhiguang Han"
  - "Jinyu Xiang"
  - "Zhitao Wang"
  - "Caiyin Yang"
  - "Yixi Ouyang"
  - "Bang Liu"
  - "Chenglin Wu"
  - "Yuyu Luo"
date: "2026-05-13"
arxiv_id: "2605.13821"
arxiv_url: "https://arxiv.org/abs/2605.13821"
pdf_url: "https://arxiv.org/pdf/2605.13821v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent进化"
  - "元编辑框架"
  - "长期优化"
  - "过程级状态"
  - "智能体搜索"
relevance_score: 9.5
---

# Harnessing Agentic Evolution

## 原始摘要

Agentic evolution has emerged as a powerful paradigm for improving programs, workflows, and scientific solutions by iteratively generating candidates, evaluating them, and using feedback to guide future search. However, existing methods are typically instantiated either as fixed hand-designed procedures that are modular but rigid, or as general-purpose agents that flexibly integrate feedback but can drift in long-horizon evolution. Both forms accumulate rich evidence over time, including candidates, feedback, traces, and failures, yet lack a stable interface for organizing this evidence and revising the mechanism that drives future evolution. We address this limitation by formulating agentic evolution as an interactive environment, where the accumulated evolution context serves as a process-level state. We introduce AEvo, a harnessed meta-editing framework in which a meta-agent observes this state and acts not by directly proposing the next candidate, but by editing the procedure or agent context that controls future evolution. This unified interface enables AEvo to steer both procedure-based and agent-based evolution, making accumulated evidence actionable for long-horizon search. Empirical evaluations on agentic and reasoning benchmarks show that AEvo outperforms five evolution baselines, achieving a 26 relative improvement over the strongest baseline. Across three open-ended optimization tasks, AEvo further outperforms four evolution baselines and achieves state-of-the-art performance under the same iteration budget.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

现有的智能体进化方法主要分为两类：一是基于固定流程的程序化进化，通过预设的外循环控制候选生成、评估和更新，虽然模块化且可复现，但长期搜索受限，容易陷入局部最优；二是基于通用智能体的进化，赋予智能体灵活整合反馈、编辑候选和探索的能力，但缺少稳定接口来组织进化过程中积累的大量证据（如候选、反馈、轨迹、失败等），导致智能体在长周期进化中容易发生漂移，过度依赖误导性证据或陈旧假设。

本文试图解决的核心问题是：现有方法缺乏一个统一的、稳定的接口来组织进化过程中积累的证据，并据此动态修正驱动未来进化的进化机制。无论是固定流程还是通用智能体，随着时间推移都会积累丰富的上下文信息，但无法将这些信息有效转化为可操作的结构，以系统性地指导搜索方向。为此，论文将智能体进化形式化为一个交互式环境，引入AEvo框架，通过元智能体观察累积的进化状态（过程级状态），并直接编辑控制未来进化的底层程序或智能体上下文，从而在保持灵活性的同时，避免长期进化中的漂移，提升跨长周期的搜索效率。

### Q2: 有哪些相关研究？

相关工作可以分为两类：

1. **智能体进化**：这类方法利用LLM和智能体通过生成、反馈和修订来迭代改进工件。代表性工作包括提示优化方法（如DSPy、SPO、TextGrad、GEPA）、智能体系统自动设计（如ADAS、Darwin Gödel Machine、AFlow、RobustFlow、SkillRL）以及开放发现系统（如AlphaEvolve、OpenEvolve、TTS-Discover等）。本文与这些方法的区别在于，这些方法的搜索行为通常由固定流程或直接管理候选生成的智能体控制，而本文则将进化过程本身视为交互环境，旨在引导控制未来搜索的机制。

2. **智能体元进化**：早期元学习工作表明学习规则本身可被优化（如学习循环强化学习动态或进化策略梯度目标）。近期系统扩展到可编辑智能体程序和记忆系统，如HyperAgents、MemEvolve、ALMA等。与HyperAgents将元改进内化在自修改程序中的方式不同，本文通过外部检索工具将智能体进化视为可观察和编辑的交互环境，同时覆盖手工设计的流程和通用智能体，并将评估和候选记录保持在外部分离管理中。

### Q3: 论文如何解决这个问题？

该论文提出AEvo框架，通过将智能体进化重新定义为交互式环境，并引入“驾驭式元编辑”机制来解决现有方法在长期进化中缺乏稳定接口和方向漂移的问题。核心创新包括：

1. **整体框架**：采用两阶段循环架构，交替进行元编辑阶段和进化片段阶段。元编辑阶段由元智能体观察累积的进化上下文（包括候选方案、反馈、轨迹和失败记录）后，编辑控制未来进化的机制；进化片段阶段则在该更新机制下运行多个迭代。

2. **主要模块**：a) **元智能体**：作为过程级编辑器而非候选项生成器，通过编辑工作区文件（过程代码、提示词、技能、工具、验证器等）和制定运行计划（迭代预算、停止条件）来改变进化机制；b) **驾驭式进化片段**：在元编辑后执行，运行当前机制产生多个候选方案，并通过驾驭器控制评估器防止奖励黑客攻击；c) **评估器隔离模块**：通过固定工作区布局组织候选方案、日志、轨迹等，隔离评估器与进化智能体。

3. **关键技术**：统一接口支持过程型进化（编辑明确的进化过程代码，如选择策略、优化算子）和智能体型进化（编辑智能体的操作上下文，如目标、技能、记忆文件）。该设计使元智能体可通过一次编辑控制未来多个迭代的进化方向，经验证在智能体和推理基准上相对最强基线提升26%，并在三个开放优化任务中达到最先进水平。

### Q4: 论文做了哪些实验？

论文在两类实验上评估了AEvo方法。首先，在标准基准测试Terminal-Bench和ARC-AGI-2上，与单智能体推理（ReAct）及五种基于过程的进化基线（ADAS、DGM、AFlow、SPO、GEPA）对比，执行模型为Gemini-3-Flash，报告Avg@3分数和达到最佳分数的轮次。结果显示，AEvo在Terminal-Bench上达到53.8分（最佳基线44.3分），在ARC-AGI-2上达到47.0分（最佳基线36.0分），平均相对提升26%。

其次，在三个开放优化任务（circle_packing_26、autocorrelation_second、Kernel优化）上，对比了基于智能体的进化（Codex、Claude Code）和基于过程的进化（OpenEvolve、HyperAgents），报告Best@3分数、最佳轮次和每轮成本。AEvo在所有三个任务上取得最佳或并列最佳分数，例如在Kernel优化任务上达到1138个周期，且每轮成本较低（如0.32-0.34美元）。实验还分析了进化轨迹，显示AEvo能在平台期后修订机制，有效利用进化预算，并且消融实验证明元智能体技能和进化框架对长期搜索至关重要。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来方向主要体现在三方面。首先，当前AEvo的meta-editing机制依赖于单一meta-agent，其编辑策略的效率和鲁棒性尚未充分验证，尤其在更复杂的进化场景中可能面临成本高昂或策略退化问题。未来可探索轻量级干预策略，例如通过结构化模板或强化学习模型降低meta-agent的推理开销。其次，论文的实验基准主要集中在agent和推理任务，对科学发现、软件工程等长尾开放域任务的适用性有待验证，可引入动态进化环境（如代码库版本迭代）测试其适应性。此外，当前框架将评估和候选记录作为外部保护，但未深入讨论失败案例的恢复机制或恶意候选过滤。可借鉴对抗性鲁棒训练思想，设计内置安全约束的进化策略，避免长期搜索中的有害漂移。最后，meta-agent自身迭代的稳定性值得关注，例如如何通过因果推理或元学习减少编辑噪声对进化过程的干扰。

### Q6: 总结一下论文的主要内容

Agentic evolution通过迭代生成、评估和反馈来改进程序、工作流和科学解决方案，但现有方法要么是固定手工流程（刚性），要么是通用智能体（易漂移），且都缺乏组织累积证据并修订进化机制的稳定接口。本文将此问题定义为交互式环境，将累积进化上下文作为过程级状态，并提出了AEvo框架。核心方法是引入一个元智能体，它不直接生成下一个候选方案，而是通过编辑控制未来进化的流程或智能体上下文来引导搜索，从而将累积证据用于长周期搜索。主要结论表明，在智能体和推理基准上，AEvo相较于五种基线实现了26%的相对提升；在三个开放优化任务中也达到了最优性能。其意义在于为长周期进化提供了机制层面的干预，推广了智能体进化的统一范式。
