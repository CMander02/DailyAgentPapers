---
title: "Self-evolving LLM agents with in-distribution Optimization"
authors:
  - "Yudi Zhang"
  - "Meng Fang"
  - "Zhenfang Chen"
  - "Mykola Pechenizkiy"
date: "2026-06-05"
arxiv_id: "2606.07367"
arxiv_url: "https://arxiv.org/abs/2606.07367"
pdf_url: "https://arxiv.org/pdf/2606.07367v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Credit Assignment"
  - "Process Reward"
  - "Self-Evolution"
  - "Implicit Q-Learning"
  - "Reinforcement Learning"
  - "Interactive Environments"
relevance_score: 9.5
---

# Self-evolving LLM agents with in-distribution Optimization

## 原始摘要

Large Language Models (LLMs) have recently emerged as powerful controllers for interactive agents in complex environments, yet training them to perform reliable long-horizon decision making remains a fundamental challenge. A key difficulty lies in credit assignment: agents often receive delayed rewards only at the end of episodes. In this paper, we propose Q-Evolve, a self-evolving framework for LLM agents that unifies automatic process-reward labeling and policy learning within a principled in-distribution reinforcement learning paradigm. In each evolving iteration, our method learns an in-distribution critic from a hybrid off-policy dataset that combines expert demonstrations with agent-generated trajectories, stabilizing Bellman backups in sparse-reward settings via a weighted Implicit Q-Learning objective. The learned value function is then used to derive step-wise process rewards through advantage estimation, enabling dense and reliable supervision without environment backtracking or human annotation. Leveraging these signals, we perform behavior-proximal policy optimization that evolves the agent over the data used for process reward labeling, allowing iterative self-improvement without exacerbating distribution shift. We evaluate our method on AlfWorld, WebShop, and ScienceWorld, showing Q-Evolve outperforms strong baselines in sample efficiency, robustness, and overall task performance. Our results demonstrate that stable agent self-evolution is achievable through the co-evolution of process-level supervision and policy, both grounded within a shared in-distribution learning loop.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的交互式智能体在长期决策任务中面临的核心挑战：稀疏、延迟的奖励信号导致信用分配困难，且现有方法生成的逐过程奖励（过程奖励模型，PRM）存在严重的分布偏移问题。研究背景是LLM正从静态文本生成转向驱动交互式智能体，以完成复杂环境中的序列决策。现有方法（如在线搜索Q值、分组优势估计等）虽试图自动生成过程监督信号，但主要局限在于：1）过程奖励对状态-动作分布高度敏感，当策略在线优化或与环境动态交互时，智能体行为会偏离PRM训练数据的分布，导致奖励信号失效；2）许多方法依赖环境确定性、状态回溯或状态离散化等强假设，且需要大量在线交互，难以在开放或高风险的现实场景中部署。为此，本文提出Q-Evolve框架，核心目标是实现**同分布（in-distribution）的智能体自我演化**：在一个闭环中同时完成自动过程奖励标注和策略学习，使策略更新始终基于固定混合离线数据，通过价值函数与策略的协同演化避免分布偏移，从而稳定解决长程信用分配问题。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作：

1. **LLM智能体方法**：现有工作利用LLM在代码、数学、游戏、计算机使用和机器人等领域的决策能力，通过规划、工具使用等扩展其应用范围。但长期决策中仍存在稀疏奖励、信用分配和样本效率低下等问题。本文的Q-Evolve针对性地提出了自演化框架来缓解这些挑战。

2. **过程奖励模型**：已有研究主要在数学推理等场景中训练过程奖励模型，通过人为标注或自动计算（如Q值估计）提供步骤级监督。但现有方法在LLM智能体应用中忽略了分布偏移风险。本文通过加权隐含Q学习在分布内稳定贝尔曼备份，并利用优势估计生成密集过程奖励，避免了环境回溯或人工标注。

3. **自演化智能体**：相关研究通过反思推理、记忆增强或自训练实现智能体迭代改进，但通常依赖持续环境交互。本文的区别在于提出“分布内演化循环”，在每次迭代中将策略、评论家与数据集共同演化于共享的分布内数据中，从而在不加剧分布偏移的前提下实现稳定的自我改进。

### Q3: 论文如何解决这个问题？

Q-Evolve通过自进化框架解决长程延迟奖励下的信用分配问题，核心是一个闭环迭代系统。整体框架包含四个阶段的可重复循环：

