---
title: "SmellBench: Towards Fine-Grained Evaluation of Code Agents on Refactoring Tasks"
authors:
  - "Fake Lin"
  - "Binbin Hu"
  - "Xi Zhu"
  - "Ziwei Zhao"
  - "Zhi Zheng"
  - "Ziqi Liu"
  - "Zhiqiang Zhang"
  - "Jun Zhou"
  - "Tong Xu"
date: "2026-06-04"
arxiv_id: "2606.05574"
arxiv_url: "https://arxiv.org/abs/2606.05574"
pdf_url: "https://arxiv.org/pdf/2606.05574v1"
categories:
  - "cs.SE"
tags:
  - "Code Agent"
  - "代码重构"
  - "基准评估"
  - "代码异味"
  - "软件工程"
  - "LLM Agent"
  - "细粒度评估"
relevance_score: 8.5
---

# SmellBench: Towards Fine-Grained Evaluation of Code Agents on Refactoring Tasks

## 原始摘要

Code Agents have achieved remarkable advances in recent years, exhibiting strong capabilities across a wide range of software engineering tasks. However, their misuse often produces bloated and disorganized code that impairing readability, extensibility, and robustness. Despite this risk, existing benchmarks largely evaluate functional correctness rather than long-term maintainability of code agents. In this paper, we propose SmellBench, an extensible code refactoring benchmark that proactively injects code smells into clean code snippets from real-world repositories. This design enables the generation of controlled, high-quality, and diverse refactoring cases with human-written ground truth. Specifically, it contains 294 cases spanning 7 popular smell types, 3 difficulty levels, 2 instruction settings across 7 real-world repositories. We further design 3 evaluation aspects covering functional correctness, localization ability, and refactoring quality assessment. Experiments with 2 popular agents and 6 large langauge models (LLMs) show that the best combination - Qwen Code + Claude Sonnet 4.5 - achieved only a 50.34 score of smell elimination. Further analysis reveals that this gap arises from a focus on local code smells and a lack of cross-file understanding, which hinders comprehensive smell elimination.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前代码智能体评估中忽视代码长期可维护性的问题。研究背景是，大型语言模型驱动的代码智能体虽能高效完成代码生成、缺陷修复等任务，但常被滥用生成臃肿、混乱的代码，严重损害可读性、可扩展性和鲁棒性。现有评估基准（如HumanEval、SWE-bench）主要聚焦于功能正确性，即代码能否通过测试，而忽略了代码质量与可维护性。同时，现有重构基准存在两大不足：一是人工构建的高质量基准成本高、扩展性差，覆盖场景有限；二是从Git提交历史自动挖掘的基准中，重构信号稀疏、碎片化，常与功能实现和缺陷修复混杂，难以系统评估。为此，本文提出了**SmellBench**，其核心创新是主动向来自真实仓库的干净代码片段注入代码坏味，从而生成受控、高质量、多样化的重构案例，并附带人工标注的真值。通过这种可控注入，SmellBench既保证了数据的纯净性（重构与其它变更隔离）和多样性（覆盖7种坏味类型、3个难度级别），又提升了扩展性。因此，本文要解决的核心问题是：**如何构建一个既能保证数据质量和可扩展性，又能系统、细粒度地评估代码智能体在重构任务上的能力（而不仅仅是功能正确性）的基准，并揭示当前方法在跨文件坏味理解和消除上的显著不足。**

### Q2: 有哪些相关研究？

本文的相关研究主要分为代码生成/修复评测和代码重构评测两类。在代码生成/修复方面，早期工作如HumanEval、MBPP聚焦单函数正确性，ClassEval关注类级生成，RepoBench、CrossCodeEval扩展到跨文件项目级理解。SWE-bench基于真实GitHub issue进行bug修复评测，LiveCodeBench引入竞赛编程挑战，GitTaskBench和CodeIF则关注用户驱动多步骤任务。这些基准主要评估功能正确性，缺乏对代码可维护性的考量。在代码重构评测方面，早期研究从少量Java项目构建数据集分析LLM重构行为，后续工作引入多步重构、抽取共享逻辑或结合IDE/静态分析工具。近期基准如CodeTaste扩展到多语言多文件重构任务，但现有方法要么依赖人工构建代价高昂，要么从提交历史挖掘导致重构与其他代码变更混杂。SmellBench通过主动向干净代码注入代码异味来生成可控、高质量的重构案例，与现有工作形成关键区别：它能生成带人工标注真值的多样化重构样本，并支持细粒度的功能正确性、定位能力和重构质量三维评估，有效弥补了现有基准在覆盖范围、可扩展性和数据纯度上的不足。

### Q3: 论文如何解决这个问题？

SmellBench通过一个四阶段的可控构造流程来解决代码智能体重构能力评估问题。整体框架围绕“主动注入代码坏味”设计，包含四个核心模块：仓库收集、候选位置发现、坏味注入和功能正确性验证。

