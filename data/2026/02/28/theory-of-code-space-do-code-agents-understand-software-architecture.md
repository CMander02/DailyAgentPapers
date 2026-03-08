---
title: "Theory of Code Space: Do Code Agents Understand Software Architecture?"
authors:
  - "Grigory Sapunov"
date: "2026-02-28"
arxiv_id: "2603.00601"
arxiv_url: "https://arxiv.org/abs/2603.00601"
pdf_url: "https://arxiv.org/pdf/2603.00601v2"
github_url: "https://github.com/che-shr-cat/tocs"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Code & Software Engineering"
  - "Memory & Context Management"
relevance_score: 9.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Theory of Code Space (ToCS)"
  primary_benchmark: "Theory of Code Space (ToCS)"
---

# Theory of Code Space: Do Code Agents Understand Software Architecture?

## 原始摘要

AI code agents excel at isolated tasks yet struggle with complex, multi-file software engineering requiring understanding of how dozens of modules relate. We hypothesize these failures stem from inability to construct, maintain, and update coherent architectural beliefs during codebase exploration. We introduce Theory of Code Space (ToCS), a benchmark that evaluates this capability by placing agents in procedurally generated codebases under partial observability, requiring them to build structured belief states over module dependencies, cross-cutting invariants, and design intent. The framework features: (1) a procedural codebase generator producing medium-complexity Python projects with four typed edge categories reflecting different discovery methods -- from syntactic imports to config-driven dynamic wiring -- with planted architectural constraints and verified ground truth; (2) a partial observability harness where agents explore under a budget; and (3) periodic belief probing via structured JSON, producing a time-series of architectural understanding. We decompose the Active-Passive Gap from spatial reasoning benchmarks into selection and decision components, and introduce Architectural Constraint Discovery as a code-specific evaluation dimension. Preliminary experiments with four rule-based baselines and five frontier LLM agents from three providers validate discriminative power: methods span a wide performance range (F1 from 0.129 to 0.646), LLM agents discover semantic edge types invisible to all baselines, yet weaker models score below simple heuristics -- revealing that belief externalization, faithfully serializing internal understanding into structured JSON, is itself a non-trivial capability and a first-order confounder in belief-probing benchmarks. Open-source toolkit: https://github.com/che-shr-cat/tocs

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI代码代理在理解复杂软件架构方面的核心能力缺陷。研究背景是，尽管大语言模型在单文件代码生成基准测试中表现出色，但在处理包含数十个相互依赖模块的真实代码库修改任务时，却常常产生不连贯的结果，这暴露了其与人类开发者之间的能力鸿沟。现有基于静态、全知视角的评估方法无法诊断这一问题的根源，它们通常一次性提供全部代码信息，未能模拟开发者需要主动探索和理解代码结构的真实场景。

现有方法的不足在于，它们缺乏一个能够系统评估AI代理在“部分可观测”条件下，如何主动构建、维护和更新对软件架构连贯认知的基准测试。近期空间推理领域的“空间理论”研究为诊断此类问题提供了框架，指出了智能体在主动探索时可能出现的“主动-被动差距”和“信念惯性”问题，但该框架尚未被应用于代码理解领域。

因此，本文要解决的核心问题是：如何评估和诊断AI代码代理是否具备在逐步探索代码库的过程中，形成并保持对软件架构（包括模块依赖、设计意图、跨模块约束等）的连贯、结构化认知的能力。为此，论文提出了“代码空间理论”基准，通过程序化生成具有明确架构的代码库，让代理在有限的“打开文件”预算下进行探索，并定期要求其以结构化JSON形式输出其架构信念，从而量化评估其架构理解能力的构建、修正和利用过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码生成评测基准、代码理解工具以及空间推理研究。

在**代码生成评测基准**方面，SWE-bench、ContextBench、SWE-ContextBench、RepoBench、LoCoBench-Agent 和 RefactorBench 等工作关注于代码补全、错误修复、上下文检索或多文件重构等任务，并主要评估输出正确性或检索效率。本文的 ToCS 与这些工作的核心区别在于：它不直接评估任务完成度，而是专注于在部分可观测条件下，系统性地评测智能体对代码库架构（如模块依赖、设计约束）的**动态信念状态**的构建与更新能力，并要求智能体将内部信念外化为结构化表示。现有基准均未涉及对可修订的、带类型的架构信念进行时序性探测和评分。

在**代码理解工具**方面，CodePlan 和 Aider‘s RepoMap 等工具通过静态分析或图算法为LLM提供外部依赖图，旨在辅助代码任务。这从工程角度印证了本文的前提——智能体需要架构理解，但当前无法自主构建。ToCS 则提供了一个诊断性基准，用于检验这些工具或方法是否能真正提升智能体自主形成的架构信念质量。

