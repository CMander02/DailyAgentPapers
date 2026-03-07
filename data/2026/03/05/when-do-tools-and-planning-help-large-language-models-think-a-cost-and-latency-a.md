---
title: "When Do Tools and Planning Help Large Language Models Think? A Cost- and Latency-Aware Benchmark"
authors:
  - "Subha Ghoshal"
  - "Ali Al-Bustami"
date: "2026-01-06"
arxiv_id: "2601.02663"
arxiv_url: "https://arxiv.org/abs/2601.02663"
pdf_url: "https://arxiv.org/pdf/2601.02663v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-4o, GPT-4o-mini"
  key_technique: "plan-execute-replan agent"
  primary_benchmark: "Event-QA, ChangeMyView (CMV)"
---

# When Do Tools and Planning Help Large Language Models Think? A Cost- and Latency-Aware Benchmark

## 原始摘要

Modern large language models (LLMs) increasingly rely on inference-time planning and external tools to improve reasoning. We benchmark this behavior on two real-world settings: event-centric question answering over graph-structured knowledge (Event-QA) and persuasive response generation in Reddit ChangeMyView (CMV). Using LangChain and LangGraph, we compare a one-shot baseline against a plan-execute-replan agent equipped with task-specific tools (DBpedia SPARQL/lookup/schema exploration, Wikipedia-focused retrieval, and topical web search). We evaluate on 60 examples each from Event-QA and CMV (3 splits of 20), and report both mean end-to-end latency and per-example token cost estimates. We evaluate GPT-4o and GPT-4o-mini under identical workflows and report accuracy and end-to-end latency. On Event-QA, the best tool-augmented configuration improves accuracy (e.g., 47.5\% $\rightarrow$ 67.5\% for GPT-4o) while increasing latency by orders of magnitude ($\sim$8s $\rightarrow$ $\sim$317s per example). On CMV, one-shot prompting is strongest (e.g., GPT-4o-mini achieves 75\% at $\sim$6s), and planning+search increases latency substantially without consistent gains. However, complex multi-tool orchestration exposes failure modes where the smaller model degrades. Overall, the findings highlight the need for task-specific, cost-aware choices of both model size and agent/tooling complexity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个当前LLM应用中的核心实践问题：在何种情况下，为大型语言模型配备推理时规划（planning）和外部工具（tools）才能真正提升其解决复杂现实任务的能力，同时需要系统性地权衡其带来的性能增益与成本、延迟开销。

研究背景在于，现代LLM已超越基础文本生成，广泛采用思维链（CoT）提示、自我一致性以及工具增强（如RAG、ReAct智能体）等推理时策略来提升多步推理和事实准确性。这些方法虽然常能提高答案正确性，但也必然引入额外的API调用、工具执行和模型思考时间，导致端到端延迟和计算成本大幅增加。现有研究往往侧重于展示这些方法在特定任务上的性能提升，却缺乏在统一、现实的约束条件下（尤其是成本和延迟）的系统性评估，未能明确回答“何时值得”采用更复杂的智能体工作流这一工程与产品决策中的关键问题。

因此，本文的核心问题是：**在面临真实世界的延迟和成本约束时，如何为特定任务明智地选择模型规模（大模型vs.小模型）以及智能体/工具的复杂度（简单单次提示vs.复杂多步规划工具调用）？** 论文通过构建一个包含规划-执行-重规划三阶段工作流的基准测试，在两个真实场景（基于图结构知识的事件问答Event-QA和基于开放域讨论的说服性回复生成CMV）上，实证比较了不同配置（模型、提示策略、工具使用）在准确率、延迟和估计成本上的权衡，旨在为成本感知的LLM系统设计提供具体指导。

### Q2: 有哪些相关研究？

本文的相关工作主要分为四个类别：

**1. 推理与推理时扩展方法**：这类研究关注如何通过增加推理时的计算来提升模型性能。例如，思维链（CoT）提示通过生成中间推理步骤来提升多步推理的准确性，但其单次生成可能不稳定。自我一致性解码通过采样多条推理路径来提升鲁棒性。更广泛的研究表明，通过额外采样、搜索或深思熟虑来增加推理时计算，有时能带来与扩大模型参数规模相媲美的收益。树状思维（Tree-of-Thoughts）等方法通过探索解决方案的搜索树来实现回溯和前瞻。本文的基准测试正是受到这些工作的启发，旨在比较一次性回答与需要显式分配额外计算的多阶段“计划-执行-重计划”流程。

