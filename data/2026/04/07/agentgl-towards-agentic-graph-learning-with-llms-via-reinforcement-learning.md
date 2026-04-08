---
title: "AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning"
authors:
  - "Yuanfu Sun"
  - "Kang Li"
  - "Dongzhe Fan"
  - "Jiajin Liu"
  - "Qiaoyu Tan"
date: "2026-04-07"
arxiv_id: "2604.05846"
arxiv_url: "https://arxiv.org/abs/2604.05846"
pdf_url: "https://arxiv.org/pdf/2604.05846v1"
github_url: "https://github.com/sunyuanfu/AgentGL"
categories:
  - "cs.CL"
tags:
  - "Agent Architecture"
  - "Tool Use"
  - "Reinforcement Learning"
  - "Graph Learning"
  - "Reasoning"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning

## 原始摘要

Large Language Models (LLMs) increasingly rely on agentic capabilities-iterative retrieval, tool use, and decision-making-to overcome the limits of static, parametric knowledge. Yet existing agentic frameworks treat external information as unstructured text and fail to leverage the topological dependencies inherent in real-world data. To bridge this gap, we introduce Agentic Graph Learning (AGL), a paradigm that reframes graph learning as an interleaved process of topology-aware navigation and LLM-based inference. Specifically, we propose AgentGL, the first reinforcement learning (RL)-driven framework for AGL. AgentGL equips an LLM agent with graph-native tools for multi-scale exploration, regulates tool usage via search-constrained thinking to balance accuracy and efficiency, and employs a graph-conditioned curriculum RL strategy to stabilize long-horizon policy learning without step-wise supervision. Across diverse Text-Attributed Graph (TAG) benchmarks and multiple LLM backbones, AgentGL substantially outperforms strong GraphLLMs and GraphRAG baselines, achieving absolute improvements of up to 17.5% in node classification and 28.4% in link prediction. These results demonstrate that AGL is a promising frontier for enabling LLMs to autonomously navigate and reason over complex relational environments. The code is publicly available at https://github.com/sunyuanfu/AgentGL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在处理具有复杂拓扑结构的真实世界数据时，其现有智能体（agentic）框架能力不足的问题。研究背景是，尽管LLMs通过检索增强生成（RAG）和智能体搜索框架，能够迭代查询外部信息以弥补静态参数知识的局限，但现有方法主要将外部信息视为非结构化文本，忽略了现实数据（如引文网络、社交平台）中普遍存在的、以文本属性图（TAGs）形式呈现的内在拓扑依赖关系。这导致仅依赖词法相似性的智能体系统无法有效利用这些结构信息进行推理。

现有方法存在明显不足。传统的图神经网络（GNNs）擅长建模结构信号，但难以处理丰富的文本语义。近期基于LLM的图模型（GraphLLMs）通过图引导提示或指令调优来整合图信息，但其使用的图上下文是静态的、在推理时一次性提取的，无法进行自适应探索。图检索增强生成（GraphRAG）系统从语料库构建大型文本知识图谱，但构建成本高昂，且难以完全保留原始TAG中固有的拓扑关联。总之，现有方法都缺乏在真实图结构上进行动态证据获取的机制。

因此，本文要解决的核心问题是：如何将智能体学习范式扩展到图结构环境中，以实现动态的、拓扑感知的推理，并高效构建这样的系统。具体而言，论文提出了“智能体图学习”（AGL）这一新范式，将图学习重新定义为拓扑感知导航与基于LLM的推理交错进行的过程，并设计了首个基于强化学习（RL）的框架AgentGL来解决其中的两大关键挑战：一是如何在组合空间中进行多尺度的拓扑感知导航，二是如何在没有逐步监督的情况下，优化智能体进行多步探索的长视野决策策略。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**基于LLM的图学习**和**基于外部知识增强的LLM**。

在**基于LLM的图学习**方面，现有工作主要分为两类：一是将局部图结构文本化，以自然语言描述供LLM推理；二是将图结构编码为令牌或嵌入，通过指令微调或上下文学习注入LLM。然而，这些方法本质上是静态的，在推理时无法根据需求动态调整或探索额外证据。本文提出的AgentGL则引入了动态、迭代的智能体范式，通过强化学习驱动的导航与推理来克服这一局限。

在**基于外部知识增强的LLM**方面，标准检索增强生成（RAG）通过静态检索提升事实性，而智能体搜索（如通过强化学习或提示进行迭代推理）则更进一步。但这些方法主要针对非结构化文本。针对结构化数据，GraphRAG方法尝试从图数据中检索证据，但其图常从扁平文本重建，且任务目标与图学习不同。即使是原生图方法（如GraphCoT用于图问答，GraphSearch用于图学习），也大多依赖启发式提示，缺乏优化，导致性能次优。本文的AgentGL与这些工作的核心区别在于，它首次将强化学习系统性地引入图学习智能体框架，通过图感知工具、搜索约束思维和图条件课程学习，实现了在复杂关系环境中长期、稳定且高效的自主导航与推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentGL的强化学习驱动框架来解决LLM在图学习任务中无法有效利用拓扑依赖关系的问题。其核心方法是将图学习重新构建为一个拓扑感知导航与LLM推理交织的过程。

**整体框架与主要模块**：
AgentGL框架围绕两个互补组件组织学习过程：1) **图原生策略引导**，使智能体掌握核心导航行为；2) **搜索效率优化**，在长程推理过程中调节工具使用。这两个组件均在**图条件课程学习**机制下进行训练，以提高稳定性和加速收敛。

