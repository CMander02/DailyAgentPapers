---
title: "Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems"
authors:
  - "Meghana Karnam"
  - "Ananya Joshi"
date: "2026-04-24"
arxiv_id: "2604.22154"
arxiv_url: "https://arxiv.org/abs/2604.22154"
pdf_url: "https://arxiv.org/pdf/2604.22154v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "LLM-as-a-Judge"
  - "Adaptive Sampling"
  - "Behavioral Health"
  - "Safety-Critical Agent"
  - "Confidence Bounds"
  - "DAG-structured Agent Pipelines"
relevance_score: 8.5
---

# Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems

## 原始摘要

Emerging AI systems in behavioral health and psychiatry use multi-step or multi-agent LLM pipelines for tasks like assessing self-harm risk and screening for depression. However, common evaluation approaches, like LLM-as-a-judge, do not indicate when a decision is reliable or how errors may accumulate across multiple LLM judgements, limiting their suitability for safety-critical settings. We present a statistical framework for multi-agent pipelines structured as directed acyclic graphs (DAGs) that provides an alternative to heuristic voting with principled, adaptive decision-making. We model each agent as a stochastic categorical decision and introduce (1) tighter agent-level performance confidence bounds, (2) a bandit-based adaptive sampling strategy based on input difficulty, and (3) regret guarantees over the multi-agent system that shows logarithmic error growth when deployed. We evaluate our system on two labeled datasets in behavioral health : the AEGIS 2.0 behavioral health subset (N=161) and a stratified sample of SWMH Reddit posts (N=250). Empirically, our adaptive sampling strategy achieves the lowest false positive rate of any condition across both datasets, 0.095 on AEGIS 2.0 compared to 0.159 for single-agent models, reducing incorrect flagging of safe content by 40\% and still having similar false negative rates across all conditions. These results suggest that principled adaptive sampling offers a meaningful improvement in precision without reducing recall in this setting.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体大语言模型（LLM）系统在安全关键场景（如自伤风险筛查）中可靠性不足的问题。研究背景是，医院和行为健康机构正在探索使用多步或多智能体LLM管线来辅助精神科分诊、危机响应等任务，这些任务通常遵循严格的机构标准操作流程（SOP），要求系统做出精准且安全的决策。现有方法存在明显不足：当前多智能体系统大多基于启发式方法，例如对固定次数的随机LLM调用结果进行简单多数投票（即“LLM作为法官”），这种方式缺乏判断决策何时可靠的原理，也无法量化多步决策中误差如何累积。此外，误差是非对称的——漏检自伤风险可能导致患者处于危险中，而过度升级则会造成临床警报疲劳和资源浪费。现有评估仅提供性能的点估计，缺乏依赖于输入的保证或最坏情况界限。因此，本文的核心问题是：如何为多智能体LLM系统构建一个统计框架，以提供原则化的、自适应的决策机制，从而可靠地判断何时可以自主行动、如何在不增加临床负担的前提下减少漏检，并保证系统在部署中误差随交互次数增长缓慢。论文通过建模每个智能体为随机分类决策，引入更紧的性能置信界、基于难度的自适应采样策略，以及提供对数误差增长遗憾保证来解决这一问题。

### Q2: 有哪些相关研究？

相关研究可分为评测资源类和方法类。评测资源方面，早期工作包括基于临床笔记的机器学习（如Guo等人，2024）及ScAN数据集中的自杀企图标注；社交媒体领域有SWMH Reddit数据集和CLPsych共享任务，以及基于哥伦比亚自杀严重程度评定量表（C-SSRS）构建的评估框架。AEGIS 2.0提供了涵盖自伤安全类别的人工标注LLM响应。ToxicChat和RealToxicityPrompts评估毒性，而LLM危害分析提供了失败模式框架。方法类方面，最相关的是将行为健康评估智能体组织成有向无环图（DAG）的工作，通过节点蒙特卡洛采样实现高达19%的准确率提升。其他多智能体系统也通过结构化流水线路由输入。本文与这些工作的核心区别在于：现有方法要么依赖单次LLM-as-a-judge分类，要么使用固定样本投票，无法确定采样充分性或错误累积方式。本文首次为DAG结构多智能体流水线提供了正式保证——通过智能体级置信界、基于难度的自适应采样策略（类似于bandit算法）以及对数级误差增长的可保证后悔界，实现了可靠决策，并在两个行为健康数据集上将假阳性率降低40%的同时保持召回率不变。

### Q3: 论文如何解决这个问题？

