---
title: "Power and Limitations of Aggregation in Compound AI Systems"
authors:
  - "Nivasini Ananthakrishnan"
  - "Meena Jagadeesan"
date: "2026-02-25"
arxiv_id: "2602.21556"
arxiv_url: "https://arxiv.org/abs/2602.21556"
pdf_url: "https://arxiv.org/pdf/2602.21556v1"
categories:
  - "cs.AI"
  - "cs.GT"
tags:
  - "Compound AI Systems"
  - "Aggregation"
  - "Principal-Agent Framework"
  - "Elicitability"
  - "System Design"
  - "Model Capabilities"
  - "Prompt Engineering"
relevance_score: 7.5
---

# Power and Limitations of Aggregation in Compound AI Systems

## 原始摘要

When designing compound AI systems, a common approach is to query multiple copies of the same model and aggregate the responses to produce a synthesized output. Given the homogeneity of these models, this raises the question of whether aggregation unlocks access to a greater set of outputs than querying a single model. In this work, we investigate the power and limitations of aggregation within a stylized principal-agent framework. This framework models how the system designer can partially steer each agent's output through its reward function specification, but still faces limitations due to prompt engineering ability and model capabilities. Our analysis uncovers three natural mechanisms -- feasibility expansion, support expansion, and binding set contraction -- through which aggregation expands the set of outputs that are elicitable by the system designer. We prove that any aggregation operation must implement one of these mechanisms in order to be elicitability-expanding, and that strengthened versions of these mechanisms provide necessary and sufficient conditions that fully characterize elicitability-expansion. Finally, we provide an empirical illustration of our findings for LLMs deployed in a toy reference-generation task. Altogether, our results take a step towards characterizing when compound AI systems can overcome limitations in model capabilities and in prompt engineering.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在从理论层面探究复合人工智能系统中“聚合”操作的根本能力与局限。复合AI系统通过整合多个AI组件（例如多个相同大语言模型的副本）来处理复杂任务，这是一种常见且有效的范式。然而，当这些被聚合的模型副本本质上是同质的时候，一个核心问题随之产生：这种聚合操作是否真的能让系统设计者获得比查询单一模型更多样或更优的输出？换言之，聚合在何时以及如何能够克服单一模型固有的限制？

研究背景在于，尽管实践中聚合方法（如多智能体辩论、提示集成等）已显示出性能提升，但其背后的理论原理尚不清晰。现有方法主要依赖经验观察，缺乏一个严谨的框架来系统性地分析聚合何时有效、为何有效。具体而言，系统设计者面临两大限制：一是“提示工程能力”的限制，即无法通过完美的提示（奖励函数）精确引导模型；二是“模型能力”的限制，即模型本身有其输出可行集的约束。

本文要解决的核心问题，就是在上述限制下，从理论上刻画聚合操作扩展系统设计者可获取输出集合（即可激发性）的能力边界。为此，论文建立了一个程式化的委托-代理框架，将系统设计者视为委托人，将每个模型副本视为代理人。在此框架下，论文形式化地揭示了聚合扩展可激发输出集的三种内在机制：可行性扩展（聚合产生单个代理可行集之外的输出）、支持扩展（聚合产生支持集更丰富的输出）以及约束集收缩（聚合将处于约束边界的输出合成为内部点）。论文的核心贡献在于证明：任何能扩展可激发性的聚合操作都必须实现至少其中一种机制（必要性），并且强化版本的这些机制共同构成了聚合扩展可激发性的充分必要条件。这为理解聚合在复合AI系统中的力量与局限提供了完整的理论特征。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**复合AI系统中的聚合方法**和**委托-代理模型与奖励设计**。

在**聚合方法**方面，相关工作包括：1）**推理时聚合**，如通过奖励模型、自一致性或合成方法对同一模型的多次采样输出进行选择，其中覆盖性是一个关键属性；2）**多智能体系统**，例如LLM辩论、生成器与判别器之间的共识博弈、提示集成以及多智能体研究框架，这些系统通常在相同模型的不同奖励函数设定下进行聚合；3）**异质模型组合**，例如通过路由查询或将模型对抗性组合以生成结果。本文与这些工作的关系在于，它们都探索了聚合多个模型输出的实践，但本文的区别在于从一个理论化的委托-代理框架出发，专注于**聚合何时能比查询单一模型引出更丰富的输出**这一根本概念问题，并形式化地揭示了聚合发挥作用的三种机制。

在**委托-代理模型与奖励设计**方面，本文直接扩展了Grossklags等人提出的战略分类中的委托-代理框架。相关研究包括：1）**单智能体设置下的努力引导分析**，原有工作刻画了分类器如何激励代理人付出真实努力；2）**多任务设置中的成本依赖研究**，探讨任务间的替代性与互补性，这与本文中锥形约束所捕获的输出维度间相互作用类似；3）**多智能体奖励联合设计**，但通常不涉及输出的聚合合成。本文的扩展在于引入了**多个智能体**并**聚合其输出**，同时用**锥形约束建模模型的能力限制**，并提出了**“可引出性扩展”**这一新概念来形式化聚合带来的能力提升。本文的目标是刻画聚合如何克服提示工程限制和模型能力限制，这与以往关注单一奖励函数设计或战略交互的研究有所不同。

### Q3: 论文如何解决这个问题？

