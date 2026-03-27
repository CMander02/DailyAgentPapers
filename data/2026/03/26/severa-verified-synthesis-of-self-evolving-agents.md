---
title: "SEVerA: Verified Synthesis of Self-Evolving Agents"
authors:
  - "Debangshu Banerjee"
  - "Changming Xu"
  - "Gagandeep Singh"
date: "2026-03-26"
arxiv_id: "2603.25111"
arxiv_url: "https://arxiv.org/abs/2603.25111"
pdf_url: "https://arxiv.org/pdf/2603.25111v1"
categories:
  - "cs.LG"
  - "cs.PL"
  - "cs.SE"
tags:
  - "Self-Evolving Agent"
  - "Formal Verification"
  - "Agent Safety"
  - "Agent Synthesis"
  - "Program Synthesis"
  - "Constrained Learning"
  - "Tool Use"
  - "Agent Architecture"
relevance_score: 9.0
---

# SEVerA: Verified Synthesis of Self-Evolving Agents

## 原始摘要

Recent advances have shown the effectiveness of self-evolving LLM agents on tasks such as program repair and scientific discovery. In this paradigm, a planner LLM synthesizes an agent program that invokes parametric models, including LLMs, which are then tuned per task to improve performance. However, existing self-evolving agent frameworks provide no formal guarantees of safety or correctness. Because such programs are often executed autonomously on unseen inputs, this lack of guarantees raises reliability and security concerns. We formulate agentic code generation as a constrained learning problem, combining hard formal specifications with soft objectives capturing task utility. We introduce Formally Guarded Generative Models (FGGM), which allow the planner LLM to specify a formal output contract for each generative model call using first-order logic. Each FGGM call wraps the underlying model in a rejection sampler with a verified fallback, ensuring every returned output satisfies the contract for any input and parameter setting. Building on FGGM, we present SEVerA (Self-Evolving Verified Agents), a three-stage framework: Search synthesizes candidate parametric programs containing FGGM calls; Verification proves correctness with respect to hard constraints for all parameter values, reducing the problem to unconstrained learning; and Learning applies scalable gradient-based optimization, including GRPO-style fine-tuning, to improve the soft objective while preserving correctness. We evaluate SEVerA on Dafny program verification, symbolic math synthesis, and policy-compliant agentic tool use ($τ^2$-bench). Across tasks, SEVerA achieves zero constraint violations while improving performance over unconstrained and SOTA baselines, showing that formal behavioral constraints not only guarantee correctness but also steer synthesis toward higher-quality agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自进化大语言模型（LLM）智能体在合成与执行过程中缺乏形式化安全保障的核心问题。研究背景是，当前利用LLM代码生成能力来自动合成智能体程序（即自进化智能体）的范式，在程序修复、科学发现等任务上显示出强大潜力。该范式通常由规划器LLM生成一个包含参数化模型（如LLM、小型神经网络、外部工具）调用的程序，并通过微调这些参数来提升任务性能。然而，现有方法存在严重不足：它们主要依赖自然语言任务描述和固定输入的测试，缺乏对智能体行为的形式化规范与验证。这导致合成的程序在未知输入上自主运行时，可能产生严重的安全与可靠性问题，例如在程序验证中作弊修改代码、在代码修复中删除失败测试、在工具使用中大规模违反领域策略等。现有方法要么（如演绎式程序合成）能提供形式化保证但无法优化任务性能，要么（如基于梯度的优化方法）能提升性能却无法保证约束满足。

因此，本文要解决的核心问题是：如何设计一个既能提供形式化正确性保证，又能通过参数优化提升任务性能的自进化智能体合成框架。具体而言，论文需要平衡安全性与性能，并找到一种能为智能体程序中每个生成模型调用灵活指定并强制执行形式化约束的机制，同时确保这些约束在模型参数更新后依然成立。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自进化智能体、形式化验证与约束学习以及程序合成与验证三大类别展开。

在**自进化智能体**方面，相关工作如AutoGPT、MetaGPT等框架探索了LLM自主规划和执行任务的能力。这些工作通常侧重于通过提示工程、工具调用或环境交互来提升任务性能，但缺乏对智能体行为安全性与正确性的形式化保证。本文提出的SEVerA框架同样属于自进化范式，但核心区别在于引入了形式化约束，为智能体程序提供可验证的正确性保障。

