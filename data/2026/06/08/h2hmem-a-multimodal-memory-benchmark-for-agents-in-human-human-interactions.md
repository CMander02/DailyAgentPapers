---
title: "H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions"
authors:
  - "Shiping Zhu"
  - "Yibo Yang"
  - "Zhengyang Wang"
  - "Tiancheng Shen"
  - "Dandan Guo"
  - "Ming-Hsuan Yang"
date: "2026-06-08"
arxiv_id: "2606.09461"
arxiv_url: "https://arxiv.org/abs/2606.09461"
pdf_url: "https://arxiv.org/pdf/2606.09461v1"
categories:
  - "cs.CL"
tags:
  - "多模态记忆基准"
  - "人机交互"
  - "多轮对话"
  - "记忆召回"
  - "记忆推理"
  - "记忆应用"
  - "LLM Agent评估"
  - "多模态Agent"
relevance_score: 9.5
---

# H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions

## 原始摘要

Large language model agents are increasingly deployed in human-human interaction settings, such as meeting assistants and clinical documentation systems, where they must observe conversations and retain information for downstream queries. Unlike traditional human-assistant settings, these environments are inherently multimodal, involve complex discourse phenomena such as anaphora and deixis, and contain asynchronous or conflicting information from multiple participants. However, existing memory benchmarks largely focus on single-user, text-only interactions, failing to capture these challenges. To address this gap, we introduce H2HMem, a Human-to-Human Multimodal Memory Benchmark for evaluating memory capabilities in complex human-human interactions. H2HMem includes both dyadic and multi-party conversations with multimodal information streams, and evaluates agents along three dimensions: memory recall, reasoning, and application. Experiments with advanced agents reveal substantial limitations in constructing, retaining, and utilizing memories across modalities, participants, and sessions, highlighting substantial room for improvement in next-generation LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有记忆评估基准无法充分适配大语言模型（LLM）智能体在复杂人际交互场景中应用的问题。研究背景是，随着LLM智能体被部署为会议助手、临床文档系统等角色，它们必须被动观察多模态、多人参与的人类对话（如医患对话或多人会议），并基于对话内容进行信息记忆、推理和应用。然而，现有记忆基准主要面向单用户、纯文本的人机对话，忽视了人际交互特有的三大挑战：1) 交互天然具有多模态性（如图片、屏幕截图与文本交织）；2) 对话中存在复杂的语言现象（如照应、指示语），需要智能体结合演进中的对话记忆进行推理，而非简单检索孤立事实；3) 涉及多个参与者，信息可能异步提供甚至相互冲突。现有基准要么仅限于双人互动（如LoCoMo虽支持多模态但无全面评估框架），要么仅支持文本（如EverMemBench虽为多人但无多模态）。因此，本文提出了H2HMem基准，首次在双人与多人互动场景中构建多模态记忆评估框架，覆盖记忆回忆、推理与应用三个维度，系统性地揭示当前多模态大模型在跨模态记忆对齐与结构化推理方面的局限。

### Q2: 有哪些相关研究？

在人类-人类交互中的智能体方面，相关研究开始关注基于LLM的智能体作为对话流观察者的场景，如Zoom AI Companion等商业系统已整合多模态会议内容。本文与其区别在于，H2HMem专门针对多模态、多参与者（包括双人和多人）的复杂交互场景，而非简单的人机助手。

在记忆机制方面，现有方法主要有三类：扩展上下文窗口、检索增强生成和专用记忆模块。这些方法主要在人机助手场景中开发和评估，在人类-人类交互中的有效性未知。本文则专门评估这些机制在更复杂的多模态、多参与者交互中的表现。

在记忆评测基准方面，PersonaMem、LongMemEval、Mem-Gallery和MemoryAgentBench针对人机助手场景；MSC和LoCoMo考虑对话记忆但限于双人交互；EverMemBench扩展到多人对话但未充分探索多模态；MemBench和M3-Bench涉及观察者式智能体但时间范围有限。本文提出的H2HMem是首个同时涵盖多模态、双人与多人交互、长期记忆，并在人类-人类交互场景中提供统一评估框架的基准。

### Q3: 论文如何解决这个问题？

H2HMem通过一个五阶段的人机协作流水线构建多模态记忆基准测试。整体框架包括：(1) 生成二元和多方对话的参与者档案，包含个性、背景等结构化属性；(2) 基于11个常见话题创建多会话场景，LLM为每个话题生成按时间排序的会话大纲和图像关键词；(3) 通过在线搜索、文本到图像生成和人工编辑收集并精炼图像，确保视觉证据与大纲对齐；(4) 利用DeepSeek-V3作为脚本编写器，结合档案、大纲和图像生成对话，由于模型不能直接处理图像，先通过GPT-4o生成详细描述，再替换为实际图像；(5) 构建并人工验证问题-答案对，覆盖记忆回忆、推理和应用三个维度。

