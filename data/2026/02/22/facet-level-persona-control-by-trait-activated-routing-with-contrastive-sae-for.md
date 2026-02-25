---
title: "Facet-Level Persona Control by Trait-Activated Routing with Contrastive SAE for Role-Playing LLMs"
authors:
  - "Wenqiu Tang"
  - "Zhen Wan"
  - "Takahiro Komamizu"
  - "Ichiro Ide"
date: "2026-02-22"
arxiv_id: "2602.19157"
arxiv_url: "https://arxiv.org/abs/2602.19157"
pdf_url: "https://arxiv.org/pdf/2602.19157v1"
categories:
  - "cs.CL"
tags:
  - "角色扮演智能体"
  - "人格控制"
  - "稀疏自编码器"
  - "可解释性"
  - "大五人格模型"
  - "对比学习"
  - "激活路由"
  - "对话一致性"
relevance_score: 8.0
---

# Facet-Level Persona Control by Trait-Activated Routing with Contrastive SAE for Role-Playing LLMs

## 原始摘要

Personality control in Role-Playing Agents (RPAs) is commonly achieved via training-free methods that inject persona descriptions and memory through prompts or retrieval-augmented generation, or via supervised fine-tuning (SFT) on persona-specific corpora. While SFT can be effective, it requires persona-labeled data and retraining for new roles, limiting flexibility. In contrast, prompt- and RAG-based signals are easy to apply but can be diluted in long dialogues, leading to drifting and sometimes inconsistent persona behavior. To address this, we propose a contrastive Sparse AutoEncoder (SAE) framework that learns facet-level personality control vectors aligned with the Big Five 30-facet model. A new 15,000-sample leakage-controlled corpus is constructed to provide balanced supervision for each facet. The learned vectors are integrated into the model's residual space and dynamically selected by a trait-activated routing module, enabling precise and interpretable personality steering. Experiments on Large Language Models (LLMs) show that the proposed method maintains stable character fidelity and output quality across contextualized settings, outperforming Contrastive Activation Addition (CAA) and prompt-only baselines. The combined SAE+Prompt configuration achieves the best overall performance, confirming that contrastively trained latent vectors can enhance persona control while preserving dialogue coherence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决角色扮演智能体（RPA）中人格控制的难题。现有方法主要分为无需训练的方法（如通过提示词或检索增强生成注入人格描述）和基于监督微调（SFT）的方法。前者在长对话中容易导致人格信号被稀释、行为漂移或不一致；后者虽有效，但需要特定人格标注数据且为每个新角色重新训练，缺乏灵活性。论文的核心目标是实现一种轻量级、可解释且能在推理时进行控制的方法，以在长上下文中稳定、精确地操控LLM的人格表现，同时避免重训练的成本与灾难性遗忘。为此，作者提出了一个基于对比学习稀疏自编码器（SAE）的框架，学习与大五人格30个维度对齐的细粒度控制向量，并通过特质激活路由模块动态选择，从而提升人格控制的稳定性、可控性和可解释性。

### Q2: 有哪些相关研究？

相关研究主要分为两类：训练时控制与推理时控制。本文聚焦于推理时控制方法，因其在效果与实用性间取得了良好平衡。具体而言，相关工作包括：

1.  **解码时控制方法**：如Plug-and-Play Language Models (PPLM)，通过调整解码过程来引导生成。但其计算开销大、对超参数敏感，且可能损害文本流畅度。
2.  **推理时控制向量方法**：此类方法轻量、可组合，无需修改预训练参数。主要包含两种生成控制向量的技术：
    *   **基于稀疏自编码器的方法**：训练SAE以获得解耦的特征空间，然后通过对比正负样本来计算控制向量。
    *   **基于对比激活加法的方法**：直接计算表达相反属性的一对提示词对应的平均激活差异，从而得到控制向量。该方法简单无需参数，但不同特质对应的向量方向可能存在重叠，导致跨特质干扰。

本文提出的方法与上述工作的关系在于：它同样属于推理时控制向量方法，但进行了关键改进。不同于先前使用通用模板的SAE/CAA流程，本文构建了专业的、防泄漏的30维度（Big Five模型）语料库进行监督；在SAE空间中引入对比学习以更好地对齐和分离不同维度的方向；并设计了一个基于情境线索动态选择和调度向量的智能体路由策略，而非一次性注入所有维度向量，从而实现了更精确、可解释的人格层面控制。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段框架解决角色扮演智能体（RPA）中人格控制的稳定性和灵活性问题。核心方法结合了对比学习稀疏自编码器（Contrastive SAE）和基于智能体的决策模块，实现了细粒度、可解释且动态的人格向量注入。

**核心方法与架构设计：**
1.  **对比学习稀疏自编码器（Contrastive SAE）训练**：首先，在通用语料（如WikiText-103）上预训练一个SAE，将模型隐藏状态映射到稀疏潜在空间。然后，利用新构建的、包含大五人格30个维度的平衡语料库，学习与特定人格面相（facet）对齐的控制向量（CV）。关键创新在于引入了对比学习损失函数（公式3），该总损失由三部分组成：原型对比损失（ℒ_CE）、正样本拉近损失（ℒ_dist）和正则化项。ℒ_CE借鉴了ArcFace/CosFace思想，通过引入角度间隔和余弦间隔，强制使注入CV后的表征靠近正类原型中心并远离负类原型中心（公式6-8）。ℒ_dist则直接最小化注入后表征与正类中心的距离（公式9）。这种对比训练确保了学得的CV在潜在空间中具有强区分性和明确的控制方向。

