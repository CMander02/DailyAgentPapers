---
title: "ClawGym: A Scalable Framework for Building Effective Claw Agents"
authors:
  - "Fei Bai"
  - "Huatong Song"
  - "Shuang Sun"
  - "Daixuan Cheng"
  - "Yike Yang"
  - "Chuan Hao"
  - "Renyuan Li"
  - "Feng Chang"
  - "Yuan Wei"
  - "Ran Tao"
  - "Bryan Dai"
  - "Jian Yang"
  - "Wayne Xin Zhao"
date: "2026-04-29"
arxiv_id: "2604.26904"
arxiv_url: "https://arxiv.org/abs/2604.26904"
pdf_url: "https://arxiv.org/pdf/2604.26904v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent训练"
  - "数据合成"
  - "基准评估"
  - "Claw-style Agent"
  - "沙箱环境"
  - "监督微调"
  - "强化学习"
relevance_score: 8.5
---

# ClawGym: A Scalable Framework for Building Effective Claw Agents

## 原始摘要

Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task sandboxes.To support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at https://github.com/ClawGym.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决Claw风格环境中自主智能体（Claw agents）开发缺乏系统性框架的问题。Claw风格环境支持基于本地文件、工具和持久工作区状态的多步骤工作流，但现有研究主要面临以下不足：一是缺乏大规模的、可验证的Claw风格训练数据，因为这类任务具有长跨度、依赖个性化用户场景和真实工作区状态的特点，难以像静态文本推理或结构化智能体基准那样轻松合成；二是现有评估基准和训练方法多聚焦于特定场景，缺乏一个覆盖从数据合成、模型训练到性能评估全生命周期的统一框架。为此，本文提出了ClawGym框架，其核心目标是：通过双路线数据合成策略（自上而下的用户角色驱动和自下而上的技能组合驱动），自动生成大规模、多样且可验证的Claw风格任务数据；利用这些数据训练ClawGym-Agents模型族（包括监督微调和强化学习）；并构建一个包含200个实例的可靠评估基准ClawGym-Bench，从而系统性地推动Claw风格个人智能体的构建与评测研究。

### Q2: 有哪些相关研究？

相关工作分为以下几类：

1. **代理框架类**：以OpenClaw为代表，这类系统将AI部署在用户数字环境中，支持工具调用、本地文件管理和Web服务交互。本文直接基于OpenClaw构建，但指出其缺乏系统化的训练数据合成与评测框架，因此提出ClawGym进行补充。

2. **训练方法类**：已有研究通过专门训练算法或在线学习框架从用户交互中提取监督信号来提升个人代理能力。本文与这些工作的区别在于，ClawGym不依赖在线用户数据，而是通过双路数据合成策略（个性驱动与技能驱动）生成大规模可验证的Claw-style任务，并在此基础上进行SFT和RL训练。

3. **评测基准类**：现有基准如SWE-Bench-Verified和BrowseComp主要面向结构化代理循环环境，而PinchBench虽涉及Claw-style任务但规模有限。本文构建的ClawGym-Bench包含200个经过难度校准和人工审核的实例，覆盖6个类别，专门针对Claw-style环境的非结构化、长周期和状态依赖特性设计评测。

本文的核心贡献在于将三类工作统一到一个系统框架中，通过自动化数据合成弥补了大规模Claw-style训练数据缺失的空白，并实现了从数据到训练到评测的完整闭环。

### Q3: 论文如何解决这个问题？

ClawGym通过构建一个可扩展的框架来系统性地解决Claw风格智能体开发中缺乏有效训练数据、评估基准和集成流程的问题。核心方法包含三个主要组件：ClawGym-SynData、ClawGym-Agents和ClawGym-Bench，形成从数据生成、模型训练到评估的完整生命周期。

整体框架以环境接地指令执行为基础，任务实例由用户指令、初始工作空间、动作空间和任务验证器组成。智能体产生由动作和观察序列构成的轨迹，最终工作空间状态是主要输出，通过混合验证方案评估任务完成度。

