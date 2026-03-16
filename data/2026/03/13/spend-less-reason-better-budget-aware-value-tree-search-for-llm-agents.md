---
title: "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents"
authors:
  - "Yushu Li"
  - "Wenlong Deng"
  - "Jiajin Li"
  - "Xiaoxiao Li"
date: "2026-03-13"
arxiv_id: "2603.12634"
arxiv_url: "https://arxiv.org/abs/2603.12634"
pdf_url: "https://arxiv.org/pdf/2603.12634v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "推理与规划"
  - "工具使用"
  - "推理效率"
  - "测试时优化"
  - "搜索算法"
  - "预算感知"
  - "理论保证"
relevance_score: 9.0
---

# Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents

## 原始摘要

Test-time scaling has become a dominant paradigm for improving LLM agent reliability, yet current approaches treat compute as an abundant resource, allowing agents to exhaust token and tool budgets on redundant steps or dead-end trajectories. Existing budget-aware methods either require expensive fine-tuning or rely on coarse, trajectory-level heuristics that cannot intervene mid-execution. We propose the Budget-Aware Value Tree (BAVT), a training-free inference-time framework that models multi-hop reasoning as a dynamic search tree guided by step-level value estimation within a single LLM backbone. Another key innovation is a budget-conditioned node selection mechanism that uses the remaining resource ratio as a natural scaling exponent over node values, providing a principled, parameter-free transition from broad exploration to greedy exploitation as the budget depletes. To combat the well-known overconfidence of LLM self-evaluation, BAVT employs a residual value predictor that scores relative progress rather than absolute state quality, enabling reliable pruning of uninformative or redundant tool calls. We further provide a theoretical convergence guarantee, proving that BAVT reaches a terminal answer with probability at least $1-ε$ under an explicit finite budget bound. Extensive evaluations on four multi-hop QA benchmarks across two model families demonstrate that BAVT consistently outperforms parallel sampling baselines. Most notably, BAVT under strict low-budget constraints surpasses baseline performance at $4\times$ the resource allocation, establishing that intelligent budget management fundamentally outperforms brute-force compute scaling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在资源受限环境下进行多步推理时的效率与性能平衡问题。研究背景是，当前提升LLM智能体可靠性的主流范式是“测试时扩展”，即在推理阶段投入大量计算资源（如进行反思、并行采样或搜索），但这通常将计算视为无限资源，导致智能体在冗余步骤或死胡同轨迹上耗尽令牌和工具调用预算，造成资源浪费和边际收益递减。

现有方法的不足主要体现在两个方面：其一，一些面向通用LLM推理的预算感知方法需要昂贵的微调，且难以迁移到自主智能体工作流中；其二，专为智能体设计的框架（如BATS）虽然将剩余预算纳入提示，但仅依赖LLM的隐式自我调节能力，只能在整条轨迹层面进行粗粒度的预算管理，缺乏在推理过程中进行实时干预的能力。这导致智能体无法及时检测并放弃失败的路径，常常陷入死循环或无效探索，在无望的方向上默默耗尽大量预算。

因此，本文要解决的核心问题是：**如何在严格受限的计算预算（令牌和工具调用次数）下，设计一个无需训练、推理时即可运行的框架，实现对智能体多步推理过程的细粒度、步进级的预算感知控制与优化，从而以更少的资源消耗获得更好或相当的任务性能。** 论文提出的BAVT框架通过将推理建模为动态搜索树、引入步进级残差值评估器以及预算条件化的节点选择机制，来应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、预算感知类和评测与框架类。

**方法类**研究聚焦于提升LLM智能体的推理能力。早期工作如ReAct、Toolformer和WebGPT开创了将推理与工具调用交织的范式。近期研究转向**测试时扩展**，通过增加推理阶段的计算资源来提升鲁棒性，代表性方法包括Self-Consistency、思维树（ToT）、思维图（GoT）以及语言代理树搜索（LATS）。这些方法将推理建模为状态空间上的搜索问题，并引入演员-评论员范式或基于提示的评论员作为价值函数来评估中间状态。然而，它们通常以精度为导向，**假定计算资源无限**，缺乏对昂贵动作的惩罚机制或根据资源消耗调整搜索策略的能力。

