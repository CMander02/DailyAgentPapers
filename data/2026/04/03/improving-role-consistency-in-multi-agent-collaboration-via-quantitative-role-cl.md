---
title: "Improving Role Consistency in Multi-Agent Collaboration via Quantitative Role Clarity"
authors:
  - "Guoling Zhou"
  - "Wenpei Han"
  - "Fengqin Yang"
  - "Li Wang"
  - "Yingcong Zhou"
  - "Zhiguo Fu"
date: "2026-04-03"
arxiv_id: "2604.02770"
arxiv_url: "https://arxiv.org/abs/2604.02770"
pdf_url: "https://arxiv.org/pdf/2604.02770v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Collaboration"
  - "Role Consistency"
  - "Fine-Tuning"
  - "Semantic Similarity"
  - "ChatDev"
  - "Failure Mode Analysis"
relevance_score: 7.5
---

# Improving Role Consistency in Multi-Agent Collaboration via Quantitative Role Clarity

## 原始摘要

In large language model (LLM)-driven multi-agent systems, disobey role specification (failure to adhere to the defined responsibilities and constraints of an assigned role, potentially leading to an agent behaving like another) is a major failure mode \cite{DBLP:journals/corr/abs-2503-13657}. To address this issue, in the present paper, we propose a quantitative role clarity to improve role consistency. Firstly, we construct a role assignment matrix $S(φ)=[s_{ij}(φ)]$, where $s_{ij}(φ)$ is the semantic similarity between the $i$-th agent's behavior trajectory and the $j$-th agent's role description. Then we define role clarity matrix $M(φ)$ as $\text{softmax}(S(φ))-I$, where $\text{softmax}(S(φ))$ is a row-wise softmax of $S(φ)$ and $I$ is the identity matrix. The Frobenius norm of $M(φ)$ quantifies the alignment between agents' role descriptions and their behaviors trajectory. Moreover, we employ the role clarity matrix as a regularizer during lightweight fine-tuning to improve role consistency, thereby improving end-to-end task performance. Experiments on the ChatDev multi-agent system show that our method substantially improves role consistency and task performance: with Qwen and Llama, the role overstepping rate decreases from $46.4\%$ to $8.4\%$ and from $43.4\%$ to $0.2\%$, respectively, and the role clarity score increases from $0.5328$ to $0.9097$ and from $0.5007$ to $0.8530$, respectively, the task success rate increases from $0.6769$ to $0.6909$ and from $0.6174$ to $0.6763$, respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型驱动的多智能体系统中普遍存在的“角色不一致”问题。研究背景是，尽管基于LLM的多智能体系统（如ChatDev、MetaGPT）在复杂任务协作（如软件开发）中取得了显著进展，通过为智能体分配不同的角色描述和交互协议，系统能够实现分工与集体推理，但实证研究表明这类系统往往表现不稳定。现有方法的主要不足在于，当前系统主要通过自然语言提示来定义角色，这种方式既不可量化也不可微分，导致智能体在实际协作中容易“越界”——即未能遵守其被分配角色的职责和约束，行为可能与其他角色混淆，从而严重降低端到端的任务成功率。这类似于社会心理学中的“角色模糊”与“角色冲突”现象，会损害团队绩效。

本文要解决的核心问题是：如何以一种可量化、可微分的方式来度量和提升多智能体协作中的角色一致性。为此，论文提出了一个“定量的角色清晰度”定义及优化框架。具体而言，通过构建角色分配矩阵来量化智能体行为轨迹与各角色描述的语义相似度，并基于此定义可微分的角色清晰度矩阵及其Frobenius范数，以此衡量角色描述与行为轨迹的对齐程度。进而，在轻量级微调（如LoRA）过程中，将角色清晰度作为正则化项加入优化目标，引导智能体内化角色约束，从而系统性提升角色一致性，并最终提高端到端的任务性能。实验在ChatDev系统上进行验证，结果表明该方法能显著降低角色越界率、提升角色清晰度得分和任务成功率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大语言模型驱动的多智能体系统及其角色一致性展开，可分为以下几类：

**1. 多智能体系统框架与方法类**：代表性工作如ChatDev、MetaGPT和AutoGen。这些系统通过为智能体分配不同的角色描述（通常为自然语言提示）和交互协议，实现复杂任务的分解与协作。本文与这些工作的关系在于，它直接基于ChatDev框架进行实验和改进。区别在于，现有框架主要依赖提示工程来定义角色，缺乏对角色一致性的量化评估和优化机制，而本文则提出了一个可量化、可微分的角色清晰度定义，并以此作为正则化项进行轻量微调，从而系统性地提升角色一致性。

