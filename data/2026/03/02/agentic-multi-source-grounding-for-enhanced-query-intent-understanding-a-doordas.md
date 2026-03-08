---
title: "Agentic Multi-Source Grounding for Enhanced Query Intent Understanding: A DoorDash Case Study"
authors:
  - "Emmanuel Aboah Boateng"
  - "Kyle MacDonald"
  - "Akshad Viswanathan"
  - "Sudeep Das"
date: "2026-03-02"
arxiv_id: "2603.01486"
arxiv_url: "https://arxiv.org/abs/2603.01486"
pdf_url: "https://arxiv.org/pdf/2603.01486v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "Enterprise & Workflow"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Agentic Multi-Source Grounded system (staged catalog entity retrieval, agentic web-search tool, configurable disambiguation layer)"
  primary_benchmark: "N/A"
---

# Agentic Multi-Source Grounding for Enhanced Query Intent Understanding: A DoorDash Case Study

## 原始摘要

Accurately mapping user queries to business categories is a fundamental Information Retrieval challenge for multi-category marketplaces, where context-sparse queries such as "Wildflower" exhibit intent ambiguity, simultaneously denoting a restaurant chain, a retail product, and a floral item. Traditional classifiers force a winner-takes-all assignment, while general-purpose LLMs hallucinate unavailable inventory. We introduce an Agentic Multi-Source Grounded system that addresses both failure modes by grounding LLM inference in (i) a staged catalog entity retrieval pipeline and (ii) an agentic web-search tool invoked autonomously for cold-start queries. Rather than predicting a single label, the model emits an ordered multi-intent set, resolved by a configurable disambiguation layer that applies deterministic business policies and is designed for extensibility to personalization signals. This decoupled design generalizes across domains, allowing any marketplace to supply its own grounding sources and resolution rules without modifying the core architecture. Evaluated on DoorDash's multi-vertical search platform, the system achieves +10.9pp over the ungrounded LLM baseline and +4.6pp over the legacy production system. On long-tail queries, incremental ablations attribute +8.3pp to catalog grounding, +3.2pp to agentic web search grounding, and +1.5pp to dual intent disambiguation, yielding 90.7% accuracy (+13.0pp over baseline). The system is deployed in production, serving over 95% of daily search impressions, and establishes a generalizable paradigm for applications requiring foundation models grounded in proprietary context and real-time web knowledge to resolve ambiguous, context-sparse decision problems at scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多类别按需配送平台（如DoorDash）中，用户查询意图理解的核心难题。随着平台从单一类别（如仅外卖）扩展至涵盖餐饮、杂货、零售等多类别的生态系统，简短且上下文稀疏的查询（如“Wildflower”）经常表现出意图模糊性，可能同时指向餐厅连锁、零售产品或花卉商品。传统的解决方案存在两大不足：一是传统的监督式多分类器采用“赢家通吃”的单标签预测模式，在训练目标上迫使不同类别竞争概率质量，从而抑制了同时存在的合理备选意图；二是尽管通用大语言模型具备推理能力，能缓解长尾查询的数据稀疏问题，但其缺乏平台特定信息的“落地”，容易产生幻觉，错误假设平台实际不存在的库存或类别。

