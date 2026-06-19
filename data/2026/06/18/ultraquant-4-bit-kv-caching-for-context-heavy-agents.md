---
title: "UltraQuant: 4-bit KV Caching for Context-Heavy Agents"
authors:
  - "Inesh Chakrabarti"
  - "David Limpus"
  - "Aditi Ghai Rana"
  - "Bowen Bao"
  - "Spandan Tiwari"
  - "Thiago Crepaldi"
  - "Ashish Sirasao"
date: "2026-06-18"
arxiv_id: "2606.20474"
arxiv_url: "https://arxiv.org/abs/2606.20474"
pdf_url: "https://arxiv.org/pdf/2606.20474v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.PF"
tags:
  - "LLM Agent"
  - "KV-Cache压缩"
  - "4-bit量化"
  - "服务优化"
  - "上下文重型Agent"
  - "多轮Agent工作负载"
  - "AMD GPU优化"
relevance_score: 8.5
---

# UltraQuant: 4-bit KV Caching for Context-Heavy Agents

## 原始摘要

Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized. We study 4-bit KV-cache compression for this setting, using TurboQuant-style rotation and codebook quantization as a quality anchor and vLLM FP8 KV caching as the deployment anchor. We report three contributions. First, we frame 4-bit KV caching around multi-round agent workloads where task quality, cache residency, and serving throughput must be measured jointly. Second, we describe the practical design choices needed to make the 4-bit path robust, including asymmetric K/V treatment, Walsh-Hadamard rotation, QJL removal, and block-scale variants. Third, we present serving optimizations on AMD GPUs, including optimized decode-attention kernels and UltraQuant, an FP4 approximation path that uses FP8 queries, FP4 KV tensors, UE8M0 group scales, and native scaled-MFMA support on CDNA4. On a long-context, multi-turn agentic workload, UltraQuant cuts P50 time-to-first-token by 3.47x in the cache-pressured late rounds (2.3x across all rounds) and raises output throughput by 1.63x over the FP8 KV baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

随着大型语言模型从短上下文聊天机器人演变为需要长期记忆的智能体，系统指令、工具定义、检索文档和代码库上下文等长前缀被跨多次短轮次复用，这给KV缓存带来了巨大压力。现有方法存在明显不足：FP8 KV缓存是vLLM中的强部署基线，虽有约2倍压缩和硬件原生支持，但在长上下文、多轮智能体工作负载下仍显不足；TurboQuant等4位标量加旋转方法虽提供了高质量精度，但依赖码本查找和软件反量化，导致内核效率低下。同时，并发性决定了服务系统能否保持GPU利用率，而现有研究缺乏对上下文密集型智能体工作负载下KV缓存压缩的联合评估框架。因此，本文旨在解决4位KV缓存压缩在上下文密集型智能体场景中的部署问题，核心目标是实现压缩质量、缓存驻留和服务吞吐量的联合优化。具体而言，需要解决三个关键挑战：哪些量化方式能在长上下文任务中保持质量；这些量化选择如何与解码注意力内核交互；以及服务系统何时能从增加的驻留上下文中获益。通过提出UltraQuant方法，利用FP4微张量近似将反量化折叠到原生CDNA4缩放MFMA指令中，在保持质量的同时显著提升吞吐量。

### Q2: 有哪些相关研究？

相关研究主要分为方法类和应用类。在方法类中，KIVI和KVQuant最早提出键值非对称量化，因为键和值的误差对softmax分布影响不同，本文继承了该思路并进一步优化了不对称处理。QJL和TurboQuant采用旋转和码本量化方法实现低位宽下的率失真优化，尤其是TurboQuant的旋转操作能分散异常值能量，使标量量化器面对更接近高斯分布的系数，本文以其为质量锚点，但指出其码本的查找和不规则访问成本不适合高效部署。TurboQuant式旋转结合逐模型Lloyd-Max或逐块变体LMPB校准的质心构成强力4位码本，本文将其作为背景和动机，转而使用硬件原生FP4网格替代任意质心。在应用类中，vLLM风格的分页服务将KV缓存驻留提升为系统级问题，本文采用类似视角但扩展至4位量化场景。与使用FP8直接矩阵核心支持的硬件原生格式不同，本文针对CDNA4的缩放F8F6F4 MFMA路径设计，使FP4操作数和UE8M0缩放因子直接由矩阵核心处理，实现了更高效的服务吞吐优化。

### Q3: 论文如何解决这个问题？

论文通过提出UltraQuant来解决上下文密集型智能体场景下的4-bit KV缓存压缩问题。核心方法基于TurboQuant的旋转和码本量化框架，但进行了多项关键改进。整体框架包含三个主要创新：

首先，在编码器设计上，UltraQuant采用了非对称的K/V处理，对键和值分别使用Walsh-Hadamard旋转来分散异常值能量，使坐标分布接近高斯分布，便于4-bit量化。同时移除了QJL处理，并引入块级缩放变体来提升量化精度。

