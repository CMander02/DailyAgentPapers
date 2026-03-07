---
title: "SorryDB: Can AI Provers Complete Real-World Lean Theorems?"
authors:
  - "Austin Letson"
  - "Leopoldo Sarra"
  - "Auguste Poiroux"
  - "Oliver Dressler"
  - "Paul Lezeau"
date: "2026-03-03"
arxiv_id: "2603.02668"
arxiv_url: "https://arxiv.org/abs/2603.02668"
pdf_url: "https://arxiv.org/pdf/2603.02668v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Reasoning & Planning"
  - "Code & Software Engineering"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Code & Software Engineering"
  domain: "Scientific Research"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "Gemini Flash, N/A"
  key_technique: "N/A"
  primary_benchmark: "SorryDB"
---

# SorryDB: Can AI Provers Complete Real-World Lean Theorems?

## 原始摘要

We present SorryDB, a dynamically-updating benchmark of open Lean tasks drawn from 78 real world formalization projects on GitHub. Unlike existing static benchmarks, often composed of competition problems, hillclimbing the SorryDB benchmark will yield tools that are aligned to the community needs, more usable by mathematicians, and more capable of understanding complex dependencies. Moreover, by providing a continuously updated stream of tasks, SorryDB mitigates test-set contamination and offers a robust metric for an agent's ability to contribute to novel formal mathematics projects. We evaluate a collection of approaches, including generalist large language models, agentic approaches, and specialized symbolic provers, over a selected snapshot of 1000 tasks from SorryDB. We show that current approaches are complementary: even though an agentic approach based on Gemini Flash is the most performant, it is not strictly better than other off-the-shelf large-language models, specialized provers, or even a curated list of Lean tactics.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自动定理证明（ATP）领域评估基准存在的局限性问题。研究背景是，随着形式化方法在数学领域的复兴，特别是基于Lean交互式定理证明器的大规模形式化项目（如Liquid Tensor Experiment）的兴起，自动定理证明技术显示出协助数学家完成复杂形式化工作的潜力。然而，现有评估方法主要依赖于静态的、基于竞赛问题（如国际数学奥林匹克、miniF2F）构建的数据集，这些方法存在明显不足：首先，它们与数学家的实际工作需求脱节，未能涵盖真实项目中的复杂依赖关系、广泛的数学背景以及实际应用中的“混乱”情况；其次，这些基准易于饱和，使得评估不同证明器的性能变得困难，阻碍了领域进展；最后，公开数据集的解决方案可能泄露到训练数据中，导致难以区分模型是在“记忆”还是在展现“泛化推理能力”。

针对这些问题，本文的核心目标是构建一个名为SorryDB的动态更新基准。该基准直接从GitHub上78个活跃的Lean形式化项目中提取尚未被证明（即标记为“sorry”占位符）的定理任务。通过这种方式，SorryDB旨在评估自动定理证明器在真实、动态且具有实际价值的数学形式化项目中的实用能力，从而弥补现有基准在实用性、对齐性和防污染方面的缺陷，为衡量AI对新颖形式化数学项目的贡献能力提供一个更鲁棒的度量标准。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 交互式定理证明器与形式化数学库**：研究背景涉及使用如Lean等交互式定理证明器进行数学形式化，并依赖Mathlib等库。本文的SorryDB基准直接源于此类真实项目中的未完成证明（`sorry`占位符），与静态竞赛数据集形成对比。

**2. 竞赛数学基准**：现有主流评估数据集（如PutnamBench、miniF2F、ProofNet）多集中于奥林匹克或本科竞赛题目。本文指出这些数据集覆盖范围窄、可能已被训练数据污染且性能趋于饱和，而SorryDB旨在弥补这一局限，专注于更广泛的真实世界形式化项目。

**3. 形式化项目基准**：先前工作如FormalML和RLMEval已尝试从真实Lean项目中提取任务，但规模较小且领域特定。miniCTX等虽扩大来源，仍聚焦于已证明定理。本文的SorryDB则系统性地构建了更大规模、动态更新的基准，强调包含未公开解决方案的新任务，以更好反映实际开发需求并降低数据污染风险。

**4. 实用基准构建方法**：受软件工程领域（如SWE-bench、CodeSearchNet）使用真实GitHub任务评估智能体的启发，SorryDB借鉴了“从实际应用提取挑战”的理念，将其适配于定理证明场景，以衡量智能体对新颖形式化项目的贡献能力。

**5. 现有定理证明系统**：包括开源模型（如Kimina Prover、DeepSeek Prover）和专有系统（如AlphaProof、SeedProver）。这些系统多在竞赛问题上表现优异，但本文评估发现，它们在SorryDB的真实任务上各有优劣，且最先进的智能体方法（如基于Gemini Flash）并非全面优于其他现成模型或符号证明器，说明当前技术是互补的，也凸显了SorryDB作为评估工具的必要性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SorryDB的动态更新基准测试框架来解决“AI证明器能否完成现实世界中的Lean定理”这一问题。其核心方法是直接从活跃的开源Lean项目中提取未完成的证明义务（即占位符`sorry`关键字），形成一个持续演进的评估数据集，从而更真实地反映社区需求并缓解测试集污染问题。

