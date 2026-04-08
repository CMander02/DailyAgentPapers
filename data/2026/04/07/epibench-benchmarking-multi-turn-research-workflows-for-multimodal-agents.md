---
title: "EpiBench: Benchmarking Multi-turn Research Workflows for Multimodal Agents"
authors:
  - "Xuan Dong"
  - "Huanyang Zheng"
  - "Tianhao Niu"
  - "Zhe Han"
  - "Pengzhan Li"
  - "Bofei Liu"
  - "Zhengyang Liu"
  - "Guancheng Li"
  - "Qingfu Zhu"
  - "Wanxiang Che"
date: "2026-04-07"
arxiv_id: "2604.05557"
arxiv_url: "https://arxiv.org/abs/2604.05557"
pdf_url: "https://arxiv.org/pdf/2604.05557v1"
categories:
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Multimodal Agent"
  - "Research Agent"
  - "Multi-turn Interaction"
  - "Memory"
  - "Evaluation Framework"
relevance_score: 8.0
---

# EpiBench: Benchmarking Multi-turn Research Workflows for Multimodal Agents

## 原始摘要

Scientific research follows multi-turn, multi-step workflows that require proactively searching the literature, consulting figures and tables, and integrating evidence across papers to align experimental settings and support reproducible conclusions. This joint capability is not systematically assessed in existing benchmarks, which largely under-evaluate proactive search, multi-evidence integration and sustained evidence use over time. In this work, we introduce EpiBench, an episodic multi-turn multimodal benchmark that instantiates short research workflows. Given a research task, agents must navigate across papers over multiple turns, align evidence from figures and tables, and use the accumulated evidence in the memory to answer objective questions that require cross paper comparisons and multi-figure integration. EpiBench introduces a process-level evaluation framework for fine-grained testing and diagnosis of research agents. Our experiments show that even the leading model achieves an accuracy of only 29.23% on the hard split, indicating substantial room for improvement in multi-turn, multi-evidence research workflows, providing an evaluation platform for verifiable and reproducible research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态智能体在科学研究工作流评估方面的不足。随着科学文献的爆炸式增长，自动化研究辅助的需求日益迫切，而现有基准测试无法系统性地评估真实研究场景中所需的关键能力。研究背景是，尽管大语言模型和多模态智能体在工具调用和文献处理方面取得了进展，但现有评测方法（如MMCR、PaperArena等）存在两大缺陷：一是任务设计偏离真实工作流，往往直接指定目标论文或仅需单篇文献中的单一图表，无需智能体主动检索文献或跨多篇文献整合多模态证据；二是评估协议不完整，缺乏对证据重用和证据正确性的细粒度过程级度量。

因此，本文的核心问题是双重的：首先，现有基准无法全面评估类人的研究工作流，包括主动检索、多轮交互以及跨论文的多模态证据融合；其次，现有协议缺乏针对证据重用和证据正确性的过程级指标，难以进行故障诊断。为此，论文提出了EpiBench基准，通过模拟短研究流程的多轮情景任务，要求智能体在未指定目标论文的情况下主动检索文献，从图表中提取结构化证据，并在多轮对话中持续整合证据以回答客观问题。同时，该基准引入了基于访问预算的评估框架，通过标注证据单元和自动溯源评分，量化证据重用效率和工具使用效果，从而实现对智能体研究工作流能力的细粒度测试与诊断。

### Q2: 有哪些相关研究？

相关研究主要分为三类：科学文档理解基准、多轮多模态推理基准以及研究导向的代理评估基准。

在科学文档理解方面，SciVQA、CharXiv和SPIQA等数据集专注于对科学图表进行问答，LiveXiv则进一步生成了大规模且持续更新的视觉问答任务。这些工作主要评估单文档内的单图或单表理解，缺乏跨文档和多证据整合的要求。SIN-Bench虽模拟了多步骤工作流（如证据发现和基于文档的问答），但仍局限于单个长文档内。PaperArena则评估了跨学术论文的多跳导航，但很少要求联合整合多个图表信息来推导答案。

