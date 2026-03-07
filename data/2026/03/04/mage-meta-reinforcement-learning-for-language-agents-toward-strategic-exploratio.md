---
title: "MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation"
authors:
  - "Lu Yang"
  - "Zelai Xu"
  - "Minyang Xie"
  - "Jiaxuan Gao"
  - "Zhao Shok"
date: "2026-03-04"
arxiv_id: "2603.03680"
arxiv_url: "https://arxiv.org/abs/2603.03680"
pdf_url: "https://arxiv.org/pdf/2603.03680v1"
github_url: "https://github.com/Lu-Yang666/MAGE"
categories:
  - "cs.AI"
tags:
  - "Learning & Optimization"
  - "Multi-Agent Systems"
relevance_score: 8.0
taxonomy:
  capability:
    - "Learning & Optimization"
    - "Multi-Agent Systems"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MAGE (Meta-Reinforcement Learning for Language Agents with population-based training and agent-specific advantage normalization)"
  primary_benchmark: "N/A"
---

# MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation

## 原始摘要

Large Language Model (LLM) agents have demonstrated remarkable proficiency in learned tasks, yet they often struggle to adapt to non-stationary environments with feedback. While In-Context Learning and external memory offer some flexibility, they fail to internalize the adaptive ability required for long-term improvement. Meta-Reinforcement Learning (meta-RL) provides an alternative by embedding the learning process directly within the model. However, existing meta-RL approaches for LLMs focus primarily on exploration in single-agent settings, neglecting the strategic exploitation necessary for multi-agent environments. We propose MAGE, a meta-RL framework that empowers LLM agents for strategic exploration and exploitation. MAGE utilizes a multi-episode training regime where interaction histories and reflections are integrated into the context window. By using the final episode reward as the objective, MAGE incentivizes the agent to refine its strategy based on past experiences. We further combine population-based training with an agent-specific advantage normalization technique to enrich agent diversity and ensure stable learning. Experiment results show that MAGE outperforms existing baselines in both exploration and exploitation tasks. Furthermore, MAGE exhibits strong generalization to unseen opponents, suggesting it has internalized the ability for strategic exploration and exploitation. Code is available at https://github.com/Lu-Yang666/MAGE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在非平稳、多智能体环境中缺乏战略适应能力的问题。研究背景是，尽管强化学习（RL）提升了LLM智能体处理复杂任务的能力，但现有方法（如上下文学习或外部记忆）主要适用于静态环境，无法让智能体内化长期、自适应的学习机制，难以应对环境动态变化或其他智能体行为带来的挑战。现有方法的不足在于，当前应用于LLM的元强化学习（meta-RL）方法多专注于单智能体任务中的探索（exploration），而忽视了在多智能体环境中至关重要的战略利用（exploitation）能力——即识别并利用对手特定行为模式以最大化自身收益。因此，本文的核心问题是：如何设计一个元强化学习框架，使LLM智能体能够在多智能体环境中同时实现战略探索与利用，从而具备从历史交互中学习、并针对不同对手动态调整策略的泛化适应能力。为此，论文提出了MAGE框架，通过多回合训练将交互历史与反思整合到上下文窗口，并以最终回合奖励为目标优化策略，促使智能体基于过往经验精细化其战略。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：上下文学习、面向LLM的智能体强化学习，以及元强化学习。

在**上下文学习（ICL）**方面，如Reflexion和Self-Refine等工作通过引入迭代反馈循环或外部记忆库，使智能体能够根据环境试错进行调整。然而，这些方法依赖固定的模型权重，难以将底层学习逻辑内化，在复杂非平稳环境中适应能力有限。本文提出的MAGE框架则旨在通过元强化学习实现策略的内化与长期改进，超越了依赖外部提示或检索的范式。

在**面向LLM的智能体强化学习（Agentic RL）**方面，研究已从简单的偏好对齐发展到增强复杂推理和多轮决策，例如在网页搜索、软件工程等任务中的应用。GiGPO等算法致力于稳定长程交互的训练。MAGE继承了这一趋势，但将重点从掌握单一任务转向掌握**适应过程本身**，强调在动态环境中的策略演进。

在**元强化学习（Meta-RL）**方面，传统方法训练智能体快速适应新任务。近期研究如LAMER将其应用于LLM，激励在单智能体环境中的高效探索。然而，这些工作大多忽视了多智能体环境中至关重要的**战略利用（exploitation）**能力。MAGE的创新之处在于，通过基于种群的训练和智能体特定的优势归一化技术，使智能体不仅能探索，还能稳健地利用对手的特定行为弱点，从而在战略探索与利用之间取得平衡，拓展了语言智能体元强化学习的前沿。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MAGE的元强化学习框架来解决LLM智能体在非平稳多智能体环境中战略探索与利用能力不足的问题。其核心方法是将元学习过程直接嵌入到LLM策略中，通过一个多回合的训练机制，使智能体能够基于历史交互经验进行自我反思和策略优化。

整体框架围绕“元回合”展开，每个元回合包含N个与环境或对手交互的常规回合。框架的核心创新在于引入了“反思内循环”。在每个常规回合结束后，LLM策略会生成一个自然语言形式的自我反思，用于总结失败模式、诊断战略错误并提出改进建议。这些反思被组织成一个上下文记忆，作为跨回合累积经验的高层抽象，并作为后续回合决策的输入。因此，智能体的动作生成不仅依赖于当前状态历史，还依赖于这个不断更新的反思记忆。

