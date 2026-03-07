---
title: "AgentSelect: Benchmark for Narrative Query-to-Agent Recommendation"
authors:
  - "Yunxiao Shi"
  - "Wujiang Xu"
  - "Tingwei Chen"
  - "Haoning Shang"
  - "Ling Yang"
date: "2026-03-04"
arxiv_id: "2603.03761"
arxiv_url: "https://arxiv.org/abs/2603.03761"
pdf_url: "https://arxiv.org/pdf/2603.03761v1"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "AgentSelect benchmark (narrative query-to-agent recommendation over capability profiles)"
  primary_benchmark: "AgentSelect"
---

# AgentSelect: Benchmark for Narrative Query-to-Agent Recommendation

## 原始摘要

LLM agents are rapidly becoming the practical interface for task automation, yet the ecosystem lacks a principled way to choose among an exploding space of deployable configurations. Existing LLM leaderboards and tool/agent benchmarks evaluate components in isolation and remain fragmented across tasks, metrics, and candidate pools, leaving a critical research gap: there is little query-conditioned supervision for learning to recommend end-to-end agent configurations that couple a backbone model with a toolkit. We address this gap with AgentSelect, a benchmark that reframes agent selection as narrative query-to-agent recommendation over capability profiles and systematically converts heterogeneous evaluation artifacts into unified, positive-only interaction data. AgentSelectcomprises 111,179 queries, 107,721 deployable agents, and 251,103 interaction records aggregated from 40+ sources, spanning LLM-only, toolkit-only, and compositional agents. Our analyses reveal a regime shift from dense head reuse to long-tail, near one-off supervision, where popularity-based CF/GNN methods become fragile and content-aware capability matching is essential. We further show that Part~III synthesized compositional interactions are learnable, induce capability-sensitive behavior under controlled counterfactual edits, and improve coverage over realistic compositions; models trained on AgentSelect also transfer to a public agent marketplace (MuleRun), yielding consistent gains on an unseen catalog. Overall, AgentSelect provides the first unified data and evaluation infrastructure for agent recommendation, which establishes a reproducible foundation to study and accelerate the emerging agent ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体（Agent）生态系统中一个日益突出的实际问题：面对爆炸式增长的、可部署的智能体配置选项（如不同的骨干模型、工具集和运行时策略的组合），用户或开发者缺乏一种原则性的方法来为特定的、自然语言描述的叙事性查询（narrative query）选择最合适的端到端智能体配置。现有方法存在明显不足：虽然已有众多针对LLM能力的排行榜和针对工具/智能体的基准测试，但它们通常孤立地评估各个组件（如单独评估模型或工具），并且在任务、评估指标和候选池方面高度碎片化。这导致了一个关键的研究空白：缺乏以查询为条件的监督信号，来学习如何推荐将骨干模型与工具包耦合的完整智能体配置。本文的核心问题正是填补这一空白，将智能体选择问题形式化为一个基于能力配置的、叙事性查询到智能体的推荐任务，并为此构建一个统一的基准测试和数据集（AgentSelect），将异构的评估数据系统性地转化为标准化的、仅包含正向交互的监督数据，以支持数据驱动的智能体推荐模型的学习与评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、组件选择方法和代理推荐任务。

在**评测基准**方面，现有工作包括专注于问答能力的LLM排行榜（如Open LLM Leaderboard）、评估工具使用能力的工具增强评测（如APIBench、ToolBench），以及衡量复杂任务完成度的代理中心排行榜。然而，这些评测通常将结果视为孤立的诊断终点，指标和格式各异。本文的AgentSelect则首次提供了一个统一框架，将异构的评测结果系统性地转化为用于代理推荐的结构化偏好信号，从而超越了传统的诊断角色，具备了指导选择的处方价值。

在**组件选择方法**方面，相关研究包括：1) **LLM路由**：旨在为给定任务选择合适的骨干模型，以优化质量-成本-延迟权衡（如RouterBench、OmniRouter）；2) **工具检索与模块化工具服务**：从大型工具库中检索与查询相关的工具（如ToolRet、RAG-MCP），并涉及工具表示学习等。这些工作分别针对代理的两个核心组件（骨干模型和工具集）进行选择。

本文与上述工作的关系和区别在于：现有的路由和工具检索方法能有效缩小组件搜索空间，但并未直接解决本文研究的**端到端代理推荐任务**。本文首次将代理选择形式化为基于能力描述的叙事查询到代理的推荐问题，并构建了一个大规模基准，将现有评测数据转化为统一的、仅含正例的监督信号，用于学习推荐可直接部署的完整代理配置。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AgentSelect的基准测试来解决LLM智能体推荐问题，其核心方法是将智能体选择重新定义为基于能力配置的叙事查询到智能体的推荐任务，并系统性地将异构评估数据转化为统一的、仅包含正向交互的数据集。

整体框架分为三个主要部分，对应三种智能体类型的数据构建与整合：
1.  **仅含骨干模型（LLM-only）的智能体（Part I）**：从Open LLM Leaderboard等大规模LLM评估中提取模型选择偏好。具体地，将每个查询中排名前10的模型视为正向交互。为确保稳定性和实用性，论文将模型范围限定在知名机构发布的173个模型。对于仅提供数据集级别分数的评估，通过构建覆盖均衡的核心查询集，并将数据集级别的模型排序转化为查询级别的弱监督信号。
2.  **仅含工具集（Toolkit-only）的智能体（Part II）**：从现有的工具使用基准（如ToolHop、UltraTool）中提取工具充分性证据。对于每个查询，构建一个骨干模型为占位符、工具集为基准指定参考工具包的智能体作为正向目标，从而隔离工具集的作用。
3.  **组合式智能体（Part III）**：这是关键的创新部分，旨在弥补前两部分数据缺乏实际端到端配置的不足。它通过一个三阶段流水线合成组合式智能体及其交互：
    *   **查询选择**：从Part I和II中选择一组覆盖均衡的原型查询。
    *   **组件检索与组合**：使用在Part I/II上训练的轻量级检索器，分别为每个查询检索可能匹配的骨干LLM短列表和所需工具集短列表，然后将它们组合成一系列`(M, T)`智能体配置，构成该查询的候选池。
    *   **交互模拟**：将为当前查询合成的配置视为伪正向交互，而为其他查询合成的配置则视为未标记（在隐式反馈设定下作为负例处理）。

