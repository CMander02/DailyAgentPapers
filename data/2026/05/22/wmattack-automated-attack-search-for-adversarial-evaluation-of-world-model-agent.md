---
title: "WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents"
authors:
  - "Zhixiang Guo"
  - "Siyuan Liang"
  - "Shi Fu"
  - "Cheng Guo"
  - "Andras Balogh"
  - "Mark Jelasity"
  - "Dacheng Tao"
date: "2026-05-22"
arxiv_id: "2605.23220"
arxiv_url: "https://arxiv.org/abs/2605.23220"
pdf_url: "https://arxiv.org/pdf/2605.23220v1"
categories:
  - "cs.LG"
tags:
  - "对抗攻击"
  - "World Model Agent"
  - "自主攻击搜索"
  - "鲁棒性评估"
  - "DreamerV3"
relevance_score: 9.5
---

# WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents

## 原始摘要

Despite the growing use of world models as decision-making agents, their adversarial robustness remains underexplored due to the lack of dedicated automated evaluation methods. A key obstacle is that attack evaluation must be both accurate and efficient: weak manually tuned attacks can overestimate robustness, while exhaustive hyperparameter search is prohibitively expensive because each candidate requires closed-loop rollouts through learned latent dynamics. We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents. WMAttack formulates robustness evaluation as a finite-budget search over attack configurations, including attack families, perturbation budgets, optimization steps, restarts, and allocation rules. To improve search accuracy, Self-Correcting Attack Search (SCAS) refines the attack proposal distribution using feedback from reward degradation, action instability, runtime cost, and rollout variability. To improve search efficiency, Representation-Guided Attack Retrieval (RGAR) retrieves effective historical configurations from representation-similar tasks, providing a warm start for unseen environments. We provide a theoretical explanation showing that proposal refinement improves finite-budget search when it shifts probability mass toward high-utility attacks. Across Atari and DeepMind Control tasks, WMAttack consistently discovers stronger attacks than the evaluated baselines, improving normalized reward drop from 0.497 to 1.034 on DreamerV3 Atari and from 0.319 to 0.682 on DMC. Ablations further show that RGAR improves initial candidate quality and SCAS improves final attack utility under fixed evaluation budgets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决世界模型（world model）作为决策智能体时，其对抗鲁棒性缺乏自动化评估方法的问题。研究背景方面，世界模型凭借其通过潜在动力学进行样本高效规划与预测的能力，已成为决策智能体的基础范式。然而，现有方法存在明显不足：一方面，手动调参的弱攻击可能高估模型鲁棒性，产生伪鲁棒性；另一方面，由于每个候选攻击配置都需要进行闭环 rollout 并反复计算潜在动力学，穷举超参数搜索的计算成本极高，无法实际应用。不同世界模型环境在观测空间、奖励尺度、时间结构和策略敏感性上差异巨大，攻击有效性高度依赖于环境动态和对抗超参数，使得鲁棒性评估变得极具挑战。核心问题在于，如何高效地暴露并量化世界模型智能体在对抗条件下的失效模式，同时兼顾评估的准确性与效率。为此，本文提出了 WMAttack，一个自动化的攻击搜索框架。该框架将鲁棒性评估形式化为一个有限预算下的攻击配置搜索问题，并能够通过跨任务经验迁移和自适应配置优化，在固定评估预算内发现更强的攻击，从而实现对世界模型智能体更准确的对抗鲁棒性评估。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是世界模型方法本身，包括PlaNet、Dreamer系列（V1/V2/V3）、IRIS、STORM、DIAMOND等，这些是本文攻击评估的对象，其基于学习到的潜在动力学进行决策；二是对抗攻击方法，如State-Adversarial MDP框架、针对性时序攻击和对抗策略等，本文在此基础上扩展为自动化的攻击搜索；三是鲁棒性评估工作，包括WorldBench和iWorld-Bench等诊断基准，以及AutoAttack等静态评估协议和Claudini等自动搜索系统。与传统方法不同，WMAttack针对世界模型的闭环评估需求，将鲁棒性评估形式化为有限预算攻击搜索，并通过表征引导检索（RGAR）和自纠正搜索（SCAS）分别提升搜索效率和准确性，填补了现有工作在自动化、高效评估世界模型鲁棒性方面的空白。

### Q3: 论文如何解决这个问题？

WMAttack将鲁棒性评估形式化为一个有限预算的攻击配置搜索问题，并为此设计了一个自动化攻击搜索框架。其核心架构由两个关键组件构成：表示引导的攻击检索（RGAR）和自纠正攻击搜索（SCAS）。

