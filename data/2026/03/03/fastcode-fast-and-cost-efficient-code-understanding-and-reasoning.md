---
title: "FastCode: Fast and Cost-Efficient Code Understanding and Reasoning"
authors:
  - "Zhonghang Li"
  - "Zongwei Li"
  - "Yuxuan Chen"
  - "Han Shi"
  - "Jiawei Li"
  - "Jierun Chen"
  - "Haoli Bai"
  - "Chao Huang"
date: "2026-03-01"
arxiv_id: "2603.01012"
arxiv_url: "https://arxiv.org/abs/2603.01012"
pdf_url: "https://arxiv.org/pdf/2603.01012v2"
github_url: "https://github.com/HKUDS/FastCode"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "成本效率"
  - "代码理解"
  - "规划与推理"
  - "软件工程"
relevance_score: 7.5
---

# FastCode: Fast and Cost-Efficient Code Understanding and Reasoning

## 原始摘要

Repository-scale code reasoning is a cornerstone of modern AI-assisted software engineering, enabling Large Language Models (LLMs) to handle complex workflows from program comprehension to complex debugging. However, balancing accuracy with context cost remains a significant bottleneck, as existing agentic approaches often waste computational resources through inefficient, iterative full-text exploration. To address this, we introduce FastCode, a framework that decouples repository exploration from content consumption. FastCode utilizes a structural scouting mechanism to navigate a lightweight semantic-structural map of the codebase, allowing the system to trace dependencies and pinpoint relevant targets without the overhead of full-text ingestion. By leveraging structure-aware navigation tools regulated by a cost-aware policy, the framework constructs high-value contexts in a single, optimized step. Extensive evaluations on the SWE-QA, LongCodeQA, LOC-BENCH, and GitTaskBench benchmarks demonstrate that FastCode consistently outperforms state-of-the-art baselines in reasoning accuracy while significantly reducing token consumption, validating the efficiency of scouting-first strategies for large-scale code reasoning. Source code is available at https://github.com/HKUDS/FastCode.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在仓库级代码理解与推理任务中，**准确性与上下文成本难以平衡的核心瓶颈问题**。

**研究背景**：随着LLM被广泛应用于软件工程工作流（如代码问答、调试、重构），仓库级代码推理变得至关重要。这类任务要求模型能理解自然语言查询，在庞大的代码库中定位相关部分、追踪跨文件依赖，并给出有根据的回答。然而，仓库级推理远比片段级理解复杂，涉及跨文件、符号的多跳依赖追踪。

**现有方法的不足**：当前方法在平衡精度与成本方面存在显著缺陷。1) **朴素方法**（直接输入大量代码）会导致上下文过长，产生高昂的令牌成本，且无关上下文会干扰模型。2) **标准检索增强生成（RAG）** 将代码分块检索，但往往割裂了代码间关键的结构关系（如导入、继承、调用链）。3) **构建持久化仓库索引**（如DeepWiki）在离线阶段开销巨大，不适用于临时性或短生命周期的使用场景。4) **现有智能体（Agent）方法**（如SWE-agent）普遍依赖**顺序的、迭代式的全文本仓库遍历**来定位相关代码。这种探索方式代价高昂且脆弱：每次“读取”操作都消耗大量令牌，迭代循环会累积历史上下文并放大成本，且智能体常常为探索大量无关文件付出高昂代价后，仍可能因提前终止而得到依据不足的答案。

**本文要解决的核心问题**：因此，论文的核心目标是设计一种新框架，以**更低的计算（令牌）成本实现高精度的仓库级代码推理**。具体而言，就是要克服现有迭代式全文本探索方法效率低下、资源浪费的问题，通过一种“侦察先行”的策略，在投入全文本消费之前，先利用轻量级信息高效导航并精确定位相关目标，从而在单次优化步骤中构建出高价值、最小充分的上下文，最终达成准确性与成本效益的双重提升。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：代码检索增强生成（RAG）方法和自主代码智能体（Agent）方法。

在代码RAG方法中，早期工作（如基于密集语义检索的方法）将代码视为扁平文本进行检索，但忽略了代码内在的结构信息，限制了多跳推理能力。后续研究开始融入图或依赖感知的表示以改进检索，例如GraphCoder利用静态结构（如k跳邻域）来丰富上下文，LocAgent结合图索引与智能体导航来迭代定位相关代码。然而，这些方法在复杂仓库中高效、低成本地精确定位目标上下文方面仍面临挑战。

