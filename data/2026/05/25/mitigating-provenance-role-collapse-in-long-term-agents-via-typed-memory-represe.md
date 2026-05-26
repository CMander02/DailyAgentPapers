---
title: "Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation"
authors:
  - "Zhengda Jin"
  - "Bingbing Wang"
  - "Jing Li"
  - "Ruifeng Xu"
  - "Min Zhang"
date: "2026-05-25"
arxiv_id: "2605.25869"
arxiv_url: "https://arxiv.org/abs/2605.25869"
pdf_url: "https://arxiv.org/pdf/2605.25869v1"
categories:
  - "cs.CL"
tags:
  - "长期记忆架构"
  - "记忆表示"
  - "来源监控"
  - "记忆中间表示"
  - "智能体认知"
  - "LLM智能体"
relevance_score: 9.0
---

# Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation

## 原始摘要

Long-term memory is essential for persistent LLM agents, yet prevailing architectures store historical interactions as unstructured, flat text. This unconstrained storage induces provenance-role collapse, a critical failure mode where agents suffer from source-monitoring errors. To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint. MemIR writes long-term memory into grounded atoms that separate raw evidence, retrieval cues, and truth-bearing claims, with factual authorization restricted to supported claim atoms. It then applies multi-route atomic projection and provenance-scoped utilization to transform heterogeneous retrieval hits into claim-centered candidate bundles and a normalized fact interface for answer generation. Experiments on LoCoMo and BEAM-100K demonstrate that MemIR consistently outperforms existing memory baselines, especially on tasks requiring source tracking, temporal grounding, and aggregation of fragmented evidence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长期LLM代理中存在的“来源-角色混淆”问题。当前，长期记忆架构通常将历史交互存储为非结构化的平面文本，这种无约束的存储方式导致代理在记忆检索时出现“来源监控错误”，即无法区分原始证据、推断内容和事实性声明，将不同来源或不同角色的记忆片段不当合并或重复计数。例如，在回答“Joanna写了多少个剧本”时，模型可能因缺乏显式指代链接和来源边界而错误地将分散在不同时间段的同一对象的不同阶段视为独立实体。为解决这一认知脆弱性问题，本文提出了一种名为MemIR的带类型中间表示，它通过结构化的记忆原子将来源监控从认知能力转化为架构约束。MemIR将长期记忆分解为分离原始证据、检索线索和事实声明的接地原子，并仅允许受支持的声明原子作为事实记忆，从而在架构层面强制代理保持对记忆来源和角色的正确区分，避免了现有无类型平面存储方法导致的记忆混淆和推理错误。

### Q2: 有哪些相关研究？

相关研究可分为三类：

**方法类：** 包括RL驱动的CRUD操作、神经符号记忆宫殿、主动上下文压缩等长期记忆管理系统。这些方法虽能自主管理记忆，但均将历史交互存储为无类型文本摘要或压缩令牌，未区分记忆来源与角色。MemIR通过引入类型化记忆原子表示，明确分离证据、检索线索和事实断言，从根本上解决了原产地-角色崩塌问题。

**记忆组织类：** 涵盖引用感知检索、图基文本索引等结构化记忆方法，以及认知启发的测试时记忆化与主动记忆提取机制。虽然这些方法增强了多跳推理能力，但结构本身未指定记忆的功能性权威——引用锚可定位上下文，却不能作为事实断言。MemIR基于认知来源监测理论，将记忆权威操作化为事实授权与原始检索命中的分离。

**评测类：** LoCoMo和BEAM-100K等复杂多轮基准测试推动了长期智能体评估发展。MemIR在这些需要源跟踪、时间定位和碎片证据聚合的基准上显著优于现有记忆基线，验证了其类型化表示在长期交互任务中的有效性。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为MemIR（Memory Intermediate Representation）的带类型内存表示架构，从结构层面解决长期智能体中的“来源-角色崩溃”问题。该架构的核心创新是将来源监控理论作为结构性约束，强制分离证据、检索线索和事实主张三类信息。

整体框架包含三个耦合阶段：**系统化内存原子写入**将非结构化交互历史编译为七种类型的内存原子：页面原子（P）、片段原子（S）保留原始边界和逐字证据，句柄原子（H）、时间原子（T）和枢轴原子（V）提供引用和语义锚点，声明原子（A）表示有源可证的事实断言，检索视图（R）暴露访问关系。通过严格的支撑约束（每个原子必须包含非空的支持片段），确保所有提取的线索或生成的声明都保留明确的证据来源。

