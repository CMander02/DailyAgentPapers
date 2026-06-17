---
title: "ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents"
authors:
  - "Ander Alvarez"
  - "Santhiya Rajan"
  - "Samuel Mugel"
  - "Román Orús"
date: "2026-06-16"
arxiv_id: "2606.18037"
arxiv_url: "https://arxiv.org/abs/2606.18037"
pdf_url: "https://arxiv.org/pdf/2606.18037v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Tool-using Agent"
  - "事实性验证"
  - "溯源归因"
  - "MCP协议"
  - "工具调用"
  - "NLI验证"
relevance_score: 7.5
---

# ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents

## 原始摘要

Tool-using LLM agents increasingly use the Model Context Protocol (MCP) to answer from heterogeneous evidence sources, including search, APIs, databases, clinical records, and formulary tools. Standard factuality metrics usually test whether an answer is supported by pooled evidence, missing a provenance-sensitive failure mode: a claim may be supported somewhere while being attributed to the wrong source. We call this cross-source conflation.
  We introduce ProvenanceGuard, a source-aware verifier for MCP-grounded answers. It consumes captured MCP traces with stable tool IDs, source IDs, and raw outputs; decomposes answers into atomic claims; routes claims to source-specific evidence; checks support with NLI and a token-alignment proxy; compares stated attribution with the routed source; and returns per-claim verdicts plus an answer-level allow/block decision. Blocked answers can be repaired with retrieval-augmented answer revision and re-verified.
  We evaluate on 281 medical-domain MCP-agent traces. A 266-trace adjudicated subset yields 2,325 LLM-assisted claim labels split by trace; 361 held-out labels are human-verified. On the 40-trace held-out split, ProvenanceGuard achieves block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims, outperforming source-blind baselines that do not emit claim-to-source IDs. On a harder multi-source benchmark it reaches block F1 0.846, while source-plus-relation accuracy drops to 0.229, showing that exact source ownership remains difficult with semantically close sources. Repair-and-reverify resolves all blocked answers in the full trace set, often via conservative fallback. In 50 controlled clinical conflation probes, ProvenanceGuard detects all injected attribution swaps with no retained wrong attribution. These results show that source attribution is an independent axis for factuality verification in MCP-based agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于Model Context Protocol（MCP）的工具使用型LLM智能体在事实性验证中的一个关键缺陷——跨源混淆问题。

**研究背景：** 在医疗、企业等场景中，LLM智能体通过MCP协议调用多个异构数据源（如PubMed、患者病历、API、数据库等）来生成答案。每个工具调用都会产生带有稳定工具ID和源ID的原始输出，答案中的声明通常隐含或明确地归属于某个特定来源。

**现有方法的不足：** 现有的事实性验证指标（如MiniCheck、RAGAS、AlignScore等）主要检测答案是否被证据池整体支持，属于“源盲”验证。这些方法忽略了关键问题：一个声明可能在证据池的某个地方得到支持，但被错误地归因到了另一个来源。例如，“恩格列净降低死亡率终点”这一声明可能得到了临床试验文献的支持，但智能体却声称来自患者的病历图表。源盲验证器会错误地判定为“支持”，而忽视了归因错误。

**本文要解决的核心问题：** 针对MCP接地答案，提出一种“源感知”的事实性验证框架ProvenanceGuard。该框架需要同时评估每个原子声明是否被特定来源的证据支持（支持检查），以及答案中声明的归因源是否正确指向该证据来源（归源检查），从而检测并阻止跨源混淆这一独立于传统事实性的失效模式。

### Q2: 有哪些相关研究？

相关研究可分为三类：**细粒度支持验证**、**RAG忠实度与归因生成**、以及**多源工具归因系统**。在细粒度支持验证方面，FActScore、MiniCheck、SummaC、AlignScore等系统评估生成声明是否被证据支持，但这些方法不保留声明到MCP源ID的映射，因此无法直接用于源归因指标（如Top-1源准确率）。在RAG忠实度与归因领域，ALCE评估LLM生成的引用是否指向正确的支持段落，是最接近源归因的任务，但ALCE在单个检索集的段落级别操作，而MCP轨迹暴露了需要路由步骤的工具级源ID。本文将其扩展到工具来源层。对于多源系统中的归因，Atomic Information Flow等方法追踪工具输出的信息流，但与本文不同，我们不推断潜在信息流或解决参数知识冲突，而是验证声明的归属是否与路由的MCP源匹配。此外，RARR等事后修订方法和训练型验证器（如FactCC、RAGulator）与ProvenanceGuard互补，后者作为黑箱MCP智能体输出的独立事后检查。工具使用评估通常关注工具调用正确性，而本文专注于验证声明是否被引用的源支持。

