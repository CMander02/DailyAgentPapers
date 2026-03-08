---
title: "MedCollab: Causal-Driven Multi-Agent Collaboration for Full-Cycle Clinical Diagnosis via IBIS-Structured Argumentation"
authors:
  - "Yuqi Zhan"
  - "Xinyue Wu"
  - "Tianyu Lin"
  - "Yutong Bao"
  - "Xiaoyu Wang"
date: "2026-03-01"
arxiv_id: "2603.01131"
arxiv_url: "https://arxiv.org/abs/2603.01131"
pdf_url: "https://arxiv.org/pdf/2603.01131v1"
categories:
  - "cs.MA"
  - "cs.AI"
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
  key_technique: "MedCollab (dynamic specialist recruitment, IBIS-structured argumentation, Hierarchical Disease Causal Chain, multi-round Consensus Mechanism)"
  primary_benchmark: "ClinicalBench, MIMIC-IV"
---

# MedCollab: Causal-Driven Multi-Agent Collaboration for Full-Cycle Clinical Diagnosis via IBIS-Structured Argumentation

## 原始摘要

Large language models (LLMs) have shown promise in healthcare applications, however, their use in clinical practice is still limited by diagnostic hallucinations and insufficiently interpretable reasoning. We present MedCollab, a novel multi-agent framework that emulates the hierarchical consultation workflow of modern hospitals to autonomously navigate the full-cycle diagnostic process. The framework incorporates a dynamic specialist recruitment mechanism that adaptively assembles clinical and examination agents according to patient-specific symptoms and examination results. To ensure the rigor of clinical work, we adopt a structured Issue-Based Information System (IBIS) argumentation protocol that requires agents to provide ``Positions'' backed by traceable evidence from medical knowledge and clinical data. Furthermore, the framework constructs a Hierarchical Disease Causal Chain that transforms flattened diagnostic predictions into a structured model of pathological progression through explicit logical operators. A multi-round Consensus Mechanism iteratively filters low-quality reasoning through logic auditing and weighted voting. Evaluated on real-world clinical datasets, MedCollab significantly outperforms pure LLMs and medical multi-agent systems in Accuracy and RaTEScore, demonstrating a marked reduction in medical hallucinations. These findings indicate that MedCollab provides an extensible, transparent, and clinically compliant approach to medical decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在临床诊断应用中存在的两个核心问题：诊断幻觉（即生成不准确或无依据的医学结论）以及推理过程缺乏可解释性和临床严谨性。研究背景是，尽管LLM在医疗问答和报告生成方面展现出潜力，但其在真实临床工作流程中的部署仍受限，因为复杂的、非结构化的临床记录需要严格的鉴别诊断和符合病理学逻辑的推理，而现有LLM方法往往只能进行模式匹配，无法提供可追溯的、基于临床证据的解释。

现有方法，特别是近期出现的多智能体诊断框架，通过分工协作推进了诊断推理，但仍存在关键不足。这些系统通常将诊断视为一系列独立的、关联性的输出，即识别与症状相关的疾病，但未能区分相关性与因果关系。这导致诊断结论可能次优甚至危险，生成的诊断在病因学上是脱节的，无法捕捉疾病之间的病理进展链条（例如，从创伤到肋骨骨折，再到肺出血和贫血的因果序列）。同时，智能体的断言缺乏可追溯的、针对具体病例的证据支撑，难以进行逻辑审计。

因此，本文要解决的核心问题是：如何构建一个能够模拟现代医院层级化会诊流程、并确保推理过程具备因果严谨性和高度可解释性的自动化全周期临床诊断框架。为此，论文提出了MedCollab，一个因果驱动的多智能体协作框架。它通过动态招募专科智能体、采用基于议题的信息系统（IBIS）结构化论证协议来确保每个诊断立场都有迹可循的证据支持，并构建分层疾病因果链（HDCC）来显式建模病理进展中的因果和共病关系，从而将扁平的疾病预测转化为结构化的病理叙事，最终通过共识机制迭代优化，生成逻辑一致且临床可信的诊断。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类研究中，多智能体系统（如MedAgents、MedAgents-v2）通过分工协作提升了诊断任务的性能，但它们通常将诊断视为独立症状与疾病的关联性匹配，缺乏对疾病间因果关系的建模。本文提出的MedCollab框架则通过构建**分层疾病因果链（HDCC）**，显式地建模了病理进展中的因果与共病关系，从而超越了单纯的关联性诊断。

在应用类研究中，现有工作（如基于LLaMA的医疗问答模型）虽然能处理医疗文本，但普遍存在“诊断幻觉”和推理过程不透明的问题。本文通过引入**基于议题的信息系统（IBIS）论证协议**，要求每个诊断观点都必须有可追溯的证据支持，从而实现了临床推理的严谨性和可审计性，这与以往黑箱式的方法形成鲜明区别。

此外，在评估方面，本文不仅使用准确率等传统指标，还引入了**RaTEScore**来量化诊断的逻辑连贯性，这比以往仅关注最终答案正确性的评测更为深入。

### Q3: 论文如何解决这个问题？

论文通过一个名为MedCollab的多智能体协作框架来解决临床诊断中LLMs存在的幻觉和推理可解释性不足的问题。其核心方法是模拟现代医院的分级会诊工作流，将完整的诊断周期结构化、逻辑化，并通过动态协作与共识机制确保诊断的严谨性。

