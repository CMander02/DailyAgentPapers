---
title: "ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction"
authors:
  - "Che Wang"
  - "Fuyao Zhang"
  - "Jiaming Zhang"
  - "Ziqi Zhang"
  - "Yinghui Wang"
  - "Longtao Huang"
  - "Jianbo Gao"
  - "Zhong Chen"
  - "Wei Yang Bryan Lim"
date: "2026-02-24"
arxiv_id: "2602.20708"
arxiv_url: "https://arxiv.org/abs/2602.20708"
pdf_url: "https://arxiv.org/pdf/2602.20708v1"
categories:
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent Security"
  - "Prompt Injection Defense"
  - "Agent Architecture"
  - "Inference-Time Correction"
  - "Adversarial Robustness"
  - "Multi-Modal Agents"
relevance_score: 8.0
---

# ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction

## 原始摘要

Large Language Model (LLM) agents are susceptible to Indirect Prompt Injection (IPI) attacks, where malicious instructions in retrieved content hijack the agent's execution. Existing defenses typically rely on strict filtering or refusal mechanisms, which suffer from a critical limitation: over-refusal, prematurely terminating valid agentic workflows. We propose ICON, a probing-to-mitigation framework that neutralizes attacks while preserving task continuity. Our key insight is that IPI attacks leave distinct over-focusing signatures in the latent space. We introduce a Latent Space Trace Prober to detect attacks based on high intensity scores. Subsequently, a Mitigating Rectifier performs surgical attention steering that selectively manipulate adversarial query key dependencies while amplifying task relevant elements to restore the LLM's functional trajectory. Extensive evaluations on multiple backbones show that ICON achieves a competitive 0.4% ASR, matching commercial grade detectors, while yielding a over 50% task utility gain. Furthermore, ICON demonstrates robust Out of Distribution(OOD) generalization and extends effectively to multi-modal agents, establishing a superior balance between security and efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体面临的间接提示注入（IPI）攻击防御难题，并寻求在安全性与任务效用之间取得更优的平衡。

研究背景是，随着LLM智能体通过检索外部数据来执行复杂任务的能力日益增强，其安全性面临严峻挑战。IPI攻击将恶意指令隐藏在检索内容（如网页、邮件）中，由于LLM本质上难以区分指令与数据，这些恶意负载可以轻易劫持智能体的决策流程，使其执行未授权的工具调用等危险操作，而传统的安全护栏对此往往失效。

现有防御方法存在明显不足。基于启发式规则的方法（如输入模板、事后工具过滤）依赖表层模式，容易被多样化的对抗性变体绕过。基于安全微调的方法虽然安全性更强，但容易导致模型过度敏感，产生“过度拒绝”问题，即过早终止原本有效的多步工作流，严重损害任务效用。同时，微调的计算开销大，难以在动态环境中敏捷部署。这些方法普遍以牺牲任务连续性和实用性为代价来换取安全。

因此，本文要解决的核心问题是：如何设计一种高效、即插即用的防御机制，能够精准地检测并“外科手术式”地中和自适应的IPI攻击，同时最大限度地保持智能体原有任务的连续性和功能性，避免因防御而中断合法的工作流程。论文提出的ICON框架正是为了填补这一空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：攻击方法、防御策略以及底层技术基础。

在**攻击方法**方面，相关工作包括直接提示注入（Direct Prompt Injection）和本文聚焦的间接提示注入（IPI）。IPI攻击通过第三方数据嵌入恶意指令，更具隐蔽性。研究涵盖了基于模板的误导方法、基于优化的通用攻击提示生成，以及能动态绕过静态防护的自适应攻击，后者被证明更为有效。

在**防御策略**方面，现有工作主要包括：1）**提示级缓解策略**，如使用分隔符隔离不可信内容或反复重申系统指令；2）**外部检测器**，如基于Deberta的检测器或无训练启发式方法（如MELON、基于困惑度的检测），这些属于后过滤方法。此外，行业领先模型（如Llama-Guard）采用微调的安全护栏，但需要大规模高质量数据集且计算成本高。现有防御普遍面临安全与效用的权衡问题，容易导致过度拒绝，中断合法工作流。

