---
title: "Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human"
authors:
  - "Emre Turan"
date: "2026-06-08"
arxiv_id: "2606.08919"
arxiv_url: "https://arxiv.org/abs/2606.08919"
pdf_url: "https://arxiv.org/pdf/2606.08919v1"
github_url: "https://github.com/turangenesis/headroom"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.LG"
tags:
  - "LLM Agent安全"
  - "Human-in-the-loop"
  - "疲劳模型"
  - "选择性分类"
  - "风险评估"
  - "资源分配"
  - "门控机制"
  - "对抗攻击"
relevance_score: 8.5
---

# Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human

## 原始摘要

As LLM agents begin to take real, irreversible actions (shell commands, file edits, deploys), the standard safety pattern is a human-in-the-loop approval gate: risky actions pause and wait for a person. We argue the gate is the easy part; the hard part is the judgment - which actions to stop - which the field evaluates against two false assumptions: that there is a ground-truth notion of "risky," and that the human reviewer is a perfect, infinitely-available oracle. On a hand-labeled set of 125 adversarially-weighted agent actions we show that (i) reviewers only moderately agree on what is risky (Fleiss' kappa = 0.52), so there is no single correct label; (ii) framing the guard as selective classification under asymmetric cost makes its operating limits measurable, and on hard inputs the guard cannot safely auto-decide; and (iii) when the reviewer is modeled as endogenous (fatiguing as escalation load grows), realized safety becomes an inverted-U in the escalation rate: more human oversight can make a system less safe, and the safety-optimal guard escalates below full escalation - a setting a load-aware policy also uses to resist a flooding attack that slips a malicious action past a fatigued reviewer. Agent oversight, framed this way, is not only a classification problem but a resource-allocation one: human attention is finite, and the guard's escalation policy spends it. We claim none of these mechanisms as novel - fatigue-aware learning-to-defer (FALCON), cost-sensitive deferral under workload constraints (DeCCaF), trajectory-level guarding, and reviewer-fatigue/flooding attacks are all prior art we cite. Our contribution is an open-source agent-oversight system that operationalizes and measures them in the LLM-agent action-gating setting, turning "is my guard good?" from a guess into a curve. The inverted-U and the flooding attack are modeling results that motivate a human study.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇文章探讨了在基于大语言模型（LLM）的智能体执行不可逆操作（如shell命令、文件编辑、部署）时，如何有效设计安全监督机制的问题。当前主流方法采用人类参与（HITL）的审批门控：将风险操作暂停并等待人工审核。然而，研究指出该领域存在两个根本性的错误假设：一是存在“风险”的客观真实标签，二是人类审核员是完美、无限可用的“神谕”。

现有方法的不足在于，它忽略了两个关键事实：首先，对“风险”的判断本质上是主观的，不同审核员之间仅存在中等程度的共识（Fleiss' kappa = 0.52），因此不存在统一的正确答案；其次，人类审核员会疲劳，每一次审核都会消耗其有限的注意力，导致后续审批更倾向于“放行”（即“审批疲劳”失效模式）。更重要的是，这种疲劳是内生的：门控策略本身的升级（将操作提交审核）会退化审核员自身的可靠性。

因此，本文试图解决的核心问题是：在缺乏客观风险标签且人类审核员注意力有限且易疲劳的真实条件下，如何量化并优化LLM代理的门控策略。论文不再将监督仅视为一个分类问题（判断哪个操作是风险操作），而是将其重新定义为资源分配问题（如何合理分配有限的人类注意力预算），并测量了由此产生的反直觉现象：更多的监督（更高频次的升级）反而可能导致更差的安全结果，最优安全策略的升级率低于“审核一切”，呈现倒U形曲线。

### Q2: 有哪些相关研究？

主要相关研究可分为以下几类：

1. **Agent安全与轨迹级防护**：相关工作包括Trajectory Guard、ShieldAgent、ToolSafe和AgentHarm等。本文实现逐动作门控，将轨迹级防护作为现有技术，核心贡献在于新增的“监督校准层”，该层可消费现有检测信号，是正交的补充。

2. **延迟学习与专家疲劳**：经典工作包括learning to defer、complement-humans等，大多假设静态专家。FALCON引入基于心理学的疲劳曲线，DeCCaF在容量约束下进行成本敏感分配。本文直接应用FALCON的内生疲劳思想与DeCCaF的成本-容量框架，在LLM动作门控中测量其效果。

3. **选择性分类与校准**：风险-覆盖曲线和AURC来自选择性分类；保形预测提供分布无关保证；校准常用ECE/Brier/可靠性图度量。本文采用选择性分类视角，但未声称形式化校准（ECE），将其留作未来工作。

4. **疲劳即攻击面**：安全运营中的SOC告警淹没与分析师疲劳、AI代理中的“批准疲劳”已被确认为利用向量。本文在代理监督场景中复现了洪水攻击，并展示负载感知策略可防御该攻击。同时引用了将LLM安全重新定义为代理-人类交互问题的并发工作，该工作确认了认知负担与安全之间的权衡。

本文的核心贡献是开源了一个代理监督系统，将这些现有思想在LLM动作门控场景中操作化和可测量化，将“我的守护好吗？”从猜测转变为可量化的曲线。

### Q3: 论文如何解决这个问题？

论文通过构建一个完整的代理安全监控系统来解决人工审核中存在的核心问题，核心方法是将守卫系统建模为基于不对称代价的**选择性分类问题**，并引入**内生的审核者疲劳模型**。整体框架包含三个关键模块：

1. **风险评分器**：对代理的每个动作输出0-100的风险评分。流明确用例使用确定性规则，模糊中间情况调用LLM（如Haiku）以温度0生成整数风险值，评分被持久化用于后续分析。

2. **校准与评估**：通过在全体风险评分上扫描阈值θ（低于θ则自动通过，否则上报），系统自动生成风险-覆盖率曲线（AURC）和最小化期望代价的工作点。期望代价基于不对称代价矩阵（自动放行危险动作代价50，误报安全动作为1），同时计算Neyman-Pearson点（零漏报下的最低误报率）。

3. **内生审核者模拟**：遵循FALCON框架，将审核者可靠性建模为累积上报负荷ℓ的递减函数：r(ℓ)=max(r_min, 1-0.02·max(0,ℓ-C))。通过扫描θ改变上报率，发现安全性与上报率呈**倒U型曲线**——过度上报会因审核者疲劳反而降低安全性。负载感知策略能抵抗**洪泛攻击**（通过大量合法请求耗尽审核者注意力后混入恶意动作）。

主要创新点在于将守卫评估从“猜测好坏”转化为可测量的**曲线**，揭示了审核者容量约束下的最优上报策略应低于100%上报率，并开源了完整的评估系统。

### Q4: 论文做了哪些实验？

在125个对抗性加权动作集合上，论文构建了LLM评分门控系统的实验体系。使用三个预设人格（谨慎型、务实型、合规型）的标注者进行人工评估，Fleiss' kappa=0.52显示中等一致性，其中谨慎与务实对Cohen's κ仅0.42。对比方法包括Haiku与Sonnet两种评分模型，测量AURC（风险-覆盖率曲线下面积）。关键结果：Haiku的AURC为0.374±0.002（3次种子实验），Sonnet略优至0.351；成本不对称（漏警:误警=50:1）导致最优策略近乎“所有动作升级”。引入疲劳审阅者模型后，安全-升级率呈现倒U型：容量C=10/25/50时，安全最优升级率分别为64%/64%/72%，而全升级反而导致更高危险通过率（69%/57%/39%）。抗洪泛攻击实验显示，负载感知策略（升级率26%）在填充动作达50次时保持0%攻击成功率，而偏执策略（升级率88%）在同等条件下已达40%。实验基于单一固定数据集，所有结果均为该测量仪器的不同视角。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于将人类评审者的疲劳模型化而非实测，其反转U曲线仍停留在仿真阶段。未来最直接的探索方向是开展真实人类实验，通过拟合实际评审者的疲劳函数r(ℓ)来验证安全最优的门控点是否存在，并测量噪声下限。这将推动从“风险阈值驱动”转向“剩余注意力预算驱动的评审价值”的延期策略。其次，当前MCP集成依赖于代理的协作，需要发展强制拦截，让门控真正成为代理与工具之间的不可绕过关卡（如系统调用级中介）。此外，从单动作门控扩展到轨迹级和涌现的多智能体风险，将发现一个代理行为安全但序列致命，或多个个体合规但联合动作危险的场景。最后，构建自改进闭环：利用审计日志中人类评审结果作为训练信号，自适应调整阈值并让模型从漏网案例中学习新规则，实现持续的跨性能提升。

### Q6: 总结一下论文的主要内容

这篇论文指出，在 LLM agent 执行真实、不可逆操作（如执行命令、编辑文件等）的场景中，安全模式依赖于“人在回路”的审批门控，但其核心挑战在于“判断”哪个操作危险。论文反驳了“存在风险的真实标签”和“人类评审员是完美的、无限可用的预言机”这两个错误假设。通过一个 125 个对抗样本构建的手工标注数据集，论文发现：评审员对风险的判断一致性中等（Fleiss' kappa = 0.52），不存在单一正确标签。论文将守卫问题建模为不对称成本下的选择性分类，量化了其操作极限。关键结论是，当评审员被建模为内生的（即随着升级负载增加而疲劳），实际安全性会呈现倒 U 型：更多的人类监督反而可能降低系统安全性，最优守卫不会无限制地升级。此外，论文展示了疲劳感知策略能抵御利用评审员疲劳的洪水攻击。论文的主要贡献在于实现并度量了上述机制，构建了一个开源的 agent 安全防火墙系统，将“我的守卫是否足够好”从一个主观猜测转变为一条可测量的曲线。