在**空间推理**方面，Theory of Space 等工作在网格世界中提出了主动-被动差距和信念惯性等概念。本文将此框架移植到代码领域，关键创新是引入了**架构约束发现**这一代码特有的评估维度（空间域中物体放置的“原因”通常无意义），并系统地将主动-被动差距分解为选择与决策两个组件，以更精细地分析智能体的探索效率。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“Theory of Code Space (ToCS)”的综合性基准测试框架来解决评估代码智能体理解软件架构能力的问题。其核心方法并非直接提升智能体的性能，而是创建一个系统性的评估环境，以诊断和衡量智能体在部分可观测条件下构建、维护和更新对代码库架构连贯信念的能力。

**整体框架与主要模块**：
1.  **程序化代码库生成器**：这是框架的基础。它自动生成中等复杂度的Python项目，其核心创新在于定义并植入了四种具有语义的依赖边类型（imports, calls_api, data_flows_to, registry_wires），这些边反映了从语法导入到配置驱动的动态连接等不同的发现方式。每个生成的代码库都包含预设的架构约束（如禁止依赖、接口访问）和可验证的真实架构状态（ground truth）。
2.  **部分可观测性交互环境**：智能体在一个有预算（默认B=20次动作）限制的环境中进行主动探索。它只能通过一组固定的工具动作（LIST, OPEN, SEARCH, INSPECT, DONE）来逐步获取信息。关键设计是，SEARCH只返回位置而不返回内容，迫使智能体必须通过OPEN决策来深入理解代码；INSPECT则提供了一个低成本获取模块关系和目的（通过文档字符串）的渠道，模拟了实际开发中的线索发现。
3.  **周期性信念探测与评估机制**：这是评估的核心。每隔K=3个动作，框架会免费中断智能体，要求其将内部对架构的理解“外化”为结构化的JSON认知地图。这份地图需包含组件信念、依赖边、架构约束信念以及不确定性追踪。这一过程产生一个理解演化的时间序列，而不仅仅是最终状态。评估聚焦于三个操作：构建（Construct）、修订（Revise）和利用（Exploit）架构信念。

**关键技术设计与创新点**：
1.  **对“主动-被动差距”的分解**：论文创新性地将空间推理基准中的概念引入代码领域，并通过设计四种实验条件（Active, Passive-Full, Passive-Oracle, Passive-Replay），将总差距分解为“选择差距”（因文件选择不当导致的损失）和“决策差距”（因信息处理不当导致的损失），从而更精细地诊断智能体失败的根源。
2.  **引入“架构约束发现”作为评估维度**：超越传统的依赖图恢复，ToCS明确评估智能体是否能发现代码中隐含的设计规则（如禁止依赖、接口隔离），这是理解高级软件设计意图的关键，也是代码智能体面临的新挑战。
3.  **揭示“信念外化”本身即是一项关键能力**：初步实验发现，即使大型语言模型能发现基线方法无法察觉的语义边，但较弱的模型在结构化JSON输出上的得分可能低于简单启发式方法。这表明，将内部理解准确、结构化地序列化输出本身就是一个非平凡的能力，是信念探测类基准测试中一个首要的混淆因素。这一洞察是评估方法论上的重要贡献。

综上，论文通过构建一个可控、可度量、具有丰富语义和挑战性的基准测试生态系统，系统地定义了“代码空间理解”问题，并提供了诊断工具来深入分析代码智能体在架构层面认知能力的优势与局限。

### Q4: 论文做了哪些实验？

论文在三个生成的代码库（种子42、123、999）上，在预算B=20、探测间隔K=3的相同条件下，评估了四种基于规则的探索策略和来自三个提供商的五种前沿大语言模型智能体。

**实验设置与数据集**：使用论文提出的Theory of Code Space (ToCS)基准框架。核心是一个程序化代码库生成器，产生中等复杂度的Python项目，其中包含四种类型的模块依赖边（imports, calls_api, data_flows, reg_wires），并植入了架构约束和已验证的真实情况。评估在部分可观测环境下进行，智能体在有限的探索预算内行动，并通过结构化的JSON格式定期探测其架构信念。

**对比方法**：
1.  **规则基线**：包括直接输出真实图的Oracle（理论上限F1=1.0）、优先解析配置文件的Config-Aware、随机打开文件的Random以及广度优先跟随导入链的BFS-Import。这些基线通过AST解析构建认知图。
2.  **大语言模型智能体**：包括OpenAI的GPT-5.3-Codex、Anthropic的Claude Sonnet 4.6，以及Google的Gemini 2.5 Flash、Gemini 2.5 Pro、Gemini 3 Flash和Gemini 3.1 Pro。所有模型使用相同的提示词，温度设为0（GPT-5.3-Codex因API限制设为1）。

