---
title: "Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results"
authors:
  - "Benjamin Kohler"
  - "David Zollikofer"
  - "Johanna Einsiedler"
  - "Alexander Hoyle"
  - "Elliott Ash"
date: "2026-04-23"
arxiv_id: "2604.21965"
arxiv_url: "https://arxiv.org/abs/2604.21965"
pdf_url: "https://arxiv.org/pdf/2604.21965v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Scientific Agent"
  - "Reproducibility"
  - "Code Generation"
  - "Data Analysis Agent"
  - "Agent Evaluation"
  - "Error Attribution"
  - "Multi-Agent Scaffold"
relevance_score: 9.5
---

# Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results

## 原始摘要

Recent work has used LLM agents to reproduce empirical social science results with access to both the data and code. We broaden this scope by asking: Can they reproduce results given only a paper's methods description and original data? We develop an agentic reproduction system that extracts structured methods descriptions from papers, runs reimplementations under strict information isolation -- agents never see the original code, results, or paper -- and enables deterministic, cell-level comparison of reproduced outputs to the original results. An error attribution step traces discrepancies through the system chain to identify root causes. Evaluating four agent scaffolds and four LLMs on 48 papers with human-verified reproducibility, we find that agents can largely recover published results, but performance varies substantially between models, scaffolds, and papers. Root cause analysis reveals that failures stem both from agent errors and from underspecification in the papers themselves.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：能否仅凭论文的方法描述和原始数据，自动重现社会科学研究的结果，而无需访问原始分析代码。研究背景是基于当前大型语言模型（LLM）代理已能利用数据和代码复制结果，但现实是科学研究的核心传播载体是论文本身，而非代码。现有方法的不足在于依赖代码重现，忽略了论文方法描述的充分性验证；同时，论文中的方法描述常存在模糊或缺失（如具体的统计参数、数据预处理步骤等），导致人工重现困难。本文的核心贡献是构建了一个代理重现系统，通过严格的信息隔离（禁止代理接触原始代码、结果及论文全文），要求代理仅根据从论文中提取的结构化方法描述和原始数据，从零开始重新实现分析管道并输出结果。系统还设计了误差归因步骤，以追溯失败根源。实验表明，虽然前沿LLM代理能显著恢复结果（如85%的情况下符号匹配），但不同模型和框架间性能差异大，且失败原因既包括代理的理解执行错误，更关键的是论文本身的方法描述不足。

### Q2: 有哪些相关研究？

相关研究主要分为两类。在方法类工作中，ML领域有CORE-Bench、PaperBench、Paper2Code和AutoReproduce等系统，它们评估智能体复现代码架构和结果的能力；在社会科学领域，REPRO-Bench、PaperRepro和ReplicatorBench等基准测试允许智能体访问原始代码。与这些工作不同，本文的智能体仅基于论文方法描述和原始数据生成代码，完全隔离原始代码、结果和论文全文，避免了信息泄露问题。在应用类工作中，ReplicatorBench要求智能体获取新数据测试相同假设（复制而非复现），而本文严格聚焦于复现（使用相同数据）。在评测类工作中，大多数现有研究采用LLM作为法官进行评价，本文则采用确定性评估方法，将复现输出直接与原始值进行比较，并根据真实标准误调整统计显著性，避免了LLM评价的不可靠性。本文的核心创新在于实现了从论文方法到代码的端到端复现，并通过错误归因步骤追溯复现失败的根本原因，揭示了失败既源于智能体错误也源于论文本身的方法描述不充分。

### Q3: 论文如何解决这个问题？

论文构建了一个多步骤的流水线系统，用于评估LLM智能体仅凭论文方法描述和原始数据复现社会科学结果的能力。整体框架分为四个核心步骤：提取、重实现、评估和归因。

首先，方法提取步骤将完整PDF输入LLM，提取结构化方法描述，包括研究问题、数据描述、数据操作和结果表格的详细说明（不含数值），以严格隔离原始结果和代码。结果提取与盲化步骤则从论文表格中提取数值，生成结构化表示，并创建盲化模板供智能体填充。数据提取步骤从复现包中识别所需的最小可行数据集。

