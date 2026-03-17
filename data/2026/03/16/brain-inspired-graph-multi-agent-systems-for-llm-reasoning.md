---
title: "Brain-Inspired Graph Multi-Agent Systems for LLM Reasoning"
authors:
  - "Guangfu Hao"
  - "Yuming Dai"
  - "Xianzhe Qin"
  - "Shan Yu"
date: "2026-03-16"
arxiv_id: "2603.15371"
arxiv_url: "https://arxiv.org/abs/2603.15371"
pdf_url: "https://arxiv.org/pdf/2603.15371v1"
categories:
  - "cs.AI"
  - "cs.NI"
tags:
  - "多智能体系统"
  - "推理"
  - "图结构"
  - "架构设计"
  - "全局工作空间理论"
  - "基准测试"
relevance_score: 8.5
---

# Brain-Inspired Graph Multi-Agent Systems for LLM Reasoning

## 原始摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of language tasks, yet complex multi-step reasoning remains a fundamental challenge. While Large Reasoning Models (LRMs) equipped with extended chain-of-thought mechanisms demonstrate improved performance over standard LLMs, both model types still suffer from accuracy collapse on sufficiently complex tasks, suggesting that scaling model-level reasoning alone is insufficient. Inspired by the global workspace theory of human cognition, we propose Brain-Inspired Graph Multi-Agent Systems (BIGMAS), in which specialized LLM agents are organized as nodes in a dynamically constructed directed graph and coordinate exclusively through a centralized shared workspace. A problem-adaptive GraphDesigner constructs task-specific agent topologies, while a global Orchestrator leverages the complete shared state for routing decisions, overcoming the local-view bottleneck of reactive approaches. Experiments on Game24, Six Fives, and Tower of London across six frontier LLMs demonstrate that BIGMAS consistently improves reasoning performance for both standard LLMs and LRMs, outperforming existing multi-agent baselines including ReAct and Tree of Thoughts, showing that multi-agent architectural design provides complementary gains orthogonal to model-level reasoning enhancements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂多步推理任务中面临的性能瓶颈问题。尽管以扩展思维链为特征的大型推理模型（LRM）在标准基准测试上表现有所提升，但研究背景表明，无论是标准LLM还是LRM，当问题复杂度超过一定阈值时，都会出现“准确性崩溃”现象。现有方法，包括单模型推理和多智能体框架，都存在根本性局限：单模型方法仅依赖模型自身能力的扩展，但研究表明这不足以解决逻辑一致执行的瓶颈；而现有的多智能体方法（如ReAct、Tree of Thoughts）通常采用点对点通信或固定预设的拓扑结构，导致全局任务状态分散在各个智能体中，缺乏对整体状态的可见性，且协作结构无法根据具体问题的需求进行动态调整，形成了“局部视图瓶颈”。

因此，本文的核心问题是：能否设计一种新型的多智能体架构，通过模拟人脑的全局工作空间理论，将认知负载分配到专用组件上，并外化中间推理状态，从而在结构上弥补模型级推理的不足，从根本上提升LLM在复杂任务上的稳健推理能力。具体而言，论文提出的BIGMAS框架试图解决如何动态构建任务自适应的智能体拓扑图，以及如何通过一个集中的共享工作空间实现全局状态协调，以克服现有方法中状态碎片化和静态协作模式的缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：推理方法增强、多智能体框架以及评测基准。

在推理方法增强方面，研究主要通过提示策略（如思维链、自我一致性）、分解策略（如最少到最多提示、思维程序）或基于可验证奖励的强化学习来扩展推理过程，从而形成大型推理模型。然而，这些模型级扩展在任务复杂度超过特定阈值时会出现“准确性崩溃”，表明其存在根本瓶颈。

在多智能体框架方面，现有工作旨在通过分布式协作提升推理。例如，ReAct在反应循环中交错进行推理与行动；Tree of Thoughts通过树搜索拓宽探索空间；Graph of Thoughts进一步将推理单元建模为具有依赖关系的图。此外，角色专业化框架（如MetaGPT）、规划与执行解耦方法（如LLMCompiler）以及多智能体对话框架（如AutoGen）都展示了协作的优势。然而，这些框架通常采用固定的协作图，且智能体状态缺乏全局共享，限制了其对问题结构的动态适应能力。

在评测基准方面，虽然GSM8K、MATH等被广泛使用，但存在数据污染和复杂度固定等问题。本文采用的Game24等可控制谜题环境，能精确操纵复杂度并进行逐步验证，更利于孤立地评估推理架构的收益。

本文提出的BIGMAS系统与上述工作的关系和区别在于：它首次将全局工作空间理论的三项核心原则（处理器专业化、动态联盟形成、全局广播）统一到一个架构中。具体而言，BIGMAS通过问题自适应的图构建实现动态拓扑，并通过集中式共享工作空间实现全局状态协调，从而弥补了现有框架在动态适应和全局信息共享方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一种受脑科学全局工作空间理论启发的图多智能体系统（BIGMAS）来解决复杂多步推理问题。其核心方法是将专门化的LLM智能体组织为动态构建的有向图中的节点，并通过一个集中式的共享工作空间进行协调，避免了传统多智能体系统中点对点通信的局部视野瓶颈。

