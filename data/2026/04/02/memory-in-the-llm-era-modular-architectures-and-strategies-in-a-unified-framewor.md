---
title: "Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework"
authors:
  - "Yanchen Wu"
  - "Tenghui Lin"
  - "Yingli Zhou"
  - "Fangyuan Zhang"
  - "Qintian Guo"
  - "Xun Zhou"
  - "Sibo Wang"
  - "Xilin Liu"
  - "Yuchi Ma"
  - "Yixiang Fang"
date: "2026-04-02"
arxiv_id: "2604.01707"
arxiv_url: "https://arxiv.org/abs/2604.01707"
pdf_url: "https://arxiv.org/pdf/2604.01707v1"
categories:
  - "cs.CL"
  - "cs.DB"
tags:
  - "Agent Memory"
  - "Unified Framework"
  - "Benchmark Evaluation"
  - "Modular Architecture"
  - "Comparative Analysis"
  - "Method Synthesis"
relevance_score: 9.0
---

# Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework

## 原始摘要

Memory emerges as the core module in the large language model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulation, iterative reasoning and self-evolution. A number of memory methods have been proposed in the literature. However, these methods have not been systematically and comprehensively compared under the same experimental settings. In this paper, we first summarize a unified framework that incorporates all the existing agent memory methods from a high-level perspective. We then extensively compare representative agent memory methods on two well-known benchmarks and examine the effectiveness of all methods, providing a thorough analysis of those methods. As a byproduct of our experimental analysis, we also design a new memory method by exploiting modules in the existing methods, which outperforms the state-of-the-art methods. Finally, based on these findings, we offer promising future research opportunities. We believe that a deeper understanding of the behavior of existing methods can provide valuable new insights for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体领域中，关于“记忆”机制的研究缺乏系统性比较和统一分析框架的问题。随着GPT-5、Qwen3等大语言模型的发展，基于LLM的智能体在复杂长程任务（如多轮对话、游戏、科学发现）中扮演着越来越重要的角色。在这些任务中，记忆模块是核心，它使智能体能够积累知识、进行迭代推理和自我进化，从而超越简单的长上下文提示，实现持续的上下文理解和个性化决策。

尽管近年来学术界提出了多种记忆方法（如MemGPT、MemoryBank等），但现有研究存在明显不足。首先，这些方法在设计和实现上各有侧重，缺乏一个统一的高层框架来抽象和系统化地分析它们，导致难以理解不同方法之间的本质联系与差异。其次，大多数研究只报告整体性能结果，很少深入剖析方法内部各个组件（如信息提取、存储结构、管理操作、检索机制）的具体作用和效果。最后，缺乏在相同实验设置下，对这些方法的准确性和效率进行全面、系统的比较。

因此，本文要解决的核心问题是：如何在一个统一的框架下，系统地梳理、比较和评估现有的智能体记忆方法，并基于此分析设计出更优的方法。为此，论文首先提出了一个统一的模块化框架，将记忆机制分解为信息提取、记忆管理、记忆存储和信息检索四个阶段，以此对现有方法进行归类和解构。然后，论文在LOCOMO和LONGMEMEVAL两个标准长程对话基准上，对代表性方法进行了广泛的实验比较和深入分析（包括性能、成本、上下文扩展性、位置敏感性等）。作为分析的自然产物，论文还通过组合现有方法的模块，设计了一种新的记忆方法，并验证其优于现有最优方法。最终，这些工作旨在为未来研究提供有价值的见解和明确的方向。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM时代下Agent的记忆方法展开，可归纳为以下几类：

**方法类研究**：已有多种记忆方法被提出，旨在通过显式记忆模块来弥补LLM有限的上下文窗口，实现跨轮次和跨会话的信息持久化与重用。这些方法通常涉及信息的提取、存储、管理（如整合、更新、过滤、增强）和检索等流程。然而，现有方法此前缺乏在统一实验设置下的系统化比较与评估。

**应用与评测类研究**：记忆机制在长视野复杂任务（如多轮对话、游戏、科学发现）中至关重要，相关研究常基于特定基准（如文中提及的两个知名基准）进行评测。这些工作探索了记忆如何促进知识积累、迭代推理和自我进化。

**与RAG的关联研究**：检索增强生成（RAG）主要关注从外部知识库检索事实证据以补充领域知识，而记忆则侧重于管理随时间演进的、与交互和状态相关的信息（如用户偏好、重要事件），两者功能互补，常被结合使用以同时提供个性化上下文和事实依据。

**本文与这些工作的关系和区别**：本文的贡献在于首次从高层视角总结了一个能涵盖所有现有Agent记忆方法的统一框架，并在此框架下对代表性方法进行了广泛、系统的实验比较与分析。这种统一的视角和全面的评测弥补了以往研究分散、缺乏直接对比的不足。此外，本文还通过利用现有方法中的模块，设计了一种新的记忆方法，并在实验中取得了优于现有最佳方法的性能。

### Q3: 论文如何解决这个问题？

该论文通过提出一个统一的模块化框架，并在此框架下进行系统性实验比较与创新组合，来解决现有智能体记忆方法缺乏系统性评估和统一理解的问题。

