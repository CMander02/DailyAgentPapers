---
title: "Dynamic Mixture of Latent Memories for Self-Evolving Agents"
authors:
  - "Dianzhi Yu"
  - "Vireo Zhang"
  - "Hongru Wang"
  - "Yanyu Chen"
  - "Minda Hu"
  - "Wanghan Xu"
  - "Siki Chen"
  - "Philip Torr"
  - "Zhenfei Yin"
  - "Irwin King"
date: "2026-05-21"
arxiv_id: "2605.21951"
arxiv_url: "https://arxiv.org/abs/2605.21951"
pdf_url: "https://arxiv.org/pdf/2605.21951v1"
categories:
  - "cs.LG"
tags:
  - "Agent记忆"
  - "自我演化代理"
  - "持续学习"
  - "混合专家模型"
  - "潜在记忆"
relevance_score: 7.5
---

# Dynamic Mixture of Latent Memories for Self-Evolving Agents

## 原始摘要

Achieving self-evolution in intelligent agents requires the continual accumulation of new knowledge across changing task sequences without forgetting previously acquired abilities. Existing approaches either internalize knowledge by updating model parameters, which induces catastrophic forgetting, or rely on external memory, which fails to genuinely enhance the model's intrinsic capabilities. We propose MoLEM, a generative mixture of latent memory framework based on a dynamic mixture-of-experts (MoE). We treat multiple experts as independent carriers to generate memory. A router selects and weights experts through key-query matching, and the aggregated latent memory is injected into the reasoning process. The base model for reasoning remains entirely frozen, with all experiential knowledge internalized into the additional modules, avoiding catastrophic forgetting. For continual learning, each training stage is paired with a lightweight autoencoder that selects the appropriate routing group at inference, and inputs that match no stage fall back to the pretrained model. Experiments train the framework on continual-learning sequences spanning math, science, and code domains. After training, we evaluate the framework on the corresponding test sets to measure task learning and competence preservation across continual adaptation stages. After the full continual-learning sequence, our method improves the average accuracy by 10.40% over the Vanilla pretrained baseline, while none of the competing methods consistently exceed this baseline across different training orders.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决智能体在持续学习场景中的自我进化问题。现有方法主要分为两类：参数记忆通过更新模型参数（如SFT或GRPO）内化知识，但会导致灾难性遗忘，破坏先前任务和预训练能力；而基于检索的外部记忆虽不修改参数，但仅通过上下文工程调用模型既有能力，无法真正增强模型内在技能。两种方式各有缺陷。

本文提出的MoLEM框架针对三个核心不足：一是传统静态架构无法动态扩展容量以适应新领域或任务难度；二是现有潜在记忆方法虽然不更新骨干网络，但记忆模块的参数在不同任务间复用时会被覆盖，导致遗忘；三是缺乏灵活的模块化集成能力，无法像人脑那样动态组合不同认知功能。

因此，核心研究问题是如何设计一种灵活、可扩展的智能体认知架构，使其在面对连续变化的任务序列时，既能动态扩展容量以获取新知识，又能避免遗忘已学能力。具体而言，论文通过动态混合专家系统，将多个专家作为独立记忆载体，利用路由器进行键值匹配和加权，并将聚合的潜在记忆注入推理过程，同时采用阶段自编码器实现无任务标识的域感知路由，以在持续学习中平衡新任务学习与旧能力保持。

### Q2: 有哪些相关研究？

**方法类相关研究**：参数化方法（如SFT、GRPO、DPO）通过直接微调LLM参数内化知识，其中RLVMR、MEM1、Memory-R1引入推理步骤或记忆机制，但仍依赖参数更新，存在灾难性遗忘问题。本文MoLEM通过冻结基座模型、只训练额外模块来避免这一问题。检索式记忆方法（如MemoryBank、Memento、ExpeL、A-Mem、ReasoningBank）维护外部记忆系统避免遗忘，但本质是上下文工程，无法提升模型内在能力。MoLEM的潜在记忆机制则直接将知识注入推理过程。

**应用类相关研究**：MemGen、SoftCoT、Coconut等潜在记忆方法使用连续向量承载记忆而不修改原始参数。但MoLEM指出这些方法未考虑持续学习场景下的架构可扩展性，而这正是其核心创新——通过动态MoE和轻量级自动编码器实现持续学习各阶段的路由选择与回退机制。

**评测类相关研究**：本文在数学、科学、代码领域的持续学习序列上评测，关注任务学习与能力保持。比较方法均无法在不同训练顺序下持续超越预训练基线，而MoLEM提升平均准确率10.40%。

### Q3: 论文如何解决这个问题？

MoLEM 提出了一种基于动态混合专家（MoE）的生成式潜记忆框架，核心思路是将经验知识存储于额外模块中，而基础推理模型保持完全冻结。整体框架由三个核心模块构成：**专家模块**、**路由器模块**和**阶段自编码器**。