因此，本文要解决的核心问题是：如何设计一个系统，能够同时克服传统分类器在模糊查询上意图压制，以及通用大语言模型因缺乏具体上下文而幻觉频发这两个缺陷，从而实现更精准、可靠的查询意图理解。为此，论文提出了一个“基于代理的多源落地系统”，其核心创新在于结合了两方面：首先，通过一个分阶段的目录实体检索流程和代理式的网络搜索工具，将LLM的推理过程“落地”于平台专有目录和实时网络知识，确保预测基于实际证据；其次，系统不预测单一标签，而是输出一个有序的多意图集合，并通过一个可配置的消歧层（应用确定的业务规则）进行最终解析，这种解耦设计增强了系统的通用性和可扩展性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类上，相关工作主要包括：
1.  **传统监督分类器**：如基于BERT的模型，它们采用赢家通吃的单标签分类范式。本文指出，这种范式在处理意图模糊的查询时存在根本性缺陷，因为其训练目标会抑制同时合理的备选意图。
2.  **通用大语言模型**：利用LLM的推理能力处理长尾查询，但存在“幻觉”问题，即可能生成与平台实际库存无关的意图。本文的**Agentic Multi-Source Grounded系统**通过将LLM推理**锚定**于专有数据源，直接解决了此问题。
3.  **检索增强生成与工具增强LLM**：这些技术被独立研究用于为模型提供外部知识。本文的创新之处在于，首次将**智能体化的多源锚定**（结合目录检索与自主网络搜索）与**双意图预测及可配置消歧**相结合，专门用于解决生产环境中的查询意图理解问题。

在应用类上，相关工作涉及**聚合搜索与意图分类**文献，这些研究关注在多类别市场（如电商、外卖平台）中呈现多源结果所面临的挑战。本文的工作是这一领域的具体实践和深化，其提出的**解耦架构**（将预测与基于业务规则的消歧分离）旨在提供一个可推广的范式，使任何多类别市场都能通过接入自己的数据源和规则来适配该系统，而无需修改核心架构。

### Q3: 论文如何解决这个问题？

论文通过构建一个**基于多源信息接地的智能体系统**来解决用户查询意图模糊的问题，其核心方法是将大语言模型的推理过程与结构化业务知识及实时外部信息相结合，而非依赖单一分类或纯文本生成。

**整体框架**采用**检索增强分类**范式，将流程解耦为多源证据检索、双意图推理引擎和可配置的消歧层三个主要阶段。系统首先将查询映射为最多包含两个意图的有序集合，而非单一标签，以覆盖可能的歧义。

**主要模块与关键技术**包括：
1.  **两阶段目录实体检索管道**：第一阶段使用稠密检索模型将查询和业务实体映射到共享向量空间，通过近似最近邻搜索获取语义候选集，以处理词汇漂移。第二阶段采用加权模糊匹配对候选集进行重排和过滤，结合词集重叠度和部分匹配度，保留高精度实体作为内部证据源。
2.  **智能体驱动的外部搜索工具**：对于冷启动或长尾查询，系统自主调用外部网络搜索工具，获取实时世界知识作为补充证据源，使模型能动态获取新鲜上下文以区分内部知识库中未涵盖的歧义。
3.  **双意图推理引擎**：将查询、检索到的目录实体和外部信号共同构成提示词，输入大语言模型。模型输出一个有序的双意图元组，包含一个主要意图和一个可选的次要意图。
4.  **可插拔的消歧层**：当模型预测出双意图时，输出会路由至消歧层。论文实现了一个基于全局历史胜率的确定性覆盖函数，通过预设的冲突对白名单决定最终意图。该层设计为模块化，便于未来扩展个性化信号或替换为学习型排序器。

**创新点**在于：
- **问题重构**：将意图预测从单标签分类转化为集合覆盖问题，优化目标是找到包含用户真实意图的最小集合。
- **解耦与可扩展设计**：证据检索、推理与消歧分层解耦，允许任何市场平台接入自定义的接地源和解决规则，而无需修改核心架构，实现了良好的领域泛化能力。
- **混合接地策略**：同时利用内部结构化目录（保证精确性）和外部实时网络搜索（保证新鲜度），有效应对了传统分类器的“赢家通吃”局限和通用大模型的“幻觉”问题。

### Q4: 论文做了哪些实验？

论文在DoorDash的多垂类搜索平台上进行了全面的实验评估。实验设置方面，系统采用离线批处理和缓存架构部署，覆盖了95.9%的日常搜索流量。评估使用了四个代表性基准数据集，总计约30,000个查询：Branded*（7,809个品牌名查询）、Retail（7,988个一般非食品零售查询）、Tail (Synthetic)（2,335个稀有长尾查询）以及SOT（12,651个涵盖头部、中部和尾部流量的全局样本）。

