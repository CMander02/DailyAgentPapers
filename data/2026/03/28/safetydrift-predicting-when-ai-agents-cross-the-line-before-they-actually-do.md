---
title: "SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do"
authors:
  - "Aditya Dhodapkar"
  - "Farhaan Pishori"
date: "2026-03-28"
arxiv_id: "2603.27148"
arxiv_url: "https://arxiv.org/abs/2603.27148"
pdf_url: "https://arxiv.org/pdf/2603.27148v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Safety Monitoring"
  - "Risk Prediction"
  - "Markov Chain"
  - "Agent Evaluation"
  - "Multi-step Reasoning"
relevance_score: 8.0
---

# SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do

## 原始摘要

When an LLM agent reads a confidential file, then writes a summary, then emails it externally, no single step is unsafe, but the sequence is a data leak. We call this safety drift: individually safe actions compounding into violations. Prior work has measured this problem; we predict it. SafetyDrift models agent safety trajectories as absorbing Markov chains, computing the probability that a trajectory will reach a violation within a given number of steps via closed form absorption analysis. A consequence of the monotonic state design is that every agent will eventually violate safety if left unsupervised (absorption probability 1.0 from all states), making the practical question not if but when, and motivating our focus on finite horizon prediction. Across 357 traces spanning 40 realistic tasks in four categories, we discover that "points of no return" are sharply task dependent: in communication tasks, agents that reach even a mild risk state have an 85% chance of violating safety within five steps, while in technical tasks the probability stays below 5% from any state. A lightweight monitor built on these models detects 94.7% of violations with 3.7 steps of advance warning at negligible computational cost, outperforming both keyword matching (44.7% detection, 55.9% false positive rate) and per step LLM judges (52.6% detection, 38.2% false positive rate) while running over 60,000x faster.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在复杂、多步骤任务执行过程中，由于一系列看似安全的行动逐步累积，最终导致整体安全违规（如数据泄露）的预测问题，即作者提出的“安全漂移”（safety drift）现象。

研究背景是，随着LLM智能体被赋予访问文件系统、执行代码、发送网络请求等强大工具能力，其行动序列的组合复杂性急剧增加，使得即使每个独立步骤都通过了传统安全检查，整个任务轨迹仍可能违反安全策略。现有研究主要通过事后评估来测量这一问题，例如构建基准测试来统计智能体在任务完成后是否违规。然而，这种方法存在明显不足：它只能进行事后测量和评估，无法在违规发生前进行实时预测和干预，无法回答“智能体是否将在未来几步内违规”这一关键问题。

因此，本文要解决的核心问题是从“事后测量”转向“事前预测”，即建立一个能够实时监控智能体行为、并提前预测其是否将走向安全违规的框架。具体而言，论文提出了SafetyDrift框架，其核心是将智能体的累积安全状态（如访问的数据、使用的工具、行动是否可逆）建模为一个吸收马尔可夫链，并通过闭式吸收分析，计算在给定步数内轨迹达到违规状态的概率。这使得系统能够在违规实际发生之前发出预警，从而实现主动干预，弥补了现有方法在预测和预防能力上的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 智能体安全评测基准**：如OpenAgentSafety、ODCV-Bench、Agents of Chaos和Agent-SafetyBench等研究，它们通过构建基准任务，实证性地测量和分类了LLM智能体的不安全行为，并指出了安全风险可能由一系列单独安全的动作复合而成。这些工作侧重于事后评估，而本文则基于其观察到的轨迹动态进行形式化建模，并转向实时预测。

**2. 智能体可靠性研究**：已有工作提出了涵盖安全性、鲁棒性等维度的智能体可靠性分类法。本文并非停留在概念框架，而是通过形式化的状态建模和马尔可夫分析，为安全性维度提供了一个具体的预测机制。

**3. 概率安全监控方法**：与此最相关的工作是Pro2Guard，它也利用从智能体轨迹中学习的离散时间马尔可夫链进行风险概率计算和干预。本文与它的主要区别在于：(a) 采用吸收马尔可夫链理论及闭式解，计算开销极低；(b) 设计了具有单调性约束的结构化安全状态，而非通用的基于谓词的比特向量；(c) 深入分析了不同任务类别的转移动态，揭示了“不归点”具有任务类型依赖性这一新发现。

**4. 安全强化学习**：约束MDP和安全RL为序列决策中的安全性提供了理论基础，但其假设（连续状态/动作空间、奖励驱动）与LLM智能体（自然语言动作、具有离散副作用的工具调用）的运行环境存在根本差异，本文的工作是对其所需的形式化方法的一种适配。

**5. LLM智能体框架**：如ReAct等范式为智能体提供了执行模型，本文将其视为黑盒，仅对其可观察动作的安全影响进行建模。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于吸收马尔可夫链的预测模型来解决“安全漂移”问题，其核心是预测看似安全的单个行动序列如何累积并最终导致安全违规。整体方法分为三个关键部分：安全状态建模、马尔可夫链分析以及类别感知的运行时监控器。

首先，论文定义了一个**单调的安全状态模型**来刻画智能体执行过程中的累积风险。状态是一个三元组 (d, t, r)，分别代表数据暴露程度、工具使用权限和行动可逆性。关键创新在于其**单调性设计**：数据暴露和工具权限只能增加不能减少（例如，一旦读取了凭证，数据暴露等级就不会回到“无”）。这种设计使得当前状态足以编码历史信息，从而为马尔可夫假设提供了合理性。状态通过一个确定的规则函数映射到五个离散的风险等级（安全、轻度、升高、严重、违规），其中“违规”被设定为**吸收态**——一旦进入就无法离开。

