---
title: "FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments"
authors:
  - "Amir Saeidi"
  - "Venkatesh Mishra"
  - "Souradeep Mukhopadhyay"
  - "Gaowen Liu"
  - "Ali Payani"
  - "Jayanth Srinivasa"
  - "Chitta Baral"
date: "2026-04-28"
arxiv_id: "2604.25135"
arxiv_url: "https://arxiv.org/abs/2604.25135"
pdf_url: "https://arxiv.org/pdf/2604.25135v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Multi-Agent"
  - "Error Analysis"
  - "Open-Source LLMs"
  - "Interactive Environments"
relevance_score: 8.5
---

# FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments

## 原始摘要

Large Language Models are being increasingly deployed as the decision-making core of autonomous agents capable of effecting change in external environments. Yet, in conversational benchmarks, which simulate real-world customer-centric issue resolution scenarios, these agents frequently fail due to the cascading effects of incorrect decision-making. These challenges are particularly pronounced for open-source LLMs with smaller parameter sizes, limited context windows, and constrained inference budgets, which contribute to increased error accumulation in agentic settings. To tackle these challenges, we present the Failure-Aware Meta-Agentic (FAMA) framework. FAMA operates in two stages: first, it analyzes failure trajectories from baseline agents to identify the most prevalent errors; second, it employs an orchestration mechanism that activates a minimal subset of specialized agents tailored to address these failures by injecting a targeted context for the tool-use agent before the decision-making step. Experiments across open-source LLMs demonstrate performance gains up to 27% across evaluation modes over standard baselines. These results highlight that targeted curation of context through specialized agents to address common failures is a valuable design principle for building reliable, multi-turn tool-use LLM agents that simulate real-world conversational scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开源大语言模型（LLMs）在交互式工具使用环境中作为智能体时，因决策错误累积而导致的性能不佳问题。研究背景是，大语言模型越来越多地被部署为自主智能体的决策核心，用于模拟真实世界客户服务场景的多轮对话任务。现有方法，如任务特定的监督微调或强化学习，虽然取得了一定进展，但存在显著不足：对于轨迹长、部分可观测且高度可变的多轮工具使用任务，收集高质量监督数据或奖励对齐经验成本高昂；强化学习方法也因需要大规模整理轨迹和复杂工具交互而计算开销巨大。此外，这些方法通常优化正确的行为模式，很少针对特定智能体的具体失败模式，因此难以有效解决系统性错误。本文要解决的核心问题是：如何在不进行昂贵再训练的情况下，通过一种训练无关的技术，显式地识别并缓解开源LLM智能体（特别是参数量较小、上下文窗口有限、推理预算受限的模型）在多轮交互中的常见失败模式，从而稳定提升其任务完成性能。为此，作者提出了失败感知元智能体（FAMA）框架，通过分析失败轨迹并动态注入针对性上下文来缓解错误。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可按以下类别组织：

1. **评测类**：LLM-based Tool-Use Benchmarks。早期基准主要评估单轮工具调用，近期工作转向多轮交互式工具使用基准，这些基准暴露了智能体在部分可观测环境中的长程推理挑战。本文在这些基准上评估，但特别聚焦于小型开源LLM在错误累积问题上的表现。

2. **方法类（无训练技术）**：包括结构化提示和模块化智能体编排等，旨在不更新模型参数的情况下改进语言智能体。但这些方法主要在强大或专有LLM骨干上评估，对小型开源模型探索不足。FAMA专门针对小型开源LLM智能体的失败模式进行智能体设计。

3. **方法类（失败感知编排）**：近期工作开始系统分析多智能体系统中的失败原因，提出分类法和标注数据集，或自动化失败追踪。虽然存在反思性和经验性反馈技术，但未像FAMA那样利用观察到的失败模式动态组合特定模型的模块化智能体支架。FAMA通过两阶段流程（先分析失败轨迹，再编排最小专业智能体子集注入目标上下文）解决了这一空白。

### Q3: 论文如何解决这个问题？

