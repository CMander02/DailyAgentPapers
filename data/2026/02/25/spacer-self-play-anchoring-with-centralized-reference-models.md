---
title: "SPACeR: Self-Play Anchoring with Centralized Reference Models"
authors:
  - "Wei-Jer Chang"
  - "Akshay Rangesh"
  - "Kevin Joseph"
  - "Matthew Strong"
  - "Masayoshi Tomizuka"
  - "Yihan Hu"
  - "Wei Zhan"
date: "2025-10-20"
arxiv_id: "2510.18060"
arxiv_url: "https://arxiv.org/abs/2510.18060"
pdf_url: "https://arxiv.org/pdf/2510.18060v2"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.RO"
tags:
  - "多智能体系统"
  - "强化学习"
  - "模仿学习"
  - "自动驾驶"
  - "智能体仿真"
  - "自博弈"
  - "参考模型"
  - "策略锚定"
relevance_score: 8.5
---

# SPACeR: Self-Play Anchoring with Centralized Reference Models

## 原始摘要

Developing autonomous vehicles (AVs) requires not only safety and efficiency, but also realistic, human-like behaviors that are socially aware and predictable. Achieving this requires sim agent policies that are human-like, fast, and scalable in multi-agent settings. Recent progress in imitation learning with large diffusion-based or tokenized models has shown that behaviors can be captured directly from human driving data, producing realistic policies. However, these models are computationally expensive, slow during inference, and struggle to adapt in reactive, closed-loop scenarios. In contrast, self-play reinforcement learning (RL) scales efficiently and naturally captures multi-agent interactions, but it often relies on heuristics and reward shaping, and the resulting policies can diverge from human norms. We propose SPACeR, a framework that leverages a pretrained tokenized autoregressive motion model as a centralized reference policy to guide decentralized self-play. The reference model provides likelihood rewards and KL divergence, anchoring policies to the human driving distribution while preserving RL scalability. Evaluated on the Waymo Sim Agents Challenge, our method achieves competitive performance with imitation-learned policies while being up to 10x faster at inference and 50x smaller in parameter size than large generative models. In addition, we demonstrate in closed-loop ego planning evaluation tasks that our sim agents can effectively measure planner quality with fast and scalable traffic simulation, establishing a new paradigm for testing autonomous driving policies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动驾驶仿真中智能体策略难以同时兼顾**真实性**（即类人行为）与**反应性/可扩展性**的核心问题。研究背景是，为了安全可靠地部署自动驾驶汽车（AV），必须在仿真环境中使用能产生逼真、可预测且具备社会意识的交互行为的模拟智能体（sim agents）进行大规模闭环测试。

现有方法主要分为两类，但各有显著不足。一方面，**模仿学习**（尤其是基于大扩散模型或分词化模型的方法）能直接从人类驾驶数据中学习，生成高度真实的行为，但其模型通常计算开销巨大、推理速度慢，并且在需要快速反应的闭环交互场景中适应能力不足。另一方面，**自博弈强化学习**能高效扩展并自然捕捉多智能体交互，但其训练严重依赖启发式规则和精心设计的奖励函数，且习得的策略容易偏离人类行为规范，导致行为不真实。

因此，本文要解决的核心问题是：如何构建一种既能锚定在人类驾驶数据分布上以保证行为真实性，又能像自博弈RL一样高效、可扩展且具备强反应能力的仿真智能体策略。为此，论文提出了SPACeR框架，其核心思想是利用一个预训练的分词化自回归模型作为集中式参考策略，来指导去中心化的自博弈训练。该参考模型通过提供似然奖励和KL散度，将自博弈策略的学习“锚定”在人类驾驶分布上，从而在保留RL可扩展性与反应性的同时，确保了行为的类人真实性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：方法类和应用类。