在仓库收集阶段，选取7个高星PyPI项目以确保代码复杂度和测试覆盖。候选位置发现采用粗过滤（保留超过500行的源文件）和代理定位两级筛选，利用代码智能体而非规则匹配来识别符合特定坏味语义要求的注入位置，避免位置偏差。坏味注入阶段由强大的代码智能体（如OpenHands+Claude Sonnet 4.5）直接修改干净代码以引入目标坏味，同时保持可编译性，不依赖编程语言、外部工具或提交历史，从而支持无限扩展案例。功能验证阶段通过覆盖率分析筛选测试用例，对未通过的案例迭代修正，最终产生294个高质量案例。

创新点包括：1) 将重构任务形式化为7种代表性坏味类型，并引入3种难度级别和2种指令设置，实现细粒度可控评估。2) 设计三维评估体系，包括测试通过率（功能正确性）、定位准确率（识别重构目标的能力）和LLM-as-Judge（从代码质量、结构健全性、跨文件协调性和坏味消除四方面评估重构质量）。3) 引入闻味道分析作为LLM评估的前置步骤，通过显式解析坏味的结构问题和重构目标，为后续判分提供统一语义基础，提升不同模型间评估的一致性。实验显示最佳组合（Qwen Code + Claude Sonnet 4.5）坏味消除得分仅50.34，暴露了当前智能体偏向局部坏味、缺乏跨文件理解的局限。

### Q4: 论文做了哪些实验？

论文的实验围绕SmellBench基准测试展开，评估2种代码代理（OpenHands和Qwen Code）与6种大语言模型（LLM：Qwen3‑Coder‑30B、Qwen3‑Coder‑480B、DeepSeek‑V3.2、GPT‑5‑Mini、Gemini‑2.5‑Flash、Claude Sonnet‑4.5）的代码重构能力。实验设置上，所有运行使用Harbor框架在Docker隔离环境中进行，代理拥有完全修改代码库的权限，每个任务最多20分钟，仅执行一次。数据集为SmellBench，包含294个案例，覆盖7种常见代码坏味、3个难度级别和2种指令设置。评估采用6个指标，涵盖功能性正确性、定位能力和重构质量。主要结果：最佳组合Qwen Code + Claude Sonnet 4.5的“坏味消除”分仅为50.34%。几乎所有模型测试通过率高于80%，但代码质量与结构合理性分数较高。开源模型表现出竞争力，如Qwen-Coder-480B与GPT-5-Mini性能相当。OpenHands在弱LLM下表现更好，随LLM能力提升性能差距缩小。不同坏味类型表现差异大，DeepSeek在Data Clumps等上突出，但所有模型在Shotgun Surgery（需多文件协调，平均5.7文件）上均表现差，Claude只修改2.7个文件。难度越高性能越低，但模型修改文件数未相应增加，表明多文件协调能力不足。错误分析还显示代理超时（DeepSeek高达77%）和定位失败是主要瓶颈。

### Q5: 有什么可以进一步探索的点？

当前SmellBench存在多方面的局限性。首先，真实仓库中天然存在的代码异味（如上帝类）会污染评估数据，降低结果可靠性。未来研究应改进异味注入的筛选机制，确保注入前后数据的纯净对比。其次，异味的注入模式存在同质化，可能导致模型学习到套路化解法而非泛化重构能力。建议引入更复杂的复合异味组合，或动态生成上下文依赖的异味实例，如跨文件耦合问题。此外，LLM作为评估者的偏见问题需重视，可尝试引入多模型投票或人类专家验证，结合结构化评估指标（如代码度量阈值）减少主观性。更重要的是，实验揭示模型对全局异味（如跨文件耦合）的感知薄弱，未来需探索强化跨文件上下文建模能力。建议将代码仓库的完整依赖图纳入agent的观测空间，或设计分层规划机制（先全局检测异常关联，再局部重构），以提升协同重构的鲁棒性。

### Q6: 总结一下论文的主要内容

代码Agent的误用常导致代码臃肿、可读性差，但现有基准仅关注功能正确性，忽视了代码可维护性。本文提出SmellBench，一个细粒度的代码重构评估基准。其核心方法是通过主动向真实仓库的干净代码中注入7种常见的“代码坏味”，生成294个受控、高质量的重构案例，并附带人工标注的标准答案。该基准设计了涵盖功能正确性、定位能力及重构质量的三个评估维度。实验表明，当前最优组合Qwen Code + Claude Sonnet 4.5的坏味消除分数仅达50.34%。进一步分析揭示了主要差距源于模型更关注局部坏味，缺乏跨文件理解能力，阻碍了全面的坏味消除。SmellBench的意义在于首次将代码重构质量纳入评估，为衡量Agent的仓库级推理与软件长期维护能力提供了关键工具，揭示了当前模型在可维护性方面的严重不足。
