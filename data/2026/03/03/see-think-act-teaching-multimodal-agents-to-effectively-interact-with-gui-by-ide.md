---
title: "See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles"
authors:
  - "Zongru Wu"
  - "Rui Mao"
  - "Zhiyuan Tian"
  - "Pengzhou Cheng"
  - "Tianjie Ju"
date: "2025-09-17"
arxiv_id: "2509.13615"
arxiv_url: "https://arxiv.org/abs/2509.13615"
pdf_url: "https://arxiv.org/pdf/2509.13615v3"
github_url: "https://github.com/ZrW00/StaR"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.HC"
tags:
  - "Reasoning & Planning"
  - "Perception & Multimodal"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "State-aware Reasoning (StaR)"
  primary_benchmark: "state control benchmark (constructed by the authors)"
---

# See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles

## 原始摘要

The advent of multimodal agents facilitates effective interaction within graphical user interface (GUI), especially in ubiquitous GUI control. However, their inability to reliably execute toggle control instructions remains a key bottleneck. To investigate this, we construct a state control benchmark with binary toggle instructions derived from public datasets. Evaluation results of existing agents demonstrate their notable unreliability, particularly when the current toggle state already matches the desired state. To address the challenge, we propose State-aware Reasoning (StaR), a multimodal reasoning method that enables agents to perceive the current toggle state, infer the desired state from the instruction, and act accordingly. Experiments on four multimodal agents demonstrate that StaR can improve toggle instruction execution accuracy by over 30\%. Further evaluations on three public agentic benchmarks show that StaR also enhances general agentic task performance. Finally, evaluations on a dynamic environment highlight the potential of StaR for real-world applications. Code and benchmark: https://github.com/ZrW00/StaR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态智能体在执行图形用户界面（GUI）中常见的“开关控制”指令时准确率低下的问题。研究背景是，随着多模态大语言模型（MLLMs）的发展，多模态智能体能够在无需API的情况下感知、推理并与GUI交互，成为提升人机交互效率的灵活助手。然而，在GUI中无处不在的开关控件（如切换按钮、滑动开关、复选框）是实现二进制状态改变（如开/关）的基础交互机制，现有智能体在执行这类简单的开关控制指令时却表现出显著的不可靠性。

现有方法的不足主要体现在两个方面：首先，论文构建了一个基于公开数据集的状态控制基准测试，评估发现现有智能体（包括GPT-5等）的执行准确率普遍低于50%。典型错误包括“假阴性”（当前状态与期望状态不同时未能执行切换）和“假阳性”（当前状态已符合期望时仍多余执行切换）。这些错误在精度要求高的应用中可能导致任务失败和严重问题。其次，针对此问题，常见的两种直观改进方法——通过精心设计的提示词引导智能体检查状态，或引入额外的注释器智能体进行多智能体协作——均存在局限。提示词方法难以从根本上提升智能体的推理能力；而引入注释器则面临悖论：若现有智能体本身无法可靠感知开关状态，则其作为注释器不可靠；若注释器足够可靠，则直接将其作为执行智能体更高效，从而避免了协作的复杂性和延迟。

因此，本文要解决的核心问题是：如何提升多模态智能体的内在推理能力，使其能够准确感知当前开关状态、从用户指令推断期望状态，并据此决定是否执行切换动作，从而可靠地执行开关控制指令。为此，论文提出了状态感知推理（StaR）方法，通过将显式的状态感知整合到推理过程中，教导智能体遵循“感知-推断-决策”的步骤，以消除对额外注释器的依赖，并显著提高开关执行的准确性和可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态智能体的推理、GUI交互以及GUI开关交互三个方面展开。

在**多模态智能体推理**方面，相关工作旨在提升智能体的决策准确性和可解释性。例如，CoAT推理通过引入语义标注和中间推理链来提高动作执行准确率。后续研究则通过额外训练来强化推理过程，以提升多模态智能体在GUI交互中的内在推理能力。本文提出的状态感知推理（StaR）方法正是对这些工作的深化，专注于改进智能体对开关控制指令的感知、推理和执行的内在能力。

