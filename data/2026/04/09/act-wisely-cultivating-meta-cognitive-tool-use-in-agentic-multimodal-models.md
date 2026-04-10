---
title: "Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models"
authors:
  - "Shilin Yan"
  - "Jintao Tong"
  - "Hongwei Xue"
  - "Xiaojun Tang"
  - "Yangyang Wang"
  - "Kunyu Shi"
  - "Guannan Zhang"
  - "Ruixuan Li"
  - "Yixiong Zou"
date: "2026-04-09"
arxiv_id: "2604.08545"
arxiv_url: "https://arxiv.org/abs/2604.08545"
pdf_url: "https://arxiv.org/pdf/2604.08545v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Tool Use"
  - "Multi-modal Agent"
  - "Reinforcement Learning"
  - "Reasoning"
  - "Efficiency Optimization"
  - "Meta-cognition"
relevance_score: 9.0
---

# Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

## 原始摘要

The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体多模态模型中存在的“元认知缺陷”问题，即当前模型无法明智地在依赖内部知识（参数化知识）和调用外部工具（如搜索、计算API）之间做出动态仲裁。研究背景是，随着多模态大语言模型（MLLMs）发展为能够主动与环境交互的自主智能体系统，它们在复杂视觉推理任务中取得了显著进展。然而，现有方法存在严重不足：智能体普遍表现出“盲目工具调用”的病理行为，即使问题仅凭原始视觉上下文即可解决，它们也倾向于反射性地执行工具查询。这导致了严重的延迟瓶颈，并引入了额外的环境噪声，干扰了正确的推理轨迹。

现有强化学习方法试图通过一个标量化的奖励（将工具使用作为惩罚项）来缓解此问题，但这种耦合设计造成了不可调和的优化困境：若惩罚过重，模型会变得过于保守，抑制必要工具使用，损害任务准确性；若惩罚过轻，效率奖励信号在优势归一化过程中会被准确性奖励的方差完全淹没，从而无法有效遏制工具滥用。因此，标量化奖励从根本上无法培养模型根据具体实例进行战略仲裁的能力。

本文要解决的核心问题是：如何设计一种优化框架，使智能体能够学会“何时使用工具”，即培养其元认知能力，在确保任务准确性的前提下，实现高效、经济的工具使用。为此，论文提出了HDPO框架，将工具效率从一个竞争性的标量目标重新定义为严格的条件性目标，通过解耦准确性和效率的优化通道，并引入条件优势估计，迫使智能体首先掌握任务解决，再在此基础上提升其自给自足能力，从而从根本上克服现有方法的瓶颈。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大语言模型（MLLMs）、具备工具调用能力的智能体模型，以及针对工具使用效率的优化方法。

在**多模态大语言模型（MLLMs）**方面，早期研究主要关注视觉问答等任务的直接答案生成。后续工作引入了类似思维链的显式中间推理步骤，以处理更复杂的多模态问题。近期研究则探索了在推理过程中融入连续视觉表征的潜在视觉推理方法，提升了空间推理能力。然而，这些模型大多是被动的，仅限于解释输入和生成响应，缺乏主动调用外部工具的能力，这限制了其在复杂任务上的可靠性。

在**智能体模型**领域，越来越多的研究为MLLM赋予了智能体能力，使其能够在推理过程中调用外部工具（如裁剪、定位、图像搜索等）并与环境交互。这类模型在需要详细检查、迭代证据收集或中间计算的任务上表现出色，尤其是在原始视觉输入信息不足时。现有工作主要侧重于增强工具能力和改进多步交互，但对工具使用效率的关注较少。

在**工具使用效率优化**方面，现有方法（如强化学习协议）试图通过标量化的奖励来惩罚工具使用，以抑制过度调用。但本文指出，这种耦合的优化方案存在根本性矛盾：严厉的惩罚会抑制必要的工具使用，而温和的惩罚在优势归一化过程中又会被准确率奖励的方差所淹没，从而无法有效解决工具滥用问题。本文提出的HDPO框架与这些方法的核心区别在于，它将工具效率从一个竞争性的标量目标重构为一个严格的条件性目标，通过解耦的优化通道分别最大化任务准确率和执行效率，从而从根本上避免了上述困境。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HDPO（分层解耦策略优化）的创新框架来解决智能体在多模态环境中盲目调用外部工具的问题。其核心思想是将传统方法中耦合的、标量化的奖励目标，重构为两个正交且条件独立的优化通道，从而从根本上避免了目标间的干扰和信用分配混乱。

**整体框架与主要模块**：HDPO框架包含两个并行的优化通道。第一个是**准确性通道**，其目标是最大化任务正确性。它计算一个准确性奖励（结合答案正确性和格式合规性），并基于组内所有轨迹的标准GRPO（组相对策略优化）方法计算优势值。第二个是**效率通道**，其目标是在保证正确的前提下优化工具使用的经济性。它定义一个条件性的工具奖励，该奖励仅在答案正确时根据工具调用次数的倒数给出（调用越少奖励越高），否则为零。其关键创新在于**条件优势估计**机制：效率优势的计算仅限定于一个“合格集合”内，该集合只包含当前组内答案正确的轨迹。这样，效率优化信号严格建立在正确解之间的相对比较上，防止了模型通过牺牲正确性来“骗取”效率奖励。

