---
title: "Talking Trees: Reasoning-Assisted Induction of Decision Trees for Tabular Data"
authors:
  - "George Yakushev"
  - "Alina Shutova"
  - "Ivan Rubachev"
  - "Natalia Bereberdina"
  - "Renat Sergazinov"
date: "2025-09-25"
arxiv_id: "2509.21465"
arxiv_url: "https://arxiv.org/abs/2509.21465"
pdf_url: "https://arxiv.org/pdf/2509.21465v2"
categories:
  - "cs.LG"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "Data Science & Analytics"
  research_type: "New Method/Model"
attributes:
  base_model: "GPT-5, DeepSeek R1, GLM-4.5"
  key_technique: "agentic thought-action-observation loop with a toolkit for decision-tree construction and refinement"
  primary_benchmark: "N/A"
---

# Talking Trees: Reasoning-Assisted Induction of Decision Trees for Tabular Data

## 原始摘要

Tabular foundation models are becoming increasingly popular for low-resource tabular problems. These models compensate for small training datasets by pretraining on large volumes of data. The prior knowledge obtained via pretraining provides exceptional performance, but the resulting model becomes a black box that is difficult to interpret and costly to run inference on. In this work, we explore an alternative strategy that is both more lightweight and controllable: using reasoning-capable LLMs to induce decision trees for small tabular datasets in an agentic setup. We design a minimal set of tools for constructing, analyzing, and manipulating decision trees. Using these tools, an LLM agent combines its prior knowledge with the user-specified constraints and learning from data to create lightweight decision trees. We show that a single decision tree constructed via the agentic loop can be competitive with state-of-the-art black-box models on tabular benchmarks, while also providing a human-readable reasoning trace that can be checked for biases and data leaks. Additionally, we show the model can incorporate fairness and monotonicity constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决低资源表格数据预测任务中，模型的可解释性、可控性和部署成本之间的平衡问题。研究背景是，当前表格基础模型通过大规模预训练在小样本表格任务上表现出色，但这类模型本质上是黑箱，决策规则隐含在参数中，难以解释和验证，且推理时计算和内存开销较大。现有方法（如基于上下文学习的表格基础模型或直接使用大语言模型进行推理）虽然性能强大，但要么缺乏透明度，要么推理成本高昂，且难以灵活融入领域知识或业务约束。

本文的核心问题是：如何在小规模表格数据集上，构建一个既保持高性能，又具备可解释性、低部署成本，并能灵活融入用户约束的预测模型。为此，论文提出了一种替代策略：利用具备推理能力的大语言模型，以智能体循环的方式，引导决策树的归纳构建。该方法仅在训练时使用大语言模型，通过为其设计一套用于构建、分析和操作决策树的工具，使智能体能结合其先验知识、用户指定的约束以及从数据中学习，迭代地生成轻量级的决策树。最终得到的单棵决策树不仅推理成本极低（无需调用大语言模型），而且能提供可读的构建轨迹以供检查和调试，同时还能灵活纳入公平性、单调性等约束。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于推理时上下文学习的表格基础模型、基于训练时调优的LLM应用方法，以及直接与决策树交互的LLM方法。

第一类方法在推理时利用LLM的上下文学习能力处理表格数据，如TabLLM和TabuLa-8B通过直接提示进行预测，具有可引导性但每次预测都需LLM前向传播，计算成本高。更广泛的表格基础模型如TabPFN和TabICL将训练摊销到学习到的先验中，降低了单样本推理开销，但仍依赖上下文学习且整体可解释性有限。

第二类方法在模型学习阶段使用LLM，例如用于自动化特征工程（如CAAFE、OCTree和LLM-FE）或数据清洗。这些工作能生成可解释的特征，但主要在特征层面可解释，且过程通常不可引导（即难以融入用户约束）。

第三类研究与本文最相关，探索LLM与决策树的直接交互。早期工作让LLM根据问题描述零样本构建决策树，而DeLTa等方法使用LLM编辑随机森林的决策规则并拟合纠错层。与这些工作相比，本文提出了一种更通用、以智能体（agentic）为核心的方法：不是让LLM遵循固定流程，而是为其提供一套工具，使其能在迭代中结合数据和领域知识主动构建、分析和优化决策树。这使得本文方法不仅能生成完全可解释、推理轻量的决策树模型，还能灵活融入用户对公平性和单调性等的约束，在保持竞争力的同时提供了可追溯的推理过程。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大型语言模型（LLM）的智能体（Agent）框架，以迭代、可控的方式诱导决策树，从而解决小样本表格数据建模中黑箱模型可解释性差、推理成本高的问题。其核心方法是将决策树的学习过程重新定义为一项智能体任务，让LLM在工具辅助下逐步构建和优化树结构，而非一次性生成整个模型。

整体框架围绕一个LLM智能体展开，该智能体运行在一个自定义环境中，能够访问数据、预加载的软件包以及一套专门设计的树操作工具。智能体通过“思考-代码-观察”的循环（最多20个周期）与环境和工具交互，逐步完善决策树。这一过程轻量且高效，单棵树构建时间不超过10分钟，API成本低于0.3美元，并可并行化以集成学习。

