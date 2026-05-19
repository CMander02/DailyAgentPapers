---
title: "LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems"
authors:
  - "Hyunji Lee"
  - "Justin Chih-Yao Chen"
  - "Joykirat Singh"
  - "Zaid Khan"
  - "Elias Stengel-Eskin"
  - "Mohit Bansal"
date: "2026-05-18"
arxiv_id: "2605.18565"
arxiv_url: "https://arxiv.org/abs/2605.18565"
pdf_url: "https://arxiv.org/pdf/2605.18565v1"
github_url: "https://github.com/amy-hyunji/LongMINT"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long-Horizon Agent"
  - "Multi-Target Interference"
  - "Benchmark"
  - "Memory-Augmented Agent"
  - "Domain Generalization"
relevance_score: 9.0
---

# LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems

## 原始摘要

Real-world agents operate over long and evolving horizons, where information is repeatedly updated and may interfere across memories, requiring accurate recall and aggregated reasoning over multiple pieces of information. However, existing benchmarks focus on static, independent recall and fail to capture these dynamic interactions between evolving memories. In this paper, we study how current memory-augmented agents perform in realistic, interference-heavy, long-horizon settings across diverse domains and question types. We introduce LongMINT (Long-Horizon Memory under INTerference), a benchmark featuring (1) long, highly interconnected contexts with frequently updated information that induces substantial interference, (2) diverse domains (state tracking, multi-turn dialogue, Wikipedia revisions, and GitHub commits), enabling evaluation of domain generalization, and (3) diverse question types that assess robustness to interference, including (i) single-target recall tasks requiring retrieval of a specific target from long contexts, and (ii) multi-target aggregation tasks requiring reasoning over multiple relevant pieces of information. Overall, LongMINT has 15.6k question-answering pairs over long-horizon contexts averaging 138.8k tokens and extending up to 1.8M tokens per instance. We evaluate 7 representative systems, including vanilla long-context LLMs, RAG, and memory-augmented agent frameworks. Across all systems, we observe consistently low performance (avg. 27.9% accuracy), especially on questions requiring aggregated reasoning over multiple pieces of evidence. Our analysis shows that performance is primarily limited by retrieval and memory construction. Furthermore, current memory systems struggle to recall and reason over earlier facts that are later revised or interfered with by subsequent context, with performance degrading as the number of intervening updates increases.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基准测试无法评估长时域智能体在多目标信息干扰下记忆与推理能力的问题。研究背景是，现实世界中的智能体需要在不断演变的长时域中运行，信息会反复更新且彼此间可能产生干扰，要求智能体不仅能准确回忆单个信息，还能对多个相关信息进行聚合推理。然而，现有的评估基准如长上下文LLM测试大多聚焦于静态、独立的回忆任务，未能捕捉动态信息更新带来的干扰效应，例如早期信息被后续更新覆盖或冲突时，智能体仍能正确调用和推理。本文的核心问题是：当前记忆增强型智能体在高度干扰、信息频繁更新的长时域场景中表现如何？为了系统评估这一问题，作者提出了 LongMINT 基准，其特点包括：构造长且高度互联的上下文，频繁更新信息以诱导干扰；覆盖状态追踪、多轮对话、维基百科修订和GitHub提交等多样领域；设计单目标回忆和多目标聚合两类问题。实验表明，现有系统（包括长上下文LLM、RAG和记忆增强框架）平均准确率仅27.9%，尤其在需要聚合推理的任务上表现差，主要受限于检索和记忆构建能力，且随着干扰更新次数增加，性能显著下降。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**记忆增强智能体系统**，如Reflexion、MemGPT、ChatDev等，它们通过长期记忆、检索增强生成（RAG）或外部知识库来支持长程任务。本文的LongMINT与这些系统不同，重点关注多目标干扰动态更新对记忆检索的影响，而非仅测试静态回忆。第二类是**长上下文与记忆评测基准**，包括Needle-in-a-Haystack、L-Eval、LongBench等，它们主要评估单目标检索或孤立信息理解。LongMINT进一步引入多目标聚合推理任务，并模拟信息更新导致的高干扰长上下文，揭示现有基准忽视的“后见之明”更新干扰问题。第三类是**推理与综合理解评测**，如HotpotQA、2WikiMultiHopQA等，侧重多跳推理。LongMINT则更强调在多目标干扰下对频繁更新的信息的检索与推理，并涵盖多领域（状态追踪、多轮对话、维基百科修订、GitHub提交），以测试领域泛化能力。总之，LongMINT填补了现有工作在动态长程记忆干扰评估上的空白。

### Q3: 论文如何解决这个问题？

