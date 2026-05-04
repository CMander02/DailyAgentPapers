---
title: "TADI: Tool-Augmented Drilling Intelligence via Agentic LLM Orchestration over Heterogeneous Wellsite Data"
authors:
  - "Rong Lu"
date: "2026-04-30"
arxiv_id: "2605.00060"
arxiv_url: "https://arxiv.org/abs/2605.00060"
pdf_url: "https://arxiv.org/pdf/2605.00060v1"
categories:
  - "cs.AI"
  - "eess.SY"
tags:
  - "LLM Agent"
  - "Tool-Augmented Agent"
  - "Domain-Specific Agent"
  - "Drilling Intelligence"
  - "Data Integration"
  - "Multi-Step Reasoning"
  - "Evidence Grounding"
relevance_score: 8.5
---

# TADI: Tool-Augmented Drilling Intelligence via Agentic LLM Orchestration over Heterogeneous Wellsite Data

## 原始摘要

We present TADI (Tool-Augmented Drilling Intelligence), an agentic AI system that transforms drilling operational data into evidence-based analytical intelligence. Applied to the Equinor Volve Field dataset, TADI integrates 1,759 daily drilling reports, selected WITSML real-time objects, 15,634 production records, formation tops, and perforations into a dual-store architecture: DuckDB for structured queries over 12 tables with 65,447 rows, and ChromaDB for semantic search over 36,709 embedded documents. Twelve domain-specialized tools, orchestrated by a large language model via iterative function calling, support multi-step evidence gathering that cross-references structured drilling measurements with daily report narratives. The system parses all 1,759 DDR XML files with zero errors, handles three incompatible well naming conventions, and is backed by 95 automated tests plus a 130-question stress-question taxonomy spanning six operational categories. We formalize the agent's behavior as a sequential tool-selection problem and propose the Evidence Grounding Score (EGS) as a simple grounding-compliance proxy based on measurements, attributed DDR quotations, and required answer sections. The complete 6,084-line, framework-free implementation is reproducible given the public Volve download and an API key, and the case studies and qualitative ablation analysis suggest that domain-specialized tool design, rather than model scale alone, is the primary driver of analytical quality in technical operations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决石油钻井行业中，从异构操作数据中提取可执行情报时面临的效率低下和自动化程度不足的问题。在石油上游工业中，一口井的钻探会产生海量、多模态的数据，包括每日钻井报告、实时传感器记录、地质数据等。现有的方法存在明显不足：电子钻井记录器虽能捕获高频传感器数据，但无法与叙述性报告整合；钻井分析平台需要手动配置，且无法理解自由文本的操作描述；而最近应用的大语言模型（LLM）也被当作被动处理器，需要人工预先选择数据，无法自主规划检索和分析路径。因此，核心问题在于如何从被动的、需要大量人工介入的数据处理与分析，转向一个能自主导航异构数据源、调用领域特定工具、并进行多步推理的主动智能系统。本文提出的TADI系统旨在通过一个智能体系统，无缝整合结构化查询（SQL）与语义搜索，实现跨模态证据的自动化收集与生成，从而将钻井工程师从繁琐的手工报告阅读与交叉参考中解放出来。

### Q2: 有哪些相关研究？

TADI的相关研究可归纳为四类：  
1. **工具增强与智能体系统**：基于ReAct框架，TADI通过领域专用工具（如相检测、NPT分类）扩展了Toolformer、Gorilla和HuggingGPT的思路。与ToolLLM和API-Bank的通用API不同，TADI的12个工具封装了钻井工程专业知识，需在有限调用预算内自主决策，强调工具设计而非模型规模。  
2. **NLP在钻井领域的应用**：从Antoniak等人的逻辑回归文本挖掘到Kumar等的大模型微调，相关工作通常将语言模型作为预设数据的处理器。TADI的创新在于智能体架构：大模型自主决定检索内容、工具调用和跨模态证据关联（如结构化测量与文本报告交叉验证）。  
3. **检索增强生成**：超越标准RAG，TADI实现“结构化-语义混合RAG”——通过DuckDB执行聚合、分组等分析型SQL查询，结合ChromaDB向量搜索，并设计SQL关键词回退机制。这与HybridRAG的结构与非结构化混合不同，更强调智能体的分析性查询能力。  
4. **Volve数据集相关工作**：TAD首次将Volve数据集的五种模态（日报、WITSML、生产记录、地层顶界、射孔）集成至统一的大模型可分析框架，区别于Tunkiel等人的实时钻探分析、Nikitin的场开发优化等单一模态研究。

