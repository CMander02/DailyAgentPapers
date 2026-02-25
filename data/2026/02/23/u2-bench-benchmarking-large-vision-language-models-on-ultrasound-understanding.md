---
title: "U2-BENCH: Benchmarking Large Vision-Language Models on Ultrasound Understanding"
authors:
  - "Anjie Le"
  - "Henan Liu"
  - "Yue Wang"
  - "Zhenyu Liu"
  - "Rongkun Zhu"
  - "Taohan Weng"
  - "Jinze Yu"
  - "Boyang Wang"
  - "Yalun Wu"
  - "Kaiwen Yan"
  - "Quanlin Sun"
  - "Meirui Jiang"
  - "Jialun Pei"
  - "Siya Liu"
  - "Haoyun Zheng"
  - "Zhoujun Li"
  - "Alison Noble"
  - "Jacques Souquet"
  - "Xiaoqing Guo"
  - "Manxi Lin"
date: "2025-05-23"
arxiv_id: "2505.17779"
arxiv_url: "https://arxiv.org/abs/2505.17779"
pdf_url: "https://arxiv.org/pdf/2505.17779v4"
categories:
  - "cs.CV"
  - "cs.LG"
tags:
  - "多模态大模型"
  - "基准测试"
  - "医学影像"
  - "超声影像"
  - "视觉语言模型"
  - "模型评估"
relevance_score: 4.0
---

# U2-BENCH: Benchmarking Large Vision-Language Models on Ultrasound Understanding

## 原始摘要

Ultrasound is a widely-used imaging modality critical to global healthcare, yet its interpretation remains challenging due to its varying image quality on operators, noises, and anatomical structures. Although large vision-language models (LVLMs) have demonstrated impressive multimodal capabilities across natural and medical domains, their performance on ultrasound remains largely unexplored. We introduce U2-BENCH, the first comprehensive benchmark to evaluate LVLMs on ultrasound understanding across classification, detection, regression, and text generation tasks. U2-BENCH aggregates 7,241 cases spanning 15 anatomical regions and defines 8 clinically inspired tasks, such as diagnosis, view recognition, lesion localization, clinical value estimation, and report generation, across 50 ultrasound application scenarios. We evaluate 23 state-of-the-art LVLMs, both open- and closed-source, general-purpose and medical-specific. Our results reveal strong performance on image-level classification, but persistent challenges in spatial reasoning and clinical language generation. U2-BENCH establishes a rigorous and unified testbed to assess and accelerate LVLM research in the uniquely multimodal domain of medical ultrasound imaging.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型视觉-语言模型（LVLMs）在医学超声影像理解领域缺乏系统性评估基准的问题。超声是全球医疗中广泛使用但解读极具挑战的成像模态，其图像质量受操作者、噪声和解剖结构影响大，且需要动态空间推理和临床专业知识。尽管LVLMs在自然和医学多模态任务中展现出强大能力，但现有研究多集中于CT、MRI等静态、高分辨率影像，针对超声的复杂特性（如操作者依赖性、伪影、序列动态性）的评估几乎空白。先前超声AI研究通常基于小型、特定任务的数据集，无法全面衡量LVLM在多样化临床场景中的泛化能力。

现有方法的不足主要体现在：缺乏一个公共、平衡且全面的基准来评估LVLMs在超声领域处理分类、检测、回归和文本生成等综合任务的能力，特别是模型在空间推理和临床语言生成方面的表现尚未得到充分检验。

因此，本文的核心问题是构建首个综合性基准“U2-BENCH”，以系统评估LVLMs在超声理解上的性能。该基准聚合了7,241个病例，涵盖15个解剖区域和8类临床任务（如诊断、视图识别、病灶定位、报告生成等），共50个应用场景，旨在为LVLMs在超声这一独特多模态领域的研究提供严谨、统一的测试平台，揭示模型当前优势与局限，并推动其发展。

### Q2: 有哪些相关研究？

相关研究主要分为两大类：大型视觉-语言模型（LVLMs）和多模态基准评测。

