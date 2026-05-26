---
title: "Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG"
authors:
  - "Moshe Hazoom"
  - "Gal Patel"
  - "Alon Talmor"
  - "Tom Hope"
date: "2026-05-25"
arxiv_id: "2605.25641"
arxiv_url: "https://arxiv.org/abs/2605.25641"
pdf_url: "https://arxiv.org/pdf/2605.25641v1"
categories:
  - "cs.CL"
tags:
  - "Agentic RAG"
  - "知识库优化"
  - "事实校正"
  - "检索增强生成"
  - "B2B智能体"
  - "索引时优化"
  - "生产环境评估"
relevance_score: 9.0
---

# Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG

## 原始摘要

Agentic retrieval-augmented generation (RAG) systems in complex B2B (business-to-business) settings may often receive free-form response feedback. Rather than generic feedback signals such as style, preference, or overall response quality, we focus on actionable factual corrections. We identify these instances and convert them into compact knowledge-base entries, which we call factual nuggets. We introduce Iterative Nugget Optimization (INO), an index-time optimization method that uses the production agentic RAG as a test harness: it creates an initial nugget, probes it with the triggering query and paraphrases, reflects over failed retrieval and answer traces, and revises the nugget until it is discoverable. We evaluate INO with two production B2B knowledge-assistance agents across multiple companies that use our system: a product support agent that answers questions over company-specific knowledge bases, and a support ticket agent that assists support engineers. INO consistently improves results over baselines in terms of discoverability and usage of factual corrections, in automated and human evaluations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决B2B企业级AI知识助手在部署后，如何有效利用用户反馈中蕴含的可操作事实修正信息，以持续改进知识库和代理回答准确性的问题。具体而言，现有方法主要存在以下不足：第一，用户反馈多为模糊、主观或与单一对话相关的通用信号（如“无帮助”），缺乏针对具体事实错误的可重用修正；第二，传统的知识库更新方式（如简单记录原始反馈）会导致知识条目过于狭窄，无法被未来采用不同措辞的用户查询发现和利用；第三，现有提示或上下文优化方法会影响整个系统行为，无法针对单一事实修正进行可审计的局部调整。本文的核心问题是：如何从B2B代理RAG系统的用户反馈中自动提取并构建紧凑、自包含、可独立检索的事实修正条目，即“事实核”（factual nugget），并通过迭代优化使其在未来的相关查询中被轻易发现和正确使用，从而在不修改生产系统提示和上下文的前提下，实现持续、可审计的纠错与知识更新。

### Q2: 有哪些相关研究？

首先，在文档扩展方法方面，相关工作通过合成查询或相关文本来增强可检索单元。本文与之的区别在于，插入的是源自反馈的短事实片段（factual nugget），且采用逐片段优化的方式，通过在下游 Agentic RAG 系统中迭代执行查询并反思结果。

其次，在LLM增强的智能体记忆方面，现有方法将过往交互重写为自包含的记忆并添加元数据。本文的不同在于，起始于需过滤的自由文本反馈以提取可操作的事实修正，并将事实片段存储在企业知识库中，而非私有的 episodic 记忆。此外，本文还增加了一个下游优化阶段，逐一测试和修订每个片段直至其能被现有生产环境 Agentic RAG 系统发现并利用。

最后，在反馈驱动的RAG更新方面，PatchRAG研究学术基准上的合成反馈，未评估真实用户反馈，也未关注事实修正或优化反馈表征。STACKFEED则基于下游失败反馈编辑现有知识库文档。与之对比，本文采用来自部署的B2B知识助手的真实最终用户反馈，创建全新原子化事实片段而非编辑源知识，并针对被发现和使用进行优化。

### Q3: 论文如何解决这个问题？

论文提出了一种名为**迭代事实片段优化**的方法，旨在解决代理RAG系统中用户反馈的事实性修正信息在后续检索中无法被发现的问题。核心思想是将生产环境中的代理RAG系统作为测试工具，通过闭环迭代优化事实片段的可检索性。

**整体框架**是一个闭环优化循环。首先从用户针对特定查询 \( q_0 \) 的反馈中提取**初始事实片段** \( n \)，并对其进行初始扩展（Variant D），即附加原始查询的释义和4个LLM生成的合成查询作为检索锚点。然后进入最多 \( T=3 \) 轮的迭代优化循环：

