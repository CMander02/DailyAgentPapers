---
title: "MemToolAgent overview with a simple restaurant booking scenario where the agent retrieves similar memories, receives feedback on an invalid time format, and generates a reflection to update its memory"
authors:
  - "Suleyman Armagan Er"
  - "Danilo Ribeiro"
  - "Yogesh Virkar"
  - "Surafel Lakew"
  - "Adi Kalyanpur"
  - "James Gung"
  - "Thomas Delteil"
  - "Arshit Gupta"
date: "2026-06-06"
arxiv_id: "2606.07909"
arxiv_url: "https://arxiv.org/abs/2606.07909"
pdf_url: "https://arxiv.org/pdf/2606.07909v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "工具使用"
  - "记忆机制"
  - "反思机制"
relevance_score: 7.5
---

# MemToolAgent overview with a simple restaurant booking scenario where the agent retrieves similar memories, receives feedback on an invalid time format, and generates a reflection to update its memory

## 原始摘要

Modern large language model (LLM) agents can use external tools to help users solve complex tasks. However, for problems that require learning from long-term historical events or from previous agent-environment interactions, LLM agents are required to use memory mechanisms to store and retrieve experiences. While sophisticated memory systems exist for dialogue agents, few studies have empirically examined how to improve agents' tool-using capabilities through past user-agent conversations. We propose MemToolAgent, a framework that improves tool use through memory management. Our approach contains a memory extraction module that processes past experiences into structured memory entries, and a retrieval module that dynamically selects a subset of the stored memory entries. This enables more personalized and accurate responses aligned with user preferences and feedback without requiring LLM fine-tuning. In summary, this work has three main contributions: (1) a unified memory entry format that improves both general-purpose and personalized tool use without LLM fine-tuning, (2) a reflection-based memory extraction that uses environment and user feedback to distill wrong executions into critiques to store, and (3) a retrieval module that chooses how many past experiences to use based on the memory similarity distribution. MemToolAgent achieves 29%, 80%, and 17% relative improvements compared to strong baselines on the WorkBench, NESTFUL, and PEToolBench benchmarks, respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文研究的是如何提升大型语言模型（LLM）智能体在使用外部工具时的能力。现有方法中，虽然有些对话智能体配备了复杂的记忆系统，但很少有研究系统性地探索如何利用过往的“用户-智能体交互历史”来改进工具使用能力。LLM的固定上下文窗口限制了其在长对话中保持连贯性，且注意力机制在长序列中易被大量无关信息干扰，导致效果下降。因此，智能体需要可靠的外部反馈（如记忆）来自我纠正，但简单将原始历史轨迹作为记忆提供给智能体，会让它在学习失败经验的同时处理当前任务，增加了认知负担。

本文的核心问题是：**如何设计一种有效的记忆机制，使LLM智能体能够从过去的交互历史（包括成功的经验和失败的教训）中学习，从而提升其通用工具使用能力和个性化工具选择能力，且无需对LLM进行微调。**

具体而言，论文提出了MemToolAgent框架，通过三个创新点解决上述问题：1）设计统一的记忆条目格式，将经验结构化存储；2）提出基于反思的记忆提取模块，把失败的执行轨迹提炼为明确的批评（critique），而非直接存储原始轨迹；3）开发动态Top-n检索模块，根据查询与记忆条目的相似度分布动态决定检索数量，代替固定数量的检索，从而更精准地提供上下文。实验表明，该方法在WorkBench、NESTFUL和PEToolBench三个基准测试上，相较于强基线分别取得了29%、80%和17%的相对性能提升。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：

**方法类：** MemGPT提出OS启发的记忆层级；Mem0和A-MEM使用知识图谱或Zettelkasten组织记忆；Reflexion通过自我反思存储经验；RMM利用强化学习排序记忆条目；LEGOMem仅沉淀成功轨迹；ReMem在任务中主动重组记忆。不同于这些方法，MemToolAgent设计了统一记忆格式，同时处理个性化与通用工具使用，并明确利用用户反馈改进记忆条目。

**记忆增强工具使用类：** TOOLMEM存储工具能力记忆辅助选择；EXPEREPAIR针对代码修复；T1缓存工具调用结果；$Mem^p$从轨迹提取指令；Agent Workflow Memory存储工作流引导导航。本文区别于上述方法，其记忆条目同时包含工具轨迹、执行反思和用户反馈，且检索模块基于相似度分布动态调整记忆数量。

**上下文学习方法：** ICAL和STE通过离线轨迹创建静态记忆。与这些方法不同，MemToolAgent采纳动态记忆更新和在线反馈整合，无需微调即可适应不同用户偏好。

