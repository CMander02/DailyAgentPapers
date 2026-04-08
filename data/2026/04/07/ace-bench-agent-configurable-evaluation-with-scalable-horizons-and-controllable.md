---
title: "ACE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments"
authors:
  - "Wang Yang"
  - "Chaoda Song"
  - "Xinpeng Li"
  - "Debargha Ganguly"
  - "Chuang Ma"
  - "Shouren Wang"
  - "Zhihao Dou"
  - "Yuli Zhou"
  - "Vipin Chaudhary"
  - "Xiaotian Han"
date: "2026-04-07"
arxiv_id: "2604.06111"
arxiv_url: "https://arxiv.org/abs/2604.06111"
pdf_url: "https://arxiv.org/pdf/2604.06111v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Evaluation Methodology"
  - "Planning and Reasoning"
  - "Lightweight Environment"
  - "Controllable Difficulty"
  - "Scalable Horizons"
  - "Agent Reasoning"
  - "Tool Use"
relevance_score: 9.0
---

# ACE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments

## 原始摘要

Existing Agent benchmarks suffer from two critical limitations: high environment interaction overhead (up to 41\% of total evaluation time) and imbalanced task horizon and difficulty distributions that make aggregate scores unreliable. To address these issues, we propose ACE-Bench built around a unified grid-based planning task, where agents must fill hidden slots in a partially completed schedule subject to both local slot constraints and global constraints. Our benchmark offers fine-grained control through two orthogonal axes: Scalable Horizons, controlled by the number of hidden slots $H$, and Controllable Difficulty, governed by a decoy budget $B$ that determines the number of globally misleading decoy candidates. Crucially, all tool calls are resolved via static JSON files under a Lightweight Environment design, eliminating setup overhead and enabling fast, reproducible evaluation suitable for training-time validation. We first validate that H and B provide reliable control over task horizon and difficulty, and that ACE-Bench exhibits strong domain consistency and model discriminability. We then conduct comprehensive experiments across 13 models of diverse sizes and families over 6 domains, revealing significant cross-model performance variation and confirming that ACE-Bench provides interpretable and controllable evaluation of agent reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有智能体（Agent）评估基准存在的两个关键缺陷：高环境交互开销以及任务视野（horizon）和难度分布不均衡导致的评估效率与可靠性不足的问题。

研究背景是，随着基于大语言模型（LLM）的智能体快速发展，出现了如WebArena、TAU2-Bench等评估基准。然而，这些现有方法为了追求真实感，采用了复杂的环境设置（如网页模拟器、LLM模拟用户），导致环境交互耗时占总评估时间的比例高达34%至41%，这使得大规模评估或训练过程中的验证变得极其昂贵且低效。此外，现有基准中的任务步骤数（即任务视野）在不同实例和领域间分布极不平衡（例如，电信领域任务平均步骤数约为航空领域的2.4倍），且任务难度在不同领域间也存在系统性差异（例如，零售领域平均奖励显著高于电信领域）。这种不均衡性使得简单的领域平均分数无法可靠地反映模型的真实能力，可能掩盖模型在长视野、高难度任务上的系统性失败。

因此，本文要解决的核心问题是：如何构建一个既能大幅降低评估开销，又能对任务视野和难度进行细粒度、可解释控制的智能体评估框架。为此，论文提出了ACE-Bench，其核心创新在于通过一个统一的、基于网格规划的轻量级任务范式，并引入两个正交的控制轴——由隐藏槽位数量 \(H\) 控制的“可扩展视野”和由诱饵预算 \(B\) 控制的“可调难度”，从而实现对智能体推理能力进行高效、可复现且诊断性强的评估。

### Q2: 有哪些相关研究？

相关研究主要分为两大类：**智能体评测基准**和**可扩展长上下文评测**。

