---
title: "AutomationBench"
authors:
  - "Daniel Shepard"
  - "Robin Salimans"
date: "2026-04-21"
arxiv_id: "2604.18934"
arxiv_url: "https://arxiv.org/abs/2604.18934"
pdf_url: "https://arxiv.org/pdf/2604.18934v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Workflow Automation"
  - "API Tool Use"
  - "Cross-Application Coordination"
  - "Policy Adherence"
  - "Autonomous Discovery"
  - "REST API"
  - "Evaluation"
relevance_score: 8.5
---

# AutomationBench

## 原始摘要

Existing AI benchmarks for software automation rarely combine cross-application coordination, autonomous API discovery, and policy adherence. Real business workflows demand all three: a single task may span a CRM, inbox, calendar, and messaging platform - requiring the agent to find the right endpoints, follow a policy document, and write correct data to each system. To address this gap, we introduce AutomationBench, a benchmark for evaluating AI agents on cross-application workflow orchestration via REST APIs. Drawing on real workflow patterns from Zapier's platform, tasks span Sales, Marketing, Operations, Support, Finance, and HR domains. Agents must discover relevant endpoints themselves, follow layered business rules, and navigate environments with irrelevant and sometimes misleading records. Grading is programmatic and end-state only: whether the correct data ended up in the right systems. Even the best frontier models currently score below 10%. AutomationBench provides a challenging, realistic measure of where current models stand relative to the agentic capabilities businesses actually need.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有AI智能体在自动化真实商业工作流时面临的评估标准缺失问题。研究背景是，现代企业依赖大量相互关联的Web应用（如CRM、邮箱、日历等），协调这些应用间的操作是知识工作中最耗时的部分之一，而AI智能体被寄予自动化这些工作流的厚望。然而，现有基准测试存在明显不足：它们要么专注于单应用内的长周期网页任务（如WebArena、Mind2Web），要么评估开放式的计算机使用任务（如OSWorld），要么在受限环境中评估工具/API使用（如ToolBench、API-Bank），普遍缺乏对跨应用协调、自主API发现和策略遵从这三项关键能力的综合考察。一些基准（如AppWorld）虽涉及跨应用，但未要求自主发现API；另一些（如τ³-bench）虽包含策略规则和部分文档化工具发现，但任务仍局限于单一应用内部。

因此，本文要解决的核心问题是：如何建立一个能真实、全面评估AI智能体在跨应用工作流编排方面能力的基准。具体而言，该基准需模拟真实的商业场景，要求智能体根据自然语言描述的业务任务，自主发现数十个集成应用中的相关REST API端点，进行顺序且相互依赖的API调用，遵循分层的业务规则，并在包含干扰项、诱饵记录和对抗性输入的环境中导航，最终仅根据“正确数据是否写入正确系统”这一最终状态进行程序化评分。AutomationBench的引入正是为了填补这一空白，旨在准确衡量当前模型与商业实际所需的智能体能力之间的差距，并推动相关研究发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：软件自动化评测基准、API驱动的智能体研究，以及工作流协调任务。

在**软件自动化评测基准**方面，现有工作如WebArena、AgentBench和OSWorld等，主要聚焦于单一应用内的操作（如网页或桌面环境），或依赖预先定义的API列表。AutomationBench则强调跨多个商业应用（如CRM、日历、消息平台）的协调，并要求智能体自主发现REST API端点，这更贴近真实业务场景中需集成不同系统的需求。

在**API驱动的智能体研究**方面，相关工作探索了利用API工具完成具体任务，但通常假设API文档已知或环境简单。本文的基准特别引入了环境中存在无关甚至误导性记录、以及需要遵循分层业务规则（政策文档）的复杂性，对智能体的理解、规划和抗干扰能力提出了更高要求。

在**工作流协调任务**方面，研究多集中于流程建模或特定领域自动化。本文的创新在于直接从真实平台（Zapier）提取跨领域（销售、市场、运营等）的工作流模式，并以严格的“仅终态”程序化评分（检查数据是否最终正确写入各系统）来评估，旨在衡量当前模型与商业实际所需智能体能力之间的差距。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AutomationBench的基准测试平台来解决现有AI代理在跨应用工作流编排能力评估上的不足。其核心方法是模拟真实商业环境中跨多个应用（如CRM、邮箱、日历、消息平台）的自动化任务，要求代理自主发现API端点、遵循分层业务规则，并在包含无关或误导性记录的环境中导航。

