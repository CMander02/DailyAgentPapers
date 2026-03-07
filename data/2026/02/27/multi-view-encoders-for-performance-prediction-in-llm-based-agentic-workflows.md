---
title: "Multi-View Encoders for Performance Prediction in LLM-Based Agentic Workflows"
authors:
  - "Patara Trirat"
  - "Wonyong Jeong"
  - "Sung Ju Hwang"
date: "2025-05-26"
arxiv_id: "2505.19764"
arxiv_url: "https://arxiv.org/abs/2505.19764"
pdf_url: "https://arxiv.org/pdf/2505.19764v2"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Learning & Optimization"
  - "Architecture & Frameworks"
relevance_score: 8.0
taxonomy:
  capability:
    - "Learning & Optimization"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Agentic Predictor with multi-view workflow encoding and cross-domain unsupervised pretraining"
  primary_benchmark: "N/A"
---

# Multi-View Encoders for Performance Prediction in LLM-Based Agentic Workflows

## 原始摘要

Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks, but optimizing LLM-based agentic systems remains challenging due to the vast search space of agent configurations, prompting strategies, and communication patterns. Existing approaches often rely on heuristic-based tuning or exhaustive evaluation, which can be computationally expensive and suboptimal. This paper proposes Agentic Predictor, a lightweight predictor for efficient agentic workflow evaluation. Agentic Predictor is equipped with a multi-view workflow encoding technique that leverages multi-view representation learning of agentic systems by incorporating code architecture, textual prompts, and interaction graph features. To achieve high predictive accuracy while significantly reducing the number of required workflow evaluations for training a predictor, Agentic Predictor employs cross-domain unsupervised pretraining. By learning to approximate task success rates, Agentic Predictor enables fast and accurate selection of optimal agentic workflow configurations for a given task, significantly reducing the need for expensive trial-and-error evaluations. Experiments on a carefully curated benchmark spanning three domains show that our predictor outperforms several strong graph-based baselines in both predictive accuracy and workflow utility, highlighting the potential of performance predictors in streamlining the design of LLM-based agentic workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体工作流在自动化设计和优化过程中面临的核心瓶颈问题：评估候选工作流配置的性能成本过高。

研究背景是，LLM驱动的智能体系统能够执行复杂的多步骤任务，但其设计通常依赖手动工程或自动搜索方法。现有方法，特别是自动化搜索方法，为了在庞大的配置空间（包括智能体架构、提示策略和交互模式）中找到最优方案，需要对大量候选工作流进行迭代生成和评估。这种评估通常依赖于昂贵的、基于实际执行或LLM API调用的“试错”式验证，导致计算成本极高、耗时漫长，严重限制了智能体系统的快速开发和部署。

现有方法的不足主要体现在两个方面：一是**工作流异质性**，即工作流在结构、行为和语义上差异巨大，细微的配置变化可能导致性能显著不同，这使得构建一个统一的预测模型非常困难；二是**标注数据稀缺**，因为通过实际执行来获取工作流的性能标签（如成功率）成本过高，导致可用于监督训练的高质量数据极少，形成了数据瓶颈。

因此，本文要解决的核心问题是：如何**高效且准确地预测LLM智能体工作流的性能**，从而避免对每个候选配置都进行昂贵的实际评估。为此，论文提出了名为Agentic Predictor的轻量级预测器框架。其核心思路是引入一个基于学习的预测模型，通过多视图编码技术（融合代码架构、文本提示和交互图特征）来表征异构的工作流，并采用跨领域无监督预训练来缓解标注数据不足的问题，最终实现对工作流成功率的快速近似估计，从而显著加速最优工作流配置的搜索与选择过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**基于LLM的智能体工作流自动生成**和**用于神经架构搜索的性能预测器**。

