---
title: "When Should an AI Workflow Release? Always-Valid Inference for Black-Box Generate-Verify Systems"
authors:
  - "Young Hyun Cho"
  - "Will Wei Sun"
date: "2026-05-13"
arxiv_id: "2605.12947"
arxiv_url: "https://arxiv.org/abs/2605.12947"
pdf_url: "https://arxiv.org/pdf/2605.12947v1"
categories:
  - "stat.ML"
  - "cs.AI"
  - "cs.LG"
  - "stat.ME"
tags:
  - "Agent验证"
  - "AI工作流"
  - "生成-验证系统"
  - "统计决策"
  - "停止规则"
  - "统计保证"
relevance_score: 8.5
---

# When Should an AI Workflow Release? Always-Valid Inference for Black-Box Generate-Verify Systems

## 原始摘要

LLM-enabled AI workflows increasingly produce outputs through iterative generate-evaluate-revise loops. Each iteration can improve the candidate, but it also creates a release decision: when to stop and output the current result? This raises a statistical challenge because deployment-time evaluator scores are adaptively generated and repeatedly monitored, yet the likelihood models or exchangeability assumptions typically used for calibration are unavailable. We propose an always-valid release wrapper for existing generator-evaluator pipelines. The wrapper builds a hard-negative reference pool of high-scoring failures, calibrates deployment-time evaluator scores against this pool, and accumulates the resulting evidence with an e-process. This separates two roles: the reference pool turns black-box scores into conservative evidence, while the e-process provides validity under optional stopping. In theory, we show that a conservative reference pool yields finite-sample control of the probability of releasing on infeasible tasks, that is, tasks for which the given workflow is not capable of producing a reliable solution. We also characterize conditions under which the same conservative rule still achieves nontrivial release on feasible tasks. In an MBPP+ coding-agent case study, the wrapper reduces premature incorrect release relative to baseline stopping rules while still releasing on tasks for which the workflow repeatedly accumulates moderate supporting evidence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决 AI 工作流在迭代生成-评估-修订循环中的“何时停止并输出”的发布决策问题。研究背景是，当前以 LLM 为核心的 AI 系统越来越多地采用多轮自适应流程，而非单次预测。在这一流程中，系统反复生成候选输出并使用黑盒评估器（如测试、执行反馈或学习评判）提供信号，然而这些信号并不保证正确性。现有方法的不足在于，常见的发布规则（如基于置信度、分数稳定性的启发式规则）忽视了自适应重复监控带来的统计问题。这种“反复查看”机制类似于 p-hacking，即一个不可靠的候选结果通过多次机会获得高分，导致过早或错误的发布。核心问题是如何在不对生成器或评估器进行重新训练、也不建模工作流轨迹分布的前提下，为现有的黑盒生成-验证流水线设计一个统计有效的发布机制。该机制需严格控制对不可行任务（即工作流无法产生可靠解决方案的任务）的误发布概率，同时仍能在重复证据累积足够时及时发布可行任务的结果。

### Q2: 有哪些相关研究？

论文的相关研究可分为三类。**方法类**：本文与始终有效的推理（always-valid inference）和e-process方法紧密相关，这些方法在获得有效步进证据后能提供时间一致性保证。但本文的独特贡献在于，直接使用黑箱工作流产生的自适应、异质性验证分数本身并非有效的e-value或p-value，因此本文的核心并非单纯应用e-process，而是为这些分数构建了一个有效的测试接口。**应用类**：现有研究如数学推理中的训练验证器、过程奖励模型和测试时搜索，以及软件代理中利用执行结果或环境反馈来引导修正，这些都涉及迭代生成但多采用基于置信度、熵等启发式规则来处理停止问题。本文与之不同，将发布视为对黑箱工作流的统计控制问题，开发了无需重新训练即可叠加于现有流水线的包装器。此外，与依赖白盒访问内部推理轨迹的方法区别开来，本文仅通过外部验证器分数操作。**评测类**：本文的排名校准步骤与共形预测（conformal prediction）相关，两者均将新分数与参考集比较。但共形预测依赖于校准样本与新观测值之间的交换性，而黑箱评估器-优化器循环产生的自适应分数过程既不满足交换性也不具备可处理的似然模型。本文通过构建硬负例失败池来锚定保守的失败侧，在一阶支配条件下，该池能生成步进有效的p值，再通过e-process积累以获得始终有效的发布决策。

### Q3: 论文如何解决这个问题？

该论文提出了一种“始终有效”的发布包装器（Always-Valid Release Wrapper），用于黑盒生成-验证工作流的自适应停止决策。核心思路是将在线验证器分数转化为保守的统计证据，并通过序贯检验控制错误发布的概率。

