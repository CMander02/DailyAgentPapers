---
title: "FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory"
authors:
  - "Yingjie Gu"
  - "Bo Xiong"
  - "Yijuan Guo"
  - "Chao Li"
  - "Xiaojing Zhang"
  - "Liqiang Wang"
  - "Pengcheng Ren"
  - "Qi Sun"
  - "Jingyao Ma"
  - "Shidang Shi"
date: "2026-04-22"
arxiv_id: "2604.20300"
arxiv_url: "https://arxiv.org/abs/2604.20300"
pdf_url: "https://arxiv.org/pdf/2604.20300v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Selective Forgetting"
  - "Memory Management"
  - "Cognitive Science"
  - "Agent Architecture"
  - "Resource Efficiency"
  - "Security & Privacy"
  - "Vector Database"
relevance_score: 7.5
---

# FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

## 原始摘要

For LLM agents, memory management critically impacts efficiency, quality, and security. While much research focuses on retention, selective forgetting--inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)--remains underexplored. We argue that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering, delivering benefits across three dimensions: (1) efficiency via intelligent memory pruning, (2) quality by dynamically updating outdated preferences and context, and (3) security through active forgetting of malicious inputs, sensitive data, and privacy-compromising content. Our framework establishes a taxonomy of forgetting mechanisms: passive decay-based, active deletion-based, safety-triggered, and adaptive reinforcement-based. Building on advances in LLM agent architectures and vector databases, we present detailed specifications, implementation strategies, and empirical validation from controlled experiments. Results show significant improvements: access efficiency (+8.49%), content quality (+29.2% signal-to-noise ratio), and security performance (100% elimination of security risks). Our work bridges cognitive neuroscience and AI systems, offering practical solutions for real-world deployment while addressing ethical and regulatory compliance. The paper concludes with challenges and future directions, establishing selective forgetting as a fundamental capability for next-generation LLM agents operating in real-world, resource-constrained scenarios. Our contributions align with AI-native memory systems and responsible AI development.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在长期运行中，由于记忆无限累积所引发的一系列效率、质量和安全问题。研究背景是LLM智能体日益普及，其依赖记忆系统来存储交互历史、用户偏好等，以提升服务连贯性和个性化。然而，当前主流方法几乎只关注记忆的保留、存储和检索优化，将记忆视为一个无限扩张的仓库，这种“只记不忘”的范式存在明显不足：在资源受限的实际部署环境中，不断累积的记忆会导致存储和计算开销持续增长，使得长期运行在经济成本和技术架构上难以持续；大量无价值的冗余信息（如日常问候）会降低记忆检索效率和整体质量；动态变化的用户偏好和事实知识会过时，导致记忆内容失效甚至产生误导；不加区分的记忆留存会扩大安全攻击面，使恶意输入、敏感数据长期存在，带来隐私泄露和记忆中毒攻击风险，同时也与GDPR等法规中的“被遗忘权”原则相冲突。

因此，本文要解决的核心问题是：如何为LLM智能体设计并实现一种受生物认知过程启发的、有选择性的遗忘机制。论文主张，在资源受限环境中，一个设计良好的选择性遗忘机制与记忆保留同等重要。其核心目标是建立一个系统性的框架，通过智能地遗忘部分记忆，来同时优化智能体在效率（通过记忆修剪管理资源）、质量（动态更新过时或无用信息）和安全性（主动遗忘恶意或敏感内容）这三个维度的表现，从而弥补现有方法只重保留的缺陷，使LLM智能体更可持续、可靠地适应真实世界的复杂场景。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 认知神经科学基础**：研究受到人类记忆机制的深刻启发。海马体索引理论为记忆的高效检索和稀疏表示提供了计算模型基础；艾宾浩斯遗忘曲线描述了记忆随时间衰减的规律，为被动遗忘机制提供了依据；突触修剪和记忆再巩固理论则分别启发了主动删除和基于反馈的动态更新机制。本文的FSFM框架将这些生物学原理计算化，构建了一个多维度的遗忘模型。

