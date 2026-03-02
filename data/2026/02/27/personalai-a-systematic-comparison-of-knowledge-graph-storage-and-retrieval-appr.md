---
title: "PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents"
authors:
  - "Mikhail Menschikov"
  - "Dmitry Evseev"
  - "Victoria Dochkina"
  - "Ruslan Kostoev"
  - "Ilia Perepechkin"
  - "Petr Anokhin"
  - "Nikita Semenov"
  - "Evgeny Burnaev"
date: "2025-06-20"
arxiv_id: "2506.17001"
arxiv_url: "https://arxiv.org/abs/2506.17001"
pdf_url: "https://arxiv.org/pdf/2506.17001v5"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agent 架构"
  - "记忆机制"
  - "知识图谱"
  - "检索增强生成"
  - "个性化"
  - "长期交互"
  - "外部记忆"
  - "推理"
relevance_score: 9.0
---

# PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents

## 原始摘要

Personalizing language models that effectively incorporating user interaction history remains a central challenge in development of adaptive AI systems. While large language models (LLMs), combined with Retrieval-Augmented Generation (RAG), have improved factual accuracy, they often lack structured memory and fail to scale in complex, long-term interactions. To address this, we propose a flexible external memory framework based on knowledge graph, which construct and update memory model automatically by LLM itself. Building upon the AriGraph architecture, we introduce a novel hybrid graph design that supports both standard edges and two types of hyper-edges, enabling rich and dynamic semantic and temporal representations. Our framework also supports diverse retrieval mechanisms, including A*, water-circle traversal, beam search and hybrid methods, making it adaptable to different datasets and LLM capacities. We evaluate our system on three benchmarks: TriviaQA, HotpotQA, DiaASQ and demonstrate that different memory and retrieval configurations yield optimal performance depending on the task. Additionally, we extend the DiaASQ benchmark with temporal annotations and internally contradictory statements, showing that our system remains robust and effective in managing temporal dependencies and context-aware reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个性化大语言模型（LLM）智能体在长期交互中如何有效编码、存储和检索用户历史信息这一核心挑战。研究背景是，尽管结合了检索增强生成（RAG）的LLM提升了事实准确性，但在开发能够适应用户的个性化AI系统时，现有方法存在明显不足。传统RAG方法主要依赖对原始文本块的密集向量相似性检索，其记忆本质上是非结构化的，缺乏对存储记忆间语义关系的有效支持，并且在复杂、长期的交互场景中难以扩展，导致智能体在支持高效推理和响应生成方面存在局限。

因此，本文要解决的核心问题是：如何为个性化LLM智能体构建一个灵活、结构化且可扩展的外部记忆框架，以克服现有RAG方法在表示和利用语义关系、时间依赖关系以及进行复杂推理方面的缺陷。具体而言，论文提出了一个基于知识图谱的灵活外部记忆框架，该框架允许LLM自身自动构建和更新记忆模型。它支持多种记忆格式（如节点、知识三元组、论点陈述、情景痕迹），并将其动态组织成知识图谱，从而实现对语义和时间关系更具控制力和可解释性的表示与访问。同时，框架提供了一个可插拔的检索接口，支持多种图遍历机制（如A*搜索、水循环遍历、束搜索等），以适应不同任务需求和模型能力。通过在不同基准测试上的评估，论文展示了该框架在管理时间依赖性和上下文感知推理方面的有效性与鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：知识增强问答与检索、基于知识图的记忆框架，以及个性化智能体。

在知识增强问答与检索方面，早期研究利用维基百科等大规模知识源，结合文档检索与文本理解。传统稀疏检索方法（如TF-IDF、BM25）后来被基于稠密表示的检索方法超越，后者在数据充足时表现更佳。近期，检索增强生成（RAG）模型通过结合参数化与非参数化记忆，提升了知识密集型任务性能。无监督稠密检索模型（如ART）进一步实现了先进性能，且无需标注数据。

