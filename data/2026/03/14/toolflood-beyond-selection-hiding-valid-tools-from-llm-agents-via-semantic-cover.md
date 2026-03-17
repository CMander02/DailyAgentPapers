---
title: "ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering"
authors:
  - "Hussein Jawad"
  - "Nicolas J-B Brunel"
date: "2026-03-14"
arxiv_id: "2603.13950"
arxiv_url: "https://arxiv.org/abs/2603.13950"
pdf_url: "https://arxiv.org/pdf/2603.13950v1"
github_url: "https://github.com/as1-prog/ToolFlood"
categories:
  - "cs.CL"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Adversarial Attack"
  - "Retrieval-Augmented Generation"
  - "Robustness"
relevance_score: 8.0
---

# ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering

## 原始摘要

Large Language Model (LLM) agents increasingly use external tools for complex tasks and rely on embedding-based retrieval to select a small top-k subset for reasoning. As these systems scale, the robustness of this retrieval stage is underexplored, even though prior work has examined attacks on tool selection. This paper introduces ToolFlood, a retrieval-layer attack on tool-augmented LLM agents. Rather than altering which tool is chosen after retrieval, ToolFlood overwhelms retrieval itself by injecting a few attacker-controlled tools whose metadata is carefully placed by exploiting the geometry of embedding space. These tools semantically span many user queries, dominate the top-k results, and push all benign tools out of the agent's context.
  ToolFlood uses a two-phase adversarial tool generation strategy. It first samples subsets of target queries and uses an LLM to iteratively generate diverse tool names and descriptions. It then runs an iterative greedy selection that chooses tools maximizing coverage of remaining queries in embedding space under a cosine-distance threshold, stopping when all queries are covered or a budget is reached. We provide theoretical analysis of retrieval saturation and show on standard benchmarks that ToolFlood achieves up to a 95% attack success rate with a low injection rate (1% in ToolBench). The code will be made publicly available at the following link: https://github.com/as1-prog/ToolFlood

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决大语言模型（LLM）智能体在利用外部工具时，其基于嵌入向量的工具检索层存在的一个新型安全漏洞。研究背景是，随着工具生态系统的快速扩张，受限于上下文窗口长度，LLM智能体通常采用检索方式，根据用户查询的嵌入向量，从海量工具元数据（如名称、描述）中召回最相关的top-k个子集供模型后续选择和规划。现有关于工具生态系统的攻击研究主要集中在“选择阶段”，即假设恶意工具已出现在候选列表中，通过优化其元数据使其被选中的概率更高。然而，这类方法存在一个根本局限：它们默认良性工具仍会出现在检索结果中，攻击只是在候选列表内部进行竞争。

本文指出并致力于解决一个此前未被充分探索的核心问题：**检索层的“top-k支配”攻击**。这种攻击的目标并非在候选列表中“推销”自己的工具，而是通过向工具库中注入少量由攻击者精心构造的工具，使其在嵌入空间中 strategically positioned，从而在语义上覆盖广泛的用户查询，彻底垄断top-k检索结果，将所有的良性工具完全“挤出”智能体的可见上下文。这相当于对工具可见性发起了一次检索层的拒绝服务攻击，使得那些依赖于候选集中存在良性工具的选择阶段防御机制（如提示注入过滤）完全失效。因此，本文的核心问题是：如何系统性地构造和注入这种“语义覆盖”攻击工具（即ToolFlood攻击），以极低的注入比例实现高成功率的top-k支配，从而暴露并分析基于嵌入检索的工具发现机制的脆弱性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工具增强智能体范式、针对工具选择的攻击以及检索层攻击。

在**工具增强智能体范式**方面，相关工作包括ReAct（通过提示技术实现推理与执行的交织）、Toolformer（通过自监督微调学习工具使用）以及Gorilla和ToolLLM等处理大规模API的模型。这些系统都依赖基于嵌入的检索机制来动态选择相关工具。本文的研究建立在此范式之上，但重点关注其检索阶段的鲁棒性。

