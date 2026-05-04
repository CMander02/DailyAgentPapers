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
pdf_url: "https://arxiv.org/pdf/2604.27906v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Schema-Grounded Memory"
  - "Memory Extraction"
  - "AI Agent"
  - "Knowledge Base"
relevance_score: 9.5
---

# From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction

## 原始摘要

Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later. This design is useful for thematic recall, but it is mismatched to the kinds of memory that agents need in production: exact facts, current state, updates and deletions, aggregation, relations, negative queries, and explicit unknowns. These operations require memory to behave less like search and more like a system of record.
  This paper argues that reliable external AI memory must be schema-grounded. Schemas define what must be remembered, what may be ignored, and which values must never be inferred. We present an iterative, schema-aware write path that decomposes memory ingestion into object detection, field detection, and field-value extraction, with validation gates, local retries, and stateful prompt control. The result shifts interpretation from the read path to the write path: reads become constrained queries over verified records rather than repeated inference over retrieved prose.
  We evaluate this design on structured extraction and end-to-end memory benchmarks. On the extraction benchmark, the judge-in-the-loop configuration reaches 90.42% object-level accuracy and 62.67% output accuracy, above all tested frontier structured-output baselines. On our end-to-end memory benchmark, xmemory reaches 97.10% F1, compared with 80.16%-87.24% across the third-party baselines. On the application-level task, xmemory reaches 95.2% accuracy, outperforming specialised memory systems, code-generated Markdown harnesses, and customer-facing frontier-model application harnesses. The results show that, for memory workloads requiring stable facts and stateful computation, architecture matters more than retrieval scale or model strength alone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有AI持久化记忆系统在处理生产环境中的精确事实、当前状态、更新删除、聚合查询、关系推理及否定查询等操作时可靠性不足的问题。当前的主流方法将记忆简化为检索问题：通过将历史交互存储为文本并嵌入向量，在需要时让模型检索相关上下文。这种设计虽适合主题回忆，但本质上是一种非结构化的“模糊回忆”机制，无法满足Agent对精确记录系统的要求——模型需要在多个片段中反复进行推理推断，导致事实漂移、信息不一致以及对“未知”状态无法明确表达。

现有方法的不足在于缺乏模式约束：没有明确定义哪些信息必须被精确记录、哪些可以忽略、哪些值绝不能由模型推断。这导致读路径承担了过多语义解释负担，而写路径只是简单存储原始文本。

本文核心解决方案是提出一种基于模式约束的迭代式、感知模式的写路径架构。它将记忆摄入过程分解为对象检测、字段检测和字段值提取三个步骤，并通过验证门控、本地重试和状态化提示控制确保提取可靠性。其核心洞见是：将语义解释从读路径转移到写路径，使读取变为对已验证记录的约束查询而非对检索文本的反复推理，从而将记忆系统从“检索相似文本”转变为“可靠记录系统”。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几类工作。**方法类**中，传统AI记忆系统多依赖非结构化文本检索（如LangChain Memory、MemGPT），将记忆简化为嵌入和检索过程。本文与之核心区别在于提出**模式引导（schema-grounded）** 方法，将记忆写入过程明确分解为对象检测、字段检测和值提取，并以验证门控和重试机制取代纯检索。**评测类**工作包括现有的结构化提取基准（如Schema-Guided Extraction）和端到端记忆基准（如MemoryBank、ChatGPT Memory），本文在这些基准上将准确率从80%-87%提升至97%F1。**应用类**相关研究包括专门化的记忆系统（如MemGPT、Neo4j知识图谱）和代码生成框架（如Code Interpreter），本文通过对比实验证明其方法在需要稳定事实和状态计算的应用任务上（95.2%准确率）优于这些系统。整体而言，本文强调**写入路径的架构设计**比检索规模和模型能力对可靠性记忆更重要。

### Q3: 论文如何解决这个问题？

该论文通过引入模式感知（Schema-Aware）的迭代提取框架来解决传统AI记忆系统依赖检索式召回、难以支持精确事实与状态管理的问题。核心方法是将记忆写入路径从简单的文本嵌入重构为可验证的结构化处理流程，将解释负担从读取路径转移到写入路径。

