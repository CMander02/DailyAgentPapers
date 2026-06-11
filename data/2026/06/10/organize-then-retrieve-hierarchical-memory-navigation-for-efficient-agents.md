---
title: "Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents"
authors:
  - "Hao-Lun Hsu"
  - "Nikki Lijing Kuang"
  - "Boyi Liu"
  - "Zhewei Yao"
  - "Yuxiong He"
date: "2026-06-10"
arxiv_id: "2606.11680"
arxiv_url: "https://arxiv.org/abs/2606.11680"
pdf_url: "https://arxiv.org/pdf/2606.11680v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Memory Management"
  - "Hierarchical Retrieval"
  - "Working Memory"
  - "Agent Efficiency"
relevance_score: 7.5
---

# Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents

## 原始摘要

Large language model (LLM) agents struggle with long-horizon tasks due to their inherent statelessness, requiring all task-relevant information to be encoded in growing input contexts. The resulting degraded reasoning quality, increased inference cost, and higher latency necessitate efficient working memory mechanisms. However, existing approaches either rely on lossy compression or similarity-based retrieval, which often fail to capture temporal structure and causal dependencies required for multi-step agentic tasks. In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information. HORMA decomposes working memory into two stages: structured memory construction and navigation-based retrieval. The construction module iteratively refines how experiences are structured by distinguishing between failures caused by missing information and those caused by misleading or overloaded context. The navigation module retrieves task-relevant context by traversing the hierarchy using a lightweight agent trained with reinforcement learning to select minimal yet sufficient context, thereby reducing latency along the critical execution path. Across ALFWorld, LoCoMo, and LongMemEval, HORMA improves task performance under constrained context budgets while requiring at most 22.17% of the baseline token usage in long conversation tasks. Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）智能体在长程任务中由于固有“无状态”特性所导致的效率低下问题。现有的方法存在严重不足：一方面，智能体倾向于将所有历史信息直接塞入不断增长的输入上下文（“历史囤积者”），导致上下文过载、信息稀释、推理质量下降和推理成本飙升；另一方面，依赖有损压缩（如摘要）或基于语义相似性的扁平检索机制，则会不可逆地丢失细粒度信息，并难以捕捉长程交互中关键的时序结构和因果依赖关系，导致检索结果在时间上不一致或上下文无关。

针对这些挑战，本文提出了HORMA（Hierarchical Organize-and-Retrieve Memory Agent）框架，其核心目标是构建一个高效、可扩展的工作记忆机制。具体而言，工作被分解为两个解耦的模块：记忆构建模块负责将原始经验组织成类文件系统的分层摘要结构，并通过对比成功与失败轨迹进行递归技能优化；记忆检索模块则通过一个轻量级强化学习智能体在该层次结构中主动导航，以提取最少的任务相关上下文。该论文旨在解决的核心问题是：如何在不丢失细节信息的前提下，实现高效、可导航的结构化记忆访问，从而在严格上下文预算下显著提升长程任务的性能与效率，并超越现有方法。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作。第一类是**基于LLM的智能体工作记忆方法**，包括压缩和结构化方法（如ReSum、ACON）以及在线维护方法（如基于循环更新或策略的内存操作）。HORMA的不同在于它通过构建文件系统式的层次结构来组织经验，并使用轻量级检索代理进行导航式检索，避免了有损压缩或仅基于相似性检索的局限性，同时保留了时间结构和因果依赖。第二类是**基于强化学习（RL）的LLM**，如DeepSeek-R1、Search-R1，以及用于内存构建的RL方法（如MemRL、MemSkill）。与这些端到端的内存增强RL方法不同，HORMA将内存检索形式化为导航问题，并单独训练专用检索代理，从而缓解了信用分配难题。第三类是**内存与技能演化**，包括基于RL的技能选择（如MemSkill、SkillRL）以及非参数方法（如Skill-Pro、MCE）。HORMA属于非参数方法，将内存管理技能建模为非参数更新，在推理时无需修改底层LLM即可持续适应，具备更强的泛化能力和更低的训练成本。

### Q3: 论文如何解决这个问题？

HORMA通过将工作记忆解耦为结构化的记忆构建和基于导航的检索两个独立模块来解决长程任务中的状态缺失问题。其核心架构是一个类似文件系统的层级记忆工作空间，其中摘要实体与原始轨迹相链接，在高效访问的同时不丢失细节信息。

