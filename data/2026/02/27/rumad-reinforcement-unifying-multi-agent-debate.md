---
title: "RUMAD: Reinforcement-Unifying Multi-Agent Debate"
authors:
  - "Chao Wang"
  - "Han Lin"
  - "Huaze Tang"
  - "Huijing Lin"
  - "Wenbo Ding"
date: "2026-02-27"
arxiv_id: "2602.23864"
arxiv_url: "https://arxiv.org/abs/2602.23864"
pdf_url: "https://arxiv.org/pdf/2602.23864v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "多智能体辩论"
  - "强化学习"
  - "Agent架构"
  - "Agent协调"
  - "Agent推理"
  - "动态通信拓扑"
  - "资源效率"
relevance_score: 9.0
---

# RUMAD: Reinforcement-Unifying Multi-Agent Debate

## 原始摘要

Multi-agent debate (MAD) systems leverage collective intelligence to enhance reasoning capabilities, yet existing approaches struggle to simultaneously optimize accuracy, consensus formation, and computational efficiency. Static topology methods lack adaptability to task complexity variations, while external LLM-based coordination risks introducing privileged knowledge that compromises debate neutrality. This work presents RUMAD (Reinforcement-Unifying Multi-Agent Debate), a novel framework that formulates dynamic communication topology control in MAD as a reinforcement learning (RL) problem.
  RUMAD employs a content-agnostic observation scheme that captures high-level debate dynamics avoiding access to raw agent reasoning content. RUMAD uses a multi-objective reward to model solution quality, cohesion and efficiency. A PPO-trained controller dynamically adjusts edge weights in the communication graph, while a dual-threshold mechanism enables fine-grained control over both agent activation and information visibility.
  Experimental evaluation across MMLU, GSM8K, and GPQA benchmarks demonstrates that RUMAD achieves substantial efficiency gains, reducing token costs by over 80\%, while still improving reasoning accuracy compared to single LLM model and multiple MAD baselines. Notably, RUMAD trained exclusively on MMLU exhibits robust zero-shot generalization to out-of-domain (OOD) tasks, indicating that the learned communication strategies capture task-independent principles of effective multi-agent coordination. These results establish RUMAD as a efficient and robust approach for deploying multi-agent reasoning application with practical resource constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体辩论（MAD）系统中，如何同时优化推理准确性、共识形成和计算效率的核心难题。研究背景是，利用多个大语言模型（LLM）进行集体辩论可以提升推理能力，但现有方法在平衡这些目标上存在显著不足。

现有方法主要有两类不足：第一类是采用静态拓扑结构（如环形、星形）的方法，它们缺乏对任务复杂度变化的适应性。对于简单任务，它们可能保留了冗余的低价值通信连接，浪费计算资源；对于复杂任务，又可能切断了有价值的信息路径，损害集体推理能力。第二类是引入外部LLM（如GPT-4）作为“裁判”或“总结者”的协调方法，这虽然增加了适应性，但外部模型会接触到辩论内容，其引入的“特权知识”可能压制内部智能体群体的观点多样性，破坏辩论的中立性。此外，现有方法普遍缺乏对通信成本（即token消耗）的显式建模和精细控制，难以在实际资源约束下部署。

因此，本文提出的核心问题是：能否设计一个无需外部LLM干预、能够动态适应辩论过程、并同时优化准确性、共识与效率的多智能体辩论框架？为此，论文引入了RUMAD框架，其核心创新在于将动态通信拓扑控制形式化为一个强化学习问题。RUMAD通过一个内容无关的观察机制（仅捕捉高层辩论动态，如语义相似性、答案一致性等标量信息）和一个多目标奖励函数（同时建模解决方案质量、内聚力和效率），训练一个PPO控制器来动态调整通信图中的边权重。该框架还采用双阈值机制对智能体激活和信息可见性进行细粒度控制，从而在保持辩论中立性的前提下，实现准确性、共识形成与计算效率的协同优化。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多智能体辩论（MAD）的通信拓扑设计和基于强化学习（RL）的智能体协调方法展开，可分为以下几类：

