---
title: "GeoBrowse: A Geolocation Benchmark for Agentic Tool Use with Expert-Annotated Reasoning Traces"
authors:
  - "Xinyu Geng"
  - "Yanjing Xiao"
  - "Yuyang Zhang"
  - "Hanwen Wang"
  - "Xinyan Liu"
  - "Rui Min"
  - "Tianqing Fang"
  - "Yi R. Fung"
date: "2026-04-05"
arxiv_id: "2604.04017"
arxiv_url: "https://arxiv.org/abs/2604.04017"
pdf_url: "https://arxiv.org/pdf/2604.04017v1"
github_url: "https://github.com/ornamentt/GeoBrowse"
categories:
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Multimodal Agent"
  - "Visual Reasoning"
  - "Knowledge-Intensive Query"
  - "Agentic Workflow"
  - "Reasoning Traces"
  - "Geolocation"
relevance_score: 8.5
---

# GeoBrowse: A Geolocation Benchmark for Agentic Tool Use with Expert-Annotated Reasoning Traces

## 原始摘要

Deep research agents integrate fragmented evidence through multi-step tool use. BrowseComp offers a text-only testbed for such agents, but existing multimodal benchmarks rarely require both weak visual cues composition and BrowseComp-style multi-hop verification. Geolocation is a natural testbed because answers depend on combining multiple ambiguous visual cues and validating them with open-web evidence. Thus, we introduce GeoBrowse, a geolocation benchmark that combines visual reasoning with knowledge-intensive multi-hop queries. Level 1 tests extracting and composing fragmented visual cues, and Level 2 increases query difficulty by injecting long-tail knowledge and obfuscating key entities. To support evaluation, we provide an agentic workflow GATE with five think-with-image tools and four knowledge-intensive tools, and release expert-annotated stepwise traces grounded in verifiable evidence for trajectory-level analysis. Experiments show that GATE outperforms direct inference and open-source agents, indicating that no-tool, search-only or image-only setups are insufficient. Gains come from coherent, level-specific tool-use plans rather than more tool calls, as they more reliably reach annotated key evidence steps and make fewer errors when integrating into the final decision. The GeoBrowse bernchmark and codes are provided in https://github.com/ornamentt/GeoBrowse

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前评估深度研究智能体（Deep Research Agents）在复杂多模态任务中工具使用能力的基准测试不足的问题。研究背景是，现实世界任务（如地理定位）通常需要从开放网络收集分散的证据，并结合多模态信息（尤其是模糊的视觉线索）进行多步推理和验证。现有的文本基准（如BrowseComp）专注于文本信息的碎片化和多跳浏览验证，但缺乏对视觉线索处理的要求；而现有的多模态基准要么侧重于困难的视觉感知，要么将图像处理作为以文本为主的推理链中的单一环节，未能同时强调**模糊视觉线索的提取与组合**以及**基于证据的、知识密集型的多跳查询验证**。

现有方法的不足主要体现在三个方面：首先，许多广泛使用的地理定位数据集（如MP-16、GLDv2等）仅提供坐标或粗略标签，缺乏专家逐步标注的推理轨迹，这偏向于纯视觉的位置预测，而非工具驱动的推理评估。其次，一些声称可解的基准（如GeoVista、GeoComp）往往过滤掉依赖细微环境信号的困难案例，只保留显著地标，降低了任务难度和真实性。第三，对智能体工具使用的评估不够全面，现有工作很少系统测试图像处理、浏览等广泛的工具组合。

因此，本文要解决的核心问题是：**如何构建一个能够综合评估智能体在需要结合弱视觉线索提取与开放网络证据验证的多步骤、知识密集型任务中工具使用能力的基准**。为此，论文引入了GeoBrowse基准，它包含两个层级：Level 1侧重于从碎片化的弱视觉线索中进行组合推理；Level 2则进一步增加了长尾知识需求和实体混淆，要求进行BrowseComp风格的多跳查询和验证。同时，论文提供了配套的智能体工作流程GATE和专家标注的逐步推理轨迹，以支持对工具使用规划和推理轨迹的深入分析。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：方法类与评测类。

在**方法类**研究中，近期自主网络智能体在开放域信息检索与整合方面展现出潜力，但多模态环境下的工具使用更为复杂，需融合视觉线索与文本知识及外部验证。现有工作探索了多模态思维链提示、结构化视觉推理，以及基于多模态检索增强生成（RAG）的知识 grounding。然而，这些方法往往未能紧密耦合图像推理与网络搜索验证：BrowseComp风格的多模态基准主要依赖文本搜索提升难度，视觉作用有限；而“think-with-image”基准则强调视觉操作，缺乏同等挑战性的开放网络推理。本文通过地理定位任务弥合这一缺口，要求智能体同时执行图像推理与网络搜索以整合碎片化证据。