在**针对工具选择的攻击**方面，已有工作如ToolHijacker和Attractive Metadata Attack (AMA)通过毒化或优化工具元数据，使恶意工具在检索后的候选集中被优先选择。这些攻击的共同局限在于，它们依赖于在固定的top-k候选列表内与良性工具竞争，且其效果可能受到提示级防御或后检索过滤的缓解。本文提出的ToolFlood攻击与这些工作有本质区别：它不旨在在候选集中竞争胜出，而是通过“语义覆盖”在检索阶段就将所有良性工具挤出top-k列表，使其对LLM完全不可见，从而绕过下游的选择安全措施。

在**检索层攻击**方面，相关工作主要来自检索增强生成（RAG）领域，例如通过注入精心构建的文本来污染知识库或操纵检索结果以引导生成。本文借鉴了这种将“检索器+索引”视为安全边界的思路，首次将此类攻击系统性地应用于工具检索场景。此外，ToolFlood在概念上与经典的**Sybil攻击**（通过创建大量虚假身份来获得不成比例的影响力）相关，可被理解为针对工具检索层的Sybil式影响力操作。

### Q3: 论文如何解决这个问题？

论文通过一个名为ToolFlood的两阶段攻击策略来解决针对工具增强型LLM代理检索层的攻击问题。其核心目标是向工具库中注入少量由攻击者控制的工具，使其元数据在嵌入空间中精心布局，从而在语义上覆盖大量用户查询，垄断检索结果的前k位，并将所有良性工具挤出代理的上下文。

整体框架分为两个主要阶段：第一阶段是生成多样化的对抗性工具元数据候选池；第二阶段则是将工具注入问题建模为预算约束下的语义多重覆盖问题，并通过贪心优化算法选取最优工具子集。

在**第一阶段（候选池生成）**中，系统首先从目标查询集\(\mathcal{Q}_{tar}\)中随机采样一个小子集\(S_i\)，然后利用攻击者控制的LLM基于该子集生成一组工具元数据（包括名称和描述）。生成过程要求元数据与子集中所有查询语义相关，而非针对单一查询，这促使生成的工具嵌入位于该子集查询嵌入的共享区域，从而能够泛化覆盖多个邻近查询。此过程迭代进行，最终合并所有生成的元数据形成候选池\(\mathcal{P}_I\)。该阶段的理论保证是，随着迭代次数增加，候选池将以高概率包含足够多的工具，能够覆盖所有目标查询。

**第二阶段（贪心选择与注入）**将问题形式化为：在给定注入预算\(B\)下，从候选池\(\mathcal{P}_I\)中选择一个子集\(\mathcal{M}_{adv}\)，最大化被“饱和”的查询数量。一个查询被饱和是指其被至少\(r = k\)个对抗性工具覆盖（即这些工具与查询的余弦距离小于阈值\(\delta\)，在嵌入空间中比大多数良性工具更接近查询）。由于这是NP难的预算最大覆盖问题，论文采用迭代贪心近似算法：初始化对抗工具集为空，并维护剩余查询集\(R\)和每个查询的当前覆盖计数\(c(q)\)。在每一轮中，计算每个候选工具对剩余查询的边际覆盖增益（即能新覆盖多少尚未饱和的查询），选择增益最大的工具加入\(\mathcal{M}_{adv}\)，并更新相关查询的覆盖计数。若查询覆盖计数达到\(r\)，则将其从\(R\)中移除。循环直至预算用尽或剩余查询无法被任何候选工具覆盖。最终选出的工具集即为要注入的对抗性工具。

**关键技术**包括：1) **基于查询子集的条件生成**，利用LLM产生具有广泛语义覆盖性的工具描述；2) **基于余弦距离阈值的覆盖定义**，在代理嵌入空间\(\tilde{\phi}\)中量化工具与查询的语义接近程度；3) **贪心多重覆盖算法**，高效逼近最优注入组合。**创新点**在于首次系统性地攻击工具检索层（而非选择层），通过**语义覆盖**策略实现检索饱和；将攻击形式化为一个**预算约束的多重覆盖优化问题**；并提供了关于候选池收敛性的**理论保证**，确保攻击的有效性。实验表明，即使在低注入率（如ToolBench中1%）下，攻击成功率也可高达95%。

