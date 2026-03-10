---
title: "FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use"
authors:
  - "Jiaxuan Lu"
  - "Kong Wang"
  - "Yemin Wang"
  - "Qingmei Tang"
  - "Hongwei Zeng"
  - "Xiang Chen"
  - "Jiahao Pi"
  - "Shujian Deng"
  - "Lingzhi Chen"
  - "Yi Fu"
  - "Kehua Yang"
  - "Xiao Sun"
date: "2026-03-09"
arxiv_id: "2603.08262"
arxiv_url: "https://arxiv.org/abs/2603.08262"
pdf_url: "https://arxiv.org/pdf/2603.08262v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Financial Agent"
  - "Evaluation Framework"
  - "Domain-Specific Agent"
relevance_score: 8.5
---

# FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use

## 原始摘要

The integration of Large Language Models (LLMs) into the financial domain is driving a paradigm shift from passive information retrieval to dynamic, agentic interaction. While general-purpose tool learning has witnessed a surge in benchmarks, the financial sector, characterized by high stakes, strict compliance, and rapid data volatility, remains critically underserved. Existing financial evaluations predominantly focus on static textual analysis or document-based QA, ignoring the complex reality of tool execution. Conversely, general tool benchmarks lack the domain-specific rigor required for finance, often relying on toy environments or a negligible number of financial APIs. To bridge this gap, we introduce FinToolBench, the first real-world, runnable benchmark dedicated to evaluating financial tool learning agents. Unlike prior works limited to a handful of mock tools, FinToolBench establishes a realistic ecosystem coupling 760 executable financial tools with 295 rigorous, tool-required queries. We propose a novel evaluation framework that goes beyond binary execution success, assessing agents on finance-critical dimensions: timeliness, intent type, and regulatory domain alignment. Furthermore, we present FATR, a finance-aware tool retrieval and reasoning baseline that enhances stability and compliance. By providing the first testbed for auditable, agentic financial execution, FinToolBench sets a new standard for trustworthy AI in finance. The tool manifest, execution environment, and evaluation code will be open-sourced to facilitate future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决金融领域大语言模型（LLM）智能体在真实工具使用场景中缺乏有效评估基准的核心问题。研究背景是LLM正推动金融行业从被动信息检索转向动态、自主的交互，工具调用型智能体被越来越多地用于连接金融数据和API。然而，现有评估方法存在显著不足：一方面，通用的工具学习基准（如API正确性测试）缺乏金融领域特有的严格性，常依赖模拟环境或极少量的金融工具，无法覆盖金融业务高风险、强监管、数据时效性强的核心需求；另一方面，现有的金融领域评测主要集中于静态文本分析或基于文档的问答，几乎不涉及可执行工具，忽略了工具实际执行的复杂性。因此，当前方法难以区分一个智能体是仅仅“正确执行了工具调用”，还是其工具选择在金融关键维度上“真正可接受”。

本文要解决的核心问题，正是填补这一空白，即如何系统、真实地评估金融工具学习智能体在现实世界中的表现。具体而言，论文提出了首个可运行的、面向真实金融工具的评测基准FinToolBench，它不仅评估工具调用的成功与否，更关键的是引入了金融领域特有的评估维度——时效性、意图约束和监管领域对齐——来衡量工具调用链的合规性与可接受性，从而应对因数据过时、意图误判或领域错配而可能导致的严重金融风险。

### Q2: 有哪些相关研究？

本文的相关研究可分为三大类：**通用工具学习与智能体评测**、**金融领域评测基准**以及**基于LLM的自动评估方法**。

在**通用工具学习与智能体评测**方面，代表性工作包括ReAct、Toolformer等工具学习框架，以及API-Bank、StableToolBench等大规模工具调用评测基准。此外，AgentBench、WebArena等基准侧重于在真实环境中评估智能体的长程交互能力。本文的FinToolBench与这些工作的核心区别在于**领域专属性**：通用基准缺乏金融领域所需的高风险性、强合规性和数据时效性等严格约束，常依赖模拟环境或极少数金融API，而本文构建了包含760个可执行金融工具的真实生态系统。