在**智能体评测基准**方面，已有工作针对不同应用领域构建了专门的测试环境。例如，Web智能体基准（如早期环境）专注于基于浏览器的任务完成；软件工程基准（如SWE-bench及其变体）评估代码生成和仓库级问题解决能力；科学智能体基准（如ScienceWorld）面向研究导向的推理与实验任务；对话智能体基准（如τ-Bench）则评测工具辅助的对话服务场景。与这些工作相比，本文提出的ACE-Bench并非针对特定领域，而是通过统一的网格规划任务构建了一个通用、轻量化的评测框架，其核心创新在于通过可扩展视野（H）和可控难度（B）两个正交轴实现细粒度控制，并大幅降低了环境交互开销（通过静态JSON文件解析工具调用），从而支持快速、可复现的评估。

在**可扩展长上下文评测**方面，早期基准如LongBench和L-Eval奠定了长上下文语言模型能力评估的基础；后续工作如∞-Bench进一步扩展了上下文长度以测试模型极限；基于合成任务的基准（如NIAH和Ruler）则提供了针对性测试；近期研究如HELMET和LV-Eval引入了可控上下文长度和基于LLM的评估指标，支持更系统、细粒度的分析。本文工作与这一脉络相关，但侧重点不同：ACE-Bench并非直接评测长上下文理解能力，而是通过控制任务视野（隐藏槽位数H）来模拟不同复杂度的规划问题，并强调在轻量化环境下实现难度（通过干扰项预算B）与复杂度的独立、可控调节，从而提供对智能体推理能力更可解释、可控的评估。

### Q3: 论文如何解决这个问题？

论文通过设计一个统一的、基于网格规划任务的基准测试ACE-Bench来解决现有智能体评估中环境交互开销高、任务时长与难度分布不均的问题。其核心方法是构建一个可配置的评估框架，使任务时长和难度成为两个正交且可独立控制的维度，从而实现对智能体推理能力的精细、可解释的评估。

整体框架围绕一个部分完成的日程表网格展开，智能体需填充其中的隐藏格子。每个任务实例包含一个R×C的网格，每个格子必须从特定领域的物品池中填入一个物品。其中H个格子被设定为隐藏槽位，需要智能体填充；其余格子已预填。每个隐藏槽位受到局部槽位约束Cs的限制，同时所有槽位必须共同满足整个网格的全局约束G。每个隐藏槽位提供K个候选物品，分为三类：唯一正确答案（truth）、违反Cs的过滤候选（可通过局部推理排除）、以及满足Cs但会导致任何有效完成方案都违反G的诱饵候选，这确保了每个实例有唯一解。

架构设计的关键在于两个独立控制轴：
1.  **可扩展的任务时长**：通过隐藏槽位的数量H来控制。H值越大，智能体需要维持的连贯全局推理决策序列就越长，从H=1的独立选择到H=17的复杂序列规划。
2.  **可控的任务难度**：通过诱饵预算B来控制。B决定了全局误导性诱饵候选的数量。B=0时任务退化为纯局部过滤；B增大时，智能体必须进行更广泛的全局约束推理以区分真相和诱饵。诱饵的生成经过精心设计，确保其满足局部约束但必然违反全局约束。

主要模块/组件包括：
*   **任务生成器**：根据指定的H和B值，结合六个现实世界规划领域（课程安排、杂货购物等）生成任务实例。所有数据存储在静态JSON文件中。
*   **轻量级环境**：这是关键创新点。所有工具调用（如物品属性查询、约束检查）都通过直接查询静态JSON文件来解析，无需运行任何服务或外部依赖，彻底消除了环境设置开销，实现了快速、可复现的评估。
*   **统一的工具接口**：智能体通过一组预定义的工具与环境交互，例如属性过滤器查询（对隐藏槽位返回满足条件的候选ID，强制逐步推理）、槽位约束检查器、全局约束检查器、设置槽位和完成信号等。

创新点主要体现在：
1.  **正交可控的评估维度**：首次明确将任务时长（H）和难度（B）解耦为两个独立、可量化的控制参数，使评估结果更具解释性。
2.  **轻量级、无开销的环境设计**：完全基于静态文件解析工具调用，极大提升了评估效率，适合训练时验证。
3.  **保证唯一解的约束系统设计**：通过局部约束、全局约束以及三类候选（真相、过滤候选、诱饵候选）的划分，确保了任务的明确性和挑战性。
4.  **领域一致性与可扩展性**：统一的网格任务结构应用于六个不同领域，避免了领域偏差，同时易于扩展到新领域。

