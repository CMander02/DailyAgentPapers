---
title: "MemPO: Self-Memory Policy Optimization for Long-Horizon Agents"
authors:
  - "Ruoran Li"
  - "Xinghua Zhang"
  - "Haiyang Yu"
  - "Shitong Duan"
  - "Xiang Li"
date: "2026-02-28"
arxiv_id: "2603.00680"
arxiv_url: "https://arxiv.org/abs/2603.00680"
pdf_url: "https://arxiv.org/pdf/2603.00680v1"
categories:
  - "cs.AI"
tags:
  - "Memory & Context Management"
  - "Learning & Optimization"
relevance_score: 8.5
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Algorithm"
attributes:
  base_model: "Qwen-2.5-7B, Qwen-2.5-14B, Qwen-2.5-32B, Qwen-2.5-72B"
  key_technique: "MemPO (Self-Memory Policy Optimization)"
  primary_benchmark: "WebArena, GAIA, ToolEmu, ToolBench, AgentBench"
---

# MemPO: Self-Memory Policy Optimization for Long-Horizon Agents

## 原始摘要

Long-horizon agents face the challenge of growing context size during interaction with environment, which degrades the performance and stability. Existing methods typically introduce the external memory module and look up the relevant information from the stored memory, which prevents the model itself from proactively managing its memory content and aligning with the agent's overarching task objectives. To address these limitations, we propose the self-memory policy optimization algorithm (MemPO), which enables the agent (policy model) to autonomously summarize and manage their memory during interaction with environment. By improving the credit assignment mechanism based on memory effectiveness, the policy model can selectively retain crucial information, significantly reducing token consumption while preserving task performance. Extensive experiments and analyses confirm that MemPO achieves absolute F1 score gains of 25.98% over the base model and 7.1% over the previous SOTA baseline, while reducing token usage by 67.58% and 73.12%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视野智能体（Long-horizon Agents）在与环境交互过程中，由于交互历史不断累积导致上下文长度线性增长所带来的核心问题。研究背景是，随着大语言模型（LLMs）能力的提升，智能体在解决复杂任务（如深度研究、数据分析）时，通常采用ReAct等交互范式，将环境反馈和历史记录全部拼接到提示词中。这导致上下文窗口迅速膨胀，引发三个主要挑战：受限于模型有限的上下文窗口长度，交互轮数存在明确上限；过长的上下文会产生极高的token成本，阻碍实际部署；过长的输入还会导致模型出现“迷失在中间”的现象，性能下降。

现有方法（主流方案）主要通过引入外部记忆模块，利用检索增强生成（RAG）技术从存储的历史中查找相关信息。然而，这种方法的不足在于：记忆模块是外部的、离线的，其内容压缩与组织过程缺乏与智能体任务执行的联合优化，难以与智能体的总体任务目标有效对齐。这导致模型的记忆检索是被动的，而非利用其自身能力主动地选择和组织信息，后者才能更有效地促进任务完成。

因此，本文要解决的核心问题是：如何让智能体（策略模型本身）具备主动管理和优化自身记忆内容的内在能力，使其能够在长视野、多轮次的交互中，自主地总结、压缩和组织历史信息，从而在维持任务性能的同时，显著降低上下文长度和token消耗。为此，论文提出了自记忆策略优化算法（MemPO），通过改进基于记忆有效性的信用分配机制，使策略模型能够选择性地保留关键信息，实现记忆管理与任务执行的联合优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：外部记忆系统方法、检索增强生成（RAG）方法以及强化学习（RL）在智能体中的应用。

**1. 外部记忆系统方法**：这类工作旨在通过引入外部记忆模块来扩展智能体的上下文处理能力。例如，MemGPT 受操作系统启发，采用多级内存层次管理上下文信息；Mem0 则通过动态提取、整合和检索对话信息来增强记忆容量。然而，这些方法通常依赖固定的工作流程，缺乏灵活的优化能力，难以支持跨阶段的联合优化，限制了系统的适应性和可扩展性。本文提出的 MemPO 与这些工作的核心区别在于，它使策略模型能够自主总结和管理记忆，实现了记忆内容的主动优化，而非被动检索。

**2. 检索增强生成（RAG）方法**：RAG 通过整合外部知识源来提升大语言模型的性能，现有许多记忆系统也基于 RAG 实现相关记忆片段的检索。但其主要局限在于检索仅依赖于查询与文本块的嵌入相似度，不一定能返回对解决目标任务最有用的信息，且缺乏端到端的联合优化。本文方法虽然也涉及信息管理，但通过强化学习机制进行优化，直接鼓励模型保留与任务最相关的信息，超越了基于相似度的检索范式。

**3. 基于强化学习的智能体优化方法**：强化学习已成为增强大语言模型智能体解决复杂任务的重要工具。然而，将 RL 专门用于优化智能体记忆的研究相对较少。现有工作如 MEM1，虽然将记忆整合到推理过程并对策略模型应用 RL 优化，但并未为记忆优化设计明确的目标，可能导致记忆表征次优。本文 MemPO 的核心创新在于引入了针对记忆奖励的专用信用分配机制，明确鼓励模型选择性保留关键信息，从而在保证任务性能的同时显著降低 Token 消耗。

### Q3: 论文如何解决这个问题？

论文通过提出自记忆策略优化算法（MemPO）来解决长视野智能体在交互过程中上下文增长导致的性能与稳定性下降问题。其核心是让策略模型（智能体）在环境交互中自主总结和管理记忆，而非依赖外部模块被动检索。该方法的关键在于设计了一种新颖的信用分配机制，通过评估记忆的有效性来提供细粒度奖励，从而引导模型选择性保留关键信息，显著减少令牌消耗。

