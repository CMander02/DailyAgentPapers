---
title: "Agentic Very Long Video Understanding"
authors:
  - "Aniket Rege"
  - "Arka Sadhu"
  - "Yuliang Li"
  - "Kejie Li"
  - "Ramya Korlakai Vinayak"
  - "Yuning Chai"
  - "Yong Jae Lee"
  - "Hyo Jin Kim"
date: "2026-01-26"
arxiv_id: "2601.18157"
arxiv_url: "https://arxiv.org/abs/2601.18157"
pdf_url: "https://arxiv.org/pdf/2601.18157v2"
categories:
  - "cs.CV"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "规划与推理"
  - "多模态智能体"
  - "视频理解"
  - "长期记忆"
  - "检索增强生成"
relevance_score: 8.0
---

# Agentic Very Long Video Understanding

## 原始摘要

The advent of always-on personal AI assistants, enabled by all-day wearable devices such as smart glasses, demands a new level of contextual understanding, one that goes beyond short, isolated events to encompass the continuous, longitudinal stream of egocentric video. Achieving this vision requires advances in long-horizon video understanding, where systems must interpret and recall visual and audio information spanning days or even weeks. Existing methods, including large language models and retrieval-augmented generation, are constrained by limited context windows and lack the ability to perform compositional, multi-hop reasoning over very long video streams. In this work, we address these challenges through EGAgent, an enhanced agentic framework centered on entity scene graphs, which represent people, places, objects, and their relationships over time. Our system equips a planning agent with tools for structured search and reasoning over these graphs, as well as hybrid visual and audio search capabilities, enabling detailed, cross-modal, and temporally coherent reasoning. Experiments on the EgoLifeQA and Video-MME (Long) datasets show that our method achieves state-of-the-art performance on EgoLifeQA (57.5%) and competitive performance on Video-MME (Long) (74.1%) for complex longitudinal video understanding tasks. Code is available at https://github.com/facebookresearch/egagent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决“超长视频理解”这一核心问题，其背景是全天候可穿戴设备（如智能眼镜）的兴起催生了始终在线的个人AI助手。这类助手需要理解用户连续、纵向的第一人称视频流（可长达数天甚至数周），而不仅仅是孤立的短时事件，以实现个性化、上下文感知的辅助。

现有方法存在明显不足。一方面，大型语言模型和检索增强生成等方法受限于有限的上下文窗口，无法直接处理极长视频序列。另一方面，现有的智能体方法虽然能通过工具进行搜索和推理，但在处理超长时间跨度时，往往难以对实体及其关系进行连贯的推理，也难以进行细粒度的时间定位（例如追踪跨天的重复行为）和跨模态信息的有效关联。

因此，本文要解决的核心问题是：如何构建一个能够对超长、连续的自我中心视频进行详细、跨模态且时间连贯的推理的系统。为此，论文提出了EGAgent，一个以实体场景图为核心的增强型智能体框架。该框架通过构建表示人物、地点、物体及其随时间变化关系的实体图，并赋予规划智能体在该图上进行结构化搜索与推理的工具，以及混合视觉与音频搜索能力，从而克服现有方法的局限，实现对复杂纵向体验的理解与回忆。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：长视频理解、基于图的检索增强生成以及智能体化视频理解。

在**长视频理解与LLMs**方面，现有方法主要应对LLM上下文窗口有限的挑战。主流技术包括帧选择、视觉令牌压缩、滑动窗口或分层摘要策略，以及直接扩展LLM上下文容量。这些方法旨在压缩视频输入以适应模型处理限制，可分为查询依赖型或查询独立型。本文的EGAgent框架同样致力于长视频理解，但区别于这些侧重于输入压缩或摘要的方法，它通过构建结构化的、时间感知的实体场景图来进行深度推理。

在**基于图的检索增强生成**方面，传统RAG处理孤立文本块可能丢失关系信息。GraphRAG、LightRAG等方法利用从文本构建的知识图来改善这一点。多模态RAG（如Video-RAG、AdaVideoRAG、RAVU、GraphVideoAgent）进一步整合了视觉、音频等多种模态信息进行检索。VideoMindPalace构建了分层的时空图。本文方法与这类研究密切相关，同样采用图结构进行增强检索。关键区别在于，本文构建的实体场景图是**时间感知的**（节点带有时间标注），并且支持**增量构建**，而非一次性为整个视频建图。这使得系统能高效处理持续流入的视频流，实验表明在达到相近性能时处理的帧数更少。

在**智能体化视频理解**方面，VideoAgent、DrVideo、SiLVR等工作引入了具备工具调用能力的智能体框架，通过迭代搜索、信息增强或文本域推理来回答问题。本文的EGAgent属于此类智能体框架的演进。它与前驱工作的主要区别在于，其核心工具是**带时间标注的实体场景图**，而非依赖非结构化的视频描述或重复的原始帧检索。这种设计旨在实现更高效的跨模态搜索和对复杂、纵向查询的组合式推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EGAgent的增强型智能体框架来解决超长视频理解问题，其核心是构建并利用实体场景图进行结构化搜索和推理。整体方法分为两个关键步骤：首先，从视频中提取并构建一个以实体为中心的图结构表示；其次，设计一个基于规划的智能体框架，该框架能够利用专用工具对该图进行多步骤、跨模态的查询与推理。

