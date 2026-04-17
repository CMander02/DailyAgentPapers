---
title: "SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling"
authors:
  - "Hao Han"
  - "Jin Xie"
  - "Xuehao Ma"
  - "Weiquan Zhu"
  - "Ziyao Zhang"
  - "ZhiLiang Long"
  - "Hongkai Chen"
  - "Qingwen Ye"
date: "2026-04-16"
arxiv_id: "2604.14820"
arxiv_url: "https://arxiv.org/abs/2604.14820"
pdf_url: "https://arxiv.org/pdf/2604.14820v1"
categories:
  - "cs.SE"
tags:
  - "Agent Architecture"
  - "Reinforcement Learning for Agents"
  - "Tool Use / Code Agent"
  - "Process Reward Model"
  - "Long-Horizon Reasoning"
  - "Benchmark Evaluation"
  - "Inference Optimization"
relevance_score: 9.0
---

# SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling

## 原始摘要

Resolving real-world software engineering (SWE) issues with autonomous agents requires complex, long-horizon reasoning. Current pipelines are bottlenecked by unoptimized demonstration data, sparse execution rewards, and computationally prohibitive inference scaling, which collectively exacerbate token bloat, reward hacking, and policy degradation. We present SWE-TRACE (Trajectory Reduction and Agentic Criteria Evaluation), a unified framework optimizing the SWE agent lifecycle across data curation, reinforcement learning (RL), and test-time inference. First, we introduce an LLM multi-task cascading method, utilizing stepwise oracle verification to distill a 60K-instance Supervised Fine-Tuning (SFT) corpus strictly biased toward token-efficient, shortest-path trajectories. Second, to overcome the instability of sparse outcome rewards, we design a MemoryAugmented Agentic RL pipeline featuring a Rubric-Based Process Reward Model (PRM). An auxiliary Rubric-Agent provides dense, fine-grained heuristic feedback on intermediate steps, guiding the model through long-horizon tasks. Finally, we bridge training and inference by repurposing the PRM for heuristic-guided Test-Time Scaling (TTS). By dynamically evaluating and pruning action candidates at each step, SWE-TRACE achieves superior search efficiency without the latency overhead of standard parallel sampling. Extensive experiments on standard SWE benchmarks demonstrate that SWE-TRACE significantly advances the state-of-the-art, maximizing resolution rates while drastically reducing both token consumption and inference latency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决构建高效、强大的自主软件工程（SWE）智能体时所面临的系统性挑战。研究背景是，随着大语言模型从被动代码生成器演变为能够在真实开发环境中执行多步骤操作的自主SWE智能体，出现了如SWE-bench这样的仓库级基准测试，将软件工程任务定义为需要长期、多步骤推理的端到端问题。尽管现有方法（如工具使用的ReAct式交互）已取得进展，但构建强大的开源SWE智能体仍存在三个关键不足：1）监督微调所使用的演示数据往往低效，包含冗余探索和冗长推理链，导致模型模仿噪声搜索而非高效解决问题；2）强化学习面临长期信用分配难题，因为最终执行结果提供的奖励稀疏且延迟，难以评估中间步骤的有效性，易导致策略不稳定或奖励黑客行为；3）测试时扩展方法（如采样多条完整轨迹再重排序）计算成本高昂，引入显著延迟，难以实用。

本文要解决的核心问题是：如何通过一个统一的框架，优化SWE智能体在整个生命周期（包括数据构建、强化学习和测试时推理）中的决策效率与性能。具体而言，论文提出了SWE-TRACE框架，旨在同时解决上述三个瓶颈：在监督阶段，通过创新的轨迹合成方法获取高效、最短路径的演示数据；在强化学习阶段，引入基于规则的流程奖励模型提供密集的中间步骤反馈，以克服稀疏奖励的不稳定性；在推理阶段，重用该奖励模型进行启发式引导的测试时扩展，动态评估并剪枝动作候选，从而在降低延迟的同时提升搜索效率。最终目标是使轻量级模型在有限计算预算下，在复杂的长期软件工程任务上达到先进的性能水平。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：软件工程（SWE）智能体基准与系统、可扩展训练环境与数据生成，以及强化学习与验证器优化。

在**SWE智能体基准与系统**方面，SWE-bench及其验证子集SWE-bench Verified建立了基于真实GitHub问题的评测标准。SWE-agent和OpenHands等工作开发了专门的智能体-计算机接口与可扩展平台，以提升代码库操作能力。Agentless则展示了非智能体化、结构化的任务分解流程也能取得竞争力。本文提出的SWE-TRACE框架属于此类系统优化工作，但通过集成数据蒸馏、过程奖励和测试时启发式搜索，在长程推理效率上进行了统一优化。

