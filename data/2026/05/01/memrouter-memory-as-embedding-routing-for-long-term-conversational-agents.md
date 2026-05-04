---
title: "MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents"
authors:
  - "Tianyu Hu"
  - "Weikai Lin"
  - "Weizhi Zhang"
  - "Jing Ma"
  - "Song Wang"
date: "2026-05-01"
arxiv_id: "2605.00356"
arxiv_url: "https://arxiv.org/abs/2605.00356"
pdf_url: "https://arxiv.org/pdf/2605.00356v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "长期对话记忆"
  - "记忆路由"
  - "嵌入路由"
  - "轻量分类器"
  - "LoCoMo基准"
  - "延迟优化"
  - "LLM智能体"
relevance_score: 8.5
---

# MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents

## 原始摘要

Long-term conversational agents must decide which turns to store in external memory, yet recent systems rely on autoregressive LLM generation at every turn to make that decision. We present MemRouter, a write-side memory router that decouples memory admission from the downstream answer backbone and replaces per-turn memory-management decoding with an embedding-based routing policy. MemRouter encodes each turn together with recent context, projects the resulting embeddings through a frozen LLM backbone, and predicts whether the turn should be stored using lightweight classification heads while training only 12M parameters. Under a controlled matched-harness comparison on LoCoMo, where the retrieval pipeline, answer prompts, and QA backbone (Qwen2.5-7B) are held identical, MemRouter outperforms an LLM-based memory manager on every question category (overall F1 52.0 vs 45.6, non-overlapping 95% CIs) while reducing memory-management p50 latency from 970ms to 58ms. Descriptive factorial averaging further shows that learned admission improves mean F1 by +10.3 over random storage, category-specific prompting adds +5.2 over a generic prompt, and retrieval contributes +0.7. These results suggest that write-side memory admission can be learned by a small supervised router, while answer generation remains a separate downstream component in long-horizon conversational QA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长程对话代理中内存管理的高成本和与下游模型耦合的问题。现有基于LLM的内存管理方法(如Memory-R1、AgeMem等)在每个对话轮次都需要进行一次或多次完整的自回归生成调用来决定是否存储信息,导致计算开销巨大。例如,Memory-R1每轮需要两次生成调用,一个600轮对话就需要约1200次调用。同时,这些方法的内存策略与特定下游答案模型紧密耦合,升级模型需要重新训练内存管理策略。

本文提出MemRouter,核心创新是将内存准入决策从自回归生成解耦为基于嵌入的路由策略。它编码每轮对话及其上下文,通过冻结的LLM主干得到嵌入,再用轻量级分类头预测是否存储,仅训练1200万个参数。在相同检索管道、回答提示和QA主干条件下,MemRouter在所有问题类别上超越基于LLM的内存管理器(整体F1为52.0 vs 45.6),并将延迟从970ms降至58ms。研究表明,写端内存准入可以通过小型监督路由器学习,而答案生成仍作为独立组件,实现了高效且可复用的内存管理。

### Q2: 有哪些相关研究？

相关研究可分为三类：**记忆架构类**、**强化学习训练的记忆管理类**和**路由与门控机制类**。

在记忆架构方面，MemGPT、A-MEM、MemoryBank、Mem0 等工作关注记忆组织和检索，但依赖启发式规则或LLM本身决定存储内容，这是本文要解决的核心瓶颈。本文的创新在于将写入侧内存准入决策从LLM生成解耦为轻量嵌入路由。

在强化学习方法中，Memory-R1 是最近工作，同时训练记忆管理器和答案代理，但记忆管理器仍是每轮生成的7B LLM，延迟高。本文证明无需LLM参与每轮准入决策，仅训练12M参数的分类头即可达到更好效果（F1 52.0 vs 45.6）。

在路由机制方面，RCR-Router、MemR3、G-MemLLM 等工作主要在检索或潜在更新中使用路由，而本文首次将嵌入级路由应用于写入侧的对话轮次是否存入记忆的决策，而非生成式选择。

### Q3: 论文如何解决这个问题？

MemRouter提出了一种将记忆管理（写路径）与问答生成（读路径）完全解耦的架构，核心方法是用轻量级嵌入路由器替代每轮自回归LLM解码。整体框架由三个组件构成：记忆路由器、记忆存储、答案生成器。

记忆路由器是核心创新，包含三个串联阶段。第一阶段：近期对话历史被切分为固定大小的块（每块最多5轮，最多13块），由冻结的句子编码器（BGE-large-en-v1.5）编码为块级嵌入，再通过一个带LayerNorm和GELU的两层MLP投影到骨干网络隐藏维度（Qwen2.5-7B的3584维），投影层是主要可训练参数（约8M）。第二阶段：投影后的块序列直接馈入冻结的Qwen2.5-7B transformer体（不经过token嵌入查找），利用其28层进行单次前向传播完成上下文化，提取当前轮次的最终表示。第三阶段：该表示通过两个轻量分类头（约4M参数）预测存储操作（ADD/NOOP）和内容类型（key_facts/emotional等）。整个路由器仅训练12M参数（0.17%的7B模型）。

