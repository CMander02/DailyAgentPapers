---
title: "Parallel Context Compaction for Long-Horizon LLM Agent Serving"
authors:
  - "Musa Cim"
  - "Burak Topcu"
  - "Chita Das"
  - "Mahmut Taylan Kandemir"
date: "2026-05-22"
arxiv_id: "2605.23296"
arxiv_url: "https://arxiv.org/abs/2605.23296"
pdf_url: "https://arxiv.org/pdf/2605.23296v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Serving"
  - "Context Window Management"
  - "Parallel Compaction"
  - "Multi-hop QA"
  - "Long-Context Dialogue"
  - "Multi-Agent Systems"
relevance_score: 9.0
---

# Parallel Context Compaction for Long-Horizon LLM Agent Serving

## 原始摘要

Long-horizon LLM agents accumulate growing conversation histories that eventually exceed the model's context window. Context compaction via LLM-based summarization keeps the conversation bounded, but summarization is inherently lossy and the blocking call stalls agent inference for tens of seconds. Moreover, the operator has no fine-grained control over summary volume since prompt instructions are largely ignored, and as context grows, both the amount of output tokens the model produces and the information it retains fluctuate substantially from run to run, making the agent's retained knowledge unpredictable across runs. We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks. Parallel compaction gives the operator fine-grained, predictable control over summary volume and enables more targeted prompt engineering per block. At matched compaction decode volume, it reduces end-to-end wall time and improves compaction throughput over the sequential baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对长周期LLM代理服务中的上下文压缩问题展开研究。在长期运行的代理任务中，对话历史不断累积，最终会超出模型的上下文窗口限制。现有方法通常采用基于LLM的同步顺序压缩（即通过LLM生成摘要来压缩历史），但存在三个核心不足：1）压缩过程是阻塞调用，会导致代理推理停滞数十秒；2）操作者无法精细控制摘要体积，因为模型往往忽略提示指令，导致输出长度和内容在每次运行中不稳定；3）随着上下文增长，信息丢失变得不可预测，尤其在交互式场景（如CLI编码代理）中，最新上下文也被过度压缩，迫使代理在后续轮次中重新发现信息。为此，本文提出**并行压缩**方案，将长上下文切分为固定大小的块，并行生成摘要，从而为操作者提供对摘要体积的细粒度、可预测控制。实验表明，在相同压缩解码量下，并行压缩相比顺序基线能显著降低端到端耗时并提升压缩吞吐量，有效解决了同步压缩的高延迟、不可控和不可预测问题。

### Q2: 有哪些相关研究？

本文的相关研究主要分为以下几类：

1. **上下文压缩与摘要方法类**：本文与基于LLM的上下文压缩方法（如LLMLingua、Selective Context等）相关。这些方法通过剪枝或摘要减少上下文长度，但面临信息丢失和输出不可控的问题。本文提出的并行压缩方法不同于这些顺序阻塞式方法，允许在细粒度上控制摘要体积。

2. **长上下文Agent系统类**：相关工作包括MemoChat、MemorySandbox等长对话记忆管理方法，以及AutoMem、REMEMBER等长期Agent记忆系统。这些工作通常依赖顺序压缩或检索增强，而本文通过并行化压缩过程显著降低延迟。

3. **高效推理与服务类**：与vLLM、FastTransformer等推理优化系统相关，这些工作关注提升LLM推理速度，但未专门处理agent场景下的长上下文压缩。本文首次将并行思想引入agent上下文压缩，实现压缩与推理的流水线化。

4. **基准测试类**：在HotpotQA（多跳问答）和LoCoMo（长上下文对话）基准上评估，与现有长上下文Agent评测形成补充。

本文的核心区别在于将压缩从顺序阻塞操作转变为并行、粒度可控的流水线操作，显著降低了端到端延迟，同时保持了对摘要体积的可预测控制。

### Q3: 论文如何解决这个问题？

论文提出并行压缩方法解决长对话场景下LLM代理的上下文溢出问题。整体框架分为三个阶段：快照与分区、派遣、合并。首先，当对话长度超过压缩阈值τ时，系统对当前对话进行快照并记录长度，将其划分为N个固定大小的连续块B。接着，为每个块k构建包含块1到k前缀的提示，其中目标块k被<TARGET_BLOCK>标记包裹，所有N个提示并发派遣到vLLM服务器。最后，将所有工作完成后的块级摘要按顺序拼接成紧凑历史，替换原始对话。

