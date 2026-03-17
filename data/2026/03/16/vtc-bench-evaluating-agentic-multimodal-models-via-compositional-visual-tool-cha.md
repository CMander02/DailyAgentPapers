---
title: "VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining"
authors:
  - "Xuanyu Zhu"
  - "Yuhao Dong"
  - "Rundong Wang"
  - "Yang Shi"
  - "Zhipeng Wu"
  - "Yinlun Peng"
  - "YiFan Zhang"
  - "Yihang Lou"
  - "Yuanxing Zhang"
  - "Ziwei Liu"
  - "Yan Bai"
  - "Yuan Zhou"
date: "2026-03-16"
arxiv_id: "2603.15030"
arxiv_url: "https://arxiv.org/abs/2603.15030"
pdf_url: "https://arxiv.org/pdf/2603.15030v1"
categories:
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "多模态Agent"
  - "工具使用"
  - "视觉工具链"
  - "规划与执行"
  - "OpenCV"
  - "MLLM"
relevance_score: 9.0
---

# VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining

## 原始摘要

Recent advancements extend Multimodal Large Language Models (MLLMs) beyond standard visual question answering to utilizing external tools for advanced visual tasks. Despite this progress, precisely executing and effectively composing diverse tools for complex tasks remain persistent bottleneck. Constrained by sparse tool-sets and simple tool-use trajectories, existing benchmarks fail to capture complex and diverse tool interactions, falling short in evaluating model performance under practical, real-world conditions. To bridge this gap, we introduce VisualToolChain-Bench~(VTC-Bench), a comprehensive benchmark designed to evaluate tool-use proficiency in MLLMs. To align with realistic computer vision pipelines, our framework features 32 diverse OpenCV-based visual operations. This rich tool-set enables extensive combinations, allowing VTC-Bench to rigorously assess multi-tool composition and long-horizon, multi-step plan execution. For precise evaluation, we provide 680 curated problems structured across a nine-category cognitive hierarchy, each with ground-truth execution trajectories. Extensive experiments on 19 leading MLLMs reveal critical limitations in current models' visual agentic capabilities. Specifically, models struggle to adapt to diverse tool-sets and generalize to unseen operations, with the leading model Gemini-3.0-Pro only achieving 51\% on our benchmark. Furthermore, multi-tool composition remains a persistent challenge. When facing complex tasks, models struggle to formulate efficient execution plans, relying heavily on a narrow, suboptimal subset of familiar functions rather than selecting the optimal tools. By identifying these fundamental challenges, VTC-Bench establishes a rigorous baseline to guide the development of more generalized visual agentic models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在作为智能体使用外部视觉工具时，评估体系不足的核心问题。研究背景是，随着MLLMs的发展，它们已从基础的视觉问答扩展到能够调用外部工具来完成高级视觉任务，展现出“智能体”的潜力。然而，现有的评估基准存在明显不足：它们通常依赖有限的工具集和简单的单一工具调用，无法捕捉现实应用中所需的、复杂多样的工具组合与多步骤规划执行。这使得现有基准难以真实反映模型在实际复杂场景下的工具使用能力，也无法有效指导更强大、可靠的视觉智能体的研发。

因此，本文要解决的核心问题是：如何构建一个全面、严谨的基准，以评估MLLMs在复杂、组合性视觉工具使用方面的熟练度。具体而言，论文引入了VTC-Bench，它通过集成32种基于OpenCV的多样化视觉操作来模拟真实的计算机视觉流程，从而支持对多工具组合和长视野、多步骤规划执行的严格评估。该基准包含了680个精心设计的问题，并配有真实的执行轨迹，旨在系统性地暴露当前模型在适应多样化工具集、泛化到未见操作、以及进行高效多工具组合规划等方面的根本性挑战，为未来开发更具通用性的视觉智能体模型确立一个坚实的评估基线。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：视觉智能体模型和智能体评测基准。

在**视觉智能体模型**方面，早期研究主要协调外部视觉专家或固定API进行基础视觉分析。为了增强感知，采用了交互式注意力机制（如主动缩放和视觉掩码）来优化输入。最近的强化学习方法针对特定工具集优化了这些策略。然而，这些方法依赖固定的视觉解析器集合，限制了泛化能力。程序化视觉操作（如使用Python代码作为基础工具）解决了这一局限，允许按需构建包含复杂逻辑的工具。先进框架能动态生成代码进行针对性视觉编辑，而Thyme则为开源工具使用模型提供代码测试。当前领先模型（如GPT系列）已利用代码执行来动态构建任务特定工具。

