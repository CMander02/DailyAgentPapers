---
title: "Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents"
authors:
  - "Jiahong Xiang"
  - "Wenxiao He"
  - "Xihua Wang"
  - "Hongliang Tian"
  - "Yuqun Zhang"
date: "2026-02-26"
arxiv_id: "2602.22764"
arxiv_url: "https://arxiv.org/abs/2602.22764"
pdf_url: "https://arxiv.org/pdf/2602.22764v1"
categories:
  - "cs.SE"
tags:
  - "LLM-based Agent"
  - "Agent Architecture"
  - "Tool Use"
  - "Agent Benchmark"
  - "Code Agent"
  - "Software Engineering"
  - "ReAct"
  - "Automated Issue Resolution"
relevance_score: 8.5
---

# Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents

## 原始摘要

The Rust programming language presents a steep learning curve and significant coding challenges, making the automation of issue resolution essential for its broader adoption. Recently, LLM-powered code agents have shown remarkable success in resolving complex software engineering tasks, yet their application to Rust has been limited by the absence of a large-scale, repository-level benchmark. To bridge this gap, we introduce Rust-SWE-bench, a benchmark comprising 500 real-world, repository-level software engineering tasks from 34 diverse and popular Rust repositories. We then perform a comprehensive study on Rust-SWE-bench with four representative agents and four state-of-the-art LLMs to establish a foundational understanding of their capabilities and limitations in the Rust ecosystem. Our extensive study reveals that while ReAct-style agents are promising, i.e., resolving up to 21.2% of issues, they are limited by two primary challenges: comprehending repository-wide code structure and complying with Rust's strict type and trait semantics. We also find that issue reproduction is rather critical for task resolution. Inspired by these findings, we propose RUSTFORGER, a novel agentic approach that integrates an automated test environment setup with a Rust metaprogramming-driven dynamic tracing strategy to facilitate reliable issue reproduction and dynamic analysis. The evaluation shows that RUSTFORGER using Claude-Sonnet-3.7 significantly outperforms all baselines, resolving 28.6% of tasks on Rust-SWE-bench, i.e., a 34.9% improvement over the strongest baseline, and, in aggregate, uniquely solves 46 tasks that no other agent could solve across all adopted advanced LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用基于大语言模型（LLM）的智能体（Agent）来自动化解决真实世界、仓库级别的Rust编程语言开发问题。研究背景是Rust语言因其内存安全和并发安全的特性，在系统编程等关键领域日益流行，但其严格的所有权模型和类型系统也带来了陡峭的学习曲线和较高的编码难度，阻碍了其更广泛的采用。与此同时，LLM驱动的代码智能体在解决复杂软件工程任务（如Python问题修复）上已展现出巨大潜力，但现有评估基准主要针对Python或Java，缺乏专门针对Rust的大规模、仓库级任务基准，导致无法系统评估和提升智能体在Rust生态中的实际效能。

现有方法的不足主要体现在两个方面：一是缺乏一个能够全面反映Rust仓库级软件工程挑战的大规模基准测试集，现有Rust基准多集中于函数级代码合成或特定漏洞分析，而包含Rust的通用软件工程基准任务数量又过少；二是即使将现有的通用代码智能体（如采用ReAct范式）应用于Rust，其效果也受限于两大核心挑战：难以理解仓库级别的整体代码结构，以及难以遵守Rust严格的类型和特质（trait）语义。此外，研究还发现问题的复现（issue reproduction）是解决Rust任务的关键瓶颈。

因此，本文要解决的核心问题是：如何系统评估并提升基于LLM的智能体在自动化解决真实世界、仓库级Rust软件工程问题上的能力。为此，论文首先构建了首个大规模仓库级Rust基准测试集Rust-SWE-bench，并在此基础上进行了全面的实证研究，揭示了现有智能体的局限性。进而，针对发现的代码结构理解与问题复现难题，论文提出了一种名为RUSTFORGER的新型智能体框架，通过集成自动化测试环境搭建和基于Rust元编程的动态追踪策略，来提升问题复现与动态分析能力，最终显著提高了Rust问题的自动解决率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：Rust编程辅助工具、基于LLM的代码智能体（Agents）以及软件工程任务评测基准。

