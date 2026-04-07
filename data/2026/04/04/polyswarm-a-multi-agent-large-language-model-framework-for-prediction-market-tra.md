---
title: "PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage"
authors:
  - "Rajat M. Barot"
  - "Arjun S. Borkhatariya"
date: "2026-04-04"
arxiv_id: "2604.03888"
arxiv_url: "https://arxiv.org/abs/2604.03888"
pdf_url: "https://arxiv.org/pdf/2604.03888v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
  - "q-fin.TR"
tags:
  - "Multi-Agent"
  - "LLM Agent"
  - "Prediction Market"
  - "Trading"
  - "Swarm Intelligence"
  - "Decision-Making"
  - "Risk Management"
  - "Framework"
  - "Financial AI"
relevance_score: 7.5
---

# PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage

## 原始摘要

This paper presents PolySwarm, a novel multi-agent large language model (LLM) framework designed for real-time prediction market trading and latency arbitrage on decentralized platforms such as Polymarket. PolySwarm deploys a swarm of 50 diverse LLM personas that concurrently evaluate binary outcome markets, aggregating individual probability estimates through confidence-weighted Bayesian combination of swarm consensus with market-implied probabilities, and applying quarter-Kelly position sizing for risk-controlled execution. The system incorporates an information-theoretic market analysis engine using Kullback-Leibler (KL) divergence and Jensen-Shannon (JS) divergence to detect cross-market inefficiencies and negation pair mispricings. A latency arbitrage module exploits stale Polymarket prices by deriving CEX-implied probabilities from a log-normal pricing model and executing trades within the human reaction-time window. We provide a full architectural description, implementation details, and evaluation methodology using Brier scores, calibration analysis, and log-loss metrics benchmarked against human superforecaster performance. We further discuss open challenges including hallucination in agent pools, computational cost at scale, regulatory exposure, and feedback-loop risk, and outline five priority directions for future research. Experimental results demonstrate that swarm aggregation consistently outperforms single-model baselines in probability calibration on Polymarket prediction tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用大型语言模型（LLM）在去中心化预测市场（如Polymarket）中进行实时、可靠且有利可图的自动化交易和套利的问题。

研究背景方面，区块链预测市场（如Polymarket、Kalshi）已成为聚合分散信息、形成共识概率预测的重要金融机制，交易量巨大，为自动化系统提供了天然测试场。同时，LLM在理解和推理非结构化文本信息方面展现出强大潜力，使其成为金融预测的候选工具。

然而，现有方法存在明显不足。单一LLM部署存在众所周知的缺陷：容易产生事实性“幻觉”、概率估计系统性过度自信或校准不佳、对提示词表述敏感度高。这些在金融语境下后果严重，一个自信但错误的预测会直接导致交易亏损。此外，单个LLM的推理本质上是高方差的随机采样，结果不稳定。尽管近期出现了AutoGen等多智能体框架，但将其应用于实时金融市场预测与交易的研究仍基本处于空白。

因此，本文要解决的核心问题是：如何设计一个稳健的多智能体LLM框架，以克服单一模型的局限性，在预测市场中实现更准确、校准更好的概率预测，并在此基础上执行风险可控的交易，同时探测和利用市场低效性（如跨市场定价偏差和延迟套利机会）。PolySwarm框架通过部署多样化的智能体群、采用置信度加权的贝叶斯聚合方法、结合信息论市场分析引擎以及延迟套利模块，来系统性地应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要属于“LLMs用于金融预测”这一领域，可分为以下几类：

**1. 金融情感分析与文本挖掘**：早期基于词典的方法（如Loughran-McDonald金融情感词典）因可解释性强而被广泛采用。随着预训练模型发展，领域特定微调成为最佳实践，例如FinBERT在金融情感基准上优于通用BERT。近期，大型语言模型（如ChatGPT）在零样本情况下对新闻标题进行情感分析，已显示出预测股票收益的显著能力，超越了传统词典方法。

