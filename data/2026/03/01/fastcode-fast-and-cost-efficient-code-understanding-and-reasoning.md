---
title: "FastCode: Fast and Cost-Efficient Code Understanding and Reasoning"
authors:
  - "Zhonghang Li"
  - "Zongwei Li"
  - "Yuxuan Chen"
  - "Han Shi"
  - "Jiawei Li"
date: "2026-03-01"
arxiv_id: "2603.01012"
arxiv_url: "https://arxiv.org/abs/2603.01012"
pdf_url: "https://arxiv.org/pdf/2603.01012v2"
github_url: "https://github.com/HKUDS/FastCode"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Code & Software Engineering"
  - "Tool Use & API Interaction"
relevance_score: 9.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "FastCode (structural scouting mechanism, cost-aware policy)"
  primary_benchmark: "SWE-QA, LongCodeQA, LOC-BENCH, GitTaskBench"
---

# FastCode: Fast and Cost-Efficient Code Understanding and Reasoning

## 原始摘要

Repository-scale code reasoning is a cornerstone of modern AI-assisted software engineering, enabling Large Language Models (LLMs) to handle complex workflows from program comprehension to complex debugging. However, balancing accuracy with context cost remains a significant bottleneck, as existing agentic approaches often waste computational resources through inefficient, iterative full-text exploration. To address this, we introduce FastCode, a framework that decouples repository exploration from content consumption. FastCode utilizes a structural scouting mechanism to navigate a lightweight semantic-structural map of the codebase, allowing the system to trace dependencies and pinpoint relevant targets without the overhead of full-text ingestion. By leveraging structure-aware navigation tools regulated by a cost-aware policy, the framework constructs high-value contexts in a single, optimized step. Extensive evaluations on the SWE-QA, LongCodeQA, LOC-BENCH, and GitTaskBench benchmarks demonstrate that FastCode consistently outperforms state-of-the-art baselines in reasoning accuracy while significantly reducing token consumption, validating the efficiency of scouting-first strategies for large-scale code reasoning. Source code is available at https://github.com/HKUDS/FastCode.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在仓库级代码理解与推理任务中面临的“准确性”与“上下文成本”之间的核心矛盾。研究背景是现代AI辅助软件工程（如代码问答、调试、重构）日益依赖LLMs进行大规模代码库的推理，这需要模型能够理解自然语言查询、定位相关代码、追踪跨文件依赖并生成回答。然而，现有方法存在显著不足：通用LLMs因上下文长度限制难以处理整个仓库；简单的检索增强生成方法将代码视为扁平文本块，割裂了代码间关键的结构化依赖关系（如导入、继承、调用链）；而像DeepWiki等方法构建持久化索引则带来高昂的离线开销，不适用于临时性任务；近期兴起的智能体方法（如SWE-agent）虽能通过命令交互迭代探索仓库，但其依赖顺序、全文本读取的遍历方式代价高昂且脆弱，智能体常需反复读取文件并累积历史上下文，导致大量计算资源浪费在无关代码上，成本激增而准确性未必提升。

因此，本文的核心问题是：如何在不牺牲推理准确性的前提下，显著降低仓库级代码推理的上下文获取成本。为此，论文提出了FastCode框架，其核心创新在于将仓库探索与内容消费解耦。它通过一种“结构侦察”机制，首先利用轻量级的语义-结构地图（包含元数据和依赖图）来导航和精确定位相关目标代码，而无需立即读取完整文本内容。只有在目标明确后，才通过一次优化的步骤构建高价值上下文供LLM推理。这种方法旨在避免现有迭代式全文本探索的资源浪费，实现成本与精度的更好平衡。

### Q2: 有哪些相关研究？

相关研究主要可分为代码检索增强生成（RAG）方法和自主编码智能体两大类。

在代码RAG方法中，早期工作（如基于密集语义检索的方法）将代码视为扁平文本进行检索，但忽略了代码内在的结构信息。为改进这一点，近期研究开始融入图或依赖感知的表示，例如**GraphCoder**利用静态结构（如k跳邻域）来检索和丰富上下文，**LocAgent**则结合图索引与智能体导航来迭代定位相关代码。这些方法虽然提升了结构感知能力，但在复杂仓库中高效、低成本地精准定位目标上下文仍面临挑战。

在自主编码智能体方面，代表性框架如**MapCoder**、**CodeAgent**、**SWE-agent**和**OpenHands**，以及商业系统如**Cursor**和**Claude Code**，通常遵循迭代式的“观察-思考-行动”范式。它们通过多轮调用环境工具（如搜索、文件操作、测试）来逐步积累上下文并执行任务。尽管这些智能体在仓库级任务上有效，但其多轮交互导致上下文不断累积，带来了高昂的令牌消耗成本。

本文提出的FastCode与上述工作密切相关，但核心区别在于其“侦察优先”策略。FastCode通过将仓库探索与内容消费解耦，首先利用轻量级语义-结构地图进行结构侦察来导航和追踪依赖，从而单步优化构建高价值上下文。这既克服了传统RAG方法结构信号利用不足的局限，又显著降低了智能体方法因迭代探索产生的高令牌消耗，在准确性与成本效率之间实现了更好平衡。

### Q3: 论文如何解决这个问题？

论文通过提出FastCode框架来解决代码理解与推理中准确性与计算成本难以平衡的问题。其核心方法是将代码库的探索与内容消费解耦，采用结构引导的导航策略来构建高价值上下文，从而在单次优化步骤中完成推理。

