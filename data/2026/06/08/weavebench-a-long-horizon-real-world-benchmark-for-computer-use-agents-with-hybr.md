---
title: "WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces"
authors:
  - "Wanli Li"
  - "Bowen Zhou"
  - "Yunyao Yu"
  - "Zhou Xu"
  - "Yifan Yang"
  - "Dongsheng Li"
  - "Caihua Shan"
date: "2026-06-08"
arxiv_id: "2606.09426"
arxiv_url: "https://arxiv.org/abs/2606.09426"
pdf_url: "https://arxiv.org/pdf/2606.09426v1"
categories:
  - "cs.AI"
tags:
  - "Computer-Use Agent"
  - "Benchmark"
  - "Hybrid Interface"
  - "GUI Agent"
  - "CLI Agent"
  - "Long-Horizon Task"
  - "Evaluation"
  - "Trajectory-Aware Judge"
  - "Code Agent"
relevance_score: 9.5
---

# WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces

## 原始摘要

Computer-use agents (CUAs) increasingly operate in runtimes that combine visual desktop control, command-line execution, code editing, browsers, and external tools. Existing benchmarks, however, often evaluate these interfaces as separable capabilities, leaving long-horizon cross-interface orchestration under-tested. Thus, we introduce WeaveBench, a long-horizon hybrid-interface benchmark with 114 tasks across 8 real-world work domains, grounded in real user requests and publicly verifiable artifacts. Each task requires agents to combine GUI observations/actions with CLI/code operations within a single trajectory. We evaluate these tasks on a real Ubuntu desktop inside deployed CLI-agent runtimes, augmented with a minimal desktop-control plugin. We also propose a companion trajectory-aware judge that inspects deliverables, files, screenshots, logs, and action traces, while detecting shortcut behaviors such as fabricated visual evidence or hard-coded metrics. Across frontier model-runtime pairings, the best PassRate reaches only 41.2%, showing the benchmark remains far from saturated. The trajectory-aware judge further reveals that outcome-only grading substantially overestimates agent performance. Overall, WeaveBench exposes a critical gap in CUA evaluation and provides an effective testbed to measure whether agents can orchestrate GUI, CLI, and code operations across long-horizon real-world tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有计算机使用代理（CUA）基准测试在评估混合接口长期协同能力方面的严重缺陷。研究背景是，实际部署中的CUA需要在一个工作流中协同操作视觉桌面（GUI）、命令行/代码（CLI/code）、浏览器和外部工具，但现有基准测试存在明显不足：GUI/OS类基准仅测试单一GUI通道，甚至存在CLI代理表现更优的“捷径”；多接口基准虽然同时暴露GUI和CLI，但多数任务仍可通过单一通道解决，混合接口仅作为便利而非必需；而真实世界任务基准又往往局限于CLI环境，缺乏GUI交互。因此，核心问题在于缺乏一个能够强制要求代理在单一轨迹中交替使用GUI和CLI/code操作、且任务无法通过单一通道简化的长期跨接口协同评测基准。为此，论文提出WeaveBench，包含114个来自真实用户请求、需混合使用GUI与CLI/code的长期任务，并设计了能检测虚假视觉证据等捷径行为的轨迹感知评判器，以精准评估代理的跨接口编排能力。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是计算机使用代理（CUA）的基准测试，分为GUI端和CLI/编码端。GUI基准测试（如评估静态元素定位或真实OS、移动端、网页环境下的端到端执行）和CLI/编码基准测试（如基于终端的软件工程任务）各自针对单一模态优化，无法测试代理跨通道的信息移动能力。本文指出这种隔离甚至使单通道GUI基准测试产生误导，例如在OSWorld上，不依赖视觉的CLI代理能达到甚至超越视觉代理的性能。第二类是混合接口基准测试，包括MCPWorld、OSWorld-MCP和PwP-Bench，它们将API或MCP操作叠加到GUI任务上，但任务仍存在等效的单通道解决方案，科学协作类的ScienceBoard虽需GUI/CLI协作，但仅限于任务层面的分工且局限于科学发现场景。第三类是部署型CLI代理的基准测试，如WildClawBench、ClawBench和CocoaBench，它们基于真实用户请求和部署运行时（如Claude Code、OpenClaw），但均未评估GUI通道。本文WeaveBench与这些工作的核心区别在于：它基于Claw类范式，将GUI提升为与CLI对等的通道，确保任务中通道不可替代，并结合部署型运行时和轨迹感知裁判进行评测。

### Q3: 论文如何解决这个问题？

