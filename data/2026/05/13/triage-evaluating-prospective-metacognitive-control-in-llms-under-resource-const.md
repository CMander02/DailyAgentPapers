---
title: "TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints"
authors:
  - "Zabir Al Nazi"
  - "Shubhashis Roy Dipta"
date: "2026-05-13"
arxiv_id: "2605.13414"
arxiv_url: "https://arxiv.org/abs/2605.13414"
pdf_url: "https://arxiv.org/pdf/2605.13414v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "元认知控制"
  - "资源分配"
  - "评估框架"
  - "任务规划"
relevance_score: 8.5
---

# TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints

## 原始摘要

Deploying language models as autonomous agents requires more than per-task accuracy: when an agent faces a queue of problems under a finite token budget, it must decide which to attempt, in what order, and how much compute to commit to each, all before any execution feedback is available. This is the prospective form of metacognitive control studied for decades in human cognition, yet whether language models possess it remains untested. We introduce TRIAGE, an evaluation framework in which a model receives a task pool and a token budget calibrated to its own baseline cost, and commits to a single ordered plan that jointly encodes selection, sequencing, and per-problem allocation. Plans are scored against an oracle with full knowledge of the model's solvability and cost on each problem, yielding a triage efficiency ratio on a common scale. We evaluate frontier and open-source models, with and without reasoning enabled, across competition mathematics, graduate-level science, code generation, and expert multidisciplinary knowledge, and find that current language models exhibit substantial gaps in prospective metacognitive control, revealing a previously unmeasured capability dimension with direct implications for resource-efficient agent deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在资源约束环境下，大型语言模型（LLM）作为自主智能体时，缺乏前瞻性元认知控制能力的问题。研究背景是：尽管测试时计算扩展已成为提升LLM推理能力的主要范式，但这也凸显了计算资源分配这一核心难题。现有方法存在不足：推理模型即使在处理简单问题时也会生成大量token，而面对难题时又会过早放弃合理的推理路径；智能体在任务中浪费计算资源却仍可能失败，表现出“分析瘫痪”现象。虽然已有研究关注LLM的单题准确率或单独判断自身能否回答某问题，但这些方法无法应对一个关键场景：面对一个任务队列和有限的总token预算，智能体需要在没有任何执行反馈的情况下，提前决定选择哪些任务、以何种顺序执行、以及为每个任务分配多少计算资源。这正是人类认知中研究的“前瞻性元认知控制”，即基于对自身知识状态的判断来调节努力分配。本文的核心问题是：LLM是否具备这种跨任务的联合规划能力，即同时评估自身对不同任务的可行性、成本和优先级，从而在共享预算下最大化整体效用。现有评估仅考察单任务行为，尚未检验模型能否自主进行这种组合优化，而这正是构建资源高效智能体的前提。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为以下几类：

1. **元认知知识与监控类**：该领域已有大量工作。例如，LLMs能预测自己能否正确回答问题（元认知监控），并能对任务进行技能标签分配（元认知知识）。研究表明，LLMs在自信度校准上存在系统性缺陷，如过自信（尤其对开放式生成任务）和在没有正确答案时仍给出自信回答。这些研究聚焦于单个任务上的自我评估能力，但本文指出，现有的元认知能力评估均任务是独立的。

2. **从监控到控制类**：最接近的工作是SWE-Bench Verified，它测试了模型在接受或拒绝连续性工作任务时的前瞻性自我评估，但其设计是顺序的、独立的接受/拒绝决策，无法暴露在共享预算下联合选择、分配和排序的组合问题。AbstentionBench也测试了模型在不该回答时是否保持沉默，但不可回答性是问题的固有属性，而非模型-任务-预算三元组的结果。

3. **测试时计算与资源分配类**：TALE和SelfBudgeter等方法让模型在解决问题前估计自己的token成本，但它们是单任务的和前瞻性的，不涉及是否尝试的选择，也没有跨任务的共享预算。系统侧的方法（如长度桶分类、列表排序）在任务池层面进行调度，但预测器是外部的，且目标是延迟，模型自身对问题可解性的判断不起作用。

本文（TRIAGE）填补了上述研究的空白：它要求模型在共享预算下，对任务池进行联合选择、排序和分配，从而评估LLM的“前瞻性元认知控制”能力——一种比单任务监控更复杂的组合决策能力。

### Q3: 论文如何解决这个问题？

TRIAGE通过设计一个前瞻性元认知控制评估框架来解决这个问题。核心方法是：将语言模型作为规划器，在没有任何执行反馈的情况下，对一组任务（任务池）制定一个单一的有序计划。该计划联合编码了三项核心决策：（i）选择哪些任务进行尝试（基于可行性判断）、（ii）按什么顺序尝试（排序）、以及（iii）为每个任务分配多少token预算（成本预测）。计划随后在一个固定的全局token预算下执行。

