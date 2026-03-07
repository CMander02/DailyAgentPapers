---
title: "MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM"
authors:
  - "Wenliang Li"
  - "Rui Yan"
  - "Xu Zhang"
  - "Li Chen"
  - "Hongji Zhu"
date: "2025-09-24"
arxiv_id: "2509.20067"
arxiv_url: "https://arxiv.org/abs/2509.20067"
pdf_url: "https://arxiv.org/pdf/2509.20067v4"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Learning & Optimization"
  domain: "Healthcare & Bio"
  research_type: "New Method/Model"
attributes:
  base_model: "Llama-3.1 8B, Llama-3.1 70B, DeepSeek-R1-Distill-Llama 70B"
  key_technique: "Multi-Agent Clinical Diagnosis (MACD) framework with self-learned knowledge"
  primary_benchmark: "N/A"
---

# MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM

## 原始摘要

Large language models (LLMs) have demonstrated notable potential in medical applications, yet they face substantial challenges in handling complex real-world clinical diagnoses using conventional prompting methods. Current prompt engineering and multi-agent approaches typically optimize isolated inferences, neglecting the accumulation of reusable clinical experience. To address this, this study proposes a novel Multi-Agent Clinical Diagnosis (MACD) framework, which allows LLMs to self-learn clinical knowledge via a multi-agent pipeline that summarizes, refines, and applies diagnostic insights. It mirrors how physicians develop expertise through experience, enabling more focused and accurate diagnosis on key disease-specific cues. We further extend it to a MACD-human collaborative workflow, where multiple LLM-based diagnostician agents engage in iterative consultations, supported by an evaluator agent and human oversight for cases where agreement is not reached. Evaluated on 4,390 real-world patient cases across seven diseases using diverse open-source LLMs (Llama-3.1 8B/70B, DeepSeek-R1-Distill-Llama 70B), MACD significantly improves primary diagnostic accuracy, outperforming established clinical guidelines with gains up to 22.3% (MACD). In direct comparison with physician-only diagnosis under the same evaluation protocol, MACD achieves comparable or superior performance, with improvements up to 16%. Furthermore, the MACD-human workflow yields an 18.6% improvement over physician-only diagnosis, demonstrating the synergistic potential of human-AI collaboration. Notably, the self-learned clinical knowledge exhibits strong cross-model stability, transferability across LLMs, and capacity for model-specific personalization.This work thus presents a scalable self-learning paradigm that bridges the gap between the intrinsic knowledge of LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂真实世界临床诊断中面临的挑战。研究背景是医疗资源分布不均的全球性问题，而LLMs在医疗应用虽展现出潜力，但传统提示方法难以应对开放式的真实临床诊断场景。现有方法存在明显不足：一方面，通过扩大模型规模或进行专业后训练虽能提升性能，但计算成本高昂，难以在资源有限的基层医疗场景部署；另一方面，成本较低的提示工程策略（如思维链、少样本学习）虽然能引导模型推理，但每次诊断推理都是孤立的，无法积累和复用可重复使用的临床经验知识，这与现实中医生通过经验积累不断提升诊断能力的过程存在本质差异。

本文要解决的核心问题是：如何让LLM能够像医生一样，通过积累和复用临床经验知识来提升诊断准确性和实用性。为此，论文提出了一个新颖的多智能体临床诊断框架，通过模拟医生专业知识发展的过程，使LLM能够从历史诊断案例中自主获取、提炼并内化临床知识，形成一个可进化、可复用的自学习知识库，从而弥合LLM内在能力与复杂临床现实需求之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要包括提升大语言模型（LLM）医学能力的途径。一是通过扩大模型规模或进行医学领域的专门后训练（如医学微调），但这通常需要大量计算资源。二是采用提示工程策略，如思维链（Chain-of-Thought）和少样本（Few-Shot）提示，这些方法成本较低，旨在引导LLM的推理过程。本文提出的MACD框架与这些方法密切相关，但存在关键区别。现有的提示工程方法通常对每个诊断推理进行独立优化，未能积累和复用可重用的临床经验。MACD的核心创新在于通过多智能体管道（总结、提炼、应用）使LLM能够自我学习临床知识，模拟医生通过经验积累专业知识的过程，从而超越了传统提示工程和微调方法在孤立推理上的局限。

