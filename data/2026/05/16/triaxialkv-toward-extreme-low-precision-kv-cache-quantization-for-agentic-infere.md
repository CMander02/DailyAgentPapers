---
title: "TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks"
authors:
  - "Hanzhang Shen"
  - "Haoran Wu"
  - "Yiren Zhao"
  - "Robert Mullins"
date: "2026-05-16"
arxiv_id: "2605.17170"
arxiv_url: "https://arxiv.org/abs/2605.17170"
pdf_url: "https://arxiv.org/pdf/2605.17170v1"
categories:
  - "cs.LG"
tags:
  - "KV-cache量化"
  - "混合精度量化"
  - "Agent推理效率"
  - "长上下文"
  - "多模态Agent"
  - "Computer Use Agent"
  - "系统优化"
relevance_score: 8.5
---

# TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks

## 原始摘要

Agentic workloads have emerged as a major workload for LLM inference. They differ significantly from chat-only workloads, requiring long-context processing, the ability to handle multimodal inputs, and structured multi-turn interactions with tool calling capabilities. As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning. These axes capture distinct token behaviors and lead to different sensitivities to KV-cache compression. However, existing KV-cache quantization methods are typically homogeneous or exploit only heterogeneity on a single dimension, such as temporal proximity or modality, overlooking the interactions among them. To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. We implement TriAxialKV as an end-to-end serving system, comprising calibration, mixed-precision quantization and memory management, and custom fused Triton decode kernels. When using Qwen3-VL-32B-Thinking as a computer-use agent operating the OSWorld, TriAxialKV matches the accuracy of SGLang with BF16 KV cache while supporting 4.5$\times$ KV cache size and achieving 30% higher end-to-end throughput, when running on real GPU systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在AI智能体推理任务中，大语言模型的长上下文处理对KV缓存造成的巨大内存瓶颈问题。随着LLM从单轮对话向智能体工作负载（如网页搜索、计算机操作、代码生成等）演进，模型需要处理包含多模态输入、工具调用和结构化多轮交互的极长上下文，这导致KV缓存迅速增长，成为推理过程中的主要内存瓶颈。现有KV缓存压缩方法存在明显不足：它们要么对KV缓存采用同质的压缩策略，要么仅考虑单一维度的异质性（如时间近因或模态），忽视了智能体上下文中沿三个关键轴——时间近因（与当前轮的接近程度）、模态（文本或图像令牌）和语义角色（用户查询、工具调用、观察结果或推理）——的显著结构差异。这些单轴方法将压缩敏感度截然不同的令牌分配到相同位宽，导致在激进压缩下精度严重下降。因此，本文核心要解决的是：如何联合建模时间、模态和语义三维结构，为每个令牌分配最优的混合精度位宽，在固定内存预算下实现极端低精度的KV缓存量化，从而在保持精度的同时大幅提升推理吞吐量。

### Q2: 有哪些相关研究？

以下是该论文的相关研究工作，主要分为两类：KV缓存压缩方法和高效LLM服务系统。

在KV缓存压缩方法类，本文与KIVI、KVQuant、ZipCache、QServe等全精度或混合精度方法不同，这些方法通常采用同质化量化或仅依赖单一维度的异质性（如时间邻近性、通道轴）。TriAxialKV创新性地引入三轴标签，联合考虑时间新近性、模态（文本/图像）和语义角色（用户查询、工具调用、推理），实现多维度混合精度分配。与PM-KVQ、ThinKV、ChanMix、SmallKV等工作相比，这些方法仅沿单一结构轴（如层间、推理/非推理、通道或辅助模型）进行混合精度分配，忽略了多轴间的交互，而TriAxialKV通过校准每标签敏感度，在固定内存预算下分配INT2/INT4位宽，实现了更精细的压缩。

在高效LLM服务系统类，本文借鉴了Orca的迭代级调度、Sarathi-Serve的分块预填充、FlashAttention的显存优化、vLLM的PagedAttention以及SGLang的前缀共享等思想。与这些系统不同，TriAxialKV作为端到端服务系统，不仅集成校准、混合精度量化和内存管理，还定制了融合Triton解码内核，特别针对智能体推理任务的长上下文、多模态和结构化多轮交互场景优化，从而在OSWorld等实际任务上匹配BF16精度并大幅提升吞吐量。

### Q3: 论文如何解决这个问题？

