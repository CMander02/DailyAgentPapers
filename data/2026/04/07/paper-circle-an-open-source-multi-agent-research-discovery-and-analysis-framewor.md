---
title: "Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework"
authors:
  - "Komal Kumar"
  - "Aman Chadha"
  - "Salman Khan"
  - "Fahad Shahbaz Khan"
  - "Hisham Cholakkal"
date: "2026-04-07"
arxiv_id: "2604.06170"
arxiv_url: "https://arxiv.org/abs/2604.06170"
pdf_url: "https://arxiv.org/pdf/2604.06170v1"
github_url: "https://github.com/MAXNORM8650/papercircle"
categories:
  - "cs.CL"
tags:
  - "Multi-agent System"
  - "Research Agent"
  - "Tool Use"
  - "Knowledge Graph"
  - "Retrieval"
  - "System Design"
  - "Open Source"
relevance_score: 7.5
---

# Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework

## 原始摘要

The rapid growth of scientific literature has made it increasingly difficult for researchers to efficiently discover, evaluate, and synthesize relevant work. Recent advances in multi-agent large language models (LLMs) have demonstrated strong potential for understanding user intent and are being trained to utilize various tools. In this paper, we introduce Paper Circle, a multi-agent research discovery and analysis system designed to reduce the effort required to find, assess, organize, and understand academic literature. The system comprises two complementary pipelines: (1) a Discovery Pipeline that integrates offline and online retrieval from multiple sources, multi-criteria scoring, diversity-aware ranking, and structured outputs; and (2) an Analysis Pipeline that transforms individual papers into structured knowledge graphs with typed nodes such as concepts, methods, experiments, and figures, enabling graph-aware question answering and coverage verification. Both pipelines are implemented within a coder LLM-based multi-agent orchestration framework and produce fully reproducible, synchronized outputs including JSON, CSV, BibTeX, Markdown, and HTML at each agent step. This paper describes the system architecture, agent roles, retrieval and scoring methods, knowledge graph schema, and evaluation interfaces that together form the Paper Circle research workflow. We benchmark Paper Circle on both paper retrieval and paper review generation, reporting hit rate, MRR, and Recall at K. Results show consistent improvements with stronger agent models. We have publicly released the website at https://papercircle.vercel.app/ and the code at https://github.com/MAXNORM8650/papercircle.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科研人员在面对海量、快速增长的学术文献时，难以高效地进行文献发现、评估、组织和理解的难题。研究背景是科学出版物数量呈指数级增长，而传统的搜索引擎和推荐系统往往无法提供文献综述所需的深度和上下文，导致发现流程碎片化。尽管近期基于大语言模型的多智能体系统展现了成为“AI科学家”的潜力，但现有方法（如PaperQA、STORM、Connected Papers等）存在明显不足：它们要么缺乏真正的多智能体协同编排，要么不支持多源发现，要么无法构建带类型的论文知识图谱，或者不具备确定性的可复现流程和丰富的结构化输出，难以全面支撑从发现到分析、批判与合成的完整文献研读生命周期。

因此，本文要解决的核心问题是：如何构建一个开放源码的多智能体研究平台，以弥合完全自主的AI系统与人类研究者实际协作需求之间的鸿沟。具体而言，Paper Circle致力于通过一个集成的、可协作的工作台来增强人类智能，其核心是设计并实现两个互补的流水线——**发现流水线**（整合多源检索、多标准评分、多样性感知排序和结构化输出）和**分析流水线**（将单篇论文转化为包含概念、方法、实验等类型化节点的知识图谱，支持基于图的问答和覆盖验证）。该系统旨在将文献调研从一项孤立的劳动，转变为社区驱动的、AI增强的协同操作，并提供完全可复现、同步的结构化成果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：自动化研究生命周期系统、垂直领域科学多智能体系统，以及模拟科学协作的框架。

