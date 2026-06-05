---
title: "ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents"
authors:
  - "Rahul Suresh Babu"
  - "Laxmipriya Ganesh Iyer"
date: "2026-06-04"
arxiv_id: "2606.06284"
arxiv_url: "https://arxiv.org/abs/2606.06284"
pdf_url: "https://arxiv.org/pdf/2606.06284v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "工具使用"
  - "工具选择"
  - "因果过滤"
  - "多步任务"
  - "推理效率"
  - "训练无关方法"
relevance_score: 9.0
---

# ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents

## 原始摘要

Large language model agents increasingly rely on external tools, but larger tool menus can reduce reliability and efficiency by increasing wrong-tool calls, premature actions, and token cost. Existing tool-selection methods often optimize semantic relevance, exposing tools whose names or descriptions match the user request. We argue that relevance is insufficient: a tool may be related to the task while still being unnecessary or premature at the current step.
  We propose Causal Minimal Tool Filtering (CMTF), a training-free method that selects tools by causal sufficiency. CMTF uses lightweight precondition-effect contracts to expose only the minimal next-step tool frontier needed to advance from the current state toward the user goal. Across multi-step tool-use tasks, we compare CMTF with all-tools exposure, keyword retrieval, state-aware filtering, and causal-path ablations, measuring task success, wrong-tool calls, premature actions, tool exposure, and token cost. In the main benchmark with 102 tasks, 100 tools, four LLM backends, and 2448 task-method-model runs, CMTF matches the strongest causal baseline in aggregate success while reducing visible tools from 100 to one per step and reducing token usage by about 90% relative to all-tools exposure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在多步工具使用任务中，由于暴露过多语义相关但非必要的工具而导致的可靠性和效率下降问题。研究背景是，现代LLM智能体越来越多地依赖外部工具来扩展功能，但工具菜单的扩大增加了错误工具调用、过早行动和令牌成本。现有方法（如基于关键词或嵌入的检索、状态感知过滤）主要优化工具的语义相关性，即暴露名称或描述与用户请求匹配的工具。然而，论文指出语义相关性不足以确保可靠的多步工具使用：一个工具可能与任务相关，但在当前步骤中仍然是不必要的、过早的或具有干扰性。例如，在“查找邮件并起草回复”任务中，搜索邮件、阅读邮件、创建草稿、发送邮件和归档邮件等工具都语义相关，但只有在获得邮件标识符后，搜索工具才是因果有用的，过早暴露后期或高风险工具会导致错误调用、更长轨迹和更高令牌成本。本文将此失败模式称为“工具选择混淆”（ToolChoiceConfusion），并提出因果最小工具过滤（CMTF）方法，其核心问题是：如何基于因果充分性而非语义相关性，仅暴露当前步骤中推动任务向目标前进所需的最小因果工具集，从而提升智能体的可靠性和效率。

### Q2: 有哪些相关研究？

相关研究可分为三类：**评测类**包括API-Bank、Berkeley Function-Calling Leaderboard和AgentBench，它们评估LLM的API选择、参数构造等多步工具使用能力，但均假设工具接口已预先定义，而本文聚焦于上游的工具暴露问题——即每个决策步骤前应展示哪些工具，不同于这些评测对既定工具集的测试。**系统方法类**中，ReAct提出推理与行动交替执行，Toolformer展示模型可学习调用外部API，ToolLLM/ToolBench将工具使用评估扩展至大规模API生态系统，但这些工作未解决工具库增长带来的选择困难。Babu和Agrawal的自愈编排器在执行后监测并恢复工具错误，而本文的CMTF在执行前通过控制可见工具集降低错误概率，具有互补性。**工具筛选方法类**中，现有检索增强方法如工具向量检索、短名单大小权衡等，均将筛选视为语义相关性问题，暴露名称或描述匹配用户请求的工具。CMTF则基于因果充分性，利用轻量级前提条件-效果契约暴露当前步骤中因果必要的最小工具前沿，而不仅是语义相关工具。此外，CMTF受经典规划中STRIPS的前提条件-效果抽象启发，但不同于完整符号规划器，它仅用于过滤工具菜单而非替代LLM。与三种常见基线（基于相关性检索、状态感知暴露、全因果路径暴露）相比，CMTF避免了不必要、不可执行或过早展示问题。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为因果最小工具过滤（CMTF）的训练无关方法，用于提升多步LLM代理工具选择的可靠性。核心思想是通过因果充分性而非语义相关性来选择工具。整体框架包括：首先为每个工具定义轻量级前置条件-效果合约（precondition-effect contracts），即工具需要哪些状态变量（R_i）以及产生哪些新变量（E_i）。然后构建一个前置条件-效果依赖图，表征从当前状态（s_t）到目标状态（g）的因果路径。在每一步，CMTF使用广度优先搜索算法寻找一条最短的因果工具序列（最小路径），使得该序列的累积效果能够达到目标。最后，仅暴露当前步骤所需的最小工具前沿（frontier），即最小路径中的第一个可执行工具。主要模块包括：依赖图构建模块、最小因果路径搜索模块和工具前沿暴露模块。创新点在于：1）提出了基于因果充分性的工具选择标准，避免了语义相关但非必要工具的干扰；2）实现每步仅暴露单个工具，大幅减少工具菜单（从100个降至1个），降低token消耗约90%；3）通过消除过早动作（premature actions）和错误工具调用（wrong-tool calls）提升成功率，在102个任务、100个工具和4种LLM后端的实验验证中，其成功率与最强因果基线相当。

