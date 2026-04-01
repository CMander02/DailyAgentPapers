---
title: "MemFactory: Unified Inference & Training Framework for Agent Memory"
authors:
  - "Ziliang Guo"
  - "Ziheng Li"
  - "Zhiyu Li"
date: "2026-03-31"
arxiv_id: "2603.29493"
arxiv_url: "https://arxiv.org/abs/2603.29493"
pdf_url: "https://arxiv.org/pdf/2603.29493v1"
github_url: "https://github.com/Valsure/MemFactory"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent_Memory"
  - "Training_Framework"
  - "Inference_Framework"
  - "Reinforcement_Learning"
  - "Modular_Architecture"
  - "Evaluation"
relevance_score: 9.0
---

# MemFactory: Unified Inference & Training Framework for Agent Memory

## 原始摘要

Memory-augmented Large Language Models (LLMs) are essential for developing capable, long-term AI agents. Recently, applying Reinforcement Learning (RL) to optimize memory operations, such as extraction, updating, and retrieval, has emerged as a highly promising research direction. However, existing implementations remain highly fragmented and task-specific, lacking a unified infrastructure to streamline the integration, training, and evaluation of these complex pipelines. To address this gap, we present MemFactory, the first unified, highly modular training and inference framework specifically designed for memory-augmented agents. Inspired by the success of unified fine-tuning frameworks like LLaMA-Factory, MemFactory abstracts the memory lifecycle into atomic, plug-and-play components, enabling researchers to seamlessly construct custom memory agents via a "Lego-like" architecture. Furthermore, the framework natively integrates Group Relative Policy Optimization (GRPO) to fine-tune internal memory management policies driven by multi-dimensional environmental rewards. MemFactory provides out-of-the-box support for recent cutting-edge paradigms, including Memory-R1, RMM, and MemAgent. We empirically validate MemFactory on the open-source MemAgent architecture using its publicly available training and evaluation data. Across both in-domain and out-of-distribution evaluation sets, MemFactory consistently improves performance over the corresponding base models, with relative gains of up to 14.8%. By providing a standardized, extensible, and easy-to-use infrastructure, MemFactory significantly lowers the barrier to entry, paving the way for future innovations in memory-driven AI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决记忆增强型大语言模型（LLM）在构建长期AI智能体时，其训练与推理框架高度碎片化、缺乏统一基础设施的核心问题。研究背景是，随着AI智能体向长期自主交互发展，赋予LLM记忆能力（如提取、更新、检索历史经验）变得至关重要。近期，利用强化学习（RL）优化这些记忆操作已成为极具前景的方向，相关研究如Memory-R1、MemAgent等已展示出超越传统启发式方法的潜力。

然而，现有方法存在显著不足：当前的各种记忆RL实现方案彼此割裂、高度定制化，且与特定任务深度耦合。这导致研究社区在复现、组合不同记忆模块（例如，将某个架构的检索模块替换为另一类重排序器）或进行系统化实验时，需要大量重复且非必要的工程工作，严重阻碍了该领域的创新与协作。

因此，本文的核心问题是填补这一基础设施空白，即缺乏一个类似于LLaMA-Factory那样标准化、可扩展的统一框架，来简化记忆增强智能体从构建、训练到评估的完整复杂流程。为此，论文提出了MemFactory，这是一个专为记忆智能体设计的首个模块化统一训练与推理框架。它通过将记忆生命周期抽象为可插拔的原子组件，支持像“搭积木”一样灵活定制智能体架构，并原生集成GRPO等RL算法来优化记忆策略，从而显著降低研究门槛，推动记忆驱动AI智能体的未来发展。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：统一微调框架、基于强化学习的记忆优化方法，以及高效的强化学习算法。

在**统一微调框架**方面，相关工作如LLaMA-Factory，它集成了多种参数高效微调和对齐算法；MS-Swift专注于多模态模型；VERL则为大规模强化学习流程提供基础设施。然而，这些框架主要针对静态的序列到序列建模，缺乏对记忆增强智能体复杂、有状态生命周期（如记忆提取、更新）的原生支持。MemFactory借鉴了前者的模块化思想和后者的强化学习中心设计，但进行了根本性重构，以专门支持记忆-强化学习这一独特范式。

在**基于强化学习的记忆优化方法**方面，近期研究将记忆管理视为顺序决策问题，用强化学习优化。代表性工作包括：1）**结构化记忆操作**（如Memory-R1），训练记忆管理器执行增删改查操作；2）**循环状态优化**（如MemAgent），将固定长度的潜在记忆变量作为循环状态进行压缩；3）**检索优化**（如RMM），利用反思信号动态优化记忆检索。这些工作证明了强化学习在不同记忆范式中的有效性，但各自为政，实现碎片化。MemFactory的核心贡献在于将这些核心机制抽象为统一模块，提供了一个可无缝复现、评估和集成这些先进算法的平台。

