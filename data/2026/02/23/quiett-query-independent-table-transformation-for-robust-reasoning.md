---
title: "QUIETT: Query-Independent Table Transformation for Robust Reasoning"
authors:
  - "Gaurav Najpande"
  - "Tampu Ravi Kumar"
  - "Manan Roy Choudhury"
  - "Neha Valeti"
  - "Yanjie Fu"
  - "Vivek Gupta"
date: "2026-02-23"
arxiv_id: "2602.20017"
arxiv_url: "https://arxiv.org/abs/2602.20017"
pdf_url: "https://arxiv.org/pdf/2602.20017v1"
categories:
  - "cs.CL"
tags:
  - "表格推理"
  - "数据预处理"
  - "查询无关处理"
  - "鲁棒性"
  - "下游任务增强"
relevance_score: 5.5
---

# QUIETT: Query-Independent Table Transformation for Robust Reasoning

## 原始摘要

Real-world tables often exhibit irregular schemas, heterogeneous value formats, and implicit relational structure, which degrade the reliability of downstream table reasoning and question answering. Most existing approaches address these issues in a query-dependent manner, entangling table cleanup with reasoning and thus limiting generalization. We introduce QuIeTT, a query-independent table transformation framework that preprocesses raw tables into a single SQL-ready canonical representation before any test-time queries are observed. QuIeTT performs lossless schema and value normalization, exposes implicit relations, and preserves full provenance via raw table snapshots. By decoupling table transformation from reasoning, QuIeTT enables cleaner, more reliable, and highly efficient querying without modifying downstream models. Experiments on four benchmarks, WikiTQ, HiTab, NQ-Table, and SequentialQA show consistent gains across models and reasoning paradigms, with particularly strong improvements on a challenge set of structurally diverse, unseen questions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实世界中表格数据因模式不规则、数值格式异构和隐含关系结构而导致下游推理和问答可靠性下降的问题。当前大多数方法以查询依赖的方式处理这些挑战，将表格清理与推理过程紧密耦合，例如通过提示策略（如思维链或程序链）或针对每个查询的表格转换来动态调整表格表示。这种做法限制了方法的泛化能力，因为模型需要针对每个具体查询重新解析表格，无法形成可复用的规范化表示，同时也违背了数据工程中“先转换、后查询”的最佳实践。

研究背景是，表格推理在自然语言理解任务中至关重要，但实际表格常包含混合单位、自由文本日期、多实体单元格等不规则内容，使得直接查询困难。现有方法虽能部分应对，却未将表格转换视为一个独立于查询的预处理步骤，导致效率低下且难以推广到结构多样的未见查询。

本文的核心问题是：能否在未见查询之前，将原始半结构化表格转换为单一、可重用且支持SQL查询的规范表示？为此，论文提出了QUIeTT框架，通过无损的模式与数值规范化、显式关系暴露以及原始快照保留，实现查询无关的表格转换，从而将表格预处理与下游推理解耦，提升推理的鲁棒性和效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、应用类和评测类。

在方法类研究中，相关工作主要围绕表格规范化与重构展开。轻量级规范化方法（如NormTab）主要对数值和日期进行标准化，并执行有限的调整（如转置），但将层次结构、隐式关系和异构布局等问题留待下游推理阶段处理，其假设模式基本固定。程序化表格重构方法（如Auto-Tables、DataMorpher和RelationalCoder）通过生成明确的转换程序（如SQL或Python脚本）进行更广泛的重构，但这些方法通常受限于预定义的运算符或与程序执行紧密耦合，且未强制生成单一、无损、可复用的表示形式。

在应用类研究中，部分工作将表格转换与推理过程紧密耦合。例如，TabFormer将表格重构与SQL回答联合进行，使得转换依赖于具体查询；Chain of Tables和TableReasoner采用查询驱动的模式选择或迭代推理，虽提升了效率，但同样将结构调整绑定在查询时推理阶段。

本文提出的QuIeTT框架与上述工作均存在显著区别。它**将表格转换视为一个查询无关的预处理步骤**，旨在生成一个单一、规范且无损的表示形式，该表示可在不同查询、任务和模型间重复使用。这种方法**彻底将表格表示质量与下游推理解耦**，避免了现有方法中因查询依赖或紧密耦合而导致的泛化能力受限问题，从而实现了更干净、可靠且高效的查询。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为QuIeTT的查询无关表格转换框架来解决现实世界中表格结构不规则、数值格式异构及隐含关系等问题对下游推理可靠性的影响。其核心方法是“先转换，后查询”，将表格预处理与后续推理解耦，从而提升泛化能力和效率。

整体框架分为三个阶段。第一阶段是问题探测与规划：系统首先生成一组针对输入原始表格的合成探测查询，这些查询旨在暴露表格中潜在的结构缺陷，并生成结构化的“问题标注”来指导转换规划，探测完成后相关中间产物会被丢弃，确保转换过程独立于下游真实查询。对于层次复杂的表格，会先进行确定性的扁平化处理，将隐含的父子层级显式化为列，为后续步骤提供统一的列式表示。

