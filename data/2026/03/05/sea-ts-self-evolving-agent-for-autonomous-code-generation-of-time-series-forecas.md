---
title: "SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms"
authors:
  - "Longkun Xu"
  - "Xiaochun Zhang"
  - "Qiantu Tuo"
  - "Rui Li"
date: "2026-03-05"
arxiv_id: "2603.04873"
arxiv_url: "https://arxiv.org/abs/2603.04873"
pdf_url: "https://arxiv.org/pdf/2603.04873v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "自演化"
  - "代码生成"
  - "规划与推理"
  - "工具使用"
  - "强化学习"
relevance_score: 9.0
---

# SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms

## 原始摘要

Accurate time series forecasting underpins decision-making across domains, yet conventional ML development suffers from data scarcity in new deployments, poor adaptability under distribution shift, and diminishing returns from manual iteration. We propose Self-Evolving Agent for Time Series Algorithms (SEA-TS), a framework that autonomously generates, validates, and optimizes forecasting code via an iterative self-evolution loop. Our framework introduces three key innovations: (1) Metric-Advantage Monte Carlo Tree Search (MA-MCTS), which replaces fixed rewards with a normalized advantage score for discriminative search guidance; (2) Code Review with running prompt refinement, where each executed solution undergoes automated review followed by prompt updates that encode corrective patterns, preventing recurrence of similar errors; and (3) Global Steerable Reasoning, which compares each node against global best and worst solutions, enabling cross-trajectory knowledge transfer. We adopt a MAP-Elites archive for architectural diversity. On the public Solar-Energy benchmark, SEA-TS generated code achieves a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On proprietary datasets, SEA-TS generated code reduces WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieves 26.17% MAPE on load forecasting versus 29.34% by TimeMixer. Notably, the evolved models discover novel architectural patterns--including physics-informed monotonic decay heads encoding solar irradiance constraints, per-station learned diurnal cycle profiles, and learnable hourly bias correction--demonstrating that autonomous ML engineering can generate genuinely novel algorithmic ideas beyond manual design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统时间序列预测模型开发过程中面临的三大核心挑战：数据稀缺、分布漂移以及人工迭代带来的边际效益递减问题。研究背景是，尽管时间序列预测在能源、金融、医疗等多个领域至关重要，但现有机器学习开发流程依赖大量领域专家经验和手动试错，效率低下且难以适应动态变化的环境。

现有基于大语言模型的自主代码生成方法（如AIDE、ML-Master）试图将LLM作为“机器学习工程师”来自动编写和优化代码，但仍存在明显不足：一是智能体容易通过“作弊代码”（如数据泄露）获得虚高的评估分数，而这类逻辑错误难以自动检测；二是搜索策略通常使用固定或二元奖励机制，无法区分细微改进与重大突破，导致搜索效率低下；三是智能体的推理仅依赖局部信息，缺乏对全局最优和最差解决方案的认知；四是系统提示词在整个搜索过程中保持静态，无法根据已发现的错误模式或成功经验进行动态调整。

因此，本文的核心问题是：如何构建一个能够自主、高效且可靠地生成、验证并持续优化时间序列预测算法代码的智能体框架。具体而言，论文提出了SEA-TS框架，旨在通过其创新的自进化循环，克服现有方法的上述缺陷，实现无需人工干预的、能够发现新颖有效算法架构的自动化机器学习工程。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：基于LLM的自主机器学习代理、质量-多样性优化方法，以及时间序列预测模型。

在**基于LLM的自主机器学习代理**方面，相关工作如AIDE、ML-Master、I-MCTS和R&D-Agent，它们利用大语言模型生成和优化代码。本文提出的SEA-TS框架与这些工作一脉相承，但针对其普遍存在的三个局限进行了改进：通过引入带运行提示精炼的代码审查机制防止奖励黑客攻击；使用基于标准化优势分的MA-MCTS提升奖励粒度；以及通过全局可引导推理实现跨轨迹知识迁移，突破了局部搜索的局限。

在**质量-多样性优化方法**方面，本文借鉴了MAP-Elites及其变体（如AlphaEvolve、OpenEvolve）的思想，利用档案库来维持生成解决方案的架构多样性，以确保探索到不同行为特征的高性能模型。

在**时间序列预测模型**方面，相关工作涵盖了从统计方法到深度学习模型（如Transformer变体TimeMixer和iTransformer）以及结合物理知识的混合模型。本文的SEA-TS并非提出一个新的具体预测模型，而是提供了一个能够针对特定部署场景自动生成、验证和优化预测代码的自主工程框架，旨在解决现有模型手动适配成本高的问题，并在此过程中发现了新颖的架构模式。

### Q3: 论文如何解决这个问题？

论文通过一个名为SEA-TS的自进化智能体框架来解决时间序列预测算法的自主代码生成问题。其核心方法是将算法开发建模为程序空间上的搜索问题，并设计了一个结合蒙特卡洛树搜索（MCTS）、大语言模型（LLM）代码生成与自动化评估的闭环自进化系统。

整体框架是一个迭代的五阶段循环：1）基于UCT公式的节点选择；2）提示组装与代码生成；3）沙箱执行与评估；4）代码审查与提示更新；5）树更新（包括奖励计算、反向传播和存档维护）。框架的关键创新点体现在三个核心组件上：

首先，**度量优势蒙特卡洛树搜索（MA-MCTS）** 取代了传统的固定奖励。它通过计算当前节点性能指标（如WAPE、MAPE）相对于历史指标分布的标准化Z分数（即“优势分数”A_j）作为奖励信号。这使得奖励具有区分性（对突破性改进给予高奖励）、自适应性（随搜索进程调整尺度）且与具体度量指标无关。奖励R_j最终由优势分数和代码审查结果共同决定，逻辑错误的代码会被赋予固定负奖励（-1），以防止错误方案污染搜索树。

