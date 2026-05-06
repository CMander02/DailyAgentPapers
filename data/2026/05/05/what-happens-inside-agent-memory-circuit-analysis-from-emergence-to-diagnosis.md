---
title: "What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis"
authors:
  - "Xutao Mao"
  - "Jinman Zhao"
  - "Gerald Penn"
  - "Cong Wang"
date: "2026-05-05"
arxiv_id: "2605.03354"
arxiv_url: "https://arxiv.org/abs/2605.03354"
pdf_url: "https://arxiv.org/pdf/2605.03354v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "电路分析"
  - "内部机制"
  - "可解释性"
  - "LLM Agent"
  - "规模扩展"
  - "Qwen"
  - "mem0"
  - "A-MEM"
relevance_score: 9.5
---

# What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis

## 原始摘要

Agent memory failures are silent: an LLM-based agent can produce a fluent response even when it fails to extract, retain, or retrieve the information needed across sessions. The write-manage-read loop describes the external pipeline of these systems but leaves open which internal computations implement each stage. Tracing internal feature circuits across the Qwen-3 family (0.6B--14B) and two memory frameworks (mem0 and A-MEM), we report three findings. First, control is detectable before content: routing circuitry is causally active at 0.6B, while content circuitry produces no detectable signal until 4B under our tracing setup, creating a deployment regime where small models route with apparent competence but silently fail at extraction and grounding. Second, within the content group, Write and Read share a late-layer hub that operates as a context-grounding substrate already present in the base model; only memory framing recruits a functional grounding direction on this substrate, and the hub transfers across both frameworks. Third, emergence does not imply steerability: although the content circuit becomes detectable at 4B, it becomes reliably steerable only at 8B, indicating that detection and intervention have distinct scale thresholds. As a practical implication, the feature-space separation between the two circuit groups enables per-operation failure localization at 76.2% accuracy without supervision, providing a stage-level diagnostic for otherwise silent agent-memory failures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决多轮交互场景下基于LLM的智能体记忆系统中的**无声失效**问题。研究背景是，现有智能体架构（如mem0、A-MEM）通过写-管理-读循环实现跨会话信息持久化，但每个阶段仅输出语法正确的令牌，导致提取错误、路由错误和接地错误在行为层面完全不可区分，最终只能用一个端到端准确率模糊地评估性能。

现有方法的主要不足体现在两方面：一是机械可解释性研究（如ReDeEP、ROME）局限于单次前向传递中的检索或事实关联，无法追踪横跨多次前向调用的全流水线故障；二是跨模型尺度的内部机制分析缺失，导致无法区分故障因容量限制消失还是结构性瓶颈固化。

本文要解决的核心问题是：**能否在神经网络内部为智能体记忆系统的写、管理、读三阶段找到可分离的内隐特征回路，并利用这些回路的可观测性实现无声故障的阶段级定位。** 为此，作者在Qwen-3家族（0.6B-14B）和两种记忆框架上进行了首次电路级跨尺度分析。研究发现，控制回路在0.6B即具备因果性而内容回路到4B才可检测，且检测到内容回路（4B）与成功干预它（8B）存在不同尺度阈值，最终基于特征空间分离实现了76.2%的无监督故障定位准确率。

### Q2: 有哪些相关研究？

以下是论文的相关研究，主要分为三类：

1. **Agent记忆系统研究**：相关工作统一了agent记忆的写-管理-读循环框架，涵盖显式LLM调用、分层分页、观察-反思-检索和强化学习策略、图存储等设计。实证研究显示增删操作影响长期行为，基准评测揭示了选择性遗忘、被动回忆与主动使用间的差距。本文在此基础上进一步揭示了内部计算实现，将外部流程映射到特征电路。

2. **电路分析与规模缩放研究**：使用transcoder进行电路追踪生成特征级归因图，自动电路发现提供互补的图搜索方法。最相关的是跨Qwen-3追踪规划电路，发现规模依赖的涌现和训练稳定性。本文扩展了该方向，发现控制电路在0.6B就活跃但内容电路直到4B才可检测，且检测与干预具有不同规模阈值。

3. **检索与事实记忆的机制可解释性研究**：ReDeEP和Retrieval Heads识别RAG幻觉和上下文检索机制，ROME和MEMIT定位事实关联于MLP。本文与这些单轮检索或静态知识研究不同，聚焦多轮写-管理-读循环，追踪记忆电路随规模的演化，并提出以76.2%准确率进行无监督操作级故障定位的诊断方法。

### Q3: 论文如何解决这个问题？

该研究提出了一套完整的电路分析方法，用于诊断LLM智能体记忆系统中的内部故障。整体框架基于一个三阶段流水线：Write（从对话中提取事实）、Manage（决定添加/更新/删除/无操作）和Read（基于检索记忆回答问题）。每个阶段都是独立的LLM前向推理过程，并配有特定阶段的提示词。

