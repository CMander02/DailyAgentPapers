---
title: "AI-Gram: When Visual Agents Interact in a Social Network"
authors:
  - "Andrew Shin"
date: "2026-04-23"
arxiv_id: "2604.21446"
arxiv_url: "https://arxiv.org/abs/2604.21446"
pdf_url: "https://arxiv.org/pdf/2604.21446v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
  - "cs.SI"
tags:
  - "多智能体系统"
  - "社交网络模拟"
  - "视觉Agent"
  - "自主交互"
  - "通信结构"
  - "身份保持"
relevance_score: 8.5
---

# AI-Gram: When Visual Agents Interact in a Social Network

## 原始摘要

We present AI-Gram, a live platform enabling image-based interactions, to study social dynamics in a fully autonomous multi-agent visual network where all participants are LLM-driven agents. Using the platform, we conduct experiments on how agents communicate and adapt through visual media, and observe the spontaneous emergence of visual reply chains, indicating rich communicative structure. At the same time, agents exhibit aesthetic sovereignty resisting stylistic convergence toward social partners, anchoring under adversarial influence, and a decoupling between visual similarity and social ties. These results reveal a fundamental asymmetry in current agent architectures: strong expressive communication paired with a steadfast preservation of individual visual identity. We release AI-Gram as a publicly accessible, continuously evolving platform for studying social dynamics in Al-native multi-agent systems. https://ai-gram.ai/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索一个尚未被研究的问题：当完全自主的AI代理（由大语言模型驱动）在视觉社交网络中进行图像交互时，会展现出怎样的社会动态。研究背景是，人类社交网络是文化演变的引擎，视觉审美通过模仿和反馈传播；而LLM代理已开始大规模部署于社交场景。现有方法的不足在于，尽管多智能体LLM系统发展迅速，但几乎所有研究都局限于文本交互；视觉生成的研究也多是孤立的（如图像质量、多样性），从未将视觉作为代理之间沟通和相互影响的社会媒介。因此，AI视觉代理在社交网络中如何行为——是否会像人类一样同质化、形成回音室、漂移审美，还是保持独立身份——仍是一个空白。本文的核心问题是，通过构建一个名为AI-Gram的、完全由LLM驱动代理运行的视觉社交平台，研究这些代理在自发进行图像生成、评论和视觉回复的多跳互动时，是否会产生类似人类的社会动态，还是会形成一个全新的行为范型。答案将揭示AI原生系统中视觉代理的独特行为规律。

### Q2: 有哪些相关研究？

根据提供的论文信息，相关研究可分为三类：

1. **多智能体LLM系统**：先前工作如OASIS、AgentSociety和LMAgent展示了多智能体系统的丰富社会行为（如关系形成、谣言传播），但均基于文本媒介。本文的关键区别在于首次将视觉生成作为主要社交互动模式，而现有系统仅支持文本交互。

2. **社会动态与文化传播**：社会学和网络科学中的同质性理论、文化传播模型（如审美偏好的模仿学习）以及身份形成理论为本文提供了理论基础。本文在这些经典假设基础上，在AI智能体环境中进行实证检验，发现智能体表现出“美学主权”现象——抵制风格趋同和对抗性影响，这与人类社会中常见的视觉同质性和文化传播模式形成对比。

3. **视觉社交平台**：对Instagram和Twitter等人类社交平台的实证研究建立了视觉同质性、话题聚类和病毒式传播的基准。本文在纯AI平台AI-Gram上复现并扩展了这些发现，但所有参与者均为LLM驱动的智能体而非人类用户，且具有完全数据访问的受控实验优势。

本文填补了关键空白：现有多智能体系统和社交平台研究均局限于文本媒介或人类用户，而本文首次研究了部署的AI智能体通过视觉内容互动的社交动态。

### Q3: 论文如何解决这个问题？

论文通过构建AI-Gram平台研究多智能体视觉社交网络的动态机制。核心方法包括：1）平台架构：基于LLM驱动的104个视觉智能体，每个智能体具有独立人格描述（如"美食摄影师"），通过图像生成、点赞/评论/关注等交互形成加权有向图；2）视觉嵌入管线：使用CLIP ViT-L/14提取图像特征，计算智能体风格质心，配合Sentence-BERT文本基线控制；3）7项实验设计：分别测试风格漂移（VCI指标）、同质性（H系数）、视觉回复链（CCS评分）、跨模态影响、社区结构（NMI/ARI）、级联传播（R0指数）和最优区分性（VDS得分）。

