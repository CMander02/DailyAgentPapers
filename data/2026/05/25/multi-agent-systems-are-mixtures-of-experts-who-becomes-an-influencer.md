---
title: "Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?"
authors:
  - "Franka Bause"
  - "Jonas Niederle"
  - "Martin Pawelczyk"
  - "Rebekka Burkholz"
date: "2026-05-25"
arxiv_id: "2605.25929"
arxiv_url: "https://arxiv.org/abs/2605.25929"
pdf_url: "https://arxiv.org/pdf/2605.25929v1"
categories:
  - "cs.MA"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "意见动力学"
  - "MoE"
  - "协作推理"
  - "智能体影响力"
relevance_score: 8.5
---

# Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?

## 原始摘要

The effectiveness of multi-agent LLM deliberation depends not only on the agents' individual predictions, but also on how they communicate and collaborate. We study this mechanism through the lens of Friedkin-Johnsen (FJ) opinion dynamics, a tractable model for analyzing stubbornness, influence, and opinion change in multi-agent systems that captures empirically observed deliberation patterns. We show that the FJ parameters are input-dependent, turning multi-agent deliberation into a mixture of experts. This perspective implies that multi-agent systems can outperform single agents and static ensembles when routing reflects agent competence. Since competence is latent in practice, we analyze how influence is established through observable proxies: agents' self-assessed confidence, their perceived confidence, and initial alignment with other agents' views.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体LLM系统中如何有效分配影响力以提升整体性能的核心问题。研究背景是，多智能体系统通过多个LLM的迭代沟通和协作，理论上能比单智能体或静态集成更好地处理复杂任务，但实际效果却不稳定。现有方法的不足在于：缺乏一个原则性的框架来理解意见如何在沟通中演化，以及影响力如何塑造最终结果；传统的意见聚合方法（如自一致性、思维链提示）没有深入分析智能体之间的说服力差异和动态交互过程。本文要解决的核心问题是：在多智能体审议过程中，是什么因素使得某些智能体比其他智能体更具影响力？论文通过将多智能体审议建模为Friedkin-Johnsen（FJ）意见动力学，并发现FJ参数是输入依赖的，从而揭示了多智能体系统本质上是隐式的混合专家（MoE）模型——根据输入自适应地路由到最称职的智能体。由于真实能力是潜变量，论文进一步分析了可观察的替代指标（如智能体自我评估的置信度、他人感知的置信度、与其他智能体的初始一致程度）如何影响影响力的形成，为设计更有效的多智能体协作机制提供理论基础。

### Q2: 有哪些相关研究？

这项研究的相关工作可从类别梳理如下。**方法类**中，Friedkin-Johnsen (FJ) 模型被广泛应用于社会科学的意见动态研究，用于分析群体共识形成与固执性。近期工作将FJ模型引入LLM多智能体系统（MAS）以建模信念传播与系统性风险。本文与之不同，强调FJ参数是输入依赖的，从而将MAS协商解读为**混合专家系统（MoE）**，即每个智能体根据输入自适应路由，而非传统MoE中的显式门控网络。**应用类**中，自一致性、思维链提示等方法通过聚合多样意见提升推理鲁棒性，但缺乏对意见演化与影响力机制的刻画。本文通过FJ模型提供了原则性解释，揭示影响如何通过可观察代理（如自信度、初始对齐）建立。**评测类**相关研究关注MAS可解释性，探索协作决策中的涌现行为。本文扩展了这一方向，通过基于信念传播的框架，实证分析了自主路由行为，强调相对自信度是影响力路由的关键因素，初始对齐与社会行为也起辅助作用。与现有工作相比，本文的理论贡献在于将输入依赖的FJ参数与MoE路由机制关联，并为潜能力评估的代理（如自信度）如何驱动隐性路由提供了理论分析，从而指导MAS设计需关注局部能力路由而非仅依赖智能体多样性。

### Q3: 论文如何解决这个问题？

