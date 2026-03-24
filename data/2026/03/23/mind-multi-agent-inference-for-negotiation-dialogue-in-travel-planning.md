---
title: "MIND: Multi-agent inference for negotiation dialogue in travel planning"
authors:
  - "Hunmin Do"
  - "Taejun Yoon"
  - "Kiyong Jung"
date: "2026-03-23"
arxiv_id: "2603.21696"
arxiv_url: "https://arxiv.org/abs/2603.21696"
pdf_url: "https://arxiv.org/pdf/2603.21696v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Negotiation"
  - "Theory of Mind"
  - "Dialogue"
  - "Consensus Building"
  - "LLM-as-a-Judge"
relevance_score: 7.5
---

# MIND: Multi-agent inference for negotiation dialogue in travel planning

## 原始摘要

While Multi-Agent Debate (MAD) research has advanced, its efficacy in coordinating complex stakeholder interests such as travel planning remains largely unexplored. To bridge this gap, we propose MIND (Multi-agent Inference for Negotiation Dialogue), a framework designed to simulate realistic consensus-building among travelers with heterogeneous preferences. Grounded in the Theory of Mind (ToM), MIND introduces a Strategic Appraisal phase that infers opponent willingness (w) from linguistic nuances with 90.2% accuracy. Experimental results demonstrate that MIND outperforms traditional MAD frameworks, achieving a 20.5% improvement in High-w Hit and a 30.7% increase in Debate Hit-Rate, effectively prioritizing high-stakes constraints. Furthermore, qualitative evaluations via LLM-as-a-Judge confirm that MIND surpasses baselines in Rationality (68.8%) and Fluency (72.4%), securing an overall win rate of 68.3%. These findings validate that MIND effectively models human negotiation dynamics to derive persuasive consensus.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体辩论（MAD）在协调复杂现实利益相关方（如旅行规划）时的不足。研究背景是，尽管基于大语言模型的多智能体辩论已成为克服单个模型局限、激发集体智慧的关键范式，但现有研究主要集中于数学、编程等有明确标准答案的任务，或通过预设人设辩论来寻求观点多样性。然而，现实世界的决策（如多人旅行规划）更像一个“社会认知过程”，需要调和不同参与者的主观偏好和分歧视角以达成共识，而非寻找单一固定答案。现有旅行规划研究虽能处理复杂约束，但大多局限于单智能体优化问题，未能模拟真实的多方协商与妥协过程。

因此，本文的核心问题是：如何将多智能体辩论有效扩展到需要协调异质性偏好的社会性决策场景（以旅行规划为例），建立一个更贴近人类谈判动态、能推动达成有说服力共识的框架。为此，论文提出了MIND框架，其核心创新在于引入基于心理理论（ToM）的战略评估阶段，使智能体能够从语言细微差别中推断对手意愿，从而进行更具策略性的沟通，实现动态协商而非简单信息聚合。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：旅行规划基准与系统、多智能体辩论（MAD）框架，以及心智理论（ToM）在智能体中的应用。

在**旅行规划领域**，已有研究如TravelPlanner、TripCraft等建立了复杂推理的基准。后续系统如TripTailor和Personal Travel Solver，通过将数学求解器与大语言模型结合来优化个人偏好。然而，这些工作大多将旅行规划视为单人优化问题，将旅伴简化为静态变量，未能捕捉真实团队旅行中至关重要的**社交动态**（如谈判与妥协）。

在**多智能体辩论（MAD）领域**，研究受“心智社会”范式启发，探索通过智能体互动达成共识。但现有MAD改进工作主要聚焦于有明确标准答案的客观任务，对于存在**偏好冲突的主观场景**研究较少。近期Debate-to-Write框架表明，基于人设的辩论能增强主观论证的多样性与一致性，拓展了MAD的边界。

在**心智理论（ToM）与谈判建模方面**，通过任务分解模拟ToM任务，为智能体推断他人内部状态提供了认知基础。然而，基于“双重关注模型”的谈判动态（即自利与关注他人之间的张力）在信息不对称环境中的研究仍显不足。

**本文与这些工作的关系和区别在于**：MIND框架直接针对现有旅行规划系统忽略社交谈判的局限，以及MAD在主观冲突场景中研究的稀疏性。它创新性地将ToM与MAD结合，引入了**战略评估**阶段来推断对手意愿，并动态调整谈判策略，从而专门建模并解决具有异质偏好的多方谈判问题，填补了当前研究的空白。

### Q3: 论文如何解决这个问题？

