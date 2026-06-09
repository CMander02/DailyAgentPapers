---
title: "QueryWeaver: Reliable Multi-Tool Query Execution Planning via LLM-Based Graph Generation"
authors:
  - "Aishwarya Chakravarthy"
  - "Vidhi Kulkarni"
  - "Duen Horng Chau"
date: "2026-06-06"
arxiv_id: "2606.08300"
arxiv_url: "https://arxiv.org/abs/2606.08300"
pdf_url: "https://arxiv.org/pdf/2606.08300v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Multi-Step Planning"
  - "Query Execution"
  - "Graph-Based Planning"
relevance_score: 8.5
---

# QueryWeaver: Reliable Multi-Tool Query Execution Planning via LLM-Based Graph Generation

## 原始摘要

Many real-world queries over personal data span multiple applications and require structured planning, as individual tools expose only partial information. While LLMs show strong reasoning and tool use, reliably executing multi-step, cross-tool queries remains challenging. We introduce a system that converts natural language queries into structured graphs and executes them via a deterministic planner. Our approach uses depth-first search to resolve dependencies and combine results across tools, improving reliability and enabling queries beyond traditional keyword-based search. We demonstrate high accuracy even with smaller or locally hosted LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决跨多应用的自然语言查询执行问题。研究背景是：现代个人数据分散在多个应用（如日历、邮件、文件等）中，用户常需要执行跨工具的多步查询（例如“上周在皮德蒙特公园见的人叫什么名字”），这需要协调多个工具获取信息并整合结果。现有方法的不足主要有两点：一是传统搜索工具（如 Spotlight、Windows Search）仅支持基于关键词的简单检索，无法处理跨应用、多步骤的复杂查询；二是尽管大语言模型具有一定推理和工具使用能力，但在复杂多步任务中，尤其是需要规划和工具协调时，性能会显著下降，且依赖大型专有模型时成本高、可靠性差。本文要解决的核心问题是：如何让LLM可靠地执行跨工具的多步查询，通过将自然语言查询转化为结构化图表示，并利用确定性规划器（深度优先搜索）决定工具调用顺序和依赖关系，从而避免传统Agent式工具调用中LLM的不可靠性，实现对复杂查询的端到端执行。

### Q2: 有哪些相关研究？

相关研究主要集中在以下方面：

方法类：ReAct和Toolformer将推理与工具调用交织，Plan-and-Solve通过分离规划与执行提高准确性。这些方法依赖线性推理，在多步跨工具查询中可靠性不足。Graph of Thoughts、Graph Chain-of-Thought、Tree-of-Traversals和GTool采用图结构建模，通过结构化遍历引导多步多工具任务，与本文思路相近。本文的区别在于：将自然语言查询转化为依赖图，并用确定性的深度优先搜索解析依赖并合并结果，而非依赖LLM的逐步推理。

应用类：现有工作大多基于LLM进行线性或树状推理，如LLM生成对象级计划或过渡函数，与经典框架结合作为高层规划器。本文创新性地将图生成与确定性执行结合，使系统能处理传统关键词搜索无法胜任的跨工具多步查询。

评测类：本文证明即使使用较小的本地LLM，该方法的准确率也较高，与依赖强大LLM推理的方法形成对比，体现了混合架构对LLM规模的鲁棒性。

### Q3: 论文如何解决这个问题？

QueryWeaver的核心方法是利用LLM将自然语言查询转化为结构化的有向图表示，然后通过一个确定性的深度优先搜索（DFS）规划器来执行该图。整体框架由两个主要阶段组成：图生成和图执行。

在图生成阶段，LLM充当翻译器，将用户查询映射为包含节点（如Email、Person、Self等）、边（如`from`、`attended`等关系）、过滤器、动作（find/count）及返回变量等元素的图结构`G`。关键创新在于将边的方向性视为无向，避免LLM直接指定执行顺序，从而降低其推理复杂度。

在图执行阶段，系统采用DFS算法从返回变量节点开始遍历图。算法核心是维护一个已访问集合和变量到候选集的映射。DFS会递归处理，识别出没有未访问邻居的“绑定节点”（如Date和Self节点），这些节点可独立通过本地过滤器或LLM（处理模糊日期表达式）解析。解析后，算法回溯并利用双向的工具调用（如`self_attended_event`的左到右和`event_occurred_on_date`的右到左工具）来传播和组合候选集，最终通过边和过滤器的约束逐步求出目标节点（如Webpage）的结果。

系统通过将LLM的规划能力与确定性的图执行逻辑结合，实现了高可靠性，即使使用小型或本地部署的LLM也能取得高准确率。

### Q4: 论文做了哪些实验？

论文在7个跨应用复杂查询上评估了QueryWeaver系统，这些查询源自Feldspar数据集，涉及邮件、文件、日历等多工具联合操作（如“找出二月事件中见过的人发来的邮件中提到的网页”）。实验使用两类模型：外部模型GPT-5.4和本地模型GPT-OSS:20B（中等推理强度）。主要对比方法是传统基于关键词的操作系统搜索。实验结果显示：在图表生成准确率（Graph）和执行准确率（Exec）上，GPT-5.4和GPT-OSS均达到100%；平均运行时分别为30.469秒和61.161秒，表明QueryWeaver即使使用较小或本地LLM也能可靠执行复杂多步跨工具查询，且外部模型速度更快。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于当前图结构相对固定，难以灵活适配用户多变的查询意图，且DFS执行策略在深度路径中可能产生较大中间搜索空间。未来可探索以下方向：1) 构建自适应图模式，通过用户反馈或查询历史动态扩充节点类型和边关系，使系统能处理更复杂的跨工具依赖；2) 引入代价模型驱动的执行规划，例如结合谓词选择性估计，优先执行过滤性最强的子任务以缩减中间结果集；3) 研究混合型规划器，将LLM的语义推断与符号规划的可靠性结合，对高不确定性分支采用回溯或并行试探策略；4) 针对数据敏感场景，设计图结构中的隐私约束标注机制，确保跨工具查询时不泄露原始数据。此外，可考虑将执行轨迹反馈回LLM以迭代优化图生成，形成闭环自改进能力。

### Q6: 总结一下论文的主要内容

该论文提出了QueryWeaver系统，旨在解决跨多工具执行自然语言查询的可靠规划问题。核心贡献在于将自然语言查询转化为结构化图，并通过确定性规划器执行，从而克服了单独工具仅提供部分信息的局限。方法上，系统利用LLM生成查询图，采用深度优先搜索解析工具间的依赖关系并合并结果，实现了比传统关键词搜索更复杂的跨工具查询。主要结论表明，即使使用较小的或本地部署的LLM，该系统也能实现高准确率，显著提升了多步骤、跨工具查询的可靠性。这项工作的意义在于为个人数据跨应用查询提供了可靠的结构化规划方案。
