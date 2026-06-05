---
title: "EGTR-Review: Efficient Evidence-Grounded Scientific Peer Review Generation via Multi-Agent Teacher Distillation"
authors:
  - "Xinpeng Qiu"
  - "Wang Yihu"
  - "Zhifeng Liu"
  - "Xiaochen Wang"
  - "Jimin Wang"
date: "2026-06-04"
arxiv_id: "2606.06025"
arxiv_url: "https://arxiv.org/abs/2606.06025"
pdf_url: "https://arxiv.org/pdf/2606.06025v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent Teacher Distillation"
  - "Scientific Peer Review Generation"
  - "Evidence-Grounded Generation"
  - "Lightweight Student Model"
  - "Task-Prefix-Driven Multi-Task Learning"
relevance_score: 9.5
---

# EGTR-Review: Efficient Evidence-Grounded Scientific Peer Review Generation via Multi-Agent Teacher Distillation

## 原始摘要

Scientific peer review generation has attracted increasing attention for reducing reviewing burdens and providing timely feedback. However, existing Large Language Model (LLM)-based methods often produce generic comments with insufficient evidence support and weak source traceability, while complex multi-agent systems incur high inference costs. To address these challenges, we propose EGTR-Review, an Evidence-Grounded and Traceable Review Generation framework via Multi-Agent Teacher Distillation. EGTR-Review first constructs a multi-agent teacher that performs structure-aware paper decomposition, key-element extraction, external scholarly evidence retrieval, evidence-state labeling, verification reasoning, and review synthesis. It then distills both intermediate reasoning trajectories and final review comments into a lightweight student model through task-prefix-driven multi-task learning. An evidence-weighted objective further reduces the influence of weak, missing, or non-verifiable supervision. Experiments on public peer-review datasets show that EGTR-Review (Student) outperforms strong prompt-based, fine-tuned, and structured/agentic baselines across automatic metrics, LLM-as-Judge evaluation, and human evaluation, while maintaining strong factual grounding and source traceability with substantially lower token consumption and inference time. Our code, prompts, configurations, and sample data are available on GitHub.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学同行评审自动生成中存在的一系列关键问题。研究背景在于，随着学术投稿量的激增，评审负担加重、反馈延迟，因此自动评审生成技术变得越来越重要。现有方法主要基于大型语言模型（LLM），包括提示工程、监督微调或多智能体系统，但它们存在明显不足：首先，生成的评论往往缺乏来自论文内容或外部学术证据的支撑，导致评论泛泛而谈而非基于证据；其次，面对长而复杂的论文，评论难以追溯到具体的章节、段落或实验设置，削弱了可追溯性和针对性；最后，多智能体系统虽然提升了质量，但依赖于多轮推理和重复调用大模型，导致推理成本高昂。

针对这些挑战，本文提出的核心问题是：如何将基于证据、可追溯且具体到论文的评审能力，从一个复杂、高成本的多智能体教师模型，迁移到一个轻量级的学生模型？为此，论文提出了EGTR-Review框架，通过多智能体教师蒸馏，将证据驱动的推理过程和最终评论压缩到一个小型学生模型中，在保持高质量的同时大幅降低推理成本和耗时。

### Q2: 有哪些相关研究？

在自动同行评审生成领域，相关工作可分为三类：**1. 提示/微调方法**：如基于zero-shot或准则引导提示的通用LLM方法（常缺乏深度），以及ReviewMT和Reviewer2等基于论文-评审对进行监督微调的方法。EGTR-Review通过蒸馏证据推理轨迹，在轻量学生模型中实现了更深的论文特异性反馈。**2. 结构化/多智能体系统**：包括SWIFT²T、SEA-E、TreeReview、ScholarPeer和DeepReviewer2.0，它们通过分解评审、检索增强或可追溯封装来实现聚焦反馈。EGTR-Review与之不同之处在于，它不仅构建了多智能体教师进行证据状态标记和验证推理，还通过任务前缀驱动的多任务学习，将证据-基础推理轨迹蒸馏至轻量学生，从而降低推理成本。**3. 知识蒸馏方法**：已有工作从响应级模仿转向过程级监督（如理性蒸馏、逐步推理），以及多步/多智能体蒸馏（如QCRD、STEPER、Magdi、AgentArk、Chain-of-Agents）。EGTR-Review的独特贡献在于，它专门针对科学同行评审场景，蒸馏出包含证据状态感知的推理轨迹，并利用基于论文位置、外部学术证据和可靠性标签的证据增强输入，实现高源可追溯性。

### Q3: 论文如何解决这个问题？

