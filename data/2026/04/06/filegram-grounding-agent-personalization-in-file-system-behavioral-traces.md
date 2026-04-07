---
title: "FileGram: Grounding Agent Personalization in File-System Behavioral Traces"
authors:
  - "Shuai Liu"
  - "Shulin Tian"
  - "Kairui Hu"
  - "Yuhao Dong"
  - "Zhe Yang"
  - "Bo Li"
  - "Jingkang Yang"
  - "Chen Change Loy"
  - "Ziwei Liu"
date: "2026-04-06"
arxiv_id: "2604.04901"
arxiv_url: "https://arxiv.org/abs/2604.04901"
pdf_url: "https://arxiv.org/pdf/2604.04901v1"
github_url: "https://github.com/synvo-ai/FileGram"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Agent Personalization"
  - "Agent Memory"
  - "File-System Agent"
  - "Benchmark"
  - "Data Synthesis"
  - "Multimodal Traces"
  - "Human-AI Interaction"
relevance_score: 8.0
---

# FileGram: Grounding Agent Personalization in File-System Behavioral Traces

## 原始摘要

Coworking AI agents operating within local file systems are rapidly emerging as a paradigm in human-AI interaction; however, effective personalization remains limited by severe data constraints, as strict privacy barriers and the difficulty of jointly collecting multimodal real-world traces prevent scalable training and evaluation, and existing methods remain interaction-centric while overlooking dense behavioral traces in file-system operations; to address this gap, we propose FileGram, a comprehensive framework that grounds agent memory and personalization in file-system behavioral traces, comprising three core components: (1) FileGramEngine, a scalable persona-driven data engine that simulates realistic workflows and generates fine-grained multimodal action sequences at scale; (2) FileGramBench, a diagnostic benchmark grounded in file-system behavioral traces for evaluating memory systems on profile reconstruction, trace disentanglement, persona drift detection, and multimodal grounding; and (3) FileGramOS, a bottom-up memory architecture that builds user profiles directly from atomic actions and content deltas rather than dialogue summaries, encoding these traces into procedural, semantic, and episodic channels with query-time abstraction; extensive experiments show that FileGramBench remains challenging for state-of-the-art memory systems and that FileGramEngine and FileGramOS are effective, and by open-sourcing the framework, we hope to support future research on personalized memory-centric file-system agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在本地文件系统中作为“协同工作者”时，如何实现有效个性化所面临的核心瓶颈。研究背景是，随着操作系统级助手的发展，AI智能体正从对话界面演变为集成在文件系统中的协同工作伙伴。然而，要实现无缝的人机协作，智能体必须超越执行孤立命令，能够根据用户长期、多变的工作流程、组织习惯和执行风格进行持续适应。

现有方法存在三个主要不足：首先，在**数据**层面，由于严格的隐私限制和缺乏可扩展的收集策略，获取真实、多模态、长轨迹的文件系统行为数据极其困难，这严重限制了模型的训练和评估。其次，在**评估**层面，现有基准测试主要关注对话回忆或孤立的图形用户界面成功率，而忽视了基于文件系统行为、以记忆为中心的个性化行为理解任务。最后，在**方法**层面，主流记忆架构本质上是“以交互为中心”的，它们依赖自上而下的对话摘要来构建用户画像，缺乏能够从连续的文件系统原子操作（如创建、编辑、重组文件）和内容增量中，自底向上提炼用户程序性行为模式的架构。

因此，本文要解决的核心问题是：如何克服数据稀缺、评估缺失和方法论局限，为文件系统智能体建立一个以行为痕迹为基础的记忆与个性化框架。为此，论文提出了FileGram这一统一框架，它通过三个核心组件系统性地应对上述挑战：一个用于大规模生成模拟数据的数据引擎（FileGramEngine），一个用于评估记忆系统的诊断性基准（FileGramBench），以及一个直接从原子操作和内容增量自底向上构建用户画像的新型记忆架构（FileGramOS），从而为开发真正自适应的、以记忆为中心的AI协同工作者奠定基础。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：评测基准和记忆系统与个性化。

