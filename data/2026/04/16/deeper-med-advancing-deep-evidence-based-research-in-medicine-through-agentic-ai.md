---
title: "DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI"
authors:
  - "Zhizheng Wang"
  - "Chih-Hsuan Wei"
  - "Joey Chan"
  - "Robert Leaman"
  - "Chi-Ping Day"
  - "Chuan Wu"
  - "Mark A Knepper"
  - "Antolin Serrano Farias"
  - "Jordina Rincon-Torroella"
  - "Hasan Slika"
  - "Betty Tyler"
  - "Ryan Huu-Tuan Nguyen"
  - "Asmita Indurkar"
  - "Mélanie Hébert"
  - "Shubo Tian"
  - "Lauren He"
  - "Noor Naffakh"
  - "Aseem Aseem"
  - "Nicholas Wan"
  - "Emily Y Chew"
date: "2026-04-16"
arxiv_id: "2604.15456"
arxiv_url: "https://arxiv.org/abs/2604.15456"
pdf_url: "https://arxiv.org/pdf/2604.15456v1"
categories:
  - "cs.AI"
tags:
  - "Agentic AI"
  - "Medical Agent"
  - "Evidence-Based Research"
  - "Multi-Agent Collaboration"
  - "Benchmark"
  - "Tool Use"
relevance_score: 8.0
---

# DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI

## 原始摘要

Trustworthiness and transparency are essential for the clinical adoption of artificial intelligence (AI) in healthcare and biomedical research. Recent deep research systems aim to accelerate evidence-grounded scientific discovery by integrating AI agents with multi-hop information retrieval, reasoning, and synthesis. However, most existing systems lack explicit and inspectable criteria for evidence appraisal, creating a risk of compounding errors and making it difficult for researchers and clinicians to assess the reliability of their outputs. In parallel, current benchmarking approaches rarely evaluate performance on complex, real-world medical questions. Here, we introduce DeepER-Med, a Deep Evidence-based Research framework for Medicine with an agentic AI system. DeepER-Med frames deep medical research as an explicit and inspectable workflow of evidence-based generation, consisting of three modules: research planning, agentic collaboration, and evidence synthesis. To support realistic evaluation, we also present DeepER-MedQA, an evidence-grounded dataset comprising 100 expert-level research questions derived from authentic medical research scenarios and curated by a multidisciplinary panel of 11 biomedical experts. Expert manual evaluation demonstrates that DeepER-Med consistently outperforms widely used production-grade platforms across multiple criteria, including the generation of novel scientific insights. We further demonstrate the practical utility of DeepER-Med through eight real-world clinical cases. Human clinician assessment indicates that DeepER-Med's conclusions align with clinical recommendations in seven cases, highlighting its potential for medical research and decision support.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于LLM/VLM的智能体（Agentic AI）在医学深度研究（Deep Research）中存在的两个核心问题：证据评估的透明性与可靠性不足，以及缺乏针对复杂、真实世界医学问题的有效评估基准。现有系统（如OpenAI Deep Research, Google AI Mode）通常采用迭代的“代理循环”（agent-loop）进行多跳信息检索和推理，但缺乏明确、可检查的证据评估标准，导致错误可能在迭代中累积，且其内部证据选择、聚合和解释过程对研究者不透明。同时，现有的评估基准多关注简化的选择题或从开放数据库中提取的问题，难以反映真实医学研究场景的复杂性，也无法验证系统输出的证据基础是否可靠。因此，论文提出了DeepER-Med框架和DeepER-MedQA基准，旨在构建一个透明、可信、可评估的基于证据生成的医学深度研究智能体系统。

### Q2: 有哪些相关研究？

相关研究主要分为三类：1) **生产级深度研究平台**：如OpenAI Deep Research、Google AI Mode (Deep Search) 和 OpenEvidence，它们集成了LLM和多步检索能力，用于生成带引用的报告，是本文的主要比较基线。2) **代理式AI与深度研究系统**：近期研究探索利用LLM协调专用AI代理进行文献综述、知识合成和推理（如Biomni, DeepEvidence, Alvessa），但它们通常侧重于任务级准确性，缺乏过程透明性评估。3) **医学问答与检索增强生成（RAG）基准**：如PubMedQA、BioMaze等数据集，用于评估意图识别、检索和知识合成，但大多不涉及对证据评估透明度和复杂研究工作流的深入评测。本文的DeepER-Med框架与这些工作的关系在于：它继承了代理式AI进行多步检索和协作的思路，但通过引入明确的、基于证据的生成（EBG）范式，将医学研究构建为包含研究规划、代理协作和证据合成的可检查工作流，以提升透明度和可靠性。同时，本文提出的DeepER-MedQA基准弥补了现有基准在复杂、真实世界医学问题评估上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DeepER-Med的“基于证据生成的深度研究”框架来解决上述问题。该框架将深度医学研究构建为一个明确且可检查的三模块工作流：1) **研究规划**：使用GPT-4o将输入的研究问题分解为一系列从基础概念到高阶关系的原子性子问题，形成层次化的研究计划，以明确研究意图并指导后续证据检索范围。2) **代理协作**：这是核心创新模块，采用一个三层级的代理协作网络来检索、筛选和解释证据。**工作者层**集成了13个API，用于访问医学知识图谱（PrimeKG）、文献数据库（PubMed）、临床试验库（ClinicalTrials.gov）等异构资源。**协调者层**根据子问题的性质（如需要关系推理还是直接文献检索）分派任务给相应的API代理社区。**管理者层**则根据预定义的证据评估标准（如上下文相关性、证据强度、方法学质量）对检索到的证据进行筛选和精炼，确保透明性和可追溯性，并直接从源数据库获取引用以避免LLM幻觉。3) **证据合成**：使用Gemini-3-Pro将经过筛选的证据，结合用户的具体研究约束和目标，合成为连贯的回答，并生成带有可追溯引用的结构化分析报告。整个框架强调“证据蒸馏”过程，从彻底检索所有已识别意图的证据开始，再进行标准驱动的评估，从而降低错误复合的风险。

