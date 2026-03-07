---
title: "HotelQuEST: Balancing Quality and Efficiency in Agentic Search"
authors:
  - "Guy Hadad"
  - "Shadi Iskander"
  - "Oren Kalinsky"
  - "Sofia Tolmach"
  - "Ran Levy"
date: "2026-02-27"
arxiv_id: "2602.23949"
arxiv_url: "https://arxiv.org/abs/2602.23949"
pdf_url: "https://arxiv.org/pdf/2602.23949v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "N/A"
  primary_benchmark: "HotelQuEST"
---

# HotelQuEST: Balancing Quality and Efficiency in Agentic Search

## 原始摘要

Agentic search has emerged as a promising paradigm for adaptive retrieval systems powered by large language models (LLMs). However, existing benchmarks primarily focus on quality, overlooking efficiency factors that are critical for real-world deployment. Moreover, real-world user queries often contain underspecified preferences, a challenge that remains largely underexplored in current agentic search evaluation. As a result, many agentic search systems remain impractical despite their impressive performance. In this work, we introduce HotelQuEST, a benchmark comprising 214 hotel search queries that range from simple factual requests to complex queries, enabling evaluation across the full spectrum of query difficulty. We further address the challenge of evaluating underspecified user preferences by collecting clarifications that make annotators' implicit preferences explicit for evaluation. We find that LLM-based agents achieve higher accuracy than traditional retrievers, but at substantially higher costs due to redundant tool calls and suboptimal routing that fails to match query complexity to model capability. Our analysis exposes inefficiencies in current agentic search systems and demonstrates substantial potential for cost-aware optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前智能体搜索（agentic search）系统在评估和实际部署中面临的核心矛盾：即现有研究过于关注答案质量，而忽视了效率因素和用户查询中普遍存在的偏好不明确问题，导致许多性能优异的系统在实际应用中缺乏可行性。

研究背景在于，大语言模型（LLM）催生了能够自主使用工具、进行复杂任务的新一代智能体，其中智能体搜索是一个关键应用。这类系统需要处理从简单事实查询到复杂多步推理的各类搜索任务。然而，现有的智能体搜索基准测试主要聚焦于最终答案的准确性。

现有方法的不足主要体现在两个方面：首先，它们忽略了决定系统能否实际部署的关键效率维度，如延迟和计算成本；其次，现实中的用户查询常常包含模糊、未明确说明的偏好（例如“适合带狗的酒店”），这对基于标准相关性概念的评估构成了挑战，而现有研究对此探索不足。这使得难以判断智能体是否合理使用了资源，或是否为有限的收益进行了过度计算。

因此，本文要解决的核心问题是：如何建立一个更全面的评估框架，以同时衡量智能体搜索系统的**质量**（相关性和事实性）与**效率**（成本和延迟），并专门应对**用户偏好不明确**这一现实挑战。为此，论文引入了HotelQuEST基准测试，包含从简单到复杂的酒店搜索查询，并通过收集“澄清说明”来显式化标注者的隐含偏好以供评估。论文通过实证分析揭示了当前基于LLM的智能体存在成本效益低下的问题，如冗余的工具调用和未能根据查询复杂度匹配模型能力，从而为设计更具成本效益的智能体指明了方向。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：代理基准、代理搜索基准以及效率与质量权衡的研究。

在**代理基准**方面，相关工作旨在评估代理在包含搜索在内的多样化任务中的综合能力。例如，Mind2Web、WebShop、BrowseComp、TheAgentCompany、GAIA和GAIA2等基准覆盖了通用、电商和企业领域，它们通常评估准确性（A）和事实性（F），但普遍忽略了效率（E）指标。

在**代理搜索基准**方面，近期研究专注于深度研究、事实查找和广泛搜索等具体搜索任务。例如，InfoDeepSeek、DeepResearch Bench、LiveDRBench和WideSearch等基准虽然关注搜索质量，但同样缺乏对效率的系统性评估，也未涉及对用户隐含意图（即未明确指定的查询）的处理。

关于**效率与质量权衡**的研究，已有工作探索了LLM中的“快思考”与“慢思考”模式（如思维链），以及用于自适应模式选择的混合框架。然而，现有基准并非专门为代理搜索设计，未能系统评估其在效率与质量之间的平衡能力。

