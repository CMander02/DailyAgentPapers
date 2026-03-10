---
title: "UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking"
authors:
  - "Chang Liu"
  - "Chuqiao Kuang"
  - "Tianyi Zhuang"
  - "Yuxin Cheng"
  - "Huichi Zhou"
  - "Xiaoguang Li"
  - "Lifeng Shang"
date: "2026-03-09"
arxiv_id: "2603.08117"
arxiv_url: "https://arxiv.org/abs/2603.08117"
pdf_url: "https://arxiv.org/pdf/2603.08117v1"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "信息检索智能体"
  - "多智能体框架"
  - "网页浏览与交互"
  - "基准构建与评估"
  - "工具使用"
  - "指令微调"
  - "现实世界应用"
relevance_score: 8.0
---

# UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking

## 原始摘要

Recent advancements in LLM-based information-seeking agents have achieved record-breaking performance on established benchmarks. However, these agents remain heavily reliant on search-engine-indexed knowledge, leaving a critical blind spot: Unindexed Information Seeking (UIS). This paper identifies and explores the UIS problem, where vital information is not captured by search engine crawlers, such as overlooked content, dynamic webpages, and embedded files. Despite its significance, UIS remains an underexplored challenge. To address this gap, we introduce UIS-QA, the first dedicated UIS benchmark, comprising 110 expert-annotated QA pairs. Notably, even state-of-the-art agents experience a drastic performance drop on UIS-QA (e.g., from 70.90 on GAIA and 46.70 on BrowseComp-zh to 24.55 on UIS-QA), underscoring the severity of the problem. To mitigate this, we propose UIS-Digger, a novel multi-agent framework that incorporates dual-mode browsing and enables simultaneous webpage searching and file parsing. With a relatively small $\sim$30B-parameter backbone LLM optimized using SFT and RFT training strategies, UIS-Digger sets a strong baseline at 27.27\%, outperforming systems integrating sophisticated LLMs such as O3 and GPT-4.1. This demonstrates the importance of proactive interaction with unindexed sources for effective and comprehensive information-seeking. Our work not only uncovers a fundamental limitation in current agent evaluation paradigms but also provides the first toolkit for advancing UIS research, defining a new and promising direction for robust information-seeking systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的信息检索智能体在现实场景中的一个关键盲区：未索引信息检索问题。现有研究主要关注依赖搜索引擎索引的已知信息获取，并在GAIA等基准测试上取得了优异性能。然而，现实世界中大量重要信息并未被搜索引擎爬虫捕获，例如被忽视的网页内容、动态生成的页面以及嵌入文件等，这些构成了未索引信息。现有基准测试未能区分索引与非索引信息，导致智能体在此类任务上的能力未被充分评估与优化。

针对这一不足，本文首先明确了UIS问题的定义及其与现实任务的相关性，并指出当前先进智能体在此类任务上存在严重性能缺陷。为此，研究团队构建了首个专注于UIS评估的基准测试UIS-QA，包含110个专家标注的问答对。实验表明，即使顶尖智能体在该基准上的准确率也大幅下降，凸显了问题的紧迫性。

为解决该问题，本文提出了UIS-Digger——一个新颖的多智能体框架。该框架通过双模式浏览机制支持同步网页搜索与文件解析，并结合监督微调与拒绝采样微调策略优化模型。仅使用约300亿参数的基础模型，UIS-Digger在UIS-QA上取得了优于集成GPT-4.1等复杂模型的性能，证明了主动与未索引源交互的重要性。这项工作不仅揭示了当前智能体评估范式的根本局限，还为推动UIS研究提供了首个工具包，定义了鲁棒信息检索系统的新方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：信息寻求基准、计算机使用基准以及智能体系统方法。

在**信息寻求基准**方面，现有工作如BrowseComp-en/zh、xbench-DeepSearch和GAIA-textual-103，主要评估智能体在开放网络中进行多步探索、搜索和信息提取的能力。然而，这些基准严重依赖搜索引擎已索引的内容，未能涵盖未索引信息。本文提出的UIS-QA基准则首次明确要求智能体依赖未索引信息（如动态网页、嵌入式文件），并强调在真实网络环境中的综合能力。

在**计算机使用基准**方面，WebArena、Mind2Web及其衍生版本（Mind2Web-Live、Online-Mind2Web）专注于评估智能体通过交互式浏览器操作（如点击、输入）完成用户任务的能力。其中，Live版本虽引入了真实网络环境，但其核心仍是工具操作，而非以最终答案为导向的信息整合。UIS-QA则融合了信息寻求与计算机使用，要求智能体主动交互以获取未索引内容，并以确定性答案进行自动评估。

在**智能体系统方法**上，现有先进系统（如基于GPT-4.1或O3的智能体）虽然在传统基准上表现优异，但在UIS-QA上性能骤降，暴露了对未索引信息处理的盲区。本文提出的UIS-Digger框架通过双模式浏览（同时进行网页搜索和文件解析）和相对较小的骨干模型（约300亿参数），针对未索引信息寻求进行了优化，在UIS-QA上超越了依赖更大规模通用模型的方法，为这一新方向建立了强基线。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为UIS-Digger的多智能体框架来解决未索引信息检索问题。其核心方法在于构建一个协同工作的多智能体系统，通过双模式浏览和并行处理能力，主动探索搜索引擎未抓取的信息源。

整体框架包含四个主要智能体模块：规划器、网页搜索器、网页浏览器和文件阅读器。规划器作为顶层协调者，负责解析用户查询并分解为子任务，调度其他智能体执行。网页搜索器同时使用搜索引擎和爬虫工具检索已索引信息，并能将任务委派给浏览器和文件阅读器以获取未索引内容。网页浏览器采用创新的双模式内存共享浏览策略，既能以文本模式高效处理网页内容，又能在需要时切换至视觉模式处理复杂交互元素，如点击、滚动、填写表单等，且两种模式共享内存和浏览器状态，避免了同步开销。文件阅读器则专门处理PDF、XLSX、DOCX等嵌入式文件格式，支持分块读取以应对长文档。

