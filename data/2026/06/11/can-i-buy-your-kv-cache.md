---
title: "Can I Buy Your KV Cache?"
authors:
  - "Luoyuan Zhang"
date: "2026-06-11"
arxiv_id: "2606.13361"
arxiv_url: "https://arxiv.org/abs/2606.13361"
pdf_url: "https://arxiv.org/pdf/2606.13361v1"
categories:
  - "cs.AI"
  - "cs.CE"
  - "cs.MA"
tags:
  - "KV缓存"
  - "Agent推理优化"
  - "Prefill计算"
  - "持续预填充"
  - "提供商缓存"
  - "Agent经济模型"
  - "跨代理协作"
  - "计算效率"
relevance_score: 8.5
---

# Can I Buy Your KV Cache?

## 原始摘要

Right now, across the world, AI agents are repeating the same absurd act: to read one document, they each recompute it from scratch. Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. The same answer, computed a million times. We make a proposal that is almost offensively simple: compute it once. Let a publisher precompute a document's KV cache, and let every other agent buy the right to load it and skip prefill. It works, and it is token-exact: loading a precomputed KV and continuing matches prefilling from scratch (24/24 greedy tokens, and at the logits level), with no accuracy cost. On Qwen3-4B, reuse is 9-50x cheaper in compute than prefill, and the gap widens with length (prefill's attention scales with L^2), so a single reuse already pays it back. Then the part that matters: where the KV lives. Shipping it fails, because KV is nearly incompressible, so per-load egress costs more than the prefill it saves. Hosting it provider-side, exactly as production prompt-caching works, removes egress entirely. The size of the prize is set by our measured compute saving: serving one hot 3774-token document to 80M agents costs ~$1.5M to re-prefill but only ~$0.03M of reuse compute (49.7x less). The 0.1x cache-read tariff APIs charge passes a 10x discount to users while sitting inside this measured envelope, so the 10x is a floor that the measured ~50x compute saving clears, and the gap to the physical ~50x is provider margin: millions of dollars per popular document. We frame the resulting agent-native prefill CDN and leave lossless KV compression and a cross-party payment layer as the open problems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI代理系统中一个极其低效且普遍存在的问题：当大量代理需要读取同一份文档时，每个代理都会独立、重复地运行大语言模型（LLM）中最消耗计算资源的前缀填充（prefill）阶段，从而为相同的文本内容反复构建相同的键值缓存（KV cache）。这种“重复造轮子”的行为导致了巨大的算力浪费。

现有的研究方法，如生产系统中常见的RadixAttention式前缀缓存，虽然实现了同一服务器内请求间的KV复用，但其本质是服务器内存中的优化手段，缓存无法作为独立的、可跨主体共享的持久化资产。当文档由内容发布者提供，并被成千上万个来自不同会话或代理的请求访问时，重复预填充的计算浪费问题依然存在。

针对这一痛点，本文提出了一个“简单到冒犯”的核心方案：**只计算一次**。即让内容发布者预先计算并持久化文档的KV缓存，其他代理可以付费加载该缓存并跳过前缀填充计算。论文的核心贡献在于验证了这种跨主体的KV缓存复用方案（作者称之为“预填充CDN”），在代币级别上是与从头计算完全一致的（精确校验），并且在计算成本上具有显著优势（对Qwen3-4B模型而言，复用相比预填充可节省9至50倍的计算量），从而为构建一个更高效的AI代理内容分发网络奠定了理论和实验基础。

### Q2: 有哪些相关研究？

相关研究可分为三大类：第一类是跨查询复用预计算KV的工作，如CacheBlend通过选择性重计算部分token恢复跨块注意力质量，Cache-Craft管理可复用块缓存池以降低冗余计算，CacheClip使用辅助模型引导重计算，这些方法针对位置无关的碎片缓存融合问题但引入精度损失。本文聚焦完全共享前缀的精确复用场景（无需重计算、无精度损失），重点研究复用规模的经济性，而非提出新型融合机制，因此技术正交且可互补。第二类将KV作为持久化或可迁移状态处理，包括MatKV将预计算KV存入闪存、InstInfer将KV卸载到计算存储设备、NetKV和ConServe在分离式部署中跨机器传输KV。这些工作证明了KV的持久化存储和跨设备传输可行性，但本文新增了跨参与方的可交易商品属性与成本缩放分析。第三类是KV压缩方向，如SIFT仅存储注意力高值索引的紧凑位向量、SpectrumKV为分离式服务做逐token精度分配。我们的int8实验验证了均匀量化会破坏精确等价性，表明非均匀/选择性压缩方案可在不改变架构前提下优化预填充CDN的经济性。简言之，现有研究使KV复用可行、可存、可移、可小，而我们将其定位为跨多方发布商品，系统论证其成本效益。

