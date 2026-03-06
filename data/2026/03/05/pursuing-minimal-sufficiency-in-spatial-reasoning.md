---
title: "Pursuing Minimal Sufficiency in Spatial Reasoning"
authors:
  - "Yejie Guo"
  - "Yunzhong Hou"
  - "Wufei Ma"
  - "Meng Tang"
  - "Ming-Hsuan Yang"
date: "2025-10-19"
arxiv_id: "2510.16688"
arxiv_url: "https://arxiv.org/abs/2510.16688"
pdf_url: "https://arxiv.org/pdf/2510.16688v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "视觉语言模型"
  - "空间推理"
  - "工具使用"
  - "规划与推理"
  - "数据合成"
relevance_score: 7.5
---

# Pursuing Minimal Sufficiency in Spatial Reasoning

## 原始摘要

Spatial reasoning, the ability to ground language in 3D understanding, remains a persistent challenge for Vision-Language Models (VLMs). We identify two fundamental bottlenecks: inadequate 3D understanding capabilities stemming from 2D-centric pre-training, and reasoning failures induced by redundant 3D information. To address these, we first construct a Minimal Sufficient Set (MSS) of information before answering a given question: a compact selection of 3D perception results from \textit{expert models}. We introduce MSSR (Minimal Sufficient Spatial Reasoner), a dual-agent framework that implements this principle. A Perception Agent programmatically queries 3D scenes using a versatile perception toolbox to extract sufficient information, including a novel SOG (Situated Orientation Grounding) module that robustly extracts language-grounded directions. A Reasoning Agent then iteratively refines this information to pursue minimality, pruning redundant details and requesting missing ones in a closed loop until the MSS is curated. Extensive experiments demonstrate that our method, by explicitly pursuing both sufficiency and minimality, significantly improves accuracy and achieves state-of-the-art performance across two challenging benchmarks. Furthermore, our framework produces interpretable reasoning paths, offering a promising source of high-quality training data for future models. Source code is available at https://github.com/gyj155/mssr.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型在三维空间推理任务中存在的根本性瓶颈问题。研究背景是，尽管VLMs在诸多任务上表现出色，但在需要将语言与三维空间理解相结合的空间推理任务上，其表现仍然不佳。现有方法主要存在两大不足：首先，由于预训练数据以二维图像为主，VLMs普遍缺乏三维几何先验知识，导致其在感知三维布局、方向和深度等信息时能力不足；其次，三维环境信息密集，现有方法倾向于不加选择地汇总所有感知信息，导致大量冗余或弱相关信息涌入模型上下文，这不仅会分散模型的注意力，还可能诱导其采用捷径启发式策略，最终损害推理的准确性。

本文的核心问题是：如何让模型在面对三维空间推理问题时，能够像人类一样，主动构建并维护一个“任务特定”且“最小化”的信息集合，从而在保证信息充分性的同时避免冗余干扰。为此，论文提出了“最小充分集”的概念，并设计了一个名为MSSR的双智能体框架来具体实现这一目标。该框架通过一个感知智能体利用专家模型工具（包括新颖的SOG模块）来程序化地提取充分的三维感知信息，再通过一个推理智能体迭代地提炼这些信息，剔除冗余并请求缺失部分，直至构建出能够精确回答当前问题的最小充分信息集，从而同时攻克三维感知能力不足和信息冗余损害推理这两个核心挑战。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、智能体框架类和视觉编程类。

在**方法类**研究中，传统的整体式视觉语言模型通常通过在合成数据上微调或集成专用模块来处理3D模态（如点云）。这些方法虽然取得进展，但依赖昂贵的3D指令数据集，且可能遗忘预训练知识，损害模型的通用推理能力。本文提出的MSSR框架则无需训练，以零样本方式工作，通过结构化感知-推理过程来保持VLM的完整能力，从而避免了上述限制。

