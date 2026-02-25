---
title: "Nazrin: Atomic Tactics for Graph Neural Networks for Theorem Proving in Lean 4"
authors:
  - "Leni Aniva"
  - "Iori Oikawa"
  - "David Dill"
  - "Clark Barrett"
date: "2026-02-21"
arxiv_id: "2602.18767"
arxiv_url: "https://arxiv.org/abs/2602.18767"
pdf_url: "https://arxiv.org/pdf/2602.18767v1"
categories:
  - "cs.LO"
  - "cs.LG"
tags:
  - "定理证明"
  - "智能体"
  - "图神经网络"
  - "自动推理"
  - "形式化验证"
  - "工具使用"
relevance_score: 7.5
---

# Nazrin: Atomic Tactics for Graph Neural Networks for Theorem Proving in Lean 4

## 原始摘要

In Machine-Assisted Theorem Proving, a theorem proving agent searches for a sequence of expressions and tactics that can prove a conjecture in a proof assistant.
  In this work, we introduce several novel concepts and capabilities to address obstacles faced by machine-assisted theorem proving. We first present a set of \textbf{atomic tactics}, a small finite set of tactics capable of proving any provable statement in Lean. We then introduce a \textbf{transposing atomization} algorithm which turns arbitrary proof expressions into a series of atomic tactics. We next introduce the \textbf{ExprGraph} data structure, which provides a succinct representation for Lean expressions. Finally, we present the \textbf{Nazrin Prover}, a graph neural network-based theorem proving agent using atomic tactics and ExprGraph. Nazrin circumvents many challenges faced by existing proving agents by exclusively dispatching atomic tactics, and it is robust enough to both train and evaluate on consumer-grade hardware. We demonstrate the potential of tools like Nazrin using theorems from Lean's standard library and from Mathlib.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器辅助定理证明（MATP）领域中的几个关键挑战。具体来说，它针对在Lean 4证明助手中，基于机器学习构建定理证明智能体（Agent）时遇到的障碍。主要问题包括：1）Lean的战术空间是无限且多样的，导致人类编写的证明数据集中存在大量噪声和选择偏好，这会使训练过程混乱或低效；2）人类编写的最终证明侧重于简洁性和可检查性，而非揭示如何“寻找”证明的过程，对学习搜索策略帮助有限；3）Lean表达式中的任意命名与数学论证无关，也引入了噪声。

为此，论文提出了一种新颖的MATP方法，其核心是通过引入一个有限的“原子战术”集合来规范化动作空间，从而降低智能体在每一步证明搜索中的决策复杂度。同时，通过“转置原子化”算法，将现有证明转换为原子战术序列，生成侧重于“如何找到证明”的训练数据。此外，论文设计了“ExprGraph”这一基于图的精简表示来捕获表达式的本质数学结构，并最终构建了基于图神经网络的定理证明智能体“Nazrin Prover”。该方法旨在使智能体能够更高效、更鲁棒地进行证明搜索，甚至可以在消费级硬件上进行训练和评估。

### Q2: 有哪些相关研究？

相关工作主要围绕定理证明的搜索方法、表达式表示和证明自动化工具展开。

在搜索方法方面，传统树搜索是基础范式。具体到定理证明，Hypertree Proof Search 引入了乘积奖励和与或树结构来评估多目标；BFS-Prover 和 DT-Solver 则利用语言模型（LLM）来估计目标的价值或可行性，后者还通过比较目标与其祖先来辅助判断。此外，LeanDojo 和 ReProver 将 LLM 作为强化学习智能体，以使用策略完成目标。DeepSeek-Prover 展示了 LLM 直接与证明助手进行文本交互的方式。本文的 Nazrin Prover 同样属于定理证明智能体，但它**摒弃了直接使用复杂策略或依赖 LLM 进行价值估计**，转而专注于调度其新提出的**原子策略**，并采用图神经网络（GNN）进行决策，旨在规避现有方法面临的挑战。

在表达式表示方面，Graph4HOL 等工作已探索使用图（GNN）来表示 HOL 中的表达式以进行前提选择，这与 Lean 环境类似。本文提出的 **ExprGraph** 数据结构延续了这一思路，为 Lean 表达式提供了一种简洁的图表示，并直接应用于 Nazrin Prover 的输入。

在证明自动化工具方面，Aesop 引入了**元变量耦合**概念，揭示了证明中目标间的相互干扰问题。Pantograph 则区分了**搜索视图**和**呈现视图**，强调了证明搜索过程与验证过程的不同。本文借鉴了 Pantograph 的视图概念（并关联到“动机证明”的思想）来缩减搜索空间，并直接使用 Pantograph 作为与 Lean 4 交互的工具。本文的原子策略和转置原子化算法，可以看作是为应对 Aesop 所指出的元变量耦合等复杂性问题，提供了一种更细粒度、更可控的底层操作基础。

