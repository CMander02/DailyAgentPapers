---
title: "WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces"
authors:
  - "Sicheng Fan"
  - "Rui Wan"
  - "Yifei Leng"
  - "Gaoning Liang"
  - "Li Ling"
date: "2026-03-05"
arxiv_id: "2603.05295"
arxiv_url: "https://arxiv.org/abs/2603.05295"
pdf_url: "https://arxiv.org/pdf/2603.05295v1"
categories:
  - "cs.AI"
  - "cs.CV"
tags:
  - "Tool Use & API Interaction"
  - "Web & Browser Automation"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Web & Browser Automation"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Dual Mid-Training"
  primary_benchmark: "WebChainBench"
---

# WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces

## 原始摘要

We introduce WebChain, the largest open-source dataset of human-annotated trajectories on real-world websites, designed to accelerate reproducible research in web agents. It contains 31,725 trajectories and 318k steps, featuring a core Triple Alignment of visual, structural, and action data to provide rich, multi-modal supervision. The data is collected via a scalable pipeline that ensures coverage of complex, high-value tasks often missed by synthetic methods. Leveraging this dataset, we propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on our proposed WebChainBench and other public GUI benchmarks. Our work provides the data and insights necessary to build and rigorously evaluate the next generation of scalable web agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决构建和评估下一代可扩展网络智能体（Web Agent）所面临的核心瓶颈问题：缺乏大规模、高质量、真实世界的人类交互轨迹数据。研究背景是，网络浏览器作为数字任务的主要界面，其自动化（即GUI智能体）具有极高价值。尽管视觉-语言-动作模型取得了进展，但网络环境的复杂动态性以及高质量轨迹数据的稀缺，严重阻碍了智能体在空间定位、鲁棒推理和长时程规划方面的发展。

现有方法存在显著不足。开源的人类标注数据集通常规模有限、完整性不足，无法验证模型的缩放效应。而合成数据方法虽然成本较低，但受限于安全机制（如反机器人检测、验证码、需个人认证的登录场景），无法捕捉真实、高价值的用户工作流程。此外，许多重要研究依赖非公开的专有数据集，导致关键发现无法复现，阻碍了社区共识的形成和领域的整体进步。

因此，本文要解决的核心问题是：为网络智能体研究提供一个大规模、开源、高质量的真实世界人类交互轨迹数据集，以打破数据垄断，并基于此数据集探索有效的模型训练方法。具体而言，论文引入了WebChain数据集，它通过可扩展的收集流程确保了数据的规模、多样性和对复杂任务的覆盖，并提出了“三重对齐”机制来提供丰富的多模态监督。基于此，论文进一步提出了解耦空间定位与规划的“双中期训练”方法，以推动网络智能体性能的提升。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕网页智能体（Web Agent）的训练与评估环境、数据收集方法以及模型技术路线展开，可分为以下几类：

**1. 训练与评估环境**：早期研究依赖于合成、沙盒环境（如MiniWoB++），虽任务可控但无法反映真实网页的视觉与结构噪声。为弥合差距，近期工作引入了更真实的执行环境，例如WebArena和VisualWebArena，它们托管了可复现的网站，但仍存在“模拟鸿沟”，缺乏实时网页的动态DOM结构、广告和视觉杂乱。本文的WebChain则直接在真实、多样化的实时网站上收集数据，填补了这一空白。

**2. 数据驱动方法**：为获取真实交互数据，相关研究从实际应用中挖掘交互轨迹。Rico在移动UI领域开创了先河，而Mind2Web和WebLINX将其扩展到网页领域，提供了大规模的离线轨迹。然而，这些数据集在规模上仍不足以系统验证现代GUI智能体模型的缩放效应。本文的WebChain通过可扩展的人工标注流程，提供了目前最大规模的人类标注轨迹数据集，特别涵盖了合成方法难以捕获的需身份验证的复杂、高价值任务。

