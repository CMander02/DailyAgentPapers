---
title: "CodeTaste: Can LLMs Generate Human-Level Code Refactorings?"
authors:
  - "Alex Thillen"
  - "Niels Mündler"
  - "Veselin Raychev"
  - "Martin Vechev"
date: "2026-03-04"
arxiv_id: "2603.04177"
arxiv_url: "https://arxiv.org/abs/2603.04177"
pdf_url: "https://arxiv.org/pdf/2603.04177v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Code & Software Engineering"
relevance_score: 7.5
taxonomy:
  capability:
    - "Code & Software Engineering"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "propose-then-implement decomposition"
  primary_benchmark: "CodeTaste"
---

# CodeTaste: Can LLMs Generate Human-Level Code Refactorings?

## 原始摘要

Large language model (LLM) coding agents can generate working code, but their solutions often accumulate complexity, duplication, and architectural debt. Human developers address such issues through refactoring: behavior-preserving program transformations that improve structure and maintainability. In this paper, we investigate if LLM agents (i) can execute refactorings reliably and (ii) identify the refactorings that human developers actually chose in real codebases. We present CodeTaste, a benchmark of refactoring tasks mined from large-scale multi-file changes in open-source repositories. To score solutions, we combine repository test suites with custom static checks that verify removal of undesired patterns and introduction of desired patterns using dataflow reasoning.
  Our experimental results indicate a clear gap across frontier models: agents perform well when refactorings are specified in detail, but often fail to discover the human refactoring choices when only presented with a focus area for improvement. A propose-then-implement decomposition improves alignment, and selecting the best-aligned proposal before implementation can yield further gains. CodeTaste provides an evaluation target and a potential preference signal for aligning coding agents with human refactoring decisions in realistic codebases.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）编码代理在生成代码时，虽然能实现功能，但往往导致代码复杂性累积、重复和架构债务的问题。研究背景是LLM编码代理在软件工程领域被快速采用，其在解决实际任务方面表现突出，但现有评估（如SlopCodeBench）表明，随着需求迭代，代理生成的代码会变得冗长且结构恶化，难以维持代码质量和长期可维护性。现有方法的不足在于缺乏具有挑战性的重构基准：当前的重构基准（如RefactorBench和SWE-Refactor）仅覆盖小范围、有限的重构任务，且主要评估模型在给定具体重构指令下的执行能力，而无法衡量模型能否自主识别代码中的可重构点并决定应实施何种重构。例如，GPT-4已在SWE-Refactor上达到75%的准确率，但近期研究发现，LLM在自主识别重构机会方面表现不佳（如ChatGPT仅识别出180个专家选定机会中的28个）。因此，本文要解决的核心问题是：探究最先进的编码代理能否在真实代码库中自主发现并实施与人类开发者选择一致的重构，即评估其（i）可靠执行重构的能力，以及（ii）识别人类实际所做重构选择的能力。为此，论文引入了CodeTaste基准，该基准从开源仓库的大型多文件变更中挖掘重构任务，结合仓库测试套件和自定义静态检查（使用数据流推理验证不良模式的移除和期望模式的引入）来评分，以填补现有评估空白并推动编码代理与人类重构决策的对齐。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和应用类。

在**方法类**研究中，已有工作探索了LLM在代码生成和重构方面的能力。例如，OpenAI报告其模型在大规模代码重构任务上进行训练和评估，但未公开内部框架。此外，有研究发现LLM很少能自主识别重构机会：给定Java文件输入时，ChatGPT仅识别出人类专家所选180个重构机会中的28个。本文与这些工作的区别在于，它不仅关注LLM执行指定重构的能力，还重点评估其自主发现并实施与人类开发者选择一致的重构的能力。

在**评测类**研究中，现有基准如RefactorBench和SWE-Refactor提供了重构任务的评估。RefactorBench包含少量文件的语法测试任务，而SWE-Refactor从18个Java仓库收集了1,099个方法级重构实例。然而，这些基准仅覆盖小范围、有限的重构，导致其快速过时（例如GPT-4 Codex已在SWE-Refactor上达到75%准确率）。本文提出的CodeTaste基准则通过挖掘开源仓库中的大规模多文件重构来克服这一局限，并结合测试套件和静态分析规则进行语义验证，从而更贴近真实开发场景。

在**应用类**研究中，相关工作如SlopCodeBench评估了迭代需求更新下代码的冗长和结构退化问题，而其他实验（如使用自主编码代理构建浏览器渲染引擎或C编译器）揭示了代理在长期代码质量维护上的困难。本文与这些工作的联系在于，它同样关注编码代理在真实代码库中维持代码质量的挑战，但通过引入对齐分数来量化代理重构与人类决策的一致性，为改进代理的代码维护能力提供了新方向。

### Q3: 论文如何解决这个问题？

