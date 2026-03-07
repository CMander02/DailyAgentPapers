---
title: "DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science"
authors:
  - "Fan Shu"
  - "Yite Wang"
  - "Ruofan Wu"
  - "Boyi Liu"
  - "Zhewei Yao"
date: "2026-02-27"
arxiv_id: "2602.24288"
arxiv_url: "https://arxiv.org/abs/2602.24288"
pdf_url: "https://arxiv.org/pdf/2602.24288v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Code & Software Engineering"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Code & Software Engineering"
  domain: "Data Science & Analytics"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "gpt-4o-mini, Qwen3-32B, Qwen3-4B"
  key_technique: "DARE-bench"
  primary_benchmark: "DARE-bench"
---

# DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science

## 原始摘要

The fast-growing demands in using Large Language Models (LLMs) to tackle complex multi-step data science tasks create an emergent need for accurate benchmarking. There are two major gaps in existing benchmarks: (i) the lack of standardized, process-aware evaluation that captures instruction adherence and process fidelity, and (ii) the scarcity of accurately labeled training data. To bridge these gaps, we introduce DARE-bench, a benchmark designed for machine learning modeling and data science instruction following. Unlike many existing benchmarks that rely on human- or model-based judges, all tasks in DARE-bench have verifiable ground truth, ensuring objective and reproducible evaluation. To cover a broad range of tasks and support agentic tools, DARE-bench consists of 6,300 Kaggle-derived tasks and provides both large-scale training data and evaluation sets. Extensive evaluations show that even highly capable models such as gpt-o4-mini struggle to achieve good performance, especially in machine learning modeling tasks. Using DARE-bench training tasks for fine-tuning can substantially improve model performance. For example, supervised fine-tuning boosts Qwen3-32B's accuracy by 1.83x and reinforcement learning boosts Qwen3-4B's accuracy by more than 8x. These significant improvements verify the importance of DARE-bench both as an accurate evaluation benchmark and critical training data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）在应对复杂、多步骤的数据科学任务时，缺乏准确且全面的评估基准的问题。随着LLM被越来越多地用于辅助或自动化数据科学工作流（如机器学习建模），业界急需一个能有效衡量模型在此领域能力的评测标准。

现有基准存在两大不足：首先，它们通常缺乏标准化的、过程感知的评估方法。这意味着现有评测往往只关注最终输出结果的正确性，而忽略了模型在完成任务过程中是否严格遵循了用户指令、是否保持了正确的步骤和逻辑（即指令遵循和过程保真度）。其次，用于训练和微调模型的高质量、带准确标注的数据科学任务数据非常稀缺。

因此，本文的核心问题是填补上述空白，具体而言是构建一个名为DARE-bench的基准。该基准专门为评估LLM在机器学习建模和数据科学领域的指令遵循能力而设计。它通过提供大量具有可验证标准答案的任务，确保评估的客观性和可复现性，并同时为模型训练提供关键的大规模数据支持，以推动模型在该领域性能的提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：数据科学任务评测基准、指令遵循评估方法，以及用于模型训练的数据集构建工作。

在**数据科学任务评测基准**方面，现有工作如DS-1000、CodeXGLUE等主要关注代码生成或特定数据操作，但往往缺乏对完整机器学习建模流程（如数据预处理、特征工程、模型训练与评估）的标准化、过程感知的评估。DARE-bench则专门针对数据科学全流程，强调“指令遵循”和“过程保真度”，且所有任务均提供可验证的真实答案，确保了客观可复现的评估，这与依赖人工或模型评分的主观基准有本质区别。

在**指令遵循评估方法**上，相关工作如IFEval、MT-Bench等评估通用指令遵循能力，但未深入数据科学领域的具体步骤合规性。DARE-bench通过设计具有明确步骤和可验证中间状态的任务，能更精细地评估模型对复杂数据科学指令的遵循程度。

在**训练数据集构建**方面，许多基准（如HumanEval）主要提供评测集，缺乏大规模、高质量的标注训练数据。DARE-bench的突出贡献是同时提供了大规模、源自真实Kaggle平台的任务数据用于训练和评估，直接支持模型微调，并验证了其数据能显著提升模型在数据科学任务上的性能，这弥补了该领域高质量训练数据稀缺的缺口。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为DARE-bench的新型基准测试来解决现有评估体系中的两大核心缺口。其核心方法是创建一个具有可验证真实标签、覆盖广泛数据科学任务、并支持工具使用的标准化评估框架。

