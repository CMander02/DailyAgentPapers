---
title: "Agentic-imodels: Evolving agentic interpretability tools via autoresearch"
authors:
  - "Chandan Singh"
  - "Yan Shuo Tan"
  - "Weijia Xu"
  - "Zelalem Gero"
  - "Weiwei Yang"
  - "Michel Galley"
  - "Jianfeng Gao"
date: "2026-05-05"
arxiv_id: "2605.03808"
arxiv_url: "https://arxiv.org/abs/2605.03808"
pdf_url: "https://arxiv.org/pdf/2605.03808v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent-面向可解释性"
  - "AutoML"
  - "LLM-智能体交互"
  - "数据科学智能体"
  - "可解释性"
  - "Auto-Research循环"
  - "工具演化"
relevance_score: 7.5
---

# Agentic-imodels: Evolving agentic interpretability tools via autoresearch

## 原始摘要

Agentic data science (ADS) systems are rapidly improving their capability to autonomously analyze, fit, and interpret data, potentially moving towards a future where agents conduct the vast majority of data-science work. However, current ADS systems use statistical tools designed to be interpretable by humans, rather than interpretable by agents. To address this, we introduce Agentic-imodels, an agentic autoresearch loop that evolves data-science tools designed to be interpretable by agents. Specifically, it develops a library of scikit-learn-compatible regressors for tabular data that are optimized for both predictive performance and a novel LLM-based interpretability metric. The metric measures a suite of LLM-graded tests that probe whether a fitted model's string representation is "simulatable" by an LLM, i.e. whether the LLM can answer questions about the model's behavior by reading its string output alone. We find that the evolved models jointly improve predictive performance and agent-facing interpretability, generalizing to new datasets and new interpretability tests. Furthermore, these evolved models improve downstream end-to-end ADS, increasing performance for Copilot CLI, Claude Code, and Codex on the BLADE benchmark by up to 73%

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有自主数据科学（ADS）系统中存在的一个核心矛盾：尽管ADS系统正快速提升自主分析、拟合和解释数据的能力，但它们所使用的统计工具仍然是面向人类可解释性设计的（如可视化或可干预组件），而非面向AI代理可解释性。这使得代理在解析模型行为时遇到困难（例如难以准确解析可视化、理解系数含义），导致分析不可靠、分析选择不透明。现有的可解释机器学习文献虽提供了决策树、广义加性模型等模型，并通常通过人类实验来量化可解释性，但这无法满足代理环境的需求。本文提出一种名为“Agentic-imodels”的自主研究循环，旨在自动化设计一种新型“面向代理可解释”的数据科学工具。核心创新在于：用一套基于LLM的可解释性评估指标取代人类实验，该指标通过一系列LLM评分测试（如模拟模型预测、特征效应和反事实），衡量代理仅通过模型的字符串表示就能“模拟”其行为的能力。最终目标是在保证预测性能的同时，显著提升模型对LLM代理的“可模拟性”，从而改进代理在端到端数据分析中的表现。

### Q2: 有哪些相关研究？

**方法类**：与可解释机器学习相关，如决策树、规则列表、广义加性模型（GAMs）及稀疏线性模型（imodels、interpretML等库），以及将LLM用于构建可解释模型的工作（如Aug-imodels通过手工设计方法从LLM构建可解释模型，或训练Transformer直接生成可解释模型）。本文与这些方法的区别在于，本文不依赖人类设计的可解释性标准，而是通过自主研究循环让智能体直接优化模型的“智能体可解释性”（基于LLM的模拟性评分），从而自动发现新的、对智能体更友好的模型类。

**应用与评测类**：与智能体数据科学（ADS）相关，主要关注评测智能体的端到端数据分析能力（如BLADE基准）并记录失败模式（如p-hacking、缺乏检查）。本文的独特之处在于，不是将智能体视为现有可解释性方法的使用者，而是将其视为方法的设计者，通过优化LLM可解释性指标来提升下游ADS任务性能（Copilot CLI、Claude Code、Codex），实现高达73%的改进。

**自动化发现类**：与自主研究（autoresearch）相关，如AlphaEvolve通过循环生成和优化代码以追求可验证目标，以及通过进化“技能”（文本提示）改善智能体性能的工作。本文继承该范式但将其应用于特定领域——发现对智能体可解释的机器学习模型，并通过泛化实验验证了所得模型在新数据集和测试上的有效性。

### Q3: 论文如何解决这个问题？

Agentic-imodels 通过一个基于智能体的自动研究循环（agentic autoresearch loop）来解决现有数据分析系统对智能体不可解释的问题。核心方法是让编码智能体（如 Claude Code）迭代地探索、构建和优化模型类，同时优化预测性能和一种新颖的、基于 LLM 的可解释性指标。

