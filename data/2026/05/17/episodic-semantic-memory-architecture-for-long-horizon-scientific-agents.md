---
title: "Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents"
authors:
  - "Nikola Milosevic"
date: "2026-05-17"
arxiv_id: "2605.17625"
arxiv_url: "https://arxiv.org/abs/2605.17625"
pdf_url: "https://arxiv.org/pdf/2605.17625v1"
categories:
  - "cs.AI"
tags:
  - "LLM科学Agent"
  - "长期记忆架构"
  - "情境记忆-语义记忆"
  - "双重过程记忆"
  - "长时任务"
  - "科学工作流"
  - "跨模型验证"
  - "记忆整合"
relevance_score: 9.0
---

# Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents

## 原始摘要

As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. Scientific workflows involving iterative data analysis and hypothesis refinement rapidly saturate even extended contexts with dense technical content, while monolithic approaches suffer from quadratic cost scaling and cognitive degradation. We evaluate a Dual Process Memory Architecture that decouples immediate episodic needs (constant 10-message window) from long-term consolidated knowledge (growing at approximately 3 tokens/message). Unlike prior social agent memory systems, our domain-specific consolidation addresses contradictory parameter evolution, multi-hop reasoning across experimental phases, and precise technical fact retention. Through large-scale evaluation spanning 15,000 messages with cross-model validation across six LLMs from three families (OpenAI, Anthropic, Google), totaling 1,440 queries, we establish three key findings. First, while full-context models fail at 10,000 messages due to context overflow, our system maintains 70-85% accuracy with 1-2 second latency using 62% fewer tokens (45,434 vs 120,000+ limit). Second, cross-model validation reveals architecture-level trade-offs independent of specific LLMs: Dual Process excels at numeric/temporal queries (65-90% accuracy) while RAG excels at historical retrieval (60-85%), suggesting complementary deployment strategies. Third, we identify a "Sim-to-Real" gap where synthetic tests maintain constant memory but realistic workflows exhibit linear growth (about 3 tokens/message), with consolidation quality emerging as the primary scalability bottleneck. The architecture successfully manages profiles with 14,000+ scientific facts (125k tokens), demonstrating that domain-specific memory consolidation enables sustained operation beyond full-context limits.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在长期科学协作中的**上下文窗口饱和**问题。研究背景是，LLM正被用于药物发现、基因组学等需要持续数周甚至数月的科学工作流中，这些工作流涉及迭代的数据分析与假设修正，产生大量密集的技术内容。现有方法存在显著不足：第一，即使拥有百万级token的扩展上下文窗口，全上下文模型面临**经济成本线性增长**（注意力机制呈二次方增长）和**认知退化**（相关信息被大量无关会话噪音淹没，即“迷失在中间”现象）的双重瓶颈；第二，传统基于RAG的历史检索方法在处理科学领域特有的记忆需求时表现不佳，例如需要追踪矛盾的参数演化（如p值阈值从p<0.05变为p<0.001）、跨实验阶段的多跳推理，以及精确的事实保留（如“178个样本”而非近似值）。因此，本文核心问题是设计一种**领域专属的长期记忆架构**，能够在超越全上下文限制的持续操作中（实验达15,000条消息），通过将即时情景记忆（恒定10条消息窗口）与长期巩固知识（约3 tokens/消息增长）解耦，以较低token消耗（节省62%）和1-2秒延迟维持70-85%的准确率，并系统性地解决科学工作流中的参数矛盾、多跳推理和精确事实保留这些独特挑战。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：一是基于LLM的记忆架构设计，如Park等人的Generative Agents采用三层记忆层次（观察、反思、检索）实现虚拟社交模拟，但本文指出其适用于行为合理性而非科学精度，且未解决矛盾参数更新和远距离推理问题。Packer等人的MemGPT借鉴操作系统虚拟内存，通过显式分页函数管理上下文，但本文采用隐式自动合并机制，无需LLM推理记忆操作，且以固定10条会话窗口保持近期状态，而MemGPT压缩任意上下文段落，缺乏时间连贯性。二是认知记忆理论的应用，如Cheng等人的MemoryBank通过外部知识检索增强常识推理，但缺乏时间感知，不适用于多轮对话中状态追踪（如当前阈值vs历史阈值）。三是提升长上下文能力的方法，包括上下文窗口扩展（如Ring Attention、Landmark Attention）和压缩技术（如RecurrentGPT、Chevalier等人方法），但本文强调这些方法侧重于近似无损文本生成，而非科学工作流所需的高精度事实检索与矛盾解决。此外，传统认知架构（ACT-R、Soar）和神经记忆网络（如神经图灵机）启发了本文的双过程设计，但前者依赖符号规则，后者在合成数据集上验证，未达到15,000消息规模。RAG方法擅长历史事实检索（80-85%准确率），但在近期状态查询上完全失败（0%），因余弦相似性无法区分时间优先级。

### Q3: 论文如何解决这个问题？

