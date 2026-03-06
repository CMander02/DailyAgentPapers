---
title: "ClinNoteAgents: An LLM Multi-Agent System for Predicting and Interpreting Heart Failure 30-Day Readmission from Clinical Notes"
authors:
  - "Rongjia Zhou"
  - "Chengzhuo Li"
  - "Carl Yang"
  - "Jiaying Lu"
date: "2025-12-08"
arxiv_id: "2512.07081"
arxiv_url: "https://arxiv.org/abs/2512.07081"
pdf_url: "https://arxiv.org/pdf/2512.07081v2"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "LLM Application"
  - "Clinical Decision Support"
  - "Interpretability"
  - "Information Extraction"
relevance_score: 8.0
---

# ClinNoteAgents: An LLM Multi-Agent System for Predicting and Interpreting Heart Failure 30-Day Readmission from Clinical Notes

## 原始摘要

Heart failure (HF) is one of the leading causes of rehospitalization among older adults in the United States. Although clinical notes contain rich, detailed patient information and make up a large portion of electronic health records (EHRs), they remain underutilized for HF readmission risk analysis. Traditional computational models for HF readmission often rely on expert-crafted rules, medical thesauri, and ontologies to interpret clinical notes, which are typically written under time pressure and may contain misspellings, abbreviations, and domain-specific jargon. We present ClinNoteAgents, an LLM-based multi-agent framework that transforms free-text clinical notes into (1) structured representations of clinical and social risk factors for association analysis and (2) clinician-style abstractions for HF 30-day readmission prediction. We evaluate ClinNoteAgents on 3,544 notes from 2,065 patients (readmission rate=35.16%), demonstrating high extraction fidelity for clinical variables (conditional accuracy >= 90% for multiple vitals), key risk factor identification, and preservation of predictive signal despite 60 to 90% text reduction. By reducing reliance on structured fields and minimizing manual annotation and model training, ClinNoteAgents provides a scalable and interpretable approach to note-based HF readmission risk modeling in data-limited healthcare systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用临床自由文本笔记进行心力衰竭（HF）患者30天再入院风险预测和解释的挑战。研究背景是，心力衰竭是全球性的重大健康问题，再入院率高，给医疗系统带来沉重负担。电子健康记录（EHR）中的临床笔记包含了丰富的患者信息，尤其是社会健康决定因素（SDOH），这些对于再入院风险至关重要，但在数据资源有限的医疗环境中（如许多发展中国家，甚至美国EHR中80%的信息仍为非结构化文本），这些笔记未被充分利用。

现有方法的不足主要体现在几个方面：传统计算模型通常依赖专家制定的规则、医学词典和本体来解读临床笔记，但笔记本身可能存在拼写错误、缩写和领域特定术语，导致解读困难且扩展性差。此外，现有方法要么主要依赖结构化EHR数据而忽略了文本中的丰富信息，要么在利用NLP和LLM时，往往侧重于预定义的SDOH分类或仅关注社会因素，未能将临床预测因子与社会因素统一、协调地提取和整合到一个框架中，从而限制了模型的全面性和可解释性。

因此，本文要解决的核心问题是：如何开发一个可扩展、可解释的框架，能够从非结构化的出院笔记中，自动、准确地联合提取和结构化临床风险因素与社会风险因素，并基于此进行HF再入院风险预测和关联分析，以降低对结构化EHR数据的依赖，并最小化人工标注和模型训练的需求。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于结构化数据的传统模型、结合非结构化文本的混合模型，以及基于大语言模型（LLM）的提取与预测方法。

在**传统与混合模型**方面，早期的心力衰竭再入院风险模型主要依赖结构化电子健康记录（EHR）数据，如人口统计学、实验室指标等。后续研究开始纳入非结构化临床笔记以获取更丰富的上下文信息，例如通过笔记嵌入与结构化变量结合的混合模型提升了预测性能。这些方法通常依赖于专家制定的规则、医学词典或预定义的社会健康决定因素（SDOH）分类体系。