**预算感知类**研究直接应对部署LLM的经济与计算成本瓶颈。初期策略如模型级联和路由系统（如EcoAssistant）通过将查询导向更便宜的模型来降低成本。近期工作探索了通用LLM推理的动态资源分配，以及专门针对智能体的预算感知工具使用框架（如BATS）。然而，这些方法要么局限于静态的闭卷问题，要么依赖于昂贵的训练后对齐，且对资源的管理多采用**粗略的启发式方法或轨迹级干预**（例如在完整序列失败后评估成本），无法在执行中进行精细调整。

**评测与框架类**工作为复杂智能体的部署和测试提供了基础设施，例如LangChain等编排框架，以及Inspect AI、OctoTools等评估工具包。

**本文与这些工作的关系和区别**在于：BAVT框架属于方法类中的测试时扩展与搜索方法，但**核心创新是实现了严格的预算感知**。它与LATS等方法类似，将多跳推理建模为动态搜索树，但**关键区别**在于：1）引入了**步骤级价值评估**与**预算条件化的节点选择机制**，能根据剩余资源比例动态调整搜索策略（从广泛探索到贪婪利用），这是一种无需训练、数学原理清晰的精细控制；2）为应对LLM自评估过度自信的问题，设计了**残差价值预测器**来评估相对进展而非绝对状态质量。因此，BAVT在无需训练的前提下，解决了现有预算感知方法依赖粗粒度启发式或昂贵微调的不足，并在严格低预算约束下实现了优于基线方法的性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“预算感知价值树”（BAVT）的无训练推理时框架来解决LLM智能体在严格预算约束下的多步推理问题。其核心方法是将多跳推理建模为一个动态搜索树，并利用单一LLM主干内的步骤级价值估计来指导搜索，同时创新性地引入预算条件节点选择机制。

整体框架基于三个核心支柱：1) **测试时扩展树**：将推理过程建模为动态树结构，节点代表中间推理状态或外部观察，边代表智能体生成的动作（如工具调用）。LLM作为生成器，基于当前节点提出多样化的后续动作集合，从而允许同时探索多条推理路径，避免陷入单一死胡同。2) **步骤级价值估计**：为了解决轨迹级评估延迟的问题，BAVT动态提示同一LLM主干切换至评论家角色，对新生成的子节点进行即时评估，输出一个标量价值，估计当前状态距离成功的“距离”。这为树扩展提供了基于即时信息增益的指导，而非 speculative 的前向预测。3) **预算感知扩展**：这是连接树结构和价值估计的关键机制。它通过一个预算感知的节点选择策略，根据剩余资源比例动态调整选择下一个扩展节点的概率分布。