论文通过构建一个自适应多智能体大语言模型系统来解决自伤风险筛查中的可靠性问题。整体架构基于有向无环图，包含三个专业智能体节点：Worker节点执行初级内容筛查，Risk节点进行二次风险评估，Legal节点负责最终合规审查，构成递进升级链。每个节点共享动作空间{安全、不安全、升级}，其中升级标签会将输入传递给下游节点。

核心技术是采用自适应采样赌博机算法替代传统固定样本多数投票。每个节点将输入评估建模为K臂赌博机问题（K=3），通过置信区间消除非最优决策。算法核心创新包括：（1）基于DKW不等式推导出更紧的节点级性能置信界，确保算法以至少1-δ的概率不会错误消除真实最优臂；（2）提出“识别或升级”终止条件：当预算耗尽仍无法确定标签时返回升级而非强制分类，保留医疗安全性保障；（3）建立系统级遗憾保证，证明自适应策略的累积遗憾为O(log T)而非O(T)，意味着错误增长随处理量增加呈对数级而非线性增长。

关键设计是统一动作空间使所有节点共享相同统计保证，避免不同节点需不同不等式带来的复杂度。样本复杂度分析表明，输入难度决定所需LLM调用次数：概率间隙Δ_s(x)大的明确输入快速收敛，模糊输入升级至人类专家。实验证明该策略在保持相似假阴性率的同时，将假阳性率降低40%。

### Q4: 论文做了哪些实验？

论文在AEGIS 2.0行为健康子集（N=161）和SWMH Reddit帖子分层样本（N=250）两个数据集上进行了实验。实验设置了10种条件，涵盖单智能体（1次LLM调用）、多数投票（MV n=1/3/5，在DAG各节点独立调用n次）以及自适应采样（预算B=10/50/75/100/124/150，采用基于bandit的自适应采样策略）。对比方法包括单智能体系统和固定采样多数投票，报告了准确率、假阳性率（FPR）、假阴性率（FNR）、升级率和平均拉取次数等指标，并给出95% Wilson置信区间。

在AEGIS 2.0上，主要结果：自适应采样B=100达到最高准确率0.768（95% CI [0.695, 0.827]），FPR最低为0.095（95% CI [0.037, 0.221]），相比单智能体的0.159降低40%；FNR在各条件下稳定在0.281-0.290之间。在SWMH上，自适应采样B=100同样获得最低FPR为0.227；所有有效条件对自杀关注子版块（SW）的FNR均为0.100（95% CI [0.044, 0.214]），且预算超过100后无额外收益。B=10和B=50因预算过低导致所有输入升级，无法分类。

### Q5: 有什么可以进一步探索的点？

论文提出的自适应多智能体系统在可靠性上取得了显著进步，但存在若干可改进方向。首先，预算耗尽时的路由行为过保守：当节点在B次采样内无法收敛时仍传递至后续节点，导致最多3B次调用后才送达人工审核，计算成本高昂。未来可引入预算耗尽即提前终止并直接上报的策略，减少对模糊输入的冗余计算。其次需区分预算耗尽与模型主动上报两种升级情形，以便为临床决策提供更细致的路由依据。此外，当前自适应采样平均需80-90次拉取，相比多数投票n=3的1-5次，API调用成本增加20-30倍，实际部署中需权衡FPR收益与预算限制。基础模型、温度参数及临床人群对最小有效预算B=100的影响尚待验证。最后，SWMH数据集以子版块成员身份代理临床金标准，应基于C-SSRS等验证工具和临床专家标注构建基准，以更准确评估假阴性率。

### Q6: 总结一下论文的主要内容

本论文针对心理健康领域AI系统中多智能体流水线在安全关键场景下的可靠性问题，提出了一种基于自适应多智能体大语言模型（LLM）的可靠自伤风险筛查框架。该方法将每个智能体建模为随机分类变量，通过统计框架提供四大贡献：更紧致的智能体级性能置信界、基于输入难度的自适应采样策略（使用多臂老虎机算法）、以及保障多智能体系统部署时对数级误差增长的遗憾界。在AEGIS 2.0行为健康子集（N=161）和SWMH Reddit帖子分层样本（N=250）两个数据集上，该自适应采样策略在所有条件下实现了最低假阳性率（AEGIS 2.0上0.095 vs. 单智能体模型0.159），将无害内容的错误标记减少了40%，同时假阴性率保持类似水平。核心结论表明，在安全关键临床环境中，用自适应采样替代固定样本多数投票能显著提升精度而不牺牲召回率，并且当无法在预算内做出置信决策时，系统会升级至人工审核而非猜测，强调“知道何时不决策”与“知道如何决策”同等重要。这项工作为多智能体LLM系统在安全关键场景中的可靠部署提供了原则性的决策框架。
