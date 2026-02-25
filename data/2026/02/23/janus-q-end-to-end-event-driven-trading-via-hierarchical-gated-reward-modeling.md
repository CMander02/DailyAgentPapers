---
title: "Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling"
authors:
  - "Xiang Li"
  - "Zikai Wei"
  - "Yiyan Qi"
  - "Wanyun Zhou"
  - "Xiang Liu"
  - "Penglei Sun"
  - "Yongqi Zhang"
  - "Xiaowen Chu"
date: "2026-02-23"
arxiv_id: "2602.19919"
arxiv_url: "https://arxiv.org/abs/2602.19919"
pdf_url: "https://arxiv.org/pdf/2602.19919v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "强化学习"
  - "决策"
  - "工具使用"
  - "多目标优化"
  - "事件驱动"
  - "金融交易"
relevance_score: 7.5
---

# Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling

## 原始摘要

Financial market movements are often driven by discrete financial events conveyed through news, whose impacts are heterogeneous, abrupt, and difficult to capture under purely numerical prediction objectives. These limitations have motivated growing interest in using textual information as the primary source of trading signals in learning-based systems. Two key challenges hinder existing approaches: (1) the absence of large-scale, event-centric datasets that jointly model news semantics and statistically grounded market reactions, and (2) the misalignment between language model reasoning and financially valid trading behavior under dynamic market conditions. To address these challenges, we propose Janus-Q, an end-to-end event-driven trading framework that elevates financial news events from auxiliary signals to primary decision units. Janus-Q unifies event-centric data construction and model optimization under a two-stage paradigm. Stage I focuses on event-centric data construction, building a large-scale financial news event dataset comprising 62,400 articles annotated with 10 fine-grained event types, associated stocks, sentiment labels, and event-driven cumulative abnormal return (CAR). Stage II performs decision-oriented fine-tuning, combining supervised learning with reinforcement learning guided by a Hierarchical Gated Reward Model (HGRM), which explicitly captures trade-offs among multiple trading objectives. Extensive experiments demonstrate that Janus-Q achieves more consistent, interpretable, and profitable trading decisions than market indices and LLM baselines, improving the Sharpe Ratio by up to 102.0% while increasing direction accuracy by over 17.5% compared to the strongest competing strategies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于学习的金融交易系统中，如何有效利用文本信息（特别是金融新闻事件）作为主要交易信号的核心难题。研究背景是，传统方法主要依赖历史价格、成交量等数值时间序列进行预测，但市场波动常由离散的、可解释的金融事件（如财报发布、并购）驱动，这些事件通过新闻传达，其影响具有异质性、突发性，且难以被纯数值预测目标捕捉。因此，学术界和业界日益关注将文本信息整合到交易系统中。

然而，现有方法存在两大不足。首先，缺乏大规模、以事件为中心的数据集，能够联合建模新闻语义和基于统计的市场反应（即事件驱动的累积异常收益）。现有数据集要么领域狭窄，要么标注粗糙，未能同时提供细粒度事件类型、关联股票、情感标签和量化的市场影响，导致模型难以区分经济上有意义的新闻与噪音，也无法学习事件到市场反应的异质性映射。其次，语言模型的语义推理与动态市场条件下的有效交易行为之间存在错位。语言模型可能生成流畅的新闻解读，但其语义判断未必与实际市场结果相符（例如，正面消息可能因预期已消化而引发价格回调），导致纯监督学习可能捕获表面相关性，而纯利润驱动的优化又容易产生利用短期噪音的虚假策略。

因此，本文要解决的核心问题是：如何构建一个端到端的事件驱动交易框架，将金融新闻事件从辅助特征提升为主要决策单元，以克服上述数据缺失和语义-市场错位的挑战，从而实现更一致、可解释且盈利的交易决策。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：事件驱动的市场分析、机器学习/深度学习方法在金融文本中的应用，以及基于大语言模型（LLM）的交易系统。

在**事件驱动的市场分析**方面，早期研究源于计量经济学和统计金融学，将离散事件视为外生冲击，并通过事件窗口内的异常收益动态进行分析。经典的事件研究法为此建立了标准工具包。随着文本信息的普及，后续研究开始纳入媒体情绪等定性信息，证明其能提供超越价格特征的市场信号。