论文通过构建CodeTaste基准测试框架来解决评估LLM代码重构能力的问题。其核心方法分为四个阶段：首先从开源仓库的历史提交中挖掘人类开发者执行的多文件重构案例；然后将每个重构转化为两种任务描述（详细说明重构类型与仅指定改进区域）；接着构建可复现的执行环境以运行原仓库的单元测试；最后生成静态分析规则来捕获重构前后的模式变化。

整体架构包含数据挖掘、任务生成、环境执行和评估验证四大模块。关键技术在于采用“测试套件+静态规则”的双重评估机制：测试套件确保功能行为不变性，而自定义的静态检查则通过数据流推理验证不良模式的消除和理想模式的引入。创新点体现在提出了“提议-实施”分解策略，即先让LLM生成多个重构方案提议，选择与人类选择最对齐的方案后再进行具体实现，从而显著提升了对齐效果。

该方法的关键创新在于将重构任务形式化为可量化的评估目标，通过映射函数精确追踪代码行的增删改变化，并利用静态规则捕捉重构的语义一致性。这种设计不仅能够可靠地执行重构，还能识别LLM与人类开发者在实际代码库中重构选择的一致性差距。

### Q4: 论文做了哪些实验？

论文构建了名为CodeTaste的基准测试，并围绕其进行了实验。实验设置方面，研究者从开源仓库的大规模多文件变更中挖掘重构任务，每个任务实例对应一个代码库提交。他们使用一个多阶段流程来筛选和构建包含160个高质量重构任务的基准。为每个任务生成了结构化的详细任务描述（类似GitHub issue），并创建了容器化的可复现执行环境。

数据集/基准测试即CodeTaste基准，它包含从GitHub Archive和GitHub Activity Data数据集中筛选出的真实重构任务，覆盖了2023-2025年的提交。每个任务都关联了原始代码库状态（R）和经过人工重构后的黄金状态（R ∘ X*）。

对比方法主要评估了前沿大语言模型（LLM）智能体。实验考察了两种主要设置：一是当重构任务被详细指定时模型的性能；二是当仅给出需要改进的焦点区域时，模型能否自主发现人类开发者实际选择的重构方案。此外，论文还测试了一种“先提议后实施”的分解策略，以及一种在实施前选择最佳对齐提议的方法。

主要结果和关键指标显示，模型之间存在明显差距。智能体在重构任务被详细指定时表现良好，但在仅给出改进焦点时，常常无法发现人类实际选择的重构方案。“先提议后实施”的分解策略提高了与人类选择的对齐度，而在实施前选择最佳对齐提议能带来进一步的性能提升。评估结合了代码库测试套件和自定义静态检查，后者使用数据流推理来验证不良模式的移除和期望模式的引入。

### Q5: 有什么可以进一步探索的点？

该论文揭示了LLM在代码重构任务上的局限性，即当仅给出改进方向而非具体重构指令时，模型难以准确识别人类开发者实际选择的重构方案。这为进一步探索提供了几个方向：首先，可研究如何通过更精细的提示工程或上下文学习，提升模型对代码“坏味道”的自主检测能力，而不仅依赖显式指令。其次，论文中“提议-实施”的分解方法虽有效，但未来可探索多智能体协作框架，让不同模型分别负责诊断、提议和验证，以模拟人类团队的分工。此外，基准测试CodeTaste主要基于开源项目，未来可纳入更多行业私有代码库或特定领域语言的重构案例，以增强泛化性。最后，结合强化学习，利用测试套件和静态检查的反馈作为奖励信号，持续优化模型的重构决策过程，可能使模型更贴近人类的代码质量偏好。

### Q6: 总结一下论文的主要内容

这篇论文提出了CodeTaste基准测试，旨在评估大型语言模型（LLM）编码代理在代码重构任务上的能力。核心问题是探究LLM代理能否可靠地执行重构，以及能否识别并选择与真实代码库中人类开发者实际决策相一致的重构方案。

论文的方法是通过一个可扩展的流水线，从开源GitHub仓库中挖掘出100个大型多文件重构实例，为每个任务创建可执行环境和静态分析规则。这些规则利用数据流推理来验证代码模式从“不良”到“理想”的转换。评估结合了仓库测试套件和自定义静态检查，以确保功能正确性和模式转换。

主要结论揭示了前沿模型存在明显差距：在给定详细重构指令时，代理表现良好（对齐分数最高达69.6%）；但在仅提供改进重点区域、需要自主发现重构方案时，代理表现显著不佳（对齐分数低于8%）。论文发现，采用“先提议后实施”的分解策略能改善对齐效果，且在实施前选择最佳对齐提议可带来进一步增益。CodeTaste为在现实代码库中使编码代理与人类重构决策对齐提供了评估目标和潜在的偏好信号。