在**智能体框架类**工作中，如ReAct等先驱方法展示了LLM可以交错进行推理与行动，这一范式被扩展到3D领域，用于具身探索和3D视觉问答等任务的信息收集。然而，这些方法主要侧重于信息积累，而本文针对的3D场景信息密集，冗余细节会降低性能。因此，MSSR的关键区别在于它不仅收集信息，还主动修剪无关内容，追求信息的最小充分性。

在**视觉编程类**范式中，常将复杂视觉任务分解为可执行程序以查询3D属性。本文的感知代理采用了视觉编程作为执行主干，以利用其模块化集成专用工具。与典型的一次性执行不同，本文的框架将视觉编程集成到一个闭环中，保留了完整的执行状态，使得后续感知步骤可以基于先前的计算进行，从而实现动态信息精炼并避免冗余工作。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MSSR（最小充分空间推理器）的双智能体框架来解决空间推理中的两大瓶颈：二维预训练导致的3D理解能力不足，以及冗余3D信息引发的推理失败。其核心方法是主动构建一个“最小充分集”（MSS），即在回答问题前，从3D场景中提取一个既足够又无冗余的紧凑信息集合。

整体框架由感知智能体（PA）和推理智能体（RA）组成，二者进行闭环协作。流程始于一个空的MSS候选集S。首先，感知智能体根据一个宽泛的指令（如“提取所有可能相关的信息”），利用其视觉编程工具箱，从多视角图像中执行程序化查询，提取丰富的3D感知信息（如物体坐标、空间关系）来初步填充S。这个工具箱包含基础模块（如物体定位、几何计算）和几个关键创新模块：1）**基础3D场景重建模块**，利用快速神经重建模型（如VGGT）从稀疏2D图像生成统一的3D点云和深度图，作为空间信息提取的基础画布；2）**全局坐标系校准模块**，根据查询中的显式指令或显著地标建立统一的全局坐标系，以消除“左”、“后”等视角依赖术语的歧义；3）**新颖的“情境化方向定位”（SOG）模块**，它通过将语言描述的方向（如“椅子的正面”、“出口方向”）转化为3D向量，解决了复杂、情境依赖的方向理解难题。SOG采用“由粗到细”的策略，将方向回归问题转化为更可靠的视觉选择任务：首先生成稀疏的候选方向向量并渲染到原始视图和合成规范视图上，提示视觉语言模型（VLM）进行选择，然后围绕所选方向生成更密集的候选进行细化，从而鲁棒地获得精确的3D方向。

初步填充的S被传递给推理智能体进行“精炼”。推理智能体的工作分为两个阶段：1）**计划引导的信息筛选**：它首先制定一个回答查询的高层推理计划，然后基于此计划，严格审查S中的每一项信息，只保留与计划因果相关的必要项，剔除冗余和无关细节，从而强制实现“最小性”。2）**战略决策**：筛选后，推理智能体判断当前信息集是否“充分”。如果不足，它会生成一个精准的自然语言请求（如“<Request> 坐在椅子上的人所面对的方向”），发回给感知智能体进行针对性信息补充。感知智能体基于此请求和现有环境快照（避免重复计算）执行新的编程查询来更新S。这个“筛选-请求”的循环持续进行，直到推理智能体判定信息已充分。此时，它触发<Decide>动作，丢弃所有先前上下文，仅基于最终筛选出的最小充分集，使用思维链进行推理并生成最终答案，确保了推理的专注性和可解释性。

该方法的创新点在于：1）明确提出了“最小充分性”原则，并通过双智能体闭环交互机制系统性地实现它；2）设计了强大的感知工具箱，特别是SOG模块，显著增强了对于语言条件化方向的理解能力；3）整个框架是零样本驱动的，不依赖于上下文学习示例，增强了泛化能力。通过这种主动构建最小充分信息集并迭代精炼的方式，MSSR有效克服了信息不足和冗余干扰的问题，从而提升了空间推理的准确性和鲁棒性。

### Q4: 论文做了哪些实验？

