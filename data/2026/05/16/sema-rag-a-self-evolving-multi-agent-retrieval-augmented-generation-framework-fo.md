---
title: "SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning"
authors:
  - "Yongfeng Huang"
  - "Ruiying Chen"
  - "James Cheng"
date: "2026-05-16"
arxiv_id: "2605.17101"
arxiv_url: "https://arxiv.org/abs/2605.17101"
pdf_url: "https://arxiv.org/pdf/2605.17101v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体RAG"
  - "医学问答"
  - "自进化检索"
  - "任务解耦"
  - "临床推理"
  - "LLM Agent"
relevance_score: 9.0
---

# SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning

## 原始摘要

Retrieval-Augmented Generation (RAG) is widely employed to mitigate risks such as hallucinations and knowledge obsolescence in medical question answering, yet its predominantly single-round, static retrieval paradigm misaligns with the multi-stage process of clinical reasoning. This compressed workflow induces two structural deficiencies: question-to-query translation often lacks clinically grounded semantic interpretation, and retrieval lacks iterative sufficiency feedback, making it difficult to form reliable evidence chains. We argue that both issues stem from a deeper cause: overloading a single reasoning chain with heterogeneous tasks of interpretation, exploration, and adjudication. The remedy is to reconstruct the workflow via task decoupling and dynamic multi-round exploration. To this end, we propose SEMA-RAG, a Self-Evolving Multi-Agent RAG framework for medical question answering, which assigns these roles to three specialist agents: the Interpreter Agent for clinical schema interpretation, the Explorer Agent for sufficiency-driven self-evolving retrieval, and the Arbiter Agent for evidence adjudication and answer selection. Across five benchmarks and five LLM backbones, SEMA-RAG improves the strongest baseline by +6.46 accuracy points on average, measured per backbone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有检索增强生成（RAG）框架在医学问答中存在的根本性缺陷。研究背景是，虽然RAG被广泛用于缓解大语言模型在医学领域的幻觉和知识过时问题，但标准RAG框架通常采用静态、单轮的检索范式。这与临床推理的多阶段过程（包括问题解释、证据收集和判断整合）严重不匹配。这种压缩的工作流导致了两个结构性不足：第一，从问题到查询的转换缺乏基于临床语义的解读，难以显式表达隐含约束；第二，检索过程缺乏基于证据充分性的反馈机制，无法在证据不足时进行自适应的迭代收敛，从而难以形成可靠的证据链。论文认为，这两个问题的深层原因在于将问题解读、证据探索和答案裁决这几种异质任务过度耦合到单一推理链中，导致认知负荷增大，模型难以在证据不足或矛盾时灵活调整。因此，本文提出SEMA-RAG框架，其核心思想是通过任务解耦和角色分工（解释者、探索者、裁决者三个专业智能体）来重构工作流，并引入自演进的、基于证据充分性驱动的多轮检索，使系统在测试过程中能动态调整和收敛证据链，从而解决现有静态单轮RAG的核心缺陷。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**迭代式RAG方法**、**医疗领域多智能体系统**和**通用多智能体协作框架**。

1. **迭代式RAG方法**：如Self-RAG、CRAG通过自我反思触发重新检索，i-MedRAG通过追问迭代优化查询。但这些方法缺乏临床意图和约束建模，容易导致浅层重写、检索漂移和失控扩展。SEMA-RAG通过显式解耦"解释-探索-裁决"任务，引入临床模式解释（Interpreter）和充分性驱动的自我进化检索（Explorer），避免了无意义的重复检索。

2. **医疗多智能体系统**：如MedAgents、Agent-Hospital通过多角色协作提升诊断质量。但现有工作假设关键证据已在上下文中，主要聚焦于 deliberation（审议），忽视了证据获取的系统性，如差距识别、充分性终止、证据裁决与整合。SEMA-RAG专门设计了Arbiter Agent进行证据裁决和答案选择，并构建了封闭的证据链。

3. **通用多智能体框架**：如CAMEL、MetaGPT通过角色专业化解决复杂任务，ReAct结合推理与工具使用。SEMA-RAG在此基础上针对医疗推理场景，将临床推理拆解为三个专用智能体，实现了从静态单次检索到动态多轮探索的范式转变。

简言之，本文的核心区别在于首次将任务解耦、临床模式解释和充分性驱动的自进化检索系统性地整合到医疗RAG框架中。

### Q3: 论文如何解决这个问题？

SEMA-RAG 通过任务解耦和多轮动态检索解决传统RAG在医学问答中的结构缺陷。核心是将解释、探索和裁决三种异构任务分离，赋予三个专业智能体：解析智能体(I-Agent)、探索智能体(E-Agent)和裁决智能体(A-Agent)，它们共享同一个底层语言模型，仅通过角色提示区分。