**2. 工具增强与程序辅助的LLM**：这类研究旨在通过外部工具弥补LLM在参数化知识和事实基础方面的不足。代表性工作包括：检索增强生成（RAG），通过检索支持性证据来提升知识密集型任务的表现；ReAct框架，将推理轨迹与具体行动（如搜索）交错进行以改善任务完成度和可解释性；Toolformer，通过自监督方法教导模型何时调用API；以及程序辅助方法（如PAL、程序思维提示），将计算卸载给符号解释器。本文的基准测试与这些方向一致，不仅评估最终答案质量，还评估不同模型在多步控制逻辑下有效使用工具的实践能力，其中较小的模型可能因规划或工具调用错误而失败。

**3. 知识图谱与说服力评测基准**：在结构化知识访问方面，知识图谱问答长期受到关注，通常需要查询构建和实体链接。本文使用的Event-QA基准专门针对以事件为中心的问答，需要结构化检索和对事件图谱的推理。在说服力论证方面，Reddit的ChangeMyView（CMV）社区提供了一个自然的环境，被广泛用于说服力预测、论证质量建模等任务。本文利用这两个具有针对性的现实世界任务来构建基准，评估工具辅助的规划与检索相比直接生成能否带来改进。

**4. 成本感知部署的评估考量**：随着实际系统部署的需求增长，模型规模、推理时计算和工具开销之间的权衡日益受到关注。近期关于测试时扩展的研究强调，在推理时分配更多计算（通过采样、搜索等）可能是扩大参数规模的一种有竞争力的替代方案。在工具增强系统中，每次额外的工具调用都会增加延迟并引入错误累积的机会。本文的实验明确报告了不同规划和工具配置下的准确性和延迟，从而能够在更大模型与更小、更便宜的替代方案之间进行成本感知的比较。这与AgentBench、ToolBench等提供广泛环境覆盖的智能体评测工作形成互补，本文更侧重于两个特定任务中精度-延迟-成本的权衡。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的基准测试框架来解决“何时工具和规划对大型语言模型（LLM）的思考有帮助”的问题，其核心方法是**在真实世界任务中，对比不同复杂度的工作流，并量化评估其性能、成本和延迟**。

**整体框架与主要模块**：
研究基于 LangChain 和 LangGraph 实现了一个可复现的评估系统。整体框架包含两种主要的工作流模式：
1.  **单次推理基线**：LLM 直接接收问题/提示，无需任何工具，单次调用生成答案。
2.  **多阶段规划-执行-重规划智能体**：这是一个三状态的 LangGraph 智能体，包含：
    *   **规划器**：生成有序的步骤计划并选择要使用的工具。
    *   **执行器**：执行计划步骤，调用结构化工具（如搜索、查询），并将工具输出存储为证据。
    *   **重规划器/应答器**：判断证据是否足以回答问题；若不足，则修订计划并继续循环。

**关键技术组件与创新点**：
1.  **任务与工具定制化**：针对两个不同的真实任务（Event-QA 和 CMV），设计了特定的工具集。对于 Event-QA（基于知识图谱的问答），提供了 **DBpedia 工具套件**（SPARQL查询、实体查找、模式探索）和**维基百科聚焦检索**。对于 CMV（说服性回复生成），则使用了**主题网络搜索**工具，并将搜索主题细分为10个政策相关类别，以提高检索针对性。
2.  **迭代调优协议**：为了在准确性和运行时之间取得平衡，研究采用了**分步迭代调优**的方法。先在小型试点集上初始化提示和控制器，然后在三个数据分片上进行顺序调优和保留评估，最终报告调优后的稳定性能。这一方法旨在系统性减少工具使用失败（如实体解析错误、SPARQL构造错误）并改进规划质量。
3.  **多维评估指标**：核心创新在于不仅评估**准确性**，还系统性地量化了**端到端延迟**和**每个示例的估算令牌成本**。这使得研究能够清晰揭示工具增强带来的性能提升与随之而来的巨大开销（延迟增加数个数量级）之间的权衡。
4.  **模型与配置对比**：在相同的工作流下，对比了不同规模的模型（GPT-4o 与 GPT-4o-mini）以及不同复杂度的配置（无规划、单工具规划、多工具规划）。这种对比揭示了任务特异性：在 Event-QA 上，最佳工具增强配置能显著提升准确性；而在 CMV 上，单次提示往往更强，增加规划与搜索反而会大幅增加延迟且无稳定收益。同时，复杂的多工具编排会暴露较小模型的性能退化问题。

总之，论文通过构建一个包含定制化工具、多阶段智能体工作流、迭代调优协议以及成本与延迟感知评估指标的综合性基准测试框架，系统地分析和回答了在何种情况下为LLM增加工具和规划能力是必要且高效的。

