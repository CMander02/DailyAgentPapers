---
title: "LiTS: A Modular Framework for LLM Tree Search"
authors:
  - "Xinzhe Li"
  - "Yaguang Tao"
date: "2026-02-28"
arxiv_id: "2603.00631"
arxiv_url: "https://arxiv.org/abs/2603.00631"
pdf_url: "https://arxiv.org/pdf/2603.00631v1"
github_url: "https://github.com/xinzhel/lits-llm"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "LiTS (modular framework for LLM tree search)"
  primary_benchmark: "MATH500, Crosswords, MapEval"
---

# LiTS: A Modular Framework for LLM Tree Search

## 原始摘要

LiTS is a modular Python framework for LLM reasoning via tree search. It decomposes tree search into three reusable components (Policy, Transition, and RewardModel) that plug into algorithms like MCTS and BFS. A decorator-based registry enables domain experts to extend to new domains by registering components, and algorithmic researchers to implement custom search algorithms. We demonstrate composability on MATH500 (language reasoning), Crosswords (environment planning), and MapEval (tool use), showing that components and algorithms are orthogonal: components are reusable across algorithms within each task type, and algorithms work across all components and domains. We also report a mode-collapse finding: in infinite action spaces, LLM policy diversity (not reward quality) is the bottleneck for effective tree search. A demonstration video is available at https://youtu.be/nRGX43YrR3I. The package is released under the Apache 2.0 license at https://github.com/xinzhel/lits-llm, including installation instructions and runnable examples that enable users to reproduce the demonstrated workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）树搜索推理方法（如思维树、RAP、ReST-MCTS等）在实现和应用中存在的**模块化不足、可复用性差**的核心问题。研究背景是，尽管这些树搜索方法在复杂推理任务上表现出色，但现有实现大多是任务特定的，导致两个主要弊端：当研究人员希望将方法适配到新领域（如从数学推理转向工具使用）时，需要大量重复实现工作；当需要公平比较不同搜索算法（如MCTS与BFS）的性能时，由于底层实现紧密耦合，难以确保比较是在相同的领域逻辑（如提示、环境动态）下进行的，影响了评估的可靠性。

现有方法的不足在于其“一体化”的设计，将搜索算法与领域特定的逻辑（如动作生成、状态转移、奖励判断）深度绑定。这种紧耦合使得代码难以复用、扩展和维护，阻碍了算法研究的迭代和领域应用的快速迁移。

因此，本文提出了LiTS框架，其核心要解决的是**通过模块化设计实现树搜索组件与算法的解耦**。具体而言，它将树搜索分解为三个可复用的核心组件（策略Policy、状态转移Transition、奖励模型RewardModel），并使其能够灵活接入不同的搜索算法（如MCTS、BFS）。这样，领域专家可以专注于注入领域知识（通过注册组件），而无需改动搜索算法；算法研究者则可以独立开发新算法，并轻松在不同领域和组件上进行测试。最终目标是提升LLM树搜索技术的可复用性、可扩展性和可观测性，促进该领域的算法创新与跨领域应用。

### Q2: 有哪些相关研究？

本文的相关研究主要分为方法类和应用类框架。

在方法类研究中，LLM树搜索算法本身是核心。相关工作包括将蒙特卡洛树搜索（MCTS）等经典算法应用于LLM推理，以及使用思维链（CoT）、思维树（ToT）和思维图（GoT）等提示工程技术来构建和探索推理路径。本文提出的LiTS框架并非提出新算法，而是为这些已有的搜索算法（如MCTS、BFS）提供了一个模块化、可复用的实现框架。

在应用类框架方面，本文重点对比了其他用于构建LLM推理工作流的系统。**LLM Reasoners** 是另一个提供完整树搜索实现的框架，但LiTS与其关键区别在于模块化程度。如表所示，LLM Reasoners将任务特定逻辑捆绑在整体配置类中，用户为每种搜索方法都需要重新实现完整任务逻辑。而LiTS通过分解出策略（Policy）、转移（Transition）和奖励模型（RewardModel）三个可复用组件，实现了逻辑与算法的解耦。**LangGraph** 是一个广泛采用的LLM编排框架，但它本身不原生支持树搜索。用户需要自定义状态类型、扩展/评分/剪枝函数并手动连接计算图来实现树搜索，而LiTS直接提供了预实现的搜索算法，并通过提示注册简化了跨任务应用。因此，LiTS的核心贡献在于其高度的模块化、组件共享能力和易扩展性，使得领域专家和算法研究者能够更高效地分别进行组件定制和算法创新。

### Q3: 论文如何解决这个问题？

论文通过构建一个模块化的框架LiTS来解决LLM树搜索中的通用性问题，其核心方法是将树搜索过程解耦为三个可复用的组件（Policy、Transition、RewardModel），并通过统一的抽象接口和类型系统，使这些组件能够灵活地插入到不同的搜索算法（如MCTS、BFS）中，从而支持多样化的推理任务。

整体框架基于分层类型系统（Action → Step → State → Node）设计，每个层级定义了任务无关的通用接口，使得搜索算法（lits.agents）能够独立于具体任务实现运行。主要模块包括：1）**Policy**：从当前状态生成候选动作；2）**Transition**：执行动作并产生新状态；3）**RewardModel**：评估动作质量以指导搜索。这些组件通过多态子类实现任务特定的逻辑（如数学推理、环境规划、工具使用），而基础架构（如日志记录、提示词管理）由基类统一处理。

