---
title: "CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence"
authors:
  - "Tarakanath Paipuru"
date: "2026-02-23"
arxiv_id: "2602.20048"
arxiv_url: "https://arxiv.org/abs/2602.20048"
pdf_url: "https://arxiv.org/pdf/2602.20048v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent 架构"
  - "工具使用"
  - "Agent 评测/基准"
  - "代码智能体"
  - "导航悖论"
  - "模型行为对齐"
relevance_score: 9.0
---

# CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence

## 原始摘要

Modern code intelligence agents operate in contexts exceeding 1 million tokens--far beyond the scale where humans manually locate relevant files. Yet agents consistently fail to discover architecturally critical files when solving real-world coding tasks. We identify the Navigation Paradox: agents perform poorly not due to context limits, but because navigation and retrieval are fundamentally distinct problems. Through 258 automated trials across 30 benchmark tasks on a production FastAPI repository, we demonstrate that graph-based structural navigation via CodeCompass--a Model Context Protocol server exposing dependency graphs--achieves 99.4% task completion on hidden-dependency tasks, a 23.2 percentage-point improvement over vanilla agents (76.2%) and 21.2 points over BM25 retrieval (78.2%).However, we uncover a critical adoption gap: 58% of trials with graph access made zero tool calls, and agents required explicit prompt engineering to adopt the tool consistently. Our findings reveal that the bottleneck is not tool availability but behavioral alignment--agents must be explicitly guided to leverage structural context over lexical heuristics. We contribute: (1) a task taxonomy distinguishing semantic-search, structural, and hidden-dependency scenarios; (2) empirical evidence that graph navigation outperforms retrieval when dependencies lack lexical overlap; and (3) open-source infrastructure for reproducible evaluation of navigation tools.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决代码智能体在大型代码库中导航的根本性难题，即“导航悖论”。随着大模型上下文窗口的扩大，传统观点认为将所有文件放入上下文就能解决检索问题。然而，论文指出，即使代码库完全在上下文内，智能体仍然经常无法发现对任务至关重要的、结构上相关但语义上不明显的文件（例如，修改基类需要更新所有实例化点）。这是因为代码库本质上是依赖关系图，而基于关键词或语义相似性的检索方法无法捕捉这种结构关联。

因此，论文的核心问题是：如何让代码智能体超越简单的语义检索，有效地在代码的结构依赖图中进行导航，以发现那些“隐藏的依赖关系”。为此，论文提出了CodeCompass工具，它通过模型上下文协议（MCP）向智能体暴露代码的静态依赖图，将导航能力作为一等公民提供给智能体进行推理。研究通过实验验证了在依赖关系缺乏词汇重叠的任务上，基于图的导航方法相比普通智能体或BM25检索有显著优势（提升超过20个百分点），同时也揭示了智能体行为对齐的挑战——即使工具可用，也需要明确的提示工程引导智能体去使用结构信息而非依赖词汇启发式方法。

### Q2: 有哪些相关研究？

本文的相关工作主要涵盖四个领域，它们共同构成了本研究的背景和对比基础。

在**仓库级代码编辑**方面，SWE-bench 是评估智能体在真实Python仓库中解决GitHub问题的基准测试。主流方法（如Agentless）采用基于检索（如BM25、嵌入相似度）的文件定位策略。本文工作与之互补，构建了一个受控基准，将依赖类型（语义、结构、隐藏）作为首要实验变量，专注于隔离导航行为而非整体补丁质量。

在**代码知识图谱**方面，RepoGraph、CodexGraph 和 KGCompass 等工作都认同图结构优于扁平检索的直觉，但评估任务（代码补全、修复）和指标不同。Seddik等人（2026）的编程知识图谱（PKG）框架最为接近，它构建AST衍生的层次图用于代码生成的检索增强。关键区别在于：PKG是针对自包含问题的生成任务的检索增强，而CodeCompass是针对多文件代码库的智能体编辑任务的导航工具；PKG是查询前操作（离线建图，推理时检索），CodeCompass是交互式操作（任务执行期间遍历图谱）。

在**长上下文LLM的上下文利用**方面，“Lost-in-the-middle”现象及相关研究表明，即使目标信息存在于上下文中，LLM也可能无法有效利用。这些发现是本文“导航显著性假设”在注意力层面的类比，两者都源于对LLM能否正确使用可用信息的根本关切，尽管本文工作在更粗的粒度（文件发现 vs. 上下文内注意力）上进行。

在**MCP与智能体工具使用**方面，模型上下文协议（MCP）为向LLM暴露工具和数据源提供了标准化接口。据本文所知，CodeCompass是首个公开发布的、专门设计用于暴露静态代码依赖图以进行智能体导航评估的MCP服务器。

本文与这些工作的关系是：它继承了SWE-bench对仓库级任务的关注，但通过引入依赖类型分类深化了问题分析；它借鉴了代码知识图谱利用结构信息的思路，但将其应用场景从生成转向了导航，并强调了交互式遍历；它呼应了长上下文利用的研究，将问题从模型内部注意力扩展到了智能体的外部文件发现行为；最后，它在MCP的生态中实现了一个新的、专门化的工具服务器。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CodeCompass的基于图的结构化导航系统来解决代码智能体在大型代码库中难以发现关键依赖文件的“导航悖论”问题。核心方法是利用代码的结构化依赖关系（如导入、继承、实例化）来引导智能体，而非依赖传统的基于关键词的语义检索。

