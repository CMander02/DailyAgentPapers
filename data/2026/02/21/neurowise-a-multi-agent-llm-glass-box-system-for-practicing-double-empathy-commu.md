---
title: "NeuroWise: A Multi-Agent LLM \"Glass-Box\" System for Practicing Double-Empathy Communication with Autistic Partners"
authors:
  - "Albert Tang"
  - "Yifan Mo"
  - "Jie Li"
  - "Yue Su"
  - "Mengyuan Zhang"
  - "Sander L. Koole"
  - "Koen Hindriks"
  - "Jiahuan Pei"
date: "2026-02-21"
arxiv_id: "2602.18962"
arxiv_url: "https://arxiv.org/abs/2602.18962"
pdf_url: "https://arxiv.org/pdf/2602.18962v1"
categories:
  - "cs.HC"
  - "cs.AI"
  - "cs.CY"
  - "cs.IR"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "LLM应用"
  - "人机交互"
  - "社会智能体"
  - "AI辅助沟通"
  - "心理健康"
relevance_score: 7.5
---

# NeuroWise: A Multi-Agent LLM "Glass-Box" System for Practicing Double-Empathy Communication with Autistic Partners

## 原始摘要

The double empathy problem frames communication difficulties between neurodivergent and neurotypical individuals as arising from mutual misunderstanding, yet most interventions focus on autistic individuals. We present NeuroWise, a multi-agent LLM-based coaching system that supports neurotypical users through stress visualization, interpretation of internal experiences, and contextual guidance. In a between-subjects study (N=30), NeuroWise was rated as helpful by all participants and showed a significant condition-time effect on deficit-based attributions (p=0.02): NeuroWise users reduced deficit framing, while baseline users shifted toward blaming autistic "deficits" after difficult interactions. NeuroWise users also completed conversations more efficiently (37% fewer turns, p=0.03). These findings suggest that AI-based interpretation can support attributional change by helping users recognize communication challenges as mutual.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决神经典型个体（neurotypical）与自闭症谱系个体（neurodivergent）沟通中存在的“双重同理心问题”。传统干预措施大多单向地训练自闭症个体适应神经典型规范，而忽视了支持神经典型个体去理解自闭症伙伴的视角并调整自身沟通方式。论文指出，沟通障碍源于双向的认知与风格差异，但神经典型个体往往难以解读自闭症沟通线索，容易将沟通困难归咎于对方的“缺陷”，从而可能导致无效甚至有害的互动。

为此，研究者提出了NeuroWise系统，这是一个基于多智能体大语言模型的AI辅导系统。它旨在为神经典型用户提供一个实践环境，核心目标不是单纯训练回应技巧，而是帮助用户在决定如何回应前，先理解自闭症伙伴可能的内心体验和压力源。系统通过压力可视化、内部体验解释和情境化沟通建议三大功能，引导用户将沟通挑战视为双向误解而非单方缺陷。

论文通过实证研究（N=30）具体探讨了三个问题：AI解释能否防止用户在经历困难沟通后回归对自闭症的“缺陷”归因；用户如何接受这种AI支持的辅导；以及这些功能是否能提升模拟沟通的效率。研究发现，NeuroWise能有效帮助用户减少缺陷归因，并更高效地完成对话，从而为支持“双重同理心”的实践工具提供了新的设计路径和证据。

### Q2: 有哪些相关研究？

相关研究主要分为两大方向：一是关于自闭症沟通与双重共情问题的心理学与社会科学研究，二是基于大语言模型（LLM）的社交模拟与辅导系统。

在自闭症沟通领域，早期研究（如APA, 2013）将沟通困难归因于自闭症个体的社交缺陷，这种“缺陷框架”强化了污名化（Botha, 2022）。Milton（2012）提出的“双重共情问题”对此进行了关键重构，指出困难源于神经典型与神经分化个体间沟通风格的双向不匹配，后续实证研究（如Crompton, 2020; Heasman, 2019）支持了这一观点。然而，现有干预措施（Kapp, 2019）大多仍聚焦于训练自闭症个体，缺乏对神经典型伴侣的支持。本文的NeuroWise系统直接针对这一研究空白，旨在帮助神经典型用户理解并适应双向不匹配。

在LLM应用领域，相关研究包括用于模拟人类行为的“生成智能体”（Park, 2023）以及用于谈判等场景的培训系统（Xia, 2025）。同时，LLM辅导系统（借鉴Hattie, 2007等反馈研究）侧重于改善用户的言行。但现有系统大多将沟通问题视为执行或技能问题，忽视了帮助用户进行“情境理解”的阐释维度。先前HCI研究（如Liao, 2020）表明，澄清意图和背景的解释能支持用户的意义建构，从而改变归因。此外，针对自闭症沟通的AI工具（如Parsons, 2002的虚拟环境到近期LLM系统Cao, 2025; Wang, 2024）也主要服务于自闭症个体的行为训练。本文的NeuroWise系统与这些工作的关系是：它整合了社交模拟（与生成智能体相关）和即时辅导，但其创新核心在于引入了“阐释者”组件，专注于帮助用户理解伙伴的内在体验，从而将辅导重点从行为纠正转向基于理解的双向沟通实践，填补了LLM在沟通阐释维度和支持神经典型用户方面的空白。

### Q3: 论文如何解决这个问题？

NeuroWise通过一个基于多智能体LLM的“玻璃盒”系统来解决双共情沟通中的归因偏差问题。其核心架构是一个由三个专门化智能体组成的处理管道，协同工作以可视化压力、解释内部体验并提供情境化指导。

