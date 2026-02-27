---
title: "CiteLLM: An Agentic Platform for Trustworthy Scientific Reference Discovery"
authors:
  - "Mengze Hong"
  - "Di Jiang"
  - "Chen Jason Zhang"
  - "Zichang Guo"
  - "Yawen Li"
  - "Jun Chen"
  - "Shaobo Cui"
  - "Zhiyang Su"
date: "2026-02-26"
arxiv_id: "2602.23075"
arxiv_url: "https://arxiv.org/abs/2602.23075"
pdf_url: "https://arxiv.org/pdf/2602.23075v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agentic Platform"
  - "Tool Use"
  - "Trustworthy AI"
  - "Scientific Research"
  - "Information Retrieval"
  - "Human-Agent Interaction"
  - "Hallucination Mitigation"
relevance_score: 8.0
---

# CiteLLM: An Agentic Platform for Trustworthy Scientific Reference Discovery

## 原始摘要

Large language models (LLMs) have created new opportunities to enhance the efficiency of scholarly activities; however, challenges persist in the ethical deployment of AI assistance, including (1) the trustworthiness of AI-generated content, (2) preservation of academic integrity and intellectual property, and (3) protection of information privacy. In this work, we present CiteLLM, a specialized agentic platform designed to enable trustworthy reference discovery for grounding author-drafted claims and statements. The system introduces a novel interaction paradigm by embedding LLM utilities directly within the LaTeX editor environment, ensuring a seamless user experience and no data transmission outside the local system. To guarantee hallucination-free references, we employ dynamic discipline-aware routing to retrieve candidates exclusively from trusted web-based academic repositories, while leveraging LLMs solely for generating context-aware search queries, ranking candidates by relevance, and validating and explaining support through paragraph-level semantic matching and an integrated chatbot. Evaluation results demonstrate the superior performance of the proposed system in returning valid and highly usable references.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决学术写作中引用文献时面临的信任、隐私和效率问题。研究背景是，虽然大语言模型（LLM）能提升学术活动效率，但其在参考文献发现任务中的直接应用存在严重缺陷：一是LLM容易产生“幻觉”，生成虚假或不相关的文献引用，损害学术诚信；二是现有工具（如Google Scholar Labs）通常需要将未发表的稿件上传至第三方服务，存在泄露敏感研究内容的风险；三是传统的人工查找参考文献过程（反复搜索、阅读筛选）极其耗时。

现有方法的不足在于，它们未能系统性地同时解决上述三个核心挑战。要么过度依赖LLM生成内容而牺牲了可信度，要么为了隐私保护而牺牲了自动化便利，或者自动化方案缺乏对具体论述语境的深度理解。

因此，本文要解决的核心问题是：如何构建一个既可信赖（确保引用真实、相关）、又保护隐私（数据不离开本地环境）、且高效便捷的自动化参考文献发现系统。具体而言，论文提出了CiteLLM这一智能体平台，其核心创新在于将LLM的效用严格限定在生成搜索查询、排序和解释验证等任务上，而通过动态路由机制，直接从可信的在线学术数据库中检索文献候选，从而从根本上杜绝LLM编造参考文献的可能，并在本地化的LaTeX编辑环境中实现无缝、隐私安全的用户体验。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及方法类和应用类。在方法层面，相关工作包括基于LLM的学术写作辅助工具，如文献综述生成和文本润色系统，它们通常依赖LLM直接生成内容或引用，但存在幻觉风险和数据隐私问题。相比之下，CiteLLM通过动态路由机制，仅从可信学术仓库检索候选文献，并限制LLM仅用于生成查询、排序和验证，从而确保引用真实性。在应用层面，现有工具如Google Scholar Labs提供引用发现功能，但需上传文稿至云端，可能泄露未发表研究；而CiteLLM将LLM功能嵌入本地LaTeX编辑器，实现无数据外传的隐私保护工作流。此外，在评测层面，已有研究关注AI生成内容的可信度评估，但多集中于通用领域；本文则专门针对引用发现的准确性和可用性进行系统评估，验证其返回有效引用的性能优势。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CiteLLM的、内嵌于LaTeX编辑器的智能代理平台来解决科学引用发现中的可信度、学术诚信与隐私保护问题。其核心方法是**将大型语言模型（LLM）的效用严格限定在本地环境内，并设计了一个以可信学术知识库为唯一来源、LLM为智能“调度员”与“解释器”的混合架构**，从而在杜绝幻觉的同时提升引用发现的精准性与可用性。

