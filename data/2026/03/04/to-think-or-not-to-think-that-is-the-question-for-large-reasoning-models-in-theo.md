---
title: "To Think or Not To Think, That is The Question for Large Reasoning Models in Theory of Mind Tasks"
authors:
  - "Nanxu Gong"
  - "Haotian Li"
  - "Sixun Dong"
  - "Jianxun Lian"
  - "Yanjie Fu"
  - "Xing Xie"
date: "2026-02-11"
arxiv_id: "2602.10625"
arxiv_url: "https://arxiv.org/abs/2602.10625"
pdf_url: "https://arxiv.org/pdf/2602.10625v3"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Theory of Mind"
  - "Agent Reasoning"
  - "LLM Evaluation"
  - "Social Reasoning"
  - "Cognitive Skills"
relevance_score: 7.5
---

# To Think or Not To Think, That is The Question for Large Reasoning Models in Theory of Mind Tasks

## 原始摘要

Theory of Mind (ToM) assesses whether models can infer hidden mental states such as beliefs, desires, and intentions, which is essential for natural social interaction. Although recent progress in Large Reasoning Models (LRMs) has boosted step-by-step inference in mathematics and coding, it is still underexplored whether this benefit transfers to socio-cognitive skills. We present a systematic study of nine advanced Large Language Models (LLMs), comparing reasoning models with non-reasoning models on three representative ToM benchmarks. The results show that reasoning models do not consistently outperform non-reasoning models and sometimes perform worse. A fine-grained analysis reveals three insights. First, slow thinking collapses: accuracy significantly drops as responses grow longer, and larger reasoning budgets hurt performance. Second, moderate and adaptive reasoning benefits performance: constraining reasoning length mitigates failure, while distinct success patterns demonstrate the necessity of dynamic adaptation. Third, option matching shortcut: when multiple choice options are removed, reasoning models improve markedly, indicating reliance on option matching rather than genuine deduction. We also design two intervention approaches: Slow-to-Fast (S2F) adaptive reasoning and Think-to-Match (T2M) shortcut prevention to further verify and mitigate the problems. With all results, our study highlights the advancement of LRMs in formal reasoning (e.g., math, code) cannot be fully transferred to ToM, a typical task in social reasoning. We conclude that achieving robust ToM requires developing unique capabilities beyond existing reasoning methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型推理模型在心理理论任务上的表现，并试图解决一个核心问题：在形式推理领域（如数学、代码）表现出色的逐步推理能力，能否有效提升模型在社会认知任务（如心理理论）上的性能。

研究背景是，心理理论作为社会认知的基础，要求模型推断他人隐藏的心理状态（如信念、欲望），这对于自然社交交互至关重要。近年来，大型推理模型通过链式思维等逐步推理技术，在数学、编程等结构化领域取得了显著进展，这引发了一个重要疑问：这种强大的推理机制能否成功迁移到心理理论这类社会推理任务中？

现有方法的不足在于，尽管已有研究尝试将链式思维等推理策略应用于心理理论，但效果并不一致，甚至可能因引入推理而降低模型表现。当前研究多集中于方法层面的改进，缺乏从模型层面系统性地比较推理模型与非推理模型在心理理论任务上的性能差异，因此无法明确推理能力本身的有效性及其潜在问题。

本文要解决的核心问题正是填补这一空白：通过系统评估九种先进大型语言模型在三个代表性心理理论基准上的表现，探究推理模型是否真的优于非推理模型，并深入分析其失败的原因。研究发现，推理模型并未持续领先，有时甚至更差。论文揭示了三个关键问题：一是“慢思考崩溃”，即过长的推理反而损害性能；二是适度和自适应推理才有益；三是“选项匹配捷径”，即推理模型可能依赖选项匹配而非真正的逐步演绎。这些发现表明，形式推理的进步不能直接转化为社会推理能力的提升，要实现稳健的心理理论，需要发展超越现有推理方法的独特能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：心智理论能力评估和大推理模型评估。

在心智理论能力评估方面，相关研究主要围绕构建不同侧重点的评测基准展开。早期工作基于经典的“莎莉-安妮”测试，采用多项选择形式。后续研究不断拓展：ToMi通过程序化变化的叙事和系统性的查询来扩展ToM-bAbi；HI-TOM将信念推理推至四阶；FANTOM引入了对话介导的场景并针对“虚幻心智理论”问题；BigToM和OpenToM则拓宽了心理状态的分类，纳入感知、欲望和情绪。此外，还出现了领域特定的评估，如NegotiationToM将BDI推理融入多轮谈判对话，ToMBench追求近乎全面的ATOMS覆盖并采用双语构建以减少预训练污染。数据创建方法也在演进，如ExploreToM采用A*驱动多样化，ToMATO利用LLM间信息不对称的自博弈。本文选取了HiToM、ToMBench和ToMATO这三个基准进行综合评估，它们分别覆盖了高阶信念深度、广泛的心理状态分类和多样化的评估场景。