首先，RGAR用于解决冷启动问题。它通过构建一个包含潜在状态、预测的未来状态、动作和奖励的轨迹级行为摘要 \(\psi_\tau\)，来表征智能体的行为。对于一个新任务，RGAR会在攻击存储器中检索与该任务摘要表示最相似的历史任务记录，并利用这些历史任务上高效攻击配置的加权组合，来初始化一个热启动的候选攻击分布 \(q_0(c \mid \tau)\)，从而避免了从随机配置开始搜索，显著提升了初期候选配置的质量。

其次，SCAS负责在搜索过程中进行自适应优化。每一轮，WMAttack都从当前候选分布 \(q_t\) 中采样一批攻击配置，并通过闭环仿真进行代价评估。SCAS会收集奖励下降、动作不稳定、评估成本和仿真方差等反馈信号，并据此更新攻击配置的优选分布 \(q_{t+1}\)。该更新过程通过融合历史搜索经验中的高质量样本和方向性反馈，将搜索预算持续引向更可能暴露智能体缺陷的攻击区域，从而不断提升后续批次中发现高效攻击的概率。

创新点在于，WMAttack将自动化攻击搜索与表示学习和自纠正机制相结合，通过RGAR提供知识迁移的冷启动，再通过SCAS根据在线反馈进行动态调整，形成一个从初始化到自适应的完整攻击挖掘循环，有效解决了传统方法中手动调参不准确或穷举搜索代价过高的问题。

### Q4: 论文做了哪些实验？

论文在Atari和DeepMind Control Suite（DMC）上评估了WMAttack，主要受害模型为DreamerV3（26个Atari任务和20个DMC任务），并扩展至DreamerV2、TD-MPC2和IRIS。对比方法包括随机搜索（Random）和Claudini风格基线。攻击搜索空间涵盖APGD-CE、APGD-DLR、FAB、Square Attack和PhysCond-WMA五种攻击族，配置包括扰动预算ε、优化步数、重启次数等。主要结果：在DreamerV3 Atari上，WMAttack的归一化奖励下降（Drop）为1.034，远高于Claudini（0.497）和Random（0.446），并实现唯一正效用值（0.430）；在DMC上，Drop达0.682，动作翻转率0.800。消融实验显示，结合RGAR和SCAS后，首轮效用从0.048提升至0.397，最终效用达0.020。效率方面，WMAttack在Atari上达到90%最佳效用的命中率为87.5%，高于Claudini（53.8%）和Random（52.9%）。此外，Qwen2.5-3B在Drop（1.034）和效用（0.430）上表现最佳，但更大模型并非必然更好。

### Q5: 有什么可以进一步探索的点？

该论文在自动化攻击搜索方面做出了贡献，但仍存在若干可探索的方向。首先，当前方法依赖固定的攻击类型集合（如FGSM、PGD），未来可引入自适应攻击生成技术，使攻击策略能根据智能体动态实时演化。其次，SCAS的反馈信号（如奖励衰减、动作不稳定性）局限于系统级指标，若能结合模型内部表示（如潜在状态分布偏移）构建更细粒度的反馈机制，可能提升搜索精度。此外，RGAR的跨任务迁移依赖任务表示的相似性，但未考虑任务结构异质性，可探索基于因果结构或行为语义的迁移策略。另一个方向是将攻击搜索与防御训练结合，通过对抗训练使世界模型更鲁棒，同时评估搜索方法对防御效果的促进。最后，当前实验仅覆盖Atari和DMC两类控制任务，扩展到更复杂的3D环境或多智能体场景将验证框架的泛化能力。未来工作可聚焦于多目标优化，在攻击成功率与计算成本之间取得更优平衡。

### Q6: 总结一下论文的主要内容

论文提出 WMAttack，一个用于世界模型智能体对抗鲁棒性评估的自动化攻击搜索框架。当前世界模型应用广泛，但缺乏专门的自动化评估方法，手动调参易高估鲁棒性，而穷举搜索因需要闭环 rollout 而代价高昂。WMAttack 将鲁棒性评估定义为有限预算下的攻击配置搜索问题，包括攻击类型、扰动预算、优化步数等。其核心包含两个组件：表征引导攻击检索（RGAR）利用世界模型间的表征相似性，从历史任务中检索有效配置作为新任务的热启动；自纠正攻击搜索（SCAS）通过奖励下降、动作不稳定等多维反馈迭代优化攻击策略的提议分布。理论上证明，反馈驱动的提议细化能在有限预算下提升攻击搜索效率。在 Atari 和 DeepMind Control 任务上，WMAttack 在 DreamerV3 上使归一化奖励下降从 0.497 提升至 1.034，在 DMC 上从 0.319 提升至 0.682，且消融实验验证了 RGAR 和 SCAS 各自的有效性。该工作系统性地揭示了世界模型智能体的对抗脆弱性，为安全评估提供了高效自动化工具。