在**自动化研究生命周期系统**方面，相关工作如 DORA AI agent、EvoResearch、O-Researcher、MARS 和 AlphaResearch 等，旨在实现从假设生成到报告撰写的端到端自动化，常将研究视为多步优化问题。本文的 Paper Circle 与这些工作的核心区别在于其设计理念：它不追求完全自动化以取代研究者，而是优先考虑**文献的筛选管理和过程的可复现性**，旨在作为人类研究团队的“力量倍增器”，确保发现过程透明且可验证。

在**垂直领域科学多智能体系统**方面，已有许多成功应用于特定学科（如化学、生物、医疗、金融）的框架，例如 ChemThinker、CellAgent、ASTRAFIN 等。这些系统利用大语言模型进行分子发现、细胞分析或市场预测等任务。Paper Circle 与这些工作的关系是**互补**。它提供了一个**通用**的文献发现与分析管道，可作为跨学科文献综述和知识管理的基础层，而非针对某一特定领域。

在**模拟科学协作的框架**方面，相关研究如 ResearchTown 通过智能体模拟研究社区中思想的传播，而 PiFlow、REDEREF 等则探索智能体在信息发现中的协作机制。Paper Circle 的显著区别在于它超越了模拟，构建了一个**真实的人机协作平台**。它不仅模拟研究者如何互动，更通过共享阅读列表、讨论线程和协同排名等功能，主动促进这些互动。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Paper Circle的多智能体系统来解决科研文献发现与分析难题。该系统采用双管道架构：**发现管道**负责高效检索与筛选文献，**分析管道**则对单篇论文进行深度结构化理解与知识抽取。

**整体框架与核心模块**：系统基于smolagents库构建，以CodeAgent作为中央协调器，管理多个具备特定工具的ToolCallingAgent。发现管道包含多个协同工作的智能体：**意图分类智能体**解析用户查询，确定搜索模式与偏好；**论文搜索智能体**执行离线（如本地库）与在线（如arXiv）检索并去重；**排序智能体**依据新颖性、引用量、相似度等多标准进行重排序；**分析智能体**计算统计洞察；**导出智能体**生成同步的结构化输出。分析管道则是一个四阶段流程：**摄取层**使用PyMuPDF解析PDF，提取元数据、章节、图表等，并通过语义分块生成结构感知的文本单元；**图构建器**协调四个专用提取器（概念、方法、实验、视觉关联），将论文转化为类型化的知识图谱，节点包括概念、方法、实验等，边表示其语义与结构关系，所有元素均带有可追溯原文的元数据；**问答系统**结合向量检索与图遍历，实现基于图谱的精准问答；**验证层**通过覆盖率检查确保分析完整性。

**关键技术**：1. **多智能体协同与状态迭代**：发现管道采用类似“噪声-去噪”的迭代机制，维护一个显式演化的发现状态（论文、链接、统计等），通过智能体步骤逐步精炼。2. **结构化知识图谱构建**：定义了丰富的图谱模式，并采用分阶段增量构建策略，确保信息的结构化与可追溯性。3. **图感知的检索与问答**：问答模块融合了基于嵌入的检索和图邻居扩展，使回答能基于文本证据和图关系。4. **可复现的输出同步**：每个智能体步骤均生成完全同步、可复现的多种格式输出（JSON、CSV、BibTeX等）。

**创新点**：一是将文献发现与深度分析任务解耦为互补且集成的双管道，覆盖从宏观检索到微观理解的完整工作流；二是通过多智能体分工与对话，模拟了研究者的不同角色（如质疑者、分析者），提升了推理深度并减少了幻觉；三是构建了具备完整溯源能力的论文知识图谱，为后续的查询、验证与合成提供了结构化基础。

### Q4: 论文做了哪些实验？

论文进行了多组实验，主要围绕系统在文献检索和论文分析两大核心功能上的性能评估。

**实验设置与数据集**：实验在配备4×40GB Nvidia GPU的硬件上，使用Ollama平台和fastllm库进行。构建了一个包含21,115篇论文的多样化语料库，主要来自OpenReview等平台，覆盖ICLR、NeurIPS、ICML、CVPR等主要CS/ML会议。