其次，**带有运行提示精炼的代码审查**机制。每个成功执行的代码都会经过一个LLM审查器进行自动化逻辑审查，重点检测数据泄露、归一化错误、数据污染等隐蔽问题。审查结果（是否逻辑错误）直接影响奖励。更重要的是，无论是否发现问题，审查的发现以及后续的“全局可导推理”洞察都会被一个辅助LLM提炼成可执行的文本更新，持续集成到“运行提示”（P_run）中。这使得系统提示成为一个不断积累纠正性保障和正向设计模式的自改进知识库，防止类似错误复发并引导后续生成。

第三，**全局可导推理**。该机制将每个新评估的非错误节点与全局最佳（N*）和最差（N⊥）解决方案进行结构化比较，由一个LLM生成总结，指出值得效仿的成功策略和需要避免的失败模式。这些全局洞察会被附加到节点分析中，并在其作为父节点时传递给子节点，实现了跨搜索轨迹的知识迁移，而不仅仅是沿着树路径的渐进式改进。

此外，系统采用**MAP-Elites存档**来维持架构多样性，沿架构类型、特征工程复杂度和训练复杂度三个表型维度对精英解进行分类存档，防止搜索收敛到狭窄的架构子集。

总之，SEA-TS通过将MA-MCTS的定向搜索、自动化代码审查与提示精炼的知识积累、以及全局比较的跨轨迹推理有机结合，形成了一个能够自主生成、验证、优化并发现新颖算法模式的自进化系统。

### Q4: 论文做了哪些实验？

论文在能源时间序列预测领域进行了实验，涵盖公开基准和行业专有数据集。实验设置方面，SEA-TS框架使用GPT-5（高推理能力）进行代码生成和审查，Qwen3-coder-plus作为替代模型。采用MCTS进行搜索（探索常数C=√2，每任务预算T=500次迭代），并使用MAP-Elites存档（343个单元）保持架构多样性。

数据集与基准测试包括：1）公开数据集Solar-Energy（137个光伏电站的10分钟间隔数据）；2）专有光伏数据集（2023年10月至2025年3月的每小时发电数据）；3）专有负荷数据集（2025年5月至10月的每小时居民用电数据）。对比方法为当前最先进的TimeMixer和Timer模型。

主要结果与关键指标如下：在公开Solar-Energy基准上，SEA-TS生成代码的MAE为1.757，相比TimeMixer的2.929降低了40%。在专有光伏预测任务中，WAPE从TimeMixer的25.75%降至17.12%，相对降低8.6%。在专有负荷预测任务中，相比Timer的WAPE 47.47%，SEA-TS降至39.74%（降低7.7%）；相比TimeMixer的MAPE 29.34%，SEA-TS达到26.17%（降低3.17%）。

实验还发现，自主演化出的模型架构包含多项新颖模式，如编码太阳辐照度物理约束的单调衰减头、针对每个站点的学习型日周期剖面、以及可学习的每小时偏差校正等，这些均未在初始参考代码或提示中出现，体现了自主机器学习工程超越人工设计的创新能力。

### Q5: 有什么可以进一步探索的点？

本文提出的SEA-TS框架在自主生成时序预测代码方面取得了显著进展，但其仍存在一些局限性，并为进一步探索提供了方向。论文自身指出的未来工作包括多目标优化、上下文剪枝、自动维度发现、高级搜索算法研究、领域知识注入以及编码与研究智能体的结合。这些方向旨在提升效率、降低成本和增强生成模型的实用性。

在此基础上，我认为还有几个值得深入探索的点。首先，框架目前主要针对代码生成，但生成的模型在长期稳定性和泛化能力方面仍需在更复杂、多变的数据分布下进行系统性评估。其次，当前的“自我进化”循环严重依赖预设的奖励信号和代码审查机制，未来可以探索更动态、自适应的评估机制，使智能体能够自主定义或调整优化目标。此外，将框架扩展至其他序列生成任务（如自然语言生成、程序合成）或跨模态任务，验证其通用性也是一个有趣的方向。最后，如何使生成的“新颖架构模式”不仅性能优越，而且具备更好的可解释性，以促进人机协作与信任，是实际部署中需要解决的关键问题。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为SEA-TS的自进化智能体框架，旨在自主生成、验证和优化时间序列预测算法的代码，以解决传统机器学习开发中面临的数据稀缺、分布漂移适应性差以及手动迭代收益递减等问题。其核心贡献在于引入了三个关键创新方法：首先，采用基于度量优势的蒙特卡洛树搜索（MA-MCTS），通过归一化的优势分数替代固定奖励，以提供更具区分性的搜索指导；其次，设计了带有运行提示精炼的代码审查机制，对每个执行的解决方案进行自动审查，并更新提示以编码纠正模式，防止类似错误复发；最后，提出全局可引导推理，通过将每个节点与全局最优及最差解决方案进行比较，实现跨轨迹的知识迁移。此外，框架采用MAP-Elites存档以保持架构多样性。实验结果表明，在公开的Solar-Energy基准测试中，SEA-TS生成的代码相比TimeMixer实现了40%的平均绝对误差降低，超越了现有最优方法；在私有数据集上，其在太阳能光伏预测和住宅负荷预测任务中分别比人工设计的基线模型降低了8.6%和7.7%的加权绝对百分比误差。尤为重要的是，进化出的模型发现了新颖的架构模式，如编码太阳辐照约束的物理信息单调衰减头、各站点学习的日周期配置文件以及可学习的每小时偏差校正，这证明了自主机器学习工程能够产生超越人工设计的全新算法思想。