TriAxialKV提出了一种混合精度KV缓存量化方案，通过三轴标签系统实现细粒度比特分配。核心方法包括离线校准和在线服务两个阶段。整体框架将Agent工作负载的令牌按三个正交轴标记：时间轴（older/turn_m2/turn_m1/current）、模态轴（text/image）和语义轴（inst/user/assistant/reasoning/tool_call/obs/delim），形成联合标签空间。离线校准阶段首先捕获KV痕迹，然后通过敏感度分析量化每个标签在INT2和INT4下的注意力输出MSE，得到每个标签的失真表Dk(b)。在线服务阶段根据平均比特预算B，通过贪心算法或穷举搜索（标签空间≤22时）求解优化问题，为每个标签分配比特宽度。

关键技术包括：1) 采用不对称组量化（组大小G=32），INT2键按通道量化以处理异常值，INT4和INT2值按令牌量化；2) 双池内存架构共享虚拟地址空间，通过偏移量区分INT2和INT4池，每个池有独立页分配器；3) 自定义Triton融合解码核，支持两种精度的即时反量化；4) 处理残差令牌时使用INT4路径而非全精度，避免内存碎片。创新点在于首次联合考虑时间、模态和语义三个维度的异质性敏感度，实现比单一维度更好的压缩效率。

### Q4: 论文做了哪些实验？

论文在BFCL Memory（文本函数调用）和OSWorld（多模态计算机使用）两个智能体基准上评估了TriAxialKV。实验使用Qwen3系列（14B、32B、235B-A22B）、Falcon3-10B及多模态模型Qwen3-VL（8B/32B-Thinking）、InternVL3.5-38B。对比方法包括SGLang BF16（无损基线）、SGLang FP4（统一低比特浮点量化）和KIVI（非对称2-bit量化）。主要结果：在BFCL上，TriAxialKV混合精度在所有模型上的准确率距离BF16基线保持在1.1%以内（如Qwen3-14B：24.22% vs 25.11%）；在OSWorld上，混合精度准确率与BF16相当甚至略高（如Qwen3-VL-32B-Thinking：40.59% vs 39.20%）。端到端吞吐量测试中，在H100 GPU上运行OSWorld轨迹时，TriAxialKV相比SGLang BF16实现了1.52倍吞吐量提升（Qwen3-VL-32B），并在同等内存预算下支持3.4-4.0倍的并发请求数。消融实验表明，语义轴和三轴标记设计对准确率影响最大：移除语义轴导致Qwen3-14B上准确率下降6.22个百分点，而移除时间轴仅下降2.22个百分点。

### Q5: 有什么可以进一步探索的点？

TriAxialKV的局限性在于其标签系统仅依赖简单的对话模板规则，无法动态捕捉任务中语义角色的微妙变化（如推理链中的中间结论与最终结论）；同时，INT2/INT4的静态分配策略未考虑token在不同解码阶段重要性会动态演变。未来可探索：1）引入在线学习机制，基于解码反馈实时微调每个token的位宽分配，减少校准阶段的失真估计误差；2）将三轴标签扩展至更细粒度的语义维度（如函数调用参数、图像中的物体边界框），利用注意力头对特定语义的偏好实现自适应压缩；3）结合稀疏化技术（如Top-k淘汰）与量化，在极端压缩比下优先保留对当前生成步最关键的token。此外，当前仅测试单Agent场景，可推广至多Agent协作推理，利用跨Agent的上下文复用模式进一步优化缓存效率。

### Q6: 总结一下论文的主要内容

TriAxialKV旨在解决现有KV缓存量化方法对智能体推理任务中上下文结构复杂性考虑不足的问题，这类任务具有长上下文、多模态输入和结构化多轮交互的特点。论文提出一种混合精度KV缓存量化方案，通过为每个令牌分配包含时间近因、模态（文本/图像）和语义角色（用户查询、工具调用等）的三轴标签，并校准每个标签的灵敏度，在固定内存预算下分配INT2/INT4位宽。该方法实现为端到端服务系统，包含校准、混合精度量化和内存管理，并使用定制的融合Triton解码内核。在OSWorld等基准测试上，使用Qwen3-VL-32B-Thinking模型时，TriAxialKV在保持与BF16 KV缓存同等精度的同时，支持4.5倍KV缓存容量，并在真实GPU系统上实现比SGLang高30%的端到端吞吐量。这项工作的核心意义在于证明了联合考虑时间、模态和语义结构对于实现激进的KV缓存压缩既必要又实用。
