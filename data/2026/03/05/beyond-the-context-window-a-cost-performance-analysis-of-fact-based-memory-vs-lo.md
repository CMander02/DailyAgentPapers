---
title: "Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents"
authors:
  - "Natchanon Pollertlam"
  - "Witchayut Kornsuwannawit"
date: "2026-03-05"
arxiv_id: "2603.04814"
arxiv_url: "https://arxiv.org/abs/2603.04814"
pdf_url: "https://arxiv.org/pdf/2603.04814v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Persistent Agent"
  - "Cost-Performance Analysis"
  - "Long-Context LLM"
  - "Fact-Based Memory"
  - "Agent Architecture"
  - "Agent Evaluation"
relevance_score: 8.5
---

# Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents

## 原始摘要

Persistent conversational AI systems face a choice between passing full conversation histories to a long-context large language model (LLM) and maintaining a dedicated memory system that extracts and retrieves structured facts. We compare a fact-based memory system built on the Mem0 framework against long-context LLM inference on three memory-centric benchmarks - LongMemEval, LoCoMo, and PersonaMemv2 - and evaluate both architectures on accuracy and cumulative API cost. Long-context GPT-5-mini achieves higher factual recall on LongMemEval and LoCoMo, while the memory system is competitive on PersonaMemv2, where persona consistency depends on stable, factual attributes suited to flat-typed extraction. We construct a cost model that incorporates prompt caching and show that the two architectures have structurally different cost profiles: long-context inference incurs a per-turn charge that grows with context length even under caching, while the memory system's per-turn read cost remains roughly fixed after a one-time write phase. At a context length of 100k tokens, the memory system becomes cheaper after approximately ten interaction turns, with the break-even point decreasing as context length grows. These results characterize the accuracy-cost trade-off between the two approaches and provide a concrete criterion for selecting between them in production deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决持久性会话AI系统在长期部署中面临的核心架构选择问题：是使用长上下文大语言模型（LLM）直接处理完整对话历史，还是构建一个基于事实的专用记忆系统来提取和检索结构化信息。研究背景是，随着AI助手在跨多会话场景（如个人助理、客服）中的广泛应用，系统需要持续、连贯地访问过往交互信息。尽管当前长上下文LLM的上下文窗口已极大扩展，使得直接输入全部历史看似可行，但现有方法存在明显不足。长上下文LLM方案虽然可能提供较高的信息召回准确率，但其API成本会随着上下文长度线性增长，即使采用提示缓存技术，每次交互仍会产生与上下文长度成比例的增量费用，这在长期、高频的交互中会导致经济成本急剧上升。相比之下，基于事实的记忆系统虽在部分任务上准确率可能稍逊，但其成本结构不同：前期一次性写入成本后，每次查询仅需检索少量相关事实，单次读取成本大致固定。因此，本文要解决的核心问题是：在持久性智能体的实际部署中，如何权衡长上下文LLM与基于事实的记忆系统在准确性和经济成本之间的取舍，并提供具体的决策标准。论文通过在多个人记忆基准测试上比较两种架构的准确率，并构建包含缓存机制的成本模型，量化分析两者的累积成本差异，从而为生产环境中的架构选型提供依据。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 长上下文大语言模型（LLMs）**
相关研究致力于通过改进架构和位置编码技术来扩展Transformer模型的有效上下文窗口，例如Gemini 2.5 Pro、Claude Opus 4.5和GPT-5等模型支持百万级token的上下文。然而，研究表明，当相关信息出现在长上下文中间时，模型性能常会下降，且有效利用的上下文长度常短于名义窗口大小。为降低长上下文推理的计算成本，已有工作提出了提示词压缩和模型级联等方法。**本文与这些工作的关系在于**，它将采用提示缓存的LLM作为持久对话记忆的候选架构之一，并评估其与基于事实的记忆系统在准确性和成本上的差异。