在**底层技术**方面，相关研究涉及**模型可解释性**（如发现不同注意力头对任务有异质重要性）和**潜在空间操纵（LSM）**。LSM是一种灵活的、模型无关的方法，直接在推理时操作内部表示（如隐藏状态或注意力权重）。**模型探测**（内部状态分析）和**模型引导**（如LM-Steer通过线性变换输出嵌入来引导生成）也为本文提供了技术基础。

本文提出的ICON框架与上述工作的关系和区别在于：它专注于IPI防御，其核心创新是将**探测**（通过潜在空间痕迹探测器识别攻击特征）与**缓解**（通过手术式注意力引导进行校正）相结合。与依赖严格过滤或拒绝的现有防御不同，ICON旨在运行时选择性操纵注意力，在有效中和攻击（达到极低的攻击成功率）的同时，显著提升了任务效用（增益超50%），实现了安全与效率的更优平衡。它无需微调，并展示了良好的分布外泛化能力。

### Q3: 论文如何解决这个问题？

论文提出的ICON框架通过一个探测与缓解的两阶段在线防御机制来解决间接提示注入（IPI）攻击问题，其核心在于识别并修正模型内部注意力机制的异常，而非简单地拒绝执行。该方法的核心架构包含两个主要模块：潜在空间轨迹探测器（LSTP）和缓解矫正器（MR），并辅以一个离线的数据合成模块用于训练。

整体框架遵循“离线训练，在线检测与矫正”的范式。离线阶段，论文采用“LLM-as-Optimizer”框架合成大量具有上下文对齐性和潜在隐蔽性的IPI攻击样本，旨在划定良性任务与自适应攻击在潜在空间中的边界，为后续模块提供高质量的训练数据，确保其学习到IPI攻击的本质“过度聚焦”特征，而非表面的关键词模式。

在线防御阶段是ICON的核心。首先，**潜在空间轨迹探测器（LSTP）** 作为实时门卫，负责检测攻击。其理论基础是IPI攻击会导致模型注意力机制出现结构性异常，即对恶意内容产生“强制聚焦”，从而在潜在空间中留下可区分的痕迹。LSTP的输入是模型在生成过程中的原始注意力权重。为了量化这种异常，论文首先定义了**聚焦强度分数（FIS）**，它基于注意力熵的补数来计算，熵值越低（FIS越高）表示注意力越集中，可能预示着攻击。LSTP接着对变长的注意力熵序列进行**时序特征聚合**，提取每个注意力头的最小熵、平均熵和标准差这三个关键特征，形成固定维度的特征向量。这些特征经过一个结合了1D-CNN和MLP的**混合架构**进行处理，并采用自适应全局最大池化来保证对不同生成长度的不变性，最终输出攻击检测结果。

一旦LSTP检测到攻击，**缓解矫正器（MR）** 立即介入，进行精准的注意力调控以恢复模型功能。与直接拒绝并终止工作流的传统方法不同，MR执行的是“外科手术式”的潜在空间矫正。其关键技术是**双因素注意力干预**机制：1) **调控范围（τ）**：根据FIS识别出异常注意力头，并基于阈值θ确定需要抑制的、权重过高的特定查询-键依赖关系（即异常聚焦点），生成一个二值掩码。2) **调控强度（γ）**：对原始注意力矩阵应用一个对比性调控操作，使用系数γ（<1）来抑制掩码标识的异常权重。这种在Softmax归一化之前的抑制，会利用Softmax的重新分配效应，自然地将注意力权重重新分配到未被抑制的良性上下文上，从而在削弱恶意指令影响的同时，放大任务相关元素，恢复模型原本的功能轨迹。

ICON的创新点在于：1) **从拒绝到矫正的范式转变**：通过注意力调控在潜在空间直接中和攻击，避免了因简单拒绝导致的“过度拒绝”和工作流中断，显著提升了任务效用（论文显示效用增益超过50%）。2) **基于内在表征的检测**：利用IPI攻击在注意力熵上留下的“过度聚焦”特征进行检测，对多样化和隐蔽性攻击具有更好的泛化能力。3) **精准的干预机制**：双因素干预实现了对异常注意力模式的细粒度、可调控的抑制，最小化了对正常推理过程的干扰。实验表明，ICON在将攻击成功率（ASR）降至极低水平（0.4%）的同时，保持了最高的任务效用，在安全性与效率间取得了优越的平衡。

