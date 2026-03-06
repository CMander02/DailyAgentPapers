---
title: "Interleaved Tool-Call Reasoning for Protein Function Understanding"
authors:
  - "Chuanliu Fan"
  - "Zicheng Ma"
  - "Huanran Meng"
  - "Aijia Zhang"
  - "Wenjie Du"
  - "Jun Zhang"
  - "Yi Qin Gao"
  - "Ziqiang Cao"
  - "Guohong Fu"
date: "2026-01-07"
arxiv_id: "2601.03604"
arxiv_url: "https://arxiv.org/abs/2601.03604"
pdf_url: "https://arxiv.org/pdf/2601.03604v2"
categories:
  - "cs.AI"
tags:
  - "Tool-Augmented Agent"
  - "Scientific Agent"
  - "Tool Use"
  - "Reasoning"
  - "Knowledge-Intensive Task"
  - "Problem Decomposition"
relevance_score: 7.5
---

# Interleaved Tool-Call Reasoning for Protein Function Understanding

## 原始摘要

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用大语言模型（LLM）进行蛋白质功能理解这一科学任务时，现有纯文本推理方法的局限性问题。

研究背景是，蛋白质功能理解是计算生物学的基础任务，对药物发现等领域至关重要。传统监督微调方法性能虽好，但缺乏可解释性且难以泛化。近期，以DeepSeek R1为代表的模型通过思维链（CoT）推理和强化学习，在数学、编程等符号领域取得了显著成功，这启发研究者尝试将此类文本推理范式迁移到蛋白质领域。

然而，现有方法（即直接迁移基于文本的CoT和强化学习范式）存在明显不足。论文通过早期实验发现，这种迁移是无效的：强化学习主要放大了模型对表面关键词模式的依赖，而未能引入新的生物学知识，导致模型性能提升有限且很快达到瓶颈。其根本原因在于，蛋白质功能预测是一个知识密集型的科学任务，本质上依赖于外部的生物学先验知识和计算工具，而非纯粹的、封闭的符号推理。LLM的内部推理无法弥补其缺失的领域专业知识。

因此，本文要解决的核心问题是：如何设计一个与蛋白质功能理解任务内在需求相匹配的推理框架，以克服纯内部文本推理的局限，实现可靠且可泛化的预测。为此，论文提出了PFUA，一个工具增强的蛋白质推理智能体。其核心思想是摒弃不受约束的长链符号推理，转而将问题分解、工具调用和基于证据的答案生成统一起来，通过整合领域特定工具来产生可验证的中间证据，从而将推理过程扎根于外部知识。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：蛋白质语言模型、思维链推理方法以及工具增强型语言模型。

在蛋白质语言模型方面，近期研究将蛋白质理解任务转化为文本生成问题，通过查询压缩、交叉注意力或投影等方法将蛋白质序列或结构表示与预训练大语言模型对齐。这些方法虽在实证中表现良好，但本质上是依赖统计相关性的黑盒预测器，缺乏明确的生化推理机制。本文提出的PFUA则强调引入外部生物先验和计算工具进行可验证的中间推理，与之形成鲜明对比。

在推理方法上，思维链提示通过生成中间自然语言解释实现多步推理，并在数学等领域通过测试时扩展和强化学习取得进展。然而，在蛋白质理解等科学任务中，此类方法往往停留于纯文本推理，生成的原理可能仅反映表层语言模式而非基于知识的机制推断。本文指出直接迁移此类范式效果有限，因此转向工具增强的推理框架。

在工具增强型语言模型方面，检索增强生成通过将输出锚定于外部语料库来减少幻觉并支持知识密集型问答。ReAct进一步交织推理与工具执行，使模型能将工具输出纳入推理过程；ReTool则利用强化学习策略性地决定工具调用时机与方式。本文的PFUA继承了这类工作“推理-行动”交织的核心思想，但专门针对蛋白质功能理解这一知识密集型科学任务进行设计，统一了问题分解、工具调用与基于证据的答案生成，强调通过领域专用工具产生可验证的中间证据，而非依赖冗长无约束的推理轨迹。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PFUA的工具增强型蛋白质推理智能体来解决蛋白质功能理解问题。其核心方法是设计一个**交错式工具调用推理流水线**，将领域专用工具无缝集成到模型的推理循环中，以生成可验证的中间证据，而非依赖长而无约束的文本推理链。

**整体框架与主要模块**：
PFUA的架构是一个**统一执行器**驱动的工具调用循环。智能体在推理过程中，根据当前需求，自主选择并调用外部计算工具，利用工具返回的结构化证据来约束假设空间、指导后续推理，并最终生成基于证据的答案。整个流程实现了问题分解、工具调用和答案生成的高度统一。

