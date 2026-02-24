---
title: "MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems"
authors:
  - "Jin Jia"
  - "Zhiling Deng"
  - "Zhuangbin Chen"
  - "Yingqi Wang"
  - "Zibin Zheng"
date: "2026-02-23"
arxiv_id: "2602.19843"
arxiv_url: "https://arxiv.org/abs/2602.19843"
pdf_url: "https://arxiv.org/pdf/2602.19843v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "可靠性评估"
  - "故障注入"
  - "系统鲁棒性"
  - "Agent评测"
relevance_score: 8.0
---

# MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems

## 原始摘要

As LLM-based Multi-Agent Systems (MAS) are increasingly deployed for complex tasks, ensuring their reliability has become a pressing challenge. Since MAS coordinate through unstructured natural language rather than rigid protocols, they are prone to semantic failures (e.g., hallucinations, misinterpreted instructions, and reasoning drift) that propagate silently without raising runtime exceptions. Prevailing evaluation approaches, which measure only end-to-end task success, offer limited insight into how these failures arise or how effectively agents recover from them. To bridge this gap, we propose MAS-FIRE, a systematic framework for fault injection and reliability evaluation of MAS. We define a taxonomy of 15 fault types covering intra-agent cognitive errors and inter-agent coordination failures, and inject them via three non-invasive mechanisms: prompt modification, response rewriting, and message routing manipulation. Applying MAS-FIRE to three representative MAS architectures, we uncover a rich set of fault-tolerant behaviors that we organize into four tiers: mechanism, rule, prompt, and reasoning. This tiered view enables fine-grained diagnosis of where and why systems succeed or fail. Our findings reveal that stronger foundation models do not uniformly improve robustness. We further show that architectural topology plays an equally decisive role, with iterative, closed-loop designs neutralizing over 40% of faults that cause catastrophic collapse in linear workflows. MAS-FIRE provides the process-level observability and actionable guidance needed to systematically improve multi-agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体系统（MAS）在可靠性评估上面临的核心挑战。当前，这类系统通过非结构化的自然语言进行协作，容易产生“软性”的语义故障（如幻觉、指令误解、推理漂移），这些故障会无声传播，而不会引发运行时异常。现有的评估方法主要依赖端到端的任务成功率等黑箱式指标，无法深入揭示故障是如何产生、系统如何从中恢复的，导致提升系统鲁棒性只能依赖试错。为此，论文提出了MAS-FIRE框架，通过系统性的故障注入和细粒度评估，来诊断多智能体系统的脆弱性并理解其容错行为。该框架定义了涵盖智能体内部认知错误与智能体间协调故障的15种故障类型，并设计了非侵入式的注入机制，从而为系统设计者提供过程级的可观测性和改进系统可靠性的具体指导。

### Q2: 有哪些相关研究？

本文的研究背景与多个领域的工作密切相关。首先，在**LLM驱动的多智能体系统（MAS）**方面，相关工作包括MetaGPT、ChatDev、AutoGen、CAMEL等，它们探索了不同的多智能体架构（如顺序流水线、层次结构、协作网络），以实现复杂任务分解与协作。本文将这些系统视为一种新型“智能软件”，并强调其依赖自然语言进行协调的特性，这区别于传统基于固定协议（如gRPC）的分布式系统。

其次，在**故障注入（Fault Injection）与可靠性评估**领域，已有研究将FI应用于硬件、软件（如微服务）等层面，以测试系统容错性。然而，传统FI方法主要针对语法或结构故障（如代码突变、数据损坏），而MAS的故障常表现为“静默”的语义错误（如幻觉、指令误解）。本文指出，直接套用现有方法不足以评估MAS的可靠性，因为其故障本质是认知与协作层面的语义偏差。

因此，本文提出的MAS-FIRE框架，旨在填补这一空白：它**系统化地扩展了故障注入的概念**，将其适配到MAS的语义交互环境中。通过定义涵盖智能体内部认知错误与智能体间协调失败的故障分类，并采用非侵入式机制（如提示修改、响应重写）进行注入，本文为多智能体系统的可靠性评估提供了更精细、更贴近其运行本质的方法论。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MAS-FIRE的系统性框架来解决多智能体系统（MAS）的可靠性评估问题。其核心方法包括三个关键部分：建立故障分类法、设计非侵入式故障注入机制，以及定义细粒度的鲁棒性度量标准。

首先，框架定义了一个包含15种具体故障类型的分类法，将其划分为**智能体内故障**和**智能体间故障**两大类。智能体内故障涵盖规划、记忆、推理和行动四个子类，反映了单个智能体的认知错误。智能体间故障则包括配置、指令和通信三个子类，捕捉了智能体间协调与信息流中的问题。这一分类为系统性评估奠定了基础。

