---
title: "One-Eval: An Agentic System for Automated and Traceable LLM Evaluation"
authors:
  - "Chengyu Shen"
  - "Yanheng Hou"
  - "Minghui Pan"
  - "Runming He"
  - "Zhen Hao Wong"
  - "Meiyi Qiang"
  - "Zhou Liu"
  - "Hao Liang"
  - "Peichao Lai"
  - "Zeang Sheng"
  - "Wentao Zhang"
date: "2026-03-10"
arxiv_id: "2603.09821"
arxiv_url: "https://arxiv.org/abs/2603.09821"
pdf_url: "https://arxiv.org/pdf/2603.09821v1"
github_url: "https://github.com/OpenDCAI/One-Eval"
categories:
  - "cs.CL"
tags:
  - "Agentic System"
  - "Automated Evaluation"
  - "Workflow Automation"
  - "Benchmarking"
  - "Human-in-the-Loop"
  - "Reproducibility"
  - "NL2Bench"
  - "Tool Use"
relevance_score: 7.5
---

# One-Eval: An Agentic System for Automated and Traceable LLM Evaluation

## 原始摘要

Reliable evaluation is essential for developing and deploying large language models, yet in practice it often requires substantial manual effort: practitioners must identify appropriate benchmarks, reproduce heterogeneous evaluation codebases, configure dataset schema mappings, and interpret aggregated metrics. To address these challenges, we present One-Eval, an agentic evaluation system that converts natural-language evaluation requests into executable, traceable, and customizable evaluation workflows. One-Eval integrates (i) NL2Bench for intent structuring and personalized benchmark planning, (ii) BenchResolve for benchmark resolution, automatic dataset acquisition, and schema normalization to ensure executability, and (iii) Metrics \& Reporting for task-aware metric selection and decision-oriented reporting beyond scalar scores. The system further incorporates human-in-the-loop checkpoints for review, editing, and rollback, while preserving sample evidence trails for debugging and auditability. Experiments show that One-Eval can execute end-to-end evaluations from diverse natural-language requests with minimal user effort, supporting more efficient and reproducible evaluation in industrial settings. Our framework is publicly available at https://github.com/OpenDCAI/One-Eval.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型评估过程中存在的高人工成本、低灵活性和结果可解释性不足的问题。随着大语言模型和多模态模型在工业系统中的快速应用，评估已成为模型开发、选择、迭代和部署前验证的关键环节。评估目标日益多样化和任务特定化，但现有评估方法存在明显不足。当前主流实践通常有两种方式：一是用户自行查找并复现特定任务的基准测试库，手动配置环境和运行脚本；二是依赖静态评估框架，需要用户显式配置模型、数据集、参数和指标。这两种方法虽在一定程度上标准化了执行流程，但仍要求用户投入大量精力去发现合适的基准、构建有效配置并解释结果，导致工作流高度依赖经验、迭代成本高且难以适应不断变化的评估需求。现有工具主要聚焦于执行和分数聚合，将基准和指标视为静态配置，很少涉及更高层次的阶段，如评估意图理解、个性化基准选择、配置验证或面向下游决策的结果分析。因此，评估输出往往局限于孤立的标量指标，不足以支持实际的工业决策。本文的核心问题是：如何将抽象的、自然语言表达的评估意图，自动、可靠地转化为可执行、可追溯且可定制的端到端评估工作流。为此，论文提出了One-Eval这一智能体评估系统，通过自然语言到基准的意图解析、自动化基准解析与配置验证、以及面向决策的度量与报告生成三个阶段，实现从自然语言请求到完整评估流程的自动化转换，并引入人在回路的检查点以确保可靠性和可审计性。

### Q2: 有哪些相关研究？

相关研究可分为三类。在模型评测方面，已有大量基准数据集（如GSM8K、MATH、MMLU）和标准化工具包（如lm-eval-harness、OpenCompass），它们提升了评测的可复现性，但通常预设了任务、基准和指标，需要用户手动将评测目标映射到具体设置。本文的One-Eval系统则通过智能体自动化整个流程，从自然语言请求直接生成可执行的工作流，实现了端到端的自动化，而非依赖预定义配置。

在自动化与智能体系统方面，现有研究已证明基于智能体的系统在代码生成、工具调用等多步骤任务中的有效性，能够通过分解目标来减少人工干预。然而，这些工作多集中于自动化孤立环节，而本文将评测视为一个完整的、由智能体驱动的决策过程，实现了从意图解析到结果分析的全程自动化与可追溯，解决了实践中自动化支持碎片化的问题。

在个性化评测与报告方面，传统研究多提供单一或聚合的指标分数，虽便于标准化比较，却难以支撑实际部署决策。虽有工作探索了多维度评测以更全面刻画模型行为，但其评测维度和报告格式往往固定。本文则强调基于用户目标和任务需求进行个性化评测规划，并生成面向决策的报告，超越了静态的标量分数输出。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为One-Eval的智能体化评估系统，将自然语言评估请求自动转换为可执行、可追溯且可定制的工作流，从而系统性地解决了大模型评估中手动操作繁琐、流程异构、结果解读困难等核心问题。

