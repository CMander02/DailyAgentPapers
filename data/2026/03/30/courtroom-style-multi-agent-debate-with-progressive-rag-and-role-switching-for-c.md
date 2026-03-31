---
title: "Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification"
authors:
  - "Masnun Nuha Chowdhury"
  - "Nusrat Jahan Beg"
  - "Umme Hunny Khan"
  - "Syed Rifat Raiyan"
  - "Md Kamrul Hasan"
  - "Hasan Mahmud"
date: "2026-03-30"
arxiv_id: "2603.28488"
arxiv_url: "https://arxiv.org/abs/2603.28488"
pdf_url: "https://arxiv.org/pdf/2603.28488v1"
github_url: "https://github.com/mnc13/PROClaim"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体辩论"
  - "检索增强生成"
  - "结构化智能体"
  - "争议性验证"
  - "角色扮演"
  - "零样本评估"
  - "基准测试"
relevance_score: 8.0
---

# Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification

## 原始摘要

Large language models (LLMs) remain unreliable for high-stakes claim verification due to hallucinations and shallow reasoning. While retrieval-augmented generation (RAG) and multi-agent debate (MAD) address this, they are limited by one-pass retrieval and unstructured debate dynamics. We propose a courtroom-style multi-agent framework, PROClaim, that reformulates verification as a structured, adversarial deliberation. Our approach integrates specialized roles (e.g., Plaintiff, Defense, Judge) with Progressive RAG (P-RAG) to dynamically expand and refine the evidence pool during the debate. Furthermore, we employ evidence negotiation, self-reflection, and heterogeneous multi-judge aggregation to enforce calibration, robustness, and diversity. In zero-shot evaluations on the Check-COVID benchmark, PROClaim achieves 81.7% accuracy, outperforming standard multi-agent debate by 10.0 percentage points, with P-RAG driving the primary performance gains (+7.5 pp). We ultimately demonstrate that structural deliberation and model heterogeneity effectively mitigate systematic biases, providing a robust foundation for reliable claim verification. Our code and data are publicly available at https://github.com/mnc13/PROClaim.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在关键领域（如争议性声明验证）中进行事实核查时，因幻觉、浅层推理和过度自信而导致的不可靠问题。研究背景是，尽管LLM在推理密集型任务上表现出强大的零样本能力，但其在高风险声明验证中的可靠性仍然有限。现有方法如检索增强生成（RAG）通过引入外部知识来缓解幻觉，但标准RAG流程依赖于静态、单次检索，缺乏迭代推理机制，容易导致证据不完整或结论有偏。同时，多智能体辩论（MAD）通过多个LLM实例辩论来提升可靠性，但现有MAD方法往往是非结构化的，容易导致辩论过早收敛、强化共同偏见，且证据探索有限，经常误将智能体间的一致同意视为正确性。

本文的核心问题是：如何设计一个更可靠、结构化的框架，以克服现有RAG和MAD方法的不足，从而更准确、稳健地验证争议性声明。为此，论文提出了PROClaim框架，将声明验证重新构建为一个类似法庭的结构化对抗性审议过程。该框架通过引入明确的角色（如原告、被告、法官等）、证据准入协议和多阶段审议，并结合渐进式检索增强生成（P-RAG）来动态扩展和精炼辩论中的证据池，以促进深度推理和减少系统性偏见。最终，该研究旨在通过结构化审议和模型异质性，为可靠的声明验证提供一个鲁棒的基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕检索增强生成（RAG）和多智能体辩论（MAD）两大方向展开，旨在解决大语言模型在事实核查中的幻觉和浅层推理问题。

在**方法类**工作中，标准RAG通过静态检索引入外部知识，但缺乏迭代检索和推理机制，容易导致证据不完整或偏差。本文提出的渐进式RAG（P-RAG）对此进行了关键改进，实现了辩论过程中证据池的动态扩展与精炼。传统的多智能体辩论则通过多个LLM实例的交互来提升答案质量，但往往存在辩论结构松散、容易过早收敛或强化共同偏见等问题。本文受法律体系启发，引入了法庭式的结构化辩论框架，通过明确的角色分工（如原告、被告、法官）和对抗性审议来克服这些局限。

在**应用与评测类**工作中，现有研究多关注于一般性问答或推理任务，而本文专注于**争议性声明验证**这一高风险领域，并在Check-COVID基准上进行零样本评估。与先前工作相比，本文不仅整合了结构化辩论和动态检索，还创新性地引入了证据协商、自我反思和异构多法官聚合等机制，以增强校准性、鲁棒性和多样性。实验表明，该框架显著优于标准多智能体辩论方法，其中P-RAG是性能提升的主要驱动力，同时模型异构性也被证明对抵消系统性偏差至关重要。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PROClaim的法庭式多智能体辩论框架来解决争议性声明验证问题，其核心方法是将验证过程重构为一个结构化、对抗性的审议流程。整体框架模拟法庭诉讼，包含原告律师、被告律师和独立法官团等专门角色，并集成了渐进式检索增强生成（P-RAG）技术。

