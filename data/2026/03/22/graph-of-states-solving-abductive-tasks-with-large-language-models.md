---
title: "Graph of States: Solving Abductive Tasks with Large Language Models"
authors:
  - "Yu Luo"
  - "Rongchen Gao"
  - "Lu Teng"
  - "Xidao Wen"
  - "Jiamin Jiang"
  - "Qingliang Zhang"
  - "Yongqian Sun"
  - "Shenglin Zhang"
  - "Jiasong Feng"
  - "Tong Liu"
  - "Wenjie Zhang"
  - "Dan Pei"
date: "2026-03-22"
arxiv_id: "2603.21250"
arxiv_url: "https://arxiv.org/abs/2603.21250"
pdf_url: "https://arxiv.org/pdf/2603.21250v1"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "推理与规划"
  - "神经符号系统"
  - "框架设计"
  - "逻辑推理"
  - "状态管理"
  - "回溯机制"
relevance_score: 8.0
---

# Graph of States: Solving Abductive Tasks with Large Language Models

## 原始摘要

Logical reasoning encompasses deduction, induction, and abduction. However, while Large Language Models (LLMs) have effectively mastered the former two, abductive reasoning remains significantly underexplored. Existing frameworks, predominantly designed for static deductive tasks, fail to generalize to abductive reasoning due to unstructured state representation and lack of explicit state control. Consequently, they are inevitably prone to Evidence Fabrication, Context Drift, Failed Backtracking, and Early Stopping. To bridge this gap, we introduce Graph of States (GoS), a general-purpose neuro-symbolic framework tailored for abductive tasks. GoS grounds multi-agent collaboration in a structured belief states, utilizing a causal graph to explicitly encode logical dependencies and a state machine to govern the valid transitions of the reasoning process. By dynamically aligning the reasoning focus with these symbolic constraints, our approach transforms aimless, unconstrained exploration into a convergent, directed search. Extensive evaluations on two real-world datasets demonstrate that GoS significantly outperforms all baselines, providing a robust solution for complex abductive tasks. Code repo and all prompts: https://anonymous.4open.science/r/Graph-of-States-5B4E.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在溯因推理任务上的能力不足问题。研究背景是，尽管大语言模型在演绎和归纳推理上已表现出色，但作为现实世界决策（如医疗诊断、刑事侦查）基础的溯因推理——即从有限观察中推断最可能解释——却尚未得到充分探索。现有方法，如思维链、思维树等主流推理框架，主要针对静态、确定性的演绎任务设计，直接应用于动态、信息不完整的溯因场景时存在根本性局限。

现有方法的不足具体体现在四个关键缺陷上：1) 证据捏造：模型为维持逻辑一致性，倾向于编造不存在的事实；2) 上下文漂移：在长程推理中遗忘进展，陷入冗余循环；3) 回溯失败：面对模糊的中间结果时，缺乏明确约束而无法及时纠正错误路径；4) 过早终止：满足于表面症状而未能深入挖掘根本原因。论文指出，这些缺陷源于现有框架的两个根本性结构限制：一是将推理状态隐含在非结构化的上下文历史中，缺乏清晰的状态表示；二是缺乏状态控制机制，导致回溯和深入探索的决策完全依赖模型不受约束的自主性。

因此，本文要解决的核心问题是：如何构建一个通用、专用的推理框架，以克服现有方法的结构性缺陷，从而有效处理溯因任务的动态性和非单调性。为此，论文提出了“状态图”这一神经符号框架，通过引入因果图来显式编码逻辑依赖以结构化信念状态，并利用状态机来管控推理过程的合法转移，从而将无目标的探索转化为收敛的、定向的搜索。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：针对演绎任务的通用推理框架和针对特定溯因任务的领域适应方法。

在**通用推理框架**方面，研究主要围绕提升大语言模型在演绎任务（如数学问题、游戏）上的推理能力。Chain-of-Thought (CoT) 及其改进版本（如 CoT-SC、VerifyCoT）通过将问题分解为线性步骤进行推理。Tree of Thoughts (ToT) 及其扩展（如 Graph of Thoughts, GoT）进一步引入了树或图结构来探索非线性的推理路径。然而，这些方法主要针对静态、演绎问题设计，其非结构化的状态表示和缺乏明确的状态控制，使其难以直接推广到需要动态假设生成与验证的溯因任务上，容易导致证据捏造、上下文漂移等问题。

在**特定溯因任务方法**方面，现有工作主要通过领域特定的工程来适配，可分为四类：1) **多智能体定制**（如 MAM、D-Bot），设计静态的协作拓扑模拟专家工作流；2) **检索增强生成**（RAG，如 MDAgents、FlowXpert），利用外部知识库 grounding 推理；3) **监督微调**（SFT，如 Med-PaLM 2、LogLM），通过领域数据微调模型内部化知识；4) **数据预处理**（如 TrioXpert），将异构输入转化为结构化上下文。这些方法高度依赖特定领域的工程，缺乏通用的溯因推理能力。

本文提出的 Graph of States (GoS) 框架与上述工作的区别在于：它不局限于演绎任务，而是专门为溯因推理设计；它不同于领域特定的工程化方案，是一个通用的神经符号框架。GoS 通过结构化的信念状态图、因果依赖编码和状态机控制，将无目标的探索转化为收敛的定向搜索，从而系统性地解决了通用溯因推理的挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“状态图”的双层神经符号框架来解决溯因推理任务中的挑战。该框架的核心在于将非结构化的推理过程转化为受控的、收敛的搜索，从而有效避免证据捏造、上下文漂移、回溯失败和过早停止等问题。

