---
title: "MacArena: Benchmarking Computer Use Agents on an Online macOS Environment"
authors:
  - "Victor Muryn"
  - "Maksym Shamrai"
  - "Sofiia Mazepa"
  - "Yehor Khodysko"
date: "2026-06-04"
arxiv_id: "2606.06560"
arxiv_url: "https://arxiv.org/abs/2606.06560"
pdf_url: "https://arxiv.org/pdf/2606.06560v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.HC"
tags:
  - "GUI Agent"
  - "Benchmark"
  - "Computer-Use Agent"
  - "Multi-Platform Evaluation"
  - "macOS"
relevance_score: 9.5
---

# MacArena: Benchmarking Computer Use Agents on an Online macOS Environment

## 原始摘要

Computer-use agents (CUAs) operate graphical user interfaces (GUIs) through vision and control primitives, and their capabilities have advanced rapidly, driven in part by standardized online evaluation benchmarks such as OSWorld, which serve both as evaluation tools and as training environments for reinforcement learning. However, macOS remains underserved in this landscape: the only existing benchmark, macOSWorld, covers a narrow slice of first-party applications with simpler tasks, and runs on x86 virtual machines incompatible with Apple Silicon. We introduce MacArena, a benchmark of 421 manually verified tasks spanning 50 applications that combines a curated port of OSWorld tasks, content sourced from macOSWorld, and 49 new macOS-native tasks, all running on Apple's native Virtualization framework on Apple Silicon. We argue that macOS presents distinct GUI challenges beyond what Linux-based benchmarks capture, and our evaluation supports this claim: strong model performance on existing benchmarks can reflect familiarity with task distributions rather than genuine cross-platform GUI competence. Notably, model rankings invert between ported and macOS-native tasks, with a leading model trailing by over 26% on the MacArena subset, suggesting that macOS poses a genuinely harder environment for current GUI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有计算机使用代理（CUA）基准测试中macOS平台评估不足的问题。研究背景是，CUA通过视觉和操作基元与图形用户界面交互，其能力在标准化在线评估基准（如OSWorld）推动下快速进步，这些基准同时作为评估工具和强化学习训练环境。然而，现有方法存在显著不足：唯一的macOS基准测试macOSWorld仅覆盖少量第一方应用和简单任务，且基于x86虚拟机，与苹果自研芯片（Apple Silicon）不兼容，无法反映当前硬件性能。核心问题是，macOS是否对GUI代理提出了超越Linux基准测试的独特挑战？为填补这一空白，论文引入MacArena，这是一个包含421个手动验证任务的基准测试，跨越50个应用，整合了OSWorld任务的移植版、macOSWorld任务以及49个新增的macOS原生任务。评估发现，模型排名在移植任务和macOS原生任务之间发生反转，领先模型在MacArena子集上表现落后超过26%，表明macOS对当前GUI代理是真正更难的测试环境，从而凸显了现有基准测试在跨平台能力评估上的局限性。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是离线评测基准，如Mind2Web、AITW、ScreenSpot系列和GUIrilla，它们基于静态截图评估GUI定位或导航能力，无法捕捉真实环境中的顺序决策和错误恢复。本文的MacArena是交互式在线基准，克服了这一局限。第二类是其他平台的在线基准：OSWorld是Linux/Windows上最全面的桌面基准，但未覆盖macOS；AndroidWorld、B-MoCA针对移动端；WebArena、VisualWebArena关注网页。本文针对macOS填补空白，并与OSWorld任务保持兼容以进行跨平台比较。第三类是直接相关的macOS基准macOSWorld，但前者仅覆盖30个第一方应用、任务较简单，且基于已淘汰的x86架构；MacArena支持50个应用（含大量第三方）、任务更复杂，并原生运行于Apple Silicon。此外，早期GUI代理依赖提示式pipeline（如UFO、SeeAct），后续发展为专用视觉定位模型（如CogAgent）和端到端训练模型（如UI-TARS、Aguvis），以及强化学习方法（如ComputerRL）。MacArena为这些方法提供了新的macOS训练和评估环境。

### Q3: 论文如何解决这个问题？

MacArena通过构建一个基于Apple Silicon原生虚拟化框架的在线macOS评测环境来解决现有CUA基准测试覆盖不足的问题。核心方法是将智能体交互形式化为部分可观测马尔可夫决策过程（POMDP），状态空间包含macOS完整系统状态，观测空间提供屏幕截图和可访问性树两种模态，动作空间包含鼠标、键盘和终端三大类共16种原子操作。

