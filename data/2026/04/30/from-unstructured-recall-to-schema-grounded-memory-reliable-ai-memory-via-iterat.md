---
title: "From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction"
authors:
  - "Alex Petrov"
  - "Alexander Gusak"
  - "Denis Mukha"
  - "Dima Korolev"
date: "2026-04-30"
arxiv_id: "2604.27906"
arxiv_url: "https://arxiv.org/abs/2604.27906"
pdf_url: "https://arxiv.org/pdf/2604.27906v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent记忆"
  - "结构化记忆"
  - "Schema提取"
  - "LLM Agent"
  - "可信记忆"
  - "迭代提取"
  - "评测基准"
relevance_score: 8.5
---

# From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction

## 原始摘要

Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later. This design is useful for thematic recall, but it is mismatched to the kinds of memory that agents need in production: exact facts, current state, updates and deletions, aggregation, relations, negative queries, and explicit unknowns. These operations require memory to behave less like search and more like a system of record.
  This paper argues that reliable external AI memory must be schema-grounded. Schemas define what must be remembered, what may be ignored, and which values must never be inferred. We present an iterative, schema-aware write path that decomposes memory ingestion into object detection, field detection, and field-value extraction, with validation gates, local retries, and stateful prompt control. The result shifts interpretation from the read path to the write path: reads become constrained queries over verified records rather than repeated inference over retrieved prose.
  We evaluate this design on structured extraction and end-to-end memory benchmarks. On the extraction benchmark, the judge-in-the-loop configuration reaches 90.42% object-level accuracy and 62.67% output accuracy, above all tested frontier structured-output baselines. On our end-to-end memory benchmark, xmemory reaches 97.10% F1, compared with 80.16%-87.24% across the third-party baselines. On the application-level task, xmemory reaches 95.2% accuracy, outperforming specialised memory systems, code-generated Markdown harnesses, and customer-facing frontier-model application harnesses. The results show that, for memory workloads requiring stable facts and stateful computation, architecture matters more than retrieval scale or model strength alone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI系统中外部记忆（external memory）在支持精确事实、状态跟踪、聚合、关系查询、否定查询等生产级工作负载时存在的根本性可靠性问题。

**研究背景与现有不足：** 当前的AI记忆系统大多采用非结构化检索范式（Unstructured Retrieval），即将历史交互存储为文本并嵌入，在查询时通过语义相似度检索相关片段。这种设计在主题回忆（thematic recall）方面表现良好，但在需要精确事实的记忆任务中（如“我们设置了多少超时时间？”、“当前状态是什么？”），存在三个关键缺陷：1）精度失败（Precision failure）：检索到的文本相关但不包含确切事实；2）遗漏失败（Omission failure）：低显著性细节在压缩或排序中被丢弃；3）替代失败（Substitution failure）：当证据缺失时，模型会推断出看似合理但实际错误的数值。此外，语义检索无法实现否定查询（如“哪些决定未被重新审视？”）或聚合操作，因为嵌入空间本质上是连续相似度度量，而非离散谓词求值器。传统改进手段如扩大检索规模、重排序、混合检索或长上下文注入，都只能缓解症状，不能从根本上改变“语义相似度不等于事实保证”的问题。

**核心问题：** 本文要解决的核心问题是：如何设计外部记忆的写路径（write path），使其从“基于未结构化文本的检索”转变为“基于模式（Schema）的可靠记录系统”，从而实现精确、完整、确定性的记忆召回，避免语义推断带来的记忆漂移和下游推理错误。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

**1. 方法类：结构化记忆与提取**
- **Schema-grounded memory systems**：本文提出的核心方法，通过定义模式（schema）来明确需要记忆的事实、可忽略的字段及不允许推断的值，采用迭代式、模式感知的写入路径（对象检测、字段检测、字段-值提取）来生成验证过的记录。这与传统方法不同，后者将记忆视为检索问题。
- **Unstructured memory systems**：将交互存储为文本、嵌入并在读取时检索的方法。论文指出这种设计在精确事实、状态更新、聚合和否定查询等操作上存在精度失败、遗漏失败和替代失败，因为它依赖隐式相关性而非显式事实。

**2. 应用类：AI记忆系统**
- **Third-party memory systems**：如论文在端到端记忆基准测试中对比的基线系统（F1得分80.16%-87.24%），包括专门记忆系统、代码生成的Markdown harness和面向用户的frontier-model应用harness。本文提出的xmemory在相同基准上达97.10% F1，展现出架构设计优于检索规模或模型强度。
- **Specialised memory systems**：针对具体应用（如客服、任务跟踪）的记忆方案，本文通过应用级任务（95.2%准确性）证明其通用架构能超越这些专门系统。

