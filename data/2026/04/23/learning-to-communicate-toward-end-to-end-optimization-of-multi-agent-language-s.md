---
title: "Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems"
authors:
  - "Ye Yu"
  - "Heming Liu"
  - "Haibo Jin"
  - "Xiaopeng Yuan"
  - "Peng Kuang"
  - "Haohan Wang"
date: "2026-04-23"
arxiv_id: "2604.21794"
arxiv_url: "https://arxiv.org/abs/2604.21794"
pdf_url: "https://arxiv.org/pdf/2604.21794v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "多智能体通信"
  - "潜在通信"
  - "端到端优化"
  - "参数高效训练"
  - "推理增强"
  - "LLM Agent"
  - "DiffMAS"
  - "数学推理"
  - "代码生成"
  - "心智理论"
relevance_score: 9.5
---

# Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems

## 原始摘要

Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体语言系统中通信机制不可学习、无法与推理过程联合优化的问题。研究背景是，基于大型语言模型的多智能体系统在复杂推理任务（如数学、编程、常识推理）上表现出色，其有效性通常归因于系统结构、角色分配以及智能体间的通信。现有方法的不足在于，大多数工作专注于优化智能体角色和工作流设计，却将智能体间的通信视为固定接口（如离散的自然语言消息）。这种离散消息传递方式在智能体之间创建了优化边界，导致梯度无法跨智能体传播，使得中间推理状态的表征和解读效率受限，无法根据任务动态调整。核心问题因此是：如何让智能体间的通信成为可学习的、可微分的组件，实现通信与多智能体推理的端到端联合优化。本文提出的 DiffMAS 框架，通过将键值缓存作为潜在的连续通信信道，并采用参数高效的监督训练方法，使智能体能够共同学习如何编码和解读交互信息，从而提升推理准确性和解码稳定性。

### Q2: 有哪些相关研究？

相关工作可分为三类：多智能体系统设计、隐式推理方法、以及潜在通信机制。

在多智能体系统设计方面，现有工作主要关注角色工程、自动化工作流构建和架构搜索，尽管增强了系统能力，但普遍依赖自然语言作为固定通信接口，将内部推理状态序列化为离散token，限制了信息保真度。本文与之不同，将通信作为可学习组件，通过联合优化推理与通信提升性能。

在隐式推理领域，如Implicit CoT蒸馏、Quiet-STaR等研究探索了将推理行为内化为隐藏表示，减少对显式文本的依赖。本文将这些思想扩展到多智能体场景，但不仅限于单模型推理，而是通过智能体间潜在轨迹的联合训练实现通信优化。

在潜在通信机制方面，已有工作通过共享KV缓存或隐藏状态实现比文本更丰富的交互，但多为免训练交换或模型对齐。本文提出的DiffMAS框架首次将潜在通信视为可优化组件，通过参数高效监督训练同步学习编码与解码策略，使通信能够随推理任务自适应调整。实验表明，这种端到端优化在AIME24等基准上显著优于文本基线和现有潜在通信方法。

### Q3: 论文如何解决这个问题？

DiffMAS通过将多智能体系统中的隐式通信建模为可学习的连续计算过程，实现端到端优化。其核心架构由三个关键组件构成：

1. **延迟轨迹表示**：将智能体间通信定义为KV缓存片段组成的连续潜变量块序列。每个智能体执行T个微分计算微步，每步发射一个d维潜变量块，通过拼接方式累加至共享轨迹，形成维度递增的轨迹空间T_j=Z^{jT}。这种设计避免了传统覆盖式通信中固定维度载体导致的信号衰减。

2. **可微分阶段算子**：每个智能体对应一个阶段算子A_θ^(j)，由初始化函数η_θ、发射函数g_θ和残差更新函数f_θ构成。初始化函数基于输入x、阶段提示p_j和先前轨迹初始化内部状态；发射函数生成新增潜变量块；残差更新函数通过f_θ维持状态演化。所有函数对参数θ可微，使得损失函数梯度能通过所有阶段和微步反向传播。

