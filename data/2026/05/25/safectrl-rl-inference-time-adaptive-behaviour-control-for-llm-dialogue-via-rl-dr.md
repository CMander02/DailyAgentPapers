---
title: "SafeCtrl-RL: Inference-Time Adaptive Behaviour Control for LLM Dialogue via RL-Driven Prompt Optimisation"
authors:
  - "Michael Orme"
  - "Yanchao Yu"
  - "Zhiyuan Tan"
date: "2026-05-25"
arxiv_id: "2605.25984"
arxiv_url: "https://arxiv.org/abs/2605.25984"
pdf_url: "https://arxiv.org/pdf/2605.25984v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent安全"
  - "推理时干预"
  - "RL驱动"
  - "对话安全"
  - "提示优化"
relevance_score: 8.5
---

# SafeCtrl-RL: Inference-Time Adaptive Behaviour Control for LLM Dialogue via RL-Driven Prompt Optimisation

## 原始摘要

Ensuring safe and contextually appropriate behaviour in Large Language Models (LLMs) remains a critical challenge for real-world deployment. We present \textbf{SafeCtrl-RL}, an inference-time behavioural control framework that enables adaptive safety regulation without model retraining or parameter modification. The method formulates dialogue generation as a sequential decision process, where a reinforcement learning agent dynamically selects prompt adjustment strategies based on contextual feedback. This allows unsafe behaviours to be suppressed through iterative refinement, which we conceptualise as inference-time behavioural unlearning. Evaluated across multiple LLMs and unsafe dialogue scenarios, SafeCtrl-RL consistently improves safety and response quality, outperforms existing prompt-based optimisation methods, and achieves favourable performance--efficiency trade-offs. **Warning: This paper may contain examples of harmful language, and reader discretion is recommended.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决大型语言模型（LLMs）在动态对话场景中推理时的安全与适应性行为控制问题。研究背景在于，LLMs 已广泛应用于教育、编程辅助等交互式对话系统，但其在实际部署中持续面临产生不安全或不合时宜输出的挑战。现有方法如微调、过滤和模型编辑等离线对齐技术，虽然有效，但存在明显不足：一方面，这些方法更新成本高，且难以应用于无法访问模型参数的黑盒场景；另一方面，它们缺乏在对话过程中根据动态变化的上下文进行实时调整的能力，导致在实时对话中的有效性受限。核心问题是：如何在不重新训练或修改模型参数的前提下，实现推理阶段的安全行为自适应调控？为此，本文提出了 SafeCtrl-RL 框架。该框架将对话生成建模为基于提示构建的序列决策过程，通过强化学习智能体，根据实时对话上下文和反馈信号动态选择并调整提示策略，通过迭代优化逐步抑制不安全输出，从而实现推理时的行为“反学习”，最终在不修改模型的情况下显著提升响应的安全性和质量。

### Q2: 有哪些相关研究？

相关研究主要分为参数编辑方法和基于提示的控制方法。参数编辑方法如ROME和MEMIT通过修改模型内部表征来更新或移除知识，但需白盒访问且离线运行，适用性有限。本文SafeCtrl-RL无需模型重训练或参数修改，属于推理时行为控制框架。提示控制方法通过输入条件调节行为，兼容黑盒模型，但通常依赖静态提示，适应性不足。改进的自校正方法引入多步优化但仍用固定策略。提示优化方法包括OPRO和GRIPS通过搜索或反馈信号改进提示，但通常离线优化或在部署时采用静态调整。本文创新在于将行为控制建模为推理时决策过程，基于安全质量反馈和交互历史动态调整提示策略，实现了上下文感知的自适应行为调节。其他关联工作包括推理时行为压制概念，本文将其具体化为推理时行为遗忘方法。在应用类研究中，多数方法优化单一安全维度，本文在多个不安全对话场景和语言模型上评估，兼顾安全性与回复质量。评测方面，本文对比了静态提示优化方法，在性能与效率权衡上更具优势。

### Q3: 论文如何解决这个问题？

SafeCtrl-RL将对话安全建模为一个闭环控制问题，通过强化学习驱动的提示优化实现推理时自适应行为控制。其核心是将对话生成视为顺序决策过程，在不修改模型参数或重新训练的情况下动态调整行为。

整体框架采用生成-评估-优化的闭环流程：首先，固定的LLM基于系统提示和用户输入生成响应；然后，安全-质量评估器对响应进行评分，该评分由质量分数（捕捉连贯性和相关性）和安全分数（基于细粒度的有害内容分类法）组成；最后，如果响应未达到预设阈值（0.9），RL代理根据当前状态选择提示调整策略，更新系统提示并重新生成。

