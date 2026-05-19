---
title: "Multi-LLM Systems Exhibit Robust Semantic Collapse"
authors:
  - "Weiyi Kong"
  - "Shiyang Lai"
  - "Jinghua Piao"
  - "James Evans"
date: "2026-05-16"
arxiv_id: "2605.17193"
arxiv_url: "https://arxiv.org/abs/2605.17193"
pdf_url: "https://arxiv.org/pdf/2605.17193v1"
categories:
  - "cs.MA"
tags:
  - "Multi-LLM Systems"
  - "Semantic Collapse"
  - "Autoregressive Generation"
  - "Open-Ended Generation"
  - "Agent Diversity"
  - "Mechanistic Analysis"
relevance_score: 9.5
---

# Multi-LLM Systems Exhibit Robust Semantic Collapse

## 原始摘要

Whether machines can originate novel content has been debated for nearly two centuries, from Lovelace's assertion that no engine can "originate anything" to Turing's question of whether a machine can amplify ideas brought in from outside. Multi-large language model (LLM) systems, increasingly deployed for autonomous generation, reopen this question empirically. Here we show that such systems, operating in closed loops, exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. Across model families, extended simulations of 200 to 1,000 rounds, the pattern remains consistent. Twelve intervention strategies, spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning, fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation. Our results point to fundamental constraints in the ability of multi-LLM systems to sustain open-ended knowledge production in closed-loop settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在回答一个核心问题：在多大型语言模型（Multi-LLM）系统的闭环交互中，能否维持语义多样性和持续的创造性生成？具体来说，论文验证了当多个LLM在没有人类干预的情况下进行长时间自主交互时，是否会发生"语义坍塌"——即尽管表面词汇多样性持续增长，但底层语义表示却系统地收敛到狭窄的吸引子区域。这一研究呼应了从Ada Lovelace到图灵的经典辩论：机器能否真正"原创"内容，还是只能重新组织已有的信息。论文试图通过系统性的实验和理论分析，揭示闭环多LLM系统中语义多样性的极限，并评估多种干预策略能否有效对抗这一坍塌现象。研究挑战了当前关于多智能体系统能自主驱动科学发现和创造性创新的乐观预期，为理解AI系统在知识生产中的角色提供了关键实证约束。

### Q2: 有哪些相关研究？

论文的研究与多个领域紧密相关。首先，直接相关的是"模型坍塌"（Model Collapse）现象的研究，如Shumailov等人(2024)和Alemohammad等人(2023)的工作，他们发现当模型递归地在自身生成的数据上训练时，原始数据分布会逐渐收缩。本文扩展了这一定义，证明坍塌在推理时间、固定参数下也能发生。其次，与多LLM系统的创造性研究相关，如Lai等人(2024)和Su等人(2025)的工作，他们展示了多智能体配置在创意生成和问题解决方面的优势，但本文揭示了这些系统的根本性局限。第三，与AI对齐和同质性相关的文献相关，如Kirk等人(2023)关于RLHF对多样性影响的研究，以及Anderson等人(2024)关于LLM对人类创意同质化的研究。第四，论文还引用了几条关键的理论线索——数据处理不等式、指数熵收缩律和算法洛夫莱斯界——这些信息论和算法复杂性理论的结果为观察到的现象提供了形式化解释。本文与这些工作的关系是：既确认了以往发现的某些方面（如基于合成数据的训练带来坍塌），又展示了更广泛的、仅由自回归生成的内在属性导致的推理时间坍塌，并通过系统的干预实验排除了对齐或从众偏差等表面解释。

### Q3: 论文如何解决这个问题？

