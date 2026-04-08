---
title: "Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning"
authors:
  - "Qisheng Su"
  - "Shiting Huang"
  - "Zhen Fang"
  - "Ziyan Chen"
  - "Zehui Chen"
  - "Feng Zhao"
date: "2026-04-07"
arxiv_id: "2604.05404"
arxiv_url: "https://arxiv.org/abs/2604.05404"
pdf_url: "https://arxiv.org/pdf/2604.05404v1"
github_url: "https://github.com/sqs-ustc/tool-reasoning-framework-PTE"
categories:
  - "cs.PF"
  - "cs.SE"
tags:
  - "Tool-Integrated Reasoning"
  - "Efficiency Metrics"
  - "KV-Cache"
  - "Inference Latency"
  - "Benchmarking"
  - "Hardware-Aware"
relevance_score: 7.5
---

# Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning

## 原始摘要

In real-world Tool-Integrated Reasoning (TIR) scenarios, where LLMs interleave reasoning with external tool calls, a major source of inefficiency is that the toolcalls create pauses between LLM requests and cause KV-Cache eviction, forcing recomputation. Also, the long, unfiltered response returned by external tools inflates the KV-Cache, so each decode step spends more time loading the growing cache and thus becomes steadily slower as context length increases. However, existing efficiency metrics like token counts and toolcall counts fail to capture the real model inference latency. To address this, we introduce PTE (Prefill Token Equivalents), a hardware-aware TIR-efficiency metric that unifies internal reasoning and external tool-use costs while explicitly accounting for non-reusable KV-Cache and long-tool-response scenarios. Validation in a high-concurrency industrial setting indicates that PTE aligns significantly better with wall-clock latency than standard token counts, while maintaining consistent efficiency rankings across diverse hardware profiles. We conduct extensive experiments across five TIR benchmarks, quantify their PTE costs, and identify four inefficiency patterns that appear in TIR. We also discover that trajectories with higher PTE costs tend to have lower reasoning correctness, indicating that simply using more tools does not improve the quality of the answer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工具集成推理（TIR）场景中现有效率评估方法的不足。研究背景是，大型语言模型（LLMs）通过调用外部工具（如搜索引擎、计算器）来增强复杂任务处理能力，但在实际部署中，工具调用会导致LLM推理过程暂停，引发KV-Cache（键值缓存）被驱逐，迫使模型在后续步骤中重新计算；同时，外部工具返回的长且未经筛选的响应会急剧膨胀上下文长度，使得解码阶段因需要加载不断增大的缓存而变得越来越慢。然而，现有评估方法主要关注准确性，效率指标则依赖于简单的令牌计数或工具调用次数，这些指标无法捕捉模型推理的真实延迟，因为它们忽略了计算密集型的前填充阶段与内存密集型的解码阶段之间的成本不对称性，也未能统一衡量内部推理与外部工具使用的真实开销。

因此，本文的核心问题是：如何建立一个能够准确反映TIR场景中真实硬件开销的效率评估框架。为此，论文提出了PTE（预填充令牌等价量）这一硬件感知的度量标准，它通过将内存受限的解码成本折算为计算受限的前填充令牌单位，从而在统一内部推理和外部工具使用成本的同时，显式地考虑了KV-Cache不可重用和长工具响应等关键因素。最终，研究不仅提供了更贴近实际延迟的评估工具，还通过大量实验量化了TIR成本，识别出四种低效模式，并揭示了PTE成本与推理正确性之间的负相关关系。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：工具增强LLM的评测基准和工具集成推理的效率优化研究。

在**评测基准**方面，早期工作如BFCL、Webshop、ToolBench和T-Eval侧重于API选择和计划分解，主要衡量任务成功率。后续的API-Bank和Critic-Tool引入了基于执行的指标（如API成功率）。近期，TIR基准已扩展到复杂多步骤任务，涵盖网页浏览（如BrowseComp、WideSearch、GAIA）和数学与代码等特定领域推理（如GSM8K、MATH500、SWE-Bench）。尽管这些工作以准确率为主要指标，但效率常被忽视或仅用简单指标（如令牌数、步骤数）衡量，如MCP-RADAR、ToolQA和CLASSIC。近期研究尝试引入成本意识，但缺乏基于Transformer推理物理延迟的统一框架。**本文提出的PTE指标正是为了弥补这一空白，提供了一个硬件感知的统一效率度量，直接关联实际推理延迟。**