在**智能体工作流自动生成**方面，现有工作主要分为两类。一类是采用静态或预定义多智能体结构的框架，如MetaGPT、ChatDev、AgentVerse和LLM-Debate，它们通常依赖固定的协作模式，适应性有限。另一类是旨在优化工作流结构的方法，如GPTSwarm、G-Designer、DyLAN、ADAS、AFlow和AgentSquare，它们通过强化学习、动态选择或利用大模型迭代生成等方式来优化工作流。然而，这些方法通常需要进行大量昂贵的LLM调用和试错评估。与这些工作不同，本文提出的Agentic Predictor并非直接生成或优化工作流，而是作为一个**轻量级性能预测器**，旨在快速评估候选工作流的性能，从而大幅减少对 exhaustive LLM 评估的依赖。具体而言，本文与近期同样关注预测的FLORA-Bench（使用单视图图神经网络）和MAS-GPT（微调LLM直接生成工作流）等方法存在显著区别，主要体现在采用了**多视图编码**（融合图拓扑、代码和提示）、**跨领域无监督预训练**以缓解标注数据稀缺，以及**轻量级高效预测**这三个方面。

在**性能预测器**方面，研究灵感来源于**神经架构搜索**领域。该领域已发展出多种性能预测技术来降低评估候选架构的成本，例如PRE-NAS的预测辅助进化策略、BRP-NAS的图卷积网络、CAP的上下文感知自监督学习以及FlowerFormer的流感知图变换器。这些方法的共同趋势是强调学习更具信息量的表征以指导搜索。本文借鉴了这一核心思想，将性能预测引入智能体工作流领域，并从**表征中心**的视角出发，通过多视图表征学习来实现对工作流空间的准确性能估计和高效探索。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Agentic Predictor的轻量级预测器来解决LLM智能体工作流性能预测问题，其核心在于避免对大量工作流配置进行昂贵的试错式LLM调用评估。该方法的核心架构与关键技术如下：

**整体框架**：Agentic Predictor是一个端到端的预测模型，其输入是智能体工作流配置W（定义为包含智能体集合、边、系统提示和完整代码的有向无环图）和任务描述T，输出是预测的性能分数ê。框架主要包含两个阶段：首先通过多视图工作流编码器将异构的工作流信息编码为统一表示；随后，一个轻量级的性能预测器基于该表示进行监督学习。在标注数据稀缺时，框架还引入了跨领域无监督预训练阶段来提升编码器的泛化能力。

**核心方法：多视图工作流编码**
这是本工作的主要创新点。论文认为传统基于图的编码不足以捕捉智能体工作流的全部关键信号，因此提出了一个三视图编码方案：
1.  **图视图**：显式建模智能体之间的结构依赖和直接交互。使用图神经网络处理工作流DAG，但创新性地构建了三个共享节点和边集但节点特征不同的图：提示图（节点特征为智能体提示的嵌入）、代码图（节点特征为智能体关联的函数调用代码）和操作符图（节点特征为操作符类型和定义）。通过跨视图自注意力块和视图注意力池化模块，融合这三个图的节点信息，最终通过图读出得到图级别的表示Z_G。
2.  **代码视图**：隐式编码工作流整体代码C的程序级语义、控制逻辑、计算复杂度和工具使用模式。使用一个多层感知机对完整工作流代码进行编码，得到全局的代码表示Z_C。
3.  **提示视图**：捕获智能体角色、行为规范和全局上下文语义。同样使用一个MLP对完整的工作流指令提示进行整体编码，得到提示表示Z_P。

**关键技术：表示学习与预测**
- **聚合层**：将上述三个视图的表示Z_G, Z_C, Z_P进行拼接，并通过一个最终的MLP进行自适应融合，生成统一的工作流表示Z。
- **无监督预训练**：为解决标注数据稀缺问题，论文设计了包含重构损失和对比损失的多任务预训练目标。重构损失要求从潜在表示Z重建各视图的输入特征；对比损失则鼓励不同视图（如图与代码）之间相同工作流的表示相互靠近，而与批次内其他工作流的表示远离。这使编码器能在不接触性能标签的情况下学习到通用且丰富的表示。
- **性能预测器**：在获得预训练编码器后，冻结其参数或进行微调，并训练一个轻量级的预测器（如MLP）。该预测器以工作流表示Z和任务描述T的编码（通过一个任务编码器）的联合表示F作为输入，预测性能分数。训练使用有限的标注工作流-性能数据对。

