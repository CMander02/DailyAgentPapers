---
title: "CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing"
authors:
  - "Haobo Hu"
  - "Xiangwu Guo"
  - "Zhiheng Chen"
  - "Difei Gao"
  - "Haotian Liu"
  - "Libiao Jin"
  - "Qi Mao"
date: "2026-05-19"
arxiv_id: "2605.19484"
arxiv_url: "https://arxiv.org/abs/2605.19484"
pdf_url: "https://arxiv.org/pdf/2605.19484v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.GR"
  - "cs.HC"
tags:
  - "GUI Agent Benchmark"
  - "Compositional GUI Agents"
  - "Media Post-Production Editing"
  - "Long-Horizon Task"
  - "Autonomous GUI Agents"
  - "Multimodal Inference"
relevance_score: 9.0
---

# CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing

## 原始摘要

While GUI agents have made significant progress in web navigation and basic operating system tasks, their capabilities in professional creative workflows remain largely underexplored. To bridge this gap, we introduce Cutverse, a benchmark designed to systematically evaluate autonomous GUI agents in realistic media post-production environments. We curate expert demonstrations across 7 professional applications (e.g., Premiere Pro, Photoshop), covering 186 complex, long-horizon tasks grounded in authentic editing workflows, involving dense multimodal interfaces and tightly coupled interaction sequences. To support scalable evaluation, we develop a lightweight parser that transforms raw screen recordings and low-level interaction logs into structured, compositional GUI action trajectories with precise grounding. Extensive evaluations reveal that existing agents achieve only 36.0\% task success on realistic media editing tasks, underscoring the challenges posed by complex, long-horizon media post-production workflows in our benchmark.While current models demonstrate promising spatial grounding, multimodal alignment, and coordinated action execution, they remain limited in long-horizon reliability and domain-specific planning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前GUI智能体在专业创意工作流，特别是媒体后期制作领域评估缺失的问题。研究背景是，尽管GUI智能体在网页导航和基础操作系统任务上取得了显著进展，但它们在专业创意软件（如Premiere Pro、Photoshop）中的能力尚未得到充分探索。现有方法的不足主要体现在两方面：一是现有基准测试主要针对轻量级、结构化的通用场景，无法覆盖媒体后期制作中高密度界面、精细交互、长执行跨度及多模态紧密耦合的操作序列（如时间线操控、图层合成、参数调优等）；二是缺乏支持高保真、资源密集型场景（如高内存占用、复杂动态系统状态）的可扩展评估基础设施。为此，本文提出的核心问题是：如何构建一个能够系统评估GUI智能体在真实媒体后期制作环境中完成复杂、长程协作任务能力的基准，并揭示现有智能体在空间定位、时序协调及组合操作等方面的性能瓶颈。通过设计包含186个复杂任务、覆盖7款专业软件的CutVerse基准，论文旨在填补专业创意领域自动化评估的空白。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **AIGC agents**：这类工作采用规划器-执行器范式和工具增强来自动化多模态内容生成，但主要关注粗粒度语义对齐和高层视觉一致性，无法胜任专业媒体后期制作中细粒度的视频特效、精确时间线操作和复杂转场编辑等精细操作。

2. **GUI agents**：近期基于VLM的GUI代理在网页导航和操作系统等通用领域展现出强大交互能力，能够连接自然语言指令与可执行操作。然而，专业媒体后期制作这一领域仍严重未被探索，现有GUI基准大多局限于简化、短步交互。

3. **媒体创意基准**：现有评测主要评估生成内容的感知质量和语义保真度，但局限于静态输出评估，缺乏评估专业创作工具交互密度的标准化协议。

本文与这些工作的区别在于：CutVerse首次聚焦于专业级媒体后期制作环境（如Premiere Pro、Photoshop），提出186个复杂长视界任务，通过里程碑驱动的轨迹评估框架，将评估从静态输出转向动态、基于轨迹的专业媒体操作验证，系统填补了GUI代理在专业创意工作流中的评估空白。

### Q3: 论文如何解决这个问题？

CutVerse通过构建一个端到端的评估管线来解决现有GUI智能体在专业媒体后期制作中的不足。核心方法包括三个模块：数据记录、多模态解析和双模式评估。架构上，智能体部署在可重置的Windows虚拟机上，只能通过鼠标拖拽、坐标点击和键盘快捷键等拟人化操作与软件交互，模拟人类认知运动循环；这避免了使用特权级API，使得评估更贴近真实场景。

