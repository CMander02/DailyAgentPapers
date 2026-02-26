---
title: "DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs"
authors:
  - "Xi Ye"
  - "Wuwei Zhang"
  - "Fangcong Yin"
  - "Howard Yen"
  - "Danqi Chen"
date: "2026-02-25"
arxiv_id: "2602.22175"
arxiv_url: "https://arxiv.org/abs/2602.22175"
pdf_url: "https://arxiv.org/pdf/2602.22175v1"
categories:
  - "cs.CL"
tags:
  - "长上下文推理"
  - "解码算法"
  - "注意力机制"
  - "检索增强"
  - "推理能力提升"
relevance_score: 6.5
---

# DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs

## 原始摘要

Understanding and reasoning over long contexts is a crucial capability for language models (LMs). Although recent models support increasingly long context windows, their accuracy often deteriorates as input length grows. In practice, models often struggle to keep attention aligned with the most relevant context throughout decoding. In this work, we propose DySCO, a novel decoding algorithm for improving long-context reasoning. DySCO leverages retrieval heads--a subset of attention heads specialized for long-context retrieval--to identify task-relevant tokens at each decoding step and explicitly up-weight them. By doing so, DySCO dynamically adjusts attention during generation to better utilize relevant context. The method is training-free and can be applied directly to any off-the-shelf LMs. Across multiple instruction-tuned and reasoning models, DySCO consistently improves performance on challenging long-context reasoning benchmarks, yielding relative gains of up to 25% on MRCR and LongBenchV2 at 128K context length with modest additional compute. Further analysis highlights the importance of both dynamic attention rescaling and retrieval-head-guided selection for the effectiveness of the method, while providing interpretability insights into decoding-time attention behavior. Our code is available at https://github.com/princeton-pli/DySCO.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在处理长上下文时性能显著下降的问题，即“上下文腐化”现象。随着模型支持的上文长度不断增加（如128K tokens），尽管技术上能够处理，但在实际推理任务中，模型的准确率会随着输入长度的增长而急剧恶化。

研究背景是，当前的长上下文模型虽然在架构和数据上取得了进步，但在生成过程中，其注意力机制往往无法持续、动态地对准当前解码步骤最相关的上下文信息。现有方法，如注意力均匀缩放、KV缓存淘汰或压缩技术，主要侧重于提升推理效率，有时甚至会损害推理性能；而更高层次的智能体流程或外部上下文管理系统，则并非直接作用于模型的核心注意力机制。

本文要解决的核心问题是：如何在解码阶段，以轻量且无需训练的方式，动态调整模型的注意力分布，使其在生成长文本时能更有效地聚焦于任务相关的关键上下文片段。为此，论文提出了DySCO解码算法，其核心思想是利用模型中专门负责长上下文检索的“检索头”来识别每一步的相关令牌，并显式地提升这些令牌在注意力中的权重，从而在仅增加少量计算开销的情况下，显著提升模型在长上下文推理任务上的准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：改进长上下文语言模型的方法和长上下文推理技术。

在**改进长上下文语言模型**方面，已有大量研究从多个维度展开，包括模型架构设计、数据工程策略、上下文窗口扩展技术、评测基准构建，以及对长上下文行为和失效模式的分析。这些工作的共同点在于，它们主要通过修改模型参数、架构或训练数据来提升性能。与之形成鲜明对比的是，本文提出的DySCO方法不改变模型本身，而是聚焦于**改进解码过程**，是一种无需训练、可直接应用于现成模型的后处理技术。

在**长上下文推理技术**方面，另一类研究工作专注于推理阶段的优化方法。DySCO属于这一范畴，但其核心创新在于**动态调整解码时的注意力机制**。具体而言，DySCO利用模型内部固有的“检索头”（专门用于长上下文检索的注意力头子集），在每一步解码时识别任务相关的关键令牌，并显式地提升其注意力权重。这与许多静态的或基于检索增强生成（RAG）的推理优化技术不同，DySCO实现了**基于模型内部信号的、动态的注意力重缩放**，从而更精准地利用长上下文中的相关信息。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为DySCO的新型解码算法来解决长上下文语言模型在解码过程中注意力难以持续聚焦于最相关上下文的问题。该方法的核心思想是在解码的每一步，动态地识别并增强对任务关键令牌的关注，从而提升模型的长程推理能力。

