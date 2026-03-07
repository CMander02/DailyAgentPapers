---
title: "Agentified Assessment of Logical Reasoning Agents"
authors:
  - "Zhiyu Ni"
  - "Yifeng Xiao"
  - "Zheng Liang"
date: "2026-03-03"
arxiv_id: "2603.02788"
arxiv_url: "https://arxiv.org/abs/2603.02788"
pdf_url: "https://arxiv.org/pdf/2603.02788v1"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "agentified assessment framework"
  primary_benchmark: "FOLIO (solver-verified and repaired split)"
---

# Agentified Assessment of Logical Reasoning Agents

## 原始摘要

We present a framework for evaluating and benchmarking logical reasoning agents when assessment itself must be reproducible, auditable, and robust to execution failures. Building on agentified assessment, we use an assessor agent to issue tasks, enforce execution budgets, parse outputs, and record structured failure types, while the agent under test only needs to expose a standardized agent-to-agent interface. As a case study, we benchmark an auto-formalization agent for first-order logic (FOL) reasoning on a solver-verified and repaired split of FOLIO. The agent translates natural language premises and conclusions into executable Z3Py programs and employs satisfiability modulo theories (SMT) solving to determine logical entailment. On the cleaned FOLIO validation set, the auto-formalization agent achieves 86.70% accuracy under the assessor protocol, outperforming a chain-of-thought baseline (73.89%).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决逻辑推理智能体评估中存在的可复现性、可审计性和鲁棒性不足的问题。研究背景在于，随着基于大语言模型的智能体在复杂推理任务（如一阶逻辑推理）中的应用日益增多，如何准确、可靠地评估其性能成为关键挑战。现有评估方法通常采用静态测试框架，存在明显缺陷：它们将工具执行失败（如超时、运行时错误）与模型本身的推理错误混为一谈，导致单一的准确率指标掩盖了具体的失败模式；同时，评估逻辑与智能体实现紧密耦合，使得集成新基准测试的成本高昂，缺乏标准化。

针对这些不足，本文的核心问题是设计一个能够实现可复现、可审计且对执行失败鲁棒的评估框架。为此，论文提出了“智能体化评估”框架，其核心思想是将评估逻辑本身实现为一个“评估者智能体”。该评估者通过标准化的智能体间接口与被测智能体交互，负责发布任务、执行预算控制、解析输出并记录结构化的失败类型，从而清晰区分操作失败与推理错误。论文以一阶逻辑推理任务为案例，在清洗和验证后的FOLIO数据集上，对一个将自然语言转化为Z3Py代码并进行求解的自动形式化智能体进行了基准测试，验证了该框架的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测框架类、逻辑推理基准类以及自动形式化方法类。

在评测框架方面，相关工作包括传统的静态评测工具（如静态评估工具链），这些工具通常将操作失败与推理错误混为一谈，且评测逻辑与智能体实现紧耦合。本文借鉴了AgentBeats提出的“智能体化评测”（agentified assessment）思想，通过独立的评估者智能体与被测智能体交互，实现了可复现、可审计且对执行失败鲁棒的评测，从而解决了传统方法的问题。

在逻辑推理基准方面，本文以FOLIO数据集作为一阶逻辑推理的基准。与直接使用原始数据不同，本文通过数据清洗流程对FOLIO进行了验证和修复，建立了一个更可靠的基准版本，减少了数据质量问题对评估的干扰。

在自动形式化方法上，相关研究包括使用思维链（chain-of-thought）等提示工程方法进行逻辑推理。本文提出的方法则是一个白盒的自动形式化智能体，它将自然语言前提和结论转化为可执行的Z3Py程序，并利用SMT求解器进行逻辑蕴涵判定。这种方法在清洗后的FOLIO验证集上取得了比思维链基线更高的准确率，体现了其优势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Agentified Assessment”（可译为“智能体化评估”）的框架来解决逻辑推理智能体的评估问题。其核心思想是将评估过程本身也建模为一个智能体，从而将评估逻辑与被测智能体解耦，实现可复现、可审计且对执行失败鲁棒的评估。

**整体框架与架构设计：**
框架包含两个核心交互组件：**被测智能体** 和 **评估者智能体**。两者通过一个标准化的**智能体到智能体接口**进行通信。这种设计改变了传统评估中评估脚本与特定基准测试紧密耦合的模式。在传统模式下，集成成本随基准测试数量线性增长；而在本框架下，智能体只需实现一次A2A接口，即可参与众多评估者的评估，集成成本为常数级，实现了“即插即用”的评估和架构自由。