在多轮多模态推理方面，MMDU基于维基百科内容构建了多图像多轮对话，MULTIVERSE进一步扩展了其规模和深度，MMCR则强调跨对话轮的上下文推理。这些研究推动了多轮推理的发展，要求代理重用先前步骤积累的信息，但如Memory-QA和EMP等工作主要关注从记忆中检索单个查询的答案，且通常不以论文为中心，很少涉及跨论文的图表证据整合。

本文提出的EpiBench与上述工作的主要区别在于：它专门针对科研工作流，要求代理在多轮中主动探索多篇论文，整合跨文档的图表证据，并迭代积累和重用证据，以回答需要跨论文比较和多图融合的客观科学问题，从而系统评估现有基准未能充分覆盖的主动搜索、多证据整合和持续证据使用能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为EpiBench的基准测试平台来解决现有评测体系在评估多轮、多模态研究型智能体工作流方面的不足。其核心方法是设计一个**情景式多轮多模态基准**，模拟真实的短期科研工作流程，并提供一个**过程级评估框架**进行细粒度测试与诊断。

整体框架上，EpiBench将研究任务实例化为一个多轮问题链构成的“情景”。每个情景包含一系列回合，每个回合向智能体提出一个客观问题，并可选择性地提供图像片段或文献提示作为初始线索。智能体必须调用外部工具包来回答问题，工具包功能包括搜索论文、打开PDF、提取图表或文本等。检索到的证据被存储在一个记忆池中，供后续回合复用。最后一个回合通常要求融合跨论文的多模态证据来生成结构化答案。

主要模块与组件包括：
1.  **基准构建流水线**：首先从公开渠道收集种子论文，然后利用Connected Papers工具通过引文图扩展候选论文池，形成一个包含485篇论文的源语料库。接着使用大语言模型草拟情景式问题链，并生成包含目标论文和具体图表目标的工具调用检查表。最后，由领域专家进行人工精炼、验证和整理，确保高质量。
2.  **智能体框架**：实现了一个可复现的智能体接口，耦合大型多模态模型、外部工具和持久化记忆。智能体在每回合接收问题和记忆状态，通过函数调用循环决定是否及如何调用工具。提供了四个核心工具：网络搜索（定位论文）、PDF提取器（解析论文）、PDF提取器RAG（在论文内检索相关文本）和内容提取器（提取指定图表）。记忆模块按时间顺序存储所有访问过的内容。
3.  **评估指标体系**：设计了多维度评估指标：(a) **情景成功率**：要求所有回合均答对方算成功；(b) **证据正确率**：衡量智能体在答对的回合中实际访问了多大比例的必要证据单元，以区分“幸运猜测”；(c) **最小化差距**：在成功的情景中，计算智能体工具调用次数与预设最小可行路径的比值，评估效率；(d) **基于轨迹的错误分析**：对失败情景进行归因分析。

关键创新点在于：
1.  **聚焦多轮研究情景**：评估完整的短期科研工作流而非孤立问题，捕捉迭代检索、假设渐进细化、跨回合一致性等行为，暴露单轮设置中不会出现的故障模式。
2.  **强调跨论文多模态证据融合**：问题设计迫使智能体必须对齐来自多个图表（通常跨多篇论文）的信息，考验其解读图表、提取数据、协调跨来源实验设置的多模态 grounding 能力。
3.  **要求主动的引文引导搜索**：智能体需根据情景中积累的间接线索主动发现相关论文，而非从明确指定的标题开始，更贴近真实研究场景。
4.  **引入带有过程监督的证据复用机制**：明确标记应在后续回合复用的证据单元，并在最终的高难度回合禁用工具访问，强制基于记忆进行复用，从而实现对智能体是否在适当时机正确复用了早期证据的过程级评估。

### Q4: 论文做了哪些实验？

