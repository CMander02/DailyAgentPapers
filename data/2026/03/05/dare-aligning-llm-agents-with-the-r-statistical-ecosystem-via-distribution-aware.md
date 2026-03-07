---
title: "DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval"
authors:
  - "Maojun Sun"
  - "Yue Wu"
  - "Yifei Xie"
  - "Ruijian Han"
  - "Binyan Jiang"
date: "2026-03-05"
arxiv_id: "2603.04743"
arxiv_url: "https://arxiv.org/abs/2603.04743"
pdf_url: "https://arxiv.org/pdf/2603.04743v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Code & Software Engineering"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Code & Software Engineering"
  domain: "Data Science & Analytics"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "DARE (Distribution-Aware Retrieval Embedding)"
  primary_benchmark: "N/A"
---

# DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval

## 原始摘要

Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在自动化数据科学工作流时，难以有效利用R语言庞大且严谨的统计生态系统的问题。研究背景是，尽管基于LLM的智能体在自动化Python生态中的数据科学任务上取得了进展，但R语言作为统计计算的核心平台，拥有CRAN上数千个经过同行评审、方法严谨的专业包，这些资源在现有LLM智能体中未被充分利用。这是因为LLM的训练语料严重偏向通用编程语言（尤其是Python），导致其在处理R语言时存在知识鸿沟，经常出现幻觉函数、误用参数或无法识别正确统计包的问题。

现有方法的不足在于，当前缓解该问题的检索增强生成（RAG）方法主要依赖用户查询与函数文本描述之间的语义相似性进行检索。然而，统计方法的适用性不仅取决于语义意图，更关键地依赖于数据分布特征（如稀疏性、维度、分布假设等）。通用的嵌入模型无法捕捉这些细微但至关重要的分布条件，导致检索结果不准确，进而引发下游代码生成和执行失败。

因此，本文要解决的核心问题是：如何让LLM智能体能够根据具体的数据分布特征，精准地检索和调用R统计生态系统中合适的工具包和方法。为此，论文提出了一个分布感知的检索解决方案，旨在缩小LLM自动化能力与成熟的R统计生态系统之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM数据科学智能体、稠密检索与RAG，以及工具学习。

在**LLM数据科学智能体**方面，已有工作通过赋予LLM规划、代码执行、自我修正和报告生成等能力，使其能够自动化数据科学工作流。然而，现有智能体主要依赖Python生态，对R语言的支持有限且代码生成质量较低，原因在于训练数据中R语言的稀缺性。本文提出的RCodingAgent正是为了弥补这一缺口，专注于面向R语言的可靠代码生成。

在**稠密检索与RAG**领域，代表性工作如DPR、Contriever等双编码器架构，以及近期通过扩大参数规模和指令微调取得领先的模型（如Snowflake Arctic、Gte-large-en-v1.5）。这些通用模型在一般基准上表现优异，但其设计侧重于语义相似性，难以捕捉统计计算场景中至关重要的数据分布特征和模型假设等兼容性因素，且大模型带来较高的检索计算开销。本文的DARE模型则针对性地将数据分布信息显式融入函数表示学习，实现了面向统计工具的高效、精准检索。

在**工具学习**方面，主流方法依赖于上下文学习与API描述，将工具选择与代码生成紧密耦合。本文工作的区别在于引入了一个独立的、数据感知的检索模块（DARE），将工具选择与生成过程解耦，从而能够可扩展地访问海量统计函数，使智能体能在下游数据分析任务中有效利用更广泛的R包。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为DARE（Distribution-Aware Retrieval Embedding）的轻量级、即插即用检索模型来解决LLM代理在R统计生态系统中工具检索不佳的问题。核心方法是**将数据分布信息融入函数表示**，以提升检索的相关性。

**整体框架与主要模块**：
1.  **RPKB（R Package Knowledge Base）**：首先构建一个高质量的R包知识库作为检索基础。从CRAN的8,191个包中，通过提取、函数级分块与过滤、数据配置文件生成和存储四个阶段，精心筛选出专注于核心统计原语和计算算法的高质量R函数集合。每个函数被形式化定义为包含自然语言文档和结构化数据配置文件的元组。
2.  **DARE检索模型**：这是核心创新模块。采用**双编码器架构**，共享一个基于`sentence-transformers/all-MiniLM-L6-v2`初始化的编码器网络。其关键创新在于，编码器的输入不仅包含用户查询`q`和函数文档`d`的语义信息，还**拼接了数据配置文件**（`c_q`和`c_d`）。这些配置文件（如数据模态、分布假设、维度）由LLM从文档或数据集中推断，编码了数据分布的约束。模型通过计算查询嵌入向量与函数嵌入向量之间的余弦相似度进行检索，并使用基于InfoNCE损失的对比学习进行微调，以拉近语义和数据分布均匹配的查询-函数对。
3.  **RCodingAgent**：一个面向R的LLM代理，将DARE模块集成到下游统计分析工作流中。代理接收自然语言查询后，首先调用DARE检索出既符合分析意图又满足数据兼容性约束的候选R函数及其元数据。然后将这些结构化信息通过上下文学习注入LLM，指导其进行工具调用和R代码生成，最终完成端到端的分析任务。

