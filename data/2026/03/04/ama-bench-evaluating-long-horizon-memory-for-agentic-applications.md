---
title: "AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications"
authors:
  - "Yujie Zhao"
  - "Boqin Yuan"
  - "Junbo Huang"
  - "Haocheng Yuan"
  - "Zhongming Yu"
  - "Haozhou Xu"
  - "Lanxiang Hu"
  - "Abhilash Shankarampeta"
  - "Zimeng Huang"
  - "Wentao Ni"
  - "Yuandong Tian"
  - "Jishen Zhao"
date: "2026-02-26"
arxiv_id: "2602.22769"
arxiv_url: "https://arxiv.org/abs/2602.22769"
pdf_url: "https://arxiv.org/pdf/2602.22769v2"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "Agent 记忆"
  - "长视野任务"
  - "Agent 架构"
  - "工具使用"
relevance_score: 8.5
---

# AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications

## 原始摘要

Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA-Bench (Agent Memory with Any length), which evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons, paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information and are constrained by the lossy nature of similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA-Agent, an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA-Agent achieves 57.22% average accuracy on AMA-Bench, surpassing the strongest memory system baselines by 11.16%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前智能体（Agent）记忆评估标准与实际应用需求之间的脱节问题。随着大语言模型（LLM）被部署为自主智能体来处理日益复杂的任务（如代码编辑、网页搜索），长时程记忆能力变得至关重要。然而，现有的记忆评估基准主要集中于以对话为中心的人机交互场景，这与现实应用存在显著差距。在真实场景中，智能体记忆是一个连续的智能体-环境交互流，其内容主要由机器生成的符号化表示（如代码、JSON数据、表格）构成，而非简单的自然语言对话。

现有方法存在三个主要不足：一是缺乏对多样化机器生成符号（如代码块、结构化数据）的表征能力；二是缺乏对因果关系的建模，而智能体轨迹中的每个动作都会引发表观环境状态的因果性转换；三是信息冗余度低且目标信息密集，不同于对话中常见的闲聊式冗余。这些不足导致现有记忆系统在长时程、机器主导的智能体任务中表现不佳。

因此，本文的核心问题是：如何构建一个能准确评估智能体在真实长时程任务中记忆能力的基准，并设计一个能有效应对此类任务需求的记忆系统。为此，论文提出了AMA-Bench基准，包含真实世界轨迹和可任意扩展的合成轨迹，以全面评估记忆能力；并进一步提出了AMA-Agent记忆系统，通过因果图保留客观信息与因果依赖，并利用工具增强检索来克服现有基于相似性检索的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、方法类系统和应用类系统。

在**评测基准**方面，现有工作主要分为两类：一是以对话为中心的基准，如LoCoMo、LongMemEval等，它们评估多轮人机对话中的记忆保持能力，其交互内容和来源多为自然语言；二是长上下文基准，如QuALITY、RULER等，侧重于对静态长文档的多跳理解。本文提出的AMA-Bench与这些工作有显著区别：它专注于智能体与环境交互的轨迹评估，其内容来源是机器生成的表示，包含因果依赖和密集的客观信息，更贴近真实智能体应用场景。

在**方法类系统**方面，主要研究路径包括：1) **长上下文模型**，如GPT-5.2、Qwen2.5 1M系列，通过扩展上下文窗口直接处理记忆，但受物理上下文长度限制；2) **检索增强生成（RAG）**，如传统BM25、Qwen3 Embedding系列，以及更结构化的GraphRAG、HippoRAG2等方法，通过外部存储和相似性检索来增强上下文。然而，现有RAG方法多依赖基于相似性或实体的检索，常忽略存储信息中的内在因果关系。

在**应用类系统（记忆智能体系统）**方面，近期研究转向由智能体自主管理记忆，例如MemoryBank、MemGPT让LLM自主决定记忆的检索与更新；MemoRAG采用双系统架构；MEM1、Mem-α、SimpleMem等通过迭代压缩或编辑操作（如插入、删除）来构建和压缩记忆。但这些系统在智能体记忆任务上表现不佳，原因在于其压缩方法多针对自然语言冗余设计，而智能体轨迹是密集且因果结构化的；同时，基于相似性的检索难以有效提取机器生成表示中的所需证据。

本文提出的AMA-Agent系统，通过引入因果图（causality graph）和工具增强检索（tool-augmented retrieval），旨在直接解决现有方法在因果关系捕捉和检索有效性方面的不足，从而在AMA-Bench上取得了显著优于基线的性能。

### Q3: 论文如何解决这个问题？

论文通过提出名为AMA-Agent的新型记忆系统来解决长时程记忆评估与性能不足的问题。其核心方法围绕两个关键机制展开：一是构建因果图以最小化信息损失，二是采用工具增强的检索模块来提升检索效果。

