---
title: "Agentic Code Reasoning"
authors:
  - "Shubham Ugare"
  - "Satish Chandra"
date: "2026-03-02"
arxiv_id: "2603.01896"
arxiv_url: "https://arxiv.org/abs/2603.01896"
pdf_url: "https://arxiv.org/pdf/2603.01896v2"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.PL"
tags:
  - "Code & Software Engineering"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "semi-formal reasoning"
  primary_benchmark: "RubberDuckBench, Defects4J"
---

# Agentic Code Reasoning

## 原始摘要

Can LLM agents explore codebases and reason about code semantics without executing the code? We study this capability, which we call agentic code reasoning, and introduce semi-formal reasoning: a structured prompting methodology that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Unlike unstructured chain-of-thought, semi-formal reasoning acts as a certificate: the agent cannot skip cases or make unsupported claims. We evaluate across three tasks (patch equivalence verification, fault localization, and code question answering) and show that semi-formal reasoning consistently improves accuracy on all of them. For patch equivalence, accuracy improves from 78% to 88% on curated examples and reaches 93% on real-world agent-generated patches, approaching the reliability needed for execution-free RL reward signals. For code question answering on RubberDuckBench Mohammad et al. (2026), semi-formal reasoning achieves 87% accuracy. For fault localization on Defects4J Just et al. (2014), semi-formal reasoning improves Top-5 accuracy by 5 percentage points over standard reasoning. These results demonstrate that structured agentic reasoning enables meaningful semantic code analysis without execution, opening practical applications in RL training pipelines, code review, and static program analysis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在不执行代码的情况下，对代码库进行深入语义分析和推理的能力问题，即“智能体代码推理”。研究背景是，在复杂的软件仓库中，进行代码审查、补丁验证和缺陷定位等任务时，需要跨多个文件理解代码语义，但执行代码（如运行测试）可能成本高昂或存在安全风险。因此，开发无需执行的可靠代码推理能力具有重要应用价值。

现有方法存在明显不足。一方面，近期一些工作（如SWE-RM、Agentic Rubrics、CodeJudge）探索了免执行的代码验证，但它们依赖于非结构化的推理（如思维链），允许模型在没有明确证据支持的情况下对代码行为做出断言，导致推理可能不完整或存在猜测。另一方面，形式化验证方法（如使用Lean、Coq）虽然能通过自动证明检查确保严谨性，但需要将代码或推理完全形式化，这对于涉及多种语言和框架的任意仓库代码来说不切实际，且通常针对特定任务，缺乏通用性。

因此，本文要解决的核心问题是：如何设计一种通用、实用的方法，使LLM智能体能够在无需执行代码的情况下，进行深入、可靠且可验证的代码语义推理，弥合非结构化推理与完全形式化验证之间的鸿沟。为此，论文提出了“半形式化推理”这一结构化提示方法。它要求智能体遵循特定模板，明确陈述前提、追踪执行路径并得出形式化结论，从而充当一种“证明证书”，确保推理的完整性和可验证性，避免跳过关键情况或做出无根据的断言。该方法旨在不依赖专门模型训练或完全形式化语义的情况下，提升智能体在补丁等价性验证、故障定位和代码问答等多种任务上的推理准确性和可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM驱动的软件工程智能体**：如SWE-agent通过专用命令接口实现与代码库的交互，OpenHands提供开发平台，Agentless将缺陷修复分解为定位与修复阶段。这些系统依赖测试执行进行验证，而本文旨在通过语义代码推理减少对执行的依赖。

**2. 免执行的代码验证方法**：SWE-RM训练奖励模型提供免执行反馈，Agentic Rubrics使用LLM生成可解释的验证准则，CodeJudge探索LLM作为代码质量评估者。本文的**半形式化推理**方法通过结构化提示（要求构建明确前提、追踪执行路径、推导形式结论）提升验证准确率，在真实补丁上达到93%的准确率，与这些工作形成对比。

**3. 基于LLM的缺陷定位与代码理解**：AgentFL和FlexFL专注于项目级缺陷定位，CodePlan结合LLM与规划进行仓库级代码编辑，RubberDuckBench提供代码理解任务基准。本文的工作扩展了智能体推理在代码分析任务中的适用性，涵盖补丁验证、缺陷定位和代码问答。

**4. 程序等价性与形式验证**：传统方法依赖形式化方法（如转换验证），近期研究探索LLM用于形式验证（如EquiBench基准、Sultan等关于程序终止性的工作）。另有研究通过静态分析对LLM推理进行事后验证。本文聚焦于“输入侧”，通过结构化推理提升智能体分析过程的严谨性，而非事后验证输出。

**5. LLM推理与思维链**：本文方法建立在思维链提示、ReAct（推理与行动结合）、CodeAct（可执行代码动作）等研究基础上，针对代码推理设计特定结构化模板，将语义验证准确率提升最高11个百分点。

**6. 软件工程智能体的训练与扩展**：如SWE-Gym、R2E-Gym提供训练环境与混合验证器，SWE-RL通过强化学习提升推理能力。本文的免执行验证方法可补充这些工作，降低强化学习训练的计算成本。

### Q3: 论文如何解决这个问题？

论文通过引入一种称为“半形式化推理”的结构化提示方法来解决LLM代理在不执行代码的情况下探索代码库并进行语义推理的问题。该方法的核心是强制代理在推理过程中构建明确的逻辑结构，从而避免非结构化思维链中常见的跳跃性结论和未经证实的断言。