本文提出的HotelQuEST与上述工作的主要区别在于：1）它是首个在代理搜索领域**联合评估质量（准确性、事实性）与效率**的基准；2）它专门设计了包含从简单到复杂全谱系难度的酒店搜索查询，并创新性地通过收集“澄清”信息来解决**未明确指定用户偏好**这一现实挑战，从而填补了现有研究的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为HotelQuEST的综合性基准测试，并设计一套严谨的实验分析框架，来系统性地解决现有智能体搜索系统在质量与效率之间失衡、以及难以评估用户隐含偏好（underspecified preferences）的问题。

**核心方法与架构设计**：
论文的核心方法是建立一个包含214个酒店搜索查询的基准数据集，这些查询覆盖了从简单事实查询到复杂多约束请求的完整难度谱系。为了解决用户查询中普遍存在的偏好不明确问题，论文在数据构建中引入了一个关键创新环节：在生成每个查询后，要求标注者额外提供一份“澄清说明”（Clarification），以显式化其隐含的假设和意图。这份澄清说明作为评估时的“黄金标准”，仅提供给评估者（LLM-as-a-judge），用于准确判断系统输出是否符合用户的真实意图。

**主要模块与实验框架**：
1.  **基准数据集构建**：采用三阶段协议。阶段一生成反映真实旅行场景的自然语言查询。阶段二为每个查询生成澄清说明，捕获用户隐含意图。阶段三由标注者根据解决查询的预估时间（5分钟、5-15分钟、>15分钟）将查询复杂度分为简单、中等、复杂三级。
2.  **查询解构分析**：将每个查询分解为多个限定符（qualifiers），并标注其类型（显式/隐式/否定）和内容（如位置、人群、描述）。这允许进行细粒度分析，研究查询特征如何影响不同系统架构的质量和效率。
3.  **多层次系统评估**：实验评估了涵盖质量-效率谱系的一系列基线系统：
    *   **纯检索模型**：包括BM25和不同规模的稠密检索模型（22M和300M参数），在两个数据源（酒店描述、用户评论）上分别测试。
    *   **检索+LLM重排序器**：在稠密检索（300M）的基础上，增加一个LLM重排序器（600M或4B参数）对检索结果进行精排。
    *   **LLM智能体**：基于LangGraph框架构建迭代式智能体（使用Claude和Qwen3-32B模型）。其工作流程包括规划（选择数据源并生成搜索查询）、检索、过滤和更新记忆，循环进行直至找到足够数量的酒店或达到迭代上限。
    *   **Oracle模型**：引入两种理论上限模型作为参照。“预算Oracle”在固定成本约束（如1、2、4美元）下最大化准确率；“质量Oracle”为每个查询选择能达到最高准确率的最便宜模型。

**关键技术点与创新**：
1.  **引入“澄清说明”作为评估基础**：这是解决隐含偏好评估挑战的关键创新。它确保了评估信号基于搜索者自身的真实意图，而非评估者的主观猜测，从而实现了更可靠、一致的质量评估。
2.  **系统性效率-质量权衡分析**：论文不仅评估准确率，还综合衡量了成本（API费用）、处理令牌数、中位数（P50）和尾部（P90）延迟等多个效率指标。通过将不同复杂度的系统置于同一框架下对比，清晰揭示了LLM智能体虽然能获得更高准确率，但其代价是成本（因冗余工具调用）和延迟（因次优的路由决策，未能使查询复杂度与模型能力匹配）的急剧上升。
3.  **通过Oracle模型量化优化潜力**：实验结果显示，预算Oracle仅用1-4美元的成本就能达到接近顶级智能体的质量（准确率4.23-4.55），而顶级智能体（如Claude 3.7 Sonnet）的成本高达96.03美元。这有力地证明了当前智能体搜索系统存在巨大的、可通过成本感知优化来提升的效率空间。图表分析进一步指出，超过一定阈值后，增加成本或延迟对质量提升的边际效益递减甚至归零，为优化指明了方向。

综上，论文通过构建一个包含真实用户隐含意图的、难度分布均衡的基准测试，并设计一个涵盖从轻量检索到复杂智能体的多层次评估体系，系统地诊断了当前智能体搜索系统的效率瓶颈，并通过与Oracle上限的对比，实证了进行成本感知优化的必要性和巨大潜力。

### Q4: 论文做了哪些实验？

