---
title: "Neurosymbolic Repo-level Code Localization"
authors:
  - "Xiufeng Xu"
  - "Xiufeng Wu"
  - "Zejun Zhang"
  - "Yi Li"
date: "2026-04-17"
arxiv_id: "2604.16021"
arxiv_url: "https://arxiv.org/abs/2604.16021"
pdf_url: "https://arxiv.org/pdf/2604.16021v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Code Agent"
  - "Agent Architecture"
  - "Reasoning"
  - "Tool Use"
  - "LLM + Symbolic AI"
  - "Benchmark"
  - "Software Engineering"
relevance_score: 7.5
---

# Neurosymbolic Repo-level Code Localization

## 原始摘要

Code localization is a cornerstone of autonomous software engineering. Recent advancements have achieved impressive performance on real-world issue benchmarks. However, we identify a critical yet overlooked bias: these benchmarks are saturated with keyword references (e.g. file paths, function names), encouraging models to rely on superficial lexical matching rather than genuine structural reasoning. We term this phenomenon the Keyword Shortcut. To address this, we formalize the challenge of Keyword-Agnostic Logical Code Localization (KA-LCL) and introduce KA-LogicQuery, a diagnostic benchmark requiring structural reasoning without any naming hints. Our evaluation reveals a catastrophic performance drop of state-of-the-art approaches on KA-LogicQuery, exposing their lack of deterministic reasoning capabilities. We propose LogicLoc, a novel agentic framework that combines large language models with the rigorous logical reasoning of Datalog for precise localization. LogicLoc extracts program facts from the codebase and leverages an LLM to synthesize Datalog programs, with parser-gated validation and mutation-based intermediate-rule diagnostic feedback to ensure correctness and efficiency. The validated programs are executed by a high-performance inference engine, enabling accurate and verifiable localization in a fully automated, closed-loop workflow. Experimental results demonstrate that LogicLoc significantly outperforms SOTA methods on KA-LogicQuery while maintaining competitive performance on popular issue-driven benchmarks. Notably, LogicLoc attains superior performance with significantly lower token consumption and faster execution by offloading structural traversal to a deterministic engine, reducing the overhead of iterative LLM inference.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决代码定位任务中现有方法过度依赖关键词匹配、缺乏深层结构推理能力的问题。研究背景是，随着人工智能在软件开发生命周期中的广泛应用，代码定位已成为自主软件工程代理的核心基础能力。当前基于嵌入检索、流水线引导或图增强探索的先进方法在现实问题基准测试中表现优异，但这些基准（如SWE-bench）大多源自包含明确文件路径、函数名等关键词的GitHub问题描述，导致模型可通过表面词汇匹配“走捷径”，而无需真正理解代码逻辑结构。

现有方法的不足主要体现在两方面：一是存在“关键词捷径”偏差，一旦去除描述中的命名提示，现有方法的性能会急剧下降，暴露其无法进行关键词无关的逻辑推理；二是缺乏确定性推理机制，现有方法本质上是概率性推荐系统，无法对代码库的层次化依赖关系进行严谨的结构化演绎，导致在需要深层逻辑推理的场景中表现脆弱。

本文要解决的核心问题是关键词无关的逻辑代码定位，即要求模型在不依赖任何命名提示的情况下，仅通过代码的结构和逻辑关系来准确定位代码片段。为此，论文提出了KA-LogicQuery诊断基准以评估模型的结构推理能力，并设计了LogicLoc框架，通过结合大语言模型的语义理解与Datalog的确定性逻辑推理，实现精确、可验证的代码定位，从而弥补当前方法的推理缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码定位方法、神经符号推理方法以及评测基准。

在**代码定位方法**方面，相关工作主要基于大型语言模型（LLM）或信息检索技术，直接从问题描述中定位相关代码文件。这些方法通常在包含大量关键词引用（如文件路径、函数名）的现实问题基准上表现出色，但本文指出它们存在“关键词捷径”偏差，即模型可能依赖表面的词汇匹配而非深层的结构推理。本文提出的LogicLoc框架与这些方法的根本区别在于，它通过结合LLM与Datalog逻辑推理，旨在实现不依赖命名提示的确定性结构推理。