**2. 多智能体评估与问题诊断类**：相关研究关注多智能体系统的不稳定性和失败模式。例如，有实证研究指出角色不一致（如智能体行为偏离其定义职责，表现得像其他角色）是导致系统失败的一个主要因素。本文与此类工作的关系是，它通过实验（如在ChatDev上评估角色越界率）进一步验证了角色不一致问题的普遍性和严重性。区别在于，本文不仅诊断问题，还进一步提出了一个具体的量化指标（角色清晰度矩阵的Frobenius范数）来测量角色描述与行为轨迹的对齐程度，为问题提供了可优化的数学定义。

**3. 优化与训练方法类**：为了提升智能体行为，现有方法可能依赖精心设计的强化学习奖励函数或更复杂的提示工程。本文与这些优化方法的目标一致，即改善智能体性能。但区别在于，本文提出了一种新的、基于梯度的优化途径：通过将可微分的角色清晰度矩阵作为正则化项融入轻量微调（如LoRA）的目标函数中，直接引导智能体内化角色约束，减少对复杂奖励工程或纯粹提示调整的依赖。

综上所述，本文在现有多智能体协作框架的基础上，针对其核心的角色一致性问题，从量化评估和可微分优化两个维度提出了创新方法，与相关工作形成了互补和推进。

### Q3: 论文如何解决这个问题？

论文通过提出一种可量化的角色清晰度定义，并将其作为正则化项融入轻量级微调过程，来解决多智能体协作中的角色不一致问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心方法**：该方法构建了一个包含三个步骤的量化框架。首先，使用编码器将每个智能体的角色描述文本和行为轨迹嵌入到共享的语义空间，得到角色嵌入向量 \(\mathbf{r}_i\) 和行为嵌入向量 \(\mathbf{b}_i\)。其次，基于这些嵌入向量计算角色分配矩阵 \(S(\phi)\)，其元素 \(s_{ij}\) 表示智能体 \(i\) 的行为与智能体 \(j\) 的角色描述之间的余弦相似度。然后，对 \(S(\phi)\) 按行应用带温度参数的 softmax 归一化，得到行随机矩阵，再减去单位矩阵 \(I\)，最终得到角色清晰度矩阵 \(M(\phi)\)。该矩阵的对角线元素衡量角色一致性（行为符合自身角色），非对角线元素衡量角色越界（行为侵入其他角色职责）。最后，定义系统的角色清晰度为 \(M(\phi)\) 的 Frobenius 范数的倒数形式 \(C(M(\phi)) = 1/(1+\|M(\phi)\|_F)\)，该度量与角色一致性单调相关且可微分。

**主要模块与训练流程**：为实现优化，论文将角色清晰度转化为一个可微的正则化损失函数 \(\mathcal{L}_{RC}^{CE}(\phi) = -\frac{1}{n}\sum_{i=1}^{n} \log softmax_{\tau}(s_{ii}(\phi))\)，其本质是鼓励每个智能体的行为与其自身角色描述的对齐概率（softmax 后的对角线元素）最大化。该正则化项与标准的自回归语言建模负对数似然损失 \(\mathcal{L}_{MLE}\) 结合，形成总体损失 \(\mathcal{L} = \mathcal{L}_{MLE} + \lambda \mathcal{L}_{RC}^{CE}\)。为高效微调大语言模型，论文采用参数高效的 Low-Rank Adaptation (LoRA) 技术，仅训练注入到 Transformer 权重中的低秩矩阵 \(A\) 和 \(B\)，而冻结预训练的主干模型参数。在训练过程中，角色嵌入使用冻结的预训练参数计算，以保持角色描述的稳定锚点；而行为嵌入则通过可训练的参数（LoRA 增量）计算，使得模型能够调整其行为输出以更好地匹配指定角色。

**创新点**：
1.  **量化角色清晰度**：首次提出了一个结构化的、可优化的数学定义（角色清晰度矩阵及其范数），将模糊的自然语言角色描述转化为可量化的对齐与越界度量。
2.  **基于清晰度的正则化**：创新地将角色清晰度转化为一个基于交叉熵的可微正则化项，并融入标准语言模型训练目标，引导模型在完成目标任务的同时，自发地遵守角色规范。
3.  **高效的训练范式**：结合 LoRA 微调，在极大减少可训练参数量的前提下，实现针对角色一致性的定向优化，保证了方法的实用性和可扩展性。实验表明，该方法能显著降低角色越界率，提升角色清晰度分数和任务成功率。

