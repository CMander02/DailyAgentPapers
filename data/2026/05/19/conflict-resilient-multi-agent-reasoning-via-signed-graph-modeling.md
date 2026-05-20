---
title: "Conflict-Resilient Multi-Agent Reasoning via Signed Graph Modeling"
authors:
  - "Longgang He"
  - "Longzhu He"
  - "Daojing He"
  - "Chaozhuo Li"
date: "2026-05-19"
arxiv_id: "2605.19418"
arxiv_url: "https://arxiv.org/abs/2605.19418"
pdf_url: "https://arxiv.org/pdf/2605.19418v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "符号图建模"
  - "冲突感知推理"
  - "结构化交互图"
  - "消息传递"
  - "LLM智能体协作"
relevance_score: 9.5
---

# Conflict-Resilient Multi-Agent Reasoning via Signed Graph Modeling

## 原始摘要

LLM-based multi-agent systems (MAS) have demonstrated strong reasoning and decision-making capabilities that consistently surpass those of single LLM agents. However, their performance often suffers from naive aggregation mechanisms that assume uniformly cooperative interactions. Upon close inspection, we observe that existing graph-based MAS frameworks (1) propagate errors when conflicting signals arise without control, and (2) lack explicit modeling of conflicting inter-agent relations as well as structural awareness, failing to identify reliable interaction patterns. To bridge this gap, we introduce SIGMA, a novel SIgned Graph-informed Multi-Agent reasoning framework that explicitly captures trust, conflict, and neutral relations among agents via a signed relational graph. Specifically, given a query, SIGMA first selects a set of relevant and diverse agents, then constructs a structured signed interaction graph with confidence-weighted edges. Reasoning proceeds through conflict-aware signed message passing, which reinforces information from trustworthy agents while suppressing conflicting signals, and terminates with a structure- and conflict-aware weighted aggregation to yield globally consistent and conflict-resilient predictions. Extensive experiments on six benchmark datasets, across multiple LLM backbones and diverse multi-agent configurations, demonstrate that SIGMA consistently outperforms state-of-the-art baselines, achieving notable gains in both accuracy and conflict-resilient performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的多智能体系统（MAS）在推理过程中面临的冲突鲁棒性问题。当前，基于图的MAS框架虽然能建模智能体间的复杂交互，但存在两个核心不足：一是假设所有智能体间都是均匀协作关系，缺乏对信任、冲突等不同极性关系的明确建模，导致冲突信号在推理过程中不受控制地传播并放大错误；二是缺乏结构感知能力，难以识别可靠交互模式，当面对噪声或对抗性智能体时，系统鲁棒性显著下降。现有方法（如链式、树式、图式结构）均采用简单聚合机制，无法区分来自可信或矛盾智能体的信息，从而在冲突场景下容易产生不一致或错误的全局预测。为弥补这一差距，本文提出SIGMA框架，核心创新在于通过符号图（Signed Graph）显式建模智能体间的信任、冲突和中性三种关系，并引入冲突感知的带符号消息传递机制，强化可信信息、压制冲突信号，最终实现结构感知与冲突感知的加权聚合，从而在存在矛盾或低质量智能体的复杂推理场景中，生成全局一致且冲突鲁棒的预测结果。

### Q2: 有哪些相关研究？

相关研究主要包括三类方法：**（1）基于图的LLM多智能体系统**，如DyLAN、AutoAgents等，它们假设智能体之间的交互关系均为非负合作，通过无向或有向图推进推理。与之不同，本研究指出这种假设忽略了冲突信号，SIGMA显式建模正负交互关系，避免了错误传播和不稳定共识。（2）**冲突检测与消歧方法**，如Mixture-of-Agents（MoA）利用多个模型生成的候选答案，通过投票或加权减少分歧，但缺乏结构化的关系建模。SIGMA通过符号图不仅区分信任与冲突，还利用平衡理论在传播中抑制不可靠信号。（3）**符号图神经网络（Signed GNN）**，如SGCN、SiGAT，已在社交网络分析中建模积极和消极关系，但主要面向静态网络和固定特征。本文首次将其引入LLM推理场景，结合文本交互实现动态子图构建和冲突感知的消息传递。

### Q3: 论文如何解决这个问题？

SIGMA框架的核心方法是构建带符号的关系图来显式建模智能体间的信任、冲突和中立关系，从而实现冲突鲁棒的多智能体推理。整体框架主要由四个阶段组成：查询引导的智能体选择、带符号关系图构建、冲突感知的符号消息传递、以及符号共识读出。

