---
title: "To Know is to Construct: Schema-Constrained Generation for Agent Memory"
authors:
  - "Lei Zheng"
  - "Weinan Song"
  - "Daili Li"
  - "Yanming Yang"
date: "2026-04-22"
arxiv_id: "2604.20117"
arxiv_url: "https://arxiv.org/abs/2604.20117"
pdf_url: "https://arxiv.org/pdf/2604.20117v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Cognitive Schema"
  - "Generative Memory"
  - "Retrieval-Augmented Generation"
  - "Long-Term Adaptation"
  - "Multi-Hop Reasoning"
  - "Architecture Design"
relevance_score: 9.0
---

# To Know is to Construct: Schema-Constrained Generation for Agent Memory

## 原始摘要

Constructivist epistemology argues that knowledge is actively constructed rather than passively copied. Despite the generative nature of Large Language Models (LLMs), most existing agent memory systems are still based on dense retrieval. However, dense retrieval heavily relies on semantic overlap or entity matching within sentences. Consequently, embeddings often fail to distinguish instances that are semantically similar but contextually distinct, introducing substantial noise by retrieving context-mismatched entries. Conversely, directly employing open-ended generation for memory access risks "Structural Hallucination" where the model generates memory keys that do not exist in the memory, leading to lookup failures. Inspired by this epistemology, we posit that memory is fundamentally organized by cognitive schemas, and valid recall must be a generative process performed within these schematic structures. To realize this, we propose SCG-MEM, a schema-constrained generative memory architecture. SCG-MEM reformulates memory access as Schema-Constrained Generation. By maintaining a dynamic Cognitive Schema, we strictly constrain LLM decoding to generate only valid memory entry keys, providing a formal guarantee against structural hallucinations. To support long-term adaptation, we model memory updates via assimilation (grounding inputs into existing schemas) and accommodation (expanding schemas with novel concepts). Furthermore, we construct an Associative Graph to enable multi-hop reasoning through activation propagation. Experiments on the LoCoMo benchmark show that SCG-MEM substantially improves performance across all categories over retrieval-based baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体在长期记忆系统中面临的核心挑战。研究背景是，为了实现自主智能体在长期互动中的连贯推理、个性化与时间一致性，记忆能力至关重要。当前主流方法，如MemGPT或基于检索增强生成（RAG）的系统，普遍采用“经验主义”假设，将记忆访问视为一个基于密集向量检索的判别性问题。然而，现有方法存在明显不足：首先，密集检索严重依赖句子内的语义重叠或实体匹配，但语义相似并不等同于上下文相关。这导致嵌入向量常常无法区分语义相同但上下文截然不同的实例，从而引入大量上下文不匹配的噪声条目。其次，大多数检索索引在拓扑结构上是扁平的，缺乏进行关联性多跳推理所需的关系结构。尽管近期有研究尝试引入图结构，但它们仍依赖密集检索来选择初始节点，继承了相同的噪声问题。另一种直接利用LLM进行开放式生成以访问记忆的方法，则存在“结构幻觉”风险，即模型可能生成记忆中根本不存在的记忆键，导致查找失败。

因此，本文要解决的核心问题是：如何设计一种既能避免检索噪声，又能杜绝结构幻觉的可靠、可演进的长期记忆访问机制。受皮亚杰建构主义认识论的启发，论文认为记忆本质上由认知图式组织，有效的回忆必须是在这些图式结构约束下进行的生成过程。为此，论文提出了SCG-MEM（模式约束生成记忆）架构，将记忆访问重新定义为“模式约束生成”。通过维护一个动态的认知图式（具体实现为前缀树），严格约束LLM的解码过程，使其只能生成存在于该图式中的有效记忆键，从而从形式上杜绝了结构幻觉。此外，论文还通过同化（将新输入纳入现有图式）和顺应（用新概念扩展图式）对记忆更新进行建模，以支持长期适应，并构建关联图以实现通过激活传播进行多跳推理。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：记忆架构、检索方法以及约束解码技术。

