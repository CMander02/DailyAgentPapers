---
title: "PACE: Procedural Abstractions for Communicating Efficiently"
authors:
  - "Jonathan D. Thomas"
  - "Andrea Silvi"
  - "Devdatt Dubhashi"
  - "Moa Johansson"
date: "2024-09-30"
arxiv_id: "2409.20120"
arxiv_url: "https://arxiv.org/abs/2409.20120"
pdf_url: "https://arxiv.org/pdf/2409.20120v4"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "Agent通信"
  - "抽象与推理"
  - "协作任务"
  - "神经符号方法"
  - "强化学习"
  - "语言涌现"
  - "库学习"
relevance_score: 7.5
---

# PACE: Procedural Abstractions for Communicating Efficiently

## 原始摘要

A central but unresolved aspect of problem-solving in AI is the capability to introduce and use abstractions, something humans excel at. Work in cognitive science has demonstrated that humans tend towards higher levels of abstraction when engaged in collaborative task-oriented communication, enabling gradually shorter and more information-efficient utterances. Several computational methods have attempted to replicate this phenomenon, but all make unrealistic simplifying assumptions about how abstractions are introduced and learned. Our method, Procedural Abstractions for Communicating Efficiently (PACE), overcomes these limitations through a neuro-symbolic approach. On the symbolic side, we draw on work from library learning for proposing abstractions. We combine this with neural methods for communication and reinforcement learning, via a novel use of bandit algorithms for controlling the exploration and exploitation trade-off in introducing new abstractions. PACE exhibits similar tendencies to humans on a collaborative construction task from the cognitive science literature, where one agent (the architect) instructs the other (the builder) to reconstruct a scene of block-buildings. PACE results in the emergence of an efficient language as a by-product of collaborative communication. Beyond providing mechanistic insights into human communication, our work serves as a first step to providing conversational agents with the ability for human-like communicative abstractions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能在协作问题解决中如何像人类一样动态地引入和使用抽象概念的核心难题。研究背景源于认知科学发现：人类在协作任务中会自然发展出更高层次的抽象表达，从而使沟通更简洁高效。现有计算方法虽然尝试模拟这一现象，但通常对抽象概念的引入和学习方式做了不切实际的简化假设，例如预设抽象库或固定学习时机，未能充分捕捉语言在协作中动态演化的本质。

本文的核心问题是：如何在多智能体协作任务中，设计一个计算框架，使智能体能够通过重复互动自主地发现、引入并学习使用程序性抽象概念，从而发展出一种高效、简洁的共享语言，以优化沟通效率。为此，论文提出了PACE这一神经符号方法，它结合了符号侧的库学习（用于从常见动作序列中提出抽象）、神经侧的涌现通信和强化学习，并创新性地利用多臂赌博机算法来权衡引入新抽象（探索）与使用现有表达（利用）之间的关系。该方法在经典的“建筑师-建造者”协作搭建任务中进行了验证，旨在揭示高效通信压力如何驱动抽象的形成与演化，并为构建具备类人抽象沟通能力的对话智能体迈出第一步。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及方法类和应用类，可归纳为以下几个方面：

在方法类研究中，相关工作主要包括基于符号推理和基于深度强化学习的两种路径。一方面，**Bayesian模型**结合了程序抽象库学习与社会推理通信，能捕捉人类通信趋势，但其假设了指令到动作的预定义映射，并人为限制语言规模，未实现动态扩展。另一方面，**深度强化学习方法**将交互过度简化，假设建造者能即时理解抽象概念，从而将多智能体问题简化为单智能体框架，削弱了高效通信的压力。

在应用类研究中，**涌现通信**领域被广泛用于模拟人类语言现象，如组合性、群体效应和语义范畴命名等。然而，在认知科学中的“建筑师-建造者”协作建造任务中，现有方法难以处理多轮交互和稀疏奖励的挑战。

本文提出的PACE方法通过神经符号途径整合了上述工作的优势：在符号层面借鉴库学习来提出抽象，在神经层面结合通信与强化学习，并创新性地利用多臂赌博机算法平衡新抽象的探索与利用。与Bayesian模型相比，PACE允许智能体通过交互动态学习抽象，无需预定义语义；与深度强化学习方法相比，它保持了真实的多智能体协作框架，使通信效率压力自然限制语言规模，从而更贴近人类抽象通信的机制。

### Q3: 论文如何解决这个问题？

论文通过一个名为PACE的神经符号混合方法来解决协作任务中高效抽象与通信的问题。其核心是设计了一个三阶段循环框架：选择、通信和抽象。在架构上，系统包含两个智能体（建筑师和建造者）以及三个关键模块：基于库学习的抽象生成模块、基于神经网络的通信模块，以及利用多臂老虎机进行探索与利用权衡的程序选择模块。

