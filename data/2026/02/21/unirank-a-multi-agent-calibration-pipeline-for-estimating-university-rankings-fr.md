---
title: "UniRank: A Multi-Agent Calibration Pipeline for Estimating University Rankings from Anonymized Bibliometric Signals"
authors:
  - "Pedram Riyazimehr"
  - "Seyyed Ehsan Mahmoudi"
date: "2026-02-21"
arxiv_id: "2602.18824"
arxiv_url: "https://arxiv.org/abs/2602.18824"
pdf_url: "https://arxiv.org/pdf/2602.18824v1"
categories:
  - "cs.SI"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "LLM 管道"
  - "工具增强"
  - "校准"
  - "基准/评测"
  - "推理"
  - "数据合成"
relevance_score: 7.5
---

# UniRank: A Multi-Agent Calibration Pipeline for Estimating University Rankings from Anonymized Bibliometric Signals

## 原始摘要

We present UniRank, a multi-agent LLM pipeline that estimates university positions across global ranking systems using only publicly available bibliometric data from OpenAlex and Semantic Scholar. The system employs a three-stage architecture: (a) zero-shot estimation from anonymized institutional metrics, (b) per-system tool-augmented calibration against real ranked universities, and (c) final synthesis. Critically, institutions are anonymized -- names, countries, DOIs, paper titles, and collaboration countries are all redacted -- and their actual ranks are hidden from the calibration tools during evaluation, preventing LLM memorization from confounding results. On the Times Higher Education (THE) World University Rankings ($n=352$), the system achieves MAE = 251.5 rank positions, Median AE = 131.5, PNMAE = 12.03%, Spearman $ρ= 0.769$, Kendall $τ= 0.591$, hit rate @50 = 20.7%, hit rate @100 = 39.8%, and a Memorization Index of exactly zero (no exact-match zero-width predictions among all 352 universities). The systematic positive-signed error (+190.1 positions, indicating the system consistently predicts worse ranks than actual) and monotonic performance degradation from elite tier (MAE = 60.5, hit@100 = 90.5%) to tail tier (MAE = 328.2, hit@100 = 20.8%) provide strong evidence that the pipeline performs genuine analytical reasoning rather than recalling memorized rankings. A live demo is available at https://unirank.scinito.ai .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决全球大学排名系统依赖昂贵、部分专有且方法不透明的数据（如调查数据、机构自报数据）的问题，这导致排名覆盖范围有限（仅约1500所大学，而全球有超过3万所高等教育机构），且缺乏可验证性。为此，论文提出了一个核心研究问题：能否仅利用公开可得的文献计量数据（来自OpenAlex和Semantic Scholar），通过一个多智能体大语言模型（LLM）管道来估算大学的排名位置，而无需依赖调查数据、声誉信号或专有机构数据？这一方法的关键创新在于通过严格的匿名化（隐藏机构名称、国家、论文标题等所有识别信息）和数据隐藏（在评估时从排名数据存储中移除目标大学）技术，防止LLM直接记忆或回忆已知排名，从而迫使模型进行真正的分析推理，而非依赖记忆。论文的目标是开发一个既透明又基于公开数据的排名估算系统，以提供更广泛、可复现的排名洞察。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及四个领域。在大学排名系统方面，已有QS、THE和ARWU等主流排名，它们的方法论差异显著（如声誉调查与硬性研究指标的权重不同），这为本文构建一个不依赖特定排名方法、仅从文献计量信号进行估计的系统提供了动机。

在文献计量学与科学计量学方面，本文依赖OpenAlex和Semantic Scholar等开放数据库提供的海量学术数据，并使用了h指数、领域加权引用影响力（FWCI）等经典指标作为特征输入。

在大语言模型（LLM）应用于知识密集型任务方面，相关工作为本文的多智能体管道架构提供了直接基础。例如，ReAct和Toolformer展示了LLM使用工具进行推理的能力；AutoGen、CAMEL和MetaGPT等多智能体框架证明了任务分解与协作的有效性。特别是MAgICoRe框架，其“多智能体、迭代式、由粗到精”的优化思想，直接启发了本文的三阶段校准流程设计。

在LLM评估与数据去污染方面，针对LLM可能记忆训练数据并导致评估失真的风险，已有研究提出了n-gram过滤等技术。本文的创新在于采取了输入层面的匿名化策略，通过完全抹去机构身份信息，从根本上杜绝了模型通过记忆“走捷径”的可能性，这是对现有去污染方法的一种有效补充。

### Q3: 论文如何解决这个问题？

UniRank 通过一个精心设计的三阶段多智能体LLM流水线来解决仅基于匿名化文献计量数据估算大学排名的问题，其核心在于强制模型进行真正的分析推理，而非依赖记忆。整个架构围绕数据匿名化和信息隐藏构建，确保评估的纯净性。

**核心方法与架构设计：**
系统采用三阶段递进式架构。**第一阶段（初始零样本估计）**：LLM接收完全匿名化的大学文献计量特征向量（共16个指标，如h指数、国际合作率、影响力引用比率等），这些指标已进行归一化和Z分数转换。模型在此阶段无法使用任何工具，仅能基于对各排名体系（如THE、QS、ARWU）方法论的理解和提供的统计信号，为每个系统生成一个粗略的排名范围估计。这迫使模型进行基础的跨指标推理。

