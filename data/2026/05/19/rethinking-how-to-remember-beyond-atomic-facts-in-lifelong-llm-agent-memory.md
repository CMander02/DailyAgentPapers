---
title: "Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory"
authors:
  - "Jingwei Sun"
  - "Jianing Zhu"
  - "Jiangchao Yao"
  - "Tongliang Liu"
  - "Bo Han"
date: "2026-05-19"
arxiv_id: "2605.19952"
arxiv_url: "https://arxiv.org/abs/2605.19952"
pdf_url: "https://arxiv.org/pdf/2605.19952v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent Memory"
  - "Lifelong Learning"
  - "Memory Architecture"
  - "Prompt Optimization"
  - "Multi-granularity Memory"
  - "Dialogue History"
  - "TextGrad"
relevance_score: 9.5
---

# Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory

## 原始摘要

To enable reliable long-term interaction, LLM agents require a memory system that can faithfully store, efficiently retrieve, and deeply reason over accumulated dialogue history. Most existing methods adopt an extracted fact based paradigm: handcrafted static prompts compress raw dialogues into atomic facts, which are then stored, matched, and injected into downstream reasoning. Nevertheless, such fact-centric designs inevitably discard fine-grained details in original dialogues and fail to support deep reasoning over scattered isolated facts. Moreover, static prompts cannot maintain consistent extraction granularity across diverse dialogue styles. To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning. We further adopt TextGrad-based prompt optimization, which iteratively refines extraction and profiling prompts via response quality feedback, achieving lifelong evolution without any parameter updating. Extensive experiments on LoCoMo and PerLTQA across multiple LLM backbones demonstrate that TriMem consistently outperforms strong memory baselines. The code is available at https://TMLR-TriMem.github.io .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前LLM智能体记忆系统在长期交互中面临的关键问题。研究背景指出，尽管LLM在多种场景下表现出色，但受限于上下文窗口容量，长对话中历史信息丢失和上下文逻辑断裂会严重限制智能体的性能。现有方法普遍采用基于“原子事实”的范式：通过静态手工设计的提示词，将原始对话压缩提取为孤立的事实进行存储、检索和推理。然而，这种设计存在三个根本性不足：第一，存储有损，事实提取必然丢弃原始对话中的细粒度细节（如修饰词），导致信息永久缺失；第二，推理浅层化，系统仅能回答依赖单条事实的简单问题，对于需要整合分散信息进行深度理解（如情感推断、逻辑归纳）的多证据问题表现极差；第三，提示词僵化，静态的固定提示词无法适应真实世界对话风格的多样性（如显式/隐式表达），造成提取粒度不一致。核心问题在于，现有记忆系统无法同时保证存储保真度、检索效率和推理深度。为此，本文提出TriMem架构，通过维护原始对话片段、提取事实和综合轮廓三种共存表示粒度，并利用TextGrad自动优化提示词，以实现高保真存储、高效检索和深度推理的统一。

### Q2: 有哪些相关研究？

相关研究主要分为两个方向：

1. **LLM Agent记忆系统**：现有方法（如Mem0、A-Mem、MemoryOS）遵循“提取事实-存储-检索-推理”的三阶段范式，核心是将原子事实作为所有阶段的统一基本单元。这类方法依赖于手工静态提示压缩对话为事实，但会丢失原始对话的细粒度细节，且难以支持跨散落孤立事实的深度推理。与之不同的是，本文提出TriMem，在存储阶段保留原始对话片段以确保保真度，在检索阶段使用原子事实实现高效匹配，在推理阶段构建实体画像支持整体理解。本文强调三阶段不应孤立设计，而应采用一致的多级表示管道。

2. **终身演化Agent**：一类方法将记忆管理建模为强化学习问题（如MemAgent、MemBuilder、AgentFold、MEM1），但需要参数更新，训练成本高且不适用于仅API可访问的模型。另一类方法无需参数更新（如Voyager、ExpeL、MemSkill），通过维护技能库或规则实现演化。本文属于后者，但创新性地应用TextGrad优化提取和画像提示，通过响应质量反馈实现提示的终身演化。与聚焦动作空间的技能/规则外化不同，本文的提示级演化直接重塑原始经验如何解析为记忆，更适合由提示而非固定策略网络主导行为的记忆系统。

### Q3: 论文如何解决这个问题？

