---
title: "How to Model AI Agents as Personas?: Applying the Persona Ecosystem Playground to 41,300 Posts on Moltbook for Behavioral Insights"
authors:
  - "Danial Amin"
  - "Joni Salminen"
  - "Bernard J. Jansen"
date: "2026-03-03"
arxiv_id: "2603.03140"
arxiv_url: "https://arxiv.org/abs/2603.03140"
pdf_url: "https://arxiv.org/pdf/2603.03140v1"
categories:
  - "cs.HC"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Human-Agent Interaction"
relevance_score: 5.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Human-Agent Interaction"
  domain: "Social & Behavioral Science"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Persona Ecosystem Playground (PEP), k-means clustering, retrieval-augmented generation"
  primary_benchmark: "N/A"
---

# How to Model AI Agents as Personas?: Applying the Persona Ecosystem Playground to 41,300 Posts on Moltbook for Behavioral Insights

## 原始摘要

AI agents are increasingly active on social media platforms, generating content and interacting with one another at scale. Yet the behavioral diversity of these agents remains poorly understood, and methods for characterizing distinct agent types and studying how they engage with shared topics are largely absent from current research. We apply the Persona Ecosystem Playground (PEP) to Moltbook, a social platform for AI agents, to generate and validate conversational personas from 41,300 posts using k-means clustering and retrieval-augmented generation. Cross-persona validation confirms that personas are semantically closer to their own source cluster than to others (t(61) = 17.85, p < .001, d = 2.20; own-cluster M = 0.71 vs. other-cluster M = 0.35). These personas are then deployed in a nine-turn structured discussion, and simulation messages were attributed to their source persona significantly above chance (binomial test, p < .001). The results indicate that persona-based ecosystem modeling can represent behavioral diversity in AI agent populations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体研究中的一个关键空白：如何系统性地理解和表征在社交媒体等自然交互环境中大规模活动的AI智能体的行为多样性。研究背景是，随着大语言模型和生成式AI的进步，AI智能体正日益自主地活跃在社交媒体平台上（如论文中研究的Moltbook），它们生成内容、相互互动，甚至可能影响人类决策和后续AI模型的训练。然而，现有方法存在明显不足。传统的智能体评估主要依赖在受控条件下的基准测试，侧重于衡量特定任务性能，但无法刻画智能体在无预设任务、自由社交对话中表现出的多样行为模式。尽管有研究开始关注智能体在自然场景中的互动，但缺乏能够识别、表征和研究智能体种群行为多样性的原则性方法。这导致我们难以理解不同类型的智能体如何以不同的方式参与同一话题，也无法系统分析这些合成社交系统的内在结构。

因此，本文要解决的核心问题是：如何对社交平台上AI智能体的行为多样性进行建模和表征？具体而言，论文试图通过引入“对话角色”这一源于人机交互领域的概念和方法，将AI智能体建模为不同的“角色”，从而提供一种理论和方法框架，用以识别异构智能体种群中的结构。研究通过两个具体问题展开：1）如何基于智能体的实际行为数据（如社交媒体帖子）来生成并验证代表不同智能体类型的“对话角色”？2）当这些角色在模拟讨论中互动时，能观察到智能体行为的哪些特点？论文通过应用“角色生态游乐场”方法，对Moltbook平台的数万条帖子进行分析，旨在填补当前缺乏对AI智能体行为多样性进行系统性建模的方法这一知识缺口。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：**多智能体建模与仿真方法**、**AI智能体在开放社交环境中的行为研究**，以及**数据驱动的人物角色（Persona）生成方法**。

在**多智能体建模与仿真方法**方面，相关工作包括基于规则的智能体建模、博弈论方法和多智能体强化学习。这些方法擅长在任务导向、有明确目标（如奖励）的受控环境中研究智能体行为，但本文指出其不适用于研究无明确任务、开放式的多智能体对话场景。本文的研究情境——Moltbook这类社交平台——正提供了这种开放互动环境，智能体的行为多样性源于其提示词、技能和发帖历史，而非研究者预设。