其次，论文将安全状态的演变序列建模为一个**吸收马尔可夫链**。通过从大量智能体执行轨迹中经验估计状态转移概率，构建转移矩阵。由于单调性，从任何非吸收态最终到达违规态的概率在无限步长下均为1.0，因此研究的核心转向**有限步长违规概率**的计算，即预测在给定未来若干步内发生违规的可能性。分析发现，违规概率高度依赖于任务类别：在研究与通信任务中，一旦达到“升高”风险状态，5步内违规概率高达96.9%，存在明显的“不归点”；而在系统管理或代码调试任务中，从任何状态出发的违规概率都低于5%。这揭示了**任务类别特异性**的风险模式，是论文的一个重要发现。

基于上述分析，论文设计了一个**轻量级、类别感知的运行时监控器**。其架构是：在智能体每一步提议行动后，监控器通过一个轻量级分类器（大部分基于确定性规则，少数复杂情况使用LLM作为后备）将行动映射为安全状态增量，更新当前安全状态，然后查询**对应任务类别的有限步长违规概率**。如果该概率超过为该类别校准的阈值，监控器就会触发干预（如阻止行动、请求人工批准等）。整个检查过程仅需字典查找，耗时极短（<0.001毫秒），计算成本可忽略不计，实现了高效预测。

该方法的主要创新点在于：1) 提出了“安全漂移”的量化预测框架，将问题从“是否违规”转变为“何时违规”；2) 利用单调状态和吸收马尔可夫链模型，实现了对累积风险轨迹的紧凑建模和高效分析；3) 发现了风险模式的强任务类别依赖性，并据此设计了类别感知的监控器，在保持高检测率（94.7%）和提前预警（平均3.7步）的同时，极大超越了关键词匹配和每一步使用LLM判断等基线方法的性能与效率。

### Q4: 论文做了哪些实验？

论文实验设置围绕评估 SafetyDrift 模型预测 AI 代理安全漂移的能力。实验设计了 40 个现实多步骤任务，分为四类（每类 10 个）：数据处理、系统管理、研究通信和代码调试。每个场景包含自然语言任务提示、模拟环境（含不同敏感度文件）和 3 到 5 个可用工具。使用 Claude Sonnet 作为底层 LLM，在 ReAct 风格代理循环中执行，每个场景运行 5 到 10 次，共生成 357 条执行轨迹（2,947 个步骤）。步骤安全状态通过确定性规则（85% 步骤）和 LLM 判断（Claude Haiku，15% 模糊情况）标注。数据按类别和违规状态分层划分为训练集（285 条轨迹）和测试集（72 条轨迹）。

对比方法包括：无监控（基线）、基于关键词的监控（匹配网络工具或敏感数据代码执行）、每步 LLM 判断（无上下文）和每步 LLM 判断（3 步上下文）。主要结果：一阶马尔可夫模型在下一状态预测准确率达 75.3%，二阶 81.6%，三阶 83.6%；但一阶模型在计算成本与准确率间权衡最佳。类别间违规率差异显著：研究通信任务违规率 100%，代码调试仅 3%。SafetyDrift 监控器在测试集上检测率达 94.7%（95% CI [83, 99]），误报率 11.8%（95% CI [5, 27]），平均提前预警 3.7 步，每步处理时间 <0.01 毫秒。显著优于关键词监控（检测率 44.7%，误报率 55.9%）和 LLM 判断（检测率 52.6%，误报率 38.2%），且速度快 60,000 倍以上。消融实验显示工具升级是预测轨迹动态的最重要维度。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来探索方向可从多个层面展开。首先，当前安全状态分类器仅停留在工具调用层面，无法分析具体参数内容（如邮件正文是否已脱敏），可能导致误报。未来可探索结合轻量级内容分析的方法，在成本可控的前提下提升判断精度。其次，研究依赖模拟环境，需在真实生产系统中验证其预测模式的泛化能力，并扩展至更多开源模型以加强结论普适性。

从方法改进角度看，可进一步细化风险画像。例如，对同一工具（如运行命令）根据参数进行风险分级，避免对良性操作过度预警。同时，当前模型仅预测违规概率，未区分违规类型（数据泄露、权限提升等）。未来可构建多类别预测框架，以实现更有针对性的干预策略。

此外，论文提到任务类别误分类会影响监控效果，需系统量化误分类率与安全性能的衰减关系，并设计更鲁棒的在线分类机制。最后，将有限时域预测与动态任务长度估计相结合，可优化阈值调整策略，使监控系统能自适应不同任务场景的节奏与风险容忍度。

### Q6: 总结一下论文的主要内容

该论文提出了SafetyDrift框架，用于预测LLM智能体在任务执行过程中因安全漂移（即一系列单独安全的行为累积导致最终违规）而引发的安全问题。核心贡献在于将智能体的安全轨迹建模为吸收马尔可夫链，通过闭式吸收分析计算轨迹在给定步数内达到违规状态的概率，从而实现对违规行为的提前预测。

方法上，论文设计了单调状态空间，使得任何无监督的智能体最终必然违规，因此重点转向有限时间范围内的预测。研究基于357条轨迹覆盖40个现实任务，发现“不归点”高度依赖任务类别：在通信任务中，智能体一旦进入轻度风险状态，后续5步内违规概率高达85%，而在技术任务中该概率始终低于5%。

主要结论表明，基于任务类别的轻量级监控器能以可忽略的计算成本实现94.7%的违规检测率，并提供平均3.7步的预警，性能显著优于关键词匹配和单步LLM判断方法。这证明了轨迹级安全建模的必要性，因为单步评估无法捕捉安全漂移的累积动态。