### Q3: 论文如何解决这个问题？

ProvenanceGuard 通过一种**源感知的细粒度事实验证**方法来解决跨源混淆问题。其核心是构建一个**基于MCP轨迹的验证流水线**，将验证过程分解为五个关键步骤。

**整体框架**围绕MCP轨迹展开，该轨迹包含稳定的工具ID、源ID和原始输出。主要模块包括：1）**原子声明分解器**：将代理的回答拆解为不可再分的原子声明；2）**源路由证据检索引擎**：根据声明的语义和MCP轨迹中的源ID，将每个声明路由到对应的证据源（如数据库记录、API输出等）；3）**双层支持验证器**：采用自然语言推理（NLI）模型和**令牌对齐代理**（通过计算声明与证据间的令牌覆盖比例作为替代指标）来验证声明是否被其路由源支持；4）**源归因比较器**：对比声明中陈述的源归属与实际路由的源是否一致，这是识别跨源混淆的关键；5）**裁决与修复模块**：输出每个声明的通过/失败判决，以及整个回答的允许/阻止决策。被阻止的回答会进入**检索增强的答案修订**环节，通过引入遗漏或正确的源信息生成修正答案，并重新经过验证。

**创新点**在于：首次将“源归属错误”（即一个声明被正确证据支持但归因于错误来源）作为独立的验证维度；通过令牌对齐代理弥补NLI在细粒度源匹配上的不足；以及结合MCP轨迹的稳定标识符实现高效的证据路由与回溯。

### Q4: 论文做了哪些实验？

论文在医疗领域的MCP Agent上进行了三项主要实验。**实验设置**：使用281条医疗MCP Agent轨迹，其中266条含标注的轨迹被拆分为训练/验证集（1,597+367条声明）和40条轨迹的留出测试集（361条声明，260条具有源可评估性）。**对比方法**：将ProvenanceGuard与MiniCheck、RAGAS Faithfulness、AlignScore和SummaC-ZS等无源感知基线比较（仅支持度指标）。**主要结果**：1) 在留出集上，ProvenanceGuard达到block F1=0.802，源准确率=0.858；2) 在更难的包含2,587个成对源候选行的多源基准测试上，block F1=0.846，但源加关系准确率降至0.229；3) 在全量轨迹集上，修复与重新验证流程解决了所有被阻断的回答；4) 在50个受控临床混淆探测中，检测到所有注入的归因交换且无保留的错误归因。这些结果表明源归因是MCP Agent事实性验证的独立维度。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向**  
1. **多源语义混淆**：当来源间语义高度重叠（如同药不同厂商），ProvenanceGuard的源准确率从0.858骤降至0.229，表明其缺乏对关系型归因的细粒度建模。未来可引入结构化三元组匹配或对比学习增强源间冲突感知。  
2. **修复机制保守性**：当前“修复-再验证”流程依赖回溯式回退，可能过度抑制真实但多源交叉的回答。建议设计基于置信度的动态裁剪策略，结合主动查询（如追问用户来源偏好）实现精准修复。  
3. **跨领域迁移性**：医疗领域实体术语规范、来源边界清晰，但开放域场景（如新闻聚合、多模态知识库）中相同事实可能自然分布于异构源，需研究模糊归因的容忍度边界。  
4. **效率瓶颈**：原子声明逐条路由至NLI+对齐代理的计算开销较高，可探索基于图神经网络的端到端归因推理，或利用流式处理优先验证高风险声明（如含数字、专名句）。  
**改进思路**：构建分层归因框架——先通过对比学习编码源特征向量，再以声明-源相似度矩阵结合注意力机制动态确定路由阈值，降低对人工规则依赖。

### Q6: 总结一下论文的主要内容

该论文提出了新颖的源感知事实性验证框架ProvenanceGuard，专门面向基于模型上下文协议（MCP）的LLM代理。核心问题是标准事实性指标仅检查证据是否支持答案，但忽略了"跨源混淆"的关键故障——陈述可能被证据支持但属性归属错误。方法上采用"路由器+NLI验证器"架构：首先将答案分解为原子声明，通过捕获稳定工具ID和源ID的MCP轨迹逐源路由证据，使用自然语言推理和令牌对齐代理检查支持度，同时对比声明中归属与路由源是否一致，最终输出逐声明判定和整体拦截决策。拦截答案可通过检索增强重写回溯修复。在281条医疗领域MCP代理轨迹上的评估表明，ProvenanceGuard在40条保留集上达到拦截F1值0.802和源准确性0.858，显著优于源盲基线。在50个受控跨源混淆探测中，它检测出所有注入的属性交换且零错误保留。结果证明了源归因是MCP代理事实性验证的独立维度，对构建真实环境下可靠的工具调用代理具有重要价值。
