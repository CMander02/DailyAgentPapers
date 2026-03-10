---
title: "RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback"
authors:
  - "Xiaoying Zhang"
  - "Zichen Liu"
  - "Yipeng Zhang"
  - "Xia Hu"
  - "Wenqi Shao"
date: "2026-03-09"
arxiv_id: "2603.08561"
arxiv_url: "https://arxiv.org/abs/2603.08561"
pdf_url: "https://arxiv.org/pdf/2603.08561v1"
categories:
  - "cs.AI"
tags:
  - "强化学习"
  - "在线学习"
  - "内在反馈"
  - "自我反思"
  - "记忆检索"
  - "经验学习"
  - "探索策略"
  - "任务泛化"
relevance_score: 9.5
---

# RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback

## 原始摘要

Large language model (LLM)-based agents trained with reinforcement learning (RL) have shown strong potential on complex interactive tasks. However, standard RL paradigms favor static problem-solving over continuous adaptation: agents often converge to suboptimal strategies due to insufficient exploration, while learned knowledge remains implicit within parameters rather than explicitly retrievable, limiting effective experiential learning. To address these limitations, we introduce RetroAgent, an online RL framework that empowers agents to master complex interactive environments not just by solving, but by evolving. Concretely, RetroAgent features a hindsight self-reflection mechanism that produces dual intrinsic feedback: (1) intrinsic numerical feedback that that tracks incremental subtask completion relative to prior attempts, rewarding promising explorations, and (2) intrinsic language feedback that distills reusable lessons into a memory buffer, retrieved via our proposed Similarity & Utility-Aware Upper Confidence Bound (SimUtil-UCB) strategy balancing relevance, utility, and exploration to effectively leverage past experiences. Extensive experiments on two model families across four challenging agentic tasks demonstrate that RetroAgent significantly outperforms existing methods, achieving state-of-the-art results -- e.g., surpassing Group Relative Policy Optimization (GRPO)-trained agents by +18.3% on ALFWorld, +15.4% on WebShop, +27.1% on Sokoban, and +8.9% on MineSweeper -- while exhibiting strong test-time adaptation and generalization to out-of-distribution scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在强化学习（RL）训练中存在的两大核心问题：探索不足导致策略早熟收敛于次优解，以及经验知识隐式存储在模型参数中而无法被显式检索和复用，从而限制了智能体的持续适应与进化能力。

研究背景是，当前利用RL训练LLM智能体以掌握复杂交互任务已成为主流范式。然而，现有标准RL范式通常侧重于“学会解决一个具体问题”，而非“持续适应”。例如，在具身AI任务中，训练往往在找到一个有效动作序列后就终止。这导致了两个关键不足：首先，智能体倾向于利用（exploitation）而非探索（exploration），容易过早收敛到并非最优的策略；其次，学到的知识隐含在模型参数内部，过去的成功或失败经验无法被显式地提取和用于指导后续决策，导致学习效率低下和泛化能力脆弱。

针对这些不足，现有研究大致分为两条独立路线：一是通过元RL或不确定性校准等方式促进探索，二是为智能体添加显式记忆机制来存储历史或提炼技能。但这些方法各自为战，未能将“解决问题”和“持续适应”有机结合起来。

因此，本文提出的核心问题是：如何设计一个统一的RL框架，使智能体不仅能解决当前任务，还能通过回顾反思实现自我进化，从而在复杂交互环境中实现更高效的学习、更强的探索能力和更优的泛化性能？为此，论文引入了RetroAgent框架，其核心是通过事后回顾机制产生双重内在反馈（数值反馈和语言反馈），并配合新颖的记忆检索策略，旨在同时攻克探索不足和经验隐式化这两大瓶颈，桥接“解决”与“进化”之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM作为决策智能体、用于LLM智能体的强化学习，以及基于反思的经验学习。

在**LLM作为决策智能体**方面，相关工作分为两类：一是提示冻结LLM的方法（如ReAct、Reflexion），依赖上下文示例和外部工具，但受限于基础模型能力；二是直接训练LLM智能体的方法（如监督微调或强化学习），使智能体能从环境交互中学习。本文属于后者，但侧重于通过强化学习实现持续进化。

