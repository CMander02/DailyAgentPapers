---
title: "AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views"
authors:
  - "Minh Tam Pham"
  - "Trinh Pham"
  - "Tong Chen"
  - "Hongzhi Yin"
  - "Quoc Viet Hung Nguyen"
  - "Thanh Tam Nguyen"
date: "2026-04-08"
arxiv_id: "2604.07041"
arxiv_url: "https://arxiv.org/abs/2604.07041"
pdf_url: "https://arxiv.org/pdf/2604.07041v1"
github_url: "https://github.com/pminhtam/AV-SQL"
categories:
  - "cs.DB"
  - "cs.AI"
  - "cs.ET"
  - "cs.HC"
  - "cs.IR"
tags:
  - "Text-to-SQL"
  - "Agent Architecture"
  - "Multi-Agent Collaboration"
  - "Query Decomposition"
  - "Tool Use"
  - "LLM Agent"
  - "Database Interaction"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views

## 原始摘要

Text-to-SQL is the task of translating natural language queries into executable SQL for a given database, enabling non-expert users to access structured data without writing SQL manually. Despite rapid advances driven by large language models (LLMs), existing approaches still struggle with complex queries in real-world settings, where database schemas are large and questions require multi-step reasoning over many interrelated tables. In such cases, providing the full schema often exceeds the context window, while one-shot generation frequently produces non-executable SQL due to syntax errors and incorrect schema linking. To address these challenges, we introduce AV-SQL, a framework that decomposes complex Text-to-SQL into a pipeline of specialized LLM agents. Central to AV-SQL is the concept of agentic views: agent-generated Common Table Expressions (CTEs) that encapsulate intermediate query logic and filter relevant schema elements from large schemas. AV-SQL operates in three stages: (1) a rewriter agent compresses and clarifies the input query; (2) a view generator agent processes schema chunks to produce agentic views; and (3) a planner, generator, and revisor agent collaboratively compose these views into the final SQL query. Extensive experiments show that AV-SQL achieves 70.38% execution accuracy on the challenging Spider 2.0 benchmark, outperforming state-of-the-art baselines, while remaining competitive on standard datasets with 85.59% on Spider, 72.16% on BIRD and 63.78% on KaggleDBQA. Our source code is available at https://github.com/pminhtam/AV-SQL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂现实场景下的Text-to-SQL问题，即如何将自然语言查询准确转换为可执行的SQL语句。研究背景是，尽管大语言模型（LLMs）推动了该领域的快速发展，但现有方法在面对大规模数据库架构和需要多步推理的复杂查询时仍存在明显不足。具体而言，现有方法通常假设整个数据库模式可以一次性输入提示中，这在真实世界包含数千张表和列的大型数据库中是不切实际的，因为完整模式常常超出LLMs的上下文窗口限制，导致注意力分散和模式链接错误增加。此外，现有的一步生成方法容易产生因语法错误或无效引用而无法执行的SQL，且由于错误相互纠缠，修复单一复杂查询非常困难。

本文的核心问题是：如何设计一个鲁棒的框架，以有效处理长上下文约束下的复杂Text-to-SQL任务，确保生成的SQL可执行且准确。为此，论文提出了AV-SQL框架，其核心创新在于引入“代理视图”的概念——即由代理生成的公共表表达式（CTEs），用于封装中间查询逻辑并从大型模式中筛选相关模式元素。该框架通过多阶段专业化代理协作，将复杂查询分解为可管理的步骤，从而缓解上下文窗口压力，显式化模式过滤，并通过中间CTEs的执行验证提升最终SQL的可执行性。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：评测基准、方法模型和长上下文建模。

在**评测基准**方面，早期工作如Academic、MAS等关注单领域；后续WikiSQL实现了大规模单表评测，Spider引入了跨领域多表复杂查询，BIRD覆盖了37个专业领域，KaggleDBQA则针对真实网络数据库。本文重点应对的Spider 2.0进一步提升了复杂度，其模式包含数千列，使得完整模式提示变得不切实际。

在**Text-to-SQL方法**上，研究经历了多个阶段。预LLM时代的神经语义解析器（如RAT-SQL、RESDSQL）依赖结构化解码和显式模式建模。LLM出现后，零样本和少样本提示（如DIN-SQL、DAIL-SQL）通过任务分解、示例演示和多模型流水线提升了性能。监督微调方法（如CodeS）以及混合多候选方法（如CHESS）进一步增强了鲁棒性。近期系统（如CHASE-SQL、Alpha-SQL）引入了规划、候选选择和执行反馈来处理复杂模式。然而，现有方法在Spider 2.0上表现仍不佳，最近的智能体方法（如ReForCE、DSR-SQL）执行准确率仅约35%。本文提出的AV-SQL与这些工作的核心区别在于引入了**可验证的、基于CTE的智能体视图**作为中间步骤，通过分块处理大型模式来指导最终SQL合成，从而在Spider 2.0上取得了70.38%的显著提升。

在**长上下文建模**方面，常见策略包括扩展上下文长度（如GPT-4）、检索增强生成（RAG）以及智能体框架（如CoA）。本文受CoA启发，将长上下文分解思想适配到Text-to-SQL任务中，通过将大型模式分割为可管理的块，让智能体顺序处理子集，从而避免了将完整模式加载到单个提示中的问题，显式地进行了模式过滤，并通过对中间智能体视图进行验证来提高鲁棒性。

### Q3: 论文如何解决这个问题？