核心技术创新在于"前缀感知的目标在末尾布局"设计。这种架构避免了两种自然替代方案的缺陷：独立块会破坏前缀缓存并丢失跨块上下文，共享完整前缀同样因不同偏移标记破坏缓存。而目标在末尾布局将目标块置于提示末端注意力最强位置，每个工作节点的前缀严格继承前一个节点的前缀，保持缓存连续性；同时每个工作节点能看到完整历史直到其目标块，维护了跨块上下文。这天然适配代理工作流的因果顺序特性。

关键技术包括：使用固定块大小B作为配置参数实现细粒度控制；通过并行派遣消除顺序摘要的数十秒阻塞延迟；前缀缓存技术在并行请求间共享KV缓存。实验在8B到120B参数的四种架构（含密集/MoE、推理/非推理模型）上验证，表明并行压缩在同等解码量下降低了端到端耗时并提升压缩吞吐量，且摘要量具有可预测性。

### Q4: 论文做了哪些实验？

论文围绕长时域LLM Agent的上下文压缩问题，进行了两组核心实验。首先，实验系统地表征了顺序压缩（Sequential Compaction）的缺陷。实验设置上，使用HotpotQA和LoCoMo两个长上下文基准，在4种骨干模型（参数量从8B到120B，涵盖密集和MoE架构、推理与非推理模型）上，以2k至96k的输入长度进行测试。主要发现：模型输出令牌数几乎不随输入长度增长（仅约400-600个令牌，远小于输入48倍增长），且提示词指令无法有效控制压缩量（如从简洁到详细提示，输出曲线几乎不变）；同时，运行间稳定性差，以变异系数（CV）和余弦相似度衡量，随输入增长，输出长度和语义内容波动加剧（如Llama-3.3-70B在96k输入时CV高达171.6%，余弦相似度降至0.491）。其次，实验在相同基准上评估了提出的并行压缩（Parallel Compaction）方法，与顺序基线对比。在100k令牌上下文下，通过改变块大小（16k、8k、4k、2k）引入不同数量工作线程。结果显示，并行压缩通过保留更多上下文信息，单调地提升了问答准确率（块越小，输出令牌越多，准确率越高）。系统性能上，在HotpotQA多轮Agent流程中，并行压缩在匹配压缩解码量下，相比顺序基线实现了最高1.75倍的端到端吞吐量提升（如gpt-oss-20B模型在2k块大小时），并降低了压缩延迟，同时提供了对压缩体积的细粒度可预测控制。

### Q5: 有什么可以进一步探索的点？

该研究提出的并行压缩方法虽然有效，但仍有几个关键局限值得进一步探索。首先，论文主要评估了多跳问答和长对话场景，尚未验证在需要工具调用、代码生成或多人协作等更复杂智能体任务中的表现，未来可扩展至这些场景以检验方法的鲁棒性。其次，压缩块的分割策略依赖固定窗口大小，可能无法自适应地捕捉语义边界，可考虑引入动态分块机制，例如基于注意力权重或语义相似度来划分关键信息段。此外，并行压缩虽然降低了延迟，但各块独立压缩可能丢失跨块的长程依赖关系，未来可探索轻量级的跨块信息融合机制，如采用图神经网络或键值缓存来保留隐式关联。在实验设计上，当前仅考虑了端到端时间指标，未深入分析不同压缩比例下智能体任务完成质量的退化曲线，可建立更细粒度质量-效率帕累托边界。最后，针对MoE架构等不同模型结构的适配性还可优化，例如为每个专家模块设计专用压缩策略。

### Q6: 总结一下论文的主要内容

并行上下文压缩方法旨在解决长周期LLM代理服务中对话历史不断增长导致上下文窗口超限的问题。传统顺序压缩存在三大缺陷：总结体积不可控（模型几乎忽略提示指令）、信息丢失不可预测（输出长度与内容在不同运行间剧烈波动）、以及阻塞推理延迟达数十秒。该方法创新性地将长上下文分割为多个块，对各块并行执行LLM压缩，赋予操作者通过块数量精确控制摘要体积的能力。在HotpotQA和LoCoMo基准上，使用包含稠密/混合专家架构、推理/非推理模型的四个骨干网络（8B-120B参数）进行实验，结果表明：在匹配压缩解码量的条件下，并行压缩相比顺序基线减少了端到端耗时，提高了压缩吞吐量，实现了摘要体积的细粒度可预测控制，并支持每块更针对性的提示工程。该研究系统刻画了顺序与并行两种压缩方案的行为特征，为长周期代理服务提供了更高效的上下文管理方案。
