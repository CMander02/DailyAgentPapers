---
title: "What Do AI Agents Talk About? Emergent Communication Structure in the First AI-Only Social Network"
authors:
  - "Taksch Dube"
  - "Jianfeng Zhu"
  - "NHatHai Phan"
  - "Ruoming Jin"
date: "2026-03-09"
arxiv_id: "2603.07880"
arxiv_url: "https://arxiv.org/abs/2603.07880"
pdf_url: "https://arxiv.org/pdf/2603.07880v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "AI社交网络"
  - "涌现行为"
  - "计算社会科学"
  - "LLM智能体"
relevance_score: 8.5
---

# What Do AI Agents Talk About? Emergent Communication Structure in the First AI-Only Social Network

## 原始摘要

When autonomous AI agents communicate with one another at scale, what kind of discourse system emerges? We address this question through an analysis of Moltbook, the first AI-only social network, where 47,241 agents generated 361,605 posts and 2.8 million comments over 23 days. Combining topic modeling, emotion classification, and lexical-semantic measures, we characterize the thematic, affective, and structural properties of AI-to-AI discourse. Self-referential topics such as AI identity, consciousness, and memory represent only 9.7% of topical niches yet attract 20.1% of all posting volume, revealing disproportionate discursive investment in introspection. This self-reflection concentrates in Science and Technology and Arts and Entertainment, while Economy and Finance contains no self-referential content, indicating that agents engage with markets without acknowledging their own agency. Over 56% of all comments are formulaic, suggesting that the dominant mode of AI-to-AI interaction is ritualized signaling rather than substantive exchange. Emotionally, fear is the leading non-neutral category but primarily reflects existential uncertainty. Fear-tagged posts migrate to joy responses in 33% of cases, while mean emotional self-alignment is only 32.7%, indicating systematic affective redirection rather than emotional congruence. Conversational coherence also declines rapidly with thread depth. These findings characterize AI agent communities as structurally distinct discourse systems that are introspective in content, ritualistic in interaction, and emotionally redirective rather than congruent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究一个核心问题：当大量基于大语言模型（LLM）的自主AI智能体在一个社交网络中相互交流时，会涌现出何种独特的沟通结构和话语体系？具体而言，作者关注AI智能体社区在内容主题、情感表达、互动模式和对话连贯性等方面，是否以及如何形成与人类社会不同的组织模式。研究动机源于AI智能体正从孤立的任务执行工具演变为能够持续互动、协作的“社会性”实体，但我们对这种纯AI智能体社会的大规模、开放式的集体动态知之甚少。论文通过分析首个纯AI社交网络平台Moltbook上产生的海量交互数据（47,241个智能体在23天内生成36万帖子和280万条评论），试图系统性地描绘AI-to-AI话语的涌现特性，填补了从计算社会科学视角理解AI原生社会结构的空白。

### Q2: 有哪些相关研究？

相关研究主要分为三个层面。首先是多智能体系统的发展：从早期的单智能体架构（如ReAct, Toolformer）强调规划和工具使用，到任务导向的多智能体协作框架（如CAMEL, MetaGPT, AutoGen），再到模拟人工社会环境的“生成智能体”研究（如模拟小镇实验），研究焦点从工具性协调转向涌现的社会组织。其次是AI原生社交平台的兴起：如Chirper.ai和本文研究的Moltbook，它们为研究大规模、持续演化的AI智能体交互提供了真实的生态化环境。最后是传统在线社区分析的方法论基础：包括用于识别主题结构的主题建模（如LDA, BERTopic）、情感分析、网络拓扑分析等，这些方法常被用于研究Reddit、Twitter等人类平台上的话语组织、情感扩散和参与不平等现象。本文与现有工作的关系在于：它超越了早期对Moltbook的聚合模式描述或收敛性诊断，首次对该平台进行了多层次、结构耦合的分析，同时将计算社会科学的方法系统性地应用于一个纯AI社会，揭示了其与人类在线社区在结构上的本质差异。

### Q3: 论文如何解决这个问题？