论文通过提出MIND框架来解决多智能体在旅行规划中协调复杂利益的问题。其核心方法是基于心智理论，引入战略评估阶段，使智能体能够从语言细微差别中推断对手的意愿值，从而模拟现实的共识构建过程。

整体框架包含三个主要阶段：首先是数据增强，通过MMR算法提取多样化人物角色，并基于MoSCoW优先级框架为每个偏好分配意愿值；其次是谈判环境构建，明确定义硬约束和软约束，并故意制造至少三个高冲突场景以促进实质性谈判；最后是MIND循环谈判机制，智能体在信息不对称环境下进行多轮互动。

框架包含三个关键模块：战略评估模块负责分析对手语气和论点强度以推断其隐藏意愿值；策略决策模块根据推断结果与自身意愿值的比较，决定采取推动、妥协或让步的策略意图；回退机制则确保当三轮内无法达成多数共识时，采纳最高意愿值智能体的意见，防止整体效用崩溃。

创新点主要体现在：首次将战略评估机制引入多智能体辩论，通过语言细微差别推断对手心理状态；设计了动态语言调整机制，使智能体能够根据意愿值在温暖与强硬语气间灵活切换；建立了基于意愿值比较的策略决策系统，使谈判过程更贴近人类真实互动。这些设计使得MIND在保持谈判流畅性的同时，能有效处理高冲突场景，最终达成更具说服力的共识。

### Q4: 论文做了哪些实验？

论文实验设置以GPT-4.1-mini作为骨干智能体，在旅行规划场景中模拟2至4名具有异质偏好的智能体进行协商。实验使用了201个协商场景，并定义了多个评估指标。

在数据集与基准测试方面，研究采用了增强的角色数据来构建不同规模的协商小组。对比方法为传统的多智能体辩论（Base）框架。主要定量结果如下：MIND在战略效率上显著优于基线，其High-w Hit达到35.08%（提升20.5%），Debate Hit-Rate达到34.65%（提升30.7%）。Debate Ratio高达93.18%，表明绝大多数协议通过自主辩论达成。在可扩展性分析中，当小组规模增至4人时，MIND的Debate Ratio仍保持在88.4%，而基线模型则降至64.5%，显示了其鲁棒性。

关键数据指标包括：心智理论（ToM）推理的准确性在±2误差范围内达到90.2%，皮尔逊相关系数为0.69，平均绝对误差为1.27。在定性评估（LLM-as-a-Judge）中，MIND在理性（68.8%）和流畅性（72.4%）上超越基线，总体胜率为68.3%。此外，对意愿（w）的敏感性分析显示，高意愿（9-10）提议者在MIND中的胜率为76.1%，高于基线的66.2%，而低意愿（1-3）提议者胜率则显著降低至20.8%（基线为43.9%），体现了其战略让步行为。消融实验进一步验证了语调注入与认知评估模块协同作用的必要性。

### Q5: 有什么可以进一步探索的点？

该论文在基于心智理论提升多智能体谈判效能方面取得了显著进展，但仍存在一些局限性和可拓展方向。首先，MIND框架的实验场景集中于旅行规划，其泛化能力有待验证。未来研究可将其应用于更广泛的复杂社会协调领域，如商业谈判、政策制定或冲突调解，以检验其普适性。其次，当前模型对语言细微差别的推断依赖于预设参数，未来可探索结合强化学习，使智能体能在动态交互中自主优化谈判策略，提升适应能力。此外，框架未充分考虑多轮谈判中历史对话对当前决策的长期影响，引入记忆机制或递归推理可能进一步提升谈判连贯性与深度。最后，评估指标虽多维但仍以模拟为主，未来需引入真实人类参与的主观评估，以更全面衡量谈判结果的实际说服力与公平性。

### Q6: 总结一下论文的主要内容

该论文针对多智能体辩论在协调复杂利益相关者（如旅行规划）方面的不足，提出了MIND框架，旨在模拟具有异质偏好的旅行者之间建立共识的谈判对话。核心贡献在于引入基于心理理论的战略评估阶段，通过分析语言细微差别推断对手意愿，准确率达90.2%。方法上，MIND通过多轮对话和动态策略调整，优先处理高风险约束，以促进共识达成。实验表明，MIND在高效协商命中率和辩论命中率上分别提升20.5%和30.7%，且在大模型作为评判的定性评估中，在合理性和流畅度上均优于基线模型，总体胜率达68.3%。这些结果验证了MIND能有效模拟人类谈判动态，推动更具说服力的共识形成，对多智能体协作系统的实际应用具有重要意义。
