---
title: "SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking"
authors:
  - "Guohong Liu"
  - "Jialei Ye"
  - "Pengzhi Gao"
  - "Wei Liu"
  - "Jian Luan"
  - "Yunxin Liu"
  - "Yuanchun Li"
date: "2026-05-24"
arxiv_id: "2605.25160"
arxiv_url: "https://arxiv.org/abs/2605.25160"
pdf_url: "https://arxiv.org/pdf/2605.25160v1"
categories:
  - "cs.AI"
tags:
  - "Mobile GUI Agent"
  - "Benchmark"
  - "LLM"
  - "Synthetic Environment"
  - "Evaluation"
relevance_score: 9.0
---

# SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking

## 原始摘要

Mobile GUI agents powered by large language models have progressed rapidly, creating urgent needs for realistic and comprehensive evaluation. Existing benchmarks prioritize reproducibility but are often limited to open-source apps or file-operation tasks for the difficulty of constructing rewards on real applications, leaving a gap between benchmark settings and real-world usage. Moreover, most benchmarks focus on basic grounding and navigation, with limited coverage of complex, long-horizon interactions. To address these limitations, we introduce SimuWoB, a fully synthetic benchmark for mobile GUI agents with 120 challenging tasks spanning diverse types and difficulty levels. We build a robust virtual environment generation framework that synthesizes high-fidelity tasks and environments, and automatically provides valid rewards for each task. Each environment is deployed as a backend-free webpage accessible via URL, enabling efficient and reproducible evaluation. We conduct comprehensive experiments on several state-of-the-art mobile GUI agents. The average success rate is only 27.92%, dropping to 17.82% on long-horizon tasks, which reveals substantial weaknesses in current agents under complex scenarios. Evaluation result comparison with real-world sample tasks demonstrate that agent assessments based on our synthetic environment generalize well. We further provide diagnostic insights across key capability dimensions and discuss implications for future mobile GUI agent development.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有移动图形用户界面（GUI）智能体基准测试中存在的三个核心问题。首先，研究背景显示，尽管基于大语言模型的移动GUI智能体发展迅速，但现有的基准测试为了追求可重复性，大多局限于开源的应用程序或文件操作类任务，难以在真实应用程序上构建奖励函数，导致基准测试与真实世界应用场景之间存在显著差距。其次，现有基准测试的任务复杂性有限，多数侧重于基础的视觉定位和简单导航，缺乏对需要长周期执行、中间信息管理和多步推理等复杂任务的覆盖，无法有效指导智能体的下一步发展。最后，许多交互式基准测试依赖模拟器或虚拟设备，导致系统复杂度和运行开销高，评估效率低下。本文提出SimuWoB，通过构建一个完全合成的基准测试环境，利用大语言模型自动生成高保真的模拟网页应用和交互逻辑，并自动验证任务的可解性与提供有效的奖励函数，解决了上述问题。其核心在于实现一个无需后端、可通过URL访问的轻量级评估框架，支持高效、可复现且更贴近真实场景的移动GUI智能体评估。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **静态数据集**：如早期的GUI grounding数据集和指令跟随数据集，基于截图或UI树进行离线评估。本文指出这些方法无法捕捉闭环交互（如错误恢复、多步依赖），而SimuWoB提供可执行的虚拟环境，支持端到端任务评估。

2. **交互式基准**：包括基于容器、模拟器或VM快照的平台（如AndroidEnv、MobileEnv、WebArena等），它们提高了可重复性但工程成本高。本文通过合成无后端的URL可访问环境，显著降低了资源消耗和重置开销，同时保持高保真度。

3. **复杂任务基准**：现有工作（如OSWorld、AgentBench）主要覆盖短程或结构简单的任务，对长程、模糊、复合推理任务覆盖不足。SimuWoB专门设计了120个包含长时间跨度、模糊指令和复杂推理的高难度任务，平均成功率仅27.92%，远低于现有基准。

4. **奖励构建方法**：许多基准依赖开源应用或文件操作来获取可访问的内部状态，而SimuWoB通过合成环境自动提供有效奖励，无需手动规则工程，解决了真实应用中奖励难获取的瓶颈。

本文的核心区别在于通过全合成但高保真的环境，同时实现了现实性、任务覆盖广度、奖励可扩展性和评估效率，弥补了现有基准在复杂真实场景与可重复性之间的鸿沟。

### Q3: 论文如何解决这个问题？

