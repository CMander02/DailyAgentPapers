---
title: "Taming \"Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution"
authors:
  - "Taolin Zhang"
  - "Pukun Zhao"
  - "Qizhou Chen"
  - "Jiuheng Wan"
  - "Chen Chen"
  - "Xiaofeng He"
  - "Chengyu Wang"
  - "Richang Hong"
date: "2026-05-17"
arxiv_id: "2605.17348"
arxiv_url: "https://arxiv.org/abs/2605.17348"
pdf_url: "https://arxiv.org/pdf/2605.17348v1"
categories:
  - "cs.CL"
tags:
  - "LLM多智能体系统"
  - "智能体状态管理"
  - "弹性多智能体进化"
  - "软状态转换"
  - "风险估计器"
  - "智能体调度"
relevance_score: 8.5
---

# Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution

## 原始摘要

Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks. To improve overall efficiency, existing methods often rely on aggressive graph evolution among agents (e.g., node or edge pruning), which risks prematurely discarding valuable agents due to transient issues such as hallucinations or temporary knowledge gaps. However, such hard pruning overlooks the potential for ``zombie'' agents to recover and contribute in subsequent discussion rounds. In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. Our approach dynamically manages agent collaboration through soft state transitions, implemented via two key components: (1) State-Aware Policy Learning: Agent states are divided into ``Active'', ``Standby'', and ``Terminated'' states, selectively propagating messages based on agent memory. The policy employs a risk estimator to optimize agent state transitions by assessing hallucination risk, minimizing the influence of unreliable nodes while safeguarding valuable ones. (2) State-Aware Edge Optimization: Subgraph edges are pruned according to states learned from the policy, permanently removing ``Terminated'' nodes and retaining ``Standby'' nodes for subsequent rounds to assess their potential future contributions. Extensive experiments on general reasoning, domain-specific, and hallucination challenge tasks show that our method consistently outperforms strong baselines and significantly reduces token consumption through state-aware agent scheduling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统中，现有方法在处理“僵尸”智能体时的不足。当前的多智能体协作系统常采用图剪枝策略（如节点或边缘修剪）来提升效率，但这种“硬剪枝”方法会因幻觉、临时知识缺口等短期问题而永久性地丢弃有价值的智能体。这些被丢弃的智能体在后续讨论轮次中仍可能恢复并做出贡献，但现有方法忽略了其恢复潜力，导致性能损失。此外，基于图生成的方法虽能动态构建协作图，但缺乏全局拓扑状态考虑，难以重新评估或整合前期被排除的智能体。核心问题在于：如何在优化通信效率的同时，避免对临时失效但可恢复的智能体进行永久性剪枝，从而提升系统在复杂任务中的鲁棒性和整体性能。本文提出AgentRevive框架，通过马尔可夫状态感知的软状态转换机制，动态管理智能体协作，允许智能体在后续轮次中从“待机”状态恢复为“活跃”状态，从而在保持效率的同时最大化智能体的潜在贡献。

### Q2: 有哪些相关研究？

相关研究可分为三类：**1) 静态拓扑方法**：如LATM、ChatDev、MetaGPT、AutoGen、SoA等采用预定义拓扑（非交互、链式、星型、树型），虽有效但缺乏灵活性与可扩展性。**2) 动态图学习方法**：如GPTSwarm、DSPy、DyLAN、EvoMAC通过强化学习或反馈学习自适应通信图，但未解决冗余结构问题。**3) 图剪枝方法**：如DyLAN动态选择团队，但采用硬剪枝可能误删有价值节点；而AgentRevive创新提出软状态转移（Active/Standby/Terminated），通过风险估计器保留“僵尸”智能体，避免因瞬时幻觉等导致的误删，兼顾性能与token效率。本文与DyLAN等剪枝方法的关键区别在于：以马尔可夫状态感知的恢复机制替代硬性删除，并通过子图边缘优化永久移除终止节点、保留待定节点以评估其未来贡献，实现弹性进化。

### Q3: 论文如何解决这个问题？

本文提出AgentRevive框架，通过马尔可夫状态感知机制解决多智能体系统中因硬剪枝导致有价值智能体被过早丢弃的问题。核心创新在于将传统硬剪枝范式转化为动态状态管理：