在大推理模型评估方面，相关研究主要关注LRMs在形式化领域的推理能力评测。数学推理基准包括竞赛风格和小学数学应用题集（如MATH、GSM8K）、视觉数学（MathVista）和图表推理（ChartQA）。逻辑推理数据集涵盖演绎和溯因（如ProofWriter、FOLIO）以及关系归纳压力测试（CLUTRR）。常识推理资源探究物理合理性和广泛知识（如WinoGrande、MMLU）。代码基准强调精确性和可执行性（如HumanEval、MBPP、SWE-bench）。此外，还有评估交互环境下多步规划和工具使用的网络/具身环境基准（如Mind2Web、ALFWorld）。本文与这些工作的关系在于，它系统地将LRMs评估的视角从上述形式推理领域转移到了心智理论这一社会推理典型任务上，旨在检验LRMs在形式推理上的进步是否能迁移到社会认知技能，并诊断其失败模式。

### Q3: 论文如何解决这个问题？

论文通过系统性的实验分析和设计干预方法来解决大型推理模型在心理理论任务中表现不佳的问题。核心方法是首先对九种先进的大型语言模型进行基准测试，比较推理模型与非推理模型在三个代表性ToM任务上的表现，发现推理模型并未持续优于非推理模型，有时甚至更差。基于此，论文进行了细粒度分析，揭示了三个关键洞察：慢思考崩溃现象（回答越长准确率越低，更大的推理预算反而损害性能）、适度自适应推理的益处（限制推理长度可缓解失败，而不同的成功模式表明需要动态适应），以及选项匹配捷径问题（移除多项选择选项后推理模型表现显著提升，表明其依赖选项匹配而非真正演绎）。

整体框架包括评估、分析和干预三个阶段。主要模块包括基准测试集（涵盖三类ToM任务）、模型对比组（推理与非推理模型）、细粒度分析工具（如响应长度与准确率关联分析、选项移除实验），以及两种干预方法：慢到快自适应推理（S2F）和思考到匹配捷径预防（T2M）。S2F通过动态调整推理步骤长度来平衡深度与效率，T2M则通过修改任务格式（如隐藏选项）强制模型进行内在推理，避免依赖表面匹配。

创新点在于首次系统揭示了LRMs在形式推理与社会推理之间的能力转移局限，并通过实证分析指出了推理模型在ToM任务中的具体失效模式。干预方法不仅验证了问题根源，还提供了缓解路径，强调了开发超越现有推理方法的独特能力对于实现稳健ToM的必要性。

### Q4: 论文做了哪些实验？

论文在三个代表性心智理论（ToM）基准测试上，对九种先进大语言模型进行了系统实验。实验设置方面，模型分为推理模型（如GPT-4o-mini、DeepSeek-R1）和非推理模型（如GPT-4o、DeepSeek-V3），统一使用温度0、top-p 1和最大输出长度2048个token的参数。数据集包括：HiToM（测试多层递归信念推理深度）、ToMATO（评估对话情境中的心智状态推断）和ToMBench（全面覆盖信念、欲望等多种心智状态）。主要对比方法为直接比较同系列推理与非推理模型的性能。

实验结果显示，推理模型并未一致优于非推理模型，有时表现更差。关键数据指标包括：在ToMATO上，非推理模型在所有模型配对中均取得更高准确率；在HiToM上，非推理模型也赢得了多数比较；仅在ToMBench上推理模型保持优势。细粒度分析进一步揭示：随着响应长度增加，准确率显著下降（慢思考崩溃现象）；限制推理长度可缓解失败；移除多项选择选项后，推理模型表现明显提升，表明其依赖选项匹配而非真正推理。这些结果通过两种干预方法（慢到快自适应推理、思维到匹配捷径预防）得到了进一步验证。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来可进一步探索的方向包括：首先，开发自适应推理机制，使模型能根据任务复杂度动态切换“快思考”与“慢思考”模式，避免在心理理论任务中因过度推理导致性能下降。其次，需设计针对性的训练策略，减少模型对选择题选项的依赖，例如通过强化学习奖励基于真实推理而非选项匹配的决策。此外，可探索双系统架构的深度融合，如让直觉系统快速生成候选答案，再由推理系统进行验证，以平衡效率与准确性。最后，未来研究应拓展至更复杂的社交推理场景，验证现有干预方法（如S2F和T2M）的泛化能力，并开发能处理模糊性和视角漂移的稳健算法。

### Q6: 总结一下论文的主要内容

该论文系统研究了大型推理模型在心理理论任务中的表现，发现其在形式推理领域的优势并不能直接迁移到社会推理场景。核心问题是探究推理模型是否比非推理模型在ToM任务中表现更优，结论是否定的：推理模型不仅未能一致超越非推理模型，有时甚至表现更差。

论文通过对比九种先进大模型在三个代表性ToM基准上的表现，揭示了两个主要失败原因：一是“慢思考崩溃”现象，即过长的推理链反而导致准确率下降，更大的推理预算损害性能；二是“选项匹配捷径”问题，模型依赖选项匹配而非真正演绎，当移除选择题选项时推理模型表现显著提升。研究同时发现适度且自适应的推理能带来收益，约束推理长度可缓解失败。

基于这些发现，论文提出了两种干预方法：慢到快自适应推理和想到匹配捷径预防，以验证并缓解上述问题。最终结论强调，要实现稳健的心理理论能力，需要开发超越现有推理方法的独特能力，而非简单扩展形式推理策略。这凸显了形式推理与社会推理之间的根本差异，为未来开发具备ToM能力的LRMs指明了方向。
