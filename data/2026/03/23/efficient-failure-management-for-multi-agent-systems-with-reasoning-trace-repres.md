---
title: "Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation"
authors:
  - "Lingzhe Zhang"
  - "Tong Jia"
  - "Mingyu Wang"
  - "Weijie Hong"
  - "Chiming Duan"
  - "Minghua He"
  - "Rongqian Wang"
  - "Xi Peng"
  - "Meiling Wang"
  - "Gong Zhang"
  - "Renhai Chen"
  - "Ying Li"
date: "2026-03-23"
arxiv_id: "2603.21522"
arxiv_url: "https://arxiv.org/abs/2603.21522"
pdf_url: "https://arxiv.org/pdf/2603.21522v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "故障管理"
  - "推理轨迹表示"
  - "对比学习"
  - "可靠性"
  - "软件工程"
relevance_score: 8.0
---

# Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

## 原始摘要

Large Language Models (LLM)-based Multi-Agent Systems (MASs) have emerged as a new paradigm in software system design, increasingly demonstrating strong reasoning and collaboration capabilities. As these systems become more complex and autonomous, effective failure management is essential to ensure reliability and availability. However, existing approaches often rely on per-trace reasoning, which leads to low efficiency, and neglect historical failure patterns, limiting diagnostic accuracy. In this paper, we conduct a preliminary empirical study to demonstrate the necessity, potential, and challenges of leveraging historical failure patterns to enhance failure management in MASs. Building on this insight, we propose \textbf{EAGER}, an efficient failure management framework for multi-agent systems based on reasoning trace representation. EAGER employs unsupervised reasoning-scoped contrastive learning to encode both intra-agent reasoning and inter-agent coordination, enabling real-time step-wise failure detection, diagnosis, and reflexive mitigation guided by historical failure knowledge. Preliminary evaluations on three open-source MASs demonstrate the effectiveness of EAGER and highlight promising directions for future research in reliable multi-agent system operations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体系统（MAS）中，因系统复杂性和自主性增强而出现的故障管理效率与准确性问题。研究背景是LLM驱动的MAS已成为软件系统设计的新范式，在多个领域展现出强大的推理与协作能力，但其动态行为和复杂的推理过程也导致了不可预测的故障，传统监控或调试方法难以有效应对。

现有方法主要存在两大不足。首先，当前方法（如MAST、TRAIL、RAFFLES等）通常依赖“逐迹推理”，即对每个推理轨迹进行独立的语义分析，并常使用大型评判LLM进行异常检测和故障诊断。这种方法虽然有效，但处理每个轨迹都需消耗大量计算，导致在需要高吞吐量的实际MAS中运行效率低下。其次，这些方法大多忽视了历史故障模式的利用，主要依赖LLM针对新故障进行类人推理。然而，LLM的输出本身具有不稳定性，使得相同故障的诊断结果可能前后不一致，这限制了故障诊断的准确性。尽管有方法引入额外评估层来评判推理质量，但并未从根本上解决历史知识复用的问题。

因此，本文要解决的核心问题是：如何设计一种高效的故障管理框架，能够克服现有方法效率低和忽视历史模式的缺陷，实现对MAS故障的实时检测、准确诊断和快速缓解。具体而言，论文聚焦于为特定、任务类型相对固定的实用MAS，构建一个基于推理轨迹表示的框架（EAGER）。该框架需要解决两个关键子问题：如何为富含智能体内推理动态和智能体间协调逻辑的推理轨迹学习有效的表示模型，以及如何在缺乏充足标注且可泛化的故障数据的情况下，利用未标注或弱结构化的历史轨迹来提升诊断精度。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的多智能体系统故障管理展开，可分为以下几类：

**1. 多智能体系统故障管理方法**：现有方法通常采用“逐迹推理”，即对每个推理轨迹进行独立分析以检测和诊断故障。这类方法效率较低，且往往忽略历史故障模式，导致诊断准确性受限。本文提出的EAGER框架与这些方法的核心区别在于，它主动利用历史故障知识，通过推理轨迹表示学习来提升管理效率与精度。

**2. 智能体推理轨迹表示学习**：当前先进的文本嵌入模型（如论文中评估的Qwen3和BGE-M3）在通用NLP任务上表现良好，但初步实验表明，它们在捕捉多智能体系统中复杂的层次化推理和协作语义方面效果不佳（检索Recall@10仅约22%）。本文与之的区别在于，专门设计了针对推理范围的对比学习，以编码智能体内推理和智能体间协调的语义。

**3. 基于经验学习的系统可靠性研究**：在传统软件工程和部分AI系统中，利用历史日志或错误模式进行故障预测和缓解已有探索。本文将这类思想引入多智能体系统领域，并聚焦于其独特的推理轨迹，通过实证研究首次明确了故障模式在特定推理或协调范围内高度集中的现象，从而论证了利用历史知识的潜力和必要性。

总体而言，本文工作与现有研究的关系是：它识别了当前故障管理方法效率低、历史知识利用不足的局限，以及通用嵌入模型对多智能体轨迹表示的不适应性，进而提出了一个集成了新型轨迹表示和实时故障管理的综合框架EAGER作为解决方案。

### Q3: 论文如何解决这个问题？

论文提出的EAGER框架通过一种基于推理轨迹表示的高效方法来解决多智能体系统中的故障管理问题。其核心是设计了一个能够实时进行逐步故障检测、诊断和自反缓解的架构，并利用历史故障知识来指导整个过程。

