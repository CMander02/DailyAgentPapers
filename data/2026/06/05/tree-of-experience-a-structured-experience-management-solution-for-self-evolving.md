---
title: "Tree-of-Experience: A Structured Experience-Management Solution for Self-Evolving Agents under Low-Repetition and Implicit-Reward Environments"
authors:
  - "Zihao Deng"
  - "Yining Zhu"
  - "Leiming Wang"
  - "Jingfei Lu"
  - "Junbo Wang"
  - "Chuncheng Ran"
  - "Yu Yang"
  - "Dixuan Yang"
  - "Jikun Shen"
date: "2026-06-05"
arxiv_id: "2606.06960"
arxiv_url: "https://arxiv.org/abs/2606.06960"
pdf_url: "https://arxiv.org/pdf/2606.06960v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "自我进化"
  - "经验管理"
  - "基准测试"
  - "金融情感预测"
  - "工具使用"
relevance_score: 7.5
---

# Tree-of-Experience: A Structured Experience-Management Solution for Self-Evolving Agents under Low-Repetition and Implicit-Reward Environments

## 原始摘要

Experience-based self-evolution is crucial for LLM agents, but existing benchmarks often assume explicit goals, stable task patterns, and clear feedback. We study a more challenging setting: low-repetition tasks with implicit rewards, where past experience is difficult to reuse and feedback is delayed, noisy, and outcome-level. We introduce \textsc{FinEvolveBench}, a temporally controlled benchmark for financial sentiment prediction that links daily news-driven predictions to future excess returns. We further propose Tree-of-Experience (ToE), a structured experience-management method that organizes, retrieves, validates, and updates agent experience. Experiments show that general-purpose experience mechanisms do not consistently outperform no-experience baselines, while ToE achieves stronger overall performance. These results highlight the importance of structured experience management for self-evolving agents in implicit-reward environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对现有基于经验的自进化AI Agent研究中的一个关键缺陷展开：现有基准测试大多假设任务具有清晰的显式目标、稳定的重复模式和明确的反馈信号（如软件工程、网页导航等程序化任务），这使得Agent可以通过简单复用成功轨迹来进化。然而，现实世界中许多决策问题呈现低重复性（任务实例之间表面相似但内在因果和决策逻辑不同）、反馈是隐式的（仅有延迟、带噪声的最终结果级反馈，缺乏逐步骤指导）且环境非平稳。例如金融情绪预测中，每日市场新闻驱动的预测仅有远期超额收益作为间接奖惩，无法精确定位归因。这种环境对Agent的信用分配和经验的可靠复用构成了严峻挑战。现有通用经验机制在这种低重复、隐式奖励场景下表现不稳定，甚至可能不如无经验的基线。因此，本文核心要解决的研究问题即：如何设计一种结构化的经验管理方法，使Agent能够在低任务重复性、隐式且非平稳反馈的环境中，有效地组织、检索、校验和更新自身经验，从而实现可靠的自我进化，避免直接复用表面相似但已失效的过往经验。

### Q2: 有哪些相关研究？

根据论文内容，相关工作可分为两类：**自进化方法类**和**金融NLP基准类**。

在**方法类**中，相关研究包括 Reflexion、Mem0、Evo-Memory 和 MemRL 等系统，它们探索了智能体如何通过外部记忆存储、检索和重用过去的成功与失败经验来优化推理。本文提出的 **Tree-of-Experience (ToE)** 与之关键区别在于：这些通用经验机制在低重复性与隐式奖励环境下（如本文的金融情感预测任务）表现不稳定，甚至不如不使用经验的基线，而 ToE 通过结构化的经验组织、检索、验证和更新机制，实现了更强的整体性能。

在**基准类**中，现有通用基准（如 SWE-Bench、GAIA、ALFWorld）和金融基准（如 FinQA、TAT-QA、StockBench）存在明显局限：它们大多假设明确的成功信号、稳定的任务模式和清晰的任务重复，而金融基准提供的是静态的、实例级别的监督，不要求智能体处理时间索引信息或适应延迟的市场反馈。本文提出的 **FinEvolveBench** 则专门设计用于低重复性、隐式奖励（延迟、有噪声、结果级别的回报）场景，通过每日新闻驱动的预测与未来超额收益的关联来评估智能体的自进化能力。

### Q3: 论文如何解决这个问题？

Tree-of-Experience (ToE)通过结构化经验管理解决低重复性和隐式奖励环境下的智能体自我进化问题。核心框架围绕一个深度受限、宽度可扩展的经验树展开，每个根到叶的路径定义了一个可执行的分析视角，包含抽象任务模式（上层）和具体推理原则（下层）。

