---
title: "VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking"
authors:
  - "Jingyang Lin"
  - "Jialian Wu"
  - "Jiang Liu"
  - "Ximeng Sun"
  - "Ze Wang"
  - "Xiaodong Yu"
  - "Jiebo Luo"
  - "Zicheng Liu"
  - "Emad Barsoum"
date: "2026-03-20"
arxiv_id: "2603.20185"
arxiv_url: "https://arxiv.org/abs/2603.20185"
pdf_url: "https://arxiv.org/pdf/2603.20185v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Video Agent"
  - "Tool Use"
  - "Active Perception"
  - "Efficiency"
  - "Long-Horizon Reasoning"
  - "Think-Act-Observe Loop"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking

## 原始摘要

Video agentic models have advanced challenging video-language tasks. However, most agentic approaches still heavily rely on greedy parsing over densely sampled video frames, resulting in high computational cost. We present VideoSeek, a long-horizon video agent that leverages video logic flow to actively seek answer-critical evidence instead of exhaustively parsing the full video. This insight allows the model to use far fewer frames while maintaining, or even improving, its video understanding capability. VideoSeek operates in a think-act-observe loop with a well-designed toolkit for collecting multi-granular video observations. This design enables query-aware exploration over accumulated observations and supports practical video understanding and reasoning. Experiments on four challenging video understanding and reasoning benchmarks demonstrate that VideoSeek achieves strong accuracy while using far fewer frames than prior video agents and standalone LMMs. Notably, VideoSeek achieves a 10.2 absolute points improvement on LVBench over its base model, GPT-5, while using 93% fewer frames. Further analysis highlights the significance of leveraging video logic flow, strong reasoning capability, and the complementary roles of toolkit design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有视频智能体模型在处理长视频和复杂视频理解任务时，计算成本过高的问题。研究背景是，随着大语言模型和多模态模型的发展，视频-语言理解任务取得了显著进展，但主流方法（包括新兴的视频智能体）通常依赖于对视频进行密集的帧采样和预处理（例如以0.2-2 FPS的速率解析），将视觉内容转化为详细的文本描述或结构化记忆。这种“贪婪解析”范式存在明显不足：其计算成本随视频长度急剧增加，效率低下，且对于许多问题而言，大部分视频内容可能是不必要的，论文指出在LVBench基准上，超过80%的问题只需检查原视频不到5%的内容即可回答。

因此，本文要解决的核心问题是：如何设计一种更高效、更智能的视频智能体范式，使其能够像人类一样，主动地、有选择性地在视频中寻找与答案关键相关的证据，而不是被动地、无差别地处理全部视频内容。具体而言，论文提出了VideoSeek，一个利用视频逻辑流来主动“寻找”证据的长视野视频智能体。它通过一个“思考-行动-观察”的循环，结合一个精心设计的、支持多粒度观察的工具包，实现对视频的查询感知式探索，从而在显著减少处理帧数的同时，维持甚至提升视频理解和推理的性能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：视频语言模型和视频智能体模型。

在**视频语言模型**方面，早期研究通过视频适配器将图像语言架构扩展到视频领域。后续工作则转向构建高质量的合成视频指令跟随数据，或基于现有视频描述数据集生成问答对。近期研究强调在训练中混合文本、图像和视频数据的重要性。随着基础任务性能趋于饱和，长视频理解和复杂视频推理成为焦点，但这些方法大多仍采用单次处理固定帧的范式，难以应对需要迭代证据收集的复杂场景。本文则将其视为需要迭代规划的长视野问题。

在**视频智能体模型**方面，早期方法依赖于人工设计的工作流程。VideoAgent 率先使用大语言模型作为中心代理迭代检查关键帧。后续研究通过粗到细的树状搜索或构建视频数据库进行信息检索来改进。近期工作则发展出基于工具使用的自主自适应范式，例如 DVD 和 Ego-R1 Agent。然而，这些方法大多依赖于预建数据库或贪婪地扫描整个视频，计算成本高。**本文提出的 VideoSeek 与这些工作的核心区别在于**：它不依赖预建数据库，而是利用视频内在的逻辑流，在长对话历史中基于累积观察主动寻找信息关键帧，从而避免了对完整视频的密集解析，显著降低了计算开销。

### Q3: 论文如何解决这个问题？

论文通过设计一个基于“思考-行动-观察”循环的长视野视频智能体VideoSeek来解决传统视频智能体依赖密集采样帧导致计算成本高的问题。其核心方法是让模型主动、有选择性地寻找与答案关键相关的证据，而非穷举解析整个视频。