**1. 静态拓扑方法**：早期MAD系统通常采用全连接等固定拓扑，但效率低下。后续研究如S-MAD引入了环状、星型等稀疏固定模式，Group Debate和S²-MAD则采用静态分组或两阶段拓扑，旨在平衡共识形成与计算成本。这些方法依赖于预设的、任务无关的静态结构，无法根据辩论动态或任务复杂度进行自适应调整。

**2. 工作流优化方法**：近期研究如MACNET、AFlow和MaAS关注于为多智能体系统自动生成或选择静态工作流。例如，AFlow使用蒙特卡洛树搜索寻找最优静态工作流，MaAS则根据查询选择静态流程。这些方法主要优化任务级别的、一次性的流程编排，而非辩论过程中动态的、轮次级的通信管理。

**3. 基于强化学习的协调方法**：强化学习被用于建模多智能体系统中的时序动态。例如，FMH等分层RL框架使用多层面奖励进行语义任务分解。然而，这些方法通常关注于通过管理者-工作者模式生成子目标，与动态通信控制的侧重点不同。

**本文工作（RUMAD）与上述研究的区别在于**：它将MAD中的动态通信拓扑控制形式化为一个RL问题，其核心创新在于**轮次级的自适应图结构调控**。与静态拓扑或工作流方法不同，RUMAD的控制器在每一轮都根据辩论状态（如智能体一致性）动态调整通信图中的边权重，并能通过双阈值机制精细控制智能体激活与信息可见性。此外，RUMAD采用了**内容无关的观察方案**和**多目标奖励函数**，以中立的方式建模解决方案质量、内聚力和效率的权衡，避免了引入特权知识，这与依赖外部LLM进行协调或访问内部推理内容的方法形成对比。

### Q3: 论文如何解决这个问题？

RUMAD 通过一个基于强化学习的自适应拓扑控制框架来解决多智能体辩论中精度、共识形成与计算效率难以协同优化的问题。其核心方法是将动态通信拓扑控制建模为一个强化学习问题，并设计了内容无关的观察、多目标奖励和双重阈值机制等关键技术。

整体框架分为三个阶段：1）独立初始化，各智能体独立生成初始答案以确保多样性；2）自适应稀疏辩论，在强化学习控制器的动态调节下进行多轮迭代交互；3）共识形成，通过多数投票聚合最终答案。主要模块包括一个集中式的PPO训练控制器、一个内容无关的观察编码器和一个基于双重阈值的通信调节机制。

创新点首先体现在**内容无关的观察方案**上。控制器不访问智能体的原始推理文本或嵌入，仅观察一个 N×N 的相似度矩阵。该矩阵由智能体间答案的一致性指标和推理嵌入的余弦相似度加权组合而成，从而在保护辩论中立性的同时捕捉高层辩论动态。

其次，**随机且可微的动作空间参数化**是关键。对于通信图中每条有向边，策略网络输出一个高斯分布的参数，从中采样并经过Sigmoid变换得到连续的通信权重。这种设计便于使用PPO进行随机梯度优化，支持对高维动作空间的有效探索和稳健的信用分配。

第三，**双重阈值机制**实现了对通信效率和信息流的细粒度控制。一方面，通过计算每个智能体的平均外部影响力（入度权重均值），并与一个激活阈值（设计为智能体对自身观点的权重）比较，决定该智能体在本轮是否被“修剪”（即复用上一轮回答以节省token）。另一方面，根据权重大小将邻居智能体的信息划分为关键、参考、背景和不可见等级别，构建定制化的提示词，从而精细调控信息可见性。

最后，**层次化的多目标奖励函数**引导控制器平衡多个目标。奖励综合了答案准确性、群体共识度、效率（token消耗）和稀疏性等多个信号，并分为每轮即时奖励和每回合终止奖励两个层次，以协调短期收益与最终目标。

通过这些设计，RUMAD能够学习任务无关的有效协调策略，在显著降低token消耗（超过80%）的同时提升推理精度，并展现出强大的零样本泛化能力。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：MMLU（多领域推理）、GSM8K（算术推理）和GPQA（研究生级科学问答）。实验设置上，RUMAD的PPO拓扑控制器仅在MMLU开发集上训练，并在所有评估中使用了由LLaMA-3.1-8B-Instruct、ChatGLM-4-9B和Deepseek-Math-7B-Instruct三种不同模型构成的六智能体池，所有模型均采用4位量化以提升效率。

