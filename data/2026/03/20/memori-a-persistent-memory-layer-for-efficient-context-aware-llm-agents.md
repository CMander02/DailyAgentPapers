---
title: "Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents"
authors:
  - "Luiz C. Borro"
  - "Luiz A. B. Macarini"
  - "Gordon Tindall"
  - "Michael Montero"
  - "Adam B. Struck"
date: "2026-03-20"
arxiv_id: "2603.19935"
arxiv_url: "https://arxiv.org/abs/2603.19935"
pdf_url: "https://arxiv.org/pdf/2603.19935v1"
categories:
  - "cs.LG"
tags:
  - "Agent Memory"
  - "Persistent Memory"
  - "Context Management"
  - "Semantic Representation"
  - "Retrieval-Augmented Generation"
  - "Multi-Session Interaction"
  - "Efficiency Optimization"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents

## 原始摘要

As large language models (LLMs) evolve into autonomous agents, persistent memory at the API layer is essential for enabling context-aware behavior across LLMs and multi-session interactions. Existing approaches force vendor lock-in and rely on injecting large volumes of raw conversation into prompts, leading to high token costs and degraded performance.
  We introduce Memori, an LLM-agnostic persistent memory layer that treats memory as a data structuring problem. Its Advanced Augmentation pipeline converts unstructured dialogue into compact semantic triples and conversation summaries, enabling precise retrieval and coherent reasoning.
  Evaluated on the LoCoMo benchmark, Memori achieves 81.95% accuracy, outperforming existing memory systems while using only 1,294 tokens per query (~5% of full context). This results in substantial cost reductions, including 67% fewer tokens than competing approaches and over 20x savings compared to full-context methods.
  These results show that effective memory in LLM agents depends on structured representations instead of larger context windows, enabling scalable and cost-efficient deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主智能体（Agent）在长期、多轮次交互中，如何高效、低成本地实现持久记忆（Persistent Memory）并保持上下文感知能力的问题。

研究背景是，随着LLM发展为具备推理、规划和工具使用能力的智能体，记忆成为其持续学习和适应环境的关键支柱。然而，LLM的参数在部署时无法实时更新，因此记忆必须依赖外部系统设计。当前，个性化助手、推荐系统等应用都迫切需要智能体能够跨会话保留和利用历史信息。

现有方法主要存在两大不足：一是导致供应商锁定（vendor lock-in），缺乏模型无关的解决方案；二是简单地将大量原始对话历史注入提示（prompt）中，这会导致上下文窗口急剧膨胀，带来高昂的令牌（token）成本，并引发性能退化，如模型可能忽略关键信息、输出不一致，出现所谓的“上下文腐化”（context rot）问题。

因此，本文要解决的核心问题不是简单的存储问题，而是一个**数据结构化问题**。论文的核心是设计一个与LLM无关的持久记忆层，其关键在于如何将嘈杂、非结构化的对话数据，转化为一种既高效可检索、又能有效支持下游推理的紧凑结构化表示，从而在保证智能体高性能的同时，大幅降低计算成本与令牌消耗。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，现有工作多通过将大量原始对话历史直接注入提示（prompt）来提供上下文，这导致了高昂的令牌成本和性能下降。一些方法还与特定LLM供应商深度绑定，存在锁定风险。Memori与这些工作的核心区别在于，它将记忆视为一个数据结构化问题，而非简单的存储问题。它通过其“高级增强”流水线，将非结构化对话转化为紧凑的语义三元组和对话摘要，实现了精确检索和连贯推理，从而在根本上区别于依赖扩大上下文窗口的现有方法。

在应用类研究中，许多个性化助手、推荐系统和社交模拟应用都强调了跨会话持久记忆的必要性。Memori作为一个与LLM无关的持久记忆层，其设计目标正是为了支持这类需要长期、跨模型上下文感知行为的智能体应用，提供了更通用和高效的底层支持。

在评测类研究方面，本文使用LoCoMo基准进行评估。该基准专注于评估长期对话记忆与推理能力，为比较不同记忆系统提供了标准。Memori在该基准上的优异表现（81.95%准确率）直接证明了其结构化记忆方法相对于传统全上下文或简单检索方法的优势。

### Q3: 论文如何解决这个问题？

论文通过设计一个解耦的持久化内存层Memori来解决LLM智能体在多轮对话中因注入大量原始对话导致的token成本高和性能下降问题。其核心方法是采用“高级增强”流水线，将非结构化对话转化为结构化的语义三元组和对话摘要，从而实现精确检索和连贯推理。

