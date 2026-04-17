---
title: "Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems"
authors:
  - "Nishanth Madhusudhan"
  - "Vikas Yadav"
  - "Alexandre Lacoste"
date: "2026-04-16"
arxiv_id: "2604.14799"
arxiv_url: "https://arxiv.org/abs/2604.14799"
pdf_url: "https://arxiv.org/pdf/2604.14799v1"
categories:
  - "cs.CL"
  - "cs.CV"
tags:
  - "多模态智能体"
  - "评估基准"
  - "拒绝回答"
  - "视觉语言模型"
  - "多智能体系统"
  - "可靠性"
relevance_score: 7.5
---

# Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems

## 原始摘要

Effective abstention (EA), recognizing evidence insufficiency and refraining from answering, is critical for reliable multimodal systems. Yet existing evaluation paradigms for vision-language models (VLMs) and multi-agent systems (MAS) assume answerability, pushing models to always respond. Abstention has been studied in text-only settings but remains underexplored multimodally; current benchmarks either ignore unanswerability or rely on coarse methods that miss realistic failure modes. We introduce MM-AQA, a benchmark that constructs unanswerable instances from answerable ones via transformations along two axes: visual modality dependency and evidence sufficiency. Evaluating three frontier VLMs spanning closed and open-source models and two MAS architectures across 2079 samples, we find: (1) under standard prompting, VLMs rarely abstain; even simple confidence baselines outperform this setup, (2) MAS improves abstention but introduces an accuracy-abstention trade-off, (3) sequential designs match or exceed iterative variants, suggesting the bottleneck is miscalibration rather than reasoning depth, and (4) models abstain when image or text evidence is absent, but attempt reconciliation with degraded or contradictory evidence. Effective multimodal abstention requires abstention-aware training rather than better prompting or more agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态推理系统（如视觉语言模型和多智能体系统）在面临证据不足或信息不完整时，无法可靠地“拒绝回答”（即主动选择不生成答案）的问题。研究背景是，随着这些系统在医疗影像分析、法律文档审查等高风险领域部署的增加，其可靠性变得至关重要。然而，现有的评估范式（如MMMU、MM-Vet等基准测试）普遍假设所有输入实例都是可回答的，这促使模型总是尝试给出答案，而忽略了现实世界中大量存在信息模糊、缺失或矛盾的情况。现有方法的不足在于：它们要么完全忽略不可回答性，要么仅通过粗糙的方法构建不可回答样本，未能全面覆盖真实的失败模式（例如视觉依赖缺失或证据不足导致的模棱两可）。因此，本文的核心问题是：如何系统评估多模态推理系统在证据不足时能否有效识别并主动放弃回答，从而避免产生过度自信或幻觉输出，提升实际部署中的安全性与可靠性。为此，论文引入了MM-AQA基准，通过沿视觉模态依赖性和证据充分性两个轴心对可回答实例进行转化，构建不可回答样本，并评估模型在其中的表现，以揭示当前系统在校准和决策机制上的根本缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 不可回答问题范式与基准构建**：在文本领域，SQuAD 2.0通过构建对抗性不可回答问题来评估模型。本文的MM-AQA基准将这一思路扩展到多模态场景。VizWiz则通过盲人摄影师拍摄的图像引入了自然的不可回答性。在视觉问答（VQA）领域，UNK-VQA通过五种扰动类型构建不可回答问题，而MoHoBench则是对本文最直接可比的并发工作，大规模评估了多模态大模型。

**2. 选择性预测与弃答**：该领域理论工作形式化了风险与覆盖率的权衡，并将其扩展到深度网络。研究发现模型校准性差，这直接启发了本文采用的校准指标。Abstain-QA及其AUCM混淆矩阵是本文评估方法的前驱。近期研究发现，推理微调会损害弃答能力，且模型规模几乎无影响，本文实验也印证了这一点。

**3. 大语言模型的自我认知与不确定性**：研究表明，模型在识别不可回答查询方面落后于人类，但可以通过P(True)等方法进行自我评估。研究指出语言化的置信度比原始概率校准得更好，但模型总体上仍存在系统性过度自信。多数投票一致性和语义熵等方法也被探索，但通常需要微调才能可靠迁移。

**4. 可靠的VQA、多模态弃答与幻觉**：早期工作将VQA弃答定义为选择性预测。研究发现视觉模型过度自信且校准误差高。在幻觉方面，CHAIR和POPE建立了标准评估指标，HallusionBench表明前沿模型仍极易产生幻觉，而研究则表明不确定性估计可用于大规模检测幻觉，这连接了本文所针对的两种失败模式。

**5. 多智能体推理系统**：多智能体辩论研究表明，智能体间的分歧能提升事实性；研究验证了LLM作为评判者能达到超过80%的人类一致性，这为本文验证者的设计提供了核心依据。通过知识差距探测将弃答率提升了19.3%。对不遵从请求进行了分类，本文将此分类扩展到了多模态场景，并利用真实基准实例和多智能体进行评估。