整体框架包含两个主要部分：动态更新的基准测试数据集和用于提取与验证解决方案的框架。主要模块/组件包括：
1.  **仓库选择模块**：依据特定标准从Lean包注册表Reservoir中筛选GitHub仓库。标准包括：采用OSI批准的开源许可证、在2025年1月后仍有更新、仓库公开。最终从78个仓库中提取任务，这些仓库被手动分类为教学、工具、基准测试、库和具体形式化项目等类别，确保了问题的多样性和现实复杂性。
2.  **任务提取与处理模块**：该模块遍历选定的仓库，提取所有`sorry`关键字并存储元数据。随后进行过滤，确保任务可复现、严格需要证明，并进行去重以保留最新出现。这构成了基准测试的核心数据。
3.  **自动化验证管道**：这是关键技术组件。为了评估一个解决方案（即用于替换`sorry`的代码），该框架会利用LeanInteract工具，在特定位置检查证明状态，并验证整个代码能否成功编译，且最终状态中不包含任何`sorry`类的占位符。仅构建项目不足以验证，因为`sorry`本身在Lean中是语法有效的。此管道确保了评估的自动化和确定性。

创新点主要体现在：
*   **数据来源的动态性与真实性**：与由竞赛问题组成的静态基准不同，SorryDB直接从持续开发的实际形式化项目中提取任务，使其与社区需求对齐，更能评估AI对复杂依赖的理解和实际贡献能力。
*   **持续更新的机制**：通过提供持续更新的任务流，有效缓解了模型在静态测试集上过拟合（测试集污染）的问题，为智能体的长期能力评估提供了更鲁棒的指标。
*   **精细化的任务定义与验证**：将评估任务精确定义为“填充特定的`sorry`”，而非证明整个定理，这更贴合实际辅助编程场景。其验证方法不仅检查编译，还确保目标占位符被实质性解决，提高了评估的严谨性。

### Q4: 论文做了哪些实验？

论文在SorryDB-2601数据集的一个包含1000个任务（从78个GitHub仓库的5663个任务中选取，注重近期性和仓库多样性）的快照上进行了实验评估。实验设置包括评估多种方法：确定性策略（如trivial、ring、grind等，仅评估一次）、通用大语言模型（如GPT 5.2、Claude Opus 4.5、Gemini Flash/Pro 3、Qwen 3，评估pass@1和pass@32）、专用定理证明器（如Kimina Prover 8B、Goedel Prover V2 32B，评估pass@1和pass@32），以及迭代/智能体方法（基于Claude Opus 4.5和Gemini Flash 3的自校正方法，以及一个基于Gemini Flash 3、具有ReAct架构和LeanSearch工具调用的智能体方法，最多运行16次迭代）。

主要结果如下：在pass@1指标下，确定性策略（Tactics）解决8.4%的任务，通用LLM中Gemini Pro 3表现最佳（11.0%），专用证明器表现较弱（Goedel Prover V2为2.7%）。迭代方法显著提升性能，Gemini Flash 3智能体方法达到30.3%的解决率。所有方法共同解决了35.7%的任务，体现了互补性。关键数据指标显示，仅通过16次模型调用的迭代方法远优于32次并行采样（如Gemini Flash 3 pass@32为20.5%），表明错误反馈和环境测试极为有效。此外，不同方法在不同仓库类别上表现各异，教学类仓库任务更容易，而数学形式化项目更难；专用证明器在基准仓库上相对较好但泛化能力较弱。

### Q5: 有什么可以进一步探索的点？

该论文提出的动态基准SorryDB在评估AI定理证明能力方面具有创新性，但仍存在一些局限性和可探索的方向。首先，数据范围局限于Lean社区的项目，可能导致领域偏差，未来可扩展至其他证明辅助工具（如Coq、Isabelle）以提升泛化性。其次，当前验证流程限制了证明者添加导入或引理的能力，这可能阻碍复杂问题的解决；未来可放宽约束，允许更灵活的证明策略。此外，基准中的任务可能包含不可证明的命题，未来可通过尝试证明其否命题来识别这类任务，并引入类似Elo评分的相对评估机制。最后，验证流程可能存在漏洞（如sorryAx绕过），需集成更严格的检查工具（如Leanchecker）以确保可靠性。从研究视角看，可探索结合符号推理与LLM的混合方法，利用SorryDB的动态特性构建自适应评估框架，并设计针对数学依赖关系的结构化表示学习，以提升对复杂定理的理解能力。

### Q6: 总结一下论文的主要内容

该论文提出了SorryDB，一个动态更新的基准测试集，用于评估AI证明助手在真实世界数学定理形式化任务中的能力。其核心贡献在于构建了一个从GitHub上78个活跃的Lean形式化项目中提取的、持续更新的“sorry”语句（即待证明目标）数据库，这不同于由竞赛问题构成的静态基准。这确保了基准与形式化社区的实际需求对齐，并能缓解测试集污染问题。

方法上，论文从这些项目中收集未解决的证明目标，并选取了1000个任务快照，评估了包括通用大语言模型、智能体方法以及专用符号证明器在内的多种技术路径。主要结论显示，当前基于Gemini Flash的智能体方法表现最佳，但它并非在所有方面都严格优于其他现成大模型、专用证明器或精心设计的Lean策略集，表明不同方法具有互补性。SorryDB的意义在于为开发更强大、更实用的证明助手提供了一个能反映真实且不断演进的数学形式化需求的稳健评估框架。
