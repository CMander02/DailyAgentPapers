---
title: "Doc-V*:Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA"
authors:
  - "Yuanlei Zheng"
  - "Pei Fu"
  - "Hang Li"
  - "Ziyang Wang"
  - "Yuyi Zhang"
  - "Wenyu Ruan"
  - "Xiaojin Zhang"
  - "Zhongyu Wei"
  - "Zhenbo Luo"
  - "Jian Luan"
  - "Wei Chen"
  - "Xiang Bai"
date: "2026-04-15"
arxiv_id: "2604.13731"
arxiv_url: "https://arxiv.org/abs/2604.13731"
pdf_url: "https://arxiv.org/pdf/2604.13731v1"
categories:
  - "cs.CL"
tags:
  - "Document Agent"
  - "Visual Reasoning"
  - "Agentic Framework"
  - "Interactive Navigation"
  - "Imitation Learning"
  - "Multi-Page VQA"
  - "OCR-free"
  - "Evidence Aggregation"
  - "Working Memory"
  - "Policy Optimization"
relevance_score: 8.5
---

# Doc-V*:Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA

## 原始摘要

Multi-page Document Visual Question Answering requires reasoning over semantics, layouts, and visual elements in long, visually dense documents. Existing OCR-free methods face a trade-off between capacity and precision: end-to-end models scale poorly with document length, while visual retrieval-based pipelines are brittle and passive. We propose Doc-$V^*$, an \textbf{OCR-free agentic} framework that casts multi-page DocVQA as sequential evidence aggregation. Doc-$V^*$ begins with a thumbnail overview, then actively navigates via semantic retrieval and targeted page fetching, and aggregates evidence in a structured working memory for grounded reasoning. Trained by imitation learning from expert trajectories and further optimized with Group Relative Policy Optimization, Doc-$V^*$ balances answer accuracy with evidence-seeking efficiency. Across five benchmarks, Doc-$V^*$ outperforms open-source baselines and approaches proprietary models, improving out-of-domain performance by up to \textbf{47.9\%} over RAG baseline. Other results reveal effective evidence aggregation with selective attention, not increased input pages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多页文档视觉问答（DocVQA）中现有方法在**处理能力与精度之间的根本性权衡**问题。研究背景是，多页文档（如学术论文、财务报告）包含复杂的文本语义、空间布局和视觉元素（如图表）的交互，传统基于OCR的流程会丢失布局细节并累积识别错误，而新兴的免OCR纯视觉方法虽能联合推理，却面临两大局限。现有方法的不足主要体现在：一方面，端到端模型将整个文档作为长图像序列处理，受限于二次注意力成本、上下文长度限制以及“迷失在中间”效应，难以扩展到长文档；另一方面，基于视觉检索增强生成（RAG）的流水线虽通过检索相关页面来降噪，但存在检索错误、对超参数敏感、多跳推理能力有限的问题，且这两种范式都是**被动的**——它们处理固定输入，无法根据新证据动态调整策略，这与人类主动、迭代的阅读行为不匹配。

因此，本文要解决的核心问题是：如何设计一个**免OCR的、主动的（agentic）框架**，以模拟人类阅读中的主动视觉认知过程，实现从粗到细的交互式视觉推理，从而在长而密集的多页文档中高效、精确地聚合证据并回答问题。具体而言，论文提出的Doc-V*框架将多页DocVQA重新定义为**顺序证据聚合过程**，通过全局缩略图概览、语义检索、定向页面抓取等主动导航动作，在结构化工作记忆中逐步积累证据，最终进行基于证据的推理作答，以平衡答案准确性与证据搜索效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多页文档视觉问答（DocVQA）的方法展开，可分为以下几类：

**1. OCR-based DocVQA方法**：这类方法首先通过OCR和文档解析提取文本和布局结构，然后在结构化表示上进行推理。它们在格式规范的文档上有效，但存在OCR和布局错误的级联问题，对噪声或领域外场景泛化能力差。本文提出的Doc-V*是OCR-free的，避免了此类错误累积。

**2. OCR-free纯视觉DocVQA方法**：近期方法利用大型视觉-语言模型直接从文档图像中推理，保留了丰富的视觉和空间线索。具体可细分为：
*   **端到端模型**：联合处理所有页面，但计算成本和内存消耗随文档长度急剧增长，可扩展性差。
*   **基于检索的方法**：先检索最相关的k个页面再生成答案，提高了效率，但对检索错误和固定超参数敏感，且是被动式检索。
*   **基于智能体（Agent）的系统**：迭代式探索文档，引入了交互但增加了复杂性。

本文的Doc-V*属于OCR-free的智能体框架，但与上述方法有显著区别：它将多页DocVQA重新定义为**一个顺序的证据聚合过程**。该智能体从缩略图概览开始，通过语义检索和针对性页面获取进行主动导航，并在结构化工作记忆中聚合证据以进行推理。这实现了在长文档中主动、高效地聚合视觉证据，在精度与效率间取得了更好的平衡。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Doc-V*的、无需OCR的智能体框架来解决多页文档视觉问答中的容量与精度权衡问题。其核心是将任务建模为一个顺序决策过程，使智能体能够主动、有选择地收集证据，而非被动处理整个文档。

**整体框架与架构设计**：Doc-V*基于Qwen-2.5-VL架构构建，包含视觉编码器、投影模块和大语言模型主干。其创新在于引入了一个**由粗到细的交互式推理流程**。首先，系统为整个文档生成一个**全局缩略图概览**，将多页文档分组并重组为网格图像，并标注绝对页码，使智能体能快速把握文档结构、布局和图表分布等宏观信息，为后续导航提供先验。智能体以此概览和问题作为初始观察，开始与环境进行多轮闭环交互。

