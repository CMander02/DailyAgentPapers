---
title: "Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation"
authors:
  - "Jingbo Wen"
  - "Liang He"
  - "Ziqi He"
date: "2026-06-03"
arxiv_id: "2606.04402"
arxiv_url: "https://arxiv.org/abs/2606.04402"
pdf_url: "https://arxiv.org/pdf/2606.04402v1"
categories:
  - "cs.AI"
tags:
  - "Agent推理"
  - "测试时计算分配"
  - "代价感知调度"
  - "SWE-bench"
  - "任务路由"
  - "边缘效用"
  - "成本加权损失"
relevance_score: 8.5
---

# Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation

## 原始摘要

Modern reasoning models can allocate different amounts of test-time computation, such as thinking tokens, model calls, or compute budget, to different tasks. Existing methods generally drive this allocation by predicted difficulty and spend more compute where it is expected to raise accuracy. This implicitly assumes that all failures cost the same, since an accuracy objective weights every task equally. However, such an assumption does not hold in deployment: A typo in a log message and a migration that corrupts a production database both count as one benchmark failure, but their real-world costs are fundamentally different. To fill this gap, we propose consequence-aware test-time compute allocation. Instead of routing compute only by predicted difficulty, we use a lightweight predictor to estimate from the issue text how costly a task would be if solved incorrectly. The scheduler then routes higher-consequence tasks to larger compute tiers or higher thinking budgets under the same total budget. We conduct main experiments on SWE-bench Lite and evaluate cross-dataset behavior on Multi-SWE-bench mini, covering 700 software-engineering tasks in total. Our results reveal that consequence and difficulty are approximately orthogonal under various annotations, and that current thinking models do not allocate compute sufficiently according to consequence. Moreover, our issue-only predictor never misclassifies a high-consequence task as low-consequence across the 300 SWE-bench tasks. Under matched compute budgets, our consequence-aware scheduler reduces cost-weighted loss by 22% to 33% relative to difficulty-aware routing; in particular, the priority-aware variant, which routes by per-task cost scaled by the marginal-utility signal, crosses 30%, and its deployable predictor-driven version retains over 90% of the oracle gain.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有自适应测试时计算分配方法中一个根本性的假设缺陷。当前研究背景是，现代推理模型（如OpenAI o系列、DeepSeek-R1等）能够根据任务难度动态分配思考时间或计算预算，其核心理念是“更困难的任务需要更多计算”。然而，现有方法存在一个关键不足：它们普遍以平均准确率为优化目标，隐含地假设所有任务失败的代价是相等的。但在实际部署场景中，这一假设完全不成立。例如，一个代码助手产生的“日志消息中的拼写错误”和“因竞态条件静默破坏生产数据库的迁移错误”，在基准测试中都只计为一次失败，但后者的实际成本远高于前者。这种“部署成本不对称”问题在当前的LLM自适应计算目标函数中被完全忽视了。为填补这一空白，本文提出了**后果感知的测试时计算分配**方法。其核心问题是：在保持总计算预算不变的前提下，如何根据任务错误后果的严重性来分配计算资源，而不仅仅是依据预测难度。该方法通过一个轻量级预测器从问题描述中预先估计错误成本，调度器据此将高后果任务分配给更大的计算层级或思考预算，从而显著降低代价加权损失。

### Q2: 有哪些相关研究？

该论文将相关工作归纳为四个类别。首先是**自适应测试时计算**，现有方法如训练奖励预测器根据预期准确率增益分配计算资源，或利用令牌级置信度提前停止生成，其共同目标是通过预测难度来提升平均准确率。本文与其核心区别在于：路由信号从“预测难度”转向“预测后果”，当两个任务预期准确率增益相似但失败成本差异巨大时，准确性驱动路由会将其等同对待，而本文的部署导向调度器则不会。

其次是**理性元推理**，该框架认为额外计算的价值取决于其效用是否超过成本，本文与之紧密契合，但现有工作多将效用操作化为准确率或奖励，而本文直接采用任务依赖的错误成本。

第三是**代价敏感学习与选择性预测**，相关工作承认错误代价不同，但前者通过修改训练目标或决策规则来调整，后者允许模型在不确定时弃权。本文的不同之处在于在计算时使用代价信号：模型仍需回答所有任务，但调度器根据代价决定计算量，这无需重新训练推理模型。

最后是**软件工程基准**，本文以SWE-bench Lite为主要实验平台，利用多SWE-bench子集进行跨数据集验证，该领域任务天然具有难度差异大和部署风险差异大的特点，适合验证后果感知分配的有效性。

### Q3: 论文如何解决这个问题？

