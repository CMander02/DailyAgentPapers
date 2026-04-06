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
pdf_url: "https://arxiv.org/pdf/2604.01527v2"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.LG"
tags:
  - "代码智能体"
  - "评测基准"
  - "生产环境"
  - "软件工程"
  - "任务评估"
  - "多语言编程"
  - "模型评估"
relevance_score: 8.0
---

# ProdCodeBench: A Production-Derived Benchmark for Evaluating AI Coding Agents

## 原始摘要

Benchmarks that reflect production workloads are better for evaluating AI coding agents in industrial settings, yet existing benchmarks differ from real usage in programming language distribution, prompt style and codebase structure. This paper presents a methodology for curating production-derived benchmarks, illustrated through ProdCodeBench, a benchmark sourced from real developer-agent sessions. We detail our data collection and curation practices including LLM-based task classification, test relevance validation, and multi-run stability checks which address challenges in constructing reliable evaluation signals from monorepo environments. Each curated sample consists of a verbatim prompt, a committed code change and fail-to-pass tests spanning seven programming languages. Our systematic analysis of four foundation models yields solve rates ranging from 53.2% to 72.2%. We demonstrate how these offline evaluation signals drive practical decisions around model selection and harness design, while noting that offline benchmarks provide directional signal that we complement with online A/B testing for production deployment decisions. We share our methodology and lessons learned to enable other organizations to construct similar production-derived benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何构建一个贴近实际生产环境的评估基准，以更可靠地评估AI编程助手（AI coding agents）在工业场景中的性能。研究背景是，随着AI编程助手越来越多地被部署到实际软件开发流程中，组织需要快速、可重复的方法来比较不同基础模型、验证智能体配置变更以及评估基础设施更新。然而，现有的评估方法各有局限：在线A/B测试虽然信号保真度高，但耗时长、资源消耗大且可能影响用户体验；影子部署避免了用户干扰，但存在非确定性和可复现性问题；而使用现有公开基准（如SWE-Bench）进行离线评估虽然快速可复现，但其任务来源（如Python GitHub问题）与真实工业工作负载在多个关键维度上存在显著差异，包括编程语言分布（以Python为主 vs. 多语言代码库）、提示风格（结构化问题描述 vs. 非正式的开发者请求）以及代码库结构（独立仓库 vs. 大规模单体仓库）。这些差异使得现有基准难以准确反映生产环境的真实需求。

因此，本文的核心问题是：如何从真实的生产数据中构建一个评估基准，以弥合现有评估方法与实际工业应用之间的差距。具体而言，该基准需要能够：1）保留原始的真实用户提示，而非人工合成；2）反映目标部署环境中真实的编程语言和任务类型分布；3）提供稳定、基于代码执行的评估信号，既适用于快速实验，也支持强化学习。为此，论文提出了一个可复现的方法论，并通过构建名为ProdCodeBench的基准（源自真实开发者与智能体的交互会话）进行具体阐述，以解决上述问题。

### Q2: 有哪些相关研究？

本文的相关研究可分为三大类：评测基准、开发者交互研究和模型训练方法。

在**评测基准**方面，相关工作分为两代。第一代基准（如HumanEval、MBPP）评估模型根据自然语言描述生成独立函数的能力，但脱离了真实开发环境。第二代基准（如SWE-bench及其变体SWE-bench Verified、SWE-Gym）将评估置于真实代码库上下文中，通过GitHub问题描述构建任务。本文提出的ProdCodeBench属于第二代，但关键区别在于任务来源：现有基准使用开发者间沟通的Issue描述，而本文直接采集开发者与AI助手交互的真实提示（verbatim prompts），这更能反映实际使用场景。其他多语言基准（如SWE-Sharp-Bench、Multi-SWE-bench）和跨文件评估基准（CrossCodeEval）也属于此类。

在**开发者交互研究**方面，多项实证研究分析了开发者与AI工具的互动模式。例如，Barke等人识别了“加速”和“探索”两种模式；Vaithilingam等人研究了Copilot对开发效率的影响；Xiao等人整理了开发者与ChatGPT的对话数据集。这些研究揭示了真实交互模式，但未转化为评测基准。本文则直接利用真实交互数据构建基准，填补了这一空白。

在**模型训练与改进**方面，自动程序修复（APR）研究（如ChatRepair）展示了如何利用测试反馈迭代改进代码生成。强化学习方法（如CodeRL、RLEF）使用测试结果作为奖励信号来训练模型。本文的基准设计（包含测试分类）可支持此类训练范式，提供细粒度的奖励信号构建。

此外，本文还考虑了**基准可靠性**问题，通过多轮稳定性检查应对测试不稳定性，并采用滚动更新设计（类似LiveCodeBench）缓解数据污染问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ProdCodeBench的、源自真实生产环境的基准测试来解决现有评估基准与工业场景脱节的问题。其核心方法是建立一个从真实开发者-Agent会话中提取、并经过严格筛选和验证的基准数据集，以确保评估任务在编程语言分布、提示风格和代码库结构上反映实际生产工作负载。

整体框架是一个数据筛选管道（Data Funnel），从海量的真实IDE内开发者-Agent单轮对话开始，通过多级过滤最终得到高质量的基准测试样本。每个样本包含三个核心组件：**原样保留的开发者自然语言提示**、**后续被批准并提交的代码变更（解决方案diff）**，以及一组**可执行的测试**。评估时，Agent在模拟的工业级单体代码库（monorepo）环境中工作，解决方案diff被隐藏，最终完全依赖测试执行结果（而非LLM评判）来提供通过/失败信号。