整体框架由认知层和符号层构成，形成双向交互的闭环系统。认知层作为一个多智能体系统，包含一个中央协调器和多个领域专家智能体，负责执行具体的工具调用和证据收集。符号层则作为导航锚点，将推理状态形式化为结构化的信念状态，具体包括因果图和状态机两个关键组件。因果图是一个有向图，节点分为症状、证据和假设三类，边则编码了推导、细化和支持/反驳三种逻辑关系，从而显式地建模了逻辑依赖。状态机则通过一个状态变量来追踪当前正在调查的假设的语义粒度层级，控制推理的深度。

创新点主要体现在三个方面。首先，引入了“推理焦点”机制，即在每个推理步骤中，符号层会根据当前层级的置信度选择最有可能的假设作为焦点，指导认知层进行定向调查，这取代了无目标的探索，实现了资源的集中利用。其次，设计了严格的状态转换规则来驱动推理进程：当出现矛盾证据时，系统会触发回溯机制，剪除基于错误前提的后续假设，并重置状态到更浅的层级；当当前焦点假设满足置信度差距和最小证据支持数量的双重阈值时，系统则执行深入转换，生成更细粒度的子假设或直接输出最终预测。最后，框架实现了认知层与符号层的双向交互：符号层通过推理焦点为认知层提供可执行的指令，确保探索的聚焦性和一致性；认知层则将收集到的证据汇总，更新符号层中的因果图拓扑和节点置信度，从而将动态的协作推理实时地反映在结构化的信念状态中。

通过这种将显式的符号化状态控制与灵活的神经多智能体协作相结合的方式，GoS 将溯因推理转化为一个在结构化状态空间中进行的有向搜索过程，显著提升了复杂溯因任务的鲁棒性和准确性。

### Q4: 论文做了哪些实验？

论文在两个真实的溯因推理任务上进行了实验：医疗诊断和分布式系统故障诊断。实验设置方面，所有方法均采用GPT-5.1-2025-11-13作为智能体骨干，并统一使用ReAct范式作为原子推理单元。在医疗诊断任务中，使用了DiagnosisArena数据集中的150个真实病理案例；在分布式系统故障诊断任务中，使用了来自某全球领先IT公司生产环境的150个事件构建的数据集。

对比方法综合了智能体架构（单智能体 vs. 多智能体）和推理拓扑（思维链CoT、思维树ToT、思维图GoT、思维森林FoT）两个维度，共合成8个基线。评估主要采用LLM-as-a-Judge（使用2/1/0的三点量表）并报告Match（得分为2）和Relevant（得分为1或2）两个指标；针对医疗诊断，额外引入了具备临床经验的研究者进行Human-as-a-Judge评估以保障可靠性。

主要结果显示，Graph of States (GoS)在两个任务上均显著优于所有基线。在医疗诊断中，Human-as-a-Judge评估下GoS的Match达到39.86%，Relevant达到78.99%，而最佳基线Multi/FoT分别为26.09%和65.94%，且GoS成本仅为0.12美元/案例，远低于Multi/FoT的0.73美元。在分布式系统故障诊断中，GoS的Match达到70.67%，Relevant达到88.00%，最佳基线Multi/CoT的Match为34.00%，Multi/FoT的Relevant为86.67%但成本高达0.94美元/案例，GoS以0.10美元的成本实现了约8倍的成本效益。消融实验表明，移除推理焦点、因果图或状态机任一组件均导致性能显著下降，Match最低降至12.32%，验证了各组件必要性。敏感性分析进一步揭示了推理预算与双阈值参数在精度与保守性间的权衡关系。

### Q5: 有什么可以进一步探索的点？

本文提出的GoS框架在解决溯因推理任务上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架严重依赖人工设计的因果图和状态机来提供结构化约束，这限制了其在未知或动态领域中的泛化能力。未来研究可探索如何利用LLMs自动从数据或交互中学习并演化这些符号结构，实现更自适应的推理。其次，当前工作主要针对文本形式的溯因任务，未来可扩展至多模态场景（如结合视觉、传感器数据），以处理更复杂的现实问题。此外，框架中的多智能体协作机制较为固定，可引入更灵活的协商或竞争策略，以提升探索效率。最后，评估目前集中在特定数据集，需在更多样化和高风险的领域（如医疗诊断、故障分析）进行验证，并进一步研究如何量化推理过程的可信度与可解释性，这对实际应用至关重要。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在溯因推理任务上的不足，提出了一种名为“状态图”的通用神经符号框架。现有方法主要面向静态演绎任务，在溯因推理中易出现证据捏造、语境漂移、回溯失败和过早停止等问题。GoS的核心贡献在于将多智能体协作建立在结构化的信念状态上，通过因果图显式编码逻辑依赖关系，并利用状态机严格控制推理过程的有效状态转移。该方法将原本无目标、无约束的探索，转化为受符号约束引导的收敛性定向搜索。在多个真实数据集上的评估表明，GoS显著优于所有基线方法，为复杂的溯因推理任务提供了一个鲁棒且有效的解决方案。
