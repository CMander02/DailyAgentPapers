---
title: "AgentIR: Reasoning-Aware Retrieval for Deep Research Agents"
authors:
  - "Zijian Chen"
  - "Xueguang Ma"
  - "Shengyao Zhuang"
  - "Jimmy Lin"
  - "Akari Asai"
date: "2026-03-04"
arxiv_id: "2603.04384"
arxiv_url: "https://arxiv.org/abs/2603.04384"
pdf_url: "https://arxiv.org/pdf/2603.04384v2"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 9.0
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

# AgentIR: Reasoning-Aware Retrieval for Deep Research Agents

## 原始摘要

Deep Research agents are rapidly emerging as primary consumers of modern retrieval systems. Unlike human users who issue and refine queries without documenting their intermediate thought processes, Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore. To exploit this overlooked signal, we introduce: (1) Reasoning-Aware Retrieval, a retrieval paradigm that jointly embeds the agent's reasoning trace alongside its query; and (2) DR-Synth, a data synthesis method that generates Deep Research retriever training data from standard QA datasets. We demonstrate that both components are independently effective, and their combination yields a trained embedding model, AgentIR-4B, with substantial gains. On the challenging BrowseComp-Plus benchmark, AgentIR-4B achieves 68\% accuracy with the open-weight agent Tongyi-DeepResearch, compared to 50\% with conventional embedding models twice its size, and 37\% with BM25. Code and data are available at: https://texttron.github.io/AgentIR/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（Deep Research agents）作为现代检索系统主要用户时，现有检索方法未能充分利用其独特交互模式的问题。研究背景是，随着大型语言模型的发展，能够自主推理并进行多轮搜索的深度研究智能体已成为一类新兴的检索系统用户。与传统人类用户不同，这些智能体在每次搜索调用前会生成显式的自然语言推理轨迹，其中包含了丰富的搜索意图和问题解决上下文信息。

现有方法的不足在于，传统的检索系统（如基于查询嵌入的模型或BM25）仅处理智能体发出的最终查询文本，完全忽略了其前置的推理轨迹。这导致在面对模糊或简短的查询时，检索结果往往不够精准，因为查询本身可能缺乏足够的上下文来明确表达智能体的真实信息需求。例如，智能体可能在前序推理中已识别出关键奖项、音乐子类型或搜索历史中的关键线索，但这些信息未被纳入检索过程，造成检索效率低下。

本文要解决的核心问题是：如何有效利用深度研究智能体生成的推理轨迹来提升检索性能。为此，论文提出了“推理感知检索”这一新范式，通过联合嵌入智能体的推理轨迹和查询，使检索器能够理解并利用推理中蕴含的意图和上下文信息。同时，针对深度研究场景中缺乏训练数据的问题，论文还提出了一种数据合成方法，从标准问答数据集中生成适用于智能体检索的训练数据，以训练出更高效的嵌入模型。最终，通过结合这两项创新，论文旨在显著提升深度研究智能体在复杂研究任务中的检索准确性和效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作包括：1）**深度研究智能体**，这类工作基于检索增强生成（RAG）和强化学习，发展出能自主进行多轮搜索以解决复杂问题的智能体，其多轮特性是本文要解决的新检索问题。2）**检索与推理结合**，如ReasonIR和RaDeR等检索器旨在处理需要推理的复杂任务，但它们的目标是让检索器在单轮内独立完成任务，而本文的AgentIR则专注于在多轮中与智能体**协作**进行检索。3）**处理模糊查询**，传统方法如指令感知检索、交互式澄清提问或HyDE（利用LLM生成假设上下文）都试图挖掘用户查询之外的意图信号。本文与这些工作的核心区别在于，深度研究智能体**免费提供了明确的推理轨迹**作为丰富信号，本文方法正是学习利用这一被现有检索器忽略的信息。

在**应用与评测层面**，本文的工作建立在BrowseComp-Plus等基准测试之上，这些基准用于评估复杂任务上的性能。本文提出的DR-Synth数据合成方法，从标准QA数据集生成训练数据，也属于为训练此类新型检索器而进行的数据构建方法创新。

综上，本文与相关工作的关系是继承并深化了多轮检索智能体和推理感知检索的方向，其核心区别在于首次系统性地利用智能体显式的、中间过程的推理轨迹来提升检索效果，并提出了配套的数据合成方法。

### Q3: 论文如何解决这个问题？

论文通过提出“推理感知检索”这一新范式，并结合数据合成方法DR-Synth，来解决深度研究智能体检索中忽略其显式推理过程的问题。

核心方法是构建一个能够联合嵌入智能体推理轨迹和查询的检索系统。整体框架基于标准的对比学习损失进行训练，其输入是智能体在每一步搜索时生成的推理轨迹τ_t与查询q_t的拼接表示[τ_t, q_t]。该方法的关键在于，它不再像传统检索那样仅处理孤立的查询，而是将智能体在生成查询前的完整思考过程（即推理轨迹）作为额外的、富含意图和上下文信息的信号，与查询一并输入给检索器。

主要模块包括两个部分：一是推理感知检索范式本身，二是用于生成训练数据的DR-Synth管道。推理感知检索是架构设计的核心创新，它直接利用深度研究智能体在标准ReAct循环中“免费”产生的推理轨迹。这些轨迹从三个方面增强检索：阐明模糊查询背后的具体任务意图；反映对先前搜索结果的分析和整合；提出基于参数知识和交互历史的假设性搜索目标。这与需要额外LLM调用的查询扩展方法（如HyDE）有本质区别，因为其推理是智能体自身状态的自然产物。