**第二阶段（按系统并行校准）**：这是多智能体设计的核心。三个独立的校准引擎（每个对应一个排名系统）并行运行。每个引擎被赋予两个关键工具：1) `get_ranking_samples`：获取指定排名范围内的真实大学样本及其官方子分数，但在评估时，目标大学会从返回的样本集中被隐藏，防止数据泄露；2) `compute_metrics`：计算给定名称大学的完整文献计量指标集，以便与匿名目标进行直接比较。每个引擎通过最多12个智能体步骤（获取样本、计算指标、比较、调整）进行迭代式校准，最终输出一个更精确的排名范围（目标宽度为30-50位）。此阶段实现了“基于已知锚点的相对定位”。

**第三阶段（最终报告合成）**：接收完整的非匿名化大学数据以及前两阶段的结果，生成结构化的最终分析报告。

**关键技术：**
1.  **严格的匿名化协议**：这是防止LLM记忆混淆结果的根本技术。在数据进入流水线前，应用匿名化函数α，将所有识别信息替换：机构名称变为随机十六进制ID，国家、论文标题、DOI、合作国家均被遮蔽或替换为占位符，已发布的排名数据也被置空。仅保留纯数值指标和计算出的统计量（如Z分数）。
2.  **评估时的数据隐藏**：在第二阶段使用`get_ranking_samples`工具时，系统会从排名存储库`R_s`中临时移除目标大学`u*`，确保校准过程无法直接“看到”或比较目标大学的真实排名，进一步杜绝记忆或数据泄漏。
3.  **分层归一化与信号构建**：指标不仅进行全局归一化（基于分层的基准值，如Top 500的25分位数和Top 10的75分位数），还计算相对于最近层级的Z分数，生成如“h指数：高于第二层级均值+1.2σ”的强解释性信号，辅助LLM理解相对位置。
4.  **多智能体并行与工具增强**：针对不同排名体系定制独立的校准智能体，允许并行处理和体系特定的推理。工具的使用将LLM从纯文本推理转变为能够主动查询、计算和比较的“数据分析师”。

通过这套组合方案，UniRank实现了在完全匿名和隐藏真实排名的约束下，仅凭文献计量信号进行排名推理，其系统性的预测偏差（如一致预测排名更差）和从精英层到尾部层性能的单调下降，都成为了其进行的是真实分析而非记忆的有力证据。

### Q4: 论文做了哪些实验？

论文在THE世界大学排名（包含约2092所大学）上进行了系统评估。实验设置采用分层抽样构建了包含500所大学的测试集，按排名层级（精英、强、中、低、尾部）和地区进行分层。评估采用双盲协议，确保数据匿名且真实排名对校准工具隐藏，以防止LLM记忆干扰。

基准测试包括多种指标：平均绝对误差（MAE）、中位数绝对误差、百分比归一化MAE（PNMAE）、命中率（Hit@25/50/100）、范围覆盖、记忆指数（MI）以及斯皮尔曼/肯德尔相关系数。主要结果基于352所成功预测的大学：MAE为251.5排名位置，中位数绝对误差为131.5，PNMAE为12.03%，斯皮尔曼ρ为0.769，命中率@50为20.7%，@100为39.8%，记忆指数严格为零（表明无记忆性预测）。误差分析显示系统存在正向偏差（+190.1），即倾向于预测比实际更差的排名，且性能从精英层（MAE=60.5，命中率@100=90.5%）到底层（MAE=328.2，命中率@100=20.8%）单调下降，这证明了管道进行的是真实分析推理而非记忆召回。统计测试表明校准阶段对整体性能改善不显著（p=0.343），但对精英和尾部预测有提升作用。失败案例归因于声誉、教学等不可观测信号或数据缺陷。

### Q5: 有什么可以进一步探索的点？

本文提出的 UniRank 系统在匿名化数据下进行排名估计，其局限性与未来方向可从几个方面深入探索。首先，当前系统在尾部院校（非精英梯队）的预测误差显著增大（MAE 从 60.5 升至 328.2），表明模型对非顶尖机构的特征学习与推理能力不足，未来需针对长尾分布设计更精细的校准策略，例如采用自适应校准，基于指标相似性而非排名邻近性选择参照高校。其次，系统仅依赖文献计量数据，未来可整合多源异构信息，如政府数据库的师生比例、专利数据、奖项记录及实时网络声誉信号（通过 Agentic web search 获取），以提升排名维度的完整性。再者，方法论上可引入多准则决策技术（如 TOPSIS），为 LLM 校准提供可解释的数学基准，并探索两者结合的有效性。最后，需将评估扩展至 QS、ARWU 等不同排名体系，验证方法的泛化能力，并进一步降低系统性的正向偏差（当前一致预测排名更差），这可能需调整损失函数或引入偏差校正模块。

### Q6: 总结一下论文的主要内容

这篇论文提出了UniRank，一个多智能体LLM校准流水线，其核心贡献并非构建一个实用的大学排名系统，而是建立了一个用于评估LLM在排名任务中真实推理能力的严谨框架。该框架的关键创新在于通过数据匿名化（隐去机构名称、国家、论文标题等）和评估时隐藏真实排名，有效隔离了LLM对训练数据记忆的影响，迫使系统进行基于文献计量数据的分析推理。实验表明，系统在THE排名上取得了有意义的顺序一致性（如斯皮尔曼相关系数0.769），且记忆指数为零，证实了其推理的有效性。性能从精英梯队到尾部梯队的规律性下降以及系统性的正向误差，进一步揭示了其无法获取声誉、教学等关键排名信号的固有局限。因此，该工作的主要意义是提供了一个包含留一法协议、去污染流程、记忆指数测量和多维错误分类的标准化评估方法论，为未来改进排名估计模型设立了清晰的基线基准和可复现的测评体系。
