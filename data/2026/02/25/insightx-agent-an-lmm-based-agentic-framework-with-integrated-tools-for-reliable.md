---
title: "InsightX Agent: An LMM-based Agentic Framework with Integrated Tools for Reliable X-ray NDT Analysis"
authors:
  - "Jiale Liu"
  - "Huan Wang"
  - "Yue Zhang"
  - "Xiaoyu Luo"
  - "Jiaxiang Hu"
  - "Zhiliang Liu"
  - "Min Xie"
date: "2025-07-20"
arxiv_id: "2507.14899"
arxiv_url: "https://arxiv.org/abs/2507.14899"
pdf_url: "https://arxiv.org/pdf/2507.14899v3"
categories:
  - "cs.AI"
  - "cs.CV"
tags:
  - "Agentic Framework"
  - "Tool Use"
  - "Multimodal Agent"
  - "Reasoning"
  - "Interpretability"
  - "Industrial Application"
relevance_score: 8.0
---

# InsightX Agent: An LMM-based Agentic Framework with Integrated Tools for Reliable X-ray NDT Analysis

## 原始摘要

Non-destructive testing (NDT), particularly X-ray inspection, is vital for industrial quality assurance, yet existing deep-learning-based approaches often lack interactivity, interpretability, and the capacity for critical self-assessment, limiting their reliability and operator trust. To address these shortcomings, this paper proposes InsightX Agent, a novel LMM-based agentic framework designed to deliver reliable, interpretable, and interactive X-ray NDT analysis. Unlike typical sequential pipelines, InsightX Agent positions a Large Multimodal Model (LMM) as a central orchestrator, coordinating between the Sparse Deformable Multi-Scale Detector (SDMSD) and the Evidence-Grounded Reflection (EGR) tool. The SDMSD generates dense defect region proposals from multi-scale feature maps and sparsifies them through Non-Maximum Suppression (NMS), optimizing detection of small, dense targets in X-ray images while maintaining computational efficiency. The EGR tool guides the LMM agent through a chain-of-thought-inspired review process, incorporating context assessment, individual defect analysis, false positive elimination, confidence recalibration and quality assurance to validate and refine the SDMSD's initial proposals. By strategically employing and intelligently using tools, InsightX Agent moves beyond passive data processing to active reasoning, enhancing diagnostic reliability and providing interpretations that integrate diverse information sources. Experimental evaluations on the GDXray+ dataset demonstrate that InsightX Agent not only achieves a high object detection F1-score of 96.54\% but also offers significantly improved interpretability and trustworthiness in its analyses, highlighting the transformative potential of LMM-based agentic frameworks for industrial inspection tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工业X射线无损检测（NDT）中现有AI系统存在的交互性差、可解释性不足以及缺乏关键性自我评估能力的问题，从而提升诊断的可靠性和操作人员的信任度。研究背景是，X射线检测对于航空航天、制造等行业的内部缺陷检测至关重要，传统依赖人工判读的方式存在主观性强、效率低的问题。近年来，基于深度学习的自动化方法（如CNN、Transformer）虽能实现高精度检测，但大多为“黑盒”系统，仅输出检测框和置信度，缺乏对决策原因的解释，且无法与操作人员进行交互式对话，难以融入复杂的决策流程。

现有方法的不足主要体现在两方面：一是传统深度学习检测器缺乏透明度和交互能力；二是近期虽有研究探索将大型多模态模型（LMM）直接用于异常检测，但若将其作为独立的视觉定位工具，需要大量像素级标注数据，成本高昂，且容易产生“幻觉”输出，定位精度难以满足工业要求。若仅将LMM用作被动的后端分析器，又无法批判性地审视上游检测结果，可靠性有限。

因此，本文的核心问题是：如何构建一个既具备高精度缺陷检测能力，又能提供可解释、可交互分析，并能主动进行推理和自我验证的NDT系统。为此，论文提出了InsightX Agent框架，其创新在于将LMM定位为中央协调器，而非简单的检测器或分析模块。该框架让LMM智能地协调两个专用工具：用于高效、精准定位缺陷的稀疏可变形多尺度检测器（SDMSD），以及引导LMM对初始检测结果进行证据驱动的反思、验证和优化的EGR工具。通过这种智能体架构，系统实现了从被动数据处理到主动工具驱动推理的范式转变，在保证高检测精度的同时，显著提升了结果的可解释性和可信度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统及深度学习方法、基于大语言/多模态模型（LLM/LMM）的检测方法，以及新兴的智能体（Agent）框架。

