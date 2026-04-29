---
title: "AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery"
authors:
  - "Lei Xiong"
  - "Kun Luo"
  - "Ziyi Xia"
  - "Wenbo Zhang"
  - "Jin-Ge Yao"
  - "Zheng Liu"
  - "Jingying Shao"
  - "Jianlyu Chen"
  - "Hongjin Qian"
  - "Xi Yang"
  - "Qian Yu"
  - "Hao Li"
  - "Chen Yue"
  - "Xiaan Du"
  - "Yuyang Wang"
  - "Yesheng Liu"
  - "Haiyu Xu"
  - "Zhicheng Dou"
date: "2026-04-28"
arxiv_id: "2604.25256"
arxiv_url: "https://arxiv.org/abs/2604.25256"
pdf_url: "https://arxiv.org/pdf/2604.25256v1"
github_url: "https://github.com/CherYou/AutoResearchBench"
categories:
  - "cs.AI"
tags:
  - "AI Agent Benchmark"
  - "Scientific Literature Discovery"
  - "Multi-step Reasoning"
  - "Information Retrieval"
  - "Evaluation"
relevance_score: 8.5
---

# AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery

## 原始摘要

Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a research problem, or to acquire evidence for verifying assumptions and supporting claims. To assess AI agents' capability in driving this process, we present AutoResearchBench, a dedicated benchmark for autonomous scientific literature discovery. AutoResearchBench consists of two complementary task types: (1) Deep Research, which requires tracking down a specific target paper through a progressive, multi-step probing process, and (2) Wide Research, which requires comprehensively collecting a set of papers satisfying given conditions. Compared to previous benchmarks on agentic web browsing, AutoResearchBench is distinguished along three dimensions: it is research-oriented, calling for in-depth comprehension of scientific concepts; literature-focused, demanding fine-grained utilization of detailed information; and open-ended, involving an unknown number of qualified papers and thus requiring deliberate reasoning and search throughout. These properties make AutoResearchBench uniquely suited for evaluating autonomous research capabilities, and extraordinarily challenging. Even the most powerful LLMs, despite having largely conquered general agentic web-browsing benchmarks such as BrowseComp, achieve only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, while many other strong baselines fall below 5%. We publicly release the dataset and evaluation pipeline to facilitate future research in this direction. We publicly release the dataset, evaluation pipeline, and code at https://github.com/CherYou/AutoResearchBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在自主科学文献发现能力评估上的缺失。研究背景是，随着基于大语言模型的AI科学家系统的发展，自主科学研究成为可能，而其中核心步骤之一是能够精准、全面地发现目标科学文献，以探索已有知识或验证假设。然而，现有方法存在明显不足：首先，当前主流的智能体网络浏览基准测试（如GAIA、BrowseComp）主要评估通用信息检索能力，其任务更偏向常识性推理和浅层匹配，无法衡量智能体对专业、前沿且领域特定的科学概念的深度理解。其次，科学文献发现更具挑战性：关键证据往往隐藏在论文的详细方法、消融实验表格、图表标题、附录及引用链等细粒度内容中，而非元数据或摘要；且搜索任务具有开放性，合格论文的数量未知，甚至可能为零，要求智能体具备复杂的推理、验证和终止搜索的决策能力。因此，本文提出了AutoResearchBench这一专用基准，核心目标是精准评估AI智能体在处理科研级复杂文献发现任务时的自主能力，填补了现有基准在科学研究专业性和深度上的空白。

### Q2: 有哪些相关研究？

---

**相关研究**

本文的相关工作可分为两类：**学术搜索智能体（方法类）** 与 **学术搜索基准（评测类）**。

1.  **学术搜索智能体**：这类工作聚焦于构建专门面向学术文献的搜索代理。例如 PaSa 和 SPAR 定制了针对学术语境的搜索与推理流程，能导航数字图书馆、提取方法论细节。与它们相比，本文不提出新智能体，而是提供一个用于评估这些智能体的基准，其特点在于强调对科学概念的深层理解、细粒度文献信息利用，以及开放式的搜索未知结果。

2.  **学术搜索基准**：早期基准如 GAIA 和 BrowseComp 主要评估通用网络浏览能力，而 WideSearch 等专注于特定搜索模式。近期工作如 DeepWideSearch 试图统一深度和广度搜索范式，但这些开放网络数据集缺乏受控语料，不适合严谨的科学评估。在学术领域，RealScholarQuery 和 SPAR 提供领域特定挑战但规模有限，SAGE 拥有受控语料却缺乏动态交互环境。与它们不同，**AutoResearchBench** 是首个大规模、在受控学术语料库中系统评估动态智能体执行深度与广度搜索双重任务的基准，填补了现有工作缺乏可控性与交互性的空白。

