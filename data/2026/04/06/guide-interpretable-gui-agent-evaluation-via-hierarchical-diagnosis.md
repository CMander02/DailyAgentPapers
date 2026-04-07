---
title: "GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis"
authors:
  - "Yuwen Zhai"
  - "Runze Li"
  - "Liang Wang"
  - "Nian Shi"
  - "Liwu Xu"
  - "Wei Zhang"
  - "Ran Lin"
  - "Bo Xu"
  - "Benlei Cui"
date: "2026-04-06"
arxiv_id: "2604.04399"
arxiv_url: "https://arxiv.org/abs/2604.04399"
pdf_url: "https://arxiv.org/pdf/2604.04399v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "GUI Agent"
  - "Interpretability"
  - "Diagnostic Framework"
  - "Benchmarking"
  - "Trajectory Analysis"
relevance_score: 8.0
---

# GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis

## 原始摘要

Evaluating GUI agents presents a distinct challenge: trajectories are long, visually grounded, and open-ended, yet evaluation must be both accurate and interpretable. Existing approaches typically apply a single holistic judgment over the entire action-observation sequence-a strategy that proves unreliable on long-horizon tasks and yields binary verdicts offering no insight into where or why an agent fails. This opacity limits the utility of evaluation as a diagnostic tool for agent development. We introduce GUIDE (GUI Understanding and Interpretable Diagnostic Evaluation), a framework that decomposes trajectory assessment into three sequential stages mirroring the compositional structure of GUI tasks. Trajectory Segmentation partitions the full trace into semantically coherent subtask units. Subtask Diagnosis evaluates each unit in context, assigning a completion verdict and generating a structured error analysis with corrective recommendations. Overall Summary aggregates per-subtask diagnoses into a task-level judgment. By operating on bounded subtask segments rather than full trajectories, GUIDE mitigates the context overload that degrades existing evaluators as task complexity grows. We validate GUIDE on three benchmarks: an industrial e-commerce dataset of 932 trajectories, AGENTREWARDBENCH spanning five web agent tasks with 1302 trajectories, and AndroidBench for mobile device control. Across all settings, GUIDE substantially outperforms existing evaluators-achieving up to 5.35 percentage points higher accuracy than the strongest baseline-while producing structured diagnostic reports that directly inform agent improvement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决图形用户界面（GUI）智能体评估中存在的准确性与可解释性不足的问题。随着大型视觉语言模型的发展，GUI智能体能够执行跨浏览器、移动应用等环境的复杂多步骤自动化任务，但对其性能的可靠评估成为研究和部署的关键需求。现有方法（如基于LLM的评估器）通常对整个动作-观察序列进行单一的整体判断，这种策略存在明显缺陷：在长周期任务中，由于上下文信息过载，评估准确性会随轨迹长度增加而显著下降（例如WebJudge在长轨迹上的准确率下降近18个百分点）；同时，仅输出二元成功/失败判决，无法揭示智能体在何处失败、为何失败，也无法提供改进见解，导致评估结果缺乏诊断价值，难以指导智能体开发。

针对这些不足，本文的核心问题是：如何设计一个既能保持高准确性（尤其在长轨迹任务中）、又能提供结构化可解释诊断的GUI智能体评估框架。为此，论文提出了GUIDE框架，通过分层分解评估过程来应对挑战：先将完整轨迹自动分割为语义连贯的子任务单元，再对每个单元进行独立诊断（生成完成状态、错误根因分析和纠正建议），最后聚合为总体任务判决。这种“分解后诊断”的架构减少了单次评估的上下文负担，提升了长轨迹任务的鲁棒性，并输出层次化的诊断报告，直接服务于智能体优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**GUI智能体基准与系统**、**评估方法**以及**分层/层次化方法**三大类。

**1. GUI智能体基准与系统**：相关研究为GUI智能体的发展提供了任务环境和实现范例。例如，WebArena、VisualWebArena、Mind2Web、Android in the Wild和OSWorld等构建了涵盖网页、移动和桌面环境的复杂、多步骤任务基准。在系统实现方面，SeeAct、WebVoyager以及Claude Computer Use等商业系统展示了视觉语言模型（VLM）在GUI自动化中的直接应用。本文的GUIDE框架旨在评估在这些复杂、长视野任务上运行的智能体，其评估对象直接来源于此类研究。

