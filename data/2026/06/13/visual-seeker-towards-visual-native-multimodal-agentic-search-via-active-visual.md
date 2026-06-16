---
title: "Visual-Seeker: Towards Visual-Native Multimodal Agentic Search via Active Visual Reasoning"
authors:
  - "Zhengbo Zhang"
  - "Changtao Miao"
  - "Jinbo Su"
  - "Zhaowen Zhou"
  - "Chunxia Zhang"
  - "Xukai Wang"
  - "Ruiqi Liu"
  - "Kaiyuan Zheng"
  - "Jiansheng Cai"
  - "Bo Zhang"
  - "Zhe Li"
  - "Shiming Xiang"
  - "Ying Yan"
date: "2026-06-13"
arxiv_id: "2606.15231"
arxiv_url: "https://arxiv.org/abs/2606.15231"
pdf_url: "https://arxiv.org/pdf/2606.15231v1"
github_url: "https://github.com/ZhengboZhang/Visual-Seeker"
categories:
  - "cs.AI"
tags:
  - "Multimodal Agent"
  - "Visual Reasoning"
  - "Deep Search"
  - "Agentic Search"
  - "Data Synthesis"
  - "Multimodal Large Language Model"
  - "Tool Use"
relevance_score: 9.5
---

# Visual-Seeker: Towards Visual-Native Multimodal Agentic Search via Active Visual Reasoning

## 原始摘要

Multimodal large language models (MLLMs) have demonstrated impressive capabilities in many visual tasks, but they often struggle with factual grounding when confronted with complex, open-world scenarios. While recent multimodal deep search agents attempt to address this issue by utilizing external tools, the visual-native search paradigm remains underexplored. Existing methods primarily rely on simple images with explicit semantics and text-only evidence trajectories, limiting the agent's ability to perform multi-hop, cross-modal reasoning and search. To address these limitations, we propose Visual-Seeker, a visual-native multimodal deep search agent via active visual reasoning. Rather than treating vision as a static input, our agent actively attends to fine-grained visual details, dynamically harvests visual evidence throughout the search process. To unlock its visual-native potential, we design an active visual reasoning data pipeline and synthesize 5K high-quality multimodal trajectories for model training. Extensive experiments demonstrate the state-of-the-art performance across five challenging multimodal search benchmarks, even surpassing several proprietary models, validating robust visual-native reasoning and search in real-world web environments. The code and data can be accessed at: https://github.com/ZhengboZhang/Visual-Seeker.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有多模态大模型（MLLMs）在面对复杂开放世界场景时的事实性根基不足问题，特别是多模态深度搜索代理在视觉原生能力上的缺失。当前方法存在两个主要局限：一是训练数据多使用包含显式语义的简单图像，缺乏复杂背景和多实体场景，导致模型视觉感知能力训练不足；二是搜索过程仅依赖文本证据轨迹，视觉信息仅作为查询输入的辅助模态，而非主动收集和推理视觉证据，限制了代理进行多跳、跨模态推理和搜索的能力。因此，本文提出Visual-Seeker，一个通过主动视觉推理实现视觉原生多模态深度搜索的代理。核心目标是让代理不仅仅将视觉作为静态输入，而是能够主动关注细粒度视觉细节，在搜索过程中动态采集视觉证据，并在复杂现实世界环境中进行鲁棒的视觉原生推理与搜索。为此，作者设计了一个主动视觉推理数据合成流程，生成了5K高质量多模态轨迹用于模型训练，以弥合被动视觉感知与主动跨模态搜索之间的鸿沟。

### Q2: 有哪些相关研究？

主要相关研究可分为三类：

**1. 文本深度搜索代理**：如Text-only Deep Search Agents，将信息检索转化为迭代推理与工具调用循环，使LLM能自主生成查询和浏览网页。本文与其区别在于，这些方法局限于文本查询和文档检索，无法利用多模态感官数据，而Visual-Seeker将视觉作为主动推理的核心。

**2. 多模态深度搜索代理**：早期工作为代理配备反向图像搜索工具获取图像语义信息，结合文本QA与实体视觉查询生成微调数据。近期工作引入图像裁剪工具，利用视觉定位能力检索目标实体以减少背景干扰。本文指出这些方法在构建真实世界复杂多实体图像的视觉查询、以及将视觉证据纳入搜索必要路径方面存在局限。

**3. 视觉推理方法**：现有方法将视觉视为静态输入，依赖简单图像与纯文本证据轨迹。本文提出主动视觉推理范式，让代理在搜索过程中动态关注细粒度视觉细节并收集视觉证据，通过合成的5K高质量多模态轨迹激活视觉原生能力。

相比现有工作，Visual-Seeker首次系统性地实现了视觉原生的多跳跨模态搜索，在五个基准上超越包括专有模型在内的现有方法。

### Q3: 论文如何解决这个问题？

