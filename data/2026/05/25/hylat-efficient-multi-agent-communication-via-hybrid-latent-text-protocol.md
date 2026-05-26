---
title: "HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"
authors:
  - "Xinyi Mou"
  - "Siyuan Wang"
  - "Zejun Li"
  - "Yulan He"
  - "Zhongyu Wei"
date: "2026-05-25"
arxiv_id: "2605.25421"
arxiv_url: "https://arxiv.org/abs/2605.25421"
pdf_url: "https://arxiv.org/pdf/2605.25421v1"
categories:
  - "cs.CL"
tags:
  - "多智能体通信"
  - "混合通信协议"
  - "隐空间通信"
  - "文本通信"
  - "通信效率"
  - "可解释性"
  - "协同训练"
  - "通信三元论"
relevance_score: 10.0
---

# HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol

## 原始摘要

Communication protocol design is a central challenge in large language model-based multi-agent systems. Existing single-channel approaches face an inherent communication trilemma: text-based methods are interpretable but verbose, while latent-space methods are efficient but opaque and limited to unidirectional workflows. Inspired by multi-channel communication theory, we propose HyLaT, a hybrid latent-text communication protocol that transmits elaborate cognitive signals through a latent channel for efficiency, while expressing concise critical signals in natural language to preserve interpretability and precision. We introduce a two-stage training framework combining single-agent hybrid generation learning and multi-agent interactive co-training, enabling agents to generate and interpret hybrid messages across multiple rounds of interaction. Experiments demonstrate that HyLaT reduces communication overhead significantly while maintaining competitive task performance, with strong generalization and robustness across diverse settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统中，现有单通道通信协议面临的根本性矛盾，即“智能体通信三难困境”：文本通信可解释但低效（信息冗余、令牌开销大）；潜在空间通信高效但完全不透明（缺乏可解释性）且仅支持单向/单轮流程，无法灵活支持多轮交互。现有方法受限于单通道的固有缺陷，无法同时满足效率、可解释性与通用性（如支持多轮、多智能体、人机交互）这三个关键需求。

受多通道通信理论启发，作者认为消息中包含的“详尽认知信号”（如推理过程）与“关键决策信号”（如最终答案）在功能上对不同通道有不同偏好。核心问题在于：能否设计一种混合协议，让智能体通过专门“通道”传输不同类型信息，从而在效率与透明度之间取得最优平衡，同时支持更复杂、通用的多智能体协作场景。

### Q2: 有哪些相关研究？

在相关研究中，本文主要关注三类工作：

1. **基于文本的多Agent通信方法**：如通过自然语言、结构化消息或共享记忆进行交互的MAS应用（辩论、软件开发、社会模拟）。这些方法可解释性强，但随Agent与轮次增加，通信开销迅速增长。本文区别在于提出混合协议，用潜在通道传递高效认知信号，保留文本通道的精确性与可解释性。

2. **通信效率优化方法**：早期涌现通信工作表明Agent可自创紧凑协议；近年研究包括压缩消息内容、修剪消息传递图或重组协议。本文不同之处在于，现有方法局限于结构化文本或学习符号语言，信息密度受限，而HyLaT的潜在通道可编码更密集的认知信号。

3. **基于潜在表示的推理与协作**：包括通过共享隐藏状态或投影KV缓存实现跨模型语义传递的单轮推理扩展。尽管此类方法在效率上优于显式思维链，但存在两个主要局限：完全依赖潜在通信导致可解释性与可控性下降；其思维传递机制通常仅支持单向顺序流程，无法处理多轮交互。本文的混合协议同时解决了这两个问题，且训练框架支持多轮协同学习。

### Q3: 论文如何解决这个问题？

HyLaT通过混合潜-文协议解决多智能体通信中的效率与可解释性矛盾。整体框架采用双通道设计：潜通道传输详细认知信号（如推理过程），文本通道传递简洁关键信息（如最终答案）。这一分工通过两阶段训练实现。

第一阶段为单智能体混合生成学习。训练时对同一输入同时进行两个前向传播：混合前向从特殊标记<bot>开始自回归生成k个连续潜向量，随后生成文本回答，并计算文本部分的语言建模损失；文本前向则在教师强制下生成完整的“解释+答案”。关键创新在于跨通道对齐：将文本前向中回答前最后一个位置的隐藏状态作为目标，通过L2损失让混合前向在该位置的特征接近文本前向的对应激活（梯度停止），从而将解释信息压缩到潜空间。损失函数为三种损失的加权和。

