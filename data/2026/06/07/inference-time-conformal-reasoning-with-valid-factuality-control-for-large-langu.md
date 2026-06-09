---
title: "Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models"
authors:
  - "Ting Wang"
  - "Yuanjie Shi"
  - "Yan Yan"
  - "Huan Zhang"
date: "2026-06-07"
arxiv_id: "2606.08831"
arxiv_url: "https://arxiv.org/abs/2606.08831"
pdf_url: "https://arxiv.org/pdf/2606.08831v1"
categories:
  - "cs.AI"
tags:
  - "LLM推理"
  - "置信预测"
  - "事实性控制"
  - "推理图"
  - "不确定性量化"
  - "多步推理"
  - "推理时校准"
relevance_score: 8.5
---

# Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models

## 原始摘要

Large language models (LLMs) increasingly perform multi-step reasoning, where intermediate claims form implicit directed acyclic graphs whose node correctness is structurally conditioned on their ancestors. This makes factuality uncertainty structural, rather than a trivial accumulation of node-wise errors, and necessitates inference-time uncertainty quantification over the reasoning structure. While conformal prediction (CP) offers flexible user-specified factuality control, existing work remains post-hoc and cannot intervene during generation. To fill the gap between CP's flexibility and its post-hoc limitation, we propose an \emph{Inference-Time Conformal Reasoning (ITCR)} framework that integrates CP directly into reasoning graph generation. ITCR learns a structure-level factuality uncertainty function that aggregates claim-level factuality signals over reasoning graphs without complex modeling assumptions. We then design the non-conformity score based on graph-level factuality uncertainty and calibrate the conformal threshold to decide when to stop generation. We theoretically show such generation is nested, yielding valid coverage guarantees for factuality control. Experiments over multiple datasets and coverage objectives demonstrate empirically valid coverage. In downstream reasoning tasks, inference-time calibrated graphs yield more accurate generation than post-hoc pruned graphs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在多层推理过程中缺乏有效的实时事实性控制问题。研究背景是，LLM越来越多地执行多步骤推理，其中间步骤的依赖关系形成一个有向无环图，节点的正确性结构性地依赖其祖先节点，导致事实性不确定性是结构性的，而非节点级错误的简单累积。现有方法如共形预测虽能提供灵活的用户指定事实性保证，但仅作为后处理应用：先完整生成多步骤回答，再对候选子集进行共形过滤并强制祖先闭合约束。这种后验方式存在根本缺陷：校准仅针对已生成内容，无法干预生成过程本身，导致生成过程中的事实性错误无法及时遏制。本文要解决的核心问题是：能否将共形预测直接集成到推理图生成过程中，实现推理时的事实性控制，同时保留覆盖保证。为此，论文提出推理时共形推理框架，通过学习结构级事实性不确定性函数，聚合推理时的节点级信号，并基于图级非一致性分数校准阈值，在生成过程中动态决定是否停止扩展，从而确保输出的推理图满足事实性覆盖保证。

### Q2: 有哪些相关研究？

### 相关研究

1. **方法类：不确定量化与预言校准**  
   现有工作多聚焦于LLM推理中的节点级不确定性评估（如自洽性评分、置信度校准），但忽略结构依赖性。本文基于预言预测（CP）提出结构级不确定性聚合函数，可处理推理图的条件依赖，实现生成过程中的事实性控制，区别于传统后验修剪方法。

2. **应用类：推理生成与事实性控制**  
   相关研究包括利用思维链（CoT）或树搜索（ToT）进行多步推理，但缺乏对中间断言事实性的动态干预。本文首次在生成阶段集成CP，通过校准非一致性阈值动态决定停止生成时机，相比后验修剪图可输出更准确的推理结构。

3. **评测类：覆盖保证与推理准确性**  
   现有评测主要对比生成结果的事实性（如TruthfulQA），但未验证结构级覆盖保证。本文在多数据集上证明经验覆盖与理论有效覆盖的一致性，并揭示推理时剪枝图相比后验图在下游任务中精度更高，填补了CP灵活性与生成干预之间的空白。

### Q3: 论文如何解决这个问题？

为了解决推理时事实性控制问题，论文提出了**推理时共形推理（ITCR）框架**，将共形预测（CP）直接集成到推理图生成过程中，实现有覆盖率保证的结构化生成。

核心方法包括：
1. **图级事实不确定性函数**：ITCR学习一个参数化的图级不确定性函数 \(\FU_\theta\)，该函数以当前生成的子图 \(U\) 和节点级不确定性分数 \(\{ \fu(v) \}\) 为输入，输出一个连续的不确定性分数。由于图级事实性是二元谓词，该学习过程简化为二元分类任务，且其准确性不影响共形覆盖的有效性，只影响效率。