**3. 评测类：记忆能力基准**
- **结构化提取基准**：用于评估对象级准确率和输出准确率。本文的judge-in-the-loop配置达到90.42%对象级准确率和62.67%输出准确率，优于所有前沿结构化输出基线。
- **端到端记忆基准**：评估精确事实召回、状态一致性、缺失检测等能力。本文的xmemory在F1上明显优于第三方基线，说明现有方法在事实性记忆上的根本缺陷。

**关系与区别**：本文与现有研究的核心区别在于，它认为记忆问题本质上不是检索问题，而是记录系统问题。现有方法（如语义检索、reranking、长上下文填充）虽能改善覆盖率，但无法保证精确性、完整性和确定性。本文通过将解释从读取路径转移到写入路径（即提前验证和结构化存储），从根本上改变了记忆的语义，使读取变成对验证记录的受限查询，而非对检索文本的反复推断。

### Q3: 论文如何解决这个问题？

论文通过引入一种迭代的、模式感知的写入路径来解决不可靠记忆的问题。核心方法是将记忆摄入过程分解为三个顺序阶段：对象检测、字段检测和字段值提取。每个阶段都嵌入验证门，并在失败时进行本地重试，从而将单次复杂的结构化输出任务转化为一系列受控的、更窄的决策问题，显著提高了每一步的可靠性。

整体架构围绕一个“模式感知提示引擎”构建，该引擎根据提取状态动态生成提示，使提示逻辑从静态指令转变为状态化控制。架构创新性地将记忆上下文划分为三个范围：请求上下文（处理单次摄入的局部决策）、会话上下文（跨请求和分块边界组装部分对象）以及主记忆上下文（持久化、带版本和溯源记录的存储）。这使得信息流和最终决策点清晰分离，同时允许通过状态化提示在各阶段之间传递已验证的信息。

关键技术在于将“解释”从读取路径转移到写入路径。写入阶段执行严格的验证和提取，将非结构化文本转化为符合预设模式的事实记录。而读取路径则简化为对这些已验证记录的约束查询和计算，避免了每次读取时对原始文本的重复解释和推断。这种设计利用模式作为“记忆契约”，明确了必须记忆、可以忽略以及绝不可推断的事实，使得记忆缺失成为可检测的错误而非沉默的偏差。最终，这一写路径的复杂度换来了读路径的绝对正确性、稳定性和可审计性，特别适用于需要精确事实和状态计算的智能体工作负载。

### Q4: 论文做了哪些实验？

论文在结构化提取基准测试和端到端记忆基准测试上评估了所提出的迭代、模式感知写入路径（xmemory）。在提取基准测试中，使用了包含多字段模式的合成数据，对比了所有前沿的结构化输出基线方法，并设置了“法官环路”（judge-in-the-loop）配置。主要结果：对象级准确率达到90.42%，输出准确率达到62.67%，均优于所有对比的单次结构化输出基线。在端到端记忆基准测试中，对比了第三方记忆系统（准确率范围80.16%-87.24%），xmemory达到了97.10%的F1分数。此外，在应用级任务中，xmemory达到95.2%的准确率，优于专门的记忆系统、代码生成的Markdown框架以及面向客户的工程应用框架。实验还通过令牌消耗分析（假设读写比R=10）得出，文本记忆系统比xmemory多消耗约3.15倍的令牌。

### Q5: 有什么可以进一步探索的点？

进一步探索的点包括：当前系统在写入路径上依赖LLM进行对象、字段和值的抽取，虽然验证门和重试机制提高了准确性，但整体仍以LLM为核心，这可能导致高延迟和token消耗。未来可探索更轻量级的抽取模型，或结合符号规则与LLM的混合方法，以降低对LLM的依赖。此外，当前方案假设schema是静态预定义的，但实际应用中记忆需求会随时间变化，因此动态schema进化——如基于使用模式自动调整字段或约束——值得研究。另一个方向是处理高度复杂的嵌套对象或互相关联的多个记忆实体，当前的对象-字段-值分解在复杂场景中可能效率不足，可考虑引入图式记忆结构或层次化抽取。最后，当前评估集中于结构化抽取和端到端记忆基准，在开放域对话或长期任务中鲁棒性尚未验证，未来需要测试其对罕见、噪声或对抗性输入的适应能力，并探索如何将记忆错误（如字段遗漏）反馈到写入通路实现持续学习。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个以模式（Schema）为核心的可靠外部AI记忆系统。作者指出，现有基于非结构化文本检索的记忆方法在处理精确事实、状态追踪、聚合查询等生产级需求时存在根本性缺陷，因为嵌入搜索本质上是主题检索而非事实验证。为此，论文设计了一个迭代的、模式感知的写入流程，将记忆摄入分解为对象检测、字段检测和字段值提取三个受控阶段，并引入验证门和局部重试机制，将解读负担从读取路径转移到写入路径。在结构化提取基准上，该系统的目标级准确率达90.42%；在端到端记忆基准上，F1分数达97.10%，远超第三方基线系统。结论表明，对于需要稳定事实和状态计算的记忆工作负载，架构设计比检索规模或模型强度更为重要。