在**评测类**研究中，早期基于图像的地理定位基准主要提供坐标监督用于识别或检索，未明确针对多步推理或工具使用。跨视角数据集专注于受限区域内街景与航拍图像的匹配，而近期大规模街景库虽扩展了地理覆盖，但仍强调单张图像的定位。最新研究开始纳入人类信号或有限工具交互（如聚合人类游戏数据、支持缩放和网络搜索），但现有基准很少结合全球可定位图像、高难度信息检索查询以及专家标注的多模态工具使用步骤轨迹。本文提出的GeoBrowse填补了这一空白，提供了支持轨迹级分析的专家标注推理痕迹，以评估需同时进行图像推理和网络验证的智能体框架。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GeoBrowse的基准测试集，并配套提出一个名为GATE（Geolocation Agentic-workflow with Tool Enhancement）的智能体工作流来解决评估智能体在结合视觉推理与知识密集型多跳查询方面能力的问题。

**核心方法与整体框架**：论文的核心方法是创建一个两层级（Level 1和Level 2）的基准测试集，并设计一个结构化的工具增强型智能体工作流来应对挑战。整体框架遵循ReAct（推理-行动）风格的交互循环。智能体接收输入图像，然后进入一个循环：在“思考”阶段总结现有证据并规划下一步；在“行动”阶段调用工具；在“观察”阶段接收工具返回的结果并更新状态，直至得出最终答案。

**主要模块/组件与关键技术**：
1.  **GeoBrowse基准测试集**：
    *   **Level 1**：专注于从图像中提取和组合模糊的视觉线索（如标志、建筑风格、植被），平均每个实例包含约3个线索，测试视觉推理能力。
    *   **Level 2**：在Level 1基础上，将地理定位答案作为起点，在维基百科超链接图上构建多跳推理链。通过使用大语言模型对中间实体进行模糊化描述，生成知识密集型查询，要求智能体必须先进行视觉定位，再进行多跳的信息检索与验证。

2.  **GATE智能体工作流与工具套件**：
    *   **“随图思考”工具**：包含5个专门用于精细化图像分析的工具，如裁剪、旋转、辅助线、局部超分辨率和像素分析，旨在提取那些容易被单一前向传递所忽略的微弱、局部化视觉线索。
    *   **知识工具**：包含4个用于开放网络信息获取与验证的工具，如网络图片搜索、网络文本搜索、特定网页访问（用于目标导向的页面阅读）以及代码解释器（用于符号计算）。
    *   **轨迹内图像注册表**：这是一个关键的技术创新。为了解决在交互轨迹中不断产生新图像（如裁剪后的图片、搜索到的图片）所带来的上下文管理、引用混乱和成本问题，系统维护一个持久的图像注册表。每个图像被分配一个唯一的`img_id`，并关联其指针、简短描述和来源元数据。智能体通过`img_id`来引用图像，环境负责解析，这大大提高了多模态工具使用的鲁棒性和效率。

**创新点**：
*   **基准设计创新**：GeoBrowse首次将**弱视觉线索组合**与**BrowseComp风格的多跳知识验证**紧密结合在一个任务（地理定位）中，通过两个精心设计的层级系统性地评估智能体的多模态推理与工具使用规划能力。
*   **工作流与工具创新**：提出的GATE工作流不仅提供了结构化的工具套件（分为视觉与知识两类），还引入了**图像注册表机制**，有效管理了多步推理中产生的复杂视觉状态，解决了长期交互中图像引用和追溯的实践难题。
*   **评估深度**：论文不仅提供最终答案的评估，还发布了**专家标注的、基于可验证证据的逐步推理轨迹**，支持对智能体决策过程进行轨迹级分析，从而更深入地理解工具使用策略的有效性（例如，实验发现性能提升源于连贯的、针对层级的工具使用计划，而非单纯增加工具调用次数）。

### Q4: 论文做了哪些实验？

论文在GeoBrowse基准上进行了全面的实验评估。实验设置方面，作者提出了一个名为GATE的智能体工作流，包含五个“图像思考”工具和四个知识密集型工具，并采用固定的协议、工具套件和调用预算进行标准化工具使用评估。