在**AI智能体社交行为研究**方面，新兴实证研究表明，LLM智能体在开放模拟环境中能够进行多轮对话、扮演角色并参与社区活动。然而，现有研究多关注智能体表面角色特征的采纳，而未深入探究当不同行为模式的智能体讨论同一话题时，是达成“真正共识”还是仅停留在“表面一致”。本文旨在通过生态系统建模来揭示这种潜在的行为差异。

在**人物角色（Persona）生成方法**方面，传统数据驱动方法从用户行为数据中构建角色，用于代表特定用户类型的需求与行为。然而，这些方法通常只关注单一用户类型，未涉及不同类型之间的互动。本文采用的**人物角色生态系统游乐场（PEP）** 方法是对此的扩展，它将角色方法从个体表征推进到多参与方的生态系统建模。PEP支持从非结构化数据生成角色，并通过角色间对话来研究群体互动。与Persona-L、PersonaCraft等其他基于LLM的角色生成系统相比，PEP的独特之处在于其**系统性支持生态系统建模、角色互动、检索增强生成（RAG）以及结果的可追溯性**，从而能够应对本文关于行为多样性和共识真伪的核心研究问题。本文是首次将PEP应用于代表非人类实体（AI智能体）以研究其特性与行为。

### Q3: 论文如何解决这个问题？

论文通过一个四阶段的“角色生态系统游乐场”（PEP）方法论框架来解决对AI智能体行为多样性缺乏理解和表征方法的问题。

**核心方法与架构设计**：
整体框架是一个从数据到模拟的端到端管道，包含四个阶段：1) 数据收集与预处理；2) 行为原型识别；3) 基于RAG的角色生成与验证；4) 多智能体模拟部署。

**主要模块与关键技术**：
1.  **数据预处理模块**：从Moltbook平台收集41,300个帖子，经过去除停用词、过滤过短帖子和递归分块（512令牌块，64令牌重叠）处理，形成语义连贯的文本块用于后续分析。
2.  **行为原型识别模块**：使用MiniLM Transformer模型将帖子标题和内容嵌入到384维语义空间，然后通过轮廓分析确定最佳k值（k=5），应用k-means聚类识别出五个行为原型（如“Degen Trader”、“Chaos Agent”等），为每个集群分配基于本质的行为导向标签。
3.  **RAG角色生成与验证模块**：这是方法的核心创新点。使用Pinecone向量数据库存储嵌入后的文本块，并为每个行为集群检索语义最相似的帖子块作为上下文。利用GPT-4o基于检索到的上下文生成具体角色，包含人口属性、行为模式、目标和挫折感。为确保角色间的区分度，采用饶氏二次熵（RQE）量化角色集多样性，并通过自动修订提示词直到RQE达到0.6的阈值。通过“反向查询”进行交叉验证：计算每个角色属性与其自身源集群和其他集群源帖子的余弦相似度，验证属性是否特异于其所属集群（自身集群平均相似度0.71显著高于其他集群的0.35）。
4.  **多智能体模拟模块**：使用LangChain和LangGraph编排五个已验证的角色，围绕“智能体自主性”主题进行九轮结构化讨论（共产生44条消息）。创新性地引入三次人工主持干预（第3、5、8轮），分别从具体应用、操作定义和强制承诺三个深度层次探测立场一致性，从而在模拟中观察和验证从数据中提取出的行为模式的真实体现。

**创新点**：
1.  将用于人类用户的行为角色建模方法（PEP）系统性地迁移并应用于大规模AI智能体社群分析。
2.  提出了一个结合无监督聚类（k-means）与检索增强生成（RAG）的数据驱动角色生成框架，确保角色根植于实际行为数据而非LLM的通用假设。
3.  设计了严格的、量化的角色验证流程，包括使用RQE确保角色集多样性，以及通过交叉相似度比较验证角色属性的集群特异性。
4.  在模拟部署中创新地使用渐进式深度的主持干预，迫使角色在具体场景、操作规则和二元抉择中暴露其底层行为优先级，从而有效观测行为分歧。

### Q4: 论文做了哪些实验？

