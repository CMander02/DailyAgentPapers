---
title: "AutoVerifier: An Agentic Automated Verification Framework Using Large Language Models"
authors:
  - "Yuntao Du"
  - "Minh Dinh"
  - "Kaiyuan Zhang"
  - "Ninghui Li"
date: "2026-04-03"
arxiv_id: "2604.02617"
arxiv_url: "https://arxiv.org/abs/2604.02617"
pdf_url: "https://arxiv.org/pdf/2604.02617v1"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.IR"
  - "cs.LG"
  - "cs.SI"
tags:
  - "Agent Framework"
  - "Automated Verification"
  - "Knowledge Graph"
  - "Structured Reasoning"
  - "Multi-step Agent"
  - "Scientific Intelligence"
  - "Claim Verification"
relevance_score: 7.5
---

# AutoVerifier: An Agentic Automated Verification Framework Using Large Language Models

## 原始摘要

Scientific and Technical Intelligence (S&TI) analysis requires verifying complex technical claims across rapidly growing literature, where existing approaches fail to bridge the verification gap between surface-level accuracy and deeper methodological validity. We present AutoVerifier, an LLM-based agentic framework that automates end-to-end verification of technical claims without requiring domain expertise. AutoVerifier decomposes every technical assertion into structured claim triples of the form (Subject, Predicate, Object), constructing knowledge graphs that enable structured reasoning across six progressively enriching layers: corpus construction and ingestion, entity and claim extraction, intra-document verification, cross-source verification, external signal corroboration, and final hypothesis matrix generation. We demonstrate AutoVerifier on a contested quantum computing claim, where the framework, operated by analysts with no quantum expertise, automatically identified overclaims and metric inconsistencies within the target paper, traced cross-source contradictions, uncovered undisclosed commercial conflicts of interest, and produced a final assessment. These results show that structured LLM verification can reliably evaluate the validity and maturity of emerging technologies, turning raw technical documents into traceable, evidence-backed intelligence assessments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学与技术情报分析中，对快速增长的技术文献进行复杂技术主张验证的难题。研究背景是，在科学出版物快速涌现的时代，情报分析的核心挑战已从信息匮乏转变为信号有效性甄别，即需要区分真正的技术突破与渐进式或纯理论贡献，并验证报告结果的方法论严谨性、检测结论超越证据的过度宣称，以及识别利益冲突。现有方法，如命名实体识别和事实核查系统，仅能处理问题的个别方面，难以应对技术文档中复杂且相互依赖的主张，导致在表面事实准确性与深层方法论有效性之间存在一个未被弥合的“验证鸿沟”。

现有方法的不足在于，它们无法系统性地对技术主张进行结构化分解和跨源、跨层级的深度推理验证。同时，尽管大语言模型为解决此问题提供了潜力，但其固有的幻觉倾向和可能产生看似合理却无证据支持的结论，限制了其直接应用。

因此，本文要解决的核心问题是：如何构建一个自动化的、结构化的验证框架，以弥补上述验证鸿沟，在不依赖领域专家的情况下，实现对技术主张端到端的、可追溯的、基于证据的智能评估。为此，论文提出了AutoVerifier这一基于大语言模型的智能体框架。其核心解决方案是将每个技术断言分解为（主体、谓词、客体）形式的结构化主张三元组，并构建知识图谱，通过一个包含六个渐进丰富层级的管道（语料构建与摄取、实体与主张提取、文档内验证、跨源验证、外部信号佐证、最终假设矩阵生成）进行结构化图推理，从而将原始技术文档转化为可验证的、有据可查的情报评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要包括：
1.  **基于命名实体识别（NER）和事实核查的系统**：这些传统方法主要关注从文本中提取离散事实或核查简单的声明，但难以处理技术文档中复杂且相互依存的论断，无法弥合表面事实准确性与深层方法论有效性之间的“验证鸿沟”。
2.  **基于大型语言模型（LLM）的推理**：LLM为复杂推理提供了潜力，但其存在“幻觉”倾向，可能产生看似合理但缺乏支持的结论，缺乏结构化约束。