整体框架包含几个主要模块。首先，一个专用的表示模型通过“推理范围对比学习”进行训练，该模型负责将多智能体交互过程中产生的推理轨迹（包含智能体内推理和智能体间协调模式）编码到一个统一的潜在语义空间中。训练过程无需故障标签数据，而是通过问题变体构建样本，并联合训练两个层次编码器：捕获智能体内推理语义的“推理编码器”和整合多个推理嵌入以编码智能体间编排依赖关系的“轨迹编码器”。其总体损失函数融合了智能体内对比损失、智能体间对比损失和前缀到全轨迹的排序损失，以确保表示的鲁棒性和泛化能力。

在系统运行时，EAGER执行“逐步检测”。每当一个智能体完成其推理，其生成的推理嵌入会与历史积累的“细粒度知识”（即针对单个智能体具体推理错误的识别）进行匹配。在所有智能体推理完成后，整个推理轨迹的嵌入会与“粗粒度知识”（即整个轨迹级别的故障识别）进行比较。一旦检测到相似性（即匹配到已知故障模式），便触发故障警报。

紧接着，“自反缓解”机制被激活。该机制根据检测到的故障粒度采取不同策略：若逐步检测精确识别出某个特定智能体的故障，则执行以模型为中心的自反思，优化该智能体的推理过程；若整个推理轨迹被判定为有误，则触发以编排为中心的自反思，重新评估智能体间的协调，从全局层面恢复一致的推理动态。此外，框架还包含一个可选的“专家检查+智能体根因分析”流程，用于在用户判定系统输出错误时，利用先进的AgentOps方法分析轨迹，并经专家判断来验证和提炼发现，从而持续丰富细粒度和粗粒度的故障知识库，实现系统的持续改进。

EAGER的创新点在于：1) 提出了无监督的推理范围对比学习方法来统一表示智能体内和智能体间的语义，避免了依赖标注数据；2) 设计了结合细粒度和粗粒度历史故障知识的逐步实时检测机制，提升了效率和诊断准确性；3) 引入了分层级的自反缓解策略，能够针对不同故障范围进行精准恢复。

### Q4: 论文做了哪些实验？

论文在三个开源多智能体系统（AutoGen-Code、RCLAgent、SWE-Agent）上进行了初步评估，以验证所提框架EAGER的有效性。实验设置主要包括异常检测、故障诊断和任务性能提升三个方面。在数据集/基准测试上，直接使用了上述三个系统的运行环境与任务。对比方法方面，论文主要将EAGER集成到基线系统（如RCLAgent）中，与原始系统性能进行对比。

主要结果如下：首先，在异常检测与故障诊断任务中，EAGER取得了较高的F1分数。具体关键数据指标为：在AutoGen-Code上异常检测F1为73.57%，故障诊断为63.23%；在RCLAgent上分别为86.18%和78.76%；在SWE-Agent上分别为79.95%和69.51%。平均检测延迟较低，在4.57秒至5.23秒之间，体现了实时性。其次，在任务性能提升实验中，将EAGER与RCLAgent集成后，各项召回率指标（R@1, R@3, R@5, R@10）和平均倒数排名（MRR）均获得一致提升。例如，R@1从28.47%提升至30.19%，MRR从46.13%提升至48.65%。这些结果表明EAGER能够有效进行实时故障管理并提升系统可靠性。

### Q5: 有什么可以进一步探索的点？

该论文的初步探索为基于历史故障模式的多智能体系统（MAS）失效管理提供了有效框架，但仍存在若干局限和可拓展方向。首先，EAGER目前主要依赖无监督对比学习进行推理轨迹表征，未来可探索结合监督或半监督学习，利用更丰富的标注数据提升诊断精度，尤其是在复杂协作场景中。其次，框架的泛化能力有待验证，需在更多样化的MAS架构和任务领域（如动态环境或长期决策）中进行大规模评估，并考虑跨系统迁移学习的可能性。此外，当前方法侧重于实时检测与缓解，未来可引入预测性维护机制，通过分析历史模式提前预警潜在故障。从工程角度看，如何降低计算开销以支持超大规模智能体集群，以及设计更灵活的可插拔治理模块，也是值得深入的方向。最后，结合因果推理等解释性技术，可增强故障根因分析的透明度，进一步提升系统可靠性与可信度。

### Q6: 总结一下论文的主要内容

本文针对基于大语言模型的多智能体系统（MAS）提出了一种高效的故障管理框架EAGER。现有方法通常依赖对每条推理轨迹进行独立分析，效率低下，且忽视历史故障模式，导致诊断准确性受限。为此，论文首先通过实证研究验证了在固定MAS中故障类型有限且可复现，以及通用文本嵌入模型难以有效捕捉智能体推理轨迹的结构与语义关系。

EAGER的核心贡献在于利用推理轨迹表示进行高效故障管理。该方法采用无监督的推理范围对比学习，对智能体内推理和智能体间协作进行统一编码，从而能够实时进行逐步故障检测、诊断和基于历史知识的反射式缓解。框架主要包括：通过表示模型将历史推理轨迹编码到潜在空间；在系统执行中进行步进式检测；一旦检测到故障则触发反射式缓解以快速恢复；并在最终输出错误时通过专家检查与根本原因分析更新故障知识库。

初步实验在三个开源多智能体系统上进行，结果表明EAGER在异常检测和故障诊断方面具有有效性，其即时检测和反射缓解机制还能提升特定任务的响应准确性。这项工作为可靠的多智能体系统运维提供了新思路，强调了利用历史模式提升管理效率与准确性的潜力。
