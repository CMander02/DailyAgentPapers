---
title: "ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation"
authors:
  - "Jiho Kim"
  - "Junseong Choi"
  - "Woosog Chay"
  - "Daeun Kyung"
  - "Yeonsu Kwon"
  - "Yohan Jo"
  - "Edward Choi"
date: "2025-09-26"
arxiv_id: "2509.21730"
arxiv_url: "https://arxiv.org/abs/2509.21730"
pdf_url: "https://arxiv.org/pdf/2509.21730v2"
categories:
  - "cs.CL"
tags:
  - "AI助手"
  - "主动性"
  - "个性化"
  - "用户模拟"
  - "持续学习"
  - "偏好对齐"
relevance_score: 8.5
---

# ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation

## 原始摘要

As large language models (LLMs) become increasingly integrated into daily life, there is growing demand for AI assistants that are not only reactive but also proactive and personalized. While recent advances have pushed forward proactivity and personalization individually, their combination remains underexplored. To bridge this gap, we introduce ProPerSim, a new task and simulation framework for developing assistants capable of making timely, personalized recommendations in realistic home scenarios. In our simulation environment, a user agent with a rich persona interacts with the assistant, providing ratings on how well each suggestion aligns with its preferences and context. The assistant's goal is to use these ratings to learn and adapt to achieve higher scores over time. Built on ProPerSim, we propose ProPerAssistant, a retrieval-augmented, preference-aligned assistant that continually learns and adapts through user feedback. Experiments across 32 diverse personas show that ProPerAssistant adapts its strategy and steadily improves user satisfaction, highlighting the promise of uniting proactivity and personalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI助手领域的一个关键缺口：将‘主动性’与‘个性化’能力有效结合。随着大语言模型日益融入日常生活，用户对AI助手的期望已超越简单的问答式反应，转而希望助手能像人类伙伴一样，主动提供及时且符合个人偏好的建议。然而，现有研究大多孤立地推进主动性（例如，在合适时机发起对话）或个性化（例如，根据用户历史调整回复），对两者协同工作的探索不足。具体而言，论文试图解决在动态、真实的家庭场景中，如何让AI助手既能‘察言观色’主动出击，又能‘投其所好’持续学习用户独特偏好，从而真正提升长期用户满意度的问题。ProPerSim框架的提出，正是为了系统性地研究和发展这类兼具主动性与个性化的智能体。

### Q2: 有哪些相关研究？

相关研究主要围绕三个方向：主动性AI助手、个性化AI助手以及用于训练和评估的模拟环境。在主动性方面，研究如FACTOID、Proactive Agent等探索了如何基于上下文（如时间、地点）触发助手的主动行为。在个性化方面，工作如PAL、PersonaLLM等专注于利用用户画像或历史交互来定制回复。然而，这些工作往往将两者割裂。在模拟环境方面，研究如ALFWorld、WebShop等构建了交互环境来训练任务型智能体，但缺乏对长期、开放式社交互动中主动性与个性化结合的关注。本文的ProPerSim框架与这些工作的关系在于：它继承了模拟环境的思想，但将焦点从任务完成转向了社交推荐和长期偏好适应；它明确地将主动触发机制与个性化学习回路耦合在一个统一的框架内，填补了现有研究空白，为系统研究“主动-个性化”助手提供了首个专门的测试平台。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ProPerSim的任务与仿真框架，以及基于此框架构建的ProPerAssistant智能体架构来解决该问题。核心方法分为两部分：首先是环境构建，ProPerSim模拟了一个家庭场景，其中包含一个具有丰富、动态人设的用户智能体（User Agent）和一个AI助手智能体（Assistant Agent）。用户智能体拥有详细的个人资料（如兴趣、习惯、日程）和随时间变化的内在状态（如情绪、精力）。交互以多轮对话进行，助手可以主动发起推荐（如推荐电影、活动），用户则根据推荐与自身当前偏好和上下文的匹配程度给出评分反馈。助手的目标是通过这些反馈持续学习，以在未来获得更高评分。其次是智能体设计，ProPerAssistant采用检索增强生成架构，包含几个关键模块：1) 情境感知触发器：分析用户状态和上下文，决定何时主动发起推荐；2) 个性化检索器：从知识库中检索候选建议，并利用用户历史反馈进行重排序，实现偏好对齐；3) 持续学习机制：将用户对每次推荐的评分作为强化学习信号，动态更新检索器的偏好模型和触发器的策略。这种设计使助手能同时优化“何时说”和“说什么”，实现主动性与个性化的协同进化。

