---
title: "Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use"
authors:
  - "Zhixin Ma"
  - "Yutong Zhou"
  - "Yongqi Li"
  - "Chong-Wah Ngo"
  - "Wenjie Li"
date: "2026-06-09"
arxiv_id: "2606.10803"
arxiv_url: "https://arxiv.org/abs/2606.10803"
pdf_url: "https://arxiv.org/pdf/2606.10803v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CV"
tags:
  - "物理工具使用"
  - "具身智能评估"
  - "多模态大语言模型基准"
  - "工具规划"
  - "场景理解"
relevance_score: 8.5
---

# Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

## 原始摘要

Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use. PhysTool-Bench comprises 2,510 queries over 2,678 real-world physical tools spanning diverse domains, including manufacturing, electrical work, agriculture, and healthcare. Concretely, models are evaluated along two primary dimensions: 1) recognizing all physical tools present in the scene, and 2) planning the tool selection and use sequence based on the instruction and visual context. Across 13 leading MLLMs, even the strongest model (Gemini-3.1-Pro) identifies only 58.7% of tools in a scene and completes merely 21.0% of queries end-to-end. Our analysis reveals a two-level deficit: MLLMs struggle to perceive tools in realistic scenes, and the much larger drop at the planning stage further indicates a lack of functional commonsense for mapping perceived tools onto task semantics, pinpointing a critical bottleneck for the development of practical embodied AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型(MLLMs)在物理世界工具使用中的能力缺失问题。当前研究背景是，MLLMs在数字工具使用方面取得了显著进展，能够通过API完成订票、数据库查询等结构化任务，并被视为具身AI的“大脑”，指导机器人执行交互任务。然而，现有方法主要聚焦于室内导航和物体操控，对物理工具使用的评估几乎空白。具体而言，MLLMs能否在真实场景中识别物理工具、理解其功能并根据指令规划使用顺序，仍是未解之谜。核心问题在于：MLLMs具备强大数字工具能力，但在面对物理世界时，其视觉感知和物理常识存在严重不足。本文引入PhysTool-Bench基准，包含2510个涉及2678种真实工具（涵盖制造、电气、农业、医疗等领域）的查询，系统评估MLLMs的两项能力：场景中所有工具的识别，以及基于指令的工具选择与行动规划。实验表明，最强模型Gemini-3.1-Pro仅识别出58.7%工具，端到端完成率仅21.0%，且大部分错误源于功能相似物替代，揭示出瓶颈并非感知能力，而是缺乏将感知工具映射到任务语义的物理常识。

### Q2: 有哪些相关研究？

相关研究主要分为方法类和评测类。方法类工作中，早期研究如SayCan、PaLM-E和RT-2探索了LLM在具身任务中的规划与执行，但聚焦于基础的“拾取-放置”或空间重排，将物体视为被动目标，未专门考察工具使用。RoboTool通过多智能体LLM流水线生成代码，实现机器人创造性使用工具，但其评估规模极小（仅6个场景），且依赖预定义状态，绕过了真实视觉感知的挑战。评测类工作中，现有基准（如工具学习benchmark）多局限于文本模态和数字API环境，评估LLM在工具选择与调用上的能力，未能涵盖视觉场景理解与物理工具操控。BEHAVIOR-1K虽涉及复杂物理交互，但未明确评估多模态基础模型对专业设备的零样本认知与规划能力。本文PhysTool-Bench的贡献在于：首次聚焦物理工具使用，从视觉识别和功能规划两个维度系统评估MLLM，且涵盖2,678个真实工具和2,510个查询，更全面地暴露了模型在真实场景感知与功能常识上的双重短板，弥补了现有工作在物理工具视觉识别与规划评估上的空白。

### Q3: 论文如何解决这个问题？

论文通过构建首个物理工具使用基准PhysTool-Bench，系统评估多模态大语言模型在真实场景中的工具感知与规划能力。核心方法围绕两个渐进式任务展开：任务一要求模型从场景图像中枚举所有可见工具（物理工具识别），任务二要求根据指令输出有序的工具选择与使用序列（工具选择与动作规划）。

