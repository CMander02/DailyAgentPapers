---
title: "ReDAct: Uncertainty-Aware Deferral for LLM Agents"
authors:
  - "Dzianis Piatrashyn"
  - "Nikita Kotelevskii"
  - "Kirill Grishchenkov"
  - "Nikita Glazkov"
  - "Ivan Nasonov"
  - "Ilya Makarov"
  - "Timothy Baldwin"
  - "Preslav Nakov"
  - "Roman Vashurin"
  - "Maxim Panov"
date: "2026-04-08"
arxiv_id: "2604.07036"
arxiv_url: "https://arxiv.org/abs/2604.07036"
pdf_url: "https://arxiv.org/pdf/2604.07036v1"
categories:
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Uncertainty Estimation"
  - "Model Cascading"
  - "Sequential Decision-Making"
  - "Cost-Efficiency"
  - "Embodied Environments"
  - "ALFWorld"
  - "MiniGrid"
relevance_score: 8.0
---

# ReDAct: Uncertainty-Aware Deferral for LLM Agents

## 原始摘要

Recently, LLM-based agents have become increasingly popular across many applications, including complex sequential decision-making problems. However, they inherit the tendency of LLMs to hallucinate, leading to incorrect decisions. In sequential settings, even a single mistake can irreversibly degrade the trajectory, making hallucinations an even bigger problem. Although larger LLMs hallucinate less, they incur a significantly higher per-token cost. In this paper, we address this tradeoff by proposing ReDAct (Reason-Defer-Act). In ReDAct, an agent is equipped with two LLMs: a small, cheap model used by default, and a large, more reliable but expensive model. When the predictive uncertainty of the small model exceeds a calibrated threshold, the decision is deferred to the large model. We evaluate our approach in text-based embodied environments such as ALFWorld and MiniGrid and show that deferring only about 15% of decisions to the large model can match the quality of using it exclusively, while significantly reducing inference costs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在顺序决策环境中，因模型幻觉导致错误行动，进而造成不可逆的轨迹退化问题，同时平衡性能与推理成本。研究背景是LLM智能体在文本化具身环境（如ALFWorld和MiniGrid）中的广泛应用，这些环境要求智能体在部分可观测状态下进行连续决策，任何单一错误都可能累积并彻底破坏整个任务 episode。现有方法主要存在两个不足：一是尽管使用更大、更可靠的LLM可以减少幻觉，但会带来极高的每 token 计算成本，不适合持续部署；二是现有的模型路由或级联方法通常针对单次查询选择模型，没有考虑智能体在交互式轨迹中需要连续决策的场景，且缺乏在顺序环境下基于不确定性进行动态 deferral（推迟决策）的机制。因此，本文的核心问题是：如何在顺序决策任务中，设计一种成本感知的机制，使得智能体能在自身不确定性高时，将决策推迟给更大更可靠的模型，从而以较低成本达到与全程使用大模型相当的性能。为此，论文提出了ReDAct框架，通过不确定性量化来触发 deferral，实现性能与效率的权衡。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三个领域：不确定性量化、预测延迟以及具身环境中的智能体应用。

在**不确定性量化**方面，相关方法主要分为三类。第一类是信息论方法，直接利用生成词元的概率，要求模型是白盒的。第二类关注生成输出的语义，通常需要多次生成序列并通过自然语言推理进行聚类，计算其“方差”（如熵），计算成本较高。第三类是言语化方法，通过提示让大语言模型直接输出“我不确定”或置信度。本文的方法属于第一类，利用小模型生成动作的概率来估计不确定性，但将其应用于序列决策的延迟场景。

在**预测延迟**方面，已有研究在图像和文本领域探讨了延迟到更高级模型的机制。针对大语言模型，有工作训练了监督路由器在小模型和大模型之间进行选择，但这些研究仅限于单步任务（如问答），未涉及序列化智能体问题。一项相关研究在不确定性高时延迟到“预言机”（如人类），但该方法依赖于成本高昂的共形预测，且仅考虑延迟到人类，而本文则实现了完全自主的、在大小模型之间的延迟。

在**具身环境智能体**方面，已有许多工作将基于大语言模型的智能体应用于文本化具身环境，如ALFWorld、MiniGrid和WebShop。这些环境测试了智能体在长序列、不可逆状态变化或部分可观测下的决策能力。然而，此前的研究尚未在智能体内部考虑基于不确定性的、在小模型和大模型之间的动态延迟机制。本文的ReDAct框架首次将不确定性感知的延迟机制引入到此类序列决策的智能体中，以在控制成本的同时保证决策质量。

### Q3: 论文如何解决这个问题？

论文通过提出ReDAct框架来解决LLM智能体在序列决策中因幻觉导致错误累积以及大模型成本高昂的问题。其核心方法是设计一个双模型协作的智能体架构，在不确定性超过阈值时将决策权从默认的小模型转移至可靠但昂贵的大模型，从而在保证性能的同时显著降低成本。

