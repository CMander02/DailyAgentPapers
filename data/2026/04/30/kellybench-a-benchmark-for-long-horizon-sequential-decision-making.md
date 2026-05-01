---
title: "KellyBench: A Benchmark for Long-Horizon Sequential Decision Making"
authors:
  - "Thomas Grady"
  - "Kip Parker"
  - "Iliyan Zarov"
  - "Henry Course"
  - "Chengxi Taylor"
  - "Ross Taylor"
date: "2026-04-30"
arxiv_id: "2604.27865"
arxiv_url: "https://arxiv.org/abs/2604.27865"
pdf_url: "https://arxiv.org/pdf/2604.27865v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Long-Horizon Decision Making"
  - "Sequential Decision Making"
  - "Sports Betting"
relevance_score: 9.0
---

# KellyBench: A Benchmark for Long-Horizon Sequential Decision Making

## 原始摘要

Language models are saturating benchmarks for procedural tasks with narrow objectives. But they are increasingly being deployed in long-horizon, non-stationary environments with open-ended goals. In this paper we introduce KellyBench, an environment for evaluating sequential decision-making in sports betting markets. Agents are placed in a sequential simulation of the 2023-24 English Premier League season and tasked with maximising their long-term bankroll growth. They are given detailed historical data, including advanced statistics, lineups, and public odds. To succeed they must build machine learning models, identify edge in public markets, and adapt as the environment changes over time. We find that all frontier models evaluated lose money on average over the course of the season for five seeds. The best performing model achieves an average return of -8%, and many models experiencing ruin across seeds. To judge strategy sophistication, we use a human expert rubric to grade each model and find their approaches to be unsophisticated compared to human baselines; Claude Opus 4.6 achieves a rubric score of 26.5%, which means there is significant room for improvement. KellyBench is available as an open-access API endpoint at https://openreward.ai/GeneralReasoning/KellyBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文旨在解决当前语言模型评估中缺乏对真实世界复杂决策能力测试的问题。研究背景是，现有的大多数基准测试（如terminalbench2）都聚焦于静态环境、明确任务和稀疏反馈，例如让模型实现特定算法。然而，现实中智能体需要在非平稳、目标开放的环境中做出长期序列决策，例如体育博彩市场。现有方法存在明显不足：它们无法衡量模型从经验中学习、构建和修正模型、以及在不确定性和变化中适应和盈利的能力。这种静态评估忽略了现实世界中的非平稳性和风险管理的挑战，导致模型的真实决策能力被高估。本文的核心问题是：当前最先进的语言模型是否能够在开放、非平稳、数据丰富的环境中，通过持续学习和策略优化实现长期盈利？为了回答这个问题，论文提出了KellyBench，一个基于2023-24赛季英超联赛数据的体育博彩市场模拟环境，要求模型管理资金、构建预测模型、识别市场错误定价，并在整个赛季中最大化资金增长。评估结果显示，所有模型平均都亏损，最佳模型（GPT-5.4）的平均回报率为-8%，而人类专家的策略复杂性评分远高于模型（如Claude Opus 4.6仅得26.5%），表明当前模型在长期序列决策能力上存在显著短板。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **方法类**：本文继承了Kelly准则（Kelly, 1956）和Ed Thorp、Bill Benter在赌博与金融中的实践，强调信息优势转化为资本增长。与这些经典工作相比，KellyBench不只是验证凯利公式本身，而是要求智能体自主构建模型、识别市场边际、并持续调整策略。此外，动态状态空间模型（如动态泊松模型、贝叶斯状态空间模型）被用于处理非平稳性，而xG模型等高级统计指标也构成特征工程的重要部分。KellyBench整合了这些方法，但测试的是端到端的顺序决策能力，而非单独建模。

2. **评测类**：与MLE-Bench（Kaggle竞赛评测）、MLGym（开放研究任务）、PostTrainBench（后训练评测）等不同，KellyBench的环境是非平稳的、特征空间庞大，并且要求在顺序决策中落地模型。与ForecastBench、FutureX等预测评测相比，KellyBench聚焦于大量结构相似事件的重复决策，能更系统地检验模型是否一致地将边际转化为长期收益，而不仅仅是单次预测精度。

3. **应用类**：金融交易评测如PyMarketSim、MarS、FinRL、StockBench、AI-Trader等，通常面临时间泄漏或信息集不完整的问题。KellyBench通过提供时间戳化的赛前信息（如阵容、统计数据、赔率），在保持开放探索的同时避免了完全重建互联网信息的难度，处于更实际和可复现的中间地带。

### Q3: 论文如何解决这个问题？

本论文通过设计一个名为 KellyBench 的基准测试环境，来解决评估语言模型在长时序、非平稳且目标开放环境下的顺序决策能力的问题。核心方法是构建一个模拟真实体育博彩市场的顺序决策框架，要求智能体在2023-24赛季的英超模拟中进行长期本金增长。