在**智能体评测基准**方面，标准的多模态大模型评测主要关注静态感知和推理。早期研究引入主动视觉探索任务，但仅测试裁剪、缩放等基本操作。近期研究评估多模态智能体推理、图像处理能力以及组合多种工具完成开放式视觉任务。然而，现有基准（如GTA、TIR-Bench、Agent-X、VisualToolBench、AgentVista）普遍受限于工具库规模较小，缺乏对组合式多工具推理的系统性要求，且未能捕捉实际应用的复杂需求。

**本文工作（VTC-Bench）与这些研究的区别在于**：它提供了一个包含32种多样化工具（基于OpenCV）的丰富工具集，支持代码和接口双重交互范式，并设计了680个需要多步骤工具组合的问题，以严格评估模型的长视野、多步骤执行计划能力以及工具间的严格功能依赖关系。相比之下，现有基准在工具数量、多工具组合、长序列调用和功能依赖等方面均存在不足，而VTC-Bench在这些维度上进行了全面覆盖，旨在更贴近真实计算机视觉流程的复杂需求。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为VTC-Bench的综合性基准测试来解决评估多模态大语言模型（MLLMs）在复杂、组合式工具使用方面的能力瓶颈问题。其核心方法是设计一个结构化、层次化的评估框架，以模拟真实世界的计算机视觉处理流程，从而系统性地诊断模型在工具调用、组合和长程规划中的缺陷。

**整体框架与架构设计**：
VTC-Bench的整体框架围绕一个**三层认知层次结构**构建，包含9个具体任务，旨在评估模型从基础感知到高级推理的完整能力谱系。这三级分别是：1) **视觉感知增强**（如鲁棒OCR、感知恢复），要求模型使用工具处理环境干扰；2) **定量视觉估计**（如测量、颜色、计数），评估模型量化物理属性的能力；3) **组合视觉推理**（如图表、数学、空间推理），测试模型通过多步骤工具编排进行复杂逻辑推导的能力。这种分层设计确保了评估的全面性和渐进性。

**主要模块与关键技术**：
1.  **丰富的工具集**：为了解决现有基准测试工具稀疏的问题，论文精心策划了一个包含**32个基于OpenCV的视觉操作**的工具集。这些工具被组织成四个功能模块：**几何**（空间变换）、**增强**（信号优化）、**特征提取**（结构语义基元获取）和**绘制**（推理验证与属性量化）。这个设计模拟了标准的人类认知流程（恢复、提炼、验证），并为模型提供了广泛且可控的操作选项。
2.  **精心构建的数据集**：论文通过结合网络爬取图像和开源数据集，构建了包含**680个高质量问题**的数据集。每个问题都配有**人工标注的真实执行轨迹（参考工具链）**，平均链长为5.04步，涉及4.97个独特工具，体现了任务的高复杂性。数据构建引入了可控的视觉扰动（如几何畸变），迫使模型必须进行主动的工具链规划，而非被动识别。
3.  **严格的验证协议**：采用多阶段人工与模型（如Gemini-3.0-Pro）结合的验证流程，确保问题、答案及参考工具链的准确性和可靠性。
4.  **多维度的评估指标**：除了整体的平均通过率（APR），论文还设计了多个细粒度指标来深入分析工具使用行为：**工具调用率（TCR）** 衡量模型调用工具的倾向；**平均绝对误差（MAE）** 量化预测工具链与真实链的长度差异；**工具使用效率（Eff_tool）** 评估工具调用序列的精确性和简洁性。这些指标共同提供了对模型“代理能力”的深入洞察。

**创新点**：
1.  **系统性评估维度**：首次通过一个统一的、基于认知层次的基准，系统评估MLLMs在**多工具组合**和**长视野、多步骤规划**方面的能力，超越了以往仅关注单一或简单工具使用的评测。
2.  **与现实流程对齐的工具集设计**：工具集的选取和模块划分紧密对齐实际计算机视觉流水线，使得评估更具现实意义。
3.  **诊断性分析能力**：通过提供每个问题的真实工具链和一系列细粒度指标，VTC-Bench不仅能给出性能分数，更能**诊断模型失败的具体原因**（如工具选择不当、规划效率低下、泛化到未见工具困难等），从而为未来模型开发提供明确的改进方向。实验结果表明，即使是领先的模型（如Gemini-3.0-Pro）在该基准上也仅达到51%的通过率，凸显了当前视觉代理模型面临的严峻挑战。

