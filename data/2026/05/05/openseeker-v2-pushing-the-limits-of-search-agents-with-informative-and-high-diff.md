---
title: "OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories"
authors:
  - "Yuwen Du"
  - "Rui Ye"
  - "Shuo Tang"
  - "Keduan Huang"
  - "Xinyu Zhu"
  - "Yuzhu Cai"
  - "Siheng Chen"
date: "2026-05-05"
arxiv_id: "2605.04036"
arxiv_url: "https://arxiv.org/abs/2605.04036"
pdf_url: "https://arxiv.org/pdf/2605.04036v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "搜索智能体"
  - "监督微调"
  - "数据合成"
  - "浏览基准"
  - "开源"
relevance_score: 9.0
---

# OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories

## 原始摘要

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry recipe involves a highly resource-intensive pipeline spanning pre-training, continual pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). In this report, we show that when fueled with informative and high-difficulty trajectories, a simple SFT approach could be surprisingly powerful for training frontier search agents. By introducing three simple data synthesis modifications: scaling knowledge graph size for richer exploration, expanding the tool set size for broader functionality, and strict low-step filtering, we establish a stronger baseline. Trained on merely 10.6k data points, our OpenSeeker-v2 achieves state-of-the-art performance across 4 benchmarks (30B-sized agents with ReAct paradigm): 46.0% on BrowseComp, 58.1% on BrowseComp-ZH, 34.6% on Humanity's Last Exam, and 78.0% on xbench, surpassing even Tongyi DeepResearch trained with heavy CPT+SFT+RL pipeline, which achieves 43.4%, 46.7%, 32.9%, and 75.0%, respectively. Notably, OpenSeeker-v2 represents the first state-of-the-art search agent within its model scale and paradigm to be developed by a purely academic team using only SFT. We are excited to open-source the OpenSeeker-v2 model weights and share our simple yet effective findings to make frontier search agent research more accessible to the community.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决前沿搜索智能体（search agents）开发领域长期被工业界巨头垄断、依赖昂贵且复杂的多阶段训练流水线（如持续预训练CPT、监督微调SFT、强化学习RL）的问题。现有方法（如通义DeepResearch）虽然性能出众，但需要海量计算资源和专有数据，形成了巨大的研究壁垒，严重阻碍了学术界和开源社区的创新与参与。作者的核心挑战在于：能否仅通过一种简单直接的SFT方法，仅靠高质量的训练轨迹数据，就达到甚至超越这些重工业流水线的性能？为此，论文提出了OpenSeeker-v2。其核心思路并非设计更复杂的训练算法或模型架构，而是将焦点完全回归到训练数据的质量上。通过引入三项关键的数据合成改进：扩大知识图谱规模以提供更丰富的探索路径、扩展工具集数量以学习更多样化的策略、以及实施严格的低步骤过滤以确保任务难度，作者构建了一个仅含约1万条高难度轨迹的数据集。实验证明，仅在此小数据集上对约30B参数的模型进行一次SFT训练，就取得了跨4个基准的全面最优性能（例如在BrowseComp上46.0% vs 通义DeepResearch的43.4%），首次由纯学术团队使用纯SFT方式在ReAct范式中达成了SOTA水平，有效降低了前沿搜索智能体研究的门槛。

### Q2: 有哪些相关研究？

本文的相关研究主要可以分为以下几类：

**方法类**：最直接相关的是工业界的深度搜索智能体训练范式，例如通义千问的DeepResearch，它依赖于持续的预训练（CPT）、监督微调（SFT）和强化学习（RL）这一复杂且资源密集型的流水线。本文的工作OpenSeeker-v2与这些工作的核心区别在于，它挑战了这种多阶段训练的依赖关系，证明了仅通过简单的SFT方法，并在高质量、高难度轨迹数据驱动下，就能达到甚至超越复杂的工业流水线性能。另一个相关工作是本文的前身OpenSeeker，OpenSeeker-v2在其基础上进行了数据合成管线的关键升级。

**应用/评测类**：本文聚焦于搜索智能体，其性能通过与多个代表性评测基准进行对比来证明，包括BrowseComp、BrowseComp-ZH、Humanity's Last Exam和xbench。这些基准构成了当前前沿搜索智能体的主要评估框架，其中一些模型（如Tongyi DeepResearch）是本文的直接对比对象。

总体而言，本文的核心贡献在于通过强调数据质量而非复杂训练流程，为学术社区提供了一个可复现且高性能的搜索智能体基线，与工业界的资源密集型路径形成了鲜明对比。

### Q3: 论文如何解决这个问题？

OpenSeeker-v2 通过一个基于监督微调（SFT）的简洁但高效的数据合成与训练框架解决了当前搜索智能体依赖昂贵工业流水线的问题。其核心思想是：只要提供信息丰富且高难度的训练轨迹，简单的SFT目标就足以诱导出强大的长程搜索与推理能力。具体方法包括三个关键技术创新：