### Q3: 论文如何解决这个问题？

AutoResearchBench通过构建两个互补的任务来评估AI智能体的科学文献发现能力。在整体架构上，它设计了深度研究和宽泛研究两个框架，分别对应精确文献定位和全面文献覆盖。核心技术方法包括：深度研究采用全文本优先流水线，通过从论文完整内容（包括附录、消融实验、证明细节等非显著信息）中提取自然语言约束条件，基于最小充分性原则逐步缩小候选集直至唯一目标论文，并包含无答案实例来测试智能体的否决能力。宽泛研究则基于学术实体图，通过领域候选收集、结构抽象与查询公式化、查询精炼与验证、迭代扩展与审计的四阶段流程，系统性枚举满足特定科学约束的完整论文集合。

在具体实现上，系统采用ReAct智能体框架与DeepXiv搜索工具交互，该工具提供结构化元数据和全文访问能力，特别适合需要长期探索和全文浏览的科学搜索场景。关键创新点包括：将引用关系转化为显式子问题实现多跳搜索、通过主题级和细节级模糊化处理抑制词汇捷径、以及通过迭代剪枝移除冗余约束。该基准测试面向研究导向，要求深度理解科学概念，并具有开放结局特性，需要智能体进行精细化的信息利用和深思熟虑的推理搜索。

### Q4: 论文做了哪些实验？

论文在AutoResearchBench上进行了全面的实验评估。实验设置包括开源模型（如Qwen3.5系列、Deepseek-V3.2、MiniMax-M2.5、Kimi-K2.5）和闭源模型（如Qwen3-Max、Seed 2.0 Pro、Gemini系列、GPT-5.4、Claude系列），以及三个端到端研究系统（Alphaxiv、GPT DeepResearch、AI Studio Gemini-3.1-pro）。所有模型在统一ReAct智能体框架下使用DeepXiv搜索工具，端到端系统随机采样50个查询。主要结果：Deep Research任务最好成绩是Claude-Opus-4.6的9.39%准确率，Wide Research任务最好成绩是Gemini-3.1-Pro-Preview的9.31% IoU。多数模型得分低于5%。额外实验包括：对比DeepXiv与开放网络搜索工具（WebSearch），显示DeepXiv更优（平均准确率5.42% vs 3.97%）；对比思考模式（Think vs NoThink），发现显式推理未带来一致收益；测试时扩展实验显示，pass@k对Deep Research有更明显提升。

### Q5: 有什么可以进一步探索的点？

从论文的实验结果来看，当前AI agent在科学文献发现任务上的表现与人类专家存在巨大差距（<10%），这揭示了几个关键局限和未来方向。首先，基准测试的**检索空间过于庞大**（300万篇论文）且**语义复杂度高**，现有模型在长文本理解与精准信息定位上明显不足。未来可探索**分层注意力机制**或**检索增强生成（RAG）的改进版**，通过先粗筛再细读的迭代策略缩小搜索范围。其次，**开放性与无限候选集**（Wide Research）要求模型具备动态策略调整能力，当前模型往往陷入局部最优或过早终止搜索。可以考虑引入**强化学习**或**蒙特卡洛树搜索**的决策框架，让agent根据已获取证据动态规划下一步搜索动作。最后，**跨论文的推理整合**（如对比多篇论文的结论）尚未被充分评估，未来可设计基于**知识图谱**的中间表征，增强模型对分散信息的逻辑聚合能力。这些改进方向将推动agent从“信息检索”向“科学推理”跃迁。

### Q6: 总结一下论文的主要内容

AutoResearchBench 是一个用于评估AI智能体在自主科学文献发现能力上的基准测试。该基准定义了两个互补的任务类型：Deep Research（深度研究）和Wide Research（广泛研究）。前者要求智能体通过逐步探查来定位一篇特定的目标论文，后者则要求全面收集满足给定科学条件的所有论文。与通用网页浏览基准不同，AutoResearchBench具有三个核心特性：研究导向性（需要深度理解科学概念）、文献聚焦性（需利用论文中的图表、参考文献等细粒度信息）和开放性（符合条件的论文数量未知，需要智能体判断搜索是否完成）。基于超过300万篇arXiv论文构建的评估环境显示，即使是最强大的大语言模型，在该基准上也表现挣扎：Deep Research任务的最佳准确率仅为9.39%，Wide Research的最佳IoU为9.31%。这一结果揭示了当前AI智能体在科学文献发现这一关键研究步骤上的严重能力缺陷，为发展下一代推理驱动的学术智能体提供了评估基础。
