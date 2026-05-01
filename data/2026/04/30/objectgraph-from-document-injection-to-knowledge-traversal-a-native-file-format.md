---
title: "ObjectGraph: From Document Injection to Knowledge Traversal -- A Native File Format for the Agentic Era"
authors:
  - "Mohit Dubey"
  - "Open Gigantic"
date: "2026-04-30"
arxiv_id: "2604.27820"
arxiv_url: "https://arxiv.org/abs/2604.27820"
pdf_url: "https://arxiv.org/pdf/2604.27820v1"
categories:
  - "cs.AI"
  - "cs.DB"
  - "cs.IR"
  - "cs.MA"
tags:
  - "Agent文件格式"
  - "知识图谱"
  - "文档消费"
  - "上下文窗口优化"
  - "Token缩减"
  - "多智能体协议"
  - "形式化文档建模"
relevance_score: 9.5
---

# ObjectGraph: From Document Injection to Knowledge Traversal -- A Native File Format for the Agentic Era

## 原始摘要

Every document format in existence was designed for a human reader moving linearly through text. Autonomous LLM agents do not read - they retrieve. This fundamental mismatch forces agents to inject entire documents into their context window, wasting tokens on irrelevant content, compounding state across multi-turn loops, and broadcasting information indiscriminately across agent roles. We argue this is not a prompt engineering problem, not a retrieval problem, and not a compression problem: it is a format problem.
  We introduce OBJECTGRAPH (.og), a file format that reconceives the document as a typed, directed knowledge graph to be traversed rather than a string to be injected. OBJECTGRAPH is a strict superset of Markdown - every .md file is a valid .og file - requires no infrastructure beyond a two-primitive query protocol, and is readable by both humans and agents without tooling.
  We formalize the Document Consumption Problem, characterise six structural properties no existing format satisfies simultaneously, and prove OBJECTGRAPH satisfies all six. We further introduce the Progressive Disclosure Model, the Role-Scoped Access Protocol, and Executable Assertion Nodes as native format primitives. Empirical evaluation across five document classes and eight agent task types demonstrates up to 95.3 percent token reduction with no statistically significant degradation in task accuracy (p > 0.05). Transpiler fidelity reaches 98.7 percent content preservation on a held-out document benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有文档格式与自主LLM智能体之间存在的根本性不匹配问题，即“文档消费问题”。当前所有主流文档格式（如Markdown、JSON、YAML等）都是为人类线性阅读设计的。当智能体处理任务时，它们不是“阅读”而是“检索”，但现有格式强制智能体将整个文档注入其上下文窗口，导致一系列核心失效：首先，**Token膨胀**，智能体读取文档的全部内容，但实际与任务相关的平均内容仅占6.3%，造成大量token浪费；其次，**上下文复合**，在智能体的多轮交互循环中，由于API无状态，每次调用都需重传全部历史记录，导致单次文档读入的成本在多轮中呈超线性增长；最后，**角色盲区**，现有格式无法根据智能体的不同角色（如编排者、执行者、监控者）提供差异化的内容视图，导致信息无差别广播。

论文的核心论点在于，这并非提示工程、检索增强生成或压缩技术能解决的问题，而是一个本质上的**格式问题**。因此，本文提出一个原生面向智能体的文件格式OBJECTGRAPH，将文档重新构想为一个可在其上遍历的、带类型的有向知识图谱，而非被整体注入的字符串。其核心目标是同时满足六个现有格式无法兼顾的关键属性：可查询索引、分层压缩、类型化依赖图、角色作用域访问控制、可执行断言以及人类可读性，从而实现高达95.3%的token缩减并保持任务精度。

### Q2: 有哪些相关研究？

**方法类相关工作：**
- **上下文压缩**：通过内容移除减少token消耗，如去除无用/冗余/过期信息实现39.9–59.7%输入token减少，或通过渐进式披露实现48%描述压缩。本文区别在于这些方法仍在注入模型内压缩，未消除全文读取或上下文累积问题。
- **结构化知识表示**：对比YAML/Markdown/JSON/TOON等格式的agent性能，TOON实现25–46% token减少但仅限序列化。本文提供图遍历、依赖解析和人机共写能力。

**应用类相关工作：**
- **图基知识表示**：从文档语料构建实体图需向量数据库和离线索引，不适合通用文档格式。本文原生支持图结构无需外部基础设施。
- **文件原生agent上下文**：CLAUDE.md/AGENTS.md等静态注入文件无查询接口。本文提供双原语查询协议，直接取代注入模式。

**技能表示类相关工作：**
- SSL表示法关注技能内部结构但未涉及文件格式。本文可存储SSL结构化技能作为节点。

本文核心区别：重新定义文档格式为知识图谱而非字符串，首次实现无基础设施需求的图遍历、角色作用域访问、渐进式披露和可执行断言节点。

