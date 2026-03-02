---
title: "FinBloom: Knowledge Grounding Large Language Model with Real-time Financial Data"
authors:
  - "Ankur Sinha"
  - "Chaitanya Agarwal"
  - "Pekka Malo"
date: "2025-02-04"
arxiv_id: "2502.18471"
arxiv_url: "https://arxiv.org/abs/2502.18471"
pdf_url: "https://arxiv.org/pdf/2502.18471v2"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "q-fin.ST"
tags:
  - "Agent 架构"
  - "工具使用"
  - "知识增强"
  - "领域应用"
  - "实时数据"
relevance_score: 7.5
---

# FinBloom: Knowledge Grounding Large Language Model with Real-time Financial Data

## 原始摘要

Large language models (LLMs) excel at generating human-like responses but often struggle with interactive tasks that require access to real-time information. This limitation poses challenges in finance, where models must access up-to-date information, such as recent news or price movements, to support decision-making. To address this, we introduce Financial Agent, a knowledge-grounding approach for LLMs to handle financial queries using real-time text and tabular data. Our contributions are threefold: First, we develop a Financial Context Dataset of over 50,000 financial queries paired with the required context. Second, we develop FinBloom 7B, a custom 7 billion parameter LLM, by fine-tuning Bloom 7B on 14 million financial news articles from Reuters and Deutsche Presse-Agentur (DPA), alongside a random sample of 25% from 12 million Securities and Exchange Commission (SEC) filings. Third, we fine-tune FinBloom 7B using the Financial Context Dataset to serve as a Financial Agent. This agent generates relevant financial context, enabling efficient real-time data retrieval to answer user queries. By reducing latency and eliminating the need for users to manually provide accurate data, our approach significantly enhances the capability of LLMs to handle dynamic financial tasks. Our proposed approach makes real-time financial decisions, algorithmic trading and other related tasks streamlined, and is valuable in contexts with high-velocity data flows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在处理需要实时信息的交互式任务时存在的局限性，特别是在金融领域。研究背景是，尽管LLM在自然语言生成、问答等任务上表现出色，但它们通常是基于静态的、历史的数据进行训练，无法获取和处理实时更新的信息。在金融决策、算法交易等场景中，用户需要依据最新的新闻、股价变动等动态数据来做出判断，而现有冻结参数的LLM无法满足这一需求。

现有方法的不足主要体现在两个方面：一是直接对LLM进行微调以适应实时数据成本高昂且不切实际，因为金融数据更新速度极快，频繁的再训练会导致模型始终滞后于市场；二是现有的一些知识增强方法（如某些专注于交易决策的研究）可能范围较窄，未能提供一个通用的、能够处理多样化金融查询的实时数据检索与整合框架。

因此，本文要解决的核心问题是：如何为LLM建立一个高效的知识增强框架，使其能够利用实时流动的文本和表格数据来准确回答金融领域的用户查询。具体而言，论文提出了一个名为“Financial Agent”的解决方案，通过构建一个包含实时数据模块和金融代理的架构，让代理自动理解查询、从数据模块中检索最新相关信息并构建上下文，从而为后续的大型LLM（如GPT）提供实时、准确的背景信息来生成最终答案。这避免了用户手动提供精确数据的麻烦，降低了延迟，显著提升了LLM处理动态金融任务的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为知识增强方法、金融领域应用及金融数据集三类。

在知识增强方法方面，相关工作包括：1）提示工程方法，如思维链（CoT）提示、元提示编程和AUTOPROMPT，它们通过设计提示词引导模型，但需要手动优化且受限于模型输入长度；2）参数高效微调方法，如P-Tuning、Prefix Tuning和QLoRA，它们通过调整少量参数使模型适应下游任务，但面对高频动态数据时更新成本高；3）检索增强生成（RAG）方法，如传统RAG模型、ATLAS和LLM-Augmenter，它们通过检索外部知识来增强模型，但在处理金融这类结构化、高时效性数据时，存在检索不精确、文本化转换失真和索引更新延迟等问题。本文提出的Financial Agent方法区别于传统RAG，它不依赖稠密向量检索，而是通过一个轻量级Agent预测并生成精确的结构化数据查询，直接从关系型数据库中获取实时数据，从而解决了传统方法在金融场景下的精度和延迟问题。

在金融领域应用方面，已有研究探索了LLM在情感分析、实体识别、关系抽取和问答等任务中的应用，但通常依赖于静态或特定任务的数据集。本文则专注于构建一个能处理实时、动态金融查询的智能体系统。

在金融数据集方面，已有SentiWordNet、Financial Phrase Bank、FINQA等多个针对情感分析、命名实体识别或复杂问答的标注数据集。本文的贡献在于创建了一个包含5万多个金融查询及其所需上下文的Financial Context Dataset，专门用于训练模型理解查询并获取实时数据的能力，与之前的数据集在目标和规模上有所不同。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FinBloom的金融智能体系统来解决LLMs在处理实时金融信息时的局限性。其核心方法是采用“知识增强”的架构，将大语言模型与实时数据检索模块相结合，形成一个端到端的问答系统。

