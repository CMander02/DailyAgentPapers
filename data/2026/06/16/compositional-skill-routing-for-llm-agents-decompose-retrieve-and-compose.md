---
title: "Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose"
authors:
  - "Xueping Gao"
date: "2026-06-16"
arxiv_id: "2606.18051"
arxiv_url: "https://arxiv.org/abs/2606.18051"
pdf_url: "https://arxiv.org/pdf/2606.18051v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "技能路由"
  - "任务分解"
  - "组合检索"
  - "基准评测"
  - "多步骤规划"
relevance_score: 8.5
---

# Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose

## 原始摘要

LLM agents increasingly rely on external skills -- reusable tool specifications -- but real-world tasks often require composing multiple skills, not just selecting one. We formalize this as the Compositional Skill Routing problem: given a complex user query and a large skill library, decompose the query into atomic sub-tasks, retrieve the appropriate skill for each sub-task, and compose an executable plan. We present SkillWeaver, a decompose-retrieve-compose framework combining an LLM task decomposer, a bi-encoder skill retriever with FAISS indexing, and a dependency-aware DAG planner. To support evaluation, we introduce CompSkillBench, a benchmark of 300 compositional queries over 2,209 real MCP server skills spanning 24 functional categories, sourced from the public MCP ecosystem. Our experiments reveal that task decomposition quality is the primary bottleneck: standard LLM decomposition reaches only 34.2% category recall at the step level. To address this, we propose Iterative Skill-Aware Decomposition (SAD), a retrieval-augmented feedback loop that iteratively aligns decomposition with available skills. SAD improves decomposition accuracy from 51.0% to 67.7% (+32.7%, Wilcoxon p < 10^-6) in a single iteration; DA-conditioned analysis confirms that correct granularity is the prerequisite for effective retrieval (CatR@1 rises from 34% to 41% when DA=1). SkillWeaver reduces context window consumption by over 99%, and transfer experiments confirm generalization (+35.6% relative DA gain even when target categories are absent from the retrieval pool).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在组合使用外部技能时面临的“组合技能路由”问题。研究背景是，LLM智能体越来越依赖外部工具（技能）来执行任务，但现实世界的复杂查询往往需要组合多个技能，而非简单选择单个技能。现有方法的不足在于：大多数检索增强生成（RAG）方法仅支持单一技能选择，缺乏对多技能组合的支持；任务分解质量低下，标准LLM分解在步骤级别的类别召回率仅为34.2%，成为性能瓶颈；现有评估基准不覆盖组合查询与大规模技能库。本文核心问题是：如何设计一个框架，让LLM智能体能够将复杂用户查询分解为原子子任务，从大规模技能库中为每个子任务检索合适技能，并组合成可执行的依赖感知计划。为此，作者提出了SkillWeaver框架，包含LLM任务分解器、双编码器技能检索器（采用FAISS索引）和依赖感知的DAG规划器，并通过引入迭代式的技能感知分解（SAD）方法，利用检索增强的反馈循环来对齐分解与可用技能，显著提升了分解准确率，从而解决了组合技能路由中的核心瓶颈。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

**方法与框架类**：本文与ReAct、Toolformer等工具增强型LLM方案不同，后者侧重单步工具选择，而SkillWeaver解决多技能组合问题。与FunSearch、Voyager等程序化智能体相比，本文更关注技能库的检索效率（使用FAISS索引）。Plan-and-Solve等通用规划方法则未考虑技能库的结构化检索。

**检索增强类**：传统检索增强生成（RAG）通常检索文本段落，而本文提出细粒度技能检索（bi-encoder）和迭代式Skill-Aware Decomposition（SAD），这是对标准RAG在任务分解场景的改进。与Self-Ask、Least-to-Most等启发式分解方法相比，SAD通过检索反馈动态调整子任务粒度。

**评测基准类**：现有工具评测（如ToolBench、API-Bank）主要测试单工具调用，而CompSkillBench针对组合查询构建，包含2209个真实MCP技能。与SWE-bench等端到端任务不同，本文更系统化地评估分解-检索-组合的每个环节（提出DA、CatR等分解质量指标）。

核心区别在于：1）首次形式化组合技能路由问题；2）提出依赖感知的DAG规划器；3）设计检索增强的迭代分解策略，实验证明分解质量是主要瓶颈。

