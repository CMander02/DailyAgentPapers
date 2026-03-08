---
title: "Tool Verification for Test-Time Reinforcement Learning"
authors:
  - "Ruotong Liao"
  - "Nikolai Röhrich"
  - "Xiaohan Wang"
  - "Yuhui Zhang"
  - "Yasaman Samadzadeh"
date: "2026-03-02"
arxiv_id: "2603.02203"
arxiv_url: "https://arxiv.org/abs/2603.02203"
pdf_url: "https://arxiv.org/pdf/2603.02203v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "T^3RL (Tool-Verification for Test-Time Reinforcement Learning)"
  primary_benchmark: "MATH-500, AMC, AIME 2024"
---

# Tool Verification for Test-Time Reinforcement Learning

## 原始摘要

Test-time reinforcement learning (TTRL) has emerged as a promising paradigm for self-evolving large reasoning models (LRMs), enabling online adaptation on unlabeled test inputs via self-induced rewards through majority voting. However, a spurious yet high-frequency unverified consensus can become a biased and reinforced reward signal, leading to incorrect mode collapse. We address this failure mode with T^3RL (Tool-Verification for Test-Time Reinforcement Learning), which introduces test-time tool verification into reward estimation. Concretely, a verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training. Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T^3RL significantly improves over TTRL, with larger gains on harder problems. More broadly, T^3RL can be viewed as verified online data synthesis, highlighting test-time tool verification as a key mechanism for stabilizing self-evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决测试时强化学习（TTRL）中因“伪高频共识”导致的错误模式崩溃问题。研究背景是，随着大型推理模型（LRMs）进入自进化时代，测试时强化学习成为一种有前景的范式，它允许模型在无标注的测试输入上，通过多数投票产生自我诱导的奖励信号，实现在线适应和性能提升。然而，现有TTRL方法存在一个根本性缺陷：当模型内部推理存在偏差时，基于自我一致性的多数投票可能形成一个虚假但高频的“共识”，这个未经核实的共识会作为有偏的奖励信号被强化学习过程进一步放大，最终导致模型错误地收敛到不正确的答案上，即发生“伪流行模式崩溃”。

本文要解决的核心问题，正是如何使这种无标签的自进化过程对上述“伪流行模式崩溃”具有鲁棒性。作者认为，人类在面临类似困境时会寻求外部证据进行验证，而现有TTRL方法恰恰缺少这样一个能够打破自我共识闭环的外部验证机制。因此，本文提出了T³RL方法，其核心思想是将测试时工具验证引入奖励估计过程。具体而言，该方法通过一个验证器调用外部工具（如代码执行器）作为证据，在投票时提升已验证推理路径的权重，从而产生更可靠的伪标签用于训练，引导模型从学习“高频模式”转向学习“已验证的正确模式”，以稳定自进化过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**测试时验证**与**测试时训练**。

在**测试时验证**方面，已有研究利用外部验证器（如奖励模型、生成式验证器、符号检查或多智能体系统）来评估额外计算的质量，并从多个候选输出中选择最佳答案。近期，工具集成推理（TIR）进一步将工具使用形式化为一种稳健的证据来源。然而，这些工作均未在测试时训练（即在推理过程中进行参数更新）的框架下探索验证机制。本文的T³RL首次将验证引入测试时训练，利用工具验证将采样的推理轨迹转化为带有证据标签的在线训练实例，从而塑造训练过程，实现一种“已验证的在线数据合成”。

在**测试时训练**方面，测试时训练（TTT）旨在推理阶段适应模型参数以处理分布偏移，已应用于视频生成、理解及大语言模型等领域。其最新进展是测试时强化学习（TTRL），它结合了无监督强化学习和带可验证奖励的强化学习（RLVR）。尽管TTRL为自进化人工智能提供了框架，但现有研究均未讨论如何应对虚假奖励估计对自进化过程的挑战。本文首次提出了针对自进化的测试时验证，特别是基于工具的证据验证，以生成更可靠的奖励信号。这在日益依赖工具交互、又需要可靠奖励来实现稳定在线学习的智能体系统中具有更广泛的意义。

### Q3: 论文如何解决这个问题？

论文通过提出T³RL框架来解决测试时强化学习中因虚假高频共识导致的奖励信号偏差和错误模式崩溃问题。其核心方法是将工具验证机制集成到奖励估计过程中，以产生更可靠的伪标签用于模型训练。

整体框架包含三个核心组件：外部验证器、验证工具和验证权重。首先，外部验证器是一个大型语言模型，负责将推理轨迹编译成可执行的Python代码，并基于执行输出判断其有效性。其次，验证工具是一个代码解释器，执行生成的Python程序并将输出信号返回给验证器。最后，验证权重用于取代简单多数投票，引入验证感知的加权投票机制，提升已验证轨迹的投票权重。

