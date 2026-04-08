---
title: "Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction"
authors:
  - "Yuzhe Zhang"
  - "Xianwei Xue"
  - "Xingyong Wu"
  - "Mengke Chen"
  - "Chen Liu"
  - "Xinran He"
  - "Run Shao"
  - "Feiran Liu"
  - "Huanmin Xu"
  - "Qiutong Pan"
  - "Haiwei Wang"
date: "2026-04-07"
arxiv_id: "2604.05477"
arxiv_url: "https://arxiv.org/abs/2604.05477"
pdf_url: "https://arxiv.org/pdf/2604.05477v1"
categories:
  - "cs.CL"
tags:
  - "GUI Agent"
  - "Robustness"
  - "Self-Correction"
  - "Action Verification"
  - "Training Pipeline"
  - "Android Benchmark"
relevance_score: 8.0
---

# Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction

## 原始摘要

Autonomous GUI agents based on vision-language models (VLMs) often assume deterministic environment responses, generating actions without verifying whether previous operations succeeded. In real-world settings with network latency, rendering delays, and system interruptions, this assumption leads to undetected action failures, repetitive ineffective behaviors, and catastrophic error accumulation. Moreover, learning robust recovery strategies is challenging due to the high cost of online interaction and the lack of real-time feedback in offline datasets.We propose VeriGUI (Verification-driven GUI Agent), which explicitly models action outcomes and recovery under noisy environments. VeriGUI introduces a Thinking--Verification--Action--Expectation (TVAE) framework to detect failures and guide corrective reasoning, and a two-stage training pipeline that combines Robust SFT with synthetic failure trajectories and GRPO with asymmetric verification rewards. We further construct a Robustness Benchmark based on AndroidControl to evaluate failure recognition and correction. Experiments show that VeriGUI significantly reduces failure loops and improves recovery success while maintaining competitive standard task performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于视觉语言模型（VLM）的自主图形用户界面（GUI）智能体在真实、动态环境中鲁棒性不足的核心问题。研究背景是GUI自动化已成为VLM的重要应用方向，智能体能够理解截图和自然语言指令，在移动设备上执行多步骤任务，并在标准基准测试上取得了快速进展。

然而，现有方法普遍存在一个根本性不足：它们隐含地假设每次发出的动作都会按预期确定性地执行成功。这一假设在实践中很少成立，因为真实环境存在网络延迟、渲染延迟和系统中断等噪声，可能导致动作失败。当失败发生时，现有智能体由于缺乏验证机制，会继续基于错误的进度假设进行操作，甚至无限重复相同的无效动作，形成执行死循环，造成资源浪费和错误累积。论文指出，这类“幂等性失败”（即失败动作未改变屏幕状态）并非极端情况，而是导致任务执行超时的主要原因。此外，训练鲁棒的恢复策略也面临挑战：在线强化学习因交互延迟和系统不稳定而成本高昂、难以扩展；而离线数据集又缺乏明确的动作失败反馈信号，无法有效指导恢复行为。

因此，本文要解决的核心问题是：如何让GUI智能体在充满不确定性的真实环境中，能够像人类一样，在执行动作后主动验证其效果，检测失败，并进行自我诊断与纠正，从而避免盲目操作和错误累积，实现鲁棒的自动化交互。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：基于视觉语言模型（VLM）的GUI智能体、强化学习（RL）在GUI自动化中的应用，以及处理执行失败的方法。

在**基于VLM的GUI智能体**方面，早期工作依赖HTML树或无障碍元数据等结构化界面表示，泛化能力有限。近期研究如CogAgent、SeeClick、ShowUI、Ferret-UI和UI-TARS等，利用VLM直接从屏幕截图进行视觉 grounding，实现了跨平台的泛化能力提升，并通过UI特定预训练和统一的视觉-语言-动作建模提高了效率。然而，这些方法通常假设每一步动作都能按预期执行，对于失败的处理多隐含在重规划（replanning）过程中。本文提出的VeriGUI则明确建模动作与效果的一致性，通过验证每个动作是否引发预期的视觉结果，实现了原理性的、步骤级的失败检测与恢复。

