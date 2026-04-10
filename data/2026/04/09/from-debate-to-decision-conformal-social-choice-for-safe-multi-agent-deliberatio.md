---
title: "From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation"
authors:
  - "Mengdie Flora Wang"
  - "Haochen Xie"
  - "Guanghui Wang"
  - "Aijing Gao"
  - "Guang Yang"
  - "Ziyuan Li"
  - "Qucy Wei Qiu"
  - "Fangwei Han"
  - "Hengzhi Qiu"
  - "Yajing Huang"
  - "Bing Zhu"
  - "Jae Oh Woo"
date: "2026-04-09"
arxiv_id: "2604.07667"
arxiv_url: "https://arxiv.org/abs/2604.07667"
pdf_url: "https://arxiv.org/pdf/2604.07667v1"
categories:
  - "cs.AI"
  - "cs.MA"
  - "cs.SI"
tags:
  - "多智能体辩论"
  - "安全决策"
  - "共形预测"
  - "不确定性校准"
  - "人机协作"
  - "社会选择"
  - "后处理层"
  - "可解释性"
relevance_score: 8.0
---

# From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation

## 原始摘要

Multi-agent debate improves LLM reasoning, yet agreement among agents is not evidence of correctness. When agents converge on a wrong answer through social reinforcement, consensus-based stopping commits that error to an automated action with no recourse. We introduce Conformal Social Choice, a post-hoc decision layer that converts debate outputs into calibrated act-versus-escalate decisions. Verbalized probability distributions from heterogeneous agents are aggregated via a linear opinion pool and calibrated with split conformal prediction, yielding prediction sets with a marginal coverage guarantee: the correct answer is included with probability ${\geq}\,1{-}α$, without assumptions on individual model calibration. A hierarchical action policy maps singleton sets to autonomous action and larger sets to human escalation. On eight MMLU-Pro domains with three agents (Claude Haiku, DeepSeek-R1, Qwen-3 32B), coverage stays within 1--2 points of the target. The key finding is not that debate becomes more accurate, but that the conformal layer makes its failures actionable: 81.9% of wrong-consensus cases are intercepted at $α{=}0.05$. Because the layer refuses to act on cases where debate is confidently wrong, the remaining conformal singletons reach 90.0--96.8% accuracy (up to 22.1pp above consensus stopping) -- a selection effect, not a reasoning improvement. This safety comes at the cost of automation, but the operating point is user-adjustable via $α$.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体辩论系统中一个关键的安全性问题：智能体之间达成的一致意见并不等同于正确答案，但现有系统却将这种共识直接转化为自动化决策，导致错误无法被拦截。研究背景是，大型语言模型通过多智能体辩论可以提升推理能力，但辩论过程存在社会强化效应，即智能体可能迫于群体压力而收敛于一个错误的答案，形成“错误共识”。现有方法（如多数投票或基于稳定性的停止机制）的不足在于，它们仅将共识作为停止信号和决策依据，无法评估共识的正确性，也无法量化决策风险，从而可能导致系统在高度自信的情况下执行错误操作。

本文要解决的核心问题是将多智能体辩论从单纯的答案选择重构为风险可控的行动选择。具体而言，作者提出了一种名为“Conformal Social Choice”的后处理决策层，它不依赖于模型内部的校准，而是通过聚合异构智能体输出的概率分布，并应用分裂共形预测技术，生成具有边际覆盖保证的预测集合。该机制能够根据用户设定的风险水平（α），在答案置信度不足时自动升级至人工处理，从而在保持自动化效率的同时，显著拦截错误共识，提升最终执行决策的准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体辩论与意见动态、用于大语言模型的共形预测，以及言语化置信度与社会选择。

在多智能体辩论方面，已有工作通过辩论提升事实性与推理能力，并研究了停止标准、与投票的比较、博弈论建模及交叉审问等。这些研究关注如何改进辩论过程或何时停止，而本文则解决部署层面的关键问题：系统应在何时被允许自主行动，何时应拒绝行动并升级给人类处理。

在共形预测方面，已有方法（如APS、RAPS）为LLM构建无分布预测集，并应用于多项选择问答、开放生成等场景。与本文最相关的是“辩论即优化”工作，它将共形预测用作辩论中的内部过滤器，但破坏了标准覆盖保证且需白盒访问。本文则采用标准的分割共形预测，将其作为后处理层应用于最终集体信念，在完全黑盒设置下保持了清晰的边际覆盖保证。

在言语化置信度与社会选择方面，现有研究主要集中于单智能体的不确定性言语化表达（如语义不确定性、自我一致性）。社会选择传统上关注赢家选择。本文的创新在于，通过线性意见池聚合多个异质智能体的言语化概率分布，并后接共形校准，从而将社会选择扩展至无需假设个体校准良好的集值风险控制。

### Q3: 论文如何解决这个问题？

论文通过提出“Conformal Social Choice”这一后处理决策层来解决多智能体辩论中“共识不等于正确”的安全风险问题。其核心方法是将辩论输出转化为具有边际覆盖保证的预测集，并基于集大小制定分层的自动化决策策略。