整体框架是一个迭代循环：智能体编辑模型代码 → 在新数据集和合成数据上评估模型性能和可解释性 → 检查指标是否提升 → 记录结果 → 重复。每个模型类都是一个兼容 scikit-learn 的 Python 类，包含 fit、predict 和 __str__ 方法。

主要模块包括三个部分。**预测性能评估**：在一系列表格回归数据集上计算测试集 RMSE，并通过排名取平均来避免噪声。**智能体可解释性指标**：这是核心创新点。该指标通过 200 个 LLM 评分的测试来衡量模型的可解释性。每个测试首先生成已知真实函数的合成数据，让模型拟合后，仅向 LLM 提供模型的 __str__ 输出（如系数方程或决策路径），然后询问关于模型预测的定量问题（如“输入为 x0=2, x1=0, x2=0 时预测值是多少？”），最后根据真实结果判断回答是否准确。测试覆盖了特征归因、点模拟、敏感性分析、反事实推理、结构理解和复杂函数模拟六大类别，并分为开发集和保留集。**编码智能体**：该智能体被提示需创造性地从零构建新模型，而非导入已知模型调参。它通过 CSV 文件记忆每次迭代的模型名称、思路和指标，并能持续运行直到手动停止。

其创新点在于：1）首次提出并度量面向智能体的可解释性，而非传统的人为可解释性；2）自动发现既准确又对 LLM 透明的模型类；3）这些进化出的模型在下游 BLADE 基准测试中，将 Copilot CLI、Claude Code 和 Codex 的性能提升了最多 73%。

### Q4: 论文做了哪些实验？

论文在65个回归数据集（OpenML TabArena的7个数据集和PMLB的58个数据集）上评估了预测性能，使用80%-20%训练测试划分，子采样至最多1000个样本和50个特征。对比了16个基线模型，涵盖线性（OLS、Ridge、Lasso）、树（DT、HSTree）、加性（PyGAM、EBM）、规则（FIGS、RuleFit）和黑箱（RF、GBM、MLP、TabPFN）五种类型。主要实验包括：1）使用Claude Code和Codex两个编码代理，在三种推理努力水平下运行Agentic-imodels环路，生成467个演化模型；2）在157个保留测试上评估代理可解释性分数，发现演化模型在预测性能和代理可解释性上均实现帕累托改进，例如Claude Code的HingeEBM（5bag）在归一化排名（越低越好）为0.19时，代理可解释性分数达0.71，而性能最好的基线TabPFN排名0.16但可解释性仅0.17；3）在BLADE基准的13个数据集上进行端到端ADS评估，为四个AI代理（Copilot CLI、Claude Code、Codex）提供演化模型后，所有代理的性能均提升，Copilot Gemini提升72.5%（13/13数据集改善），Claude Code提升32.3%，Codex提升7.9%。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来方向主要围绕评估方法、成本和应用广度展开。首先，当前的LLM-as-Judge评估可能存在偏差和奖励作弊问题，未来需要设计更鲁棒的代理可解释性测试，例如通过API隐藏测试问题以避免代理直接“看到”答案，并探索更精确的代理行为模拟器来替代人工评估。其次，代理循环的LLM API调用成本高昂，但随推理效率提升会逐步缓解。在应用拓展上，应将该框架从回归任务推广到分类、时间序列、文本数据及更大规模数据集，并针对更通用的工具（如文本解释流水线、因果干预）进行优化。此外，未来可研究将这套测试套件作为优化目标，直接改进现有模型包而无需重新架构。最重要的是，将演化模型融入真实世界的代理工作流（如科学发现管道），验证其在复杂分析中的迁移效果；同时，考虑将框架改造为优化人机协作，而非仅针对代理或人类单独优化。随着LLM解析结构化模型能力的增强，该方法有望实现超人类的数据洞察。

### Q6: 总结一下论文的主要内容

该论文聚焦于为AI代理设计可解释性工具。传统数据科学工具以人类为中心，输出可视化内容，但AI代理难以有效解析。为此，作者提出Agentic-imodels，一个自动研究循环，其核心是让编码代理（如Claude Code）迭代修改一个Python类，以同时优化预测性能和一种新型的、基于LLM的可解释性指标。该指标通过一系列LLM评分测试来衡量代理是否能仅通过模型的字符串表示来“模拟”其行为（如预测、特征效应）。实验表明，该循环在65个表格数据集上发现的模型类成功推进了Pareto前沿，不仅在新数据集和测试上泛化良好，还将Agent（如Copilot CLI、Claude Code）在BLADE端到端基准上的性能提升了8%-73%。此工作重新定义了AI时代的可解释性方向，即设计服务于代理而非人类的模型，对自动化数据科学具有重要推动意义。