**创新点**：
*   **分布感知的检索**：与现有仅关注函数级语义的方法不同，DARE创新性地将数据分布特征作为关键信号融入嵌入表示，实现了语义与数据上下文的对齐。
*   **高质量、专注的R知识库（RPKB）**：通过严格的过滤流程构建，确保了检索库的统计知识密度和实用性。
*   **系统化的评估框架**：设计了基于16个代表性R统计分析任务的评估套件，在真实的、基于执行的数据上下文中系统评估LLM代理生成有效代码和输出结果的能力。

### Q4: 论文做了哪些实验？

论文实验主要包括两部分：检索模型评估和下游智能体任务评估。

在检索模型实验中，作者构建了包含245,730条合成查询的数据集，使用85%的数据训练，15%测试。模型基于all-MiniLM-L6-v2初始化，用AdamW优化器训练100个epoch，批量大小为256，学习率为1e-4。评估时，将提出的DARE模型与多个开源先进嵌入模型（如BAAI/bge-m3、intfloat/e5-large-v2等）进行对比。关键指标显示，DARE在NDCG@10上达到93.47%，比最优基线提升高达17%，同时在Recall@1、MRR@10等指标上均显著领先。效率方面，DARE的平均延迟为1.21 ms/query，吞吐量为825.62 QPS，体现了部署可行性。

在下游任务实验中，作者评估了集成DARE的RCodingAgent在16个统计分析任务上的表现，对比了无DARE和有DARE两种设置，并在六个代表性LLM（如deepseek-v3.2、gpt-5.2等）上测试鲁棒性。每个任务最多允许20次交互步骤。主要结果以成功率（SR）衡量：集成DARE后，所有LLM代理的下游任务成功率均获得显著提升，例如在特定任务中成功率提高超过20%，证明了DARE检索对提升LLM代理实际分析能力的有效性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向可从以下几个维度进一步探索：首先，提升LLM对R语言的原生熟练度是关键。当前大模型在R统计计算上的内在能力有限，主要因为预训练数据中缺乏高质量的R语料。未来可构建大规模、以R为中心的知识库（如教程、文档和可执行分析流程），以增强模型的内在统计推理和编程能力，而不仅仅依赖检索增强。其次，在工具学习与利用方面，当前方法通过JSON描述进行上下文增强，未能充分捕捉统计工具间的层次化和组合关系。未来可研究更结构化、自适应的策略，例如动态工具抽象、函数级推理图或基于记忆的选择机制，以更好地支持复杂工具的调用。此外，知识库的扩展与维护也至关重要。尽管当前知识库包含八千多个函数，但R生态中还有大量领域特定包和专用工具。开源知识库并鼓励社区驱动扩展，可建立更全面、持续演进的统计知识基础设施。最后，将RCodingAgent集成到专家混合（MoE）系统中是一个有前景的方向，使其作为R统计分析的专用专家，与其他负责互补任务的智能体协同工作，从而提升复杂端到端分析工作流的可扩展性和灵活性。这些方向不仅深化了检索与工具学习的结合，也拓宽了LLM智能体在专业领域的应用边界。

### Q6: 总结一下论文的主要内容

该论文旨在解决大语言模型（LLM）代理在自动化数据科学工作流时，难以有效利用R语言中严谨统计方法的问题。现有检索增强方法通常只关注函数级别的语义，而忽略了数据分布信息，导致检索结果不佳。

论文的核心贡献包括三点：首先，构建了一个精心整理的R包知识库（RPKB），涵盖8,191个高质量的CRAN包。其次，提出了一种轻量级即插即用的检索模型DARE，它将数据分布特征与函数元数据融合到嵌入表示中，从而显著提升了R包检索的相关性。最后，开发了一个面向R的LLM代理RCodingAgent，用于可靠的R代码生成，并设计了一套统计分析任务来系统评估代理在真实场景下的性能。

实验表明，DARE在包检索任务上NDCG@10达到93.47%，以更少的参数量大幅领先现有开源嵌入模型。将DARE集成到RCodingAgent中，有效提升了后续分析任务的表现。这项研究有助于缩小LLM自动化与成熟的R统计生态系统之间的差距。