主要模块与关键技术包括：
1.  **数据收集与真实性保障**：直接从集成了AI编程助手的IDE中收集会话，并利用代码溯源（AI provenance）技术，精确追踪哪些AI生成的内容被开发者接受并最终提交，从而建立从对话到提交代码的可靠映射。为确保任务意图明确，仅选取单轮对话且对应唯一代码提交的会话。
2.  **提示质量过滤**：使用LLM分类器过滤掉无法通过自动化测试可靠评估的任务（如仅文档更新、UI调整）。同时，排除引用解决方案diff（可能让Agent通过版本控制系统“作弊”）或属于系统模板的提示，确保提示代表真实的开发者交互意图。
3.  **测试质量过滤与验证**：这是确保评估信号可靠的关键。首先，通过**概率性测试检索**发现与代码变更相关的测试，并排除不稳定、失败或禁用的测试。其次，构建一个**测试相关性Agent**，该Agent配备代码差异获取和代码搜索工具，用于分析变更内容，验证每个测试是否确实受到代码变更的影响（直接或间接），提高了测试发现的精确度。最后，进行**测试验证与分类**：在变更前和变更后的代码版本上多次执行候选测试，根据其行为稳定地将测试分类为“失败转通过”（Fail-to-Pass, F2P，作为主要评估信号）或“通过转通过”（Pass-to-Pass, P2P，作为回归测试），并排除执行不一致的测试。
4.  **滚动基准设计**：为应对大型单体代码库中工具链、索引和服务随时间推移而失效的“时间旅行”难题，基准被设计为**滚动更新**。定期用新样本刷新任务集，而非永久固定，这保证了基准与当前开发实践同步、免受数据污染，并维持足够的任务量。

创新点在于：1）**生产源头性**：基准完全源于真实生产会话，其提示天然包含企业内部语境、调试真实故障、遵循现有模式等合成基准缺乏的特征。2）**评估完整性**：通过回退（back out）解决方案diff、隐藏答案、严格过滤测试相关性及稳定性，在动态的工业代码库环境中构建了可靠的、基于执行的评估信号。3）**方法论系统性**：提供了一套完整、可复用的方法论，包括从数据收集、多级过滤（提示质量、测试质量）到滚动维护的完整流程，使其他组织能够构建类似的生产衍生基准。

### Q4: 论文做了哪些实验？

论文实验主要包括模型性能比较、评估工具链（harness）对比和定性分析三部分。实验在基准的“失败到通过”（F2P）子集上进行，该子集仅包含至少有一个相关失败测试的代码变更。

在实验设置上，研究评估了多个大语言模型，每个模型运行三次以测量方差。数据集为ProdCodeBench，其样本来源于真实的开发者-Agent会话，包含逐字提示、已提交的代码变更以及涵盖七种编程语言的失败到通过测试。对比方法涉及不同模型（如Claude Opus、Claude Sonnet、GPT 5.1 Codex）以及两种评估工具链：功能有限的Agent-Basic和提供完整IDE类体验（包含代码导航、诊断等更多工具）的Agent-IDE。此外，还评估了包含代码库知识的“上下文文件”的影响。

主要结果方面，模型解决率（solve rates）在53.2%到72.2%之间，Claude Opus表现最佳。关键数据指标包括：Claude Opus在Agent-IDE工具链上的解决率最高（约72.2%）；使用Agent-IDE工具链比Agent-Basic能显著提升解决率；在较弱的Agent-Basic工具链上，添加上下文文件也能提升性能。工具使用分布显示，Agent-Basic会触发更多搜索调用（例如GPT 5.1 Codex达48.5%），而Agent-IDE的导航更高效。对用于数据整理的LLM分类器进行的人工验证显示，其在任务分类和测试相关性判断上与人工标注的一致性分别达到96.67%和80%。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性分析，未来研究可从以下几个维度深入探索：首先，在任务设计上，当前基准局限于单轮交互，未能涵盖真实开发中常见的多轮调试、问题分解等协作模式。未来可构建支持迭代式对话的评估框架，并引入需要跨文件协调或领域知识的复杂任务，以提升基准的挑战性和生态效度。其次，在数据规模与质量方面，现有筛选流程导致样本量有限，难以支持基于强化学习的模型微调。可通过并行化测试执行、引入缓存机制来提升数据处理效率，同时扩展数据来源，纳入多轮对话记录及不同AI编程助手的数据，以丰富任务多样性。此外，评估环境的真实性有待加强，例如通过还原开发时的本地未提交变更快照，避免工具泄露解题信息，确保评估的公正性。最后，针对当前模型性能接近天花板的问题，需设计更具区分度的任务，并建立动态更新的基准体系，以持续追踪模型进展，同时结合在线A/B测试，使离线评估与线上部署决策形成互补。

### Q6: 总结一下论文的主要内容

该论文提出了一种从实际生产环境中构建AI编程智能体评估基准的方法，并以ProdCodeBench为例进行说明。核心贡献在于设计了一套系统化的数据收集与筛选流程，包括基于大语言模型的任务分类、测试相关性验证和多轮运行稳定性检查，以解决从单体仓库环境中提取可靠评估信号所面临的挑战。该方法生成的基准保留了原始用户提示、已提交的代码变更以及覆盖七种编程语言的测试用例，更真实地反映了工业场景下的使用模式，与现有基于GitHub问题的基准形成区别。对四个基础模型的系统评估显示，其解决率在53.2%至72.2%之间，性能更高的模型更倾向于使用工作验证工具，表明迭代验证能提升智能体效能。论文强调离线基准可提供方向性指导，辅助模型选择与工具设计，但实际部署决策需结合在线A/B测试。所提出的方法论具有可复现性，旨在帮助其他组织基于自身生产数据构建类似基准。