**多路由原子投影**阶段结合稀疏检索（BM25基于检索视图）和稠密检索（BGE-M3基于声明和片段），通过倒数秩融合整合排名信号，并将异构命中统一投影到声明中心候选空间。投影规则确保只有片段、句柄或枢轴原子通过关联的声明进入事实候选层，形成包含声明、聚合检索强度和完整溯源闭包的候选包。

**溯源范围利用**阶段使用粗到细的重新排序：先保留M个候选包覆盖广度，再用交叉编码器评分，最后由LLM选择器挑选最多X个互补候选包。这些包被转换为规范化的事实接口F_q，包含声明文本、溯源闭包、时间线索和功能角色。生成模型f_φ基于该结构化接口生成答案，若证据不足则返回“证据不足”而非生成虚构内容。在LoCoMo和BEAM-100K数据集上的实验表明，该架构在单跳、多跳、时间和开放域任务中全面优于现有基线，尤其在来源追踪和碎片证据聚合任务上表现突出。

### Q4: 论文做了哪些实验？

MemIR在LoCoMo和BEAM-100K两个长期记忆基准上进行了实验。LoCoMo包含10段长多轮对话和1540个问题，涵盖单跳、多跳、时序和开放域问答，使用F1、BLEU-1和LLM评分（Judge）评估。BEAM-100K包含20段对话和10万token历史，含400个问题涉及10个任务类别（如矛盾解决、知识更新、时序推理等），采用LLM评分。对比方法包括LoCoMo、ReadAgent、Zep、Mem0等15种基线。主要结果：在BEAM-100K上，MemIR以GPT-4.1-mini为骨干取得平均48.26分，远超第二名SimpleMem的40.68分，尤其在矛盾解决（32.30 vs 20.60）、知识更新（58.40 vs 55.00）和时序推理（38.50 vs 35.00）上提升显著。在LoCoMo上，MemIR在GPT-4.1和GPT-4.1-mini骨干下均优于所有基线，在单跳、时序和开放域问题上增益最大。消融实验验证了claim原子、cue原子、类型约束投影和候选包组件的必要性。骨干对比显示，更强的骨干（GPT-4.1）进一步提升性能。超参数分析表明，每页12个claim原子、预排序池大小32和选定包预算6为最优设置。

### Q5: 有什么可以进一步探索的点？

MemIR主要通过结构化记忆缓解了溯源-角色坍缩问题，但其核心局限在于仅优化了证据的组织形式，而对跨事实的复杂推理仍高度依赖下游生成模型。未来可探索在记忆层引入显式的多跳逻辑推理机制，例如基于图结构的claim bundle关系推理，使模型能在检索阶段直接完成因果关系推导，而非仅提供候选事实。此外，当前多类型原子的写入带来了显著的计算开销，在长期交互中可能积累为延迟瓶颈。可以研究轻量化的压缩技术，如利用可微分内存或语义哈希对重复线索进行稀疏化编码，并在解码时通过分层注意力动态激活相关原子，从而在保持溯源清晰的同时降低冗余存储。另一个值得关注的方向是动态调整原子类型的粒度和授权范围，使系统能根据任务复杂度自适应地权衡事实精确性与推理自由度。

### Q6: 总结一下论文的主要内容

长期智能体面临的关键问题是长程记忆中的“溯源-角色崩溃”现象，即扁平化文本存储导致智能体难以区分信息来源、角色与事实权威性，从而引发源监控错误。为解决这一问题，论文提出了MemIR，一种类型化记忆中间表示，通过在架构层面实施源监控约束。MemIR将长程记忆分解为原子化的基础单元，分别存储原始证据、检索线索和主张性事实，并仅授权支持性主张原子进行事实输出。通过多路径原子投影与溯源范围利用，MemIR将异构检索结果转化为以主张为中心的候选束，并生成标准化事实接口以辅助答案生成。在LoCoMo和BEAM-100K数据集上的实验表明，MemIR在需要源追踪、时间锚定及碎片证据聚合的任务上持续优于现有记忆基线方法。这一研究揭示了可靠长程记忆不仅依赖有效检索，更需明确的溯源保存与事实授权。