**架构设计与关键技术**：
1.  **解耦的奖励与优势计算**：HDPO摒弃了将准确性奖励和效率奖励线性加权为一个标量奖励的做法。取而代之的是，分别计算两个独立的优势估计 \(A^{acc}\) 和 \(A^{tool}\)，每个优势都基于其自身奖励的组内均值和方差进行归一化。这消除了因奖励方差和协方差导致的梯度纠缠问题。
2.  **条件性效率信号**：效率通道的奖励和优势计算均以答案正确为严格前提。这通过“合格集合” \(\mathcal{Q}\) 实现，确保了模型不会因为单纯减少工具调用（甚至不调用）而获得奖励，除非它能同时给出正确答案。
3.  **联合策略更新**：最终的策略更新损失是两个通道损失的加权和：\(\mathcal{L}_{HDPO} = w_{acc} \cdot \mathcal{L}_{GRPO}(A^{acc}) + w_{tool} \cdot \mathcal{L}_{GRPO}(A^{tool})\)。由于优势已解耦，梯度可以干净地分解，各自独立地推动策略向更高准确性和更高效率的方向进化。
4.  **隐式的认知课程学习**：该设计自然地诱导了一个两阶段的学习过程。训练初期，模型正确率低，合格集合常常为空或很小，效率优势信号微弱或为零，优化由准确性目标主导，迫使模型先学会完成任务。随着模型能力提升，合格集合扩大，效率优化信号逐渐增强，引导模型在已能正确解题的基础上，进一步学习减少不必要的工具依赖。这一过程是自动涌现的，无需手动调度奖励或超参数。

此外，论文还配套提出了一个**元认知数据 curation 流程**，用于构建高质量的监督微调（SFT）数据集和强化学习（RL）环境。这包括执行沙箱验证以消除幻觉的环境动态、基于零样本可解性过滤非必要工具使用的样本，以及使用大模型法官进行多维度质量评估，确保训练数据本身就能示范审慎、必要的工具使用策略。

综上所述，HDPO通过其解耦的、条件化的双通道优化架构，以及配套的高质量数据构建方法，系统性地解决了工具滥用问题，在显著减少工具调用次数的同时，甚至提升了推理的准确性。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估。实验设置包括两个训练阶段：首先使用公开可用的工具增强多模态轨迹数据集（DeepEyesV2、V-Interaction、Thyme）以及OpenMMReasoner的无工具推理数据进行监督微调（SFT）；随后使用约5K个高质量提示进行强化学习（RL）训练，这些提示涵盖感知（45%）、搜索（36%）和数学/通用推理（19%）任务。模型以Qwen3-VL-8B-Instruct为骨干，使用提出的HDPO框架进行优化，关键参数包括批次大小128、学习率1e-6，并设置了正交的准确率（权重1.0）与效率（权重0.15）优化通道。

评估使用了多组基准测试，主要分为两类：1) 感知与文档理解：V*Bench、HRBench、TreeBench、MME-RealWorld、SEEDBench2-Plus、CharXiv；2) 数学与逻辑推理：MathVista_mini、MathVerse_mini、WeMath、DynaMath、LogicVista。

对比方法涵盖三类基线：1) 无工具使用的开源模型（如LLaVA-OneVision、InternVL3-8B、Qwen系列）；2) 纯文本推理模型（如MM-Eureka、ThinkLite-VL）；3) 智能体多模态模型（如Pixel-Reasoner、DeepEyes系列、Thyme、Mini-o3、Skywork-R1V4）。

主要结果表明，所提出的模型Metis在显著减少工具调用（数量级降低）的同时，提升了推理准确率。在多个基准测试中，Metis consistently outperforms existing open-source agentic models，实现了任务正确性与执行效率的协同优化。

### Q5: 有什么可以进一步探索的点？

该论文提出的HDPO框架虽有效解决了工具滥用问题，但仍存在若干局限和可拓展方向。首先，其条件化效率优化依赖于“准确轨迹”的判定，这在复杂开放环境中可能难以稳定界定，未来可探索更动态的阈值机制或引入不确定性感知模块。其次，当前方法主要针对视觉问答场景，未来需验证其在具身智能、跨模态规划等需要时序决策的任务中的泛化能力。此外，论文未深入探讨工具间的依赖关系与组合优化，可引入分层策略网络来管理工具调用链。从更宏观视角看，该研究揭示了智能体元认知能力的重要性，未来可结合因果推理或符号逻辑，让智能体不仅能判断“何时用工具”，还能理解“为何用工具”，从而在效率与鲁棒性间取得更深层平衡。

### Q6: 总结一下论文的主要内容

该论文针对当前多模态智能体普遍存在的“元认知缺陷”问题展开研究，即智能体无法有效权衡何时依赖内部知识、何时调用外部工具，导致其频繁进行不必要的“盲目工具调用”，从而引发延迟瓶颈并引入噪声干扰推理。现有强化学习方法通常将任务准确性和工具效率合并为一个标量化奖励进行优化，但这种耦合设计会导致不可调和的优化困境：严厉的惩罚会抑制必要的工具使用，而温和的惩罚又会在优势归一化过程中被准确性奖励的方差所淹没，无法有效遏制工具滥用。

为解决此问题，论文提出了HDPO框架。该方法的核心创新在于将工具效率从一个竞争性的标量目标重构为一个严格的条件性目标。HDPO摒弃了奖励标量化，维持了两个正交的优化通道：一个“准确性通道”用于全局最大化任务正确性；另一个“效率通道”则通过新颖的条件优势估计机制，仅在准确的轨迹中强制要求执行的经济性。这种解耦架构自然地诱导出一种认知课程：迫使智能体先掌握任务解决，再提升其自主性。基于此框架训练的智能体Metis在多项评估中，将工具调用量降低了数个数量级（例如从98%降至2%），同时提升了推理准确性，证明了战略性的工具使用与强大的推理性能并非此消彼长，消除冗余工具调用能直接贡献于更优的准确性。这项工作推动工具增强学习从单纯教导“如何使用工具”转向培养“何时不用工具”的元认知智慧。
