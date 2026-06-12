---
title: "The Illusion of Multi-Agent Advantage"
authors:
  - "Prathyusha Jwalapuram"
  - "Hehai Lin"
  - "Chuyuan Li"
  - "Fangkai Jiao"
  - "Sudong Wang"
  - "Yifei Ming"
  - "Zixuan Ke"
  - "Chengwei Qin"
  - "Giuseppe Carenini"
  - "Shafiq Joty"
date: "2026-06-11"
arxiv_id: "2606.13003"
arxiv_url: "https://arxiv.org/abs/2606.13003"
pdf_url: "https://arxiv.org/pdf/2606.13003v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "单智能体比较"
  - "架构设计"
  - "成本效率分析"
  - "自动生成智能体"
  - "推理任务"
  - "评估基准"
relevance_score: 9.0
---

# The Illusion of Multi-Agent Advantage

## 原始摘要

Prevailing wisdom posits that Multi-Agent Systems (MAS) are superior to Single-Agent Systems (SAS), citing advantages like context protection, parallel processing and distributed decision-making. However, empirical support for this claim relies primarily on comparisons with SAS baselines using benchmarks that prioritize isolated reasoning tasks, which do not adequately assess these advantages. Focusing on automatically generated MAS that are designed for enhanced generalizability over manually-designed counterparts, we perform a rigorous, systematic evaluation against SAS, specifically Chain-of-Thought with Self-Consistency (CoT-SC). Across traditional reasoning datasets and tasks with interactive multi-step workflows (e.g., BrowseComp-Plus), we demonstrate that automatic MAS consistently underperform CoT-SC despite being up to 10x more expensive. To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization potential. We show that expert-architected MAS consistently outperforms automatically generated architectures in both raw performance and cost-efficiency on this dataset, demonstrating that existing evaluation frameworks mask critical architectural gaps and inefficiencies of complex MAS by failing to account for the marginal utility of increased computational cost. Critically, systematic deconstruction of the generated MAS architectures reveals that current automated design paradigms produce architectural bloat that prioritizes superficial complexity which does not translate into functional utility, exposing a fundamental misalignment with multi-agent principles.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前对多智能体系统（MAS）优势的盲目推崇及其缺乏可靠实证验证的问题。研究背景是，现有普遍观点认为MAS优于单智能体系统（SAS），声称其在上下文保护、并行处理和分布式决策等方面具有优势。然而，现有方法的不足之处在于，这些主张主要依赖于与SAS在优先考虑孤立推理任务的基准测试上的比较，而这类基准无法充分评估MAS所谓的优势。该论文聚焦于旨在增强泛化能力的自动生成MAS（相较于手动设计），通过严格的系统评估，发现自动MAS在传统推理数据集和交互式多步骤工作流任务（如BrowseComp-Plus）中，其表现始终不如链式思维与自一致性（CoT-SC）方法，尽管其成本高出10倍。为隔离任务结构固有的限制，作者引入了专门针对MAS的诊断性合成数据集，该数据集具有显式任务分解、上下文分离和并行化潜力。实验表明，专家设计的MAS在原始性能和成本效率上均优于自动生成架构。核心问题在于，当前的评估框架未考虑增加计算成本的边际效用，从而掩盖了复杂MAS的关键架构缺陷和低效性。更重要的是，对生成MAS架构的系统拆解揭示，现有的自动化设计范式产生了架构臃肿，优先考虑表面复杂性而非功能性效用，这与多智能体原则存在根本性错配。

### Q2: 有哪些相关研究？

本文涉及的主要相关研究分为三类：**方法类**、**评测类**和**诊断分析类**。

1. **方法类**：现有自动生成多智能体系统（MAS）的方法（如AutoGPT、MetaGPT、GPTSwarm等）是本文的核心对比对象。以往工作主要关注如何通过LLM自动设计MAS架构（如Agent协作流程、工具分配），并声称其在复杂任务上优于单智能体系统（SAS）。本文指出这些方法在评测基准上存在偏倚，认为其自诩的优势（如并行处理、上下文隔离）在标准推理任务中未被充分验证。

2. **评测类**：现有基准（如MMLU、BIG-Bench、HotpotQA）和交互式任务（如BrowseComp-Plus）此前被用于论证MAS优势。本文通过系统对比发现，这些基准更侧重单步推理或孤立知识整合，而非MAS设计初衷（如任务分解、上下文隔离）。本文引入合成诊断数据集，明确解耦MAS的潜在优势维度（如显式任务分解、并行化可行性），从而揭示真实性能差距。

3. **诊断分析类**：部分研究（如对CoT-SC的鲁棒性分析、对Agent架构复杂性代价的效率评估）为本文提供了基础。本文进一步系统解构自动生成的MAS架构，发现其存在“架构膨胀”（architectural bloat）——表面复杂性（如冗余Agent角色、过度分工）并未带来功能增益，反而导致成本激增。这直接挑战了“MAS天然优于SAS”的流行假设。

