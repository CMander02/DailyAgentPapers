---
title: "NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama"
authors:
  - "Logan Mann"
  - "Abdur Rahman"
  - "Mohammad Saifullah"
  - "Taaha Kazi"
  - "Vasu Sharma"
date: "2026-06-16"
arxiv_id: "2606.17391"
arxiv_url: "https://arxiv.org/abs/2606.17391"
pdf_url: "https://arxiv.org/pdf/2606.17391v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "long-horizon planning"
  - "world model"
  - "audio drama agent"
  - "evaluation benchmark"
  - "state-space model"
relevance_score: 7.5
---

# NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama

## 原始摘要

Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open benchmark of nine narrative-structure metrics evaluated across horizons h in {10, 20, 50, 100, 200}, with cross-lingual evaluation across four Indic languages (Hindi, Tamil, Telugu, Marathi). We introduce N-VSSM, a Narrative Variational State-Space Model that maintains a structured 256-dimensional latent world state over more than 200 episodes via a Mamba-2 backbone with an event-conditioned posterior and an 8B decoder. N-VSSM holds plot-beat F1 >= 0.84 across all horizons at 4x lower compute than the closed-frontier band. A learned Cultural Transfer Function lifts cross-language fidelity by +0.20 to +0.23 Likert points. In a within-subjects writer study (n = 12 professional authors, 240 trials), N-VSSM is preferred over Claude Opus 4.5 on long-arc consistency 71% of the time and rated +1.3 Likert points higher on controllability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长程协作式音频剧创作中的叙事一致性崩溃问题。长格式连载音频剧（200-800集）是全球快速增长的艺术形式，但现有大语言模型在这一场景中表现不佳。当前研究背景是，通用长上下文基准（如LongBench、RULER）仅评估检索、事实回忆和摘要等能力，没有测量结构性叙事连贯性这一创作核心指标。现有方法的不足体现在：（1）所有前沿封闭模型在情节节拍F1指标上存在0.78-0.81的性能饱和天花板，且在200集水平上出现约0.20的F1下降；（2）缺乏针对跨100+集、人机协作延续场景的统一评估标准；（3）跨语言（如印地语、泰米尔语等）叙事保真度显著下降。本文的核心问题是：如何构建一个能够在超过200集的超长程协作创作中保持结构叙事一致性的系统，同时突破现有模型的性能天花板并解决跨语言保真度问题。为此，论文提出NarrativeWorldBench基准和N-VSSM潜世界模型，后者通过结构化256维隐状态空间和Mamba-2骨干网络，在所有水平上保持≥0.84的F1值，计算量仅为封闭模型前缘的1/4。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **长上下文评测基准**：LongBench、RULER、L-Eval、InfinityBench和NoCha主要聚焦于长输入下的检索与召回能力，与本文互补但未评估叙事结构。本文提出的NarrativeWorldBench专门针对叙事结构进行九维度评测，并覆盖四种印度语言。

2. **故事与剧本生成**：Re3、DOC、Dramatron、WritingBench及“故事生成即搜索”方法采用规划-写作或基于搜索的长文本生成范式。最近相关的工作包括学习型规划器和结构化记忆Transformer，它们为基座生成器添加显式结构。本文N-VSSM的创新在于通过Mamba-2骨干网络和事件条件化后验维护256维隐式世界状态，无需显式规划即可保持长程一致性。

3. **状态空间模型**：S4、Mamba和Mamba-2提供了线性时间序列骨干网络，可扩展至超长上下文。N-VSSM采用Mamba-2作为解码器，在此基础上引入变分状态空间框架实现高效世界建模。

4. **跨文化自然语言生成**：现有研究关注LLM在本地化与文化对齐中的未说明性，本文据此设计跨语言协议和文化迁移函数，使N-VSSM在四种印度语言上获得显著保真度提升。

与前述工作的关键区别在于，本文同时提出需要评估叙事结构的评测基准和能维持超长篇一致性的生成模型，并首次系统分析跨语言长篇音频剧场景。

### Q3: 论文如何解决这个问题？

论文通过提出一个全新的基准NarrativeWorldBench和一个名为N-VSSM的潜在世界模型来解决长程协同创作音频剧中的叙事一致性问题。整体框架分为两部分：基准测试与模型创新。

NarrativeWorldBench是一个开放的基准，包含1204个序列化音频剧续写实例，横跨6种类型，弧长80-412集。它评估9个叙事结构指标，包括情节节奏F1、角色声音一致性、世界规则违反率、伏笔回报率等，并在5个时间跨度（h∈{10,20,50,100,200}）上评估。基准还包含跨语言评估（印地语、泰米尔语、泰卢固语、马拉地语），通过专业翻译和本土评分者评估文化保真度。

