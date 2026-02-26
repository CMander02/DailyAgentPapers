---
title: "SciTS: Scientific Time Series Understanding and Generation with LLMs"
authors:
  - "Wen Wu"
  - "Ziyang Zhang"
  - "Liwei Liu"
  - "Xuenan Xu"
  - "Jimin Zhuang"
  - "Ke Fan"
  - "Qitan Lv"
  - "Junlin Liu"
  - "Chen Zhang"
  - "Zheqi Yuan"
  - "Siyuan Hou"
  - "Tianyi Lin"
  - "Kai Chen"
  - "Bowen Zhou"
  - "Chao Zhang"
date: "2025-09-26"
arxiv_id: "2510.03255"
arxiv_url: "https://arxiv.org/abs/2510.03255"
pdf_url: "https://arxiv.org/pdf/2510.03255v2"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM应用"
  - "时间序列分析"
  - "科学数据理解"
  - "基准测试"
  - "多模态LLM"
  - "模型泛化性"
relevance_score: 5.5
---

# SciTS: Scientific Time Series Understanding and Generation with LLMs

## 原始摘要

The scientific reasoning ability of large language models (LLMs) has recently attracted significant attention. Time series, as a fundamental modality in scientific data, presents unique challenges that are often overlooked in current multimodal LLMs, which either encode numerical sequences as text or convert them into images. Such approaches may be insufficient for comprehensive scientific time series understanding and generation. Existing unified time series models typically specialise in either forecasting or analysis, and their effectiveness on non-periodic, heterogeneous scientific signals remains unclear. To address these gaps, we introduce SciTS, a benchmark spanning 12 scientific domains and 43 tasks, with over 50k+ instances, both univariate and multivariate signals ranging from $10^0$ to $10^7$ in length and up to 10~MHz in frequency. We benchmark 17 models, including text-only LLMs, multimodal LLMs, and unified time series models, and find that general-purpose LLMs exhibit stronger generalisability than specialised time series models, while representing time series as text or images limits their performance due to excessively long sequences and loss of numerical precision, respectively. We then introduce TimeOmni, a framework that equips LLMs with the ability to understand and generate time series while remaining compatible with general-purpose LLM training. This work fills a gap in both dedicated benchmarks and modelling frameworks for scientific time series, paving the way for LLMs to understand and generate complex temporal scientific data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在科学时间序列数据理解与生成方面的能力不足问题。研究背景是，尽管LLMs在自然语言处理上表现出色，且其科学应用潜力备受关注，但科学数据常以多模态形式存在，其中时间序列是物理、天文、生物等学科中最基础且广泛的数据模态。现有方法主要有两类不足：一是当前多模态LLMs通常将时间序列简单编码为文本或转换为图像，前者因序列过长超出模型处理极限，后者则损失数值精度，均难以捕捉科学时间序列中复杂的时序动态、长程依赖和领域特定模式；二是现有的统一时间序列模型多专注于单一任务类型（如预测或分析），且其架构专门化，难以融入LLMs，它们在非周期性、异质的科学信号上的有效性尚不明确。因此，本文的核心问题是：如何填补科学时间序列领域专用基准和建模框架的空白，使LLMs能够有效理解和生成这类具有多样长度、频率和模式的复杂科学时序数据。为此，论文引入了SciTS基准和TimeOmni框架，以评估和提升LLMs在此类任务上的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：科学时间序列基准和时序表示学习方法。

在**科学时间序列基准**方面，现有工作如SFE、ScienceQA等主要关注文本和图像推理，将时序数据转换为图像会导致信息损失。其他通用时序基准（如Time-MQA、MTBench）虽直接处理时序数据，但并非针对科学领域，且任务类型、领域覆盖和数据规模有限。SciTS与这些工作的区别在于，它首次构建了一个大规模、多领域（12个领域）、多任务（7类任务）且包含真实与合成数据的科学时序专用基准，专注于科学时序的理解与生成。

在**时序表示学习**方面，现有统一时序模型（如基于Transformer的架构）通常专精于预测或分析单一任务，且在处理非周期性、异质的科学信号上效果不明。近期研究尝试将LLMs用于时序分析，但效果存疑，或通过多模态/对齐方法将时序作为额外模态处理。这些方法大多只关注理解或生成的单一层面，且专用架构设计无法与通用LLM训练兼容。UniTS虽整合了QA和预测任务，但仍依赖独立架构。本文提出的TimeOmni框架与这些工作的区别在于，它首次统一了7类理解与生成任务，并能轻松集成到LLMs中，实现与其他模态和任务的联合训练。

### Q3: 论文如何解决这个问题？

论文通过提出TimeOmni框架来解决科学时间序列理解与生成的挑战。其核心方法是将时间序列编码为适合大型语言模型（LLM）处理的表示，并利用LLM的强大推理能力进行多任务处理。

整体框架由三个主要部分组成：时间序列编码器、预训练LLM主干和任务特定的输出头。编码器负责将原始时间序列（可能为多变量）转换为与LLM隐藏维度对齐的嵌入序列。具体流程是：首先将输入时间序列沿时间维度展平；然后，编码器内的路由器根据序列长度自动选择合适的分块大小，确保经过专家处理后输出序列长度在100到200之间，以适配LLM的上下文窗口。选定的分块专家通过一维卷积将分块后的序列映射到一个统一的中间维度。