在**记忆架构**方面，早期系统如MemoryBank、MemGPT将文本分块并通过密集检索或缓存层级管理；ReadAgent采用要点压缩支持交互式查找。为支持高级推理，RAPTOR、GraphRAG等将数据组织为递归树或知识图，但多针对静态语料，更新成本高。近期动态方法如MemTree、CAM采用受皮亚杰启发的树结构进行在线聚类。然而，这些方法本质上仍依赖判别式检索进行初始访问，易受语义相似但上下文无关的向量噪声干扰。

在**检索与生成方法**上，传统密集检索严重依赖句子内的语义重叠或实体匹配，难以区分语义相似但语境不同的实例。生成式检索如RetroLLM使用FM-index约束直接生成细粒度证据，但未解决记忆键不存在导致的“结构幻觉”问题。

在**约束解码技术**领域，早期工作如Grid Beam Search关注词汇约束，确保关键词出现在输出中。近期发展包括Synchromesh、PICARD等系统，通过掩码无效词元对代码生成施加语法约束。在图遍历任务中，GCR、DoG等方法利用约束引导LLM在知识图上选择有效节点，但通常基于静态图，未考虑模式动态演化。

本文提出的SCG-MEM与上述工作的区别在于：它从根本上摆脱了检索范式，通过**模式约束生成**实现记忆访问。与静态约束解码不同，SCG-MEM引入动态认知模式，通过前缀树约束解码仅生成有效的记忆条目键，从而避免结构幻觉，并支持通过同化与顺应进行模式演化，实现了在语义和本体层面的约束适应。

### Q3: 论文如何解决这个问题？

论文通过提出SCG-MEM架构来解决传统密集检索方法中的噪声问题和开放式生成中的“结构幻觉”问题。其核心方法是将记忆访问重新定义为“模式约束生成”，确保生成的所有记忆键都严格符合动态认知模式，从而从根本上杜绝结构幻觉。

整体框架包含三个紧密耦合的组件。基础是**认知模式**，它定义了智能体的认知边界。该模式并非静态列表，而是通过一个**前缀字典树**来实现，该字典树编码了所有有效概念键。在生成过程中，该字典树作为一个硬性约束，在LLM解码的每一步，通过一个二元有效性指示器将导致无效前缀的令牌概率置零，并重新归一化概率分布。这确保了最终生成的任何完整键必然属于有效模式集合，从数学上保证了结构幻觉概率为零。

为了支持长期适应，论文设计了**演化模式构建**机制。它受皮亚杰理论启发，通过两种途径动态更新模式：**同化**和**顺应**。当新信息输入时，系统首先尝试在现有模式约束下将其“同化”为已有概念。如果失败（例如困惑度过高），则触发“顺应”过程：暂时放松模式约束，允许基础LLM生成新概念，经验证后将其插入字典树，从而显式扩展认知边界。这使系统能在保持结构一致性的同时实现开放式的知识增长。

为了超越简单的有效性检查并支持多跳推理，框架在演化模式之上叠加了一个**关联图**。该图以模式中的有效概念为节点，边权重基于概念在整个交互历史中的共现强度计算，采用逆文档频率乘积来强调稀有、特定领域概念之间的联系。在回忆时，过程分为两步：首先，对查询进行模式约束的束搜索，生成一组多样且相关的**种子概念**；然后，通过基于边权重的加权采样进行**关联传播**，从种子概念扩散到其拓扑邻居，从而检索出隐含的相关上下文概念。最后，将这些激活的概念映射回原始文本片段，为LLM生成最终回答提供依据。

创新点主要体现在：1）将构造主义认识论形式化为一个可计算的、模式约束的生成框架；2）通过前缀字典树实现硬约束解码，为消除结构幻觉提供了形式化保证；3）将模式演化（同化与顺应）与关联推理（图传播）分离，分别管理“存在性”和“关联性”，使系统兼具严谨性与灵活性。

