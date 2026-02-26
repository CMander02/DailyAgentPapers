---
title: "SurGo-R1: Benchmarking and Modeling Contextual Reasoning for Operative Zone in Surgical Video"
authors:
  - "Guanyi Qin"
  - "Xiaozhen Wang"
  - "Zhu Zhuo"
  - "Chang Han Low"
  - "Yuancan Xiao"
  - "Yibing Fu"
  - "Haofeng Liu"
  - "Kai Wang"
  - "Chunjiang Li"
  - "Yueming Jin"
date: "2026-02-25"
arxiv_id: "2602.21706"
arxiv_url: "https://arxiv.org/abs/2602.21706"
pdf_url: "https://arxiv.org/pdf/2602.21706v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Surgical AI"
  - "Contextual Reasoning"
  - "Vision-Language Models"
  - "Reinforcement Learning from Human Feedback"
  - "Benchmarking"
  - "Decision Support"
relevance_score: 5.5
---

# SurGo-R1: Benchmarking and Modeling Contextual Reasoning for Operative Zone in Surgical Video

## 原始摘要

Minimally invasive surgery has dramatically improved patient operative outcomes, yet identifying safe operative zones remains challenging in critical phases, requiring surgeons to integrate visual cues, procedural phase, and anatomical context under high cognitive load. Existing AI systems offer binary safety verification or static detection, ignoring the phase-dependent nature of intraoperative reasoning. We introduce ResGo, a benchmark of laparoscopic frames annotated with Go Zone bounding boxes and clinician-authored rationales covering phase, exposure quality reasoning, next action and risk reminder. We introduce evaluation metrics that treat correct grounding under incorrect phase as failures, revealing that most vision-language models cannot handle such tasks and perform poorly. We then present SurGo-R1, a model optimized via RLHF with a multi-turn phase-then-go architecture where the model first identifies the surgical phase, then generates reasoning and Go Zone coordinates conditioned on that context. On unseen procedures, SurGo-R1 achieves 76.6% phase accuracy, 32.7 mIoU, and 54.8% hardcore accuracy, a 6.6$\times$ improvement over the mainstream generalist VLMs. Code, model and benchmark will be available at https://github.com/jinlab-imvr/SurGo-R1

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决微创手术中安全操作区域（Go Zone）的智能识别与上下文推理问题。研究背景是，尽管微创手术改善了患者预后，但术中识别安全操作区域仍极具挑战，尤其在关键阶段，外科医生需在高认知负荷下整合视觉线索、手术阶段和解剖上下文。现有AI方法存在明显不足：它们多局限于二元安全验证（如判断是否达到“安全关键视图”）或静态检测，忽略了术中推理本质上依赖于手术阶段（phase-dependent），缺乏对动态上下文的理解，也无法提供可解释的、主动的决策支持。

因此，本文要解决的核心问题是：如何开发一个能够进行上下文感知推理的AI系统，使其不仅能准确定位手术视频中随时间变化的安全操作区域，还能像外科医生一样，结合当前手术阶段、暴露质量、风险提示和后续动作进行结构化、可解释的推理。为此，论文引入了ResGo基准数据集，它首次将Go Zone的空间定位框与临床医生撰写的、包含阶段、推理、下一步动作和风险提醒的理性标注配对。基于此，论文进一步提出了SurGo-R1模型，其采用“先识别阶段，再基于该上下文生成推理和坐标”的多轮架构，并通过强化学习优化，以实现对未见手术过程的泛化能力，从而超越现有通用视觉语言模型，提供更贴合实际手术需求的、安全感知的术中引导。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**手术安全智能**和**视觉语言模型与视觉定位**两大类。

在**手术安全智能**方面，相关研究旨在通过计算模型辅助外科医生识别安全操作区域。关键工作包括：1）**CVS框架及其自动化**：如DeepCVS实现了对关键视野安全标准的自动验证，LG-CVS通过图结构推理增强了鲁棒性；2）**基于区域（Zone-based）的范式**：将手术安全重新定义为安全与危险解剖区域的空间定位，并进行了专家验证。然而，这些现有方法多为**静态、固定输出**的系统，需要为每个目标类别提供显式标签，无法处理隐式的安全查询或提供基于知识的解释。

