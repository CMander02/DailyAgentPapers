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
  - "Code Agent"
  - "Agent Benchmark"
  - "Architectural Understanding"
  - "Partial Observability"
  - "Belief State"
  - "Tool Use"
  - "Agent Evaluation"
relevance_score: 8.5
---

# Theory of Code Space: Do Code Agents Understand Software Architecture?

## 原始摘要

AI code agents excel at isolated tasks yet struggle with complex, multi-file software engineering requiring understanding of how dozens of modules relate. We hypothesize these failures stem from inability to construct, maintain, and update coherent architectural beliefs during codebase exploration. We introduce Theory of Code Space (ToCS), a benchmark that evaluates this capability by placing agents in procedurally generated codebases under partial observability, requiring them to build structured belief states over module dependencies, cross-cutting invariants, and design intent. The framework features: (1) a procedural codebase generator producing medium-complexity Python projects with four typed edge categories reflecting different discovery methods -- from syntactic imports to config-driven dynamic wiring -- with planted architectural constraints and verified ground truth; (2) a partial observability harness where agents explore under a budget; and (3) periodic belief probing via structured JSON, producing a time-series of architectural understanding. We decompose the Active-Passive Gap from spatial reasoning benchmarks into selection and decision components, and introduce Architectural Constraint Discovery as a code-specific evaluation dimension. Preliminary experiments with four rule-based baselines and five frontier LLM agents from three providers validate discriminative power: methods span a wide performance range (F1 from 0.129 to 0.646), LLM agents discover semantic edge types invisible to all baselines, yet weaker models score below simple heuristics -- revealing that belief externalization, faithfully serializing internal understanding into structured JSON, is itself a non-trivial capability and a first-order confounder in belief-probing benchmarks. Open-source toolkit: https://github.com/che-shr-cat/tocs

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI代码代理在理解复杂软件架构方面存在的核心能力缺陷问题。研究背景是，尽管大语言模型在单文件代码生成基准测试中表现优异，但在实际软件工程场景中，当需要理解和修改包含数十个相互依赖模块的真实代码库时，这些模型往往产生不连贯的结果，存在显著的实践差距。现有方法的不足在于，当前的评估基准主要关注被动代码生成，未能有效衡量AI代理在**主动探索、构建和维护代码库整体架构认知**方面的能力。具体而言，现有方法缺乏对代理在“部分可观测”环境下（即无法一次性看到所有代码）如何逐步形成并更新其关于模块依赖、设计意图等结构化信念的评估。

本文要解决的核心问题是：**AI代码代理是否具备以及如何具备对软件架构的理解和信念构建能力？** 为此，论文提出了“代码空间理论”基准，将空间推理中的认知地图诊断框架移植到软件工程领域。该基准通过程序化生成具有明确架构约束的中等复杂度代码库，让代理在有限的探索预算下主动查看文件，并定期要求其将内部架构信念外化为结构化JSON，从而系统性地评估代理**构建、维护和利用连贯架构信念**的能力。这超越了传统的静态代码理解评估，引入了“架构约束发现”这一代码特有的评估维度，以检验代理能否识别代码中植入的、可验证的设计约束。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：代码生成评测基准、代码理解工具以及空间推理研究。

在**代码生成评测基准**方面，SWE-bench、ContextBench、SWE-ContextBench、RepoBench、LoCoBench-Agent 和 RefactorBench 等均聚焦于评估代理在代码补全、错误修复或重构等任务中的输出正确性或上下文检索效率。然而，这些基准均不要求代理在探索过程中构建、维护并外化一个可修订的、结构化的架构信念状态，也未在部分可观测条件下设置探索预算或针对植入的架构约束进行评分。本文提出的 ToCS 基准则专门填补了这一空白，旨在直接评测代理对代码架构的理解和信念构建能力。

在**代码理解工具**方面，CodePlan 通过静态分析依赖图辅助LLM进行变更传播，Aider's RepoMap 利用解析和排序构建仓库上下文，Code World Models 则通过执行轨迹训练模型。这些工作可视为工程解决方案，其存在本身验证了本文的前提：代理需要架构地图但目前无法独立构建。ToCS 则提供了一个诊断性基准，用于测试这些方法是否真正提升了代理的架构信念质量。