整体框架包含三个主要组件：首先是**代码语义-结构表示**，它通过多层级依赖图统一了混合索引。具体而言，将代码库解析为文件、类、函数和文档四个层级的层次树，并为每个节点提取轻量级元数据（如类型签名、文档字符串），形成一个高效的骨架视图。同时，采用**双索引机制**，结合基于BM25的稀疏索引（用于精确符号匹配）和基于嵌入模型的稠密索引（用于捕获语义相似性），并构建一个多层的代码关系图（包括依赖层、继承层和调用层）来捕捉跨文件的拓扑关系。

其次是**代码库上下文导航机制**，其创新在于引入了**结构侦察策略**。在导航阶段，系统首先对查询意图进行分类和增强，包括查询重写和关键词扩展，并利用LLM生成伪代码提示作为结构锚点。随后，代理使用目录遍历和代码库搜索两种导航工具，基于返回的轻量级元数据（如文件路径、匹配密度）来评估候选单元的相关性，而无需读取完整代码内容。导航过程是自适应的迭代工作流：初始回合结合检索流和工具探索流获取候选，并通过图扩展纳入非词汇依赖关系；后续回合中，代理根据聚合的元数据视图（包括来源、结构身份和成本指标）决定保留哪些单元以及是否继续侦察。

第三是**成本感知的上下文管理策略**，它将上下文构建形式化为一个状态感知的自适应过程。系统在每一步维护一个状态向量，综合查询复杂度、仓库熵、资源消耗、迭代深度和认知置信度等因素。策略基于动态预算和迭代控制来运作：根据环境复杂度分配动态行数预算，并通过认知置信度决定执行快速路径（高置信时跳过昂贵操作）还是迭代扩展。在扩展过程中，监控信息增益率，当达到充分性、低效率或预算耗尽条件时终止。最后，通过基于优先级的上下文选择，依据相关性、工具发现标记和信息密度对单元进行评分，并贪婪地选择最高分单元直至达到预算，从而在有限资源内最大化推理置信度。

### Q4: 论文做了哪些实验？

论文在四个基准数据集上进行了全面的实验评估。实验设置方面，FastCode框架以Gemini-3-Flash等LLM为骨干模型，与三类基线方法进行了对比：1）直接使用LLM（零样本和全上下文模式）；2）基于RAG的方法（如Func RAG、Sliding RAG、File BM25 RAG）；3）基于智能体和流程的方法（如SWEQA-Agent、OpenHands、LocAgent）；4）商业工具（如DeepWiki、Cursor、Claude Code）。

使用的数据集/基准测试包括：SWE-QA（评估仓库级问答）、LongCodeQA（评估长上下文理解和跨文件推理）、LOC-BENCH（特别是SWE-Bench-Lite子集，评估真实维护场景中的故障定位能力）以及GitTaskBench（评估复杂、可执行仓库任务的端到端性能）。

主要结果如下：在SWE-QA上，FastCode总得分达到43.28，显著优于直接LLM（32.30）、Func RAG（39.62）和SWEQA-Agent（42.33），尤其在完整性和推理能力上提升最大。在LongCodeQA上，FastCode与Gemini 2.5 Pro结合时，在多个上下文窗口大小下均带来性能提升（例如在1M tokens下从69.8提升至80.0）。在LOC-BENCH的定位任务中，FastCode使用Gemini-3-Flash实现了86.13%的Acc@1，优于LocAgent的77.74%。在GitTaskBench上，使用Claude 3.5 Sonnet时任务通过率（TPR）达46.30%，超过OpenHands（40.74%）。关键效率指标显示，FastCode大幅降低了token消耗：在LongCodeQA的256K tokens设置下成本降低超过90%；在LOC-BENCH上比OpenHands等智能体框架便宜18-22倍；在GitTaskBench上，Gemini-3-Flash变体的成本比最先进的智能体低三个数量级。消融实验证实了其混合检索、图扩展和成本感知上下文管理等核心组件的贡献。

### Q5: 有什么可以进一步探索的点？

该论文提出的FastCode框架虽然有效，但其核心局限在于对代码库的“轻量级语义结构图”的构建质量和依赖性。未来研究可首先探索如何更动态、增量地维护此结构图，以应对快速迭代的代码库，避免信息过时。其次，其“成本感知策略”目前可能较为静态，未来可引入强化学习，让模型在探索与利用间动态权衡，并针对不同任务类型（如调试、重构）学习最优导航策略。此外，框架主要针对代码理解，可将其“侦察优先”范式与具体编辑、生成动作更紧密闭环，形成能真正执行复杂软件工程任务的智能体。最后，评估目前集中于基准测试，未来需在真实、庞大的工业级代码库中验证其鲁棒性与实用性。

### Q6: 总结一下论文的主要内容

论文针对大规模代码理解任务中，现有方法因反复迭代读取全文导致计算成本高、效率低的问题，提出了FastCode框架。其核心贡献在于将代码库的探索与内容消费解耦，通过构建轻量级的语义-结构地图，利用结构感知的导航工具和成本感知策略，在单次优化步骤中精准定位依赖关系和高价值上下文，从而避免全文摄入的开销。实验在SWE-QA等多个基准测试中表明，FastCode在推理准确率上优于现有最优方法，同时显著降低了token消耗。这验证了“侦察优先”策略在大规模代码推理中的高效性，为AI辅助软件工程提供了可扩展且资源高效的解决方案。