数据集/基准测试为GeoBrowse，包含两个难度级别：Level 1侧重于提取和组合碎片化的视觉线索；Level 2通过注入长尾知识和模糊关键实体来增加查询难度，需要多跳检索和验证。评估指标主要使用准确率（pass@1），并通过LLM-as-judge进行判断。

对比方法分为三类：
1.  **直接推理**：模型无需工具调用直接给出答案，评估了包括GPT-4o/5系列、Gemini系列、Claude-4.5-Opus、Llama-3.2-90B、Qwen-VL系列在内的多个大模型。
2.  **开源智能体**：选取了三种具有互补工具能力的代表性智能体：专注于搜索的OmniSearch、支持端到端网络搜索和浏览验证的WebWatcher，以及提供代码驱动视觉操作的PyVision。
3.  **GATE**：论文提出的方法，在不同骨干模型上使用标准化的工具套件进行评估。

主要结果与关键数据指标如下：
*   GATE consistently outperforms direct inference and open-source agents. For example, with GPT-4o backbone, GATE improves accuracy from 23.1% to 31.8% on Level 1 and from 11.9% to 21.8% on Level 2, surpassing OmniSearch (24.6%, 18.8%) and PyVision (29.6%, 13.9%).
*   The best performance is achieved by GATE with Gemini-3-Pro backbone, reaching 48.2% on Level 1 and 34.7% on Level 2.
*   Fine-grained localization (city-level) is substantially harder than coarse-grained (state/country).
*   **单工具消融实验**表明，在Level 1上，仅使用图像处理器（Image Processor）可获得38.6%的准确率，接近全工具设置的39.7%；在Level 2上，最佳单工具设置（Web Text Search + Visit）为27.0%，与全工具设置的30.7%存在3.7%的协同差距，说明工具协调在Level 2中更为重要。
*   **固定策略与智能规划对比**显示，智能规划（Agentic planning）优于固定工具使用策略（Fixed policy），且该优势在难度更高的Level 2上更为明显。例如，GPT-4o在Level 2上，智能规划比固定策略的准确率高出6.2%。
*   **轨迹级分析**揭示了强模型（如GPT-5、Gemini-3-Pro）和弱模型（如Qwen系列）的失败阶段不同：强模型在错误时仍能覆盖较多关键证据步骤（里程碑命中率57-59%），但可能在合成或验证阶段失败；弱模型则在早期提取或实体定位阶段就出现崩溃（里程碑命中率显著下降）。
*   **错误诊断**将失败分为六类，结果显示强模型的主要错误集中在证据合成与最终决策失败（E6，占38.2-39.7%），而弱模型的主要错误在于感知与实体定位失败（E1）及检索策略与查询失败（E2）。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于数据集规模和分布：GeoBrowse作为专家标注的高质量基准，样本量有限，且存在地理覆盖不均、国家层级实例占主导的分布偏差。未来研究可首先扩展数据集规模与多样性，纳入更多城市/地标层级的实例，并平衡全球区域覆盖以减少偏差。其次，可探索更自适应的智能体规划机制，当前GATE依赖预设工具组合，未来可引入动态工具选择或基于强化学习的策略优化，以提升跨场景泛化能力。此外，可研究多模态融合的增强方法，如结合视觉语言模型进行更细粒度的线索提取，或引入外部知识图谱辅助验证。最后，基准评估可扩展至更复杂的真实世界场景，如动态环境下的增量推理或对抗性干扰下的鲁棒性测试，以推动智能体在开放域任务中的实用化进展。

### Q6: 总结一下论文的主要内容

GeoBrowse是一个结合视觉推理与知识密集型多步查询的地理定位基准，旨在评估智能体在多模态工具使用中的能力。其核心贡献在于填补了现有基准的空白，要求智能体整合模糊的视觉线索并通过开放网络证据进行多跳验证。基准分为两级：第一级测试从图像中提取和组合碎片化视觉线索的能力；第二级通过引入长尾知识和模糊关键实体来增加查询难度。

论文提出了一个名为GATE的智能体工作流程，配备了五类图像思考工具和四类知识密集型工具，并提供了专家标注的、基于可验证证据的逐步推理轨迹，以支持轨迹级分析。实验表明，GATE在性能上超越了直接推理和开源智能体，证明了无工具、仅搜索或仅图像的方法均不足。性能提升主要源于连贯且针对特定层级的工具使用规划，而非单纯增加工具调用次数，这使得系统更可靠地达到标注的关键证据步骤，并在整合信息进行最终决策时犯错更少。

该工作的意义在于为评估智能体的工具使用与复杂推理提供了标准化测试平台，强调了多模态信息融合与规划在解决现实世界模糊任务中的重要性。
