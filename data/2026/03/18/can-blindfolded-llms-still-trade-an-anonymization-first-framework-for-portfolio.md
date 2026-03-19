---
title: "Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization"
authors:
  - "Joohyoung Jeon"
  - "Hongchul Lee"
date: "2026-03-18"
arxiv_id: "2603.17692"
arxiv_url: "https://arxiv.org/abs/2603.17692"
pdf_url: "https://arxiv.org/pdf/2603.17692v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "q-fin.CP"
  - "q-fin.PM"
tags:
  - "LLM Agent"
  - "Multi-Agent Systems"
  - "Financial Agent"
  - "Anonymization"
  - "Tool Use"
  - "Reasoning"
  - "Policy Optimization"
  - "Signal Validation"
  - "Backtesting"
  - "Market Dynamics"
relevance_score: 7.5
---

# Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization

## 原始摘要

For LLM trading agents to be genuinely trustworthy, they must demonstrate understanding of market dynamics rather than exploitation of memorized ticker associations. Building responsible multi-agent systems demands rigorous signal validation: proving that predictions reflect legitimate patterns, not pre-trained recall. We address two sources of spurious performance: memorization bias from ticker-specific pre-training, and survivorship bias from flawed backtesting. Our approach is to blindfold the agents--anonymizing all identifiers--and verify whether meaningful signals persist. BlindTrade anonymizes tickers and company names, and four LLM agents output scores along with reasoning. We construct a GNN graph from reasoning embeddings and trade using PPO-DSR policy. On 2025 YTD (through 2025-08-01), we achieved Sharpe 1.40 +/- 0.22 across 20 seeds and validated signal legitimacy through negative control experiments. To assess robustness beyond a single OOS window, we additionally evaluate an extended period (2024--2025), revealing market-regime dependency: the policy excels in volatile conditions but shows reduced alpha in trending bull markets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）应用于金融投资组合优化时，其表现可能依赖虚假信号而非真正市场理解的核心可信度问题。研究背景是LLM在金融交易中的应用日益增多，但现有方法存在严重缺陷：一方面，LLM在预训练中可能记忆了特定股票代码（如“特斯拉”）与市场表现之间的表面关联，而非学习到普适的市场动态规律，导致**记忆偏差**；另一方面，传统的回测方法普遍存在**幸存者偏差**（数据中剔除了已退市的失败公司）和**前瞻性偏差**，使得在历史数据上表现优异的策略在实际部署中失效。现有方法未能严格验证LLM生成的交易信号是否源于对市场模式的合法推理，还是仅仅源于数据泄露或记忆。

因此，本文要解决的核心问题是：如何构建一个可信的LLM交易智能体框架，确保其投资决策基于对市场动态的真实理解，而非对预训练数据中特定标识符（如公司名称、股票代码）的机械记忆或回测环境中的统计偏差。为此，论文提出了“BlindTrade”框架，其核心思想是“蒙眼”（Blindfolded）测试：通过匿名化所有股票标识符，迫使模型仅能依据基本面、新闻事件、动量等通用逻辑进行推理，从而剥离并验证信号的有效性，最终实现一个稳健且可解释的投资组合优化系统。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. LLM交易智能体研究**：FinGPT通过LoRA进行轻量级适配，FinMem增加了对历史市场模式的层次化记忆，TradingAgents则通过多智能体辩论模拟交易公司决策。然而，实时评估研究（如LiveTradeBench和AI-Trader）发现，这些在静态基准上表现优异的模型在实际交易中可能表现不佳，且缺乏风险管理的智能体在实践中表现较差。本文与这些工作的共同点是利用LLM进行交易决策，但核心区别在于，本文通过匿名化方法（BlindTrade）严格检验LLM是否真正理解了市场动态，而非仅仅依赖预训练中对股票代码的**记忆**。

**2. 金融领域大语言模型的局限性**：现有模型如FinBERT和BloombergGPT在训练/评估中直接使用股票代码，导致无法区分模型表现是源于**记忆偏差**还是真正的市场理解。近期综述也提出了相同担忧。本文直接针对此问题，通过匿名化所有标识符来**剥离记忆效应**，从而验证信号的有效性。

