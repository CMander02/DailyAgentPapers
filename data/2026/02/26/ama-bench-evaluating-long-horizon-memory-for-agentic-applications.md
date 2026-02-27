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
pdf_url: "https://arxiv.org/pdf/2602.22769v1"
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

这篇论文旨在解决当前智能体（Agent）记忆评估标准与实际应用需求之间的脱节问题。随着大语言模型（LLM）被部署为自主智能体来处理日益复杂的任务（如代码编辑、网页搜索），长时程记忆能力变得至关重要。然而，现有的记忆评估基准主要集中于以对话为中心的人机交互场景，这与现实智能体应用中的记忆特性存在显著差距。

现有方法的不足主要体现在三个方面：首先，在表征类型上，现有基准主要处理自由形式的自然语言，而真实智能体轨迹包含多样化的机器生成符号（如JSON、代码块、ASCII表格）。其次，在因果性上，智能体行动会引发环境状态的因果转换，而现有基准遵循无约束的语言流。最后，在信息密度上，智能体轨迹是客观、信息密集的机器生成内容，而对话基准常包含冗余的社交闲聊。

因此，本文的核心问题是：如何构建一个能准确评估智能体在真实长时程任务中记忆能力的基准，并设计出能克服现有记忆系统缺陷的新方法。为此，论文提出了AMA-Bench基准，包含真实世界轨迹和可任意扩展的合成轨迹，以评估长时程记忆。同时，针对现有记忆系统因基于相似性的检索和损失性压缩导致的性能瓶颈，论文提出了AMA-Agent解决方案，通过因果图工具增强检索来提升记忆性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、记忆增强方法以及记忆代理系统。

在**评测基准**方面，现有工作主要分为两类：一是以对话为中心的基准（如LoCoMo、LongMemEval、MemoryAgentBench等），它们评估多轮人机对话中的记忆保持能力，但交互范式以人类语言为主；二是长上下文基准（如QuALITY、RULER、LongBench v2等），侧重于对静态长文档的多跳理解。本文提出的AMA-Bench与这些工作的主要区别在于，它专注于评估**智能体与环境交互**的记忆，其轨迹由机器生成的表示、因果依赖和密集的客观信息构成，更贴近实际自主应用场景。

在**记忆增强方法**上，相关研究包括：1）**长上下文模型**（如GPT-5.2、Qwen2.5 1M），通过扩展上下文窗口直接处理记忆，但受物理长度限制；2）**检索增强生成（RAG）**，包括基于相似性的传统方法（如BM25、Qwen3 Embedding）和结构化方法（如GraphRAG、HippoRAG2），它们通过外部存储和检索来增强记忆，但大多依赖相似性或实体中心检索，常忽略信息间的因果性。

在**记忆代理系统**方面，近期研究（如MemoryBank、MemGPT、MemoRAG、MEM1、SimpleMem等）让LLM代理自主管理记忆的构建、压缩和检索。然而，这些方法多针对自然语言设计，依赖压缩和基于相似性的检索，在处理智能体轨迹时效果不佳，因为轨迹信息密集、因果结构强且机器生成表示多，相似性检索难以准确提取所需证据。

本文的AMA-Agent系统通过引入因果图（causality graph）和工具增强检索，直接针对上述局限性进行改进，从而在AMA-Bench上取得了显著优于现有基线的性能。

### Q3: 论文如何解决这个问题？

论文通过提出名为AMA-Agent的新型记忆系统来解决长时程记忆评估与性能不足的问题。其核心方法围绕两个关键机制展开：一是构建因果图以最小化信息损失，二是采用工具增强的检索模块来提升检索效果。

在架构设计上，AMA-Agent首先从智能体的交互轨迹中构建一个全局因果图。该过程分为三个阶段：首先，解析每个时间步的相邻转换对（观察-行动-观察），提取环境与对象状态，并识别潜在的状态间因果依赖关系以及状态与对象的关联；接着，将这些关系实例化为连接相应状态节点的有向因果边和无向关联边；最后，将这些局部交互整合成全局因果图，并将节点映射到潜在嵌入空间，以支持基于相似性的检索和关系推理。