整体框架基于任务特定的提示模板，这些模板规定了代理必须遵循的推理格式。主要模块包括：定义模块（明确任务相关的形式化定义）、前提模块（要求代理陈述每个代码变更或可疑区域的具体内容）、分析模块（针对每个测试用例或代码路径，要求代理追踪执行路径并给出基于证据的断言），以及形式化结论模块（基于前述分析推导出结论）。例如，在补丁等价性验证任务中，模板强制代理列出每个补丁修改的文件和变更内容，然后为测试套件中的每个测试分析其在两个补丁下的执行路径和预期结果（通过/失败），并进行比较，最后根据测试结果的一致性给出形式化结论。

关键技术在于将自然语言直觉与结构化逻辑步骤相结合。与完全非结构化的标准推理（仅用自然语言解释并输出结论）不同，半形式化推理通过模板强制代理在执行分析前收集证据，例如必须枚举程序路径、追踪函数调用以证明其声称的行为。这种结构化的推理过程充当了一种“证明证书”，使得代理无法跳过案例或做出无支持的论断。创新点体现在：1）将半形式化方法从数学推理领域成功适配到代码语义推理任务；2）通过设计可泛化的模板结构（针对不同任务调整具体内容但保持核心原则），统一提升了多种代码推理任务（补丁等价性验证、故障定位、代码问答）的准确性和可靠性；3）该方法实现了无需实际执行代码的深度语义分析，为强化学习训练管道、代码审查和静态程序分析等实际应用提供了可行基础。

### Q4: 论文做了哪些实验？

论文在三个核心任务上进行了实验：补丁等价性验证、代码问答和故障定位。实验设置上，主要对比了标准推理（Standard）与半形式推理（Semi-formal）两种方法，并评估了单次调用（Single-shot）与智能体探索（Agentic）两种模式。使用的模型包括Opus-4.5和Sonnet-4.5。

在**补丁等价性验证**任务中，构建了一个包含170个挑战性示例的精选数据集，源自从SWE-bench-Verified采样的不同智能体生成的补丁对。主要对比方法包括：基于difflib的文本相似度（最佳阈值0.4）、单次LLM调用、带文件上下文的单次调用以及智能体探索。使用Opus-4.5模型，半形式推理将整体准确率从标准推理的78.2%提升至88.8%。在另一个包含200个真实世界智能体生成补丁的平衡数据集上，当提供测试补丁时，Opus-4.5结合半形式推理达到了93.0%的最高准确率。

在**故障定位**任务中，使用Defects4J基准测试。评估了两种匹配指标：“All”（要求预测覆盖所有真实错误代码块）和“Any”（至少覆盖一个）。在小规模评估（50个错误）中，Opus-4.5模型在智能体探索模式下，半形式推理将Top-5准确率（All指标）从标准推理的60.5%提升至72.1%。在大规模验证（100个错误）中，半形式推理将Top-5准确率（All指标）从标准推理的43.3%提升至47.8%（Opus-4.5），提升了约5个百分点。

在**代码问答**任务中，使用RubberDuckBench数据集。Opus-4.5模型在智能体探索模式下，半形式推理将准确率从标准推理的78.3%显著提升至87.0%。Sonnet-4.5模型在该任务上提升不明显，标准推理已达84.2%，半形式推理为84.8%。关键数据指标包括：补丁验证最高准确率93.0%，故障定位Top-5（Any）最高准确率88.4%，代码问答最高准确率87.0%。半形式推理普遍需要更多推理步骤（约2-3倍），但显著提升了准确性和可靠性。

### Q5: 有什么可以进一步探索的点？

本文提出的半形式化推理方法虽在多项任务中提升了准确性，但仍存在局限性。首先，该方法依赖精心设计的提示模板，其构建成本较高，且可能无法覆盖所有代码逻辑的细微差别。其次，作为基于LLM的方法，它缺乏传统静态分析工具的形式化保证，推理过程可能隐含模型本身的幻觉或偏见。此外，当前评估集中于特定基准，在更复杂、规模更大的真实代码库上的泛化能力有待验证。

未来研究方向可从以下几个维度展开：一是模型层面，通过针对代码推理的后续训练（Post-training），使模型内化半形式化推理结构，从而减少提示工程开销并进一步提升准确率。二是任务扩展，将此类结构化推理范式应用于漏洞检测、代码异味识别、API误用检测等其他静态分析任务，验证其通用性。三是构建混合验证系统，探索将LLM的灵活推理与轻量级形式化方法或符号执行相结合，在保持灵活性的同时提供更强的正确性保证。此外，还可研究如何将推理过程模块化或可解释化，以增强结果的可信度与可调试性。

### Q6: 总结一下论文的主要内容

该论文研究了LLM智能体在不执行代码的情况下探索代码库并推理代码语义的能力，即“智能体代码推理”。针对此问题，作者提出了“半形式化推理”方法，这是一种结构化的提示方法，要求智能体构建明确的前提、追踪执行路径并推导形式化结论。与无结构的思维链不同，该方法作为一种“证明”，强制智能体不能跳过情况或做出无依据的断言。

论文在三个任务上评估了该方法：补丁等价性验证、缺陷定位和代码问答。实验结果表明，半形式化推理在所有任务上都持续提升了准确性。具体而言，在补丁等价性验证任务中，准确率从78%提升至88%（在精选示例上），在真实智能体生成的补丁上达到93%，接近无需执行的强化学习奖励信号所需的可靠性。在RubberDuckBench的代码问答任务上达到87%准确率。在Defects4J的缺陷定位任务上，Top-5准确率比标准推理提升了5个百分点。

核心贡献在于证明了结构化的智能体推理能够实现无需执行代码的有意义的语义分析，为强化学习训练流程、代码审查和静态程序分析等实际应用开辟了道路。