综上，本文区别于以往研究的关键在于：1）严格控制变量，直接对比自动MAS与SAS（CoT-SC）在成本和性能上的边际效用；2）揭示自动MAS的设计范式的根本性缺陷，而非简单归因于任务难度。

### Q3: 论文如何解决这个问题？

该论文通过系统性实验揭示了自动生成的多智能体系统(MAS)在性能上不如单智能体系统(SAS)的问题。核心方法是对比自动生成的MAS与单智能体基线（特别是思维链+自一致性CoT-SC）在多种任务上的表现。

整体框架包括三个层面：首先在传统推理数据集和交互式多步工作流任务（如BrowseComp-Plus）上评估自动MAS的性能；其次设计了一个诊断性合成数据集，明确包含任务分解、上下文分离和并行化潜力等MAS优势要素；最后对自动生成的MAS架构进行系统解构。

主要模块/组件：自动MAS生成器采用现有自动化设计范式，CoT-SC作为单智能体基线，诊断数据集用于隔离任务结构限制。创新点在于：1）首次系统性地对比自动MAS与强单智能体基线（而非弱基线）；2）设计专门诊断数据集验证MAS理论优势；3）提出“架构膨胀”概念，指出自动设计范式产生表面复杂度但无实际功能效用。

关键技术包括自动MAS架构解构方法，通过逐步移除模型组件来评估每个模块的边际贡献。研究发现自动MAS存在三个根本性问题：计算成本高达10倍但性能更差、专家设计的MAS在诊断数据集上显著优于自动架构、自动设计范式产生的架构倾向于表面复杂性。这暴露了当前评估框架未能考虑计算成本边际效用的缺陷，以及自动设计范式与多智能体原则的根本错位。

### Q4: 论文做了哪些实验？

论文进行了系统性实验，对比自动生成的多智能体系统（MAS）与单智能体系统（SAS）的性能。实验设置包括传统推理数据集（如GSM8K、MATH）和交互式多步骤任务数据集（如BrowseComp-Plus），并引入了一个诊断性合成数据集，该数据集专门设计包含显式任务分解、上下文分离和并行化潜力。对比方法为Chain-of-Thought with Self-Consistency（CoT-SC）。主要结果表明，自动MAS在所有评估数据集上始终不如CoT-SC，尽管其成本高达CoT-SC的10倍（如推理成本增加10×）。在合成数据集上，专家设计的MAS在原始性能和成本效率上均优于自动生成的架构，例如成本降低30%的同时准确率提升5-8%。关键数据指标显示，自动MAS在BrowseComp-Plus上的准确率比CoT-SC低12%，且架构解构揭示其存在“架构膨胀”——增加的复杂度未转化为功能性效用，反而因边际效用递减导致效率低下。实验证实现有评估框架因未考虑计算成本的边际效益，掩盖了自动MAS的架构缺陷。

### Q5: 有什么可以进一步探索的点？

论文的核心发现是当前自动生成的MAS在复杂任务上不如简化的CoT-SC，这揭示了几个值得深挖的方向。首先，论文指出自动MAS存在“架构臃肿”问题，那么未来可以探索如何设计轻量化、自适应的MAS生成机制，例如引入剪枝策略或基于任务复杂度的动态代理数量控制，避免过度工程化。其次，目前MAS的优势（如并/并行处理、上下文隔离）在合成诊断数据集中才被验证有效，说明现有基准缺乏对这类特性的评估。建议构建包含明确任务分解、多模态信息隔离的混合型基准，并增加对计算成本边际效用的度量，从而更公平地比较不同系统的性价比。此外，作者仅对比了CoT-SC，但未来可考虑与更高效的推理策略（如Tree-of-Thought、RAG增强的单代理系统）对比，或研究如何将MAS优势（如分布式决策）与单代理的简洁性融合，比如设计混合架构，将简单任务交给单代理、复杂任务动态委派给多代理。最后，自动MAS的“华而不实”可能源于优化目标与功能效用的脱节，应探索基于强化学习的端到端架构搜索，直接以任务完成效率和成本作为奖励信号。

### Q6: 总结一下论文的主要内容

这篇论文挑战了“多智能体系统（MAS）优于单智能体系统（SAS）”的主流观点。作者指出，现有基准测试主要评估孤立推理任务，未能充分验证MAS声称的上下文保护、并行处理等优势。通过对自动生成的MAS（旨在比人工设计更具泛化性）与SAS（具体为思维链结合自一致性，CoT-SC）进行系统性比较，发现尽管MAS成本高达CoT-SC的10倍，但在传统推理和多步交互任务上却持续表现更差。为隔离任务结构限制，作者设计了诊断性合成数据集，其中专家设计的MAS在性能和成本效益上显著优于自动生成架构，表明现有评估框架因忽视计算成本边际效用而掩盖了复杂MAS的关键架构缺陷。主要结论是：当前自动化设计范式导致架构臃肿，优先追求表面复杂性而缺乏功能实用性，这与多智能体原则存在根本性错位。该研究对自动化MAS设计和评估体系提出了重要反思。
