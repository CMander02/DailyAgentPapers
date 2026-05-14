---
title: "Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue"
authors:
  - "Vardhan Dongre"
  - "Dilek Hakkani-Tür"
date: "2026-05-13"
arxiv_id: "2605.12920"
arxiv_url: "https://arxiv.org/abs/2605.12920"
pdf_url: "https://arxiv.org/pdf/2605.12920v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体协作"
  - "世界模型对齐"
  - "具身Agent通信"
  - "LLM Agent"
  - "对话交流"
  - "PARTNR基准"
relevance_score: 8.5
---

# Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue

## 原始摘要

Effective collaboration between embodied agents requires more than acting in a shared environment; it demands communication grounded in each agent's evolving understanding of the world. When agents can only partially observe their surroundings, coordination without communication is provably hard, but communication can, in principle, bridge this gap by allowing agents to share observations and align their world models. In this work, we examine whether LLM-based embodied agents actually realize the ability to communicate. We extend PARTNR, a benchmark for collaborative household robotics, with a natural-language dialogue channel that enables two agents with partial observability to communicate during task execution. To evaluate whether dialogue leads to genuine world-model alignment rather than superficial coordination, we propose a framework for measuring world-model alignment defined over per-agent world graphs: observation convergence (do private world models align over time?), information novelty (do messages convey what the partner lacks?), and belief-sensitive messaging (do agents model what their partner knows?). Our experiments across three LLMs reveal that dialogue reduces action conflicts 40 to 83 percentage points but degrades task success relative to silent coordination. Using our metrics, we characterize the gap between superficial coordination and genuine world-model alignment, and identify where current models fall on this spectrum.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文探讨的是具身多智能体系统中，通过自然语言对话实现世界模型对齐的问题。研究背景是，在部分可观测的物理环境中，多个具身智能体（如家用机器人）的有效协作不仅需要共享环境行动，更需要基于各自对世界不断演化的理解进行沟通。现有方法的不足在于，虽然理论上通过通信可以弥补部分可观测性带来的协作困难，将难以处理的分散式规划问题简化为集中式规划，但目前基于大语言模型（LLM）的具身智能体在通信时，其对话是否真正实现了有意义的世界模型对齐，而非仅仅是表面上的协调，尚未得到验证。现有的多智能体协作基准测试大多只报告任务成功率，不深入分析通信内容是否促进了对齐。因此，本文要解决的核心问题是：当两个LLM驱动的具身智能体通过自然语言对话在物理环境中协作时，它们是否尝试在交流中真正对齐各自对世界的理解（即世界模型），还是仅仅表现出表面上看似协调的行为。为此，作者扩展了PARTNR基准测试，引入对话通道，并提出了衡量世界模型对齐的诊断框架，包括观测收敛性、信息新颖性和信念感知通信等指标，以区分真实对齐与表面协作。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**理论框架类**、**人机对话协作类**和**具身多智能体评测类**。

**理论框架类**方面，本文建立在Dec-POMDP（去中心化部分可观测马尔可夫决策过程）的理论基础上，指出无通信时多智能体协作是NEXP-complete的，而通过有效通信可降为PSPACE-complete（如Amato & Zilberstein的工作）。与这些纯理论工作不同，本文首次将理论上的"通信降低计算复杂度"落实为对LLM具身智能体对话中"心智模型对齐"的实际测量。

**人机对话协作类**方面，相关工作探讨了LLM在文本基准测试中的心智理论（Theory of Mind）能力（如Sap et al.）。本文与这些工作的核心区别在于：现有研究主要在纯文本或问答场景中评估LLM的心智理论能力，而本文将其置于物理家务协作环境中，验证对话是否能真正对齐世界模型，而非仅表面协调。

**具身多智能体评测类**方面，已有工作如PARTNR（本文扩展的基准）、Habitat和ALFRED等评测了多智能体任务成功率，但大多未分析通信质量。本文的创新在于超越了任务成功率指标，提出了世界图收敛、信息新颖性和信念敏感消息三个对齐度量，揭示了对话减少行动冲突（40-83个百分点）却降低任务成功率的矛盾现象。

### Q3: 论文如何解决这个问题？