### Q3: 论文如何解决这个问题？

这套方案的核心思路是将预填充过程商品化，设计为一种可购买的“计算制品”。整体框架分为出版商和消费者两个角色：出版商对文档执行一次全预填充，生成并存储键值缓存；消费者在推理时直接加载该缓存，从缓存末尾开始生成新token。

关键组件包括三个模块。第一是缓存生成模块，出版商对文档进行单次前向传播，获取所有层的键值张量，并与模型ID、数据类型、文档长度等元数据一起序列化成文件。第二是消费加载模块，消费者在运行时加载缓存，通过设置正确的起始位置ID（文档长度L）和全因果注意力掩码，确保后续token的RoPE位置编码和注意力范围与从头预填充完全一致，从而保证贪婪解码的token级精确性。第三是验证机制，论文证明了预填充单文档的缓存与预填充“文档接续问题”时的对应位置缓存完全一致，因为因果注意力保障了位置i的缓存只依赖前i个token。

创新点体现在三个层面：一是将推理计算解耦为可交易的缓存制品，使每个智能体无需重复预填充。二是设计了无精度损失的精确复用方案，通过位置ID校准和全掩码策略保证了输出与原生预填充完全一致，实测24个贪婪token均匹配，logit差异仅来自浮点精度扰动。三是揭示了关键瓶颈在于缓存传输成本，提出必须采用类似提示缓存的供应商侧托管模式才能消除传输开销，计算上复用比预填充节省9-50倍，单个文档服务8000万次可节省约150万美元。

### Q4: 论文做了哪些实验？

论文在Qwen3-4B模型（fp16精度，Apple M1 Pro/MPS）上进行了实验，旨在验证KV缓存复用（跳过prefill）的有效性和计算成本优势，并与完整prefill进行对比。实验设置排除了磁盘I/O，假设KV始终驻留在内存中。主要实验包括：1) **正确性验证**：贪心解码下，复用预计算的KV缓存进行续写与从头prefill的生成结果完全一致（24/24 token匹配），logits层面的下一token预测argmax相同，最大绝对差值仅0.02，归因于浮点非确定性。2) **计算成本对比**：测量了不同长度下完整prefill与单步续写（复用KV）的时间，结果显示复用带来8.6x至49.7x的加速，且优势随序列长度增加而扩大（如255 tokens时8.6x，3774 tokens时达49.7x）。具体数据：255 tokens时prefill需0.67秒、复用0.078秒；3774 tokens时prefill需14.71秒、复用0.296秒。3) **规模效应**：计算摊销成本与复用次数N的关系，发现盈亏平衡点极低（N*在1.02至1.13之间），即第二次读取即可收回成本。4) **量化影响探究**：对692 token的KV缓存进行int8量化（大小减半至51.1 MB），但破坏了token精确等价，贪心下仅16/32 token匹配原始fp16结果，表明有损压缩会丧失准确性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在KV缓存分发和部署的实际挑战上。未来可探索以下方向：首先，跨设备与跨模型的验证需扩展至服务器GPU和长上下文场景，以分离设备无关的计算趋势。其次，结合有损KV压缩（如混合精度量化）来降低存储和传输成本，但需平衡压缩比与推理精确性。第三，引入缓存融合技术（如CacheBlend），使KV缓存支持多片段检索复用，扩大应用场景至检索增强生成。经济层面需设计跨代理付费层、缓存失效策略和回退本地预填的机制。安全方面需实现托管KV的加密存储与访问控制，防止内容泄露或未计量复用。最后，多模态KV（视频、长文档）因预填成本更高，是更优的复用候选对象，可探索其大小、精确度与复用模式。总体而言，建立“KV原生内容层”将推动从“预填计算”向“缓存交易”的范式转变。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献在于提出了一种创新的计算范式：通过预计算并缓存文档的键值对（KV）缓存，使AI代理无需重复执行昂贵的预填充操作（prefill）。其问题定义是：当前大量AI代理在处理相同文档时，各自独立执行预填充，导致计算资源严重浪费。论文的方法概述为：让内容发布者一次性预计算文档的KV缓存，其他代理通过购买加载权直接使用，从而跳过预填充。主要结论是：在Qwen3-4B模型上，复用KV缓存相比从头预填充可节省9至50倍的计算量，且上下文越长节省越大；该过程是token精确的，无精度损失。但论文也指出，由于KV缓存近乎不可压缩，直接传输成本过高，因此提议采用“提供者端托管”模式（如现有的prompt缓存），以消除传输成本。这项工作的重要意义在于，它为大规模、长上下文、高重复性的文档服务场景（如AI代理、RAG系统）提出了一个计算可优化且经济上可行的方案，并定义了“预填充CDN”这一新架构，同时将无损KV压缩和跨主体支付层作为开放问题留待解决。
