---
title: "An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration"
authors:
  - "Dutao Zhang"
  - "Tian Liao"
date: "2026-05-05"
arxiv_id: "2605.03989"
arxiv_url: "https://arxiv.org/abs/2605.03989"
pdf_url: "https://arxiv.org/pdf/2605.03989v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Retrieval-Augmented Generation"
  - "Agent Skill"
  - "Experience Memory"
  - "Retrieval Strategy Orchestration"
relevance_score: 7.5
---

# An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration

## 原始摘要

Retrieval-augmented generation systems often assume that one fixed retrieval pipeline is sufficient across heterogeneous tasks, yet factoid question answering, multi-hop reasoning, and scientific verification exhibit different retrieval preferences. We present Experience-RAG Skill, an agent-oriented pluggable retrieval orchestration layer positioned between the agent and the retriever pool. The proposed skill analyzes the current scene, consults an experience memory, selects an appropriate retrieval strategy, and returns structured evidence to the agent. Under a fixed candidate pool, Experience-RAG Skill achieves an overall nDCG@10 of 0.8924 on BeIR/nq, BeIR/hotpotqa, and BeIR/scifact, outperforming fixed single-retriever baselines and remaining competitive with Adaptive-RAG-style routing. The results suggest that retrieval strategy selection can be productively encapsulated as a reusable agent skill rather than being hard-coded in the upper workflow.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

检索增强生成（RAG）系统当前普遍假设单一固定检索流程可适用于异构任务，但事实性问答、多跳推理和科学验证等场景展现出截然不同的检索偏好：密集检索器擅长直接事实问题，混合检索对多跳推理和证据匹配更稳定。现有方法如自适应路由虽尝试动态选择，但大多将检索策略硬编码在上层工作流中，缺乏可插拔的通用技能层。本文的核心问题是：如何将检索策略选择封装为智能体的可复用技能，使其能根据任务场景动态编排检索流程，而非依赖固定流水线。具体而言，论文提出Experience-RAG Skill——位于智能体与检索器池之间的可插拔编排层，通过场景分析、经验记忆查询、策略路由和结果打包四步，为不同任务选择最优检索策略。在固定候选池设置下，该技能在BeIR/nq、BeIR/hotpotqa和BeIR/scifact上达到0.8924的nDCG@10，超越单一检索基线并与自适应路由持平，证明检索策略选择可有效封装为独立于上层流程的智能体技能，解决了异构任务下检索策略动态适配的通用性问题。

### Q2: 有哪些相关研究？

相关研究可分为方法类、评测类和框架类。方法方面，现有RAG工作主要关注单一检索管道优化，如查询重写、层级检索、主动检索、纠错检索、自反检索和长上下文检索等，这些方法通常假设固定检索策略可应对所有任务。本文区别于这些工作，提出将检索策略选择封装为可插拔的智能体技能，而非硬编码在上层工作流中。评测类研究如BeIR基准（包含nq、hotpotqa、scifact）常被用于评估多任务检索性能，本文即在该标准上评估。框架方面，本文与工具使用和行动型语言智能体（如ReAct、Toolformer）相关，但聚焦于检索策略编排这一具体子问题；与Adaptive-RAG的路由方法类似，但本文通过经验记忆记录场景特征和多检索器表现，实现更细粒度的策略选择，而非简单的任务级路由。总体而言，本文创新在于将检索策略选择问题从单一检索方法提升为可复用智能体技能层。

### Q3: 论文如何解决这个问题？

Experience-RAG Skill通过设计一个面向Agent的可插拔检索编排层来解决固定检索管线无法适应异构任务的问题。整体框架由六个核心模块构成：Skill Interface、Scene Analyzer、Experience Memory、Strategy Router、Retriever Pool和Result Packager。Agent仅通过统一的Skill Interface与系统交互，无需关心底层检索细节。