整体框架基于一个包含600多个公开任务和600多个私有评估任务的合成数据集，涵盖销售、营销、运营、支持、财务和人力资源六大领域。数据集构建利用了Zapier平台的真实工作流模式，通过大模型生成并经过多轮迭代以确保真实性和难度。关键技术包括：1）**程序化验证**：仅通过最终状态（即正确数据是否写入正确系统）进行客观评分，不依赖主观判断；2）**任务强化技术**：通过添加无关数据、将关键信息隐藏在工具调用响应后、使用相似命名制造歧义、设置严格的业务策略规则等手段增加任务复杂性；3）**策略遵循设计**：明确要求代理参考策略文档，避免与提示注入混淆；4）**结构化决策记录**：代理需将主观判断（如分配优先级）转化为系统状态变更（如更新状态字段），以便验证。

主要模块包括：1）**工具接口**：提供Search和Execute两种工具。Search工具允许代理通过关键词搜索（BM25算法）跨所有可用API模式（返回top-5结果）自主发现相关端点；Execute工具模拟HTTP请求执行操作，无需处理身份验证。2）**状态模拟**：通过Pydantic模型模拟应用数据库状态，保留真实API模式的结构（如分页、必填字段、4xx错误码）。3）**任务执行环境**：设定最大50步的限制（目前极少触及），支持每步并行调用多个工具。

创新点在于首次将跨应用协调、自主API发现和策略遵循三者结合在一个基准测试中，并通过仅关注最终状态的程序化评估、使用真实工作流模式合成任务、以及应用多种强化技术来确保基准的挑战性和现实性，从而准确衡量当前模型与商业实际所需代理能力之间的差距。

### Q4: 论文做了哪些实验？

论文在AutomationBench基准上进行了系统实验，评估了多个前沿AI模型在跨应用工作流编排任务上的表现。实验设置要求智能体通过REST API自主发现相关端点、遵循分层业务规则，并在包含无关或误导记录的环境中导航，最终仅根据“正确数据是否写入正确系统”这一最终状态进行程序化评分。

数据集基于Zapier平台的真实工作流模式构建，涵盖销售、营销、运营、支持、财务和人力资源六大领域。对比方法包括使用不同工具集的测试：默认API工具集、基于Zapier内部操作构建的Zapier工具集，以及仅包含必要工具的Limited Zapier工具集。此外，还设置了一个简单领域作为基线，以验证测试框架的有效性。

主要结果显示，所有前沿模型的得分均低于10%。具体而言：Claude Opus 4.7以9.9%的通过率领先；Gemini和Opus的通过任务集Jaccard相似度仅为0.17，表明它们解决的任务差异很大。在效率方面，Opus平均每个任务使用12.6步和29.8次工具调用，而Gemini使用21.8步和35.4次工具调用。不同工具集对性能有显著影响：例如Gemini 3.1 Pro在API、Zapier和Limited Zapier工具集下的通过率分别为9.6%、12.8%和14.3%。模型普遍存在“错误自信”问题，在失败案例中，Opus、Gemini和GPT 5.4 High分别有72%、91%和84%的比例错误宣称任务成功。常见失败模式包括数据查找不持久、列表处理不完整以及未能严格遵循指令要求。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在：1）合成数据可能缺乏真实性和存在逻辑不可能性，虽然通过人工抽样和任务硬化技术缓解，但难以完全模拟真实商业流程的复杂性和突发状况；2）任务规模庞大导致人工全面审查困难，可能存在隐藏的评估偏差；3）当前基准仅关注最终状态正确性，忽略了执行过程的合理性和效率。

未来可探索的方向包括：1）引入过程性评估指标，如步骤合理性、API调用效率、错误恢复能力等；2）构建动态环境，允许任务参数和规则在运行时变化，以测试智能体的适应能力；3）增加多模态交互场景，结合图形界面操作与API调用；4）开发增量学习机制，使智能体能够从历史任务中持续优化策略；5）建立真实企业数据脱敏后的测试集，弥补合成数据的不足。这些改进将推动智能体从“任务执行者”向“流程优化者”演进。

### Q6: 总结一下论文的主要内容

该论文针对现有AI智能体在软件自动化评估上的不足，提出了AutomationBench这一新基准。其核心问题是评估智能体在跨应用业务流程编排中的真实能力，这要求智能体能够自主发现REST API端点、遵循分层业务规则、在包含干扰和误导记录的环境中协调多个独立应用的操作。

方法上，该基准基于Zapier平台的真实工作流模式构建，覆盖销售、营销、运营等六大业务领域的47个模拟应用。智能体需根据自然语言任务描述，自主检索相关API，执行一系列相互依赖的API调用，并依据给定的政策文档进行决策。评估采用纯程序化的终态验证，即仅检查正确数据是否最终写入目标系统，模拟企业实际验收标准。

主要结论显示，即使当前最先进的模型在该基准上的得分也低于10%，这揭示了现有AI能力与商业实际所需的智能体化（agentic）能力之间存在巨大差距。AutomationBench的意义在于提供了一个兼具挑战性和现实性的衡量标准，能够引导研究朝向企业最需要的跨应用协调、自主工具发现和策略遵从等关键能力发展。
