---
title: "Knowledge Graph Representations for LLM-Based Policy Compliance Reasoning"
authors:
  - "Wilder Baldwin"
  - "Sepideh Ghanavati"
date: "2026-04-30"
arxiv_id: "2604.27713"
arxiv_url: "https://arxiv.org/abs/2604.27713"
pdf_url: "https://arxiv.org/pdf/2604.27713v1"
categories:
  - "cs.AI"
tags:
  - "合规智能体"
  - "RAG+知识图谱"
  - "LLM Agent框架"
  - "政策推理"
relevance_score: 7.5
---

# Knowledge Graph Representations for LLM-Based Policy Compliance Reasoning

## 原始摘要

The risks posed by AI features are increasing as they are rapidly integrated into software applications. In response, regulations and standards for safe and secure AI have been proposed. In this paper, we present an agentic framework that constructs knowledge graphs (KGs) from AI policy documents and retrieves policy-relevant information to answer questions. We build KGs from three AI risk-related polices under two ontology schemas, and then evaluate five LLMs on 42 policy QA tasks spanning six reasoning types, from entity lookup to cross-policy inference, using both heuristic scoring and an LLM-as-judge. KG augmentation improves scores for all five models, and an open, LLM-discovered schema matches or exceeds the formal ontology.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI系统在快速融入软件应用时带来的政策合规性风险问题。随着欧盟AI法案、NIST AI风险管理框架等治理文件的出台，开发者需要同时遵守多项交叉引用的复杂政策要求，但现有方法存在不足：大型语言模型虽能处理文本，却难以从参数化知识中可靠提取政策条款细节，而传统文本检索方式缺乏对政策结构关系的保留。为此，本文提出一个基于知识图谱的智能体框架，通过将AI政策文档构建为结构化图谱，结合LLM进行自动化的政策合规推理。核心创新在于：1）采用端到端流程（分块提取-模式约束生成-智能体检索）构建政策知识图谱；2）设计六类推理任务（从实体查找至跨政策推理）评估系统效果；3）对比标准模式（基于AI风险本体）与开放模式（LLM自主发现）的建模效果。最终通过42组QA实验证明，知识图谱增强可显著提升所有测试模型的合规推理准确率（+0.17至+0.55），特别是政策原文引用类任务中提升最明显，同时验证了开放模式可达到甚至超越人工定义模式的效果。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

**方法类**：一类工作聚焦于利用LLM自动构建知识图谱（KG），如CoDe-KG在标注三元组上达到92.4% F1，AutoKG通过多智能体协调提取与推理阶段。另一类研究LLM增强的KG检索，例如Graph RAG生成社区摘要、RoG基于KG结构进行多跳推理、SubgraphRAG通过并行三元组评分检索子图。本文在此基础上探索面向政策合规的KG构建与检索，特别比较了两种本体模式（形式化本体与LLM发现的开本体）对推理效果的影响。

**应用类**：GraphCompliance将监管文本分解为策略图，RAGulating Compliance抽取无本体三元组并采用分段检索，PrivComp-KG结合GDPR KG与SWRL规则检查。这些工作均针对单一政策验证图方法，而本文首次实现跨三个AI政策框架的推理（T6类型），涵盖EU AI Act、GDPR等政策间的联合查询。

**评测类**：OPP-115和PolicyQA提供隐私政策阅读理解基准，PolicyIE支持结构化抽取，LegalBench包含162项法律推理任务。本文在此基础上构建了涵盖6种推理类型的42项政策QA任务，尤其是新增了跨政策推理任务，弥补了现有基准的不足。

### Q3: 论文如何解决这个问题？

该论文提出了一种基于知识图谱（KG）增强的智能体框架，用于提升大语言模型（LLM）在AI政策合规推理任务中的准确性和可解释性。核心方法是一个四阶段流水线：分块、提取、检索和答案合成。

首先，**分块代理**采用“扫描+审查”的两阶段设计，通过滑动窗口识别自然语义边界（如章节结尾），确保每个文本块长度不超过4000字符，同时保留文档逻辑结构。**提取代理**则负责将每个文本块结构化为带类型的知识图谱，比较了两种本体模式：一种是基于AI风险本体（AIRO）的封闭式预定义类型（如风险、后果、缓解措施），另一种是开放式的涌现模式，允许LLM自行生成蛇形命名标签（如technical_risk）。提取过程采用两遍扫描：先提取实体，再提取关系，并通过上下文整合（如已有实体ID、跨策略高价值实体）实现增量式多源提取。此外，还通过嵌入余弦相似度（阈值0.70）为不同策略来源的实体创建跨策略对应关系边。