主要组件包括：1）安全-质量评估器，基于DeepEval框架，使用Gemini 2.0 Flash计算质量和安全两个维度的分数；2）状态表示，将对话历史和优化过程编码为36维向量，包含元学习特征（优化进度、探索率）、分数特征（性能统计和策略有效性）和提示特征（危害类别、风险等级、结构特征）；3）动作空间，包含11种离散的提示调整策略，分为无历史访问、基于摘要和基于性能/轨迹三类；4）RL代理，采用ε-贪心策略学习策略π(a_t|S_t(k))，选择最优动作进行确定性提示更新。

关键技术在于：使用指数加权乘积作为奖励函数（r = q^(αβ) * s^((1-α)β)），并引入硬安全约束，当关键安全指标低于阈值（0.8）时奖励置零，确保安全与质量联合优化且安全不可妥协。

### Q4: 论文做了哪些实验？

为了全面评估SafeCtrl-RL的有效性，论文设计了三大互补实验。实验在统一的百万级不安全提示语料库（整合了PKU-SafeRLHF、TOXIC-DPO、BeaverTails和DarkSide DPO数据集，覆盖12种伤害类型）上进行，评测模型涵盖从1.5B到3.2B参数规模的多种LLM（包括未审查模型如BlackSheep-Llama3.2-3B和经微调对齐的模型）。

实验设置如下：
1.  **策略比较实验**：将SafeCtrl-RL与动作空间中的几种手动设计的固定提示调整策略（如raw_history、ai_enhanced、progressive）进行比较。目标是验证基于策略的自适应选择是否优于固定规则。主要结果：SafeCtrl-RL在所有模型和场景下均优于这些静态策略。
2.  **提示优化比较实验**：将SafeCtrl-RL与现有最先进的提示优化方法（如Evolutionary、TextGradient、GRIPS、OPRO等）进行比较。这些方法通过搜索或梯度技术优化提示，但不显式建模序列决策。主要结果：SafeCtrl-RL在安全性和响应质量上持续超越这些基线方法，并取得了更优的性能-效率权衡，其性能效率比（\(R_{perf}\)，即宏观性能提升除以迭代次数）更高。
3.  **保留研究**：通过移除SafeCtrl-RL后生成的响应与使用SafeCtrl-RL时生成的响应进行比较，评估行为改善的持久性和一致性。关键指标包括平均奖励变化（\(\Delta_{mean}\)）和保留率（Retention，即奖励≥0.8的样本百分比）。结果表明，SafeCtrl-RL诱导出的安全行为具有高度稳定性和一致性。

所有方法均基于初始无防护响应计算安全-质量分数（\(P_{Score}\)）及行为改善（\(\Delta P\)）进行评价。

### Q5: 有什么可以进一步探索的点？

首先，论文主要评估了弱对齐模型，后续可探索SafeCtrl-RL与GPT-4等高对齐指令微调模型的交互，分析其在该场景下是否仍能有效抑制不安全行为而不损害原有对齐能力。其次，未来应扩展至更多样化的模型架构（如Mamba、Falcon）和更大规模的安全分类体系，以验证框架的通用性和鲁棒性。第三，当前行为保持分析仅基于少数样本，后续需在全数据集上评估长期行为稳定性，并探索轻量级记忆机制以维持安全约束的持久性。最后，目前仅使用单一外部评估器，未来可引入多个具不同偏好的评估器（如基于人类偏好或不同价值体系的RLHF模型），并设计自适应评估器选择策略，使框架对评估器噪声更具鲁棒性。此外，结合在线学习或元学习技术，动态调整RL策略以适应对话分布漂移，也是潜在改进方向。

### Q6: 总结一下论文的主要内容

SafeCtrl-RL 提出了一种推理时行为控制框架，无需模型重训练或参数修改即可确保大型语言模型 (LLM) 对话的安全性和上下文适当性。该方法将对话生成形式化为一个顺序决策过程，其中强化学习智能体根据上下文反馈动态选择提示调整策略，通过迭代细化抑制不安全行为，可视为推理时的行为遗忘。实验表明，SafeCtrl-RL 在多个 LLM 和不安全对话场景中一致地提升了安全性与响应质量，优于现有的基于提示的优化方法，并取得了良好的性能-效率权衡。该工作的核心意义在于为需要动态适应的真实世界 LLM 部署提供了一种灵活、高效的安全控制方案。
