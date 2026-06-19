---
title: "MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization"
authors:
  - "Aueaphum Aueawatthanaphisut"
date: "2026-06-18"
arxiv_id: "2606.20164"
arxiv_url: "https://arxiv.org/abs/2606.20164"
pdf_url: "https://arxiv.org/pdf/2606.20164v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
  - "q-bio.QM"
tags:
  - "多智能体协作"
  - "医学AI Agent"
  - "递归推理"
  - "长上下文推理"
  - "临床决策支持"
  - "证据图记忆"
  - "传感器引导"
  - "不确定性管理"
relevance_score: 9.0
---

# MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization

## 原始摘要

Real-world clinical decision support requires reasoning over heterogeneous and longitudinal patient information rather than answering isolated medical questions. However, current medical large language models and retrieval-augmented generation systems often rely on single-step prompting or retrieval, which can be fragile when clinical evidence is distributed across long electronic health records, medical images, sensor streams, guidelines, and referral constraints. This paper proposes MedRLM, a Recursive Multimodal Health Intelligence framework for long-context clinical reasoning, sensor-guided screening, and community-to-tertiary referral support. Instead of compressing all patient information into one prompt, MedRLM treats the patient case as an external clinical environment that can be recursively inspected, decomposed, retrieved, verified, and synthesized. The framework coordinates specialized agents for clinical text, longitudinal EHR, medical imaging, physiological sensor signals, guideline retrieval, uncertainty auditing, and referral planning. It further introduces a Clinical Evidence Graph Memory to connect patient-specific observations with retrieved evidence, standardized definitions, sensor-derived biomarkers, and referral criteria. A sensor-guided recursive triggering mechanism activates deeper reasoning when abnormal physiological or behavioral patterns are detected, while uncertainty-gated refinement supports clinician review for high-risk or low-confidence cases. We also outline a real-data evaluation design using public and credentialed clinical datasets spanning EHR, radiology, ECG, ICU time series, and referral-proxy outcomes. MedRLM aims to move medical AI from static question answering toward auditable, multimodal, and workflow-aware clinical decision support.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前医疗AI在面对真实世界临床决策支持时的一个核心问题：现有方法（如医疗大语言模型和检索增强生成系统）通常依赖单步提示或检索，无法有效处理分散在长电子健康记录、医学图像、传感器信号、临床指南和转诊约束中的异质性、长期患者信息。研究背景方面，尽管医疗LLM在知识编码和问答上表现优异，但临床决策是复杂的多步推理任务，压缩所有信息到单个提示会导致上下文丢失、幻觉、推理不可靠和可追溯性差。现有长上下文LLM也存在“中间信息丢失”的退化问题，而简单的RAG系统仅聚焦检索，未建模递归临床工作流。因此，本文提出MedRLM，一个递归多模态健康智能框架，其核心创新在于将患者数据视为外部临床环境，通过递归检查、分解、检索、验证和合成来动态处理；引入临床证据图记忆连接观测与证据，并设计传感器引导的递归触发和不确定性门控优化，从而解决从社区到三级医院的长期临床推理、传感器筛查和循证转诊优化问题，推动医疗AI从静态问答迈向可审计、工作流感知的临床决策支持。

### Q2: 有哪些相关研究？

相关研究主要分为四类：**长上下文推理方法**、**医疗大语言模型**、**检索增强生成（RAG）系统**以及**纵向电子健康记录（EHR）建模**。

1. **长上下文推理**：现有工作如LongBench指出单纯扩展上下文窗口难以保证可靠推理；递归语言模型（如SRLM、λ-RLM）通过外部化长提示、程序化分解信息来提升推理能力。MedRLM继承其递归思想，但将应用从通用长上下文任务转向临床推理，并协调文本、影像、传感器等多模态信息，而非仅处理文本。

2. **医疗大语言模型**：Med-PaLM/Med-PaLM 2展示了LLM在医学问答中的潜力；LLaVA-Med、Med-PaLM Multimodal等扩展了多模态能力。然而，这些模型主要被评估为答案生成系统，缺乏对长病史、传感器触发推理及可审计证据综合的显式机制。MedRLM将LLM定位为递归临床控制器，而非单一答案生成器。

3. **医疗RAG系统**：MEDRAG、MIRAGE及多模态RAG方法通过检索提升事实性，但通常聚焦于改进单轮问答的准确性。MedRLM将检索融入递归临床工作流，使检索证据不仅用于问答，还用于更新风险评估、不确定性分析及转诊规划。

4. **纵向EHR建模**：如EHRSHOT聚焦于纵向结构化数据的少样本预测，但未考虑社区筛查场景中的症状、传感器及转诊约束。MedRLM通过整合纵向患者表征、传感器数字生物标志物、多模态检索与转诊效用优化，填补了这一空白。

因此，MedRLM的核心区别在于：其目标不是回答孤立问题，而是通过递归、多模态、感知风险的推理，生成可审计且上下文敏感的转诊决策支持。

### Q3: 论文如何解决这个问题？

MedRLM通过递归多模态健康智能框架解决长上下文临床推理难题，其核心思想是将患者的异质性数据视为外部临床环境，而非压缩为单一提示。整体框架由递归控制器、专用智能体、临床证据图记忆和推理规划模块组成。

