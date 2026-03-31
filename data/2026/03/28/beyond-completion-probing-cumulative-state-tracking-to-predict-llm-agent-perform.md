---
title: "Beyond Completion: Probing Cumulative State Tracking to Predict LLM Agent Performance"
authors:
  - "Dengzhe Hou"
  - "Lingyu Jiang"
  - "Deng Li"
  - "Zirui Li"
  - "Fangzhou Lin"
  - "Kazunori D Yamada"
date: "2026-03-28"
arxiv_id: "2603.27343"
arxiv_url: "https://arxiv.org/abs/2603.27343"
pdf_url: "https://arxiv.org/pdf/2603.27343v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "State Tracking"
  - "Working Memory"
  - "Probing"
  - "Benchmarking"
  - "Model Capability Analysis"
  - "Reasoning"
relevance_score: 7.5
---

# Beyond Completion: Probing Cumulative State Tracking to Predict LLM Agent Performance

## 原始摘要

Task-completion rate is the standard proxy for LLM agent capability, but models with identical completion scores can differ substantially in their ability to track intermediate state. We introduce Working Memory Fidelity-Active Manipulation (WMF-AM), a calibrated no-scratchpad probe of cumulative arithmetic state tracking, and evaluate it on 20 open-weight models (0.5B-35B, 13 families) against a released deterministic 10-task agent battery. In a pre-specified, Bonferroni-corrected analysis, WMF-AM predicts agent performance with Kendall's tau = 0.612 (p < 0.001, 95% CI [0.360, 0.814]); exploratory partial-tau analyses suggest this signal persists after controlling for completion score and model scale. Three construct-isolation ablations (K = 1 control, non-arithmetic ceiling, yoked cancellation) support the interpretation that cumulative state tracking under load, rather than single-step arithmetic or entity tracking alone, is the primary difficulty source. K-calibration keeps the probe in a discriminative range where prior fixed-depth benchmarks become non-discriminative; generalization beyond this open-weight sample remains open.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前评估大型语言模型（LLM）智能体能力时过度依赖“任务完成率”这一单一指标的问题。研究背景是，随着LLM被越来越多地用于构建需要执行多步骤任务的智能体，准确评估其底层能力变得至关重要。现有方法（如HotpotQA、AgentBench等基准测试）主要关注智能体最终是否完成任务（即“完成率”），但作者指出这存在“完成谬误”——即使完成率相同，模型在追踪和处理多步骤任务中的中间状态（即过程能力）上可能存在巨大差异，而这种差异对于智能体在复杂场景中的可靠行为至关重要。

因此，本文要解决的核心问题是：如何超越最终完成率，去探测和量化LLM智能体在执行多步骤任务时，其“累积状态追踪”这一关键过程能力，并验证该能力是否能有效预测智能体在下游任务中的实际表现。为此，论文引入了名为WMF-AM的校准化探测方法，专门针对“负载下的累积算术状态追踪”能力进行测量。通过在一系列模型上的实验，论文旨在证明这种过程层面的探测能够捕捉到仅凭完成率无法反映的、对智能体性能有预测力的关键方差。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测方法类、过程-结果关联研究类以及状态追踪与过程敏感探测类。

在评测方法类工作中，传统的基准测试如MMLU、HotpotQA、AgentBench和HELM主要关注任务完成结果的正确性，而忽视了对推理过程的考察。本文指出这导致了“完成谬误”，即相同的结果可能由完全不同的过程实现，掩盖了模型在过程质量上的差异。

在过程-结果关联研究类工作中，近期研究如PAE、Fragile Thoughts and Robust Answers、Turpin等人的工作以及AgentProcessBench，均记录了大规模语言模型中推理过程与最终输出结果之间存在脱节的现象，例如智能体成功完成任务但轨迹已损坏，或推理链断裂却仍产生正确答案。过程监督和CEF等方法尝试从不同角度衡量过程质量。