整体框架包含两个主要组件：记忆管理器（M_m）和检索代理（M_r）。记忆管理器负责将原始交互转化为层级结构，通过bash命令（如mkdir、nano）执行文件系统操作，将轨迹归档为带时间戳的目录，并选择性生成结构化笔记，包含任务相关抽象、时间元数据和指向原始轨迹的引用。该模块采用递归技能精炼方法，通过对比使用原始历史（成功）与HORMA结构化记忆（失败）的案例来识别信息丢失（外生集）或噪声过滤（内生集），从而迭代优化管理策略。

检索代理则通过导航层级结构来构建任务相关上下文C_t，利用目录层级、时间组织和来源元数据等显式结构信号定位相关内容。其动作空间包括ls、grep、cd、cat等bash命令以及select和done两个终止动作，使检索能先遍历紧凑结构笔记，仅在必要时才展开原始轨迹。该策略通过GRPO（组相对策略优化）进行强化学习优化，基于检索上下文与真实证据的重叠度定义奖励函数，鼓励精确紧凑的上下文选择，从而在关键执行路径上降低延迟。这种方法在ALFWorld、LoCoMo和LongMemEval等基准测试中，在受限上下文预算下提升了任务性能，且token使用量仅需基线方法的22.17%。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验。**实验设置**包括: ALFWorld (交互式具身模拟), LoCoMo 和 LongMemEval (长对话问答)。**对比方法**包括使用相似度检索、压缩 (如记忆折叠) 和固定上下文窗口的基线系统。

**主要结果**:
1.  **ALFWorld**: HORMA 在不同上下文限制下均取得更高成功率，并实现了交互步数与输入 token 数之间更优的帕累托效率。
2.  **LoCoMo**: HORMA 仅使用基线方法 3.07%-22.17% 的 token 数，取得更优或相当的性能。
3.  **LongMemEval**: HORMA 仅使用基线方法 1.24%-16.19% 的 token 数。其轻量级检索代理展现出强大的**分布外泛化能力**，在性能上超越了所有基线，甚至包括那些没有上下文限制的基线。

关键数据指标显示，HORMA 在任务性能和 Token 效率之间取得了更好的平衡，证明了将记忆管理与检索解耦的有效性。

### Q5: 有什么可以进一步探索的点？

该工作提出的层级记忆导航机制虽有效，但存在几个关键局限。首先，树的构建依赖于预定义的总结策略，对动态任务中因果关系的捕捉可能不够细粒度，例如未能区分偶然共现与真实依赖。未来可探索基于因果图或反事实推理的自动结构优化，让记忆组织更符合任务逻辑。其次，强化学习训练的导航器虽能压缩上下文，但在高噪声或信息冗余场景中可能陷入局部最优——尤其在长尾任务中，轻量策略容易忽略远距离但关键的线索。改进思路是引入分层注意力或课程学习，先粗搜再精调。此外，当前方法仅支持显式层级导航，缺乏对隐式语义关联（如跨层级概念抽象）的利用。可尝试结合符号推理与神经检索，构建可解释的记忆路径图，并允许智能体在推理中动态拆解或合并节点。最后，多模态场景下的记忆结构（如视觉-文本跨模态对齐）尚未验证，这是重要的扩展方向。

### Q6: 总结一下论文的主要内容

大型语言模型（LLM）智能体在处理长时任务时，因无状态性而面临上下文膨胀、推理质量下降和高延迟等问题。现有方法要么采用有损压缩，要么依赖基于相似性的检索，但难以捕捉多步任务所需的时间结构与因果依赖。为此，本文提出HORMA——一种层次化组织-检索记忆智能体。其核心贡献在于将工作记忆显式解耦为两个独立模块：记忆构建模块通过对比分析成功与失败轨迹，迭代地将原始经验组织成类似文件系统的层次化结构，并保留与原始轨迹的链接；记忆检索模块则通过强化学习训练一个轻量级智能体，利用Bash工具导航这个层次结构，以选择最精简且充足的任务相关上下文。在ALFWorld、LoCoMo和LongMemEval三个基准上的实验表明，HORMA在有限的上下文预算下提升了任务性能，在长对话任务中仅需基线模型3.07%-22.17%的token，并展现出了优异的跨任务泛化能力。该方法通过解耦记忆构建与检索，为长时任务提供了一个更高效、可解释且可扩展的工作记忆机制。
