---
title: "Let the Agent Search: Autonomous Exploration Beats Rigid Workflows in Temporal Question Answering"
authors:
  - "Xufei Lv"
  - "Jiahui Yang"
  - "Yifu Gao"
  - "Linbo Qiao"
  - "Houde Liu"
date: "2026-03-02"
arxiv_id: "2603.01853"
arxiv_url: "https://arxiv.org/abs/2603.01853"
pdf_url: "https://arxiv.org/pdf/2603.01853v1"
github_url: "https://github.com/AT2QA-Official-Code/AT2QA-Official-Code"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "AT2QA (Autonomous, Training-free Agent for Temporal Question Answering)"
  primary_benchmark: "MultiTQ"
---

# Let the Agent Search: Autonomous Exploration Beats Rigid Workflows in Temporal Question Answering

## 原始摘要

Temporal Knowledge Graph Question Answering (TKGQA) demands multi-hop reasoning under temporal constraints. Prior approaches based on large language models (LLMs) typically rely on rigid, hand-crafted retrieval workflows or costly supervised fine-tuning. We show that simply granting an off-the-shelf LLM autonomy, that is, letting it decide what to do next, already yields substantial gains even in a strict zero-shot setting. Building on this insight, we propose AT2QA, an autonomous, training-free agent for temporal question answering that iteratively interacts with the temporal knowledge graph via a general search tool for dynamic retrieval. Experiments on MultiTQ demonstrate large improvements: AT2QA achieves 88.7% Hits@1 (+10.7% over prior SOTA), including a +20.1% gain on challenging multi-target queries, showing that agentic autonomy can decisively outperform fine-tuning for temporal question answering. Code and the full set of sampled trajectories are available on https://github.com/AT2QA-Official-Code/AT2QA-Official-Code

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决时序知识图谱问答（TKGQA）中现有方法存在的自主性不足、错误传播严重、训练成本高以及可解释性差等问题。研究背景是，现实世界的事实具有动态性和时间依赖性，传统的静态知识图谱无法满足需求，因此时序知识图谱通过四元组（主体、关系、客体、时间戳）来捕捉知识的演变。TKGQA任务需要在结构实体和精确的时间动态上进行多跳推理，比传统的静态知识图谱问答更具挑战性。

现有方法主要包括两类：一是传统的基于嵌入的方法，它们将问题和知识图谱四元组映射到低维向量空间进行评分，但缺乏语义理解，难以处理复杂的时序约束，且像“黑盒”一样缺乏可解释性和自我纠正能力；二是基于大语言模型（LLM）的方法，它们通常依赖人工设计的、僵化的检索工作流程（如静态的检索增强生成）或需要进行昂贵的监督微调。这些方法存在明显不足：它们缺乏自主性，强制LLM遵循固定流程，限制了其探索和适应能力；在复杂多跳查询中，一旦中间检索失败，错误会级联传播，且缺乏自我纠正机制；微调成本高昂，耗时耗力；同时，许多方法无法提供明确的证据链，导致决策过程难以审计。

本文要解决的核心问题是：能否构建一个自主的、无需训练的、具有明确证据链可解释性、并能充分激发LLM自主性的TKGQA方法，从而显著超越现有最佳性能？为此，论文提出了AT2QA框架，其核心思想是赋予现成的LLM自主权，让其作为一个自主智能体，通过一个通用的搜索工具与时序知识图谱环境进行迭代交互，动态决定下一步行动，从而实现系统级的自我纠正，克服静态工作流程的瓶颈。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为传统方法和基于大语言模型（LLM）的现代方法两大类。

在传统方法中，主要包括基于表示学习（如嵌入方法）和基于语义解析（如逻辑查询）的范式。前者将实体和时序关系编码为低维向量，通过评分函数评估候选事实，但可解释性差；后者尝试将自然语言问题转化为逻辑表达式。这些方法通常需要大量特定训练资源，难以泛化到未见过的时序知识图谱。

近年来，LLM的引入推动了范式转变。现有LLM集成方法主要聚焦于检索增强生成（RAG）和提示工程：例如ARI通过时间感知训练信号增强模型适应性；$TimeR^{4}$和PoK通过改进检索组件生成更全面的推理计划；TempAgent通过设计包含10个特定时序工具的套件，将ReAct范式适配到时序领域。此外，RTQA采用自底向上的分解策略递归求解子问题，而MemoTime利用闭源API进行推理并存储解决路径作为记忆。然而，这些方法通常缺乏一致性验证机制，容易因前序步骤错误而偏离正确推理轨迹。

近期，一些工作（如TKG-Thinker和Temp-R1）探索了更自主的智能体架构。但它们要么依赖于复杂、人工设计的硬编码路径，限制了LLM的全局规划和自主纠错能力；要么需要进行昂贵且耗时的“重构式”训练。

本文提出的AT2QA与上述工作的核心区别在于：它摒弃了僵化的检索工作流程或监督微调，而是赋予现成的LLM完全的自主性，让其通过通用搜索工具与知识图谱动态交互，自主决定下一步行动。这种训练零样本、高度自主的智能体架构，在保持灵活性的同时，显著提升了性能，特别是在复杂多目标查询上。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AT2QA的、完全自主且无需训练的LLM智能体框架来解决时序知识图谱问答问题。其核心方法是摒弃传统僵化的检索流程或监督微调，转而赋予通用大语言模型自主决策能力，使其能够通过迭代搜索与知识图谱环境交互，进行动态自我修正。

整体框架包含两个核心组件：一个配备结构化时序搜索工具的检索增强推理智能体，以及一个从模型自生成经验中挖掘有效少样本示例的轨迹优化策略。在推理时，智能体接收系统提示、问题和少样本示例，然后反复调用搜索工具与环境交互，直到收集到足够证据或达到最大步数限制。

