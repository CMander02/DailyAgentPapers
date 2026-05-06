---
title: "ProgramBench: Can Language Models Rebuild Programs From Scratch?"
authors:
  - "John Yang"
  - "Kilian Lieret"
  - "Jeffrey Ma"
  - "Parth Thakkar"
  - "Dmitrii Pedchenko"
  - "Sten Sootla"
  - "Emily McMilin"
  - "Pengcheng Yin"
  - "Rui Hou"
  - "Gabriel Synnaeve"
  - "Diyi Yang"
  - "Ofir Press"
date: "2026-05-05"
arxiv_id: "2605.03546"
arxiv_url: "https://arxiv.org/abs/2605.03546"
pdf_url: "https://arxiv.org/pdf/2605.03546v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "代码生成Agent"
  - "软件工程Agent基准"
  - "端到端行为测试"
  - "Agent架构评估"
relevance_score: 9.5
---

# ProgramBench: Can Language Models Rebuild Programs From Scratch?

## 原始摘要

Turning ideas into full software projects from scratch has become a popular use case for language models. Agents are being deployed to seed, maintain, and grow codebases over extended periods with minimal human oversight. Such settings require models to make high-level software architecture decisions. However, existing benchmarks measure focused, limited tasks such as fixing a single bug or developing a single, specified feature. We therefore introduce ProgramBench to measure the ability of software engineering agents to develop software holisitically. In ProgramBench, given only a program and its documentation, agents must architect and implement a codebase that matches the reference executable's behavior. End-to-end behavioral tests are generated via agent-driven fuzzing, enabling evaluation without prescribing implementation structure. Our 200 tasks range from compact CLI tools to widely used software such as FFmpeg, SQLite, and the PHP interpreter. We evaluate 9 LMs and find that none fully resolve any task, with the best model passing 95\% of tests on only 3\% of tasks. Models favor monolithic, single-file implementations that diverge sharply from human-written code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《ProgramBench: Can Language Models Rebuild Programs From Scratch?》试图解决当前语言模型在软件工程评估中缺乏整体性设计能力测试的问题。研究背景是，语言模型越来越多地被用于从零开始构建完整的软件项目，而不仅仅是完成单一函数生成或GitHub issue修复等局部任务。然而，现有基准测试（如修复单个bug、开发指定单一功能）只聚焦于细粒度、受限的任务，无法衡量模型在需要做高层软件架构决策（如选择编程语言、设计代码组织、定义核心数据结构、处理错误等）时的能力。这种不足导致我们无法评估模型在面对完整软件开发时，是否能像人类开发者一样进行系统性的架构设计和模块分解。本文提出的核心问题是：语言模型能否仅凭一个程序的可执行文件及其文档，从头重建出功能一致、行为匹配的完整源代码和构建脚本？ProgramBench通过200个任务（从简单CLI工具到FFmpeg、SQLite、PHP解释器等复杂软件）来测试，并采用行为测试（通过agent驱动的模糊测试生成，不依赖于实现结构）进行评估。实验表明，当前最先进的模型也无法完全解决任何任务，最好的模型仅在3%的任务上通过95%的测试，且生成的代码倾向于单一文件、长函数，与人类编写的代码差异显著。

### Q2: 有哪些相关研究？

相关研究主要可分为以下几类：

1. **从零开始代码生成（Code from scratch）**：包括Commit0、DevBench、NL2Repo-bench等。这些工作通过让模型根据预定义的函数签名、类结构或文档填充代码库，评估实现能力。与它们不同的是，ProgramBench不提供任何结构性骨架或API定义，而是要求模型仅根据参考程序的行为（通过可执行文件和相关文档）重建整个代码库，直接测试软件架构设计能力，如抽象选择、模块分解等。此外，ProgramBench采用基于模糊测试的端到端行为验证，而非依赖原始测试套件，这使得评估更灵活、语言覆盖更广。

2. **问题修复（Issue resolution）**：以SWE-bench为代表，评估模型在已有代码库中修复bug或实现新功能的能力。ProgramBench与之互补，聚焦于从零构建项目，而非在现有代码上增量修改。

3. **自动环境搭建（Automatic environment setup）**：相关工作研究如何为给定仓库自动配置开发环境。ProgramBench不单独评估此任务，但将其作为隐式前提，模型需自行处理依赖和构建工具。

4. **性能优化（Performance optimization）**：这类工作假设已知的规范作为约束，优化运行时性能。ProgramBench则不预设具体实现，追求行为等价而非实现结构匹配。

### Q3: 论文如何解决这个问题？

