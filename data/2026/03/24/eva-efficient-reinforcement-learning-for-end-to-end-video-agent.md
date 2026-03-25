---
title: "EVA: Efficient Reinforcement Learning for End-to-End Video Agent"
authors:
  - "Yaolun Zhang"
  - "Ruohui Wang"
  - "Jiahao Wang"
  - "Yepeng Tang"
  - "Xuanyu Zheng"
  - "Haonan Duan"
  - "Hao Lu"
  - "Hanming Deng"
  - "Lewei Lu"
date: "2026-03-24"
arxiv_id: "2603.22918"
arxiv_url: "https://arxiv.org/abs/2603.22918"
pdf_url: "https://arxiv.org/pdf/2603.22918v1"
github_url: "https://github.com/wangruohui/EfficientVideoAgent"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Video Agent"
  - "Reinforcement Learning"
  - "Planning-Before-Perception"
  - "Efficient Video Understanding"
  - "Tool Use"
  - "Reasoning"
  - "MLLM"
  - "End-to-End Training"
relevance_score: 7.5
---

# EVA: Efficient Reinforcement Learning for End-to-End Video Agent

## 原始摘要

Video understanding with multimodal large language models (MLLMs) remains challenging due to the long token sequences of videos, which contain extensive temporal dependencies and redundant frames. Existing approaches typically treat MLLMs as passive recognizers, processing entire videos or uniformly sampled frames without adaptive reasoning. Recent agent-based methods introduce external tools, yet still depend on manually designed workflows and perception-first strategies, resulting in inefficiency on long videos. We present EVA, an Efficient Reinforcement Learning framework for End-to-End Video Agent, which enables planning-before-perception through iterative summary-plan-action-reflection reasoning. EVA autonomously decides what to watch, when to watch, and how to watch, achieving query-driven and efficient video understanding. To train such agents, we design a simple yet effective three-stage learning pipeline - comprising supervised fine-tuning (SFT), Kahneman-Tversky Optimization (KTO), and Generalized Reward Policy Optimization (GRPO) - that bridges supervised imitation and reinforcement learning. We further construct high-quality datasets for each stage, supporting stable and reproducible training. We evaluate EVA on six video understanding benchmarks, demonstrating its comprehensive capabilities. Compared with existing baselines, EVA achieves a substantial improvement of 6-12% over general MLLM baselines and a further 1-3% gain over prior adaptive agent methods. Our code and model are available at https://github.com/wangruohui/EfficientVideoAgent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于多模态大语言模型（MLLM）的长视频理解任务中存在的效率低下和适应性不足的问题。研究背景是，视频理解作为多模态智能的核心应用，正从传统的被动感知模型向主动智能体范式演进。然而，现有方法存在显著不足：传统方法通常将MLLM视为被动识别器，要么处理整个视频，要么对帧进行均匀采样，缺乏对视频中长时依赖和冗余帧的自适应处理能力，导致在极长视频中关键信息可能被遗漏或计算资源浪费。近期基于智能体的方法虽然引入了外部工具（如帧选择模块），但其工作流程往往是手动设计的、感知先行的（即先输入一组采样帧再推理），且工具调用参数（如采样率）固定，缺乏灵活性和探索能力，在长视频上依然效率不高。

本文要解决的核心问题是：如何让一个基于MLLM的视频智能体能够自主、高效、自适应地进行视频理解，即自主决定“看什么、何时看、如何看”。为此，论文提出了EVA框架，其核心是“规划先于感知”的范式，通过迭代的“总结-规划-行动-反思”推理循环，使智能体仅基于文本查询就能主动规划视觉信息的获取策略，从而实现对长视频的查询驱动、高效理解。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：视频理解智能体方法以及工具集成推理训练方法。

在**视频理解智能体方法**方面，现有工作主要利用外部工具来辅助理解。一类方法（如Ego-R1、M3-Agent）依赖调用外部MLLM API或传统视觉模型来提升视觉理解能力，其性能很大程度上受限于所调用工具的性能，而非基础模型自身的多模态能力。另一类方法则为MLLM配备采样工具，以从视频中提取部分或时序视觉信息。这些方法虽然利用了智能体的规划与识别能力，但仍将MLLM视为固定工作流中的一个被动组件，仅能沿单一控制维度（如采样哪些帧）生成预定参数。本文提出的EVA框架与这些工作的核心区别在于，它赋予了智能体真正的自主性，使其不仅能决定观察视频的哪些部分（“看什么”），还能灵活控制如何观察（如空间分辨率和时间粒度），实现了基于查询的自适应、高效理解。

