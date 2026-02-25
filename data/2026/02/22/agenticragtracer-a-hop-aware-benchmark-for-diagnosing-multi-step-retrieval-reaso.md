---
title: "AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG"
authors:
  - "Qijie You"
  - "Wenkai Yu"
  - "Wentao Zhang"
date: "2026-02-22"
arxiv_id: "2602.19127"
arxiv_url: "https://arxiv.org/abs/2602.19127"
pdf_url: "https://arxiv.org/pdf/2602.19127v1"
categories:
  - "cs.CL"
tags:
  - "Agentic RAG"
  - "评测基准"
  - "多步推理"
  - "诊断工具"
  - "数据合成"
relevance_score: 8.0
---

# AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG

## 原始摘要

With the rapid advancement of agent-based methods in recent years, Agentic RAG has undoubtedly become an important research direction. Multi-hop reasoning, which requires models to engage in deliberate thinking and multi-step interaction, serves as a critical testbed for assessing such capabilities. However, existing benchmarks typically provide only final questions and answers, while lacking the intermediate hop-level questions that gradually connect atomic questions to the final multi-hop query. This limitation prevents researchers from analyzing at which step an agent fails and restricts more fine-grained evaluation of model capabilities. Moreover, most current benchmarks are manually constructed, which is both time-consuming and labor-intensive, while also limiting scalability and generalization. To address these challenges, we introduce AgenticRAGTracer, the first Agentic RAG benchmark that is primarily constructed automatically by large language models and designed to support step-by-step validation. Our benchmark spans multiple domains, contains 1,305 data points, and has no overlap with existing mainstream benchmarks. Extensive experiments demonstrate that even the best large language models perform poorly on our dataset. For instance, GPT-5 attains merely 22.6\% EM accuracy on the hardest portion of our dataset. Hop-aware diagnosis reveals that failures are primarily driven by distorted reasoning chains -- either collapsing prematurely or wandering into over-extension. This highlights a critical inability to allocate steps consistent with the task's logical structure, providing a diagnostic dimension missing in traditional evaluations. We believe our work will facilitate research in Agentic RAG and inspire further meaningful progress in this area. Our code and data are available at https://github.com/YqjMartin/AgenticRAGTracer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前Agentic RAG（基于智能体的检索增强生成）评估中存在的关键缺陷。具体而言，现有用于评估多跳推理能力的基准数据集（如HotpotQA）通常只提供最终的问题-答案对，而缺乏连接原子问题与最终复杂查询的中间步骤（hop-level）问题。这导致研究者无法精确定位智能体在哪个推理或检索步骤失败，从而限制了进行细粒度能力诊断的可能性。此外，现有基准大多依赖人工构建，成本高、可扩展性差，且可能存在多跳复杂性标注不真实、与RAG设置前提不符（如依赖模型先验知识而非可检索证据）以及未提供完整知识库索引等问题。为此，论文提出了AgenticRAGTracer这一首个支持逐步验证、主要利用大语言模型自动构建的基准，专注于诊断Agentic RAG中的多步检索推理过程，并通过引入“跳感知”分析，揭示错误如何在推理链中累积，例如因推理步骤与任务逻辑结构不匹配而导致的链条过早崩溃或过度扩展。

### Q2: 有哪些相关研究？

相关研究主要涵盖三个方向：Agentic RAG、多跳检索评测基准以及数据合成技术。

在**Agentic RAG**方面，早期研究如RAG框架将检索与生成结合，后续发展出Advanced RAG、Modular RAG和Graph RAG等静态流水线系统。近期研究转向集成智能体能力（如规划、工具使用和反思）的Agentic RAG，旨在实现动态检索决策和多步交互的编排，相关工作包括对系统的形式化研究以及利用强化学习优化推理-搜索轨迹的探索。

在**多跳检索评测基准**方面，现有工作主要包括两类：一是早期人工构建的基准，如HotpotQA、2WikiMultihopQA等，它们虽被广泛使用但构建耗时且扩展性有限；二是近期利用大语言模型辅助生成的基准，如MoreHopQA、MultiHop-RAG和MINTQA，但这些方法存在局限，例如仅扩展已有基准的跳数，或缺乏对生成问题的细粒度质量控制。

在**数据合成**方面，已有研究广泛探索了利用LLM驱动的工作流系统（如DataFlow）在文本和多模态领域生成高质量合成数据，用于增强模型在各种下游任务上的能力。

本文与这些工作的关系在于：针对现有Agentic RAG评测基准在**中间步骤标注缺失**和**人工构建 scalability 不足**两大核心痛点，本文提出的AgenticRAGTracer基准首次实现了**以LLM为主进行自动构建**，并支持**逐跳（hop-aware）的诊断性评估**。它不同于仅扩展跳数的MoreHopQA，也不同于缺乏细粒度控制的MultiHop-RAG/MINTQA，通过提供中间跳级问题，能够更精细地分析智能体在多步推理中的失败环节（如推理链过早崩溃或过度扩展），从而弥补了传统评估的诊断性维度缺失。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AgenticRAGTracer的基准测试来解决现有Agentic RAG评估中缺乏中间步骤诊断和可扩展性的问题。其核心方法是一个主要由大语言模型（LLM）自动生成、并辅以严格人工审核的多步骤数据构建流程。