在**视觉语言模型与视觉定位**方面，通用视觉语言模型（VLMs）已在连接自然语言与视觉内容上取得进展。医学领域的适应工作主要集中在临床视觉问答（VQA），但通常**仅生成文本输出，缺乏空间定位能力**。视觉定位方法则从基于短语的定位，发展到能生成边界框的VLM集成方法。进一步的**推理定位**范式能够处理需要世界知识的隐式查询。然而，新兴的医学推理定位研究主要针对诊断成像，而非**手术过程指导**。

**本文工作与上述研究的区别与关系在于**：本文提出的SurGo基准和模型，首次将**推理定位**范式引入到**术中手术**领域。它要求模型在生成可解释文本响应的同时，定位安全解剖区域，并且其评估强调对手术阶段的依赖（阶段识别错误则定位视为失败）。这超越了现有手术安全系统（缺乏动态推理和解释能力）和通用医学VLMs（缺乏空间定位或针对手术阶段的理解），实现了**上下文感知的、可解释的术中安全区域推理**。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SurGo-R1的多模态推理框架来解决手术视频中安全操作区域（Go Zone）的上下文感知识别问题。其核心方法是设计了一个“先识别阶段，后推理定位”（phase-then-go）的两阶段架构，并利用基于强化学习的人类反馈（RLHF）技术，具体为GRPO（Group Relative Policy Optimization）进行优化。

**整体框架与主要模块：**
1.  **两阶段顺序推理流程**：模型被设计为进行两次“对话”（Turn）。在第一阶段（Turn 1），模型接收手术场景帧和候选阶段标签，通过一个多项选择题（MCQ）的形式，强制模型首先识别当前的手术阶段（如分离、止血等）。在第二阶段（Turn 2），模型基于第一阶段预测的阶段，进行Go Zone的推理和空间坐标定位。
2.  **阶段-定义映射工具（Phase-Definition Mapping Tool）**：这是一个关键的“智能体”工作流组件，作为中间监督器。在推理阶段，它根据模型预测的阶段$\hat{p}$，动态检索并注入该阶段对应的、包含手术约束的结构化定义$\mathcal{D}_{\hat{p}}$到提示中，为后续推理提供上下文。在训练阶段，该工具采用差异化策略：如果阶段预测错误，则使用真实阶段$y$对应的定义$\mathcal{D}_y$，以确保推理模块在正确的上下文中学习空间定位，从而将空间学习与上游分类噪声隔离。
3.  **复合奖励模型（Reward Modeling）**：模型使用GRPO进行优化，并设计了针对性的复合奖励函数。
    *   **阶段识别奖励**：使用严格的二元准确率奖励$\mathbf{R}_{acc}$，激励模型精确识别手术阶段。
    *   **推理奖励**：为了确保生成的临床理由符合标准，设计了一个基于语义实体匹配的轻量级奖励$\mathbf{R}_{reason}$。它使用scispaCy从真实理由中提取核心临床实体（如手术目标、操作、风险），并计算这些实体在模型生成理由中的召回率，引导模型融入关键临床概念。
    *   **定位奖励**：结合了两个奖励来监督Go Zone的坐标预测。一是标准的交并比奖励$\mathbf{R}_{IoU}$，用于边界对齐。二是引入的**中心距离奖励**$\mathbf{R}_{dist}$，它通过计算预测框与真实框中心点的距离并取负指数，提供了密集的监督信号。这在训练早期预测框与真实框无重叠时尤为重要，能防止梯度消失，引导模型向正确解剖区域移动，稳定了GRPO训练。

**创新点：**
1.  **阶段条件化推理架构**：提出的“phase-then-go”架构明确地将手术阶段识别作为空间推理的先决条件，模仿了外科医生的认知过程，解决了现有方法忽略阶段依赖性的问题。
2.  **训练与推理解耦的上下文注入机制**：阶段-定义映射工具在训练时纠正阶段错误以保证学习质量，在推理时则完全依赖模型自身预测，这种策略既强化了空间对齐，又训练了模型根据自预测上下文进行自适应推理的能力。
3.  **针对手术场景的复合奖励设计**：特别是中心距离奖励的引入，有效解决了手术定位任务中因初始预测不准导致的零奖励和梯度问题，是模型能在具有挑战性的文本到图像定位任务上取得显著性能提升的关键技术之一。
4.  **高效的语义监督**：采用基于实体提取的轻量级推理奖励，替代计算开销大的基于LLM的奖励模型，在保证临床语义对齐的同时提升了训练效率。

