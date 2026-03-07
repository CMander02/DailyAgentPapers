---
title: "AgentIR: Reasoning-Aware Retrival for Deep Research Agents"
authors:
  - "Zijian Chen"
  - "Xueguang Ma"
  - "Shengyao Zhuang"
  - "Jimmy Lin"
  - "Akari Asai"
date: "2026-03-04"
arxiv_id: "2603.04384"
arxiv_url: "https://arxiv.org/abs/2603.04384"
pdf_url: "https://arxiv.org/pdf/2603.04384v1"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Tongyi-DeepResearch, gpt-oss-120B, GLM-4.7"
  key_technique: "Reasoning-Aware Retrieval, DR-Synth"
  primary_benchmark: "BrowseComp-Plus"
---

# AgentIR: Reasoning-Aware Retrival for Deep Research Agents

## 原始摘要

Deep Research agents are rapidly emerging as primary consumers of modern retrieval systems. Unlike human users who issue and refine queries without documenting their intermediate thought processes, Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore. To exploit this overlooked signal, we introduce: (1) Reasoning-Aware Retrieval, a retrieval paradigm that jointly embeds the agent's reasoning trace alongside its query; and (2) DR-Synth, a data synthesis method that generates Deep Research retriever training data from standard QA datasets. We demonstrate that both components are independently effective, and their combination yields a trained embedding model, AgentIR-4B, with substantial gains. On the challenging BrowseComp-Plus benchmark, AgentIR-4B achieves 68\% accuracy with the open-weight agent Tongyi-DeepResearch, compared to 50\% with conventional embedding models twice its size, and 37\% with BM25. Code and data are available at: https://texttron.github.io/AgentIR/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（Deep Research agents）作为现代检索系统主要用户时，现有检索方法无法有效利用其独特交互模式的问题。研究背景是，随着大型语言模型的发展，能够自主推理并进行多轮搜索的深度研究智能体已成为一类新兴的检索系统用户。与传统人类用户不同，这些智能体在每次搜索调用前会生成显式的自然语言推理轨迹，其中包含了丰富的搜索意图和问题解决上下文信息。

现有方法的不足在于，传统的检索系统（如基于查询嵌入的模型或BM25）仅处理智能体最终发出的查询文本，完全忽略了其前置的推理轨迹。这导致在面对模糊或简短的查询时，检索结果往往不够精准，因为查询本身可能缺乏足够的上下文来明确表达智能体的真实意图。例如，智能体可能在前序推理中已明确某些关键细节或假设，但查询文本并未包含这些信息，使得检索效果大打折扣。

本文要解决的核心问题是：如何有效利用深度研究智能体生成的推理轨迹来提升检索性能。为此，论文提出了“推理感知检索”这一新范式，通过联合嵌入智能体的推理轨迹和查询，使检索器能够理解其背后的丰富意图和上下文。同时，针对深度研究场景中缺乏训练数据的问题，论文还提出了一种数据合成方法，从标准问答数据集中生成适用于智能体检索的训练样本，从而训练出高效的嵌入模型AgentIR-4B。最终，通过在挑战性基准测试上的验证，该方法显著超越了传统检索方法，实现了更高的准确性和效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作包括：1）**检索增强生成（RAG）**的演进，从单轮检索-回答流程发展到能够自主进行多轮搜索的语言模型，这为深度研究智能体的出现奠定了基础。2）**推理感知检索**，例如ReasonIR等工作，旨在处理需要复杂推理的单轮检索任务。3）**处理模糊查询**的方法，如指令感知检索、交互式澄清提问以及HyDE等方法，它们都致力于从查询之外挖掘额外信号来理解用户真实意图。

在**应用类**研究中，核心是**深度研究智能体**本身。这类智能体通过强化学习等技术加速发展，能够进行多轮、长时间的探索性检索来解决复杂问题，这与传统单轮RAG的设计目标有本质不同。

本文工作与上述研究的关系和区别在于：1）**与RAG演进和深度研究智能体的关系**：本文直接针对深度研究智能体这一新兴“用户”设计检索系统，旨在解决其固有的多轮检索新问题，这是对传统单轮RAG检索器的扩展。2）**与推理感知检索的区别**：类似ReasonIR等方法旨在让检索器自身在单轮内完成复杂推理和检索，而本文的AgentIR则侧重于与智能体**协作**，利用智能体在多轮中生成的显式推理轨迹来辅助每一轮的检索，目标是在多轮交互中共同解决复杂任务。3）**与模糊查询处理方法的区别**：传统方法需要主动挖掘或生成额外信号来弥补查询的不足，而本文方法则直接、免费地利用了深度研究智能体自然生成的、明确阐述其意图的**推理轨迹**作为富上下文信号，这是一种更直接和高效的意图利用方式。

### Q3: 论文如何解决这个问题？

论文通过提出“推理感知检索”这一新范式以及配套的数据合成方法DR-Synth来解决深度研究智能体检索中忽略其显式推理过程的问题。

核心方法是设计一个能够联合嵌入智能体推理轨迹和查询的检索器。整体框架基于标准的对比学习损失进行训练，其输入是智能体在每一步搜索前生成的推理文本τ_t与查询q_t的拼接。架构上，该方法将传统的单查询检索扩展为对“推理-查询”对的联合编码和匹配。关键技术在于利用深度研究智能体固有的多轮交互特性：智能体根据完整的历史交互生成推理，其中蕴含了任务意图、对先前结果的反思以及基于参数知识对未来搜索目标的假设。这些信息共同为当前查询提供了丰富的上下文，使其意图更明确。