在**应用类**研究中，当前LLM在医疗领域的解决方案多集中于问答任务，依赖于简化场景，未能充分应对现实世界中开放式临床诊断的复杂性。MACD框架直接针对这一应用缺口，旨在处理来自真实世界的复杂患者病例，并通过MACD-人协作工作流，探索了多LLM智能体协商与人类医生监督相结合的协同诊断模式，这与以往单一的AI辅助诊断应用有所不同。

在**评测类**研究中，本文的评估基准包括权威的临床指南（如文中引用的多项专业指南）和Mayo Clinic知识，并将其作为专业知识的代表进行对比。此外，研究也与先进的闭源模型（如GPT-5）的诊断性能进行了比较。MACD框架生成的自我学习知识（SLK）在这些对比中显示出优势，不仅诊断准确率超越临床指南和GPT-5，而且在模型间展现了更好的稳定性和可迁移性，这为评估LLM的临床诊断能力提供了新的视角和基准。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MACD（多智能体临床诊断）的创新框架来解决复杂临床诊断中LLMs经验积累不足的问题。其核心方法是模拟医生通过经验积累专业知识的过程，设计了一个由三个智能体协同工作的自学习流水线。

整体框架包含三个主要模块：1）**知识总结智能体**，负责从历史病例中识别和提取关键的诊断见解；2）**知识提炼智能体**，负责将这些见解整合并结构化到一个不断演化的知识记忆中；3）**诊断智能体**，负责利用这些积累的经验来指导和改进诊断推理。这三个智能体协作，实现了从病例中“总结-提炼-应用”诊断知识的完整认知循环。

关键技术在于其**自学习知识生成机制**。与依赖外部权威知识（如机构标准或梅奥诊所知识）不同，MACD框架让LLMs直接从真实世界临床病例中蒸馏出知识。这种自学习知识更贴合实际临床场景的复杂性，并且与模型自身的推理模式具有内在一致性，从而弥合了理论知识与实际应用之间的差距。此外，框架支持**MACD-人机协同工作流**，当多个基于LLM的诊断智能体无法达成一致时，由评估智能体和人类监督介入进行迭代会诊。

创新点主要体现在：1）**可扩展的自学习范式**：使LLM能够通过多智能体协作自我积累和复用临床经验，显著提升了诊断准确性，在七种疾病上平均优于权威基线知识11.6%，最高达22.3%。2）**出色的可预测性与可迁移性**：自学习知识恢复了诊断性能的可预测性，其效果随基础模型本身能力线性增长，避免了外部知识可能带来的性能波动。同时，该知识展现出强大的跨模型稳定性，能有效提升不同架构LLM（如Qwen、DeepSeek V3.1、GPT-5）的诊断能力。3）**发现“自我偏好”现象**：每个诊断智能体使用其自身智能体团队生成的知识时性能最优，这揭示了知识生成者与消费者之间内在兼容性的重要性，类似于医生形成的个性化启发式理解。该框架作为一个“即插即用”的解决方案，在资源有限的环境中为升级诊断能力提供了一条可扩展的途径。

### Q4: 论文做了哪些实验？

论文实验设置基于提出的MACD多智能体临床诊断框架，使用三个可本地部署的开源大语言模型作为基础模型：Llama 3.1-8B-Instruct、Llama 3.1-70B-Instruct和DeepSeek-R1-Distill-Llama-3.3-70B。数据集为从MIMIC-CDM和MIMIC-IV v2.2构建的MIMIC-MACD数据集，包含4,390个真实世界患者病例，涵盖阑尾炎、胆囊炎等七种疾病，每个病例包括病史、体格检查、实验室结果和影像报告。数据集分为用于知识自学习的学习集和用于评估的测试集。

