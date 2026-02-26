---
title: "EO-1: An Open Unified Embodied Foundation Model for General Robot Control"
authors:
  - "Delin Qu"
  - "Haoming Song"
  - "Qizhi Chen"
  - "Zhaoqing Chen"
  - "Xianqiang Gao"
  - "Dong Wang"
  - "Xinyi Ye"
  - "Qi Lv"
  - "Modi Shi"
  - "Guanghui Ren"
  - "Cheng Ruan"
  - "Maoqing Yao"
  - "Haoran Yang"
  - "Jiacheng Bao"
  - "Bin Zhao"
  - "Xuelong Li"
date: "2025-08-28"
arxiv_id: "2508.21112"
arxiv_url: "https://arxiv.org/abs/2508.21112"
pdf_url: "https://arxiv.org/pdf/2508.21112v5"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "Embodied AI"
  - "Foundation Model"
  - "Robot Control"
  - "Vision-Language-Action"
  - "Multimodal Reasoning"
  - "Interleaved Learning"
  - "Long-Horizon Manipulation"
  - "Generalization"
relevance_score: 9.0
---

# EO-1: An Open Unified Embodied Foundation Model for General Robot Control

## 原始摘要

The human ability to seamlessly perform multimodal reasoning and physical interaction in the open world is a core goal for general purpose embodied intelligent systems. Recent vision-language-action (VLA) models, which are co-trained on large-scale robot and visual-text data, have demonstrated notable progress in general robot control. However, they still fail to achieve human-level flexibility in interleaved reasoning and interaction. In this work, we introduce EO-Robotics, consists of EO-1 model and EO-Data1.5M dataset. EO-1 is a unified embodied foundation model that achieves superior performance in multimodal embodied reasoning and robot control through interleaved vision-text-action pre-training. The development of EO-1 is based on two key pillars: (i) a unified architecture that processes multimodal inputs indiscriminately (image, text, video, and action), and (ii) a massive, high-quality multimodal embodied reasoning dataset, EO-Data1.5M, which contains over 1.5 million samples with emphasis on interleaved vision-text-action comprehension. EO-1 is trained through synergies between auto-regressive decoding and flow matching denoising on EO-Data1.5M, enabling seamless robot action generation and multimodal embodied reasoning. Extensive experiments demonstrate the effectiveness of interleaved vision-text-action learning for open-world understanding and generalization, validated through a variety of long-horizon, dexterous manipulation tasks across multiple embodiments. This paper details the architecture of EO-1, the data construction strategy of EO-Data1.5M, and the training methodology, offering valuable insights for developing advanced embodied foundation models. Project Page: https://eo-robotics.ai/eo-1.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决通用具身智能系统在开放世界中实现多模态推理与物理交互无缝协同的核心难题。当前，尽管基于大规模机器人及视觉-文本数据联合训练的视觉-语言-动作（VLA）模型在通用机器人控制上取得了显著进展，但它们仍无法达到人类在**交错式推理与交互**（interleaved reasoning and interaction）中展现的灵活水平。现有方法主要存在两大不足：一是多数VLA模型仅针对机器人数据集训练，导致其继承的通用语义知识受限、任务领域狭窄且指令遵循能力不足；二是即使近期研究尝试结合网络数据与机器人数据进行协同训练，其模型通常仅在输出序列末端生成机器人动作，忽视了开放世界具身交互中视觉、语言和动作模态间固有的**丰富时序动态与因果依赖关系**，未能实现推理与行动灵活互通的协同机制。

为此，本文提出了**EO-Robotics**框架（包含EO-1模型与EO-Data1.5M数据集），其核心目标是**通过交错式视觉-文本-动作预训练，构建一个统一的具身基础模型，以同时提升多模态具身推理与机器人控制性能**。具体而言，研究重点围绕两个关键支柱展开：一是设计一种**统一架构**，能够无差别地处理图像、文本、视频和动作等多模态输入；二是构建一个大规模、高质量的**多模态具身推理数据集EO-Data1.5M**，其中包含超过150万个强调视觉-文本-动作交错理解的样本。通过自回归解码与流匹配去噪的协同训练，EO-1模型能够在同一序列中灵活生成机器人动作并进行多模态推理，从而模拟人类“推理引导行动、行动反馈推理”的交互模式，最终实现开放世界理解与泛化能力的大幅提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 基础视觉-语言模型（VLMs）与视觉-语言-动作模型（VLA模型）**
*   **方法类**：早期通用机器人策略主要将VLMs（如CLIP、Flamingo等）扩展为VLA模型，通过在机器人数据上进行微调来生成动作。典型方法包括对离散动作令牌进行自回归解码，或引入额外的连续流匹配模块来处理动作。这些工作（如RT-1、RT-2系列）为VLA范式奠定了基础。
*   **本文关系与区别**：本文的EO-1模型同样建立在预训练的VLM之上，继承了广泛的视觉-语言知识。关键区别在于，现有VLA模型通常在序列末端输出动作，忽略了多模态交互中固有的时序动态和因果依赖。而EO-1通过**交错式（interleaved）的视觉-文本-动作预训练**，在统一架构中实现了推理与行动的灵活交织与相互引导。

