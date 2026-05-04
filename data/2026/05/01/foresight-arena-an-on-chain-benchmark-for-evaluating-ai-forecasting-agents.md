---
title: "Foresight Arena: An On-Chain Benchmark for Evaluating AI Forecasting Agents"
authors:
  - "Maksym Nechepurenko"
  - "Pavel Shuvalov"
date: "2026-05-01"
arxiv_id: "2605.00420"
arxiv_url: "https://arxiv.org/abs/2605.00420"
pdf_url: "https://arxiv.org/pdf/2605.00420v1"
github_url: "https://github.com/foresight-arena/contracts"
categories:
  - "cs.MA"
  - "cs.LG"
  - "q-fin.GN"
tags:
  - "LLM Agent"
  - "AI Forecasting Agent"
  - "Benchmark"
  - "On-chain Evaluation"
  - "Prediction Markets"
  - "Brier Score"
  - "Alpha Score"
relevance_score: 7.5
---

# Foresight Arena: An On-Chain Benchmark for Evaluating AI Forecasting Agents

## 原始摘要

Evaluating the true forecasting ability of AI agents requires environments resistant to overfitting, free from centralized trust, and grounded in incentive-compatible scoring. Existing benchmarks either rely on static datasets vulnerable to training-data contamination, or measure trading PnL -- a metric conflating predictive accuracy with timing, sizing, and risk appetite. We introduce Foresight Arena, the first permissionless, on-chain benchmark for evaluating AI forecasting agents on real-world prediction markets. Agents submit probabilistic forecasts on binary Polymarket markets via a commit-reveal protocol enforced by Solidity smart contracts on Polygon PoS; outcomes are resolved trustlessly through the Gnosis Conditional Token Framework. Performance is measured by the Brier Score and a novel Alpha Score -- proper scoring rules that incentivize honest probability reporting and isolate predictive edge over market consensus. We provide a formal analysis: closed-form variance for per-market Alpha, the connection to Murphy's classical Brier decomposition, and a power analysis characterizing the number of rounds required to reliably distinguish agents of different skill levels. We show that detecting a true edge of $α^* = 0.02$ at 80% power requires approximately 350 resolved binary predictions (50 rounds of 7 markets), while $α^* = 0.01$ requires four times more. We complement these analytical results with a 50-round live evaluation of five frontier LLM agents plus a random baseline. Murphy decomposition distinguishes well-calibrated agents from market-tracking agents that fail through reduced resolution. All smart contracts and evaluation infrastructure are open-source.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有AI预测智能体评估框架中的三个核心问题。首先，传统静态基准数据集容易受到训练数据污染，模型可能因为预训练中遇到过类似问题而表现良好，而非真正具备预测能力。其次，现有评估系统大多依赖中心化信任，需要信任中央机构诚实地记录预测、正确评分并防止结果被事后篡改，这在商业场景中尤其成问题。第三，近期工作使用交易损益（PnL）来评估智能体，但PnL将预测准确性与市场时机、头寸规模和风险偏好混为一谈，无法准确衡量预测能力。论文提出的Foresight Arena是一个无需许可、基于链上智能合约的评估基准，通过Polygon PoS上的commit-reveal协议和Gnosis条件代币框架实现信任最小化，并使用严格适当的Brier分数和新颖的Alpha分数来评估预测能力，从而隔离出纯粹的预测边缘，解决了数据污染、中心化信任和评估指标不当三大问题。

### Q2: 有哪些相关研究？

相关研究可分为几类。在**评估方法类**中，早期工作如Halawi等人发现GPT-4在实时预测问题上未能显著优于50%基线；随后研究表明通过检索增强和集成可提升性能，Schoenegger等人的“硅谷人群”证明12个LLM集成在三周内可达到925名人类预测者的水平。Zou等人提出的ForecastBench是持续更新的基准测试，前沿模型在提供市场预测时的Brier分数约0.122（无此信息时为0.136），而人类超级预测者为0.096。本文与这些工作的核心区别在于：Foresight Arena将评估从被动概率估计扩展到竞争性多智能体评估，且从中心化记录转向链上可验证性。

在**市场与机制类**中，预测市场研究（如Iowa电子市场）验证了其作为信息聚合机制的有效性；LMSR为Polymarket等平台提供了理论基础。本文利用Polymarket作为问题来源和基准概率，但不同于Zhang等人的Prediction Arena（用真实资本交易，发现所有模型在Kalshi亏损），Foresight Arena通过适当评分规则分离预测与交易成分。

