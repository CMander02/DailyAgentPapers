---
title: "Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory"
authors:
  - "Zhenting Wang"
  - "Huancheng Chen"
  - "Jiayun Wang"
  - "Wei Wei"
date: "2026-03-04"
arxiv_id: "2603.04257"
arxiv_url: "https://arxiv.org/abs/2603.04257"
pdf_url: "https://arxiv.org/pdf/2603.04257v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "记忆机制"
  - "长程规划"
  - "强化学习"
  - "工具使用"
  - "经验索引"
  - "上下文管理"
relevance_score: 9.5
---

# Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory

## 原始摘要

Large language model (LLM) agents are fundamentally bottlenecked by finite context windows on long-horizon tasks. As trajectories grow, retaining tool outputs and intermediate reasoning in-context quickly becomes infeasible: the working context becomes prohibitively long, eventually exceeds the context budget, and makes distant evidence harder to use even when it is still present. Existing solutions typically shorten context through truncation or running summaries, but these methods are fundamentally lossy because they compress or discard past evidence itself. We introduce Memex, an indexed experience memory mechanism that instead compresses context without discarding evidence. Memex maintains a compact working context consisting of concise structured summaries and stable indices, while storing full-fidelity underlying interactions in an external experience database under those indices. The agent can then decide when to dereference an index and recover the exact past evidence needed for the current subgoal. We optimize both write and read behaviors with our reinforcement learning framework MemexRL, using reward shaping tailored to indexed memory usage under a context budget, so the agent learns what to summarize, what to archive, how to index it, and when to retrieve it. This yields a substantially less lossy form of long-horizon memory than summary-only approaches. We further provide a theoretical analysis showing the potential of the Memex loop to preserve decision quality with bounded dereferencing while keeping effective in-context computation bounded as history grows. Empirically, on challenging long-horizon tasks, Memex agent trained with MemexRL improves task success while using a significantly smaller working context.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在执行长周期任务时，因有限的上下文窗口而产生的根本性瓶颈问题。研究背景是，随着LLM智能体被广泛部署为通用问题解决者，需要执行跨越数十到数百个步骤的复杂工作流（如科学文献调研、多API业务流程编排等），过程中会产生大量中间观察结果、工具输出和推理痕迹。成功不仅依赖于局部推理质量，还取决于智能体能否保留并重用早期出现的关键信息（如对话初期提到的约束、工具暴露的故障模式等）。

现有方法主要存在以下不足：它们通常通过静态的上下文工程来应对上下文压力，例如采用大型滚动提示、启发式摘要或相关的记忆启发式方法。这些方法虽然能减少活跃工作上下文，但本质上是有损的，因为它们要么截断大量过去的交互内容，要么将其压缩成有损的摘要，导致后续难以准确恢复。另一种常见的替代方案是将所有内容记录到外部记忆库中，并在需要时通过语义相似性进行检索。然而，在长周期工具使用场景中，这种设计往往很脆弱：当记忆库包含大量嘈杂、近似重复的片段时，检索会变得模糊不清，模型必须反复解析结构松散的历史记录。更重要的是，基于相似性的检索无法指导智能体如何组织自身经验，例如无法确定哪些中间结果值得建立稳定引用、哪些分支是死胡同，或者如何命名工件以确保后续访问的精确性。因此，许多现有系统仍依赖于手工设计的模板和启发式方法进行记忆构建和检索，这与人类管理长期工作的方式（在外部保留精确的笔记和引用，同时仅在工作记忆中保持少量活跃概念）存在差距。

本文要解决的核心问题是：如何为长周期LLM智能体设计一种记忆机制，使其能够在压缩上下文的同时不丢弃证据，从而实现精确、可审计的长周期信息保留与重用。具体而言，论文提出了Memex系统，其核心是索引化经验记忆机制。该机制将冗长的工具使用轨迹在工作上下文中替换为紧凑的索引化摘要，同时将完整的底层工件存档在外部键值经验存储中，并建立稳定的索引。当特定的过去结果变得相关时，智能体可以显式地解引用索引，以恢复确切的存档内容并将其重新注入工作上下文。这样，Memex明确地将紧凑的上下文内工作上下文与高保真的外部经验存档分离开来。为了优化记忆的写入（包括总结什么、存档什么、如何索引、何时压缩）和读取（包括何时以及解引用什么）行为，论文进一步提出了MemexRL强化学习框架，在上下文预算下通过量身定制的奖励塑形来训练智能体，使其学会高效管理索引化记忆。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：LLM记忆机制与长视野LLM智能体。