### Q4: 论文做了哪些实验？

论文在一个包含102个任务、100个工具的主基准上进行了实验，涉及四个LLM后端（Amazon Nova 2 Lite/Pro Preview、Claude 3.5 Haiku/Sonnet 4）和六种过滤策略，共2448次任务-方法-模型运行。实验设置采用模拟执行环境，每步向模型提供当前状态和过滤后的工具，模型需选择一个工具并给出参数，目标状态达到或超步限（最多6步）则停止。对比方法包括：全部工具、关键词top-5/top-10（基于语义相关性）、状态感知过滤（暴露可执行工具）、全因果路径（暴露因果路径上所有工具），以及提出的CMTF（仅暴露下一因果前沿工具）。核心指标：任务成功率、错误工具调用数、过早动作数、每步可见工具数、token消耗。主要结果：CMTF与最强基线（全因果路径）在聚合成功率上持平（均为0.99），但仅暴露1个工具/步，错误工具调用从全部工具的1.25降至0.01，过早动作降为0，token使用从24,569降至2,405（降低约90%）。关键词和状态感知方法成功率较低（分别为0.61/0.65），表明语义相关性或可执行性不足以确保可靠工具选择。CMTF在所有模型上表现一致，尤其削弱模型（如Claude 3.5 Haiku）成功率从0.48提升至0.94。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要有以下几点：首先，当前benchmark为合成任务，未能充分模拟真实工具生态中的不确定性，如工具故障、延迟、认证问题和模糊观测。未来可以将CMTF扩展到真实API和生产环境中，评估其在噪声状态下的鲁棒性。其次，CMTF假设工具契约（前置条件、效果、风险）是准确可用的，现实中契约可能不完整或错误，导致过度过滤或错误暴露。因此，一个关键研究方向是开发契约自动生成、验证和版本管理机制，例如从API文档或执行轨迹中推断契约。第三，当前方法严格依赖准确的状态追踪和目标映射，适用于搜索-读取-更新等有明确状态转换的任务，但对于开放、创造性或多目标任务，需要更灵活的目标表示和不确定性感知的扩展策略。例如，可以引入“恢复集”机制：默认暴露最小因果前沿，当状态不确定或执行失败时，动态添加后备或诊断工具，从而实现可控的扩展与容错。此外，将CMTF与成本-延迟权衡结合，用于指导小模型或资源受限场景下的工具选择，也是重要的实用方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为“工具选择混淆”的问题，即在多步骤智能体任务中，即使工具在语义上与用户请求相关，但在当前步骤不必要或过早暴露，会导致智能体性能下降（如错误调用工具、过早执行操作和增加token消耗）。为解决这一问题，论文提出了一种无需训练的因果最小工具过滤方法（CMTF）。该方法利用轻量级的前置条件-效果合约，为每个工具定义其依赖关系，通过构建从当前状态到目标状态的依赖图，动态地仅在每一步暴露最少数量的、因果上直接推进任务的“前沿工具”。在包含102个任务、100个工具和多种大模型后端的基准测试中，CMTF方法在保持与最强基线相当的任务成功率的同时，将每步可见工具数量从100个降至1个，并将token消耗减少了约90%。这项工作证明了因果充分性而非单纯语义相关性，是实现可靠工具增强型智能体的关键，展示了动态、状态感知的工具选择方法对提升LLM Agent可靠性与效率的核心意义。