在**评分理论类**中，Brier分解、Murphy的校准与分辨力分析、以及技能分数概念构成了本文Alpha Score的理论基础。Foresight Arena位于评估空间的独特位置：完全去中心化且使用适当评分规则，区别于仅使用PnL或中心化数据集的现有工作。

### Q3: 论文如何解决这个问题？

Foresight Arena通过一个去中心化、激励兼容的链上基准测试框架来解决AI预测智能体评估中的过拟合、中心化信任和指标混杂问题。整体框架基于Polygon PoS链上的Solidity智能合约，结合Gnosis条件代币框架（CTF）作为去中心化预言机，确保结果解析的信任最小化。

核心机制是提交-揭示（commit-reveal）协议：智能体在知道结果前将预测概率向量p和随机数salt的keccak256哈希提交上链，截止后揭示原始数据并由合约验证哈希匹配，防止预测被篡改或互相窥探。性能评估采用两种严格正确的评分规则：Brier Score衡量预测概率与二元结果的平方误差，其期望值仅在报告真实信念时最小化；创新性的Alpha Score定义为市场基准Brier Score与智能体Brier Score之差，正数表示优于市场共识，避免了传统PnL指标将预测能力与仓位大小和风险偏好混为一谈的问题。

关键技术包括Murphy分解法（将Brier得分分解为不确定性、可靠性和分辨率）来区分校准良好的智能体与单纯追踪市场的智能体；以及基于每个市场Alpha方差的闭合形式推导（与|b-p|和结果方差相关）和功效分析，显示检测α*=0.02的真实边缘需要约350个预测（50轮，每轮7个市场）。所有合约和基础设施均开源，并通过无gas中继器降低参与门槛。

### Q4: 论文做了哪些实验？

论文在 Foresight Arena 平台上进行了50轮（共350个市场）的实时评估实验。实验数据选自 Polymarket 上过去24小时交易量最高且趋势活跃的二元预测市场，确保流动性充足且话题时效性强。对比方法包括5个前沿 LLM agent（如 GPT-4、Claude 等）和一个随机基线。主要评估指标是 Brier Score 和 Alpha Score，后者通过隔离市场共识来反映预测边际优势。关键结果：Murphy 分解显示，最前沿的 agent 能实现良好校准（高分辨率），而市场跟随型 agent 虽校准但不具分辨率，导致表现差。检测显著优势所需轮数：α*=0.02 需350个市场（50轮×7个），α*=0.01 需1400个。实验所有智能合约和评估基础设施已开源。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向主要包括：当前基准仅依赖二元预测市场，未考虑多类别或连续型预测场景，可扩展至更复杂的预测类型（如事件概率密度估计）。其次，Alpha得分虽能分离预测优势，但其方差依赖于市场共识波动性，未来可设计自适应轮次分配策略以降低高波动市场的采样噪声。此外，合约的Gas成本与延迟可能影响高频预测策略的实用性，可探索Layer2扩容方案或zk-Rollup优化。值得关注的改进方向包括：引入动态奖惩机制（如基于信息熵的加权评分）以抑制“搭便车”行为，以及构建跨市场预测迁移性测评框架（如领域自适应评估）。另外，当前五类LLM代理仅体现基础能力，可系统分析不同模型结构（如MoE、强化学习微调）与记忆机制（如检索增强生成）对校准性能的影响。最终，开发可解释性工具（如归因分析）来诊断过度拟合与虚假相关性将提升基准的科研价值。

### Q6: 总结一下论文的主要内容

Foresight Arena 提出了首个无许可的链上基准测试，用于评估AI预测代理在现实世界预测市场中的表现。现有基准面临三大局限：静态数据集易受训练数据污染、依赖中心化信任、以及使用交易损益（PnL）这种将预测精度与时机、仓位和风险偏好混淆的评估指标。该论文通过结合Polygon PoS上的Solidity智能合约实现的提交-揭示协议和Gnosis条件代币框架的无信任结果解析，构建了抗过拟合、去中心化且激励兼容的评估环境。性能评估采用Brier评分和创新的Alpha评分，这些严格适当的评分规则能激励诚实概率报告并分离出相对于市场共识的预测优势。论文提供了正式分析，包括每个市场Alpha的闭式方差、与Murphy经典Brier分解的联系，以及用于区分不同能力水平代理所需轮次的功效分析。结果表明，在80%功效下检测到的真实优势需要约350个已解析的二元预测。50轮实时评估对五个前沿LLM代理加随机基线进行了对比，Murphy分解能有效区分校准良好的代理与仅追踪市场的代理。所有智能合约和基础设施均已开源，使评估可独立验证。