其次，UltraQuant提出了基于FP4 E2M1格式的硬件原生KV缓存。它将头维度划分为32通道的组，每组使用32个FP4编码（每字节2个码）加上1个UE8M0缩放因子，实现4.25 bits/元素的存储效率。关键在于优化单个全局常数c（实验中为0.156），通过离线校准使FP4网格与旋转后的数据分布匹配，避免了运行时查表开销。

最后，在AMD GPU上实现了优化的解码注意力核。通过使用FP8查询和FP4键值张量，并利用CDNA4架构的原生scaled-MFMA支持，将反量化操作简化为一条指数移位指令。这种设计消除了软件gather操作，使键值无需转换为BF16格式，显著减少了长上下文解码的延迟。

创新点包括：1) 模型无关的Lloyd-Max码本校准（仅需10%层的前向传播）；2) 基于块级absmax的免归一化设计（取代逐token的ℓ2范数）；3) 单常数优化的FP4近似路径（收敛于理想码本质量的6%以内）。在长上下文多轮智能体工作负载上，UltraQuant相比FP8基准实现P50时间至首令牌延迟降低3.47倍（晚期缓存压力场景），输出吞吐量提升1.63倍。

### Q4: 论文做了哪些实验？

论文在多轮对话代理场景下进行了系统实验。实验设置采用长上下文、多轮agent工作负载，基准测试包括GPQA-Diamond、LCB-128K、AIME25和MATH500四个数据集，对比方法包括BF16基线、TQ4（TurboQuant风格4-bit）、FP8 KV缓存、Ultra-TQ以及UltraQuant。在精度实验中，UltraQuant在MATH500上表现稳定（Qwen3.5-A3B达到86.80%，+0.80pp），在GPQA和LCB-128K上具有竞争力，但在AIME25上出现显著退化（-13.33pp和-10.00pp）。在性能实验中，采用MiniMax-M2.5模型、TP=2、2×MI355X GPU、32K/1K配置及并发度64，UltraQuant的输出吞吐量达到BF16基线的1.38倍，与硬件FP8 KV缓存路径的1.37倍相当，同时KV缓存占用减半。在每token延迟方面，UltraQuant的TPOT是BF16的1.40倍，优于Ultra-TQ的1.58倍和vLLM OSS TQ的5.56倍。随着上下文长度增加，UltraQuant的优势更加明显，在64K上下文时延迟降至BF16的约0.5倍。在端到端多轮工作负载中，UltraQuant在缓存压力较大的后期轮次将P50首次token延迟降低了3.47倍（全轮次2.3倍），输出吞吐量提升了1.63倍。

### Q5: 有什么可以进一步探索的点？

基于该研究，未来探索可从以下几方面深入：1）**算法层面**需系统比较固定旋转、校准旋转与学习型旋转在同一Agent基准下的性能差异，并探索KV缓存压缩对长上下文Agent推理中指令遵循、工具调用等细粒度指标的影响；2）**系统层面**应扩展至更多模型族（如Mamba、混合Transformer）、极端上下文长度（>1M token）及不同并发度场景，验证4-bit压缩的泛化性；3）**硬件感知量化**是重要方向——论文揭示非最优码本若直接映射到矩阵核指令，可提升端到端吞吐，这启发未来需联合设计量化方案与硬件指令集，例如探索非均匀量化格式与CUDA Core/MFMA指令的协同优化。此外，当前方法仅关注KV缓存压缩，未来可结合激活值量化、稀疏化等多模态压缩策略，在保持任务质量前提下进一步降低显存压力。

### Q6: 总结一下论文的主要内容

本文针对上下文密集型智能体工作负载下的KV缓存压缩问题，提出4-bit量化方案UltraQuant。该工作负载的特点是长前缀在多个短轮次中复用，且并发性决定GPU利用率。方法上，以TurboQuant风格的旋转量化和码本量化作为质量锚点，vLLM FP8 KV缓存作为部署锚点，通过非对称K/V处理、Walsh-Hadamard旋转、消除QJL和块尺度变体等设计实现高质量4-bit压缩。在系统优化层面，利用AMD GPU的CDNA4架构特性，通过FP8查询、FP4 KV张量、UE8M0组尺度和原生缩放MFMA支持，实现近似旋转码本路径的FP4微张量。实验结果表明，在多轮智能体工作负载的缓存压力大的后期阶段，UltraQuant将P50首次令牌生成时间降低至FP8基线3.47倍（全轮次2.3倍），输出吞吐量提升1.63倍。核心贡献在于证明了4-bit KV缓存能保持激进压缩的上下文容量优势，同时接近硬件原生FP8 KV缓存的可部署性，为智能体服务系统提供了联合优化任务质量、缓存驻留、吞吐量和交互性的端到端方案。