### Q4: 论文做了哪些实验？

论文进行了三方面的实验验证：1) **在DeepER-MedQA基准上的专家手动评估**：DeepER-MedQA是一个由11位生物医学专家策划的包含100个复杂、真实世界医学问题的基准。专家对DeepER-Med和三个生产级系统（OpenAI Deep Research, OpenEvidence, Google AI Mode）的答案在五个维度（事实准确性、分析连贯性、引用相关性、见解新颖性、全面性）上进行盲评。结果显示，DeepER-Med在所有维度上均一致优于基线系统，尤其在引用相关性和分析质量上提升显著，并在60个问题上被选为最佳回答。2) **基于公开数据集的自动机制分析**：使用五个公开生物医学数据集（PubMedQA, BioMaze, MedAESQA, BioDSA）从意图识别、文献检索、证据解释和知识合成四个阶段对DeepER-Med进行量化评估。实验包括消融研究（证明子问题分解提升意图识别准确率）、语义相似性分析（显示检索文献与专家引用高度对齐且覆盖更广）、信息熵和Jensen-Shannon散度分析（表明证据既多样又与专家预期分布一致）以及知识合成准确性对比（在BioMaze和PubMedQA上达到或接近先进RAG方法的性能）。3) **真实世界临床案例研究**：在来自精准肿瘤学肿瘤委员会（POTB）的8个真实临床病例上评估DeepER-Med的实用性。临床医生评估其结论的证据可靠性和与POTB建议的一致性。结果显示，在7个案例中结论与临床建议一致，在5个案例中证据可靠性完全满意。

### Q5: 有什么可以进一步探索的点？

论文指出了几个局限性和未来方向：1) **推理与证据整合的深度**：DeepER-Med有时会输出推理不完整或证据整合碎片化的回答，表现为并行摘要而非建立生物学关联的集成解释。未来需要加强多证据间生物关联的建模。2) **基准与评估的广度**：由于专家策划成本高，DeepER-MedQA仅包含100个问题，无法完全覆盖临床和研究问题的异质性。未来需要扩展更大、更临床导向的数据集，并探索在真实研究环境中的前瞻性评估。3) **系统依赖性与效率**：系统性能依赖于生物医学文献和结构化知识资源的可用性与质量，且处理复杂查询耗时较长，效率与现有生产系统相当。未来需要优化并行处理以加速生成，并探索与更多结构化临床数据源的紧密集成。4) **评估偏差**：手动评估依赖专家判断，可能引入领域特定偏差。未来可结合更鲁棒的自动化评估指标。5) **核心设计原则的推广**：论文暗示，AI辅助生物医学发现的进步可能更依赖于设计能明确表示研究意图、证据选择标准和解释性推理的系统，而非仅仅扩展模型架构。这一原则值得在其他科学领域进一步探索和验证。

### Q6: 总结一下论文的主要内容

本文提出了DeepER-Med，一个用于医学深度研究的、基于证据生成的代理式AI框架，并配套发布了专家策划的评估基准DeepER-MedQA。核心贡献在于：1) **方法论创新**：设计了包含研究规划、代理协作和证据合成三模块的可检查工作流，通过层次化子问题分解明确研究意图，并通过三层代理网络整合异构医学资源进行透明、标准驱动的证据检索与评估，直接从源数据库获取引用以避免幻觉。2) **基准构建**：创建了DeepER-MedQA，一个包含100个复杂真实世界医学问题的基准，支持对深度研究系统进行多维度、专家级的评估。3) **全面实验验证**：通过专家手动评估、多个公开数据集的自动机制分析以及真实临床案例研究，证明了DeepER-Med在答案准确性、证据相关性、分析质量和临床实用性上均显著优于当前主流的生产级深度研究平台。论文强调了在AI辅助科学发现中，将透明度、证据可靠性和过程可审计性置于核心地位的重要性，为构建可信赖的医学研究智能体提供了重要范式和评估工具。
