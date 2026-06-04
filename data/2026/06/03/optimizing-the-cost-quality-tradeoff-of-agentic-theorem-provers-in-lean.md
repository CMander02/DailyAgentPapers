---
title: "Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean"
authors:
  - "Kári Rögnvaldsson"
  - "Chenhao Sun"
  - "Jasper Dekoninck"
  - "Martin Vechev"
date: "2026-06-03"
arxiv_id: "2606.04883"
arxiv_url: "https://arxiv.org/abs/2606.04883"
pdf_url: "https://arxiv.org/pdf/2606.04883v1"
categories:
  - "cs.CL"
  - "cs.LO"
tags:
  - "LLM Agent"
  - "定理证明"
  - "成本优化"
  - "数据与控制平面"
  - "动作路由"
  - "Lean"
  - "智能体决策"
  - "资源分配"
relevance_score: 8.5
---

# Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean

## 原始摘要

Large language models (LLMs) are increasingly used in workflows for generating formal proofs in Lean. These workflows often decompose problems into smaller lemmas, sample many proof attempts, and use compiler feedback to guide search. However, they can be prohibitively expensive, often spending substantial compute on attempts that ultimately fail. In this work, we address this problem with an action routing agent that consists of a data plane and a control plane. The data plane generates natural-language lemma decompositions, formalizes them in Lean, and samples proof attempts for the resulting theorem and lemma targets. The control plane observes previous failed Lean attempts, estimates both the likelihood of success and cost of another attempt, and decides whether to continue proving the current target or restart from a new breakdown. On a subset of PutnamBench, our agent decreases the cost by $25.8\%$ over a fixed-step baseline on average, preserving performance while using substantially less compute. These results suggest that failed Lean trajectories provide actionable signals for cost-aware resource allocation in agentic theorem proving.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对基于大型语言模型（LLM）的Lean形式化定理证明代理成本过高的问题展开研究。现有方法在Lean中生成形式化证明时，通常采用固定步长的策略：将问题分解为引理、生成大量证明尝试，并利用编译器反馈进行搜索。虽然这些方法通过大量计算资源换取了高性能（如在某基准上每题花费50美元），但其固定策略存在根本性效率缺陷：对所有问题无差别地分配相同预算（如分解次数、生成尝试次数），导致大量计算被浪费在不可解问题或形式化错误的目标上。边际收益与成本不成比例，而以往工作主要关注提升性能，忽略了成本优化。本文核心要解决的是如何在保持定理证明性能的同时，显著降低计算成本。作者提出了一个包含数据平面和控制平面的动作路由代理：数据平面负责生成和尝试证明，而控制平面则通过一个轻量级路由器，根据历史失败轨迹动态估计下一次尝试的成功概率与计算成本，并依据成本-质量权衡决策是继续在当前目标上投入计算，还是重新生成分解。在PutnamBench子集上的实验表明，该方法在保持同等性能下将成本降低了25.8%，证明了利用失败信号进行成本感知资源分配的有效性。

### Q2: 有哪些相关研究？

- **Lean 基准测试**：相关工作包括 MiniF2F 和 PutnamBench 等广泛使用的评测集，本文在 PutnamBench 子集上评估，不同于这些仅关注难度的基准，本文强调成本与质量权衡。
- **Lean 证明器模型**：如 GoedelProver 等模型通过强化学习在大量证明轨迹上训练，擅长简单基准但难处理复杂问题；本文不训练新模型，而是优化现有 agent 系统的资源分配。
- **Agentic 证明系统**：现有系统递归分解引理、采样尝试并用编译器反馈搜索，虽提升难度基准解决率但计算成本高；本文的核心区别是引入动作路由代理，通过数据面和控制面动态调整尝试策略，减少无效计算。
- **路由与级联**：传统方法如路由选择模型或级联执行递增昂贵模型，依赖置信度等代理信号；本文在 Lean 定理证明的独特环境中应用路由，基于结构化失败轨迹直接估算成功概率与成本，而非开放任务中的模糊信号。
- **Agentic 环境中的路由**：最近工作扩展到多 agent 系统，优化查询级模型选择或任务分配；本文首次在 Lean 定理证明的 agentic 搜索过程中路由，观察失败尝试的反馈信号做出专用决策。