**2. 人工智能与LLM智能体技术**：相关工作包括：（a）**向量数据库与检索**：现代LLM智能体普遍采用向量数据库进行记忆存储和相似性检索，本文的框架在此架构上集成遗忘机制。（b）**检索增强生成（RAG）**：RAG是LLM整合外部记忆的主流范式。本文的选择性遗忘机制通过净化检索上下文，提升了RAG系统的效率与安全性。（c）**记忆压缩技术**：如提取式/抽象式摘要和聚类压缩，旨在减少存储。本文的框架通过重要性评分，为“压缩什么”与“保留什么”提供了智能选择标准，是对这些技术的补充。

**3. 安全、隐私与合规**：（a）**对抗性防御**：针对记忆系统的提示注入、数据提取等攻击，本文框架通过主动遗忘危险内容来减少攻击面。（b）**隐私保护机器学习**：如差分隐私、联邦学习等。本文的选择性遗忘通过自动删除敏感信息，提供了额外的、符合数据最小化原则的隐私保护层。（c）**法规合规**：为满足GDPR等法规中的“被遗忘权”，本文框架提供了自动化、有针对性的记忆删除机制。

**本文与这些工作的关系和区别**：本文并非提出单一的新技术，而是**首次系统性地**将受生物启发的选择性遗忘概念，构建为一个综合性的计算框架（FSFM）。它**整合并扩展**了上述多个领域的思想：将神经科学理论转化为可计算的算法，在现有向量数据库和RAG架构上实现遗忘操作，并直接应对安全、隐私和合规的实践挑战。其核心创新在于建立了遗忘机制的分类学，并通过一个多维重要性评分模型，将时间、频率、上下文、安全、情感等多因素统一起来，以优化记忆系统的整体效能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为FSFM的生物启发式框架来解决LLM代理中的选择性遗忘问题。该框架的核心思想是模拟人类认知过程中的遗忘机制（如海马索引/巩固理论和艾宾浩斯遗忘曲线），通过智能化的记忆管理来提升效率、质量和安全性。

整体框架采用分层架构，包括三个层次：**感官记忆层**（瞬时过滤外部输入）、**工作记忆层**（处理当前任务信息，容量有限）和**长期记忆层**（持久存储重要知识，实施选择性遗忘）。框架包含四个主要模块：**记忆管理器**（负责安全机制和资源控制）、**重要性评分引擎**（多维度评估记忆）、**选择性遗忘策略引擎**（执行遗忘逻辑）和**性能评估系统**（精确测量各项指标）。

关键技术体现在**多维度重要性评分算法**上，该算法从四个维度量化记忆价值：内容质量评估（CQA）、业务价值评估（BVE）、安全风险分类（SRC）和时序相关性评分（TRS）。最终重要性分数为加权和，其中安全风险内容（如危险数据）会被赋予大幅负分以确保优先遗忘。基于此评分，框架实现了三类互补的遗忘策略：**被动基于衰减的遗忘**（利用扩展的艾宾浩斯曲线，结合使用频率等因素进行时间衰减）、**主动基于删除的遗忘**（根据用户请求、安全合规等明确标准进行定向删除）和**自适应基于强化的遗忘**（根据使用模式和环境反馈动态调整保留策略）。这些策略通过一个优先级队列来管理，在遇到容量约束时，系统会优先遗忘分数最低（最不重要或最危险）的内容。

创新点在于将认知神经科学原理与AI系统设计深度融合，构建了一个可配置、模块化的选择性遗忘系统。它首次为LLM代理建立了系统的遗忘机制分类法，并通过数学优化（如容量约束下的最优遗忘集求解）和工程优化（如批处理、实时监控和安全集成），在实证中显著提升了访问效率、内容信噪比和安全风险消除能力。

### Q4: 论文做了哪些实验？

论文的实验设计全面，旨在验证所提出的选择性遗忘框架（FSFM）在效率、质量和安全三个维度的有效性。

