---
title: "EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis"
authors:
  - "Harihara Muralidharan"
  - "Reema Baskar"
  - "Soo Hee Lee"
  - "Tim Proctor"
  - "Kenny Workman"
date: "2026-06-11"
arxiv_id: "2606.13602"
arxiv_url: "https://arxiv.org/abs/2606.13602"
pdf_url: "https://arxiv.org/pdf/2606.13602v1"
categories:
  - "cs.AI"
tags:
  - "评测基准"
  - "科学Agent"
  - "生物信息学Agent"
  - "LLM Agent评估"
  - "可验证基准"
  - "短时域任务"
relevance_score: 9.0
---

# EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis

## 原始摘要

We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and return deterministically gradable answers. The benchmark includes 106 evaluations across CUT\&Tag/CUT\&RUN, ATAC-seq, ChIP-seq, and DNA methylation workflows. Across 5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts: GPT-5.5 / Pi led at 45.0\% (143/318 attempts; 95\% confidence interval (CI), 36.3--53.7), followed by GPT-5.5 / OpenAI Codex at 39.9\% (127/318 attempts; 95\% CI, 31.6--48.3). Claude Opus 4.8 Max / Pi and GPT-5.4 / Pi each passed 39.0\% (124/318 attempts; 95\% CI, 30.2--47.8 and 31.0--47.0, respectively). Performance varies across assay types, and many failed runs still contain parts of the correct answer. Agents often found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在表观基因组学数据分析中缺乏可靠评估基准的问题。研究背景是，表观基因组学分析（如CUT&Tag、ATAC-seq、ChIP-seq和DNA甲基化测序）涉及从读段比对、峰值检测到基序解读、基因组注释等一系列复杂决策，很小的流程选择就可能导致不同的生物学结论。现有方法的不足在于：目前已有的生物学基准测试虽然开始评估AI在实践分析中的能力，但覆盖范围较广或聚焦于其他数据类型，没有一个专门针对表观基因组学分析任务设计。因此，现有AI智能体在执行这类任务时容易产生幻觉，且在不同组织、疾病和研究设计中的生物学判断可靠性差。本文核心解决的问题是：构建一个可验证的表观基因组学短时程分析基准EpiBench，包含106个评估项和16个模型-工具组合的5088条有效轨迹，要求智能体从真实的工作流状态出发，做出明确的分析决策并返回可确定性评分的结构化答案。结果表明，最佳系统（GPT-5.5/Pi）也仅通过45%的尝试，所有模型均未能通过多数测试，证明了当前AI在需要深度、特异性科学判断的表观基因组学任务中存在系统性不足。

### Q2: 有哪些相关研究？

本文的主要相关研究可分为评测类和方法类。

**评测类相关工作**：现有生物信息学基准测试主要关注其他数据模态或更广泛的生物学问题（如基因表达、蛋白质结构预测、药物发现等），但据本文所知，它们都不专门针对表观基因组学分析。EpiBench 填补了这一空白，聚焦于 CUT&Tag/CUT&RUN、ATAC-seq、ChIP-seq 和 DNA 甲基化等表观基因组学流程中的短周期、可验证的判断任务，提供了首个专门评测 AI 智能体在该领域的基准。

**方法类相关工作**：AI 智能体在人类引导的生物数据分析中展现出初步潜力，能够检查文件、编写代码、调用命令行工具并行使一定的科学判断。然而，现有方法普遍存在幻觉和判断不可靠的问题，尤其是在跨组织、疾病和研究设计的复杂场景下。EpiBench 通过设计可确定性评分的任务（要求智能体返回结构化答案），揭示了当前最先进系统（如 GPT-5.5 配合不同工具链）在需要深入生物学推理（如选择合适样本、准确归一化、识别基因组特征等）时的性能瓶颈，与现有工作形成对比。

### Q3: 论文如何解决这个问题？

EpiBench通过构建一个可验证的基准测试框架，将短周期的表观基因组学分析任务转化为确定可评分的决策问题，从而解决AI代理在科学分析中缺乏可靠评估的问题。整体框架基于四类实际工作流程（CUT&Tag/CUT&RUN、ATAC-seq、ChIP-seq、DNA甲基化），将分析分解为106个短时、可评分的子任务，覆盖质量控制、峰值调用、染色质状态比较、基因组注释、甲基化统计、比对检查及下游分析八大类别。