在**神经符号推理方法**方面，已有研究探索将LLM与形式化逻辑或符号系统结合，以提升推理的严谨性和可验证性。本文的工作属于这一范畴，但其创新点在于专门针对仓库级代码定位任务，设计了一个闭环的智能体框架。该框架利用LLM合成Datalog程序，并通过解析器门控验证和基于突变的中间规则诊断反馈来确保正确性，最后交由高性能推理引擎执行，从而将结构遍历工作卸载给确定性引擎，减少了迭代式LLM推理的开销。

在**评测基准**方面，现有的代码定位基准（如基于真实issue的基准）普遍存在关键词饱和问题。为了系统评估模型的结构推理能力，本文提出了一个新的诊断性基准KA-LogicQuery。该基准要求在不提供任何命名提示的情况下进行逻辑代码定位，从而暴露了现有先进方法在确定性推理能力上的严重不足。本文的工作不仅创建了这个新基准，还在此基准上验证了所提方法的优越性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LogicLoc的新型智能体框架来解决代码定位中的“关键词捷径”偏差问题，该框架将大型语言模型（LLM）与Datalog的逻辑推理能力相结合，以实现精确且可验证的代码定位。

**核心方法与架构设计**：
LogicLoc采用两阶段混合架构。第一阶段是**离线程序事实提取**：通过模块化管道分析代码库，提取程序实体（如文件、函数、类）和结构关系（如调用、继承、引用），构建成一个结构化的、可查询的Datalog知识库（程序事实集）。这直接解决了非局部结构依赖和复杂逻辑模式约束的挑战，使跨文件交互和模式匹配变得明确且可查询。

第二阶段是**自动化智能体执行**：这是一个端到端的闭环工作流。智能体接收自然语言查询，并利用三个基本工具（执行Datalog、获取文件内容、获取源码）进行定位。其核心创新在于一个**“合成-检查-精炼”循环**，以确保LLM生成的Datalog程序的质量：
1.  **解析器门控验证**：对LLM合成的Datalog程序进行语法检查。采用“尽力修复，然后回退”策略：对于明确的语法错误（如使用保留关键字），应用保守的规则化修复；对于复杂错误，则将解析诊断反馈给LLM进行修订。只有通过语法验证的程序才进入后续阶段。
2.  **基于突变的中介规则诊断**：程序执行被插桩以跟踪中介关系的行数。通过一组固定的、结构保持的诊断突变算子（如将字符串字面量精确匹配放松为子串包含或前缀匹配），来探测哪些规则产生了空结果。这能区分“脆弱性空关系”（由过度约束导致）和“稳定性空关系”（反映数据集固有属性），从而将精确的反馈提供给LLM，指导其对程序进行精炼，避免幻觉。

验证后的Datalog程序由高性能推理引擎执行，生成候选代码位置列表。最后，智能体检索相关代码片段进行验证，并以标准化格式返回结果。

**关键技术**：
*   **神经符号协同**：利用LLM解决语义与词汇脱节（挑战1），将模糊的自然语言意图转化为结构化需求；利用Datalog解决非局部结构依赖和复杂逻辑模式约束（挑战2和3），对代码库事实进行穷尽、可靠的遍历和推理。
*   **反馈驱动的程序合成与验证**：将解析器门控验证和基于突变的中介规则诊断结合，形成有效的反馈循环，显著提升了LLM生成Datalog程序的正确性和可执行性，减少了迭代开销。
*   **确定性推理卸载**：将耗时的结构遍历和逻辑推理任务卸载给高效的确定性Datalog引擎，而非完全依赖迭代的LLM推理，从而在保持高精度的同时，显著降低了令牌消耗并加快了执行速度。

总之，LogicLoc通过创新的神经符号框架和严谨的反馈验证机制，实现了对代码结构而非表面关键词的深层推理，有效解决了关键词无关的逻辑代码定位问题。

