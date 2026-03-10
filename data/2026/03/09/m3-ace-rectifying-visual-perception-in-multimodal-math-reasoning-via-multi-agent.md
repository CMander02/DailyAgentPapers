---
title: "M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering"
authors:
  - "Peijin Xie"
  - "Zhen Xu"
  - "Bingquan Liu"
  - "Baoxun Wang"
date: "2026-03-09"
arxiv_id: "2603.08369"
arxiv_url: "https://arxiv.org/abs/2603.08369"
pdf_url: "https://arxiv.org/pdf/2603.08369v1"
categories:
  - "cs.AI"
tags:
  - "Multimodal Agent"
  - "Multi-Agent Collaboration"
  - "Visual Perception"
  - "Mathematical Reasoning"
  - "Context Engineering"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering

## 原始摘要

Multimodal large language models have recently shown promising progress in visual mathematical reasoning. However, their performance is often limited by a critical yet underexplored bottleneck: inaccurate visual perception. Through systematic analysis, we find that the most failures originate from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability. Moreover, models tend to remain overly confident in their initial perceptions, making standard strategies such as prompt engineering, multi-round self-reflection, or posterior guidance insufficient to reliably correct errors.
  To address this limitation, we propose M3-ACE, a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. Instead of directly aggregating final answers, our approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. Multiple agents collaboratively contribute complementary observations, enabling the system to expose inconsistencies and recover missing perceptual information. To support stable multi-turn collaboration, we further introduce two lightweight tools: a Summary Tool that organizes evidence from different agents into consistent, complementary, and conflicting components, and a Refine Tool that filters unreliable samples and guides iterative correction.
  Extensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. Our method establishes new state-of-the-art results 89.1 on the MathVision benchmark and achieves consistent improvements on other related datasets, including MathVista and MathVerse. These results highlight the importance of perception-centric multi-agent collaboration for advancing multimodal reasoning systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在视觉数学推理任务中因视觉感知不准确而导致的性能瓶颈问题。研究背景在于，尽管现有模型在视觉数学推理（如数学图表理解）方面已取得显著进展，但它们在面对细微的感知模糊性、噪声视觉证据或复杂图表表示时仍表现脆弱。现有方法（如提示工程、多轮自我反思或后验指导）通常假设模型能够自主纠正错误，但论文通过系统分析发现，这些方法存在根本不足：模型失败主要源于视觉证据提取的错误或不完整，而非推理能力缺陷；且模型对初始感知结果表现出过度自信，导致标准策略难以可靠纠正错误。

本文要解决的核心问题是：如何有效纠正多模态数学推理中的视觉感知错误，以提升整体推理性能。为此，论文提出了M³-ACE框架，通过多智能体上下文工程来解耦感知与推理，动态维护以视觉证据列表为中心的共享上下文，使多个智能体协作提供互补观察，从而暴露不一致性并恢复缺失的感知信息。该方法避免了依赖单一模型的自我修正，转而通过结构化多智能体交互实现交叉验证和迭代优化，从根本上突破了现有方法在纠正视觉证据错误上的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为评测基准和方法框架两类。

在评测基准方面，**MathVista** 是首个综合性基准，整合了多个数据集以评估多模态数学推理。**MathVerse** 通过“视觉消融”设计，能诊断模型是否真正利用了视觉信息。**MathVision** 则专注于竞赛级难题，代表了该领域的难度上限。本文的工作正是在这些基准上进行评估，并指出当前模型存在“模态惰性”、细粒度视觉感知不足以及复杂推理链整合困难等挑战，而本文提出的方法正是为了直接应对这些瓶颈。

在方法框架方面，**Agentic Context Engineering (ACE)** 是一种将大语言模型视为处理器、并通过管理上下文窗口来执行任务的范式，其操作包括写入、选择、压缩和隔离。相关技术从思维链（CoT）发展到ReAct和Reflexion，并有LangChain、AutoGPT等框架实现。与需要更新模型权重的监督微调（SFT）或RLHF等方法相比，ACE具有高效、灵活、可解释和可控的优势。本文的M³-ACE框架属于多模态ACE范畴，其核心创新在于**将感知与推理解耦**，并通过**多智能体协作**来维护和修正共享的视觉证据列表，从而直接针对现有ACE方法在纠正错误视觉感知方面的不足。这与传统单智能体的自我反思或后验引导策略有显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为M³-ACE的多智能体上下文工程框架来解决多模态数学推理中视觉感知不准确的核心瓶颈。该方法的核心思想是将感知与推理解耦，并通过多智能体的协作与迭代精炼来纠正和补充初始的视觉证据。