**主要模块与交互协议**：智能体在每轮交互中遵循严格的“思考-行动”格式（ReAct风格）。思考部分被结构化，包含对当前信息的分析、下一步计划以及更新到工作记忆中的摘要。行动部分则定义了三种原子操作：1. **检索动作**：允许智能体发出文本查询，近似于“文档内搜索”行为，环境调用外部多模态检索器返回最相关的未访问页面。2. **获取动作**：允许智能体通过绝对页码直接请求特定页面，支持基于缩略图线索（如目录、图表位置）或问题中明确提及的页码进行精准导航。3. **回答动作**：当证据充足时，智能体生成最终答案并终止交互。环境动态返回所请求页面的高分辨率视觉令牌，并避免重复访问。为解决长交互中的遗忘问题，系统维护了一个**结构化工作记忆**，持续拼接历史摘要，确保推理链的连贯性。

**训练与优化关键技术**：训练分为两阶段。首先，使用从专家轨迹蒸馏的数据进行**监督微调**，确保智能体掌握工具使用和基本推理。其次，采用**分组相对策略优化**进行强化学习，在仅使用结果监督（答案正确性、证据检索质量等）的情况下，对智能体在有限交互步数内的探索效率进行优化，平衡信息获取与处理成本。

**核心创新点**：1) **主动、顺序的证据聚合范式**，模拟人类目标导向的浏览行为；2) **由粗到细的视觉表示**，通过缩略图概览引导精细探索；3) **结构化、可审计的交互协议与工作记忆**，增强了推理过程的透明性和连贯性；4) **结合模仿学习与高效RL的训练策略**，在提升准确性的同时优化了探索效率。该方法在多个基准测试上超越了开源基线，并接近了专有模型的性能。

### Q4: 论文做了哪些实验？

论文在五个基准数据集上进行了全面实验，涵盖域内和域外评估。实验设置方面，模型基于Qwen-2.5-VL-7B-Instruct初始化，使用ColQwen作为外部检索器，动态设置检索预算k=min(⌈N/10⌉,4)，最大交互步数T=8，并采用复合奖励函数（答案正确性权重0.6、证据召回0.3、结构有效性0.1）进行优化。

数据集包括域内的MP-DocVQA和DUDE，以及域外的SlideVQA、LongDocURL和MMLongBench-Doc，以评估泛化能力。对比方法涵盖三类：端到端模型（如HiVT5、mPLUG-DocOwl2）、检索增强生成方法（如CREAM、M3DocRAG）和基于智能体的方法（如VRAG-RL、CogDoc），同时以闭源模型（如GPT-4o、Claude-3.7-Sonnet）作为参考。

主要结果显示，Doc-V*在开源方法中表现优异。在域内评估中，DUDE上达到64.5 ANLS，超越所有开源基线及GPT-4o（54.1）；MPDocVQA上为86.2 ANLS，与最优基线URaG（88.2）相当。在域外评估中，SlideVQA上F1达77.2，超越SlideVQA专训模型CogDoc（67.9）；MMLongBench-Doc和LongDocURL上准确率分别为42.1和56.3，创开源新高。关键指标显示，与RAG Top-5基线相比，Doc-V*在DUDE上提升12.3 ANLS（52.2→64.5），在LongDocURL上提升18.5准确率（37.8→56.3），域外性能最高提升47.9%。此外，分析表明Doc-V*在证据选择效率（Page-F1）和长文档处理（>80页时准确率40.7，远超RAG的30.9）上具有显著优势，且对检索器质量依赖较低，体现了其主动补偿机制的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于实验设置和场景覆盖。首先，方法仅在单一视觉语言骨干模型（Qwen2.5-VL）上验证，未系统评估其在不同模型架构上的泛化能力。虽然框架设计是骨干无关的，但不同模型的视觉编码和语义理解能力差异可能影响智能体的导航与证据聚合行为，这需要跨骨干的消融实验来验证。其次，研究仅针对单文档VQA，未涉及多文档场景。在真实应用中，答案可能分散在多个异构文档中，这要求智能体具备跨文档的检索、去重和关联推理能力，是重要的扩展方向。

结合个人见解，未来可从三方面深入探索：一是增强智能体的规划与反思机制，当前框架依赖模仿学习，可引入强化学习或思维链提示，让智能体能动态调整搜索策略，处理更复杂的多跳推理问题。二是探索多模态工具的集成，如结合OCR工具处理特殊字体或公式，形成混合式解决方案，以兼顾精度与效率。三是研究计算效率的优化，特别是在长文档场景下，如何减少页面获取和推理的延迟，实现更高效的粗到细交互。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Doc-V*的免OCR智能体框架，用于解决多页文档视觉问答任务。其核心贡献在于将多页文档理解建模为一个从粗到精的主动证据聚合过程，以克服现有方法在容量与精度之间的权衡问题。具体方法上，Doc-V*首先通过缩略图概览进行粗粒度定位，然后通过语义检索和目标页面抓取进行主动导航，最后在结构化工作记忆中聚合证据以进行可追溯的推理。该框架通过模仿学习从专家轨迹中训练，并利用群体相对策略优化进行微调，从而在答案准确性和证据搜索效率之间取得平衡。实验结果表明，Doc-V*在五个基准测试上超越了开源基线，并接近专有模型性能，特别是在长文档和领域外文档上，其性能比检索增强生成基线提升了高达47.9%。主要结论是，这种选择性的证据聚合机制为固定上下文和检索增强方法提供了一种更鲁棒的替代方案。