整体框架分为三个主要阶段：图设计、图执行和答案提取。核心架构包含四个关键组件：1) **共享工作空间（Workspace）**：作为系统的单一事实来源，采用四分区结构（上下文区、工作区、系统元数据区和答案区），所有智能体节点仅通过读写该空间进行交互。2) **图设计器（GraphDesigner）**：根据具体问题实例动态生成任务特定的有向智能体图拓扑、工作区初始模板和交互契约，实现了问题自适应的智能体联盟构建。3) **智能体节点（Agent Nodes）**：每个节点具有特定角色描述符，按照契约规定执行结构化读写操作，输出包含目标路径、操作类型和有效载荷的指令。4) **全局协调器（Orchestrator）**：基于完整的工作空间状态和执行历史进行路由决策，能够识别收敛、检测无效循环并启用备用节点。

关键技术创新体现在：首先，采用**动态图拓扑设计**，不同问题生成不同结构的智能体图（可包含循环以支持迭代优化），突破了固定架构的限制。其次，引入**结构化验证与自校正机制**，在执行写入前对节点输出进行路径存在性、操作兼容性和负载非空性检查，失败时触发最多R次自我校正循环，确保工作空间状态完整性。最后，设计**全局条件路由策略**，协调器利用系统全局状态而非局部信息决定下一个激活节点，当步数预算耗尽时由备用解析器从工作空间中提取最佳候选答案。

该系统通过将推理过程分解为专业化智能体的协作工作流，并依托集中式工作空间实现全局状态感知，在Game24、Six Fives和Tower of London等复杂推理任务上显著提升了标准LLM和大型推理模型的性能，其架构设计增益与模型级推理增强形成正交互补。

### Q4: 论文做了哪些实验？

论文在三个推理基准上进行了实验：Game 24（算术推理）、Six Fives（约束表达式生成）和 Tower of London（多步规划）。实验设置涉及使用六个前沿大语言模型作为基础，包括 DeepSeek-V3.2、DeepSeek-V3.2 (+thinking)、Claude 4.5 Sonnet、Claude 4.5 (+thinking)、Gemini 2.5 Pro 和 GPT-5。对比方法包括：1）基础大语言模型的直接单模型推理；2）现有多智能体基线方法，如 ReAct 和 Tree of Thoughts。

主要结果如下：BIGMAS 在所有模型和任务上均一致提升了推理性能。关键数据指标包括：对于较弱的基模型，提升显著，例如 DeepSeek-V3.2 在 Game 24 上的准确率从 25.0% 提升至 36.0%，在 Six Fives 上从 12.0% 提升至 30.0%，在 Tower of London 上从 6.0% 提升至 20.0%。Claude 4.5 Sonnet 也有类似大幅提升。对于已很强的模型如 GPT-5，BIGMAS 仍能带来有意义的增长，例如在 Tower of London 上从 91.0% 提升至 98.0%。对于大型推理模型，提升同样显著，如 Claude 4.5 (+thinking) 在 Tower of London 上从 57.0% 跃升至 93.0%。

在与多智能体基线的对比中，以 DeepSeek-V3.2 为骨干模型，BIGMAS 在三个任务上均优于 ReAct 和 Tree of Thoughts。具体数据为：在 Game 24 上，BIGMAS 准确率为 36.0%，高于 Tree of Thoughts 的 30.0%；在 Six Fives 上为 30.0%，高于 Tree of Thoughts 的 25.0%；在 Tower of London 上为 20.0%，高于 Tree of Thoughts 的 18.0%。

此外，论文还分析了系统自动生成的智能体图拓扑复杂度（节点和边数量分布）、节点角色分配、各阶段（图设计、协调器路由、节点执行）的令牌消耗以及路由决策次数分布。结果显示，图设计器能根据任务特性生成合适的拓扑结构，节点执行消耗了大部分计算资源，且错误运行通常需要更多的路由决策，揭示了系统的一种特征性失败模式。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在评估范围较窄、图设计缺乏记忆性、超参数固定以及总体计算成本较高。未来可从以下几个方向深入探索：首先，将BIGMAS框架扩展到开放域问答、数学竞赛题和代码生成等更复杂的任务，验证其泛化能力。其次，引入图设计的记忆机制，如基于元学习或案例记忆的拓扑构建，以提升对同类问题家族的适应效率。再者，利用路由动态信号实现自适应早期停止机制，动态调整步数预算和自我修正次数，避免无效计算。最后，通过令牌感知的图设计和微调专用智能体来实现角色专业化，在降低单智能体负担的同时优化总体令牌消耗，推动异构多智能体系统向更高效、更强大的方向发展。这些改进有望进一步提升复杂推理任务的准确性和效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种受大脑全局工作空间理论启发的图多智能体系统BIGMAS，旨在解决大语言模型在复杂多步推理任务中存在的准确性崩溃问题。核心贡献在于通过架构设计而非单纯增强模型推理能力来提升性能，证明了多智能体协调与模型级推理增强是正交且互补的。

问题定义聚焦于LLM和大型推理模型在复杂任务上表现不佳的根本瓶颈，即一致的逻辑执行而非解决方案发现。方法上，BIGMAS将专用LLM智能体组织为动态构建的有向图节点，通过集中式共享工作空间进行协调，包含GraphDesigner智能体自适应构建任务特定的智能体拓扑，以及Orchestrator利用全局状态进行路由决策。

主要结论显示，BIGMAS在Game24、Six Fives和Tower of London等任务上显著提升了六种前沿LLM和LRM的推理性能，优于ReAct、Tree of Thoughts等基线方法。其优势源于结构设计：通过分解问题、减轻单智能体认知负担，并在全局可验证的工作空间中外部化中间状态。实验表明，图拓扑能动态适应任务复杂度，协调开销可控，且路由次数可自然反映实例难度。这为突破现有模型性能天花板提供了神经科学启发的架构路径。
