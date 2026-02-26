---
title: "WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks"
authors:
  - "Hao Bai"
  - "Alexey Taymanov"
  - "Tong Zhang"
  - "Aviral Kumar"
  - "Spencer Whitehead"
date: "2026-01-05"
arxiv_id: "2601.02439"
arxiv_url: "https://arxiv.org/abs/2601.02439"
pdf_url: "https://arxiv.org/pdf/2601.02439v4"
categories:
  - "cs.LG"
  - "cs.CV"
tags:
  - "视觉智能体"
  - "强化学习"
  - "训练环境"
  - "网页交互"
  - "基准评测"
  - "可扩展性"
  - "离线学习"
relevance_score: 8.0
---

# WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks

## 原始摘要

We present WebGym, the largest-to-date open-source environment for training realistic visual web agents. Real websites are non-stationary and diverse, making artificial or small-scale task sets insufficient for robust policy learning. WebGym contains nearly 300,000 tasks with rubric-based evaluations across diverse, real-world websites and difficulty levels. We train agents with a simple reinforcement learning (RL) recipe, which trains on the agent's own interaction traces (rollouts), using task rewards as feedback to guide learning. To enable scaling RL, we speed up sampling of trajectories in WebGym by developing a high-throughput asynchronous rollout system, designed specifically for web agents. Our system achieves a 4-5x rollout speedup compared to naive implementations. Second, we scale the task set breadth, depth, and size, which results in continued performance improvement. Fine-tuning a strong base vision-language model, Qwen-3-VL-8B-Instruct, on WebGym results in an improvement in success rate on an out-of-distribution test set from 26.2% to 42.9%, significantly outperforming agents based on proprietary models such as GPT-4o and GPT-5-Thinking that achieve 27.1% and 29.8%, respectively. This improvement is substantial because our test set consists only of tasks on websites never seen during training, unlike many other prior works on training visual web agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练视觉网页智能体（visual web agents）时面临的核心挑战：如何构建一个大规模、真实且高效的训练环境，以支持智能体策略的鲁棒学习和泛化。研究背景是，随着视觉语言模型（VLMs）在网页任务上展现出潜力，如何让智能体像人类一样通过观察网页截图（而非仅依赖文本如无障碍树）来完成复杂、长周期的真实任务（如比价、信息查找）成为关键。然而，现有方法存在明显不足：一方面，多数训练环境要么基于人工模拟网站，缺乏真实性；要么虽使用真实网站但任务集规模小、多样性有限，且真实网站的非平稳性（如内容动态变化）使得小规模任务集难以让智能体学到稳健策略。另一方面，现有训练方法（尤其是强化学习）在视觉网页领域难以扩展，因为网页交互的轨迹采样（rollout）速度慢（受浏览器模拟计算开销大、奖励信号模糊等因素制约），导致数据收集效率低下，阻碍了基于大规模任务集的策略训练。

因此，本文要解决的核心问题是：如何构建一个能够支持视觉网页智能体规模化训练的环境，具体包括（1）提供一个大规模、多样化、基于真实网站且带有清晰评估标准的任务集，以促进智能体的泛化能力；（2）设计一个高效的异步轨迹采样系统，大幅提升数据收集速度，从而突破训练效率瓶颈。通过引入WebGym环境（包含近30万个任务和高效的异步采样系统），论文试图证明，在任务集的广度、深度和规模上进行扩展，并结合高效的训练流程，能够显著提升视觉网页智能体在未见网站任务上的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：视觉网页智能体、评测基准与训练环境，以及在线强化学习的规模化训练。

在**视觉网页智能体**方面，相关工作分为通用视觉语言模型（VLM）和网页专用视觉智能体。前者如Gemma3、GLM-4.1v和Qwen3-VL，通过提示工程或少量网页数据后训练来提升在网页任务上的表现；后者如UI-TARS，则是在网页或相关任务上进行了大量后训练。本文训练的智能体基于Qwen-3-VL-8B-Instruct，通过在大规模环境（WebGym）中进行强化学习微调，显著超越了这些通用模型以及GPT-4o等专有模型在分布外测试集上的性能。