第二阶段是查询无关的转换执行：系统基于探测到的问题动态生成一个有序的转换计划序列，该计划明确定义了每项操作的输入、输出和依赖关系，并确定了目标模式。随后，框架通过代码生成与执行来落实该计划，即为每项操作生成确定性的、可执行的Python代码块，并严格按计划执行。此过程确保转换是确定性和可重现的，同时通过保留原始快照列来实现信息无损，最终输出一个规范化的、SQL就绪的规范表格。

第三阶段是下游问答：对于任何后续查询，推理模型（如思维链或SQL生成器）直接基于规范表格进行推理和答案生成，无需修改模型本身。

关键技术及创新点包括：1）严格的查询无关性，转换仅依赖于表格自身结构和固定的转换词汇表，与下游查询分布完全分离；2）通过合成探测查询诱导出表格内在的表示缺陷闭包，实现通用查询支持的自动化规划；3）采用“规划-代码”分离的执行模式，确保转换的确定性、可审计性和可重现性；4）通过保留原始快照实现信息无损，保证所有原始信息均可从规范表格中恢复。这种方法使得任意表格仅需转换一次，生成的规范表示即可被多种下游查询、任务和模型重复使用，从而在多个基准测试中取得了稳定且显著的性能提升。

### Q4: 论文做了哪些实验？

论文在四个基准数据集（WikiTQ、NQ-Table、SequentialQA、HiTab）上进行了全面的实验评估，涵盖了多样的表格结构和推理需求。实验设置固定下游QA模型和提示策略，以隔离表格转换效果。评估指标统一使用F1分数，并应用了轻量级、无损的答案格式化。

对比方法包括两大类：直接提示方法（如CoT、CoT+SQL、NormTab、E5、EEDP、Binder、TableSQLify）和智能体方法（如Chain of Tables、POT）。实验在五个大语言模型（Gemini 2.0/2.5、DeepSeek V3.1、Qwen 3、GPT-OSS）上运行。

主要结果显示，QuIeTT在所有数据集和模型上均取得最佳或接近最佳性能。关键数据指标包括：在WikiTQ上，QuIeTT在Gemini 2.5上达到79.80 F1；在NQ-Table上，在Gemini 2.5上达到80.10 F1；在SequentialQA上，在Gemini 2.5上达到72.32 F1；在HiTab上，在Gemini 2.5上达到84.41 F1。相较于各模型最强的基线方法，QuIeTT带来了约4-8个F1点的提升。

此外，在针对结构多样性挑战问题的子集上，QuIeTT优势更明显，在WikiTQ和NQ-Table挑战集上分别达到74.41和77.16 F1（Gemini 2.5），比最强基线提升约5-8个F1点。表格级分析表明，QuIeTT为60%的网页表格和57%的层次表格带来了性能提升。实验还表明，改进的表格转换降低了对模型规模的依赖，即使使用较小的QA模型（如LLaMA、Mistral）也能获得多数问题的正确答案。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性，未来研究可以从以下几个方向深入探索。首先，针对大规模表格的处理，可以研究分层或分块的转换策略，结合高效的压缩或摘要技术，以突破现有语言模型的输入长度限制，同时保持信息的完整性。其次，需要扩展框架以支持多模态表格，开发能够联合处理文本、图像和结构化数据的统一表示方法，这要求模型具备跨模态理解和推理能力。此外，可以探索轻量化的转换模型，通过知识蒸馏或专门针对表格结构设计的架构，降低对大型语言模型的依赖，提升在资源受限环境中的适用性。最后，将单表处理扩展到多表或跨文档场景，研究表格检索、关联和聚合机制，以实现更复杂的问答任务，这可能需要结合图神经网络或检索增强生成技术来建模表格间的隐含关系。这些改进有望进一步提升表格推理的鲁棒性和泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了QUIeTT框架，旨在解决现实世界中表格数据因模式不规则、值格式异构和隐含关系结构而导致下游推理和问答可靠性下降的问题。现有方法大多以查询依赖的方式处理这些问题，将表格清理与推理过程耦合，限制了泛化能力。QUIeTT的核心贡献在于提出一种查询无关的表格转换框架，在未见测试查询前，将原始表格预处理为单一、无损且支持SQL查询的规范表示。该方法通过解耦表格转换与下游推理，实现了模式与值的无损规范化、隐含关系显式化，并利用原始表格快照保留完整溯源信息，从而无需修改下游模型即可提升查询效率和可靠性。实验在WikiTQ、HiTab等多个基准上验证了该框架能一致提升不同模型和推理范式的性能，尤其在结构多样、未见问题上的改进显著，表明性能增益源于表格表示的优化而非推理策略改变。这确立了查询无关表格转换作为鲁棒表格问答基础组件的意义，并为扩展到大规模表格、多模态格式及多表推理的未来工作提供了方向。
