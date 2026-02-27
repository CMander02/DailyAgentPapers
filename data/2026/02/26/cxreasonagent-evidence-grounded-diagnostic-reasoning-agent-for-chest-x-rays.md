---
title: "CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays"
authors:
  - "Hyungyung Lee"
  - "Hangyul Yoon"
  - "Edward Choi"
date: "2026-02-26"
arxiv_id: "2602.23276"
arxiv_url: "https://arxiv.org/abs/2602.23276"
pdf_url: "https://arxiv.org/pdf/2602.23276v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "医疗诊断"
  - "多模态 Agent"
  - "证据推理"
  - "基准评测"
relevance_score: 7.5
---

# CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays

## 原始摘要

Chest X-ray plays a central role in thoracic diagnosis, and its interpretation inherently requires multi-step, evidence-grounded reasoning. However, large vision-language models (LVLMs) often generate plausible responses that are not faithfully grounded in diagnostic evidence and provide limited visual evidence for verification, while also requiring costly retraining to support new diagnostic tasks, limiting their reliability and adaptability in clinical settings. To address these limitations, we present CXReasonAgent, a diagnostic agent that integrates a large language model (LLM) with clinically grounded diagnostic tools to perform evidence-grounded diagnostic reasoning using image-derived diagnostic and visual evidence. To evaluate these capabilities, we introduce CXReasonDial, a multi-turn dialogue benchmark with 1,946 dialogues across 12 diagnostic tasks, and show that CXReasonAgent produces faithfully grounded responses, enabling more reliable and verifiable diagnostic reasoning than LVLMs. These findings highlight the importance of integrating clinically grounded diagnostic tools, particularly in safety-critical clinical settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决胸部X光（CXR）诊断中，现有大型视觉-语言模型（LVLMs）在证据可靠性和可验证性方面的不足。研究背景是CXR作为胸部疾病诊断的核心影像学检查，其解读本质上是一个多步骤、基于证据的推理过程，需要识别解剖区域、获取定量测量或空间观察，并应用诊断标准。然而，现有LVLMs虽然能生成看似合理的回答，但往往未能忠实基于图像中的诊断证据，导致结论在临床实践中不可靠；同时，它们通常仅提供文本解释，缺乏直接在图像上呈现的可视化证据，使得推理过程难以验证。此外，为支持新的诊断任务，LVLMs通常需要昂贵的重新训练，限制了其适应性和临床部署效率。

现有方法的不足主要体现在三方面：一是LVLMs的响应缺乏对图像诊断证据的忠实依据，可靠性低；二是缺乏可视化证据支持，可验证性差；三是扩展新任务时需重训练，成本高且不灵活。尽管已有研究尝试通过工具增强的智能体来整合特定任务模型，但这些工具通常只提供最终诊断结论或区域级可视化，未暴露从图像证据推导结论的中间诊断步骤，因此仍无法支持可靠、可验证的证据驱动推理。

本文要解决的核心问题是：如何构建一个能够执行证据驱动诊断推理的智能体，确保其响应严格基于图像衍生的诊断证据和可视化证据，同时无需重训练即可灵活适应多种诊断任务。为此，论文提出了CXReasonAgent，它通过将大型语言模型（LLM）与临床诊断工具集成，利用工具返回的定量测量、空间观察等诊断证据及图像上的可视化证据，生成忠实基于证据的响应。为了评估这种能力，论文还引入了多轮对话基准CXReasonDial，涵盖12项诊断任务，以验证响应的证据忠实度。实验表明，该方法能产生正确接地的响应，显著提升了诊断推理的可靠性和可验证性，尤其适用于安全关键的临床环境。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要围绕大型视觉-语言模型（LVLMs）和工具增强型智能体。LVLMs（如通用多模态模型）试图直接生成诊断解释，但常产生缺乏图像证据支撑的“幻觉”响应，且难以提供可视化证据进行验证。另一类研究是工具增强型诊断智能体，它们将特定任务模型作为工具与LLM结合，以扩展任务范围而无需重新训练。然而，这些方法通常依赖直接输出最终诊断结论或区域级可视化结果的工具，未能暴露从图像证据推导出结论的**中间诊断步骤**，因此仍无法实现可靠、可验证的证据扎根推理。本文提出的CXReasonAgent与这些工作的核心区别在于，它集成的临床诊断工具能返回**图像衍生的定量测量、空间观察等诊断证据及诊断结论**，并提供将这些证据呈现在图像上的**可视化证据**，从而支持更可靠、可验证的多步推理。