1.  **索引与探测**：将候选片段 \( n^* \) 索引到客户知识库中，并构建一个**探测集**，包含 \( q_0 \) 及3-5个全新生成的、与锚点查询不重叠的释义查询。使用完整的代理RAG系统对这些探测查询进行检索和回答。
2.  **失败分析**：检查每个探测查询的检索结果，判断 \( n^* \) 是否被成功检索并引用。如果任何一次探测失败，则进入下一步。
3.  **重写优化**：一个**LLM反射器**接收失败的查询、检索到的竞争文档、生成的答案以及当前片段，然后重写片段的可索引表示（包括标题、正文措辞和检索锚点）。其目标是使修正信息更易被发现，例如添加缺失术语、消除角色或产品的歧义，或区分排名错误的文档，但**严格禁止添加新的事实性声明**。

优化后的新候选片段重新索引并进入下一轮迭代，直至所有探测查询均能成功检索到该片段。

**主要创新点**在于：1) 将事实修正的发现性问题转化为一个可端到端优化的索引时过程；2) 使用生产级RAG系统作为真实测试平台，而非人工评估；3) 通过LLM反射器进行有针对性的重写，仅优化片段的可发现性而不改变核心事实，实现了自动化的事实修正维护。

### Q4: 论文做了哪些实验？

论文在两个生产级B2B知识辅助系统上进行了实验：产品支持Agent和工单支持Agent。主要实验使用从真实负反馈事件中采集的100条可操作事实性知识颗粒（factual nuggets），这些样本均匀分布在7个客户的数据集上。对比方法包括：标准知识颗粒(A)、仅触发查询锚点(B)、合成锚点(C)、触发+合成锚点(D)以及本文提出的INO方法(E)。在410条保留查询（110条真实历史查询和300条LLM生成查询）上的评估显示，INO在检索率和引用率上均显著优于基线：真实查询上分别达到77.3%和68.1%（对比基线A的52.3%和41.3%），合成查询上达93.7%和86.1%。在工单Agent上测试160个样本，INO的检索率提升至78.2%（基线35.1%），引用率提升至70.4%（基线29.7%）。LLM作为评判者的评估表明，INO使答案符合修正要求的比例从52.2%提升至73.4%（McNemar检验p≈0.003），同时未检索率从40%降至13%。三个运行周期的标准差均控制在2.2以内，验证了方法稳定性。

### Q5: 有什么可以进一步探索的点？

首先，论文仅在单一混合检索架构上进行了验证，未来应探索在纯稠密、稀疏或延迟交互检索器上的表现，以验证方法的普适性。其次，评估仅限英语，尽管方法语言无关，但需在非英语场景中检验其鲁棒性。最后，重大依赖前沿LLM进行锚点生成、反思和判断，不同模型可能导致性能差异，未来可开展模型消融实验，或引入更轻量级、可控的组件以减少这种依赖。此外，可以考虑将INO扩展到多轮交互场景，用户反馈可能包含更加细微和复杂的修正；或者研究如何自动识别哪些反馈对应的修正值得被持久化为事实片段，以减少噪声。还可以探索使用更高效的索引策略或融合用户满意度信号来进一步优化片段的可发现性。

### Q6: 总结一下论文的主要内容

本论文研究了在复杂B2B场景下的智能体检索增强生成系统中，如何将可操作的事实纠正反馈转化为可检索、可用的知识条目（称为“事实核”）。核心问题是，现有系统处理自由形式反馈时，往往只关注风格或整体质量，而忽略了具体的事实修正。为此，论文提出了迭代核优化（INO）方法，一种索引时优化技术。它利用生产环境中的智能体RAG作为测试工具，为每个事实核创建初始版本，通过触发查询及其释义进行检索测试，根据失败的回溯和回答轨迹进行反思和修订，迭代直至该事实核能被可靠发现。在多个B2B客户部署的两种智能体（产品支持智能体和工单支持智能体）上进行的自动和人工评估表明，INO在事实修正的可发现性和使用率上显著优于基线方法。该方法离线运行，每次修正成本约0.31美元且耗时不到两分钟，不会增加查询延迟，已在生产中每周处理数百个事实核。这项工作的意义在于提供了一种实用、高效的机制，使RAG系统能够从用户反馈中持续学习并自我修正事实性错误。
