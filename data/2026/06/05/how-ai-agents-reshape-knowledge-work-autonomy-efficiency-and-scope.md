---
title: "How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope"
authors:
  - "Jeremy Yang"
  - "Kate Zyskowski"
  - "Noah Yonack"
  - "Jerry Ma"
date: "2026-06-05"
arxiv_id: "2606.07489"
arxiv_url: "https://arxiv.org/abs/2606.07489"
pdf_url: "https://arxiv.org/pdf/2606.07489v1"
categories:
  - "cs.AI"
  - "econ.GN"
tags:
  - "AI Agent"
  - "知识工作自动化"
  - "自主性"
  - "效率"
  - "Perplexity产品分析"
  - "任务分解"
  - "工作流加速"
  - "用户研究"
  - "实证分析"
relevance_score: 8.5
---

# How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope

## 原始摘要

Frontier AI systems are bridging the gap between intelligence and utility by shifting from conversational assistants to autonomous agents that execute tasks end to end. Using production data from Perplexity's Search and Computer products, we study this transition by examining how AI agents accelerate and reshape knowledge work. Three key empirical findings emerge. First, using sessions with near-identical initial query pairs as natural experiments for the same underlying task attempted with both products, Computer performs 26 minutes of autonomous work per user session, versus 33 seconds for Search. Computer automates task decomposition and execution that Search users might otherwise manually orchestrate and implement. As a result, Computer shifts follow-up query distribution toward higher-order work such as verification and extension. Autonomy also increases execution quality, with per-query dissatisfaction rates 55% lower on Computer than on Search. Second, due to its autonomy advantage, Computer reduces completion time from 269 to 36 minutes on matched tasks, lowering estimated time and cost by 87% and 94%, respectively, compared to humans equipped with Search alone. Third, Computer changes the scope of work that users attempt: Computer queries more often cross occupational boundaries, require higher-order cognition, draw on broader expertise, take the form of composite tasks that bundle interdependent subtasks into a single query, and unlock work activities that are essentially absent from Search usage among the same users. Together, the evidence indicates that AI agents accelerate workflows, enhance output quality, reduce costs, and expand the breadth and depth of automated work.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地研究AI从对话式助手（如搜索引擎）向自主代理（如 Computer 产品）转型如何重塑知识工作。研究背景是，尽管大语言模型能力快速提升，但现有AI产品大多停留在提供信息或辅助协作层面，用户仍需手动分解任务、执行中间步骤并协调多个工具，导致效率瓶颈和认知负荷。现有研究的不足在于：缺乏基于真实生产数据的现场证据来量化这种转型在任务层面的经济影响，尤其是自主性提升如何改变工作流程、成本结构和任务范围。本文的核心问题是：相比传统的对话式助手（Search），具有更高自主性的AI代理（Computer）在真实知识工作场景中能否显著提升执行效率、降低时间和成本、提高产出质量，并在多大程度上扩展用户尝试的工作类型——包括跨职业边界、更高阶认知需求、复合型任务以及全新工作活动。通过使用Perplexity平台上同一用户的匹配会话数据作为自然实验，论文从自主性程度、效率增益和工作范围三个维度提供了首个大规模实证证据。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **AI助手生产力影响**：实验证据显示生成式AI能显著提升工作效率，如ChatGPT减少写作时间40%，GitHub Copilot提升任务完成率26%。但本文指出这些研究聚焦于“人机交互式协作”，而本文研究的Computer产品通过异步委托取代交互循环，实现了更彻底的自动化。

2. **从辅助到自主Agent**：相关工作包括工具调用学习、多步推理优化及实际部署分析，如Cursor用户合并请求增加39%、Claude Code任务时长延长等。本文与此互补之处在于：对比自主Agent与对话助手的用户交互差异，并将影响分析从编码扩展到更广泛的知识工作。

3. **职业暴露与任务重组**：宏观估计显示80%美国职业可能受LLM影响，但测的是潜在替代而非实际变化。近期研究通过使用数据发现AI辅助略多于完全自动化，而本文首次从微观角度揭示：当用户从对话助手转向Agent时，任务会横向跨职业边界扩展、纵向向更复杂工作迁移，并重组为复合任务。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于任务步骤数的成本-价值理论框架，并结合Perplexity的Search（对话模式）和Computer（代理模式）的生产数据来验证假设。核心方法是将用户会话作为自然实验，比较两种模式下相同初始查询的任务执行差异。

整体框架从四个关键假设出发：任务价值随步骤数递增、价值仅在任务完全完成后实现、代理模式固定成本更高但边际成本更低。基于此推导出关键阈值$s^*$：当任务步骤数低于该阈值时，对话模式更优；高于阈值时，代理模式更优，因为其更高的固定成本能被更低的边际成本摊薄。

