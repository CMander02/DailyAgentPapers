---
title: "What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design"
authors:
  - "Ivan Bercovich"
date: "2026-04-30"
arxiv_id: "2604.28093"
arxiv_url: "https://arxiv.org/abs/2604.28093"
pdf_url: "https://arxiv.org/pdf/2604.28093v1"
categories:
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "基准设计指南"
  - "终端Agent"
  - "对抗性评估"
  - "奖励欺骗"
relevance_score: 8.5
---

# What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design

## 原始摘要

Terminal-agent benchmarks have become a primary signal for measuring the coding and system-administration capabilities of large language models. As the market for evaluation environments grows, so does the pressure to ship tasks quickly, often without thorough adversarial review of the verification logic. This paper is a guideline for writing good benchmark tasks, drawn from over a year of contributing to and reviewing tasks for Terminal Bench. Most people write benchmark tasks the way they write prompts. They shouldn't. A prompt is designed to help the agent succeed; a benchmark is designed to find out if it can. We argue that good tasks are adversarial, difficult, and legible, and that a large class of common failure modes -- AI-generated instructions, over-prescriptive specifications, clerical difficulty, oracle solutions that assume hidden knowledge, tests that validate the wrong things, and reward-hackable environments -- are predictable consequences of treating task authoring as prompt authoring. We catalog these failure modes, argue that real difficulty is conceptual rather than environmental, and discuss recent empirical evidence that over 15% of tasks in popular terminal-agent benchmarks are reward-hackable. We hope this serves as a useful reference for benchmark maintainers, task contributors, and researchers using benchmark scores as evidence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《What Makes a Good Terminal-Agent Benchmark Task》旨在解决当前终端代理基准测试设计中普遍存在的质量问题。研究背景是，随着大语言模型在编码和系统管理能力评估中的广泛应用，终端代理基准测试已成为主要信号。然而，现有方法存在严重不足：大量任务作者像写提示词一样编写基准测试，导致任务过于友好、缺乏挑战性，且验证逻辑未经严格对抗性审查。这种“提示-基准”混淆的写作范式，使得任务无法有效区分智能体的真实能力。核心问题在于，许多任务存在可预测的失败模式，包括AI生成的指令、过于详细的规范、琐碎的机械性难度、依赖隐藏知识的“神谕”解决方案、验证错误目标的测试，以及可被奖励黑客攻击的环境。论文指出，超过15%的热门终端代理基准测试任务是可被奖励黑客利用的。因此，本文要解决的核心问题是：如何设计具有对抗性、高难度和可解释性的优质基准测试任务，以准确评估智能体的真实能力，避免任务被轻易攻破或产生虚假分数。

### Q2: 有哪些相关研究？

这篇论文提出了一套设计终端智能体（terminal-agent）基准测试任务的原则，并批评了现有工作中普遍存在的问题。相关研究主要可分为以下几类：

1.  **基准测试设计与方法论类**：本文的核心贡献是提出“对抗性、困难、可读”的设计准则。与之相关的工作包括 SWE-bench（评估代码修复）、Intercode（评估交互式编码）等，这些工作更侧重于构建特定场景的评估能力，而本文指出它们普遍存在将“任务写作”等同于“提示写作”的系统性错误，导致验证逻辑容易被破解或过于简单。

2.  **奖励破解与鲁棒性评测类**：论文提到超过15%的流行终端智能体基准测试任务是可作弊的。这直接关联到针对大语言模型的奖励破解（reward hacking）和对抗性评测研究，例如对代码生成任务中单元测试鲁棒性的分析。本文的新颖之处在于从环境设计源头系统性地分类了失败模式（如AI生成的指令、假设隐藏知识的神谕解法），而不是事后修补。

3.  **概念难度与环境难度区分**：本文强调真正的难度应该是“概念上的”而非“环境上的”。这与一些旨在增加代理任务复杂度（如长上下文、多步骤）的工作形成对比，认为后者若只是增加环境噪音而非推理挑战，则属于徒增“文员式难度”。

整体上，本文是一篇指导性而非提出新模型或新环境的论文，它通过反思现有基准的常见陷阱，为如何写出更有效、更诚实的评测任务提供了原则性建议。

### Q3: 论文如何解决这个问题？

核心方法是将基准任务设计从“提示词编写”范式转向“测试用例设计”范式。整体框架围绕三个核心准则展开：对抗性、困难性和可读性。任务编写者必须主动假设智能体会试图利用验证逻辑的漏洞，从而设计出能够抵御这种“奖励黑客”行为的任务。