### Q4: 论文做了哪些实验？

论文在两个真实世界任务上进行了实验：事件中心知识图谱问答（Event-QA）和Reddit ChangeMyView（CMV）说服性回复生成。实验设置上，使用LangChain和LangGraph框架，比较了单次提示（NoPlanning）基线方法与一个配备特定工具的“计划-执行-重计划”智能体。工具包括针对Event-QA的DBpedia SPARQL查询、查找、模式探索，以及针对CMV的以维基百科为中心的检索和主题网络搜索。

数据集与基准测试方面，从Event-QA和CMV数据集中各随机抽取60个样本，并分别划分为3个各含20个样本的子集（Event-QA按问题类型分层）。评估指标包括准确率和端到端平均推理延迟（含所有规划、工具调用时间）。对于CMV的开放式生成，使用ROUGE-1 F值（阈值τ=0.27）判断回复正确性以计算准确率。

对比方法主要包括：单次提示基线（NoPlanning）、使用维基百科检索的工具增强方法（Wikipedia）、使用DBpedia多工具的方法（DBpedia，仅Event-QA）以及结合规划与搜索的方法（PlanningSearch，仅CMV）。测试模型为GPT-4o和GPT-4o-mini。

主要结果与关键指标如下：
1.  **Event-QA**：工具增强方法能提升准确率但大幅增加延迟。最佳配置为GPT-4o使用DBpedia工具，最终准确率（Split 2 & 3平均）达67.5%（较基线47.5%提升20%），但平均推理时间增至约317秒/样本（基线约8秒）。GPT-4o-mini使用维基百科配置在速度与准确率间较平衡，最终准确率55%，延迟约84秒。
2.  **CMV**：单次提示基线表现最强，且延迟极低。GPT-4o-mini的NoPlanning配置最终准确率达75%，平均延迟仅约6秒；GPT-4o的NoPlanning配置为70%准确率，延迟类似。而规划加搜索（PlanningSearch）方法虽增加延迟（GPT-4o约21-27秒，GPT-4o-mini约150-216秒），却未带来一致的准确率提升，有时甚至下降。

总体表明，工具与规划的效益高度依赖于任务特性，需在性能、延迟和成本间进行权衡。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其工具链依赖外部动态资源（如DBpedia和维基百科），可能引入非确定性和时效性问题，且评估仅基于两个特定任务（Event-QA和CMV），泛化性有待验证。未来研究可从以下方向深入：首先，探索更普适的“任务复杂度-工具效用”映射理论，建立预测模型以指导不同场景下工具与规划策略的自动选择；其次，设计轻量级、自适应的工具调用机制，例如通过动态剪枝或早期终止来平衡延迟与精度，避免当前方案中高达数十倍的延迟开销；此外，可研究多工具协同的鲁棒性优化，特别是针对小模型在复杂编排中的性能退化问题，引入纠错或回退策略。最后，需构建更全面的评估框架，纳入长期稳定性、资源消耗及经济成本等多维度指标，推动高效能Agent系统的实际部署。

### Q6: 总结一下论文的主要内容

该论文提出了一个在成本和延迟约束下评估大语言模型（LLM）推理时规划与工具使用效果的基准。核心问题是探究在现实任务中，复杂的“思考”（如多步规划与外部工具调用）何时能真正提升性能，而非徒增开销。研究聚焦于两个代表性场景：基于图结构知识的事件问答（Event-QA）和开放域说服性回复生成（CMV）。

方法上，论文使用LangChain和LangGraph构建了一个“规划-执行-重规划”智能体，配备了DBpedia查询、检索等任务特定工具，并与简单的一次提示（NoPlanning）基线进行对比。评估指标包括准确率、端到端延迟和估算的令牌成本。

主要结论表明，工具和规划的价值高度依赖于任务特性。在Event-QA中，工具增强能显著提升准确率（如GPT-4o从47.5%升至67.5%），但代价是延迟急剧增加（从约8秒增至约317秒）。而在CMV任务中，一次提示基线（尤其是使用较小的GPT-4o-mini）在保持极低延迟的同时取得了最佳准确率，增加规划和检索反而无益。研究揭示了一个实用的部署启发式：应从低成本、低延迟的简单基线开始，仅当任务需要结构化证据访问或多步组合时才引入规划和工具，并仅在工具协调成为瓶颈时才考虑升级到更大模型。这强调了在实际应用中需根据任务需求，在模型能力、工具复杂性与成本延迟间做出权衡。