在**Rust编程辅助工具**方面，已有一些针对特定问题的解决方案。例如，RustAssistant利用LLM帮助修复编译错误；Syzygy专注于将遗留C代码库自动迁移至Rust；Concrat旨在替换并发程序中的不安全C锁API；Bronze通过引入可选垃圾收集器来简化复杂内存管理；PanicKiller则专注于自动修复Rust程序中的panic错误。这些工作都是针对Rust开发中**特定痛点**的专门化工具。本文提出的RUSTFORGER与它们的核心区别在于，它旨在构建一个能够处理**多样化、真实世界、仓库级别**Rust问题的**通用型智能体**，而非解决单一类型问题。

在**基于LLM的代码智能体**方面，研究主要围绕如何构建能够自主解决复杂软件工程任务的智能体框架。代表性工作包括采用“思考-行动-观察”（ReAct）循环的范式，如SWE Agent和OpenHands（基于CodeAct架构），它们通过工具调用与环境交互。另一类采用更结构化的多阶段工作流，例如AutoCode v2.0使用专门化智能体管道进行迭代式上下文检索和规范推断，而Agentless则采用“定位-修复-验证”的非迭代式简化流程。这些智能体在Python生态（如SWE-bench）上取得了显著成功。本文的研究正是建立在这些智能体范式之上，但首次将它们系统性地应用于并评估于**Rust生态系统**，并针对研究中发现的Rust特有挑战（如理解仓库级代码结构、遵守严格的类型/特征语义）提出了新的增强方法RUSTFORGER。

在**软件工程任务评测基准**方面，SWE-bench是评估端到端软件维护能力的标杆，它提供了大量源自GitHub issue的Python仓库级任务。其验证子集SWE-bench Verified确保了任务质量。为了评估智能体的多语言泛化能力，后续出现了Multi-SWE-bench、SWE-bench Multilingual和SWE-PolyBench等基准，它们涵盖了Java、JavaScript等多种语言。**本文与这些基准工作的关系是延续和专门化**。现有多语言基准中虽然包含Rust任务，但数量有限（几十到两百多个），不足以支撑对Rust生态中智能体能力的严谨系统评估。因此，本文专门构建了**大规模、仓库级的Rust基准Rust-SWE-bench**（包含500个任务），填补了这一空白，为在Rust生态中评估和改进智能体提供了必要的基础设施。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RUSTFORGER的新型智能体方法来解决自动化Rust仓库级问题修复中的挑战。该方法的核心创新在于整合了**自动化测试环境搭建**与**基于Rust元编程的动态追踪策略**，以应对现有智能体在理解仓库级代码结构和遵守Rust严格类型/特质语义方面的两大主要局限。

**整体框架与主要模块：**
RUSTFORGER的设计旨在增强智能体在问题复现和动态分析阶段的可靠性，这是成功解决任务的关键。其架构包含两个关键技术组件：
1.  **自动化测试环境设置模块**：此模块负责处理Rust Cargo项目的依赖和环境配置，通过定制的Shell工具来管理，确保智能体能够在一个可控且一致的环境中复现问题。这解决了Rust项目特有的构建复杂性，为后续分析奠定基础。
2.  **Rust元编程驱动的动态追踪策略**：这是方法的创新核心。它利用Rust的元编程能力（如宏、过程宏等）在代码执行时动态注入追踪点，从而收集运行时信息（如函数调用栈、变量状态、类型信息等）。这种动态分析能力使智能体能够超越静态代码分析，深入理解问题的运行时行为、数据流以及复杂的类型和特质约束，从而生成更符合Rust语义的修复方案。

**工作流程与创新点：**
智能体首先利用自动化环境设置模块复现问题，确保能够可靠地触发原始issue中描述的错误行为。随后，在尝试修复的过程中，动态追踪策略被激活，为LLM提供丰富的运行时上下文和语义信息。这使得智能体（尤其是基于ReAct范式的智能体）在规划行动（如代码编辑、导航）时，能够更准确地理解代码库的全局结构，并避免产生违反Rust所有权、生命周期或特质系统的编译错误。

**效果与优势：**
评估表明，结合了Claude-Sonnet-3.7的RUSTFORGER在Rust-SWE-bench基准测试上实现了28.6%的任务解决率，比最强的基线（OpenHands + Claude-Sonnet，21.2%）提升了34.9%，并且独特解决了46个其他所有智能体都无法解决的任务。这一提升验证了该方法通过增强**可靠的问题复现**和提供**深度的动态语义洞察**，有效克服了现有智能体在应对Rust复杂仓库级任务时的核心瓶颈。

### Q4: 论文做了哪些实验？