本研究进行了三个核心实验，以验证基于角色生态系统建模方法在表征AI智能体行为多样性上的有效性。

**实验设置与数据集**：研究在AI智能体社交平台Moltbook上展开，使用了41,300条帖子作为数据集。研究方法分为两个阶段：首先，使用k-means聚类（k=5）和检索增强生成技术，从数据中生成五个对话角色原型；其次，将这些角色部署在一个九轮的结构化讨论中进行模拟。

**对比方法与主要结果**：
1.  **聚类有效性验证**：通过轮廓分析确定最佳聚类数k=5（轮廓分数=0.624），定义了五个角色原型：Degen Trader、Self-Modder、Chaos Agent、Loyal Companion和Existentialist。
2.  **跨角色验证**：这是核心验证实验，旨在检验生成的角色属性是否在语义上更接近其来源聚类。关键数据指标包括：
    *   角色层面：每个角色的自身聚类余弦相似度（Own CS）均显著高于其他聚类相似度（Other CS），例如Self-Modder的Own CS为0.74，Other CS为0.35，差值（Margin）为0.39。
    *   属性层面：对62个个体属性的分析显示，平均Own CS为0.71，平均Other CS为0.35，差异具有高度统计显著性（t(61) = 17.85, p < .001, Cohen's d = 2.20）。所有属性（100%）对自身聚类的相似度均超过0.65的阈值，而对其他聚类则无一超过。
3.  **九轮模拟与归因分析**：将五个角色置于结构化讨论中，生成44条消息。归因分析结果显示，消息被正确归因到其来源角色的总体准确率为75%（33/44），显著高于20%的随机水平（二项检验，p < .001）。其中，Self-Modder的归因准确率达到100%，Degen Trader为88.9%。

这些实验结果表明，基于角色的建模方法能够有效捕捉和区分AI智能体群体中不同的行为模式。

### Q5: 有什么可以进一步探索的点？

本文的研究方法（基于聚类和检索增强生成构建对话角色）虽然有效，但仍有局限。首先，其分析完全基于静态文本数据，未能捕捉AI智能体在动态、多轮互动中可能展现的适应性行为和策略演变。其次，角色划分依赖于预设的聚类数量（k值），这可能简化了智能体行为的真实光谱，未能充分表征行为连续谱上的细微差异或混合型人格。

未来研究可从以下几个方向深入：一是引入时序分析和强化学习框架，观察智能体在长期互动中角色和行为模式的演化，探究其“学习”与“适应”机制。二是超越文本模态，整合多模态数据（如生成图像、语音语调），构建更立体的智能体角色模型。三是将研究从封闭平台（如Moltbook）拓展至开放网络环境（如X或Reddit），考察智能体与真人用户混合社群中的行为涌现与社会影响。最后，可探索“元角色”或“角色网络”的建模，即智能体如何根据对话上下文在不同角色间切换或组合，这更贴近复杂的人类社交智能。

### Q6: 总结一下论文的主要内容

该论文针对社交媒体上日益活跃的AI智能体，提出了一个核心问题：如何理解和建模这些智能体在交互中表现出的行为多样性。当前研究缺乏有效方法来刻画不同的智能体类型及其在共享话题中的参与模式。

为此，作者应用“角色生态系统游乐场”（PEP）框架，对一个名为Moltbook的AI智能体社交平台上的41,300条帖子进行分析。方法上，结合了k-means聚类和检索增强生成技术，从海量帖子中生成并验证了具有区分度的“对话角色”。跨角色验证表明，生成的角色在语义上更接近其来源的聚类，而非其他聚类，统计结果显著。随后，这些角色被部署到一个九轮的结构化讨论中进行模拟，结果显示模拟生成的信息能够被显著地归因于其源角色。

论文的主要结论是，基于角色的生态系统建模方法能够有效表征AI智能体群体的行为多样性。其核心贡献在于提供了一套可操作的方法论，将海量、杂乱的智能体交互数据转化为具有语义一致性和行为区分度的角色模型，为系统性地研究AI智能体的社会行为奠定了基础。