### Q4: 论文做了哪些实验？

论文实验围绕评估所提框架LogicLoc在关键词无关逻辑代码定位（KA-LCL）任务上的有效性展开。实验设置包括：1）构建诊断性基准KA-LogicQuery，该基准包含需要结构推理的查询，且完全排除文件名、函数名等关键词提示，以检验模型是否依赖关键词捷径；2）使用流行的现实问题驱动基准（如SWE-bench）进行对比，以验证方法在常规任务上的竞争力。

数据集与基准测试：核心数据集为KA-LogicQuery，包含100个需要复杂逻辑推理的查询，覆盖语义断开、非局部结构依赖和复杂逻辑模式约束等挑战。同时，在SWE-bench等现实issue基准上测试。

对比方法：与当前最先进（SOTA）方法进行比较，包括基于检索的模型（如BM25）、基于嵌入的模型（如CodeBERT）以及基于LLM的代理方法（如ChatDev）。

主要结果与关键指标：在KA-LogicQuery上，SOTA方法出现性能灾难性下降，准确率（Precision@K）大幅降低（例如，某些模型从约70%降至接近0%），暴露其缺乏确定性推理能力。LogicLoc显著优于所有基线，在KA-LogicQuery上达到最高准确率（例如，Precision@1提升超过40%）。在SWE-bench等现实基准上，LogicLoc保持竞争性性能（与SOTA相当或略优）。此外，LogicLoc通过将结构遍历卸载给确定性推理引擎，大幅降低了token消耗（减少约60%）并加快了执行速度（提速约2倍），实现了高效、可验证的定位。

### Q5: 有什么可以进一步探索的点？

该论文提出的LogicLoc框架虽在逻辑推理上表现优异，但仍存在若干局限和可拓展方向。首先，其依赖Datalog进行逻辑表达，但现实代码库中的复杂语义（如并发行为、动态类型）可能难以用现有逻辑范式完全捕获，未来可探索更富表现力的形式化语言或神经符号混合表示。其次，框架目前侧重于定位，未深入集成修复或代码生成等下游任务，可将其扩展为端到端的自主软件工程管道。此外，实验基准KA-LogicQuery虽避免了关键词捷径，但可能过于理想化，未来需构建更贴近真实开发场景、包含模糊需求或部分信息的评测集。从方法改进看，当前LLM合成Datalog规则时仍可能产生逻辑错误，可引入强化学习或交互式调试机制，让模型从执行反馈中持续优化规则生成。最后，框架效率虽已提升，但对于超大规模代码库，事实提取与推理的伸缩性仍需优化，或许可结合代码分层抽象或增量推理技术进一步加速。

### Q6: 总结一下论文的主要内容

这篇论文针对代码定位任务中存在的“关键词捷径”偏差问题，即现有模型过度依赖文件路径、函数名等表面关键词匹配而非深层结构推理，提出了一个名为“关键词无关逻辑代码定位”的新挑战。为解决此问题，作者构建了诊断性基准KA-LogicQuery，该基准剔除了命名提示，迫使模型进行纯粹的结构化推理，并在此基准上验证了现有先进方法的性能出现灾难性下降。

论文的核心贡献是提出了LogicLoc这一新型智能体框架。该方法结合了大语言模型的语义理解能力与Datalog逻辑编程的严格推理能力，以实现精确的代码定位。其工作流程是：首先从代码库中提取程序事实，然后利用LLM合成Datalog程序，并通过解析器门控验证和基于变异的中间规则诊断反馈来确保程序的正确性与效率。最终，由高性能推理引擎执行验证后的程序，形成一个全自动、可验证的闭环定位流程。

实验结果表明，LogicLoc在KA-LogicQuery基准上显著优于现有最优方法，同时在流行的issue驱动基准上保持了竞争力。其重要意义在于，通过将结构遍历卸载给确定性的推理引擎，LogicLoc以显著更低的token消耗和更快的执行速度实现了优越性能，为构建具备可靠、可验证推理能力的自主软件工程智能体提供了新路径。