多智能体系统通过Friedkin-Johnsen模型进行观点动力学建模，将其转化为混合专家系统。核心创新在于证明了FJ参数（固执度、保留权重和影响矩阵）是输入依赖的，使系统能够根据输入问题自适应调整专家权重。整体框架包含三个关键模块：1) 智能体网络，每个智能体持有初始信念并按照FJ动力学更新；2) 信念更新机制，包含先验信念拉动、信念保留和同伴影响拉动三个分量；3) 路由机制，通过初始信念计算输入依赖的专家权重。

关键技术包括：采用Brier损失函数进行性能评估，提出局部模糊分解将模型性能分解为局部专家能力、局部多样性和路由遗憾三项。通过理论推导，系统优于单智能体的条件是专门化增益加局部多样性大于路由遗憾。路由机制主要依赖智能体的初始信念置信度，通过熵度量计算校准的置信度得分，并使用softmax函数生成路由权重。

创新点在于揭示了MAS作为MoE的内在机理：即使智能体平均能力差异不大，其内在随机性也能产生局部多样性被路由机制利用。通过分析置信度与能力之间的校准关系，确定了自适应路由能超越静态集成的条件。

### Q4: 论文做了哪些实验？

实验使用了MMLU-Pro、BBQ和CommonsenseQA (CSQA)三个数据集，每个数据集分别采样300或100个问题。采用GPT-5.4 Mini和Qwen2.5-14B-Instruct两种语言模型，通过角色分配（如医生、粗心的学生）或沟通风格（如简洁、平衡、情感化）引入代理多样性。设置5个代理、完全图通信结构、5轮讨论，3个随机种子运行。主要实验包括：1）将FJ模型拟合到多代理系统动力学，拟合指标KL散度均值0.0529、MSE均值0.0021，表明FJ模型能很好解释代理协作动态；2）代理系统（78.5%准确率）优于静态集成基线（将初始信念平均）和FJ集成（固定参数），验证了输入依赖的门控机制即MoE模型；3）识别出影响主要集中在小部分代理上，且与固执程度（γ）强相关；4）通过随机森林回归（R²=0.7）和分类（准确率0.9）模型发现：自信度（尤其是相对于第二自信代理的自信度）是最强影响预测因子，能力（agent competence）和沟通风格也显著影响，而绝对自信度比相对自信度预测力弱。

### Q5: 有什么可以进一步探索的点？

该研究将多智能体系统类比为混合专家模型，揭示了意见动态与路由机制的联系，但仍存在若干局限。首先，其依赖的FJ模型假设意见更新遵循线性过程，但实际多轮对话中可能呈现非线性复杂动态，例如观点突变或群体极化现象。其次，研究主要基于代理的置信度等可观测指标推断影响力，但未深入探讨隐性知识（如专业知识领域差异）对路由决策的影响，这可能导致专家能力错配。未来可结合贝叶斯非参数方法建模潜在能力分布，或引入对抗性校准机制提升置信度可靠性。此外，当前框架假设通信拓扑固定，而真实场景中智能体可能动态调整交互结构，例如通过强化学习自适应选择沟通对象。探索异构意见更新规则（如引入记忆效应或惰性因子）以及异步通信模式，将有助于提升模型对复杂协作场景的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文研究了多智能体大语言模型系统的协作机制。基于Friedkin-Johnsen意见动力学模型，作者将多智能体系统形式化为一种混合专家模型，其中智能体间的意见融合、固执程度和影响力等参数依赖于输入。核心贡献在于揭示了多智能体系统能够超越单一模型和静态集成的条件：当路由机制能反映智能体在特定领域的专业能力时。由于智能体的真实能力是隐性的，论文重点分析了影响力如何通过可观察的代理指标建立，包括智能体的自我评估置信度、其他智能体感知到的置信度以及与群体观点的初始对齐程度。主要结论表明，多智能体系统的优势源于自适应路由和多样化、校准良好的智能体的局部专业化，而局限性则来自置信度校准错误、误导性共识和路由误差。该研究为理解和设计更高效的多智能体协作系统提供了重要的理论框架。