首先，构建混合离线数据集，将专家演示与当前策略的交互轨迹相结合，以覆盖成功区域和实际失败模式。每个时间步通过回顾性奖励标记，基于LLM自然语言反馈（如格式错误、无效动作、重复观察）自动分配规则化辅助奖励，提供细粒度信号。

其次，在固定数据集上离线训练分布内评论家。采用加权隐式Q学习（IQL），通过两个关键设计解决稀疏奖励难题：一是构建混合数据增强覆盖，二是使用基于轨迹长度和成功标志的步加权（w_t），优先学习成功轨迹后期步的有效信号，稳定贝尔曼备份。

第三，利用学到的价值函数通过广义优势估计（GAE）派生过程奖励，仅使用环境奖励计算优势，避免辅助奖励干扰任务目标。这些优势作为稠密的逐帧监督信号。

最后，采用行为近端策略优化（BPPO）更新策略，该目标使用非对称裁剪（对负动作更激进抑制）和KL正则化，确保更新严格限制在离线数据分布内。每个循环后，新策略在环境中采集新轨迹，刷新混合数据集，实现策略、评论家和数据的协同进化。

### Q4: 论文做了哪些实验？

论文在AlfWorld、WebShop和ScienceWorld三个具有延迟奖励的文本环境上评估了Q-Evolve方法，使用Llama2-7B-Chat作为基础模型，每个任务采样3条轨迹。对比方法包括GPT-4、GPT-3.5-Turbo、Reflexion等强基线，以及微调基线如SFT、RFT、PPO、Best-of-N、ETO、DMPO和QLASS。主要结果如下：在WebShop上，Q-Evolve得分为70.5（第二名QLASS为70.3）；ScienceWorld上，Seen场景76.3（第二QLASS 75.3）、Unseen场景69.7（第二QLASS 66.4）；ALFWorld上，Seen场景90.7（第二QLASS 77.9）、Unseen场景89.6（第二QLASS 82.8）；平均分79.4，显著高于第二名QLASS的74.5。实验表明Q-Evolve在所有任务上均优于对比方法，尤其在ALFWorld上表现出极大的领先优势，证明了其在样本效率、鲁棒性和任务性能上的有效性，验证了通过分布内过程奖励与策略协同进化实现agent稳定自改进的可行性。

### Q5: 有什么可以进一步探索的点？

论文的局限主要体现在两个方面：一是对专家示范的质量依赖较强，若初始示范分布存在偏差，可能限制自我进化的上限；二是隐式Q学习（Implicit Q-Learning）的加权机制在稀疏奖励场景下仍需大量探索样本，对复杂长尾任务泛化不足。未来可探索以下方向：（1）引入离线数据集中的负面样本或对抗性探索，通过动态调整加权阈值增强对分布外状态的鲁棒性；（2）结合世界模型或因果推理，在无过程奖励标签时推测环境反馈的潜在因果结构，降低对交互数据的依赖；（3）设计层级化过程奖励机制，将子目标分解与优势估计解耦，缓解长程信用分配中的方差膨胀问题；（4）探索多智能体协同进化框架，让不同策略的LLM代理相互生成反事实轨迹，加速过程奖励的自动标注与策略收敛的同步优化。

### Q6: 总结一下论文的主要内容

本文提出Q-Evolve，一个用于训练LLM智能体的自进化框架。核心问题是在稀疏延迟奖励的交互环境中，如何为LLM智能体进行有效的信用分配，以使其能够进行可靠的长程决策。现有方法存在分布偏移问题：在线策略优化时，策略会生成超出过程奖励模型（PRM）训练分布的行为，导致反馈失效。Q-Evolve通过将自动过程奖励标注与策略学习统一在一种原理性的分布内强化学习范式中来解决这一问题。方法上，它首先从混合了专家演示和智能体生成轨迹的离策略数据集中学习一个分布内评论家（critic），使用加权隐式Q学习目标来稳定贝尔曼备份，从而解决稀疏奖励问题。接着，通过优势估计从该价值函数导出密集且可靠的步骤级过程奖励，无需环境回溯或人工标注。最后，利用这些信号进行行为邻近策略优化，使智能体在用于过程奖励标注的数据上迭代自我改进，避免加剧分布偏移。在AlfWorld、WebShop和ScienceWorld上的实验表明，Q-Evolve在样本效率、鲁棒性和整体任务性能上均优于强基线。其主要贡献是展示了通过过程监督与策略的共同进化（两者都固定在一个共享的分布内学习循环中）可以实现稳定的智能体自我进化。