关键技术包括：1）**回合间差分元奖励**：将学习信号定义为当前回合与上一回合的累计任务奖励之差，从而直接优化跨回合的学习进展。2）**跨回合的回报计算**：设计的步回报不仅考虑当前回合内的未来稀疏奖励，还通过折扣因子考虑后续所有回合的回报，从而将长期策略改进纳入优化目标。3）**基于种群的训练与智能体特定优势归一化**：在多智能体设置中，让智能体与一个包含多种固定策略的对手池进行交互。同时，对从不同对手交互中计算出的优势值进行归一化处理，这有助于丰富智能体的行为多样性并确保学习的稳定性。

最终，MAGE通过一个广义的策略梯度目标进行优化，该目标最大化期望的累积元奖励，其损失函数由优势函数加权的动作对数似然构成。这种方法使LLM智能体能够内化一种能力：在面对不同对手时，能主动推断对方行为模式，并动态调整自身策略，实现战略性的探索（发现有效策略）与利用（优化已知有效策略），从而在多变环境中实现长期性能提升。

### Q4: 论文做了哪些实验？

论文实验设置以Qwen3-4B为基础大语言模型，采用GiGPO算法进行训练，并设置了跨轨迹折扣因子γ_traj=0.6。每个元情节包含3个情节，训练时每批使用8个元情节组。为公平比较样本效率，标准强化学习基线每批组大小扩展至24。在多智能体环境中，采用基于种群的训练方法，例如在井字棋中与基于MCTS、偏好模式和随机策略的对手交互，在库恩扑克中则面对保守、激进和中间型对手原型。

实验在多样化的战略基准上进行评估。多智能体任务包括井字棋（评估对确定性最优策略的快速适应）和库恩扑克（测试战略推理和虚张声势）。单智能体任务包括ALFWorld（交互式家庭规划）、WebShop（目标导向的网络导航）和Sokoban（长视野空间解谜）。

对比的基线方法广泛，涵盖启发式智能体框架（如ReAct、Reflexion）、记忆增强智能体（如A-MEM、Memento）、基础强化学习方法（如GRPO、GiGPO）以及相关元学习方法（如LAMER）。主要评估指标为成功率，采用Pass@k形式报告，即智能体在元情节的前k个情节中至少成功完成一次任务的概率。

主要结果如下：在多智能体战略利用方面，MAGE在井字棋中对阵MCTS-100达到67.2%的终端成功率，显著优于LAMER（60.2%）和GiGPO（41.4%）；在库恩扑克中达到65.6%的理论上限。在单智能体探索任务中，MAGE在WebShop中从第1情节的66.4%成功率提升至第5情节的100%，优于基线20-30%；在Sokoban中从40.6%提升至77.3%（+36.7%）；在ALFWorld中达到91.4%的Pass@10，超越LAMER（89.8%）和GiGPO（88.3%）。泛化评估显示，面对近乎不可战胜的MCTS-1000，MAGE在井字棋中的平局率从81.2%升至100%；在库恩扑克中对阵CFR对手达到50.8%的理论上限。在单智能体OOD任务中，Sokoban的1箱和3箱变体分别达到91.4%和46.1%的成功率；WebShop保持96.1%；ALFWorld终端性能为78.9%。消融实验证实，差分回报设计、平衡的对手分布以及跨情节分组（全局锚点）的优势归一化是性能提升的关键。

### Q5: 有什么可以进一步探索的点？

该论文提出的MAGE框架在提升LLM智能体策略性探索与利用方面取得了进展，但仍存在一些局限性和可进一步探索的方向。首先，其实验环境相对简化，主要基于博弈类任务，未来可扩展到更复杂、开放式的多智能体场景（如社交互动、经济系统模拟），以验证其泛化能力。其次，当前方法依赖多轮交互历史与反思，可能受限于LLM的上下文长度，未来可研究更高效的经验压缩或分层记忆机制。此外，MAGE的训练需要大量交互数据，计算成本较高，可探索轻量化元学习或与模型微调结合的方法。从更广视角看，未来可研究如何将策略性适应能力与工具调用、环境感知等结合，构建更通用的自主智能体。最后，论文未深入讨论安全与对齐问题，在赋予智能体策略性能力时，需考虑其行为可解释性与伦理约束，避免策略滥用。

### Q6: 总结一下论文的主要内容

该论文提出了MAGE框架，旨在解决大型语言模型（LLM）智能体在非平稳环境中适应能力不足的问题。核心问题是现有基于上下文学习或外部记忆的方法难以实现长期策略内化，而元强化学习（meta-RL）方法又大多局限于单智能体探索，忽视了多智能体环境中必要的战略利用能力。

MAGE通过多轮次训练机制，将交互历史与反思整合到上下文窗口中，并以最终轮次奖励为目标，激励智能体基于过往经验优化策略。方法上结合了基于群体的训练和智能体特定的优势归一化技术，以增强智能体多样性并确保学习稳定性。

实验表明，MAGE在探索与利用任务上均优于现有基线，并能泛化至未见过的对手，证明其已内化了战略探索与利用的能力。该工作的主要贡献在于为LLM智能体提供了一个统一的元强化学习框架，使其能在动态多智能体环境中自主发展并优化长期策略。
