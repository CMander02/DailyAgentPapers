---
title: "CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents"
authors:
  - "Bowen Wang"
  - "Dunjie Lu"
  - "Junli Wang"
  - "Tianyi Bai"
  - "Shixuan Liu"
  - "Zhipeng Zhang"
  - "Haiquan Wang"
  - "Hao Hu"
  - "Tianbao Xie"
  - "Shuai Bai"
  - "Dayiheng Liu"
  - "Que Shen"
  - "Junyang Lin"
  - "Tao Yu"
date: "2026-05-25"
arxiv_id: "2605.25624"
arxiv_url: "https://arxiv.org/abs/2605.25624"
pdf_url: "https://arxiv.org/pdf/2605.25624v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Computer-Use Agent"
  - "Reinforcement Learning with Verifiable Rewards"
  - "Training Data Synthesis"
  - "Agent Benchmark"
  - "Multi-Agent Orchestration"
  - "Web Agent"
  - "GUI Agent"
  - "Environment Generation"
  - "Open Source"
relevance_score: 9.5
---

# CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has driven breakthroughs in domains such as math, tool-use, and software engineering, yet its extension to computer-use agents (CUAs) has been bottlenecked by the scarcity of scalable training data with deterministic rewards. Constructing such data for CUAs requires consistent task instruction, executable environment, and verifiable reward. However, hand-curated benchmarks achieve high reward fidelity but cover few applications and LLM-as-judge-based datasets scale broadly but lack reliable verification. We present CUA-Gym, a scalable pipeline that co-generates task instructions, environment states, and reward functions. Concretely, a Generator agent constructs the initial and golden environment states, and a separate Discriminator agent writes the reward function from the task specification. An orchestrator agent drives the two through iterative rounds upon execution. Generated tuples then pass a final filter combining LLM majority voting and agent rollouts, ensuring quality beyond the per-task adversarial loop. To address the scarcity of training environments, we further synthesize CUA-Gym-Hub, a broad suite of high-fidelity mock web applications grounded in real-world software-use distributions, expanding the scale of CUA RLVR data by magnitude. Using this pipeline, we construct CUA-Gym, a dataset of 32,112 verified RLVR training tuples grounded in 110 environments. Trained with GSPO on CUA-Gym, our CUA-Gym-A3B and CUA-Gym-A17B achieve 62.1% and 72.6% on OSWorld-Verified, outperforming prior open-source CUAs at comparable scales, with performance scaling smoothly in both data volume and environment diversity. The same checkpoints also improve on the held-out WebArena benchmark, indicating transfer beyond the training environments. We will open-source the full synthesis pipeline, dataset, CUA-Gym-Hub environments, and models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将基于可验证奖励的强化学习（RLVR）成功扩展到计算机使用智能体（CUA）时面临的核心瓶颈：缺乏规模化、可验证且具有确定性的训练数据。

研究背景上，RLVR在数学、软件工程等领域的突破已证明其有效性，其关键在于能大规模合成带有确定性奖励信号的训练任务。然而，CUA领域的RLVR数据构建存在结构性困难：一个完整的训练实例需要任务指令、可执行环境状态和奖励函数三要素的协同，这让数据生成远比纯文本领域复杂。现有方法均无法同时满足可验证奖励、广泛的应用覆盖和可扩展的任务多样性三个关键特性：人工构造的基准代价高昂且覆盖有限；基于大语言模型作为评判者的方案引入奖励噪声，不利于策略稳定优化；基于代码的流水线虽能生成确定性奖励，但规模有限且环境单一。这导致CUA RLVR的数据规模远落后于数学和代码领域，阻碍了其性能随数据量增长而提升的路径。

因此，本文的核心问题是：如何设计一个可扩展的流水线，能够自动、大规模地合成高质量的、带有确定性可验证奖励的CUA训练数据，并同时提供足够多样化的训练环境，从而将RLVR的成功经验从数学/代码领域迁移到复杂的计算机使用智能体任务上。

### Q2: 有哪些相关研究？

在相关研究方面，本文涉及数据合成与后训练、GUI智能体任务与环境合成两类工作。

**数据合成与后训练**：软件工程中，SWE-smith、R2E-Gym和SWE-Gym通过程序化检查合成可验证任务，终端操作中Endless Terminals和Terminal-Task-Gen利用双验证协议生成CLI任务。这些工作均展示RLVR在数字智能体领域具有规模扩展潜力，但尚未涉及GUI领域。本文创新性将这些思路扩展到计算机使用智能体，构建了首例大规模RLVR训练数据集。

**任务与环境合成**：GUI智能体领域，ZeroGUI采用VLM奖励估计但存在假阳性问题；GUI-Genesis、InfiniteWeb和AutoWebWorld通过代码原生奖励或acles合成了可控网页环境，但局限于浏览器交互，无法覆盖桌面级或跨应用任务。本文的CUA-Gym-Hub通过合成高保真模拟Web应用，首次实现了确定性可验证奖励、广泛OS级应用覆盖和可扩展任务多样性的统一，填补了现有工作空白。