整体框架上，Memori作为一个独立的内存层，部署在应用逻辑与底层LLM之间，通过轻量级SDK包装现有LLM客户端来拦截请求和管理内存。系统主要包含两个关键模块：一是语义提取与三元组生成模块，它从对话中主动扫描具体事实、用户偏好和约束等，将其解构为原子化的语义三元组（主体-谓词-客体），每个三元组都链接到其出现的具体对话片段，这既构建了低噪声、高信号的知识索引以提升向量检索精度，也起到了数据压缩的作用。二是对话摘要模块，它为特定对话线程生成简洁的高层概述，捕捉用户的整体意图、对话的时序进展和任务的隐含上下文，以补充三元组所缺失的叙事背景。

创新点在于其双层次、互联的内存资产设计。三元组提供精确、高效的事实召回，而对话摘要提供理解时序变化和执行复杂推理所需的连贯叙事流。通过将原子三元组直接链接到其源对话的摘要，系统确保了细粒度事实始终不脱离其宏观上下文。这种结构化表示方法替代了传统上直接嵌入和检索原始对话块的做法，在评测中仅需平均每查询约1294个token（约完整上下文的5%），就在保持高准确率的同时大幅降低了成本。

### Q4: 论文做了哪些实验？

论文在LoCoMo基准测试上进行了实验，以评估Memori高级增强流水线生成的内存资产的质量和准确性。实验设置方面，使用LoCoMo数据集，该数据集专注于评估智能体在跨多轮会话的长对话中跟踪、保留和综合信息的能力。Memori将对话处理为语义三元组和会话摘要，并使用Gemma-300模型进行嵌入，利用FAISS进行索引和混合检索（余弦相似度与BM25结合）。回答生成使用GPT-4.1-mini，并采用LLM-as-a-Judge方法（同样使用GPT-4.1-mini）进行评估。

对比方法包括现有的内存系统Zep、LangMem、Mem0以及作为性能上限的Full-Context方法。主要结果如下：Memori在LoCoMo基准上的整体准确率达到81.95%，优于Zep（79.09%）、LangMem（78.05%）和Mem0（62.47%）。在具体推理类别上，Memori在单跳推理（87.87%）和多跳推理（72.70%）上表现强劲，在时序推理（80.37%）上稍逊于LangMem和Zep，在开放域推理（63.54%）上仍有挑战。

关键数据指标方面，Memori在保持高准确率的同时，显著降低了token消耗。其每次查询平均仅向上下文添加1,294个token，仅为完整上下文（26,031 token）的4.97%。与Zep（3,911 token）相比，token使用量减少约67%；与Full-Context方法相比，成本节省超过20倍。这验证了通过结构化表示而非扩大上下文窗口来实现高效、低成本LLM智能体内存的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于特定基准（LoCoMo），可能未充分覆盖更复杂、多轮或领域特定的对话场景。此外，其语义三元组和摘要的生成仍依赖现有LLM，可能引入错误或偏差，且结构化表示的设计可能无法完全捕捉对话中的隐含信息和情感细微差别。

未来研究方向可包括：1）扩展评估至更动态、开放域的环境，以测试系统的泛化能力；2）探索自适应记忆压缩机制，根据对话复杂度动态调整表示粒度；3）结合多模态记忆（如图像、音频）以支持更丰富的上下文感知。改进思路上，可引入增量学习机制，让记忆结构随交互持续优化，或集成外部知识库以增强事实一致性。此外，研究记忆的“遗忘”策略可能有助于提升长期效率，避免信息过载。

### Q6: 总结一下论文的主要内容

本文针对LLM智能体在多轮交互中因缺乏持久记忆而导致上下文信息丢失、成本高昂的问题，提出了一种独立于具体LLM的持久记忆层解决方案Memori。其核心贡献在于将记忆视为数据结构问题，通过创新的高级增强管道，将非结构化的对话内容转化为紧凑的语义三元组和对话摘要，从而实现精准的记忆检索和连贯的推理。在LoCoMo基准测试中，Memori以81.95%的准确率超越了现有记忆系统，且每次查询仅需约1294个令牌（约为完整上下文的5%），显著降低了67%的令牌消耗，相比完整上下文方法节省超过20倍成本。研究结论表明，高效LLM智能体记忆的关键在于结构化的记忆表征，而非更大的上下文窗口，这为可扩展且经济高效的智能体部署提供了有效路径。
