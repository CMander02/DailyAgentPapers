---
title: "Grammar of the Wave: Towards Explainable Multivariate Time Series Event Detection via Neuro-Symbolic VLM Agents"
authors:
  - "Sky Chenwei Wan"
  - "Tianjun Hou"
  - "Yifei Wang"
  - "Xiqing Chang"
  - "Aymeric Jan"
date: "2026-03-12"
arxiv_id: "2603.11479"
arxiv_url: "https://arxiv.org/abs/2603.11479"
pdf_url: "https://arxiv.org/pdf/2603.11479v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Neuro-Symbolic AI"
  - "Vision-Language Model (VLM)"
  - "Agent Framework"
  - "Time Series Analysis"
  - "Explainable AI"
  - "Zero-Shot Learning"
  - "Knowledge Representation"
  - "Event Detection"
relevance_score: 7.5
---

# Grammar of the Wave: Towards Explainable Multivariate Time Series Event Detection via Neuro-Symbolic VLM Agents

## 原始摘要

Time Series Event Detection (TSED) has long been an important task with critical applications across many high-stakes domains. Unlike statistical anomalies, events are defined by semantics with complex internal structures, which are difficult to learn inductively from scarce labeled data in real-world settings. In light of this, we introduce Knowledge-Guided TSED, a new setting where a model is given a natural-language event description and must ground it to intervals in multivariate signals with little or no training data. To tackle this challenge, we introduce Event Logic Tree (ELT), a novel knowledge representation framework to bridge linguistic descriptions and physical time series data via modeling the intrinsic temporal-logic structures of events. Based on ELT, we present a neuro-symbolic VLM agent framework that iteratively instantiates primitives from signal visualizations and composes them under ELT constraints, producing both detected intervals and faithful explanations in the form of instantiated trees. To validate the effectiveness of our approach, we release a benchmark based on real-world time series data with expert knowledge and annotations. Experiments and human evaluation demonstrate the superiority of our method compared to supervised fine-tuning baselines and existing zero-shot time series reasoning frameworks based on LLMs/VLMs. We also show that ELT is critical in mitigating VLMs' inherent hallucination in matching signal morphology with event semantics.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统时间序列事件检测（TSED）中依赖大量标注数据进行归纳学习所带来的两大核心问题：数据稀缺性和模型不可解释性。研究背景是，在高风险领域（如医疗、能源），事件通常具有复杂的语义内涵和内部时态逻辑结构（例如“A急剧上升后B进入平台期”），而获取足量标注数据成本高昂。现有基于深度学习的归纳方法不仅难以在低资源场景下有效学习，而且其“黑箱”特性导致决策过程缺乏可解释性，无法提供人类专家可理解和验证的逻辑依据，从而阻碍了在需要高度信任的领域中的实际应用。

为此，论文提出了一个全新的任务设定——知识引导的时间序列事件检测（K-TSED）。其核心问题是：在几乎没有训练数据的情况下，如何让模型仅根据自然语言描述的事件语义知识，准确地在多元时间序列中定位对应的事件区间，并同时提供忠实、结构化、可验证的解释。这本质上是从归纳模式识别转向演绎式知识落地（grounding）的范式转换。

为了解决这一核心问题，论文引入了事件逻辑树（ELT）这一新颖的知识表示框架，将非结构化的语言描述转化为能清晰表达原子模式间时序逻辑关系的树形结构。基于ELT，论文进一步提出了一个神经符号视觉语言模型（VLM）智能体框架（SELA），通过逻辑分析智能体和信号检查智能体的协作，迭代地从信号可视化中实例化基本模式并在ELT约束下组合它们，最终输出检测到的事件区间及其对应的实例化逻辑树作为解释。这种方法旨在同时达成高精度检测和高可信度解释的目标。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：符号化时间序列表示方法、基于基础模型的少样本/零样本时间序列推理方法，以及本文所针对的知识引导时间序列事件检测（K-TSED）新设定。