**关键技术组件（工具池）**：
1.  **序列基本属性分析工具**：作为快速、机制无关的初步检查。它直接从氨基酸序列计算轻量级描述符，如序列长度、最大疏水片段长度（作为跨膜倾向性的代理）和低复杂度指数。这为早期分类提供了基线假设，例如，识别出可能为膜蛋白或具有无序区域的蛋白质，防止下游分析做出错误假设。
2.  **基于MMseqs2的同源性搜索工具**：用于将预测建立在经过人工审核的生物知识上。该工具针对高质量参考数据库（如Swiss-Prot）进行快速序列相似性搜索，并提取最佳匹配条目的结构化证据（如蛋白质名称、功能描述、催化反应、EC编号、GO术语等）。这为智能体提供了从同源性到功能推断的可审计桥梁，极大地约束了假设空间。
3.  **Pfam结构域分析工具**：作为一种机制层面的分析。它通过扫描Pfam-A隐马尔可夫模型库来识别具有统计显著性的结构域。这能在蛋白质水平注释之前，在结构域和折叠层面约束功能假设空间，使智能体能基于保守的结构域家族（如转移酶折叠）推理可能的生化机制，避免过早承诺过于具体的功能。
4.  **TMbed跨膜拓扑预测工具**：作为一个结构感知的定位判别器。它利用基于大规模蛋白质语言模型的嵌入来预测跨膜螺旋和膜相关区域，具有高灵敏度。其预测的拓扑信息对于细胞组分（CC）GO术语的标注至关重要，能从根本上约束可能的功能假设。

**创新点**：
1.  **范式转变**：从依赖纯文本链式推理，转向以**领域工具为驱动、证据为中心**的推理范式。这承认了蛋白质功能预测是一个知识密集型的科学任务，必须依赖外部生物先验和计算工具。
2.  **交错式集成**：工具调用不是独立或顺序执行的，而是**深度交织在推理循环中**。智能体动态地根据上一步的证据决定下一步调用哪个工具，形成“假设-证据-精炼”的迭代过程。
3.  **证据约束与可验证性**：每个工具都产生结构化、可验证的中间证据（如JSON格式），使推理过程透明、可审计，并有效防止了基于表面关键词模式的过度自信或错误泛化。
4.  **工具选择策略**：精心策划的工具池优先考虑可编程访问、快速响应和高证据价值的工具，覆盖了从序列属性、同源知识、结构域机制到结构拓扑的不同抽象层次，为智能体提供了全面的调查能力。

### Q4: 论文做了哪些实验？

论文在四个蛋白质问答基准上进行了实验：Mol-Instructions（涵盖蛋白质/分子指令跟随任务）、UniProtQA（基于UniProt注释的功能、过程和定位问题）、PDB-QA（基于PDB条目的结构域/拓扑推理查询）以及CAFA（CAFA设置下的基因本体功能推断）。实验设置方面，作者将提出的PFUA（一种工具增强的蛋白质推理智能体）与五类基线方法进行了对比：1）监督微调方法（如BioMedGPT、ProtT3、Prot2Text、Qwen2.5-3B-SFT）；2）基于文本的推理方法（如BioMedGPT-R1、Qwen2.5-3B-R1）；3）在线大语言模型（如DeepSeek-Reasoner、Kimi-K2-Thinking、Qwen3-Max-Preview）；4）多源检索增强生成方法；5）工具驱动的蛋白质智能体（使用相同在线大语言模型作为骨干，但采用交错工具调用推理）。所有模型在解码时温度均设置为0.0以确保确定性。

主要结果基于Mol-Instructions数据集上的四个任务进行评估：蛋白质功能预测、催化活性预测、结构域和基序识别以及通用文本描述生成。性能指标采用ROUGE-1和ROUGE-L召回率。关键数据显示，PFUA（基于Qwen3-Max-Preview）在平均ROUGE-1和ROUGE-L上分别达到64.33%和46.16%，显著优于所有基线。具体而言，相比纯文本推理的最佳基线Qwen2.5-3B-R1（平均ROUGE-L为39.51%），PFUA实现了平均16.65个百分点的提升（相对提升约42.1%）；相比多源RAG方法，PFUA在结构域识别等任务上提升尤为明显。结果表明，PFUA通过主动交错推理与显式工具调用，在需要整合异质生物信号的任务上实现了更可靠的知识 grounding 和泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，工具集的设计与优化是关键。当前工具池固定，未来可探索动态工具选择或自适应工具组合机制，甚至引入工具学习（Tool Learning）让模型能根据任务需求推荐或生成新工具。其次，领域扩展性需验证。本文聚焦蛋白质QA，但工具增强推理在酶优化、蛋白质设计等更复杂任务上的有效性尚未系统评估，可探索跨任务迁移与领域自适应方法。此外，评估体系有待完善。当前依赖简洁参考答案，未来需设计能对齐复杂推理链的评估指标，如基于证据可信度的分步评分，或引入人类专家对推理过程进行细粒度评估。最后，数据质量方面，可通过主动学习或噪声标注检测技术减少标注误差，提升模型鲁棒性。这些方向将推动蛋白质科学中AI代理从“工具使用者”向“智能协作伙伴”演进。

### Q6: 总结一下论文的主要内容

该论文针对蛋白质功能理解这一知识密集型科学任务，指出传统基于纯文本的思维链推理范式（如强化学习）存在局限，其容易放大表面关键词模式而无法引入新的生物学知识，导致泛化能力不足。为此，作者提出PFUA，一种工具增强的蛋白质推理智能体，其核心贡献在于将问题分解、工具调用和基于证据的答案生成统一起来。PFUA不依赖冗长无约束的推理轨迹，而是整合领域专用工具（如生物计算工具）来产生可验证的中间证据，从而提升预测的可靠性和可解释性。实验表明，PFUA在多个基准测试中显著优于纯文本推理模型，平均性能提升达103%。这项工作强调了工具集成智能体作为科学AI系统的有前景的范式，为生物信息学等需要外部先验和计算验证的领域提供了新的解决方案。