在基于知识图的记忆与推理方面，GraphReader等框架利用结构化推理增强知识提取与长上下文推理。MemWalker、RAPTOR和ReadAgent专注于处理长文本，通过高效遍历或构建记忆片段来整合信息。KGP（Knowledge Graph Prompting）则通过构建知识图来提升多文档问答中的上下文推理能力。

在个性化智能体方面，AriGraph提出了整合情景记忆与长期规划的知识图框架，HippoRAG则利用个性化算法构建语义图以提升问答性能。这些工作为个性化交互奠定了基础。

本文工作与上述研究紧密相关，但存在区别。本文在AriGraph架构基础上，提出了一种新颖的混合图设计（支持标准边和两类超边），以支持更丰富、动态的语义与时间表征。同时，本文框架支持多样化的检索机制（如A*、水循环遍历、束搜索及混合方法），使其能适应不同数据集和LLM能力，并在包含时间标注和内部矛盾语句的扩展基准上验证了系统的鲁棒性。因此，本文是对现有知识图个性化框架在记忆结构灵活性与检索机制多样性方面的系统化推进与实证比较。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于知识图谱的灵活外部记忆框架来解决个性化LLM智能体在长期复杂交互中缺乏结构化记忆和可扩展性的问题。其核心方法是利用LLM自身自动从非结构化文本中构建和更新一个混合图结构的知识库作为外部记忆，并设计多样化的检索机制来高效提取相关信息以生成答案。

整体框架包含两个主要管道：记忆构建管道（Memorize pipeline）和问答管道（QA pipeline）。记忆构建管道负责从文本中自动提取信息并构建记忆图。问答管道则负责处理用户问题，从记忆图中检索相关信息并生成答案。

记忆图采用了一种新颖的混合图设计，包含语义记忆和情景记忆。语义记忆由对象顶点（$V_o$，代表原子概念）、对象边（$E_o$，代表概念间的直接关系）、论点顶点（$V_t$，代表完整的原子思想）和论点边（$E_t$，一种连接一组对象顶点的超边）构成。情景记忆则由情景顶点（$V_e$，对应原始文本片段，也作为超边）和情景边（$E_e$，连接所有从同一文本中提取的语义顶点）构成。这种设计同时支持标准边和两种超边（论点边和情景边），能够丰富、动态地表示语义和时序关系。

关键技术包括：1）基于LLM的自动记忆构建与更新：LLM被提示从文本中提取三元组和论点，并解析输出以结构化存储；当检测到新旧信息冲突时，通过匹配顶点、广度优先搜索（BFS）关联边，并提示LLM更新知识。2）模块化的问答管道：包含实体提取器、实体-顶点匹配器、记忆图三元组检索器、三元组过滤器和条件答案生成器。首先提取问题中的关键实体并匹配到图中的顶点，然后以此为基础启动图遍历算法检索候选三元组，接着通过向量嵌入计算语义相似度进行过滤，最后LLM基于过滤后的三元组生成答案。3）多样化的图检索算法：设计了A*算法（使用不同的启发式函数寻找最短路径）、WaterCircles算法（基于BFS，关注从不同起点出发路径的交集）、BeamSearch算法（受束搜索启发，构建多条语义相关路径）以及混合算法（整合前述方法）。这些算法通过可配置参数在检索的“完整性”和“相关性”之间进行动态权衡，以适应不同任务和数据特性。

