---
title: "TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis"
authors:
  - "Pepe Alonso"
date: "2026-03-18"
arxiv_id: "2603.17973"
arxiv_url: "https://arxiv.org/abs/2603.17973"
pdf_url: "https://arxiv.org/pdf/2603.17973v1"
github_url: "https://github.com/pepealonso95/TDAD"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "AI Coding Agent"
  - "Tool Use"
  - "Benchmark"
  - "Code Regression"
  - "Graph-Based Analysis"
  - "SWE-bench"
  - "Agent Skill"
relevance_score: 8.0
---

# TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis

## 原始摘要

AI coding agents can resolve real-world software issues, yet they frequently introduce regressions, breaking tests that previously passed. Current benchmarks focus almost exclusively on resolution rate, leaving regression behavior under-studied. This paper presents TDAD (Test-Driven Agentic Development), an open-source tool and benchmark methodology that combines abstract-syntax-tree (AST) based code-test graph construction with weighted impact analysis to surface the tests most likely affected by a proposed change. Evaluated on SWE-bench Verified with two local models (Qwen3-Coder 30B on 100 instances and Qwen3.5-35B-A3B on 25 instances), TDAD's GraphRAG workflow reduced test-level regressions by 70% (6.08% to 1.82%) and improved resolution from 24% to 32% when deployed as an agent skill. A surprising finding is that TDD prompting alone increased regressions (9.94%), revealing that smaller models benefit more from contextual information (which tests to verify) than from procedural instructions (how to do TDD). An autonomous auto-improvement loop raised resolution from 12% to 60% on a 10-instance subset with 0% regression. These findings suggest that for AI agent tool design, surfacing contextual information outperforms prescribing procedural workflows. All code, data, and logs are publicly available at https://github.com/pepealonso95/TDAD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI编程代理在修复软件问题时频繁引入回归错误（即破坏先前通过的测试）的核心挑战。研究背景是，当前基于大语言模型的编码代理在解决真实世界软件问题（如SWE-bench Verified基准测试中的GitHub问题）方面已展现出强大能力，但现有评估几乎完全聚焦于“解决率”（即代理生成的补丁能否通过特定问题测试），而忽视了回归行为。然而，回归在实践中至关重要——一个修复了一个错误却破坏了其他多个功能的补丁在代码审查中会被拒绝。

现有方法的不足在于：代理缺乏对代码-测试依赖关系的结构性认知。代理面临两难选择：要么运行仓库中的所有测试（这在测试套件庞大时不可扩展），要么仅运行更改文件附近的测试（这会遗漏因共享接口变更导致的间接依赖，而单纯的代码差异无法揭示这些传递关系）。例如，基线实验中，普通代理在100个实例中导致了562次“通过到失败”的测试错误，平均每个补丁破坏6.5个测试，甚至出现单个补丁破坏全部322个测试的极端案例。尽管SWE-bench评估工具已收集了衡量回归所需的数据（如PASS_TO_PASS测试集），但这些数据并未在排行榜或评估报告中得到重视。近期研究也证实，约一半通过SWE-bench的补丁在实际中不会被维护者合并，CI/CD失败是代理提交的拉取请求被拒的主要原因。

因此，本文要解决的核心问题是：如何让AI编码代理在生成补丁时，能有效减少回归错误，并将回归率提升为与解决率同等重要的一级评估指标。为此，论文提出了TDAD（测试驱动的代理开发），这是一个开源工具和基准方法，它通过构建基于抽象语法树的代码-测试依赖图，并进行加权影响分析，来识别最可能受更改影响的测试，从而为代理提供上下文信息（即“需要检查哪些测试”），而非仅仅规定工作流程（如如何执行TDD）。该方法旨在以零依赖集成的方式，帮助代理在无需运行全部测试的情况下，精准预测和避免回归。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：评测基准、回归测试方法与图结构应用。在评测基准方面，SWE-bench 是评估AI编程代理解决GitHub问题的主要基准，其衍生工作如SWE-bench Verified、SWE-Agent、AutoCodeRover、OpenHands、SWE-smith、SWE-Bench++和SWE-CI等，均聚焦于提升问题解决率，但普遍忽视了对回归行为的系统评估。本文的TDAD则填补了这一空白，专门针对代理引入的代码回归问题构建基准和方法，强调仅关注解决率会鼓励激进修改而忽略副作用。