该论文通过提出Visual-Seeker，一种视觉原生多模态深度搜索智能体，以解决现有方法在复杂多模态搜索中视觉推理能力不足的问题。核心是利用主动视觉推理（Active Visual Reasoning）实现动态视觉证据采集。

整体框架基于ReAct循环架构，智能体与外部工具（文本搜索、反向图像搜索、图像搜索、网页访问、图像裁剪）进行多轮交互。关键技术包括：1) **主动视觉推理数据合成管道**（核心创新）：先从多实体图像中提取种子实体（结合视觉和文本线索进行命名实体识别、过滤与消歧），再在维基百科知识图谱上通过两种策略（回溯策略生成树状结构、循环约束策略确保路径多样性）进行随机游走，以生成非线性、多跳推理轨迹。随后利用LLM生成基于子图的问答对。2) **视觉证据注入**（另一创新）：为强制智能体进行视觉搜索和像素级推理，管道将答案实体的视觉属性（如颜色、空间布局）以两跳问答形式注入轨迹，并生成相应搜索关键词，驱动模型调用`search_image`工具获取图像并进行主动视觉证据采集。这使训练数据中`search_image`工具调用比例显著提升。3) **监督微调训练**：使用Claude-4.6-Opus作为教师模型，基于该管道合成的5,000条高质量多模态深搜轨迹（含视觉证据注入和纯文本实例）进行冷启动监督微调，训练模型学习多轮工具调用和主动收集视觉-文本证据的模式。

### Q4: 论文做了哪些实验？

论文在五个挑战性的多模态智能搜索基准上进行了广泛实验：MMSearch、MMSearch-Plus、BrowseComp-VL、MM-BrowseComp和VisBrowse-Bench。对比方法包括三类：直接回答（如GPT-5、Gemini-2.5系列、Claude-4-Sonnet、Qwen3-VL-8B-Instruct）、智能体工作流（同样模型配合工具使用）和多模态深度搜索智能体（如MMSearch-R1-7B、WebWatcher-7B/32B、DeepEyesV2-7B等）。主要结果以准确率（%）为指标，使用Qwen3-235B-A22B-Instruct作为评判模型。Visual-Seeker在五个基准上平均准确率为39.6%，超越所有现有开源多模态深度搜索智能体，甚至优于GPT-5（37.5%）和Gemini-2.5-Pro（37.1%）等闭源模型。相较于基模型Qwen3-VL-8B-Instruct（智能体工作流为23.0%），每个基准性能几乎翻倍（如MMSearch提升18.4%，MM-BrowseComp提升9.4%）。消融实验证明：数据合成流水线引入视觉证据后，MMSearch-Plus性能提升17.2%，MM-BrowseComp和VisBrowse显著改善；工具消融显示，移除image_crop或search_image工具后，VisBrowse基准准确率分别下降9.6%和14.6%；工具使用分析表明，模型交互轮次从简单基准的4.3圈到复杂基准的14.1圈，且VisBrowse中reverse_image_search和search_image工具调用频率更高。

### Q5: 有什么可以进一步探索的点？

该论文提出的Visual-Seeker虽然实现了视觉原生搜索，但仍存在几个可进一步探索的方向。首先，其数据合成管道依赖于预定义的多实体图像和人工注入视觉证据，可能限制了模型在更复杂、动态的真实场景中的泛化能力。未来可探索使用强化学习或对抗生成网络自动生成更多样化的视觉推理轨迹。其次，当前方法主要关注静态图像中的实体感知，尚未充分利用视频或动态环境中的时序视觉信息。整合时序推理能力将是重要扩展点。此外，模型在跨模态证据融合时可能仍存在模态偏差，可考虑引入更细粒度的注意力机制或对比学习来平衡文本与视觉线索的权重。最后，当前基准测试主要针对英文场景，评估多语言、跨文化图像中的视觉搜索能力将更具挑战性。通过构建多语言多模态训练数据，或采用迁移学习策略，有望提升模型的跨文化适应性。

### Q6: 总结一下论文的主要内容

现有搜索代理主要依赖文本，视觉仅作为被动输入，导致在多跳、跨模态推理中表现不佳。为克服这一局限，论文提出Visual-Seeker，一种通过主动视觉推理实现视觉原生多模态深度搜索的智能体。其核心创新在于将视觉从静态输入转变为主动探索源：智能体在搜索过程中动态关注细粒度视觉细节，主动收集视觉证据，并利用合成数据管道生成了5000条高质量的多模态训练轨迹。在五个具有挑战性的多模态搜索基准上的实验表明，Visual-Seeker取得了最先进的性能，甚至超越了部分专有模型。该工作首次系统性地构建了视觉原生的搜索范式，证明了主动视觉推理和搜索在真实网络环境中的有效性，为多模态智能体在开放世界中的事实性定位提供了新方向。