N-VSSM是核心创新，它基于Mamba-2 8B解码器，增加了一个显式的256维叙事潜在状态z_t，每场景更新一次。关键技术包括：事件提取器在每个场景边界生成事件元组e_t；后验网络q_ϕ(z_t|z_{t-1},e_t,h_t)提供高斯分布；通过交叉注意力将潜在状态注入Mamba-2的低秩适配器。训练采用场景级负ELBO损失加KL退火和伏笔回报辅助损失。还引入了文化迁移函数T_l——一个2层MLP，通过并行场景对训练，将潜在状态迁移到目标文化区域。

主要创新点包括：1) 显式的叙事世界模型保持长期一致性，在所有跨度上维持F1≥0.84；2) 计算效率比闭源前沿模型低4倍；3) 文化迁移函数提升跨语言保真度0.20-0.23 Likert点；4) 在专业作家用户研究中，71%情况下长弧一致性优于Claude Opus 4.5。

### Q4: 论文做了哪些实验？

论文进行了两个主要实验。首先，在 NarrativeWorldBench 基准测试上，对 21 个模型（包括经典、微调、开放前沿、封闭前沿和推理模型）进行对比，使用 9 个叙事结构指标评估，数据集涵盖跨视界 h ∈ {10, 20, 50, 100, 200} 及四种印度语言。主要结果：封闭前沿模型在情节节拍 F1 上饱和于 [0.78, 0.81]，在 h=200 时下降约 -0.20；提出的 N-VSSM 模型在所有视界保持 F1 ≥ 0.84，计算成本低 4 倍，在 h=200 时，伏笔回报改善 +0.18，时间连贯性 +0.14，母题持续性 +0.12。文化迁移函数使跨语言保真度提升 +0.20 到 +0.23 Likert 点（p < 0.01）。其次，进行了一项 12 位专业作家、240 次试验的组内写作研究。作家在 71% 的试验中偏好 N-VSSM 的长弧一致性（95% CI [64%, 77%]），可控性评分高出 Claude Opus 4.5 约 +1.3 Likert 点（95% CI [+0.9, +1.7]）。消融实验显示，移除潜在后验使 h=200 时 F1 下降 -0.11，替换 Mamba-2 为 Transformer 使 F1 下降 -0.06，移除伏笔辅助损失使伏笔率下降 -0.13。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于基准数据和实验设计的广度不足。首先，NarrativeWorldBench仅覆盖四种印度语言且语料偏向独立制作，未来应扩展至更多语种（如中文、阿拉伯语）及主流商业作品，以验证世界模型的跨文化泛化能力。其次，当前N-VSSM的256维潜在状态虽能维持长程一致性，但状态空间大小与遗忘曲线的理论边界尚未探明，可尝试引入可微分记忆网络或分层状态架构（如将情节记忆与角色状态分离）来提升容量。此外，用户研究仅有12位专业作者，样本量较小且存在评委-模型重叠偏差，未来需在大规模业余创作者或听众群体中验证长期叙事控制的主观偏好。从技术角度，事件条件后验与Mamba-2骨干的结合虽高效，但可探索将文化迁移函数直接融入世界模型的目标函数（如文化差异感知的正则化），而非仅作为后处理变换。最后，当前N-VSSM的8B解码器在极长序列（>500集）下的误差累积机制尚不明确，可设计动态回溯修正模块来缓解情节漂移。

### Q6: 总结一下论文的主要内容

这篇论文提出了NarrativeWorldBench基准，用于评估21个大语言模型在长序列音频剧（200-800集）中的叙事结构指标。实验发现所有封闭前沿系统在剧情节拍F1得分上饱和于0.78-0.81，并在200集时下降约0.20。为解决这一问题，论文引入N-VSSM，一种叙事变分状态空间模型，通过Mamba-2骨干网络和事件条件后验维持256维潜在世界状态，解码器8B参数，能在所有水平上保持≥0.84的F1得分，计算量仅为封闭前沿系统的四分之一。此外，学习到的文化迁移函数将跨语言保真度提升0.20-0.23 Likert点。在12位专业作者的240次试验中，N-VSSM在长弧一致性上71%优于Claude Opus 4.5，可控性评分高1.3点。核心贡献在于揭示了现有模型的长程叙事崩溃问题，并提供了首个可持续维持叙事连贯性的潜在世界模型，对协同创作高算力需求场景有重要意义。