论文提出了一种后果感知（Consequence-Aware）的测试时计算分配方法，用于替代传统的仅基于难度分配计算资源的方法。核心创新在于引入“后果”（consequence）作为任务的关键属性，即任务如果解决错误可能造成的实际部署成本，并将其作为计算资源分配的主要依据。

整体框架由两个主要模块构成：**后果预测器**和**后果感知调度器**。首先，后果预测器是一个轻量级模块，在部署阶段仅通过任务的问题文本（issue text）和文件路径，在无需查看最终修复补丁的情况下，预测出该任务的后果等级（低、中、高）。实验证明，该预测器能够可靠地避免将高后果任务误判为低后果任务，这是保证安全性的关键。其次，后果感知调度器接收预测的后果标签，在固定的总计算预算下，采用一种解耦的分配方案：将任务按预测后果从高到低排序，然后优先将高后果任务分配给更昂贵的计算层级（如更大的思考预算或更强的模型），直到总预算耗尽。

该方法的关键技术特点包括：1）完全是一个调度层方案，无需重新训练任何推理模型；2）预测器只需在序数上正确（确保高后果任务不会被分配到最低层级），而不是绝对标签精确；3）性能表现良好，在SWE-bench Lite基准测试中，与同等预算的基于难度的调度方法相比，该方法将成本加权损失降低了22%至33%。

### Q4: 论文做了哪些实验？

论文基于SWE-bench Lite（300个任务）和Multi-SWE-bench mini（共计700个软件工程任务）进行实验。实验设置了一个16模型计算层基准测试，将模型按解决数分为廉价层（底部4个）和优质层（顶部4个），固定价格比率4:1。对比了七种分配策略：随机、难度感知（Snell风格）、后果感知（使用Qwen或Claude预测器）、后果感知（oracle，使用LLM补丁标签）、优先级感知（预测器/oracle，结合后果与边际收益）。主要结果在将25%任务路由到优质层的匹配预算下，以代价加权损失为指标：难度感知损失268.25（基准0%），随机233.00（+13.1%），后果感知（Claude预测器）220.50（+17.8%），后果感知（Qwen预测器）209.75（+21.8%），后果感知（oracle）205.75（+23.3%），优先级感知（Qwen预测器）186.00（+30.7%），优先级感知（oracle）179.75（+33.0%）。可部署的Qwen预测器保留了93.6%的后果感知oracle增益和92.9%的优先级感知oracle增益。实验进一步分析了难度感知分配失效原因：在控制难度和通过率方差后，后果与边际增益的偏Spearman相关为+0.696（p<10^{-43}），且增加后果将使仅含难度和通过率方差的R²从0.474提升至0.738（绝对提升26.4个百分点）。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向**

当前研究存在以下局限：首先，代价标签的获取依赖人工标注或规则映射，缺乏自动化的动态代价评估机制，难以覆盖长尾任务。其次，实验仅聚焦软件工程任务，未验证代码生成、数学推理等领域的泛化性。此外，调度策略仅基于单任务代价，未建模任务间代价依赖关系（如连锁故障成本）。

未来可探索的方向包括：1）利用LLM自我反思或历史错误数据库自动生成代价因子，结合贝叶斯优化动态更新代价分布；2）将代价感知与任务间依赖图结合，对关键路径上的任务分配更高计算预算。3）引入代价校准机制，通过对比学习对齐模型对任务代价的预估值与真实成本。4）设计多目标调度策略，在计算预算、响应延迟与后果风险之间做帕累托优化。5）探索代价感知与简单性/确定性维度的联合路由，避免高代价易错任务被误判。这些方向将推动推理计算分配从“性能最大化”转向“风险最小化”的实用范式。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种后果感知的测试时计算分配方法，旨在解决现有自适应计算分配中“将所有错误视为等代价”的缺陷。在部署场景中，不同任务出错的实际成本差异巨大（例如日志拼写错误 vs. 数据库损坏），而现有方法仅根据任务难度分配计算资源，忽略了这种代价不对称性。作者在SWE-bench（700个软件工程任务）上定义并测量了任务的后果严重性，发现后果与难度几乎正交。通过审计现有推理模型，发现它们（如Qwen3、Claude）对后果的敏感性不足。为此，作者提出一个轻量级预测器，仅从问题文本估算任务后果，并由调度器据此将高后果任务路由到更高的计算层。实验结果表明，在相同总预算下，该后果感知调度器相比难度感知路由，将代价加权损失降低了22%至33%。其中，结合了边际效用信号的优先级感知变体降低了超过30%的损失，且其可部署的预测器驱动版本保留了90%以上的性能增益。
