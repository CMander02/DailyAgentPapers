---
title: "Agentic Planning with Reasoning for Image Styling via Offline RL"
authors:
  - "Subhojyoti Mukherjee"
  - "Stefano Petrangeli"
  - "Branislav Kveton"
  - "Trung Bui"
  - "Franck Dernoncourt"
  - "Arko Mukherjee"
date: "2026-03-07"
arxiv_id: "2603.07148"
arxiv_url: "https://arxiv.org/abs/2603.07148"
pdf_url: "https://arxiv.org/pdf/2603.07148v1"
categories:
  - "cs.LG"
tags:
  - "Agentic Planning"
  - "Tool Use"
  - "Offline RL"
  - "Reasoning"
  - "Image Editing"
  - "Synthetic Data"
  - "Vision-Language Model"
relevance_score: 8.0
---

# Agentic Planning with Reasoning for Image Styling via Offline RL

## 原始摘要

Direct prompt-based editing often fails on complex transformations because vague and subjective prompts often require nuanced understanding of what should be changed in the image. Our core intuition is that leveraging compositional image editing tools rather than direct prompting profits from structured agent-level planning with explicit reasoning, leading to better results. This structured planning framework enables efficient offline RL post-training on quality-scored trajectories to improve performance. We present a tool-based agentic RL post-training framework that addresses this through structured planning with chain-of-thought reasoning. Our key contributions include: (1) A tool-based agentic planning methodology that combines a compositional library of orthogonal primitive transformations, structured context representation, and explicit per-step reasoning to decompose complex styling into interpretable tool sequences. (2) A synthetic data generation pipeline producing three large-scale datasets (each $\sim$10K trajectories) with reasoning chains, plans, and quality scores, as no existing datasets provide such supervision. Our datasets and code are publicly available at the HuggingFace repository. (3) Offline RL training methods for learning planners with reasoning as our core algorithmic contributions, which consistently improve over the Edit-Only baseline in visual quality and instruction following. (4) Comprehensive evaluation across 4B and 8B parameter Qwen3-VL models showing that our methods outperform other baselines in the majority of compositional tasks, validated by human evaluations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于自然语言提示的直接图像编辑方法在处理复杂、多维度的图像风格化任务时效果不佳的问题。研究背景是，随着视觉-语言基础模型（如DALL-E、Stable Diffusion）的发展，用户可以通过自然语言提示来编辑图像，这极大地 democratized 了图像编辑。然而，现有方法（如直接提示编辑或单次前向生成）存在根本性不足：自然语言提示通常是模糊和主观的，难以精确表达复杂的、需要协调多个视觉属性（如光照、季节、天气、氛围）的转换意图。这导致模型在理解用户指令时产生歧义，生成的图像往往存在不一致、指令遵循度低、颜色错位和结构伪影等问题。

本文要解决的核心问题是：如何通过结构化的智能体规划和显式推理，将复杂的图像风格化任务分解为一系列可解释的、基于工具的原语操作序列，从而实现对图像更精确的控制，并生成更符合人类偏好的高质量结果。为此，论文提出了一个基于工具的智能体强化学习后训练框架，其核心创新在于结合了组合工具库、结构化上下文表示、分步思维链推理以及利用质量评分轨迹进行离线RL训练的方法，以学习更好的规划器，从而超越直接提示编辑的基线性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：图像风格化方法、基于工具的规划与推理、以及离线强化学习与对齐技术。

在**图像风格化方法**方面，早期工作包括经典的图像到图像翻译、神经风格迁移和循环一致性对抗网络，它们为跨域视觉转换奠定了基础，但通常局限于特定变换或需要配对数据。近期，基于视觉语言基础模型（如DALL-E、Stable Diffusion、Qwen3-VL）的直接提示编辑成为主流，允许用户通过自然语言指令进行图像编辑。此外，StyleBooth和Styleshot等专门方法针对个性化风格迁移和少样本风格适应进行了优化。本文与这些工作的核心区别在于：现有方法大多采用从提示到图像的“直接映射”范式，而本文则引入了一个基于工具的、结构化的智能体规划框架，将复杂任务分解为可解释的原始工具序列，从而实现对多维度变换的更精确控制。

