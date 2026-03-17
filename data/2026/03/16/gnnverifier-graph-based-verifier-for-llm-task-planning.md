---
title: "GNNVerifier: Graph-based Verifier for LLM Task Planning"
authors:
  - "Yu Hao"
  - "Qiuyu Wang"
  - "Cheng Yang"
  - "Yawen Li"
  - "Zhiqiang Zhang"
  - "Chuan Shi"
date: "2026-03-16"
arxiv_id: "2603.14730"
arxiv_url: "https://arxiv.org/abs/2603.14730"
pdf_url: "https://arxiv.org/pdf/2603.14730v1"
github_url: "https://github.com/BUPT-GAMMA/GNNVerifier"
categories:
  - "cs.LG"
tags:
  - "任务规划"
  - "规划验证"
  - "图神经网络"
  - "结构化推理"
  - "错误定位与修正"
  - "数据合成"
relevance_score: 8.5
---

# GNNVerifier: Graph-based Verifier for LLM Task Planning

## 原始摘要

Large language models (LLMs) facilitate the development of autonomous agents. As a core component of such agents, task planning aims to decompose complex natural language requests into concrete, solvable sub-tasks. Since LLM-generated plans are frequently prone to hallucinations and sensitive to long-context prom-pts, recent research has introduced plan verifiers to identify and correct potential flaws. However, most existing approaches still rely on an LLM as the verifier via additional prompting for plan review or self-reflection. LLM-based verifiers can be misled by plausible narration and struggle to detect failures caused by structural relations across steps, such as type mismatches, missing intermediates, or broken dependencies. To address these limitations, we propose a graph-based verifier for LLM task planning. Specifically, the proposed method has four major components: Firstly, we represent a plan as a directed graph with enriched attributes, where nodes denote sub-tasks and edges encode execution order and dependency constraints. Secondly, a graph neural network (GNN) then performs structural evaluation and diagnosis, producing a graph-level plausibility score for plan acceptance as well as node/edge-level risk scores to localize erroneous regions. Thirdly, we construct controllable perturbations from ground truth plan graphs, and automatically generate training data with fine-grained annotations. Finally, guided by the feedback from our GNN verifier, we enable an LLM to conduct local edits (e.g., tool replacement or insertion) to correct the plan when the graph-level score is insufficient. Extensive experiments across diverse datasets, backbone LLMs, and planners demonstrate that our GNNVerifier achieves significant gains in improving plan quality. Our data and code is available at https://github.com/BUPT-GAMMA/GNNVerifier.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在任务规划中因幻觉和长上下文敏感性而产生的不可靠问题，特别是现有验证方法难以检测跨步骤结构性错误的核心缺陷。

研究背景是，随着LLM发展为通用智能体，任务规划成为其核心组件，负责将复杂的自然语言请求分解为可执行的子任务序列。现有方法主要依赖LLM通过提示生成规划，但长上下文容易导致注意力分散和幻觉，产生看似合理但实际不可执行或内部不一致的计划。为此，先前研究引入了计划验证器来评估和修正计划，但现有验证器大多仍基于LLM，通过额外的提示进行计划审查或自我反思。

现有LLM基验证器的不足在于：一方面，它们容易被流畅的步骤描述所误导，将看似合理的叙述误判为正确执行；另一方面，许多失败源于跨步骤的结构性关系（如类型不匹配、缺失关键中间步骤或依赖关系断裂），这些错误难以通过孤立阅读步骤来检测和定位。

因此，本文要解决的核心问题是：如何超越依赖LLM进行文本级审查的传统验证范式，设计一种能够有效捕捉和诊断任务规划中结构性错误的验证方法。具体而言，论文提出了一种基于图的验证器（GNNVerifier），通过将计划表示为带有丰富属性的有向图，利用图神经网络（GNN）进行结构评估和诊断，从而识别LLM基验证器难以发现的深层逻辑不一致问题，并指导LLM进行精准的局部修正以提升规划质量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：LLM任务规划方法、验证器（Verifier）研究，以及图神经网络在规划中的应用。

在**LLM任务规划方法**方面，现有工作主要分为两类。一是“内在LLM规划”，即LLM利用自身能力直接生成子任务序列，典型方法包括CoT、ReAct、HuggingGPT等，它们通过提示工程引导分解；ToT、GoT等方法则通过生成多条轨迹进行探索，并让LLM自身担任评估者。二是“外部规划器集成”，即引入符号组件或小型神经网络处理复杂约束，例如将自然语言问题转化为PDDL形式化描述后使用经典求解器。本文提出的GNNVerifier属于外部集成范式，但区别于现有工作，它**专注于通过图结构显式建模子任务间的依赖与顺序关系**，而非直接进行符号推理或依赖LLM自评估。

在**验证器研究**方面，早期工作集中于数学、代码生成等可客观验证的领域，分为评估最终结果的ORMs和评估推理过程的PRMs。近期研究（如VersaPRM）将验证器扩展到开放域问答、规划等更具主观性的任务，并出现生成式验证器以提供自然语言反馈。在规划领域，已有工作（如VeriPlan）通过模型检查或迭代验证子任务一致性来提供修正反馈。然而，这些方法**大多忽视了计划图中结构依赖关系的关键作用**。本文的GNNVerifier则通过图神经网络进行结构评估与诊断，生成图级、节点级和边级的细粒度风险评分，从而提供更精准的结构感知反馈。

