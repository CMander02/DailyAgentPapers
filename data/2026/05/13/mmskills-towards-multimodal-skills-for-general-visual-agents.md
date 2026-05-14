---
title: "MMSkills: Towards Multimodal Skills for General Visual Agents"
authors:
  - "Kangning Zhang"
  - "Shuai Shao"
  - "Qingyao Li"
  - "Jianghao Lin"
  - "Lingyue Fu"
  - "Shijian Wang"
  - "Wenxiang Jiao"
  - "Yuan Lu"
  - "Weiwen Liu"
  - "Weinan Zhang"
  - "Yong Yu"
date: "2026-05-13"
arxiv_id: "2605.13527"
arxiv_url: "https://arxiv.org/abs/2605.13527"
pdf_url: "https://arxiv.org/pdf/2605.13527v1"
categories:
  - "cs.AI"
tags:
  - "多模态Agent"
  - "技能表示与复用"
  - "视觉Agent"
  - "GUI Agent"
  - "技能生成"
  - "工具使用"
  - "推理时决策"
  - "Agent框架"
relevance_score: 8.5
---

# MMSkills: Towards Multimodal Skills for General Visual Agents

## 原始摘要

Reusable skills have become a core substrate for improving agent capabilities, yet most existing skill packages encode reusable behavior primarily as textual prompts, executable code, or learned routines. For visual agents, however, procedural knowledge is inherently multimodal: reuse depends not only on what operation to perform, but also on recognizing the relevant state, interpreting visual evidence of progress or failure, and deciding what to do next. We formalize this requirement as multimodal procedural knowledge and address three practical challenges: (I) what a multimodal skill package should contain; (II) where such packages can be derived from public interaction experience; and (III) how agents can consult multimodal evidence at inference time without excessive image context or over-anchoring to reference screenshots. We introduce MMSkills, a framework for representing, generating, and using reusable multimodal procedures for runtime visual decision making. Each MMSkill is a compact, state-conditioned package that couples a textual procedure with runtime state cards and multi-view keyframes. To construct these packages, we develop an agentic trajectory-to-skill Generator that transforms public non-evaluation trajectories into reusable multimodal skills through workflow grouping, procedure induction, visual grounding, and meta-skill-guided auditing. To use them, we introduce a branch-loaded multimodal skill agent: selected state cards and keyframes are inspected in a temporary branch, aligned with the live environment, and distilled into structured guidance for the main agent. Experiments across GUI and game-based visual-agent benchmarks show that MMSkills consistently improve both frontier and smaller multimodal agents, suggesting that external multimodal procedural knowledge complements model-internal priors.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前视觉智能体在技能重用上的一个核心矛盾：现有技能库（如文本提示、代码或执行图）主要编码行为步骤，但对依赖视觉证据的智能体而言，**可重用的程序性知识本质上是多模态的**——它不仅需要描述“做什么”，还必须包含“如何识别视觉状态”、“何时执行/跳过”、“如何通过视觉信号验证进展”这些状态依赖的决策信息。现有方法要么依赖冗长却模糊的纯文本技能，丢失视觉上下文；要么使用演示轨迹，但难以泛化且不具可复用性。因此，本文要解决的核心问题是：**如何形式化、自动化构建并高效利用这种“多模态程序性知识”**。具体包括三个子挑战：(1) 多模态技能包应该包含什么内容（表示问题）；(2) 如何从公开的非测试交互轨迹中自动生成这些技能包（生成问题）；(3) 在推理时，智能体如何查阅多模态技能证据而不引入过多图像上下文或过度锚定到参考截图（利用问题）。

### Q2: 有哪些相关研究？

### 相关研究

本文的相关工作可从三个类别进行梳理：

**1. 技能复用类方法**：传统技能复用源于时间抽象和运动基元，近期LLM代理将可复用行为存储为语言、代码、API或学习库。另一条思路将累积经验视为长期记忆，同时有评测基准评估技能的相关性、选择性和安全性。MMSkills遵循模块化视角，但存储状态条件的多模态包，并通过分支加载（而非插入完整技能记忆）进行使用。

**2. 视觉代理基础能力**：视觉代理基准涵盖网页、移动端、桌面和具身环境，现有模型和框架改进了截图理解与GUI控制能力，专用的定位基准则衡量模型定位UI元素的能力。MMSkills构建于这些基础之上，但层次更高：它告诉代理哪些程序状态是重要的，以及哪些视觉证据可以确认该状态。

**3. 最相关工作**：Mirage-1引入了层次化多模态技能，XSkill从视觉经验中提取技能，CUA-Skill将计算机使用技能表示为参数化程序和执行图。MMSkills的区别在于：围绕运行时状态卡和多视角证据组织技能，并通过分支加载将选中的证据与实时环境对齐，再为主体代理生成结构化引导。

### Q3: 论文如何解决这个问题？

MMSkills通过三部分设计解决视觉智能体如何表示、生成和使用多模态程序性知识的问题。核心是多模态技能包、技能生成管道和分支加载推理机制。

