---
title: "Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination"
authors:
  - "Rakshit Trivedi"
  - "Kartik Sharma"
  - "David C Parkes"
date: "2026-02-24"
arxiv_id: "2602.20517"
arxiv_url: "https://arxiv.org/abs/2602.20517"
pdf_url: "https://arxiv.org/pdf/2602.20517v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "模仿学习"
  - "人机协作"
  - "行为多样性"
  - "语言引导"
  - "推理"
  - "条件生成模型"
  - "视觉语言模型"
relevance_score: 8.5
---

# Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination

## 原始摘要

Effective human-AI coordination requires artificial agents capable of exhibiting and responding to human-like behaviors while adapting to changing contexts. Imitation learning has emerged as one of the prominent approaches to build such agents by training them to mimic human-demonstrated behaviors. However, current methods struggle to capture the inherent diversity and non-Markovian nature of human behavior and lack the ability to steer behavior at inference time. Drawing inspiration from the theory of human cognitive processes, where inner speech guides action selection before execution, we propose MIMIC (Modeling Inner Motivations for Imitation and Control), a framework that uses language as an internal representation of behavioral intent. MIMIC employs the novel use of vision-language models as linguistic scaffolding to train a conditional variational autoencoder capable of generating inner speech from observations. A diffusion-based behavior cloning policy then selects actions conditioned on current observations and the generated inner speech. MIMIC enables fine-grained steering of behavior at inference time by conditioning the agent on behavior-specific speech. Experiments across robotic manipulation tasks and human-AI collaboration games demonstrate that MIMIC significantly enhances both behavior diversity and fidelity to human demonstrations while enabling nuanced behavioral steering without training on additional demonstrations. We open source our code and provide pre-trained MIMIC agents and qualitative demos at: https://mimic-research.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人机协作中智能体行为模仿的多样性与可控性问题。研究背景是，为了实现有效的人机协作，AI智能体需要能够模仿人类多样化的行为模式，并适应动态环境。模仿学习是训练此类智能体的主流方法，但现有方法（尤其是行为克隆）存在明显不足：它们难以捕捉人类行为固有的多模态分布和非马尔可夫特性，并且在推理时缺乏对生成行为的细粒度引导和控制能力，通常仅限于目标条件生成，灵活性有限。

本文的核心问题是：如何让模仿学习智能体不仅能更真实、多样地复现人类行为，还能在推理时接受外部引导，以可控的方式生成符合特定意图的新行为。受人类认知过程中“内部语言”（inner speech）在行动选择前起引导作用的理论启发，论文提出了MIMIC框架。该框架将自然语言作为行为意图的内部表征，通过视觉语言模型提供语言支架，训练一个条件变分自编码器从观察中生成内部语言，再使用基于扩散模型的行为克隆策略，根据当前观察和生成的内部语言选择动作。这样，在推理时可通过输入描述特定行为的语言来精细引导智能体，从而实现无需额外演示数据的行为操控。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：模仿学习方法、语言交互的模仿学习，以及认知过程的AI建模方法。

在模仿学习方法方面，传统的行为克隆（BC）通过监督学习从状态-动作对中学习策略，但难以捕捉人类行为的多样性和非马尔可夫性。本文提出的MIMIC框架则通过引入内语言作为潜在行为意图表示，并结合条件变分自编码器（CVAE）和扩散模型，增强了行为多样性和推理时的可操控性。

在语言交互的模仿学习方面，相关工作包括“思想克隆”（TC），它直接模仿人类标注的思维步骤，但严重依赖每一步的思维注释，且在无目标任务条件下性能显著下降。另有研究使用外部语音通过动作重排序来引导智能体，但其机制仍外在于智能体。还有工作将“智能体内语音”用作半监督标注，作为BC的辅助监督以实现零样本泛化，但其语言模型是冻结的。相比之下，MIMIC将内语言视为在线生成的、用于调节策略的潜在中介，实现了无需额外演示的可操控、多样化模仿。

在认知过程的AI建模方面，相关研究包括“自目的AI”，它将语言内化用于自我导向学习，但侧重于目标生成而非行为多样性。另有工作利用大语言模型模拟行动前的推理链，但其过程是序列化、确定性的，不同于本文所依据的维果茨基理论中内语言的随机、并行处理特性。还有研究将自然语言作为强化学习的潜在空间以构建行为层次，但重点在于任务分解而非生成行为多样性。MIMIC独特地将内语言的随机性与模仿学习结合，无需显式语言监督即可捕捉人类行为变化。

### Q3: 论文如何解决这个问题？

论文提出的MIMIC框架通过引入“内部言语”作为行为意图的潜在表征，来解决模仿学习中难以捕捉人类行为多样性和非马尔可夫性、且无法在推理时进行行为引导的问题。其核心方法是将人类认知理论中的“内部言语”概念计算化，构建了一个由内部言语生成器和基于内部言语的行为克隆策略组成的双层架构。