### Q3: 论文如何解决这个问题？

TADI通过三项核心设计原则解决钻井数据分析问题：框架无关的简洁性、嵌入工具的领域知识、以及双重来源证据架构。整体采用双存储架构——DuckDB处理12张表65,447行结构化数据的SQL查询，ChromaDB存储36,709个文档嵌入用于语义检索。12个领域专用工具（表1）由LLM通过迭代函数调用编排，每个工具封装特定钻井分析算法（如相位检测、NPT分类、风险评分等），工具输出不依赖LLM采样方差。核心创新点在于：将Agent行为形式化为顺序工具选择问题，通过最大化证据基础分数（EGS）引导多步交叉验证证据收集；系统提示词强制要求答案同时引用结构化测量数据（深度、时长、速率）和带归属的日报叙述引用；输出验证器检查6个必需章节、测量数值和日报引用是否存在。关键设计包括：273行两阶段相位检测算法（先按井眼直径检测主相位，再按活动代码划分子相位）、349行多源根因关联问题检测、651行五模式现场基准排名（含复合困难指数和风险评分），以及161行的确定性日报叙述检索工具（确保每个推理链末尾调用该工具获取带来源归属的文本证据）。95个自动化测试和130个压力测试问题验证了系统可靠性。

### Q4: 论文做了哪些实验？

论文对TADI系统进行了多维度的实验评估，包括四个质量维度：证据基础、推理质量、领域正确性和覆盖范围。实验使用包含130个压力测试问题的分类体系，涵盖6个操作类别（相位识别与验证20个、时间与效率分析21个、钻速性能21个、BHA配置有效性20个、操作问题与根本原因26个、综合比较与建议22个）。系统基于Equinor Volve Field数据集，处理了1,759份每日钻井报告、WITSML实时对象、15,634条生产记录等数据，采用DuckDB（12张表，65,447行）和ChromaDB（36,709个嵌入文档）的双存储架构。主要案例研究包括：为15/9-F-11 T2井识别三大钻井阶段（工具执行0.2秒）、识别操作问题（119个问题/NPT活动占24.1%）、跨井对比分析。系统提出证据基础得分（EGS），综合测量、DDR引用和回答部分三个要素。消融实验分析了SQL-only、无向量存储、通用提示、无交叉引用、仅DDR五种变体的预期影响，表明领域专用工具设计比模型规模更关键。系统通过95个自动化测试（包括配置、解析、工具测试）和全面的130问题验证。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：首先，系统依赖Volve数据集单一来源，未验证在不同地质条件、数据质量或钻井场景下的泛化能力；其次，Evidence Grounding Score（EGS）作为评估指标仅关注引用完整性与准确性，未量化推理链的因果逻辑强度或决策可解释性；再者，工具编排依赖固定规则迭代调用，缺乏动态优先级学习机制。未来可探索方向包括：引入自适应工具选择策略，通过强化学习优化工具调用序列以提升复杂查询效率；构建跨数据集迁移学习框架，利用预训练领域知识增强低资源场景的鲁棒性；设计更细粒度的多模态证据链验证方法（如时空对齐的传感器-文本矛盾检测）；也可尝试将符号推理（如钻井物理约束）融入神经-符号编排框架，增强对异常工况的因果推理能力。此外，结合在线上下文蒸馏技术降低LLM调用成本，或在边缘端部署轻量化工具集以满足实时钻井监控需求，均是值得关注的突破点。

### Q6: 总结一下论文的主要内容

TADI系统将钻井操作数据转化为基于证据的分析智能，解决了现有工具无法自主整合结构化传感器数据与文本报告的问题。该系统在Equinor Volve数据集上实现，采用DuckDB（12张表、65,447行数据）与ChromaDB（36,709个嵌入文档）的双存储架构，通过大语言模型编排12个领域专用工具进行多步证据检索与交叉引用。核心贡献包括：将智能体行为形式化为序列化工具选择问题，提出证据归因评分（EGS）量化双源引用质量；构建包含130个压力测试问题的钻井操作分类体系；零错误解析1,759份DDR XML文件并整合多种异构数据源。研究表明，领域专用工具设计而非模型规模是决定技术分析质量的关键因素。
