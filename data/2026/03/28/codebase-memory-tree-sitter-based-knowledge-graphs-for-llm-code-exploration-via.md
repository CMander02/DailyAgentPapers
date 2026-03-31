---
title: "Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP"
authors:
  - "Martin Vogel"
  - "Falk Meyer-Eschenbach"
  - "Severin Kohler"
  - "Elias Grünewald"
  - "Felix Balzer"
date: "2026-03-28"
arxiv_id: "2603.27277"
arxiv_url: "https://arxiv.org/abs/2603.27277"
pdf_url: "https://arxiv.org/pdf/2603.27277v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.PL"
tags:
  - "Code Agent"
  - "Knowledge Graph"
  - "Tool Use"
  - "Model Context Protocol"
  - "Code Exploration"
  - "Efficiency"
  - "System Design"
relevance_score: 7.5
---

# Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP

## 原始摘要

Large Language Model (LLM) coding agents typically explore codebases through repeated file-reading and grep-searching, consuming thousands of tokens per query without structural understanding. We present Codebase-Memory, an open-source system that constructs a persistent, Tree-Sitter-based knowledge graph via the Model Context Protocol (MCP), parsing 66 languages through a multi-phase pipeline with parallel worker pools, call-graph traversal, impact analysis, and community discovery. Evaluated across 31 real-world repositories, Codebase-Memory achieves 83% answer quality versus 92% for a file-exploration agent, at ten times fewer tokens and 2.1 times fewer tool calls. For graph-native queries such as hub detection and caller ranking, it matches or exceeds the explorer on 19 of 31 languages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）编程代理在探索和理解代码库时存在的效率低下和缺乏结构化理解的核心问题。研究背景是，随着Claude Code、Cursor等基于LLM的编码代理的出现，软件开发进入了自然语言驱动的新阶段。然而，这些代理目前主要依赖反复读取文件和使用grep搜索等基于纯文本的交互方式。

现有方法的主要不足在于，这种文本探索策略扩展性差。代理需要消耗数十万计的大量令牌（tokens）和多次工具调用，才能回答诸如“更改这个函数会影响什么？”这类本质上属于结构性的问题。这源于一个根本性的不匹配：LLM代理处理的是非结构化文本，但开发者提出的问题（如调用图、依赖链、影响分析）却具有内在的结构性。基于文本的搜索无法有效捕获代码元素间的传递关系，导致效率低下、成本高昂。尽管已有一些图结构的代码表示（如代码属性图）和知识图谱增强检索的研究，但它们通常需要复杂的基础设施，且未与新兴的轻量级代理工具标准（如模型上下文协议MCP）有效结合。

因此，本文要解决的核心问题是：如何为LLM编码代理提供一种高效、轻量且具备深度结构理解能力的代码库探索机制。具体而言，论文提出了Codebase-Memory系统，其核心思路是将代码库结构视为可通过轻量级工具直接查询的一等知识图谱，而非仅提供原始文件内容。该系统利用Tree-Sitter解析66种语言，构建持久化的知识图谱，并通过MCP协议向代理暴露14种结构化查询工具（如调用路径追踪、影响分析、枢纽检测），从而实现以十分之一的令牌消耗和约一半的工具调用次数，达到与基于文件探索的传统代理相近的答案质量，并在图原生查询任务上表现更优。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**结构化代码表示与知识图谱构建**、**基于图谱的智能体导航与检索增强**以及**代码智能体架构与评测基准**。

在**结构化代码表示与知识图谱构建**方面，早期研究如程序依赖图（PDG）、代码属性图（CPG）和CodeQL构建了强大的代码分析框架，但它们通常笨重且依赖特定查询语言，不适合LLM直接使用。近期工作如GraphCoder、CodexGraph、RepoGraph和KGCompass则专注于为LLM构建代码图谱以提升仓库级任务性能。本文的Codebase-Memory与这些工作目标相似，但关键区别在于：它通过Model Context Protocol（MCP）提供标准化接口，兼容任何支持MCP的智能体；采用SQLite实现零依赖部署；支持增量同步和通过单一二进制解析66种语言，在易用性和通用性上更具优势。