论文在 Rust-SWE-bench 基准上进行了全面的实验评估。实验设置方面，评估了四种代表性的代码智能体：SWE-agent、OpenHands+CodeAct v2.1、Agentless 和 AutoCode v2.0，并使用了四种先进的 LLM 作为其底层模型：Claude-Sonnet-3.7、GPT-4o、o4-mini 和 Qwen3-235B。主要评估指标是解决率（Pass@1），即生成的补丁能成功应用并通过所有开发者编写的验收测试的任务比例。此外，还报告了平均 API 推理成本、令牌使用量、编辑范围（行、块、文件）以及针对问题复现阶段引入的“复现成功率”。

主要结果如下：在 Rust-SWE-bench 的 500 个任务上，采用 ReAct 范式的智能体表现最佳。其中，OpenHands 搭配 Claude-Sonnet-3.7 取得了最高的 21.2% 解决率（106个任务），显著优于其他配置。其他智能体与模型组合的解决率在 1.8% 到 15% 之间不等。实验发现，解决率高的智能体（如 OpenHands 和 SWE-agent）通常会产生更大范围的代码修改（平均编辑超过2个文件和70行代码），而结构化工作流的智能体（如 Agentless 和 AutoCode）编辑范围较小（约1.2个文件和少于20行）。所有智能体在需要小补丁的任务上表现相近，但在需要大规模、复杂补丁的挑战性任务上，ReAct 风格智能体展现出明显优势。成本方面，表现最好的智能体也最昂贵，例如 OpenHands 与 Claude-Sonnet 组合的平均任务成本为 3.81 美元。基于这些发现，论文提出了 RUSTFORGER 新方法，其在后续评估中将解决率提升至 28.6%。

### Q5: 有什么可以进一步探索的点？

本文提出的RUSTFORGER在自动化解决Rust仓库级问题上取得了显著进展，但仍存在多个可深入探索的方向。首先，当前方法主要依赖动态追踪和元编程来复现问题，但面对涉及复杂并发、内存安全或外部系统交互的缺陷时，其复现的可靠性和覆盖率可能不足。未来可探索结合形式化验证或符号执行来增强对Rust特有所有权、生命周期等语义的理解，从而更精准地定位深层错误。

其次，基准测试Rust-SWE-bench虽具代表性，但任务规模（500个）和仓库多样性（34个）仍有扩展空间。未来可纳入更多工业级项目（如操作系统、浏览器引擎）中的复杂问题，以评估智能体在极端场景下的鲁棒性。此外，当前智能体主要针对已有issue进行修复，未来可探索其在新功能开发、架构重构等创造性任务上的潜力。

最后，智能体的效率与成本值得优化。动态追踪和多次测试运行可能导致较高计算开销，未来可研究轻量级静态分析或增量学习策略，在保证效果的同时降低资源消耗。同时，可探索智能体与开发者的协同机制，例如通过自然语言交互解释修复意图，增强其在真实工作流中的实用性。

### Q6: 总结一下论文的主要内容

这篇论文针对Rust编程语言自动化问题解决的挑战，提出了首个大规模、仓库级的Rust软件工程任务基准测试Rust-SWE-bench，并设计了一种新型智能体方法RUSTFORGER以提升解决性能。

论文的核心问题是：现有基于大语言模型（LLM）的代码智能体在解决复杂的、仓库级的Rust软件工程问题时能力有限，缺乏专门的评估基准。为此，作者构建了包含500个真实任务、覆盖34个流行Rust仓库的Rust-SWE-bench基准。

研究首先对四种代表性智能体和四种先进LLM进行了全面评估，发现ReAct风格智能体最多只能解决21.2%的问题，主要受限于两点：难以理解仓库级的代码结构，以及难以遵守Rust严格的类型和trait语义。研究还发现，可靠地复现问题是解决任务的关键。

基于这些发现，作者提出了RUSTFORGER方法。该方法整合了自动化测试环境搭建和基于Rust元编程的动态追踪策略，以促进可靠的问题复现和动态分析。实验表明，使用Claude-Sonnet-3.7的RUSTFORGER显著优于所有基线，在Rust-SWE-bench上解决了28.6%的任务，比最强基线提升了34.9%，并且独特地解决了46个其他所有智能体都无法解决的任务。

该工作的主要贡献和意义在于：为Rust生态的自动化代码修复研究提供了首个大规模基准，深入揭示了现有智能体的局限性，并提出了一种创新的、针对Rust语言特性的智能体架构，有效提升了仓库级问题解决的性能。