在**可扩展训练环境与数据生成**方面，SWE-Gym、SWE-smith和R2E-Gym等研究致力于构建可执行的训练环境和规模化合成数据管道，以解决数据与环境的瓶颈。本文的贡献与之相关，其第一步即通过多任务级联方法从验证轨迹中蒸馏出大规模、高质量的监督微调语料，直接针对数据优化问题。

在**强化学习与验证器优化**方面，早期如CodeRL研究利用批评性反馈改进程序合成。近期DeepSWE、SWE-Master等工作通过执行环境后训练和大规模测试时缩放来提升SWE智能体的长程能力。SWE-RM则强调了验证器质量（如判别与校准能力）对稳定强化学习信号的重要性。本文与此方向紧密相关，其核心创新是设计了基于量规的过程奖励模型，提供细粒度中间步骤反馈以稳定强化学习，并将该模型复用于启发式测试时缩放，从而在奖励引导和推理效率两方面进行了整合与推进。

### Q3: 论文如何解决这个问题？

论文通过一个名为SWE-TRACE的统一框架来解决长视野软件工程（SWE）智能体面临的挑战，该框架整合了数据优化、强化学习和推理优化三个核心阶段。

**整体框架与核心方法**：SWE-TRACE包含三个主要部分：1）一个旨在生成高质量、令牌高效轨迹的监督微调（SFT）数据合成管道；2）一个结合了基于准则的过程奖励模型（PRM）和记忆增强架构的强化学习（RL）框架，以提供密集的中间步骤指导；3）一种在推理时重用PRM进行启发式引导的测试时缩放（TTS）方法，以提升搜索效率。

**主要模块与关键技术**：
1.  **令牌高效的轨迹合成**：为了解决原始数据中轨迹冗余和效率低下的问题，论文设计了**LLM多任务级联**方法。该方法在每一步生成多种操作意图（如定位、检查、编辑）的候选动作，然后利用一个**基于测试的Oracle验证器**对候选动作进行逐步评估和选择。验证器根据测试状态改进、范围接近度、补丁对齐度、信息增益以及令牌成本和冗余惩罚等多个维度进行评分，贪婪地选择最优动作，从而将成功的教师轨迹压缩成最短路径风格的高质量SFT数据。同时，被拒绝的候选动作被用作结构化的困难负样本。

2.  **过程引导的智能体强化学习**：为了克服稀疏执行奖励的不稳定性，论文引入了**基于准则的过程奖励模型（PRM）**。首先，一个**准则智能体**为每个任务实例生成一个包含具体行为期望（如目标定位、编辑约束、轨迹纪律）的准则。PRM则根据整个完成后的轨迹满足这些准则的程度，输出一个轨迹级评分，从而能够区分具有相同最终结果但过程质量不同的轨迹。PRM通过从执行偏好和准则偏好对中学习来训练。在策略优化阶段，采用**组相对策略优化（GRPO）**，将稀疏的执行奖励与密集的PRM评分结合成一个复合奖励，确保成功轨迹始终优于失败轨迹，同时在每个类别内根据过程质量进行排序。此外，框架还包含一个**记忆增强架构**，当交互历史超出上下文限制时，利用PRM评分作为关键步骤检测器，选择性地保留历史中的关键步骤（如重要决策点），以维持长期推理能力。

3.  **启发式测试时缩放**：为了在推理时避免标准并行采样带来的延迟开销，论文将训练好的PRM重新用于**启发式引导的测试时缩放**。在每一步，模型动态生成多个候选动作，并使用PRM（或其轻量级版本）对这些候选进行快速评估和剪枝，只扩展最有希望的路径。这实现了高效的搜索，而无需运行完整的并行rollout。

**创新点**：
- **LLM多任务级联与Oracle验证**：通过结构化候选生成和基于隐藏元数据的逐步验证，从源头合成令牌高效的最短路径SFT数据。
- **基于准则的PRM**：利用自然语言准则将过程监督具体化，提供可解释且密集的轨迹级反馈，有效解决了稀疏奖励和信用分配难题。
- **训练与推理的桥梁**：创新性地将PRM用于推理时的启发式搜索，实现了高效的测试时决策，减少了令牌消耗和延迟。
- **记忆增强与关键步骤检测**：利用PRM智能地管理长上下文，保留对成功至关重要的精确历史步骤，而非进行可能丢失细节的摘要。

### Q4: 论文做了哪些实验？

