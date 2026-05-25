---
title: "Cross-domain benchmarks reveal when coordinated AI agents improve scientific inference from partial evidence"
authors:
  - "Fiona Y. Wong"
  - "Markus J. Buehler"
date: "2026-05-21"
arxiv_id: "2605.22300"
arxiv_url: "https://arxiv.org/abs/2605.22300"
pdf_url: "https://arxiv.org/pdf/2605.22300v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体协作"
  - "跨领域基准"
  - "科学推理"
  - "协调智能体"
  - "评估框架"
  - "AI科学"
relevance_score: 8.5
---

# Cross-domain benchmarks reveal when coordinated AI agents improve scientific inference from partial evidence

## 原始摘要

Scientific evidence often spans instruments, databases, and disciplines, so no single source records the full phenomenon. This makes it difficult to determine when coordinated AI agents add value over simpler scientific workflows. We evaluate this question with a cross-domain benchmark spanning four scientific tasks: mapping molecular structure into musical representations, detecting historical paradigm shifts in science, identifying vector-borne disease emergence, and vetting transiting-exoplanet candidates. Each case uses a frozen evaluation panel, predefined scoring protocols, explicit baselines, ablations or null controls, and stated limitations. The results define three operating regimes. When different disciplines each capture only part of the phenomenon, cross-channel composites improve over single-channel baselines: climate-vector emergence reaches AUROC 0.944 and exoplanet vetting reaches AUROC 0.955. However, the exoplanet workflow is effectively tied with a strong combined-summary baseline, showing that decomposition does not always improve top-line performance. When one signal dominates, as in paradigm-shift detection, coordination mainly improves interpretation and traceability. For molecular sonification, the gain is representational rather than predictive. ScienceClaw x Infinite provides the auditable artifact and provenance layer for this evaluation. The benchmark therefore assigns value to coordination only when the corresponding performance, provenance, or representation claim is supported by explicit comparators.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的核心问题是：在多学科交叉的科学推理场景中，如何系统性地评估协调式AI智能体相较于简单工作流程（如单通道基线或汇总摘要）的实际增值作用。研究背景在于，科学证据往往分散于不同仪器、数据库和学科中，没有单一源头能记录完整现象（如传染病暴发需结合气候、生态、流行病学数据；系外行星验证需综合凌星形状、恒星背景和后续确认信息）。现有方法的不足包括：大多数自主AI科学发现系统的评估仍停留在演示或狭窄任务基准上，缺乏跨领域、可比较的框架；且常混淆“性能提升”、“可解释性与溯源提升”、“表征转换”三类不同主张。本文的核心贡献是建立了一个跨领域基准框架，包含冻结评估小组、预定义评分协议、显式基线、消融实验和局限声明，并通过四个具体任务（分子音乐化、科学范式转变检测、媒介传播疾病暴发识别、系外行星候选体筛选）来界定协调式工作流的三种运行机制：分布式证据下提升判别性能、主导信号下增强解释与可追溯性、表征映射下实现跨域结构恢复。该框架要求“协调”的价值必须通过与显式比较器的对比来确立。

### Q2: 有哪些相关研究？

该论文的相关工作可归纳为三类：**评测基准类**、**方法框架类**和**跨学科应用类**。

1. **评测基准类**：论文的核心贡献是提出了一个跨领域的协调AI智能体评测框架，与现有单一领域的基准（如科学发现、文献挖掘）不同，它要求每个任务必须包含固定评估面板、预定义评分规则、显式基线/消融实验和局限性声明。这使得协调智能体的性能（而非模型数量）成为可跨域比较的对象。

2. **方法框架类**：本文提出的“SciClaw × Infinite”框架强调通过内容可寻址的中间工件实现跨通道协调，与传统的单智能体摘要基线（直接拼接特征）或并行模型集成（如多任务学习）不同。论文通过系统消融证明，协调带来的价值（如可审计性、表征转换）仅在明确对比基线时才成立，而非自动优于强单智能体基线。

3. **跨学科应用类**：四个应用案例分别对应不同学科交叉场景。例如Climate-Vector Emergence与已有气候-流行病学联合预警研究的关系在于，它通过时序加权协调（如ENSO→容器生态→成蚊涌现）超越了气候/生态/流行病学单通道基线；Cosmic Filter则与天文领域行星候选体确认方法区别在于，其四通道分解（光变曲线、恒星背景、档案检查、后续观测）虽与强摘要基线性能持平，但显著提升了可审计性。

### Q3: 论文如何解决这个问题？

论文的核心方法是提出一个跨领域基准框架来评估协调式AI智能体在科学推理中的实际价值。整体架构通过四个科学任务（分子声映射、历史范式转变检测、媒介传播疾病预警、系外行星候选体审核）构建统一评估体系，每个任务都包含冻结评估面板、预定义评分协议、明确基线（脚本化单通道基线/单智能体摘要基线）、剔除实验或零假设控制，以及已知局限性声明。

