---
title: "CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning"
authors:
  - "Yuxuan Liu"
  - "Weikai Xu"
  - "Kun Huang"
  - "Changyu Chen"
  - "Jiankun Zhao"
date: "2026-02-27"
arxiv_id: "2602.24142"
arxiv_url: "https://arxiv.org/abs/2602.24142"
pdf_url: "https://arxiv.org/pdf/2602.24142v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Architecture & Frameworks"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Channel-of-Mobile-Experts (CoME), output-oriented activation, progressive training (Expert-FT, Router-FT, CoT-FT), InfoGain-Driven DPO (Info-DPO)"
  primary_benchmark: "AITZ, AMEX"
---

# CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning

## 原始摘要

Mobile Agents can autonomously execute user instructions, which requires hybrid-capabilities reasoning, including screen summary, subtask planning, action decision and action function. However, existing agents struggle to achieve both decoupled enhancement and balanced integration of these capabilities. To address these challenges, we propose Channel-of-Mobile-Experts (CoME), a novel agent architecture consisting of four distinct experts, each aligned with a specific reasoning stage, CoME activates the corresponding expert to generate output tokens in each reasoning stage via output-oriented activation. To empower CoME with hybrid-capabilities reasoning, we introduce a progressive training strategy: Expert-FT enables decoupling and enhancement of different experts' capability; Router-FT aligns expert activation with the different reasoning stage; CoT-FT facilitates seamless collaboration and balanced optimization across multiple capabilities. To mitigate error propagation in hybrid-capabilities reasoning, we propose InfoGain-Driven DPO (Info-DPO), which uses information gain to evaluate the contribution of each intermediate step, thereby guiding CoME toward more informative reasoning. Comprehensive experiments show that CoME outperforms dense mobile agents and MoE methods on both AITZ and AMEX datasets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动智能体在执行用户指令时，如何有效实现混合能力推理的问题。研究背景是，随着多模态大语言模型的发展，移动智能体正从端到端预测转向逐步推理的新范式，以提升动作决策的准确性和鲁棒性。这种混合能力推理通常需要依次完成屏幕状态感知、子任务规划、高层动作决策和底层动作函数执行等多个维度的能力。

现有方法存在明显不足。一方面，现有的移动智能体要么在特定任务数据集上增强单项能力（如屏幕理解或动作定位），但缺乏多种能力的有效整合；要么在大规模数据集上进行预训练，这容易导致不同能力的发展不平衡。总之，缺乏对多种能力进行解耦增强与平衡整合的有效方法。另一方面，虽然混合专家模型通过输入导向的激活实现了部分能力解耦，但理想的混合能力推理要求专家激活与生成每个输出令牌时所需的推理阶段能力对齐，这种输出导向的激活与MoE的设计并不兼容。

因此，本文要解决的核心问题是：如何设计一种新的智能体架构和训练方法，以实现对混合能力推理中各项能力的解耦增强、平衡整合，并缓解多阶段推理中的错误传播问题。为此，论文提出了Channel-of-Mobile-Experts架构、渐进式训练策略以及基于信息增益的DPO方法。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为移动智能体（Mobile Agents）和专家混合（Mixture-of-Experts, MoE）两大类。

在**移动智能体**方面，相关研究旨在通过API调用或动作模拟自主执行用户指令。早期工作通过引入先验探索阶段或设计特定任务（如屏幕理解、控件识别、界面转换和元素/动作定位）来为智能体注入移动知识。随着多模态大语言模型（MLLMs）的发展，一些研究设计了多阶段或多智能体的框架。近期，更多工作通过在大规模混合数据上进行预训练或微调来构建通用移动智能体。然而，现有智能体在能力解耦与平衡整合方面仍存在不足。本文提出的CoME正是为了应对这一挑战，通过一种新颖的专家架构专门针对混合能力推理（HCR）进行优化。

在**专家混合（MoE）方法**方面，MoE通过集成多个专家并动态路由输入来处理多样化任务。近期研究已将MoE集成到LLMs和MLLMs中，通过将前馈网络层扩展为多个专家并为每个输入token激活Top-K专家，以提升模型容量和效率。首个MoE GUI智能体AriaUI展示了MoE在移动自动化中的潜力。然而，传统的MoE依赖于**面向输入的激活**机制，这对于需要分阶段推理的HCR并非最优。与此相对，本文的CoME采用了**面向输出的激活**机制，使专家激活与特定的推理阶段（如屏幕摘要、子任务规划等）对齐，从而实现了更好的阶段匹配与能力整合。此外，本文还提出了渐进式训练策略和信息增益驱动的DPO，以进一步增强能力并缓解错误传播，这些是区别于现有MoE方法的关键创新。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为CoME（Channel-of-Mobile-Experts）的新型智能体架构，结合渐进式训练策略和基于信息增益的优化方法，来解决移动智能体在混合能力推理中面临的解耦增强与平衡整合难题。

**核心架构设计**：CoME采用了一种输出导向激活的专家混合架构。它在Transformer的每一层中扩展了前馈网络模块，引入了四个独立的专家，分别对应混合能力推理的四个阶段：屏幕摘要（$\mathcal{E}_{ss}$）、子任务规划（$\mathcal{E}_{sp}$）、动作决策（$\mathcal{E}_{ad}$）和动作函数调用（$\mathcal{E}_{af}$）。这些专家共享同一套自注意力模块。与传统的基于输入激活的MoE不同，CoME的关键创新在于其**输出导向激活机制**。模型通过一个通道路由器，根据当前推理阶段的需要，从对应的专家通道中选择性地融合隐藏状态，从而生成最终的输出令牌。这确保了在推理轨迹的每个特定阶段，都由最匹配该阶段能力需求的专家主导生成过程。