在**金融领域评测**方面，现有工作如FinanceBench、FinQA、TAT-QA等主要聚焦于静态文本分析或基于文档的问答，评估的是领域知识而非工具执行能力。近期工作如Finance Agent Benchmark虽引入了工具使用，但未提供标准化的大型工具库，也缺乏对工具调用层面合规性的度量。本文则首次建立了**以执行为基础**的评测环境，通过配对可执行工具与必须使用工具才能解答的问题，并引入时效性、意图类型和监管领域对齐等金融关键维度进行评估，填补了从静态问答到可审计、可执行工作流的空白。

在**评估方法**上，相关研究如MT-Bench、G-Eval等利用LLM作为评判员进行结构化评分。本文借鉴了此类方法，但通过重复评判、明确分离工具执行失败与答案正确性评估，以降低评估的不稳定性，并确保评测结果更可靠。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FinToolBench的基准测试平台，并结合一个名为FATR的基线方法，来解决金融领域大语言模型（LLM）智能体在真实工具使用中面临的评估缺失问题。

**核心方法与架构设计：**
论文的核心是构建一个**可执行的、基于真实金融工具的基准测试系统**。其整体框架分为两大部分：1）**FinToolBench基准测试平台**的构建；2）**FATR（Finance-Aware Tool Routing）基线智能体**的设计。

**FinToolBench的主要模块与关键技术：**
1.  **工具库构建与规范化**：从RapidAPI（实时网络API市场）和AkShare（开源Python金融数据库）两个互补生态中，通过严格的**可执行性过滤管道**（包括接口有效性、去重、速率限制、认证可行性和运行时可调用性测试）筛选出760个可执行的金融工具。每个工具被统一规范化为一个**工具清单**，包含标识符、描述和机器可读的参数签名，确保了异构工具的可用性。
2.  **问题集构建与对齐**：从现有金融QA数据集中，筛选出**必须依赖工具调用**才能回答的295个问题（包括166个单工具问题和129个多工具问题）。通过一个两阶段流程（基于BGE-M3的粗粒度检索和基于Qwen3-8B的LLM验证投票）建立问题与工具之间的**高置信度对齐**，并引入人工抽查确保质量。
3.  **金融属性标注与评估框架**：创新性地为每个工具标注了一套**轻量级金融属性模式**，包括：**更新频率**（用于评估调用及时性）、**意图类型**（信息性、咨询性、交易性，用于防止意图升级）、**监管领域**（用于确保领域对齐）。这使得评估超越了简单的“执行成功与否”，能够从**能力**和**合规性**两个维度进行细粒度评估。能力指标包括工具调用率、执行成功率等；合规性指标则基于工具执行轨迹，使用LLM法官来判定每次调用在及时性、意图和领域上是否违反约束，并计算失配率。

**FATR基线方法的关键创新点：**
FATR是一个**金融感知的工具检索与推理基线**，其创新在于将金融约束显式地注入到一个通用的LLM规划器中，而非训练专用模型。
1.  **约束感知的规划流程**：面对一个用户问题，FATR首先让LLM**推断约束集合**，明确问题所隐含的及时性要求、意图边界和监管领域。
2.  **工具卡片与检索**：通过检索获取Top-K相关工具，并将每个工具呈现为包含其金融属性标签的**标准化工具卡片**。这缩小了动作空间，并将约束信息直接暴露给规划器。
3.  **约束引导的ReAct循环**：LLM规划器在一个ReAct循环中进行工具调用决策。整个规划过程受到推断出的约束集合的引导，例如，避免选择意图类型不匹配（如非交易性问题使用交易性工具）或监管领域不交集的工具。对于多工具问题，鼓励先解析歧义（如确定正确的市场），以确保下游调用的领域一致性。

总之，论文通过构建一个大规模、可执行、带有精细金融属性标注的基准测试环境（FinToolBench），并设计一个将领域约束显式融入推理过程的基线智能体（FATR），系统地解决了对金融领域LLM智能体进行现实、可审计、多维度评估的难题。

