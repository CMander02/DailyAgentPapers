---
title: "ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?"
authors:
  - "Jiajun Li"
  - "Mingshu Cai"
  - "Yixuan Li"
  - "Yu Ding"
  - "Ran Hou"
  - "Guanyu Nie"
  - "Xiongwei Han"
  - "Wanyuan Wang"
date: "2026-06-18"
arxiv_id: "2606.19787"
arxiv_url: "https://arxiv.org/abs/2606.19787"
pdf_url: "https://arxiv.org/pdf/2606.19787v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Operations Research"
  - "Benchmark"
  - "End-to-End Evaluation"
  - "Code Generation"
  - "Task Planning"
  - "Feasibility Constraints"
  - "Autonomous Problem Solving"
relevance_score: 9.0
---

# ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?

## 原始摘要

Large language models are increasingly deployed as autonomous agents for multi-step tasks in executable environments, yet their ability to perform realistic operations research (OR) work remains unclear. Existing OR evaluations often decouple modeling from solving, rely on pre-formalized or text-only instances, and rarely test the full workflow from operational artifacts to validated decisions. In this work, we introduce ORAgentBench, an execution-grounded benchmark for evaluating autonomous agents on challenging end-to-end operations research tasks. It contains 107 human-reviewed tasks across diverse operational scenarios, each packaged in an isolated environment with a natural-language brief, multi-file data, configuration artifacts, and a required submission schema. Agents must write and run solution code, and their submissions are evaluated by hidden validators for schema validity, hard-constraint feasibility, and normalized objective quality. Experiments with fourteen frontier agent-model configurations show that current agents remain far from reliable OR practice. The best agent passes only 35.51% of all tasks and 20.59% of hard tasks, and many feasible submissions still fall below the required quality threshold. Failure analysis further shows that errors are dominated by strategic weaknesses, including missed operational rules, brittle formulations, weak feasible-solution construction, and insufficient solution improvement. OR-specific procedural skills increase hard-task feasibility, but do not reliably improve solution quality or pass rate. These results suggest that progress in OR agents requires moving beyond plausible optimization code toward dependable, high-quality operational decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型（LLM）代理在真实运筹学（OR）任务中缺乏可靠端到端执行能力的核心问题。研究背景是，运筹学广泛应用于货运、排班、生产计划等高价值决策场景，其实际工作流程涉及从模糊的操作需求出发，进行数据协调、模型设计、编码、验证和修订的完整工程链条，通常需要多领域专家协作且成本高昂。然而，现有评估方法存在明显不足：一方面，聚焦求解器的基准测试（如MIPLIB、CVRPLIB）仅评估预先形式化后的优化实例，忽略了从操作文档到数学模型的建模过程；另一方面，面向建模的基准（如NL4Opt）虽测试问题生成能力，但未检查代理在运行时环境下执行代码、修复错误并生成可验证决策工件的完整能力。这些评估人为地将建模与求解分离，无法反映真实OR工作对二者联合设计的要求。因此，本文提出ORAgentBench，通过包含107个经人工审核的端到端任务、多文件输入、隔离执行环境及隐藏验证器（检查模式合规性、硬约束可行性与目标质量），首次系统评估LLM代理完成真实OR工作流的全流程能力，揭示当前最佳代理仅通过35.51%任务、硬任务通过率低至20.59%的严峻现状。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

1. **优化建模与求解类**：早期工作如NL4Opt、Mamo评估自然语言到数学建模的能力，IndustryOR、OptiBench、OptMATH、MIPLIB-NL等则扩展至实际OR场景和求解器辅助的端到端求解。这些工作关注生成合理的公式或求解代码，但不评估代理能否选择有效的抽象和建模策略。ORAgentBench在此基础上进一步要求代理在真实工作流中通过可执行方案和验证的决策质量来评估建模选择。

2. **组合优化推理类**：CO-Bench研究智能体算法搜索，NLCO关注对组合优化问题的直接自然语言推理。它们覆盖了CO推理能力，但缺乏从操作工件到验证决策的完整流程。

3. **通用智能体基准类**：如SWE-bench、WebArena等评估软件工程、机器学习工程、网页交互等领域的执行型任务，但输出通常是补丁或操作，而非受可行性和目标质量约束的运营决策。ORAgentBench填补了这一空白，将多文件执行环境与OR风格的约束验证和目标优化相结合。