### Q3: 论文如何解决这个问题？

ObjectGraph通过将文档重新构思为类型化、有向的知识图谱来解决LLM智能体的文档消耗问题，而非传统的线性文本注入。核心创新在于一种原生文件格式（.og），它既是Markdown的超集，又通过一个仅需两种原语的查询协议实现拓扑遍历。

整体框架包含三个主要组件：**文件级清单**、**渐进式披露模型（PDM）**和**角色限定访问协议**。清单是关键的索引创新，由三个必选块组成：meta（元数据）、schema（模式定义）和index（路由表）。其中index块仅需约30个token，提供完整的节点路由表，使智能体无需加载任何内容即可确定任务相关性。PDM通过三种读取深度消除token膨胀：Pass 1（索引扫描，约30个固定token）、Pass 2（密集摘要，每节点约10-15个token）和Pass 3（完整读取，每节点约100-300个token）。典型场景下可实现87%的token节省。

关键技术包括**自动依赖遍历**——当查询协议解析一个节点时，自动追踪所有:requires边并获取前置节点；**可执行断言节点**——直接在文档中编码验证逻辑、重试路由和升级路径，消除在提示词中编码验证逻辑的需求；以及**会话级skip-if-known过滤器**——跨多轮交互记忆已访问节点，进一步节省token。格式层面还实现了**角色限定访问控制**，通过scope属性确保不同角色的智能体只能看到与其相关的节点内容，例如orchestrator角色可以看到真实凭证，而worker角色只能看到安全抽象的凭证信息。

### Q4: 论文做了哪些实验？

论文构建了一个包含240份文档的基准测试集（技能文件48份、操作手册52份、执行计划44份、技术文档56份、知识库40份），文档长度从200到15000个token不等（中位数1680）。定义了8类代理任务：信息查找、流程执行、多步规划、角色条件访问、跨节点推理、更新检测、断言验证和多智能体交接，每个文档-任务对重复执行5次。对比方法包括全Markdown注入(B1)、基于text-embedding-3-large的RAG(B2)和SkillReducer优化Markdown(B3)，使用Claude Sonnet 4.5、Haiku 4.5和GPT-4o进行评估。

主要结果：ObjectGraph (Arch.A)将平均token消耗从2340降至187（92.0%降幅，p<0.001），Arch.B在大型操作手册上进一步降至130-220 tokens。在5轮工作流中，Markdown累计消耗46,000 tokens，而Arch.B仅需1,260 tokens（36.5倍减少）。任务准确率方面，ObjectGraph在7/8任务上匹配或超越Markdown基线，唯一例外是跨节点推理（差距从4.2%缩小至1.8%通过显式边声明）。最高token减少达95.3%（操作手册类），全文保留率达98.7%。

### Q5: 有什么可以进一步探索的点？

基于论文内容和我的专业判断，未来探索可从以下方向展开：**1. 复杂知识推理与动态更新**。论文中Executable Assertion Nodes尚无法处理深度因果推理和跨文档时间线冲突，建议构建基于超图（Hypergraph）的推理引擎，支持节点间动态依赖关系学习。**2. 多模态扩展**。当前格式仅支持文本，可引入视觉-语言跨模态对齐技术，将图片/表格的语义信息编码为结构化节点，实现非文本内容的token级精准检索。**3. 协作协议层优化**。Role-Scoped Access Protocol在百万级节点场景下存在权限粒度不足问题，可借鉴属性基加密（ABE）设计分层追踪协议，配合差分隐私机制实现细粒度信息暴露控制。**4. 自适应压缩策略**。95.3%的token缩减在长尾知识节点（如罕见API参数）上可能因过度压缩导致关键信息丢失，需开发基于信息熵的节点重要性动态评估算法，平衡压缩率与恢复保真度。

### Q6: 总结一下论文的主要内容

该论文提出了一种面向自主LLM智能体的新型文件格式ObjectGraph (.og)，以解决现有文档格式（如Markdown）与智能体工作方式之间的根本性不匹配问题。当前智能体需要将完整文档注入上下文窗口，导致严重的token浪费（利用率仅约6.3%）和上下文复合问题。论文将文档重新构想为一个带类型的、有向的知识图谱，智能体通过两个原语（search_index和resolve_context）进行查询遍历，而非整体注入。该方法定义了文档消费问题，并证明ObjectGraph同时满足查询可寻址索引、分层压缩、类型化依赖图、角色作用域访问控制、可执行断言和人类可读性六项必要属性。实验表明，在五种文档类别和八种任务类型上，该方法实现了高达95.3%的token缩减，同时任务准确性无统计学显著下降。核心贡献在于将问题重新定义为格式问题而非工程问题，提供了向后兼容Markdown的即用方案。