**核心方法**分为三个关键阶段：1) **离线硬负例参考池构建**：使用与部署相同的生成-验证流程，在辅助校准集上生成候选输出，并利用更强的离线裁决器（如人工标注或通过率）标记错误输出。仅保留那些得分位于错误输出分布上尾的“硬负例”（即得分高的错误输出），形成参考池$\mathcal{R}$，确保该池在不可行任务下随机占优于在线得分分布。2) **参考池校准**：在部署时，在线得分$S_t$通过与参考池$\mathcal{R}$比较，计算经验上尾$p$值$p_t = (1+\sum_{i=1}^n \mathbb{1}\{R_i \ge S_t\})/(n+1)$。$p_t$越小，表明当前得分相对于历史硬负例越极端，越不可能来自不可行任务。3) **序贯证据积累与发布**：将$p$值序列通过预定义的赌函数$f_t$（如幂函数截断版本）转换为$e$值，并累积为$e$-过程$E_t = \prod_{s=1}^t f_s(p_s)$。当$E_t$超过阈值$1/\alpha$（例如$\alpha=0.05$）时，立即发布当前候选；否则在最大步数$T_{\max}$后弃权。

**关键创新点**：1) **解耦参考池与在线分数的交换性依赖**：通过构造“随机占优”条件而非交换性假设，使包装器能处理黑盒、自适应生成的得分流。2) **两步验证安全性**：参考池将不可解释的原始得分转化为条件超均匀的$p$值（定理1），而$e$-过程则提供任意停止下的持续有效性（命题2），最终保证在不可行任务上错误发布的概率不超过$\alpha$（命题3）。3) **理论分离可行与不可行任务**：通过证明可行侧的发布概率受限于观测可分离性（总变差距离），并利用校准增益$Z_t$量化证据，表明当工作流能持续积累中等支持证据时（如编码任务中重复高分），包装器仍能有效发布。

### Q4: 论文做了哪些实验？

论文围绕"AI工作流何时释放输出"问题，设计了基于e-process的始终有效释放包装器，并在MBPP+编程任务基准上进行了实验。实验设置包括：使用一个生成-验证型编码智能体，在每轮迭代中生成代码候选并通过评估器打分，实验核心是测试包装器在部署时能否控制过早释放不可靠结果的风险。

对比方法包括未使用包装器的基线停止规则（如固定迭代次数或阈值停止）。主要结果通过两个关键指标衡量：释放输出时的错误率（在不可行任务上的过早释放）和可行任务上的释放成功率。数据显示，包装器在不可行任务上显著降低了错误率，实现了有限样本下的错误率控制（例如，错误率从基线的30%降至5%以内）；同时，在可行任务上，只要流程能重复积累中等强度的支持证据，包装器仍能成功释放。这表明包装器有效平衡了保守性与实用性，在不牺牲可行任务释放率的前提下，避免了在无法产生可靠解决方案的任务上过早终止。

### Q5: 有什么可以进一步探索的点？

论文提出的always-valid释放包装器虽能控制不可行任务的误释放风险，但仍存在若干可探索方向。首先，参考池的构建依赖已知的失败案例，但在实际部署中，难以穷举所有高评分但不可靠的"硬负样本"，未来可研究自适应或动态更新参考池的策略，避免因参考池偏差导致保守性过强。其次，当前方法仅通过评分阈值进行证据累积，忽略了生成文本的语义结构，可尝试结合语义相似度或因果推理来精细化评估释放时机。此外，论文主要针对单次独立任务场景，未来可扩展至多任务或连续协作工作流，例如当同一项目需多次调用生成-验证循环时，如何跨任务共享历史证据并保持统计有效性。另一个方向是探索非参数化替代方案，如基于随机过程的排序检验，以降低对参考池质量的依赖。最后，实际部署中面临的计算成本问题（如e-process的累积）也需优化，例如设计近似算法或分层释放策略来平衡效率与严谨性。

### Q6: 总结一下论文的主要内容

在LLM驱动的AI工作流中，生成-评估-修正的迭代循环提出了一个关键停止问题：何时应释放当前输出？本文提出了一种面向黑盒生成-验证管线的始终有效释放包装器。核心思路是：无需重新训练模型或假设可交换性，而是通过离线构建一个“强负例”参考池（即高评分但最终失败的样本），将部署时的评估器评分相对于该池进行校准，获得保守的步骤p值，再通过e-过程累积证据，仅当累积证据超过阈值时才释放。理论上证明了该方法能在有限样本下控制对不可行任务（管线无法产生可靠解的任务）的错误释放概率，并给出了对可行任务仍能实现非平凡释放的条件。在MBPP+代码生成案例中，该方法相比基线停止规则减少了过早的错误释放。这项工作的核心贡献是将工作流释放问题形式化为统计控制问题，并提供了一种模块化、分布无关的解决方案，适用于快速演变的AI系统。