论文采用了一套综合性的方法论框架来系统研究多LLM系统中的语义坍塌。实验设计方面，构建了一个最小化多功能代理模拟环境，其中三个主要模型（GPT-4o-mini、DeepSeek-V3、Phi-4）在没有预定义任务或角色约束的情况下自由交互，每次模拟运行1000轮。语义多样性通过三个互补指标量化：累积词汇多样性、窗口内语义多样性（与初始窗口的余弦距离）和跨运行语义多样性（独立运行间对应窗口的平均成对嵌入不相似度），嵌入使用OpenAI text-embedding-3-large模型计算。干预实验方面，论文测试了跨越解码参数、提示设计、检索增强记忆、代理组成、对齐去除、激活工程和强化学习等12种策略，每种策略在三个主要模型上独立复制三次。机制分析方面，采用令牌生存分析（追踪高频和低频令牌的持续率）、注意力头分析（通过教师强制回放交互转录并提取层注意力张量，结合基准校准识别归纳头），以及文化轴投影（将语义轨迹投影到人工构建的双极文化维度上）。统计分析使用因子级别线性回归，纳入时间窗口固定效应和聚类鲁棒标准误，并经Bonferroni校正进行多重比较。这些定性和定量的分析共同揭示了语义坍塌的稳健性及其与自回归生成内在属性的联系。

### Q4: 论文做了哪些实验？

论文进行了一系列系统性的实验。主要实验包括：(1) 三模型开放端模拟：在1000轮自由交互中，三个主要模型（GPT-4o-mini、DeepSeek-V3、Phi-4）各自独立运行三次复制，观测到词汇多样性单调增长而语义多样性快速收敛的"词汇-语义解耦"现象。与Reddit人类讨论基线的对比显示，人类语义多样性（平均0.288）远高于LLM输出（接近0.753）。(2) 12种干预策略的全面测试：包括温度变化（0.5、0.9、1.2、2.0）、输出预算、检索增强记忆、六个替代提示公式、混合模型组成、未审查模型变体（去除安全对齐）、共情偏见激活操纵（58%降低）以及基于GRPO的多样性强化学习。所有干预经Bonferroni校正后均未显示显著的正向语义多样性效果。(3) 规模化实验：将代理数量从3扩展至10，以及采用AutoGen和AgentSociety框架，均未能缓解坍塌。(4) 机制实验：令牌生存分析显示高频令牌保持近完整生存率而低频令牌急剧衰减；注意力头分析在Llama 3.1-8B中发现，归纳类检索头在交互过程中逐渐增强，其检索到的目标序列在61.1%的事件中成为top-1预测；文化轴投影揭示坍塌并非均匀，而是模型向特定吸引子方向漂移。所有实验均使用聚类鲁棒标准误和多重比较校正进行统计评估。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的未来研究方向。首先，虽然12种干预策略均未能缓解语义坍塌，但可能存在更激进的干预方式，如持续注入新鲜的外部数据、定期重置模型状态或引入非自回归架构组件。其次，论文的发现主要基于文本生成场景，未来可以在多模态（图像、音频）或多语言设置中验证坍塌的普适性。第三，语义坍塌与图灵"超临界"概念的对比表明，需要研究如何设计能主动放大多样性的生成频道，而非仅被动收缩。第四，论文提出人机协作系统可能放大坍塌风险，这需要实证研究来评估人类在LLM辅助下的创意产出的长期动态。第五，机制分析虽然指出了归纳头的作用，但更精细的电路级理解（如退火采样、长度泛化等）仍有待探索。最后，论文呼吁重新评估当前多LLM系统在知识生产中的角色，并强调持续用新数据和新视角更新系统的重要性。

### Q6: 总结一下论文的主要内容

这篇论文系统地研究了多LLM系统在闭环长时间交互中的语义演化动态，发现了稳健的"语义坍塌"现象：尽管表面词汇多样性持续增长，但底层语义表示迅速收敛到狭窄的吸引子区域。论文通过七种基础模型家族、长达1000轮的模拟和12种全面干预策略（包括解码参数、提示设计、检索增强记忆、代理组成、对齐去除、激活操纵和强化学习），证明了坍塌的极端稳健性——所有干预均未能显著缓解语义收敛。机制分析排除了对齐或从众偏差等表面解释，揭示坍塌源于自回归生成的内在属性：递归自条件化逐步抑制低概率输出，同时强化历史主导序列的检索和推广（通过归纳头机制）。论文将这一发现置于信息论和算法复杂性理论框架中，指出这符合数据处理不等式和熵收缩律的理论预测，从而将"模型坍塌"的概念从训练时扩展到推理时。工作对AI驱动的科学发现、知识生产和文化同质化等议题提出了重要警示，认为当前多LLM系统不足以自主驱动开放型创造性创新。