其次，框架设计了三种非侵入式的故障注入机制来模拟这些故障：
1.  **提示词修改**：通过修改系统提示词（定义智能体角色）或用户提示词（定义任务），注入配置故障（如角色模糊、盲目信任）和指令故障（如逻辑冲突、语义模糊）。
2.  **拦截与响应重写**：在运行时拦截智能体的输出（如规划、推理结果、工具调用请求），并通过**语义级突变**（使用LLM指导，注入规划错误、幻觉、工具选择错误等）或**结构级突变**（直接算法修改，注入记忆丢失、参数格式错误等）来重写响应，从而注入智能体内故障。
3.  **消息路由操纵**：通过编程方式操纵消息的流向和频率，而不改变其内容，注入通信故障（如消息循环、消息风暴、广播放大）。

这些机制允许在不对系统进行深度修改的情况下，在关键交互边界（提示词、输出、消息流）注入可控且具代表性的故障，以观察系统的反应。

最后，为了超越简单的端到端任务成功率评估，论文定义了双层的鲁棒性度量框架，不仅衡量系统级的整体任务恢复能力，还评估机制级的故障检测、本地恢复和全局恢复等具体容错行为的有效性。通过将观察到的容错行为归纳为机制、规则、提示词和推理四个层级，MAS-FIRE能够对系统在何处、为何成功或失败进行细粒度的诊断，从而为系统改进提供可操作的指导。

### Q4: 论文做了哪些实验？

论文实验设置包括：选取三种代表性的多智能体系统（MetaGPT、Table-Critic、Camel），分别对应代码生成、表格问答和网络导航任务，并使用HumanEval、WikiTableQuestions和WebShop作为基准数据集。实验注入15种故障类型，覆盖智能体内部认知错误和智能体间协调故障，通过提示修改、响应重写和消息路由操纵三种机制实现。评估使用GPT-5和DeepSeek-V3作为基础模型对比，并采用鲁棒性分数（RS_f）量化系统在故障下的表现。

主要结果揭示：不同故障类型对系统影响差异显著。智能体内部故障中，内存故障在具有共享消息池的MetaGPT中影响较小（RS_f > 90%），而在线性结构的Camel中严重（RS_f ≈ 67%）；规划故障在迭代式设计的Table-Critic中通过自我修正保持高鲁棒性（RS_f > 89%），但在顺序执行的MetaGPT中大幅降低（RS_f可低至43.84%）。智能体间故障如配置和指令故障可能导致系统崩溃（MetaGPT的RS_f可降至0%），但迭代闭环架构能提供部分韧性。基础模型能力的影响具有双重性：GPT-5在语义相关故障（如幻觉）上表现优于DeepSeek-V3（ΔRS可达+22.05%），但在某些场景下严格遵循指令反而阻碍恢复。此外，基础设施级防御对通信故障非常有效（RS_f > 93%）。

### Q5: 有什么可以进一步探索的点？

本文提出的MAS-FIRE框架为多智能体系统的可靠性评估开辟了新路径，但其局限性与未来方向值得深入探讨。主要局限在于：1）故障注入机制仍依赖于外部干预（如改写提示或响应），未能完全模拟智能体内部自主产生的原生语义错误；2）评估主要关注静态的故障恢复能力，缺乏对系统在持续运行中性能退化或自适应学习能力的动态观测；3）故障分类学（15种类型）可能尚未覆盖所有复杂的、涌现性的协调失败场景。

未来可探索的方向包括：开发更内生的故障注入方法，例如通过扰动智能体的内部记忆或工具调用逻辑来诱发错误；将评估从单次故障恢复扩展到长期运行的韧性与演化能力分析；研究不同通信拓扑（如去中心化网络）与动态重组机制对容错性的影响；以及探索如何利用评估中发现的“容错层级”知识，主动设计具有自监测与自修复架构的智能体系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了MAS-FIRE框架，专门用于评估基于大语言模型的多智能体系统的可靠性。其核心贡献在于首次系统性地定义了多智能体系统中可能发生的15种故障类型（涵盖智能体内部认知错误和智能体间协调故障），并设计了三种非侵入式的故障注入方法（提示修改、响应重写和消息路由操控）来模拟这些故障。通过将该框架应用于三种典型的多智能体架构，研究发现系统的容错行为可分为机制、规则、提示和推理四个层级，这为细粒度诊断系统成败原因提供了新视角。论文的重要发现是：更强的基座模型并不能均匀提升系统鲁棒性，而系统架构拓扑（如迭代闭环设计）对可靠性的影响同样关键，甚至能化解超过40%会导致线性工作流崩溃的故障。MAS-FIRE的意义在于为理解和提升多智能体系统的可靠性提供了可操作的过程级观测工具与指导。
