---
title: "Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks"
authors:
  - "Kunihiro Miyazaki"
  - "Takanobu Kawahara"
  - "Stephen Roberts"
  - "Stefan Zohren"
date: "2026-02-26"
arxiv_id: "2602.23330"
arxiv_url: "https://arxiv.org/abs/2602.23330"
pdf_url: "https://arxiv.org/pdf/2602.23330v1"
categories:
  - "cs.AI"
  - "q-fin.TR"
tags:
  - "Multi-Agent System"
  - "Financial Trading"
  - "Task Decomposition"
  - "LLM Application"
  - "Decision-Making"
  - "System Design"
relevance_score: 8.0
---

# Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks

## 原始摘要

The advancement of large language models (LLMs) has accelerated the development of autonomous financial trading systems. While mainstream approaches deploy multi-agent systems mimicking analyst and manager roles, they often rely on abstract instructions that overlook the intricacies of real-world workflows, which can lead to degraded inference performance and less transparent decision-making. Therefore, we propose a multi-agent LLM trading framework that explicitly decomposes investment analysis into fine-grained tasks, rather than providing coarse-grained instructions. We evaluate the proposed framework using Japanese stock data, including prices, financial statements, news, and macro information, under a leakage-controlled backtesting setting. Experimental results show that fine-grained task decomposition significantly improves risk-adjusted returns compared to conventional coarse-grained designs. Crucially, further analysis of intermediate agent outputs suggests that alignment between analytical outputs and downstream decision preferences is a critical driver of system performance. Moreover, we conduct standard portfolio optimization, exploiting low correlation with the stock index and the variance of each system's output. This approach achieves superior performance. These findings contribute to the design of agent structure and task configuration when applying LLM agents to trading systems in practical settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的自主金融交易系统中，由于任务设计过于粗略而导致的性能下降和决策过程不透明的问题。研究背景是，随着LLM的快速发展，多智能体系统被广泛应用于金融投资领域，通常通过模拟分析师、经理等角色来构建交易系统。然而，现有主流方法往往只给智能体分配抽象的角色和高层目标（例如，简单地指令一个基本面分析智能体“分析财务报表”），这种粗粒度的任务设置忽略了现实世界投资分析工作流程的复杂性。这种简化设计带来两大挑战：一是性能退化，过于模糊的指令会降低LLM的输出质量，甚至在处理复杂任务时可能导致推理中断或放弃；二是缺乏可解释性，模糊指令下通常只能看到最终输出，无法理解中间推理过程，这在涉及重大资金的资产管理实践中难以实际部署。

因此，本文要解决的核心问题是：如何通过改进多智能体LLM交易系统中的任务设计，以提升其投资性能和决策透明度。具体而言，论文提出构建一个多智能体LLM交易框架，该框架不是提供粗粒度的指令，而是依据真实投资分析师的实际工作实践，将投资分析过程显式地分解为一系列细粒度的具体任务。论文通过实验验证这种细粒度任务分解是否能带来性能提升，并分析其对智能体推理行为和输出可解释性的影响，最终通过投资组合优化来证明其在现实场景中的适用性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体交易系统结构设计、基于强化学习的优化方法，以及任务分解与专家流程编码。

在多智能体交易系统结构方面，现有研究主要采用“经理-分析师”架构，通过角色分工处理异构金融信息（如Xiao等人、Yu等人、Xiong等人的工作）。这些工作侧重于模仿真实投资团队的组织形式和交互，但通常使用较为粗粒度的指令来定义角色任务，未与真实投资流程的细粒度任务明确对齐。本文则在此基础上，进一步细化了每个角色的提示设计，使其更贴近实际投资机构的专业分工，旨在提升系统的可控性和决策可解释性。

在优化方法上，另一类研究聚焦于利用强化学习技术（如反思机制、分层记忆架构）来迭代改进决策策略。本文的研究重点与之不同，主要集中于前述的结构与角色设计范畴，并未采用强化学习进行策略优化。

在任务分解与流程编码方面，近期LLM研究（如MetaGPT、Agent-S框架）表明，将标准操作程序（SOP）或“先计划后执行”等范式编码到多智能体系统中，能提升复杂任务的表现。在金融领域，FinRobot提出的金融思维链（CoT）提示通过预定义分析章节来引导推理，与本文思路有相似之处。但本文与之关键区别在于：1）将专家工作流程形式化为固定的分析协议，而非通用的CoT提示；2）核心目标是驱动可操作的交易决策，而非仅生成分析报告；3）分析范围更广，整合了公司层面、宏观经济和行业信息等多重因素。

### Q3: 论文如何解决这个问题？

论文通过构建一个细粒度任务分解的多智能体LLM交易框架来解决传统方法因指令抽象而导致的推理性能下降和决策不透明问题。其核心方法是：将投资分析过程明确分解为多个专业化的细粒度任务，并为每个智能体设计具体、可操作的分析指令，而非笼统的宏观指导。

整体框架包含七个专门化的智能体，它们协同工作：技术分析智能体和量化分析智能体是直接产生投资执行信号的核心，论文对它们进行了细粒度与粗粒度任务的对比实验。此外，还有文本分析智能体、新闻分析智能体、行业分析智能体、宏观分析智能体以及投资组合经理（PM）智能体。