在**强化学习应用**方面，相关工作如DigiRL、DistRL在轨迹级进行优化，而UI-R1、InfiGUI-R1等则采用基于偏好的学习（如DPO）或Group Relative Policy Optimization（GRPO）框架，以提升鲁棒性和泛化能力，并整合反应式执行与深思熟虑的推理。但这些方法主要优化任务级成功率或代理步骤正确性。本文同样基于GRPO框架，但创新地将“动作-效果验证”作为核心的强化学习目标，使智能体能够学习诚实的自我监控和鲁棒的自我纠正。

在**处理执行失败**方面，先前工作多通过搜索、反思或执行反馈驱动的重规划来处理多步推理中的失败，这是一种隐式的、任务级的应对方式。本文则通过显式的步骤级验证（TVAE框架）和包含合成失败轨迹的两阶段训练流程，专门针对嘈杂环境中的动作失败进行建模和纠正，这与之前的工作有显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VeriGUI的验证驱动GUI智能体来解决环境不确定性问题。其核心是结合了闭环推理周期和两阶段训练流程，以系统性地培养验证驱动的自我纠正能力。

**核心方法与架构设计：**
VeriGUI的核心是一个结构化的推理过程，称为“思考-验证-行动-期望”（TVAE）框架。这并非一个线性链条，而是一个时间上链接的循环：在步骤t预测的“期望效果”（E_t）会成为步骤t+1的“验证”（V_t）假设。这种时间依赖性确保了跨步骤的因果一致性，使得错误无法被忽略或被后续动作覆盖。在每个步骤t，智能体依次产生四个结构化输出：1) **思考（T_t）**：使用显式标签（如[Verify]、[Recall]）进行结构化分析，在纠正错误时结构会转变为[Diagnose]和[Recovery]；2) **验证（V_t）**：一个二元判断，评估上一步动作是否成功（SUCCESS）或屏幕未发生变化（NO_CHANGE）；3) **行动（A_t）**：可执行的JSON格式动作；4) **期望效果（E_t）**：对屏幕将发生变化的预测，作为下一步的验证目标。

**两阶段训练流程与关键技术：**
1.  **第一阶段：鲁棒监督微调（Robust SFT）**：为了教授错误识别，构建了一个混合数据集，包含正样本（成功轨迹）和合成的负样本（失败恢复轨迹）。通过GPT-4o为两种类型生成结构化的思维链注释，并使用标准交叉熵损失进行训练。这一阶段建立了必要的行为先验，防止模型过度拟合所有动作都会成功的乐观假设。
2.  **第二阶段：基于组相对策略优化的强化学习（GRPO）**：此阶段采用GRPO和专门的奖励机制，仅使用离线数据模拟在线反馈。关键创新在于**隐式环境模拟**策略：利用GUI错误的幂等性属性（错误动作通常使屏幕保持不变），将离线轨迹转化为具有环境反馈信号的训练样本，无需任何实时交互。奖励函数由三部分组成：**动作奖励（R_act）** 衡量执行正确性；**效果奖励（R_eff）** 评估预测期望效果与参考效果的语义一致性；**验证奖励（R_ver）** 通过不对称惩罚（成功匹配+1.0，误报-2.0，漏报-0.5）强制进行诚实的自我监控，其中对“幻觉”（误报）的严重惩罚迫使智能体将其内部信念与视觉现实对齐。优化采用GRPO算法，对一组输出计算归一化优势，并使用裁剪替代损失和KL散度惩罚进行策略更新。

**整体创新点：**
论文的主要创新在于将验证和期望效果预测显式地建模到GUI智能体的决策循环中，并通过结合合成失败轨迹的鲁棒SFT和利用隐式环境模拟与不对称验证奖励的GRPO两阶段训练，在完全离线的设置下有效地学会了故障识别与自我纠正，从而显著提升了在噪声环境下的鲁棒性。