1. **状态感知策略学习**：将智能体划分为三种状态——活跃（Active）、待命（Standby）和终止（Terminated）。通过风险估计器评估幻觉风险，优化状态转移决策。待命状态允许"僵尸"智能体在后续轮次恢复为活跃状态，避免永久性移除。策略网络采用轻量MLP实现，结合LSTM编码智能体记忆进行状态预测。

2. **状态感知边优化**：根据策略生成的终止节点掩码矩阵，对子图边进行永久剪枝。待命节点保留但其消息被压缩为历史摘要（通过LLM压缩），活跃节点正常传播消息。边权重通过核范数最小化进行参数化优化，平衡任务性能与图稀疏性。

3. **双流信息传递**：整合空间边（同轮次智能体连接）和时间边（跨轮次连接），利用可训练连续权重[0,1]构建有向无环图。消息聚合同时考虑空间邻域信息和时序信息，状态感知响应根据当前状态选择完整推理或历史摘要。

4. **增强训练目标**：轨迹奖励综合考虑任务得分和活跃节点的KL散度（量化幻觉矛盾），通过无偏策略梯度优化边权重。多轮推理后通过平均存活率阈值筛选关键节点，构建稀疏通信图。

实验在通用推理、领域特定和幻觉挑战任务上取得最优性能，同时通过状态感知调度显著降低token消耗。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了全面实验。实验设置包括：通用推理（MMLU、GSM8K）、领域特定及幻觉挑战（TruthfulQA, TQA）任务，使用 Llama3-8B-Instruct 和 Qwen2.5-72B-Instruct 作为基座模型。对比方法包括：单智能体方法（CoT、SC）、固定拓扑多智能体系统（MAS_round=1、MAS_round=T、AutoGen、AgentVerse）以及动态图多智能体系统（ARG-Designer、AgentDropout）。主要结果：AgentRevive 在两类基座模型上均取得最优平均性能（Llama3-8B: 68.53%；Qwen2.5-72B: 84.34%），显著优于所有基线，尤其在 TruthfulQA（幻觉挑战）上提升显著。消融实验证实了三个关键组件的作用：去除状态感知策略学习（w/o SPL）导致性能下降最大（Llama3-8B 上平均降 5.73%）。在资源效率上，相比 MAS_round=T，AgentRevive 在 MMLU 上准确率提升 6.9%，同时节省 33.7% 的 Token 消耗。AgentRevive 在帕累托效率上最优，通过状态感知调度以适度成本取得高绩效。鲁棒性分析显示其在提示攻击和不同图结构初始化下性能退化最小。

### Q5: 有什么可以进一步探索的点？

该工作的核心局限在于状态转移策略依赖于预定义的“Active/Standby/Terminated”三态机制和风险估计器，尚无法自动学习最优的调度策略。未来可探索引入强化学习框架，让智能体在交互过程中自主习得何时应保持活跃、何时应休眠，而非依赖人工设定的阈值。此外，当前框架仅在推理轮次间评估恢复可能性，缺乏对agent长期行为模式的预测能力。可进一步引入时序模型（如LSTM或Transformer）对agent的历史贡献曲线进行建模，预测其未来可靠性，从而在更早轮次识别潜在的“僵尸”agent。另一个改进方向是扩展状态空间，例如加入“观察态”或“训练态”，让agent在休眠期间仍可通过被动学习更新知识。最后，当前评估主要关注推理和问答任务，未来可在动态协作更频繁的开放域任务（如多轮谈判、协同编程）中验证框架的鲁棒性，并探索跨领域迁移时状态策略的自适应能力。

### Q6: 总结一下论文的主要内容

本文提出AgentRevive，一种基于马尔可夫状态感知的韧性多智能体演化框架，旨在解决大语言模型多智能体系统中因激进硬剪枝导致的有价值智能体过早被丢弃（称为“僵尸”智能体）的问题。核心方法包括：1）状态感知策略学习，将智能体状态划分为“活跃”、“待机”和“终止”，通过风险估计器评估幻觉风险，优化状态转换以最小化不可靠节点影响并保护潜在有价值节点；2）状态感知边优化，根据学习到的状态对子图边进行软修剪，永久移除“终止”节点而保留“待机”节点以备后续轮次评估其贡献。在通用推理、领域特定和幻觉挑战任务上的实验表明，该方法持续优于强基线，并通过状态感知调度显著降低token消耗。主要贡献在于将智能体状态过渡建模为马尔可夫过程，避免了破坏性硬剪枝，为构建更鲁棒高效的多智能体协作系统提供了新范式。