具体流程如下：对于输入提示x，从策略中采样N条推理轨迹，验证器对每条轨迹进行评估，生成三元组（验证器得出的答案a_i，验证指示器v_i）。验证工具提供外部确定性证据，通过执行代码并对比输出与轨迹提取的候选答案，产生工具验证的有效性指示。在加权机制中，引入超参数ω来量化已验证轨迹相对于未验证轨迹的投票权重，未验证轨迹权重为1，已验证轨迹权重为ω≥1。通过验证感知的共识标签计算，最大化总加权投票质量，使共识从最频繁答案转向已验证答案。

创新点在于将工具验证作为稳定自我进化的关键机制，通过外部可执行证据提升奖励信号的可靠性。该方法在数学推理任务中显著提升了性能，尤其在难题上增益更大，体现了验证在线数据合成的有效性。

### Q4: 论文做了哪些实验？

论文在三个数学推理基准测试上进行了实验：AIME 2024、AMC和MATH-500。实验设置遵循测试时强化学习范式，评估了多种骨干模型，包括基础模型（如Qwen-2.5-1.5B、Qwen-3-4B）、数学专用模型（如Qwen-2.5-Math-1.5B）和指令微调模型（如Llama-3.2-1B-Instruct）。主要对比方法是基线模型和原始的测试时强化学习方法（TTRL）。实验采用GRPO进行训练，使用AdamW优化器和余弦学习率调度，峰值学习率为5e-7。生成64个响应进行标签估计，并下采样至32个用于训练，最大令牌长度为2560。

主要结果显示，提出的T³RL方法在所有模型和基准上均一致优于TTRL。关键数据指标如下：在Qwen-2.5-Math-1.5B上，T³RL在MATH-500、AMC和AIME 2024的准确率分别达到74.6%、50.9%和20.8%，相比TTRL分别提升了2.2%、4.1%和31.6%。平均而言，T³RL在MATH-500、AMC和AIME 2024上相比TTRL的相对提升分别为3.5%、9.7%和19.8%，整体提升达11.0%。此外，在MATH-500的难度分级（L1最简单，L5最难）中，T³RL在最高难度L5上的提升最为显著（相比TTRL提升4.3%），表明该方法对更复杂问题效果更佳。消融实验验证了测试时验证、工具辅助验证和验证加权投票三个关键组件的贡献，其中适中的验证权重（c=5）取得了最佳性能。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心局限性在于对验证器（Verifier）的强依赖。当验证器能力较弱时（如论文中提到的Qwen-0.5B），其工具调用可能引入噪声，导致验证感知投票错误加权，反而使伪标签估计不如传统的多数投票稳定。此外，在任务本身较为简单、模型输出已高度一致的情况下，工具验证带来的边际收益有限，增加了计算开销却未显著提升性能。

未来研究方向可以从以下几个维度深入探索：
1.  **验证器的鲁棒性与效率**：研究如何设计更鲁棒、轻量级的验证器，或开发无需依赖强大外部验证器的自验证机制，以降低框架对特定工具的敏感性和计算成本。
2.  **动态计算分配策略**：论文指出验证能提升每个rollout的质量，减少对大规模采样的依赖。未来可研究自适应的测试时计算分配算法，动态权衡“采样更多rollout”与“进行更深入验证”之间的资源分配，以在固定预算下实现最优性能。
3.  **错误诊断与纠正机制**：当前框架主要依赖验证来调整奖励信号。可以进一步探索如何利用验证过程中产生的证据（如代码执行错误、逻辑矛盾）来诊断推理链中的具体错误类型，并引导模型进行更有针对性的修正和学习，而不仅仅是重新加权。
4.  **扩展到更复杂领域**：论文在数学推理任务上验证了有效性。未来可探索在需要多步骤工具调用、动态环境交互或长程规划的更复杂任务（如复杂代码生成、具身推理）中应用和评估该框架，研究其泛化能力和面临的挑战。

### Q6: 总结一下论文的主要内容

该论文针对测试时强化学习（TTRL）中存在的“伪高频率未验证共识”导致错误模式崩溃的问题，提出了T³RL方法，其核心贡献是在奖励估计中引入了测试时工具验证机制。具体而言，T³RL通过一个验证器，利用外部工具（如代码执行）提供的证据，在验证感知的投票中对已验证的推理路径（rollouts）赋予更高权重，从而生成更可靠的伪标签用于模型训练。实验在多个数学基准（MATH-500、AMC、AIME 2024）和不同骨干模型上进行，结果表明T³RL相比TTRL取得了显著提升，且在更难的问题上增益更大。论文将T³RL更广泛地定位为一种经过验证的在线数据合成方法，强调了测试时工具验证是实现模型稳定自我演化的关键机制。