第二阶段为多智能体交互共训练。多个智能体共享同一骨干网络，每轮交互中每个智能体接收自身累积上下文和其他智能体上一轮的完整响应（包含潜向量和文本）。训练时对每个智能体分别计算与第一阶段相同的三项损失，然后对所有智能体取平均。这样各智能体就能学会解读来自同伴的潜向量，并生成包含潜向量和文本的混合响应。

该设计的关键创新在于：通过跨通道对齐机制将冗长解释压缩为潜向量实现高效通信，同时保留文本通道确保可解释性；两阶段训练框架使模型既能独立生成混合输出，又能通过交互学习理解他人的潜信号。

### Q4: 论文做了哪些实验？

论文在LlaMA-3.2-1B-Instruct主干模型上进行实验，采用两阶段训练：阶段1使用CommonsenseQA、SocialIQA等包含详细推理链的数据集训练单智能体混合输出；阶段2使用HotpotQA等多跳数据集构建多智能体交互数据（精炼与分解任务）。评估采用多智能体辩论（MAD）任务，涵盖领域内（CommonsenseQA等5个）和领域外（MedQA、ARC-Easy/Challenge）8个数据集，使用3智能体、2轮通信设置。

对比方法包括：文本方法（NL、AutoForm、EcoLang、SDE）、潜在空间方法（Cipher、LatentMAS-V）以及训练基线（TextFullT、LatentFullT）。主要结果：（1）HyLaT在效率上超越所有基线，平均每问题仅使用72.01个token（1.47秒），相比最有效的文本方法EcoLang（960.26 token/10.04秒）提升10.6×/6.8×；（2）性能保持竞争力，在SocialIQA上平均准确率达82.56%（最佳），多数投票达83.00%（最佳），在领域内5个数据集中2项第二、2项第一；（3）消融实验证实双通道设计的互补性：纯文本变体token增至639.18但性能略降，纯潜在变体准确率仅50.28%；两阶段训练不可或缺，跳过阶段1准确率降至38.43%，跳过阶段2格式错误率达22.27%。此外展示了异构智能体兼容性、鲁棒性（σ≤0.5噪声下性能稳定）、扩展到4智能体/3轮的能力，以及在信任博弈社会模拟中的泛化性（平均返还10.84，远高于其他方法）。

### Q5: 有什么可以进一步探索的点？

首先，论文主要依赖1B和3B参数的小模型进行实验，其结论在更大规模模型上的泛化性尚未验证。未来可探索将HyLaT应用于7B以上模型，观察混合协议在更大参数量下是否能保持甚至提升通信效率与性能优势。其次，HyLaT与vLLM等主流推理框架不兼容，限制了其在长时间、多轮次的大规模多智能体场景中的部署。因此，优化生成过程以适配高效推理框架是实现实际应用的关键。第三，文本通道的多样性受限于QA式辩论数据，导致表达模式单一。未来可引入更丰富的多智能体交互数据，如角色扮演、协作推理等，以增强文本通道的语义丰富度和上下文适应性。最后，潜在通道的可解释性问题依然突出。如何设计信息瓶颈或正则化机制，在保留潜在向量高效性的同时提升其解码透明度和可控性，是值得探索的方向。

### Q6: 总结一下论文的主要内容

本文提出了HyLaT，一种混合潜在-文本通信协议，旨在解决大语言模型多智能体系统中的通信三难困境：纯文本方法可解释但冗长，潜在空间方法高效但不透明且局限于单向流程。HyLaT通过潜在通道传输详尽的认知信号以提高效率，同时通过文本通道表达简洁的关键信号以保持可解释性和精确性。研究提出了两阶段训练框架，包括单智能体混合生成学习和多智能体交互协同训练，使智能体能够跨多轮交互生成和解释混合消息。实验表明，HyLaT在显著降低通信开销的同时保持了竞争性的任务性能，并在多种设置下展现出强大的泛化能力和鲁棒性。该工作的核心贡献在于首次提出混合通信协议设计，有效平衡了效率与可解释性，为多智能体系统的高效协作提供了新范式。
