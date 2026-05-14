---
title: "Cognifold: Always-On Proactive Memory via Cognitive Folding"
authors:
  - "Suli Wang"
  - "Yiqun Duan"
  - "Yu Deng"
  - "Rundong Zhao"
  - "Dai Shi"
  - "Xinliang Zhou"
date: "2026-05-13"
arxiv_id: "2605.13438"
arxiv_url: "https://arxiv.org/abs/2605.13438"
pdf_url: "https://arxiv.org/pdf/2605.13438v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Cognitive Architecture"
  - "Proactive Agent"
  - "Graph-based Memory"
  - "Complementary Learning Systems"
relevance_score: 9.2
---

# Cognifold: Always-On Proactive Memory via Cognitive Folding

## 原始摘要

Existing agent memory remains predominantly reactive and retrieval-based, lacking the capacity to autonomously organize experience into persistent cognitive structure. Toward genuinely autonomous agents, we introduce Cognifold, a brain-inspired "always-on" agent memory designed for the next generation of proactive assistants. CogniFold continuously folds fragmented event streams into self-emerging cognitive structures, bootstrapping progressively higher-level cognition from incoming events and accumulated knowledge. We ground this by extending Complementary Learning Systems (CLS) theory from two layers (hippocampus, neocortex) to three, adding a prefrontal intent layer. Emulating the prefrontal cortex as the locus of intentional control and decision-making, CogniFold achieves this through graph-topology self-organization: cognitive structures proactively assemble under the stream, merge when semantically similar, decay when stale, relink through associative recall, and surface intents when concept-cluster density crosses a threshold. We evaluate structural formation using CogEval-Bench, demonstrating that CogniFold uniquely produces memory structures that match cognitive expectations and concept emergence. Furthermore, across 7 broad-coverage benchmarks spanning five cognitive domains, we validate that CogniFold simultaneously performs robustly on conventional memory benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI代理记忆系统缺乏主动性和自主认知结构组织能力的问题。现有代理记忆（如静态知识图谱、文本级重写、混合解耦或时间追踪）本质上是被动、检索式的，其拓扑结构一旦形成便固定不变，无法自主地将持续流入的碎片化事件流组织为持久的认知结构。由于缺乏内生的主动能力，现有系统只能在应用层通过调度触发器、规划循环或周期性反思等方式“嫁接”主动性，但这造成了结构性天花板——智能体只能产生应用层明确设计好的目标，无法自主涌现。

论文借鉴人类生物记忆持续接收感官输入、自主编码巩固并涌现意图的机制，提出Cognifold——一种“始终在线”的主动代理记忆。其核心创新是将互补学习系统（CLS）理论从经典的两层（海马体、新皮层）扩展为三层，增加前额叶意图层。通过图拓扑结构的自组织（持续折叠事件流、语义相似时合并、陈旧时衰减、关联回忆时重新链接、概念簇密度超阈值时涌现意图），Cognifold使记忆本身成为主动认知的基质，让目标能从累积的结构拓扑中内生涌现，而非外部硬编码。

### Q2: 有哪些相关研究？

相关研究主要围绕记忆增强型智能体展开，可分为三类：

**方法类**：包括静态知识图谱、文本级重写（如A-Mem）、混合解耦和时间追踪等现有记忆架构。这些方法均存在共同局限——拓扑结构一旦形成便固定不变，记忆成为“成品图”而非持续代谢的基底。本文Cognifold突破这一限制，通过引入三层互补学习系统（CLS）理论，新增前额叶意图层，实现记忆拓扑的持续自组织。

**理论类**：基于互补学习系统理论，将传统海马体-新皮层二层结构扩展为三层，模拟前额叶皮层的意向控制功能。与依赖应用层硬编码的调度触发器、规划循环或周期性反思不同，Cognifold让意图从概念聚类密度阈值中自主涌现。

**评测类**：本文提出CogEval-Bench，首次从第一性原理直接测量连续事件流下形成的拓扑结构是否符合认知预期。区别于仅关注检索准确率的传统记忆基准（7个涵盖5个认知领域的下游基准），该框架能隔离评估主动涌现能力。

与现有工作的核心区别在于：Cognifold将主动性内化为记忆基质的属性，而非应用层的附加机制；采用透明的图级操作实现测试时学习，既区别于A-Mem的文本级重写，也区别于Titans的梯度更新。

### Q3: 论文如何解决这个问题？

