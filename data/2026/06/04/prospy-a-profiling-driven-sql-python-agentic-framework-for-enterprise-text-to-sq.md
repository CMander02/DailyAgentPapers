---
title: "ProSPy: A Profiling-Driven SQL-Python Agentic Framework for Enterprise Text-to-SQL"
authors:
  - "Zhaorui Yang"
  - "Huawei Zheng"
  - "Sen Yang"
  - "Yuhui Zhang"
  - "Haoxuan Li"
  - "Zhizhen Yu"
  - "Xuan Yi"
  - "Chen Hou"
  - "Defeng Xie"
  - "Chao Hu"
  - "Minfeng Zhu"
  - "Dazhen Deng"
  - "Haozhe Feng"
  - "Danqing Huang"
  - "Yingcai Wu"
  - "Peng Chen"
  - "Wei Chen"
date: "2026-06-04"
arxiv_id: "2606.05836"
arxiv_url: "https://arxiv.org/abs/2606.05836"
pdf_url: "https://arxiv.org/pdf/2606.05836v1"
categories:
  - "cs.CL"
tags:
  - "Text-to-SQL"
  - "Agent"
  - "Multi-stage Reasoning"
  - "Schema Pruning"
  - "Data Profiling"
  - "Enterprise Database"
  - "LLM Agent"
  - "SQL-Python Hybrid"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# ProSPy: A Profiling-Driven SQL-Python Agentic Framework for Enterprise Text-to-SQL

## 原始摘要

Large language models have substantially advanced Text-to-SQL systems, yet applying them to enterprise-scale databases remains challenging. Real-world databases often contain large and heterogeneous schemas, incomplete metadata, dialect-specific SQL syntax, and complex analytical questions that are difficult to solve with a single SQL query. To address these challenges, we propose ProSPy, a Profiling-driven SQL--Python agentic framework for enterprise-scale Text-to-SQL. ProSPy structures the reasoning process into four stages: it first extracts fine-grained data evidence through automatic profiling, progressively prunes large schemas into task-relevant contexts, fetches intermediate views through a dialect-agnostic SQL interface, and finally performs flexible downstream analysis with Python. This design combines the efficiency of SQL over large databases with the flexibility of Python-based analysis, while reducing reliance on unreliable metadata and improving robustness across SQL dialects. Experiments on Spider 2.0-Lite and Spider 2.0-Snow show that ProSPy consistently outperforms strong baselines with both open-source and proprietary models, achieving execution accuracies of 60.15% and 60.51% with Claude-4.5-Opus, without majority voting. Further analysis shows that ProSPy is robust to SQL dialect variations and achieves a favorable trade-off between schema recall and precision.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决企业级文本到SQL任务中的核心挑战。研究背景是，虽然大语言模型在标准文本到SQL基准测试（如Spider、BIRD）上取得了显著进展，但实际企业数据库环境与这些基准存在巨大差异。现有方法的不足主要体现在三个方面：首先，企业级数据库模式通常规模庞大、异构性强，包含众多表、模糊的命名约定和深层嵌套结构，而现有方法依赖重复调用大语言模型和数据库探测来识别相关模式元素，导致高延迟和计算开销；其次，企业数据库的元数据常不完整或不可靠，使得模式语义难以解释，同时复杂分析问题往往需要多个中间视图和下游统计计算，难以用单条SQL查询解决；最后，不同数据库引擎的方言差异使直接生成SQL变得脆弱，导致在简单基准上表现良好的方法在企业场景中性能显著下降。本文提出ProSPy框架，通过将推理过程分解为四个阶段（数据剖析、渐进式模式修剪、方言无关的中间视图获取、Python分析），结合SQL在大规模数据库上的高效检索能力和Python灵活的多步分析能力，以解决企业级文本到SQL的可靠性、可扩展性和方言差异问题。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几类工作：

1. **方法类**：早期的Text-to-SQL研究依赖提示工程和上下文学习，通过示例、分解策略和中间推理步骤引导LLM生成SQL。近期方法进一步引入测试时计算，如蒙特卡洛树搜索、多路径推理和候选选择策略。ProSPy与这些方法的区别在于，它不是单纯优化SQL生成，而是构建了一个四阶段代理框架，将SQL的高效性与Python的灵活性结合，以应对企业级数据库的复杂挑战。

2. **代理工作流类**：受LLM代理成功启发，相关工作探索了两阶段流程：模式链接（如EviLink引入多路径假设模式定位和投票不确定性估计）和SQL生成（如通过自纠正和投票选取最终答案）。ProSPy与EviLink等的区别在于，它不将模式链接作为中间优化步骤，而是以端到端方式解决问题。此外，ProSPy通过自动profile提取细粒度数据证据，渐进式裁剪模式，避免了依赖不可靠元数据和冗余探索。

3. **探索式方法类**：如APEX-SQL通过代理探索进行SQL构建，但其动作空间仍局限于SQL生成，无法充分利用LLM的推理和灵活分析能力。ProSPy则通过引入Python进行下游分析，突破了SQL表达式的限制，实现了更好的效率与灵活性权衡。

总体而言，ProSPy在模式链接、SQL生成和灵活分析方面与现有工作形成互补，并通过实验在Spider 2.0基准上验证了其鲁棒性和优越性。

### Q3: 论文如何解决这个问题？

ProSPy通过四个核心阶段的结构化流程解决企业级Text-to-SQL的挑战。整体框架将复杂分析推理从SQL生成转移到Python编码空间，利用LLM在程序合成和迭代数据分析方面的优势。