整体框架包含四个关键部分：动态智能体招募、基于IBIS的结构化论证、分层疾病因果链构建以及全科医生主导的共识机制。首先，系统由一个全科医生智能体根据患者的主诉、病史和原始检查结果，动态招募相关的临床专科医生和检查科智能体，形成一个定制化的专家团队。检查科智能体直接解读原始医学发现生成专业报告，与基础临床记录共同构成证据库，为后续诊断提供事实约束，减少信息幻觉。

在诊断推理环节，系统采用议题式信息系统结构来规范每个智能体的输出。每个参与的专科智能体不是生成自由文本，而是必须输出结构化的IBIS元组，包含议题、诊断假设、临床论证以及严格源自证据库或医学知识库的追溯证据。这种设计将非正式的对话转化为可验证的有向无环论证图，确保了推理过程的透明性和可追溯性。

针对扁平化诊断标签缺乏病因逻辑一致性的问题，论文提出了分层疾病因果链的创新设计。该模型将所有验证过的诊断假设通过两种临床关系组织起来：因果关系和共病关系。系统构建出有向的病理进展链，从而区分根本病因和下游并发症，形成结构化的疾病轨迹。每条因果链的置信度分数由支持该链的智能体的权重及其论证的逻辑有效性加权计算得出。

最后，通过一个迭代的多轮共识机制来优化结果。全科医生智能体监督整个过程，对每个智能体的论证进行逻辑审计，并根据其论证与医学共识的逻辑不一致性，以指数惩罚方式动态调整其权重。这个过程持续迭代，直到某条因果链获得明确的多数支持，从而过滤低质量推理，确保最终诊断符合严格的临床标准。整个框架通过这种结构化的协作与逻辑约束，显著提升了诊断的准确性和可解释性。

### Q4: 论文做了哪些实验？

论文在ClinicalBench（1500例真实临床病例）和MIMIC-IV（595例病例子集）两个数据集上进行了实验。实验设置包括将数据统一格式化为会诊模式，并使用DeepSeek-V3生成标准化真实标签。评估指标涵盖诊断精度（如准确率ACC、综合诊断率CDR、实体F1值Entity-F1、科室分类准确率DCA）和临床推理质量（如RaTEScore、BLEU、ROUGE-L）。对比方法包括领先的大语言模型（如GPT-4o、Gemini-3-Flash、GLM-4.7等）和医疗多智能体系统（如MedLA、ClinicalAgent、MEDDxAgent）。

主要结果显示，MedCollab在诊断精度上显著优于基线。在ClinicalBench上，其ACC达到76.9%，比最佳基线（ClinicalAgent的68.7%）高出8.2个百分点；在MIMIC-IV上ACC为57.7%，同样领先。CDR在ClinicalBench上达到72.4%，超出最佳基线13.1个百分点以上。Entity-F1和DCA也均为最高，表明其有效减少了医学幻觉并实现了准确的科室分诊。在临床推理质量上，MedCollab在诊断依据（DB）等维度的RaTEScore最高（如ClinicalBench上DB RaTEScore为62.0%），超越了仅依赖表面文本相似度的基线模型。消融实验进一步证实，移除逻辑审核机制会使ACC从76.9%大幅降至49.7%，移除因果链则使ACC降至52.9%，证明了各核心组件的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文在可解释性和逻辑一致性方面取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，其因果链和论证协议高度依赖预设的医学知识结构，可能难以泛化到罕见病或复杂多病症交织的临床场景。其次，框架中的“共识机制”虽能过滤低质量推理，但多轮迭代可能导致诊断效率下降，在实时急诊环境中应用受限。

未来研究可从以下方面深入：一是增强动态适应性，探索基于在线学习的知识更新机制，使系统能持续整合最新临床指南和病例数据。二是引入不确定性量化，让模型不仅能输出诊断，还能评估每个结论的置信度，辅助医生权衡风险。三是探索跨模态协作，将文本论证与医学影像、时序生理信号等数据融合，构建更立体的诊断依据。此外，可尝试将IBIS协议扩展至治疗规划与预后评估阶段，实现全周期临床决策支持。

### Q6: 总结一下论文的主要内容

该论文提出了MedCollab，一个基于因果驱动的多智能体协作框架，旨在实现全周期临床诊断。核心问题是解决大语言模型在医疗应用中存在的诊断幻觉和推理可解释性不足的局限。方法上，该框架模拟现代医院的分级会诊流程，通过动态专家招募机制，根据患者特定症状和检查结果自适应地组建临床与检查智能体团队。为确保临床工作的严谨性，系统采用结构化的问题型信息系统（IBIS）论证协议，要求智能体提供有医学知识和临床数据可追溯证据支持的“立场”。此外，框架构建了分层疾病因果链，通过显式逻辑运算符将扁平的诊断预测转化为结构化的病理进展模型，并利用多轮共识机制，通过逻辑审计和加权投票迭代筛选低质量推理。主要结论显示，在真实世界临床数据集上的评估中，MedCollab在准确性和RaTEScore上显著优于纯大语言模型和其他医疗多智能体系统，并大幅减少了医疗幻觉。其核心贡献在于提供了一个可扩展、透明且符合临床规范的医疗决策新途径，对推动AI在临床实践中的可靠应用具有重要意义。