关键的创新点在于**分块重编程模块**。该模块利用LLM本身的词嵌入表，通过多头交叉注意力机制，将卷积后的时间序列特征重新表示为与LLM词汇语义空间对齐的嵌入。这相当于为时间序列“学习了一种语言”，使其能够被LLM有效理解。在输入LLM前，编码后的时间序列嵌入与文本任务提示的嵌入进行拼接。对于理解任务，采用“提示作为后缀”的策略；对于生成任务，则采用“提示作为前缀”的策略。

输出端根据任务类型进行设计：对于理解任务（如分类、问答），LLM的输出嵌入通过一个softmax层生成文本令牌；对于生成任务（如预测、插值），输出嵌入则被展平并通过一个线性回归头映射回目标长度的时间序列数据。为了应对基准测试中输出长度的巨大差异，模型预定义了一组回归头，并根据需要选择最接近的一个，必要时进行截断。

该架构的设计使得TimeOmni能够统一处理从短到极长、频率各异的科学时间序列，同时保持了与通用LLM训练流程的兼容性，避免了将序列转为文本或图像所导致的信息丢失或长度限制问题。

### Q4: 论文做了哪些实验？

论文在提出的SciTS基准上进行了全面的实验评估。实验设置方面，采用零样本评估方式，对比了三大类共17个模型：1) 纯文本大语言模型（如GPT-4.1-mini、Gemini-2.5-Flash、DeepSeek-V3及多个开源模型），时间序列被处理为文本数字序列；2) 多模态大语言模型（如GPT-5-mini、Gemini-2.5-Flash、InternVL、Qwen2.5-VL），时间序列被转换为图像输入；3) 统一时间序列模型（如Moirai-Large、TimeMoE-Large、Chronos-bolt-Base、ChaTS、UniTS）。此外，论文还评估了自身提出的TimeOmni框架（基于Qwen3-8B微调）。评估数据集为涵盖12个科学领域、43个任务、超过5万个实例的SciTS基准，数据长度从10^0到10^7，频率高达10MHz，包含单变量和多变量信号。

主要结果如下：在理解任务上，评估指标为准确率/F1分数。结果显示，通用大语言模型（尤其是闭源模型）表现出比专用时间序列模型更强的泛化能力，但在天文学、神经科学等科学领域表现有限（F1分数常低于10%）。多模态LLM因图像压缩长序列，通常优于纯文本LLM。TimeOmni在几乎所有学科都取得了最佳性能（平均排名AvgRk为1.9），例如在天文学、生物声学、地球科学等学科的F1分数分别达到73.2%、58.1%、82.5%。在生成任务上，评估指标为成功率加权平均绝对百分比误差（swMAPE）。生成任务更具挑战性，纯文本输入在需要数值精确度的任务上优于图像输入。闭源LLM普遍优于开源LLM。专用时间序列模型在支持的预测任务上表现优异（如Moirai在经济学任务swMAPE低至1.8），但任务覆盖度低。TimeOmni在生成任务上也取得了最佳整体排名（AvgRk为4.1），其swMAPE在多个学科显著更低（如天文学2.8、地球科学2.2、气象学37.5）。任务覆盖度和实例级成功率分析表明，闭源LLM能处理大多数任务，但实例成功率仍相对较低；专用时间序列模型任务覆盖度低；而TimeOmni实现了对所有任务和实例的完全覆盖与100%成功率。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于，现有方法（如将时间序列编码为文本或图像）难以处理超长序列和保持数值精度，且统一时间序列模型在非周期性、异质性科学信号上的有效性未得到充分验证。未来研究可探索以下方向：一是开发更高效的序列表示方法，例如结合符号化表示与子序列压缩技术，以平衡信息保留与计算效率；二是设计针对科学时间序列的专用架构，如引入可处理多尺度特征的层次化注意力机制，提升对高频和长程依赖的建模能力；三是增强模型的因果推理能力，结合领域知识（如物理定律）进行约束生成，提高生成结果的科学合理性。此外，可扩展基准至更多跨模态任务（如时间序列与文本的联合生成），推动面向复杂科学问题的端到端推理框架发展。

### Q6: 总结一下论文的主要内容

该论文针对当前多模态大语言模型在科学时间序列数据处理上的不足，提出了SciTS基准和TimeOmni框架。核心问题是现有模型要么将数值序列编码为文本（导致序列过长），要么转换为图像（损失数值精度），且现有统一时间序列模型通常专精于预测或分析，对非周期性、异质的科学信号处理效果不明。为此，作者构建了SciTS基准，涵盖12个科学领域、43项任务、超过5万个实例，序列长度和频率跨度极大。通过评估17个模型，发现通用大语言模型比专用时间序列模型泛化性更强，但现有表示方法限制了性能。基于此，论文提出了TimeOmni框架，使大语言模型在保持通用训练兼容性的同时，获得理解与生成时间序列的能力。这项工作的主要贡献在于填补了科学时间序列专用基准和建模框架的空白，为利用大语言模型处理复杂科学时序数据开辟了新途径。