系统首先通过**压力估计器**智能体对用户的每条消息进行实时分析。该智能体使用GPT-4o-mini模型，将用户输入分类为验证、无效化、施压、提供选项或感官调节等沟通模式，并基于预定义的规则库（如无效化消息会大幅增加压力）动态计算并更新模拟自闭症伙伴“Alex”的压力水平。这一过程的结果通过一个**压力条**直观呈现给用户，使其能够即时感知自身沟通方式对对方情绪状态的影响，这是实现归因改变的第一步。

当检测到压力显著上升时，系统会触发另外两个智能体。**解释器**智能体负责“打开黑箱”，向用户阐明Alex此刻可能的内在认知与感官体验（例如，“突然改变计划可能让Alex感到焦虑，因为他对可预测的常规有强烈需求”），将通常不可见的神经多样性个体的内部状态转化为可理解的语言。紧接着，**教练**智能体会提供具体、情境化的回应建议，引导用户采取验证情感、提供选择或进行感官调节等支持性策略，而非施加压力。

这种设计的关键在于，它没有试图“修复”自闭症方的沟通，而是通过多智能体协作，将互动的动态过程（压力变化）、对方的内部状态（解释）以及建设性的行动路径（指导）同时、透明地呈现给神经典型用户。在技术实现上，系统采用混合方法：LLM负责复杂的意图分类与自然语言生成，而规则引擎则确保压力更新的透明性与可预测性。该架构使神经典型用户能够直观理解沟通障碍是双向的（源于相互误解），从而将归因从指责对方的“缺陷”转向认识到情境的相互性，最终促进了更高效、更具共情的对话。

### Q4: 论文做了哪些实验？

该研究采用了一项被试间实验设计，共招募30名神经典型（neurotypical）参与者，将其随机分为NeuroWise实验组和基线对照组。实验设置中，所有参与者均与模拟的自闭症伙伴进行多轮文本对话，以应对具有挑战性的社交场景（如误解、计划变更）。NeuroWise组使用具备“玻璃盒”特性的多智能体LLM系统，该系统集成了压力可视化条（Stress Bar）、内部状态解释器（Interpreter）和情境化指导教练（Coach）三个核心功能；而基线组仅使用标准的聊天界面，无任何辅助功能。

研究通过三项基准测试评估系统效果：首先，针对RQ1（预防缺陷归因），使用包含两个反向计分题项的复合量表（α=0.84）测量参与者在对话前后对“沟通问题主要源于自闭症伙伴缺陷”这一归因态度的变化。其次，针对RQ2（用户接受度），通过7点李克特量表评估NeuroWise各组件的感知有用性，并收集开放式反馈进行主题分析。最后，针对RQ3（沟通效率），直接统计完成对话所需的消息轮次（turns）作为客观指标。

主要结果显示：在缺陷归因方面，NeuroWise组参与者的缺陷归因评分显著降低（均值变化-0.63），而基线组则出现上升（+0.30），条件×时间交互作用显著（p=0.02，效应量大），表明系统能有效帮助用户将沟通挑战理解为双向问题而非单方缺陷。在用户接受度上，NeuroWise所有功能均获高评分（整体帮助度6.60/7），解释器被评为最有帮助（6.27/7）。在沟通效率上，NeuroWise组完成对话所需轮次中位数显著少于基线组（8轮 vs 11轮，p=0.03），且最终沟通结果（压力水平）无显著差异，证明系统在提升效率的同时未牺牲沟通质量。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于研究场景单一（仅聚焦日常惯例被打乱的情境）、实验环境为模拟对话而非真实互动，且仅测量了即时效果，因此结论的泛化性和长期影响尚不明确。

未来可进一步探索的方向包括：1）**纵向与迁移研究**：检验归因改变的效应是否能长期保持，并迁移到与真实自闭症伙伴的日常沟通中；2）**系统设计的深化与扩展**：邀请自闭症群体共同参与设计与评估，确保解释符合真实体验；个性化设计伙伴智能体以反映自闭谱系的多样性（如沟通模式、感官敏感度等）；开发**双向支持工具**，帮助双方相互理解，更贴合双重共情原则；3）**机制与个体差异探究**：研究压力触发的具体机制、可观察行为与主观评分间的关联，以及参与者先前对自闭症的熟悉度等个体差异的影响。

### Q6: 总结一下论文的主要内容

这篇论文提出了NeuroWise，一个基于多智能体大语言模型的“玻璃盒”教练系统，旨在帮助神经典型人士（neurotypical）与自闭症伙伴进行更具双同理心的沟通。其核心贡献在于，它没有遵循传统干预措施仅聚焦于自闭症个体的思路，而是通过AI赋能，主动支持神经典型用户。系统通过压力可视化、内部体验解读和情境引导，帮助用户理解沟通挑战是双向的（即“双同理心问题”），而非单方面的缺陷。

研究通过对比实验（N=30）验证了其有效性：所有参与者都认为NeuroWise有帮助。关键发现是，NeuroWise能显著防止用户回归到基于缺陷的归因模式，而基线用户则在困难互动后更倾向于指责自闭症伙伴的“缺陷”。此外，NeuroWise用户完成对话的效率更高（对话轮次减少37%）。

这项工作的意义在于，它首次实证表明，基于AI的解读中介能够促进归因改变，为解决持续存在的双同理心鸿沟提供了一种有前景的技术途径，将沟通困难重新定义为相互的误解，从而推动更平等、有效的社会互动。
