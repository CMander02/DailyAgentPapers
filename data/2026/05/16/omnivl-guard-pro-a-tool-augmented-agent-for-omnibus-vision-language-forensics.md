---
title: "OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics"
authors:
  - "Jinjie Shen"
  - "Zheng Huang"
  - "Yuchen Zhang"
  - "Yujiao Wu"
  - "Yaxiong Wang"
  - "Lechao Cheng"
  - "Shengeng Tang"
  - "Tianrui Hui"
  - "Nan Pu"
  - "Zhun Zhong"
date: "2026-05-16"
arxiv_id: "2605.16962"
arxiv_url: "https://arxiv.org/abs/2605.16962"
pdf_url: "https://arxiv.org/pdf/2605.16962v1"
github_url: "https://github.com/shen8424/OmniVL-Guard-Pro"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Tool-Augmented Agent"
  - "Vision-Language Forensics"
  - "Reinforcement Learning"
  - "Multi-modal Agent"
  - "Zero-shot Generalization"
relevance_score: 7.5
---

# OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics

## 原始摘要

Existing vision-language forgery detection and grounding methods operate under a closed-world paradigm, assuming verification can be completed by the model alone. However, self-contained MLLMs are constrained by finite parametric knowledge, static training corpora, and limited perceptual resolution, creating a practical ceiling in dynamic open-world forensics -- particularly for real-time event verification requiring external clues and forgery segmentation demanding fine-grained scrutiny of local manipulations. To address these limitations, we shift from scaling up the self-contained model toward reaching beyond it. We propose \textbf{OmniVL-Guard Pro}, a tool-augmented agent that extends unified forensics from closed-world prediction to open-world clues-driven reasoning. OmniVL-Guard Pro integrates a tool environment spanning real-time event search, local cropping and zooming, edge-anomaly screening, face detection, video frame extraction, and SAM3-based segmentation. To generate high-quality tool-reasoning trajectories, we introduce \textbf{Tree-Structured Self-Evolving Tool Trajectory Generation}, which produces diverse trajectories through seed guidance, guider-free self-evolution, and weakly-hinted hard sample synthesis, yielding the Full-Spectrum Tool Reasoning (FSTR) dataset for training. We further propose \textbf{Checker-Guided Agentic Reinforcement Learning} (CGARL), which provides process-level supervision to penalize cases where the answer is correct but the reasoning is distorted. Extensive experiments demonstrate that OmniVL-Guard Pro achieves state-of-the-art performance across various tasks, and exhibits strong zero-shot generalization. The FSTR dataset and code for OmniVL-Guard Pro will be publicly released at \url{https://github.com/shen8424/OmniVL-Guard-Pro}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有视觉语言伪造检测与定位方法在**开放世界场景**下的局限性。当前方法主要采用**封闭世界范式**，假设模型能独立完成所有验证，但自包含的多模态大语言模型受限于有限的参数知识、静态训练语料和较低的感知分辨率，在处理动态、开放的取证任务时面临瓶颈。具体而言：在**实时事件验证**任务中，模型需要获取超出其参数记忆的实时外部线索；在**伪造分割**任务中，则需要精细的局部边界、纹理等细粒度异常分析。传统的“扩展模型规模”策略成本高昂且难以应对持续演变的伪造技术。

为了突破这一天花板，本文提出的核心问题是：**如何将封闭世界预测拓展为开放世界线索驱动推理**。即构建一个**工具增强的智能体**，使其能动态获取外部知识和调用专业感知工具（如实时搜索、局部裁剪、边缘异常筛查、人脸检测等），以弥补基座模型的内在不足。同时，还需解决高质量工具推理轨迹生成的难题（避免事后偏差），并确保模型在利用工具时形成证据一致且可验证的判断，而非仅得到偶然正确的答案。

### Q2: 有哪些相关研究？

相关研究主要围绕多模态伪造检测与定位、工具增强型智能体以及推理轨迹生成三个方面展开。在方法类研究中，OmniVL-Guard建立了统一的多模态伪造检测和定位框架，但闭世界假设限制了其实时事件验证和细粒度分割能力。本文引入工具增强型智能体，通过外部工具拓展能力边界。相关工作还包括纯文本思维链推理和工具调用方法，但与这些工作不同，本文处理的是跨文本、图像和视频模态的伪造检测任务，需要同时进行工具选择、参数指定和观察理解。在训练数据生成方面，现有方法多依赖人工标注或直接注入答案，容易产生后见偏差。本文提出的树状结构自演化工具轨迹生成方法通过种子引导、无引导自演化和弱提示的难样本合成构建高保真轨迹数据集FSTR，避免了直接注入答案信息。在强化学习方法上，传统方法主要关注答案级别的奖励信号。本文提出的检查器引导智能体强化学习引入过程级监督，通过多智能体系统中的检查器评估中间推理、工具使用和观察证据是否支持最终判断，有效缓解了答案正确但推理过程扭曲的伪成功模式。在评测类工作中，本文构建了实时事件验证基准，这是现有工作缺乏的。

### Q3: 论文如何解决这个问题？

该论文通过构建一个工具增强的智能体框架，将视觉语言取证从封闭世界预测扩展到开放世界线索驱动推理，核心包括三个创新部分。

整体框架由工具环境、轨迹生成和强化学习三部分组成。首先，工具环境集成了实时事件搜索、局部裁剪与放大、边缘异常筛查、人脸检测、视频帧提取以及基于SAM3的分割等工具，使模型能够获取超出自身参数知识的动态外部证据，支持检测、定位和分割任务。

为解决冷启动阶段高质量工具搜索轨迹的生成难题，论文提出树状结构自演化工具轨迹生成策略。该策略分为四个阶段：在少量种子数据上，利用两个专家MLLM分别作为探索者和指导者，通过树状分支扩展与剪枝生成高保真轨迹；随后进行无指导者自演化，让模型自主探索并过滤有效轨迹；对于长尾困难样本，采用弱提示机制提供粗略线索，再由精炼者消除提示痕迹，最终形成涵盖5种模态、69k样本的全面工具推理数据集（FSTR），支持分类、定位、分割和实时事件验证。

在训练阶段，论文提出检查器引导的智能体强化学习（CGARL），采用三阶段训练。首先在FSTR上进行SFT获得初始策略，然后用结果级强化学习训练出具有工具能力的策略π_ans；接着利用该策略在另一子集上生成轨迹，并由多个专家MLLM交叉验证构建检查器训练集，训练出过程判别模型π_checker；最后在第三阶段进行检查器引导的过程监督强化学习，对正确但推理过程扭曲的样本施加惩罚，同时引入工具使用效率奖励，使模型在保证答案正确的同时生成更连贯、可信且简洁的工具推理轨迹。

### Q4: 论文做了哪些实验？

论文通过多维度实验验证了OmniVL-Guard Pro的性能。实验设置分为域内和域外零样本两种场景：域内使用对应测试集；域外（OOD）涵盖ISOT（文本）、CASIA2.0（图像）、MMFakeBench（图文）、FakeTT（视频-文本）和IMD（分割）等基准。对比方法包括通用多模态大模型（如Qwen3VL-235B，零样本评估）和领域专用方法（直接跨域测试）。主要结果如下：

1.  **域内对比**：OmniVL-Guard Pro在所有任务中取得最佳性能。特别是在细粒度任务上提升显著：实时验证（RealFact）和分割任务分别比先前方法提升30.71%和25.77%。
2.  **域外零样本对比**：模型超越所有通用MLLM和领域专用方法。在文本-图像和文本-视频任务上分别达到81.74%和68.06%的准确率，在IMD分割上达到42.93% Dice系数。
3.  **消融实验**：
    *   **训练组件**：仅SFT效果有限；加入结果级强化学习（ARSPO）平均提升21.64%；使用专用Checker进行过程监督，平均提升达28.16%，优于直接使用通用MLLM的16.28%。
    *   **工具模块**：移除所有工具导致全任务大幅下降。其中移除搜索工具使RealFact准确率从86.5%降至62.3%；移除视频工具使视频定位tIoU从64.4%降至15.7%，证实各工具提供互补证据。

### Q5: 有什么可以进一步探索的点？

该工作通过工具增强的智能体范式将闭集伪造检测推向开放世界，但仍有若干值得深化的方向。首先，工具环境虽然丰富，但当前工具集（如搜索、分割）是预定义的，未来可探索让代理动态自主定义或组合新工具，以适应更异构的伪造形态。其次，Tree-Structured Self-Evolving Trajectory Generation依赖于初始种子轨迹的质量，种子偏差可能导致轨迹分布固化，可考虑引入对抗性种子生成或基于多样性的主动采样策略来缓解。CGARL中的Checker提供过程级监督，但其评分标准可能无法覆盖所有合理的推理路径，未来可研究更细粒度的、可解释的奖励模型，或在多轮交互中加入人类反馈微调。此外，面对细粒度篡改如局部像素级修改，当前基于SAM3的粗粒度分割可能不够精确，可结合高分辨率特征或扩散模型的反向推理进行像素级定位。最后，跨模态时序一致性推理（如视频帧间的工具调用）也是重要延伸点。

### Q6: 总结一下论文的主要内容

现有视觉语言取证方法局限于封闭世界，依靠模型自身完成验证，受限于有限参数知识、静态训练数据和感知分辨率。本文提出OmniVL-Guard Pro，一个工具增强的智能体，将统一取证从封闭世界预测扩展到开放世界线索驱动的推理。它集成了实时事件搜索、局部裁剪放大、边缘异常筛查、人脸检测、视频帧提取和SAM3分割等工具环境。为生成高质量工具推理轨迹，本文提出树结构自演化工具轨迹生成，通过种子引导、无引导者自演化和弱提示难样本合成，生成全频谱工具推理数据集。进一步提出检查器引导的智能体强化学习，提供过程级监督惩罚答案正确但推理扭曲的情况。实验表明，OmniVL-Guard Pro在多种任务上达到最先进性能，并展现出强大的零样本泛化能力。该工作为开放场景下的视觉语言取证提供了新的范式。
