---
title: "DomAgent: Leveraging Knowledge Graphs and Case-Based Reasoning for Domain-Specific Code Generation"
authors:
  - "Shuai Wang"
  - "Dhasarathy Parthasarathy"
  - "Robert Feldt"
  - "Yinan Yu"
date: "2026-03-22"
arxiv_id: "2603.21430"
arxiv_url: "https://arxiv.org/abs/2603.21430"
pdf_url: "https://arxiv.org/pdf/2603.21430v1"
github_url: "https://github.com/Wangshuaiia/DomAgent"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Code Agent"
  - "Domain Adaptation"
  - "Knowledge Graph"
  - "Case-Based Reasoning"
  - "Retrieval-Augmented Generation"
  - "Autonomous Agent"
  - "Software Engineering"
relevance_score: 7.5
---

# DomAgent: Leveraging Knowledge Graphs and Case-Based Reasoning for Domain-Specific Code Generation

## 原始摘要

Large language models (LLMs) have shown impressive capabilities in code generation. However, because most LLMs are trained on public domain corpora, directly applying them to real-world software development often yields low success rates, as these scenarios frequently require domain-specific knowledge. In particular, domain-specific tasks usually demand highly specialized solutions, which are often underrepresented or entirely absent in the training data of generic LLMs. To address this challenge, we propose DomAgent, an autonomous coding agent that bridges this gap by enabling LLMs to generate domain-adapted code through structured reasoning and targeted retrieval. A core component of DomAgent is DomRetriever, a novel retrieval module that emulates how humans learn domain-specific knowledge, by combining conceptual understanding with experiential examples. It dynamically integrates top-down knowledge-graph reasoning with bottom-up case-based reasoning, enabling iterative retrieval and synthesis of structured knowledge and representative cases to ensure contextual relevance and broad task coverage. DomRetriever can operate as part of DomAgent or independently with any LLM for flexible domain adaptation. We evaluate DomAgent on an open benchmark dataset in the data science domain (DS-1000) and further apply it to real-world truck software development tasks. Experimental results show that DomAgent significantly enhances domain-specific code generation, enabling small open-source models to close much of the performance gap with large proprietary LLMs in complex, real-world applications. The code is available at: https://github.com/Wangshuaiia/DomAgent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在特定领域代码生成任务中表现不佳的核心问题。研究背景是，尽管LLM在通用代码生成基准上表现出色，但在现实软件开发中，许多任务（如卡车控制系统、数据科学）需要高度专业化的领域知识（如特定库的使用、领域逻辑和工作流适配），而这些知识在基于公开语料训练的通用LLM中往往缺失或代表性不足。现有方法主要存在两大不足：一是单纯依赖领域数据微调模型成本高昂且难以适应快速更新的库；二是主流的检索增强生成（RAG）方法虽更灵活，但通常仅基于文本相似性进行检索（如BM25或嵌入匹配），缺乏对领域内结构化概念关系和代表性案例的系统性利用，导致检索内容可能冗长、无关或覆盖不全，难以精准满足复杂领域任务的需求。

因此，本文要解决的核心问题是：如何高效、精准地让LLM获取并利用领域特定知识来生成高质量代码。为此，论文提出了DomAgent系统，其核心是通过模仿人类学习过程——结合自上而下的概念理解（来自结构化知识图谱）与自下而上的经验学习（来自案例库）——来弥补这一差距。具体而言，论文设计了新颖的检索模块DomRetriever，它动态集成知识图谱推理（提供结构化知识）和基于案例的推理（提供具体示例），实现迭代式检索与知识合成，以确保检索内容的上下文相关性和广泛的任务覆盖，从而显著提升领域特定代码生成的准确性和适应性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于检索增强生成（RAG）的方法、基于知识图谱（KG）的方法以及基于示例（如案例推理CBR）的方法。