**2. LLMs直接用于价格预测与交易**：研究尝试以零样本或少样本提示方式，让LLMs基于价格历史、新闻和技术指标进行方向性或概率性预测。尽管早期结果积极，但后续评估揭示了其局限性，包括无法获取实时数据、预测置信度校准不佳，以及在有效市场假说下持续盈利的挑战。检索增强生成（RAG）和ReAct（推理与行动交织）框架被引入，以整合外部实时知识并改善推理过程。

**3. 多智能体与协作方法**：为克服单模型幻觉、过度自信和提示敏感性问题，研究开始探索多智能体框架。例如，通过多智能体辩论减少幻觉，或使用AutoGen等进行灵活智能体编排。这些方法旨在汇集多样视角，降低相关误差。

**4. 本文（PolySwarm）与相关工作的关系和区别**：
- **关系**：本文建立在上述研究基础上，特别是利用LLMs进行市场预测、采用多智能体协作思想，并关注信息整合（如类似RAG的考量）。
- **区别**：本文的创新点在于**专门针对去中心化预测市场（如Polymarket）**，设计了一个包含**50个多样化LLM人格的群体系统**，并采用**基于置信度的贝叶斯聚合**与市场隐含概率结合。此外，系统集成了**基于KL散度和JS散度的信息论市场分析引擎**以检测低效定价，并包含一个**延迟套利模块**，利用中心化交易所（CEX）的定价模型在人类反应时间窗口内执行交易。这构成了一个**端到端的实时交易与套利框架**，超越了大多数研究仅侧重于情感分析或单一模型预测的范畴。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为PolySwarm的多智能体大语言模型框架来解决预测市场交易和延迟套利问题。其核心方法围绕**异构智能体群体、两阶段贝叶斯聚合以及信息论市场分析**展开。

**整体框架**：系统采用Python FastAPI后端与Vue 3前端，通过WebSocket进行实时通信。核心扫描循环以5秒为周期，从Polymarket获取活跃市场数据，经过过滤后触发群体评估。

**主要模块与关键技术**：
1.  **异构智能体池**：系统维护一个包含50个不同角色的LLM智能体池，涵盖宏观经济学家、技术分析师、逆向投资者、领域专家等。每个智能体通过思维链提示生成带有置信度的概率预测，这种设计确保了分析视角的多样性，为群体智慧效应奠定基础。
2.  **并行推理与协调机制**：采用**独立并行采样**作为协调机制。系统从池中采样一定数量（默认25个）的智能体，通过异步并发（asyncio）同时进行推理，智能体间不进行通信。这最大程度保持了预测的独立性，有利于在聚合时实现误差抵消。LLM响应缓存机制用于降低延迟和成本。
3.  **两阶段贝叶斯聚合**：这是核心创新点。首先，对个体智能体的预测进行**置信度加权平均**，得到群体共识概率 \( p_{swarm} \)。然后，将 \( p_{swarm} \) 与市场隐含概率 \( p_{market} \) 通过**线性贝叶斯混合**进行结合，生成最终组合概率 \( p_{combined} \)（默认权重为70%群体共识，30%市场价格）。这种设计既利用了群体的独立分析，又纳入了市场信息。
4.  **交易决策与执行**：基于 \( p_{combined} \) 计算交易的预期价值，仅当超过阈值且群体意见分歧度低时才触发交易。仓位大小遵循**四分之一凯利准则**进行风险控制。系统支持实盘交易（通过API）和模拟交易两种模式。
5.  **信息论市场分析引擎**：利用**KL散度和JS散度**来检测跨市场效率低下和否定对错误定价，为识别套利机会提供量化工具。
6.  **延迟套利模块**：通过对数正态定价模型从中心化交易所推导隐含概率，并利用Polymarket价格更新的延迟，在人类反应时间窗口内执行交易。