通过这一系列设计，SurGo-R1在未见过的术式上实现了76.6%的阶段识别准确率、32.7%的mIoU以及54.8%的硬核准确率，相比主流通用视觉语言模型有显著提升。

### Q4: 论文做了哪些实验？

论文的实验主要包括基准测试、模型性能评估和消融研究。实验设置严格遵循“先识别手术阶段，再定位安全区域”的分层框架，并使用定义工具确保推理过程的结构一致性。

在数据集和基准测试方面，研究使用了新提出的ResGo数据集，该数据集包含标注了“Go Zone”边界框和临床医生撰写的推理依据的腹腔镜手术视频帧。评估指标包括阶段识别准确率、定位准确率（Acc@0.25）、中心点误差（Δcen↓）、平均交并比（mIoU）以及严格评估下的准确率（HA0.25）和mIoU（HmIoU）。其中，严格评估要求阶段识别和区域定位必须同时正确。

对比方法包括主流的通用视觉语言模型（VLMs）以及单轮推理的基线模型。主要结果显示，现有通用和专用模型在将手术阶段知识与安全区域定位对齐方面存在显著缺陷。而提出的SurGo-R1模型在未见过的病例上取得了显著提升：手术阶段准确率达到76.6%，mIoU为32.7%，严格准确率（HA0.25）为54.8%。与主流通用VLMs相比，SurGo-R1在严格准确率上实现了6.6倍的提升。

消融实验验证了各个组件的有效性。引入距离奖励（R_dist）和阶段定义映射工具（Def-Tool）均能提升性能，尤其是后者通过基于阶段检索解剖定义，有效弥合了视觉特征与医学知识之间的语义鸿沟。此外，多轮架构（阶段识别后生成推理和坐标）在各项指标上均优于单轮基线（后者同时处理阶段和定位），例如阶段准确率从69.5%提升至76.6%，严格准确率从49.6%提升至54.8%。针对推理奖励（R_reason）的消融显示，包含该奖励的模型在临床医生的盲审中获得了79.9%的选择率和52.5%的准确率评分，显著优于未包含的版本（17.3%， 47.2%）和基线模型Qwen3-VL（0.27%， 10.7%）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，当前模型主要针对胆囊切除术，其泛化能力有待验证。未来可扩展至更多术式（如胃肠、妇科手术），并纳入更复杂、多变的解剖结构和病理状况，以测试模型的普适性。其次，模型依赖人工标注的“安全区域”和临床推理，这受限于标注者的主观经验。未来可探索半监督或自监督学习，利用大量未标注手术视频数据，或结合术中实时生理信号（如出血量、组织弹性）进行多模态融合，使安全区域判断更客观、动态。此外，当前评估指标虽强调阶段依赖性，但未充分考虑手术流程的时序连贯性。可引入时间序列建模（如Transformer或LSTM），使模型能基于历史帧信息进行前瞻性风险预测，而不仅是单帧分析。最后，模型部署的实时性与计算效率也是关键。未来需优化轻量级架构，并探索模型在机器人辅助手术中的实时交互应用，如与手术导航系统集成，提供即时、可操作的临床决策支持。

### Q6: 总结一下论文的主要内容

该论文针对微创手术中安全操作区域识别这一关键挑战，提出了一个名为SurGo-R1的基准测试和模型。核心问题是现有AI系统仅提供静态或二值化安全验证，忽略了手术阶段依赖的上下文推理。为此，作者首先构建了ResGo基准，包含标注了“可操作区域”边界框和临床医生撰写的多维度推理（如手术阶段、暴露质量、下一步动作和风险提示）的腹腔镜视频帧。

论文的主要贡献是提出了SurGo-R1模型。该方法采用强化学习人类反馈优化的多阶段架构：模型首先识别手术阶段，然后基于该阶段上下文生成推理并预测可操作区域坐标。这种“先阶段，后区域”的设计强制模型进行条件推理。

主要结论显示，现有通用视觉语言模型在此任务上表现不佳。而SurGo-R1在未见过的术式上取得了显著提升，其阶段识别准确率达76.6%，区域预测的mIoU为32.7%，在严格评估指标“硬核准确率”上达到54.8%，比主流通用模型提升了6.6倍。这项工作强调了上下文推理在手术AI中的重要性，并为该领域提供了首个专注于动态、阶段感知操作区域识别的基准和专用模型。