**3. 回测偏差问题**：金融回测常受**幸存者偏差**和**前视偏差**影响。本文通过严格使用每个时间点的实际标普500成分股来规避这些偏差，确保了回测的严谨性。

**4. 图神经网络在金融中的应用**：GNN常用于学习股票关系，但大多依赖固定的行业分类图。本文的创新在于，利用LLM推理嵌入的语义相似性**动态构建图关系**，这使得即使在匿名化状态下也能学习有效的股票关联。

**5. 投资组合强化学习**：已有研究引入端到端策略梯度或基于市场状态的方案，但多数RL策略是黑箱。本文的PPO-DSR策略则**显式暴露意图变量**（防御/中性/进攻模式），增强了策略的可解释性，并分析了不同模式下的换手率等行为特征。

### Q3: 论文如何解决这个问题？

论文通过一个名为“BlindTrade”的匿名化优先框架来解决LLM交易代理中存在的记忆偏差和生存偏差问题，其核心是“蒙蔽”代理以验证其是否真正理解市场动态。整体框架包含六个阶段，核心方法、架构设计和关键技术如下：

**1. 整体框架与主要模块：**
框架依次执行数据匿名化、LLM特征生成、IC验证、图神经网络编码、强化学习策略和回测。首先，**数据匿名化模块**将所有股票代码、公司名称及相关专有名词替换为合成标识符（如AAPL→STOCK_0026），切断了LLM依赖预训练记忆的路径。接着，**四个专业化的LLM代理**（动量、新闻事件、风险机制、均值回归）在严格的时间窗口（t-60至t-1）内，基于匿名化数据每日为每只股票生成评分并输出**解释性推理文本**。然后，**IC验证模块**通过计算LLM输出与21日后收益的Spearman秩相关系数，筛选出具有真实预测能力的特征（如风险机制代理的IC显著为正）。此后，**SemGAT编码模块**将每只股票表示为394维特征向量（包含LLM评分和推理文本的384维嵌入），并构建股票关系图：节点基于相同行业全连接，边则基于推理嵌入向量的余弦相似度（>0.75）添加，形成“语义重连”。最后，**RL策略模块**使用PPO算法确定投资组合权重，并引入执行惯性参数控制换手率。

**2. 关键技术细节与创新点：**
- **匿名化与推理强制**：不仅匿名标识符，还要求LLM输出推理过程，为后续图构建提供语义基础，这是验证信号合法性的关键。
- **多视角LLM代理与结构化约束**：每个代理专注于特定市场视角（如新闻事件代理分析匿名化头条情感），并受限于确定性的JSON输出和严格知识截止期，防止前瞻偏差。
- **基于IC的特征筛选与验证**：通过ΔIC（LLM IC - RAW IC）评估特征，不仅关注正向预测信号，也重视将误导性的负相关RAW特征修正至接近零，从而提升信号质量。
- **语义图构建与GNN编码**：创新性地利用LLM推理文本的嵌入相似性构建股票间语义边，使GNN（采用2层GATv2）能学习“评估理由相似”的关系，增强了模型在匿名条件下的关系推理能力。
- **分层RL策略设计**：策略包含三个组件：（i）**意图头**通过聚合所有代理输出选择防御/中性/激进模式，避免单一代理依赖；（ii）**节点评分头**根据意图模式调整温度缩放以控制集中度；（iii）**狄利克雷分布**将评分转化为权重，并结合Top-K掩码（仅保留前20只股票）降低动作空间维度。奖励函数使用可微分的夏普比率，并扣除交易成本。

**3. 解决偏差问题的核心机制：**
- 针对**记忆偏差**：匿名化彻底移除可识别信息，迫使LLM依赖动态分析而非记忆关联；IC验证进一步确认信号源于模式识别而非回忆。
- 针对**生存偏差**：回测时严格使用时点指数成分股数据，动态反映成分股变化，确保评估的鲁棒性。

