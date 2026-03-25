---
title: "SortedRL: Accelerating RL Training for LLMs through Online Length-Aware Scheduling"
authors:
  - "Yiqi Zhang"
  - "Huiqiang Jiang"
  - "Xufang Luo"
  - "Zhihe Yang"
  - "Chengruidong Zhang"
  - "Yifei Shen"
  - "Dongsheng Li"
  - "Yuqing Yang"
  - "Lili Qiu"
  - "Yang You"
date: "2026-03-24"
arxiv_id: "2603.23414"
arxiv_url: "https://arxiv.org/abs/2603.23414"
pdf_url: "https://arxiv.org/pdf/2603.23414v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习训练"
  - "训练效率"
  - "调度策略"
  - "长序列生成"
  - "推理能力"
  - "基础设施"
relevance_score: 7.5
---

# SortedRL: Accelerating RL Training for LLMs through Online Length-Aware Scheduling

## 原始摘要

Scaling reinforcement learning (RL) has shown strong promise for enhancing the reasoning abilities of large language models (LLMs), particularly in tasks requiring long chain-of-thought generation. However, RL training efficiency is often bottlenecked by the rollout phase, which can account for up to 70% of total training time when generating long trajectories (e.g., 16k tokens), due to slow autoregressive generation and synchronization overhead between rollout and policy updates. We propose SortedRL, an online length-aware scheduling strategy designed to address this bottleneck by improving rollout efficiency and maintaining training stability. SortedRL reorders rollout samples based on output lengths, prioritizing short samples forming groups for early updates. This enables large rollout batches, flexible update batches, and near on-policy micro-curriculum construction simultaneously. To further accelerate the pipeline, SortedRL incorporates a mechanism to control the degree of off-policy training through a cache-based mechanism, and is supported by a dedicated RL infrastructure that manages rollout and update via a stateful controller and rollout buffer. Experiments using LLaMA-3.1-8B and Qwen-2.5-32B on diverse tasks, including logical puzzles, and math challenges like AIME 24, Math 500, and Minerval, show that SortedRL reduces RL training bubble ratios by over 50%, while attaining 3.9% to 18.4% superior performance over baseline given same amount of data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习（RL）的大语言模型（LLMs）训练中，因生成长轨迹（如长思维链）而导致的效率瓶颈问题。研究背景是，RL已被证明能有效提升LLMs在复杂推理任务（如数学解题）上的能力，其训练通常交替进行“生成”（rollout）和“更新”两步。然而，现有方法存在明显不足：首先，由于LLM的自回归生成特性，生成长轨迹极其耗时，在总训练时间中占比可高达70%，成为主要瓶颈；其次，常用的RL算法（如PPO）是在线策略的，要求生成完成后才能开始更新，而批次内样本的生成长度差异巨大（呈长尾分布），导致GPU必须等待最长的生成完成，产生大量资源闲置的“气泡”（bubble），利用率低下。虽然增大生成批次并采用持续批处理等技术可缓解此问题，但这会带来新的矛盾：若固定更新批次大小，模型会对同一批生成数据多次更新，导致训练数据逐渐偏离当前策略（off-policy），损害训练稳定性；若强制更新批次与生成批次一致，则缺乏灵活性，可能影响效果。

因此，本文要解决的核心问题是：如何在不牺牲训练稳定性和策略一致性的前提下，显著加速RL训练中的生成阶段，减少气泡，提高整体计算效率。为此，论文提出了SortedRL方法，其核心是通过在线长度感知调度、控制离策略程度的机制以及专用基础设施，来协同优化样本效率和计算效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**RLHF训练框架**和**高效推理服务系统**。

在**RLHF训练框架**方面，相关工作包括算法库（如TRL、RL4LMs）和面向吞吐量的分布式系统（如ColossalChat、DeepSpeed-Chat、NeMo-Aligner）。最新的框架如OpenRLHF和VeRL/HybridFlow进一步简化了流程并支持异构硬件并行。然而，这些现有框架均未提供**在线批次调度**和**细粒度的rollout控制**，而这正是SortedRL所引入的核心能力。

在**高效推理服务系统**方面，现代RLHF的rollout阶段常依托于高性能LLM服务栈，例如使用vLLM的PagedAttention或SGLang的RadixAttention来优化KV缓存访问。这些系统集成了连续批处理、推测解码等优化技术，但其设计目标主要是针对**权重冻结、低延迟的在线推理**。这与RLHF训练中权重频繁更新、需要高吞吐量“半离线”生成的场景存在根本差异，后者会导致缓存失效、产生训练“气泡”。SortedRL正是针对这一特定瓶颈，通过在线长度感知调度来缩小气泡、提升吞吐量，从而弥补了现有推理系统与RL训练需求之间的差距。

### Q3: 论文如何解决这个问题？

论文通过提出SortedRL这一在线长度感知调度策略来解决强化学习训练中因长轨迹生成导致的效率瓶颈问题。其核心方法围绕三个关键组件展开：在线长度感知调度、可控离策略采样以及协同设计的强化学习基础设施。

整体框架由两个核心模块构成：长度感知控制器和状态化经验回放缓冲区。控制器负责动态管理提示词输入、调度生成过程并实施早期终止策略；缓冲区则存储部分生成的轨迹及其对数概率等中间状态，支持轨迹的恢复与复用。训练流程主要包含四个步骤：1）拼接缓冲区内容并输入提示词；2）基于批次相关阈值实施早期终止，收集已完成或部分生成的输出；3）收集并更新轨迹数据；4）对训练批次进行排序并送入训练器。

