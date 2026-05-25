---
title: "Adaptive Mass-Segmented KV Compression for Long-Context Reasoning"
authors:
  - "Junzhe Yang"
  - "Xiaoyu Shen"
date: "2026-05-22"
arxiv_id: "2605.23200"
arxiv_url: "https://arxiv.org/abs/2605.23200"
pdf_url: "https://arxiv.org/pdf/2605.23200v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "KV Cache Compression"
  - "Long-Context Reasoning"
  - "LLM Inference"
  - "Attention Mechanism"
  - "Memory Management"
relevance_score: 8.5
---

# Adaptive Mass-Segmented KV Compression for Long-Context Reasoning

## 原始摘要

The linear growth of the Key-Value (KV) cache is a critical bottleneck in long-form LLM inference. Existing KV compression methods mitigate this by evicting tokens based on importance scores. However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence. To address this, we propose Adaptive Mass-Segmented (AMS) KV Compression, a framework that shifts the paradigm from token-level competition to region-aware quota allocation. AMS adaptively partitions the KV cache based on the spatial distribution of attention mass, ensuring structurally vital reasoning segments receive guaranteed memory quotas. To ensure stability during iterative decoding, an EMA-based smoothing mechanism is incorporated to prevent jitter in segment boundaries. Crucially, AMS is a universal plug-and-play layer that is orthogonal to existing scorers. It can be seamlessly integrated into representative methods such as TOVA, Expected Attention, KeyDiff, R-KV and TriAttention. AMS is also system-compatible with modern paged-KV serving frameworks such as vLLM, supporting efficient gather-and-compact KV execution without introducing additional steady-state attention overhead. Extensive experiments across a diverse suite of tasks, including mathematical reasoning (MATH500, AIME, GSM8K), code completion, open-domain QA, and sparse retrieval, demonstrate that AMS consistently mitigates structural fragmentation and boosts model performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长上下文推理中 KV 缓存压缩导致的“区域擦除”（Region Wipe-out）问题。研究背景是，大语言模型在长链推理中，KV 缓存会随生成线性增长，成为推理时延的主要瓶颈。现有方法通常采用基于重要性分数的 Top-k 全局选择策略来压缩缓存。然而，本文指出这种在 token 层面进行全局竞争的方式存在关键不足：它会天然地倾向于保留少数“高注意力”的 token，而那些分散但逻辑上至关重要的推理步骤（如中间推理链条）则容易被整体丢弃，造成“区域擦除”。这会导致模型出现问题漂移、过早推翻结论或重复循环等逻辑断裂现象。虽然已有一些基于块或段的压缩方法尝试缓解此问题，但其划分结构固定，无法适应推理过程中注意力分布的动态变化。因此，本文的核心问题是如何在压缩时避免破坏推理轨迹的逻辑连贯性，并提出了一种名为自适应质量分段（AMS）KV 压缩框架。该框架将范式从 token 层面的竞争转变为区域感知的配额分配，通过自适应分段和基于指数移动平均的稳定机制，确保关键推理区域获得保留配额，从而在不修改底层评分器的情况下，提升极端压缩下的推理质量。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

1. **解码时KV驱逐与免训练评分方法**：包括TOVA、KeyDiff、SnapKV、Expected Attention、TriAttention、R-KV和RPC等。这些方法通过注意力、重构、几何或推理感知代理对token评分，但通常采用全局或每头top-k选择，缺乏对连续时空区域的保护，在严格预算和重复压缩下脆弱。本文提出的AMS框架是评分器无关的即插即用层，可无缝集成到这些方法中。

2. **自适应预算与结构感知压缩方法**：包括PyramidKV、OmniKV、LaCache、AdaKV、DuoAttention、HeadKV、RazorAttention等非均匀分配层或头预算的方法，以及ChunkKV、SABlock、ClusterKV、ProtoKV、TreeKV、HeteroCache等分块或聚类方法。这些方法改进了跨层、头或粗粒度缓存单元的分配，但未明确为每头内的自适应时间区域分配配额。AMS则通过注意力导出的自适应分段，在token级评分前分配显式的区域配额。

3. **稳定性与系统方法**：如ReST-KV、G-KV等历史感知评分方法，以及LongFlow、Lethe、ThinKV等长输出推理系统。AMS通过EMA平滑机制使配额分配历史感知，保持评分器不变，并且与vLLM等分页KV服务框架兼容，是一种正交的、评分器无关的头内时间配额分配方法。

### Q3: 论文如何解决这个问题？

该论文提出了自适应质量分段键值压缩方法，通过将全局Top-k竞争范式转变为区域感知配额分配来解决逻辑结构碎片化问题。核心创新在于构建了基于注意力质量质量的宏观分割机制，具体包含三个关键阶段：

