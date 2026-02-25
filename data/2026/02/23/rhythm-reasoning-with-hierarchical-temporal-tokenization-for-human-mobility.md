---
title: "RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility"
authors:
  - "Haoyu He"
  - "Haozheng Luo"
  - "Yan Chen"
  - "Qi R. Wang"
date: "2025-09-27"
arxiv_id: "2509.23115"
arxiv_url: "https://arxiv.org/abs/2509.23115"
pdf_url: "https://arxiv.org/pdf/2509.23115v3"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM应用"
  - "时空预测"
  - "轨迹推理"
  - "序列建模"
  - "提示工程"
relevance_score: 6.5
---

# RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility

## 原始摘要

Predicting human mobility is inherently challenging due to complex long-range dependencies and multi-scale periodic behaviors. To address this, we introduce RHYTHM (Reasoning with Hierarchical Temporal Tokenization for Human Mobility), a unified framework that leverages large language models (LLMs) as general-purpose spatio-temporal predictors and trajectory reasoners. Methodologically, RHYTHM employs temporal tokenization to partition each trajectory into daily segments and encode them as discrete tokens with hierarchical attention that captures both daily and weekly dependencies, thereby quadratically reducing the sequence length while preserving cyclical information. Additionally, we enrich token representations by adding pre-computed prompt embeddings for trajectory segments and prediction targets via a frozen LLM, and feeding these combined embeddings back into the LLM backbone to capture complex interdependencies. Computationally, RHYTHM keeps the pretrained LLM backbone frozen, yielding faster training and lower memory usage. We evaluate our model against state-of-the-art methods using three real-world datasets. Notably, RHYTHM achieves a 2.4% improvement in overall accuracy, a 5.0% increase on weekends, and a 24.6% reduction in training time. Code is publicly available at https://github.com/he-h/rhythm.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人类移动性预测中存在的核心挑战：如何有效建模复杂的长期依赖和多尺度周期性行为。研究背景在于，人类移动轨迹对交通规划、流行病控制和城市规划至关重要，但其预测面临轨迹序列长、空间异质性强以及受动态因素（如天气、特殊事件）影响等难题，导致非平稳、多尺度的时空模式难以捕捉。

现有方法存在明显不足。传统的马尔可夫或循环神经网络（RNN）方法要么忽略了长期的周期性模式，要么在处理长序列时面临梯度消失问题。而基于Transformer的方法虽然能处理长序列，但通常将时间视为静态特征，未能有效解耦和建模多尺度（如日级和周级）的周期性模式。此外，一些专门的移动性模型（如PMT、ST-MoE-BERT）虽然针对移动数据设计，但缺乏利用大型语言模型（LLMs）强大推理能力来建模复杂相关性的机制，限制了预测性能。

因此，本文提出的RHYTHM框架要解决的核心问题是：如何设计一个统一、高效且可扩展的模型，以同时捕获人类移动中的细粒度时空动态、深层语义上下文以及多尺度周期性依赖。具体而言，它通过引入分层时间标记化（将轨迹分割为日级片段并编码为离散标记）来显著减少序列长度并保留周期信息，同时利用冻结的预训练LLM作为推理骨干，以参数高效的方式增强对复杂相互依赖关系的建模能力，从而在提升预测准确性的同时降低计算成本。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：移动性预测方法和LLM跨领域适配方法。

在**移动性预测方法**方面，早期研究采用概率模型，随后发展为基于LSTM等序列模型和注意力机制的深度学习方法，以更好地建模时序依赖。图神经网络等方法进一步引入了空间关系建模。近年来，Transformer架构被用于捕捉长程依赖，但其在处理移动模式固有的多尺度周期性（如日周期和周周期）方面存在局限。一些最新研究尝试将大语言模型（LLMs）用于移动预测，但通常将轨迹视为通用序列，未能显式地建模其周期性结构。本文提出的RHYTHM框架则通过分层时序标记化（Hierarchical Temporal Tokenization）来显式捕获日级和周级依赖，这是与前述工作的重要区别。

在**LLM跨领域适配方法**方面，LLMs已成功适配到计算机视觉、语音、生物医学、时间序列预测等多个领域。常见的适配策略包括使用LoRA等参数高效微调方法。近期也有研究探索保持LLM主干冻结，仅将其用作序列表征提取器，以降低计算成本并保留其语义推理能力。本文工作属于后一脉络，但据作者所知，RHYTHM是首个将冻结LLM适配于人类移动预测任务的方法，其通过预计算提示嵌入来丰富标记表征，无需大量微调即可保持模型的推理能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RHYTHM的统一框架来解决人类移动性预测中复杂的长期依赖和多尺度周期性问题。其核心方法是利用大型语言模型（LLM）作为通用的时空预测器和轨迹推理器，并围绕此设计了层次化的时序标记化与语义上下文集成机制。

整体框架包含几个主要模块。首先，**时空特征编码模块**为每个轨迹点构建可学习的时序嵌入（如一天内时间和星期几）和空间嵌入（如位置类别和地理坐标），并通过逐元素相加融合成统一的时空嵌入。其次，**时序标记化模块**是关键创新点。它将长轨迹序列按天等有意义的时间间隔分割成多个非重叠的片段。每个片段内部通过“片段内注意力”建模局部依赖，然后通过可学习的池化操作将每个片段压缩为一个离散的“片段标记”。这些片段标记再经过“片段间注意力”来捕获跨片段的长期依赖（如周模式）。这种层次化注意力设计将序列长度从T二次方地减少到片段数量N，从而在保留周期信息的同时大幅降低了计算复杂度。