关键技术方面，CutVerse开发了一个轻量级解析器，能将原始屏幕录制和低级交互日志转化为结构化的、组合式的GUI动作轨迹，并对每个步骤进行精确的视觉状态关联。该解析器还进一步将长任务分解为层次化的语义里程碑，对应到原子能力（如时间线导航、参数微调、跨模态资产检索），从而实现细粒度的诊断分析。创新点包括：1）覆盖7个商业软件（Premiere Pro、After Effects、ComfyUI等）和186个长任务，任务平均步长18.73步，远超标准Web导航基准；2）通过时间线和多轨界面推动评估瓶颈从点选到像素级视听定位；3）支持动态多模态输入（视频画布、音频波形、参数面板），要求智能体具备跨模态对齐和时空同步能力。实验表明，现有最强的智能体（如Claude Opus-4.6）整体任务成功率仅68.3%，在核心编辑任务上更是低至45.1%。

### Q4: 论文做了哪些实验？

论文在CutVerse基准上进行了全面的在线实验，评估了5个视觉语言模型：Claude-Opus-4.6、Gemini-3-flash（通过API访问），以及Qwen3-32B、UI-TARS-1.5-7B、EvoCUA-32B（本地部署于4块RTX 5090）。实验在统一Windows 11 Pro虚拟机中进行，任务初始化状态、文件、软件配置完全一致。代理需根据任务描述和实时截图自主生成pyautogui操作，形成闭环执行。

实验覆盖7款专业软件（Keling、ComfyUI、JianYing、DaVinci、Premiere Pro、Photoshop、After Effects）共186个长时任务。主要结果：整体任务成功率仅36.0%；分软件看，Claude在Keling上最高（81.5%），Gemini在ComfyUI上最高（83.3%），而After Effects上表现最差（Claude 57.7%，其他低于35%）。

关键发现：（1）在程序化操作（如生成工作流、导出）中所有模型成功率接近1.0；（2）核心媒体编辑任务（如蒙版、抠图、特效调优）性能急剧下降，UI-TARS在遮罩任务中仅9.5%，Claude和Gemini也仅28.6%和38.1%；（3）里程碑成功率与任务成功率存在显著差距，如Claude在音频编辑中里程碑成功率达92.9%，但最终任务成功率仅33.3%，表明高中间步骤准确率不等同于完整任务完成。典型失败模式包括组件误识别和像素级定位不精确。

### Q5: 有什么可以进一步探索的点？

基于论文分析，当前GUI智能体在专业媒体后期制作中存在显著局限：在长周期、高密度交互的核心编辑任务（如特效、音频节奏调整）中成功率仅36%，且容易陷入静态视觉反馈导致的死循环。未来可探索的方向包括：1）改进跨模态对齐机制，特别是音频-视觉信息的动态融合，因为现有模型在After Effects等密集视觉界面中容易过载；2）引入状态感知的规划模块，避免因缺乏界面状态变化反馈而重复无效点击；3）设计领域特定的抽象动作原语，将复杂的编辑操作（如遮罩追踪）分解为可组合的子步骤，提升长程任务可靠性；4）利用结构化生成工具（如ComfyUI）的中间表征来引导专业软件的交互，实现跨工具的知识迁移。此外，当前基准测试局限于桌面端，可扩展至支持协同编辑的云原生环境，并纳入用户创造力评价维度。

### Q6: 总结一下论文的主要内容

CutVerse 是一个专门用于评估自主GUI代理在专业媒体后期制作环境中能力的基准。针对现有代理在专业创意工作流中能力未被充分探索的问题，该基准涵盖了Premiere Pro、Photoshop等7个专业应用中的186个复杂、长周期的任务，这些任务基于真实的编辑流程，涉及密集的多模态界面和紧密耦合的交互序列。为了支持可扩展评估，他们开发了一个轻量级解析器，将原始屏幕录制和低级交互日志转化为结构化的、组合性的GUI动作轨迹。广泛评估显示，现有代理在真实媒体编辑任务上的成功率仅为36.0%，凸显了复杂、长周期媒体后期制作工作流的挑战。该研究的核心贡献在于定义了一个更具挑战性的评估场景，揭示了当前模型在空间定位、多模态对齐和协调动作执行方面虽有进展，但在长周期可靠性和特定领域规划方面存在明显不足，对推动更强大、更可靠的自主GUI代理研发具有重要意义。