在回归测试方法上，软件工程领域已有长期研究，如回归测试选择（RTS）与优先级排序（Elbaum等人综述）、静态RTS（Legunsen等人）、动态文件级依赖跟踪（Gligoric等人）以及方法级变更影响分析（Chianti）。TDAD借鉴了这些经典思想，但将其创新地应用于AI编程代理场景：传统RTS旨在优化开发者工作流，而TDAD则利用影响分析主动告知代理哪些测试可能受影响，使其在提交前能自我修正，从而减少回归。

在图结构应用方面，代码属性图统一了AST、控制流图和程序依赖图用于漏洞检测；GraphRAG证明图结构检索在复杂推理中优于扁平向量搜索；GRACE构建多层代码图以提升代码补全效果。TDAD采用了类似的“图优先”原则，但针对不同任务：它通过构建显式的代码-测试依赖图，并基于加权影响分析精准定位受影响的测试，而非用于代码补全或漏洞检测。此外，本文还涉及测试驱动开发（TDD）的相关研究（如Cui和Rehan的工作），但指出仅靠TDD提示可能增加回归，而提供具体的上下文信息（如哪些测试需验证）对代理更为有效。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为TDAD（测试驱动的智能体开发）的系统和流程来解决AI编程智能体频繁引入回归错误的问题。其核心方法是构建一个基于抽象语法树（AST）的代码-测试依赖图，并利用加权影响分析来精准识别可能受代码变更影响的测试，从而引导AI智能体在修改代码后优先验证这些关键测试，而非盲目运行所有测试或遵循可能产生误导的流程指令。

整体框架分为两个主要阶段。第一阶段是索引，它解析Python代码库并构建代码-测试依赖图。该阶段包含三个核心组件：AST解析器（使用Python标准库ast模块提取函数、类、导入和调用关系）、图构建器（根据解析结果创建代表文件、函数、类和测试的节点，并通过CONTAINS、CALLS、IMPORTS、INHERITS等边类型建立静态关系）以及测试链接器（这是最关键组件，它通过命名约定、前缀匹配和目录邻近性三种策略，创建连接测试节点与其所测试代码的TESTS边）。最终生成一个包含四种节点类型和五种边类型的图结构。

第二阶段是影响分析。当给定变更的文件列表时，系统并行运行四种分析策略来计算每个相关测试的“影响分数”。这四种策略及其基础权重（平衡配置下）分别是：直接测试变更代码（权重0.95）、通过1-3层调用链与变更代码关联（权重0.70）、文件级依赖（权重0.80）以及导入变更文件（权重0.50）。最终分数由策略权重和链接置信度加权合并得出。系统根据分数将测试分为高、中、低三个优先级，并输出一个静态的、可被grep搜索的文本文件（test_map.txt），其中列出了源文件到可能受影响测试文件的映射。

TDAD的创新点主要体现在三个方面。首先，它提出了一个轻量级、无运行时依赖的集成方案：AI智能体仅需接收test_map.txt和一个简短的技能定义文件（SKILL.md，约20行），即可通过grep查找并运行相关测试，无需复杂的图数据库服务器或API调用。其次，论文通过实验发现，为智能体提供“上下文信息”（即告知它需要验证哪些测试）比规定“工作流程”（如如何执行TDD）更能有效减少回归错误并提高问题解决率，这一发现对AI智能体工具设计具有指导意义。最后，系统设计了灵活的后端，默认使用内存中的NetworkX图以简化部署，同时保留Neo4j后端选项以支持大规模场景，并通过自动改进循环不断优化流程，显著提升了智能体的性能。

### Q4: 论文做了哪些实验？