核心技术模块包括：1）确定性评分器，通过数值区间检查、结构化标签匹配或全字段比较自动验证代理输出；2）快照式任务设计，每个问题包含真实分析流程中关键步骤前的数据快照、解释性元数据、高层级任务描述和对应评分器；3）三原则约束：任务可验证、科学结论持久（不同合理分析路径应得到相同结论）、抗捷径（防止通过先验知识或简单启发式绕过数据交互）。

创新点体现在：任务指定"要恢复什么结果"而非"如何恢复"，强制代理理解特定实验背景；通过手动质量控制排除过度指定方法或可作弊的任务；最终基于5,088条有效轨迹发现，即使最佳系统GPT-5.5/Pi也仅通过45%尝试，且频繁在需要深度分析科学判断时失败，证明该基准能有效识别代理在基础操作与科学推理间的能力差距。

### Q4: 论文做了哪些实验？

论文在EpiBench基准上进行了实验，包含106个评估任务，覆盖CUT&Tag/CUT&RUN、ATAC-seq、ChIP-seq和DNA甲基化四种工作流。实验设置了16个模型-工具对（包括GPT-5.5、Claude Opus等模型与Pi、OpenAI Codex等工具），每个模型-工具对在每个任务上运行3次，共产生5088条有效轨迹。主要结果：所有系统均未达到50%的通过率。表现最佳的GPT-5.5 / Pi通过率为45.0%（143/318次，95%CI: 36.3-53.7），其次为GPT-5.5 / OpenAI Codex（39.9%）、Claude Opus 4.8 Max / Pi和GPT-5.4 / Pi（均为39.0%）。按实验类型分，CUT&Tag/CUT&RUN通过率最高（34.0%），甲基化测序为33.3%，ChIP-seq为30.6%，ATAC-seq最低（22.8%）。进一步分析显示，68.2%的答案字段评分通过，但仅31.0%的端点通过率，表明许多失败案例包含部分正确结果，但在需要深度科学判断的关键选择（如比对参数、统计量选择、数据层处理）上出错，导致最终答案错误。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三方面：任务分布不均衡（CUT&Tag/CUT&RUN和甲基化测序占主导，下游分析及质控任务过多），相关评估间存在重复失败模式（导致聚合分数部分反映同一决策的反复测试），以及确定性评分器无法覆盖所有科学合理的分析路径。未来研究方向可从以下角度展开：1）构建更为平衡的任务集合，纳入更多ATAC-seq和ChIP-seq评估，并增加上游数据处理和流程规划类任务；2）设计层次化评价体系，区分“工具操作能力”与“科学判断能力”，针对后者设计细粒度诊断指标（如错误原因分类）；3）探索可解释性增强方法，在agent决策过程中显式要求其引用具体实验伪影（如峰图背景噪声、甲基化CpG偏好性），并训练模型基于证据而非默认参数进行推理；4）引入多路径评价机制，允许agent返回带置信度的多个备选答案，由领域专家或验证模型评估合理性。当前agent之所以能执行流程却给出错误生物学结论，根本原因在于缺乏将实验结果与特定技术性伪影关联的深度推理能力，未来应重点突破这种“执行-判断”割裂问题。

### Q6: 总结一下论文的主要内容

EpiBench是一个用于评估AI智能体在表观基因组学分析中可验证表现的基准测试。问题定义在于当前AI智能体在生物数据分析中容易产生幻觉和不可靠的判断，而现有基准缺乏针对表观基因组学分析的专门评估。方法上，EpiBench包含了106个评估任务，涵盖CUT&Tag/CUT&RUN、ATAC-seq、ChIP-seq和DNA甲基化工作流程，通过快照真实工作流状态并设置确定性评分答案来测试智能体的分析决策能力。主要结论显示，在16个模型-工具组合的5,088条有效轨迹中，没有任何系统能通过半数以上尝试，表现最好的GPT-5.5/Pi仅达到45.0%的通过率。失败案例表明智能体往往能找到正确文件并计算有用中间结果，但在需要深层、实验类型特定的科学判断时失败。核心贡献在于提供了一个可验证的基准来分离工具执行与科学判断能力，为改进AI智能体在生物学推理中的可靠性提供了重要参考。
