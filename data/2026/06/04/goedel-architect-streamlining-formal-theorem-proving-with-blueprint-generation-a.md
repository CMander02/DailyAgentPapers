---
title: "Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement"
authors:
  - "Jui-Hui Chung"
  - "Ziyang Cai"
  - "Zihao Li"
  - "Qishuo Yin"
  - "Rohit Agarwal"
  - "Simon Park"
  - "Rodrigo Porto"
  - "Narutatsu Ri"
  - "Ziran Yang"
  - "Shange Tang"
  - "Xingyu Dang"
  - "Hongzhou Lin"
  - "Mengdi Wang"
  - "Danqi Chen"
  - "Chi Jin"
  - "Liam H Fowl"
  - "Sanjeev Arora"
date: "2026-06-04"
arxiv_id: "2606.06468"
arxiv_url: "https://arxiv.org/abs/2606.06468"
pdf_url: "https://arxiv.org/pdf/2606.06468v1"
categories:
  - "cs.AI"
tags:
  - "定理证明Agent"
  - "Lean 4"
  - "蓝图生成与精炼"
  - "多智能体协作"
  - "代码Agent"
  - "工具使用"
  - "深度求索模型"
relevance_score: 8.5
---

# Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement

## 原始摘要

We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas that builds up to the main theorem. First, Goedel-Architect generates a blueprint of formally stated definitions and lemmas, along with declared dependencies. This blueprint is optionally guided by a natural language proof. Then, a tool-equipped Lean prover component closes each open lemma node in parallel using relevant dependencies. Failed lemmas in turn drive refinement of the global blueprint. This strategy contrasts with other mainstream approaches which use recursive lemma decomposition, and can inefficiently loop on dead-end strategies. Using the open-weight DeepSeek-V4-Flash (284B-A13B) as the backbone, Goedel-Architect attains 99.2% pass@1 on MiniF2F-test and 75.6% pass@1 on PutnamBench. With an optional natural-language proof seeding the initial blueprint on the harder problems, we additionally close the remaining two MiniF2F-test problems (reaching 100%), lift PutnamBench to 88.8% (597/672), and solve 4/6 on IMO 2025, 11/12 on Putnam 2025, and 3/6 on USAMO 2026. This represents state-of-the-art performance for an open-source pipeline at a price point up to 500x less than comparable open-source pipelines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的核心问题是：在形式化定理证明领域，如何以极低的计算成本实现接近甚至超越顶级闭源系统的性能，同时保持模型的开放性和可复现性。研究背景是近年来AI数学能力飞速发展，但生成的数学证明验证成本巨大。现有方法存在明显不足：（1）非智能体证明器通过单次前向传播生成Lean证明，但在PutnamBench等高难度基准上表现极差（<15%）；（2）智能体证明器虽然能通过交互式调用Lean编译器提升性能，但通常依赖闭源商业模型（如Claude Opus 4.5），API成本高达数千美元；（3）现有流水线方法（如Draft-Sketch-Prove）虽然引入了非正式证明辅助，但递归式分解策略容易陷入无效循环。为此，本文提出Goedel-Architect框架，创新性地引入**全局蓝图依赖图**机制——首先生成包含定义和引理依赖关系的蓝图，然后并行证明各开放节点，并通过失败节点驱动蓝图全局精化。该方法避免了递归分解的低效循环，使用开源DeepSeek-V4-Flash模型，单问题成本仅0.44美元（比最接近的开源流水线低500倍），却在MiniF2F上达到99.2%的pass@1，PutnamBench达到75.6%，甚至通过非正式证明引导解决了未解决的IMO/IMO问题。其核心贡献是建立了形式化定理证明的**新帕累托前沿**，首次在极低成本下实现了与顶级闭源系统竞争的性能。

### Q2: 有哪些相关研究？

相关工作可按技术路线分为三类：**非智能体证明器**、**智能体证明器**和**流水线系统**。

本文属于流水线系统，其核心创新在于**蓝图依赖图**机制。与现有流水线（如Draft-Sketch-Prove用自然语言草稿填充占位符、Hilbert递归分解目标）不同，本文将整个证明组织为一个全局的依赖关系图，并支持全局迭代精炼——失败引理会驱动整张蓝图的改写，而非仅在单个子树内回溯。这避免了递归分解中“死循环”的效率问题，并允许并行证明节点共享上下文。

与非智能体证明器（如Goedel-Prover、DeepSeek-Prover、Kimina-Prover等）相比，这些方法一次性输出完整证明，无法利用中间错误反馈，在难度较高的PutnamBench上表现不佳（通常<15%）。本文通过蓝图迭代闭环，实现了大幅性能提升。

与智能体证明器（如AxProverBase、Numina-Lean-Agent）相比，这些方法使用单一智能体交替推理与工具调用（如Lean编译器、Mathlib检索），但常依赖闭源的顶级模型（如Claude Opus 4.5）。本文则使用开源权重模型（DeepSeek-V4-Flash），并开放整个流水线，以极低的计算成本（约为其他最优开源流水线的1/500）达到了可比甚至更优的结果。

此外，本文的可选自然语言证明种子策略，继承了Draft-Sketch-Prove的思想，但将其融入蓝图结构：自然语言证明被映射为带名字的子引理图，供后续精炼模块全局优化，而非被丢弃的扁平草图。这使其在极难问题上（如IMO 2025）能进一步提升性能。