在**GUI交互的多模态智能体**方面，现有工作可分为两类：一是基于专有MLLM并通过提示工程构建的智能体（如AppAgent系列、Mobile-Agent v1/v2）；二是基于进一步训练的开源MLLM构建的智能体（如OS-Atlas、Aguvis、OS-Genesis等）。尽管这些智能体在感知和行动上取得了进展，但大多仍缺乏处理精细GUI开关控制的有效推理机制。本文的StaR方法正是为了弥补这一不足。

在**GUI开关交互**方面，由于开关状态识别的视觉细粒度特性，准确识别具有挑战性。先前工作常依赖外部标注器（如辅助多模态智能体、OminiParser等解析器或人工反馈）来提供显式状态信息以辅助推理。然而，这引入了额外复杂性。本文则专注于提升多模态智能体自身准确感知、推理和执行开关控制指令的内在能力，与依赖外部标注的路径形成区别。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“状态感知推理（StaR）”的多模态推理方法来解决多模态代理在GUI切换控制中不可靠的问题，特别是在当前切换状态已符合指令要求时容易出错的瓶颈。该方法的核心是模拟人类执行切换指令的三步推理过程，并将其结构化地整合到代理的决策流程中。

整体框架设计上，StaR将推理链明确划分为三个主要模块：感知、分析和决策。在感知模块中，代理被引导从屏幕截图中识别当前切换状态σ，通过关联视觉特征与细粒度的切换状态（如开关的开启/关闭、复选框的选中/未选中）来实现准确的状态感知。在分析模块中，代理从自然语言指令中推断出期望状态σ_u；论文指出，对于肯定指令（如“打开开关”），期望状态与当前状态不同，而对于否定指令（如“不要关闭开关”），期望状态与当前状态相同。在决策模块中，代理比较σ和σ_u：若两者不同，则预测点击动作（CLICK）以执行切换；若相同，则预测任务已完成（COMPLETED），从而避免不必要的操作。

关键技术在于，论文不仅通过提示工程引导代理遵循这一三步推理，还进一步对多模态代理进行训练以学习StaR过程。具体而言，作者在状态控制基准的训练集上训练代理，使其内化状态感知推理。同时，为了保持代理在通用任务上的性能，作者还对包含切换控制指令的智能体基准数据进行了标注和推理链细化，将其与原始的其他任务推理过程结合，形成混合训练集。这种训练策略使代理能够自适应地对切换指令应用StaR，而对其他任务保留原有推理能力，从而在提升切换控制精度的同时不牺牲通用性能。

创新点主要体现在：一是首次将状态感知明确分解为可操作的推理步骤，解决了现有代理因忽略状态比对而盲目行动的问题；二是通过混合训练实现了专业化改进与泛化能力的平衡，使代理既能可靠处理切换指令，又能维持广泛的智能体任务性能。实验表明，该方法能将切换指令执行准确率提升30%以上，并在动态环境中展现出实际应用潜力。

### Q4: 论文做了哪些实验？

本文实验主要围绕验证所提出的状态感知推理（StaR）方法的有效性展开，涵盖实验设置、基准测试、对比方法和主要结果。

**实验设置与数据集**：实验在四个具有不同历史建模策略的多模态智能体上进行：OS-Atlas-7B、UI-TARS-7B、AgentCPM-GUI-8B 和 GUI-Owl-7B。所有智能体均使用其原始提示和格式进行微调。训练数据包括状态控制基准的训练集，以及 AndroidControl、AITZ 和 GUI-Odyssey 这三个包含长链复杂任务的基准训练集。测试评估则使用状态控制基准的测试集，以及 AndroidControl（分为仅高级目标的 H 设置和包含低级指令的 L 设置）、AITZ 和 GUI-Odyssey 的测试集。此外，为了评估真实世界适用性，研究还构建了一个包含20个真实世界切换控制任务的动态评估基准，该基准在 AndroidStudio 模拟器上实现。

