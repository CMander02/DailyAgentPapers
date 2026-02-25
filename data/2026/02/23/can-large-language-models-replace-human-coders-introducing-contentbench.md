---
title: "Can Large Language Models Replace Human Coders? Introducing ContentBench"
authors:
  - "Michael Haman"
date: "2026-02-23"
arxiv_id: "2602.19467"
arxiv_url: "https://arxiv.org/abs/2602.19467"
pdf_url: "https://arxiv.org/pdf/2602.19467v1"
categories:
  - "cs.CY"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent 评测/基准"
  - "LLM 应用于 Agent 场景"
  - "文本标注"
  - "内容分析"
  - "成本效益分析"
relevance_score: 7.5
---

# Can Large Language Models Replace Human Coders? Introducing ContentBench

## 原始摘要

Can low-cost large language models (LLMs) take over the interpretive coding work that still anchors much of empirical content analysis? This paper introduces ContentBench, a public benchmark suite that helps answer this replacement question by tracking how much agreement low-cost LLMs achieve and what they cost on the same interpretive coding tasks. The suite uses versioned tracks that invite researchers to contribute new benchmark datasets. I report results from the first track, ContentBench-ResearchTalk v1.0: 1,000 synthetic, social-media-style posts about academic research labeled into five categories spanning praise, critique, sarcasm, questions, and procedural remarks. Reference labels are assigned only when three state-of-the-art reasoning models (GPT-5, Gemini 2.5 Pro, and Claude Opus 4.1) agree unanimously, and all final labels are checked by the author as a quality-control audit. Among the 59 evaluated models, the best low-cost LLMs reach roughly 97-99% agreement with these jury labels, far above GPT-3.5 Turbo, the model behind early ChatGPT and the initial wave of LLM-based text annotation. Several top models can code 50,000 posts for only a few dollars, pushing large-scale interpretive coding from a labor bottleneck toward questions of validation, reporting, and governance. At the same time, small open-weight models that run locally still struggle on sarcasm-heavy items (for example, Llama 3.2 3B reaches only 4% agreement on hard-sarcasm). ContentBench is released with data, documentation, and an interactive quiz at contentbench.github.io to support comparable evaluations over time and to invite community extensions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个核心的方法论问题：低成本的大型语言模型（LLMs）能否取代人类编码员，承担社会科学实证研究中至关重要的解释性内容分析（interpretive coding）工作？内容分析是将文本与概念、论点和社会过程联系起来的基础方法，传统上依赖训练有素的人类编码团队，成本高昂、速度慢且难以扩展。论文指出，尽管已有研究探讨LLMs在文本标注任务上的表现，但结果参差不齐，且缺乏一个稳定、可复现的基准来系统性地评估LLMs在解释性分类任务上的表现、成本效益以及随时间推移的进展。因此，本文引入了ContentBench，一个公开的基准测试套件，旨在通过跟踪低成本LLMs在相同解释性编码任务上达到的一致性程度及其成本，来帮助回答这个“替代”问题。论文报告了其第一个赛道（ContentBench–ResearchTalk v1.0）的结果，聚焦于对学术研究相关的社交媒体风格帖子进行五分类任务。

### Q2: 有哪些相关研究？