**关键技术细节**：
1. **图原生搜索工具集**：设计了四种专门的图搜索工具，覆盖信息空间的两个关键维度（局部vs全局、结构vs语义）：
   - **1-hop/2-hop邻域搜索**：实现精确的局部定位，通过加权融合策略协调拓扑依赖与查询需求。
   - **结构显著性搜索**：作为结构先验，识别拓扑枢纽以指导宏观推理。
   - **图密集搜索**：将RAG中的密集检索范式适配到图上，通过潜在语义关联桥接不相连的节点。

2. **强化学习优化**：采用无评论家的策略优化算法（如GRPO和REINFORCE++）直接优化策略，避免了构建监督式微调数据的高成本。通过设计严格的、机器可解析的交互模板（思考-行动-观察循环），将AGL过程建模为递归状态转移过程。

3. **奖励塑造**：使用复合奖励函数，包括格式奖励（确保模板遵守）、准确率奖励（锚定最终任务）和覆盖奖励（鼓励早期探索所有工具），以提供密集的程序化监督。

4. **搜索约束思维**：在效率优化阶段，引入“多思考、少搜索”范式，通过**回顾性终止触发**和**认知密度正则化**，迫使智能体自主辨别最小充分轨迹，用深度推理替代冗余检索，从而在保证准确性的前提下隐式优化效率。

**创新点**：
- **首创RL驱动的AGL框架**：首次将强化学习应用于图学习的智能体化，使LLM能自主探索图结构。
- **图原生工具设计**：提供了一套专门用于图结构多尺度探索的工具，超越了传统框架将外部信息视为非结构化文本的局限。
- **搜索约束思维机制**：通过认知约束将效率优化转化为对最小充分轨迹的搜索，平衡了准确性与效率。
- **图条件课程学习**：利用图固有的拓扑和语义先验来量化学习难度，实现了从易到难、稳定高效的训练过程，无需逐步监督或昂贵的试点运行。

### Q4: 论文做了哪些实验？

论文在多个文本属性图（TAG）基准上进行了节点分类和链接预测实验。实验设置包括领域内（In-Domain）和零样本迁移（Zero-shot Transfer）两种场景。使用的数据集涵盖OGB-Arxiv、OGB-Products、PubMed、Amazon-Photo、Amazon-Computers、Arxiv-23和Reddit。对比方法分为两大类：基于GNN的方法（如GCN、RevGAT、SAGE）和基于LLM的方法，后者进一步细分为GraphLLMs（如GraphPrompter、GraphGPT、LLaGA、GraphICL）和GraphRAG方法（如LinearRAG、HippoRAG2、GraphCoT），以及纯LLM推理（Qwen2.5）和搜索基线（Search-R1/O1）。AgentGL提出了两种强化学习变体：AgentGL-R++和AgentGL-GRPO。

主要结果显示，AgentGL在多个数据集和任务上显著优于所有基线。关键数据指标上，在节点分类任务中，使用Qwen2.5-3B时，AgentGL在OGB-Arxiv上达到66.9%（绝对提升最高达17.5%以上）；在链接预测任务中，在OGB-Arxiv上达到92.3%（绝对提升最高达28.4%）。使用更大的7B骨干模型时，性能进一步提升，例如在OGB-Products链接预测上达到97.4%。消融实验验证了其图原生搜索策略（GNSPB）和多尺度探索（MSO）组件的有效性，表明它们能平衡搜索效率与精度。

### Q5: 有什么可以进一步探索的点？

该论文在将LLM与图学习结合方面取得了显著进展，但其探索仍处于初期阶段，存在多个可深入挖掘的方向。首先，**计算效率与可扩展性**是核心局限：当前方法依赖LLM的多次调用和强化学习训练，成本高昂，难以应用于大规模动态图。未来可探索轻量级策略网络或知识蒸馏技术，将LLM的推理能力迁移至更高效的模型中。其次，**泛化能力与领域适配**有待加强：实验集中于文本属性图（TAG），未来需验证其在异质图、时空图或缺乏文本信息的结构数据上的表现，并研究如何减少对特定图结构的依赖。此外，**训练稳定性与奖励设计**可进一步优化：尽管采用了课程强化学习，但长周期决策的稀疏奖励问题依然存在；未来可结合逆强化学习或引入更精细的中间奖励信号（如局部结构一致性）。最后，**多模态与工具扩展**是重要方向：当前工具集中于图结构探索，未来可整合视觉、时序等多模态工具，使智能体能够处理更复杂的现实环境（如社交网络动态、生物分子图），真正实现“感知-推理-决策”的闭环。

### Q6: 总结一下论文的主要内容

该论文提出了Agentic Graph Learning（AGL）这一新范式，旨在将大语言模型（LLMs）的智能体能力与图结构数据相结合。核心问题是现有基于LLM的智能体框架主要处理非结构化文本，无法有效利用现实世界数据中固有的拓扑依赖关系，而传统的图学习方法（如GNNs或静态提示的GraphLLMs）又难以实现动态、自适应的图探索与推理。

为此，论文提出了首个基于强化学习（RL）的AGL框架——AgentGL。其方法主要包括：1）为LLM智能体配备一套支持多尺度探索的图原生搜索工具（如局部邻域扩展、跳数约束遍历）；2）引入“搜索约束思维”机制，鼓励智能体在发起新查询前进行深度推理，以平衡准确性与效率；3）设计一种图条件课程RL策略，通过逐步增加探索难度、整合多维度奖励，在无需逐步监督的情况下稳定地优化长视野决策策略。

主要结论显示，在多个文本属性图（TAG）基准测试和不同LLM骨干网络上，AgentGL在节点分类和链接预测任务上显著优于现有的GraphLLM和GraphRAG基线模型，绝对性能提升最高分别达到17.5%和28.4%。这证明了AGL是使LLMs能够自主导航和推理复杂关系环境的一个有前景的新方向。
