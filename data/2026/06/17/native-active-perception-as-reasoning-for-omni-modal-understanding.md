---
title: "Native Active Perception as Reasoning for Omni-Modal Understanding"
authors:
  - "Zhenghao Xing"
  - "Ruiyang Xu"
  - "Yuxuan Wang"
  - "Jinzheng He"
  - "Ziyang Ma"
  - "Qize Yang"
  - "Yunfei Chu"
  - "Jin Xu"
  - "Junyang Lin"
  - "Chi-Wing Fu"
  - "Pheng-Ann Heng"
date: "2026-06-17"
arxiv_id: "2606.19341"
arxiv_url: "https://arxiv.org/abs/2606.19341"
pdf_url: "https://arxiv.org/pdf/2606.19341v1"
github_url: "https://github.com/harryhsing/omniagent"
categories:
  - "cs.CV"
  - "cs.CL"
  - "cs.SD"
tags:
  - "视频理解Agent"
  - "主动感知"
  - "POMDP推理"
  - "Agentic SFT"
  - "Agentic RL"
  - "测试时扩展"
  - "多模态Agent"
  - "长期视频理解"
relevance_score: 9.5
---

# Native Active Perception as Reasoning for Omni-Modal Understanding

## 原始摘要

Passive models for long video understanding typically rely on a "watch-it-all" paradigm, processing frames uniformly regardless of query difficulty, causing computational cost to grow with video duration. Although interactive frameworks have emerged, they often rely on global pre-scanning, and their context cost still scales with video length. We propose OmniAgent, the first native omni-modal agent that formulates video understanding as a POMDP-based iterative Observation-Thought-Action cycle. OmniAgent executes on-demand actions to selectively distill audio-visual cues into a persistent textual memory, effectively decoupling reasoning complexity from raw video duration. To operationalize this, we introduce (1) Agentic Supervised Fine-Tuning to bootstrap native active perception via best-of-N trajectory synthesis with dual-stage quality control, and (2) Agentic Reinforcement Learning with TAURA (Turn-aware Adaptive Uncertainty Rescaled Advantage), which leverages turn-level entropy to steer credit assignment toward pivotal discovery turns. Crucially, OmniAgent exhibits positive test-time scaling, where performance improves as the number of reasoning turns increases, validating the efficacy of active perception. Empirical results across ten benchmarks (e.g., VideoMME, LVBench) demonstrate that OmniAgent achieves state-of-the-art performance among open-source models. Notably, on LVBench, our 7B agent outperforms the 10$\times$ larger Qwen2.5-VL-72B (50.5% vs. 47.3%).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视频理解中计算成本高、推理效率低下的核心问题。研究背景方面，现有被动模型采用“全量观看”范式，无论查询难易，均需统一处理所有视频帧，导致计算成本随视频时长呈超线性增长，处理长视频在计算上变得不可行。现有方法的不足主要体现在两方面：一是基于代理的框架，它们通常依赖LLM作为控制器调用外部工具，但中间模块造成了信息瓶颈，割裂了推理与感知之间的梯度流；二是“带图像思考”的方法，它们虽然引入了时间裁剪、空间缩放等工具，但往往仍保留半被动特性，需要对视频进行全局预扫描或维持密集的视觉缓冲来决定“看向哪里”，未能真正将推理复杂度与视频时长解耦，导致难以处理长达数小时的视频。因此，本文要解决的核心问题是：如何设计一种原生主动感知的智能体，使其能够像系统-2推理一样，根据用户查询的难度，主动、按需地选择性地从视频中提取音频-视觉线索，并通过将高维瞬时感知蒸馏为持久文本记忆的方式，使得智能体的内部状态仅取决于推理轨迹的复杂性，而非原始视频的时长，从而在长视频理解中实现计算开销与视频时长的真正解耦，并展现出正向的测试时缩放特性。

### Q2: 有哪些相关研究？

在相关研究中，作者将现有工作分为两条主线：一是基于LLM编排专家模块的方法（如VisProg），这类方法依赖预先提取的上下文（如字幕、摘要）或结构化规划，常借助跟踪、ASR、搜索和集成工具；二是将“结合图像思考”范式扩展到视频的方法，通过时间裁剪、空间缩放或组合裁剪等变换进行穷举分析。本文指出，这两种方法都忽略了视频固有的时序特性，将其视为静态信息容器或大图像，阻碍了可扩展性。

与这些方法不同，作者提出OmniAgent，将视频理解建模为部分可观测马尔可夫决策过程（POMDP），为多模态大语言模型注入原生主动感知能力。本文的创新在于：通过Agentic监督微调和基于回合级熵的强化学习（TAURA），实现按需的观察-思考-行动迭代循环，从而将推理复杂度与原始视频长度解耦。与需要全局预扫描或固定上下文预提取的现有工作相比，OmniAgent展现了正向测试时扩展特性，即在无外部模块依赖下，随推理轮次增加性能持续提升，这从根本上区别于依赖外部工具或静态上下文的传统方法。

