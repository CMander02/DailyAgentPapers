---
title: "SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents"
authors:
  - "Xinshun Feng"
  - "Xinhao Song"
  - "Lijun Li"
  - "Gongshen Liu"
  - "Jing Shao"
date: "2026-04-09"
arxiv_id: "2604.07791"
arxiv_url: "https://arxiv.org/abs/2604.07791"
pdf_url: "https://arxiv.org/pdf/2604.07791v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Self-Evolving Agent"
  - "Tool Use"
  - "Memory"
  - "Reinforcement Learning"
  - "Reward Shaping"
  - "Policy Optimization"
  - "Experience Replay"
relevance_score: 7.5
---

# SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents

## 原始摘要

Recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) have demonstrated significant potential in single-turn reasoning tasks. With the paradigm shift toward self-evolving agentic learning, models are increasingly expected to learn from trajectories by synthesizing tools or accumulating explicit experiences. However, prevailing methods typically rely on large-scale LLMs or multi-agent frameworks, which hinder their deployment in resource-constrained environments. The inherent sparsity of outcome-based rewards also poses a substantial challenge, as agents typically receive feedback only upon completion of tasks. To address these limitations, we introduce a Tool-Memory based self-evolving agentic framework SEARL. Unlike approaches that directly utilize interaction experiences, our method constructs a structured experience memory that integrates planning with execution. This provides a novel state abstraction that facilitates generalization across analogous contexts, such as tool reuse. Consequently, agents extract explicit knowledge from historical data while leveraging inter-trajectory correlations to densify reward signals. We evaluate our framework on knowledge reasoning and mathematics tasks, demonstrating its effectiveness in achieving more practical and efficient learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自进化智能体（self-evolving agents）在资源受限环境和稀疏奖励信号下面临的核心挑战。研究背景是，随着智能体学习范式向自进化方向转变，模型被期望能够通过合成工具或积累显式经验来从轨迹中学习。然而，现有主流方法通常依赖于大规模语言模型（LLMs）或多智能体框架，这导致其在计算资源有限的环境中难以部署。同时，基于任务结果的奖励 inherently sparse，智能体通常只在任务完成时获得反馈，这使得学习过程低效且困难。

现有方法存在两大不足。首先，在工具使用方面，现有框架多采用静态设计，预定义大量固定工具，限制了智能体的适应性和泛化能力；而一些工具生成方法（如Alita, STELLA）虽然能自主创建工具，但将其存储在非结构化仓库中，缺乏结构性连接，导致工具可重用性和细粒度组合能力受限。其次，在经验利用方面，基于强化学习或经验驱动的方法虽然利用历史试验数据，但往往忽略了复杂推理所必需的显式依赖关系，且奖励设计多关注轨迹级成功或格式正确性，缺乏对推理质量的步骤级反馈，限制了其通用性。

因此，本文要解决的核心问题是：如何设计一个高效、实用的自进化智能体框架，使其能够在资源受限环境下，通过结构化地积累和利用工具与经验，克服奖励稀疏性，实现策略与记忆的协同进化与持续能力提升。具体而言，论文提出了SEARL框架，通过联合优化策略模型和基于工具图的结构化记忆，使智能体能够从历史数据中提取显式知识，并利用轨迹间相关性来稠密化奖励信号，从而在知识推理和数学等任务上实现更实用和高效的学习。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及自进化智能体和智能体强化学习两大方向。

在自进化智能体方面，现有研究致力于通过持续适应克服大语言模型的静态局限，其进化维度包括模型参数更新、长期记忆扩展以及自主工具创建或复用，进化方式涵盖推理时的动态调整和跨任务的持续学习。代表性系统如Alita、SE-Agent和Agent KB已在动态工具生成、轨迹优化和跨领域知识迁移方面展现出能力。然而，这些方法大多将工具进化与策略学习视为独立模块进行处理。

在智能体强化学习方面，强化学习已成为改进智能体在多轮环境中决策的核心范式，旨在解决长期信用分配和稀疏奖励等挑战。早期基于轨迹的方法（如GRPO）受限于粗糙的反馈信号，后续研究通过基于组的优势估计以及评估推理质量和工具效率的结构化奖励提升了稳定性。近期工作进一步将训练扩展到更长时序并集成了分层规划。尽管如此，现有方法大多仅专注于优化策略参数，而忽视了持久的外部记忆。

本文与上述工作的核心区别在于，它通过将策略优化与结构化工具图记忆的成长相耦合，桥接了策略学习与持久记忆积累之间的鸿沟。本文提出的SEARL框架构建了一个整合规划与执行的结构化经验记忆，提供了新颖的状态抽象，从而促进了在类似情境（如工具复用）中的泛化，并利用轨迹间的相关性来稠密化奖励信号。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SEARL的、基于工具记忆的自进化智能体框架来解决资源受限环境下基于稀疏奖励的自我进化学习问题。其核心方法是将策略优化与结构化工具图记忆进行联合优化，以提供状态抽象、促进泛化并稠密化奖励信号。