关键技术细节与创新点包括：
- **残差价值预测**：针对LLM自我评估的过度自信问题，评论家评估的是相对进展（信息增量Δ_t），而非绝对状态质量。子节点价值V(n')通过父节点价值V(n)加上Δ_t并经过边界函数Φ(·)归一化得到。这能更可靠地捕捉推理进展轨迹，并有效惩罚冗余或无信息的工具调用。
- **价值引导的步骤指令**：步骤级价值直接指导搜索树的拓扑扩展。根据子节点价值V(n')与阈值τ及父节点价值V(n)的比较，决定采取三种操作之一：若V(n') ≥ τ，则生成最终答案；若V(n') ≤ V(n)，则进行搜索拓宽（探索不同思路）；若V(n) < V(n') < τ，则进行搜索深化（继续深入推理）。这确保了智能体在深度优先利用有希望路径和广度优先探索不确定路径之间高效切换。
- **从探索到利用的动态转变**：核心创新是预算条件节点选择机制。定义有效剩余预算比例r_t（剩余工具和令牌预算比例的最小值），并令动态缩放指数α_t = 1/r_t。候选节点n_i的选择权重w_{n_i} = V(n_i)^{α_t}，概率通过softmax归一化。当预算充足时（r_t ≈ 1, α_t ≈ 1），分布近似与原始价值成正比，鼓励探索。随着预算消耗（r_t → 0, α_t增大），价值差异被放大，概率质量集中在高价值节点上，策略转变为贪婪利用。这是一个无需调参、原则性的转变过程。
- **全局回传与预算后备机制**：发现首个终端答案节点后，会触发全局价值更新，自底向上递归平滑节点价值，使导致多个强候选答案的路径获得优先。为确保在严格预算约束下必有输出，当工具预算耗尽或令牌预算比例低于临界阈值η且未生成任何答案时，框架会立即停止标准扩展，选择累积价值最高的未完成叶节点，强制生成器基于已有上下文合成最终答案。

BAVT通过将树搜索、即时步骤评估与基于剩余资源比例的数学调节深度融合，实现了在有限计算资源下更智能的预算分配和推理路径探索，其理论收敛性也得到了证明。

### Q4: 论文做了哪些实验？

实验在四个复杂多跳推理基准数据集上进行：HotpotQA、2WikiMultihopQA、MuSiQue和Bamboogle。这些数据集严格要求顺序使用工具和动态信息收集，问题无法仅凭模型内部参数权重回答，是评估资源受限环境下交互的理想测试平台。

评估模型包括两个不同架构：具备内部思维链和原生工具使用能力的GPT-OSS-20B推理模型，以及通用指令优化模型Qwen3-30B-A3B-Instruct-2507。主要对比基线是并行采样基线，即在相同资源约束下并行执行K个独立推理轨迹，耗尽预算后通过多数投票确定最终答案。

实验设置了三个预算等级：低预算（最多5次工具调用，推理模型token限2000，指令模型1000）、中预算（10次工具调用，token限分别为4000和2000）和高预算（20次工具调用，token限分别为8000和4000）。性能通过精确匹配（EM）和F1分数衡量。

主要结果显示，BAVT在所有数据集和预算等级上均优于基线。最显著的是，在严格低预算约束下，BAVT的性能超越了基线使用4倍资源（高预算）时的表现。例如，使用OSS-20B模型时，BAVT在低预算等级（5次工具调用）达到0.338的平均EM，超过了基线高预算等级（20次工具调用）的0.334 EM。对于Qwen3-30B指令模型，基线性能随预算增加基本停滞（EM从0.289仅升至0.293），而BAVT在低预算等级就将平均EM提升至0.386。在特定数据集上，如MuSiQue，BAVT将Qwen3-30B的EM从基线的0.12提升至0.21；在Bamboogle上，OSS-20B的EM从基线的0.31大幅提升至0.49。这些结果证明了智能预算管理从根本上优于暴力计算扩展。

### Q5: 有什么可以进一步探索的点？

该论文提出的BAVT框架在推理时预算管理上取得了进展，但仍存在一些局限性和可探索的方向。首先，其核心依赖LLM自身的价值评估，虽然引入了残差预测器缓解过度自信问题，但评估的准确性和泛化能力在不同任务和领域可能不稳定，未来可研究更鲁棒的多模态价值估计模型或引入外部验证机制。其次，当前方法主要针对工具调用类任务，对于更复杂的动态环境或长期规划问题，其树搜索效率可能下降，可探索分层搜索或与模型微调结合以提升适应性。此外，预算分配策略虽具理论保证，但实际中预算类型（如时间、token成本）可能异构，需要更细粒度的多维资源优化。另一个方向是将BAVT与知识蒸馏结合，压缩搜索模型以降低部署开销，或探索在线学习机制，使代理能在执行中根据历史轨迹调整策略，实现更动态的预算适应。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在测试时扩展中计算资源消耗过大的问题，提出了一种无需训练、推理时使用的预算感知价值树（BAVT）框架。核心贡献在于将多跳推理建模为动态搜索树，并引入两个关键创新：一是基于预算条件的节点选择机制，利用剩余资源比例作为节点价值的自然缩放指数，实现从广泛探索到贪婪利用的原则性过渡；二是采用残差值预测器来评估相对进展而非绝对状态质量，以缓解LLM自评估的过度自信问题，从而可靠地剪枝无信息或冗余的工具调用。论文还提供了理论收敛保证，证明在有限预算下BAVT能以至少1-ε的概率获得最终答案。实验表明，BAVT在四个多跳QA基准测试中均优于并行采样基线，尤其在严格低预算约束下，其性能可超越基线使用4倍资源分配时的表现，证明了智能预算管理从根本上优于暴力计算扩展。