### Q4: 论文做了哪些实验？

论文对19个主流多模态大语言模型（MLLMs）进行了全面评估，包括GPT系列、Gemini系列以及Qwen3-VL等开源模型。实验设置上，研究采用VTC-Bench基准，该基准包含基于OpenCV的32种视觉操作工具和680个精心构建的问题，这些问题按九级认知层次分类并带有真实执行轨迹。评估框架比较了直接回答基线与工具增强推理（分为接口驱动和代码驱动两种范式）的性能，并使用Qwen-Agent和Thyme框架来管理工具调用。评估方法结合了基于规则的确定性匹配和GPT-4o作为评判的LLM-as-a-Judge协议。

主要结果如下：所有模型在基准设置下表现均不理想，得分在22.06%到46.47%之间，Gemini-3.0-Flash以46.47%获得最高基础分。在工具增强后，Gemini-3.0-Pro取得了最高总体得分51.18%。专有模型显著优于开源模型，例如GPT-4o在接口设置下实现了+9.56%的性能提升。关键指标包括平均通过率（APR）、工具调用率（TCR）和工具使用效率（Eff.）。分析显示，工具调用率与平均通过率呈正相关，但模型在工具组合和多步骤执行上存在效率低下问题，例如GPT-5.2的效率仅为16.78%，其平均绝对误差（MAE）高达9.96。此外，模型倾向于频繁使用少数简单工具（如缩放、旋转），而在面对复杂任务时难以制定高效的执行计划，揭示了当前模型在视觉代理能力上的根本局限。

### Q5: 有什么可以进一步探索的点？

该论文提出的VTC-Bench在评估多模态智能体的工具链能力方面迈出了重要一步，但仍存在一些局限性和值得深入探索的方向。首先，基准测试主要基于OpenCV的32种视觉操作，虽然多样，但未能涵盖更广泛的现实工具类型（如专业图像编辑软件、3D建模工具或领域专用API），未来可扩展工具集以测试模型在跨领域、异构工具环境下的适应能力。其次，评估侧重于已知工具的组合执行，但对零样本工具学习、工具动态发现与接口理解的能力考察不足，这限制了智能体在开放世界中的实际应用潜力。此外，当前基准的问题生成依赖人工设计，未来可引入自动化或交互式任务生成机制，以模拟更复杂、动态的用户需求。从模型改进角度看，研究可探索更强大的工具抽象与规划架构，例如引入分层规划、元工具学习或基于强化学习的工具选择策略，以提升模型在长视野、多步骤任务中的决策效率和泛化能力。最后，将评估从静态图像扩展到视频流、3D场景或多模态实时交互环境，将进一步推动视觉智能体向实用化发展。

### Q6: 总结一下论文的主要内容

这篇论文提出了VTC-Bench，一个用于评估多模态大语言模型（MLLMs）工具使用能力的综合性基准测试。核心问题是现有基准受限于工具集稀疏和工具使用轨迹简单，无法捕捉复杂多样的工具交互，难以评估模型在真实复杂任务下的表现。

为此，论文构建了一个包含32种基于OpenCV的多样化视觉操作工具集，支持广泛的工具组合，以严格评估多工具组合和长视野、多步骤的计划执行能力。方法上，VTC-Bench精心设计了涵盖九类认知层次的680个问题，每个都提供了真实执行轨迹作为标准答案。

主要结论是，通过对19个领先MLLMs的广泛实验，揭示了当前模型在视觉智能体能力上的严重局限：模型难以适应多样化工具集并泛化到未见过的操作（最佳模型Gemini-3.0-Pro准确率仅51%）；多工具组合是持续挑战，面对复杂任务时，模型难以制定高效执行计划，严重依赖熟悉但次优的狭窄工具子集，而非选择最优工具。VTC-Bench通过识别这些根本性挑战，为开发更通用的视觉智能体模型建立了严格的基线。
