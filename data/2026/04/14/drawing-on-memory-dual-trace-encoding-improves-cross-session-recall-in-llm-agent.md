---
title: "Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents"
authors:
  - "Benjamin Stern"
  - "Peter Nadel"
date: "2026-04-14"
arxiv_id: "2604.12948"
arxiv_url: "https://arxiv.org/abs/2604.12948"
pdf_url: "https://arxiv.org/pdf/2604.12948v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Memory Encoding"
  - "Long-term Memory"
  - "Cognitive Science"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents

## 原始摘要

LLM agents with persistent memory store information as flat factual records, providing little context for temporal reasoning, change tracking, or cross-session aggregation. Inspired by the drawing effect [3], we introduce dual-trace memory encoding. In this method, each stored fact is paired with a concrete scene trace, a narrative reconstruction of the moment and context in which the information was learned. The agent is forced to commit to specific contextual details during encoding, creating richer, more distinctive memory traces. Using the LongMemEval-S benchmark (4,575 sessions, 100 recall questions), we compare dual-trace encoding against a fact-only control with matched coverage and format over 99 shared questions. Dual-trace achieves 73.7% overall accuracy versus 53.5%, a +20.2 percentage point (pp) gain (95% CI: [+12.1, +29.3], bootstrap p < 0.0001). Gains concentrate in temporal reasoning (+40pp), knowledge-update tracking (+25pp), and multi-session aggregation (+30pp), with no benefit for single-session retrieval, consistent with encoding specificity theory [8]. Token analysis shows dual-trace encoding achieves this gain at no additional cost. We additionally sketch an architectural design for adapting dual-trace encoding to coding agents, with preliminary pilot validation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体（Agent）在持久性记忆（persistent memory）方面的一个核心缺陷：现有系统通常将信息存储为扁平的事实记录（flat factual records），缺乏对信息获取时的上下文（如时间、地点、情境）的编码。这种扁平化存储使得智能体难以进行跨会话（cross-session）的复杂记忆操作，例如时间推理（temporal reasoning）、知识更新追踪（knowledge-update tracking）和多会话信息聚合（multi-session aggregation）。这限制了智能体从长期交互中有效学习和回忆的能力，使其更像一个静态的查找工具，而非一个真正理解用户历史和上下文的有用助手。论文受人类认知心理学中“绘画效应”（drawing effect）的启发，提出了一种新的记忆编码方法，以增强智能体在需要上下文和时序理解的复杂任务中的回忆准确性。

### Q2: 有哪些相关研究？

相关研究主要分为两个领域：LLM智能体记忆架构和人类认知中的精细编码（elaborative encoding）。在智能体记忆方面，MemGPT/Letta框架引入了分层记忆架构（核心、回忆、归档记忆），为本文工作提供了基础。Park等人的生成智能体通过观察流和反思来捕捉时间结构，但未在编码时生成精细的痕迹。基于检索增强生成（RAG）的框架专注于检索架构而非编码策略。商业系统如Mem0专注于事实提取和向量检索。记忆基准方面，LoCoMo测试单次长对话的记忆，而LongMemEval（及其单用户变体LME-S）则测试跨数千独立会话的记忆，后者被本文选为评估基准。在认知科学方面，Fernandes等人提出的“绘画效应”表明，绘制概念比书写能产生更强的记忆，其核心机制是精细生成（elaborative generation），即承诺于具体的细节。Wammes等人进一步验证了该效应的稳健性。Tulving和Thomson的“编码特异性原则”指出，检索线索与编码上下文匹配时最有效。Paivio的“双重编码理论”认为，信息以言语和意象两种格式编码时更易检索。本文的创新在于将认知科学中的精细编码原理（特别是绘画效应的机制）系统性地引入并适配到LLM智能体的记忆系统中，以解决现有技术只存储“什么”而忽略“何时、何地、为何”的局限性。

### Q3: 论文如何解决这个问题？

论文提出了“双痕迹记忆编码”（dual-trace memory encoding）协议。其核心思想是，每当智能体存储一条个人信息时，同时创建两个配对的条目：1) **事实痕迹（Fact Trace）**：一个结构化的、类似现有系统存储的事实记录，包含YAML元数据和具体细节列表。2) **场景痕迹（Scene Trace）**：一个具体的、可意象化的叙事，将相同的事实嵌入到一个特定的时刻、地点和上下文中（例如，以“Picture:”开头描述一个具体的视觉场景）。场景痕迹的生成过程强制智能体在编码时进行“精细生成”，承诺于特定的时空和上下文细节，从而创建更丰富、更具区分度的记忆痕迹。该方法还包含几个关键技术组件：**证据评分门控（Evidence Scoring Gate）**：使用相关性、具体性和明确性三个维度（各0-2分）对每个会话进行评分，以决定是否进行编码及编码深度（如DROP或FULL），避免存储无关噪声。**三状态检索协议（Three-State Retrieval Protocol）**：在检索时，根据找到的记忆痕迹类型调整置信度：状态A（找到事实和场景）先重建场景再高置信度回答；状态B（仅找到事实）基于事实中置信度回答；状态C（未找到）明确弃权。该协议直接体现了编码特异性原则。在实验设计中，论文通过严格控制变量（C6-draw vs C7-control）来隔离场景痕迹的贡献，确保两者在会话覆盖率、事实痕迹格式和证据评分阈值上完全可比，唯一的区别是C6生成场景痕迹而C7不生成。此外，论文还概述了将该方法适配到编码智能体（如Letta Code）的架构设计，将场景词汇从“Picture:”调整为“Moment:”，并扩展了证据评分维度以适应软件工程领域。