在**基于LLM的NLP方法**方面，近期研究利用自然语言处理（NLP）和LLM从临床笔记中提取临床或社会风险因素。例如，有工作使用机器学习或Transformer模型基于出院笔记进行预测，或通过摘要预处理提升信号质量，LLM也被证明能以接近临床医生的准确度提取SDOH。

**本文工作（ClinNoteAgents）与这些研究的区别和关系在于**：它继承了利用非结构化文本和LLM技术的方向，但提出了一个统一的、基于多智能体的框架。与多数现有方法仅关注社会因素或依赖预定义分类法不同，本文框架能**联合提取并协调**临床与社会风险因素，并将其转化为结构化表示和临床风格的摘要，既用于关联分析也用于预测建模。这减少了对结构化EHR字段和大量人工标注的依赖，旨在为数据有限的医疗系统提供一种可扩展且可解释的解决方案。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ClinNoteAgents的基于大语言模型（LLM）的多智能体系统来解决心力衰竭（HF）30天再入院预测和风险因素挖掘问题。其核心方法是将自由文本的临床记录转化为两种结构化表示：一是用于关联分析的结构化临床与社会风险因素；二是用于预测的、类似临床医生风格的摘要。

**整体框架与主要模块**：
系统包含三个核心智能体，均基于Qwen3-14B模型实现：
1.  **风险因素提取器**：使用精心设计的领域特定提示词，从出院记录中提取结构化的风险因素。提取范围涵盖三类信息：已记录的社会健康决定因素（如性别、年龄）、未记录的社会健康决定因素（如酒精使用、住房状况）以及临床测量值（如生命体征、主诉、诊断）。
2.  **风险因素标准化器**：针对文本中异质性强的社会健康决定因素，设计了一个两阶段的LLM标准化流程。首先由“标准化器”LLM为每个变量生成一组简洁的标准化类别，然后由“标注器”LLM将提取的原始值分配至对应类别，从而将自由文本转化为可用于定量分析的分类值。
3.  **记录摘要器**：为了提升下游预测模型的性能并增强可解释性，该模块将冗长的原始记录转化为精炼的临床摘要。论文特别比较了两种摘要方式：一是包含数值的“整体摘要”；二是将所有数值替换为定性描述的“无数字摘要”，旨在减少LLM处理原始数字时的不稳定性。

**关键技术流程与创新点**：
1.  **任务形式化与数据构建**：将问题明确分解为两个相互关联的子任务——再入院风险预测（学习映射 f: X_i → y_i）和风险因素挖掘（通过提取器 h(·) 获得结构化风险因素 R_i，再进行统计分析）。研究利用MIMIC-III数据库，通过连接每次入院与其后续入院构建分析对，以前次出院的摘要作为输入，并以此确定30天再入院标签。
2.  **多智能体协同的端到端分析流程**：三个智能体顺序协作，首先从非结构化文本中提取并结构化关键变量，接着对这些变量进行标准化处理，最后生成用于预测的定性或定量摘要。这种设计实现了从原始文本到预测与解释的完整分析链条。
3.  **评估框架的综合性**：论文设计了多维度的评估体系：通过对比结构化EHR数据来评估提取的准确性和覆盖度；通过逻辑回归和卡方检验等统计方法分析提取的风险因素与再入院结局的关联；通过下游机器学习分类器（如逻辑回归、XGBoost）的性能（准确率、F1、AUROC等）来评估不同摘要方法对预测效果的提升。

总之，ClinNoteAgents的创新在于利用LLM多智能体协作，自动化地完成从临床记录中提取、标准化信息并生成预测性摘要的全过程，减少了对结构化字段和大量人工标注的依赖，为数据有限的医疗系统提供了一种可扩展且可解释的风险建模方法。

### Q4: 论文做了哪些实验？

