---
title: "MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research"
authors:
  - "Dingbang Wu"
  - "Rui Hao"
  - "Haiyang Wang"
  - "Shuzhe Wu"
  - "Han Xiao"
  - "Zhenghong Li"
  - "Bojiang Zhou"
  - "Zheng Ju"
  - "Zichen Liu"
  - "Lue Fan"
  - "Zhaoxiang Zhang"
date: "2026-05-25"
arxiv_id: "2605.26114"
arxiv_url: "https://arxiv.org/abs/2605.26114"
pdf_url: "https://arxiv.org/pdf/2605.26114v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Mobile GUI Agent"
  - "Simulation Platform"
  - "Online RL"
  - "Multi-Agent"
  - "Agent Training"
  - "Benchmark"
  - "State-based Judging"
  - "Scalability"
relevance_score: 9.5
---

# MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

## 原始摘要

We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends. It enables two capabilities previously out of reach for everyday apps: verifiable outcome signals through deterministic state-based judging over structured JSON state, and scalable online RL through low-cost parallel rollouts. The full environment state is captured, configured, forked, and compared as structured JSON, and a single server can host hundreds of parallel instances, with about 400 MB memory per instance and about 3 s cold start. A layered state model and a declarative task-definition framework keep state programmability and task creation practical at scale, and a single programmatic judging mechanism delivers both deterministic evaluation verdicts and dense RL rewards. The accompanying MobileGym-Bench provides 416 parameterized task templates, including 256 test and 160 train templates, over 28 apps, with deterministic judges and a structured AnswerSheet protocol that avoids free-text matching failures. In a Sim-to-Real case study, GRPO on Qwen3-VL-4B-Instruct gains +12.8 percentage points on the 256-task test set, and on a 59-task real-device signal subset, real-device execution retains 95.1% of the simulation-side training gain. Project page: https://mobilegym.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动GUI智能体研究中，日常应用环境的可重复实验与大规模在线训练难以兼得的根本矛盾。现有方法分为两类：基于模拟器的环境（如AndroidWorld）虽可重复，但主要覆盖系统工具和简单开源应用，且因每个实例需要数GB内存而难以并行扩展；基于真实设备的环境（如MobileBench-OL）虽能访问日常应用，但受限于实时账户、后端状态不可控、操作不可逆及设备维护成本，导致实验难以控制、复现和并行化。其核心问题在于，日常应用的状态普遍“不可读、不可写、不可分叉、不可逆”，内部状态无法通过ADB或无障碍树直接获取，基于VLM的评估存在固有不可靠性，状态难以重置或配置，大规模并行训练需要廉价复制和状态分叉，且许多操作会造成永久后果。因此，本文提出了MobileGym，一个基于浏览器的轻量级类Android模拟平台，通过将应用数据、系统状态和设备上下文表示为结构化JSON，实现了确定性的状态评估、可配置和重置的状态、支持快照分叉的并行回滚以及沙盒化安全操作。该平台仅需约400MB内存和3秒冷启动时间，可在一台服务器上运行数百个并行实例，结合结构化AnswerSheet协议避免自由文本匹配失败，从而为日常应用场景提供了可验证的信号和可扩展的在线强化学习能力。

### Q2: 有哪些相关研究？

相关研究主要围绕移动GUI智能体的评测平台和方法展开。**基于真实设备与模拟器的方法**包括：AndroidWorld通过adb对116个模板任务进行确定性判断；AndroidLab结合UI树和LLM验证器处理问答子任务；MobileWorld直接查询后端数据库；A3使用Appium操控20款主流Google Play应用并从MLLM-as-judge处理动态内容；MobileBench-OL在80款中文真实应用上运行1080个任务，但其XPath规则易受弹窗或更新影响且不支持并行。这些方法均未实现全环境状态对比、快照恢复和完整状态定制。**其他移动端评测基准**如SPA-Bench、Mobile-Bench等提供了独立于基础设施的任务集合，本文参考了其分类设计。**合成与轨迹回放环境**方面，GUI-Genesis通过交互轨迹重建轻量网页环境但受限于单一轨迹；UISim等采用图像生成方法但长期视觉预测误差累积。**跨领域可验证环境**包括WebArena、OSWorld等网页、桌面和API模拟平台。**RL训练工作**如DigiRL、UI-TARS-2及UI-R1等展示了在线RL在设备控制中的优势。本文提出的MobileGym通过浏览器端结构化JSON状态实现确定性验证与低成本并行部署，支持完整状态快照、参数化任务及Sim-to-Real迁移验证，与现有工作形成互补。