在**工具集成推理训练方法**方面，近期研究致力于将工具调用集成到大语言模型的推理过程中，并通过强化学习进行优化，以生成和优化复杂工作流。本文的工作与此类研究思路一脉相承，但具体贡献在于，我们设计了一个专门针对视频理解智能体的三阶段训练流程（SFT、KTO、GRPO），并构建了对应的高质量数据集，以稳定、可复现地训练智能体进行迭代式的规划、信息帧选择和反思。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EVA的端到端强化学习框架来解决视频理解中因长序列、冗余帧和固定工作流导致的效率低下问题。其核心方法是让智能体自主决策“看什么、何时看、如何看”，实现查询驱动的高效视频理解。

整体框架基于马尔可夫决策过程（MDP）建模。在每个时间步，智能体观察一个信念状态，包括用户查询、历史文本-帧序列以及通过工具调用获取的视觉证据。策略由参数化的策略网络决定。EVA的关键创新在于其“总结-规划-行动-反思”的迭代推理循环。初始时，模型仅接收查询，而无任何视觉信息，从而避免无关视觉线索对规划的误导。为此，论文设计了一个灵活的帧选择工具，允许时域和空域控制，参数包括时间窗口起止、采样帧数和空间下采样比例，为智能体提供了广阔的探索空间以学习如何跨轮次分配时空信息来获取精确答案。

训练这样的端到端自主视频智能体需要高质量数据和高效训练策略。论文设计了一个三阶段学习流程：
1.  **监督微调（SFT）阶段**：使用教师大模型（Qwen2.5-VL-72B）生成高质量的智能体视频理解数据。数据实例遵循“总结+规划+行动+反思”格式，旨在让模型学习工具调用格式、推理模式，并训练其基于当前信息规划行动、评估成本与结果的能力，以及在答案生成前反思视觉证据是否充足。
2.  **卡尼曼-特沃斯基优化（KTO）阶段**：针对SFT模型仍存在的典型失败模式（如证据不足即作答、采样帧数分布不合理），采用KTO框架进行优化。KTO仅需单样本偏好标签（“采纳”或“拒绝”），通过收集失败轨迹作为拒绝样本，并重采样高质量成功轨迹作为采纳样本，让模型从外部收集的经验中学习细粒度偏好，稳定后续在线强化学习。
3.  **广义奖励策略优化（GRPO）阶段**：这是一个在线强化学习框架，模型通过自我生成多个轨迹（rollouts）并从成功与失败中迭代学习。为解决传统GRPO依赖静态数据集、挑战多样性受限的问题，论文引入了**数据增强的GRPO管道**：收集KTO后模型的失败案例，将其作为上下文示例，引导教师大模型为未见视频生成新的开放式问答对，从而动态扩展和增强训练数据集。

在GRPO优化中，采用混合格式数据集（多项选择和开放式问题）和复合奖励函数。奖励包括准确率奖励（针对多项选择题使用完备性自验证奖励，针对开放式问题使用ROUGE分数）和格式奖励（防止模型不经过当推理直接猜测答案）。优化目标在最大化期望回报的同时，通过KL散度正则约束策略不偏离经过SFT和KTO初始化的参考模型。

主要创新点包括：1）提出“规划先于感知”的自主视频理解范式，通过灵活的工具设计支持时域和空域自适应控制；2）设计了三阶段训练流程，有效衔接监督模仿与强化学习，特别是数据增强的GRPO管道缓解了训练数据多样性瓶颈；3）构建了高质量、分阶段的数据集以支持稳定、可复现的训练。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估，主要涵盖以下方面：

**实验设置**：以Qwen2.5-VL-7B-Instruct为基础模型，采用三阶段训练流程：首先使用EVA-SFT数据进行监督微调（SFT），随后使用EVA-KTO数据进行Kahneman-Tversky优化（KTO），最后使用EVA-RL数据进行广义奖励策略优化（GRPO）。GRPO阶段结合了多项选择题（MCQ）和开放式问答（90% vs 10%），奖励函数根据问题类型设计（MCQ看正确性，开放式问答使用ROUGE分数）。训练在32张H100 GPU上进行。