1.  **扩展知识图谱规模（Scaling Graph Size）**：在任务合成阶段，从原始知识图 \(\mathcal{G}\) 中构建更大的子图 \(\mathcal{G}_{sub}^{(K)}\)（\(K > k\)）。更大的子图包含更丰富的拓扑相关源，增加了可行推理路径的数量和多样性，从而迫使模型学会跨多节点聚合证据，而非依赖少数几个源。

2.  **扩展工具集规模（Expanding the Tool Set）**：为搜索智能体配备一个比先前版本更大的工具集 \(\mathcal{A}\)。在生成ReAct风格的轨迹 \(\tau\) 时，模型可从更丰富的工具中调用动作 \(a_t\)。这鼓励模型学习更多样化的交互模式，并利用互补工具解决问题，从而产生更灵活、功能更丰富的行为。

3.  **严格低步过滤（Strict Low-step Filtering）**：对合成的原始轨迹数据进行过滤，仅保留工具调用步数 \(T(\tau)\) 大于等于阈值 \(T_{\min}\) 的样本。这剔除了那些可通过直接查找或浅层关键词匹配解决的简单实例，确保了训练数据的最低难度门槛。

最终，OpenSeeker-v2 在仅使用10.6k个经过过滤后的、高难度且信息丰富的训练数据上，基于 Qwen3-30B-A3B 模型进行标准的 SFT 训练。该方法是一个纯学术团队在30B规模模型上、使用简单的 SFT 方案，首次在多个基准上超越了采用CPT+SFT+RL等复杂工业流水线训练的同类模型。

### Q4: 论文做了哪些实验？

OpenSeeker-v2通过三个关键改进（扩大知识图谱规模、扩展工具集、严格低步数过滤）生成了高质量训练数据，仅使用10.6k条轨迹进行监督微调（SFT）。实验在四个基准测试上进行：BrowseComp、BrowseComp-ZH、Humanity's Last Exam (HLE)和xbench-DeepSearch。对比方法包括同规模（约30B参数）的ReAct范式智能体，如Tongyi DeepResearch（使用CPT+SFT+RL）、RedSearcher（使用CPT+SFT+RL）、WebSailor-V2、WebLeaper及OpenSeeker-v1，以及更大规模的开源/闭源模型。主要结果：OpenSeeker-v2在四个基准上均取得最优，分别为46.0%（BrowseComp）、58.1%（BrowseComp-ZH）、34.6%（HLE）和78.0%（xbench），全面超越使用更复杂流水线的Tongyi DeepResearch（43.4%、46.7%、32.9%、75.0%）。相比OpenSeeker-v1，在BrowseComp上提升16.5%（29.5→46.0），在xbench上提升4%。平均轨迹步数达64.67步（高于v1的46.97步和RedSearcher的36.01步），表明数据难度更高。

### Q5: 有什么可以进一步探索的点？

论文的核心贡献在于验证了高质量合成数据对搜索Agent能力的巨大提升，但其局限性同样明显。首先，当前方法高度依赖模板化的数据合成流程，包括固定知识图谱、预定义工具集和规则式过滤，这可能导致数据多样性不足，限制了模型在更开放、动态场景下的泛化能力。未来可以探索基于强化学习或对抗生成的方法来自动生成更复杂、更具探索性的轨迹，例如动态调整图结构、引入随机工具组合，甚至模拟人类在搜索过程中的试错行为。其次，论文仅聚焦于30B参数规模的ReAct范式模型，对于更大规模、更复杂架构（如Plan-and-Solve、树搜索）的效果尚不明确。此外，虽然SFT取得了惊人的效果，但RL阶段的缺失可能意味着性能天花板，未来工作可尝试在高质量数据上进行短链RL微调以进一步优化策略。最后，数据量的缩放律需要更系统的验证，包括在百万级样本下是否持续有效，以及如何平衡数据量增长与质量衰退的风险。

### Q6: 总结一下论文的主要内容

这篇论文提出了OpenSeeker-v2，一个基于简单监督微调（SFT）方法的高性能搜索代理。核心问题是：在依赖大量资源的预训练、连续预训练（CPT）、SFT和强化学习（RL）的工业级流水线主导下，如何用更少的资源训练出前沿搜索代理。方法上，该论文通过三项关键数据合成改进：扩大知识图谱规模以增强探索丰富性、扩展工具集以提升功能广度、以及实施严格的低步数过滤，仅用10.6k数据点就训练出强大的搜索代理。主要结论是，OpenSeeker-v2在四个基准测试（BrowseComp、BrowseComp-ZH、Humanity's Last Exam、xbench）上均取得最优性能，分别达到46.0%、58.1%、34.6%和78.0%，显著超越了采用CPT+SFT+RL流水线的Tongyi DeepResearch（43.4%、46.7%、32.9%和75.0%）。这是首个由纯学术团队仅使用SFT方法开发出的该规模与范式下的最佳搜索代理，表明精心设计的高质量数据能解锁大幅性能提升，为社区获取前沿搜索代理研究提供了更易实现的途径。