在自主代码智能体方面，代表性框架（如MapCoder、CodeAgent、SWE-agent、OpenHands）以及商业系统（如Cursor、Claude Code）通常遵循迭代的“观察-思考-行动”范式，通过多轮调用工具与环境交互来逐步积累上下文并执行操作。这类方法虽能有效处理仓库级任务，但多轮交互导致上下文不断累积，产生了高昂的令牌消耗成本。

本文提出的FastCode框架与上述工作均相关，但核心区别在于其“先侦察后消费”的策略。它通过将仓库探索与内容消费解耦，利用轻量级语义-结构地图进行结构感知的导航，从而在单次优化步骤中构建高价值上下文。这既克服了传统RAG方法结构信号利用不足或成本高的问题，也解决了现有智能体因迭代式全文探索而导致令牌效率低下的瓶颈，在显著降低令牌消耗的同时保持了优异的推理准确性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为FastCode的、成本感知的智能体框架来解决代码库规模推理中准确性与计算成本之间的权衡问题。其核心方法是**将上下文获取重新定义为结构引导的导航过程**，而非传统的、低效的迭代式全文检索与阅读。整体框架包含三个关键组件，实现了探索与内容消耗的解耦。

**1. 代码语义-结构表示：** 这是框架的基础。与将代码视为扁平文本块的标准RAG方法不同，FastCode构建了一个保留代码库拓扑完整性的整体表示。它首先将代码库解析为包含文件、类、函数和文档四个层次的层次化树结构，并为每个节点提取轻量级元数据（如类型签名、文档字符串、行号范围），形成一个高效的“骨架视图”。同时，它采用**双索引机制**：稀疏索引（BM25）用于精确匹配关键词（如函数签名），而密集索引（嵌入模型）用于捕获隐含语义。更重要的是，它通过基于AST的高效分析，构建了一个包含依赖层、继承层和调用层的**多层有向关系图**，以建模代码单元间的拓扑联系，避免跨文件上下文碎片化。

**2. 代码库上下文导航机制：** 这是核心创新点，旨在以低成本“侦察”来缩小搜索空间，再对高价值目标进行精读。导航始于对查询意图的分类，并实施**双轨增强策略**：一方面重写查询以优化语义匹配，另一方面进行关键词扩展以提升词法检索。此外，系统还利用LLM生成**伪代码提示**，作为结构锚点来匹配代码逻辑。导航过程由智能体驱动，它使用两种工具（目录遍历和代码库搜索）进行探索，但工具返回的是结构元数据而非完整代码。导航采用**自适应侦察工作流**：系统整合来自检索和工具流的候选结果，并通过图扩展纳入逻辑相关的单元；然后，智能体基于包含来源、结构身份和成本指标的聚合元数据视图，迭代决定保留哪些单元或是否发起新的工具调用。

**3. 成本感知的上下文管理策略：** 该策略动态调控信息收集，以在有限预算内最大化推理置信度。它将迭代检索形式化为一个在多维状态空间（包含查询复杂度、仓库熵、资源消耗、迭代深度和认知置信度）中的轨迹。策略的核心是**动态预算与迭代控制**：根据环境复杂度分配动态行数预算，并依据认知置信度决定流程。若初始侦察置信度高，则走“快速路径”直接进入精炼阶段；否则进行迭代扩展，并监控**信息增益率**，在达到置信度阈值、连续低增益或预算耗尽时终止。最后，通过一个**基于优先级的上下文选择**公式，贪婪地选择得分最高的代码单元，直至达到预算上限，确保在成本约束下保留最关键的上下文。

**创新点总结**：1) **“侦察优先”范式**：将探索（基于轻量元数据）与消费（读取完整代码）解耦，从根本上减少了不必要的全文读取。2) **统一语义-结构表示**：结合层次化元数据、双索引和多层关系图，实现了对代码库拓扑和语义的精准建模。3) **成本感知的自适应策略**：通过形式化的状态空间和动态策略，智能地平衡推理准确性与资源消耗。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了全面的实验评估：SWE-QA、LongCodeQA、LOC-BENCH和GitTaskBench，分别对应仓库级问答、长代码理解、文件定位和端到端任务执行能力。