关键技术体现在精心设计的一套用于树分析、构建和操作的工具集，这些工具封装在一个围绕`Tree`类的Python库中。主要工具模块包括：1) **查看树结构**：以文本形式显示树或子树，并包含可用于定位的节点ID；2) **剪枝子树**：将指定节点转换为叶节点，可通过节点ID或直接操作完成；3) **选择数据**：根据树在数据集上的运行结果，筛选出经过特定节点的样本；4) **嫁接子树**：用新的子树替换当前树中指定的节点。这些工具使得智能体能够执行精细的局部修改，例如测试假设、纠正错误，并基于数据反馈进行优化。

创新点在于将LLM的链式推理能力与传统的基于数据的决策树归纳过程相结合。智能体不仅利用其先验知识，还能结合用户指定的约束（如公平性、单调性）并从数据中学习。这种“智能体循环”允许模型以增量方式工作，通过假设检验和错误修正来提升性能。实验结果表明，该方法构建的单一决策树（如Ours [TabPFN+CART]）在多个表格基准测试中，其性能可与最先进的黑箱模型（如XGBoost、TabPFNv2）竞争，同时提供了可检查偏见和数据泄露的人类可读推理轨迹，并成功融入了约束条件。

### Q4: 论文做了哪些实验？

论文在低资源表格数据问题上进行了全面的性能评估和消融实验。实验设置方面，使用来自OpenML的tabarena-v0.1中所有17个样本量不超过2500的数据集（8个二分类、4个多分类、5个回归任务），采用5次标准分层划分（80%训练/20%验证），评估指标包括ROC AUC（二分类）、LogLoss（多分类）和RMSE（回归）。主要方法使用GPT-5作为智能体构建决策树，仅使用训练-验证集。

对比方法包括：传统表格方法（Scikit-Learn的CART决策树默认与调优版、XGBoost、TabM神经网络集成、TabPFN v2表格基础模型）和基于LLM的方法（OC-Tree、DeLTA）。关键结果显示：1）LLM构建的决策树在17个数据集中有16个超越调优CART，仅在UsedFiat500上略低0.1%；2）与黑盒模型相比，智能体决策树虽在多数任务上仍有差距（如XGBoost、TabPFN v2），但显著缩小了性能差异；3）用智能体决策树校正TabPFN v2预测可进一步提升性能；4）相比OC-Tree（在所有数据集上被超越）和DeLTA（在9/17数据集上优于其CART版本），本文方法表现更优。

消融实验涵盖：不同LLM骨干对比（GPT-5最优，Claude Opus 4.5接近）、无限制工具访问（性能提升但不及黑盒模型）、无树脚手架（性能下降且波动大）、无元数据（提供描述通常有益）、数据泄露测试（洗牌数据后性能降至基线）、无智能体循环（零次生成性能大幅下降）。关键指标示例：在Fitness数据集上，GPT-5的ROC AUC为0.818±0.017；无智能体时降至0.692±0.012。分析还显示智能体操作中约50%为探索分析与特征工程，直接树编辑不足10%。

### Q5: 有什么可以进一步探索的点？

该论文提出的方法虽然展示了利用LLM先验知识构建可解释决策树的潜力，但仍存在一些局限性和值得深入探索的方向。首先，其性能严重依赖于所选LLM的推理能力和先验知识质量，这可能导致结果不稳定且难以复现。其次，方法目前主要针对小规模数据集，其在大规模、高维表格数据上的可扩展性尚未得到验证，代理循环的计算成本可能很高。

未来研究可以从以下几个方向展开：一是**增强方法的鲁棒性与泛化能力**，例如通过集成多个LLM的决策或引入不确定性量化来减少对单一模型的依赖。二是**探索更高效的交互与学习机制**，比如将LLM的符号推理与传统的优化算法（如梯度提升）相结合，以平衡可解释性与性能。三是**扩展约束处理的广度与深度**，论文展示了处理公平性、单调性等约束的能力，未来可以研究如何动态整合更复杂、多目标的领域知识（如因果约束或时序依赖）。此外，**评估框架的完善**也至关重要，需要建立更全面的基准来量化这种“对话式”归纳在可解释性、偏差控制和计算效率方面的长期价值。最后，将此类方法部署到真实场景时，还需考虑其与现有MLOps管道的集成以及持续学习的能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种利用具备推理能力的大语言模型（LLM）以智能体（Agent）方式为小规模表格数据归纳决策树的新方法。其核心问题是：在数据资源有限时，如何构建既高性能又具备可解释性、且能融入用户约束的轻量级预测模型，以替代需要大量预训练、计算成本高且难以解释的表格基础模型黑箱。

方法上，作者设计了一套简洁的工具集，供LLM智能体调用，以支持决策树的构建、分析和修改。在一个智能体循环中，LLM结合其先验知识、用户指定的约束（如公平性、单调性）以及从数据中学习的信息，逐步推理并生成决策树。

主要结论和贡献在于：该方法生成的单一决策树在多个表格数据基准测试中，性能可与最先进的黑箱模型相竞争，同时提供了可人工检查推理过程、排查偏见和数据泄露的清晰决策路径。它成功地将高性能、强可解释性、用户约束融入以及轻量级部署结合在一个框架内，为低资源表格数据问题提供了一种可控且高效的替代方案。
