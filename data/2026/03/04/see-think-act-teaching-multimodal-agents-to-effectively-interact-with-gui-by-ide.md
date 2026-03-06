---
title: "See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles"
authors:
  - "Zongru Wu"
  - "Rui Mao"
  - "Zhiyuan Tian"
  - "Pengzhou Cheng"
  - "Tianjie Ju"
  - "Zheng Wu"
  - "Lingzhong Dong"
  - "Haiyue Sheng"
  - "Zhuosheng Zhang"
  - "Gongshen Liu"
date: "2025-09-17"
arxiv_id: "2509.13615"
arxiv_url: "https://arxiv.org/abs/2509.13615"
pdf_url: "https://arxiv.org/pdf/2509.13615v4"
github_url: "https://github.com/ZrW00/StaR"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.HC"
tags:
  - "Multimodal Agent"
  - "GUI Interaction"
  - "Agent Reasoning"
  - "State Awareness"
  - "Agent Benchmark"
  - "Tool Use"
  - "Agent Architecture"
relevance_score: 8.5
---

# See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles

## 原始摘要

The advent of multimodal agents facilitates effective interaction within graphical user interface (GUI), especially in ubiquitous GUI control. However, their inability to reliably execute toggle control instructions remains a key bottleneck. To investigate this, we construct a state control benchmark with binary toggle instructions derived from public datasets. Evaluation results of existing agents demonstrate their notable unreliability, particularly when the current toggle state already matches the desired state. To address the challenge, we propose State-aware Reasoning (StaR), a multimodal reasoning method that enables agents to perceive the current toggle state, infer the desired state from the instruction, and act accordingly. Experiments on four multimodal agents demonstrate that StaR can improve toggle instruction execution accuracy by over 30\%. Further evaluations on three public agentic benchmarks show that StaR also enhances general agentic task performance. Finally, evaluations on a dynamic environment highlight the potential of StaR for real-world applications. Code and benchmark: https://github.com/ZrW00/StaR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态智能体在图形用户界面（GUI）中执行“开关”（toggle）控制指令时不可靠的问题。研究背景是，随着多模态大语言模型（MLLMs）的发展，多模态智能体能够感知、推理并与GUI交互，成为灵活的人机交互助手。然而，在GUI中无处不在的开关控件（如按钮、切换开关、复选框）是实现二进制状态切换（如开/关）的基础交互机制，现有智能体在执行这类开关指令时准确率很低（多数低于50%），成为影响其可靠性和应用的关键瓶颈。

现有方法的不足主要体现在两个方面：一是智能体经常出现两种典型错误：当当前状态与期望状态不同时未能执行切换（假阴性），以及当前状态已符合期望时仍多余地执行切换（假阳性）。这些错误在精度要求高的应用中可能导致任务失败。二是现有改进思路（如精心设计提示词引导智能体检查状态，或引入额外的注释器智能体进行协作）效果有限：提示方法难以从根本上提升智能体的推理能力；而引入注释器则存在悖论——若注释器本身能可靠识别状态，那它直接作为执行智能体更高效，否则它同样不可靠。

因此，本文要解决的核心问题是：如何提升多模态智能体的内在推理能力，使其能够准确感知、推理并执行开关控制指令。为此，论文提出了“状态感知推理”（State-aware Reasoning, StaR）方法，通过教导智能体明确执行三个步骤：从屏幕截图中感知当前开关状态、从用户指令中推断期望状态、并通过比较两者来决定是否执行切换动作，从而将明确的状态感知整合到推理过程中，以提升执行的准确性和可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态智能体的推理、GUI交互以及GUI开关交互三个方面展开。

在**多模态智能体推理方法**方面，相关工作致力于提升智能体的决策准确性和可解释性。例如，CoAT推理通过引入语义标注和中间推理链来提高动作执行精度。后续研究则通过额外训练来强化推理过程，以提升多模态智能体进行GUI交互的内在推理能力。本文提出的状态感知推理（StaR）方法，正是对这些工作的深化和细化，专注于改进智能体对关键开关控制指令的感知、推理和执行的内在能力。

在**面向GUI交互的多模态智能体**方面，现有研究可分为两类：一是基于闭源大语言模型（MLLM）通过提示工程构建的智能体，如AppAgent系列和Mobile-Agent v1/v2；二是基于进一步训练的开源MLLM构建的智能体，如OS-Atlas、Aguvis、Mobile-Agent v3等。研究通过预训练、在智能体基准上微调等方式持续改进这些智能体。然而，尽管它们在感知和行动上取得了成功，大多数工作仍缺乏处理细粒度GUI开关控制的有效推理机制，这正是本文旨在解决的核心问题。

在**GUI开关交互**方面，由于开关状态识别的视觉细粒度特性，准确识别具有挑战性。先前工作通常依赖外部标注器（如辅助多模态智能体、OminiParser等解析器或人工反馈）来提供显式的状态信息，以用于下游推理和决策。这种方法引入了额外的复杂性。相对而言，很少有工作专注于提升多模态智能体准确感知、推理和执行开关控制指令的内在能力，本文的StaR方法正是针对这一空白提出的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“状态感知推理”（StaR）的多模态推理方法来解决多模态代理在GUI切换控制中不可靠的问题，特别是在当前切换状态已符合指令要求时容易出错的情况。该方法的核心是模拟人类执行切换指令时的结构化思维过程，并将其嵌入到代理的推理链中。