在应用类研究中，相关工作主要涉及**科学文献分析和技术情报（S&TI）评估**，但现有方法通常依赖领域专家进行手动、耗时的分析，缺乏自动化、可扩展且不依赖领域知识的端到端验证框架。

**本文与这些工作的关系和区别**：
AutoVerifier框架与上述工作既有继承也有显著创新。它**区别于**传统NER/事实核查系统，通过将复杂技术主张分解为（主体，谓词，客体）三元组并构建知识图谱，实现了超越表面事实的**结构化图推理**，以进行多跳因果分析和矛盾检测。它**利用并改进了**LLM的能力，通过一个严格的六层管道（从语料构建到最终假设矩阵生成）来引导和约束LLM的推理过程，从而**弥补了**纯LLM方法容易产生幻觉的缺陷，将LLM的推理优势与结构化验证框架相结合。最终，它实现了一个**自动化、端到端且不依赖领域专家**的验证流程，这是对传统依赖专家的S&TI分析方法的重大突破。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AutoVerifier的、基于大语言模型（LLM）的智能体化框架，以端到端的方式自动化验证技术主张，而无需依赖领域专家知识。其核心方法是设计一个六层、流水线式的结构化推理架构，每一层都是一个LLM驱动的智能体模块，接收前序层的结构化输出，并将 enriched 的结果传递给下一层，最终生成可追溯的、基于证据的评估。

**整体框架与主要模块：**
1.  **语料库构建与摄取层**：首先构建一个全面、无偏的证据基础。通过搜索学术论文、专利等多源文档，并基于引用量等信号评估其质量。随后进行文本提取与向量嵌入、视觉资产处理（利用视觉-语言模型解析图表）和元数据对齐，将处理后的数据存入向量数据库，形成可检索的证据基。
2.  **实体与主张提取层**：从文档中提取关键实体，并将每个技术断言分解为结构化的（主体，谓词，客体）三元组。创新性地为每个三元组标注一个五级**溯源分类**（从基于实验数据的L1到无证据的作者断言L5），并对定量主张进行**度量标准化**，以识别定义差异。输出可视为一个知识图谱。
3.  **文档内验证层**：评估单个文档的内部一致性。通过**主张-证据对齐**（使用自然语言推理风格判断证据是支持、矛盾还是中立）和**方法论-结果一致性**检查，来验证文档自身的证据是否支持其主张。同时进行**过度主张检测**，标记超出证据范围的结论。
4.  **跨源验证层**：比较不同来源的主张三元组。通过引文网络遍历、语义相似性搜索和基于实体的图遍历来**发现相关主张**。对匹配的主张进行**引文保真度**检查（检测“引文扭曲”）和**矛盾根因分析**（追溯方法差异等原因）。最后评估**来源独立性**（基于作者重叠、机构关联等），并加权计算跨源共识分数。
5.  **外部信号佐证层**：将技术主张置于更广泛的非学术背景下。通过分析公开数据构建实体的**财务档案并检测利益冲突**，通过多跳推理进行**供应链依赖映射**，并解析新闻稿以整合**战略信号**，构建事件时间线。
6.  **最终假设矩阵生成层**：聚合前五层所有信息（溯源级别、一致性结论、跨源共识、实体信号），为每个主张三元组生成统一的证据档案。通过思维链提示生成可检验的假设及对抗性反假设，并基于多轮生成的语义熵和多个独立LLM的一致性来估计**置信度**。最终输出一个假设矩阵，包含假设、证据、一致性、置信度、反假设及最终标签（如“支持”、“需审查”），并附带技术成熟度评估。

**关键技术及创新点：**
*   **结构化分解与知识图谱**：将非结构化文本主张转化为结构化的（主体，谓词，客体）三元组，并构建知识图谱，为后续各层的结构化推理和关联分析奠定了基础。
*   **分层渐进式验证架构**：六层设计实现了从微观证据对接到宏观背景分析的逐层深化验证，逻辑清晰，模块化强，支持证据的追溯。
*   **多维度证据评估体系**：创新性地引入了**五级溯源分类**，区分了主张的证据根基；结合了**内部一致性检查**、**加权跨源共识分析**以及**外部非技术信号佐证**，形成了立体、全面的评估框架。
*   **智能体化与LLM的深度应用**：各层核心任务（如实体提取、NLI推理、根因分析、假设生成）均通过精心设计的提示工程驱动LLM完成，实现了复杂推理的自动化。
*   **多模态与多源信息融合**：不仅处理文本，还通过视觉-语言模型处理图表；不仅分析学术文献，还整合财务、供应链、新闻等多源外部信号，提升了评估的深度和现实相关性。

