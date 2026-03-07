---
title: "MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval and Multispecialty Consensus"
authors:
  - "Zheng Li"
  - "Jiayi Xu"
  - "Zhikai Hu"
  - "Hechang Chen"
  - "Lele Cong"
date: "2026-03-05"
arxiv_id: "2603.05129"
arxiv_url: "https://arxiv.org/abs/2603.05129"
pdf_url: "https://arxiv.org/pdf/2603.05129v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "Healthcare & Bio"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MedCoRAG (Medical Collaborative RAG)"
  primary_benchmark: "MIMIC-IV"
---

# MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval and Multispecialty Consensus

## 原始摘要

Diagnosing hepatic diseases accurately and interpretably is critical, yet it remains challenging in real-world clinical settings. Existing AI approaches for clinical diagnosis often lack transparency, structured reasoning, and deployability. Recent efforts have leveraged large language models (LLMs), retrieval-augmented generation (RAG), and multi-agent collaboration. However, these approaches typically retrieve evidence from a single source and fail to support iterative, role-specialized deliberation grounded in structured clinical data. To address this, we propose MedCoRAG (i.e., Medical Collaborative RAG), an end-to-end framework that generates diagnostic hypotheses from standardized abnormal findings and constructs a patient-specific evidence package by jointly retrieving and pruning UMLS knowledge graph paths and clinical guidelines. It then performs Multi-Agent Collaborative Reasoning: a Router Agent dynamically dispatches Specialist Agents based on case complexity; these agents iteratively reason over the evidence and trigger targeted re-retrievals when needed, while a Generalist Agent synthesizes all deliberations into a traceable consensus diagnosis that emulates multidisciplinary consultation. Experimental results on hepatic disease cases from MIMIC-IV show that MedCoRAG outperforms existing methods and closed-source models in both diagnostic performance and reasoning interpretability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决临床肝病诊断中人工智能方法在准确性、可解释性和实际部署方面存在的关键问题。研究背景是，在精准医疗时代，从电子健康记录中实现准确且可解释的肝病诊断至关重要，但肝病症状常模糊且重叠，使得早期诊断困难。现有方法存在明显不足：首先，大型语言模型虽然展现了潜力，但其知识可能静态过时，且推理过程缺乏可追溯的逐步论证，难以满足高风险诊断所需的可解释性标准。其次，传统的检索增强生成方法通常依赖单一的非结构化文本证据源，难以支持基于结构化临床数据的多步推理。再者，尽管一些方法引入了医学知识图谱以进行结构化推理，但原始图谱路径常包含不相关链接，且未能有效整合临床实践指南中的情境化指导。最后，新兴的多智能体框架试图模拟多学科会诊，但大多基于静态、固定的专家团队，无论病例复杂度如何都启用相同专家，导致冗余讨论或专业不足，并且缺乏对知识图谱和权威指南的深度整合，其推理过程也往往优先考虑最终任务准确性而非符合临床医生思维的可解释性。

因此，本文要解决的核心问题是：如何构建一个端到端的诊断框架，能够生成准确、可解释且基于证据的肝病诊断，以模拟真实世界的多学科会诊过程。具体而言，论文提出的MedCoRAG框架致力于克服现有方法在证据来源单一、推理缺乏结构化与迭代性、以及智能体调度僵化等方面的局限，通过融合多源证据检索与动态多智能体协同推理，实现透明、可追溯且与临床实践对齐的诊断决策。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：医学检索与知识增强推理，以及用于临床协作的多智能体系统。

在医学检索与知识增强推理方面，相关工作旨在通过检索外部知识来提升大语言模型诊断的准确性和可解释性。例如，MedGraphRAG构建多层知识图谱并生成结构化标签摘要以进行连贯检索；MedRAG通过症状相似性对疾病分组来改善诊断对齐；KG-Rank利用知识图谱实体路径相关性对检索段落重排序以提升答案质量；rationale-guided RAG则首先生成轻量级诊断依据来引导单步检索。然而，这些方法通常依赖单一知识源，且不支持基于结构化临床数据的迭代推理。本文提出的MedCoRAG通过联合检索知识图谱路径和临床指南，并进行领域感知剪枝，构建了聚焦、可追溯的证据包，从而弥补了这一不足。

在多智能体临床协作系统方面，早期工作通过零样本角色扮演或模拟临床环境建立基于角色的协作。近期研究则转向基于证据和优化的工作流，如ColaCare、LINS在结构化电子健康记录上协调智能体，TxAgent专注于治疗计划的动态工具组合，MedAgent-Pro构建可追溯的多模态诊断路径，MMedAgent-RL利用强化学习优化协作策略。但这些系统大多采用固定的协作结构，或将审议过程与统一的证据基础分离，限制了适应性和临床保真度。本文方法通过根据异常发现动态路由专科智能体，并协调它们在共享的、以指南为基础的知识图谱上进行强化学习驱动的迭代审议，从而实现了更灵活、仿真的多学科会诊。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MedCoRAG的端到端框架来解决肝脏疾病诊断中准确性、可解释性和可部署性的挑战。其核心方法结合了混合证据检索与多智能体协同推理，旨在模拟真实世界多学科会诊的流程。

**整体框架与核心组件**：框架包含三个核心阶段。首先，**异常发现与初步诊断**：从患者叙述中提取异常临床发现，并通过统一医学语言系统（UMLS）进行标准化，生成一组初步诊断假设。其次，**混合检索增强生成（Hybrid RAG）**：为每个假设，系统并行检索两个互补的证据源——临床指南摘录和UMLS知识图谱路径。检索到的证据会利用完整的临床上下文进行联合剪枝，形成针对特定患者的、连贯的证据包。最后，**多智能体协同推理**：一个路由智能体（Router Agent）基于病例描述和异常发现评估病例复杂性。对于简单病例，直接由全科智能体（Generalist Agent）根据初始证据生成诊断。对于复杂病例，则动态调度相关的专科智能体（Specialist Agents，如肝病学、肾病学等）参与推理。