整体框架包含两个主要模块：**基于条件变分自编码器的内部言语生成器**和**基于扩散模型的行为克隆策略**。内部言语生成器（CVAE）负责从观察到的行为历史中，生成压缩的、语义丰富的语言表征（即内部言语）。它利用预训练的视觉语言模型（VLM）提供的语言描述作为“脚手架”进行训练，学习将视觉行为序列映射到描述性语言嵌入，并通过变分瓶颈实现语义压缩，捕获行为的本质。行为克隆策略（DDPM-T）是一个基于Transformer的扩散模型，它以当前环境状态和生成的内部言语为条件，通过去噪过程生成具体的动作。这种设计使得策略能够根据不同的内部言语，在相同状态下产生多样化的行为。

关键技术体现在三个方面：1. **理论形式化**：将内部言语形式化为一个随机中介过程，其结构特性（述谓性、语义压缩、时序调节动力学）通过数学模型（如关系编码、信息瓶颈、非马尔可夫历史条件）来刻画，并指导了架构设计。2. **架构创新**：使用Transformer的注意力机制实现述谓性处理，关注状态、内部言语和动作历史之间的关系而非实体；使用CVAE的变分目标直接实现信息瓶颈，进行语义压缩；通过周期性的内部言语生成（每W步更新一次）来实现时序调节，模拟间歇性的战略思考过程。3. **训练与引导机制**：采用分类器无关引导技术训练扩散策略，使其能灵活地在有/无内部言语条件下工作。在推理时，通过为用户提供指定内部言语或让代理自行生成内部言语的能力，实现了对行为的细粒度引导，无需额外的演示数据。

创新点在于首次将内部言语理论系统地计算化并融入模仿学习框架，利用VLM作为无需人工标注的语言脚手架，以及结合CVAE与扩散模型来实现多样、可控且高保真度的行为模仿。

### Q4: 论文做了哪些实验？

论文在机器人操作任务和人类-AI协作游戏两类环境中进行了实验。实验设置方面，MIMIC框架包含一个基于CVAE的内部语音生成器和一个基于扩散模型的行为克隆策略，使用Adam优化器，并对不同数据集调整学习率等超参数。

数据集和基准测试包括：1）机器人控制任务，使用D3IL基准中的Aligning、Sorting和Stacking环境，评估时考虑基于视觉和基于特征的观测；2）人类-AI协作任务，使用Overcooked数据集，包含Cramped room、Coordination ring和Asymmetric advantages三种布局，通过模拟100局游戏进行评估。

对比方法以基于DDPM-T架构的最先进行为克隆方法（BC）作为主要基线。论文评估了MIMIC的两个变体：追求最高成功率的MIMIC-S和追求最高行为熵的MIMIC-E。

主要结果和关键指标如下：在D3IL基准测试中，MIMIC在生成类人行为的多样性和成功率上均优于BC。例如，在Aligning任务中，MIMIC-S的成功率达到0.8021（BC为0.6645），终点距离降至0.0664（BC为0.1105），状态Wasserstein距离大幅降低至0.0459（BC为0.6961）。在Stacking任务中，MIMIC-E在堆叠1个和2个盒子时取得了最佳成功率和熵。在Overcooked协作任务中，MIMIC与人类代理协作获得的集体奖励显著高于BC，在Cramped room布局中奖励达到151.8（BC为115.8），提升显著。这些结果表明MIMIC能够以高保真度模仿多样的人类行为，并有效提升人机协作性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的MIMIC框架在利用内部语音指导行为模仿方面具有创新性，但仍存在一些局限性和值得深入探索的方向。首先，其内部语音的生成依赖于预训练的视觉-语言模型（VLMs），这可能导致生成的语言描述受限于VLM的训练数据分布，在复杂或未见过的场景中可能产生不准确或无关的内部指导。未来研究可探索更自主或与策略共同优化的语言生成模块，以减少对外部模型的依赖。

其次，当前方法在行为“引导”方面主要依赖于手动指定的语言指令，这在实际人机协作中可能不够灵活。未来的工作可以研究如何让AI智能体主动生成或请求澄清指令，实现更动态的双向沟通。例如，智能体可以基于环境不确定性主动提问，或通过多轮对话细化行为意图。

此外，论文的实验集中在相对结构化的任务（如机器人操作和协作游戏），未来可测试在更开放、长期或多人交互环境中的有效性。另一个方向是探索内部语音与其他认知表征（如目标、情感状态）的结合，以产生更丰富、更拟人化的行为谱系。最后，评估方面除了多样性和保真度，还可引入人类主观评价，直接衡量协作体验的自然度和效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MIMIC的框架，旨在通过模仿学习提升人机协作中AI代理的行为多样性和可控性。核心问题是现有方法难以捕捉人类行为的多样性和非马尔可夫特性，且无法在推理时灵活引导行为。受人类认知过程中内在语言指导行动选择的启发，MIMIC将语言作为行为意图的内部表征，创新性地利用视觉语言模型作为语言支架，训练条件变分自编码器从观察中生成内在语言，再通过基于扩散模型的行为克隆策略，根据当前观察和生成的内在语言选择动作。该方法允许在推理时通过特定行为语言精细调控代理行为。实验在机器人操作任务和人机协作游戏中进行，结果表明MIMIC显著提高了行为多样性和对人类演示的保真度，且无需额外演示训练即可实现细致的行为引导，为人机协调提供了更灵活、拟人化的解决方案。
