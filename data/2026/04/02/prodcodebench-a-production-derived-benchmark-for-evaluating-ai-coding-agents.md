---
title: "ProdCodeBench: A Production-Derived Benchmark for Evaluating AI Coding Agents"
authors:
  - "Smriti Jha"
  - "Matteo Paltenghi"
  - "Chandra Maddila"
  - "Vijayaraghavan Murali"
  - "Shubham Ugare"
  - "Satish Chandra"
date: "2026-04-02"
arxiv_id: "2604.01527"
arxiv_url: "https://arxiv.org/abs/2604.01527"
pdf_url: "https://arxiv.org/pdf/2604.01527v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.LG"
tags:
  - "代码智能体"
  - "评测基准"
  - "生产环境"
  - "工具使用"
  - "验证机制"
relevance_score: 7.5
---

# ProdCodeBench: A Production-Derived Benchmark for Evaluating AI Coding Agents

## 原始摘要

Benchmarks that reflect production workloads are better for evaluating AI coding agents in industrial settings, yet existing benchmarks differ from real usage in programming language distribution, prompt style and codebase structure. This paper presents a methodology for curating production-derived benchmarks, illustrated through ProdCodeBench - a benchmark built from real sessions with a production AI coding assistant. We detail our data collection and curation practices including LLM-based task classification, test relevance validation, and multi-run stability checks which address challenges in constructing reliable evaluation signals from monorepo environments. Each curated sample consists of a verbatim prompt, a committed code change and fail-to-pass tests spanning seven programming languages. Our systematic analysis of four foundation models yields solve rates from 53.2% to 72.2% revealing that models making greater use of work validation tools, such as executing tests and invoking static analysis, achieve higher solve rates. This suggests that iterative verification helps achieve effective agent behavior and that exposing codebase-specific verification mechanisms may significantly improve the performance of externally trained agents operating in unfamiliar environments. We share our methodology and lessons learned to enable other organizations to construct similar production-derived benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何构建一个能真实反映工业场景下生产工作负载的AI编程助手评估基准的问题。当前，评估AI编程助手的方法各有局限：在线A/B测试虽能获得高保真信号，但耗时耗力且可能影响用户体验；影子部署避免了用户干扰，却因非确定性而难以复现；而使用现有公开基准（如SWE-Bench）进行离线评估虽快速可复现，但其任务来源（如GitHub问题）与工业实际在编程语言分布（以Python为主 vs. 多语言代码库）、提示风格（结构化问题描述 vs. 非正式开发者请求）和代码库结构（独立仓库 vs. 包含多项目共享基础设施的大型单体仓库）上存在显著差异。这些差异导致现有基准难以准确评估AI助手在真实生产环境中的表现。

因此，本文的核心问题是：如何从实际生产数据中构建一个既保留真实交互特征（如原始提示、多语言任务分布），又能提供稳定、基于执行的自动化评估信号的基准。为此，论文提出了ProdCodeBench，一个从生产AI编程助手真实会话中提炼的基准，其每个样本包含原始提示、已提交的代码变更以及一组“失败转通过”的测试，从而无需依赖LLM评判即可自动验证正确性。研究通过设计一套包含LLM任务分类、测试相关性验证和多轮稳定性检查的数据筛选流程，解决了单体仓库环境中构建可靠评估信号所面临的挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：评测基准、开发者交互研究和模型训练方法。

在**评测基准**方面，第一代基准（如HumanEval、MBPP）专注于从自然语言生成独立函数，评估功能正确性。第二代基准（如SWE-bench及其变体SWE-bench Verified、SWE-Gym）将评估置于真实代码库环境中，使用GitHub问题描述作为任务来源。本文提出的ProdCodeBench与SWE-bench共享代码库级评估范式，但关键区别在于任务提示的来源：现有基准使用开发者间沟通的GitHub问题描述，而本文直接从开发者与AI编码助手的真实交互会话中提取逐字提示，更贴近实际使用场景。

在**开发者交互研究**方面，多项实证研究（如Barke等人对GitHub Copilot使用模式的观察、Vaithilingam等人对开发者价值的分析）揭示了开发者与AI工具交互的具体模式（如加速模式和探索模式）及信任因素。这些研究为理解真实交互提供了基础，但现有评测基准未能捕捉这些真实交互。本文的基准直接源于实际使用数据，填补了这一空白。

在**模型训练与改进方法**方面，自动程序修复（APR）研究（如ChatRepair）表明，结合测试反馈能有效提升模型性能。强化学习方法（如CodeRL、RLEF）利用测试结果作为奖励信号来训练模型。本文的基准通过其测试分类方案（如失败到通过的测试）支持此类训练范式，为构建细粒度奖励信号提供了基础。此外，本文还通过多运行稳定性检查应对测试不稳定性，并采用滚动更新设计来缓解数据污染问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ProdCodeBench的基准测试来解决如何评估AI编程助手在真实生产环境中的表现问题。其核心方法是直接从生产环境中采集真实的开发者与AI助手交互数据，并设计了一套严格的数据筛选和验证流程，以确保评估信号可靠且贴近实际工作负载。

整体框架围绕三个目标构建：反映真实的开发者提示、在大型工业级单体仓库中运行、提供可靠的基于执行的评估信号。主要模块包括数据收集、任务筛选和测试验证三大环节。数据来源于集成了AI编程助手的IDE中记录的真实单轮对话，这些对话最终导致了代码变更被提交到主分支。每个基准任务包含三个组件：原始提示（保留真实措辞和上下文）、解决方案差异（已提交的代码变更）以及一组可执行测试。