**核心方法与架构设计**：
1.  **图构建**：使用Python的AST模块解析代码库，提取三种类型的依赖边（IMPORTS, INHERITS, INSTANTIATES），构建成一个有向图（存储在Neo4j中）。该图以文件为节点，依赖关系为边，精确刻画了代码的架构连接。
2.  **导航工具**：将图封装成一个Model Context Protocol (MCP) 服务器，向智能体暴露一个关键工具：`get_architectural_context(file_path)`。该工具查询指定文件的1跳邻域（入边和出边），返回其直接的结构邻居文件列表。
3.  **实验与评估**：在一个真实的FastAPI代码库上构建了包含30个任务的基准测试，并将任务分为三类（语义搜索、结构依赖、隐藏依赖），以系统评估不同方法。实验对比了三种条件：无增强的原始智能体（A）、基于BM25检索增强的智能体（B）、以及使用CodeCompass图导航的智能体（C）。

**关键技术**：
- **结构化导航 vs. 语义检索**：论文的核心洞见是指出导航（基于结构连接发现文件）和检索（基于词汇匹配查找文件）是根本不同的问题。对于缺乏词汇重叠的隐藏依赖（G3任务），图导航通过追踪代码间的静态依赖链，能直接发现相关文件，而BM25检索则完全失效。
- **1跳邻域查询**：`get_architectural_context` 工具的设计是关键。它不进行复杂的多跳推理，而是返回目标文件的直接结构上下文。这简单有效，因为许多关键的架构依赖就在一跳之内（如图中示例，一次调用即可横跨领域模型、模式、服务、测试等多个架构层）。
- **行为对齐的提示工程**：研究发现，仅仅提供图工具（条件C）是不够的，58%的试验中智能体根本未调用该工具。因此，必须通过明确的提示工程（在任务提示中指示智能体首先对主任务文件调用该工具，并读取所有返回的邻居文件）来引导智能体改变其默认的、依赖词汇启发式的行为，转而采用结构化导航策略。这揭示了工具可用性之外的“行为对齐”瓶颈。

最终，CodeCompass在图导航条件下，在隐藏依赖任务上实现了99.4%的任务完成率，显著优于原始智能体（76.2%）和BM25检索（78.2%），证明了基于图的结构化导航在解决代码智能体导航悖论上的有效性。

### Q4: 论文做了哪些实验？

论文在真实生产环境的FastAPI代码库上设计了30个基准任务，进行了258次自动化实验。实验设置了三种条件进行对比：A（Vanilla，无额外检索）、B（BM25关键词检索）和C（基于依赖图的导航工具CodeCompass）。任务被分为三类：G1（语义搜索）、G2（结构依赖）和G3（隐藏依赖）。

主要结果如下：在G3隐藏依赖任务上，图导航（Condition C）取得了99.4%的平均代码覆盖率（ACS），相比基础智能体（76.2%）提升了23.2个百分点，相比BM25检索（78.2%）提升了21.2个百分点，且统计显著性极高（p<0.001）。然而，实验揭示了一个关键的行为采纳问题：在Condition C的88次试验中，有58%（51次）的试验完全没有调用图导航工具，导致其平均覆盖率降至80.2%，与基础智能体无异。但当工具被使用时，平均覆盖率高达99.5%。进一步的提示工程（如在提示末尾加入强制性检查清单）成功将G3任务的工具采纳率提升至100%，并进一步提高了性能。此外，实验还发现，在G2结构任务上，图导航的表现（76.4%）反而低于基础智能体（79.7%）和BM25（85.1%），且工具采纳率为零，表明智能体在任务看似可解时会理性地避免使用工具，尽管这可能牺牲架构完整性。

### Q5: 有什么可以进一步探索的点？

本文揭示了工具采纳是核心瓶颈而非工具能力本身。未来可探索的方向包括：1. **工作流结构性强制**：设计系统使图工具调用成为必经步骤（如通过 `tool_choice` 强制初始调用），而非依赖提示词引导，以解决代理在简单任务上“理性忽略”工具的问题。2. **自适应导航策略**：开发能动态感知任务难度（如通过初步探索判断是否存在隐藏依赖）并据此切换导航策略（词法启发式 vs. 结构导航）的智能体，实现成本与收益的平衡。3. **高质量图构建与维护**：研究如何融入领域专家知识来验证和增强自动生成的依赖图，并建立图的持续更新机制，因为陈旧的错误依赖图可能比没有图更糟。4. **泛化与评估**：将研究扩展到更多编程语言、代码库架构和智能体模型，以验证结论的普适性；同时开发能同时衡量导航完整性与代码正确性的综合评估指标。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了“导航悖论”，并开发了CodeCompass工具来解决智能代码代理在大型代码库中的导航问题。研究发现，随着LLM上下文窗口的扩大，代理的失败模式从检索容量不足转变为导航显著性不足。论文通过258次实验证明，基于图结构的导航工具在处理隐藏依赖任务时，能将任务完成率提升至99.4%，比传统代理和BM25检索分别高出23.2和21.2个百分点。然而，研究也揭示了一个关键瓶颈：代理的行为对齐。高达58%的试验在拥有图工具访问权限时却未调用该工具，表明工具可用性并非限制因素，代理需要明确的提示工程引导才能持续利用结构上下文而非词汇启发式方法。论文的意义在于指出，对于生产部署，可能需要通过强制工具选择或多代理流水线来实现结构化工作流，以充分发挥图导航在复杂、非语义重构任务中的潜力。
