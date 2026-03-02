---
title: "WisPaper: Your AI Scholar Search Engine"
authors:
  - "Li Ju"
  - "Jun Zhao"
  - "Mingxu Chai"
  - "Ziyu Shen"
  - "Xiangyang Wang"
  - "Yage Geng"
  - "Chunchun Ma"
  - "Hao Peng"
  - "Guangbin Li"
  - "Tao Li"
  - "Chengyong Liao"
  - "Fu Wang"
  - "Xiaolong Wang"
  - "Junshen Chen"
  - "Rui Gong"
  - "Shijia Liang"
  - "Feiyan Li"
  - "Ming Zhang"
  - "Kexin Tan"
  - "Junjie Ye"
date: "2025-12-07"
arxiv_id: "2512.06879"
arxiv_url: "https://arxiv.org/abs/2512.06879"
pdf_url: "https://arxiv.org/pdf/2512.06879v2"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agent System"
  - "Agentic Model"
  - "Tool Use"
  - "Reasoning"
  - "Information Retrieval"
  - "Workflow Automation"
relevance_score: 8.5
---

# WisPaper: Your AI Scholar Search Engine

## 原始摘要

We present \textsc{WisPaper}, an end-to-end agent system that transforms how researchers discover, organize, and track academic literature. The system addresses two fundamental challenges. (1)~\textit{Semantic search limitations}: existing academic search engines match keywords but cannot verify whether papers truly address complex research questions; and (2)~\textit{Workflow fragmentation}: researchers must manually stitch together separate tools for discovery, organization, and monitoring. \textsc{WisPaper} tackles these through three integrated modules. \textbf{Scholar Search} combines rapid keyword retrieval with \textit{Deep Search}, in which an agentic model, \textsc{WisModel}, validates candidate papers against user queries through structured reasoning. Discovered papers flow seamlessly into \textbf{Library} with one click, where systematic organization progressively builds a user profile that sharpens the recommendations of \textbf{AI Feeds}, which continuously surfaces relevant new publications and in turn guides subsequent exploration, closing the loop from discovery to long-term awareness. On TaxoBench, \textsc{WisPaper} achieves 22.26\% recall, surpassing the O3 baseline (20.92\%). Furthermore, \textsc{WisModel} attains 93.70\% validation accuracy, effectively mitigating retrieval hallucinations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科研人员在学术文献检索、组织与追踪过程中面临的两个核心挑战。研究背景是科学文献的指数级增长，使得研究人员难以高效地跟进领域进展，现有方法存在明显不足。首先，在语义搜索方面，现有主流学术搜索引擎（如Google Scholar、Semantic Scholar）主要依赖关键词匹配，难以处理复杂的、概念性的研究问题查询（例如“探索上下文学习与推理时缩放关系的论文”）。它们无法深入理解查询的语义，也无法验证检索到的论文是否真正解决了该问题，而不仅仅是提及了相关术语。尽管近期基于大语言模型的方法改进了查询重构，但仍缺乏对论文内容进行深度推理以验证实际相关性的机制。其次，在工作流程方面，现有工具是割裂的：研究人员通常需要使用不同的工具分别进行文献发现（搜索引擎）、组织（如Zotero、Mendeley等参考文献管理器）和追踪（如arXiv或提醒服务）。各环节间的切换需要大量手动操作（如下载PDF、复制元数据、标记条目、检查更新），导致研究人员将大量时间耗费在信息管理而非实质性的科研工作上。

因此，本文要解决的核心问题是：如何构建一个端到端的智能学术代理系统，以克服现有语义搜索的局限性，并整合碎片化的工作流程，从而提升科研人员文献发现、组织与追踪的整体效率和智能化水平。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：学术搜索引擎、基于LLM的智能体系统，以及端到端自动化研究平台。

在**学术搜索引擎**方面，主流工具如Google Scholar和PubMed基于关键词匹配，但难以处理需要语义理解的复杂查询。后续改进如Semantic Scholar引入了基于引用的指标和推荐功能，Connected Papers提供了引文网络可视化，但它们都侧重于文献发现，缺乏对文献组织与管理的支持。