AV-SQL通过引入一个基于多智能体协作的管道式框架来解决复杂Text-to-SQL任务中的挑战，其核心思想是将复杂的整体任务分解为多个专门的子任务，并利用“智能体视图”作为中间推理和模式过滤的载体。

**整体框架与主要阶段**：框架分为三个阶段。首先，**问题重写阶段**使用一个重写器智能体（LLM_Rewriter）对原始自然语言查询进行澄清和压缩，整合外部知识并过滤无关信息，输出结构清晰、意图明确的改写后问题，为下游阶段提供干净的输入。其次，**智能体视图生成阶段**是核心。系统先将庞大的数据库模式通过压缩（合并冗余表/列）和基于长度的分块处理，分解为多个可管理的模式块。每个模式块由一个视图生成器智能体（LLM_View）独立处理，该智能体接收改写后的问题和单个模式块，并行生成两个输出：1) 基于公共表表达式的**智能体视图**，即封装了中间查询逻辑（如连接、过滤）的可执行CTE查询及其自然语言原理；2) **JSON模式选择**，标识出与该问题相关的候选表和列。此阶段还包含一个迭代的验证与修复循环，包括从CTE中提取字面值并检索匹配的数据库值、基于执行的语法和模式链接错误验证、以及CTE与JSON选择之间的一致性检查，确保中间输出的质量。最后，**SQL生成阶段**由规划器、生成器和修订器智能体协作，利用前阶段聚合的所有已验证的智能体视图和过滤后的全局模式选择，组合生成最终的SQL查询。

**关键技术与创新点**：1) **智能体视图概念**：创新性地将CTE作为智能体生成的、可重用且已验证的中间推理模块，既压缩了复杂逻辑，又实现了从庞大模式中动态过滤相关元素。2) **模式分治与并行处理**：通过模式压缩和分块，将超出LLM上下文窗口的超大规模模式分解，使每个智能体能专注于局部模式，克服了信息过载问题。3) **多智能体专业化管道**：采用分工明确的智能体（重写器、多个视图生成器、规划器、生成器、修订器）进行链式协作，而非单一LLM的一次性生成，提高了处理复杂、多步骤推理的鲁棒性和准确性。4) **迭代验证与闭环修复**：在视图生成阶段集成执行验证和一致性检查，形成“生成-验证-反馈-修复”的闭环，显著提升了中间结果和最终SQL的可执行性。

### Q4: 论文做了哪些实验？

论文在三个标准数据集（Spider、BIRD、KaggleDBQA）和更具挑战性的Spider 2.0基准上进行了广泛的实验。实验设置上，AV-SQL框架采用了分阶段的多智能体管道，包括问题重写、视图生成和SQL生成，并引入了模式压缩（约10倍压缩率）和分块处理来应对大规模数据库模式。

主要对比方法包括基于LLM的先进模型，如DIN-SQL、DAIL-SQL、C3等。实验结果表明，AV-SQL在复杂的Spider 2.0基准上取得了70.38%的执行准确率，显著超越了基线方法。在标准数据集上，它也保持了强大的竞争力，在Spider上达到85.59%的准确率，在BIRD上达到72.16%，在KaggleDBQA上达到63.78%。这些关键数据指标证明了该框架在分解复杂查询、处理大规模模式方面的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的AV-SQL框架在复杂Text-to-SQL任务上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其性能高度依赖于大语言模型（LLM）的能力，在涉及深层逻辑推理或高度专业化领域知识（如金融、医疗）的查询时，准确性可能下降。其次，多智能体协作的管道式设计虽然提升了可解释性，但也引入了额外的计算开销和延迟，在需要低延迟响应的实时应用中可能受限。

未来研究可以从以下几个方向展开：一是**优化智能体间的协作机制**，探索更高效的通信协议或动态规划策略，以减少迭代次数和整体耗时。二是**增强对模糊或隐含语义的理解**，通过结合外部知识库或进行多轮交互式澄清，提升对复杂用户意图的解析能力。三是**探索轻量化部署方案**，例如通过模型蒸馏或选择性调用，在保持性能的同时降低对大型LLM的依赖。此外，可将“智能体视图”的概念扩展到**多数据库或联邦查询场景**，研究如何在数据分布、权限隔离的环境下安全高效地生成与组合视图，这更具现实应用价值。

### Q6: 总结一下论文的主要内容

本文针对复杂Text-to-SQL任务中因数据库模式庞大、查询多步推理困难而导致的上下文窗口溢出和生成SQL不可执行等问题，提出了AV-SQL框架。其核心贡献是引入了“代理视图”概念，即由大型语言模型（LLM）代理生成的可执行公共表表达式（CTE），用于封装中间查询逻辑并从大型模式中筛选相关模式元素。

方法上，AV-SQL采用三阶段多代理协作管道：首先，重写代理对输入查询进行压缩和澄清；其次，视图生成代理处理分块后的模式，生成并利用执行反馈迭代修复代理视图；最后，规划器、生成器和修订器代理协同将这些视图组合成最终的SQL查询。

实验表明，该方法在具有挑战性的Spider 2.0基准测试上取得了70.38%的执行准确率，优于现有先进方法，同时在Spider、BIRD和KaggleDBQA等标准数据集上保持竞争力。该框架在零样本设置下表现强劲，无需微调或示例，并通过分解复杂查询、验证中间步骤，显著提升了在真实世界大规模复杂场景下的鲁棒性和可执行性。