**2. 评估方法**：这是与GUIDE最直接相关的研究领域，主要分为两类。一是**基于规则的评估**，早期方法依赖URL匹配、DOM状态比较等确定性规则，虽可复现但脆弱且需人工设计。二是**LLM-as-Judge范式**，它利用大语言模型进行任务无关的评估，成为主流替代方案，相关研究包括Pan等人的自主评估、WebJudge、Auto-Eval Judge以及过程奖励模型（PRM）等。本文指出，现有评估方法（包括上述两类）普遍存在局限：或在单一上下文窗口中对整个轨迹进行整体评判（易受长轨迹干扰），或需要执行环境/训练奖励模型，或提供的评估信号（如标量奖励）对开发者不具可解释性。GUIDE的核心区别在于，它首先将轨迹**分解**为语义连贯的子任务单元再进行评估，这减少了每次评估的上下文负载，从而在长任务中更鲁棒，并能生成结构化的、可解释的诊断报告，直接指出失败的位置和原因。

**3. 分层/层次化方法**：这类研究为GUIDE的分层诊断思想提供了方法论背景。主要包括：**任务规划**（如SayCan、DEPS、Voyager将高级目标分解为可执行子目标）、**推理增强**（如Tree of Thoughts通过树状搜索组织推理过程）以及**记忆管理**（如Generative Agents、HiAgent通过分层结构管理长期信息）。此外，在错误处理方面，Reflexion、BacktrackAgent等也采用了分层反思与恢复机制。GUIDE与这些工作的关系在于，它借鉴了“将复杂问题分解为可管理单元”的核心思想，但将其专门应用于**评估阶段**，提出了轨迹分割、子任务诊断、总体汇总的三阶段评估框架，专注于提升评估的准确性与可解释性，而非用于智能体的规划或执行过程。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GUIDE的层次化诊断框架来解决GUI智能体评估中轨迹长、视觉基础、开放性强，以及评估需兼具准确性与可解释性的挑战。其核心方法是**将整体轨迹评估分解为三个顺序执行的模块**，模仿GUI任务本身的结构化特性，从而避免现有方法因一次性处理过长上下文而导致的不可靠和难以解释的问题。

**整体框架与主要模块**：
1.  **轨迹分割模块**：此模块首先将完整的动作-观察序列τ依据语义边界分割成k个连贯的子任务片段τ_i，并为每个片段生成对应的子任务描述t_i。其设计关键点是**仅基于文本化的动作序列（不含截图）进行分割**，这使其保持轻量，并能有效捕捉子任务间的语义转换。分割将评估上下文长度从O(n)降至O(n/k)，从根本上解决了长视野任务中的上下文过载问题，并为后续诊断提供了清晰的局部范围。

2.  **子任务诊断模块**：这是一个多模态模块，负责对每个子任务片段(t_i, τ_i)进行深入评估。它接收子任务描述、该片段的动作序列和对应截图，以及所有子任务描述的列表作为上下文。模块输出一个**结构化的诊断三元组**D_i = (v_i, e_i, c_i)，其中包含“成功/部分成功/失败”的三类判定v_i、自然语言错误分析e_i，以及步骤级别的纠正建议c_i。其创新点在于强制模型进行链式思考推理，并要求枚举问题步骤及其根因与修复方案，这确保了评估的深度与可解释性，直接回答了“哪里出错”和“应如何改正”的问题。

3.  **整体总结模块**：该模块负责聚合所有子任务的诊断结果{D_i}，生成最终的任务级成功与否判定E(t, τ)。其设计并非采用简单的固定规则（如所有子任务必须成功），而是**利用语言模型对全部诊断证据进行整体推理**。这允许模型处理现实世界中复杂的任务依赖关系，例如判断一个中间子任务的失败是否被后续步骤补救，或累积的小错误是否导致总体目标失败，从而做出更精准的最终裁决。

