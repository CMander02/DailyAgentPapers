---
title: "Graph-based Target Back-Propagation for Context Adaptation in Multi-LLM Agentic Systems"
authors:
  - "Tan Zhu"
  - "Tong Yao"
  - "Kananart Kuwaranancharoen"
  - "Amit Singh"
  - "Yushang Lai"
  - "Deepa Mohan"
  - "Shankara Bhargava"
date: "2026-06-12"
arxiv_id: "2606.14155"
arxiv_url: "https://arxiv.org/abs/2606.14155"
pdf_url: "https://arxiv.org/pdf/2606.14155v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "multi-agent systems"
  - "context adaptation"
  - "prompt engineering"
  - "credit assignment"
  - "graph-based optimization"
  - "LLM workflow"
relevance_score: 8.5
---

# Graph-based Target Back-Propagation for Context Adaptation in Multi-LLM Agentic Systems

## 原始摘要

Context adaptation automates prompt engineering in LLM-based systems by iteratively revising tunable prompts from task feedback, without modifying model weights. Extending this paradigm to multi-LLM agentic systems is crucial: existing methods suffer from inaccurate credit assignment and lack convergence guarantees. We propose \textbf{G}raph-based \textbf{T}arget \textbf{B}ack-\textbf{P}ropagation (GTBP), a context adaptation framework for agentic workflows modeled as directed acyclic graphs. GTBP propagates local target outputs backward through the workflow graph and uses target--output discrepancies to guide a stage-wise prompt update mechanism. Theoretically, we show that GTBP's stage-wise prompt updates become stable over iterations, and that a sufficiently capable LLM optimizer can decrease the overall objective. Empirically, GTBP consistently outperforms strong baselines across three benchmarks while maintaining comparable computational cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多LLM智能体系统中上下文适应的信用分配不准确和缺乏收敛保证的问题。研究背景方面，在基于LLM的系统中，通过任务反馈迭代修改可调提示（不修改模型权重）实现上下文适应，能够自动化提示工程。然而，现有方法在多LLM智能体系统中面临两大不足：一是像GEPA和ACE这类方法通过隐式而非明确定义的推理过程进行信用分配，导致归因模糊，无法准确将最终错误归因到负责的模块特定上下文；二是TextGrad和Agentic Neural Networks等基于图结构传播文本反馈的方法，其管道主要基于启发式，没有直接耦合到提示优化目标，并且采用基于启发式规则的LLM优化器更新提示，在多模块系统中的收敛性质在理论上未得到充分探索。因此，本文的核心问题是提出一种显式、稳定且具有收敛保证的信用分配方法，以实现多LLM智能体系统中提示的高效上下文适应。

### Q2: 有哪些相关研究？

与本文相关的研究主要分为三类：信用分配方法、上下文自适应优化和理论分析。

**1. 信用分配方法：** 传统方法如反向传播（BP）依赖链式法则梯度，但多LLM系统缺乏可微性。替代方法包括解耦神经接口（DNI）和差异目标传播（DTP），后者通过为中间模块分配目标输出来实现信用分配。本文的GTBP借鉴了DTP的“目标反向传播”思想，但针对有向无环图（DAG）结构的智能体工作流进行了适配，而非仅用于神经网络。近期工作如TextGrad和Agentic Neural Networks通过文本梯度传播实现结构化信用分配，而TextResNet则利用残差架构改进归因。GTBP与之不同，它通过局部目标-输出差异进行分阶段提示更新，而非依赖梯度信号。

**2. 上下文自适应优化：** 自动提示优化方法如APE和OPRO基于标量任务级反馈搜索提示候选；Reflexion和GEPA利用文本反馈迭代改进；ACE则通过剧本（playbook）实现结构化更新。这些方法常使用黑箱LLM反射进行信用分配，难以控制。GTBP通过沿DAG反向传播局部目标，提供结构化、可收敛的更新机制，显著提升稳定性。

**3. 理论分析：** 现有研究将上下文自适应与权重更新联系，证明提示更新可等效于参数更新，但缺乏通用理论。GTBP从理论上证明了分阶段提示更新的迭代稳定性及优化器可降低整体目标，填补了这一空白。

### Q3: 论文如何解决这个问题？

