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
pdf_url: "https://arxiv.org/pdf/2601.02439v5"
categories:
  - "cs.LG"
  - "cs.CV"
tags:
  - "视觉智能体"
  - "强化学习"
  - "训练环境"
  - "网页交互"
  - "基准评测"
  - "视觉语言模型微调"
relevance_score: 7.5
---

# WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks

## 原始摘要

We present WebGym, the largest-to-date open-source environment for training realistic visual web agents. Real websites are non-stationary and diverse, making artificial or small-scale task sets insufficient for robust policy learning. WebGym contains nearly 300,000 tasks with rubric-based evaluations across diverse, real-world websites and difficulty levels. We train agents with a simple reinforcement learning (RL) recipe, which trains on the agent's own interaction traces (rollouts), using task rewards as feedback to guide learning. To enable scaling RL, we speed up sampling of trajectories in WebGym by developing a high-throughput asynchronous rollout system, designed specifically for web agents. Our system achieves a 4-5x rollout speedup compared to naive implementations. Second, we scale the task set breadth, depth, and size, which results in continued performance improvement. Fine-tuning a strong base vision-language model, Qwen-3-VL-8B-Instruct, on WebGym results in an improvement in success rate on an out-of-distribution test set from 26.2% to 42.9%, significantly outperforming agents based on proprietary models such as GPT-4o and GPT-5-Thinking that achieve 27.1% and 29.8%, respectively. This improvement is substantial because our test set consists only of tasks on websites never seen during training, unlike many other prior works on training visual web agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练视觉网页智能体（visual web agents）时面临的核心挑战：如何构建一个大规模、真实且高效的训练环境，以支持智能体策略的鲁棒学习和泛化能力提升。

研究背景是，随着视觉语言模型（VLMs）在网页任务上展现出潜力，如何将其有效训练为能在真实、动态网页上执行复杂任务的智能体成为关键。现有方法主要依赖两类基准：基于人工模拟网站的环境（如VisualWebArena）虽稳定但真实性不足；基于真实网站的环境（如GAIA-Web）虽更贴近实际，但面临网站非平稳性（如内容动态变化）、任务规模有限、评估信号模糊等问题。更重要的是，现有方法在训练效率上存在严重瓶颈：视觉网页任务需要处理细粒度的渲染界面，数据收集（即轨迹采样）速度缓慢，这阻碍了强化学习（RL）等后训练方法在视觉网页智能体领域的规模化应用，尤其难以扩展到多样化和长视野任务。

因此，本文要解决的核心问题是：**如何构建一个能支持规模化训练视觉网页智能体的环境，以克服现有任务集规模小、多样性不足以及训练效率低下的缺陷**。具体而言，论文提出了WebGym环境，它通过两个关键创新来解决上述问题：1）提供一个包含近30万个任务的大规模、多样化、基于真实网站且带有明确评估准则的任务集，以促进智能体的泛化能力；2）设计一个专门针对网页智能体的高吞吐量异步轨迹采样系统，大幅提升数据收集效率，从而使得在庞大任务集上应用强化学习等训练方法成为可能，最终推动视觉网页智能体性能的实质性提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：视觉网页智能体、评测基准与训练环境，以及在线强化学习的规模化训练。

在**视觉网页智能体**方面，相关工作分为通用视觉语言模型（VLM）和网页专用视觉智能体。前者如Gemma3、GLM-4.1v和Qwen3-VL，通过提示工程或少量网页数据后训练来提升网页任务表现；后者如UI-TARS，则在网页或相关任务上进行了大量后训练。本文训练的智能体基于Qwen-3-VL-8B-Instruct，通过大规模在线强化学习进行微调，与前者相比训练更系统，与后者相比则更侧重于利用真实、多样且规模化的环境进行策略学习。