与这些工作相比，ORAgentBench的独特性在于：它要求智能体从自然语言描述和多文件操作工件出发，编写并运行代码生成方案，再通过隐藏验证器评估方案的有效性、约束可行性和目标质量，从而测试完整的端到端OR工作流能力。

### Q3: 论文如何解决这个问题？

论文通过构建ORAgentBench基准来系统评估LLM智能体解决运筹学任务的能力。核心方法包括四部分:任务形式化定义、渐进式验证机制、严格的任务构建流水线和多维度诊断分析。

整体框架将运筹任务定义为七元组(τ=(D,C,q,E,V)),包含多文件数据、自然语言简报、隔离执行环境和隐藏验证器。智能体需自主生成可执行代码,在沙箱环境中运行后由验证器评估。验证采用三个递进维度:输出模式有效性、硬约束可行性和目标质量,只有通过可行性门槛且质量分超过0.4才算通过任务。

关键技术方面,构建流水线包含四阶段:场景选择(从论文和真实场景筛选)、任务数据丰富(人工注入操作规则和耦合约束)、智能体辅助验证(循环诊断修复)、人工审查(检查合法性、抗作弊等)。任务难度通过六个构建维度控制:求解策略、公式结构、约束耦合、动态结构、数据规模和问题理解。

创新点在于:1) 提出端到端运筹任务定义,区别于仅测试翻译能力的传统基准;2) 设计隐藏验证器实现自动可复现评估;3) 引入建模策略和求解策略的双隐变量框架,揭示智能体需要同时完成问题表示和计算过程设计;4) 包含107个经人工审查的多样运筹场景,任务数据保留真实业务依赖和操作语义。实验发现最佳智能体仅通过35.51%任务,且错误主要来自建模策略缺陷。

### Q4: 论文做了哪些实验？

论文进行了四个方面的实验。首先，在ORAgentBench的107个任务上评估了14个前沿模型-代理配置（包括MiniMax、Kimi、Qwen、DeepSeek、GLM、Claude和OpenAI系列模型），使用Harbor隔离环境，设置45分钟交互预算和5分钟求解限制。结果显示最佳代理（GPT-5.4）仅通过35.51%的任务（硬任务20.59%），且可行性始终高于通过率，表明存在显著的质量差距。其次，分析了效率权衡，发现通过率与运行时间或API成本不呈单调关系，最佳代理既非最慢也非最贵。第三，失败模式诊断表明54.8%的失败源于建模策略错误（如遗漏操作规则、脆弱公式化），而非求解器问题。最后，技能增强实验固定GPT-5.4，比较无技能、基础技能和专家技能三种设置。专家技能提升了硬任务的可行性和通过率（从17.65%到21.50%），但降低了简单任务性能（从62.50%到59.81%），说明OR特定技能有助于复杂任务但可能对简单任务造成过度负担。

### Q5: 有什么可以进一步探索的点？

基于论文的分析，进一步探索点集中在提升策略可靠性和质量上。当前模型在可行性构建和方案改进上有明显短板，未来可研究混合检索增强生成（RAG）结合约束求解器的多阶段框架，让代理先通过规则库纠正逻辑错误，再调用优化器生成可行解。针对任务难度分布不均的问题，可以开发自适应难度的提示策略，例如根据约束耦合度动态调整推理链长度。此外，论文中六维评估体系（如动态状态、数据规模）可作为元学习基准，训练代理在不同操作场景下自主选择建模范式。建议引入对抗性验证机制，通过自动生成隐藏约束来暴力测试代理的规则覆盖性，这能直接提升现实部署中的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了ORAgentBench，一个用于评估大语言模型自主智能体在端到端运筹学任务中表现的可执行基准。目前，现有评估往往将建模与求解分离，且依赖预形式化或纯文本实例，无法测试完整工作流。ORAgentBench包含107个经人工审核的任务，覆盖多种运营场景，每个任务都在隔离环境中提供自然语言说明、多文件数据、配置工件及所需提交模式。智能体必须编写并运行求解代码，其提交结果通过隐藏验证器评估模式有效性、硬约束可行性及归一化目标质量。对14个前沿智能体配置的实验表明，当前最佳智能体仅通过35.51%的任务（困难任务通过率20.59%），且许多可行提交未达质量门槛。失败分析发现，错误主要源于战略弱点，如遗漏运营规则、模型脆弱、可行解构建不足及解改进不力。该工作强调了运筹学智能体需从生成合理代码转向实现可靠、高质量的运营决策。