在**评测基准与训练环境**方面，现有工作如WebVoyager、Mind2Web-Live等评测基准，任务集规模较小且经过精心设计，侧重于评估特定能力。而训练环境（如WebRL和PAE框架）虽提供了训练系统，但其任务集在多样性和难度上有限，且数据收集（rollout）系统未针对速度优化。本文提出的WebGym环境通过基于评分标准的事实组和任务分解，极大地扩展了任务的多样性和规模（近30万个任务），并设计了一个完全异步的高吞吐量rollout系统，实现了4-5倍的加速，从而解决了现有环境在规模和效率上的不足。

在**规模化在线强化学习训练**方面，先前研究（如在软件工程、数学推理等领域）表明，通过在线RL增加训练轨迹数量能有效提升智能体能力。本文借鉴了这一思路，构建了跨多领域和难度级别的大规模多样化任务集，并利用从自身交互轨迹中收集的数据进行在线策略RL训练，验证了通过扩展任务集的广度、深度和规模可以带来持续的性能提升。

### Q3: 论文如何解决这个问题？

论文通过构建一个大规模、多样化的训练环境WebGym，并设计高效的异步轨迹采样系统，结合基于强化学习的策略训练方法，来解决视觉网页智能体训练中环境非平稳、任务规模不足以及采样效率低下的问题。

**核心方法与架构设计**：
1.  **大规模、结构化任务集的构建**：这是解决环境多样性和任务规模问题的核心。论文从10个现有基准和训练集中收集种子任务，并利用GPT-4o进行**程序化扩展**。关键创新在于**基于评估准则的任务分解**。具体流程为：首先为每个任务生成结构化的评估准则，将其组织为包含若干事实的“事实组”；然后，将任务的难度定义为所有事实组中事实的总数。对于满足条件（至少2个事实组，且至少一个组是“大”组，即包含≥3个事实）的原始任务，算法通过选择事实组的有效子集（每个子集必须包含至少一个“大”组）来生成新的、难度更低但定义明确的分解任务。这极大地扩展了任务集的**广度**（覆盖127,645个网站）和**深度**（从原子任务到组合任务），最终构建了包含近30万个任务的训练集，并严格划分了训练/测试集，确保测试任务来自训练中完全未见的网站。

2.  **高效异步轨迹采样系统**：这是解决强化学习训练中采样瓶颈的关键。传统同步采样系统存在“突发-空闲”行为，导致硬件利用率低下。WebGym设计了一个**服务器-客户端架构的异步采样框架**。
    *   **服务器端**：采用主/工作者范式，完全基于CPU运行浏览器模拟环境。主节点将API请求路由到承载实际模拟器的工作者节点。
    *   **客户端**：承载运行在GPU上的智能体实例，并向服务器发送请求。通过一个操作特定的本地队列来管理请求，在资源紧张的情况下均匀分配CPU和GPU负载。
    *   **创新点**：该系统消除了步骤和回合级别的全局同步屏障。一旦观察就绪，工作进程立即将数据流式传输给GPU进行推理，使得新的采样过程可以尽早加入，从而平滑了CPU和GPU的负载，避免了空闲等待。实验表明，该系统在CPU受限的情况下实现了**4-5倍的采样速度提升**，并且随着GPU节点增加，系统吞吐量接近线性扩展。

3.  **基于强化学习的策略训练**：
    *   **整体框架**：采用简单的在线强化学习流程，利用智能体自身在WebGym中交互产生的轨迹（rollouts），以任务奖励作为反馈来指导学习。
    *   **策略更新**：使用基于二元终端奖励的REINFORCE算法（无基线或负梯度），这等价于**在线过滤的行为克隆**，即只保留成功轨迹并最大化其对数似然。这种方法避免了失败轨迹的负梯度，提高了训练稳定性。
    *   **基础模型与动作空间**：以强大的视觉语言模型Qwen-3-VL-8B-Instruct作为基础策略进行微调。动作空间扩展了点击、输入、滚动、返回、导航到指定网站等操作，并直接在坐标模式下运行（无需元素标记）。
    *   **训练技巧**：包括对任务进行随机采样或按难度比例采样，在训练时控制最大交互步数以保持采样效率，以及动态屏蔽无法访问的网站。