在架构设计上，流程分为几个关键阶段。首先，对原始声明进行分解，生成可独立验证的前提命题，以便进行针对性检索和作为论证完整性的检查清单。证据检索阶段采用P-RAG机制，它并非一次性检索，而是动态进行：在每一轮辩论中，智能体基于滚动辩论上下文、自我识别的证据缺口以及上一轮的反思需求来生成查询，由法官优化后执行检索。检索到的证据需通过新颖性过滤、冗余度等自适应停止标准筛选，确保证据池的多样性和质量。此外，框架在辩论前还进行了立场条件检索，分别为支持和反对立场生成优化查询，并引入“谈判注入”步骤，让双方知晓对方的证据池，从而从一开始就构建一个对抗平衡的证据基础。

多智能体辩论是核心推理引擎，涉及五个裁决角色，每个角色由不同的底层大语言模型担任，这种异构分配旨在防止共谋并引入真实分歧。每轮辩论包含证据发现、论证生成、专家证人作证（可动态请求）、自我反思和批评家评估五个步骤。自我反思模块让每个律师从逻辑性、新颖性和反驳力三个维度进行结构化自我批评，其分数会影响最终置信度。独立的批评家智能体则评估双方表现，并可在关键前提均已解决时发出终止信号。

创新点主要体现在几个方面：一是引入了角色切换一致性测试，在主要辩论结束后交换原告和被告律师的角色重新进行辩论，以此诊断论证是证据驱动还是立场锚定，其一致性分数被纳入最终置信度计算。二是采用异构多法官聚合机制，由三个不同模型的法官独立评估案件并投票得出最终裁决，有效降低了系统性偏差。三是设计了一个两阶段的置信度计算方案，基础置信度基于法官共识强度和平均质量评分，再结合角色切换调整和获胜方的自我反思调整进行修正，并通过网格搜索优化权重以实现良好的校准效果。

通过这种将结构化对抗审议、动态渐进检索与模型异构性相结合的系统设计，PROClaim实现了更深入、更可靠的推理，显著提升了在零样本设置下进行声明验证的准确性和鲁棒性。

### Q4: 论文做了哪些实验？

论文在Check-COVID基准测试上进行了零样本评估，这是一个包含具有明确二元真值（支持或反驳）的争议性健康声明的数据集。实验设置采用了法庭风格的多智能体辩论框架PROClaim，包含原告、被告、法官等专门角色，并集成了渐进式检索增强生成（P-RAG）在辩论中动态扩展证据池。对比方法包括：使用RAG的单次调用大语言模型（如GPT-5-mini和DeepSeek-v3.2），以及标准的多智能体辩论（MAD）基线（包含两个代理和一个法官，进行3轮辩论）。主要结果显示，PROClaim的多数投票准确率达到81.7%，显著优于标准MAD（71.7%，提升10.0个百分点）和单次调用基线（如GPT-5-mini为85.8%，但缺乏可追溯性）。关键指标包括：P-RAG带来+7.5个百分点的最大性能增益；平均证据池大小为67.5；平均辩论轮数为5.47；法官间一致性（平均Cohen‘s κ为0.468）。消融实验证实了各组件贡献：移除P-RAG导致准确率下降7.5个百分点；移除角色切换下降4.2个百分点；移除三法官面板下降3.3个百分点。此外，框架在HealthVer和FEVEROUS数据集上的泛化实验分别取得了72.0%和78.3%的准确率，证明了其领域适应性。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架在计算成本和运行稳定性方面存在明显局限。未来研究可从以下方向深入：首先，在架构优化上，可探索基于证据置信度的动态回合终止机制，或引入轻量级学生模型进行知识蒸馏，以降低多轮辩论与角色切换带来的高昂计算开销。其次，在检索增强方面，可尝试将渐进式RAG与实时知识库（如动态更新的学术数据库）结合，并引入检索质量评估模块，以提升证据迭代的效率和准确性。此外，该框架目前依赖最终置信度评分，未来可设计细粒度的辩论过程追踪机制，例如通过辩论路径可视化或因果分析，以深入理解多智能体在争议性主张验证中的动态推理过程。最后，将该法庭辩论范式迁移至科学事实核查、金融合规审查等领域时，需针对领域特性设计专用角色与证据评估标准，并探索跨领域泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PROClaim的法庭式多智能体辩论框架，旨在解决大语言模型在争议性声明验证中存在的幻觉和浅层推理问题。核心贡献是将验证任务重构为结构化的对抗性审议过程，通过角色分工（如原告、被告、法官）与渐进式检索增强生成相结合，动态扩展和精炼证据库。方法上，系统整合了证据协商、自我反思和异构多法官聚合机制，以增强校准性、鲁棒性和多样性。实验结果表明，在Check-COVID基准的零样本评估中，PROClaim达到了81.7%的准确率，比标准多智能体辩论提升了10.0个百分点，其中渐进式检索贡献了主要性能增益（+7.5个百分点）。最终证明，结构化审议和模型异质性有效缓解了系统偏见，为可靠的声明验证提供了稳健基础。
