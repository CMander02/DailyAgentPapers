---
title: "Can Agents Read the Room? Benchmarking Visual Social Intelligence in Multimodal Simulation"
authors:
  - "Shijun Wan"
  - "Xuehai Wu"
  - "Jiwen Zhang"
  - "Siyuan Wang"
  - "Zhongyu Wei"
date: "2026-06-13"
arxiv_id: "2606.15152"
arxiv_url: "https://arxiv.org/abs/2606.15152"
pdf_url: "https://arxiv.org/pdf/2606.15152v1"
github_url: "https://github.com/JunsWan/AgentViSS"
categories:
  - "cs.CL"
tags:
  - "多模态智能体"
  - "社交智能"
  - "视觉智能"
  - "评测基准"
  - "角色扮演"
  - "交互管理"
relevance_score: 8.5
---

# Can Agents Read the Room? Benchmarking Visual Social Intelligence in Multimodal Simulation

## 原始摘要

Social interaction depends on both language and visible social signals, such as facial expressions, posture, gaze, and emotional shifts. Yet existing social-agent benchmarks are largely text-based and rarely test whether multimodal agents can use visual cues to guide interaction. We introduce \textsc{\benchmarkname{}}, a benchmark evaluating visual social intelligence in multimodal social simulation. It contains 240 scenarios, 585 role instances, and 2,340 role-task instances, combining aligned textual-visual evidence, structured role profiles, and four role-level tasks: expression task, characteristic task, interaction regulation task, and interaction outcome task. Evaluating seven recent MLLMs under verbalized-vision and direct-vision reveals a clear gap between local role enactment and interaction management: role-specific expression and conflict handling are near saturation, whereas interaction regulation and visually grounded outcome achievement remain substantially more difficult. The code is released at https://github.com/JunsWan/AgentViSS, and the dataset is available at https://huggingface.co/datasets/JunsWan/AgentViSS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态智能体在社交仿真中缺乏视觉社会智能评估的问题。研究背景指出，真实社交互动不仅依赖语言，还依赖面部表情、姿态、目光等可见的社会信号，但现有的社交智能体基准测试大多是纯文本的，很少测试多模态智能体是否能利用视觉线索来指导互动。现有方法的不足主要体现在三个方面：第一，纯文本环境无法复现塑造现实社交的可见线索，导致智能体感知和响应这些信号的能力未经测试；第二，场景设计往往无法捕捉日常社交的复杂性，如人际冲突、信息不对称或策略性间接表达；第三，评估标准通常简化为是否达成顶层目标，而忽略了智能体是否维持自身角色状态或追踪其他参与者的动态状态。因此，本文提出的核心问题是：当前的多模态智能体能否利用视觉社交信号做出恰当的交互决策？为了解决这一问题，论文引入了AgentViSS基准，通过结合对齐的文本-视觉证据、结构化角色档案和四个角色级任务（表达任务、特征任务、交互调节任务和交互结果任务），在多模态社交仿真中系统评估视觉社会智能，并揭示了智能体在局部角色扮演上接近饱和，但在交互管理和基于视觉的结果达成方面仍存在显著困难。

### Q2: 有哪些相关研究？

相关研究可分为两大类。第一类是**社交代理与仿真**，包括评估目标驱动交互（如合作、冲突、谈判）的社交代理基准，以及侧重于人格一致性、角色扮演和群体动态的角色扮演基准。生成式代理系统进一步模拟了记忆增强的社会和长期社会行为。这些工作主要基于文本，很少考察视觉证据如何影响代理的逐轮决策。第二类是**多模态社交理解**，包括从文本、音频、图像或视频中评估情感和关系推断的多模态数据集，以及扩展到多模态心智理论和情绪变化的基准。本文提出的AgentViSS基准与它们的区别在于：专注于仿真中的**视觉社交智能**，不仅评估局部角色扮演（如表情、特征任务），还评估交互管理（如交互调节和结果任务）。现有工作大多局限于单一层面，而AgentViSS通过结构化角色档案和四种角色级任务，系统性地将视觉证据整合到多轮社交仿真中，填补了多模态代理在复杂社交情境中视觉线索利用能力的评估空白。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为AgentViSS的多模态社交模拟基准，系统性地评估多模态大模型在社交交互中的视觉社交智能。核心方法包括三个主要部分：