论文在EpiBench基准上进行了全面的实验评估。实验设置采用ReAct式的工作流，智能体在每轮次中拥有默认10步的有限步骤预算，若超时则有一次额外机会进行总结和回答。评估了8个代表性的大语言模型（LMM）作为智能体骨干，包括4个开源模型（Qwen3-VL-235B-A22B-Instruct/Thinking、GLM-4.5V、Kimi-K2.5）和4个闭源模型（GPT-5-Mini、GPT-5.2、Grok-4.1、Gemini-2.5-Pro），并设置了两位计算机科学博士专家作为人类基线。

主要评估指标包括：整体任务成功率（ESR）、最终轮次准确率（Acc_final）和非最终轮次准确率（Acc_pre）。关键结果显示，所有模型中GPT-5.2表现最佳，在困难子集上的ESR为29.23%，最终轮次准确率为49.23%，非最终轮次准确率为86.46%。开源模型中Kimi-K2.5表现突出，平均ESR达35.35%。人类专家表现显著优于所有模型，平均ESR为85.11%，Acc_final为95.74%。

实验还进行了细粒度的过程级诊断分析，包括证据正确率（EC）和最小化差距（MG）。GPT-5.2和Kimi-K2.5的EC较高（分别达86.10%和84.13%），但MG显示工具调用存在冗余。错误分析将失败归因于检索、感知、记忆读取或推理等环节，发现不同模型的失败模式存在差异：Gemini-2.5-Pro和Qwen3-VL-Thinking主要受检索错误影响，而GPT-5.2和Kimi-K2.5则在感知和推理阶段错误更多。

此外，论文通过消融实验探究了内存约束的影响：允许最终轮次使用工具时，ESR和Acc_final大幅提升，表明跨轮次的多模态证据融合是主要瓶颈；而去除PDF文本RAG工具的影响较小，说明文本检索并非主要限制因素。步骤预算实验表明，将预算从5步增至10步可提升ESR，但进一步增至15步则收益甚微，表明性能瓶颈主要在于证据对齐和内存复用等系统性问题。

### Q5: 有什么可以进一步探索的点？

该论文提出的EpiBench基准在评估多轮、多证据的科研工作流方面迈出了重要一步，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，基准目前侧重于“短”研究流程，未来可扩展至更长期、更复杂的真实科研周期，例如包含假设生成、实验设计、结果复现等环节。其次，当前评估主要依赖客观问答，未来可引入对推理过程、证据链完整性以及决策可解释性的细粒度评估。此外，基准主要针对已发表论文的静态信息，未能涵盖动态科研活动（如代码执行、数据获取、同行评议交流），未来可考虑融入这些维度以提升生态效度。

从技术改进角度看，现有智能体在证据融合与记忆重用方面表现不佳，这提示未来研究需设计更强大的跨模态记忆机制与注意力模型，使智能体能有效关联分散在多篇文献图表中的证据。另一个方向是开发更主动、目标导向的搜索与信息筛选策略，减少无关信息的干扰。最后，该基准为开发可验证、可复现的研究智能体提供了平台，未来可在此基础上探索如何将智能体的决策过程与外部工具（如数据库、代码库）更深度地结合，以实现真正端到端的科研辅助自动化。

### Q6: 总结一下论文的主要内容

该论文提出了EpiBench基准，旨在系统评估多模态智能体在科学研究多轮工作流中的能力。现有基准大多忽视主动搜索、多证据整合及长期证据利用等关键环节，而该工作通过模拟短研究流程来填补这一空白。其核心贡献在于设计了一个情景式多轮多模态评测框架，要求智能体根据给定研究任务，在多篇论文中主动导航，整合图表证据，并利用记忆中的累积信息回答涉及跨文献比较和多图融合的客观问题。

方法上，EpiBench构建了包含过程级评估的细粒度测试与诊断体系，不仅关注最终答案准确性，还追踪智能体在证据收集、对齐与持续使用中的表现。实验结果表明，即使在当前领先模型上，其在困难任务集的准确率也仅为29.23%，凸显了多轮多证据研究工作流仍存在巨大提升空间。该基准为可验证、可复现的研究型智能体提供了重要的评估平台，推动了面向复杂科学推理的智能体能力发展。