**3. 模型技术路线**：GUI智能体的范式已从基于DOM的语言模型转向感知像素的视觉-语言-动作（VLA）模型。早期方法依赖解析HTML文本，但常受限于复杂页面的上下文长度。近期进展利用通用VLM（如GPT-4V）和专用UI模型（如SeeAct, CogAgent），通过截图来感知布局和视觉线索。尽管有进步，VLM在密集、杂乱的页面上仍存在空间幻觉和 grounding 错误，这很大程度上源于缺乏将高层意图与精确边界框和DOM元素对齐的细粒度标注数据。本文通过提供密集、经过验证的空间标注（Triple Alignment）来应对此挑战，并在实验中展示了如何解耦空间 grounding 与规划。

**4. 训练策略**：监督微调（SFT）是训练网页智能体的主流策略，但存在分布偏移问题。强化学习（RL）提供了优化长期任务成功的替代方案，但在开放网页任务中面临奖励稀疏和探索空间巨大的挑战。本文提出的Dual Mid-Training方法，利用高质量SFT初始化（通过思维链增强的中期训练）为有效的RL微调提供了稳定的基础，从而在长视野基准测试中取得了先进性能。

### Q3: 论文如何解决这个问题？

论文通过构建大规模、高质量的真实世界网页交互轨迹数据集WebChain，并基于此提出一种创新的“双中期训练”方法来解决提升网页智能体能力的问题。其核心方案分为数据构建和模型训练两大支柱。

在数据层面，论文设计了一个三阶段、可扩展的管道来创建WebChain数据集。首先，通过**结构化功能提取**，对目标网站进行静态分析，生成一个定义精确可执行边界的模式，确保后续任务生成的可行性。接着，进行**模式约束的任务生成**，利用大语言模型在该模式的约束下合成大量、分层级的复杂任务，涵盖简单信息检索、多约束导航和条件依赖任务。然后，通过**人在回路轨迹收集**，让标注员使用专用工具完成任务，并被动、详尽地记录每一步的多模态交互痕迹，包括DOM快照、具体动作、高保真空间信息（如坐标、边界框）和元素元数据。最后，通过**后处理上下文增强**来提升数据效用：一是**视觉定位密集化**，为每个状态提取屏幕上所有交互元素的边界框等信息，将任务转化为密集的、感知布局的分割问题；二是**合成推理链生成**，利用视觉语言模型为每个动作生成解释其选择理由的自然语言推理轨迹，为智能体提供规划监督信号。由此产生的数据集规模空前，且具备视觉、结构、动作数据的“三重对齐”，提供了丰富的多模态监督。

在模型训练方法上，论文的核心创新是**双中期训练范式**，其关键思想是将空间定位与长期规划这两个挑战解耦，分阶段进行专项训练，为最终的强化学习优化奠定坚实基础。整体框架首先对基础视觉语言模型进行两种并行的中期训练：1. **空间定位导向的强化学习训练**：专注于给定截图和低级指令时，准确预测动作类型和参数（如点击坐标）。研究引入了视觉定位密集化数据增强和推理提示策略，以提升元素识别和减少空间幻觉。2. **思维链监督微调**：利用数据集中合成的推理链，训练模型生成解释其决策过程的自然语言理由，从而显式地建模规划推理能力。完成这两种中期训练后，模型获得了稳健的空间感知和初步的规划能力。随后，进行**长期链导向的强化学习后训练**，在此阶段模型专注于在复杂、多步的任务中优化长期奖励。实验表明，这种解耦的训练策略显著优于标准的端到端监督方法，在论文提出的WebChainBench以及其他公开GUI基准测试中都达到了最先进的性能。该方法的核心优势在于，通过中期训练分别夯实了感知和推理的基础，使得最终的强化学习能够更高效地专注于长期奖励优化，从而实现了在复杂真实网页任务上的卓越表现和强大泛化能力。

### Q4: 论文做了哪些实验？

论文实验围绕验证WebChain数据集的有效性和提出的Dual Mid-Training训练方法展开。实验设置包括两个核心任务：**空间定位**（Spatial Grounding）和**长程规划**（Long-horizon planning），均在统一的奖励加权优化框架下进行。奖励由动作类型匹配和动作内容正确性两部分组成。