针对现有基于事实的终身记忆系统存在的存储有损（丢弃原始对话细节）和推理浅层（无法对分散孤立的事实进行深度推理）两大问题，TriMem提出了一个多粒度联合记忆框架。其核心是构建三层并存表示：首先，通过滑动窗口将原始对话分段，并在事实提取时额外抽取源对话标识符（source identifier）作为锚点，确保存储保真度；其次，保留传统的原子事实用于高效检索匹配；最后，按人物将分散事实聚合并通过简档提示（profile prompt）合成结构化、多维度的人物简档，捕获身份属性、性格、人际关系等综合语义，支撑深层理解式推理。这三层通过索引关联，使得检索时不仅能找到事实，还能通过源标识符恢复完整对话片段，通过人物标识符获取综合简档，从而兼顾检索效率与推理深度。此外，为应对静态提示无法适应多样化对话风格的问题，TriMem引入TextGrad进行无参数更新的终身提示优化：将事实提取提示和简档提示作为可优化参数，根据下游问答任务的生成质量（由LLM裁判评估）计算文本梯度，即LLM提供的自然语言修改建议，通过迭代地应用这些建议来动态调整提示。整个过程无需对LLM本身进行微调，实现了提取粒度与理解能力的持续演化。实验表明TriMem在多个基准和LLM骨干上显著超越基线方法，且token消耗合理。

### Q4: 论文做了哪些实验？

论文在LoCoMo和PerLTQA两个基准上进行了全面实验。对比方法包括Naive RAG、Mem0、MemoryOS、A-Mem、LightMem、SimpleMem和xMemory等主流记忆系统。主要实验设置：窗口大小40、步长38，使用Qwen3-embedding-0.6b模型编码提取的事实，检索条目上限25，提示词优化轮次4轮。

在PerLTQA基准上，TriMem使用Qwen3-8B在Profile(92.46%)、Social Relationship(83.23%)、Events(85.72%)和Dialogues(55.79%)四个子任务上均取得最优结果，显著优于Mem0、LightMem等方法。在高能力模型(GPT-4o等)上也持续领先，且仅消耗约1.2k tokens。

消融实验表明：移除实体概要或原始对话模块会导致性能显著下降；演化步数设为4时最优，步数过多反而导致性能退化；检索条目数25为最佳平衡点；引入搜索查询虽然增加检索时间但大幅提升检索准确率；窗口大小设为40可在性能和效率间取得良好平衡。

### Q5: 有什么可以进一步探索的点？

基于当前研究，未来可从以下方向深入探索：首先，TriMem依赖TextGrad优化提示词，但若对话分布发生剧烈漂移或出现全新交互模式，迭代优化可能收敛缓慢甚至失效，可引入在线元学习或增量式提示适配机制，以提升对动态环境的鲁棒性。其次，当前记忆粒度包含原始片段、原子事实和合成档案，但三者间的融合与冲突解决仍显粗糙——例如事实与档案可能矛盾，未来可设计动态可信度评分或图结构推理，实现跨粒度一致性校验。此外，实验仅在LoCoMo和PerLTQA两个基准上验证，缺乏对长尾实体、多模态对话或协作型多智能体场景的测试，建议构建包含时序推理与反事实记忆的新基准。最后，记忆的遗忘机制尚未明确，可借鉴认知科学中的间隔重复或经验衰退模型，使系统能自适应清除冗余信息，降低检索复杂度。

### Q6: 总结一下论文的主要内容

这篇论文重新审视了终身学习型LLM代理的记忆系统设计，指出现有基于原子事实的范式存在三大缺陷：有损存储、浅层推理以及异构对话风格下的次优提示。为解决这些问题，作者提出了TriMem记忆系统，其核心贡献在于维护三种共存的表示粒度：原始对话片段（保证存储保真度）、提取的原子事实（保证检索效率）以及合成的用户/情境画像（促进深层推理）。此外，系统采用基于TextGrad的提示优化方法，通过下游响应质量反馈迭代地改进事实提取和画像构建的提示，实现无需更新模型参数的终身适应。在LoCoMo和PerLTQA基准上的大量实验表明，TriMem在多种LLM骨干上均显著优于强基线方法。该工作的意义在于打破了原子事实范式的局限，通过多粒度表示实现存储、检索与推理间的更好平衡，并提供了轻量级、可适用于仅API模型的适应性机制。