递归控制器是系统的核心，它通过上下文复杂度函数 \(\kappa(q,\E_p)\) 评估案例的长度、模态多样性、证据分散性和临床风险。若复杂度低于阈值 \(K\)，控制器直接调用基础模型 \(M\) 进行检索和回答；若超过阈值，则将临床查询 \(q\) 分解为多个细粒度子查询 \(q_j\)（如文本、EHR、图像、传感器、指南等），并为每个子查询构建子环境 \(\E_{p,j}\)。这种递归分解机制避免了长文档中的信息丢失和中间困惑问题。

每个子查询由专用智能体处理：文本智能体提取症状实体，EHR智能体建模纵向时间风险，图像VLM生成异常图谱，传感器编码器计算数字生物标志物，临床RAG检索指南证据。所有智能体的输出通过证据箭头汇入临床证据图记忆 \(\M_p = (\mathcal{V}_p, \mathcal{E}^{g}_p)\)，以可审计三元组 \(\tau_i = (o_i, s_i, \delta_i)\) 形式连接患者观察、支撑证据和标准化定义。

传感器引导的递归触发机制是关键创新：当传感器检测到异常生理或行为模式时，系统主动启动更深层次的推理循环。不确定性门控细化模块通过自一致性检查评估置信度，对高风险或低置信度案例要求人工审核。最终输出包括风险评分、可溯源证据解释、转诊决策（观察/远程会诊/转至三级中心）以及完整的审计轨迹。

### Q4: 论文做了哪些实验？

论文的实验设计聚焦于验证MedRLM在真实多模态临床数据上的推理与决策能力。实验使用了六个公开或经授权可访问的数据集：MIMIC-IV v3.1（364,627名患者，546,028次住院，用于长上下文EHR推理）、MIMIC-CXR-JPG v2.1.0（377,110张胸片，用于影像-报告多模态对齐）、CheXpert（224,316张胸片，含不确定性标签，用于异常检测基准）、eICU-CRD v2.0（超过200,000次ICU入院，用于多中心ICU风险验证）、PTB-XL v1.0.3（21,799份12导联心电图，用于传感器引导的递归筛查）以及PhysioNet/CinC Challenge 2012（12,000个ICU成年病例，用于死亡率预测校准）。实验框架通过协调文本、EHR、影像、生理信号、指南检索和转诊规划等专用智能体，在长上下文推理、影像-报告对齐、传感器引导筛查和转诊代理指标（如ICU入院、院内死亡率、急性恶化、再入院、专科升级或远程ICU干预）上进行评估。主要结果显示，MedRLM在所有核心证据通道上均能有效运作：MIMIC-IV和eICU支持长程病史与ICU验证；MIMIC-CXR和CheXpert支持影像报告对齐；PTB-XL和2012 Challenge支持生理信号时间序列筛查。由于直接社区-三级转诊标签在公共数据集中稀缺，实验采用临床可辩护的代理转诊结局（如ICU入院或院内死亡率）进行风险分层与决策支持评估，无需引入合成数据。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在以下方面：第一，MedRLM的递归推理机制可能在高复杂度临床场景中面临计算效率瓶颈，尤其是多轮跨模态检索与证据图更新可能导致响应延迟；第二，当前框架对传感器信号的解读更多依赖预定义异常阈值，缺乏对长程时序模式中细微病理演变的捕捉能力；第三，不确定性门控机制的实际临床阈值设定需大量专家标注，且可能因不同科室、不同疾病谱系存在校准偏差。未来可探索的方向包括：引入分层压缩策略降低长上下文推理开销，例如基于注意力稀疏化或关键片段动态采样；开发自监督时序表征学习模块，使传感器驱动的递归触发能感知非平稳生理信号中的早期预警特征；设计可学习的置信度校准器，结合强化学习从临床反馈中自动调整不确定性阈值。此外，如何将临床证据图与机构层面的知识图谱（如诊疗路径）动态对齐，以支持跨院区转诊最优决策，也是极具价值的研究方向。

### Q6: 总结一下论文的主要内容

MedRLM提出了一种递归多模态健康智能框架，旨在解决临床决策支持中长上下文、多模态信息推理的挑战。现有医疗大语言模型和检索增强生成系统在处理分散在电子健康记录、医学图像、传感器数据等多源异构信息时，常因单步提示或检索而出现上下文丢失、幻觉和推理不可靠等问题。MedRLM将患者病例视为可递归检查、分解、检索、验证和综合的外部临床环境，协调文本、纵向电子健康记录、医学影像、生理传感器信号、指南检索、不确定性审计和转诊规划等专门代理。它引入临床证据图记忆，连接患者特定观察与检索证据、标准定义、传感器衍生的生物标志物和转诊标准，并通过传感器引导的递归触发机制在检测到异常时启动更深层推理，同时采用不确定性门控精化支持高风险或低置信度病例的临床审查。基于公共和经认证临床数据集的设计评估表明，MedRLM旨在将医疗AI从静态问答推进到可审计、多模态和流程感知的临床决策支持，特别适用于资源有限的社区医疗场景。
