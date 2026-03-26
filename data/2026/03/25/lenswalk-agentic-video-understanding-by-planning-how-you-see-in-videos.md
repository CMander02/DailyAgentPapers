---
title: "LensWalk: Agentic Video Understanding by Planning How You See in Videos"
authors:
  - "Keliang Li"
  - "Yansong Li"
  - "Hongze Shen"
  - "Mengdi Liu"
  - "Hong Chang"
  - "Shiguang Shan"
date: "2026-03-25"
arxiv_id: "2603.24558"
arxiv_url: "https://arxiv.org/abs/2603.24558"
pdf_url: "https://arxiv.org/pdf/2603.24558v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Agentic Framework"
  - "Video Understanding"
  - "Tool Use"
  - "Reasoning and Planning"
  - "Active Perception"
  - "Vision-Language Models"
  - "Zero-Shot"
relevance_score: 7.5
---

# LensWalk: Agentic Video Understanding by Planning How You See in Videos

## 原始摘要

The dense, temporal nature of video presents a profound challenge for automated analysis. Despite the use of powerful Vision-Language Models, prevailing methods for video understanding are limited by the inherent disconnect between reasoning and perception: they rely on static, pre-processed information and cannot actively seek raw evidence from video as their understanding evolves. To address this, we introduce LensWalk, a flexible agentic framework that empowers a Large Language Model reasoner to control its own visual observation actively. LensWalk establishes a tight reason-plan-observe loop where the agent dynamically specifies, at each step, the temporal scope and sampling density of the video it observes. Using a suite of versatile, Vision-Language Model based tools parameterized by these specifications, the agent can perform broad scans for cues, focus on specific segments for fact extraction, and stitch evidence from multiple moments for holistic verification. This design allows for progressive, on-demand evidence gathering that directly serves the agent's evolving chain of thought. Without requiring any model fine-tuning, LensWalk delivers substantial, plug-and-play performance gains on multiple model recipes, boosting their accuracy by over 5\% on challenging long-video benchmarks like LVBench and Video-MME. Our analysis reveals that enabling an agent to control how it sees is key to unlocking more accurate, robust, and interpretable video reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视频理解中一个核心挑战：现有方法在推理与感知之间存在脱节，无法根据动态演进的认知需求主动地从原始视频中搜寻证据。视频信息具有密集、时序展开的特性，使得一次性、均匀的采样分析既低效又容易遗漏关键事件。尽管当前基于视觉语言模型（VLMs）的方法取得了进展，但它们通常依赖于静态、预处理的视频表示（如固定采样帧或预提取的文本描述），其观察过程是预先确定的，无法在推理过程中根据中间假设的变化主动调整观察的时空范围和密度。

现有方法存在明显不足：传统单次前向模型采用均匀采样，可能丢失稀疏但决定性的事件；基于启发式关键帧选择的方法仍依赖固定的一次性采样，无法动态转移焦点；而近期基于检索或工具调用的智能体框架虽然能按需获取信息，但通常仅限于查询预计算的索引或固定类型的预处理结果（如字幕、OCR），缺乏对原始视频进行细粒度、按需观察的能力，导致观察与推理耦合松散，且整体计算资源分配缺乏规划。

因此，本文提出的核心问题是：如何构建一个智能体框架，使大型语言模型（LLM）作为推理器能够主动规划并控制其对视频的观察过程，实现根据推理链的演进动态指定观察的时间范围、采样密度，从而进行渐进式、按需的证据收集。为此，论文引入了LensWalk框架，它通过建立“推理-规划-观察”的紧密循环，让智能体使用一套参数化的工具（如扫描搜索、片段聚焦、拼接验证）主动从原始视频中提取视觉证据，从而提升长视频理解的准确性、鲁棒性和可解释性，同时高效管理观察成本。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：上下文选择、测试时扩展和多模态工具使用代理。

在**上下文选择**方面，现有工作主要关注如何在有限的多模态大语言模型上下文窗口中，通过查询感知的关键帧或片段选择、任务特定的对齐模块，或信息压缩（如去除冗余帧）来选取紧凑且信息丰富的视频上下文。然而，这些方法通常在推理前一次性静态选定可见内容，而本文的LensWalk框架则将上下文选择本身转变为由代理推理假设驱动的、逐步的、工具介导的动态过程。

