---
title: "KAT-Coder-V2 Technical Report"
authors:
  - "Fengxiang Li"
  - "Han Zhang"
  - "Haoyang Huang"
  - "Jinghui Wang"
  - "Jinhua Hao"
  - "Kun Yuan"
  - "Mengtong Li"
  - "Minglei Zhang"
  - "Pengcheng Xu"
  - "Wenhao Zhuang"
  - "Yizhen Shao"
  - "Zongxian Feng"
  - "Can Tang"
  - "Chao Wang"
  - "Chengxiao Tong"
  - "Fan Yang"
  - "Gang Xiong"
  - "Haixuan Gao"
  - "Han Gao"
  - "Hao Wang"
date: "2026-03-29"
arxiv_id: "2603.27703"
arxiv_url: "https://arxiv.org/abs/2603.27703"
pdf_url: "https://arxiv.org/pdf/2603.27703v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agentic Coding"
  - "Specialization and Unification"
  - "Reinforcement Learning"
  - "Supervised Fine-Tuning"
  - "Model Distillation"
  - "Tool Use"
  - "SWE-bench"
  - "WebArena"
  - "Multi-Expert Training"
  - "Infrastructure Design"
relevance_score: 9.5
---

# KAT-Coder-V2 Technical Report

## 原始摘要

We present KAT-Coder-V2, an agentic coding model developed by the KwaiKAT team at Kuaishou. KAT-Coder-V2 adopts a "Specialize-then-Unify" paradigm that decomposes agentic coding into five expert domains - SWE, WebCoding, Terminal, WebSearch, and General - each undergoing independent supervised fine-tuning and reinforcement learning, before being consolidated into a single model via on-policy distillation. We develop KwaiEnv, a modular infrastructure sustaining tens of thousands of concurrent sandbox instances, and scale RL training along task complexity, intent alignment, and scaffold generalization. We further propose MCLA for stabilizing MoE RL training and Tree Training for eliminating redundant computation over tree-structured trajectories with up to 6.2x speedup. KAT-Coder-V2 achieves 79.6% on SWE-bench Verified (vs. Claude Opus 4.6 at 80.8%), 88.7 on PinchBench (surpassing GLM-5 and MiniMax M2.7), ranks first across all three frontend aesthetics scenarios, and maintains strong generalist scores on Terminal-Bench Hard (46.8) and tau^2-Bench (93.9). Our model is publicly available at https://streamlake.com/product/kat-coder.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）向**智能体化编程**（Agentic Coding）演进过程中面临的三个核心挑战。研究背景是，当前前沿模型正从单轮代码生成转向能够在真实开发环境中自主规划、执行和验证多步骤软件工程任务的智能体。然而，现有方法存在明显不足：首先，**能力碎片化**问题突出，不同编程领域（如软件工程、网页编码、终端操作）的任务特性和训练信号差异巨大甚至冲突，单一的训练流程难以在所有领域同时达到最优。其次，**基础设施耦合**严重，现有的智能体强化学习训练系统将沙箱编排、基准测试和不同框架支持紧密绑定，导致集成新的任务或工具链成本高昂、灵活性差。最后，**智能体强化学习的规模化**存在困难，需要在任务复杂度、意图对齐和框架泛化等多个维度上同时扩展，并需应对混合专家模型训练的不稳定性以及树状多轮轨迹带来的计算冗余问题。

因此，本文要解决的核心问题是：如何构建一个强大、通用且高效的智能体化编程模型。具体而言，论文提出了KAT-Coder-V2模型及其配套方法，通过“**先专精后统一**”的范式来系统性地应对上述挑战。该方法将整体能力分解为五个独立的专家领域进行专门训练，再通过策略蒸馏统一为单一模型；设计了模块化基础设施KwaiEnv以解耦训练组件；并提出了新的训练算法来稳定混合专家训练和加速树状轨迹处理，最终目标是实现一个在多个编程领域和基准测试上均达到顶尖水平的全能型编程智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可以分为方法类、基础设施类和评测基准类。

在方法类上，相关工作主要集中于构建端到端的智能体编码模型。例如，Claude Code、OpenClaw 和 OpenCode 等框架提供了与开发环境交互的脚手架。本文提出的“先专精后统一”范式与这些工作形成对比，它将整体能力分解为五个独立的专家领域进行专门训练，再通过在线策略蒸馏统一，旨在解决单一训练流程难以同时优化多个冲突领域的问题。

在基础设施类上，现有系统通常将数据集、沙箱和脚手架紧密耦合，导致集成新组件成本高昂。本文开发的 KwaiEnv 是一个模块化基础设施，旨在解耦这些组件，支持高并发沙箱实例，为大规模强化学习训练提供了基础。

在评测基准类上，SWE-bench、Terminal-Bench 和 τ²-Bench 等是评估智能体编码能力的标准测试集。本文不仅在这些基准上评估模型，还通过提出的“智能体扩展”范式，在任务复杂性、意图对齐和脚手架泛化等多个维度上系统性地扩展了训练数据，生成了超过10万个多样化的高难度样本，以提升模型的泛化能力。

### Q3: 论文如何解决这个问题？

论文通过“先专精后统一”的范式来解决智能体编码能力的构建问题。其核心方法是将复杂的智能体编码任务分解为五个正交的专家领域：软件工程、网页编码、终端操作、网络搜索和通用编码。每个领域都经历了独立的数据构建与训练，最终通过策略蒸馏统一到一个模型中。

