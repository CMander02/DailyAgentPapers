---
title: "Multi-Agent Systems for Root Cause Analysis in Microservices"
authors:
  - "Alexander Naakka"
  - "Yuqing Wang"
  - "Mika V Mäntylä"
date: "2026-05-05"
arxiv_id: "2605.03505"
arxiv_url: "https://arxiv.org/abs/2605.03505"
pdf_url: "https://arxiv.org/pdf/2605.03505v1"
categories:
  - "cs.SE"
tags:
  - "LLM-based Agent"
  - "Multi-Agent System"
  - "Root Cause Analysis"
  - "Microservices"
  - "Language Agent Tree Search"
  - "Reflection-based Reasoning"
relevance_score: 7.5
---

# Multi-Agent Systems for Root Cause Analysis in Microservices

## 原始摘要

Recent advances in large language models (LLMs) have enabled early attempts to automate root cause analysis (RCA) in microservice-based systems (MSS). Yet, prior works typically rely on a linear reasoning process that proceeds along a single diagnostic path. In this paper, we propose LATS-RCA, an LLM-based multi-agent framework for RCA in MSS. LATS-RCA formulates RCA as a reflection-guided tree-structured search using a Language Agent Tree Search algorithm. In LATS-RCA, multiple LLM-driven agents iteratively perform RCA for each microservice by reasoning over its execution logs and performance metrics to collect operational evidence for root cause exploration. Reflection scores derived from intermediate diagnostic states are used to guide the search toward the most likely root cause based on accumulated evidence. We evaluate LATS-RCA on the open-source industrial MSS, Light-OAuth2 (LO2), using a publicly available dataset and in a production microservice environment (Prod) in a case company with substantially higher operational complexity. LO2 is a small-team Java system with a homogeneous technology stack. The results on LO2 show that LATS-RCA achieves high diagnostic accuracy, and we further benchmark its associated computational costs. Compared to LO2, Prod attains lower diagnostic accuracy and incurs higher computational cost. The Prod deployment demonstrates the practical applicability of LATS-RCA in real-world MSS and reflects the challenges introduced by polyglot tech stack, varied logging practices of source components, and multi-factor root-causes by production-scale MSS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决微服务系统中根因分析（RCA）高度依赖人工、效率低下且难以规模化的问题。当前，微服务架构在生产环境中广泛部署，异常频发，但RCA主要依赖工程师手动排查，这一过程耗时费力且依赖个人经验，难以应对大规模系统的复杂性。虽然已有研究尝试利用大语言模型（LLM）实现RCA自动化，如RCAgent和MicroRCA，但这些方法采用线性推理过程，即沿着单一诊断路径进行分析。然而，在实际微服务环境中，一个异常现象往往可能指向多个服务或组件，线性推理难以有效处理这种多候选根因的复杂诊断场景。针对这一不足，本文提出LATS-RCA，这是一个基于LLM的多智能体框架。其核心创新在于将RCA问题建模为反射引导的树结构搜索过程，利用语言智能体树搜索（LATS）算法，通过多个LLM驱动的智能体并行探索多条候选推理路径，并基于日志和指标逐步收集证据、计算反射分数，从而动态引导搜索聚焦于最可能的根因，旨在突破线性推理的局限，提升自动化RCA的准确性和实用性。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先指出基于LLM的多智能体系统用于微服务根因分析（RCA）的现有工作非常稀缺，仅有RCAgent和MicroRCA两项相关工作。**RCAgent**将RCA形式化为基于执行推理的任务，通过生成可执行分析程序（如Python代码）来查询、聚合和预处理多模态监控数据（日志、指标、追踪），然后对程序执行结果进行推理，输出结构化的诊断答案（如故障时间范围和故障组件）。**MicroRCA**则采用流水线导向方法，先对日志、追踪、指标进行大量模态特定的预处理（如日志解析、模板过滤、启发式异常检测），再通过精心设计的提示将处理后的信号输入LLM，使其综合跨模态证据并推断根因，输出JSON格式的结构化结果。本文提出的**LATS-RCA**与二者的区别在于：LATS-RCA放弃了线性或流水线的单路径推理，而是将根因分析构建为基于语言智能体树搜索（LATS）的反射引导树形搜索过程。它允许多个LLM驱动的智能体并行迭代地为每个微服务收集运行证据，并通过反射分数动态引导搜索路径，从而更全面地在多样化操作证据中探索最可能的根因，突破了先前方法在推理路径上的局限性。

