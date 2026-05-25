---
title: "LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems"
authors:
  - "Sadia Asif"
  - "Mohammad Mohammadi Amiri"
  - "Momin Abbas"
  - "Prasanna Sattigeri"
  - "Karthikeyan Natesan Ramamurthy"
date: "2026-05-21"
arxiv_id: "2605.22786"
arxiv_url: "https://arxiv.org/abs/2605.22786"
pdf_url: "https://arxiv.org/pdf/2605.22786v1"
categories:
  - "cs.AI"
  - "cs.ET"
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "安全"
  - "KV缓存"
  - "对抗训练"
  - "隐私保护"
  - "潜通信"
relevance_score: 8.5
---

# LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

## 原始摘要

Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文关注的是基于大语言模型的多智能体系统中潜在的隐私泄露问题。当前多智能体系统主要依赖文本进行通信，但这种方式效率低下且信息有损。为此，最近的研究尝试使用Transformer的键值缓存进行隐式通信，这能提升效率并保留更丰富的语义信息。然而，键值缓存作为一个高维、语义密集的表示层，会编码上下文输入、中间推理状态和智能体特定信息。当这些缓存作为共享工作内存在智能体间传递时，形成了一个不透明的、高带宽的通信通道。即使敏感信息从未以文本形式输出，攻击者也可能通过训练解码器从共享的键值缓存中重建这些信息，从而造成严重的隐私泄露。现有安全机制主要针对生成的输出或工具调用，无法约束隐式表示中的信息流；而针对键值缓存安全的研究则侧重隔离或驱逐，并非针对故意共享的情况。因此，本文要解决的核心问题是：如何在利用键值缓存进行高效隐式通信的同时，限制共享表示中智能体特定敏感信息的可恢复性，从而实现隐私与效用的平衡。

### Q2: 有哪些相关研究？

相关研究主要可分为三类。第一类是**方法类**，包括基于自然语言的Agent通信（如CAMEL、AutoGen）和新兴的潜在通信（如S3、CoA、DCoT），后者通过共享KV缓存提升效率。本文首次指出这种潜在通信引入信息泄露风险，现有方法无法约束表示层内容。第二类是**安全评测类**，如AgentLeak、MAGPIE、PrivacyLens等基准，本文在这些基准上验证LCGuard的效果，并展示其与传统KV共享基线相比更优的隐私-效用权衡。此外，现有KV缓存安全研究（如FastGen、ServeLLM）聚焦隔离或驱逐，而非跨Agent共享场景中的信息控制；多Agent系统安全机制（如CASP、Sotopia）主要约束输出或工具行为，忽略潜在表示的直接泄露。本文填补了这一空白，将泄露定义为重建可恢复性，并通过对抗训练在保留任务语义的同时抑制信息提取。

### Q3: 论文如何解决这个问题？

LCGuard通过对抗学习框架解决多智能体系统中KV缓存共享带来的敏感信息泄露问题。其核心创新在于将共享KV缓存视为隐式工作记忆，在缓存传递前学习表示级变换，实现效用-隐私权衡的显式控制。

整体框架包含两个核心组件：通信函数（Communication Functions）和对抗解码器（Adversarial Decoder）。通信函数参数化为g_{ij}，对KV表示进行变换，保留任务相关信息的同时限制敏感输入的可恢复性；对抗解码器D_i则尝试从观测到的通信工件M_obs中重建敏感输入s_i。两者通过最小最大优化（minimax optimization）进行联合训练：通信函数最小化包含重建损失和任务损失的联合目标，而对抗解码器最大化重建损失以强化窃取能力。

关键技术包括：1）形式化定义表示级敏感信息泄露，通过对抗重建实验判定缓存工件安全性；2）引入可调超参数β控制隐私-效用权衡曲线；3）采用交替优化策略，交替更新通信参数φ_i和对抗参数ψ_i；4）支持局部和系统级两种观测设置，分别对应单链路和全链路泄露防护。实验表明该方法能持续降低重建攻击成功率和任务性能保持的平衡。

### Q4: 论文做了哪些实验？

该论文在多个多智能体基准测试和模型上进行了广泛实验。实验设置包括三个基准测试集: PrivacyLens（评估上下文隐私侵犯）、AgentLeak（评估内部通信泄露）和 MAGPIE（协作私有信息场景）。对比方法包括: 直接传输KV表示的 Vanilla KV Sharing、策略级约束的PrivAct、差分隐私加噪声的ADAPT、以及局部和全系统LCGuard。评估指标包括任务准确率、Helpfulness、隐私得分、泄露率和攻击成功率（ASR）。主要实验结果: 在Qwen3-4B、Gemma-9B和LLaMA-8B三个模型上，分别测试了顺序和层次化两种通信拓扑。结果显示，Vanilla KV Sharing 的Helpfulness最高（如Qwen3-4B顺序PrivacyLens达0.780），但ASR也极高（0.871）。Full-System LCGuard在保持较高Helpfulness（如0.710）的同时，将ASR降至0.216（相比Vanilla KV降低约75%）。ADAPT虽ASR低（0.332），但Helpfulness大幅下降至0.285。PrivAct隐私得分提升（0.820），但ASR仍高达0.845。全系统优化较局部优化效果更好，且LCGuard在多种拓扑和模型上均展现出最佳隐私-效用权衡。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来方向包括：1）当前LCGuard假设所有Agent共享相同的模型架构和潜在空间，但实际多智能体系统常由异构Agent（不同架构或参数量）组成，需要研究跨异构模型间的安全KV共享方法，例如设计通用的表示对齐模块或自适应投影网络。2）仅处理纯文本模态，但多智能体系统正逐步整合视觉、语音等模态数据，需扩展至多模态潜在通信的场景，构建通用敏感信息过滤框架。3）当前采用固定通信策略，未来可探索动态自适应机制，基于任务需求或上下文敏感度决定KV传输的粒度与时机，例如通过强化学习训练开关控制器，在保任务质量与隐私保护间取得更优平衡。此外，可进一步探索差分隐私噪声注入与对抗训练的结合，以抵御更强的推理攻击。

### Q6: 总结一下论文的主要内容

这篇论文提出了LCGuard框架，用于解决多智能体系统中基于键值缓存的潜在通信安全问题。问题定义在于，大语言模型多智能体系统通过共享KV缓存进行潜在通信时，会编码上下文输入、中间推理状态和智能体特定信息，导致敏感内容可能以非文本形式在智能体间传播。方法上，LCGuard将共享KV缓存视为潜在工作记忆，在缓存工件传输前学习表示级转换，并采用对抗训练框架：对抗者学习从共享缓存中重建敏感输入，而LCGuard学习保持任务相关语义并减少可重建信息的变换。主要结论是，在多个模型家族和多智能体基准上的实验表明，与标准KV共享基线相比，LCGuard持续降低了基于重建的泄露和攻击成功率，同时保持了竞争性的任务性能。核心贡献在于形式化了潜在通信中的表示级敏感信息泄露问题，并提供了可验证的安全保障方案，对推动多智能体系统的安全部署具有重要意义。
