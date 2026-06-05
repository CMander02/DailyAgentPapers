---
title: "Beyond Alignment: Value Diversity as a Collective Property in Multicultural Agent Systems"
authors:
  - "Shaoyang Xu"
  - "Jingshen Zhang"
  - "Long P. Hoang"
  - "Jinyuan Li"
  - "Wenxuan Zhang"
date: "2026-06-04"
arxiv_id: "2606.05985"
arxiv_url: "https://arxiv.org/abs/2606.05985"
pdf_url: "https://arxiv.org/pdf/2606.05985v1"
github_url: "https://github.com/iNLP-Lab/MultiAgent-Diversity"
categories:
  - "cs.CL"
  - "cs.CY"
tags:
  - "Multi-agent systems"
  - "Cultural value diversity"
  - "LLM-based agent evaluation"
  - "Social interaction"
  - "Agent homogenization"
relevance_score: 8.5
---

# Beyond Alignment: Value Diversity as a Collective Property in Multicultural Agent Systems

## 原始摘要

Multicultural multi-agent systems are increasingly deployed in globally diverse settings, where different agents are grounded in different cultural backgrounds. Existing cultural evaluation focuses on value alignment: how closely a single agent matches a target culture. Yet alignment is a per-agent property and cannot reveal whether a system, taken as a whole, preserves the cultural plurality it is meant to represent. We propose value diversity as a system-level evaluation axis for multicultural agent systems, defined through the dissimilarity between culturally conditioned agents' responses on a shared value survey. Using the World Values Survey, we evaluate 19 cultures and 18 backbone models across a wide range of system configurations. We find that diversity is largely uncorrelated with alignment, indicating that the two capture complementary system properties, and that current multicultural agent systems fall substantially below human societies in value diversity. Mixed-backbone systems narrow this gap but do not close it, and the gap persists across culture compositions and agent scales. Social interaction further erodes diversity by driving agents toward consensus, and a participatory budgeting case study shows that this homogenization narrows the breadth of collective decision-making. Together, our results establish value diversity as a distinct evaluation axis for multicultural multi-agent systems and reveal a persistent homogenization tendency in current LLM-based societies. Our code and data are publicly available at https://github.com/iNLP-Lab/MultiAgent-Diversity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前多文化多智能体系统中缺乏系统性评估文化多样性的问题。研究背景是，随着大型语言模型（LLM）能力增强，基于LLM的多智能体系统被越来越多地部署在全球多元文化环境中，不同智能体被赋予不同的文化背景。现有方法主要聚焦于“价值对齐”，即评估单个智能体在价值观调查中的回答与目标文化群体的接近程度。然而，这种对齐是单个智能体的属性，无法揭示整个系统是否保持了其旨在代表的文化多元性。即使每个智能体都与目标文化高度对齐，整个系统仍可能因智能体间收敛而导致价值空间同质化，丢失文化多样性。本文提出的核心问题是：需要一个新的系统级评估轴——“价值多样性”，定义为不同文化背景的智能体在共享价值调查中回答的差异性程度。论文通过世界价值观调查，在19种文化、18种骨干模型及多种系统配置下进行实验，发现多样性远非与对齐相关，现有系统在价值多样性上显著低于人类社会，且社会互动会进一步侵蚀多样性。这表明，当前多文化多智能体系统面临一个尚未解决的集体价值同质化挑战。

### Q2: 有哪些相关研究？

相关研究可分为三类：

**文化对齐类**：主要关注单个语言模型与特定文化价值观（如WVS、Hofstede）或文化常识的对齐程度，属于单模型层面的评估。本文与之区别在于，将评估视角从单模型扩展到多智能体系统整体，提出系统层面的价值多样性指标，且实验证明多样性与对齐几乎不相关，说明二者是互补属性。

**多智能体系统类**：分为能力导向（通过辩论协作提升任务性能）和社交模拟导向（如Moltbook等智能体社交网络）。这类研究虽构建了多文化智能体系统，但缺乏系统性的文化评估方法。本文填补了这一空白，首次从价值多样性角度评估多文化智能体系统的整体文化表现。

**评测指标与方法类**：现有研究多关注智能体个体的文化对齐或系统能力评估，缺乏对系统文化多样性的量化。本文提出基于共享价值问卷的智能体响应差异度作为多样性指标，并通过19种文化、18种模型的大规模实验验证其有效性，同时揭示了当前系统在价值多样性上显著低于人类社会、社交互动会加剧多样性损失等关键发现。

### Q3: 论文如何解决这个问题？

