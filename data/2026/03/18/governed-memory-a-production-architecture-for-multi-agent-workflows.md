---
title: "Governed Memory: A Production Architecture for Multi-Agent Workflows"
authors:
  - "Hamed Taheri"
date: "2026-03-18"
arxiv_id: "2603.17787"
arxiv_url: "https://arxiv.org/abs/2603.17787"
pdf_url: "https://arxiv.org/pdf/2603.17787v1"
github_url: "https://github.com/personizeai/governed-memory"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Agent Memory"
  - "Agent Governance"
  - "Agent Architecture"
  - "Production System"
  - "Shared Memory"
  - "Retrieval"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Governed Memory: A Production Architecture for Multi-Agent Workflows

## 原始摘要

Enterprise AI deploys dozens of autonomous agent nodes across workflows, each acting on the same entities with no shared memory and no common governance. We identify five structural challenges arising from this memory governance gap: memory silos across agent workflows; governance fragmentation across teams and tools; unstructured memories unusable by downstream systems; redundant context delivery in autonomous multi-step executions; and silent quality degradation without feedback loops. We present Governed Memory, a shared memory and governance layer addressing this gap through four mechanisms: a dual memory model combining open-set atomic facts with schema-enforced typed properties; tiered governance routing with progressive context delivery; reflection-bounded retrieval with entity-scoped isolation; and a closed-loop schema lifecycle with AI-assisted authoring and automated per-property refinement. We validate each mechanism through controlled experiments (N=250, five content types): 99.6% fact recall with complementary dual-modality coverage; 92% governance routing precision; 50% token reduction from progressive delivery; zero cross-entity leakage across 500 adversarial queries; 100% adversarial governance compliance; and output quality saturation at approximately seven governed memories per entity. On the LoCoMo benchmark, the architecture achieves 74.8% overall accuracy, confirming that governance and schema enforcement impose no retrieval quality penalty. The system is in production at Personize.ai.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业级多智能体工作流中普遍存在的“记忆治理鸿沟”问题。随着企业部署数十个分布在不同工作流和团队中的自主智能体节点，每个节点都对相同的实体（如客户、公司）进行操作，但缺乏共享的记忆层和统一的治理层，导致组织智能无法有效积累和利用。

研究背景是当前企业AI应用已从单一智能体转向复杂的多智能体生态系统。现有方法，特别是检索增强生成（RAG），主要关注单一智能体在单次查询中的检索相关性，是一个检索原语，而非基础设施层。其不足在于：无法管理多个智能体间的记忆共享，导致**记忆孤岛**；缺乏统一的策略执行机制，造成**治理碎片化**；记忆以非结构化文本为主，形成**下游系统无法使用的死胡同**；在自主多步执行中缺乏会话感知，导致**上下文冗余交付**；以及没有质量监控反馈循环，导致**系统性能无声退化**。

因此，本文要解决的核心问题是：如何构建一个**共享的记忆与治理层**，以系统性地解决上述五个结构性挑战，确保多智能体工作流在组织范围内能够协调、高效、可靠地运行，并使记忆能够被下游系统有效利用。论文提出的“受治理记忆”架构，通过双记忆模型、分层治理路由、反射边界检索与闭环模式生命周期等机制，旨在填补RAG范式留下的这一基础设施空白。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**检索增强生成（RAG）与检索优化方法**：包括RAG及其扩展、文档扩展查询预测（Document expansion by query prediction）和HyDE等方法。这些研究聚焦于提升检索质量，但本文指出它们存在四个关键缺口：缺乏对存储内容的治理、缺乏组织上下文路由、缺乏会话感知的交付机制，以及缺乏质量反馈闭环。本文的治理路由层借鉴了文档扩展策略以融入组织上下文，但核心贡献在于整体的治理架构，而非检索原语本身。

**单智能体记忆系统**：这类系统为受控环境中的单个智能体建模记忆，但未解决组织上下文、模式（schema）强制实施或多租户隔离等问题。本文的架构旨在为跨工作流的多个智能体提供共享记忆层。

