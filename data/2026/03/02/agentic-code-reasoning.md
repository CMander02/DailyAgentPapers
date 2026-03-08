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
  - "Reasoning & Planning"
  - "Code & Software Engineering"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Code & Software Engineering"
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

这篇论文旨在解决大型语言模型（LLM）智能体在不执行代码的情况下，对代码库进行深入语义分析和推理的难题，即“智能体代码推理”。研究背景是，在复杂的软件仓库中，进行代码审查、补丁验证和缺陷定位等任务时，往往需要跨文件理解代码语义，而频繁执行代码（尤其是在沙箱中）成本高昂或不切实际。因此，开发一种无需执行即可可靠分析代码的能力至关重要。

现有方法存在明显不足。一方面，近期研究（如SWE-RM、Agentic Rubrics、CodeJudge）探索了免执行的验证方法，但它们依赖于非结构化的推理（如思维链），允许模型在没有明确证据支持的情况下做出关于代码行为的断言，其推理过程不透明且可能遗漏关键情况。另一方面，形式化验证方法（如使用Lean、Coq）虽然能通过自动证明检查确保严谨性，但需要将代码或推理完全形式化，这对于涉及多种语言和框架的实际代码库而言不切实际，且通常局限于特定任务，缺乏通用性。

因此，本文要解决的核心问题是：如何设计一种既保持推理严谨性、又具备实际可行性的方法，来提升LLM智能体在不执行代码的情况下进行代码语义推理的准确性和可靠性。为此，论文引入了“半形式化推理”这一结构化提示方法。它要求智能体在推理过程中必须明确陈述前提、追踪执行路径并得出形式化结论，从而构成一个可验证的“证明证书”。这种方法强制智能体进行完整推理，避免跳跃步骤或无根据的断言，同时保持了自然语言的灵活性，无需完全形式化。论文通过在补丁等价性验证、故障定位和代码问答三个任务上的评估，证明了该方法能显著提升推理准确性，为解决免执行代码分析中的可靠性挑战提供了新途径。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. LLM驱动的软件工程智能体**：如SWE-agent、OpenHands和Agentless等系统，它们通过代码库交互或分阶段任务分解实现自动化软件开发，但普遍依赖测试执行进行验证。本文则旨在通过语义代码推理减少对执行的依赖。

**2. 免执行的代码验证方法**：与本文最直接相关，包括SWE-RM（训练奖励模型提供免执行反馈）、Agentic Rubrics（使用LLM生成可解释的验证准则）和CodeJudge（以LLM作为代码质量评判者）。本文的**区别**在于强调**结构化半形式推理**，通过要求智能体构建明确前提、追踪执行路径并推导形式结论，显著提升了验证准确率（在真实补丁上达93%）。

**3. 基于LLM的故障定位与代码理解**：例如AgentFL和FlexFL专注于故障定位，CodePlan结合规划进行仓库级代码编辑，RubberDuckBench则提供代码理解任务的评测基准。本文的工作将智能体推理能力扩展至这些更广泛的代码分析任务。

**4. 程序等价性与形式验证**：传统方法依赖形式化方法，近期研究探索用LLM进行形式验证或等价性判断（如EquiBench、Sultan等人的工作）。另有研究通过静态分析对LLM推理进行事后验证。本文的**不同**在于聚焦“输入侧”，通过结构化推理提升智能体分析过程的严谨性，而非事后验证输出。半形式证书虽缺乏全形式方法的自动可检查性，但更易于人工验证。

**5. LLM推理与思维链**：本文方法建立在思维链、ReAct（推理与行动结合）、CodeAct（可执行代码动作）等结构化推理研究基础上，并**将其专门化**于代码推理领域，设计了包含前提、执行追踪和形式结论的任务特定模板，从而显著提升了语义验证准确率。

**6. 软件工程智能体的训练与扩展**：如SWE-Gym、R2E-Gym和SWE-RL等工作构建了训练环境与强化学习框架。本文的免执行验证方法可作为补充，为这类训练管道提供更高效的奖励信号，降低计算成本。

### Q3: 论文如何解决这个问题？

论文通过引入一种称为“半形式化推理”的结构化提示方法来解决LLM智能体在不执行代码的情况下探索代码库并进行语义推理的问题。该方法的核心是强制智能体在推理过程中遵循一个明确的模板，该模板要求其构建显式的前提、追踪执行路径并推导出形式化结论，从而作为一种“证明证书”，防止智能体跳过关键步骤或做出无依据的断言。

整体框架和主要模块围绕“半形式化推理”模板展开。该模板是任务特定的，但遵循统一原则：智能体必须在得出结论前记录可验证的证据。对于补丁等价性验证任务，模板包含几个关键部分：首先是“定义”，明确任务目标（如补丁在测试结果上等价的条件）；其次是“前提”，要求智能体明确陈述每个补丁修改了哪些文件及具体更改；接着是“测试行为分析”，要求针对每个测试用例，分别基于两个补丁追踪执行路径，预测测试结果（通过/失败）并提供原因（如函数调用跟踪），然后比较结果是否相同；如果发现不等价，则需提供“反例”，具体指出导致结果差异的代码追踪证据；最后是“形式化结论”，基于定义和证据得出最终判断。