第三，**语义上下文集成模块**解决了传统方法忽略丰富语义信息的问题。它为每个轨迹片段和预测目标时间戳，使用冻结的预训练LLM离线生成描述性的提示词，并提取其语义嵌入。这些预计算的语义嵌入随后与对应的时序标记嵌入进行对齐和融合。最后，**对齐与预测模块**将融合了语义信息的嵌入序列输入到冻结的LLM主干中。LLM利用其强大的上下文推理能力处理这些对齐的信息，最终通过一个输出投影层将LLM的隐藏表示映射到候选位置的预测概率。

主要创新点包括：1）**层次化时序标记化**，通过分片和两级注意力高效建模多尺度时间依赖；2）**预计算提示嵌入的集成**，利用冻结LLM注入丰富的语义上下文，而无需在训练时进行LLM前向传播，兼顾了信息丰富性与计算效率；3）**整体高效设计**，保持LLM主干冻结，结合序列长度压缩，实现了更快的训练速度、更低的内存使用以及理论上的性能保证。

### Q4: 论文做了哪些实验？

论文在三个真实世界的人类移动数据集（熊本、札幌、广岛，源自YJMob100K）上进行了实验，时间分辨率为30分钟。实验设置采用7天回顾窗口（336个时间槽）和1天预测范围（48个时间槽），将数据按天数划分为70%训练、20%验证和10%测试集。评估指标包括Accuracy@k（k=1,3,5）、平均倒数排名（MRR）、动态时间规整（DTW）和BLEU。

对比方法涵盖了LSTM基模型（LSTM、DeepMove）、Transformer基模型（PatchTST、iTransformer、CMHSA、PMT、COLA、ST-MoE-BERT）以及LLM基模型（Time-LLM、Mobility-LLM）。RHYTHM本身测试了以不同预训练LLM（Llama-3.2-1B/3B、Gemma-2-2B）为骨干的变体。

主要结果显示，RHYTHM在大多数指标上优于基线。具体而言，在Accuracy@1上整体比最佳基线提升2.4%，在周末时段提升达5.0%。在札幌和广岛数据集上，RHYTHM在所有评估指标中都取得了最佳性能。关键数据指标例如：在熊本数据集上，RHYTHM-Llama-3B的Acc@1为0.2941，Acc@5为0.5947；在札幌数据集上，RHYTHM-Gemma-2B的Acc@1为0.2943。地理评估中，RHYTHM在札幌的DTW得分最优（3745），显示了更好的空间对齐；MRR consistently优于所有基线，提升1.44%。效率方面，RHYTHM可训练参数仅占全模型大小的12.37%，训练时间比最佳基线减少24.6%，比LLM基方法平均快80.6%。模型性能随LLM骨干规模增大而提升，例如Llama-3.2-3B相比Llama-3.2-1B在Acc@1上提升0.40%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度进一步探索。首先，模型性能高度依赖预训练大语言模型的质量，而这些模型并非为移动性预测任务设计，未来可探索针对时空数据预训练的专用基础模型，或设计更高效的适配器微调方法以更好地迁移语义知识。其次，RHYTHM未采用自回归预测策略，虽然这有助于捕捉全局依赖，但可能忽略了人类移动决策的逐步生成特性；未来可研究混合预测范式，例如在层次化tokenization基础上引入条件自回归解码，以平衡长期依赖与逐步推理。此外，尽管冻结LLM主干提升了效率，训练时间仍较长，未来可结合动态稀疏激活、量化压缩或蒸馏技术进一步优化计算开销。从数据层面看，模型主要关注周期模式，未来可整合实时上下文信息（如天气、事件）及用户画像，以提升对非规律性移动的预测能力。最后，该框架的“即插即用”特性为集成多模态LLM（如视觉-语言模型）提供了可能，未来可探索融合地理图像、文本描述等多源数据，构建更全面的人类移动推理系统。

### Q6: 总结一下论文的主要内容

该论文提出了RHYTHM框架，旨在解决人类移动性预测中存在的复杂长程依赖和多尺度周期行为难题。其核心贡献在于创新性地将大语言模型（LLMs）作为通用时空预测器和轨迹推理器，构建了一个统一的预测框架。

方法上，RHYTHM首先使用时序标记化技术，将每条轨迹分割为每日片段并编码为离散标记，通过分层注意力机制同时捕获日级和周级依赖关系，从而在保留周期信息的同时显著缩短序列长度。此外，它通过冻结的LLM为轨迹片段和预测目标生成预计算的提示嵌入，以丰富标记表征，并将这些组合嵌入馈送回冻结的LLM主干，以捕捉复杂的相互依赖关系。这种设计使得预训练的LLM主干保持冻结，大幅降低了训练时间和内存消耗。

实验结果表明，在三个真实世界数据集上，RHYTHM在整体准确率上优于现有先进方法，尤其在周末预测上提升显著，同时训练时间大幅减少，验证了其高效性和有效性。
