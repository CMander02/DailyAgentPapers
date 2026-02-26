---
title: "AgentLTV: An Agent-Based Unified Search-and-Evolution Framework for Automated Lifetime Value Prediction"
authors:
  - "Chaowei Wu"
  - "Huazhu Chen"
  - "Congde Yuan"
  - "Qirui Yang"
  - "Guoqing Song"
  - "Yue Gao"
  - "Li Luo"
  - "Frank Youhua Chen"
  - "Mengzhuo Guo"
date: "2026-02-25"
arxiv_id: "2602.21634"
arxiv_url: "https://arxiv.org/abs/2602.21634"
pdf_url: "https://arxiv.org/pdf/2602.21634v1"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 数据合成/规划/推理/记忆/工具使用"
  - "LLM 应用于 Agent 场景"
  - "自动化机器学习"
  - "代码生成与执行"
  - "搜索与演化算法"
relevance_score: 9.0
---

# AgentLTV: An Agent-Based Unified Search-and-Evolution Framework for Automated Lifetime Value Prediction

## 原始摘要

Lifetime Value (LTV) prediction is critical in advertising, recommender systems, and e-commerce. In practice, LTV data patterns vary across decision scenarios. As a result, practitioners often build complex, scenario-specific pipelines and iterate over feature processing, objective design, and tuning. This process is expensive and hard to transfer. We propose AgentLTV, an agent-based unified search-and-evolution framework for automated LTV modeling. AgentLTV treats each candidate solution as an {executable pipeline program}. LLM-driven agents generate code, run and repair pipelines, and analyze execution feedback. Two decision agents coordinate a two-stage search. The Monte Carlo Tree Search (MCTS) stage explores a broad space of modeling choices under a fixed budget, guided by the Polynomial Upper Confidence bounds for Trees criterion and a Pareto-aware multi-metric value function. The Evolutionary Algorithm (EA) stage refines the best MCTS program via island-based evolution with crossover, mutation, and migration. Experiments on a large-scale proprietary dataset and a public benchmark show that AgentLTV consistently discovers strong models across ranking and error metrics. Online bucket-level analysis further indicates improved ranking consistency and value calibration, especially for high-value and negative-LTV segments. We summarize practitioner-oriented takeaways: use MCTS for rapid adaptation to new data patterns, use EA for stable refinement, and validate deployment readiness with bucket-level ranking and calibration diagnostics. The proposed AgentLTV has been successfully deployed online.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决生命周期价值（LTV）预测建模在实际工业应用中面临的核心挑战：构建高效、可迁移且能处理复杂数据模式（如负LTV）的自动化建模流程成本高昂且困难。研究背景是，LTV预测在广告、推荐和电商等领域至关重要，但现有方法存在明显不足。传统方法主要分为三类：概率模型依赖强分布假设，可能简化用户行为导致精度下降；机器学习方法虽表现更好，但难以处理大规模高维数据；深度学习方法能捕捉复杂模式，但在工业部署中仍面临三大挑战：一是多数方法无法显式处理负LTV（如用户带来净成本），而负值会破坏常见损失函数（如零膨胀对数正态损失）的假设；二是建模过程高度依赖人工，需反复迭代特征工程、目标设计和超参数调优，导致开发和维护成本极高；三是现有模型通常针对特定场景定制，复杂且难以迁移到新场景，易出现过拟合问题。近期虽有研究利用大语言模型（LLM）自动生成代码，但难以平衡场景特异性与泛化性，仍可能生成与任务不匹配的流水线。因此，本文的核心问题是：如何设计一个自动化框架，以系统化地搜索和演化LTV建模流水线，从而减少人工干预、适应多样数据模式（包括负LTV）、并提升模型在不同场景下的可迁移性与部署效率。为此，论文提出了AgentLTV框架，通过基于智能体的统一搜索与演化机制来解决上述问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大领域：LTV预测方法和基于LLM的代码生成。