在**高效的强化学习算法**方面，近端策略优化是主流，但需要额外的价值网络，内存开销大。组相对策略优化通过组内奖励归一化估计优势，完全消除了参数化价值模型，显著降低了内存需求。MemFactory原生集成了GRPO，利用其内存效率，降低了记忆-强化学习研究的硬件门槛。

### Q3: 论文如何解决这个问题？

论文通过构建一个高度模块化的统一框架MemFactory来解决内存增强智能体训练与推理流程碎片化的问题。其核心方法是将复杂的内存生命周期抽象为可插拔的原子组件，并集成强化学习进行策略优化。

整体框架包含四层：模块层、智能体层、环境层和训练器层。模块层是基础核心，将内存工程流水线分解为提取、更新、检索等原子操作，并定义了标准的生成、滚动和推理接口，确保模块的可互换性。智能体层作为策略执行中心，采用“乐高式”组合方式，通过组装不同模块来构建定制化内存智能体，并负责在交互中生成轨迹。环境层兼具数据加载和奖励管理功能，它将原始数据标准化为统一状态，并根据长期与短期内存的分类设计了两种环境，同时提供格式奖励和基于大模型的评估等多维奖励信号。训练器层是优化引擎，集成了分组相对策略优化算法，利用环境反馈对智能体内加载的预训练模型进行微调，以优化其内部内存管理策略。

关键技术包括：1）模块化抽象与标准化接口，使研究者能灵活组合不同内存操作模块；2）原生集成GRPO算法，通过分组轨迹采样和相对优势计算高效优化策略；3）支持多种前沿内存范式，如Memory-R1、RMM和MemAgent，并实现了对应的模块；4）训练与推理的统一，框架允许使用相同模块配置进行纯推理比较，再投入强化学习训练。

创新点主要体现在：首次为内存增强智能体提供了统一的、可扩展的基础设施；通过原子化、可插拔的设计显著降低了构建和实验复杂内存管道的门槛；并实证验证了其在领域内和分布外评估集上能持续提升基础模型性能。

### Q4: 论文做了哪些实验？

论文实验主要围绕验证MemFactory框架的有效性展开。实验设置上，研究者基于MemFactory构建了三种代表性智能体（MemoryR1Agent、MemoryAgent、MemoryRMMAgent），并选择MemAgent架构进行具体验证。数据集采用MemAgent公开发布的训练和评估数据，训练数据经过简化，将上下文长度缩减至原长的约三分之一，每个样本包含50至80个文档。评估使用了三个测试集：两个主任务数据集（eval_50和eval_100）和一个分布外（OOD）数据集（eval_fwe_16384）。

对比方法上，实验以两个开源大语言模型（Qwen3-1.7B和Qwen3-4B-Instruct）的原始检查点作为基线，与经过MemFactory框架强化学习（RL）训练后的版本进行对比。主要结果通过表格展示：对于Qwen3-1.7B，使用MemFactory RL后，平均得分从0.3118提升至0.3581，相对提升达14.8%，在主任务数据集上提升显著（如eval_50从0.4727升至0.5684），但OOD数据集（eval_fwe_16384）得分略有下降。对于Qwen3-4B-Instruct，平均得分从0.6146提升至0.6595，相对提升7.3%，且在包括OOD数据集在内的所有测试集上均获得一致提升（如eval_50从0.6523升至0.7051）。整个训练和评估流程在单张NVIDIA A800 80GB GPU上完成，证明了框架的高效性和可复现性。

### Q5: 有什么可以进一步探索的点？

该论文提出的MemFactory框架虽在统一性和模块化上迈出重要一步，但仍存在多方面局限和可拓展空间。首先，框架目前仅支持少数代表性记忆范式（如Memory-R1、RMM），未来可扩展至更广泛的记忆机制，如基于神经符号的混合记忆或动态记忆图结构，以应对更复杂的长期任务。其次，训练效率仍有提升空间，可探索更高效的强化学习算法或与离线学习结合，减少交互成本。此外，当前评估集中于特定数据集，需在更开放、动态的多模态环境中验证其泛化能力。从系统角度看，可进一步优化框架的分布式训练支持与硬件加速，并探索记忆模块的自动架构搜索。结合见解，未来可研究跨任务记忆迁移机制，使智能体能够积累和复用不同领域的经验，真正实现持续学习。

### Q6: 总结一下论文的主要内容

该论文提出了MemFactory，首个专为记忆增强智能体设计的统一、模块化训练与推理框架。针对当前记忆增强大语言模型研究中强化学习优化方法高度碎片化、任务定制化的问题，MemFactory将记忆生命周期抽象为提取、更新、检索等原子化、可插拔组件，支持通过“乐高式”架构灵活构建定制化记忆智能体。框架原生集成了基于群体相对策略优化的训练器，可利用多维环境奖励微调内部记忆管理策略，并内置支持Memory-R1、RMM、MemAgent等前沿范式。实验基于开源MemAgent架构验证了其有效性，在领域内和分布外评估集上均一致提升性能，相对增益最高达14.8%。该框架通过提供标准化、可扩展的基础设施，显著降低了记忆驱动智能体的研发门槛，为未来创新铺平道路。
