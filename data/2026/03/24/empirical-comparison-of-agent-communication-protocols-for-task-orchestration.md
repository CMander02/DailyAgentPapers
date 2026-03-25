---
title: "Empirical Comparison of Agent Communication Protocols for Task Orchestration"
authors:
  - "Ivan Dobrovolskyi"
date: "2026-03-24"
arxiv_id: "2603.22823"
arxiv_url: "https://arxiv.org/abs/2603.22823"
pdf_url: "https://arxiv.org/pdf/2603.22823v1"
categories:
  - "cs.AI"
tags:
  - "Agent Communication"
  - "Benchmark"
  - "Multi-Agent Systems"
  - "Tool Use"
  - "LLM Orchestration"
  - "Empirical Study"
relevance_score: 8.5
---

# Empirical Comparison of Agent Communication Protocols for Task Orchestration

## 原始摘要

Context. Nowadays, artificial intelligence agent systems are transforming from single-tool interactions to complex multi-agent orchestrations. As a result, two competing communication protocols have emerged: a tool integration protocol that standardizes how agents invoke external tools, and an inter-agent delegation protocol that enables autonomous agents to discover and delegate tasks to one another. Despite widespread industry adoption by dozens of enterprise partners, no empirical comparison of these protocols exists in the literature. Objective. The goal of this work is to develop the first systematic benchmark comparing tool-integration-only, multi-agent delegation, and hybrid architectures across standardized queries at three complexity levels, and to quantify the trade-offs in response time, context window consumption, monetary cost, error recovery, and implementation complexity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个在LLM驱动的智能体（Agent）系统设计与实践中日益凸显但缺乏实证数据指导的关键问题：如何选择智能体通信协议？具体而言，随着智能体系统从单一工具调用演变为复杂的多智能体编排，两种主流的通信协议——由Anthropic提出的Model Context Protocol（MCP，用于标准化智能体调用外部工具）和由Google提出的Agent-to-Agent Protocol（A2A，用于实现智能体间的发现与任务委派）——在业界被广泛采用，但学术界缺乏对它们性能特性的系统性实证比较。论文指出，现有的唯一相关工作（Chen et al., 2025）仅为理论分析，导致实践者在选择协议时只能依赖直觉而非数据。因此，本文的目标是填补这一空白，通过开发首个系统性的基准测试，量化比较MCP-only、A2A多智能体和混合（Hybrid）三种架构在不同查询复杂度下的性能权衡，包括响应时间、上下文窗口消耗（Token数）、成本、错误恢复和实现复杂性，从而为协议选择提供一个基于证据的决策框架。

### Q2: 有哪些相关研究？

相关研究主要分为三个层面：工具使用基础、多智能体框架以及协议本身的理论分析。在工具使用基础方面，论文引用了Schick等人的Toolformer（让语言模型学会调用工具）、Patil等人的Gorilla（提升API调用准确性）以及Yao等人的ReAct（推理-行动循环），这些工作奠定了现代智能体使用工具的能力，但未涉及智能体间的通信协议。在多智能体框架方面，论文提到了Wu等人的AutoGen（可对话的多智能体系统）、Moura的CrewAI（基于角色的编排）以及Hong等人的MetaGPT（用于软件工程的多智能体协作），这些框架都实现了各自的专有通信机制，但并未采用MCP或A2A这类标准化协议。在协议本身，论文引用了Anthropic发布的MCP规范和Google发布的A2A规范，并特别指出了Chen等人的理论分析工作，该工作首次从理论上比较了MCP和A2A，并指出了它们的互补性，但缺乏实证测量。本文正是在此基础上，首次通过受控实验对这两种标准化协议进行了头对头的实证基准测试，解决了现有文献中缺乏实证数据指导协议选择的空白。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的实证研究方法来解决协议比较问题。首先，构建了一个统一的实验应用——“开源健康分析器”，该应用能够根据自然语言查询，从GitHub、npm、OSV.dev和StackOverflow四个公共API获取数据。然后，将完全相同的应用逻辑在三种不同的架构中实现：1）**MCP-Only架构**：一个单一的智能体通过stdio传输连接到四个MCP工具服务器，所有工具响应都累积在同一个LLM上下文窗口中。2）**A2A多智能体架构**：一个协调者智能体通过HTTP和JSON-RPC，使用A2A协议将子任务委派给四个独立的专家智能体（每个运行一个FastAPI服务器），每个专家智能体维护自己的上下文窗口。3）**混合架构**：一个基于关键词的轻量级路由层，根据查询复杂度将简单查询路由到MCP，复杂查询路由到A2A。为了系统评估，研究者定义了30个标准化查询，分为简单（单源单项目）、中等（多源单项目）和复杂（多源多项目比较）三个复杂度等级。每个查询在每个架构上执行5次，共产生450次执行。所有实验使用相同的LLM模型（Claude Sonnet）以控制变量。性能指标包括：端到端延迟、总LLM Token消耗（据此计算成本）、LLM API调用次数、数据源API调用次数以及代码复杂度（代码行数和圈复杂度）。最后，采用严格的非参数统计方法进行分析，包括计算95%的自举置信区间、使用Bonferroni校正的Mann-Whitney U检验进行显著性测试，以及使用Cliff's delta计算效应大小，以确保结果的统计稳健性。