### Q3: 论文如何解决这个问题？

MobileGym 通过一个浏览器托管、轻量级且完全可控的模拟环境解决移动GUI智能体研究中的保真度、可验证性和可扩展性问题。其核心创新在于将整个环境状态建模为结构化JSON，实现确定性状态判断，从而提供可验证的结果信号，并支持低成本并行rollout的在线强化学习。

整体框架包含一个分层的状态模型和声明式任务定义框架。分层状态模型将GUI状态抽象为结构化JSON，涵盖从抽象任务目标到具体UI元素属性的多个层次，使得状态可编程、可配置、可分支和可比较。声明式任务定义框架允许研究者以JSON格式快速定义任务，包括初始状态、目标条件和评判规则，实现了大规模任务创建的可操作性。

关键技术包括一个单一的编程化评判机制，该机制基于确定性的状态比较，既提供精确的评估判定，又生成密集的强化学习奖励信号，避免了传统自由文本匹配的失败问题。系统架构支持单台服务器容纳数百个并行环境实例，每个实例仅需约400MB内存和约3秒冷启动时间，极大地降低了计算资源门槛。训练过程中，MobileGym通过增强的并行rollout能力，利用结构化状态直接驱动在线RL算法，如GRPO。最终在Sim-to-Real案例研究中，基于Qwen3-VL-4B-Instruct的GRPO训练在256任务测试集上获得+12.8个百分点的提升，且在真实设备上保留了95.1%的仿真训练增益，验证了其高效性和实际应用价值。

### Q4: 论文做了哪些实验？

论文在MobileGym-Bench的256个测试任务上评估了9个智能体，包括3个闭源模型（Gemini 3.1 Pro、Doubao-Seed-2.0-Pro、Qwen3.6-Plus）和6个开源模型。实验设置分为四个难度层级（L1-L4），使用成功率（SR）、进展率（PR）和诊断指标（虚假完成FC、超时终止OT、意外副作用USE）进行评估。主要结果显示：闭源模型中Gemini 3.1 Pro表现最佳，整体SR为58.8%；开源GUI专用模型（如AutoGLM-Phone-9B）SR为12.9%-20.0%；通用模型Qwen3-VL-4B-Instruct仅9.4%。在Sim-to-Real迁移实验中，使用GRPO对Qwen3-VL-4B-Instruct在160个训练任务上进行10步微调，超参数为lr=1e⁻⁶、组大小k=8、批大小bs=12、KL=0.01。训练后模型在模拟测试集上SR从9.4%提升至22.2%（+12.8个百分点），在59个真实设备信号子集上保留95.1%的训练增益，真实设备通过率从32.2%提升至72.9%。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在视觉外观、后端动态建模和功能覆盖三个方面。视觉上，模拟环境与真实应用存在布局细节、动画和图标差异，对依赖精确图标识别的任务迁移仍有影响，未来可引入更精细的渲染模型或利用扩散模型合成逼真界面。后端动态内容（如广告、推荐流）被简化为可控制JSON状态，无法捕捉服务器端随机行为或实时变化，未来可设计可配置的随机扰动注入模块，增强环境对真实干扰的鲁棒性。模拟应用仅覆盖核心场景，功能完整度不足，后续可构建分层功能树，逐步扩展边缘案例，或结合LLM自动生成任务模板以降低人工成本。此外，当前评测主要聚焦单步操作，多智能体协作或长期时序依赖任务尚未涉及，可探索将MobileGym扩展为分布式对抗训练平台。

### Q6: 总结一下论文的主要内容

MobileGym提出了一个轻量级、可验证且高度可并行的移动GUI仿真平台，解决了日常应用场景中仿真环境与真实设备之间的关键权衡挑战。该平台通过将应用状态表示为结构化JSON，实现了确定性验证、状态可写、可沙盒化以及支持低成本并行回滚，每个浏览器实例仅需约400MB内存和3秒冷启动。基于此平台构建的MobileGym-Bench包含416个参数化任务模板，覆盖28个日常应用，采用结构化AnswerSheet协议避免自由文本匹配失败。实验表明，在Qwen3-VL-4B-Instruct上使用GRPO训练获得+12.8个百分点的测试集提升，且59个真实设备任务的训练收益保留率达95.1%。该工作首次使日常移动应用的可重复研究和规模化在线RL训练成为可能，无需真实账号、设备农场或专有后端。