在**LTV预测方法**方面，相关工作可分为三类。一是基于概率统计的模型，如RFM框架和Pareto/NBD模型（BTYD家族），它们解释性强但难以建模长期动态。二是基于传统机器学习的方法，如将LTV预测视为回归/分类问题，使用随机森林或两阶段（购买倾向与金额）框架，这些方法在结构化场景有效，但对序列依赖和复杂非线性模式建模能力有限。三是基于深度学习的方法，如使用CNN识别高价值用户、引入ZILN损失处理零膨胀和重尾分布，以及结合循环网络、注意力机制和图神经网络的最新进展。此外，工业界也部署了多任务、分布感知的系统（如Kuaishou、NetEase、Baidu、Tencent的方案）。与这些工作不同，本文提出的AgentLTV并非设计另一个特定的LTV模型，而是构建一个**自动化框架**，旨在通过智能搜索与演化自动生成和优化整个建模流水线，以解决现有方法需要大量人工、场景特定、难以迁移的痛点。

在**基于LLM的代码生成**方面，相关工作主要遵循两种范式。一是广度优先策略，即LLM生成大量独立候选程序并通过执行评估选择最佳（如相关研究），或结合执行反馈进行迭代修复。更进一步的研究将LLM与树搜索结合，用于指导结构化空间中的代码生成（如Yao等人、Koh等人的工作）。二是深度优先的代码演化范式，即LLM在多轮迭代中引导程序的变异与精化（如FunSearch、AlphaEvolve等）。本文的AgentLTV框架**融合并扩展了这两种范式**：它首先利用蒙特卡洛树搜索（MCTS）进行广泛的探索，然后通过进化算法（EA）进行深度精化。这与现有工作不同，现有方法在LTV建模场景下面临挑战——广度优先方法可能无法生成可运行且准确的预测模型，而深度演化方法通常需要一个稳定的初始程序（这在现实LTV设置中难以获得）。AgentLTV通过两阶段协同搜索，专门解决了在自动化LTV模型代码生成中平衡广泛探索与结构化优化的关键难题。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于LLM驱动的多智能体协作统一搜索与进化框架AgentLTV来解决LTV建模中场景特定、流程复杂且难以迁移的问题。其核心方法是将每个候选解决方案视为一个可执行的流水线程序，利用智能体自动生成、运行、修复和分析代码，并通过两阶段搜索策略（蒙特卡洛树搜索MCTS和进化算法EA）来高效探索和优化模型。

整体框架包含三个紧密耦合的模块：配置模块、MCTS模块和EA模块。配置模块负责实例化决策智能体（MCTS智能体和EA智能体）和辅助智能体（代码生成器、代码修复器、专家优化器和顾问智能体），所有智能体都遵循统一的流水线接口以确保公平比较。MCTS模块在固定预算下对高层建模决策进行广泛探索。它采用多根初始化生成多样化的初始程序，然后使用结合了多项式上置信树（PUCT）准则和帕累托感知多指标价值函数的节点选择策略，在探索与利用之间取得平衡。在LLM驱动的扩展步骤中，顾问智能体分析程序结构并提出优化建议，专家优化器注入LTV领域知识并将其转化为可执行的提示，代码生成器据此生成新的子程序，代码修复器则负责执行、评估和迭代修复。节点价值通过一个综合考虑多个评估指标、帕累托前沿状态和种群多样性的奖励函数进行更新，并通过反向传播优化搜索。最终输出MCTS阶段的最佳程序。

EA模块则对MCTS的最佳程序进行精细化改进。它采用基于岛屿的进化策略，以促进多样性并避免早熟收敛。首先，利用MCTS的最优程序通过变异初始化多个岛屿的种群。在每个岛屿内，进化过程包括评估程序适应度、根据精英比率选择精英个体、通过交叉和变异（操作由顾问智能体和专家优化器指导生成）产生后代，并形成新一代种群。此外，定期在岛屿间迁移高适应度程序以实现知识共享。经过多代进化后，从所有岛屿中选出全局最优程序作为最终输出的LTV预测代码。

关键创新点在于：1) 构建了一个LLM驱动的多智能体系统，将领域知识、代码生成与自动执行修复无缝集成；2) 设计了两阶段分层搜索策略，MCTS用于快速、广泛的探索以适应新数据模式，EA用于稳定、深入的细化；3) 在搜索过程中引入了帕累托感知的多目标奖励和基于拥挤距离的多样性奖励，以平衡不同评估指标并保持解集的多样性；4) 提出了面向实践者的部署验证方法，强调使用分桶级别的排序和校准诊断来确保模型上线 readiness。该框架已成功在线部署，实验表明其能在排序和误差指标上持续发现强模型。

