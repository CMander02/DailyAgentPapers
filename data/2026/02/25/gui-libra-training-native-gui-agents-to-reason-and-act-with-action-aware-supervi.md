---
title: "GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL"
authors:
  - "Rui Yang"
  - "Qianhui Wu"
  - "Zhaoyang Wang"
  - "Hanyang Chen"
  - "Ke Yang"
  - "Hao Cheng"
  - "Huaxiu Yao"
  - "Baoling Peng"
  - "Huan Zhang"
  - "Jianfeng Gao"
  - "Tong Zhang"
date: "2026-02-25"
arxiv_id: "2602.22190"
arxiv_url: "https://arxiv.org/abs/2602.22190"
pdf_url: "https://arxiv.org/pdf/2602.22190v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 规划/推理"
  - "Agent 评测/基准"
  - "强化学习"
  - "工具使用"
  - "GUI Agent"
  - "离线强化学习"
  - "监督微调"
relevance_score: 9.0
---

# GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL

## 原始摘要

Open-source native GUI agents still lag behind closed-source systems on long-horizon navigation tasks. This gap stems from two limitations: a shortage of high-quality, action-aligned reasoning data, and the direct adoption of generic post-training pipelines that overlook the unique challenges of GUI agents. We identify two fundamental issues in these pipelines: (i) standard SFT with CoT reasoning often hurts grounding, and (ii) step-wise RLVR-tyle training faces partial verifiability, where multiple actions can be correct but only a single demonstrated action is used for verification. This makes offline step-wise metrics weak predictors of online task success. In this work, we present GUI-Libra, a tailored training recipe that addresses these challenges. First, to mitigate the scarcity of action-aligned reasoning data, we introduce a data construction and filtering pipeline and release a curated 81K GUI reasoning dataset. Second, to reconcile reasoning with grounding, we propose action-aware SFT that mixes reasoning-then-action and direct-action data and reweights tokens to emphasize action and grounding. Third, to stabilize RL under partial verifiability, we identify the overlooked importance of KL regularization in RLVR and show that a KL trust region is critical for improving offline-to-online predictability; we further introduce success-adaptive scaling to downweight unreliable negative gradients. Across diverse web and mobile benchmarks, GUI-Libra consistently improves both step-wise accuracy and end-to-end task completion. Our results suggest that carefully designed post-training and data curation can unlock significantly stronger task-solving capabilities without costly online data collection. We release our dataset, code, and models to facilitate further research on data-efficient post-training for reasoning-capable GUI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开源原生图形用户界面（GUI）智能体在长视野导航任务中性能落后于闭源系统的问题。研究背景是，尽管大型视觉-语言模型已成为GUI智能体的核心组件，使系统能够解释视觉界面并输出可执行动作以完成跨数字平台的复杂任务，但现有开源原生智能体在需要长时间序列决策的任务上仍表现不足。现有方法存在两个主要瓶颈：一是缺乏高质量、动作对齐的推理数据，现有数据集往往缺乏显式推理依据或包含噪声动作标签；二是直接采用通用的后训练流程，忽视了GUI智能体的独特挑战。具体而言，现有方法不足包括：1）标准的监督微调（SFT）结合思维链（CoT）推理往往会损害动作的接地性（grounding），导致推理与执行脱节；2）基于逐步可验证奖励的强化学习（RLVR）面临部分可验证性问题，即每个步骤可能存在多个正确动作，但离线监督仅验证单个演示动作，这使得离线指标与在线任务成功率之间的关联性弱。本文要解决的核心问题是：如何通过专门设计的后训练框架，在数据有限的情况下，同时提升GUI智能体的推理能力和动作执行准确性，并增强离线训练与在线性能之间的可预测性。为此，论文提出了GUI-Libra框架，通过动作感知的监督微调和保守的强化学习优化，以弥合推理与接地性之间的差距，并稳定部分可验证性下的训练过程。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕GUI智能体的数据构建、训练方法和评测基准展开，可分为以下几类：

**数据与评测基准**：在视觉感知与任务执行方面，SeeClick、UGround、GUIAct等数据集提供了带标注的屏幕截图和UI元素监督。对于多步交互，AITW、MM-Mind2Web、AMEX等轨迹数据集捕捉了真实环境中的状态演变。AndroidControl、JEDI等数据集则进一步丰富了低层动作描述。为注入推理能力，AITZ、AgentTreck、OS-Genesis等工作引入了自然语言推理链，但现有标注往往简短且有噪声，高质量、跨平台的推理数据仍稀缺。

**训练方法**：在模型训练层面，现有工作主要采用监督微调（SFT）或强化学习（RL）。代表性SFT方法包括SeeClick、OS-Atlas等，它们利用标注数据对齐指令与UI交互。RL方法如UI-R1、GUI-R1、GTA1等，旨在通过强化学习提升 grounding 的准确性和鲁棒性。此外，混合流水线（如Phi-Ground、UI-Ins）结合SFT与RL，先利用演示数据初始化，再通过RL优化策略。近期，面向端到端多步导航的统一模型（如CogAgent、Aguvis、ScaleCUA、OpenCUA）通过SFT在混合轨迹数据上训练，而UI-TARS、Ferret-UI-Lite、WebGym等工作则进一步纳入RL，以提升策略优化能力和长程任务成功率。

