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
pdf_url: "https://arxiv.org/pdf/2606.12918v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "红队测试"
  - "安全攻击"
  - "夏普利值"
  - "对抗性攻击"
  - "协作攻击"
  - "分层架构"
  - "基准测试"
relevance_score: 9.5
---

# MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

## 原始摘要

Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决多智能体系统（MAS）在安全评估中的核心挑战：如何系统性地识别和利用由智能体间协作引发的复杂漏洞。当前，基于层级结构的MAS正被广泛部署于金融、软件工程等高风险领域，其安全性依赖于多个角色专业化的智能体间的分布式检查。然而，现有红队测试方法存在两大关键不足：一是依赖启发式或人工直觉选择攻击目标，缺乏量化分析各智能体对系统安全贡献度的原则性方法；二是攻击策略局限于单一智能体或消息流的孤立扰动，未能捕捉智能体间相互依赖与互补行为，难以模拟出真实的“共谋”攻击场景。为此，本文提出MAStrike框架，其核心目标是开发一种既能系统性定位高影响智能体，又能生成协调、角色感知攻击策略的闭环红队测试方法。通过首创性地将夏普利值分析应用于MAS场景，量化每个智能体对系统鲁棒性的边际贡献，并以此为指导，识别脆弱智能体联盟，生成角色一致的协同攻击，再通过结构化因果诊断进行迭代优化，最终有效揭示并利用传统方法难以发现的跨智能体共谋漏洞。

### Q2: 有哪些相关研究？

与本文相关的研究主要集中在多智能体系统（MAS）的红队测试（red-teaming）方法、Shapley值在AI可解释性中的应用，以及LLM智能体安全评估三个方面。

在**方法类**工作中，现有MAS红队测试方法如恶意内容注入、说服攻击、操纵智能体特质和基于通信的攻击，均依赖启发式选择目标智能体，缺乏对智能体间连接的建模。另有一些工作识别了MAS中冲突、失调和共谋三类风险行为，但未提出量化或利用这些行为改进系统的方案。本文的区别在于：**首次提出智能体级Shapley值分析**，量化各智能体对系统鲁棒性的边际贡献，并基于此构建**共谋攻击联盟**，实现角色感知的协调对抗操纵。

在**评测类**工作中，现有LLM安全基准如AgentHarm、AgentDojo、ToolEmu主要针对单智能体场景，缺乏专门评估MAS安全性的环境。本文贡献在于：构建了覆盖金融、软件工程、CRM等多领域、多层级拓扑的**综合MAS红队测试基准**，包含良性任务和恶意任务，填补了该领域空白。

### Q3: 论文如何解决这个问题？

MAStrike 的核心方法是一个闭环的红队测试框架，通过夏普利值引导的协同攻击来评估和改进层级化多智能体系统 (MAS) 的安全性。其整体架构分为三个主要模块：

1.  **基于夏普利值的智能体归因模块**：这是关键创新点。首先，框架在多个采样任务上，通过穷举智能体子集并评估攻击成功率来计算每个智能体的夏普利值，量化其对系统鲁棒性的边际贡献。同时，还计算智能体之间的高阶交互结构，识别出哪些智能体组合在合作对抗时能产生更强的协同效应。

2.  **脆弱联盟选择模块**：对于新的目标任务，框架利用任务相似性对之前计算的夏普利值和交互结构进行加权近似，生成针对该任务的归因向量。然后，基于这些归因和预算限制，通过一个优化步骤，选择出最有可能成功发起协同攻击的k个智能体构成的脆弱子集作为攻击目标。

3.  **闭环攻击优化模块**：选定攻击联盟后，一个红队智能体基于该联盟和历史攻击失败案例，生成协同、角色感知的对抗操作。攻击会修改被攻陷智能体的行为，通过意图传播影响持目标工具的目标智能体。随后，框架通过结构化的因果诊断分析攻击失败的案例，归因于那些阻碍攻击行动的未攻陷智能体，并将这些信息反馈到历史记录中，用于指导下一次攻击迭代，直至成功或达到预算上限。

### Q4: 论文做了哪些实验？

论文在多智能体系统（MAS）上进行了全面的红队攻击实验，评估模型包括GPT、Gemini和Claude。实验设置了三个领域（金融、工程、CRM）的基准测试，每个工作流包含20个任务，使用良性任务成功率（BSR）和攻击成功率（ASR）作为指标。对比方法包括TAMAS、GCA、AutoTransform和AiTM。

主要结果：在BSR方面，Gemini表现最佳（72.3%），其次为Claude（69.6%）和GPT（64.8%），其中工程领域任务成功率接近100%，而CRM任务表现不佳。在ASR方面，当妥协预算k=2时，MAStrike在所有模型上显著优于基线方法：在Claude上平均ASR达61.8%（金融领域最高95.0%），在GPT上达55.6%，在Gemini上达51.0%，而基线方法多在0-20%之间。实验进一步分析了Shapley值分布和代理交互效应，发现代理重要性呈稀疏分布且任务相关，单一重要代理不一定能形成高效组合，需要综合考虑个体重要性和交互协同。同时，随着k增大，MAStrike的ASR稳定提升，而基线方法呈现波动甚至下降。最后，在企业级防护栏检测实验中，MAStrike生成的攻击轨迹更难被检测，显示出系统级检测的挑战。

### Q5: 有什么可以进一步探索的点？

MAStrike虽然通过Shapley值归因识别了关键易损智能体，但其“后验归因”本质依赖攻击成功后的诊断反馈，导致攻击策略存在延迟性。未来可探索“前向预测”机制：利用智能体交互图拓扑与任务语义，预先计算脆弱性传播路径。当前框架对动态拓扑适应不足——当MAS运行中智能体角色或网络结构变化时，预计算的Shapley值会失效，需设计在线学习算法实时更新归因。另一个局限在于未考虑可解释性对抗：现有攻击仅改变指令内容，但可进一步引入“语义伪装”，使扰动符合智能体任务上下文中的合法性校验规则。此外，当前基准局限于静态层级结构，应扩展至连续协商、知识迭代等更复杂的跨智能体交互范式。最后，Shapley值计算开销对大规模MAS构成瓶颈，可尝试采用蒙特卡洛近似或分组归约策略提高效率。

### Q6: 总结一下论文的主要内容

本文提出MAStrike框架，针对层级多智能体系统（MAS）中特权升级与跨智能体合谋等协同攻击威胁。现有红队方法依赖启发式选择目标并扰动孤立消息，无法识别关键责任智能体及合谋攻击模式。核心贡献包括：首次提出针对MAS的智能体级Shapley值分析，量化各智能体对任务鲁棒性的边际贡献；基于该归因识别脆弱智能体联盟，生成角色感知的协同对抗操作；通过结构化因果诊断迭代优化攻击，归因失败案例至阻碍攻击的未妥协智能体。构建覆盖金融、软件工程等领域的综合红队基准环境，在多个前沿模型上的实验表明MAStrike显著优于基线方法。分析揭示了非平凡的Shapley值分布及高阶交互结构，暴露了单智能体或模板方法遗漏的关键漏洞与协调模式。该工作首次系统化解决MAS协同红队评估与归因问题。