在**测试时扩展**方面，相关研究旨在通过增加推理时计算来提升性能。一类工作通过训练模型支持长链思维和自我纠正来强化内部推理（如Video-R1），但仍基于固定的视觉输入。另一类工作将视频模型嵌入代理工作流，让大语言模型控制如何检索或聚合预处理后的片段和描述。本文框架的不同之处在于，它允许代理在测试时主动决定如何观察视频（如选择时间范围、采样密度），而不仅仅是基于固定观察内容分配更多计算。

在**多模态工具使用代理**方面，现有研究主要沿两个方向展开：代理主动搜索文本和视觉证据以增强推理上下文，或使用工具在解决问题时转换、合成或生成图像。针对视频理解，近期工具化方法通常通过预处理代理（如密集描述或片段嵌入数据库）与视频交互，代理只能决定查询内容，而对视频的观察方式（如时间覆盖、采样密度）控制有限。本文的LensWalk则通过提供参数化工具，赋予代理对观察过程的精细控制能力，实现了按需、渐进的证据收集。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LensWalk的智能体框架来解决视频理解中推理与感知脱节的问题。该框架的核心是建立一个“推理-规划-观察”的紧密循环，让基于大语言模型（LLM）的推理器能够主动、动态地控制其视觉观察的范围和粒度。

**整体框架与主要模块**：LensWalk的架构围绕一个LLM推理器（Reasoner, Mr）和一个由视觉语言模型（VLM）驱动的观察工具包（Observation Toolkit, O）构建。推理器分析用户查询、视频元数据和累积的历史证据，生成一个具体的行动计划。这个计划的核心是调用观察工具，并精确指定本次观察的**时间范围**和**采样密度**（如帧率、区间划分）。执行计划后，观察器（Observer, Mo）从指定的视频上下文中提取信息，形成新的证据并更新历史。为了确保多轮交互的连贯性，系统引入了两个轻量级记忆机制：**时间戳锚点**（在观察帧中插入时间文本，强制观察器在回答中引用具体时间）和**全局主体记忆表**（记录视频中出现的实体及其属性和出现时间戳，供推理器进行一致引用和后续规划）。

**关键技术组件（观察工具包）**：工具包包含三种精心设计的工具，支持灵活的观察策略组合：
1.  **扫描搜索**：用于在较大时间区间内进行**高效、广泛的线索定位**。它将指定区间划分为多个切片，对每个切片进行稀疏采样并并行查询VLM，返回每个切片的摘要或相关性判断，以快速发现潜在相关段落。
2.  **片段聚焦**：用于对**单个连续时间段进行精细探查**。它采用密集采样策略，旨在提取细粒度的细节、局部动态或微小视觉属性，适用于假设验证、属性读取或消除歧义。
3.  **缝合验证**：专为**整合来自多个非连续视频段的证据**而设计，用于前后对比、跟踪物体转移或验证因果叙事。它允许对不同的片段采用**非对称的采样率**（例如，对动作密集段用高帧率，过渡段用低帧率），并将所有帧整合为一个批次供VLM处理，从而在单一观察步骤中支持对复杂事件链的推理。

**创新点**：
1.  **动态、按需的观察调度**：核心创新在于将“如何观察”参数化并交由智能体在推理循环中动态决定，实现了观察范围与粒度随思维链演进的自适应调整，突破了依赖固定预处理信息的局限。
2.  **表达力强的模块化工具包**：通过扫描、聚焦、缝合三种基础工具的灵活组合，智能体可以执行从粗粒度定位到细粒度提取再到跨片段整合的完整证据搜集策略，直接服务于其推理过程。
3.  **轻量而有效的证据 grounding 机制**：结合时间戳锚点和主体记忆表，以较低的计算开销实现了证据的时空锚定和实体一致性维护，支持智能体对模糊区域进行重新观察和自我纠正，增强了系统的鲁棒性和可解释性。

综上，LensWalk通过赋予智能体控制其视觉观察的能力，构建了一个无需微调、即插即用的渐进式证据搜集框架，从而显著提升了长视频理解的准确性。