对比方法包括四个基线：(1) Legacy：现有生产系统，一个BERT+LLM混合集成模型；(2) Gemini Base：使用标准单意图提示的Gemini-2.5-flash（未接地）；(3) GPT-4o和(4) GPT-4o-mini：代表更大和更小的通用未接地单意图模型。

主要结果显示，提出的系统（DI）在所有基准测试上均取得显著准确率提升。在全局SOT基准上，其准确率达到94.0%，分别超过Gemini基线10.9个百分点、GPT-4o 10.8个百分点、GPT-4o-mini 14.2个百分点。在长尾（Tail）查询上，系统准确率为90.7%，超过基线13.0个百分点。关键数据指标包括：在SOT基准上，系统对头部、中部和尾部查询的准确率分别为99.5%、94.7%和90.7%。通过增量消融实验量化了各组件贡献：目录接地（Catalog Grounding）带来+8.3pp提升，智能体网络搜索接地（Agentic Search）带来+3.2pp提升，双意图消歧（Dual-Intent Disambiguation）带来+1.5pp提升，累计提升达+13.0pp。

### Q5: 有什么可以进一步探索的点？

本文提出的系统虽已取得显著效果，但仍存在局限性和广阔的探索空间。主要局限性在于其离线批处理和缓存设计，导致系统只能覆盖已见过的查询，无法实时处理全新或突发的冷启动查询。未来工作可首先致力于实现系统的完全在线化与实时化，例如通过持续学习或流式处理机制，使模型能即时利用新出现的目录或网络信息进行动态接地。

其次，论文提及的“教师-学生”知识蒸馏方向值得深入。未来可探索更高效的蒸馏方法，不仅压缩模型规模以降低推理成本，还可尝试将多源接地的复杂推理过程（如调用搜索工具的决策逻辑）也迁移至轻量级模型中，以提升学生模型的自主性和准确性。

此外，系统的可扩展性与个性化是核心改进方向。当前的“可插拔消歧层”设计为融入更多信号奠定了基础。未来可探索如何动态整合实时用户画像（如实时位置、当前购物车内容）、会话上下文以及市场趋势等多维度信息，使意图解析从“可配置”走向“自适应”和“个性化”。例如，系统可学习根据用户的历史行为，自动调整对不同接地源（如目录 vs. 网络搜索）的置信度权重，实现更精准的个性化排序与消歧。

### Q6: 总结一下论文的主要内容

本文针对多类别市场平台中用户查询意图模糊的问题，提出了一种“代理式多源信息锚定”系统，以提升查询意图理解的准确性。核心问题是处理如“Wildflower”这类上下文稀疏的查询，其可能同时指向餐厅、零售产品或花卉等不同业务类别。传统分类器强制进行单一类别分配，而通用大语言模型则容易产生与现有库存不符的“幻觉”。

该方法的核心贡献在于设计了一个解耦的架构。系统首先通过一个分阶段的目录实体检索管道，将LLM的推理过程锚定在专有业务目录上；其次，对于冷启动查询，系统会自主调用一个代理式网络搜索工具来获取实时信息。模型输出的是一个有序的多意图集合，而非单一标签，随后由一个可配置的消歧层根据确定的业务策略进行最终解析，该设计也便于未来集成个性化信号。

主要结论显示，该系统在DoorDash的多垂直搜索平台上显著优于基线模型：相比未锚定的LLM基线准确率提升10.9个百分点，相比旧有生产系统提升4.6个百分点。在长尾查询上，目录锚定、代理式网络搜索锚定和双重意图消歧分别贡献了8.3、3.2和1.5个百分点的提升，最终准确率达到90.7%。该系统已部署于生产环境，处理超过95%的日搜索请求，为需要结合专有上下文与实时网络知识来解决大规模模糊决策问题的应用，提供了一个可推广的范式。