### Q4: 论文做了哪些实验？

论文在ChatDev多智能体系统中进行了实验，以评估所提出的角色清晰度正则化方法在提升角色一致性和端到端任务性能方面的有效性。

**实验设置**：实验基于ChatDev系统，使用Qwen2.5-7B-Instruct和Llama-3.1-8B-Instruct作为骨干模型。针对角色越界主要发生在CEO和CPO智能体之间的问题，仅对这两个智能体进行参数高效的微调，采用LoRA适配器（秩r=16，缩放因子α=16，丢弃率0.05），学习率为5e-5，批量大小为32，最多训练10个周期。

**数据集/基准测试**：使用SWE-Dev基准（包含14,000个训练实例和500个测试实例）进行微调和角色一致性评估。端到端任务性能在SRDD（软件需求描述数据集）上评估，该数据集包含1,200个跨5个领域、40个子类别的任务提示。

**对比方法与主要结果**：实验比较了四种配置：(i) 基线（两者均不微调），(ii) 仅微调CPO，(iii) 仅微调CEO，(iv) 联合微调两者（FT）并应用角色清晰度正则化。还设置了消融实验（移除正则化项）。

**关键数据指标**：
1.  **角色一致性**：在SWE-Dev上，使用角色清晰度分数和角色越界率（越界测试用例数/总测试用例数）衡量。
    *   **Qwen**：联合微调后，总越界率从46.4%降至8.4%，角色清晰度分数从0.5328升至0.9097。
    *   **Llama**：联合微调后，总越界率从43.4%降至0.2%，角色清晰度分数从0.5007升至0.8530。
    *   消融实验表明，移除正则化项后，角色清晰度分数改善微弱甚至下降，凸显了正则化的关键作用。

2.  **端到端任务性能（SRDD）**：从完整性、可执行性、一致性和综合质量四个维度评估。
    *   **Qwen**：微调后，任务成功率（质量分数）从0.6769提升至0.6909。
    *   **Llama**：微调后，任务成功率从0.6174提升至0.6763。
    同时，在SRDD推理中，角色越界率大幅下降（Qwen下降65.79%，Llama下降62.25%），角色清晰度分数显著提升（Qwen提升35.39%，Llama提升34.28%），表明方法有效提升了任务表现和角色边界遵守。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估主要集中于ChatDev框架内的相对短期、结构化的任务，尚未验证在更复杂、开放或长程规划场景中的泛化能力。其角色清晰度矩阵基于语义相似度，可能无法完全捕捉角色行为的动态交互和上下文依赖性，且微调方法可能带来计算成本和过拟合风险。

未来研究方向可包括：1) 将方法扩展到动态角色分配和自适应协作场景，研究角色在任务演进中的演变；2) 探索更细粒度的行为轨迹表征，结合时序或因果推理以提升对齐精度；3) 开发无需微调的即时优化技术，如基于角色的提示工程或推理时约束机制，以降低部署成本；4) 建立跨领域、多模态的角色一致性基准，涵盖工具使用、人机协作等真实应用。此外，可研究角色一致性与系统涌现性、鲁棒性之间的平衡，避免过度约束导致协作僵化。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型驱动的多智能体系统中普遍存在的“角色越界”问题，即智能体未能遵守其指定角色的职责和约束，提出了一个量化角色清晰度的方法来提升角色一致性。其核心贡献是定义了一个角色清晰度矩阵，用以量化智能体行为轨迹与其角色描述之间的对齐程度，并将此矩阵作为正则化项引入轻量级微调过程。

具体方法上，作者首先构建角色分配矩阵，计算每个智能体的行为轨迹与所有角色描述的语义相似度。然后，通过对该矩阵进行行归一化并减去单位矩阵，得到角色清晰度矩阵，其Frobenius范数即为量化的角色清晰度指标。在训练中，通过最大化该指标来正则化模型，从而提升角色一致性。

实验在ChatDev多智能体系统上进行，结果表明该方法能显著降低角色越界率、提升角色清晰度分数，并最终提高端到端任务的成功率，验证了提升角色一致性对整体任务性能的积极影响。