**主要模块与关键技术：**
1.  **评估者智能体**：这是框架的核心创新模块。它负责执行完整的评估协议，具体功能包括：
    *   **任务发布**：向被测智能体发送推理任务。
    *   **预算控制**：强制执行超时、重试等执行预算。
    *   **输出解析与验证**：解析被测智能体的响应，并依据基准标准确定最终标签（True/False/Uncertain）。对于无法解析的输出，会记录为ParseError。
    *   **结构化失败记录**：不简单地丢弃失败案例，而是系统记录超时、运行时错误、解析错误等结构化失败类型。
    *   **生成评估报告**：输出包含每个实例记录（黄金标签、预测标签、正确性、错误类型、延迟）和聚合指标的可机读评估结果。

2.  **被测智能体**：论文以两个智能体作为案例研究：
    *   **思维链基线智能体**：采用提示工程，指导模型进行逐步推理，并在最后一行输出单一标签，由评估者解析。
    *   **自动形式化智能体（核心创新点）**：该智能体采用两阶段流水线解决一阶逻辑推理问题：
        *   **阶段一（代码生成）**：使用语言模型将自然语言前提和结论翻译成可执行的Z3Py代码。
        *   **阶段二（执行与验证）**：在沙箱环境中执行生成的程序（设60秒超时）。通过可满足性模理论求解进行逻辑有效性判定：根据特定公式的可满足性结果来分配True/False/Uncertain标签。
        *   **自修复循环**：为提高鲁棒性，该智能体集成了一个关键的自修复机制。当执行因语法错误或量词格式错误而失败时，智能体会提取错误信息并进行针对性的代码修复，最多可尝试三次，这显著提升了系统的健壮性和成功率。

**总结创新点：**
论文的主要创新在于提出了一个**将评估过程智能体化的通用框架**，通过标准接口解耦评估与执行，大幅降低了评估集成成本。在具体案例中，创新性地设计了**基于自动形式化与SMT求解的两阶段推理管道**，并辅以**执行失败后的自修复循环**，从而在清理后的FOLIO验证集上取得了优于思维链基线的准确率（86.70% vs 73.89%）。整个系统构建在AgentBeats平台上，并支持构建可复现比较的排行榜。

### Q4: 论文做了哪些实验？

实验在清理后的FOLIO验证集上进行，该数据集包含203个经过标签验证的样本。实验设置上，对比了思维链基线智能体和自动形式化智能体，两者均以Gemini 2.5 Flash作为骨干大语言模型，温度设为0.0以确保输出确定性，最大输出标记数默认为65535。两种智能体均采用系统-用户提示结构：思维链基线的系统提示要求逐步推理并将最终答案标签置于最后一行；自动形式化智能体的提示则包含Z3代码生成指令和语法指南。实验未为任何智能体提供上下文学习示例。

主要结果方面，思维链基线在整体数据集上的准确率为73.89%（150/203），而自动形式化智能体将准确率提升至86.70%（176/203）。关键数据指标显示，在“假”类别中，准确率从44.26%显著提升至77.05%；在“真”类别上两者表现相近（基线89.04% vs. 自动形式化90.41%）；在“不确定”类别中，准确率从84.06%提升至91.30%。这些结果证明了基于求解器的形式化验证在提升逻辑推理鲁棒性方面的优势。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于评估框架目前主要针对一阶逻辑的自动形式化任务，未来可扩展至更复杂的逻辑系统（如高阶逻辑、模态逻辑）和多样化推理场景（如常识推理、数学证明）。评估代理的策略较为基础，未来可探索动态预算分配、多轮交互评估等更灵活的机制。

结合个人见解，可能的改进方向包括：1）引入对抗性评估，设计专门测试逻辑边界情况的挑战性问题集；2）将评估框架与强化学习结合，使代理能在评估反馈中持续优化；3）开发跨模态逻辑推理评估，如图文结合的逻辑问题；4）探索分布式评估体系，允许多个评估代理协作完成复杂任务评估。这些方向能进一步提升评估的严谨性和代理的泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为“Agentified Assessment”的评估框架，旨在对逻辑推理智能体进行可复现、可审计且对执行失败鲁棒的基准测试。其核心问题是解决传统评估方法在自动化、标准化和容错性方面的不足。

方法上，框架引入了一个独立的“评估者智能体”，它负责发布任务、管理执行资源、解析被测试智能体的输出，并系统化地记录各类结构化失败类型。被评估的智能体只需暴露一个标准化的智能体间接口即可。论文以一阶逻辑自动形式化智能体为案例，在修复后的FOLIO数据集上进行了验证。该智能体将自然语言前提和结论翻译成可执行的Z3Py代码，并利用可满足性模理论求解器来判断逻辑蕴涵关系。

主要结论是，在清理后的FOLIO验证集上，该自动形式化智能体在评估者协议下达到了86.70%的准确率，显著优于思维链基线模型的73.89%。这项工作的核心贡献在于提供了一个通用、严谨的智能体评估范式，其意义在于推动了AI智能体评估向更自动化、标准化和可靠的方向发展，为未来复杂推理系统的性能衡量奠定了基础。