架构设计上，TRIAGE包含四个关键组件和两个执行机制。四个关键组件是：**任务池**（由一组问题组成，每个问题有其固定价值和模型求解的二元结果及token成本）；**预算**（基于模型自身基线成本的校准比例）；**计划**（由模型生成的有序子集及对应的token分配方案）；**评价指标**（分诊效率比，η）。该比率将模型的实际价值归一化到0-1之间，其中0代表完全未利用自身知识（等同于随机选择），1代表达到拥有完全知识（预言机）的最优水平。

主要创新点在于：1）**前瞻性元认知控制**：首次将人类认知中的前瞻性元认知（执行前计划）引入LLM评估，区分于并发或回顾性判断。2）**四原语的联合评估**：同时衡量可行性、成本、选择和排序这四种能力，而非孤立测试。3）**双执行机制**：设计了“非约束（U）”和“约束（E）”两种执行机制，分别隔离评估模型的“前瞻性监控”和“严格的前瞻性控制”能力。约束机制强制模型遵守自己设定的预算，检验其自我承诺能力。4）**标准化的分诊效率比**：通过预言机和随机参考点归一化，提供了一个跨模型、跨任务池的通用可比较尺度。

### Q4: 论文做了哪些实验？

论文通过TRIAGE框架进行了系统的实验评估。实验设置上，模型需要面对一个任务池和基于自身基线成本校准的token预算，制定一个同时包含选择、排序和每问题资源分配的单一有序计划。

数据集/基准测试涵盖四类：竞赛数学（AIME）、研究生级科学（GPQA）、代码生成（LCB）和专家级跨学科知识（HLE）。对比方法包括前沿模型和开源模型（如Qwen 2.5/3.5系列、GPT-OSS、Gemini 2.5 Flash），分别以标准推理和扩展推理模式运行，并与随机规划者和拥有完全信息的理想规划者（oracle）对比。

主要结果：在中等预算（α=0.5）下，大多数配置在约束模式（预算绑定）下的分诊效率η_E为负，显著低于咨询模式（预算建议）下的η_U。例如，在推理密集型基准（AIME、GPQA、LCB）上η_U-η_E差距最大。仅Gemini 2.5 Flash（标准推理）在所有基准上取得正η_E。扩展推理虽提升基线准确率，但未一致提升分诊质量，反而因输出更长导致约束模式下性能崩溃。识别不可解任务的检测率跨模型差异大，Gemini 2.5 Flash检测率稳定在0.60-0.79，而推理训练模型（如Qwen 3 32B）检测率低至0.00-0.30。分诊质量不随参数规模增长，例如Qwen 2.5 32B在GPQA上表现最差。

### Q5: 有什么可以进一步探索的点？

当前TRIAGE评估框架主要聚焦于单次前瞻性元认知控制，未来可从以下方向深入探索：1) **动态资源重分配机制**：当前模型在规划阶段无法根据执行中的中间结果调整策略，未来可引入类似人类“认知卸载”的在线重规划能力，例如在发现子问题超支时自动回收剩余token。2) **多粒度协同调度**：模型在任务选择时可能因过度关注全局效率而忽视局部最优，可探索分层元认知架构，让高层级（任务优先级排序）与低层级（token分配）控制解耦。3) **噪声鲁棒性增强**：现有评估假设模型对自身能力有完美认知，现实中模型经常高估/低估任务难度，可结合不确定性量化（如置信度校准）来改进资源分配决策。4) **跨模态泛化测试**：当前仅涉及文本任务，可拓展到多模态场景（如图文混合问题），检验元认知控制在感知-推理联合任务中的表现。5) **训练范式革新**：建议设计元认知损失函数，通过强化学习让模型在计算预算惩罚下自主学会“审慎暴力”策略（即高性价比任务优先投入）。

### Q6: 总结一下论文的主要内容

本文介绍了一个名为TRIAGE的评估框架，用于衡量大语言模型在资源约束下的前瞻性元认知控制能力。该能力指模型在有限的令牌预算下，需要同时决定尝试哪些任务、任务执行顺序以及为每个任务分配多少计算资源，且所有决策必须在获得执行反馈前做出。TRIAGE框架要求模型在给定任务池和基于其自身基线成本校准的预算后，输出一个包含任务选择、排序和资源分配的完整计划，并通过与知情预言家对比来计算分诊效率比。研究在竞赛数学、研究生级科学、代码生成和专家级多学科知识四个领域评估了20种模型架构，包括标准LLM和推理增强模型。主要结论显示，当前模型在前瞻性元认知控制方面存在显著缺陷，这种能力不足作为一个新的能力维度，直接影响资源高效智能体部署的可行性。研究表明，扩展推理能提升任务准确性却无法改善分诊质量，且推理模型更不善于识别任务池中的不可解问题。
