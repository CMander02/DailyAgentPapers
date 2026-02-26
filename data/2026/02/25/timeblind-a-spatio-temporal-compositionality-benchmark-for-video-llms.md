---
title: "TimeBlind: A Spatio-Temporal Compositionality Benchmark for Video LLMs"
authors:
  - "Baiqi Li"
  - "Kangyi Zhao"
  - "Ce Zhang"
  - "Chancharik Mitra"
  - "Jean de Dieu Nyandwi"
  - "Gedas Bertasius"
date: "2026-01-30"
arxiv_id: "2602.00288"
arxiv_url: "https://arxiv.org/abs/2602.00288"
pdf_url: "https://arxiv.org/pdf/2602.00288v3"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "视频理解"
  - "多模态大语言模型"
  - "基准评测"
  - "时空推理"
  - "具身AI"
  - "模型诊断"
relevance_score: 7.5
---

# TimeBlind: A Spatio-Temporal Compositionality Benchmark for Video LLMs

## 原始摘要

Fine-grained spatio-temporal understanding is essential for video reasoning and embodied AI. Yet, while Multimodal Large Language Models (MLLMs) master static semantics, their grasp of temporal dynamics remains brittle. We present TimeBlind, a diagnostic benchmark for compositional spatio-temporal understanding. Inspired by cognitive science, TimeBlind categorizes fine-grained temporal understanding into three levels: recognizing atomic events, characterizing event properties, and reasoning about event interdependencies. Unlike benchmarks that conflate recognition with temporal reasoning, TimeBlind leverages a minimal-pairs paradigm: video pairs share identical static visual content but differ solely in temporal structure, utilizing complementary questions to neutralize language priors. Evaluating over 20 state-of-the-art MLLMs (e.g., GPT-5, Gemini 3 Pro) on 600 curated instances (2400 video-question pairs), reveals that the Instance Accuracy (correctly distinguishing both videos in a pair) of the best performing MLLM is only 48.2%, far below the human performance (98.2%). These results demonstrate that even frontier models rely heavily on static visual shortcuts rather than genuine temporal logic, positioning TimeBlind as a vital diagnostic tool for next-generation video understanding. Dataset and code are available at https://baiqi-li.github.io/timeblind_project/ .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在视频理解中缺乏真正时空组合推理能力的问题。研究背景是，细粒度的时空理解对于视频推理和具身AI至关重要，尽管现有的MLLMs在静态语义理解上表现出色，但其对时间动态的把握仍然薄弱。现有方法的不足在于，当前的视频评测基准通常未能将时间结构作为唯一的判别因素，导致模型可以依赖“静态捷径”——即通过视觉实体与答案的关联来猜测，而非真正建模时间动态；同时，语言先验也让模型可能根据文本合理性进行猜测，从而高估了模型的真实时序理解能力。本文要解决的核心问题是：如何准确诊断MLLMs在时空组合理解上的真实能力，剥离静态内容和语言先验的干扰，专门评估模型对纯时间动态结构的推理能力。为此，论文提出了TimeBlind这一诊断性基准，其核心设计是采用“最小对比对”范式：每个实例包含两个静态视觉内容几乎相同、仅时间结构不同的视频，并配以互补性问题来消除语言先验，从而强制模型必须依据时间证据进行推理。该基准构建了一个系统的时空组合性分类体系（事件、事件属性、结构事件逻辑），以全面评估模型的细粒度时序理解能力。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为视频问答基准和时空组合性评估两大类。

在**视频问答基准**方面，早期数据集关注简单场景和短片段，而近期基准则致力于综合评估、复杂推理、长时理解和特定领域设置。然而，这些工作大多未能将时间结构作为唯一的区分因素，导致模型可能依赖静态视觉捷径（如物体共现）或语言先验，而非真正建模时间动态。

在**评估时空组合性**方面，近期研究旨在更精准地诊断模型的时间推理能力。例如，在图像领域，BLINK通过精心设计的多选题来评估感知能力并消除语言先验。在视频领域，一些工作通过设计具有时间挑战性的问题来明确评估时间理解。特别值得注意的是，采用**配对视频-问题协议**的研究方向，如TempCompass通过系统操作原始视频（如反转播放或改变速度）来构建视频对，从而将时间理解与“静态捷径”隔离；VinoGround则进一步要求模型对配对视频回答相同问题，确保正确答案仅由时间差异决定，有效消除了语言先验。后续的GLIMPSE和MVP等工作将此范式扩展到物理和视觉中心推理。

**本文与这些工作的关系和区别**在于：TimeBlind同样采用了配对视频的最小对比范式来隔离时间因素并消除语言先验，这与TempCompass、VinoGround等一脉相承。然而，本文的核心创新在于提出了一个**精心策划的形式化分类体系**。它从认知事件感知理论出发，并扩展了图像组合性理论，将时间推理系统地分解为原子事件、参数化事件属性和结构逻辑三个层次，从而实现了对时空组合性更细致、更结构化的评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TimeBlind的诊断性基准测试来解决视频大语言模型（Video LLMs）在细粒度时空理解上的不足。其核心方法是设计一个严格控制的评估框架，迫使模型必须依赖真实的时序推理，而非静态视觉或语言先验的捷径。

**整体框架与架构设计**：TimeBlind的架构围绕“时序最小对”范式构建。每个测试实例是一个四元组 `(v1, v2, q1, q2)`，包含一对视频和一对互补问题。视频对 `(v1, v2)` 在静态视觉内容（物体、背景）上完全相同，仅在某个特定的时序维度上存在差异。问题对 `(q1, q2)` 是逻辑互补的，即对于同一个问题，两个视频的正确答案是相反的。这种设计“抵消”了静态视觉线索和语言先验，模型必须精确捕捉并推理视频间的时序差异才能正确回答。