整体架构基于Open Reward Standard (ORS)协议，将环境、任务和工具封装为可访问的API。环境模拟整个赛季（约100-150个比赛日），智能体在每个比赛日遵循固定的交互循环：获取观察（当前赛程和博彩公司赔率）、在沙盒计算环境中开发模型（读写文件、训练ML模型）、下注（五种博彩类型），以及结算并更新数据。关键技术包括：
1. **递进式数据披露**：智能体在季初只获得历史数据（1993-94赛季起），每轮比赛后动态更新最新的比赛结果和球员统计数据，模拟真实信息结构。
2. **工具集设计**：提供两类工具——环境工具（如view_matches、place_bet）用于与博彩世界交互，以及CLI工具（如bash、write、edit）用于在沙盒中开发机器学习模型（支持NumPy、pandas、scikit-learn）。
3. **密集可验证奖励**：使用对数财富变化作为即时奖励信号（r_t = log(W_{t+1}/W_t)），这与Kelly准则直接关联，能最大化长期几何增长率。奖励完全由比赛结果和赔率确定，无需LLM评判器。
4. **防数据泄露机制**：通过阻断沙盒网络访问、明确要求基于规则的策略、以及监控智能体行为远离直觉性下注，防止权重记忆或在线信息导致作弊。例如，明确告知智能体若不遵循规则策略将被禁赛，且观察到的轨迹显示模型确实遵守了这些约束。

创新点在于将金融投资中的Kelly准则与体育博彩市场结合，构建了一个可验证、长时域且带动态数据披露的基准，能够评估模型在非平稳环境中自适应构建预测模型和优化策略的能力。实验表明，当前最前沿的LLM在此环境下平均亏损8%，且策略复杂度远低于人类专家（Claude Opus 4.6得分仅26.5%）。

### Q4: 论文做了哪些实验？

在论文中，作者通过在KellyBench基准上评估多个前沿模型来测试其长期序贯决策能力。实验设置采用2023-24赛季英超联赛为期120个比赛日的完整模拟，初始银行roll为10万英镑（标准化后）。数据集包含1993-94赛季以来的历史比赛数据（球队、比分、赔率等）以及2008年以来的球员级别数据（如xG、助攻等），测试场景为最近赛季。对比方法包括Claude Opus 4.6、GPT-5.4等前沿语言模型，并在同一测试场景中设置文献变体（提供30+篇体育预测论文）。主要结果：所有模型在整个赛季中平均亏损，表现最佳模型的平均回报率为-8%（五轮种子平均值），许多模型遭遇破产。Claude Opus 4.6在人类专家评分中仅获26.5%的评分，表明策略不够成熟。作者还进行了消融实验：文献变体中提供研究论文可略微提升模型性能，但总体表现仍不理想。关键指标包括累计对数财富收益（最终与初始银行roll的比值对数）和专家评分（基于策略复杂度、模型开发能力等维度）。实验揭示当前模型在动态、非平稳环境下的长序决策能力显著不足。

### Q5: 有什么可以进一步探索的点？

首先，KellyBench的评估主要基于单一赛季的固定种子，未来研究可扩展至多赛季、动态赔率调整及市场参与者行为变化，以测试模型的泛化性和鲁棒性。其次，当前前沿模型表现不佳，平均回报为-8%，策略得分仅26.5%，表明模型在构建预测模型、识别市场“边缘”和适应非平稳环境方面存在明显局限。未来可探索将强化学习与在线学习结合，设计能动态调整下注策略的智能体，例如使用元学习或贝叶斯优化来实时更新模型参数。此外，可引入多模态数据（如新闻情绪、伤病报告）并开发因果推理模块，以区分真实信号与噪声。最后，本任务的“开放目标”特性（最大化长期增长）与人类专家的直觉策略差异显著，改进方向可包括模仿学习人类专家策略，或使用逆强化学习提取隐含的决策奖励函数，从而提升智能体的决策复杂度与长期收益。

### Q6: 总结一下论文的主要内容

KellyBench是一个用于评估语言模型在长期、非平稳环境中进行序贯决策能力的基准测试，具体任务是在体育博彩市场中最大化长期资金增长。问题定义为：代理需模拟2023-24赛季英超联赛，基于历史数据（包括高级统计、阵容和公开赔率）进行投注。方法上，代理需构建机器学习模型、识别市场优势并适应环境变化。主要结论是：所有前沿模型（如GPT-5.4）在五个随机种子下平均亏损，最佳模型平均回报率为-8%，多个模型出现破产；仅有3/25个种子实现正收益，但跨种子平均仍为负值。人类专家对模型策略的评分显示，表现最好的Claude Opus 4.6仅得26.5%，表明策略缺乏复杂性。该基准的核心贡献在于揭示了当前模型在动态、开放目标环境中的能力局限，并倡导评估从固定任务向复杂、需经验学习的世界转变。KellyBench作为开放API提供，强调了显著改进空间。
