---
title: "Agentic Proving for Program Verification"
authors:
  - "Alessandro Sosso"
  - "Akhil Arora"
  - "Bas Spitters"
date: "2026-05-22"
arxiv_id: "2605.23772"
arxiv_url: "https://arxiv.org/abs/2605.23772"
pdf_url: "https://arxiv.org/pdf/2605.23772v1"
categories:
  - "cs.AI"
  - "cs.LO"
  - "cs.PL"
  - "cs.SE"
tags:
  - "Agentic Theorem Proving"
  - "Program Verification"
  - "LLM Agent"
  - "Agentic Framework"
  - "Formal Verification"
  - "Lean 4"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Agentic Proving for Program Verification

## 原始摘要

Agentic systems have recently emerged as state-of-the-art approaches for automated theorem proving in formal mathematics. To assess how far these capabilities extend to program verification, we evaluate Claude Code in an agentic proving framework on CLEVER, a Lean 4 benchmark for verifiable code generation. Our results show that Claude generates arguably valid specifications for 98.8% of problems (with 81.3% also accepted by CLEVER's isomorphism-based scoring on the correct portion of the benchmark), certifies implementations against correct ground-truth specifications for 87.5% of problems, and reaches a 98.1% success rate on the end-to-end program generation and verification pipeline over entries with self-consistent premises. Across all stages, Claude further provides high-quality feedback on its own attempts (as confirmed under manual review), identifying underlying causes of failure and lingering bugs in the dataset. These findings highlight a growing mismatch between the difficulty of existing program verification benchmarks and the capabilities of modern agentic provers, and point to the need for more rigorous, bug-resilient evaluation methodologies, and in particular for alternatives to isomorphism-based scoring of generated specifications. More broadly, our results provide empirical evidence that tight compiler-in-the-loop agentic paradigms are currently the most effective approach for foundational program verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有程序验证基准测试无法有效评估现代智能体定理证明器能力的问题。近年来，基于大语言模型的智能体系统在形式化数学的自动定理证明中取得了最先进成果，但这些进展主要应用于数学领域，而非程序验证。程序验证与数学证明不同，它需要对可执行工件、显式规范及微妙边界条件进行推理，且受严格语法和语义约束。现有方法（如全证明生成模型、符号策略）在程序验证基准测试（如CLEVER）上表现不佳，而初步实验表明，基于Claude Code的智能体系统已接近饱和性能，甚至能识别并修复基准测试本身的错误。因此，本文的核心问题在于：1）评估当前最先进的智能体范式（即编译器参与循环的智能体系统）在完整程序验证流程（规范生成、实现认证、端到端验证）上的实际能力；2）揭示现有基于同构性评分的方法在评估自动形式化时的局限性，并指出需要更严格、对错误更具鲁棒性的评估方法。

### Q2: 有哪些相关研究？

相关研究主要集中在基于LLM的自动定理证明领域，可分为以下几类：

1. **方法类**：现有工作采用多种架构策略，包括全证明生成（whole-proof generation）、证明状态搜索（proof-state search）以及日益主流的智能体设计（agentic designs）。这些智能体系统整合了规划、工具使用和迭代精炼能力。本文使用的Claude Code属于代表性的智能体框架，与传统的专用全证明生成模型和符号策略形成对比。

2. **应用类**：已有工作在Lean 4、Isabelle、Rocq等类型理论证明助手的数学形式化基准上取得了显著进展。本文将这些能力扩展到程序验证这一更实际且结构更复杂的场景，需要处理可执行工件、显式规范、细微边界条件等。

3. **评测类**：本文在CLEVER基准上进行评估，该基准是Lean 4上的可验证代码生成评测集。与已有工作不同的是，本文发现智能体系统不仅在证明生成上接近饱和性能，还能识别基准本身的规范错误和实现缺陷，揭示了现有程序验证基准与当代智能体证明器能力之间的不匹配。

本文的主要区别在于：相比前期的初步实验（使用自定义精简流程），本文采用CLEVER的原始评测管线进行系统评估；同时方法论上揭示了基于同构性评分在自动形式化评估中的结构性局限，并提出了替代评测策略的建议。

### Q3: 论文如何解决这个问题？

论文提出了一种采用“编译器在环”（compiler-in-the-loop）的智能体框架进行程序验证。核心方法是让Claude Opus 4.6模型在Lean 4环境中自主执行四个阶段的任务：规范生成（specgen）、规范同构证明（speciso）、实现生成（implgen）和实现正确性证明（proofgen）。整体框架基于Claude Agent SDK，每个智能体实例配备两个关键组件：lean-lsp-mcp（一个与Lean语言服务器接口的MCP服务器，提供项目上下文和Mathlib中搜索相关引理的工具）和lean4-skills（注入Lean特定指令、命令、策略最佳实践和工作流模式的包）。对于每个任务，系统从模板初始化临时目录作为Lean项目，创建包含基准条目相关组件的Lean文件，然后提示新的智能体实例根据当前任务编辑文件。对于定理证明任务（speciso和proofgen），使用/lean4:autoprove命令启动多周期定理证明例程。任务超时设置为3600秒，完成后智能体报告结果，分为成功（OK）、失败（FAIL）或无法证明（ISSUE/MISMATCH）。创新点包括：通过MCP服务器实现与编译器的紧密交互，允许智能体在可观察的环境中推理和调试；使用结果分类和详细诊断分析，能够识别基准数据集中的错误；以及建立端到端的自动化验证管道，从自然语言规范到形式化证明的全流程。

### Q4: 论文做了哪些实验？

论文在CLEVER基准测试上评估了Claude Code在Lean 4程序验证中的表现。实验采用pass@1单次尝试，分多个阶段进行：规范生成（specgen）、规范同构验证（speciso）、实现生成（implgen）和证明生成（proofgen）。在specgen阶段，使用简单提示语时，模型为161个条目全部生成可接受的规范。speciso阶段显示，98.8%的规范有效解释源描述，但只有81.3%被CLEVER的同构评分接受。使用引导提示语后，虽改善了格式，但同构率提升不显著。多重规范提示语测试进一步筛选出11个条目成功同构。在proofgen阶段，基于有效真实规范（80道无问题题目）的实现成功率为87.5%。从生成规范出发的端到端管道（两个尝试）成功率为95.7%，去除基准问题后达98.1%。主要对比方法包括简单提示、引导提示和多重规范提示。结果揭示现有基准测试难度与Agent能力间存在差距，同构评分机制存在局限性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在以下几个方面：首先，评估方法依赖于同构性评分（isomorphism-based scoring），但该方法无法检测出规格说明中的语义错误，导致部分有缺陷的规格得以通过验证。其次，基准测试本身存在缺陷，如部分问题依赖于未解决的数学猜想（如Collatz猜想），或包含无法修复的固定组件。未来研究方向包括：开发更鲁棒、能容忍bug的评估方法论，替代同构性评分；探索更严谨的规格说明形式化方法，以弥补自然语言描述的歧义性；以及改进编译器在环（compiler-in-the-loop）的智能体范式，使其能自动检测并修复规格与实现中的语义错误。此外，可以尝试引入多轮交互式验证机制，让智能体在发现错误后自动修正规格或实现，形成闭环改进流程。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于智能体系统（Claude Code）的自动化程序验证框架，在CLEVER基准（Lean 4可验证代码生成基准）上评估其能力。问题定义为：现有智能体定理证明器能否有效扩展到程序验证领域。方法上，采用编译器在环的智能体范式，让Claude生成规范、证明实现正确性并进行自我反馈评估。主要结论包括：Claude为98.8%的问题生成了可认为有效的规范（其中81.3%通过同构评分），从正确黄金规范出发实现了87.5%的实现认证成功率，对于自洽前提的问题端到端成功率达98.1%。核心贡献在于揭示了当前程序验证基准与先进智能体证明器能力之间的日益增长的不匹配，指出现有同构评分方法在评估中的结构局限性。该研究意义重大：推动了需要更严格、鲁棒的评估方法学的需求，并为编译器在环智能体范式作为基础程序验证最有效方法提供了实证证据。