架构设计采用三阶段流水线：首先通过人工种子集结合LLM扩展与干扰项回收机制，构建涵盖2678种真实物理工具的工具库；接着由Gemini等模型生成包含1-3个目标工具、3-10个干扰项的组合查询，并通过Nano Banana Pro渲染成包含随机遮挡的逼真场景；最后实施三级质量控制——QC-I验证工具与任务的专业相关性，QC-II确保图像描述与候选集严格对齐，QC-III人工过滤物理不合理或存在人工提示的图像。关键技术包括将有序与无序任务统一为带步标签的序列匹配，以及采用精确匹配、任务完成率和前k步成功率等多维度评估指标。

创新点在于：（1）首次聚焦物理工具使用的感知-规划二段式评估，揭示模型在现实场景中工具感知率仅58.7%（Gemini-3.1-Pro），而端到端完成率更低至21.0%；（2）通过系统性注入视觉相似和功能相近的干扰项，有效检测模型对功能常识的缺失；（3）发现从感知到规划的显著性能下降（近60%），指出缺乏将工具功能映射到任务语义的认知瓶颈是阻碍具身智能发展的关键。

### Q4: 论文做了哪些实验？

论文构建了PhysTool-Bench基准测试，包含2,510个查询，覆盖2,678个真实物理工具，横跨制造、电气、农业和医疗等领域。实验设置了两项任务：任务I要求模型识别场景中所有可见工具（顺序无关），任务II要求根据指令进行工具选择与使用序列规划（顺序敏感）。评估了13个前沿多模态大模型（MLLMs），包括GPT-4o、GPT-5.2、Gemini-3.1-Pro、Qwen3-VL-Plus等闭源模型，以及Deepseek-VL2、MiniCPM、OpenFlamingo等开源模型。主要结果：任务I中最佳模型Qwen3-VL-Plus的F1分数仅62.37%，多数模型低于50%；任务II中最强模型Gemini-3.1-Pro的精确匹配率（EM）仅20.96%，任务完成率（TCR）32.12%。SR@1最高55.83%（Gemini-3.1-Pro），但SR@3骤降至13.90%。进一步分析表明，模型在规划阶段的性能下降远超识别阶段（如Gemini-3.1-Pro在任务I中识别仅58.7%工具，任务II端到端完成仅21.0%），表明功能常识缺失是主要瓶颈。

### Q5: 有什么可以进一步探索的点？

该研究的局限在于工具类别覆盖仍不完整，尤其是长尾专业领域受限于视觉样本获取难度难以纳入；同时，静态场景评估忽略了动态状态变化和交互反馈，无法反映真实物理操作中的多轮推理需求。未来可探索的方向包括：1）构建交互式评估框架，允许模型在工具使用过程中提出额外视角查询或根据工件状态变化调整规划，更贴近具身智能的实际需求；2）针对功能性常识缺陷，开发显式的多步物理推理训练范式，例如结合因果推理或工具体验学习——让模型通过模拟或真实反馈建立“工具-操作-结果”的关联；3）引入专用检测器与MLLM的闭环协作，弥补感知粒度不足，同时利用人类标注的细粒度功能属性来增强规划模块对工具语义映射的理解。突破瓶颈的关键或在于将物理世界运作的因果逻辑内化到模型参数中，而非单纯扩大视觉编码器的规模。

### Q6: 总结一下论文的主要内容

本文介绍了PhysTool-Bench，这是首个专门评估多模态大模型（MLLM）在物理世界中工具使用能力的基准。问题定义上，现有MLLM在数字API工具使用上表现出色，但在物理工具识别、选择和规划方面能力未知。方法上，基准包含2510个查询和2678个真实物理工具，覆盖制造、电气、农业和医疗等多个领域，通过两个任务进行评估：任务1要求识别场景中所有工具，任务2要求根据指令正确选择和排序工具。主要结论是，即使最强的模型（Gemini-3.1-Pro）也仅能识别58.7%的工具，端到端完成21.0%的查询。分析显示存在两级缺陷：模型在真实场景中感知工具困难，更大的瓶颈在于缺乏将感知到的工具映射到任务语义上的功能常识，这导致大量错误（42-61%）源于混淆功能相似的替代工具。该研究首次揭示了物理工具使用是MLLM从数字智能向具身AI发展的关键瓶颈，并指出现有瓶颈在于物理常识推理而非感知能力。
