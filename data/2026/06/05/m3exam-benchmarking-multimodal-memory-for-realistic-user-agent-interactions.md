---
title: "M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions"
authors:
  - "Zhengjun Huang"
  - "Wenxuan Liu"
  - "Zhoujin Tian"
  - "Wei Chen"
  - "Junle Chen"
  - "Yuqian Wu"
  - "Fangyuan Zhang"
  - "Qintian Guo"
  - "Xiaofang Zhou"
date: "2026-06-05"
arxiv_id: "2606.07402"
arxiv_url: "https://arxiv.org/abs/2606.07402"
pdf_url: "https://arxiv.org/pdf/2606.07402v1"
categories:
  - "cs.CL"
tags:
  - "多模态智能体"
  - "评估基准"
  - "对话记忆"
  - "跨模态推理"
  - "MLLM"
  - "查询引导"
relevance_score: 9.0
---

# M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions

## 原始摘要

Language agents are increasingly deployed over accumulating multimodal information, yet existing benchmarks assume a human-human form with sparse visuals and straightforward content, evaluating neither reasoning over authentic multimodal file interaction nor the interpretation of concealed user information. We therefore introduce M$^3$Exam, a query-centric multimodal conversational memory benchmark built on realistic user-agent interaction, with multi-dimensional evaluation spanning cross-modal grounding and implicit information inference. Benchmarking MLLMs and memory systems reveals persistent gaps in cross-modal grounding, cross session reasoning, and the efficiency cost of accumulating multimodal context. We further propose M$^3$Proctor, a multimodal memory method that detects query modality bias and consumes raw visual sources only on demand, improving accuracy by 13% while cutting index-construction time and retrieved tokens by over 70%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前语言智能体在真实多模态用户交互中面临的核心评估缺失问题。研究背景是，随着AI智能体向现实世界部署，多模态个人助手成为代表性场景，其核心挑战从单轮感知转向管理长期、异质的跨会话多模态历史（包含文本、图像、PDF等）。现有基准方法存在明显不足：早期基准仅限文本，忽略了视觉模态；后续多模态基准虽引入图像，但将其视为静态快照，缺乏对PDF等文档级工件的处理，且评估维度单一，主要关注检索或简单多跳推理，无法衡量跨模态推理、隐含信息解读等能力。同时，几乎所有现有基准都假设用户信息被完全陈述，忽视了需要通过历史间接推断未明说意图的“隐含推理”场景。

因此，本文要解决的核心问题是：缺乏一个能真实反映用户-智能体交互中多模态记忆复杂性的基准。该基准需同时评估三个维度：1）内容复杂性（跟踪管理异构多模态工件）；2）推理复杂性（跨模态连接，如将咖啡视觉状态与过去的PDF关联）；3）意图复杂性（推断未明说的用户上下文，如从历史推断用户是咖啡师或家长）。通过提出M³Exam基准，本文旨在填补这一空白，推动智能体在多模态记忆、跨模态推理和隐含信息解读方面的能力评估。

### Q2: 有哪些相关研究？

相关研究可归为评测类与系统类。评测方面，早期多轮文档问答（如MMLongBench-Doc、MultiDoc2Dial）将文档作为静态输入，未考虑积累的记忆；后续转向对话历史，LongMemEval等关注文本长记忆检索，LoCoMo引入了图像但仅作为话题锚点，MMDialog、MMRC、Mem-Gallery等支持多会话多模态，但未涉及隐含意图推理。本文的M³Exam在此基础上，聚焦真实积累的多模态文件交互，并专门评测跨模态推理与隐含信息推断，弥补了现有基准的空白。系统方面，文本记忆系统（A-Mem、Mem0、MemoryOS）通过笔记网络或事实压缩管理记忆，多模态系统（Universal-RAG、MemVerse、MIRIX）则支持跨模态检索，但均采用全局检索策略，不区分查询是否需视觉证据。本文提出的M³Proctor通过检测查询的模态偏向，仅在需要时消耗原始视觉资源，相比全局方法在准确性上提升13%，同时将索引构建时间和检索令牌数降低超70%。

### Q3: 论文如何解决这个问题？

M³Proctor的核心方法是通过显式建模查询的模态偏好，并采用级联策略来优化多模态记忆的检索与推理。整体框架分为索引构建和模态感知推理两大阶段。

