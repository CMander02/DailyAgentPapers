---
title: "DUEL: Adversarial Self-Play for Multimodal Reasoning"
authors:
  - "Lin Qiu"
  - "Hanqing Zeng"
  - "Yao Liu"
  - "Bingjun Sun"
  - "Guangdeng Liao"
  - "Ji Liu"
date: "2026-05-24"
arxiv_id: "2605.24794"
arxiv_url: "https://arxiv.org/abs/2605.24794"
pdf_url: "https://arxiv.org/pdf/2605.24794v1"
categories:
  - "cs.CV"
  - "cs.CL"
tags:
  - "多模态推理"
  - "自对弈强化学习"
  - "视觉语言模型"
  - "对抗训练"
  - "无监督后训练"
relevance_score: 8.5
---

# DUEL: Adversarial Self-Play for Multimodal Reasoning

## 原始摘要

Reinforcement learning (RL) has emerged as an effective paradigm for improving the reasoning capability of vision-language models (VLMs). However, RL-based optimization typically depends on costly high-quality annotations that are difficult to scale. Existing unsupervised alternatives may drift toward biased solutions due to weak visual grounding and the lack of reliable verification signals. We propose a self-evolving post-training framework, DUEL, where supervision emerges from adversarial interactions between two policies initialized from the same pretrained VLM. A Challenger generates an image-grounded true claim together with a minimally perturbed hard-negative counterpart, while a Solver verifies both claims against the image, encouraging fine-grained visual discrimination under near-neighbor semantics. To stabilize optimization, we introduce a length-normalized log-likelihood reward that preserves informative optimization signals beyond binary outcome supervision and improves learning stability under sparse feedback. Experiments show that DUEL consistently improves visual reasoning and robust discrimination without additional human annotations, external reward models, or image editing tools.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文提出了一种名为DUEL的自进化后训练框架，旨在解决多模态推理中强化学习训练信号获取困难的问题。现有视觉-语言模型（VLM）主要依赖大规模人工标注数据或外部监督，如监督微调和基于偏好的对齐，但这在开放视觉环境中难以扩展且存在奖励偏差。虽然自进化方法已在大型语言模型（LLM）中取得进展，但将其扩展到VLM面临根本性挑战：自一致性方法可能强化错误预测并陷入性能平台，而Vision-Zero等现有工作依赖外部图像编辑工具（如GPT模块）来构造训练信号，缺乏可靠的视觉验证机制。核心问题在于，如何在不使用额外人工标注或外部奖励模型的情况下，构建既能锚定于视觉证据又能稳定提供可扩展训练信号的监督信号。DUEL通过从同一个预训练VLM实例化两个策略，让挑战者（Challenger）生成基于图像的真实声明及其最小扰动的难负例，求解者（Solver）则需验证两者真伪，从而在零和对抗中自主产生微调视觉辨别力的监督信号。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是**监督式多模态预训练**，如CLIP、Flamingo和BLIP-2，它们依赖大规模人工标注或精细数据，而DUEL无需任何人工标注。第二类是**基于RLHF的多模态对齐**，包括Factually Augmented RLHF和DPO，这些方法依赖外部提供的偏好对或静态偏好信号，而DUEL通过在线对抗自对弈从未标注图像中构建训练信号。第三类是**自对弈和自我进化学习范式**，包括Vision-Zero、EvoLMM和VisPlay等，它们利用一致性或自洽性信号从无标签数据中学习。与这些仅依赖一致性信号从而可能强化偏见预测的方法不同，DUEL将自对弈构建为对抗性配对验证游戏：挑战者生成近邻反事实声明，解决者验证声明与图像的一致性，从而鼓励细粒度视觉判别。DUEL的创新在于通过对抗性互动生成监督信号，利用长度归一化对数似然奖励稳定优化，无需外部奖励模型或图像编辑工具。

### Q3: 论文如何解决这个问题？