**生产记忆层与记忆原语**：例如SimpleMem和Mem0，它们将记忆原子化为经过共指消解和语义去重的事实，解决了单个事实如何存储和检索的问题。本文的Governed Memory（\sysname{}）则位于更上层的基础设施层，其贡献是正交的。它扩展了任何记忆底层，增加了模式强制、组织治理路由、实体范围的多租户隔离和闭环质量反馈等功能，两者是架构上的互补关系而非竞争。

**记忆管理与评估技术**：包括Self-RAG（引入反射式检索）、MemGPT（探索分层记忆管理）以及基于领域特定量规的评分与执行轨迹捕获（用于治理场景下的评估）。这些工作孤立地解决了特定的记忆能力。Liu等人的研究揭示了模型对长上下文中间信息的利用不足，这启发了本文的会话感知渐进式交付机制。

**本文的独特定位**：与上述所有研究工作不同，此前没有系统能提供一个统一的共享基础设施层，将模式强制的类型化记忆、组织治理路由、渐进式上下文交付、闭环模式优化和多租户实体隔离整合起来，供组织内任意智能体访问。本文的Governed Memory架构正是为了填补这一空白而设计的。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“治理内存”的四层架构来解决企业多智能体工作流中缺乏共享内存和统一治理的问题。该架构的核心是构建一个共享的内存与治理层，确保各智能体节点能够基于统一的组织上下文进行操作，同时避免信息孤岛和治理碎片化。

整体框架包含四个层次，每层针对特定的治理问题设计，并可独立配置。第一层是**双内存存储**，采用双提取管道处理内容：一方面生成开放集记忆（原子化、自包含的事实），另一方面生成模式强制的记忆（遵循组织模式定义的属性值）。两者均以统一的格式存储，并带有实体范围和组织隔离。关键技术包括单次LLM调用同时提取两种记忆、基于嵌入相似度的属性选择、以及写入时的去重机制，防止近重复积累。

第二层是**治理路由**，负责根据具体任务选择并注入组织上下文（如政策、指南）。它提供两种模式：快速模式（约850毫秒）通过混合评分（嵌入相似度、关键词重叠、治理范围提升）进行排序，无需LLM调用；完整模式（2-5秒）则采用LLM进行结构化分析。创新点在于**渐进式内容交付**：通过会话状态跟踪已交付的变量，在自主多步执行中仅注入增量内容，避免了冗余上下文导致的令牌膨胀和注意力分散，实验显示可减少50%的令牌使用。

第三层是**治理检索**，结合向量相似度搜索与实体范围过滤，并引入**反射有界循环**：LLM在有限轮次（默认2轮）内判断证据完整性，若不完整则生成针对性后续查询，确保检索质量。检索过程严格隔离实体，防止跨实体污染，实验显示在500次对抗查询中实现了零泄漏。

第四层是**模式生命周期与质量反馈**，实现了闭环的治理增强。通过AI辅助模式创作将自然语言描述转化为模式定义，并提供交互式增强功能。系统执行领域特定的评估，记录结构化轨迹（如记忆召回日志、治理上下文有用性评级），并基于反馈进行**自动化逐属性优化**，持续改进提取质量。

此外，系统通过统一的记录结构确保数据可追溯性，并强制实施组织分区和实体范围隔离。它暴露标准MCP接口，使不同框架的智能体都能通过相同的组织上下文读写和治理内存，无需定制集成。实验验证了该架构在保持高检索准确性的同时，有效解决了内存孤岛、治理碎片化等五大挑战。

### Q4: 论文做了哪些实验？

论文通过一系列受控实验验证了其核心架构机制。实验设置上，主要使用合成数据集（共250个样本，涵盖通话记录、文档、邮件、转录文本和聊天记录五种内容类型），并嵌入已知事实、属性值、共指问题和近重复项等真实情况，以确保可重复测量。所有实验均在生产API上使用固定随机种子（42）执行。

数据集与基准测试方面，除了主实验语料，还构建了多源实体、实体隔离配置文件、召回查询集、治理变量对和冲突对等专门数据集用于特定测试。外部验证则使用了LoCoMo基准测试（包含272个会话和1542个问题）。

对比方法主要体现在不同实验条件的对比上，例如：在提取质量中对比了不同内容类型；在反射消融实验中对比了无反射、API管理反射和手动多轮反射等条件；在端到端评估中对比了无记忆、原始记忆、开放集+治理和完全受治理记忆四种条件；并将最终结果与Mem0、Zep、OpenAI内置记忆等独立评估的记忆系统进行了背景对比。

