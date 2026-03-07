---
title: "From Threat Intelligence to Firewall Rules: Semantic Relations in Hybrid AI Agent and Expert System Architectures"
authors:
  - "Chiara Bonfanti"
  - "Davide Colaiacomo"
  - "Luca Cagliero"
  - "Cataldo Basile"
date: "2026-03-04"
arxiv_id: "2603.03911"
arxiv_url: "https://arxiv.org/abs/2603.03911"
pdf_url: "https://arxiv.org/pdf/2603.03911v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CR"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "Cybersecurity"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "hypernym-hyponym semantic relation extraction, neuro-symbolic multi-agent system"
  primary_benchmark: "N/A"
---

# From Threat Intelligence to Firewall Rules: Semantic Relations in Hybrid AI Agent and Expert System Architectures

## 原始摘要

Web security demands rapid response capabilities to evolving cyber threats. Agentic Artificial Intelligence (AI) promises automation, but the need for trustworthy security responses is of the utmost importance. This work investigates the role of semantic relations in extracting information for sensitive operational tasks, such as configuring security controls for mitigating threats. To this end, it proposes to leverage hypernym-hyponym textual relations to extract relevant information from Cyber Threat Intelligence (CTI) reports. By leveraging a neuro-symbolic approach, the multi-agent system automatically generates CLIPS code for an expert system creating firewall rules to block malicious network traffic. Experimental results show the superior performance of the hypernym-hyponym retrieval strategy compared to various baselines and the higher effectiveness of the agentic approach in mitigating threats.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决网络安全领域响应新型威胁时存在的延迟和自动化配置难题。研究背景是网络攻击日益自动化，而防御方仍依赖人工分析威胁情报报告并手动配置安全控制措施（如防火墙规则），导致响应缓慢，形成攻防不对称。现有基于AI的方法虽尝试自动化处理威胁情报，但常受限于语义理解的不足、数据类别不平衡以及难以将文本描述准确映射到具体防御动作。

现有方法的不足主要体现在：传统AI方法在自动分类敏感安全数据时，因威胁类别数据严重不平衡而性能受限；同时，缺乏对威胁语义的深层理解，难以可靠地提取信息并生成可执行的防御代码。本文要解决的核心问题是：如何利用Agentic AI和大型语言模型，从网络威胁情报报告中自动、准确且可信地提取语义信息，并直接转化为可部署的专家系统规则（如CLIPS代码），以实现快速、自动化的威胁缓解。为此，论文提出基于上下位词关系的语义检索方法，增强对安全事件的理解，并通过多智能体系统生成防火墙规则代码，从而弥补从威胁情报到实际防御行动之间的语义鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：语义信息提取方法、网络安全应用中的AI系统架构，以及专家系统与代码生成技术。

在**语义信息提取方法**方面，现有研究通常关注于利用本体结构，但往往需要额外的训练数据来融入这种结构化知识。与之不同，本文采用了一种基于推理的神经符号方法，直接利用文本中固有的上下位词关系进行语义检索，无需额外训练。本文的方法通过多阶段提示策略（实体提取、语义抽象、操作执行）逐步深化理解，这与单次提取的现有方法形成对比，能更好地处理嘈杂冗长的网络威胁情报报告。

在**网络安全AI架构**方面，先前工作已探索了基于规则的专家系统和概率方法。本文的创新在于将认知心理学理论（如艾宾浩斯记忆衰减、柯林斯和奎利安的语义网络）实际整合到智能体框架中，扩展了CoALA框架。与通常采用决策树的实现方式不同，本文的智能体采用了基于图的知识库来跟踪概念，这更利于增量更新，并优化了代码生成过程。

在**专家系统与代码生成**领域，CLIPS作为基于规则的前向链推理引擎在网络安全中已有长期应用。本文的工作与之衔接，但重点是利用语义关系自动从威胁情报生成CLIPS代码（防火墙规则），实现了从非结构化文本到可执行安全策略的自动化转换，这区别于传统的直接分类或代码生成映射。

### Q3: 论文如何解决这个问题？

论文通过一个结合神经与符号人工智能的混合多智能体系统来解决从威胁情报自动生成防火墙规则的问题。其核心方法是设计了一个“语义信息流”管道，将非结构化的网络威胁情报报告转化为可执行的防火墙规则（如iptables规则）。

整体框架由两大主要模块构成：**增强型CoALA智能体**和**专家系统**。首先，增强型CoALA智能体作为神经组件，负责从CTI报告文本中提取关键的语义信息。其关键技术是采用了一种**迭代式上下位词检索策略**：智能体首先调用大型语言模型从文本中识别出具体的安全概念（下位词），然后进一步迭代检索出这些概念的更通用类别（上位词）。这种基于语义关系的提取方法，旨在更精准地捕获威胁的本质属性。

