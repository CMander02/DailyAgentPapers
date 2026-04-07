---
title: "PassiveQA: A Three-Action Framework for Epistemically Calibrated Question Answering via Supervised Finetuning"
authors:
  - "Madhav S Baidya"
date: "2026-04-06"
arxiv_id: "2604.04565"
arxiv_url: "https://arxiv.org/abs/2604.04565"
pdf_url: "https://arxiv.org/pdf/2604.04565v1"
github_url: "https://github.com/MadsDoodle/PassiveQA"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Reasoning"
  - "Agent Decision-Making"
  - "Supervised Finetuning"
  - "Epistemic Awareness"
  - "Question Answering"
  - "Retrieval-Augmented Generation"
  - "Hallucination Reduction"
  - "Information Sufficiency"
relevance_score: 7.5
---

# PassiveQA: A Three-Action Framework for Epistemically Calibrated Question Answering via Supervised Finetuning

## 原始摘要

Large Language Models (LLMs) have achieved strong performance in question answering and retrieval-augmented generation (RAG), yet they implicitly assume that user queries are fully specified and answerable. In real-world settings, queries are often incomplete, ambiguous, or missing critical variables, leading models to produce overconfident or hallucinated responses.
  In this work, we study decision-aware query resolution under incomplete information, where a model must determine whether to Answer, Ask for clarification, or Abstain. We show that standard and enhanced RAG systems do not reliably exhibit such epistemic awareness, defaulting to answer generation even when information is insufficient.
  To address this, we propose PassiveQA, a three-action framework that aligns model behaviour with information sufficiency through supervised finetuning. Our approach integrates structured information-state representations, knowledge graph-grounded context, and a finetuned planner that explicitly models missing variables and decision reasoning.
  Experiments across multiple QA datasets show that the finetuned planner achieves significant improvements in macro F1 and abstention recall while reducing hallucination rates, under a compute-constrained training regime.
  These results provide strong empirical evidence that epistemic decision-making must be learned during training rather than imposed at inference time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在问答和检索增强生成任务中普遍存在的一个根本性问题：模型默认所有用户查询都是信息完整且可回答的，而现实中的查询往往不完整、模糊或缺少关键变量，导致模型产生过度自信或幻觉的答案。研究背景是现有RAG系统和LLM在部署时，面对信息不足的查询，缺乏判断是否应该回答、请求澄清还是拒绝回答的“认知意识”，通常会直接生成答案，造成错误。

现有方法的不足主要体现在两个方面。首先，标准的RAG及其增强版本（如使用语义分块、混合检索、重排序等技术）并未从根本上解决这一问题，反而可能因为检索到更看似合理的证据而加剧过度自信的回答，实验表明一个增强的RAG管道幻觉率高达51.7%。其次，常见的缓解方法（如基于置信度校准的拒绝机制）存在缺陷：一是它无法区分“知识库中完全缺失相关信息”（应拒绝）和“查询缺少关键变量但可通过对话澄清”（应提问）这两种本质不同的认知状态；二是基于熵的置信度信号本身不足以让LLM进行可靠的选择性预测，模型在低置信度时也常常不会拒绝回答。

因此，本文要解决的核心问题是：如何让模型在信息不完整的情况下，具备基于信息状态的、细粒度的认知决策能力。具体而言，论文提出了一个名为PassiveQA的三行动框架，通过监督微调使模型行为与信息充分性对齐。该框架要求模型根据查询的信息状态（已知变量、缺失变量、上下文）明确决策是回答、请求澄清还是拒绝回答，从而从根本上减少幻觉，实现更安全、更可靠的问答。

### Q2: 有哪些相关研究？

本文的相关工作主要涵盖以下几类：

**检索增强生成（RAG）与幻觉检测**：标准及增强的RAG系统通过检索外部知识来提升问答性能，但缺乏对信息充分性的显式建模，易导致过度自信的回答。针对幻觉问题，已有研究通过后验校准或选择性弃权来检测和抑制不忠实内容。本文与之不同，**聚焦于在生成答案之前的决策本身**（即是否回答），而非对已生成答案的事后验证。