**核心方法与架构设计**：
1.  **数据基础与原子问题生成**：从维基百科文档库中采样，并过滤掉与现有基准重叠的文档以确保新颖性。使用LLM从文档中合成“原子”问答对（即单跳问题），并通过启发式过滤、参数知识排除和基于上下文的可解性验证三个步骤保证质量。
2.  **多跳问题设计**：设计了两种核心推理拓扑结构来全面评估智能体能力：**顺序推理**（Inference），需要逐步的逻辑链；**并行比较**（Comparison），需要先收集多个实体的独立信息再进行综合。以此为基础构建2跳问题。
3.  **严格的验证协议**：生成的2跳候选问题需经过三重严格验证：
    *   **结构完整性过滤**：剔除存在语法逻辑缺陷、信息泄露或简单拼接的问题。
    *   **语义逻辑验证**：使用LLM审核员剔除推理链不连贯的问题，例如强行连接无关实体或无效比较。
    *   **多跳必要性与可解性检查**：确保问题必须依赖检索、证据链不可简化（移除任一支撑文档即无法回答），并且在给定全部证据时可解。
4.  **扩展到更高跳数**：将已验证的2跳问题迭代扩展至3-4跳，并施加相同的严格过滤流程，以创建具有挑战性的高阶问题。
5.  **质量控制的最后防线**：使用维基百科SPARQL查询消除实体歧义，并对整个数据集进行全量人工验证，由多名标注者检查事实性、忠实度和推理步骤有效性，并通过讨论达成共识，最终弗莱斯Kappa系数为0.65，表明标注一致性较高。

**关键技术**：
*   **LLM驱动的自动化与规模化构建**：利用LLM作为核心工具进行文档标注、原子QA生成、多跳问题合成与逻辑验证，大幅降低了传统人工构建的成本，并实现了基准的规模化和可泛化。
*   **跳数感知的诊断框架**：基准不仅提供最终问答，还包含了连接原子问题到最终查询的中间跳级问题，使得研究者能够精确定位智能体在哪一步失败，实现细粒度能力评估。
*   **多样化的评估维度**：通过涵盖多种领域、平衡两种推理拓扑、以及设置2-4跳的难度梯度，基准能够全面评估智能体在顺序规划、并行信息整合以及长链条推理中的表现。实验结果（如GPT-5在4跳推理上仅22.6%的准确率）及步骤分析（揭示模型存在推理链过早坍塌或过度延伸的问题）验证了其诊断价值。

### Q4: 论文做了哪些实验？

论文在统一的实验设置下评估了多种大语言模型，包括闭源模型（GPT和Grok系列）、开源模型（DeepSeek和Qwen系列）以及基于Qwen2.5-7B-Instruct微调的Agentic RAG模型（如Search-R1）。评估使用Qwen-Agent框架，遵循ReAct范式进行推理与行动的交替。报告了精确匹配（EM）、F1分数和基于LLM的评判分数。

主要结果显示，基准测试对模型的多跳推理能力构成挑战。即使在最强的GPT-5模型上，在4跳推理子集上的EM准确率也仅为22.6%。性能随着推理跳数（从2跳到4跳）的增加而普遍下降，且所有模型在推理子集上的表现均差于比较子集。闭源模型（如GPT-5、o4-mini和Grok-4）整体优于大多数开源模型，但GPT-4o表现意外不佳。分析发现，高性能模型（如Grok-4、GPT-5）倾向于在每一步检索更多文档（更大的top-k值），而GPT-4o和DeepSeek-V3则采用保守的检索策略，导致信息积累不足。

多跳分析表明，模型失败时，其正确回答的平均最高跳数揭示了推理深度的局限性。错误案例分析发现，绝大多数失败源于初始任务分解的错误，导致后续推理链整体偏离正确轨迹。讨论部分指出，当前模型缺乏在遇到矛盾证据时进行自主评估和轨迹修正的动态元认知能力。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其基准构建虽自动化，但仍需人工验证以确保逻辑保真度，这限制了数据规模的进一步扩展。此外，当前诊断主要聚焦于推理链的扭曲（过早崩溃或过度扩展），未深入探究导致这些现象的具体内部机制，如模型的知识冲突或检索噪声的影响。

未来方向可从三方面探索：一是提升基准的完全自动化生成能力，通过更精细的规则或强化学习减少人工干预，以支持更大规模、多领域的评估。二是深化诊断维度，结合可解释性技术分析模型在各步骤中的注意力模式或知识检索偏差，从而揭示推理失效的根本原因。三是推动智能体自我修正机制的研究，基于步骤级诊断结果开发动态调整推理路径或进行链式验证的方法，以增强Agentic RAG系统的鲁棒性与适应性。

### Q6: 总结一下论文的主要内容

这篇论文提出了AgenticRAGTracer，这是首个专为Agentic RAG（检索增强生成）设计的、支持逐步验证的自动化构建基准。其核心贡献在于解决了现有评估体系的两个关键缺陷：一是缺乏中间步骤（hop-level）的细粒度诊断能力，无法定位智能体在多步推理中具体在哪一环失败；二是突破了传统人工构建基准的规模与泛化性限制。该基准通过大语言模型自动生成，涵盖多领域，包含1305个数据点，且与现有主流数据集无重叠。实验表明，即使是顶尖大模型（如GPT-5）在其最难子集上的精确匹配准确率也仅为22.6%，凸显了现有智能体在复杂多步检索推理上的严重不足。更重要的是，通过“跳数感知”诊断，论文揭示了失败主因是推理链的扭曲（过早终止或过度延伸），即模型无法根据任务逻辑结构合理分配推理步骤。这项工作为Agentic RAG研究提供了关键的诊断维度和评估工具，将推动该领域向更精细、可解释的方向发展。