创新点主要体现在：1）**模块化与可组合性**：通过装饰器注册机制（@register_transition等），用户无需修改核心代码即可扩展新组件或任务，实现了“即插即用”；2）**算法与组件解耦**：搜索算法（继承自BaseTreeSearch）只需实现纯算法逻辑，即可自动适配所有已注册的组件和任务类型；3）**统一的提示词管理**：通过PromptRegistry支持提示词的层级化复用（从任务实例到任务类型再到默认提示），兼顾通用性与定制化；4）**工具协议兼容性**：采用LangChain兼容的工具接口，使异构工具（如SQL查询、API调用）能够被统一的Policy和Transition调用，支持复杂的工具使用场景。

此外，框架提供了链式代理（如ReActChat）和树搜索代理（如MCTS）两种推理模式，两者共享相同的Policy和Transition组件，确保了不同推理策略在相同领域逻辑下的公平比较。这种设计使得领域专家可专注于实现任务特定的组件，而算法研究者可独立开发搜索算法，两者通过标准化的接口协同工作，显著提升了框架的灵活性和可扩展性。

### Q4: 论文做了哪些实验？

论文在三个任务类别上进行了实验，以验证LiTS框架的通用性和可扩展性。实验设置、数据集、对比方法和主要结果如下：

**实验设置与数据集**：
1.  **环境规划任务**：使用BlocksWorld（30个示例）和Crosswords（30个示例）数据集。前者动作空间有限，后者动作空间无限。使用Claude 3.5 Sonnet模型，通过AWS Bedrock API调用，因此报告成本（美元）。
2.  **工具使用任务**：使用MapEval-SQL数据集（10个示例）。同样使用Claude 3.5 Sonnet模型并报告成本。
3.  **语言推理任务**：使用MATH500数据集的前100个具有数值答案的示例。使用自部署的Llama3-8B模型，因此报告总挂钟时间（小时）。

**对比方法**：
-   主要对比了简单链式推理（Chain）与基于树搜索的方法（如MCTS、BFS、ReAct）。
-   在语言推理任务中，对比了思维链（CoT）、RAP（MCTS）、ReST（MCTS）和ToT（BFS）。

**主要结果与关键指标**：
1.  **环境规划任务**：
    *   **BlocksWorld**：MCTS准确率达到66.7%，显著优于Chain的26.7%。MCTS输出令牌数为488K，成本为$21.99。
    *   **Crosswords**：MCTS的精确匹配（所有线索正确）准确率为0%，但部分匹配（平均线索准确率）为22.67%，优于Chain的6.67%/10.33%。MCTS输出令牌数为14K，成本为$2.42。实验发现，在无限动作空间中，LLM策略多样性是瓶颈，重复率高达81.1%。
2.  **工具使用任务**：
    *   **MapEval-SQL**：ReAct方法达到40%的准确率，输出令牌10.6K，成本$0.57。MCTS在3个示例子集上准确率为0%，成本高达$18.40（$6.13/示例），表明奖励模型质量是工具使用树搜索的瓶颈。
3.  **语言推理任务**：
    *   **准确率**：ToT（BFS）和ReST（MCTS）表现最佳，分别为39%和37%，均优于CoT（17%）和RAP（MCTS，18%）。
    *   **效率**：ToT（BFS）在约14.7小时内完成，速度快于ReST（MCTS）的26.0小时和RAP（MCTS）的8.0小时。CoT最快，仅需0.6小时。
    *   **调用与令牌**：ToT（BFS）的LLM调用次数（2.8K）和输出令牌数（1.53M）低于ReST（MCTS）的4.0K调用和2.24M令牌。

实验结果表明，LiTS的组件在不同算法和任务间可重用，且算法选择（如BFS与MCTS）和组件设计（如推理形式）对性能有显著影响。

### Q5: 有什么可以进一步探索的点？

该论文提出的LiTS框架在模块化和可复用性方面具有优势，但其局限性和未来探索方向可从多个维度展开。首先，框架目前主要依赖静态组件注册，未来可探索动态环境下的自适应机制，例如在工具使用场景中实现实时工具发现与组合，这需要更灵活的过渡模型和策略组件。其次，论文指出无限动作空间中LLM策略多样性是瓶颈，未来可研究如何通过多模态策略生成、课程学习或对抗训练来增强探索能力，避免搜索陷入局部最优。此外，框架的评估集中于特定任务（如数学推理、填字游戏），未来需扩展到更复杂的现实世界问题，如多轮对话规划或跨领域决策，并考虑计算效率与搜索深度的权衡。最后，可探索将框架与外部知识库或仿真环境深度集成，以支持长期推理和不确定性处理，进一步提升其通用性和实用性。

### Q6: 总结一下论文的主要内容

LiTS是一个用于大型语言模型（LLM）树搜索推理的模块化Python框架。其核心贡献是将树搜索过程解耦为三个可复用的组件——策略（Policy）、状态转移（Transition）和奖励模型（RewardModel），这些组件可灵活插入到蒙特卡洛树搜索（MCTS）和广度优先搜索（BFS）等算法中。该框架通过基于装饰器的注册机制，使领域专家能轻松注册新组件以扩展到新领域，算法研究者也能实现自定义搜索算法。

论文在数学推理（MATH500）、环境规划（Crosswords）和工具使用（MapEval）三个任务上验证了框架的模块化和可组合性，证明了组件与算法之间的正交性：组件可在同一任务类型的不同算法间复用，算法也能跨所有组件和领域工作。一个重要发现是，在无限动作空间中，LLM策略的多样性（而非奖励模型的质量）是影响树搜索效果的关键瓶颈，即存在“模式崩溃”问题。

该框架以Apache 2.0协议开源，为LLM的复杂推理和规划任务提供了一个可扩展、易复用的实验平台，促进了算法研究与实际应用的结合。