主要模块包括：结构化参与者档案、多会话场景大纲、多模态图像集合、对话生成流水线，以及三层记忆评估任务（9种类型）。创新点在于：1) 首次聚焦人类间多模态对话的记忆挑战，涵盖指代、歧义和异步冲突信息；2) 采用人类在环中的质量控制，确保场景一致性和视觉接地；3) 设计细粒度评估维度，包括单模态精确回忆、跨模态关联检索、实体演化追踪、新场景即时学习、矛盾检测和拒绝回答能力。实验发现当前先进代理在多模态、多参与者和跨会话的记忆构建、保留和应用上仍有显著局限。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置上，采用了Qwen2.5-VL系列（3B和7B）及GPT-4.1-Nano作为骨干模型。对比方法包括文本型（Full Text、NaiveRAG、A-Mem）和多模态型（Full MM、MuRAG、NGM），均通过GPT-4o生成的图像描述增强文本方法以实现公平比较。评估指标采用LLM-as-Judge评分（GPT-4o-mini作为零样本评估器，与人类判断的Cohen’s κ=0.84）及精确率（P）、召回率（R）、F1分数和BLEU-1。

主要结果如下：
1. 整体性能低下，最佳加权平均LLM-as-Judge得分仅为0.5757（A-Mem）。
2. 跨模态对齐困难：以MuRAG为例，单模态精确回忆（UPR）与跨模态相关检索（CRR）在LLM-as-Judge得分上存在差距（0.6346 vs. 0.5326）。
3. 干扰过滤能力弱：A-Mem召回率0.4215但精确率仅0.2206，表明难以过滤多人信息中的噪声。
4. 因果推理与指代理解不足：多模态因果推理（MCR）和参考与演化追踪（RET）得分最低，且BLEU-1接近零。
5. 冲突检测（CD）极具挑战，A-Mem的CD召回率仅0.0869。

此外，实验对比了双人（dyadic）与多人（multi-party）交互结构：多人场景下，知识解析（KR）和冲突检测（CD）更困难（NaiveRAG的KR得分从0.4896降至0.2500），而依赖密集上下文的CRR和即时学习（TTL）表现相当。效率分析显示，全记忆方法推理延迟高（文本型17.99秒/查询，多模态型26.09秒/查询），而代理型系统（如A-Mem）虽降低推理延迟（4.57秒/查询）但存储成本极高（351.08秒/会话）。错误分析表明，44%-48%的失败源于模态错位，32%-37%源于讲话者相关错误。

### Q5: 有什么可以进一步探索的点？

当前工作存在几个关键局限和未来方向。首先，跨模态对齐仍是核心瓶颈，模型在跨模态检索（CRR）和细粒度视觉推理（UPR）间存在显著性能落差（如MuRAG下降约10个百分点），未来可探索更紧密的模态融合机制，如动态门控注意力或显式视觉-文本实体映射。其次，干扰过滤能力薄弱，尽管检索召回率较高，但精度低（如A-Mem召回0.4215 vs 精度0.2206），尤其在多说话人场景中冲突检测（CD）几乎失效（BLEU-1趋近0），可引入说话人感知的注意力掩码或基于对话角色的记忆结构化压缩。此外，因果推理与指代消解严重不足，尤其是多模态因果推理（MCR）和引用追踪（RET）得分最低，模型难以处理人类隐式引用和分布证据的关联，可借鉴认知架构的因果链建模或引用记忆的显式溯源。最后，存储-推理效率存在严重权衡（如A-Mem记忆构建耗时351秒/会话），亟需轻量化记忆压缩范式，如基于信息熵的稀疏化存储或异步记忆更新机制。

### Q6: 总结一下论文的主要内容

H2HMem是一个面向复杂人际交互场景的多模态记忆基准测试，用于评估LLM智能体在人类对话中的记忆能力。现有基准大多聚焦于单用户、纯文本交互，无法捕捉人际交互中的多模态特性、复杂话语现象（如指代和照应）以及多参与者的异步或矛盾信息。为此，H2HMem包含双人及多人对话中的多模态信息流，从记忆回忆、推理和应用三个维度评估智能体。实验表明，当前先进智能体在跨模态、跨参与者、跨会话的信息整合上存在显著缺陷：它们能检索相关片段（如图像、事实），但无法将视觉证据与文本对齐、正确归属信息源或解决多来源矛盾。该工作揭示了记忆碎片化到连贯多模态记忆重建的挑战，为下一代LLM智能体的记忆能力提升指明了方向。