**整体框架与主要模块**：
1.  **本地化嵌入架构**：系统直接集成在LaTeX编辑器（如Overleaf）中，形成一个自包含的工作空间。所有文稿内容、中间数据均在本地处理，绝不传输至外部服务器，从根本上保障了数据主权与隐私。
2.  **智能引用发现流水线**：当作者高亮文本中的某个主张（S）后，系统启动以下核心模块：
    *   **学科感知路由**：首先使用一个轻量级LLM分类器推断所选文本的学科属性。基于此，系统动态地将搜索路由至预定义的、可信的学术预印本仓库（如arXiv、bioRxiv、medRxiv）。采用主-次仓库策略确保跨学科主张的检索覆盖率，并通过结构化JSON输出提供可解释的决策依据。
    *   **语义驱动查询构建**：对用户选中的文本进行句子级分割，识别关键主张。系统利用LLM，结合全文摘要和上下文，以批处理方式生成包含领域术语和核心学术概念的关键词查询。此过程可由本地部署的小型LLM高效执行，进一步保护隐私。
    *   **多源检索与容错获取**：根据路由决策，使用构建的查询并发检索指定仓库。若无结果，则自动回退至备用仓库。结果按标题去重，并通过论文ID或DOI自动获取标准化的BibTeX条目，内置指数退避重试机制确保鲁棒性。
    *   **全文验证与语义匹配**：为确保引用真实有效，系统从检索结果中提取PDF链接（优先开放获取），并使用GROBID工具解析全文为结构化文本。随后，通过少量示例提示的LLM进行细粒度语义匹配，计算候选论文与主张的整体相关性分数，并排名。
    *   **结果呈现与集成**：向用户呈现结构化的候选引用列表，包含标题、链接、摘要以及匹配度最高的三个段落及其分数和匹配理由。用户可一键插入BibTeX条目和文内引用标记。此外，系统提供一个集成的、预填充了文稿上下文和引用元数据的LLM聊天机器人，用于对已插入的引用进行深入的、上下文感知的交互式探讨。

**关键技术**：
*   **LLM效用隔离与角色限定**：创新性地将LLM的角色严格限定为生成搜索查询、排序候选文献以及验证解释支持，而**不直接生成引用内容本身**。引用的来源被严格限制在可信的学术知识库中，从而根除了幻觉问题。
*   **上下文感知的批处理提示设计**：在查询构建阶段，将多个句子主张与全文概要上下文一并送入LLM进行批处理，既降低了延迟，又保持了句间连贯性，生成了更准确的查询。
*   **端到端的自动化与无缝集成**：实现了从用户意图识别（高亮文本）到精准文献检索、验证、解释，再到最终引用格式插入的完整自动化流程，并深度融入写作环境，极大简化了工作流。

**创新点**：
1.  **范式创新**：提出了“在创作点进行AI集成”的新范式，通过将辅助工具与编辑上下文在本地共置，实现了高效协助与绝对隐私保护的统一。
2.  **架构创新**：设计了基于学科路由的、LLM驱动查询与可信知识库检索相结合的混合检索架构，在利用LLM语义理解优势的同时，确保了引用来源的可靠性与可追溯性。
3.  **体验创新**：提供了包含结构化匹配证据和集成聊天机器人的深度解释功能，不仅返回引用，还帮助作者理解引用如何支持其主张，支持更精准的表述和迭代式文稿精炼。

### Q4: 论文做了哪些实验？

论文实验主要评估CiteLLM平台在生成可信参考文献方面的性能。实验设置上，从多学科公开研究论文中采样40个句子陈述，每个句子均附带人工标注的搜索查询和至少一个来自原文的真实参考文献。

数据集与基准测试方面，首先比较了三种查询构建方法：仅使用原始句子的基线、使用LLM从句子提取关键词的查询，以及结合关键词与稿件上下文的上下文感知查询。三名经验研究员独立从清晰度、特异性以及与人工标注查询的一致性三个维度，按5点李克特量表评分。结果显示，上下文感知方法在所有维度上均优于基线。

对比方法包括：（1）使用原始句子作为查询的Google Scholar搜索；（2）具备网络访问能力的ChatGPT，被要求生成五个与句子及上下文匹配的真实相关参考文献。性能通过三个指标衡量：有效性（检索到的参考文献真实且可公开访问的比例）、精确度（语义相关且具支持性的参考文献比例）和可用性（系统返回至少一个直接可用参考文献的案例比例）。精确度和可用性通过人类专家检查和GPT-5作为评判进行验证。

主要结果：所提系统在验证集上实现了100%的有效性，并表现出高精确度和可用性。关键数据指标显示，ChatGPT方法在有效参考文献中的精确度较高，但常产生无效或虚构参考文献；而GPT-5的评分普遍高于人类评估者，揭示了评估标准的不一致，凸显了在研究中需谨慎使用全自主LLM代理。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其系统主要针对LaTeX环境，可能限制了在更广泛写作平台（如Word或在线编辑器）中的应用。此外，依赖特定学术数据库进行检索，可能无法覆盖所有学科或新兴领域的文献资源。未来研究可探索跨平台集成方案，以支持多样化的写作工具。在技术层面，可进一步优化查询生成与排序算法，结合多模态信息（如图表数据）提升检索精度。从伦理角度，可研究动态版权协商机制，在引用时自动处理知识产权许可。另外，系统目前侧重于参考文献发现，未来可扩展至协助论文结构规划、实验设计论证等更广泛的学术写作环节，形成端到端的智能辅助流程。

### Q6: 总结一下论文的主要内容

CiteLLM是一个面向学术写作的智能代理平台，旨在解决AI辅助科研中的可信度、学术诚信与隐私保护问题。其核心贡献在于提出了一种无幻觉、隐私安全的参考文献发现方法，通过将LLM功能直接嵌入LaTeX编辑器实现本地化操作，避免数据外泄。方法上，系统采用动态学科感知路由，仅从可信学术数据库中检索候选文献，并利用LLM生成上下文感知的搜索查询、对结果进行相关性排序，以及通过段落级语义匹配和集成聊天机器人验证与解释文献支持。主要结论显示，CiteLLM在返回有效且高可用性参考文献方面表现优异，为负责任地整合AI到学术工作流提供了范例，既提升了研究效率，又保障了学术完整性。未来工作将优化用户体验并降低延迟与成本。
