---
title: "LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation"
authors:
  - "Yilin Xiao"
  - "Jin Chen"
  - "Qinggang Zhang"
  - "Yujing Zhang"
  - "Chuang Zhou"
  - "Longhao Yang"
  - "Lingfei Ren"
  - "Xin Yang"
  - "Xiao Huang"
date: "2026-04-03"
arxiv_id: "2604.02954"
arxiv_url: "https://arxiv.org/abs/2604.02954"
pdf_url: "https://arxiv.org/pdf/2604.02954v1"
github_url: "https://github.com/Jord8061/logicPoison"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Retrieval-Augmented Generation (RAG)"
  - "GraphRAG"
  - "Adversarial Attack"
  - "Logical Reasoning"
  - "Knowledge Graph"
  - "Robustness"
relevance_score: 7.5
---

# LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation

## 原始摘要

Graph-based Retrieval-Augmented Generation (GraphRAG) enhances the reasoning capabilities of Large Language Models (LLMs) by grounding their responses in structured knowledge graphs. Leveraging community detection and relation filtering techniques, GraphRAG systems demonstrate inherent resistance to traditional RAG attacks, such as text poisoning and prompt injection. However, in this paper, we find that the security of GraphRAG systems fundamentally relies on the topological integrity of the underlying graph, which can be undermined by implicitly corrupting the logical connections, without altering surface-level text semantics. To exploit this vulnerability, we propose \textsc{LogicPoison}, a novel attack framework that targets logical reasoning rather than injecting false contents. Specifically, \textsc{LogicPoison} employs a type-preserving entity swapping mechanism to perturb both global logic hubs for disrupting overall graph connectivity and query-specific reasoning bridges for severing essential multi-hop inference paths. This approach effectively reroutes valid reasoning into dead ends while maintaining surface-level textual plausibility. Comprehensive experiments across multiple benchmarks demonstrate that \textsc{LogicPoison} successfully bypasses GraphRAG's defenses, significantly degrading performance and outperforming state-of-the-art baselines in both effectiveness and stealth. Our code is available at \textcolor{blue}https://github.com/Jord8061/logicPoison.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并利用基于图的检索增强生成（GraphRAG）系统的一个新型安全漏洞。研究背景是，GraphRAG通过将知识组织成图结构，增强了大型语言模型（LLM）的推理能力，并因其社区检测和关系过滤等机制，对传统的RAG攻击（如文本投毒、提示注入）表现出固有的抵抗力。现有方法（如GRAGPOISON）主要依赖生成虚假内容来攻击，但这类方法容易被检测，且未能触及GraphRAG的核心防御——其推理能力依赖于图结构的拓扑完整性，而非孤立的数据点。

现有方法的不足在于，它们试图通过注入错误内容或攻击单点来破坏系统，但GraphRAG的图结构能够通过多跳推理路径维持整体推理的稳健性，使得传统攻击效果有限。本文发现，GraphRAG的安全根本依赖于底层知识图的拓扑完整性，而这一完整性可以在不改变文本表面语义的情况下，通过破坏逻辑连接来暗中破坏。

因此，本文要解决的核心问题是：如何在未知图内部结构（黑盒）的情况下，设计一种有效、隐蔽且可迁移的攻击方法，来破坏GraphRAG的逻辑推理能力，而不是仅仅污染其内容。为此，论文提出了LogicPoison攻击框架，其核心是通过保持实体类型不变的实体交换机制，扰动图中的关键逻辑枢纽和推理桥梁，从而在维持文本可读性的同时，暗中破坏图的拓扑结构，将有效的推理路径引向死胡同或错误方向，最终导致系统性能显著下降。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕检索增强生成（RAG）模型的安全攻击研究展开，可分为以下几类：

**1. 传统RAG攻击方法**：这类工作主要针对基于文本的RAG系统。例如，PoisonedRAG通过知识库投毒来引导模型行为；PANDORA利用检索功能进行间接越狱攻击；TrojanRAG通过联合攻击在检索上下文中插入后门；Jamming攻击则通过提升阻塞文档来引发拒绝服务。这些攻击大多依赖于**显式的内容注入或添加性扰动**，即直接修改或插入文本内容。

**2. 图RAG（GraphRAG）的初期攻击**：GRAGPOISON是近期针对GraphRAG的攻击工作，它通过注入由大语言模型生成的文本来模拟图中的虚假链接。虽然它针对了图结构，但其**本质仍是内容注入**，依赖于生成虚假的文本信息来构造关联。

**本文提出的LogicPoison与上述工作的核心区别在于攻击范式不同**。现有技术主要基于“显式内容注入”，而LogicPoison是一种**隐式的逻辑攻击**。它不改变任何表面文本的语义，而是通过类型保持的实体交换机制，扰动图中的逻辑枢纽和推理桥梁，从而破坏图拓扑的完整性，误导多跳推理路径。这种方法针对的是GraphRAG所依赖的**结构化逻辑关系**，而非文本内容本身，因此能更隐蔽地绕过GraphRAG对传统文本攻击的固有防御。

### Q3: 论文如何解决这个问题？