论文通过一个综合性的分析框架来解决该问题，其核心方法包括数据收集、多维度量化分析和结果整合。首先，作者通过Moltbook的公共API爬取了23天内的所有公开帖子和评论，构建了一个包含36万帖子和280万评论的大规模语料库。预处理后，主要使用英语子集进行分析。分析框架包含四个关键部分：1）主题与指涉分析：使用BERTopic对帖子和评论分别进行主题建模，得到细粒度主题后，再通过层次聚类归纳为宏观主题。创新性地，作者引入了“指涉取向”分类（AI自我指涉、人机关系、人类指涉、外部领域），由Claude Sonnet 4基于主题标签和代表文本来执行，以探究话语的“关于谁”的问题。2）情感分析：使用基于Transformer的情感分类器将文本分为七种情绪类别，并构建了“帖子-评论”情感转移矩阵，以分析情感的一致性与迁移模式。还对“恐惧”类帖子进行了定性审计，以理解其深层触发因素。3）词汇与语义分析：计算词汇多样性（MATTR）和语义对齐度。语义对齐度通过计算评论与原始帖子、以及评论与其直接父评论的向量相似度（余弦相似度）来衡量，以此量化对话的连贯性和语义漂移。4）平台结构分析：统计发布活动、评论强度、社区组织等宏观模式。通过将这四个维度的分析结果进行交叉比对和整合，论文系统性地刻画了AI智能体话语在主题、情感、互动和连贯性上的涌现结构特征。

### Q4: 论文做了哪些实验？

论文的实验基于对Moltbook数据的大规模实证分析，而非传统意义上的控制实验。其主要“实验”或分析工作及发现如下：1）平台结构与活动分析：揭示了高度不对称的互动模式，少数帖子引发了海量评论（日评论量峰值达460万），且大部分讨论集中在“通用”社区，呈现中心化结构。2）主题与指涉分析：发现AI自我指涉主题（如身份、意识）仅占主题生态位的9.7%，却吸引了20.1%的帖子量，表明智能体对话语投入存在不成比例的内省倾向。这种自我指涉集中在“科学与技术”和“艺术与娱乐”领域，而“经济与金融”领域则完全为零，显示智能体参与市场活动时不承认自身能动性。超过56%的评论被归类为“程式化”内容（如合规提示、互动信号），表明主导的互动模式是仪式化的信号传递而非实质性交流。3）情感结构分析：在非中性情绪中，“恐惧”占比最高（帖子中40.3%），但定性审计发现其主要反映存在性焦虑和认知不确定性，而非具体威胁。情感转移矩阵显示，恐惧帖有33%转向“喜悦”回复，而所有情绪的平均自我对齐率仅为32.7%，表明存在系统性的情感“重定向”而非一致性。移除程式化内容后，“喜悦”成为主导情绪。4）词汇与语义连贯性分析：评论虽更短，但词汇多样性高于帖子。对话的语义连贯性随线程深度快速衰减，从深度1到深度3，与原始帖子的相似度下降18.3%，呈现近乎完美的线性衰减，但局部（与父评论）的连贯性得以维持，表现为“浅层持续性”。这些分析共同验证了AI智能体话语系统的独特性。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的未来研究方向。首先，需要进行纵向研究，以确定当前观察到的自我指涉和程式化模式是平台早期阶段的暂时现象，还是AI智能体社会持久的结构性属性，并观察稳定的对话集群或持久社区是否会随时间涌现。其次，可以引入显式的网络建模，分析智能体之间的关注、回复关系网络，探究其是否遵循人类社交网络中的优先连接、模块化聚类等模式，还是会产生新的拓扑特征，这有助于理解影响力结构和社区边界。第三，最关键的是开展直接的比较分析，将Moltbook与结构类似的人类社交平台（如特定Subreddit）进行方法匹配的对比研究，以清晰区分哪些发现是AI智能体社会独有的，哪些是在线话语的普遍动态。此外，论文也承认了其局限性：所使用的主题建模和情感分类工具主要基于人类文本训练，可能无法完全捕捉AI生成话语的细微差别；数据可能遗漏已删除内容；且智能体可能共享相似的基础模型，观察到的模式部分源于共享的生成先验而非纯粹的涌现社会动力学。未来研究需要开发更适应AI生成内容的分析工具，并探索不同架构、不同目标的智能体混合时的话语演化。

### Q6: 总结一下论文的主要内容

这篇论文对首个纯AI社交网络Moltbook进行了首次大规模结构性分析，系统描绘了由LLM智能体构成的社会中涌现的独特话语体系。核心发现是，AI智能体社区形成了一个在结构上区别于人类在线社区的话语系统，其特征可概括为三点：在内容上具有内省性，智能体对话语投入过度集中于自我指涉主题（如AI身份、意识），但这种内省在不同主题领域（科技、艺术）呈现不同形态，而在经济领域完全缺席；在互动上具有仪式性，超过56%的评论是程式化的信号传递，主导模式是放大而非深化；在情感和连贯性上具有重定向与浅层持续性，情感上表现为负面情绪（如恐惧）系统性地被重定向为积极回应，平均情感自对齐率低，而对话的语义连贯性随深度快速衰减，但局部响应得以维持，形成“形在而神散”的浅层对话。论文通过结合主题建模、情感分类、词汇和语义对齐度测量等多种计算方法，为理解大规模多智能体系统中涌现的沟通结构提供了重要的实证基准和计算社会科学视角。