### Q3: 论文如何解决这个问题？

论文通过提出SkillWeaver框架系统性地解决了组合技能路由问题，核心方法为“分解-检索-组合”三阶段架构。整体框架由三个模块组成：首先，LLM任务分解器将复杂用户查询原子化为子任务序列；其次，基于双编码器（bi-encoder）的技能检索器利用FAISS索引从包含2,209个真实MCP服务器技能的库中高效匹配各子任务对应技能；最后，依赖感知的有向无环图（DAG）规划器将检索结果组合成可执行计划。关键技术包括：提出迭代式技能感知分解（SAD）方法，通过检索增强的反馈循环持续对齐子任务分解与可用技能——在单次迭代中将分解准确率从51.0%提升至67.7%（提升32.7%），验证了分解质量是检索性能的前提条件；采用双编码器架构和FAISS索引实现>99%的上下文窗口节约，显著降低计算开销。创新点体现在三方面：一是形式化定义了组合技能路由问题并构建了包含300个组合查询、覆盖24个功能类别的CompSkillBench基准；二是揭示了标准LLM分解在步骤级别仅达34.2%类别召回率的瓶颈，并提出SAD迭代优化策略；三是通过依赖感知的DAG规划确保技能组合逻辑正确性，在目标类别完全不在检索池的零样本场景中仍获得+35.6%的相对准确率提升。

### Q4: 论文做了哪些实验？

论文围绕Compositional Skill Routing问题，在CompSkillBench基准上进行了系统实验。该基准包含300个组合查询，技能库涵盖2209个真实MCP服务器技能，分属24个功能类别。

实验设置包括三个核心组件：LLM任务分解器、基于双编码器和FAISS索引的技能检索器、依赖感知的DAG规划器。对比方法涉及标准LLM分解、迭代技能感知分解（SAD）等。主要发现：任务分解质量是首要瓶颈，标准LLM分解在步骤级类别召回率仅34.2%；SAD通过检索增强反馈循环，单次迭代将分解准确率从51.0%提升至67.7%（提升32.7%，Wilcoxon检验p<10^-6）；当分解准确性（DA=1）时，类目检索召回率（CatR@1）从34%升至41%。此外，SkillWeaver上下文窗口消耗降低超过99%；迁移实验中即使目标类别不在检索池内，DA仍相对提升35.6%。这些结果验证了组合技能路由中分解-检索-组成范式的有效性及其泛化能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，虽然SAD显著提升了分解质量，但当前仅支持单轮迭代优化，实际应用中可能需要更鲁棒的多轮自适应机制；其次，依赖FAISS的稠密检索在跨领域迁移时可能因特征分布偏移导致召回率下降；最后，评估基准CompSkillBench仅包含静态技能库，未覆盖动态更新的实战场景。

未来可从三个方向改进：一是引入强化学习或主动学习策略，让智能体在规划失败时自主请求人类反馈，实现分解策略的在线进化；二是结合图神经网络对技能依赖关系进行显式建模，将DAG规划升级为端到端可微的神经符号系统；三是探索技能库的动态扩展机制，例如利用增量学习持续吸收新MCP服务器技能，或通过元学习实现零样本跨域泛化。此外，当前94.7%的步数压缩率暗示还有优化空间，可尝试用更轻量的蒸馏模型替代LLM分解器。

### Q6: 总结一下论文的主要内容

该论文提出组合式技能路由问题，即面对复杂用户查询和庞大技能库时，需要将查询分解为原子子任务，为每个子任务检索适当技能，并组合成可执行计划。为此，作者设计了SkillWeaver框架，采用分解-检索-组合流程，结合LLM任务分解器、基于双编码器与FAISS索引的技能检索器，以及依赖感知的有向无环图规划器。为评估该方法，论文创建了CompSkillBench基准，包含300个组合查询，覆盖24个功能类别的2209个真实MCP服务器技能。实验发现，任务分解质量是主要瓶颈，标准LLM分解的步骤级类别召回率仅34.2%。为此，作者提出迭代技能感知分解（SAD），一种检索增强的反馈循环，单次迭代将分解准确率从51.0%提升至67.7%（提升32.7%）。核心结论是：正确的分解粒度是有效检索的前提，该方法能减少超过99%的上下文窗口消耗，并在迁移实验中表现出良好的泛化能力。