整体框架分为记忆构建与检索推理两大部分。在记忆构建阶段，系统从智能体轨迹中解析相邻的转换对（观察-行动-观察），提取环境与对象状态，识别潜在的状态间因果依赖关系以及状态与对象的关联。这些信息被实例化为有向的因果边和无向的关联边，连接相应的状态节点，最终整合成一个全局的因果图。图中的节点会被映射到潜在嵌入空间，以支持基于相似性的检索和关系推理。

在检索阶段，AMA-Agent首先基于嵌入相似性检索出最相关的K个节点，并进行自我评估以判断证据是否充足。若不足，系统会根据缺失上下文的类型，调用两种工具之一进行补充检索：一是图节点搜索工具，通过深度控制的邻域遍历来聚合多跳上下文和因果关系；二是关键词搜索工具，通过一个允许编写和执行脚本的工具接口，实现精确的关键词匹配和统计聚合。最后，系统综合所有检索到的证据生成最终回答。

创新点主要体现在：1）利用因果图结构化地存储轨迹中的因果与关联信息，克服了传统基于相似性检索的损失性限制，并保留了关键的目标信息；2）引入了工具增强的多模式检索机制，将向量相似性检索与基于图遍历的关系推理、基于脚本的关键词搜索相结合，显著提升了长时程、复杂上下文中关键信息的召回与理解能力。

### Q4: 论文做了哪些实验？

论文在AMA-Bench基准上进行了全面的实验评估。实验设置方面，研究评估了三大类基线方法：长上下文模型、检索增强生成（RAG）和记忆代理，并统一使用Qwen3-32B和Qwen3-8B作为骨干模型以确保公平比较。数据集包括两个互补的子集：1）真实世界子集，包含来自代表性智能体应用的轨迹，配有专家标注的2496个QA对；2）合成子集，包含两个任务共1200个QA对，轨迹长度从8K到128K tokens不等，用于评估长视野下的可扩展性。对比方法涵盖了Claude Haiku、GPT系列、Gemini、Qwen等长上下文模型，以及BM25、GraphRAG、HippoRAG2等多种RAG方法，和MemAgent、MemGPT、MemoRAG等多种记忆代理方法。

主要结果显示，在真实世界子集上，使用Qwen3-32B骨干时，论文提出的AMA-Agent在平均准确率上达到了57.22%，显著超越了最强的RAG基线HippoRAG2（44.80%）和最强的记忆代理基线MemoRAG（46.06%）。具体到四个评估维度（Recall、Causal Inference、State Updating、State Abstraction），AMA-Agent的准确率分别为0.6238、0.6145、0.5305和0.4719，均取得了最优性能。在合成子集上，AMA-Agent也表现出优越的可扩展性，在长达128K tokens的轨迹上仍能保持稳健的高准确率，而长上下文方法在超过32K后性能显著下降。消融实验进一步验证了因果图（Causality Graph）和工具增强检索（Tool-Augmented Retrieval）两个关键组件的必要性，移除它们分别导致平均准确率下降24.6%和22.8%。

### Q5: 有什么可以进一步探索的点？

该论文聚焦于单次任务内的记忆评估，其局限性在于尚未涉及跨任务的终身学习场景。未来研究可探索如何将因果图等机制扩展到长期、多任务环境中，使智能体能在不同任务间积累和复用知识。此外，当前基准主要依赖合成与真实轨迹，未来可纳入更动态、开放的环境交互数据，以测试记忆系统在不可预见情况下的鲁棒性。改进思路方面，可尝试将符号逻辑与神经网络检索结合，提升对复杂因果链的推理能力；同时，引入记忆的主动遗忘与压缩机制，以优化长期存储效率。这些方向有望推动智能体记忆向更通用、可持续的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型作为自主智能体在复杂应用中面临的长时记忆评估标准缺失问题，提出了AMA-Bench评估基准。核心问题是现有基准主要关注人机对话场景，而实际智能体记忆是连续的环境交互流，且多为机器生成表示，导致评估与实践脱节。为此，作者构建了包含真实世界智能体轨迹与专家标注问答、以及可扩展至任意长度的合成轨迹与规则生成问答的数据集。研究发现，现有记忆系统在AMA-Bench上表现不佳，主要归因于缺乏因果与目标信息，且受限于基于相似性的检索机制的信息损失。为解决这些局限，论文进一步提出了AMA-Agent记忆系统，其采用因果图与工具增强检索机制。实验表明，AMA-Agent在AMA-Bench上达到57.22%的平均准确率，超越现有最强基线11.16%，显著提升了智能体在长时记忆任务中的性能。