整体框架采用ReAct式的工作流程，智能体在由思考模型、工具集和累积轨迹构成的循环中迭代运行。主要模块包括：1）一个作为推理核心的思考大语言模型（θ_think），负责分析查询和当前轨迹，规划下一步行动；2）一个精心设计的、包含三个不同时间粒度视频分析工具的工具包（T）。这三个工具是创新的关键：**Overview工具**首先对全视频进行均匀采样，生成粗粒度的全局摘要，建立故事线并初步定位相关区域；**Skim工具**对候选的长片段进行中等粒度的扫描，通过采样少量帧并高亮查询相关内容，进一步缩小搜索范围；**Focus工具**则对最终确定的短片段进行高帧率（如1 FPS）的细粒度分析，以捕捉精确细节。此外，工具包还包含一个用于终止循环并生成答案的<answer>工具。

其创新点在于将视频语言任务重构为长视野推理问题，并模拟人类观看视频的逻辑流：先概览，再定位，最后聚焦。通过这种多粒度、由粗到精的主动寻求策略，VideoSeek能够以远少于基线模型的帧数（例如在LVBench上减少93%），高效地构建信息密集的推理轨迹（τ），并基于此轨迹生成最终答案，从而在降低计算成本的同时，实现了理解能力的维持甚至提升。

### Q4: 论文做了哪些实验？

论文在四个具有挑战性的视频理解与推理基准上进行了实验：LVBench、Video-MME（长视频子集）、LongVideoBench（长视频子集）和Video-Holmes。实验设置以GPT-5作为默认的思考大语言模型，VideoSeek代理在“思考-行动-观察”循环中运行，并使用一个包含三个工具（overview、skim、focus）的工具包来主动寻找关键证据，而非密集采样。关键超参数α根据基准进行调整（LVBench设为4，其他设为2），最大循环轮数N设为20。

对比方法包括大型多模态模型（如Qwen2.5-VL-72B、GPT-4o、Gemini系列、GPT-5基础版）和视频代理模型（如VideoAgent、VideoTree、DrVideo、VCA、MR. Video、DVD）。主要结果如下：在LVBench上（无字幕），VideoSeek以平均92.3帧取得了68.4%的准确率，优于基础模型GPT-5（60.1%，384帧），并接近最佳代理DVD（74.2%，8074帧），但仅使用了后者约1%的帧数；在有字幕时，VideoSeek以27.2帧取得76.7%的准确率，显著超越GPT-5（66.5%）和DVD（76.0%）。在Video-MME上（无字幕），VideoSeek以60.9帧取得70.1%的准确率，优于所有对比模型；有字幕时以15.9帧取得81.2%的准确率。在LongVideoBench上，VideoSeek以29.6帧取得73.5%的准确率，优于GPT-5（64.5%）和DVD（68.6%）。在复杂的Video-Holmes基准上，VideoSeek以42.7帧取得47.3%的整体准确率，优于Gemini 2.5 Pro（45.0%）和GPT-5（44.1%）。消融实验表明，基础模型的推理能力（GPT-5优于o4-mini和GPT-4.1）以及工具包中每个工具（尤其是overview）都对性能至关重要。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其逻辑驱动的导航策略可能不适用于需要捕捉意外或高度局部化突发事件的任务，例如异常检测，因为这类任务的关键证据难以通过逻辑流预判。未来研究可探索如何将主动寻求与对意外事件的被动监控相结合，例如引入一个并行的、基于变化的检测模块来触发对异常片段的细粒度分析。此外，当前工具集和推理循环的效能严重依赖于基础大模型（如GPT-4）的能力，未来可研究如何为视频逻辑流设计更专用的、参数更少的轻量级推理模型，以进一步提升效率并降低对通用大模型的依赖。另一个方向是探索多模态工具，例如结合音频或文本字幕的逻辑流，以提供更全面的上下文，从而在复杂叙事或对话密集的视频中做出更精准的导航决策。

### Q6: 总结一下论文的主要内容

本文提出VideoSeek，一种面向长视频理解与推理的智能体模型，旨在解决现有视频智能体因依赖密集帧采样而导致计算成本过高的问题。其核心思想是利用视频的逻辑流主动寻找与答案关键相关的证据，而非贪婪地解析全部视频内容。方法上，VideoSeek采用“思考-行动-观察”的循环框架，并设计了一个包含概览、略读和聚焦三种工具的多粒度工具包，使模型能够根据查询动态调整观察策略，实现高效导航与推理。实验在LVBench、Video-MME等四个挑战性基准上进行，结果表明VideoSeek在使用远少于先前方法的帧数（如在LVBench上减少93%帧数）的同时，取得了更优的准确率（如在LVBench上比基础模型GPT-5提升10.2个绝对百分点）。论文的主要贡献在于提出了一种高效的长视频智能体范式，强调了利用视频逻辑流、强大推理能力以及工具包设计在提升视频智能体性能与效率中的关键作用。