在**符号化时间序列表示方法**方面，论文系统分析了现有框架在满足事件检测可解释性所需特性上的不足。SAX和ABBA通过无监督学习将时间序列映射为字符串序列，但表示依赖于数据集，缺乏层次结构（D1）和拓扑弹性（D3），对语义量化（D2）支持有限。Logical-Shapelets和Z-Time使用频繁出现的子序列（shapelets）进行表示，后者支持可变长度（满足D3），但两者均缺乏语义抽象（D2），且层次结构表示能力有限（部分满足D1）。Chronicle系统和信号时序逻辑（STL）采用图结构或递归逻辑公式，能很好表示层次结构（D1），但将语义一致性建模为二值判断（部分满足D2），且依赖实际时间区间（不满足D3）。本文提出的**事件逻辑树（ELT）** 框架则全面满足了所有三个期望特性。

在**基于基础模型的少样本/零样本推理**方面，相关工作探索了利用大语言模型（LLM）或视觉语言模型（VLM）处理时间序列。ChatTS通过合成数据对齐时间序列与语言进行问答，但存在合成与真实数据的领域差距以及幻觉风险。VL-Time将时间序列可视化为图表以利用VLM的推理能力，在分类任务中表现良好，但可视化会损失精度，且仍有幻觉问题。本文方法通过主动可视化工具克服精度损失，并利用ELT有效缓解了幻觉。

本文与这些工作的核心区别在于，首次明确了**知识引导TSED**这一新任务设定（给定自然语言事件描述，在极少或无需训练数据下定位多元信号区间），并提出了一个**神经符号VLM智能体框架**，该框架基于ELT这一新颖的知识表示，迭代地从信号可视化中实例化基元并在ELT约束下组合它们，从而同时产生检测结果和可解释的实例化树。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SELA的神经符号化视觉语言模型（VLM）多智能体框架来解决知识引导的时间序列事件检测问题。其核心方法是引入事件逻辑树（ELT）作为知识表示框架，将自然语言描述的事件语义与多元时间序列的物理信号形态进行结构化对齐，并在极少或无需训练数据的情况下，通过智能体的迭代推理实现可解释的事件检测。

整体框架由三个主要部分组成：中央逻辑引擎、统一接口和智能体推理与协作模块。中央逻辑引擎是系统的“后端”，采用三层架构：定义层存储从事件描述解析出的ELT模式（包括原子基元及其语义谓词、物理通道，以及由SEQ、SYNC、GUARD、OR等时态逻辑算子定义的复合结构）；实例化层存储从信号中检测到的基元实例（包含时间区间和语义一致性分数）以及复合节点实例；数据层存储原始多元时间序列数据。引擎的核心功能是依据模糊逻辑，通过定义的时态逻辑算子自底向上递归计算整个事件的置信度。

统一接口是连接智能体与后端引擎的桥梁。它提供一个联合的视觉-符号化可视化界面，将时间序列数据与逻辑树的状态并排显示。接口解析智能体发出的标准化JSON函数调用，执行相应动作（如提交模式定义或实例化候选），并更新视图和逻辑树状态。智能体可通过接口动态调用可视化工具，例如对特定时间窗口进行缩放和视图依赖的归一化，以揭示局部信号形态，或放置参考标记以跨通道对齐时间边界。

智能体推理被建模为马尔可夫决策过程，其动作空间是标准化的函数调用。创新点在于将复杂的落地任务分解为由两个专业化智能体通过共享环境协作完成：逻辑分析师负责将非结构化的文本事件描述语义翻译为ELT模式，识别原子基元并推断层次化的时态逻辑关系，输出为模式工件；信号检查员则负责在具体信号数据上实例化该模式，通过可视化工具分析信号形态，提交包含时间区间和置信度的实例化工件，并参照逻辑树状态不断优化检测边界，以最大化根节点（代表全局事件）的置信度。

关键技术包括：1）ELT表示法，它通过基元（描述单通道信号形态）和复合节点（定义时态逻辑关系）对事件内在结构进行显式建模，并辅以构造性组合、时间紧凑性和物理排他性三条公理来约束搜索空间，确保模式的合理性。2）时态逻辑算子的形式化定义与软性门控机制，例如SEQ算子通过因果门和连贯门确保时序先后关系并禁止语义间隙，SYNC和GUARD算子则使用基于IoU或边界溢出的惩罚项来强制时态对齐或包含关系，同时所有算子都集成了碰撞算子Ψ来强制执行物理排他性公理。这些设计共同使系统能够从信号可视化中迭代实例化基元，并在ELT约束下组合它们，最终输出检测到的时间区间以及以实例化树形式呈现的忠实解释，有效缓解了VLM在匹配信号形态与事件语义时的幻觉问题。