在**评测基准与训练环境**方面，现有视觉网页评测基准（如WebVoyager、Mind2Web-Live）通常任务集小且经过精心设计，用于评估特定能力。训练环境则相对稀缺，WebRL和PAE框架等初步尝试在任务多样性和难度上有限，且数据收集（rollout）系统未针对速度优化。本文提出的WebGym环境通过基于评分标准的事实组和任务分解来大幅扩展任务多样性（近30万个任务），并设计了高效的全异步rollout系统，实现了4-5倍的加速，从而解决了现有环境规模小、效率低的问题。

在**规模化在线强化学习训练**方面，先前研究（如在软件工程、数学推理等领域）表明，增加在线RL的训练轨迹数量能显著提升智能体能力。本文借鉴了这一思路，但将其应用于视觉网页交互这一具体领域，通过构建跨多领域和难度级别的大规模任务集，并利用从自身交互轨迹中进行的策略性RL训练，实现了在未知网站任务上性能的持续提升。

### Q3: 论文如何解决这个问题？

论文通过构建一个大规模、多样化的训练环境WebGym，并设计高效的异步轨迹采样系统，结合基于强化学习的策略训练方法，来解决视觉网页智能体训练中环境非平稳、任务规模不足和采样效率低下的问题。

**核心方法与架构设计**：
1.  **大规模任务集构建**：论文的核心创新之一是构建了包含近30万个任务的WebGym环境。其方法并非从零开始，而是**聚合了10个现有开源基准和训练集中的任务作为种子**。关键步骤在于利用LLM（GPT-4o）对这些种子任务进行**结构化增强**：
    *   **生成评估准则**：为每个任务生成结构化的评估准则，由多个“事实组”构成，每个组包含一个或多个具体的评估事实。任务的难度被定义为所有事实组中事实的总数。
    *   **任务分解**：对于满足条件（至少2个事实组，且至少一个组是“大”组，即包含≥3个事实）的原始任务，通过生成事实组的有效子集组合，**自动分解出多个更简单、定义良好的子任务**。这既扩展了任务集的深度（从原子任务到组合任务），也提供了更密集的奖励信号，有助于学习。

2.  **高效的异步轨迹采样系统**：为了支撑大规模强化学习训练，论文设计了一个**专门针对网页智能体的高吞吐量异步采样系统**。该系统采用**服务器-客户端架构**，旨在消除传统同步采样中的“突发-空闲”低效问题。
    *   **服务器端**：完全基于CPU，采用主/工作者范式，负责托管和运行浏览器模拟环境。主节点将API请求路由到承载实际模拟器的工作者节点。
    *   **客户端**：托管在GPU上的智能体实例，向服务器发送请求。通过一个**操作特定的本地队列**来管理请求，在资源紧张的情况下均匀分配CPU和GPU负载。
    *   **创新点**：此系统实现了**真正的异步多步模拟**。每个浏览会话在独立的进程中运行，一旦资源可用，新任务立即开始推理，无需等待其他会话完成步骤或整个回合。这使得CPU和GPU的利用率更加平滑和高效。

3.  **强化学习训练策略**：在构建的任务集和高效的采样系统基础上，论文采用了一种**简单的在线强化学习配方**来训练智能体。
    *   **策略更新**：使用基于二元终端奖励的**REINFORCE算法**（无基线或负梯度）。这本质上等同于**在线过滤的行为克隆**，即只保留成功的轨迹，并最大化其对数似然。这种方法训练稳定，避免了失败轨迹带来的负面影响。
    *   **基座模型**：使用强大的开源视觉语言模型**Qwen-3-VL-8B-Instruct**作为基础策略进行微调。
    *   **动作空间**：扩展了常见的网页交互动作，包括点击、输入、滚动、返回上一页以及导航到指定网站，并直接在基于坐标的截图模式（无标记）下操作。

**整体效果与创新点**：
通过上述方法的结合，论文实现了两个维度的扩展：**任务集的广度、深度和规模**，以及**采样效率**。异步采样系统相比朴素实现带来了**4-5倍的采样加速**。在如此大规模且多样化的任务集上训练，使得智能体性能持续提升。最终，在完全由训练中未见网站任务组成的分布外测试集上，成功率从基座模型的26.2%显著提升至42.9%，超越了基于GPT-4o等专有模型的智能体。核心创新在于**通过LLM驱动的结构化任务构建与分解，创建了大规模、高质量、有评估准则的任务环境**，并配套设计了**首个针对网页智能体优化的开源异步采样系统**，从而成功地将强化学习规模化应用于视觉网页智能体的训练。