**渐进式训练策略**：为了赋予CoME强大的混合能力推理能力，论文设计了一个三阶段的渐进式训练策略：
1.  **专家微调**：首先，使用特定能力的数据集分别独立训练四个专家，实现不同能力的解耦和专门化增强。
2.  **路由器微调**：接着，在标注了各输出令牌所属推理阶段（即应激活的专家）的数据上，训练通道路由器，使其学会将专家激活与正确的推理阶段对齐。
3.  **思维链微调**：最后，在完整的混合能力推理数据上进行微调，并加入路由器归一化损失作为正则项，以促进不同专家之间的无缝协作与平衡优化。

**关键技术：信息增益驱动的DPO**：为了缓解多步推理中的错误传播问题，论文提出了InfoGain-Driven DPO方法。其核心思想是利用**信息增益**来评估每个中间推理步骤对最终动作的贡献度。具体而言，训练一系列奖励模型来估计在给定之前所有推理步骤的条件下，最终动作的概率。当前步骤的信息增益即定义为该概率相对于前一步骤的增量。在构建DPO数据时，不仅考虑最终动作的准确性奖励，还将各阶段信息增益的乘积作为推理质量奖励。通过优化结合了信息增益奖励和准确性奖励的DPO目标，模型被引导生成每一步都具有高信息贡献、逻辑连贯的推理轨迹。

综上所述，CoME通过其独特的输出导向专家架构、系统的渐进训练流程以及创新的基于信息增益的强化学习优化，有效地实现了移动智能体所需多种能力的解耦、增强与协同，从而提升了混合能力推理的整体性能。

### Q4: 论文做了哪些实验？

论文在AITZ和AMEX两个移动代理基准数据集上进行了全面的实验。实验设置方面，CoME模型包含四个专家，激活参数量为5B，并采用渐进式训练策略（Expert-FT、Router-FT、CoT-FT）和信息增益驱动的DPO（Info-DPO）进行优化。

主要对比方法涵盖了密集模型（如Qwen2VL、ShowUI、UITars、GUI-R1、SeeClick、UGround、OS-Atlas、SphAgent、UI-S1）和稀疏MoE模型（如MolmoE、Qwen2VL-MoE、AriaUI、DeepSeekVL2），参数量从1B到7B不等。评估指标为动作类型和匹配的准确率。

主要结果显示，在AITZ数据集上，CoME取得了最高的整体动作匹配准确率（66.98%），相比2B系列密集模型提升11.35%，相比7B系列模型提升1.57%，并超越MoE模型3.42%。在更具挑战性的CLICK动作上达到65.22%（+1.45%），且动作类型间的性能更均衡（偏差4.41）。在AMEX数据集涵盖的九个应用上，CoME整体准确率达72.61%，超越最佳密集模型1.90%，超越最佳MoE模型8.05%。

消融实验表明，Info-DPO对性能提升贡献最大（AITZ上+4.68%），Router-FT和Expert-FT的移除分别导致准确率下降4.08%和4.36%。进一步分析显示，CoME在各推理阶段（屏幕摘要、子任务规划、动作决策、动作执行）上表现均衡，专家激活与推理阶段对齐的准确率达99%，显著优于MoE模型。在辅助GUI任务（Caption、OCR、Grounding）上也具有竞争力。效率方面，CoME（5B）在训练和推理时的GPU内存占用（18.52GB和11.69GB）低于对比的7B密集模型和激活3B的MoE模型，同时取得了更高的准确率。

### Q5: 有什么可以进一步探索的点？

该论文提出的CoME架构在移动智能体混合能力推理上取得了进展，但仍存在一些局限性和可探索方向。首先，其实验主要基于特定数据集（AITZ和AMEX），在更复杂、动态的真实移动环境（如多应用切换、网络延迟干扰）中的泛化能力有待验证。其次，专家模块的设计虽然实现了能力解耦，但可能增加了模型复杂性和推理延迟，未来可研究更轻量化的专家结构或动态专家选择机制。此外，Info-DPO方法依赖于信息增益评估中间步骤，但信息增益的计算可能受限于预设的奖励模型或标注数据，未来可探索更鲁棒的无监督或自监督评估方式。结合领域趋势，可能的改进包括：引入跨任务元学习来增强专家模块的适应能力；探索多模态输入（如语音指令结合屏幕内容）以提升交互自然性；或将CoME与具身推理框架结合，拓展到机器人操作等物理世界任务中。这些方向有望进一步提升智能体在复杂场景下的稳健性和实用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为CoME的新型移动智能体架构，旨在解决现有智能体在混合能力推理（包括屏幕摘要、子任务规划、行动决策和行动执行）中难以实现能力解耦增强与平衡整合的问题。其核心贡献是设计了一个由四个独立专家组成的架构，每个专家对应一个特定的推理阶段，并通过面向输出的激活机制在相应阶段调用专家生成输出。方法上，论文引入了渐进式训练策略：Expert-FT用于解耦和增强各专家能力；Router-FT使专家激活与推理阶段对齐；CoT-FT促进多能力间的无缝协作与平衡优化。此外，为减少推理中的错误传播，作者提出了InfoGain-Driven DPO方法，利用信息增益评估中间步骤的贡献，从而引导模型进行信息量更丰富的推理。实验结果表明，CoME在AITZ和AMEX数据集上均优于现有的密集模型和混合专家方法，证明了其在移动智能体混合能力推理任务上的有效性和先进性。