在**应用类**研究中，相关工作包括将AI应用于胸部X光（CXR）分析以及其他医学影像模态（如心电图ECG）。近期ECG分析的研究表明，整合基于测量的工具可以提供定量诊断证据，这为本文实现更可靠的诊断推理提供了方向借鉴。本文则专注于CXR这一关键模态，构建了一个专门用于证据扎根诊断推理的智能体。

在**评测类**研究中，缺乏专门评估多轮、证据扎根诊断对话能力的基准。本文为此引入了**CXReasonDial基准**，它包含多轮对话和多种诊断任务，专门用于衡量响应是否基于图像证据正确扎根，这区别于以往侧重于最终诊断准确性或单轮问答的评测数据集。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CXReasonAgent的诊断智能体来解决胸部X光片诊断中大型视觉语言模型（LVLMs）存在的响应缺乏可靠证据支撑、视觉证据有限且难以适应新任务的问题。其核心方法是设计一个模块化、可解释的智能体框架，将大型语言模型（LLM）与一系列基于临床规则的诊断工具深度集成，实现基于证据的、可验证的多轮诊断推理。

整体框架分为三个主要阶段，构成了一个清晰的推理流水线。首先，在**查询解释与工具规划**阶段，智能体解析用户查询（例如询问心胸比或请求可视化标注），识别出所请求的具体诊断任务（如心脏肥大评估）和所需的证据类型（诊断证据或视觉证据），并据此规划调用相应的诊断工具。其次，在**基于临床规则的诊断工具执行**阶段，系统调用预先集成的、基于CheXStruct管道实现的诊断工具。这些工具并非基于数据驱动的黑箱模型，而是依据与放射科医生共同制定的临床标准，通过基于规则的几何计算对X光图像进行分析。对于诊断证据请求，工具输出量化的测量值、空间观察结果及其对应的诊断标准和结论；对于视觉证据请求，则输出直接在原图上标注了相关解剖区域或测量覆盖图的图像。由于采用确定性规则，证据提取过程可复现，确保了可靠性。最后，在**基于证据的响应生成**阶段，LLM严格依据上一步工具返回的图像衍生证据（而非直接访问原始图像）来生成最终的回答。这种设计使得响应完全基于可核查的证据，用户可以通过工具输出的原始证据（如测量数值或标注图）来验证回答的正确性，从而实现了可靠、连贯且可验证的多轮诊断对话。

该方法的创新点主要体现在三个方面：一是**架构设计**上，采用了“规划-执行-生成”的分离式架构，将不确定的LLM规划能力与确定性的、临床可靠的证据提取工具相结合，在利用LLM语言理解优势的同时，从根本上保证了诊断证据的准确性与可验证性。二是**工具集成**，创新性地集成了基于明确临床规则的诊断工具集（CheXStruct），覆盖了12项预定义的、证据可可靠提取的诊断任务（如心脏大小、纵隔异常、气道对齐和图像质量评估等），使智能体具备了扎实的临床基础。三是**可验证性保障**，通过强制响应生成仅基于工具返回的证据，并区分诊断证据与可视化证据请求，不仅提高了回答的忠实性（Faithful Grounding），还为用户提供了直接验证响应依据的途径，这对于安全至上的临床环境至关重要。

### Q4: 论文做了哪些实验？

