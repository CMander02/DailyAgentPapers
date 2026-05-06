---
title: "QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs"
authors:
  - "Pratik Honavar"
  - "Tejpratap GVSL"
date: "2026-05-05"
arxiv_id: "2605.03884"
arxiv_url: "https://arxiv.org/abs/2605.03884"
pdf_url: "https://arxiv.org/pdf/2605.03884v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "KV-cache 量化"
  - "多智能体系统"
  - "边缘设备"
  - "CacheCard"
  - "混合精度分配"
  - "LLM推理"
relevance_score: 8.5
---

# QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs

## 原始摘要

Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文针对边缘设备上多智能体LLM系统中的关键瓶颈——智能体间上下文传递的效率问题。当前实践中，接收智能体要么完全重计算共享上下文（re-prefill），消耗大量延迟；要么传输全精度KV缓存，占用过多显存。这限制了边缘设备上多智能体系统的部署。论文研究QKVShare框架，旨在通过量化的KV缓存（CacheCard）在智能体间高效传递，结合跨智能体感知的混合精度分配策略（基于Don't Waste Bits的扩展，加入下游需求信号和段特征），在避免重计算的同时压缩传输带宽，特别关注量化误差在多跳推理中的传播，以及缓存传输的端到端延迟（TTFT）和内存密度。核心目标是证明量化KV传递是一个实用方向，并量化当前原型中剩余的成本构成。

### Q2: 有哪些相关研究？

相关工作涵盖三大类。第一类是KV缓存量化：KIVI、KVQuant、ZipCache、Don't Waste Bits等方法针对单智能体场景减少显存，但未考虑跨智能体边界；第二类是多智能体KV缓存共享：KVCOMM解决偏移-方差问题实现跨前缀复用（70%+复用率）、C2C通过神经投影器实现异构模型间KV融合、LatentMAS实现无训练潜在协作、Q-KVComm提出自适应层粒度量化传输（5-6×压缩），但Q-KVComm是层粒度而非本文的token粒度，且未评估边缘部署或多跳推理；第三类是边缘LLM推理（MobiLoRA、Continuum、Agent Memory系统）和文本级智能体协议（Google的A2A、Anthropic的MCP）。QKVShare与Q-KVComm的不同在于：token级分配、使用Llama-3.1-8B中等规模、明确考虑跨智能体重要性信号，而非仅局部重建误差。

### Q3: 论文如何解决这个问题？

QKVShare设计了三个核心组件。1) 跨智能体感知token重要性评分：扩展Don't Waste Bits的四特征控制器（频率、质量分数、注意力方差、熵），增加下游需求信号（基于段级先验和注意力锚点重叠估计token对后续智能体的重要性）和段类型特征，形成6维特征向量，通过轻量2层MLP（512参数）输出{2,4,8,16}位宽分配，优化目标为最小化量化误差加权的期望，受限于给定内存预算。2) CacheCard压缩表示：自包含的量化KV组（自适应或均匀）、元数据（位宽向量、序列长度、模型ID、位置偏移占位符）和平均位宽统计，专为智能体间传递设计。3) 接收端注入路径：当前HuggingFace兼容原型先将CacheCard解量化为FP16的past_key_values再执行前向传播，代价是仅能测量当前原型延迟而无法加速注意力计算本身。实验采用混合运行时栈（PyTorch/HuggingFace用于自适应量化实验，llama.cpp用于基线共享和重计算延迟测量），评估顺序链拓扑（2-5跳GSM8K推理）。

### Q4: 论文做了哪些实验？

实验在12GB RTX 5070 Ti Laptop GPU上使用Llama-3.1-8B-Instruct，包含三个核心实验。E1（多跳推理准确性）：150个GSM8K问题，2-5跳顺序链，对比FP16共享、均匀Q4/Q8、自适应本地和QKVShare拓扑感知控制器，在约8位预算下拓扑感知控制器在5跳达到82.67%（均匀Q8为71.33%），但约4位结果混合，自适应未一致优于均匀。E2（控制器对照消融）：300个GSM8K问题配对比较显示拓扑感知对本地控制器净胜+2，与均匀Q4基本持平（-1），未确定性地证明拓扑优势。E3（延迟基准）：单次传递后TTFT测量，QKVShare均匀Q4路径在标称1K/4K/8K上下文中分别从完全重计算的150.2/565.3/1029.7 ms降至130.7/152.5/397.1 ms；阶段分解显示生成占主导（如8K中生成232.9 ms vs 卡片创建71.3 ms和注入92.8 ms），瓶颈在接收方前向传播而非CacheCard构造。论文承认混合运行时栈限制，未提供直接可比的全面消融。

### Q5: 有什么可以进一步探索的点？

论文自身指出几个明确未来方向：1) 最关键的实验是重新运行E2，在所有约4和约8位预算下进行大规模配对统计，直接验证拓扑感知分配是否优于本地或均匀分配；2) 开发原生融合量化跨智能体注意力核（如Q4→Q4核），以消除解量化和注入开销，使延迟测量更接近理论收益；3) 将实现迁移到统一运行时（如llama.cpp），实现更具可比性的端到端评估；4) 扩展到更复杂拓扑（层次化、异质管道）和更广泛任务（HotpotQA等），以及测量真实设备内存密度；5) 探索混合精度分配在更长上下文、更小模型和移动NPU场景下的泛化性；6) 研究位置编码对齐和跨前缀复用与量化传递结合的方法。

### Q6: 总结一下论文的主要内容

QKVShare提出并评估了面向边缘设备多智能体LLM系统的量化KV缓存传递框架，由三部分组成：跨智能体感知的token级混合精度位宽分配（扩展Don't Waste Bits控制器添加下游需求信号）、自包含的CacheCard压缩表示（量化KV组+元数据）、以及HuggingFace兼容的注入路径。主要实证结果为：避免重计算在延迟上获益显著（8K上下文TTFT从1029.7 ms下降到397.1 ms）；自适应分配在多跳中表现有前景，特别是约8位预算下5跳准确率82.67%（vs均匀71.33%）；但拓扑感知vs本地自适应优势尚未被消融确定。当前原型限制为混合运行时栈、均匀Q4延迟路径和解量注入。论文贡献在于一个可测量的原型，证明量化KV传递是实用方向，但暴露出剩余瓶颈（生成阶段主导延迟）和未闭合假设（拓扑特征的效果需进一步大规模验证）。