**检索阶段**采用自适应双路径架构，由路由代理根据问题复杂度判断路径：简单问题（如定义查询、单条款查找）走直接路径，通过嵌入检索Top-5种子实体并扩展1跳邻居；复杂问题（如多跳推理、跨策略链接）进入ReAct循环的代理路径，使用关键词搜索、语义搜索、邻居扩展等5种图工具，最多7步探索后调用答案综合工具。最终**答案合成代理**接收证据实体（按关系类型序列化）、原始文本块、ICL示例和问题，生成基于KG的合规答案。整体框架以MCP服务器形式提供16个工具、7个资源和8个提示，兼容任何MCP客户端。

创新点包括：1）将政策文档转化为可查询的结构化知识图谱；2）对比封闭式与开放式本体模式在提取和推理上的表现；3）自适应双路径检索路由有效降低简单问题的计算开销；4）通过跨策略对应边实现多政策文本的联合推理。实验采用42个覆盖6种推理类型的政策QA任务，结合启发式评分和LLM作为裁判进行双重评估，结果显示KG增强使所有5个模型得分提升，且开放模式表现不亚于形式化本体。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涉及5个模型（gpt-5-mini、gpt-4.1-mini、nemotron:30b、gpt-oss:20b、granite4:micro）在三种条件（无上下文基线NC、AIRO本体KG、开放涌现模式KG）下的对比。数据集包含从三份AI风险相关政策文档构建的KGs，评估使用42个政策QA任务，涵盖六种推理类型（T1实体查找到T6跨策略推理）。评估指标包括启发式评分（0-1）和LLM-as-judge评分（1-5），每条件运行5次。

主要结果：KG增强全面提升了所有模型的评分。最强的启发式增益出现在gpt-5-mini（AIRO +0.120，Open +0.128），而最大judge增益在gpt-oss:20b（+0.46 AIRO，+0.55 Open）。开放模式在judge评分上匹配或略超AIRO。按任务类型，T1和T3（属性检索）增益最显著（启发式提升+0.11至+0.40），而T4（多跳推理）依赖模型能力，granite4:micro出现-0.04的轻微下降。T6跨策略推理在judge评分上展现一致改进。关键发现是两种指标均证实KG > NC，且开放模式在四种模型上优于AIRO。

### Q5: 有什么可以进一步探索的点？

该研究的核心局限在于评估规模和自动化程度的有限性。首先，42个问题的测试集过小，且仅涵盖三部英语AI政策文件，导致个别问题对任务类型得分影响过大，且无法推广到非英语或不同法律体系的司法管辖区。其次，依赖单词重叠的启发式评分器低估了同义或冗长但正确的回答，而完全自动化评估缺乏开发者用户研究，无法验证KG增强答案的实际可操作性。未来方向可从三方面改进：一是扩展多语言、多司法管辖区的政策文档及更大规模的问答集，以增强泛化性；二是引入语义相似度评分器（如基于嵌入的匹配）来替代单词重叠，并评估KG构建的跨运行方差以消除模型间比较的混淆因素；三是进行用户研究，探索如何将KG证据更好地整合到合规工作流中。此外，针对跨策略推理的词汇壁垒，可尝试构建同义或跨本体映射层，或利用LLM自动发现词汇对齐规则，以提升对“数据中毒”与“训练偏差”等跨术语概念的检索能力。

### Q6: 总结一下论文的主要内容

该论文提出一个基于知识图谱的框架，用于增强大语言模型在AI政策合规性推理上的表现。问题定义为：AI特性在软件应用中快速集成带来风险，需从政策文档中提取信息以回答复杂的合规性问题。方法上，作者构建基于三种AI风险政策文档的知识图谱，采用两种本体架构，并评估五种大语言模型在42项覆盖六种推理类型的政策问答任务上的性能，使用启发式评分和大语言模型作为裁判。主要结论是：知识图谱增强对所有五种模型的评分均有提升，其中启发式F1最高提升0.13，大语言模型裁判评分提升0.55；基于大语言模型自动发现的本体架构表现优于或等于形式化标准本体。核心贡献在于证明了知识图谱能有效提升大语言模型在政策合规性推理中的准确性和可靠性，而自动构建的本体可降低对人工标准本体的依赖，意义是为AI安全合规评估提供了可扩展的技术方案。