在**空间推理研究**方面，Theory of Space 等工作在网格世界中揭示了主动-被动差距和信念惯性等现象。本文将此框架移植到代码领域，并增加了**架构约束发现**这一代码特有的评估维度，这是空间域中通常不涉及的。同时，本文对主动-被动差距进行了更细致的分解（选择与决策组件）。相关工作 TOM-SWE 关注代理对用户心智状态的建模，与本文关注代理对代码库的信念形成互补。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“代码空间理论”的基准测试框架来解决评估智能体在部分可观测环境下构建、维护和更新代码库架构信念能力的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
框架包含三个核心组件：
1.  **程序化代码库生成器**：自动生成中等复杂度的Python项目，其中植入了具有四种类型依赖边（如语法导入、API调用、数据流、注册表动态连接）的架构图、跨模块不变量和设计约束，并提供可验证的真实架构作为基准。
2.  **部分可观测性约束机制**：智能体在有限的行动预算（默认20次）下探索代码库。它只能通过一组固定语义的工具动作（如LIST、OPEN、SEARCH、INSPECT）来逐步获取信息，其中SEARCH仅返回位置而不提供内容，迫使智能体必须通过主动的OPEN决策来理解架构。
3.  **周期性信念探测与评估**：每间隔若干步（K=3），框架会免费中断智能体，要求其将当前的架构信念外部化为结构化的JSON输出。这产生了一个理解发展的时间序列，而不仅仅是最终状态。评估聚焦于三种操作：从部分观察中**构建**信念、在环境变化时**修订**信念、以及利用信念完成下游工程任务（当前版本通过反事实探测作为代理）。

**关键创新点与技术**：
1.  **对“主动-被动差距”的分解**：框架创新性地将传统空间推理中的性能差距分解为**选择成本**（智能体自主选择查看哪些文件的代价）和**决策成本**（智能体处理所获观察信息的代价）。这是通过设计四种对比实验条件实现的：主动探索、被动接收完整代码库、被动接收由预言机选择的最优文件序列、以及被动重放主动运行的观察轨迹。
2.  **引入“架构约束发现”作为评估维度**：除了依赖图重建，框架专门评估智能体是否能发现代码库中预设的、具有不同可发现性要求的高级设计约束（如禁止依赖、仅接口访问、验证链）。这通过反事实多选题进行探测。
3.  **强调信念外部化本身即关键能力**：实验发现，将内部理解准确序列化为结构化JSON是一项非平凡的任务，其能力差异成为信念探测评估中的首要混淆因素。这揭示了评估架构理解时需区分“实际理解”与“表达理解”的挑战。
4.  **轻量级探索通道设计**：INSPECT动作允许智能体以较低成本（一次动作）获取符号的类型签名和文档字符串，其中常包含架构关系的提示，为智能体提供了除完整阅读文件外的另一种高效发现途径。

综上，论文通过一个可控、可测量、聚焦于架构信念动态构建过程的基准测试框架，系统化地诊断和评估了代码智能体在复杂软件工程场景下的核心能力瓶颈。

### Q4: 论文做了哪些实验？

论文在ToCS基准上进行了初步实验，评估了规则基线和前沿大语言模型（LLM）智能体在部分可观测环境下理解代码架构的能力。

**实验设置与数据集**：实验在三个由程序生成的Python代码库（种子42、123、999）上进行，每个包含约27-30个模块。所有智能体在相同的部分可观测环境中探索，预算（B）固定为20个动作，每探索3步（K=3）进行一次结构化信念探测（JSON格式）。评估指标包括依赖关系F1分数、精确率、召回率、动作AUC（衡量早期发现效率）以及跨模块不变量的F1分数。

**对比方法**：评估了四类方法：
1.  **规则基线**：包括输出真实图的Oracle（理论上限，F1=1.0）、优先解析配置文件的Config-Aware、随机打开文件的Random以及广度优先跟随导入链的BFS-Import。这些基线仅从AST解析的导入和配置引用构建认知图。
2.  **LLM智能体**：来自三个提供商共五个前沿模型，包括OpenAI的GPT-5.3-Codex、Anthropic的Claude Sonnet 4.6，以及Google的Gemini 2.5 Flash、Gemini 2.5 Pro、Gemini 3 Flash和Gemini 3.1 Pro。所有模型使用相同的提示词，温度设为0（GPT-5.3-Codex因API限制设为1）。

**主要结果与关键指标**：
1.  **性能范围**：所有方法在依赖F1上表现跨度大（0.129至0.646）。最佳LLM智能体（GPT-5.3-Codex，F1=0.676；Claude Sonnet 4.6，F1=0.664）超越了最佳规则基线Config-Aware（F1=0.577）。
2.  **边缘类型发现**：LLM智能体能够发现全部四种语义边缘类型（imports, calls_api, data_flows, reg_wires），而规则基线最多只能发现两种（仅imports和reg_wires）。例如，GPT-5.3-Codex在imports上的召回率最高（69%），Gemini 3.1 Pro在data_flows上召回率最高（50%）。
3.  **信念外化瓶颈**：实验揭示了“信念外化”本身是一项重要能力。尽管某些Gemini模型表现出代码理解行为，但其在将内部理解序列化为结构化JSON时存在困难，表现为粒度不匹配、推理不足或信念状态不稳定（如Gemini 3 Flash的近期偏差导致知识丢失）。
4.  **效率与策略差异**：在动作AUC指标上，Claude Sonnet 4.6最高（0.350），表明其探索效率领先。不同模型展现出不同的精确率-召回率权衡：Claude近乎完美精确率（0.983）但召回率适中（0.502）；GPT-5.3-Codex以稍低的精确率（0.782）换取了最高召回率（0.597）；而Gemini 2.5 Pro虽有完美精确率（1.000），但召回率极低（0.138），反映了保守策略。
5.  **不变性发现**：改进后的提示使LLM智能体能够发现跨模块约束（不变性），其中Claude Sonnet 4.6的Inv F1最高（0.778），而所有规则基线在此项得分均为零。