除了基于嵌入相似性的检索，AMA-Agent还引入了工具增强的搜索机制。其工作流程如下：首先基于嵌入相似性检索前K个节点，并进行自我评估以判断检索到的证据是否足以回答问题。若证据不足，系统会分类缺失的上下文类型，并调用图节点搜索工具或关键词搜索工具。在图节点搜索路径中，执行深度控制的邻域遍历，以聚合多跳上下文和因果关系；在关键词搜索路径中，则通过工具接口编写和执行脚本，进行程序化分析，实现精确的关键词匹配和统计聚合。最终，系统综合所有检索到的证据生成回答。

创新点主要体现在：一是利用因果图结构化地捕捉智能体与环境交互中的因果和关联关系，克服了传统基于相似性检索的损失性限制；二是结合了多种检索策略（相似性检索、图遍历、关键词搜索），通过工具增强的方式动态补充证据，有效提升了长时程记忆任务中的信息完整性和检索准确性。

### Q4: 论文做了哪些实验？

论文在AMA-Bench基准上进行了全面的实验评估。实验设置方面，研究评估了三大类基线方法：长上下文模型、检索增强生成（RAG）和记忆代理，并统一使用Qwen3-32B和Qwen3-8B作为骨干模型以确保公平比较。数据集包括两个互补的子集：1）真实世界子集，包含来自代表性智能体应用的轨迹，配有专家标注的2496个QA对；2）合成子集，包含两个任务共1200个QA对，轨迹长度从8K到128K令牌不等，用于评估长视野下的可扩展性。评估指标主要报告准确率和F1分数。

主要结果如下：在真实世界子集上，直接使用长上下文模型的对比中，GPT 5.2取得了最高的平均准确率（0.7226）。但在统一使用Qwen3-32B骨干模型的记忆系统对比中，论文提出的AMA-Agent在所有四个维度（Recall、Causal Inference、State Updating、State Abstraction）上都达到了最优，平均准确率为0.5722，显著超过了最强的RAG基线HippoRAG2（0.4480）和最强的记忆代理基线MemoRAG（0.4606）。在合成子集上，实验表明其性能与真实世界子集强相关，并且AMA-Agent在序列长度增至128K时仍能保持稳健的高准确率，显示出优异的可扩展性。消融实验进一步验证了因果图（Causality Graph）和工具增强检索（Tool-Augmented Retrieval）两个关键组件的必要性，移除任一组件都会导致性能显著下降（平均准确率分别降至0.43和0.44）。

### Q5: 有什么可以进一步探索的点？

该论文聚焦于单次任务内的记忆评估，其局限性在于尚未涉及跨任务的终身学习场景。未来研究可探索如何将因果图等机制扩展到长期、多任务环境中，使智能体能在不同任务间积累和复用知识。此外，当前评估主要依赖合成与真实轨迹，未来可引入更动态、开放的环境，测试记忆系统在不可预见干扰下的鲁棒性。从方法改进角度，可结合神经符号方法，将符号化的因果推理与神经网络的模糊检索相结合，以平衡精确性与泛化能力。另外，记忆的主动遗忘与重要性加权机制也值得深入，以避免信息过载并提升长期效率。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型作为自主智能体在复杂应用中长期记忆能力评估的不足，提出了AMA-Bench这一新基准。核心问题是现有评估标准主要关注以人类对话为中心的交互，而实际智能体记忆是连续的、主要由机器生成表征的智能体-环境交互流，两者存在显著差距。

为此，论文贡献了AMA-Bench，它包含两个关键部分：一是来自代表性智能体应用的真实世界交互轨迹及专家标注的问答对；二是可扩展至任意长度的合成交互轨迹及基于规则的问答对。通过全面实验，论文发现现有记忆系统在AMA-Bench上表现不佳，主要原因是缺乏因果性和目标信息，且受限于许多系统采用的、有信息损失的基于相似性的检索方法。

为解决这些局限，论文进一步提出了AMA-Agent记忆系统，其特点是引入了因果图并采用工具增强的检索机制。实验结果表明，AMA-Agent在AMA-Bench上达到了57.22%的平均准确率，比最强的基线记忆系统高出11.16%，有效证明了新基准的价值及所提方法的优越性。该工作为评估和提升智能体在真实应用中的长期记忆能力提供了重要的基准和方法。