**数据集/基准测试**：在六个视频理解基准上评估模型性能：LSDBench（采样困境基准）、LongVideoBench、MLVU、VideoMME、LVBench（长视频理解）以及Video-Holmes（零样本视频推理）。评估指标均为准确率（Accuracy）。

**对比方法**：与多种基线模型进行比较，包括闭源模型（如GPT-4o、Gemini系列）、开源静态帧采样模型（如Qwen2.5-VL、Video-R1、LongVA）以及自适应智能体方法（如VideoAgent、FrameThinker、VideoMTR）。

**主要结果与关键指标**：
1.  **采样效率与准确性（LSDBench）**：EVA仅使用约6.2K视觉令牌，取得了51.8%的准确率，相比基础模型Qwen2.5-VL（使用166.4K令牌，准确率50.1%）在显著减少令牌使用量的同时，准确率提升了2.6%。
2.  **长视频理解**：在四个长视频基准上，EVA（GRPO版本）取得了有竞争力的结果：LongVideoBench（55.0%）、MLVU（68.3%）、VideoMME-Long/Overall（48.4%/60.2%）、LVBench（43.3%），通常仅处理每视频约20-30帧，超越了大多数开源和自适应智能体基线。
3.  **零样本推理（Video-Holmes）**：EVA-GRPO在零样本设置下取得了37.2%的整体准确率，与采用均匀采样帧的顶级开源模型（如Video-R1的36.5%）性能相当，展示了其强大的泛化与推理能力。
4.  **训练策略消融**：实验验证了三阶段训练（SFT→KTO→GRPO）的有效性。GRPO模型在消耗最少帧数的同时，取得了所有基准上的最高性能，表明其学会了更精准、多轮次的战略性视觉探索。
5.  **效率优势**：尽管进行多轮规划与感知，EVA的总令牌消耗与静态均匀采样基线相当甚至更低，文本令牌仅占计算预算的一小部分，推理时间主要取决于自适应选择的少量视觉令牌，实现了高效的视频理解。

### Q5: 有什么可以进一步探索的点？

该论文提出的EVA框架在自适应视频理解方面取得了显著进展，但其仍有若干局限性值得深入探索。首先，其“摘要-计划-行动-反思”的推理循环虽然高效，但可能对计算资源要求较高，未来可研究更轻量化的循环机制或引入早期终止策略以进一步提升效率。其次，当前训练依赖于构建的高质量多阶段数据集，其可扩展性和泛化能力有待验证；未来可探索如何利用更弱监督或自监督数据，或研究跨任务、跨领域的迁移学习方案。此外，框架的决策透明度不足，其内部规划过程的逻辑难以解释，未来可结合可解释AI技术，使智能体的“观看决策”更具可信度。从方法融合角度看，将EVA的主动感知机制与更强大的世界模型或物理常识模型结合，可能使其对视频中复杂时空关系和因果逻辑的理解更为深刻。最后，评估目前集中于标准基准，未来需在更开放、动态的真实世界长视频流中测试其鲁棒性与实用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为EVA的高效强化学习框架，旨在解决基于多模态大语言模型的视频理解中存在的挑战，即视频序列长、包含大量时间依赖和冗余帧的问题。现有方法通常将MLLMs视为被动识别器，处理整个视频或均匀采样帧，缺乏自适应推理能力；而近期基于智能体的方法虽然引入了外部工具，但仍依赖人工设计的工作流程和“先感知后规划”的策略，导致处理长视频效率低下。

EVA的核心贡献在于提出了一种“规划先于感知”的迭代式“总结-规划-行动-反思”推理框架，使智能体能够自主决定观看内容、时机和方式，实现查询驱动的高效视频理解。方法上，论文设计了一个简单有效的三阶段训练流程：首先进行监督微调，接着使用Kahneman-Tversky优化来对齐人类偏好，最后通过广义奖励策略优化进行强化学习，从而桥接了监督模仿与强化学习。此外，研究还为每个阶段构建了高质量数据集，以支持稳定、可复现的训练。

实验在六个视频理解基准上进行，结果表明EVA具备全面的能力。与现有基线相比，EVA相比通用MLLM基线取得了6-12%的显著提升，相比先前的自适应智能体方法也有1-3%的进一步增益。该工作为开发高效、自主的视频理解智能体提供了新的思路和可复现的实践路径。