**2. 对话智能体的记忆系统**
为LLM智能体设计的记忆系统主要包括：工作记忆（覆盖活动上下文窗口）、事实（长期）记忆（存储用户偏好和过往事件）以及情景记忆（记录交互的事件序列）。相关研究包括：将检索增强生成（RAG）作为早期记忆增强形式；MemGPT提出的分层存储架构，类比操作系统虚拟内存；以及Mem0提出的提取原子化、扁平类型事实并存入向量数据库的管道。近期系统（如EverMemOS、Temporal Semantic Memory、A-MEM、Zep）则追求更丰富的表示，向结构化、时序感知的知识图谱发展。**本文与这些工作的区别在于**，它使用Mem0的扁平事实提取作为受控基线，并将其与长上下文推理进行对比，而非与其他更复杂的记忆架构比较。

**3. LLM推理的成本效率**
由于LLM API按token计价，成本是生产部署的核心关切。提示缓存（重用已计算输入前缀的键值状态）是最有效的成本降低机制之一，OpenAI和Anthropic等提供商均提供大幅折扣。相关研究如Cache-Augmented Generation将缓存应用于静态知识库，以及分析KV缓存淘汰策略以优化多轮对话的尾部延迟。**本文与这些工作的关系在于**，其成本模型对长上下文基线应用了90%折扣的提示缓存，并在此基础上推导出记忆系统变得更具成本优势的交互轮次转折点。

**4. 长上下文评测基准**
多个基准测试用于评估LLM在需要长程记忆任务上的表现，包括专门针对对话记忆的LongMemEval、LoCoMo和PersonaMem v2，以及更通用的长上下文基准如LongBench、∞Bench和“大海捞针”社区基准。相关研究利用这些基准记录了“迷失在中间”、名义与有效上下文大小不符等性能下降模式。**本文与这些工作的关系在于**，它正是在LongMemEval、LoCoMo和PersonaMemv2这三个以记忆为中心的基准上，对两种架构的准确性进行了评估和比较。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于事实的记忆系统（Mem0框架）与长上下文LLM进行对比，来解决持久性对话AI系统在准确性与成本之间的权衡问题。核心方法包括设计一个四阶段架构的记忆系统，并与直接使用长上下文LLM的架构进行性能和经济性评估。

**整体框架与主要模块**：
记忆系统架构包含四个关键阶段：
1.  **对话分割**：将长对话按时间顺序分段处理（批次大小=10，每段最多8000字符），以保持时序并防止上下文漂移。
2.  **事实提取**：使用GPT-5-nano作为提取模型，将对话内容提炼为原子化、非层级（扁平类型）的结构化事实，便于后续向量检索。
3.  **嵌入与存储**：使用text-embedding-3-small模型将事实转换为1536维向量，并存储于pgvector数据库（采用HNSW索引，余弦相似度）。
4.  **检索机制**：针对每个查询，执行向量搜索（top_k=20）检索相关事实，再由推理模型（GPT-5-mini）基于检索到的事实生成答案。

作为对比，长上下文LLM架构不进行事实提取，而是直接将原始对话历史作为上下文输入给生成模型（如GPT-5-mini或GPT-OSS-120B）。

**关键技术**：
- **评估基准**：在三个内存中心化基准（LongMemEval、LoCoMo、PersonaMemv2）上测试，覆盖不同上下文长度和记忆需求。
- **评估方法**：采用LLM-as-a-judge框架（GPT-5-mini作为评判模型），通过3票共识协议（多数投票）减少随机偏差，计算回答准确率。
- **成本模型**：构建了包含提示缓存（对后续轮次输入令牌提供90%折扣）的成本分析模型。长上下文LLM的成本随轮次和上下文长度增长（首轮全价，后续轮次折扣价），而记忆系统的成本分为一次性写入成本（事实提取和嵌入）和固定的每轮读取成本（仅处理检索到的事实和当前查询）。

**创新点**：
1.  **系统化对比**：首次在多个基准上对事实记忆系统与长上下文LLM进行准确性和成本的综合比较。
2.  **经济性分析模型**：提出了明确的成本计算公式和盈亏平衡点分析，揭示两种架构的成本结构差异：长上下文LLM的每轮成本随上下文长度增长，而记忆系统的每轮读取成本在一次性写入后基本固定。
3.  **决策指导**：通过实验发现，在约10万令牌的上下文长度下，记忆系统在大约10轮交互后变得更具成本效益，且盈亏平衡点随上下文长度增加而降低。这为生产部署中根据交互轮次和上下文长度选择架构提供了具体准则。