相关研究主要围绕四个方向展开：1) **LLM编码性能的证据**：多项研究表明，在特定结构化分类任务上，提示调优的LLMs（如ChatGPT, GPT-4）可以匹配甚至超越众包或专家标注，且成本极低（Gilardi et al., 2023; Törnberg, 2025）。然而，其他研究也指出，当任务扩展到不同领域、语言或复杂概念（如讽刺、法律推理、民族志标注）时，LLMs表现不佳，性能差异巨大，且存在可复现性和英语主导性问题（Ollion et al., 2023; Bhat & Varma, 2023; Goodall et al., 2026）。2) **测量基础与参考标准**：内容分析强调编码者间信度（如Krippendorff‘s alpha）。然而，人类标注本身也存在分歧，且标注者背景会影响判断（Pei & Jurgens, 2023）。使用LLMs作为标注工具引发了关于如何建立可靠、有效参考标准的新问题，特别是LLM的误差可能具有系统性并与研究变量相关（Ashwin et al., 2023; Baumann et al., 2025）。3) **混合设计与集成方法**：鉴于直接替代的不确定性，许多研究探索人机混合工作流，例如基于不确定性的任务分配（Li et al., 2023）、置信度阈值审核（Tavakoli & Zamani, 2025），或使用统计方法（如设计监督学习）结合廉价LLM标签和少量黄金标准标签（Egami et al., 2023）。4) **基准测试的缺口**：尽管AI领域有丰富的基准，但社会科学缺乏针对其解释性编码任务的标准化评估工具。一些研究呼吁（Lin & Zhang, 2025）并开始建立领域特定的基准或排行榜（González-Bustamante, 2024a, 2024b）。本文的ContentBench旨在填补这一空白，专注于解释性分类任务，并将协议稳定性、可审计性和成本分析作为核心设计目标。

### Q3: 论文如何解决这个问题？

论文通过设计并发布一个名为ContentBench的公开基准测试套件来解决这个问题。其核心方法包括：1) **套件架构**：ContentBench被设计为一个包含多个版本化赛道（track）的框架，每个赛道代表一个特定领域的数据集家族（如ResearchTalk）。这种设计允许基准随时间演进，同时保持历史评估的可复现性，并鼓励社区贡献新赛道。2) **数据集构建（第一个赛道）**：创建了ContentBench–ResearchTalk v1.0数据集，包含1000条合成的、模仿社交媒体风格的学术研究评论帖子。使用合成数据避免了真实用户数据的伦理和法律问题，并允许跨类别（赞扬、批评、讽刺、问题、程序性陈述）可控地构建项目。帖子由GPT-5和Gemini 2.5 Pro以50/50的比例生成，提示设计具有对抗性，旨在生成对人类易读但对标准LLM分类器困难的文本。3) **参考标签生成**：采用了一个保守的三模型评审团（jury）共识机制来产生参考标签。评审团由三个最先进的推理模型（GPT-5, Gemini 2.5 Pro, Claude Opus 4.1）组成。只有当这三个模型在相同的分类提示下独立给出完全一致的标签时，该帖子才被纳入最终数据集，并赋予该一致标签。之后，作者对所有1000个最终项目进行了人工质量审核。这种方法旨在产生一个高共识、稳定的参考标准，用于评估低成本模型在“明确可分类”案例上的表现。4) **数据分割**：包含两个分割：平衡的核心分割（n=500，每类100条）和硬讽刺分割（n=500，仅包含讽刺性批评类别）。硬讽刺分割专门设计为挑战集，其中的帖子在生成阶段就能被GPT-3.5 Turbo错误分类，从而测试模型对微妙讽刺的识别能力。5) **评估协议**：使用一个固定的、简洁的分类提示（以最小化令牌使用和成本），在温度0.0下评估了59个模型。评估指标包括与评审团标签的整体一致率、核心分割的宏F1和每类召回率、以及硬讽刺分割的讽刺召回率。同时，论文详细计算并报告了每个模型处理5万条帖子的预估成本（基于实际API使用量和定价快照），将性能与成本效益直接关联。

### Q4: 论文做了哪些实验？

