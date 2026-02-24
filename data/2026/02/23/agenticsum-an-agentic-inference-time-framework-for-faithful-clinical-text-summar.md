---
title: "AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization"
authors:
  - "Fahmida Liza Piya"
  - "Rahmatollah Beheshti"
date: "2026-02-23"
arxiv_id: "2602.20040"
arxiv_url: "https://arxiv.org/abs/2602.20040"
pdf_url: "https://arxiv.org/pdf/2602.20040v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "Agentic 推理"
  - "医疗应用"
  - "文本摘要"
  - "幻觉缓解"
relevance_score: 8.0
---

# AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization

## 原始摘要

Large language models (LLMs) offer substantial promise for automating clinical text summarization, yet maintaining factual consistency remains challenging due to the length, noise, and heterogeneity of clinical documentation. We present AgenticSum, an inference-time, agentic framework that separates context selection, generation, verification, and targeted correction to reduce hallucinated content. The framework decomposes summarization into coordinated stages that compress task-relevant context, generate an initial draft, identify weakly supported spans using internal attention grounding signals, and selectively revise flagged content under supervisory control. We evaluate AgenticSum on two public datasets, using reference-based metrics, LLM-as-a-judge assessment, and human evaluation. Across various measures, AgenticSum demonstrates consistent improvements compared to vanilla LLMs and other strong baselines. Our results indicate that structured, agentic design with targeted correction offers an effective inference time solution to improve clinical note summarization using LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在临床文本摘要任务中存在的“幻觉”问题，即生成流畅但缺乏源文档支持、可能歪曲临床事实的内容。当前基于LLM的摘要系统通常采用单次前向生成，缺乏在生成过程中进行显式验证、修正或监督控制的机制，这与临床文档工作流中要求草案经过审核和授权的实践不匹配。为此，论文提出了AgenticSum，一个推理时（inference-time）的智能体框架。该框架通过将摘要任务分解为协调的多个阶段——包括上下文选择、生成、验证和针对性修正——来结构化地减少幻觉内容。其核心创新在于将程序化的智能体架构与模型内部注意力等 grounding 信号相结合，从而实现对生成内容的细粒度事实性评估和可控修订，以提高临床摘要的忠实度。

### Q2: 有哪些相关研究？

相关工作主要围绕临床文本摘要、幻觉与忠实性、令牌级过滤与注意力选择，以及面向忠实摘要的智能体分解四个方面。

在**临床文本摘要**方面，先前研究利用了预训练语言模型（如BioGPT、PubMedBERT）和指令微调模型（如Flan-T5），并提出了特定任务架构（如Pointer-GPT）以改善内容保留。然而，这些方法通常在未压缩的令牌序列上操作，对于冗长的临床叙述存在效率低下和幻觉风险增加的问题。本文提出的AgenticSum框架通过分离上下文选择、生成、验证和针对性修正等阶段，直接应对了长文档处理中的效率与忠实性挑战。

关于**幻觉与忠实性**，研究指出临床摘要中普遍存在外在幻觉问题，即生成内容临床合理但缺乏原文支持。现有评估框架强调基于源文本的事实性。近期方法开始利用模型内部信号来估计生成过程对源内容的依赖。本文继承了这一视角，利用内部注意力信号来识别弱支持文本段，并设计了针对性的修正机制。

在**令牌级过滤与注意力选择**方面，已有工作通过基于注意力的技术（如PoWER-BERT、Rho-1）选择重要令牌以减少计算开销，但主要关注效率提升，缺乏确保事实基础的机制。本文的上下文选择阶段借鉴了此类输入压缩思想，但将其整合进一个更广泛的、以忠实性为核心的智能体框架中。

最后，在**智能体分解**方面，先前研究表明，将生成、评估和修订解耦的智能体或多阶段框架（如Self-Refine、Reflexion、ReAct）能提升复杂生成任务的鲁棒性。协作智能体系统也被探索用于文档处理和临床工作流。然而，这些工作主要关注任务准确性或交互质量，对临床摘要中基于源文档的忠实性和显式的幻觉诊断关注有限。本文的AgenticSum框架正是针对这一缺口，将智能体分解结构与事实验证机制紧密结合，专门用于提升临床文本摘要的忠实性。

### Q3: 论文如何解决这个问题？

AgenticSum 通过一个模块化的、基于智能体（Agent）的推理时框架来解决临床文本摘要中的事实一致性问题。其核心方法是将摘要生成过程分解为四个专门化的智能体和一个监督控制模块，通过分离上下文选择、生成、验证和针对性修正来减少幻觉。

**核心架构与流程**：
1.  **FocusAgent（输入压缩）**：首先对冗长、嘈杂的临床文档进行压缩。它采用FOCUS方法，利用冻结Transformer模型的解码器自注意力机制，在句子级别计算上下文显著性分数（β_j），保留得分最高的前k个句子（k = ⌊r·m⌋，r为保留比例）。这确保了后续阶段仅处理与摘要任务最相关的信息，减轻了生成模型的负担。

2.  **DraftAgent（草稿生成）**：基于压缩后的文档 D_reduced，使用预训练的语言模型生成初始摘要草稿 S^(0)。此阶段不进行事实核查，专注于生成流畅、连贯的文本。