具体而言，每个专家都是一个独立的 LoRA 适配器，附着在冻结的基础推理模型上。当输入经过推理模型时，激活的专家会生成一个候选的潜记忆矩阵。路由器同样是一个 LoRA 适配器，它通过提取当前推理状态的查询向量，与每个专家维护的可学习键向量进行余弦相似度匹配，计算得到各专家的权重。然后，路由器根据这些权重对所有专家生成的候选潜记忆进行加权聚合，形成一个最终的混合潜记忆，并将其注入回推理模型的隐状态中，影响后续的生成过程。

为支持持续学习，论文设计了**分阶段专家招募**策略。每进入一个新领域，当前阶段的专家和路由器参数被冻结，并招募一组全新的、随机初始化的专家和路由器进行训练，确保不同领域的知识被隔离在独立的参数子空间中。在推理时，系统面临无任务标签的挑战。为此，每个阶段配备了一个轻量级自编码器，它专门训练以重构该阶段输入特征的分布。对于任意输入，系统先通过冻结推理模型获得其提示结束特征，然后将其送入所有已见阶段的自编码器中，选择重构误差最小且低于该阶段阈值的自编码器所对应的路由组。若所有误差均超阈值，则认为输入为分布外样本，直接回退到预训练模型。这种设计在无任务标识的情况下实现了有效的领域感知路由，同时避免了灾难性遗忘。

### Q4: 论文做了哪些实验？

我们进行了三项实验。**实验设置**：使用Qwen3-4B-Instruct-2507作为冻结的基础推理模型，在Math→Science→Code的默认顺序下进行持续学习训练（另两种顺序见附录）。**数据集/基准**：数学（Nemotron MATH）、科学（Nemotron Science）、代码（KodCode）三个领域的测试集。对比方法包括：Vanilla（无微调预训练模型）、SFT（顺序全参数微调）、MemGen（潜在记忆基线）、ExpeL（外部记忆方法）。**主要结果**：完整三阶段训练后，我们的方法平均准确率达73.93%，超过Vanilla基线（63.53%）10.40%，SFT（34.40%）39.53%，最强对比方法MemGen（63.47%）10.46%。在数学和代码任务上同时取得最高分（59.20%和74.20%）。遗忘、后向迁移和前向迁移均为零。我们还进行了消融实验：1）MoE（多专家vs单专家）：单阶段下多专家提升数学准确率（53.80→59.80），但共享路由组时仍会出现遗忘；2）隔离路由组（各阶段独立vs共享）：只有完全隔离的路由与专家配置（√/√）才能在所有阶段保持零遗忘和最高平均分（73.93%），共享配置会导致灾难性遗忘（如共享多专家变体最终遗忘率达30.50）。

### Q5: 有什么可以进一步探索的点？

论文虽然提出了创新的动态记忆融合框架，但仍存在若干可深入探索的方向。首先，MoLEM 依赖预定义的训练阶段划分（每个阶段绑定一个自编码器），这在实际应用中可能难以预知任务边界，未来可探索**无阶段标签的在线持续学习**，让路由器自主发现任务切换点。其次，当前实验仅针对数学、科学、代码等结构化领域，**缺乏对开放域、长文本或对话生成任务的验证**，这类任务对记忆的复杂性和泛化性要求更高。未来可改进路由机制，引入**可学习的知识遗忘曲线**，根据时间间隔或任务相关性动态调整专家权重。此外，当前路由基于简单的 key-query 匹配，可引入**注意力增强的图结构**来捕捉专家间的协作关系，或通过**元学习**优化初始路由策略，减少对人工调参的依赖。最后，可探索**记忆压缩与冗余消除**机制，防止长期累积的模块指数级增长。

### Q6: 总结一下论文的主要内容

该论文提出MoLEM框架，旨在解决智能体在持续任务序列中自演化时面临的灾难性遗忘与能力固化问题。现有方法要么通过参数更新内化知识导致遗忘，要么依赖外部记忆而无法增强模型内在能力。MoLEM基于动态混合专家架构，将多个专家作为独立记忆载体，通过键值查询路由选择并加权专家，聚合后的潜在记忆注入推理过程。推理基础模型完全冻结，所有经验知识内化到额外模块中，避免灾难性遗忘。针对持续学习，每个训练阶段配备轻量级自编码器，推理时选择重建误差最小的路由组，不匹配任何阶段的输入回退到预训练模型。在数学、科学和代码领域的持续学习序列上实验，完整序列后该方法平均准确率比原始预训练基线提升10.40%，且其他竞争方法无法在不同训练顺序下始终超越该基线。这一框架为构建持续演化的智能体提供了新范式。