整体框架包含三个主要组件：首先通过**对象检测**识别需要记忆的实体类型（如用户、物品），然后进行**字段检测**确定需记录的属性集合，最后通过**字段-值提取**获得精确数值。该流程的关键创新在于三重验证机制：**验证门**（Validation Gates）确保每个提取结果符合预定义的模式约束，**本地重试**（Local Retries）在检测到异常时自动调用大语言模型重新提取，**状态化提示控制**（Stateful Prompt Control）维持整个提取过程的上下文连贯性。

架构设计上采用判官参与回路（Judge-in-the-Loop）模式，将提取结果与模式约束逐级比对，当存在字段缺失或值推断时触发回溯纠正。这种设计使记忆系统能够支持更新、删除、聚合、关系查询和显式否定等精确操作，将无结构文本转化为严格遵循Schema的验证记录。相比传统方法需要依赖模型在读取时反复解读原始文本，本方案通过结构化约束将存储内容转化为可查询的记录系统，在端到端记忆基准测试中达到97.10%的F1值，显著优于80.16%-87.24%的基线水平。

### Q4: 论文做了哪些实验？

论文在三个层次上进行了实验验证。首先，在结构化抽取基准测试中，使用合成的多实体多字段数据集，设置Judge-in-the-loop配置（含验证门控与本地重试），对比了GPT-4o等前沿结构化输出基线。结果显示：对象级准确率达到90.42%，输出准确率62.67%，均超过所有对比方法。

其次，在端到端记忆基准测试中，采用包含更新、删除、聚合、否定查询等九类操作的专用数据集，对比了Memoripy、Mem0等第三方记忆系统。xmemory的F1值高达97.10%，而基线系统仅达到80.16%-87.24%。

最后，在应用级任务中，使用模拟客户服务场景，测试事实引用、状态更新等操作。xmemory准确率达95.2%，超过了专有记忆系统、代码生成的Markdown方案以及前沿模型应用框架。实验充分说明：对于需要稳定事实和状态计算的记忆工作负载，架构设计比检索规模或模型能力更为关键。

### Q5: 有什么可以进一步探索的点？

论文将记忆管理重心放在写路径的schema约束上，但存在几个可探索的局限。首先，当前schema设计依赖人工预定义，在开放域场景下难以覆盖所有动态实体关系，未来可研究自动的schema演化机制，通过用户交互反馈或知识图谱补全动态调整字段约束。其次，验证门控机制仅在提取阶段进行局部重试，未利用写入后的一致性校验，可引入异步的跨记录冲突检测（如同属性值矛盾），结合时间戳版本控制实现增量修正。第三，实验主要评估事实性记忆的精确度，但缺乏对语义模糊查询（如“最近常提到的客户”）的鲁棒性测试，未来可设计带噪声指令的对抗性测试集。另外，当前面向单智能体设计，多智能体场景下不同消息来源的schema对齐与权限控制问题值得探索。最后，可考虑将提取阶段的判别式验证与小规模生成式修补结合，例如用轻量级模型快速定位字段错误，再由大模型按模板修正，平衡效率与准确性。

### Q6: 总结一下论文的主要内容

这篇论文针对现有AI记忆系统仅依赖检索功能（如文本嵌入和语义搜索）在精确事实、状态更新、聚合查询、关系维护等生产级需求上的不足，提出了一种基于模式（schema）的可靠外部记忆系统。问题定义在于，当前记忆设计本质上是“非结构化召回”，难以支持精确存储、修改、删除及负查询等操作。核心贡献是提出一种迭代的、模式感知的写入路径，通过目标检测、字段检测、字段-值提取三级分解，结合验证门控、本地重试和状态化提示控制，将解释负担从读取路径转移到写入路径，使读取成为对已验证记录的约束查询而非对检索文本的重复推理。主要结论表明，在结构化提取基准上，该系统的物体级准确率达90.42%，输出准确率62.67%；端到端记忆基准F1高达97.10%，远优于第三方基线（80.16%-87.24%）；应用级任务准确率95.2%，超越了专业记忆系统和前沿模型应用框架。这证明了在处理需要稳定事实和状态计算的记忆任务时，体系结构设计比检索规模或模型强度更为关键。