然而，现成的嵌入模型并未针对此类“推理+查询”的输入进行优化。因此，论文提出了DR-Synth数据合成方法，以生成所需的训练数据。该模块首先利用一个基础检索器和智能体，在标准QA数据集（包含全局问题Q、答案A和相关文档集P）上进行多轮推演，从而提取出每一步的子查询q_t及其对应的推理轨迹τ_t。关键的创新在于其监督信号生成机制：对于每一步t，它采用一个“预言家重排序”流程。具体而言，将全局相关的文档P混入基础检索器返回的候选文档中，然后提示一个大语言模型，根据当前子查询q_t、全局问题Q和答案A，对候选文档进行列表式重排序，以确保文档既与当前步骤相关，又与全局目标一致。重排序后的顶部文档被标记为正例，底部文档作为硬负例，从而为每一步构造出高质量的训练样本( [τ_t, q_t], d^+_t, {d^-_t} )。

最终，通过DR-Synth合成的数据对检索模型进行训练，得到的AgentIR-4B模型在BrowseComp-Plus基准测试上取得了显著优于传统检索模型（包括规模更大的模型）的性能，验证了联合利用推理轨迹与查询这一范式的有效性。

### Q4: 论文做了哪些实验？

实验设置方面，研究者使用DR-Synth方法在WebShaper数据集上合成了5,238个训练实例，并以此对Qwen3-Embedding-4B模型进行对比学习微调，得到最终模型AgentIR-4B。评估时，将其与三个开源深度研究智能体（Tongyi-DeepResearch、gpt-oss-120B、GLM-4.7）结合，在BrowseComp-Plus基准上进行端到端测试。该基准包含复杂的多跳查询，需要超过20次搜索。评估指标包括问答准确率（Accuracy）、检索文档相对于真实证据的召回率（Recall）以及智能体发出的搜索调用次数（Search Calls）。

对比方法涵盖三类基线：1）仅查询检索器，包括BM25、微调前的Qwen3-Embedding-4B、Qwen3-Embedding-8B和ReasonIR-8B；2）查询扩展方法，如Reason-Rewriter + Reason-Embed-8B（一种微调后的HyDE式扩展器）以及同期工作Agentic-R；3）重排序方法，即使用Qwen3-8B对Qwen3-Embedding-4B检索的前20个文档进行列表级重排序。

主要结果显示，AgentIR-4B在所有智能体上均取得最佳性能。关键数据指标如下：与Tongyi-DR配合时，其准确率达到66.27%，相比骨干模型Qwen3-Embedding-4B（48.67%）绝对提升17.60%，且优于规模大一倍的Qwen3-Embedding-8B（50.72%）；搜索调用次数从BM25的32.92次降至25.91次，效率显著提升。同时，AgentIR-4B也超越了计算代价高昂的重排序方法（55.66%准确率）。该模型在泛化性方面表现突出，在未微调的情况下，于gpt-oss-120B和GLM-4.7智能体上分别达到66.99%和64.66%的准确率，并可与“访问”工具协同工作，在Tongyi-DR（Visit）设置下准确率进一步提升至68.07%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其方法主要依赖于当前推理轨迹，而忽略了历史信息的有效整合。分析表明，增加历史推理轮次并未提升检索效果，这主要由于信息冗余和噪声引入。未来研究可探索更智能的历史信息筛选机制，例如动态选择与当前查询最相关的历史片段，而非简单截断。此外，论文仅验证了合成数据训练的有效性，但未深入探讨不同合成策略的影响，未来可研究如何生成更高质量、多样化的训练数据以进一步提升模型泛化能力。另一个方向是扩展该方法到多模态检索场景，使智能体能同时处理文本、图像等多源信息。最后，可考虑将推理感知检索与智能体的决策过程更紧密耦合，实现端到端的优化，从而在复杂任务中取得更大突破。

### Q6: 总结一下论文的主要内容

本文针对深度研究智能体（Deep Research agents）作为现代检索系统主要用户的新兴场景，提出了“推理感知检索”新范式。核心问题是传统检索系统仅处理孤立查询，而智能体在每次搜索前会生成显式的自然语言推理轨迹，其中蕴含了丰富的意图和上下文信息，现有检索器完全忽略了这一信号。

论文的核心贡献包括两方面：一是提出了“推理感知检索”范式，该方法将智能体的推理轨迹与其查询共同嵌入，以联合利用这些信息；二是设计了DR-Synth数据合成方法，能够从标准问答数据集中自动生成适用于深度研究场景的多轮检索器训练数据。实验表明，这两个组件各自独立有效，而结合它们训练出的嵌入模型AgentIR-4B性能显著提升。在BrowseComp-Plus基准测试中，该模型配合通义深度研究智能体取得了68%的准确率，大幅优于规模更大的传统嵌入模型和BM25方法。

主要结论是，显式利用推理轨迹能有效将每次搜索锚定在智能体的历史上下文中，同时该轨迹本身充当了历史信息的隐式筛选器，能自然过滤掉先前轮次中的错误假设。这项工作为检索器的“上下文工程”指明了未来方向。