### Q3: 论文如何解决这个问题？

论文提出了一种“动作路由智能体”（Action Routing Agent），通过引入控制平面与数据平面分离的架构，优化代价-质量权衡。整体框架包括两个核心部分：

**数据平面**负责生成并记录证明轨迹，由四个模块组成：1）**分解模块**：使用通用大模型（如GPT-4o）将原问题分解为一系列自然语言引理及其证明草图；2）**形式化模块**：用Goedel形式化模型将引理翻译为Lean代码，编译筛选最佳候选；3）**形式分解证明器**：尝试用已形式化的引理作为公理证明顶层定理，记录失败轨迹；4）**引理证明器**：从栈中弹出被证明引理依赖的未证明引理，递归验证直至栈空。

**控制平面**是核心创新，其决策基于失败轨迹的统计特征：1）首先固定采样两次初始尝试以获取非平凡信息；2）定义动作空间为{继续尝试, 终止}，其中终止会放弃当前分解并切换至新候选；3）路由策略同时估计下一次尝试的成功概率（基于编译器错误类型、输出长度等特征）与计算代价，通过优化代价-质量目标函数（平衡期望收益与计算开销）做出决策，替代固定预算策略。

关键技术特点包括：仅编译无错（无语法或类型错误）的形式化候选被保留；引文提取机制确保只证明真实被依赖的引理，避免浪费；路由器利用失败轨迹的丰富信号（错误消息、尝试次数等）进行动态分配。在PutnamBench子集上，该架构相比固定步长基线平均降低25.8%计算成本，同时保持性能。

### Q4: 论文做了哪些实验？

论文在PutnamBench的一个85题子集上评估了提出的动作路由智能体，实验设置包括一个固定步骤基线（预算固定）与动态路由方法对比。智能体在数据平面生成自然语言引理分解并形式化为Lean代码，然后对定理和引理目标采样证明尝试；控制平面则基于历史失败轨迹估计后续尝试的成功概率和计算成本，并动态决定是继续尝试当前目标还是从新的分解重新开始。主要结果是动态路由策略显著优于固定基线：在准确性持平的前提下，平均降低了25.8%的预算（即LLM生成计算量）；在成本持平的前提下，准确性提高了7.8%。这证明了固定策略存在大量无效计算，而路由机制通过早期识别低价值尝试来节约资源。实验还对比了不同成本-质量权衡参数λ下的表现，动态路由在所有设置下均更优。关键指标包括成本降低率（25.8%）和准确性提升率（7.8%）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在控制平面仅基于历史失败轨迹的简单启发式决策（如成功率与成本估算），未充分利用LLM的语义理解能力。未来可从三方面探索改进：1) 引入多模态反馈融合机制，将编译器错误类型（如类型不匹配、归纳变量选择错误）与自然语言分解语义联合建模，实现更精准的失败归因；2) 设计分层预算分配策略，根据lemma的图依赖结构动态调整探索深度，而非简单重启；3) 探索主动学习框架，让代理在训练阶段自主生成困难样本的退火方案，通过对抗性训练提升zero-shot鲁棒性。此外，将控制平面从二元决策（继续/重启）扩展为混合动作空间（如局部回溯或假设松弛），可能进一步降低冗余计算。

### Q6: 总结一下论文的主要内容

大型语言模型在Lean中的自动化定理证明取得了进展，但现有代理工作流常采用固定预算策略，导致大量计算浪费在注定失败的尝试上。本文针对此问题提出了一种动作路由代理，通过分离数据平面和控制平面来优化成本与质量的权衡。数据平面负责将问题分解为自然语言引理、形式化并采样证明尝试；控制平面则基于历史失败轨迹，预测下一次尝试的成功概率和计算成本，并动态决策是继续尝试还是从头重新分解。在PutnamBench子集上的实验表明，该方法在保持性能的前提下，平均降低25.8%的计算成本，或在同等成本下提升7.8%的准确率。核心贡献在于识别了固定策略的低效性，并证明了失败的Lean轨迹能为成本感知的资源分配提供可操作信号。
