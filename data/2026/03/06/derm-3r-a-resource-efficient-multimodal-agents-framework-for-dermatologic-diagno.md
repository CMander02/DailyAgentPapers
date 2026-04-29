---
title: "DERM-3R: A Resource-Efficient Multimodal Agents Framework for Dermatologic Diagnosis and Treatment in Real-World Clinical Settings"
authors:
  - "Ziwen Chen"
  - "Zhendong Wang"
  - "Chongjing Wang"
  - "Yurui Dong"
  - "Luozhijie Jin"
  - "Jihao Gu"
  - "Kui Chen"
  - "Jiaxi Yang"
  - "Bingjie Lu"
  - "Zhou Zhang"
  - "Jirui Dai"
  - "Changyong Luo"
  - "Xiameng Gai"
  - "Haibing Lan"
  - "Zhi Liu"
date: "2026-03-06"
arxiv_id: "2604.09596"
arxiv_url: "https://arxiv.org/abs/2604.09596"
pdf_url: "https://arxiv.org/pdf/2604.09596v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体协作"
  - "资源高效框架"
  - "轻量级多模态LLM"
  - "皮肤科诊断治疗"
  - "中医"
  - "少样本微调"
relevance_score: 8.0
---

# DERM-3R: A Resource-Efficient Multimodal Agents Framework for Dermatologic Diagnosis and Treatment in Real-World Clinical Settings

## 原始摘要

Dermatologic diseases impose a large and growing global burden, affecting billions and substantially reducing quality of life. While modern therapies can rapidly control acute symptoms, long-term outcomes are often limited by single-target paradigms, recurrent courses, and insufficient attention to systemic comorbidities. Traditional Chinese medicine (TCM) provides a complementary holistic approach via syndrome differentiation and individualized treatment, but practice is hindered by non-standardized knowledge, incomplete multimodal records, and poor scalability of expert reasoning. We propose DERM-3R, a resource-efficient multimodal agent framework to model TCM dermatologic diagnosis and treatment under limited data and compute. Based on real-world workflows, we reformulate decision-making into three core issues: fine-grained lesion recognition, multi-view lesion representation with specialist-level pathogenesis modeling, and holistic reasoning for syndrome differentiation and treatment planning. DERM-3R comprises three collaborative agents: DERM-Rec, DERM-Rep, and DERM-Reason, each targeting one component of this pipeline. Built on a lightweight multimodal LLM and partially fine-tuned on 103 real-world TCM psoriasis cases, DERM-3R performs strongly across dermatologic reasoning tasks. Evaluations using automatic metrics, LLM-as-a-judge, and physician assessment show that despite minimal data and parameter updates, DERM-3R matches or surpasses large general-purpose multimodal models. These results suggest structured, domain-aware multi-agent modeling can be a practical alternative to brute-force scaling for complex clinical tasks in dermatology and integrative medicine.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对中医皮肤科诊断和治疗领域面临的核心挑战。首先，中医皮肤科实践受制于非标准化的知识体系、不完整的多模态记录（如图像-文本对应缺失）以及专家推理难以规模化，这限制了中医在皮肤科中的应用和扩展。其次，现代西医皮肤科治疗虽然能快速控制急性症状，但长期效果有限，存在单一靶点治疗、疾病复发频繁以及对系统性合并症关注不足等问题。中医提供了一种通过辨证论治和个体化方案的整体性互补方法，能够多靶点调节免疫、神经和内分泌系统，从而改善全身平衡、降低复发率。然而，将中医皮肤科知识转化为可计算的AI系统面临数据稀缺、任务复杂和计算资源受限等困难。因此，论文提出DERM-3R框架，旨在通过多智能体协作，在有限数据和计算资源下，建模中医皮肤科的诊断与治疗决策过程，解决上述挑战，并为复杂临床任务提供资源高效的AI解决方案。

### Q2: 有哪些相关研究？

论文涉及的相关研究主要集中在几个领域：一是大型语言模型（LLM）和视觉语言模型（VLM）在医疗诊断中的应用，如GPT系列、Gemini等通用多模态模型已用于医学问答和图像分析，但它们在中医皮肤科等细分领域表现受限，且计算成本高、易产生幻觉。二是多智能体系统研究，其中多个智能体协作处理复杂任务，如代码生成、网页交互等，但在医疗临床推理中的应用较少。三是资源高效AI方法，包括参数高效微调（如LoRA）和少样本学习，旨在减少数据和计算需求。此外，论文提到先前工作Tianyi语言模型，专注于中医知识建模。本文与这些工作的关系在于：它提出了一个专门针对中医皮肤科的多智能体框架，将临床工作流分解为三个智能体（识别、表示、推理），并基于轻量级VLM进行少样本微调，从而在特定医疗场景中实现了资源高效且高性能的AI系统，超越了通用大模型的暴力扩展方法。

### Q3: 论文如何解决这个问题？

