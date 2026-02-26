---
title: "Med-REFL: Medical Reasoning Enhancement via Self-Corrected Fine-grained Reflection"
authors:
  - "Zongxian Yang"
  - "Jiayu Qian"
  - "Zegao Peng"
  - "Haoyu Zhang"
  - "Yu-An Huang"
  - "KC Tan"
  - "Zhi-An Huang"
date: "2025-06-11"
arxiv_id: "2506.13793"
arxiv_url: "https://arxiv.org/abs/2506.13793"
pdf_url: "https://arxiv.org/pdf/2506.13793v4"
categories:
  - "cs.AI"
tags:
  - "Agent Reasoning"
  - "Self-Correction"
  - "Tree-of-Thoughts"
  - "Medical AI"
  - "Reasoning Enhancement"
  - "Preference Optimization"
  - "High-Stakes Applications"
relevance_score: 7.5
---

# Med-REFL: Medical Reasoning Enhancement via Self-Corrected Fine-grained Reflection

## 原始摘要

Large reasoning models excel in domains like mathematics where intermediate reasoning is straightforward to verify, but struggle to self-correct in medicine fields where evaluating intermediate reasoning is cumbersome and expensive. This verification bottleneck hinders the development of reliable AI reasoners for high-stakes application. Here we propose Med-REFL, a novel framework that learns fine-grained reflection without human labels or model distillation. Med-REFL introduces a deterministic structural assessment of the reasoning space to automatically generate preference data for reflection. By globally evaluating all explored reasoning paths in a tree-of-thoughts, our method quantifies the value of corrective actions, enabling the automated construction of direct preference optimization pairs. This trains the model to recognize and amend its own reasoning fallacies. Extensive experiments show Med-REFL delivers robust gains across diverse models architectures and medical benchmarks, boosting a general-purpose Llama3.1-8B by +5.82% and the state-of-the-art Huatuo-o1 by +4.13% on the MedQA benchmark. Our Med-REFL-8B achieves state-of-the-art performance among 7-8B models while even competing with models twice its size. Crucially, targeted ablations prove its success generalizes to other domains such as logical reasoning and mitigates the `fake reflection' phenomenon in LRMs. Ultimately, our framework provides a scalable solution to the verification bottleneck, paving the way for more reliable AI reasoners in high-stakes domains like medicine. Med-REFL has been made publicly available in https://github.com/TianYin123/Med-REFL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型推理模型在医学等高风险领域难以进行有效自我反思和修正的问题。研究背景是，尽管大型推理模型在数学、代码等验证成本低的领域能通过工具（如计算器、编译器）获得即时反馈并实现自我修正，但在医学领域，由于缺乏廉价、自动化的验证工具，中间推理步骤的评估依赖昂贵的人工专家或非结构化数据库查询，形成了“验证瓶颈”，阻碍了可靠AI推理器的发展。

现有方法存在明显不足。主要分为两类：第一类是基于结果的方法，如使用蒸馏思维链进行监督微调或基于结果的强化学习。这类方法仅依赖最终答案作为信号，容易让模型学习到偶然得出正确答案的错误逻辑，或陷入奖励欺骗。第二类是基于过程奖励模型的方法，虽能提供更细粒度的步骤反馈，但需要训练独立且要求高的奖励模型，流程复杂，且其核心是奖励最正确的路径，而非教会模型如何从自身多样错误中进行反思和恢复。

因此，本文要解决的核心问题是：如何在不依赖人工标注、教师模型蒸馏或复杂过程奖励模型的前提下，设计一个资源高效的框架，使模型能够自动学习细粒度的自我反思能力，从而克服医学领域的验证瓶颈，提升推理的鲁棒性和可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，现有工作主要围绕如何提升大型推理模型在医学领域的性能。第一类范式依赖于从昂贵教师模型蒸馏的长思维链进行监督微调，或基于结果的强化学习。这类方法以结果为导向，仅依赖最终答案作为信号，容易学习到有缺陷但巧合正确的逻辑，或遭遇奖励破解问题。第二类范式利用过程奖励模型提供逐步反馈，但需要训练独立的奖励模型，流程复杂，且主要奖励最正确路径，未能有效教导模型如何从自身多样错误中反思和恢复。本文提出的Med-REFL框架与这些方法不同，它通过确定性结构评估推理空间，自动生成细粒度反思数据，无需人工标注、模型蒸馏或单独的过程奖励模型，直接优化模型自我纠正能力。

在应用类研究中，已有工作如Huatuo-o1、MedReason、AlphaMed等专门针对医学领域开发模型。这些模型或在特定能力（如反思）上有局限，或依赖外部专家知识、检索增强生成等技术。Med-REFL则专注于增强医学推理中的反思能力，其框架设计为专家无关、PRM无关且RAG无关，提供了更通用和可扩展的解决方案。

在评测方面，相关研究通常使用MedQA-USMLE等标准医学基准进行评估。本文不仅在这些分布内数据集上验证性能，还测试了在GPQA等分布外数据集以及逻辑推理任务上的泛化能力，证明了其方法的鲁棒性和广泛适用性。

### Q3: 论文如何解决这个问题？

Med-REFL 通过一个无需人工标注或模型蒸馏的四阶段框架，自动学习细粒度的自我反思能力，以解决医学等领域中因中间推理步骤难以验证而阻碍模型自我修正的瓶颈问题。

其核心架构与流程如下：
1.  **多样化推理轨迹生成**：采用思维树（ToT）方法，为每个医学问题生成多样化的链式推理（CoT）轨迹。每个节点代表一个中间推理状态，从根到叶的路径构成一条完整的推理轨迹。
2.  **基于结构的确定性评估**：设计了一套量化评估指标，用于评价任何中间步骤或反思行动的质量。关键指标包括：
    *   **步骤质量**：基于以某步骤为根的子树上正确与错误路径的数量比例计算。
    *   **解决方案质量**：整条推理路径上所有步骤质量的平均值。
    *   **剩余质量**：从某个中间步骤到路径终点的部分轨迹的步骤质量平均值。
    *   **行动价值**：综合评估从一个节点通过某个反思行动转移到另一个节点所带来的步骤质量、解决方案质量和剩余质量的变化，用以量化反思行动的价值。
3.  **自动构建偏好数据对**：利用上述评估指标，自动构建两种类型的直接偏好优化（DPO）数据对：
    *   **反思学习对**：模拟模型在推理中或推理后进行检查和修正的场景。首先使用“错误定位器”识别轨迹中的第一个错误步骤，然后使用“反思器”生成解释错误并转向正确步骤的反思文本。通过探索替代推理分支并计算行动价值，筛选出有效的反思轨迹（被选）和无效的反思轨迹（被拒），形成对比数据对。
    *   **推理增强对**：为保持广泛的推理能力，补充构建通用推理偏好对。通过比较高质量的正确推理轨迹与看似合理但最终错误的轨迹，形成另一组数据对。
4.  **模型微调**：使用构建好的DPO数据集对大型语言模型进行微调，训练模型优先选择有效的反思和推理模式，从而内化强大的自我纠错能力。

该方法的创新点在于：
*   **无监督的细粒度反思学习**：完全避免了昂贵的人工标注或模型蒸馏，通过结构化的自动评估生成训练数据。
*   **全局推理空间评估**：不同于仅关注最终答案，该方法在思维树的全局空间中量化每个步骤和每个反思行动的价值，实现了对中间推理过程的精细评估。
*   **双类型数据构建**：同时针对“反思行为本身”和“基础推理能力”构建偏好数据，确保模型既学会在出错时修正，也提升了生成高质量初始推理的能力。
*   **可扩展性与泛化性**：框架不依赖于特定领域知识，实验证明其能有效提升不同架构模型在多个医学基准上的性能，并能泛化至逻辑推理等领域，缓解“虚假反思”现象。

### Q4: 论文做了哪些实验？

论文在多个医学基准上进行了广泛的实验，以评估Med-REFL框架的有效性和泛化能力。实验设置方面，主要使用MedQA-USMLE（5选项）作为开发和评估的主要数据集，并在多个其他医学基准上进行测试，包括MedMCQA、PubMedQA、GPQA医学子集（GPQA-M）、MMLU-Pro医学子集（MMLU-Pro(M)）以及专家级基准MedXpertQA（分为理解MedXpert-U和推理MedXpert-R两部分）。评估模型涵盖了六种7B-8B参数的基线模型，分为三类：指令微调模型（Llama3.1-8B和Qwen2.5-7B）、推理重型模型（Huatuo-o1-8B和DeepSeek-Distill-8B）和知识重型模型（MedReason-8B和UltraMedical3.1-8B），同时还测试了完全使用GRPO训练的AlphaMed模型。所有结果均为三次独立运行的平均值以确保稳定性。

对比方法方面，论文将Med-REFL应用于不同基线模型，并与原始模型性能进行对比。主要结果显示，Med-REFL在所有测试模型和基准上均带来了显著且一致的性能提升。关键数据指标包括：在MedQA基准上，通用模型Llama3.1-8B提升了+5.82%，最先进的Huatuo-o1-8B提升了+4.13%；在OoD挑战中，Huatuo-o1-8B平均提升+3.59%。在需要深度多步推理的数据集上提升尤为明显，例如GPQA（Med+）平均增益+3.89%，MMLU-Pro（Med+）平均增益+2.37%。此外，Med-REFL-8B模型（基于Huatuo-o1训练）在7-8B模型中达到了最先进的性能，甚至可与两倍大小的模型竞争。分析还表明，Med-REFL导致模型生成了更长、更详细的推理轨迹，这与性能增益结构相关，并且框架在检索导向任务（如PubMedQA）上的增益相对较小，这符合预期，进一步验证了其核心贡献在于提升推理过程质量。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，Med-REFL 依赖树状思维（ToT）探索来生成偏好数据，这可能导致计算开销较大，且探索空间的覆盖度有限，未来可研究更高效的采样策略或动态剪枝方法，以平衡性能与成本。其次，框架中“思考转换器”（Thinker）模块的性能严格依赖于模型规模，这表明小模型在语言化结构化路径时存在信息损失，未来可探索通过知识蒸馏或模块化训练提升小模型在该任务上的能力。此外，论文发现训练独立的奖励模型（RM）在训练阶段并未带来增益，这提示我们当前的结构化评估已接近最优，但如何将 RM 在推理阶段的优势更有效地融入训练过程，仍值得深入探索，例如研究迭代式训练或课程学习策略。最后，尽管论文在医学和逻辑推理领域验证了有效性，但在其他高风险领域（如法律、金融）的泛化能力尚未充分检验，未来可扩展至更多需要细粒度反思的复杂决策场景，并进一步探究模型反思能力的可解释性，以增强其在实际应用中的可信度。

### Q6: 总结一下论文的主要内容

该论文提出了Med-REFL框架，旨在解决医学等高风险领域中大语言模型自我修正的验证瓶颈问题。核心贡献在于无需人工标注或模型蒸馏，通过确定性结构评估自动生成细粒度反思所需的偏好数据。方法上，它利用思维树结构全局评估所有推理路径，量化纠正动作的价值，从而构建直接偏好优化对来训练模型识别并修正自身推理错误。实验表明，Med-REFL能显著提升不同模型在医学基准上的性能，例如将Llama3.1-8B在MedQA上提升5.82%，并使8B参数模型达到同类最佳水平。主要结论是，该方法能有效内化真实的自我修正能力，其原理可推广至逻辑推理等其他领域，为高风险应用开发可靠AI推理器提供了可扩展的解决方案。
