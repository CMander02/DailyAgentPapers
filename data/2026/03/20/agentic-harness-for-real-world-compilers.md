---
title: "Agentic Harness for Real-World Compilers"
authors:
  - "Yingwei Zheng"
  - "Cong Li"
  - "Shaohua Li"
  - "Yuqun Zhang"
  - "Zhendong Su"
date: "2026-03-20"
arxiv_id: "2603.20075"
arxiv_url: "https://arxiv.org/abs/2603.20075"
pdf_url: "https://arxiv.org/pdf/2603.20075v1"
github_url: "https://github.com/dtcxzyw/llvm-autofix"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 工具与框架"
  - "代码智能体"
  - "专业领域应用"
  - "基准测试"
  - "LLM 能力评估"
relevance_score: 7.5
---

# Agentic Harness for Real-World Compilers

## 原始摘要

Compilers are critical to modern computing, yet fixing compiler bugs is difficult. While recent large language model (LLM) advancements enable automated bug repair, compiler bugs pose unique challenges due to their complexity, deep cross-domain expertise requirements, and sparse, non-descriptive bug reports, necessitating compiler-specific tools. To bridge the gap, we introduce llvm-autofix, the first agentic harness designed to assist LLM agents in understanding and fixing compiler bugs. Our focus is on LLVM, one of the most widely used compiler infrastructures. Central to llvm-autofix are agent-friendly LLVM tools, a benchmark llvm-bench of reproducible LLVM bugs, and a tailored minimal agent llvm-autofix-mini for fixing LLVM bugs. Our evaluation demonstrates a performance decline of 60% in frontier models when tackling compiler bugs compared with common software bugs. Our minimal agent llvm-autofix-mini also outperforms the state-of-the-art by approximately 22%. This emphasizes the necessity for specialized harnesses like ours to close the loop between LLMs and compiler engineering. We believe this work establishes a foundation for advancing LLM capabilities in complex systems like compilers. GitHub: https://github.com/dtcxzyw/llvm-autofix

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动修复编译器漏洞这一极具挑战性的问题。研究背景是，编译器作为现代计算的基础设施至关重要，但其漏洞修复极其困难，因为编译器是复杂的大型系统，其漏洞报告通常缺乏自然语言描述（仅有重现错误的测试用例、堆栈跟踪或反例），且理解和修复需要涉及词法分析、类型系统、中间表示优化等深度的跨领域专业知识。现有基于LLM的通用软件工程自动化方法（如SWE-bench和SWE-agent）主要连接标准bash工具来处理常规软件问题，在面对编译器这类特殊复杂系统时效果有限，无法有效应对其独特的挑战。

因此，本文要解决的核心问题是：如何弥合通用LLM能力与编译器工程特殊需求之间的鸿沟，为LLM智能体（Agent）提供专门的支持，使其能够理解和修复编译器漏洞。为此，论文以广泛使用的LLVM编译器基础设施（特别是其中端优化部分）为焦点，首次提出了一个名为“llvm-autofix”的智能体化工具套件。该套件旨在通过提供编译器专用工具、一个包含可重现LLVM漏洞的基准测试集（llvm-bench）以及一个为修复LLVM漏洞量身定制的最小化智能体（llvm-autofix-mini），来系统性地辅助LLM智能体完成编译器漏洞的定位与修复任务，从而推动LLM在编译器这类复杂系统中的应用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：编译器缺陷修复、基于LLM的自动程序修复（APR）以及智能体（Agent）框架。

在**编译器缺陷修复**方面，传统方法多依赖开发者手动分析，或使用符号执行、模糊测试等自动化工具定位问题，但通常难以生成有效补丁。本文提出的llvm-autofix则首次将LLM智能体系统化引入该领域，专注于修复而非仅检测。

在**基于LLM的APR**方面，现有工作（如ChatRepair、Self-Repair）已探索利用LLM修复通用软件缺陷，并常构建基准（如HumanEval、Defects4J）进行评估。本文指出，编译器缺陷具有跨领域知识复杂、错误报告稀疏等独特性，导致前沿模型在此类任务上性能骤降60%。因此，本文创建了专门的编译器缺陷基准llvm-bench，并设计了适配编译器的智能体工具链。

在**智能体框架**方面，当前研究（如AutoGPT、MetaGPT）致力于构建通用任务求解智能体。本文与之不同，提出了一个**领域特定的智能体套件（agentic harness）**，通过集成专为LLVM设计的工具、基准和最小化智能体（llvm-autofix-mini），显著提升了修复效率，其性能优于现有最佳方法约22%，体现了领域定制化智能体框架的必要性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为llvm-autofix的智能体化工具套件来解决编译器（特别是LLVM）错误自动修复的难题。其核心方法是设计一个专门针对编译器复杂性的辅助框架，将LLM智能体与专业的编译器工具链深度集成，从而弥补LLM在理解深层领域知识和处理稀疏、非描述性错误报告方面的不足。