### Q4: 论文做了哪些实验？

论文的实验设置主要将ICON集成到ReAct框架中，评估其对间接提示注入（IPI）攻击的防御效果。实验覆盖了多种骨干模型，包括文本模型（Qwen、LLaMA、Mistral）和多模态视觉语言模型（Qwen-VL、InternVL、MiniCPM），以验证方法的通用性。

使用的数据集和基准测试包括：InjectAgent和AgentDojo用于评估防御效果；TrojanTools用于训练，以测试分布外泛化能力；视觉任务则采用Meta提供的Visual Prompt Injection Benchmarks。

对比方法涵盖了三类主流防御机制：基于模板的方法（如Repeat Prompt和Delimiting）、基于过滤的方法（如MELON）以及基于微调的方法（如Qwen3Guard和Gemini）。这些基线方法在安全性和任务效用方面提供了对比基准。

主要结果方面，ICON在安全性上达到了0.4%的平均攻击成功率（ASR），与商用检测器（0.2% ASR）相当，同时显著提升了任务效用。例如，在Qwen-3实验中，ICON保持了53.8%的效用准确率（UA），优于其他基线（低于49%）。关键指标包括：在分布外测试中，ICON在AgentDojo上的攻击检测率（ADR）超过97%，在InjectAgent上超过80%；效用恢复率（URR）在Qwen-3-8B上达到62.3%以上。此外，ICON的训练成本极低，仅需2分钟和255个样本，参数量约3.1万，远低于微调方法（如Qwen3Guard需10小时和119万样本）。在多模态场景中，ICON将平均ASR降至2.9%，同时将UA提升至47.2%，比Gemini高出近20%，实现了安全与效用的平衡。

### Q5: 有什么可以进一步探索的点？

该论文提出的ICON框架在防御间接提示注入攻击方面取得了显著效果，但其局限性和未来探索方向仍值得深入。首先，ICON依赖于潜在空间中的“过度聚焦”特征来检测攻击，这可能无法覆盖所有新型或更隐蔽的攻击模式，尤其是那些不留下明显潜在空间痕迹的攻击。其次，框架在注意力机制上进行手术式修正，但可能对模型内部复杂依赖关系的理解不够全面，未来可结合更细粒度的神经元级分析来增强修正精度。

未来研究方向包括：一是扩展攻击场景的覆盖范围，例如针对多轮对话或长期记忆中的潜伏性注入攻击；二是提升框架的通用性和自适应能力，使其能动态适应不同LLM架构和多模态任务，而无需针对每个模型进行微调；三是探索与形式化验证结合的方法，为防御机制提供理论安全保障。此外，ICON目前主要关注防御，未来可集成主动检测与修复机制，形成更全面的安全闭环。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体易受间接提示注入（IPI）攻击的问题，提出了一种名为ICON的新型防御框架。其核心贡献在于突破了现有防御方法（如严格过滤或拒绝机制）因过度拒绝而中断正常任务流程的局限，实现了在有效抵御攻击的同时保持任务连续性的平衡。

论文的问题定义聚焦于IPI攻击，即攻击者通过检索内容中的恶意指令劫持智能体执行。方法上，ICON基于一个关键洞察：IPI攻击会在模型的潜在空间中留下独特的“过度聚焦”特征。为此，框架包含两个核心组件：首先，“潜在空间追踪探测器”通过计算高强度的聚焦分数来检测攻击；随后，“缓解校正器”进行精准的注意力引导，选择性地操纵对抗性的查询-键依赖关系，同时放大与任务相关的元素，从而恢复LLM的正常功能轨迹。

主要结论显示，ICON在多个骨干模型上的广泛评估中取得了卓越效果：攻击成功率（ASR）低至0.4%，与商用级检测器相当，同时任务效用提升了超过50%。此外，ICON展现出强大的分布外（OOD）泛化能力，并能有效扩展到多模态智能体，在安全性与效率之间建立了优越的平衡。