### Q4: 论文做了哪些实验？

论文进行了四项实验来评估AgentLTV框架。实验设置方面，主要在一个大规模工业数据集（来自一款流行手机游戏，包含约80万用户，覆盖两个季度数据）和一个公开基准（Kaggle Acquire Valued Shoppers Challenge数据集，约180万样本）上进行。数据集按8:1:1划分为训练/验证/测试集。特征包括用户属性、广告属性和游戏行为共132维，标签是安装后60天的累计收入（可为负值）。评估指标包括误差率（ER）、归一化基尼系数（Norm GINI）、斯皮尔曼等级相关（Spearman）和均方根误差（RMSE）。

对比方法涵盖了广泛的LTV预测基线模型，包括Wide&Deep、DeepFM、ZILN、DCN、GateNet、Kuaishou、TSUR、OptDist、USE-LTV和Hi-LTV。AgentLTV框架本身采用两阶段搜索：蒙特卡洛树搜索（MCTS）阶段在固定预算下探索广泛的建模选择空间，进化算法（EA）阶段对最佳MCTS程序进行基于岛屿的交叉、变异和迁移优化。

主要结果显示，在工业数据集上，AgentLTV在所有指标上均显著优于基线。具体关键数据指标：与最强基线相比，AgentLTV平均降低ER 41.26%，提升Norm GINI 15.44%，提升Spearman 40.97%，降低RMSE 47.82%（例如Period 1上ER为0.705，Norm GINI为0.963）。消融实验表明，移除EA阶段会导致性能下降（如RMSE从141.09升至185.95），移除MCTS阶段则对排名相关指标影响更大（Norm GINI从0.962降至0.778）。在线桶级分析显示，AgentLTV在高价值和负LTV区间提升了排名一致性和值校准。在公开数据集上，AgentLTV也持续领先（ER 0.479，Norm GINI 0.732，RMSE 3646.851），验证了其泛化能力。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentLTV框架在自动化LTV建模方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架依赖LLM生成和修复代码，其生成质量、稳定性和计算成本仍需优化，未来可研究更轻量、可控的代码生成机制。其次，搜索过程基于固定预算，缺乏自适应调整搜索策略的能力，可引入元学习或强化学习动态分配MCTS与EA的资源。此外，实验主要基于特定数据集，框架在更广泛场景（如小样本、多模态数据）下的泛化能力有待验证。从方法融合角度看，可探索将符号推理与神经搜索结合，提升 pipeline 的可解释性。最后，当前框架侧重于离线优化，未来可研究在线学习机制，实现模型在部署后的持续进化，并进一步系统化评估框架的长期维护成本与效益。

### Q6: 总结一下论文的主要内容

该论文提出了AgentLTV，一个基于智能体的统一搜索与进化框架，用于自动化生命周期价值（LTV）预测建模。核心问题是解决LTV预测中因数据模式多变而需人工构建复杂、场景特定流水线的高成本和低可迁移性难题。其核心贡献在于将候选解决方案视为可执行的流水线程序，利用LLM驱动的智能体生成代码、运行修复流水线并分析反馈，通过两阶段决策智能体协调搜索：第一阶段采用蒙特卡洛树搜索（MCTS），在固定预算下基于多项式上置信界树准则和帕累托感知多指标价值函数，广泛探索建模选择空间；第二阶段采用进化算法（EA），通过基于岛屿的交叉、变异和迁移操作，对MCTS得到的最佳程序进行精细化改进。实验表明，AgentLTV在排名和误差指标上均能稳定发现强模型，在线桶级分析进一步提升了排名一致性和价值校准能力，尤其对高价值和负LTV用户段效果显著。该框架已成功在线部署，为实践者提供了关键启示：利用MCTS快速适应新数据模式，利用EA进行稳定优化，并通过桶级排名和校准诊断验证部署就绪度。