在**基于LLM的智能体**方面，近期研究如LitSearch和ResearchArena开始评估LLM在学术搜索中的潜力。PaSa等系统利用智能体调用搜索工具、解析论文并遍历引文网络来处理复杂查询，在召回率上超越了传统基线。然而，这些工作主要聚焦于检索阶段，并未解决检索后的文献组织与长期追踪需求。

在**端到端自动化研究平台**方面，一些系统如ChemCrow和Coscientist专注于自动化特定领域（如化学）的实验流程。更宏大的框架如AI Scientist和ResearchAgent试图覆盖从构思、实验到论文撰写的全过程，但其全自动设计限制了用户控制，且旨在替代而非辅助研究者。Agent Laboratory虽将工作流扩展到文献综述，但优先目标是生成新研究产出而非管理现有文献。

本文提出的WisPaper与上述工作的区别在于：它**整合了检索、组织与追踪三大模块**，形成了一个闭环的端到端智能体系统。它不仅通过WisModel进行深度语义验证以提升检索质量（区别于传统关键词搜索和PaSa等纯检索系统），还无缝衔接了文献库管理和AI推荐订阅，解决了工作流碎片化问题。与全自动研究平台不同，WisPaper定位于**辅助研究者**，支持跨学科文献管理，并强调用户控制下的长期学术跟踪。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为WisPaper的端到端智能体系统来解决学术文献发现、组织与追踪中的语义搜索局限和工作流碎片化问题。其核心方法是设计一个由三个紧密集成的模块构成的“知识循环”整体框架，使发现、组织与监控形成闭环，相互增强。

整体框架围绕“知识循环”展开，包含三个主要模块：**学者搜索**、**文献库**和**AI订阅源**。学者搜索模块提供快速搜索和深度搜索两种模式。深度搜索是其关键技术创新，它调用一个名为**WisModel**的智能体模型来处理复杂、意图驱动的查询。WisModel采用两阶段结构化推理流程：第一阶段是**意图分解**，将用户查询扩展为多个搜索查询并构建一个可验证的检查清单；第二阶段是**证据支持的验证**，对检索到的候选论文，WisModel生成结构化报告，将检查清单中的每个条目与论文中的具体证据（如标题、摘要）关联起来，并给出评估标签，最终根据检查清单的满足程度对结果进行排序。整个过程对用户透明且可编辑，允许协作式细化，有效缓解了检索幻觉问题。

WisModel本身的训练是另一大创新点。它通过**监督微调**初始化后，采用**分组相对策略优化**（GRPO）进行强化学习优化。为了确保验证的严谨性，论文设计了**多维成形奖励函数**，从格式一致性、忠实性（反幻觉）、逻辑蕴含和推理对齐四个维度进行精细奖励。此外，还采用了**动态课程优化**策略，在训练早期优先保证输出结构正确，后期再逐步加强对语义和逻辑推理的优化，从而稳定地训练出能执行严格学术验证的智能体。

文献库模块作为个人知识中枢，支持一键导入论文并自动提取元数据，通过用户显式（如文件夹分类）和隐式（如导入行为）信号构建动态的**用户兴趣画像**。AI订阅源模块则利用该画像进行双层过滤（源选择与个性化匹配），每日推荐少量高度相关的论文。这三个模块形成了一个增强循环：搜索发现的论文存入文献库以更新用户画像；更新后的画像使AI订阅源的推荐更精准；推荐又可能触发新的深度搜索，从而实现了从发现到长期追踪的无缝闭环工作流。

### Q4: 论文做了哪些实验？

论文进行了三项核心实验，以评估其深度搜索（Deep Search）能力。实验设置、数据集、对比方法和主要结果如下：

**1. 查询理解与标准生成实验**
*   **实验设置与数据集**：评估WisModel将用户复杂查询分解为可验证标准的能力。使用自建数据集，包含来自10个学科（如计算机科学、医学等）的2,777条真实中英文查询，每条查询由领域专家标注了优化的关键词组合和判定论文是否相关的具体标准。
*   **对比方法**：与多个先进大语言模型对比，包括GPT-5.1、GPT-4o、Qwen-Max、GLM-4-Flash、GLM-4.6和DeepSeek-V3.2-Exp。
*   **主要结果与指标**：WisModel在所有评估指标上均达到最优，其中**语义相似度为94.8%**，**ROUGE-L为67.7%**，**BLEU为39.8%**，相比第二名模型分别提升了4.8%、15.1%和18.3%。DeepSeek-V3.2-Exp作为开源模型表现突出（语义相似度90.2%）。