论文在两个具有挑战性的空间推理基准测试上进行了广泛的实验：MMSI-Bench 和 ViewSpatial-Bench。MMSI-Bench 是一个手工制作的多图像数据集，侧重于位置关系、多步推理以及属性与运动理解；ViewSpatial-Bench 则评估模型在不同空间视角（相机中心和人中心）下的泛化能力。

实验设置了五类基线模型进行对比：1) 专有LLM（如GPT-4o、Gemini系列、o3）；2) 开源LLM（如Llama-3.2-Vision、Qwen-VL系列、InternVL系列）；3) 3D-VLM（如VLM-3R、Video-3D-LLM）；4) 专家模型（LEO）；5) 智能体框架（ViLaSR、VADAR）。

主要结果显示，MSSR方法在MMSI-Bench上取得了49.5%的整体准确率，显著优于最佳基线o3（41.0%）和最佳开源模型Qwen3-VL-8B（31.1%）；在ViewSpatial-Bench上达到51.8%的整体准确率，在相机中心和人物中心任务上分别达到51.0%和54.4%。关键指标包括：相比GPT-4o骨干网络，在MMSI-Bench上提升了19.2个百分点，在ViewSpatial-Bench上提升了16.8个百分点。

此外，论文进行了消融实验，验证了框架关键组件的作用：仅使用感知代理（PA）准确率降至37.1%，仅使用推理代理（RA）降至31.1%，去除SOG模块降至46.9%，去除迭代机制降至47.2%。实验还证明了最小充分性原则的有效性：当信息集元素从平均17.3个修剪至5.9个时，推理准确率从45.8%提升至48.3%。最后，论文展示了MSSR在不同开源骨干模型上的泛化性，以及其作为数据标注引擎的潜力：使用MSSR生成的标注数据对Qwen2.5-VL-7B进行微调后，其在MMSI-Bench上的准确率从25.9%提升至30.1%。

### Q5: 有什么可以进一步探索的点？

该论文提出的MSSR框架在追求空间推理的“最小充分性”上取得了显著进展，但其设计仍存在一些局限性和可拓展方向。首先，框架高度依赖预设的专家感知模型（如3D检测、方向定位模块）来构建信息集，这限制了其在开放世界或未知场景中的泛化能力。未来研究可探索如何让模型本身通过少量样本学习这些感知能力，或构建更通用的3D基础模型作为感知工具箱。其次，当前的双智能体循环依赖于程序化查询，推理过程可能受限于预定义的逻辑规则。可引入强化学习或世界模型，让智能体通过与环境交互自主探索信息获取与精简的策略，从而处理更复杂、多步骤的空间推理任务。此外，论文生成的“高质量推理路径”可作为训练数据，但尚未验证其用于模型训练的实际效果。未来可系统性地利用这些轨迹进行指令微调或强化学习，以提升VLMs的固有3D推理能力，减少对外部模块的依赖。最后，该框架目前专注于静态3D场景，可进一步扩展至动态场景或跨模态时序推理（如结合视频与语言），以应对更现实的应用场景。

### Q6: 总结一下论文的主要内容

该论文针对视觉语言模型在空间推理任务中存在的两大瓶颈——基于2D预训练导致的3D理解能力不足，以及冗余3D信息引发的推理失败——提出了一个追求“最小充分性”的解决方案。其核心贡献是提出了MSSR（最小充分空间推理器）这一双智能体框架。该方法首先定义了“最小充分集”的概念，即在回答问题前，从专家模型中筛选出紧凑且足够的3D感知信息。具体实现上，感知智能体利用一个包含新颖的“情境化方向定位”模块的工具箱，以编程方式查询3D场景以提取充分信息；随后，推理智能体通过闭环迭代，不断提炼该信息以追求最小化，即剪除冗余并请求缺失内容，直至构建出最小充分集。实验表明，该方法通过显式地追求信息的充分性与最小化，在多个基准测试中显著提升了准确性并达到了最先进的性能。此外，该框架生成的解释性推理路径，为未来模型提供了高质量的训练数据来源。
