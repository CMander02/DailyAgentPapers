---
title: "SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents"
authors:
  - "Qiao Xiao"
  - "Haochen Shi"
  - "Yisen Gao"
  - "Wenbin Hu"
  - "Huihao Jing"
  - "Tianshi Zheng"
  - "Baixuan Xu"
  - "Ziheng Zhang"
  - "Weiqi Wang"
  - "Haoran Li"
  - "Jiaxin Bai"
  - "Yangqiu Song"
date: "2026-06-15"
arxiv_id: "2606.16591"
arxiv_url: "https://arxiv.org/abs/2606.16591"
pdf_url: "https://arxiv.org/pdf/2606.16591v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "工具发现"
  - "意图图"
  - "检索增强"
  - "工具使用"
  - "主动检索"
  - "Agent架构"
relevance_score: 9.5
---

# SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents

## 原始摘要

Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a natural alternative, but existing one-shot retrieval methods often fail to align isolated tool descriptions with the agent's true task intention, especially in long-horizon tasks where required capabilities emerge through decomposition, observations, and newly induced subgoals. We propose SING, an intention-aware active tool discovery framework that builds an intention-tool graph linking user intentions, tool capabilities, and tool collaboration patterns, and dynamically retrieves tools according to evolving task states. Using a unified corpus of 7,471 tools, we evaluate SING on three real-world tool-use benchmarks. SING improves Global Recall@5 by up to 59.8% and downstream success rate by up to 28.9% over baselines, while reducing full-corpus tool-schema exposure by 99.8%, demonstrating that intention-aware graph structure enables more accurate and context-efficient tool discovery in large-scale agentic ecosystems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模工具生态系统中，大型语言模型（LLM）智能体因静态工具注入模式带来的可扩展性与意图对齐不足的问题。现有方法通常将所有工具模式一次性注入模型上下文，但这在工具数量扩展到成百上千时会产生严重问题：不仅消耗大量上下文预算、引入无关工具、削弱模型对关键信息的保留能力，更本质上是基于封闭世界假设，限制了智能体根据动态任务状态主动发现所需工具的能力。虽然检索增强的工具选择可作为替代方案，但现有的一次性检索方法仅根据初始用户查询匹配孤立的工具描述，难以将检索结果与真正的任务意图对齐。对于需要多轮交互的长期任务，用户意图往往是模糊、组合性或部分指定的，所需的能力需通过任务分解、中间观察和新增子目标逐步显现，而一次性检索无法捕捉这些下游或先决条件工具。为此，本文提出了SING框架，通过构建连接用户意图、工具能力与工具协作模式的意图-工具图，并基于动态任务状态进行推理时的主动检索，有效解决了上述问题，实现了在大规模工具空间中更准确且上下文高效的工具发现。

### Q2: 有哪些相关研究？

主要相关研究可分为两类：方法类和应用类。方法类包括早期推理-行动范式的ReAct，以及监督微调方法如Toolformer、Gorilla、ToolLLM，它们通过标注或合成演示训练模型模仿API调用，但受限于离线数据覆盖范围和质量的局限性。近期强化学习方法如ToolRL、ReTool、ToRL则通过学习执行反馈优化工具选择与动作，但仍假设候选工具已预先定义。本文与这些工作的核心区别在于，SING聚焦于开放世界的工具发现，而非静态工具库中的使用。工具检索方面，Tool2Vec学习工具嵌入，AnyTool进行分层检索，ToolRerank结合层级感知重排序，而MCP-Zero实现主动发现，但依赖模型生成请求与自然语言描述的匹配，易受描述模糊性和意图复杂性影响。SING通过构建意图-工具图结构，将任务意图、工具能力与协作模式关联，实现动态检索，克服了现有方法在跨轮次、组成性意图上的脆弱性。应用类基准包含ToolBench、API-Bank等真实工具使用评测，SING在7,471工具库上较基线提升Global Recall@5达59.8%，并降低99.8%完整模式暴露，验证了意图感知图结构在大规模生态下的扩展优势。

### Q3: 论文如何解决这个问题？