论文对ContentBench–ResearchTalk v1.0赛道进行了全面的实验评估：1) **实验设置**：评估了总计59个模型，包括来自OpenAI、Google Gemini系列以及通过OpenRouter访问的各种开源和商业模型（如Llama, Qwen, GLM等）。焦点是“低成本”模型（输入价格≤$0.15/百万令牌）。所有评估使用统一的、锁定的分类提示，温度设为0.0以确保确定性输出。API调用和数据收集于2025年9月完成。2) **基准测试与主要结果**：a) **整体性能**：表现最佳的低成本模型（如Gemini 2.5 Flash系列、GPT-5 Mini）在综合评估集（核心+硬讽刺）上与评审团标签的一致率达到97-99.8%，远高于作为早期LLM标注研究基线的GPT-3.5 Turbo（在核心分割上一致率为79.6%）。b) **类别特异性分析**：在平衡的核心分割上，讽刺性批评类别的平均召回率（约0.52）显著低于其他四类（约0.93-0.96），这证实了讽刺检测的挑战性，并证明了设立硬讽刺分割的必要性。c) **成本分析**：多个顶级模型编码5万条帖子的预估成本仅为几美元（例如，Gemini 2.0 Flash Lite约1.18美元，GLM 4 32B约1.47美元），展示了极高的成本效益。d) **小型开源模型表现**：像Llama 3.2 3B这样可在消费级硬件上本地运行的模型，在核心分割上达到76%的一致率，但在硬讽刺分割上仅达到4%的讽刺召回率，表明其在复杂解释性任务上仍有很大差距。3) **结果解读**：实验结果表明，自GPT-3.5 Turbo以来，低成本LLMs在解释性立场分类任务上的基线性能已大幅提升。然而，作者谨慎指出，由于基准仅保留了评审团一致同意的明确案例，因此高一致率应被解释为在锁定协议下对明确可分类项目的性能，而非跨所有领域或边界案例的普遍有效性保证。

### Q5: 有什么可以进一步探索的点？

论文指出了多个值得未来探索的方向和当前工作的局限性：1) **基准范围的扩展**：当前赛道（ResearchTalk v1.0）范围较窄，仅限英语、短文本、五个类别和合成数据。未来需要扩展到其他领域（如政治话语、媒体报道）、更多语言、更复杂的编码方案（如主题编码、框架分析）以及使用真实世界数据（需解决伦理和数据许可问题）。2) **参考标准的多样性**：当前使用模型评审团共识加人工审核作为参考标准。未来赛道应纳入传统的人类编码参考标签（如专家小组、多人编码、裁决流程），以更直接地评估LLMs与人类编码者的一致性，并探索不同参考标准生成方法的影响。3) **本地开源模型的提升**：实验显示小型开源模型在讽刺等复杂任务上表现不佳。未来工作的一个优先方向是提升这些可在本地部署、避免依赖商业API的模型的性能，以增强研究的可复现性和可控性。4) **方法论与伦理框架**：论文提出了一系列开放性问题，指向一个更根本的探索领域：在何种条件下，LLM编码可以作为已发表研究中内容分析的唯一基础？当使用LLM编码时，应遵循哪些报告标准（模型版本、提示、验证程序）以确保可复现性？如果发现基于LLM的分类存在系统性偏差，应如何划分责任和进行纠正？这些涉及研究方法论、科研伦理和学术规范的问题亟待社区共同探讨并形成共识。5) **对模型更新和API依赖的应对**：商业API模型的频繁更新和淘汰是重大可复现性挑战。需要持续维护基准版本和协议文档，并鼓励对模型快照和本地化部署的评估。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了ContentBench，一个用于评估大型语言模型（LLMs）能否替代人类进行解释性内容分析编码的公开基准测试套件。论文通过第一个赛道ContentBench–ResearchTalk v1.0，系统评估了59个低成本LLMs在对学术研究相关社交媒体帖子进行五分类（赞扬、批评、讽刺、提问、程序性陈述）任务上的表现和成本。其创新点在于：1) 采用保守的三模型评审团共识加人工审核的方式，构建了一个高共识、稳定的参考标签集；2) 专门设计了平衡的核心分割和具有挑战性的硬讽刺分割，以深入分析模型性能，特别是讽刺检测的难点；3) 将模型性能（一致率、F1、召回率）与大规模编码的预估成本紧密结合，为研究者提供了实用的成本效益分析视角。实验结果表明，当前顶级的低成本LLMs（如Gemini 2.5 Flash, GPT-5 Mini）在明确可分类的项目上能达到97-99.8%的高一致率，且编码数万条帖子的成本仅需几美元，性能远超早期的GPT-3.5 Turbo基线。然而，小型开源模型在复杂讽刺任务上仍表现不佳。论文强调，ContentBench并非宣称LLMs已完全取代人类，而是提供了一个可复现、可比较的评估基础设施，以推动关于LLM在社会科学研究中方法论角色、有效性边界及负责任使用框架的持续讨论。
