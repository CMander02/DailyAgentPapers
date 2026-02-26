---
title: "TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts"
authors:
  - "Jiafeng Lin"
  - "Yuxuan Wang"
  - "Huakun Luo"
  - "Zhongyi Pei"
  - "Jianmin Wang"
date: "2026-02-25"
arxiv_id: "2602.21693"
arxiv_url: "https://arxiv.org/abs/2602.21693"
pdf_url: "https://arxiv.org/pdf/2602.21693v1"
categories:
  - "cs.LG"
tags:
  - "时间序列预测"
  - "多模态学习"
  - "大语言模型"
  - "Transformer"
  - "混合专家模型"
  - "因果推理"
relevance_score: 5.5
---

# TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts

## 原始摘要

Multimodal time series forecasting has garnered significant attention for its potential to provide more accurate predictions than traditional single-modality models by leveraging rich information inherent in other modalities. However, due to fundamental challenges in modality alignment, existing methods often struggle to effectively incorporate multimodal data into predictions, particularly textual information that has a causal influence on time series fluctuations, such as emergency reports and policy announcements. In this paper, we reflect on the role of textual information in numerical forecasting and propose Time series transformers with Multimodal Mixture-of-Experts, TiMi, to unleash the causal reasoning capabilities of LLMs. Concretely, TiMi utilizes LLMs to generate inferences on future developments, which serve as guidance for time series forecasting. To seamlessly integrate both exogenous factors and time series into predictions, we introduce a Multimodal Mixture-of-Experts (MMoE) module as a lightweight plug-in to empower Transformer-based time series models for multimodal forecasting, eliminating the need for explicit representation-level alignment. Experimentally, our proposed TiMi demonstrates consistent state-of-the-art performance on sixteen real-world multimodal forecasting benchmarks, outperforming advanced baselines while offering both strong adaptability and interpretability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态时间序列预测中，如何有效利用文本信息来提升预测准确性的核心难题。研究背景在于，现实世界中的时间序列（如销售额、交通流量）常受外部文本信息（如促销公告、政策新闻）的因果影响，这些文本蕴含了导致数值波动的关键因素。传统时间序列预测模型大多仅依赖历史数值数据，忽视了多模态信息的潜力；而现有的多模态方法通常借鉴视觉-语言模型的跨模态对齐技术，但这类方法存在根本局限：文本与视觉数据在语义上是对齐的，而时间序列相关的文本（如描述未来事件的报告）与历史数值序列之间缺乏直接的语义对应关系，强行进行特征层面的融合往往效果不佳，且难以捕捉文本中的因果推理知识。

现有方法的不足主要体现在两方面：一是多数方法无法有效处理文本模态，尤其是那些缺乏直接语义对齐、但具有因果解释力的外部文本（如紧急事件报告）；二是即使尝试融合文本，也常陷入简单的特征对齐或融合，未能深入挖掘文本中关于未来趋势的隐含因果知识，导致预测性能提升有限且可解释性差。

因此，本文的核心问题是：如何克服模态对齐的挑战，充分利用大型语言模型（LLMs）的因果推理能力，将文本信息中的结构化未来知识有效整合到时间序列预测中，从而实现更准确、可解释的多模态预测。为此，论文提出了TiMi框架，通过LLMs从文本中推理出未来发展的因果知识作为指导，并设计了一个轻量化的多模态专家混合模块（MMoE），以插件方式增强基于Transformer的时间序列模型，避免显式的表示层对齐，实现文本与序列数据的无缝集成。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕时间序列预测的Transformer模型改进和多模态融合方法展开，可分为以下两类：

**1. 时间序列Transformer的架构优化**：早期研究如LogSparse和Informer通过改进自注意力机制来提升计算效率；后续工作如Autoformer引入自相关机制捕捉序列级依赖，而iTransformer将整个序列作为单一令牌学习多元相关性。近期TimeXer通过可学习的全局令牌交互不同粒度令牌，增强了处理异构时间序列数据的能力。这些研究为Transformer在时间序列分析中的应用奠定了基础，但主要针对单模态数据。本文的TiMi在此基础上，通过引入多模态混合专家（MMoE）模块，扩展了Transformer处理多模态数据的能力，无需显式的表示层对齐。

**2. 多模态时间序列预测的融合方法**：现有方法可分为早期融合和晚期融合两类。早期融合（如Time-LLM、UniTime、AutoTimes）将时间序列数据对齐到文本隐藏状态，直接利用LLM作为主干进行建模；晚期融合（如Time-MMD、IMM-TSF）则分别处理时间序列和文本模态，再融合特征进行预测。这些方法通常面临模态语义不对齐的挑战。本文提出了一种“非融合引导”新范式，与上述方法有本质区别：它不进行直接的模态融合或对齐，而是利用LLM生成对未来发展的推理作为指导信息，通过轻量级MMoE模块引导时间序列主干模型进行预测，从而避免了显式对齐的困难，并释放了LLM的因果推理能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TiMi的新型多模态时间序列预测框架来解决现有方法难以有效整合文本信息的问题。其核心思想是利用大型语言模型（LLM）的因果推理能力来指导时间序列预测，并通过一个创新的多模态专家混合模块实现无缝融合，避免了复杂的跨模态对齐。