在**效率优化**方面，研究已识别出TIR中的低效行为（如“认知卸载”和“过度使用工具”）。主流缓解方法是采用强化学习，其研究可分为奖励工程和算法创新。奖励工程包括：间接优化（通过监督推理质量来隐式提升效率）和直接优化（明确加入成本惩罚）。然而，当前惩罚依赖于工具调用次数或令牌数等简单指标，未能捕捉硬件级延迟。算法创新则旨在优化推理过程本身，例如基于熵的探索策略、推理与工具使用的动态路由以及基于梯度的停止标准以剪枝冗余步骤。**本文与这些工作的核心区别在于，它首先系统性地定义和验证了一个能准确反映实际延迟的效率度量（PTE），并基于此量化了TIR中的四种低效模式，为后续优化提供了更精确的评估基础。**

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PTE（Prefill Token Equivalents）的新型硬件感知效率度量标准来解决工具集成推理（TIR）场景中的低效问题。该问题的核心在于，传统的效率指标（如令牌数和工具调用次数）无法准确反映模型推理的真实延迟，尤其是在外部工具调用导致KV-Cache失效和膨胀的情况下。

**核心方法与架构设计**：
PTE的整体框架基于对LLM推理两个阶段的成本建模：计算受限的Prefill（预填充）阶段和内存受限的Decode（解码）阶段。其核心思想是将这两种不同瓶颈的成本统一到一个具有物理意义的单位中，即处理一个输入（预填充）令牌的等效成本。

**主要模块/组件与关键技术**：
1.  **成本统一公式**：PTE的总成本计算公式为 \( PTE = \sum_{i=1}^{k} (D_{prefill_i} + \gamma \cdot L_{seq_i} \cdot D_{decode_i}) \)。其中：
    *   \( D_{prefill_i} \) 代表第i轮对话中累积的上下文令牌数，用于计算Prefill阶段的成本。
    *   \( D_{decode_i} \) 代表第i轮中模型生成的令牌数。
    *   \( L_{seq_i} \) 代表第i轮解码开始前的累积序列长度（总上下文）。
    *   \( \gamma \) 是一个关键的无量纲系数，表示内存受限操作相对于计算受限操作的相对成本。

2.  **γ系数的计算与建模**：
    *   **Prefill成本建模**：近似为与模型参数量 \( N_{params} \) 成正比，即 \( C_{prefill} \approx 2 \cdot N_{params} \) FLOPs。
    *   **Decode成本建模**：解码阶段的瓶颈在于加载KV-Cache所需的内存带宽。其等效计算成本通过KV-Cache的内存访问量 \( S_{KV} \) 乘以**硬件操作强度（HOI）** 来转换，即 \( C_{decode}^{eq} = S_{KV} \cdot HOI \) FLOPs。
    *   **γ的定义**：\( \gamma = C_{decode}^{eq} / C_{prefill} \)。它本质上是解码阶段等效计算成本与预填充阶段成本的比值。
    *   **架构优化适配**：公式针对现代注意力机制进行了细化，例如对于分组查询注意力（GQA），通过KV头与查询头的比例（\( H_{kv}/H_q \)）对γ进行缩放；对于多头潜在注意力（MLA），则使用压缩维度（\( d_{latent} + d_{rope} \)）替代隐藏维度 \( d_{model} \)。这使得γ成为一个静态的模型-硬件对属性。

**创新点**：
1.  **硬件感知的统一度量**：PTE首次明确地将计算成本（Prefill）和内存带宽成本（Decode，特别是受KV-Cache大小影响的部分）统一到一个指标中，能够更真实地反映TIR场景下的推理延迟。
2.  **显式建模KV-Cache影响**：通过引入累积序列长度 \( L_{seq_i} \) 作为乘数，PTE公式直接捕捉了KV-Cache随上下文增长而导致的解码速度下降问题，以及工具调用暂停可能引发的KV-Cache失效（需重新计算）所带来的额外开销。
3.  **引入γ系数**：γ系数是该方法的技术核心，它量化了特定模型在特定硬件上内存访问相对于计算的“昂贵”程度，使PTE能够跨不同模型和硬件配置进行一致的效率排名。
4.  **揭示效率模式**：基于PTE对多个TIR基准进行量化分析，论文不仅提供了更准确的效率评估，还进一步识别出了TIR中存在的四种低效模式，并发现了高PTE成本与低推理正确性之间的相关性，超越了单纯的工具使用数量分析。

### Q4: 论文做了哪些实验？

论文在五个TIR基准测试上进行了广泛的实验，以评估其提出的PTE效率指标并识别TIR中的低效模式。

