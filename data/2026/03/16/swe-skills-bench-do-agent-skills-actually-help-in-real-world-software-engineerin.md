---
title: "SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?"
authors:
  - "Tingxu Han"
  - "Yi Zhang"
  - "Wei Song"
  - "Chunrong Fang"
  - "Zhenyu Chen"
  - "Youcheng Sun"
  - "Lijie Hu"
date: "2026-03-16"
arxiv_id: "2603.15401"
arxiv_url: "https://arxiv.org/abs/2603.15401"
pdf_url: "https://arxiv.org/pdf/2603.15401v1"
github_url: "https://github.com/GeniusHTX/SWE-Skills-Bench"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Software Engineering Agent"
  - "Agent Skills"
  - "Tool Use"
  - "Evaluation Framework"
  - "LLM Agent"
  - "Code Agent"
relevance_score: 8.5
---

# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

## 原始摘要

Agent skills, structured procedural knowledge packages injected at inference time, are increasingly used to augment LLM agents on software engineering tasks. However, their real utility in end-to-end development settings remains unclear. We present SWE-Skills-Bench, the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE). It pairs 49 public SWE skills with authentic GitHub repositories pinned at fixed commits and requirement documents with explicit acceptance criteria, yielding approximately 565 task instances across six SWE subdomains. We introduce a deterministic verification framework that maps each task's acceptance criteria to execution-based tests, enabling controlled paired evaluation with and without the skill. Our results show that skill injection benefits are far more limited than rapid adoption suggests: 39 of 49 skills yield zero pass-rate improvement, and the average gain is only +1.2%. Token overhead varies from modest savings to a 451% increase while pass rates remain unchanged. Only seven specialized skills produce meaningful gains (up to +30%), while three degrade performance (up to -10%) due to version-mismatched guidance conflicting with project context. These findings suggest that agent skills are a narrow intervention whose utility depends strongly on domain fit, abstraction level, and contextual compatibility. SWE-Skills-Bench provides a testbed for evaluating the design, selection, and deployment of skills in software engineering agents. SWE-Skills-Bench is available at https://github.com/GeniusHTX/SWE-Skills-Bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究一个在AI代理领域日益流行但缺乏实证评估的现象：在真实世界的软件工程任务中，为大型语言模型代理注入“技能”是否真的有效。研究背景是，基于LLM的代理已被广泛用于代码生成、缺陷修复等软件工程任务，而“代理技能”作为一种无需微调或检索、只需在推理时注入上下文的程序性知识包（如标准操作流程、代码模板），其生态在短期内爆炸式增长（例如，136天内创建了超过84,000个技能）。然而，现有评估方法存在明显不足：现有的基准测试（如TerminalBench、HumanEval、BigCodeBench）要么不包含技能增强条件，要么仅针对自包含的函数补全，缺乏多文件上下文和真实开发场景；而首个跨领域技能基准SkillsBench中软件工程任务占比很小，且其设计目标并非专门评估真实开发工作流中的需求满足情况。因此，现有方法无法回答一个核心问题：在端到端的现实软件开发环境中，注入这些技能究竟能为代理完成需求带来多少边际效用？

本文要解决的核心问题正是填补这一空白，即量化评估代理技能在真实软件工程任务中的实际效用。为此，论文构建了首个需求驱动的基准测试SWE-Skills-Bench，通过将49个公开技能与固定的真实GitHub仓库及带有明确验收标准的需求文档配对，创建了约565个任务实例，并引入一个确定性的验证框架（将验收标准映射为基于执行的测试），从而在严格控制下对比代理“使用技能”与“不使用技能”的表现。其根本目标是隔离技能的影响，并科学地回答技能注入是否真正帮助代理满足了任务需求。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：软件工程基准、Agent技能评估以及基于执行的验证方法。

在**软件工程基准**方面，已有如SWE-bench、HumanEval等广泛使用的评测集，它们评估LLM代理在代码生成或问题修复上的整体能力。然而，这些基准通常不专门设计来隔离和量化“技能”（即预定义的程序知识包）在端到端开发中的边际效用。本文的SWE-Skills-Bench则填补了这一空白，它通过配对真实GitHub仓库、需求文档和具体技能，首次构建了一个需求驱动、可控制对比（使用技能与不使用技能）的评测环境。

在**Agent技能评估**领域，现有工作多关注技能的设计与集成框架（如LangChain、AutoGPT），或通过案例研究展示其潜力，但缺乏系统性的实证评估来衡量技能在实际工程任务中的具体收益与开销。本文直接针对这一缺口，通过大规模实验揭示了技能效果的高度局限性，强调了领域适配和上下文兼容性的关键作用。

在**验证方法**上，许多基准依赖模糊匹配或人工判断。本文则引入了**确定性的、基于执行的验证框架**，将每个任务的验收标准转化为自动化测试，从而实现了客观、可复现的结果度量。这种方法提升了评估的严谨性和可靠性，与依赖主观评分的先前工作形成区别。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SWE-Skills-Bench的基准测试框架来解决评估智能体技能在实际软件工程中真实效用的问题。其核心方法是设计一个需求驱动、可重复验证的评估体系，以隔离并量化技能注入带来的边际效益。