在**形式化验证与约束学习**领域，相关工作包括将形式化规范（如契约、时序逻辑）与机器学习结合的方法，例如在强化学习中施加安全约束（Safe RL），或使用可满足性模理论（SMT）求解器验证神经网络的属性。本文的贡献在于提出了形式化守护生成模型（FGGM），它将生成模型（如LLM）的调用包裹在具有可验证回退机制的拒绝采样器中，从而确保输出始终满足用一阶逻辑指定的形式化契约。这与传统的事后验证或软约束方法不同，FGGM在调用时即提供硬性保证。

在**程序合成与验证**方面，大量研究致力于从规范或示例中自动生成程序，并利用形式化方法（如Dafny、Coq）进行验证。本文的工作将智能体程序合成视为一个约束学习问题，将搜索、验证和学习三个阶段紧密结合。其创新点在于，先通过形式化验证确保候选程序在所有参数下均满足硬约束，从而将问题简化为无约束学习，再通过基于梯度的优化（如GRPO风格的微调）来提升软目标性能。这种方法区别于传统的、可能无法保证泛化正确性的端到端合成或微调方法。

综上所述，本文与现有工作的核心关系是继承并融合了自进化智能体、形式化验证和程序合成的思想，但其关键区别在于通过FGGM和分阶段的验证学习框架，首次为自进化智能体提供了严格的形式化正确性保证，并证明这种约束不仅能确保安全，还能引导合成出更高质量的智能体。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SEVerA的三阶段框架来解决自进化智能体缺乏形式化安全保障的问题。其核心方法是**将智能体代码生成建模为一个约束学习问题**，结合硬性形式化规约与软性任务效用目标，并引入**形式化守卫生成模型（FGGM）** 作为关键创新组件来确保可靠性。

**整体框架**包含三个主要阶段：
1.  **搜索（Search）**：由规划器大语言模型根据任务信息、库函数集合、参数化生成模型列表以及行为规约，合成候选的参数化智能体程序。程序中的所有生成模型调用都通过FGGM进行定义，即为其指定局部输入-输出契约（用一阶逻辑表示）。
2.  **验证（Verify）**：首先验证规划器提出的所有FGGM定义本身是否良构。一旦通过，便利用这些局部契约来检查整个程序是否满足全局行为规约。若验证通过，则进入无约束学习阶段；否则，将错误信息反馈给规划器以迭代改进。
3.  **学习（Learn）**：对已验证程序中的每个FGGM内部的底层生成模型参数进行基于梯度的优化（例如GRPO风格的微调），以降低任务损失并提升模型对其局部契约的遵从性，同时保持形式化正确性不变。优化后的智能体会加入已验证池，并可能用于生成新的候选程序。

**核心模块与关键技术**：
*   **形式化守卫生成模型（FGGM）**：这是架构的核心创新。每个FGGM调用封装一个底层生成模型（如LLM），并绑定由规划器定制的局部契约 `(φ_local, ψ_local)`。FGGM的实现包含一个**拒绝采样器**和一个**经验证的非参数后备程序**。采样器会尝试从生成模型获取最多K个输出，仅接受满足局部契约的样本；若所有样本均被拒绝，则执行后备程序。**关键特性**在于：1) **灵活性**：允许规划器动态定义契约；2) **参数无关的正确性**：由于有经验证的后备程序兜底，无论底层模型参数如何变化，FGGM的输出都保证满足其局部契约；3) **局部学习目标**：局部契约本身为梯度优化提供了明确的目标，引导模型生成更符合契约的输出，从而提高采样接受率，减少对后备程序的依赖。
*   **验证器**：利用FGGM提供的局部契约以及关于库函数的公理，对智能体程序进行形式化验证，证明其对于所有可能的输入和参数值都满足全局行为约束。这**将约束学习问题简化为无约束优化问题**，因为一旦程序通过验证，后续的参数调优就不会破坏其正确性。
*   **规划器与搜索空间**：规划器大语言模型在受限的Dafny语言子空间（支持基本类型、条件、循环、函数调用）中进行搜索合成。库函数集包括非参数函数（如数学运算、验证器、解析器）和小型参数化神经网络，支持神经符号程序的表达。

