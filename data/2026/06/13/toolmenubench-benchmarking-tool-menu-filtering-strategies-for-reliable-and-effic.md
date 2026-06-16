---
title: "ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents"
authors:
  - "Rahul Suresh Babu"
  - "Laxmipriya Ganesh Iyer"
date: "2026-06-13"
arxiv_id: "2606.15508"
arxiv_url: "https://arxiv.org/abs/2606.15508"
pdf_url: "https://arxiv.org/pdf/2606.15508v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Augmented Agent"
  - "Tool Selection"
  - "Agent Benchmark"
  - "Safety"
  - "Efficiency"
  - "LLM Agent"
  - "Tool Menu Filtering"
relevance_score: 8.5
---

# ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents

## 原始摘要

Tool-augmented large language model agents increasingly operate over large tool libraries, but existing evaluations often focus on whether a model can call a tool correctly rather than how the visible tool menu shapes reliability, efficiency, and safety-relevant risk exposure. We introduce ToolMenuBench, a benchmark for evaluating tool-menu construction in multi-step LLM agents. ToolMenuBench varies tool-menu size, distractor type, state-dependent task structure, and risk exposure, and reports both filter-level and downstream agent metrics, including visible-tool count, risky-tool exposure, task success, wrong-tool calls, premature actions, and token usage. In a controlled evaluation across seven model backends, three tool-menu sizes, six filtering methods, and seven evaluation settings, CMTF improves task success from 32.1% under all-tools exposure to 85.7%, while reducing average token usage by roughly 98%. Causal minimal tool filtering achieves the strongest overall tradeoff, reducing visible tools, wrong-tool calls, premature actions, and risky-tool exposure relative to unfiltered exposure, lexical filtering, state-aware filtering, and broader causal-path baselines. ToolMenuBench provides a reusable evaluation framework for studying the agent-interface problem: which tools should be visible, when they should be visible, and under what cost or risk constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）代理在大型工具库环境下，由于可见工具菜单设计不当导致的可靠性、效率和安全性问题。现有研究多聚焦于模型能否正确调用单个工具，而忽略了工具菜单本身的选择、大小、干扰项分布对代理决策的影响。现有方法将工具集视为固定或给定的，未能系统评估菜单过滤策略。当面对众多语义相似、部分重叠、操作过早、存在风险或无关的工具时，代理容易做出错误调用、过早行动，并消耗大量令牌。同时，仅基于语义相似度的检索或剪枝可能推荐因果上不合适的工具，增加了不必要的风险暴露。

论文的核心问题是：在多步骤代理任务中，如何构建一个既高效又可靠的可见工具菜单？具体来说，需要解决三个关键子问题：哪些工具应在何时变得可见，以及在何种成本或风险约束下进行权衡。为此，论文提出了ToolMenuBench基准，引入因果最小工具过滤（CMTF）等方法，旨在通过因果导向的菜单设计，在提升任务成功率的同时，显著减少错误工具调用、过早行动、令牌消耗和风险工具暴露，从而将工具菜单设计作为评估代理性能的一等目标。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**工具使用与评测类**、**工具检索与过滤类**、**系统可靠性类**。工具使用方面，ReAct、Toolformer、ToolLLM、ToolBench和API-Bank等工作奠定了模型调用API的核心能力，但通常假设工具集已固定或精心挑选；ToolMenuBench则聚焦于“工具菜单”本身的构建策略。函数调用评测（如伯克利函数调用排行榜）衡量模型的选择与参数构造能力，但忽略了工具菜单大小、干扰项和风险暴露对行为的显著影响。在工具检索与过滤方面，基于词汇匹配、嵌入相似度或学习模型的方法（如ToolScope）主要解决相关性与冗余问题；ToolMenuBench在此基础上引入了状态感知过滤（仅暴露前提满足的工具）和因果最小化过滤（仅暴露因果上必要的下一步工具），并指出语义相关不等于必要或安全。系统可靠性方面，自愈型编排器关注运行时错误恢复，而本文聚焦于动作可见性这一前置界面层，显式建模了多种现实干扰项（如近重复API、高风险操作），并同时评测过滤级和下游代理级指标（如成功率和令牌消耗）。ToolMenuBench将工具菜单构建作为第一类系统问题，填补了现有评测缺少对菜单构造策略进行统一、可复用评估的空白。

### Q3: 论文如何解决这个问题？