在**机器学习/深度学习**方法中，研究趋势是从手工构建的情感指标转向直接从文本中学习事件语义。例如，Ding等人从新闻中提取结构化事件并学习其表示来建模对股价的影响；Wang等人提出的StockMem框架则利用事件的时间演化进行类比检索，以支持更可解释的预测。然而，现有方法仍以预测为导向，将事件主要作为输入，未能显式建模事件层面的属性（如历史背景、相对重要性）以支持面向决策的交易目标，且缺乏标准化的交易数据集。本文则构建了一个集成事件分类、情感标注和基于CAR事件影响评估的大规模数据集。

在**基于LLM的交易系统**方面，近期研究利用LLM处理非结构化文本和进行链式推理的能力。例如，Yang等人将指令微调的LLM用于金融分析和交易；Zhang等人提出了基于LLM的金融智能体FinAgent；Xiao等人研究了LLM驱动的多智能体交易框架，并后续工作Trading-R1应用强化学习来增强LLM的决策。Li等人提出的RETuning框架则通过反思和证据分析来改进推理。然而，现有LLM交易系统存在局限：一是交易决策往往不透明，文本信息与决策过程结合较弱；二是基于强化学习的方法通常依赖启发式、线性加和的奖励设计，难以建模有经济意义的权衡。本文提出的分层门控奖励模型（HGRM）旨在解决这些问题，将事件层面的语义推理与市场交易结果对齐。

### Q3: 论文如何解决这个问题？

论文通过一个名为Janus-Q的端到端事件驱动交易框架来解决所提出的挑战，该框架采用两阶段范式，统一了事件中心的数据构建和模型优化。

**整体框架与核心方法**：框架分为两个核心阶段。第一阶段专注于**事件中心的数据构建**，旨在创建大规模、高质量的金融新闻事件数据集。具体方法包括：1）基于经典事件研究法，通过“事件到累积异常收益（CAR）”建模量化事件的市场影响幅度；2）由六名领域专家对新闻进行细粒度事件类型、关联股票、情感等语义标注。CAR的计算经过两步处理：首先使用市场模型剔除大盘影响得到异常收益，再通过多因子风险模型进行风格/行业中性化，最终在事件窗口内累加得到纯净的事件驱动收益。每个事件被表示为包含CAR数值、事件类型、方向（由CAR符号决定）和交易强度（由CAR阈值决定）的标签元组。

第二阶段进行**决策导向的微调**，结合监督学习与强化学习，并引入**分层门控奖励模型（HGRM）** 这一关键技术来指导优化。训练先通过监督微调稳定模型的事件推理能力，再使用分组相对策略优化进行强化微调。HGRM的创新性在于其结构化、分层的奖励设计，它明确建模了多个交易目标之间的权衡：

1.  **方向硬门控**：首先设置方向门。若预测方向与真实方向相反，则施加重罚并阻断后续所有奖励，防止错误方向上的虚假盈利。
2.  **事件类型软门控**：预测事件类型正确则给予全额奖励；若错误或缺失，则施加惩罚，并通过一个折扣因子降低后续利润奖励的贡献，鼓励事件理解与交易决策的一致性。
3.  **利润奖励**：基于真实的CAR和交易成本计算单事件交易损益，但仅在预测交易强度为“强”时激活，并受事件类型折扣因子调节。
4.  **辅助奖励**：包括**幅度奖励**（鼓励CAR预测值接近真实值）和**过程奖励**（鼓励结构化的推理输出，惩罚冗长或无关内容）。
5.  **交易强度正则化**：对误判交易强度（该交易时不交易，不该交易时交易）施加不对称惩罚，防止模型退化为“永远交易”或“永不交易”的平庸策略。

最终奖励是上述分量的加权和，高层门控（如方向门）控制着低层奖励（如利润、幅度奖励）是否被激活。

**创新点**：1）构建了大规模、高质量、融合市场量化影响与语义标注的事件中心数据集；2）提出了HGRM，通过分层门控机制将事件语义理解、方向判断、交易强度决策与最终经济收益明确关联，系统性地解决了多目标权衡与对齐问题，从而引导模型做出更一致、可解释且盈利的交易决策。