在传统及深度学习方法方面，已有大量工作致力于X射线无损检测的自动化。例如，Xu等人使用改进的U-Net进行分割，Shen等人提出双流CNN架构处理增强图像，Zhang等人则通过改进特征金字塔网络（FPN）来提升检测性能。此外，Wang等人引入了自注意力机制以识别复杂背景下的细微缺陷，而Intxausti等人和Wen等人则分别利用自监督预训练和领域自适应技术应对工业场景中标注数据稀缺的挑战。这些方法在检测精度上取得了进展，但普遍缺乏可解释性和交互能力，被视为“黑箱”系统。

近年来，研究者开始探索将LMMs应用于异常检测，以增强系统的解释和对话能力。例如，Gu等人提出的AnomalyGPT通过微调LMM在异常检测数据集上取得了优异性能；Cao等人和Zhang等人则分别探索了GPT-4V在多模态零样本异常检测和视觉问答（VQA）范式下的潜力。这些研究为将对话式AI融入工业检测奠定了基础，但它们通常将LMM作为被动的终端分析器，在需要高精度定位的工业场景中可能面临幻觉问题或难以批判性审视上游检测结果。

本文提出的InsightX Agent框架与上述工作均不同。它并非简单地将LMM用作直接定位或分析的工具，而是将其定位为一个**中心协调者（Orchestrator）**，主动规划和调用两个专用工具（SDMSD检测器和EGR反思工具）来完成分析任务。这属于新兴的**基于LMM的智能体框架**范畴。与“标准DL检测器”相比，本框架增加了主动推理和解释能力；与“LMM直接定位”方法相比，本框架通过专用工具保证高精度检测，避免了像素级标注数据需求和幻觉风险；与一般的“LMM工作流”相比，本框架通过结构化的EGR机制实现了对检测结果的批判性验证与优化，从而在保持高检测性能的同时，显著提升了系统的可靠性、可解释性和交互性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为InsightX Agent的新型LMM（大型多模态模型）驱动的智能体框架来解决X射线无损检测中交互性、可解释性和自我评估能力不足的问题。其核心方法是让LMM作为中央协调器，战略性地调用和整合两个专门工具：用于缺陷检测的SDMSD（稀疏可变形多尺度检测器）和用于验证与反思的EGR（证据驱动的反思）工具，从而将被动数据处理转变为主动推理。

整体框架以LMM智能体为核心。给定X射线图像和用户查询后，LMM首先进行隐式意图识别，决定分析路径。对于缺陷识别任务，系统依次调用SDMSD和EGR工具。SDMSD负责生成精确的缺陷定位假设，而EGR则对这些假设进行系统性验证和修正。

主要模块与关键技术包括：
1.  **LMM智能体核心的领域适应**：采用LoRA（低秩适应）对预训练LMM进行高效领域微调，避免灾难性遗忘。训练采用两阶段课程：第一阶段使用构建的NDT知识语料库（包含1000个问答对）注入领域知识；第二阶段通过模板驱动的对齐机制，让LMM学习遵循“检测-证据-评估-建议”的结构化分析范式，确保输出可靠、可量化评估。
2.  **SDMSD检测器**：其创新点在于结合了密集提案生成与稀疏化处理。首先生成密集的多尺度缺陷区域提案以确保高召回率，然后通过非极大值抑制（NMS）进行稀疏化，得到高质量的候选集。最后，这些稀疏提案通过一个采用可变形注意力机制的Transformer编码器-解码器进行高效处理，特别优化了对X射线图像中常见的小而密集目标的检测。
3.  **EGR验证工具**：这是框架的关键创新点，它引导LMM执行一个受思维链启发的、结构化的六阶段审查流程：上下文评估、个体缺陷分析、误报消除、置信度重新校准和质量保证。在个体缺陷分析中，EGR对每个提案进行视觉验证、边界框质量评估（如紧密度、覆盖率）和真实性判断。它不仅能过滤误报、校准置信度，还能提出边界框修正建议，从而系统性地验证和优化SDMSD的初始输出。

