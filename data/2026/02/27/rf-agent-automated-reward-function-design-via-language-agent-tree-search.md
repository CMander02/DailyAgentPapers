---
title: "RF-Agent: Automated Reward Function Design via Language Agent Tree Search"
authors:
  - "Ning Gao"
  - "Xiuhui Zhang"
  - "Xingyu Jiang"
  - "Mukang You"
  - "Mohan Zhang"
  - "Yue Deng"
date: "2026-02-27"
arxiv_id: "2602.23876"
arxiv_url: "https://arxiv.org/abs/2602.23876"
pdf_url: "https://arxiv.org/pdf/2602.23876v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "规划与推理"
  - "Agentic 强化学习"
  - "自动化奖励设计"
  - "语言智能体"
  - "蒙特卡洛树搜索"
relevance_score: 8.0
---

# RF-Agent: Automated Reward Function Design via Language Agent Tree Search

## 原始摘要

Designing efficient reward functions for low-level control tasks is a challenging problem. Recent research aims to reduce reliance on expert experience by using Large Language Models (LLMs) with task information to generate dense reward functions. These methods typically rely on training results as feedback, iteratively generating new reward functions with greedy or evolutionary algorithms. However, they suffer from poor utilization of historical feedback and inefficient search, resulting in limited improvements in complex control tasks. To address this challenge, we propose RF-Agent, a framework that treats LLMs as language agents and frames reward function design as a sequential decision-making process, enhancing optimization through better contextual reasoning. RF-Agent integrates Monte Carlo Tree Search (MCTS) to manage the reward design and optimization process, leveraging the multi-stage contextual reasoning ability of LLMs. This approach better utilizes historical information and improves search efficiency to identify promising reward functions. Outstanding experimental results in 17 diverse low-level control tasks demonstrate the effectiveness of our method. The source code is available at https://github.com/deng-ai-lab/RF-Agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习中低层控制任务（如运动、复杂操作）的奖励函数自动化设计难题。传统方法依赖专家手动设计密集奖励函数，虽可解释但耗时且易次优；逆强化学习和基于偏好的强化学习虽能自动生成奖励，却需要大量专家数据且缺乏可解释性。近期，基于大语言模型（LLM）的方法（如L2R、Text2Reward）利用LLM的世界知识和代码能力生成可解释的奖励函数，减少了专家依赖，但现有方法（如Eureka的贪心算法、Revolve的进化算法）存在两大不足：一是搜索效率低，难以在探索与利用间取得平衡，易陷入局部最优；二是历史反馈利用不足，仅保留局部信息，忽略了从低性能到高性能奖励函数的潜在决策路径。因此，本文的核心问题是：如何更高效地利用LLM进行奖励函数设计，以提升复杂控制任务中的性能与训练效率。为此，论文提出RF-Agent框架，将LLM视为语言智能体，把奖励函数设计重构为序列决策过程，并引入蒙特卡洛树搜索（MCTS）来管理搜索过程，以增强上下文推理能力，从而充分利用历史信息、优化搜索策略，最终生成高性能且训练高效的奖励函数。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：奖励函数设计和基于LLM的智能体决策。

在**奖励函数设计**方面，相关工作主要利用LLM生成奖励函数以降低对专家经验的依赖。早期方法如L2R和T2R能够生成密集、可解释的奖励函数代码，开创了有前景的范式。近期工作如Eureka采用贪婪迭代优化，Revolve则结合进化算法来演化新奖励。然而，这些方法普遍存在**历史反馈利用不足**和**搜索效率低下**的问题。本文提出的RF-Agent与这些工作目标一致，但通过引入蒙特卡洛树搜索（MCTS）将奖励设计构建为序列决策过程，从而更有效地利用历史信息和LLM的上下文推理能力，显著提升了在复杂控制任务中的优化性能。

在**基于LLM的智能体决策**方面，LLM因其世界知识和逻辑推理能力被用作智能体解决决策问题，例如在机器人规划或网页交互中。随着任务变复杂，出现了如ReAct的线性推理方法，以及如ToT、LATS和RAP等采用树搜索（尤其是MCTS）来增强推理和探索替代决策路径的方法。本文**受此类方法启发**，同样将奖励设计视为决策过程，并整合MCTS来管理优化流程。与单纯用于环境交互的智能体不同，RF-Agent专注于**内部优化搜索**，利用LLM的多阶段推理来分析和利用历史反馈，从而生成更高质量的奖励函数。

### Q3: 论文如何解决这个问题？

论文通过提出RF-Agent框架，将奖励函数设计问题构建为一个序列决策过程，并利用大语言模型作为语言智能体，结合蒙特卡洛树搜索来优化搜索效率。其核心方法是将每个由LLM生成的奖励函数视为一个动作，将输入指令视为状态，通过树搜索结构来管理和迭代优化过程。