整体框架是一个四阶段流程：首先，由异构的LLM智能体进行多轮辩论，每轮每个智能体输出一个**言语化的概率分布**（而非仅投票或argmax），这些分布通过**线性意见池**（加权平均）聚合成一个“社会概率”分布。这一设计保留了偏好强度信息，优于多数投票。其次，基于社会概率定义**非一致性分数**（如 \( 1 - P_{\text{social}}(y|x) \)），用于衡量每个候选标签与社会共识的偏离程度。接着，利用一个保留的校准集，通过**分裂共形预测**计算一个分位数阈值 \(\hat{q}\)，使得对于新的测试样本，其真实标签被包含在预测集中的概率至少为 \(1-\alpha\)（用户设定的错误覆盖率）。这一覆盖保证仅需数据可交换性假设，不依赖单个模型的校准质量。最后，根据阈值构建预测集 \(\mathcal{C}(x) = \{ y : P_{\text{social}}(y|x) \geq 1-\hat{q} \}\)，并执行**分层行动策略**：若预测集为单例（即最高社会概率足够高且与次高者差距足够大），则系统自主执行该答案；若预测集包含多个候选，则升级给人类专家处理；若预测集为空，则标记为异常进行全人工审查。

关键技术包括：1) **言语化概率聚合**：通过结构化提示获取各智能体的显式概率分布，即使存在噪声或偏差，共形校准仍能保证覆盖。2) **社会概率与线性意见池**：以加权和方式聚合分布，保留了置信度差异，并满足匿名性、中立性等社会选择性质。3) **共形校准**：将启发式的社会概率转化为具有统计保证的预测集，核心创新在于将共形预测应用于多智能体辩论的输出，提供了风险可控的决策契约。4) **基于集大小的行动策略**：将统计不确定性直接映射到“自动化 vs. 升级”的操作决策，使得辩论失败时（如错误共识）能够被有效拦截（实验显示81.9%的错误共识案例在α=0.05时被拦截），而剩余被自动化执行的单例预测集准确率显著提升（达90.0–96.8%）。这一提升并非源于推理改进，而是共形层对高不确定性案例的筛选效应。整个方法作为后处理层，不修改辩论过程本身，保持了模块化和用户可通过α调整风险与自动化水平的特性。

### Q4: 论文做了哪些实验？

实验在MMLU-Pro数据集上进行，该数据集包含数学、物理、化学、法律、工程、经济、健康和心理学八个专业领域的十选项多项选择题。实验使用三个异构大语言模型（Claude Haiku、DeepSeek-R1和Qwen-3 32B）进行四轮辩论，温度设为0.7。主要对比方法是基于共识的停止规则（一旦智能体达成一致就输出答案），而本文提出的方法是“共形社会选择”，即通过线性意见池聚合智能体输出的概率分布，并使用分割共形预测进行校准，以生成具有边际覆盖保证的预测集。

实验评估了边际覆盖率、平均预测集大小、单例率（预测集大小为1的样本比例）和单例准确率（单例样本中的准确率）等指标。共形预测在α=0.05（目标覆盖率95%）时，各领域和轮次的实际覆盖率在93.0%至97.6%之间，接近理论目标。平均预测集大小随领域难度自适应变化，例如在数学领域（较易）第三轮平均大小仅为1.01，而在法律领域（较难）为6.91。关键发现是，共形决策层能有效拦截错误共识：在α=0.05时，81.9%的错误共识案例被拦截（即预测集大小>1，从而升级为人工审核），这使得最终被自动执行的单例预测准确率高达90.0%至96.8%，比共识停止规则的最高提升达22.1个百分点（法律领域）。然而，这种安全性的代价是自动化率降低，例如法律领域仅有6.2%的样本被解析为单例。实验结果表明，共形层并未提升推理能力，而是通过选择性地拒绝高不确定性的案例来实现更高的行动可靠性。

### Q5: 有什么可以进一步探索的点？

论文的局限性为未来研究提供了明确方向。首先，其边际覆盖保证无法确保每个子组或特定难度实例的覆盖，未来可探索条件性覆盖方法，如基于分组的校准或贝叶斯后验界限，以提升对困难样本的可靠性。其次，方法依赖数据可交换性假设，在实际分布漂移场景中可能失效，未来可集成在线保形预测方法，实现动态适应。此外，当前依赖语言模型输出的概率存在噪声和解析偏差，未来可研究更鲁棒的概率提取与校准技术，例如通过强化学习优化提示或直接建模置信度。计算成本方面，多轮辩论导致高延迟，未来可探索轻量级辩论架构或异步协作机制。最后，当前方法限于封闭选项任务，未来需扩展至开放生成场景，例如通过候选生成与保形过滤结合，以处理无界输出空间。这些改进有望在保持安全性的同时，进一步提升自动化决策的效率和适用范围。

### Q6: 总结一下论文的主要内容

该论文针对多智能体辩论中“共识不等于正确”的安全隐患，提出了一种名为“Conformal Social Choice”的后处理决策框架。核心问题是：当多个语言模型通过辩论达成一致但可能错误时，如何避免将错误共识直接转化为自动化行动。方法上，该框架首先汇集异构智能体输出的概率分布，通过线性意见池进行聚合，再利用分割共形预测进行校准，生成具有边际覆盖保证的预测集合（即正确答案以至少1-α的概率被包含）。随后，一个分层行动策略将单点集映射为自主行动，将多点集升级为人工审核。主要结论显示，在八个MMLU-Pro领域上的实验表明，该框架在α=0.05时能拦截81.9%的错误共识案例，而剩余被允许自主行动的单点集准确率高达90.0%-96.8%。这并非提升了推理能力，而是通过校准拒绝产生的选择效应。其核心贡献在于为多智能体审议提供了一个具有统计保证的安全决策机制，将失败转化为可操作的升级决策，在保证安全性的同时允许用户通过调整α来权衡自动化程度。
