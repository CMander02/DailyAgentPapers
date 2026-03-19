---
title: "Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding"
authors:
  - "Haiyang Yan"
  - "Hongyun Zhou"
  - "Peng Xu"
  - "Xiaoxue Feng"
  - "Mengyi Liu"
date: "2026-03-18"
arxiv_id: "2603.17307"
arxiv_url: "https://arxiv.org/abs/2603.17307"
pdf_url: "https://arxiv.org/pdf/2603.17307v1"
github_url: "https://github.com/Haiyang0226/Symphony"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Long-Video Understanding"
  - "Cognitive-Inspired"
  - "Reasoning"
  - "Task Decomposition"
  - "Video Grounding"
  - "VLM Agent"
relevance_score: 8.0
---

# Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding

## 原始摘要

Despite rapid developments and widespread applications of MLLM agents, they still struggle with long-form video understanding (LVU) tasks, which are characterized by high information density and extended temporal spans. Recent research on LVU agents demonstrates that simple task decomposition and collaboration mechanisms are insufficient for long-chain reasoning tasks. Moreover, directly reducing the time context through embedding-based retrieval may lose key information of complex problems. In this paper, we propose Symphony, a multi-agent system, to alleviate these limitations. By emulating human cognition patterns, Symphony decomposes LVU into fine-grained subtasks and incorporates a deep reasoning collaboration mechanism enhanced by reflection, effectively improving the reasoning capability. Additionally, Symphony provides a VLM-based grounding approach to analyze LVU tasks and assess the relevance of video segments, which significantly enhances the ability to locate complex problems with implicit intentions and large temporal spans. Experimental results show that Symphony achieves state-of-the-art performance on LVBench, LongVideoBench, VideoMME, and MLVU, with a 5.0% improvement over the prior state-of-the-art method on LVBench. Code is available at https://github.com/Haiyang0226/Symphony.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视频理解任务中现有方法面临的严峻挑战。随着视频时长增加，信息密度和问题复杂性急剧上升，对多模态理解和逻辑推理提出了更高要求。尽管基于多模态大语言模型的智能体已成为主流范式，但它们在处理长序列输入和复杂任务时，指令遵循和推理能力会显著下降。

现有方法主要存在两大不足。一方面，基于检索增强生成的方法通过构建视频数据库来提取相关片段，但难以从复杂问题中生成有效的检索查询，且视频内容中的噪声和冗余会损害检索准确性，直接基于嵌入的检索还可能丢失关键信息。另一方面，基于任务分解和多步工具调用的方法将推理完全委托给核心大语言模型，当任务复杂度超出模型能力时性能会大幅退化。此外，现有的多智能体系统虽能分解任务，但存在跨模态信息交换困难或采用线性协作管道等问题，限制了推理过程中的任务探索空间，未能突破单智能体的能力局限。

因此，本文的核心问题是：如何设计一个有效的多智能体系统，以克服长视频理解中存在的**推理能力不足**和**视频片段定位不准**两大瓶颈。为此，论文提出了Symphony系统，其核心解决方案是：1）受人类认知模式启发，将长视频理解任务按功能维度分解给专门化的智能体，并通过反思增强的动态协作机制来提升系统整体推理能力；2）引入一个结合大语言模型与视觉语言模型的定位智能体，以深度理解问题语义并实现更精准的视频片段相关性评估，从而应对具有隐含意图和大时间跨度的复杂问题定位。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**长视频理解方法**、**多智能体系统设计**以及**认知启发式推理**三大类别。

在**长视频理解方法**方面，现有工作常采用基于嵌入的检索来缩减时间上下文，但本文指出这可能导致复杂问题关键信息的丢失。与之相比，Symphony 提出了一种基于视觉语言模型（VLM）的定位方法，以分析任务并评估视频片段的相关性，从而更精准地定位具有隐含意图和大时间跨度的复杂问题。

在**多智能体系统设计**方面，近期研究显示，简单的任务分解与协作机制难以胜任长链推理任务。本文提出的 Symphony 系统通过模仿人类认知模式，将长视频理解分解为细粒度子任务，并引入了由反思增强的深度推理协作机制，显著提升了系统的推理能力。

在**认知启发式推理**方面，相关工作多集中于单一代理的规划或反思。Symphony 的创新之处在于将这种认知模式系统性地整合到一个多智能体框架中，实现了更接近人类的问题解决流程。实验表明，该方法在多个基准测试上取得了领先性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Symphony的多智能体系统来解决长视频理解任务中的挑战。其核心方法是受人类认知模式启发，将复杂的LVU任务分解为细粒度的子任务，并通过一个由反思增强的深度推理协作机制来协调多个功能专一的智能体。

整体框架包含五个主要智能体：规划智能体作为中央协调器，负责全局任务规划、调度其他智能体、整合信息并生成最终答案；视觉感知智能体执行多维视觉感知，调用帧检查、全局摘要和多片段分析等工具；字幕智能体处理视频字幕并进行语义分析，实现实体识别、情感分析等功能；创新性地提出了一个基于VLM的定位智能体，它通过分析查询的复杂性，自适应地选择基于VLM的相关性评分工具或基于CLIP的检索工具，以高效定位与问题相关的视频片段；反思智能体则对推理轨迹进行回顾性评估，检测逻辑不一致或证据不足的情况，并生成纠正建议以启动新一轮的优化。