创新点在于将推理过程本身结构化，而不仅仅是输出格式。与无约束的“标准推理”（仅用自然语言解释思考）相比，半形式化推理强制智能体在得出结论前系统性地收集证据，例如枚举程序路径、跟踪函数调用以验证主张。这促进了更深层次的跨过程推理，避免了常见于非结构化推理中的草率判断。例如，在补丁等价性任务中，该方法能发现因忽略对会话中间件的修改而导致测试失败的细微问题，而标准推理则会遗漏。这种结构化方法被证明能显著提升多个任务的准确性：在补丁等价性验证中，准确率从78%提升至88%（在真实智能体生成的补丁上达到93%）；在代码问答任务中达到87%的准确率；在缺陷定位任务中，Top-5准确率提升了5个百分点。因此，半形式化推理通过提供一种可验证的、证据驱动的推理框架，使LLM智能体能够在无需执行代码的情况下进行有意义的语义代码分析。

### Q4: 论文做了哪些实验？

论文在三个核心任务上进行了实验：补丁等价性验证、代码问答和缺陷定位。实验设置上，主要对比了标准推理与半形式化推理两种方法，并评估了单次调用、带文件上下文和智能体探索等不同模式。使用的模型包括Opus-4.5和Sonnet-4.5。

在补丁等价性验证任务中，构建了一个包含170个挑战性示例的精选数据集，源自从SWE-bench-Verified获取的代理生成补丁对。主要对比方法包括基于difflib的相似度阈值法、单次LLM调用、带文件上下文的单次调用以及智能体探索模式。关键结果显示，使用Opus-4.5模型时，标准推理的总体准确率为78.2%，而半形式化推理将其提升至88.8%。在包含200个示例的真实世界补丁验证中（其中100个正确，100个错误），当提供测试补丁时，Opus-4.5结合半形式化推理达到了93.0%的最高准确率，显著优于单次调用模式（86.0%-87.5%）和标准智能体模式（87.0%）。

在缺陷定位任务中，使用Defects4J基准测试。评估了单次提供所有代码（单次模式）与智能体迭代探索文件（智能体模式）两种探索方式，并采用“All”（预测需覆盖所有真实缺陷块）和“Any”（预测至少覆盖一个真实缺陷块）两种严格度不同的指标。在小规模评估（50个缺陷）中，Opus-4.5模型在智能体探索模式下，半形式化推理将Top-5准确率（All指标）从标准推理的60.5%提升至72.1%。在更大规模的100个缺陷样本验证中，Opus-4.5的半形式化推理将Top-5准确率（All指标）从标准推理的43.3%提升至47.8%，提升了约5个百分点。

在代码问答任务中，使用RubberDuckBench数据集。评估了单次模式、标准智能体推理和半形式化智能体推理。关键结果显示，对于Opus-4.5模型，半形式化推理将智能体模式的准确率从78.3%显著提升至87.0%。对于Sonnet-4.5模型，标准智能体推理已达到84.2%的较高准确率，半形式化推理（84.8%）提升不明显。所有实验均报告了平均推理步骤数，半形式化推理通常需要更多步骤（例如补丁验证中从10.08步增至28.17步），但换来了准确性的显著提升。

### Q5: 有什么可以进一步探索的点？

本文提出的半形式化推理方法虽有效，但仍存在局限性。首先，该方法依赖提示工程，推理过程可能产生幻觉或遗漏边缘情况，缺乏传统静态分析工具的严格形式化保证。其次，当前评估集中于特定任务和数据集，其泛化能力到更复杂、大规模或跨语言代码库仍需验证。未来研究可从以下方向深入：一是对模型进行后训练，使其内化半形式化推理结构，从而减少提示开销并提升准确率；二是将该方法扩展至漏洞检测、代码异味识别等更多静态分析任务，验证其通用性；三是探索混合验证路径，结合轻量级形式化方法或符号执行，在保持灵活性的同时增强推理的可靠性。此外，如何将此类推理能力无缝集成到实际开发与代码审查流水线中，并处理实时、增量式的代码变更，也是值得探索的实践挑战。

### Q6: 总结一下论文的主要内容

该论文研究了LLM智能体在不执行代码的情况下探索代码库并进行语义推理的能力，即“智能体代码推理”。核心贡献是提出了一种称为“半形式化推理”的结构化提示方法，要求智能体构建明确的前提、追踪执行路径并推导形式化结论。该方法作为一种“证明”，避免了非结构化思维链可能出现的跳过情况或缺乏支持的断言。

论文在三个任务上评估了该方法：补丁等价性验证、故障定位和代码问答。实验表明，半形式化推理在所有任务上都持续提升了准确性。具体而言，在补丁等价性验证上，对真实世界智能体生成补丁的验证准确率达到93%，接近无需执行的强化学习奖励信号所需的可靠性；在RubberDuckBench代码问答任务上达到87%准确率；在Defects4J故障定位任务上，Top-5准确率比标准推理提升了5个百分点。

主要结论是，结构化智能体推理使得无需执行的、有意义的代码语义分析成为可能，为强化学习训练管道、代码审查和静态程序分析等实际应用开辟了道路。该方法为传统静态分析提供了补充路径：无需将分析逻辑编码为专用算法，而是通过任务特定的提示格式实现跨语言和框架的泛化。未来工作包括对代码推理进行微调、将方法扩展到其他静态分析任务，以及探索与轻量级形式化方法的混合验证。
