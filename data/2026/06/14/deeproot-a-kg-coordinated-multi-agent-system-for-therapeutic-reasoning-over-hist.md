---
title: "DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts"
authors:
  - "Zijian Carl Ma"
  - "Sean J. Wang"
  - "Sijbren Kramer"
  - "Li Erran Li"
date: "2026-06-14"
arxiv_id: "2606.15931"
arxiv_url: "https://arxiv.org/abs/2606.15931"
pdf_url: "https://arxiv.org/pdf/2606.15931v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "知识图谱协作"
  - "大语言模型智能体"
  - "药物发现"
  - "历史医学文本"
relevance_score: 7.5
---

# DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts

## 原始摘要

Historical medical archives and traditional medicines hold immense potential for drug discovery and remain a primary source for current drug development. However, pre-ontological prose and idiosyncratic taxonomies prevent the standardization and medical modernization of the data for use in current biomedical pipelines. Furthermore, no existing LLM agent system, whether tool-calling, retrieval-augmented, or agentic deep-research, can convert such text into verifiable drug-discovery leads at scale. We close this gap with DeepRoot, a multi-agent LLM system that jointly builds and utilizes a verified knowledge graph, showing that grounding and reasoning -- often conflated -- are separable axes the system can compose for therapeutic reasoning. Applied to the Shen Nong Ben Cao Jing, DeepRoot recovers $10$ of $21$ held-out compound-disease treatment pairs at R@$20$ ($47.6\%$ vs $4.8\%$ for a raw corpus LLM and $\sim\!2.4\%$ random) and dominates an LLM-as-judge audit for reasoning quality over baseline LLMs and LLMs with direct tool-call access to the same APIs DeepRoot itself queries. Tool-using LLMs hallucinate evidence on $87\%$ of claims, versus 7-10% for DeepRoot. Graph-only inference hallucinates $0\%$ but ranks lowest on reasoning coherence; DeepRoot KG+LLM is the only condition to win on both axes, pointing toward a route for systematic mining and repurposing of historical medical knowledge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何从历史医学文献中大规模、可验证地挖掘药物发现线索的问题。研究背景方面，天然产物是药物开发的主要来源，许多重要药物（如青蒿素）均源于对传统医学文献的挖掘。然而，现有方法存在明显不足：首先，历史医学文本使用前本体论散文和特有条目分类法，缺乏标准化，难以与当代生物医学知识管道对接；其次，现有的基于大语言模型（LLM）的智能体系统（包括工具调用、检索增强或深度研究型）均无法将此类文本转化为可验证的药物发现线索——它们要么将文本视为纯输入分类问题而缺乏推理轨迹，要么在构建知识图谱时依赖专家监督和纯LLM生成结果，缺乏对生物实体的严格验证。深层次问题是：这些系统往往混淆了“知识锚定”（grounding）与“推理”（reasoning），导致要么幻觉率高（如直接使用工具调用的LLM在87%的声明上产生幻觉），要么推理连贯性差。因此，本文提出DeepRoot，一个基于知识图谱协调的多智能体LLM系统，通过分离锚定与推理流程，联合构建并利用经严格验证的知识图谱，实现对历史医学典籍中治疗关系的可验证、可推理的识别，从而系统性地挖掘和再利用历史医学知识。

### Q2: 有哪些相关研究？

相关工作可以分为三类：**KG构建方法类**、**推理评测类**和**多Agent系统类**。

- **KG构建方法类**：直接相关的是**OpenTCM**，其采用Graph-RAG架构进行LLM推理，但构建过程依赖专家监督和纯LLM生成，缺乏严格验证。本文的DeepRoot通过七个专用Agent协作，将LLM规范化与生物医学数据库（如Neo4j）的严格验证相结合，实现了知识图谱的自动化、可信构建，降低了人工成本。

- **推理评测类**：以往ML/DL/LLM方法（如用于挖掘《神农本草经》的文本分类模型）将文本视为纯输入分类问题，缺乏基于已验证生物学证据的推理轨迹。DeepRoot则分离了“知识锚定”与“推理”两个维度，通过图谱遍历（Cypher查询）与LLM批判性推理的组合，在药物-疾病治疗对召回率上显著优于原始语料LLM（47.6% vs 4.8%），且工具调用型LLM在87%的生成结果中产生幻觉，而DeepRoot仅为7-10%。

- **多Agent系统类**：现有工作虽使用共享KG进行多Agent协调，但未对图谱与Agent的解耦进行消融实验。DeepRoot首次通过严格对照实验（纯图谱推理零幻觉但推理连贯性最低，KG+LLM组合则同时在两维度最优）证明了“图谱锚定”与“LLM推理”是可分离、可组合的核心构件，为历史医学知识的系统性挖掘与重利用提供了验证路径。

### Q3: 论文如何解决这个问题？