### Q3: 论文如何解决这个问题？

CUA-Gym通过一个协同生成管线，联合生成任务指令、环境状态和奖励函数，以解决计算机使用智能体（CUA）在可验证强化学习（RLVR）训练数据上的稀缺性问题。整体框架由一个编排器（Orchestrator Agent）驱动一对对抗耦合的子智能体——生成器（Generator）和判别器（Discriminator）——在多轮迭代中逐步构建数据元组。

核心方法分为两步：首先，从任务指令和上下文生成初始与最终环境状态脚本（initial_setup.py和golden_patch.py），并由判别器在严格信息隔离下独立编写奖励函数（reward.py），避免奖励与构造过程的相关性。编排器检查五个一致性条件，确保元组内部一致。其次，通过数据集级过滤器，结合大模型多数投票和教师智能体回滚，剔除模糊或不可解任务，保证训练效用。

在架构上，CUA-Gym还构建了CUA-Gym-Hub，一套自主合成的高保真模拟Web应用程序，覆盖110个环境（如通信、生产力、电商等），支持状态注入与会话隔离，使并行RL训练成为可能。关键技术包括：对抗性分角色协作、信息屏障保证奖励真实性、LLM+回滚双阶段过滤提升数据质量，以及多智能体管线（计划、开发、测试）自动化模拟环境合成。最终生成了32,112个已验证的RLVR训练元组，在OSWorld-Verified和WebArena上取得领先性能，证明了数据规模和多样性的平滑扩展能力。

### Q4: 论文做了哪些实验？

论文在Qwen3.5系列的两个参数规模（小模型和大模型）上进行实验。实验使用CUA-Gym生成的10,858个经验证的RLVR训练元组，覆盖80+个环境，另包含3,578条SFT预热轨迹。训练算法采用Group Sequence Policy Optimization (GSPO)，并使用一种确定性轨迹切片脚手架来管理长序列图像历史。

主要结果在两个基准测试上报告：OSWorld-Verified和WebArena。对比方法包括专有模型（Claude Sonnet 4.6、Claude Opus 4.7、GPT-5.5）和开源模型（EvoCUA-8B/32B、OpenCUA-32B/72B等）。

关键结果：CUA-Gym-A3B在OSWorld-Verified上达到62.1%（较基准提升7.6个百分点），在WebArena上达到44.5%（提升3.7pp）；CUA-Gym-A17B在OSWorld-Verified上达到72.6%（提升10.4pp），在WebArena上达到56.0%（提升2.0pp）。在多个子领域（多应用工作流+21.5pp、LibreOffice Calc+14.9pp、VS Code+13.6pp）均有显著提升。实验验证了RLVR训练数据质量和可扩展性，且性能在数据量和环境多样性上平滑扩展，并成功迁移到未见的WebArena基准。

### Q5: 有什么可以进一步探索的点？

这项研究通过CUA-Gym构建了可验证训练数据，但其终端状态验证的局限性在于无法捕捉中间步骤的正确性。例如，智能体可能通过低效或错误的操作序列偶然达到正确终端状态，而缺乏对任务解构逻辑的监督。未来可引入过程级奖励信号，例如基于子目标达成度的增量验证，或利用逆强化学习从执行轨迹中推断隐式意图。此外，当前环境合成依赖预定义的领域模板，对长尾或动态交互场景覆盖不足，可探索用大语言模型生成更开放的模拟环境，并结合对抗性训练增强鲁棒性。另一个方向是验证奖励函数的泛化性——当前过滤器依赖LLM投票和回滚测试，但可能受自洽偏差影响，可设计跨模型交叉验证机制或人类反馈校准。最终，将强化学习与元学习结合，使智能体在少量新环境上快速适应，可能是突破数据瓶颈的关键。

### Q6: 总结一下论文的主要内容

计算机使用智能体的强化学习面临可验证奖励训练数据稀缺的瓶颈。本文提出CUA-Gym，一个可扩展的流水线，能协同生成任务指令、环境状态和奖励函数。具体地，由生成器构建初始与目标环境状态，判别器根据任务描述编写奖励函数，编排器驱动二者通过迭代执行确保质量。为扩大训练环境，进一步合成CUA-Gym-Hub，基于真实软件使用分布构建高质量模拟网页应用。最终构建包含32,112个验证过的训练元组、覆盖110个环境的数据集。训练后的CUA-Gym-A3B和CUA-Gym-A17B在OSWorld-Verified上分别达到62.1%和72.6%的准确率，优于同规模开源模型，并展现出在数据量和环境多样性上的平滑缩放能力。这项工作首次展示了可验证奖励范式在计算机使用领域的可扩展性，环境多样性被证明是独立于数据量的缩放轴。