其整体框架和关键技术如下：DySCO是一种无需训练、可直接应用于现成语言模型的解码时方法。它的核心架构依赖于模型内部已有的“检索头”——即模型中专门负责长上下文信息检索的那一部分注意力头。在解码生成每个新令牌时，DySCO首先利用这些检索头来扫描整个长上下文，并计算每个上下文令牌与当前生成步骤的相关性分数。基于这些分数，算法识别出最相关的一小部分关键令牌。随后，DySCO的核心操作——动态注意力缩放——被激活：它显式地提升（即“up-weight”）这些关键令牌在注意力机制中的权重，同时相应地降低其他不相关令牌的权重。这个过程是动态的，随着解码步骤的推进而不断调整，确保注意力始终被引导至当前最需要的上下文信息上。

主要创新点包括：1) **训练无关的动态调整**：无需对模型进行任何微调或额外训练，直接在推理阶段修改注意力分布，计算开销较小。2) **检索头引导的令牌选择**：创新性地利用模型内部固有的、功能特化的注意力头作为“指南针”，来精准定位相关上下文，这比使用外部检索器或简单启发式方法更为内聚和高效。3) **可解释的注意力行为**：该方法在提升性能的同时，提供了对解码过程中注意力聚焦机制的洞察，增强了模型行为的可解释性。通过这种动态的、基于内部信号引导的注意力重缩放机制，DySCO有效地缓解了长上下文下模型性能衰减的问题。

### Q4: 论文做了哪些实验？

论文在多个长上下文推理任务上进行了实验。实验设置方面，主要测试了Qwen3-4B/8B/32B和Llama-3.1-8B-Instruct等开源模型，并直接使用官方实现中检测到的检索头（QR heads）。对比方法包括：1）标准解码（Vanilla）；2）用于扩展上下文窗口的YaRN；3）统一注意力缩放（AttnTS），即对所有注意力logits进行温度缩放。DySCO和AttnTS的超参数在MRCR开发集上设定，并直接应用于其他数据集。

使用的数据集/基准测试主要包括：1）PathTrans，用于评估模型在解码各步骤中保持关注相关上下文的能力；2）MRCR（多轮共指消解）、LongBenchV2和Clipper，用于评估长上下文下的多步思维链推理；3）HotpotQA和InfBench（含InfMC和InfQA），用于评估长上下文直接召回（即“大海捞针”式）任务。上下文长度覆盖4K、8K、16K、32K、64K和128K。

主要结果如下：在PathTrans上，DySCO在不同上下文长度下均带来性能提升，例如在32K长度下，Qwen3-8B的准确率从1%提升至33%（AttnTS仅提升至2%）。在128K长度的主要推理任务上，DySCO（结合YaRN）相比仅使用YaRN，为Qwen3-8B在MRCR上带来3.5个绝对百分点（相对提升22%）、在LongBenchV2上提升8.2点（29%）、在Clipper上提升2.5点（10%）的改进。在长上下文召回任务中，DySCO也普遍提升性能，如将Llama-3.1-8B-Instruct在HotpotQA上的准确率从46提升至52。AttnTS的改进则较小且不稳定。此外，与RAG（Stella）和提示词压缩方法（LongLLMLingua）相比，DySCO在Qwen3-8B上表现更优，且在上下文长度64K以内时持续带来提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的DySCO方法虽然有效，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖于模型自身存在的“检索头”，但并非所有模型都具备或能清晰识别此类头部，这限制了方法的普适性。未来可研究如何自动检测或诱导出更通用的上下文检索机制。其次，动态调整仅基于当前解码步的局部信息，可能缺乏对全局文档结构的考量；结合层次化注意力或引入轻量级记忆模块来维持长期依赖，是潜在的改进思路。此外，方法在超长上下文（如百万token）下的效率和效果尚未验证，探索更高效的近似检索与权重缩放算法至关重要。最后，当前评估集中于特定基准，未来需在更复杂的真实长文档任务（如法律分析、科学文献综述）中检验其泛化能力，并探索与检索增强生成（RAG）等范式的协同优化。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为DySCO的新型解码算法，旨在提升语言模型在长上下文推理任务中的性能。核心问题是现有模型尽管支持长上下文窗口，但在输入长度增加时准确率会下降，因为解码过程中注意力难以持续聚焦于最相关的上下文信息。

DySCO的核心方法是在解码时动态调整注意力权重。它利用模型内部专门用于长上下文检索的“检索头”，在每个解码步骤中识别出与当前任务最相关的关键token，并显式地提升这些token的注意力权重。这种方法无需额外训练，可直接应用于现有的预训练语言模型。

实验表明，DySCO在多个指令微调和推理模型上，对MRCR、LongBenchV2等具有挑战性的长上下文推理基准测试（上下文长度达128K）均能带来性能提升，相对增益最高可达25%，且仅需适度的额外计算开销。论文进一步分析证实，动态注意力重缩放和基于检索头的引导选择是该方法有效的关键，同时也为解码时的注意力行为提供了可解释性洞察。