整体框架基于策略优化，在训练过程中对每个样本进行多次轨迹采样。其核心架构包含两个主要优势计算模块：轨迹级优势（A^T）和记忆级优势（A^M）。轨迹级优势沿用GRPO方法，基于最终答案的正确性和输出格式给出稀疏奖励，并对组内奖励进行标准化，以评估整体轨迹质量。记忆级优势是算法的创新核心，它为每一步生成的记忆内容（即<mem>动作）设计了一个步级奖励。该奖励基于一个关键洞察：若一段上下文包含足够解决问题的信息，则模型基于该上下文生成正确答案的条件概率会更高。因此，记忆奖励R^M定义为：基于当前记忆内容生成正确答案的条件概率，减去基于此前所有步骤的轨迹生成答案的条件概率（作为偏置项）。这个差值量化了当前记忆相较于历史轨迹所保留的有效信息增益。记忆奖励同样在组内进行标准化，得到记忆级优势A^M。

最终的令牌级优势A_{i,k}是两者的结合：对于记忆段内的令牌，其优势是轨迹级优势与记忆级优势之和；对于其他令牌，则仅使用轨迹级优势。这种设计使得记忆生成获得了更丰富、更明确的反馈信号。优化目标则是在标准策略梯度目标基础上，结合了重要性采样比率裁剪和KL散度正则化，以稳定训练并防止策略偏离参考模型过远。

在推理阶段，MemPO对经典ReAct框架进行了关键修改：在每一步，模型不再依赖完整的过往历史s_{<t}，而是仅以上一步生成的记忆s_{t-1}^{mem}作为推理上下文。这实现了上下文的高效压缩与传递。

MemPO的主要创新点在于：1）提出了一个基于条件概率的、可量化的记忆有效性评估指标，实现了对记忆质量的细粒度、步级监督；2）设计了融合轨迹级与记忆级的双层优势计算机制，显著改善了信用分配，使模型能主动学习生成信息密集且任务相关的记忆摘要；3）在推理时仅依赖最新记忆，而非完整历史，从而在保持甚至提升任务性能（如F1分数）的同时，大幅降低了令牌消耗。实验表明，该方法在多项指标上超越了现有基线。

### Q4: 论文做了哪些实验？

论文实验主要在多目标问答任务上评估MemPO算法的有效性。实验设置方面，作者使用Qwen2.5-7B作为基础模型，在训练阶段先利用GPT-4.1生成的约10k条轨迹进行指令微调，随后在强化学习阶段采用分组RL方法（rollout组大小N=16，批次大小128，学习率1e-6），最大交互轮数设为16，并使用本地维基搜索引擎作为训练时的搜索工具。

数据集与基准测试方面，实验构建了多目标任务测试集：结合HotpotQA和NQ验证集的查询构建了2目标任务测试集，并利用HotpotQA合成了更多目标（4、6、8、10目标）的测试集。评估在本地维基和真实网络搜索两种环境下进行。评估指标包括答案精确度的F1分数和精确匹配（EM），以及效率指标：解决问题的总token消耗量（TT）和单步峰值token消耗量（PT）。

对比方法涵盖了多种基线：基于提示的ReAct；基于智能体RL的DeepResearcher和ReSearch；与记忆相关的RL方法MEM1和RAG方法A-MEM；以及使用相同环境但无记忆的GRPO训练模型作为基线。

主要结果如下：MemPO在性能上显著超越基线，在10目标任务上相比基础模型实现了25.98%的绝对F1分数提升，相比之前的最优基线（SOTA）提升了7.1%。在效率方面，MemPO大幅降低了token消耗，总token使用量减少了67.58%（相比基础模型）和73.12%（相比SOTA基线）。具体到10目标任务，MemPO的token消耗仅为ReSearch的约1/3，峰值token仅为1/5。消融研究证实了其奖励设计的有效性，且在不同上下文保留设置（完整、1步、3步）下均表现出稳定的性能和泛化能力。条件概率分析进一步显示，MemPO引导模型生成的记忆具有更高的信息相关性，其条件概率分布更偏向高值，有助于提升回答精度。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于，其优势计算依赖于对轨迹进行分组平均，但由于不同步骤中工具调用和记忆内容存在差异，导致状态不完全等价，可能引入偏差。尽管通过引入ε参数进行了缓解，但在更复杂的环境中，这种偏差仍需更精细的解决方案。

未来研究方向可包括：第一，探索更自适应的优势估计方法，例如利用注意力机制动态加权不同步骤的贡献，以减少状态不等价带来的偏差。第二，将记忆管理机制扩展到多模态或动态变化的环境中，研究其泛化能力。第三，结合世界模型或因果推理，使记忆摘要不仅能压缩信息，还能主动预测未来关键状态，进一步提升长序列决策的效率和稳定性。此外，可探索将记忆管理与模型参数更新更紧密耦合，实现完全端到端的优化。

### Q6: 总结一下论文的主要内容

本文提出了一种名为MemPO的自记忆策略优化算法，旨在解决长视野智能体在交互过程中因上下文增长而导致的性能下降和稳定性问题。现有方法通常依赖外部记忆模块被动检索信息，而MemPO的核心贡献在于使策略模型能够自主总结和管理记忆内容，从而与任务目标对齐。方法上，MemPO通过改进基于记忆有效性的信用分配机制，让智能体能选择性保留关键信息，显著减少令牌消耗同时保持任务性能。实验表明，MemPO在绝对F1分数上比基础模型提升25.98%，比先前SOTA基线提升7.1%，同时令牌使用量分别减少67.58%和73.12%。其意义在于通过强化学习整合记忆、推理和工具调用，实现了在长视野任务上的高效性能与计算成本降低。