记忆存储部分采用混合检索：结合密集语义匹配（BGE）和BM25稀疏检索，并引入说话者增益、时间线索增强、会话多样性约束等轻量调整。答案生成器使用冻结的LLM（Qwen2.5-7B），仅对问题调用一次，通过分类特定的提示优化输出格式（如单跳/时间问题要求5-6词精确回答，多跳问题要求列举）。

主要创新点：1）嵌入级的记忆路由策略完全消除每轮自回归解码开销（延迟从970ms降至58ms）；2）路由器与答案生成器的解耦设计，使得记忆管理可独立训练而无需修改大型语言模型；3）通过教师模型（Qwen3.5-35B-A3B）生成监督标签，结合加权交叉熵训练，在LoCoMo上F1达52.0显著优于LLM基线的45.6。

### Q4: 论文做了哪些实验？

在LoCoMo数据集上，采用Memory-R1的1:1:8划分（对话1训练，2验证，3-10测试）并排除对抗性问题。主要对比方法包括Memory-R1（GRPO）及相关基线，使用官方token级F1指标。关键的匹配控制实验固定了检索管道、答案提示和QA骨干模型（Qwen2.5-7B），仅改变写入端存储策略。MemRouter在所有问题类别上超越基于LLM的记忆管理器：总体F1 52.0 vs 45.6（非重叠95%置信区间），单跳57.5→19%提升，多跳52.4→19%提升。存储管理p50延迟从970ms降至58ms（17倍降低），端到端吞吐量提升11倍（2.58 vs 0.24 QA/s）。预算匹配实验（62%存储率）显示MemRouter最优（F1 50.8），优于MLP-only（50.0）、关键词启发式（47.2）、随机存储（42.8）和最近k存储（38.6），而全部存储上限为53.7。存储预算曲线表明，在低预算下差距扩大至11.4 F1。描述性因子分析显示，学习型准入策略贡献+10.3 F1（优于随机），类别特定提示+5.2，检索+0.7。跨骨干迁移（LLaMA-3.1-8B）验证了仅需重训练12M参数的轻量级路由头，总体F1达49.1，时序F1（46.3）甚至超过原始设置。

### Q5: 有什么可以进一步探索的点？

MemRouter的核心创新在于将记忆写入决策从生成式LLM解耦为轻量路由，但其局限也十分明显。第一，当前实验仅基于LoCoMo单一数据集，且答案骨干固定为Qwen2.5-7B，该路由策略在更长对话跨度（如千轮级）、不同语言或领域（如医疗、客服）下的泛化能力未被验证。第二，路由策略仅依赖历史上下文编码，未显式建模未来查询主题的分布，可能过早丢弃后续对话中要回顾的关键细节。第三，12M参数的头虽然高效，但固定了预训练backbone，未能利用对话动态调整嵌入空间。未来可从三个方向改进：一是引入元学习或强化学习，使路由策略在记忆占用与检索效用之间动态权衡；二是设计分层记忆槽，让Router按主题或实体预测存储层级，而非简单二值化；三是结合用户反馈信号（如重复追问）在线微调路由决策，使记忆构建逐步适配个性化需求。

### Q6: 总结一下论文的主要内容

本文提出MemRouter，一种嵌入驱动的写端存储路由方法，旨在解决现有多轮对话记忆系统中LLM每次交互都要生成存储决策导致的过高延迟和模型耦合问题。传统方法每轮记忆管理需多次自回归生成调用，不仅带来显著计算开销，还将存储策略与下游回答模型绑定，升级时需重新训练。MemRouter将每一轮对话与近程上下文编码为嵌入序列，通过冻结的LLM骨干网络投影后，使用轻量级分类头直接推理该轮是否应存入外部记忆，仅训练约1200万参数。在LoCoMo基准控制实验中，保持检索管道、提示模板和QA骨干（Qwen2.5-7B）完全一致，MemRouter的整体F1值达52.0，显著优于基于LLM的记忆管理器的45.6，且非重叠置信区间确认差异显著。P50延迟从970毫秒锐减至58毫秒。通过因子消融分析，学习型存储策略相比随机存储平均提升F1达10.3，任务特定提示比通用提示提升5.2，检索贡献0.7。结果表明，写作侧记忆准入可通过轻量监督路由器独立学习，而回答生成保持为下游组件，实现高效、解耦的长程问答记忆管理。