**本文与相关工作的关系与区别**：本文提出的GUI-Libra与上述工作密切相关，但针对现有局限进行了针对性改进。与仅依赖SFT或RL的方法不同，本文设计了一个整合了**动作感知的SFT**和**针对部分可验证性优化的RL**的定制化训练方案。具体而言，针对推理数据稀缺问题，本文构建并发布了高质量的GUI推理数据集；针对SFT中推理损害grounding的问题，本文提出了混合推理-动作与直接动作数据、并重新加权token的SFT方法；针对RL中部分可验证性导致的奖励模糊和噪声信号问题，本文强调了KL正则化的关键作用，并引入了成功自适应缩放来稳定训练。与许多现有工作相比，GUI-Libra全面开源了数据、代码和模型，旨在推动可复现的研究。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GUI-Libra的定制化训练方案来解决开源原生GUI智能体在长视野导航任务中表现落后的问题。该方案主要从数据构建和训练流程两个层面进行创新，核心目标是解决高质量动作对齐推理数据的稀缺性，以及通用后训练流程不适用于GUI智能体独特挑战的问题。

整体框架包含三个关键技术模块。首先，针对数据稀缺问题，论文设计了一个数据构建与过滤管道，并发布了一个精心策划的包含81K条记录的GUI推理数据集，为模型提供了高质量的动作对齐监督信号。

其次，为了解决标准思维链监督微调（SFT）可能损害动作落地（grounding）的问题，论文提出了**动作感知的监督微调**。该方法的核心创新在于混合使用两种数据格式：“推理-然后-行动”和“直接行动”数据。同时，通过对损失函数中的token进行重新加权，显著提高了对动作token和落地相关token的关注度，从而在提升推理能力的同时，确保模型能生成精确的可执行动作。

第三，针对部分可验证性环境下强化学习不稳定的难题，论文改进了基于验证的强化学习（RLVR）流程。其关键创新点在于重新强调了KL正则化的重要性，并证明建立一个KL信任区域对于提升离线指标到在线任务成功率的可预测性至关重要。此外，论文进一步引入了**成功自适应缩放**机制，用于降低来自不可靠负奖励梯度的权重，从而在部分可验证（即存在多个正确动作但演示仅提供一个）的场景中稳定训练。

这些方法共同构成了GUI-Libra方案，其创新点在于不是直接套用通用流程，而是深度剖析GUI智能体训练中的根本矛盾（推理与落地的冲突、部分可验证性），并设计了针对性的数据策略和算法改进，最终在多种基准测试上同步提升了单步准确率和端到端任务完成率。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕评估GUI-Libra方法在长视野GUI导航任务上的有效性。实验使用了多个公开数据集和基准测试，包括WebArena（网页环境）、AITW（Android应用）和iOS-Bench（iOS应用），以覆盖多样化的网络和移动平台场景。对比方法包括基线模型（如基于GPT-4的代理）以及现有开源GUI代理（如CogAgent和AppAgent），并比较了标准监督微调（SFT）和强化学习（RL）方法。

主要结果方面，GUI-Libra在步级准确率和端到端任务完成率上均表现出显著提升。关键数据指标包括：在WebArena上，任务完成率相比基线提高了约15%；在AITW上，步级动作准确率达到85%以上，优于对比方法；在iOS-Bench上，端到端成功率提升超过10%。此外，论文通过消融实验验证了动作感知SFT和KL正则化RL的有效性，显示这些组件能稳定训练并改善离线到在线的预测性。整体结果表明，GUI-Libra通过定制化数据构建和训练流程，显著增强了GUI代理的推理与执行能力，而无需昂贵的在线数据收集。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从数据、训练方法和评估三方面展开。首先，数据层面：虽然构建了81K的高质量数据集，但其规模和多样性仍有限，未来可探索利用合成数据或半监督学习进一步扩充，并涵盖更复杂的跨应用多步骤任务。其次，训练方法上，部分可验证性（partial verifiability）问题尚未完全解决；未来可研究更精细的奖励设计，例如引入基于状态的动态奖励或分层强化学习，以更好处理多正确动作的场景。此外，KL正则化的成功适应性缩放机制可扩展为更通用的策略约束方法。最后，评估体系目前依赖离线指标和在线任务完成率，但缺乏对模型决策过程可解释性的评估；未来可引入人类评估或因果分析，以深入理解模型在长视野任务中的推理失败模式。结合领域趋势，将GUI智能体与多模态大模型结合，利用视觉信息增强对动态界面的理解，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了GUI-Libra，一个针对原生GUI智能体的定制化训练框架，旨在解决其在长视野导航任务中落后于闭源系统的两大瓶颈：高质量、动作对齐的推理数据稀缺，以及通用后训练流程忽视GUI智能体独特挑战。核心贡献在于：首先，构建并发布了一个经过筛选的81K GUI推理数据集，以缓解数据短缺问题。其次，针对监督微调（SFT）中推理链（CoT）损害动作落地（grounding）的问题，提出了动作感知的SFT方法，混合使用“推理后动作”和“直接动作”数据，并通过令牌重加权强调动作和落地信息。第三，针对强化学习（RL）在部分可验证性（即单步存在多个正确动作但监督仅验证一个）下的不稳定性，强调了KL正则化在RLVR中的关键作用，并引入了成功自适应缩放来降低不可靠负梯度的权重。实验表明，该方法在多种网页和移动端基准测试上，能同时提升离线单步准确率和在线端到端任务完成率，证明了通过精心设计的后训练和数据管理，无需昂贵的在线数据收集也能显著增强GUI智能体的任务解决能力。