总之，InsightX Agent通过其“LMM协调器 + 专用工具”的架构，将强大的通用推理能力、专业的缺陷检测算法和严格的证据审查流程相结合，实现了可靠、可解释、交互式的分析，超越了传统的顺序式深度学习流水线。

### Q4: 论文做了哪些实验？

论文在GDXray+射线成像集合的铸件检测子集上进行了实验验证。该数据集专注于工业铝铸件（如车轮、转向节）的自动缺陷检测，包含67个独立序列。通过预处理移除无标签或样本过少的序列后，采用序列内划分策略，将每个序列的图像随机分为80%训练集和20%测试集，最终形成571张训练图像和143张测试图像，以避免数据泄露并模拟真实工业检测场景。评估指标采用目标检测任务中常见的精确率、召回率和F1分数，并设定IoU阈值为0.5。此外，根据边界框像素面积将缺陷分为小（面积<32²像素）、中（32²≤面积<96²像素）和大（面积≥96²像素）三组进行分析。

实验对比了不同配置的InsightX Agent框架。主要结果如下：完整框架（SDMSD + EGR）在测试集上达到了96.54%的F1分数，精确率为96.55%，召回率为96.53%。在消融研究中，仅使用基础LMM（无工具）的F1分数为91.23%；仅添加SDMSD检测器后，F1分数提升至94.67%；而结合SDMSD与EGR工具后，性能进一步提升至96.54%。这表明EGR工具通过反思链过程有效优化了检测结果。在不同尺寸缺陷的检测上，完整框架对小、中、大缺陷的F1分数分别达到95.01%、97.12%和97.49%，显示出其多尺度检测能力。实验在单张NVIDIA A10 GPU（24GB显存）上完成，使用PyTorch框架，并以Qwen2.5-VL（70亿参数）作为基础LMM进行微调。

### Q5: 有什么可以进一步探索的点？

该论文在实验验证上主要基于GDXray+数据集的铸造检测子集，这虽然具有针对性，但也构成了其局限性。未来研究可以进一步探索以下几个方向：首先，**框架的通用性与可扩展性**。当前工作聚焦于X射线铸造缺陷检测，未来可验证其在其他NDT模态（如超声波、热成像）或更广泛的工业视觉任务中的表现，并研究如何模块化地适配新的专业工具。其次，**对LMM智能体能力的深度挖掘**。论文中LMM主要作为协调者，其主动推理和规划能力尚有提升空间。未来可以探索让LMM自主决定何时调用、以何种顺序调用工具，甚至基于任务复杂度动态调整EGR反思链的深度，实现更自适应的问题求解。再者，**提升效率与实时性**。尽管SDMSD考虑了计算效率，但整合LMM和多次反思的端到端框架在实时工业检测中可能面临延迟挑战。未来可研究模型轻量化、推理加速以及更高效的反思机制。最后，**增强解释性与人机协作**。目前的解释性输出主要服务于验证，未来可设计更结构化、可交互的解释报告，并研究如何将智能体的不确定性估计和决策依据更好地传递给操作员，以建立更深层次的信任，实现真正的人机协同分析。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为InsightX Agent的新型智能体框架，旨在解决X射线无损检测（NDT）中现有深度学习方法交互性差、可解释性不足以及缺乏关键自我评估能力的问题。其核心贡献是构建了一个以大型多模态模型（LMM）为中心协调器的智能体框架，通过集成和协同两个专用工具——稀疏可变形多尺度检测器（SDMSD）与证据驱动的反思（EGR）工具——来实现可靠、可解释的交互式分析。

方法上，SDMSD负责从多尺度特征图中生成密集的缺陷区域建议，并通过非极大值抑制进行稀疏化，以高效检测X射线图像中的小型密集目标。EGR工具则引导LMM智能体进行链式思维驱动的审查流程，包括上下文评估、个体缺陷分析、误报消除、置信度重新校准和质量保证，从而验证和优化SDMSD的初始检测结果。这种设计使系统从被动数据处理转向主动推理。

实验在GDXray+数据集上进行，结果表明InsightX Agent不仅取得了96.54%的高目标检测F1分数，更重要的是显著提升了分析的可解释性和可信度。论文的结论强调了基于LMM的智能体框架在提升工业检测任务的诊断可靠性和操作者信任方面具有变革性潜力。