### Q4: 论文做了哪些实验？

实验在LoCoMo基准测试上进行，该基准用于评估长期、多会话的智能体记忆。数据集包含超长对话（平均9K token，最多35个会话），评估了四个类别：单跳（单会话检索）、多跳（跨会话合成）、时序（时间相关更新）和对抗性（误导性查询），排除了开放域以专注于对话基础记忆。主要评估指标为F1分数（平衡精确率和召回率）和BLEU-1（衡量生成响应与真实响应的词重叠）。

对比方法包括五种代表性记忆系统：LoCoMo（无记忆机制，直接将完整历史对话加入提示）、ReadAgent（通过分页、记忆摘要和交互查找处理长文档）、MemoryBank（基于艾宾浩斯遗忘曲线动态更新历史交互）、MemGPT（受操作系统内存层次启发的双层虚拟上下文管理系统）以及A-MEM（将原始交互重构为结构化“笔记”并使用密集检索进行初始访问）。所有模型均本地部署，使用Hugging Face Transformers库，并在Qwen2.5（1.5B, 3B）和Llama 3.2（1B, 3B）模型上评估，文本嵌入使用BGE-M3模型。

主要结果显示，SCG-MEM在所有类别和模型规模上均显著优于最强基线A-MEM。具体而言，在Qwen2.5 3B上，单跳任务的F1提升达146.7%（从17.23提升至42.51），多跳任务F1提升126.6%（从12.57提升至28.49），对抗性任务F1提升88.6%（从27.91提升至52.63）。平均F1提升在Qwen2.5 3B上达94.5%（从21.33提升至41.48）。消融实验表明，移除认知约束（无模式约束解码）导致多跳F1下降39.5%，移除进化更新（禁用同化机制）导致多跳F1下降34.2%，验证了各组件的重要性。超参数分析显示，检索概念数k约35时性能最优，关联传播深度为1跳时效果最佳，更深传播会引入噪声导致性能下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的SCG-Mem架构在解决结构幻觉和提升记忆访问精度方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，当前系统主要依赖文本模态，未来可扩展至多模态场景（如视觉、听觉），构建更通用的认知图式，以支持更复杂的现实世界交互。其次，论文提到的记忆压缩和重写机制尚未具体实现，这关系到长期适应中的存储效率与知识整合能力，需设计算法来消除冗余并动态优化记忆结构。此外，图式目前以前缀树形式组织，未来可探索分层或图神经网络的抽象表示，以增强多级概念间的语义连贯性与推理效率。从更广阔的视角看，如何将此类架构与强化学习结合，使智能体能通过环境反馈自主演化图式，或引入不确定性建模来处理模糊或冲突的记忆，均是提升系统鲁棒性与泛化能力的关键方向。

### Q6: 总结一下论文的主要内容

该论文针对现有基于密集检索的智能体记忆系统存在的语义混淆和检索噪声问题，提出了一种基于建构主义认识论的生成式记忆架构SCG-MEM。其核心思想是将知识视为在认知图式（schema）约束下主动建构的过程，而非被动复制。方法上，系统将记忆访问重新定义为**图式约束生成**：通过维护动态的认知图式，严格约束大语言模型的解码过程，使其仅生成记忆中实际存在的有效键值，从而从根本上避免了“结构幻觉”导致查找失败的问题。为支持长期适应，记忆更新通过**同化**（将输入归入现有图式）和**顺应**（扩展图式以纳入新概念）进行建模，并构建**关联图**以实现通过激活传播的多跳推理。在LoCoMo基准测试上的实验表明，SCG-MEM在所有类别上均显著优于基于检索的基线方法。该工作的主要贡献在于为智能体记忆提供了一个具有形式化保证、能抗幻觉且支持动态演化的生成式框架，推动了记忆系统从被动检索到主动建构的范式转变。