1. **数据构建流水线**：从《老友记》剧本和视频中提取240个社交场景，通过脚本对齐、视觉证据选择和场景描述构建，生成包含群像图、角色肖像、场景描述、结构化角色档案（表达风格和冲突特征）、初始情感状态以及四项角色级任务的标准化输入。

2. **仿真框架设计**：采用两种观测模式——语言化视觉（将图像转为文本描述）和直接视觉（直接输入图像），让多个智能体轮流交互。每轮交互中，激活的智能体接收当前对话历史、自身档案和情感状态，以及视觉信息，输出公开消息、内心想法、更新情感状态和下一发言者建议。系统动态更新对话历史和情感状态，并通过图像编辑模型更新角色肖像。

3. **评估机制**：对每个角色的四项任务（表达任务、特征任务、交互调控任务和交互结果任务）分别评分，使用三个评判模型进行多数投票。创新点在于区分了角色扮演任务（表达和特征）和交互管理任务（调控和结果），揭示了当前MLLMs在角色扮演上接近饱和（平均94.37分）但在交互管理上仍存在显著差距（平均57.39分），且直接视觉模式在交互调控上明显弱于语言化视觉模式。

### Q4: 论文做了哪些实验？

论文评估了七种多模态大语言模型在视觉社交智能基准测试上的表现。实验设置包括两种观察模式：语言化视觉和直接视觉。数据集包含240个场景、585个角色实例和2340个角色任务实例，涵盖四个角色级任务：表达任务、特征任务、交互调节任务和交互结果任务。评估采用三个裁判模型（Gemini-3.1-pro-preview、GPT-5.4、Qwen3.5-27B）进行多数投票，将任务完成情况分为“完成”、“部分完成”或“未完成”，并计算归一化得分。对比方法包括Claude、GPT、Qwen、GLM和InternVL系列模型。主要结果：角色执行任务接近饱和，平均得分94.37；交互管理任务更具挑战性，平均得分57.39，Claude-Sonnet-4.6表现最佳（71.32）。进一步分析发现，直接视觉模式下交互调节得分（31.21）显著低于语言化视觉模式（49.60），差距达18.39分。在强视觉依赖的交互结果任务上，所有模型得分从77.42下降到56.53。与纯文本基线相比，两种视觉模式均表现更好，表明视觉信息有益但模型仍难以将其有效转化为交互决策。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向包括：首先，场景仅取自单一西方情景喜剧（《老友记》），缺乏跨文化、职业及非英语社会规范的代表性，未来应扩展至多元文化背景的数据集，提升泛化能力。其次，当前使用固定帧的群像和角色肖像而非连续视频，未能捕捉目光转移、微表情等时序线索，后续可引入视频流或多帧动态分析，增强对非言语信号的建模。第三，任务评分依赖LLM作为裁判的三标签投票体系，可能引入与待评估模型相似的偏差，且粗粒度评分难以区分社交恰当性的细微差异，可探索更细粒度的评分体系或结合人类评估。此外，观察到本地角色扮演与交互管理能力间的差距，推测现有模型缺乏对全局社交动态的推理机制，可尝试引入图神经网络或记忆增强模块以建模多轮交互中的依赖关系。最后，当前任务设计以预设角色任务为导向，未来可加入开放式社交场景，测试模型自主感知与自适应决策的协同能力。

### Q6: 总结一下论文的主要内容

该论文提出了AgentViSS，一个用于评估多模态社会模拟中视觉社交智能的基准。其核心问题是：当前多模态智能体能否利用面部表情、姿势等视觉社交线索做出恰当的交互决策？AgentViSS基于《老友记》场景构建了240个场景、585个角色实例和2340个角色任务实例，结合了文本与视觉证据，并定义了四个评估维度：表情任务、特征任务、交互调节任务和交互结果任务。通过评估七个多模态大语言模型，研究发现：在局部角色扮演方面，模型表现趋于饱和，但在交互调节任务和视觉线索驱动的结果实现任务上表现困难，特别是当视觉信息以原始图像输入而非文本描述形式呈现时。这表明当前模型存在从视觉感知到决策整合的瓶颈，难以将视觉线索有效转化为社交决策依据。该基准揭示了多模态智能体在视觉驱动的交互管理能力上的显著不足。