首先在索引构建阶段，系统将所有原始视觉模态（图片、文档、图表）投影为带模态标签的文本替代物，关键创新是仅用低成本的文本描述和数值转录来保留视觉信息，避免直接存储高维视觉token。每个chunk附有二进制模态标签，并额外添加跨会话摘要chunk以保留时序信号。

在推理阶段的核心创新是级联策略：第一步，用指令微调LLM检测查询的模态偏好，返回二值向量表示查询依赖何种模态，同时基于此偏好对检索结果进行重排序，通过偏置调制得分公式巧妙提升含相关模态chunk的排名，整个过程无多模态计算成本。第二步，尝试仅用文本替代物回答查询，并通过置信度测试判断是否可靠——当文本答案不可靠或模态偏好未满足时，才触发视觉源消耗。基于融合模态证据分来决定是否以及何时调用原始视觉源，该分数融合了检索chunk中模态占比、检测到的偏好和表面词汇线索三个信号。

关键创新点包括：将模态偏好作为一等信号用于重排序；端到端一致的模态决策；以及成本感知的级联机制，使得大多数纯文本可答查询在一阶段完成，仅必要时才消耗昂贵视觉资源。

### Q4: 论文做了哪些实验？

该论文在M³Exam基准上进行了全面实验。实验设置包括两类系统：前沿多模态大模型（如Claude-Opus-4.6、GPT-5.4、GLM-5.1等）作为无记忆基线，以及基于Qwen-2.5-VL-7B骨架的智能体记忆系统（文本方法包括NaiveRAG、A-Mem、Mem0等；多模态方法包括UniversalRAG、MemVerse、NGM、MIRIX及所提出的M³Proctor）。评估指标包括精确匹配（EM）、Token级F1、BLEU-1和LLM-Judge分数（使用Qwen2.5-VL-32B-Instruct作为裁判），并计算综合得分。主要结果：最强前沿模型GLM-5.1综合得分仅0.549，表明基准远未解决。交叉模态和隐式意图问题是瓶颈，模型在单会话推理上表现良好，但在交叉模态推理（MR，MLLM得分0.468）和隐式推断（II，0.052）上急剧下降。所提出的M³Proctor在记忆系统中取得最佳综合得分0.484（相比之前最佳0.456），在难度最大的MR（LLM-J 0.606）、II（0.652）和FM（EM 0.569）上领先。同时，M³Proctor将准确率提升13%，索引构建时间和检索Token减少超70%，在7B骨干网络上超越了多个前沿MLLM。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：当前基准主要针对单轮问答，而真实用户交互往往涉及多轮长程对话，意图会动态演变，记忆也需要迭代更新。未来可以构建动态多轮记忆评估场景，测试智能体在连续交互中的记忆整合与推理能力。此外，M³Proctor在需要深度解释的隐式意图推断问题上表现有限，说明当前方法对用户隐式状态的建模仍不充分。改进方向包括：引入更精细的隐式状态推理模块，例如利用用户行为轨迹或情感信号辅助理解；或者设计分层记忆结构，区分显式事实与隐式意图的存储与检索。同时，当前方法依赖单次查询时的模态判断，未来可探索跨会话的模态偏好动态学习，避免重复加载视觉信息。从效率看，虽然级联机制降低了开销，但索引构建仍需优化，例如采用渐进式索引更新策略以适应持续增长的交互历史。

### Q6: 总结一下论文的主要内容

这篇论文针对现有AI Agent基准测试中，缺乏对多模态文件交互和隐式用户信息理解的评估问题，提出了M$^3$Exam基准测试。该基准以用户与Agent的真实交互为中心，构建了查询导向的多模态对话记忆评估，涵盖跨模态基础和隐式信息推理等多个维度。评估发现，现有MLLM和记忆系统在跨模态基础、跨会话推理以及累积多模态上下文的效率方面存在明显不足。为此，论文提出了M$^3$Proctor多模态记忆方法，通过检测查询的模态偏向，仅在需要时调用原始视觉源，从而在提升13%准确率的同时，将索引构建时间和检索token量缩减超过70%。这项研究揭示了当前多模态Agent在长期记忆推理上的局限，并为构建更高效的记忆系统提供了新思路。
