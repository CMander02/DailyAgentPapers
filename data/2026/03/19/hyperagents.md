---
title: "Hyperagents"
authors:
  - "Jenny Zhang"
  - "Bingchen Zhao"
  - "Wannan Yang"
  - "Jakob Foerster"
  - "Jeff Clune"
  - "Minqi Jiang"
  - "Sam Devlin"
  - "Tatiana Shavrina"
date: "2026-03-19"
arxiv_id: "2603.19461"
arxiv_url: "https://arxiv.org/abs/2603.19461"
pdf_url: "https://arxiv.org/pdf/2603.19461v1"
github_url: "https://github.com/facebookresearch/Hyperagents"
categories:
  - "cs.AI"
tags:
  - "Self-Improving Agents"
  - "Meta-Learning"
  - "Agent Architecture"
  - "Open-Ended Learning"
  - "Computational General Intelligence"
  - "Agent Evaluation"
relevance_score: 9.5
---

# Hyperagents

## 原始摘要

Self-improving AI systems aim to reduce reliance on human engineering by learning to improve their own learning and problem-solving processes. Existing approaches to self-improvement rely on fixed, handcrafted meta-level mechanisms, fundamentally limiting how fast such systems can improve. The Darwin Gödel Machine (DGM) demonstrates open-ended self-improvement in coding by repeatedly generating and evaluating self-modified variants. Because both evaluation and self-modification are coding tasks, gains in coding ability can translate into gains in self-improvement ability. However, this alignment does not generally hold beyond coding domains. We introduce \textbf{hyperagents}, self-referential agents that integrate a task agent (which solves the target task) and a meta agent (which modifies itself and the task agent) into a single editable program. Crucially, the meta-level modification procedure is itself editable, enabling metacognitive self-modification, improving not only the task-solving behavior, but also the mechanism that generates future improvements. We instantiate this framework by extending DGM to create DGM-Hyperagents (DGM-H), eliminating the assumption of domain-specific alignment between task performance and self-modification skill to potentially support self-accelerating progress on any computable task. Across diverse domains, the DGM-H improves performance over time and outperforms baselines without self-improvement or open-ended exploration, as well as prior self-improving systems. Furthermore, the DGM-H improves the process by which it generates new agents (e.g., persistent memory, performance tracking), and these meta-level improvements transfer across domains and accumulate across runs. DGM-Hyperagents offer a glimpse of open-ended AI systems that do not merely search for better solutions, but continually improve their search for how to improve.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有自改进AI系统的一个根本性限制：其元层改进机制通常是固定且手工设计的，这限制了系统自我改进的速度和范围，尤其是在非编码领域。研究背景是，能够自我改进的AI系统有望加速科技进步，但现有方法（如达尔文·哥德尔机DGM）依赖于固定的元代理来生成改进指令，这造成了瓶颈。虽然DGM在编码任务中展示了开放式自改进，但其成功基于一个关键假设：任务解决技能（如编码）与自我反思和修改的技能高度一致。这一假设在编码以外的领域（如论文评审、机器人奖励设计）往往不成立，因为任务技能与元认知技能可能截然不同。

因此，本文的核心问题是：如何构建一个通用的、能够进行“元认知自修改”的自我改进系统，使其不仅能改进任务解决能力，还能改进其自身的改进机制，从而在任何可计算任务上实现潜在的自我加速进步。为此，论文引入了“超智能体”框架，将任务代理和元代理整合到一个单一、可修改的自我指涉程序中。通过扩展DGM创建DGM-Hyperagents（DGM-H），该系统消除了对领域特定技能对齐的依赖，允许元层的修改过程本身被编辑和优化。这使得系统不仅能搜索更好的解决方案，还能持续改进其“如何改进”的搜索过程，从而实现跨领域、可累积的元级改进。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：开放探索、自我改进AI以及自指元学习。

在**开放探索**领域，近期研究利用基础模型作为人类兴趣的代理，在游戏、科学发现和机器人控制等多个领域生成和评估新颖行为，旨在实现持续探索以产生多样化且能力不断增强的成果。本文在此基础上，进一步探索系统如何实现复合式改进，即不仅改进生成的成果，还改进产生新发现和进步的机制本身。

在**自我改进AI**方面，早期理论如哥德尔机提出了可自我修改的智能体，但难以实际应用。后续研究通过元学习、进化或自我博弈等方式，让智能体调整自身参数或学习动态，例如AlphaGo在棋类领域取得超人类表现，但其底层学习算法仍是固定的。近期，基础模型通过迭代优化提示、推理轨迹或代码库来实现自我改进，其中达尔文·哥德尔机在编码领域实现了递归式自我改进。然而，现有方法（包括DGM及其衍生）通常依赖手工设计的固定元层机制，限制了自我改进的复合效应和跨领域泛化。本文提出的超智能体框架则消除了这种限制。

在**自指元学习**领域，先前研究探索了神经网络和进化方法中学习改进学习机制的系统。近期工作利用基于基础模型的智能体实现自指改进，DGM及其后继者主要在编码领域通过自我修改实例化递归自我改进。但这些方法依赖于评估任务与自我修改所需技能之间的对齐（例如，编码能力的提升能直接提升自我改进能力）。本文的核心区别在于，超智能体不假设这种对齐，因为其自我修改机制本身是可编辑的，且不绑定于特定任务领域，从而能在任何可计算任务上同时改进任务性能和改进过程本身。

### Q3: 论文如何解决这个问题？

论文通过提出“超智能体”框架来解决传统自改进系统依赖固定、手工设计的元级机制，从而限制改进速度的问题。其核心方法是将任务智能体（解决目标任务）和元智能体（修改自身及任务智能体）整合为一个单一的可编辑程序，即超智能体。这使得元级的修改过程本身也可被编辑，从而实现“元认知自修改”，不仅能改进任务解决行为，还能改进生成未来改进的机制。