**主要结果与关键指标**：
*   **性能范围**：所有方法在依赖关系发现的F1分数上跨度很大（从0.129到0.646）。表现最佳的两个LLM智能体（GPT-5.3-Codex F1=0.676， Claude Sonnet 4.6 F1=0.664）超越了所有规则基线（最佳基线Config-Aware F1=0.577）。
*   **边缘类型发现**：LLM智能体能够集体发现全部四种依赖边类型，而规则基线最多只能发现两种（仅imports和reg_wires）。例如，GPT-5.3-Codex在imports边的召回率最高（69%），Gemini 3.1 Pro在data_flows边的召回率最高（50%）。
*   **架构约束发现**：在改进的探测提示下，LLM智能体在架构约束（Invariant）发现上取得了显著分数（如Claude Sonnet 4.6的Inv F1=0.778），而所有规则基线在此项得分为零。
*   **效率与策略**：在衡量早期发现效率的AUC指标上，Claude Sonnet 4.6（0.350）和GPT-5.3-Codex（0.306）表现突出，优于Config-Aware（0.212）。不同模型展现出不同的精度-召回权衡：Claude精度接近完美（0.983）但召回适中（0.502），GPT-5.3-Codex以稍低的精度（0.782）换取了最高召回（0.597）。
*   **信念外化瓶颈**：实验揭示了“信念外化”本身是一项关键能力。一些Gemini模型尽管打开了相当数量的文件，却表现出信念状态不稳定（如遗忘先前发现）或报告粒度不匹配等问题，导致其性能甚至低于简单启发式方法。

### Q5: 有什么可以进一步探索的点？

基于论文讨论，可以进一步探索的点包括：在技术层面，未来研究可以开发混合方法，结合AST级别的导入提取与LLM语义分析，以在保证结构完整性的同时增加语义深度。同时，需针对信念外化能力进行专门训练，优化模型将架构知识准确序列化为结构化格式的能力。探索策略也需优化，例如扩大文件覆盖范围以提升召回率，并引入显式的状态管理机制，为智能体提供持久、累积的数据结构，而非依赖其隐式维护信念状态，这有助于解决如Gemini系列模型出现的信念状态不稳定等新失败模式。

在评估与基准设计方面，论文揭示了提示词规范本身是影响性能的一阶变量，未来应进行提示词消融研究，明确边缘类型决策规则和组件边界定义，并采用分层评分机制，区分格式合规性与真实架构理解。此外，需扩展基准的复杂性，例如引入包含独立文档（如README、设计文档）的代码库，以模拟真实世界中通过文档发现架构、处理文档过时问题等场景，并评估智能体在资源有限时是否懂得查阅外部文档。

从更广阔的视角看，当前研究聚焦于单一架构模式（Pipeline）和语言（Python），未来可扩展到多种架构风格（如微服务、事件驱动）和编程语言，以检验智能体架构理解能力的通用性。生成代码库虽结构真实，但使用了中性文件名，未来可纳入真实代码库的命名先验和有机复杂性，使评估更贴近实际工程挑战。这些方向将共同推动代码智能体从处理孤立任务向真正理解复杂软件系统架构迈进。

### Q6: 总结一下论文的主要内容

该论文针对当前AI代码代理在复杂多文件软件工程任务中表现不佳的问题，提出其根本原因在于代理缺乏在探索代码库时构建、维护和更新连贯架构信念的能力。为此，作者提出了“代码空间理论”（ToCS）这一基准测试框架，旨在系统评估代理的软件架构理解能力。

ToCS框架的核心贡献包括：1) 一个过程化代码库生成器，能创建具有已知架构约束的中等复杂度Python项目，其中包含四种需要通过不同方法（从语法导入到配置驱动的动态连接）来发现的依赖边类型；2) 一个部分可观测性环境，代理需在有限探索预算下工作；3) 通过结构化JSON定期探测代理的信念状态，形成架构理解的时间序列。论文还将空间推理中的主动-被动差距分解为选择和决策两个部分，并引入了“架构约束发现”这一代码特有的评估维度。

初步实验验证了该基准的区分能力：不同方法（包括四种基于规则的基线和五种前沿LLM代理）的性能差异显著（F1分数从0.129到0.646）。研究发现，LLM代理能发现所有基线方法无法察觉的语义边类型，但能力较弱的模型得分甚至低于简单启发式方法。这揭示了“信念外化”——即将内部理解忠实地序列化为结构化JSON——本身是一项非平凡的能力，并且是信念探测基准测试中的首要混淆因素。该工作为评估和改进代码代理的架构理解能力提供了重要工具和洞见。