### Q4: 论文做了哪些实验？

论文在多个具有挑战性的长视频理解基准上进行了实验。实验设置上，LensWalk作为一个即插即用的框架，允许任意组合推理器和观察者模型，实验中选用了o3、GPT-4.1、GPT-5、Qwen2.5-VL-72B等先进模型进行组合。代理被限制最多调用20次工具，每次调用一回合，并为扫描搜索、片段聚焦和缝合验证工具分别设定了180、32和128帧的每调用帧数预算。

使用的数据集/基准测试主要包括：用于长时态理解的LVBench和LongVideoBench（验证集的长视频部分）；用于通用长视频理解的Video-MME（30-60分钟的长视频部分）；以及用于评估需要高级推理的视频问答任务的MMVU和Video-MMMU；此外还包括了以自我为中心视角的EgoSchema。

对比方法广泛，包括：（1）基于视觉语言模型的方法，如Gemini系列、GPT系列、o3、LLaVA-Video、InternVL2.5、Qwen2.5-VL等；（2）智能体视频理解方法，如VideoAgent、VCA、Ego-R1、MR. Video和Deep Video Discovery。

主要结果显示，LensWalk在所有基准上都取得了强劲性能。在长视频基准上，例如使用o3作为推理器的LensWalk在LVBench上达到68.6%的准确率，在LongVideoBench上达到70.6%，在Video-MME长视频部分达到71.4%，在EgoSchema上达到74.8%，显著超越了基线模型和先前的智能体方法。在推理基准上，LensWalk (o3) 在MMVU上达到79.2%，在Video-MMMU整体上达到78.33%，相比强大的o3基线（75.44%）有显著提升。关键数据指标包括：在Video-MME长视频部分，LensWalk (o3/GPT-4.1) 相比GPT-4.1基线（63.1%）提升了6.9个百分点至70.0%。消融实验表明，移除扫描搜索工具导致性能下降4.6%，移除缝合验证下降3.2%，移除片段聚焦下降1.9%。此外，框架对开源模型也有效，例如使用o3作为推理器能将Qwen2.5-VL-7B观察者的准确率从55.4%提升至61.3%（+5.9%）。效率分析显示，该框架能以更少的帧数和端到端推理时间实现有竞争力的准确率，并降低了每回合的峰值令牌数，缓解了内存压力。

### Q5: 有什么可以进一步探索的点？

该论文的框架虽然实现了动态规划与观察的闭环，但在几个方面仍有进一步探索的空间。首先，其视觉感知工具依赖于预训练的视觉语言模型，这些模型本身可能存在对复杂场景或细微动态的理解偏差，未来可研究如何将工具本身也设计为可在线学习或自适应优化的模块。其次，当前规划完全基于大语言模型的推理，缺乏对视频全局结构的先验建模，可引入轻量化的视频摘要或场景图生成模块，为智能体提供高层语义引导，减少盲目搜索。此外，框架主要针对问答类任务，未来可扩展至视频生成编辑、自动化剪辑等创作型任务，探索“规划-观察-执行”的完整工作流。最后，在计算效率上，动态采样虽提升了精度，但可能增加延迟，如何平衡精度与实时性，尤其是在流式视频处理中，是值得优化的方向。

### Q6: 总结一下论文的主要内容

本文提出LensWalk框架，旨在解决视频理解中推理与感知脱节的核心问题。传统方法依赖预处理的静态信息，无法根据理解进展主动从视频中动态获取原始证据。为此，LensWalk设计了一个由大语言模型驱动的智能体框架，通过“推理-规划-观察”的紧密循环，让智能体能够自主控制视觉观察过程：每一步动态指定观察的时间范围和采样密度，并利用基于视觉语言模型的工具集执行广泛扫描、聚焦特定片段提取事实、整合多时刻证据进行整体验证。这种方法实现了按需渐进式证据收集，直接服务于智能体演进的思维链。无需微调模型，LensWalk在LVBench和Video-MME等长视频基准测试中为多种模型配方带来了显著的即插即用性能提升，准确率提高超过5%。研究表明，赋予智能体控制其观察方式的能力，是实现更准确、鲁棒和可解释视频推理的关键。