实验对比了多种方法和知识源。主要对比基准包括：1）权威外部知识基准（使用Gemini 2.5 Pro提取的机构标准专业知识和梅奥诊所知识）；2）大模型自身零知识能力；3）传统推理方法如思维链和少样本学习；4）资源密集型微调方法如LoRA；5）其他先进大模型如DeepSeek V3.1、Qwen3-235B和GPT-5。此外，还评估了MACD与人类医生协作的工作流程。

主要结果如下：首先，自学习知识显著提升了诊断准确率。相比权威基准知识，自学习知识在所有评估模型上均带来提升，平均提升11.6%（Llama-8B +10.3%， DeepSeek-70B +8.7%， Llama-70B +15.9%）。具体地，基于Llama-70B的智能体优于专业知识22.4%，优于梅奥诊所知识9.3%。其次，MACD框架显著优于现有方法范式。相比基础模型的零知识能力，MACD带来超过25%的性能增益。它显著优于思维链（例如Llama-70B上MACD 84.5% vs. CoT 57.9%）和微调（54.5%）。再者，配备MACD的模型性能超越先进大模型，例如Llama-3.1-70B+MACD（84.5%）优于DeepSeek V3.1（55.2%）、Qwen3-235B（60.5%）和GPT-5（69.6%）。MACD-人类协作工作流程相比纯医生诊断提升了18.6%。关键指标还包括自学习知识展现出良好的可预测性和跨模型可迁移性，其性能随基础模型能力线性增长，并能提升不同架构模型的性能。但研究也发现了“自我偏好”现象，即每个诊断智能体使用自身团队生成的知识时性能最优。人类专家评估也证实了自学习知识与目标疾病具有显著的临床相关性（评分多在3-4分以上）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，MACD框架目前主要针对七种疾病进行验证，其泛化能力需在更广泛的疾病谱系（如罕见病、多病共存）和临床场景（如急诊、慢性病管理）中进一步测试。其次，虽然框架强调了自学习知识的可迁移性，但不同模型架构（如纯解码器与编码器-解码器模型）对知识吸收的差异尚未深入探索，未来可研究知识表示形式的标准化以提升跨模型兼容性。

结合个人见解，可能的改进思路包括：1）引入动态知识更新机制，使自学习知识能随新病例和医学进展实时演化，避免知识僵化；2）增强多模态信息整合能力，当前框架以文本为主，未来可融合影像、实验室数据等多模态输入，模拟真实临床决策；3）探索人机协同的精细化设计，如量化人类专家在迭代会诊中的贡献度，或开发自适应协作协议以优化诊断效率。此外，框架的安全性与伦理考量（如误诊责任界定、患者隐私保护）也需在部署前系统评估。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MACD（多智能体临床诊断）的新型框架，旨在解决大语言模型在复杂真实世界临床诊断中面临的挑战。传统提示方法难以积累可重用的临床经验，而MACD通过模拟医生通过经验积累专业知识的过程，设计了一个多智能体管道，使LLMs能够自我学习临床知识。该框架包含总结、提炼和应用诊断见解的步骤，从而专注于疾病特异性关键线索，实现更精准的诊断。

方法上，MACD扩展为一个人机协作工作流，其中多个基于LLM的诊断智能体进行迭代咨询，并由一个评估智能体和人类监督支持，以处理未达成一致的病例。研究在七种疾病的4,390个真实患者病例上评估了MACD，使用了多种开源LLM（如Llama-3.1和DeepSeek-R1-Distill-Llama）。主要结论显示，MACD显著提升了主要诊断准确率，最高优于现有临床指南22.3%，并在与纯医生诊断的直接比较中达到相当或更优性能，最高提升16%。人机协作工作流进一步比纯医生诊断提升18.6%，展示了人机协同的潜力。此外，自我学习的临床知识表现出强大的跨模型稳定性、可转移性和模型特定个性化能力，为LLMs搭建了内在知识与实际应用之间的桥梁。