其核心方法是一个模块化的三阶段流水线架构，对应三个主要组件：NL2Bench、BenchResolve以及Metrics & Reporting。首先，**NL2Bench模块**作为入口，负责意图解析与基准规划。它通过“意图结构化”将用户自然语言请求解析为包含评估领域、能力焦点、约束条件等的结构化表示。随后，它采用“双源候选检索”策略：优先从本地精心维护的、包含77个已验证可执行基准的图库中检索，支持嵌入向量和TF-IDF两种检索后端；若高质量匹配不足，则动态回退至HuggingFace Hub进行实时搜索。最后，它在考虑评估成本、冗余度和可执行性等约束下进行选择，并通过“人在回路”机制允许用户审查、编辑和确认最终基准计划。

其次，**BenchResolve模块**负责基准解析与配置，确保工作流的可执行性。它采用“分层解析策略”：对于高频基准，直接从本地注册表加载预验证配置以保证稳定性；对于未见过的基准，则动态回退至HuggingFace进行解析与下载。关键创新在于“统一配置与异构数据适配”，它将所有解析后的基准归一化为一个统一的配置对象（BenchInfo），其中记录了数据源、评估子集、列映射和任务元数据，从而将评估逻辑与异构的数据表示解耦，实现了可追溯和可复现的执行。

最后，**Metrics & Reporting模块**是分析核心，负责生成面向决策的评估报告。其创新点体现在：1) **双轨制指标推荐**：优先采用用户或基准元数据中的显式配置；对于未配置的开放任务，则让智能体基于数据集上下文进行语义推理，从运行时扫描的指标库中动态选择；若无有效结果则回退至规则建议，确保了灵活性与鲁棒性。2) **分层诊断报告**：超越单一的标量分数，生成宏观（能力剖析雷达图）、诊断（根因分析，如归因错误模式）和微观（失败案例检查）三个层次的报告。3) **去中心化指标注册**与**专用指标库**：支持通过装饰器轻松扩展新指标，并内置了用于捕获特定失败模式（如数学符号等价性、格式合规性）的专用指标，支撑深度分析。

整体上，One-Eval的创新在于将评估建模为一个由用户意图驱动、各阶段互联的端到端决策过程，并通过智能体协调、分层解析、人在回路以及分层报告等关键技术，实现了评估流程的自动化、可定制化与结果的可操作化。

### Q4: 论文做了哪些实验？

论文进行了三项互补的实验研究。实验设置上，作者从工业可用性和可靠性角度评估One-Eval系统，而非追求固定基准测试集的排行榜性能提升。

第一项是定性案例研究，通过一个真实运行示例（用户请求：“关注广泛常识覆盖，并检查模型是否能处理一些轻度推理”）来展示完整工作流程和面向决策的报告生成。系统将请求解析为意图槽，通过NL2Bench规划基准（如MMLU、TruthfulQA、CommonsenseQA、GSM8K、MATH-500），并通过BenchResolve自动解析配置、划分数据集并进行模式归一化以确保可执行性。

第二项是受控的端到端成功率评估。研究收集了涵盖推理、数学、代码、安全性、检索和事实问答六大能力领域的100个自然语言评估请求，测量了三个累积成功率指标：计划可执行率（99/100，99%）、自动完成率（85/100，85%）和完整计划率（84/100，84%）。关键数据指标显示，整个8步流程的中位完成时间约为每请求11.4分钟（平均13分钟），平均处理令牌数为10,652。

第三项是特征级对比分析。通过对比表将One-Eval与lm-eval-harness、OpenCompass、HELM等代表性评估框架进行比较，重点关注定制化、端到端自动化、基于意图的基准推荐和指标推荐等关键能力。结果显示，One-Eval是唯一在这四项功能上均支持（标记为✓）的框架，而其他框架在自动化或推荐功能上存在缺失。

### Q5: 有什么可以进一步探索的点？

该论文提出的自动化评估系统在提升效率和可追溯性方面有显著贡献，但仍有多个方向值得深入探索。首先，系统目前主要面向文本任务，未来可扩展至多模态（如图像、音频）评估，这需要设计统一的跨模态数据表示和适配的评估代理。其次，系统对长尾和小众基准的支持有限，可研究如何通过主动学习或少量样本泛化来自动发现和集成这类基准。此外，当前评估流程虽有人工审核点，但决策透明度不足；未来可引入可解释性模块，让系统不仅输出结果，还能解释评估指标的选择依据和潜在偏差。另一个重点是动态环境适应：随着模型和任务快速演进，系统需能自动更新评估策略，例如通过元学习调整工作流。最后，从工业部署角度，系统可探索分布式评估和实时监控能力，以支持大规模、持续性的模型评测需求。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为One-Eval的智能评估系统，旨在解决大语言模型评估中手动工作繁重、流程复杂且难以复现的问题。其核心贡献是构建了一个将自然语言请求自动转换为可执行、可追溯且可定制化评估工作流的智能体系统。

论文定义的问题是如何自动化处理从评估意图理解到最终报告生成的整个评估流程，以减少人工干预并提升效率与可复现性。方法上，One-Eval系统集成了三个关键模块：NL2Bench用于解析用户自然语言请求并规划个性化基准测试；BenchResolve负责自动获取和规范化数据集以确保可执行性；Metrics & Reporting则进行任务感知的指标选择并提供超越标量分数的决策导向报告。系统还设计了人工介入检查点以支持审核与回滚，并保留了样本证据链以供调试和审计。

主要结论表明，One-Eval能够以最少的用户努力，处理多样化的自然语言请求并完成端到端的评估，有效支持了工业场景中更高效、可复现的模型评估。该框架已开源，为自动化、可追溯的LLM评估提供了实用工具。