WeaveBench通过构建一个长程混合界面基准测试来评估计算机使用代理在真实世界任务中的表现。其核心方法是构建包含114个任务的测试套件，这些任务覆盖8个真实工作领域，每个任务都要求智能体在单个轨迹中协调GUI观察/操作与CLI/代码操作。任务准入需满足三个关键属性：通道不可替代性（必须同时使用GUI和CLI）、长程执行（包含多次交错切换）和跨应用状态（涉及多个独立程序）。

整体框架包括三个主要部分：任务构建流程、执行环境和评估协议。任务构建采用四阶段流水线：原型引导来源、资产打包、盲审和试点验证。执行环境基于容器化Ubuntu虚拟机，在现有CLI代理上添加最小化桌面控制插件，包含一个截图工具和九个基于pyautogui的执行原语（点击、双击等）。

关键技术方面，论文提出了轨迹感知评估机制。该机制采用基于代理的评判器，通过分层流水线进行评分：先将每个交付物分解为原子条款，然后验证每个条款的满足程度，同时从人工制品、截图、日志和参考锚点中主动获取证据。该评判器还并行检测九种确认的捷径模式（如伪造截图、硬编码指标等），一旦触发直接判零分。最终得分采用交付物正确性和多个处理维度的最小值，防止辅助维度掩盖交付缺陷。

### Q4: 论文做了哪些实验？

论文在WeaveBench基准上进行了多组实验。实验设置：所有任务在容器化Linux VM中运行，使用固定快照、限制网络访问，并施加工具输出和时钟预算。数据集/基准：包含8个真实工作域（桌面、文档、游戏、Web开发、数据分析与可视化、DevOps、空间/3D、设计）的114个长时域混合界面任务。对比方法：首先在固定OpenClaw框架下对比多种模型API（GPT-5.1-codex至GPT-5.5、Claude Opus 4.7、Gemini 3.1 Pro、Qwen系列等）；然后固定最强API（GPT-5.5和Claude Opus 4.7），在Codex CLI、Claude Code、Hermes和OpenClaw四个运行时框架中测试。主要结果：最佳PassRate仅41.2%（Claude Opus 4.7 + Claude Code）；在OpenClaw框架上，Claude Opus 4.7最高（35.1%），GPT-5.5次之（33.3%）。界面消融实验显示，纯GUI模式PassRate≤1.8%，纯CLI模式≤3.5%，而混合模式达33.3-35.1%，跨界面增益高达+31.6pp（对比其他基准仅+3.2至+4.5pp）。轨迹感知评判显示，仅依赖最终结果会高估10.3-20.2个PassRate点。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来可从以下方向深入探索：**1) 模型架构改进**：当前CUA在跨界面长程任务中表现不佳（最优PassRate仅41.2%），可引入分层决策机制或记忆增强模块，分离高层任务规划与底层跨界面控制。**2) 界面交互耦合**：论文拆分为GUI+CLI/代码操作，但真实场景中界面间存在强依赖（如GUI点击触发CLI输出），未来可探索融合状态表示（如联合视觉-命令流特征）或注意力门控机制。**3) 评价体系优化**：轨迹感知判别器虽能检测虚假证据，但难以量化任务完成质量。建议引入细粒度子目标完成度评分、环境状态图推理等机制。**4) 环境扩展**：限制在Ubuntu桌面，需扩展至Windows/macOS及移动端混合界面，测试跨平台泛化能力。**5) 鲁棒性挑战**：可构建对抗性界面干扰（如窗口遮挡、CLI输出错位），测试代理的容错与自适应能力。

### Q6: 总结一下论文的主要内容

WeaveBench提出了一个评估计算机使用代理在混合界面（GUI、CLI/代码、浏览器和外部工具）中长程协调能力的新基准。现有基准常将不同界面能力分开评估，忽略了跨界面协同的必要性。为此，WeaveBench包含114个来自真实用户请求的任务，覆盖8个实际工作领域，每个任务都要求代理在单个轨迹中结合GUI操作与CLI/代码操作。方法上，研究者在现有CLI代理运行时上增加了一个最小化的桌面控制插件，并引入了一个轨迹感知评判器，通过多轮检查交付物、文件、截图、日志和操作痕迹来避免伪造证据和硬编码等作弊行为。实验表明，最强模型和运行时的通过率仅为41.2%，远低于其他基准上的表现，说明当前代理在长程跨界面协调上仍有显著缺陷。轨迹感知评判器还揭示了仅基于结果评分会严重高估代理性能。WeaveBench的核心贡献在于暴露了现有CUA评估中的关键空白，并提供了一个有效的测试平台来衡量代理在真实世界长程任务中协调GUI、CLI和代码操作的能力。