在具体设计上，首先，**在线长度感知调度**通过感知生成序列的细粒度动态，采用“超额订阅”策略，向生成引擎提供超过其队列容量的提示词，确保引擎始终以硬件运行时图确定的最优批次大小运行，从而最大化设备利用率。结合早期终止机制，一旦满足条件（如生成了足够数量的令牌），便收割输出，有效减少了计算空泡。

其次，**分组式经验收集与微课程构建**将提示词分组处理，并实施缓存感知的加载策略：在缓存的所有提示词被消耗完之前，不从数据加载器加载新提示词。这确保了所有提示词在有限时间内被完全处理，避免了提示词“饥饿”。由于短响应通常更早完成，输出在时间片上自然按长度聚类，形成了按长度排序的批次。考虑到推理模型中长度与奖励的相关性，这些批次自然地构建了难度递增的“微课程”，有利于训练。

最后，**可控离策略采样与选择性批次训练**提供了完全在线策略和部分离策略两种可切换模式。在部分模式下，被中断轨迹的生成令牌及其对数概率会被缓存。在后续批次中，这些中断的轨迹（提示词和已生成令牌）会被重新送入生成引擎，并将新旧对数概率拼接，以确保重要性采样时每个令牌都能使用其生成时的精确概率值。这通过缓存机制控制了离策略训练的程度，在稳定性和样本效率之间取得了灵活平衡。

创新点在于：1）首次将在线长度感知调度与早期终止结合，显著降低了生成阶段的空泡比；2）通过分组策略和缓存机制，在提升硬件效率的同时，自然地构建了有利于训练的微课程，并实现了可控的离策略训练；3）协同设计了专用的强化学习基础设施，以状态化管理支持上述复杂调度和缓冲逻辑，实现了高效的流水线协调。

### Q4: 论文做了哪些实验？

论文在逻辑推理和数学解题两类任务上进行了实验。实验设置方面，使用VeRL开源框架和SGLang作为生成引擎，在配备H100/MI300X GPU的集群上运行。数据集包括：1）LogicRL，包含5000个“骑士与无赖”逻辑谜题，按角色数（3-7）划分难度，各1000样本，训练时打乱并留10%评估；2）DAPO-Math-17k，来自AoPS的多样化数学问题集，评估时使用GSM8K、MATH500、Minerva Math、OlympiadBench、AIME 2024和AMC 2023六个基准。模型选用LLaMA-3.1-8B-Instruct处理逻辑任务，Qwen-2.5-32B处理数学任务。

对比方法为传统RL训练流程（基线）。在逻辑任务中，基线使用Reinforce++，设置提示批量大小128、每提示8个响应、更新批量1024轨迹；数学任务基线使用PPO，对应参数为512、1和128。SortedRL则引入在线长度感知调度，通过按输出长度排序样本、分组更新来加速。

主要结果显示：1）效率提升：在最大生成长度8k、批量512的设置下，SortedRL的完全在线模式和部分模式相比基线分别提升吞吐量7.57%和39.48%（达4289和5559令牌/秒），训练气泡比从74%降至5.81%和3.37%。2）性能表现：在逻辑任务中，SortedRL（在线模式）比基线提前约150步开始探索长响应，达到相同评估分数（如2分）时节省约3轮训练；在数学任务中，训练600步后，SortedRL在线模式在AIME24上准确率达23.33%（均值@32），优于部分模式（20.83%）和基线（19.69%）。其他基准如MATH500（79.20% vs 76.2%）、Minerva（30.88% vs 29.04%）也显示类似趋势，但GSM8K上基线略优（95.15% vs 91.96%）。消融实验验证了分组设计和组大小超参数的重要性，极端设置（如过大组大小）会导致性能下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的SortedRL方法在提升RL训练效率方面成效显著，但仍有进一步探索的空间。其局限性在于：首先，方法主要针对输出长度差异大的任务优化，对于长度分布均匀或动态范围未知的任务，其排序调度的优势可能减弱；其次，缓存机制虽控制离策略程度，但如何动态调整缓存策略以平衡新旧数据，避免策略滞后或过拟合，仍需更精细的理论与实证指导。

未来研究方向可包括：一是将长度感知扩展为更通用的“难度感知”调度，依据推理复杂度、不确定性等指标动态排序样本，构建更智能的课程学习；二是探索异步化与动态批处理的更深层次结合，在分布式环境中实现弹性资源分配，进一步压缩训练气泡；三是研究排序策略与不同RL算法（如PPO、DPO）的适配性，验证其在多模态或代码生成等长序列任务中的泛化能力。

结合个人见解，可能的改进思路有：引入元学习优化调度器参数，使其能在线适应不同任务的数据流；或结合模型早期预测的生成长度置信度，实现前瞻性调度，减少排序开销。这些方向有望推动RL训练框架向更高效、更通用的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型强化学习训练中因长轨迹生成导致的效率瓶颈问题，提出了SortedRL这一在线长度感知调度策略。核心问题是RL训练中rollout阶段因自回归生成慢和同步开销大，占据了高达70%的训练时间，严重制约了训练效率。

方法上，SortedRL通过根据输出长度对rollout样本进行在线重排序，优先处理短样本并分组进行早期策略更新。这种方法同时实现了大rollout批次、灵活更新批次以及近似在策略的微课程构建。为进一步加速，该方法还引入了基于缓存的机制来控制离策略训练的程度，并得到专用RL基础设施的支持，通过有状态控制器和rollout缓冲区来管理流程。

主要结论是，在多个逻辑谜题和数学挑战任务上的实验表明，SortedRL能将RL训练气泡比降低50%以上，并在相同数据量下获得比基线模型高出3.9%到18.4%的性能。其核心贡献在于显著提升了LLM在需要长链推理任务上的RL训练效率，为扩展RL训练提供了有效的系统级解决方案。