关键技术包括工具体系的产物中介机制：每个专业智能体生成的结构化产物表示为 \( a=(u, y, m, P, q, r) \)，其中包含唯一标识符、类型化载荷、元数据、父产物集、质量标志和摘要。产物通过SHA256内容寻址实现可审计性和可复用性，形成有向无环图状溯源结构。评分公式为 \( S_i=\sum_j w_j x_{ij}+\sum_j \gamma_j \ell_{ij} \)，其中 \( x_{ij} \) 为通道特征，\( \ell_{ij} \) 为归一化领先时间，通过前向时间加权整合跨域证据。

主要创新点在于：（1）提出三种运行机制——分布式不完整证据（跨通道互补提升性能）、主导单通道（协调主要增强解释性和溯源性）、表征映射（非预测性结构恢复）；（2）设计对比器体系强制要求明确的性能/溯源/表征主张对应比较器；（3）19个对比器/剔除实验臂、11个控制/零假设检验、28个报告指标的跨域可比架构。以Climate-Vector Emergence为例，协调工作流AUROC达0.944，相较最强单通道基线提升+0.277，较组合摘要基线提升+0.208，证明领先时间加权跨通道评分优于孤立通道或简单信号聚合。

### Q4: 论文做了哪些实验？

论文在四个跨领域任务上进行了实验。实验设置包括每个任务使用固定的评估面板、预定义的评分协议、明确的基线方法、消融或零假设控制以及局限性声明。数据集方面：Sound of Molecules采用16个化合物的固定面板，使用检索@3、最近邻一致性和鲁棒性评分；Computational Kuhn使用16个范式转变事件与16个匹配控制，基于留一对AUROC和领先时间评分；Climate-Vector Emergence使用12个新兴事件与12个地区控制，通过首次信号年份和领先时间评分；Cosmic Filter使用12个确认行星与12个误报候选者，基于四种证据通道评估。对比方法包括：单一通道基线（如气候、生态、流行病学单独模型）、单一智能体摘要基线、通道消融（如无档案、无后续观测）以及零模型（随机标签置换）。主要结果：Climate-Vector Emergence达到AUROC 0.944，优于最强单通道基线0.667和组合摘要基线0.736；Cosmic Filter达到AUROC 0.955，但与强组合摘要基线持平；Computational Kuhn的AUROC为0.9688，但未优于最佳简单基线；Sound of Molecules的检索@3为0.2708，未超越化学基线。实验定义了三种运行模式：分布不完整证据（协同改善性能）、主导单通道（协同增加可解释性）和表征映射（协同揭示跨域结构）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是基准测试的规模有限（仅四个任务），且数据集均为回顾性筛选，缺乏前瞻性验证；二是确定性流水线虽然保证了可复现性，但未能测试模型在真实动态环境下的鲁棒性和泛化能力；三是当前评测聚焦于性能指标（如AUROC），对协调性带来的可解释性和可追溯性改进缺乏量化评估。未来可探索的方向包括：1）扩展跨域任务类型（如多模态生物医学诊断），验证协调智能体的适用范围；2）引入不确定性建模和自适应协调机制，使智能体能根据证据分布动态调整协作策略；3）设计可审计的元评测框架，量化协调性对科学推理透明度的增益；4）探索弱监督或自监督方法以减少对人工标注的依赖，并验证协调智能体在数据稀缺场景下的优势。此外，当前复合基线（combined-fraction）已接近协调模型性能，未来可尝试将协调智能体与端到端集成学习结合，探索混合架构的边界效益。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个跨领域基准框架，旨在回答一个核心问题：在科学推理中，何时通过协调AI代理整合来自多个不完整观测源的证据能带来价值，而何时简单的基线方法就已足够。问题定义在于，科学证据常分散于不同仪器、数据库和学科，单一来源无法反映全貌。方法上，该框架在四个科学任务上进行了评估：分子结构的音乐映射、科学范式转变的检测、媒介传播疾病预警和系外行星候选体筛选。每个任务都使用固定的评估面板、预定义的评分协议和明确的基线方法（如单通道或综合摘要）。主要结论通过结果总结为三种操作模式：1）当各学科证据互补时，协调能显著提升性能（如疾病预警AUROC达0.944）；2）当单一信号占主导时，协调主要增强可解释性和溯源能力（如范式检测）；3）在表征映射任务中，协调的价值在于揭示跨领域结构而非提升预测性能。该基准框架的核心贡献在于提供了严格的比较方法，系统地证明了协调代理的价值取决于具体情境，反对了代理数量或分解本身能带来性能提升的假设。