关键技术体现在以下几个方面：
1. **数据筛选管道**：采用多级过滤器确保任务质量。首先通过LLM驱动的分类器排除无法用自动化测试评估的任务（如文档更新、UI调整）。其次，过滤掉引用解决方案差异的提示，防止代理通过版本控制系统“作弊”。最后，排除模板化或系统自动生成的提示，确保只保留真实的交互任务。

2. **测试验证机制**：为了解决单体仓库中“时间旅行”问题（即难以完全复现历史提交环境），论文设计了滚动基准方法，定期更新任务集以保持新鲜度。测试发现采用概率性检索，但进一步通过“测试相关性代理”进行验证，该代理配备代码搜索工具，分析代码变更是否真正影响特定测试，从而提高测试关联的精确性。随后，对候选测试进行多次执行，将其分类为“失败转通过”（F2P，核心评估信号）或“通过转通过”（P2P，回归测试），并排除不稳定测试。

3. **评估完整性保障**：通过从当前代码库中“回退”解决方案差异，确保代理在评估时无法直接访问已提交的解决方案。同时，仅选择可干净回退的变更，排除存在冲突的案例。

创新点包括：
- **真实性**：直接捕获真实开发者提示，包含企业上下文、内部术语和调试场景，与合成任务描述形成鲜明对比。
- **可靠性**：完全依赖可执行测试而非LLM评判，并通过多轮运行和测试分类确保评估信号稳定。
- **适应性**：支持多编程语言，任务类型涵盖错误修复、功能请求和重构，且设计为滚动更新，避免数据污染并保持与当前开发实践同步。

最终，该方法不仅提供了一个高质量基准，还通过分析发现，更充分利用工作验证工具（如执行测试、调用静态分析）的模型解决率更高，揭示了迭代验证对提升代理在陌生环境中性能的重要性。

### Q4: 论文做了哪些实验？

论文实验主要包括模型性能比较、评估工具链（harness）对比和定性分析三部分。实验在基准测试的“失败转通过”（F2P）子集上进行，即仅包含至少有一个“失败转通过”测试的代码变更。

在模型性能比较中，评估了多个大型语言模型（如Claude Opus、Claude Sonnet、Claude Haiku和GPT Codex），每个模型运行三次以测量方差。主要结果以解决率（solve rate）呈现，Claude Opus表现最佳，解决率达72.2%，Claude Sonnet为66.7%，Claude Haiku和GPT Codex分别为53.2%和55.6%（均附带95%置信区间）。分析发现，更频繁使用验证工具（如执行测试、调用静态分析）的模型解决率更高。

在评估工具链对比中，比较了两种工具链：功能有限的Agent-Basic和提供完整IDE类体验的Agent-IDE（工具数量约为前者的3倍）。实验还测试了“上下文文件”（Context Files，包含代码库内部知识的Markdown文件）的影响。结果显示，更强的Agent-IDE工具链显著提升了解决率；在较弱的Agent-Basic工具链上，模型间性能差异更大，而添加上下文文件能提升解决率，尤其对具有公司特定约定的编程语言帮助明显。

定性分析包括对任务分类器和测试相关性分类器的人工验证。采样30个任务进行人工标注，任务分类器与人工共识的二进制（可测试/不可测试）一致率达96.67%（29/30）。测试相关性验证采样15对（代码变更，测试），分类器与人工共识的一致率为80%（12/15），分歧主要出现在相关性的主观边界上。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，基准测试仅涵盖单轮交互，忽略了实际开发中常见的多轮调试、协作分解等复杂场景，这限制了其对智能体迭代和协作能力的评估。未来可纳入多轮对话数据，设计需要跨文件协调或领域知识的任务，以提升任务多样性和挑战性。其次，基准中约65%的样本为AI完全生成，可能导致评估偏向于模型自我一致性检验而非解决新问题，未来需区分数据来源，增强样本独立性。此外，当前解决率已达约70%，存在天花板效应，未来可通过纳入更复杂任务或不同助手的数据来提高区分度。在技术层面，可探索并行化测试执行、缓存机制以提升基准构建效率，并引入工作空间快照以还原真实开发环境。最后，基准的编程语言分布和任务复杂度可能不具备普适性，未来可扩展至更多样化的代码库和开发场景，以增强外部效性。

### Q6: 总结一下论文的主要内容

该论文提出了一种从实际生产环境中构建AI编程智能体评估基准的方法，并以ProdCodeBench为例进行说明。核心问题是现有基准在编程语言分布、提示风格和代码库结构上与真实工业场景存在差异。方法上，论文详细介绍了数据收集与筛选流程，包括基于LLM的任务分类、测试相关性验证和多轮稳定性检查，以解决从单体仓库环境中构建可靠评估信号的挑战。每个样本包含原始提示、已提交的代码变更和覆盖七种编程语言的测试用例。通过对四个基础模型的系统分析，发现解决率在53.2%至72.2%之间，且表现更好的模型更频繁地使用工作验证工具（如执行测试和静态分析）。主要结论表明，迭代验证有助于提升智能体效能，而暴露代码库特定的验证机制可显著改善外部训练智能体在陌生环境中的性能。该研究的意义在于提供了一套可复现的方法论，使其他组织能够基于自身生产数据构建类似的基准，从而更准确地评估AI编程智能体在真实工业场景中的能力。