GTBP的核心创新在于将目标传播技术应用于多LLM智能体工作流中的上下文自适应。整体框架包括两个主要阶段：目标传播和阶段式提示更新。首先，将智能体工作流建模为有向无环图（DAG），每个节点代表一个可调提示的LLM模块。在目标传播阶段，从最终输出节点开始，以参考输出作为最终目标，沿逆向拓扑顺序逐层向上传播。对于每个节点，利用LLM引导的后向推理算子，根据当前节点的目标输出、原始输入和局部上下文推断其前驱节点的输入目标。后向推理算子通过精心设计的提示模板实现，在保持与原始输入语义相近的同时，生成能促使模型产生目标输出的新输入。这一过程解决了文本数据非可微分、模块为黑箱的难题。在提示更新阶段，系统收集传播过程中产生的输入、缓存输出和推断目标，构建模块级更新集。采用阶段式更新机制：提示结构为有序的文本声明列表，初始编辑预算控制可修改声明数；每隔固定迭代次数添加一条新声明（claim-addition），并定时衰减编辑预算（edit-budget decay），使优化从粗粒度调整逐渐过渡到细粒度精调。更新时，LLM优化器根据当前输出与目标输出的差异，有选择地修改现有提示声明。理论保证方面，论文证明阶段式更新在迭代中趋于稳定，且足够强大的LLM优化器能持续降低整体目标。关键技术特点包括：非侵入式、无需修改模型权重；通过逐节点目标分配精确信用归因；通过调度参数实现收敛性控制。该方法在三个基准测试中一致超越强基线，且计算成本相近。

### Q4: 论文做了哪些实验？

论文在三个真实数据集上进行了实验：SubPOP（子群体分布预测）、HotpotQA（多跳问答）和LiveBench-Math（高中数学奥林匹克题）。SubPOP使用Wasserstein距离（WD）评估预测分布与真实分布的差异；HotpotQA采用distractor设置，报告答案级F1分数；LiveBench-Math衡量准确率。对比方法包括零样本、少样本（随机选取示例）以及GEPA（基于Pareto的候选选择与更新跳过机制），所有方法均使用GPT-4.1-mini作为基座模型。主要结果如下：GTBP在所有基准测试中均取得最优性能，相比最强基线GEPA，HotpotQA的F1从0.769提升至0.800（+4.0%），LiveBench-Math准确率从0.641提升至0.669（+4.4%），SubPOP的WD从0.116降至0.107（-7.8%）。在训练效率上，GTBP在LiveBench-Math和SubPOP上的LLM调用次数远少于GEPA（如SubPOP：12,700次 vs 1,639次），且推理时token使用量与GEPA在同一量级。此外，在SubPOP上的收敛性实验表明，GTBP的Wasserstein距离和排序匹配准确率在前几轮快速改善后逐渐稳定，提示长度单调增长而更新比例下降，验证了算法理论上的稳定性。

### Q5: 有什么可以进一步探索的点？

GTBP的理论分析依赖于“LLM优化器足够精确”等强假设，未来可探索在更弱假设下的收敛性证明，并分析多条子节点分支时的多目标歧义问题。针对当前仅验证一层隐藏层的工作流，可扩展至更深层图结构、工具调用或动态路由等实际场景。提示词更新导致长度持续增长，未来可引入合并冗余声明、联合优化任务损失与提示长度的预算机制，或采用记忆检索模块动态提取相关声明以降低推理成本。此外，与微调模型的对比中，GTBP在保持泛化能力时可能牺牲特定任务性能，可探索混合策略：对关键模块进行轻量级微调，同时保留上下文适应框架。最后，当前方法依赖人工设计或固定拓扑，可尝试利用强化学习或神经架构搜索自动发现最优工作流图结构。

### Q6: 总结一下论文的主要内容

本论文提出基于图的目标反向传播（GTBP）框架，用于多LLM智能体系统中的语境自适应。问题定义是：在由多个LLM模块构成的智能体工作流（有向无环图）中，现有方法难以准确分配各模块的贡献，且缺乏收敛保证。GTBP方法通过沿工作流图反向传播局部目标输出，利用目标与真实输出的差异指导各阶段提示的逐级更新。理论证明，该方法能实现提示更新的稳定性，且具备足够能力的LLM优化器可降低整体目标函数。三个基准实验表明，GTBP在保持相近计算成本的同时，持续优于强基线方法。核心贡献在于将基于梯度的反向传播思想引入多LLM系统，实现了精确的信用分配，为自动化提示工程提供了可收敛的理论框架，对复杂智能体工作流的自适应优化具有重要意义。