**对比方法与评估指标**：在**文献检索**方面，评估了多种检索基线方法（BM25、语义检索、混合检索等）以及不同智能体组成的管道结构（如完整管道、最小管道等）。使用了两个查询基准：SemanticBench（基于论文标题/摘要生成的50个自然语言查询）和RAbench（由GPT-OSS-20B生成的500个研究助理式查询）。关键评估指标包括命中率（Hit Rate）、平均倒数排名（MRR）、召回率@K（R@K）和成功率。

**主要结果**：
1.  **模型比较**：在SemanticBench上，表现最佳的智能体模型是Qwen3C-30B-Inst-Q3_K_M，其命中率达80%，MRR为0.627，R@1为0.58，每查询耗时约22.2秒。BM25基线表现极具竞争力，命中率为78%，MRR为0.541。在更大的RAbench上，Qwen3C-30B-Inst-Q3_K_M性能进一步提升，命中率达98%，MRR为0.882。
2.  **消融研究**：实验表明，结合过滤器和离线检索的配置（命中率96%）性能优异，而缺少具体提及或混合在线/离线检索的配置性能显著下降（命中率62-64%）。在检索基线中，BM25方法在精确匹配（R@1达0.80）上持续优于纯语义检索（R@1为0.62）。
3.  **论文分析与综述生成**：论文展示了系统生成的交互式概念图、概念解释、问答界面等可视化分析输出。在论文综述生成任务中，实验发现聊天风格的大模型（如gpt-oss）比纯代码导向的智能体（如qwen3-coder-30B）能生成更连贯、质量更高的综述，且综述质量随模型规模增大而提升。
4.  **定性评估与用户研究**：通过对81次真实用户会话的分析，PaperCircle平均每次查询8.7个源，其论文覆盖范围远超单源检索（如arXiv遗漏70.9%）。用户反馈显示系统认知负荷低（NASA-TLX工作量评分1.2/7），易用性高（正面项平均7.6/10）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于其评审代理与人类判断的弱对齐性，相关性系数低且可能出现负相关，导致系统无法可靠地区分论文质量，因此尚不能作为可信的排名工具。这反映出当前基于大语言模型的代理在深层语义理解和价值判断上仍有不足。

未来研究方向可从以下几方面深入：首先，提升代理的评审能力，通过引入更精细的指令微调、人类反馈强化学习（RLHF）或领域特定的评估准则，以增强其与专家判断的一致性。其次，系统可扩展为动态学习框架，利用用户交互数据持续优化检索和评分策略，实现个性化推荐。此外，探索多模态分析，将图表、实验数据等非文本信息更深度地整合到知识图谱中，以提供更全面的论文洞察。最后，增强系统的可解释性，让代理的决策过程更透明，帮助研究者理解推荐依据，从而建立信任并促进学术协作。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为Paper Circle的开源多智能体研究文献发现与分析框架，旨在解决科学文献快速增长导致的研究者难以高效发现、评估和整合相关工作的难题。其核心贡献在于设计并实现了一个基于大语言模型的多智能体系统，通过两个互补的流水线来系统化地辅助文献调研：一是**发现流水线**，它整合了多来源的离线与在线检索、多标准评分、考虑多样性的排序以及结构化输出，以高效发现相关论文；二是**分析流水线**，它将单篇论文转化为结构化的知识图谱，包含概念、方法、实验、图表等类型化节点，支持基于图谱的问答和覆盖度验证。系统基于编码器LLM的多智能体编排框架构建，每一步智能体操作都产生完全可复现、同步的多种格式输出。实验在论文检索和综述生成任务上进行了基准测试，结果显示使用更强的智能体模型能带来性能的持续提升。该工作的意义在于为学术研究提供了一个自动化、结构化、可复现的文献处理新范式，其代码和网站均已开源，有助于推动AI辅助科研工具的发展。
