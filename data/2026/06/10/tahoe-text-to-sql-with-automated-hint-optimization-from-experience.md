---
title: "TAHOE: Text-to-SQL with Automated Hint Optimization from Experience"
authors:
  - "Zhiyi Chen"
  - "Jie Song"
  - "Peng Li"
date: "2026-06-10"
arxiv_id: "2606.12387"
arxiv_url: "https://arxiv.org/abs/2606.12387"
pdf_url: "https://arxiv.org/pdf/2606.12387v1"
categories:
  - "cs.DB"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Text-to-SQL Agent"
  - "Agent Memory/Experience"
  - "Agent Prompt Optimization"
  - "Agent Benchmark"
relevance_score: 8.0
---

# TAHOE: Text-to-SQL with Automated Hint Optimization from Experience

## 原始摘要

Large Language Models (LLMs) have democratized database access through Text-to-SQL, but moving from prototypes to production remains difficult. Real deployments must handle strict SQL dialects, massive schemas, and evolving user preferences, while supervised fine-tuning is costly and rigid and agentic test-time scaling is expensive. We present Tahoe, a system that treats prompt optimization as a dynamic data management problem. Tahoe uses an error-driven hint learning pipeline across Development and Deployment to consolidate debugging traces into a structured Hint Bank. Compiler feedback is distilled into reusable Syntax Hints for dialect-specific rules, while execution and user feedback are converted into Semantic Hints for schema- and user-specific logic. Tahoe further introduces a Strategy Layer that models conflicting user intents as competing strategies under shared natural-language triggers, with recency signals and post-learning attribution statistics that summarize empirical success, harm, inertness, and support. At inference time, Tahoe retrieves relevant hints and guides the LLM through Logic Planning followed by SQL Synthesis. We implement and evaluate the development-phase workflow, leaving deployment-time human-feedback updates for future work. On Spider 2.0-Snow, Tahoe substantially improves Text-to-SQL without updating model parameters. On 113 supervised Spider 2.0-Snow-0212 examples using GPT-5.5, Tahoe raises pass rate from 61.95 percent to 79.42 percent and pass-at-4 from 72.57 percent to 87.61 percent, achieves 100 percent Snowflake syntax pass rate, and reduces average compiler-feedback critic rounds from 2.79 to 0.12 per sampled candidate. The same Hint Bank also transfers to weaker backbones, including a 19.7 percentage-point pass-rate gain on Doubao-2.0-lite.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将Text-to-SQL从原型系统部署到实际生产环境时面临的三大核心挑战：严格的SQL方言约束、大规模数据库模式推理以及不断演变的用户意图。现有方法存在明显不足：基于测试时扩展的智能体工作流虽然能提升准确性，但会产生高延迟和昂贵的计算成本，且会话间无法积累经验，导致重复错误；监督微调（SFT）能内化领域知识，但成本高昂且僵化固定，无法适应数据库模式或用户偏好的动态变化，同时模型权重不可迁移；而基于文档的检索增强生成（RAG）方法则因“上下文窗口谬误”引入噪声，导致关键信息被淹没，难以提取精确的领域逻辑。

为克服上述局限性，本文提出TAHOE系统，将提示优化重构为一个动态数据管理问题。其核心思想是，通过错误驱动的提示学习管道，将调试痕迹与用户反馈等经验转化为结构化的、可复用的“提示库”（Hint Bank）。与噪声大、速度慢的现有方法不同，TAHOE旨在检索简洁的、由错误驱动的精确提示，在保持低延迟和模型无关性的同时，实现持续进化与高准确性，从而显著降低初始生成的错误率，避免昂贵的迭代修正循环。

### Q2: 有哪些相关研究？

**指令提示优化方法**：AutoHint、基于梯度下降与束搜索的自动提示优化、GEPA等通过LLM自主生成和优化全局提示，但易陷入单一提示无法处理企业数据中用户间逻辑冲突。TAHOE将提示优化重构为数据管理问题，构建结构化提示库，按触发词、作用域和策略组织，实现查询特定检索与冲突显式管理。  
**Text-to-SQL提示增强方法**：DIN-SQL、DAIL-SQL通过精细分步提示优化，ReFSQL、SQLGenie等采用检索增强生成（RAG）从示例库检索匹配对。但RAG常受无关信息干扰。TAHOE转向检索显式、抽象的语法提示和语义提示，而非原始样例，并利用策略层建模互斥逻辑，结合时间戳与归因统计动态消歧。  
**测试时扩展方法**：Agentar-Scale-SQL等通过多步推理与迭代修正提升精度，却引入高延迟且错误不持久化。TAHOE将计算负载左移至开发阶段的错误驱动学习，通过持久化提示库避免重复错误，替代代价高昂的在线迭代。  
**长期记忆系统**：Generative Agents、MemGPT、ChatDB、Mem0等通过内存流或结构化存储增强LLM记忆。TAHOE专门为Text-to-SQL设计策略层，层级化保留互斥行为而非聚合，按用户上下文动态解决语义冲突。  
**监督微调方法**：SyntaxSQLNet、RAT-SQL、PICARD等依赖标注数据进行参数更新，面临“刚性陷阱”——适应新模式或方言需重新训练。TAHOE保持LLM参数不变，仅更新外部提示库，实现轻量、模型无关且可迁移的适配。