在**大型视觉-语言模型**方面，相关工作包括通用领域模型（如GPT-4V、Claude、Gemini、DeepSeek-VL、LLaVA、Qwen-VL、MiniGPT4）和医学专用模型。通用模型在多模态任务上表现出色，但其临床可靠性研究不足。医学专用模型如MiniGPT-Med、RadFM、MedDr和Lingshu，专注于X光、CT、MRI等多种医学影像模态，但均未涵盖超声。Med-Gemini和MedGemma虽包含超声，但其能力主要局限于图像描述生成。本文与这些工作的关系在于，它首次系统性地评估了这些现有LVLMs（包括通用和医学专用模型）在超声领域的性能，填补了现有模型在超声理解方面的研究空白。

在**多模态基准评测**方面，相关工作包括通用领域基准（如MMBench、MMT-Bench、SEED-Bench）和早期医学视觉问答数据集（如VQA-RAD、VQA-Med、PathVQA）。这些基准要么缺乏临床针对性，要么并非为评估现代LVLMs而设计。最近的GMAI-MMBench是一个针对医学LVLMs的大规模基准，但其超声部分仅包含约1.4k病例，专注于6个解剖部位，任务局限于分类和分割，且不评估临床价值估计或结构化报告生成等更广泛的能力。本文提出的U2-BENCH与这些工作的区别在于，它是首个专注于超声的综合性基准，涵盖了更广泛的临床任务（8类）、解剖区域（15个）和应用场景（50个），并支持自由文本输出，旨在为超声这一独特的多模态领域提供一个严谨统一的评测平台。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为U2-BENCH的综合性基准测试来解决大型视觉-语言模型在超声理解领域性能评估不足的问题。其核心方法是设计一个系统化的评估框架，从多个维度对模型能力进行量化分析。

整体框架围绕四个核心能力展开：分类、检测、回归和文本生成。基于这四大能力，论文定义了八项临床启发式任务，具体包括：疾病诊断、切面识别与评估、病灶定位、器官检测、关键点检测、临床值估计、报告生成和描述生成。这些任务覆盖了50个超声应用场景，旨在全面模拟真实的超声诊断工作流。

主要模块和组件包括：
1.  **数据集构建管道**：从40个已授权的超声数据集中筛选出7,241个病例，涵盖15个解剖区域。构建过程分为数据收集与采样、数据清洗与格式统一、质量验证三个关键步骤。
2.  **任务特定提示设计**：为确保评估的一致性和公平性，为每个应用场景设计了结构化的提示词。提示词包含三个部分：临床角色定义（设定背景和专业性）、与标准超声工作流对齐的任务指令、以及输出格式规范（如分类选项、值范围或参考输出示例）。
3.  **评估与度量体系**：针对不同任务类型采用相应的评估指标，例如分类任务使用准确率，检测任务使用交并比（IoU），回归任务使用均方误差（MSE），文本生成任务则使用临床相关性和结构一致性等指标。

关键技术及创新点体现在：
*   **首个综合性超声理解基准**：U2-BENCH是首个专门针对超声影像多模态理解设计的全面基准，填补了该领域的空白。
*   **临床驱动与任务多样性**：八项任务均源于真实的临床需求和工作流程，并经过领域专家修正，确保了评估的实践相关性。任务设计不仅关注图像级分类，更深入挑战模型的空间推理（如病灶定位）和临床语言生成（如报告生成）能力。
*   **严谨的数据处理流程**：采用了患者级别的采样策略以防止数据泄露，并对数据进行了严格的自动化过滤和人工交叉验证（由工程师、生物医学专家和临床医生三重审核），保证了基准数据的高质量和可靠性。
*   **统一且可复现的评估平台**：通过标准化的数据格式、结构化的提示词设计和明确的评估协议，为不同模型（包括开源与闭源、通用与医学专用）提供了一个公平、可比较且可复现的测试平台。

### Q4: 论文做了哪些实验？