主要结果与关键数据指标如下：
1.  **提取质量**：整体事实召回率达到99.6%，各内容类型召回率在98%至100%之间。质量门控使输出缺陷率相对降低25%（从8.4%降至6.3%），时间准确性提升6.8个百分点（从88.4%升至95.2%），信噪比从1.1:1提升至4.2:1。
2.  **双模态覆盖**：开放集记忆和模式强制记忆具有互补性，34%的事实被两者共同捕获，38%仅被开放集捕获，12%仅被模式强制捕获，综合召回率为82.8%。
3.  **治理路由**：路由精度达到92%，召回率为88%。
4.  **反射检索**：在困难的多跳查询上，手动两轮反射可将答案完整性从基线37.1%提升至62.8%。
5.  **实体隔离**：在500个对抗性查询下，实现了零真实跨实体泄漏，误报率为2.74%。
6.  **冲突解决**：新鲜信息在答案中出现的冲突检测率为83.3%，完全抑制陈旧信息的严格标准达成率为33.3%。
7.  **端到端质量**：与无记忆基线（平均得分79.5）相比，完全受治理记忆系统将得分提升6.4分至85.9。
8.  **治理合规**：在50个对抗性场景中实现了100%的合规性，护栏激活率为96%。
9.  **基准测试**：在LoCoMo基准测试中总体准确率达到74.8%，在开放式推理类别（83.6%）上超过人类基线（75.4%），验证了治理和模式强制机制未损害检索质量。

### Q5: 有什么可以进一步探索的点？

该论文在讨论部分已明确指出多个局限性，这些正是未来研究的关键方向。首先，系统的多个核心组件依赖启发式规则或经验阈值（如质量门控、去重阈值），未来可通过引入更深入的语义分析或基于内容特性的自适应机制来提升鲁棒性。其次，对于多智能体并发写入冲突这一实际生产场景，目前仅验证了时序冲突，并发冲突的检测与解决仍是一个开放问题，需要设计新的并发控制协议。此外，反思检索的效能高度依赖查询生成策略，如何使轮次边界适应查询复杂度、优化API的查询生成是计划中的改进点。

结合个人见解，还可探索以下几点：第一，论文提及的“开放集与模式执行内存的频谱”概念，可进一步研究动态映射机制，自动将开放集事实归类到现有或新扩展的模式属性中，以实现更智能的信息整合。第二，在治理层面，可探索跨组织的联邦学习框架，使治理策略能在不同数据规范和成熟度的机构间有效迁移与验证。第三，为应对数据隐私与偏见，未来可集成差分隐私或公平性约束到治理层中，使系统在提供详细画像的同时，满足合规性并减少歧视性模式。这些方向将推动治理内存从高效生产系统向更自适应、可靠且符合伦理的下一代架构演进。

### Q6: 总结一下论文的主要内容

该论文针对企业AI中多智能体工作流存在的“记忆治理鸿沟”问题，提出了“受治理记忆”这一生产级架构。核心问题是多个自主智能体节点在工作流中对同一实体进行操作时，缺乏共享记忆和统一治理，导致了记忆孤岛、治理碎片化、下游系统无法使用非结构化记忆、多步执行中上下文冗余传递以及缺乏反馈环导致的静默质量退化这五大结构性挑战。

论文的核心贡献是设计并实现了一个共享记忆与治理层，它通过四种集成机制来解决上述问题：1）结合开放集原子事实与模式强制类型属性的双重记忆模型；2）具有渐进式上下文传递的分层治理路由；3）基于反思的检索与实体范围隔离；4）包含AI辅助创作和自动化属性级优化的闭环模式生命周期。

实验验证表明，该架构在生产规模下有效：实现了99.6%的事实召回率和互补的双模态覆盖、92%的治理路由精度、500次对抗查询中零跨实体泄漏、100%的对抗性治理合规性，并在LoCoMo基准测试上达到74.8%的总体准确率，证明治理和模式强制不会损害检索质量。此外，每个实体约七个受治理记忆时输出质量达到饱和，为智能体部署提供了实用操作点。该方案已投入商业应用。