**选择性预测与弃权**：该领域研究覆盖度与准确性的权衡，已有工作将弃权机制形式化并应用于开放域问答。然而，研究发现大语言模型往往不善于判断何时应拒绝回答，且仅依赖置信度熵并不可靠。本文**将选择性预测扩展为一个包含“回答”、“澄清提问”和“弃权”的三路决策框架**，以更精细地处理信息不完整的情况。

**对话式与澄清寻求式问答**：ShARC基准首次引入了在给出基于策略的答案前寻求澄清的机制，直接启发了本文的“提问”动作。后续研究探讨了信息寻求对话和主动提问的生成。本文的贡献在于提出了一个**统一的三动作框架**，并引入了基于知识图谱的监督信号，而先前工作或缺乏统一框架，或未使用图谱进行决策强化。

**基于知识图谱的问答**：已有研究利用知识图谱的结构化知识来支持多跳推理，例如通过图神经网络进行联合推理。本文**扩展了这一范式**，构建了一个决策强化的知识图谱，其边权重编码了三动作监督信号，这是先前图增强QA系统所不具备的维度。

**参数高效微调与对齐**：LoRA等高效微调技术使得在有限算力下调整大模型成为可能。从InstructGPT等工作中可知，训练时对齐是改变模型行为的根本机制。本文**应用LoRA对模型进行监督微调**，将认知路由决策视为一个行为对齐问题，而非提示工程问题，从而在计算受限的条件下实现决策行为的有效植入。

### Q3: 论文如何解决这个问题？

论文通过提出PassiveQA框架来解决LLMs在面对信息不完整查询时过度自信或产生幻觉的问题。其核心方法是采用一个三动作（回答、澄清询问、弃权）的决策框架，并通过监督微调使模型行为与信息充分性对齐。

整体架构设计将决策与生成分离。系统首先初始化一个信息状态S(q)，该状态由已知变量V_known、缺失变量V_missing和约束集C构成。一个专门的规划器π_θ基于此状态，通过一个神经网络f_θ计算，在三个动作上输出一个概率策略，其目标是最大化给定信息状态下的期望效用，而非直接生成回复。这种决策与生成的解耦是区别于传统RAG系统的关键架构承诺。

主要模块与关键技术包括：
1.  **状态表示与不完整性度量**：信息状态被形式化地结构化表示。不完整性度量I(q) = |V_missing| / (|V_known| + |V_missing|) 被用作决策的关键信号，论文假设幻觉风险H(q)与I(q)成正比。
2.  **多信号决策门控**：规划器（或一个硬门控规则）综合四种检索衍生的信号进行决策：
    *   **置信度(Conf)**：查询与检索文档的最佳匹配度。
    *   **覆盖率(Coverage)**：查询术语在检索结果中的覆盖比例。
    *   **模糊性(Amb)**：基于查询长度、代词、模糊量词等启发式特征估计的查询模糊程度。
    *   **冲突(Conflict)**：检索到的前k个文本块之间的平均余弦不相似度，用于检测证据内部矛盾。
    这些信号被整合为一个联合可回答性信号A(q)，理论上当任一信号不足时都会促使系统转向“询问”或“弃权”。
3.  **知识图谱锚定的上下文**：系统利用知识图谱来评估缺失变量的可恢复性。如果缺失变量能在图谱中作为占位符节点注入，则认为可恢复（触发“询问”），否则可能触发“弃权”。图谱边的权重结合了语义相似度和动作强化信号，用于支持路径推理。
4.  **监督微调与损失函数**：对规划器进行监督微调，损失函数包含决策分类损失（交叉熵）和生成损失（因果语言建模损失），即L = L_decision + λL_generation，确保模型学习基于信息状态的决策逻辑。
5.  **多轮对话状态更新**：在对话中，信息状态会动态更新。成功的“询问”动作会将用户澄清提供的变量从V_missing移至V_known，从而降低不完整性度量，推动对话向可“回答”的方向演进。

创新点在于：1) 明确将信息充分性作为核心决策维度，并形式化为结构化状态和不完整性度量；2) 提出决策与生成分离的架构，通过专用规划器实现基于效用的三动作策略；3) 综合利用多种可计算的检索信号和知识图谱来量化信息缺口与矛盾，为决策提供细粒度依据；4) 通过监督微调而非推理时启发式方法，使模型内化这种认知决策能力。实验表明，该方法在计算受限的训练下显著提升了宏观F1和弃权召回率，同时降低了幻觉率。