### Q3: 论文如何解决这个问题？

论文提出LATS-RCA，一个基于LLM的多智能体框架，用于微服务系统中的根因分析。其核心方法是将根因分析建模为反射引导的树结构搜索过程，采用语言智能体树搜索算法。

框架整体由两个诊断智能体（日志智能体和指标智能体）与一个协调监督器组成。每个智能体独立处理其对应的可观测性模态：日志智能体分析日志数据，指标智能体分析性能指标并生成可视化图表。监督器负责协调跨模态的任务交接和执行顺序，并进行最终的相关性评估。

关键技术方面，每个智能体将诊断过程建模为有限时域的顺序决策过程，并通过LLM反射引导的蒙特卡洛树搜索算法进行诊断。具体操作包含四个阶段：选择阶段，使用置信上限树得分选择待扩展的节点，平衡探索与利用；扩展阶段，在选择的叶子节点采样N=5个候选动作；反射阶段，LLM反射模块从证据质量、诊断完整性和内部一致性三个维度对每个候选动作评分，并聚合为反射分数；反向传播阶段，将组合奖励沿搜索路径反向传播更新节点值。

创新点包括：通过树结构搜索实现非线性的诊断推理路径，探索多种假设；引入反射机制进行自我评估和引导；通过多智能体协作实现跨模态的交叉验证，减少单一模态局限性；采用智能体间的高效信息传递机制，避免完整树结构传递带来的计算开销和循环推理风险。

### Q4: 论文做了哪些实验？

论文在Light-OAuth2 (LO2) 开源数据集和真实生产环境（Prod）中进行了实验。LO2 数据集包含7个微服务，通过API错误注入生成53个故障案例，使用485个性能指标。对比方法包括单智能体ReAct和多智能体ReAct基线。主要结果：LATS-RCA在LO2上达到91.3%的诊断准确率，显著优于单智能体ReAct（39.8%）和多智能体ReAct（57.4%），计算成本更高（每次调查53.1次API调用、156K token、9.1分钟）。消融实验表明，候选批处理贡献最大（去除后准确率降至84.3%），其次是反向传播（84.8%）和反思机制（87.6%）。在生产环境中，LATS-RCA准确率降至60-70%，每次调查需75次API调用、220K token和13分钟，主要因生产系统的多语言技术栈、日志格式多样性和多因素根因问题。实验验证了LATS-RCA在结构化日志环境中的有效性和对复杂生产环境的适应性。

### Q5: 有什么可以进一步探索的点？

基于论文的实验结果，LATS-RCA 在真实生产环境中的诊断准确率明显低于标准化测试环境，核心瓶颈在于多语言技术栈（Node.js, Rust, Python, Go）带来的日志格式和监控指标的异构性。未来可以探索自适应日志标准化模块，利用少量样本微调LLM自动对齐不同组件的指标命名、时间戳格式和严重级别映射，降低对人工预处理的依赖。其次，当前树搜索完全依赖反射评分引导，但评分标准是否最优尚不明确，可以引入集成贝叶斯推理或多轮交叉验证机制来量化诊断置信度。另外，生产环境中的多因素根因难以被单一搜索路径捕获，未来可设计并行搜索分支，允许系统输出根因候选集而非单一答案，并利用故障注入实验构建多标签评估基准。最后，计算成本与搜索深度之间的权衡值得深入优化，例如通过剪枝策略或动态调整搜索宽度来提升效率。

### Q6: 总结一下论文的主要内容

本文提出LATS-RCA，一个基于大语言模型的多智能体框架，用于微服务系统中的根因分析。核心贡献在于将根因分析问题形式化为一个反思引导的树结构搜索过程，通过多智能体协作，对每个微服务的执行日志和性能指标进行推理，利用中间诊断状态的反思分数引导搜索，从而克服传统线性推理路径的局限。在公开数据集Light-OAuth2（同构技术栈）上的实验证明了高诊断准确性；在真实生产环境（异构技术栈）的部署则展示了实际应用价值，但诊断准确率较低、计算成本更高。主要结论表明，LATS-RCA在同构系统中表现优异，但生产环境的异构性、多语言日志和多重根因等因素会显著增加推理复杂度和降低诊断性能，为未来在规模化微服务系统中应用基于LLM的多智能体根因分析提供了实证基础和挑战分析。