DeepRoot通过一个知识图谱协调的多智能体系统解决历史医学文本中治疗推理的难题。整体框架分为知识图谱构建和下游推理两个阶段。在构建阶段，系统采用七种专业化智能体按依赖顺序协作：提取器从原始文本中识别源、疾病和制备方法节点；审计员标准化源节点并归档无法匹配的文本片段；三个链接器分别将实体与化合物库（COCONUT2.0/PubChem）、分子靶点库（ChEMBL）和靶点-疾病关联（Open Targets/NCBI Taxonomy）连接；疾病映射器采用“生成-验证”协议，由LLM提出候选名称后仅通过容错精确匹配恢复本体代码，杜绝幻觉标识符；审核员归档未匹配实体。最终生成包含6种节点类型和7种边类型的知识图谱（如21,111个节点和52,467条边）。关键技术在于实体身份的确定性归约：化合物使用RDKit计算的InChIKey，靶点使用ChEMBL ID，确保不同来源的等价实体自动合并。创新点体现在三个层面：一是将知识图谱构建作为可重复的预处理步骤（单次成本约0.25美元），避免推理时反复查询外部数据库的高开销；二是通过图谱的机械闭环（源化合物→靶点→疾病）实现可验证的治疗推理；三是分离了其它系统常混淆的“接地”（grounding）与“推理”（reasoning），使图谱仅负责事实性约束（零幻觉），LLM负责推理连贯性，两者组合后同时在真实性和推理质量上超越基线方法。

### Q4: 论文做了哪些实验？

论文通过四个实验系统评估DeepRoot系统。**实验一：KG消融实验**，通过逐步打乱知识图谱边（0%-100%），让Critic代理评估30个源文本-疾病对的治疗合理性置信度。结果显示，随着扰动增加，置信度下降，约50%扰动时与原始LLM基线持平，验证KG结构的关键作用。**实验二：候选化合物恢复实验**，在30个迷你语料库（每个含3个闭环和7个非闭环源）中测试。DeepRoot Discovery的源召回率@3为0.41，化合物召回率@10为0.48，分别超过LLM基线1.95倍和6.11倍。**实验三：盲恢复实验**，在21个历史治疗对（ChEMBL临床指征）中隐藏已知药物-疾病边后重新排名。DeepRoot以R@20=47.6%恢复10个，显著优于原始文本LLM的4.8%（1个）和随机基线~2.4%。**实验四：推理质量审计**，用Claude Sonnet 4.6评估7种条件（30个源文本-疾病对）。三个KG增强配置（DeepRoot）总体得分3.70-3.83，幻觉率仅7-10%；工具调用LLM幻觉率达87%，图推理幻觉率0%但推理连贯性最低。此外，与Biomni对比显示，DeepRoot在50个样本中39个判断为“合理或更好”，疾病分类一致率42%，判决一致率30%。

### Q5: 有什么可以进一步探索的点？

单凭《神农本草经》这一部 71 篇的典籍验证，样本仅 21 对，缺乏置信区间和跨语料库迁移验证，是核心局限。未来可扩展至阿育吠陀、民族药典等非本体论语料，同时建立更大规模金标准数据集以增强统计效力。第二，图谱构建依赖 LLM 的篇章切分与实体抽取质量，可引入主动学习或人工审核迭代优化图谱边界。第三，当前评分仅基于 Open Targets 人类疾病数据库，对非现代适应症或新化合物-疾病关联无效，可集成多层级证据源（如化学结构相似性、基因网络扰动）实现更鲁棒的零样本排序。第四，推理质量受底层 LLM 的认知边界约束，可探索将 KG 子图直接作为结构化提示输入强推理模型（如链式思维强化学习），或设计可微分推理层以端到端学习治疗路径权重。最后，DeepRoot Assembly 虽为一次性低成本调用，但拒绝热启动更新模式，应支持增量图谱修正并保持溯源审计能力。

### Q6: 总结一下论文的主要内容

历史医学文献和传统医药包含大量潜在的药物发现资源，但因其非标准化文本和独特分类体系而难以被现代生物医学流程利用。现有的大语言模型代理系统无法大规模地将这些文本转化为可验证的药物发现线索。为此，本文提出DeepRoot，一个多智能体大语言模型系统，它通过七个专用智能体协同构建并利用经过验证的知识图谱。该系统将通常混淆的知识图谱构建（推理前提）与基于图谱的推理（结论）分离，并组合使用。应用于《神农本草经》时，DeepRoot能召回21个保留化合物-疾病治疗对中的10个（R@20为47.6%），远超原始语料大语言模型的4.8%和随机水平，且在推理质量评估中优于基线模型。工具调用式大语言模型在87%的声明中出现幻觉，而DeepRoot仅为7-10%。纯图谱推理虽无幻觉但连贯性最差，而DeepRoot的KG+LLM组合在事实性和推理连贯性上均表现最优，为系统性挖掘和再利用历史医学知识指明了道路。