论文在标准软件工程（SWE）基准上进行了广泛的实验。实验设置包括：1）**数据合成与SFT轨迹生成**：从超过1000个GitHub仓库中筛选出77个可执行且包含可运行测试的仓库，通过测试感知的bug合成方法生成约14万个候选bug实例，并经过四阶段严格过滤得到6万个高质量样本。利用LLM多任务级联和带oracle验证的逐步轨迹优化方法，从教师模型（如Claude和MiniMax 2.5）的成功rollout中蒸馏出token高效的SFT轨迹。2）**过程引导的强化学习**：设计了一个基于准则的过程奖励模型（PRM），该模型通过一个辅助的Rubric-Agent为每个任务生成特定于问题的准则（如目标定位、编辑约束、轨迹纪律），并为完整轨迹提供密集的、细粒度的评分。策略使用组相对策略优化（GRPO）进行训练，结合了稀疏的执行奖励和PRM提供的密集过程奖励。3）**启发式测试时缩放**：在推理阶段，复用PRM进行启发式引导的测试时缩放，通过动态评估和剪枝每个步骤的候选动作来提高搜索效率。

**数据集/基准测试**：实验在标准的SWE基准上进行，包括SWE-Gym（2,438个真实世界任务）、SWE-smith（来自114个仓库的14K合成实例）和R2E-Gym（超过4.6K个可执行任务和混合验证器）。论文构建的数据集包含从77个仓库中筛选出的6万个高质量样本。

**对比方法**：论文将SWE-TRACE与当前最先进的SWE代理系统进行比较，但具体对比模型名称在提供章节中未明确列出。

**主要结果与关键指标**：SWE-TRACE显著推进了技术水平，在最大化问题解决率的同时，大幅降低了token消耗和推理延迟。具体数据指标包括：在bug合成阶段，采用测试感知方法后，成功率从35.0%提升至50.7%（在25个仓库上，过滤后样本数从20,638增至24,995）。PRM与GRPO的结合确保了通过轨迹的奖励严格高于失败轨迹（最小奖励间隔Δ_min > 0），并在每个类别内根据过程质量进行区分。整体上，框架在搜索效率和轨迹质量上均表现出优越性。

### Q5: 有什么可以进一步探索的点？

本文提出的SWE-TRACE框架在数据优化、过程奖励和推理扩展方面做出了显著贡献，但仍存在一些局限性和值得深入探索的方向。

首先，其核心组件“基于量规的过程奖励模型（PRM）”依赖于一个辅助的Rubric-Agent提供密集反馈。这个Rubric-Agent本身的判断准确性、泛化能力以及对复杂、模糊或边缘性代码变更的评估鲁棒性，尚未得到充分验证。未来研究可以探索如何量化该代理的可靠性，或设计多专家投票、不确定性校准等机制来提升其稳定性。

其次，启发式测试时扩展（TTS）方法在动态剪枝行动候选时，所依赖的启发式函数可能过于简化。当前方法可能无法充分捕捉到那些看似短期低效、但长期必要的探索性步骤（例如，为了理解复杂依赖而进行的额外代码阅读）。未来可以研究更复杂的、基于价值预测的剪枝策略，或者在剪枝时引入一定的随机性以保持探索能力。

此外，框架整体在“长周期推理”上的优化仍集中于单任务轨迹。软件工程实践中经常涉及多个相互关联的Issue或需要跨任务的知识迁移。一个重要的拓展方向是研究如何在智能体架构中引入外部记忆或知识库，使其能够积累和复用跨项目的经验，实现持续学习，从而应对更宏大的软件维护场景。

最后，从工程实践角度看，该框架的训练和部署成本依然较高。探索更轻量级的PRM模型（如基于小型专家模型），或研究如何将TTS的高效搜索能力蒸馏到一个更小的策略模型中，对于推动其在真实开发环境中的落地应用具有重要意义。

### Q6: 总结一下论文的主要内容

本文提出SWE-TRACE框架，旨在优化解决现实世界软件工程问题的自主智能体在长周期推理中的性能。核心问题是现有方法存在数据低效、奖励稀疏和推理扩展计算成本高三大瓶颈，导致令牌膨胀、奖励破解和策略退化。为解决这些问题，论文贡献了一个统一框架，覆盖数据整理、强化学习和测试时推理全流程。方法上，首先通过LLM多任务级联与逐步验证，从14万候选样本中蒸馏出6万条偏向最短路径的高效监督微调轨迹数据。其次，设计了基于记忆增强的智能体强化学习流程，引入基于量规的过程奖励模型，通过辅助的Rubric-Agent提供细粒度中间步骤反馈，以缓解稀疏结果奖励的不稳定性。最后，创新性地将过程奖励模型复用于启发式引导的测试时扩展，在推理时动态评估并剪枝每一步的动作候选，从而在无需标准并行采样的延迟开销下实现更优的搜索效率。主要结论表明，SWE-TRACE显著提升了在SWE-bench等标准基准上的解决率，同时大幅降低了令牌消耗和推理延迟，使轻量级模型也能达到与大型前沿系统竞争的性能，这为提升智能体效能指明了优化全生命周期决策过程的新方向。
