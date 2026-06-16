---
title: "Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents"
authors:
  - "Shiyang Chen"
date: "2026-06-15"
arxiv_id: "2606.16364"
arxiv_url: "https://arxiv.org/abs/2606.16364"
pdf_url: "https://arxiv.org/pdf/2606.16364v1"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.SE"
tags:
  - "LLM Agent"
  - "Tool Selection"
  - "Attention Mechanism"
  - "Interpretability"
  - "Tool Calling"
  - "LLM Safety"
relevance_score: 7.5
---

# Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents

## 原始摘要

LLM agents mis-call tools, and the natural guess is that the model failed to see the right tool in a crowded harness. We show the opposite through a lens concurrent work sets aside -- the model's attention to labeled tool-definition segments. On real BFCL failures, by per-candidate attention argmax the model attends most to the correct tool 80% of the time (vs. 21% chance), and the gold is the under-attended segment on only 10%: it looks at the right tool and still picks wrong. This directly refutes the intuitive "crowded-harness / lost-in-the-middle" explanation: the failure is at the decision readout, not the harness, and we pin it there three ways. (1) Input vs. readout: repairing the prompt (reordering or duplicating the gold tool) recovers <=23% of failures, while readout-side interventions recover 59-91%. (2) Representation-invariance: two gold-pointed interventions in different representations -- an additive attention-logit bias and a residual-stream steering vector -- recover largely the same failures (per-task Jaccard 0.865 pooled, 0.79-0.91 per model), so the bottleneck is localized to the readout independent of which representation is poked. (3) A training-free, gold-free selector: per-segment attention closes most of the gold-free-vs-oracle gap on BFCL (+11.9 pts pooled function-name selection vs. +17.9-pt oracle headroom) and adds +14.9 pts on Seal-Tools; every model positive (exact McNemar p<=8e-4 each). Scopes differ: the causal attention-bias dose-response is bidirectional and monotonic on 10 mask-honoring models (3-32B), the full 0.5-32B span carrying only the correlational diagnostic; the deployable selector is evaluated on 5 single-turn models and does not yet transfer to a multi-turn loop.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体在调用工具时出现的“工具选择失败”问题。研究背景是，LLM智能体通常被赋予一个包含多个工具定义的系统提示，但即使模型能够正确关注到正确的工具定义，仍然会错误地选择其他工具。现有方法通常通过端到端评估来诊断失败，但无法解释模型内部的注意力机制与其选择行为之间的关系。

现有方法的不足在于，直观上人们可能认为失败是由于工具定义在提示中“拥挤”或模型“丢失在中间”导致的，即模型没有看到正确的工具。然而，本文通过对真实BFCL失败案例的分析发现，模型在80%的情况下实际上最关注正确的工具定义（随机概率仅为21%），只有10%的失败案例中正确工具被模型忽视。这表明失败的原因不在于输入阶段的注意力不足，而在于决策读出（readout）阶段的瓶颈。

因此，本文的核心问题是：为什么LLM智能体在已经注意到正确工具的情况下仍然选择错误？具体而言，论文旨在通过注意力-片段（attention-segment）分析，将失败定位到模型的读出阶段，而非输入阶段，并证明注意信号本身是可读、可操控的，从而为工具选择失败提供新的解释和干预方法。

### Q2: 有哪些相关研究？

相关研究可分为几类。首先，在**注意力分析与干预方法**方面，InstABoost和SpotLight通过添加注意力偏置来引导模型行为，但SpotLight仅支持增强操作且无候选选择功能；Attention Buckets和MoICE发现位置→注意力低谷对工具使用的影响，但无法定位特定工具段且无诊断指标。本文与它们的主要区别在于：采用双向剂量反应、有金标签与干扰项边界、可实现无金标签选择器。其次，在**内部信号诊断与修复**领域，多项并发工作（2025-2026）展示了从隐藏状态线性可读且可操控的工具选择，例如通过激活空间α-扫描切换所选工具。本文认同读头瓶颈论点但补充其未测量的注意力视角，即通过注意力logits而非残差流进行干预。此外，MindGuard从决策token测量工具元数据的注意力能量，但仅作相关性检测而不干预；PASTA通过重加权注意力处理用户标记片段但目的不同。最后，在**工具选择的评测与应用**上，BFCL和Seal-Tools被用作评估基准，而Agent-Radar将注意力引导用于多代理对话历史而非工具定义段。本文的贡献在于：提出"注意而未选择"的驳斥性发现，建立段级注意力因果杠杆，并开发训练免费的无金标签选择器。

### Q3: 论文如何解决这个问题？

该论文通过一种称为“注意力-分割”的分析视角，揭示了LLM代理工具选择失败的根本原因并非模型未能“看见”正确的工具，而是决策读取阶段的瓶颈。核心方法围绕注意力机制展开，通过三个关键实验定位并验证了这一发现。