这篇论文通过提出 ToolMenuBench 基准，系统性地评估了在多步骤LLM代理中构建工具菜单的不同策略。其核心方法是将工具可见性、模型选择和任务完成这三个通常混淆的问题分离开来，并设计了包含控制工具注册表、多步骤任务、黄金轨迹和干扰标注的评估框架。

整体框架上，每个基准实例包括用户任务、初始状态、目标状态、工具注册表和过滤方法。在每个决策步骤，过滤方法根据任务、当前状态、目标和注册表生成一个可见工具子集。代理基于当前任务和这个子菜单选择并执行工具，环境更新状态，直至达到目标或步骤耗尽。主要组件包括：1) **工具注册表**，包含任务相关工具和各类干扰项，如语义干扰、近重复、模式兼容错误工具、过早工具、风险工具和跨域工具。2) **黄金轨迹**，定义每个步骤应有的“黄金下一个工具”，用于过滤级别评估，以及预期的状态转换，用于下游评估。3) **多种过滤策略**，包括全工具暴露、关键词匹配、状态感知过滤、完整因果路径暴露，以及论文提出的关键创新方法——**因果最小工具过滤（CMTF）**。

关键技术在于CMTF利用工具的前置条件和效果契约，仅暴露当前状态和目标所需的最小因果相关工具集。实验表明，CMTF在多种模型和设置下表现出最强的综合权衡，将任务成功率从全工具暴露的32.1%提升至85.7%，同时平均Token使用量减少约98%，并显著降低了错误工具调用、过早操作和风险工具暴露。

### Q4: 论文做了哪些实验？

论文在ToolMenuBench上进行了大规模实验，共执行26,460次端到端智能体执行。实验设置包括7个模型后端（Nova 2 Lite、Nova Premier、Nova 2 Pro、Claude Haiku 4.5、Claude Sonnet 4.6、Claude Opus 4.8、GPT-OSS-120B）、3种工具菜单规模（25、100、250个工具）、6种过滤方法（全部工具、关键词Top-5、关键词Top-10、状态感知、完整因果路径、CMTF）以及7种评估设置（1个混合干扰基准和6个针对性干扰压力测试：语义、近重复、模式兼容、过早、风险、跨领域）。主要基准测试中，全部工具暴露仅达到32.1%的成功率，平均每次任务消耗56,062个token；而CMTF方法达到85.7%的成功率，平均仅暴露0.99个工具并消耗1,125个token，成功率绝对提升53.6个百分点，token使用减少约98%。在六项针对性干扰测试中，CMTF均被评为最佳方法，成功率在84.4%至90.6%之间，平均token使用约1,100。模型级结果显示Claude Haiku 4.5、Claude Opus 4.8和Nova 2 Lite达到100%成功率。所有实验采用确定性模拟工具环境，排除外部API不确定性。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其实验环境过于理想化：采用固定的符号状态表示和完整的合约元数据（前置条件/效果），这在实际生产系统中往往难以获得，存在状态提取噪声、合约不完整或API延迟、认证失败等现实问题。未来可探索的方向包括：1) **鲁棒合约获取**：研究如何从不完美的工具文档或少量示例中自动学习、推断工具的前置条件和效果，或者开发能够容忍合约噪声的因果过滤变体；2) **部分可观测性下的过滤**：当代理无法确切知道系统状态时，需要研究基于信念状态或概率推理的菜单构造策略；3) **安全与成本的动态权衡**：论文揭示“最小暴露”原则能减少风险，但未来可扩展研究在风险敏感场景（如财务、医疗）中，如何动态调整过滤的严格程度，而非仅追求最小化；4) **扩展到异构环境**：将过滤框架应用于代码执行、机器人控制或长周期企业工作流，验证其在不同任务结构下的泛化能力。

### Q6: 总结一下论文的主要内容

ToolMenuBench提出了一个评估LLM代理工具菜单构建的基准。该基准定义的问题是多步骤代理在大型工具库中，可见工具菜单如何影响可靠性、效率和风险暴露。方法上，它引入了一个受控的工具注册表、多步骤任务、金轨迹和前提效果契约，并定义了包括语义、近重复、架构兼容、过早、高风险和跨领域干扰在内的干扰类别。评估采用过滤级（可见工具暴露）和下游代理级（任务成功率、错误工具调用、过早行动、令牌使用和风险暴露）指标。主要结论是，因果最小工具过滤（CMTF）在七个模型后端的混合干扰测试中，将任务成功率从全工具暴露的32.1%提升至85.7%，并将平均令牌使用量减少约98%。该研究强调，工具菜单的设计需基于因果必要性而非语义相关性，以实现可靠、高效且安全的代理行为。
