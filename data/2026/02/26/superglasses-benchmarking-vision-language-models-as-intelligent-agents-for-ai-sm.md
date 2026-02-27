---
title: "SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses"
authors:
  - "Zhuohang Jiang"
  - "Xu Yuan"
  - "Haohao Qu"
  - "Shanru Lin"
  - "Kanglong Liu"
  - "Wenqi Fan"
  - "Qing Li"
date: "2026-02-26"
arxiv_id: "2602.22683"
arxiv_url: "https://arxiv.org/abs/2602.22683"
pdf_url: "https://arxiv.org/pdf/2602.22683v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Vision Language Models"
  - "Agent Benchmarking"
  - "Multimodal Interaction"
  - "Visual Question Answering"
  - "Retrieval-Augmented Generation"
  - "Egocentric Vision"
  - "Tool Use"
relevance_score: 7.5
---

# SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses

## 原始摘要

The rapid advancement of AI-powered smart glasses, one of the hottest wearable devices, has unlocked new frontiers for multimodal interaction, with Visual Question Answering (VQA) over external knowledge sources emerging as a core application. Existing Vision Language Models (VLMs) adapted to smart glasses are typically trained and evaluated on traditional multimodal datasets; however, these datasets lack the variety and realism needed to reflect smart glasses usage scenarios and diverge from their specific challenges, where accurately identifying the object of interest must precede any external knowledge retrieval. To bridge this gap, we introduce SUPERGLASSES, the first comprehensive VQA benchmark built on real-world data entirely collected by smart glasses devices. SUPERGLASSES comprises 2,422 egocentric image-question pairs spanning 14 image domains and 8 query categories, enriched with full search trajectories and reasoning annotations. We evaluate 26 representative VLMs on this benchmark, revealing significant performance gaps. To address the limitations of existing models, we further propose SUPERLENS, a multimodal smart glasses agent that enables retrieval-augmented answer generation by integrating automatic object detection, query decoupling, and multimodal web search. Our agent achieves state-of-the-art performance, surpassing GPT-4o by 2.19 percent, and highlights the need for task-specific solutions in smart glasses VQA scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前智能眼镜（AI Smart Glasses）领域缺乏一个能真实反映其实际应用场景和核心挑战的视觉问答（VQA）基准测试的问题。

研究背景是，随着AI技术（尤其是大语言模型和视觉语言模型）的进步，AI智能眼镜作为热门可穿戴设备，正通过增强现实和情境感知能力改变人机交互方式。其内置智能代理的核心应用之一，是基于外部知识源的视觉问答。然而，现有用于开发和评估智能代理的VQA基准（如Dyn-VQA、LIVEVQA等）存在显著不足：首先，其数据并非来源于真实的智能眼镜使用场景，导致存在“场景鸿沟”；其次，传统VQA数据集的图像通常清晰、目标明确，而智能眼镜采集的具身视角图像包含大量无关背景噪声，要求代理必须先准确识别和定位目标物体，才能进行知识检索与问答，这大大增加了任务难度；最后，现有基准缺乏在检索增强生成范式下详细的搜索记录或工具使用轨迹，而这对于理解和优化智能眼镜中的代理行为至关重要。

因此，本文要解决的核心问题是：填补上述鸿沟，为智能眼镜的VQA任务建立一个全面、真实、具有挑战性的专用基准，并在此基础上评估现有模型的不足，进而提出一个更高效的专用智能代理解决方案。为此，论文引入了SUPERGLASSES基准和SUPERLENS代理，前者基于真实设备采集的数据构建，后者则通过集成目标检测、查询解耦和多模态搜索来应对智能眼镜VQA的特殊挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基准数据集、智能体方法以及评测工作。

在**基准数据集**方面，现有研究如Dyn-VQA、LIVEVQA和CRAG-MM等，专注于动态、知识密集或需要多跳推理的视觉问答任务。然而，这些数据集通常使用非智能眼镜采集的通用图像，场景清晰且目标物体突出，与智能眼镜实际使用中存在的视角独特、背景噪声多、目标物体需先定位等挑战存在显著差距。本文提出的SUPERGLASSES则首次完全基于真实智能眼镜设备采集的数据构建，专门针对智能眼镜场景，并包含了完整的搜索轨迹标注，弥补了这一场景与可追溯性上的空白。

在**智能体方法**方面，现有智能眼镜中的智能体大多基于配备检索增强生成（RAG）流程的大型视觉语言模型（VLM）。这些模型通常在通用多模态数据上进行训练，缺乏对智能眼镜特定任务（如先检测后问答）的优化。本文提出的SUPERLENS智能体，通过集成自动目标检测、查询解耦和多模态网络搜索，专门针对智能眼镜的以自我为中心和知识密集型推理需求进行了设计，与通用VLM智能体在方法思路上有显著区别。

在**评测工作**方面，现有研究多基于上述通用VQA基准对VLM进行评估。本文则首次在真实智能眼镜场景基准上系统评估了26个代表性VLM，揭示了它们在面对真实场景挑战时的性能局限，并建立了专门的性能排行榜，为领域发展提供了新的评测视角和洞见。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SUPERLENS的多模态智能眼镜智能体来解决现有视觉语言模型在智能眼镜场景下VQA任务中的局限性。其核心方法是构建一个检索增强的生成框架，将模型的内部知识与外部证据动态结合。