首先，论文构建了受控的工具选择基准测试，其中包含一个正确工具和多个干扰项。通过提取HuggingFace的急切注意力权重，计算每个工具定义片段的注意力质量（即金标准工具与干扰工具的平均注意力差异），发现即使在失败案例中，模型在80%的情况下也最关注正确的工具，直接反驳了“拥挤环境”或“迷失在中间”的直觉解释。

其次，论文实施了因果干预。通过向注意力logits添加一个4维可加性偏置（注意力偏置干预），对金标准工具或干扰工具的注意力进行双向操控。结果显示，提升金标准工具的注意力logits能单调地提高选择成功率（从0.19到0.97），而提升干扰工具则导致崩溃。这种因果效应主要集中在大模型的最后四分之一层，证明了决策发生在读取阶段，而不是输入编码阶段。

最后，论文通过输入侧与读取侧干预的对比，进一步确认了瓶颈位置。输入侧干预（如重排或复制金标准工具）仅能恢复不到23%的失败，而读取侧干预（注意力偏置或残差流转向向量）能恢复59-91%。更重要的是，这两种不同表示层面的读取干预在恢复的失败案例上高度重叠（Jaccard指数0.865），表明瓶颈独立于具体表示，只与读取过程相关。

创新点在于：1）提出了注意力-分割分析框架，直接定位失败原因；2）实现了免训练的、无需金标的工具选择器，通过分段注意力即可在BFCL和Seal-Tools上关闭大部分金标与非金标之间的性能差距；3）通过双向剂量反应曲线证明了注意力的因果可控性。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了系统实验。实验设置包括：（1）在BFCL live_multiple和Seal-Tools两个真实基准测试上评估工具选择失败问题，使用150个任务×6个条件（共3600行）的关联实验，以及300个任务的诊断和修复实验。（2）对比方法包括输入侧干预（重排工具顺序、复制工具）和读出侧干预（注意力logit偏置、残差流引导向量、输出logit偏置），以及训练好的隐藏状态探针。主要结果：（1）在198个真实失败案例中，模型80%的情况下关注了正确工具（随机概率为21%），只有10%的失败源于对正确工具的忽视，直接反驳了“拥挤工具集/中间丢失”的解释。（2）读出侧干预可恢复59-91%的失败，而输入侧干预仅恢复16-18%。（3）因果剂量反应实验表明，增强黄金工具段注意力可将P(gold)从0.18提升至0.90，成功率从0.19提升至0.97，且效果集中在深层。（4）训练无关的黄金无关选择器在BFCL上提升+11.9点准确率（从0.780到0.899），在Seal-Tools上提升+14.9点（从0.759到0.907）。关键数据指标：注意力偏置和残差引导向量恢复重叠的Jaccard指数为0.865；AUROC分别在0.751（关联）和0.893（BFCL诊断）水平。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于：1) 当前方案仅聚焦于工具选择（function selection）而非参数填充（argument generation），无法解决工具调用中参数错误的场景；2) 缺乏多轮对话（multi-turn）的迁移验证，已有证据表明预决策信号在多轮中接近随机水平；3) 注意力因果性存在争议，部分实验依赖白盒注意力（闭源模型和Phi-3除外）；4) 置信门控虽能降低但无法完全消除干预伤害（13-9%残留错误）。

未来可探索方向包括：a) 将注意力-段落的诊断机制扩展到参数选择，例如结合工具定义中的参数锚点与输入实体进行交叉注意力分析；b) 设计多轮场景下的累积注意力衰减模型，利用历史对话中的工具选择轨迹作为先验；c) 开发无需白盒注意力的替代方法，例如利用输出logit的隐空间方向或激活修补（activation patching）来近似注意力效应；d) 构建自适应置信阈值，根据工具分布的动态变化（如长尾工具出现频率）动态调整门控参数，降低误判率；e) 探索将注意力诊断与强化学习结合，使模型在训练阶段就完善"看到即正确选择"的决策映射关系。

### Q6: 总结一下论文的主要内容

本文研究了LLM智能体在工具选择时的失败机制。核心发现令人惊讶：模型通常“看到了”正确的工具（在80%的失败案例中，模型对正确工具定义的注意力最高，远高于21%的随机概率），但仍然选择了错误的工具。这一结果直接反驳了直觉上的“拥挤工具架/中间迷失”解释。论文将此定位为“读头瓶颈”问题，即失败发生在模型从内部表征到输出决策的读取环节，而非输入阶段。方法上，作者通过测量每个候选工具定义上的注意力余量（attention margin），并利用两种不同的表征（注意力logit偏差和残差流引导向量）进行因果干预，证实了读头瓶颈的存在——两种干预手段恢复了大量相同的失败案例。通过无需训练的、无金标的注意力选择器，该方法在BFCL和Seal-Tools基准上显著提升了函数名选择精度。主要结论是：模型“看”与“选”之间存在分离，而注意力机制是一种可观测、可因果操纵并可用于无金标修复的关键信号。