**实验设置与数据集**：实验使用了多个LLM作为骨干模型，包括Gemini-3-Flash、Claude 3.5/3.7 Sonnet、Qwen2.5-14B、Qwen3-Coder-30b等。对比方法涵盖四大类：(1) 直接使用LLM（零样本或全上下文）；(2) 基于RAG的方法（如Func RAG、Sliding RAG、File BM25 RAG）；(3) 智能体与流程化方法（如SWEQA-Agent、Agentless、SWE-agent、OpenHands、LocAgent）；(4) 商业工具（如DeepWiki、CodeWiki、Gemini Code、Claude Code、Cursor）。

**主要结果与关键指标**：
1.  **SWE-QA**：FastCode在总得分上达到43.28，显著优于直接LLM（32.30）、Func RAG（39.62）和SWEQA-Agent（42.33），并在推理（8.72 vs. 4.91）和完整性（7.94 vs. 3.71）上提升最大。
2.  **LongCodeQA**：FastCode在不同上下文窗口大小下均能提升基线LLM性能。例如，Gemini 2.5 Pro在1M窗口下准确率从69.8%提升至80.0%；而Claude 3.5 Sonnet结合File BM25 RAG在32K窗口下性能从65.5%暴跌至25.55%，凸显了FastCode依赖关系感知的优势。
3.  **LOC-BENCH（文件定位）**：FastCode使用Gemini-3-Flash达到Acc@1为86.13%，大幅超越最佳基线LocAgent（77.74%）。即使使用轻量级本地模型Qwen3-Coder-30b，Acc@1仍达75.55%，接近Claude 3.5 Sonnet的性能，且成本极低。
4.  **GitTaskBench（端到端任务）**：FastCode使用Claude 3.7 Sonnet达到任务通过率（TPR）57.41%和执行完成率（ECR）74.07%，优于OpenHands（40.74%）和SWE-Agent（22.23%）。其Gemini-3-Flash版本以更低的成本实现53.70%的TPR，超越了使用更强模型的基线。

**效率优势**：FastCode在显著降低令牌消耗的同时保持或提升准确性。在SWE-QA上比Cursor等商业工具成本降低约55%；在LongCodeQA的256K令牌场景下成本降低超90%；在LOC-BENCH上比OpenHands等智能体框架便宜18-22倍；在GitTaskBench上成本可降低数个数量级（从15倍到超过2000倍）。消融实验证实了其混合检索、图扩展和成本感知上下文管理等核心组件的贡献。

### Q5: 有什么可以进一步探索的点？

该论文提出的FastCode框架在代码库探索与内容消费解耦方面具有创新性，但仍存在一些局限性和值得深入探索的方向。首先，其结构感知导航严重依赖代码的静态语义结构图，对于动态语言特性（如反射、运行时生成代码）或高度复杂的依赖关系可能捕捉不足，未来可研究结合动态分析或执行轨迹来增强上下文理解。其次，成本感知策略目前主要基于token消耗优化，未充分考虑计算延迟、内存占用等实际部署成本，可探索多目标优化策略。此外，框架在超大规模代码库（如千万行级别）中的可扩展性尚未验证，需进一步研究分布式索引与增量更新机制。从方法改进看，可引入强化学习让导航策略自适应不同代码结构与任务类型，或融合视觉化代码表示（如AST图嵌入）以提升结构理解深度。最后，当前评估集中于问答与调试任务，未来可扩展至代码生成、架构重构等更复杂的软件工程场景，以检验其通用性。

### Q6: 总结一下论文的主要内容

论文《FastCode》针对大规模代码库理解与推理任务中，现有方法因反复迭代式全文探索导致计算成本高昂的问题，提出了一种高效且成本优化的解决方案。其核心贡献在于将代码库的探索过程与内容消费解耦，通过构建轻量级的语义-结构地图，利用结构感知的导航工具在单次优化步骤中精准定位高价值上下文，从而避免了传统方法中低效的全文摄入开销。该方法在SWE-QA、LongCodeQA等多个基准测试中均显著超越了现有最优基线，在提升推理准确率的同时大幅降低了令牌消耗。这验证了“先侦察后消费”策略的有效性，为复杂软件工程任务提供了可扩展且资源高效的框架。