具体而言，建筑师首先从符号程序表中为当前目标场景选择一个程序。初始时每个场景对应一个基础程序。通信阶段，建筑师和建造者通过可微分的神经通信策略进行交互：建筑师将程序中的每个指令编码为离散消息，建造者根据当前状态和消息预测下一状态，两者通过最小化状态重建误差进行端到端联合训练。经过多轮通信后，系统进入抽象阶段：建筑师运用改进的库学习算法，从已有程序中识别频繁出现的子序列作为候选抽象，并依据最小描述长度原则选择能最大程度缩短程序描述的新抽象，将其加入符号库。此后，建筑师对同一场景将拥有多个不同长度的程序可选。

创新点主要体现在：1）将符号库学习与神经通信、强化学习相结合，使抽象能力从协作中自然涌现；2）创新性地将程序选择建模为上下文组合多臂老虎机问题，通过Q值乘积评估程序质量，并采用ε-贪婪策略平衡对新旧程序的探索与利用；3）设计了包含正信号偏置的损失函数，鼓励生成有意义的消息；4）去除了抽象库大小的显式上限，使系统能持续学习。实验表明，该方法能像人类一样在协作中逐步发展出词汇精简、表达高效的语言。

### Q4: 论文做了哪些实验？

论文实验基于认知科学文献中的协作构建任务，模拟人类在协作沟通中逐步形成高效抽象语言的过程。实验设置涉及两个智能体：一个作为“建筑师”发出指令，另一个作为“建造者”根据指令重建积木场景。通过多轮交互，智能体学习引入和使用过程抽象来优化通信效率。

数据集/基准测试采用积木建筑场景的协作任务，具体任务细节未在摘要中明确，但参考了认知科学中常用的实验范式。对比方法包括以往尝试模拟人类抽象引入机制的计算方法，这些方法通常对抽象的学习和引入做了不现实的简化假设。

主要结果方面，PACE 方法通过神经符号结合的方式，利用符号侧的库学习提出抽象，并结合神经方法进行通信和强化学习，通过新颖的 bandit 算法控制探索与利用的权衡。实验显示，PACE 在协作任务中表现出与人类相似的倾向，即随着沟通进行，话语逐渐缩短且信息效率提升，从而自然涌现出一种高效语言。关键数据指标包括通信效率的提升（如指令长度缩短）和任务完成准确率，但摘要未提供具体数值。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其研究场景较为单一，目前仅应用于“建筑师-建造者”积木协作任务，且假设每个目标状态都存在初始程序集，这在更复杂的开放环境（如ARC抽象推理语料库）中可能难以实现。此外，PACE侧重于指令性抽象，尚未深入探讨如何将其扩展到自然语言的泛化理解与生成，也未从信息论角度系统分析所涌现语言在程序长度与词汇量之间的帕累托最优权衡。

未来研究方向可沿以下路径拓展：一是将PACE框架迁移至更多协作领域（如多步骤规划、机器人指令传递），验证其抽象机制的泛化能力；二是结合大语言模型（LLMs）研究对话动态，探索如何让LLMs理解并运用类似的过程性抽象进行高效沟通；三是从信息压缩与传输效率视角，量化分析抽象语言的演化边界，建立其与人类语言效率理论的联系。可能的改进思路包括引入元学习机制，使智能体能在未知环境中自主构建初始程序库，并融合语义解析技术，将过程性抽象与自然语言指令进行双向映射，从而增强人机协作的灵活性与可扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PACE（Procedural Abstractions for Communicating Efficiently）的神经符号方法，旨在解决AI在协作问题解决中如何像人类一样引入和使用抽象的核心挑战。问题定义聚焦于多智能体在面向任务的通信中，如何通过抽象逐步发展出更高效、更简短的语言表达，以提升沟通效率。

方法概述上，PACE结合了符号方法与神经方法：符号层面借鉴了库学习技术来提出抽象概念；神经层面则利用强化学习和通信机制，并创新性地采用多臂老虎机算法来平衡探索新抽象与利用现有抽象之间的权衡。该方法在一个认知科学文献中的协作搭建任务（建筑师指导建造者重建积木场景）上进行了验证。

主要结论表明，PACE能够复现人类在协作沟通中倾向于更高层次抽象的行为，并作为协作的副产品，自然涌现出一种高效的语言。其核心贡献在于突破了以往方法在抽象引入和学习方面的简化假设，为理解人类通信机制提供了计算模型，同时为对话智能体实现类人的抽象通信能力迈出了重要一步。
