---
title: "MemRefine: LLM-Guided Compression for Long-Term Agent Memory"
authors:
  - "Minjae Kim"
  - "Jinheon Baek"
  - "Soyeong Jeong"
  - "Sung Ju Hwang"
date: "2026-06-11"
arxiv_id: "2606.13177"
arxiv_url: "https://arxiv.org/abs/2606.13177"
pdf_url: "https://arxiv.org/pdf/2606.13177v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent Memory Management"
  - "Long-term Memory Compression"
  - "Storage-Budgeted Memory"
  - "LLM-Guided Compression"
  - "Memory Retrieval"
relevance_score: 8.5
---

# MemRefine: LLM-Guided Compression for Long-Term Agent Memory

## 原始摘要

Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks. However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence. Furthermore, this is especially limiting on resource-constrained platforms with hard memory budgets, motivating us to formulate storage-budgeted memory management, the task of keeping an already constructed memory store within a fixed budget while preserving information useful for future interactions. To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）代理在长期交互过程中面临的记忆存储效率问题。随着代理不断积累对话历史，其持久化记忆存储会无限制增长，充斥大量冗余条目，这不仅增加了存储成本（尤其在资源受限的设备上），还会因检索到低价值或重复内容而降低性能。现有方法如会话摘要、提示压缩或图结构剪枝，均未能针对已构建好的记忆存储进行预算约束下的压缩：摘要仅在记忆生成前处理原始文本，压缩仅在推理时作用于检索上下文，而图剪枝依赖无法捕捉事实冗余性的中心性指标。因此，论文引入了一个新任务——“存储预算约束下的记忆管理”（storage-budgeted memory management），要求在固定预算内压缩已构建的记忆存储，同时保留对未来交互有用的信息。核心挑战在于：表面相似性无法准确衡量条目的事实价值——两个文本相似的记忆可能包含冗余、互补或完全不同的事实。为此，论文提出MemRefine框架，利用相似性候选配对，但将删除、合并或保留的决策交由LLM判断器基于事实内容做出，通过迭代压缩直至满足预算，从而在保持下游任务性能的同时实现紧凑存储。

### Q2: 有哪些相关研究？

在相关工作中，本文首先回顾了**长时记忆系统**，包括用户级记忆库、显式读写模块、虚拟上下文管理、结构化笔记图和通用代理记忆层等，以及评估长时记忆召回能力的基准。现有工作主要关注如何扩展记忆（即添加和检索新信息），而忽略了在存储预算下对已构建记忆库进行压缩的逆问题。本文的创新在于将事后存储缩减作为独立任务，压缩现有记忆库以满足预算，同时保持底层记忆框架不变。

其次，论文讨论了**记忆与上下文压缩**，涉及会话语义级摘要（如递归摘要）、推理时上下文压缩（如RECOMP、LLMLingua）和基于图结构的离线缩减。这些方法要么在记忆构建前进行摘要，要么压缩推理提示而非记忆库本身，要么依赖对内容不敏感的标准或与构建管线耦合。本文与之区别在于，直接以固定存储预算为目标，通过LLM对语义相似条目进行判别（如删除冗余、合并互补、保留独立），且与底层记忆构建和检索管线解耦。

### Q3: 论文如何解决这个问题？

MemRefine 提出了一种 LLM 引导的离线内存压缩框架，用于解决长期交互中记忆存储无限增长、冗余膨胀导致性能下降的问题。其核心方法是将存储预算内存管理形式化为一个预算约束下的最大-最小优化问题：在满足固定存储预算前提下，最大化最坏情况下的下游任务效用。由于直接优化不可行，MemRefine 通过一个实用的两阶段过程来近似：

1. **候选对选择**：利用余弦相似度作为提议机制（而非决策依据），每次迭代选出最相似且尚未评估的一对记忆条目。这一步骤高效地将冗余可能性高的对筛选出来，供后续深入分析。

2. **LLM 引导的判定与操作**：将一个 LLM 作为“法官”，基于条目的**事实内容**（而非表面相似性）对选出的候选对做出三类判定之一：**删除**（若内容被另一条完全覆盖）、**合并**（若内容互补）、或**保留**（若事实独立）。判定后执行相应操作：删除目标条目，或由另一 LLM 依据指令合成合并后的新条目（并更新其嵌入与链接）。被判决为“保留”的条目对被缓存，避免重复评估。

**创新点**在于：将压缩从独立评分问题转化为**关系性判断问题**，通过成对比较捕捉条目之间的冗余、互补或独立关系，从而避免误删关键事实。整个框架是查询无关的离线模块，在维护阶段运行，不增加在线检索开销，且与多种记忆框架兼容。算法迭代直到满足预算或所有相似对均被评估过（即无法进一步无损压缩）为止。

### Q4: 论文做了哪些实验？

论文在多个长期对话记忆基准上评估了MemRefine的压缩性能。主要使用LoCoMo数据集（包含10个样本、1986个问题，覆盖单跳事实、多跳推理、时间推理、开放性和反事实五类问题），并构造了3倍和10倍长度的扩展版本以测试更冗余的历史。另外在LongMemEval_S上使用60个问题（每类10个）进行验证。实验采用两个代表性记忆框架：A-MEM图结构（结构化笔记图）和Mem0（管道处理记忆）。比较的基准是未压缩的原始记忆，以及两种基于规则的消融基线（RuleSim：固定嵌入相似度阈值；RulePR：PageRank图中心性）。压缩预算设置为原始存储的70%、60%、50%、40%、30%。主要结果如表所示：在LoCoMo上，A-MEM图在预算50%时F1=0.3902（原始0.4013），EM=0.1628（原始0.1712）；Mem0在相近压缩比下性能下降更小。在3x和10x扩展数据集上，压缩依然平滑保持性能。类别分析显示，单跳和时间问题在压缩后改善，开放性和反事实问题更敏感。与规则基线对比，在宽松预算下方法相当，但在30%紧缩预算时MemRefine显著优于RuleSim和RulePR（F1高出约0.05-0.08）。使用不同压缩模型（GPT-5-mini vs Qwen3-8B）在中等预算下表现相近，紧缩预算下更强的LLM更有优势。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于MemRefine仅作为后处理模块，未融入记忆生成过程，且仅在两种记忆框架和长对话基准上验证，缺乏对多智能体、工具使用等复杂场景的评估。未来可探索将压缩机制嵌入记忆构建阶段，实现边生成边压缩，避免冗余累积。此外，当前LLM judge依赖事实内容决策，但高频调用可能成本高昂，可研究轻量级近似模型或主动学习策略来替代部分判断。针对资源受限平台，可进一步优化迭代压缩算法，确保固定预算下的实时性。长期真实日志的部署测试及跨框架泛化性也是重要方向，例如结合记忆图结构动态调整合并策略，或在压缩时优先保留与未来任务相关的潜在线索。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为 MemRefine 的 LLM 引导的存储预算内存管理框架，用于解决长期交互中智能体内存无限增长、冗余信息充斥导致存储成本升高和检索性能下降的问题。其核心贡献是，在固定预算约束下，通过相似度筛选候选对，但将由 LLM 作为判断依据，基于事实内容决定删除、合并或保留，迭代压缩已构建的内存存储。实验表明，在多种内存框架和基准测试中，MemRefine 能一致地达到目标预算并保持下游性能，尤其在严格预算下显著优于基于规则的基线。主要结论是，后构建压缩是实用的维护层，且压缩与构建应联合考虑，而内存表示方式会影响可安全移除的内容量。