### Q4: 论文做了哪些实验？

论文实验设置包括一个端到端的事件驱动交易策略，在给定股票池中，Janus-Q每日分析新闻事件并生成做多、做空或持有的信号，通过事件类型权重聚合信号，并在下一个交易日开盘时执行交易，持仓最多两个交易日后平仓。实验旨在回答四个研究问题，涵盖整体交易性能、核心组件贡献、多样化奖励目标的有效性以及与人类判断的一致性。

数据集整合了多源信息：从Datayes平台收集2023年1月1日至2025年1月25日的原始新闻文章，从Tushare获取对应股价数据进行回测（至2025年2月6日），并按4:4:1:1的比例按时间顺序划分为历史统计、训练、验证和测试集。此外，还从Wind平台引入公司概况（如行业类别和市场份额）以支持语义丰富。

对比方法分为四类：市场指数（如CSI 300、CSI 500、CSI 1000）、时间序列导向的LLM（如Time-MQA、ChatTS-14B、TimeMaster）、金融领域专用LLM（如FinMA、DISC-FinLLM、Stock-Chain）以及通用LLM（如QwQ-32B、Claude-3-Haiku、GPT-4o-mini、DeepSeek-v3.1-nex-n1等共7个模型）。

主要结果基于六项指标：Janus-Q在全部指标上优于所有基线。关键数据指标包括：方向准确率（DA）达0.5869，较最佳时间序列LLM、金融LLM和通用LLM基线分别提升17.5%、29.0%和22.4%；夏普比率（SR）为1.3088，较亚军QwQ-32B提升超过102.0%；平均绝对误差（MAE）为0.0349，较最佳时间序列模型降低18.3%。消融实验显示，移除监督微调导致性能大幅下降（DA降低超14%，SR转为负值），而移除分层门控奖励模型中的任一奖励目标均会降低性能，例如移除方向目标使DA下降4.8%，移除幅度或盈亏目标使SR分别降低约11.7%和8.7%。此外，在与人类判断对齐的评估中，Janus-Q在事件类型理解上与人类共识的平局率高达74.0%至83.0%，损失率低于5.0%，显示出较高的对齐度和解释性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从数据、模型和市场动态三方面展开。首先，数据层面，虽然构建了大规模事件数据集，但事件类型（10类）和覆盖范围（62,400篇文章）仍有限，未来可扩展至更多事件类别（如地缘政治、行业政策）和多语言新闻源，并引入非结构化数据（如财报电话会议音频）以提升事件表征的丰富性。其次，模型层面，Hierarchical Gated Reward Model（HGRM）虽能权衡多目标，但奖励函数的设计仍依赖人工设定，未来可探索基于逆强化学习自动从市场数据中推断潜在奖励结构，或引入因果推理模块以区分事件相关性与其实际因果影响。此外，框架对市场极端事件（如闪崩、流动性危机）的适应性未充分验证，需增强风险感知机制。最后，交易实践层面，论文未考虑高频交易场景、交易成本动态变化及监管约束，未来可结合多时间粒度决策（如事件冲击的短期vs长期效应）并模拟实盘摩擦因素，以提升部署可行性。

### Q6: 总结一下论文的主要内容

该论文提出了Janus-Q，一个端到端的事件驱动交易框架，旨在解决基于新闻事件进行量化交易的两个核心挑战：缺乏大规模、事件中心的数据集，以及语言模型推理与动态市场条件下有效交易行为之间的错配。其核心贡献在于构建了一个两阶段范式。第一阶段专注于事件中心数据构建，创建了一个包含62,400篇文章的大规模金融新闻事件数据集，标注了细粒度事件类型、关联股票、情感标签和事件驱动的累计异常收益。第二阶段进行决策导向的微调，结合监督学习和由分层门控奖励模型指导的强化学习，该模型明确捕捉了多个交易目标之间的权衡。主要结论表明，Janus-Q相比市场指数和大型语言模型基线，能做出更一致、可解释且盈利的交易决策，将夏普比率提升高达102.0%，方向预测准确率提升超过17.5%，验证了将新闻事件作为主要决策单元的有效性。