### Q5: 有什么可以进一步探索的点？

基于论文讨论，可以进一步探索的点主要集中在以下几个方面：

**1. 提升信念外化能力与状态管理**：论文指出，即使模型具备代码理解能力，也可能在将内部理解序列化为结构化JSON时失败，这揭示了“信念外化”本身是一项关键且非平凡的能力。未来研究可以探索：
    *   **专门的训练目标**：设计训练任务，显式优化模型将架构知识忠实、结构化地输出的能力。
    *   **显式状态管理机制**：为智能体提供持久化、可累积的数据结构（如外部记忆或知识图谱），而非依赖其隐式维护信念状态，以解决类似Gemini模型表现出的信念状态不稳定（如灾难性遗忘、近因偏差）问题。

**2. 优化探索策略与混合方法**：
    *   **探索策略**：研究如何优化智能体的文件探索顺序和范围，因为更广的文件覆盖度与更高的召回率和独特边类型发现直接相关。可以结合主动学习或基于不确定性的探索策略。
    *   **混合架构分析**：结合基于AST的语法级依赖提取（确保结构完整性）与LLM的语义分析（增加深度），形成优势互补的混合方法。

**3. 完善评估基准与提示设计**：
    *   **提示规范与消融研究**：论文发现，许多“错误”源于提示本身的模糊性（如边类型定义互斥性、组件边界）。未来工作需将提示设计视为关键实验变量，进行系统性的消融研究（如改变模式细节、示例数量、思维链引导），以区分模型能力与提示敏感性。
    *   **更精细的评分机制**：采用分层评分（对语义等价答案给予部分分数）或标准化预测，避免将格式合规性与架构理解能力混为一谈。
    *   **扩展基准复杂性**：引入真实代码库的典型复杂性，如独立的架构文档（README、ADR）、文档过时问题（用于测试修订能力）、多语言项目、更丰富的架构模式，以及包含“死代码”等有机复杂性，使评估更贴近现实。

**4. 理解“探针即草稿”模式的影响**：在探针响应被保留并供后续步骤参考的模式下，探针提示不仅是被动测量工具，还主动塑造了智能体的探索策略。这开辟了一个研究方向：如何设计探针以积极引导智能体进行更有效的探索和信念更新，类似于一种元认知干预。

**5. 模型能力差异的深层原因**：不同模型家族（甚至同家族不同规模模型）在信念外化能力和稳定性上存在巨大差异（如最小模型反而最稳定），这暗示其根源可能在于训练目标或模型架构选择，而非单纯的规模大小。深入研究这些差异的成因，能为训练更鲁棒的代码智能体提供指导。

### Q6: 总结一下论文的主要内容

该论文针对当前AI代码代理在复杂多文件软件工程中表现不佳的问题，提出了“代码空间理论”（ToCS）这一评估框架。其核心假设是，失败源于代理在探索代码库时无法构建、维护和更新连贯的架构信念。

论文的主要贡献是设计了一个系统性基准测试。它首先通过程序化代码生成器创建具有已知架构约束的中等复杂度Python项目，其中包含四种需要通过不同方法（如语法分析或配置解析）发现的依赖关系类型。然后，在部分可观测性条件下，让代理在有限探索预算内进行代码库探索，并定期通过结构化JSON输出探测其架构信念，从而形成一个理解能力的时间序列。

方法上，论文将空间推理中的“主动-被动差距”分解为选择与决策两部分，并引入了“架构约束发现”这一针对代码的评估维度。初步实验验证了该基准的区分能力：不同方法性能差异显著，前沿大模型能发现基线方法不可见的语义边类型，但较弱模型的表现甚至不如简单启发式方法。一个重要结论是，“信念外化”——即将其内部理解忠实序列化为结构化JSON——本身是一项非平凡的能力，并成为信念探测类基准测试的首要混淆因素。该工作为评估和提升代码代理的软件架构理解能力提供了重要工具和见解。