整体框架与主要模块设计如下：StaR将推理过程明确划分为三个步骤，对应三个关键模块。第一步是“感知”模块：引导代理从屏幕截图中识别出当前切换状态（σ），通过将视觉特征与细粒度的切换状态（如开/关）相关联，实现准确的状态感知。第二步是“分析”模块：引导代理从文本指令中推断出期望的目标状态（σ_u）。对于肯定指令（如“打开”），期望状态与当前状态不同；对于否定指令（如“不要关闭”），期望状态与当前状态相同。第三步是“决策”模块：引导代理比较当前状态σ与期望状态σ_u，并据此决定最终动作——若两者不同则预测执行点击（CLICK）操作，若相同则预测任务已完成（COMPLETED）。这种分步推理架构使代理能明确地进行状态比对，从而避免不必要的冗余操作。

在技术创新点上，论文不仅通过提示工程来引导这一推理过程，还进一步对多模态代理进行了针对性训练以固化该能力。具体而言，作者在构建的状态控制基准训练集上训练代理学习StaR推理过程。同时，为了保持代理在通用智能体任务上的性能，论文还对包含切换控制指令的通用智能体基准数据进行了标注与推理链细化，将其与原始的其他任务数据一同用于训练。这种混合训练策略使代理能自适应地对切换指令应用StaR推理，而对其他任务保持原有的推理方式，从而在显著提升切换控制精度的同时不损害其通用任务性能。实验表明，该方法能将切换指令执行准确率提升超过30%，并在动态环境中展现出实际应用潜力。

### Q4: 论文做了哪些实验？

本论文进行了四组核心实验，以评估所提出的状态感知推理（StaR）方法的有效性。

**实验设置**：研究在四个具有不同历史建模策略的多模态智能体上评估StaR，包括OS-Atlas-7B、UI-TARS-7B、AgentCPM-GUI-8B和GUI-Owl-7B。所有智能体均使用其原始提示和格式进行微调，训练采用LLaMA-Factory框架，学习率为5e-6，共3个epoch。

**数据集与基准测试**：
1.  **状态控制基准**：一个专门构建的二元开关指令基准，用于核心评估。
2.  **通用智能体基准**：使用AndroidControl（分H/L两种设置）、AITZ和GUI-Odyssey的测试集来评估通用任务性能。
3.  **动态评估基准**：构建了一个包含20个真实世界开关控制任务的动态环境，基于AndroidStudio模拟器和AndroidWorld框架。

**对比方法**：将StaR训练后的智能体与以下基线进行比较：
1.  **零样本**：未经StaR训练的原始智能体。
2.  **StaR风格提示**：通过结构化提示引导智能体进行类似StaR的推理，但不进行训练。

**主要结果与关键指标**：
1.  **在状态控制基准上**：StaR训练显著提升了开关指令执行准确率。关键指标包括整体动作匹配率（O-AMR）、正例动作匹配率（P-AMR）和负例动作匹配率（N-AMR）。例如，StaR将OS-Atlas-7B的O-AMR提升了35.77%，UI-TARS-7B提升了30.41%。同时，负例误触发率（N-FPTR）和负例误报率（N-FPR）大幅下降，有效缓解了误触发问题。StaR训练的效果远超单纯的StaR风格提示。
2.  **在通用智能体基准上**：StaR在保持或提升通用任务性能的同时，在复杂长链任务（如GUI-Odyssey）上带来显著提升。例如，UI-TARS-7B在GUI-Odyssey上的任务成功率（TSR）提升了7.14%到20.17%。
3.  **在动态评估基准上**：StaR训练一致提高了在动态环境中的任务成功率。关键指标为最终任务成功率（范围[0,1]）。例如，OS-Atlas-7B的成功率从10%大幅提升至55%，UI-TARS-7B从35%提升至40%，AgentCPM-GUI-8B从20%提升至42.5%，证明了其现实应用潜力。

### Q5: 有什么可以进一步探索的点？

该论文提出的StaR方法在提升多模态代理执行二元开关指令的可靠性方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，研究主要聚焦于静态截图中的“二元”开关状态识别，而现实GUI环境中的状态往往更复杂（如多档位滑块、连续值调节），未来可扩展至多状态或连续状态的控制任务。其次，当前方法依赖于对当前状态的显式感知和推理，但在动态、实时交互环境中（如视频流或连续操作），代理需具备状态追踪和时序推理能力，这要求模型能处理时间维度的信息。此外，StaR的泛化性虽在多个基准上得到验证，但其在跨领域、跨应用（如从桌面软件到移动端或游戏界面）的迁移能力尚未充分探索，可研究领域自适应或元学习技术以提升鲁棒性。从方法改进角度，可考虑将状态感知与动作规划更紧密集成，例如引入强化学习框架，让代理通过试错学习优化决策链；或结合大语言模型的推理能力，生成更精细的中间步骤解释，以提升可解释性和错误调试效率。最后，实际应用中用户指令可能模糊或隐含状态信息，未来可探索结合上下文历史或对话交互的主动查询机制，使代理能更智能地处理不确定性。

### Q6: 总结一下论文的主要内容

该论文针对多模态智能体在图形用户界面（GUI）交互中执行切换指令时可靠性不足的问题展开研究。作者首先构建了一个基于公开数据集的二元切换指令状态控制基准测试，发现现有智能体在执行切换指令时表现不稳定，尤其是在当前状态已符合目标状态时容易出错。为解决这一问题，论文提出了状态感知推理（StaR）方法，该方法引导智能体通过多模态推理感知当前切换状态、从指令推断目标状态，并据此执行相应操作。实验表明，StaR 在四种多模态智能体上将切换指令执行准确率提升了超过 30%，并在三个公开的智能体基准测试中提升了通用任务性能。动态环境下的评估进一步验证了 StaR 在实际应用中的潜力。该研究的核心贡献在于揭示了切换状态识别对 GUI 交互可靠性的关键影响，并提出了一种简单有效的推理框架来提升智能体的执行准确性与泛化能力。