在**图神经网络应用**方面，已有研究（如GNN4Plan）指出LLM在准确识别计划图结构方面存在不足，并表明GNN可有效处理此类约束。本文在此基础上，**系统地将计划表示为属性丰富的有向图，并利用GNN进行结构评估与错误定位**，同时通过可控扰动自动生成训练数据，构建了一个可训练的、专用于计划验证的图神经网络验证器。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于图神经网络的验证器来解决LLM任务规划中的幻觉和结构错误问题。其核心方法是将任务计划表示为带属性的有向图，并利用GNN进行结构评估和诊断，从而提供全局质量评分和局部风险定位，最终引导LLM进行局部修正。

整体框架包含四个主要组件：首先，将LLM生成的计划（子任务序列和对应工具）转换为带丰富节点和边属性的有向计划图。节点代表工具调用实例，包含工具语义、步骤语义、工具I/O类型编码以及步骤-工具对齐特征；边代表执行顺序和依赖关系，包含I/O兼容性、成对共现统计和多步关系特征。其次，使用一个边感知的定向GNN对计划图进行编码，通过多层消息传递聚合邻域信息，最终输出图级、节点级和边级的风险分数。图级分数评估整体合理性，节点级分数标识错误工具选择，边级分数检测不可靠的过渡（如缺失中间步骤）。第三，为了解决训练数据中细粒度标注的缺乏，论文提出基于扰动的监督方法：通过对真实计划图进行可控扰动（如替换工具、删除或压缩步骤）自动生成带有图级、节点级和边级软标签的训练数据。最后，当图级分数低于阈值时，利用GNN验证器输出的高风险节点和边集合来引导LLM进行受限的局部编辑（如工具替换或步骤插入），而非重新生成整个计划，从而高效修正错误。

创新点在于：1) 首次将计划验证形式化为图结构评估问题，利用GNN捕捉跨步骤的结构关系错误（如类型不匹配、缺失中间步骤），克服了传统LLM验证器易受叙事误导的局限；2) 设计了丰富的节点和边特征，特别是步骤-工具对齐特征和多步关系特征，以增强语义和结构感知；3) 提出了基于扰动的自动数据生成方法，无需人工标注即可获得细粒度监督信号；4) 实现了验证与修正的闭环，通过局部化诊断约束LLM的修正范围，提升修正效率与准确性。

### Q4: 论文做了哪些实验？

论文在Task-Bench（包含HuggingFace、Multimedia、DailyLife三个数据集）和UltraTool两个任务规划基准上进行了广泛的实验。实验设置遵循GNN4Plan的公开数据划分，每个数据集使用3000个实例训练，500个实例测试，并留出10%训练集作为验证集。评估指标包括节点F1分数（n-F1）、链接F1分数（l-F1）和准确率（Acc）。实验采用GPT-4o和Qwen3-235B-A22B-Instruct-2507作为主干大语言模型，并应用于三种规划方法：Direct、ReAct和GNN4Plan。对比基线包括仅LLM的自我精炼方法（Refine）、基于LLM的验证助手（VeriCoder）以及结合外部验证器的VeriPlan。

主要结果显示，GNNVerifier在所有规划器和数据集上均显著提升了计划质量。例如，在HuggingFace数据集上，使用Direct规划器时，完整GNNVerifier（Full）将n-F1从原始的79.60%提升至82.82%，l-F1从55.27%提升至60.71%，Acc从34.20%大幅提升至43.80%。在Multimedia数据集上，使用ReAct规划器时，完整模型将n-F1从86.50%提升至90.46%，l-F1从64.53%提升至73.73%，Acc从48.80%提升至59.00%。消融实验验证了各关键组件（如GNN模块、两阶段训练、节点/边特征、各层级反馈）的有效性，表明完整模型性能最优。此外，验证引导的校正有效减少了各类计划错误。

### Q5: 有什么可以进一步探索的点？

该论文提出的GNNVerifier虽然有效，但其局限性也为未来研究提供了多个方向。首先，其图结构表示和GNN诊断能力高度依赖于预定义的节点与边属性（如工具类型、依赖关系），这限制了其对开放式、非结构化任务（如创造性写作或开放式问题解决）的泛化能力。未来可探索更灵活的动态图构建方法，或结合符号推理来增强语义理解。

其次，训练数据的生成依赖于对真实图的人为扰动，这可能无法覆盖现实场景中LLM规划的全部错误模式，尤其是涉及复杂因果链或隐性约束的任务。未来可考虑利用LLM自身模拟错误生成，或构建更大规模、多领域的基准测试集。

此外，当前验证与修正过程是分离的：GNN负责诊断，LLM负责修正。未来可研究更紧密的闭环交互，例如让GNN直接生成修正建议的图结构提示，或开发端到端的联合训练框架，使验证器能指导规划器的内部表示学习，从源头减少错误。

最后，该方法目前主要针对工具调用类任务，未来可扩展至多模态任务规划（如图像编辑或机器人操作），其中图节点需包含视觉或物理状态信息，这对图表示和验证都提出了新挑战。

### Q6: 总结一下论文的主要内容

该论文针对LLM任务规划中生成的计划常存在幻觉和结构不一致问题，提出了一种基于图神经网络的验证器GNNVerifier。核心贡献在于用图结构表示任务计划，以节点表示子任务、边表示执行顺序和依赖关系，并利用GNN进行结构评估与诊断，输出图级可信度分数及节点/边级风险分数，从而定位错误区域。方法上，通过从真实计划图构建可控扰动自动生成训练数据，并结合GNN反馈引导LLM对高风险区域进行局部修正（如工具替换或插入）。实验表明，该方法在多种数据集、骨干LLM和规划器上均显著提升了计划质量，相比基线在节点、边和图级指标上分别取得2.13%、9.22%和15.96%的相对提升，有效解决了传统LLM验证器易受流畅叙述误导、难以检测跨步骤结构缺陷的局限性。