在**用于LLM智能体的强化学习**方面，现有工作（如ArCHer、LOOP、GRPO及其变体GiGPO）主要利用外部环境反馈进行优化，并改进信用分配。Meta-RL方法（如LAMER）支持跨回合训练以促进探索。与这些主要依赖外在奖励的方法不同，本文提出的RetroAgent通过事后自我反思机制产生**双重内在反馈**，将目标从静态问题解决转向持续适应。

在**基于反思的经验学习**方面，早期研究利用语言反馈或反思记忆，通过上下文学习迭代改进任务表现。后续工作将反馈内化到模型参数中（如用于元RL或策略优化的反思数据），或采用基于记忆的架构存储经验以供检索。本文沿用了记忆检索的思路，但创新性地**同时生成内在数值反馈（奖励子任务进展）和内在语言反馈（提炼可重用经验）**，并通过提出的SimUtil-UCB检索策略平衡相关性、效用和探索，从而更有效地利用过去经验驱动策略优化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RetroAgent的在线强化学习框架来解决传统RL智能体在复杂交互任务中探索不足、知识隐式化以及难以持续适应的问题。其核心方法是引入一个“事后自我反思”机制，该机制在每一轮训练结束后分析轨迹，并产生两种形式的内在反馈，共同驱动智能体从“解决问题”向“持续进化”转变。

整体框架基于标准的马尔可夫决策过程建模，但通过创新的模块进行增强。主要组件包括：
1.  **自我反思机制**：这是框架的核心。在每个训练回合后，该机制分析轨迹，生成一个包含三个部分的反思元组：用于量化子任务完成度的“潜力分数”、二元成功预测、以及从经验中提炼的可重用自然语言“教训”。
2.  **双内在反馈生成**：
    *   **内在数值反馈**：基于反思得到的潜力分数计算。通过维护一个历史最佳平均成功率基线，将当前潜力分数超出该基线的部分作为奖励。这种“能力进化奖励”旨在鼓励那些虽未立即成功但显示出进步潜力的探索行为，解决了稀疏奖励下的探索难题。
    *   **内在语言反馈**：将反思提炼出的“教训”存储在一个持久化的记忆缓冲区中。当面对新任务时，通过创新的 **SimUtil-UCB检索策略** 从缓冲区中检索相关教训，并将其作为上下文提示注入策略模型，提供语义丰富的行动指导。
3.  **SimUtil-UCB检索策略**：这是利用过去经验的关键创新点。该策略在检索时综合考虑三个标准：1）**语义相关性**，确保教训与当前任务相关；2）**反思效用**，基于历史记录评估教训的有用性；3）**探索覆盖度**，采用上置信界方法鼓励探索使用次数较少的教训。通过凸组合将相关性与UCB增强后的效用分结合，实现经验的有效利用与探索的平衡。
4.  **策略优化**：框架与GRPO等RL算法兼容。在轨迹生成阶段，一半轨迹使用基础策略，另一半使用经记忆检索增强的策略，兼顾探索与利用。优化目标结合了基于外在奖励和内在数值反馈的决策目标，以及在“RL训练变体”中可选的自反思准确性目标。

创新点在于将元认知（自我反思）思想形式化为一个可训练的、产生双模态反馈的机制。它不仅通过基于潜力的数值奖励塑造探索，更重要的是通过SimUtil-UCB策略显式地管理和重用语义化的经验知识，使学习到的知识可检索、可迁移，从而实现了持续的适应和进化，在多个基准任务上取得了显著优于现有方法的效果。

### Q4: 论文做了哪些实验？

论文在四个具有挑战性的智能体任务上进行了广泛的实验评估。实验设置方面，主要采用Qwen2.7B和Llama-3.1-8B-Instruct模型，以GRPO算法为默认强化学习基础，并基于Verl训练库实现。训练时，智能体从训练集轨迹中提炼经验作为记忆；测试时，则利用这些记忆完成任务。