在**评测基准**方面，现有工作主要遵循两种范式：对话回忆和环境任务执行。对话类基准（如DuLeMon、DialogBench、MemoryBank、LongMemEval、MemAgentBench、MMDU、LoCoMo、MMRC、Mem-Gallery）侧重于从长文本对话中进行静态语义检索，但剥离了真实工作流的流程上下文。执行驱动类基准（如OSWorld、OfficeBench）将智能体置于操作系统或网页界面中，但将记忆作为通过任务成功间接衡量的隐变量。近期一些轨迹感知基准（如MEMTRACK、AgencyBench、Evo-Memory、MemoryArena）评估记忆也主要用于通用推理和事实保留。与这些工作不同，本文提出的FileGramBench是首个基于文件系统行为痕迹、专注于评估智能体从纵向痕迹中推断和预测用户特定行为的可控评测套件，它同时提供了多模态内容、持久化记忆和受控用户画像。

在**记忆系统与个性化**方面，现有架构（主要隐含于上述对话类基准中）主要从对话历史中提取显性事实和关系结构，与用户的操作环境脱节。近期在多模态感知和轨迹追踪方面的进展虽然能捕捉时间动态，但通常在孤立或高度受限的模拟环境（如在线购物）中对这些维度进行建模。关键的是，现有框架都未利用细粒度的文件系统活动来共同维持持续协同工作所需的流程性、语义性和情景性记忆。本文提出的FileGramOS通过直接将原子化的文件系统操作和内容变化编码到一个统一的三通道记忆框架中，弥补了这一空白，实现了对行为模式的稳健提取。

### Q3: 论文如何解决这个问题？

论文通过提出FileGram这一综合框架来解决基于文件系统行为轨迹的智能体个性化问题，其核心是FileGramOS这一自底向上的记忆架构。该方法摒弃了传统以对话摘要为中心的记忆构建方式，直接从原子操作和内容差异中构建用户画像。

整体框架采用三阶段流水线设计。首先，在**单轨迹编码阶段**，原始行为轨迹通过三个并行提取流处理成名为“记忆印痕”（Engram）的结构化原子单元。其中，**程序提取流**通过动作计数、计算和向量化，将50多个行为特征压缩为17维指纹向量；**语义解析流**利用视觉语言模型处理多模态文件快照和编辑差异，生成结构描述和行为风格描述符；**动作合并流**则对原始事件时间线进行边界检测，分割为离散的逻辑片段。这三个流输出的程序单元、语义单元和片段单元共同构成一个Engram。

其次，在**跨印痕整合阶段**，多个Engram的组件被路由到三个专门的记忆通道中。**程序通道**通过聚合多个轨迹的17维指纹并计算跨轨迹统计量（均值、中位数、标准差等），形成稳定的“程序线索”，用以刻画如“深度嵌套组织”等行为特质。**语义通道**处理行为描述符和文件元数据，通过分块、嵌入和LLM跨会话摘要，合并不同风格和偏好，形成统一的“语义线索”。**片段通道**则保持时间保真度并检测行为漂移，它基于序列相似性对轨迹进行聚类，并使用z-score归一化和LLM驱动的“异常判断器”来区分任务相关的变化与真正的行为偏移，输出情境化的“片段线索”。

最后，在**查询自适应检索阶段**，系统根据用户查询提取关键词，自适应地从MemoryStore中检索预计算好的三类线索，并将它们路由到最终的LLM生成步骤，以合成有证据支持的答案。

该方法的创新点在于：1）**自底向上的结构化记忆构建**：不同于叙事优先的方法在摄入时就进行摘要（从而抹去关键行为细节），FileGramOS在摄入时保留分布统计信息，将语义抽象推迟到查询时，避免了行为特征的“扁平化”。2）**三通道分离与协同**：程序、语义、片段通道各司其职，分别捕获稳定的行为模式、内容风格偏好和时序异常，在查询时动态组合，实现了更精细和鲁棒的个性化理解。实验表明，该方法在FileGramBench基准测试中显著优于现有的最先进记忆系统，尤其在需要跨会话比较和行为异常检测的任务上优势明显，并证明了细粒度的操作微观结构是文件系统个性化的决定性信号。