### Q3: 论文如何解决这个问题？

TAHOE将提示优化视为动态数据管理问题，核心方法是构建一个持续演化的Hint Bank作为持久化知识库。系统分为开发和部署两阶段，开发阶段利用离线有标注数据（含真实SQL和执行结果）初始化Hint Bank，部署阶段通过编译器反馈和用户反馈异步更新。

架构设计围绕三个核心模块：1）Hint Learning Module作为"写入者"，接收查询上下文、冻结的全局Hint Bank和反馈信号，通过三层学习流水线生成提示：首先进行多样本采样推理，然后依次进行语法反馈（利用编译器修复方言错误，生成Syntax Hints）和语义调试（比较执行结果与真实值，生成Semantic Hints），最后通过多迭代提示优化验证修改效果；2）Hint Management Module作为"策展人"，批量合并各示例的临时提示增量，去重、解决冲突，核心创新是Strategy Layer，将互斥行为（如不同舍入规则）建模为共享自然语言触发器下的竞争策略，维护学习时间戳信号和事后归因统计（成功、危害、惰性、支持度），用于推理时排序和平衡纠错与普通行为；3）Hint-Guided Inference Module在推理时检索相关提示，先进行逻辑规划再进行SQL合成。

关键技术包括：错误驱动的提示学习流程、语法/语义差分提取、临时提示库的迭代验证、策略层的冲突建模和信号维护。系统无需更新模型参数即可显著提升Text-to-SQL性能。

### Q4: 论文做了哪些实验？

论文主要评估了TAHOE系统在Text-to-SQL任务上的开发阶段性能。实验使用Spider 2.0-Snow数据集及其监督子集Spider 2.0-Snow-0212（113个示例），基准测试涵盖了Snowflake SQL方言的严格语法要求。对比方法为无提示优化的基线GPT-5.5模型。主要结果：在监督集上，TAHOE将pass rate从61.95%提升至79.42%，pass-at-4从72.57%提升至87.61%；Snowflake语法通过率达到100%；平均编译器反馈迭代次数从2.79降至0.12。此外，TAHOE的Hint Bank有效迁移至更弱的模型（Doubao-2.0-lite），pass rate提升19.7个百分点。实验验证了无需更新模型参数，仅通过错误驱动的提示优化即可显著提升性能。

### Q5: 有什么可以进一步探索的点？

Tahoe当前仅在开发阶段验证了Hint的有效性，未来可探索完整的人机交互闭环：将用户反馈（如错误修正、偏好调整）实时转化为语义提示，并研究提示的长期衰减与自动更新策略。其次，Hint Bank的跨任务泛化性值得深挖——当前仅测试了Snowflake SQL，可尝试覆盖更多方言（如BigQuery、DuckDB）并增加Schema动态变化的适应性。策略层目前依赖人工设定的触发器，可引入强化学习让模型自动发现用户意图与提示策略的映射关系。另外，Tahoe对较弱的基座模型（如Doubao）提升明显但仍有19.7%的增益空间，可尝试将Hint与小型模型的知识蒸馏结合，或在提示检索中增加置信度分数来自动降级到更强的LLM。最后，多轮交互中的意图冲突建模仅基于回数统计，未来可引入因果推断区分用户真实意图与偶然性反馈。

### Q6: 总结一下论文的主要内容

TAHOE提出了一种将提示优化转化为持久化数据管理问题的方法，用于解决Text-to-SQL在实际部署中面临的SQL方言严格、模式庞大和用户偏好演变等挑战。核心贡献包括：一个基于错误驱动的提示学习流水线，从开发调试和部署反馈中提取可复用的语法提示和语义提示，构建结构化提示库；一个策略层，通过触发-策略抽象建模冲突用户意图，并利用近因信号和后学习归因统计进行运行时排序。在Spider 2.0-Snow基准测试中，使用GPT-5.5时，TAHOE将通过率从61.95%提升至79.42%，语法通过率达100%，平均修正轮次从2.79降至0.12，且提示库可跨模型迁移，展现了高效、持续演化、模型无关和泛化能力强的特点。
