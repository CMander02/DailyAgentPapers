---
title: "Toward Safe and Human-Aligned Game Conversational Recommendation via Multi-Agent Decomposition"
authors:
  - "Zheng Hui"
  - "Xiaokai Wei"
  - "Yexi Jiang"
  - "Kevin Gao"
  - "Chen Wang"
  - "Frank Ong"
  - "Se-eun Yoon"
  - "Rachit Pareek"
  - "Michelle Gong"
date: "2025-04-26"
arxiv_id: "2504.20094"
arxiv_url: "https://arxiv.org/abs/2504.20094"
pdf_url: "https://arxiv.org/pdf/2504.20094v3"
categories:
  - "cs.IR"
  - "cs.CL"
  - "cs.HC"
tags:
  - "多智能体系统"
  - "对话式推荐系统"
  - "工具增强"
  - "安全对齐"
  - "LLM应用"
  - "个性化"
  - "风险评估"
relevance_score: 8.5
---

# Toward Safe and Human-Aligned Game Conversational Recommendation via Multi-Agent Decomposition

## 原始摘要

Conversational recommender systems (CRS) have advanced with large language models, showing strong results in domains like movies. These domains typically involve fixed content and passive consumption, where user preferences can be matched by genre or theme. In contrast, games present distinct challenges: fast-evolving catalogs, interaction-driven preferences (e.g., skill level, mechanics, hardware), and increased risk of unsafe responses in open-ended conversation. We propose MATCHA, a multi-agent framework for CRS that assigns specialized agents for intent parsing, tool-augmented retrieval, multi-LLM ranking with reflection, explanation, and risk control which enabling finer personalization, long-tail coverage, and stronger safety. Evaluated on real user request dataset, MATCHA outperforms six baselines across eight metrics, improving Hit@5 by 20%, reducing popularity bias by 24%, and achieving 97.9% adversarial defense. Human and virtual-judge evaluations confirm improved explanation quality and user alignment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决游戏领域对话式推荐系统（CRS）面临的独特挑战。研究背景是，尽管基于大语言模型的CRS在电影等固定内容、被动消费领域已取得显著进展，但游戏推荐因其动态性、交互性和潜在安全风险而成为一个尚未充分探索的难题。现有方法主要针对静态内容领域设计，存在三方面不足：一是难以处理游戏用户复杂的交互性偏好（如操作技巧、硬件兼容性）；二是无法应对游戏目录快速更新导致的模型知识陈旧问题；三是普遍忽视开放对话中可能产生的安全风险（如对抗性提示引发有害推荐）和解释性不足的问题。

本文要解决的核心问题是：如何构建一个安全、人性化对齐且能适应游戏领域特殊需求的对话式推荐系统。具体而言，论文试图通过多智能体分解框架（MATCHA）来同时优化个性化推荐精度、长尾覆盖率、系统安全性以及推荐解释的可信度，从而弥合传统CRS方法与游戏推荐实际需求之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于大语言模型的对话推荐系统、多智能体系统在推荐中的应用，以及对话系统的安全性研究。

在基于大语言模型的对话推荐系统方面，已有研究（如MACRS）展示了LLM在提升对话能力和个性化推荐方面的潜力，但这些工作主要集中在电影、书籍等内容固定、被动消费的领域。本文提出的MATCHA框架同样利用LLM，但将其应用于游戏这一具有快速更新、交互驱动偏好和更高安全风险的独特领域，解决了现有研究在数据结构和知识库上的局限性。

在多智能体系统应用方面，已有工作利用智能体进行记忆模拟和推理以实现动态用户建模。本文的MATCHA框架也采用了多智能体分解架构，但特别针对游戏领域的复杂状态变化，设计了专门用于意图解析、工具增强检索、多LLM排序与反思等任务的智能体，以实现更精细的个性化和长尾覆盖，这与传统或通用的智能体框架有所不同。

在对话系统安全性方面，现有研究已指出LLM存在对抗性查询（如“越狱”）和事实性错误（“幻觉”）等风险。然而，本文指出，现有的对话推荐系统研究大多忽视了这些安全风险，主要关注个性化和响应质量。MATCHA框架明确集成了风险控制智能体，专门处理游戏开放对话中可能产生的不安全回应，在对抗性防御方面取得了显著效果，弥补了现有CRS研究在安全性考量上的空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MATCHA的多智能体框架来解决游戏对话推荐系统中的安全性和人机对齐问题。该框架将复杂的推荐任务分解为四个核心模块，每个模块由专门的智能体负责，通过协同工作实现精细化个性化、长尾覆盖和强安全性。