**本文与这些工作的关系与区别**：本文系统地整合了上述多个方向，特别是将文本领域的弃答评估范式（如SQuAD 2.0）和选择性预测理论，首次通过系统化的轴（视觉模态依赖性和证据充分性）构建并应用于多模态基准MM-AQA。与MoHoBench等并发工作相比，本文更侧重于通过可控的变换来剖析失败模式，并深入评估了多智能体架构在弃答任务上的表现与权衡，得出了“有效的多模态弃答需要弃答感知训练，而非更好的提示或更多智能体”这一核心结论。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MM-AQA的新型基准测试，并设计一套系统的评估框架来解决多模态推理系统中的“有效弃答”问题。核心方法包括：首先，从可回答的实例出发，沿着“视觉模态依赖性”和“证据充分性”两个轴进行变换，构造出不可回答的实例，从而创建出能够精细评估模型在证据不足时是否选择弃答的基准数据集。其次，论文设计了全面的评估架构，涵盖单模态视觉语言模型和多智能体系统两种设置。在单模型设置中，模型直接处理多模态提示；在多智能体系统中，采用包含推理者、验证者和协调者三个角色的架构，并实例化为顺序（单轮）和迭代（多轮）两种交互模式，通过智能体间的协作与制衡来促进弃答决策。关键技术涉及多种实验条件的交叉测试，包括基础输出、口头置信度评分以及思维链推理，并结合了标准弃答条款和极端弃答压力条款，形成3x2的实验设计以探究不同提示策略的影响。创新点主要体现在：1) 首次系统性地在多模态领域构建了专注于评估弃答能力的基准，突破了现有评估范式默认问题皆可回答的局限；2) 引入了扩展的五分类混淆矩阵和相应的性能指标（如MCC），将“在不可回答问题上作答”作为一个独立错误类别进行量化，更精确地衡量幻觉与弃答的权衡；3) 通过实证揭示了当前前沿模型的根本瓶颈是校准错误而非推理深度不足，并发现多智能体系统虽能提升弃答但会带来准确率与弃答率的权衡，最终指出实现有效多模态弃答需要弃答感知的训练，而非仅仅改进提示或增加智能体数量。

### Q4: 论文做了哪些实验？

实验在作者构建的MM-AQA基准上进行，该基准包含2079个样本，由两个子集构成：Abstain-MMLongBench-Doc（A-MMLBD，1526个样本，源自文档问答）和Abstain-MMMU（A-MMMU，553个样本，源自STEM领域），两者均保持约1:1的可答与不可答比例。实验评估了三种前沿视觉语言模型（VLM）：GPT-5、Claude Sonnet 4.5和Qwen 2.5-32B-VL，以及两种多智能体系统（MAS）架构（顺序式和迭代式）。对比方法包括标准提示（Base）、思维链提示（CoT）和口头置信度阈值（vconf）等。主要结果如下：在标准提示下，所有VLM在不可答问题上几乎不放弃（UAC极低），例如在A-MMMU上，Sonnet 4.5的UAC仅为1.2%，GPT-5为4.9%，Qwen 2.5为4.0%，表明模型倾向于幻觉回答。引入极端放弃提示（Extreme Abstain clause）能大幅提升UAC（如Sonnet 4.5在A-MMMU上从1.2%升至41.5%），但会轻微降低可答准确率（AAC）。MAS显著改善了放弃行为，但引入了准确率与放弃率的权衡：例如在A-MMMU上，基于Claude的顺序式MAS实现了高达92.1%的UAC，但AAC降至约39%；基于GPT-5的顺序式MAS取得了更平衡的结果（AAC 59.1%，UAC 64.4%）。关键指标包括AAC（可答准确率）、UAC（不可答放弃率）、AR（总体放弃率）和最佳MCC（马修斯相关系数）。实验发现，即使最佳系统（如MAS-Seq with Claude Sonnet 4.5）的MCC也仅为0.287（A-MMMU）和0.383（A-MMLBD），与人类专家预估的MCC~0.83存在巨大差距，表明当前方法远未实现有效的多模态放弃。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于当前基准主要聚焦于STEM领域和静态图像，未涵盖更广泛的非STEM领域、视频及多文档等复杂场景。未来研究可首先扩展MM-AQA至开放域和动态多模态输入，以检验模型在更真实、多元环境下的拒答能力。其次，论文指出模型存在潜在不确定性信号但被抑制，因此需开发专门针对多模态的校准技术，如视觉语义熵估计，以提升不确定性量化的可靠性。此外，尽管多智能体架构能改善拒答，却带来准确率与拒答的权衡，这提示需探索超越现有帕累托边界的拒答感知训练方法，例如设计新的损失函数或引入强化学习来优化权衡。最后，可研究模型对证据退化或矛盾的细粒度响应机制，以增强其在模糊情境下的鲁棒决策能力。

### Q6: 总结一下论文的主要内容

该论文针对多模态推理系统中有效弃权（EA）能力不足的问题，提出了MM-AQA基准，旨在系统评估模型在证据不足时主动放弃回答的能力。核心问题是现有视觉语言模型（VLM）和多智能体系统（MAS）的评估范式通常假设问题可答，缺乏对现实场景中证据不充分情形的考量。

方法上，作者通过视觉模态依赖性和证据充分性两个维度，将可回答的实例转化为不可回答的实例，构建了包含2079个样本的基准。他们评估了三种前沿VLM（包括闭源和开源模型）和两种MAS架构。

主要结论包括：1）在标准提示下，VLM极少主动弃权，甚至简单的置信度基线方法都优于该设置；2）MAS能提升弃权能力，但引入了准确率与弃权率的权衡；3）顺序设计匹配或优于迭代变体，表明瓶颈在于模型校准而非推理深度；4）模型在图像或文本证据完全缺失时会弃权，但面对质量退化或矛盾的证据时仍会尝试回答。研究最终指出，实现有效的多模态弃权需要弃权感知的训练，而非仅依赖更好的提示或增加智能体数量。