### Q4: 论文做了哪些实验？

实验在作者发布的真实世界时间序列基准测试KITE上进行，该基准包含KITE-easy和KITE-hard两个子集，用于评估模型在少样本或零样本条件下，根据自然语言事件描述进行检测的能力。实验设置包括：随机猜测；在低资源环境下训练监督模型（如CNN、Transformer）及微调时间序列基础模型（Timer、Moment、Chronos）；少样本/零样本LLM/VLM方案（如直接输入数值的Numeric、基于可视化的VL-Time）；两位具有行业经验的人类数据科学家；以及作者提出的神经符号VLM智能体框架SELA及其使用真实事件逻辑树（ELT）的Oracle变体。评估采用基于IoU的F1分数，阈值设为0.5和0.9以衡量定位精度。

主要结果显示，在基于LLM/VLM的方法中，SELA显著优于Numeric和VL-Time。具体而言，在零样本设置下，基于GPT-5的SELA在KITE-easy上达到F1@0.5为83.33%，F1@0.9为44.79%；在KITE-hard上分别为79.31%和68.96%，综合表现仅次于人类专家（F1@0.5接近人类水平，但F1@0.9仍有差距）。监督模型在低资源下受限，而浅层网络如Transformer在硬集上表现相对较好。消融实验表明，ELT对于处理复杂事件结构至关重要：在简单场景中其贡献有限，但在事件互斥且逻辑层次较深时，若无ELT引导，系统性能会严重下降（如VLM陷入局部特征或过度自信）。ELT将GPT-5在零样本下的F1@0.5相比VL-Time提升了约4倍，F1@0.9提升约2倍，有效缓解了VLM在匹配信号形态与事件语义时的幻觉问题。

### Q5: 有什么可以进一步探索的点？

该论文提出的方法在知识引导、低资源场景下展现了潜力，但仍存在一些局限和可拓展方向。首先，其核心知识表示框架“事件逻辑树”（ELT）依赖专家预先定义的事件结构，这限制了其泛化能力，未来可探索如何从少量示例或语言描述中自动归纳或演化出逻辑结构，实现更灵活的知识获取。其次，系统依赖于将时间序列转化为可视化图像供VLM处理，这可能丢失原始高维信号的细微特征，且计算开销较大；未来可研究如何让VLM或专用模型直接处理原始时序数据，或引入更高效的多模态对齐机制。此外，当前方法在极端复杂或噪声强烈的信号中性能可能下降，可考虑引入不确定性量化模块，使系统能评估自身推理的置信度，并在低置信时主动寻求人类反馈。最后，该框架目前侧重于检测，未来可扩展至事件预测、因果解释或跨领域迁移学习，例如将医疗事件逻辑适配至工业设备监测，从而提升方法的通用性和实用价值。

### Q6: 总结一下论文的主要内容

本文针对时间序列事件检测（TSED）任务，提出了一种新的“知识引导”设定和相应的神经-符号化视觉语言模型（VLM）智能体框架。核心问题是：在缺乏大量标注数据的情况下，如何根据自然语言事件描述，从多元时间序列信号中定位具有复杂内部语义结构的事件区间。

论文的核心贡献是提出了事件逻辑树（ELT）这一新颖的知识表示框架，它将语言描述与物理信号通过事件内在的时间逻辑结构（如时序、因果、形态关系）连接起来。基于ELT，作者设计了一个神经-符号化VLM智能体，它通过迭代地从信号可视化图像中实例化基本单元（如峰值、模式），并在ELT的符号约束下组合它们，从而输出检测到的事件区间以及可解释的、实例化的逻辑树作为忠实解释。

主要结论是，该方法在基于真实世界数据构建的基准测试中，显著优于需要监督微调的基线模型以及现有的基于LLM/VLM的零样本时间序列推理框架。实验表明，ELT框架对于弥合信号形态与事件语义之间的鸿沟、有效缓解VLM固有的“幻觉”问题至关重要，为实现可解释、低数据依赖的时序事件检测提供了新路径。