在架构设计上，系统主要包括六大组件：1）**规划智能体**：负责将复杂的用户查询分解为一系列子任务，并为每个子任务选择合适的检索工具；2）**三种检索工具**：包括**视觉搜索工具**（基于嵌入向量和属性进行混合搜索）、**音频转录搜索工具**（基于LLM或BM25的文本搜索）以及核心的**实体图搜索工具**（通过SQL查询图数据库）；3）**分析器工具**：对检索到的信息进行LLM驱动的轻量级推理、证据提取和去重；4）**VQA智能体**：综合工作记忆中积累的所有跨模态证据，生成最终答案。整个流程是迭代式的：规划智能体制定计划，调用工具检索数据，分析器提炼信息并更新工作记忆，最终由VQA智能体进行答案合成。

其关键技术及创新点在于：第一，**实体场景图的构建与表示**。系统使用LLM从视频的音频转录和场景描述文本中，联合提取人物、物体、地点等实体及其之间的交互关系（如“交谈”、“使用”、“提及”），并为每条边标注精确的时间区间。这些信息被结构化为一个存储在SQLite数据库中的图，支持高效的、基于时间的查询。第二，**智能体驱动的、工具化的推理框架**。规划智能体不仅能分解任务，还能为实体图搜索工具动态生成并优化SQL查询，采用“从严格到宽松”的策略（先精确匹配，逐步放宽时间、文本或关系类型约束）来平衡检索的精确性与召回率。第三，**跨模态的混合检索与证据积累**。框架并非单一依赖图检索，而是协同利用视觉、音频和图结构三种数据源，通过工作记忆逐步整合多模态证据，从而支持对实体长期行为、交互关系进行组合式、多跳的复杂推理。这种方法克服了传统方法因上下文窗口限制和缺乏结构化实体关系建模而难以处理长达数周视频中复杂查询的瓶颈。

### Q4: 论文做了哪些实验？

论文在EgoLifeQA和Video-MME (Long)两个基准测试上进行了实验，以评估所提出的EGAgent框架在超长视频理解任务上的性能。

**实验设置与数据集**：实验使用了两个专注于超长视频理解的基准。EgoLifeQA包含500个来自EgoLife数据集的多选题，视频时长约50小时，问题涉及物品定位、事件回忆、习惯追踪和社交互动分析等。Video-MME (Long)包含300个时长30至60分钟的视频，共2700个多选题。系统为每个视频（或EgoLifeQA中每小时视频）构建实体场景图，并利用音频文本转录进行多模态处理。

**对比方法与主要结果**：论文将EGAgent与三类基线方法进行比较：1）均匀采样的多模态大模型（MLLM），如GPT-4.1、Gemini 2.5 Pro；2）结合检索增强生成（RAG）的MLLM；3）现有智能体方法，如EgoButler、VideoAgent和Ego-R1。

在EgoLifeQA上，EGAgent（以Gemini 2.5 Pro为骨干）取得了57.5%的平均准确率，达到了新的最优性能（SOTA），相比之前的SOTA（EgoButler的36.9%）提升了20.6个百分点。特别是在需要复杂关系推理的RelationMap和TaskMaster类别上，分别比Gemini 2.5 Pro（均匀采样）提升了20.8%和22.2%。在Video-MME (Long)上，EGAgent（Gemini 2.5 Pro骨干）取得了74.1%的准确率，具有竞争力。

**关键数据指标**：EgoLifeQA上，EGAgent (Gemini 2.5 Pro) 在EL、ER、HI、RM、TM五个类别的准确率分别为54.4%、57.1%、60.3%、62.4%、74.6%，平均57.5%。消融实验表明，使用融合字幕（C+T）进行实体图提取以及使用LLM进行转录搜索能带来最佳性能提升（例如，GPT-4.1骨干下准确率从36.8%提升至50.7%）。

### Q5: 有什么可以进一步探索的点？

该论文提出的EGAgent框架在超长视频理解上取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，系统严重依赖预提取的实体场景图，其构建质量和完整性直接影响最终性能。未来可探索更动态、在线的图构建与更新机制，减少预处理依赖。其次，当前框架主要处理多选问答任务，未来需扩展到更复杂的开放式问答、推理和决策任务，以支持全天候个人AI助手所需的主动交互。此外，实验表明不同骨干模型（如GPT-4.1与Gemini 2.5 Pro）性能差异显著，未来可研究如何设计更轻量、高效的专用模型，降低对超大闭源模型的依赖。最后，系统目前主要整合视觉和音频模态，未来可融入更多传感器数据（如位置、生理信号）以提升情境理解深度，并探索在资源受限的穿戴设备上的高效部署方案。

### Q6: 总结一下论文的主要内容

本文针对全天候可穿戴设备（如智能眼镜）产生的超长第一人称视频理解问题，提出了一种新的智能体框架EGAgent。现有方法受限于有限的上下文窗口，难以对跨越数天甚至数周的连续视频流进行组合式、多跳推理。该论文的核心贡献是构建了一个以实体场景图为中心的增强型智能体框架，该图能随时间推移表征人物、地点、物体及其相互关系。系统赋予规划智能体一系列工具，使其能够对这些图进行结构化搜索和推理，并具备混合视觉与音频搜索能力，从而实现细致、跨模态且时间连贯的推理。实验表明，该方法在EgoLifeQA和Video-MME (Long)数据集上，针对复杂的纵向视频理解任务，分别取得了57.5%的领先性能和74.1%的竞争性性能，验证了其有效性。