**关键技术及创新点**：
-   **层次化分解与上下文管理**：通过先分割后评估的流水线，显著降低了每个评估单元需处理的上下文长度，这是其在高复杂度任务上保持稳健性和高准确率（较基线提升高达5.35个百分点）的关键机制。
-   **结构化、可操作的诊断输出**：子任务诊断模块产生的结构化三元组是框架可解释性的核心。它超越了二元的整体判决，提供了细粒度的失败原因分析和具体改进建议，使评估结果能直接用于指导智能体的开发和优化。
-   **模块化与针对性设计**：各模块职责清晰且输入经过优化。例如，分割模块仅用文本以保证效率；诊断模块引入多模态信息和链式思考以保证深度；总结模块基于诊断证据进行灵活推理以保证最终判定的合理性。这种设计使得整个评估过程既准确又透明。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行了实验验证：工业电子商务数据集（932条轨迹）、AGENTREWARDBENCH（1302条轨迹，涵盖5个网页任务基准）和AndroidBench（480条轨迹）。实验设置上，GUIDE框架采用gemini-3.0-flash作为骨干模型，所有模块输出JSON格式，并设计了包含最多10次重试的鲁棒解析流程。

对比方法包括：基于规则的方法、NNetNav、Autonomous Evaluation、GPT-4o (A11y Tree)、Claude 3.7 Sonnet、WebJudge、AgentTrek以及Pan等人提出的多种评估器。关键指标为准确率（Accuracy）、精确率（Precision）、召回率（Recall）和F1分数。

主要结果如下：在工业电子商务数据集上，GUIDE达到95.80%的准确率和94.31%的F1分数，比最强基线WebJudge高出5.35个百分点。在AGENTREWARDBENCH上，GUIDE总体精确率达89.21%，超越WebJudge（82.0%）7.2个百分点，且在五个子基准上均保持领先或竞争力。在AndroidBench上，GUIDE平均准确率为94.9±0.3%，优于所有基线。

实验还分析了轨迹长度的影响：随着轨迹步骤增加（从<10步到50-80步），基线方法性能显著下降（如WebJudge从92.9%降至75.0%），而GUIDE保持稳定（93.2%至97.6%）。消融实验表明，去除分割模块导致准确率大幅下降至74.14%，验证了各模块的必要性。此外，分割质量评估显示99.4%的子任务得分在4分或5分（满分5分），证明分割模块的可靠性。

### Q5: 有什么可以进一步探索的点？

该论文提出的GUIDE框架在评估准确性和可解释性上取得了显著进展，但其局限性和未来研究方向仍值得深入探索。首先，GUIDE依赖于大语言模型（LLM）进行轨迹分割和诊断，这可能导致计算成本较高，且对模型能力敏感。未来可研究更轻量化的分割算法，或探索小模型与规则结合的方法以提升效率。其次，当前评估主要基于静态轨迹数据，未来可引入动态交互评估，即在智能体执行过程中实时诊断并反馈，形成“评估-改进”闭环。此外，GUIDE的误差分析虽结构化，但尚未与智能体训练过程深度融合；未来可将诊断结果转化为强化学习奖励信号或策略修正指令，直接驱动智能体优化。另一个方向是扩展任务范围，当前工作集中于GUI任务，但其分层诊断思想可能适用于机器人操作、多模态对话等更长视域、更开放的任务评估。最后，可探索自动化诊断报告的生成与可视化工具开发，降低人工分析成本，进一步提升评估的实用价值。

### Q6: 总结一下论文的主要内容

该论文提出了GUIDE框架，旨在解决GUI智能体评估中因轨迹长、视觉基础且开放性强而导致的评估不准确和缺乏可解释性问题。现有方法通常对整个动作观察序列进行单一整体判断，这在长时程任务中不可靠，且仅提供二元结果，无法揭示失败的具体位置和原因。GUIDE通过三层分解流程改进评估：轨迹分割将完整轨迹划分为语义连贯的子任务单元；子任务诊断在上下文中独立评估每个单元，生成包含完成判定、根因错误分析和纠正建议的结构化报告；整体总结将子任务诊断汇总为最终任务级判断。该方法通过操作有界的子任务段而非完整轨迹，减少了上下文过载，提升了评估鲁棒性。实验在三个基准测试（包括工业电商数据集、AGENTREWARDBENCH和AndroidBench）中验证了GUIDE的优越性，其准确率最高比基线提升5.35个百分点，并能生成层次化诊断报告，直接指导智能体改进。核心贡献在于提供了既准确又可解释的评估工具，推动了GUI智能体开发中的诊断能力。