其次，重实现步骤中，自主LLM智能体在隔离沙箱环境中，仅访问提取的方法、盲化模板和数据，为每个表格编写Python脚本并运行，禁止访问原始代码、结果或论文PDF。系统通过正则扫描和LLM审查两阶段审计工具，确保信息隔离，并通过硬编码审计验证输出是否源于真实计算。

关键技术包括确定性单元格级比较，通过符号一致性和百分比偏差将数值结果划分A-F等级；以及误差归因步骤，利用LLM分析失败单元格，定位原始代码和智能体代码的差异，并由审计器识别四大错误类型：人工错误（数据缺失、论文与代码矛盾）和智能体错误（方法提取不完整、智能体未遵循方法）。创新点在于严格的信息隔离设计、多维度审计机制和结构化误差归因，有效区分了智能体错误与论文本身表述不清的问题。

### Q4: 论文做了哪些实验？

该论文的实验旨在评估AI智能体仅根据论文方法描述与原始数据复现社会科学结果的能力。实验设置包括四种智能体框架（SWE-Agent、OpenCode、Codex GPT-5.4、Claude Code Opus 4.6）和四种LLM（GPT-5.4、GPT-5.3、GLM-5、Opus 4.6），在48篇经人工验证可复现的论文上进行测试。主要结果如下：在系数层面，最佳智能体（OpenCode GPT-5.4）的符号匹配率达91%，且超过80%的复现系数落在原始系数的95%置信区间内。在表格与论文层面，最强智能体复现近完美表格（A级）的数量是较弱者的两倍，但超过60%的表格能达到B级（差异在20%内）。错误溯源分析显示，大部分偏差源于论文本身的描述不充分（原始错误）或数据缺失；智能体错误是第二大原因，但最强的智能体此项占比显著降低。此外，消耗更多计算资源（令牌数、时间、成本）的智能体表现更好，揭示了性能与算力投入之间的权衡。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于：即使是最好的代理系统，其成功复现也高度依赖于论文本身的描述充分性，且存在显著的计算成本-性能权衡。未来可探索的方向包括：第一，改进方法论提取环节，通过交互式问答而非单次提取来消除歧义，尤其针对论文中未明确说明的数据缩放、变量编码等细节；第二，设计自适应计算预算分配机制，让系统能根据任务难度动态调整token消耗，而非简单增加算力投入；第三，开发更鲁棒的误差归因方法，区分“代理能力不足”与“论文描述不完整”导致的失败，并探索向作者反馈回路以补全方法描述缺失；第四，当前系统仅依赖文本和方法描述，未来可引入跨论文的常识推理或领域知识图谱来弥补信息缺失；第五，评估框架可扩展到更复杂的因果推断、面板数据等计量方法，检验代理在不同范式下的泛化能力。

### Q6: 总结一下论文的主要内容

本文研究了大语言模型智能体在仅凭论文方法描述和原始数据的情况下复现社会科学研究结果的能力。当前问题在于：现有工作依赖代码复现，但论文本身作为科学传播的权威载体，其方法描述是否足以支持从零复现尚待验证。论文开发了一个智能体复现系统，通过从论文中提取结构化方法描述，在严格信息隔离条件下（智能体从未见过原始代码、结果或论文）重新实现分析流程，并实现结果与原始结果的确定性格级对比。系统还引入错误归因步骤，追踪偏差根源。对48篇经人工验证可复现论文的测试表明，前沿智能体在复现中表现良好，最优方案（GPT-5.4搭载OpenCode脚手架）可实现85%以上系数符号一致性和70%以上置信区间覆盖。然而模型和脚手架间性能差异显著，性能提升伴随更高计算成本。根因分析揭示，复现失败主要源于论文方法描述不充分和智能体对方法理解或执行偏差。该研究证明了智能体系统在弥合实证社会科学复现差距中的潜力，但仍需进一步改进。