### Q4: 论文做了哪些实验？

论文通过一个量子计算案例研究进行实验，评估AutoVerifier框架在无需领域专业知识的情况下验证技术声明的能力。实验设置上，团队测试了两种实现方式：一是使用Perplexity Sonar（第1-2层）和Google Gemini Pro（第3-6层）的多LLM顺序管道；二是使用Claude Code的单智能体框架，通过提示调用内置工具（如网络搜索、文档检索）自动执行六层验证流程。数据集/基准测试方面，针对目标论文《Runtime Quantum Advantage with Digital Quantum Optimization》及其相关文献，构建了包含11个来源的语料库，涵盖目标论文、4篇支持论文、3篇独立反驳、2篇独立基准测试和1个外部评估框架。

主要结果包括：1）从目标论文中提取了17个实体和20个经过溯源性分类的声明三元组，其中仅30%（6个）被内部证据完全支持；2）发现量子运行时排除了约2秒的转换开销，这与报告的0.2-2.2秒总运行时相当，若包含该开销将显著削弱声称的加速优势；3）跨源验证显示，所有独立评估均反驳了“运行时量子优势”主张，且目标论文的作者存在未披露的商业利益冲突（所有作者受雇于Kipu Quantum）；4）假设矩阵最终将“运行时优势是真实的”假设评估为“可能幻觉”，置信度低，而将“优势是测量假象”评估为“支持”，置信度高。关键数据指标包括：声明三元组支持率30%、语义熵值（支持发现0.12，争议发现0.68）、量子转换开销约2秒、经典初始化开销约1.65秒，以及声称的80倍加速被确认为单一异常值（中位数加速约5-7倍）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其验证能力高度依赖外部知识库的覆盖度和质量，若相关领域文献稀疏或存在偏见，可能影响结论的可靠性。此外，框架对LLM的依赖性较强，可能受模型幻觉或上下文窗口限制，在处理极长或高度专业化的文档时存在风险。

未来研究方向可围绕以下几点展开：一是增强框架的主动学习能力，使其能自动识别知识缺口并主动查询或生成假设，而非被动依赖现有语料；二是引入多模态验证，例如结合专利图表、实验数据或代码仓库，提升对方法细节的核查深度；三是开发动态可信度评估机制，为不同来源的证据赋予随时间演变的权重，以应对科学共识的变化。此外，可探索将框架扩展至实时监测场景，如自动追踪预印本或会议报告的更新，实现持续验证。最后，考虑融入领域专家的人类反馈循环，通过少量干预校准自动化决策，平衡效率与准确性。

### Q6: 总结一下论文的主要内容

该论文提出了AutoVerifier，一个基于大语言模型（LLM）的智能体框架，旨在自动化完成科技情报分析中复杂技术主张的端到端验证，以弥合表面准确性与深层方法有效性之间的“验证鸿沟”。其核心贡献在于设计了一个无需领域专家知识的、结构化的六层验证流程：语料构建与摄取、实体与主张提取、文档内验证、跨源验证、外部信号佐证以及最终假设矩阵生成。该方法首先将技术主张分解为（主体、谓词、客体）三元组形式，并构建知识图谱以支持结构化推理。

论文通过在量子计算领域一个有争议的“运行时间优势”主张上进行演示，表明该框架能有效识别目标论文中的夸大陈述和指标不一致性，追踪跨文献矛盾，揭露未公开的商业利益冲突，并生成最终评估。主要结论是，结构化的LLM验证能够可靠地评估新兴技术的有效性和成熟度，将原始技术文档转化为可追溯、有证据支持的情报评估，从而证明了LLM无需分析师具备先验领域知识即可完成深度验证的潜力。未来工作方向包括将各层模块化为可复用的智能体技能以支持定制化，以及从静态评估转向持续监控的动态情报更新。