在状态追踪与过程敏感探测类工作中，相关研究探索LLM如何维持和更新内部状态表示。例如，Entity Tracking测试被动状态检索，Latent State Persistence则涉及对隐藏整数的顺序操作，这与本文的WMF-AM最为接近，但缺乏算术累积操作和下游智能体性能的预测验证。Minerva中的Quantity State任务在结构上与WMF-AM相似，但其固定的深度（K=200）使得其在本文研究的模型范围内失去区分度。本文的WMF-AM方法通过K值校准恢复了在0.5B-35B模型范围内的区分能力，并增加了结构隔离消融实验套件，以及针对确定性智能体测试集的预测效度验证，从而与这些先前工作区分开来。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为WMF-AM（工作记忆保真度-主动操控）的探测任务来解决评估LLM智能体在累积状态跟踪能力上的差异问题。其核心方法并非直接改进智能体性能，而是设计了一个经过校准的、无需思维链（no-scratchpad）的探测工具，用于量化模型在认知负荷下进行连续算术运算和状态维护的内在能力，并验证此能力对智能体任务完成表现的预测力。

整体框架与主要模块：
1.  **认知评估框架（CEF）**：作为顶层设计透镜，将过程敏感的探测任务组织为四个假设维度（WMF、MCC、EMC、CLA），WMF-AM是其中工作记忆保真度维度的旗舰探测任务。
2.  **WMF-AM探测任务设计**：
    *   **任务形式**：模型首先获知一个初始数值状态，随后接收K个连续的加法或减法操作指令，最终需要报告累积计算后的最终状态。
    *   **表面形式**：为避免任务特异性，设计了三种不同的情景（积分、仓库库存、银行账户）来包装相同的算术逻辑。
    *   **校准机制（K-校准）**：通过系统性地调整操作链长度K（如3,5,7），将任务难度控制在具有区分度的范围，避免了固定深度基准测试可能出现的天花板或地板效应。
3.  **解释性框架与消融实验**：为了确证探测的是“累积状态跟踪”这一特定结构，而非其他混淆因素，论文设计了三种构造隔离消融实验：
    *   **K=1控制**：仅单步操作，用于分离单步算术能力与多步累积跟踪的难度。
    *   **非算术上限测试**：检验模型在无需算术的纯实体跟踪任务上的表现。
    *   **联动取消控制**：每个操作后紧跟其逆操作（如+5后-5），这使得算术步骤总数相同但无需维持累积状态（最终答案等于初始状态），以分离算术计算负荷与状态维护负荷。

创新点与关键技术：
1.  **超越完成率的新评估视角**：论文的核心创新在于提出并验证了“累积状态跟踪能力”是预测智能体性能的一个独立且关键的内在认知指标，即使任务完成率相同的模型，在此能力上也可能存在显著差异。
2.  **主动操控与负荷测试**：与之前主要测试被动检索的实体跟踪任务不同，WMF-AM主动要求模型对内部状态进行连续的算术转换和更新，并在更长的操作链（K=7）下施加认知负荷，从而暴露模型在维持“运行总和”这一工作记忆功能上的弱点。
3.  **预测性验证**：通过预先指定的统计分析（邦费罗尼校正），论文实证表明WMF-AM得分与智能体在确定性任务电池上的表现具有显著的中等相关性（Kendall‘s tau = 0.612），且探索性分析提示该信号在控制了完成分数和模型规模后依然存在。这为使用此类过程性探测来预测和诊断智能体性能提供了实证依据。

总之，论文通过精心设计的、可解释的WMF-AM探测任务及其验证框架，揭示了累积状态跟踪是影响LLM智能体性能的一个关键潜在认知因素，并提供了一种超越最终结果、深入评估模型内部计算过程的新方法论。

### Q4: 论文做了哪些实验？

论文设计了一系列实验来验证其提出的WMF-AM探针在预测LLM智能体性能方面的有效性。

**实验设置**：研究评估了20个开源模型（0.5B-35B参数，来自13个架构家族）。所有模型均在Ollama平台上使用默认聊天模板、fp16量化和贪婪解码（temperature=0）运行。实验分为六个阶段，依次进行。

**数据集/基准测试**：
1.  **阶段1（结果正确性，OC）**：使用一个包含100个项目的通用知识电池测试，涵盖事实、数学、科学、推理和语言五个领域，作为通用能力基线。
2.  **阶段2（WMF-AM探针）**：核心实验，使用WMF-AM探针评估累积算术状态跟踪能力。在K∈{3,5,7}三种深度下进行，每个深度15个问题，使用4个独立随机种子和3种表面形式（积分/库存/账户）。
3.  **阶段3（MCC-MA）**：应用一个包含20个问题的自我监控探针。
4.  **阶段4（联动取消控制）**：使用操作相互抵消（如先增益后损失）的对照任务，以分离算术解析和状态跟踪的难度。
5.  **阶段5（模板协调）**：在三种提示包装器（bare/chat/chain-of-thought）下重新运行WMF-AM，测试提示格式敏感性。
6.  **阶段6（智能体验证）**：使用一个包含10个确定性多步骤智能体任务（工具使用、多步推理、状态跟踪）的电池作为下游性能标准（Agent Battery Score, ABS）。