DUEL提出了一种基于对抗自对弈的无监督后训练框架，核心在于通过两个从同一预训练VLM初始化的策略——挑战者（Challenger）和解决者（Solver）——进行零和博弈。整体框架如图2所示：给定无标注图像，挑战者首先生成一个有图像支撑的真实声明（true claim），然后基于该真实声明和图像生成一个最小扰动的硬负样本声明（hard-negative false claim），通过词级编辑距离约束确保两者语义高度接近但真假相反。解决者针对每个声明输出一个包含视觉推理证据和二元判断（yes/no）的验证序列。关键技术包括：1）长度归一化的对数似然奖励函数，该函数结合了结果正确性（+1/-1）和序列平均对数概率，在稀疏反馈下提供更细粒度的优化信号；2）基于GRPO的组归一化策略优化，通过多个采样输出计算组内归一化优势值来降低梯度方差。创新点在于这种自监督的对抗自对弈机制使得解决者必须学习细粒度的视觉证据判别，无法依赖语言先验或粗略语义差异，而挑战者在最小偏差约束下持续生成更具挑战性的负样本，形成相互促进的迭代优化过程。整个训练不需要任何人工标注、外部奖励模型或图像编辑工具。

### Q4: 论文做了哪些实验？

论文在多个视觉推理基准上评估了DUEL框架。**实验设置**：使用LoRA微调，在2块NVIDIA H200 GPU上训练约24小时，Solver与Challenger从同一预训练VLM初始化。**数据集与基准**：训练集来自ChartQA、AI2D等6个基准共约6000张无标签图像；测试集包含8个基准，涵盖数学推理（MathVerse、MathVista、VisNumBench）、图表理解（ChartQA、AI2D）和通用推理（ScienceQA、MMMU、MuirBench）。**对比方法**：包括无监督方法（MM-UPT、Vision-Zero、EvoLMM）和监督方法（VLAA-Thinker-7B、OpenVLThinker-7B）。**主要结果**：DUEL（Solver）在8个基准中6个取得最高精度，平均提升+1.4%（如ChartQA +2.1%、MathVista +1.4%），优于所有无监督和监督基线。消融实验显示，配对负样本构建贡献最大（去除后ChartQA下降2.8%），隐身正则化与校准奖励次之。数据规模实验表明，仅需1K无标签图像即可达接近完整性能（平均69.0%），增至12K仅提升0.3%。超参数敏感性分析显示，隐身权重λ=0.2-0.3、温度α≈5、Solver采样次数K=3-4时性能最优。此外，DUEL在Qwen2.5-VL-7B/3B、InternVL3-8B和Gemma3-12B-IT四种架构上均取得一致提升（相对平均提升+2.0%至+2.9%）。

### Q5: 有什么可以进一步探索的点？

DUEL的自我博弈框架在视觉推理上展现了潜力，但其核心局限在于硬负样本生成的动态性和奖励信号的稀疏性。未来可探索的方向包括：1）引入更细粒度的对抗课程学习，让Challenger根据Solver的当前弱点自适应地调整扰动幅度和语义偏移量，从而持续提供“恰到好处”的训练难度；2）改进奖励机制，例如结合对比学习中的InfoNCE损失或基于边际的排序损失，提升对近邻语义的区分能力，避免长度归一化对数似然在长文本推理中的饱和问题；3）将框架扩展到多模态链式推理场景，让Challenger不仅生成单步声明，还能构造多步逻辑中的矛盾子图，强制Solver进行更鲁棒的跨模态推理验证。此外，探索在训练中引入不确定度估计或正则化项，可能有助于缓解自我博弈中身份混淆导致的概念崩塌。

### Q6: 总结一下论文的主要内容

DUEL提出了一种基于对抗性自我博弈的多模态推理后训练框架。该方法针对强化学习优化依赖昂贵高质量标注、无监督方法易因弱视觉基础而漂移的问题，从同一预训练视觉语言模型（VLM）初始化两个策略，通过对抗互动产生监督信号。其中挑战者生成基于图像的真相声明及其最小扰动的困难负样本，解决者则验证两个声明与图像的匹配，促进细粒度视觉判别。为稳定优化，引入长度归一化的对数似然奖励，提供比二元结果监督更丰富的优化信号。实验表明，无需人工标注、外部奖励模型或图像编辑工具，DUEL在视觉推理和鲁棒判别上持续优于无监督和有监督基线，具备高数据效率和低训练成本，为自我进化的VLM提供了可扩展、架构无关且经济的路径。