**创新点总结**：
1.  **多视图编码**：首次针对LLM智能体工作流，系统性地整合了图结构、代码语义和提示文本三种互补且不同粒度的视图信息，克服了单一图表示的局限性。
2.  **跨视图注意力图编码**：在图视图中，创新地使用多图结构和跨视图注意力机制，动态学习不同视图特征对节点表示的贡献。
3.  **数据高效的训练策略**：通过结合重构与跨模态对比学习的无监督预训练，显著减少了对昂贵性能标签的依赖，提升了预测器在少量标注数据下的样本效率。
4.  **预测器引导的搜索**：训练好的预测器可以快速评估大量候选工作流配置，从而高效地引导搜索最优配置，替代了耗尽的试错评估。

### Q4: 论文做了哪些实验？

本文在精心构建的跨三个领域（代码生成、数学问题求解和一般推理）的基准测试上进行了全面实验。实验设置方面，使用了FLORA-Bench基准，该基准包含来自G-Designer和AFlow两个独立智能体框架的多样化工作流，涉及HumanEval、MBPP、GSM8K、MATH和MMLU五个数据集。数据按任务实例随机划分为训练集（80%）、验证集（10%）和测试集（10%）。

主要对比方法包括多种基于图的基线模型，例如图神经网络（GNN）的变体，以及少样本LLM-based工作流性能预测器。评估指标聚焦于预测准确率（Accuracy）和工作流效用（Utility），后者衡量模型预测的工作流排序与真实排序的一致性。

实验结果表明，所提出的Agentic Predictor在预测准确率和工作流效用方面均优于所有基线方法。具体关键数据包括：在代码生成（GD/AF框架）任务上，测试样本量分别为30,683/7,362；在数学问题求解任务上为12,561/4,059；在一般推理任务上为453,600/72,000。消融实验证实了多视图编码（结合代码架构、文本提示和交互图特征）和跨领域无监督预训练的有效性，后者在标注数据有限时尤其有助于保持预测质量。此外，模型在分布外偏移下也表现出较强的鲁棒性，并且显著优于少样本LLM预测器。

### Q5: 有什么可以进一步探索的点？

该论文提出的多视图编码器在性能预测上取得了进展，但仍存在一些局限性和可探索的方向。首先，其编码的视图（代码架构、文本提示、交互图）可能尚未完全覆盖影响智能体工作流性能的所有关键因素，例如外部工具调用的具体语义、执行过程中的动态状态变化或不同LLM底层能力的差异。未来研究可以引入更细粒度的视图，如工具API的详细描述、中间推理步骤的连贯性分析，或结合轻量级仿真来捕获动态交互模式。

其次，该方法依赖于跨领域无监督预训练来减少训练所需的评估次数，但其泛化能力在新领域或高度复杂的工作流中可能受限。可探索的方向包括设计更高效的小样本适应机制，或利用元学习让预测器快速适应未知任务分布。此外，当前预测目标仅为任务成功率，未来可扩展为多目标预测（如延迟、成本、鲁棒性），以支持多维度权衡优化。

结合见解，一个可能的改进思路是引入“可解释性视图”，通过分析工作流组件的关键失败模式（如工具调用错误、逻辑矛盾）来增强预测器的诊断能力，从而不仅预测性能，还能指导工作流迭代优化。另外，探索预测器与自动化配置搜索（如基于贝叶斯优化）的闭环结合，可能进一步提升智能体工作流的设计效率。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的智能体工作流优化难题，提出了一个名为Agentic Predictor的轻量级性能预测器。核心问题是：在庞大的智能体配置、提示策略和交互模式搜索空间中，如何高效、低成本地评估并选择最优的工作流配置，避免依赖计算开销巨大的启发式调优或穷举评估。

方法上，Agentic Predictor的核心创新在于多视图工作流编码技术。它通过融合代码架构、文本提示和交互图特征这三个视图，对智能体系统进行多视图表征学习，从而全面捕捉工作流特性。为了在保证高预测精度的同时大幅减少训练所需的真实工作流评估次数，该方法采用了跨领域无监督预训练策略。

主要结论与意义在于，实验表明，在涵盖三个领域的基准测试中，该预测器在预测准确性和工作流效用方面均优于多种基于图的基线方法。其核心贡献是首次将多视图表示学习与跨域预训练相结合，用于LLM智能体工作流的性能预测，为高效、自动化地设计和优化复杂智能体系统提供了一条新路径，显著减少了对昂贵试错评估的依赖。