在**基于图谱的智能体导航与检索增强**方面，LocAgent、GraphCodeAgent、RANGER等工作探索了如何利用图结构指导智能体在代码库中进行多跳定位或检索。Prometheus和Repository Intelligence Graph也结合了Tree-Sitter图谱与记忆机制。本文工作属于这一脉络，但更强调通过MCP提供持久化、轻量级的图谱服务，作为通用的检索层优化。

在**代码智能体架构与评测基准**方面，SWE-bench确立了评测标准，SWE-Agent、AutoCodeRover、Agentless和OpenHands等研究了智能体策略与接口设计。本文工作与这些研究是正交的：它主要优化底层检索和代码表示层，其图谱输出可以被上述任何智能体架构所利用，以解决它们通常面临的“探索效率与理解深度”的权衡（如LoCoBench-Agent所揭示的问题）。此外，像LLMLingua这类提示压缩研究，也从侧面反映了减少不必要令牌消耗的重要性，而本文通过提供精准的结构化信息，从源头上避免了冗余的令牌消耗。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于Tree-Sitter的持久化知识图谱，并利用模型上下文协议（MCP）为LLM智能体提供结构化的代码探索能力，从而解决传统LLM编码代理通过重复文件读取和grep搜索来探索代码库时缺乏结构理解、消耗大量令牌的问题。

**核心方法与架构设计：**
系统采用三阶段流水线架构。第一阶段是**解析（Parse）**，利用Tree-Sitter解析66种语言的AST，提取定义（函数、方法、类等及其签名、返回类型、复杂度等）、调用点、导入、引用和特质实现。对于Go、C和C++，采用混合方法，在Tree-Sitter提取的基础上，结合类似LSP的类型解析，以提高存在方法接收器、指针间接引用等情况下的调用图准确性。第二阶段是**构建（Build）**，执行一个多阶段流水线，使用并行工作池将提取的实体写入每个工作者的内存图缓冲区，合并后刷新到SQLite数据库，并延迟创建索引。第三阶段是**服务（Serve）**，通过一个提供14种类型化工具的MCP服务器暴露图谱，供LLM智能体通过标准工具调用语义进行交互。整个系统实现为一个静态链接的C语言二进制文件，无运行时依赖。

**关键技术模块与创新点：**
1.  **知识图谱模型**：采用属性图模型，包含类型化的节点（如项目、文件、函数、类、接口、路由等）和边（如CALLS、IMPORTS、DEFINES、IMPLEMENTS等），能表示代码的结构关系和语义链接。特别地，通过特定框架提取器发现了HTTP_CALLS和ASYNC_CALLS边，使REST端点成为图谱中的一等公民，从而支持跨语言的分布式代码库（如微服务架构）表示。
2.  **多阶段并行流水线**：构建阶段包含六个有序阶段（结构、提取、解析、丰富、刷新、后索引），在一个SQLite事务内执行。提取和解析阶段通过基于pthreads的工作池并行处理，每个工作者写入独立的缓冲区，最后合并。这避免了批量插入时的SQLite开销，并提升了性能。
3.  **智能调用解析策略**：将原始被调用者名称解析为图谱节点是核心链接挑战。系统采用一个包含六种策略的优先级级联机制，并辅以置信度评分。前三种策略（导入映射、导入映射后缀、同一模块）在结构良好的代码库中能解析约80%的调用，后三种策略处理跨模块引用和动态分发。对于Go、C/C++，还引入了**LSP风格的混合类型解析**，通过构建类型注册表和范围跟踪，自底向上评估调用点接收者表达式的类型，生成更高置信度的边。
4.  **增量索引与社区发现**：通过后台文件监视器（使用自适应轮询和XXH3内容哈希）监控代码库变更，仅对受影响文件进行增量重新索引。系统应用Louvain模块化优化算法，基于调用、HTTP调用和异步调用边将调用图划分为功能社区，用于架构分析。
5.  **安全与完整性保障**：针对MCP服务器的安全挑战，论文提出了深度防御方法，包括一个八层的CI审计套件（如静态允许列表审计、二进制字符串审计、网络出口监控等）和代码级保护（如参数验证、SQLite授权回调），以防范供应链攻击和恶意行为。