**对比方法**：主要对比了三种设置下的智能体性能：1) **零样本（Zero-shot）**：未经 StaR 训练的原始智能体。2) **使用 StaR 风格提示（w/ StaR-style Prompting）**：通过结构化提示引导智能体进行 StaR 式推理。3) **使用 StaR 训练（w/ StaR Training）**：对智能体进行 StaR 方法微调。

**主要结果与关键指标**：
1.  **在状态控制基准上**：StaR 训练显著提升了切换指令的执行准确率。关键指标包括整体动作匹配率（O-AMR）、正例动作匹配率（P-AMR）和负例动作匹配率（N-AMR）。例如，OS-Atlas-7B 的 O-AMR 提升了 35.77%，UI-TARS-7B 提升了 30.41%。同时，N-AMR 大幅提升（OS-Atlas-7B 提升 60.68%），而负例误触发率（N-FPTR）和负例误报率（N-FPR）显著下降，有效减少了误触发。StaR 训练的效果显著优于仅使用 StaR 风格提示，证明了训练的必要性。
2.  **在通用智能体任务基准上**：StaR 训练在 AndroidControl、AITZ 和 GUI-Odyssey 上保持或提升了智能体的通用任务性能。特别是在涉及复杂长链任务的 GUI-Odyssey 基准上，所有四个评估指标（类型匹配率 TMR、动作匹配率 AMR、任务成功率 TSR、定位匹配率 GMR）均有接近 10% 的提升，任务成功率（TSR）提升幅度在 7.14% 到 20.17% 之间。
3.  **在动态环境评估中**：StaR 训练一致提高了任务成功率。例如，OS-Atlas-7B 的任务成功率从 10% 大幅提升至 55%，UI-TARS-7B 从 35% 提升至 40%，AgentCPM-GUI-8B 从 20% 提升至 42.5%，证明了 StaR 在真实世界应用中的潜力。

### Q5: 有什么可以进一步探索的点？

该论文提出的StaR方法虽有效提升了多模态代理在GUI切换任务中的可靠性，但仍存在一些局限和可拓展方向。首先，其基准测试主要针对二元切换指令，未来可扩展至更复杂的多状态控件（如滑块、下拉菜单）和连续操作序列，以评估代理在真实复杂场景下的泛化能力。其次，StaR依赖于静态截图进行状态感知，在动态或实时变化的界面中可能受限，未来可结合视频流或环境反馈实现更鲁棒的在线推理。此外，该方法未深入探索指令的模糊性处理，例如当用户指令隐含状态需求时，代理需结合常识进行推断，这为引入大语言模型的深层语义理解提供了方向。最后，StaR的评估集中于现有代理框架，未来可设计更轻量化的集成方案，降低计算开销，并探索其在跨平台、跨应用场景中的自适应能力，推动多模态代理向更通用、高效的人机交互方向发展。

### Q6: 总结一下论文的主要内容

该论文针对多模态智能体在图形用户界面（GUI）交互中执行切换指令时可靠性不足的问题展开研究。作者首先构建了一个基于公开数据集的二元切换指令状态控制基准测试，评估发现现有智能体在执行切换操作时表现不稳定，尤其是在当前状态已符合目标状态时容易出错。为解决这一问题，论文提出了状态感知推理方法，该方法引导智能体通过多模态推理来感知当前切换状态、从指令中推断目标状态，并据此采取相应行动。实验表明，该方法在四种多模态智能体上将切换指令执行准确率提升了超过30%，并在三个公开的智能体基准测试中提升了通用任务性能。动态环境下的评估进一步验证了该方法在实际应用中的潜力。该研究的核心贡献在于揭示了智能体执行切换指令的瓶颈，并提出了一种简单有效的推理框架，显著提升了交互的可靠性和实用性。