**实验设置**：实验在一个统一的TIR框架中进行，使用vLLM推理引擎。所有模型使用相同的系统提示词和工具定义，以确保公平比较。框架集成了三种工具：使用Serper API的搜索工具、使用Jina API的网页访问工具，以及一个开源Python沙箱实现的Python工具。框架会记录每个推理步骤的预填充令牌数、解码令牌数和累积序列长度，用于计算PTE。

**数据集/基准测试**：使用了五个针对不同TIR能力的基准测试：
1.  **数学推理**：MATH500（数学问题）和AIME 2024/2025（高难度竞赛问题）的完整测试集，代理配备Python工具。
2.  **信息寻求**：从SimpleQA（需要特定事实检索的事实问答）和WebInstruct-Verified（需要检索和计算的复杂多学科任务）中各随机抽取500个示例。前者使用搜索和访问工具，后者额外添加Python工具。

**对比方法与主要结果**：研究评估了多个具备工具调用能力的开源模型（如Llama-3.1系列、Qwen-2.5系列、Qwen3、Deepseek-V3.1-Terminus等），并分析了它们在效率（PTE）与准确性之间的权衡。主要发现包括：
1.  **巨大的成本差异**：在准确性相近的情况下（例如AIME24上约70%），不同模型的PTE值可能相差一个数量级以上。
2.  **任务特定的TIR能力**：模型的TIR能力高度依赖于任务和工具类型。例如，Qwen2.5-72B在Web任务（SimpleQA）上表现出色，但在Python推理任务（MATH500 & AIME）上表现不佳。
3.  **不同的TIR行为模式**：研究识别了五种模型行为模式，并基于PTE分析揭示了四种低效模式：
    *   **确认性工具使用**：模型倾向于在第一步进行大量内部推理（“首步效应”），延迟工具调用，导致后续步骤因上下文增长和KV-Cache问题而成本激增。
    *   **工具混合**：DeepSeek-V3.1-Terminus能灵活混合使用不同工具集，但产生了显著更高的PTE成本，且未带来明显的准确性提升。
    *   **缺乏工具先验**：某些模型（如Qwen-2.5系列在数学任务中）启用Python工具后准确性下降且PTE成本升高，可能源于预训练中对特定工具使用的暴露有限。
    *   **工具格式崩溃**：某些模型（如Tongyi-Deepresearch）对工具调用格式的微小非语义变化极其敏感，导致调用失败，产生极高的PTE和极低的准确性。

**关键数据指标**：核心效率指标是**PTE（预填充令牌等价物）**，它比标准令牌计数更能反映实际推理延迟。例如，在AIME25任务上，启用思考模式的Qwen3-235B-Thinking模型以**1.8倍的PTE成本**换取了**+16.7%的准确性提升**；而在简单的SimpleQA任务上，同一模型的准确性**下降3.4%**，PTE却增长了**4.2倍**，显示出过度思考的低效性。

### Q5: 有什么可以进一步探索的点？

本文提出的PTE指标主要关注模型推理的计算成本，未能涵盖API调用延迟等真实世界开销，这限制了其在端到端延迟评估中的全面性。未来研究可将网络延迟、工具响应时间等外部因素纳入效率模型，构建更完整的评估体系。此外，论文发现低PTE与高质量推理存在关联，但这一结论仅在特定任务和模型上验证，需在更广泛的领域（如多模态工具调用、长序列规划）及不同架构（如MoE模型）中进行深入探究。从方法改进角度，可探索动态调整γ参数以更精细地反映硬件特性，或开发轻量级缓存管理策略来缓解长工具响应导致的KV-Cache膨胀问题。最后，将PTE与错误传播分析结合，研究低效工具使用如何影响推理链的稳健性，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

本文针对工具集成推理场景中现有效率指标（如token数和工具调用次数）无法准确反映实际推理延迟的问题，提出了PTE这一硬件感知的效率度量标准。PTE通过建模预填充和解码阶段的不对称性，统一了内部推理和外部工具使用的成本，并显式考虑了不可重用的KV缓存和长工具响应场景。实验验证表明，PTE与真实延迟的相关性显著优于传统token计数，且在不同硬件配置下保持一致的效率排名。研究在五个TIR基准测试中量化了PTE成本，识别出四种常见的低效模式，并发现PTE成本较高的推理轨迹往往正确率较低，这表明单纯增加工具使用并不能提升答案质量。该工作为TIR效率评估提供了统一视角，对未来研究具有重要指导意义。
