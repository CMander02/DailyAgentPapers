---
title: "DecoSearch: Complexity-Aware Routing and Plan-Level Repair for Text-to-SQL"
authors:
  - "Esteban Schafir"
  - "Xu Zheng"
  - "Hojat Allah Salehi"
  - "Zhuomin Chen"
  - "Mo Sha"
  - "Wei Cheng"
  - "Dongsheng Luo"
date: "2026-06-16"
arxiv_id: "2606.17821"
arxiv_url: "https://arxiv.org/abs/2606.17821"
pdf_url: "https://arxiv.org/pdf/2606.17821v1"
categories:
  - "cs.AI"
tags:
  - "Text-to-SQL"
  - "LLM Agent"
  - "Training-Free"
  - "Complexity-Aware Routing"
  - "Plan-Level Repair"
  - "Schema Selection"
  - "RAG"
  - "DAG Decomposition"
relevance_score: 8.5
---

# DecoSearch: Complexity-Aware Routing and Plan-Level Repair for Text-to-SQL

## 原始摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities in translating natural language to SQL, yet existing methods still falter on complex queries requiring multi-step, data-aware reasoning. We introduce DecoSearch, a training-free framework that addresses this by routing each query to the appropriate level of reasoning effort. A lightweight Schema Selector first prunes the full database schema to the relevant tables and columns. An LLM Judger then decides whether the question requires decomposition: straightforward questions follow a direct generation path and complex ones are escalated to a Directed Acyclic Graph (DAG) of atomic sub-questions, each solved by a targeted SQL generation step. A RAG component grounds the decomposer with semantically similar training examples, and a Topology Refiner restructures the reasoning plan when execution failures signal a flawed decomposition rather than a fixable SQL error. DecoSearch achieves 70.53% execution accuracy on BIRD and 88.31% on Spider with a DeepSeek backbone, surpassing all training-free baselines while consuming an order of magnitude fewer tokens than competing methods. It also functions as a model-agnostic wrapper, consistently improving fine-tuned SQL generation backbones without any modification to the pipeline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂 Text-to-SQL 任务中，现有方法无法系统性处理由不同抽象层级失败（如实现错误、策略错误、规划错误）导致性能下降的问题。研究背景指出，大语言模型在简单查询上表现优异，但在需要多步逻辑推理、数据感知、复杂 JOIN 操作或大数据库场景下，单次自回归生成常常失败。现有方法虽各有应对，如分解机制简化问题、自我调试修复语法错误、多候选生成扩大搜索空间、复杂度感知路由分配计算资源，但它们都仅处理单一失败模式（例如自调试无法识别推理计划缺陷，分解系统无法修正错误子问题，多候选方法不能自适应聚焦计算）。作者通过观察发现，复杂查询的失败根源是异质的：有些是 SQL级别的 bug（如错误连接条件），可通过执行反馈直接修复；有些是策略层面的不适配（如错误选择了嵌套子查询而非 CTE）；而有些则是规划层面的根本性错误（如缺失依赖或分解过粗），此时任何 SQL 级修复都无济于事。核心问题是：没有一个现有框架能系统诊断失败发生的层级并路由到相应的修复机制。因此，本文引入 DecoSearch，这是一个无需训练的框架，通过层级失败路由架构，让“审判器”决定查询走直接路径还是分解为有向无环图，并首创“规划级修复”机制，在持久执行失败时自动重构推理计划，从而适当地分配计算资源到真正需要其的深层失败。

### Q2: 有哪些相关研究？

在文本到SQL领域，相关研究主要分为以下几类：**方法类**方面，早期工作依赖语义解析和模式感知神经编码器，而大规模LLM的兴起转向基于上下文学习。本文的Decomposition-based方法如DIN-SQL和DEA-SQL开创了分解式上下文学习与工作流范式，本文通过形式化为依赖DAG并引入计划级修复拓展了这些思路。**Schema Linking类**包括CHESS和RSL-SQL，采用LLM驱动的模式剪枝实现高效召回，本文的Schema Selector遵循类似范式。**Self-Refinement类**如ExCoT利用执行反馈迭代修正SQL，但仅处理实现级错误，本文则通过计划级操作在分解失败时重写DAG而非修补单个查询。**Multi-Candidate与Routing类**包括CHASE-SQL、Agentar-Scale-SQL等生成多候选方案，EllieSQL和Rethinking Agentic Workflows探索复杂度感知路由，本文采用Judger引导路由，在直接生成与分层分解间抉择，以DAG方法处理复杂查询。与这些工作相比，DecoSearch的关键区别在于：它是首个同时结合复杂度感知路由与计划级修复的训练无关框架，且能作为模型无关包装器提升微调模型性能。

