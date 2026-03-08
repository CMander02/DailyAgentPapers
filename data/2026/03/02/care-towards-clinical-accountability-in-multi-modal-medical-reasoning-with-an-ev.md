---
title: "CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework"
authors:
  - "Yuexi Du"
  - "Jinglu Wang"
  - "Shujie Liu"
  - "Nicha C. Dvornek"
  - "Yan Lu"
date: "2026-03-02"
arxiv_id: "2603.01607"
arxiv_url: "https://arxiv.org/abs/2603.01607"
pdf_url: "https://arxiv.org/pdf/2603.01607v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "Healthcare & Bio"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "CARE (Clinical Accountability in multi-modal medical Reasoning with an Evidence-grounded agentic framework)"
  primary_benchmark: "standard medical VQA benchmarks"
---

# CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework

## 原始摘要

Large visual language models (VLMs) have shown strong multi-modal medical reasoning ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert visual grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both reasoning accuracy and trust. In this paper, we introduce CARE, advancing Clinical Accountability in multi-modal medical Reasoning with an Evidence-grounded agentic framework. Unlike existing approaches that couple grounding and reasoning within a single generalist model, CARE decomposes the task into coordinated sub-modules to reduce shortcut learning and hallucination: a compact VLM proposes relevant medical entities; an expert entity-referring segmentation model produces pixel-level ROI evidence; and a grounded VLM reasons over the full image augmented by ROI hints. The VLMs are optimized with reinforcement learning with verifiable rewards to align answers with supporting evidence. Furthermore, a VLM coordinator plans tool invocation and reviews evidence-answer consistency, providing agentic control and final verification. Evaluated on standard medical VQA benchmarks, our CARE-Flow (coordinator-free) improves average accuracy by 10.9% over the same size (10B) state-of-the-art (SOTA). With dynamic planning and answer review, our CARE-Coord yields a further gain, outperforming the heavily pre-trained SOTA by 5.2%. Our experiments demonstrate that an agentic framework that emulates clinical workflows, incorporating decoupled specialized models and explicit evidence, yields more accurate and accountable medical AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态医疗推理中存在的临床可问责性不足的问题。研究背景是，尽管大型视觉语言模型在医疗图像理解和视觉问答任务上表现出色，但现有方法大多采用端到端的“黑箱”式推理，直接将图像和文本映射到答案，缺乏对支持性视觉证据的显式定位和验证。这种设计与临床医生基于证据、分阶段的工作流程相悖，容易导致模型学习捷径和产生幻觉，特别是在数据分布变化时，因为细粒度、病例相关的证据既未被检索也未在推理中被要求使用。

现有方法的不足主要体现在三个方面：一是大多数视觉语言模型以单次、整体的方式运作，未显式定位或验证支持答案的视觉发现，削弱了临床可靠性和可问责性；二是一些工作虽然增加了视觉定位模块，但通常将其视为孤立的感知头，其输出未被充分反馈到推理过程中；三是近期通用领域视觉问答中出现的将定位与推理耦合在单一通用模型内的方法，需要高质量配对数据和昂贵的强化学习来稳定工具使用，且在数据稀缺时性能下降，同时基于视觉语言模型的定位常遗漏微小但临床显著的发现，而耦合设计还会放大错误传播，导致早期定位错误影响后续推理。

因此，本文要解决的核心问题是：如何构建一个模拟临床工作流程、具有明确证据基础的智能体框架，以提升多模态医疗推理的准确性和临床可问责性。具体而言，论文提出了CARE框架，通过解耦专门化模块（包括医疗实体提议、实体指代分割和证据接地的视觉问答）并引入动态协调器进行工具调用规划和答案审查，从而减少捷径学习和幻觉，确保推理基于可靠的像素级证据，最终实现更准确、更可问责的医疗人工智能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**中，相关工作包括：1）**医学多模态大语言模型**：现有通用视觉语言模型缺乏医学知识，早期模型数据质量低，近期工作虽利用更好数据和强化学习，但多为单步黑箱，易产生幻觉；本文则通过解耦的智能体框架，引入显式视觉证据提升可问责性。2）**基于视觉定位的模型**：现有研究将定位视为辅助多任务优化，且依赖大规模细粒度标注数据进行监督微调；本文则将定位证据作为下游推理的支持，专门训练模型利用局部视觉线索，提升性能。3）**视觉语言推理方法**：自思维链提出后，多种方法（如RLVR）推动了推理发展，但现有方法常计算昂贵或需高质量人工标注数据；本文以模型生成的视觉线索作为直接输入，降低了数据依赖。

在**应用类**中，已有工作探索了智能体流程或工具使用，但通常缺乏视觉证据支持诊断可靠性；本文通过模拟临床工作流，协调专用模块，实现了更准确、可追溯的医学推理。

本文与这些工作的核心区别在于：**摒弃了单一通用模型的耦合设计，采用解耦的专家模块协同框架，强调证据驱动的推理与智能体控制，从而在提升准确性的同时增强了临床可问责性**。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CARE的、基于证据的智能体化框架来解决多模态医学推理中临床可问责性不足的问题。其核心方法是模仿临床分阶段、基于证据的工作流程，将复杂的端到端黑箱任务分解为多个协调的、专门化的子模块，并通过强化学习优化各模块与证据的一致性。

**整体框架与主要模块**：CARE框架包含三个核心专家模型和一个可选的协调器。处理流程始于**医学实体提议模块**，这是一个经过强化学习微调的紧凑视觉语言模型（VLM），其职责是根据用户问题，提出图像中相关的解剖结构或发现（即“医学实体”）。接着，**实体指代分割模型**接收提议的实体，利用一个基于SAM架构的专家模型进行像素级的精准定位，生成高质量的区域兴趣（ROI）掩码作为显式视觉证据。最后，**证据接地的视觉问答（EG-VQA）模型**以原始图像和经过处理的视觉证据（如局部放大图、掩码或全局指示符）作为输入，进行最终推理并生成答案。为了提升流程的智能性和可靠性，论文引入了**VLM协调器**，它负责动态规划工具调用序列、选择最具信息量的证据视图，并在最终确定前对推理链和答案的一致性进行迭代审查。