### Q3: 论文如何解决这个问题？

Goedel-Architect的核心创新在于围绕“蓝图”（blueprint）组织形式化定理证明流程。整体框架是一个迭代循环，包含三个阶段：蓝图生成、并行定理证明和蓝图精炼。

首先，蓝图生成阶段接收目标定理的形式化陈述，生成一个依赖图（dependency graph），其中每个节点是形式化定义或引理，边表示证明依赖关系。该图要求无环、所有节点可从目标定理可达，并通过与Lean编译器迭代确保类型正确。可选地，可用自然语言证明引导蓝图生成，使依赖图结构更贴近非形式化推理策略。

随后，每个蓝图中的引理被并行分发给Lean定理证明器。证明器只看到待证引理及其声明的依赖，并配备Lean编译器和Mathlib检索工具，可在预算内迭代调用。若证明失败，返回结构化诊断（如尝试记录、相矛盾的反例），若成功则标记为已证明。

蓝图精炼阶段是核心循环的关键：基于每个引理的诊断结果（已证明/未证明及原因），精炼模型重写依赖图，典型操作包括将硬引理分解为中间辅助引理、重连依赖关系、修正或删除被证明为假的引理。已证明的引理保持签名不变以保留先前投入。精炼后的图进入下一轮证明，循环直至所有引理被证明或达到迭代预算。

整体框架优势在于：以全局依赖图替代递归分解，避免死胡同循环；利用可选的NL证明引导提高困难问题成功率；并行证明+精炼迭代实现高效资源利用，以开源模型DeepSeek-V4-Flash达到SOTA性能，且成本降低500倍。该设计在MiniF2F上实现99.2% pass@1，在PutnamBench达到75.6%，结合NL引导后分别提升至100%和88.8%，并解决多项国际竞赛难题。

### Q4: 论文做了哪些实验？

在实验中，Goedel-Architect 在五个 Lean 4 定理证明基准上进行了评估。主要基准包括：244个问题的 MiniF2F-test（高中竞赛题，如AMC、AIME、IMO）和672个问题的 PutnamBench（大学水平普特南竞赛题，涵盖分析、代数、组合与数论）。另外三个小型无污染基准是 IMO 2025（6题）、Putnam 2025（12题）和 USAMO 2026（6题，训练数据截止后发布）。

对比方法包括：Seed-Prover、Hilbert（基于 Gemini 2.5 Pro）、AxProverBase（基于 Claude Opus 4.5）以及同一 DeepSeek-V4-Flash 骨干下的基线（直接推理、工具集成推理 Hilbert 变体）。

主要结果：在 MiniF2F-test 上，Goedel-Architect 实现 99.2% pass@1（242/244），自然语言引导后达到 100%（244/244），首次完全解决该基准。在 PutnamBench 上，pass@1 达 75.6%（508/672），超过 Hilbert 的 70.0% 和 AxProverBase 的 54.7%；自然语言引导下 pass@4 达 88.8%（597/672）。总 API 成本仅 294 美元，远低于 Hilbert 的约 16.3 万美元。在 IMO 2025 上解决 4/6，Putnam 2025 上解决 11/12，USAMO 2026 上解决 3/6。在 200 题子集上，Goedel-Architect 以更少 token 达到 76% 准确率，而工具集成推理基线仅 54.5%。消融实验显示，蓝图精化迭代带来近似对数线性提升，从初始蓝图的 29.8% 升至16次迭代后的 75.6%。

### Q5: 有什么可以进一步探索的点？

论文的进一步探索点包括：首先，蓝图生成严重依赖自然语言提示，对于复杂问题（如IMO 2025 P1），缺乏自然语言引导时性能骤降，未来可研究如何自动从问题陈述或定理库中提取蓝图结构，减少对人工输入的依赖。其次，当前否定通道和放弃机制虽能反馈错误，但仅针对单节点，未充分利用全局依赖关系；可探索图神经网络或强化学习来学习蓝图优化策略，而非简单重写。第三，计算成本虽已优化，但在PutnamBench上仍需百万级token，未来可研究更高效的迭代策略，如提前终止低潜力分支或基于置信度的预算分配。最后，当前框架聚焦于Lean 4，可扩展至其他证明助手（如Coq、Isabelle），并探索跨语言迁移学习。这些方向有望进一步提升形式化定理证明的自动化和可扩展性。

### Q6: 总结一下论文的主要内容

Goedel-Architect提出了一个基于蓝图生成与精炼的智能体框架，用于在Lean 4中实现形式化定理证明。核心思路是首先构建一个包含定义和引理的依赖图（蓝图），可选地由自然语言证明引导，然后利用配备工具的Lean证明器并行地求解每个未证明的引理节点。当证明失败时，系统会诊断问题（例如陈述错误或引理过难）并驱动对全局蓝图进行精炼，例如修正形式化或分解引理。与递归分解策略不同，这种方法避免了陷入无效循环。使用开源模型DeepSeek-V4-Flash作为骨干，该方法在MiniF2F-test上达到99.2% pass@1，在PutnamBench上达到75.6% pass@1，并在引入自然语言证明后，在更难的题目上实现了100%和88.8%的成绩，同时解决了多个近期IMO等竞赛问题，以远低于同类开源方案的成本达到了领先水平。该工作为开源形式化证明设立了新的性能标杆。