综上，BlindTrade通过匿名化前置、多代理推理生成、语义图融合及分层强化学习，构建了一个能验证信号真实性、适应市场机制变化的投资组合优化系统。

### Q4: 论文做了哪些实验？

论文实验设置将数据划分为训练集（2020-01-02至2024-09-30）、验证集（2024-10-01至2024-12-31）和样本外测试集（OOS，2025-01-02至2025-08-01，共145个交易日）。此外，为评估鲁棒性，还进行了扩展期（2024-2025年）测试。超参数通过Optuna在验证集上优化，并固定用于OOS评估。所有结果均为20次随机种子的均值±标准差，交易成本设定为每单位换手率10个基点。

使用的基准测试包括被动策略（SPY和EQWL ETF）和主动策略（动量策略、市值Top-20和仅基于技术指标的RAW Top-20）。主要性能指标为年化夏普比率、累计收益、最大回撤和年化波动率。

主要结果显示，BlindTrade在2025年YTD OOS上实现了年化夏普比率1.40±0.22和累计收益32.22%±5.21%，显著优于所有基准。但其波动率（42.34%）和最大回撤（-31.66%）也更高。在扩展期测试中，策略表现出对市场状态的依赖，在波动市场中表现优异，但在趋势性牛市中阿尔法收益降低。

消融实验表明，移除LLM特征会使夏普比率下降0.26（至1.14±0.02）；移除图神经网络结构则导致夏普比率大幅下降0.78（至0.62±0.50），且稳定性变差。负控制实验通过随机打乱GNN预测分数，证实了策略信号的有效性（|RankIC|从0.015降至0.0004）。此外，RL策略通过控制换手率（1.7%/天）对实现盈利至关重要，而简单的等权重Top-20投资因高换手率（139%/天）导致夏普比率崩溃至-1.17。

最后，论文比较了不同的GNN训练目标，发现基础版本（SemGAT）在20次种子中均战胜SPY，且方差最低（0.20），而增加复杂性的变体反而降低了稳定性和胜率。

### Q5: 有什么可以进一步探索的点？

本文的局限性与未来研究方向可从几个维度展开。首先，论文验证了匿名化能有效防止记忆偏差，但未深入探讨匿名化后模型是否仍可能通过其他隐含特征（如行业分类、市值规模等）产生间接记忆，未来可研究更彻底的特征剥离方法。其次，策略在趋势性牛市（trending bull markets）中阿尔法收益下降，表明其存在市场状态依赖性，未来可探索自适应机制，使智能体能根据市场状态（如波动率、趋势强度）动态调整意图（Intent）或集成不同市场机制下的专家策略。此外，当前框架依赖人工设计的意图统计量（动量、风险等），未来可尝试用可学习的表征替代，以更灵活地捕捉市场共识。最后，论文主要聚焦股票市场，该框架在跨资产（如加密货币、外汇）或极端市场情境下的泛化能力仍有待检验，这也是一个重要的探索方向。

### Q6: 总结一下论文的主要内容

本文提出了一种名为BlindTrade的匿名化框架，旨在解决LLM交易代理中因记忆偏差和幸存者偏差导致的虚假性能问题，以验证其是否真正理解市场动态。核心方法是“蒙蔽”代理，即在投资组合优化过程中对股票代码和公司名称进行匿名化处理，迫使模型依赖市场模式而非记忆信息。具体流程包括：四个LLM代理基于匿名化信息输出评分与推理；从推理嵌入构建图神经网络（GNN）图；最终使用PPO-DSR策略进行交易决策。实验结果表明，在2025年初至8月1日的测试中，该框架实现了1.40±0.22的夏普比率，并通过负对照实验验证了信号的有效性。此外，在2024-2025年的扩展评估中，发现策略表现具有市场状态依赖性：在波动市场中表现优异，但在趋势性牛市中阿尔法收益降低。该研究的核心贡献在于通过严格的匿名化验证，为构建可靠、负责任的多智能体交易系统提供了方法论基础，强调了信号验证在金融AI应用中的重要性。