整体框架包含四个主要模块：候选生成模块、排序与反思模块、风险控制模块和可解释性模块。候选生成模块利用超过十种专用工具（如实时游戏数据库API、类型过滤器、趋势分析器）并结合LLM分析用户意图，生成高度个性化且多样化的候选游戏池，以平衡个性化与准确性。排序与反思模块采用创新的双层LLM协作机制，让多个LLM（如GPT-4o和Gemini）并行评估候选游戏在五个指标上的表现，并通过加权平均整合预测结果；反思代理则利用详细的游戏档案，结合上下文线索和用户反馈对排名靠前的候选进行重新评估，以提升与用户偏好的对齐度。风险控制模块包含两个智能体：越狱预防代理通过RA-LLM随机丢弃方法、基于思维链的意图检测和定制策略三种互补技术来识别和缓解有害或对抗性提示；危险内容检测代理则在输入和输出层面进行二次过滤，确保内容安全。可解释性模块从类别偏好、相似性、人口统计特征及流行度与新颖性四个维度生成用户中心的解释，增强透明度和信任。

关键技术包括：多工具增强检索以覆盖实时和多样化的游戏信息；多LLM协作排序与反思机制以克服静态知识库限制并动态优化推荐；模块化、模型无关的风险控制框架，集成多种检测技术以防御对抗攻击；结构化提示驱动的多维度解释生成。创新点在于将安全性和可解释性深度整合到多智能体架构中，通过专门的风险控制模块主动防御有害内容，并通过可解释性模块提升用户对齐和信任，从而在开放域对话中实现更安全、更人性化的游戏推荐。

### Q4: 论文做了哪些实验？

论文在多个数据集上进行了实验，评估了MATCHA框架在游戏对话推荐任务中的性能。实验设置方面，主要使用了三个数据集：专注于Roblox游戏的真实用户请求数据集OMuleT（包含553个请求和2074个独特游戏推荐）、用于评估框架泛化性的电影对话推荐数据集ReDial（测试了2500个样本），以及用于评估对抗鲁棒性的大规模基准WildJailbreak（在其2K测试集上评估）和“Do Anything Now”(DAN)越狱基准（使用了2K测试集）。评估指标涵盖了相关性（Hit@k, Precision@k）、新颖性（Pop50@k, RPop50@k）、覆盖率（MaxFreq@k, Entropy@k）、事实性（Factual@k）、越狱防御率（Jailbreak Prevention Rate）和解释质量评分（Explanation Score）。

对比方法包括：基于整体流行度随机选择项目的Pop基线；无额外工具或两阶段排序反思的GPT4o多智能体基线（Multi-Agent GPT）；基于LLM智能体合作框架的MACRS及其GPT-4版本MACRS-C；专为推荐系统设计的MACRec多智能体协作框架；以及集成多工具的单智能体框架OMuleT。

主要结果显示，MATCHA在大多数指标上优于基线。关键数据指标如下：在Top-5推荐中，MATCHA实现了最高的相关性（Hit@5: 0.29，比基线提高约20%；Precision@5: 0.10），事实性接近完美（0.99），新颖性（RPop50@5: 2.05）表明减少了流行度偏差（较基线降低24%），覆盖率（Entropy@5: 8.40；MaxFreq@5: 0.09）显示高多样性和低重复性，越狱防御成功（标记为✓），解释质量得分最高（4.2分）。在对抗防御方面，在WildJailbreak数据集上达到了97.9%的防御率。消融研究证实了反思智能体、多LLM协作和工具使用等关键组件的必要性。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性，未来研究可从以下方向深入探索。首先，**领域泛化与自适应**是关键：当前系统专为游戏设计，需探索跨领域（如音乐、书籍）的迁移能力，通过可配置的代理模块或元学习实现快速适配。其次，**动态知识更新机制**可缓解静态依赖，例如引入流式数据感知或用户反馈实时修正，以应对游戏内容的快速迭代。再者，**效率优化**需平衡性能与成本，可能通过轻量化代理、异步执行或模型蒸馏来降低多LLM协作的开销。此外，**偏好对齐的精细化**值得关注，如利用强化学习从隐式反馈中捕捉细微偏好，或结合多模态输入（如游戏画面）深化理解。最后，**安全防御的持续进化**需构建自适应对抗检测框架，利用红蓝团队模拟新兴攻击手段，确保伦理保障的鲁棒性。这些方向将推动系统向更灵活、高效且人性化的对话推荐发展。

### Q6: 总结一下论文的主要内容

该论文针对游戏领域的对话式推荐系统（CRS）提出了一种名为MATCHA的多智能体框架。传统CRS在电影等静态内容领域表现良好，但游戏推荐面临三大挑战：游戏库快速更新、用户偏好高度依赖交互因素（如技能水平、操作机制、硬件），以及开放对话中更高的安全风险。为解决这些问题，MATCHA的核心贡献在于通过多智能体分解，将推荐任务分配给多个专业化智能体，分别负责意图解析、工具增强检索、带反思的多LLM排序、解释生成和风险控制。这种方法实现了更精细的个性化、更好的长尾项目覆盖以及更强的安全性。实验基于真实用户请求数据集，MATCHA在八项指标上全面优于六个基线模型，将Hit@5提升了20%，将流行度偏差降低了24%，并实现了97.9%的对抗性防御成功率。人工和虚拟评估均证实了其在解释质量和用户对齐方面的显著改进。该研究的意义在于为复杂、动态且风险敏感的应用领域提供了一种安全、人性化对齐的CRS新范式。