论文在HotelQuEST基准上进行了全面的实验，以评估智能体搜索系统的质量与效率。实验设置包括：使用包含214个酒店搜索查询的HotelQuEST数据集，查询难度从简单事实性请求到复杂需求不等，并收集了澄清信息以评估对用户未明确偏好的处理能力。

对比方法分为两类：一是传统检索基线（如BM25、稠密检索器），二是基于大语言模型（LLM）的智能体系统（包括Claude 3 Haiku、Sonnet 3.7、Sonnet 4以及Qwen3-32B）。此外，论文还引入了两种具有完美前瞻性的Oracle基线（预算Oracle和质量Oracle）来建立路由效率的理论上限。

主要结果与关键指标如下：
1.  **质量与效率差距**：LLM智能体（如Sonnet 3.7）实现了最高准确率，但成本显著更高（例如，比检索模型高出多个数量级）。传统检索方法成本近乎为零、延迟低，但准确率有限。
2.  **Oracle分析揭示优化空间**：预算Oracle在给定全局预算下选择模型以最大化总准确率，结果显示在约2美元预算处出现收益拐点。质量Oracle为每个查询选择能达到最高准确率的最便宜模型。关键发现是：仅少数复杂查询需要最强大的模型，质量Oracle能以低于最佳智能体的成本实现更优性能；预算Oracle在1美元预算下能达到高于所有智能体的准确率，同时成本比Sonnet 3.7低96倍，比Qwen3-32B低4倍。这表明当前系统存在巨大的成本优化空间。
3.  **智能体行为低效**：轨迹分析发现，智能体经常在获取足够证据后仍进行冗余的工具调用，导致过度探索，增加成本和延迟却未提升准确率。限制Sonnet 3.7的工具调用次数实验表明，过度调用会导致成本与延迟增加，而中位延迟保持稳定，准确率无相应增益。
4.  **查询属性影响**：查询复杂性显著影响检索模型的准确率，但对智能体模型影响较小。查询长度影响检索模型和较小智能体（如Qwen3-32B）。Qwen3-32B还对限定词数量以及否定、主观性等语言属性敏感。在应对不同复杂度查询时，多数智能体（如Qwen3-32B、Sonnet 4）会随复杂度提升增加计算投入（成本、延迟、令牌使用量），但额外努力仅部分抵消复杂查询上的准确率下降；而Sonnet 3.7在查询最难时反而投入更少，表现出停止行为失准。

### Q5: 有什么可以进一步探索的点？

本文的局限性为未来研究提供了多个探索方向。首先，在评估框架上，论文指出由于查询设计完全开放，难以确定每个查询的绝对最优答案和质量上限。未来可探索更精细的评估理论，例如引入概率性质量边界或基于用户满意度的相对评估体系，以更可靠地衡量系统性能上限。其次，在系统效率方面，研究发现当前智能体存在冗余工具调用和查询-能力匹配不佳的问题，这指向了重要的优化空间。未来可设计更智能的路由机制，例如基于查询复杂度的实时分类器，动态分配简单查询给轻量级检索器、复杂查询给大语言模型，并在执行过程中引入预算感知的提前终止策略。此外，提示工程的敏感性也是一个开放挑战，未来可系统研究提示模板的鲁棒性优化或探索提示自动生成技术。最后，数据集规模有限，未来可通过半自动方法扩展高质量测试集，或研究在小样本设定下更具统计效力的评估指标。总体而言，在追求质量的同时，将效率（如延迟、成本）作为核心优化目标并设计协同评估框架，是推动智能体搜索走向实用的关键。

### Q6: 总结一下论文的主要内容

该论文提出了HotelQuEST基准，旨在评估智能搜索代理在平衡查询质量与系统效率方面的表现。核心问题是现有评估体系过度关注检索质量，而忽视了实际部署中至关重要的效率因素（如延迟、成本），且对用户查询中普遍存在的偏好不明确问题缺乏有效评估方法。

论文方法包括构建一个包含214个从简单到复杂酒店搜索查询的数据集，并通过收集“澄清说明”将标注者的隐式偏好显式化，以更可靠地评估对模糊意图的理解。实验对比了传统检索模型与基于大语言模型（LLM）的智能代理。

主要结论发现，基于LLM的代理虽能达到更高准确性，但因其冗余的工具调用和未能根据查询复杂度合理分配模型能力（即路由不佳），导致成本显著增高。研究揭示了当前智能搜索系统在效率上的严重缺陷，并强调了未来需研究能协同优化响应质量与计算经济成本的策略。