首先，查询引导的智能体选择机制通过一个统一评分函数联合考量语义相关性、结构多样性和智能体置信度三个维度，筛选出高质量、多样且可靠的智能体子集，为后续推理奠定基础。接着，SIGMA构建一个带符号的邻接矩阵，其中每条边被分解为表示交互极性的符号（正表示信任，负表示冲突）和表示强度的权重，从而显式建模不同类型的交互关系，并利用符号图平衡理论递归定义多跳的平衡和不平衡邻域，以捕获长程的共识与矛盾模式。

然后，在冲突感知的符号消息传递阶段，每个智能体维护独立的积极（pos）和消极（neg）表示向量，通过多跳邻域聚合来自支持性和冲突性的信号，并在聚合过程中对冲突信号进行极性翻转，从而有效分离和利用相反信号来精炼表征。最后，符号共识读出阶段采用结构感知的加权聚合，权重基于智能体在符号图中的净支持强度计算，从而强调被广泛认可的智能体并抑制处于冲突中的智能体，生成稳定且一致的全局预测。

该框架的创新点在于：1) 显式建模冲突关系，克服了传统方法假设均匀合作的局限；2) 设计冲突感知符号消息传递机制，实现了支持与冲突信号的结构化传播；3) 采用结构感知加权聚合，增强了推理对噪声和不可靠交互的鲁棒性。

### Q4: 论文做了哪些实验？

论文在六个基准数据集上进行了全面实验，包括通用推理数据集（MMLU、MMLU-Pro、GPQA）和领域特定数据集（GSM8K、MultiArith、HumanEval）。对比方法涵盖单智能体方法（CoT、ComplexCoT、Self-Consistency、PHP）和多智能体方法（MoA、Self-MoA、Complete Graph、Random Graph、DyLAN、AutoGen、GPTSwarm、G-Designer、GoA）。采用GPT-5和GPT-5 mini作为骨干模型，温度设为0.7。主要结果：SIGMA在所有数据集上均取得最佳平均准确率89.17%，其中MMLU达92.53%、MMLU-Pro 95.71%、GPQA 54.51%、GSM8K 96.23%、MultiArith 98.87%、HumanEval 97.14%，显著优于最先进基线（如G-Designer平均88.53%）。此外，消融实验显示冲突感知消息传递（CMP）和结构感知聚合（SCR）是关键模块。鲁棒性实验表明，在高达50%恶意智能体注入下，SIGMA在MMLU上最大性能下降仅4.1%，HumanEval上最差情况仍达91%。超参数敏感性分析显示λ和k对性能影响稳定。

### Q5: 有什么可以进一步探索的点？

首先，SIGMA框架中的符号图构建依赖于初始代理的选择和置信度加权，这可能导致对初始种子质量的敏感性，未来可探索动态或基于上下文的代理选取机制以减少偏差。其次，尽管冲突感知消息传递有效抑制了矛盾信号，但框架未充分处理冲突的时变特性——真实交互中合作关系可能动态演变，可以引入时序图或在线学习机制来实时更新符号边权重。另外，当前工作主要聚焦于聚合阶段的冲突缓解，但未深入分析冲突源头（如知识盲区或推理错误），因此未来方向可结合可解释性模块，通过反事实推理定位具体冲突原因。从改进思路上看，可尝试将符号图建模与强化学习结合，使代理能从历史冲突中自我优化互动策略，或引入自适应阈值来区分“建设性辩论”与“有害冲突”。最后，扩展到多模态场景或大规模异构代理网络将是重要挑战，需要探索更高效的符号图表示学习与稀疏化技术。

### Q6: 总结一下论文的主要内容

现有的基于LLM的多智能体系统存在一个关键限制：它们假设智能体间为均匀合作关系，缺乏对冲突和信任关系的显式建模，导致在矛盾或噪声信号下传播错误、鲁棒性下降。为解决该问题，该论文提出SIGMA框架，通过符号关系图建模智能体间的信任、冲突和中性关系。方法首先根据查询选择相关且多样化的智能体，构建带置信度权重的结构化符号交互图；然后通过冲突感知的符号消息传递机制增强可信信号并压制冲突信号；最后进行结构和冲突感知的加权聚合以生成全局一致且冲突鲁棒的预测。在六个基准数据集上的实验表明，SIGMA在多种LLM骨干网络和多智能体配置下均优于现有方法，在准确率和冲突鲁棒性上取得显著提升。该研究首次将符号图建模引入多智能体推理，揭示了结构化关系建模对提升系统可靠性的核心作用。