整体框架遵循ReAct范式，但引入了不确定性感知的延迟决策机制。主要模块包括：1）一个默认使用的小型、低成本LLM；2）一个备用的大型、高可靠性LLM；3）一个基于动作级不确定性量化的延迟触发器；4）一个经过校准的阈值选择模块。关键技术在于如何有效量化不确定性并确定延迟时机。

论文通过实验发现，在推理阶段和动作选择阶段中，动作级的不确定性指标（如困惑度、序列概率和平均词元熵）能更可靠地预测错误，且无需重复模型推理，因此ReDAct专注于动作级不确定性度量。具体而言，在每个决策步骤，系统计算小模型生成动作的不确定性值，若超过预设阈值τ，则将该步骤的决策任务交由大模型处理。

创新点体现在两方面：一是提出了基于校准阈值的动态延迟机制，通过在小模型不确定性过高时调用大模型，平衡了成本与可靠性；二是设计了一种数据驱动的阈值校准方法，使用一组校准样本来确定阈值，使得大模型的平均调用次数接近预设目标K，从而实现对成本的控制。实验表明，仅需将约15%的决策延迟给大模型，即可达到完全使用大模型的性能水平，同时大幅降低推理开销。

### Q4: 论文做了哪些实验？

论文在ALFWorld和MiniGrid这两个基于文本的具身交互环境中进行了实验。实验设置方面，ALFWorld使用了400个episode，MiniGrid使用了200个episode，每个episode的最大步数上限为50步。在MiniGrid中，主要采用了全视角设置。

使用的模型分为小型和大型两类。小型模型包括Qwen-small、Llama-3和Llama-4，大型模型包括GPT-4、Qwen-medium和Qwen-large。评估指标主要是任务成功率（成功episode占总episode的比例）和推理成本（以美元计）。

对比方法包括：仅使用小型模型、仅使用大型模型，以及作为基线的随机调用大型模型策略。ReDAct的核心是使用基于不确定性的指标（信息熵MTE、语义概率SP和困惑度PPL）来指导何时将决策“递延”给大型模型。这些指标的阈值在100个episode的校准集上设定，目标是平均每个episode调用大型模型约5次。

主要结果显示，基于不确定性（尤其是困惑度PPL）的递延策略显著优于随机递延。关键数据指标是：在ALFWorld环境中，基于PPL的ReDAct方法仅需将总步数中约15%的决策递延给大型模型，就能达到与全程使用大型模型相当的成功率（例如，Qwen-small + GPT-4组合下，成功率从0.683提升至0.808，接近GPT-4单独使用的0.783）。在成本方面，仅使用GPT-4的成本为45.21美元，而Qwen-small + GPT-4（PPL策略）的成本仅为16.25美元，在性能相近的情况下大幅降低了开销。实验还表明，不确定性引导的递延在成功率和大型模型调用次数/成本之间达到了帕累托最优。

### Q5: 有什么可以进一步探索的点？

该论文提出的ReDAct方法在不确定性感知的延迟决策方面取得了进展，但仍存在若干局限性和可进一步探索的方向。首先，该方法依赖信息论不确定性量化（UQ）方法，需要获取词元级概率，这在某些API受限或黑盒模型场景中可能难以实现。其次，研究仅考虑了参数规模超过700亿的大型模型，未涵盖更广泛的小型或中等规模模型，限制了方法的普适性。

未来研究方向可以从以下几个角度展开：一是探索更灵活的不确定性估计方法，例如基于模型内部表征或无需概率输出的代理指标，以适配更多样的模型部署环境。二是将延迟机制扩展到多模型协作框架，不仅限于大小模型切换，可引入领域专家模型或工具调用，形成动态路由决策网络。三是研究在更复杂的长期规划任务中，如何优化延迟阈值的学习策略，使其能自适应环境变化和任务阶段。此外，可以探索将延迟决策与在线学习结合，让模型在交互中持续校准不确定性估计，进一步提升成本效益比。

### Q6: 总结一下论文的主要内容

本文提出ReDAct框架，旨在解决LLM智能体在序列决策中因幻觉导致错误累积的问题，核心贡献在于通过不确定性感知的延迟决策机制平衡性能与成本。问题定义聚焦于如何在降低大模型高昂推理开销的同时，维持智能体在复杂环境（如ALFWorld和MiniGrid）中的决策质量。方法概述为：智能体配备一大一小两个LLM模型，默认使用小模型决策，并基于其预测不确定性（如信息论指标Perplexity）动态校准阈值，当不确定性超过阈值时将决策延迟给大模型处理。主要结论显示，仅需将约15%的高不确定性决策交由大模型处理，即可达到甚至超越全程使用大模型的性能，同时大幅降低成本；其中动作级别的不确定性信号最为有效，为高效部署LLM智能体提供了简单可行的路径。