**关键技术细节与创新点**：1) **任务解耦与专业化**：与将定位和推理耦合在单一通用模型中的现有方法不同，CARE将任务分解为独立的、各司其职的专家模块。这种设计减少了模型走捷径学习和产生幻觉的风险，因为每个模块专注于其最擅长的子任务（如精准分割或复杂推理），且后续模块可以基于前一步提供的显式证据进行独立验证。2) **证据表示与融合**：EG-VQA模型设计了三种临床导向的证据表示方式——局部放大、掩码提示和全局视图，以适应不同类型的问题，同时避免直接覆盖掩码可能破坏医学图像原有物理意义（如像素值和对比度）的问题。3) **基于强化学习的可验证对齐**：论文采用带可验证奖励的强化学习（RLVR）对实体提议和EG-VQA两个VLM进行微调。创新性地，对于实体提议任务，奖励函数不仅包含准确性，还引入了基于嵌入相似度的语义匹配奖励、实体数量奖励和重复惩罚，这有助于模型在合成数据上训练后能更好地泛化到真实用户问题。4) **智能体化协调与审查**：协调器的引入是框架的另一大创新。它使系统从静态流水线（CARE-Flow）升级为动态智能体（CARE-Coord）。协调器不仅能优化工具调用效率（例如，对于全局性问题跳过分割步骤），还能执行迭代的“思维链-答案”审查，确保内部推理逻辑与最终答案一致，从而在模型规模有限的情况下进一步提升答案的可信度和准确性。

### Q4: 论文做了哪些实验？

论文在四个标准医学视觉问答（VQA）基准上进行了实验，包括OmniMedVQA、VQA-RAD、SLAKE（用于域内评估）和VQA-Med-2019（用于域外评估）。实验设置方面，CARE框架包含三个核心模块：一个基于InternVL3-2B的实体提议VLM、一个基于SA-Med-2D（600M参数）的专家分割模型，以及一个基于InternVL3-2B/8B的基于证据的VQA VLM。整体参数规模分别为4B（CARE-Flow-S）和10B（CARE-Flow-B）。此外，还引入了基于GPT-5的协调器进行动态规划和答案审查（CARE-Coord）。

对比方法包括：1）专有模型（GPT-4o、GPT-5）；2）通用VLM（Llama-3.2 Vision、Qwen2.5-VL、InternVL3、DeepEyes）；3）医学专用VLM（LLaVA-Med、medgemma、HuatuoGPT-Vision、Lingshu、MedVLm-R1-2B）；4）分割模型（RecLMIS、LISA、MedPLIB、UniBiomed、BiomedParse）。

主要结果显示：1）CARE-Flow（无协调器）在整体准确率上比同等规模（10B）的SOTA模型平均提升10.9%。2）加入协调器动态规划与审查的CARE-Coord进一步带来增益，整体准确率达77.5%，比经过大量预训练的SOTA模型高出5.2%。关键数据指标：在ID数据集（OMVQA、VQA-RAD、SLAKE）上，CARE-Coord平均准确率为83.1%；在OOD数据集（VQA-Med-2019）上为60.8%。消融实验证实，使用分割掩码、局部放大和全局图像作为视觉线索进行训练，并结合协调器进行证据审查，能带来最大性能提升（整体准确率相对基线提升5.1%）。此外，论文提出的分割模型在MeCo-G数据集上的平均Dice分数达到81.9%，优于其他对比模型。

### Q5: 有什么可以进一步探索的点？

该论文提出的CARE框架在提升可解释性和准确性方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，框架依赖多个独立模块（如实体提取、分割和推理模型），这可能导致系统延迟较高，在实时临床场景中的应用受限。未来可研究更轻量化的模块集成或知识蒸馏技术，以平衡效率与性能。其次，当前证据生成主要基于视觉区域（ROIs），而临床决策常需结合文本报告、病史等多模态时序数据。扩展框架以融合动态时序信息和跨模态对齐，能更好地模拟真实工作流。此外，强化学习的奖励函数基于可验证证据，但医疗标注成本高昂且存在主观差异。未来可探索半监督或自监督学习，利用未标注数据提升泛化能力。最后，框架的“问责性”仍停留在技术层面，如何将证据链转化为符合临床法规的审计轨迹，并与医疗伦理框架结合，是推动实际落地的关键。

### Q6: 总结一下论文的主要内容

该论文针对多模态医疗推理中临床可问责性不足的问题，提出了CARE框架，旨在通过证据驱动的智能体架构模拟临床分阶段工作流。核心贡献在于将传统端到端的黑箱模型分解为协同的专用子模块，以减少捷径学习和幻觉。具体方法包括：首先由紧凑的视觉语言模型提出相关医疗实体；接着由专家级实体指代分割模型生成像素级的感兴趣区域证据；然后由基于证据的视觉语言模型结合全图像和区域提示进行推理；最后通过强化学习优化模型，使其答案与支持证据对齐。此外，引入视觉语言模型协调器动态规划工具调用并审查证据与答案的一致性，实现智能体控制和最终验证。实验表明，该框架在标准医疗视觉问答基准上显著提升了准确性和可问责性，其中基础版本比同规模先进模型平均准确率提升10.9%，而带协调器的版本进一步超越大规模预训练先进模型5.2%，验证了分解工作流与显式证据结合的有效性。