论文在U2-BENCH基准上对23个先进的大规模视觉语言模型（LVLM）进行了全面评估，包括开源和闭源、通用和医学专用模型。实验设置方面，研究使用了涵盖15个解剖区域、7,241个病例的数据集，定义了8个临床任务（如诊断分类DD、视图识别VRA、病变定位LL、临床价值估计CVE、报告生成RG等），共50个应用场景。评估指标与临床相关性对齐：分类任务使用准确率和F1分数；检测任务因模型输出格式问题简化为9类位置分类，使用准确率；回归任务使用RMSE、MAE和容差百分比；生成任务使用BLEU-4、ROUGE和BERTScore。此外，设计了一个综合评估指标U2-Score，通过加权各任务得分来反映模型整体超声理解能力。

主要结果如下：闭源模型整体领先，其中Dolphin-V1以0.5835的U2-Score最高，显著优于其他模型；GPT-5和Gemini-2.5-Pro-Preview分别为0.3250和0.2968。最佳开源模型DeepSeek-VL2得分为0.2630，与闭源模型仍有差距。任务难度差异显著：图像分类任务相对容易，Dolphin-V1在DD任务上准确率最高达0.682；但空间推理（如KD任务准确率均低于0.160）和文本生成（RG任务BLEU-4均低于7.5）仍具挑战；回归任务中，仅闭源Qwen-Max的CVE RMSE低至0.1248。模型缩放呈现收益递减：Qwen-2.5-VL系列从3B扩展到72B参数虽带来性能提升，但在语言生成和空间推理任务上改进有限。医学专用模型在推理任务上表现突出：如MedDr在CVE任务上RMSE为0.214，CG任务BERTScore达81.21；MedGemma-4B-it的CVE RMSE为0.167，但在视觉分类上弱于通用模型（如Qwen-72B的DD F1为0.456，高于MedDr的0.312）。这些结果揭示了LVLM在超声图像感知和临床推理方面的局限性。

### Q5: 有什么可以进一步探索的点？

该论文构建了首个超声多模态理解基准，但仍有多个方向值得深入探索。首先，基准主要评估静态图像或少量帧，而临床超声本质是动态视频流，未来可扩展至时序建模任务，如实时解剖结构追踪、动态功能评估（如心脏射血分数计算），这对模型的空间-时间推理能力提出更高要求。其次，当前任务依赖结构化提示与固定输出格式，限制了模型在开放问答、多轮临床对话等灵活场景下的表现，需开发更贴近真实医患交互的评估范式。此外，基准虽涵盖15个解剖区域，但数据分布不均衡，未来可纳入更多罕见病或跨模态数据（如结合超声与CT/MRI），以检验模型的泛化与融合能力。从技术角度看，现有LVLM在空间推理和临床语言生成上仍有不足，可探索引入医学先验知识（如解剖图谱）增强视觉定位，或采用检索增强生成技术提升报告的专业性与一致性。最后，基准尚未涉及模型决策可解释性、伦理偏差（如不同人群间的性能差异）等关键问题，这些都是未来医疗AI落地必须攻克的挑战。

### Q6: 总结一下论文的主要内容

该论文提出了首个针对超声影像理解的大规模视觉语言模型（LVLM）综合评测基准U2-BENCH。其核心问题是评估现有LVLM在超声这一关键但具挑战性的医疗影像模态上的多模态理解能力，以填补该领域系统性评估的空白。

方法上，研究团队构建了一个包含7,241个病例、覆盖15个解剖区域和50个应用场景的多样化数据集，并定义了8类临床启发式任务，包括分类、检测、回归和文本生成等。他们系统评估了23个前沿的开源与闭源、通用与医疗专用的LVLM。

主要结论显示，现有模型在图像级分类任务上表现较强，但在空间推理（如病灶定位）和临床语言生成（如报告撰写）方面仍面临持续挑战。该基准的建立为超声这一独特多模态领域的LVLM研究提供了严谨统一的测试平台，有助于加速相关模型在医疗应用中的发展与优化。