关键技术体现在两个方面。一是**反思增强的动态推理框架**：该框架受Actor-Critic启发，将规划智能体视为策略模型（π），负责生成子任务指令；将反思智能体视为验证模型（φ），负责验证推理过程和结果。通过算法1所示的迭代过程，在正向推理阶段，规划智能体基于当前状态（问题和历史轨迹）动态选择下一个子任务（如定位、视觉感知或字幕分析），由相应智能体执行并更新状态，直至积累足够证据形成答案。在验证阶段，反思智能体评估推理的严谨性，若发现问题则生成批判性建议并更新状态，重新触发规划智能体的推理，从而显著扩展了多智能体系统的探索空间，提升了复杂问题的解决能力。

二是**创新的基于VLM的定位方法**：针对长视频任务中常见的查询模糊性和多跳推理需求，定位智能体利用LLM对原始查询进行分析、扩展和精炼，生成增强后的查询。然后，它使用视觉语言模型（VLM）根据预定义的评分标准（如表所示，将相关性分为4个等级），并行评估每个视频片段与增强查询的语义相关性，输出分数及推理依据。这种方法相比直接使用CLIP进行检索，能更好地捕捉抽象概念、动作序列和隐含意图，从而更全面、准确地定位具有大时间跨度的复杂问题所涉及的关键片段。系统通过这种认知维度解耦的范式，最小化了智能体间的耦合度，降低了信息整合成本，最终在多个基准测试中取得了最先进的性能。

### Q4: 论文做了哪些实验？

论文在四个代表性长视频理解数据集上进行了全面实验。实验设置方面，Symphony 系统使用了 DeepSeek R1 作为规划和反思智能体的推理模型，DeepSeek V3 作为字幕智能体，Doubao Seed 1.6 VL 作为视觉感知和定位智能体的视觉语言模型。输入序列限制为最多40帧，分辨率上限为720p。对于基于VLM的评分工具，设置时长T=60秒并从每个片段采样30帧。智能体调度轮次和每个智能体内最大工具调用次数设为15，反思智能体的最大调度轮次设为3。

使用的数据集/基准测试包括：LVBench（平均时长68分钟，涵盖时序定位、摘要、推理等六个核心能力维度）、LongVideoBench（3763个视频，包含指代推理任务）、MLVU（包含推理、描述、识别等九类任务）以及Video-MME（使用其“长”时长子集评估时空复合推理能力）。

对比方法涵盖了多类先进方法：包括商业VLMs（Gemini-1.5-Pro, GPT-4o, OpenAI o3）、开源VLMs（InternVL2.5-78B, Qwen2.5-VL-72B）、基于智能体的框架（VideoTree, VideoAgent, MR. Video, DVD）、长上下文方法LongVILA、基于检索增强生成的方法VideoRAG以及基于令牌压缩的方法AdaRETAKE。

主要结果如下：Symphony 在所有基准测试上均取得了最先进的性能。在最具挑战性的LVBench上，其总体得分达到71.8%，比之前的SOTA方法DVD（66.8%）高出5.0%。在LongVideoBench上，其准确率比VideoDeepResearch高出6.5%。在LVBench的细粒度能力维度分析中，Symphony 在实体识别（70.0%）、事件理解（69.4%）、关键信息检索（77.2%）、时序定位（70.1%）、推理（69.4%）和摘要（72.5%）六个维度上均表现优异。消融实验表明，移除反思智能体导致性能下降2.5%，移除字幕智能体下降1.4%，移除视觉感知智能体下降2.2%。此外，研究还探索了集成投票机制（Symphony-Vote），其在LVBench上进一步将性能提升至73.7%。

### Q5: 有什么可以进一步探索的点？

该论文提出的Symphony系统在长视频理解任务上取得了显著进展，但其架构和实验设计仍存在一些局限性，为未来研究提供了多个可探索的方向。首先，系统依赖于多个专用代理（如规划、定位、字幕、视觉感知）的协同，这可能导致计算开销较大、响应延迟较高，未来可研究更轻量化的代理融合机制或动态代理生成策略，以提升效率。其次，当前方法主要基于静态的任务分解与反思机制，对于视频中动态演变的复杂事件（如交互式场景或长期因果链）可能处理不足，可探索引入时序感知的推理框架，使代理能自适应地跟踪视频内容的演进。此外，实验虽在多个基准测试中表现优异，但未充分评估系统在开放域、多模态干扰（如音频、文本冲突）下的鲁棒性，未来可扩展到更复杂的真实场景。另一个方向是增强系统的可解释性——目前代理间的协作过程仍较“黑箱”，可设计可视化工具或因果追踪模块，以帮助理解推理轨迹。最后，论文未讨论计算资源限制（如GPU内存）对长视频处理的影响，未来可研究高效的内存管理或分段处理策略，以支持超长视频（如数小时）的理解。

### Q6: 总结一下论文的主要内容

本文提出Symphony，一个受人类认知启发的多智能体系统，旨在解决长视频理解任务中信息密度高、时间跨度大带来的挑战。核心贡献在于通过模拟人类认知模式，将复杂的长视频理解任务分解为规划、定位、字幕和视觉感知四个智能体，并引入反思智能体评估推理轨迹，从而构建了一个深度推理协作机制。方法上，系统采用基于视觉语言模型的定位方法，通过分析问题、分解扩展并评估视频片段相关性，以精准定位隐含意图和大时间跨度的复杂问题。实验表明，Symphony在LVBench、LongVideoBench等四个基准测试中达到最先进性能，尤其在LVBench上比之前最佳方法提升5.0%，显著提升了长视频推理能力。