EGTR-Review通过多智能体教师蒸馏框架解决科学同行评审生成中的证据不足和成本高企问题。整体框架分为教师端和学生端两部分：教师端构建多智能体协作系统，先由结构解析器进行结构感知的论文分解，将论文按章节、段落等切分为带位置索引的片段，再由关键要素提取器从每个片段中提取研究问题、方法等评审相关信息并生成检索查询。随后，证据检索器通过多源API（SerpApi、arXiv、Semantic Scholar）检索外部学术证据，并为每个片段分配五种证据状态标签（强证据支持、强证据反驳、弱元数据证据、无证据、不可验证项），这些标签指导后续推理。协调机制允许相邻智能体间进行最多两轮反馈修正。验证推理器根据证据状态执行证据感知推理：强证据检验支持或冲突，弱证据避免强判断，无证据检查论文内部有效性，非可验证项关注写作质量等。评审综合器过滤并整合推理轨迹生成最终评审。学生端采用任务前缀驱动的多任务蒸馏，以统一证据增强表示为输入，通过[推理]和[评审]两个任务前缀同时学习推理轨迹和最终评论。创新点在于：设计证据加权目标函数，根据证据状态标签分配的可靠性权重降低弱证据单元的损失贡献；通过蒸馏将多智能体的强证据支撑和可追溯性保留到轻量模型中，同时大幅减少推理时间和token消耗。推理时仅保留解析和检索模块，用学生模型替代昂贵的验证推理和综合步骤。

### Q4: 论文做了哪些实验？

论文在 PeerRead 和 OpenReview（ICLR 2017–2024）构建的基准数据集上进行实验，包含 1,386 篇论文（997 训练，60 验证，329 测试）。对比了三组基线：基于提示的（Zero-Shot LLM、Criteria-guided LLM）、监督微调的（ReviewMT-SFT、Reviewer2）和结构化/智能体的（SWIF²T、SEA-E、TreeReview），并以 GPT-5.1 为骨干。主要结果：自动评估中，EGTR-Review (学生) 在 R-L (23.60)、BERTScore (85.60)、SN-F1 (48.45) 和 ITF-IDF (5.14) 上均超越所有外部基线，优于最强基线 TreeReview（R-L 提升 0.85，BERTScore 提升 1.15）。LLM-as-Judge 评估中，学生在证据基础性（8.15）和可追溯性（8.20）上领先（均提升 7.2%）。人类评审偏好评估中，学生对 TreeReview 的整体偏好为 58.0，在证据基础性和可追溯性上优势最大（65.0 和 67.5）。此外，事实基础性评估显示学生的 FActScore 为 0.746，可追溯性准确率（TA）为 0.812。消融实验证实，证据检索与可靠性标注、任务前缀多任务学习等组件均不可或缺。效率方面，学生模型每篇论文仅消耗 105,124 个 token 和 44 秒，远低于教师模型（308,800 token，139 秒）。

### Q5: 有什么可以进一步探索的点？

EGTR-Review的局限性首先体现在领域泛化不足：当前仅评估了AI相关论文（如ML/NLP/CV），而生物医学等其他领域对实验验证、领域特定证据和安全性考量有不同评审标准，未来需要跨领域迁移和适应性微调。其次，当前框架局限于纯文本处理，未涉及多模态评审（如图表清晰度、标题信息量、视觉证据与文本的一致性），这在实际审稿中至关重要。可能的改进方向包括：1) 引入跨领域知识适配机制，如领域特定的证据检索与验证模块；2) 融合视觉语言模型，评估图表与文本的对齐度和呈现质量，生成多模态反馈；3) 探索自适应证据加权策略，根据领域难度动态调整弱/缺失证据的惩罚系数，进一步提升鲁棒性。

### Q6: 总结一下论文的主要内容

论文提出了EGTR-Review框架，解决现有基于大语言模型的科学同行评审生成方法中存在的评论缺乏证据支撑、可追溯性弱以及多智能体系统推理成本高的问题。该方法首先构建一个多智能体教师模型，执行结构感知的论文分解、关键元素提取、外部学术证据检索、证据状态标注、验证推理和评论合成；随后通过任务前缀驱动的多任务学习，将中间推理轨迹和最终评论蒸馏到轻量级学生模型中，并利用证据加权目标减少弱、缺失或不可验证监督的影响。实验结果表明，EGTR-Review（学生模型）在自动评估、LLM评判和人工评估上均优于强基线，同时显著降低令牌消耗和推理时间，保持了良好的事实依据和来源可追溯性。该工作的核心贡献在于首次将多智能体教师蒸馏应用于证据驱动的可追溯评审生成，实现了质量与效率的平衡，并明确了辅助人类评审而非替代的定位。