整体框架包含三个关键模块：1）**金融智能体（Financial Agent）**：基于微调后的FinBloom 7B模型，负责解析用户自然语言查询，并生成结构化的数据请求。2）**数据模块（Data Module）**：接收结构化请求，从外部实时数据源（如新闻、股价、SEC文件）中检索所需信息。3）**上下文生成与答案合成**：智能体利用检索到的实时数据生成包含相关金融背景的答案。

核心创新点在于分阶段训练定制化的领域大模型。首先，**FinBloom 7B的预训练**：并非简单地在通用基座模型上进行指令微调，而是使用大规模、高质量的领域文本语料（包括1400万篇路透社和DPA的金融新闻，以及300万份SEC文件样本）对Bloom 7B进行持续预训练。这使模型深入掌握了金融术语、概念及上下文关联，克服了现有金融LLMs仅依赖有限规模、高度结构化数据导致的领域知识浅薄问题。

其次，**任务特定的指令微调**：在预训练得到的领域专家模型FinBloom 7B基础上，使用专门构建的**金融上下文数据集**（包含超过5万条金融查询及所需上下文配对）进行指令微调，将其转化为能胜任特定任务的“金融智能体”。该智能体的关键技术是学会将模糊的自然语言查询（如“苹果公司最近表现如何？”）自动分析并转化为包含明确公司实体、所需金融指标、相关新闻主题及日期范围的结构化数据请求函数，从而桥接了自然语言与数据模块之间的鸿沟。

该方法通过让LLM专注于其擅长的语言理解与生成，而将实时信息获取委托给专门的数据模块，实现了高效、低延迟的实时金融信息处理，无需用户手动提供精确数据，显著提升了LLMs在动态金融任务（如实时决策、算法交易）中的实用性。

### Q4: 论文做了哪些实验？

该论文的实验主要包括三个部分：模型构建、数据集创建和性能评估。

在实验设置上，研究者首先构建了一个金融上下文数据集，包含超过5万条金融查询及其所需背景信息。其次，他们开发了FinBloom 7B模型，该模型基于Bloom 7B，在1400万篇来自路透社和德新社的金融新闻文章，以及从1200万份美国证券交易委员会文件中随机抽取的25%样本上进行微调。最后，他们使用金融上下文数据集对FinBloom 7B进行进一步微调，使其成为能够生成结构化数据请求的金融智能体。

数据集和基准测试方面，论文使用了自行构建的Financial Context Dataset，并与多个现有金融大语言模型进行对比，包括FiMA、FinGPT、CFGPT和InvestLM等。

主要结果和关键指标显示，FinBloom 7B在生成相关金融上下文以支持实时数据检索方面表现优异。通过减少延迟并消除用户手动提供准确数据的需求，该方法显著提升了LLM处理动态金融任务的能力。具体而言，该智能体能够有效分析用户自然语言查询，智能识别所需的金融指标、相关指标和新闻，确定相关公司及数据时间范围，并以数据模块可解释的形式呈现这些要求。与现有金融LLM相比，FinBloom 7B在理解金融文本的细微差别和捕捉金融指标间复杂相互依赖关系方面表现更好，这得益于其在大规模高质量金融文本语料上的训练。

### Q5: 有什么可以进一步探索的点？

该论文在实时金融数据与LLM结合方面做出了有益尝试，但仍有多个方向值得深入探索。首先，模型主要依赖新闻和SEC文件等文本数据，未来可整合更多元的结构化数据源，如高频交易流、宏观经济指标和另类数据（如社交媒体情绪），以构建更全面的金融知识图谱。其次，FinBloom 7B基于Bloom微调，可探索更先进的架构（如MoE）或高效微调方法（如LoRA），在保持实时性的同时提升模型对复杂金融逻辑的推理能力。此外，当前系统侧重于信息检索与生成，未来可引入强化学习框架，使智能体能在模拟交易环境中进行决策优化，并加入风险控制和可解释性模块。最后，数据实时性虽被强调，但未深入讨论数据延迟与信噪比处理机制，这是实际金融应用中需解决的关键工程挑战。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在金融领域处理实时信息不足的问题，提出了FinBloom框架。核心贡献在于构建了一个包含超过5万条金融查询及对应上下文的Financial Context Dataset，并基于Bloom 7B模型，利用路透社和德新社的1400万篇金融新闻以及美国证券交易委员会文件的部分样本进行微调，开发了FinBloom 7B专用模型。进一步地，作者将该模型微调为Financial Agent，使其能够根据用户查询自动生成相关的金融上下文，从而高效检索实时数据以回答问题。该方法显著降低了延迟，免去了用户手动提供准确数据的负担，提升了LLMs在动态金融任务（如实时决策、算法交易）中的处理能力，对高速数据流环境下的应用具有重要价值。