**对比方法与主要结果**：
*   **主要预测效度**：WMF-AM得分与智能体电池得分（ABS）在20个模型上呈现显著等级相关，Kendall's τ = 0.612 (p < 0.001， 95% CI [0.360, 0.814])。这是预先指定的主要发现。
*   **增量预测效度**：在控制了结果正确性（OC）得分后，WMF-AM对智能体性能仍有显著的增量预测能力（探索性偏τ = 0.411, p = 0.011）。在同时控制OC和模型规模（参数对数）后，偏τ = 0.389 (p = 0.016)。
*   **模板稳定性**：在15个模型上，bare和chat两种提示模板下的模型排名显著相关（τ = 0.524, p = 0.006），表明排名对提示格式变化具有中等稳健性。而Chain-of-Thought模板使几乎所有模型性能达到天花板（≥0.93），失去了区分度。
*   **构造隔离消融实验**：三项消融实验支持WMF-AM的难度主要源于负载下的累积状态跟踪，而非单步算术或实体跟踪本身：(1) 非算术任务（直接赋值更新）准确率接近天花板（均值0.98），显著高于算术任务；(2) K=1的单步控制任务准确率很高（均值0.957），而K=7时骤降（均值0.151）；(3) 联动取消控制任务的准确率普遍高于对应的WMF-AM任务（除deepseek-r1:14b外，其他14个模型WMF-Yoked差值为负）。
*   **关键数据指标**：
    *   WMF-AM得分范围：0.050 至 0.983（跨度0.933）。
    *   结果正确性（OC）得分范围：0.44 至 0.92（跨度0.480）。在≥3B的15个大模型中，OC得分高度集中（SD = 0.052），而WMF-AM则分布广泛（SD = 0.228）。
    *   智能体电池得分（ABS）范围：0.0 至 0.9（跨度0.90）。
    *   模型规模与智能体性能的相关性：τ = 0.503 (p < 0.01)。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性分析，未来可探索的方向包括：首先，**扩大模型样本的多样性与规模**，当前研究仅涵盖20个开源模型（0.5B-35B），未来需纳入更多闭源API模型、微调变体及非英语任务，以验证WMF-AM指标的普适性；同时需进行多随机种子实验，确保代理任务评估的可靠性。其次，**深化对构造效度的理解**，尽管论文通过控制实验排除了单步算术、实体跟踪等混淆因素，但指令遵循、分词器效应等潜在影响尚未完全消除，未来可通过更精细的模板设计和跨语言验证进一步隔离核心变量。此外，**探索累积状态跟踪与多样化代理任务之间的机制联系**，当前仅证实相关性，需结合认知理论或可解释性工具揭示其内在因果路径。最后，**将WMF-AM与标准基准（如MMLU、GSM8K）系统对比**，并开发包含负载变化、元认知组件的扩展评测框架，以构建更全面的智能体能力评估体系。

### Q6: 总结一下论文的主要内容

该论文针对当前以任务完成率作为大语言模型智能体能力主要评估指标的局限性，提出了一种新的评估方法。核心问题是，即使任务完成率相同的模型，其在追踪和操作中间状态的能力上也可能存在显著差异，而这种能力对智能体的实际表现至关重要。

为此，作者提出了“工作记忆保真度-主动操作”方法，这是一种经过校准、无需思维链的探测方法，专门用于评估模型在负载下对累积算术状态的追踪能力。该方法通过三个构造隔离消融实验，证明了累积状态追踪（而非单步算术或实体追踪）是主要的困难来源。

论文的主要结论是，WMF-AM方法能有效预测智能体在确定性任务集上的性能，其相关性显著且独立于任务完成率和模型规模。这一发现的意义在于，它超越了简单的完成率指标，为理解和评估智能体的核心认知能力——即在工作记忆中维护和更新复杂状态的能力——提供了一个更精细、更具预测性的工具，有助于未来开发更鲁棒的智能体。