Cognifold通过扩展互补学习系统（CLS）理论，将传统的双层结构（海马体、新皮层）增加为三层（海马体、新皮层、前额叶），实现了主动、持续的记忆组织。其核心架构是一个动态演化的类型化多重图，包含事件节点（海马体层）、概念节点（新皮层层）和意图节点（前额叶层）。系统通过"概念自举"机制实现三个阶段的连续折叠：累积阶段（原始事件流逐字记录）、巩固阶段（检测统计规律并抽象为概念）、结晶阶段（概念簇密度超过阈值时形成意图）。关键技术包括：1）写/读路径解耦——写路径执行拓扑演化操作，读路径执行多策略检索；2）三层优先级分配机制（结构中心性、时间近因、访问频率）构建主动上下文窗口；3）四种结构债务自动偿还操作——强化（REINFORCES边缘）、压缩（MERGE_NODES合并相似概念）、衰减（指数衰减边缘权重）、补全（kNN推理缺失连接）；4）意图生命周期管理（待定→已解决/已拒绝/已推迟）。创新点在于首次将CLS扩展至三层并实现拓扑级自我组织，通过图操作模拟生物记忆代谢，使记忆结构自主折叠、合并、衰减和重连，形成持续的认知脚手架。

### Q4: 论文做了哪些实验？

论文在结构评估和下游记忆质量两方面进行了实验。结构评估使用自建的CogEval-Bench基准，包含6个场景（软工、健康、团队、新闻、学术、支持），每个场景先定义黄金概念图，再生成事件并注入10-15%的干扰项。对比了OpenIE KG、Cognee、HippoRAG 2、GraphRAG、Mem0、Zep和Cognifold。结果：Cognifold在Track A（概念质量）中Harmony达0.476（GraphRAG为0.323），Gold F1为0.358，LLM Quality为0.733，且是唯一Purity非零（0.361）的系统；Track C中压缩比4.6倍，Proactivity 0.614（其他系统均为0）。记忆质量评估覆盖7个基准：LoCoMo（对话记忆，J-Score/ F1）、MuSiQue（多跳推理，EM/F1）、NarrativeQA（叙事理解，F1）、StreamingQA（流式时间QA，F1）、MuTual（对话连贯性，准确率）、ToMi（心理理论，精确匹配）、BABILong（长上下文事实提取，精确匹配）。在LoCoMo上，Cognifold总体J-Score 81.23（仅次于EverMemOS）；在MuSiQue上F1达58.7（超过HippoRAG 2的+9.4和PolicyRAG的+2.8）；在ToMi上+3.3超过AutoToM；在BABILong上+1.2超过ARMT。所有基准统一使用gpt-4o-mini和text-embedding-3-small。

### Q5: 有什么可以进一步探索的点？

首先，Cognifold存在路径依赖问题，即事件输入顺序影响认知结构形成，这与人类学习中的课程效应类似但造成记忆稳定性不足。未来可探索顺序感知的整合机制、基于经验回放的状态平滑，以及对流式图进行有界散度分析，以缓解因顺序变化导致的结构差异。

其次，当前模型对前额叶的模拟仅实现了图式驱动的整合，尚缺乏价值评估、认知控制和反事实推演等关键功能。因此，无法对意图进行长周期效用排序，也无法在更强目标激活时抑制冲动输出，更不能预判后续影响。建议引入强化学习中的价值函数以实现意图优先级排序，加入门控机制进行认知控制，并利用世界模型或反事实推理来预测行动后果。

此外，考虑将认知结构应用于在线学习中的课程自适应编排，使模型能自主感知知识密度并动态组织经验序列，从而提升样本效率和泛化能力。

### Q6: 总结一下论文的主要内容

本文提出了一种名为Cognifold的新型智能体记忆架构，旨在解决现有智能体记忆主要依赖反应式检索、缺乏自主组织经验能力的问题。受大脑互补学习系统理论启发，Cognifold将其从海马体和新皮层两层扩展至三层，新增前额叶意图层，实现了持续的、主动的认知折叠。该方法通过图拓扑自组织机制，将碎片化事件流折叠成自涌现的认知结构：认知结构在事件流中主动组装，语义相似时合并，陈旧时衰减，通过联想回忆重新连接，概念聚类密度超过阈值时浮现意图。在CogEval-Bench基准上的结构形成评估表明，Cognifold能生成符合认知期望和概念涌现的记忆结构。此外，在覆盖五个认知领域的七个广泛基准上，Cognifold在常规记忆基准上也表现稳健。这项工作为下一代主动式智能体的核心记忆设计提供了新范式，推动了从被动检索向主动认知组织的关键转变。