**总结**：论文的创新点在于**将大规模、结构化任务构建程序与高性能异步采样系统相结合**，为视觉网页智能体提供了一个前所未有的、可扩展的训练平台。通过在此平台上应用简单的强化学习配方微调基础VLM，成功将智能体在未见网站任务上的成功率从26.2%显著提升至42.9%，超越了基于GPT-4o等专有模型的智能体。

### Q4: 论文做了哪些实验？

论文实验主要包括训练视觉网页智能体，并围绕两个核心问题展开：一是如何通过强化学习训练将现有视觉语言模型转化为能高效解决复杂网页任务的智能体，二是探究在大规模多样化任务集上训练时智能体泛化能力的提升。

**实验设置**：采用基于坐标的截图模式作为观测输入，动作空间包括点击、输入、滚动、返回上一页和导航到指定网站。策略更新使用简单的REINFORCE算法，仅利用二元终端奖励（成功为1，失败为0），相当于在线过滤的行为克隆，仅最大化成功轨迹的对数似然。训练时设定了交互步数上限以保持效率。

**数据集/基准测试**：使用WebGym环境，包含近30万个任务，覆盖多样化的真实网站和不同难度级别。测试集采用训练中从未见过的网站任务，以评估泛化能力。

**对比方法**：与基于闭源模型（如GPT-4o和GPT-5-Thinking）的智能体进行对比。同时，对任务采样方法（随机采样与按难度比例采样）进行了消融实验。

**主要结果与关键指标**：通过强化学习训练，基于Qwen-3-VL-8B-Instruct模型的智能体在分布外测试集上的成功率从初始的26.2%提升至42.9%。相比之下，基于GPT-4o和GPT-5-Thinking的智能体分别仅达到27.1%和29.8%的成功率。此外，研究还开发了高吞吐量异步轨迹采样系统，相比朴素实现实现了4-5倍的加速，并展示了任务集的广度、深度和规模的扩展能持续带来性能改进。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其任务环境虽规模庞大，但主要基于静态网页快照，未能充分模拟动态交互（如实时更新的内容或复杂JavaScript交互），且评估主要依赖预设规则，可能无法全面反映真实用户意图。未来研究可探索多模态输入的更深度融合，例如结合语音指令或屏幕阅读器信息以增强可访问性。此外，当前强化学习策略的样本效率仍有提升空间，可引入课程学习或分层强化学习来逐步攻克复杂任务。另一个方向是开发更通用的动作空间，使智能体能跨网站迁移技能，而不仅限于训练过的站点。最后，引入人类反馈或对抗性测试能进一步提升智能体的鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

这篇论文提出了WebGym，一个用于训练视觉网页智能体的大规模开源环境。其核心问题是现有训练环境通常基于人工或小规模任务集，无法应对真实网站的多样性和非平稳性，导致学到的策略不够鲁棒。为此，WebGym构建了包含近30万个任务的庞大集合，这些任务覆盖了多样化的真实网站和不同难度级别，并配有基于量规的评估方法。

在方法上，论文采用了一个简单的强化学习配方，利用智能体自身交互轨迹进行训练，并以任务奖励作为学习反馈。为了支撑大规模RL训练，作者专门为网页智能体开发了一个高吞吐量的异步轨迹采样系统，相比简单实现获得了4-5倍的加速。此外，他们通过扩展任务的广度、深度和规模来持续提升性能。

主要结论是，在WebGym上对强大的基础视觉语言模型Qwen-3-VL-8B-Instruct进行微调后，其在一个分布外测试集上的成功率从26.2%显著提升至42.9%。这个测试集完全由训练中未出现过的网站任务构成，而该模型的表现大幅超越了基于GPT-4o和GPT-5-Thinking等专有模型的智能体。这证明了WebGym在训练能够泛化到新网站的、鲁棒的视觉网页智能体方面的有效性和重要意义。