整体架构基于达尔文·哥德尔机（DGM）进行扩展，形成DGM-超智能体（DGM-H）。DGM-H保留了DGM的开放式探索结构，包括维护一个逐步改进的智能体档案库，成功变体可作为未来进步的垫脚石。关键创新在于将整个元级修改机制变为可编辑的，从而突破了DGM中仅适用于编码领域的局限性，使系统能在任何可计算任务上实现自加速进步。

主要模块包括：1）超智能体程序，统一了任务执行和智能体生成；2）开放式探索过程，交替进行元认知自修改和评估两个阶段。在自修改阶段，从档案库中根据性能概率选择父代超智能体，生成自身的修改版本；在评估阶段，对修改后的超智能体进行实证评估并存入档案。这种设计允许智能体不仅修改任务解决逻辑，还能改进元智能体自身，例如改进记忆机制或性能跟踪方法。

关键技术亮点是元认知自修改，它使系统能持续优化自我改进的过程。实验表明，DGM-H能在多样领域中提升性能，优于无自改进或开放式探索的基线及先前自改进系统，且元级改进能跨领域迁移和跨运行累积，展现了真正的开放式自我改进潜力。

### Q4: 论文做了哪些实验？

论文在四个不同领域（编程、论文评审、机器人奖励设计、奥林匹克数学评分）进行了实验。实验设置上，DGM-H 从一个简单的超智能体（包含任务智能体和元智能体）初始化，配备 Bash 和文件修改工具，使用冻结的基础模型并允许自主调用工具。对比基线包括：无自改进元智能体的 DGM-H（固定元级修改机制）、无开放式探索的 DGM-H（无存档、仅替换前代）、原始 DGM（依赖手工固定机制）以及为各领域手工定制的 DGM（DGM-custom），此外还与各领域已有的静态解决方案对比。

主要数据集与基准：编程使用 Polyglot 基准（训练 60 任务，测试 50 任务）；论文评审使用基于顶级会议提交与接收决策的数据集（训练 100 任务，测试集未明确大小）；机器人奖励设计使用模拟环境，训练任务为让四足机器人向前行走，测试任务为零样本生成最大化躯干高度的奖励函数；数学评分使用 IMO-GradingBench（训练 100 任务，测试集未明确大小）。评估采用分阶段协议，先在小任务子集上估计效果，再扩展评估。

关键结果：DGM-H 在所有领域随时间推移性能持续提升，且优于所有基线（包括无自改进、无开放式探索的变体以及手工定制的 DGM）。具体指标上，在编程领域，DGM-H 在测试集上达到约 75% 的成功率，显著高于原始 DGM（约 65%）和静态基线（约 55%）；在论文评审领域，DGM-H 预测与人类决策对齐的准确率超过 80%，优于静态评审智能体（约 75%）；在机器人领域，DGM-H 设计的奖励函数在训练任务上获得高策略性能，并在测试任务上实现有效的零样本迁移；在数学评分领域，DGM-H 的评分准确率较静态基线（ProofAutoGrader）提升约 10%。此外，DGM-H 成功改进了其生成新智能体的元级过程（如持久记忆、性能跟踪），这些改进能够跨领域迁移并在多次运行中累积。

### Q5: 有什么可以进一步探索的点？

该论文提出的超智能体框架（DGM-H）虽然实现了跨领域的开放式自我改进，但其核心仍基于程序生成与评估的迭代循环，存在几方面局限性。首先，系统依赖于初始的元级修改程序作为“种子”，其设计质量可能制约长期改进的上限；若初始机制存在偏差，自我改进可能陷入局部最优。其次，当前实验集中于相对结构化的领域（如算法任务、游戏），在开放动态环境（如物理交互、社会推理）中，如何保证自我修改的安全性与稳定性仍未解决。此外，系统缺乏对“改进目标”本身的反思能力，改进方向完全由预设的性能指标驱动，可能无法适应复杂任务中多目标权衡的需求。

未来研究可从三方面深入：一是引入**元认知约束机制**，让系统能评估修改行为的长期影响，避免有害自我迭代；二是探索**分层自我改进架构**，在修改策略、目标函数、环境模型等多个层面同时学习，提升改进效率；三是结合**外部知识引导**，在关键阶段引入人类反馈或领域知识，突破自我循环可能遇到的能力瓶颈。最终，实现真正安全、高效且能持续进化的通用自我改进系统，仍需在理论基础、算法框架与验证方法上取得突破。

### Q6: 总结一下论文的主要内容

该论文提出了“超智能体”框架，旨在实现开放式的、自我加速的通用人工智能系统。核心问题是现有自改进AI依赖于固定、手工设计的元机制，限制了改进速度，且仅在编码等特定领域有效，缺乏跨领域的通用自改进能力。

论文的核心贡献是设计了一种自指涉的智能体架构，将任务智能体与元智能体整合为单个可编辑程序。其中元智能体不仅能修改任务求解行为，还能编辑自身的改进机制，从而实现“元认知自修改”。方法上，论文扩展了达尔文·哥德尔机，构建了DGM-Hyperagents，消除了任务性能与自改进技能需领域对齐的假设，使其可应用于任何可计算任务。

主要结论显示，DGM-H在多样任务中随时间持续提升性能，优于无自改进或开放式探索的基线及先前自改进系统。更重要的是，它能改进生成新智能体的过程（如持久记忆、性能跟踪），且这些元级改进能跨领域迁移并跨运行累积。这为AI系统不仅搜索更好解，还持续改进其“如何改进”的搜索过程提供了可行路径。