论文提出的LogicPoison攻击框架通过破坏知识图谱的拓扑结构而非注入虚假内容来攻击GraphRAG系统。其核心方法是采用类型保持的实体置换机制，在不改变表层文本语义的前提下，隐式地破坏逻辑连接，从而误导系统的多跳推理。

整体框架包含两个互补的子策略：全局逻辑毒化和查询中心逻辑毒化。全局策略针对语料库级别的逻辑枢纽实体，通过文档频率分析识别高频实体作为目标，破坏图谱的整体连通性；查询中心策略则针对特定查询所需的多跳推理链中的关键实体，利用大语言模型进行思维链推理提取，确保攻击覆盖用户查询的精确路径。两者结合形成统一的候选实体集合。

关键技术包括：首先进行实体提取与类型标注，使用NER模型识别文档中的类型化实体；其次通过语料库级频率分析近似评估实体的拓扑重要性；接着利用查询引导的机制，通过CoT提取并验证查询相关的推理实体；最后采用循环置换函数对目标实体进行类型保持的替换，确保替换后的文本在局部保持语法合理性和语义可读性，从而规避基于语法的检测。

创新点在于首次针对GraphRAG系统的逻辑推理脆弱性进行攻击，通过扰动逻辑枢纽和推理桥梁实体，有效将有效推理路径重定向至死胡同，同时保持表层文本的合理性。实验表明，该方法在多个基准测试中显著降低了GraphRAG系统的性能，其攻击成功率和隐蔽性均优于现有基线。

### Q4: 论文做了哪些实验？

论文实验设置方面，在三个多跳问答基准数据集（HotpotQA、2WikiMultihopQA、MuSiQue）上各随机采样500个查询进行评估，使用Facebook/contriever作为嵌入模型，检索top-k设为10，并选取知识图谱中前5%的实体作为攻击目标。实验对比了多种基线方法：针对RAG系统的最先进攻击PoisonedRAG，以及针对LLM的传统对抗方法（Naive Attack、Prompt Injection、GCG Attack、Disinformation）。评估在三种代表性的GraphRAG框架（Microsoft GraphRAG、HippoRAG 2、GFM-RAG）和三种不同规模的基础大语言模型（GPT-4o-mini、Llama-3.1-8B、Qwen-3-32B）上进行，以验证攻击的普适性。

主要结果通过攻击成功率（ASR）和基于LLM评判的语义攻击成功率（ASR-G）来衡量。关键数据指标显示，LogicPoison在所有评估场景中均达到最优。例如，在2Wiki数据集上，针对GPT-4o-mini+GraphRAG的组合，LogicPoison的ASR为78.4%，ASR-G为95.6%，显著高于其他基线（如Prompt Injection的58.8%和80.4%）。在更具挑战性的MuSiQue数据集上，LogicPoison也表现出主导性能，验证了逻辑破坏对于多跳推理任务比内容注入更有效。效率分析表明，LogicPoison在时间消耗上比PoisonedRAG快约4倍，Token消耗仅为后者的1/8，且无需向数据集中注入任何攻击性令牌，隐蔽性更高。消融实验证实了其全局逻辑毒化和查询中心逻辑毒化两个模块均具有显著效果，组合后达到最佳攻击性能。此外，防御分析实验表明，查询改写（Paraphrasing）防御策略对LogicPoison几乎无效（攻击效果下降始终小于1.0%），基于困惑度（PPL）的检测也基本失效（AUC值仅为0.57，接近随机猜测）。

### Q5: 有什么可以进一步探索的点？

本文提出的LogicPoison攻击虽揭示了GraphRAG在拓扑逻辑层面的脆弱性，但仍存在若干局限值得深入探索。首先，当前研究基于静态知识图谱构建，而实际系统常涉及动态更新（如实时增删节点），攻击在高频更新下的持久性与稳定性需进一步实证检验。其次，实验仅针对英文语料，尽管逻辑推理本身具有语言无关性，但在形态复杂或屈折丰富的语言中实现隐蔽的实体替换需设计特定的改写启发式方法，未来可拓展至多语言场景验证。此外，攻击目前集中于离散的结构扰动，未来可探索结合语义细微篡改的混合攻击模式，以测试系统对逻辑与语义联合攻击的鲁棒性。从防御视角看，研究可探索动态图学习机制，通过实时监测逻辑路径异常或引入冗余验证节点来增强拓扑完整性，从而构建更具韧性的GraphRAG架构。

### Q6: 总结一下论文的主要内容

该论文针对基于图检索增强生成（GraphRAG）系统的安全性问题展开研究。GraphRAG通过知识图谱增强大语言模型的推理能力，对传统文本投毒等攻击具有抵抗力，但其安全依赖于图谱的拓扑完整性。论文发现，通过破坏逻辑连接而非篡改文本内容，可有效攻击该系统。为此，作者提出了LogicPoison攻击框架，采用保持实体类型不变的实体交换机制，从全局逻辑枢纽和查询特定推理桥梁两个层面扰动图谱结构，从而阻断多跳推理路径，使有效推理陷入死胡同，同时保持表层文本的合理性。实验表明，LogicPoison能成功绕过GraphRAG的防御，显著降低其性能，并在效果和隐蔽性上优于现有基线。该研究揭示了GraphRAG在逻辑层面的安全脆弱性，为相关领域的安全研究提供了重要方向。