通过这一整套方法，Codebase-Memory使得LLM智能体能够以结构化的方式高效探索代码库，显著减少了令牌消耗和工具调用次数，并在图原生查询（如枢纽检测、调用者排名）上表现出色。

### Q4: 论文做了哪些实验？

论文实验主要围绕四个维度展开。在实验设置上，研究者构建了一个包含12个标准化问题类别的基准测试，涵盖枢纽检测、调用者排序、依赖清单和完整调用链追踪等任务。数据集为31种编程语言对应的31个真实开源代码库，规模从78个节点到49,398个节点不等。

对比方法为两个智能体：使用Codebase-Memory系统14种工具的MCP智能体，以及使用传统文件读取和grep搜索的探索者智能体。两者均以Claude Opus 4.6作为LLM后端。主要结果通过人工检查代码生成的参考答案进行评分。

关键数据指标显示：在答案质量上，MCP智能体得分为0.83，探索者智能体为0.92，前者达到后者90%的水平。在效率上，MCP智能体每个问题平均消耗约1000个token，使用2.3次工具调用，分别仅为探索者智能体（约10000个token和4.8次工具调用）的十分之一和约一半（2.1倍更少）。查询延迟方面，MCP智能体低于1毫秒，而探索者智能体需10-30秒。在针对图结构查询（如枢纽检测）的任务中，MCP智能体在31种语言中的19种上匹配或超越了探索者智能体。系统性能上，为49K节点建立新鲜索引约需6秒，增量重新索引约1.2秒，BFS调用路径追踪约0.3毫秒。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是知识图仅捕获静态代码结构，无法处理宏、运行时行为或动态特性；二是评估主要基于单一LLM后端和特定阈值，结论的普适性有待验证；三是当前系统主要针对单个代码库，尚未覆盖多仓库的依赖关系。

未来研究方向可以从以下几个维度展开：首先，技术层面可探索混合检索架构，将结构检索与基于嵌入的语义检索相结合，以兼顾关系查询和语义理解；其次，系统功能上应扩展对领域特定语言（如临床数据转换中的DSL）的支持，并开发LLM生成的图摘要功能，提升可解释性；再者，需开展更全面的实证研究，在SWE-bench等基准上对比图检索、文本检索及其他工具（如ctags）的性能；最后，鉴于MCP生态的安全隐患，亟需建立标准化的安全验证框架，确保工具链的可信度。这些方向共同指向更高效、安全且通用的代码智能探索系统。

### Q6: 总结一下论文的主要内容

论文针对LLM代码代理在探索代码库时依赖重复文件读取和搜索、缺乏结构理解且消耗大量令牌的问题，提出了Codebase-Memory系统。其核心贡献是构建了一个基于Tree-Sitter的持久化知识图谱，通过模型上下文协议（MCP）为代理提供结构化的代码查询能力。方法上，系统采用多阶段流水线，包括并行工作池、调用图遍历、影响分析和社区发现（如Louvain算法），支持66种语言，能快速生成可查询的知识图谱。主要结论显示，在31个真实代码库的评估中，该系统以十分之一的令牌消耗和2.1倍更少的工具调用，实现了83%的答案质量（接近文件探索代理的92%），尤其在图原生查询（如枢纽检测和调用者排名）中表现优异。此外，系统通过静态链接的C二进制文件实现高效扩展，并集成了自动化发布验证流程，增强了供应链安全信任。这为基于LLM的代码智能提供了高效且可靠的结构化检索基础。