### Q4: 论文做了哪些实验？

论文进行了三组核心实验。首先，在基准验证实验中，通过控制隐藏槽位数量 \(H\) 和诱饵预算 \(B\)，验证了其对任务视野和难度的可控性：任务步骤数随 \(H\) 线性增长，任务得分随 \(B\) 增加而下降。同时，Qwen3.5-27B 在六个领域（课程、餐饮、PC组装、购物、旅行、工作）的得分保持稳定（74.1% 至 79.6%），证明了领域一致性；且在 Qwen3.5 Dense、Qwen3.5 MoE 和 MiniMax 三个模型系列内部，得分均随模型规模单调递增，显示了强大的模型区分能力。

其次，在综合性能评估实验中，评估了来自5个系列的13个模型（参数规模0.8B至397B，架构包括Dense和MoE）。实验在6个领域共324个任务实例上进行，每个实例为5x7的网格，隐藏槽位 \(H\) 和诱饵预算 \(B\) 按预设范围组合。主要结果显示，Qwen3.5-397B-A17B 获得最高平均得分84.9%；Qwen3.5 Dense系列性能随规模显著提升（0.8B: 0.6%, 27B: 74.7%）；MiniMax系列得分中等（44.1%-58.6%）。热图分析进一步表明，弱模型（如Qwen3.5-0.8B）在所有设置下得分接近零，而强模型性能随 \(H\) 或 \(B\) 增加而下降。

最后，在工具调用失败鲁棒性实验中，通过随机拒绝工具调用来模拟网络或服务不稳定（失败率 \(p = 0.0, 0.1, 0.3\)）。结果显示，即使 \(p=0.1\) 也会导致性能明显下降，且 \(p=0.3\) 时影响更显著，尤其是在高 \(H\) 和高 \(B\) 的任务中，证明了该基准可用于评估智能体在现实不稳定环境下的韧性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其任务场景相对单一，主要围绕网格规划问题，可能无法全面反映智能体在更复杂、开放世界环境中的泛化能力。未来研究可探索将类似的轻量化评估框架扩展到多模态交互、动态环境或需要长期记忆的任务中，以提升基准的通用性。此外，当前难度控制仅通过诱饵预算实现，未来可引入更多元化的干扰因素，如时间压力、部分可观察状态或资源限制，以更精细地模拟真实决策场景。结合见解，可考虑将ACE-Bench与课程学习结合，设计自适应难度调整机制，使智能体在训练中逐步挑战更高复杂度任务，从而优化学习效率。同时，引入跨任务迁移评估，能进一步检验智能体核心推理能力的可迁移性。

### Q6: 总结一下论文的主要内容

该论文提出了ACE-Bench，一个旨在解决现有智能体评估基准两大局限性的新型基准：高昂的环境交互开销（占总评估时间高达41%）以及任务视野和难度分布不均衡导致的聚合分数不可靠。其核心贡献是设计了一个基于统一网格规划任务的轻量级评估框架。

问题定义为评估智能体在受局部和全局约束的调度规划任务中的推理能力。方法上，ACE-Bench通过两个正交轴提供细粒度控制：“可扩展视野”（由隐藏槽位数量H控制）和“可控难度”（由决定全局误导性干扰项数量的诱饵预算B控制）。所有工具调用均通过静态JSON文件在轻量级环境中解析，消除了设置开销，实现了快速、可重复的评估。

主要结论是，实验验证了H和B能可靠控制任务视野与难度，且基准表现出强大的领域一致性和模型区分度。对13个不同规模和家族的模型在6个领域的测试揭示了显著的跨模型性能差异，证实了ACE-Bench能为智能体推理提供可解释且可控的评估。其意义在于为智能体的高效、可靠迭代和比较提供了关键工具。