整体框架基于三个设计原则：解耦原则、互补信息原则和过滤原则。系统主要由一个锚定智能体、多个异构的辅助智能体以及两个轻量级辅助工具（摘要工具和精炼工具）构成。流程分为三个主要步骤：首先，在多智能体初始化阶段，锚定智能体和辅助智能体独立生成包含视觉证据列表和最终答案的结构化响应，其中辅助智能体的上下文被冻结作为参考。其次，在上下文摘要与再生阶段，摘要工具将来自各智能体的视觉证据列表汇总并分类为一致、互补和冲突三组；锚定智能体基于此分类摘要，再生出更新的视觉证据列表和答案。最后，在精炼与过滤阶段，精炼工具会评估新答案与先前答案的一致性以及更新上下文中冲突视觉证据的比例，将那些答案分歧大且冲突比例高的样本拒绝并送回上一步进行迭代精炼，直至达到预定的选择比例阈值。

其关键技术在于两个辅助工具的设计。摘要工具通过轻量级智能体结合硬逻辑规则，对视觉证据进行结构化分类并计算冲突比率，为精炼提供量化信号。精炼工具则综合答案一致性与冲突比率，实施两阶段过滤，确保系统资源集中在感知模糊和存在争议的困难样本上，从而高效稳定地维护多轮协作的共享上下文。

创新点主要体现在：1）通过多智能体协作和动态维护的共享视觉证据上下文，显式地针对并纠正感知错误，而非直接聚合最终答案；2）引入摘要与精炼工具，以轻量且稳定的方式支持迭代过程，有效减少了确认偏见和冗余计算；3）整个方法不改变基础模型参数，是一种高效的上下文工程策略，显著提升了多个数学推理基准上的性能。

### Q4: 论文做了哪些实验？

实验设置方面，论文构建了两个不同能力级别的多智能体集合：SOTA集合包含Gemini-3 Pro、Gemini-2.5 Pro、GPT-5和Claude-4.5 Sonnet四个先进的多模态大语言模型；子SOTA集合则移除了其中最强和最弱的模型。在推理过程中，轮流指定每个模型为锚点智能体，其余作为辅助智能体，并引入了摘要工具和精炼工具来组织证据与筛选样本。

使用的数据集/基准测试主要包括MathVision、MathVista和MathVerse，其中MathVision是核心评估基准。对比方法涉及单智能体思维链推理与多智能体答案直接聚合等基线。

主要结果上，M³-ACE在MathVision基准上取得了新的最先进结果，整体准确率达到89.1%。关键数据指标显示，在SOTA集合中，经过第一轮“带摘要的重新生成”后，各锚点模型准确率相比单智能体推理均有提升：Gemini-3 Pro提升3.1点至88.1%，Gemini-2.5 Pro提升7.2点至80.5%，GPT-5提升9.3点至81.3%，Claude-4.5 Sonnet提升14.8点至76.0%。随后的精炼阶段筛选出的高置信度子集准确率接近90%（如Gemini-3 Pro对应子集达92.7%），而被拒绝的样本准确率则低30点以上。在反思阶段，困难样本经过多轮修正后，Gemini-3 Pro准确率进一步提升10.8点，Gemini-2.5 Pro提升9.4点。论文还通过消融研究验证了性能提升与视觉感知错误纠正强相关，且基于视觉证据列表的上下文工程优于直接的答案级聚合。

### Q5: 有什么可以进一步探索的点？

该论文提出的M³-ACE框架虽在视觉感知纠偏上取得进展，但仍存在一些局限和可拓展方向。首先，其多智能体协作主要聚焦于静态图像中的数学问题，未来可探索动态或连续视觉场景（如视频推理）中的感知修正，这对时序一致性和跨帧证据整合提出了更高要求。其次，当前框架依赖人工设计的摘要与精炼工具，未来可引入强化学习或元学习，让智能体自主优化协作策略与工具使用逻辑，提升自适应能力。此外，研究仅验证了数学推理任务，该感知协同机制能否迁移到科学图解、图表分析等更广泛的跨模态任务中，值得进一步验证。最后，框架的计算开销较大，如何通过智能体剪枝、证据压缩等轻量化设计平衡性能与效率，也是实际部署的关键挑战。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型在视觉数学推理任务中存在的视觉感知瓶颈问题，提出了一种名为M³-ACE的多智能体上下文工程框架。核心问题是模型性能受限的主要原因并非推理能力不足，而是初始视觉证据提取不准确或不完整，且模型对初始感知结果过于自信，导致传统提示工程、自我反思或后验指导等方法难以有效纠错。

为解决此问题，M³-ACE的核心方法是将感知与推理过程解耦，通过多个智能体协作动态维护一个以视觉证据列表为中心的共享上下文。多个智能体提供互补的观察，从而暴露不一致性并恢复缺失的感知信息。为了支持稳定的多轮协作，框架引入了两个轻量级工具：总结工具用于将不同智能体的证据组织成一致、互补和冲突的部分；精炼工具则用于过滤不可靠样本并指导迭代修正。

实验结果表明，该方法显著提升了多个基准测试上的视觉数学推理性能，在MathVision基准上取得了89.1分的新的最先进结果，并在MathVista和MathVerse等相关数据集上取得了一致性提升。论文的主要贡献在于揭示了感知中心的多智能体协作对于推进多模态推理系统的重要性，为解决视觉感知错误这一关键瓶颈提供了有效且通用的框架。