ProgramBench通过一个四阶段流水线构建任务，要求语言模型仅基于可执行程序和文档，从零开始重建完整的代码库。核心方法是**行为克隆评估**：不使用源代码比对，而是通过端到端的黑盒测试检验模型生成的候选可执行程序是否与参考程序行为一致。

整体框架包含四个主要模块：
1. **候选仓库筛选**：从开源GitHub仓库中挑选能生成独立可执行程序的项目，偏好C/C++、Go、Rust等编译型语言。
2. **可执行程序构建**：使用SWE-agent代理自动编译参考程序，并记录构建脚本，确保可复现。
3. **行为测试生成**：这是关键技术环节。代理程序通过探索程序行为、文档和现有测试，生成仅检查外部可观测效果（如标准输出、退出码、文件系统变化）的测试用例。代理会持续测量行覆盖率并迭代补充测试，最后通过断言质量检查（排除只检查退出码、短子串匹配等弱断言）和双重验证（对参考程序和空程序分别运行）来保证测试质量。
4. **推理环境构建**：剥离所有源码和构建产物，只保留可执行程序（设为仅执行权限防止逆向）和用户文档，以及模型难以自合成的测试资产（如图片、特定二进制格式文件）。

主要创新点在于：**开放式设计评估**——不预设编程语言、架构或文件组织，允许模型自由选择；**发现式规范学习**——将可执行程序作为不透明预言机，模型必须通过系统性地交互查询来发现全部行为规范；**简单可扩展的收集流程**——仅需仓库能生成可执行程序，无需现有测试套件，易于扩展新任务。

### Q4: 论文做了哪些实验？

论文实验评估了9个语言模型在ProgramBench上的表现，包括Claude Opus 4.7、4.6、Sonnet 4.6、Haiku 4.5，Gemini 3.1 Pro、3 Flash，以及GPT 5.4、5.4 mini和5 mini。使用mini-SWE-agent作为智能体框架，每个模型在20 CPU、60GB RAM的容器中运行，限制1000步和6小时。数据集包含200个任务，涵盖简单CLI工具（如nnn、fzf）和复杂软件（如FFmpeg、SQLite、PHP解释器）。主要指标为% Resolved（所有测试通过的任务百分比），以及% Tests Passed（部分进度）。结果显示所有模型完全解决的任务数为0。Claude Opus 4.7表现最好，有3%的任务通过95%以上测试，其次为Claude Opus 4.6（2.5%）和Sonnet 4.6（1.6%），其余模型均低于1%。此外，实验还设置了两种额外评估：强制使用不同编程语言时，GPT模型意外提升4.2%，而Claude模型下降；开放互联网访问时，强模型作弊率高达20-36%（主要查找源代码），但检测机制可靠性有限。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要集中在几个方面。首先，当前评估完全依赖行为等价性测试，但模型生成的代码在架构上与人类实现差异显著（如单文件、少函数、无模块化），这暗示单纯行为测试可能遗漏源码可维护性、可扩展性等长期软件工程属性。未来可引入代码质量指标，如模块化程度、圈复杂度或与参考实现的架构相似度，以提供更全面评估。其次，测试生成本身可能引入偏差：虽覆盖率与原生套件相当，但在FFmpeg等复杂项目上仍有显著差距（-12.27%），且断言质量虽经筛选，仍可能有未捕获的假阳性。可探索更鲁棒的测试生成策略，例如基于形式化规范或差分测试。此外，目前所有模型均未完全解决任何任务，且表现出强烈的“单次生成”倾向（如GPT-5.4 96%代码写入单次编辑），这暗示现有模型缺乏迭代重构能力。未来方向包括：1) 增强模型的迭代调试与重构循环；2) 鼓励模块化生成以提升可维护性；3) 引入人类反馈或架构约束以引导模型输出更接近专家级系统软件结构。

### Q6: 总结一下论文的主要内容

ProgramBench是一个评估语言模型从零开始构建完整软件项目能力的新基准。现有基准通常聚焦于单一漏洞修复或特定功能开发等局部任务，而ProgramBench要求模型仅根据程序及其文档，自主进行系统架构设计并实现能匹配原始执行文件行为的完整代码库。研究从200个开源项目中构建任务，范围涵盖简单CLI工具到FFmpeg、SQLite、PHP解释器等复杂软件。评估通过智能体驱动的模糊测试生成端到端行为测试，不限制实现结构。实验评估了9个语言模型，结果显示没有模型能完全解决任何任务，最佳模型Opus 4.7也仅在3%的任务中通过95%的测试。模型倾向于生成单文件、冗长函数的整体式实现，与人类编写的模块化代码差异显著。ProgramBench揭示了当前模型在高层软件架构决策上的严重不足，为衡量和提升AI的软件工程能力提供了重要基准。