**多模态技能包** 是紧凑的状态条件化包，包含四部分：描述符D、可重用文本化流程P、运行时状态卡集合S（含何时使用/何时不使用条件、可见线索、验证线索、可用视图）以及多视角关键帧集合K（含全局帧、聚焦裁剪、前后对比帧）。这些组件将程序化知识、决策条件和视觉证据绑定为一个可重用单元，弥补了纯文本技能的不足。

**技能生成管道** 利用一个元技能引导的生成器，将公开非评估轨迹转换为多模态技能库。分为五个阶段：阶段0对任务指令进行嵌入和聚类；阶段1通过LLM基于聚类提出原子技能边界；阶段2合并去重生成规范化技能；阶段3不依赖图像起草文本描述和流程；阶段4通过视觉定位和审计完善关键帧绑定。该管道保守添加视图，仅用于状态识别、转换比较或完成验证，避免过度存储。

**分支加载推理** 在推理时将环境定位过程隔离到临时分支，避免参考图像干扰主轨迹。第一步进行门控视图选择，根据当前观测和历史仅加载相关的状态卡和视图；第二步在分支中对齐证据并输出结构化指导G_t，包含适用性判断、局部子目标、技能条件化计划、负约束和视觉验证。主智能体使用G_t作为决策支持，但动作仍基于实时观测，从而保护了程序化指导而不让参考图像覆盖当前状态。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了实验：OSWorld (桌面GUI任务)、macOSWorld (macOS GUI任务)、VAB-Minecraft (游戏任务) 和 Super Mario Bros (游戏任务)。实验设置了三种技能条件对比：无技能、纯文本技能和MMSkills，评估了多个前沿与小规模多模态模型（如Gemini 3.1 Pro、Gemini 3 Flash、Qwen3-VL-235B、GLM-5V、Kimi-K2.6和Qwen3-VL-8B-Instruct）。主要结果包括：在OSWorld上，MMSkills使Gemini 3.1 Pro的总体成功率从44.08%提升至50.11%，Qwen3-VL-235B从21.34%提升至39.17%，小模型Qwen3-VL-8B从10.78%提升至25.40%；在VAB-Minecraft上，该模型成功率从23.28%提升至38.79%；在macOSWorld和Super Mario Bros上也观察到一致提升。消融实验显示：移除状态卡或图像分别削弱了状态判别和视觉定位能力；分支加载优于直接加载，且完整的MMSkills包效果最佳。行为分析表明，MMSkills使技能调用更频繁（如Qwen3-VL-235B在OSWorld上调用率从37.50%升至65.28%），同时平均步骤数减少（在该模型上减少5.35步），说明多模态技能帮助智能体更高效地完成任务。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要集中在三个方面：首先，MMSkills高度依赖源轨迹的覆盖范围，若训练数据中缺乏特定领域或罕见操作的轨迹，技能生成质量会显著下降，这限制了其在长尾场景中的泛化能力。其次，技能生成和视觉定位环节存在累积误差，例如多视图关键帧的选取可能因相似状态而产生歧义，导致分支加载时对齐失败。最后，分支加载机制虽然缓解了图像上下文过载问题，但额外计算成本在资源受限设备上不可忽视。

未来的探索方向包括：1) 引入在线技能修复机制，通过实时环境反馈动态调整状态卡和关键帧，减少对离线生成质量的依赖。2) 设计层次化技能库，结合元学习自动聚类相似轨迹，在保证覆盖率的同时压缩冗余技能包。3) 探索轻量化视觉编码器与交叉注意力机制，在低算力场景下实现分支加载与主代理的高效协同。此外，将该框架迁移至具身导航或安全关键任务（如手术机器人）时，需融入因果推理约束，确保动作选择符合物理定律与伦理规范。

### Q6: 总结一下论文的主要内容

这篇论文提出了MMSkills框架，旨在为通用视觉智能体定义、生成和运用多模态技能。其核心问题在于：传统的技能包（如文本提示或代码）无法充分表达视觉决策所依赖的“多模态程序性知识”，这种知识不仅包括“做什么”，还涉及“识别当前状态”和“判断视觉证据”。论文的贡献在于：首先，形式化了多模态技能包应包含的内容（文本程序、运行时状态卡片、多视角关键帧）；其次，设计了一个从公开交互轨迹自动生成这些技能包的生成器，通过工作流分组、程序归纳、视觉定位和元技能审计完成；最后，引入了一种分支加载的多模态技能智能体，在推理时通过临时分支审查关键帧并与实时环境对齐，为主智能体提供结构化指导。实验表明，该框架在GUI和游戏类基准测试中持续提升了前沿模型和较小模型的表现，证明了外部的多模态程序性知识能够有效补充模型内部先验知识。主要结论是，多模态技能是一种可泛化、可复用的视觉决策资源，能显著提升视觉智能体在复杂环境中的适应能力。