技术上，ClawGym-SynData采用双流水线合成策略：自上而下的基于角色驱动合成，通过组合用户画像、情景类别和原子操作集生成多样化任务种子，再由LLM扩展为具体任务；自下而上的基于技能组合合成，从OpenClaw技能库中筛选并标注技能，再组合成多步工作流。资源准备阶段为每个任务生成轻量级模拟文件，验证设计阶段结合代码检查和基于规则检查进行混合验证，最后通过自动质量评估过滤低质量样本。

创新点包括：1) 双流水线任务合成机制，兼顾场景多样性和操作可行性；2) 混合验证方案，代码检查确保客观正确性，规则检查评估质量维度；3) 生成的13.5K训练数据集和200实例评估基准，以及在黑盒轨迹上通过监督微调和强化学习训练智能体模型。

### Q4: 论文做了哪些实验？

论文围绕ClawGym框架进行了一系列实验。实验设置包括构建数据集、训练模型和评估基准。首先，研究者构建了ClawGym-SynData数据集，包含13.5K经过筛选的任务，这些任务基于人物驱动的意图和技能导向的操作合成，并配备了模拟工作空间和混合验证机制。然后，论文训练了ClawGym-Agents模型家族，通过监督微调黑盒交互轨迹实现，并进一步探索了轻量级强化学习流程，该流程在每任务沙箱中并行化交互。评估环节构建了ClawGym-Bench基准，包含200个经过自动筛选和人工-LLM审核的实例。主要对比方法包括基线模型（如不同基础架构）与ClawGym-Agents的性能比较。关键结果指标未明确列出具体数值，但强调ClawGym-Agents在任务完成率、泛化能力和鲁棒性上优于基线，且强化学习微调进一步提升了性能，尤其是在复杂多步骤工作流中。实验凸显了框架在数据合成、训练和评估全生命周期的有效性。

### Q5: 有什么可以进一步探索的点？

ClawGym 在数据合成、训练与评估上取得了系统性进展，但仍存在可进一步探索的点。首先，其合成数据基于固定的人物意图与技能操作，可能无法涵盖真实世界中用户行为的多样性与长尾需求。未来可引入开放式用户模拟或动态意图生成机制，增强数据覆盖的真实性。其次，SFT 和 RL 训练依赖黑盒环境的 rollout 轨迹，缺乏对中间推理步骤的显式监督。可探索过程奖励模型或基于搜索的推断时干预，提升多步操作的鲁棒性。最后，ClawGym-Bench 的 200 个实例规模有限，且校准完全依赖自动化与人工-LLM 审核，存在评估偏差风险。构建更大规模、基于真实用户交互的动态基准，并引入跨环境迁移能力测试，将有助于验证泛化性。此外，如何在不牺牲安全性的前提下整合大规模工具调用与持久状态管理，也是后续值得深入研究的方向。

### Q6: 总结一下论文的主要内容

ClawGym是一个可扩展框架，旨在系统化地支持Claw风格个人智能体的开发全周期，包括数据合成、模型训练和评估。核心贡献包括：1) ClawGym-SynData: 首个大规模合成数据集，包含13.5K个可执行任务，通过角色驱动自上而下和技能驱动自下而上的双路线合成，并配备混合验证机制（代码检查与评分标准结合）；2) ClawGym-Agents: 在OpenClaw环境中收集高质量轨迹，通过监督微调（SFT）训练智能体，并探索轻量级强化学习（RL）并行化策略；3) ClawGym-Bench: 200个实例的基准测试，经难度感知过滤和人工-LLM审核确保可靠性。实验表明，小模型（如Qwen3-8B）在PinchBench和ClawGym-Bench上分别提升38.90%和43.46%，大模型（如Qwen3-30B-A3B）提升54.68%和25.96%。该工作填补了Claw任务数据稀缺和系统框架缺失的空白，为构建环境导向型智能体提供了可扩展基础。
