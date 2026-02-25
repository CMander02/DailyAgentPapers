---
title: "HieraMAS: Optimizing Intra-Node LLM Mixtures and Inter-Node Topology for Multi-Agent Systems"
authors:
  - "Tianjun Yao"
  - "Zhaoyi Li"
  - "Zhiqiang Shen"
date: "2026-02-23"
arxiv_id: "2602.20229"
arxiv_url: "https://arxiv.org/abs/2602.20229"
pdf_url: "https://arxiv.org/pdf/2602.20229v1"
categories:
  - "cs.MA"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "LLM混合"
  - "通信拓扑"
  - "强化学习"
  - "信用分配"
  - "角色分配"
  - "系统优化"
relevance_score: 9.5
---

# HieraMAS: Optimizing Intra-Node LLM Mixtures and Inter-Node Topology for Multi-Agent Systems

## 原始摘要

Multi-agent systems (MAS) built on large language models (LLMs) have shown strong performance across many tasks. Most existing approaches improve only one aspect at a time, such as the communication topology, role assignment, or LLM routing, while treating each agent as a single, indivisible unit. This misses the opportunity to use mixtures of LLMs within an agent to strengthen role-specific abilities. We propose HieraMAS, a hierarchical collaboration framework that combines intra-node LLM mixtures with an inter-node communication topology. HieraMAS introduces supernodes, where each functional role is implemented by multiple heterogeneous LLMs using a propose-synthesis structure. Optimizing HieraMAS creates unique credit-assignment challenges: final task performance depends heavily on the underlying LLMs' capabilities, which can lead reinforcement methods to incorrectly reward suboptimal configurations. To address this, we use a two-stage algorithm: (1) multi-level reward attribution, which provides fine-grained feedback at both the node level and the overall system level; (2) graph classification for topology selection, which treats choosing the communication structure as a holistic decision rather than optimizing edges one by one. Experiments on reasoning and coding benchmarks show that HieraMAS substantially outperforms existing methods while also delivering better cost-performance trade-offs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的多智能体系统（MAS）研究中存在的局限性问题。研究背景是，现有方法通常孤立地优化系统的某个单一维度，例如智能体间的通信拓扑、角色分配或LLM路由选择，而将每个智能体视为一个不可分割的单一LLM单元。这种做法忽略了在单个智能体（角色）内部利用多个异构LLM进行协作，以增强其特定角色能力的巨大潜力。现有方法的不足在于，它们未能有效整合LLM本身具有的“协作性”——即一个LLM在接收其他模型输出作为辅助输入时能产生更好响应的现象，与多智能体系统固有的协作范式相结合。

因此，本文要解决的核心问题是：如何设计一个统一框架，以协同优化多智能体系统的内部构成与外部结构，从而全面提升系统性能与效率。具体而言，论文提出了HieraMAS框架，其核心创新在于引入了“超级节点”的概念。每个超级节点代表一个功能角色，但其内部由多个异构LLM以“提议-合成”结构协同工作，实现了节点内的LLM混合协作。在此基础上，论文需要联合优化三个相互关联的维度：超级节点间的通信拓扑、需要保留的功能角色（角色剪枝）以及每个超级节点内部的LLM选择。这带来了独特的信用分配挑战：最终任务奖励会掩盖单个节点的错误，且逐边优化通信拓扑会面临贡献纠缠问题。为此，论文提出了两阶段算法来解决这些核心优化难题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多智能体系统（MAS）的优化维度展开，可分为以下几类：

**1. 通信拓扑学习**：这类工作专注于优化智能体间的信息流结构，例如通过强化学习调整连接边。本文的HieraMAS同样优化拓扑，但将其视为整体图分类任务，而非逐边优化，以避免贡献分配纠缠问题。

**2. 角色分配与专业化**：研究如何为智能体分配不同的功能职责，以提升系统效率。本文在此基础上引入了“超节点”概念，每个功能角色内部由多个异构LLM通过提议-合成结构实现，从而增强了角色特定能力，这是与将智能体视为单一单元的传统方法的根本区别。