SING通过构建意图-工具图（Intention-Tool Graph）来主动追踪工具，并采用动态ReAct框架实现上下文物联的检索。核心方法分为三部分：第一，意图图构建。它从工具模式中合成真实用户查询，并扩展到多工具链，然后提取原子动词-宾语意图（如“获取天气”），跨工具合并后构建异构图，包含服务器、工具和意图节点，以及has_tool、has_intention和有向tool_next等边，使用对数频率加权。第二，动态ReAct框架。代理在每个步骤可选择Discover、Invoke或Respond。Discover时，将状态转化为查询，通过层级发现管道检索新工具：先检索相关服务器（结合语义匹配和以意图为种子的个性化PageRank图传播），再对工具重排序（融合描述匹配、意图匹配和图重要性分数）。Invoke调用已发现工具，Respond终止。第三，创新点在于用意图作为用户请求和工具描述之间的中间抽象，使语义对齐更精确，并通过图结构捕获工具协作模式，从而在保留99.8%工具库的情况下，将Global Recall@5提升高达59.8%，下游任务成功率提升达28.9%。

### Q4: 论文做了哪些实验？

论文在构建包含779个MCP服务器、7,471个工具的语料库上进行实验，评估了SING在Global（全语料库检索）和Restricted（限定基准服务器检索）两种设置下的性能。数据集采用三个互补基准：MCP-Universe（领域特定任务、执行评估）、MCP-Atlas（多步任务、基于声明的评分）和MCP-Bench（模糊依赖工具编排）。对比方法包括基于嵌入的一次性检索（Embedding Only）和动态ReAct式主动发现框架MCP-Zero。关键结果：在Global设置下，SING在Recall@5上相对MCP-Zero提升显著，MCP-Bench提升14.2%（0.7901→0.9022）、MCP-Universe提升25.3%（0.4339→0.5438）、MCP-Atlas提升59.8%（0.1985→0.3172）；MRR提升0.057至0.214；下游任务成功率在MCP-Universe上相对提升28.9%（Global）和20.8%（Restricted）。此外，SING将全语料库工具模式暴露减少99.8%（从693,574降至1,298 tokens）。错误分析表明，SING主要减少了检索错误（Global下从156降至91），将瓶颈从发现阶段转移至下游执行阶段。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在评估成本和执行变异性两个方面。未来可探索的方向包括：1) 在更广泛的模型家族和智能体骨干网络上验证SING的有效性，以增强其泛化能力；2) 研究如何将意图-工具图与在线学习结合，使其能动态适应工具变化（如API更新或服务下线），并引入反馈机制自动修正检索偏差；3) 针对长程任务中工具依赖的累积误差，可探索基于图注意力网络的层次化意图分解，将高层目标拆解为子目标对应的工具链；4) 进一步优化图结构以捕捉隐式工具协作模式，例如通过时序图神经网络建模工具调用序列的因果依赖关系，提升对新兴组合任务的适应能力。这些改进将有助于突破当前静态工具库的封闭世界假设，实现更鲁棒的动态工具发现。

### Q6: 总结一下论文的主要内容

这篇论文提出了SING（合成意图图）框架，旨在解决大规模工具生态系统中大语言模型（LLM）智能体的工具发现与选择问题。核心问题是，随着智能体可调用的工具数量增至数百甚至数千，传统的静态工具注入不仅成本高昂，还固化了智能体的能力边界；而现有的检索增强方法也常因无法对齐工具描述与智能体动态演化的任务意图而失效。SING方法通过构建一个意图-工具图，显式地链接用户意图、工具能力及工具间的协作模式，使智能体能够根据任务状态的演变进行动态、主动的工具检索。在包含7,471个工具的统一语料库上进行的实验表明，SING在三个真实基准测试中，将全局Top-5召回率最高提升了59.8%，下游任务成功率最高提升了28.9%，同时减少了99.8%的全量工具模式暴露。该工作的主要意义在于，通过引入意图感知的图结构，为构建更准确、高效且可扩展的智能体工具使用机制提供了一条实用路径，推动了智能体从封闭静态环境向开放动态环境的发展。