整体框架包含四个主要组件：(1) 先验经验归纳：将历史推理轨迹重写为紧凑逻辑骨架，自动构建层次化经验树；(2) 深度受限表示：经验被组织为固定深度的树结构，新经验通过添加叶节点扩展；(3) 分层选择与自适应扩展：采用由粗到精的检索策略，每层保留top-k候选路径，避免过早承诺单一推理路线，叶层通过语义相似度筛选，并由LLM-as-judge模块判断是否需要扩展新叶节点；(4) 运行时效用估计：维护经验路径的效用向量Q，通过延迟环境反馈进行更新。

关键技术包括：基于乘积的上下文兼容性评分函数，结合历史效用于选择；两种更新策略——显式数值校准（带边界感知和频率衰减的增量更新）和LLM-based效用重写。数值更新实现软遗忘机制，使无效路径逐渐被少选而非直接删除。在FinEvolveBench金融情感预测任务中，ToE通过两层层次结构（关键词匹配的金融因子类别和相似性检索的分析原则，阈值0.8）实现了结构化经验管理，相比无经验基线和通用经验机制，取得了更强的整体性能。

### Q4: 论文做了哪些实验？

论文在FinEvolveBench基准上评估了Tree-of-Experience (ToE)方法，该基准用于金融情感预测，将每日新闻驱动预测与未来超额收益关联。实验使用DeepSeek-V4-Flash作为主骨干模型，Qwen3.6-35B-A3B作为消融。对比方法包括：Baseline（平均聚合LLM情感分数）、Pipe（行业过滤预测）、Pipe+mem0、Pipe+MemRL以及Pipe+ToE。主要评估指标为信息系数（IC），包括截面IC（csIC）和时间序列IC（tsIC）。

在20个交易日的预测中，Pipe+ToE在DeepSeek-V4-Flash上取得最高tsIC（0.0741）和csIC（0.0528），优于Pipe（0.0517和0.0408）和所有其他方法。通用经验系统（Pipe+mem0和Pipe+MemRL）表现不如无经验的Pipe。预测时间跨度消融显示，ToE在1、10、20天间隔上表现最佳，但在5天间隔上弱于无经验基线，表明结构化经验对更长预测期更有利。更新策略消融对比了公式化经验更新与LLM直接更新，结果显示公式化更新在tsIC（0.0741 vs 0.0598）和csIC（0.0528 vs 0.0431）上均显著优于LLM直接更新。

### Q5: 有什么可以进一步探索的点？

针对该论文，以下几个方向值得深入探索：

1. **短周期噪声抑制**：由于短周期金融预测本身存在大量噪声，历史经验检索可能产生误导。未来可探索引入“经验置信度评估”机制，对检索到的经验进行实时可靠性打分，并动态调整其在决策中的权重。也可以尝试利用小波变换等去噪技术预处理输入信号，筛选出高信噪比的片段进行经验匹配。

2. **上游误差鲁棒性**：系统严重依赖新闻结构化流程，误差会沿管线传播。一个改进思路是构建端到端的联合学习框架，将新闻处理、经验管理与预测目标一起进行多任务训练，使系统能自动调整上游模块，减少级联误差。例如，引入对抗训练强化模型对噪声新闻输入的容忍度。

3. **完整交易回测验证**：当前仅使用预测指标进行评测，与真实交易收益存在差距。未来应构建完整的模拟交易回测系统，将预测因子转化为仓位、考虑交易成本和冲击成本，并结合风控模块检验在隐式奖励环境下经验管理能否持续稳定盈利。同时，可引入强化学习中的策略梯度方法，直接优化累计收益目标。

### Q6: 总结一下论文的主要内容

论文研究低重复率与隐含奖励环境下智能体的自我进化问题。现有基准通常假设明确目标、稳定任务模式和清晰反馈，而该文聚焦于更具挑战的场景：任务重复率低导致经验难以复用，反馈延迟、有噪声且仅为结果级。为此，作者提出FinEvolveBench，一个基于金融情绪预测的时间控制基准，将每日新闻驱动的预测与未来超额收益关联。同时提出Tree-of-Experience (ToE)结构化经验管理方法，通过组织、检索、验证和更新智能体经验。实验表明通用经验机制不一定优于无经验基线，而ToE取得了更优的整体性能。核心贡献在于揭示了结构化经验管理在隐含奖励环境中对智能体自我进化的重要性，并为该领域提供了标准化的评估基准和参考解决方案。