1. **自适应分段**：首先基于近期滑动窗口注意力计算头维度的质量分布向量，通过累计质量阈值法沿序列动态划分段落。高注意力密度区域被切分为更细粒度段落（如推理关键区块），低密度区域则合并为较长段落，并通过最小/最大长度约束（$L_{\min}, L_{\max}$）进行微调。

2. **分段配额分配**：每个段落先获得最小保留配额$q_{\min}$保证结构性存续，剩余预算按段落质量比例分配，并强制保留序列起始的注意力汇点与最近后缀令牌。这种"分段预算-局部选择"机制确保每个历史片段至少保留最小表征，避免连续推理块被整体擦除。

3. **时间稳定机制**：引入指数移动平均（EMA）信用向量跨压缩事件平滑质量信号，通过混合系数$\beta$平衡当前质量与历史信用，抑制因注意力波动导致的段落边界突变，提升迭代解码的稳定性。

该方法可直接嵌入TOVA、预期注意力等现有评分器作为即插即用层，保持后端评分函数不变，仅修改选择阶段。系统实现兼容vLLM等分页KV服务框架，通过收集-压缩操作实现高效执行。实验证明该方法在数学推理、代码补全等任务中持续缓解结构碎片化问题。

### Q4: 论文做了哪些实验？

该论文围绕提出的AMS（自适应质量分段）KV压缩框架进行了一系列实验。实验设置上，主要采用解码时KV压缩方式，在数学推理（MATH500、AIME24、AIME25、GSM8K）、代码补全、开放域问答（TriviaQA）、长文本基准（LongBench）和稀疏检索（NIAH）等多样化任务上进行评估。主骨干模型为DeepSeek-R1-Distill-Qwen-7B，并在32B变体和OpenThinker3-7B上测试可扩展性与跨骨干泛化性。对比方法包括StreamingLLM、TOVA、KeyDiff、ChunkKV-Expected、PyramidKV、AdaKV-ExpE2、R-KV、RPC和TriAttention等无训练压缩方法。在核心数学推理任务上，AMS显著提升性能：在MATH500中，AMS-TOVA在缓存预算T_keep=256/512/1024下，相比TOVA分别绝对提升7.2%、3.8%、4.6%；AMS-Expected相比AdaKV-ExpE2在该预算下分别提升16.0%、7.4%、0.8%。在极端预算256下，AMS-Expected在MATH500上达到48.6%，远超TOVA的29.2%。在GSM8K上，AMS-Expected在T_keep=64时达56.7%，优于TOVA（48.9%）。跨骨干和跨任务结果同样验证了AMS的通用性与有效性，如AMS-Expected在代码补全上甚至超过无压缩的Full KV。消融实验表明，移除质量加权配额或EMA平滑机制会显著降低性能。系统性能评估显示AMS具有较低内存占用和更快解码时间。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于其基于注意力质量分布的配额分配策略可能过度依赖注意力模式的稳定性，在注意力分布极度稀疏或噪声较大的场景下（如长文本中无关信息密集的区域），EMA平滑机制可能无法完全避免错误分段。未来可探索的方向包括：1）引入动态分段阈值自适应机制，根据任务类型或模型层数自动调整分段粒度；2）结合因果注意力掩码的先验知识优化配额分配，例如对近期上下文分配更高配额；3）将分段策略与早期退出（Early Exit）技术结合，在中间层跳过注意力计算以降低开销。此外，当前方法仅优化KV缓存保留策略，未来可探索与稀疏注意力计算（如稀疏Transformer）的深度融合，从计算和存储两个维度联合优化长上下文推理效率。

### Q6: 总结一下论文的主要内容

长上下文大语言模型推理中，键值(KV)缓存线性增长是关键瓶颈。现有压缩方法基于重要性分数驱逐令牌，但其全局Top-k选择机制会引发“区域清除”问题，即连续推理块被严重驱逐，破坏逻辑连贯性。为此，本文提出自适应质量分段(AMS)KV压缩框架，将范式从令牌级竞争转变为区域感知配额分配。AMS根据注意力质量的空间分布自适应划分KV缓存，确保结构关键的推理段获得内存保障。为在迭代解码中保持稳定，引入了基于指数移动平均的平滑机制，防止段边界抖动。AMS作为通用即插即用层，可无缝集成TOVA、Expected Attention、KeyDiff、R-KV和TriAttention等现有方法，并兼容vLLM等现代分页KV服务框架，支持高效聚集压缩KV执行而不增加稳态注意力开销。在数学推理、代码补全、开放域问答和稀疏检索等任务上的广泛实验表明，AMS能有效缓解结构碎片化并提升模型性能。