对比方法包括完全连接的MAD基线、以及S-MAD（星型和环型结构）、GD和S²MAD等方法。评估指标主要是答案准确率和平均每任务令牌消耗成本。

主要结果显示，RUMAD在显著降低计算成本的同时，保持或提升了准确率。关键数据指标如下：在MMLU上，RUMAD（B=12）准确率达68%，令牌成本为11.43k/任务，相比MAD基线成本降低了81.74%；在GSM8K上，准确率达86%（B=12）或89%（B=18），成本降低86.40%或77.53%；在GPQA上，准确率达32%（B=12）或35%（B=18），成本降低66.21%或42.24%。此外，仅在MMLU上训练的RUMAD控制器在GSM8K和GPQA上展现了强大的零样本泛化能力。

论文还进行了消融实验和可扩展性分析。消融研究表明，去除智能体激活机制会导致令牌成本急剧上升（如在MMLU上从11.4k增至51.9k），而去除预算损失则会损害跨域泛化性能。可扩展性实验表明，在固定预算下增加智能体数量（如从6增至9），RUMAD能在提升准确率的同时进一步降低成本，体现了其学习策略的效率和通用性。

### Q5: 有什么可以进一步探索的点？

本文提出的RUMAD框架在动态拓扑控制和效率提升方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心控制器采用集中式PPO训练，虽然适用于小规模智能体群（6-8个），但在扩展到数百甚至数千智能体的大规模场景时，可能会面临计算瓶颈和单点故障风险。未来研究可探索去中心化或分层式的多智能体强化学习架构，例如让智能体学习局部通信策略，或引入轻量级的协调者智能体进行分层管理。

其次，RUMAD的观察机制是内容无关的，这虽然保障了中立性，但也可能丢失了语义层面的关键协调信号。未来可以研究如何在不引入偏见的前提下，设计更精细的、基于语义的观察表示，例如对智能体输出的置信度或分歧程度进行编码，从而可能实现更精准的协调控制。

此外，论文展示了出色的跨领域零样本泛化能力，但所学策略的“任务无关原则”具体是什么仍不明确。未来工作可对控制器策略进行可解释性分析，提炼出普适的辩论协调模式，并将其形式化为理论或启发式规则，这不仅能增强系统透明度，也可能启发更高效的无学习规则方法。

最后，实验主要围绕封闭式问答任务展开。未来可将框架扩展到更开放、更具创造性的任务（如代码生成、策划写作），研究动态拓扑在促进创新性共识形成中的作用，并探索将效率与创造性产出共同优化的多目标奖励设计。

### Q6: 总结一下论文的主要内容

本文提出了一种名为RUMAD的新型强化学习统一多智能体辩论框架，旨在解决现有多智能体辩论系统在同时优化准确性、共识形成和计算效率方面面临的挑战。核心问题是静态通信拓扑缺乏适应性，而基于外部大语言模型的协调可能引入特权知识，破坏辩论中立性。

RUMAD的核心方法是将动态通信拓扑控制建模为一个强化学习问题。它采用一个与内容无关的观测方案来捕捉高层辩论动态，避免接触原始推理内容，并使用一个多目标奖励函数来建模解决方案质量、内聚力和效率。通过PPO算法训练的控制器动态调整通信图中的边权重，并利用双阈值机制对智能体激活和信息可见性进行细粒度控制。

实验结果表明，RUMAD在多个基准测试上取得了显著成效，在将令牌成本降低超过80%的同时，其推理准确性仍优于单一LLM模型及多个MAD基线。更重要的是，仅在MMLU上训练的RUMAD对领域外任务展现出强大的零样本泛化能力，这表明其学习到的通信策略捕捉了与任务无关的有效多智能体协调原则。该研究为在资源受限条件下部署高效、鲁棒的多智能体推理应用提供了新思路。