**数据集/基准测试**：主要使用论文提出的**WebChainBench (WCB)**，包含1.2k个交互步骤，分为WCB-S（空间定位）和WCB-L（长程规划）两个变体。同时，在多个公开GUI基准上评估泛化能力，包括**AndroidControl (AC-High/AC-Low)、GUI-Act-Web、GUI-Odyssey、OmniAct-Desktop/OA-Web**。

**对比方法**：比较了零样本模型（如Qwen2.5-VL-3B/7B）、在其他数据集上训练的模型（如GUI-R1-3B/7B）以及在WebChain上训练的不同变体模型。WebChain训练模型包括基础LCRL版本，以及增加了思维链监督微调（CoT-SFT）和空间定位强化学习训练（SGRL）的增强版本。

**主要结果与关键指标**：
1.  **数据规模影响**：在WCB-L上，使用完整数据集（150k步骤）训练的Qwen2.5-VL-3B模型，其成功率显著高于仅使用4k步骤的基线，证实了数据规模对长程规划能力的重要性。
2.  **空间定位优化**：在WCB-S上，结合视觉定位稠密化（VGD）和推理提示（RP）的策略取得了最佳性能。例如，WebChain-LCRL-7B模型结合SGRL和CoT-SFT后，在多个基准的“Type”和“GR”指标上表现优异。
3.  **双阶段训练有效性**：提出的Dual Mid-Training（SGRL + CoT-SFT）能有效解耦空间感知与规划。在WCB-L上，采用此范式初始化的模型进行LCRL后训练，取得了最佳长程规划性能。具体地，WebChain-LCRL-7B模型结合SGRL和CoT-SFT后，在WCB-L上的整体性能达到81.4%，显著高于基线。
4.  **跨基准泛化**：在WebChain上训练的模型在全部六个公开基准测试中均取得了领先或极具竞争力的性能。例如，在OmniAct-Desktop上，“Type”准确率最高达99.7%，“SR”达86.8%；在AndroidControl-High上，“SR”达61.8%。这证明了模型强大的零样本迁移能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的WebChain数据集和双阶段训练方法为网页智能体研究提供了重要基础，但仍存在一些局限性和可探索方向。首先，数据集的覆盖范围虽广，但主要基于特定采集管道，可能未充分涵盖某些高度动态或需复杂逻辑推理的交互场景（如涉及多步骤验证或跨域任务）。其次，当前方法将空间定位与规划解耦，但两者在复杂任务中可能存在紧密耦合，未来可探索更动态的集成机制，例如引入实时反馈循环或基于强化学习的自适应决策模块。此外，数据标注依赖人工，成本较高且可能引入主观偏差，未来可结合半自动标注或合成数据增强技术，在保证质量的同时扩展数据多样性。从技术角度看，模型的多模态对齐仍可深化，例如引入跨模态注意力机制以更好地融合视觉、结构和动作信息。最后，评估基准WebChainBench虽聚焦长视野任务，但可进一步纳入对鲁棒性、泛化能力和安全性的测试，推动智能体在真实开放环境中的实用化部署。

### Q6: 总结一下论文的主要内容

这篇论文提出了WebChain，一个大规模、开源的真实世界网页交互轨迹数据集，旨在推动网页智能体研究的可复现性。其核心问题是现有网页智能体研究缺乏高质量、大规模且与真实用户行为对齐的多模态数据，导致评估受限且难以泛化到复杂任务。

论文的核心贡献是构建了包含31,725条轨迹和31.8万步交互的WebChain数据集。其方法的关键在于设计了一个可扩展的数据收集流程，获取了涵盖复杂高价值任务的真实用户交互轨迹，并首创了“视觉、结构、动作”三重对齐的数据模式，提供了丰富的多模态监督信号。基于此数据集，作者进一步提出了一种“双阶段中期训练”方法，将空间定位与任务规划解耦，从而在作者提出的WebChainBench及其他公开GUI基准测试中取得了最先进的性能。

主要结论是，WebChain数据集及其配套的训练方法为构建和严格评估下一代可扩展的网页智能体提供了必要的数据基础和有效见解，显著提升了智能体在真实、复杂网页任务上的表现。