核心方法分三步：首先，Scene Analyzer根据查询q、对话历史h和任务元数据m构建结构化场景表示s，涵盖任务类型、领域、上下文长度、查询复杂度、查询风格和文档结构等维度。然后，Strategy Router结合Experience Memory中的经验记录进行路由决策，输出最优检索策略r*。经验记录不仅存储最佳策略标签，还包含场景特征、得分向量、最佳策略及裕度，支持基于规则和学习的路由。当前最强配置采用基于规则的路由：直接任务映射到稠密检索，多跳和科学任务映射到混合RRF。最后，Retriever Pool执行检索，Result Packager将结果打包为标准化结构化证据包返回给Agent。

主要创新点在于：将检索策略选择封装为可复用的Agent技能，而非硬编码在上层工作流中；引入经验记忆机制实现场景特征的记录与复用；通过统一的面向Agent的接口和结构化证据包装，使编排层可插拔且易于替换底层检索器。在BeIR/nq、BeIR/hotpotqa和BeIR/scifact上，该方法取得0.8924的整体nDCG@10，优于固定单检索器基线，并与Adaptive-RAG风格路由性能相当。

### Q4: 论文做了哪些实验？

论文在三个公共检索基准 BeIR/nq、BeIR/hotpotqa 和 BeIR/scifact 上进行实验，每个数据集采样 120 个查询和候选语料库。实验设置了固定单检索器基线（BM25、Rewrite-BM25、Dense、Hybrid RRF）以及 Experience-RAG Skill，同时扩展了现代基线（HyDE、RAPTOR-style、LongRAG-style、Adaptive-RAG-style）。主要评估指标包括 Recall@10、MRR@10 和 nDCG@10。结果显示，Experience-RAG Skill 在固定候选池中取得最佳整体检索性能：nDCG@10 为 0.8924、Recall@10 为 0.9428、MRR@10 为 0.9006，优于最强固定单方法基线 Hybrid RRF（nDCG@10 0.8802）及 Dense（0.8627）、BM25（0.8426）等方法。在扩展候选池对比中，Experience-RAG Skill（nDCG@10 0.8924）与 Adaptive-RAG-style（0.8934）性能几乎持平，且显著优于 HyDE（0.8326）、LongRAG-style（0.7095）和 RAPTOR-style（0.6841）。实验表明，该技能在异构任务编排中的优势显著，而非在每个子任务上单独占优。

### Q5: 有什么可以进一步探索的点？

首先，论文在三个基准测试上的实验采用了采样语料而非全量数据集，这限制了结论的泛化性。未来应在更大规模、更完整的语料库上验证该方法的鲁棒性。其次，学习驱动的策略路由尚未超越基于规则的基线，表明经验记忆的利用效率或策略选择算法有待改进。可以探索强化学习或在线学习机制，使模型能从持续交互中动态优化路由决策。第三，当前实现仍假设固定的候选检索器池，限制了系统对新检索器的适应能力。未来可研究动态更新候选池的机制，例如自动发现并集成领域特定检索器。最后，工作流案例分析是定性的，缺乏端到端的交互式智能体基准。建议构建包含多轮对话、任务推理的完整评估框架，量化经验技能对智能体整体性能的提升。此外，可引入元学习来加速经验积累，或设计经验压缩机制以降低存储开销。

### Q6: 总结一下论文的主要内容

传统的检索增强生成系统通常假设单一固定检索管线能适用于所有异构任务，但事实问答、多跳推理和科学验证任务实际具有不同的检索偏好。为此，论文提出Experience-RAG Skill，这是一个智能体导向的可插拔检索编排层，位于智能体和检索器池之间。该技能通过分析当前场景、查阅经验记忆、选择合适的检索策略，并向智能体返回结构化证据。在固定候选池下，Experience-RAG Skill在BeIR/nq、BeIR/hotpotqa和BeIR/scifact上取得了整体nDCG@10为0.8924的成绩，优于固定单检索器基线，并与Adaptive-RAG式路由竞争。主要结论表明，检索策略选择可以有效地封装为可复用的智能体技能，而非硬编码在上层工作流中。