FAMA框架通过两阶段流程解决开源LLM在交互式工具使用环境中的失败问题。第一阶段是失败模式分析，首先在任务集上执行基线代理并收集所有零分任务的完整交互轨迹作为失败案例。然后针对四种预定义错误类别（领域策略违规、复杂工具输出检索不当、上下文误解与幻觉、未完成执行或过早停止），分别部署独立错误分析代理，这些代理基于经验分析的失败原因列表对轨迹进行检测，输出分类决策和文本理由。所有分析结果与完整交互轨迹拼接后输入编排器代理，由它进行最终失败归因，特别考虑了代理从错误中恢复的情况以确保归因准确性。第二阶段是目标架构设计，基于编排器识别的错误类别和预定义代理的促进函数，专用缓解代理为每个错误类别推荐能有效缓解该错误的最小子集，最后聚合所有任务上的推荐结果，得到每个任务所需的最小代理配置。核心架构包含基础代理集（领域约束提取器、工具建议器、工具输出重构器、规划器、决策验证器、用户上下文管理器）和独立错误分析代理。创新点在于：1）元代理框架能自适应识别不同模型的失败模式；2）通过目标化最小代理子集来缓解特定失败，避免完全代理集导致的上下文窗口溢出；3）在有限资源下实现高达27%的性能提升。

### Q4: 论文做了哪些实验？

论文在交互式工具使用环境中，基于Qwen3-4B/14B/32B-Instruct及Qwen2.5-72B-Instruct等开源LLM，在τ-bench（航空与零售）、τ-trait（远程医疗与电信）和ACEBench（单智能体设置）三个基准上评估FAMA框架。对比方法包括函数调用（FC）、ReAct和输入重构多智能体框架（IRMA）。主要实验分两阶段：首先以GPT-4o为基线，比较LLaMA-3.1-70B等模型作为用户模拟器的能力，选出Qwen2.5-72B作为最优用户智能体。随后固定该用户智能体，对工具调用智能体进行测试。结果显示FAMA在τ-bench航空域平均Pass@1超越ReAct 4.63%、FC 11.57%、IRMA 5.27%；在零售域分别提升5.30%、8.96%、6.15%。例如Qwen3-4B上，FAMA在航空域Pass@1达37.60%（对比ReAct的32.00%），Qwen2.5-72B零售域Pass@1为44.17%（对比ReAct 43.47%）。消融实验发现内存大小依赖领域（零售k=6最优，航空k=2最优），且FAMA通过仅激活缓解特定失败的专用智能体，将标记开销控制在约30%（IRMA达50-58%），并有效减少上下文窗口溢出导致的错误。错误分析显示领域约束违反和上下文误解是主要失败模式。

### Q5: 有什么可以进一步探索的点？

首先，FAMA框架的局限性在于其依赖预定义的专家代理池，这导致无法自动发现和应对新的失败模式。未来可以探索自动化故障模式挖掘与代理生成机制，例如利用在线学习或强化学习动态识别新兴错误类型，并自动合成对应的专家代理，从而提升框架的泛化能力。其次，当前评估仅聚焦结构化对话环境，未覆盖具身、多模态或开放式场景。这些场景的失败类型更复杂且边界模糊，可研究如何将失败感知策略迁移至视觉-语言代理或机器人控制任务中。此外，框架对上下文注入的依赖可能引入冗余或噪声，可尝试优化上下文选择的稀疏性，例如通过注意力机制或信息论指标动态筛选关键失败相关历史。最后，当前框架设计了“先分析后执行”的两阶段流程，未来可探索端到端的联合训练，让失败识别与策略触发协同优化。总体而言，将失败感知机制与自动代理发现、跨模态适应及在线学习结合，是提升开放环境代理鲁棒性的重要方向。

### Q6: 总结一下论文的主要内容

大语言模型在作为自主代理核心时，尤其是在交互式工具使用环境中，常因级联错误而失败，开源小模型问题尤甚。为此，论文提出故障感知元代理框架，旨在通过动态多代理协作提升性能。该框架分两个阶段：首先分析基线代理的失败轨迹，识别最常见的错误模式；其次通过编排机制，激活最小规模的专门代理子集，在决策前向工具使用代理注入针对性上下文以修正这些错误。在多个交互式工具调用基准和开源模型上的实验表明，该框架在各评估模式下实现了高达27%的性能提升。核心贡献在于提出了一个通过专门代理针对性策划上下文以应对常见故障的通用设计原则，为构建资源高效且可靠的多轮对话代理提供了新思路。