在RAG方法中，早期研究如Yang等人使用BM25等基础检索方法，将外部知识库中的相关内容直接附加到提示中。后续工作如Li等人引入句子嵌入进行语义搜索以提高检索精度，而Wang等人和Zhu等人则分别通过文本分块和利用AST结构线索来解决长文本检索带来的信息过载问题。Gao等人进一步使用LLM过滤和压缩检索内容以保留关键信息。

在利用结构化知识方面，知识图谱（KG）因其能明确表示实体间关系而受到关注。例如，Ouyang等人将KG用作检索源，为代码修复任务提供相关信息，这比非结构化文本更适用于捕获领域特定的编程知识依赖。

在基于示例的方法中，上下文学习（ICL）和案例推理（CBR）是主流策略。Dannenhauer等人通过构建案例库并基于语义相似度动态选择示例来提升泛化能力。Nashid等人则利用AST分析重新排序候选案例，以捕捉纯文本相似度可能忽略的结构关系。此外，Tan等人提出了集成多源检索内容的分段提示策略，而Guo等人通过迭代优化构建大规模高质量案例库。

**本文与这些工作的关系和区别**：本文提出的DomAgent（特别是其DomRetriever模块）**综合并扩展了上述思路**。它并非单独使用KG或CBR，而是创新性地**动态整合了自上而下的KG推理与自下而上的CBR**，实现了结构化知识与代表性案例的迭代检索与合成。这与单纯进行文本检索、仅使用KG或仅动态选择案例的方法有显著区别。此外，本文方法旨在解决大型案例库维护成本高、难以适应快速演变工业环境的问题，通过KG引导的案例选择构建更精炼的案例库，从而在确保上下文相关性和广泛任务覆盖的同时，提升领域特定代码生成的适应性和效率。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为DomAgent的自主编码代理来解决领域特定代码生成问题，其核心是结合知识图谱（KG）的推理与基于案例的推理（CBR），并利用检索增强生成（RAG）技术。整体框架包含三个关键模块：案例库构建、检索增强的代码生成以及智能体训练。

首先，在案例库构建模块中，系统利用知识图谱中函数与代码案例之间的调用关系，通过分层案例选择策略来构建具有代表性的案例库。具体步骤包括：1）包级锚定，以软件包在KG中的根节点作为锚点，将其子节点（如函数和属性）的文本名称与描述编码为语义向量；2）函数级聚类，对每个包内的嵌入向量进行k-means聚类，以识别语义连贯的功能使用模式；3）覆盖驱动的案例选择，通过迭代遍历候选代码案例，选择那些能增加包覆盖率或聚类覆盖率的案例，直到达到预设的阈值，确保案例库既覆盖广泛包又包含多样化的功能模式。所有案例均经过执行验证，并存储于向量数据库中，以支持基于相似度的任务检索。

其次，在检索增强代码生成模块中，DomAgent采用自上而下与自下而上相结合的检索策略。给定任务描述，自上而下检索首先使用LLM分类器确定相关软件包，然后通过余弦相似度从KG中检索最相关的领域知识节点；自下而上检索则基于任务嵌入与案例描述的语义相似度获取初始案例列表，并通过计算案例与检索知识之间的包重叠度来进一步精炼。随后，一个推理LLM作为代理，通过调用封装的检索工具（如SearchKG和SearchCase）对检索结果进行审查，自动过滤无关知识或补充缺失信息，最终输出精炼后的领域知识和代表性案例。这些内容与原始任务描述拼接后，送入代码生成LLM以产生目标代码。

最后，在智能体训练模块中，论文采用强化学习来训练推理LLM自主调用检索工具并优化检索结果。通过手动创建少样本示例并利用强大LLM生成推理链，对模型进行微调，使其学会生成触发检索的特殊标记。进一步，使用奖励模型评估检索内容的相关性，并采用GRPO等强化学习算法更新模型参数，以最大化奖励信号，从而提升模型在解决编码任务时的推理和知识访问能力。

创新点在于：1）动态整合知识图谱推理与案例推理，模拟人类学习领域知识的方式；2）通过分层案例选择确保案例库的覆盖度和多样性；3）利用强化学习训练LLM自主管理检索过程，增强上下文相关性和任务覆盖范围。这种方法使得小规模开源模型在复杂现实应用中能显著缩小与大型专有LLM的性能差距。