**第一阶段：数据画像（Data Profiling）**。针对传统方法通过反复数据库交互获取元数据效率低下的问题，ProSPy设计自动画像流程。给定表名后，画像器通过模板化SQL查询检索所有列及其类型，进行隐式类型检测，并将每列分类为指标、维度、标识符、时间或其他特殊类型等五种语义类型。随后收集类型特定的统计信息（如维度列的值分布、指标列的汇总统计、时间列的时间范围），并记录空值比例和样本值。对于复杂嵌套类型，进行递归模式推断暴露内部结构。结构化画像和轻量级数据预览被序列化注入到智能体上下文中，且每个数据库仅并行画像一次，跨问题复用。

**第二阶段：渐进式模式剪枝（Progressive Schema Pruning）**。与传统最大化召回的方法不同，ProSPy将模式链接形式化为渐进式剪枝过程。每次迭代中，基于LLM的剪枝算子移除与查询无关的模式元素。大模式首先被分批以适应上下文窗口，共享相同列集合的表被压缩分组。每批中LLM识别任务相关表并剪枝无关候选，然后对保留表的列执行相同剪枝。所有批次的结果合并形成精简的模式上下文，在保留必要模式覆盖的同时最小化无关信息。

**第三阶段：智能体数据获取（Agentic Data Fetching）**。引入迭代数据获取范式，替代单条SQL查询。智能体首先规划识别所需数据并分解检索目标，随后通过结构化分析阶段生成视图定义。这些视图定义使用领域特定语言(DSL)编写，围绕维度、指标和条件三个核心组件组织，然后被转译成可执行SQL。迭代过程中，智能体可重用先前定义的视图并构建嵌套视图。

**第四阶段：基于Python的分析**。物化视图数据以CSV保存，智能体加载后在Python中执行最终计算，支持灵活的多步转换和自定义分析操作。遇到执行错误时迭代改进代码，最终结果写入CSV进行比较评估。

创新点在于：(1) 用SQL进行数据检索和轻量聚合，Python负责复杂分析，实现功效与效率的平衡；(2) 通过自动画像减少对不可靠元数据的依赖；(3) DSL抽象屏蔽SQL方言差异，提高跨数据库鲁棒性；(4) 渐进式剪枝在召回率和精确率间取得有利权衡。

### Q4: 论文做了哪些实验？

论文在Spider 2.0基准测试的两个子集（Spider 2.0-Lite和Spider 2.0-Snow，各547个样本）上评估ProSPy。实验使用三个模型：DeepSeek V3.2、GLM-5（开源）和Claude-Opus-4.5（闭源），对比方法包括Spider-Agent、ReForce、AutoLink、DSR-SQL、RSL-SQL、LinkAlign和APEX-SQL。主要采用执行准确率（EX）作为端到端评价指标，以及用于表级模式链接的SRR、NSR、NSP、NSF和token消耗量。

主要结果：在Lite上，ProSPy+Claude-Opus-4.5达到60.15% EX（单次尝试，无多数投票），远超LinkAlign（33.09%，有投票）和ReForce（36.56%，GPT-o3）；在Snow上，ProSPy+Claude-Opus-4.5取得60.51% EX，超过APEX-SQL（51.01%）。模式链接方面，ProSPy达到86.02% NSP和87.40% NSF，大幅领先RSL-SQL（30.53% NSP）和APEX-SQL（53.67% NSP）。消融实验显示，去除数据profiling导致EX下降6.4 pp，用直接SQL替换DSL数据获取下降9.1 pp，用SQL替代Python分析（无投票）下降19.0 pp，证明各模块均至关重要。杂交模型配置（如Claude+GLM）在Lite和Snow上分别达48.63%和51.74%。

### Q5: 有什么可以进一步探索的点？

首先，论文明确指出“错误传播”是核心局限。ProSPy 将复杂推理分解为数据抓取与 Python 分析，但中间视图的错误会直接误导最终结果。未来可探索引入中间结果校验机制，例如设计一个轻量级的验证步骤，让模型对返回的中间表进行语义合理性检查，或使用一致性损失函数来训练模型识别异常数据，从而阻断误差链。

其次，当前评估仅局限于 Spider 2.0 系列的类 Snowflake 环境。对于更异构的数据库（如键值存储、图数据库混杂的混合架构）或缺乏完整元数据的极端场景，ProSPy 的“方言无关”接口是否能保持鲁棒性尚未验证。未来可构建涵盖多种 NoSQL 和流式数据源的新基准，并研究如何将 profiling 阶段从静态统计扩展到自适应采样，以处理极稀疏或大规模的数据分布。此外，当前四阶段流程仍依赖固定顺序，改进思路是探索动态路由机制，让智能体根据问题复杂度自主选择是否跳过 Python 分析步骤，从而在简单查询上避免不必要的开销。

### Q6: 总结一下论文的主要内容

ProSPy提出了一种面向企业级文本到SQL任务的、基于数据剖析的智能体框架。现有方法在处理真实企业数据库时，常因模式庞大、元数据不完整、SQL方言差异及复杂分析需求而表现不佳。该框架将推理过程分解为四个阶段：首先通过自动数据剖析提取细粒度数据特征，随后渐进式修剪大型模式以保留任务相关上下文，接着通过方言无关的SQL接口获取中间视图，最后结合Python进行灵活的下游分析。这种设计融合了SQL在大规模数据上的高效性以及Python的分析灵活性，减少了对不可靠元数据的依赖，并增强了跨SQL方言的鲁棒性。在Spider 2.0-Lite和Spider 2.0-Snow基准上，ProSPy搭配Claude-4.5-Opus模型分别达到60.15%和60.51%的执行准确率（无多数投票），显著优于强基线。进一步分析表明，该框架对SQL方言变化具有鲁棒性，并在模式召回率与精确率之间取得了良好平衡。其核心意义在于为复杂企业场景下的文本到SQL任务提供了结构化、高适应性的解决方案。