在方法类中，相关工作包括：1）**自博弈强化学习（Self-Play RL）**，例如GIGAFlow，它通过大规模自博弈训练出鲁棒的自动驾驶策略，展现了良好的可扩展性，但其策略可能偏离人类行为规范。本文的SPACeR同样以自博弈RL为基础，但通过引入集中式参考模型来提供人类行为锚定，解决了行为偏离问题。2）**基于模仿学习的交通仿真**，近期主流方法又分为扩散模型和分词化模型（如SMART、CAT-K）。它们能直接从人类数据中学习，生成高度逼真的行为，但推理计算成本高、速度慢。本文并未直接使用这些模型进行仿真，而是将其作为预训练的参考策略，为自博弈提供奖励信号。

在应用类中，存在**对预训练模仿学习模型进行RL微调**的工作，例如使用GRPO提升真实性，或利用人类反馈进行对齐。这些工作遵循“预训练-微调”范式。本文则采用“RL优先”的路径，以自博弈为核心框架，将模仿学习模型作为奖励提供者融入其中，从而在保持RL可扩展性的同时，确保了行为的人类相似性。

### Q3: 论文如何解决这个问题？

论文通过提出SPACeR框架来解决自动驾驶仿真中智能体行为既要高效安全，又要符合人类驾驶规范的问题。其核心方法是结合模仿学习与自博弈强化学习，利用一个预训练的集中式参考模型来引导去中心化的自博弈训练，从而在保持强化学习可扩展性的同时，将策略锚定在人类驾驶分布上。

整体框架是一个多智能体强化学习系统。每个智能体拥有一个基于局部观测的策略网络π_θ。训练的关键创新在于引入了一个预训练的、基于令牌化的自回归运动模型作为集中式参考策略π_ref。该模型在真实人类驾驶数据上训练，能够基于全局场景状态和动作历史，为每个智能体在每一步生成一个动作概率分布。

主要模块和关键技术包括：
1.  **复合奖励函数**：智能体在训练时接收的奖励r_t由任务奖励r^{task}_t和人类相似度奖励r^{humanlike}组成。任务奖励鼓励到达目标、避免碰撞和保持在道路上。人类相似度奖励定义为当前动作在参考模型下的对数似然，即log π_ref(a_t|s_t)，为每一步提供密集的、鼓励拟人化行为的反馈。
2.  **分布对齐目标**：在优化目标中，除了标准的近端策略优化（PPO）目标L_PPO外，还增加了一个KL散度项D_KL(π_θ||π_ref)。这项直接鼓励学习策略的动作分布与参考模型所代表的人类驾驶分布对齐，提供了另一个密集的、分布层面的引导信号。
3.  **集中式参考模型的应用**：参考模型π_ref是集中式的，能观察到所有智能体的完整状态，这类似于师生框架中的“教师”。它为每个智能体在每一步提供独立的动作分布，从而精细地解决了多智能体强化学习中的信用分配问题，能够提供基于每个智能体、每个时间步的指导，而非稀疏的轨迹级奖励。
4.  **高效训练设计**：为确保效率，框架采用了与参考模型对齐的令牌化动作空间，避免了训练时的在线令牌化，并允许以闭式形式计算KL散度。同时，训练时只需对参考模型进行单次前向传播即可获得完整的动作分布，无需进行耗时的自回归采样，保证了训练流程的可扩展性。
5.  **目标到达处理的改进**：通过采用“目标丢弃”技术，在训练中随机地使用或不使用目标条件，并配合最终目标奖励，减少了策略对显式目标输入的依赖，避免了智能体为快速到达目标而产生不自然的加速行为。

总之，SPACeR的创新点在于创造性地将一个可提供密集、分布级信号的集中式参考模型，与去中心化的自博弈强化学习相结合。这种方法既利用了自博弈在多智能体交互中高效、可扩展的优势，又通过参考模型提供的似然奖励和KL散度约束，确保了最终策略的行为符合人类驾驶规范，实现了拟真性、效率与模型轻量化的统一。

### Q4: 论文做了哪些实验？

