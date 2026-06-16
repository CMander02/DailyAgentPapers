---
title: "LabOSBench: Benchmarking Computer Use Agents for Scientific Instrument Control"
authors:
  - "Anqi Zou"
  - "Han Deng"
  - "Chengyu Zhang"
  - "Junquan Hu"
  - "Yu Wang"
  - "Yuxiang Xing"
  - "Aokai Zhang"
  - "Hanling Zhang"
  - "Zhaoyang Liu"
  - "Ben Fei"
  - "Zhihui Wang"
  - "Wanli Ouyang"
date: "2026-06-15"
arxiv_id: "2606.16802"
arxiv_url: "https://arxiv.org/abs/2606.16802"
pdf_url: "https://arxiv.org/pdf/2606.16802v1"
categories:
  - "cs.AI"
tags:
  - "Benchmark"
  - "GUI Agent"
  - "Scientific Instrument Control"
  - "Vision-Language Model"
  - "Agent Evaluation"
relevance_score: 7.5
---

# LabOSBench: Benchmarking Computer Use Agents for Scientific Instrument Control

## 原始摘要

Current computer-use benchmarks primarily focus on software operation tasks in virtualized systems, whereas scientific instrumentation scenarios require coordinated control over complex interfaces, and feedback-driven parameter adjustment. However, directly evaluating agents on physical high-precision instruments is impractical due to high cost, safety risks, limited accessibility, and difficulty in ensuring reproducible evaluation. This motivates the need for a simulated yet realistic testbed that preserves the operational challenges of scientific instruments while enabling scalable and safe benchmarking. To this end, we introduce LabOSBench, a challenging benchmark for multimodal GUI agents built on a suite of web-based scientific-instrument simulators. Operating directly via a browser, LabOSBench avoids resource-heavy OS virtualization while supporting flexible task configuration and execution-based evaluation. Specifically, LabOSBench constructs 96 subtasks across eight instrument simulators, covering workflows from sample loading, alignment, parameter tuning, and data acquisition to result inspection. We evaluate general-purpose vision-language models, specialized GUI agent models, and advanced agentic frameworks at both subtask and end-to-end levels. Our experiments reveal that while existing agents can complete many structured GUI subtasks, they still struggle with feedback-driven operations and long-horizon workflow execution. Overall, LabOSBench provides a reproducible, low-cost testbed for advancing computer-using agents toward scientific-instrument control.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的问题是：缺乏一个可扩展、低成本且安全的基准测试平台，用于评估多模态AI智能体在科学仪器图形用户界面（GUI）控制上的表现。现有基准测试如OSWorld依赖昂贵的操作系统虚拟化（如VMware、Docker），难以部署和扩展；而WebArena、Mind2Web等Web基准测试则专注于通用网页导航，无法模拟科学仪器界面中复杂的布局、长周期操作流程（如从样品加载、参数调整到数据采集）和基于反馈的连续参数调优。此外，许多基准测试依赖静态演示或离线评估，无法有效测试智能体的交互学习、探索和替代操作能力。直接使用物理仪器进行评估则面临成本高、安全风险大、可及性有限以及难以保证评估可重复性等挑战。因此，本文的核心目标是构建LabOSBench——一个基于Web的、轻量级、可执行的科学仪器模拟器基准测试，它通过浏览器直接运行，无需操作系统虚拟化，能够保留科学仪器GUI的操作挑战，并提供灵活的任务配置和基于执行结果的评估，从而为评估和推动多模态GUI智能体在专业科学领域的应用提供一个可重复、低成本的测试平台。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是**计算机使用智能体**，从基于DOM的网页智能体发展到基于视觉的屏幕操作智能体，屏幕解析方法提升了它们在复杂视觉场景中识别可操作元素的能力。本文指出当前智能体在处理长程规划、精确定位和状态依赖交互时仍存在困难。第二类是**科学智能体**，研究了推理、实验规划、化学工具使用、机器学习实验和自主发现等任务。MyScope提供了基于浏览器的显微镜模拟器用于人类教育。本文与之的关键区别在于LabOSBench为计算机使用智能体添加了可执行评估，包含自然语言任务描述、子任务成功检查器、日志记录、浏览器执行和仪器专用指标。第三类是**计算机使用基准**，涵盖网页、桌面、移动端和科学工作流环境。网页基准轻量但侧重通用导航，操作系统级基准真实感好但虚拟化成本高。ScienceBoard在真实科学工作流中评估多模态自主智能体。然而现有基准对科学仪器GUI操作的覆盖有限，要求智能体操控密集的控制面板、跟踪仪器状态、进行连续参数调整并响应状态依赖的反饋。相比之下，LabOSBench聚焦于当设备API不可用时，在可执行的浏览器科学仪器模拟器上评估基于GUI的仪器控制能力。

### Q3: 论文如何解决这个问题？

LabOSBench通过构建一套轻量级、基于浏览器的科学仪器模拟器来解决问题。核心思想是绕过资源密集的操作系统虚拟化，直接在网页端复现科学仪器的操作复杂度，从而实现安全、可复现且低成本的评估。