整体框架以I-Agent为起点，它将输入医学问题Q解析为临床模式元组Q'，包含临床意图、医学实体、临床约束和初始检索查询四部分。通过线性化函数将Q'转换为检索查询字符串，保留核心查询的同时显式融入临床约束，减少初始检索阶段的语义漂移。

E-Agent负责自进化迭代检索。它以线性化模式查询为起点，在多轮循环中基于当前证据集和临床锚点，预测充分性标志、缺口描述和下一轮查询集。当证据不足时生成多个候选后续查询，针对缺失条件或推理步骤进行补充检索，直到证据充分、达到最大迭代次数或停滞为止。这一过程构建了最终证据集C*和自进化轨迹。

A-Agent执行证据裁决与答案选择。它首先对证据集进行裁决，去除冗余和冲突内容，将支持和反对线索组织成结构化证据报告R，保留每个证据的文档标识符实现可追溯性。最后基于R和候选答案集Y进行离散答案选择，确保答案完全基于证据支撑。

### Q4: 论文做了哪些实验？

论文在五个医疗问答基准（MMLU-Med、MedQA-US、MedMCQA、PubMedQA*、BioASQ-Y/N）上进行了实验，并使用五个不同LLM作为骨干模型（deepseek-v3.1、kimi-k2、qwen3-coder-plus、gemini-2.0-flash、glm-4.0-flash）。对比方法包括：无检索的CoT、单轮检索的MedCPT和MedRAG、以及迭代检索的i-MedRAG。所有方法在零样本设置下评估，使用MedCPT作为检索器，从Textbooks和StatPearls语料库中检索。SEMA-RAG默认设置T_max=2, k=16, m=3。

主要结果表明，SEMA-RAG在每个骨干模型下均取得最佳平均准确率，例如在deepseek-v3.1上平均准确率从基线最佳（i-MedRAG）的71.49%提升至79.71%，提升达+8.22个百分点；在gemini-2.0-flash上从最佳基线（MedRAG）的65.04%提升至78.08%，提升显著。

此外，还进行了角色消融实验，在MedQA-US和PubMedQA*上检验三个智能体的贡献。移除E-Agent（取消自演进检索）导致最大性能下降（MedQA-US从89.95%降至83.58%），移除I-Agent或A-Agent也分别有下降。同时，探索了最大迭代次数T_max（1-9）和每轮查询广度m（1-3）的影响，发现T_max=2或3时性能最优（MedQA-US上T_max=2达89.95%，T_max=3达90.10%），且增加m值（从1到3）持续提升准确率，但边际效益递减。这些结果验证了任务解耦与自演进多轮检索设计的有效性。

### Q5: 有什么可以进一步探索的点？

SEMA-RAG通过任务解耦和动态多轮探索提升了医疗推理性能，但仍存在多个可深入探索的方向。首先，当前评估局限于基准测试，未来应扩展到真实临床工作流，如纵向EHR推理或基于记录的决策支持；这要求框架能处理非结构化病历和时序数据。其次，检索语料库的质量和覆盖率是关键瓶颈，若关键证据缺失或过时，自演进循环可能收敛到不完整的依据；引入动态知识库更新或跨源验证机制（如结合医学知识图谱的语义检索）可增强鲁棒性。第三，充分性标准仅针对检索轮次设计，未考虑选项级可分离性或生成完整性；可探索基于信息论（如互信息）或推理路径嵌入的细粒度终止条件。此外，证据累积缺乏显式相关性过滤，性能对超参数敏感；可引入轻量级门控网络或对比学习来筛选噪声证据。最后，角色专业化带来的推理开销可通过混合专家（MoE）架构或自适应任务分发（如单轮简单问题跳过迭代）来优化，平衡精度与效率。

### Q6: 总结一下论文的主要内容

SEMA-RAG提出了一种用于医学问答的自进化多智能体RAG框架。论文指出，传统RAG采用单轮静态检索方式，与临床推理的多阶段过程不匹配，导致两个结构性问题：问题到查询的转换缺乏临床语义解释，以及检索缺乏迭代反馈，难以形成可靠证据链。这些问题源于将解释、探索和裁决等异构任务过度集中于单一推理链。SEMA-RAG通过任务解耦和动态多轮探索重构工作流，将角色分配给三个专家智能体：解释智能体负责临床模式解释、探索智能体负责自进化检索、裁决智能体负责证据评估和答案选择。在五个基准测试和五个LLM骨干上，SEMA-RAG相比最强基线平均提升了+6.46个准确率点。实验还验证了其在不同检索器、小模型和开放交互场景中的鲁棒性，表明医学RAG应从静态单轮检索转向适应性更强的证据构建方式。
