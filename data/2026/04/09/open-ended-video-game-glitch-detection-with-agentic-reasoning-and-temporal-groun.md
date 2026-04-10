---
title: "Open-Ended Video Game Glitch Detection with Agentic Reasoning and Temporal Grounding"
authors:
  - "Muyang Zheng"
  - "Tong Zhou"
  - "Geyang Wu"
  - "Zihao Lin"
  - "Haibo Wang"
  - "Lifu Huang"
date: "2026-04-09"
arxiv_id: "2604.07818"
arxiv_url: "https://arxiv.org/abs/2604.07818"
pdf_url: "https://arxiv.org/pdf/2604.07818v1"
categories:
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Benchmark"
  - "Video Understanding"
  - "Reasoning"
  - "Temporal Grounding"
  - "Tool-Augmented Agent"
relevance_score: 7.5
---

# Open-Ended Video Game Glitch Detection with Agentic Reasoning and Temporal Grounding

## 原始摘要

Open-ended video game glitch detection aims to identify glitches in gameplay videos, describe them in natural language, and localize when they occur. Unlike conventional game glitch understanding tasks which have largely been framed as image-level recognition or closed-form question answering, this task requires reasoning about game-specific dynamics such as mechanics, physics, rendering, animation, and expected state transitions directly over continuous gameplay videos and distinguishing true glitches from unusual but valid in-game events. To support this task, we introduce VideoGlitchBench, the first benchmark for open-ended video game glitch detection with temporal localization. VideoGlitchBench contains 5,238 gameplay videos from 120 games, each annotated with detailed glitch descriptions and precise temporal spans, enabling unified evaluation of semantic understanding and temporal grounding. We further propose GliDe, an agentic framework with three key components: a game-aware contextual memory for informed reasoning, a debate-based reflector for multi-perspective glitch detection and verification, and an event-level grounding module that recovers complete glitch intervals from fragmented temporal evidence. We also design a task-specific evaluation protocol that jointly measures semantic fidelity and temporal accuracy. Experiments show that this task remains highly challenging for current multimodal models, while GliDe achieves substantially stronger performance than corresponding vanilla model baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开放世界视频游戏故障检测问题，即从游戏视频中识别故障、用自然语言描述其内容，并精确定位其发生的时间段。研究背景在于游戏质量保证（QA）中，测试人员通常需要观看游戏录像来发现异常行为并撰写详细的错误报告。现有方法多将故障理解任务简化为图像级识别、纯文本推理或基于视频的封闭式问答（如多项选择），这些方法仅能处理问题的有限方面，无法应对真实游戏QA中所需的丰富上下文分析。具体而言，现有方法存在两大不足：一是难以区分真正的游戏故障与视觉上异常但符合游戏设计逻辑的正常事件，这需要模型深入理解游戏机制、物理规则、渲染效果等动态背景；二是无法有效处理故障的多样时间模式（如短暂出现、持续发生或间歇性重复），缺乏对时间证据的碎片化信息进行整合与完整定位的能力。因此，本文的核心问题是建立一个统一框架，实现开放式的、基于视频的故障检测与时间定位，要求模型具备游戏感知推理、多视角验证以及跨时间窗口的证据整合能力，以弥补现有方法在上下文分析和时间建模上的缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：游戏故障理解基准、游戏故障检测方法、视频理解的智能体框架，以及视频异常检测（VAD）。

在**游戏故障理解基准**方面，相关工作如GamePhysics、GlitchBench、GameBugDescriptions和GameBench，主要关注单帧图像识别或基于多项选择题的封闭式问答，缺乏对原始视频进行开放式描述和时间定位的能力。本文提出的VideoGlitchBench则填补了这一空白，要求模型直接从连续视频中检测故障，并用自然语言描述及精确时间戳进行定位。

在**游戏故障检测方法**上，现有方法如基于CLIP的检索（GamePhysics）、专用多模态助手（VideoGameBunny）或结合物理常识的模型（PhysVLM），大多依赖于预定义查询或有限答案空间。它们难以应对开放式检测任务，而本文提出的GliDe框架通过情境记忆、辩论式反思器和事件级定位模块，实现了对原始视频的自主推理与完整时间区间恢复。

在**视频理解的智能体框架**领域，VideoAgent、TraveLER等工作利用迭代规划和工具调用增强视频问答，而游戏领域的自动测试智能体（如CCPT）专注于通过交互探索发现漏洞。本文的GliDe与之不同，它专为从已录制的游戏视频中被动检测并定位故障而设计，不依赖主动环境交互。

最后，在**视频异常检测**方面，传统VAD方法（如Holmes-VAD）主要针对监控视频中的异常人类行为，而游戏故障源于游戏机制、物理模拟等虚拟世界规则的违反。因此，本文任务需要显式地对游戏特定动态进行推理，与常规VAD有本质区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GliDe的智能体框架来解决开放世界视频游戏故障检测问题，该框架包含三个核心设计，以应对任务中累积上下文需求、误报率高以及时间定位碎片化等挑战。整体框架是一个五阶段流水线。

首先，输入的游戏视频被分割成非重叠的窗口，每个窗口的帧被拼接成复合图像，以保留短时序线索并减少对大语言模型的调用。框架的核心模块包括：
1.  **Scanner（扫描器）**：对每个窗口进行单次处理，预测其是否包含潜在故障、粗略类别、当前游戏上下文摘要以及置信度。这些上下文摘要随后被聚合，通过一个LLM摘要函数生成一个轻量级的**游戏感知上下文记忆**，该记忆捕获视频整体的场景、实体和动态，为后续推理提供全局先验。