### Q3: 论文如何解决这个问题？

OmniAgent将视频理解重构为基于POMDP的迭代"观察-思考-行动"（OTA）循环，将主动感知视为查询驱动的推理过程。其核心架构包含三个组件：1）**持久化文本记忆**：通过周期性丢弃原始高维媒体数据，将关键视听线索蒸馏为结构化文本摘要，使推理成本与视频时长解耦；2）**三元组动作空间**：包括帧提取(`a_frames`)、音频段截取(`a_audio`)、连续片段捕获(`a_clip`)和终止回答(`a_answer`)，环境根据动作返回新的瞬态感知；3）**记忆整合机制**：每次行动后仅保留文本观察，保证媒体开销恒定。

创新点体现在两个训练阶段：**Agentic SFT**通过最佳-N轨迹合成和双阶段质量控制（结果正确性验证+GPT-4o理性审计），从58K探索轨迹中引导基础行动能力；**Agentic RL**提出TAURA算法，利用轮级熵对优势函数进行自适应重缩放，解决多轮推理中优势同质化问题——高熵关键探索轮获得放大优势，低熵填充轮获得抑制，从而精确分配信用。最终OmniAgent展现出正向测试时扩展性：随着推理轮次增加，性能持续提升。

### Q4: 论文做了哪些实验？

论文在10个基准上进行了三大类实验评估：(1) 视频理解与推理：VideoMME、VSI-Bench、MLVU、Minerva、LVBench（时长从数十秒到两小时以上）；(2) 音视频理解：DailyOmni、WorldSense、OmniVideoBench；(3) 时间定位：LongVALE、VUE-TR。采用Qwen2.5-Omni-7B为基础模型，进行两阶段训练：Agentic SFT（58K轨迹，2轮，学习率1e-5，16张A100）和Agentic RL（仅困难查询，最大10轮，DAPO策略，64张A100）。主要结果：OmniAgent-7B在LVBench上达50.5%，超越10倍大的Qwen2.5-VL-72B（47.3%）；在MLVU上达71.1%，高于Video-R1（60.9%）；在VideoMME和MLVU上分别比被动基线LongVU高7.2%和5.7%。音视频任务上，比Qwen2.5-Omni在DailyOmni和OmniVideoBench上分别提升4.7%和7.8%。时间定位上，在LongVALE和VUE-TR上分别提升33.4%和33.0%，并超越GPT-4o等专有模型。消融实验显示：Agentic SFT优于标准SFT，TAURA比Vanilla GRPO在MLVU（71.1% vs 69.9%）和DailyOmni（64.8% vs 62.2%）上更优。测试时缩放分析表明，随推理轮次增加准确率单调提升（+6.2%），且实际执行轮次趋于饱和（约11.7轮），验证了计算成本由任务复杂度而非视频时长驱动。

### Q5: 有什么可以进一步探索的点？

首先，OmniAgent的POMDP框架在复杂长视频上可能面临状态表示和搜索空间爆炸问题，尤其是当动作空间（如音频、视觉模态选择）增大时。未来可探索分层或抽象化的状态空间压缩方法，或引入记忆衰减机制来减轻历史依赖性。其次，当前奖励设计依赖动作后的事实性正确性，但未考虑发现新信息的“好奇心”奖励。可结合内在动机，如信息增益或熵减，鼓励探索性动作。此外，TAURA中的熵估计在极端长视频中可能不稳定，可采用对比学习或动态窗口调整。OmniAgent的文本记忆可能丢失细粒度视觉/音频线索，未来可引入跨模态检索增强生成，或使用轻量级视觉token记忆。最后，其“正测试时缩放”受限于推理步数，可研究自适应终止策略（如基于置信度或困惑度）以平衡计算与精度。总体而言，将感知推理与强化学习进一步融合，并扩展至更开放的交互环境（如联网查询）值得探索。

### Q6: 总结一下论文的主要内容

本论文提出OmniAgent，首个将视频理解建模为基于POMDP的“观察-思考-行动”迭代循环的原生全模态智能体。核心贡献在于：(1)将主动感知形式化为推理过程，通过按需执行动作选择性提取视听线索并蒸馏为持久文本记忆，从而使推理复杂度与视频时长解耦；(2)提出两阶段智能体优化：Agentic SFT通过最佳N轨迹合成与双阶段质量控制引导主动感知，TAURA强化学习利用轮次级熵解决GRPO中优势同质化问题，精准分配关键探索回合的信用。实验表明，OmniAgent在10个基准上达到开源最优，例如在LVBench上，7B模型以73%更少帧数超越10倍大的Qwen2.5-VL-72B（50.5% vs 47.3%），并展现出正向测试时扩展特性。该工作首次实现了单模型内原生的主动感知与推理统一，为长视频理解提供了可扩展的新范式。