该论文提出了一种用于科学长周期任务的“双过程记忆架构”。核心是将记忆系统解耦为两个并行组件：**情景缓冲器**和**新皮层记忆**。在推理时，大型语言模型同时接收这两个组件的内容作为上下文。

**整体框架**上，情景缓冲器维护一个固定大小为10条消息的滑动窗口，保留原始、未压缩的近期对话，以确保代词消解和话语连贯性，并实现近因偏差，保持恒定复杂度。新皮层记忆则通过**增量整合**过程，动态增长地维护一个自然语言摘要，其中包含从完整对话历史中提取的事实、偏好和领域知识。这解决了长期记忆保持、语义压缩和知识积累的问题。

**核心创新点**在于其整合流程，它分为三个阶段：1. **情景到语义提取**：每次用户-智能体交互后，异步调用一个专门的LLM（如GPT-4o-mini），结合情景缓冲区、现有整合档案和最新消息，提取科学事实、参数、数据集和偏好，并进行矛盾检测。2. **冲突解决**：当检测到矛盾信息（如显著性阈值改变），系统通过时间优先规则，用最新信息覆盖旧值。3. **增量档案更新**：将更新后的档案替换新皮层记忆中的旧档案，无需每次都重处理整个历史，实现了高效扩展。

该架构的关键创新在于：通过将实时连贯性与长期事实分离，突破了全上下文方法的词元线性增长和成本二次方限制。实验证明，在超长对话（高达15,000条消息）中，它能在使用62%更少词元的情况下，维持70-85%的准确率，并仅有1-2秒延迟，成功实现了在超越上下文窗口极限情况下的持续科学协作。

### Q4: 论文做了哪些实验？

论文进行了大规模实验评估，涵盖多种设置、数据集、对比方法和关键结果。实验设置包括三个主要基准：真实生物医学对话（114条消息，含矛盾参数更新）、合成可扩展性测试（10到100,000条消息，测试“中间丢失”现象）和现实模拟（100到15,000条消息，各20个独立测量点）。对比方法包括Dual Process（10条消息的滑动窗口+约3 tokens/消息增长的新皮质记忆）、RAG（500-token分块、50-token重叠、FAISS索引）和Full Context（120,000-token滑动窗口截断）。主要结果：在30个消融任务中，Dual Process达到100%准确率和9.20分质量，而仅RAG为46.7%。合成测试中，Dual Process在100,000条消息下保持100%准确率（~820ms延迟，~180 tokens），而Full Context在50,000条消息后因窗口截断丢失中间事实（0%准确率）。现实模拟中，10,000条消息时Full Context崩溃，Dual Process保持85%准确率、约1,490ms延迟和30,096 tokens；15,000条消息时准确率70%、2,250ms延迟、45,434 tokens。跨查询类型实验显示，Dual Process在近期状态（75%准确率）和矛盾查询（20%）上优于RAG（0%），而RAG在历史检索（75%）和长期记忆（80%）上更好。跨模型验证（6个模型，共1,440次查询）证实Dual Process在近期状态上达到65-90%准确率，RAG在历史检索上60-85%，且该模式在所有模型家族中一致。消融实验发现，GPT-4o-mini和GPT-4o在合并质量上无显著差异（约23.7%准确率），且结构化提取更差（16.0%）。

### Q5: 有什么可以进一步探索的点？

论文中双过程架构在近期状态、矛盾检测与多跳推理等任务上显著优于RAG，但在历史检索和长期记忆任务上表现不佳（准确率30-40% vs RAG的60-85%），表明单纯的语义记忆难以独立应对长期科学工作流。未来可探索将RAG与双过程架构进行更细粒度的混合：例如，根据查询类型自适应路由——用RAG处理静态事实检索，用情景-语义记忆处理动态推理任务。此外，本文发现记忆整合质量是首要瓶颈，且模型容量（GPT-4o vs mini）无显著差异，暗示提示工程已到天花板。下一步可改进基于图或概率逻辑的知识表示与更新机制，以支持矛盾消解与参数演化。同时，仅依赖跨模型验证不足以揭示架构普适性，需在更复杂的多智能体协作和开放域科学研究场景下验证其泛化能力。最后，当前无法处理可编辑/遗忘的用户偏好，可引入可控记忆修正机制以适配实际科学发现中的迭代性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向长时科学智能体的双过程记忆架构（Dual-Process Memory Architecture），旨在解决大语言模型在长期科学协作中因上下文窗口饱和导致的性能瓶颈。该方法将短期情景记忆（恒定的10条消息窗口）与长期语义记忆（通过增量压缩形成的动态增长摘要）分离，以低于全上下文62%的token消耗（在1.5万条消息中约4.5万token）和1-2秒延迟，将准确率维持在70-85%。在跨越六大语言模型（来自OpenAI、Anthropic、Google）的1,440次查询验证中，研究发现了架构层面的根本性权衡：双过程架构擅长数值/时间类动态查询（65-90%准确率），而RAG擅长静态历史检索（60-85%），这表明两者是互补策略。核心贡献在于，其证明了领域特定的记忆整合机制是让智能体突破全上下文限制并实现持续运行的关键瓶颈。