**2. 多模态数据协同训练**
*   **数据与方法类**：近期研究（如Octo、OpenVLA）探索将网络规模的多模态数据（图像-文本对）与机器人数据共同训练VLA模型，以提升模型在新物体和陌生背景下的泛化能力。
*   **本文关系与区别**：本文延续了利用网络数据和机器人数据协同训练的思路。核心区别在于数据构造范式：本文构建了专门的**EO-Data1.5M数据集**，它不仅包含机器人控制序列，还通过VLM和人工标注，在动作序列中**交错插入了丰富的具身推理QA对**（如物理常识、任务规划、物体定位等），从而直接支持模型学习交错的多模态推理与动作生成。

**3. 模型架构与训练范式**
*   **方法类**：现有VLA模型常为动作生成引入特定的模块或参数（如额外的动作头或适配器），这可能造成模态对齐的瓶颈。
*   **本文关系与区别**：本文提出了一种**统一的解码器架构**，使用单一的Transformer骨干网络，通过共享参数同时处理文本、视觉和动作模态。它创新性地将**自回归解码（用于文本）与流匹配去噪（用于连续动作）** 的目标在交错序列上协同优化，避免了从头训练动作专用参数，促进了更有效的跨模态知识迁移。

**总结**：本文的相关工作脉络是从专用VLA模型，发展到多数据源协同训练的VLA模型。本文的核心推进在于，通过**精心构建的交错式多模态具身数据集**和**支持交错生成与推理的统一模型架构**，旨在实现更接近人类水平的、推理与行动灵活交织的通用具身智能。

### Q3: 论文如何解决这个问题？

论文通过提出一个统一的具身基础模型EO-1及其配套的大规模高质量数据集EO-Data1.5M，来解决现有视觉-语言-动作模型在交错推理与交互方面灵活性不足的问题。其核心方法围绕**统一的架构设计**和**创新的训练范式**展开。

**整体框架与主要模块**：EO-1采用单一的、仅解码器的Transformer作为统一骨干网络（基于Qwen2.5-VL初始化），以无差别的方式处理交错的多模态输入序列，包括图像、文本、视频、机器人状态和带噪声的动作。该架构包含几个关键组件：1）文本分词器和视觉编码器（继承自预训练VLM），用于将文本和图像转换为令牌；2）随机初始化的状态投影器，将机器人状态线性投影到相同的嵌入空间；3）噪声动作线性投影器，用于嵌入带噪声的动作和流匹配时间步。模型通过两个独立的头部生成输出：一个**语言建模头部**用于自回归地解码离散文本令牌，实现多模态具身推理；一个**流匹配头部**用于对连续动作令牌进行去噪，生成机器人控制信号。这种设计使得语义知识能够在视觉-语言理解和动作生成之间无缝迁移。

**关键技术细节与创新点**：
1.  **交错的多模态序列建模与统一提示**：所有模态数据（图像、文本、状态、动作）被编码并拼接成一个交错的令牌序列，使用特殊的开始/结束标记（如[BOI]、[BOS]、[BOR]、[BOA]）进行分隔。模型在此统一序列上进行自回归预测。
2.  **协同的自回归与去噪训练范式**：模型通过结合**下一令牌预测目标**（用于文本生成）和**流匹配去噪目标**（用于动作生成）进行端到端训练。流匹配采用修正流技术，通过预测向量场并从噪声中积分出干净动作。
3.  **交错整流采样策略**：这是处理交错视觉-文本-动作数据的关键创新。在训练包含多个动作生成片段的交错序列时，通过采样多个子序列并巧妙地将中间动作生成片段中的噪声动作令牌替换为干净动作令牌，解决了动作去噪过程可能破坏多模态令牌序列中因果依赖关系的问题，确保了后续文本/图像/动作令牌能够基于干净的前文进行预测。
4.  **全向注意力掩码机制**：在训练时，根据不同的数据类型（纯多模态理解、纯机器人控制、混合模态生成）采用因果注意力掩码，并在推理时缓存已生成多模态上下文的键值对，以加速交错生成。