整体框架包含三个主要模块：首先是**基准构建模块**，它整合了49个公开的软件工程技能、固定在特定提交版本的GitHub仓库以及带有明确验收标准的需求文档，生成了涵盖六个软件工程子领域的大约565个任务实例。这种配对设计确保了每个任务都可以在“使用技能”和“不使用技能”两种条件下进行对比。

其次是**确定性验证框架**，这是关键创新点。它将每个任务的验收标准映射为基于执行的测试用例。通过自动化运行这些测试，可以客观、可重复地判定任务是否成功完成，从而避免了主观评估的偏差。

最后是**受控的配对评估流程**。对于每个任务实例，研究团队在完全相同的项目上下文和需求下，分别运行注入相关技能的智能体和不注入技能的智能体（即基线），然后比较两者的通过率。这种方法严格隔离了技能变量本身的影响。

该研究的主要创新在于首次创建了一个能够精准衡量技能“净效用”的基准。其关键技术在于将真实的、版本固定的代码仓库与结构化需求结合，并采用执行测试作为黄金验证标准。通过这种严谨的设计，论文揭示了技能效用的局限性：大部分技能并未带来通过率提升，其价值高度依赖于领域匹配度、抽象层次和上下文兼容性。该框架本身也成为一个供社区持续测试和优化技能设计与部署的实验平台。

### Q4: 论文做了哪些实验？

该研究构建了SWE-Skills-Bench基准，通过配对实验评估技能注入对LLM智能体在真实软件工程任务中的边际效用。实验设置上，研究者将49个公开的SWE技能与固定的GitHub仓库提交版本及包含明确验收标准的需求文档配对，生成了约565个任务实例，覆盖六个软件工程子领域。核心是对比“使用技能”与“不使用技能”两种条件下智能体的表现。

验证框架采用基于执行的确定性测试，将每个任务的验收标准映射为可自动运行的测试用例。主要对比方法即控制组（无技能）与实验组（注入特定技能）在相同任务上的表现。关键数据指标包括通过率（pass rate）的变化和令牌（token）开销。

主要结果显示，技能的整体效用有限：49个技能中，39个未能带来任何通过率提升，平均增益仅为+1.2%。令牌开销差异巨大，从少量节省到激增451%不等，且通过率可能并无改善。仅有七个高度专业化的技能产生了有意义的提升（最高达+30%），但同时有三个技能因版本不匹配的指导与项目上下文冲突，反而导致性能下降（最高达-10%）。这些结果表明，技能效用严重依赖于领域匹配度、抽象层次和上下文兼容性。

### Q5: 有什么可以进一步探索的点？

该论文揭示了技能注入在真实软件工程任务中效益有限的核心问题，为进一步探索提供了多个方向。局限性在于当前评估集中于技能本身的边际效用，但未深入探究技能与任务、项目上下文动态适配的机制。未来研究可首先聚焦于**技能的动态选择与组合机制**，开发能根据代码库状态、依赖版本、任务复杂度自动匹配或调整技能内容的智能体，而非静态注入。其次，需研究**技能抽象层次的优化**，论文发现过于具体或版本敏感的指令易导致冲突，因此可探索分层技能设计（如从原则性指导到具体代码模板），并引入上下文感知的指令适配器。此外，**评估维度可扩展至长期维护性**，如技能使用对代码质量、可读性、架构一致性的影响，而不仅是即时通过率。结合见解，一个关键改进思路是构建**技能效用预测模型**，利用代码变更历史、问题报告等元数据，预先评估技能在特定上下文的潜在价值与风险，实现更精准的部署。最后，需探索**技能与自主学习的结合**，使智能体能从成功/失败的任务实例中迭代更新技能库，形成持续进化的能力体系。

### Q6: 总结一下论文的主要内容

这篇论文提出了SWE-Skills-Bench，这是首个用于评估智能体技能在真实世界软件工程任务中边际效用的需求驱动基准。其核心问题是探究在推理时注入的结构化程序知识包（即技能）是否真正有益于端到端的软件开发。

论文方法上构建了一个包含49个公开技能、固定提交版本的GitHub仓库以及带有明确验收标准的需求文档的基准，共产生约565个跨六个软件工程子领域的任务实例。作者引入了一个确定性验证框架，将每个任务的验收标准映射为基于执行的测试，从而支持在有技能和无技能条件下的受控配对评估。

主要结论表明，技能注入的实际效益远低于业界快速采用的预期：49个技能中有39个未能带来通过率的任何提升，平均增益仅为+1.2%。虽然令牌开销有节省案例，但部分技能导致开销激增451%而通过率不变。仅有七个高度专业化的技能带来了显著增益（最高+30%），另有三个技能因版本不匹配的指导与项目上下文冲突反而降低了性能（最多-10%）。这些发现表明，智能体技能是一种狭窄的干预措施，其效用高度依赖于领域匹配度、抽象层次和上下文兼容性。该基准为评估软件工程智能体中技能的设计、选择和部署提供了重要的测试平台。