整体框架由三个核心组件构成：环境、任务集和评测框架。环境层面采用UTM管理虚拟机，维护两个独立VM镜像：一个用于适配OSWorld和macOSWorld的遗留任务，另一个通过自动化构建脚本为原生macOS任务定制。采用写时复制策略确保每个任务episode的初始状态完全一致。任务集包含421个经过人工验证的任务，覆盖50个应用，来源包括移植的OSWorld任务（221个）、macOSWorld任务（151个）和49个原生新增任务。每个任务包含自然语言指令、初始化配置和确定性评估函数三要素，支持OSWorld的结构化配置文件和macOSWorld的shell脚本两种格式。评测框架采用执行驱动的方式，在智能体发出DONE信号后自动运行定制评估脚本，返回[0,1]区间的连续分数。

关键技术在于跨平台评测对比设计：通过在同一环境下运行不同来源的任务，发现模型在习得任务分布特征而非真正跨平台GUI能力。创新点包括：首次在Apple Silicon上实现完整macOS智能体评测、引入可访问性树作为辅助观测、建立自动化VM配置流程保障可复现性，以及通过任务来源分类揭示模型能力与任务分布的相关性。

### Q4: 论文做了哪些实验？

论文设计了MacArena基准测试，包含421个手动验证任务，覆盖50个应用，由OSWorld子集、macOSWorld子集和49个新的MacArena原生子集组成。实验在Apple Silicon的macOS虚拟机上运行，使用原始鼠标和键盘操作，每步输入截图，限制15步，模型运行2次。评估了四个基线代理：UI-TARS-1.5 7B、Qwen3-VL 2B、Qwen3-VL 4B和OpenAI CUA。主要指标为成功率（SR）。整体上，OpenAI CUA最高（31.83%），其次是Qwen3-VL 4B（24.23%）、UI-TARS-1.5 7B（21.14%）和Qwen3-VL 2B（11.40%）。在OSWorld子集上，UI-TARS-1.5 7B以21.27%领先OpenAI CUA的16.74%；但在MacArena子集上排名反转，OpenAI CUA以36.73%远超UI-TARS-1.5 7B的10.20%，差距达26.5个百分点。与Ubuntu上的原始OSWorld基准对比，所有模型在macOS上性能显著下降（如OpenAI CUA从26.0%降至16.74%）。多应用任务是最难的类别，大多数模型得分接近0%。MacArena子集任务平均消耗步数最多（13.96），macOSWorld子集最少（10.92）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，所有任务均依赖人工标注，这限制了可扩展性。未来可探索自动化任务生成，例如利用LLM结合应用模式或交互日志合成任务指令，但需配套自动可行性验证机制（如限定步数内由参考智能体完成），并配合人工抽检以确保质量；其次，缺乏人类表现基准，这影响了对模型性能天花板的理解，建议参考OSWorld引入人类基线以量化改进空间；最后，任务覆盖虽达50个应用但仍有偏斜，可尝试基于苹果原生虚拟化框架动态生成更复杂跨应用工作流（如邮件+日历+备忘录联动）。值得关注的改进方向是：当前MAC环境相对Linux更强调多窗口调度与苹果原生UI控件（如触控栏、手势），但现有任务对此挖掘不足。可设计需要组合多个系统级操作的测试（如通过Spotlight调用计算器再拖拽结果）。此外，排名倒置现象提示需构建对抗性测试集，例如对端口任务注入macOS独有的鼠标悬停/右键菜单干扰项，以消除模型对特定平台模式的"虚假"熟悉度。

### Q6: 总结一下论文的主要内容

MacArena提出了macOS平台首个全面的GUI智能体基准测试，包含421个手动验证任务，覆盖50个应用程序。这些任务整合了OSWorld的移植任务、macOSWorld来源任务以及49个全新的macOS原生任务，所有任务均在Apple Silicon上的原生虚拟化框架中运行。核心贡献在于揭示了macOS相对于Linux等现有基准测试存在独特的GUI挑战：模型在现有基准上的强表现可能反映的是对任务分布的熟悉度，而非真实的跨平台GUI能力。评估发现，模型排名在移植任务和macOS原生任务之间出现反转，领先模型在MacArena子集上落后超过26%。结论表明，macOS对当前GUI智能体构成更困难的环境，该基准测试旨在建立跨操作系统可靠泛化的GUI智能体基础。
