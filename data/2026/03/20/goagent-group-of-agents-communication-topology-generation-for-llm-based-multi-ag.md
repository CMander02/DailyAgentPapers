---
title: "GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems"
authors:
  - "Hongjiang Chen"
  - "Xin Zheng"
  - "Yixin Liu"
  - "Pengfei Jiao"
  - "Shiyuan Li"
  - "Huan Liu"
  - "Zhidong Zhao"
  - "Ziqi Xu"
  - "Ibrahim Khalil"
  - "Shirui Pan"
date: "2026-03-20"
arxiv_id: "2603.19677"
arxiv_url: "https://arxiv.org/abs/2603.19677"
pdf_url: "https://arxiv.org/pdf/2603.19677v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Communication Topology"
  - "LLM-based Agents"
  - "Group Collaboration"
  - "Information Bottleneck"
  - "Autoregressive Generation"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems

## 原始摘要

Large language model (LLM)-based multi-agent systems (MAS) have demonstrated exceptional capabilities in solving complex tasks, yet their effectiveness depends heavily on the underlying communication topology that coordinates agent interactions. Within these systems, successful problem-solving often necessitates task-specific group structures to divide and conquer subtasks. However, most existing approaches generate communication topologies in a node-centric manner, leaving group structures to emerge implicitly from local connectivity decisions rather than modeling them explicitly, often leading to suboptimal coordination and unnecessary communication overhead. To address this limitation, we propose GoAgent (Group-of-Agents), a communication topology generation method that explicitly treats collaborative groups as the atomic units of MAS construction. Specifically, GoAgent first enumerates task-relevant candidate groups through an LLM and then autoregressively selects and connects these groups as atomic units to construct the final communication graph, jointly capturing intra-group cohesion and inter-group coordination. To mitigate communication redundancy and noise propagation inherent in expanding topologies, we further introduce a conditional information bottleneck (CIB) objective that compresses inter-group communication, preserving task-relevant signals while filtering out redundant historical noise. Extensive experiments on six benchmarks demonstrate the state-of-the-art performance of GoAgent with 93.84% average accuracy while reducing token consumption by about 17%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统中通信拓扑结构生成的关键问题。研究背景是，多智能体系统在解决复杂任务方面展现出强大潜力，但其效能高度依赖于协调智能体交互的底层通信拓扑。现有方法大多采用节点中心范式，即逐个添加智能体并预测其连接，这种方式存在明显不足：首先，它无法显式建模任务所需的协作群组结构（如分解、求解、验证等角色组成的紧密团队），导致宏观协作流程割裂、协调效率低下；其次，由于缺乏明确的群组边界，生成的拓扑往往连接过于密集，不仅带来大量冗余通信开销，还使得任务无关的历史噪声在智能体间传播，干扰关键信息。因此，本文的核心问题是：能否超越节点中心范式，采用更高层次的抽象来设计通信拓扑，以显式捕获和利用协作群组结构？为此，论文提出GoAgent方法，将协作群组作为构建的基本单元，首先生成任务相关的候选群组，然后自回归地选择并连接这些群组来构建通信图，同时引入条件信息瓶颈来压缩群组间通信，从而在提升任务解决能力的同时显著降低通信成本。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：LLM驱动的多智能体系统和面向群组的图生成方法。

在**LLM驱动的多智能体系统**方面，早期工作如链式结构依赖静态通信拓扑。后续的模板化方法（如G-Designer、AgentPrune、AgentDropout）通过剪枝预定义图来优化拓扑，实现了自适应通信。更近期的ARG-Designer则完全绕过模板，以自回归方式从头构建拓扑。然而，所有这些方法都是**节点中心**的，将单个智能体视为原子单元，难以显式捕捉协作所需的群组结构，且易产生冗余通信边。本文提出的GoAgent与这些工作的核心区别在于，它将**协作群组**而非单个智能体作为构建系统的基本原子单元，从而更直接地建模任务所需的团队结构。

在**面向群组的图生成**方面，图表示学习领域的研究已指出节点中心方法在可扩展性和结构一致性上的局限。相关工作包括显式建模宏观子图再建立微观连接的层次化网络、结合全局与局部约束以确保结构有效性的基于扩散的方法，以及证明通过高阶单元生成图可提升效率与保真度的可扩展框架。本文借鉴了这些高阶范式的思想，但将其创新性地应用于多智能体系统领域。GoAgent通过LLM推导出的候选群组作为构建块，显式地捕获了群组内聚性与群组间协调性，这是与通用图生成方法在**应用目标**上的关键区别。此外，本文还引入了条件信息瓶颈目标来压缩群组间通信，以进一步减少冗余和噪声，这是针对多智能体通信场景的特定优化。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为GoAgent的组级通信拓扑生成方法来解决现有节点中心方法中存在的隐式群组结构导致协调不佳和通信开销过大的问题。其核心思想是将协作群组作为多智能体系统构建的原子单元，显式地建模群组内聚力和群组间协调。