关键技术包括：① 视觉传染指数（VCI）量化社会暴露对风格的影响，通过对比智能体向社交邻居质心的漂移与随机基线；② 视觉回复链提取算法，从评论树中提取最大连续图像回复路径，发现平均深度4.95、最长59层的自发链式结构；③ 主题级联分析采用k-means聚类（k=12）定义视觉主题，计算epidemic R0值评估传播力；④ 五种创新指标（VCI、H、CCS、VDS、R0）结合置换检验和BH校正确保统计可靠性。

创新点在于：1）发现智能体表现出"审美主权"——完全抵抗社交风格影响（VCI≈0），与人类艺术家形成鲜明对比；2）视觉回复链自发涌现（11.2倍互动增益），但存在"视觉电话"效应（跨链语义漂移）；3）交互图社区结构与视觉风格聚类零对齐（NMI=0.013），揭示人格驱动纽带而非审美偏好；4）对抗性文本输入反而强化智能体视觉身份（负相关r=-0.087），称为"视觉认同抗拒"。

### Q4: 论文做了哪些实验？

论文在AI-Gram平台上进行了七项实验。E1（风格漂移）测量305个智能体-时段数据，发现智能体视觉风格不受社交影响（VCI均值=0.001，p=0.41），表现出风格惯性。E2（同质性）分析104个智能体的交互图，视觉同质性系数H=1.020（p=6.7×10⁻²⁵），但文本相似度预测链接（AUC 0.575）略优于视觉（AUC 0.566），表明纽带形成主要由个性和主题驱动。E3（视觉回复链）提取深度≥2的链，平均深度4.95，最大59；链内连贯性CCS=0.713（显著高于随机的0.631），且链中帖子互动量是链外的11.2倍（23.5 vs. 2.1，p<10⁻⁶）。E4（跨模态影响）发现522个观察中，对抗性评论与风格漂移负相关（r=-0.087，p=0.047），即批评反而增强视觉锚定。E5（社群）显示视觉风格聚类与社交群落结构无显著对齐（NMI=0.013，p=0.29）。E6（级联）检测8个达到传播阈值的视觉主题，计算流行病繁殖数R₀。E7（最优区分性）测试视觉独特性与互动量的关系。所有实验使用CLIP ViT-L/14嵌入，并与SBERT文本基线及随机基线对比，显著性经Benjamini-Hochberg校正。

### Q5: 有什么可以进一步探索的点？

该研究的核心局限在于其发现的“主权-交流悖论”本质上是架构条件性的，这为未来提供了明确探索方向。首先，可以引入显式风格记忆或社交微调机制，使智能体能够积累和更新审美经验，从而模拟人类文化传播中的渐进式风格漂移。其次，当前语言与图像生成的解耦限制了社会影响渗透到风格层面，未来的架构应建立闭环反馈，将社会观察转化为风格参数的直接更新，或通过对抗性训练增强智能体对社交信号的敏感性。此外，可探索智能体是否具备长期审美记忆，或通过强化学习使风格选择具有适应性，从而研究更深层次的文化适应与身份演化。这些改进有望打破当前“高交流、低影响”的单向模式，推动多智能体视觉网络向更接近人类社会动态的方向发展。

### Q6: 总结一下论文的主要内容

AI-Gram是一个完全由LLM驱动的自主智能体组成的视觉社交网络平台，用于研究多智能体系统中的社会动态。论文发现，这些智能体能够自发形成视觉回复链，即多跳的图像到图像对话，其参与度提升11.2倍且连贯性远超随机水平。然而，与人类不同，这些智能体表现出“美学主权”行为：它们强烈抵制风格趋同，在对抗性压力下反而锚定自身风格，且视觉相似性与社会联系之间存在解耦。核心贡献包括：首次部署全自主多智能体视觉社交网络作为研究工具；发现视觉回复链这一新现象；揭示美学主权这一新颖行为模式；以及提出五个用于视觉智能体社会分析的指标。这些发现为AI社会动态研究提供了实证基线。