论文在Waymo Open Motion Dataset (WOMD)的大规模交通场景中进行了实验，使用GPUDrive模拟器，初始化1秒后模拟剩余8秒，训练使用1万场景。实验设置包括：将问题建模为部分可观测随机博弈，智能体接收50米半径内的局部观察；采用离散化的轨迹动作空间（K=200个令牌，5Hz频率）；奖励函数结合任务完成、碰撞、偏离道路和人类似性奖励；使用基于PPO的后期融合前馈网络进行训练，在单A100 GPU上训练10亿步。

使用的数据集/基准测试是Waymo Sim Agents Challenge (WOSAC)，评估指标包括复合真实感、运动学、交互、地图真实感、minADE、碰撞率、偏离道路率和吞吐量。

对比方法包括：仅使用任务奖励的PPO（自博弈）、使用KL散度正则化的HR-PPO（行为克隆参考），以及两种模仿学习基线——SMART和CAT-K（均为令牌化闭环模型）。

主要结果：SPACeR在WOSAC验证集上超越了其他自博弈方法，在所有真实感指标上表现更优。关键数据指标：复合真实感达0.741（PPO为0.710，HR-PPO为0.716），minADE降至4.101（PPO为12.725），碰撞率0.036，与模仿学习方法相比，SPACeR的碰撞率和偏离道路率更低，且在保持竞争性性能的同时，推理速度快10倍（吞吐量211.8场景/秒 vs. CAT-K的22.5场景/秒），参数规模小50倍（约6.5万参数 vs. CAT-K的320万）。在VRU（行人/自行车）实验中，SPACeR同样显著优于PPO和HR-PPO，复合真实感达0.729。此外，闭环规划器评估表明，SPACeR能更有效地惩罚不安全策略，相关性分析显示其模拟更具反应性和真实性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向主要体现在以下几个方面。首先，评估指标WOSAC存在缺陷，它过度强调对记录轨迹的复现，而非评估行为的安全性或拟人性，这可能导致对合理替代行为的错误惩罚。未来需要开发更全面的评估体系，能够区分轨迹相似性与行为质量，并更好地与强化学习目标对齐。

其次，对弱势道路使用者（VRU）的模拟尚不充分。当前指标和奖励设计主要针对车辆，缺乏对行人、自行车等特定行为的刻画，如人行道遵守、斑马线使用等。未来需设计VRU专用的评估指标和奖励函数，并构建相应的场景基础设施，以提升多类型智能体仿真的真实感。

此外，训练效率存在瓶颈。由于当前框架缺乏多GPU支持，单次训练耗时较长。未来可通过集成多GPU训练或采用更高效的后端（如PufferLib）来大幅提升训练速度。同时，内存限制也制约了场景规模与智能体数量，优化内存使用或采用分层训练策略是值得探索的方向。

结合个人见解，可能的改进思路包括：引入可解释的奖励分解机制，以更好平衡拟人性与安全性；探索元学习或课程学习策略，加速多智能体协作的收敛；以及结合世界模型进行想象规划，提升智能体在闭环场景中的适应能力。

### Q6: 总结一下论文的主要内容

本文提出SPACeR框架，旨在解决自动驾驶仿真中智能体策略需兼具人类行为真实性与计算效率的问题。现有模仿学习方法虽能生成逼真行为，但推理慢、成本高且难以适应闭环交互；而自博弈强化学习虽扩展性好，却易偏离人类驾驶规范。

SPACeR的核心贡献是引入一个预训练的令牌化自回归运动模型作为集中式参考策略，以指导去中心化的自博弈训练。该方法通过参考模型提供似然奖励和KL散度，将策略锚定在人类驾驶分布上，同时保持强化学习的可扩展性。

在Waymo仿真智能体挑战上的评估表明，该方法性能与模仿学习策略相当，但推理速度快10倍，模型参数规模小50倍。此外，闭环自我规划评估验证了该框架能通过快速、可扩展的交通仿真有效衡量规划器质量，为自动驾驶策略测试建立了新范式。