### Q4: 论文做了哪些实验？

实验在标准基准测试MetaTool和ToolBench上进行，评估了ToolFlood攻击在检索层主导和端到端攻击成功率方面的有效性。实验设置遵循固定的三阶段智能体流程：查询→检索→工具选择，其中检索器基于余弦相似度返回top-k候选工具，再由LLM从中选择。数据集方面，MetaTool包含199个良性工具，ToolBench包含11,760个良性工具；每个基准测试定义了10个目标任务，并生成总计1000个语义多样的查询用于评估。

对比方法包括两种检索层攻击基线：Random-Sybil Injection（随机注入攻击）和针对工具场景适配的PoisonedRAG攻击。主要结果以Top-k Domination Rate (TDR) 和 Attack Success Rate (ASR) 为关键指标。在MetaTool上，ToolFlood的TDR达97.2%，ASR在GPT-4o等不同选择器LLM上均接近99%以上；在ToolBench上，TDR为91.0%，ASR约94.6%-96.1%。相比之下，Random-Sybil Injection攻击几乎无效（TDR仅0-1.6%），PoisonedRAG在ToolBench上表现也较弱（TDR 82.0%）。实验还表明，攻击成功率随注入预算增加而单调上升，且在不同嵌入模型间具有良好的可迁移性（例如，用MiniLM优化、在text-embedding-3-small上评估仍保持84% TDR和91.2% ASR）。此外，针对防御措施的测试显示，MMR重排序能降低TDR至44.8%，但ASR仍高达91.0%；而Llama Prompt Guard过滤则完全无效。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于嵌入检索的工具调用系统在安全性上的根本性弱点，即攻击者可通过精心构造的“语义覆盖”工具淹没检索结果。其局限性主要在于：攻击前提是攻击者能向开放工具库中注入大量工具，这在严格审核的私有环境中较难实现；攻击效果依赖于对代理所用嵌入模型的了解，若实际部署采用混合检索或动态学习机制，攻击成功率可能下降；评估场景相对理想，未充分考虑实际系统中可能存在的多信号融合排序、用户行为反馈等复杂防御策略。

未来研究可从攻防两个维度深入。在攻击层面，可探索对黑盒或自适应检索系统的更通用攻击方法，以及研究在有限注入预算下如何实现更高效的语义覆盖。在防御层面，以下几个方向极具潜力：一是设计具有“反西比尔攻击”能力的检索算法，例如引入基于工具功能多样性的重排序机制，避免结果被语义相似的工具簇垄断；二是在检索层开发异常检测模型，实时识别工具描述在嵌入空间中的异常聚集模式；三是构建更强的工具来源认证与治理框架，从源头控制恶意工具注入；四是研究鲁棒性训练目标，使嵌入模型对语义覆盖攻击不敏感，同时保持正常检索效用。此外，将检索过程与任务推理更紧密地结合，发展动态、可解释的工具选择策略，也是提升系统整体韧性的重要途径。

### Q6: 总结一下论文的主要内容

本文提出了一种针对工具增强型LLM代理的新型攻击方法ToolFlood，其核心在于攻击工具检索层而非后续的选择阶段。现有系统通常依赖嵌入检索来选取少量相关工具，但该阶段的鲁棒性研究不足。ToolFlood通过向工具库中注入少量由攻击者控制的工具，精心设计其元数据在嵌入空间中的几何位置，使其语义覆盖大量用户查询，从而垄断检索结果的前k位，将良性工具完全排除在代理的上下文之外。

该方法采用两阶段对抗性工具生成策略：首先采样目标查询子集，利用LLM迭代生成多样化的工具名称和描述；随后进行迭代贪婪选择，在余弦距离阈值下最大化工具对剩余查询在嵌入空间中的覆盖范围，直至覆盖所有查询或达到预算上限。理论分析证明了检索饱和现象，实验表明在标准基准测试中，即使仅注入1%的工具（如在ToolBench中），攻击成功率也可高达95%。这项研究揭示了工具检索系统在规模化时的安全漏洞，强调了在构建可靠LLM代理时需加强检索阶段的防御。