主要模块和组件包括：
1. **指令设计**：强调“目标导向”而非“流程导向”。指令应简洁、直接、无冗余，像对资深工程师描述最终状态，而非教新手一步步操作。这避免了因格式复杂或细节过细导致的“文员式错误”。
2. **验证逻辑设计**：核心原则是“测试结果而非实现”。测试用例必须独立于特定的解决方法，验证最终功能正确性，而不是检查中间变量（如特定库是否安装）或硬编码的解决方案路径。对于有内在差异性的任务（如词向量训练），应采用统计性或多角度验证。
3. **环境抗游戏化设计**：确保智能体无法通过探查或复制测试文件本身来作弊。例如，通过修改测试框架，在提示词中加入“测试签名”，并运行“请破解”版本，在任务上线前分析轨迹，以此主动发现可被利用的漏洞。同时，限制智能提权限（如使用非root用户）也是一种手段，但更推荐给予无限制访问以避免无意义的“环境困难性”。

其核心创新点在于：
- 提出了任务作为“测试”而非“提示”的新范式，并系统性地分类了六种常见的失败模式：AI生成指令、过度规定指令、文员式困难、假设隐藏知识的神谕解决方案、验证错误目标的测试以及可奖励黑客的环境。
- 强调“真正的困难应是概念层面的，而非环境层面的”，并通过实证（超过15%的任务可被奖励黑客）证明了其准则的必要性和有效性。

### Q4: 论文做了哪些实验？

该论文本身并未进行直接的实验，而是基于对终端代理基准测试（Terminal Bench）社区超过一年的贡献与评审经验，提出了一套用于设计高质量基准任务的指导原则，并提供了一个案例分析。论文的核心论点是：好的基准任务应具备对抗性（adversarial）、困难性（difficult）和可读性（legible）三个特征。研究者分析了任务创作中常见的失败模式，包括AI生成的指令、过度规定性的规格说明、文书性难度、假设隐藏知识的预言机解决方案、验证了错误内容的测试，以及可奖励-黑客的环境等。论文引用了实证证据，表明在流行的终端代理基准测试中，超过15%的任务存在可奖励-黑客（reward-hackable）的问题。这些证据来自对现有基准测试（如SWE-bench）的观察，而非论文作者自行设计的新实验。因此，论文的主要“实验”是通过回顾和批判性分析现有任务，总结出设计失败模式的分类，并以此论证其提出的指导原则的必要性，最终期望为基准维护者、任务贡献者和研究者提供参考。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的“概念难度”与“环境难度”的区分非常关键，但也带来几个值得深入探索的方向。首先，论文承认“概念难度”本身难以量化，且人类与LLM的难度分布呈“锯齿状”，因此未来研究可以探索**更系统的难度评估方法**，例如构建一个基于“认知步骤数”或“搜索复杂度”的度量标准，取代依赖人类直觉或模型表现。其次，论文指出**时间限制可能变成“黑箱”**，隐藏了模型推理过程。可以借鉴“渐进式评分”思路，将时间与质量映射为连续分数，而非简单的通过/失败，这样能更细致地刻画模型性能。此外，当前“对抗性设计”虽能防止reward hacking，但作者的解决方案偏向于任务作者个人经验，未来可以尝试**自动化对抗性测试框架**——例如用另一个LLM或形式化方法自动生成验证逻辑的漏洞案例，降低人工评审成本。最后，论文提到“让代理知道时限导致其惊慌”，这揭示了**元认知能力**的缺失。或许可以研究在基准中明确告知环境约束（如资源限制）并考察模型如何调整策略，从而更公平地衡量其规划与自我保护能力。总之，未来的工作应聚焦于构建更数学化的难度体系、自动化验证流程，并设计能捕捉模型推理过程丰富信息的评估方式。

### Q6: 总结一下论文的主要内容

这篇论文提出了终端智能体基准任务（terminal-agent benchmark）的设计指导原则，指出大多数任务撰写者错误地将其当作提示词（prompt）来设计，而实际上基准应旨在发现模型能否完成任务，而非帮助其成功。论文基于作者在Terminal Bench上一年多的评审经验，定义了好任务应具备的三个特性：对抗性（adversarial）、困难性（difficult）和可读性（legible）。文章分类列举了常见失败模式，包括AI生成的指令、过度规定性规范、繁琐而非概念性的困难、依赖隐藏知识的“神谕”解法、验证错误内容的测试以及可被奖励黑客（reward-hackable）的环境。核心结论是真正的困难应是概念性的而非环境性的，并引用了实证证据表明超过15%的流行终端基准任务存在奖励黑客漏洞。该论文为基准维护者、任务贡献者和研究者提供了评估设计的重要参考。