**关键技术细节与创新点**：
1.  **混合证据检索与剪枝**：创新性地同时利用结构化知识图谱（提供可解释的推理路径）和非结构化临床指南（提供权威陈述）。通过基于LLM的剪枝步骤，确保证据与具体病例高度相关，解决了单一来源检索的局限性。
2.  **动态、迭代的多智能体推理**：路由智能体实现**动态专科调度**，而非固定设置，使专家配置与临床上下文匹配。各专科智能体基于共享证据包进行迭代推理，并输出立场、置信度和证据充分性判断。当多数智能体认为证据不足时，会触发**智能体引导的再检索**，形成一个“检索-推理”闭环，使证据和诊断假设协同演化。
3.  **可追溯的共识形成**：全科智能体负责综合所有专科智能体的审议意见，生成校准后的置信度分数和中期共识。最终诊断并非简单选择最高分假设，而是通过**整体裁决函数**，综合考虑审议历史、证据演变、分歧与不确定性，输出一个单一、可追溯且临床可行的诊断结论，并附有详细的共识报告。

总之，MedCoRAG通过结构化证据合成、动态多智能体协作以及迭代式证据检索与推理的闭环设计，实现了性能与可解释性的共同提升，有效模拟了基于证据的多学科临床会诊。

### Q4: 论文做了哪些实验？

实验在真实世界肝病诊断任务上评估MedCoRAG。实验设置方面，从MIMIC-IV数据库构建临床数据集，聚焦13种常见肝病，保留患者所有住院记录以构建纵向病史。由于MIMIC-IV主要为结构化数据，研究使用LLM基于时间线合成丰富的临床叙事文本，并格式化为医学问答对。最终数据集包含3470个QA样本，按疾病类别分层，以7:3比例划分为训练集和测试集用于蒸馏阶段。

评估使用四个标准指标：精确率、召回率、F1分数和F0.5分数，均以13个疾病类别的加权平均值报告。对比方法涵盖多类模型：参数≤8B的医学领域模型（如Qwen3-Medical-GRPO-4B）、大型闭源模型（如GPT-4o、Gemini-2.5-Pro）、14B–32B参数的中型通用模型（如DeepSeek-R1-Distill-Qwen-32B）、≤7B参数的轻量模型（如ChatGLM3-6B），以及近期基于RAG和多智能体的诊断框架（如ColaCare、MedAgent-Pro）。所有方法使用相同测试协议和临床叙事进行评估。

外部知识源整合了结构化生物医学知识图谱（基于UMLS）和非结构化临床指南语料库（38份权威指南）。使用Qwen3-Embedding-8B进行密集检索，Milvus索引，Qwen3-Reranker-8B重排序。骨干模型为Llama-3.1-8B-Instruct，并通过蒸馏将Qwen3-Max的推理能力迁移至该模型，使用LoRA进行监督微调。

主要结果显示，MedCoRAG在所有评估方法中取得最佳性能：精确率81.32%、召回率79.18%、F1分数79.12%、F0.5分数78.99%。其表现优于参数量达8B的专用医学模型、大型闭源模型、中小型通用模型以及近期多智能体诊断框架，验证了其结合结构化证据合成与动态智能体协作方法的有效性。

### Q5: 有什么可以进一步探索的点？

MedCoRAG在肝病诊断上取得了显著进展，但其局限性也为未来研究提供了明确方向。首先，该框架仅处理单次临床快照，缺乏对实验室指标趋势、影像学演变等纵向时序信息的建模，这限制了其对慢性病进展或急性事件预测的能力。未来可集成时序模型（如Transformer或RNN）来捕捉动态临床轨迹。其次，系统依赖UMLS实体对齐和静态指南，对真实世界临床文本中的歧义和未标准化表述可能敏感。可通过增强实体链接的上下文理解能力，并引入动态更新的医学知识库来提升鲁棒性。此外，当前评估完全基于回顾性数据，需通过前瞻性临床研究验证其在实际工作流中的效用，并探索与电子病历系统的无缝集成。从架构角度看，多智能体协作虽提升解释性，但推理延迟较高（复杂案例平均33秒），未来可研究智能体剪枝、异步推理等轻量化机制以平衡效率与精度。最后，框架目前专注于肝病领域，其泛化能力尚未验证；可探索跨科室适配机制，并引入更多专科智能体以构建更全面的临床决策支持系统。

### Q6: 总结一下论文的主要内容

该论文提出了MedCoRAG框架，旨在解决肝脏疾病诊断中AI方法缺乏透明度、结构化推理和可部署性的问题。核心贡献在于构建了一个端到端的可解释诊断系统，通过混合证据检索与多智能体协作共识来提升诊断性能与可解释性。

方法上，首先基于患者异常指标，从UMLS知识图谱和临床指南中联合检索并剪裁路径，构建个性化的证据包。随后采用多智能体协同推理：路由智能体根据病例复杂度动态调度专科智能体，这些智能体在证据包上迭代推理并在需要时触发定向重检索，同时全科智能体综合所有讨论，形成可追溯的共识诊断，模拟多学科会诊。

实验基于MIMIC-IV真实肝病病例，结果表明MedCoRAG在诊断性能和推理可解释性上均优于现有方法及闭源模型。该工作推动了更透明、证据驱动且符合临床实践的AI医疗决策支持系统的发展。