### Q3: 论文如何解决这个问题？

DecoSearch通过一个复杂度感知的路由与计划级修复框架解决文本到SQL生成中的复杂查询问题。核心方法包括以下组件:首先，**Schema Selector**采用两阶段剪枝策略，先通过LLM提取任务相关关键词和实体，再基于这些关键词选择相关表和列，将大型数据库的提示长度缩减一个数量级。随后，**LLM Judger**评估问题复杂度，输出二元路由决策（是否需要分解），默认优先走直接路径，仅在涉及聚合粒度冲突、极端连接复杂度、多阶段推理或公式驱动查询时才触发分解。

对于直接路径，系统尝试单次SQL生成并执行，成功则返回结果；失败则回退到分解阶段。在复杂查询时，系统构建**有向无环图（DAG）**，将问题分解为原子子问题，节点间通过@[n]占位符传递数据依赖（小结果集内联为IN列表，大结果集物化为临时表）。**RAG组件**检索成功训练示例作为少样本提示，提升分解质量。关键创新在于**层级控制循环**：当某节点SQL执行失败时，**Topology Refiner**不重试同子问题，而是根据错误重构DAG拓扑（重新划分依赖、插入中间节点、调整数据流），最多尝试B次后优雅降级。整个框架无需训练，仅依赖预训练LLM的推理能力，在BIRD和Spider上分别达到70.53%和88.31%的执行准确率，且token消耗比竞争方法低一个数量级。

### Q4: 论文做了哪些实验？

论文在BIRD和Spider两个标准Text-to-SQL基准上进行了实验。BIRD有1534条开发查询，强调数据感知推理；Spider有2147条测试查询，侧重SQL结构复杂度。实验设置包括训练无关基线（如CHESS、GenaSQL、DAIL-SQL、DIN-SQL）和微调基线（如XiYan-SQL、OmniSQL）。主要评估指标是执行准确率（Execution Accuracy）。

主要结果：DecoSearch在BIRD上达到70.53%准确率，在Spider上达到88.31%，均超越所有训练无关方法。在Token效率方面，DecoSearch在BIRD上仅消耗约200万token即达到峰值准确率，而CHESS需约2000万token（10倍开销）。作为模型无关包装器，DecoSearch显著提升了微调模型表现：在BIRD上，XiYanSQL-7B提升10.67个百分点，GPT-5-mini提升5.61个百分点，OmniSQL-7B提升3.52个百分点。消融实验显示，Judger组件最为关键（移除导致准确率下降10.65个百分点），Schema Selector次之（下降1.82个百分点但token开销膨胀6.3倍）。

### Q5: 有什么可以进一步探索的点？

DecoSearch的核心局限在于对可执行反馈的强依赖。当SQL无法执行（如权限受限、环境缺失）或执行返回“语法正确但语义错误”的结果时，拓扑重构和路由决策将失效。未来可探索**无执行信号的推理路径**，例如：(1) 利用LLM自身的语义一致性校验作为替代反馈，通过对比子问题意图与生成SQL的逻辑结构来发现计划级错误；(2) 引入**概率化路由机制**，基于查询复杂度（如表列数或JOIN深度）而非执行结果来动态调整分解粒度，降低对事后反馈的依赖；(3) 构建轻量级的**离线DAG质量评估器**，在任务开始前预测分解计划的可靠性，从而避免代价高昂的在线执行成本。此外，当前方法将RAG限制于语义相似样例，若将历史失败模式（如特定JOIN路径容易出错）融入检索，可进一步提升分解鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文介绍了DecoSearch，一个无需训练的文转SQL框架，通过复杂度感知的路由和计划级修复来解决复杂查询问题。针对现有LLM在多步数据感知推理上的不足，DecoSearch首先使用轻量级Schema Selector剪枝数据库模式，再由LLM Judger判断问题难度：简单问题直接生成SQL，复杂问题则分解为有向无环图的原子子问题并逐一求解。方法还引入RAG组件增强分解，并利用执行失败信号启动拓扑修改器修复有缺陷的推理计划。在BIRD和Spider数据集上，DecoSearch以DeepSeek为骨干分别达到70.53%和88.31%的执行准确率，超越所有无训练基线，同时相比CHESS等方法消耗的token数量小一个数量级。消融实验证明Judger路由是最大贡献者（-10.65pp）。DecoSearch的核心贡献是提出了一种高效、即插即用的路由与修复机制，可作为模型无关的包装器提升微调模型性能，无需修改现有流水线。