整体架构包含两个核心组件：需求自适应应答器和双镜头知识检索器。需求自适应应答器首先判断问题是否可以通过模型内部知识直接回答。它引入了一个领域路由机制，让VLM识别图像-问题对的语义领域，并应用预定义的领域特定提示来激活相关知识，增强领域感知推理。对于超出模型知识范围的查询，则触发检索增强生成流程。

双镜头知识检索器负责从外部获取多模态信息。它包含一个基于VLM的搜索路由器，将所需知识分解为视觉对象和文本查询两个模态。对于视觉对象，使用开放词汇目标检测器从图像中精准定位相关区域；对于需要多跳推理的文本查询，则通过查询解耦器将其分解为单跳子查询以降低搜索复杂度。检索到的原始HTML网页经过网页阅读器进行内容提取和清洗。为了优化效率，系统采用了两层Redis缓存来避免重复搜索和解析。最后，一个多模态重排序器根据与文本和视觉查询的加权相似度对信息块进行重排序，确保最相关的证据被整合到RAG提示中，指导应答器生成最终答案。

该方法的创新点在于其针对智能眼镜场景的定制化设计：1）需求自适应的应答机制，平衡了效率与准确性；2）双模态检索流程，充分结合了视觉与文本信息；3）引入了查询解耦和对象检测等预处理步骤，以应对智能眼镜视野广阔、目标物体可能较小且查询复杂的挑战；4）高效的缓存和重排序策略，提升了系统的实时性。实验表明，该智能体在SUPERGLASSES基准上取得了最先进的性能，超越了GPT-4o等模型。

### Q4: 论文做了哪些实验？

论文在SUPERGLASSES基准上进行了广泛的实验。实验设置方面，评估了26个视觉语言模型（VLM），包括20个基础模型（如LLaMA-3.2-Vision、MiMo-VL、Qwen2.5-VL、Phi-3-Vision、GPT-4o、Claude 4 Sonnet、Gemini 2.5 Pro等）和6个通过启发式检索增强生成（RAG）策略增强的变体。图像输入的最短边被调整为1024像素。评估采用LLM-as-Judge框架，使用Qwen2.5-32B作为评判模型，根据真实答案判断模型回答的准确性。

使用的数据集是论文提出的SUPERGLASSES基准，包含2,422个由智能眼镜设备采集的以自我为中心的图像-问题对，涵盖14个图像领域和8个查询类别。

主要结果如下：所有模型在该基准上都面临巨大挑战，性能最佳的Gemini 2.5 Pro准确率也仅为43.02%。GPT-4o准确率为41.91%。开源模型显著落后于闭源模型。模型性能随规模增大而提升，体现了缩放定律。简单的启发式RAG策略并未带来整体性能增益，甚至可能因检索噪声导致性能下降（如LLaMA-3.2-11B的RAG变体准确率降至13.54%-17.13%）。

论文提出的智能眼镜代理SUPERLENS取得了最优性能，总体准确率达到44.10%，超过了GPT-4o（2.19%的领先优势），相比基线Qwen2.5-VL-7B提升了11.28%。消融实验表明，其需求自适应检索器和双镜头知识检索器的协同设计至关重要：移除查询解耦器导致性能下降3.18%，移除物体检测器下降1.53%；同时禁用两者则导致大幅下降11.28%。错误分析显示，当前模型的主要错误类型集中在查询解耦和工具调用方面。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准数据集规模相对有限（2422个样本），且主要聚焦于静态图像问答，未能充分模拟智能眼镜动态、连续的使用场景（如视频流理解、实时交互）。未来研究可探索以下方向：首先，扩展数据集至视频模态，引入时序推理任务，以更好地反映真实世界中的连续视觉交互需求。其次，当前模型依赖预定义的对象检测和查询解耦模块，未来可研究端到端的自适应架构，使模型能动态学习何时及如何检索外部知识，减少模块化设计的误差累积。此外，论文提出的解决方案尚未充分考虑隐私与计算效率的平衡，这对于穿戴设备至关重要；可探索轻量化模型与边缘计算结合，在本地实现高效推理。最后，智能眼镜的应用场景极具个性化，未来工作可引入用户自适应机制，使模型能根据使用习惯优化检索与回答策略。

### Q6: 总结一下论文的主要内容

该论文针对AI智能眼镜场景中视觉问答（VQA）任务缺乏真实评估基准的问题，提出了首个基于真实智能眼镜采集数据的VQA基准SUPERGLASSES。该基准包含2,422个以第一人称视角采集的图像-问题对，覆盖14个图像领域和8类查询，并提供了完整的搜索轨迹与推理标注。论文评估了26个主流视觉语言模型（VLMs），发现现有模型在智能眼镜应用场景中存在显著性能差距。为应对这一挑战，作者进一步提出了SUPERGLASSES智能眼镜代理系统SUPERLENS，其通过集成自动目标检测、查询解耦和多模态网络检索，实现了检索增强的答案生成。实验表明，该代理取得了最先进的性能，较GPT-4o提升了2.19%，凸显了针对智能眼镜VQA任务进行专门化系统设计的重要性。