在**基于工具的规划与推理**方面，相关研究涉及工具增强的智能体和思维链推理。本文借鉴了使用组合工具库进行复杂任务分解的思想，但进一步提出了结构化的文档表示和每步的思维链推理，以显式编码图像状态并解释规划决策，从而提升规划的可解释性和一致性。

在**离线强化学习与对齐技术**方面，相关研究包括基于人类反馈的强化学习（RLHF）和直接偏好优化（DPO）等，用于对齐模型输出与人类偏好。本文采用离线RL进行后训练，其优势在于使用固定、经人工验证的高质量轨迹数据集，确保了可重复性和公平比较。本文的核心算法贡献是提出了奖励加权（RW）和标准化奖励加权（SW）训练方法，通过根据轨迹质量分数进行加权损失计算，有效提升了从合成数据中学习组合规划的性能。

总之，本文的创新在于将上述方向有机结合，构建了一个包含组合工具库、结构化状态表示、显式推理链和离线RL后训练的完整框架，以解决直接提示编辑在复杂、主观图像风格化任务中的局限性。

### Q3: 论文如何解决这个问题？

论文通过一个结合结构化规划、链式推理和离线强化学习的智能体框架来解决复杂图像风格化中模糊提示导致效果不佳的问题。其核心方法是将图像编辑重新定义为序列决策过程，让智能体学习从组合工具库中调用工具来逐步转换图像。

整体框架包含四个阶段：第一阶段（提取结构化上下文）将输入图像和用户提示转换为包含10个视觉维度（如地点、建筑风格、时间、季节等）的文本描述，为规划提供明确依据。第二阶段（带推理的行动规划）是关键创新，模型基于上下文和原始提示，通过链式思维（CoT）逐步推理，生成一系列符号化工具调用动作。例如，将“文艺复兴油画风格”分解为设置时代、选择油画媒介、调整色调和光照等具体步骤，每个步骤都伴随明确的推理文本。第三阶段（合成精确指令）将推理链和动作序列整合成详细、精确的自然语言编辑指令。第四阶段（渲染最终图像）使用冻结的黑盒图像编辑器（如Qwen-Image-Edit）执行该指令，生成最终图像。这种设计将“规划”（决定改什么和怎么改）与“执行”（像素渲染）分离，使训练专注于提升语言模型的推理和规划能力。

在关键技术方面，论文构建了一个正交的组合工具库，包含10个相互独立的参数化变换维度（如time_of_day、artistic_medium），确保效果可组合且干扰最小。更重要的是，论文提出了多种离线强化学习算法进行规划器的奖励感知后训练，以利用合成轨迹的质量分数（奖励）。这些算法包括：1）简单的监督微调（SFT），忽略奖励信号；2）基于过滤的行为克隆（BC），仅使用高质量轨迹；3）直接偏好优化（DPO），从偏好对比中学习；4）奖励加权回归（RW），按奖励比例加权损失；5）标准化奖励加权（SW），通过标准化奖励减少方差，使其能适应不同输入间的奖励分布差异。其中，SW算法是核心创新之一，它通过计算数据集中奖励的z-score作为样本权重，在保留所有数据多样性的同时，让高于平均质量的轨迹对梯度更新有更大贡献，从而稳定、高效地提升规划质量。

此外，论文还贡献了大规模合成数据生成管道，产生了三个包含推理链、行动计划和质量分数的大规模数据集（各约1万条轨迹），为训练提供了必要的监督信号。实验表明，该框架在4B和8B参数的Qwen3-VL模型上均能有效提升视觉质量和指令跟随能力，在多数组合任务上超越基线。

### Q4: 论文做了哪些实验？