提取出的上位词随后被传递给符号人工智能组件——**专家系统A**。该模块的核心创新点在于充当了一个**语法验证层和防幻觉屏障**。它将上位词信息填充到预定义的CLIPS模板中，生成形式化的知识表示（如事实和产生式规则）。这一过程通过模板的顺序实例化，能够系统性地检测和阻止错误传播，确保了信息的逻辑一致性和可靠性。

最后，**精炼引擎**（内含专家系统B）根据已形式化的威胁语义信息，识别可用的安全控制措施，并生成具体的防火墙过滤规则。整个流程以一次最终的语法正确性验证作为收尾，确保生成的规则能被防火墙直接接受并执行。

论文的创新点主要体现在：1）利用上下位词语义关系进行信息提取，提高了从复杂文本中抽取安全相关概念的准确性；2）采用神经-符号混合架构，将LLM的灵活理解能力与专家系统的确定性、可验证性相结合，在追求自动化的同时保障了输出的可信度；3）在整个管道中实施了严格的确定性推理控制（如固定随机种子、贪婪解码等），使基于概率模型的LLM输出更稳定，便于与下游符号系统集成。

### Q4: 论文做了哪些实验？

论文进行了两项主要实验。实验在配备NVIDIA RTX 4090和RTX 5090 GPU的硬件平台上进行。

**实验设置与数据集**：
*   **任务A（语义提取评估）**：采用多标签分类实验，使用Dataset A。评估了三种方法：A-1基于静态/上下文嵌入（Word2Vec, GloVe, SecureBERT）；A-2基于提示方法（思维链CoT和本文方法）；A-3采用该领域传统机器学习方法（如朴素贝叶斯、SVM、随机森林）。本文方法使用Qwen2.5-Coder-14B-Instruct模型，并首次尝试为CLIPS规则提取进行语义增强提示。
*   **任务B（智能体框架评估）**：在Dataset B上运行完整的多智能体流水线以生成防火墙规则。评估了Qwen2.5-Coder-14B-Instruct和Foundation-Sec-14B-Instruct模型，最终选定前者。由网络安全专家对输出进行定性评估。

**对比方法与主要结果**：
*   在任务A中，本文提出的基于上下义关系的语义提取方法（A-2 Ours）在加权F1分数（0.329）和Top-10准确率（0.968）上表现优异，优于所有基线方法，证明了其在筛选相关文本片段上的更强能力。语义指标（BERTScore 0.858， ROUGE-L 0.444）也证实了其相关性。分析表明，下义词比上义词更有效，且设置较低的置信度阈值（如50%）能提升性能。
*   在任务B中，专家评估从三个维度衡量系统输出质量，并计算了评分者间一致性指标。结果显示，在**技术正确性**上Krippendorff‘s α最高（+0.5768），表明对语法正确性有强共识；**范围校准**的Spearman相关性最高（+0.7143），支持规则范围排序的一致性；**对CTI的忠实度**在所有指标上也保持较高水平，表明评估者间具有满意的一致性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，系统目前主要依赖超类-子类语义关系进行信息提取，未来可探索更复杂的语义关系（如部分整体关系、因果关系）以提升威胁情报理解的深度和广度。其次，实验虽验证了代理系统的有效性，但未充分评估其在动态对抗环境中的鲁棒性，例如面对对抗性提示或误导性威胁报告时的表现。此外，论文提到LLM的确定性探索尚属启发式阶段，未来需设计更严格的机制确保生成规则的可靠性与可解释性，例如结合形式化验证或规则一致性检查。从实际部署角度，可研究如何将系统与实时网络流量分析结合，实现自适应规则更新，并探索人机协同机制，允许安全专家对AI生成的规则进行校准与优化，以平衡自动化与可控性。最后，可扩展应用场景至其他安全控制领域（如入侵检测策略生成），验证架构的通用性。

### Q6: 总结一下论文的主要内容

该论文研究如何利用人工智能自动生成防火墙规则以应对网络威胁。核心问题是提升网络安全响应的速度和可靠性，特别是在从网络威胁情报报告中提取关键信息并转化为可执行规则方面。论文提出了一种混合AI智能体与专家系统架构，其方法核心是利用文本中的上下位词语义关系，从威胁情报报告中提取相关信息，并通过一种神经符号方法，使多智能体系统能自动生成CLIPS代码。该代码供专家系统使用，以创建拦截恶意流量的防火墙规则。实验结果表明，基于上下位词的检索策略性能显著优于多种基线方法，并且这种智能体方法在缓解威胁方面更为有效。论文的主要贡献在于验证了特定语义检索模块在入侵防御系统中的优越性，为在网络安全等敏感领域更可靠地使用大语言模型提供了方向。
