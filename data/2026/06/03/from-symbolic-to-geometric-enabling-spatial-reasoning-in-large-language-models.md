---
title: "From Symbolic to Geometric: Enabling Spatial Reasoning in Large Language Models"
authors:
  - "Chen Chu"
  - "Bita Azarijoo"
  - "Li Xiong"
  - "Khurram Shafique"
  - "Cyrus Shahabi"
date: "2026-06-03"
arxiv_id: "2606.04381"
arxiv_url: "https://arxiv.org/abs/2606.04381"
pdf_url: "https://arxiv.org/pdf/2606.04381v1"
github_url: "https://github.com/chuchen2017/SLM"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "多模态LLM Agent"
  - "空间推理"
  - "空间语言模型"
  - "基准测试"
  - "指令数据集"
relevance_score: 8.5
---

# From Symbolic to Geometric: Enabling Spatial Reasoning in Large Language Models

## 原始摘要

Recent large language models (LLMs) often appear to exhibit spatial reasoning ability; however, this capability is largely \emph{symbolic}, arising from pattern matching over spatial language rather than true \emph{geometric} reasoning over space. Because LLMs operate on discrete tokens, they lack native support for continuous spatial representations, explicit geometric computation, and structured spatial operators. To address this limitation, we introduce the \emph{Spatial Language Model (SLM)}, the first multimodal LLM that treats location information as a first-class modality and enables geometric spatial reasoning within the model's inference process. SLM directly operates on learned spatial representations rather than textual descriptions of spatial relations. To support effective training, we construct a \emph{Spatial Instruction Dataset} that aligns spatial representations, atomic geometric operations, and natural language instructions. We further propose a new benchmark named \emph{SpatialEval}, which is designed to evaluate spatial reasoning across attributes, distance, topology, and relative-position tasks. Extensive experiments show that SLM significantly outperforms existing LLM-based approaches that rely on symbolic reasoning via prompt engineering or textual abstraction, demonstrating the benefits of integrating geometric spatial representations for robust spatial reasoning.
  Our instruction dataset, evaluation benchmark, model training codes, and models' checkpoints can be found at:
  \hyperlink{https://github.com/chuchen2017/SLM}{https://github.com/chuchen2017/SLM}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在空间推理上的根本性缺陷：当前LLM所展现的空间推理能力本质上是**符号化**的，而非真正的**几何空间推理**。研究背景指出，尽管LLM在处理空间语言（如地名、坐标等符号）上表现尚可，但其能力主要源于从文本语料中学习到的共现模式，而非对空间几何结构的显式建模。现有方法的不足体现在三个方面：1）**依赖符号检索**：LLM通过模式匹配回答空间查询，容易产生幻觉，且无法泛化到未见过的新地点；2）**缺乏几何计算**：涉及距离测量、拓扑关系或相对位置等需要精确数值计算的任务时，LLM因缺乏可靠的计算能力而表现不佳；3）**外部工具依赖**：为弥补缺陷，现有方法（如使用地图API或搜索引擎）将几何推理外包，导致推理成本高、延迟大，且核心能力并未内化到模型中。因此，本文要解决的核心问题是：**如何让LLM直接内在地具备几何空间推理能力**，即从符号化的空间语言模式匹配转向对连续空间表征的显式几何运算，从而摆脱对外部工具的依赖并提升推理的鲁棒性与泛化性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：

1. **多模态语言模型**：相关工作包括视觉-语言模型、视频、音频以及点云和街景图像等特定领域模态的扩展。这些模型通过特定编码器将原始输入转换为高级特征，再映射到语言模型嵌入空间。与本文的区别在于，现有多模态LLM未显式支持几何空间推理，而本文首次将显式几何空间表示集成到多模态LLM框架中，实现超越符号文本空间表征的内在空间推理。

2. **空间表征学习**：传统方法如Poly2Vec和Geo2Vec支持统一向量表征学习，但通常仅处理单一地理空间实体类型，限制了统一空间推理。本文利用统一表征学习的特性，将复杂符号表征压缩为单一向量，使语言模型能更高效地进行空间推理。与以往方法相比，本文的创新在于直接将位置信息作为一等模态处理，在推理过程中启用几何空间计算，而非依赖文本描述的空间关系。

### Q3: 论文如何解决这个问题？

论文通过提出空间语言模型（SLM）来解决问题，该模型将位置信息作为第一类模态，实现了几何空间推理。核心方法包括三个关键设计：首先，采用统一空间编码器Geo2Vec，将异构地理实体（如POI、道路、建筑）映射到共享嵌入空间，捕获几何形状和绝对位置，形成连续空间表示。其次，设计了交错提示格式，为每个实体添加特殊标记<GEO>作为空间模态占位符，在推理时替换为对应的几何表示向量，使LLM直接处理几何表征而非文本描述。最后，构建了空间指令数据集，将复杂空间推理问题分解为原子几何函数（如面积、长度、距离计算），并通过智能体引导的答案构建，生成结构化的<geo_think>推理轨迹，监督模型学习显式空间操作。创新点在于：1）首次将空间表示作为单独模态集成到LLM中，替代了依赖文本模式的符号推理；2）通过地理空间思维链分解，使模型内部化几何计算能力；3）利用提示演化策略增强数据多样性，避免过拟合。整体框架包含空间编码器、适配器将几何向量投影到词嵌入空间，以及微调阶段对LLM进行空间推理训练，实验在SpatialEval基准上显著优于传统LLM方法。

### Q4: 论文做了哪些实验？

论文在三个地理空间数据集（北京和洛杉矶的城市级POI、道路网络、建筑足迹，以及美国国家级县/州边界）上评估了SLM的空间推理能力。实验设置包括：使用Qwen3-8B作为基座模型，通过LoRA微调仅在训练集的几何表示上训练SLM。对比方法包括开源LLM（Qwen3-8B、DeepSeek-R1-Distill-Qwen-32B、LLaMA-3.3-70B-Instruct）、商业模型（Gemini 2.5 Flash、ChatGPT 5.1）及VLM方法SpatialRGPT，所有基线都通过提供显式地理坐标进行符号空间推理。评估使用SpatialEval基准，涵盖距离（L2误差）、最近邻（NN准确率）和拓扑关系任务。主要结果显示：SLM在所有指标上显著优于基线，例如在北京数据集上，SLM的PT-PL距离误差为7816.0（响应有效率52.3%），而最佳基线Gemini 2.5 Flash为2600.1（有效率100%）；在NN任务中，SLM的PT-PL准确率仅12.50%，远低于Gemini的71.9%。这表明SLM通过集成几何空间表示实现了更鲁棒的空间推理，但性能受表示质量影响。

### Q5: 有什么可以进一步探索的点？

该工作虽在空间推理上取得突破，但仍存在若干可深入探索的方向。首先，**空间表征的通用性与可迁移性**有待加强：当前SLM依赖特定坐标形式的空间特征，未来可探索如何将稀疏点云、网格图或拓扑图等更丰富的几何结构纳入统一表征，以提升对复杂真实场景（如3D环境或不规则物体）的泛化能力。其次，**推理的符号-几何混合机制**值得关注：单纯几何推理可能丧失符号推理中的抽象因果链，结合两者（如分阶段先几何定位再符号推理）或能互补。再者，**指令数据的自动生成与规模扩展**是瓶颈：人工标注空间关系耗时易错，可尝试引入程序化合成（如基于游戏引擎渲染）与基于规则的空间操作逻辑来生成海量多样化数据。最后，**跨模态实时动态推理**尚未触及：例如在导航或操作任务中，LLM需处理动态变化的视觉空间输入，当前静态测试无法体现该能力，未来可构建交互式环境并设计时序空间推理任务。

### Q6: 总结一下论文的主要内容

这篇论文提出空间语言模型（SLM），旨在解决大语言模型（LLM）在空间推理上的根本缺陷：当前LLM主要依赖符号化模式匹配进行空间推理，而非真正的几何空间推理。SLM首次将位置信息作为独立模态集成到多模态LLM中，直接操作学习到的空间表示而非文本描述，从而在模型推理过程中实现几何空间推理。为支持训练，作者构建了空间指令数据集，对齐空间表示、原子几何操作与自然语言指令。同时提出SpatialEval基准，系统评估属性、距离、拓扑和相对位置推理任务。实验表明，SLM显著优于依赖提示工程或文本抽象的符号化方法，证明了将几何空间表示融入模型对于鲁棒空间推理的有效性。该研究的关键意义在于突破了LLM对符号化空间知识的依赖，实现了向真正几何推理的范式转变。