3. **参数高效训练**：基于预训练Transformer实现上述函数，仅通过LoRA更新少量参数（<5%），保持骨干网络冻结。训练采用监督负对数似然损失，梯度通过拼接式通信接口传播时不会引入深度相关的衰减因子（相比覆盖式通信的ρ^{K-j}指数衰减），确保所有中间智能体获得可比拟的梯度信号。

创新点体现在：(1) 将隐式通信纳入端到端优化，打破传统固定协议限制；(2) 利用连续潜变量保留丰富推理信号，避免离散化压缩；(3) 证明拼接式通信接口的梯度保真度特性，实现各阶段均衡优化。这种设计在数学推理（AIME 24 26.7%）、科学QA（GPQA 20.2%）等任务上取得显著提升。

### Q4: 论文做了哪些实验？

论文在数学推理、科学问答、代码生成和常识推理四个任务组上进行了全面实验。数据集包括AIME 2024/2025（数学竞赛）、GPQA-Diamond（科学QA）、HumanEval+和MBPP+（代码生成）、OpenBookQA（常识推理）。对比方法包括单模型推理、基于文本的多智能体系统（TextMAS）、无训练潜通信（LatentMAS）以及可训练潜通信方法C2C。模型涵盖Qwen3-4B/8B/14B、Mistral3-8B和DeepSeek-R1-Distill-Qwen-32B。训练采用参数高效LoRA微调，使用少量领域数据（如数学用210样本、代码用50样本）。主要结果：DiffMAS在所有基准上一致最优，例如在Qwen3-8B上AIME24达到76.7%（单模型50%），GPQA-Diamond达到60.1%（单模型39.9%）；在Qwen3-14B上HumanEval+达87.7%、MBPP+达77.2%；OpenBookQA上Qwen3-4B达83.2%。C2C在困难推理任务上表现较差，因训练数据不匹配。DiffMAS在解码稳定性上也优于基线。

### Q5: 有什么可以进一步探索的点？

**进一步探索点：**

1. **通信步数敏感性问题**：论文发现10步通信最优，增加步数反而性能下降。未来可探索动态调整通信步数的机制，让模型自动判断何时停止通信，避免冗余噪声积累。

2. **模型扩展性与架构设计**：当前仅在小模型上验证，大型模型（如GPT-4级别）的KV缓存通信效率、显存占用及跨Agent位置一致性仍是开放问题。可探索稀疏KV注意力或压缩隐空间表示。

3. **任务泛化边界**：消融实验显示分布外场景中通信学习优势更明显，但未测试完全脱离训练分布的零样本迁移能力。可引入元学习或在线适应，使通信协议能快速适配新任务。

4. **可解释性与通信协议分析**：KV缓存作为隐式通信接口缺乏人类可读性。未来可尝试将部分KV状态映射为自然语言摘要，或在训练中加入正则项约束通信内容的结构化程度。

5. **多轮交互效率**：当前所有Agent共享连续KV轨迹，但长轨迹中存在信息冗余。可引入注意力窗口或遗忘机制，筛选关键历史信息进行传递，降低计算开销。

### Q6: 总结一下论文的主要内容

本文提出了一种名为DiffMAS的训练框架，旨在解决多智能体语言系统中智能体间通信效率低下的问题。现有基于大语言模型的多智能体系统大多将通信视为固定接口，简单依赖文本交互，未能联合优化通信与推理过程。DiffMAS将潜在通信（如键值缓存中的内部表示）作为可学习组件，通过参数高效的监督训练对多智能体系统的完整潜在交互轨迹进行优化，使智能体能够协同学习信息的编码与解读方式。在数学推理、科学问答、代码生成和常识推理等基准测试中，DiffMAS相比单智能体推理、文本交互多智能体系统及先前的潜在通信方法，均展现出更高的推理准确率和解码稳定性，例如在AIME24上达到26.7%，在GPQA-Diamond上达到20.2%。该工作将潜在通信确立为多智能体系统优化的关键目标，为未来实现端到端可微分交互的多智能体系统奠定了基础。