关键技术体现在以下方面：
1.  **结构化时序检索工具**：该工具是连接LLM与结构化知识图谱的桥梁。它接受查询字符串和一组结构化约束（如时间窗口、实体、关系）作为输入。其工作流程分为三步：首先，利用约束对图谱进行符号化过滤，得到候选事实子集；其次，采用密集检索方法，将查询和候选事实编码到同一向量空间进行语义匹配和排序；最后，提供两种排序模式（基于相关性或基于时间顺序），以灵活处理时序信息。
2.  **自主推理与自我修正过程**：LLM作为自主智能体，在每一步基于历史信息生成“思考”并调用搜索工具。这种多轮交互机制使得智能体能够进行**自我修正**：如果检索到的证据与当前假设冲突，智能体可以在后续步骤中调整其搜索约束（例如扩大时间窗口），从而动态优化推理路径。
3.  **训练免费的轨迹优化（创新点）**：为了提升智能体性能而不更新模型参数，论文提出了一种无需训练的、类似GRPO的经验选择方案。其流程是：对一批训练问题采样生成多条推理轨迹；通过规则（答案是否完全匹配）为每条轨迹分配二元奖励，仅保留成功的轨迹；然后，利用LLM本身评估这些成功轨迹的“边际教学价值”，筛选出能提供新见解的“优势经验”；最后，通过验证集增益评估，构建一个固定容量的最优少样本示例库，用于测试时推理。

该方法的核心创新在于将**智能体自主性**与**专门设计的时序检索工具**相结合，并通过**训练免费的经验蒸馏**来优化提示，从而在零样本设置下实现了对复杂时序推理任务的显著性能提升。

### Q4: 论文做了哪些实验？

论文在MultiTQ数据集上进行了全面的实验评估，这是一个专为多粒度时序问答设计的综合性高难度基准测试。实验设置方面，AT2QA采用DeepSeek-V3.2作为骨干大语言模型，生成温度设为1.0，最大交互轮次限制为20轮。检索工具使用GLM-Embedding-3模型离线嵌入事实，向量维度为256，每次调用最多返回10个事实。整个推理过程无需训练，仅使用一个包含K=3个示例的固定经验库进行少量上下文学习。

对比方法分为两大类：一是基于时序知识图谱嵌入的传统方法（如EmbedKGQA、CronKGQA、MultiQA），二是基于大语言模型的静态工作流方法（包括提示工程类如ARI、TempAgent、MemoTime、RTQA，以及微调类如Search-R1、TimeR⁴、PoK、Temp-R1）。评估指标为标准Hits@1（精确匹配）。

主要结果显示，AT2QA取得了突破性性能：整体Hits@1达到88.7%，相比之前的最佳模型Temp-R1（78.0%）绝对提升了10.7%。在最具挑战性的多目标查询上，AT2QA获得了75.1%的准确率，以20.1%的绝对优势大幅超越此前最佳水平（55.0%）。在时间预测任务上达到94.5%，虽略低于微调模型Temp-R1的96.9%，但这是在保持零训练、高泛化性前提下的优异表现。轨迹分析进一步量化证明了智能体的自主行为：约32%的成功案例中，关键证据在推理后半程才首次出现，体现了自我纠正能力；而在早期发现关键证据后，智能体会继续搜索验证，展示了自我验证的元认知规划能力。

消融实验验证了框架的稳健性：更换骨干模型（Qwen3-Max、DeepSeek-R1、Kimi-2.5）在零样本设置下均能保持强劲性能（78.9%-84.4%）；移除经验库会使性能降至零样本基线（84.4%）；禁用时间排序、结构过滤分别导致准确率下降至79.6%和78.2%；而移除时间窗口约束则造成最大跌幅（59.2%），凸显了显式时序约束对多跳推理的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于效率和稳定性。其自主探索机制虽提升了鲁棒性，但检索过程依赖近邻搜索且允许最多20轮交互，导致延迟和推理成本高于单次检索的RAG方法。此外，完全自主性可能引发冗余探索或循环行为，尤其在模糊查询或干扰项强的场景下，性能可能受解码随机性和停止准则影响。

未来研究可从三方面深入：一是优化效率，例如引入近似最近邻索引和自适应早期停止策略，以平衡精度与速度；二是增强稳定性，通过设计反思机制或引入轻量级监督信号来引导探索，减少无效循环；三是扩展应用场景，探索该自主智能体在动态知识图谱或多模态时序推理中的潜力，并研究其与参数高效微调技术的结合，以进一步提升泛化能力。

### Q6: 总结一下论文的主要内容

本文针对时序知识图谱问答任务，提出了一种名为AT2QA的新型自主智能体框架。该研究的关键问题是：如何让大语言模型在无需人工设计固定工作流或进行昂贵监督微调的情况下，有效进行时序约束下的多跳推理。其核心方法是赋予现成大语言模型完全的自主性，仅通过一个通用的搜索工具接口，让其自主决定与动态时序知识图谱的交互策略，包括是否继续搜索、调整约束或重写查询，从而自然地产生迭代验证和修正行为。此外，论文还提出了一种无需训练的经验挖掘策略，从模型自身的成功轨迹中构建少量示例库以稳定其工具使用行为。主要结论是，AT2QA在MultiTQ基准测试上取得了88.7%的Hits@1，显著超越了现有最佳方法，尤其在多目标查询上提升超过20%，证明了在时序推理任务中，赋予模型自主性比强加固定流程或进行重构性训练更为有效。
