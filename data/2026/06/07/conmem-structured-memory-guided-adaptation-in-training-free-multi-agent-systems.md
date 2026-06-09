---
title: "ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems"
authors:
  - "Zhixun Tan"
  - "Qiang Chen"
  - "Tairan Huang"
  - "Xiu Su"
  - "Yi Chen"
date: "2026-06-07"
arxiv_id: "2606.08702"
arxiv_url: "https://arxiv.org/abs/2606.08702"
pdf_url: "https://arxiv.org/pdf/2606.08702v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "记忆管理"
  - "无训练适应"
  - "结构化记忆图"
  - "跨经验协调"
relevance_score: 8.5
---

# ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems

## 原始摘要

Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at https://anonymous.4open.science/r/ConMemCode

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决基于LLM的多智能体系统(MAS)在持续任务中的高效自适应问题。现有方法主要分为三类：记忆驱动方法（直接存储历史交互轨迹）存在轨迹长、噪声大、信号扭曲的问题；技能/程序驱动方法（抽象出可重用程序）在推理时缺乏关系感知的协调，无法解决策略冲突、依赖和冗余；训练驱动方法虽然效果好，但依赖额外训练或高质量监督，计算成本高。因此，核心问题是：如何在不进行额外训练的前提下，将多智能体系统积累的碎片化、噪声化的交互经验转化为结构化、可协调、可重用的集体记忆，以实现高效的自适应？ConMem通过引入“结构化记忆卡”和“关系感知记忆图”，在无需训练的情况下，实现了对历史经验的紧凑提取、有序组织和运行时协调，以克服现有方法的不足。

### Q2: 有哪些相关研究？

相关研究可分为三类：记忆增强方法（如Generative Agents、Voyager、MemoryEval、SimpleMem）将历史交互或反思直接作为记忆存储，但存在噪声大、缺乏结构化的问题，本文通过结构化记忆卡片提取可复用策略而非原始轨迹，提升了指导的简洁性；结构化与技能型方法（如MemP、MemSkill、G-Memory、ReMe）进一步将经验抽象为结构化表示，但侧重于存储和相关性检索，未考虑记忆间的关系协调，本文则构建关系感知的记忆图来显式解决策略冲突与依赖；学习与优化方法（如Memory-R1、MemRL、MemEvolve、LatentMem）通过强化学习或演化策略动态优化记忆使用，但通常需额外训练或修改宿主模型，本文在无需训练的条件下实现高效适配，避免了计算开销和系统定制。核心区别在于：ConMem首次在无训练条件下引入关系感知的跨经验协调机制，通过类型化记忆卡和预算剪枝，同时提升了适配鲁棒性与推理效率。

### Q3: 论文如何解决这个问题？

ConMem提出了一种结构化记忆引导的无训练多智能体适应框架，核心方法基于策略卡片（Strategy Card）和关系感知记忆图（Relation-Aware Memory Graph）。架构包含两大主要模块：读路径（Read Path）和写路径（Write Path）。

读路径由检索（Retrieval）、图扩展（Graph Expansion）、协调（Coordination）和预算组合（Budgeted Composition）四个阶段组成。首先，根据当前任务需求从记忆库中检索相关策略卡片，评分函数结合语义相似度、触发语义、需求匹配、可信度和效用得分，并采用最大边际相关性（MMR）去重。然后，通过记忆图（有向带权图，边类型包括支持、约束、满足、冲突）沿正向边进行分层扩展，最多L跳，冲突边会阻断扩展。协调阶段移除冗余卡片、解决局部冲突，最后在预算约束下序列化组合卡片形成记忆前缀，注入到智能体提示中。

写路径在任务完成后执行，包含反思（Reflection）、聚合（Aggregation）、准入（Admission）和合并（Merging）四个阶段。从交互轨迹中提取候选卡片，通过准入函数（评估可靠性、新颖性、时效性和预期效用，并检查一致性）筛选高质量卡片，同时将失败经验编码为负向卡片（提供避免信号）。准入后的卡片合并到记忆库中，并维护图结构的关系。

关键技术包括：利用策略卡片作为紧凑但结构化记忆单元的理论保障（基于充分性假设），通过符号化的正负卡片分别实现策略复用和失败规避，以及基于图扩展的关系感知协调机制。其创新点在于无需额外训练，仅通过提示端操作实现自适应，且能有效减少超过50%的候选扩展和80%以上的规划开销。

### Q4: 论文做了哪些实验？

论文在多任务基准和多个MAS架构上进行了实验。实验设置包括使用Qwen/Qwen3-4B-Instruct-2507作为共享LLM骨干，采用确定性解码，并评估了AutoGen（分布内宿主）、CAMEL和MacNet（未见宿主）三种MAS框架。

实验涵盖四个基准测试：TriviaQA和PopQA（知识密集型QA）、KodCode（代码生成）、PDDL via PDDLGym（符号规划）。对比方法包括无记忆基线、ChatDev、MetaGPT、JoyAgent、OAgents、Generative Agents、Voyager、SimpleMem、G-Memory、ReMe（动态）以及可学习记忆基线LatentMem。评估指标包括问答准确率、单元测试通过率和归一化规划分数。

主要结果显示，ConMem在所有宿主和基准上均实现了持续的正收益，相对于无记忆基线，跨宿主平均绝对提升在10.9到12.9个百分点之间。具体地，在AutoGen宿主上，ConMem在KodCode上达到80.80（提升12.40），在PDDL上达到27.90（提升11.51）。在15个宿主-指标对比中，ConMem排名第一8次，第二7次。消融实验表明，去除协调组件在TriviaQA上导致最大下降（CAMEL下降3.30），而去除图扩展在KodCode上伤害最大。此外，ConMem通过协调剪枝了超过50%的扩展候选，在规划任务上剪枝超过80%。

### Q5: 有什么可以进一步探索的点？

基于ConMem论文，以下几个方向值得深入探索：首先，当前structured memory cards的生成依赖预定义规则，未来可探索基于LLM的自动化知识蒸馏方法，以更动态地捕捉跨场景的可复用策略。其次，relation-aware memory graph的构建目前基于统计共现，可尝试引入因果推断或注意力机制，更准确地建模策略依赖与冲突关系。此外，论文主要在对话、编程等任务上验证，在实时决策、物理world modeling等复杂多智能体场景下的泛化性仍需检验。一个潜在改进是结合在线学习机制，让memory cards在推理时自适应更新，而非完全静态预置。最后，当智能体数量扩展至数百时，card图检索与协调的计算效率可能成为瓶颈，可探索分层压缩或稀疏化方法，平衡性能与开销。

### Q6: 总结一下论文的主要内容

ConMem提出了一个结构化内存引导的无训练多智能体系统自适应框架，旨在解决现有方法中轨迹噪声大、记忆-技能关系建模不足及依赖额外训练等问题。该框架将历史交互轨迹提炼为类型化、带符号的结构化记忆卡片，这些卡片编码了状态、计划、执行和评估信息，并被组织成关系感知的记忆图。在运行时，系统根据任务需求检索相关卡片，并通过卡片图协调以解决策略冲突和恢复依赖关系，最终在上下文预算下生成标准化的指导信息注入到冻结的主系统中。实验表明，ConMem在多个基准和主流MAS架构上均取得一致性能提升，同时通过裁剪超过50%的扩展候选和减少80%以上的规划开销，显著提高了推理效率。该工作的核心贡献在于将内存使用重新定义为在硬提示预算下对可重用策略的上下文控制，实现了轻量级、高效且无需额外训练的MAS自适应。