创新点主要体现在：提出了一个支持标准边和超边的混合图记忆模型，实现了对语义和情景信息的统一结构化表示；实现了完全由LLM驱动的记忆自动构建与更新机制；设计并系统比较了多种可配置的图遍历检索算法，增强了系统在不同场景下的适应性和鲁棒性。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行了系统实验：DiaASQ（扩展了时间标注和内部矛盾陈述）、HotpotQA和TriviaQA，分别用于评估个性化对话、多跳推理和事实性知识检索能力。实验构建了基于知识图的外部记忆框架，并比较了多种图遍历检索算法（A*、WaterCircles、BeamSearch及其混合策略）在不同图遍历限制（禁止遍历事件、论点或对象节点）下的性能。对比方法包括传统的检索增强生成（RAG）和图检索增强生成（GraphRAG）基线。评估使用了多种规模的LLM（如Qwen2.5 7B、DeepSeek R1 7B、Llama3.1 8B、GPT4o-mini、DeepSeek V3），并以LLM-as-a-Judge评分作为主要质量指标。

关键结果显示：在DiaASQ上，GPT4o-mini结合BeamSearch+WaterCircles且限制事件节点时取得最高分0.5；在HotpotQA上，同一配置在无限制时得分0.77；在TriviaQA上，DeepSeek V3使用BeamSearch+WaterCircles无限制时得分0.87。实验发现，对于7B/8B模型，限制论点节点遍历会显著降低性能（低质量配置中占比约74%），而高质量配置多限制事件或对象节点（分别占44%和34%）；对于更大模型（14B+），高质量配置则倾向于限制论点节点（占73%）。在检索算法稳定性方面，BeamSearch对参数设置敏感，性能波动可达24%，而BeamSearch+WaterCircles在大型模型上表现更稳健。此外，"NoAnswer"机制的分析显示，不同模型的最佳算法与限制组合能最小化无效回答（如7B模型在A*+WaterCircles限制论点时仅25%）。效率上，WaterCircles因无需向量检索最快（平均0.3分钟/问题），BeamSearch最慢（平均6.59分钟）。实验还指出使用Qdrant向量数据库可比Milvus提升6倍速度。

### Q5: 有什么可以进一步探索的点？

本文提出的基于知识图谱的个性化记忆框架虽具创新性，但仍存在若干局限和可拓展方向。首先，系统在动态更新和长期记忆维护方面效率有待提升，当前图遍历算法可能成为性能瓶颈，尤其是在处理大规模、高频率的用户交互时。其次，记忆的表示和检索机制仍较为依赖预设的图结构和检索策略，对于复杂、隐含的用户偏好捕捉能力有限。

未来研究可从以下方向深入：一是优化时序动态性，如引入更细粒度的“记忆时间”参数与衰减机制，使系统能更好地权衡近期互动与长期偏好；二是提升检索效率与可扩展性，结合近似最近邻搜索、图神经网络索引等技术，降低查询延迟；三是增强记忆的抽象与推理能力，探索如何利用LLM对知识图谱进行高阶语义压缩与逻辑推理，以支持更复杂的个性化决策。此外，可考虑引入多模态用户数据（如行为序列、社交关系）来丰富记忆表征，并在更开放的真实场景中验证系统的鲁棒性与泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对个性化LLM智能体在长期交互中缺乏结构化记忆、难以有效利用用户历史信息的问题，提出了一种基于知识图谱的灵活外部记忆框架。核心贡献在于扩展了AriGraph架构，引入了一种新颖的混合图设计，支持标准边和两种超边，以构建丰富的动态语义与时间表征。方法上，系统利用LLM自动构建和更新记忆图谱，并支持多种检索机制（如A*、水循环遍历、束搜索及混合方法），可根据任务和模型规模动态适配。通过在TriviaQA、HotpotQA和DiaASQ等基准测试上的评估，论文表明不同记忆与检索配置的性能随任务而异：较小模型（7B-8B）限制某些顶点类型并使用束搜索效果最佳，而较大模型则受益于混合检索策略。结论指出，该框架在管理时间依赖和上下文感知推理方面表现稳健，相比现有RAG与GraphRAG方法具有竞争力或更优性能，尤其擅长处理时序复杂和矛盾信息，为构建支持个性化、可扩展推理的LLM智能体奠定了结构化记忆的基础。