为了训练这种新型检索器，论文提出了DR-Synth数据合成流程，以解决缺乏针对多轮子查询的训练数据的问题。该方法包含两个主要模块：1) **子查询生成模块**：利用一个基础检索器和智能体在标准QA数据集的问题Q上运行，收集轨迹中每一步的(τ_t, q_t)对。2) **监督信号生成模块**：通过一个“预言家重排序”过程为每个子查询产生相关文档标签。具体而言，在每一步t，先用基础检索器获取候选文档，然后混入全局正文档P，最后使用LLM根据当前查询q_t、全局问题Q和答案A对候选列表进行重排序，将排名最高的文档作为正例，排名最低的若干文档作为硬负例，从而得到训练三元组。

创新点主要体现在三个方面：一是首次系统性地提出并利用了深度研究智能体“免费”产生的推理轨迹作为检索的增强信号；二是设计了DR-Synth，一种从现有单轮QA数据合成多轮、子查询级别训练数据的方法；三是通过结合两者，训练出的AgentIR-4B模型显著优于更大的传统嵌入模型，证明了该范式的有效性。

### Q4: 论文做了哪些实验？

实验设置方面，研究者使用DR-Synth方法在WebShaper数据集上合成了5,238个训练实例，并以此通过对比学习微调Qwen3-Embedding-4B模型，得到最终模型AgentIR-4B。评估时，将检索器与三个开源深度研究智能体（Tongyi-DeepResearch、gpt-oss-120B和GLM-4.7）配对，在BrowseComp-Plus基准上进行端到端测试。该基准包含复杂的多跳查询，需要20次以上搜索。评估指标包括问答准确率（Accuracy）、检索文档相对于真实证据的召回率（Recall）以及智能体发出搜索调用的次数（Search Calls）。

对比方法包括三类：1）仅查询检索器，如BM25、Qwen3-Embedding-4B/8B、ReasonIR-8B；2）查询扩展方法，如Reason-Rewriter + Reason-Embed-8B（类似HyDE）以及同期工作Agentic-R；3）重排序方法，即使用Qwen3-8B对Qwen3-Embedding-4B检索的前20个结果进行列表重排序。

主要结果显示，AgentIR-4B在所有智能体上均取得最佳性能。关键数据指标如下：与Tongyi-DR配对时，AgentIR-4B准确率达66.27%，显著高于Qwen3-Embedding-4B骨干模型（48.67%）、Qwen3-Embedding-8B（50.72%）和ReasonIR-8B（51.03%）；搜索调用次数从BM25的32.92次降至25.91次，效率提升明显。即使与计算成本高的重排序方法（准确率55.66%）相比，AgentIR-4B仍高出约10%。此外，模型在gpt-oss-120B和GLM-4.7上也表现出强泛化能力，准确率分别达66.99%和64.66%。当Tongyi-DR启用额外访问工具时，AgentIR-4B准确率进一步提升至68.07%。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentIR方法虽然有效，但仍存在一些局限性和值得深入探索的方向。首先，该方法主要利用了当前推理步骤（τ_t）的信息，而实验表明引入更多历史推理步骤（k>1）会因信息冗余和噪声累积导致性能下降。这揭示了当前方法在有效利用长程、多轮交互历史方面的不足。未来的研究可以探索更智能的历史信息筛选与压缩机制，例如通过动态注意力或学习性摘要，来提取历史中的关键进展并过滤掉过时或错误的假设，从而更安全地利用更丰富的上下文。

其次，论文的实验主要基于合成的训练数据（DR-Synth）和有限的基准测试（如BrowseComp-Plus）。其泛化能力有待在更多样化的任务场景、不同的智能体架构以及真实世界的研究工作流中进行验证。一个重要的方向是研究如何使检索器适应不同风格、质量或结构的推理轨迹，甚至能够处理含有错误或误导性推理的情况，从而提升系统的鲁棒性。

此外，本文的检索范式与智能体的推理过程是相对独立的。一个更具潜力的方向是探索检索与推理的紧密协同与双向优化。例如，可以训练智能体生成更有利于检索的、结构化或带有明确信息需求的推理描述；反过来，检索结果也可以实时地指导或修正智能体的推理路径。这种深度耦合的“推理感知检索-检索增强推理”闭环，可能成为实现更强大、更高效深度研究智能体的关键。

### Q6: 总结一下论文的主要内容

本文针对深度研究智能体（Deep Research agents）提出了一种新的检索范式AgentIR，其核心贡献在于利用智能体在每次搜索调用前生成的显式自然语言推理轨迹（reasoning trace），这一信息在传统面向人类的检索系统中被完全忽略。论文首先定义了“推理感知检索”（Reasoning-Aware Retrieval）问题，即联合嵌入智能体的查询及其推理轨迹以更精准理解其搜索意图和上下文。为解决深度研究场景下多轮检索训练数据稀缺的问题，作者提出了DR-Synth数据合成方法，能够从标准问答数据集中自动生成所需的训练数据。实验表明，这两项贡献各自独立有效，而结合它们训练的嵌入模型AgentIR-4B在BrowseComp-Plus基准测试上取得了显著提升：与Tongyi-DeepResearch智能体配合达到68%的准确率，大幅优于规模更大的传统嵌入模型（50%）和BM25（37%）。主要结论是，推理轨迹能够将每次搜索锚定在智能体的历史上下文中，并充当一种隐式的历史信息筛选器，自动过滤掉先前轮次中的错误假设，从而提升检索效果。这项工作为检索器的“上下文工程”提供了新的方向。