整体框架将决策过程形式化为一个结构化的元推理序列，包含规划、检索、思考、行动四个步骤级组件，并用XML风格标签明确标注以实现细粒度控制。主要模块包括：1）**策略模块**，负责生成全局规划、执行工具检索与调用；2）**奖励模块**，设计了一个复合奖励信号，结合了稀疏的结果奖励（任务完成时获得）和稠密的行为奖励（在规划、工具创建、工具执行等步骤即时获得），以提供更丰富的学习信号；3）**优势估计与策略优化算法**，创新性地提出了一个两级相对优势结构。其中，情节级相对优势在相同任务的多个轨迹上计算，提供全局任务完成质量的信号；步骤级相对优势则不再依赖原始环境状态分组，而是以工具记忆中的具体工具作为锚点进行分组计算，从而在广阔的状态空间中实现有效的细粒度信用分配，并避免奖励黑客问题；4）**工具图记忆模块**，这是一个核心创新组件，以有向图形式存储已注册的工具节点及其依赖关系。其生命周期包括子图提取、工具注册、工具检索和记忆更新四个阶段。在训练过程中，系统会从任务规划中提取子图，通过工具创建奖励鼓励智能体注册新的模块化工具，并使用语义相似度进行工具合并与去重，最终将任务特定的子图整合到全局记忆图中，从而积累可重用的操作知识。

关键技术在于：通过工具图记忆提供了新颖的状态抽象，将连续、开放的状态空间映射到有限的工具集上，使得智能体能够从历史轨迹中提取显性知识，并利用轨迹间的相关性进行泛化（如工具复用）。同时，两级优势估计机制与工具锚定的分组方法，共同解决了多步智能体设置中的信用分配难题，使得学习更加高效和稳定。

### Q4: 论文做了哪些实验？

论文在数学推理和知识密集型多跳问答任务上进行了实验。实验设置方面，研究者使用了两个基础工具：Python解释器和基于本地Wikipedia搜索服务器的搜索接口，以确保资源效率。训练数据采用Tool-star的10,000个开源RL训练样本。评估采用LLM-as-Judge方法，使用Qwen3-32B作为评判模型，以pass@1准确率报告结果。

使用的数据集/基准测试包括：数学推理任务（AIME2024、MATH500、GSM8K）和多跳知识推理任务（WebWalker、HotpotQA、2WikiMultihopQA、Musique、Bamboogle）。对比方法包括TIR Prompting、GRPO、DAPO、REINFORCE++和ARPO等轨迹级RL算法。

主要结果如下：在数学推理任务上，SEARL在GSM8K上达到0.8620，在MATH500上达到0.6820，在AIME24上与ARPO并列最佳（0.3333）。在多跳QA任务上，SEARL在HotpotQA上达到0.3350，在2wiki上达到0.3600，在Bamboogle上达到0.3040，均表现优异。其平均排名（Avg Rank）为1.43（越低越好），显著优于其他方法（如GRPO为2.43）。关键指标显示，SEARL在需要跨源信息组合的任务上优势明显，这归因于其工具图记忆的结构化检索能力。消融实验进一步证实，步骤级分组和步骤奖励对性能至关重要，移除它们会导致显著下降。案例研究也表明，SEARL能通过模块化工具链有效剪枝搜索空间，提升效率与可复用性。

### Q5: 有什么可以进一步探索的点？

该论文在工具构建与记忆整合方面虽有创新，但仍存在几个关键局限和可探索方向。首先，性能差距表明工具生成机制可能对简单任务造成冗余开销，未来可研究自适应机制，根据任务复杂度动态切换工具使用与直接推理，以平衡效率与泛化。其次，工具集的领域局限性提示需探索跨任务或跨领域的工具迁移方法，例如通过元学习或工具抽象层级提升适应性。此外，生成工具的质量问题可通过引入更精细的工具评估与筛选模块，结合人类反馈或模拟环境验证其效用。奖励稀疏性与奖励攻击风险则需设计更密集、多粒度的奖励信号，例如引入过程奖励或基于推理链的验证机制。最后，可考虑将SEARL框架与更轻量化的模型结合，进一步降低资源依赖，同时探索在开放域或动态环境中的长期自我演化能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于工具图记忆的自进化智能体框架SEARL，旨在解决资源受限环境下智能体学习效率低和基于结果的奖励稀疏性问题。其核心贡献是联合优化策略与工具图记忆，通过构建结构化的经验记忆库，将规划与执行整合，提供新颖的状态抽象以促进跨类似情境的泛化。方法上，SEARL不仅存储可执行工具，还捕获其因果依赖和使用上下文，结合基于锚点的优势估计和设计的过程奖励，使智能体能够从历史数据中提取显式知识并利用轨迹间相关性来稠密化奖励信号。实验表明，该框架在知识推理和数学任务上有效实现了更实用高效的学习，推动了自主、开放式通用智能体的发展。