论文在SWE-bench Verified数据集上进行了多阶段实验，评估TDAD方法在减少AI编码代理引入的回归问题上的效果。实验设置包括两个主要阶段：Phase 1使用Qwen3-Coder 30B模型在100个实例上进行测试，对比了三种方法：Vanilla（基线）、TDD Prompt（仅测试驱动开发提示）以及GraphRAG+TDD（结合基于AST的代码-测试图与加权影响分析）。Phase 2则使用Qwen3.5-35B-A3B模型与OpenCode代理框架，在25个实例上评估了将TDAD打包为可复用技能的效果。

主要结果如下：在Phase 1中，GraphRAG+TDD将测试级回归率从Vanilla的6.08%显著降低至1.82%（降幅70%），同时将P2P测试失败数从562减少至155（降幅72%）。与TDD Prompt相比，回归率降低幅度更大（从9.94%降至1.82%）。值得注意的是，仅使用TDD提示反而使回归率上升至9.94%。分辨率方面，GraphRAG+TDD为29%，略低于Vanilla的31%，但作者指出这是因为代理在测试图指示高风险时更倾向于生成空补丁（26% vs. 14%），体现了保守偏差。在Phase 2中，TDAD技能将分辨率从基线的24%提升至32%，生成率从40%提升至68%，且回归率保持为0%。

此外，论文还设计了一个自主自动改进循环，在10个实例子集上进行15轮迭代优化。结果显示，生成率从28%提升至80%，分辨率从12%提升至60%，且所有迭代均保持0%回归率。关键改进包括将技能文档从107行简化为20行，以及优化测试映射启发式方法。这些实验表明，提供上下文信息（如指示需验证哪些测试）比规定程序性工作流程更能有效提升AI代理的代码修改质量。

### Q5: 有什么可以进一步探索的点？

论文的局限性为：样本规模较小（共125个实例），仅使用两种较小规模本地模型，且局限于Python语言和静态分析，无法处理动态行为。外部有效性受限于所选仓库类型和模型规模，构造效度上则未能区分测试失败的重要性差异。

未来研究方向包括：在更大规模数据集（如完整的500实例集）和更多样化模型（特别是前沿大模型）上验证方法的普适性。技术层面，可探索将方法扩展到其他编程语言（利用Tree-sitter等统一解析器），并尝试结合动态分析以捕捉运行时依赖。此外，可研究更精细的回归严重性度量，而非简单计数，例如结合测试类型或业务关键性进行加权。

可能的改进思路：可以设计一种混合方法，将论文中的图影响力分析与轻量级符号执行或动态追踪相结合，以部分弥补静态分析的不足。对于智能体设计，可进一步研究如何自适应地提供上下文信息——根据模型能力、问题复杂度和可用上下文窗口，动态调整信息密度与流程指令的比例，而非固定策略。

### Q6: 总结一下论文的主要内容

该论文提出了TDAD（测试驱动智能体开发）工具与方法，旨在解决AI编程智能体在修复代码时频繁引入回归错误（即破坏原有通过测试）的问题。当前基准大多只关注解决率，而忽视了回归行为。TDAD的核心贡献在于结合基于抽象语法树（AST）的代码-测试图构建与加权影响分析，以识别最可能受代码变更影响的测试，从而减少回归。

方法上，TDAD通过构建代码与测试间的依赖图，量化变更的影响范围，引导智能体优先验证高风险测试。实验在SWE-bench Verified基准上进行，使用两个本地模型评估。结果显示，TDAD的GraphRAG工作流将测试级回归降低了70%（从6.08%降至1.82%），且作为智能体技能部署时将解决率从24%提升至32%。一个重要发现是，仅使用TDD（测试驱动开发）提示反而增加了回归（达9.94%），表明较小模型更受益于上下文信息（指明验证哪些测试），而非流程指令（如何执行TDD）。此外，自主改进循环在10个实例子集上将解决率从12%提升至60%，且回归率为0%。

论文结论强调，为AI智能体设计工具时，提供上下文信息优于规定工作流程，并呼吁社区采用综合指标（同时衡量解决率与回归率）来评估智能体的净贡献。未来工作包括扩展多语言支持、集成动态覆盖数据以提高分析精度，以及在更大规模模型上验证TDD提示悖论。