### Q4: 论文做了哪些实验？

论文在两个数据集上进行了实验：公开基准数据集DS-1000和真实世界领域特定数据集Truck CAN Signal。

**实验设置与数据集**：在DS-1000数据集上，该数据集包含1000个源自Stack Overflow的数据科学任务，涵盖NumPy、Pandas等七个常用库。实验使用了为该领域构建的知识图DS-KG（包含505,640个三元组）。在卡车软件开发的真实场景中，任务涉及六个功能域的776个CAN信号的读写，使用了制造商内部文档作为领域知识。实验以LLaMA-3.1-8B-Instruct和Qwen-2.5-7B为骨干模型，使用500个示例进行工具调用训练，并从DS-1000中采样300个示例构建案例库，其余700个用于测试。评估指标为pass@1。

**对比方法与主要结果**：实验对比了原始大模型（如GPT-4o、Qwen2.5-7B）和多种代码生成智能体（如WizardCoder、Magicoder）。在DS-1000上，原始GPT-4o总体pass@1为51.0%，而基于Qwen2.5-7B的DomAgent达到39.2%，基于LLaMA3.1-8B的DomAgent达到40.5%，超越了所有其他同规模智能体（如MagicoderS-CL的37.5%）。当DomRetriever与大型外部模型结合时，性能进一步提升，例如LLaMA3.1-8B (DomRetriever) + GPT-4o达到58.6%，较原始GPT-4o提升7.6个百分点。在卡车CAN信号任务中，原始GPT-4o总体准确率为71.22%，结合DomRetriever后提升至98.04%；而基于Qwen2.5-7B的DomAgent达到96.64%，远超其原始基线（39.62%）。

**关键数据指标**：DS-1000上，DomAgent (LLaMA3.1-8B) 总体pass@1为40.5%；卡车任务中，DomAgent (Qwen2.5-7B) 总体准确率为96.64%。消融实验显示，在DS-1000上，知识图谱（KG）和基于案例的推理（CBR）各自带来提升，两者结合在DomAgent框架下效果最佳（如Qwen2.5-7B+KG+CBR总体提升9.9个百分点）。在卡车任务中，Qwen2.5-7B+KG+CBR (DomAgent) 较基线提升57.02个百分点，达到96.64%。

### Q5: 有什么可以进一步探索的点？

本文提出的DomAgent系统在结合知识图谱与案例推理方面取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，系统高度依赖领域知识图谱的构建质量，若图谱不完整或更新滞后，可能影响检索效果；其次，案例库的覆盖范围有限，对于高度新颖或边缘化的任务可能无法提供有效参考。未来研究可考虑引入动态知识图谱更新机制，通过在线学习实时整合新出现的领域概念与案例。此外，当前系统主要针对代码生成任务，其框架可扩展至其他需要领域适应的任务，如文档生成或自动化测试。另一个方向是探索多模态信息的融合，例如结合代码注释、API文档甚至视频教程，以提供更丰富的上下文。最后，可研究更高效的小模型微调策略，使系统在资源受限环境下仍能保持高性能，进一步推动领域特定AI代理的实用化。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在领域特定代码生成中成功率低的问题，提出了DomAgent这一自主编码代理。其核心贡献在于设计了DomRetriever检索模块，该模块模拟人类学习方式，通过结合知识图谱推理（自上而下的概念理解）和基于案例的推理（自下而上的经验示例），动态地迭代检索与合成结构化知识和代表性案例，从而为LLM提供高度相关且覆盖广泛的领域上下文。该方法使模型能够生成适应特定领域的代码。论文在数据科学基准DS-1000和真实卡车软件开发任务上进行了评估，结果表明DomAgent显著提升了领域特定代码生成性能，甚至能使小型开源模型在复杂实际应用中大幅缩小与大型专有LLM的性能差距。其意义在于为LLM的领域适应提供了一种灵活、有效的结构化推理与检索框架。