### Q3: 论文如何解决这个问题？

论文通过引入“原子策略”这一核心概念来解决定理证明中策略空间无限大、搜索困难的挑战。具体而言，作者设计了一个有限、完备的原子策略集合，使得任何在Lean中可证的陈述都能仅由这些策略证明。这些策略与Lean表达式的基本构造器一一对应（如表1所示），并确保每个策略的参数选择也是有限的，从而将动作空间离散化、有限化。

为了生成训练数据，论文提出了“转置原子化”算法。该算法能够将任意已有的证明项（即“表示视图”证明）转换为一系列原子策略步骤（即“搜索视图”证明）。算法以目标-解决方案对为输入，递归地尝试为当前目标匹配一个原子策略，生成新的子目标及其对应的解决方案，直至所有目标被解决。这为后续的神经网络训练提供了结构化的序列数据。

在模型架构方面，论文设计了ExprGraph数据结构来紧凑地表示Lean表达式和目标。ExprGraph是一种异构图，它通过“本质化”过程剔除了证明搜索中无关的细节（如变量名、某些技术性区别），并保持了对称性、自相似性、位置守恒和凝聚性等优良性质，非常适合图神经网络处理。

基于上述基础，论文构建了Nazrin证明器，这是一个基于图神经网络的定理证明智能体。模型采用了一种称为“神经概率自动机”的架构。GNN首先根据输入的ExprGraph（当前证明状态）在“种类”状态节点输出一个概率分布，以选择要使用的原子策略。如果所选策略需要参数（例如`apply`需要选择一个常数），则会激活后续特定的GNN头（如“应用”状态节点）来生成参数，这些参数通常通过检索与当前查询嵌入最相关的键（如可用常数集合）来确定。这种设计使得模型能够在一个有限、结构化的动作空间中进行端到端的策略生成和参数预测，从而绕过了传统证明智能体面临的许多挑战，并能在消费级硬件上进行训练和评估。

### Q4: 论文做了哪些实验？

该论文的实验设置围绕评估Nazrin Prover在Lean 4定理证明环境中的性能。实验基准主要使用Lean标准库（Std）和Mathlib中的定理作为测试集，将Nazrin与基于大型语言模型（LLM）的基线方法（如GPT-f）进行对比。核心实验包括：在训练集上验证原子战术和ExprGraph表示的有效性，并在未见过的定理上测试模型的泛化能力。

主要结果显示，Nazrin能够成功证明Lean标准库和Mathlib中的一系列定理，证明了原子战术的完备性和ExprGraph表示的实用性。与LLM基线相比，Nazrin在资源效率上表现突出，仅需消费级硬件即可完成训练和推理，同时避免了传统方法因战术组合爆炸带来的搜索挑战。实验还表明，通过原子战术的分解，模型能更稳健地处理复杂证明步骤，提升了定理证明的自动化水平。

### Q5: 有什么可以进一步探索的点？

该论文提出的原子化策略和 ExprGraph 结构虽能简化证明搜索，但仍存在明显局限。首先，原子战术序列可能比高级战术更长，导致搜索空间虽更规整但规模更大，效率问题未根本解决。其次，模型目前仅针对 Lean 4 设计，其方法能否泛化到其他证明辅助系统（如 Coq、Isabelle）尚未验证，依赖特定语法和库可能限制通用性。此外，实验仅基于标准库和 Mathlib 的已知定理，对未见过或更复杂的数学领域（如需要创造性构造的拓扑证明）的泛化能力存疑。

未来可探索的方向包括：1）结合原子战术与高级战术的混合搜索策略，在保证完备性的同时提升效率；2）将方法扩展到多证明系统，研究跨平台的定理证明迁移学习；3）引入外部知识（如数学概念库）增强模型对抽象推理的理解；4）探索强化学习与 GNN 的结合，让智能体在长期证明序列中学习策略优化。

### Q6: 总结一下论文的主要内容

这篇论文针对机器辅助定理证明中的挑战，提出了一套创新方法。其核心贡献是引入了**原子策略**——一个有限的小型策略集合，理论上能证明Lean中任何可证的陈述，从而将证明搜索的动作空间大幅简化。为了生成训练数据，论文提出了**转置原子化算法**，能将现有证明转化为原子策略序列，使模型学习如何“寻找”证明而非仅仅“呈现”证明。此外，论文设计了**ExprGraph**数据结构，以紧凑的图形式表示Lean表达式，捕捉数学结构中的本质对称性。基于这些基础，论文构建了**Nazrin证明器**，这是一个基于图神经网络的定理证明智能体，它仅使用原子策略进行推理，并能在消费级硬件上训练和评估。实验表明，Nazrin在Lean标准库和Mathlib的定理上展现出潜力。整体上，该工作通过原子化、新的数据表示和轻量级神经网络架构，为机器辅助定理证明提供了一种更清晰、可训练且资源友好的新途径。