### Q4: 论文做了哪些实验？

论文在FileGramBench基准上进行了系统实验。实验使用了FileGramEngine生成的640条轨迹，涵盖三种设置：文本（原始Markdown输出）、多模态（渲染为PDF/图像）和真实世界（人类屏幕录制）。评估对比了12种方法，分为三类：上下文方法（如Full Context、Naive RAG、VisRAG）、文本交互记忆方法（如Mem0、Zep、MemOS、EverMemOS、SimpleMem）和多模态记忆方法（如MMA、MemU），并以Gemini 2.5-Flash作为共享QA骨干。

主要结果：FileGramOS在整体平均准确率上达到59.6%，显著优于最强基线EverMemOS（49.9%）。关键指标包括：在行为推理（BehavInf）任务上达到42.1%，轨迹解耦（TraceDis）达到80.9%，异常检测（AnomDet）达到70.2%，文件 grounding（FileGrd）达到55.8%。实验显示，FileGramOS在程序性、语义性和情景性通道上均表现稳健，尤其在保留行为统计特征（如操作计数、目录深度）方面优于依赖叙事摘要的基线方法。多模态设置中，仅文本方法性能下降，而FileGramOS因依赖模态不变的事件日志而最具韧性；真实世界设置中，所有方法在人类屏幕录制数据上准确率骤降至个位数，揭示了模拟与真实行为理解间的显著差距。

### Q5: 有什么可以进一步探索的点？

本文提出的FileGram框架在基于文件系统行为轨迹的智能体个性化方面迈出了重要一步，但其仍存在局限性和广阔的探索空间。首先，论文指出“偏移归因”是当前的关键瓶颈，即系统能检测到行为异常，却难以精确解释其性质和方向。这提示未来研究需开发更精细的因果推理或可解释性模型，以理解行为变化的深层动因。其次，框架依赖模拟生成的数据（FileGramEngine），虽具规模但可能与真实用户行为的复杂性和随机性存在差距，未来需探索在严格隐私保护下利用真实脱敏轨迹进行微调或验证的方法。此外，FileGramOS从原子操作构建用户档案，但如何动态更新档案以适应长期行为演变，并有效区分临时波动与持久性“人格漂移”，仍需更强大的在线学习与遗忘机制。从更广视角看，该工作集中于文件系统，未来可探索跨平台（如邮件、即时通讯）行为轨迹的融合，以构建更全面的数字人格画像。最后，如何将此类个性化记忆系统高效、安全地集成至实际操作系统或协作代理中，并设计人性化的用户控制界面，也是走向实用化必须解决的工程与伦理问题。

### Q6: 总结一下论文的主要内容

本文提出了FileGram框架，旨在解决AI智能体在本地文件系统中作为人类协作者时面临的有效个性化难题。核心问题在于，由于严格的隐私限制和多模态真实行为轨迹难以联合收集，导致数据稀缺、评估方法不足，且现有方法以对话为中心，忽视了文件系统操作中密集的行为轨迹。

为此，FileGram包含三个核心组件：1) **FileGramEngine**：一个可扩展的、基于人物角色的数据引擎，用于模拟真实工作流并大规模生成细粒度的多模态操作序列，以解决数据稀缺问题。2) **FileGramBench**：一个基于文件系统行为轨迹的诊断性基准测试，用于评估记忆系统在用户画像重建、轨迹解耦、角色漂移检测和多模态关联等任务上的性能。3) **FileGramOS**：一种自底向上的记忆架构，直接从原子操作和内容增量（而非对话摘要）构建用户画像，并将这些轨迹编码为程序性、语义性和情景性记忆通道。

主要结论表明，现有先进的记忆系统在FileGramBench上表现不佳（准确率44.7%-50%），而FileGramOS通过其自底向上的架构达到了59.6%的准确率，验证了其有效性。分析揭示了当前方法在行为理解上能力有限，尤其在变化归因和多模态关联方面存在瓶颈。该框架为开发以记忆为中心、个性化的文件系统智能体提供了必要的数据、评估和结构基础。