总体而言，本文的核心贡献在于提出一个统一框架，能同时优化通用与个性化工具使用，并通过反思提取和检索动态选择机制显著提升性能（在三个基准上相对提升17%-80%）。

### Q3: 论文如何解决这个问题？

MemToolAgent通过两个核心模块解决工具使用中的长期记忆学习问题:1) 记忆提取模块负责将历史交互经验转化为结构化记忆条目,每条记忆以(q,a,f,r)四元组存储,其中q为用户查询,a为工具调用序列,f为二进制用户反馈(成功=1/失败=0),r为失败时生成的反思/批评文本。当反馈为失败时,该模块调用LLM基于当前查询、可用工具集、环境反馈和语义相似的历史记忆生成结构化反思,将复杂错误轨迹蒸馏为清晰批评,避免原始执行轨迹的冗余信息干扰。2) 动态Top-n检索模块通过计算查询与记忆的余弦相似度,使用滑动窗口一阶导数估计检测相似度曲线的"膝关节"(峰值),自动确定最优检索数量n,避免固定k值导致的冗余或信息缺失。核心创新包括:统一记忆格式支持通用与个性化工具调用,无需微调LLM;基于环境与用户反馈的反思式记忆提取,将错误执行转化为批评存储;基于相似度分布动态调整检索数量的算法,通过峰值检测鲁棒地识别聚类边界。在WorkBench、NESTFUL和PEToolBench上分别取得29%、80%和17%的相对性能提升。

### Q4: 论文做了哪些实验？

论文在通用工具使用和个性化两个任务上进行了实验。使用三个基准测试：WorkBench（通用工具使用，含5个领域共549个测试查询，评估准确率）、NESTFUL（嵌套工具调用，基于MathQA和StarCoder2-Instruct，500个测试查询，评估F1分数、序列匹配和胜率）和PEToolBench（个性化工具编排，591个测试查询，评估工具和参数准确率）。对比方法包括无记忆基线、扩展思考、ReAct、以及记忆架构A-MEM和Mem0。主要结果：在WorkBench上，MemToolAgent整体准确率达85.06%，相比无记忆基线的57.56%显著提升，其中Analytics任务从18.52%提升至86.11%。在NESTFUL上，全序列匹配准确率从15.6%提升至30.4%，胜率从51.2%提升至70.2%。在PEToolBench上，工具准确率达0.82，相比A-MEM和Mem0的0.70提升17%。消融实验验证了动态记忆检索（动态n优于固定top-k）和记忆提取模块（显著提升各基准性能）的有效性。代价分析显示，虽然输入token增加，但输出token仅14585，远低于ReAct（22923）和扩展思考（40765）。

### Q5: 有什么可以进一步探索的点？

首先，论文指出的冷启动问题值得深入探索。尽管实验表明简单方法可缓解，但现实场景中工具数量远超40个，记忆系统难以覆盖所有工具用法。未来可研究基于知识图谱或元学习的预填充策略，利用工具文档和API规范自动生成初始记忆条目。其次，当前单轮对话的检索模式在多轮交互中失效，一个重要改进是设计动态逐步检索机制，在每个用户轮次后根据当前子任务重新检索相关记忆，而非仅初始检索一次。最后，现有记忆结构可能过于刚性，未能充分利用工具间关系。可引入层级记忆结构，将工具类别、常见错误模式与个性化偏好分层存储，实现更细粒度的检索与泛化。同时，可探索记忆遗忘机制，防止无关经验干扰决策，并研究跨任务迁移策略，使从简单工具学到的经验能辅助复杂工具使用。

### Q6: 总结一下论文的主要内容

现代大语言模型代理在解决复杂任务时需要借助外部工具，但长程历史交互中的上下文限制阻碍了其持续学习和适应能力。针对这一问题，论文提出MemToolAgent框架，通过结构化记忆管理提升代理的工具使用能力。该框架包含两个核心模块：记忆提取模块将用户反馈和环境反馈转化为包含反思的标准化记忆条目，尤其针对执行错误生成批判性记录；检索模块基于记忆相似度动态分布自适应选择相关历史经验。在个人化任务（如根据用户偏好选择不同API参数）和通用任务（如避免参数幻觉、依赖违规等常见错误）两类场景中均有效。在WorkBench、NESTFUL和PEToolBench基准上，相比强基线方法分别取得29%、80%和17%的相对提升，验证了无需微调即可通过记忆机制显著增强代理的个性化响应准确性和错误规避能力。