主要模块包括：1) **成本结构分析**：验证代理模式确实降低了边际成本，Computer每会话自主执行26分钟工作而Search仅33秒，验证了代理模式更低的每步成本；2) **效率提升量化**：在匹配任务上，Computer将完成时间从269分钟降至36分钟（降87%），成本降低94%；3) **范围扩展分析**：Computer处理的查询更常跨职业边界、需要高阶认知、涉及复合任务（捆绑多个子任务），并且解锁了Search中几乎不存在的活动类型。

创新点在于：1) 提出了可分解为密集（成本节省）、进入（新任务价值）和退出（放弃任务损失）三个边际的剩余变化分解方法；2) 实证证明了代理模式不仅加速现有工作，还从根本上改变了用户尝试工作的范围和复杂度，使更高价值、更复杂的任务变得经济可行。

### Q4: 论文做了哪些实验？

论文基于Perplexity的Search（对话式）和Computer（自主式）两个产品，设计了一系列实验来对比AI Agent与传统AI助手在知识工作中的表现。实验设置采用匹配对设计：从同一用户群体中筛选出分别使用Computer和Search提交过近完全相同初始查询（余弦相似度>0.99）的会话对，共10,000对，覆盖7个样本。数据集包括90天内的查询日志，以及针对100,000条Computer查询的LLM分类标签。

实验主要围绕三个核心发现展开：
1. **自主性**：Computer每会话平均执行26分钟（中位数9分钟），而Search仅33秒（中位数14秒），执行时间比约为48倍。Computer的查询不满意率比Search低55%（未给出具体百分比）。Computer有38%的会话触发暂停请求（如审批、澄清），而Search仅0.8%。在外部工具调用（连接器）方面，Computer会话平均调用1.19次，Search仅0.10次。
2. **效率**：在匹配任务上，Computer将完成时间从269分钟（Search+人工）缩短至36分钟，时间成本降低87%，总成本降低94%。该结果基于工具级和LLM级两种估算方法，并辅以25名用户的访谈验证。
3. **工作范围**：Computer的查询更常跨越职业边界（8个职业簇），需要更高阶认知（基于Bloom修订分类法），涉及更广泛专业知识（O*NET知识领域），并捆绑复合子任务。此外，Computer解锁了Search中使用完全缺失的工作活动（新任务）。具体数据方面，Computer用户中Search查询增长了14倍（非用户为12倍），并通过双重差分法证明Computer采纳使每日Search查询增加1.05次。Computer查询中，研究与分析（25.8%）和文档/资产创建（18.6%）是最常见的任务类别，领域分布广泛，软件与IT（13.8%）和金融投资（10.8%）领先。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：研究仅基于Perplexity单一平台的分析数据，缺乏跨平台比较；用户样本可能偏向技术早期采用者，结论的普适性待验证；对"工作质量"的评估指标（如用户满意度）较为单一，未考虑长期知识内化效果。未来方向可包括：1）研究不同专业领域（如法律、医疗）中agent自主性的差异化影响，探索领域适配的智能阈值；2）设计人机协作的混合自主架构，允许用户在关键决策点介入，平衡效率与认知控制；3）构建动态任务分解模型，使agent能自主识别需要人类参与的子任务；4）研究agent长期使用对用户思维模式的影响，特别是"认知卸载"可能导致的核心技能衰退；5）开发agent行为透明化技术，增强用户对自主执行过程的信任与理解。

### Q6: 总结一下论文的主要内容

这篇论文通过Perplexity搜索引擎和Computer代理产品的对比，实证研究了AI代理如何重塑知识工作。核心贡献在于提供了首个基于生产数据的任务级经济效应证据。问题定义聚焦于从对话式助手到自主代理的转变如何影响工作流程。方法上，利用同一用户的相近初始查询对作为自然实验，对比两种产品的表现。主要结论包括：第一，Computer每会话执行26分钟自主工作，而Search仅33秒，自主性提升48倍；同时Computer的查询不满意率比Search低55%。第二，在匹配任务中，Computer将完成时间从269分钟降至36分钟，时间和成本分别降低87%和94%。第三，Computer扩展了用户尝试的工作范围，更多跨职业边界、需要高阶认知、涉及复合任务，并解锁了Search中几乎不存在的新工作活动。这项研究的意义在于证明AI代理不仅加速工作流程、提升质量、降低成本，还显著扩展了自动化工作的广度和深度，对职业和组织结构有深远影响。