在架构设计上，系统采用分层与汇总的工作流。底层的四个“分析师”智能体（技术、量化、文本、新闻）并行处理不同维度的数据（价格、财报、文本报告、新闻），并输出评分和推理文本。行业分析智能体负责横向比较与整合前四个智能体的输出，形成行业层面的观点。宏观分析智能体则独立分析经济指标，提供自上而下的市场环境评估。最终，PM智能体综合自下而上（行业观点）和自上而下（宏观观点）的信息，生成每只股票的最终吸引力评分，用于构建多空投资组合。

关键技术细节与创新点主要体现在：
1.  **细粒度任务定义**：为核心智能体提供符合专业分析师日常操作标准的具体任务。例如，技术分析智能体不再直接处理原始价格数据，而是接收预先计算并标准化的一系列技术指标（如动量、波动率、振荡器），包括不同周期的价格变化率、布林带Z值、MACD、RSI、KDJ等。量化分析智能体则接收基于财务分析经典文献计算好的五大维度指标（盈利能力、安全性、估值、效率、成长性），而非原始的财务报表行项目数据。
2.  **数据规范化与时效性处理**：对所有输入指标进行标准化或比率调整以消除价格水平偏差；对流量财务指标使用滚动十二个月数据以减少季节性影响，对存量指标使用最新季度数据确保及时性；明确处理缺失数据（输入NaN并依赖LLM处理）。
3.  **促进分析与决策对齐**：论文通过分析中间智能体输出发现，细粒度任务分解的关键优势在于使上游分析输出（如具体的指标评分）更易于与下游投资决策偏好（如PM智能体的整合逻辑）对齐，这是提升系统性能的关键驱动因素。
4.  **系统输出优化**：在得到各系统的股票吸引力评分后，论文进一步利用不同系统输出之间的低相关性以及各自输出的方差，进行标准的投资组合优化，从而实现了更优的绩效表现。

总之，该方法的创新性在于将实际金融工作流程中的标准分析任务编码为智能体的具体指令，通过精细化的任务分解与专业的数据预处理，提升了多智能体系统的分析质量、决策透明度及最终的投资绩效。

### Q4: 论文做了哪些实验？

论文的实验设置基于日本TOPIX 100成分股，数据涵盖2023年9月至2025年11月的股价、财务报表、新闻和宏观信息，并在严格控制信息泄露的回测环境下进行。主要对比方法是提出的细粒度任务分解多智能体系统与传统的粗粒度指令系统。实验评估了不同投资组合规模（N ∈ {10, 20, 30, 40, 50}，即做多和做空各N/2只股票）下的表现。

主要结果方面，细粒度系统在风险调整后收益（夏普比率）上显著优于粗粒度基线。具体数据显示，在投资组合规模为20、30、40和50时，细粒度系统的夏普比率提升具有统计显著性（p值<0.0001, 0.001, 0.05），例如在N=50时，细粒度比粗粒度的夏普比率中位数高出0.26。仅N=10时差异不显著。留一法（Leave-one-out）实验表明，细粒度架构在大多数配置下仍保持优势，但移除技术分析智能体（Technical Agent）会导致较大投资组合下性能反转，突显其关键作用。消融研究进一步量化了各智能体的贡献：在细粒度设置下，移除技术分析智能体通常导致夏普比率大幅下降（例如N=50时下降0.66），而移除其他智能体（如定量、定性）常带来小幅提升或噪声。此外，通过分析智能体输出的文本相似性发现，细粒度设置显著提升了技术分析信息向上层（如行业分析智能体）的语义传播效率（余弦相似度提升0.022），这与回测结果一致。最后，论文通过组合六种智能体策略（全智能体及五种留一策略）进行投资组合优化，利用其与股票指数的低相关性及策略间输出的异质性，实现了更优的绩效。

### Q5: 有什么可以进一步探索的点？

该论文在任务细化和多智能体协作方面取得了进展，但仍存在一些局限性和可探索的方向。首先，实验数据局限于日本股市，其市场特性和信息环境可能与其他市场（如A股或美股）存在差异，未来需在更广泛的市场中进行验证以检验泛化能力。其次，系统依赖历史数据进行回测，但实际交易中市场机制、流动性冲击和交易成本等因素更为复杂，需进一步融入实时市场微观结构仿真。此外，虽然细粒度任务分解提升了透明度，但智能体间的决策对齐机制仍较为隐式，未来可引入强化学习或因果推断方法显式优化分析输出与投资偏好的协同。最后，当前框架未充分探索多模态信息（如财报图表、管理层演讲视频）的融合，整合视觉或语音模型可能挖掘更深层的市场信号。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于大语言模型的多智能体金融交易框架，其核心贡献在于通过细粒度任务分解来提升投资决策的透明度和绩效。针对现有方法通常依赖粗粒度指令、忽视真实工作流程细节而导致推理性能下降和决策不透明的问题，本文设计了一个将投资分析明确分解为多个精细任务的多智能体系统。

方法上，该框架利用日本股市数据（包括价格、财务报表、新闻和宏观信息），在严格控制数据泄露的回测环境中进行评估。实验结果表明，与传统的粗粒度设计相比，细粒度的任务分解能显著提高风险调整后收益。关键分析发现，智能体中间分析输出与下游决策偏好之间的对齐是驱动系统性能的关键因素。

此外，研究通过标准的投资组合优化，利用系统输出与股指的低相关性及其方差，进一步实现了卓越的投资表现。这些发现为在实际场景中应用LLM智能体构建交易系统时的智能体结构设计与任务配置提供了重要见解。