SimuWoB通过一个两阶段的全合成环境生成流水线来解决现有移动GUI代理基准测试中真实性与可复现性不足的问题。核心设计是首先构建高保真的应用模拟，再注入基准任务和验证器。

**整体框架**分为两阶段：第一阶段构建最小工作环境（MWE），利用代码生成LLM（如Gemini或Claude）迭代生成产品需求文档（PRD），并基于PRD实现页面结构、数据模式和交互逻辑，经过多轮自检和修订形成可执行UI逻辑和初始数据的稳定环境。第二阶段进行任务注入和奖励合成，先在MWE基础上扩展数据库内容，然后由任务注入代理扫描代码库，为每个任务生成可执行的验证器。由于环境状态转换的细粒度控制，验证器能精确检查成功条件而非依赖近似模式匹配。

关键技术包括：一是通过任务与环境的共生成机制避免过拟合，即在同一应用上下文中共同生成多个相关任务，而非孤立注入；二是设计了人机协作的缺陷检测与修复循环，对每个环境包进行多步验证，由验证代理执行任务，失败轨迹交由人类专家分类，环境缺陷反馈回生成管线修复。最终所有环境都经过手动验证确保质量。

创新点在于完全合成但高保真的环境能同时实现现实的交互模式和大规模可靠奖励评估，覆盖33个Google Play应用类别中的20个（超过60%），包含120个跨语言、有/无返回值、简单/长程/数学相关等多样任务，平均成功率仅27.92%，长程任务更低至17.82%，有效暴露了当前智能体的弱点。

### Q4: 论文做了哪些实验？

论文在SimuWoB基准上评估了5个主流移动GUI智能体：API模型包括UI-TARS-1.5、doubao-seed-1.8和Gemini 3 Pro，开源微调模型包括MAI-UI-8B和GUI-Owl-1.5-8B。实验使用8个并行worker，主指标为成功率(SR)，每个轨迹上限100步，所有结果取两次运行平均。主要结果如下：在无返回值任务中，seed-1.8达到50.00%，Gemini 3 Pro达45.27%，UI-TARS-1.5达39.86%；在有返回值任务中，三者SR分别降至30.43%、28.26%和13.04%。所有模型在SimuWoB上的平均SR仅27.92%，远低于在AndroidWorld上的69.38%。在长程任务上平均SR仅17.82%，简单子集为56.48%，显示明显能力差距。人类平均SR为92.08%。为验证泛化性，论文设计了20个真实应用样本任务进行评估，发现模型排名与合成环境一致。此外，对11个需要精细控制（如拖拽滑块、日期选择器）的任务进行专项分析，Gemini 3 Pro完成5/11个任务，其他模型平均仅完成0.5-1.5个。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在两个核心方向：一是当前仅依赖Web渲染的视觉观测空间，无法完全模拟真实Android系统中的可访问性树等结构化信号，这限制了Agent对层级布局与元素语义的理解能力。未来可探索混合观测框架，在合成环境中同步生成近似真实系统的结构化数据接口。二是任务局限于单应用流程，缺少跨应用协同场景。这可通过扩展环境生成框架实现，例如用LLM自动设计涉及多应用数据传递的复合任务，并设计跨应用状态机验证奖励。此外，当前长时域任务成功率仅17.82%，说明Agent的规划与错误恢复能力薄弱，可引入逐步奖励分解或分层强化学习策略。未来方向包括：构建动态对话式任务生成机制以规避记忆效应，以及利用大模型自动校验环境语义保真度，缩小合成与现实场景的泛化差距。

### Q6: 总结一下论文的主要内容

SimuWoB是一个面向移动GUI智能体的全合成基准测试，旨在解决现有基准在真实性和复杂性上的不足。现有基准多聚焦于开源应用或文件操作任务，难以在真实应用中构建奖励，且任务偏重基础导航，缺乏对长周期复杂交互的覆盖。论文核心贡献是提出了一个基于大语言模型的虚拟环境生成框架，能自动构建高保真、无需后端的可交互网页环境，并为每项任务提供有效的自动奖励。该基准包含120个源自真实场景的挑战性任务，覆盖多种类型和难度。实验表明，当前最先进智能体的平均成功率仅为27.92%，在长周期任务上更是降至17.82%，揭示了其在复杂场景下的显著缺陷。通过与真实样本的对比，证实了该合成环境的评估具有良好的泛化性。这项工作为衡量进展和指导下一代移动GUI智能体研究提供了一个可扩展且实用的测试平台，并诊断出智能体在主动探索和细粒度动作控制方面的弱点。