使用的数据集/基准测试包括：1）ALFWorld（基于文本的具身环境，评估了分布内和分布外泛化）；2）WebShop（模拟电商环境）；3）Sokoban（推箱子规划任务，使用6x6棋盘和2个箱子）；4）MineSweeper（扫雷逻辑任务，使用6x6棋盘和3个地雷）。主要评估指标为成功率，WebShop额外使用任务分数。

对比方法涵盖四大类：1）基于提示的方法（如ReAct、Reflexion）；2）RL算法（如RLOO、GRPO、GiGPO）；3）基于RL的框架（如MemRL、EvolveR、SkillRL、GRPO w/ EMPG）；4）元RL框架（LaMer）。

主要结果显示，RetroAgent在所有任务上均取得最先进性能。关键数据指标为：在ALFWorld上成功率达95.6%（超越GRPO基线+18.3%），WebShop任务分数达88.9%（超越GRPO+15.4%），Sokoban成功率达38.3%（超越GRPO+27.1%），MineSweeper成功率达48.2%（超越GRPO+8.9%）。此外，测试时适应能力评估（使用Discovery@k指标）表明，RetroAgent在三次尝试内能在分布内（WebShop）达到99.0%、分布外（ALFWorld）达到100.0%的发现率，显著优于基线。消融实验证实，双内在反馈设计具有互补性，且训练后提炼的经验知识已有效内化到策略权重中。

### Q5: 有什么可以进一步探索的点？

RetroAgent通过事后反思机制和双内在反馈有效提升了LLM智能体的探索与适应能力，但其设计仍存在一些局限和可拓展方向。首先，论文中反思机制的质量高度依赖于提示工程或额外的RL训练，这可能导致反馈的稳定性和泛化性不足。未来可探索更自动化的反思生成方法，例如通过元学习或引入外部知识库来增强反思的深度和准确性。其次，SimUtil-UCB检索策略虽然平衡了相关性与效用，但记忆缓冲区的管理仍较为简单，缺乏对长期记忆的压缩与抽象能力。可考虑引入分层记忆结构，将具体经验归纳为更高阶的策略知识，以提升跨任务泛化效率。此外，实验集中于相对封闭的交互环境（如ALFWorld、WebShop），未来需验证在开放世界、多模态或具身任务中的有效性，例如在机器人操作或复杂游戏环境中测试其持续进化能力。另一个潜在方向是将双内在反馈与模型参数更新更紧密地结合，例如通过反思直接微调策略网络，而不仅依赖于上下文提示，从而减少推理开销并提升决策速度。最后，当前框架未充分考虑多智能体协作场景，未来可探索分布式反思与知识共享机制，使智能体群体能协同进化，应对更复杂的动态环境。

### Q6: 总结一下论文的主要内容

本文提出RetroAgent，一个旨在解决现有强化学习（RL）训练大语言模型（LLM）智能体时存在局限性的在线RL框架。核心问题是标准RL范式偏向静态问题求解而非持续适应，导致智能体探索不足、易收敛于次优策略，且学到的知识隐式存储在参数中难以显式检索利用。

RetroAgent的核心方法是引入一种事后回顾机制，生成双重内在反馈。第一重是内在数值反馈，通过追踪相较于先前尝试在子任务完成度上的增量进展来提供标量奖励，以鼓励有潜力的探索行为。第二重是内在语言反馈，将过去的成功与失败经验提炼成可重用的行动教训，存储于显式记忆缓冲区中。为了高效检索这些知识，论文提出了相似性与效用感知上置信界（SimUtil-UCB）策略，该策略在检索时综合考虑了记忆条目的语义相关性、历史效用以及探索需求。

实验在ALFWorld、WebShop、Sokoban和MineSweeper四个具有挑战性的任务上进行，结果表明RetroAgent显著超越了现有方法，取得了最先进的性能，并在测试时适应和分布外泛化方面表现出强大能力。论文的主要贡献在于将探索促进与显式记忆机制相结合，使智能体不仅能“解决问题”，更能通过持续积累和利用经验实现“自我进化”。
