---
title: "Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing"
authors:
  - "Nils Loose"
  - "Nico Winkel"
  - "Kristoffer Hempel"
  - "Felix Mächtle"
  - "Julian Hans"
  - "Thomas Eisenbarth"
date: "2026-03-09"
arxiv_id: "2603.08616"
arxiv_url: "https://arxiv.org/abs/2603.08616"
pdf_url: "https://arxiv.org/pdf/2603.08616v1"
categories:
  - "cs.SE"
  - "cs.CR"
tags:
  - "Multi-Agent System"
  - "Agent Architecture"
  - "Tool Use"
  - "Code Generation"
  - "Software Engineering"
  - "Fuzzing"
  - "ReAct"
  - "LLM-powered Agent"
relevance_score: 7.5
---

# Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing

## 原始摘要

Coverage-guided fuzzing has proven effective for software testing, but targeting library code requires specialized fuzz harnesses that translate fuzzer-generated inputs into valid API invocations. Manual harness creation is time-consuming and requires deep understanding of API semantics, initialization sequences, and exception handling contracts. We present a multi-agent architecture that automates fuzz harness generation for Java libraries through specialized LLM-powered agents. Five ReAct agents decompose the workflow into research, synthesis, compilation repair, coverage analysis, and refinement. Rather than preprocessing entire codebases, agents query documentation, source code, and callgraph information on demand through the Model Context Protocol, maintaining focused context while exploring complex dependencies. To enable effective refinement, we introduce method-targeted coverage that tracks coverage only during target method execution to isolate target behavior, and agent-guided termination that examines uncovered source code to distinguish productive refinement opportunities from diminishing returns. We evaluated our approach on seven target methods from six widely-deployed Java libraries totaling 115,000+ Maven dependents. Our generated harnesses achieve a median 26\% improvement over OSS-Fuzz baselines and outperform Jazzer AutoFuzz by 5\% in package-scope coverage. Generation costs average \$3.20 and 10 minutes per harness, making the approach practical for continuous fuzzing workflows. During a 12-hour fuzzing campaign, our generated harnesses discovered 3 bugs in projects that are already integrated into OSS-Fuzz, demonstrating the effectiveness of the generated harnesses.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决Java库代码覆盖率引导模糊测试中，自动化生成高质量测试适配器（fuzz harness）的核心难题。研究背景在于，覆盖率引导模糊测试已成为发现软件漏洞的关键技术，但其在库代码测试中的有效性严重依赖于能够将模糊器生成的随机输入转换为有效API调用的测试适配器。目前，手动创建适配器耗时费力，需要开发者深入理解API语义、初始化序列和异常处理契约，这极大地限制了模糊测试在Java库中的广泛应用。

现有自动化方法存在明显不足：基于使用模式的方法需要大量客户端代码库，对于新库或专用库往往不可行；基于结构的方法从类型签名推导，但难以处理隐式前置条件，且依赖领域特定启发式规则，泛化能力有限；基于反馈驱动的方法虽能迭代优化，但通常采用固定的终止阈值，缺乏对覆盖率差距的语义理解。近期基于大语言模型（LLM）的系统有所进展，但在生成过程中缺乏迭代、按需查询的探索机制，且一次性生成难以处理复杂库所需的多步初始化，预处理整个API也容易耗尽上下文窗口。

因此，本文要解决的核心问题是：如何设计一个自动化系统，能够高效、低成本地生成高质量的Java库模糊测试适配器，以克服现有方法在信息获取、上下文管理、语义理解和迭代优化方面的局限性。为此，论文提出了一种多智能体架构，通过五个分工协作的ReAct智能体（研究、合成、编译修复、覆盖率分析、优化），并结合按需查询的模型上下文协议（MCP）以及创新的方法定向覆盖度和智能体引导终止机制，来实现这一目标。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：传统方法生成和基于大语言模型（LLM）的合成。

在**传统方法生成**方面，相关工作主要基于程序分析技术。这又可细分为：1) **基于使用模式的生成**，从现有客户端代码或单元测试中挖掘有效的API调用模式，其优势在于捕获了真实的交互，但严重依赖可用且合适的消费者代码。2) **基于结构的生成**，直接从类型签名和接口规范推导测试工具，适用性更广但通常缺乏迭代精炼，适应新目标需大量人工。3) **基于反馈驱动的生成**，利用运行时信号（如API使用模式的自动机学习）迭代优化测试工具，但其终止决策常依赖特定领域启发式规则或固定覆盖率阈值。本文工作属于反馈驱动生成的范畴，但通过引入智能体来解释覆盖率差距，超越了固定的阈值决策。

在**基于LLM的合成**方面，近期研究利用LLM自动生成测试工具。相关工作包括：评估提示策略的可行性研究、基于覆盖率反馈进行提示变异的迭代精炼系统（但缺乏对覆盖率差距的语义解释）、以及利用API关系知识图谱增强LLM推理的方法（通常需预先处理整个API表面信息）。此外，也有工作将LLM推理集成到静态分析流程中。本文与这些LLM方法的关键区别在于：本文的多智能体架构通过模型上下文协议，实现了对文档、源代码和调用图信息的**按需查询**，避免了前期全量处理导致的信息过载，并能聚焦于目标特定深度。同时，本文引入了**方法定向覆盖率**和**智能体引导终止**等专门化静态分析与自适应编排机制，使智能体能动态决定迭代预算并解释覆盖率差距，而非采用固定迭代次数或通用启发式规则。

### Q3: 论文如何解决这个问题？

论文通过一个多智能体架构，结合静态分析与动态覆盖反馈，自动化生成并迭代优化用于Java库模糊测试的测试工具。其核心方法是将工作流分解为五个专门的ReAct智能体：研究、生成、编译修复、覆盖分析和优化。这些智能体通过模型上下文协议（MCP）按需查询文档、源代码和调用图信息，避免了预处理整个代码库，从而在探索复杂依赖时保持上下文聚焦。