2. **嵌套非一致性分数**：为实现推理时停止，设计了满足嵌套属性的非一致性分数 \(S(U) = 1 - \sigma(\FU_\theta(U, \cdot)) + \lambda |V_U|\)。其中，第一项捕获模型的不确定性，第二项是节点数惩罚项。通过设置足够大的 \(\lambda\) 来抵消模型项的非单调波动，保证该分数在子图扩展时单调递增，使阈值交叉不可逆，从而无需回溯。

3. **共形校准与阈值停止**：在校准阶段，基于无假或无漏目标收集子图的非一致性分数，并计算相应分位数作为阈值 \(\tau_\alpha\)。推理时，算法从根节点子图开始，逐步扩展当前子图并检查分数 \(S(U^t)\) 是否超过阈值。若未超过，则接受当前子图并继续扩展；若超过，则停止，并返回上一个被接受的子图作为最终预测。

主要创新点：
- **推理时干预**：区别于事后剪枝，ITCR在生成过程中动态决定何时停止，保证输出子图是祖先闭包且事实性可控。
- **理论保证**：形式化证明了嵌套属性与非一致性分数的单调性相结合，能在无分布假设下为无假覆盖和无漏覆盖提供有效的边际覆盖率保证。
- **灵活性**：框架兼容任何置换不变模型（如线性模型、图神经网络）作为不确定性函数，且共形校准与模型精度解耦，确保了鲁棒性。

### Q4: 论文做了哪些实验？

论文在MATH、GSM8K和QA三个数据集上进行了实验。实验设置包括：使用标注了子句事实正确性的数据集，按祖先闭包准则生成子集级标签，并随机划分为学习图级事实不确定性函数、共形校准和测试三个子集。对比方法包括基线CPL（基于LLM的个体声明级事实风险估计）及ITCR的变体（ITCR-MAX、ITCR-SUM、ITCR-AVG，采用不同的节点级不确定性聚合方式）。在两个覆盖目标（无假覆盖和无漏覆盖）和两个误覆盖水平（α=0.05和α=0.10）下评估经验覆盖率和效率。

主要结果：ITCR在所有数据集、覆盖目标和误覆盖水平上均实现有效覆盖（经验覆盖率接近目标1-α），且效率最高。例如，在MATH数据集无假目标α=0.10下，ITCR覆盖率为0.908±0.07，效率34.77%；而CPL覆盖率仅0.624±0.10且违反覆盖要求。在GSM8K无漏目标α=0.05下，ITCR覆盖率为0.945±0.04，效率2.15%。此外，敏感性分析显示，使用MLP、随机森林或SVM实现图级不确定性函数时，ITCR均能保证有效覆盖，但MLP效率最高。下游推理任务中，ITCR生成的图比后剪枝图更准确。嵌套性条件在实践中可满足，违反率随λ增加单调降至0。

### Q5: 有什么可以进一步探索的点？

论文的核心创新在于将共形预测（CP）与推理图生成过程相结合，实现了推理阶段的实时事实性控制。然而，该方法存在几个值得进一步探索的局限性。首先，当前的非一致性分数基于图级别的事实性不确定性聚合，可能忽略了推理图中不同路径或子结构对最终输出的差异化影响。未来可以探索更精细的、路径敏感的不确定性度量，例如为关键推理链赋予更高权重。其次，该方法假设生成过程是嵌套的，但实际推理中，随着新节点的添加，早期节点的置信度可能动态变化，破坏了嵌套假设。因此，研究非嵌套或部分可交换的共形预测框架，以处理推理图的非单调不确定性演化，是一个重要方向。此外，该工作主要关注“停止生成”的时机，但未涉及如何回溯修正早期错误节点。未来可集成主动回溯机制，在检测到高不确定性时触发局部重生成或纠错，形成“生成-验证-修正”的闭环。最后，将该框架扩展到多模态推理（如视觉-语言链式推理）也是极具潜力的方向，因为此时不确定性来源更加异构和复杂。

### Q6: 总结一下论文的主要内容

大型语言模型进行多步推理时，中间断言形成隐式有向无环图，其节点正确性在结构上依赖于祖先节点，这使得事实性不确定性具有结构性，而非简单节点错误的累积。为在推理过程中对此类结构进行不确定性量化，论文提出了一种推理时间共形推理（ITCR）框架。该方法学习一种结构层面的事实性不确定性函数，该函数能聚合推理图上的断言级事实性信号，无需复杂建模假设；并基于此设计非一致性分数，校准共形阈值以决定何时停止生成。理论证明这种生成是嵌套的，能保证事实性控制的有效覆盖。实验表明该方法在多数据集和覆盖目标上实现了经验有效覆盖，且在推理任务中，经推理时间校准的图比事后剪枝的图能生成更准确的结果。核心贡献在于将共形预测直接集成到推理图生成中，实现了灵活且可验证的事实性控制。