论文的实验设置围绕评估其提出的基于工具的智能体离线强化学习框架在图像风格化任务上的性能。实验使用了三个合成数据集：Simple（10,000条轨迹，1-2步编辑）、Regular（10,000条轨迹，3-5步组合编辑，含10个室内设计主题）和Complex（10,000条轨迹，3-5步组合编辑，含83个多样主题）。这些数据集通过一个四阶段流程生成，包含推理链、计划和质量分数。

对比方法包括八种：基线（B，未经微调的预训练Qwen3-VL）、仅编辑（E，无结构化规划的直接图像编辑）、标准监督学习（S，平等对待所有轨迹）、RL（奖励过滤训练，丢弃35%数据）、奖励加权（RW，按奖励分数加权梯度）、标准化奖励加权（SW，z分数归一化梯度加权）、DPO（基于成对偏好的对比学习）以及GPT-4o规划器（零样本参考）。实验在Qwen3-VL-4B和8B模型上进行，包括仅文本和视觉语言两种配置。

主要结果基于GPT-4o对200个测试样本在6个图像质量维度（0-100分）的评估。关键发现包括：离线RL方法有效，SW在组合文本任务中表现最佳（4B模型总体得分78.77），RW在简单视觉任务中占优（视觉-4B总体得分79.33），DPO在多样主题分布中领先（复杂视觉-8B总体得分85.41）。仅编辑基线（E）持续表现不佳，总体差距达1.3-7.3分，证实了结构化规划的必要性。训练后的模型在规划指标（如语义准确性、指令遵循）上显著优于基线，且紧凑模型在多数配置中图像质量超过GPT-4o零样本基线。视觉模型通过视觉接地获得更高绝对分数，而显式的逐步推理链提升了规划质量。

### Q5: 有什么可以进一步探索的点？

本文提出的基于工具的智能体强化学习框架在图像风格化任务上取得了进展，但仍存在一些局限性和值得探索的方向。首先，其工具库目前仅限于10种基础图像变换操作，未来可以扩展至更丰富、更细粒度的编辑工具（如局部笔刷、3D变换），以处理更复杂的创意需求。其次，该方法依赖于合成数据生成，虽然规模较大，但与真实用户编辑数据存在分布差距；未来可探索结合少量人类编辑轨迹进行微调，或利用在线交互数据提升泛化能力。此外，当前框架主要针对静态图像，未来可延伸至视频编辑，需解决跨帧时序一致性与动态风格迁移等挑战。从算法角度看，离线强化学习对奖励函数设计敏感，本文采用人工评分，未来可研究更自动化、多模态的质量评估机制（如基于视觉-语言模型的偏好学习）。最后，该智能体规划依赖于链式推理，但推理步骤的生成可能受限于基础大模型的能力；结合更强大的世界模型或知识增强的推理模块，有望进一步提升复杂任务下的规划鲁棒性与创造性。

### Q6: 总结一下论文的主要内容

本文提出了一种基于工具的智能体强化学习（RL）后训练框架，用于解决复杂图像风格化任务中直接提示编辑效果不佳的问题。核心思想是通过结构化规划和显式推理，将模糊的用户指令分解为可解释的、由基础工具组成的操作序列，从而实现对图像的多维度精确编辑。

论文的主要贡献包括：首先，设计了一种结合正交原始变换工具库、结构化上下文表示和逐步推理链的智能体规划方法，能够将复杂风格化任务分解为可解释的工具序列。其次，构建了一个合成数据生成流程，产生了三个大规模数据集（各约1万条轨迹），包含推理链、规划步骤和质量分数，填补了该领域监督数据的空白。第三，提出了奖励加权（RW）和标准化奖励加权（SW）等离线RL训练方法作为核心算法贡献，这些方法在视觉质量和指令遵循方面持续优于直接提示编辑的基线。最后，在4B和8B参数的Qwen3-VL模型上进行了全面评估，结果表明该方法在大多数组合任务上优于其他基线，并得到了人工评估的验证。

总之，该工作证明了通过结构化规划与基于质量的离线RL训练，能够显著提升图像编辑智能体在复杂任务上的性能，为创意领域的智能体系统提供了一个有效的蓝图。