2.  **基于智能体的决策模块（动态路由）**：为了解决多个人格向量可能相互竞争或与上下文无关的问题，论文引入了基于特质激活理论的动态路由机制。在推理时，并不注入所有CV，而是利用角色扮演模型自身的基座LLM作为一个路由智能体。该智能体分析当前用户的查询，推断出问题最强烈地提示了哪个人格面相（例如，写作建议提示“开放性”而非“外向性”）。然后，系统仅注入与这些最相关面相对应的CV。这样，人格知识仍通过提示或检索增强生成（RAG）提供，而学得的CV则充当“放大器”，根据上下文线索进行精准、有针对性的行为微调。

**关键技术：**
- **稀疏潜在空间中的控制向量**：CV在SAE的稀疏潜在空间中定义和优化（公式2），通过掩码（m）仅激活与目标人格面相最相关的少数维度，增强了控制的针对性和可解释性。
- **残差空间注入**：训练完成后，将学得的潜在代码z解码回模型的残差空间得到v，并通过公式1将其加到隐藏状态h(x)中，其中α控制注入强度。这是一种无需重新训练模型的参数高效微调方法。
- **对比学习增强的CV训练**：通过结合间隔化的对比损失和距离损失，显著提升了CV在拉近/推远不同人格表征方面的效能和强度，使其在长对话中也能保持稳定的控制力。

综上，该方法通过对比SAE学习到强区分性的人格控制向量，再通过智能体路由实现动态、上下文感知的向量选择与注入，从而在保持对话连贯性的同时，实现了精确、稳定且灵活的人格层面控制。

### Q4: 论文做了哪些实验？

实验在Qwen3-4B和Mistral-7B两个模型上进行，评估了角色扮演智能体（RPA）的人格控制性能。基准测试基于大五人格模型，使用了44个抽象问题和改写后的情境化问题。评估指标包括全准确率（FA）、均方误差（MSE）、平均绝对误差（MAE）和多轮对话率（MTR）。

实验比较了多种方法：Base RPA（无干预）、Prompt-Label（提示词控制）、CV-CAA（对比激活加法）、CV-SAE（提出的对比稀疏自编码器方法）以及它们与提示词结合的混合方法。主要结果显示，CV-SAE在人格准确性和输出稳定性上优于CV-CAA和纯提示方法。特别是在情境化问题上，CV-SAE表现稳健。混合方法CV-SAE+Prompt取得了最佳整体性能，在Qwen3-4B和Mistral-7B上，对于情境化问题的FA分别达到88.5%。此外，实验还分析了控制强度α的影响，发现CV-SAE在中等α值时能在高准确率和低MTR之间取得更好平衡。消融研究证实了对比学习（CL）对于提升表征对齐和准确率的必要性。

### Q5: 有什么可以进一步探索的点？

本文提出的基于对比稀疏自编码器（SAE）的人格控制方法虽在细粒度人格操控上取得进展，但仍存在局限。首先，方法依赖精心构建的平衡语料库（15,000样本），其构建成本高，且人格模型（大五人格30个维度）的覆盖度和文化普适性有待验证。其次，特质激活路由模块的动态选择机制在极端复杂或冲突人格组合场景下的鲁棒性尚未充分测试。最后，方法主要在中层残差进行干预，对更深层或更浅层模型结构的泛化能力需进一步探索。

未来方向包括：1）扩展人格模型与语料，纳入更动态、跨文化的人格特质，并探索少样本或无监督的语料构建方法以降低依赖；2）研究更自适应、可解释的路由机制，以处理多特质冲突与长程对话中的动态人格演化；3）将框架推广至更大规模模型（如千亿参数）及多模态角色扮演场景，验证其扩展性；4）探索与人类反馈强化学习（RLHF）或直接偏好优化（DPO）的结合，以对齐人格控制与主观对话质量。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种用于角色扮演大语言模型（RPAs）的细粒度人格控制方法，核心贡献在于引入了基于对比学习的稀疏自编码器（SAE）框架来学习与“大五”人格30个维度对齐的“人格控制向量”。为解决现有方法（如提示工程或监督微调）在长对话中人格易漂移、不一致或缺乏灵活性的问题，作者构建了一个包含1.5万个样本、经过泄漏控制的语料库，为每个细粒度人格维度提供平衡的监督信号。学习到的向量被注入模型的残差空间，并通过一个“特质激活路由”模块进行动态选择，从而实现对人格特质的精确、可解释的引导。实验表明，该方法在保持对话连贯性的同时，显著提升了角色扮演的稳定性和忠实度，其“SAE+提示”的组合配置性能优于现有的对比激活添加（CAA）和纯提示基线。这项工作的意义在于为可控角色扮演智能体提供了一种无需为每个新角色重新训练、且能实现深层、稳定人格控制的通用解决方案。