### Q4: 论文做了哪些实验？

论文在离线与在线环境中进行了全面的实验评估。实验设置方面，作者基于Qwen2.5-VL-3B和Qwen2.5-VL-7B构建了VeriGUI-3B和VeriGUI-7B两个模型，采用两阶段训练流程：第一阶段（Robust SFT）使用学习率1e-5训练2个epoch，第二阶段（GRPO）使用学习率5e-6训练15个epoch，并设置了特定的奖励权重（α=0.5, β=0.5）。训练在8张A100 GPU上进行。离线评估采用了一种伪在线模拟方法：正确动作会跳转到真实下一屏幕，错误动作则返回未变化的屏幕。

使用的数据集和基准测试包括：AndroidControl-High（约1.5万训练轨迹和2500测试轨迹）、AITW-Gen、GUI Odyssey作为离线评估套件，以及MiniWoB++和AndroidWorld作为完全在线的真实环境。对比方法涵盖了3B规模模型（Qwen2.5-VL-3B、UI-R1-3B）、7B/8B规模模型（OS-Genesis-7B、OS-Atlas-7B、Qwen2.5-VL-7B、AgentCPM-GUI-8B、UI-TARS-7B、UI-S1-7B）以及闭源系统GPT-5.1和Gemini-3-flash。

主要结果如下：在AndroidControl-High上，VeriGUI-3B的类型匹配率（TM）达到72.2%，在3B开源模型中最高；VeriGUI-7B的TM为74.2%，创下开源新纪录。在模拟任务成功率（Sim-TSR）上，VeriGUI-3B为16.7%（平均步骤开销ASO=1.25），VeriGUI-7B提升至23.5%（ASO=1.09），显著优于同规模开源模型。在专门构建的鲁棒性基准测试中，VeriGUI-3B的恢复成功率（RSR）为51.1%，循环率（LR）为24.3%；VeriGUI-7B的RSR为52.5%（开源最佳），LR为15.6%。在线评估中，VeriGUI-7B在MiniWoB++和AndroidWorld上的成功率分别为59.7%和25.1%，超越所有开源基线；VeriGUI-3B也优于同规模模型。消融实验验证了训练阶段、负样本比例（70:30最佳）和奖励组件（动作、验证和效果预测三者结合）的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两方面：一是其鲁棒性评估基于“失败操作后屏幕状态不变”的强假设，未能涵盖非幂等性故障（如意外页面跳转、部分界面更新或应用崩溃），这限制了其在真实复杂场景下的泛化能力；二是其逐步骤验证机制虽能纠正局部错误，但随着任务步数增加，缺乏高层任务规划能力，可能导致长期依赖下的性能下降。未来可探索的方向包括：构建更细粒度的故障分类体系，设计能区分非幂等性故障的验证模块；开发分层决策框架，将局部自纠正与全局任务规划相结合，例如引入子目标分解机制或基于记忆的长期状态跟踪；此外，可研究更高效的离线训练方法，利用合成故障轨迹与真实环境反馈的混合学习策略，进一步降低对在线交互的依赖。

### Q6: 总结一下论文的主要内容

该论文针对基于视觉语言模型（VLM）的自主GUI代理在现实环境中因网络延迟、渲染延迟和系统中断等不确定因素导致的“盲目操作”问题，提出了VeriGUI解决方案。其核心贡献是引入了思考-验证-行动-预期（TVAE）框架，通过显式建模动作结果和恢复机制来检测操作失败并引导纠正推理。方法上采用了两阶段训练流程：结合了合成失败轨迹的鲁棒监督微调（Robust SFT）以及采用非对称验证奖励的GRPO强化学习。论文还构建了基于AndroidControl的鲁棒性基准来评估失败识别与纠正能力。实验结果表明，VeriGUI能显著减少失败循环，提高恢复成功率，同时在标准任务性能上保持竞争力，证明了其在动态真实环境中的泛化能力和跨应用领域的可迁移性，为未来GUI代理设计中显式处理执行不确定性提供了重要思路。