整体框架上，DARE-bench包含6,300个从Kaggle平台衍生的任务，这些任务被精心设计为涵盖数据科学的多个环节，特别是机器学习建模任务。其架构设计的关键在于摒弃了依赖主观人工或模型评判的传统方式，而是为所有任务提供了客观、可验证的“地面真值”（ground truth）。这确保了评估过程的客观性和可重复性，直接解决了“缺乏标准化、过程感知评估”的问题。

主要模块/组件包括大规模的训练数据集和评估集。训练数据的提供旨在解决“缺乏准确标注训练数据”的缺口。这些数据不仅用于评估，更重要的是可以作为高质量的监督微调（SFT）和强化学习（RL）的训练资源，从而直接提升模型在复杂、多步骤数据科学任务上的指令遵循和过程保真度。

创新点主要体现在三个方面：一是**过程感知的客观评估**，通过可验证的真实结果来量化模型对指令的遵循程度和建模过程的正确性；二是**数据来源与规模**，从真实数据科学社区（Kaggle）大规模衍生任务，确保了任务的现实相关性和广度；三是**训练与评估一体化**，该基准同时提供了能显著提升模型性能的训练数据，验证了其作为关键训练资源的双重价值。实验表明，利用其数据进行微调能带来模型性能的倍数级提升，这强有力地证明了该基准在准确评估和有效训练两方面的有效性。

### Q4: 论文做了哪些实验？

论文构建了DARE-bench基准，包含6,300个源自Kaggle的数据科学任务，涵盖数据预处理、特征工程、模型构建与评估等环节。实验设置上，该基准所有任务均提供可验证的真实答案，确保了评估的客观性和可复现性。数据集分为大规模训练集和评估集，支持智能体工具的使用。

对比方法上，论文评估了包括gpt-4o-mini在内的多个先进大语言模型。主要结果显示，即使是高性能模型在数据科学任务，尤其是机器学习建模任务上表现也欠佳。例如，gpt-4o-mini在相关任务中表现挣扎。

关键数据指标方面，论文通过微调显著提升了模型性能：使用DARE-bench训练任务进行监督微调，使Qwen3-32B的准确率提升了1.83倍；而通过强化学习微调，Qwen3-4B的准确率提升了超过8倍。这些结果验证了DARE-bench作为评估基准和训练数据的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的DARE-bench虽然有效填补了数据科学领域LLM评估的空白，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，其任务主要基于Kaggle竞赛，可能无法全面覆盖真实业务场景中更复杂、模糊或动态变化的数据科学问题，未来可纳入更多行业特定任务以提升泛化性。其次，基准侧重于结果的可验证性，但对推理过程的中间步骤（如特征工程或模型选择背后的逻辑）评估不足，未来可引入过程跟踪或可解释性指标来细化评估维度。此外，论文未深入探讨多智能体协作场景下的性能，而实际数据科学工作常涉及团队分工，因此可探索基于DARE-bench的多智能体协同任务框架。最后，当前训练数据虽规模大，但可能缺乏对新兴技术（如自动机器学习AutoML）的覆盖，未来可持续更新任务库以保持前沿性。结合这些方向，研究者可进一步开发混合评估方法，结合自动化指标与人类专家评判，以更全面衡量LLM在复杂数据科学工作流中的实用价值。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型在复杂多步骤数据科学任务中缺乏标准化评估基准的问题，提出了DARE-bench。现有基准主要存在两大不足：一是缺乏能捕捉指令遵循和过程保真度的标准化、过程感知评估；二是缺乏准确标注的训练数据。为此，作者构建了一个包含6,300个源自Kaggle任务的数据集，涵盖广泛的数据科学任务并支持智能体工具使用，其所有任务均具备可验证的真实答案，确保了评估的客观性和可复现性。

论文的核心贡献在于提供了一个兼具大规模训练集和评估集的基准，用于评估LLMs在机器学习建模和数据科学指令遵循方面的能力。方法上，该基准不依赖人工或模型评判，而是基于客观真实标签进行评估。主要结论显示，即使是GPT-4-mini等高性能模型在该基准上表现也欠佳，尤其在建模任务中；而利用DARE-bench的训练数据进行微调（如监督微调和强化学习）能大幅提升模型性能，例如Qwen3-4B经强化学习后准确率提升超过8倍。这验证了DARE-bench作为精准评估基准和关键训练数据的重要价值。