**2. 论文-标准匹配验证实验**
*   **实验设置与数据集**：评估WisModel根据给定标准准确判断论文相关性的能力。使用上述数据集中的5,879条人工标注标准，由专家将论文-标准对分类为“支持”、“部分支持”、“拒绝”和“信息不足”四类。
*   **对比方法**：与GPT-5.1、Claude-Sonnet-4.5、Qwen3-Max、DeepSeek-V3.2、Gemini3-Pro等模型对比。
*   **主要结果与指标**：WisModel展现出压倒性优势，**整体准确率达到93.70%**，显著优于次优模型（73.23%）。其在四个分类上的准确率分别为：信息不足90.64%、拒绝94.54%、部分支持91.82%、支持94.38%。基线模型普遍在“部分支持”这类模糊判断上表现薄弱。

**3. 端到端论文召回实验**
*   **实验设置与数据集**：在TaxoBench基准上评估完整Deep Search流程的检索效果。该基准包含8个计算机子领域的72篇高引综述，并标注了3,815篇核心论文作为真实答案。
*   **对比方法**：与先前在该基准“深度研究模式”下的最佳系统O3进行对比。
*   **主要结果与指标**：WisPaper的深度搜索流程实现了**22.26%的召回率**，超越了O3系统所保持的**20.92%** 的先前最优结果，证明了其基于结构化标准验证的检索有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的WisPaper系统在整合检索、验证、组织与追踪方面做出了有价值的探索，但其局限性和未来方向值得深入探讨。首先，系统验证模块WisModel的准确性虽高（93.70%），但其验证能力可能受限于训练数据的领域覆盖范围，对于高度专业或新兴交叉学科的复杂查询，其结构化推理和证据验证的可靠性仍需进一步测试。其次，系统在TaxoBench基准上的召回率（22.26%）虽有提升但绝对值仍较低，表明其在处理多样化和长尾学术需求时，语义理解和检索完整性存在局限。

未来研究可从以下几方面展开：一是增强系统的跨领域和跨语言适应能力，通过引入更丰富的学术图谱和预训练知识，提升对复杂研究问题的深层语义匹配。二是探索个性化与协同过滤的结合，当前用户画像主要基于个人库，未来可引入群体智慧，通过匿名化协作数据发现潜在相关文献。三是实现动态工作流的灵活定制，允许研究人员根据不同研究阶段（如开题、实验、写作）配置不同的搜索与推荐策略。最后，可考虑集成生成式AI功能，如自动生成文献综述或研究缺口分析，使系统从“搜索-管理”工具演进为“主动研究伙伴”。

### Q6: 总结一下论文的主要内容

论文提出了WisPaper，一个端到端的学术智能体系统，旨在解决现有学术搜索中的语义局限和工作流碎片化两大核心挑战。系统通过三个紧密集成的模块构建了一个“知识闭环”：1) **学者搜索**模块提供快速关键词检索和深度搜索，其中智能体模型WisModel能将复杂的自然语言查询分解为可验证的结构化标准，并通过严格的原文引用验证来确保检索结果的实际相关性，有效缓解幻觉问题；2) **文献库**模块支持一键无缝保存和管理已发现的论文，并逐步构建用户画像；3) **AI订阅**模块基于用户画像持续推荐相关新文献，从而引导后续的探索行为。主要贡献在于首次将搜索、组织与追踪整合为一个自我优化的闭环系统，并开发了通过强化学习训练的WisModel进行结构化推理验证。实验表明，WisPaper在TaxoBench基准上实现了22.26%的召回率，优于基线，且WisModel的验证准确率达到93.70%。该系统将文献消费从被动检索转变为主动、持续优化的知识管理流程，提升了研究效率。