**3. LLM路由与选择**：这类工作旨在为不同智能体角色选择合适的骨干模型，以权衡成本与能力。本文的优化维度包含了超节点内部的LLM选择，但其创新点在于将节点内部LLM混合与节点间拓扑进行联合优化。

此外，研究还观察到LLM在接收其他模型输出作为辅助输入时表现更好的现象，这为MAS中的LLM协作提供了新视角，但现有工作未有效整合这种协作性。HieraMAS则统一了这两种协作形式，构建了一个层次化协作框架。

与上述通常只优化单一维度的现有方法不同，HieraMAS的核心贡献在于**联合优化**了节点内配置（LLM混合与角色保留）和节点间结构（通信拓扑），并设计了相应的两级算法（多级奖励归因和拓扑图分类）来解决由此带来的复杂信用分配挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HieraMAS的分层协作框架来解决多智能体系统中联合优化节点内LLM组合与节点间通信拓扑的挑战。其核心方法是一个两阶段训练算法，旨在解决因最终任务性能与底层LLM能力深度耦合而产生的独特信用分配难题。

**整体框架与主要模块：**
HieraMAS框架的核心是引入了**超级节点**的概念。每个超级节点对应一个功能角色（如规划者、执行者、评审者），但其内部并非单一LLM，而是采用“提议-合成”结构：包含多个**提议者**LLM和一个**合成器**LLM。给定查询时，框架分两步构建定制化MAS：1) 为每个超级节点内的各个位置选择最优LLM；2) 选择合适的超级节点间通信拓扑图。

框架包含两个关键学习模块：
1.  **LLM选择器**：一个策略学习器，根据查询和角色描述，计算为每个位置选择候选LLM池中某个模型（包括一个特殊的“跳过”令牌）的概率。选择“跳过”令牌可以实现自适应剪枝：在提议者位置选择则省略该提议者以降低开销；在合成器位置选择则停用整个超级节点，从而动态调整MAS的组成和规模。
2.  **图分类器**：将拓扑选择视为一个整体的图分类问题，而非逐边优化。系统预先生成一个包含K个随机有向无环图的多样化候选池。对于每个查询和候选图（由其邻接矩阵表示），图分类器通过图卷积网络处理节点特征（由角色嵌入和查询嵌入拼接而成），聚合得到图级表示，并输出一个适合度分数。推理时选择分数最高的拓扑。

**创新点与两阶段训练算法：**
为解决信用分配挑战，论文提出了创新的两阶段训练算法：
*   **第一阶段：优化超级节点内的LLM配置**。此阶段使用随机采样的图拓扑，重点训练LLM选择器。其关键创新在于**多级奖励机制**。除了系统最终输出的奖励，还为每个超级节点计算一个节点级奖励（通过评估其合成器输出得到）。有效奖励是两者的加权和，这为每个节点提供了细粒度的反馈，防止系统级成功掩盖个别节点的失败。奖励函数本身是成本感知的，在鼓励正确性的同时惩罚高计算成本。
*   **第二阶段：优化节点间通信拓扑**。冻结第一阶段训练好的LLM选择器，然后训练图分类器。通过使用固定的LLM选择器、以不同的候选图执行MAS来生成训练数据，并根据获得的奖励为拓扑图打标签（高奖励图为正例）。图分类器通过二元交叉熵损失进行训练，学习预测拓扑图的适合度。

这种解耦的两阶段设计具有多重优势：避免了在联合优化中直接进行困难的逐边信用分配；通过将拓扑选择转化为整体图分类问题，使其成为一个定义良好的估计问题；并且利用优化后的LLM选择器为图分类器提供有意义的训练信号。实验表明，该方法在推理和编码基准测试上显著优于现有方法，并实现了更好的成本-性能权衡。

### Q4: 论文做了哪些实验？