论文实验主要围绕风险因素挖掘和再入院预测两大模块展开。在风险因素挖掘方面，实验首先评估了从临床笔记中提取临床变量和社会决定因素（SDOH）的准确性，使用结构化电子健康记录（EHR）作为替代真实值。提取覆盖率（% Extracted）从身高的4.03%到心率的89.25%不等；在提取非空值的情况下，条件准确率（Cond Acc）多数在90%左右（如收缩压90.85%，舒张压91.24%），但体重较低（57.90%）。对于诊断提取，采用LLM-as-a-judge框架评估，平均相似性得分为3.04（0-5分），条件准确率为62.27%。其次，通过LLM代理对SDOH进行归一化，将自由文本条目标准化为可分析的类别（如婚姻状况分为5类）。最后，进行相关性分析：对数值变量（如生命体征、年龄）使用逻辑回归，发现年龄（OR=1.008, p=0.008）、体重（OR=0.778, p=0.010）和血压（收缩压OR=0.816, p<0.001）与心衰再入院显著相关；对分类变量（如SDOH）使用卡方检验，仅住房状况显著（p=0.012）。

在再入院预测方面，实验评估了将出院笔记转换为结构化临床摘要对预测性能的影响。使用包含3,544份笔记（来自2,065名患者，再入院率35.16%）的数据集，比较了三种摘要方法（无数字摘要、整体摘要、结构化提取摘要）与原始笔记的预测效果，并采用三种分类器：TF-IDF+逻辑回归（LR）、ClinicalBERT和LoRA微调的Qwen3-8B。主要结果以AUROC衡量：原始笔记性能最高（LR: 0.6535；ClinicalBERT: 0.6095；LoRA: 0.6064）。尽管文本压缩率达60-90%，摘要后性能下降适中。其中，无数字摘要（压缩61.36%）表现最佳，AUROC接近原始基线（LR: 0.6434；ClinicalBERT: 0.6046）；而结构化提取摘要（压缩91.44%）下降最大（LR: 0.5735）。实验表明，ClinNoteAgents在保持预测信号的同时，实现了高提取保真度和显著文本压缩。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向包括：首先，LLM在提取身高、体重等异质格式数据时准确率显著下降，且存在幻觉风险。未来可研究更鲁棒的数值与单位解析方法，例如结合规则引擎或小型专用模型进行后处理校验。其次，社会决定因素（SDOH）的提取覆盖度低，部分源于临床记录本身文档不全。未来可探索多模态数据融合（如结合护理记录、社工评估），并设计针对SDOH的提示工程或微调策略以提升召回率。再者，摘要生成并未带来预测性能的显著提升，表明信息压缩与关键信号保留的平衡点需进一步优化，可探索基于预测任务的反向指导摘要方法。最后，缺乏临床医生对提取与摘要结果的直接评估，未来工作应引入闭环临床验证，并将系统嵌入真实工作流以评估其可用性与影响。此外，可探索智能体间更动态的协作机制，例如让摘要智能体根据提取结果动态调整焦点，以提升整体系统的自适应能力。

### Q6: 总结一下论文的主要内容

该论文提出了ClinNoteAgents，一个基于大语言模型的多智能体框架，旨在利用临床文本笔记预测和解释心力衰竭患者30天再入院风险。核心问题是临床笔记虽信息丰富但非结构化，包含拼写错误和术语缩写，传统方法依赖专家规则和词典，难以高效利用。该方法通过多智能体协作，将自由文本转换为结构化临床变量、社会风险因素表示以及用于预测的临床风格摘要。主要结论显示，系统在3544份笔记上验证，对关键临床变量提取准确率高（≥90%），能识别风险因素，并在文本压缩60-90%情况下保持预测信号。其意义在于减少对结构化字段和人工标注的依赖，为数据有限的医疗系统提供了可扩展、可解释的心衰再入院风险建模方案。