论文在自建的胸部X光多轮对话基准测试CXReasonDial（包含12个诊断任务下的1,946个对话）上进行了实验。实验设置包括使用多个LLM骨干（闭源的Gemini-3-Flash、GPT-5 mini，开源的Llama 3.3-70B和Qwen3系列）构建的CXReasonAgent，并与三个大型视觉语言模型（LVLM）基线（Gemini-3-Flash、Pixtral-Large、MedGemma 27B）进行对比。评估在三种设置下进行：1）“无真实历史”（Without GT），模型基于自身输出构建对话历史；2）“有真实历史”（With GT），提供真实历史以防止错误传播；3）“动态用户模拟器”（Dynamic User Simulator），用户查询会根据模型历史响应动态生成。

评估指标分为轮次级和对话级。轮次级指标（由Gemini-3-Flash作为评判员评估）包括：诊断任务识别（DTI）、证据类型识别（ETI）、覆盖率（Cov）、忠实度（Faith）和幻觉率（Hall）。对话级指标包括平均对话成功率（Avg）和严格对话成功率（Strict）。

主要结果显示，CXReasonAgent在所有设置和指标上均显著优于LVLM基线。关键数据指标如下：在“无真实历史”设置下，CXReasonAgent（GPT-5 mini骨干）的忠实度达99.2%，幻觉率仅0.8%，平均对话成功率为96.9%，严格对话成功率为74.8%；而表现最好的LVLM基线（Pixtral-Large）忠实度为57.9%，幻觉率高达41.5%，平均对话成功率仅为48.6%。即使在最小的骨干模型（Qwen3-4B）上，CXReasonAgent的性能也全面超越所有LVLM。在动态用户模拟器设置下，CXReasonAgent（GPT-5 mini）的平均对话成功率高达98.4%，而LVLM基线最高仅为35.5%。这些结果证明了基于临床诊断工具的证据 grounding 设计的有效性，能产生更可靠、可验证的诊断推理。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其任务范围较窄，仅覆盖了胸部X光的12项诊断任务，且模态单一。未来研究可从以下几个方向深入探索：首先，**扩展任务与模态**，将代理框架推广到CT、MRI等多模态医学影像及其他专科（如眼科、皮肤科）的诊断任务中，以验证其通用性。其次，**增强证据的细粒度与可解释性**，当前依赖图像衍生的诊断证据，未来可集成更先进的视觉基础模型（如SAM）来提供像素级定位证据，使视觉依据更精准、可验证。再者，**提升对话的复杂性与动态性**，可探索在不确定场景下的主动询问机制，让代理能像医生一样动态规划检查或追问病史，从而模拟真实临床决策流程。此外，**降低工具调用成本与延迟**也是关键，需优化工具集成架构，以支持实时临床部署。最后，**加强安全性与伦理考量**，建立更严格的幻觉检测和纠错机制，确保在安全关键场景中的可靠性。这些改进将推动证据驱动的诊断智能体向更实用、可信的临床辅助系统演进。

### Q6: 总结一下论文的主要内容

该论文针对胸部X光诊断中现有大型视觉语言模型（LVLMs）存在的局限性——如生成回答缺乏可靠的诊断证据支撑、提供的视觉证据有限且难以验证，以及为适应新诊断任务需昂贵重训练——提出了一个名为CXReasonAgent的诊断智能体。其核心贡献在于设计了一种将大型语言模型（LLM）与临床诊断工具相结合的新方法，利用从图像中提取的诊断证据和视觉证据，进行基于证据的、可验证的多轮对话推理。为了系统评估这种能力，论文还构建了一个包含12项诊断任务、1946个对话的多轮对话基准CXReasonDial。实验结果表明，与LVLMs相比，CXReasonAgent能持续生成忠实于证据的回答，实现了更可靠、更连贯的多轮诊断推理。这些发现凸显了在安全关键的临床环境中，整合临床诊断工具对于实现可靠、可验证诊断推理的重要性。论文的当前工作集中于胸部X光的12项诊断任务，未来计划将智能体扩展到更广泛的诊断任务和模态。