整体框架分为三个阶段：
1.  **监督微调**：为每个专家领域构建大规模、高质量的训练数据，训练出独立的专家模型。例如，软件工程专家利用“Issue-PR配对”从真实GitHub仓库提取问题与修复的关联链，并设计了“AutoBuilder”管道自动合成可验证的交互式任务。
2.  **强化学习**：利用KwaiEnv沙盒环境和验证器基础设施，进行基于环境反馈的强化学习，以提升模型在多轮交互和长视野任务中的决策质量。论文提出了**MCLA**方法来稳定混合专家模型的强化学习训练，并引入了**Tree Training**技术，通过消除树状轨迹上的冗余计算，将训练速度提升最高达6.2倍。
3.  **策略蒸馏**：将多个领域专家的能力通过策略蒸馏整合到统一的KAT-Coder-V2模型中，实现单模型部署的同时，在所有领域保持专家级性能。

主要模块与创新点包括：
*   **领域专精的数据构建**：每个领域都有针对性的数据合成方法。例如，网页编码专家提出了**三视角标签系统**，将用户感知、设计原理和技术实现对齐，并采用**提示词重写**策略，弥合了详细设计说明与用户简短口语化需求之间的分布差距。
*   **可扩展的基础设施**：开发了**KwaiEnv**模块化基础设施，支持数万个并发沙盒实例，为大规模交互式训练提供了基础。
*   **系统化的评估**：特别是在网页编码领域，论文建立了首个系统的**无参考美学评估基准**，将美学保真度分解为结构、视觉、组件和动态四个层面的多个维度，超越了传统仅关注代码正确性的评估方式。

通过这一系列方法，KAT-Coder-V2成功地将多个领域的专精能力融合到一个通用模型中，并在多个基准测试中取得了领先或接近顶级模型的性能。

### Q4: 论文做了哪些实验？

论文构建了名为KwaiEnv的模块化基础设施，以支持大规模、高并发的智能体编码实验。实验设置上，KwaiEnv将数据集、沙箱、脚手架和验证逻辑解耦，通过配置文件灵活组合，实现了从模型评估到强化学习（RL）训练的全流程自动化闭环。该系统可秒级触发数万个并发的远程沙箱实例，每个沙箱运行在隔离的容器环境中，为RL训练提供高吞吐量的轨迹收集能力。

数据集与基准测试方面，实验整合了主流LLM基准，涵盖数据分析、代码生成、软件工程（SWE）、网络搜索和通用推理。具体包括SWE-bench、LiveCodeBench等公开评估集，以及内部专有的训练和测试集，以支持多维评估和全场景RL训练。

对比方法上，KwaiEnv支持以“黑盒”方式集成领先的编码智能体脚手架，如Claude Code、Kilo Code、Cline、OpenClaw、OpenCode等。这些智能体通过统一的网络代理层调用LLM API，无需修改代码即可集成，降低了工程成本。

主要结果与关键指标体现在系统能力上：KwaiEnv能够支持数万个并发沙箱，满足RL训练对海量rollout的高性能需求。其模块化设计带来了数据可扩展性（仅需实现统一数据接口）、脚手架可扩展性（通过配置即可接入新智能体）、评估敏捷性（评估与训练管道基础设施一致）和算法适应性（通过注册新规则即可支持新RL算法）。这些特性显著降低了数据收集和模型训练的工程开销，为后续KAT-Coder-V2模型的训练与评估提供了坚实基础。

### Q5: 有什么可以进一步探索的点？

该论文提出的“Specialize-then-Unify”范式和多专家训练框架虽成效显著，但仍存在一些局限性和可探索空间。首先，其五个专家领域的划分（如SWE、WebCoding等）可能不够完备或存在重叠，未来可探索更细粒度或动态的任务领域划分机制，使模型能自适应地识别和调用所需技能。其次，当前训练高度依赖模拟环境（KwaiEnv）和合成数据，在真实、复杂且充满不确定性的用户场景（如模糊需求、多轮交互）中的泛化能力有待验证，需引入更多人类反馈强化学习（RLHF）或真实交互数据进行对齐。此外，模型统一依赖策略蒸馏，可能造成专家知识在合并过程中的损失，未来可研究更高效的模型融合或动态路由机制（如改进的MoE架构），在保持各专家性能的同时降低推理成本。最后，评估基准虽多但集中于功能正确性，对代码可维护性、安全性、以及跨领域复杂工作流的评估不足，需建立更全面的评估体系。从更广视角看，将此类智能体与规划工具、外部API更深度集成，实现长期、多步骤的项目级代码生成与管理，是极具潜力的方向。

### Q6: 总结一下论文的主要内容

该论文介绍了快手KwaiKAT团队开发的KAT-Coder-V2，这是一个面向智能体编程的代码模型。论文核心在于提出并实现了一种“先专业化后统一”的范式，以解决智能体编程面临的三大挑战：能力碎片化、基础设施耦合和强化学习规模化问题。

具体方法上，研究将智能体编程能力分解为SWE、WebCoding、Terminal、WebSearch和General五个专家领域，每个领域独立进行监督微调和基于环境反馈的强化学习。随后，通过“在线策略蒸馏”技术将这些专家能力无损融合到一个统一的模型中。为支持大规模训练，团队开发了模块化基础设施KwaiEnv，并提出了沿任务复杂性、意图对齐和脚手架泛化三个维度扩展的智能体规模化范式。此外，论文还提出了用于稳定MoE强化学习的MCLA方法，以及用于消除树状轨迹冗余计算、实现最高6.2倍加速的“树训练”技术。

实验结果表明，KAT-Coder-V2在多个基准测试中达到或接近顶尖水平，例如在SWE-bench Verified上达到79.6%，在PinchBench上获得88.7分，并在前端美学场景中领先。这验证了领域专业化训练、大规模系统化智能体强化学习与在线策略蒸馏相结合的有效性，为构建强大的编程智能体提供了一条可行路径。