### Q4: 论文做了哪些实验？

论文在LongMemEval-S（LME-S）基准上进行了严格的实验评估。LME-S包含4,575个真实用户对话会话和100个结构化回忆问题，涵盖五种记忆能力：单会话事实检索、多会话聚合、知识更新追踪、时间推理和弃权。实验设置了多个条件以追踪系统迭代路径，但核心对比是在两个严格控制的条件之间：C6-draw（双痕迹编码）和C7-control（仅事实编码）。两者使用相同的证据评分门控（0-2分丢弃，3-6分编码）、相同的事实痕迹格式和命名约定，并达到了可比的会话覆盖率（54.8% vs 57.4%）。主要使用Claude Sonnet作为智能体模型，GPT-4o作为答案评判器。统计方法上，使用10,000次重复的bootstrap重采样计算95%置信区间和单侧p值，并使用McNemar检验分析配对问题结果。主要结果如下：整体准确率上，C6-draw达到73.7%，C7-control为53.5%，绝对提升20.2个百分点（95% CI: [+12.1, +29.3], p < 0.0001）。分类结果显示，提升集中在时间推理（+40pp）、知识更新追踪（+25pp）和多会话聚合（+30pp）任务上，而在单会话事实检索任务上两者表现相同（75% vs 75%），这与编码特异性理论的预测一致。在99个共同问题中，有22个问题仅C6答对而C7答错，反向情况仅有2个（McNemar‘s χ² = 15.04, p < 0.001）。此外，令牌分析表明，尽管C6生成了更多的完成令牌，但由于提示令牌占主导，其编码阶段总成本比C7低1.7%，检索阶段低3.3%，实现了性能提升而无需额外成本。论文还报告了从初始条件到最终条件的渐进性能提升，并简要描述了在编码智能体上进行初步试点验证的结果。

### Q5: 有什么可以进一步探索的点？

论文指出了几个未来研究方向。首先，需要进行**编码-检索消融实验**，以分离场景痕迹的贡献究竟来自编码时的场景生成、检索时的场景重建，还是两者共同作用。这有助于更精确地理解其作用机制。其次，需要在**更多基准和真实世界部署**中评估双痕迹编码的泛化能力，以验证其超越LME-S的有效性。第三，需要对**编码智能体的适配方案**进行受控的实验验证，使用领域特定的基准。第四，当前**每类问题的样本量较小**（n=20），未来需要更大的问题集以获得更精确的类别特定效应量估计。第五，可以探索将双痕迹原则**推广到其他领域**，如医疗、法律或教育智能体，这些领域的信息同样具有时间、原理或演进维度。第六，论文提到一个定性观察，即场景痕迹可能支持检索推理过程中的**主动自我纠错**，这一现象值得系统性地研究。最后，在工程层面，需要解决智能体**训练默认行为与外部记忆协议竞争**的问题（如试点中发现的系统指令被覆盖），确保编码协议能可靠生效。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种受人类“绘画效应”启发的“双痕迹记忆编码”方法，用于增强基于LLM的智能体的长期跨会话记忆能力。核心创新在于，在存储结构化事实痕迹的同时，强制智能体生成一个具体的场景痕迹，该叙事将事实锚定在特定的时空上下文中。这种精细编码过程创造了更丰富、更具区分度的记忆痕迹。在LongMemEval-S基准上的严格实验表明，与仅存储事实的基线相比，双痕迹编码带来了20.2个百分点的整体准确率提升，且提升完全集中在需要时间推理、更新追踪和多会话聚合的复杂任务上，而在简单的事实检索任务上无额外收益，这符合认知心理学中的编码特异性理论。令牌分析显示该性能提升无需额外成本。论文还展示了该方法向编码智能体等领域的可扩展性。这项工作强调了记忆编码深度（如何存储）相对于存储广度（存储多少）的重要性，为构建更强大、更类人的持久记忆智能体提供了新的技术路径和理论基础。