其核心方法是构建一个涵盖所有现有记忆方法的四组件统一框架。该框架将智能体记忆系统分解为四个关键模块：**信息提取**（从当前消息中筛选和转换关键知识）、**记忆管理**（将新信息与现有记忆通过整合、更新等操作进行融合）、**记忆存储**（以向量、图或混合形式组织和持久化记忆）以及**信息检索**（根据查询从存储中检索相关信息）。这个框架从高层视角抽象了不同方法的共性，为系统化比较提供了基础。

在架构设计上，论文以此框架为指导，在多个知名基准上对代表性方法进行了全面实验。实验分析不仅评估了各方法的有效性，还深入剖析了不同模块设计对性能的影响。作为分析的自然产物，论文的创新点在于**利用现有方法的模块进行组合，设计出一种新的记忆方法**。该方法通过择优选取和整合不同方法中表现最优的组件模块，形成了一个性能更强的混合架构，从而超越了当时的先进方法。

最终，论文通过“统一框架构建 -> 系统性实验比较 -> 模块化创新设计”这一连贯策略，不仅实现了对现有记忆方法的透彻理解与比较，还直接催生了一种更优的新方法，并为未来研究指明了方向。

### Q4: 论文做了哪些实验？

论文在统一的实验框架下，对多种智能体记忆方法进行了系统性的实验比较。实验设置方面，研究复现了10种代表性的记忆方法，包括A-MEM、MemoryBank、MemGPT、Mem0、MemoChat、Zep、MemTree、MemoryOS和MemOS，并在8张NVIDIA A100 GPU上运行。默认使用Qwen2.5-7B-Instruct作为基础大语言模型，最大上下文长度为20,000个token，采用贪婪解码，并使用统一的all-MiniLM-L6-v2句子嵌入模型进行检索。

实验在两个广泛使用的长时记忆基准数据集上进行：LOCOMO和LONGMEMEVAL。LOCOMO基于双人对话，包含10个长对话，平均198.6个问题，涵盖单跳检索、多跳检索、时序推理和开放域知识四类任务。LONGMEMEVAL基于用户-AI交互，包含500个问题，评估信息提取、多会话推理、知识更新和时序推理四种核心能力。

评估采用F1和BLEU-1两个互补指标。主要结果通过表格呈现，对比了各方法在不同任务和不同规模模型（Qwen2.5-7B-Instruct和Qwen2.5-72B-Instruct）下的表现。关键数据指标显示，在LONGMEMEVAL上，使用7B模型时，MemTree在总体F1和BLEU-1上取得最佳成绩（36.92和31.05），MemoryOS紧随其后（32.50和28.31）。使用72B模型时，MemoryOS表现最佳（总体F1 46.04，BLEU-1 39.42），MemTree次之（44.25和37.02）。在LOCOMO上，Mem0和Mem0\(^g\)在时序推理任务上表现突出（F1分别达37.49和35.70）。此外，实验还进行了多维度分析，包括token成本效率、真实信息位置敏感性、上下文可扩展性以及大模型主干依赖性评估。

### Q5: 有什么可以进一步探索的点？

该论文虽然对现有记忆方法进行了系统性比较，并提出了统一框架，但仍存在一些局限性和值得深入探索的方向。首先，实验主要基于特定基准任务（如多轮对话、游戏），其结论在更开放、动态的真实世界场景（如长期自主交互、跨领域任务迁移）中的泛化能力有待验证。其次，当前框架侧重于模块化设计，但未深入探讨记忆的“质量评估”机制——例如如何动态遗忘冗余信息或纠错，这在实际应用中至关重要。

未来研究可朝以下方向拓展：一是开发自适应记忆策略，使智能体能根据任务复杂度实时调整记忆容量与检索粒度；二是探索记忆与推理的更深层耦合，例如引入神经符号结合的方法，提升记忆的逻辑结构化能力；三是加强跨任务记忆迁移研究，通过元学习或终身学习框架，让记忆模块在多样任务中持续进化。此外，结合神经科学中的人类记忆模型（如情景记忆与语义记忆的互动），可能为设计更高效的记忆架构提供新灵感。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体中的记忆机制进行了系统性研究。核心问题是现有多种记忆方法缺乏统一的框架和公平的比较，阻碍了对各方法组件效果的理解与进一步优化。为此，论文首先提出了一个统一的模块化框架，将记忆机制分解为信息提取、记忆管理、记忆存储和信息检索四个阶段，并在此框架下对十种代表性方法进行了分类与剖析。

论文的主要方法是在此统一框架下，于LOCOMO和LONGMEMEVAL两个长期对话基准上，对这些方法进行了全面的实验比较与分析，评估维度包括整体性能、计算成本、上下文扩展性和位置敏感性等。实验分析的一个重要副产品是，作者通过组合现有方法的有效模块，设计出一种新的记忆方法，该方法在实验中取得了优于现有最优方法的性能。

主要结论是，该统一框架为系统化理解和比较智能体记忆方法提供了有效视角，而深入的实验分析揭示了不同设计选择的影响。基于此提出的新方法验证了模块化设计的优势。论文的贡献在于为未来记忆机制的研究提供了清晰的分类框架、全面的实验基准、性能更优的新方法以及有价值的研究方向启示。