**创新点**：
*   **面向金融预测的异构多智能体架构**：专门设计了多样化的分析角色，并采用独立并行协调，以生成具有统计独立性的多样化预测。
*   **群体共识与市场信息的贝叶斯融合**：提出的两阶段聚合方法，在理论上有原则地结合了主观分析（群体）和客观信息（市场价格）。
*   **实时交易系统的完整实现**：将多智能体LLM预测与实际的预测市场交易引擎（包括风险管理和延迟套利）深度集成，构建了一个端到端的生产级系统。

### Q4: 论文做了哪些实验？

论文在Polymarket预测市场平台上进行了实时交易和延迟套利实验。实验设置方面，系统部署了包含50个多样化LLM角色的智能体池，默认每次评估从中采样25个角色，通过异步并发框架每5秒扫描一次市场数据，并采用置信度加权贝叶斯聚合方法将智能体共识与市场隐含概率结合，最终使用四分之一凯利准则进行仓位管理。

数据集与基准测试主要基于Polymarket的二元结果预测市场，通过其Gamma REST API获取实时市场数据。评估方法采用了Brier分数、校准分析和对数损失指标，并与人类超级预测者的表现进行基准比较。对比方法包括单模型基线以及多种多智能体框架（如AutoGen、CAMEL、AgentVerse等），论文特别比较了这些框架在智能体数量、协调机制、聚合方法、金融专注度、实时性和开源性等方面的差异。

主要结果显示，群体聚合方法在概率校准方面持续优于单模型基线。关键数据指标包括：聚合权重设置为群体共识70%、市场隐含概率30%；交易触发条件要求预期价值超过5%且群体标准差低于30%；系统在模拟交易模式下完整追踪虚拟仓位、盈亏和胜率。实验进一步证实，通过独立并行采样和两阶段贝叶斯聚合，系统能够有效利用群体智慧，在预测任务中实现更优的校准性能。

### Q5: 有什么可以进一步探索的点？

本文提出的PolySwarm框架在实时预测市场交易与延迟套利方面展现出潜力，但仍存在若干局限与可拓展方向。首先，系统依赖50个LLM代理的群体共识，但代理池可能产生“集体幻觉”或系统性偏差，未来可探索更精细的代理筛选机制或引入对抗性验证代理来提升鲁棒性。其次，计算成本随代理数量线性增长，在规模化部署时可能面临效率瓶颈，未来研究可考虑动态代理调度或轻量化模型集成以平衡性能与开销。此外，当前框架主要针对二元结果市场，未来可扩展至多选项或连续结果市场，并整合更多外部数据源（如新闻流、社交媒体情绪）以增强上下文感知。从方法论看，信息论引擎仅使用KL与JS散度，可引入更复杂的非线性度量或时序模型来捕捉市场动态。最后，监管与伦理风险（如反馈循环导致市场操纵）需建立模拟环境进行压力测试，并探索合规透明的交易决策解释机制。

### Q6: 总结一下论文的主要内容

本文提出了PolySwarm，一个新颖的多智能体大语言模型框架，专为去中心化预测市场的实时交易和延迟套利而设计。核心问题是利用LLM提升预测市场交易性能，同时克服单模型存在的幻觉、校准不佳等问题。

方法上，系统部署了50个具有不同角色的LLM智能体，并发评估二元结果市场。其核心贡献在于：1）采用置信度加权的贝叶斯聚合方法，将群体共识与市场隐含概率结合，并使用四分之一凯利公式进行风险控制下的头寸管理；2）设计了信息论市场分析引擎，利用KL散度和JS散度检测跨市场低效和否定对错误定价；3）实现了延迟套利模块，通过对数正态定价模型利用过时价格，在人类反应时间窗口内执行交易。

主要结论显示，在Polymarket预测任务中，群体聚合方法在概率校准上持续优于单模型基线。论文还系统评估了性能并讨论了智能体幻觉、计算成本、监管风险等开放挑战，为未来研究指明了方向。