整体框架基于MCTS的四阶段循环：选择、扩展、模拟和反向传播。主要模块包括：1）初始化模块，利用LLM的零样本能力根据任务信息和环境观察生成初始奖励函数及设计思路，并训练策略获得反馈；2）选择模块，采用改进的UCT公式，综合考虑评估分数、自我验证分数和访问次数，以平衡探索与利用，从而选择有潜力的节点；3）扩展模块，定义了五种基于LLM的动作类型来生成新的奖励函数，包括突变（局部修改结构或参数）、交叉（结合精英节点信息）、路径推理（利用优化路径历史）、不同思路（避免早熟收敛），这些动作充分利用了树中存储的历史反馈信息；4）模拟模块，使用生成的奖励函数训练策略，并引入设计思路对齐过程，确保奖励函数与逻辑描述的一致性；5）反向传播模块，更新节点的Q值和访问次数，并生成自我验证分数以辅助后续选择。

关键技术包括：改进的UCT选择策略，融入归一化的Q值和LLM生成的自我验证分数；多类型动作驱动的扩展机制，通过结构化提示引导LLM进行多样化探索；设计思路对齐技术，在模拟后重新生成与奖励函数匹配的详细思路，提升历史信息的可靠性。创新点在于将MCTS与LLM的多阶段上下文推理能力深度结合，通过树结构系统化地积累和利用历史反馈，克服了以往方法信息利用不足和搜索效率低下的问题，从而在复杂控制任务中实现了更高效的奖励函数自动设计。

### Q4: 论文做了哪些实验？

论文在IsaacGym和Bi-DexHands两个低层控制环境中进行了实验，涵盖8种控制智能体和17个多样化任务。实验设置上，所有任务均使用调优后的PPO算法及基准默认超参数进行策略训练，每个最终奖励函数使用5个不同种子单独训练并报告各检查点平均最大评估分数。对比方法包括：Human（专家设计的密集奖励函数）、Sparse（使用稀疏评估分数作为奖励）、Eureka（基于任务信息和环境观察批量生成奖励的贪婪迭代方法）以及Revolve（使用环境反馈的自动化进化算法版本）。为确保公平比较，所有基于LLM的方法设定了相同的总奖励函数采样数（IsaacGym为80，Bi-DexHands为512），并使用了GPT-4o-mini和GPT-4o两种LLM骨干模型。

主要结果方面，在IsaacGym的7个任务中，RF-Agent在两种LLM模型下均取得最佳性能。关键指标如平均归一化分数（Avg norm score），使用GPT-4o-mini时RF-Agent为1.70，显著高于Eureka的0.63和Revolve的0.67；使用GPT-4o时RF-Agent进一步提升至2.68，优于Eureka的2.00和Revolve的2.03。在具体任务上，例如Ant任务中，RF-Agent（GPT-4o）得分为7.10±0.11，高于Human的6.75±0.30。在Bi-DexHands的10个复杂操作任务中，RF-Agent在Expert-Easy和Expert-Hard两组任务上的成功率均明显优于人类专家和其他对比方法，尤其在复杂任务上优势显著。此外，训练曲线和搜索性能图显示，RF-Agent生成的奖励函数能使策略更快收敛到更高成功率，且其奖励函数优化效率更高。消融实验进一步验证了其搜索方法、动作设计和推理组件对性能提升的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于计算成本高昂，需要多次与LLM交互并进行重复的策略训练，导致时间和资源消耗大。尽管RF-Agent通过树搜索提升了历史信息利用和搜索效率，但未减少强化学习训练迭代次数，这在复杂任务中可能限制其可扩展性。

未来研究方向可聚焦于：1）优化训练效率，例如引入元学习或课程学习来加速策略收敛，减少训练周期；2）增强LLM的推理能力，结合符号推理或知识图谱，提升奖励函数设计的准确性和可解释性；3）扩展应用场景，如将其适配到高维或动态环境中，测试其泛化性能；4）探索多智能体协作设计，通过分布式搜索或协同优化进一步提升效率。这些改进有望在保持性能的同时降低计算负担，推动自动化奖励设计走向实用化。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为RF-Agent的自动化奖励函数设计框架，旨在解决强化学习中为复杂低层控制任务手动设计高效奖励函数的难题。其核心贡献在于将大型语言模型（LLM）视为语言智能体，并将奖励函数设计问题重新定义为序列决策过程，从而利用LLM的多阶段上下文推理能力来优化设计。

在方法上，RF-Agent创新性地集成了蒙特卡洛树搜索（MCTS）来管理奖励函数的设计与优化流程。该方法将历史反馈信息（如训练结果）整合到搜索树中，引导LLM进行更高效的探索与利用，克服了现有方法（如贪婪或进化算法）对历史信息利用不足、搜索效率低下的局限。这使得框架能够更系统地探索奖励函数空间，并识别出有潜力的候选函数。

实验结果表明，RF-Agent在17个多样化的低层控制任务上取得了优异的性能，显著超越了现有方法，证明了其有效性和通用性。该工作的意义在于为自动化奖励工程提供了一种新范式，通过结合LLM的推理能力与MCTS的结构化搜索，减少了对专家经验的依赖，并有望推动复杂强化学习任务的自动化解决。
