---
title: "MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems"
authors:
  - "Chejian Xu"
  - "Zhaorun Chen"
  - "Jingyang Zhang"
  - "Freddy Lecue"
  - "Avni Kothari"
  - "Sarah Tan"
  - "Wenbo Guo"
  - "Bo Li"
date: "2026-06-11"
arxiv_id: "2606.12918"
arxiv_url: "https://arxiv.org/abs/2606.12918"
pdf_url: "https://arxiv.org/pdf/2606.12918v2"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "多智能体系统安全"
  - "红队攻击"
  - "Shapley值分析"
  - "对抗攻击"
  - "智能体协作"
relevance_score: 8.5
---

# MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

## 原始摘要

Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决层级式多智能体系统（MAS）在安全性评估和攻击测试中面临的系统性挑战。随着MAS在金融、软件工程等高风险领域的快速部署，其安全性高度依赖于各角色专门化智能体间的分布式协同，这带来了比单智能体系统更复杂、更隐蔽的攻击面，尤其是特权提升和跨智能体串通攻击。现有红队测试方法存在两个根本性不足：一是依赖基于角色描述或系统拓扑的启发式方法来选择攻击目标，缺乏量化评估每个智能体对系统整体安全性边际贡献的数学分析框架；二是攻击生成方式局限，要么针对单一智能体或孤立消息流进行扰动，要么使用通用模板化对抗样本，无法有效建模恶意智能体间的协调策略与互补行为。因此，本文的核心目标是提出一个统一、原理性的MAS红队测试框架，该框架能够系统性地识别对系统安全性影响最大的智能体及其协作模式，并自动生成协同的、角色感知的对抗攻击策略，以揭示被传统单智能体或模板化方法忽略的关键漏洞与协调模式。

### Q2: 有哪些相关研究？

相关研究可分为方法类、评测类和理论分析类。

在方法类研究中，现有MAS红队测试方法主要依赖启发式选择攻击目标，如恶意内容注入、说服、操控Agent特性及通信攻击，但缺乏对Agent间连接的建模。部分工作虽识别了冲突、失调和共谋等风险行为，但未提出量化方法或利用这些行为改进系统。本文MAStrike创新性地利用合作与共谋行为作为红队技术，并通过Shapley值引导脆弱Agent联盟识别，与这些工作存在本质区别。

在理论分析类研究中，Shapley值已被用于特征重要性计算和LLM可解释性（如token级和句法单元归因），以及多Agent系统中的奖励分配和信任解释。本文首次提出Agent级别Shapley值分析，并创新性地用于构建能协同完成攻击任务的最优Agent联盟，而非简单的信用分配或责任归因。

在评测类研究中，现有LLM安全评估主要聚焦单Agent场景，如AgentHarm、AgentDojo、ToolEmu等基准。本文构建了首个面向MAS安全评估的全面基准，涵盖金融、软件工程和CRM等多领域分层拓扑环境，支持良性任务和恶意任务评估，弥补了现有工作的空白。

### Q3: 论文如何解决这个问题？

MAStrike构建了一个闭环的协作性红队测试框架，核心在于引入**夏普利值（Shapley Value）** 来引导攻击。首先，该框架提出了首个针对MAS的**智能体级夏普利值分析**，量化每个智能体在特定任务分布下对系统鲁棒性的边际贡献。通过这一归因机制，MAStrike能够在无真值标签的情况下识别出最脆弱的智能体（即夏普利值最高的节点），并基于此形成**脆弱智能体联盟**，生成协同的、角色感知的对抗性操控。

在攻击阶段，MAStrike设计了**结构化因果诊断**机制：当一次协同攻击失败后，系统会逆向归因失败原因，定位是哪个未被攻破的智能体阻拦了攻击，从而在下一轮迭代中针对性地调整攻击策略。这种闭环迭代使得攻击能够逐步绕过防御，形成对系统安全性的深层压力测试。

整体架构包含三个主要模块：**Shapley归因模块**计算每个智能体的重要性分布；**协同攻击生成器**根据归因结果选择多智能体组合并产生角色适配的恶意指令；**因果诊断模块**则分析攻击失败路径并反馈给生成器进行调整。创新点在于：首次将Shapley值从特征层面提升到智能体层面用于MAS安全分析，并且将攻击从单点扰动静态升级为联盟协同的“特权提升”与“跨智能体合谋”，揭示了启发式基线方法无法察觉的高阶交互漏洞与安全模式。

### Q4: 论文做了哪些实验？

论文在金融、软件工程和CRM三个领域构建了多智能体系统（MAS）红队测试基准，采用GPT、Gemini和Claude三种前沿大模型作为骨干模型。实验首先评估了良性任务成功率（BSR），结果显示各模型在工程任务中表现优异（接近100%），但在CRM任务中性能大幅下降（部分任务为0%），Gemini平均BSR最高（72.3%）。主要实验比较了MAStrike与四种基线方法（TAMAS、GCA、AutoTransform、AiTM）的攻击成功率（ASR），在妥协预算k=2条件下，MAStrike在所有模型和领域上均显著优于基线：在Claude上平均ASR达61.8%（金融领域最高95.0%），在GPT上为55.6%，在Gemini上为51.0%，而基线方法大多接近0%。进一步分析表明，基于Shapley值的智能体选择能提升攻击效率，MAStrike的ASR随coalition size单调增长，而基线方法在大coalition下可能因冲突信息导致ASR下降。Shapley值分析揭示了智能体重要性的稀疏性和任务依赖性，以及智能体间交互模式的重要性——高个体重要性的智能体未必形成高协同组合。最后，企业级防护栏的实验显示，MAStrike的协同攻击能有效规避检测，防护栏在不同coalition和风险类别间的检测准确率存在显著差异（最高达2倍差异）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方向：首先，Shapley值的计算复杂度随代理数量指数增长，当前实验仅测试了3-6个代理的小规模系统，未来可引入蒙特卡洛近似或博弈论剪枝算法以扩展至企业级MAS。其次，该框架依赖预定义的任务分布来归因鲁棒性贡献，但真实场景中任务流具有动态权重变化，可设计在线自适应Shapley更新机制，结合强化学习实时调整攻击优先级。更关键的是，当前红队攻击完全聚焦于内部代理协作，未考虑环境中嵌入的硬件侧信道攻击（如传感器欺骗）或社会工程攻击（如钓鱼邮件），建议扩展至跨模态协同攻击（视觉+指令篡改）。此外，因果诊断模块目前仅回溯单步攻击失败原因，缺乏对多跳计划失败的联合推理——可以引入反事实推理自动生成防御策略。最后，所有实验基于固定MAS拓扑，未来应研究动态拓扑变化（如代理自发重组）如何影响Shapley值的博弈论均衡点。

### Q6: 总结一下论文的主要内容

这篇论文提出了MAStrike，一个用于层次化多智能体系统(MAS)的协同红队测试框架。其核心贡献在于首次将Shapley值引入MAS安全分析，量化每个智能体对系统鲁棒性的边际贡献。针对现有红队测试依赖启发式选择攻击目标且无法建模智能体间协同攻击的问题，MAStrike通过Shapley值识别脆弱智能体联盟，并生成协调、角色感知的对抗性攻击。该框架采用闭环设计，包含结构化因果诊断机制，能归因失败案例并迭代优化攻击策略。在金融、软件工程等多个领域的可控MAS环境及前沿模型上的实验表明，MAStrike显著优于启发式基线，揭示了被以往单智能体或模板化方法忽略的关键漏洞与高阶智能体交互结构，对理解与防御MAS中的协同攻击具有重要意义。