整体框架由三大核心组件构成：1）**智能体友好的LLVM工具集**：这是llvm-autofix的核心创新，它将编译器工程中繁琐且专业的任务封装成一系列智能体可调用的工具，使智能体能专注于错误修复本身。工具集覆盖了完整的工作流，包括环境搭建与构建（Setup & Build）、错误复现与原因定位（Reproduce & Cause）、探索与调试（Explore & Debug）、编辑与打补丁（Edit & Patch）、测试与验证（Test & Validate）以及基准测试与评估（Benchmark & Evaluate）。例如，它集成了`opt`、`alive2`（中间端转换验证器）、`gdb`调试器和`llvm-lit`测试工具，使智能体能够动态检查LLVM内部状态、验证优化正确性并运行大量回归测试。2）**可复现的LLVM错误基准测试集llvm-bench**：该基准包含334个（后续扩展到446个）可复现的LLVM中端错误，并根据修复难度分为easy、medium和hard三个等级。每个错误都提供了复现器、回归测试和正确的“黄金补丁”。此外，还创建了一个持续更新的“live”子集，以应对LLM训练数据泄露的评估挑战。3）**定制的轻量级智能体llvm-autofix-mini**：这是一个专为修复LLVM错误设计的四阶段智能体，其架构为“Setup → Reason → Generate → Validate”。前两个阶段进行根因分析：Setup阶段利用工具集验证错误可复现，并通过调试器在关键断点（如崩溃函数前）暂停，以捕获运行时状态；Reason阶段则进入一个ReAct循环，动态调用调试、代码审查等工具来推断根本原因。Generate阶段基于根因启动另一个ReAct循环，使用编辑和在线测试工具来合成并迭代改进补丁。最后的Validate阶段进行离线的严格测试验证。

关键技术在于将编译器特定的、需要深厚专业知识的操作（如使用alive2验证错误、通过gdb检查中间表示状态）抽象为智能体可无缝使用的工具，从而极大地扩展了LLM在复杂系统领域的行动和认知边界。其创新点主要体现在：首次提出了针对编译器错误的智能体化工具套件概念；构建了首个大规模、可复现的LLVM错误基准；设计了一个利用运行时动态信息（而不仅仅是静态代码库）进行根因分析和补丁生成的专用智能体架构。评估表明，该最小智能体的性能超越了现有最佳方法约22%，验证了这种专业化工具套件在连接LLM与编译器工程方面的必要性和有效性。

### Q4: 论文做了哪些实验？

实验设置方面，研究评估了前沿大语言模型在LLVM编译器bug修复任务上的表现。使用的基准测试是论文提出的llvm-bench（包含229个可复现的LLVM中端bug），并划分为简单、中等、困难三个难度等级。对比方法包括：1）通用软件工程智能体MSWE（作为基线）；2）论文提出的专用智能体llvm-autofix-mini。评估模型包括GPT 5、Gemini 2.5 Pro、DeepSeek V3.2、Qwen 3 Max以及作为基线的GPT-4o。实验采用pass@1指标，以问题解决率（% Resolved）为核心评估标准，并设置了严格的参数（温度0、上下文窗口64K token、编辑/测试调用上限各25次）。

主要结果如下：首先，在编译器bug修复任务上，所有前沿模型相比通用软件bug修复（SWE-bench Verified）性能平均下降60%（范围35.2%-82.9%）。具体地，在llvm-bench上，DeepSeek V3.2表现最佳，解决率为38.9%（89/229），而Gemini 2.5 Pro仅为9.2%（21/229）。其次，论文提出的专用智能体llvm-autofix-mini相比通用智能体MSWE平均提升约22%，其中GPT 5配合专用智能体达到最高解决率51.5%（118/229），成本增量低于1.5美元/问题。然而，专家人工审查发现，即使通过测试的补丁，正确率也普遍低于42%，表明模型真实修复能力仍有限。例如，GPT 5配合专用智能体生成的补丁仅39%被专家认可为正确，使得真实问题解决率从51.5%降至20.1%。此外，随着难度增加，模型性能显著下降，困难等级的问题仅GPT 5配合专用智能体能修复个别案例。常见失败原因包括token预算耗尽、工具调用超限以及错误定位（WrongLocalization）等。

### Q5: 有什么可以进一步探索的点？

该论文在构建面向编译器的智能体框架上取得了进展，但仍有多个方向值得深入探索。首先，当前工作主要集中于LLVM这一特定编译器框架，未来可扩展至GCC、Rustc等其他复杂编译器或解释器，以验证框架的通用性。其次，论文依赖的基准测试集规模有限，且主要针对已复现的bug，未来需要构建更大规模、涵盖更隐蔽或并发类编译器缺陷的数据集，以提升智能体的鲁棒性。此外，现有方法仍严重依赖LLM的代码生成能力，但编译器bug常涉及深层逻辑推理与跨模块分析，可探索结合形式化验证、符号执行等传统程序分析技术，增强智能体的诊断与修复逻辑。最后，当前智能体以离线修复为主，未来可研究将其集成到持续集成流程中，实现实时监控与自动修复，并设计人机协同机制，允许开发者介入关键决策，形成混合增强的修复闭环。

### Q6: 总结一下论文的主要内容

该论文针对编译器（特别是LLVM）中难以修复的复杂bug问题，提出首个面向LLM智能体的辅助工具链llvm-autofix。核心问题是编译器bug修复需要跨领域专业知识，且bug报告描述稀疏，导致现有LLM方法效果显著下降。论文贡献包括：1）设计了一套对智能体友好的LLVM专用工具，帮助LLM理解编译器代码和测试；2）构建了可复现的LLVM bug基准测试集llvm-bench；3）开发了定制化最小智能体llvm-autofix-mini，专门用于修复LLVM bug。实验表明，前沿模型处理编译器bug时性能相比普通软件bug下降60%，而llvm-autofix-mini比现有最优方法提升约22%的修复成功率。这项工作强调了针对复杂系统（如编译器）开发专用LLM工具链的必要性，为LLM在系统软件工程中的应用奠定了基础。