**创新点总结**：
1.  **理论框架创新**：首次为自进化智能体提出了一个结合形式化验证与梯度学习的统一约束学习框架。
2.  **FGGM设计**：创造性地通过“拒绝采样+经验证后备”机制，将不可靠的生成模型调用转化为具有形式化保证的组件，从而桥接了离散程序合成与连续参数优化。
3.  **保证与性能兼得**：通过验证阶段确保智能体始终满足硬性安全约束，再通过无约束学习阶段优化任务性能，实现了安全性与实用性的统一。实验表明，该方法能在实现零约束违反的同时，性能超越无约束和现有先进基线。

### Q4: 论文做了哪些实验？

论文在三个任务上进行了实验评估：Dafny程序验证、符号数学合成和符合策略的智能体工具使用（τ²-bench）。实验设置上，SEVerA框架包含搜索、验证和学习三个阶段，核心是形式化守卫生成模型（FGGM），它将生成模型调用与局部输入-输出契约绑定，并配备经验证的备用程序，确保无论模型参数如何，契约始终成立。

数据集和基准测试方面：1）Dafny程序验证任务使用Dafny内置验证器定义损失函数，并利用Dafny解析器和AST差异检查器定义行为约束；2）符号回归任务使用包含噪声观测值的数据集，损失函数为归一化均方误差（NMSE），并编码已知的函数属性作为形式约束；3）τ²-bench用于评估符合策略的智能体工具使用。

对比方法包括无约束基线（如直接使用LLM规划器）和当前最优（SOTA）方法。主要结果显示，SEVerA在所有任务上均实现了零约束违反，同时性能优于无约束和SOTA基线。关键数据指标包括：在符号回归任务中，SEVerA在满足约束的同时实现了更低的NMSE；在程序验证任务中，成功验证的程序比例更高；在τ²-bench上，任务完成率提升且无策略违反。这表明形式化行为约束不仅能保证正确性，还能引导合成更高质量的智能体。

### Q5: 有什么可以进一步探索的点？

本文提出的SEVerA框架在保证形式化正确性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其验证过程严重依赖形式化规约的精确编写，这在实际复杂任务中可能成为瓶颈；未来可研究如何自动化或半自动化地从自然语言任务描述中推导出形式化约束。其次，当前方法主要处理静态约束，对于动态环境或时序性约束的保障能力有限，可探索将时序逻辑或运行时监控机制融入框架。此外，框架的验证阶段可能带来较高的计算开销，未来需研究更高效的符号验证或抽象解释技术以提升可扩展性。从更广阔的视角看，如何平衡形式化保证与开放式探索能力是一个关键挑战；或许可以引入“安全探索”机制，在已验证的安全边界内允许Agent进行有限度的自主创新。最后，将此类方法扩展到多智能体协作场景，并研究其 emergent behavior 的可靠性，也是一个富有前景的方向。

### Q6: 总结一下论文的主要内容

本文提出了一种名为SEVerA的框架，旨在为自进化智能体提供形式化的安全与正确性保证。核心问题是现有自进化智能体框架缺乏形式化验证，导致在未知输入上自主执行时存在可靠性和安全隐患。为此，论文将智能体代码生成建模为约束学习问题，结合硬性形式规范与软性任务效用目标。

方法上，论文首先引入了形式化守卫生成模型（FGGM），允许规划LLM使用一阶逻辑为每个生成模型调用指定形式化输出契约，并通过经验证的备用机制确保输出始终满足契约。基于FGGM，SEVerA框架分为三个阶段：搜索阶段合成包含FGGM调用的候选参数化程序；验证阶段使用内置验证器证明程序对所有参数值均满足硬约束，从而将问题简化为无约束学习；学习阶段通过基于梯度的优化（如GRPO微调）提升软性目标，同时保持正确性。

主要结论表明，SEVerA在多个任务（如Dafny程序验证、符号数学合成和策略合规工具使用）中实现了零约束违反，且性能优于无约束和现有先进基线。这证明形式化行为约束不仅能保证正确性，还能引导合成更高质量的智能体，平衡了安全性与性能。