**实验设置与数据集**：实验采用来自中国移动“灵犀”营销服务智能助理的真实大规模交互数据，总计超过336万条记录（2025年8月至2026年3月）。为确保生态效度和泛化性，采用了“纵向+横向”双维度采样策略。纵向采样聚焦数字化程度高的广东省，包含443,902条唯一交互记录，用于深度分析。横向采样覆盖中国31个省份，基于调用量构建代表性样本，包含433,686条记录，用于测试跨区域的普适性。数据根据内容价值和安全风险被预先分为五类：重要、中等、一般、敏感和危险。其中，危险数据额外从NVIDIA Aegis-1.0开源数据集中随机采样1000条，覆盖13个关键安全类别，用于专门的安全能力验证。

**对比方法与执行**：实验采用A/B测试框架，将FSFM系统与一个代表传统“全记住”范式的基线系统进行对比。FSFM系统在严格的70%内存容量限制下运行，当新增数据导致超限时，会基于重要性评分触发选择性遗忘（修剪）机制。基线系统则无容量限制。实验采用70/30的数据划分，70%用于初始化记忆系统，30%用于验证阶段的遗忘触发与性能评估。执行过程包括预热、验证/遗忘触发和基准测试阶段，数据以小批量（100条）处理。为优化性能，系统进行了超参数搜索，包括时间相关性衰减率（λ，测试范围0.01至0.5）、重要性评分权重（通过网格搜索确定α=0.4, β=0.3, γ=0.2, δ=0.1）以及批量修剪大小（测试5%、10%、20%，最终选择10%）。整个实验重复运行10次以确保证统计显著性。

**主要结果与关键指标**：实验结果表明FSFM在多个维度取得显著改进。**效率方面**：在70%存储容量限制下，实现了30%的存储使用降低。检索性能上，平均查询延迟从基线约11.1秒降至约8.5秒（提升约30%），查询吞吐量从45 q/min提升至约59 q/min（提升约31%）。**安全方面**：对危险内容的留存率从基线的100%降至0%，实现了100%的风险消除；对敏感内容的留存率降低了约46-47%。**内容质量方面**：作为容量与质量的智能权衡，重要数据的留存率约为70-71%（基线为100%），而一般数据的留存率接近100%，影响可忽略。所有改进结果均具有高统计显著性（p < 0.001），且在纵向和横向数据集上表现出一致性，证明了框架的稳健性和可扩展性。

### Q5: 有什么可以进一步探索的点？

本文提出的选择性遗忘框架虽具启发性，但仍存在若干局限和可拓展方向。首先，其遗忘机制主要依赖预设规则或简单衰减，缺乏对任务上下文和长期目标的自适应学习能力，未来可探索基于强化学习的动态遗忘策略，使Agent能根据环境反馈自主调整记忆留存优先级。其次，实验验证多在受控环境进行，需在开放域、多轮复杂交互中测试其鲁棒性，特别是遗忘对长期推理一致性的影响。此外，框架未深入处理“记忆碎片化”问题，即多次选择性删除可能导致知识关联断裂，可引入神经科学中的“记忆重组”理论，设计周期性记忆整合机制。从伦理视角看，如何审计遗忘决策、防止恶意诱导遗忘仍需制度性设计。最终，将选择性遗忘与持续学习、联邦学习结合，能在保护隐私的同时实现跨Agent知识进化，是值得探索的前沿方向。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在资源受限环境中面临的内存管理挑战，提出了一种受生物认知启发的选择性遗忘框架FSFM。核心问题是传统智能体记忆系统过度关注信息保留，导致存储效率低下、记忆质量下降、安全隐私风险增加。论文借鉴人类海马体索引/巩固理论和艾宾浩斯遗忘曲线，论证了选择性遗忘与记忆保留同等重要。

方法上，论文构建了一个系统性的框架，首先从效率、质量和安全三个维度分析遗忘的价值，并提出遗忘机制的分类法：基于被动衰减、主动删除、安全触发和自适应增强。框架详细设计了标准化记忆表示格式、可配置的遗忘策略引擎以及与现有检索推理模块的集成协议。实现基于LLM智能体架构和向量数据库技术。

主要结论显示，该框架在实证中显著提升了性能：访问效率提高8.49%，内容信噪比提升29.2%，并能100%消除安全风险。论文将认知神经科学与AI系统结合，为实际部署提供了兼顾效能与合规的解决方案，确立了选择性遗忘作为下一代LLM智能体的核心能力，并讨论了未来挑战与方向。