整体框架分为三个阶段：目标研究、工具构建和迭代的覆盖引导优化。在环境初始化阶段，系统下载库构件并准备分析基础设施，包括提取Javadoc文档、使用GTAGs索引源代码，以及使用SootUp计算以目标方法为根的静态调用图（深度通常为10）。关键创新点之一是引入了方法定向覆盖：通过扩展JaCoCo并利用ASM进行离线字节码插桩，实现了运行时切换覆盖跟踪，确保仅记录目标方法执行期间的覆盖数据，从而精准反映目标行为，避免代理因调用无关工具方法而产生误导性激励。

主要模块通过MCP工具暴露给智能体，包括文档查询、源代码检索和调用图查询三类工具，并根据智能体角色进行访问控制，防止探索偏离。研究智能体将目标方法签名转化为关于API语义的上下文知识，生成结构化研究报告。生成智能体随后合成初始工具代码，重点处理异常推断与捕获。若编译失败，编译修复智能体会分析诊断信息并迭代修正。成功编译后，工具在模糊测试下执行以收集初始覆盖数据。

优化循环由覆盖分析智能体和优化智能体协作完成。覆盖分析智能体将覆盖数据与静态调用图合并，分析未覆盖的方法，判断优化潜力，并决定是否终止（基于收益递减判断）或继续优化。若继续，优化智能体则根据策略修改工具，例如多样化输入生成或触发异常处理路径，形成“编译-模糊测试-分析-优化”的反馈闭环，直至收敛或达到迭代限制。这种设计使得生成的工具在覆盖率和缺陷发现上均优于基线方法，且成本可控，适用于持续模糊测试工作流。

### Q4: 论文做了哪些实验？

论文的实验设置包括使用LangGraph进行工作流编排，并以Claude 4.5 Sonnet作为底层模型。生成的安全带通过Gradle编译，并使用Jazzer配合插桩覆盖率收集来执行。

实验在六个广泛部署的Java库（commons-cli、gson、guava、jackson-databind、jsoup、antlr4）的七个目标方法上进行，总计拥有超过115,000个Maven依赖项。对比的基线方法包括：1) OSS-Fuzz（谷歌的开源软件持续模糊测试服务），使用其现有的手工编写安全带；2) Jazzer AutoFuzz（一种基于反射的自动安全带生成模式）。由于实现问题，未能成功与OSS-Fuzz-Gen进行LLM方法对比。

实验主要评估了两种覆盖率：1) **方法目标覆盖率**：仅在目标方法执行期间激活，以聚焦目标行为；2) **完整目标范围覆盖率**：使用标准的JaCoCo对整个库进行插桩，以便与基线进行公平比较。所有模糊测试活动均运行12小时，使用单线程和空种子语料库。

**主要结果**：
- 在方法目标覆盖率下，生成的安全带相比OSS-Fuzz基线实现了**中位数26%** 的提升。
- 在完整目标范围覆盖率下，生成的安全带相比AutoFuzz和OSS-Fuzz基线分别实现了**中位数5%和6%** 的提升。
- 在12小时的模糊测试活动中，生成的安全带在已集成于OSS-Fuzz的项目中发现了**3个新错误**（commons-cli中2个空指针异常，jsoup中1个索引越界异常），且没有误报。
- 安全带生成的平均成本为**3.20美元**，平均时间为**599秒（约10分钟）**，显示出实用性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估范围相对有限，仅针对七个目标方法，且主要关注无状态或简单状态API。未来研究可首先扩展到复杂的状态化API，例如涉及数据库连接或会话管理的库，这需要智能体能够理解和生成跨多个调用的状态序列。其次，当前方法为单个方法生成测试套件，成本仍有优化空间；未来可探索如何识别“关键方法集”，即通过覆盖分析找到能以最小成本最大化库覆盖率的少量核心API入口，从而系统性降低生成开销。此外，论文侧重于基于崩溃的模糊测试，未来可探索生成“基于属性的安全测试套件”，即让智能体不仅调用API，还能自动推断并验证安全不变性（如内存安全、信息泄露等），从而直接检测更深层的逻辑漏洞。最后，多智能体架构的协作效率仍有提升可能，例如引入动态任务分配或基于覆盖反馈的智能体策略调整，以进一步减少上下文查询和迭代开销。

### Q6: 总结一下论文的主要内容

本文提出了一种用于Java库模糊测试的多智能体自动测试工具生成方法。核心问题是传统模糊测试需要人工编写测试工具（harness）来调用库API，这过程耗时且依赖专业知识。为解决此问题，作者设计了一个由五个基于LLM的ReAct智能体组成的架构，它们分工协作：研究、合成、编译修复、覆盖率分析和优化。方法上，智能体按需通过模型上下文协议查询文档和代码，而非预处理整个代码库，以保持上下文聚焦。关键创新包括：引入了方法定向覆盖率，仅在目标方法执行期间跟踪覆盖率以隔离目标行为；以及智能体引导的终止机制，通过检查未覆盖代码来区分有效的优化机会与收益递减情况。实验在六个广泛使用的Java库的七个目标方法上进行。结果表明，生成的测试工具在包范围覆盖率上比OSS-Fuzz基准中位数提升26%，并优于Jazzer AutoFuzz 5%。每个测试工具生成平均成本为3.20美元和10分钟，适合持续集成。在12小时模糊测试活动中，发现了3个已集成于OSS-Fuzz项目中的错误，证明了其有效性。该工作自动化了测试工具生成，显著提升了模糊测试对库代码的覆盖效率和实用性。