整体框架以Transformer为基础，以时间序列为主要模态。主要包含三个关键模块：文本编码、时间序列嵌入和多模态专家混合模块。首先，文本编码模块使用一个冻结的LLM处理外生文本内容，通过平均池化生成一个富含因果知识的文本令牌，该令牌蕴含了对未来趋势、周期性和波动的推断。其次，时间序列嵌入模块将历史序列分割成重叠的片段，并通过可训练的线性投影层转换为时间令牌，以捕捉局部时序模式。

核心创新在于提出的多模态专家混合模块，它作为一个轻量级插件嵌入Transformer层中。该模块包含两个并行的专家混合子模块：文本感知专家混合模块和序列感知专家混合模块。文本感知模块以LLM生成的文本表征作为路由网络的输入，动态地为所有时间令牌选择一组稀疏的专家网络，从而将文本中提取的未来趋势知识有针对性地注入预测过程。序列感知模块则将所有时间令牌拼接成一个全局序列表征用于路由，使模型能同时把握序列的整体模式和局部依赖。两个子模块的输出共同构成多模态专家混合模块的输出，随后与自注意力层的输出进行残差连接和层归一化，完成信息融合。

这种方法的关键技术优势在于：1）充分利用了LLM强大的因果推理能力来生成预测指导，而非进行简单的表示对齐；2）通过双路由机制，分别基于文本信息和序列全局上下文动态激活专家，实现了模态间信息的互补与协同；3）模块化设计使其能灵活赋能各种基于Transformer的时间序列模型，具备强适应性和可解释性。实验表明，该方法在多个真实世界基准数据集上取得了先进的性能。

### Q4: 论文做了哪些实验？

论文在多个真实世界多模态时间序列预测基准上进行了广泛的实验验证。实验设置方面，主要使用了Time-MMD数据集，涵盖农业、气候、经济、能源、健康、安全、社会公益和交通等九个领域的十六个数据集，每个数据集包含数值序列和相关文本数据。对比方法包括十种先进的深度预测模型，如多模态模型Time-MMD、AutoTimes、Time-LLM、GPT4TS，以及基于Transformer的TimeXer、iTransformer、PatchTST、Autoformer等。主要结果方面，TiMi在绝大多数数据集上取得了最先进的预测性能，显著优于基线模型。关键数据指标显示，在规则多模态预测中，TiMi相比其时间序列骨干模型PatchTST有显著提升；在不规则多模态数据集Time-IMM上，TiMi的平均均方误差（MSE）相比PatchTST降低了29.57%，优于Time-MMD（11.26%）和Time-IMM（16.46%）。此外，消融实验验证了其模块设计的必要性，自适应研究表明其提出的MMoE模块作为轻量级插件，可泛化到多种Transformer骨干（如PatchTST、TimeXer、Autoformer），平均性能提升分别达到18.2%、12.5%和12.4%。系列感知分析则通过Mann-Kendall趋势测试可视化了其模块的时序感知与可解释性。

### Q5: 有什么可以进一步探索的点？

本文提出的TiMi框架虽然取得了显著效果，但仍存在一些局限性和值得深入探索的方向。首先，模型高度依赖LLM生成的未来趋势推理，其质量直接影响预测性能，但LLM可能产生幻觉或错误推理，如何有效评估和约束LLM输出的可靠性是一个关键问题。其次，当前方法主要针对文本与时间序列的双模态融合，未来可扩展至更多模态（如图像、音频等），研究更通用的多模态对齐与融合机制。此外，TiMi的MMoE模块作为轻量级插件，虽然增强了适应性，但在处理极端不平衡或高噪声多模态数据时可能表现不稳定，未来可探索动态专家选择或引入不确定性量化机制。从长远看，将TiMi核心模块嵌入基础模型进行大规模预训练是一个有前景的方向，但需要解决计算效率、跨领域迁移以及如何构建高质量文本-时序语料库等挑战。最后，模型的解释性仍有提升空间，例如可视化LLM推理路径与时间序列预测间的关联，以增强用户对因果推理过程的理解与信任。

### Q6: 总结一下论文的主要内容

本文提出了一种名为TiMi的新型多模态时间序列预测框架，旨在解决现有方法难以有效整合文本信息（如紧急报告、政策公告）进行预测的问题。传统方法通常依赖跨模态对齐，但文本与数值序列之间缺乏直接语义对应，且文本中包含无关信息，导致性能受限。

TiMi的核心创新在于利用大型语言模型（LLM）的因果推理能力，从文本中提取对未来趋势的结构化因果知识，作为预测的指导。为无缝整合外部文本信息和历史序列数据，论文设计了多模态专家混合（MMoE）模块作为轻量级插件，可嵌入基于Transformer的时间序列模型。MMoE包含文本感知专家（TMoE）和序列感知专家（SMoE），分别引导模型关注文本中的因果知识和历史序列的长期趋势，避免模糊的特征级融合。

实验在16个真实世界多模态预测基准上进行，结果表明TiMi consistently取得了最先进的性能，超越了先进的单模态和多模态基线，同时兼具良好的适应性和可解释性。该工作为多模态时间序列预测提供了一种无需显式对齐的新范式，显著提升了预测准确性。