### Q4: 论文做了哪些实验？

论文进行了大规模、受控的实验以收集可靠的性能数据。实验设置如下：所有执行在一台机器上进行，A2A智能体部署在本地主机以消除网络差异。针对30个预定义的查询（每个复杂度等级10个），在MCP、A2A和混合三种架构上各执行5次，总计450次完整执行。所有执行均实时查询四个外部API，未使用缓存。此外，还引入了故障注入测试（随机关闭一个API）以评估错误恢复能力，并部署了幻觉检测模块以确保输出中的所有事实声明都能追溯到实际的API响应数据。实验结果显示，所有450次执行均成功完成，零失败。核心实验结果揭示了显著的“交叉效应”：对于简单查询，MCP架构延迟显著更低（8.9秒 vs A2A的19.8秒，p<0.0001，效应量大）；对于中等复杂度查询，MCP仍保持优势（30.3秒 vs 36.0秒）；但对于复杂查询，A2A架构在延迟上反超（45.1秒 vs MCP的51.8秒，效应量中等），并且在Token消耗上优势巨大：A2A仅消耗11,318个Token，而MCP消耗34,959个Token，是A2A的3.1倍（p<0.0001）。这直接导致成本差异：处理复杂查询时，A2A成本（$0.079）比MCP（$0.130）低39%。混合架构在各级复杂度上都紧密跟踪性能更优的协议，实现了近乎最优的表现。统计检验确认了简单和复杂层级上所有成对比较的效应量均达到“大”级别，证实了差异的实质性。论文还量化了实现复杂性：A2A架构的代码行数（1530 LOC）是MCP架构（706 LOC）的2.2倍，圈复杂度也更高。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的局限性，这些也正是未来研究可以深入探索的方向。首先，**模型泛化性**：所有实验仅使用了Claude Sonnet一个模型，不同LLM（如GPT、Gemini等）在推理模式、上下文管理效率上的差异可能导致性能交叉点发生变化，需要扩展到更多模型进行验证。其次，**网络环境**：实验在本地主机进行，忽略了真实分布式部署中的网络延迟和带宽限制，这可能会增加A2A协议的HTTP通信开销，从而影响其性能优势，甚至改变交叉点。第三，**应用领域**：基准测试仅聚焦于开源项目分析这一特定领域，不同领域（如金融分析、科学计算）的任务特性和数据源模式可能对协议性能产生不同影响，需要扩展到更多应用场景。第四，**自适应路由**：本文的混合架构使用了基于关键词的启发式路由，未来可以探索更智能的自适应路由机制，例如基于机器学习模型实时预测查询复杂度或直接学习性能交叉点，以实现动态优化。第五，**协议组合**：论文提到MCP和A2A是互补的，未来可以研究更深度的协议栈融合，例如让A2A中的专家智能体内部使用MCP来调用工具，形成分层架构。最后，可以增加实验的规模和粒度，例如增加每个查询的重复执行次数以检测更小的效应，或者设计更细粒度的复杂度谱系来精确刻画性能转变的临界点。

### Q6: 总结一下论文的主要内容

这篇论文是首篇对LLM智能体两大主流通信协议——MCP（工具集成协议）和A2A（智能体间委派协议）——进行系统性实证比较的研究。通过构建一个开源健康分析器应用，并在MCP-only、A2A多智能体和混合三种架构上实现相同逻辑，论文设计了涵盖三个复杂度等级的30个查询，进行了总计450次受控实验。核心发现是一个统计显著的“性能交叉效应”：对于简单查询，MCP凭借零开销（无HTTP、无代理发现）在延迟上占优；但对于复杂查询，A2A则因分布式上下文窗口避免了单智能体架构中的“上下文窗口膨胀”问题，在Token消耗（减少68%）和成本（降低39%）上显著更优，并在延迟上也实现反超。混合架构通过轻量级路由实现了接近最优的折衷。论文不仅通过严谨的统计方法量化了这些权衡，还首次实证验证了MCP与A2A的互补性而非竞争关系。其核心贡献在于提供了一个基于证据的决策框架：简单任务用MCP，复杂编排用A2A，未知复杂度时用混合路由，为智能体系统架构师和开发者提供了宝贵的实践指导。所有代码和数据均已开源，促进了该领域的可重复研究和进一步发展。