**主要模块与关键技术**：
1.  **认知启发的组合性分类法**：这是基准的理论基础，将时序理解分解为三个递进的原语层级：
    *   **事件**：识别原子视觉变化（如开门 vs. 关门）。
    *   **事件属性**：感知事件如何展开的连续或定性参数（如速度、力度、持续时间）。
    *   **结构事件逻辑**：推理多个事件间的高阶关系（如时间拓扑、因果关联、跨事件比较）。
2.  **三层数据构建流水线**：
    *   **模式生成**：使用前沿大语言模型（如GPT-5）根据分类法生成描述时序差异的视频对描述和互补问题对。
    *   **视频获取**：通过三种来源获取匹配描述的视频对：互联网检索（从同一视频源提取不同时序片段）、人工录制、模拟生成（如Unity），以确保对时序因素的精确控制。
    *   **人工严格验证**：对每个候选实例进行人工审核，确保满足**静态一致性**、**时序最小性**和**问题有效性**，保证数据的高质量和诊断的纯净性。
3.  **诊断性评估指标**：采用分层指标来全面评估模型能力并规避捷径。核心指标是**实例准确率**，要求模型对一个实例中的两个视频、两个问题（共四个判断）全部答对，这被视为模型真正掌握时空组合性理解的代理指标。此外还包括视频准确率、问题准确率等辅助指标。

**创新点**：
1.  **“最小对”诊断范式**：通过严格控制变量（仅时序不同），将模型的缺陷直接归因于时序理解能力的缺失，提供了前所未有的诊断清晰度。
2.  **组合性分类法**：系统地将复杂的时空理解分解为可解释、可评估的认知层级，使评估更具结构性，并能定位模型在哪个抽象层次上失败。
3.  **互补问题设计**：有效中和了模型可能依赖的语言先验或文本合理性猜测，迫使模型必须基于视频证据进行判断。
4.  **多源、高质量的数据集构建**：结合自动化生成与严格人工验证，确保了600个实例（2400个视频-问题对）在保持挑战性的同时，具有高度的可靠性和平衡性（如三类任务比例均衡，时间拓扑关系覆盖全面）。

### Q4: 论文做了哪些实验？

论文在TimeBlind基准上进行了全面的实验评估。实验设置方面，采用零样本评估，视频通常以1 FPS均匀采样，在4块NVIDIA H100 GPU上进行。评估了超过20个前沿的多模态大语言模型（MLLMs），包括闭源模型（如GPT-5、Gemini 3 Pro、Claude、Qwen3-VL Plus）和开源模型（如Qwen3-VL、InternVL 3.5、Molmo2等）。主要评估指标是实例准确率（I-Acc），即正确区分视频对中两个视频的能力，同时报告了标准准确率（Acc）、视频准确率（V-Acc）和问题准确率（Q-Acc）。

主要结果显示，所有模型在细粒度时空理解上都表现不佳。最佳模型Gemini 3 Pro的I-Acc仅为48.2%，远低于人类表现的98.2%。开源模型中，Molmo2-8B表现最佳，I-Acc为31.2%，甚至超过了更大的Qwen3-VL-235B（25.8%）。分析表明，模型在离散事件识别上相对较好（如GPT-5在事件类别平均I-Acc为58.3%），但在需要理解连续物理属性（如速度、力度）的事件属性类别上表现很差（GPT-5为32.3%），在结构事件逻辑推理上也存在不足。消融实验表明，单纯增加输入帧数（从8帧到32帧）或模型参数量对I-Acc提升有限（通常只有个位数百分比增长），而启用推理模式（如Thinking模式）能带来一定提升（如Qwen3-VL-235B提升10.4%至36.3%），但仍远未解决问题。此外，通过单帧、纯语言和帧乱序的短路测试证实，成功通过TimeBlind需要真正的时序理解，而非依赖静态捷径。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准测试主要关注诊断而非解决方案，且当前评估的模型在细粒度时空推理上表现薄弱，揭示了模型过度依赖静态视觉线索的核心问题。未来研究可进一步探索以下方向：首先，开发更高效的时空表示学习方法，如引入可学习的时序注意力机制或动态图神经网络，以增强模型对事件间依赖关系的建模能力。其次，结合因果推理框架，设计能够显式推理事件前后因果关系的训练目标，减少对表面关联的依赖。此外，可扩展基准的复杂度，引入更长时序、多模态交互（如音频与动作）的测试场景，以更贴近真实世界的动态性。最后，探索小样本或零样本迁移能力，使模型能泛化至未见的时空组合模式，推动具身智能等应用的发展。

### Q6: 总结一下论文的主要内容

该论文提出了TimeBlind，一个用于诊断视频大语言模型（Video LLMs）时空组合理解能力的基准测试。核心问题是现有模型虽擅长静态语义理解，但对精细时间动态的把握依然薄弱。TimeBlind将细粒度时间理解分为三个认知层次：识别原子事件、描述事件属性、推理事件间依赖关系。其关键方法在于采用“最小对比对”范式：构造视频对，它们静态视觉内容完全相同，仅时间结构不同，并配以互补性问题以消除语言先验偏差。通过评估20多个前沿MLLM（如GPT-5、Gemini 3 Pro）在600个实例（共2400个视频-问题对）上的表现，主要结论是：最佳模型的实例准确率（正确区分一对视频）仅为48.2%，远低于人类水平（98.2%）。这表明即使顶尖模型也严重依赖静态视觉捷径而非真正的时间逻辑推理。TimeBlind的贡献在于提供了一个精准的诊断工具，揭示了当前视频理解的重大缺陷，对推动下一代具身AI和视频推理模型的发展具有重要意义。