整体框架是一个四阶段的自动回归生成管道。首先，通过任务编码器将任务查询编码为全局任务表示。其次，利用大语言模型（如GPT-4）枚举出K个与任务相关的候选协作群组，每个群组都有预定义的结构化模式（名称、专长、角色、内部拓扑），其文本描述被编码为候选嵌入矩阵。生成过程的核心是自动回归循环：在每一步t，模型基于当前图状态（由先前生成的群组序列通过GRU聚合的历史状态）和全局任务表示（通过动态门控融合），预测下一个要添加的群组M_t以及从现有群组到M_t的入边。

关键技术创新主要体现在两个方面。第一是引入了条件信息瓶颈（CIB）层，以压缩历史通信信号并过滤冗余噪声。CIB层从原始特征（群组特征或边特征）中提取压缩的潜在表示c，通过优化一个目标函数来实现：最小化一个预测项（确保c保留预测目标y的足够信息）和一个压缩项（限制噪声历史信息的流动）。与标准变分信息瓶颈不同，这里引入了任务条件先验p(c|z_Q)，认为不同任务类型需要不同的基线拓扑结构。这通过一个KL散度项实现正则化，迫使表示c在保留任务相关信息的同时，丢弃与任务无关的噪声。第二是采用了一种以群组为中心的生成范式，将拓扑生成分解为群组选择和边预测的序列，这显著减少了搜索空间，并更好地对齐了类似人类的组织结构。

训练方面，论文通过自动启发式探索过程构建了包含任务-最优图对的数据集，并使用教师强制进行端到端监督训练。总损失函数结合了群组预测的负对数似然、边预测的二元交叉熵以及应用于群组和边层面的KL散度正则项。推理时，模型根据新任务查询，以确定性的方式自动回归生成最终的群组级通信图。

### Q4: 论文做了哪些实验？

论文在六个基准测试上进行了实验，包括通用推理（MMLU）、数学推理（GSM8K、MultiArith、SVAMP、AQuA）和代码生成（HumanEval）。实验设置上，主要使用GPT-4o模型，通过OpenAI API访问，并设置最大交互轮数为3。组编码器采用all-MiniLM-L6-v2模型，嵌入维度为384。训练时仅使用40或60个查询，并采用线性预热策略调整条件信息瓶颈（CIB）的超参数。

对比方法涵盖三类：单智能体基线（如Vanilla、CoT、Self-Consistency）、固定拓扑的多智能体系统（如Chain、Tree、Complete graph、Random graph、LLM-Debate）以及可学习拓扑的方法（如AgentPrune、AgentDropout、G-Designer、EIB-LEARNER、ARG-Designer）。主要结果显示，GoAgent在六个基准上均取得了最优性能，平均准确率达到93.84%，较最佳基线（ARG-Designer的92.62%）提升1.22个百分点。具体指标上，在MMLU达到91.50%（提升1.96%），HumanEval达到94.21%（提升2.47%）。同时，GoAgent显著降低了通信开销，令牌消耗比最优基线减少约17%。

消融实验验证了关键组件的贡献：移除组级生成（w/o Group）或CIB层（w/o CIB）均导致性能下降，例如在MMLU上分别下降2.61%和3.27%。此外，实验还评估了效率与鲁棒性：在令牌消耗方面，GoAgent在MMLU和GSM8K上均低于密集拓扑方法；在对抗提示注入攻击时，GoAgent保持了89.54%的准确率，显示出更强的鲁棒性。案例研究进一步表明，GoAgent能生成更简洁、高效的协作图，减少冗余通信。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于预定义协作群组池限制了动态灵活性，以及评估场景集中于静态推理任务。未来可探索的方向包括：首先，引入在线群组生成机制，结合强化学习或元学习，使系统能在推理过程中动态合成新群组，以应对未预见的任务需求。其次，将方法扩展到动态交互环境（如具身AI或多智能体强化学习），研究群组拓扑在实时协作中的适应性，可能需结合环境反馈优化通信压缩。此外，可探索跨任务群组迁移学习，提升泛化能力；或引入分层通信机制，进一步减少冗余，平衡组内凝聚与组间协调的效率。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的多智能体系统中通信拓扑结构生成问题，提出了一种名为GoAgent的新方法。现有方法通常以节点为中心生成拓扑，导致隐含形成的群组结构可能不协调且通信开销大。GoAgent的核心贡献在于采用以群组为中心的设计范式，将协作群组视为构建多智能体系统的基本原子单元。方法首先通过大语言模型枚举与任务相关的候选群组，然后以自回归方式将这些群组作为原子单元进行选择和连接，以构建最终的通信图，从而同时捕获群组内聚力和群组间协调。为了减少拓扑扩展中固有的通信冗余和噪声传播，论文进一步引入了条件信息瓶颈目标来压缩群组间通信，保留任务相关信号并过滤冗余的历史噪声。在六个基准测试上的实验表明，GoAgent实现了最先进的性能（平均准确率93.84%），同时将令牌消耗降低了约17%，显著提升了结构鲁棒性并减少了通信开销。