**核心方法与架构设计**：整体框架包含一个浏览器驱动的协调器。每个评估任务由命令行参数和自然语言指令初始化。协调器使用Playwright控制浏览器打开模拟器网页，接收并执行智能体（Agent）的GUI动作（如点击、拖拽、输入），并捕获屏幕截图。模拟器页面内置了基准测试脚本（如benchmark_sem.js），用于记录子任务完成情况、步骤轨迹和元数据。最后，一个Python协调器从浏览器中导出这些数据，并根据仪器特定的JSON Schema聚合指标。

**主要模块/组件**：
1.  **八大科学仪器模拟器**：覆盖显微成像（SEM, TEM, LFM）、衍射光谱分析（XRD, EDS, APT）和微纳加工（FIB, SPM）。每个模拟器都是高保真Web界面，包含多维度滑块、实时动态图表等特定控制。

2.  **96个子任务分解**：将每个仪器的完整工作流分解为一系列有意义的子任务，如样品准备、环境调节、参数配置、数据采集等。这实现了可解释的评估，能定位智能体在长流程中的具体失败阶段。

3.  **两种评估模式**：
    *   **全任务模式**：智能体从初始状态开始，在步数限制内完成整个工作流程，衡量长程任务完成能力和复合错误恢复能力。
    *   **子任务模式**：模拟器通过编程接口（如XRD_fast_forward_to_subtask）直接快进到目标子任务前的状态，隔离评估智能体在单一操作（如定位滚轮、下拉选单）上的GUI接地能力。这能区分局部失误和长程推理失败。

**创新点**：
*   **低成本高保真模拟**：通过Web模拟替代实体仪器或虚拟机，解决了成本、安全性和可复现性的核心难题。
*   **结构化诊断评估**：通过子任务分解和两种评估模式，提供了超越简单二元成功率（成功/失败）的诊断能力，能精准定位智能体在特定操作步骤（如参数调节、状态识别）上的不足。
*   **图像质量量化**：对于生成图像的仪器（如SEM），引入PSNR等像素级质量指标，评估参数调整是否达到科学可用状态，而不仅仅是触发了正确动作。

### Q4: 论文做了哪些实验？

论文在LabOSBench基准测试上进行了实验，包含八种科学仪器模拟器（SEM、SPM、TEM、XRD、LFM、FIB、APT、EDS），共96个子任务。实验设置中，每个模型在每个子任务上有最多50次交互步骤，每个模型-子任务对运行两次，报告子任务归一化成功率。对比方法分为三类：通用多模态模型（Qwen3VL-32B、EvoCUA-8B、Claude Sonnet-4.5、Kimi-K2.5、Seed-1.6、GPT-5.5、Claude Opus-4.5）、专用GUI模型（UI-TARS-1.5-7B、GUI-Owl-7B）和智能体框架（GTA1 w/ GPT-5.5、VLAA-GUI w/ Opus-4.5、Hippo Agent w/ Opus-4.5）。主要结果：GTA1 w/ GPT-5.5平均分最高（0.814），但所有非人类模型平均分（0.924）远低于人类。在子任务层面，Seed-1.6（0.763）和GPT-5.5（0.726）表现较好，但在端到端评估中，GPT-5.5平均成功率仅26.3%（仅在EDS、APT、XRD上非零成功）。分析表明，FIB和LFM最困难，涉及长程依赖和反馈驱动操作；通用模型优于专用GUI模型，但所有模型在反馈驱动和长程任务上仍困难。

### Q5: 有什么可以进一步探索的点？

首先，论文明确指出基于网页模拟器而非物理仪器，无法捕捉硬件延迟、校准不确定性、安全约束和真实故障模式，这限制了评估结果的现实代表性。未来可以构建混合仿真环境，融合物理仪器的实时反馈数据与模拟界面，或引入硬件-in-the-loop机制提升逼真度。

其次，当前覆盖的仪器和流程有限，未包含湿实验室操作、机器人操控、化学合成或多仪器实验规划等更广泛的科研场景。未来可扩展至跨领域仪器协同任务，并引入领域知识图谱辅助智能体决策。

第三，评估依赖截图和状态日志，未能充分利用多模态传感器信号（如光谱、图像序列）。建议集成视觉-语言-数值多模态输入，使智能体能基于信号特征自主调整参数，并探索强化学习中的奖励塑形方法以处理长周期反馈。

此外，安全监督机制尚未集成，未来应加入权限控制、操作日志与人工介入接口，确保向物理仪器部署时的安全性。可研究可解释性模型以预测风险操作。

### Q6: 总结一下论文的主要内容

LabOSBench 提出了一个针对科学仪器控制的计算机使用代理基准测试。现有基准主要关注虚拟化系统中的软件操作任务，而科学仪器场景需要复杂界面协调控制和基于反馈的参数调整，直接在物理仪器上评估成本高、有安全风险、可重复性差。为此，该工作构建了基于网页科学仪器模拟器的轻量级可执行基准LabOSBench，通过浏览器直接操作，避免了资源密集型的操作系统虚拟化。基准包含8个仪器模拟器、96个子任务，覆盖从样品加载、对准、参数调优到数据采集和结果检查的工作流程。实验评估了通用视觉语言模型、专用GUI代理模型和高级代理框架。主要结论显示，现有代理能完成许多结构化GUI子任务，但在基于反馈的操作和长周期工作流执行中仍存在困难，特别是在科学状态解释、精确空间定位、闭环调整和误差累积方面表现不足。LabOSBench为连接计算机使用代理评估与自主实验室系统提供了可复现、低成本的测试平台。