**架构设计与关键技术**：
*   **智能体表示**：将每个可部署的智能体抽象为一个能力配置`A = (M, T)`，其中`M`是骨干语言模型，`T`是可调用的外部工具集。这是实现跨框架、可比较和可复现推荐的最小核心抽象。每个智能体还存储为包含完整配置`(M, T, C)`的YAML文件以确保可运行性，但基准测试和学习的核心聚焦于`(M, T)`。
*   **数据统一与构建**：核心创新在于将来自40多个源的异构社区评估成果（如排行榜、工具基准）系统地转化为统一的“查询-智能体”交互格式。这避免了从头标注，并允许基准随新评估成果的出现而扩展。
*   **处理数据稀疏性与长尾分布**：分析表明，数据分布存在从Part I的密集重复使用到Part II/III的极度稀疏长尾的机制转变。这要求推荐方法不能依赖基于流行度的协同过滤，而必须进行基于内容（能力）的匹配。Part III的合成交互正是为了增强对现实组合的覆盖和学习能力。

**创新点**：
1.  **问题重构**：首次将智能体选择系统地定义为叙事查询到能力配置的推荐任务。
2.  **基准构建方法论**：提出了一个将分散、异构的评估数据转化为统一、仅含正向交互的推荐数据集的创新流程，特别是通过合成方法创建了稀缺的组合式智能体交互数据（Part III）。
3.  **可操作性与可复现性**：智能体以可运行的YAML配置表示，确保了推荐结果的可部署性，并为研究提供了可复现的基础设施。
4.  **揭示关键挑战**：通过数据分析揭示了智能体推荐场景中从密集头部分布到稀疏长尾分布的机制转变，强调了能力匹配的重要性，为未来研究指明了方向。

### Q4: 论文做了哪些实验？

论文的实验设置基于AgentSelect基准，该基准包含111,179个查询、107,721个可部署智能体和251,103条交互记录，涵盖LLM-only、工具包-only和组合智能体三类。数据集分为三个部分：Part I（密集重复交互）、Part II（工具包-only）和Part III（合成的组合交互）。实验在NVIDIA A40 GPU上使用PyTorch 2.2.2和Transformers 4.48.1进行，采用统一的特征集（查询内容、模型内容、工具内容、模型ID和工具ID），并报告Precision@10、Recall@10、F1@10、nDCG@10和MRR@10等指标，结果基于五次随机种子的平均值。

对比方法涵盖六类推荐和检索范式：交互式潜在因子模型（如MF、LightFM）、内容感知匹配模型（如NCF、双塔架构）、基于图的传播方法（如NGCF、KGAT、LightGCN、SimGCL）、嵌入检索与重排方法（如BGE-Reranking、KaLM、EasyRec）以及生成式推荐器OneRec。关键结果包括：在Part I中，基于交互的方法（如MF的nDCG@10为0.9339）表现优异；而在Part II和Part III中，内容感知模型（如双塔架构使用BGE-M3嵌入在Part III的nDCG@10达0.8501）更稳健，凸显了在长尾、近一次性监督下语义匹配的重要性。此外，模态归因实验表明，文本内容（而非ID）是能力匹配的主要驱动力（如移除ID后Part III的nDCG@10仅从0.9344降至0.9260）。反事实编辑验证了模型对能力变化的敏感性（如移除关键工具的一致性达64%）。最后，在真实世界验证中，基于AgentSelect微调的EasyRec*在MuleRun数据集上优于原始版本（如nDCG@10从0.5491提升至0.5870），证明了其可迁移性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其数据主要源于现有评估结果聚合，缺乏真实用户与复杂多轮交互的细粒度数据，这可能导致推荐模型对动态、上下文敏感的代理选择场景泛化能力不足。未来研究可探索如何整合在线学习机制，使推荐系统能根据用户反馈实时调整；同时，需设计更细粒度的能力评估维度（如计算效率、成本敏感性），以支持多目标优化。结合见解，改进思路可包括：引入合成数据生成技术，模拟长尾查询与代理的交互，以缓解数据稀疏性；开发基于因果推理的推荐框架，区分代理能力与任务需求的本质关联，减少混杂偏差；并探索跨平台、跨模态的代理统一表征学习方法，提升推荐系统的可迁移性与鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了AgentSelect基准，旨在解决LLM智能体生态中缺乏系统性方法为特定叙事查询推荐合适智能体配置的问题。核心贡献是将智能体选择重新定义为基于能力配置的查询到智能体推荐任务，并构建了一个统一的大规模数据集。方法上，论文将候选智能体视为可部署的能力配置，通过整合40多个来源的异构评估数据，系统性地构建了包含三个部分（仅LLM、仅工具包、组合智能体）的交互记录，形成了正样本监督信号。主要结论显示，数据呈现从密集头部重用到长尾近一次性监督的机制转变，使得基于内容的智能体能力匹配方法优于传统的协同过滤方法；同时，合成的组合交互数据是可学习的，并能迁移到真实智能体市场，提升推荐效果。该研究为智能体推荐提供了首个统一的数据与评估基础设施，对加速智能体生态发展具有重要意义。