论文在推理和代码生成任务上进行了全面的实验评估。实验设置方面，作者使用了包含多种异构大语言模型（LLM）的模型池，包括Qwen3、DeepSeek、Llama、Gemma和GPT系列模型，并通过开放API调用。实验分为两种主要设置：一种是基于GPT-5-Mini，另一种是基于Qwen3-Next-80B-A3B-Instruct。对于支持学习型LLM选择的方法（如HieraMAS和MASRouter），在GPT-5-Mini设置下使用模型池中的所有LLM，在Qwen3-80B设置下则排除所有GPT模型。

评估使用了三个基准数据集：HumanEval++（代码生成，报告Pass@1）、MATH（数学推理，报告准确率）和MMLU-Redux（综合知识，报告准确率）。对比方法涵盖单智能体方法（如Base、CoT）、固定多智能体方法（如Self-Consistency、LLM-Debate、Full-Graph、Random-Graph）以及学习型多智能体方法（AFlow、GDesigner、MASRouter）。

主要结果显示，HieraMAS在平均性能上达到94.61%，显著优于基线。具体而言，在HumanEval++上取得最佳性能，在MATH上表现最优，在MMLU-Redux上获得有竞争力的结果。关键数据指标包括：在MMLU-Redux上，HieraMAS成本为1.29美元，而全连接图（Full-Graph）成本为4.23美元，后者贵3.27倍；在HumanEval++上，HieraMAS的训练成本比AFlow低18.41倍。消融实验表明，移除图评分机制（w/o Graph）导致MATH准确率下降3.45%，MMLU-Redux下降3.36%；移除LLM选择（w/o LLM Selection）虽在MATH上略有提升，但成本显著增加（2.56美元 vs. 1.52美元），且在MMLU-Redux上成本增加203.9%的同时准确率更低。此外，对学习到的拓扑结构分析显示，其密度比在0.23到0.32之间，远低于全连接图（密度=1.0），且角色如心理学家和医生常作为汇聚节点，批评家和经济学家常作为源节点，体现了稀疏、不规则的高效结构。

### Q5: 有什么可以进一步探索的点？

该论文提出的HieraMAS框架虽在多智能体协作上取得进展，但仍存在若干局限和可拓展方向。首先，其两阶段优化算法依赖预定义的奖励函数和拓扑分类器，可能无法充分适应动态或开放域任务，未来可探索在线学习机制，使系统能根据实时反馈调整内部模型混合与通信结构。其次，实验集中于推理和编码等结构化任务，未涉及更复杂的现实场景（如长期规划或不确定环境下的决策），需在更具挑战性的环境中验证泛化能力。此外，框架假设智能体角色固定，但实际任务中角色可能需要动态重组，可研究如何引入元学习或课程学习策略，让智能体自主演化角色定义与协作模式。从工程角度看，当前方法对异构大语言模型（LLM）的依赖可能带来高昂计算成本，未来可探索轻量化模型替代方案或蒸馏技术，在保持性能的同时提升效率。最后，信用分配机制虽有多层奖励，但未考虑跨节点协作中的长期依赖，结合注意力机制或因果建模来细化贡献评估，可能是值得深入的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为HieraMAS的分层协作框架，旨在优化多智能体系统（MAS）的性能。现有方法通常将每个智能体视为单一不可分割单元，仅优化通信拓扑、角色分配或LLM路由等单一方面，而忽略了在单个智能体内混合使用不同大语言模型（LLM）以增强角色特定能力的机会。

HieraMAS的核心贡献在于同时优化节点内LLM混合与节点间通信拓扑。它引入了“超级节点”概念，每个功能角色由多个异构LLM通过“提议-合成”结构共同实现。为解决由此产生的独特信用分配挑战（即最终任务表现高度依赖底层LLM能力，可能导致强化学习方法错误奖励次优配置），论文提出了两阶段优化算法：第一阶段采用多级奖励归因，在节点级别和系统整体级别提供细粒度反馈；第二阶段使用图分类进行拓扑选择，将通信结构的选择视为整体决策而非逐边优化。

实验结果表明，在推理和编码基准测试中，HieraMAS显著优于现有方法，同时实现了更好的成本-性能权衡。该工作的重要意义在于突破了传统多智能体系统的设计局限，通过层次化协同设计为构建更高效、更强大的LLM多智能体系统提供了新范式。