### Q4: 论文做了哪些实验？

论文实验部分主要评估了三种逐步复杂的检索增强生成（RAG）架构，并在一个平衡的900样本保留集（每个动作300个样本）上进行了测试，随后引入了基于图的规划器进行微调。

**实验设置与数据集**：实验使用了四个公开数据集（ShARC、QuAC、HotpotQA、ContractNLI），它们被整合并转换为统一的JSON格式，最终构建了一个包含约61K样本的平衡训练子集，动作分布为：Answer 49.9%、Ask 28.9%、Abstain 21.2%。评估在一个包含900个样本的保留集上进行，每个动作类别各300个。

**对比方法**：
1.  **基线RAG**：标准的检索-生成流程，使用FAISS进行向量检索，由Mistral-7B-Instruct-v0.3模型生成响应。
2.  **增强型RAG**：在基线基础上引入了五项改进，包括多粒度知识库、混合检索（BM25+稠密检索）、查询理解、交叉编码器重排序与上下文压缩以及自我反思。
3.  **架构3（硬门控管道）**：采用预生成决策管道，通过证据评分、可回答性分类器和基于明确规则的硬门控来决定动作，再调用特定动作的生成提示。

**主要结果与关键指标**：
*   **基线RAG**：决策准确率34%，幻觉率42.7%，宏F1分数26.7%。模型严重偏向Answer动作（准确率81%），而Ask和Abstain的准确率分别仅为12%和9%。
*   **增强型RAG**：尽管进行了多项改进，但其决策准确率（34%）和宏F1分数（26.7%）与基线无统计差异，幻觉率甚至升至51.7%，表明仅靠推理时改进无法解决模型固有的认知偏差。
*   **架构3（硬门控）**：取得了可测量的改进：决策准确率38%，宏F1分数35.3%（提升8.6个百分点），幻觉率33.8%（降低9个百分点），Ask召回率达到40%（基线为2%）。然而，Abstain召回率仍然较低（13.3%）。这些结果凸显了仅通过推理时干预存在上限，从而引出了对模型进行监督微调的必要性。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的PassiveQA框架在提升模型对信息充分性的认知判断上取得了进展，但其局限性和未来探索方向也较为明显。首先，当前工作主要依赖监督微调，这需要大量高质量、标注了三种动作（回答、澄清、弃权）的训练数据，其构建成本高昂且可能难以覆盖开放域中所有的信息不完整场景。未来可探索更高效的学习范式，例如结合强化学习从交互反馈中学习决策，或利用自监督方法从模型自身的不确定性中生成训练信号。

其次，框架中的“知识图谱锚定上下文”可能受限于特定领域的知识图谱完备性。一个重要的改进方向是探索更灵活、动态的知识感知机制，例如让模型在推理时主动检索外部知识源（包括非结构化文本）来评估信息缺口，而不仅仅依赖预定义的图谱。

最后，论文在“计算受限的训练机制”下验证了效果，但未深入探讨模型规模与认知校准能力的关系。未来可研究：1）是否能在更小的模型上通过架构设计（如专门的决策头）实现类似能力；2）如何将这种决策框架无缝集成到现有的复杂RAG管道中，使其不仅能判断，还能主动引导多轮对话以逐步补全信息。这些方向有望使AI助手在真实、信息模糊的交互中更加可靠和有用。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在问答任务中因用户查询信息不完整而导致的过度自信或幻觉问题，提出了PassiveQA框架。核心贡献在于将模型行为与信息充分性对齐，通过监督微调使模型能够根据查询完整性自主选择三种动作：回答、请求澄清或弃权。方法上，该框架整合了结构化信息状态表示、基于知识图谱的上下文以及一个经过微调的规划器，该规划器显式建模缺失变量和决策推理。实验表明，在计算受限的训练条件下，微调后的规划器在多个问答数据集上显著提升了宏观F1分数和弃权召回率，同时降低了幻觉率。主要结论是，认知决策能力必须在训练阶段学习，而非仅在推理时强制施加，这为构建更可靠、自知不确定性的问答系统提供了实证依据。