2.  **基于辩论的验证循环**：对于扫描器筛选出的候选窗口，系统进入一个由Planner（规划器）、Executor（执行器）和Reflector（反射器）构成的迭代验证阶段。规划器根据当前假设、全局记忆和累积的调查记忆，选择下一步动作（如调用VQA工具、局部放大或对象跟踪工具）。执行器执行动作并返回观察结果。**反射器**是此阶段的关键创新，它通过一个结构化的**辩论机制**进行评估：由“倡导者”（主张是故障）、“怀疑者”（提出合理的游戏内解释）和“法官”（仲裁并输出最终判决及置信度）三个角色进行多视角推理。这迫使系统在决策前对比竞争性解释，有效区分真实故障与罕见但有效的游戏行为，从而降低误报。

3.  **事件级Grounder（定位器）**：验证阶段在窗口级别进行，而输出需要完整的事件级故障报告。因此，定位器执行两步操作：首先，基于语义对已验证的故障窗口进行**聚类**，将描述同一故障现象的窗口归为一组，即使它们在时间上不连续。其次，对每个事件簇进行**双向时间传播**，从初始检测的窗口开始，向相邻窗口迭代检查并扩展边界，从而恢复故障的完整时间范围。

最终，框架将每个事件簇汇总成一个连贯的自然语言描述，并将精炼后的帧范围转换为时间戳间隔，输出结构化的故障报告集合。该方法的核心创新点在于集成了游戏感知记忆以实现上下文感知推理、引入多角色辩论机制进行可靠验证，以及通过语义聚类与时间传播实现从碎片化窗口检测到完整事件级定位的转换。

### Q4: 论文做了哪些实验？

论文在VideoGlitchBench基准上进行了全面的实验评估。实验设置方面，视频统一以4 FPS采样，并划分为不重叠的8帧窗口，帧被空间拼接成复合图像后输入模型；实验在四块NVIDIA Quadro RTX 8000 GPU上运行。

评估的数据集是论文提出的VideoGlitchBench，包含来自120款游戏的5,238个游戏视频，每个视频都标注了详细的故障描述和精确的时间跨度。对比方法包括一系列多模态模型：专有模型（gemini-2.0-flash、gpt-4o-mini、claude-3.5-haiku、nova-lite-v1）和开源模型（Qwen2.5-VL-3B/7B-Instruct、InternVL2.5-4B/8B、UI-TARS-1.5-7B、LLaVA-OneVision-7B）。论文提出的GliDe框架主要在开源模型上进行对比。

主要结果如下：当前多模态模型在该任务上表现仍有限，最佳专有模型（claude-3.5-haiku）的F1仅为26.01%，mIoU为0.47；最佳开源基线（UI-TARS-1.5-7B）的F1为21.62%，六个开源模型平均F1仅14.47%，平均mIoU为0.28。应用GliDe后，所有开源骨干模型在所有主要指标上均有显著提升：平均F1从14.47%提升至36.05%（+21.58%），平均mIoU从0.28提升至0.51（+0.23），整体F1×IoU分数也从平均4.37%升至17.05%。经过GliDe增强的开源模型在F1、mIoU和F1×IoU上均超过了表中所列的专有基线。

消融实验验证了GliDe三个关键组件的有效性：移除游戏感知记忆会使F1从39.12%降至33.03%；移除基于辩论的验证机制则使精确率从34.55%降至28.94%；移除事件级定位策略会导致mIoU在不同骨干网络上显著下降（例如Qwen2.5-VL-7B-Instruct从0.53降至0.32）。此外，超参数敏感性研究表明，4 FPS和窗口大小为8的设置能取得最佳性能。

### Q5: 有什么可以进一步探索的点？

该论文在开放域游戏故障检测方面做出了重要贡献，但仍存在一些局限性和值得探索的方向。首先，当前框架主要依赖预训练的多模态模型作为基础，其性能上限受限于这些模型的视觉理解和时序推理能力。未来可探索更专门的视频编码器或引入游戏引擎的内部状态信息作为补充信号，以提升对复杂游戏动态的感知。其次，辩论式验证模块虽然能整合多视角，但计算开销较大，且可能陷入循环争论；可研究更高效的共识形成机制，或引入强化学习来优化辩论策略。此外，基准测试虽涵盖120款游戏，但故障类型和游戏风格仍有局限；未来需扩展至更开放的游戏环境（如开放世界游戏）和更细粒度的故障分类（如物理、渲染、逻辑错误等）。最后，当前任务侧重于检测与描述，未来可进一步探索故障的自动修复或因果分析，推动从诊断到干预的闭环系统发展。

### Q6: 总结一下论文的主要内容

该论文针对开放世界视频游戏故障检测任务，提出了首个包含时序定位的基准测试VideoGlitchBench及一个新型智能体框架GliDe。核心问题是：从连续的游戏视频中检测故障，用自然语言描述其语义，并精确定位其发生的时间区间。这要求模型能理解游戏特有的动态机制（如物理、渲染、状态转换），并区分真实故障与游戏中虽罕见但合理的事件。

论文的主要贡献包括：1) 构建了VideoGlitchBench，包含来自120款游戏的5,238段游戏视频，每段都标注了详细的故障描述和精确的时间跨度，为语义理解和时序定位提供了统一评估基准；2) 提出了GliDe框架，其包含三个关键组件：用于知情推理的游戏感知上下文记忆、基于辩论的反射器以实现多视角故障检测与验证、以及从碎片化证据恢复完整故障区间的事件级定位模块；3) 设计了一个联合评估语义保真度和时序准确性的任务特定协议。

实验表明，当前多模态模型在此任务上仍面临巨大挑战，而GliDe相比基线模型取得了显著更强的性能。该工作推动了游戏内容理解向更开放、动态和细粒度的方向发展。