3.  **HallucinationDetectorAgent（幻觉检测）**：对当前摘要 S^(t) 进行双重验证。
    *   **注意力信号（AURA）**：计算每个生成token的解码器自注意力中分配给源文档token的比例，得到token级AURA分数，再聚合为摘要片段（如句子）级的连续分数 a_j，反映模型对源文档的依赖程度。
    *   **语义验证**：使用文本蕴含（entailment）方法，以源文档为唯一依据，判断每个摘要片段 z_j 是否被支持，产生二元幻觉标签 h_j（1表示不支持）。

4.  **FixAgent（针对性修复）**：根据检测结果，对疑似幻觉的片段集合 H（定义为 h_j=1 或 a_j < 阈值 τ 的片段）进行修订。它利用压缩文档 D_reduced、当前摘要 S^(t) 和待修正片段 H，生成修订后的摘要 S^(t+1)。

5.  **ClinicalSupervisorAgent（监督迭代优化）**：控制整个迭代修正循环。在每次迭代t中，触发幻觉检测和修复。它通过计算当前摘要的平均AURA分数 Ā^(t) 等指标来判断是否收敛。当平均分数变化小于阈值ε、新识别的幻觉片段集为空或达到最大迭代次数时，终止流程，输出最终摘要。

**关键技术**：
*   **模块化与角色专精**：将复杂任务分解为专注子任务的智能体，各司其职，便于控制和调试。
*   **内部注意力作为 grounding 信号**：创新性地利用模型固有的解码器自注意力（AURA）作为量化源文档依赖程度的轻量级、无需训练的信号，与外部语义验证互补。
*   **针对性修正与显式终止控制**：仅对检测出的问题片段进行修订，而非全文重写，提高了效率。监督智能体提供了明确的迭代终止条件，避免了无约束自我修正的不稳定性。

总之，AgenticSum通过这种结构化的、多智能体协作的推理时框架，实现了对临床文本摘要生成过程的精细控制，有效提升了摘要的事实忠实度。

### Q4: 论文做了哪些实验？

论文在MIMIC-IV-Ext-BHC和SOAP Summary两个临床文本数据集上进行了全面的实验评估。实验设置包括与多个强基线模型（如BioBART、T5-Large、Flan-T5、Gemma3-1B、Llama-3.2-3B、Mistral-7B、MedAlpaca-7B和ConTextual）进行比较，并进行了模块消融研究（对比Vanilla LLM、DraftAgent和完整AgenticSum系统）。

基准测试使用了三类指标：1) 基于参考的语义指标（BLEU-1/2、ROUGE-L和BERTScore），用于评估内容重叠和语义对齐；2) LLM-as-a-Judge评估，使用指令调优的LLaMA-3-8B模型在1-5分尺度上对幻觉频率、事实一致性、完整性和连贯性四个维度进行评分；3) 人工评估，通过在线调查让23名具有不同学术/临床背景的参与者，在精神病学、心肺科和肿瘤学三个临床领域，比较基线模型与AgenticSum生成摘要的幻觉严重性，并计算正确猜测准确率和幻觉严重性分数。

主要结果显示，AgenticSum在两个数据集的所有语义指标上均取得最佳性能（例如在MIMIC-IV上，BLEU-2为12.61，BERTScore为84.50）。在LLM评估中，AgenticSum在MIMIC-IV上获得了最低的幻觉评分（1.88），并在两个数据集上保持了高完整性和事实一致性。人工评估进一步证实了其有效性，在三个临床领域中，参与者正确识别AgenticSum摘要幻觉更少的准确率均超过78%（最高达91.3%），且其幻觉严重性分数（平均约1.99）显著低于原始LLM摘要（平均约3.93），所有结果均具有统计显著性。消融研究表明，其输入压缩和生成后修正模块均对性能提升有贡献。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于未能完全消除幻觉，主要针对上下文不一致问题，而微妙的语义遗漏等事实扭曲形式仍未解决。依赖模型内部注意力信号可能遗漏未体现在注意力模式中的幻觉，尽管通过结合注意力基础与语义验证进行了缓解。实验聚焦中小型模型以降低临床部署延迟与成本，但未验证在更大模型上的效果。

未来可探索的方向包括：开发更全面的幻觉检测机制，超越注意力信号结合外部知识验证；针对语义遗漏等细微事实失真设计专项修正模块；将框架扩展至更大规模语言模型，评估其性能增益与计算成本平衡；探索框架在其他高精度要求领域（如法律、金融文本）的泛化能力；研究如何进一步优化多阶段协作的推理效率，减少延迟以满足实时临床需求。

### Q6: 总结一下论文的主要内容

这篇论文提出了AgenticSum，一个用于临床文本摘要的智能体推理框架，旨在解决大语言模型在生成临床摘要时容易产生事实性错误（幻觉）的难题。其核心贡献在于将摘要任务分解为四个协调的智能体阶段：首先选择并压缩任务相关上下文，然后生成初始草稿，接着利用模型内部注意力信号识别草稿中证据薄弱的部分，最后在监督控制下有选择地修正这些被标记的内容。这种结构化的“选择-生成-验证-修正”流程，无需额外训练，仅在推理时通过智能体协作来提升事实一致性。实验在多个公开数据集上通过自动指标、LLM评判和人工评估证实，该方法相比原始LLM及其他基线模型能持续提升摘要的忠实度。其意义在于为LLM在临床等高风险领域的可靠应用，提供了一种有效的、可解释的推理时解决方案。