### Q4: 论文做了哪些实验？

论文实验围绕FinToolBench基准展开，旨在评估不同LLM代理在真实金融工具使用场景下的性能。实验设置采用统一的代理框架FATR，该框架集成了工具检索、金融属性注入和稳定执行模块，仅更换LLM规划器以对比不同模型。评估覆盖全部295个问题，每个问题最多进行5轮工具调用，每轮可发出多个工具调用，单次调用超时60秒并允许最多2次重试。工具执行在受控环境中进行，具有确定性缓存和完整日志记录。

数据集为FinToolBench，包含760个可执行金融工具和295个需要工具使用的查询，问题按单工具/多工具以及问题类别进行分层。对比方法包括多个代表性LLM规划器后端：Doubao-Seed-1.6、Qwen3-8B、GLM-4-7-Flash和GPT-4o。所有模型使用相同的工具库、检索结果和执行环境，以确保性能差异仅源于规划器的推理和工具选择能力。

评估指标超越传统的二进制执行成功率，重点考察金融关键维度：及时性（timeliness）、意图类型（intent type）和监管领域对齐（regulatory domain alignment）。具体采用LLM作为评判员（使用GPT-5.1）进行答案正确性和需求推断评估，每个判断重复三次以减少方差，对于及时性等软指标（\soft）取三次评分的平均值；对于合规性评估，每个工具调用执行一次LLM评判，输出匹配/不匹配的离散标签。主要结果显示，不同LLM规划器在金融工具使用的稳定性、合规性和推理准确性上存在显著差异，突显了领域特定评估的必要性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其工具库和查询集虽已相当丰富，但仍主要基于免费层级的公开API，未能完全覆盖金融领域核心的、依赖专有实时数据流（如彭博终端）的高频交易或深度分析场景。此外，当前评估框架假设工具API本身是稳定且合规的，但现实世界中金融工具的接口、政策及监管要求会持续演变，智能体在此动态环境下的长期鲁棒性尚未得到充分检验。

未来研究方向可从三方面深入：一是**生态扩展**，纳入模拟或沙盒环境下的专有数据源与高风险工具（如期权交易），以评估智能体在更严苛场景下的决策能力。二是**动态适应性研究**，设计机制使智能体能主动监测API更新、监管政策变动及市场异常，并实现安全自适应，例如通过强化学习与合规性模块的动态耦合。三是**推理可解释性增强**，当前FATR基线虽提升了稳定性，但其决策过程仍较“黑箱”；可探索将金融知识图谱或规则引擎嵌入推理链，使工具选择与参数生成更具可审计性，这对于满足金融监管的透明性要求至关重要。这些改进将推动智能体从“能执行工具”向“能安全、合规、适应性地解决复杂金融问题”演进。

### Q6: 总结一下论文的主要内容

这篇论文针对金融领域大语言模型（LLM）智能体工具使用的评估空白，提出了首个真实、可运行的基准测试平台FinToolBench。核心问题是现有金融评估多集中于静态文本分析，而通用工具学习基准又缺乏金融领域所需的高风险性、强合规性和数据时效性等专业严谨性，无法有效评估智能体在真实金融场景中执行复杂工具操作的能力。

论文的主要贡献是构建了一个高度仿真的金融工具生态系统，包含760个可执行的金融工具和295个需要调用工具才能解决的严格查询。方法上，论文不仅评估工具执行的二进制成功率，还创新性地提出了一个多维度评估框架，重点考察金融领域至关重要的**时效性、意图类型和监管领域对齐**。此外，论文还提出了一个金融感知的工具检索与推理基线方法FATR，以增强智能体执行的稳定性和合规性。

主要结论是，FinToolBench为可审计的、具备自主执行能力的金融AI智能体提供了首个测试平台，通过开源其实测环境与评估代码，为未来研究树立了新标准，推动了金融领域可信AI的发展。