综上所述，EO-1通过一个共享的Transformer骨干网络统一处理所有模态，并利用创新的交错数据格式、整流采样策略以及结合自回归与流匹配的协同训练目标，实现了在单一模型中无缝衔接的文本推理与物理动作生成，从而提升了在开放世界中长视野、灵巧操作任务上的理解和泛化能力。

### Q4: 论文做了哪些实验？

论文的实验设置包括：在整合了总计135B令牌的大规模语料库上训练EO-1模型，该语料库包含来自多个数据集的120万真实机器人演示、570万网络多模态样本和150万交错体现数据对。训练使用Flash-Attention变长打包，平均序列长度16384，批次大小为1，采用DeepSpeed ZeRO-1优化器。推理时，模型以多视角相机观测和子任务指令为条件，通过10次去噪迭代预测16步动作块，在单张NVIDIA RTX 4090上仅需6GB显存。

实验在两个关键类别的基准测试上进行评估：体现推理和机器人控制。体现推理评估使用了三个基准：RoboVQA（评估具身场景中的高级推理，使用BLEU-4分数）、ERQA（评估空间推理和基础世界知识）以及自建的EO-Benchmark（包含700个多选题，评估物理常识、空间理解、状态估计和任务推理）。机器人控制评估使用了两个操作基准：SimplerEnv（在视觉多样化环境中评估WidowX和Google Robots的短视界任务和真实到模拟的迁移）以及LIBERO（在复杂模拟环境中评估长视界、多阶段任务）。

对比方法包括三类基线：公开的视觉语言模型（如Qwen2.5 VL、InternVL2.5）、私有视觉语言模型（如GPT-4o、Gemini 1.5 Flash、Claude 3.5）以及联合训练的视觉-语言-动作模型（如ChatVLA、Magma）。

主要结果：在体现推理任务上，EO-1（3B参数）在RoboVQA上取得58.5 BLEU-4分数，在ERQA上取得45.5分，在EO-Benchmark的空间子项上取得36.4分，时间子项上取得38.9分，总体得分44.8分。与基线相比，EO-1在RoboVQA上超越了所有对比模型（包括GPT-4o的47.2分和Qwen2.5 VL 7B的56.9分），在ERQA上与最佳基线（InternVL2.5 8B的45.2分）相当，在EO-Benchmark总体得分上优于大多数基线，展示了其在交错视觉-文本-动作学习上的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的EO-1模型在统一架构和交错式多模态预训练方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，模型在复杂动态环境中的实时交互与长期规划能力尚未充分验证，其推理-行动交错机制在高度不确定或突发干扰场景下的鲁棒性有待进一步测试。其次，当前训练数据虽规模庞大，但主要基于静态标注和有限的任务类型，缺乏开放世界中主动探索、试错学习以及人类演示中隐含的物理常识与直觉的数据，这限制了模型对未知物体和复杂物理交互的泛化能力。此外，模型参数量为3B，相较于通用大模型仍较小，未来可探索扩展模型规模与数据多样性，并引入更高效的多模态对齐机制。从方法改进角度看，可结合世界模型与强化学习，使模型不仅能生成动作，还能预测动作后果并进行自我修正；同时，引入分层决策框架，将高层语义规划与底层运动控制更紧密耦合，以处理更长期的复杂任务。最后，模型的实际部署效率、计算开销以及安全性与可解释性也是未来需要重点攻关的实用化方向。

### Q6: 总结一下论文的主要内容

该论文提出了EO-Robotics框架，其核心是EO-1统一具身基础模型和EO-Data1.5M大规模高质量数据集，旨在解决开放世界中通用机器人控制所面临的多模态推理与物理交互交织的挑战。现有视觉-语言-动作模型通常将动作生成置于序列末端，忽略了模态间动态的因果依赖，导致泛化能力有限。

论文的核心贡献在于：1）提出了一种统一架构，采用仅解码器的Transformer，通过自回归解码和流匹配去噪的协同训练，无缝处理图像、文本、视频和动作等混合模态输入，无需引入额外的动作专用参数。2）构建了包含超过150万样本的EO-Data1.5M数据集，该数据集通过整合网络视觉-语言数据和真实机器人轨迹，并利用VLM和人工标注时空问答对，形成了交织的视觉-文本-动作序列，以促进细粒度几何和时空表征学习。

主要结论是，这种交织的多模态预训练范式使EO-1在多种长视野、灵巧操作任务中展现出卓越的开放世界理解和泛化能力。实验验证了其在多个具身推理和机器人控制基准上的优越性能，表明统一的建模方法能有效实现推理与行动的灵活整合，为发展先进的具身基础模型提供了重要见解。