### Q4: 论文做了哪些实验？

论文在三个以记忆为中心的基准测试（LongMemEval、LoCoMo和PersonaMemv2）上，对比了基于Mem0框架构建的事实记忆系统与长上下文LLM推理的性能和成本。实验设置包括：记忆系统使用GPT-5-nano进行事实提取，GPT-5-mini作为读取器；长上下文基线使用LC GPT-5-mini和LC GPT-OSS-120B模型，直接处理完整对话历史。

在准确性方面，LC GPT-5-mini在LoCoMo和LongMemEval上表现最佳，准确率分别为92.85%和82.40%，显著高于记忆系统的57.68%和49.00%。在PersonaMemv2上，记忆系统准确率为62.48%，与LC GPT-5-mini（69.75%）差距较小，且略优于LC GPT-OSS-120B（60.50%）。

成本分析基于LongMemEval实验（500次对话，平均上下文长度101,601个词元）。记忆系统的一次性写入阶段（事实提取和嵌入）总成本约为21.80美元，每次查询的读取成本约0.0013美元。长上下文基线中，GPT-5-mini每次请求成本约0.0293美元，GPT-OSS-120B约0.0115美元。关键指标显示：在上下文长度为100,000词元时，记忆系统在约10次交互轮次后成本更低；交互20轮时，记忆系统成本低约26%。随着上下文长度增加，盈亏平衡点所需轮次减少（例如从30,000词元的13轮降至500,000词元的9轮），表明记忆系统在高上下文场景下更具成本优势。

### Q5: 有什么可以进一步探索的点？

本文的局限性为未来研究提供了多个可探索的方向。首先，在记忆架构方面，当前研究仅评估了基于扁平类型事实提取的Mem0系统，未来可探索更结构化的记忆系统，如包含时间语义或分层记忆的系统，以更好地保留对话中的时间标记、隐式指代和瞬时更新等信息，从而提升事实召回率。其次，在评估范围上，现有基准测试主要关注跨会话的用户特定信息，未来可扩展至需要实时知识、结构化数据推理或多文档证据链的任务，以更全面地衡量记忆系统的能力。此外，本文的成本模型基于特定API定价和缓存假设，未来可纳入基础设施成本（如向量数据库托管）并考虑动态记忆更新场景，以更贴近实际部署。从改进思路看，可设计混合架构，在长上下文推理保证精度的同时，利用记忆系统处理高频查询以优化成本；也可开发更智能的提取模型，通过上下文感知减少信息丢失。这些方向有助于深化对持久智能体设计中精度-成本权衡的理解。

### Q6: 总结一下论文的主要内容

这篇论文针对持久性对话AI系统的记忆架构选择问题，对比了两种主流方案：将完整对话历史输入长上下文大语言模型（LLM）的方案，与基于结构化事实提取和检索的专用记忆系统（以Mem0框架为例）。研究通过LongMemEval、LoCoMo和PersonaMemv2三个以记忆为中心的基准测试，评估了两种架构在事实准确性（召回率）和累积API成本上的表现。

在准确性方面，长上下文GPT-5-mini在需要回忆具体事实和日期的LongMemEval和LoCoMo测试中表现更优，准确率高出约33-35个百分点。而在侧重于人物属性一致性的PersonaMemv2测试中，基于事实提取的记忆系统表现相当甚至略优，说明其对于稳定、事实型属性的记忆是有效的。

在成本方面，论文构建了一个包含提示缓存折扣的成本模型，揭示了两者截然不同的成本结构：长上下文方案每轮交互的成本随上下文长度增长而持续增加；记忆系统则需一次性支付构建记忆库的写入成本，此后每轮的读取成本基本固定。模拟显示，当上下文长度达到10万词元时，记忆系统在大约10轮交互后开始更经济，交互达20轮时可节省约26%总成本，且上下文越长，盈亏平衡点出现得越早。

核心结论是，两种方案在准确性与成本间存在权衡，没有绝对最优。论文的意义在于为生产部署提供了明确的选择依据：对于用户会多次交互的长期服务（如客户支持、个人助手），记忆系统能在保证足够准确性的同时显著节省成本；而对于一次性或短期交互且准确性优先的场景，长上下文方案是更佳选择。