论文通过构建一个形式化的主-代理框架来研究聚合在复合AI系统中的能力与局限。核心方法是：将系统设计者视为主方（Principal），将多个同质的大型语言模型（LLM）视为代理（Agents），主方通过设计奖励函数和预算来引导每个代理生成输出，然后聚合这些输出以合成最终结果。

整体框架包含三个关键部分：1）**输出表示**：将每个代理的输出表示为M维非负向量，每个维度对应输出的一种特征（如话题覆盖度、质量等）。2）**模型能力约束**：用锥形约束矩阵C来刻画代理的能力限制，定义了代理能生成的可行输出集合。3）**提示工程限制**：通过特征权重矩阵α将高维输出映射到低维特征空间，奖励函数基于这些特征计算，这模拟了设计者无法通过提示精确控制所有输出维度的问题。

主要模块包括：代理优化程序（每个代理在可行集和预算约束下最大化其奖励函数）、聚合规则（如取坐标最小值的交集聚合和加权求和的加法聚合），以及可激发性（Elicitability）的定义与判定机制。

论文的创新点在于提出了聚合扩展可激发性的三种自然机制：1）**可行性扩展**：聚合能产生超出单个代理可行集的输出，例如通过交集聚合剔除不良维度。2）**支持扩展**：聚合能组合多个小支持集的输出，形成支持集更丰富的输出，克服奖励函数无法同时激励多个维度的限制。3）**绑定集收缩**：聚合能结合多个有绑定约束的输出，产生绑定约束更少的输出，利用约束限制来简化激励方向。

这些机制被证明是聚合扩展可激发性的必要条件，而强化版本则构成充分必要条件。论文还通过一个参考文献生成任务的实证分析，展示了不同提示和聚合规则如何产生语义不同的输出向量，验证了理论框架的实用性。

### Q4: 论文做了哪些实验？

论文通过一个玩具式的参考文献生成任务进行了实证研究，以说明其理论发现。实验设置基于一个简化的主-代理框架，其中系统设计者通过指定奖励函数来部分引导每个代理（即相同模型的多个副本）的输出，但仍受限于提示工程能力和模型能力。实验聚焦于一个三维输出空间（M=3）和二维特征（N=2），特征权重矩阵为特定形式，使前两个输出维度分别专用于两个特征，第三个维度同时影响两个特征，其贡献由参数q加权。

数据集/基准测试方面，论文未使用外部标准数据集，而是构建了一个受控的合成任务环境，以探究聚合机制如何扩展可激发性。对比方法主要涉及两种聚合规则：交集聚合（intersection aggregation）和加法聚合（addition aggregation），用于比较单模型查询与多模型聚合后的输出效果。

主要结果方面，论文通过理论分析和示例验证了三种自然机制如何通过聚合扩展可激发性：可行性扩展（产生超出单个代理可行集的输出）、支持扩展（组合具有较小支持集的输出以产生支持更丰富的输出）和绑定集收缩（组合具有绑定约束的输出以产生约束更少的输出）。关键数据指标包括：在可行性扩展示例中，聚合操作将输出[1,0,1]和[0,1,1]合成为[0,0,1]，后者因仅包含“合意”维度而不可行，但通过聚合变得可激发；在支持扩展示例中，聚合将[1,0,0]和[0,1,0]合成为[1/2,1/2,0]，后者无法直接激发，但通过聚合实现；绑定集收缩机制则通过减少绑定约束来增强可激发性。这些结果共同表明，聚合能在特定条件下克服模型能力和提示工程的限制。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其理论框架较为理想化，假设了同质化模型和简化的奖励函数设定，未充分考虑现实场景中模型的异质性、复杂任务的多维度要求以及动态环境下的适应性。未来研究可探索异质模型聚合的机制，分析不同架构或训练数据的模型组合如何互补；同时，可将理论扩展到更复杂的任务结构，如多轮交互或分层决策，以验证聚合机制在真实复合AI系统中的泛化能力。此外，结合强化学习或元学习优化聚合策略，动态调整权重以应对模型不确定性，可能进一步提升系统输出范围。实证研究也可从玩具任务扩展到实际应用，如代码生成或科学推理，以检验理论发现的实践价值。

### Q6: 总结一下论文的主要内容

本文研究了复合AI系统中聚合操作的能力与局限。核心问题是：当系统设计者查询多个相同模型的副本并聚合其响应时，聚合能否比查询单一模型获得更丰富的输出集合？论文在一个程式化的委托-代理框架下形式化该问题，其中设计者通过奖励函数（如提示）部分引导每个代理（模型）的输出，但仍受限于提示工程能力和模型能力。

论文的核心贡献是识别并形式化了聚合扩展设计者可引出输出集的三种机制：可行性扩展（聚合产生超出任何代理可行集的输出）、支持扩展（聚合将支持集较小的输出合并为支持更丰富的输出）和约束集收缩（聚合将处于约束边界的输出合并为处于内部的输出）。作者证明，任何聚合操作必须至少实现其中一种机制才能扩展可引出性，并且强化版本的这些机制共同构成了聚合扩展可引出性的充分必要条件。

主要结论是，聚合的力量本质上依赖于这些机制，它们使得复合AI系统能够克服单一模型在提示工程和模型能力上的局限。论文通过一个LLM参考文献生成任务的实证案例，展示了这三种机制的实际表现。这项工作为理解何时聚合相同模型副本能为系统设计者带来益处提供了理论基础和概念框架。