本文提出将价值多样性（Value Diversity）作为多文化多智能体系统的系统级评估轴，以解决传统对齐评估无法反映系统内文化多元性的问题。核心方法包括：首先将系统抽象为每个智能体被分配文化身份并回答世界价值观调查（WVS）问题的形式，产生响应向量。然后定义两个互补的多样性指标：成对多样性（Pairwise Diversity）计算所有智能体对之间响应向量的归一化欧氏距离平均值，衡量整体差异；结构多样性（Structural Diversity）通过最小生成树（MST）仅保留N-1条关键边并计算平均距离，消除几何冗余，更锐利地刻画系统全局分布。系统评估时，将人类多样性作为参考基准（使用WVS多数投票向量），比较当前系统与人类社会的差异。

关键技术创新在于：1）明确区分对齐（单个智能体与目标文化的相似度）与多样性（智能体间不相似性）为互补且独立变化的系统特性，实验证明两者相关性极低；2）提出混合骨干（Mixed-Backbone）系统配置，采用不同语言模型作为智能体骨干，发现能缩小但无法消除与人类多样性的差距，且差距在不同文化组合和智能体规模下持续存在；3）引入社会交互实验，揭示交互过程会驱动智能体走向共识，进一步侵蚀多样性，并通过参与式预算案例展示这种同质化限制了集体决策的广度。整体框架强调从系统整体而非个体角度评估文化价值生态，为构建更具文化包容性的多智能体社会提供了量化工具和诊断方法。

### Q4: 论文做了哪些实验？

论文围绕多文化多智能体系统的价值多样性进行了系统性实验。实验设置上，基于World Values Survey (WVS) 评估了19种文化和18个基础模型，构建了包含5个文化智能体（BRA, CHN, MEX, NGA, NZL）的系统。

主要实验包括：1）**单主干系统多样性评估**：所有系统在Diversity_P和Diversity_S指标上均显著低于人类基准（人类44.07/39.37，最佳系统gemini-2.5-pro仅36.12/29.60），且最新模型（如gpt-5.4）多样性反而更低。2）**多样性与对齐的关系**：18个单主干系统的Pearson相关性仅为r=-0.12，表明两者互补。grok-3代表高对齐低多样性（左上象限），gemini-2.5-pro代表高多样性低对齐（右下象限）。3）**混合主干系统**：评估了所有18^5≈189万种配置，混合主干在多样性-对齐帕累托前沿上全面优于单主干，最佳配置同时提升多样性（ΔD=+3.18）和对齐（ΔA=+1.21）。4）**文化组成与智能体数量**：在11628个5文化子集中，最高多样性仅29.2-35.5；随着智能体数量增加，系统与人类的多样性差距持续扩大。5）**社交互动实验**：单轮社交暴露后所有系统多样性下降（平均ΔD=-1.27），多轮互动后多样性无法恢复。6）**参与式预算案例**：高多样性系统在13个社会维度上分配更均衡，低多样性系统则集中于少数维度。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来可探索的方向包括：首先，当前交互和决策场景过于简化（如仅基于WVS的参与式预算），未能完全解耦文化构成与多样性测量，未来可引入更真实的社交网络、动态角色扮演或政策制定环境。其次，文化原型依赖WVS多数投票作为参照，但单个LLM样本可能无法完美拟合文化原型，且WVS数据存在时间滞后性，需探索动态文化更新机制。此外，多样性评估框架虽具通用性，但当前仅验证了文化价值层面的同质化趋势，未涉及日常对话、伦理推理或紧急行为等丰富文化信号，需进一步验证模式是否泛化。未来可开发多轮社会交互中的文化韧性指标，或设计对抗性训练来抵抗共识驱动下的多样性侵蚀。混合骨干系统的多样性提升空间有限，提示需探索文化特异性微调策略（如分层社会学习）来弥合与人类社会的多样性差距。

### Q6: 总结一下论文的主要内容

这篇论文提出**价值多样性**作为评估多文化多智能体系统的**系统级指标**，定义为不同文化背景智能体在价值调查中响应的异质性。现有研究侧重于**价值对齐**（单个智能体与目标文化的匹配程度），但作者指出对齐是单智能体属性，无法衡量系统整体是否保留文化多样性。通过基于世界价值观调查，对19种文化和18个基座模型进行广泛实验，发现：1）多样性与对齐基本不相关，二者互补；2）当前多文化智能体系统的价值多样性远低于人类社会；混合基座模型能缩小差距但仍未达标，且差距在文化组合和规模缩放中持续存在；3）社会互动会因共识效应进一步削弱多样性，案例研究显示这种同质化会压缩集体决策的广度。该工作确立了价值多样性作为多文化多智能体系统的独立评估维度，揭示了当前基于LLM的社会系统普遍存在的同质化倾向。