本文通过构建一个专为评估长时程、多目标干扰场景下记忆系统能力的新型基准LongMINT，来解决现有基准无法捕捉动态记忆交互的问题。该基准的核心设计包含三个层面：首先，构建了长度平均138.8k token、最长可达1.8M token的密集上下文，其中信息频繁更新并产生强干扰；其次，覆盖了状态跟踪、多轮对话、维基百科修订和GitHub提交四个异质领域，以检验领域泛化能力；最后，设计了两种评估记忆干扰鲁棒性的问题类型——单目标回溯任务（从长上下文中精确检索特定事实）和多目标聚合任务（整合多个相关信息进行推理）。

在方法上，研究者系统评估了七类代表性系统，包括纯长上下文大语言模型、RAG系统（检索增强生成）以及记忆增强型Agent框架。关键创新在于揭示了记忆系统在现实干扰场景下的深层失效模式：所有系统在平均27.9%的准确率下表现不佳，尤其是多目标聚合任务（准确率远低于单目标任务）。通过细致分析发现，性能瓶颈主要源于两个方面：检索机制的缺陷（难以从密集干扰信息中精准定位目标）和记忆构建的局限性（无法有效整合与更新动态信息）。更关键的是，当早期事实被后续内容修订或覆盖时，现有记忆系统表现出显著的"记忆干扰"效应——随着更新次数增加，召回和推理准确率呈单调下降趋势。这直接揭示了当前长时程Agent系统在面对现实场景中信息动态变化与相互干扰时的根本性局限。

### Q4: 论文做了哪些实验？

论文 LongMINT 设计了包含15,600个问答对的基准测试，平均上下文长度为138.8k token，最长可达1.8M token。实验设置覆盖四个多样化领域：状态追踪（如文件操作序列）、多轮对话（含信息更新）、维基百科修订和GitHub提交日志，旨在评估长期交互中多目标干扰下的记忆性能。问题类型分两类：(i) 单目标召回（从长上下文中检索特定事实）和 (ii) 多目标聚合（需综合多个相关证据进行推理）。对比方法包括7种代表性系统：普通长上下文LLM（如GPT-4）、RAG（检索增强生成）和记忆增强型Agent框架。主要结果显示，所有系统平均准确率仅27.9%，尤其在多目标聚合任务上表现更差。关键数据揭示：性能瓶颈主要在于检索准确性和记忆构建机制，当事实被后续更新干扰后，系统对早期信息的召回率随干预更新次数增加而显著下降，表明当前记忆系统无法有效处理记忆冲突与动态演化。

### Q5: 有什么可以进一步探索的点？

未来可探索的方向包括：**1）更鲁棒的记忆表征与检索机制**，当前系统在记忆更新后难以准确召回被修订的事实，可研究基于因果推理或时间感知的检索策略，例如引入“版本化记忆”或“干扰感知注意力”，在检索时优先排除后续信息干扰；**2）多目标聚合推理的端到端优化**，现有方法将检索与推理分离，易丢失跨事实关联，可探索将记忆构建与推理过程联合训练，例如通过图神经网络建模事实间依赖关系，或利用LLM生成中间推理链以辅助检索；**3）动态更新的增量学习框架**，长程场景中信息持续更正对模型构成挑战，可借鉴持续学习中弹性权重巩固（EWC）方法，或在记忆写入时预留冲突检测与回溯修正机制。此外，当前评估集中于英文文本与结构化数据（如GitHub），未来可将LongMINT扩展至多语言或非结构化视觉场景（如视频流中的目标跟踪），进一步检验跨模态记忆干扰下的模型泛化能力。

### Q6: 总结一下论文的主要内容

在长期任务驱动的AI系统中，代理常面临多段动态更新信息间的相互干扰，导致记忆与推理困难。现有基准测试局限于静态、独立的回忆任务，无法评估这一现实挑战。本论文提出LongMINT基准，专门评测记忆增强型代理在多目标干扰下的长期记忆能力。LongMINT包含长达138.8k tokens、最高1.8M tokens的上下文，涵盖状态追踪、多轮对话、维基百科修订及GitHub提交四个领域，并设计单目标回忆与多目标聚合两类问题。对7种代表性系统（包括长上下文LLM、RAG及记忆增强框架）的评估显示，平均准确率仅27.9%，在多证据聚合任务上表现更差。分析发现性能瓶颈主要在于检索与记忆构建：当前系统难以在后续信息频繁修订或干扰下，成功回忆并推理早期事实，且随着干预数量增加，性能持续下降。该工作揭示了现有记忆增强代理在处理动态信息干扰方面的根本缺陷，为构建更鲁棒的长期交互系统指明了方向。