### Q4: 论文做了哪些实验？

论文实验主要包括训练视觉网页智能体，并围绕两个核心问题展开：一是如何通过强化学习训练将现有视觉语言模型高效转化为能解决复杂网页任务的智能体，二是研究在大规模多样化任务集上训练时智能体泛化能力的提升。

**实验设置**：采用基于坐标的截图模式作为观测输入，动作空间包括点击、输入、滚动、返回上一页和导航到指定网站。策略更新使用简单的REINFORCE算法，仅基于二元终端奖励（成功为1，失败为0）进行正梯度优化，相当于在线过滤的行为克隆。训练时限制每个回合的最大交互步数以保持采样效率。

**数据集/基准测试**：使用WebGym环境，包含近30万个任务，覆盖多样化的真实网站和不同难度级别。测试集采用训练中从未见过的网站任务，以评估泛化能力。

**对比方法**：与基于闭源模型的智能体进行对比，包括GPT-4o和GPT-5-Thinking。

**主要结果与关键指标**：通过强化学习训练，基于Qwen-3-VL-8B-Instruct模型的智能体在分布外测试集上的成功率从初始的26.2%提升至42.9%。相比之下，GPT-4o和GPT-5-Thinking模型的表现分别为27.1%和29.8%。此外，论文开发的高吞吐量异步轨迹采样系统相比朴素实现实现了4-5倍的加速。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于，尽管WebGym在规模和真实性上取得了突破，但其任务评估主要依赖预设的评分标准，可能无法完全捕捉复杂、多步骤任务中的人类偏好和细微成功标准。此外，强化学习训练对计算资源要求高，且策略的泛化能力仍需在更广泛、动态变化的真实网站（如涉及JavaScript动态加载、用户登录状态维持）上进一步验证。

未来研究方向可包括：1) 开发更高效、样本利用率更高的离线或模仿学习算法，以降低与真实环境交互的高昂成本；2) 引入多模态反馈（如自然语言指令修正）来增强智能体对模糊任务的理解和适应性；3) 探索智能体在长期、跨会话任务中的记忆与规划能力，例如需要多次返回同一网站完成的操作。结合见解，一个可能的改进思路是构建“网站模拟器”或世界模型，通过预测网页状态变化来减少真实交互次数，从而加速训练并提高在未见网站上的零样本泛化性能。

### Q6: 总结一下论文的主要内容

这篇论文提出了WebGym，一个用于训练视觉网页智能体的大规模开源环境。其核心问题是现有训练环境通常基于人工或小规模任务集，无法应对真实网站的多样性和非平稳性，导致学到的策略不够鲁棒。为此，WebGym构建了包含近30万个任务的庞大集合，这些任务覆盖了多样化的真实网站和不同难度级别，并配有基于量规的评估方法。

在方法上，论文采用了一个简单的强化学习配方，利用智能体自身交互轨迹（rollouts）进行训练，并以任务奖励作为学习反馈。为了支撑大规模RL训练，作者专门为网页智能体开发了一个高吞吐量的异步轨迹采样系统，相比简单实现获得了4-5倍的加速。此外，他们通过扩展任务的广度、深度和规模来持续提升性能。

主要结论是，在WebGym上对强大的基础视觉语言模型Qwen-3-VL-8B-Instruct进行微调后，其在一个分布外测试集上的成功率从26.2%显著提升至42.9%。这个测试集完全由训练中未出现过的网站任务构成，而该智能体的表现大幅超越了基于GPT-4o（27.1%）和GPT-5-Thinking（29.8%）等专有模型的智能体。这证明了WebGym在规模化、真实环境下训练鲁棒视觉网页智能体的有效性和重要意义。