关键技术创新主要体现在三个方面：一是双模式浏览机制，平衡了功能完整性与执行效率；二是多智能体协同架构，实现了对未索引信息的并行探索与解析；三是专门设计的训练流程。训练过程采用合成数据构建与两阶段调优策略：首先从真实网站和模拟环境中构建QA训练对，模拟网站专门针对日期选择器等交互弱点设计；随后通过监督微调阶段使用教师模型生成高质量轨迹，再通过拒绝采样保留正确非平凡轨迹；最后在强化微调阶段引入温度采样和难度加权，提升模型对挑战性任务的解决能力。整个系统仅需约300亿参数的基础大语言模型，通过上述专门优化，在未索引信息检索任务上超越了使用更复杂大模型的主流系统。

### Q4: 论文做了哪些实验？

论文在实验部分主要围绕提出的UIS-QA基准测试和UIS-Digger系统进行评估。实验设置方面，作者在多个先进的信息寻求智能体系统上进行了广泛评估，这些基线方法被分为四类：直接API推理（如DeepSeek-V3.1、Claude-sonnet-4、GPT-5）、商业系统（如GLM-4.5、Doubao、Gemini-2.5-pro）、基于ReAct的框架（如WebSailor、Tongyi DeepResearch）以及多智能体框架（如DDv2、OWL、MiroThinker、Memento、AWorld）。提出的UIS-Digger系统也作为多智能体框架的一部分进行评估，其骨干模型采用了经过SFT和RFT两阶段训练的约30B参数模型（具体为38B-Pangu和Qwen3-32B两个版本）。

使用的数据集/基准测试包括新提出的UIS-QA（包含110个专家标注的QA对），以及传统的信息寻求基准GAIA和BrowseComp-zh（BC-zh），以进行对比。

主要结果和关键数据指标显示在综合评估表中。在UIS-QA基准上，所有基线方法均表现不佳，性能显著下降。例如，在GAIA上准确率超过70%的Tongyi-DR和Memento，在UIS-QA上的准确率分别骤降至23.6%和25.5%。相比之下，UIS-Digger（Pangu和Qwen版本）取得了最高的27.3%的准确率，超越了由O3等复杂大模型驱动的系统（如Memento的25.5%），这证明了其有效性。同时，UIS-Digger在GAIA和BC-zh上也取得了有竞争力的结果（如50.5%、47.6%和32.5%），展示了其通用性。实验还通过错误案例分析揭示了智能体在UIS任务中的关键失败模式，如未能检索到根源网站（Missing retrieval）或即使访问了正确来源也无法得出正确答案，突显了UIS任务的独特挑战性。此外，SFT和RFT训练阶段为UIS-Digger带来了显著的性能提升（例如Pangu骨干模型分别获得13.6%和4.6%的增益）。

### Q5: 有什么可以进一步探索的点？

本文揭示了当前信息检索代理对搜索引擎索引知识的严重依赖，其核心局限在于难以处理未索引信息。UIS-Digger虽建立了基线，但性能仍有巨大提升空间（仅27.27%准确率）。未来可探索：1）**动态与实时信息处理**：当前对动态网页（如需交互生成的表格）和实时更新内容处理不足，需开发更智能的交互式浏览与状态跟踪机制。2）**多模态与跨文件推理**：虽支持文件解析，但对嵌套文件（如ZIP中的PDF）、图像图表中未索引文本的深度提取与关联推理能力薄弱，可结合视觉-语言模型增强理解。3）**搜索策略优化**：实验显示代理常无法定位或误选关键源，需改进搜索查询生成与结果排序，引入强化学习优化多步探索策略。4）**基准扩展与泛化**：UIS-QA仅110个样本，需构建更大规模、跨领域、跨语言的基准，并探索代理在隐私数据、本地网络等真实未索引场景中的泛化能力。5）**轻量化与效率**：当前框架依赖多智能体协作，可能导致计算开销大，未来可设计更高效的单一模型架构，平衡性能与资源消耗。

### Q6: 总结一下论文的主要内容

该论文聚焦于当前基于大语言模型的信息检索智能体存在的一个关键盲区：非索引信息检索问题。UIS指的是那些未被搜索引擎爬虫捕获的重要信息，如被忽视的内容、动态网页和嵌入式文件。论文首先明确了UIS与传统的索引信息检索之间的本质区别，并指出现有基准测试未能充分评估智能体的UIS能力。

为解决此问题，作者提出了首个专门用于评估UIS能力的基准测试UIS-QA，包含110个经过专家标注的问答对。实验表明，即使最先进的智能体在该基准上的性能也出现断崖式下跌，凸显了问题的严重性。

为应对UIS挑战，论文提出了UIS-Digger，一种新颖的多智能体框架。其核心创新在于集成了双模式浏览，允许同时进行网页搜索和文件解析，并支持并行工具执行。此外，作者通过监督微调和拒绝采样微调两阶段策略，对一个相对较小的约300亿参数骨干大模型进行了优化。实验结果显示，UIS-Digger在UIS-QA上取得了27.27%的准确率，超越了集成GPT-4.1等更复杂大模型的系统，为UIS研究树立了一个强有力的基线。

这项工作的核心贡献在于揭示并形式化了UIS这一被忽视的重要问题，提供了首个专门的评估基准和高效的工具框架，强调了主动与未索引信息源交互的必要性，为构建更鲁棒、全面的信息检索系统定义了一个新的研究方向。