论文通过任务分解、重定义和多智能体协作来解决问题。首先，基于真实临床工作流，将中医皮肤科决策过程重构为三个核心环节：细粒度病变识别（从单张图像提取病变特征）、多视图病变表示与专家级发病机制建模（聚合多张图像生成整体描述和发病机制分析）、以及整体推理用于辨证论治和治疗规划（整合多模态信息生成诊断和治疗方案）。基于此，框架包含三个协作智能体：DERM-Rec（识别智能体）负责单图像病变识别和语义表示，使用518个图像-文本对进行训练；DERM-Rep（表示智能体）聚合多视图图像，生成患者级病变描述和发病机制分析，使用148个高质量样本训练，并通过条件分布建模两步推理过程；DERM-Reason（推理智能体）整合DERM-Rep输出与患者病史、症状等，进行多模态临床推理，输出整体发病机制分析、辨证论治、治疗原则和处方推荐，使用134个样本训练。所有智能体基于Qwen2.5-VL-7B多模态LLM，将其语言模型替换为专注于中医的Tianyi模型，形成Derm-VL-7B，并通过LoRA进行参数高效微调。这种设计模仿了中医临床的渐进式决策，通过智能体间的结构化协作，有效应对了数据稀缺、任务复杂和资源受限的挑战，实现了领域感知的建模。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，包括自动评估和人类评估，以验证DERM-3R框架的性能。自动评估部分：使用BLEU-4和ROUGE-L指标量化模型输出与标准答案的文本相似度，并引入LLM-as-a-Judge方法（使用Gemini-3-Flash、GPT-5.2和DeepSeek-V3.2作为评判模型），结合检索增强生成（RAG）集成中医皮肤科知识库，以进行细粒度语义评估。评估对象为DERM-Rep和DERM-Reason智能体，比较模型包括GPT-5.1-instant、Gemini-3-Flash、Qwen2.5-VL-7B和Qwen3-VL-8B。结果显示，DERM-Rep在病变描述和发病机制分析上BLEU-4和ROUGE-L分数显著高于基线模型（如BLEU-4总分0.1772 vs. GPT-5.1的0.0410）；DERM-Reason在五项临床子任务（如辨证论治、治疗原则选择）上也取得最高平均分（BLEU-4 0.2887 vs. GPT-5.1的0.1664）。LLM-as-a-Judge评估中，DERM-Reason在所有评判模型下总得分均最高（平均34.4366 vs. GPT-5.1的23.6462）。人类评估部分：设计了多中心交叉验证，涉及9家医院的15名皮肤科医生，对DERM-3R生成的完整报告进行盲评（包括病变描述、发病机制分析、辨证论治、治疗原则、处方和可读性六项，总分60分）。结果表明，DERM-3R获得最高总分44.16（方差1.49），优于所有比较模型（如GPT-5.1得41.23分），并在多项任务上展现最低方差，证明了其性能优越性和稳定性。

### Q5: 有什么可以进一步探索的点？

尽管DERM-3R在中医皮肤科任务上表现出色，仍有多个方向值得进一步探索：第一，扩展疾病范围和数据多样性：当前研究仅基于银屑病病例，未来可扩展到其他皮肤疾病（如湿疹、痤疮）或中医其他科别，以验证框架的泛化能力；同时，探索数据增强或合成技术，以应对更小规模数据集。第二，优化智能体协作机制：目前智能体间协作是顺序性的，可研究更动态的通信策略（如基于注意力的信息交换）来提升推理效率。第三，增强模型的可解释性和安全性：医疗AI需确保决策透明，未来可集成可解释性工具（如注意力可视化）和沙箱机制，以减少误诊风险。第四，临床集成与部署：开展更大规模的临床试验，评估框架在真实工作流中的实用性和用户接受度，并与医院信息系统集成。第五，技术改进：探索更先进的微调方法（如适配器调优）或多模态对齐技术，以进一步提升在有限资源下的性能；同时，研究如何平衡领域特异性与通用能力。

### Q6: 总结一下论文的主要内容

论文提出了DERM-3R，一个资源高效的多模态多智能体框架，专为中医皮肤科诊断和治疗设计。该框架针对中医实践中的知识非标准化、数据稀缺和计算受限等挑战，通过任务分解将临床决策过程转化为三个核心环节：细粒度病变识别、多视图病变表示与发病机制建模、以及整体辨证论治推理。基于此，构建了三个协作智能体（DERM-Rec、DERM-Rep、DERM-Reason），所有智能体均基于轻量级多模态LLM（Qwen2.5-VL-7B，替换语言模型为中医专用Tianyi模型），并使用LoRA在仅103个真实银屑病病例上进行微调。实验通过自动指标（BLEU-4、ROUGE-L、LLM-as-a-Judge）和多中心人类评估（15名医生）验证，结果显示DERM-3R在性能上匹配甚至超越了GPT-5.1、Gemini-3-Flash等大型通用模型，尤其在辨证论治等核心任务上优势显著，且具有更高的稳定性。论文贡献在于：提供了临床落地的多智能体框架、提出了领域感知的任务分解范式、证明了数据与计算高效AI的可行性，并强调了结构化建模优于暴力扩展的方法，为医疗AI应用开辟了新路径。