在**LLM记忆机制**方面，早期工作如MemGPT和MemoryBank通过结构化表示和动态机制来组织对话历史与积累经验，启发了后续研究。这些研究可进一步分为事实记忆（存储声明性知识以保持一致性）和经验记忆（从历史轨迹中积累知识以实现持续学习）。另一类工作则尝试将信息直接集成到模型的内部组件（如隐藏状态和键值缓存）中，以实现更高效的信息压缩。然而，这些方法的核心挑战仍在于如何在高效压缩和检索的同时保留关键信息。

在**长视野LLM智能体**方面，为解决任务轨迹增长导致的上下文窗口瓶颈问题，已有研究探索了基于学习的记忆管理。早期基于强化学习的方法（如MEM1、MemAgent）主要在问答或长上下文场景中训练模型以压缩和组织历史信息。近期工作（如SUPO、ReSum）将记忆摘要整合到多轮工具使用和搜索流程中，而FoldGRPO和AgentFold则进一步研究了结构化上下文折叠和多尺度历史摘要。然而，这些现有方法大多仍依赖于有损的摘要压缩或通用的记忆组织，它们虽然减少了活跃上下文，但通常无法保留一个可供后续确定性调用的、完整保真的过去证据存档。

**本文与这些工作的关系和区别**在于：现有方法主要通过摘要进行有损压缩，而本文提出的Memex则采用了一种**索引化经验记忆**机制。它维持一个简洁的、结构化的在上下文工作状态，同时将完整保真的交互内容存档于外部数据库，并通过稳定索引进行关联。这使得智能体不仅能决定何时压缩，还能决定归档什么、如何索引，以及在需要时通过解引用精确恢复过去的证据，从而实现了比纯摘要方法**有损程度低得多**的长视野记忆形式。

### Q3: 论文如何解决这个问题？

论文通过引入Memex（一种索引化经验记忆机制）及其强化学习训练框架MemexRL，来解决长视野任务中LLM智能体因有限上下文窗口而导致的性能瓶颈问题。其核心思想是**不丢弃证据的上下文压缩**，通过将完整交互内容存档于外部存储，并在工作上下文中保留简洁的索引化摘要，仅在需要时通过解引用索引来精确恢复过往证据。

**整体框架与主要模块**：
1.  **索引化经验记忆（Indexed Experience Memory）**：这是系统的核心组件，由两部分构成：
    *   **上下文中的索引化摘要（In-context IndexedSummary）**：这是一个结构化的紧凑状态，包含两部分：一是可操作的进度状态（如已验证的信息、计划），二是一个索引映射集 `I = {(index, description)}`。其中`index`是外部存储中内容的稳定索引键，`description`是对应内容的语义化描述摘要。此摘要始终保留在工作上下文中，取代不断增长的原始交互历史。
    *   **外部经验存储（External Store D）**：一个键值数据库（`index -> content`），用于存档完整的、高保真的交互内容块（如工具输出、推理痕迹、代码片段）。智能体不能直接浏览此存储，只能通过明确的索引进行访问。

2.  **关键操作**：
    *   **压缩操作（CompressExperience）**：当工作上下文增长时，智能体调用此工具。它将选定的记忆块（`(index, content)`对）写入外部存储`D`，然后将工作上下文重写为仅包含系统提示、任务指令和新的`IndexedSummary`。这实现了上下文的无损“压缩”——证据被完整保存，只是从上下文移到了外部存储。
    *   **读取操作（ReadExperience）**：当后续推理需要过往的精确证据时，智能体调用此工具并提供一个`index`。系统从`D`中检索对应的完整内容块，并将其作为新消息追加到工作上下文中，供智能体使用。

3.  **记忆块内容生成的双模式设计**：在压缩时，记忆块的内容支持两种生成模式，提供了灵活性与保真度：
    *   **显式编写**：模型直接生成重组或总结后的内容，以提高存储效率。
    *   **锚点提取**：模型提供三个简短的文本锚点（开始、中间、结束），系统从当前对话中定位并原样存档匹配的文本跨度。这适用于需要绝对保真的内容（如精确的对象ID、代码片段、测试输出），避免了模型重新生成可能引入的错误或冗余。