为了解决部分可观测环境下的多智能体协调问题，论文提出了一种基于自然语言对话的世界模型对齐框架。核心方法是在PARTNR基准上扩展一个对话通道，让两个异构具身智能体（四足机器人与类人机器人）在执行任务时能够交换信息。整体框架采用ReAct规划范式，每个智能体拥有独立的LLM规划器，维护各自的私有世界图（层次化场景表示），通过对话通道共享观察以对齐认知。

架构设计上，论文提出了两种通信架构：同步-代价型（SC）将发送消息作为一个消耗步骤预算的行动，与物理动作竞争资源；异步-无代价型（ACF）则允许智能体在单个LLM调用中同时输出消息和动作，消息不消耗预算。关键技术包括：基于Jaccard相似度定义观察收敛度（OC）和信念收敛度（BC）来量化世界模型对齐程度；引入信息新颖度（IN）衡量每条消息是否传递了接收方未观察到的实体；提出信念敏感消息传递（BSM）指标，通过对比随机基线来检测发送方是否优先选择接收方缺失的信息。创新点在于将对话的效果从任务成功率中解耦出来，通过对齐差距（Δ_align = BC - OC）区分真实世界模型对齐与表面协调。实验表明，对话能减少40-83个百分点的行动冲突，但降低了任务成功率，说明当前模型存在表面协调而非真正的世界模型对齐。

### Q4: 论文做了哪些实验？

论文在PARTNR基准测试的协作家居任务上进行了实验，使用自然语言对话通道让两个部分可观察的智能体通信。实验设置了四种条件：静默基准（无对话）、同步代价（SC，默认稀疏提示）、SC*（主动鼓励对话）和异步无代价（ACF，将通信作为一等行动）。评估了Sonnet、Haiku和Mistral-L三种LLM。

主要结果：对话使动作冲突降低40-83个百分点（Sonnet上SC降低93%），但任务成功率全面下降。在80集子集上，Sonnet的ΔSR=-0.100，Haiku的ΔSR=-0.368，Mistral-L的ΔSR=-0.050（p<0.01）。ACF虽增加3.5倍通信量（13.35轮/集），ΔSR仍为-0.11。通过诊断指标发现，对话导致的世界模型对齐Δalign为负值（SC下-0.15），但排除幻觉引用后Δalign_grounded转为正值（+0.19），表明60-69%的对话包含幻觉内容。信念敏感消息指标显示ACF下BSM从-0.085恶化到-0.232，自由通信导致重复性状态更新而非信息传递。轨迹分析表明初始正向对齐随时间衰减为负值。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在对对话内容的浅层分析上，仅将对话视为共享信念状态上的策略，忽略了词汇选择、信息包装、话轮转换等语言特征，未来可结合语义解析或人工标注研究这些语言维度对协调的影响。在评测方面，虽用确定性方法保证可重复性，但也牺牲了灵活性，可探索更丰富的世界图对齐度量，如动态环境下的观测收敛速率或多轮反事实推理。此外，实验发现LLM的对话存在特定失效模式：幻觉内容不对称地膨胀信念，导致看似减少冲突实则损害任务成功。未来改进方向包括：在训练中引入物理实体约束和部分可观测性，例如利用环境反馈实现自洽校验；设计反错觉机制，让模型主动区分共享与私密信息；或采用互信息最大化的对话策略来促进真正对齐而非表面协调。这些改进还能与多智能体仿真、人机交互等场景结合。

### Q6: 总结一下论文的主要内容

该论文研究了具身多智能体协调中，通过对话实现世界模型对齐的问题。定义问题是：在部分可观察环境下，LLM驱动的具身智能体能否通过自然语言对话实现真正世界模型对齐，而非表面协调。方法上，在PARTNR家务协作基准中引入对话通道，并构建评估框架，通过观测收敛性（私有世界模型是否随时间对齐）、信息新颖性（消息是否传递对方缺失信息）和信念敏感消息（智能体是否建模对方知识）三个指标衡量对齐程度。实验发现，对话使动作冲突降低40-83个百分点，但任务成功率反而低于无对话场景。核心结论是：当前LLM智能体的对话内容存在幻觉和预测性引用，无法有效对齐信念，导致表面协调与实际理解存在差距，揭示了对话内容瓶颈并指出未来设计方向（如持久共识、信念建模、结构化语言行为）。该工作系统性诊断了具身对话中的对齐问题，具有重要意义。