核心方法采用预训练线性转码器（PLTs）替代每个MLP层，形成稀疏编码器-解码器架构，产生单语义特征激活。通过冻结注意力模式和归一化项，在局部线性替代模型下精确计算加权因果边，从而构建输入嵌入、转码特征和输出logit节点之间的特征电路。

关键技术包括五步分析流程：属性归因（通过反向传播保留4096个特征节点）、交叉样本聚合（降维至50-200个循环特征）、路径追踪（贪心提取高权重边）、因果验证（零消融和5倍放大实验与随机基线比较，以因果差距为指标），以及雅卡尔相似度计算（衡量电路共享程度）。

研究创新点在于：1）在Qwen-3系列（0.6B-14B）和两种记忆框架（mem0和A-MEM）上统一应用此方法；2）发现控制电路在0.6B即可检测，内容电路需到4B才显现，形成"静默失败"窗口；3）揭示Write和Read共享一个晚期层级枢纽，该枢纽作为上下文基础子层已存在于基础模型中。最终，该方法的特征空间分离实现了76.2%准确率的无监督故障定位。

### Q4: 论文做了哪些实验？

论文通过五步分析流水线，在Qwen-3系列（0.6B、4B、8B、14B）和两个记忆框架（mem0和A-MEM）上，对记忆操作（Write、Manage、Read）进行了电路分析与干预实验。主要实验包括：

1. **因果验证实验**：在零消融电路特征或随机特征条件下，测量因果差距（causal gap）。结果表明，Manage电路在0.6B即产生显著因果信号（差距0.259，bootstrap CI排除零），而Write和Read电路直到4B才产生可检测信号。Write电路因果轨迹非单调：4B达到峰值，8B-14B逐渐下降；Read电路则从4B起单调递减。

2. **跨框架迁移实验**：在mem0和A-MEM上重复流水线。两者均呈现“控制先于内容”的不对称性（Manage在0.6B可检测，Write/Read在4B才可检测）。8B时，Read共享13/30个顶层特征，Write共享9.1%，而Manage重叠随规模下降至零。

3. **干预引导实验**：放大Write和Read电路特征（2×、3×、5×、10×倍数），测量事实召回率和问答准确率。8B是唯一在所有倍数下均获得一致提升的规模（5×时事实召回率达0.932，问答准确率0.598）。4B时5×倍导致事实召回率暴跌至0.218，而10×倍恢复至0.866。

4. **故障定位实验**：在8B模型上，通过消融各操作的特征库并检测输出最大扰动，实现无监督故障定位，准确率达76.2%，超越无训练基线（51.5%）24个百分点，超越有监督逻辑回归（63.4%）13个百分点。在LoCoMo和MemoryAgentBench上准确率分别达68.3%和72.5%。

### Q5: 有什么可以进一步探索的点？

论文揭示了模型内部记忆电路的控制与内容分离现象，但存在几个关键局限：首先，研究仅关注Qwen-3系列和两种记忆框架，缺乏跨架构（如GPT、Llama）和跨任务类型的验证，通用性存疑；其次，虽然定位了“写”和“读”共享的后期枢纽层，但未深入分析该枢纽层如何与具体记忆存储格式交互，以及不同提示工程为何无法突破基座模型预定义的“借用”方向；最后，诊断方法依赖特征空间分离，但76.2%的准确率仍有提升空间，且未验证在真实多步骤复杂任务（如多跳推理、长期对话）中的可靠性。

未来研究方向包括：探索不同基座模型家族中电路的跨模型迁移规律，设计更细粒度的干预手段（如针对枢纽层的动态方向调整），以及开发将电路诊断与自适应路由策略结合的纠错框架。关键改进在于，可尝试引入可学习的轻量级适配器来动态重定向枢纽层的功能方向，从而在较小模型上实现可控的内容提取。

### Q6: 总结一下论文的主要内容

本文研究了基于LLM的智能体记忆回路内部机制。问题定义：智能体记忆失败是隐性的，即使无法提取、保留或检索信息，也能生成流畅回复。方法：通过分析Qwen-3系列模型（0.6B-14B）和两种记忆框架（mem0和A-MEM）的内部特征回路，重点剖析“写-管理-读”循环中的内部计算。主要结论：第一，存在控制先于内容的非对称性——路由回路由0.6B模型即可检测，而内容回路直至4B才出现信号，导致小模型看似胜任却实际失败。第二，内容回路中，写和读共享一个后层枢纽，作为基础模型中已有的上下文锚定基板，仅记忆框架可在此基板招募功能方向，且该枢纽可在两框架间迁移。第三，涌现不等于可操控——内容回路虽在4B可检测，但直至8B才可靠可控，表明检测和干预存在不同规模阈值。核心贡献：特征空间分离可实现76.2%精度的无监督逐操作故障定位，为诊断隐性的智能体记忆故障提供阶段性诊断工具。意义：提升智能体记忆可靠性需利用基础模型的内部计算，为基于回路的监控和结构引导的记忆架构铺平道路。