**创新点与MemexRL训练框架**：
论文的核心创新在于**通过强化学习来优化智能体对索引化记忆的使用策略**，而不仅仅是提供记忆机制。由于决定存档什么、如何索引、何时检索等决策的效用往往在很久之后才能体现，仅靠提示工程难以优化。因此，作者提出了MemexRL框架（一种GRPO风格的更新方法）来共同学习任务解决行为和记忆行为。

**奖励函数设计**专门针对索引化记忆的使用和上下文预算进行塑造，包含：
*   **任务成功奖励（R_task）**：鼓励最终完成任务。
*   **上下文溢出惩罚（P_context）**：惩罚工作上下文令牌数超过阈值τ的情况，激励智能体在上下文过度增长前主动触发压缩。
*   **冗余工具调用惩罚（P_redundancy）**：惩罚重复执行相同参数的工具调用，鼓励智能体通过`ReadExperience`回忆已有信息，而非重新查询。
*   **格式错误惩罚（P_format）**：惩罚工具调用格式错误，确保动作空间的有效性。

通过这种训练，智能体学会在长视野任务中动态管理记忆：何时进行压缩以保持上下文简洁，如何创建稳定且有意义的索引以便后续检索，以及何时解引用索引以恢复关键证据，从而在有限的上下文窗口内，显著减少信息损失，提高任务成功率。

### Q4: 论文做了哪些实验？

论文在实验部分主要评估了其提出的Memex(RL)框架在长视野任务上的有效性。实验设置方面，研究使用了Qwen3-30B-A3B-Thinking-2507作为基础大语言模型，这是一个总参数量约300亿的混合专家模型，具备较强的工具使用和指令遵循能力。实验环境是一个经过修改的、用于评估长视野任务执行的代理环境。

实验的核心是训练过程评估和最终性能对比。在训练过程中，通过强化学习框架MemexRL对代理进行优化，使其学习如何总结、归档、索引和检索经验。关键数据指标显示，在训练过程中，代理的任务成功率从约20%提升至超过90%，而总惩罚值（与工作上下文长度相关）从-0.4改善至约-0.1，表明代理学会了在有限的上下文预算内更有效地使用记忆工具。

主要结果通过与基线方法的对比来呈现。实验结果表明，经过MemexRL训练的代理在任务成功率上从24.2%显著提升至85.6%。同时，其峰值工作上下文长度从16,934个令牌大幅降低至9,634个令牌，接近了预设的8,000个令牌的惩罚阈值。这证明了Memex机制能够在显著压缩工作上下文的同时，有效提升长视野任务的成功率，实现了比仅依赖摘要的方法更少信息损失的记忆管理。

### Q5: 有什么可以进一步探索的点？

该论文提出的Memex机制虽能有效压缩工作上下文并保留完整证据，但其局限性和未来探索方向仍值得深入。首先，索引的生成与检索依赖强化学习训练，这可能导致训练成本高且泛化能力受限；未来可探索更轻量的自监督索引方法，或结合语义相似性进行动态索引优化。其次，外部经验数据库的存储与检索效率在超长轨迹中可能成为瓶颈，需研究更高效的数据结构（如分层索引或向量数据库）以加速检索。此外，当前方法主要针对工具使用类任务，未来可扩展至多模态或动态环境交互场景，探索跨任务的经验迁移与复用。最后，理论分析假设了有限的解引用次数，实际中如何平衡解引用频率与上下文预算仍需更精细的权衡机制，例如引入自适应预算分配策略。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体在长视野任务中受限于有限上下文窗口的问题，提出了一种名为Memex的索引化经验记忆机制。核心问题是现有方法（如截断或摘要）会因压缩或丢弃历史证据而导致信息损失，难以在长轨迹中准确复用早期信息。

Memex的核心方法是引入索引化经验记忆，将智能体的工作上下文与完整经验存储分离。具体而言，它在工作上下文中维护简洁的结构化摘要和稳定索引，同时将完整的交互细节（如工具输出、代码片段）存储在外部经验数据库中。智能体可通过解引用索引，按需精确恢复过去证据。论文进一步提出MemexRL强化学习框架，通过针对索引内存使用的奖励塑形和自适应训练，优化智能体的记忆写入（摘要、归档、索引）和读取（解引用时机）行为。

主要结论表明，Memex能在严格上下文预算下，通过有界解引用保持决策质量，同时将有效上下文计算量控制在有界范围内。实验验证了在挑战性长视野任务中，经MemexRL训练的智能体能以显著更小的工作上下文提高任务成功率。该工作的意义在于为长视野LLM智能体提供了一种更接近人类工作模式的、非损失性的记忆管理范式。