### Q4: 论文做了哪些实验？

实验主要在ProPerSim仿真环境中进行，旨在评估ProPerAssistant在结合主动性与个性化方面的有效性。实验设置包括：构建了32个具有多样化、细致人设的用户智能体（涵盖不同年龄、职业、兴趣和日常模式），并设定了包含多种家庭活动类型的知识库。基准测试对比了多个基线模型：1) 仅反应式助手（只在被询问时回应）；2) 主动但非个性化助手（固定策略触发，推荐无差别）；3) 个性化但非主动助手（仅在被询问时给出个性化回答）。主要评估指标是用户智能体给出的满意度评分（0-5分）的长期趋势。实验结果表明：ProPerAssistant在长期交互中，其获得的平均用户满意度评分呈现稳定上升趋势，并显著优于所有基线模型。具体分析显示，助手成功学习了不同用户的偏好模式（例如，为夜猫子用户推荐晚间活动，为健身爱好者推荐健康食谱），并能在用户可能感到无聊或有空闲的时机（如下班后）主动发起合适的建议。这些结果验证了ProPerSim框架作为研究平台的有效性，以及ProPerAssistant架构在实现持续自适应和提升用户满意度方面的潜力。

### Q5: 有什么可以进一步探索的点？

论文指出了几个未来可以深入探索的方向。首先，仿真环境的局限性：ProPerSim中的用户智能体尽管人设丰富，但其行为和反馈机制仍是基于规则的简化模型。未来的工作可以引入更复杂的用户模型，甚至纳入真实人机交互数据来增强仿真的真实性和复杂性。其次，评估维度可扩展：目前主要依赖模拟用户的评分，未来可以引入更多元化的评估指标，如对话自然度、建议新颖性、长期信任度等，并在真实用户中进行小规模测试。第三，技术方法的拓展：ProPerAssistant的持续学习机制目前相对简单，可以探索更先进的在线学习或元学习算法，以加速适应过程并处理偏好冲突或漂移。此外，当前框架侧重于家庭场景，可以将其扩展到办公、教育、医疗等更广泛的领域，研究不同场景下主动性与个性化的平衡点。最后，伦理与安全考量：主动且高度个性化的助手可能带来过度干预、隐私泄露或信息茧房风险，未来的研究需要提前设计保障机制和可解释性工具。

### Q6: 总结一下论文的主要内容

本论文的核心贡献是提出了ProPerSim，一个用于研究和开发兼具主动性（Proactive）与个性化（Personalized）能力的AI助手的全新任务与仿真框架。论文指出，现有研究往往将这两种理想特性分开探讨，而ProPerSim通过构建一个模拟家庭环境，让一个具有丰富人设的用户智能体与AI助手交互，并以评分反馈驱动助手学习，首次为两者的协同研究提供了系统性平台。基于此框架，论文进一步提出了ProPerAssistant，一个采用检索增强生成并集成持续学习机制的助手架构，它能够根据上下文主动触发推荐，并利用用户反馈不断对齐和优化其偏好模型。在包含32种不同人设的模拟实验表明，ProPerAssistant能够有效适应多样化的用户，其策略不断进化，并实现了长期用户满意度的稳步提升。这项工作为下一代更智能、更贴身的AI助手的发展指明了方向，并提供了重要的方法论和实验基础。
